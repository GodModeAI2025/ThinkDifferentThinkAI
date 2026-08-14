---
title: "Loop Engineering"
episode_index: 47
duration: "2784"
page_url: "https://think-ai.podigee.io/47-loop-engineering"
source_feed: "https://think-ai.podigee.io/feed/mp3"
language: "de"
transcript_source: "manuell vom Nutzer bereitgestellt, keine Sekunden-Zeitmarken enthalten"
---

# Loop Engineering

**Episode:** 47
**Dauer:** 46:24 (2784s)
**Webplayer:** https://think-ai.podigee.io/47-loop-engineering

## Beschreibung (von der Podigee-Seite)

Die Moderatoren erklären, wie sich der Schwerpunkt vom Prompt Engineering zum Loop Engineering und Harness Engineering verlagert hat. Sie behandeln die Entwicklung von Prompt-Datenbanken über Skills als Markdown-Dateien bis hin zu Orchestratoren, Sub-Agents und Metaschleifen. Das Ziel besteht darin, KI auf übergeordnete Ziele statt einzelne Prompts auszurichten.

Keine externen Gäste — nur Jens und Mark.

## Transkript

*(Hinweis: manuell bereitgestellt, ohne Zeitstempel — siehe ep-047-marketing.md für geschätzte Kapitelmarken)*

Jens: Ich habe noch gar nicht gesehen.

Mark: Hast du schon runtergezählt?

Jens: Gott, wir sind schon live. Hallo, herzlich willkommen zu einer neuen Folge von

Jens: Think Different, Think AI.

Jens: Heute wollen Marc und ich mal über etwas reden, was sich, ich könnte es mal

Jens: so formulieren, über die letzten Jahre angekündigt hat.

Jens: Vor zwei, drei Jahren war die Frage noch ein bisschen, wer schreibt denn den

Jens: besten Prompt, wie schreibe ich den besten Prompt?

Jens: Heutzutage ist, glaube ich, eher die Frage, wenn man mal so schaut,

Jens: was im Internet unter den AI-Gurus so diskutiert wird, also den Gurus neben

Jens: Marc und mir, hallo Marc übrigens.

Jens: Ist das komisch, wenn man sich selber Guru nennt? Ich glaube schon.

Jens: Aber egal, mache ich gerne.

Mark: Bitte um Zuschriften an die Seite.

Jens: Heutzutage spricht man nicht mehr darüber, wer ingeniert den besten Prompt.

Jens: Heute wird darüber gesprochen, wer ingeniert die beste Schleife, den besten Loop.

Jens: Wer kriegt es also hin, die Zusammenarbeit mit KIs so zu gestalten,

Jens: dass die KIs möglichst Und ohne weiter nachzufragen, sehr komplexe Aufgaben für jemanden,

Jens: erledigen kann.

Jens: Das ist heute das Thema von der heutigen Sendung, dass wir mal darüber reden,

Jens: vom Prom zum Loop Engineering und was das denn bedeutet.

Jens: Und das betrachten wir heute in aller Tiefe, wie ihr es von uns gewohnt seid,

Jens: mit unserer Fachexpertise, ich lobe heute und zwar die ganze Zeit,

Jens: Mit dem lieben Marc, und der Marc, der darf jetzt auch gleich mal einsteigen

Jens: und sagen, seit wann war dir eigentlich so klar,

Jens: dass Prompt Engineering vielleicht nicht das Ende der Fahnenstange sein wird,

Jens: was das Thema KI betrifft?

Mark: Das finde ich eine schöne Überleitung, weil einem das klar wurde,

Mark: ich finde das tatsächlich, dass es gerade mit Blick auf Loops wieder einen neuen Pfad aufnimmt

Mark: Aber da würde ich ganz gerne erstmal irgendwie so ein bisschen darauf hinweisen.

Mark: Und nachdem du jetzt gesagt hast, dass ich hier so quasi so ein bisschen den

Mark: Einstieg machen soll, freue ich mich sehr bei den leicht erhöhten Temperaturen,

Mark: mein Gehirn so weit durchzulüften, dass es in der Lage ist, einen klaren Satz zu formulieren.

Mark: Und nicht in ein inneres Stocken zu kommen. Das innere Stocken ist auch eine

Mark: schöne Überleitung, weil der innerste Loop, den so ein LLM hat,

Mark: ist ja eigentlich der Loop erstmal über die Tokens.

Mark: Also die Zerlegung von Text in kleine Häppchen.

Mark: So nach dem Motto, ist da ein Wort drin, ist da ein Buchstabe drin,

Mark: sind da Silben drin. Wie treilt er denn die ganzen Worte in sich auf, um sie zu verarbeiten?

Mark: Da gab es ja auch vor einiger Zeit immer wieder mal so einen Aufschrei,

Mark: so nach dem Motto, Anthropic, hat die Preise erhöht? Nein, hat den Tokenverbrauch erhöht?

Mark: Ja, nein, weil sie haben diesen Tokenize, also das Zerlegen in Tokens angepasst.

Mark: Es ist aber so, mal egal, ob du Guru sagst oder nicht, Tokenizer haben wir nach

Mark: meinem Wissensstand noch nicht selbst, also verwendet ja, aber nicht selbst

Mark: verändert oder beeinflusst.

Mark: Und wenn nicht aktiv und unbewusst, wir sind ja eher eingestiegen beim Thema Prompt.

Mark: Da schließt sich so ein bisschen der Kreis von, hast du zum ersten Mal gemerkt,

Mark: dass Prompts gar nicht so das Ende der Fahnenstange sind.

Mark: Das hat tatsächlich lang gedauert. Ich erinnere mich an ein Gespräch,

Mark: wo ich Menschen immer gesagt habe, guck mal, wo ich mir so eine Prompt-Datenbank angelegt habe.

Mark: Das war so die Zeit, wo ich mit Notion gearbeitet habe. Ich habe mir eine Prompt-Datenbank

Mark: angelegt. Du bist ein erfahrener Software-Ingenieur. Du machst dies, das und jenes.

Mark: Und ich war auf meine Prompt-Datenbank ganz stolz. Die waren auch relativ lang.

Mark: Und ich habe das sehr gerne und ausführlich gepflegt.

Mark: Und ich erinnere mich, wie ich in der Firma war und Menschen von diesen ominösen

Mark: Skills gesprochen haben. Und ich dachte, ach, das setzt sich nicht durch.

Mark: Ach, der neumodische Kram. Diskette war schon immer gut. Wer will schon eine CD?

Mark: Als Treuhörer unserer Folgen wisst ihr, dass Entropic viele Begriffe geprägt

Mark: hat. MCP und Skills und das war mir damals gar nicht so geläufig.

Mark: Und das Geläufige kam mir erst sehr viel später, dass ich auf das höre,

Mark: was Entropic sagt, dass man dem Ganzen mehr Gewicht gibt. Beispielsweise ergreifend

Mark: die ganze Branche sich gefühlt danach orientiert, vor allen Dingen jetzt auch

Mark: seitdem hier Cloud-Code und so weiter durch die Decke gegangen ist.

Mark: Und so kam es dann, dass ich an irgendeinem Tag mich dann doch mal hingesetzt

Mark: habe, wo ich mir diese ominösen Skills angeschaut habe.

Mark: Und zu der damaligen Zeit war für mich ein Skill, eine Markdown-Datei mit einem sehr langen Prompt.

Mark: Und ich habe da noch keine Orchestratoren benutzt, sondern einfach,

Mark: ja, ich bin mit dem Kunden hingegangen und habe gedacht, gut,

Mark: okay, ich kann vielleicht meine ganzen Prompts jetzt als Skill.md abspeichern,

Mark: habe denen ein bisschen Namen gegeben, habe mit denen ein bisschen gearbeitet,

Mark: so wurden die nach und nach und nach immer ein bisschen besser.

Mark: Und das können wir ein bisschen zeitlich skippen, weil mittlerweile,

Mark: was sind denn Skills mittlerweile?

Mark: Mittlerweile sind Skills eine Sammlung von Prompt, die in mehr oder weniger

Mark: deterministischer, also programmatisch, also fester Reihenfolge arbeiten können.

Mark: Du kannst, das hatten wir schon mal, du kannst Wissen in so ein Skill packen,

Mark: du kannst Python-Code als Programmierung reinpacken.

Mark: Wir hatten es ja in der Folge mit René auch mal, dass ich gesagt habe,

Mark: Skills sind für mich so eine Art Laufzeitumgebung für Python,

Mark: dass man quasi Programme in dem Skill abfahren kann.

Mark: Ein Skill ist aber auch diese besagte Prompt-Geschichte, dass man Prompts reinschreibt

Mark: und ein Skill ist auch in der Lage, mit Sub-Skills zu arbeiten.

Mark: Das heißt, ich habe dann einen Orchestrator-Skill, der wieder für sich weitere

Mark: Orchestrator-Skills hat, in dem dann weitere Skills sind.

Mark: So kann man dem Ding dann sagen, du, pass mal, ich habe hier Dokumente aus einem

Mark: Prozesshaus, führe mich da durch, ich bilde bitte für jeden wichtigen Prozessschritt

Mark: einen Orchestrator, für jede wichtige Tätigkeit ein Skill der Tätigkeit,

Mark: speichere dir wichtige Richtlinien und Ähnliches als Nachschlagewerk ab und

Mark: so kann man mit dem Ding immer weiter interagieren.

Mark: Und dank des Skill Creator Skills von Anthropic ist man ja auch in der Lage,

Mark: Hinzugehen und zu sagen, nimm bitte diesen Skill und bau Eval-Routinen ein.

Mark: Also prüfe quasi die Korrektheit des Skills und mache Testcases rein,

Mark: dass wenn du zukünftig weiter an dem Skill arbeitest,

Mark: dass der Skill nie wieder so schlecht ist wie heute, sondern wie KI-Systeme

Mark: Grüße gehen an Fable5, nie wieder so schlecht werden wie heute.

Mark: Und so war dann die Zeit, und das war die Zeit, als ich dachte,

Mark: dass prompt Engineering tot ist.

Mark: Weil wir machen jetzt ja Skill Engineering.

Mark: Und wann das genau war, weiß ich nicht. Auf jeden Fall, bevor ich Claude Code

Mark: cool fand, und auch bevor ich N8N abgeschworen habe.

Jens: Ich glaube, bei Claude, ich denke auch gerade mal nach, also wenn du so geredet

Jens: hast, Claude Code war auch der Moment, wo zu dem Skill, so wie du ihn beschrieben

Jens: hast, also dem MD-File, eigentlich noch das Thema dazukam, zu sagen, es gibt weitere,

Jens: echte Files oder eben auch Code, den ich über andere Dokumente dazufügen kann.

Jens: Weißt du, das war so eine Ebene für mich. Weißt du, ich hatte dieses Skill-Thema

Jens: genauso, dass ich sage, das war eigentlich so ein bisschen das ganze Pre-Prompting

Jens: in einen Skill reinzuschreiben.

Jens: Du erinnerst dir ja auch vielleicht noch an die Custom-GPTs bei JetGPT damals,

Jens: die relativ frühzeitig ja kamen.

Jens: Da konnte man auch im Prinzip eine Custom-GPT aufbauen, den man auch so ein

Jens: bisschen mit Skill beschrieben hat, was sie da machen soll. Man konnte auch,

Jens: glaube ich, weitere Dokumente auch damals schon verlinken.

Jens: Auch bei den Kasten-GPTs konnte man das, glaube ich, schon machen.

Jens: Da müssen wir auch sagen, wo sie darauf zugreifen sollen.

Mark: Man konnte Dokumente hinterlegen, dass als Wissen die als Wissensbasis genutzt werden.

Jens: Das war so ein bisschen so ein kontinuierlicher Prozess. Ich würde mal festhalten.

Jens: Was auf jeden Fall total hip ist, dass innerhalb dieser KI-Phase,

Jens: in der wir gerade sind, relativ zügig sehr, sehr viele neue,

Jens: Hype-Namen erfunden werden für Themen, die eigentlich nur, wenn man so richtig

Jens: drauf guckt, eine kleine evolutionäre Weiterentwicklung immer wieder ist.

Jens: Aber ich würde sagen, wenn man heutzutage, und das Thema, weshalb wir es auch

Jens: in der Besondung besprechen, ist so, dass auch wieder hier unser schon mal häufiger

Jens: zitierte Kaphafi jetzt vor kurzem über das Thema Looping gesprochen hat,

Jens: das Loop-Engineering und sowas wichtiger ist als Prompt-Engineering.

Jens: Das wird gerade wieder so aufgenommen.

Jens: Aber eigentlich war das so eine stete Evolution, die wir in den letzten zwei,

Jens: drei Jahren, glaube ich, gesehen haben. Deshalb ist es, glaube ich,

Jens: auch so schwierig, diese Frage zu beantworten.

Jens: Wann ist es denn jetzt eigentlich so von diesem reinen Prompt-Engineering zu einem...

Jens: Ist Workflow, OpenClaw-Nutzer, Loop-Engineer eigentlich geworden in dem Moment.

Jens: Ich glaube, es ist gar nicht so, man kann, glaube ich, nicht den einen Punkt

Jens: festmachen, sondern wobei den Anbietern gab es immer wieder schon Ansätze in diese Richtung.

Jens: Dann gab es freie Systeme, die so ein bisschen versucht haben,

Jens: Sachen in so einen Autoloop reinzubringen, weil jetzt auch, wir haben ja mal

Jens: auch über OpenClaw geredet, also OpenClaws Heartbeat,

Jens: ist ja nichts anderes als so ein beständiger kleines Skript,

Jens: das immer mal wieder reinschaut und sagt, Ist eigentlich was Neues da?

Jens: Soll ich da nochmal was tun in diesem Zusammenhang? Und dann die Maschine quasi

Jens: anstößt, um eine neue Aufgabe abzuleiten oder aus den Erkenntnissen,

Jens: die sie vielleicht vorher gewonnen hat, nochmal etwas neu aufzusetzen.

Jens: Also so ein kleiner angestoßener Loop in sich eigentlich immer wieder, wenn man so etwas geht.

Mark: Du hast jetzt eben ja schon den Begriff des Loops auch schon,

Mark: ich sage jetzt mal ein bisschen aus der Praxis, wo man ihn vielleicht getroffen hat.

Mark: Ich würde ganz gerne vielleicht noch zwei, drei Sachen vorher ableiten,

Mark: weil wir so schön bis zu den Skills gekommen sind, dass wir vielleicht auch

Mark: dann merken, dass Dinge, nur weil sie jetzt einen Namen gekriegt haben,

Mark: nicht automatisch neu sind.

Mark: Ich meine, wenn wir ehrlich sind, eine Skill-MD-Datei, das ist halt ein Prompt,

Mark: halt ein sehr cooler und als Datei und mit Ordnerstruktur und so weiter.

Mark: Guck mal, ein Skill-Archiv, von der Seite ist vielleicht das Neue,

Mark: dass man Python-Skripte ausführen kann, dass man sie als Punkt-Skill-Datei verteilen

Mark: kann oder bei Google dann Gems nennt oder Custom-GPTs oder wie der ganze Kram so war.

Mark: So, jetzt haben wir aber diese Skills und aufmerksame Hörer haben ja auch mitbekommen,

Mark: dass ich mal dieses Berater-Ding da gebaut habe.

Mark: Das ist nach dem Motto, ein Orchestrator sucht sich Consultants.

Mark: Und wir haben uns damals darüber diskutiert, macht das eigentlich das Ergebnis

Mark: besser, dass man verschiedene Personas auf ein Thema loslässt.

Mark: Und ich war damals der Meinung, ja, ich bin immer noch der Meinung,

Mark: ja, aber meine Begründung ist mittlerweile eine andere, da möchte ich noch hinkommen,

Mark: weil jetzt gehst du halt hin und wendest so ein Skill an und sagst,

Mark: du hast mal Obacht, liebes System, machen wir mal eine PowerPoint.

Mark: Habe ich einen schönen Skill, haben wir auch in der Firma, kannst du nutzen,

Mark: machen wir mal eine schöne PowerPoint, dann kommt die PowerPoint raus und dann sagst du,

Mark: Ja, eigentlich hätte ich gerne

Mark: auch eine Zusammenfassung am Schluss und dann rennt die Maschine los.

Mark: Und dann sagst du, ah ja, du, pass mal, beobachte, ich hätte auch gerne eine

Mark: Nachrichtgliederung. Die passt so gar nicht für Top-Management,

Mark: weil Top-Management, Management-Sammarie am Anfang, ein bisschen erklären,

Mark: bloß nicht zu viele Folien, bloß nicht zu viel Text, weil soll ja eine Rundspur sein.

Mark: Wenn alle lesen, könnte es ja sein, dass du dann irgendwie vorher ausargumentiert

Mark: wirst, bevor du irgendwie auf die Folie gekommen bist.

Mark: Also du merkst quasi, während du umsetzt, dass du immer wieder nacharbeitest.

Mark: Das heißt, du kannst ein Skill verwenden, noch ein Skill verwenden,

Mark: noch ein Skill verwenden, noch einen Prompt verwenden und, und, und, und.

Mark: Dann macht Claude oder wer auch immer, oh, ich muss meinen Kontext komprimieren,

Mark: kompakten, bla, bla, bla, damit es hier weitergeht. Und du arbeitest halt iterativ damit.

Mark: Das heißt, du kommst sehr schnell, wie man das auch von anderen Lösungen kennt,

Mark: du gibst einen Prompt ein, bist bei 80 Prozent der Lösung und dann iterierst

Mark: du, iterierst du, iterierst du, iterierst du, bis du irgendwann vielleicht hoffentlich

Mark: ein bisschen besser bist.

Mark: Und da greift jetzt das Loop Engineering ein. Das Loop Engineering,

Mark: ich fand das sehr schön, ich habe das von Peter Steinberg auf X gesehen,

Mark: der dann geschrieben hat, dass er das so macht und einer meinte,

Mark: das kostet aber viele Tokens und er so, ich habe halt Unlimit Tokens, was willst du?

Mark: Ja, fand ich auch nochmal nach dem Motto, deine Armut kotzt mich an,

Mark: hat er so nicht gesagt, so habe ich es gelesen.

Mark: Und was macht das Loop Engineering? Das Loop Engineering geht jetzt im Grunde

Mark: hin und sagt, also wir definieren eigentlich einen Prompt, der das System anweist,

Mark: zu sagen, was ist mein Ziel?

Mark: Was sind meine ganz konkreten Kriterien,

Mark: an denen ich festmache, dass ich mein Ziel erreiche und ich gebe vorher eine

Mark: Aufgabe und das System geht halt quasi hin, überprüft quasi stetig,

Mark: ob das Ziel erreicht ist und wiederholt sich selbst so lange,

Mark: bis das Ziel erreicht ist.

Mark: Es geht quasi so eine Art Endlosschleife. In der Programmierung hätten wir das versucht zu vermeiden.

Mark: Beim Loop Engineering ist es quasi gewünschter Zustand je nach Ziel.

Mark: Natürlich ist ein Endlossdrehendes System jetzt nicht das Ziel,

Mark: aber wenn du sagst, pass, obacht, ich möchte,

Mark: dass du diese Texte so lange überarbeitest, bis eine fremde Person,

Mark: die mit dem Thema nichts zu tun oder das Thema versteht, es die ausreichende

Mark: Tiefe hat, um diese zu einem Experten zu machen,

Mark: es keine KI-Marke hat, es entsprechend viele Bebilderungen hat und auch von

Mark: Vorständen und kleinen Kindern verstanden werden kann und du diese ganzen Regeln definierst,

Mark: dann kannst du da drin sagen, und dafür nutzt du folgende Prompts und folgende

Mark: Skills und du greifst auf folgende Dateien zu.

Mark: Dann würde diese Schleife sich so lange drehen, bis diese Bedingung eingetreten ist.

Mark: Das kann ein Erfolgsfall sein, weil ich habe ja auch für tausend Sachen Skills und Prompts.

Mark: Und wenn du sagst, diese Skills haben dann auch immer so eine Ergebnistabelle,

Mark: dass sie etwas bewerten, wie gut finden sie das Ergebnis. Und dann kannst du

Mark: sagen, mach das so lange, bis das Ergebnis 100% gut bewertet ist.

Mark: Und zwar bis folgende 8 Skills, das Thema bis 100% gut bewertet hat.

Mark: Und dann rennt er, rennt er, rennt er. Und das kann 10 Minuten sein,

Mark: das kann 10 Stunden sein, das kann aber auch 10 Tage sein.

Mark: Vorausgesetzt, du läufst halt nicht in so eine Zwangspause wie,

Mark: oh, sie haben so viel mit Faible 5 gearbeitet, ihr Wochenkontingent ist verbraucht,

Mark: kommen sie bitte am Sonntag wieder.

Mark: Dann würde der Loop nicht automatisch anfangen. Das ist dann,

Mark: also wenn das Abo verbraucht ist, musst du es selbst nochmal anstarten.

Mark: Aber wenn du API-Usage machst, kannst du das quasi endlos laufen lassen.

Mark: Und das ist natürlich auch der Haken. Wenn es endlos laufen könnte,

Mark: Kannst du auch endlos Token kosten.

Mark: Darum kann man auch Abbruchkriterien einbauen, so nach dem Motto,

Mark: wenn die tausendste Schleife, fünf Millionen Euro, naja, ich wollte auch in

Mark: deinen Dimensionen bleiben, du erinnerst dich.

Mark: Ja, in der Zeit. Und du hast ja Open Claw und den Harness gebracht, den Hermes.

Mark: Im Grunde sind diese Schleifen, die die machen, nochmal eine übergeordnete.

Mark: Weil die Schleifen, die ich jetzt eben beschrieben habe, die gebe ich im Terminalfenster

Mark: ein. Mach das so lange bis.

Mark: Man kennt es vielleicht von Claude Cote, dass man sagt Slash Goal und dann rennt

Mark: er die Schleife so lange ab, bis das alles definitiv erreicht ist.

Mark: Und man spricht dann von sogenannten Metaschleifen.

Mark: Dann ist das das, wenn quasi das System aufgrund von Events eigenständig agiert.

Mark: Änderungen der Inbox, GitHub-Push, Zeitablauf, also der besagte Heartbeat.

Mark: Und Schleifen können Schleifen aufrufen und Schleifen können Prompts aufrufen.

Mark: Und dann glaube ich, ist zumindest meine Wissensdarlegung auch erstmal,

Mark: ich sag mal, erschöpft. Meine Schleife nähert sich dem Ende.

Mark: Was an der Stelle vielleicht auch noch zu beachten ist, die Systeme empfehlen,

Mark: Teilweise wird halt auch empfohlen, dass die Arbeit, das Act von einem anderen

Mark: Modell gemacht werden soll,

Mark: als das Check.

Mark: Weil, wenn du checkst mit demselben Modell und das im selben LLM läuft,

Mark: dann checkt er ja quasi gegen seinen eigenen Kontext.

Mark: Und da kann es gut sein, dass er dir die größte Rotze, die er hinprogrammiert

Mark: hat, als den besten Code ever auf der Welt bewertet.

Mark: Darum gibt es die Idee zu sagen, gibt es ein anderes Modell,

Mark: also in Form von gibt es eine neue Session oder gibt es ein anderes Modell,

Mark: damit das Ding quasi neutral dagegen guckt.

Mark: Und die Frage ist dann nicht, ist das hier gut, weil dann sagt er nämlich bestens,

Mark: ich habe noch nie so einen guten Entwickler gesehen wie dich.

Mark: Sondern du sagst, was ist daran schlecht, dass das Ziel nicht erreicht ist.

Mark: Du trägst die Frage quasi um,

Mark: sodass die Antwort vom Modell, weil es dir ja entsprechen will,

Mark: automatisch etwas kritischer ausfällt.

Mark: Und so bekommst du im Grunde einen kritischen Beobachter in deinen Loop.

Jens: Die, ich stelle mir gerade die Frage, weil wir momentan auch,

Jens: was wir gerade sehen, solche Themen wie Dynamic Workflows und sowas auch haben.

Jens: Ich glaube, bei Claude Opus 4.8 ist es so, dass seitdem eben diese dynamischen Workflows...

Mark: Super Funktion. Die ist so krass gut. Ist sie gut? Ich liebe sie.

Jens: Weil, was macht sie? Sie macht ja im Prinzip, und deshalb frage ich nochmal

Jens: nach, weil ich bin mir gar nicht mehr so sicher, ob das eigentlich noch so,

Jens: wie sich da verhält, sagen wir mal sowas, was du gerade beschrieben hast,

Jens: ob ich wirklich unterschiedliche Modelle haben muss, weil de facto paralysiert

Jens: Bloat dann ja in dem Moment mehrere Sub-Agents, die einzelne Routinen ablaufen können.

Jens: Und das heißt, ich habe nicht mehr einen Agenten, der jetzt quasi diesen diese

Jens: Aufgabe, diesen Loop durchführt, sondern ich habe vielleicht 20 verschiedene Instanzen,

Jens: und wäre es dann noch so, ich weiß nicht, ob du das schon überprüft hast oder

Jens: nicht, ob das, was du gerade beschrieben hast, dann trotzdem noch nötig ist oder ob ich sage, nee...

Jens: Sub-Agenten, die sind dann schon unabhängig und die werden sich schon auch gegenseitig

Jens: fest auf die Finger hauen, wenn da mal einer was schief schräg macht.

Mark: Du hast an vielen Stellen recht und auch nicht.

Jens: Ach, schade.

Mark: Also vielleicht, wie heißt es immer so schön, vielleicht liege ich auch falsch,

Mark: weil so wie ich sage, ich sage halt Anthropic und wenn es falsch ist,

Mark: darf doch jeder bestimmen, der dafür auch ein Abo bezahlt. Ich sage immer,

Mark: wer bezahlt, darf sagen, wie es heißt.

Mark: Bei Goal, Loop und Workflow, das sind ja so Funktionen und Sub-Agents, die Cloud Code bietet.

Mark: Loop ist ja sowas wie, keine Ahnung, mach hier morgens um sieben mach was.

Mark: Goal heißt, verfolge ein Ziel und mach es so lange, bis es erledigt ist.

Mark: Workflow heißt, mache dir einen Plan von Sub-Agenten, die ein Ziel verfolgen.

Mark: Und zwar nicht, dass sie sich gegenseitig quasi Intent, Act,

Mark: Check und so weiter arbeiten, sondern es wird vorher überlegt,

Mark: es wird ein JavaScript erzeugt, das JavaScript

Mark: orchestriert frische Sessions, also ein Opus kann ein Sonnet spawnen und sagen, mach mir mal 20

Mark: Rechercheagenten, da machst du mir nochmal 5 Opusagenten, die das Ganze zusammenfassen

Mark: und da machst du mir nochmal einen Opusagenten, der die Zusammenfassung zusammenfasst

Mark: und das plant der vorher, führt das aus und gibt das Ergebnis.

Mark: Und der Vorteil ist halt, jeder hat einen eigenen Kontext, jeder arbeitet in

Mark: seinem Kontext, jeder kriegt das, was er für seine Arbeit braucht und gibt dir

Mark: nur das Endergebnis und müll dir nicht deinen Kontext voll.

Mark: Und wenn du das jetzt in Kombination nutzen willst,

Mark: Und da habe ich tatsächlich meine Wissenslücke. Ich weiß nicht,

Mark: ob Slash Goal automatisch auch zur Zielverfolgung Workflows starten würde.

Mark: Ich weiß aber, dass wenn du den Cloud auf Ultrasync stellst,

Mark: dass da die Eigenschaft eben genau das ist, dass er sagt, okay,

Mark: wenn ich es brauche, starte ich Sub-Workflows.

Mark: Und von daher, was kostet die Welt mit Beleuchtung? Mein liebstes Thema ist, ich mache Cloud auf.

Mark: Ich sage ihm erst mal, plane mir das Thema, das ich umsetzen will.

Mark: Damit wirklich alles bedacht ist, dann sage ich ihm meistens mit Slash Workflow,

Mark: trete dagegen mit meinem Skill konstruktiver Kritiker und Meta-Analyse,

Mark: also Kritiker, der ist ja der Skill, der sagt,

Mark: was ist sechs Monate später passiert, dass es erfolglos war und die Meta-Analyse

Mark: ist es so geschrieben, dass ein fremdes System es verstehen würde.

Mark: Wenn dann der Plan ausreichend verfeinert ist, dann sage ich meistens,

Mark: okay, Ultracode und Slash Goal und sage bei Slash Goal, setze den Plan um,

Mark: bis der Prüfagent, also meine Codequalität und hast sie nicht gesehen oder der

Mark: Kritiker oder was auch immer, sagt mit einer Punktzahl von so lange setzt du den Plan um.

Mark: Und dann geht er halt hin und verteilt sich Workflows und macht und tut und

Mark: dann rennt der auch mal, wenn es sein muss, 10, 12, 20 Stunden.

Mark: Dass das viele Tokens kostet, liegt im Auge des Betrachters und nicht mehr auf

Mark: der Kreditkarte, weil da sind die Tokens ja dann schon runtergeflossen.

Mark: Aber das ist durchaus nochmal eine andere Arbeit, als wenn du dann da stehst

Mark: und sagst, so, hier sind jetzt zehn Punkte in meiner Checkliste,

Mark: mach nochmal Checkliste eins und dann guckst du nochmal nach und dann machst

Mark: du dies und das und jenes.

Jens: Aber genauso, wie du das beschrieben hast gerade, hätte ich jetzt auch das Thema Dynamic Workflows.

Jens: Wirklich dann, dass quasi in the runtime auch zusätzliche Subagenten zum Beispiel gestartet werden.

Jens: So habe ich das jetzt gesehen, dass es funktioniert. Also das,

Jens: was du ja auch gerade nochmal beschrieben hast, ist auch nochmal zusätzliches.

Jens: Also da war es ja auch an mehreren Stellen zum Beispiel Human in the Loop.

Jens: Das ist ja auch das Spannende, weil überall sind Loops. Ich würde sagen,

Jens: je mehr Loops wir haben, desto weiter geht quasi der Human aus dem Loop raus. Und steht quasi...

Mark: Das ist halt die Frage, was du als Loop definierst.

Jens: Was du als Definierst. Also mit welchem Ziel du hinterher bist in dem Moment.

Jens: Das ist ja nicht genauso. Also wenn du sagst, so wie ihr bei Cloud Code im Prinzip

Jens: diese Dynamic Workflows sind, wenn ich jetzt mal ein Beispiel bringen darf,

Jens: dann ist es ja auch sowas wie,

Jens: analysiere 100 Wettbewerber, ja, dann laufen halt irgendwie ein paar Sub-Agents

Jens: los und machen Pricing-Vergleiche, andere laufen los und würden die UX bewerten von dem Wettbewerber,

Jens: wieder andere suchen irgendwelche Marktinformationen dazu und hinterher wird

Jens: das dann zusammengeführt, ne, und das ist ja im Prinzip sowas wie,

Jens: viele kleine Agenten einzeln beauftragen, das wird im Prinzip durch diese Dynamic

Jens: Workflows gemacht und da laufen die dann auch wieder in einzelnen Loops los,

Jens: ne, also viele, viele Begrifflichkeiten, ehrlicherweise, die gerade ein bisschen überall rumschwirren,

Jens: für eigentlich immer ähnliche Themen.

Jens: Also irgendwo gibt es einen Anfangspunkt und einen Endpunkt.

Jens: Früher war dieser Anfangspunkt tatsächlich nur, du hast es ja richtig schön

Jens: gesagt, auch mit dem Prompt.

Jens: Das war sagen, okay, dieser Prompt, den ich reingegeben habe,

Jens: der war dann vielleicht mein Anfangspunkt.

Jens: Es gab immer schon einen anderen Anfangspunkt noch davor, weil es gab schon

Jens: immer den System-Prompt auch noch davor, der auch noch beschrieben hat,

Jens: wie sich das System verhalten soll.

Jens: Ja, das wurde eigentlich quasi nur erweitert da, um das Thema,

Jens: natürlich hast du es vorhin gesagt, da ist auch Programmierquote jetzt mittlerweile

Jens: bei, aber eigentlich hat es sich quasi nur erweitert, dass ich sage.

Jens: Ja, mach weiter, bis du das Ziel verfolgt hast. Also was ich im Prinzip früher

Jens: in so einem Einzel-Prom-Titel nur nicht wirklich gut machen könnte,

Jens: da gab es dann immer wieder Stopp-Befehle.

Jens: Derjenige von euch draußen, der auch mit Claude Groth vielleicht schon viele

Jens: Sachen auch mal gemacht hat, der erkennt auch dieses Thema, dass man eben auch,

Jens: Claude Groth schon relativ lange immer in so einen Modus reinbringen könnte,

Jens: dass er auch nicht ständig nachfragt.

Jens: Wenn er jetzt irgendwelche Sachen auf deiner Maschine zum Beispiel macht,

Jens: dann gibt es ja auch den Modus, dass ich irgendwie sagen kann,

Jens: der ist irgendwie im Danger, hast du nicht, ich weiß gar nicht mehr ganz genau,

Jens: wie der diese Zeile heißt, da kannst du ihm ja auch sagen, dass er quasi in

Jens: so einen Code-Mode reingeht und auch einfach ohne nachzufragen dann weiterläuft.

Mark: Das ist ja alles so. Das gibt es ja auch, du kannst ja ein Cloud-Code,

Mark: das ist ja auch sehr schön, dass du jetzt auch mittlerweile ohne diese ganzen Parameter

Mark: mit so einer Tab-Tasten-Kombination zwischen verschiedenen Modis durchgehen

Mark: kannst und ihm dann halt sagen kannst, mach einfach weiter, beantwortet für mich das BASCHO. Feuer!

Jens: Ja, ja, ja.

Mark: Und es ist schon erstaunlich, vor allen Dingen, ich sag mal,

Mark: es geißelt dich halt ein bisschen in der Professionalität, wie du mit dem System umgehst.

Mark: Weil das, was ich, wo ich gesagt habe, Prompt Engineering ist tot,

Mark: lang lebe das Prompt Engineering, ist, wenn du so mal guckst,

Mark: ja, was es damals dann für

Mark: verschiedene Techniken gab, wie muss ich einen Prompt bauen,

Mark: damit er das Ziel erreicht, jetzt baust du halt einen Prompt,

Mark: der im Grunde dafür sorgt, dass dieser Loop entsteht, in dem du ihm sagst,

Mark: mit diesen Sachen, was muss ich tun?

Mark: Mit was muss ich arbeiten, damit das quasi in sich alles konsistent ist,

Mark: um dieses Ziel zu erreichen?

Jens: Ja, dieses Thema Konsistenz ist, ja, und dann mache ich erst mal zu Ende, Entschuldigung.

Mark: Oh, das ist ja nett, ja. Also dieses Beobachte das Ergebnis,

Mark: wähle deine Tools mit MCP und Skills, handele durch Skills und Co.,

Mark: was du tun musst, prüfe das Ergebnis,

Mark: Halte das Ergebnis dokumentiert fest, wiederhole die Schleife so lange bis, das ist, ich meine,

Mark: Loop-Ingenierung, das kannst du auch mit Skills bauen, das kannst du auch mit

Mark: Python-Skripte bauen, ja, mit If, Then, Else und While und keine Ahnung was.

Mark: Jetzt hat es halt einen fancy Namen.

Jens: Und geht auch schneller, ne, bevor ich es alles selber baue, ne?

Mark: Wenn du dich daran gewöhnt hast, ja, geht es tatsächlich schneller und ich fand

Mark: zum Beispiel die Idee ganz cool, es gibt ja so Loop-Datenbanken,

Mark: Das ist ja auch nichts anderes als, das sind ja so 80, 90, 100 Zeichen,

Mark: das weiß ich, wiederhole so lange, bis es keine offenen Issues in deinem Git

Mark: mehr gibt oder so ein Quatsch.

Mark: Das sind also Formulierungsarten, Formulierungshilfen, sag ich mal.

Mark: Und ich bin jetzt hingegangen und habe die größten Loop-Bibliotheken,

Mark: die ich so gefunden habe, habe ich die von Claude einlesen lassen.

Mark: Und habe gesagt, so guck doch mal, so ist ein Loop aufgebaut,

Mark: guck mal, welche Formulierungen da gewählt sind und mach mir so,

Mark: wie es ein Skill-Creator-Skill gibt, ein Loop-Creator-Skill, der mir quasi hilft,

Mark: zu gucken, ob es dafür ein Loop gibt.

Mark: Und der ist so integriert, dass alles, was ich jetzt quasi gerade in der Cloud-Session

Mark: schreibe, er bewertet, es hat das quasi Loop-Potenzial.

Mark: Und wenn ja, mit mir nochmal in Diskussion geht und fragt, willst du daraus

Mark: nicht einen Loop machen? Ja, Diskussion und dann den Loop durchführt.

Mark: Und da gibt es ja total, ich meine, ich habe jetzt ja eben diese zwei Skills,

Mark: die ich da habe genannt, ja, es gibt ja auch diesen Quill Me Skill,

Mark: der quasi so lange kritisch nachfragt, bis das Thema geklärt ist.

Mark: Und ich glaube, aus so einer Kombination, das lohnt sich total.

Mark: So wie früher auch. Mach dir Gedanken, bevor du anfängst. Heute kannst du mir

Mark: zwar mit dem Prompt ein tolles Ergebnis erzielen, aber wenn du dir vorher Gedanken

Mark: machst, wobei dir das System ja auch hilft, kannst du den quasi danach losschicken,

Mark: dir ein schönes Käffchen holen.

Mark: Der rennt irgendwie acht Stunden, liefert dir Milliardenzeilen Code.

Mark: Ist vielleicht nicht automatisch gut. Da haben wir jetzt ja auch die letzten

Mark: Tage immer wieder irgendwelche Bibliotheken gesehen, die uns helfen,

Mark: dass der quasi, es gibt ja irgendwie so ein Skill, dass du der faulste Programmierer

Mark: bist, der nur da schreibt, was unbedingt nötig ist.

Mark: Auch solche Skills kannst du ja integrieren.

Mark: Aber ich glaube, dass das wirklich nochmal ein Umdenken ist,

Mark: wie die Leute mit Kosten prompting und damit auch mit der damit verbundenen Effizienz umgehen.

Jens: Ja, du hattest ja vorhin dann einmal schon, also das Thema jetzt,

Jens: was ich gerade aufnehmen wollte, war einmal das Thema Kontext.

Jens: Das passt aber auch gut zu dem anderen Thema, weil du vorhin hattest einmal

Jens: den Hermes-Agenten versehentlich mit dem Harness verwechselt.

Mark: Letztens war es immer das C,

Jens: Heute ist es H. Ist ja nicht schlimm, bietet mir die Möglichkeit einzusteigen.

Jens: Ich glaube, was wesentlich ist, wenn wir uns so ein bisschen von so einer Welt

Jens: wegbewegen, in der man sagt, es ist nicht unbedingt, die Agenten müssen besser

Jens: werden, sondern diese Loops werden eigentlich so eine Population von Agenten, die...

Jens: Miteinander mit Loops arbeiten, dass wir in so eine Welt reingehen,

Jens: da wird natürlich der Kontext der Harness natürlich noch entscheidender,

Jens: weil auch zum Harness Engineering würde ich auch dazu zählen,

Jens: dass wir sowas haben wie eine Tokenüberwachung, eine,

Jens: Modell-Switcher im Notfall auch mal, der auf lokale oder eben nicht lokale Modelle

Jens: zugreifen kann, je nachdem wie viel Reasoning vielleicht benötigt wird,

Jens: um damit schnell mit Modellen arbeiten zu können.

Jens: Ich glaube, das sind Sachen, die immer spannender werden. Plus natürlich das

Jens: Thema, was wir auch häufiger schon in der Sendung hatten, Memory.

Jens: Also wo speichere ich im Prinzip Erkenntnisse, dass sie dann eben auch Kontext,

Jens: weiterhin offen halten, auch wenn man Loop zu Ende ist, wenn man Loop vielleicht

Jens: auch mit einem Agenten zu Ende ist.

Jens: Also wir hatten jetzt vor kurzem das Beispiel Fable auch, wo dann einfach mal

Jens: ein Agent, ein Modell mit seinen Sessions dann abgeschaltet wird.

Jens: Dann ist es natürlich ein Problem, wenn alle Informationen aus diesem stundentagelang

Jens: laufenden Loop einfach verschwunden sind und nicht in anderer Art und Weise

Jens: eben auch abgespeichert sind.

Jens: Weil es wird, glaube ich, wichtig werden, dass man nicht nur den eigentlichen

Jens: Output, der dann hoffentlich zu dem gewünschten Outcome führt.

Jens: Abspeichert, also die eigentliche Decision, der eigentliche Code,

Jens: der gegebenenfalls rausgekommen ist, sondern meiner Meinung nach wird es auch

Jens: weiterhin wichtig werden, irgendwo,

Jens: die Erkenntnisse, die das Modell oder wenn der Mensch nochmal ab und zu unruf

Jens: war, auch mit den Menschen dann zusammen quasi weiter an dem Code erarbeitet

Jens: hat, an dem Produkt, was auch immer gebaut wird, gearbeitet hat,

Jens: dass diese Erkenntnisse, die auf dem Weg, also man sagt ja auch immer, der Weg ist das Ziel.

Jens: Also das sollten wir, glaube ich, also das kann man nicht zu wenig betonen, meiner Meinung nach,

Jens: dass zu einem guten Loop-Engineering meiner Meinung nach auch ein gutes Harness-Engineering gehört

Jens: mit einem vernünftigen Memory-File, Second Brain, das im Prinzip da die Erkenntnisse

Jens: rauszieht, sodass dann der Loop auch darauf weiterarbeiten kann,

Jens: unabhängig davon, ob die Modelle darunter wechseln.

Mark: Also ich finde an der Stelle, das kann man gar nicht oft genug wiederholen,

Mark: weil du wirst mir ja recht geben, nachdem wir das Thema sprechen.

Mark: Wie hast du es genannt? Was sind wir?

Jens: Menschen?

Mark: Auch, ja, danke. So heute bin ich auch noch. Gurus, Gurus. Achso,

Mark: ja, stimmt. Manche sagen Nerds.

Mark: Jetzt stell dir mal vor, aber es gibt ja durchaus einige, die jetzt nicht so

Mark: nah an der Technik sind, ohne das jetzt werten zu wollen. Andere Begriffshelten hatten wir auch schon.

Mark: Anderer Umgang mit der Technik, das ist das eine.

Mark: Nicht extrem, aber die eine Seite, die etwas unbedarfter vielleicht dran geht,

Mark: die das auch gar nicht braucht.

Mark: Ich benutze das. KI fließt in den Alltag ein. Das soll ja unter der Haube verschwinden.

Mark: Ist ja auch im Grunde das, wenn man was Gutes jetzt beispielsweise an der Apple-Ankündigung

Mark: zur Siri AI bringen will nach dem Motto KI verschwindet.

Mark: Aus der aktiven Nutzung ist einfach da. Auf der anderen Seite gibt es die großen

Mark: Hersteller, Entropic, OpenAI, alle wollen an die Börse, alle wollen das neueste

Mark: große Modell, alle, alle, alle wollen alles und bringen coole Features.

Mark: Da gibt es dann noch zusätzlich sowas wie OpenClaw und Harness,

Mark: Schon wieder Harness, Hermes Agent und Jarvis Agent und wie der ganze Kram heißt,

Mark: die im Grunde eine andere Darreichungsform bieten und genau diese Umgebung bieten,

Mark: wo laufen die Loops, welche Loops gibt es von Haus aus, wie unterstützen wir

Mark: Loop, ja, so wie Codex angefangen hat mit dem Slash Goal, kam dann später Cloud Code,

Mark: dann kam Cloud Code jetzt mit Workflows, ob das jetzt bei Codex kommt,

Mark: sei dahingestellt, Aber die geben sich da nichts und die lernen auch voneinander.

Mark: Und ich finde, an der Stelle ist eine Sache ziemlich wichtig.

Mark: Diese Anwendungen erscheinen sehr stark im Commodity-Umfeld.

Mark: Menschen schließen ein Abo ab und das Abo, das sie abschließen,

Mark: sorgt dafür, dass sie die Tools nutzen und dann benutze ich das vielleicht als

Mark: selbstständiger Programmierer, aber sie sind jetzt nicht so konzerntauglich,

Mark: so große, firmentauglich.

Mark: Das ist mehr so, ich installiere es mir, ich benutze es und wenn ich morgen

Mark: was anderes will, dann nehme ich halt was anderes.

Mark: Aber wenn du jetzt mal so an große Konzerne und Firmen denkst,

Mark: dann kommen ganz schnell auch sowas wie Zertifizierungen, sehr schnell wie irgendwelche

Mark: komischen Regularien rein, wo du halt sagst, okay gut, das hört sich so an wie alte Welt.

Mark: Ist ja gar nicht alte Welt, weil das hat ja alles seinen Sinn.

Mark: Ich meine, Dinge sind entstanden, weil was passiert ist. Vielleicht übertreibt

Mark: man in Deutschland manchmal an der einen oder anderen Stelle, das mag sein.

Mark: Nichtsdestotrotz hat das alles irgendwie einen Sinn und ich habe so ein bisschen

Mark: das Gefühl, mit KI kriegen wir das wieder eingefangen, weil wenn wir so ein

Mark: Harness selbst bauen und selbst bauen ist ja mit KI viel einfacher geworden.

Mark: Dann kannst du so einem Harness Dinge beibringen, wie auditiere,

Mark: signiere, nutze nur signierte Skills.

Mark: Auditiere das, was du getan hast, dass man weiß, okay, das Ergebnis wurde mit diesem Skill erzeugt.

Mark: Gucke jeden Tag nach, jede Stunde, wenn ein Event eintritt.

Mark: Und dann stehst du wieder an der Frage, okay, ist jeder, der im Konzern oder

Mark: in so einer großen Firma arbeitet, ITler, bist du wieder bei dem von eben? Nee, eigentlich nicht.

Mark: Du musst also die Sprache sprechen, die Funktionalität ermöglichen.

Mark: Und da finde ich diese Geschichte mit, man muss diesen Harness kontrollieren,

Mark: weil, wie gesagt, die anderen machen halt mehr so dieses Commodity-Produkt und

Mark: Enabling ist für Konzerne, ist so diese Denke, verdammte Axt, du kannst etwas bauen,

Mark: Das quasi, Also ich spinne jetzt ein bisschen.

Mark: Deutschland könnte sich auch mal einer hinhocken und sagen wir mal,

Mark: wir bauen jetzt mal hier so den deutscher Behörden-Harness.

Mark: Das hört sich total sexy an. Aber wenn sich das mal einer ernsthaft machen würde,

Mark: ich sag mal meiner Meinung nach, mehr Bürokratie als wir hat keiner.

Mark: Wenn wir so einen Harness hinstellen würden, der das quasi alles automatisch

Mark: im Hintergrund erledigt, ja, dann ist es ja quasi voll der Exportschlager.

Mark: So wie früher Spiele, wenn sie in Deutschland verboten waren.

Mark: FSK 18 in Deutschland war das ja der Verkaufsschlager von Doom.

Mark: Wir erinnern uns, im Ausland.

Mark: Und ich glaube, das wird total stark unterschätzt, welche Mächtigkeit im Harness liegt.

Mark: Und es wird total stark unterschätzt, aber das ist jetzt kein Thema für eine Loop-Folge,

Mark: dass wenn du Leute mit ein bisschen Sachverstand und ein bisschen Guardrails

Mark: und Regelwerk dransetzt, dass die auch mit Vibe Engineering so etwas bauen können.

Jens: Im Prinzip ist es ja das. Also sagen wir mal so, ich glaube,

Jens: wenn man jetzt nur ein bisschen reinschaut und nochmal Revue passieren,

Jens: das wir heute darüber gesprochen haben, auch die Entwicklung zu dem jetzigen Zeitpunkt.

Jens: Dann ist natürlich auch das kleine Skill-Bauen über den ersten Skill-MD,

Jens: den man mal geschrieben hat, dann ist das eigentlich schon so etwas wie die

Jens: Vorstufe vom Harness-Engineering gewesen.

Jens: Weil wenn ich jetzt mal Platz sage, dann ist im Prinzip, was in der heutigen

Jens: Welt passiert, ob das jetzt Sub-Agenten sind, ob das Loops sind,

Jens: ob das mit einer Hermes gemacht wird oder ob das mit OpenClaw gemacht wird,

Jens: wo einfach immer wieder ein Loop angestoßen wird,

Jens: wie sie alle heißen, die gesamten Sachen, ist ja im Prinzip einfach nur eine

Jens: stufenweite Weiterentwicklung von diesen Themen in dem Moment.

Jens: Und ich glaube, man muss jetzt gar nicht so, du hast jetzt gerade gesagt,

Jens: es ist doch wieder so ein ITler, ich glaube, ITler bringen im Prinzip dieses

Jens: Fachwissen rund um das Thema dieser Domäne, Software entwickeln,

Jens: dass die auch sicher sein kann, einfach mit.

Jens: Das ist natürlich ein riesiger Vorteil. Ich glaube, wir müssen aber nicht alle

Jens: ITler sein, um, glaube ich, gute Haarnas aufzubauen. Auch jeder für sich kann

Jens: das, glaube ich, jetzt anfangen. Es gibt auch genug Material,

Jens: wo man das nachlesen kann.

Jens: Man kann auch seine KI wieder fragen, weil das Spannende wird natürlich schon

Jens: auf der anderen Seite sein, du hast gerade von den großen Anbietern geredet,

Jens: die auch weiterhin Geld verdienen wollen.

Jens: Wenn wir sowas beobachten, was dann passiert, wie dynamische Workflows,

Jens: die auftauchen, andere Themen, die auftauchen bei den großen Anbietern,

Jens: die sehen das natürlich auch, dass Harness ein wichtiger Teil wird,

Jens: dass Memory ein wichtiger Teil wird.

Jens: Deshalb gibt es auch Memory-Files auch in den jetzt großen Agenten schon,

Jens: die da mitgelaufen werden.

Jens: Aber das wird auch so ein bisschen so ein kleiner Wettkampf sein zwischen den

Jens: großen Modellanbietern, die natürlich sagen, aha, die Welt draußen fängt an,

Jens: auch mal über Modell-Switching und sowas nachzudenken.

Jens: Die wollen vielleicht nicht immer nur Millionen von Tokens ausgeben,

Jens: sondern wollen da auch effiziente Wege finden, mit unterschiedlich starken Modellen

Jens: auch vielleicht arbeiten einfach.

Jens: Ich glaube, das wird so ein kleiner Wettlauf werden zwischen,

Jens: was haut man sich selber, was ist schlau auch selber zu bauen und das sind da

Jens: wahrscheinlich ein paar,

Jens: IT-Entscheidungen, die man tatsächlich von ITlern treffen lassen sollte,

Jens: wenn man jetzt in größeren Umfängen unterwegs ist, wie in größeren Corporates zum Beispiel.

Jens: Gegenüber dem Thema, was ist denn da draußen, was kommt von den Anbietern und

Jens: was wird zur Commodity? Also gibt es bald auch einen Chat-GPT-Harness,

Jens: der einfach mitgeliefert wird, wo ich dann einfach nur den einstelle quasi und

Jens: in der Diskussion mit meiner OpenAI-Chat-GPT.

Mark: Vielleicht setze ich mich in die Nesseln. Es ist ja alles kein geschützter Begriffsraum.

Mark: Für mich ist halt Harness genau diese Chat-GPT-App oder die Cloud-Cowork-App

Mark: oder ein OpenClaw oder ein Hermes. Ich habe es richtig gesagt.

Mark: Das ist für mich halt ein Harness, weil der das verbindet und das,

Mark: was der Harness nicht mitbringt, versucht der Anwender mühsam vielleicht von Hand rein zu klöppeln.

Mark: So nach dem Motto, ich binde mir das an, damit ich ein Memory habe,

Mark: ich binde mir das an, damit das Ding hier, ich lade mir diesen Caveman-Skill,

Mark: damit das Ding spricht wie der Höhlenmensch, um Tokens zu sparen und so weiter

Mark: und so weiter und so weiter.

Mark: Und ich will vielleicht schon die Sache noch ein bisschen weiter treiben.

Mark: Das ist dann der Harness, weil wenn ein Codex zum Beispiel ein Harness ist oder

Mark: wie gesagt Cloud Code ein Harness ist,

Mark: dann ist für mich, wenn die Menschen von einem Agentic OS sprechen,

Mark: dann eher so die Frage, wenn mehrere Agenten gleichzeitig arbeiten,

Mark: quasi der Harness mehrere Agenten parallel unabhängig voneinander steuert,

Mark: dann würde ich an der Stelle sagen, entspricht der Harness das, was man im Agentic OS

Mark: darlegt, Weil dann ja, das quasi die Heimat ist, nicht nur für einen

Mark: Loop, der für dich läuft,

Mark: also ein Loop, der Unterloops und Subagents und alles drin hat,

Mark: sondern mehrere Loops, die parallel laufen und sowas.

Mark: Ja, das wäre so ein bisschen für mich so der Versuch, das Ganze sprachlich ein

Mark: bisschen einzusortieren.

Mark: Was mir auch tatsächlich immer bei der Frage hilft, wenn du irgendwo auf einer

Mark: Konferenz oder sonst was über Dinge sprichst oder mit Kollegen sprichst,

Mark: um ein bisschen Klarheit reinzubringen nach dem Motto, was ist ein Skill und

Mark: was ist ein Prompt und was ist ein XYZ.

Mark: Wir hatten es auch schon in der Folge, du sprichst von Skills,

Mark: andere sagen Mitarbeiterentwicklung, du sagst Skill Engineering, was ist denn da los?

Mark: Und so ist halt, finde ich, diese Geschichte mit Harness und mit wo ist das LLM.

Mark: Das lässt sich auch schön wie so eine Zwiebel darstellen, je weiter aus man

Mark: geht, gibt es auch eine Begriffswelt und da drin finden sich dann die besagten

Mark: Loops und Meterloops und hast du nicht gesehen, wieder.

Mark: Was auf jeden Fall die Menschen, glaube ich, daraus mitnehmen sollten,

Mark: ist, egal wie hit das heißt, nur weil man es nicht macht, ist man nicht abgehängt.

Mark: Vielleicht macht man es, ohne es zu wissen.

Mark: Nur weil du nicht 50 Milliarden Token durch den Äther schießt und ein gutes

Mark: Ergebnis hast, heißt es ja nicht, dass du ein schlechter KI-Nutzer bist.

Mark: Aber nichtsdestotrotz, und da finde ich, können wir mit dieser Folge einen kleinen

Mark: Beitrag leisten, diese Technik zu verstehen, zu sagen,

Mark: ja verdammte Axt, geh doch mal einen Schritt zurück und beschreibe wirklich,

Mark: was ist das Ziel und wie merke ich das Ziel erreicht zu haben

Mark: Oder wie breche ich auch ab im Fehlerfall und dann die Chance zu haben,

Mark: etwas zu haben, Das wirklich von, ich gucke mal schnell nach,

Mark: sammle Daten ein und gehe aus, bis hin zu, ich muss ja auch nicht alles in Loop sein,

Mark: bis hin zu, ich mache das jetzt so lange, bis das Ergebnis erreicht ist und

Mark: ich habe Geduld und ich wiederhole und wiederhole und wiederhole.

Mark: Wo du, wenn du von Hand nachprompten würdest, auch irgendwann sagen würdest,

Mark: weißt du was, ich kann nicht mehr.

Mark: Und letzter Satz, wenn du dann die einzelnen Schritte im Loop von einem Orchestrator

Mark: machen lässt und alles in eigenen Modellen mit eigenem frischen Memory-Kontext,

Mark: also Memory geteilt, aber frischer Kontext in der Bearbeitung,

Mark: dann kannst du das ja im Grunde wirklich endlos laufen lassen,

Mark: bis entweder die goldene Rechnung geschickt wird, weil du gerade die KI-Blase

Mark: gerettet hast durch den Einwurf deiner Münzen

Mark: oder weil das System schlicht und ergreifend ein Ziel erreicht hat und nicht

Mark: vorher aufgrund des Selbstbetrugs.

Mark: Ich arbeite mit meinem Kontext. Natürlich bin ich der Geilste auf der Welt.

Mark: Natürlich habe ich alles richtig gemacht. Natürlich habe ich das Ziel erreicht,

Mark: weil ich habe den Test gelöscht, habe ja in meinem Kontext, dass der Test da

Mark: schon drin stand für die nächste Runde.

Mark: Das umgehst du alles. Damit wird das auch sogar noch zuverlässiger. Punkt.

Jens: Okay. Ja, ich glaube, damit können wir das eigentlich für heute ganz gut abschließen, dass man sagt,

Jens: so wie es vielleicht auch in der Programmierung damals schon ein wesentlicher

Jens: Sprung war, als man da schleifen einen Film runter und nicht alles an einem

Jens: Stück, irgendwie in jeder einzelnen Kurzzeile, alle möglichen...

Mark: If then else go to. Genau. Hm, Zeilensprung.

Jens: Ja, aber es ist halt, wie gesagt, wenn man überlegt, ist es ähnlich.

Jens: Und das ist natürlich auf einer ganz anderen Skalierungsebene.

Jens: Ich glaube, wir sind, wir verlassen dieses Thema, dass man sagt,

Jens: gestern musste ich vielleicht noch den einzelnen Prompt, die einzelne Codezeile

Jens: aneinanderreihen, damit hinter ein Ergebnis rauskommt.

Jens: Jetzt sind wir ja auf dieser Stufe schon, wo wir tatsächlich über die IF-Schleifen

Jens: hinausgehen, dass wir Schleifen programmieren.

Jens: Du hast es gerade angedeutet mit dem Orchestrator, wir gehen in so eine,

Jens: morgen wahrscheinlich in eine Zukunft rein, wo wir sagen, da macht das dann

Jens: auch ein Agent weiterhin für mich, der seine eigenen, wir haben über dynamische

Jens: Workflows geredet, über Subagents, die aufgesetzt werden.

Jens: Ich glaube, da gehen wir hin, dass ich im Prinzip immer weniger,

Jens: das ist da trotzdem ein guter Ansatz, immer weniger verstehen muss,

Jens: eigentlich was im Hintergrund passiert und immer weniger die einzelne Codezeile

Jens: im Zusammenspiel mit der KI aufzusetzen.

Jens: Selber quasi prompten, programmieren muss in dem Sinne, sondern dass da viel,

Jens: viel selbstständiger geht.

Jens: Weil das ist das, was natürlich dann einfach auch für alle viel greifbarer macht,

Jens: wenn ich mich, und das fand ich ein starker Satz von dir, stark auf das Ziel konzentrieren kann.

Jens: Was möchte ich denn eigentlich? Dass unsere menschliche Aufgabe sich immer mehr

Jens: darum dreht, zu erkennen, was sind denn die eigentlichen Ziele,

Jens: die wir verfolgen wollen?

Jens: Was wollen wir erreichen und uns tatsächlich mehr auf den Outcome in diesem

Jens: Fall konzentrieren, was das Ergebnis sein soll, anstatt im Prinzip,

Jens: dass der Output dann Millionen von Tokens waren.

Jens: Also ich hoffe auch im Prinzip, dass dann diese Loops natürlich auch viel effizienter

Jens: werden, dass man da Sachen einbauen kann, dass eben nicht die Maschine dumm

Jens: Tokens verbrennt, sondern auch da wird es dann, glaube ich, zu einem guten Loop

Jens: Engineering hören, dass man die,

Jens: nachhaltig effizient gestaltet und nicht einfach sagt, wie man es jetzt mal

Jens: eine Zeit lang irgendwie versucht hat von den großen Anbietern zu erzählen,

Jens: du bist es nur wert, wenn du auch Millionen und von Milliarden von Tokens verbraucht,

Jens: das auf deinem Weg, das stimmt ja nicht. Also auch da wird es glaube ich...

Mark: Hold my beer.

Jens: Dazu sollte es auch einfach kommen, dass man da im Prinzip mal,

Jens: also zum guten Loop-Engineering, zum guten Harness-Engineering,

Jens: wenn man das Memory noch baut, sollte es meiner Meinung nach auch gehören,

Jens: dass man da eben Token-optimiert arbeitet und nicht blind den Maschinen eine

Jens: Zeit lang vertraut, um weiterzulaufen.

Jens: Auch wenn sie es wahrscheinlich selber irgendwann auch ganz gut machen werden.

Jens: Das ist glaube ich per se momentan die Situation, dass wir sagen,

Jens: wenn wir gerade über ein Harness-Engineering reden, dann wird sich das auch

Jens: irgendwann relativ zügig in den Modellen finden. Die werden das auch schon selbstständig

Jens: ganz gut machen können. Und ja, ich bin da, glaube ich,

Jens: Wie immer, guter Dinge. Das war da,

Jens: also jeder sollte sich das Thema wieder angucken, der da Bock drauf hat,

Jens: baut mal eure eigenen Loops, schaut mal, was da schon funktioniert,

Jens: wie man übers Prompt hinausgehen kann in dem Moment mit den Tools der Wahl,

Jens: die einem zur Verfügung stehen. Da geht, glaube ich, schon relativ viel.

Jens: Und dass es die richtige Richtung ist, steht für mich auf jeden Fall außer Frage,

Jens: dass man da weg von dem, ich prompte einzeln, sondern ich konzentriere mich

Jens: eher auf ein Ergebnis und lasse die Maschine dann den Weg dahin bestreiten.

Mark: Ja, also von der Seite würde ich auch sagen, wir könnten es ja mal so machen, Jens.

Mark: Das Ziel, hört alle Folgen von uns.

Mark: Prüft, wenn ihr eine Folge gehört habt, ob es noch eine weitere Folge gibt,

Mark: die ihr noch nicht gehört habt.

Mark: Hört diese Folge wieder, prüft so lange, bis es keine weitere Folge mehr gibt.

Mark: Dann wartet ihr eine Woche und startet den Loop von neuem.

Mark: Und mit diesem kleinen Geschenk von Loop möchte ich mich heute bei euch verabschieden.

Mark: Und Jens, ich glaube, ich habe viel zu viel gesprochen.

Mark: Wir hätten über meine Abbruchregel vorher reden sollen.

Mark: Danke, dass du da warst. Danke, dass ihr da wart. Die Loop-Anweisung habt ihr

Mark: bekommen und schaltet das nächste Mal ein, wenn es wieder heißt. Think different.

Jens: Think AI.

Mark: Ciao.
