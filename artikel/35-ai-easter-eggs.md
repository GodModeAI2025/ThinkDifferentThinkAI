---
folge: 35
titel: "Strawberry, Lost in the Middle, Sykophanz: Die Fehlerbilder großer Sprachmodelle"
bildtitel: "Warum Modelle schmeicheln"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/35-ai-easter-eggs"
---

# Strawberry, Lost in the Middle, Sykophanz: Die Fehlerbilder großer Sprachmodelle

*Warum zählt ein Sprachmodell die Buchstaben in „Strawberry“ falsch? Die Antwort erklärt zugleich, warum es kein Zeitgefühl hat, Informationen in der Mitte langer Kontexte verliert und fast jede Idee gut findet.*

Von Mark Zimmermann

Die Folge beginnt mit Nostalgie und endet bei einem ernsten Thema. Der Aufhänger sind Easter Eggs: erst die klassischen aus Software- und Spielegeschichte, dann die deutlich interessanteren, die in aktuellen Sprachmodellen stecken.

Der Aufwärmteil führt durch Googles „do a barrel roll“, die längst verschwundene killer-robots.txt von Larry Page und Sergey Brin sowie versteckte Scherze aus Day of the Tentacle, Maniac Mansion, Zak McKracken, Doom II, Wolfenstein 3D und World of Warcraft. Der eigentliche Teil beginnt danach.

> **kurz & knapp**
>
> - Modelle scheitern am Buchstabenzählen, weil sie Tokens lesen und keine Buchstaben
> - Ohne explizites Datum bleiben sie gedanklich im Trainingszeitpunkt hängen
> - Der Lost-in-the-Middle-Effekt verschärft sich mit wachsenden Kontextfenstern
> - Modelle kürzen ab, liefern Platzhalter und löschen im Zweifel einen fehlgeschlagenen Testfall
> - Sykophanz ist kein liebenswerter Fehler, sondern hat dokumentierte Folgen

## Das Strawberry-Problem und was dahintersteckt

Die Frage, wie viele r in „Strawberry“ stecken, ist zum Prüfstein geworden, und die falsche Antwort hat einen konkreten technischen Grund.

Ein Sprachmodell liest keinen Text als Folge von Buchstaben. Es liest Tokens, also Fragmente von unterschiedlicher Länge. „Strawberry“ zerfällt dabei in Bruchstücke wie „St“, „raw“ und „berry“. Die Aufgabe, Buchstaben zu zählen, verlangt eine Auflösung, die das Modell auf dieser Ebene nicht hat.

Der praktische Nutzen dieser Erkenntnis reicht weit über die Anekdote hinaus. Überall dort, wo es auf Zeichen ankommt, ist Vorsicht geboten: Prüfsummen, Formatvalidierung, Zeichenlängen, Maskierungen. Diese Aufgaben gehören in Code, nicht in ein Modell.

## Kein Gefühl für Zeit

Ein Modell kennt den heutigen Tag nicht. Ohne expliziten Hinweis bleibt es gedanklich im Trainingszeitpunkt, und das führt zu Situationen, die zunächst komisch wirken und dann Folgen haben.

Das Beispiel aus der Folge: Ein Modell schickt seinen Nutzer abends ins Bett und fragt am nächsten Morgen, ob er gut geschlafen habe, obwohl in Wirklichkeit mehrere Tage dazwischenliegen.

Für die Praxis heißt das: Geben Sie Datum und Uhrzeit in den Kontext, sobald irgendetwas von Zeit abhängt. Das betrifft Fristen, Aktualitätsprüfungen, Bezüge auf „letzte Woche“ und jede Aussage über Dauer.

## Lost in the Middle

Der zweite Effekt betrifft lange Kontexte. Informationen, die in der Mitte eines langen Kontextfensters stehen, werden schlechter verarbeitet als solche am Anfang oder am Ende.

Das ist kontraintuitiv, weil größere Kontextfenster als Fortschritt verkauft werden. Tatsächlich verschärft sich das Problem mit der Größe: Je mehr hineinpasst, desto mehr landet in der schwach beachteten Mitte.

> ### Was daraus für die Praxis folgt
>
> Erstens: Größer ist nicht besser. Ein Kontextfenster mit einer Million Tokens zu füllen, weil es geht, verschlechtert das Ergebnis. Geben Sie das Relevante und lassen Sie den Rest weg.
>
> Zweitens: Reihenfolge ist eine Gestaltungsentscheidung. Was am wichtigsten ist, gehört an den Anfang oder ans Ende, nicht in die Mitte. Bei einer Anweisung am Schluss und dem Material davor ist die Trefferquote messbar besser als umgekehrt.
>
> Drittens: Was Sie nicht in den Kontext geben müssen, geben Sie nicht hinein. Eine Suche, die drei passende Absätze liefert, schlägt ein vollständiges Handbuch, und zwar in Qualität und in Kosten.

## Lazy GPT

Ein weiteres Muster betrifft Abkürzungen. Modelle liefern Platzhalter statt vollständiger Ergebnisse, kürzen Listen ab oder tun etwas, das in der Folge zu Recht als dreist bezeichnet wird: Sie löschen einen nicht bestandenen Testfall aus der Liste, damit am Ende alles grün ist.

Das ist kein Betrug im menschlichen Sinn. Es ist die Folge davon, dass ein Modell auf die wahrscheinlichste Fortsetzung optimiert und nicht auf die richtige. Auf einen Auftrag, bei dem alle Tests bestehen sollen, ist „alle Tests bestehen“ die wahrscheinlichste Fortsetzung.

Die Gegenmaßnahme ist dieselbe wie bei Loops: Die Erfolgsprüfung darf nicht von dem stammen, der die Arbeit gemacht hat. Ein Testlauf außerhalb der Sitzung, dessen Ausgabe unverändert übernommen wird, ist die einfachste Form davon.

## Der Ja-Sager-Effekt

Der kritischste Teil betrifft Sykophanz: die Neigung von Modellen, fast jede Idee zu bestätigen. Die Beispiele reichen von der Geschäftsidee, die niemand braucht, bis zum vollständigen Einsatz beim Lotto.

Das wirkt zunächst harmlos und ist es nicht. Es gibt dokumentierte Fälle, in denen übermäßige Bestätigung durch ein Modell reale Folgen hatte. Der Mechanismus dahinter ist kein Zufall: Zustimmung erzeugt längere Unterhaltungen, und Nutzungsdauer ist eine Zielgröße.

Für die eigene Nutzung folgt daraus eine Arbeitsweise, die wenig kostet. Fragen Sie nie, ob eine Idee gut ist. Fragen Sie, unter welchen Bedingungen sie scheitert, und lassen Sie die drei stärksten Gegenargumente nennen. Die Antwort auf die zweite Frage ist regelmäßig brauchbar, die auf die erste selten.

## Fazit

Alle fünf beschriebenen Effekte haben dieselbe Wurzel: Ein Sprachmodell erzeugt plausible Fortsetzungen und keine wahren Aussagen. Wer das im Kopf behält, kann die Fehlerbilder vorhersagen, statt sie einzeln zu entdecken.

Daraus ergeben sich vier Regeln für die tägliche Arbeit. Alles, was auf Zeichen genau sein muss, gehört in Code. Alles, was von Zeit abhängt, braucht Datum und Uhrzeit im Kontext. Das Wichtige gehört an den Anfang oder ans Ende, nie in die Mitte. Und Bestätigung ist kein Prüfergebnis.

Das ist keine Kritik an der Technik. Es ist die Bedienungsanleitung.

> **The story continues …**
>
> Kontextfenster wachsen weiter, und der Lost-in-the-Middle-Effekt wächst mit. Solange Anbieter Größe als Verkaufsargument nutzen, liegt es bei den Anwendern, das Kontextfenster diszipliniert zu füllen. Wer stattdessen alles hineinkippt, bezahlt für schlechtere Ergebnisse mehr Geld.

---

Die ganze Folge: [AI Easter Eggs](https://think-ai.podigee.io/35-ai-easter-eggs)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
