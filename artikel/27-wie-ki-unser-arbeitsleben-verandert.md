---
folge: 27
titel: "Agentic Engineering: Was von Softwarearchitektur übrig bleibt"
bildtitel: "Das Ende der Wiederverwendbarkeit?"
kicker: "Im Gespräch mit Klaus Rodewig und Alexander Heusingfeld"
podigee: "https://think-ai.podigee.io/27-wie-ki-unser-arbeitsleben-verandert"
---

# Agentic Engineering: Was von Softwarearchitektur übrig bleibt

*Wenn nativer Code in Minuten aus einer JSON-Struktur oder einem Figma-Screenshot entsteht, verlieren Wiederverwendbarkeit und Sprachwahl an Gewicht. Zwei Praktiker aus dem Vorwerk-Umfeld ziehen daraus eine steile These und liefern die Einschränkungen gleich mit.*

Von Mark Zimmermann

Zu Gast sind Klaus Rodewig und Alexander Heusingfeld, beide bei Vorwerk, Alexander zusätzlich Host des Podcasts „Conversations about Software Engineering“. Beide legen offen, dass sie skeptisch angefangen haben. Ausgelöst hat den Umschwung GitHub Copilot, verstärkt hat ihn Claude Code.

Der Ausgangspunkt ist eine nüchterne Beobachtung über Halbwertszeiten. Was vor einem halben Jahr n8n war, ist inzwischen OpenClaw. Was vor einem Monat OpenClaw war, ist inzwischen Craft Agent. Dieses Tempo überfordert Teams, und zwar unabhängig von deren Fähigkeit.

> **kurz & knapp**
>
> - Wiederverwendbarkeit, App-Architektur und Sprachwahl verlieren an Gewicht, wenn Code in Minuten entsteht
> - Vibecoding nutzt KI als qualifizierte Autovervollständigung, Agentic Engineering übergibt Ende-zu-Ende-Verantwortung
> - Teamgrenzen zwischen Frontend und Backend waren organisatorisch begründet, nicht technisch
> - Ein agentischer Regelkreis kann quartalsweise ISMS-Audits nach ISO 27001 ablösen
> - Ein Agent darf keinen Schreibzugriff auf seine eigenen Kerndateien haben

## Die steile These

Wenn eine Maschine in Minuten nativen Code aus einer JSON-Struktur oder einem Figma-Screenshot erzeugt, verlieren drei Dinge an Bedeutung: Wiederverwendbarkeit, Softwarearchitektur im Sinne von App-Architektur und sogar die Wahl der Programmiersprache.

Die Analogie, die beide Gäste dafür wählen, stammt aus der eigenen Laufbahn: der Übergang von Assembler zu Hochsprachen. Damals galt handoptimierter Assembler als überlegen, und er war es auch, gemessen an Laufzeit. Er hat trotzdem verloren, weil der Vorteil den Aufwand nicht mehr wert war.

Beachten Sie, worauf sich die These bezieht. Sie betrifft App-Architektur, also die interne Struktur einer Anwendung. Sie betrifft nicht Systemarchitektur: Wie Systeme zusammenspielen, wo Daten liegen, welche Verträge zwischen Diensten gelten. Dieser Teil wird eher wichtiger, weil mehr Einzelteile entstehen.

Wiederverwendbarkeit verliert aus einem konkreten Grund an Wert: Sie war eine Antwort auf teure Erstellung. Eine Bibliothek zu bauen, zu pflegen und in fünf Projekten einzusetzen lohnte sich, solange Neuschreiben teuer war. Sinkt dieser Preis, kippt die Rechnung, und der Wartungsaufwand der geteilten Bibliothek bleibt.

## Vibecoding gegen Agentic Engineering

Der Kern der Folge ist eine Unterscheidung, die in vielen Diskussionen fehlt.

Vibecoding heißt, KI als qualifizierte Autovervollständigung zu nutzen. Der Mensch bleibt im Ablauf, entscheidet jeden Schritt und übernimmt Vorschläge.

Agentic Engineering heißt, Agenten-Teams Ende-zu-Ende-Verantwortung zu übertragen, über Frontend- und Backend-Grenzen hinweg. Die entscheidende Bemerkung dazu: Diese Grenzen existierten aus organisatorischen Gründen, nicht aus technischen. Ein Agent, der beide Seiten gleichzeitig ändert, verletzt keine technische Notwendigkeit, sondern eine Zuständigkeitsregelung.

Das ist eine unbequeme Erkenntnis für Organisationen, die ihre Teamstruktur für eine Architekturentscheidung halten.

> ### Guardrails, konkret
>
> Am Beispiel OpenClaw wird in der Folge ein Punkt erklärt, der leicht übersehen wird: Ein Agent darf keinen Schreibzugriff auf seine eigenen Kerndateien haben, also auf die Dateien, die sein Verhalten und seine Identität festlegen.
>
> Der Grund ist nicht Misstrauen, sondern Logik. Ein System, das seine eigenen Regeln ändern darf, hat keine Regeln, sondern Vorschläge. Und da ein Agent auf Hilfsbereitschaft optimiert ist, wird er eine Regel, die einer Aufgabe im Weg steht, im Zweifel als Hindernis behandeln.
>
> Technisch ist die Umsetzung einfach: Schreibrechte entziehen, Konfiguration außerhalb des beschreibbaren Bereichs ablegen, Änderungen nur über einen Weg zulassen, der einen Menschen einschließt.
>
> Die nächste Baustelle ist eine Ebene darüber: eine Meta-Instanz, die alle laufenden Agenten prüft. Manche nennen das Agent-Orchestration-Platform. Fertige Antworten gibt es dafür noch nicht.

## Compliance als Regelkreis

Der praktisch überraschendste Teil kommt aus der Compliance. Ein Informationssicherheits-Managementsystem nach ISO 27001 arbeitet klassisch mit Audits in festen Abständen, häufig quartalsweise. Zwischen zwei Audits weiß niemand genau, wie es steht.

Ein agentischer Regelkreis kann das ablösen: kontinuierliche Prüfung statt Stichproben zu festen Terminen. Vor dem Hintergrund des EU Cyber Resilience Act ist das mehr als eine Bequemlichkeit, weil dort fortlaufende Nachweise erwartet werden.

Wichtig dabei: Kontinuierliche Prüfung ersetzt das Audit nicht, sie füttert es. Ein Auditor will Belege sehen, und ein Regelkreis erzeugt sie fortlaufend, statt sie kurz vorher zusammenzusuchen.

## Drei Ratschläge zum Einstieg

Die Folge endet ungewöhnlich konkret, und die drei Punkte sind unmittelbar anwendbar.

**Keine Annahmen treffen.** Probieren Sie echte Alltagsfälle in einer isolierten Umgebung aus, vom automatisierten Rechnungsexport bis zum eigenen MCP-Server für Mail, Kalender und Erinnerungen. Die Einschätzung aus zweiter Hand ist bei diesem Tempo wertlos.

**Muster statt Werkzeugnamen verstehen.** Skills, Plugins, Validation Loops und MCP tauchen in jedem dieser Werkzeuge auf. Wer die Muster kennt, ist beim nächsten Namenswechsel nicht bei null. Wer Werkzeugnamen sammelt, fängt jedes Mal von vorn an.

**Datenfluss bewusst steuern.** Der Satz dazu ist der wichtigste der ganzen Folge: Dass eine Anwendung lokal installiert ist, heißt längst nicht mehr, dass die Daten lokal bleiben. Prüfen Sie das je Werkzeug, nicht je Kategorie.

## Fazit

Die These vom Ende der Softwarearchitektur ist bewusst zugespitzt und trifft einen realen Kern: Was aus teurer Erstellung entstanden ist, verliert an Wert, wenn Erstellung billig wird.

Was bleibt, ist alles, was mit Zusammenspiel zu tun hat: Schnittstellen, Datenhoheit, Betrieb, Nachvollziehbarkeit und die Frage, wer verantwortet, was ein Agent getan hat.

Für Teams heißt das konkret: Prüfen Sie, welche Ihrer Strukturen technisch begründet sind und welche organisatorisch. Die zweite Sorte steht gerade zur Disposition, und es ist besser, das selbst zu entscheiden, als es von einem Agenten vorgeführt zu bekommen, der beide Seiten gleichzeitig ändert.

> **The story continues …**
>
> Eine Meta-Ebene, die alle laufenden Agenten überwacht, ist die logische nächste Schicht und existiert bislang nur in Ansätzen. Solange sie fehlt, ist die Zahl der Agenten, die eine Organisation verantworten kann, durch die Zahl der Menschen begrenzt, die hinschauen.

---

Die ganze Folge: [Wie KI unser Arbeitsleben verändert!](https://think-ai.podigee.io/27-wie-ki-unser-arbeitsleben-verandert)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
