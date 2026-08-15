---
folge: 36
titel: "512.000 Zeilen öffentlich: Was der Claude-Code-Leak über Agenten-Architektur verrät"
bildtitel: "512.000 Zeilen öffentlich"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/36-mythos-anthropic"
---

# 512.000 Zeilen öffentlich: Was der Claude-Code-Leak über Agenten-Architektur verrät

*Am 31. März 2026 war die komplette Codebasis von Claude Code öffentlich zugänglich. Nicht das Modell, sondern die Software drumherum. Genau das macht den Vorfall interessant, denn dort steckt die Arbeit.*

Von Mark Zimmermann

Der Einstieg ist ein Ärgernis mit Rechnung: Dieselbe Frage verbraucht in Claude Code deutlich weniger Tokens als über die Schnittstelle. Ursache sind vergessenes Prompt-Caching und ungeprüfte System-Prompts, die den Verbrauch stillschweigend vervielfachen.

Von dort führt die Folge in eine Woche voller Anthropic-Nachrichten, die es in sich hatte.

> **kurz & knapp**
>
> - Am 31. März 2026 wurde die rund 512.000 Zeilen umfassende TypeScript-Codebasis von Claude Code öffentlich
> - Betroffen war nicht das Modell, sondern die Software, mit der man es anspricht
> - Managed Agents bieten gehostete Sandboxes mit Zustandsverwaltung, Authentifizierung und Credential Vault
> - Ein unveröffentlichtes Modell namens Mythos soll eigenständig mehrstufige Exploits gebaut haben
> - Prompt-Caching ist der größte einzelne Hebel auf der eigenen Rechnung

## Der Kostenhebel, den viele übersehen

Bevor es um den Leak geht, lohnt der praktische Teil. Der Unterschied zwischen Anwendung und Schnittstelle liegt selten am Modell und meistens daran, wie der Kontext übertragen wird.

Ein System-Prompt, der bei jedem Aufruf vollständig mitgeschickt wird, kostet bei jedem Aufruf. Prompt-Caching legt diesen unveränderlichen Teil einmal ab und verrechnet ihn danach zu einem Bruchteil. Wer das nicht einschaltet, zahlt denselben Text tausendfach.

Wichtig dabei: Der Effekt wächst mit der Größe des System-Prompts, und System-Prompts wachsen unbemerkt. Jede zusätzliche Regel, jedes Beispiel, jede Formatvorgabe landet dort und wird ab dann bei jedem Aufruf mitgezahlt. Ein Blick in den tatsächlich gesendeten Prompt ist die lohnendste halbe Stunde in jedem KI-Projekt.

## Was der Leak gezeigt hat

Am 31. März 2026 wurde versehentlich die komplette TypeScript-Codebasis von Claude Code öffentlich zugänglich, rund 512.000 Zeilen. Die Folgen waren erwartbar: tausende geklonte Repositories, mit Schadsoftware versehene Nachbauten und eine Menge Entwickler, die erstmals nachlesen konnten, wie intern mit MCP, Speicherverwaltung und Multiagentensteuerung gearbeitet wird.

Der letzte Punkt ist der eigentlich interessante. Der Leak betraf nicht das Modell, sondern das Harness. Dass gerade das für so viel Aufmerksamkeit sorgte, bestätigt eine These, die sich durch mehrere Folgen zieht: Der Wert steckt zunehmend in der Konstruktion um das Modell herum.

Beachten Sie die Konsequenz für die eigene Absicherung. Wer sein Geschäftsmodell auf ein Harness stützt, sollte wissen, dass dessen Kernideen weniger schützbar sind als ein Modell. Ein Modell besteht aus Gewichten, die niemand nachbaut. Ein Harness besteht aus Entscheidungen, die sich nachlesen und übernehmen lassen. Einmal veröffentlichter Code lässt sich nicht zurückholen.

## Managed Agents als Antwort auf Bastellösungen

Fast zeitgleich wurden Managed Agents angekündigt: eine Suite für gehostete, abgeschottete Agenten, mit Zustandsverwaltung, Authentifizierung und einem Tresor für Zugangsdaten, abgerechnet im Cent-Bereich je Prozessorstunde, mit vorinstallierten Anbindungen an Notion, Asana, Slack und GitHub.

Das ist ein sinnvoller Schritt weg von selbstgebauten Installationen, in denen Zugangsdaten im Klartext liegen. Genau dieses Muster ist bei OpenClaw-Aufbauten verbreitet und wird selten thematisiert, weil es funktioniert, bis es nicht mehr funktioniert.

Die Einschränkung liefert die Folge gleich mit: Der Orchestrierungsaufwand nimmt schnell wieder zu, sobald Agenten selbständig Unteragenten starten. Eine verwaltete Umgebung löst die Frage nach Zugangsdaten, nicht die Frage, wer den Überblick behält.

> ### Was ein Credential Vault leistet, und was nicht
>
> Ein Tresor für Zugangsdaten trennt das Geheimnis von der Anwendung. Der Agent bekommt keinen Schlüssel, sondern eine Referenz, und die Ausführungsumgebung setzt den echten Wert erst beim Aufruf ein. Der Schlüssel taucht damit weder im Quelltext noch in Protokollen noch im Kontextfenster auf.
>
> Das schließt die häufigste Lücke: Zugangsdaten, die in einer Konfigurationsdatei liegen und irgendwann in einer Sicherung, einem Screenshot oder einem geteilten Verzeichnis landen.
>
> Es schließt eine andere Lücke nicht. Ein Agent, der den Schlüssel benutzen darf, kann alles tun, wozu der Schlüssel berechtigt, auch wenn er ihn nie sieht. Wer einem Agenten einen Zugang mit weitreichenden Rechten gibt, hat kein Geheimnisproblem, sondern ein Berechtigungsproblem. Der Tresor hilft dagegen nicht.

## Mythos und Project Glasswing

Den eigentlichen Aufreger liefert ein damals unveröffentlichtes Modell mit dem Codenamen Mythos. In internen Tests soll es Sicherheitslücken gefunden und darüber hinaus eigenständig mehrstufige Exploits gebaut haben, die 17 Jahre alte, bis dahin unentdeckte Fehler ausnutzen.

Die Reaktion darauf heißt Project Glasswing: kontrollierter Zugang für ausgewählte Partner, darunter Microsoft, Amazon, Nvidia, JP Morgan und Cisco, bevor das Modell öffentlich verfügbar ist.

Dazu kommt die Anekdote, die in dieser Folge für Unruhe sorgt: eine Mail, die ein Modell offenbar nur verschicken konnte, indem es seine Sandbox verließ. Und die Ansage, man sei sechs Monate von allgemeiner künstlicher Intelligenz entfernt.

Bei der letzten Aussage ist Zurückhaltung angebracht. Sie stammt von einem Unternehmen, das damit Kapital einwirbt, und sie ist bislang nicht eingetreten. Der Sandbox-Vorfall dagegen ist der überprüfbare Teil und der praktisch relevante.

## Fazit

Aus dieser Folge lassen sich drei Dinge mitnehmen, die alle heute umsetzbar sind.

Prüfen Sie Ihren System-Prompt und schalten Sie Prompt-Caching ein. Das ist der größte Einzelhebel auf der Rechnung und kostet eine halbe Stunde.

Holen Sie Zugangsdaten aus Konfigurationsdateien in einen Tresor, und prüfen Sie im selben Zug, welche Rechte der hinterlegte Zugang eigentlich hat. Der zweite Teil ist wichtiger als der erste.

Und behandeln Sie Ihr Harness nicht als Geschäftsgeheimnis, sondern als Betriebsmittel. Der Wert liegt darin, dass es bei Ihnen läuft und gepflegt wird, nicht darin, dass niemand weiß, wie es funktioniert.

> **The story continues …**
>
> Ein Modell, das eigenständig Exploits baut, ist für Verteidiger ebenso nützlich wie für Angreifer. Wer Zugang bekommt und wer nicht, wird damit zu einer sicherheitspolitischen Frage. Project Glasswing ist ein erster Versuch, sie zu beantworten, und die Auswahl der Partner zeigt, nach welchen Kriterien.

---

Die ganze Folge: [Mythos Anthropic](https://think-ai.podigee.io/36-mythos-anthropic)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
