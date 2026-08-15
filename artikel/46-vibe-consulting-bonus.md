---
folge: 46
titel: "Vibe Coding trifft Spezifikation: Wo die Abkürzung in der Softwareentwicklung endet"
bildtitel: "Der Prompt ist die Spezifikation"
kicker: "Live vom adesso Digital Day"
podigee: "https://think-ai.podigee.io/46-vibe-consulting-bonus"
---

# Vibe Coding trifft Spezifikation: Wo die Abkürzung in der Softwareentwicklung endet

*Anwendungen entstehen scheinbar per Zuruf. Prof. Dr. Volker Gruhn und Stephan Kempf ordnen ein, warum das für Spielzeug-Apps reicht und für ein ERP-System nicht, und wo die eigentliche Arbeit hingewandert ist.*

Von Mark Zimmermann

Aufgenommen wurde diese Doppelfolge live vom adesso Digital Day 2026, mit zwei Gästen, die aus unterschiedlichen Richtungen auf dieselbe Frage schauen. Prof. Dr. Volker Gruhn ist Aufsichtsratsvorsitzender der adesso SE und lehrt Software Engineering an der Universität Duisburg-Essen. Stephan Kempf arbeitet bei adesso mobile solutions zu Mobile, On-Device AI und Agent Harnessing und ist Co-Autor von „Corporate LLM“.

Die Frage lautet: Was passiert mit Softwareentwicklung, Beratung und Make-or-Buy-Entscheidungen, wenn Anwendungen per Prompt entstehen.

> **kurz & knapp**
>
> - Vibe Coding trägt für Spielzeuganwendungen und trägt nicht für produktionsreife Systeme
> - Der Engpass ist nicht der Code, sondern die Spezifikation
> - Natürliche Sprache wird zur Spezifikationssprache, mit allen Mehrdeutigkeiten
> - Architektur und Requirements Engineering gewinnen an Gewicht, statt zu verschwinden
> - Das eingesetzte Modell ist weitgehend austauschbar, der Harness ist es nicht

## Die Dotcom-Parallele

Gruhn ordnet die aktuelle Stimmung historisch ein, und der Vergleich sitzt.

> „Als das Internet aufkam: Egal ob du Bäcker oder Metzger bist, heute bist du ein perfekter Webseitenschreiber.“
>
> **Prof. Dr. Volker Gruhn**, Aufsichtsratsvorsitzender der adesso SE

Damals hat eine Weiterbildung in HTML gereicht, um sich als Webentwickler zu bezeichnen. Ein Teil der so entstandenen Seiten hat funktioniert, ein größerer Teil ist nach zwei Jahren nicht mehr wartbar gewesen. Der Unterschied zwischen beidem war selten am Ergebnis erkennbar, sondern erst an der ersten größeren Änderung.

Genau das wiederholt sich. Vibe Coding erzeugt lauffähige Anwendungen, und für einen abgegrenzten Zweck ist das eine echte Beschleunigung. Der Bruch kommt später: bei der zweiten Anforderung, beim Datenschutzkonzept, bei der Frage, was passiert, wenn zwei Nutzer gleichzeitig schreiben.

## Wo der Engpass wirklich liegt

Der zentrale Satz der Folge betrifft die Bedingung, unter der die Abkürzung funktioniert: Ein Prompt trägt nur dann, wenn er am Ende eine vollständige Spezifikation des Softwaresystems ist.

Damit ist die Arbeit nicht verschwunden, sondern verschoben. Wer nicht formulieren kann, was er braucht, welche Fälle auftreten und woran man die Erfüllung erkennt, bekommt auch von einem Modell keine tragfähige Lösung. Natürliche Sprache wird an dieser Stelle zur Spezifikationssprache, und sie bringt ihre bekannte Schwäche mit: Sie ist mehrdeutig, und Mehrdeutigkeit wird von einem Modell nicht als Rückfrage sichtbar, sondern als Entscheidung.

> ### Warum Spezifikation die härtere Disziplin ist
>
> Eine Spezifikation beschreibt nicht, wie ein System gebaut wird, sondern was es leisten muss und unter welchen Bedingungen. Dazu gehören funktionale Anforderungen, nichtfunktionale Anforderungen wie Antwortzeiten oder Verfügbarkeit, Randfälle und explizite Nichtziele.
>
> Der Aufwand steckt in den Randfällen. Was geschieht bei einem Abbruch mitten in der Buchung, wie verhält sich das System bei widersprüchlichen Stammdaten, welche Berechtigungen gelten für Vertretungen. Ein erfahrener Entwickler stellt diese Fragen im Gespräch, weil er die Fehlerbilder kennt. Ein Modell stellt sie nur, wenn es dazu aufgefordert wird, und beantwortet sie andernfalls selbst.
>
> Requirements Engineering galt lange als Verwaltungsdisziplin und gewinnt gerade an Bedeutung, weil es zur eigentlichen Eingabe geworden ist.

Softwarearchitektur verliert damit ebenfalls nicht an Gewicht. Sie entscheidet, ob sich ein System in Teilen ersetzen lässt, ob Verantwortlichkeiten getrennt sind und ob eine Änderung an einer Stelle nicht an drei anderen Stellen Folgen hat. Ein Modell optimiert auf die gestellte Aufgabe, nicht auf die übernächste.

## Make-or-Buy verschiebt sich

Für Beratungsentscheidungen ändert sich die Rechnung. Wenn die Erstellung günstiger wird, verschiebt sich die Grenze zwischen Standardprodukt und Eigenentwicklung.

Das Argument fällt allerdings in beide Richtungen. Selbst zu bauen wird attraktiver, weil der Erstaufwand sinkt. Gleichzeitig steigt die Bedeutung der Betriebsphase, und die wird nicht billiger. Wer eine Eigenentwicklung nur über die Erstellungskosten rechtfertigt, rechnet den teureren Teil nicht mit.

Praktisch bewährt sich eine einfache Trennung: Was das Geschäft unterscheidbar macht, gehört ins eigene Haus, weil dort die Spezifikation liegt. Was alle gleich machen, kauft man, weil dort niemand einen Vorteil aus einer eigenen Lösung zieht.

## Das Modell ist austauschbar, der Harness nicht

Der Begriff Agent Harness ist im Publikum kaum bekannt, und die Runde hält im Gespräch ausdrücklich an, um ihn zu erklären. Das ist bezeichnend für den Stand der Diskussion: Über Modelle wird viel geredet, über die Umgebung, in der sie arbeiten, wenig.

Kempfs Fazit ist die praktisch wertvollste Aussage der Folge. Das eingesetzte KI-Modell ist am Ende fast austauschbar, entscheidend ist, wie robust der Harness drumherum gebaut ist.

Das deckt sich mit dem, was Betreiber berichten. Ein Modellwechsel kostet eine Regressionsrunde, wenn Skills, Kontextverwaltung und Prüfmechanik sauber getrennt sind. Er kostet ein Projekt, wenn Ablauf und Anbietereigenheiten verwoben sind.

Für die Bewertung eines Angebots ergibt sich daraus eine brauchbare Prüffrage: Wie viel des Aufwands steckt in Dingen, die einen Modellwechsel überleben. Liegt der Schwerpunkt auf durchdachten Skills, Testfällen und Kontextführung, ist die Investition langlebig. Liegt er auf feingeschliffenen Prompts für ein bestimmtes Modell, ist sie es nicht.

## Fazit

Vibe Coding ist ein echter Fortschritt und eine gefährliche Erzählung zugleich. Der Fortschritt liegt darin, dass Ideen schneller lauffähig werden. Die Gefahr liegt in dem Schluss, damit sei Softwareentwicklung erledigt.

Was tatsächlich passiert ist: Der Codieraufwand ist gesunken, der Spezifikationsaufwand nicht. Wer bisher gut darin war zu beschreiben, was gebraucht wird, gewinnt deutlich. Wer das nie gelernt hat, produziert jetzt schneller Systeme, die niemand warten kann.

Der Rat der beiden Gäste ist entsprechend unspektakulär und richtig: Nehmen Sie Skills ernst und bauen Sie sich einen stabilen Harness. Das Modell darunter wird ohnehin wechseln.

> **The story continues …**
>
> Offen bleibt die Frage, ob Agenten künftig selbst Requirements beschreiben sollten. Technisch geht das bereits, und ein Modell stellt beim Nachfragen durchaus die richtigen Fragen. Ungeklärt ist, wer die so entstandene Spezifikation verantwortet, wenn sie später Grundlage einer Abnahme ist.

---

Die ganze Folge: [Vibe Consulting & Bonus](https://think-ai.podigee.io/46-vibe-consulting-bonus)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
