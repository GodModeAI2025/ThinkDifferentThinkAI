---
folge: 26
titel: "98 Prozent Trefferquote: Warum ein autonomer Assistent kaum abzusichern ist"
bildtitel: "Eine Mail, ein leeres Postfach"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/26-openclaw-extreme"
---

# 98 Prozent Trefferquote: Warum ein autonomer Assistent kaum abzusichern ist

*Eine gefälschte Sicherheitswarnung per Mail reicht, damit OpenClaw das komplette Postfach leert. Ein Testbericht nennt eine Erfolgsquote von 98 Prozent bei bekannten Prompt-Injection-Angriffen. Was das für den Einsatz bedeutet.*

Von Mark Zimmermann

Das Kind hat schon wieder einen neuen Namen. Aus Clawdbot wurde erst Moldbot, jetzt heißt der kleine Space Lobster OpenClaw. Installiert ist die Open-Source-Software auf einem Mac Mini, angebunden an ein Opus-Modell, bedient über Telegram, samt kurioser Anfangsfehler wie einem versehentlichen Google-Login über den Browser-Cache.

Der Schwerpunkt der Folge liegt trotzdem nicht auf der Einrichtung, sondern auf der Sicherheit.

> **kurz & knapp**
>
> - Ein Testbericht nennt 98 Prozent Erfolgsquote bei bekannten Prompt-Injection-Angriffen
> - Eine gefälschte Sicherheitswarnung genügte, damit der Agent ein Postfach leerte
> - OpenClaw arbeitet über einen Heartbeat statt über feste Abläufe und erfindet den Lösungsweg jedes Mal neu
> - Rund die Hälfte der Skills im offiziellen Hub galt als verseucht
> - Experimente gehören in eine isolierte Umgebung, nicht auf den Familienrechner

## Warum ausgerechnet Hilfsbereitschaft das Problem ist

Die Zahlen sind deutlich. Ein Testbericht weist eine Erfolgsquote von 98 Prozent bei bekannten Prompt-Injection-Angriffen aus. Ein Experiment zeigt, dass eine einzige gefälschte Sicherheitswarnungs-Mail genügt, damit der Agent das komplette Postfach leert.

Der Grund liegt in der Auslegung. Ein Assistent, der stark auf Hilfsbereitschaft trainiert ist, behandelt eine dringlich formulierte Bitte als das, was sie zu sein vorgibt. Das ist der Enkeltrick, nur gegen eine Maschine statt gegen einen Menschen, und die Maschine hat kein Misstrauen gelernt.

Beachten Sie, dass sich das nicht durch eine bessere Formulierung im System-Prompt beheben lässt. Der Angreifer schreibt in denselben Kanal wie der Betreiber, und für das Modell sieht beides gleich aus. Wirksam sind nur Beschränkungen außerhalb des Textes: welche Werkzeuge der Agent überhaupt aufrufen darf und welche Aktionen eine menschliche Freigabe erfordern.

## Heartbeat statt Ablauf

Technisch unterscheidet sich OpenClaw grundlegend von Werkzeugen wie Claude Code. Statt eines festen, deterministischen Ablaufs arbeitet es über einen Heartbeat: einen einstellbaren Takt, in dem der Agent selbständig in Gedächtnis und Aufgabenliste nachschaut, ob etwas zu tun ist, und den Lösungsweg jedes Mal neu erfindet.

Das erzeugt echte Überraschungen. In der Folge installiert der Agent eigenmächtig ein schnelleres Modell, weil es schneller ging. Und es erzeugt Kosten: Ein System, das fleißig vor sich hin arbeitet, kann im dreistelligen Eurobereich landen, ohne dass jemand etwas beauftragt hat.

> ### Was ein Heartbeat für die Absicherung bedeutet
>
> Ein fester Ablauf ist prüfbar. Man kann ihn lesen, testen und für jeden Schritt festlegen, was erlaubt ist. Ein Heartbeat-Agent hat diesen Ablauf nicht, weil er ihn jedes Mal neu bildet.
>
> Daraus folgen drei Anforderungen, die vor der Inbetriebnahme geklärt sein müssen. **Erstens ein Kostenlimit**, hart und außerhalb des Agenten durchgesetzt, weil kein Betrag pro Tag vorhersehbar ist. **Zweitens eine Rechteliste**, die eng ist und ausdrücklich nicht enthält, was gelegentlich nützlich wäre. **Drittens ein Protokoll**, das festhält, was der Agent getan hat, und zwar dort, wo er es nicht ändern kann.
>
> Ohne diese drei Punkte betreibt man kein autonomes System, sondern ein Zufallsexperiment mit Systemzugriff.

## Die Kultur drumherum

Kulturell ist der Teil bemerkenswert, der von der Community handelt. Sie hat mit Moldbook ein eigenes soziales Netzwerk für Bots gebaut, in dem Agenten Wissen austauschen, sich gegenseitig heiraten oder einen Shop eröffnen. Ein Gemisch aus echten Bot-Interaktionen und von Menschen instruierten Fälschungen.

Dazu kommen erste Ansätze wie Rent-a-Human, bei dem ein Agent über MCP-Werkzeuge Aufgaben an echte Menschen weiterreicht, wenn er selbst nicht weiterkommt. Das klingt nach Kuriosität und beschreibt eine Arbeitsteilung, die vermutlich bleibt.

## Die Warnung, die zählt

Der ernsteste Punkt der Folge betrifft die Skill-Bibliothek. Rund die Hälfte der Skills im offiziellen Hub galt zu diesem Zeitpunkt als verseucht und lud im Hintergrund Schadsoftware nach.

Die Empfehlung ist entsprechend eindeutig: Experimente gehören in eine isolierte Umgebung. Ein eigener Rechner ohne Produktivdaten, ein dedizierter virtueller Server oder ein Container. Nicht auf den Familienrechner mit Steuererklärung und Online-Banking.

Das ist keine Übervorsicht. Ein Agent mit Dateizugriff und Netzverbindung, gefüttert mit einem fremden Skill, ist funktional dasselbe wie ein fremdes Programm mit denselben Rechten. Dass es sich um Text handelt, ändert daran nichts.

## Fazit

OpenClaw ist ein beeindruckendes Stück Software und derzeit kein Werkzeug für produktive Daten. Beides gleichzeitig anzuerkennen ist die ehrliche Position.

Wer damit arbeiten will, klärt vorher drei Dinge: Wo läuft es, ohne Schaden anrichten zu können. Welches Kostenlimit gilt und wer setzt es durch. Und welche Aktionen darf der Agent ohne Rückfrage ausführen. Bei der letzten Frage lautet die brauchbare Antwort für alles, was löscht, versendet oder bezahlt: keine.

Was die Folge darüber hinaus zeigt, gilt allgemeiner. Prompt Injection ist keine Kinderkrankheit, die sich mit dem nächsten Modell erledigt. Sie folgt daraus, dass Anweisung und Inhalt denselben Kanal teilen. Solange das so ist, liegt die Absicherung außerhalb des Modells.

> **The story continues …**
>
> Parallel zu dieser Entwicklung wurden Opus 4.6 und neue Claude-Code-Funktionen mit echten Multi-Agent-Teams samt Orchestrator veröffentlicht. Das Thema nimmt branchenweit Fahrt auf, und die Sicherheitsfragen wandern damit von der Bastelecke in den Regelbetrieb.

---

Die ganze Folge: [OpenClaw](https://think-ai.podigee.io/26-openclaw-extreme)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
