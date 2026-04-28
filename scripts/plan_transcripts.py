#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

from transcribe_episode import DEFAULT_FEED_URL, parse_feed


def transcript_exists(output_dir, episode_index):
    return any(output_dir.glob(f"{episode_index:03d} - *.md"))


def write_github_output(path, values):
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def build_parser():
    parser = argparse.ArgumentParser(description="Create a GitHub Actions matrix for missing podcast transcripts.")
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--output-dir", default="transkripte")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--github-output", default="")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    output_dir = Path(args.output_dir)
    episodes = parse_feed(args.feed_url)

    selected = []
    for episode in episodes:
        if args.force or not transcript_exists(output_dir, episode.index):
            selected.append({"episode": episode.index})

    matrix = json.dumps({"include": selected}, separators=(",", ":"))
    outputs = {
        "episode_count": str(len(episodes)),
        "selected_count": str(len(selected)),
        "has_work": "true" if selected else "false",
        "matrix": matrix,
    }

    print(f"Feed episodes: {len(episodes)}")
    print(f"Episodes to transcribe: {len(selected)}")
    if selected:
        print("Selected: " + ", ".join(f"{item['episode']:03d}" for item in selected))
    write_github_output(args.github_output, outputs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
