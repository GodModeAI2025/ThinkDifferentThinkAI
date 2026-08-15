---
folge: 38
titel: "Wenn der Agent über Nacht durcharbeitet: Sandbox, Watchdog und der Preis der Denktiefe"
bildtitel: "Was macht der Agent nachts?"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/38-ki-schlaeft-nicht"
---

# Wenn der Agent über Nacht durcharbeitet: Sandbox, Watchdog und der Preis der Denktiefe

*Ein Coding-Agent, der nach 20 Minuten den Kontext verliert, ist ein Werkzeug. Einer, der acht Stunden durchläuft, ist ein Mitarbeiter mit Systemzugriff. Was das an Absicherung verlangt, und was die höchste Denkstufe tatsächlich kostet.*

Von Mark Zimmermann

Diese Folge kommt ohne Gast aus und mit einer Menge Neuigkeiten aus einer Branche, die inzwischen häufiger Modelle veröffentlicht, als andere Leute die Unterhose wechseln.

Der Kern ist trotzdem eine einzige Frage: Was passiert, wenn ein Agent nicht mehr nach 20 Minuten abbricht, sondern über Nacht durcharbeitet.

> **kurz & knapp**
>
> - Claude Opus 4.7 bringt Effort-Modi von Medium bis Max; im Maximalmodus können bis zu 40 Prozent höhere Kosten anfallen
> - Ein autonom laufender Agent braucht Sandbox, Hooks, Watchdog mit Heartbeat und ein Protokoll seiner Entscheidungen
> - Claude Design greift Figma an und importiert bestehende Design-Systeme
> - Vertrauen in einen Anbieter zählt für die Werkzeugwahl so viel wie Benchmark-Werte
> - Viele Tokens verbrennen dabei, dass Menschen Ergebnisse zwischen zwei Modellen hin- und herschieben

## Der Preis der Denktiefe

Claude Opus 4.7 führt Effort-Modi ein: Medium, High, X-High und Max, dazu eine feinere Tokenisierung. Beides erhöht die Genauigkeit und beides kostet.

Die Größenordnung ist relevant für jede Kalkulation: Im Maximalmodus können bis zu 40 Prozent mehr Kosten anfallen. Das ist kein Rundungsfehler, sondern ein Faktor, der über die Wirtschaftlichkeit eines Anwendungsfalls entscheidet.

Daraus folgt eine Steuerungsfrage, die viele Werkzeuge noch nicht beantworten: Wie viel Kontrolle will man über die automatische Delegation an kleinere Modelle haben. Ein System, das selbständig auf ein schwächeres Modell umschaltet, spart Geld und ändert unter Umständen das Ergebnis. Ein System, das das nie tut, ist teuer. Beides ohne Transparenz zu betreiben ist die schlechteste Variante.

Wichtig dabei: Für die Werkzeugwahl zählt am Ende nicht nur die Messlatte. Vertrauen in den Anbieter entscheidet mit, weil man ihm laufende Prozesse und Daten überlässt. Benchmark-Werte ändern sich im Quartalstakt, eine Anbieterbeziehung nicht.

## Der Agent, der durchläuft

Der eigentliche Kern der Folge ist ein Aufbau namens Claude Night Shift: eine Kombination aus Skills und Shell-Skripten mit Runbooks, Hooks, einer macOS-Sandbox und einem Watchdog mit Heartbeat-Überwachung. Damit wird aus einem interaktiven Werkzeug ein autonom arbeitender Prozess, der destruktive Befehle blockiert und seine Entscheidungen nachvollziehbar dokumentiert.

Die Bestandteile sind einzeln unspektakulär und in ihrer Kombination genau das, was fehlt, wenn Leute Agenten unbeaufsichtigt laufen lassen.

> ### Was ein autonom laufender Agent braucht
>
> **Sandbox.** Ein abgegrenzter Bereich, in dem der Agent schreiben darf. Ohne diese Grenze entscheidet allein die Formulierung des Auftrags darüber, welche Dateien betroffen sind, und das ist keine Sicherheitsmaßnahme.
>
> **Hooks.** Eingriffspunkte vor und nach bestimmten Aktionen. Dort lassen sich destruktive Befehle abfangen, bevor sie ausgeführt werden, und Ergebnisse prüfen, bevor sie übernommen werden.
>
> **Watchdog mit Heartbeat.** Ein Prozess, der überwacht, ob der Agent noch lebt und noch Fortschritt macht. Ohne ihn unterscheidet sich ein hängender Lauf äußerlich nicht von einem arbeitenden, und das fällt erst am nächsten Morgen auf.
>
> **Runbook.** Die schriftliche Festlegung, was zu tun ist, wenn etwas schiefgeht. Bei nächtlichen Läufen ist niemand da, der improvisiert.
>
> **Entscheidungsprotokoll.** Nachvollziehbar festgehalten, warum der Agent einen Weg gewählt hat. Ohne dieses Protokoll ist ein Ergebnis am Morgen nicht bewertbar, sondern nur abnehmbar oder verwerfbar.

Wer diese fünf Punkte nicht hat und trotzdem über Nacht laufen lässt, betreibt kein autonomes System, sondern ein unbeaufsichtigtes.

## Claude Design und der Werkzeugkasten

Der andere Schwerpunkt ist Claude Design, Anthropics Design- und Prototyping-Werkzeug. Der Funktionsumfang reicht von Wireframes über funktionale Animationen bis zum Import bestehender Figma-Dateien und Design-Systeme, und ein Wochenende Ausprobieren hat gereicht, um ernsthaft über einen Wechsel nachzudenken.

Der Import ist dabei der interessante Teil. Ein Werkzeug, das bestehende Design-Systeme aufnimmt, greift nicht den Zeichenvorgang an, sondern die Wechselkosten. Genau daran sind bisherige Herausforderer wie Google Stitch gescheitert.

Parallel dazu ist Bildgenerierung im Alltag angekommen: Nano Banana bei Gemini, GPT Image 1.5, dazu Werkzeuge wie Manus oder Crea.ai, die das nachträgliche Bearbeiten von Text auf generierten Infografiken lösen. Das war lange die praktische Schwachstelle, weil ein Diagramm mit falsch geschriebener Beschriftung unbrauchbar ist.

## Die Token-Verschwendung, über die niemand spricht

Zum Schluss eine Beobachtung, die Kosten spart, sobald man sie einmal gesehen hat. Ein erheblicher Teil des Verbrauchs entsteht dadurch, dass Menschen KI-generierte Dokumente zwischen zwei Modellen hin- und herschieben. Ergebnis aus einem System kopieren, in ein anderes einfügen, Antwort zurückkopieren.

Jeder dieser Schritte kostet Tokens für Inhalte, die bereits einmal verarbeitet wurden. Die Alternative sind direkte Verbindungen zwischen den Systemen, über A2A oder MCP. Der Aufwand dafür ist einmalig, die Ersparnis läuft mit.

Damit hängt eine Frage zusammen, die die Folge offen stellt: Wann hört Automatisierung auf, Prokrastination zu sein, und fängt an, Arbeit zu erledigen. Ein Aufbau, der drei Tage Bastelei kostet und zehn Minuten pro Woche spart, ist ein Hobby. Das ist in Ordnung, sollte aber so genannt werden.

## Fazit

Die Folge liefert eine klare Trennlinie. Ein Agent, den man beobachtet, braucht ein gutes Modell. Ein Agent, der unbeaufsichtigt läuft, braucht eine Umgebung.

Bevor Sie den ersten nächtlichen Lauf starten, klären Sie fünf Dinge: Wo darf er schreiben, was darf er nicht ausführen, wer merkt, dass er hängt, was passiert dann, und woran erkennen Sie am Morgen, ob das Ergebnis brauchbar ist.

Und prüfen Sie Ihre Kostenrechnung gegen den höchsten Effort-Modus, nicht gegen den mittleren. Der Unterschied von bis zu 40 Prozent entscheidet häufiger über die Wirtschaftlichkeit als die Modellwahl selbst.

> **The story continues …**
>
> Nebenbei entstand an einem Wochenende ein Meetingassistent für eine AR-Brille von Even Realities. Solche Aufbauten sind derzeit Einzelstücke. Interessant werden sie, sobald jemand die Frage beantwortet, wie ein Agent, der permanent mithört, mit den Rechten der Anwesenden umgeht.

---

Die ganze Folge: [KI schläft nicht !](https://think-ai.podigee.io/38-ki-schlaeft-nicht)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
