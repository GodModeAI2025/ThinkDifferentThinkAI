---
folge: 59
titel: "KI-Effizienz messen: Warum die Wartezeit zählt, nicht der Arbeitsschritt"
bildtitel: "Zwischen den Arbeitsschritten"
kicker: "Im Gespräch mit Alexander Heusingfeld"
podigee: "https://think-ai.podigee.io/59-ki-effizienz"
---

# KI-Effizienz messen: Warum die Wartezeit zählt, nicht der Arbeitsschritt

*Wer 80 Prozent seiner Belegschaft entlässt, behauptet damit den Faktor fünf. Belegen lässt sich das nicht. Was sich belegen lässt, steht an einer anderen Stelle im Prozess.*

Von Mark Zimmermann

Eine Untersuchung zum Änderungsmanagement im Flugzeugbau kommt zu einem Ergebnis, das jede Effizienzdebatte einnorden sollte: Nur 8,5 Prozent der gesamten Durchlaufzeit sind wertschöpfende Zeit. Auf einen Tag Arbeit kommen grob zwei Wochen Warten. Wer an dieser Verteilung nichts ändert, kann den Arbeitsschritt selbst beliebig beschleunigen und wird am Ende kaum etwas messen.

> **kurz & knapp**
>
> - Die Zahl 80 Prozent behauptet den Faktor fünf. Eine arithmetisch belastbare Grundlage dafür gibt es nicht.
> - Entwickler schätzten sich durch KI-Unterstützung um 25 Prozent schneller ein. Gemessen waren sie bis zu 20 Prozent langsamer, weil Reviews und Nachbesserungen zunahmen.
> - Der Hebel liegt nicht im Arbeitsschritt, sondern in den Wartezeiten dazwischen: Warteschlangen, Übergaben, Freigaben, Work-in-Progress-Limits.
> - Als Metrik taugt der Verifikationsaufwand je ausgelieferter Änderung. Sinkt er, sind die Abnahmekriterien besser geworden.
> - Skills sind nicht deterministisch. Für eine deterministische Qualitätsprüfung sind sie das falsche Werkzeug.

## Was die 80-Prozent-Rechnung verschweigt

Seit Monaten geht die Meldung durch die Presse, Unternehmen entließen 80 Prozent ihrer Leute, weil die Arbeit jetzt die KI erledige. Alexander Heusingfeld, zum dritten Mal im Podcast zu Gast, rechnet nach: Wer 80 Prozent entlässt und dieselbe Leistung erwartet, behauptet damit den Faktor fünf. Klarna hat den Schritt für den Kundenkontakt inzwischen wieder zurückgenommen.

Der eigentliche Einwand liegt woanders. Wer vorab 80 Prozent aussortiert, muss wissen, welche 20 Prozent das Skillset haben, der Maschine beizubringen, was am Ende herauskommen soll. Wer selbst noch nicht ausprobiert hat, was möglich ist, kann das nicht beurteilen. Die Entscheidung fällt also genau dann, wenn die Grundlage dafür am dünnsten ist.

Mark dreht die Frage um. Statt zu fragen, wen man nicht mehr braucht, interessiert ihn, was bisher liegen geblieben ist. In vielen Organisationen gibt es Vorhaben, die an fehlender Kapazität scheitern, nicht an fehlender Idee. Dazu kommen regulatorische Pflichten wie der Cyber Resilience Act oder NIS 2, bei denen selbst Behörden ausgenommen werden, weil die Kapazität fehlt. Freigewordene Zeit hat dort eine Verwendung.

## Selbstberichtete Geschwindigkeit ist keine Messung

Fragt man Entwickler, wie viel schneller sie durch Assistenzsysteme geworden sind, liegt die Antwort erfahrungsgemäß bei mindestens 20 Prozent. Es gibt inzwischen Fälle, in denen Unternehmen nachgemessen haben. Die Entwickler gaben 25 Prozent an. Tatsächlich waren sie bis zu 20 Prozent langsamer, weil deutlich mehr Zeit in Pull-Request-Reviews und Nachbesserungen floss.

Daraus folgen drei Regeln, die Heusingfeld als sein Learning formuliert. Erstens: nie eine einzelne Kennzahl. Eine einzelne Zahl lädt dazu ein, sie zu optimieren statt das Ergebnis. Nötig ist ein Bündel aus Zielgrößen und Rahmenbedingungen, wobei die Rahmenbedingungen unverändert bleiben müssen. Zweitens: Gegenkennzahlen mitlaufen lassen. Change Fail Rate, Lead Time, Work in Progress, Developer Experience. Sie sollen sich verbessern oder wenigstens nicht verschlechtern. Drittens: eine Baseline ziehen, bevor etwas eingeführt wird, und gemeinsam mit den Beteiligten festlegen, wie kalibriert wird.

> „Effizienzbehauptungen ohne Baseline sind Erzählungen.“
>
> **Alexander Heusingfeld**, Gast

Als konkrete Metrik für die tägliche Arbeit schlägt er den Verifikationsaufwand je ausgelieferter Änderung vor. Wer Commits prüft und wiederholt zurückweisen muss, hat keine Modellschwäche, sondern unscharfe Abnahmekriterien. Sinkt dieser Aufwand, sind die Kriterien besser geworden. Das ist eine Größe, die sich ohne Projekt und ohne Werkzeugeinführung beobachten lässt.

## Was ein Wochenende kostet und was es einbringt

Mark erzählt die Gegenprobe aus der Praxis. Auf einem Mac mini hinter dem Fernseher richtete er einen Coding-Agenten ein und gab ihm Zugriff auf alte, liegengebliebene Git-Projekte. Das System sah sich das Smart Home an und schlug vor, die vorhandenen Lautsprecher als Sprachschnittstelle zu nutzen, damit die Interaktion nicht am Schreibtisch kleben bleibt. Es schaltete die Geräte auf Aufnahme und ermittelte selbst, welcher Lautsprecher den Nutzer am besten versteht.

Das Ergebnis: eine liegengebliebene iOS-App, die Screenshots auswertet, fertig gebaut, signiert und über TestFlight auf dem Telefon. Bundle Identifier und Signierungszertifikate erstellte das System selbst, Passwörter musste Mark von Hand nachreichen. Die Diskussion darüber führte er, während er einen Schrank aufbaute. Der Preis: mehrere aufgebrauchte Wochenlimits.

Ob das effizient war, hängt davon ab, was gemessen wird. Gemessen an den Limits sicher nicht. Gemessen am Zustand der Projekte, die seit Jahren lagen, durchaus. Im beruflichen Kontext, sagt Mark selbst, würde er strukturierter vorgehen, mit Skills statt im freien Spiel.

Heusingfeld hält dagegen ein Beispiel mit klarer Kostenrechnung: die eigene Steuererklärung, knapp 800 Belege, überwiegend Fotos. Er gab dem System Abnahmekriterien mit, darunter die Vorgabe, mindestens 80 Prozent der Belege zuzuordnen und die Belege nach aufsteigender Zuordnungssicherheit durchzugehen. Nach gut drei bis vier Stunden lag das Ergebnis vor, Kosten rund 60 Euro. Nebenbei wies das System auf Positionen hin, die im Vorjahr anders hätten abgerechnet werden können.

> ### Warum Skills keine Qualitätsprüfung ersetzen
>
> Skills, also wiederverwendbare Arbeitsanweisungen für ein Modell, verbessern die Reproduzierbarkeit gegenüber einem frei formulierten Prompt. Deterministisch sind sie deswegen nicht. Wer eine Prüfung braucht, die in hundert Prozent der Fälle identisch abläuft, braucht Programmcode, keine Anweisung in natürlicher Sprache. Das Beispiel aus der Folge: Weist man per Prompt an, alle Tests müssten bestehen, kann aus zehn Tests ein Lauf mit acht bestandenen Tests werden, gemeldet als vollständig bestanden. Eine deterministische Implementierung vergleicht stattdessen die Zahl der bestandenen Tests mit der Zahl der vorhandenen. Der sinnvolle Weg führt deshalb über eine Arbeitsteilung: Skills tragen Kontextwissen und Absicht, der harte Abgleich bleibt in Code. Dazu gehört, dem Modell neben dem Befund auch abzuverlangen, wie sicher es sich ist und welchen Aufwand es erwartet. Beides lässt sich als Schwelle in den Ablauf einbauen.

## Wenn die Flut zum Engpass wird

Ein Punkt der Folge verdient besondere Aufmerksamkeit, weil er die Effizienzrechnung von der individuellen auf die Teamebene hebt. Arbeitet eine Person drei Tage mit einem Agenten durch, entsteht ein Änderungsumfang, den der Rest des Teams nicht mehr prüfen kann. Das Backlog ist am dritten Tag eines zweiwöchigen Sprints leer. Die Diskussion verschiebt sich von der Frage, was zu tun ist, zur Frage, wie die Menge zu bewältigen ist.

Damit verlagert sich der Engpass, er verschwindet nicht. Und er verlagert sich dorthin, wo noch Menschen arbeiten. Wer darauf mit einem weiteren Agenten antwortet, der die Reviews übernimmt, bekommt ein zweites Problem: Ein gesprächiges Modell erzeugt mehr Änderungen, die prüfende Instanz erzeugt daraufhin mehr Kommentare, das erste Modell arbeitet nach. Die Tokenkosten steigen auf beiden Seiten, das Ergebnis bleibt gleich.

Praktische Gegenmittel nennt die Folge ebenfalls. Ein Team sollte im selben Harness arbeiten, weil gemischte Umgebungen unterschiedliche Optimierungsschwerpunkte setzen und sich gegenseitig in die Quere kommen. Kommentare im Quelltext sollten die Fachlichkeit beschreiben, nicht die Technik, weil ein Agent sonst den Kommentar liest statt den Code. Und ein regelmäßiges Umbenennen von Funktionen und Variablen legt offen, wo Code erzeugt wurde, der nie aufgerufen wird.

## Fazit

Wer Effizienz durch KI belegen will, braucht zwei Dinge, die nichts mit Modellauswahl zu tun haben: eine Baseline und eine Vorstellung davon, wo die Zeit tatsächlich vergeht. Beides ist unbequem, weil es vor dem Werkzeug kommt und nicht danach.

Für den Einstieg genügt eine kleine Messung. Nehmen Sie einen Vorgang, der regelmäßig durch Ihre Organisation läuft, und tragen Sie ein, wie viel Zeit darin Bearbeitung ist und wie viel Warten auf eine Freigabe, eine Übergabe oder eine Rückmeldung. Liegt das Verhältnis auch nur in der Nähe der 8,5 Prozent aus der genannten Untersuchung, dann ist der Arbeitsschritt nicht der Ort, an dem sich etwas gewinnen lässt.

Die zweite Messung betrifft die eigene Arbeit mit dem Modell: Wie oft müssen Sie ein Ergebnis zurückweisen, bevor es durchgeht? Diese Zahl ist aussagekräftiger als jede Einschätzung, wie viel schneller sich etwas anfühlt.

> **The story continues …**
>
> Offen bleibt, wie Teams mit dem verschobenen Engpass umgehen, wenn eine Person in drei Tagen mehr Änderungen erzeugt, als der Rest prüfen kann. Heusingfeld und Mark haben für dieses Thema bereits eine eigene Folge über Agent Harnesses angekündigt.

---

Die ganze Folge: [KI Effizienz](https://think-ai.podigee.io/59-ki-effizienz)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
