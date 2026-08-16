---
folge: 45
titel: "90 Minuten bis zur Abschaltung: Was der Fable-Fall über KI-Souveränität zeigt"
bildtitel: "90 Minuten bis zur Abschaltung"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/45-three-days-of-fable"
---

# 90 Minuten bis zur Abschaltung: Was der Fable-Fall über KI-Souveränität zeigt

*Drei Tage nach dem Start war Fable 5 für Nicht-US-Bürger nicht mehr erreichbar. Laufende Sitzungen brachen ab, Kontext war verloren. Der Vorgang eignet sich als Prüfstein für die eigene Architektur.*

Von Mark Zimmermann

Anthropic hat Fable 5 veröffentlicht, ein Modell der sogenannten Mythos-Klasse. Diese Reihe stand zuvor nur großen Anbietern wie Amazon und Google zur Verfügung, weil sie ungewöhnlich gut darin ist, Sicherheitslücken zu finden. Bei Firefox wurden auf diesem Weg an einem Tag Hunderte kritischer Fehler entdeckt und geschlossen. Laut einem Bericht bei heise online hat eine Sicherheitsfirma mit Mythos einen Speicherschutz-Exploit auf Apple-M5-Hardware in fünf Tagen geknackt.

Drei Tage nach dem Start war das Modell für alle Nutzer außerhalb der USA weg. Dazwischen lagen ein geleakter System-Prompt, eine Anhörung im Weißen Haus und die Einstufung von Anthropic als Lieferkettenrisiko.

> **kurz & knapp**
>
> - Von der Entscheidung bis zur Abschaltung vergingen rund 90 Minuten
> - Laufende Sitzungen brachen ab, Kontext ließ sich nicht sauber auf andere Modelle übertragen
> - Offene Alternativen lösen das Problem nicht grundsätzlich, sobald sie strategisch relevant werden
> - Die praktische Konsequenz ist ein Modell-Switcher in der eigenen Architektur
> - Wissen gehört modellunabhängig abgelegt, nicht in die Sitzung eines Anbieters

## Was technisch passiert ist

Der eigentliche Schaden lag nicht im Wegfall des Modells, sondern im Zeitpunkt. Die Abschaltung erfolgte mitten im Betrieb. Sitzungen hingen, Projekte standen, und der aufgebaute Kontext ließ sich nicht ohne Verlust auf ein anderes Modell übertragen.

Das ist ein Punkt, der bei Ausfallkonzepten regelmäßig übersehen wird. Ein Modellwechsel ist keine Umleitung des Datenverkehrs. Was in einer langen Sitzung an Zwischenergebnissen, Begründungen und Festlegungen entstanden ist, existiert nur dort. Ein anderes Modell bekommt bestenfalls die Konversation übergeben und muss die Schlussfolgerungen neu ziehen, häufig anders.

Beachten Sie den Unterschied zu klassischen Abhängigkeiten. Fällt eine Datenbank aus, sind die Daten weiterhin da. Fällt ein Modell aus, ist der Zustand weg, sofern er nicht außerhalb gesichert wurde.

## Die geopolitische Einordnung

Der naheliegende Vergleich in der Folge ist der Kill-Switch-Verdacht bei Kampfjets: die Frage, ob sich ein importiertes System aus der Ferne unbrauchbar machen lässt. Der zweite Vergleich stammt aus der Pandemie und betrifft die Erkenntnis, wie abhängig Europa in kritischen Lieferketten tatsächlich ist.

Beide Vergleiche sind zugespitzt und treffen einen realen Punkt: Ein Sprachmodell ist ein importiertes Erzeugnis mit einer Verfügbarkeit, die von Handelspolitik abhängt.

Offene Modelle wie Kimi, MiniMax M3 oder Manus mildern das, lösen es aber nicht grundsätzlich. Sobald ein Modell strategisch relevant wird, wird es auch reguliert, unabhängig vom Herkunftsland. Wer offene Gewichte als dauerhafte Absicherung betrachtet, verlässt sich auf einen Zustand, nicht auf eine Eigenschaft.

> ### Was KI-Souveränität praktisch bedeutet
>
> Der Begriff wird häufig auf die Frage verkürzt, wo ein Modell trainiert wurde. Für den Betrieb sind drei andere Ebenen wichtiger.
>
> **Verfügbarkeit:** Können Sie den Dienst weiter nutzen, wenn eine Regierung oder ein Anbieter das nicht mehr möchte. Antwort darauf ist ein zweiter, tatsächlich getesteter Anbieter, nicht ein Vertrag mit einem zweiten.
>
> **Kontrolle über die Umgebung:** Wem gehört der Harness, in dem das Modell arbeitet. Liegen Skills, Kontextverwaltung und Protokolle bei Ihnen, ist das Modell eine Komponente. Liegen sie beim Anbieter, ist Ihr Prozess sein Produkt.
>
> **Kontrolle über das Wissen:** Wo liegt das, was Ihre Organisation gelernt hat. Solange das in Sitzungen und Anbieter-Projekten liegt, wandert es mit dem Anbieter.
>
> Nur die erste Ebene hängt an der Geopolitik. Die anderen beiden sind Architekturentscheidungen und lassen sich ohne politische Debatte treffen.

## Die Konsequenz: Modell-Switcher

Die praktische Empfehlung der Folge ist eindeutig.

> „Das ist etwas, was man mitnehmen sollte: Ich brauche irgendeine Art intelligenten Modell-Switcher.“
>
> **Mark Zimmermann**, Co-Host

Intelligent heißt in diesem Zusammenhang mehr als eine Konfigurationsvariable. Ein brauchbarer Switcher kennt die Eigenheiten der angebundenen Modelle, weiß, welche Aufgabe welches Modell verträgt, und hat für jede Aufgabe einen geprüften Ersatz. Er ist zugleich der Ort, an dem sich Kostensteuerung unterbringen lässt, weil nicht jede Anfrage das größte Modell braucht.

Die ehrliche Einschränkung wird in der Folge mitgeliefert: Beim Wechsel geht Reasoning und Kontext verloren, wenn beides nicht separat gesichert ist. Ein Switcher allein reicht nicht. Er löst das Verfügbarkeitsproblem und nicht das Zustandsproblem.

## Wissen gehört nach draußen

Damit ist der zweite Teil der Konsequenz beschrieben, und er ist der aufwendigere. Was Ihre Organisation weiß, darf nicht in der Sitzung eines Modells leben. Es gehört in eine eigene Ablage, modellunabhängig, durchsuchbar und in einem Format, das jedes Modell verarbeiten kann.

Als konkreten Ansatz bringt die Folge Googles Open Knowledge Format ins Spiel. Der Gedanke dahinter ist unspektakulär und gerade deshalb überzeugend: Fachdokumentation sollte sich wieder auf Inhalt konzentrieren statt auf Formatierung. Was als Textstruktur vorliegt, lässt sich sparsam in Tokens übersetzen. Was als Layout vorliegt, kostet Tokens für Information, die niemand braucht.

Wer das ernst nimmt, kommt zu einer unbequemen Schlussfolgerung über die eigene Ablage. Präsentationen und formatierte Dokumente sind für Maschinen schlechte Träger von Wissen, und der Anteil des Wissens, der nur dort existiert, ist in den meisten Organisationen groß.

## Fazit

Der Fable-Fall ist kein Argument gegen den Einsatz amerikanischer Modelle. Er ist ein Argument gegen die Annahme, ein Modell sei eine dauerhaft verfügbare Infrastruktur.

Drei Maßnahmen folgen daraus, und alle drei lassen sich ohne große Investition beginnen. Testen Sie einmal im Quartal, ob Ihre wichtigsten Abläufe auf einem zweiten Modell laufen. Sichern Sie Zwischenstände und Festlegungen außerhalb der Sitzung. Und legen Sie Wissen so ab, dass es ein beliebiges Modell lesen kann.

Der Aufwand dafür ist überschaubar. Der Aufwand, dasselbe unter Zeitdruck zu tun, während die Sitzungen bereits hängen, ist es nicht.

> **The story continues …**
>
> Ungeklärt bleibt, wie sich europäische Anbieter in dieser Gemengelage positionieren und ob eine europäische Alternative auf Augenhöhe entsteht. Bis dahin ist Souveränität weniger eine Frage der Herkunft des Modells als der Frage, wie schnell Sie es austauschen können.

---

Die ganze Folge: [Three Days of Fable](https://think-ai.podigee.io/45-three-days-of-fable)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
