# Think Different! Think AI! Podcast Transcripts

Dieses Repository erzeugt Markdown-Transkripte fuer den Podcast-Feed:

https://think-ai.podigee.io/feed/mp3

Die fertigen Dateien landen in `transkripte/` und werden nach Episodennummer und Episodentitel benannt.

## Remote-Transkription starten

Der Workflow **Transcribe podcast** kann in GitHub Actions manuell gestartet werden. Er transkribiert die Folgen parallel mit Whisper und schreibt danach alle Markdown-Dateien in einem Commit zurueck ins Repository.

Standardmodell ist `small`. Fuer einen schnelleren Lauf kann `base` ausgewaehlt werden; fuer bessere Qualitaet `medium`.
