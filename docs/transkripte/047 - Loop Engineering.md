---
title: "Loop Engineering"
episode_index: 47
published: "Sun, 05 Jul 2026 00:59:00 +0000"
duration: "2784"
page_url: "https://think-ai.podigee.io/47-loop-engineering"
image_url: "https://images.podigee-cdn.net/0x,sd1QFKk7Fz9KwWPl8Fy3WdvfRdh5LNdvp2jIEk-rsEH8=/https://main.podigee-cdn.net/uploads/u73317/cd1c2367-0bc1-4346-afdd-e4039aea950b.jpg"
audio_url: "https://audio.podigee-cdn.net/2527772-m-38fd8d3f5281b278360e205c1ef2d3e8.mp3?source=feed"
guid: "29519d809cd39170d59f0d9c3c211aca"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-07-06T10:28:37+00:00"
---

# Loop Engineering

**Veröffentlicht:** Sun, 05 Jul 2026 00:59:00 +0000
**Dauer:** 2784
**Webplayer:** https://think-ai.podigee.io/47-loop-engineering
**Cover:** https://images.podigee-cdn.net/0x,sd1QFKk7Fz9KwWPl8Fy3WdvfRdh5LNdvp2jIEk-rsEH8=/https://main.podigee-cdn.net/uploads/u73317/cd1c2367-0bc1-4346-afdd-e4039aea950b.jpg
**Audio:** https://audio.podigee-cdn.net/2527772-m-38fd8d3f5281b278360e205c1ef2d3e8.mp3?source=feed

## Beschreibung

Warum das Ziel wichtiger wird als der perfekte Prompt
Vor zwei, drei Jahren drehte sich alles um eine Frage: Wer schreibt den besten Prompt? Heute ist die eigentliche Frage laut Mark und Jens eine andere: Wer baut die beste Schleife, den besten Loop. Auslöser der Folge ist ein Zitat von Andrej Karpathy, der kürzlich öffentlich gemacht hat, dass Loop Engineering inzwischen wichtiger sei als Prompt Engineering. Mark zeichnet daraufhin seine eigene Entwicklung nach: von einer frühen Notion-Prompt-Datenbank ("Diskette war schon immer gut, wer will schon eine CD?") über Skills als Markdown-Dateien mit Sub-Skills und ausführbarem Python-Code bis zum eigentlichen Loop Engineering. Der Unterschied: Ein Loop bekommt kein einzelnes Kommando, sondern ein Ziel, klare Erfolgskriterien und die Anweisung, sich selbst so lange zu überprüfen und zu wiederholen, bis das Ziel erreicht ist.

Die praktische Warnung der Folge: Wer eine KI ihre eigene Arbeit prüfen lässt, bekommt oft nur Selbstbestätigung zurück. Mark und Jens plädieren deshalb dafür, das Ergebnis (das "Act") von einem anderen Modell checken zu lassen, statt von demselben System, das es erzeugt hat, denn ein System, das sich selbst belobigt, ist kein kritischer Beobachter. Als Beleg zitiert Mark einen Post von Peter Steinberger zu genau diesem Ansatz und dem dazugehörigen Tokenverbrauch. Darauf aufbauend ordnen die beiden aktuelle Funktionen wie Claude Codes Goal-, Loop- und Workflow-Modus ein, inklusive Marks eigenem Ablauf: erst planen, dann mit einem Kritiker- und einem Meta-Analyse-Skill gegenprüfen lassen, dann per Goal automatisiert umsetzen lassen, auch wenn das mal 10, 12 oder 20 Stunden dauert.

Ein wachsendes Thema in diesem Zusammenhang ist Harness Engineering. Je mehr Agenten und Loops parallel arbeiten, desto wichtiger werden Kontext und Memory (Stichwort "Second Brain", mit dem Beispiel der kurzfristigen Fable-Abschaltung als Warnung, wie schnell Kontext sonst verloren geht) sowie Governance-Fragen wie Auditierung und signierte Skills. Mark spinnt das Gedankenspiel humorvoll weiter zu einem "deutschen Behörden-Harness", der Bürokratie automatisiert und dadurch zum heimlichen Exportschlager werden könnte. Zum Abschluss grenzen die beiden Harness noch begrifflich von "Agentic OS" ab. Das Fazit der Folge: Es geht nicht darum, mit möglichst vielen Tokens zu beeindrucken, sondern ein klares Ziel zu definieren und der Maschine geduldig den Weg dorthin zu überlassen.

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** HDI zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:29]** Ich habe noch gar nicht gesehen, hast du es schon runtergezählt?

**[00:00:36]** Gott, wir sind schon live.

**[00:00:38]** Hallo, herzlich willkommen zu einer neuen Folge von Tink Different, Tink AI.

**[00:00:44]** Heute wollen Mark und ich mal über etwas reden, was ich, ich könnte es mal so formulieren,

**[00:00:51]** über die letzten Jahre angekündigt hat.

**[00:00:55]** Vor zwei, drei Jahren war die Frage noch ein bisschen, wer schreibt den besten Prompt, wie

**[00:01:01]** schreibe ich den besten Prompt?

**[00:01:03]** Heutzutage ist, glaube ich, eher die Frage, wenn man mal so schaut, was im Internet unter

**[00:01:08]** den AI-Gurus so diskutiert wird, also den Gurus neben Mark und mir.

**[00:01:13]** Hallo Mark, übrigens.

**[00:01:14]** Hallo Jens.

**[00:01:15]** Ist das komisch, wenn man sich selber Guru nennt, ich glaube schon.

**[00:01:18]** Aber egal, mache ich gerne.

**[00:01:20]** Bitte um Zuschriften an diese Seite.

**[00:01:24]** Heute zu Tage spricht man nicht mehr darüber, wer Ingeniert den besten prommt. Heute wird

**[00:01:31]** drüber gesprochen, wer Ingeniert die beste Schleife, den besten Loop. Wer kriegt es

**[00:01:37]** also hin, die Zusammenarbeit mit KIs so zu gestalten, dass die KIs möglichst ohne weiter

**[00:01:45]** nachzufragen sehr komplexe Aufgaben für jemanden erledigen kann. Erleben vielleicht auch,

**[00:01:53]** aber erledigen kann. Das ist heute das Thema von der heutigen Sendung, dass wir mal darüber reden

**[00:01:57]** vom Prom zum Loop Engineering und was das bedeutet und das betrachten wir heute in aller

**[00:02:04]** Tiefe, wie es von uns gewohnt seid, mit unserer Fachexpertise mit dem lieben Mark und der

**[00:02:14]** Mark, der darf jetzt auch gleich mal einsteigen und sagen, seit wann war dir eigentlich so klar,

**[00:02:21]** dass Prumtingenering vielleicht nicht das Ende der Fahnenstange sein wird, was das Thema KI betrifft?

**[00:02:30]** Das finde ich eine schöne Überleitung, wann einem das klar wurde. Hm, ich finde da tatsächlich,

**[00:02:37]** dass es gerade mit Blick auf Loops wieder einen neuen Fahrt aufnimmt, aber da würde ich ganz

**[00:02:44]** gerne erst mal irgendwie so ein bisschen drauf hin bleiben. Und nachdem du jetzt gesagt hast, dass

**[00:02:49]** ich hier so quasi so ein bisschen den Einstieg machen soll, freue ich mich sehr bei den leicht

**[00:02:55]** erhöhten Temperaturen, meinen Gehirn so weit durch zu lüften, dass es in der Lage ist,

**[00:03:00]** einen klaren Satz zu formulieren und nicht in eines inneres Stocken zu kommen. Das

**[00:03:06]** inneres Stocken ist auch eine schöne Überleitung, weil der innerste Loop, den so ein LLM hat,

**[00:03:11]** ist ja eigentlich der Loop erst mal über die Tokens. Also die Zerlegung von Text in kleine Häppchen.

**[00:03:18]** So nach dem Motto ist dann Wort drin, ist dann Buchstabe drin, sind da Silben drin. Wie treilt

**[00:03:22]** er denn die ganzen Worte in sich auf, um die zu verarbeiten? Da gab es ja auch vor einiger Zeit

**[00:03:28]** immer wieder mal so ein Aufschrei, so nach dem Motto Anthropic hat die Preise erhöht. Nein,

**[00:03:33]** hat den Tokenverbrauch erhöht. Ja nein, weil sie haben diesen Tokenis, also das Zerlegen

**[00:03:38]** in Tokens angepasst. Es ist aber so, mal egal ob du Guru sagst oder nicht, Tokenizer haben

**[00:03:45]** wir nach meinem Wissenstand noch nicht selbst, also verwendet ja, aber nicht selbst verändert

**[00:03:51]** oder beeinflusst. Und wenn nicht aktiv und unbewusst, wir sind ja eher eingestiegen beim

**[00:03:57]** Thema Prompt. Da schießt sich ein bisschen der Kreis von, hast du zum ersten Mal gemerkt,

**[00:04:01]** dass Prompt gar nicht so das Ende der Fahnenstange sind, das hat tatsächlich lange gedauert.

**[00:04:05]** Ich erinnere mich an ein Gespräch, wo ich Menschen immer gesagt habe,

**[00:04:08]** guck mal, du musst hier, wo ich mir so eine Promptdatenbank angelegt habe.

**[00:04:12]** Das war so die Zeit, wo ich mit Notion gearbeitet habe.

**[00:04:15]** Ich habe eine Promptdatenbank angelegt, du bist ein erfahrener Software Ingenieur,

**[00:04:19]** du machst dies, das und jenes.

**[00:04:21]** Und ich war auf meine Promptdatenbank ganz stolz.

**[00:04:25]** Die waren auch relativ lang und ich habe das sehr gerne und ausführlich gepflegt.

**[00:04:31]** Und ich erinnere mich, wie ich in der Firma war und Menschen von diesen

**[00:04:34]** normal nösen Skills gesprochen haben und ich dachte, das setze ich nicht durch.

**[00:04:38]** Ach, der neue modische Kram, das Kette war schon immer gut, der will schon eine CD.

**[00:04:43]** Als Treuhörer unserer Folgen, wisst ihr, dass Entropic viele Begriffe geprägt hat, MCP

**[00:04:49]** und Skills und das war mir damals gar nicht so geläufig.

**[00:04:53]** Und das geläufige kam mir sehr viel später, dass ich auf das Hörer, was Entropic sagt,

**[00:05:00]** dem ganzen mehr Gewicht gibt, z.B. in der Greifend, die ganze Promche, sich gefühlt danach orientiert,

**[00:05:05]** vor allen Dingen jetzt auch seitdem hier Crowdcode und so weiter durch die Decke gegangen ist.

**[00:05:08]** Und so kam es dann, dass ich an irgendeinem Tag mich dann doch mal hängengesetzt habe,

**[00:05:14]** wo mir diese unbedürsend Skills angeschaut habe. Und zu der damaligen Zeit war für mich ein Skill,

**[00:05:17]** ein Markdown Datei mit einem sehr langen Promt. Ich habe da noch keine Orkustratoren benutzt,

**[00:05:24]** sondern einfach, ich habe mit einem Code hingegangen und habe gedacht,

**[00:05:27]** Gut, okay, ich kann vielleicht mal eine ganze Promz jetzt als Skillpunkt MD abspeichern.

**[00:05:32]** Hab dir ein bisschen Namen gegeben, hab mit dir ein bisschen gearbeitet und so wurden die

**[00:05:34]** nach und nach immer ein bisschen besser.

**[00:05:36]** Und jetzt können wir ein bisschen zeitlich skippen, weil mittlerweile, was sind denn Skills

**[00:05:41]** mittlerweile?

**[00:05:42]** Ja, mittlerweile sind Skills eine Sammlung von Promz, die in mehr oder weniger Deterministischer,

**[00:05:48]** also programmatisch, also fester Reihenfolge arbeiten können.

**[00:05:52]** Du kannst, das hat mich schon immer, ne?

**[00:05:54]** Du kannst Wissen in so ein Skill packen, du kannst Python-Code als Programmierung reinpacken.

**[00:06:00]** Wir hatten es ja in der Folge mit René auch mal, dass ich gesagt habe, Skills sind für

**[00:06:03]** mich so eine Art Laufzeitumgebung für Python, dass man Programme in einem Skill abfahren kann.

**[00:06:10]** Ein Skill ist aber auch diese besagte Promtgeschichte, dass man Promts reinschreibt und ein Skill

**[00:06:16]** ist auch in der Lage mit Subskills zu arbeiten.

**[00:06:19]** Das heißt, ich habe dann einen Orchestratorskill, der wieder für sich weitere Orchestratorskills

**[00:06:23]** hat, indem dann weitere Skills sind. So kann man dem Ding dann sagen, du passst

**[00:06:28]** wobei ich habe hier Dokumente aus einem Prozesshaus, führe mich da durch,

**[00:06:33]** bilde bitte für jeden wichtigen Prozessschritt ein Orchestrator, für

**[00:06:37]** jede wichtige Tätigkeit ein Skill der Tätigkeit, speichert dir wichtige Richtlinien

**[00:06:43]** ähnliches als Nachschlagewerk ab und so kann man dem Ding immer weiter

**[00:06:46]** interagieren. Und dank des Skills Creator Skills von Entropic ist man ja auch

**[00:06:51]** in der Lage hinzugehen und zu sagen, nimm bitte diesen Skill und baue Evalroutinen ein. Also

**[00:07:00]** prüfe quasi die Korrektheit des Skills und mache Testcases rein, dass wenn du zukünftig

**[00:07:04]** weiter an dem Skill arbeitest, dass du quasi das Skill nie wieder so schlecht ist wie heute,

**[00:07:09]** sondern wie KI-Systeme Grüße gehen an Fable 5, nie wieder so schlecht werden wie heute.

**[00:07:15]** Und so war dann die Zeit, und das war die Zeit, als ich dachte, dass Prompt-Engineering tot ist.

**[00:07:23]** Weil wir machen jetzt der Skill-Engineering.

**[00:07:26]** Und wann das genau war, weiß ich nicht.

**[00:07:29]** Auf jeden Fall, bevor ich Claude Code cool fand.

**[00:07:31]** Und noch bevor ich N8N abgeschworen habe.

**[00:07:35]** Ich glaube bei Claude, ich denke auch gerade mal nach, wenn du so geredet hast,

**[00:07:39]** Ich glaube, Code war auch der Moment, wo zu dem Skill, so wie du es beschrieben hast,

**[00:07:44]** also dem MD-File, eigentlich noch das Thema dazu kam zu sagen, es gibt weitere echte Files

**[00:07:53]** oder eben auch Code, den ich über andere Dokumente dazu führen kann.

**[00:07:57]** Das war so eine Ebene für mich, ich hatte dieses Skill-Thema genauso, dass ich sage,

**[00:08:02]** das war eigentlich so ein bisschen das ganze Pre-Prompting in einen Skill reinzuschreiben.

**[00:08:05]** Das sehe ich auch vielleicht noch an die Custom-GPTs bei JetGPT damals, die relativ frühzeitig

**[00:08:10]** ja kam.

**[00:08:11]** Da konnte man auch im Prinzip eine Custom-GPT aufbauen, die man auch so ein bisschen mit

**[00:08:15]** Skill beschrieben hat, was sie da machen sollen.

**[00:08:17]** Man konnte auch, glaube ich, weitere Dokumente auch damals schon verlinkern.

**[00:08:22]** Auch bei den Custom-GPTs konnte man das, glaube ich, schon machen, damit ich es noch sagen

**[00:08:25]** muss, wo sie darauf zugreifen soll.

**[00:08:26]** Konntest Dokumente hinterlegen, dass, als wir es jetzt ein bisschen als Basis genutzt

**[00:08:30]** werden.

**[00:08:31]** Das war so ein bisschen ein kontinuierlicher Prozess.

**[00:08:32]** Ich würde mal festhalten, was auf jeden Fall total hip ist, dass innerhalb dieser KI-Phase,

**[00:08:40]** in der wir gerade sind, relativ zügig sehr, sehr viele neue Hype-Namen erfunden werden

**[00:08:46]** für Themen, die eigentlich nur, wenn man so richtig darauf guckt, eine kleine, evolutionäre

**[00:08:52]** Weiterentwicklung immer wieder ist.

**[00:08:53]** Aber ich würde sagen, wenn man heutzutage, und das Thema, das hat wir auch in der Besprechung

**[00:08:57]** besprochen, besprechen, ist so, dass auch wieder unser schon mal heute kritisierte

**[00:09:00]** Kapafi jetzt vor kurzem über das Thema Looping gesprochen hat, das Loop Engineering und

**[00:09:04]** sowas wichtiger ist als Prompt-Engineering. Es wird gerade wieder so aufgenommen. Aber eigentlich

**[00:09:08]** war das so eine städte Evolution, die wir in den letzten zwei, drei Jahren, glaube ich,

**[00:09:13]** gesehen haben. Deshalb ist es, glaube ich, auch so schwierig, diese Frage zu beantworten.

**[00:09:16]** Wann ist es denn jetzt eigentlich so von diesem reinen Prompt-Engineering zu einem

**[00:09:19]** Workflow-Open-Claw-Nutzer-Loop-Engineer eigentlich geworden in dem Moment? Ich glaube,

**[00:09:26]** Dann ist es gar nicht so, man kann glaube ich nicht den einen Punkt festmachen, sondern wobei den Anbietern gab es immer wieder schon Ansätze in diese Richtung.

**[00:09:32]** Dann gab es freie Systeme, die so ein bisschen versucht haben, Sachen in so ein Autolub reinzubringen, weil jetzt auch, wir haben ja mal auch über Open Claw geredet.

**[00:09:41]** Also Open Claws Hard Beat ist ja nichts anderes als so eine beständige kleine Skript, das immer mal wieder reinschaut und sagt, ist eigentlich etwas Neues da, soll ich da nochmal etwas tun in diesem Zusammenhang.

**[00:09:53]** zusammen haben. Und dann die Maschine quasi anstößt, um neue Aufgabe abzuleiten oder

**[00:10:00]** aus der Erkenntnis, die sie vielleicht vorher gewonnen hat, noch mal etwas neu aufzusetzen.

**[00:10:05]** Also so ein kleiner, angestoßener Loop und sich eigentlich immer wieder an das überlegen.

**[00:10:09]** Du hast jetzt eben ja schon den Begriff des Loops auch schon, ich sag jetzt mal ein

**[00:10:13]** bisschen aus der Praxis, wo man ihn vielleicht getroffen hat. Ich würde ganz gerne vielleicht

**[00:10:16]** noch zwei, drei Sachen vorher ableiten, weil wir so schön bis zu den Skills gekommen sind.

**[00:10:21]** vielleicht auch dann merken, dass Dinge nur weil sie jetzt einen Namen gekriegt haben,

**[00:10:26]** nicht automatisch neu sind. Ich meine, wenn wir ehrlich sind, ne, ein Skill-MD-Datei, das ist halt

**[00:10:33]** ein Prompt, halt ein sehr cooler und als Datei und mit Ordnerstruktur und so weiter, guck mal

**[00:10:38]** ein Skill-Archiv, von der Seite ist vielleicht das Neue, dass man Python-Skripte ausführen kann,

**[00:10:45]** dass man sie als Punkt Skill-Datei verteilen kann oder bei Google dann jams nennt oder

**[00:10:50]** Das haben wir mit dieses Skills und aufmerksame Hörer haben ja auch mitbekommen, dass ich mal dieses Berater-Ding da gebaut habe.

**[00:10:59]** Nach dem Motto ein Orchestrator sucht sich Consultants und wir haben uns damals darüber diskutiert, macht das eigentlich das Ergebnis besser,

**[00:11:07]** dass man verschiedene Personas auf ein Thema löst.

**[00:11:10]** Und ich war damals der Meinung, ja, ich bin immer noch der Meinung, ja, aber meine Begründung ist mittlerweile eine andere,

**[00:11:16]** ich noch hinkommen, weil jetzt gehst du halt hin und wendest so ein Skill an und sagst du pass mal

**[00:11:21]** auf, liebes System, machen wir mal eine Powerpoint. Hab ich einen schönen Skill, haben wir auch in der

**[00:11:26]** Firma, kannst du nutzen, machen wir eine schöne Powerpoint, da kommt die Powerpoint raus und sagst

**[00:11:29]** ja eigentlich hätte ich gerne auch eine Zusammenfassung am Schluss und dann rennt die

**[00:11:34]** Maschine los und dann sagst ja du pass mal auf, ich hätte auch gerne einen Rückgliederung,

**[00:11:37]** die passt gar nicht für Topmanagement, weil Topmanagement, Management Samaritan am Anfang

**[00:11:42]** ein bisschen erklären, bloß nicht zu viele Folien, bloß nicht zu viele Text, weil soll

**[00:11:45]** rund vor sein, wenn alle lesen, könnte es ja sein, dass du dann irgendwie vorher ausargumentiert

**[00:11:50]** wirst, bevor du irgendwie auf die Folie gekommen bist. Du merkst quasi, während du umsetzt,

**[00:11:53]** dass du immer wieder nacharbeitest. Das heißt, du kannst ein Skill verwenden, noch ein Skill

**[00:11:57]** verwenden, noch ein Skill verwenden, noch einen Prompt verwenden und und und und, dann macht

**[00:12:00]** Klart oder wer auch immer, oh, ich muss meinen Kontext komprimieren, kompekten, bla,

**[00:12:05]** bla, bla, damit es hier weitergeht und du arbeitest halt iterativ damit. Das heißt,

**[00:12:09]** du kommst sehr schnell, wie man das auch von anderen Lösungen kennt, du gibst

**[00:12:12]** kommt ein bis bei 80% der Lösung und dann iterierst du, iterierst, iterierst, iterierst,

**[00:12:16]** iterierst.

**[00:12:17]** Und bist du irgendwann vielleicht hoffentlich ein bisschen besser bist.

**[00:12:19]** Und da greift jetzt das Loop-Engineering ein.

**[00:12:22]** Das Loop-Engineering, ich fand das sehr schön, ich habe das von Peter Steinberg auf X gesehen,

**[00:12:28]** der dann geschrieben hat, dass er das so macht und einer meinte, höh, das kostet

**[00:12:31]** aber viele Tokens.

**[00:12:32]** Und er so, ich habe halt unlimited Tokens, was willst du, ja, fand ich auch nochmal

**[00:12:36]** nach dem Motto, deine Armut kotzt mich an, ja, hat er so nicht gesagt, so

**[00:12:39]** habe ich es gelesen.

**[00:12:40]** Und was macht das Loop-Engineering? Das Loop-Engineering geht jetzt im Grunde hin und sagt, also wir definieren eigentlich einen Prompt, der das System anweist zu sagen, was ist mein Ziel, was sind meine ganz konkreten Kriterien, an denen ich festmache, dass ich mein Ziel erreiche.

**[00:13:01]** Und ich gebe vorher eine Aufgabe und das System geht halt quasi hin, überprüft quasi stetig, ob das Ziel erreicht ist und wiederholt sich selbst so lange, bis das Ziel erreicht ist.

**[00:13:13]** Es geht quasi in so eine Art Endlust-Life. In der Programmierung hätten wir das versucht zu vermeiden.

**[00:13:20]** Beim Loop Engineering ist es quasi gewünscht, der Zustand je nach Ziel.

**[00:13:24]** Natürlich ist ein Endlustdrehendes System jetzt nicht das Ziel, aber wenn du sagst, pass obacht, ich möchte,

**[00:13:30]** dass du diese Texte so lange überarbeitest, bis eine fremde Person, die mit dem Thema nichts

**[00:13:36]** zu tun hat, das Thema versteht, ist die ausreichende Tiefe hat, um diese zu einem Experten zu machen,

**[00:13:42]** ist keine KI-Marke hart, es entsprechend viele Bebilderung hat und auch von Vorstellungen und

**[00:13:48]** kleinen Kindern verstanden werden kann und du diese ganzen Regeln definierst. Da kannst du

**[00:13:53]** da drinnen sagen und dafür nutzt du folgende Prompt und folgende Skills und du greifst

**[00:13:57]** der folgende Dateien zu. Dann würde diese Schleife sich so lange drehen, bis diese Bedingung

**[00:14:03]** eingetreten ist. Das kann ein Erfolgsfall sein, weil ich habe ja auch für 1000 Sachen Skills

**[00:14:11]** und Proms, also wenn du sagst, hier dieses Skills haben dann auch immer so eine Ergebnis-Tabelle,

**[00:14:16]** dass sie etwas bewerten, wie gut sie das Ergebnis finden. Und dann kann sie sagen,

**[00:14:19]** wir sind gemäß sagen, macht das so lange bis das Ergebnis mit 100% gut bewertet ist.

**[00:14:23]** Und zwar bis folgende 80 Skills, das die man bis 100 Prozent gut bewertet hat.

**[00:14:28]** Renter, Renter, Renter. Und das kann zehn Minuten sein, das kann zehn Stunden sein,

**[00:14:31]** das kann aber auch zehn Tage sein. Vorausgesetzt, du läufst halt nicht in

**[00:14:36]** so eine Zwangspause wie, oh, sie haben so viel mit Fable 5 gearbeitet, ihr Wochenkontinent

**[00:14:42]** ist verbraucht, kommen sie bitte am Sonntag wieder. Dann wird der Loop nicht automatisch anfangen.

**[00:14:47]** Das ist dann, also wenn das Tauchenfenster, also wenn das Tauchenfenster, das Apo verbraucht

**[00:14:51]** ist, musst du selbst nochmal anstarten. Aber wenn du Api-Usage machst, kannst du das quasi

**[00:14:56]** endlos laufen lassen. Und das ist natürlich auch der Haken. Wenn es endlos laufen könnte,

**[00:15:01]** kannst du auch endlos Token kosten. Darum kann man auch Abbruchgetälen einbauen, so

**[00:15:05]** nach dem Motto, wenn die tausendste Schleife 5 Millionen Euro, ne, dass das dann wird.

**[00:15:12]** Na ja, ich wollte auch mal in Dein Dimension bleiben, du erinnerst dich. Das ist ein

**[00:15:16]** Abricht. Und du hast ja auf den Clor und den Harnes gebracht, den Hermes. Im Grunde sind

**[00:15:22]** diese Schleifen, die die machen, nochmal eine übergeordnete. Weil die Schleifen, die ich

**[00:15:28]** jetzt eben beschrieben habe, die gebe ich im Terminalfenster ein. Mach das so lange bis.

**[00:15:32]** Man kennt es vielleicht von Claude Cote, dass man sagt slash goal und dann rennt er die

**[00:15:37]** Schleife so lange ab, bis das alles definitiv erreicht ist. Und man spricht dann von so

**[00:15:42]** sogenannten Meta-Schleifen, dann ist das das, wenn quasi das System aufgrund von Events

**[00:15:47]** eigenständig agiert.

**[00:15:49]** Änderungen in der Inbox, GitHub, Push, Zeitablauf, also der besagte Hard Beat.

**[00:15:56]** Und Schleifen können Schleifen aufrufen und Schleifen können Prompt aufrufen und

**[00:16:03]** dann glaube ich ist zumindest meine Wissensdarlegung auch erst mal, sag mal erschöpft, meine

**[00:16:09]** Schleife nähert sich dem Ende.

**[00:16:11]** Was an der Stelle vielleicht auch noch zu beachten ist, diese Themen empfehlen oder teilweise

**[00:16:18]** wird halt auch empfohlen, dass die Arbeit, das Act von einem anderen Modell gemacht werden

**[00:16:26]** soll als das Check, weil wenn du checkst mit demselben Modell und das im selben LLM läuft,

**[00:16:36]** dann checkt er quasi gegen seinen eigenen Kontext und da kann es gut sein, dass er dir

**[00:16:40]** die größte Rotze, die er hinprogrammiert hat, als den besten Code er auf der Welt bewertet.

**[00:16:45]** Darum gibt es die Idee zu sagen, gibt es einen anderen Modell, also im Form von gibt es einen

**[00:16:51]** neuen Session oder gibt es einen anderen Modell, damit das Ding quasi neutral dagegen guckt.

**[00:16:58]** Und die Frage ist dann nicht, ist das hier gut, weil dann sagt er nämlich bestens,

**[00:17:03]** ich habe noch nie so einen guten Entwickler gesehen wie dich, sondern du sagst, was ist

**[00:17:07]** daran schlecht, dass das Ziel nicht erreicht ist. Du trägst die Frage quasi um, so dass

**[00:17:12]** das, dass die Antwort vom Modell, weil es dir ja entsprechen will, automatisch etwas kritischer

**[00:17:18]** ausfällt. Und so bekommst du im Grunde einen kritischen Beobachter in dein Loop.

**[00:17:24]** Mhm. Die, ich stimme gleich die Frage, weil wir momentan auch, was wir gerade sehen,

**[00:17:30]** Solche Themen wie Dynamic Workflows und sowas auch haben.

**[00:17:34]** Ich glaube bei Claude Opus 4.8 ist es so, dass seitdem eben diese dünne Funktion, die ist

**[00:17:41]** so krass gut.

**[00:17:43]** Ist sie gut?

**[00:17:44]** Ja.

**[00:17:45]** Ich liebe sie.

**[00:17:46]** Weil, was macht sie?

**[00:17:47]** Sie macht ja im Prinzip, und deshalb frage ich nochmal nach, weil ich bin mir gar nicht

**[00:17:50]** mehr so sicher, ob das einig noch so, wie sich da verhält, sagen wir mal sowas,

**[00:17:54]** du gerade beschrieben hast, ob ich wirklich unterschiedliche Modelle haben muss, weil

**[00:17:57]** defakto, paralysiert, bloot, dann ja in dem Moment mehrere Subagents, die einzelne Routinen

**[00:18:03]** ablaufen können.

**[00:18:04]** Das heißt, ich habe nicht mehr einen Agenten, der jetzt quasi diese Aufgabe, diesen Loop

**[00:18:09]** durchführt, sondern ich habe vielleicht 20 verschiedene Instanzen und wäre es dann

**[00:18:15]** noch so, ich weiß nicht, ob das schon überprüft ist oder nicht, ob das, was du gerade beschrieben

**[00:18:19]** hast, dann trotzdem noch nötig ist oder ob ich sage, nee, also Subagenten, die sind

**[00:18:24]** dann schon unabhängig und die werden sich schon auch gegenseitig fest auf die Finger hauen,

**[00:18:28]** wenn einer mal was schief schräg macht.

**[00:18:30]** Das sind vielen Stellen recht und auch, hm, ah, schade, schade.

**[00:18:36]** Also vielleicht, wie heißt es immer so schön, jeder, vielleicht liege ich auch falsch, weil

**[00:18:41]** so wie ich sage, ich sage halt Entropic und wenn es falsch ist, soll doch der, darf

**[00:18:45]** jeder bestimmen, der dafür einen Abo bezahlt, ich sage mal, wer bezahlt, darf es sagen,

**[00:18:49]** wie es heißt.

**[00:18:50]** Bei Goal, Loop und Workflow, das sind ja so Funktionen und Subagents, die Cloud, Code bietet.

**[00:18:57]** Loop ist ja sowas wie, keine Ahnung, mach hier morgens um sieben, mach was.

**[00:19:01]** Goal heißt, verfolge ein Ziel und mach es so lange, bis es erledigt ist.

**[00:19:05]** Workflow heißt, mache dir einen Plan von Subagenten, die ein Ziel verfolgen.

**[00:19:12]** Und zwar nicht, in das sie sich gegenseitig quasi Intent, Act Check und so weiter arbeiten,

**[00:19:17]** sondern es wird vorher überlegt, es wird ein JavaScript erzeugt, das JavaScript

**[00:19:21]** orchestriert frische Sessions. Also ein Opus kann ein Sonnet spornen und sagen,

**[00:19:30]** machen wir mal 20 Rechercheagenten, da machst du mir nochmal fünf Opus-

**[00:19:35]** Agenten, die das Ganze zusammenfassen und dann machst du mir nochmal einen Opus-

**[00:19:39]** Agenten, der die Zusammenfassung zusammenfasst und das plant, der vorher

**[00:19:42]** führt das aus und gibt das Ergebnis. Und der Vorteil ist halt, jeder hat

**[00:19:46]** eigenen Kontext. Jeder Arbeit in seinem Kontext, jeder kriegt das, was er für seine Arbeit

**[00:19:50]** braucht und gibt dir nur das Endergebnis und müllt dir nicht deinen Kontext voll. Und wenn

**[00:19:55]** du das jetzt in Kombination nutzen willst, dann, da habe ich das tatsächlich meine Wissenslücke.

**[00:20:01]** Ich weiß nicht, ob Slash Girl automatisch auch zur Zielverfolgung Workflows starten würde.

**[00:20:07]** Ich weiß aber, dass wenn du den Claude auf Ultra Sync stellst, dass da die Eigenschaft

**[00:20:15]** eben genau das ist, dass er sagt, okay, wenn ich es brauche, starte ich Subworkflows.

**[00:20:20]** Ja.

**[00:20:21]** Und von daher, was kostet die Welt mit Beleuchtung?

**[00:20:24]** Mein liebstes Thema ist, ich mach Claude auf, ich sage ihm erstmal, plane mir das

**[00:20:29]** Thema, das ich umsetzen will, damit wirklich alles bedacht ist.

**[00:20:33]** Dann sage ich, je meistens mit Slash Workflow trete dagegen mit meinem Skill konstruktiver Kritiker

**[00:20:41]** und Meta-Analyse, also Kritiker, der ist ja der Skill, der sagt, was es sechs Monate später

**[00:20:47]** passiert, dass es erfolglos war und die Meta-Analyse ist es so beschrieben, dass ein fremdes System

**[00:20:53]** es verstehen würde.

**[00:20:54]** Wenn dann der Plan ausreichend verfeinert ist, dann sage ich meistens okay, Ultrakode

**[00:21:01]** und Slash Goal und sage bei Slash Goal, setze den Plan um bis der Prüfargent, also meine

**[00:21:09]** Codequalität und hast du nicht gesehen oder der kritischer Kritiker oder was auch immer

**[00:21:14]** sagt mit einer Punktzahl von, so lange setze den Plan um und dann geht er halt hin und

**[00:21:21]** verteilt sich Workflows und Macht und Hut und dann rennt der auch mal, wenn es sein

**[00:21:25]** muss, 10, 12, 20 Stunden. Dass das viele Tokens kostet, liegt im Auge des Betrachters und nicht

**[00:21:35]** mehr auf der Kreditkarte, weil da sind die Tokens ja dann schon runtergeflossen. Aber

**[00:21:39]** das ist durchaus nochmal eine andere Arbeit, als wenn du dann da stehst und sagst, so,

**[00:21:44]** hier sind jetzt 10 Punkte in meiner Checkliste, mach doch mal Checkliste ein und dann

**[00:21:48]** guckst du noch mal nach und dann machst du dies und das und jenes.

**[00:21:51]** Aber genauso, aber genauso wie du das beschrieben hast gerade, hätte ich jetzt auch das Thema Dynamic Workflows wirklich dann das quasi in the runtime auch zusätzliches Subagentchen zum Beispiel gestartet werden.

**[00:22:03]** So habe ich das jetzt gesehen, dass es funktioniert. Also das, was du ja auch gerade nochmal beschrieben hast, ist auch nochmal Zusätzliches.

**[00:22:09]** Da war es ja auch an mehreren Stellen zum Beispiel Human in the Loop.

**[00:22:12]** Das ist ja auch das Spannende, bei überall sind Loops. Ich würde sagen, je mehr Loops wir haben, desto weiter geht quasi der Human aus dem Loop raus und steht quasi...

**[00:22:23]** Das ist ja die Frage, was du als Loop definierst.

**[00:22:26]** Was du als definierst? Also, welche mit welchem Ziel du hinterher bist, ne, in dem Moment. Das ist ja gar nicht genau so. Also, wenn du sagst, also, so wie bei Claude Code im Prinzip diese Dynamic Workflows sind, wenn ich jetzt mal ein Beispiel bringen darf, dann ist es ja auch so was wie

**[00:22:37]** Analysiere 100 Wettbewerber, dann laufen halt irgendwie ein paar Subagents los und machen

**[00:22:43]** Preising-Vergleiche, andere laufen los und würden die UX-Bewerten von dem Wettbewerber

**[00:22:48]** wieder andere suchen irgendwelche Marktinformationen dazu und hinterher wird das dann zusammengeführt.

**[00:22:52]** Das ist ja im Prinzip so etwas wie viele kleine Agenten einzeln beauftragen, das wird

**[00:22:59]** prinziplich diese Dynamic Workflows gemacht und da laufen die dann auch wieder in Einzelnen

**[00:23:03]** Also viele Begrifflichkeiten, ehrlicherweise, die gerade ein bisschen überall rumschwirren,

**[00:23:09]** für eigentlich immer ähnliche Themen. Also irgendwo gibt es einen Anfangspunkt und ein Endpunkt.

**[00:23:15]** Früher war dieser Anfangspunkt tatsächlich nur, das ist ja richtig schön gesagt, auch mit den

**[00:23:20]** Prompten. Das war sagen, okay, dieser Prompt, den ich reingegeben habe, der war dann vielleicht

**[00:23:25]** mein Anfangspunkt. Es gab immer schon anderen Anfangspunkt noch davor, weil es gab schon

**[00:23:28]** immer den System prompt auch noch davor, der auch noch beschrieben hat, wie sich das System verhalten

**[00:23:34]** soll. Ja, das wurde eigentlich quasi nur erweitert da, um das Thema, natürlich hast du es vorhin gesagt,

**[00:23:38]** da ist auch Boah, mir kot jetzt mittlerweile bei. Aber eigentlich hat es quasi nur erweitert, dass ich sage,

**[00:23:42]** ja, mach weiter, bis du das Ziel verfolgt hast. Also, was ich im Prinzip früher in so einem

**[00:23:48]** einzelnen Promt hätte, nur mich wirklich gut machen könnte, da gab es dann immer wieder

**[00:23:51]** so Stoppbefehle. Derjenige von euch draußen, der auch mit Cloud Code vielleicht schon viele

**[00:23:55]** Sachen auch mal gemacht hat. Der kennt auch dieses Thema, dass man ihm auch

**[00:24:00]** relativ lange immer in so ein Modus reinbringen könnte, dass er auch nicht

**[00:24:03]** ständig nachfragt. Wenn er jetzt irgendwelche Sachen auf deiner Maschine zum Beispiel macht,

**[00:24:06]** dann gibt es ja auch den Modus, dass ich irgendwie sagen kann, der ist irgendwie

**[00:24:10]** in danger, das hast du nicht, ich weiß gar nicht mehr ganz genau wie der da ist.

**[00:24:13]** Diese Zahl heißt ja, kannst du ihm ja auch sagen, dass er quasi in so ein

**[00:24:16]** Cott-Mod rein geht und auch einfach ohne nachzufragen, dann weiterläuft.

**[00:24:19]** Das gibt es ja auch, du kannst ja ein Code, das ist ja auch sehr schön, das

**[00:24:24]** das auch mittlerweile ohne diese ganzen Parameter mit so einer Tab-Tasten-Kombination zwischen

**[00:24:30]** verschiedenen Modis durchgehen kannst und ihm dann halt sagen kannst, mach einfach weiter

**[00:24:35]** beantwortet für mich das Bastion Feuer.

**[00:24:38]** Ja, ja.

**[00:24:39]** Und es ist schon erstaunlich, vor allen Dingen, ich sag mal, es geißelt dich halt ein bisschen

**[00:24:45]** in der Professionalität, wie du mit dem System umgehst, weil das, was ich, wo ich gesagt

**[00:24:51]** Promp-Engineering ist tot, lange lebe ich das Promp-Engineering, ist, wenn du so mal guckst,

**[00:24:55]** ja, was es damals dann für verschiedene Techniken gab, wie muss ich ein Promp bauen, damit er das

**[00:25:02]** Ziel erreicht, jetzt baust du halt ein Promp, der im Grunde dafür sorgt, dass dieser Loop entsteht,

**[00:25:08]** in dem du sagst, mit diesen Sachen, was muss ich tun, mit was muss ich arbeiten, damit das quasi

**[00:25:17]** in sich alles Konsistent ist, um dieses Ziel zu erreichen. Ja, dieses Thema Persistenz ist, ja,

**[00:25:26]** machen wir das noch eine Entschuldigung? Das ist sehr nett, ja. Also dieses Beobachte das Ergebnis,

**[00:25:32]** Wähle deine Tools mit MCP und Skills, Handel durch Skills und Co. Was du tun musst, prüfe

**[00:25:38]** das Ergebnis, halte das Ergebnis dokumentiert fest, wiederhole die Schleife so lange bis,

**[00:25:44]** Das ist mein Loop-Engineering, das kannst du auch mit Skills bauen, das kannst du auch mit Python-Scripten bauen, ja, mit if, then, else und while und keine Ahnung, was.

**[00:25:54]** Jetzt hat es halt ein Fancy-Namen.

**[00:25:56]** Und geht auch schneller, bevor ich es alle selber baue, ne?

**[00:26:00]** Wenn du dich daran gewöhnt hast, ja, geht es tatsächlich schneller und ich fand zum Beispiel die Idee ganz cool.

**[00:26:06]** Es gibt ja so ein Loob-Datenbanken. Das ist ja auch nichts anderes als, das sind ja so 80, 90, 100 Zeichen.

**[00:26:14]** Was weiß ich, wie der Rode so lange bist, ist keine offenen Issues in deinem Gitme-Gibt oder so ein Quatsch.

**[00:26:21]** Das sind also Formulierungsarten, Formulierungshilfen, sag ich mal.

**[00:26:25]** Und ich bin jetzt hingegangen und habe die größten Loob-Bibliotheken, die ich so gefunden habe, habe ich die von Claude einlesen lassen.

**[00:26:32]** Ich habe gesagt, so guckt doch mal, so ist ein Loop aufgebaut, guckt mal, welche Formulierungen

**[00:26:37]** da gewählt sind und macht mir so, wie es ein Skill Creator Skill gibt, ein Loop Creator Skill,

**[00:26:43]** der mir quasi hilft, zu gucken, ob es dafür einen Loop gibt und der ist so integriert,

**[00:26:50]** dass alles, was ich jetzt quasi gerade in der Cloth Session schreibe, er bewertet,

**[00:26:55]** es hat das quasi Loop Potenzial und wenn ja, mit mir noch mal Diskussion geht und

**[00:27:00]** fragt, willst du daraus nicht einen Loop machen?

**[00:27:02]** Ja, Diskussion und dann den Loop durchführt.

**[00:27:06]** Und das gibt es ja total, ich meine ich habe jetzt eben diese 2 Skills, die ich da habe

**[00:27:09]** genannt.

**[00:27:10]** Ja, es gibt auch diesen Quill-Me-Skill, der quasi solange kritisch nachfragt, bis das

**[00:27:14]** Thema geklärt ist und ich glaube aus so einer Kombination, das lohnt sich total.

**[00:27:19]** So wie früher auch, ne, mach dir Gedanken, bevor du anfängst.

**[00:27:23]** Heute kannst du zwar mit dem prompten tolles Ergebnis erzielen, aber wenn du dir vorher

**[00:27:28]** Gedanken machst, wobei dir das System ja auch hilft. Kannst du den quasi danach los schicken, dir ein

**[00:27:33]** schönes Käffchen holen, der rennt irgendwie acht Stunden, liefert dir Milliarden-Zeilen-Code, ist

**[00:27:40]** vielleicht nicht automatisch gut. Da haben wir jetzt ja auch die letzten Tage immer wieder irgendwelche

**[00:27:44]** Bibliotheken gesehen, die uns helfen, dass der quasi, es gibt ja irgendwie so ein Skill, dass du

**[00:27:49]** der fauleste Programmierer bist, der nur das schreibt, was irgendwie nötig ist. Auch solches

**[00:27:54]** Das gilt, kannst du ja integrieren, aber ich glaube, dass das wirklich nochmal ein Umdenken

**[00:27:59]** ist, wie die Leute mit Kosten, Prompting und damit auch mit der damit verbundenen Effizienz

**[00:28:04]** umgehen.

**[00:28:05]** Ja, du hattest ja vorhin dann einmal schon das Thema jetzt, was ich gerade aufnehmen

**[00:28:10]** wollte, war einmal das Thema Kontext.

**[00:28:11]** Es passt aber auch gut zu dem anderen Thema, weil du vorhin hattest einmal den Hermes-Agenten,

**[00:28:15]** versiedig mit dem Harnis verwechselt.

**[00:28:17]** Letztens war es immer das C, heute ist es H.

**[00:28:21]** Ist ja nicht schlimm.

**[00:28:22]** Ist ja nicht schlimm.

**[00:28:23]** einzusteigen. Ich glaube, was wesentlich ist, wenn wir uns so ein bisschen von so einer Welt weg bewegen,

**[00:28:31]** in der man sagt, es ist nicht unbedingt die Agenten, die immer besser werden, sondern diese Loops werden

**[00:28:35]** eigentlich so eine Population von Agenten, die miteinander mit Loops arbeiten, dass wir in so

**[00:28:39]** eine Welt reingehen. Da wird natürlich der Kontext und der Harnis natürlich noch mehr entscheiden,

**[00:28:42]** weil auch zum Harnis, zum Harnis Engineering würde ich auch dazu zählen, dass wir so was haben,

**[00:28:47]** wie eine Tokenüberwachung, eine Modellswitcher im Notfall auch mal, der auf lokale oder eben

**[00:28:52]** nicht lokale Modell zu greifen kann, je nachdem wie viel Reasoning vielleicht benötigt wird,

**[00:28:56]** um damit schnellere Modellen arbeiten zu können. Ich glaube, das sind Sachen, die immer spannender

**[00:29:00]** werden, plus natürlich das Thema, das wir auch häufiger schon in der Sendung hatten, Memory.

**[00:29:04]** Also wo speichere ich im Prinzip der Kenntnisse, dass sie dann eben auch Kontext weiterhin

**[00:29:11]** offen halten, auch wenn man Loop zu Ende ist, wenn man Loop vielleicht auch mit einem

**[00:29:15]** Agenten zu Ende ist. Also wir hatten jetzt ein Beispiel, Fable auch, wo dann einfach mal

**[00:29:20]** ein Agent, ein Modell mit seinen Sessions dann abgeschaltet wird. Dann ist es

**[00:29:24]** natürlich ein Problem, wenn alle Informationen aus diesem stundentage lang

**[00:29:29]** laufenden Loop einfach verschwunden sind und nicht in anderer Art und Weise eben

**[00:29:34]** auch abgespeichert sind. Weil es wird, glaube ich, wichtig werden, dass man nicht

**[00:29:38]** nur den eigentlichen Output, der dann hoffentlich zu dem gewünschten

**[00:29:42]** Outcome führt, Abspeicher, also der eigentliche Decision, der eigentliche Code, der jedenfalls rausgekommen ist, sondern meiner Meinung

**[00:29:48]** auch wird es auch weiterhin wichtig werden, irgendwo die Erkenntnisse, die das Modell oder wenn der Mensch noch mal ab und zu unnupf war,

**[00:29:54]** auch mit dem Menschen dann zusammen quasi weiter an dem Code gearbeitet hat, an dem Produkt, das auch immer gebaut wird, gearbeitet hat,

**[00:30:01]** dass diese Erkenntnisse, die auf dem Weg, also man sagt ja auch mehr, der Weg ist das Ziel, also das sollten wir,

**[00:30:05]** glaube ich, also das kann man nicht zu wenig betonen, meiner Meinung nach,

**[00:30:10]** das zu einem guten Loop-Engineering meiner Meinung nach auch ein gutes Harnes-Engineering gehört,

**[00:30:16]** mit einem vernünftigen Memory-File, Second-Brain, das im Prinzip da die Erkenntnisse rauszieht,

**[00:30:22]** so dass denn der Loop auch darauf weiterarbeiten kann. Wundervoll, ob die Modelle da drunter

**[00:30:26]** wechseln. Ich finde an der Stelle, das kann man gar nicht auf genug wiederholen, weil du

**[00:30:32]** Du wirst mir recht geben, nachdem wir das Thema, wie hast du es genannt, was sind wir?

**[00:30:39]** Menschen?

**[00:30:40]** Auch?

**[00:30:41]** Ja, danke.

**[00:30:42]** So ruhig bin ich auch noch.

**[00:30:45]** Gurus, Gurus.

**[00:30:46]** Ach so ihr stimmt ja.

**[00:30:47]** Ja, manche sagen Nerds.

**[00:30:48]** Jetzt stell dir mal vor, aber es gibt ja durchaus einige, die nicht so nah an der Technik

**[00:30:54]** sind, ohne das jetzt werten zu wollen.

**[00:30:55]** An der Begriffstelten hatten wir auch schon ein anderer Umgang mit der Technik.

**[00:30:59]** Das ist das eine, nicht extremer, die eine Seite, die etwas unbedarfter vielleicht dran geht,

**[00:31:04]** die das auch gar nicht brauchen.

**[00:31:05]** Ja, ich benutze das.

**[00:31:06]** KI fließt in den Alltag ein, das soll ja unter der Haube verschwinden.

**[00:31:10]** Ist ja auch im Grunde das, wenn man etwas Gutes jetzt beispielsweise an der Apple-Ankündigung

**[00:31:14]** zu Siri AI bringen will, nach dem Motto KI verschwindet, aus der aktiven Nutzung ist

**[00:31:19]** einfach da.

**[00:31:20]** Auf der anderen Seite gibt es die großen Hersteller, Entropik, OpenAI, alle wollen

**[00:31:25]** an die Börse, alle wollen das neueste große Modell, alle alle, alle wollen alles und

**[00:31:30]** bringen coole Features. Da gibt es dann auch zusätzlich sowas wie OpenClaw und Harness,

**[00:31:35]** schon wieder Harness, Hermes Agent und Jarvis Agent, wie der ganze Kram heißt, die im

**[00:31:42]** Grunde eine andere Darreichungsform bieten und genau diese Umgebung bieten, wo laufen

**[00:31:47]** die Loops, welche Loops gibt es von Haus aus, wie unterstützen wir Loop, so wie Codex

**[00:31:52]** angefangen mit dem Slash Goal, kam dann später Cloud Code, dann kam Cloud Code jetzt mit Workflows,

**[00:31:58]** ob das jetzt bei Codex kommt, sei da hingestellt, aber die geben sich da nichts um, die lernen

**[00:32:02]** auch voneinander und ich finde an der Stelle ist eine Sache ziemlich wichtig. Diese Anwendungen

**[00:32:07]** erscheinen sehr stark im Commodity-Umfeld. Menschen schließen ein Abo ab und das Abo,

**[00:32:13]** das sie abschließen, sorgt dafür, dass sie die Tools nutzen und da benutze ich das vielleicht

**[00:32:18]** das eigen selbstständige Programmierer, aber sie sind jetzt nicht so konzerntauglich, so große

**[00:32:23]** Firmen tauglich. Das ist mehr so, ich installiere es mir, ich benutze es und wenn ich morgen was anderes

**[00:32:28]** will, dann nehme ich halt was anderes. Aber wenn du jetzt mal so an große Konzerne und Firmen

**[00:32:33]** denkst, dann kommt ganz schnell auch sowas wie Zertifizierungen, sehr schnell wie irgendwelche

**[00:32:38]** komischen Regularien rein, wo du halt sagst, okay gut, das hört sich so an, die alte Welt,

**[00:32:42]** ist ja gar nicht alte Welt, weil das hat ja alles seinen Sinn. Ich meine, Dinge sind entstanden,

**[00:32:46]** weil was passiert ist. Vielleicht übertreibt man in Deutschland, manchmal da ein oder

**[00:32:50]** anderen Stelle, das mag sein. Anissa trotz hat das alles irgendwie einen Sinn und ich habe

**[00:32:55]** so ein bisschen das Gefühl, mit KI kriegen wir das wieder eingefangen, weil wenn wir so ein

**[00:32:59]** Harnes selbst bauen, selbst bauen ist ja mit KI viel einfacher geworden. Dann kannst du so

**[00:33:07]** einem Harnes Dinge beibringen, wie Auditiere, Signiere, Nutze nur signiertes gilt. Auditiere,

**[00:33:14]** das, was du getan hast, dass man weiß, okay, das Ergebnis wurde mit diesem Skill erzeugt.

**[00:33:19]** Gucke jeden Tag nach, jede Stunde, wenn ein Event eintritt.

**[00:33:23]** Und dann stehst du wieder an der Frage, okay, ist jeder, der im Konzern oder in so einer

**[00:33:29]** großen Firma arbeitet, IT-ler, bist du wieder bei dem von eben?

**[00:33:32]** Nee, eigentlich nicht.

**[00:33:33]** Du musst also die Sprache sprechen, die Funktionalität ermöglichen und da finde

**[00:33:38]** ich diese Geschichte mit, man muss diesen Hahnes kontrollieren, weil wie gesagt die

**[00:33:42]** anderen machen halt mehr so dieses Commodity Produkt und Enabling ist für Konzerne,

**[00:33:47]** ist so diese Denke verdammter Axt. Du kannst etwas bauen, dass quasi, also ich bin jetzt ein bisschen

**[00:33:54]** ja, Deutschland könnte sich auch mal einer hin hocken und sagen wir mal, wir bauen jetzt mal

**[00:33:57]** hier so den deutscher Behörden Harnes, das hört sich total sexy an, aber wenn sich das mal

**[00:34:02]** eine ernsthaft machen würde, wie sagt man, meiner Meinung nach mehr Bürokratie als hier hat

**[00:34:07]** keiner, wenn wir so ein Harnes hinstellen würden, dass quasi alles automatisch im Hintergrund

**[00:34:10]** und erledigt, dann ist es ja quasi voll der Exportschlager. So wie früher Spiele, wenn

**[00:34:16]** sie in Deutschland verboten waren, FSK 18 in Deutschland, war das ja der Verkaufschlager

**[00:34:21]** von Doom, wir erinnern uns im Ausland. Und ich glaube, das wird total stark unterschätzt,

**[00:34:28]** welche Mächtigkeit im Hahnes liegt und es wird total stark unterschätzt, aber das

**[00:34:32]** ist jetzt kein Thema für eine Loopfolge, dass wenn du Leute mit ein bisschen Sachverstand

**[00:34:38]** und ein bisschen Guardrails und Regelwerk dran setzt, dass die auch mit Vibe Engineering

**[00:34:44]** so etwas bauen können. Im Prinzip ist ja das, also sagen wir mal so, ich glaube, wenn man

**[00:34:50]** jetzt ein bisschen reinschaut und nochmal Revue passieren, dass wir heute darüber gesprochen

**[00:34:56]** haben, auch die Entwicklung zu dem jetzigen Zeitpunkt, dann ist natürlich auch das

**[00:35:02]** kleine Skillbauen über den ersten Skill in D, den man mal geschrieben hat, dann

**[00:35:07]** ist das eigentlich schon so etwas wie die Vorstufe vom Harnes Engineering gewesen,

**[00:35:13]** weil wenn ich jetzt erst mal Platz sage, dann ist im Prinzip, was in der heutigen Welt passiert,

**[00:35:17]** ob das jetzt Sub-Agenten sind, ob das Loop sind, ob das mit einer Hermes gemacht wird,

**[00:35:22]** oder ob das mit Open Cloud gemacht wird, wo einfach immer wieder Loop angestoßen wird,

**[00:35:27]** haben die Visa alle heißen Gesamte zu Sachen, ist ja im Prinzip einfach nur eine

**[00:35:31]** Stufenweite bei alter Entwicklung von diesen Themen im Moment. Und ich glaube, man muss jetzt

**[00:35:36]** gar nicht so, wird es jetzt gerade gesagt, ist doch wieder so ein ITler. Ich glaube, ITler

**[00:35:40]** bringen im Prinzip dieses Fachwissen rund um das Thema dieser Domäne Software entwickeln,

**[00:35:45]** das die auch sicher sein kann, einfach mit. Das ist natürlich ein riesiger Vorteil. Ich

**[00:35:51]** glaube, wir müssen aber nicht alle ITler sein, um, glaube ich, gute Hanas aufzubauen. Auch

**[00:35:55]** jeder für sich kann das, glaube ich, jetzt anfangen. Es gibt auch genug Material,

**[00:35:58]** wo man das nachlesen kann. Man kann auch seinen KI wieder fragen, weil das spannende

**[00:36:02]** wird natürlich schon auf der anderen Seite sein. Du hast gerade von den großen Anbietern

**[00:36:06]** geredet, die auch weiterhin Geld verdienen wollen. Wenn wir so was beobachten, was dann

**[00:36:11]** passiert, wie dynamische Workflows die auftauchen, andere Themen die auftauchen bei den großen

**[00:36:16]** Anbietern, die sehen das natürlich auch. Das Harn ist ein wichtiger Teilwirt. Das Memory

**[00:36:22]** ein wichtiger Teilwirt. Deshalb gibt es auch Memory Files auch in den jetzt großen

**[00:36:27]** Agenten schon, die damit gelaufen werden. Aber das wird auch so ein bisschen ein

**[00:36:31]** kleiner Wettkampf sein zwischen den großen Modellanbietern, die natürlich sagen,

**[00:36:35]** ha, die Welt draußen fängt an auch mal über Modell-Switching und so was nachzudenken.

**[00:36:40]** Die wollen vielleicht nicht immer nur Millionen von Tokens ausgeben, sondern wollen da auch

**[00:36:44]** effiziente Wege finden mit unterschiedlich starken Modellen auch vielleicht arbeiten einfach.

**[00:36:47]** Ich glaube, das wird so ein kleiner Wettlauf werden zwischen, was baut man sich selber,

**[00:36:52]** was ist schlau, auch selber zu bauen. Und da sind da wahrscheinlich ein paar IT-Entscheidungen,

**[00:36:57]** die man tatsächlich vom IT-Land treffen lassen sollte, wenn man jetzt in Größe

**[00:37:00]** Umfängen unterwegs ist wie in größten Corporates zum Beispiel. Gegenüber dem Thema, was ist denn da

**[00:37:06]** draußen, was kommt von den Anbietern und was wird zur Komodität? Also, welche gibt es bald auch

**[00:37:11]** einen ChatGPT-Harness, der einfach mitgeliefert wird? Weißt du, wo ich dann einfach nur den

**[00:37:15]** Einstelle quasi und in der Diskussion mit meiner OpenAI ChatGPT. Vielleicht setze ich mich in

**[00:37:22]** die Nesseln, es ist ja alles kein geschützter Begriffsraum. Für mich ist halt Harness genau

**[00:37:27]** diese Cheshivity App oder die Cloud Co-Work App oder ein Open Claw oder ein Hermes. Ich habe es

**[00:37:34]** richtig gesagt. Das für mich halt ein Harnis, weil der das verbindet und das, was der Harnis nicht

**[00:37:39]** mitbringt, versucht der Anwender mühsam vielleicht von Hand reinzuklöppeln. So nach dem

**[00:37:43]** Motto, ich bin dem mir das an, damit ich ein Memory habe. Ich bin dem mir das an, damit das

**[00:37:49]** Ding, ich sage mir diesen Caveman Skill, damit das Ding spricht wie der Höhlenmensch und

**[00:37:54]** talk, musst du sparen und so weiter und so weiter. Und ich will vielleicht schon die Sachen

**[00:37:58]** noch ein bisschen weiter treiben. Das ist dann der Ha... weil wenn Codex zum Beispiel ein

**[00:38:02]** Harnis ist oder wie gesagt Code-Code ein Harnis ist, dann ist für mich, wenn die Menschen

**[00:38:07]** von einem Agentik OS sprechen, dann eher so die Frage, wenn mehrere Agenten gleichzeitig

**[00:38:13]** arbeiten, quasi der Harnis, mehrere Agenten parallel, unabhängig voneinander steuert,

**[00:38:20]** würde ich an der Stelle sagen, entspricht der Hanis das, was mein Agenteco ist. Da legt, weil dann ja,

**[00:38:27]** das quasi die Heimat ist nicht nur für einen Loop, der für dich läuft, der mit, also ein Loop,

**[00:38:34]** der Unter-Loops und Sub-Agence und alles drin hat, sondern mehrere Loops, die parallel laufen

**[00:38:39]** und sowas. Ja, das wäre so ein bisschen für mich so die, der versucht das ganze sprachlich

**[00:38:43]** ein bisschen einzusortieren. Was mir auch tatsächlich immer bei der Frage hilft, wenn du irgendwo

**[00:38:49]** wo auf einer Konferenz oder sonst was über Dinge sprichst oder mit Kollegen sprichst, um ein

**[00:38:56]** bisschen Klarheit reinzubringen nach dem Motto, was ist ein Skill und was ist ein Prompt und

**[00:39:00]** was ist ein X, Y und Z. Wir hatten es auch schon in der Folge, du sprichst von Skills, andere sagen

**[00:39:04]** Mitarbeiter, Entwicklung, du sagst Skill Engineering, was ist denn da los? Und so ist halt finde ich

**[00:39:09]** diese Geschichte mit Hannes und mit wo ist das LM, das lässt sich auch schön wie so eine

**[00:39:15]** Zwiebel darstellen. Da war immer hier weiter aus, wenn man geht, gibt es auch eine Begriffswelt.

**[00:39:18]** Und darin finden sich dann die besagten Loops und Metaloops und hast du nicht gesehen,

**[00:39:23]** wieder. Was auf jeden Fall die Menschen glaube ich draus mitnehmen sollten, ist,

**[00:39:28]** egal wie hip das heißt, nur weil man es nicht macht, ist man nicht abgehängt. Vielleicht

**[00:39:35]** macht man es, ohne es zu wissen. Nur weil du nicht 50 Milliarden Token durch den Erter schießt

**[00:39:42]** und ein gutes Ergebnis hast, heißt es ja nicht, dass du ein schlechter KI-Nutzer bist, aber

**[00:39:47]** das nichtsdestotrotz, und da finde ich, können wir mit dieser folgenden kleinen Beitrag leisten,

**[00:39:52]** diese Technik zu verstehen, zu sagen, ja verdammter Ax, geh doch mal einen Schritt zurück und

**[00:39:58]** beschreibe wirklich, was ist das Ziel und wie merke ich das Ziel, erreicht zu haben,

**[00:40:07]** oder wie breche ich auch ab im Fehlerfall, und dann die Chance zu haben, etwas zu

**[00:40:11]** haben das wirklich von, ich gucke mal schnell nach, sammelt Dateneine und gehe

**[00:40:16]** aus bis hin zu, ich muss auch nicht alles in Loop sein, bis hin zu, ich mache das

**[00:40:20]** jetzt so lange, bis das Ergebnis erreicht ist und ich habe Geduld und ich

**[00:40:26]** wiederhole und wiederhole und wiederhole, wo du, wenn du von Hand nach

**[00:40:31]** prompten würdest, auch irgendwann sagen würdest, weißt du was? Ich kann

**[00:40:35]** nicht mehr. Und letzter Satz, wenn du dann die einzelnen Schritte im Loop von einem

**[00:40:42]** Orchestrator machen lässt und alles in eigenen Modellen mit eigenem frischen Memory-Context,

**[00:40:48]** also Memory geteilt, aber frischer Kontext in der Bearbeitung, dann kannst du das ja im

**[00:40:52]** Grunde wirklich endlos laufen lassen bis entweder die goldenen Rechnung geschickt wird,

**[00:40:58]** weil du gerade die KI-Blase gerettet hast durch den Einwurf deiner Münzen oder weil das

**[00:41:05]** Das System schlicht und ergreifend ein Ziel erreicht hat und nicht vorher aufgrund des Selbstbetrugs.

**[00:41:10]** Ich arbeite mit meinem Kontext.

**[00:41:12]** Natürlich bin ich der Geilste auf der Welt.

**[00:41:14]** Natürlich habe ich alles richtig gemacht.

**[00:41:15]** Natürlich habe ich das Ziel erreicht, weil ich habe den Test gelöscht, habe ja in meinem

**[00:41:19]** Kontext, dass der Tester schon drin stand für die nächste Runde.

**[00:41:23]** Das umgehst du alles.

**[00:41:25]** Damit wird das auch sogar noch zuverlässiger.

**[00:41:27]** Punkt.

**[00:41:28]** Okay.

**[00:41:29]** Ja, ich glaube, damit können wir das eigentlich für heute ganz gut abschließen, dass

**[00:41:33]** Man sagt, so wie es vielleicht auch in der Programmierung damals schon ein wesentlicher Sprung war,

**[00:41:38]** als man da schleifen einen für den Kunter und nicht alles an einem Stück irgendwie in jeder

**[00:41:43]** einzelnen Code-Seile alle mögliche...

**[00:41:44]** If then, else go to.

**[00:41:46]** Genau.

**[00:41:47]** Zeilen.

**[00:41:48]** Zeilen.

**[00:41:49]** Ja, aber es ist halt, wie gesagt, wenn man überlegt, ist es ähnlich, und das natürlich

**[00:41:52]** auf einer ganz anderen Skalierungsebene.

**[00:41:54]** Ich glaube, wir verlassen dieses Thema, dass man sagt, gestern musste ich vielleicht

**[00:41:59]** noch den einzelnen Prompt, die einzelne Code-Seile einander rein, damit hinter

**[00:42:03]** ein Ergebnis rauskommt. Jetzt sind wir auf dieser Stufe schon, wo wir tatsächlich über die

**[00:42:08]** IF-Schleifen hinausgehen, dass wir Schleifen programmieren. Du hast es gerade angedeutet

**[00:42:13]** mit dem Orchestrator. Wir gehen in so eine Morgen wahrscheinlich in eine Zukunft rein, wo wir

**[00:42:17]** sagen, da macht das dann auch ein Agent weiterhin für mich, der seine eigenen, wir haben

**[00:42:20]** über dynamische Workflows geredet, über Subagents, die aufgesetzt werden. Ich glaube, da gehen

**[00:42:25]** wir hin, dass ich im Prinzip immer weniger, das ist da trotzdem ein guter Ansatz, immer

**[00:42:30]** wie derjenige verstehen muss, eigentlich, was im Hintergrund passiert und immer weniger die einzelne

**[00:42:34]** Codezeile im Zusammenspiel mit der KI selber quasi prompten programmieren muss in dem Sinne,

**[00:42:41]** sondern dass da viel viel viel selbstständiger geht, weil das ist das, was natürlich dann

**[00:42:46]** einfach auch für alle viel greifbarer macht, wenn ich mich tag und das fand ich ein starker

**[00:42:51]** Satz von dir, stark auf das Ziel konzentrieren kann. Was möchte ich denn eigentlich? Das wäre

**[00:42:56]** unsere menschliche Aufgabe, sich immer mehr darum dreht zu erkennen, was sind denn die

**[00:43:01]** eigentlichen Ziele, die wir verfolgen wollen? Was wollen wir erreichen und uns tatsächlich

**[00:43:06]** mehr auf den Outcome in diesem Fall konzentrieren, was das Ergebnis sein soll, anstatt dass der

**[00:43:11]** Output dann Millionen von Tokens waren? Also ich hoffe auch im Prinzip, dass dann diese Loops

**[00:43:16]** natürlich auch effizienter werden, dass man da Sachen einbauen kann, dass eben nicht die

**[00:43:21]** Maschine dumm Tokens verbrennt, sondern auch da wird es dann, glaube ich, zu einem guten

**[00:43:25]** Loop Engineering hören, dass man die nachhaltig effizient gestaltet und nicht einfach sagt,

**[00:43:30]** wie man es jetzt in meiner Zeit lang versucht hat, von den großen Anbietern zu erzählen.

**[00:43:33]** Du bist es nur wert, wenn du auch Millionen und fünf Milliarden von Tokens von brauchtest.

**[00:43:37]** Auf der Weg, das stimmt ja nicht. Also auch David, das glaube ich nicht mehr.

**[00:43:40]** Hold my beer! Dazu sollte es auch einfach kommen, dass man da im Prinzip mal,

**[00:43:44]** also zum guten Loop Engineering, zum guten Harnes Engineering, wenn man so um das Memory noch

**[00:43:49]** baut, sollte es meiner Meinung nach auch gehören, dass man da eben tokenoptimiert arbeitet

**[00:43:53]** und nicht blind den Maschinen der Zeit lang vertraut um weiter zu laufen, auch wenn sie es

**[00:43:58]** wahrscheinlich selber irgendwann auch ganz gut machen werden, aber das ist glaube ich per se

**[00:44:01]** momentan die Situation, dass wir sagen, wenn wir gerade über ein Harnes-Engineering reden,

**[00:44:06]** dann wird sich das auch irgendwann relativ zügig in den Modellen finden, die werden

**[00:44:09]** das auch schon selbstständig ganz gut machen können. Und ja, ich bin da glaube ich wie immer

**[00:44:15]** guter Dinge, jeder sollte sich das Thema wieder angucken, der da Bock drauf hat,

**[00:44:21]** baut mal eure eigenen Loops. Schaut mal, was da schon funktioniert, wie man über das

**[00:44:26]** Prompten hinausgehen kann in dem Moment mit den Tools der Wahl, die am Zur Verfügung stehen.

**[00:44:30]** Da geht, glaube ich, schon relativ viel. Und dass es die richtige Richtung ist, steht für mich

**[00:44:35]** auf jeden Fall außer Frage, dass man da weg von dem ich Prompte einzeln, sondern ich konzentriere

**[00:44:41]** mich eher auf ein Ergebnis und lasse die Maschine dann den Weg dahin bestreiten.

**[00:44:44]** Ja, also von der Seite würde ich auch sagen, wenn wir, wir könnten es ja mal so machen

**[00:44:51]** jetzt, ja, das Ziel hört alle Folgen von uns.

**[00:44:57]** Oh, prüft.

**[00:44:59]** Wenn ihr eine Folge gehört habt, ob es noch eine weitere Folge gibt, die ihr noch nicht gehört habt.

**[00:45:05]** Hört diese Folge wieder.

**[00:45:08]** prüft so lange, bis es keine weitere Folge mehr gibt. Dann wartet ihr eine Woche und

**[00:45:18]** startet den Loop von Neum. Und mit diesem kleinen Geschenk von Loop möchte ich mich

**[00:45:25]** heute bei euch verabschieden und Jens, ich glaube, ich habe viel zu viel gesprochen.

**[00:45:31]** Ich hätte es nicht über meine Abbruchregel vorherreden sollen. Danke, dass

**[00:45:38]** hast du da was? Danke, dass ihr da wart. Die Loop-Anweisung habt ihr bekommen und schaltet

**[00:45:43]** es nächstes Mal ein, wenn es wieder heißt. Think Different, think AI. Ciao.

**[00:45:49]** Willkommen bei Think Different, think AI, dem Podcast von Mark und Jens. Zwei technologieverliebte

**[00:45:59]** Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben. Hier gibt es klare

**[00:46:05]** Einordnungen, echte Praxis Einblicke und einen frischen Blick auf das, was möglich ist.

**[00:46:10]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:46:14]** K.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
