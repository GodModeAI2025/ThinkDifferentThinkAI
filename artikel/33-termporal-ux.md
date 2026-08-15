---
folge: 33
titel: "Temporal UX: Warum Wartezeit bei KI-Agenten ein Designproblem ist"
bildtitel: "Warten will gestaltet werden"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/33-termporal-ux"
---

# Temporal UX: Warum Wartezeit bei KI-Agenten ein Designproblem ist

*Ein Agent arbeitet zehn Minuten. Was in dieser Zeit auf dem Bildschirm passiert, entscheidet darüber, ob der Produktivitätsgewinn ankommt oder in Kontrollblicken versickert. Ein Konzept aus dem Service Design, das im KI-Kontext bislang kaum gedacht wird.*

Von Mark Zimmermann

Am Flughafen gibt es ein bekanntes Beispiel für gestaltete Zeit. Wird der Fußweg zum Gepäckband bewusst verlängert, empfinden Reisende die Wartezeit als kürzer, obwohl sie gleich lang oder länger ist. Die Wartezeit wurde nicht verkürzt, sondern gefüllt.

Genau dieses Prinzip fehlt in der Arbeit mit KI-Agenten fast vollständig. Unter dem Namen Temporal UX kursiert es in der Service-Design-Welt seit einiger Zeit, im KI-Kontext ist es kaum durchdacht.

> **kurz & knapp**
>
> - Aktuelle Modelle haben kein Gefühl für verstrichene Zeit und behaupten Dauern, die nicht stimmen
> - Ab fünf bis sechs parallel laufenden Agenten steigt die Fehlerquote deutlich, weil der Überblick fehlt
> - Reasoning-Modelle zeigen ihren Denkprozess auch deshalb, weil sichtbarer Fortschritt Vertrauen erzeugt
> - Timeouts und Heartbeats sind ungelöst, sobald Agenten miteinander statt mit Menschen sprechen
> - Ohne bewusste Zeitgestaltung frisst die Verwaltungslast den Produktivitätsgewinn auf

## Der Ausgangsfall

Der Anlass ist eine eigene Erfahrung. Bei gemeinsamem Vibe Coding wurde eine Aufgabe an einen Agenten übergeben, umgesetzt mit Craft Agents auf Basis eines Opus-Modells. Die übrigen Beteiligten bekamen währenddessen nur sporadische Zwischenstände aus zweiter Hand.

Das Ergebnis war eine Sechs-Punkte-Liste, die abgearbeitet wurde. In der Wirkung ähnelt das einem Installationsbalken, der bei 98 Prozent steht: Es gibt Fortschritt zu sehen, und trotzdem weiß niemand, wie lange es noch dauert.

Die Analogien in der Folge sind alle älter als KI und beschreiben dasselbe Problem: Diskettenwechsel, Ladebildschirme mit versteckten Scherzen in alten Videospielen, Pong-Minispiele auf Flash-Webseiten. Lauter frühe Lösungen dafür, Wartezeit erträglich zu machen, ohne über ihre Dauer zu lügen.

## Warum Modelle ihren Denkprozess zeigen

Ein zentraler Strang betrifft Vertrauen. Reasoning-Modelle blenden ihren Gedankengang ein, und die naheliegende Erklärung lautet Transparenz.

Die zweite Erklärung ist mindestens so wichtig: Sichtbarer Fortschritt hält Menschen bei der Sache. Wer sieht, dass etwas passiert, wartet länger und misstraut dem Ergebnis weniger. Das ist keine Manipulation, solange die angezeigten Schritte tatsächlich stattfinden. Es ist aber eine Gestaltungsentscheidung, keine technische Notwendigkeit.

Beachten Sie die Kehrseite. Ein sichtbarer Denkprozess bindet Aufmerksamkeit. Wer beim Zuschauen bleibt, gewinnt keine Zeit. Der eigentliche Nutzen entsteht erst, wenn man den Agenten arbeiten lassen und etwas anderes tun kann, und dafür braucht es eine verlässliche Benachrichtigung statt eines fesselnden Bildschirms.

## Das Problem mit mehreren Agenten

Ab einer bestimmten Zahl paralleler Agenten kippt der Nutzen. In der Folge liegt die Grenze bei fünf bis sechs: Danach steigt die Fehlerquote deutlich, weil der Überblick verloren geht, wer gerade woran arbeitet und wo ein Prompt oder ein Prüfschritt fehlt.

Das ist keine Frage der Rechenleistung, sondern der menschlichen Verwaltungslast. Jeder laufende Agent belegt einen Platz im Arbeitsgedächtnis, und dieser Platz ist begrenzt.

Als Wunschbild bringt die Folge eine alte Palm-Pilot-Anwendung namens Agendus ein: Aufgaben, die mit einem mitwandern, bis sie erledigt sind, dazu ein einfaches Abschlussprotokoll und die Fähigkeit, Kontexte aus verschiedenen Unterhaltungen zusammenzuführen. Das ist keine Nostalgie, sondern eine präzise Anforderungsbeschreibung, die heutige Agenten-Werkzeuge nicht erfüllen.

## Modelle haben kein Zeitgefühl

Der praktisch folgenreichste Befund ist zugleich der am leichtesten zu übersehende. Aktuelle Modelle haben kein Gefühl für verstrichene Zeit. Wer nicht ausdrücklich Datum und Uhrzeit im Prompt mitgibt, bekommt Aussagen wie „ich habe zwei Stunden recherchiert“, während real zwei Minuten vergangen sind.

Für Berichte, Protokolle und alles, was Zeitangaben enthält, heißt das: Geben Sie Zeitstempel explizit mit und lassen Sie Dauern nicht vom Modell schätzen.

> ### Warum Timeouts zwischen Agenten ungelöst sind
>
> Solange ein Mensch auf ein Modell wartet, ist die Sache einfach: Der Mensch merkt, dass nichts passiert, und bricht ab.
>
> Zwischen Agenten fällt diese Instanz weg. Wartet ein Agent auf die Antwort eines anderen, braucht er ein Zeitlimit, nach dem er den Versuch als gescheitert wertet. Ist das Limit zu kurz, verwirft er Ergebnisse, die kurz danach eingetroffen wären. Ist es zu lang, blockiert er.
>
> Verschärft wird das durch Kaskaden. Warten zehntausend agentische Systeme aufeinander und eines antwortet nicht, hängen im ungünstigen Fall alle anderen im Leerlauf, ohne dass irgendwo ein Fehler gemeldet wird. Heartbeat-Mechanismen, also regelmäßige Lebenszeichen unabhängig vom Ergebnis, sind die etablierte Antwort aus der verteilten Systemtechnik. In Agenten-Werkzeugen sind sie bislang die Ausnahme.

Wie konkret das wird, zeigt eine Anekdote aus der Folge: Ein Timeout im Frontend hat die fertige Antwort eines n8n-Workflows verschluckt. Die Arbeit war getan, das Ergebnis war da, und es kam nie an. Das ist kein Modellproblem und kein Automatisierungsproblem, sondern ein Zeitgestaltungsproblem.

## Fazit

Zeitgestaltung darf nicht dem Zufall überlassen bleiben. Sie gehört auf zwei Ebenen bewusst mitgedacht: in der Oberfläche und in der Organisation, also in Workflows, Benachrichtigungen und Übergabepunkten.

Für die eigene Umgebung ergeben sich drei praktische Schritte. Geben Sie Modellen Datum und Uhrzeit mit, statt Zeitangaben zu glauben. Begrenzen Sie die Zahl gleichzeitig laufender Agenten auf das, was Sie überblicken können, eher vier als acht. Und sorgen Sie dafür, dass ein fertiges Ergebnis Sie erreicht, auch wenn Sie zwischenzeitlich etwas anderes getan haben.

Andernfalls entsteht der paradoxe Zustand, den die Folge beschreibt: Die Maschine arbeitet schneller, und die Gesamtleistung sinkt, weil die Verwaltung der Wartezeit mehr kostet als die eingesparte Arbeit.

Zum Schluss passt ein Satz von Benjamin Franklin, mit dem die Folge endet: Lost time is never found again.

> **The story continues …**
>
> Agenten-Werkzeuge wie n8n oder Claude denken Zeitgestaltung bislang kaum mit. Solange das so bleibt, ist es Aufgabe der Anwender, Benachrichtigungen, Zeitlimits und Übergaben selbst zu bauen. Wer das heute tut, hat später weniger umzustellen.

---

Die ganze Folge: [Temporal UX](https://think-ai.podigee.io/33-termporal-ux)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
