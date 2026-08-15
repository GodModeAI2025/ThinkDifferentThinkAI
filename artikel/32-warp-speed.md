---
folge: 32
titel: "Vom Bastelprojekt zur Konzernstrategie: Was NVIDIAs NanoClaw wirklich bedeutet"
bildtitel: "Jede Firma braucht eine Agenten-Strategie"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/32-warp-speed"
---

# Vom Bastelprojekt zur Konzernstrategie: Was NVIDIAs NanoClaw wirklich bedeutet

*Ein Hobbyprojekt namens OpenClaw steht wenige Monate später als NanoClaw auf einer NVIDIA-Bühne, verbunden mit der Ansage, jede Firma brauche künftig eine Agenten-Strategie. Was daran Substanz hat und was Verkauf ist.*

Von Mark Zimmermann

Diese Folge bricht mit dem üblichen Format. Statt eines Themas stehen die Nachrichten der letzten Tage im Mittelpunkt, und zwar die, bei denen beide Hosts nach eigener Aussage sprachlos waren.

Der Bogen reicht von DNA-Sequenzierung per Chatbot bis zu einem Forschungs-Loop, in dem ein System selbständig Hypothesen aufstellt, verwirft und neu entwickelt, ohne dass jemand die Prompts nachschärft.

> **kurz & knapp**
>
> - OpenClaw, das Projekt eines einzelnen Entwicklers, steht als NanoClaw auf der NVIDIA-Bühne
> - Der Anspruch lautet Agentic OS, mit Umschaltung zwischen lokalem Modell und Cloud
> - Die Ansage: Jede Firma braucht künftig eine Agenten-Strategie, nicht nur eine KI-Strategie
> - Für die Lizenzrechnung ist das relevant, Stichwort Preissprung von E5 auf E7
> - Ein Student hat in zehn Tagen ein System für Millionen simulierter Agenten gebaut und dafür 4,5 Millionen Dollar erhalten

## Was tatsächlich passiert ist

OpenClaw begann als Vibe-Coding-Projekt eines Entwicklers und ging seit Dezember durch die Decke. Jensen Huang hat es als NanoClaw auf die Bühne geholt, inklusive Umschaltung zwischen lokalem und Cloud-Modell und dem Anspruch, ein Agentic OS zu sein.

Der Satz, der hängen bleibt: Jede Firma müsse künftig eine Agenten-Strategie haben, nicht bloß eine KI-Strategie.

Bei solchen Aussagen lohnt der Blick auf den Absender. NVIDIA verkauft Rechenleistung, und jede Agenten-Strategie erzeugt Rechenlast. Das entwertet die Aussage nicht, ordnet sie aber ein.

Substanz hat sie trotzdem, und zwar aus einem Grund, der wenig mit Hardware zu tun hat: Eine KI-Strategie beantwortet, welche Modelle eingesetzt werden. Eine Agenten-Strategie muss beantworten, wer welche Automatisierung bauen darf, wo sie liegt, wie sie geprüft wird und was passiert, wenn sie etwas Falsches tut. Das sind Governance-Fragen, und die kommen unabhängig davon, ob NVIDIA sie stellt.

## Die Rechnung, die dahinter steht

Der praktisch greifbarste Teil betrifft Lizenzkosten. Der Preissprung von E5 auf E7 bei Microsoft ist für viele Organisationen eine erhebliche Summe, und Copilot-Lizenzen sind der Anlass.

Damit wird die Frage interessant, ob eine eigene Agenten-Umgebung günstiger ist. Die naheliegende Rechnung stellt Lizenzkosten gegen Tokenkosten und übersieht dabei den größeren Posten. Eine Lizenz enthält Betrieb, Aktualisierung, Support und Haftung. Eine eigene Umgebung enthält davon nichts.

Beachten Sie deshalb bei jedem Vergleich die dritte Zahl. Was kostet die Person, die das Ganze pflegt, und was passiert, wenn sie das Unternehmen verlässt.

> ### Was in eine Agenten-Strategie gehört
>
> **Wer darf bauen.** Wenn Fachbereiche Skills schreiben, braucht es eine Festlegung, wer sie in Umlauf bringen darf und wer prüft. Sonst entsteht dieselbe Schatten-IT wie bei Excel-Makros, nur mit Systemzugriff.
>
> **Wo liegt es.** Ein Skill, der auf einem Notebook liegt, ist kein Betriebsmittel. Ablage, Versionierung und Auffindbarkeit sind Voraussetzung dafür, dass Arbeit nicht doppelt gemacht wird.
>
> **Welche Daten dürfen hinein.** Die Frage stellt sich pro Automatisierung, nicht pro Modell. Ein Skill, der Kundendaten anfasst, unterliegt anderen Regeln als einer, der Protokolle zusammenfasst.
>
> **Wer schaut hin.** Für jede Automatisierung eine benannte Person, die das Ergebnis verantwortet. Ohne diese Zuordnung ist niemand zuständig, wenn etwas auffällt.
>
> **Wie kommt man wieder raus.** Was passiert, wenn der Anbieter den Dienst einstellt, den Preis verdreifacht oder eine Funktion entfernt. Das ist die Frage, die am seltensten gestellt und am teuersten übersehen wird.

## Die Vision und ihre Grenze

Weitergesponnen wird das Bild zu Multi-Agenten-Systemen, in denen ein Orchestrator Unteragenten für Programmierung, Präsentation und Kommunikation koordiniert. Technisch ist das machbar und wird an mehreren Stellen bereits gebaut.

Die Grenze liegt nicht in der Technik, sondern im Überblick. Sobald ein Orchestrator selbständig Unteragenten startet, weiß niemand mehr sicher, wie viele gerade laufen und was sie anfassen. Das ist derselbe Punkt, an dem in anderen Folgen die Fehlerquote ansteigt.

## Was daneben noch passiert ist

Die Folge sammelt weitere Beobachtungen, die den Takt der Entwicklung illustrieren. Humanoide Roboter laufen in China testweise über echte Straßen, während der Tesla Bot in München noch Popcorn verteilt. Perplexity Computer, Kimi und Googles Gemini-CLI mit MCP-Server- und Skill-Unterstützung erhöhen den Wettbewerbsdruck. NotebookLM hat eine Cinema-Video-Funktion bekommen.

Das schrägste Beispiel: Ein chinesischer Student hat in zehn Tagen mit seinem Projekt Mirofisch ein System gebaut, das Millionen simulierter Agenten auf reale Weltereignisse reagieren lässt, unter anderem um auf Polymarket gezielter zu wetten. Dafür gab es 4,5 Millionen Dollar Investment.

Interessant daran ist weniger die Wettanwendung als die Zahl davor. Zehn Tage von der Idee zu einem System, das Investoren überzeugt, beschreibt einen Kostenverfall bei der Umsetzung, den keine Beschaffungsabteilung eingepreist hat.

## Fazit

Statt der gewohnten Distanz überwiegt in dieser Folge etwas Selteneres: Staunen. Beide Hosts geben offen zu, dass sie bei der Frage ins Grübeln kommen, was eine Ein-Personen-Firma mit Agent Harness, Skills und automatisierter Recherche heute leisten kann.

Daraus entsteht die Idee einer neuen Kategorie: die KI-Consultancy, hinter der am Ende ein Mac Mini mit gut gepflegten Skills steht.

Für alle, die keine Beratung gründen wollen, bleibt die praktische Konsequenz dieselbe. Prüfen Sie, welche Leistungen Sie einkaufen, weil sie früher Aufwand bedeutet haben. Bei einem Teil davon ist der Aufwand gerade verschwunden, und das merkt man erst, wenn jemand anderes es merkt.

Und schreiben Sie die fünf Punkte einer Agenten-Strategie auf, bevor der erste Fachbereich seinen ersten Skill in Betrieb nimmt. Danach ist es Aufräumen statt Ordnen.

> **The story continues …**
>
> Wenn eine einzelne Person mit einem gut gepflegten Harness die Leistung eines kleinen Teams erbringt, verändert das die Preisbildung für Beratungsleistungen. Wie schnell das durchschlägt, hängt weniger von der Technik ab als davon, wie lange Einkaufsabteilungen nach Tagessätzen fragen statt nach Ergebnissen.

---

Die ganze Folge: [Warp Speed](https://think-ai.podigee.io/32-warp-speed)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
