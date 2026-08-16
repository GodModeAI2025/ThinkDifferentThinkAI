"""Blog: die Fachartikel zu den Folgen als Webseiten.

Je Folge ein Artikel im Fachmagazin-Stil, geschrieben als LinkedIn-Newsletter und hier
zweitverwertet. Quelle sind `artikel/<slug>.md` (deutsch) und `artikel-en/<slug>.md`
(englisch), das Titelbild liegt unter `docs/artikelbilder/<slug>.png`.

Der Markdown-Wandler ist bewusst kein allgemeiner: Die Artikel folgen einer festen
Form (Teaser, „kurz & knapp", Großzitate, Infokasten, Ausblick), und nur so lassen
sich diese Bausteine als eigene, semantisch benannte Elemente ausgeben statt als
gleichförmige Blockquotes. Ein generischer Wandler würde alle fünf Kastenarten zu
demselben `<blockquote>` machen.
"""
from __future__ import annotations

import html
import re
from pathlib import Path

# Wie viele Wörter pro Minute für die Lesezeit. 200 ist der übliche Ansatz für
# Fachtexte; runder als jede Nachkommastelle, die Genauigkeit vortäuscht.
WPM = 200

STRINGS = {
    "de": {
        "blog_title": "Blog",
        "feed_title": "Blog — Think Different. Think AI.",
        "feed_desc": "Zu jeder Folge ein Fachartikel: eingeordnet, belegt und in "
                     "zehn Minuten gelesen.",
        "feed_link": "RSS abonnieren",
        "blog_intro": "Zu jeder Folge ein Fachartikel: eingeordnet, belegt und in "
                      "zehn Minuten gelesen. Neueste zuerst.",
        "reading": "Minuten Lesezeit",
        "to_episode": "Zur Folge",
        "to_transcript": "Volltext-Transkript",
        "all_articles": "Alle Beiträge",
        "article_for": "Fachartikel zur Folge",
        "episode": "Folge",
        "switch": "Read in English",
        "no_other": "Dieser Artikel liegt nur auf Deutsch vor.",
        "prev": "Neuerer Artikel",
        "next": "Älterer Artikel",
        "by": "Von",
    },
    "en": {
        "blog_title": "Blog",
        "feed_title": "Blog (English) — Think Different. Think AI.",
        "feed_desc": "One in-depth article per episode: contextualised, sourced and "
                     "read in ten minutes.",
        "feed_link": "Subscribe via RSS",
        "blog_intro": "One in-depth article per episode: contextualised, sourced and "
                      "read in ten minutes. Newest first.",
        "reading": "min read",
        "to_episode": "To the episode",
        "to_transcript": "Full transcript",
        "all_articles": "All posts",
        "article_for": "Article on the episode",
        "episode": "Episode",
        "switch": "Auf Deutsch lesen",
        "no_other": "This article is only available in German.",
        "prev": "Newer article",
        "next": "Older article",
        "by": "By",
    },
}

# Erkennt, um welche Art Kasten es sich handelt. Die Reihenfolge zählt: Der
# Ausblick beginnt ebenfalls mit **, muss also vor dem Faktenkasten stehen.
KASTEN_FAKTEN = re.compile(r"^\*\*(kurz & knapp|in brief|at a glance)\*\*\s*$", re.I)
KASTEN_AUSBLICK = re.compile(r"^\*\*(the story continues.*?)\*\*\s*$", re.I)
KASTEN_INFO = re.compile(r"^###\s+(.*)$")
ZITAT_ENDE = re.compile(r"^\*\*(.+?)\*\*(.*)$")


def esc(v) -> str:
    return html.escape(str(v), quote=True)


# --------------------------------------------------------------------- Parsen
def parse_article(path: Path) -> dict | None:
    """Frontmatter und Rumpf trennen. Ohne Frontmatter ist es kein Artikel."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    ende = text.find("\n---", 3)
    if ende < 0:
        return None
    kopf = {}
    for zeile in text[3:ende].splitlines():
        if ":" in zeile:
            k, _, v = zeile.partition(":")
            kopf[k.strip()] = v.strip().strip('"').strip("'")
    rumpf = text[ende + 4:].lstrip("\n")

    # H1, Teaser (kursiv) und Autorenzeile stehen am Anfang und werden im Kopf
    # der Seite eigens gesetzt, nicht im Fließtext wiederholt.
    titel = kopf.get("titel", path.stem)
    m = re.match(r"#\s+(.*?)\n", rumpf)
    if m:
        titel = m.group(1).strip()
        rumpf = rumpf[m.end():].lstrip("\n")
    teaser = ""
    m = re.match(r"\*(.+?)\*\s*\n", rumpf, re.S)
    if m:
        teaser = " ".join(m.group(1).split())
        rumpf = rumpf[m.end():].lstrip("\n")
    autor = ""
    m = re.match(r"(Von|By) ([^\n]+)\n", rumpf)
    if m:
        autor = m.group(2).strip()
        rumpf = rumpf[m.end():].lstrip("\n")

    # Der Abbinder nach dem letzten --- wird eigens gerendert.
    abbinder = ""
    teile = re.split(r"\n---\s*\n", rumpf)
    if len(teile) > 1:
        abbinder = teile[-1].strip()
        rumpf = "\n---\n".join(teile[:-1]).rstrip()

    woerter = len(re.sub(r"[#>*`\[\]()\-]", " ", rumpf).split())
    return {
        "slug": path.stem,
        "titel": titel,
        "teaser": teaser,
        "autor": autor,
        "kicker": kopf.get("kicker", ""),
        "folge": int(kopf["folge"]) if kopf.get("folge", "").isdigit() else None,
        "podigee": kopf.get("podigee", ""),
        "rumpf": rumpf,
        "abbinder": abbinder,
        "woerter": woerter,
        "lesezeit": max(1, round(woerter / WPM)),
    }


# ------------------------------------------------------------------- Inline
def inline(text: str) -> str:
    """Fett, kursiv und Links. Alles andere bleibt Text.

    Erst escapen, dann Markup einsetzen: So kann kein Zeichen aus dem Artikel
    zu HTML werden, das dort nicht hingehört.
    """
    s = esc(text)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)",
               lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<em>\1</em>", s)
    return s


def absaetze(zeilen: list[str]) -> str:
    """Zeilen zu Absätzen und Listen. Erwartet Text ohne Kastenmarkierung."""
    out, puffer, liste = [], [], []

    def puffer_leeren():
        if puffer:
            out.append(f"<p>{inline(' '.join(puffer))}</p>")
            puffer.clear()

    def liste_leeren():
        if liste:
            punkte = "".join(f"<li>{inline(x)}</li>" for x in liste)
            out.append(f"<ul>{punkte}</ul>")
            liste.clear()

    for z in zeilen:
        s = z.strip()
        if not s:
            puffer_leeren(); liste_leeren(); continue
        if s.startswith("- "):
            puffer_leeren(); liste.append(s[2:]); continue
        liste_leeren(); puffer.append(s)
    puffer_leeren(); liste_leeren()
    return "\n".join(out)


# ------------------------------------------------------------------- Kästen
def render_blockquote(inhalt: list[str]) -> str:
    """Ein Blockquote im Artikel ist immer einer von vier Bausteinen."""
    inhalt = [z for z in inhalt]
    while inhalt and not inhalt[0].strip():
        inhalt.pop(0)
    if not inhalt:
        return ""
    kopf = inhalt[0].strip()

    m = KASTEN_AUSBLICK.match(kopf)
    if m:
        return (f'<aside class="art-next"><h2>{esc(m.group(1))}</h2>'
                f'{absaetze(inhalt[1:])}</aside>')

    if KASTEN_FAKTEN.match(kopf):
        return (f'<aside class="art-facts"><h2>{esc(kopf.strip("*"))}</h2>'
                f'{absaetze(inhalt[1:])}</aside>')

    m = KASTEN_INFO.match(kopf)
    if m:
        return (f'<aside class="art-info"><h3>{inline(m.group(1))}</h3>'
                f'{absaetze(inhalt[1:])}</aside>')

    # Sonst ein Großzitat: Text, dann eine Zeile mit **Name**, Rolle.
    quelle = ""
    rest = inhalt
    for i in range(len(inhalt) - 1, -1, -1):
        s = inhalt[i].strip()
        if not s:
            continue
        m = ZITAT_ENDE.match(s)
        if m:
            quelle = inline(s)
            rest = inhalt[:i]
        break
    zitat = absaetze(rest)
    cap = f"<figcaption>{quelle}</figcaption>" if quelle else ""
    return f'<figure class="art-quote"><blockquote>{zitat}</blockquote>{cap}</figure>'


def render_body(rumpf: str) -> str:
    """Artikelrumpf zu HTML. Nur die Bausteine, die in den Artikeln vorkommen."""
    out, i = [], 0
    zeilen = rumpf.split("\n")
    fliess: list[str] = []

    def fliess_leeren():
        if fliess:
            block = absaetze(fliess)
            if block:
                out.append(block)
            fliess.clear()

    while i < len(zeilen):
        z = zeilen[i]
        s = z.strip()

        if s.startswith(">"):
            fliess_leeren()
            block = []
            while i < len(zeilen) and zeilen[i].strip().startswith(">"):
                block.append(re.sub(r"^\s*>\s?", "", zeilen[i]))
                i += 1
            out.append(render_blockquote(block))
            continue

        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            fliess_leeren()
            stufe = len(m.group(1))
            out.append(f"<h{stufe}>{inline(m.group(2))}</h{stufe}>")
            i += 1
            continue

        if re.match(r"^-{3,}$", s):
            fliess_leeren()
            out.append('<hr class="art-rule">')
            i += 1
            continue

        fliess.append(z)
        i += 1

    fliess_leeren()
    return "\n".join(x for x in out if x)


# ------------------------------------------------------------------- Seiten
def artikel_body(art: dict, *, lang: str, up: str, nav: str, bild: str,
                 folge_href: str, folge_titel: str, datum: str,
                 wechsel: tuple[str, str] | None, prev_a, next_a) -> str:
    """Rumpf der Artikelseite. Die Hülle setzt der Seitenbau."""
    t = STRINGS[lang]
    kicker = art["kicker"] or t["article_for"]
    nummer = f'{t["episode"]} {art["folge"]}' if art["folge"] else ""
    meta = " · ".join(x for x in (
        f'{t["by"]} {esc(art["autor"])}' if art["autor"] else "",
        esc(datum),
        f'{art["lesezeit"]} {t["reading"]}',
    ) if x)

    if wechsel:
        sprachlink = f'<a class="art-lang" href="{esc(wechsel[1])}">{esc(wechsel[0])}</a>'
    else:
        sprachlink = f'<span class="art-lang art-lang-off">{esc(t["no_other"])}</span>'

    hero = (f'<img class="art-hero" src="{esc(bild)}" alt="" width="1200" height="644" '
            f'loading="eager" decoding="async">') if bild else ""

    fuss = []
    if folge_href:
        fuss.append(f'<a class="art-cta" href="{esc(folge_href)}">'
                    f'<span>{esc(t["to_transcript"])}</span><b>{esc(folge_titel)}</b></a>')
    if art["podigee"]:
        fuss.append(f'<a class="art-cta art-cta-alt" href="{esc(art["podigee"])}" rel="noreferrer">'
                    f'<span>{esc(t["to_episode"])}</span><b>{esc(t["episode"])} {art["folge"]}</b></a>')

    blaettern = []
    if prev_a:
        blaettern.append(f'<a class="art-prev" href="{esc(prev_a[1])}">'
                         f'<span>{esc(t["prev"])}</span><b>{esc(prev_a[0])}</b></a>')
    if next_a:
        blaettern.append(f'<a class="art-next-link" href="{esc(next_a[1])}">'
                         f'<span>{esc(t["next"])}</span><b>{esc(next_a[0])}</b></a>')

    blog_index = f'{up}{"blog" if lang == "de" else "en/blog"}/index.html'

    return f"""{nav}
    <main class="doc-main art-page">
      <article class="art">
        <header class="art-head">
          <p class="art-kicker">{f'<b>{esc(nummer)}</b> · ' if nummer else ''}{esc(kicker)}</p>
          <h1>{esc(art["titel"])}</h1>
          {f'<p class="art-lead">{inline(art["teaser"])}</p>' if art["teaser"] else ''}
          <p class="art-meta">{meta}{' · ' if meta else ''}{sprachlink}</p>
        </header>
        {hero}
        <div class="art-body">
{render_body(art["rumpf"])}
        </div>
        <footer class="art-foot">
          <div class="art-ctas">{''.join(fuss)}</div>
          <nav class="art-blaettern" aria-label="{esc(t['all_articles'])}">
            {''.join(blaettern)}
          </nav>
          <p class="art-back"><a href="{blog_index}">{esc(t['all_articles'])}</a></p>
        </footer>
      </article>
    </main>
"""


def index_body(artikel: list[dict], *, lang: str, nav: str, bild_pfad, href) -> str:
    """Übersicht aller Artikel, neueste zuerst, wie die Folgenliste."""
    t = STRINGS[lang]
    karten = []
    for a in artikel:
        b = bild_pfad(a)
        karten.append(f"""<li class="bl-item">
            <a class="bl-link" href="{esc(href(a))}">
              {f'<img class="bl-img" src="{esc(b)}" alt="" width="1200" height="644" loading="lazy" decoding="async">' if b else ''}
              <span class="bl-text">
                <span class="bl-kicker"><b>{esc(t['episode'])} {a['folge']}</b> · {esc(a['datum'])} · {a['lesezeit']} {esc(t['reading'])}</span>
                <span class="bl-title">{esc(a['titel'])}</span>
                <span class="bl-lead">{esc(a['teaser'])}</span>
              </span>
            </a>
          </li>""")
    return f"""{nav}
    <main class="doc-main">
      <div class="bl-head">
        <h1>{esc(t['blog_title'])}</h1>
        <p class="doc-lead">{esc(t['blog_intro'])}</p>
        <p class="bl-feed"><a href="feed.xml">{esc(t['feed_link'])}</a></p>
      </div>
      <ol class="bl-list">
          {''.join(karten)}
      </ol>
    </main>
"""


# --------------------------------------------------------------------- RSS
def rss(artikel: list[dict], *, lang: str, feed_url: str, blog_url: str,
        base_url: str, rfc822, koerper) -> str:
    """Ein RSS-Feed je Sprache.

    Der volle Artikeltext steht in content:encoded, nicht nur der Teaser. Ein
    Feedleser soll den Beitrag lesen koennen, ohne die Seite aufzurufen; wer
    nur anteasert, zwingt zum Klick und macht den Feed nutzlos.

    Kein Bild-Enclosure: Das Titelbild steht bereits als erstes Element im
    content:encoded. Ein zusaetzliches Enclosure laden manche Leser als
    Anhang und zeigen es doppelt.
    """
    t = STRINGS[lang]
    eintraege = []
    for a in artikel:
        url = f"{blog_url}{a['slug']}/"
        bild = (f'<p><img src="{esc(a["bild_url"])}" alt="" width="1200" height="644"></p>'
                if a.get("bild_url") else "")
        inhalt = (bild
                  + (f'<p><em>{inline(a["teaser"])}</em></p>' if a["teaser"] else "")
                  + render_body(a["rumpf"]))
        eintraege.append(f"""  <item>
    <title>{esc(a['titel'])}</title>
    <link>{esc(url)}</link>
    <guid isPermaLink="true">{esc(url)}</guid>
    <pubDate>{esc(rfc822(a))}</pubDate>
    <dc:creator>{esc(a['autor'] or 'Mark Zimmermann')}</dc:creator>
    <category>{esc(t['episode'])} {a['folge']}</category>
    <description>{esc(a['teaser'] or a['titel'])}</description>
    <content:encoded><![CDATA[{inhalt}]]></content:encoded>
  </item>""")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:content="http://purl.org/rss/1.0/modules/content/"
     xmlns:dc="http://purl.org/dc/elements/1.1/">
<channel>
  <title>{esc(t['feed_title'])}</title>
  <link>{esc(blog_url)}</link>
  <atom:link href="{esc(feed_url)}" rel="self" type="application/rss+xml"/>
  <description>{esc(t['feed_desc'])}</description>
  <language>{esc(lang)}</language>
  <generator>scripts/build_static_pages.py</generator>
  <image>
    <url>{esc(base_url)}/covers/{esc(artikel[0]['slug'])}.jpg</url>
    <title>{esc(t['feed_title'])}</title>
    <link>{esc(blog_url)}</link>
  </image>
{chr(10).join(eintraege)}
</channel>
</rss>
"""
