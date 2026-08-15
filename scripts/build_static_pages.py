#!/usr/bin/env python3
"""Erzeugt statische, indexierbare Seiten je Folge und Sprache.

Die Single-Page-App unter docs/index.html bleibt als Such- und Blaetteroberflaeche
bestehen. Dieses Skript legt daneben fuer jede Folge eine eigene URL an, in der der
komplette Transkripttext bereits im ausgelieferten HTML steht:

    docs/de/<slug>/index.html
    docs/en/<slug>/index.html
    docs/themen/<thema>/index.html
    docs/gaeste/index.html, docs/gaeste/<slug>/index.html
    docs/sitemap.xml, docs/robots.txt, docs/llms.txt

Der Slug stammt aus page_url im Frontmatter und entspricht damit dem Podigee-Slug.
Die Dateinummer der Transkripte wird bewusst nicht als Folgennummer verwendet,
weil beide Nummerierungen auseinanderfallen.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
import unicodedata
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import blog  # noqa: E402  (liegt neben dieser Datei)

DEFAULT_BASE_URL = "https://godmodeai2025.github.io/ThinkDifferentThinkAI"
SERIES_NAME = "Think Different. Think AI."
SERIES_URL = "https://think-ai.podigee.io/"
FEED_URL = "https://think-ai.podigee.io/feed/mp3"
SOURCE_REPO = "https://github.com/GodModeAI2025/ThinkDifferentThinkAI"

HOSTS = [
    {"name": "Mark Zimmermann", "sameAs": "https://www.linkedin.com/in/mark-zimmermann-5a005123/"},
    {"name": "Jens Scharnetzki", "sameAs": "https://www.linkedin.com/in/scharnetzki/"},
]

STRINGS = {
    "de": {
        "lang": "de",
        "other": "en",
        "transcript_heading": "Transkript",
        "description_heading": "Worum es geht",
        "title_suffix": "Transkript",
        "back": "Alle Folgen",
        "listen": "Folge anhören",
        "markdown": "Als Markdown",
        "prev": "Vorherige Folge",
        "next": "Nächste Folge",
        "switch": "Read in English",
        "published": "Veröffentlicht",
        "duration": "Dauer",
        "topics": "Themen",
        "guests": "Zu Gast",
        "no_other": "Diese Folge liegt nur auf Deutsch vor.",
        "archive_title": "Transkriptarchiv",
        "toc": "Zeitmarken",
    },
    "en": {
        "lang": "en",
        "other": "de",
        "transcript_heading": "Transcript",
        "description_heading": "What it is about",
        "title_suffix": "Transcript",
        "back": "All episodes",
        "listen": "Listen to the episode",
        "markdown": "As Markdown",
        "prev": "Previous episode",
        "next": "Next episode",
        "switch": "Auf Deutsch lesen",
        "published": "Published",
        "duration": "Duration",
        "topics": "Topics",
        "guests": "Guest",
        "no_other": "This episode is only available in German.",
        "archive_title": "Transcript archive",
        "toc": "Timestamps",
    },
}

TOPICS = [
    {
        "slug": "ki-agenten",
        "name": "KI-Agenten",
        "intro": "Agenten handeln, statt nur zu antworten. Diese Folgen behandeln Agent-Harnesses, "
                 "MCP als Schnittstelle, Multi-Agenten-Setups und die Frage, wer sie eigentlich führt.",
        "keywords": ["agent harness", "harness", "mcp", "multiagent", "multi-agent", "agent client protocol", "openclaw", "clawdbot", "orchestrier", "agentic", "loop engineering", "agentennetz", "kill-switch", "guardrail", "kiagent", "ki-agent"],
    },
    {
        "slug": "ki-sicherheit",
        "name": "KI-Sicherheit",
        "intro": "Prompt Injection, Voice Cloning, Exploits aus Sicherheitspatches: Was passiert, wenn "
                 "man einem Modell Rechte gibt, und wie Angriffe darauf konkret aussehen.",
        "keywords": ["prompt injection", "voice cloning", "deepfake", "exploit", "schadsoftware", "malware", "angriffsflaeche", "angriffsfläche", "ceo-fraud", "social engineering", "darknet", "sandbox", "threat model", "pentest", "backdoor", "sicherheitsluecke", "sicherheitslücke", "phishing", "betrug"],
    },
    {
        "slug": "automatisierung-und-tools",
        "name": "Automatisierung und Tools",
        "intro": "Notion, n8n, Workflows und die Werkzeuge dahinter. Folgen darüber, wie aus einer "
                 "Notiz ein Ticket, eine Folie und ein Post wird.",
        "keywords": ["notion", "n8n", "zapier", "workflow", "worker", "trigger", "building block", "automatisierung", "werkzeugkette", "integration"],
    },
    {
        "slug": "recht-und-regulierung",
        "name": "Recht und Regulierung",
        "intro": "AI Act, Datenschutz und Haftung. Wer verantwortet, was ein Agent tut, und was "
                 "Datenschutz tatsaechlich erlaubt.",
        "keywords": ["ai act", "dsgvo", "datenschutz", "jurist", "haftung", "rechtsgut", "compliance", "gesetzgeb", "anwalt", "urteil", "verordnung", "betreiber", "regulierung"],
    },
    {
        "slug": "robotik",
        "name": "Robotik",
        "intro": "KI bekommt einen Körper. Humanoide, Teleoperation und der Abstand zwischen "
                 "Werbevideo und Wohnzimmer.",
        "keywords": ["roboter", "robotik", "humanoid", "optimus", "boston dynamics", "teleoperation", "greifer", "saugroboter", "droide"],
    },
    {
        "slug": "wissensmanagement",
        "name": "Wissensmanagement",
        "intro": "Second Brain, RAG, Ontologien und portable Skills. Wie Wissen außerhalb des "
                 "Modells liegen bleibt und trotzdem auffindbar ist.",
        "keywords": ["second brain", "obsidian", "retrieval", "ontologie", "vault", "exokortex", "wissensspeicher", "digest", "kuration", "notizen", "transkript", "skill"],
    },
    {
        "slug": "softwareentwicklung",
        "name": "Softwareentwicklung",
        "intro": "Vibe Coding, Spec-Driven Development und Agenten, die committen. Was sich in der "
                 "täglichen Entwicklungsarbeit tatsaechlich veraendert hat.",
        "keywords": ["vibe coding", "claude code", "spec-driven", "refactor", "commit", "pull request", "codebasis", "softwareentwicklung", "entwickler", "testcase", "adr", "programmier", "code"],
    },
    {
        "slug": "modelle-und-anbieter",
        "name": "Modelle und Anbieter",
        "intro": "Wer welches Modell baut, was es kostet und wer es benutzen darf. Von offenen "
                 "Gewichten aus China über Tokenrechnungen bis zu dem Tag, an dem ein Modell fuer "
                 "Nicht-US-Bürger gesperrt wurde und Kanzleien ihre Textanalyse schon darauf "
                 "gebaut hatten.",
        "keywords": ["open weights", "offene gewichte", "kimi", "moonshot", "deepseek", "exportkontrolle", "gesperrt", "souveraenitaet", "souveränität", "frontier", "benchmark", "lizenz", "modellauswahl", "destillation", "parameter", "anbieter", "abo"],
    },
    {
        "slug": "interfaces-und-interaktion",
        "name": "Interfaces und Interaktion",
        "intro": "Wie man mit etwas arbeitet, das nicht antwortet wie ein Programm. Wartezeit als "
                 "Designfrage, Sprache statt Bildschirm, Browser als Agent, und die Frage, wie ein "
                 "Mensch mehrere Agenten gleichzeitig im Blick behaelt.",
        "keywords": ["interface", "oberflaeche", "oberfläche", "voice first", "sprachsteuerung", "chatfenster", "wartezeit", "ladebalken", "smart glasses", "temporal ux", "bedienkonzept", "usability", "browser", "sprachassistent"],
    },
    {
        "slug": "fuehrung-und-arbeit",
        "name": "Führung und Arbeit",
        "intro": "Was mit Organisationen passiert, wenn Agenten Teil des Teams werden. Hierarchien, "
                 "Verantwortung und die Frage, wo Berufsanfänger noch lernen.",
        "keywords": ["fuehrung", "führung", "hierarchie", "org-chart", "organigramm", "mitarbeitende", "new work", "berufsanfaenger", "berufsanfänger", "teamstruktur", "produktmanagement", "cio", "organisation", "arbeitswelt"],
    },
]

def _englisch_laden(site_dir: Path) -> dict:
    """Englische Seitentexte aus docs/data/i18n-en.json."""
    f = site_dir / "data" / "i18n-en.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}


TIMESTAMP_RE = re.compile(r"^\*\*\[(\d{2}):(\d{2}):(\d{2})\]\*\*\s*(.*)$")


# --------------------------------------------------------------------------- utils

def slugify(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = value.replace("ß", "ss")
    value = "".join(c for c in value if not unicodedata.combining(c))
    value = re.sub(r"[^A-Za-z0-9]+", "-", value).strip("-").lower()
    return value or "eintrag"


def esc(value) -> str:
    return html.escape(str(value or ""), quote=True)


def iso_duration(seconds) -> str:
    try:
        total = int(float(seconds))
    except (TypeError, ValueError):
        return ""
    if total <= 0:
        return ""
    h, rem = divmod(total, 3600)
    m, s = divmod(rem, 60)
    out = "PT"
    if h:
        out += f"{h}H"
    if m:
        out += f"{m}M"
    if s:
        out += f"{s}S"
    return out


def human_duration(seconds, lang: str) -> str:
    try:
        total = int(float(seconds))
    except (TypeError, ValueError):
        return ""
    h, rem = divmod(total, 3600)
    m, _ = divmod(rem, 60)
    if h:
        return f"{h} h {m:02d} min"
    return f"{m} min"


def parse_published(value: str):
    if not value:
        return None
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def human_date(dt, lang: str) -> str:
    if not dt:
        return ""
    if lang == "en":
        return dt.strftime("%d %B %Y")
    months = ["Januar", "Februar", "Maerz", "April", "Mai", "Juni", "Juli",
              "August", "September", "Oktober", "November", "Dezember"]
    return f"{dt.day}. {months[dt.month - 1]} {dt.year}"


def meta_description(text: str, limit: int = 158) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    if " " in cut:
        cut = cut[: cut.rfind(" ")]
    return cut.rstrip(" ,.;:") + " …"


# --------------------------------------------------------------------------- parsing

def parse_transcript_file(path: Path) -> dict | None:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return None
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return None
    front = {}
    for line in parts[1].splitlines():
        m = re.match(r'^(\w+):\s*"?(.*?)"?\s*$', line)
        if m:
            front[m.group(1)] = m.group(2)

    # Ueberschriften tolerant matchen: in transkripte-en/018 steht ein Leerzeichen
    # vor "## Transcript". Solche Ausrutscher der Uebersetzung duerfen nicht dazu
    # fuehren, dass eine ganze Sprachfassung stillschweigend wegfaellt.
    body = parts[2]
    description = ""
    dm = re.search(r"^[ \t]*##+[ \t]*(?:Beschreibung|Description)[ \t]*$(.*?)(?=^[ \t]*##+[ \t]|\Z)",
                   body, re.S | re.M)
    if dm:
        description = dm.group(1).strip()

    transcript_body = ""
    tm = re.search(r"^[ \t]*##+[ \t]*(?:Transkript|Transcript)[ \t]*$(.*)", body, re.S | re.M)
    if tm:
        transcript_body = tm.group(1)

    lines = []
    for line in transcript_body.splitlines():
        line = line.strip()
        if not line:
            continue
        m = TIMESTAMP_RE.match(line)
        if m:
            h, mi, s, text = m.groups()
            lines.append({
                "stamp": f"{h}:{mi}:{s}",
                "anchor": f"t-{h}{mi}{s}",
                "seconds": int(h) * 3600 + int(mi) * 60 + int(s),
                "text": text.strip(),
            })
        elif lines:
            lines[-1]["text"] += " " + line

    return {"front": front, "description": description, "lines": lines, "path": path}


def slug_from_page_url(page_url: str, fallback: str) -> str:
    if page_url:
        tail = page_url.rstrip("/").rsplit("/", 1)[-1]
        if tail:
            return tail
    return slugify(fallback)


def collect_episodes(manifest_path: Path, repo_root: Path) -> list[dict]:
    """Metadaten kommen aus dem Manifest, nicht aus dem Frontmatter.

    Der Transkript-Header hat page_url erst seit Folge 38, das Manifest wird dagegen
    bei jedem Build frisch aus dem RSS-Feed erzeugt und enthaelt den Podigee-Slug fuer
    alle Folgen. transcriptPath liefert den exakten Dateibezug.
    """
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    episodes = []
    for item in manifest.get("episodes", []):
        de_rel = (item.get("transcripts", {}).get("de") or {}).get("path") or item.get("transcriptPath")
        if not de_rel:
            continue
        de_path = repo_root / de_rel
        if not de_path.exists():
            continue
        parsed = parse_transcript_file(de_path)
        if not parsed or not parsed["lines"]:
            continue

        en_rel = (item.get("transcripts", {}).get("en") or {}).get("path") or item.get("englishTranscriptPath")
        en_parsed = None
        if en_rel:
            en_path = repo_root / en_rel
            if en_path.exists():
                en_parsed = parse_transcript_file(en_path)
                if en_parsed and not en_parsed["lines"]:
                    en_parsed = None

        title = item.get("title") or parsed["front"].get("title") or de_path.stem
        en_title = (en_parsed or {}).get("front", {}).get("title") or title

        episodes.append({
            "slug": slug_from_page_url(item.get("pageUrl", ""), de_path.stem),
            "feed_description": (item.get("description") or "").strip(),
            "file_stem": de_path.stem,
            "title": title,
            "en_title": en_title,
            "index": item.get("index", ""),
            "published": parse_published(item.get("published", "")),
            "duration": item.get("duration", ""),
            "page_url": item.get("pageUrl", ""),
            "image_url": item.get("imageUrl", ""),
            "audio_url": item.get("audioUrl", ""),
            "translation_model": (en_parsed or {}).get("front", {}).get("translation_model", ""),
            "de": parsed,
            "en": en_parsed,
        })
    episodes.sort(key=lambda e: (e["published"] or datetime.min.replace(tzinfo=timezone.utc)))
    return episodes


# --------------------------------------------------------------------------- topics & guests

def assign_topics(episode: dict) -> list[dict]:
    """Themen zuordnen.

    Vier Punkte, an denen die erste Fassung falsch lag:

    1. Ohne Wortgrenzen gesucht. "rag" traf auf Frage, tragen und Auftrag, "recht" auf
       das Adverb. Wissensmanagement wurde dadurch zum Auffangbecken.
    2. Nur die ersten 80 Transkriptzeilen gelesen. Folge 012 hat ihre besten
       Haftungsfaelle bei Minute 7 und 28 und fiel deshalb durch.
    3. Absolute Trefferzahlen gezaehlt, was lange Folgen bevorzugt. Jetzt Dichte je
       1000 Woerter, gedeckelt.
    4. Stichwoerter beschrieben das Vokabular der Sendung statt zu unterscheiden.
       "agent", "openai" und "token" fallen in fast jeder Folge; damit standen 40 von
       52 Folgen unter demselben Cluster. Die Listen nennen jetzt nur, was ein Thema
       tatsaechlich von den anderen abgrenzt.

    Das staerkste Thema bekommt jede Folge, damit keine ohne Einordnung bleibt.
    Ein zweites oder drittes nur, wenn es mindestens 55 Prozent des Spitzenwerts
    erreicht.
    """
    titel = episode["title"].lower()
    beschreibung = episode["de"]["description"].lower()
    volltext = " ".join(l["text"] for l in episode["de"]["lines"]).lower()
    je_tausend = max(1.0, len(volltext.split()) / 1000)

    scored = []
    for topic in TOPICS:
        im_titel = in_besch = im_text = 0
        for kw in topic["keywords"]:
            muster = re.compile(r"(?<!\w)" + re.escape(kw) + r"\w*", re.I) if " " not in kw \
                else re.compile(re.escape(kw), re.I)
            im_titel += len(muster.findall(titel))
            in_besch += len(muster.findall(beschreibung))
            im_text += len(muster.findall(volltext))
        score = im_titel * 30 + in_besch * 6 + min(im_text / je_tausend, 25)
        if score:
            scored.append((score, topic))

    if not scored:
        return []
    scored.sort(key=lambda x: (-x[0], x[1]["slug"]))
    best = scored[0][0]
    return [scored[0][1]] + [tp for s, tp in scored[1:3] if s >= 0.55 * best]


def load_guests(path: Path) -> dict:
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {entry["episode"]: entry for entry in data.get("episodes", [])}


# --------------------------------------------------------------------------- rendering

def page_shell(*, lang: str, title: str, description: str, canonical: str, alternates: list[tuple[str, str]],
               image: str, body: str, jsonld: list[dict], depth: int, page_type: str = "article") -> str:
    up = "../" * depth
    alt_tags = "\n".join(
        f'    <link rel="alternate" hreflang="{esc(code)}" href="{esc(url)}">'
        for code, url in alternates
    )
    ld = "\n".join(
        f'    <script type="application/ld+json">{json.dumps(block, ensure_ascii=False, separators=(",", ":"))}</script>'
        for block in jsonld
    )
    return f"""<!doctype html>
<html lang="{esc(lang)}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{esc(title)}</title>
    <meta name="description" content="{esc(description)}">
    <link rel="canonical" href="{esc(canonical)}">
{alt_tags}
    <meta property="og:type" content="{esc(page_type)}">
    <meta property="og:site_name" content="{esc(SERIES_NAME)}">
    <meta property="og:locale" content="{'de_DE' if lang == 'de' else 'en_US'}">
    <meta property="og:title" content="{esc(title)}">
    <meta property="og:description" content="{esc(description)}">
    <meta property="og:url" content="{esc(canonical)}">
    <meta property="og:image" content="{esc(image)}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{esc(title)}">
    <meta name="twitter:description" content="{esc(description)}">
    <meta name="twitter:image" content="{esc(image)}">
    <link rel="stylesheet" href="{up}base.css">
    <link rel="stylesheet" href="{up}transcript.css">
{ld}
  </head>
  <body class="doc">
{body}
  </body>
</html>
"""


# Wird im Build gesetzt: In welchen Sprachen existiert der Blog ueberhaupt.
# Ohne das verlinkt die Kopfleiste auf eine Seite, die es nicht gibt.
BLOG_SPRACHEN: set[str] = set()


def render_nav(up: str, t: dict, lang: str) -> str:
    """Kopfleiste. Deutsch liegt im Wurzelverzeichnis, Englisch unter en/."""
    wurzel = up if lang == "de" else f"{up}en/"
    home = f"{wurzel}index.html"
    themen = f"{wurzel}{'themen' if lang == 'de' else 'topics'}/index.html"
    gaeste = f"{wurzel}{'gaeste' if lang == 'de' else 'guests'}/index.html"
    blog_eintrag = (f'        <a href="{wurzel}blog/index.html">'
                    f"{esc('Fachartikel' if lang == 'de' else 'Articles')}</a>\n"
                    if lang in BLOG_SPRACHEN else "")
    return f"""    <header class="doc-top">
      <a class="doc-brand" href="{home}">
        <span class="doc-brand-name">{esc(SERIES_NAME)}</span>
        <span class="doc-brand-sub">{esc(t['archive_title'])}</span>
      </a>
      <nav class="doc-nav" aria-label="{esc(t['back'])}">
        <a href="{home}">{esc(t['back'])}</a>
        <a href="{themen}">{esc('Themen' if lang == 'de' else 'Topics')}</a>
        <a href="{gaeste}">{esc('Gäste' if lang == 'de' else 'Guests')}</a>
{blog_eintrag}        <a href="{esc(SERIES_URL)}" rel="noreferrer">Podcast</a>
      </nav>
    </header>
"""


def render_episode_page(episode: dict, lang: str, base_url: str, *, prev_ep, next_ep, topics, guests) -> str:
    t = STRINGS[lang]
    parsed = episode[lang]
    other_lang = t["other"]
    has_other = episode[other_lang] is not None
    title_text = episode["title"] if lang == "de" else episode["en_title"]

    canonical = f"{base_url}/{lang}/{episode['slug']}/"
    alternates = [("de", f"{base_url}/de/{episode['slug']}/")]
    if episode["en"] is not None:
        alternates.append(("en", f"{base_url}/en/{episode['slug']}/"))
    alternates.append(("x-default", f"{base_url}/de/{episode['slug']}/"))

    # Deutsche Seite: Beschreibung aus dem Feed, die ist aktuell. Der Schnappschuss im
    # Transkript stammt vom Tag der Transkription und faellt bei jeder spaeteren
    # Korrektur zurueck. Englische Seite: dort gibt es nur die uebersetzte Fassung.
    quelle = episode["feed_description"] if (lang == "de" and episode.get("feed_description")) \
        else parsed["description"]
    # Der Standard-Abbinder aus der Podigee-Beschreibung wird hier abgeschnitten.
    # Er gehoert in die Podcast-Apps; die Seite hat einen eigenen Abo-Bereich, und
    # 52 Mal derselbe Block waere nur Rauschen.
    quelle = re.split(r"\n\s*—\s*\n(?=Think Different\. Think AI\. mit )", quelle)[0]
    desc_paragraphs = [p.strip() for p in quelle.split("\n") if p.strip()]
    lead = desc_paragraphs[0] if desc_paragraphs else ""
    rest = desc_paragraphs[1:]
    description = meta_description(rest[0] if rest else lead)

    page_title = f"{title_text} — {t['title_suffix']} | {SERIES_NAME}"

    pub_dt = episode["published"]
    up = "../../"

    # --- Kopfbereich
    meta_bits = []
    if pub_dt:
        meta_bits.append(f"<span><b>{esc(t['published'])}</b> "
                         f"<time datetime=\"{pub_dt.date().isoformat()}\">{esc(human_date(pub_dt, lang))}</time></span>")
    dur = human_duration(episode["duration"], lang)
    if dur:
        meta_bits.append(f"<span><b>{esc(t['duration'])}</b> {esc(dur)}</span>")

    lang_switch = (
        f'<a class="doc-lang" href="{up}{other_lang}/{episode["slug"]}/">{esc(t["switch"])}</a>'
        if has_other else f'<span class="doc-lang muted">{esc(t["no_other"])}</span>'
    )

    guest_html = ""
    if guests:
        items = "".join(
            f'<a href="{up}gaeste/{esc(g["slug"])}/">{esc(g["name"])}</a>' for g in guests
        )
        guest_html = f'<p class="doc-chips"><b>{esc(t["guests"])}</b> {items}</p>'

    topic_html = ""
    if topics:
        items = "".join(
            f'<a href="{up}themen/{esc(tp["slug"])}/">{esc(tp["name"])}</a>' for tp in topics
        )
        topic_html = f'<p class="doc-chips"><b>{esc(t["topics"])}</b> {items}</p>'

    # Auf die Quelldatei im Repo verlinken statt auf eine Kopie im Auslieferungsordner.
    # Das spart rund 6 MB verdoppelte Markdown-Dateien und haelt docs/ frei von Rohmaterial.
    # Die Dateinamen enthalten Leerzeichen, & und ! — ohne Kodierung bricht der Link.
    # 33-Sekunden-Promo als Einstieg. Nur auf den deutschen Seiten, weil die Clips
    # deutschsprachige Typografie zeigen. preload="none" laedt erst auf Klick,
    # das Cover dient als Standbild.
    video_html = ""
    if lang == "de" and episode.get("has_video"):
        video_html = (
            '<section class="doc-video">\n'
            f'          <video controls preload="none" playsinline '
            f'poster="{up}covers/{esc(episode["slug"])}.jpg" width="1280" height="720">\n'
            f'            <source src="{up}videos/{esc(episode["slug"])}.mp4" type="video/mp4">\n'
            '          </video>\n'
            '          <p class="doc-video-note">33 Sekunden zur Folge, bevor du liest.</p>\n'
            '        </section>')

    md_dir = "transkripte" if lang == "de" else "transkripte-en"
    md_link = f"{SOURCE_REPO}/blob/main/{md_dir}/{quote(episode['file_stem'] + '.md')}"

    # --- zitierfaehiger Vorspann
    lead_html = f'<p class="doc-lead">{esc(lead)}</p>' if lead else ""
    desc_html = "".join(f"<p>{esc(p)}</p>" for p in rest)

    # --- Transkript
    rows = []
    for line in parsed["lines"]:
        rows.append(
            f'<p class="tl" id="{esc(line["anchor"])}">'
            f'<a class="ts" href="#{esc(line["anchor"])}" aria-label="{esc(line["stamp"])}">{esc(line["stamp"])}</a>'
            f'<span class="tt">{esc(line["text"])}</span></p>'
        )
    transcript_html = "\n        ".join(rows)

    # --- Blaettern
    pager = []
    if prev_ep:
        prev_title = prev_ep["title"] if lang == "de" else prev_ep["en_title"]
        pager.append(f'<a class="pg prev" href="{up}{lang}/{prev_ep["slug"]}/">'
                     f'<span>{esc(t["prev"])}</span><b>{esc(prev_title)}</b></a>')
    if next_ep:
        next_title = next_ep["title"] if lang == "de" else next_ep["en_title"]
        pager.append(f'<a class="pg next" href="{up}{lang}/{next_ep["slug"]}/">'
                     f'<span>{esc(t["next"])}</span><b>{esc(next_title)}</b></a>')
    pager_html = f'<nav class="doc-pager">{"".join(pager)}</nav>' if pager else ""

    # Fachartikel zur Folge, sofern es ihn in dieser Sprache gibt
    artikel_btn = ""
    if episode.get(f"article_{lang}"):
        wort = "Fachartikel lesen" if lang == "de" else "Read the article"
        artikel_btn = (f'<a class="btn art-btn" href="{up}{"blog" if lang == "de" else "en/blog"}'
                       f'/{esc(episode["slug"])}/">{esc(wort)}</a>')

    body = f"""{render_nav(up, t, lang)}
    <main class="doc-main">
      <article>
        <div class="doc-head">
          <img class="doc-cover" src="{up}covers/{esc(episode['slug'])}.jpg" alt="" loading="lazy" width="200" height="200">
          <div class="doc-head-text">
            <h1>{esc(title_text)}</h1>
            <p class="doc-meta">{"".join(meta_bits)}</p>
            {lang_switch}
          </div>
        </div>

        {topic_html}
        {guest_html}

        {video_html}

        <section class="doc-desc">
          <h2>{esc(t['description_heading'])}</h2>
          {lead_html}
          {desc_html}
          <p class="doc-actions">
            <a class="btn" href="{esc(episode['page_url'])}" rel="noreferrer">{esc(t['listen'])}</a>
            <a class="btn ghost" href="{md_link}">{esc(t['markdown'])}</a>
            {artikel_btn}
          </p>
        </section>

        <section class="doc-transcript">
          <h2>{esc(t['transcript_heading'])}</h2>
        {transcript_html}
        </section>

        {pager_html}
      </article>
    </main>
"""

    # --- strukturierte Daten
    persons = [{"@type": "Person", "name": h["name"], "sameAs": h["sameAs"]} for h in HOSTS]
    guest_persons = []
    for g in guests:
        entry = {"@type": "Person", "name": g["name"]}
        if g.get("sameAs"):
            entry["sameAs"] = g["sameAs"]
        if g.get("affiliation"):
            entry["affiliation"] = {"@type": "Organization", "name": g["affiliation"]}
        guest_persons.append(entry)

    full_text = " ".join(l["text"] for l in parsed["lines"])

    audio = {
        "@type": "AudioObject",
        "contentUrl": episode["audio_url"],
        "encodingFormat": "audio/mpeg",
    }
    if iso_duration(episode["duration"]):
        audio["duration"] = iso_duration(episode["duration"])
    if full_text:
        audio["transcript"] = full_text

    ep_ld = {
        "@context": "https://schema.org",
        "@type": "PodcastEpisode",
        "@id": canonical + "#episode",
        "url": canonical,
        "name": title_text,
        "headline": title_text,
        "inLanguage": lang,
        "description": meta_description(rest[0] if rest else lead, 300),
        "image": episode["image_url"],
        "associatedMedia": audio,
        "partOfSeries": {
            "@type": "PodcastSeries",
            "name": SERIES_NAME,
            "url": SERIES_URL,
            "webFeed": FEED_URL,
        },
        "author": persons,
        "creator": persons,
        "publisher": {"@type": "Organization", "name": SERIES_NAME, "url": SERIES_URL},
    }
    if pub_dt:
        ep_ld["datePublished"] = pub_dt.date().isoformat()
    if iso_duration(episode["duration"]):
        ep_ld["timeRequired"] = iso_duration(episode["duration"])
    if guest_persons:
        ep_ld["actor"] = guest_persons
        ep_ld["about"] = guest_persons
    if topics:
        ep_ld["keywords"] = ", ".join(tp["name"] for tp in topics)

    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": STRINGS[lang]["archive_title"], "item": f"{base_url}/"},
            {"@type": "ListItem", "position": 2, "name": title_text, "item": canonical},
        ],
    }

    return page_shell(
        lang=lang, title=page_title, description=description, canonical=canonical,
        alternates=alternates, image=episode["image_url"], body=body,
        jsonld=[ep_ld, crumbs], depth=2,
    )


def render_list_page(*, lang, title, heading, intro, entries, canonical, base_url, depth,
                     alternates=None, extra_ld=None) -> str:
    t = STRINGS[lang]
    up = "../" * depth
    items = "\n        ".join(
        f'<li><a href="{esc(e["href"])}"><b>{esc(e["title"])}</b>'
        + (f'<span>{esc(e["note"])}</span>' if e.get("note") else "")
        + "</a></li>"
        for e in entries
    )
    body = f"""{render_nav(up, t, lang)}
    <main class="doc-main">
      <article>
        <h1>{esc(heading)}</h1>
        <p class="doc-lead">{esc(intro)}</p>
        <ul class="doc-list">
        {items}
        </ul>
      </article>
    </main>
"""
    return page_shell(
        lang=lang, title=title, description=meta_description(intro), canonical=canonical,
        alternates=alternates or [("de", canonical)], image=f"{base_url}/", body=body,
        jsonld=extra_ld or [], depth=depth, page_type="website",
    )


# --------------------------------------------------------------------------- build

def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def build(site_dir: Path, repo_root: Path, base_url: str) -> dict:
    manifest_path = site_dir / "data" / "episodes.json"
    if not manifest_path.exists():
        raise SystemExit(f"{manifest_path} fehlt — bitte zuerst scripts/build_site_manifest.py laufen lassen.")
    episodes = collect_episodes(manifest_path, repo_root)
    guests_map = load_guests(site_dir / "data" / "guests.json")

    # Englische Themennamen an die TOPICS haengen, damit sie auch auf den
    # Folgenseiten zur Verfuegung stehen und nicht nur auf den Themenseiten.
    i18n = _englisch_laden(site_dir)
    _en_themen = {x["slug"]: x for x in (i18n.get("themen", {}).get("topics") or [])}
    for _tp in TOPICS:
        _u = _en_themen.get(_tp["slug"], {})
        _tp["name_en"] = _u.get("name") or _tp["name"]
        _tp["intro_en"] = _u.get("intro") or _tp["intro"]

    # Fachartikel zur Folge, je Sprache. Der Dateiname ist der Episoden-Slug,
    # damit Artikel und Folgenseite ohne Umweg zueinander finden.
    artikel = {"de": {}, "en": {}}
    for lang, ordner in (("de", "artikel"), ("en", "artikel-en")):
        quelle = repo_root / ordner
        if not quelle.exists():
            continue
        for datei in sorted(quelle.glob("*.md")):
            a = blog.parse_article(datei)
            if a:
                artikel[lang][a["slug"]] = a

    global BLOG_SPRACHEN
    BLOG_SPRACHEN = {l for l in ("de", "en") if artikel[l]}

    for ep in episodes:
        for lang in ("de", "en"):
            ep[f"article_{lang}"] = ep["slug"] in artikel[lang]
        ep["has_video"] = (site_dir / "videos" / f"{ep['slug']}.mp4").exists()
        ep["topics"] = assign_topics(ep)
        entry = guests_map.get(ep["slug"], {})
        ep["guests"] = entry.get("guests", [])
        for g in ep["guests"]:
            g.setdefault("slug", slugify(g["name"]))

    # Alte generierte Ordner entfernen, damit nichts verwaist stehen bleibt.
    # In en/ liegt aber auch die englische Landingpage, und die ist ein von Hand
    # gepflegtes Artefakt wie die deutsche. Deshalb dort nur die Unterordner raeumen.
    for folder in ("de", "themen", "gaeste", "blog"):
        target = site_dir / folder
        if target.exists():
            shutil.rmtree(target)
    en_dir = site_dir / "en"
    if en_dir.exists():
        for eintrag in en_dir.iterdir():
            if eintrag.is_dir():
                shutil.rmtree(eintrag)

    # Rohmarkdown wird bewusst NICHT nach docs/ kopiert. Die Folgenseiten verlinken
    # auf die Quelldatei im Repo. Alte Kopien aus frueheren Staenden aufraeumen.
    for veraltet in ("transkripte", "transkripte-en"):
        alt_ordner = site_dir / veraltet
        if alt_ordner.exists():
            shutil.rmtree(alt_ordner)

    urls = []
    written = 0

    for i, ep in enumerate(episodes):
        prev_ep = episodes[i - 1] if i > 0 else None
        next_ep = episodes[i + 1] if i + 1 < len(episodes) else None
        for lang in ("de", "en"):
            if ep[lang] is None:
                continue
            # Blaettern nur zu Folgen, die es in dieser Sprache auch gibt
            p = prev_ep if (prev_ep and prev_ep[lang]) else None
            n = next_ep if (next_ep and next_ep[lang]) else None
            page = render_episode_page(ep, lang, base_url, prev_ep=p, next_ep=n,
                                       topics=ep["topics"], guests=ep["guests"])
            write(site_dir / lang / ep["slug"] / "index.html", page)
            written += 1
            urls.append({
                "loc": f"{base_url}/{lang}/{ep['slug']}/",
                "lastmod": (ep["published"].date().isoformat() if ep["published"] else None),
                "alts": [(l, f"{base_url}/{l}/{ep['slug']}/") for l in ("de", "en") if ep[l] is not None],
            })

    # ---- Blog: die Fachartikel zu den Folgen
    #
    # Reihenfolge wie die Folgenliste, also neueste zuerst. Der Slug ist der
    # Episoden-Slug, damit /blog/<slug>/ und /de/<slug>/ zusammengehoeren und
    # die hreflang-Paare aufgehen.
    blog_urls = []
    for lang in ("de", "en"):
        vorhanden = [ep for ep in reversed(episodes) if ep[f"article_{lang}"]]
        if not vorhanden:
            continue
        ordner = "blog" if lang == "de" else "en/blog"
        tiefe = 1 if lang == "de" else 2
        auf = "../" * tiefe
        st = blog.STRINGS[lang]
        nav = render_nav(auf, STRINGS[lang], lang)

        eintraege = []
        for ep in vorhanden:
            a = dict(artikel[lang][ep["slug"]])
            a["datum"] = (ep["published"].strftime("%d.%m.%Y" if lang == "de" else "%d %b %Y")
                          if ep["published"] else "")
            a["_ep"] = ep
            eintraege.append(a)

        # Uebersichtsseite
        idx_body = blog.index_body(
            eintraege, lang=lang, nav=nav,
            bild_pfad=lambda a: (f'{auf}artikelbilder/{a["slug"]}.jpg'
                                 if (site_dir / "artikelbilder" / f'{a["slug"]}.jpg').exists() else ""),
            href=lambda a: f'{a["slug"]}/',
        )
        idx_can = f"{base_url}/{ordner}/"
        idx_alts = [(l, f"{base_url}/{'blog' if l == 'de' else 'en/blog'}/")
                    for l in ("de", "en")
                    if any(ep[f"article_{l}"] for ep in episodes)]
        write(site_dir / ordner / "index.html", page_shell(
            lang=lang, title=f"{st['blog_title']} — {SERIES_NAME}",
            description=st["blog_intro"], canonical=idx_can, alternates=idx_alts,
            image=f"{base_url}/artikelbilder/{eintraege[0]['slug']}.jpg",
            body=idx_body, depth=tiefe, page_type="website",
            jsonld=[{
                "@context": "https://schema.org", "@type": "Blog",
                "name": f"{st['blog_title']} — {SERIES_NAME}",
                "url": idx_can, "inLanguage": lang,
                "description": st["blog_intro"],
                "blogPost": [{"@type": "BlogPosting", "headline": a["titel"],
                              "url": f"{idx_can}{a['slug']}/"} for a in eintraege[:20]],
            }],
        ))
        written += 1
        blog_urls.append({"loc": idx_can,
                          "lastmod": datetime.now(timezone.utc).date().isoformat(),
                          "alts": idx_alts})

        # Artikelseiten liegen eine Ebene tiefer als die Uebersicht (blog/<slug>/),
        # brauchen also einen eigenen Weg zum Wurzelverzeichnis.
        auf_a = "../" * (tiefe + 1)
        for i, a in enumerate(eintraege):
            ep = a["_ep"]
            bild_rel = f'{auf_a}artikelbilder/{a["slug"]}.jpg'
            hat_bild = (site_dir / "artikelbilder" / f'{a["slug"]}.jpg').exists()
            andere = "en" if lang == "de" else "de"
            wechsel = ((blog.STRINGS[lang]["switch"],
                        f'{auf_a}{"en/blog" if lang == "de" else "blog"}/{a["slug"]}/')
                       if ep[f"article_{andere}"] else None)
            vor = eintraege[i - 1] if i > 0 else None
            nach = eintraege[i + 1] if i + 1 < len(eintraege) else None

            can = f"{base_url}/{ordner}/{a['slug']}/"
            alts = [(l, f"{base_url}/{'blog' if l == 'de' else 'en/blog'}/{a['slug']}/")
                    for l in ("de", "en") if ep[f"article_{l}"]]
            body = blog.artikel_body(
                a, lang=lang, up=auf_a, nav=render_nav(auf_a, STRINGS[lang], lang),
                bild=bild_rel if hat_bild else "",
                folge_href=f'{auf_a}{lang}/{a["slug"]}/',
                folge_titel=ep["title"] if lang == "de" else ep["en_title"],
                datum=a["datum"], wechsel=wechsel,
                prev_a=(vor["titel"], f'../{vor["slug"]}/') if vor else None,
                next_a=(nach["titel"], f'../{nach["slug"]}/') if nach else None,
            )
            write(site_dir / ordner / a["slug"] / "index.html", page_shell(
                lang=lang, title=f'{a["titel"]} — {SERIES_NAME}',
                description=meta_description(a["teaser"] or a["titel"]),
                canonical=can, alternates=alts,
                image=f'{base_url}/artikelbilder/{a["slug"]}.jpg' if hat_bild else f"{base_url}/",
                body=body, depth=tiefe + 1, page_type="article",
                jsonld=[{
                    "@context": "https://schema.org", "@type": "BlogPosting",
                    "headline": a["titel"], "description": a["teaser"],
                    "url": can, "inLanguage": lang,
                    "datePublished": ep["published"].date().isoformat() if ep["published"] else None,
                    "wordCount": a["woerter"],
                    "image": f'{base_url}/artikelbilder/{a["slug"]}.jpg' if hat_bild else None,
                    "author": [{"@type": "Person", "name": n.strip()}
                               for n in (a["autor"] or "Mark Zimmermann").replace(" und ", " and ").split(" and ")],
                    "publisher": {"@type": "Organization", "name": SERIES_NAME},
                    "isPartOf": {"@type": "Blog", "name": f"{st['blog_title']} — {SERIES_NAME}",
                                 "url": idx_can},
                    "about": {"@type": "PodcastEpisode", "name": ep["title"],
                              "url": f"{base_url}/{lang}/{a['slug']}/"},
                    "mainEntityOfPage": can,
                }],
            ))
            written += 1
            blog_urls.append({
                "loc": can,
                "lastmod": ep["published"].date().isoformat() if ep["published"] else None,
                "alts": alts,
            })
    urls.extend(blog_urls)

    # ---- Themen- und Gaesteseiten, zweisprachig
    #
    # Deutsch liegt im Wurzelverzeichnis (themen/, gaeste/), Englisch unter en/
    # (en/topics/, en/guests/). Die Slugs bleiben in beiden Sprachen gleich, damit
    # bestehende Links gueltig bleiben und die hreflang-Paare sauber aufgehen.
    themen_en = _en_themen

    SPRACHEN = [
        {"lang": "de", "themen": "themen", "gaeste": "gaeste", "praefix": "",
         "themen_titel": "Themen", "gaeste_titel": "Gäste",
         "themen_intro": "Die Folgen nach Themen sortiert. Jede Seite ordnet das Thema "
                         "ein und verlinkt die zugehörigen Transkripte.",
         "gaeste_intro": "Alle Gäste des Podcasts mit ihren Folgen.",
         "folgen": lambda n: f"{n} Folge" if n == 1 else f"{n} Folgen"},
        {"lang": "en", "themen": "topics", "gaeste": "guests", "praefix": "en/",
         "themen_titel": "Topics", "gaeste_titel": "Guests",
         "themen_intro": "The episodes sorted by topic. Each page places the topic in "
                         "context and links the transcripts that belong to it.",
         "gaeste_intro": "Every guest on the show, with their episodes.",
         "folgen": lambda n: f"{n} episode" if n == 1 else f"{n} episodes"},
    ]

    by_guest = {}
    for ep in episodes:
        for g in ep["guests"]:
            by_guest.setdefault(g["slug"], {"info": g, "episodes": []})["episodes"].append(ep)

    topic_index_entries = []
    for S in SPRACHEN:
        L, P = S["lang"], S["praefix"]
        tiefe = 2 if L == "de" else 3          # themen/<slug>/ bzw. en/topics/<slug>/
        tiefe_index = 1 if L == "de" else 2
        zurueck = "../" * tiefe

        index_eintraege = []
        for topic in TOPICS:
            members = [e for e in episodes
                       if any(x["slug"] == topic["slug"] for x in e["topics"])]
            if not members:
                continue
            uebersetzt = themen_en.get(topic["slug"], {})
            name = topic["name"] if L == "de" else (uebersetzt.get("name") or topic["name"])
            intro = topic["intro"] if L == "de" else (uebersetzt.get("intro") or topic["intro"])
            entries = [{
                "href": f"{zurueck}{L}/{e['slug']}/",
                "title": e["title"],
                "note": human_date(e["published"], L),
            } for e in reversed(members)]
            canonical = f"{base_url}/{P}{S['themen']}/{topic['slug']}/"
            alternates = [("de", f"{base_url}/themen/{topic['slug']}/"),
                          ("en", f"{base_url}/en/topics/{topic['slug']}/"),
                          ("x-default", f"{base_url}/themen/{topic['slug']}/")]
            suffix = "Folgen und Transkripte" if L == "de" else "episodes and transcripts"
            page = render_list_page(
                lang=L, title=f"{name} — {suffix} | {SERIES_NAME}",
                heading=name, intro=intro, entries=entries,
                canonical=canonical, base_url=base_url, depth=tiefe,
                alternates=alternates,
                extra_ld=[{
                    "@context": "https://schema.org", "@type": "CollectionPage",
                    "name": name, "url": canonical, "description": intro,
                    "inLanguage": L,
                    "isPartOf": {"@type": "WebSite", "name": SERIES_NAME, "url": f"{base_url}/"},
                }],
            )
            write(site_dir / (P + S["themen"]) / topic["slug"] / "index.html", page)
            written += 1
            urls.append({"loc": canonical, "lastmod": None,
                         "alts": [(c, u) for c, u in alternates if c != "x-default"]})
            index_eintraege.append({"href": f"{topic['slug']}/", "title": name,
                                    "note": S["folgen"](len(members))})
            if L == "de":
                topic_index_entries.append({"slug": topic["slug"], "name": name,
                                            "intro": intro, "n": len(members)})

        canonical = f"{base_url}/{P}{S['themen']}/"
        write(site_dir / (P + S["themen"]) / "index.html", render_list_page(
            lang=L, title=f"{S['themen_titel']} | {SERIES_NAME}",
            heading=S["themen_titel"], intro=S["themen_intro"],
            entries=index_eintraege, canonical=canonical, base_url=base_url,
            depth=tiefe_index,
            alternates=[("de", f"{base_url}/themen/"), ("en", f"{base_url}/en/topics/"),
                        ("x-default", f"{base_url}/themen/")],
        ))
        written += 1
        urls.append({"loc": canonical, "lastmod": None,
                     "alts": [("de", f"{base_url}/themen/"), ("en", f"{base_url}/en/topics/")]})

        # ---- Gaeste
        gast_index = []
        for slug, data in sorted(by_guest.items(), key=lambda kv: kv[1]["info"]["name"]):
            info = data["info"]
            n = len(data["episodes"])
            entries = [{
                "href": f"{zurueck}{L}/{e['slug']}/",
                "title": e["title"],
                "note": human_date(e["published"], L),
            } for e in reversed(data["episodes"])]
            org = info.get("affiliation") or ""
            if L == "de":
                intro = (f"{info['name']}" + (f", {org}" if org else "")
                         + f", war in {S['folgen'](n)} von {SERIES_NAME} zu Gast.")
            else:
                intro = (f"{info['name']}" + (f", {org}" if org else "")
                         + f", was a guest on {S['folgen'](n)} of {SERIES_NAME}.")
            canonical = f"{base_url}/{P}{S['gaeste']}/{slug}/"
            alternates = [("de", f"{base_url}/gaeste/{slug}/"),
                          ("en", f"{base_url}/en/guests/{slug}/"),
                          ("x-default", f"{base_url}/gaeste/{slug}/")]
            person = {"@type": "Person", "name": info["name"]}
            if info.get("sameAs"):
                person["sameAs"] = info["sameAs"]
            if org:
                person["affiliation"] = {"@type": "Organization", "name": org}
            titel_suffix = "Folgen" if L == "de" else "episodes"
            write(site_dir / (P + S["gaeste"]) / slug / "index.html", render_list_page(
                lang=L, title=f"{info['name']} — {titel_suffix} | {SERIES_NAME}",
                heading=info["name"], intro=intro, entries=entries,
                canonical=canonical, base_url=base_url, depth=tiefe,
                alternates=alternates,
                extra_ld=[{"@context": "https://schema.org", "@type": "ProfilePage",
                           "url": canonical, "inLanguage": L, "mainEntity": person}],
            ))
            written += 1
            urls.append({"loc": canonical, "lastmod": None,
                         "alts": [(c, u) for c, u in alternates if c != "x-default"]})
            gast_index.append({"href": f"{slug}/", "title": info["name"],
                               "note": (org + " · " if org else "") + S["folgen"](n)})

        canonical = f"{base_url}/{P}{S['gaeste']}/"
        write(site_dir / (P + S["gaeste"]) / "index.html", render_list_page(
            lang=L, title=f"{S['gaeste_titel']} | {SERIES_NAME}",
            heading=S["gaeste_titel"], intro=S["gaeste_intro"],
            entries=gast_index, canonical=canonical, base_url=base_url, depth=tiefe_index,
            alternates=[("de", f"{base_url}/gaeste/"), ("en", f"{base_url}/en/guests/"),
                        ("x-default", f"{base_url}/gaeste/")],
        ))
        written += 1
        urls.append({"loc": canonical, "lastmod": None,
                     "alts": [("de", f"{base_url}/gaeste/"), ("en", f"{base_url}/en/guests/")]})

    # ---- Datenblöcke in die Landingpages einsetzen
    #
    # Beide Landingpages sind eigenstaendige, von Hand gestaltete Artefakte. Erzeugt
    # werden hier ausschliesslich die Daten zwischen den Markern, nie die Gestaltung.
    for L, index_path, praefix in (("de", site_dir / "index.html", ""),
                                   ("en", site_dir / "en" / "index.html", "../")):
        if not index_path.exists():
            continue
        text = index_path.read_text(encoding="utf-8")
        # Von en/index.html aus liegen Cover und Folgen eine Ebene hoeher
        auf = praefix

        # Kennzahlen
        sekunden = sum(int(float(e["duration"])) for e in episodes
                       if str(e["duration"]).strip().isdigit())
        volltexte = len(episodes) + sum(1 for e in episodes if e["en"])
        gaeste_namen = {g["slug"] for e in episodes for g in e["guests"]}
        gastfolgen = sum(1 for e in episodes if e["guests"])
        erste = min((e["published"] for e in episodes if e["published"]), default=None)
        monate_de = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
                     "August", "September", "Oktober", "November", "Dezember"]
        monat = (monate_de[erste.month - 1] if L == "de" else erste.strftime("%B")) if erste else ""
        stats = ([
            (f"{len(episodes)}", f"Folgen, zusammen {sekunden // 3600} Stunden"),
            (f"{volltexte}", "Transkripte, deutsch und englisch"),
            (f"{len(gaeste_namen)}", f"Gäste in {gastfolgen} Folgen"),
            (f"{monat} {erste.year}" if erste else "seit 2025", "erste Folge, seitdem im Wochenrhythmus"),
        ] if L == "de" else [
            (f"{len(episodes)}", f"episodes, {sekunden // 3600} hours in total"),
            (f"{volltexte}", "transcripts, German and English"),
            (f"{len(gaeste_namen)}", f"guests across {gastfolgen} episodes"),
            (f"{monat} {erste.year}" if erste else "since 2025", "first episode, weekly ever since"),
        ])
        stats_html = ("\n          <ul>\n"
                      + "".join(f"            <li><b>{esc(w)}</b><span>{esc(l)}</span></li>\n"
                                for w, l in stats)
                      + "          </ul>\n          ")

        # Folgenliste: nach Jahr gruppiert, mit der Podigee-Nummer als Anker.
        # 52 gleich aussehende Kacheln kann niemand ueberfliegen; das Cover, die
        # Nummer und die Jahresmarke geben dem Auge drei Haltepunkte.
        eintraege = []
        letztes_jahr = None
        for ep in reversed(episodes):
            jahr = ep["published"].year if ep["published"] else None
            if jahr != letztes_jahr:
                anzahl = sum(1 for e in episodes if e["published"] and e["published"].year == jahr)
                wort = "Folgen" if L == "de" else "episodes"
                eintraege.append(f'<li class="ep-jahr" aria-hidden="true"><span>{jahr}</span>'
                                 f'<span>{anzahl} {wort}</span></li>')
                letztes_jahr = jahr
            nummer = re.match(r"(\d+)", ep["slug"])
            datum = ep["published"].strftime("%d.%m.%Y" if L == "de" else "%d %b %Y") \
                if ep["published"] else ""
            dauer = human_duration(ep["duration"], L)
            andere = "en" if L == "de" else "de"
            marke = "EN" if L == "de" else "DE"
            hat_andere = ep["en"] if L == "de" else True
            alt = (f'<a class="ep-alt" href="{auf}{andere}/{esc(ep["slug"])}/" '
                   f'title="{esc(ep["title"])}">{marke}</a>') if hat_andere else ""
            eintraege.append(
                f'<li class="ep">'
                f'<a class="ep-main" href="{auf}{L}/{esc(ep["slug"])}/">'
                f'<img class="ep-cover" src="{auf}covers/{esc(ep["slug"])}.jpg" alt="" '
                f'loading="lazy" width="72" height="72">'
                f'<span class="ep-no">{esc(nummer.group(1) if nummer else "")}</span>'
                f'<span class="ep-t">{esc(ep["title"])}</span>'
                f'<span class="ep-meta"><span>{esc(datum)}</span><span>{esc(dauer)}</span></span>'
                f'</a>{alt}</li>')
        eps_html = ('\n          <ol class="lp-eps">\n            '
                    + "\n            ".join(eintraege) + "\n          </ol>\n          ")

        # Themen: eigene Akzentfarbe je Kachel, Anzahl als Blickfang.
        FARBEN = ["#34d4ff", "#ffcf24", "#ff7a1a", "#ff5fa8", "#6ef2a0"]
        pfad_themen = "themen" if L == "de" else "topics"
        themen = []
        i = 0
        for topic in TOPICS:
            anzahl = sum(1 for e in episodes
                         if any(x["slug"] == topic["slug"] for x in e["topics"]))
            if not anzahl:
                continue
            name = topic["name"] if L == "de" else topic.get("name_en", topic["name"])
            intro = topic["intro"] if L == "de" else topic.get("intro_en", topic["intro"])
            themen.append(
                f'<li class="tp" style="--tp:{FARBEN[i % len(FARBEN)]}">'
                f'<a href="{pfad_themen}/{esc(topic["slug"])}/">'
                f'<span class="tp-n">{anzahl}</span>'
                f'<strong>{esc(name)}</strong>'
                f'<span class="tp-i">{esc(intro)}</span></a></li>')
            i += 1
        topics_html = ('\n          <ul class="lp-topics">\n            '
                       + "\n            ".join(themen) + "\n          </ul>\n          ")

        # Gaeste: kompakte Zeilen mit Monogramm.
        pfad_gaeste = "gaeste" if L == "de" else "guests"
        gaeste = {}
        for ep in episodes:
            for g in ep["guests"]:
                gaeste.setdefault(g["slug"], {"name": g["name"], "n": 0,
                                              "org": g.get("affiliation", "")})["n"] += 1
        chips = []
        for slug, d in sorted(gaeste.items(), key=lambda kv: kv[1]["name"]):
            teile = [x for x in d["name"].replace("Dr.", "").replace("Prof.", "").split() if x]
            mono = "".join(x[0] for x in teile[:2]).upper()
            wort = ("Folgen" if d["n"] > 1 else "Folge") if L == "de" \
                else ("episodes" if d["n"] > 1 else "episode")
            zusatz = d["org"] or f'{d["n"]} {wort}'
            chips.append(
                f'<li class="gu"><a href="{pfad_gaeste}/{esc(slug)}/">'
                f'<span class="gu-m" aria-hidden="true">{esc(mono)}</span>'
                f'<span class="gu-b"><strong>{esc(d["name"])}</strong>'
                f'<span>{esc(zusatz)}</span></span>'
                f'<span class="gu-n">{d["n"]}</span></a></li>')
        guests_html = ('\n          <ul class="lp-guests">\n            '
                       + "\n            ".join(chips) + "\n          </ul>\n          ")

        # Blog: die sechs neuesten Fachartikel als Kacheln
        blog_html = ""
        neueste = [ep for ep in reversed(episodes) if ep[f"article_{L}"]][:6]
        if neueste:
            kacheln = []
            for ep in neueste:
                a = artikel[L][ep["slug"]]
                bild = f'{auf}artikelbilder/{ep["slug"]}.jpg'
                hat = (site_dir / "artikelbilder" / f'{ep["slug"]}.jpg').exists()
                nr = re.match(r"(\d+)", ep["slug"])
                wort = "Folge" if L == "de" else "Episode"
                ziel = f'{auf}{"blog" if L == "de" else "en/blog"}/{esc(ep["slug"])}/'
                kacheln.append(
                    f'<li class="ar"><a class="ar-link" href="{ziel}">'
                    + (f'<img class="ar-img" src="{esc(bild)}" alt="" loading="lazy" '
                       f'width="1200" height="644">' if hat else "")
                    + f'<span class="ar-kick">{wort} {esc(nr.group(1) if nr else "")} · '
                      f'{a["lesezeit"]} {"Min" if L == "de" else "min"}</span>'
                    + f'<span class="ar-t">{esc(a["titel"])}</span></a></li>')
            blog_html = ('\n          <ul class="lp-artikel-liste">\n            '
                         + "\n            ".join(kacheln)
                         + '\n          </ul>\n          ')

        for marker, block in (("STATS", stats_html), ("EPISODE-INDEX", eps_html),
                              ("BLOG", blog_html),
                              ("TOPICS", topics_html), ("GUESTS", guests_html)):
            s = text.find(f"<!-- {marker}:START")
            e = text.find(f"<!-- {marker}:END -->")
            if s == -1 or e == -1:
                continue
            s_ende = text.find("-->", s) + 3
            text = text[:s_ende] + block + text[e:]

        index_path.write_text(text, encoding="utf-8")
        written += 1
        urls.append({"loc": f"{base_url}/{praefix and 'en/'}",
                     "lastmod": datetime.now(timezone.utc).date().isoformat(),
                     "alts": [("de", f"{base_url}/"), ("en", f"{base_url}/en/")]})


    # ---- sitemap.xml
    chunks = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
              'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u in urls:
        chunks.append("  <url>")
        chunks.append(f"    <loc>{esc(u['loc'])}</loc>")
        if u["lastmod"]:
            chunks.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        for code, href in u["alts"]:
            chunks.append(f'    <xhtml:link rel="alternate" hreflang="{code}" href="{esc(href)}"/>')
        chunks.append("  </url>")
    chunks.append("</urlset>")
    write(site_dir / "sitemap.xml", "\n".join(chunks) + "\n")

    # ---- robots.txt
    write(site_dir / "robots.txt",
          "User-agent: *\n"
          "Allow: /\n\n"
          f"Sitemap: {base_url}/sitemap.xml\n")

    # ---- llms.txt
    llms = [f"# {SERIES_NAME}", "",
            "> Deutschsprachiger Podcast ueber kuenstliche Intelligenz in der Praxis, "
            "von Mark Zimmermann und Jens Scharnetzki. Dieses Archiv enthaelt die "
            "vollstaendigen Wortprotokolle aller Folgen auf Deutsch und Englisch.", "",
            f"Folgen: {len(episodes)} | Sprachen: Deutsch (Original), Englisch (Uebersetzung)",
            f"Feed: {FEED_URL}", f"Podcast: {SERIES_URL}", "",
            "## Hinweise zur Nutzung", "",
            "- Die Transkripte sind automatisch erstellt und koennen Fehler bei Eigennamen enthalten.",
            "- Jeder Absatz hat eine Zeitmarke als Anker, zum Beispiel #t-001234 fuer 00:12:34.",
            "- Beim Zitieren bitte Folgentitel, Datum und Zeitmarke angeben.", "",
            "## Folgen", ""]
    for ep in reversed(episodes):
        date = ep["published"].date().isoformat() if ep["published"] else ""
        llms.append(f"- [{ep['title']}]({base_url}/de/{ep['slug']}/) — {date}")
    # Die Fachartikel sind redaktionelle Texte, keine Transkripte. Ein eigener
    # Abschnitt, damit ein Modell beides nicht durcheinanderbringt.
    if artikel["de"]:
        llms += ["", "## Fachartikel", "",
                 "Je Folge ein redaktioneller Fachartikel im Stil der Heise-Magazine. "
                 "Das sind eingeordnete Texte, keine Wortprotokolle.", ""]
        for ep in reversed(episodes):
            if ep["article_de"]:
                a = artikel["de"][ep["slug"]]
                llms.append(f"- [{a['titel']}]({base_url}/blog/{ep['slug']}/)")
    write(site_dir / "llms.txt", "\n".join(llms) + "\n")

    return {"episodes": len(episodes), "pages": written, "urls": len(urls),
            "guests": len(by_guest), "topics": len(topic_index_entries)}


def build_parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--site-dir", default="docs")
    p.add_argument("--repo-root", default=".")
    p.add_argument("--base-url", default=DEFAULT_BASE_URL)
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    stats = build(Path(args.site_dir), Path(args.repo_root), args.base_url.rstrip("/"))
    print(f"Folgen: {stats['episodes']}")
    print(f"Seiten geschrieben: {stats['pages']}")
    print(f"URLs in sitemap.xml: {stats['urls']}")
    print(f"Themenseiten: {stats['topics']} | Gaesteseiten: {stats['guests']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
