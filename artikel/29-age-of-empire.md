---
folge: 29
titel: "Zehn Agenten, zehn Terminalfenster: Warum das Chat-Interface an seine Grenze kommt"
bildtitel: "Zehn Agenten, ein Fenster"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/29-age-of-empire"
---

# Zehn Agenten, zehn Terminalfenster: Warum das Chat-Interface an seine Grenze kommt

*Aufbausimulationen machen seit Jahrzehnten tausende Einheiten und Lieferketten überschaubar. Agenten werden dagegen über nebeneinanderliegende Terminalfenster gesteuert. Das ist kein Detail, sondern der Engpass.*

Von Mark Zimmermann

Ein Prompt, eine Antwort: Für ein Gespräch mit einem Modell ist das die richtige Form. Für die Steuerung mehrerer parallel arbeitender Agenten ist sie es nicht, sobald Skills, MCP-Anbindungen, Gedächtnisdateien und Budgetverbrauch gleichzeitig im Blick bleiben müssen.

Der Titel der Folge ist eine Verbeugung vor Age of Empires, und die Analogie trägt weiter als der Scherz.

> **kurz & knapp**
>
> - Das Chat-Interface skaliert nicht über eine Handvoll paralleler Agenten hinaus
> - Aufbausimulationen lösen dasselbe Problem seit Jahrzehnten visuell
> - Erste Ansätze stellen Agenten als Figuren in einer Spielwelt dar, samt Zonen für Rechte
> - Vier Abstufungen menschlicher Kontrolle: in the Loop, on the Loop, in the Lead, out of the Loop
> - Nicht Kontrolle entscheidet über Vertrauen, sondern Verständlichkeit

## Warum Spiele das besser können

Fabrik- und Wirtschaftssimulationen machen tausende Einheiten, Lieferketten und Produktionslinien beherrschbar. Sie tun das mit Mitteln, die in Entwicklerwerkzeugen kaum vorkommen: eine Übersichtskarte, Zustandsfarben, Warnsymbole an der Stelle des Problems, Gruppierung gleichartiger Einheiten und die Möglichkeit, zwischen Überblick und Detail zu wechseln, ohne das eine für das andere aufzugeben.

Ein Terminalfenster kann davon nichts. Es zeigt eine Sache, chronologisch, und wer zehn davon offen hat, hat zehn Chroniken und keinen Überblick.

Erste Ansätze in diese Richtung gibt es. Werkzeuge wie Agent Craft oder das erwähnte Projekt pixel-agents stellen Agenten als Figuren in einer Spielwelt dar, inklusive Sicherheitszonen, die per Rechtevergabe festlegen, wo ein Agent überhaupt hinlaufen darf.

Der letzte Punkt ist der interessanteste. Rechte räumlich darzustellen macht sie überprüfbar. Eine Berechtigungsmatrix liest niemand. Eine Zone, in die eine Figur nicht hineinlaufen kann, versteht jeder.

## Vier Stufen der Kontrolle

Ein zweiter Schwerpunkt betrifft eine Begriffsschärfung, die in Diskussionen ständig durcheinandergeht.

> ### Human in the Loop bis Human out of the Loop
>
> **Human in the Loop:** Der Mensch ist Teil des Ablaufs. Nichts geschieht ohne seine Freigabe. Sicher, langsam, und ab einer gewissen Zahl von Vorgängen nicht durchhaltbar, weil die Freigabe zur Formsache verkommt.
>
> **Human on the Loop:** Der Ablauf läuft selbständig, der Mensch beobachtet und kann eingreifen. Das ist die Stufe, auf der die meisten produktiven Systeme landen. Sie funktioniert nur, wenn Auffälligkeiten sichtbar werden, ohne dass jemand danach sucht.
>
> **Human in the Lead:** Der Mensch setzt Ziele und Grenzen, das System sucht den Weg. Kontrolle findet über Vorgaben und Ergebnisprüfung statt, nicht über Einzelschritte.
>
> **Human out of the Loop:** Kein Mensch beteiligt. Für eng umgrenzte, gut verstandene Aufgaben mit begrenztem Schaden vertretbar, sonst nicht.
>
> Die Stufen sind keine Reifegrade, bei denen die letzte die beste wäre. Sie sind eine Auswahl, und die richtige Wahl hängt vom möglichen Schaden ab. Der häufigste Fehler ist, faktisch auf Stufe zwei zu arbeiten und formal Stufe eins zu behaupten.

Mit steigender Zahl von Agenten wird diese Unterscheidung wichtiger, weil die erste Stufe schlicht nicht mehr trägt.

## Gaming-Erfahrung als Arbeitsfähigkeit

Augenzwinkernd, aber nicht ohne Substanz, wird die These aufgestellt, dass Erfahrung mit Echtzeitstrategie und World of Warcraft zu einer gefragten Fähigkeit wird. Delegieren an viele gleichzeitig handelnde Einheiten und deren Überwachung ist genau das, was Strategiespieler seit Jahren trainieren.

Nüchtern betrachtet geht es dabei um Aufmerksamkeitsverteilung: erkennen, wo gerade etwas schiefläuft, ohne alles gleichzeitig zu beobachten. Das ist eine erlernbare Fähigkeit und in klassischen IT-Ausbildungen kaum enthalten.

## Was daneben passiert ist

Der Nachrichtenteil der Folge enthält eine bemerkenswerte Gegenüberstellung. Anthropic lehnt unter Dario Amodei einen Pentagon-Vertrag ab, weil Massenüberwachung und autonome Waffensysteme nicht ausgeschlossen werden können. OpenAI unterschreibt kurz darauf denselben Vertrag.

Dazu eine sehr praktische Frage: Wie zieht man seine KI-Historie zwischen Anbietern um. Über den Datenexport bei ChatGPT und einen Migrationsprompt bei Claude geht es teilweise. Dass diese Frage überhaupt aufkommt, zeigt, wie sehr Alltag und Modellwahl inzwischen verwoben sind, und wie wenig Wechselmöglichkeit tatsächlich besteht.

## Fazit

Die Folge endet mit einem Satz, der als Leitmotiv taugt: Vertrauen bleibt die eigentliche letzte Herausforderung an die Bedienoberfläche.

Der Punkt dahinter ist präzise. Nicht Kontrolle entscheidet darüber, ob wir einem System mit vielen autonomen Teilen vertrauen, sondern Verständlichkeit. Ein System, das seine Vorgänge nachvollziehbar zeigt, wird auch dann akzeptiert, wenn man nicht jeden Schritt freigibt. Ein System, das undurchsichtig arbeitet, wird auch mit Freigabeknopf nicht vertrauenswürdig, weil niemand weiß, was er freigibt.

Für die eigene Umgebung folgt daraus eine einfache Prüfung. Sehen Sie auf einen Blick, wie viele Agenten laufen, was sie tun und welcher davon Aufmerksamkeit braucht? Wenn die Antwort „ich habe die Fenster nebeneinander“ lautet, ist die Oberfläche der Engpass und nicht das Modell.

> **The story continues …**
>
> Zwei Randthemen aus dieser Folge verdienen eigene Betrachtungen: das MIT-Experiment, in dem KI-Agenten in einer Minecraft-Welt eigenständig Kulturen, Währungen und Religionen entwickelten, und biologische Neuronen-Chips, die inzwischen Doom spielen. Beides klingt nach Kuriosität und berührt Fragen, die noch niemand sortiert hat.

---

Die ganze Folge: [Age of Agents](https://think-ai.podigee.io/29-age-of-empire)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
