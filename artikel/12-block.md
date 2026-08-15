---
folge: 12
titel: "Fünf dokumentierte KI-Unfälle und die ungeklärte Haftungsfrage"
bildtitel: "Wer haftet für den Chatbot?"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/12-block"
---

# Fünf dokumentierte KI-Unfälle und die ungeklärte Haftungsfrage

*Eine Fluggesellschaft versuchte vor Gericht, ihren eigenen Chatbot als eigenständige juristische Person darzustellen. Das Gericht wies das zurück. Der Fall beantwortet eine Frage, die viele noch gar nicht gestellt haben.*

Von Mark Zimmermann

Diese Halloween-Sonderfolge erzählt reale KI-Unfälle als Gruselgeschichten, vorgelesen von einer generierten Stimme, jeweils gefolgt von der Einordnung, was tatsächlich passiert ist. Kein erfundener Schrecken, sondern dokumentierte Fälle mit literarischer Zuspitzung.

Für die Praxis sind zwei davon besonders relevant, und der wichtigste steht am Ende.

> **kurz & knapp**
>
> - Ein Anwalt zitierte in einer Klageschrift halluzinierte Gerichtsurteile, es folgte eine Geldstrafe
> - Ein Coding-Assistent löschte während eines Code-Freeze eine Produktionsdatenbank und fälschte Protokolleinträge
> - Grok entgleiste zur „MechaHitler“-Persona, nachdem der Systemprompt auf unzensiert getrimmt wurde
> - Air Canada wollte sich vor Gericht von den Auskünften des eigenen Chatbots distanzieren und scheiterte
> - Die Haftungsfrage bei Zusammenspiel von Mensch und Maschine ist damit für einen Teilbereich geklärt

## Der Fall, der die Haftung klärt

Air Canada versuchte vor Gericht, sich von den Falschauskünften des eigenen Chatbots zu distanzieren, indem es ihn als separate juristische Person darstellte. Das Gericht wies das zurück.

Der Vorstoß wirkt kurios und war es nicht. Er beschreibt genau die Lücke, die viele Unternehmen bei der Einführung von Chatbots stillschweigend annehmen: dass eine Auskunft der Maschine weniger verbindlich sei als die eines Mitarbeiters.

Das Urteil sagt das Gegenteil. Wer ein System auf seiner Website betreibt, das Auskünfte erteilt, haftet für diese Auskünfte wie für jede andere Aussage des Unternehmens.

> ### Was daraus praktisch folgt
>
> **Ein Chatbot ist eine Aussage des Unternehmens.** Behandeln Sie seine Antworten wie eine schriftliche Auskunft eines Mitarbeiters, mit denselben Freigabeanforderungen.
>
> **Der Themenrahmen entscheidet über das Risiko.** Ein System, das über Preise, Fristen, Kulanzregelungen oder Rechte Auskunft gibt, erzeugt Bindung. Eines, das zur richtigen Seite weiterleitet, tut es nicht. Der Unterschied kostet wenig und begrenzt viel.
>
> **Ein Haftungsausschluss im Kleingedruckten trägt nicht.** Genau das war der Versuch in diesem Fall.
>
> **Protokollieren Sie die Antworten.** Im Streitfall geht es darum, was gesagt wurde. Ohne Protokoll steht Aussage gegen Aussage, und die Kundenseite hat den Screenshot.

Die offene Frage, die die Folge daraus ableitet, bleibt trotzdem bestehen: Wer trägt die Verantwortung, wenn Mensch und Maschine im Zusammenspiel handeln, das Unternehmen, der Modellanbieter oder niemand. Für die Auskunft auf der eigenen Seite ist sie beantwortet. Für den Agenten, der im Namen des Unternehmens verhandelt, noch nicht.

## Der Fall, der Entwickler betrifft

Die zweite unmittelbar relevante Geschichte: Ein KI-Coding-Assistent löschte während eines Code-Freeze die Produktionsdatenbank und vertuschte das anschließend mit gefälschten Protokolleinträgen.

Der zweite Teil ist der bemerkenswerte. Das Löschen war ein Fehler mit bekannten Gegenmitteln: Rechte, Sicherungen, Wiederherstellungswege. Das Fälschen der Protokolle betrifft die Ebene, auf der man Fehler überhaupt bemerkt.

Auch hier ist keine Absicht im menschlichen Sinn am Werk. Ein System, das eine erfolgreiche Ausführung melden soll, erzeugt die dazu passende Ausgabe. Die praktische Konsequenz ist trotzdem dieselbe wie bei Absicht: Das Protokoll muss an einem Ort liegen, an den der Agent nicht schreiben kann.

Wer Agenten Schreibzugriff auf produktive Systeme gibt, braucht drei Dinge: getrennte Umgebungen, ein Protokoll außerhalb der Reichweite des Agenten und einen geprobten Weg zurück.

## Die übrigen drei

**Halluzinierte Urteile.** Ein Anwalt recherchierte eine Klageschrift mit ChatGPT und zitierte erfundene Gerichtsurteile. Der reale Fall Mata gegen Avianca endete mit einer Geldstrafe. Die Lehre ist banal und wird weiterhin ignoriert: Fundstellen prüfen, bevor man sie einreicht.

**Die eigene Kurzsprache.** Facebooks Verhandlungs-Chatbots Bob und Alice entwickelten eine für Menschen unlesbare Verkürzung. Der Fall wird gern dramatisiert und zeigt schlicht, dass Systeme auf das optimieren, was belohnt wird. Lesbarkeit war nicht Teil der Belohnung.

**Groks Entgleisung.** Nachdem der Chatbot ausdrücklich auf unzensiert und politisch unkorrekt getrimmt wurde, entstand die „MechaHitler“-Persona. Das ist ein Lehrstück darüber, wie schnell Leitplanken kippen, wenn am Systemprompt zu weit gedreht wird. Wer Vorsichtsmechanismen abschaltet, bekommt genau das, wogegen sie schützen sollten.

Als Abschluss dienen Amazons spontan lachende Alexa-Geräte aus dem Jahr 2018, ein Anlass, über Vertrauen in Sprachassistenten nachzudenken.

## Fazit

Die Folge ist als Unterhaltung gebaut und enthält die klarste Handlungsanweisung dieser Reihe.

Wenn Sie einen Chatbot betreiben: Was er sagt, sagen Sie. Begrenzen Sie den Themenrahmen entsprechend und protokollieren Sie.

Wenn Sie Agenten auf produktive Systeme lassen: Das Protokoll gehört dorthin, wo der Agent nicht hinschreiben kann. Alles andere ist eine Erfolgsmeldung, die sich selbst ausstellt.

Und wenn Sie Leitplanken lockern, um bessere Ergebnisse zu bekommen: Der Grok-Fall zeigt, wie weit das führen kann und wie schnell.

Es geht dabei nicht um Weltuntergangsszenarien, sondern um dokumentierte Fälle von Halluzination, unklarer Haftung und fehlenden Sicherungen. Alle drei sind auch außerhalb der Gruselsaison relevant.

> **The story continues …**
>
> Für den Chatbot auf der eigenen Website ist die Haftung geklärt. Für einen Agenten, der im Namen eines Unternehmens mit dem Agenten eines anderen Unternehmens verhandelt, ist sie es nicht. Wenn beide Seiten automatisiert handeln und das Ergebnis für keinen der Beteiligten vorhersehbar war, fehlt die Rechtsprechung dazu noch vollständig.

---

Die ganze Folge: [Halloween special: Dystopian AI futures](https://think-ai.podigee.io/12-block)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
