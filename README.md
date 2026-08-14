# Think Different! Think AI! Podcast Transcripts

Dieses Repository enthält die Transkripte zum Podcast-Feed:

https://think-ai.podigee.io/feed/mp3

Deutsche Transkripte liegen in `transkripte/`, englische Übersetzungen in `transkripte-en/`,
jeweils benannt nach Feed-Position und Episodentitel.

Aus denselben Dateien wird die öffentliche Seite gebaut:

https://godmodeai2025.github.io/ThinkDifferentThinkAI/

## Wie die Seite ausgeliefert wird

**Es laufen keine GitHub Actions mehr.** GitHub Pages liefert den Ordner `docs/` direkt vom
Branch `main` aus. Was dort nicht eingecheckt ist, ist online nicht vorhanden. Der Build
passiert lokal und wird mitcommittet.

Nach jeder Änderung an `transkripte/` oder `transkripte-en/`:

```bash
python scripts/build_site_manifest.py    # docs/data/episodes.json frisch aus dem RSS-Feed
python scripts/build_static_pages.py     # alle Seiten, Sitemap, robots.txt, llms.txt
git add docs && git commit && git push
```

Lokal ansehen: `cd docs && python -m http.server` und http://localhost:8000 öffnen.

## Was erzeugt wird

`scripts/build_static_pages.py` legt für jede Folge und jede Sprache eine eigene Seite an,
in der das vollständige Transkript bereits im HTML steht:

```
docs/de/<podigee-slug>/index.html      docs/themen/<thema>/index.html
docs/en/<podigee-slug>/index.html      docs/gaeste/<name>/index.html
docs/sitemap.xml, docs/robots.txt, docs/llms.txt
```

Je Folgenseite: eigener Title und Meta-Description, Canonical, hreflang-Paar de/en plus
x-default, Open Graph und Twitter Cards, JSON-LD als `PodcastEpisode` mit Hosts und Gästen
als `Person`-Entitäten, eine Zeitmarke je Absatz als Anker zum Verlinken einzelner Aussagen
sowie Blättern zur vorherigen und nächsten Folge.

Die Single-Page-App unter `docs/index.html` bleibt als Such- und Blätteroberfläche bestehen.
Das Skript setzt dort nur die Folgenliste zwischen den `EPISODE-INDEX`-Markern ein, alles
andere in dieser Datei wird von Hand gepflegt. Die Markdown-Dateien werden nach
`docs/transkripte/` und `docs/transkripte-en/` kopiert, weil die SPA sie zur Laufzeit lädt.

Wichtig zu wissen:

- **Der Slug kommt aus `pageUrl` im Manifest, nicht aus der Dateinummer.** Die Nummerierung
  der Transkriptdateien folgt der Feed-Reihenfolge und weicht von den Podigee-Folgennummern
  ab. Nie über die Dateinummer arbeiten.
- Gäste stehen kuratiert in `docs/data/guests.json`, ebenfalls nach Podigee-Slug. Nur belegte
  Namen eintragen, `sameAs` nur setzen, wenn das Profil tatsächlich geprüft ist.
- Themen werden über Stichwortlisten in `scripts/build_static_pages.py` zugeordnet, maximal
  drei je Folge.

## Neue Folgen nachziehen

Transkription und Übersetzung laufen ebenfalls lokal:

```bash
python scripts/plan_transcripts.py                 # Feed gegen transkripte/ vergleichen
python scripts/transcribe_episode.py --help        # fehlende Folge transkribieren
python scripts/translate_transcripts.py --provider openai --help
```

Bei der Übersetzung immer `--provider openai` verwenden. Der Standard ist `local` und nutzt
`Helsinki-NLP/opus-mt-de-en`; dessen Ergebnisse sind deutlich schwächer und machen unter
anderem aus dem Podcastnamen „Singdefin, Sing.K.I.". Die englischen Transkripte der Folgen
048 bis 052 sind auf diesem Weg entstanden und sollten neu übersetzt werden.

Nach dem Nachziehen die beiden Build-Befehle oben laufen lassen, sonst ändert sich online
nichts.
