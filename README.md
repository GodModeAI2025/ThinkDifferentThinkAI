# Think Different! Think AI! Podcast Transcripts

Dieses Repository erzeugt Markdown-Transkripte für den Podcast-Feed:

https://think-ai.podigee.io/feed/mp3

Die fertigen Dateien landen in `transkripte/` und werden nach Episodennummer und Episodentitel benannt.

Die Landingpage liegt unter GitHub Pages und zeigt verfügbare Transkripte mit Absprung zum Podigee-Webplayer.

Die Webseite unterstützt Deutsch und Englisch. Deutsche Transkripte liegen in `transkripte/`, englische Übersetzungen in `transkripte-en/`. Wenn noch keine englische Datei für eine Folge existiert, zeigt die Webseite im English-Modus einen entsprechenden Hinweis.

## Remote-Transkription

Der Workflow **Transcribe podcast** läuft jeden Dienstag um 06:00 UTC automatisch. Er liest den Feed, vergleicht ihn mit den vorhandenen Dateien in `transkripte/`, transkribiert nur fehlende Folgen und schreibt danach alle neuen Markdown-Dateien in einem Commit zurück ins Repository.

Der Workflow kann in GitHub Actions auch manuell gestartet werden.

Standardmodell ist `small`. Für einen schnelleren Lauf kann `base` ausgewählt werden; für bessere Qualität `medium`.

## Englische Übersetzungen

Der Workflow **Translate transcripts** läuft jeden Dienstag um 10:00 UTC automatisch und kann manuell gestartet werden. Er übersetzt fehlende deutsche Markdown-Dateien aus `transkripte/` nach `transkripte-en/`.

Wenn im Repository das Secret `OPENAI_API_KEY` gesetzt ist, nutzt der Workflow die OpenAI API und übersetzt alle fehlenden oder zuvor fehlgeschlagenen Dateien erneut. Fehlgeschlagene Übersetzungen werden unter `transkripte-en/.errors/` protokolliert und beim nächsten Lauf automatisch wieder versucht.

Wenn kein `OPENAI_API_KEY` gesetzt ist, nutzt der Workflow als Fallback ein freies Hugging-Face-Modell (`Helsinki-NLP/opus-mt-de-en`) direkt in GitHub Actions. Dafür ist kein OpenAI-, DeepL- oder anderer API-Key nötig. Der Tradeoff ist Laufzeit in GitHub Actions und eine schwächere Qualität als bei einem bezahlten Übersetzungsmodell.

## Landingpage und statische Folgenseiten

Der Workflow **Deploy landing page** baut die Seite unter `site/` und veroeffentlicht sie
auf GitHub Pages. Zwei Schritte laufen dabei nacheinander:

1. `scripts/build_site_manifest.py` erzeugt `site/data/episodes.json` frisch aus dem RSS-Feed.
2. `scripts/build_static_pages.py` erzeugt daraus je Folge und Sprache eine eigene, komplett
   im HTML stehende Seite:

```
site/de/<podigee-slug>/index.html
site/en/<podigee-slug>/index.html
site/themen/<thema>/index.html
site/gaeste/<name>/index.html
site/sitemap.xml, site/robots.txt, site/llms.txt
```

Die Single-Page-App unter `site/index.html` bleibt als Such- und Blaetteroberflaeche
bestehen; das Skript setzt dort nur die Folgenliste zwischen den `EPISODE-INDEX`-Markern
ein. Alles andere in dieser Datei wird von Hand gepflegt.

Wichtige Punkte:

- **Der Slug kommt aus `pageUrl` im Manifest, nicht aus der Dateinummer.** Die Nummerierung
  der Transkriptdateien folgt der Feed-Reihenfolge und weicht von den Podigee-Folgennummern ab.
- Die erzeugten Ordner sind in `.gitignore` und werden bei jedem Deploy neu gebaut.
- Gaeste stehen kuratiert in `site/data/guests.json`, ebenfalls nach Podigee-Slug. Nur
  belegte Namen eintragen; `sameAs` nur setzen, wenn das Profil geprueft ist.
- Lokal testen: `python scripts/build_static_pages.py` und anschliessend
  `python -m http.server` im Ordner `site/`.
