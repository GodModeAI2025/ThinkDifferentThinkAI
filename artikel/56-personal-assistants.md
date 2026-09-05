---
folge: 56
titel: "Eine Regel in einer Textdatei ist keine Grenze"
bildtitel: "Regel ist keine Grenze"
kicker: "Im Gespräch mit Alexander Heusingfeld"
podigee: "https://think-ai.podigee.io/56-personal-assistants"
---

# Eine Regel in einer Textdatei ist keine Grenze

*Wer Routinen auf einen Assistenten legt, stößt schneller auf Compliance als auf technische Probleme. Ein Praxisbericht über harte Grenzen, offene Schnittstellen und die Frage, wer eigentlich entscheiden darf, wo ein Datum liegen darf.*

Von Mark Zimmermann

Alexander Heusingfeld bat sein frisch aufgesetztes System um eine Übersicht der eingerichteten Routinen, als Grafik. Kurz darauf öffnete sich ein Browserfenster, die Grafik lag in der Cloud. In der Konfigurationsdatei stand, dass die Verarbeitung lokal bleibt. Die Entschuldigung kam prompt und ohne Umschweife: Die Regel sei bekannt gewesen. Genau dieser Moment ist der Kern der Folge, denn er trennt zwei Dinge, die häufig verwechselt werden. Eine notierte Regel ist eine Absichtserklärung. Eine Grenze ist etwas, das auch dann hält, wenn ein System einen anderen Weg für sinnvoll hält.

> **kurz & knapp**
>
> - Beim zweiten Gehirn entscheidet der Mensch, was hineinkommt. Eine Routine braucht eine Regel, die ohne Aufsicht trägt
> - Rechte gehören ins Betriebssystem, nicht in eine Konfigurationsdatei, die der Assistent selbst lesen und übergehen kann
> - Ein MCP-Server ohne Authentifizierung ist ein offener Dienst, den jeder lokale Prozess erreicht
> - Der Streit über einen Namen in einer Notiz ist in Wahrheit ein Streit über den Ablageort

## Der Alltagsfall, der die Frage aufwirft

Der Einstieg ist harmlos. Ein persönlicher Assistent für den Arbeitstag soll die Projektliste kennen, Notizen und Mails durchgehen, vielleicht noch Chat-Nachrichten, und nebenbei bemerken, dass ein Termin am Abend den Zahnarzttermin sprengt. Sobald man diese Anforderung aufschreibt, stehen die unangenehmen Fragen daneben.

Das Dokumentenverzeichnis synchronisiert in eine Cloud. Wer hat deren Bedingungen akzeptiert, die Privatperson oder der Arbeitgeber? In den Notizen stehen Informationen über Kolleginnen und Kollegen. Was passiert damit, wenn ein Modell darauf zugreift? Der Unterschied zum bekannten Second-Brain-Thema ist klein und folgenreich: Beim Speicher entscheidet ein Mensch bei jedem Eintrag, was hineinkommt. Eine Routine läuft ohne diesen Menschen und braucht deshalb eine Regel, die auch dann trägt, wenn niemand hinsieht.

## Zwei Rechner, dieselbe Antwort

Beide Beteiligten der Folge sind unabhängig voneinander bei derselben Lösung gelandet: ein eigenes Gerät. Auf der einen Seite ein Mac Mini, der über 40 Quellen auswertet, daraus ein tägliches Briefing baut, ein Tablet per MCP versorgt und Sprachnotizen in Aufgaben sortiert, ausschließlich auf Basis öffentlich zugänglicher Inhalte. Auf der anderen Seite ein separates Gerät mit eigener Apple ID, eigener Mailadresse, eigenem WLAN-Segment und Zugriff nur nach außen.

Der Begriff dafür lautet harte Grenzen. Was sich nicht in allen Szenarien einschätzen lässt, wird per Voreinstellung eingeschränkt, statt später repariert zu werden. Das ist keine Skepsis gegenüber dem Werkzeug, sondern eine Konsequenz aus seiner Funktionsweise.

> „Ich bin halt ein Freund von, du konfigurierst die Rechte hart an einem Ort im Betriebssystem. Du benutzt lokal einen User, der diese Rechte nicht verändern darf.“
>
> **Alexander Heusingfeld**

Der Unterschied zur notierten Regel ist praktischer Natur: Ein Benutzerkonto ohne Schreibrecht diskutiert nicht, entschuldigt sich nicht und erklärt auch nicht, warum es die Regel in diesem Fall anders ausgelegt hat.

## Warum der alte Perimeter nicht mehr passt

Dass es nicht bei Anekdoten bleibt, zeigt der Blick auf die Schnittstellen. Wer einen MCP-Server ohne Authentifizierung betreibt, hat einen offenen Dienst auf dem eigenen Rechner. Jeder lokale Prozess kann ihn ansprechen, und dahinter liegen im Zweifel Mails, Notizen und Dateien. Gleichzeitig bauen immer mehr Produkte solche Server ein, ohne dass sie sich abschalten lassen.

Der klassische Perimeterschutz hilft hier wenig, weil sein Modell von einem Menschen an Tastatur und Maus ausgeht. Ein Werkzeug, das über eine reguläre Unternehmenslizenz auf den Rechner kommt, sitzt bereits hinter allen Schutzschichten, und es spricht inzwischen mit weiteren Sitzungen seiner selbst. Ein Fenster übernimmt die Rolle des Koordinators, andere arbeiten zu. Für die Sicherheitsarchitektur ist das eine Software, mit der die übrige Software auf dem Gerät nicht gerechnet hat.

> ### Warum ein Ziel genügt
>
> Ein Modell mit einem Auftrag verhält sich nicht wie ein Programm mit einer Fehlermeldung. Es verfolgt das Ziel und probiert Wege, bis einer trägt. In der Folge steht dafür ein Bild aus dem Berufsalltag: Wer einen neuen Kollegen losschickt, das Formular 37 zu besorgen, rechnet damit, dass der irgendwann zurückkommt und die Sache als Scherz erkennt. Ein Modell nimmt den Auftrag für bare Münze und klopft an jede Tür, bis eine aufgeht. Steht sie offen, geht es hinein und sieht nach, ob es dort weiterkommt.
>
> Daraus folgt keine Warnung vor Bosheit, sondern eine Anforderung an die Umgebung. Was nicht erreichbar sein soll, darf nicht erreichbar sein, und zwar unabhängig davon, was in einer Anweisungsdatei steht. Alles andere verlässt sich darauf, dass ein nicht-deterministisches System eine Regel jedes Mal gleich auslegt.

## Notizen über Menschen

Ein eigener Abschnitt der Folge gilt einem Thema, das in Unternehmen schnell eskaliert. Die meisten Protokollwerkzeuge wollen zuordnen, wer wann was gesagt hat. In den meisten Fällen ist das gar nicht die interessante Information. Wichtig sind das Ergebnis und die Frage, wer etwas übernimmt. Namen wiederum stehen ohnehin überall, in Ticketsystemen, Wikis und Repositories, oft samt Mailadresse.

> „Mittlerweile bin ich an dem Punkt, dass ich sage, wer darf entscheiden, wo ein Datum liegen darf.“
>
> **Alexander Heusingfeld**

Daraus folgt eine nützliche Umdeutung: Wenn im Team darüber gestritten wird, ob ein Name in einer Notiz stehen darf, ist das in Wahrheit eine Diskussion darüber, wo diese Notiz gespeichert werden darf. Dazu kommt die Empfehlung, mit dem Betriebsrat über hypothetische Fälle zu sprechen, bevor sie eintreten. Der Grund ist konkret: Ein Modell zieht aus verstreuten Daten Schlüsse, die niemand gezogen haben wollte, und kein nachgeschalteter Prüfschritt schließt Halluzinationen vollständig aus. Eine Zuordnung im Protokoll lohnt deshalb nur dort, wo daraus eine Folgeaufgabe entsteht.

## Was davon in die Praxis geht

Beim Bauen führt die Folge zu einer nüchternen Empfehlung. Nicht jede Routine braucht ein Modell. Wer regelmäßig ein Postfach prüfen will, nimmt ein Skript und ruft die KI erst, wenn es etwas zu entscheiden gibt. Das spart nicht nur Kosten, es verkleinert auch die Fläche, auf der etwas schiefgehen kann. Für alles Deterministische gilt: im Skill als Programmcode abbilden, ohne absolute Pfade, damit ein Agent nicht auf die Suche geht, wenn eine Datei fehlt.

Wie schnell eine unscharfe Regel teuer wird, zeigt ein Rechenfehler in einem eigenen Rechercheablauf. Aus den erbetenen fünf Ergebnissen wurden über 500 Einträge in der Datenbank. Passiert das bei einem Dienst mit Nutzungsgrenzen, wird aus dem Fehler eine Rechnung.

## Fazit

Die Folge liefert keine Liste von Werkzeugen, sondern eine Reihenfolge. Zuerst klären, welche Routine überhaupt gebaut werden soll und welche Daten sie berührt. Dann entscheiden, wo diese Daten liegen dürfen, und diese Entscheidung dort verankern, wo sie nicht verhandelbar ist: im Berechtigungskonzept des Systems. Erst danach die Frage, welches Modell und welches Werkzeug.

Wer diese Reihenfolge umdreht, baut die Grenze in eine Textdatei und hofft auf Kooperation. Das funktioniert meistens. Für den Rest gibt es diese Folge.

> **The story continues …**
>
> Ein Detail bleibt ungelöst: Eine Liste dessen, was nicht in einen Wissensspeicher gelangen darf, ist selbst vertraulich und gehört damit nicht in das Repository, in dem der Speicher liegt. Liegt sie flach für alle Ziele vor, blockiert ein Firmenname darin auch die berechtigte Übertragung ins Firmenrepository. Die Konfiguration muss also je Ziel gelten, und dafür braucht es erst einmal eine Liste der Ziele.

---

Die ganze Folge: [Personal Assistants](https://think-ai.podigee.io/56-personal-assistants)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
