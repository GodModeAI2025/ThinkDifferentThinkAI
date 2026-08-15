---
folge: 37
titel: "Skill Engineering: Warum das System um das Modell herum entscheidet"
bildtitel: "Nicht der Bohrer, das Loch"
kicker: "Im Gespräch mit Dr. René Deist"
podigee: "https://think-ai.podigee.io/37-das-strategische-gold"
---

# Skill Engineering: Warum das System um das Modell herum entscheidet

*Die reine Modellleistung sättigt, wie einst das Megapixel-Rennen bei Digitalkameras. Was danach zählt, ist die Konstruktion drumherum. Dr. René Deist über Skills, das Führungsparadox und den Skill, mit dem chinesische Mitarbeitende ihr Wissen zurückhalten.*

Von Mark Zimmermann

Die These der Folge fällt in den ersten Minuten und trägt den Rest: Prompt Engineering ist gestern, Skill Engineering ist morgen. Und zwar für Agenten wie für ganze Organisationen.

Zu Gast ist Dr. René Deist, der allererste Gast des Podcasts, mit dem vor Monaten das IOC-Modell aus Intent, Operate und Control diskutiert wurde.

> **kurz & knapp**
>
> - Ein Skill ist mehr als ein guter Prompt: Werkzeugzugriff, ausführbarer Code und beständiger Speicher
> - Skills sind modellagnostisch und überleben damit einen Anbieterwechsel
> - Die Modellleistung sättigt, wie das Megapixel-Rennen bei Digitalkameras
> - Mehr Automatisierung erzeugt mehr Führungsbedarf, nicht weniger
> - In China filtern Mitarbeitende ihr Wissen per Anti-Distillation Skill aus abzugebenden Dateien

## Was ein Skill von einem Prompt unterscheidet

Deists Definition ist präziser als die verbreitete. Ein Skill ist orchestrierter Zugriff auf Werkzeuge, ausführbarer Code mitten in der Markdown-Datei, bis hin zu Python-Ausschnitten, und dauerhafte Speichereinheiten. Und er ist modellagnostisch: Derselbe Skill läuft wahlweise mit Modellen verschiedener Anbieter.

Diese letzte Eigenschaft ist die wirtschaftlich wichtigste. Ein Prompt ist auf ein Modell hin optimiert und verliert beim Wechsel seinen Wert. Ein Skill beschreibt die Aufgabe und überlässt die Ausführung dem jeweils angebundenen Modell.

Als Einordnung dient eine Analogie aus der Digitalkamera-Ära. Irgendwann war das Megapixel-Rennen entschieden, weil zusätzliche Auflösung keinen sichtbaren Unterschied mehr machte. Danach entschied das System: Objektiv, Bildverarbeitung, Bedienung. Bei Sprachmodellen ist derselbe Punkt in Sicht.

Sehr konkret wird das an einem eigenen Skill, den Deist beschreibt: Er durchforstet alte GitHub-Repositories, überführt brauchbaren Code in eigenständige Skills und lässt den Rest als Python weiterlaufen. Mit Verweis auf Andrej Karpathy wird der Gedanke weitergesponnen: Statt ganzer Legacy-Codebasen forkt man künftig nur noch die Markdown-Datei mit der eigentlichen Idee.

> ### Jobs to be done, angewandt auf Software
>
> Die Denkfigur stammt aus der Innovationsforschung und lautet verkürzt: Niemand will einen Bohrer, alle wollen ein Loch in der Wand.
>
> Auf Software übertragen heißt das: Der Wert liegt nicht in der Implementierung, sondern in dem, was sie leistet. Solange Implementierung teuer war, fielen beide zusammen, weil der Code das einzige Mittel zum Zweck war. Sinkt der Preis für Implementierung, trennen sich die beiden.
>
> Praktisch bedeutet das, den eigenen Bestand anders zu bewerten. Eine gewachsene Codebasis ist wertvoll, soweit sie Wissen über die Domäne enthält, das nirgends sonst steht. Sie ist wertlos, soweit sie nur eine bekannte Aufgabe auf eine bestimmte Weise löst. Die Kunst besteht darin, den ersten Teil herauszuschälen und aufzuschreiben, bevor jemand den zweiten wegwirft.

## Das Führungsparadox

Die zweite Hälfte trägt eine Beobachtung, die der Intuition widerspricht. Je mehr Geschäftsprozesse automatisiert werden, desto mehr Führung wird gebraucht, nicht weniger.

Der Grund liegt in den Rückkopplungsschleifen. Ein Bestand aus vielen Agenten erzeugt laufend Ergebnisse, die auf die nächsten Schritte wirken. Wer diese Schleifen nicht strategisch steuert, bekommt ein System, das effizient in eine Richtung läuft, die niemand gewählt hat.

Delegation wird damit zur Kernkompetenz. Die Analogie aus der Folge stammt vom autonomen Fahren: Das Lenkrad ganz herauszunehmen kann sicherer sein, als auf menschliches Eingreifen im Ernstfall zu hoffen. Ein halb aufmerksamer Mensch in einer Schleife ist häufig schlechter als eine klare Zuständigkeit.

Auf Organisationsebene wird es grundsätzlich. Deist zitiert Jack Dorsey mit der Warnung, heutige Organigramme nicht einfach in agentische Strukturen zu übersetzen. Die Pyramide sei tot, Herrschaftswissen verliere an Bedeutung. Das entspricht dem, was agile Methoden seit Jahren beabsichtigen und selten erreichen.

Beachten Sie den Zusammenhang zwischen beiden Aussagen. Weniger Hierarchie und mehr Führung sind kein Widerspruch, wenn man Führung als Richtungsgebung versteht statt als Weisungskette.

## Der Blick nach China

Der kritischste Abschnitt betrifft die Praxis in China, und er enthält das für Organisationen unbequemste Detail der Folge.

Kamera-Tracking in Fabriken dient dort dem Training von Robotik. Das ist bekannt. Interessanter ist ein Werkzeug namens Anti-Distillation Skill: Mitarbeitende filtern damit ihr wertvollstes Wissen aus Skill-Dateien heraus, bevor diese ans Management gehen.

Das ist die vorhersehbare Reaktion auf eine Anforderung, die viele Organisationen gerade formulieren. Wer Mitarbeitende auffordert, ihr Erfahrungswissen in maschinenlesbare Form zu bringen, verlangt von ihnen, ihre eigene Ersetzbarkeit zu erhöhen. Ohne eine Antwort darauf, was sie im Gegenzug bekommen, ist Zurückhaltung die rationale Wahl.

Parallel dazu gibt es in chinesischen Städten Installationsdienste für OpenClaw als Kiosk-Angebot, während hierzulande eher gezögert und reguliert wird.

## Programmieren als Grundfertigkeit

Zum Ausklang plädieren beide dafür, Terminal- und Programmiergrundwissen als Life Skill zu begreifen. Nicht in dem Sinne, dass jeder selbst installieren oder entwickeln muss. In dem Sinne, dass ein Grundverständnis Souveränität schafft.

Das ist praktisch relevant für Weiterbildungsprogramme. Wer Anwendungsschulungen anbietet, vermittelt den Umgang mit einem Werkzeug, das es in zwei Jahren anders gibt. Wer vermittelt, was ein Token ist, was ein Kontextfenster leistet und warum ein Modell etwas behauptet, vermittelt etwas Haltbares.

## Fazit

Die Folge liefert eine brauchbare Prüffrage für jede KI-Investition: Was davon überlebt den nächsten Modellwechsel.

Prompts überleben ihn nicht. Skills überleben ihn, wenn sie modellagnostisch geschrieben sind. Die Kontextarchitektur überlebt ihn immer, weil sie beschreibt, welches Wissen wo liegt.

Für die Organisation kommt eine zweite Frage dazu, und sie ist die unbequemere: Was bekommen die Menschen dafür, dass sie ihr Erfahrungswissen aufschreiben. Wer darauf keine Antwort hat, bekommt Skills, in denen das Wichtige fehlt. Der Anti-Distillation Skill ist dafür nur die technisch ausgereifte Variante.

> **The story continues …**
>
> Wenn Herrschaftswissen tatsächlich an Bedeutung verliert, ändert das die Grundlage vieler Karrierewege. Wie Organisationen Beiträge künftig sichtbar machen und honorieren, wenn nicht mehr über exklusiven Wissenszugang, ist offen. Ohne eine Antwort darauf bleibt der Anti-Distillation Skill die naheliegende Reaktion.

---

Die ganze Folge: [Das strategische Gold](https://think-ai.podigee.io/37-das-strategische-gold)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
