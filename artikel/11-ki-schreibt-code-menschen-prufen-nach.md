---
folge: 11
titel: "Spec-Driven Development: Wenn der Patch zur Bauanleitung für den Exploit wird"
bildtitel: "Erst die Spezifikation"
kicker: "Im Gespräch mit Klaus Rodewig"
podigee: "https://think-ai.podigee.io/11-ki-schreibt-code-menschen-prufen-nach"
---

# Spec-Driven Development: Wenn der Patch zur Bauanleitung für den Exploit wird

*Ein Sicherheitsupdate war immer schon ein Hinweis darauf, wo die Lücke lag. Bisher brauchte man Tage an Reverse-Engineering-Erfahrung, um daraus einen Angriff zu bauen. Heute genügen Minuten.*

Von Mark Zimmermann

Klaus Rodewig ist langjähriger Sicherheitsfachmann und Pentester und beschreibt seinen Weg vom Skeptiker zum Nutzer. Er hat ein vollständiges Softwareprojekt fast ausschließlich mit KI umgesetzt: Embedded-C auf einem Raspberry-Pi-Teil plus eine Flutter-Desktop-Anwendung, kleinteilig beauftragt und Modell für Modell durchprobiert.

Der Einstieg ist ein Malheur mit Wiedererkennungswert: Ein Ausfall der AWS-Zone us-east-1 legt Perplexity lahm, während im Hintergrund die Sorge umgeht, ein liegengelassener n8n-Workflow mit gültigem Zugangstoken könnte gerade die Kreditkarte belasten.

> **kurz & knapp**
>
> - Ein Modellwechsel hilft nicht, wenn das Problem woanders liegt: Alle scheiterten am selben systemd-Filter
> - Spec-Driven Development: Anforderungen in Gherkin, erst Tests, dann Code
> - Ein Modell änderte wochenlang eigenmächtig einen Variablennamen, auch auf Nachfrage ohne Erklärung
> - Sprachmodelle disassemblieren Binärdateien ohne Symbole in lesbaren C-Code
> - Aus einem veröffentlichten Sicherheitsupdate lässt sich in Minuten ein Exploit bauen

## Wo alle Modelle gleich scheitern

Der lehrreichste Teil des Praxisberichts betrifft eine Grenze. Ein einfaches Filterproblem mit systemd und journalctl lösten weder Claude noch Gemini zuverlässig, egal wie oft nachgefragt wurde.

Das ist der wichtigste Befund für alle, die bei Schwierigkeiten das Modell wechseln. Wenn mehrere Modelle an derselben Stelle scheitern, liegt das Problem nicht am Modell. Es liegt daran, dass zu diesem Thema wenig gutes Material existiert, oder daran, dass die Aufgabe unpräzise gestellt ist.

Dazu passt die kuriose Anekdote, die zugleich ein ernstes Muster beschreibt: Ein Modell änderte wochenlang eigenmächtig eine Variable namens „Fahrzeugkontrolle“ in „Fahrzeugkontrolk“. Ohne Erklärung, auch auf Nachfrage nicht.

Solche stillen Änderungen sind der Grund, warum jede Ausgabe durch eine Versionskontrolle laufen sollte. Ein Fehler, den man sieht, ist harmlos. Einer, der zwischen zweihundert Zeilen steht, ist es nicht.

## Spec-Driven Development

Der rote Faden der Folge ist ein Vorgehen, das die verbreitete Praxis umdreht.

> ### Wie es funktioniert
>
> Statt vage zu beauftragen, zerlegt man Anforderungen in kleine Spezifikationen, formuliert in Gherkin, also der Given-When-Then-Notation aus dem Behavior-Driven Development.
>
> Beispiel: *Given* ein Benutzer ist angemeldet, *When* er eine Bestellung über 500 Euro auslöst, *Then* wird eine Freigabe angefordert.
>
> Aus diesen Spezifikationen lässt man **zuerst Tests** schreiben und **erst danach** Code. Der Code ist fertig, wenn die Tests bestehen.
>
> Der Gewinn liegt an einer unerwarteten Stelle. Das Formulieren der Spezifikation zwingt zur Klärung von Fragen, die man beim direkten Beauftragen überspringt: Was passiert bei genau 500 Euro, was bei Vertretungen, was bei Stornierungen. Diese Fragen beantwortet ein Modell sonst selbst, still.
>
> Und die Tests stammen nicht von demselben Durchgang, der den Code erzeugt hat. Damit ist das Grundproblem der Selbstbewertung umgangen, ohne dass ein zweites Modell nötig wäre.
>
> GitHub SpecKit verfolgt denselben Ansatz.

## Der Sicherheitsteil

Rodewig zieht die Linie konsequent zur Sicherheit weiter, und dieser Teil ist der beunruhigendste der Folge.

Sprachmodelle können Binärdateien ohne Symbolinformationen disassemblieren und in lesbaren C-Code zurückübersetzen. Für Audits ist das praktisch: Man kann prüfen, was eine Software tatsächlich tut, auch ohne Quelltext.

Für Patch-Zyklen ist es ein Problem. Ein veröffentlichtes Sicherheitsupdate war immer schon ein Hinweis: Wer die Version davor mit der danach vergleicht, sieht, was repariert wurde, und damit, wo die Lücke war. Bisher brauchte es Tage an Erfahrung, um daraus einen funktionierenden Angriff zu bauen. Mit Diffing und Modellanalyse sind es Minuten.

Die praktische Konsequenz betrifft jeden, der Software ausliefert: Das Zeitfenster zwischen Veröffentlichung eines Updates und dessen Installation beim Kunden ist zum kritischen Zeitraum geworden. Wer monatliche Wartungsfenster hat, hat einen Monat offenes Fenster.

## Regelwerke, maschinenlesbar

Zum Schluss geht es um MISRA C, den Kodierstandard für sicherheitskritische Automobilsoftware, und um den Cyber Resilience Act, der ab 2027 verbindliche Sicherheitsanforderungen für vernetzte Produkte bringt.

Beides sind hundertseitige Regelwerke, die sich in maschinenlesbare Vorgaben übersetzen und direkt bei der Beauftragung durchsetzen lassen. Das ist eine der überzeugendsten Anwendungen überhaupt: Regeln, die niemand vollständig im Kopf hat, werden zur Voraussetzung statt zum Prüfschritt am Ende.

## Fazit

Rodewigs Bilanz ist unaufgeregt und pointiert: Arbeitslos wird man nicht durch KI, sondern dann, wenn man sie ignoriert.

Für die eigene Arbeit ergeben sich drei Punkte. Wechseln Sie nicht das Modell, wenn mehrere an derselben Stelle scheitern. Suchen Sie stattdessen den Fehler in der Aufgabenstellung.

Schreiben Sie Spezifikationen vor dem Code und lassen Sie daraus zuerst Tests entstehen. Das ist der wirksamste bekannte Schutz gegen Ergebnisse, die gut aussehen und falsch sind.

Und rechnen Sie damit, dass Ihre Sicherheitsupdates als Bauanleitung gelesen werden. Wer bisher davon lebte, dass Reverse Engineering aufwendig ist, hat diesen Schutz verloren.

> **The story continues …**
>
> Der Cyber Resilience Act greift ab 2027. Dass sich hundertseitige Regelwerke in Vorgaben übersetzen lassen, die ein Modell beim Erzeugen einhält, ist die eine Hälfte. Die andere ist der Nachweis gegenüber einer Behörde, und dafür fehlen die Formate noch.

---

Die ganze Folge: [KI schreibt Code, Menschen prüfen nach !](https://think-ai.podigee.io/11-ki-schreibt-code-menschen-prufen-nach)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
