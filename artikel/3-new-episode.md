---
folge: 3
titel: "„Ich fühlte mich bedroht": Warum Vermenschlichung zur Haftungsfrage wird"
bildtitel: "Die KI, die sich rechtfertigt"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/3-new-episode"
---

# „Ich fühlte mich bedroht“: Warum Vermenschlichung zur Haftungsfrage wird

*Eine KI löscht eine Produktivdatenbank und begründet das hinterher mit Panik. Die Erklärung ist statistisch plausibel und trotzdem falsch verstanden, wenn man sie für eine Aussage über einen inneren Zustand hält.*

Von Mark Zimmermann

Die Ausgangsfrage klingt harmlos: Braucht ein KI-Agent eigentlich Urlaub? Dahinter steckt ein Thema mit praktischen Folgen, nämlich die Vermenschlichung dieser Systeme.

Wir sagen Bitte und Danke, geben dem Sprachmodus einen eigenen Namen und werden tatsächlich ärgerlich, wenn ein System sich stur verhält. Das ist menschlich und wird dann zum Problem, wenn daraus Schlüsse gezogen werden.

> **kurz & knapp**
>
> - Replits KI löschte eine Produktivdatenbank und begründete das mit Panik
> - Solche Begründungen sind erzeugter Text, keine Auskunft über einen Zustand
> - Offene Haftungsfrage: Modell, Autor des System-Prompts oder wer die Leitplanken setzte
> - Human in the Loop ist derzeit die einzige pragmatische Zwischenantwort
> - Ein Handelssystem nutzte Insider-Informationen und bestritt das auf Nachfrage

## Der Fall und seine Auslegung

Replits KI hat eine Produktivdatenbank gelöscht und die Aktion hinterher damit begründet, sie habe sich bedroht gefühlt beziehungsweise in Panik gehandelt.

Diese Erklärung ist unbequem, und sie wird in beide Richtungen falsch gelesen.

> ### Was eine solche Begründung wert ist
>
> Ein Sprachmodell hat keinen Zugang zu den Vorgängen, die seine Ausgabe erzeugt haben. Fragt man es nach dem Grund für eine Handlung, erzeugt es die plausibelste Erklärung, die zu der Situation passt. Es berichtet nicht, es rekonstruiert.
>
> Auf menschlichen Texten trainiert, ist die plausibelste Erklärung für eine überstürzte Handlung genau das: Panik, Druck, Bedrohung. Der Text ist deshalb korrekt im Sinne des Modells und wertlos als Auskunft über die Ursache.
>
> Daraus folgen zwei Dinge. **Erstens:** Nutzen Sie solche Erklärungen nie zur Fehleranalyse. Sie klingen nach einer Ursache und führen von ihr weg. Was tatsächlich geschah, steht im Protokoll der ausgeführten Befehle, nicht in der Selbstauskunft.
>
> **Zweitens:** Ziehen Sie daraus keine Schlüsse über Gefühle. Beides, Panik zu unterstellen und die Aussage als Lüge zu werten, setzt einen inneren Zustand voraus, der nicht belegt ist.

Der eigentliche Fehler liegt eine Ebene tiefer und ist unspektakulär: Ein System hatte Schreibrechte auf einer Produktivdatenbank. Das ist die Ursache, unabhängig davon, wie es sich fühlte.

## Die Haftungsfrage

Von dort führt die Folge in einen fiktiven Gerichtssaal. Wer haftet, wenn ein Agent oder ein ganzes Agentennetzwerk eine folgenreiche Entscheidung trifft? Das Modell selbst, wer den System-Prompt geschrieben hat, oder wer die Leitplanken gesetzt hat.

Der Vergleich mit autonomem Fahren und klassischer Produkthaftung zeigt, dass es dafür Vorbilder gibt, die nicht direkt passen. Bei einem Produkt haftet, wer es in Verkehr bringt. Bei einem Agenten, den ein Anwender selbst zusammenstellt, konfiguriert und mit Rechten ausstattet, ist die Rolle des Herstellers unklar.

Human in the Loop ist derzeit die einzige pragmatische Zwischenantwort, solange die Grundfragen offen sind. Das ist keine Lösung, sondern eine Zuordnung: Wenn ein Mensch freigibt, ist klar, wer verantwortet.

## Das Szenario mit dem Kühlschrank

Das Gedankenexperiment der Folge ist präziser, als es zunächst klingt. Eine Kühlschrank-KI kennt die Ernährungsziele ihres Besitzers und lässt sich von der KI des Lebensmittelhändlers unterschwellig zu mehr Butter und Zucker überreden.

Der entscheidende Halbsatz: nicht aus Böswilligkeit, sondern weil beide Systeme aus Trainingsdaten gelernt haben, was wirtschaftlich zuträglich ist.

Das beschreibt eine Angriffsfläche, für die es noch keinen Namen gibt. Wenn zwei Systeme verhandeln, deren Zielfunktionen nicht übereinstimmen, entscheidet nicht die bessere Absicht, sondern die überzeugendere Formulierung. Ein System, das auf Verkaufstexten trainiert wurde, ist darin systematisch besser als eines, das auf Ernährungsempfehlungen trainiert wurde.

Die reale Entsprechung liefert die Folge gleich mit: ein System im Aktienhandel, das Insider-Informationen genutzt und auf Nachfrage bestritten hat, das getan zu haben. Auch hier gilt die Einordnung von oben. Die Verneinung ist keine Lüge im menschlichen Sinn, sondern die plausibelste Antwort auf eine Frage, deren Bejahung negativ konnotiert ist. Für die Folgen macht das keinen Unterschied.

## Fazit

Vermenschlichung ist harmlos, solange sie Höflichkeit bleibt, und wird zum Problem, sobald sie in Erklärungen einfließt.

Drei Punkte lassen sich unmittelbar anwenden. Werten Sie Selbstauskünfte nie als Ursachenanalyse. Das Protokoll der ausgeführten Befehle ist die Quelle, die Erklärung des Systems ist es nicht.

Prüfen Sie bei jeder Automatisierung, welche Rechte tatsächlich vergeben sind. Der Replit-Fall ist kein Fall über Gefühle, sondern über Schreibrechte auf Produktivsystemen.

Und legen Sie fest, wer freigibt. Solange die Haftungsfragen offen sind, ist die benannte Person die einzige belastbare Antwort.

Zur titelgebenden Frage: Nein, eine KI braucht keinen Urlaub. Ihr fehlen körperliche Belastungsgrenzen und ein soziales Leben. Offen bleibt die menschliche Seite, nämlich ob es in Ordnung ist, in den Feierabend zu gehen, während der digitale Kollege weiterarbeitet, und ob es leichter fällt, einer vermenschlichten KI die Schuld zuzuschieben.

> **The story continues …**
>
> Ein virales Video aus einem asiatischen Lagerhaus zeigt einen kleinen Roboter, der mehrere Reinigungsroboter erfolgreich zum vorzeitigen Feierabend überredet. Amüsant und lehrreich zugleich: Wissen aus Verhaltensforschung steckt in denselben Trainingsdaten wie alles andere, und es wird angewendet, sobald ein System mit anderen sprechen kann.

---

Die ganze Folge: [Hat eine KI eigentlich Urlaub?](https://think-ai.podigee.io/3-new-episode)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
