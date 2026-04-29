#!/usr/bin/env python3
import argparse
import datetime as dt
import html
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_FEED_URL = "https://think-ai.podigee.io/feed/mp3"
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
}


@dataclass(frozen=True)
class Episode:
    index: int
    title: str
    page_url: str
    image_url: str
    pub_date: str
    duration: str
    description: str
    audio_url: str
    guid: str
    audio_length: int


def text_of(node, path, default=""):
    found = node.find(path, NS)
    if found is None or found.text is None:
        return default
    return html.unescape(found.text).strip()


def fetch_bytes(url, timeout=60):
    request = urllib.request.Request(url, headers={"User-Agent": "ThinkDifferentThinkAI-transcriber/1.0"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def parse_feed(feed_url):
    root = ET.fromstring(fetch_bytes(feed_url))
    channel = root.find("channel")
    if channel is None:
        raise RuntimeError("RSS feed has no channel element")
    channel_image = channel.find("itunes:image", NS)
    fallback_image_url = ""
    if channel_image is not None:
        fallback_image_url = html.unescape(channel_image.attrib.get("href", "")).strip()

    episodes = []
    for index, item in enumerate(reversed(channel.findall("item")), start=1):
        enclosure = item.find("enclosure")
        if enclosure is None or not enclosure.attrib.get("url"):
            continue

        length = enclosure.attrib.get("length", "0")
        item_image = item.find("itunes:image", NS)
        image_url = fallback_image_url
        if item_image is not None:
            image_url = html.unescape(item_image.attrib.get("href", "")).strip() or fallback_image_url
        episodes.append(
            Episode(
                index=index,
                title=text_of(item, "title", "Untitled episode"),
                page_url=text_of(item, "link"),
                image_url=image_url,
                pub_date=text_of(item, "pubDate"),
                duration=text_of(item, "itunes:duration"),
                description=text_of(item, "content:encoded") or text_of(item, "description"),
                audio_url=enclosure.attrib["url"],
                guid=text_of(item, "guid"),
                audio_length=int(length) if length.isdigit() else 0,
            )
        )
    return episodes


def clean_html(value):
    value = html.unescape(value or "")
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.IGNORECASE)
    value = re.sub(r"</p\s*>", "\n\n", value, flags=re.IGNORECASE)
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"\n{3,}", "\n\n", value)
    return value.strip()


def apply_known_transcript_corrections(value):
    return re.sub(r"\bMarc\b", "Mark", value)


def safe_filename(episode):
    title = html.unescape(episode.title).strip()
    title = title.replace("/", "-").replace("\\", "-").replace(":", " -")
    title = re.sub(r'[<>|?*"\x00-\x1f]', "", title)
    title = re.sub(r"\s+", " ", title).strip(" .")
    return f"{episode.index:03d} - {title or 'Untitled episode'}.md"


def timestamp(seconds):
    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def download_episode(episode, audio_dir):
    from tqdm import tqdm

    audio_dir.mkdir(parents=True, exist_ok=True)
    extension = Path(urlparse(episode.audio_url).path).suffix or ".mp3"
    audio_path = audio_dir / f"{episode.index:03d}{extension}"
    if audio_path.exists() and (episode.audio_length == 0 or audio_path.stat().st_size == episode.audio_length):
        return audio_path

    part_path = audio_path.with_suffix(audio_path.suffix + ".part")
    request = urllib.request.Request(episode.audio_url, headers={"User-Agent": "ThinkDifferentThinkAI-transcriber/1.0"})
    for attempt in range(1, 4):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                total = int(response.headers.get("Content-Length") or episode.audio_length or 0)
                with part_path.open("wb") as handle:
                    with tqdm(total=total, unit="B", unit_scale=True, desc=f"Download {episode.index:03d}") as progress:
                        while True:
                            chunk = response.read(1024 * 1024)
                            if not chunk:
                                break
                            handle.write(chunk)
                            progress.update(len(chunk))
            part_path.replace(audio_path)
            return audio_path
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt == 3:
                raise
            time.sleep(attempt * 5)

    raise RuntimeError(f"Download failed for episode {episode.index}")


def write_markdown(episode, transcript_path, segments, info, feed_url, model_size):
    transcript_path.parent.mkdir(parents=True, exist_ok=True)
    title = episode.title.replace('"', "'")
    transcribed_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    language = getattr(info, "language", "")
    language_probability = getattr(info, "language_probability", "")
    description = apply_known_transcript_corrections(clean_html(episode.description))

    lines = [
        "---",
        f'title: "{title}"',
        f"episode_index: {episode.index}",
        f'published: "{episode.pub_date}"',
        f'duration: "{episode.duration}"',
        f'page_url: "{episode.page_url}"',
        f'image_url: "{episode.image_url}"',
        f'audio_url: "{episode.audio_url}"',
        f'guid: "{episode.guid}"',
        f'source_feed: "{feed_url}"',
        f'whisper_model: "{model_size}"',
        f'language: "{language}"',
        f'language_probability: "{language_probability}"',
        f'transcribed_at: "{transcribed_at}"',
        "---",
        "",
        f"# {episode.title}",
        "",
    ]

    if episode.pub_date:
        lines.append(f"**Veröffentlicht:** {episode.pub_date}")
    if episode.duration:
        lines.append(f"**Dauer:** {episode.duration}")
    if episode.page_url:
        lines.append(f"**Webplayer:** {episode.page_url}")
    if episode.image_url:
        lines.append(f"**Cover:** {episode.image_url}")
    lines.append(f"**Audio:** {episode.audio_url}")
    lines.append("")

    if description:
        lines.extend(["## Beschreibung", "", description, ""])

    lines.extend(["## Transkript", ""])
    for segment in segments:
        text = apply_known_transcript_corrections(segment.text.strip())
        if text:
            lines.append(f"**[{timestamp(segment.start)}]** {text}")
            lines.append("")

    transcript_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def transcribe_episode(args):
    from faster_whisper import WhisperModel

    episodes = parse_feed(args.feed_url)
    selected = [episode for episode in episodes if episode.index == args.episode_index]
    if not selected:
        raise SystemExit(f"Episode index {args.episode_index} not found in feed with {len(episodes)} episodes")

    episode = selected[0]
    transcript_path = Path(args.output_dir) / safe_filename(episode)
    if transcript_path.exists() and not args.force:
        print(f"Transcript already exists: {transcript_path}")
        return

    print(f"Transcribing {episode.index:03d}: {episode.title}")
    audio_path = download_episode(episode, Path(args.audio_dir))
    model = WhisperModel(args.model_size, device=args.device, compute_type=args.compute_type)
    segments_iter, info = model.transcribe(
        str(audio_path),
        language=args.language,
        vad_filter=True,
        beam_size=args.beam_size,
        condition_on_previous_text=False,
    )
    write_markdown(episode, transcript_path, list(segments_iter), info, args.feed_url, args.model_size)
    print(f"Wrote {transcript_path}")


def build_parser():
    parser = argparse.ArgumentParser(description="Transcribe one episode from the Think AI podcast feed.")
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--episode-index", type=int, required=True)
    parser.add_argument("--output-dir", default="transkripte")
    parser.add_argument("--audio-dir", default=".audio-cache")
    parser.add_argument("--model-size", default="small")
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--compute-type", default="int8")
    parser.add_argument("--language", default="de")
    parser.add_argument("--beam-size", type=int, default=5)
    parser.add_argument("--force", action="store_true")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    transcribe_episode(args)


if __name__ == "__main__":
    sys.exit(main())
