---
folge: 10
titel: "Der Master-Prompt: Wenn eine Notiz zum Ticket mit Kapazitätsbuchung wird"
bildtitel: "Ein Klick, ein Ticket"
kicker: "Im Gespräch mit Dirk Beckmann"
podigee: "https://think-ai.podigee.io/10-new-episode"
---

# Der Master-Prompt: Wenn eine Notiz zum Ticket mit Kapazitätsbuchung wird

*Ein Klick nach dem Meeting, und es entstehen fertige Tickets samt Kapazitätsbuchung für die richtigen Personen im richtigen Projekt. Wie eine Agentur aus einem Notizwerkzeug ein Betriebssystem gemacht hat.*

Von Mark Zimmermann

Dirk Beckmann ist Geschäftsführer der Bremer Digitalagentur Art und Weise und Host des Podcasts „Die digitale Zeit“. Das Thema: wie Notion mit seiner KI-Version und das Automatisierungswerkzeug n8n aus einer Notizanwendung eine agentische Arbeitsumgebung machen.

> **kurz & knapp**
>
> - In Notion ist jede Zeile technisch eine eigene Seite, jede Datenbank eine Sammlung von Seiten
> - Aus der Finanzplanung wurde über Jahre ein komplettes Kapazitäts- und Ticketsystem
> - Ein Master-Prompt kennt den Firmenkontext und beantwortet, wer wann woran arbeitet
> - Killer-Feature ist die automatische Meeting-Aufzeichnung mit Ticket-Erstellung
> - n8n übernimmt, was Notion nicht kann, angebunden per Webhook

## Warum die Datenstruktur zählt

Die Grundidee hinter Notion erklärt Beckmann über die Bauweise: Statt klassischer Datenbanken arbeitet das Werkzeug mit Bausteinen. Jede Zeile ist technisch eine eigene Seite, jede Datenbank eine Sammlung von Seiten.

Das klingt nach einer Feinheit und ist der Grund, warum KI-Funktionen sich bis in einzelne Felder und Eigenschaften hineinziehen lassen, ohne Programmierkenntnisse. Wenn jedes Element ein vollwertiges Objekt ist, kann ein Modell an jedem davon ansetzen.

In einer klassischen Tabelle ist eine Zelle ein Wert. Hier ist sie ein Ort, an dem etwas passieren kann.

## Vom Kassensturz zum Betriebssystem

Der Werdegang in der Agentur ist typisch für gewachsene Systeme und deshalb lehrreich. Angefangen hat es mit Finanz- und Liquiditätsplanung. Daraus wurde über Jahre ein komplettes Kapazitäts- und Ticketsystem.

Das Herzstück ist ein selbst gebauter Master-Prompt, der den vollständigen Firmenkontext kennt und auf Nachfrage beantwortet, wer wann woran arbeitet und wo es klemmt.

> ### Was ein Master-Prompt tatsächlich ist
>
> Der Begriff führt in die Irre, weil er nach einer besonders langen Formulierung klingt. Tatsächlich ist es eine strukturierte Beschreibung des Unternehmens: welche Projekte laufen, welche Personen mit welchen Fähigkeiten und welcher Verfügbarkeit es gibt, wie Kapazität gerechnet wird, welche Begriffe intern was bedeuten.
>
> Der Wert liegt darin, dass diese Beschreibung an einer Stelle liegt und gepflegt wird. Jede Anfrage bekommt damit denselben Kontext, und die Antworten werden vergleichbar.
>
> Der Aufwand liegt entsprechend nicht im Formulieren, sondern in der Pflege. Ein Master-Prompt, der drei Monate alt ist, beantwortet Fragen über eine Firma, die es so nicht mehr gibt. Wer ihn einführt, muss festlegen, wer ihn aktualisiert und woran.
>
> Genau deshalb ist er in Notion gut aufgehoben: Er steht neben den Daten, die er beschreibt, statt in einem Chat-Fenster.

Beckmann ist ehrlich genug, das Ergebnis nicht als perfekt zu verkaufen. Es ist ein Anfang, mit dem sich ernsthaft über Kapazitätsplanung reden lässt.

## Agenten mit engen Rechten

Bemerkenswert ist der Umgang mit Berechtigungen. Beckmann hat eigene Agenten mit fein abgestuften Rechten gebaut.

Ein Stimmungs-Agent durchsucht Mails, Meeting-Tickets und Slack-Kommentare nach guter oder schlechter Stimmung. Ein Digest-Agent verdichtet morgens Neuigkeiten aus allen angebundenen Werkzeugen zu kurzen Karten für das Team-Dashboard.

Beim Stimmungs-Agenten lohnt ein Hinweis, der in der Folge nicht fällt: Ein System, das Mitarbeiterkommunikation nach Stimmung durchsucht, berührt Mitbestimmung. In Deutschland ist das mit dem Betriebsrat zu klären, bevor es läuft, unabhängig davon, wie gut die Absicht ist.

Als Killer-Feature nennt Beckmann die automatische Meeting-Aufzeichnung: ein Klick nach dem Gespräch, und es entstehen fertige Tickets mit Kapazitätsbuchung für die richtigen Personen im richtigen Projekt.

Der Grund, warum das funktioniert, ist der Master-Prompt. Ohne Kenntnis von Personen, Projekten und Kapazitäten wäre ein Protokoll das Ergebnis. Mit dieser Kenntnis wird daraus eine Buchung.

## n8n als Ergänzung

Der zweite Schwerpunkt ist n8n, das quelloffene Workflow-Werkzeug aus Berlin, das bei Beckmann frühere Make-Lizenzen abgelöst hat.

Per Webhook gehen Notion-Einträge an n8n-Abläufe, die daraus etwa über Gamma fertige Präsentationsfolien erzeugen und das Ergebnis nach Notion zurückschreiben.

Die Arbeitsteilung dahinter ist übertragbar: Das Wissenssystem hält Daten und Kontext, das Automatisierungswerkzeug übernimmt die Schritte, die außerhalb stattfinden. Wer beides in einem Werkzeug erzwingt, biegt eines davon zurecht.

Zum Aufnahmezeitpunkt neu war die Workflow-Builder-Beta, mit der sich komplette Abläufe per Anweisung statt per Ziehen und Ablegen bauen lassen. Beckmann hat damit bestehende Abläufe in Minuten nachgebaut oder verbessert.

## Fazit

Diese Folge ist der beste Beleg dafür, dass die interessanten Aufbauten nicht aus Konzernen kommen, sondern aus Häusern, die klein genug sind, um Dinge zu ändern.

Für die Übertragung auf die eigene Umgebung sind drei Punkte wichtig. Fangen Sie mit einem Bereich an, in dem Sie ohnehin Zahlen pflegen, und wachsen Sie von dort. Beckmanns System begann bei der Liquiditätsplanung.

Bauen Sie den Kontext einmal zentral und pflegen Sie ihn. Ohne diese Beschreibung liefert jede Anfrage ein anderes Bild.

Und trennen Sie Wissenssystem und Automatisierung. Beides in eines zu zwingen kostet mehr, als die zusätzliche Schnittstelle spart.

Für den Einstieg empfiehlt Beckmann einen kommerziellen Master-Prompt von Notion-Creator Simon für rund 79 Euro sowie die YouTube-Kanäle von Thomas Frank und Matthias Frank.

> **The story continues …**
>
> Workflows per Anweisung statt per Zusammenklicken zu bauen, verschiebt die Einstiegshürde deutlich nach unten. Damit wächst die Zahl der Automatisierungen in einem Unternehmen schneller als die Fähigkeit, sie zu überblicken. Die Frage, wer welchen Ablauf verantwortet, stellt sich dann als erstes.

---

Die ganze Folge: [Automation trifft Organisation: n8n × Notion](https://think-ai.podigee.io/10-new-episode)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
