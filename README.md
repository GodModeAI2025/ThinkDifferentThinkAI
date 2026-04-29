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
