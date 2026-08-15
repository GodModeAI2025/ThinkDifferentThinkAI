---
folge: 8
titel: "Drei Personas schlagen zwanzig: Was ein KI-Beirat tatsächlich leistet"
bildtitel: "Drei schlagen zwanzig"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/8-ai-advisory-board"
---

# Drei Personas schlagen zwanzig: Was ein KI-Beirat tatsächlich leistet

*Zwanzig Personas, acht bis dreizehn Seiten Beschreibung je Rolle, ein Moderator-Agent, der delegiert und gewichtet. Das Ergebnis war eindeutig: Drei gut gewählte Perspektiven liefern bessere Antworten als ein volles Gremium.*

Von Mark Zimmermann

Der Aufbau ist in einem Urlaub entstanden und ist bemerkenswert gründlich: ein vollständiger KI-Beirat, gebaut mit n8n, dem Automatisierungswerkzeug aus Deutschland, das laut Handelsblatt inzwischen mit 2,4 Milliarden Euro bewertet wird.

Statt eines einzelnen Chatbots stehen dahinter zwanzig System-Prompts, die Agenten in Persönlichkeiten wie Steve Jobs, Angela Merkel, Elon Musk, Jeff Bezos, Tim Cook und Jonathan Ive verwandeln. Acht bis dreizehn DIN-A4-Seiten je Persona, kein „verhalte dich wie“.

> **kurz & knapp**
>
> - Acht bis dreizehn Seiten je Persona statt einer Anweisungszeile
> - Ohne ausführliche Beschreibung fallen die Antworten spürbar oberflächlicher aus
> - Ein Moderator-Agent delegiert, lässt Relevanz von 0 bis 1 selbst einschätzen und gewichtet
> - Zwanzig Personas brauchen 20 bis 30 Minuten je Durchlauf und liefern schlechtere Ergebnisse
> - Drei gut gewählte, verschiedene Perspektiven schlagen das volle Gremium

## Warum der Aufwand etwas bringt

Der direkte Vergleich ist der interessante Teil. Derselbe Auftrag ohne die ausführlichen Persona-Beschreibungen liefert deutlich oberflächlichere Antworten.

Die Vermutung dahinter, in der Folge ausdrücklich als Vermutung markiert: Ein Sprachmodell braucht ein möglichst konkretes Weltmodell, um in einer Rolle konsistent zu bleiben. Fehlt es, fällt es in sein neutrales Standardverhalten zurück.

Das deckt sich mit dem, was in anderen Zusammenhängen als Context Engineering beschrieben wird. Eine Rolle ist keine Anweisung, sondern ein Bezugsrahmen: Welche Erfahrungen prägen das Urteil, welche Prioritäten gelten, was wird abgelehnt und warum. Ohne diesen Rahmen bleibt eine Rollenanweisung ein Stilhinweis.

> ### Wie das Gremium aufgebaut ist
>
> Ein **Moderator-Agent** im Stil eines Senior Consultants nimmt die Frage entgegen und delegiert sie an die passenden Personas.
>
> Jede Persona gibt eine **Selbsteinschätzung von 0 bis 1** dazu ab, wie relevant sie sich für diese Frage hält. Das ist der klügste Teil der Konstruktion: Statt alle gleich zu gewichten, entsteht ein Maß dafür, wer überhaupt etwas beizutragen hat.
>
> Der Moderator **gewichtet** die Antworten anschließend entlang dieser Einschätzung.
>
> Über eine **Perplexity-Anbindung** holen sich die Agenten aktuelle Informationen aus dem Netz, damit eine Persona nicht ausschließlich mit Trainingsdaten von vorgestern argumentiert.
>
> Die Selbsteinschätzung hat allerdings dieselbe Schwäche wie jede Selbstbewertung: Ein Modell, das nach seiner Relevanz gefragt wird, neigt zur Zustimmung. Wer den Aufbau nachbaut, sollte die Werte beobachten. Liegen alle über 0,8, misst die Skala nichts.

## Der Befund zur Gremiumsgröße

Die praktisch wertvollste Erkenntnis der Folge ist eine Reduktion. Zwanzig Personas gleichzeitig sind zu viel, sowohl was Rechenzeit angeht, also 20 bis 30 Minuten je Durchlauf, als auch was Fehleranfälligkeit betrifft.

Drei gut gewählte, verschiedene Perspektiven liefern bessere Ergebnisse als ein überfülltes Gremium.

Das entspricht der Erfahrung mit menschlichen Gremien und hat hier eine zusätzliche technische Ursache. Je mehr Beiträge zusammengeführt werden, desto stärker mittelt die Zusammenfassung. Zwanzig Stimmen ergeben einen Durchschnitt, drei ergeben einen Widerspruch, und der Widerspruch ist der Wert.

Entscheidend ist deshalb nicht die Zahl, sondern die Verschiedenheit. Drei Personas, die alle aus derselben Denkschule kommen, liefern dieselbe Antwort dreimal.

## Der Selbstversuch

Bemerkenswert ehrlich ist der Teil, in dem das Gremium auf einen der Hosts selbst angesetzt wird, gefüttert mit Arbeitszeugnissen und Feedbackgesprächen, um eine Einschätzung für eine Vorstandspräsentation zu bekommen.

Das ist die naheliegendste und zugleich heikelste Anwendung. Wer eigene Beurteilungen einspeist, bekommt eine Auswertung, die den blinden Fleck der ursprünglichen Beurteiler übernimmt. Ein Arbeitszeugnis beschreibt, wie jemand gesehen wurde, nicht wie jemand ist.

Für den beabsichtigten Zweck reicht das trotzdem, weil eine Vorstandspräsentation ebenfalls davon lebt, wie jemand gesehen wird.

## Die Frage nach dem Bias

Die Folge streift ein Thema, das über den Aufbau hinausgeht: Wie stark prägen Trainingsdaten und Anbietervorgaben das Weltbild eines Modells. Erwähnt werden der Bias-Verdacht bei US- gegenüber asiatischen Modellen und die bekannte Geschichte, dass Grok angewiesen worden sein soll, Elon Musk nicht zu kritisieren.

Für einen Beirat aus Personas ist das unmittelbar relevant. Wenn alle Personas auf demselben Modell laufen, teilen sie dessen Grundhaltung. Die Verschiedenheit ist dann eine Verschiedenheit der Sprechweise, nicht des Urteils. Wer echte Vielfalt will, verteilt die Personas auf verschiedene Anbieter.

## Fazit

Ein Beirat aus Personas ist eine der wenigen Konstruktionen, bei denen sich der Aufwand belegen lässt: Der Vergleich mit und ohne ausführliche Beschreibung fällt eindeutig aus.

Für den Nachbau gelten drei Regeln. Schreiben Sie die Personas ausführlich, mit Erfahrungshintergrund und Prioritäten, nicht als Stilhinweis. Nehmen Sie drei statt zwanzig, und wählen Sie sie nach Verschiedenheit aus. Und verteilen Sie sie über verschiedene Modelle, wenn Ihnen an echtem Widerspruch gelegen ist.

Das Fazit der Folge klingt zunächst nicht nach einer KI-Folge und trifft: Wer gut mit Menschen umgehen kann, kommt auch mit den unterschiedlichen Persönlichkeiten von Agenten besser zurecht. Soft Skills, lange als weiches Gegenstück zur IT-Kompetenz belächelt, werden im Umgang mit Multi-Agenten-Systemen zur Kernkompetenz.

> **The story continues …**
>
> Erwähnt wird das Papier „Psychologically Enhanced AI Agents“ und damit die Frage, ob Vielfalt in einem KI-Team messbar bessere Ergebnisse liefert. Das ist die Untersuchung, die diesem Aufbau die empirische Grundlage geben würde, die er bislang nicht hat.

---

Die ganze Folge: [AI ADVISORY BOARD](https://think-ai.podigee.io/8-ai-advisory-board)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
