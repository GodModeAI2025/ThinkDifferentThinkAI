---
folge: 13
titel: "Der Browser als Akteur: Was Atlas kann und warum Vorsicht angebracht ist"
bildtitel: "Der Browser klickt selbst"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/13-new-episode"
---

# Der Browser als Akteur: Was Atlas kann und warum Vorsicht angebracht ist

*Atlas klickt, füllt Formulare aus und postet im Agent Mode selbständig. Das ist beeindruckend und öffnet einen Angriffsweg, gegen den es derzeit keine belastbare Abwehr gibt.*

Von Mark Zimmermann

Der Bogen dieser Folge reicht von einer AOL-Werbung mit Boris Becker bis zu Atlas, dem KI-Browser von OpenAI. Der Unterschied zu allem davor: Der Browser ist nicht mehr Werkzeug, sondern Akteur.

Ausprobiert wurde das unter anderem für einen automatisierten LinkedIn-Beitrag und beim Aufräumen des eigenen Postfachs.

> **kurz & knapp**
>
> - Atlas arbeitet im Agent Mode selbständig: klicken, Formulare ausfüllen, recherchieren, posten
> - Neu ist weniger die Fähigkeit als die Sichtbarkeit dessen, was auf der Seite passiert
> - Prompt Injection über unsichtbaren Text auf Webseiten ist der zentrale Angriffsweg
> - Postfachzugriff bedeutet in der Praxis Zugriff auf jedes Passwort-Zurücksetzen
> - Über die Hälfte aller Online-Inhalte ist inzwischen maschinell erzeugt

## Was daran tatsächlich neu ist

Zusammenfassungen und Seitenleisten-Interaktion bietet Microsoft mit Copilot in Edge längst, Perplexity und Manus experimentieren ebenfalls mit agentischem Browsen.

Der Unterschied bei Atlas liegt in der Sichtbarkeit. Man sieht direkter, was gerade auf der Seite geschieht, während im Agent Mode Aufgaben abgearbeitet werden: Preisrecherchen, Wettbewerbsvergleiche, automatisierte Bewertungen einer Website aus Sicht verschiedener Nutzergruppen.

Der letzte Anwendungsfall ist der praktisch nützlichste und wird selten genannt. Eine Website aus der Perspektive verschiedener Zielgruppen bewerten zu lassen, ersetzt keine Nutzerforschung und liefert einen brauchbaren ersten Durchgang für einen Bruchteil des Aufwands.

## Der Angriffsweg

Kritisch wird es bei der Sicherheit, und zwar grundsätzlich.

> ### Warum Prompt Injection im Browser besonders wiegt
>
> Ein Sprachmodell unterscheidet nur schwach zwischen Anweisung und Inhalt. Beides erreicht es als Text.
>
> Im Browser liest ein Agent Seiten, die andere geschrieben haben. Steht dort Text, den ein Mensch nicht sieht, etwa weiß auf weiß, in einem ausgeblendeten Element oder in einem Attribut, liest der Agent ihn trotzdem. Enthält dieser Text eine Anweisung, besteht die Möglichkeit, dass er ihr folgt.
>
> Der Angreifer braucht dafür keinen Zugang zu Ihrem Rechner. Es genügt, dass Sie seine Seite besuchen lassen.
>
> Wirksame Gegenmittel setzen außerhalb des Modells an: Der Agent darf nur auf ausgewählten Seiten handeln, jede nach außen wirkende Aktion braucht eine Freigabe, und der Agent arbeitet mit einem eigenen, eng berechtigten Zugang statt mit Ihrem.
>
> Eine Anweisung im System-Prompt, keine Anweisungen von Webseiten zu befolgen, hilft nur begrenzt. Sie steht im selben Kanal wie der Angriff.

Besonders heikel ist der Zugriff auf das eigene Postfach. Wer ihn erteilt, erteilt in der Praxis Zugriff auf jedes Passwort-Zurücksetzen und damit indirekt auf alle Dienste, die über dieses Postfach wiederhergestellt werden können.

Bei Online-Banking stellt sich dieselbe Frage noch schärfer. Die Einschätzung in der Folge ist eindeutig: ein spannendes Feld, das derzeit mit Vorsicht zu genießen ist.

## Der Habsburg-Effekt

Der zweite Aufreger ist eine Zahl: Über die Hälfte aller Online-Inhalte ist inzwischen maschinell erzeugt, Tendenz steigend.

Daraus folgt ein Problem, für das die Folge das Bild vom Habsburg-Effekt wählt. Wenn Sprachmodelle zunehmend mit maschinell erzeugten Daten trainiert werden, verengt sich der Genpool. Fehler und Eigenheiten verstärken sich über Generationen, statt durch neue Quellen ausgeglichen zu werden.

Für Betreiber von Websites folgt daraus eine ungewohnte Aufgabe: Inhalte müssen künftig nicht mehr allein für Menschen optimiert werden, sondern auch für Agenten, die sie lesen. Das betrifft Struktur, eindeutige Angaben und maschinenlesbare Daten, und es steht im Widerspruch zu vielem, was in den letzten Jahren als gutes Webdesign galt.

## Fazit

Agentisches Browsen ist die erste Anwendung, bei der ein Modell im offenen Netz handelt statt in einer kontrollierten Umgebung. Das erklärt sowohl den Nutzen als auch das Risiko.

Wer es einsetzen will, klärt vorher drei Dinge. Auf welchen Seiten darf der Agent handeln und nicht nur lesen? Mit welchem Zugang arbeitet er, und ist das ein eigener mit engen Rechten? Und welche Aktionen erfordern eine ausdrückliche Freigabe?

Für Postfach, Bank und alles, was Geld oder Zugänge betrifft, lautet die brauchbare Antwort derzeit: keine automatischen Aktionen. Lesen ja, handeln nein.

Das ist keine Ablehnung der Technik. Es ist die Anerkennung, dass ein Angriffsweg offen ist, für den es noch keine Lösung gibt.

> **The story continues …**
>
> Als Werkzeugtipp stellt die Folge WhisperFlow vor, ein Sprache-zu-Text-Werkzeug, das Diktat direkt in jedes Textfeld überträgt. Einer zitierten Beobachtung zufolge nutzen manche Entwicklerteams es nach wenigen Monaten für rund 75 Prozent ihrer Texteingaben. Der Wechsel des Eingabekanals verläuft leiser als der Wechsel des Modells und verändert die Arbeit mindestens ebenso.

---

Die ganze Folge: [THE BROWSER STRIKES BACK](https://think-ai.podigee.io/13-new-episode)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
