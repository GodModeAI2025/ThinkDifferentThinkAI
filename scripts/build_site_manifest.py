#!/usr/bin/env python3
import argparse
import json
import re
import unicodedata
import sys
from pathlib import Path

from transcribe_episode import (DEFAULT_FEED_URL, clean_html, parse_feed,
                                safe_filename)


def transcript_item(path):
    available = path.exists()
    return {
        "available": available,
        "path": str(path).replace("\\", "/") if available else "",
    }


def _titelkern(text):
    """Vergleichsform eines Titels: nur Buchstaben und Ziffern, NFC-normalisiert.

    macOS legt Dateinamen zerlegt ab (u + Trema), der Feed liefert sie zusammen-
    gesetzt; dazu verliert der Dateiname Zeichen wie ? und !.
    """
    text = unicodedata.normalize("NFC", text or "")
    return re.sub(r"[^0-9a-zà-ÿ]+", "", text.casefold())


def transcript_path_for(transcript_dir, episode):
    exact_path = transcript_dir / safe_filename(episode)
    if exact_path.exists():
        return exact_path
    # Ueber den Titel suchen, nicht ueber die Nummer. Dateinummer und Folgennummer
    # fallen bei elf Altfaellen auseinander (018/019, 033-039, 041/043); ein Glob auf
    # die Nummer liefert dort die Datei der *anderen* Folge, und die Folgenseite zeigt
    # dann ein fremdes Transkript. Der Titel ist eindeutig.
    if transcript_dir.is_dir():
        gesucht = _titelkern(episode.title)
        for kandidat in sorted(transcript_dir.glob("*.md")):
            if _titelkern(re.sub(r"^\d{3} - ", "", kandidat.stem)) == gesucht:
                # NFC, denn macOS liefert den Namen zerlegt zurueck, Git haelt ihn
                # zusammengesetzt. Aus dem Pfad wird der GitHub-Link auf der
                # Folgenseite gebaut, und die zerlegte Form gibt dort 404.
                return Path(unicodedata.normalize("NFC", str(kandidat)))
    return exact_path


def embed_url_for(page_url):
    if not page_url:
        return ""
    return f"{page_url.rstrip('/')}/embed?context=external"


def build_manifest(feed_url, transcript_dir, english_transcript_dir):
    episodes = parse_feed(feed_url)
    items = []
    for episode in episodes:
        transcript_path = transcript_path_for(transcript_dir, episode)
        english_transcript_path = transcript_path_for(english_transcript_dir, episode)
        german_transcript = transcript_item(transcript_path)
        english_transcript = transcript_item(english_transcript_path)
        items.append(
            {
                "index": episode.index,
                "title": episode.title,
                "published": episode.pub_date,
                "duration": episode.duration,
                "pageUrl": episode.page_url,
                "embedUrl": embed_url_for(episode.page_url),
                "imageUrl": episode.image_url,
                "audioUrl": episode.audio_url,
                # Beschreibung frisch aus dem Feed, nicht aus dem Transkript.
                # Im Transkript steht ein Schnappschuss vom Tag der Transkription;
                # spaetere Korrekturen bei Podigee kaemen dort nie an. Genau so ist
                # "Stephane Kempf" auf der Webseite stehen geblieben, obwohl Podigee
                # laengst "Stephan Kempf" sagt.
                "description": clean_html(episode.description),
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
    parser.add_argument("--output", default="docs/data/episodes.json")
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
