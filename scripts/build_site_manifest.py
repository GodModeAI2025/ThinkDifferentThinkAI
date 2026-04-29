#!/usr/bin/env python3
import argparse
import json
import sys
from pathlib import Path

from transcribe_episode import DEFAULT_FEED_URL, parse_feed, safe_filename


def transcript_item(path):
    available = path.exists()
    return {
        "available": available,
        "path": str(path).replace("\\", "/") if available else "",
    }


def build_manifest(feed_url, transcript_dir, english_transcript_dir):
    episodes = parse_feed(feed_url)
    items = []
    for episode in episodes:
        transcript_path = transcript_dir / safe_filename(episode)
        english_transcript_path = english_transcript_dir / safe_filename(episode)
        german_transcript = transcript_item(transcript_path)
        english_transcript = transcript_item(english_transcript_path)
        items.append(
            {
                "index": episode.index,
                "title": episode.title,
                "published": episode.pub_date,
                "duration": episode.duration,
                "pageUrl": episode.page_url,
                "imageUrl": episode.image_url,
                "audioUrl": episode.audio_url,
                "transcriptAvailable": german_transcript["available"],
                "transcriptPath": german_transcript["path"],
                "englishTranscriptAvailable": english_transcript["available"],
                "englishTranscriptPath": english_transcript["path"],
                "transcripts": {
                    "de": german_transcript,
                    "en": english_transcript,
                },
            }
        )

    return {
        "feedUrl": feed_url,
        "generatedAt": "",
        "episodeCount": len(items),
        "availableTranscriptCount": sum(1 for item in items if item["transcriptAvailable"]),
        "availableEnglishTranscriptCount": sum(1 for item in items if item["englishTranscriptAvailable"]),
        "episodes": items,
    }


def build_parser():
    parser = argparse.ArgumentParser(description="Build static landing page data for podcast transcripts.")
    parser.add_argument("--feed-url", default=DEFAULT_FEED_URL)
    parser.add_argument("--transcript-dir", default="transkripte")
    parser.add_argument("--english-transcript-dir", default="transkripte-en")
    parser.add_argument("--output", default="site/data/episodes.json")
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    manifest = build_manifest(args.feed_url, Path(args.transcript_dir), Path(args.english_transcript_dir))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {output} with {manifest['availableTranscriptCount']} German and "
        f"{manifest['availableEnglishTranscriptCount']} English transcripts of {manifest['episodeCount']} episodes."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
