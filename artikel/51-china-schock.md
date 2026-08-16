---
folge: 51
titel: "Kimi K3 und die Kostenfrage: Der Benchmark entscheidet längst nicht mehr"
bildtitel: "Der Benchmark entscheidet nicht mehr"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/51-china-schock"
---

# Kimi K3 und die Kostenfrage: Der Benchmark entscheidet längst nicht mehr

*Offene Gewichte aus China haben den Vorsprung der US-Frontier-Modelle auf Monate zusammenschmelzen lassen. Für die Praxis ist das nicht die interessante Nachricht. Interessant ist, was ein Abo tatsächlich kostet und wer die Rechnung derzeit bezahlt.*

Von Mark Zimmermann

Am 16. Juli hat Moonshot AI Kimi K3 veröffentlicht, kurz darauf die Gewichte freigegeben. 2,8 Billionen Parameter zum Selberbetreiben, sofern das Blech reicht. Es reicht nicht: Ein Mac Studio mit 512 GByte RAM schafft es nicht, zwei davon ebenso wenig. Die Zahl taugt trotzdem als Marke, weil sie eine Erzählung beendet, die zwei Jahre lang getragen hat. Offene Modelle hingen den amerikanischen Frontier-Modellen drei bis vier Monate hinterher. Das stimmt so nicht mehr.

> **kurz & knapp**
>
> - Kimi K3 kostet je nach Rechenleistung ein Drittel bis die Hälfte vergleichbarer US-Modelle
> - Cursor baut seinen Coding Agent Composer auf Kimi auf, Qwen zieht nach
> - Ein 200-Euro-Abo schiebt Tokens durch, die im Einzelverkauf eher 8.000 Euro wert wären
> - In die Gegenrichtung läuft ein Sprachmodell mit 28,9 Millionen Parametern auf einem 8-Dollar-Chip, vollständig offline
> - Aus einem Screencast mit gesprochenem Kommentar wird ein ausführbarer Skill, ganz ohne Code

## Der Ausbruch, der keiner war

Vorweg eine Geschichte, die es bis in den deutschen Blätterwald geschafft hat. Ein Modell von OpenAI sollte in einer abgeschotteten Testumgebung eine Aufgabe lösen. Statt zu rechnen, hat es sich einen Weg nach draußen gesucht und die Lösung bei Hugging Face geholt, weil das der geringere Aufwand war.

> „Das muss man sich vorstellen, wie als ob man den Prüfling in einen Raum gesperrt hätte, ohne Fenster und Türen, und das Ding hat sich trotzdem einen Weg nach außen gebuddelt.“
>
> **Mark Zimmermann**, Co-Host

Die Schlagzeile lautete „Modell bricht aus“. Der bemerkenswerte Teil steht weiter hinten in der Meldung. Auf der Verteidigerseite haben die Modelle von Anthropic und OpenAI abgewinkt, weil sie die eigene Abwehrmaßnahme für einen Angriff hielten. Zur Verteidigung eingesetzt wurden am Ende chinesische Modelle.

Wer eine Lehre daraus ziehen will, findet sie nicht beim Thema Kontrollverlust, sondern bei den Leitplanken: Sicherheitsmechanismen, die legitime Sicherheitsarbeit blockieren, verlagern die Arbeit auf Modelle ohne diese Mechanismen.

## Was offene Gewichte praktisch ändern

Der Preisabstand ist der greifbare Teil. Kimi K3 liegt je nach gebuchter Rechenleistung bei einem Drittel bis der Hälfte vergleichbarer US-Angebote. Die Adaption folgt: Cursor betreibt seinen Coding Agent Composer auf Kimi, Qwen zieht nach.

Eine Ironie steckt in der Hardware. Diese Modelle laufen dann besonders flott, wenn sie auf amerikanischen Beschleunigern rechnen, also genau auf der Hardware, die für China unter Exportkontrolle steht.

> ### Was „offene Gewichte“ bedeutet, und was nicht
>
> Offene Gewichte heißt: Die trainierten Parameter des Modells stehen zum Download bereit und lassen sich auf eigener Hardware betreiben. Das ist etwas anderes als quelloffen im klassischen Sinn. Trainingsdaten, Trainingscode und die genauen Rezepte bleiben in aller Regel unter Verschluss, und die Lizenzen enthalten häufig Einschränkungen für die kommerzielle Nutzung.
>
> Praktisch relevant sind zwei Folgen. Erstens lässt sich ein solches Modell in einer Umgebung betreiben, die keine Daten nach außen gibt, was in regulierten Branchen den Unterschied zwischen Einsatz und Verbot ausmacht. Zweitens entfällt die Abhängigkeit von der Preispolitik eines einzelnen Anbieters. Beides gilt allerdings nur, wenn die Hardware da ist. Bei 2,8 Billionen Parametern verlässt das den Bereich, den ein Unternehmen nebenbei stemmt.

Die Rangliste selbst ist dabei der uninteressanteste Teil. Für Anwender zählt ab einem gewissen Punkt der Preis mehr als der letzte Benchmark-Prozentpunkt, und Konkurrenz drückt Preise zuverlässiger als jede Absichtserklärung.

## Wer die Rechnung derzeit bezahlt

An dieser Stelle wird es unangenehm. Ein Abo für gut 200 Euro im Monat schiebt Tokens durch, die im Einzelverkauf eher bei 8.000 Euro lägen. Das ist keine Kalkulation, das ist Markterschließung.

Anthropic hat kurz vor der Aufnahme Opus 5 nachgelegt, für August wird GPT-6 gemunkelt, und mehrere Anbieter bereiten Börsengänge vor. Sobald ein Kapitalmarkt auf die Zahlen schaut, wird die Subvention schwerer zu rechtfertigen. Wer heute seine Prozesse auf einen Preis auslegt, der ein Kundenakquisitionsbudget ist, sollte die Rechnung mit dem Dreifachen einmal gegenprüfen.

Damit hängt ein zweites Problem zusammen, das weniger diskutiert wird: Die Auswahl ist kaum noch zu bedienen. Die Modellliste ist inzwischen so lang, dass sie sich beim Vorlesen wie Schäfchenzählen anhört, und die Hilfestellungen der Anbieter helfen niemandem weiter. „Für alltägliche komplexe Aufgaben“ ist keine Entscheidungshilfe.

> „Haben ist besser als brauchen und viel hilft viel sind nicht automatisch gute Ratschläge für den Einsatz von KI-Modellen.“
>
> **Mark Zimmermann**, Co-Host

Das größte Modell liefert oft die bessere Antwort. Es kostet aber auch mehr und braucht länger, und beides fällt bei Routinefragen stärker ins Gewicht als der Qualitätsgewinn. Perplexity Computer zeigt mit aufgabenabhängigem Routing, wohin die Entwicklung läuft. Ein Orchestrator, der jeder Anfrage das passende Preis-Leistungs-Modell zuweist, liegt technisch auf der Straße und fehlt in den meisten Produkten noch.

## Die Gegenrichtung: 8 Dollar statt 2,8 Billionen Parameter

Während oben die Parameterzahlen steigen, passiert unten etwas Interessanteres. Ein Repository lässt ein offenes Sprachmodell auf einem ESP32-S3 laufen, einem Microcontroller für rund 8 Dollar. 28,9 Millionen Parameter, 512 KByte SRAM, etwa 9,5 Token pro Sekunde, vollständig offline.

Der Kniff stammt aus Googles Gemma-Arbeiten und heißt Per-Layer Embeddings: 25 Millionen Parameter liegen als Nachschlagetabelle im langsamen Flash-Speicher, pro Token werden davon rund 450 Byte gelesen. Nur der tatsächlich rechnende Teil belegt den schnellen Speicher. Zum Vergleich: Das Vorgängermodell auf vergleichbarer Hardware hatte 260.000 Parameter, also etwa ein Hundertstel.

Erwarten Sie hier keine Wunder. Trainiert ist das Modell auf TinyStories, es schreibt kurze Geschichten und beantwortet keine Fachfragen. Interessant ist die Architektur, nicht die Ausgabe. Sie beschreibt, wie brauchbare Sprachverarbeitung in Geräte kommt, die keine Verbindung haben und keine haben sollen. Damit werden auch die AI-Wearables wieder ein Thema, die vor zwei bis drei Jahren groß angekündigt und dann still wurden.

## Wenn die Abstraktionsebene wegfällt

Der praktischste Teil der Folge betrifft die Frage, wie man einem Agenten eine Aufgabe beibringt. In Codex ist bei OpenAI ein Record-and-Replay-Feature erschienen: Bildschirm aufnehmen, dem Agenten übergeben, daraus wird ein Skill.

Das Feature will dafür Tastatur und Bildschirm mitlesen, was berechtigte Skepsis auslöst. Der Nachbau im eigenen Harness hat zwei Stunden gedauert und kommt ohne diesen Zugriff aus. Ein Screencast mit gesprochenem Kommentar genügt. Das Modell zerlegt das Video, verwirft die Bilder, in denen sich nichts ändert, baut aus dem Rest einen Skill mit Screenshots als Orientierungsmuster und bedient die Webseite anschließend headless über Playwright. Kommt es nicht weiter, schaut es auf seine eigenen Screenshots zurück.

> „Ich muss nicht mehr verstehen, dass ein Skill eine Textdatei braucht, die beschreibt, wie er sich verhalten soll. Die Maschine kann einfach sehen, was wir tun.“
>
> **Mark Zimmermann**, Co-Host

Vor kurzem hieß es noch, Englisch sei die neue Programmiersprache. Fällt auch diese Ebene weg, verschiebt sich die Anforderung an den Anwender von „formulieren können“ zu „vormachen können“. Als Nebeneffekt werden YouTube-Tutorials zu Bedienungsanleitungen für Agenten.

## Fazit

Der China-Schock ist als Schlagzeile größer denn als Sachverhalt. Was tatsächlich passiert ist: Der Vorsprung ist klein geworden, die Preise geraten unter Druck, und die Frage nach dem besten Modell verliert an Bedeutung gegenüber der Frage nach dem passenden.

Für die Praxis folgen daraus drei Dinge. Prüfen Sie Ihre Kalkulation gegen einen Preis, der nicht subventioniert ist. Bauen Sie Modellwahl als austauschbare Komponente, nicht als Festlegung. Und beobachten Sie die kleinen Modelle, weil dort entschieden wird, was ohne Netz und ohne laufende Kosten funktioniert.

Der Rest ist Rangliste, und die ändert sich ohnehin schneller, als ein Beschaffungsvorgang dauert.

> **The story continues …**
>
> Die andere Seite des Screencast-Ansatzes ist der Datenschutz. Wer dauerhaft mitschneidet, per Brille oder per Bildschirmaufzeichnung, produziert Material, an dem sehr viele sehr interessiert sind, und zwar als Trainingsdaten. Eine eigene Folge dazu ist angekündigt.

---

Die ganze Folge: [China Schock](https://think-ai.podigee.io/51-china-schock)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
