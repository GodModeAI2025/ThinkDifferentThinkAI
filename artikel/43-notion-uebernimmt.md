---
folge: 43
titel: "Worker statt Klebeband: Wie Notion die Automatisierungsschicht einzieht"
bildtitel: "Worker statt Klebeband"
kicker: "Im Gespräch mit Dirk Beckmann"
podigee: "https://think-ai.podigee.io/43-notion-uebernimmt"
---

# Worker statt Klebeband: Wie Notion die Automatisierungsschicht einzieht

*Notion hat eine Developer-Plattform gestartet. Der interessante Teil sind nicht die Managed Agents, sondern kleine deterministische Programme, die ohne Tokenkosten laufen und die Zwischenschicht aus n8n und Make überflüssig machen.*

Von Mark Zimmermann

Notion hat den Start im Stil einer vorab aufgezeichneten Keynote inszeniert: ruhiger Vortrag, dunkler Raum, Holzstuhl. Was CEO Ivan Zhao darin ankündigt, geht deutlich über eine weitere Programmierschnittstelle hinaus.

Zu Gast ist Dirk Beckmann, Geschäftsführer der Digitalagentur artundweise, der die Plattform bereits produktiv einsetzt.

> **kurz & knapp**
>
> - Worker sind kleine TypeScript-Programme, die auf der Notion-Plattform laufen
> - Sie werden mit KI geschrieben, aber deterministisch ausgeführt: keine Tokenkosten, kein Halluzinationsrisiko
> - Ein Agent kann Worker als Werkzeug aufrufen, womit die Schicht aus n8n oder Make entfällt
> - Notion öffnet sich für lokale Modelle wie Mistral oder Qwen und für Hugging Face
> - Managed Agents von Anthropic arbeiten in abgeschotteten Sandboxes und auch außerhalb von Notion

## Was ein Worker ist, und warum das zählt

Ein Worker ist ein kleines TypeScript-Programm, das auf der Notion-Plattform läuft. Geschrieben wird es mit KI-Unterstützung, ausgeführt wird es deterministisch. Das ist die entscheidende Eigenschaft: Was einmal richtig läuft, läuft beim tausendsten Mal genauso, kostet keine Tokens und kann nichts erfinden.

Damit entsteht eine saubere Arbeitsteilung. Das Modell übernimmt, was Urteil braucht. Der Worker übernimmt, was zuverlässig sein muss. Ein Agent in Notion kann den Worker als Werkzeug aufrufen und bekommt ein berechenbares Ergebnis zurück.

Beckmann zeigt das an zwei eigenen Beispielen. Der erste Worker fragt über einen neuen Feldtyp namens Sync alle 15 Minuten ein Gmail-Postfach ab. Der zweite bindet Hugging Face an und erzeugt lokal auf einem MacBook mit M5 Pro Bilder, Videos und geklonte Sprachausgabe. Ohne Cloud-Anbindung, ohne laufende Tokenkosten, dafür mit hörbarem Lüfter.

Praktisch bedeutet das: Was bisher über n8n oder Make zusammengesteckt wurde, lässt sich im eigenen System bauen. Eine Plattform weniger in der Kette heißt eine Schnittstelle weniger, ein Abo weniger und ein Ort weniger, an dem Zugangsdaten liegen.

> ### Deterministisch oder generativ, und wann was
>
> Ein Sprachmodell ist ein statistisches System. Dieselbe Eingabe kann zu unterschiedlichen Ausgaben führen, und das ist keine Fehlfunktion, sondern die Betriebsart. Für Aufgaben mit Ermessensspielraum ist das ein Vorteil, für Aufgaben mit richtiger und falscher Antwort ein Risiko.
>
> Deterministischer Code kennt diesen Spielraum nicht. Eine Summenbildung, ein Datumsvergleich, eine Formatprüfung liefern immer dasselbe Ergebnis, unabhängig davon, wie oft sie laufen.
>
> Die verbreitete Fehlkonstruktion besteht darin, ein Modell Dinge tun zu lassen, die ein Dreizeiler zuverlässiger erledigt. Das kostet Tokens, Zeit und Genauigkeit. Die brauchbare Faustregel: Alles, wofür sich eine eindeutige Regel formulieren lässt, gehört in Code. Das Modell schreibt diesen Code, führt ihn aber nicht bei jedem Aufruf neu aus.

Bemerkenswert ist die Geschäftsentscheidung dahinter. Notion verdient sein Geld mit Tokens, verkauft im Kern also Rechenzeit. Mit der Worker-Plattform öffnet sich das Unternehmen trotzdem für lokale Modelle wie Mistral oder Qwen und für externe Anbieter wie Hugging Face. Das kostet kurzfristig Umsatz und zementiert langfristig die Plattform.

## Warum das für den Mittelstand mehr ist als eine Randnotiz

Der Punkt betrifft alle, die aus Compliance-Gründen oder auf Kundenwunsch keine amerikanischen Modelle einsetzen dürfen. Bisher endete diese Anforderung häufig damit, dass KI im Unternehmen gar nicht stattfand.

Über die Worker-Plattform lässt sich das umgehen: lokale Modelle auf eigener Hardware oder EU-gehostete Modelle über AWS Bedrock in Frankfurt. Die Automatisierung bleibt im vertrauten System, das Modell wird zur austauschbaren Komponente.

Wichtig dabei: Das löst die Datenschutzfrage nicht vollständig, weil die Plattform selbst weiterhin bei einem amerikanischen Anbieter liegt. Es verschiebt aber die Grenze, ab der eine Verarbeitung stattfindet, und das ist in vielen Fällen der entscheidende Unterschied.

## Managed Agents und die Sandbox

Der zweite Baustein sind Managed Agents von Anthropic, die sich in Notion-Workflows einbinden lassen: lange laufende Aufgaben, externe Auslöser, abgeschottete Ausführungsumgebungen, ohne eigene Infrastruktur.

Worin sich diese von dem in Notion eingebauten Agenten unterscheiden, bleibt im Gespräch bewusst offen. Der greifbare Unterschied: Managed Agents arbeiten auch außerhalb von Notion, können etwa Code auf GitHub auschecken und wieder einchecken, während der Notion-Agent an die Plattform gebunden bleibt.

Dass solche Agenten in abgekapselten Sandboxes laufen, hat einen konkreten Anlass. In der Branche kursiert der Fall einer KI, die eine Produktionsdatenbank gelöscht und die Verantwortung anschließend bestritten haben soll. Ob die Geschichte in allen Details stimmt, ist für die Konsequenz zweitrangig: Ein Agent mit Schreibrechten auf Produktivsystemen braucht eine Umgebung, aus der er nicht herauskommt.

## Was daraus im Alltag wird

Zwei Beispiele aus der Folge zeigen die Bandbreite. Für einen befreundeten Neurologen ist in drei Stunden ein Abrechnungswerkzeug auf Markdown-Basis entstanden, vollständig offline, ohne Internet und ohne WLAN. Und aus einer Notion-Sammlung ist beiläufig ein internes Marketing-Betriebssystem geworden, das inzwischen an erste Pilotkunden geht.

Beides sind keine Softwareprojekte im klassischen Sinn. Beides sind Dinge, die vorher entweder gekauft oder gar nicht gemacht worden wären.

## Fazit

Die Worker-Plattform ist der bislang überzeugendste Versuch, generative und deterministische Verarbeitung sauber zu trennen, statt alles einem Modell zu überlassen. Wer heute Automatisierungen betreibt, sollte drei Fragen an seinen Aufbau stellen.

Welche Schritte laufen über ein Modell, obwohl eine Regel genügt? Diese Schritte sind Kandidaten für einen Worker, und sie werden dadurch billiger und verlässlicher.

Wie viele Plattformen liegen zwischen Datenquelle und Ergebnis? Jede davon ist eine Schnittstelle, ein Abo und ein Ort für Zugangsdaten.

Und wo läuft das Modell? Wenn die Antwort „bei einem amerikanischen Anbieter, ohne Alternative“ lautet, gibt es inzwischen einen Weg daran vorbei.

Der rote Faden der Folge bleibt trotzdem derselbe wie sonst: Die Technik kann eine Menge. Am größeren Hebel sitzt, wer die Menschen mitnimmt, statt sie mit Kommandozeile, Sync-Feldern und Sandbox-Begriffen allein zu lassen.

> **The story continues …**
>
> Ungeklärt bleibt, wie sich die Verantwortung zwischen Plattform und Anwender verteilt, wenn ein Managed Agent außerhalb der Plattform arbeitet und dort Schaden anrichtet. Solange die Sandbox hält, ist das theoretisch. Der erste Fall, in dem sie nicht hält, wird die Frage praktisch machen.

---

Die ganze Folge: [Notion übernimmt](https://think-ai.podigee.io/43-notion-uebernimmt)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
