---
folge: 47
titel: "Loop Engineering: Warum das Ziel wichtiger geworden ist als der Prompt"
bildtitel: "Ziel statt Prompt"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/47-loop-engineering"
---

# Loop Engineering: Warum das Ziel wichtiger geworden ist als der Prompt

*Ein Loop bekommt kein Kommando, sondern ein Ziel, messbare Erfolgskriterien und die Anweisung, sich selbst zu prüfen. Das funktioniert, hat aber einen blinden Fleck: Ein System, das sich selbst bewertet, bewertet sich gut.*

Von Mark Zimmermann

Vor zwei, drei Jahren lautete die Frage, wer den besten Prompt schreibt. Inzwischen lautet sie, wer die beste Schleife baut. Andrej Karpathy hat kürzlich öffentlich gemacht, dass er Loop Engineering für wichtiger hält als Prompt Engineering, und das deckt sich mit dem, was in der Praxis passiert.

Der Weg dorthin verlief in Etappen. Am Anfang stand eine Prompt-Datenbank in Notion, also eine Sammlung von Formulierungen, die einmal funktioniert hatten. Danach kamen Skills: Markdown-Dateien mit Unter-Skills und ausführbarem Python-Code, die ein Agent bei Bedarf lädt. Der Schritt zum Loop ist der dritte und verändert die Rolle des Menschen stärker als die beiden davor.

> **kurz & knapp**
>
> - Ein Loop bekommt ein Ziel und Erfolgskriterien, keinen einzelnen Auftrag
> - Er prüft sich selbst und wiederholt, bis die Kriterien erfüllt sind
> - Die Prüfung gehört an ein anderes Modell: Wer sich selbst bewertet, bestätigt sich
> - Laufzeiten von 10 bis 20 Stunden für eine Aufgabe sind normal geworden
> - Mit der Zahl paralleler Loops wird Kontextverwaltung zum eigentlichen Engpass

## Was einen Loop von einem Prompt unterscheidet

Die Definition ist knapp und trägt weit.

> „Wir definieren einen Prompt, der das System anweist: Was ist mein Ziel, was sind meine ganz konkreten Kriterien, an denen ich festmache, dass ich mein Ziel erreiche. Und das System überprüft stetig, ob das Ziel erreicht ist, und wiederholt sich selbst so lange, bis das Ziel erreicht ist.“
>
> **Mark Zimmermann**, Co-Host

Der Unterschied liegt in der Verlagerung der Verantwortung. Bei einem Prompt beschreibt der Mensch den Weg und beurteilt das Ergebnis. Bei einem Loop beschreibt der Mensch das Ziel und die Messlatte, den Weg sucht die Maschine.

Damit verschiebt sich auch die Arbeit des Menschen. Sie liegt nicht mehr in der Formulierung, sondern in der Frage, woran man Erfolg eigentlich erkennt. Das ist eine Spezifikationsaufgabe, und sie ist unangenehmer, weil sie keine vagen Ziele zulässt. „Mach das gut“ ist kein Erfolgskriterium. „Alle zehn Testfälle laufen durch, und der Bericht nennt jeden einzeln mit Status“ ist eines.

> ### Warum ausgerechnet Schleifen
>
> Der Begriff wirkt zunächst überraschend, weil Schleifen zu den ältesten Konstrukten der Programmierung gehören. Neu ist, was in der Schleife steht.
>
> Bereits die Textgenerierung selbst ist eine Schleife: Das Modell sagt ein Token vorher, hängt es an und beginnt von vorn. Loop Engineering setzt eine Ebene darüber an. Dort steht in der Schleife nicht ein Token, sondern ein vollständiger Arbeitsschritt mit Werkzeugaufrufen, und die Abbruchbedingung ist kein Zeichenlimit, sondern ein fachliches Kriterium.
>
> Praktisch braucht ein solcher Loop drei Angaben: das Ziel, die überprüfbaren Kriterien und eine Obergrenze. Fehlt die Obergrenze, läuft die Schleife entweder gegen ein Kontingent oder sie erzeugt Nebenwirkungen, die niemand bestellt hat.

## Der blinde Fleck: Selbstbewertung

Der wichtigste Warnhinweis der Folge betrifft die Prüfung. Wer ein System seine eigene Arbeit bewerten lässt, bekommt in der Regel Zustimmung zurück.

Das ist keine Bosheit der Maschine, sondern eine Folge davon, wie die Bewertung zustande kommt. Dasselbe Modell mit demselben Kontext, das eine Lösung erzeugt hat, hält sie beim Nachprüfen für richtig, weil es dieselben Annahmen mitbringt. Ein Fehler, der beim Erzeugen nicht aufgefallen ist, fällt beim Prüfen ebenfalls nicht auf.

Der Ausweg ist organisatorisch, nicht technisch: Das Ergebnis wird von einem anderen Modell geprüft. Peter Steinberger hat den Ansatz samt des dafür anfallenden Tokenverbrauchs öffentlich beschrieben, und der Verbrauch ist der Preis dafür.

Ein bewährter Ablauf sieht so aus: erst planen lassen, dann den Plan von einem Kritiker-Skill und einem Meta-Analyse-Skill gegenprüfen lassen, dann die Umsetzung als Goal Loop starten. Dass ein solcher Lauf 10, 12 oder 20 Stunden dauert, ist dabei kein Fehler, sondern die Betriebsart.

## Harness Engineering wird zum Engpass

Je mehr Agenten und Loops parallel arbeiten, desto weniger entscheidet das Modell und desto mehr entscheidet der Rahmen. Zwei Themen treten dabei hervor.

Das erste ist Kontext und Memory. Ein Loop, der über Stunden läuft, muss wissen, was vorher galt, und darf nicht bei jedem Neustart von vorn anfangen. Wie schnell Kontext verloren geht, hat die kurzfristige Abschaltung eines Modells gezeigt: Was in dessen Sitzungen lag, war weg. Alles, was überleben soll, gehört in eine eigene, anbieterunabhängige Ablage.

Das zweite ist Governance. Sobald Skills ausführbaren Code enthalten und Agenten auf Unternehmenssysteme zugreifen, stellen sich die üblichen Fragen: Wer darf einen Skill in Umlauf bringen, wie wird er signiert, wie lässt sich im Nachhinein nachvollziehen, was ein Agent getan hat. Diese Fragen sind nicht neu, sie sind aus der Softwareverteilung bekannt. Neu ist, dass sie jetzt für Textdateien gelten, die jeder Fachbereich schreiben kann.

Begrifflich lohnt eine Abgrenzung: Ein Harness ist der Rahmen, in dem Agenten arbeiten, also Werkzeuge, Kontext, Regeln und Prüfung. Ein Agentic OS wäre eine Ebene darüber, mit Ressourcenverwaltung und Scheduling über konkurrierende Agenten hinweg. Was heute gebaut wird, sind Harnesses.

## Fazit

Loop Engineering ist keine neue Technik, sondern eine Verlagerung der Sorgfalt. Sie wandert von der Formulierung zur Spezifikation, und dort ist sie besser aufgehoben, weil Spezifikationen einen Modellwechsel überleben.

Für den Einstieg genügen drei Regeln. Definieren Sie das Ziel so, dass eine Maschine prüfen kann, ob es erreicht ist. Lassen Sie die Prüfung von etwas anderem erledigen als von dem, was die Arbeit gemacht hat. Und setzen Sie eine Obergrenze, bevor Sie den Lauf starten.

Es geht nicht darum, mit möglichst vielen Tokens zu beeindrucken. Es geht darum, ein klares Ziel zu definieren und der Maschine den Weg dorthin zu überlassen.

> **The story continues …**
>
> Offen bleibt die Frage nach Auditierbarkeit im Unternehmenseinsatz. Signierte Skills, nachvollziehbare Agentenprotokolle und eine Freigabekette für ausführbare Anweisungen sind derzeit weitgehend Handarbeit. Bis dafür Standards existieren, gilt dasselbe wie bei Makros vor zwanzig Jahren: Wer sie einsammelt und prüft, hat später weniger Arbeit.

---

Die ganze Folge: [Loop Engineering](https://think-ai.podigee.io/47-loop-engineering)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
