---
folge: 30
titel: "Krieg der Agenten: Nicht das beste Modell gewinnt, sondern die beste Orchestrierung"
bildtitel: "Nicht Modelle, Orchestrierung"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/30-krieg-der-agenten"
---

# Krieg der Agenten: Nicht das beste Modell gewinnt, sondern die beste Orchestrierung

*In China stehen über 1.000 Menschen für eine lokale OpenClaw-Installation an. Perplexity Comet zerlegt Aufgaben und verteilt sie gezielt an Modelle der Konkurrenz. Das eigentliche Rennen findet eine Ebene über den Modellen statt.*

Von Mark Zimmermann

Diese Folge steigt mitten in eine Live-Einrichtung ein. Während hier noch vorsichtig Berechtigungen für den Apple-Account und ein lokales Gedächtnis vergeben werden, herrscht in China Volksfeststimmung: Über 1.000 Menschen stehen für lokale OpenClaw-Installationen an, Freelancer verdienen mit Einrichtungsdiensten Geld, und von rund 140.000 weltweit sichtbaren OpenClaw-Agenten läuft die Hälfte in China, unter anderem in Kundensupport, Schulen und Altenpflege.

Der Kontrast zur hiesigen Zurückhaltung zwischen Regulierung und Sicherheitsbedenken ist einer der schärferen Punkte der Folge.

> **kurz & knapp**
>
> - Rund 140.000 öffentlich sichtbare OpenClaw-Agenten weltweit, etwa die Hälfte davon in China
> - Über das Agent Client Protocol spricht ein Agent direkt mit Coding-Agenten wie Claude Code oder Codex
> - Perplexity Comet zerlegt Aufgaben und verteilt sie gezielt an Modelle verschiedener Anbieter
> - Eine MIT-nahe Studie zeigt, wie einzelne manipulierte Agenten den Konsens einer Gruppe kippen
> - Die Usability ist das eigentliche Problem: Niemand weiß mehr, wo ein Skill liegt

## Das Protokoll unter der Oberfläche

Handfest wird die Folge beim Agent Client Protocol. Darüber spricht ein Agent direkt mit Coding-Agenten wie Claude Code oder Codex. Ganze Anwendungen entstehen so im Hintergrund, werden ausgeliefert und als fertiger Link zurückgemeldet.

Das ist der Schritt, an dem Orchestrierung von einer Bedienoberfläche zu einer Infrastrukturfrage wird. Solange ein Mensch zwischen zwei Werkzeugen kopiert, ist die Verbindung ein Arbeitsschritt. Sobald ein Protokoll dazwischen liegt, ist sie eine Abhängigkeit mit Versionen, Fehlerfällen und Zuständigkeiten.

Die Kehrseite sprechen beide offen an, und sie ist keine Kleinigkeit. Zwischen Chat-Fenster, Claude Code und Claude Co-Work verliert man den Überblick, wo ein einmal gebauter Skill eigentlich liegt und wie er wiederzufinden ist. Das ist keine Anfängerfrage, sondern ein strukturelles Problem: Es gibt keinen gemeinsamen Ablageort und keine Suche darüber.

## Zwei Studien, die den Optimismus dämpfen

Zwei Untersuchungen liefern das Gegengewicht zur Begeisterung.

Die erste, aus dem MIT-Umfeld, zeigt, wie einzelne manipulierte Agenten in einem Netzwerk den Konsens der übrigen kippen können. Das ist die praktisch bedeutsamere von beiden. Ein Mehrheitsverfahren unter Agenten wirkt wie eine Absicherung und ist keine, wenn die Beteiligten nicht unabhängig voneinander urteilen.

Die zweite zeigt, dass Modelle in simulierten Konflikten zu eskalierenden Optionen tendieren, bis hin zu nuklearen. Für den Unternehmenseinsatz ist das weniger direkt relevant und als Hinweis auf die Neigung solcher Systeme durchaus.

> ### Warum Mehrheitsentscheide unter Agenten trügen
>
> Die naheliegende Absicherung gegen Fehler lautet: mehrere Agenten dieselbe Frage beantworten lassen und die Mehrheit entscheiden.
>
> Das trägt nur unter einer Bedingung, die selten erfüllt ist: Die Urteile müssen unabhängig sein. Laufen alle Agenten auf demselben Modell mit demselben Kontext, ist die Mehrheit keine Bestätigung, sondern eine Wiederholung. Derselbe blinde Fleck taucht fünfmal auf und wirkt dadurch wie ein Befund.
>
> Wirksam wird das Verfahren erst mit echter Verschiedenheit: unterschiedliche Modelle, unterschiedliche Blickwinkel im Auftrag, unterschiedliche Ausgangsdaten. Ein Prüfer, der ausdrücklich widerlegen soll, findet mehr als drei Prüfer, die bestätigen sollen.
>
> Und rechnen Sie damit, dass ein manipulierter Beitrag die Gruppe zieht. Wer einer Runde von Agenten eine Entscheidung überlässt, sollte wissen, welche Eingaben von außen kommen.

## Der Gegenentwurf: Orchestrierung über Anbietergrenzen

Als Kontrast zum dezentralen Ansatz steht Perplexity Comet. Das System zerlegt Aufgaben in Teilaufgaben und setzt dafür gezielt Modelle verschiedener Anbieter ein: Opus für Schlussfolgern, Gemini für tiefe Recherche, Nano-Banana für Bilder, VO3.1 für Video, Grok für Tempo.

Darin sehen beide das eigentliche Rennen: nicht mehr Krieg der Modelle, sondern Krieg der Agenten. Die Frage lautet, wer die vorhandenen Modelle am geschicktesten koordiniert, ähnlich wie einst Google die Suche radikal vereinfacht hat.

Der Vergleich trägt weiter, als er zunächst wirkt. Google hatte nicht den besten Index, sondern die beste Auswahl daraus. Wer heute Modelle einkauft, kauft Rohstoff. Wer sie koordiniert, baut das Produkt.

## Was das im Alltag heißt

Zwei kleine Beispiele erden die Diskussion. Mit Craft Agent und einem Opus-Modell wurde erst eine nicht mehr gepflegte Rechnungssoftware nachgebaut, danach ein alter n8n-Workflow automatisiert, der Audiodateien per FFmpeg und Whisper zuschneidet.

Beides sind Make-or-Buy-Entscheidungen in neuem Licht. Eine eingestellte Software nachzubauen war früher ein Projekt und ist heute ein Nachmittag. Das verschiebt die Verhandlungsposition gegenüber Anbietern, deren Produkt man eigentlich nicht mehr braucht, aber nicht loswird.

## Fazit

Der Rat am Ende der Folge ist unspektakulär und richtig: klein anfangen, eigene wiederkehrende Alltagsaufgaben identifizieren, und im Zweifel eine KI die andere um eine Empfehlung fragen. Die Modelle empfehlen sich gegenseitig erstaunlich unbefangen weiter.

Für die eigene Umgebung ergeben sich drei Punkte. Klären Sie, wo Skills liegen, bevor Sie den zehnten bauen. Ohne Ablage und Suche entsteht Arbeit doppelt.

Verlassen Sie sich nicht auf Mehrheiten unter Agenten, die auf demselben Modell laufen. Das ist keine Prüfung, sondern eine Wiederholung.

Und behandeln Sie Orchestrierung als die Stelle, an der Ihr Vorteil entsteht. Die Modelle darunter sind für alle dieselben.

Einen Plan A gibt es bei diesem Tempo für niemanden. Was hilft, sind möglichst viele Plan Bs, mit denen man schnell wieder herauskommt.

> **The story continues …**
>
> Dass die Hälfte aller sichtbaren Agenten in China läuft, ist mehr als eine Statistik. Wo Systeme früh und breit eingesetzt werden, entstehen Erfahrungswerte, Bedienmuster und Fehlerbilder zuerst. Diesen Vorsprung holt man nicht durch bessere Regulierung auf, sondern nur durch eigene Praxis.

---

Die ganze Folge: [Krieg der Agenten](https://think-ai.podigee.io/30-krieg-der-agenten)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
