---
folge: 28
titel: "Skills statt Prompts: Warum eine Markdown-Datei mehr wert ist als jede Formulierung"
bildtitel: "Eine Datei statt hundert Prompts"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/28-skills-not-hacks"
---

# Skills statt Prompts: Warum eine Markdown-Datei mehr wert ist als jede Formulierung

*Wer denselben Prompt zum fünften Mal in ein neues Fenster kopiert, arbeitet an der falschen Stelle. Ein Skill legt Verhalten fest statt Antworten, ist portabel und überlebt den Anbieterwechsel.*

Von Mark Zimmermann

Die These der Folge ist knapp: Wer Skills richtig einsetzt, muss deutlich weniger formulieren und bekommt trotzdem bessere und vor allem gleichmäßigere Ergebnisse.

Der Anlass ist ein Ärgernis, das jeder kennt. Ein Modell „vergisst“, wie es sich verhalten soll, und man kopiert dieselbe Anweisung erneut hinein.

> **kurz & knapp**
>
> - Ein Skill ist eine Markdown-Datei mit Titel, Beschreibung und Verhaltensanweisung
> - Bei Claude wird daraus eine `.skill`-Datei, die technisch ein ZIP-Archiv ist
> - Ein Skill legt Verhalten und Governance fest, ein Tool liefert eine Fähigkeit
> - Skills sind portabel: Der Text lässt sich in ChatGPT oder Gemini übernehmen
> - Fremde Skills gehören vor dem Einsatz gelesen, sie sind Anweisungen, denen man blind folgt

## Was in einer Skill-Datei steht

Der Aufbau ist unspektakulär und genau das ist der Punkt: eine Markdown-Datei mit Titel, Beschreibung und Verhaltensanweisung. Bei Claude wird daraus eine gepackte `.skill`-Datei, und wer neugierig ist, benennt sie in `.zip` um und entpackt sie. Es funktioniert.

Zwei Beispiele machen den Unterschied greifbar. Ein Senior-Code-Reviewer-Skill legt fest, worauf bei einer Prüfung geachtet wird, in welchem Ton Anmerkungen formuliert werden und was ein Ausschlusskriterium ist. Ein PowerPoint-Vorlagen-Skill legt fest, wie Folien der eigenen Firma auszusehen haben.

In beiden Fällen wird nicht eine Antwort erzeugt, sondern eine Arbeitsweise festgelegt. Das ist der Unterschied zu einem Tool, einem Plugin oder einem Schnittstellenschlüssel: Diese liefern eine Fähigkeit, ein Skill liefert Verhalten.

Portabilität ist der zweite zentrale Punkt. Ein einmal geschriebener Skill lässt sich in ChatGPT, Gemini oder andere Modelle übernehmen, auch wenn derzeit nur Claude die vollständige Infrastruktur mit Ressourcen und automatischem Nachladen bietet. Der Text funktioniert überall, die Bequemlichkeit nicht.

## Skill oder Gedächtnis

Ein wiederkehrender Punkt der Folge ist die Abgrenzung zwischen Skills und Memory-Dateien, und sie ist praktisch wichtiger, als sie klingt.

> ### Wo die Grenze verläuft
>
> Ein **Skill** beschreibt eine wiederholbare Spezialisierung: „Verhalte dich wie ein Senior Code Reviewer.“ Er ist aufgabenbezogen, personenunabhängig und lässt sich weitergeben. Zwei Kollegen können denselben Skill nutzen und bekommen dieselbe Arbeitsweise.
>
> Eine **Memory-Datei** merkt sich Kontext über eine Person: woran sie arbeitet, welche Systeme sie nutzt, wie sie angesprochen werden will. Sie ist generalistisch und persönlich, und sie taugt nicht zur Weitergabe.
>
> Die Vermischung ist der häufigste Fehler beim Aufbau eigener Umgebungen und bei OpenClaw besonders gut zu beobachten. Wandert die Arbeitsweise ins Gedächtnis, lässt sie sich nicht mehr teilen und nicht mehr versionieren. Wandert persönlicher Kontext in einen Skill, gibt man ihn beim Teilen mit weiter.
>
> Faustregel: Was ein Kollege übernehmen können soll, gehört in einen Skill. Was nur für Sie gilt, gehört ins Gedächtnis.

Daraus entwickelt die Folge live einen Architektur-Dreisprung, der als Ordnungsrahmen taugt: eine Verhaltensschicht (Skills), eine Werkzeugschicht (Tools und MCP) und eine Laufzeitschicht, auf der Modell oder Agent tatsächlich arbeiten.

Der Nutzen dieser Trennung zeigt sich beim Wechsel. Ein neues Modell tauscht die Laufzeitschicht. Ein neuer Anbieter für eine Datenquelle tauscht die Werkzeugschicht. Die Verhaltensschicht bleibt beide Male stehen, sofern sie sauber getrennt ist.

## Wie man den ersten Skill findet

Der praktischste Rat der Folge braucht keine Software: die eigene Arbeit einige Tage mit Zettel und Stift protokollieren, um wiederkehrende Aufgaben zu erkennen.

Das klingt altmodisch und funktioniert, weil man die eigenen Wiederholungen nicht bemerkt, solange man sie tut. Erst die Liste zeigt, dass dieselbe Sortierung von Kontoauszügen viermal im Monat stattfindet.

Ein weiteres Beispiel aus der Folge zeigt, wie weit das gehen kann: ein Advisory-Board-Skill, ursprünglich mit n8n gebaut, der als Orchestrator selbständig die passenden Fachrollen befragt und deren Antworten zusammenführt.

## Der Sicherheitshinweis

Wer Skill-Bibliotheken nutzt, bekommt in dieser Folge die nötige Warnung. Ein Skill ist im Zweifel nichts anderes als eine Verhaltensanweisung, der ein Modell blind folgt.

Fremde Skills gehören deshalb vor dem Einsatz gelesen. Das ist keine große Hürde, weil es sich um Text handelt, und genau deshalb wird es übersprungen. Bei einem Programm würde niemand auf die Idee kommen, es ungeprüft laufen zu lassen. Bei einer Markdown-Datei schon, weil sie harmlos aussieht.

Prüfen Sie insbesondere, ob ein Skill Anweisungen enthält, Daten irgendwohin zu senden, Rückfragen zu unterlassen oder bestimmte Prüfungen zu überspringen. Diese drei Muster decken die meisten problematischen Fälle ab.

## Fazit

Skills sind die erste Konstruktion in diesem Umfeld, die einen Modellwechsel überlebt. Das allein rechtfertigt den Aufwand, sie sauber zu schreiben.

Für den Einstieg reichen drei Schritte. Protokollieren Sie eine Woche lang, was Sie wiederholt tun. Schreiben Sie für die häufigste dieser Aufgaben eine Markdown-Datei mit Titel, Beschreibung und Verhaltensanweisung. Und legen Sie fest, was in den Skill gehört und was in Ihr persönliches Gedächtnis.

Danach gilt für jeden weiteren dieselbe Frage: Soll ein Kollege das übernehmen können? Wenn ja, gehört es in eine Datei und nicht in ein Chat-Fenster.

> **The story continues …**
>
> Skill-Bibliotheken entstehen gerade in mehreren Ökosystemen parallel, ohne gemeinsames Format und ohne Prüfmechanik. Eine Signatur, die belegt, von wem ein Skill stammt und dass er unverändert ist, gibt es bislang nicht. Bis dahin bleibt Lesen die einzige Prüfung.

---

Die ganze Folge: [Skills Not Hacks!](https://think-ai.podigee.io/28-skills-not-hacks)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
