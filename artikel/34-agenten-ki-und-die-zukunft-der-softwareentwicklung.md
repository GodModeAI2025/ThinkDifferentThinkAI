---
folge: 34
titel: "Threat Modeling für Agenten: Vier Fragen, bevor die KI ans Bankkonto darf"
bildtitel: "Vier Fragen vor dem Zugriff"
kicker: "Im Gespräch mit Alex und Klaus"
podigee: "https://think-ai.podigee.io/34-agenten-ki-und-die-zukunft-der-softwareentwicklung"
---

# Threat Modeling für Agenten: Vier Fragen, bevor die KI ans Bankkonto darf

*Ein Agent soll die monatliche Buchhaltung übernehmen: Rechnungen aus dem Postfach, Kontoauszug, PDF-Export. Sobald er an Bankdaten kommt, wird aus einer Werkzeugfrage eine Sicherheitsfrage.*

Von Mark Zimmermann

Diese Folge entsteht ausnahmsweise ohne Jens, dafür mit zwei wiederkehrenden Gästen. Der Ausgangspunkt ist ein Anwendungsfall, wie er in vielen kleinen Büros liegt: Die monatliche Buchhaltung soll automatisiert werden, Rechnungen kommen per Mail, dazu Kontoauszug und PDF-Export. Die Frage lautet, ob dafür OpenClaw oder Craft Agents das richtige Werkzeug ist.

Die Antwort ist ein begründetes „kommt drauf an“, und der interessante Teil steht dahinter.

> **kurz & knapp**
>
> - Craft Agents ist eine grafische Alternative zu Claude Code auf Basis des Claude SDK, ohne Terminal
> - Aufgaben laufen dort weiter, auch wenn die Anwendung geschlossen ist
> - Quer über Claude Code, OpenCode und OpenClaw hat sich ein gemeinsames Musterbuch etabliert: Skills, Plugins, Hooks, Evaluations
> - Adam Shostacks Four-Question-Framework lässt sich als eigener Skill vor jedem Commit ausführen
> - Das größte Sicherheitsrisiko ist, dass viele Anwender nicht wissen, was ein Token ist

## Werkzeugwahl ohne Terminal

Craft Agents tritt als grafische Alternative zu Claude Code an, aufgebaut auf dem Claude SDK. Kein Terminal, dafür MCP-Anbindungen, Skills und Aufgaben, die weiterlaufen, wenn die Anwendung geschlossen ist.

Diese letzte Eigenschaft ist praktisch der entscheidende Unterschied. Ein Agent, der nur läuft, solange ein Fenster offen ist, taugt für interaktive Arbeit. Ein Agent, der Aufträge über Stunden abarbeitet, braucht eine Ausführung, die vom Bildschirm unabhängig ist.

Die Alltagsbeispiele in der Folge sind bezeichnend unspektakulär: ein Notion-Token, das ständig neu authentifiziert werden muss, und eine Anwendung zur Audiotranskription für Kolleginnen, die mit IT nichts zu tun haben. Beides sind keine Softwareprojekte, sondern Reibungspunkte, die jemand beseitigt.

Bemerkenswert ist, was sich dabei quer über die Werkzeuge herausgebildet hat. Skills, Plugins, Hooks und Evaluations tauchen in Claude Code, OpenCode und OpenClaw in vergleichbarer Form auf. Es entsteht ein gemeinsames Musterbuch, noch bevor es einen Standard gibt. Wer die Begriffe in einem Werkzeug verstanden hat, findet sich in den anderen zurecht.

## Wenn der Agent ans Konto darf

Ernst wird es an dem Punkt, an dem der Agent Zugriff auf Bankdaten oder das Postfach bekommen soll. Die Runde diskutiert Sandboxing, Netzwerksegmentierung und Zero-Trust-Prinzipien, und der Ton bleibt dabei angenehm unaufgeregt.

Die Kernaussage ist keine Warnung vor der Technik, sondern eine Beobachtung über die Anwender: Viele wissen schlicht nicht, was ein Token ist. Genau das wird zum Sicherheitsrisiko. Wer nicht versteht, dass eine Zeichenkette in einer Konfigurationsdatei dieselben Rechte trägt wie das eigene Passwort, geht damit entsprechend um.

> ### Die vier Fragen von Adam Shostack
>
> Das Four-Question-Framework ist die kürzeste brauchbare Form von Threat Modeling und kommt ohne Werkzeugkette aus:
>
> **Was bauen wir?** Ein Bild oder eine Liste der beteiligten Komponenten und der Wege zwischen ihnen. Ohne diesen Schritt diskutieren alle über verschiedene Systeme.
>
> **Was kann schiefgehen?** Die eigentliche Bedrohungsanalyse. Wer könnte was erreichen wollen, und über welchen der eingezeichneten Wege.
>
> **Was tun wir dagegen?** Je gefundener Bedrohung eine Maßnahme oder eine bewusste Entscheidung, sie zu akzeptieren.
>
> **Haben wir gute Arbeit geleistet?** Der Rückblick, der aus der Übung eine Gewohnheit macht.
>
> Klaus hat sich das als eigenen Skill in Craft Agents gebaut und lässt es automatisiert vor jedem Commit laufen. Das ist die wirksamste Form: nicht ein Workshop pro Jahr, sondern vier Fragen bei jeder Änderung.

Für die Praxis lohnt es sich, die Reihenfolge einzuhalten. Wer bei Frage zwei anfängt, sammelt Schreckensszenarien ohne Bezug zum System. Wer bei Frage drei anfängt, kauft Maßnahmen gegen Bedrohungen, die er nicht hat.

## Was das mit Softwarearchitektur macht

Der zweite große Block betrifft Teamstrukturen. Klaus berichtet, wie sein früherer Purismus aufgeweicht ist: strikt natives iOS in Swift, striktes Kotlin für Android, kein Cross-Platform. Diese Haltung war begründet, solange nativer Code teuer war und plattformübergreifende Werkzeuge Kompromisse erzwangen.

Inzwischen erzeugen Agenten für beide Plattformen nativen Code, und die Teamgrenze zwischen iOS- und Android-Entwicklung verschwimmt. Was die Trennung ursprünglich gerechtfertigt hat, war die Spezialisierung auf eine Sprache und ein Framework. Wenn diese Spezialisierung an Gewicht verliert, verliert auch die Trennung ihren Grund.

Daraus ergibt sich die weitergehende Frage, die in der Folge diskutiert und nicht abschließend beantwortet wird: Trägt der klassische Anwendungsschnitt in Frontend-Team, Backend-Team und App-Team überhaupt noch? Er ist entlang von Technologiegrenzen gezogen, und genau diese Grenzen werden gerade durchlässig.

Beachten Sie, was dabei nicht verschwindet. Die Kenntnis der Plattform, ihrer Freigabeprozesse, ihrer Eigenheiten und ihrer Fehlerbilder bleibt nötig. Was ein Agent erzeugt, muss jemand beurteilen können.

## Fazit

Die Folge liefert eine praktische Reihenfolge für alle, die einen Agenten an echte Daten lassen wollen.

Klären Sie zuerst, ob das Werkzeug Aufgaben ohne offenes Fenster ausführt. Danach richtet sich, ob Sie überhaupt automatisieren oder nur assistieren.

Führen Sie zweitens die vier Fragen durch, bevor Sie Zugangsdaten hinterlegen. Das dauert zwanzig Minuten und ist der einzige Schritt in dieser Liste, den niemand nachholt, wenn er ihn einmal übersprungen hat.

Und sorgen Sie drittens dafür, dass jeder, der mit solchen Werkzeugen arbeitet, weiß, was ein Token ist und welche Rechte daran hängen. Das ist keine Schulung, sondern ein Satz in der Einweisung, und es verhindert mehr Schaden als jede zusätzliche Software.

Der Ton der Folge ist dabei das Vorbild: keine Panik vor Agenten, die alles hacken, sondern die nüchterne Feststellung, dass Unkenntnis das eigentliche Risiko ist.

> **The story continues …**
>
> Wenn Technologiegrenzen zwischen Teams durchlässig werden, stellt sich die Frage nach dem richtigen Schnitt neu. Naheliegend wäre ein Schnitt entlang fachlicher Verantwortung statt entlang der Plattform. Wer das ernsthaft versucht, wird zuerst merken, dass die Karrierewege in Organisationen noch entlang der alten Grenzen verlaufen.

---

Die ganze Folge: [Agenten, KI und die Zukunft der Softwareentwicklung](https://think-ai.podigee.io/34-agenten-ki-und-die-zukunft-der-softwareentwicklung)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
