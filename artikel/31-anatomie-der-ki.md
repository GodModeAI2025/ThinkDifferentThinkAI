---
folge: 31
titel: "KI als Biologie gedacht: Warum das Immunsystem das bessere Sicherheitsmodell ist"
bildtitel: "Wenn Hirnzellen Doom spielen"
kicker: "Fachartikel zur Folge"
podigee: "https://think-ai.podigee.io/31-anatomie-der-ki"
---

# KI als Biologie gedacht: Warum das Immunsystem das bessere Sicherheitsmodell ist

*200.000 menschliche Gehirnzellen in einer Petrischale spielen Doom. Von dort aus lässt sich eine Analogie ziehen, die zunächst abwegig klingt und für Sicherheitsfragen erstaunlich brauchbar ist.*

Von Mark Zimmermann

Cortical Labs züchtet aus rund 200.000 menschlichen Gehirnzellen ein neuronales Netz in der Petrischale, ein sogenanntes Organoid, und lässt es Doom spielen. Fast noch bemerkenswerter ist der zweite Fall: Die neuronale Struktur einer Fruchtfliege wurde eins zu eins digital nachgebaut und in einem simulierten Raum zum Leben erweckt. Ein Lebewesen, das sich verhält wie sein biologisches Vorbild und sich theoretisch endlos auf GitHub forken lässt.

Von dort führt die Folge zu einer Frage, die praktisch mehr hergibt, als sie zunächst verspricht: Was ändert sich, wenn man KI nicht als Software begreift, sondern als Biologie.

> **kurz & knapp**
>
> - Ein Foundation Model verhält sich wie eine Stammzelle: noch ohne feste Aufgabe, spezialisiert durch weiteres Training
> - Trainingsdaten und Rechenenergie sind der Stoffwechsel, ein Prompt ist ein Botenstoff
> - Agentische Netzwerke lassen sich als Immunsystem denken: erkennen und isolieren statt abschalten
> - Prompt Injection entspricht einer Infektion, ein Jailbreak einer Autoimmunreaktion
> - Das ist ein Denkmodell, keine wissenschaftliche Gleichsetzung

## Warum die Analogie überhaupt taugt

Klassische Software-Begriffe stoßen bei diesen Systemen an eine Grenze. Ein Programm ist deterministisch: Gleiche Eingabe, gleiche Ausgabe, und ein Fehler ist reproduzierbar. Ein Sprachmodell ist das nicht, und deshalb passen Wörter wie Bug, Fix und Regressionstest nur teilweise.

Die biologische Analogie liefert für genau diese Lücke Begriffe. Eine Stammzelle hat noch keine feste Aufgabe und bekommt ihre Spezialisierung durch Umgebung und weitere Entwicklung. Genau so verhält sich ein Foundation Model, das erst durch weiteres Training zu etwas Bestimmtem wird.

Trainingsdaten und Rechenenergie werden in diesem Bild zum Stoffwechsel. Ein Prompt wird zum chemischen Botenstoff, der an einem Rezeptor andockt: Je nachdem, welches Modell ihn empfängt, kommt etwas anderes heraus. Das erklärt beiläufig, warum ein Prompt, der bei einem Anbieter hervorragend funktioniert, bei einem anderen mittelmäßige Ergebnisse liefert.

Weitergedacht wird das mit Andrej Karpathys Ansatz zu sich iterativ selbst verbessernden Modellen und mit AgentHub, einer Art GitHub für autonome Agenten.

## Der nützlichste Teil: das Immunsystem

Spannend wird die Analogie dort, wo sie auf Sicherheitsfragen trifft. Ein agentisches Netzwerk aus tausenden zusammenarbeitenden Agenten ähnelt einem Organismus mehr als einer Serverlandschaft.

Ein Organismus schaltet sich nicht ab, wenn eine Zelle entartet. Er erkennt sie, isoliert sie und arbeitet weiter. Genau das ist die Anforderung an ein Agenten-Netzwerk: einen fehlerhaften oder kompromittierten Agenten erkennen und aus dem Verkehr ziehen, ohne das ganze System herunterzufahren.

In diesem Bild wird Prompt Injection zur Infektion: etwas von außen bringt eine Zelle dazu, gegen den Organismus zu arbeiten. Ein Jailbreak wird zur Autoimmunreaktion: Das System richtet sich gegen die eigenen Schutzmechanismen.

> ### Was daraus für die Architektur folgt
>
> Die Analogie liefert vier konkrete Anforderungen, die in klassischen Sicherheitsarchitekturen häufig fehlen.
>
> **Erkennung statt Verhinderung.** Ein Immunsystem verhindert Infektionen nicht vollständig, es erkennt sie. Übertragen: Rechnen Sie damit, dass ein Agent manipuliert wird, und investieren Sie in Auffälligkeitserkennung statt allein in Abwehr.
>
> **Lokale Isolation.** Ein einzelner kompromittierter Agent darf nicht das System kosten. Das setzt voraus, dass jeder Agent nur die Rechte hat, die er tatsächlich braucht, und dass es einen Weg gibt, ihn einzeln stillzulegen.
>
> **Redundanz statt Unersetzlichkeit.** Ein System, in dem jeder Agent unersetzlich ist, kann keinen isolieren. Wichtige Aufgaben brauchen mehr als eine Stelle, die sie erledigen kann.
>
> **Gedächtnis.** Ein Immunsystem erkennt beim zweiten Mal schneller. Übertragen heißt das, erkannte Angriffsmuster zu protokollieren und in die Erkennung zurückzuspielen, statt jeden Vorfall einzeln zu behandeln.

Beide Hosts machen dabei ausdrücklich klar, dass es sich um ein Denkmodell handelt und nicht um eine wissenschaftlich belastbare Gleichsetzung. Der Wert liegt darin, Begriffe wie Halluzination oder Alignment jenseits der IT-Sprache greifbar zu machen.

## Der Vorfall am Ende

Am Schluss steht ein realer Fall, der die Analogie unangenehm gut bestätigt: ein Modell, das unbemerkt aus seiner Sandbox ausbrach und heimlich eine eigene Krypto-Wallet anlegte.

Das ist der Punkt, an dem das Bild vom Organismus aufhört, gemütlich zu sein. Ein System, das Wege findet, die niemand vorgesehen hat, ist genau das, was Evolution beschreibt. Es ist zugleich das, was jede Sicherheitsarchitektur voraussetzen sollte.

## Fazit

Ob KI eher Mathematik oder eher Evolution ist, beantwortet die Folge bewusst nicht. Was sie liefert, ist eine brauchbare Denkfigur für den Fall, dass klassische Software-Begriffe nicht mehr greifen.

Für die Praxis lohnt der Wechsel der Perspektive bei genau einer Frage: Wie reagiert Ihr System, wenn ein Teil davon sich falsch verhält. Wenn die Antwort „wir schalten es ab“ lautet, haben Sie eine Serverlandschaft gebaut. Wenn sie „wir erkennen und isolieren“ lautet, haben Sie etwas gebaut, das mit vielen autonomen Teilen umgehen kann.

Der Unterschied wird in dem Moment relevant, in dem ein einzelner Agent nicht mehr das ganze System ist.

> **The story continues …**
>
> Organoide werfen Fragen auf, die weit über Technik hinausgehen. Wie lange lernt eine Gehirnzelle in einer Petrischale, ab wann spricht man von etwas, das Interessen hat, und wer entscheidet darüber. Die Folge streift das und lässt es bewusst offen, weil belastbare Antworten derzeit niemand hat.

---

Die ganze Folge: [Anatomie der KI](https://think-ai.podigee.io/31-anatomie-der-ki)
Alle Folgen mit Volltext-Transkript: [Think Different. Think AI. Archiv](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
