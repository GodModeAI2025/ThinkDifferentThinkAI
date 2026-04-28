# Think Different! Think AI! Podcast Transcripts

Dieses Repository erzeugt Markdown-Transkripte fuer den Podcast-Feed:

https://think-ai.podigee.io/feed/mp3

Die fertigen Dateien landen in `transkripte/` und werden nach Episodennummer und Episodentitel benannt.

## Remote-Transkription

Der Workflow **Transcribe podcast** laeuft jeden Dienstag um 06:00 UTC automatisch. Er liest den Feed, vergleicht ihn mit den vorhandenen Dateien in `transkripte/`, transkribiert nur fehlende Folgen und schreibt danach alle neuen Markdown-Dateien in einem Commit zurueck ins Repository.

Der Workflow kann in GitHub Actions auch manuell gestartet werden.

Standardmodell ist `small`. Fuer einen schnelleren Lauf kann `base` ausgewaehlt werden; fuer bessere Qualitaet `medium`.
