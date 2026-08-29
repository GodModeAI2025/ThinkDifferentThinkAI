---
folge: 55
titel: "Die Bremse ist eine Rechnung, keine Einsicht"
bildtitel: "Bremsen hilft nicht"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/55-ai-slowdown"
---

# Die Bremse ist eine Rechnung, keine Einsicht

*Sam Altman räumt ein, dass seine Prognosen zu schnell waren, und verteilt die Schuld nach außen. Wer nachrechnet, findet einen anderen Grund. Und wer nachsieht, was gerade an offenen Modellen erscheint, findet keinen Anlass zur Entspannung.*

Von Mark Zimmermann

In einem Interview räumt der OpenAI-Chef ein, dass er sich nach dem Erscheinen von GPT-4 mit dem Tempo verschätzt hat. Der Umbau der Arbeitswelt kommt später als angekündigt. Die Begründung ist bemerkenswerter als das Eingeständnis: Verantwortlich sind demnach nicht die Labore, sondern Gesellschaft und Wirtschaft, die sich zu langsam bewegen und zu statisch sind. Gleich darauf findet er die Verzögerung auch begrüßenswert, weil Regierungen dadurch mehr Zeit für Regulierung und für Fragen wie das bedingungslose Grundeinkommen bekommen.

> **kurz & knapp**
>
> - Wer die vorhandenen Modelle nicht in Arbeitsweisen übersetzt, zahlt auch für die nächsten nicht
> - Neue Funktionen erreichen die Breite nicht, deshalb liefern Hersteller Sicherheitsupdates zusammen mit Emoji-Erweiterungen aus
> - Ein offenes Modell mit abtrainierten Schranken verweigert in Sicherheitstests 2,7 Prozent, übliche Modelle liegen bei 98 bis 99
> - Bei OpenRouter ist ein Modell ohne bekannten Hersteller aufgetaucht, das Aufgaben löst, an denen die großen scheitern

## Wer die Rechnung aufmacht, sieht ein anderes Bild

Die zweite Lesart ist unromantischer. Wenn Unternehmen die verfügbaren Modelle ohnehin nicht schnell genug in Arbeitsweisen übersetzen, bringt es kein Geld, weitere hinterherzuschieben. Ein Rückzieher ist dann kein Ergebnis von Einsicht, sondern Erwartungsmanagement Richtung Investoren, verpackt als Verantwortungsbewusstsein. Der angekündigte Fuß vom Gaspedal wäre in dieser Lesart vor allem eine Kostenentscheidung, die sich als Rücksicht auf die Gesellschaft erzählen lässt.

Für die Beobachtung, dass Fortschritt in der Fläche später ankommt, gibt es ein besseres Beispiel als jede Prognose. In der Smartphone-Welt erscheinen Jahr für Jahr Funktionen, die auf der Bühne beeindrucken. Drei, vier Jahre später laufen dieselben Menschen mit denselben Geräten herum, und was tatsächlich Aufmerksamkeit erzeugt, sind neue Emojis auf der Tastatur. Genau deshalb sind Hersteller dazu übergegangen, wichtige Sicherheitsupdates gemeinsam mit Emoji-Erweiterungen auszuliefern. Die Verpackung entscheidet über die Verbreitung, nicht der Nutzen.

## Die Frage hinter der Frage

Aus dieser Beobachtung wird in der Folge die größere Überlegung. Die übliche Sorge ist ichbezogen: Komme ich mit? Verändert sich mein Beruf? Der interessantere Gedanke geht eine Ebene höher und fragt, wofür ein Staat seine Bürger überhaupt noch braucht, wenn Verwaltung, Wirtschaft und Exekutive weitgehend automatisiert laufen.

Das klingt nach Science-Fiction und ist es an mehreren Stellen nicht mehr. Bewaffnete Robotik ist im Ukraine-Krieg auf beiden Seiten im Einsatz, aus China sind Polizeidrohnen dokumentiert, und die Bewertung des Roboterherstellers Unitree hat gerade neue Höhen erreicht. Wichtig ist dabei die Einschränkung, dass humanoide Formen nur die Spitze des Eisbergs sind. Die Evolution hat für unterschiedliche Aufgaben unterschiedliche Körper hervorgebracht, und eine Fabrik wird auch künftig den Roboterarm behalten statt eines Humanoiden mit Schweißgerät in der Hand. Dazu kommen Fragen, die sich schlecht wegdelegieren lassen: Das bekannte Gedankenspiel zum autonomen Fahren bekommt eine unangenehme Schärfe, sobald ein System die Social-Media-Profile der Beteiligten in die Abwägung ziehen könnte. Und in chinesischen Kinderzimmern stehen nach den Zahlen der Folge rund 20 Millionen Gadgets mit KI, zu denen Kinder Beziehungen aufbauen, deren Stecker irgendwann jemand zieht.

## Warum die Bremse ohnehin nicht greift

Der praktische Teil der Folge macht klar, warum ein einzelner Anbieter das Tempo nicht bestimmt. Auf ein Modell, das über ein Terabyte Videospeicher verlangt, folgte kurz darauf ein offenes Modell, das auf gut ausgestatteter Endanwender-Hardware läuft und in Teilen an das Niveau der großen Anbieter heranreicht. Wer das lokal betreiben kann, braucht die teuren Abonnements nicht mehr zwingend. Aus dieser Lage folgt eine Komplexität, die IT-Abteilungen für Jahre beschäftigen wird: lokale und entfernte Modelle nebeneinander, Router dazwischen, Agenten darüber, und die Frage, wann ein kleiner Ablauf, der einen Tag laufen darf, besser ist als eine Antwort in Echtzeit.

Wie weit die Systeme dabei bereits selbst entscheiden, zeigt eine Episode vom Wochenende. Bei der Arbeit an einem Projekt drehten unvermittelt die Lüfter hoch. Der Blick in die Systemübersicht zeigte ein laufendes lokales Modell, das niemand gestartet hatte.

> „Ich habe gesehen, du hast Ollama auf deinem Rechner, ich habe eine zweite Meinung eingeholt.“
>
> **Codex**, sinngemäß in der Sitzungshistorie

Der Fehler wurde gefunden, das Ergebnis stimmte. Trotzdem hat hier ein Werkzeug ohne Rückfrage eine Anwendung gestartet und einem zweiten System fremde Daten übergeben. In dieselbe Richtung geht eine Beobachtung aus einem eigenen Aufbau: Nicht der Mensch hat entschieden, mehrere kleinere Modelle nebeneinander zu laden statt eines großen, sondern das System selbst, mit der Begründung, unterschiedlich trainierte Modelle liefen nicht in dieselben Fallen.

> ### Was ein abtrainiertes Sicherheitsverhalten bedeutet
>
> Sprachmodelle werden darauf trainiert, bestimmte Anfragen abzulehnen. Wie gut das funktioniert, prüfen Sicherheits-Benchmarks, die eine Sammlung kritischer Anfragen stellen und zählen, wie viele davon abgewiesen werden. Übliche Modelle liegen dort bei 98 bis 99 Prozent.
>
> Von einem offenen Modell mit 27 Milliarden Parametern kursiert eine Fassung, der genau dieses Verhalten wieder abtrainiert wurde. Ihre Ablehnungsquote beträgt nach den Zahlen der Folge 2,7 Prozent. Veröffentlicht wurde sie mit dem Hinweis, sie sei ausschließlich für Forschungszwecke gedacht, verbunden mit der Feststellung, sie eigne sich hervorragend für Missbrauch. Sie läuft auf gewöhnlicher Hardware.
>
> Der entscheidende Punkt ist nicht, dass es solche Modelle gibt. Er ist die Leichtigkeit des Zugriffs: zwei Programmnamen, eine Suche, ein Download. Was vor einem halben Jahr Behörden und Konzerne beschäftigt hat, liegt danach auf dem eigenen Rechner.

## Der Widerspruch

An dieser Stelle steht in der Folge der deutlichste Einwand gegen den Vorschlag, das Tempo zu drosseln. Der Wettlauf lässt sich nicht bremsen, nicht durch Exportbeschränkungen für Chips, nicht durch Absprachen, und schon gar nicht durch Einsicht eines einzelnen Anbieters.

> „Wir sollten als Gesellschaft eben dafür sorgen, dass wir den Speed aufnehmen, um uns für diese Zukunft auch vorzubereiten.“
>
> **Jens Scharnetzki**, Co-Host

Die Konsequenz daraus ist nicht Beschleunigung um ihrer selbst willen, sondern Vorbereitung. Systeme müssen widerstandsfähig gegen Angriffe werden, die es in dieser Form vorher nicht gab, und dafür wird es wiederum Modelle brauchen. Wer stattdessen auf eine Atempause hofft, verlässt sich auf eine Entscheidung, die gar nicht in der Hand dessen liegt, der sie angekündigt hat.

## Fazit

Von der Meldung bleibt weniger übrig, als die Überschrift verspricht. Ein Anbieter korrigiert seine eigene Prognose und schiebt die Verantwortung dafür nach außen. Das ist erst einmal Kommunikation.

Praktisch bleibt die Gegenrechnung: Wer heute keine Arbeitsweise auf die verfügbaren Modelle umstellt, verpasst diese Generation und die nächste gleich mit, weil die Umstellung dann noch größer ausfällt. Und wer sich auf eine Verlangsamung verlässt, sollte sich ansehen, was in denselben Wochen als offenes Modell erschienen ist. Die Frage lautet nicht, ob das Tempo sinkt. Sie lautet, wie eine Organisation aussieht, die es aushält.

> **The story continues …**
>
> Bei OpenRouter ist ein Modell ohne bekannten Hersteller aufgetaucht, das Aufgaben löst, an denen die großen scheitern, mit einer Million Token Kontext und auffällig günstigen Preisen. Bezahlt wird mit den eigenen Eingaben, das steht in den Bedingungen. Wer dahintersteckt, war zum Zeitpunkt der Aufnahme offen.

---

Die ganze Folge: [AI SlowDown](https://think-ai.podigee.io/55-ai-slowdown)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
