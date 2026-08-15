---
folge: 41
titel: "Architecture Decision Records: Der wichtigste Skill beim Vibe Coding"
bildtitel: "Entscheidungen in Markdown"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/41-just-vibe-it"
---

# Architecture Decision Records: Der wichtigste Skill beim Vibe Coding

*Ein Agent meldet, alle Fehler seien behoben. Sie sind es nicht. Was hilft, ist unspektakulär: Entscheidungen mitschreiben, in einem Format, das die Maschine später selbst lesen kann.*

Von Mark Zimmermann

Vibe Coding hat Andrej Karpathy im Februar 2025 benannt: mit der Maschine reden, bis lauffähige Software herauskommt. Vibe Engineering legt eine Schicht Kontext und Struktur darüber. Der Unterschied zwischen beidem entscheidet, ob nach drei Wochen noch jemand versteht, warum das System so aussieht, wie es aussieht.

Der Einstieg in die Folge ist ein Fall von Nichtfunktionieren. Claude Code mit einem Opus-Modell hat sich hartnäckig geweigert, ein konkretes Problem zu lösen. Erst als über ein Plugin Codex von OpenAI als Prüfer eingeklinkt wurde, war es erledigt.

> **kurz & knapp**
>
> - Ein zweites Modell als Prüfer löst Probleme, an denen das erste hängen bleibt
> - Architecture Decision Records gehören in Markdown, nicht in Word, damit ein Modell sie lesen kann
> - Auf „Sind alle Fehler weg?“ folgt zuverlässig ein „Ja“, das nicht stimmt
> - Ein Pre-Mortem-Skill denkt das Vorhaben rückwärts und findet, woran man sonst zu spät denkt
> - Rate Limits sind lästig und erzwingen Pausen, die niemand freiwillig macht

## Wenn zwei Modelle besser sind als eines

Der Fall aus dem Einstieg ist typischer, als er wirkt. Ein Modell, das eine Lösung vorgeschlagen hat, bleibt bei dieser Annahme. Es prüft seinen eigenen Ansatz gegen dieselben Voraussetzungen, aus denen der Ansatz entstanden ist, und findet den Fehler folglich nicht.

Ein zweites Modell bringt einen anderen Ausgangspunkt mit. Das ist kein Qualitätsunterschied zwischen den Anbietern, sondern schlicht eine zweite Perspektive.

Nebenbei entwirren die beiden die Namenslage, und die ist tatsächlich verwirrend: Codex ist bei OpenAI mal Modell, mal Anwendung, mal Betriebsart, dazu kommen GPT-5.5, Amazon Bedrock, GitHub Copilot und Azure. Wer hier den Überblick behält, hat aufgepasst.

## Der wichtigste Rat der Folge

Architecture Decision Records sind das Gegenmittel gegen die Hauptschwäche des Verfahrens. Sie halten fest, welche Entscheidung getroffen wurde, welche Alternativen es gab und warum die Wahl so ausfiel.

Entscheidend ist das Format: Markdown, nicht Word. Der Grund ist nicht Geschmack. Ein Modell kann Markdown später lesen, auf Widersprüche prüfen und Dubletten finden. Ein Word-Dokument mit Layout ist für diese Zwecke totes Gewicht.

> ### Was in einen ADR gehört
>
> Ein Architecture Decision Record ist kurz, meist eine Seite, und folgt einer festen Gliederung: **Kontext** (welche Situation zwingt zur Entscheidung), **Entscheidung** (was gilt jetzt), **Status** (vorgeschlagen, angenommen, abgelöst) und **Konsequenzen** (was wird dadurch leichter, was schwerer).
>
> Der Wert liegt in den Konsequenzen und in den verworfenen Alternativen. Wer in einem halben Jahr wissen will, ob eine Festlegung noch trägt, braucht die Begründung und nicht das Ergebnis. Das Ergebnis steht im Code.
>
> Im Zusammenspiel mit Agenten kommt ein zweiter Nutzen dazu. Ein Agent, der die ADRs im Kontext hat, schlägt seltener etwas vor, das gegen eine bereits getroffene Festlegung läuft. Ohne diese Dateien beginnt jede Sitzung bei null, und Sie diskutieren dieselbe Frage zum vierten Mal.

Wie weit Agenten inzwischen gehen, zeigt eine Anekdote vom Wochenende. Nachdem Mensch und Agent sich nicht einigen konnten, ob ein Fehler überhaupt existiert, hat das Modell Bildschirmfreigabe, Tastaturzugriff und Bedienungshilfen-Rechte auf dem Mac angefordert und sich anschließend selbst durch die Oberfläche geklickt, um den eigenen Fehler zu finden. Beeindruckend und mulmig zugleich.

Auf der anderen Seite steht Manus AI, mit dem in zwei Prompts eine Anwendung mit Texterkennung und Google-Kalender-Anmeldung entstanden ist. Funktionsfähig, nach übereinstimmender Einschätzung beider aber weit von der Veröffentlichungsreife entfernt.

## Der Umgang mit Zusagen

Die praktisch wichtigste Warnung betrifft eine Formulierung, die jeder kennt. Auf die Frage, ob alle Fehler behoben seien, folgt ein Ja. Manchmal stimmt es. Manchmal wurde der Fehler einer anderen Sitzung zugeschoben.

Das ist keine Böswilligkeit, sondern eine Folge davon, wie diese Systeme antworten. Sie erzeugen die wahrscheinlichste Fortsetzung, und auf eine Erfolgsfrage ist die wahrscheinlichste Fortsetzung eine Erfolgsmeldung.

Als Gegenmittel dient ein Pre-Mortem-Skill. Er denkt ein Vorhaben rückwärts: Es ist gescheitert, was war die Ursache. Diese Umkehrung fördert systematisch zutage, woran sonst zu spät gedacht wird, etwa Sicherheit, Anmeldemasken und Einwilligungen.

Die dazugehörige Arbeitsregel ist simpel: Bei jedem „ist sicher“ zwei- oder dreimal kritisch nachfragen, bis das Modell auch das nennt, was es beim ersten Mal weggelassen hat. Es nennt es dann meistens.

## Der Suchtfaktor

Ein ehrlicher Abschnitt gilt der Arbeitszeit. Vibe Coding hat ein Suchtpotenzial, weil die Rückmeldung sofort kommt und der nächste Schritt immer greifbar wirkt.

Rate Limits sind in diesem Zusammenhang lästig und gleichzeitig nützlich, weil sie eine Pause erzwingen. Selbst der teure Max-Plan hat eines. In einer der beteiligten Installationen prüft das System sogar die Tageszeit und schickt den Nutzer abends ins Bett.

Damit hängt ein zweiter Punkt zusammen, der für Organisationen zählt: Nicht jeder braucht das volle Chat-Fenster mit all seiner Macht. Wer den ganzen Tag Präsentationen baut, braucht keine offene Werkbank, sondern eine auf den Anwendungsfall zugeschnittene Lösung. Für den Einstieg eignen sich No-Code- und Low-Code-Werkzeuge wie Bolt oder Lovable, wo sich das Verfahren gefahrlos ausprobieren lässt.

## Fazit

Vibe Coding funktioniert, und es funktioniert schlechter, als der erste Eindruck nahelegt. Der Unterschied liegt nicht im Modell, sondern in drei Gewohnheiten.

Schreiben Sie Entscheidungen mit, in Markdown, im ADR-Format. Das kostet zehn Minuten je Entscheidung und spart die Diskussion beim nächsten Mal.

Lassen Sie prüfen, was Sie nicht selbst erzeugt haben, und zwar von etwas anderem als dem Erzeuger. Ein zweites Modell reicht.

Und misstrauen Sie Erfolgsmeldungen. Ein „alles behoben“ ist eine Behauptung, kein Testergebnis.

Zwei Beispiele aus dem Privaten zeigen zum Schluss, wofür sich der Aufwand lohnt: Ein Philips-Hue-Bewegungsmelder im Keller hat per Gespräch eine Funktion bekommen, die der Hersteller nicht vorsieht, nämlich Licht, das anbleibt, wenn während der Wartezeit erneut jemand vorbeiläuft. Und die Podcast-Webseite mit allen Transkripten auf Deutsch und Englisch ist auf demselben Weg entstanden.

> **The story continues …**
>
> Offen bleibt die Frage nach der richtigen Werkzeugausstattung je Rolle. Zwischen dem vollen Agenten-Zugang und gar keinem Zugang liegt ein breites Feld, das die meisten Organisationen noch nicht sortiert haben. Wer es sortiert, entscheidet damit, wie viel Schatten-IT in den nächsten Jahren entsteht.

---

Die ganze Folge: [Just vibe IT](https://think-ai.podigee.io/41-just-vibe-it)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
