# Think Different! Think AI! Podcast Transcripts

Dieses Repository erzeugt Markdown-Transkripte für den Podcast-Feed:

https://think-ai.podigee.io/feed/mp3

Die fertigen Dateien landen in `transkripte/` und werden nach Episodennummer und Episodentitel benannt.

Die Landingpage liegt unter GitHub Pages und zeigt verfügbare Transkripte mit Absprung zum Podigee-Webplayer.

## Remote-Transkription

Der Workflow **Transcribe podcast** läuft jeden Dienstag um 06:00 UTC automatisch. Er liest den Feed, vergleicht ihn mit den vorhandenen Dateien in `transkripte/`, transkribiert nur fehlende Folgen und schreibt danach alle neuen Markdown-Dateien in einem Commit zurück ins Repository.

Der Workflow kann in GitHub Actions auch manuell gestartet werden.

Standardmodell ist `small`. Für einen schnelleren Lauf kann `base` ausgewählt werden; für bessere Qualität `medium`.
