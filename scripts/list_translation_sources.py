#!/usr/bin/env python3
import argparse
import re
from pathlib import Path


EPISODE_RE = re.compile(r"^(\d+)\s+-\s+")


def episode_number(path):
    match = EPISODE_RE.match(path.name)
    return int(match.group(1)) if match else 0


def error_path_for(source_path, error_dir):
    return error_dir / f"{source_path.name}.json"


def parse_priority(value):
    result = []
    for item in value.split(","):
        item = item.strip()
        if not item:
            continue
        try:
            result.append(int(item))
        except ValueError:
            raise SystemExit(f"Invalid priority episode number: {item}")
    return result


def source_sort_key(path):
    return (-episode_number(path), path.name)


def main():
    parser = argparse.ArgumentParser(description="List transcript source files needing English translation.")
    parser.add_argument("--input-dir", default="transkripte")
    parser.add_argument("--output-dir", default="transkripte-en")
    parser.add_argument("--error-dir", default="transkripte-en/.errors")
    parser.add_argument("--priority", default="")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    error_dir = Path(args.error_dir)
    priority = parse_priority(args.priority)

    sources = sorted(input_dir.glob("*.md"), key=source_sort_key)
    pending = [
        path
        for path in sources
        if not (output_dir / path.name).exists() or error_path_for(path, error_dir).exists()
    ]

    by_number = {episode_number(path): path for path in pending}
    ordered = []
    seen = set()

    for number in priority:
        path = by_number.get(number)
        if path and path not in seen:
            ordered.append(path)
            seen.add(path)

    errored = sorted(
        [path for path in pending if error_path_for(path, error_dir).exists() and path not in seen],
        key=lambda path: (episode_number(path), path.name),
    )
    ordered.extend(errored)
    seen.update(errored)

    ordered.extend(path for path in pending if path not in seen)

    for path in ordered:
        print(path.as_posix())


if __name__ == "__main__":
    main()
