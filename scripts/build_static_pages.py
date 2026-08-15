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
import unicodedata
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import quote

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


def render_nav(up: str, t: dict, lang: str) -> str:
    home = f"{up}index.html"
    return f"""    <header class="doc-top">
      <a class="doc-brand" href="{home}">
        <span class="doc-brand-name">{esc(SERIES_NAME)}</span>
        <span class="doc-brand-sub">{esc(t['archive_title'])}</span>
      </a>
      <nav class="doc-nav" aria-label="{esc(t['back'])}">
        <a href="{home}">{esc(t['back'])}</a>
        <a href="{up}themen/index.html">Themen</a>
        <a href="{up}gaeste/index.html">{esc('Gäste' if lang == 'de' else 'Guests')}</a>
        <a href="{esc(SERIES_URL)}" rel="noreferrer">Podcast</a>
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

    body = f"""{render_nav(up, t, lang)}
    <main class="doc-main">
      <article>
        <div class="doc-head">
          <img class="doc-cover" src="{esc(episode['image_url'])}" alt="" loading="lazy" width="200" height="200">
          <div class="doc-head-text">
            <h1>{esc(title_text)}</h1>
            <p class="doc-meta">{"".join(meta_bits)}</p>
            {lang_switch}
          </div>
        </div>

        {topic_html}
        {guest_html}

        <section class="doc-desc">
          <h2>{esc(t['description_heading'])}</h2>
          {lead_html}
          {desc_html}
          <p class="doc-actions">
            <a class="btn" href="{esc(episode['page_url'])}" rel="noreferrer">{esc(t['listen'])}</a>
            <a class="btn ghost" href="{md_link}">{esc(t['markdown'])}</a>
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

    for ep in episodes:
        ep["topics"] = assign_topics(ep)
        entry = guests_map.get(ep["slug"], {})
        ep["guests"] = entry.get("guests", [])
        for g in ep["guests"]:
            g.setdefault("slug", slugify(g["name"]))

    # alte generierte Ordner entfernen, damit nichts verwaist stehen bleibt
    for folder in ("de", "en", "themen", "gaeste"):
        target = site_dir / folder
        if target.exists():
            shutil.rmtree(target)

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

    # ---- Themenseiten
    topic_index_entries = []
    for topic in TOPICS:
        members = [e for e in episodes if any(t["slug"] == topic["slug"] for t in e["topics"])]
        if not members:
            continue
        entries = [{
            "href": f"../../de/{e['slug']}/",
            "title": e["title"],
            "note": human_date(e["published"], "de"),
        } for e in reversed(members)]
        canonical = f"{base_url}/themen/{topic['slug']}/"
        page = render_list_page(
            lang="de",
            title=f"{topic['name']} — Folgen und Transkripte | {SERIES_NAME}",
            heading=topic["name"], intro=topic["intro"], entries=entries,
            canonical=canonical, base_url=base_url, depth=2,
            extra_ld=[{
                "@context": "https://schema.org", "@type": "CollectionPage",
                "name": topic["name"], "url": canonical, "description": topic["intro"],
                "isPartOf": {"@type": "WebSite", "name": SERIES_NAME, "url": f"{base_url}/"},
            }],
        )
        write(site_dir / "themen" / topic["slug"] / "index.html", page)
        written += 1
        urls.append({"loc": canonical, "lastmod": None, "alts": []})
        topic_index_entries.append({
            "href": f"../themen/{topic['slug']}/",
            "title": topic["name"],
            "note": f"{len(members)} Folgen",
        })

    canonical = f"{base_url}/themen/"
    write(site_dir / "themen" / "index.html", render_list_page(
        lang="de", title=f"Themen | {SERIES_NAME}", heading="Themen",
        intro="Die Folgen nach Themen sortiert. Jede Seite ordnet das Thema ein und "
              "verlinkt die zugehoerigen Transkripte.",
        entries=[{**e, "href": e["href"].replace("../themen/", "")} for e in topic_index_entries],
        canonical=canonical, base_url=base_url, depth=1,
    ))
    written += 1
    urls.append({"loc": canonical, "lastmod": None, "alts": []})

    # ---- Gaesteverzeichnis
    by_guest = {}
    for ep in episodes:
        for g in ep["guests"]:
            by_guest.setdefault(g["slug"], {"info": g, "episodes": []})["episodes"].append(ep)

    guest_index_entries = []
    for slug, data in sorted(by_guest.items(), key=lambda kv: kv[1]["info"]["name"]):
        info = data["info"]
        entries = [{
            "href": f"../../de/{e['slug']}/",
            "title": e["title"],
            "note": human_date(e["published"], "de"),
        } for e in reversed(data["episodes"])]
        note = info.get("affiliation") or ""
        intro = (f"{info['name']}" + (f", {note}" if note else "") +
                 f", war in {len(data['episodes'])} " +
                 ("Folge" if len(data["episodes"]) == 1 else "Folgen") +
                 f" von {SERIES_NAME} zu Gast.")
        canonical = f"{base_url}/gaeste/{slug}/"
        person_ld = {"@context": "https://schema.org", "@type": "ProfilePage",
                     "url": canonical,
                     "mainEntity": {"@type": "Person", "name": info["name"]}}
        if info.get("sameAs"):
            person_ld["mainEntity"]["sameAs"] = info["sameAs"]
        if note:
            person_ld["mainEntity"]["affiliation"] = {"@type": "Organization", "name": note}
        write(site_dir / "gaeste" / slug / "index.html", render_list_page(
            lang="de", title=f"{info['name']} — Folgen | {SERIES_NAME}",
            heading=info["name"], intro=intro, entries=entries,
            canonical=canonical, base_url=base_url, depth=2, extra_ld=[person_ld],
        ))
        written += 1
        urls.append({"loc": canonical, "lastmod": None, "alts": []})
        guest_index_entries.append({
            "href": f"{slug}/", "title": info["name"],
            "note": (note + " · " if note else "") + f"{len(data['episodes'])} " +
                    ("Folge" if len(data["episodes"]) == 1 else "Folgen"),
        })

    canonical = f"{base_url}/gaeste/"
    write(site_dir / "gaeste" / "index.html", render_list_page(
        lang="de", title=f"Gäste | {SERIES_NAME}", heading="Gäste",
        intro="Alle Gäste des Podcasts mit ihren Folgen.",
        entries=guest_index_entries, canonical=canonical, base_url=base_url, depth=1,
    ))
    written += 1
    urls.append({"loc": canonical, "lastmod": None, "alts": []})

    # ---- Datenblöcke in die Landingpage einsetzen
    #
    # Die Landingpage ist ein eigenstaendiges, von Hand gestaltetes Artefakt. Erzeugt
    # werden hier ausschliesslich die Daten zwischen den Markern, nie die Gestaltung.
    index_path = site_dir / "index.html"
    if index_path.exists():
        text = index_path.read_text(encoding="utf-8")

        # Kennzahlen
        sekunden = sum(int(float(e["duration"])) for e in episodes if str(e["duration"]).strip().isdigit())
        woerter = sum(len(l["text"].split()) for e in episodes for l in e["de"]["lines"])
        volltexte = sum(1 for e in episodes) + sum(1 for e in episodes if e["en"])
        # Vier verschiedene Beweisarten statt vier Groessenmasse: Umfang,
        # Nachpruefbarkeit, Zugang zu Fachleuten, Kontinuitaet. Die Wortzahl misst
        # dasselbe wie die Stunden und faellt deshalb raus.
        gaeste_namen = {g["slug"] for e in episodes for g in e["guests"]}
        gastfolgen = sum(1 for e in episodes if e["guests"])
        erste = min((e["published"] for e in episodes if e["published"]), default=None)
        monate = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
                  "August", "September", "Oktober", "November", "Dezember"]
        stats = [
            (f"{len(episodes)}", f"Folgen, zusammen {sekunden // 3600} Stunden"),
            (f"{volltexte}", "Transkripte, deutsch und englisch"),
            (f"{len(gaeste_namen)}", f"Gäste in {gastfolgen} Folgen"),
            (f"{monate[erste.month - 1]} {erste.year}" if erste else "seit 2025",
             "erste Folge, seitdem im Wochenrhythmus"),
        ]
        stats_html = ("\n          <ul>\n"
                      + "".join(f"            <li><b>{esc(w)}</b><span>{esc(l)}</span></li>\n"
                                for w, l in stats)
                      + "          </ul>\n          ")

        # Folgenliste
        eintraege = []
        for ep in reversed(episodes):
            datum = human_date(ep["published"], "de")
            dauer = human_duration(ep["duration"], "de")
            en = (f'<a class="alt" href="en/{esc(ep["slug"])}/">EN</a>') if ep["en"] else ""
            meta = f'<span class="meta"><span>{esc(datum)}</span><span>{esc(dauer)}</span>{en}</span>'
            eintraege.append(f'<li><a href="de/{esc(ep["slug"])}/"><b>{esc(ep["title"])}</b>{meta}</a></li>')
        eps_html = ('\n          <ul class="lp-eps">\n            '
                    + "\n            ".join(eintraege) + "\n          </ul>\n          ")

        # Themen
        themen = []
        for topic in TOPICS:
            anzahl = sum(1 for e in episodes if any(x["slug"] == topic["slug"] for x in e["topics"]))
            if not anzahl:
                continue
            themen.append(f'<li><a href="themen/{esc(topic["slug"])}/">'
                          f'<strong>{esc(topic["name"])}</strong>'
                          f'<span>{esc(topic["intro"])}</span>'
                          f'<span class="meta">{anzahl} Folgen</span></a></li>')
        topics_html = ('\n          <ul class="lp-topics">\n            '
                       + "\n            ".join(themen) + "\n          </ul>\n          ")

        # Gaeste
        gaeste = {}
        for ep in episodes:
            for g in ep["guests"]:
                gaeste.setdefault(g["slug"], {"name": g["name"], "n": 0})["n"] += 1
        chips = "".join(
            f'<li><a href="gaeste/{esc(slug)}/"><strong>{esc(d["name"])}</strong>'
            f'<span class="meta">{d["n"]} {"Folge" if d["n"] == 1 else "Folgen"}</span></a></li>'
            for slug, d in sorted(gaeste.items(), key=lambda kv: kv[1]["name"]))
        guests_html = ('\n          <ul class="lp-topics lp-guests">\n            ' + chips
                       + '\n          </ul>\n          <p class="prose" style="margin-top:18px">'
                       + '<a class="lp-btn ghost" href="gaeste/">Alle Gäste</a></p>\n          ')

        for marker, block in (("STATS", stats_html), ("EPISODE-INDEX", eps_html),
                              ("TOPICS", topics_html), ("GUESTS", guests_html)):
            start = text.find(f"<!-- {marker}:START")
            ende = text.find(f"<!-- {marker}:END -->")
            if start == -1 or ende == -1:
                continue
            start_ende = text.find("-->", start) + 3
            text = text[:start_ende] + block + text[ende:]

        index_path.write_text(text, encoding="utf-8")
        written += 1

    # ---- Startseite in die Sitemap
    urls.insert(0, {"loc": f"{base_url}/", "lastmod": datetime.now(timezone.utc).date().isoformat(), "alts": []})

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
