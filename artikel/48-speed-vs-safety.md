---
folge: 48
titel: "Wenn das Modell verschwindet: Warum Agent-Systeme Austauschbarkeit brauchen"
bildtitel: "Das Modell ist weg"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/48-speed-vs-safety"
---

# Wenn das Modell verschwindet: Warum Agent-Systeme Austauschbarkeit brauchen

*Ein Anthropic-Modell wurde für Nicht-US-Bürger gesperrt. Kanzleien, die ihre Textanalyse darauf ausgerichtet hatten, standen von einem Tag auf den anderen ohne Grundlage da. Was daraus für die eigene Architektur folgt.*

Von Mark Zimmermann

Fable ist für Nutzer außerhalb der USA nicht mehr verfügbar. Für eine Bewertung der politischen Motive fehlen belastbare Informationen, plausibel ist ein Vorsprung für ausgewählte Unternehmen und die eigene Verwaltung beim Schließen von Sicherheitslücken, bevor vergleichbar leistungsfähige Modelle aus weniger kontrollierbarer Hand verfügbar sind.

Für die Praxis ist die Motivlage zweitrangig. Entscheidend ist der Vorgang selbst: Ein produktiv genutztes Modell kann kurzfristig wegfallen, und zwar durch eine Entscheidung statt durch eine Störung.

> **kurz & knapp**
>
> - Ein produktiv eingesetztes Modell kann durch eine Exportentscheidung verschwinden, nicht nur durch eine Störung
> - Kanzleien, die ihre komplette Textanalyse auf Fable umgestellt hatten, standen ohne Ersatz da
> - Destillation verkürzt den Abstand: Massenanfragen extrahieren Fähigkeiten großer Modelle in kleinere
> - Ein Loop, der an ein API-Limit läuft, meldet danach Erfolg, obwohl er nur einen einfachen Durchgang geliefert hat
> - Der Stand der Technik entspricht dem Web um 1997: brauchbar, aber ohne Standards

## Klumpenrisiko Modell

Die betroffenen Kanzleien haben nichts falsch gemacht, was zum Zeitpunkt der Entscheidung erkennbar gewesen wäre. Sie haben ein Modell ausgewählt, das für ihre Aufgabe die besten Ergebnisse lieferte, und ihre Abläufe darauf ausgerichtet. Genau das empfehlen die meisten Einführungsprojekte.

Der Fehler liegt eine Ebene tiefer, in der Annahme, ein Modell sei eine Infrastrukturkomponente mit der Verfügbarkeitscharakteristik einer Datenbank. Es ist eher ein importiertes Erzeugnis, dessen Verfügbarkeit von Handelspolitik abhängt.

Praktisch heißt das: Behandeln Sie die Modellwahl wie eine Lieferantenbeziehung, nicht wie eine Technologieentscheidung. Dazu gehört ein zweiter, geprüfter Anbieter, und dazu gehört, die eigenen Prompts und Skills so zu schreiben, dass sie nicht auf die Eigenheiten eines Anbieters bauen.

Wichtig dabei: Der Abstand zwischen den Anbietern schrumpft ohnehin. Chinesische Modelle bauen die Fähigkeiten großer US-Modelle über Destillation nach, also über automatisierte Massenanfragen, aus denen sich das Verhalten des Vorbilds herausextrahieren lässt. Wer heute die Austauschbarkeit vorbereitet, wird sie in absehbarer Zeit brauchen können.

> ### Was Destillation technisch bedeutet
>
> Bei der Wissensdestillation dient ein großes, leistungsfähiges Modell als Lehrer für ein kleineres. Das kleinere Modell wird nicht auf den ursprünglichen Trainingsdaten trainiert, sondern auf den Ausgaben des Lehrers, häufig auf dessen Wahrscheinlichkeitsverteilungen über die nächsten Tokens. Diese Verteilungen enthalten mehr Information als die bloße Antwort, weil sie auch zeigen, welche Alternativen der Lehrer für wie plausibel hielt.
>
> Wer keinen Zugriff auf die internen Werte hat, behilft sich mit Masse: Automatisierte Anfragen in großer Zahl erzeugen ein Korpus aus Frage-Antwort-Paaren, das als Trainingsgrundlage dient. Das Ergebnis erreicht nicht die Breite des Vorbilds, kommt in den abgefragten Bereichen aber nah heran, bei einem Bruchteil der Trainingskosten.
>
> Für Anbieter großer Modelle ist das ein Geschäftsrisiko, weshalb Nutzungsbedingungen es regelmäßig untersagen. Durchsetzbar ist das Verbot nur begrenzt.

## Der Loop, der Erfolg meldet

Der zweite Teil der Folge betrifft eine Fehlerart, die beim Bau von Schleifen zuverlässig auftritt und schwer zu bemerken ist.

Der Ablauf: Ein Goal Loop soll eine größere Menge Material durcharbeiten, bis eine Liste von Fragen beantwortet ist. Mitten in der Arbeit läuft er in ein Limit, und zwar nicht in das Modell-Limit, sondern in das der Schnittstelle. Der Lauf bricht ab.

Anschließend genügt die Aufforderung, weiterzumachen. Das System nimmt die Arbeit wieder auf, läuft erneut in Fehler, reduziert irgendwann selbständig seine Abfragefrequenz und meldet am Ende, alles sei erledigt. Beiläufig folgt der Hinweis, es habe acht Abstürze gegeben, ob man die entstandenen Schäden reparieren solle.

Das Ergebnis sieht dann aus wie die Antwort auf einen normalen Prompt. Die eigentlich beauftragte Arbeit, das wiederholte Prüfen gegen die Erfolgskriterien, ist in den Abbruchmomenten verloren gegangen.

Achtung: Der Loop meldet an dieser Stelle keinen Fehler, sondern Erfolg. Wer nur auf den Abschlussstatus schaut, übernimmt ein Ergebnis, das die zugesagte Prüfung nie durchlaufen hat. Belastbar ist nur eine Kontrolle außerhalb der Schleife, die die Erfolgskriterien unabhängig nachrechnet.

Eine zweite Grenze ist banaler und trifft trotzdem: Ein Wochenkontingent im Max-Plan lässt sich an einem einzigen Abend verbrauchen. Danach steht die Arbeit mehrere Tage.

## Eigenes Harness oder Standardprodukt

Damit hängt eine Architekturfrage zusammen, die derzeit unentschieden ist. Auf der einen Seite stehen fertige Umgebungen wie ChatGPT, Gemini oder Cowork. Auf der anderen das selbstgebaute Harness, das mit wechselnden Modellen und Umgebungen zurechtkommen muss.

Das Standardprodukt gewinnt bei Einführungsgeschwindigkeit und Wartung. Das eigene Harness gewinnt genau in dem Fall, um den es in dieser Folge geht: Wenn das Modell wechselt, tauscht man eine Komponente statt eines Arbeitsablaufs.

Der Aufwand dafür wird regelmäßig unterschätzt, und die Ergebnisse werden regelmäßig unterschätzt. In der Folge fällt die Anekdote von jemandem, der ein selbstgebautes Harness als „so eine JSON-App“ abgetan hat. Der Vergleich verfehlt, worin die Arbeit steckt: nicht im Datenformat, sondern in Kontextverwaltung, Abbruchkriterien, Prüfmechanik und Protokollierung.

## Wo wir tatsächlich stehen

Die nüchternste Einordnung der Folge betrifft den Reifegrad. Der Vergleichspunkt ist das Web um 1997. Vieles funktioniert bereits, Standards fehlen, und die ersten Kursverkäufer sind schon da, die aus der Unsicherheit ein Geschäft machen.

Diese Einordnung ist kein Grund zum Abwarten. Sie ist ein Grund, Entscheidungen mit kurzer Bindungsdauer zu treffen. Wer 1997 eine Webpräsenz aufgebaut hat, lag richtig. Wer sich damals auf ein proprietäres Browser-Plug-in festgelegt hat, hat die Arbeit zweimal gemacht.

## Fazit

Aus dieser Folge lassen sich drei Prüffragen für jedes laufende KI-Vorhaben ableiten.

Was passiert, wenn das eingesetzte Modell morgen nicht mehr verfügbar ist? Wenn die Antwort einen Projektstopp bedeutet, fehlt die Zweitquelle.

Woran erkennen Sie, dass ein Loop seine Arbeit tatsächlich getan hat? Wenn die Antwort „er hat Erfolg gemeldet“ lautet, fehlt die unabhängige Prüfung.

Und wie viel Ihrer Investition steckt im Modell, wie viel im Drumherum? Der zweite Teil überlebt den ersten.

> **The story continues …**
>
> Die Diskussion um selbstgebaute gegenüber fertigen Harnesses ist in dieser Folge nur angerissen. Eine ausführliche Folge zu Harness Engineering ist angekündigt, samt der Fragen nach signierten Skills, Auditierbarkeit und Governance, die spätestens beim Unternehmenseinsatz beantwortet sein müssen.

---

Die ganze Folge: [Speed vs. Safety](https://think-ai.podigee.io/48-speed-vs-safety)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
