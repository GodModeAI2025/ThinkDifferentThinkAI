---
folge: 66
titel: "Token-Budgets: Wer viel verbraucht, hat noch nichts geliefert"
bildtitel: "Verbrauch ist keine Leistung"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/66-token-budget"
---

# Token-Budgets: Wer viel verbraucht, hat noch nichts geliefert

*Abo leer, API-Rechnung höher als der Monatspreis: Der Verbrauch an Tokens sagt wenig über den Nutzen. Warum Budgets sinnvoll sind, solange sie am Ergebnis messen und nicht am Volumen.*

Von Mark Zimmermann und Jens Scharnetzki

Jens Scharnetzki arbeitet einen Tag lang am Code, bis das Kontingent seines Abos aufgebraucht ist. Die Arbeit muss trotzdem fertig werden, also schaltet er auf Abrechnung pro Token um. Am Abend liegt die Rechnung dieses einen Tages über dem, was das Abo im ganzen Monat kostet. Seine Arbeitsweise hatte er nicht geändert: Er lässt viele Agenten parallel laufen und wechselt zwischen größeren und kleineren Modellen.

Der Vorfall ist kein Ausreißer, sondern ein Muster. Die Preismodelle der Anbieter belohnen den, der viel verbraucht, und die Unternehmen haben diesen Verbrauch eine Zeit lang als Leistungsnachweis gelesen. Das kippt gerade. Der Grund ist weniger der Preis als die Einsicht, dass Volumen und Wert zwei verschiedene Größen sind.

> **kurz & knapp**
>
> - Ein Abo deckt die Last nicht, die produktive Agentenarbeit erzeugt. Bei Abrechnung pro Token kann ein einzelner Arbeitstag mehr kosten als das Monatsabo.
> - „Token Maximizing“ misst Entwickler am Verbrauch. Das ist so aussagekräftig wie die Zeilenzahl im Quelltext.
> - Der Preis je Token ist nicht der Treiber. Die Rechnung steigt, weil die Modelle größere Aufgaben übernehmen.
> - Für viele Standardaufgaben reichen kleinere oder ältere Modelle. Das größte Modell ist selten die richtige Wahl.
> - Ein persönlicher Agent auf dem iPhone zeigt die Gegenrichtung: Die Kosten tragen die Nutzer über ihr Apple-Kontingent, nicht der Entwickler.

## Die Rechnung hat mehr Posten als den Token

Wer Kosten bewertet, muss das Ergebnis danebenlegen. Mark Zimmermann ließ ein Video von zweieinhalb Minuten erzeugen und verbrauchte an einem Abend Tokens im Wert von rund 200 Dollar. Das Resultat war für den Zweck, eine Vorführung, ausreichend. Auf professionelle Qualität gebracht, wäre es teurer geworden. Der klassische Weg hätte allerdings ein Briefing, einen Dienstleister und Rechenzeit für das Rendern verlangt, oder die eigene Arbeitszeit. Aus dieser Gesamtrechnung ergibt sich nach Marks Einschätzung eher ein Vorteil für den KI-Einsatz. Gerechnet haben die Hosts das nicht, es bleibt eine Schätzung aus dem Bauch.

Jens Scharnetzki bezweifelt dagegen, dass die Abo-Modelle für die Anbieter aufgehen. Wer an einem Tag mehr verbraucht, als das Abo im Monat kostet, bekommt im Grunde subventionierte Rechenleistung. Er rechnet damit, dass sich das ändert, sobald die Anbieter an die Börse gehen. Beide Hosts erwähnten Berichte, nach denen Anthropic und OpenAI Börsengänge vorbereiten. Belegt ist das in der Folge nicht, es ist ihre Lesart.

Dazu kommt ein zweiter Effekt: Schnelle Varianten kosten mehr. Jens nutzte ein Modell im Turbo-Modus und leerte damit ein 500er-Abo in fünf Stunden. Mehrere Projekte liefen parallel, keines wurde ganz fertig. Er zieht daraus den Schluss, dass die Geschwindigkeit dort nichts brachte, wo ohnehin über eine Woche gearbeitet wird. Sein Vorsatz seither: Dem Modell mehr Zeit lassen, damit es durchgehend beschäftigt ist, statt die Tokens in einem Stoß zu verbrennen.

## Token Maximizing war die falsche Kennzahl

Der Begriff entstand Anfang des Jahres. Wer als Entwickler nicht Millionen von Tokens verbrauchte, galt in den Augen mancher Arbeitgeber als wenig wert. Jens beschreibt das als Marketinggeschichte der großen Anbieter, die damit den eigenen Absatz erklärten. Mark berichtet von einem Bekannten mit fünf großen Abos bei Anthropic, der damit eine Woche nicht auskomme. Wer ein Abo geleert hat, meldet sich beim nächsten an und arbeitet weiter.

Die Hosts sehen, dass sich das im Sommer gedreht hat. Der Verbrauch wurde kritischer betrachtet, auch wegen der Rechenzentren, die in den USA neben Wohngebieten entstehen. Anfang November kamen Berichte hinzu, nach denen große Konzerne wie Apple, Tesla und Microsoft die Budgets für ihre Entwickler gesenkt haben. Mark nannte aus dem Gedächtnis eine Absenkung von 300 auf 200 Dollar am Tag und für einzelne Abteilungen bei Tesla 200 Dollar pro Woche. Die Zahlen sind unbestätigt und wurden im Gespräch nicht nachgeprüft. Die Richtung ist aber klar: Auf die Phase des freien Ausprobierens folgt die Deckelung.

Das ist an sich nicht verkehrt. Ein Budget zwingt zur Frage, wofür ein Modell eingesetzt wird. Schwierig wird es, wenn es nur den Verbrauch begrenzt, ohne zu fragen, was dabei herauskommt.

> „Nur weil mir jemand den Ferrari in die Garage stellt, heißt das nicht, dass ich ihn effizient fahre, dass ich ihn nicht kaputtfahre, dass ich ihn überhaupt beherrsche.“
>
> **Jens Scharnetzki**, Co-Host

Jens bringt damit auf den Punkt, was ein Budget leisten soll. Es ersetzt nicht die Fähigkeit, mit dem System umzugehen. Wer einem Agenten aufträgt, 50 Subagenten mit der höchsten Stufe zu starten und das Ganze zwanzigmal zu wiederholen, um am Ende zwei Zahlen zu addieren, treibt die Kosten ohne Nutzen. Das Gegenmittel ist laut Jens ein Skill, der Agenten zu sparsamem Code anhält. Nach seiner Angabe senkt er den Verbrauch um 50 bis 60 Prozent. Eine unabhängige Messung gibt es dafür nicht.

## Teurer geworden oder mehr geleistet?

Jens widerspricht dem Satz, Tokens würden teurer. Das kleine Abo koste heute so viel wie vor einem Jahr, bringe aber ein Vielfaches an Leistung. Der höhere Verbrauch komme daher, dass man den Modellen größere Aufgaben gebe: Statt über einen Prototyp zu reden, bringe man ihn fertig mit. Wer mehr nutze und deshalb mehr bezahle, habe damit noch nichts über den Preis je Leistung gesagt.

Daraus folgt eine praktische Frage, die laut Mark selbst Programmierer schwer beantworten können: Welche Aufgabe braucht welches Modell? Wer eine Präsentation aufbereitet, braucht nicht das neueste Frontier-Modell. Ein schwächeres, womöglich lokal laufendes Modell hat die Aufgabe bis morgen erledigt. Jens arbeitet für Standardaufgaben gern mit kleineren Modellen aus der Claude-Familie und nennt sie im Verhältnis zum Nutzen sehr günstig. Beide Hosts schätzen aus dem Bauch, dass die Modelle des Vorjahres bei rund 90 Prozent der alltäglichen Fälle ausreichen.

Zur Wahl des Modells kommt die Wahl der Kennzahl. Mark verweist darauf, dass Zeilen im Quelltext nie etwas über die Qualität eines Produkts ausgesagt haben.

> „Wenn das Problem hinterher gelöst ist und besser gelöst ist, als wir das auf eine andere Art und Weise gelöst hätten, dann war es ja sinnvoll.“
>
> **Mark Zimmermann**, Co-Host

Marks Maßstab ist der Outcome, also das, was am Ende wirtschaftlich trägt, nicht der Output. Wer viele Tokens ausgibt, ist damit weder verschwenderisch noch professionell. Das sagt erst das Ergebnis.

> ### Was Apples Private Cloud Compute ist
>
> Apple betreibt für die eigene KI-Funktion Apple Intelligence Server, auf denen Anfragen verarbeitet werden, die das Gerät nicht selbst bewältigt. Nach Angaben von Apple entspricht das Datenschutzniveau dort dem der Verarbeitung auf dem iPhone. Mark hält das System für deutlich schärfer abgesichert als übliche Cloud-Angebote und verweist darauf, dass Apple Hardware und Infrastruktur absichert und Sicherheitsforschern den Zugang zur Prüfung öffnet. Die Rechenleistung zählt gegen das Kontingent der Nutzer, das vom iCloud-Abo abhängt. Mark fand dazu keine Umrechnungstabelle, nur Hinweise aus Reddit, dass ein teureres Abo mehr Leistung bringt. Für Entwickler soll die Nutzung bis zu einer Zahl von Installationen kostenlos sein. Ob die Grenze bei 200.000 oder 2 Millionen liegt, wusste Mark im Gespräch nicht sicher, und ob Apple die kostenlosen Kontingente verringert, ist offen. Bilder analysiert das System derzeit nicht.

## Der Gegenentwurf in der Hosentasche

Wie anders Abrechnung aussehen kann, zeigt Marks Experiment auf seinem neuen faltbaren iPhone. Er hat dort einen eigenen Harness gebaut, also die Laufzeitumgebung und Oberfläche, über die ein Mensch mit dem Modell arbeitet. Das Modell kommt nicht von Anthropic oder OpenAI, sondern aus Apples Private Cloud Compute. Der Agent führt zeitgesteuerte Aufträge lokal aus, ohne Serverlaufzeit: Wer ihm sagt, er solle morgen um acht etwas erledigen, bekommt dann ein Tagesbriefing oder die Recherche der letzten vier Stunden.

Bemerkenswert ist die Umgehung eines Verbots. iOS erlaubt nicht, Code zur Laufzeit auszuführen, eine klassische Sandbox ist also nicht vorgesehen. Marks Coding-Agent baute stattdessen einen Python-Interpreter, der den Code unmittelbar in etwas übersetzt, das Apple zulässt. Damit kann der Agent Skills ausführen und zum Beispiel Recherche in Folien überführen. Er hat Zugriff auf Gesundheit, Ort, Kalender und Dateien. Mails muss man über IMAP freigeben, sonst lässt Apple den Zugriff nicht zu.

Auch die Oberfläche folgt keinem Chatfenster. Sie sieht aus wie ein Notizbuch mit Seiten für Packlisten und Kalender. Handschrift wird erkannt, und was in einer anderen Farbe geschrieben wird, gilt als Kommando an die KI. Im Chat lassen sich Absätze mit dem Stift anstreichen, etwa „ausführlicher“ oder „weniger“. Dazu kommt ein Browser, der aussieht wie Safari, aber keiner ist und vom Agenten bedient wird.

Warum nicht auf dem Mac? Mark hält dagegen, dass ein Mac Mini gewartet werden will und ein zugeklappter Mac meist schlafen geht. Das Handy hat man im Urlaub dabei. Noch fehlt ein ausreichend starkes lokales Modell auf dem Gerät. Sobald es das gibt, bleibt nach Marks Bild nur das Modell entfernt und alles andere lokal.

## Fazit

Die Folge liefert eine Faustregel: Ein Budget ist so gut wie die Kennzahl, an der es hängt. Wer Verbrauch begrenzt, ohne Ergebnisse zu messen, trifft die Falschen. Wer das Volumen als Leistungsnachweis wertet, belohnt die, die am meisten verbrennen.

Daraus folgen drei Konsequenzen. Erstens gehört zu jeder Aufgabe die Frage nach dem kleinsten Modell, das sie erledigt. Zweitens gehören zur Kostenrechnung die Posten außerhalb der Rechnung des Anbieters: Zeit, Rechenleistung, Qualität des Ergebnisses. Drittens braucht es eine Kennzahl, die den Wert des Ergebnisses abbildet, etwa den wirtschaftlichen Erfolg, und nicht die Zahl der Tokens.

Mark nennt noch eine Studie, die er von einem Fachautor weitergeleitet sah. Sie soll Faktenchecks wissenschaftlicher Studien verglichen haben: Menschen lagen demnach bei etwa 25 Prozent, die besten Modelle über 90 Prozent. Die Studie haben die Hosts nicht geprüft. Mark leitet daraus ab, dass das Gefühl für Richtigkeit die KI-Prüfung nicht mehr schlägt. Für Budgets heißt das: Wer Qualität beurteilen will, sollte das nicht dem Bauchgefühl überlassen.

> **The story continues …**
>
> Die Börsengänge der großen Anbieter und die Frage, ob Apple seine kostenlosen Kontingente beibehält, entscheiden, wie die Preise für Abos und Schnittstellen aussehen. In einer der nächsten Folgen wollen die Hosts auf neue Anwendungen schauen, etwa auf 3D-Webseiten, die eine KI über Blender per MCP baut.

---

Die ganze Folge: [Token Budget](https://think-ai.podigee.io/66-token-budget)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
