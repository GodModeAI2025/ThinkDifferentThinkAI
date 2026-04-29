#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_LOCAL_MODEL = "Helsinki-NLP/opus-mt-de-en"
DEFAULT_OPENAI_MODEL = "gpt-4o-mini"
DEFAULT_OPENAI_CHUNK_MAX_CHARS = 12000
DEFAULT_OPENAI_CHUNK_MAX_LINES = 180
DEFAULT_OPENAI_MAX_OUTPUT_TOKENS = 12000
OPENAI_RESPONSES_URL = "https://api.openai.com/v1/responses"
TIMESTAMP_RE = re.compile(r"^(\*\*\[\d\d:\d\d:\d\d\]\*\*\s*)(.*)$")
TIMESTAMP_MARKER_RE = re.compile(r"\*\*\[\d\d:\d\d:\d\d\]\*\*")
URL_RE = re.compile(r"https?://[^\s)>\"]+")
META_LABELS = {
    "Veröffentlicht": "Published",
    "Dauer": "Duration",
    "Webplayer": "Web player",
    "Cover": "Cover",
    "Audio": "Audio",
}
HEADINGS = {
    "Beschreibung": "Description",
    "Transkript": "Transcript",
}


class LocalTranslator:
    def __init__(self, model_name, batch_size):
        from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

        self.model_name = model_name
        self.batch_size = batch_size
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate_many(self, values):
        import torch

        results = []
        self.model.eval()
        for start in range(0, len(values), self.batch_size):
            batch = values[start : start + self.batch_size]
            inputs = self.tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=512)
            with torch.no_grad():
                outputs = self.model.generate(**inputs, max_new_tokens=512)
            results.extend(self.tokenizer.batch_decode(outputs, skip_special_tokens=True))
        return results


class OpenAITranslator:
    def __init__(
        self,
        model_name,
        batch_size,
        api_key,
        max_retries=3,
        chunk_max_chars=DEFAULT_OPENAI_CHUNK_MAX_CHARS,
        chunk_max_lines=DEFAULT_OPENAI_CHUNK_MAX_LINES,
        max_output_tokens=DEFAULT_OPENAI_MAX_OUTPUT_TOKENS,
    ):
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is required for --provider openai")
        self.model_name = model_name
        self.batch_size = batch_size
        self.api_key = api_key
        self.max_retries = max_retries
        self.chunk_max_chars = chunk_max_chars
        self.chunk_max_lines = chunk_max_lines
        self.max_output_tokens = max_output_tokens

    def request_json(self, payload):
        data = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            OPENAI_RESPONSES_URL,
            data=data,
            method="POST",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
        )

        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                with urllib.request.urlopen(request, timeout=120) as response:
                    return json.loads(response.read().decode("utf-8"))
            except urllib.error.HTTPError as error:
                detail = safe_error_body(error)
                last_error = RuntimeError(f"OpenAI HTTP {error.code}: {detail}")
                if error.code in {400, 401, 402, 403, 404}:
                    break
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, RuntimeError) as error:
                last_error = error
            if attempt < self.max_retries:
                time.sleep(attempt * 3)
        raise last_error or RuntimeError("OpenAI translation failed")

    def translate_many(self, values):
        results = []
        for start in range(0, len(values), self.batch_size):
            batch = values[start : start + self.batch_size]
            try:
                results.extend(self.translate_batch(batch))
            except TranslationCountError:
                if len(batch) == 1:
                    raise
                for value in batch:
                    results.extend(self.translate_batch([value]))
        return results

    def translate_batch(self, values):
        payload = {
            "model": self.model_name,
            "instructions": (
                "Translate the given German podcast transcript strings to natural English. "
                "Return only JSON matching the schema. Preserve Markdown markers, timestamps, URLs, "
                "brand names, speaker names Mark Zimmermann and Jens Scharnetzki, and technical product names."
            ),
            "input": json.dumps(values, ensure_ascii=False),
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "translation_batch",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "translations": {
                                "type": "array",
                                "items": {"type": "string"},
                            }
                        },
                        "required": ["translations"],
                    },
                }
            },
        }
        body = self.request_json(payload)
        output_text = extract_openai_output_text(body)
        parsed = json.loads(output_text)
        translations = parsed.get("translations", [])
        if len(translations) != len(values):
            raise TranslationCountError(f"Expected {len(values)} translations, got {len(translations)}")
        return translations

    def translate_body_lines(self, lines):
        normalized_lines = normalize_static_markdown_lines(lines)
        translated = []
        chunks = list(chunk_lines(normalized_lines, self.chunk_max_chars, self.chunk_max_lines))
        for index, chunk in enumerate(chunks, start=1):
            print(f"Translating chunk {index}/{len(chunks)} ({len(chunk)} lines)", flush=True)
            translated.extend(self.translate_markdown_lines_with_fallback(chunk))
        return translated

    def translate_markdown_lines_with_fallback(self, lines):
        try:
            return self.translate_markdown_chunk(lines)
        except MarkdownValidationError:
            if len(lines) <= 1:
                raise
            middle = len(lines) // 2
            return self.translate_markdown_lines_with_fallback(lines[:middle]) + self.translate_markdown_lines_with_fallback(
                lines[middle:]
            )

    def translate_markdown_chunk(self, lines):
        if not any(line.strip() for line in lines):
            return lines
        payload = {
            "model": self.model_name,
            "instructions": (
                "Translate each German podcast transcript Markdown line to natural English. "
                "Return exactly the same number of lines in the same order. Preserve blank lines, Markdown structure, "
                "every timestamp marker like **[00:00:00]**, URLs, code-like tokens, brand names, and speaker names "
                "Mark Zimmermann and Jens Scharnetzki. Do not add timestamps to lines that do not already have them. "
                "Do not add commentary, summaries, or new sections. Return only JSON matching the schema."
            ),
            "input": json.dumps({"lines": lines}, ensure_ascii=False),
            "max_output_tokens": self.max_output_tokens,
            "text": {
                "format": {
                    "type": "json_schema",
                    "name": "markdown_line_translation",
                    "strict": True,
                    "schema": {
                        "type": "object",
                        "additionalProperties": False,
                        "properties": {
                            "lines": {
                                "type": "array",
                                "items": {"type": "string"},
                            },
                        },
                        "required": ["lines"],
                    },
                }
            },
        }
        body = self.request_json(payload)
        try:
            parsed = json.loads(extract_openai_output_text(body))
        except json.JSONDecodeError as error:
            raise MarkdownValidationError(f"OpenAI response was not valid JSON: {error}") from error

        translated_lines = parsed.get("lines", [])
        if not isinstance(translated_lines, list) or not all(isinstance(line, str) for line in translated_lines):
            raise MarkdownValidationError("OpenAI response did not include translated lines")
        if len(translated_lines) != len(lines):
            raise MarkdownValidationError(f"Line count mismatch: expected {len(lines)}, got {len(translated_lines)}")
        for source_line, translated_line in zip(lines, translated_lines):
            validate_preserved_markers(source_line, translated_line)
        return translated_lines


class TranslationCountError(RuntimeError):
    pass


class MarkdownValidationError(RuntimeError):
    pass


def safe_error_body(error):
    try:
        body = error.read().decode("utf-8")
    except Exception:
        return str(error)
    body = re.sub(r"sk-[A-Za-z0-9_-]+", "[redacted]", body)
    return body[:1000]


def extract_openai_output_text(body):
    if isinstance(body.get("output_text"), str):
        return body["output_text"]
    chunks = []
    for item in body.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text" and isinstance(content.get("text"), str):
                chunks.append(content["text"])
    if chunks:
        return "".join(chunks)
    raise RuntimeError("OpenAI response did not include output text")


def split_frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [], lines
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[: index + 1], lines[index + 1 :]
    return [], lines


def translate_frontmatter(lines, source_path, model_name, provider):
    translated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    result = []
    inserted = False
    for line in lines:
        if line.startswith("language:"):
            result.append('language: "en"')
            continue
        if line.strip() == "---" and not inserted and result:
            result.extend(
                [
                    'translated_from_language: "de"',
                    f'translation_provider: "{provider}"',
                    f'translation_model: "{model_name}"',
                    f'translated_from_file: "{source_path.as_posix()}"',
                    f'translated_at: "{translated_at}"',
                ]
            )
            inserted = True
        result.append(line)
    return result


def is_translatable(line):
    stripped = line.strip()
    if not stripped:
        return False
    if re.match(r"^https?://", stripped):
        return False
    if re.match(r"^\*\*(Webplayer|Cover|Audio):\*\*\s+https?://", stripped):
        return False
    return True


def normalize_static_markdown_lines(lines):
    normalized = []
    for line in lines:
        heading = re.match(r"^(#+)\s+(.+)$", line)
        if heading:
            level, text = heading.groups()
            normalized.append(f"{level} {HEADINGS.get(text, text)}")
            continue

        meta = re.match(r"^\*\*([^:]+):\*\*\s*(.*)$", line)
        if meta:
            label, value = meta.groups()
            normalized.append(f"**{META_LABELS.get(label, label)}:** {value}".rstrip())
            continue

        normalized.append(line)
    return normalized


def chunk_lines(lines, max_chars, max_lines):
    chunk = []
    chunk_chars = 0
    for line in lines:
        line_chars = len(line) + 1
        if chunk and (chunk_chars + line_chars > max_chars or len(chunk) >= max_lines):
            yield chunk
            chunk = []
            chunk_chars = 0
        chunk.append(line)
        chunk_chars += line_chars
    if chunk:
        yield chunk


def validate_preserved_markers(source, translated):
    source_timestamps = TIMESTAMP_MARKER_RE.findall(source)
    translated_timestamps = TIMESTAMP_MARKER_RE.findall(translated)
    if source_timestamps != translated_timestamps:
        raise MarkdownValidationError(
            f"Timestamp mismatch: expected {len(source_timestamps)}, got {len(translated_timestamps)}"
        )

    source_urls = URL_RE.findall(source)
    translated_urls = URL_RE.findall(translated)
    if source_urls != translated_urls:
        raise MarkdownValidationError(f"URL mismatch: expected {len(source_urls)}, got {len(translated_urls)}")


def prepare_body(lines):
    prepared = []
    texts = []
    for line in lines:
        timestamp = TIMESTAMP_RE.match(line)
        if timestamp:
            prefix, text = timestamp.groups()
            if text.strip():
                prepared.append(("translate_with_prefix", prefix, len(texts)))
                texts.append(text)
            else:
                prepared.append(("raw", line))
            continue

        heading = re.match(r"^(#+)\s+(.+)$", line)
        if heading:
            level, text = heading.groups()
            mapped = HEADINGS.get(text)
            if mapped:
                prepared.append(("raw", f"{level} {mapped}"))
            else:
                prepared.append(("translate_with_prefix", f"{level} ", len(texts)))
                texts.append(text)
            continue

        meta = re.match(r"^\*\*([^:]+):\*\*\s*(.*)$", line)
        if meta:
            label, value = meta.groups()
            translated_label = META_LABELS.get(label, label)
            if value and is_translatable(value):
                prepared.append(("translate_meta", translated_label, len(texts)))
                texts.append(value)
            else:
                prepared.append(("raw", f"**{translated_label}:** {value}".rstrip()))
            continue

        if is_translatable(line):
            prepared.append(("translate", len(texts)))
            texts.append(line)
        else:
            prepared.append(("raw", line))
    return prepared, texts


def render_body(prepared, translations):
    lines = []
    for item in prepared:
        kind = item[0]
        if kind == "raw":
            lines.append(item[1])
        elif kind == "translate":
            lines.append(translations[item[1]])
        elif kind == "translate_with_prefix":
            lines.append(f"{item[1]}{translations[item[2]]}")
        elif kind == "translate_meta":
            lines.append(f"**{item[1]}:** {translations[item[2]]}")
    return lines


def error_path_for(source_path, error_dir):
    return error_dir / f"{source_path.name}.json"


def write_error(error_path, source_path, error):
    error_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "source": source_path.as_posix(),
        "failedAt": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "error": str(error)[:2000],
    }
    error_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def translate_file(source_path, target_path, error_path, translator, provider, force=False):
    if target_path.exists() and not force and not error_path.exists():
        return "skipped"

    frontmatter, body = split_frontmatter(source_path.read_text(encoding="utf-8"))
    translated_frontmatter = (
        translate_frontmatter(frontmatter, source_path, translator.model_name, provider) if frontmatter else []
    )
    if hasattr(translator, "translate_body_lines"):
        translated_body = translator.translate_body_lines(body)
    else:
        prepared, texts = prepare_body(body)
        translations = translator.translate_many(texts) if texts else []
        translated_body = render_body(prepared, translations)

    target_path.parent.mkdir(parents=True, exist_ok=True)
    output_lines = translated_frontmatter + translated_body
    target_path.write_text("\n".join(output_lines).rstrip() + "\n", encoding="utf-8")
    if error_path.exists():
        error_path.unlink()
    return "translated"


def build_translator(args):
    if args.provider == "openai":
        model = args.model or os.environ.get("OPENAI_TRANSLATION_MODEL") or DEFAULT_OPENAI_MODEL
        return OpenAITranslator(
            model,
            args.batch_size,
            os.environ.get("OPENAI_API_KEY", ""),
            chunk_max_chars=args.chunk_max_chars,
            chunk_max_lines=args.chunk_max_lines,
            max_output_tokens=args.max_output_tokens,
        )
    model = args.model or DEFAULT_LOCAL_MODEL
    return LocalTranslator(model, args.batch_size)


def build_parser():
    parser = argparse.ArgumentParser(description="Translate German podcast transcript Markdown files to English.")
    parser.add_argument("--input-dir", default="transkripte")
    parser.add_argument("--output-dir", default="transkripte-en")
    parser.add_argument("--error-dir", default="transkripte-en/.errors")
    parser.add_argument("--source-file", action="append", default=[])
    parser.add_argument("--provider", choices=["local", "openai"], default="local")
    parser.add_argument("--model", default="")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--chunk-max-chars", type=int, default=DEFAULT_OPENAI_CHUNK_MAX_CHARS)
    parser.add_argument("--chunk-max-lines", type=int, default=DEFAULT_OPENAI_CHUNK_MAX_LINES)
    parser.add_argument("--max-output-tokens", type=int, default=DEFAULT_OPENAI_MAX_OUTPUT_TOKENS)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--max-errors", type=int, default=5)
    parser.add_argument("--fail-on-error", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    error_dir = Path(args.error_dir)
    source_files = [Path(path) for path in args.source_file] if args.source_file else sorted(input_dir.glob("*.md"))
    if args.limit:
        source_files = source_files[: args.limit]
    retry_files = [
        path
        for path in source_files
        if args.force or not (output_dir / path.name).exists() or error_path_for(path, error_dir).exists()
    ]
    if not retry_files:
        print("No missing or previously failed English transcript translations.")
        return 0

    translator = build_translator(args)
    changed = 0
    errors = 0
    for source_path in retry_files:
        print(f"Translating {source_path}", flush=True)
        target_path = output_dir / source_path.name
        error_path = error_path_for(source_path, error_dir)
        try:
            result = translate_file(source_path, target_path, error_path, translator, args.provider, force=args.force)
            if result == "translated":
                changed += 1
                print(f"Wrote {target_path}", flush=True)
        except Exception as error:
            errors += 1
            write_error(error_path, source_path, error)
            print(f"Translation failed for {source_path}: {error}", file=sys.stderr, flush=True)
            if errors >= args.max_errors:
                print(
                    f"Stopped after {errors} translation error(s). Later runs will retry missing files.",
                    file=sys.stderr,
                    flush=True,
                )
                break

    print(f"Translated {changed} transcript file(s). Recorded {errors} error(s).", flush=True)
    if errors and args.fail_on_error:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
