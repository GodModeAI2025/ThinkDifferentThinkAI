---
folge: 52
titel: "Sprachnotizen: Ohne Schnittstelle bleibt das Archiv ein Sumpf"
bildtitel: "Aufnehmen reicht nicht"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/52-exokortex"
---

# Sprachnotizen: Ohne Schnittstelle bleibt das Archiv ein Sumpf

*Ein Diktiergerät am Revers löst kein Wissensproblem. Erst der maschinelle Zugriff macht aus 28 aufgesprochenen Notizen eine abarbeitbare Liste. Ein Praxisbericht aus dem Urlaub, mit Rechnung.*

Von Mark Zimmermann

Der Plan war ein Urlaub ohne Technik. Kein Notebook, stattdessen ein E-Book-Reader, das Handy so selten wie möglich. Aufgenommen wurde diese Folge trotzdem, aus einem Tesla auf einem Ferienpark-Parkplatz in Dänemark. Verantwortlich dafür ist ein Herstellerupdate vom 23. Juli: Plaud hat einen MCP-Server veröffentlicht. Das klingt nach einer Randnotiz im Changelog, verschiebt aber die Grenze zwischen Aufnahmegerät und Arbeitsmittel.

> **kurz & knapp**
>
> - Ein Sprachrekorder ohne maschinellen Zugriff erzeugt ein Archiv, das niemand mehr anfasst
> - Der MCP-Server macht die Notizen aus Claude, ChatGPT oder Gemini heraus abfragbar
> - Apples Sprachmemos nehmen auf und transkribieren lokal, bieten aber weder Massenexport noch Schnittstelle
> - 28 Notizen aus 48 Stunden ließen sich mit einer einzigen Frage sortieren und teilweise gleich abarbeiten
> - Wer die Daten im Haus behalten will, holt die Audiodateien über die API, transkribiert lokal mit Whisper und stellt einen eigenen MCP-Server davor

## Das Pfandflaschen-Problem

Der erste Anlauf ist gescheitert, und zwar nicht an der Hardware. Ein Plaud Pin, angesteckt am Revers, hat zuverlässig aufgenommen, was ihm aufgetragen wurde. Das Problem entstand danach.

> „Ich spreche mir was auf. Ja, ich spreche mir noch was auf, das höre ich mir morgen schon wieder an. Oh, jetzt habe ich 40 Nachrichten aufgesprochen, um Gottes willen, die höre ich mir nie wieder an.“
>
> **Mark Zimmermann**, Co-Host

Das Bild dafür ist das Leergut unter dem Schreibtisch. Zwei Flaschen bringt man weg, vier auch noch, bei zwanzig kapituliert man. Aufnehmen kostet fünf Sekunden, Nacharbeiten kostet ein Vielfaches, und dieses Verhältnis kippt jedes Archiv, das auf manuelles Nachhören angewiesen ist. Der Pin wurde wieder verkauft.

Beachten Sie, dass dieser Effekt nichts mit der Aufnahmequalität zu tun hat. Er entsteht überall dort, wo eine Ablage schneller wächst, als sie erschlossen werden kann. Wer schon einmal einen Ordner „Später lesen“ angelegt hat, kennt die Mechanik.

## Was der MCP-Server ändert

Das aktuelle Gerät, die Plaud Note, hat Checkkartenformat, ein Mikrofon-Array, eigenen Speicher und klemmt per MagSafe hinten ans Handy. Die Aufnahme läuft lokal, rund 30 Stunden passen darauf. Technisch ist das eine Fortschreibung, kein Sprung.

Der Sprung liegt in der Schnittstelle. Seit dem 23. Juli stellt Plaud einen MCP-Server bereit. Damit liegen die Notizen nicht mehr allein in der Hersteller-App, sondern lassen sich aus Claude, ChatGPT, Gemini oder einem selbstgebauten Harness heraus abfragen.

Der Praxisfall aus dem Urlaub: 28 Notizen in 48 Stunden, aufgesprochen beim Radfahren, nachts im Bett, zwischen zwei Ausflügen. Teils Mails, teils Erinnerungen, teils Projektgedanken. Eine einzige Frage an das Modell, was in den letzten 48 Stunden an Aufgaben angefallen ist, liefert die sortierte Liste zurück, samt Angebot, die Dinge gleich zu erledigen. Eine der Mails war anschließend fertig formuliert.

Wichtig dabei: Die Leistung steckt nicht im Modell und nicht im Mikrofon. Sie steckt darin, dass ein Agent den Bestand überhaupt lesen kann. Genau daran hat der Vorgänger gescheitert.

> ### Was ein MCP-Server tut
>
> Das Model Context Protocol ist ein offener Standard, über den ein Sprachmodell auf externe Datenquellen und Werkzeuge zugreift. Ein MCP-Server veröffentlicht dabei eine überschaubare Liste von Funktionen, etwa „Notizen der letzten 48 Stunden abrufen“ oder „Volltext durchsuchen“. Das Modell entscheidet selbst, welche davon es aufruft, und bekommt strukturierte Daten statt einer Webseite zurück.
>
> Der Unterschied zu einer klassischen API liegt weniger in der Technik als im Adressaten. Eine API richtet sich an Entwickler, die Aufrufe fest verdrahten. Ein MCP-Server richtet sich an ein Modell, das zur Laufzeit entscheidet, was es braucht. Für den Anwender heißt das: Er formuliert eine Frage in normaler Sprache, statt eine Abfrage zu bauen.

## Warum Apples Sprachmemos an dieser Stelle aufhören

Der naheliegende Einwand lautet, dass ein iPhone all das mitbringt. Aufnehmen lässt sich über den Action-Button, auch an der Apple Watch Ultra, und transkribiert wird lokal auf dem Gerät.

Der Einwand trägt bis zur Ablage und nicht weiter. Die Dateien liegen in der Sprachmemo-App, und dort bleiben sie. Es gibt derzeit keinen MCP-Zugriff, keinen Massenexport und keinen Dateizugriff von außen. Damit fehlt genau der Teil, der aus dem Archiv Material macht. Apple liefert die beiden Schritte, die ohnehin niemandem schwerfallen, und lässt den dritten weg.

Erwarten Sie hier keine schnelle Lösung. Der fehlende Export ist kein Versäumnis, sondern folgt der Systemarchitektur, in der Nutzerdaten die App nicht verlassen sollen. Für den Datenschutz ist das ein Vorteil, für den beschriebenen Anwendungsfall ein Ausschlusskriterium.

Wer die Daten trotzdem im eigenen Haus behalten will, geht den umgekehrten Weg: Audiodateien über die Plaud-API vom Gerät holen, lokal mit Whisper transkribieren, einen eigenen MCP-Server davorstellen. Der Aufwand ist erheblich, das Ergebnis liegt danach auf der eigenen Platte.

## Zwei Arten, mit Sprache zu arbeiten

In der Folge treten zwei Nutzungsmuster gegeneinander an, und der Unterschied ist praktisch relevant.

Jens Scharnetzki nutzt Sprache als Dialogkanal. Er redet mit dem Modell, weil er schneller spricht als tippt, und erwartet sofort Antwort. Im Auto, beim Kochen, überall dort, wo die Hände belegt sind. Der Reiz liegt im Hin und Her, inzwischen auch in Verbindung mit Computer Use: Das Modell liest die Optionen aus einem Reiseportal vor, man bestätigt, es klickt und bucht.

Das zweite Muster ist das asynchrone Auskippen. Kein Feedback, keine Antwort, nur ablegen. Der Grund dafür ist banal und trotzdem entscheidend: Acht Themen wären acht Chats, und acht parallele Chats sind auf einem Handy nicht zu verwalten. Wer stattdessen unsortiert aufspricht und die Zuordnung später einer Maschine überlässt, muss sich unterwegs nicht merken, in welchem Kontextfenster welcher Gedanke liegt.

Für diese Auslagerung fällt in der Folge der Begriff Exocortex. Er trifft die Sache genauer als „Second Brain“, weil er beschreibt, was tatsächlich passiert: Denkarbeit wandert aus dem Kopf heraus auf ein Gerät. Der Unterschied zum Second Brain liegt in der Aufbereitung. Gespeichert und auffindbar ist die Vorstufe. Nutzbar wird es erst, wenn eine Maschine damit arbeiten kann.

## Was der Aufbau kostet

An dieser Stelle wird die Folge konkret, und zwar in Euro. Ein Second Brain ist kein Produkt, das man kauft.

> „Da ist ja kein Voodoo drin. Wenn einer euch Second Brain für viel Geld verkauft: wegrennen, noch schneller rennen. Macht einen Ordner, macht drei Markdowns rein, und ihr habt schon das erste Second Brain.“
>
> **Mark Zimmermann**, Co-Host

Teuer wird nicht das System, sondern das Anreichern der Altbestände. Jens Scharnetzki hat sein X-Archiv mit rund 20.000 Likes über den DSGVO-Datenabzug geholt. Der Abzug selbst kostet nichts, taugt allein aber wenig: Die interessanten Links stehen im ersten Kommentar und nicht im Post, weil der Algorithmus Beiträge mit externem Link abstraft. Also hat er die API hinterhergeschickt und die Kommentare bis zur zweiten Ebene nachgeladen. Ein Tag Rechenzeit, 41 Euro einmalig. Laufend liegen die Kosten im Cent-Bereich, weil nur noch die neuen Likes dazukommen.

Er hält die Investition für lohnend, weil ein Like verrät, was ihn wann interessiert hat. Aus dem Verlauf lässt sich ableiten, welche Themen bei ihm Gewicht haben und welche er hat liegen lassen. Das ist eine andere Qualität von Kontext als eine Liste von Projekten.

Der Nutzen zeigt sich beim Wechsel des Anbieters. Springen Sie von ChatGPT zu Gemini oder Claude, weiß das neue Modell nicht, wer Sie sind, woran Sie arbeiten und was Ihnen wichtig ist. Ein Second Brain trägt das mit.

## Das offen getragene Mikrofon

Ein Punkt bleibt in der Folge ausdrücklich ungelöst, und die beiden geben das auch so zu Protokoll. Rechtsberatung ist es keine.

Die Beobachtung dahinter ist trotzdem bemerkenswert. Ein sichtbar am Revers getragenes Mikrofon löst Rückfragen aus. Dasselbe Gerät in der Hosentasche, ein Handy, ein Paar Ohrhörer auf dem Tisch, löst keine aus, obwohl es technisch dasselbe kann.

> „Die Leute sollen wissen, was du bei dir trägst, die Leute sollen wissen, was du kannst, was du machst. Natürlich braucht es immer das Einverständnis, und ein Nein ist auch zu akzeptieren.“
>
> **Mark Zimmermann**, Co-Host

Die Plaud Note hat kein prominentes Aufnahmelicht. Wer damit Gespräche mitschneiden will, braucht die Zustimmung der Beteiligten, und die Erfahrung aus früheren Geräten zeigt, wie leicht das schiefgeht: Ein 3D-gedrucktes Mikrofon an einer Halskette vergisst man auszuschalten, und dann steht im Archiv der halbe Eisladen.

Die Hoffnung der beiden liegt auf technischen Lösungen statt auf Verzicht. Denkbar wäre ein Signal, das dem Gerät des Gegenübers mitteilt, dass keine Einwilligung vorliegt, etwa über für Menschen unhörbare Töne. Sicher ist nur die Richtung: Mit kleiner werdenden lokalen Modellen werden mehr solcher Geräte um uns herum laufen, nicht weniger.

## Fazit

Die Folge handelt nur an der Oberfläche von einem Aufnahmegerät. Darunter geht es um eine Frage, die jedes Wissenssystem entscheidet: Kommt eine Maschine an den Bestand heran.

Wer heute anfangen will, braucht dafür kein Produkt und kein Budget. Ein Ordner, ein paar Markdown-Dateien, untereinander verlinkt, das reicht für den Anfang. Die eigentliche Arbeit liegt danach, beim Anreichern der Altbestände, und die lässt sich beziffern: ein Tag Rechenzeit und 41 Euro für 20.000 Likes.

Und wer ein Gerät kauft, sollte vor der Aufnahmequalität die Schnittstelle prüfen. Ein Rekorder ohne Export ist ein Archiv, das wächst und niemandem gehört, der es lesen kann.

> **The story continues …**
>
> Am Ende der Folge fällt ein Punkt, der noch kaum diskutiert wird: Prompt Injection funktioniert auch über Sprachnachrichten. Wer fremde Audiodateien in ein System kippt, das ein Agent auswerten darf, öffnet denselben Angriffsweg wie bei manipulierten Texten. Vertrauen Sie eingehenden Audios so weit, wie Sie einem unbekannten PDF vertrauen würden.

---

Die ganze Folge: [EXOKORTEX](https://think-ai.podigee.io/52-exokortex)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
