---
title: "Notion übernimmt"
episode_index: 41
published: "Mon, 25 May 2026 03:59:00 +0000"
duration: "3707"
page_url: "https://think-ai.podigee.io/43-notion-uebernimmt"
image_url: "https://images.podigee-cdn.net/0x,sXORXp3kUYGQwj_v7RxTK4j41nepmldGaZH1l-wx9_7M=/https://main.podigee-cdn.net/uploads/u73317/6b236be7-a14b-4011-bd7b-afb7436266b8.jpg"
audio_url: "https://audio.podigee-cdn.net/2497534-m-1e3bbe292560552329e00be3991c64db.mp3?source=feed"
guid: "7ece111323b0a7ccbf006d510c1daf18"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-05-26T10:13:14+00:00"
---

# Notion übernimmt

**Veröffentlicht:** Mon, 25 May 2026 03:59:00 +0000
**Dauer:** 3707
**Webplayer:** https://think-ai.podigee.io/43-notion-uebernimmt
**Cover:** https://images.podigee-cdn.net/0x,sXORXp3kUYGQwj_v7RxTK4j41nepmldGaZH1l-wx9_7M=/https://main.podigee-cdn.net/uploads/u73317/6b236be7-a14b-4011-bd7b-afb7436266b8.jpg
**Audio:** https://audio.podigee-cdn.net/2497534-m-1e3bbe292560552329e00be3991c64db.mp3?source=feed

## Beschreibung

Das Ende der Klebeband-Lösungen
Mark und Dirk Beckmann (GF Digitalagentur artundweise) sprechen darüber, was Worker, Managed Agents und die neue Offenheit für Unternehmen bedeuten, die KI ernsthaft einsetzen wollen.

Im Stil einer Apple-Keynote, vorab aufgezeichnet, ruhig vorgetragen und mit Folgen, die weit über „noch eine API" hinausgehen. Die beiden zentralen Bausteine: Worker und Managed Agents.

Worker sind kleine TypeScript-Programme, die auf der Notion-Plattform laufen. Geschrieben mit Hilfe von KI, ausgeführt deterministisch also ohne Tokenkosten, ohne Halluzinationen. Ein Agent in Notion kann diese Worker als Werkzeug nutzen. Damit lässt sich alles bauen, was man sonst mit n8n oder Make macht, aber im eigenen System.

Managed Agents von Anthropic können nun auch in Notion-Workflows eingebunden werden. Lange laufende Aufgaben, externe Trigger, abgekapselte Sandboxes ohne dass man selbst Infrastruktur betreiben muss.
Das Spannende: Notion verkauft eigentlich Tokens („we sell work"). Mit der Worker-Plattform öffnet sich das Unternehmen für lokale Modelle, eigene Skripte und externe Anbieter. Ein Schritt, der kurzfristig Umsatz kosten kann, langfristig aber die Plattform zementiert.

## Transkript

**[00:00:00]** Willkommen bei ThinkDifferent, ThinkAI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** Hadi zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:33]** Herzlich willkommen zu einer neuen Folge von Psyngtiffin Psyng AI.

**[00:00:37]** Der Jens wäre so gerne heute dabei, aber er macht irgendwie eine Tradition draus,

**[00:00:43]** dass wenn wir einen Gast haben, mit dem wir uns über Notion unterhalten,

**[00:00:47]** dass Jens irgendwie weg ist. Diesmal ist er nicht im Urlaub oder sowas,

**[00:00:51]** diesmal ist er krank. An dieser Stelle gute Besserung Jens.

**[00:00:53]** Jens und Hallo Dirk, schön, dass du wieder da bist. Es freut mich sehr, dass wir uns heute über

**[00:00:59]** Notion unterhalten. Und du glaubst gar nicht, wie ich mich freue, lieber Mark, dass ich über

**[00:01:04]** Notion reden darf. Ja, ja. Also, es ist ja tatsächlich so, in der Zwischenzeit habe ich immer

**[00:01:10]** mehr Menschen in meinem Umfeld, die mit Notion zu tun haben bzw. sich mit Notion beschäftigen,

**[00:01:18]** in ihren Firmen so ein bisschen am rumhören waren, wer von euch kennt den Notion, nutzt den Notion

**[00:01:25]** und je nach Firma findet du mal mehr, halt weniger, aber überall findest du Menschen, die Notion 1 sind.

**[00:01:32]** Und ich hatte ja in der letzten Folge schon mal gesagt, ne, Notion, das ist so ein bisschen damals

**[00:01:39]** da mir vorbeigegangen, bis dann, und du hast immer gesagt, mach Notion, du hast immer gesagt, mach Mac,

**[00:01:44]** Ja, mit Mac hab ich damals auch gesagt, hat es da recht, und mit Nautchen dann irgendwie auch.

**[00:01:48]** Das war ja dann hier Version 3, ne, als sie dann irgendwie anfingen, ordentliche KI reinzubringen.

**[00:01:53]** Und dann hatten wir uns auch im Podcast darüber unterhalten, was Nautchen bei dir alles so bringt und macht.

**[00:01:59]** Und einfach mal um ins kalte Wasser zu springen.

**[00:02:03]** Nautchen hat schon wieder was getan.

**[00:02:05]** Und da haben wir dann gesagt, lass uns doch mal spontan unterhalten.

**[00:02:08]** Was hat Nautchen denn gemacht?

**[00:02:11]** Ja, die haben eigentlich etwas gemacht, dass man lange nicht erwartet hätte. Sie haben sich wirklich für Entwickler und Entwicklerinnen geöffnet, haben also eine Notion-Developer-Plattform gelauncht, jetzt vor ein paar Tagen, so ganz im Stil von Apple mit vor-aufgezeichneten Keynote-artigen, also wie Apple der Neustart, wie Apple Leider, wie Apple der Neustart, wir mögen das ja beide nicht, wir wollen ja live was sehen, aber jetzt ist es halt so.

**[00:02:35]** Und so haben die es auch gemacht.

**[00:02:37]** Und Ivan Sao, der Chef, hat dann eingeleitet und gesagt, ja, wir haben jetzt eine richtige

**[00:02:41]** Developer-Plattform und das wichtigste Tool dort ist eben der Worker, also ein, technisch

**[00:02:47]** kannst du das nachher besser erklären, aber ein auf Notion-Plattform ablaufender Programmteil,

**[00:02:53]** den der sowohl auf Notion zugreifen kann nativ, auf alle möglichen Dinge über die

**[00:02:58]** API und auf den Notion wiederum zugreifen kann.

**[00:03:00]** Und das ist schon ein wirklich großer Schritt.

**[00:03:03]** weil es in der Alpha, in diesem Ambassador-Programme schon vorher publiziert und getestet, aber

**[00:03:08]** ich habe nicht so viel Ahnung von CLI-Programmierung und deswegen habe ich das eigentlich nicht

**[00:03:13]** gemacht, bis es jetzt gelangt war.

**[00:03:15]** Und jetzt bin ich auch schon total Feuer und Flamme.

**[00:03:18]** Wem, was ich an der E-Note oder an der Video-Aufzeichnung, Video-Aufzeichnung, Vorproduktion, ach, egal.

**[00:03:25]** Was ich da geschätzt habe, war tatsächlich auch dieses Ambiente, das Sie da gemacht

**[00:03:30]** haben, dunkler Raum, Holzstuhl, setz ich hin, erzählt mit einer Ruhe und Überzeugung,

**[00:03:37]** also nicht Ruhe in Form von Schlaftablette, sondern Ruhe in Form von man sich bewusst,

**[00:03:42]** was man hier gerade zeigt. Man interessiert wirklich auch die Wellerpaum, war sich bewusst,

**[00:03:47]** dass man damit quasi etwas Neues geht, sehr unaufgeregt, aber in dem, was sie gezeigt haben,

**[00:03:53]** wirkt das alles so, ich sag mal jetzt bin ich ja im Vergleich zu vielen anderen ja Neuling bei

**[00:04:01]** Notion, aber es wirkt so ein bisschen okay, wir zeigen jetzt auch mal allen die Notion haben,

**[00:04:06]** es gibt diese Entwicklergemeinde, dieses CLI, dieses keine Ahnung, was für Tools und das hast du

**[00:04:13]** vorhin schon das Thema Worker in Mund genommen und CLI, also CLI ist ja die Möglichkeit,

**[00:04:20]** dass wir quasi über Kommando-Zeile, Command Line Interface mit Sachen intervieren können. Wir

**[00:04:27]** kennen das schon vom Code, da gibt es eine CLI, wir kennen es vom Codex, da gibt es eine CLI. Die

**[00:04:33]** wenigsten Menschen im Alltag verlieren sich ja in ein Terminal-Fenster oder in ein, wie heißt das

**[00:04:41]** unter Windows, CMD, Kommando, ach keine Ahnung, Menschen, die in schwarzen Bildschirmen mit blinkendem

**[00:04:46]** Cursor sehen, wissen, was ich meine und die, die nicht wissen, was ein blinkender Cursor

**[00:04:50]** am schwarzen Bildschirm ist. Willkommen in der neuen Welt. Da haben Sie etwas vorgestellt

**[00:04:55]** und ich habe mir dieses Video auch angeschaut, nachdem du mir den Link nochmal geschickt hattest,

**[00:05:01]** noch als Vorbereitung für heute und ich versuche mal in meinen Worten zusammenzubringen, was

**[00:05:06]** sie uns dort zeigt haben. Weil sie haben, und ich habe davon einen ganz anderen Blick

**[00:05:10]** wie ein Gefächt drauf geguckt, etwas adressiert, wo ich mich immer gefragt habe, wie

**[00:05:14]** wird Nautchen mit diesen Problemen umgehen und ich möchte kurz ausholen, wenn du

**[00:05:18]** auf andere Hasher guckst du aus wie GitHub Co-Pilot und so, also Microsoft, dann erfährst du, dass die

**[00:05:25]** Talkenpreise durch die Decke geht. Sie haben neue Preismundelle angekündigt, Talken werden teurer,

**[00:05:29]** werden teurer, werden teurer, werden teurer. Und zwar nicht, weil neue Modelle kommen,

**[00:05:33]** sondern weil sie einfach anders verrechnen. Es gibt dann irgendwie keine Abo-Modelle mehr

**[00:05:37]** und so ein Kram für Enterprise-Kunden. Und jetzt adressiert ja Notion auch den

**[00:05:43]** ein Businessmarkt. Das ist sehr stark. Und da habe ich mich immer gefragt, wie will der

**[00:05:47]** Notion damit halten, weil, jetzt sind die nicht klein, aber die Kosten sind für die ja auch

**[00:05:53]** eine Herausforderung. Wie bleiben wir da preislich attraktiv? Und da zahlt, wie ich finde, auch

**[00:05:59]** das, was Sie jetzt mit diesem Worker vorgestellt haben. Ein, in meiner Wahrnehmung ist der

**[00:06:04]** Worker die Möglichkeit, Programmcode zu schreiben und diesem einen Agenten zur Verfügung

**[00:06:10]** zu stellen, dass er damit arbeiten kann, oder auch einem Saft für Entwickler zur Verfügung zu stellen.

**[00:06:14]** An Ocean unterscheidet ja irgendwie auch gar nicht so stark, ob ein Tool jetzt von einem

**[00:06:19]** Agenten genutzt wird oder schon im Menschen. Und man kann dann im Grunde, das nennt sich dann

**[00:06:24]** TypeScript, Programmiersprache, völlig Wumpe, ja, ist halt Programmiersprache,

**[00:06:28]** das sind Zeiten von KI, auch völlig Wumpe, welche Programmiersprache das ist. Grüße gehen

**[00:06:34]** an die Entwickler, die für mich arbeiten, da die steigen wir immer aufs Dach, wenn die

**[00:06:37]** einen Satsach. Aber lange wieder kurzer sind. Du programmierst da quasi mit Hilfe von KI

**[00:06:44]** kleine Code-Schnipsel. Dadurch, weil es Programmcode ist, brauchst du keine Tokenkosten, keine

**[00:06:50]** KI. Es ist verlässlich. Man nennt das ja dann Deterministisch. Und diese Code-Schnipsel

**[00:06:57]** lässt du dann bei Notion laufen. Und das hört sich jetzt nicht so erzählisch langweilig

**[00:07:06]** aber es ist gar nicht so langweilig, weil du kannst eben mit dieser Agenten-Plattform,

**[00:07:13]** die das ist ja das, was sie da vorvorgestellt haben, dass du also selbst ablaufende, selbstträgernde

**[00:07:19]** durch, durch, was auch immer du willst, Statuswechsel in einem Datensatz oder Urzeit oder was

**[00:07:24]** auch immer, mit diesen Agenten kannst du auf diese Worker zugreifen und jetzt kannst

**[00:07:28]** du dir halt ein ganzes Universum bauen. Du kannst dir halt ein Worker machen, der von mir

**[00:07:32]** aus auf dein lokal installiertes Mestral zugreift oder du kannst dir ein Worker machen, der

**[00:07:37]** wie du mir das jetzt am Wochenende erklärt hast, irgendwie keine Ahnung, e-mails irgendwo

**[00:07:41]** abruft und so weiter und so fort.

**[00:07:43]** Also alles das, was man vielleicht mit nacht n oder make oder saviour gemacht hat, kannst

**[00:07:47]** du damit machen, aber eben in diesem, sagen wir mal, für dich komplett unter Kontrolle

**[00:07:54]** befindlichen Umfeld und nicht noch mit einer Plattform und so weiter und so fort.

**[00:07:58]** Und du hast das einfach, klar, du musst Notion dafür nutzen, aber das willst

**[00:08:01]** du auch, du hast das halt in deinem System. Und das finde ich auch relativ krass, weil

**[00:08:06]** sie sich halt damit natürlich auch öffnen und das Geschäftsmodell, und das hattest du ja eben

**[00:08:10]** auch kurz angehoben, ihr eigenes nämlich Tokens zu verkaufen, so wie wir das jetzt alle machen,

**[00:08:14]** weil mit den Agenten wollen sie ja auch Credits verkaufen und verkaufen sie auch. Das ist ja

**[00:08:18]** auch nicht mehr per Abo, sondern da bezahlst du ja auch per Credits, also musst du halt 1000

**[00:08:23]** Credits, 10 Dollar zahlen und dann sind die halt wirklich, dann zahlst du wieder neues Geld.

**[00:08:27]** und obwohl das deren Geschäftsmodell ist und sie sagen großartig so ja wir verkaufen jetzt

**[00:08:32]** keine Software, wir verkaufen Arbeit, also we sell work in Form der Tokens und so weiter,

**[00:08:38]** machen sie sich, öffnen sie sich trotzdem und da finde ich sieht man daran,

**[00:08:43]** dass sie noch ganz schön viel vorhaben und nicht an dieser Stelle stehen bleiben,

**[00:08:46]** sondern sich dort jetzt einen kurzfristigen Erfolg vielleicht noch mehr Tokens zu verkaufen,

**[00:08:51]** verbauen, aber dafür eine ganz andere Gemeinschaft anlocken können.

**[00:08:55]** Und man darf auch nicht vergessen, jetzt bin ich vielleicht in so einer kleinen KI-Nerd-Blase,

**[00:09:01]** du in deiner Notion-Welt, aber nichtsdestotrotz, das, was du eben sagst, dass sie öffnen in sich,

**[00:09:08]** ist halt etwas, wo jetzt jeder denkt, der jetzt vielleicht Notion nicht können öffnen,

**[00:09:11]** wieso? Wo ist denn das Besondere? Es ist ja schon etwas Besonderes. Notion hat ja

**[00:09:15]** eine total tolle Art, wie sie Daten ablegen, mit Zellenseiten Daten banken und hast nicht

**[00:09:20]** gesehen und alles ist irgendwie gleich und ein Punkt, warum ich immer noch der Meinung bin,

**[00:09:24]** warum so ein Laden wie Microsoft das nie hinkriegt, weil Notion das halt von Grund auf richtig

**[00:09:30]** gemacht hat. Was das angeht. Ich glaube, die haben auch ein bisschen Lehrgeld gezahlt

**[00:09:34]** in der Vergangenheit, was Performance angeht oder dass man sich vielleicht auch mehr

**[00:09:38]** vergalopiert hat. Und jetzt haben sie halt die Möglichkeit, die Chance, wenn ich das

**[00:09:42]** so sagen darf, durch KI, ihre doch gute Datenablage und ihre gute Interaktionsmöglichkeit

**[00:09:49]** so anzureichern, dass sie halt viel einfacher, als die anderen haben,

**[00:09:54]** agentische Systeme zu integrieren, agentische Systeme arbeiten zu lassen und

**[00:09:58]** jetzt auch bei den Worker noch mal wegen dem Öffnen. Die Worker ermöglichen es mir ja nicht nur zu sagen,

**[00:10:05]** ich gucke jetzt nach, ob keine Ahnung, eine Mail in Gmail, du hast das Beispiel eben gebracht,

**[00:10:10]** da ist, sondern ich kann ja wirklich Interaktion machen und so nach dem Motto, ich gucke nach,

**[00:10:15]** Ich mache login, ich gucke nach ob mails da sind, ich kann gucken, ob bestimmte mails da sind, ich kann mails schreiben.

**[00:10:21]** Ich könnte noch in einer anderen Datenbank nachgucken, ich könnte noch andere Tools, ja, also das, was wir in der AI-Welt mit MCP anbindung, kannst du da auch alles da reinpacken und das Lustige ist, auch wenn ich von einem komischen TypeScript gesprochen habe.

**[00:10:36]** Dank KI ist uns das ja völlig Wumpe, was es ist, weil unter dem Strich kannst du die ja quasi singemäß von der KI wünschen, was der Worker tun soll.

**[00:10:44]** Das heißt, du hast da KI genutzt und ab dann wieder ein deterministisches System.

**[00:10:49]** Das finde ich wirklich total spannend, dass sie dieses Klebeband, das Ducktape dahin gezimmert haben.

**[00:10:57]** Hört sich immer so unprofessionell an, Ducktape, aber das ist ja in dem Sinne wirklich eine Besonderheit, die auch einfach ist.

**[00:11:05]** Was hast du dir gebaut mit dem Worker? Was war das, was wir uns da angeschaut haben?

**[00:11:09]** Also ich hab selber mir gebaut dieses, also da hab ich dann,

**[00:11:13]** bisschen umständlich mit Claude Code im,

**[00:11:15]** also nicht im CLI, sondern eben in diesem, mit dieser App, von Cloud MacOS App,

**[00:11:21]** Mistral,

**[00:11:22]** angebunden, dass lokal auf meinem,

**[00:11:24]** auf meinem MacBook

**[00:11:26]** 5M5 Pro läuft

**[00:11:28]** und nicht so richtig, was toll ist, kann, aber es war halt cool zu sehen, dass es

**[00:11:32]** einfach ohne Internet

**[00:11:33]** KI gibt.

**[00:11:34]** Hat zwar nur Trainingsdaten und er hat noch nicht die schnellste Version, aber

**[00:11:37]** Eine sehr gute Version, die schon läuft und das wollte ich halt mit Noten nutzen, wollte

**[00:11:41]** herausfinden, ob das geht und dann habe ich mir diesen Worker mit Lord gebaut.

**[00:11:44]** Aber was ich dann ein bisschen realistischer fand, war die Frage, die ich dir gestellt

**[00:11:48]** hatte, nämlich dass ich ein bestimmtes Gmail-Konto regelmäßig abfrage und da kommen wir dann

**[00:11:54]** auch schon zum ersten Modus, den es den diese Worker einnehmen kann.

**[00:11:58]** Das ist so ein richtig unterstützter, ja eigentlich proprietärer Modus, nämlich der

**[00:12:02]** sogenannte Sync.

**[00:12:03]** Und ich habe das überhaupt nicht geschneilt, dass das so ein Modus ist, dann hast

**[00:12:05]** mir irgendwie geschrieben, wie ich das in welcher Reihenfolge mache. Und dann habe

**[00:12:09]** ich das an diesem CLI auch tatsächlich gemacht, also in diesem Terminal immer alles eingegeben.

**[00:12:13]** Das hat super geklappt. Dann habe ich das Claude Code auf Terminal genutzt und nicht auf Desktop.

**[00:12:19]** Und das hat auch alles geklappt. Und jetzt habe ich einen Worker, der regelmäßig in dem Fall

**[00:12:25]** alle 15 Minuten guckt, auf einem Gmail-Postfach, was reinkommt. Und das Entscheidende ist jetzt,

**[00:12:30]** der legt dann, also der Worker legt initial die Datenbank an, Notion die Datenbank an,

**[00:12:37]** wo das reinkommen soll und definiert dann, was das ist, in dem Fall sind das 5, 6 Sync-Felder und

**[00:12:44]** die haben auch einen speziellen Titel, die sind sozusagen, weil sie eben aus einem externen

**[00:12:49]** Tool kommen, sind sie eben damit gesüngt und dann kannst du dir selber noch welche dazu machen,

**[00:12:53]** also wie man das kennt, aber das ist ein neuer, neuer Typ von, von Datenbankfeld, nämlich

**[00:12:58]** besündeter Typ und das kannst du jetzt beliebig weitreiben. Jetzt kann man den Worker dazu bringen, dass er dann in der anderen Datenmarkt was nachguckt und was

**[00:13:07]** verknüpft und so weiter. Das habe ich jetzt noch nicht gemacht, aber... Und sagen wir mal so mit einer Anleitung, die ich aber auch brauchte, weil ich bin ja, wie gesagt, kein

**[00:13:14]** richtiger Entwickler, sondern ich zähle mich dafür und mache mal irgendwie so Halbentwicklersachen. War das gut?

**[00:13:21]** Also die Anleitung, die du mir gemacht hast, war gut, aber die habe ich auch gebraucht. Klar, die war jetzt super auf

**[00:13:27]** meinen Fall speziell angelegt. Also ich konnte das einfach copy-pasted. Ich musste es nicht

**[00:13:31]** mal verstehen, was ich copy-pastete. Und ich war halt froh, dass das von dir kam und ich

**[00:13:36]** dachte mir, okay, du wirst mir das schon kein Scheiß reinbauen. Und gut, also das ist jetzt

**[00:13:39]** nicht ein securitymäßig, ist das jetzt nicht ein nacharmenswürdiges Vorgehen. Aber wenn der

**[00:13:45]** Cousin das macht, dann muss das ja irgendwie wohl funktionieren. Tatsächlich ist es für

**[00:13:49]** Nichtentwickler, finde ich, nicht so dieser Easygoing-Prozess mit diesem CLI-Ding. Da muss man

**[00:13:56]** ja diese ganzen die nomenklatur davon verstehen und so weiter da kann man sich durchfummeln das ist

**[00:14:01]** noch nicht super ideal aber es ist eben möglich selbst jetzt nicht entweder zu machen und letzter

**[00:14:05]** setz dazu notion versucht auch jetzt in ganz vielen kleinen videos und auf der developer plattform die

**[00:14:11]** ureigendsten notion leute quasi noch mitzunehmen denn viele werden diesen weg nicht gehen weil

**[00:14:16]** die sehen dieses komische bringende cursor teil und sagen nee dann mache ich das meine ich

**[00:14:20]** dann mache ich lieber wieder nacht n so also das ist auch schon eine kleine hörde aber

**[00:14:24]** Aber gut, du hast natürlich ganz andere Möglichkeiten.

**[00:14:27]** Weil ich erzähle, was ich mit dem Workout gemacht habe.

**[00:14:29]** Vielleicht zwei Sachen, weil, wie Sie eben erwähnt haben,

**[00:14:32]** erstens, N8N Grüße gehen an die SAP, die irgendwie

**[00:14:35]** eine Partnerschaftkooperation, Anteilnahme,

**[00:14:38]** irgendwas jetzt kundgetan haben nach dem Motto

**[00:14:40]** zukünftige Prozesse von SAP,

**[00:14:43]** wird mit N8N unterstützt, wo ich mir dachte.

**[00:14:47]** Ja, okay. Also, ehrlicherweise für N8N

**[00:14:50]** würde ich persönlich ja nicht mehr so viel,

**[00:14:52]** ist das für SAP gut, aber die Hämme sei da hingestellt.

**[00:14:57]** Ne, bei N8n gibt es ja auch sowas wie Make, hast du ja auch erwähnt gehabt, dass du das

**[00:15:01]** nutzt, Make.

**[00:15:02]** Und die haben jetzt ja auch eine CLI angekündigt, also, oder beziehungsweise veröffentlicht.

**[00:15:06]** Von der Seite scheint das ja schon durchaus etwas zu sein.

**[00:15:10]** Wenn ich überlege, als ich mit der IT angefangen habe, haben wir mit Textbildschirmen gearbeitet.

**[00:15:16]** Dann haben wir gefeiert, dass wir eine UI kriegen, sei es Geos auf MS-DOS gewesen oder Windows.

**[00:15:24]** Und jetzt, was machen wir?

**[00:15:26]** Jetzt auf einmal hängen wir alle wieder in Textfenster im Terminal rum.

**[00:15:29]** Und ich brauche eigentlich, ich muss auch ganz ehrlich sagen,

**[00:15:32]** alle, die ich hier von Apple und so weiter kenne, es tut mir leid,

**[00:15:35]** ich hänge mehr im Textfenster rum als irgendwie in der grafischen Benutzeroberfläche

**[00:15:39]** und finde es gerade gar nicht so schlimm.

**[00:15:41]** Mal gucken, ob da nicht irgendwann wieder was Hübsches kommt,

**[00:15:43]** aber die Entwicklerkonferenzen kommen bald.

**[00:15:45]** Jetzt habe ich gesagt, mal erzählen, was ich als Worker ins Rennen werfen kann.

**[00:15:50]** Kein Mistral, sondern Hacking-Field.

**[00:15:55]** Nee, Hacking-Face, Hacking-Face, die kommen immer durcheinander.

**[00:15:56]** Hacking-Face, Hacking-Face, kannst du vereinfachter ausgedrückt, K.I.-Modelle beziehen und lokal ausführen.

**[00:16:04]** Zum Beispiel Bildgeneratoren, Videogeneratoren, Voice-Cloning.

**[00:16:08]** Und ich habe mir einen Worker gebaut, der mir Bilder baut.

**[00:16:13]** habe mir einen Worker gebaut, der mir Podcasts erstellt aus Texten in Notion. Und du hast

**[00:16:23]** halt den Notion dann deinen Kram und dann gibst du dem Agenten den Worker in die Hand

**[00:16:28]** und dann macht der Agent mit dem Worker dir ein Audio-File mit deiner Stimme und

**[00:16:34]** alles lokal. Und die weiß ohne irgendwie Cloud. Und das ist schon, das ist schon nett,

**[00:16:40]** Ja, also ich kann auch einen M5 MacBook, ja, wir sind ja die Freunde des Notions und das

**[00:16:45]** Apple, das haben wir ja schon zum Besten gegeben, und dann stehst du da und denkst dir, okay,

**[00:16:51]** es braucht vielleicht alles ein bisschen länger als bei 11 Labs oder Nano Banana, aber ich

**[00:16:57]** würde sagen, dafür, dass es mich weder tokens, ne, es kostet mich keine Tokens und

**[00:17:04]** es ist quasi einfach im Hintergrund gemacht, ist das schon sehr faszinierend, wenn

**[00:17:10]** du dir überlegst, okay, vorher konnte ich das mit Notion so nicht tun. Ich konnte es

**[00:17:14]** zwar vorher auch mit anderen KI-System tun, ja, ich meine mein drittliebstes Hobby oder

**[00:17:19]** so, sind ja Skills in Claude Code und so. Aber das war schon beeindruckend zu sehen und dann

**[00:17:25]** habe ich mir auch gedacht, wenn du jetzt jemand bist, der seine Firma in Notion hat, der,

**[00:17:33]** ich sag mal, im kreativen Unvertätiges. Wer könnte das sein, ja. Wer könnte das sein,

**[00:17:38]** weiß ich nicht. Und dann verbindest du das und kriegst im Grunde, also ich will das nicht sagen, dass man damit alles automatisieren kann oder nicht, ja, aber du hast diese Werkzeuge für Menschen im Zugriff, die das vielleicht mit einem Blick für Kreativität und Ästhetik bedienen können und kriegen dann in dem System, in ihrem Betriebssystem, in ihrem, was auch immer, manausch nennen möchte, diese Module, diese Artifakte, diese Ergebnisse da,

**[00:18:08]** geboten und das ist ja nur die Spitze des Eisbergs. Ja, das ist ja die Spitze des Eisbergs.

**[00:18:14]** Nur mal kurz um das zu verstehen. Also das Hackingface ist ein Anbieter der macht,

**[00:18:21]** dass irgendein von diesen ganzen Modellen so wie… Du kannst da ein Abo abschließen.

**[00:18:25]** Nein, nein, nein. Das sind eigene Modelle. Das sind ganz eigene Modelle,

**[00:18:29]** die du bei Hackingface konsumieren kannst. Da gibt es dann auch hier mit Abo und kostenlos und

**[00:18:35]** kommerziell frei und kommerziell gegen Geld. Da gibt es ganz viele verschiedene Sachen. Das Lustige

**[00:18:40]** ist aber, dass du dort beispielsweise auch Modelle kriegst. Also letztens habe ich mir ein Modell

**[00:18:45]** von Microsoft runtergeladen, da kannst du Audio-Dateien reinschmeißen und der macht dann

**[00:18:51]** Personenerkennung und Transkription auf das Audio-File. Und das lässt du dann halt auf

**[00:18:56]** deiner Büchse lokal laufen, was natürlich sehr viel günstiger ist, als wenn du das sagst,

**[00:19:01]** zuhause das gegen Cloud-Modelle und war es natürlich jetzt mit so etwas wie Worker dann

**[00:19:06]** auch einfach zu integrieren ist. Also dieses Hacking-Face-Ding, das mir den Podcast generiert,

**[00:19:13]** das war irgendwie keine halbe Stunde und dann war es up and running, das ist schon lustig.

**[00:19:18]** Dann kann ich das ganz normal, als der Agent vermittelt dann jetzt zwischen Notion und

**[00:19:23]** dem Worker und dem Agenten, den rufe ich auf und dann habe ich dieses Tool. Und

**[00:19:28]** Das Tool läuft dann auf meinem Rechner und wenn ich das jetzt deployen will, also wenn

**[00:19:34]** das jetzt andere Leute nutzen sollen, dann müssen wir sich das überlegen auf welchem Rechner

**[00:19:38]** das läuft.

**[00:19:39]** Genau, dann muss es halt auf einem anderen, muss es halt, wie man das so sagt, müsste

**[00:19:43]** dann auf einem anderen Rechner laufen, was für mich jetzt für meine Workflows ganz

**[00:19:48]** in Ordnung ist, dass es bei mir ist.

**[00:19:50]** Ich hatte ja vielleicht auch nicht jeder irgendwie einen M5.

**[00:19:54]** Bitte.

**[00:19:55]** egal ob Pro Max sonst warst, du brauchst schon ein bisschen Ram, du brauchst schon ein bisschen

**[00:20:01]** jetzt nicht CPU, sondern Grafikkarte oder KI-Beschleuniger wie bei Apple in den Prozessoren drin.

**[00:20:07]** Ich weiß nicht, wenn man sich von Nvidia so eine DJI Spark holt, so einen Kasten, den

**[00:20:13]** du ins Büro stellen kannst und von deinem Fernsehen ansprechen kannst, wie das müsste

**[00:20:17]** eigentlich damit auch wunderbar gehen, weil der Worker kriegt ja auch nur gesagt,

**[00:20:21]** da liegt das Zeug, sprecht das Modell an und dann liegt das Modell halt dort. Also das

**[00:20:26]** sollte kein Problem sein, das wird auch kein Problem sein, ich habe es halt nur noch nicht

**[00:20:31]** gemacht. Und diese Modelle, die dieses Haging Face kriegt zur Verfügung stellt, das sind

**[00:20:38]** eben so Modelle, die zum Teil eben auch andere, wie zum Beispiel Ulama oder, also das ist

**[00:20:44]** so ähnlich oder was ist das Besondere, weil sonst habe ich den Unterschied noch nicht

**[00:20:47]** verstanden. Ulama ist ja ein Sprachmodell, also da kannst

**[00:20:50]** Sprachmodelle reinhängen, dass du Textchat machst. Und die Modelle, die du jetzt bei Hackingface

**[00:20:55]** kriegst, sind nicht darauf spezialisiert generative AI zu machen, im Form von, ich sage, schreib

**[00:21:01]** mir ein Gedicht über den Eiffelturm, sondern multimodale Modelle, generiere mir Videos,

**[00:21:06]** analysiere mir Videos, mach okay. Das ist im Prinzip das Gleiche, das eine ist nur

**[00:21:11]** für textbasierte Geschichten. Ja, okay. So können wir uns, glaube ich, dann verstehe

**[00:21:15]** ich es. Und das heißt, du hast jetzt aber dieses Hackingface angebunden und kannst

**[00:21:19]** jetzt irgendwie alle möglichen Modelle nutzen in dem Worker.

**[00:21:23]** Du kannst von Hackingface die Stellen dann Modelle zur Verfügung sagen, mit welchen

**[00:21:28]** Laufzeit-Umgebungen diese Modelle funktionieren. Nicht alles geht auf eine

**[00:21:34]** Mac, manches braucht wirklich ein Nvidia, manches läuft nur auf

**[00:21:38]** Nvidia nicht auf dem Mac, manches nur auf dem Mac, nicht auf Nvidia, manches überall.

**[00:21:42]** Manche Modelle sind schlecht, manches sind gut, ist ein riesiges Angebot, muss man

**[00:21:46]** noch ein bisschen gucken, was gerade, ich sage jetzt mal gerade Aktuelles. Grundsätzlich würde

**[00:21:51]** ich sagen, sind die Fotovideo und Audiumodelle sehr nah an dem, was du daraus mal mag kriegst,

**[00:21:58]** also Voice Cloning, der braucht 15 Sekunden meiner lieblichen Stimme und kann mich sehr gut

**[00:22:05]** nachmachen in verschiedenen Sprachen. Und das ist schon, also ich muss gucken, wie das Modell

**[00:22:13]** hieß. Hacking Face ist ja nur die Darreichungsform und das Modell selbst

**[00:22:18]** müssen wir mal raushoben. Aber es lohnt sich durchaus dahin zu gucken, weil, ja,

**[00:22:23]** ich kann mich nur wiederholen. Es kostet dich keine Token, du hast keinen

**[00:22:26]** Datenschutz, sonst wars Thema, weil es einfach bei dir auf der Büchse läuft.

**[00:22:29]** Du brauchst halt nur in Anführungszeichen eine Büchse mit ein bisschen

**[00:22:32]** Ram und ein bisschen Muckis, die dann diese Modelle ausführt und ich gebe

**[00:22:38]** auch zu, ich merke, dass es läuft, weil bei mir geht dann durchaus auch mal

**[00:22:41]** der Lüftern. Dem, was du laufen lässt, ist das durchaus hörbar.

**[00:22:48]** Na ja, und ich meine, was für unsere Zielgruppe sozusagen als Firma wichtig ist, viele mittelständischen

**[00:22:57]** Firmen in Deutschland sind natürlich auch darauf angewiesen, dass es eben auch unamerikanische

**[00:23:03]** Modelle gehen muss. Also dies und das, also die haben ja zum Teil relativ restriktive

**[00:23:08]** Auflagen, wie sie sich selbst gegeben oder müssen die einhalten, auch gerade wenn du daran denkst, dass dann, dass die Zulieferer sind, vielleicht auch für

**[00:23:17]** High-Tech Firmen und so weiter. Und die sagen halt, okay, bitte, was ist denn jetzt mein Weg, wenn ich diese ganzen tollen amerikanischen Modelle nicht nutzen darf?

**[00:23:26]** Und dafür ist es natürlich toll. Vor allem ist es toll, du kannst im Enterprise-Programm, nur schon eben auch in Frankfurt

**[00:23:31]** gehostet haben und dann hast du irgendwie noch irgendwo installiert auf deinem Rechner, was auch immer für Infrastruktur nötig ist.

**[00:23:39]** Dann hast du dann so ein Modell, das dir vielleicht Bilder macht oder was auch immer, was du gerade sagst.

**[00:23:43]** Und dann hast du auf einmal eine Lösung und das war vor ein paar Tagen eben undenkbar, genau dieses Szenario und viele, viele andere.

**[00:23:51]** Und dadurch wird es natürlich offener und wird noch mehr zu dieser KI-Plattform so ein bisschen.

**[00:23:58]** Wenn du das jetzt von so einer Nutzerinnsicht siehst, dann kannst du eigentlich sagen,

**[00:24:02]** okay, wenn dir das jemand so ein bisschen einrichtet, wenn du selber keinen Lust hast,

**[00:24:07]** dann übernimmt das eben so eine Firma wie wir oder irgendeine andere Firma, dann kannst

**[00:24:11]** du dort direkt diese ganze, hast du direkt Zugang zu dieser ganzen tollen KI-Welt,

**[00:24:16]** also ohne dich auch nur ein bisschen damit zu beschäftigen.

**[00:24:19]** Und wenn du dann den Wunsch hast, ein lokal installiertes Graphic-Tool,

**[00:24:25]** also ein Modell für Grafikerstellung zu nutzen, dann geht das jetzt auf einmal. Das heißt,

**[00:24:30]** es ist so, das ist zwar nur technisch gesehen vielleicht nur ein kleiner Schritt, aber die

**[00:24:34]** Möglichkeiten sind jetzt quasi nicht mehr begrenzt und vorher warst du eben am Ende. Du musst

**[00:24:38]** das halt sagen, ja, wenn du mit Norrish und KI machen willst, dann wirst du immer diese

**[00:24:42]** amerikanischen Modelle nutzen müssen, sonst geht es halt nicht so. Sie ergänzen nativ auch immer

**[00:24:47]** mehr, auch kleine Modelle. Ich glaube, Diepsi kann sie jetzt auch irgendeine Version mit drin

**[00:24:52]** Und das werden sie auch immer weiter machen, weil die Token kosten natürlich sonst immer

**[00:24:55]** nur total hoch sind.

**[00:24:56]** Aber dass es halt jetzt in diesem Moment geht, dass du das gebaut hast, macht natürlich den

**[00:25:01]** großen Unterschied.

**[00:25:02]** Und egal, wo ich gerade hinkomme, die ganzen Firmen, die ganzen mittelständischen Firmen,

**[00:25:07]** die wollen eine Lösung für KI, jetzt gerade Marketing, wo wir unterwegs sind, die eben

**[00:25:13]** immer auch ein bisschen nach Alternativen schielt und nicht immer sagt, okay, Cloud

**[00:25:17]** Code installieren oder Cloud Installieren fertig, obwohl das natürlich irgendwie das

**[00:25:20]** Du hältst das, was es gerade gibt, aber sie dürfen dann eben nicht oder es ist ihnen zu teuer oder was auch immer für das Direktion.

**[00:25:26]** Insofern, das ist schon echt krass.

**[00:25:28]** Und du warst dabei.

**[00:25:30]** Hacking Face.

**[00:25:31]** Jetzt habe ich es endlich richtig über die Lippen.

**[00:25:32]** Was du halt hast, ist halt wirklich, dass du das, was du ihm sagt, dass man, du bittest den Menschen die Möglichkeit.

**[00:25:37]** Es ist zwar ein amerikanisches Modell unter Umständen, das aber dann bei dir läuft.

**[00:25:42]** Vielleicht ist das nochmal von der Feinheit, nochmal zu erwähnen.

**[00:25:45]** Stimmt.

**[00:25:45]** Aber du kannst halt wirklich Video zu Text, Text zu Video, Audio zu Text, Text zu Audio,

**[00:25:50]** Aufstieg der Erkennung in Bildern, Verständnis von Bildern, Bildzerlegung, Bildbearbeitung.

**[00:25:56]** Teilen, ich schicke ein Bild hin und du kriegst es in Fotoshop-Ebenen zurück.

**[00:26:02]** Mit Ausrechnen, was quasi da ist, wenn du die Ebene wegziehst, dass da nicht eine Lücke ist,

**[00:26:08]** weil der Dirk jetzt gerade die Kamera guckt und ich ziehe die Ebene des Dirk weg, dann ist dahinter,

**[00:26:13]** ist, was er der Meinung ist, was da reingerechnet gehört. Also, da sind schon echt tolle Sachen drin.

**[00:26:19]** Und eben, weil du es gesagt hast, hier Claude Cote, wäre so, ich sag mal das maß der Dinge,

**[00:26:25]** das ist ja auch so ein stetig tränender Kreis. Also es gibt dann Grok und dann gibt es Anthropic und

**[00:26:31]** dann gibt es, die geben sich alle nix und jeder bringt ein neues Modell raus. Vielleicht an

**[00:26:36]** der Stelle noch der Hinweis, du hast ja eben auch von Mestral gesprochen. Du kannst dir auch

**[00:26:41]** lokal auf deinem rechner modelle installieren sei es mistral sei es quen sei es

**[00:26:48]** gell ja genau genau und du kannst die auch wieder gegen clotcode koppeln also

**[00:26:55]** gegen dieses cli von anthropic kannst du gehen und sagen okay wir nehmen jetzt

**[00:27:00]** nicht die opost modelle von anthropic usa wir nehmen auch nicht die anthropic

**[00:27:06]** modelle die vielleicht bei amazon bedrock in der eu 200 frankfurt gehostet

**[00:27:11]** werden, sondern ich laufe gegen ein Modell, das liegt bei mir unten im Keller oder bei

**[00:27:16]** mir auf dem Notebook und codiere damit, habe aber trotzdem dieses CLI, Code im Zugriff und

**[00:27:23]** seit allerneuestem kannst du sogar Co-Work, also die App, von der du eben sprachst, die

**[00:27:30]** Mac App, die gibt es als Co-Work 3P heißt die, glaube ich, und du kannst die so konfigurieren

**[00:27:37]** dass auch die gegen andere Modelle läuft. Dass du sagst, okay, ich habe jetzt hier lokal mein Quen,

**[00:27:44]** dann gibt es so einen sogenannten Proxy, ist jetzt nicht in drei Sekunden erklärt, aber es gibt

**[00:27:50]** Anleitung im Netz und es wird auch von Anthropic unterstützt. Die erklären das auch in ihren

**[00:27:55]** entsprechenden Dokumenten und dann kannst du selbst das Ding gegen lokale Modelle laufen lassen.

**[00:28:00]** Allerdings natürlich wird dann auch nicht alles ganz genauso funktionieren, wie man es

**[00:28:05]** vielleicht mit den Anthropic-Modellen in der Cloud hat. Aber auch hier merkt man die Hersteller,

**[00:28:10]** ich will jetzt nicht sagen, topidieren ein eigenes Geschäftsmodell, aber so wie Notion sagt,

**[00:28:17]** naja gut, wir wollen zwar Arbeit verkaufen, aber hier ist eine alternative günstigere Lösung,

**[00:28:22]** kommt auf einmal Anthropic um die Ecke und sagt, du findest unser CLI gut,

**[00:28:26]** du findest unsere Anwendung gut, ja, du kannst auch etwas anderes hinten dran nehmen. Das ist

**[00:28:30]** ist so ein bisschen, die tun sich auch alle gegenseitig, glaube ich, so gerne ein bisschen

**[00:28:34]** weh.

**[00:28:35]** Ja, und versteht man den Markt?

**[00:28:37]** Genau, und wenn du überlegst, was die alle, also jetzt, es gibt ja die einen, die wirklich

**[00:28:42]** investieren und investieren in die, in Modelle und Modelle rausbringen wie in Anthropic oder

**[00:28:48]** Google und so weiter und da gibt es die anderen, die das nutzen, nämlich so wie Apple das

**[00:28:52]** jetzt auch tun wird, die haben wesentlichen einfach nur irgendwas nutzen oder wie eben

**[00:28:55]** Notion das macht. Und ich finde, was ich an dem Weg von Notion besonders gut finde, auch wenn

**[00:29:02]** der, das noch weit entfernt ist von der Kapazität von Claude, ist, es ist halt eben AI Agnostic,

**[00:29:10]** sagt er. Also es ist egal, welches Modell du am Ende, welches Modell sich am Ende durchsetzt,

**[00:29:16]** die ganzen Infrastruktur. Wo hast du deine Proms, wie baust du deine Skills und deine

**[00:29:21]** Factories und wie setzt du das alles zusammen? Das hast du halt laufen und irgendwann kommt

**[00:29:26]** morgen Gemini mit dem dann doch wiederum Toilsten und dann schaltest du einfach unten nur um oder

**[00:29:32]** du nimmst eben diese Worker und hast die bei dir lokal laufen. Das heißt die Wahrscheinlichkeit,

**[00:29:37]** dass du diese Abstraktions, also die Wahrscheinlichkeit, dass es sich lohnt,

**[00:29:43]** in diese Abstraktionsplattform oder Ebene zu investieren, so wie wir das jetzt machen

**[00:29:49]** mit Notion, dass das wirklich gut ausgeht, glaube ich, ist relativ hoch, weil alles bleibt für dich

**[00:29:54]** gleich und dahinter rackert dann halt irgendein anderer Agent rum. Das bringt uns ja auch zum

**[00:29:58]** Thema, was passiert eigentlich? Das ist ja ein weiterer Worker-Teil, den die mitgebracht haben,

**[00:30:04]** der ist jetzt leider auch noch nicht für Ambassadors, zumindest nicht für mich testbar,

**[00:30:08]** aber es angekündigt nämlich, dass du diese irgendwie, das musst du mir auch noch erklären,

**[00:30:14]** irgendwie von, von Claude zum Beispiel, gehosteten Agenten nutzen kannst. Also, dass du sagen, explizit in

**[00:30:20]** diesem Worker sagen kannst, okay, das soll gar kein KI-Dings-Agent von Notion machen, sondern

**[00:30:27]** irgendein anderer Agent, der irgendwo gehostet ist und der soll jetzt halt diese Arbeit machen. Und

**[00:30:33]** das fand ich dann, als das dann noch irgendwie erzählt wurde, hab ich da gedacht, ja, okay,

**[00:30:36]** dann gibt's auch kein Nachteil mehr, alles in Notion zu haben, also im ganzen Kontext,

**[00:30:41]** den ganzen Inhalte, das ganze Betriebssystem tatsächlich, buchstäblich, Betriebssystem,

**[00:30:47]** also wie es bei uns ist, weil ich kann dann ja noch ein bisschen warten und dann ist es so weit,

**[00:30:52]** eben halt auf diese externen Agenten zugreifen. Ich muss kurz erzählen, ich weiß nicht,

**[00:30:56]** dass du im Video gesehen hast, du hast dann so ein Kanban Board und dann machst du ein Statuswechsel

**[00:31:00]** von, was ist ich, human in the loop, sag ich jetzt mal, gib frei, ne, Freigabe und dann kommt

**[00:31:06]** eine kleine Animation wie irgendein externer Worker mit so einem kleinen Icon und so einem

**[00:31:11]** kleinen Bewegungs-Animation an diesem Task arbeitet. Und wenn er dann fertig ist, gibt's

**[00:31:17]** dann irgendwie einen Haken. Das heißt, du siehst auf dein To-Do-Manager, also da arbeitet

**[00:31:22]** jetzt mein Kollege, der Claude Agent, irgendwo dran. Und das ist echt gut gemacht. Also

**[00:31:28]** das fand ich sehr beeindruckend. Anthropic hat das, was du beschrieben hast von

**[00:31:35]** gewissen Zeit angekündigt und hatte bei der Ankündigung erwähnt, dass Notion einer der

**[00:31:41]** ersten ist, die das mit unterstützen und du kannst bei Anthropic quasi Cloud Infrastruktur von

**[00:31:48]** Anthropic nutzen, in denen dann von dir gebaute KI-Agenten laufen. Also das ist jetzt nicht,

**[00:31:56]** dass du da was programmierst, im deterministischen Sinne, wie die Worker selbst,

**[00:32:01]** wo du TypeScript schreibst und er wirklich eins plus eins gleich zwei macht,

**[00:32:06]** sondern du kannst da quasi mit Skills und Proms und MCPs Sachen zusammenbauen,

**[00:32:12]** die dann je nachdem auf Events reagieren und dann sinngemäß arbeiten, wenn sie benötigt werden.

**[00:32:23]** Und der Vorteil ist, es sind halt wirklich klein abgekapselte, in sich getrunken, was heißt

**[00:32:31]** klein, kleines Werten.

**[00:32:32]** Es sind in sich abgekapselte Themengebiete, die dann zu der Zeit das tun, was man halt

**[00:32:38]** von ihnen will, die quasi jederzeit parat stehen.

**[00:32:42]** Bei Anthropic gibt es für die Berechnung die üblichen Tokenpreise plus einen ganz

**[00:32:49]** kleinen Opulus, den man auf den Top bezahlen muss. Anthropic betreibt diese Infrastruktur auch

**[00:32:55]** mit ganz speziellen Sandboxen, also dass das Ding nicht ausbricht, dass der nicht Amok läuft

**[00:33:03]** und dir 5 Millionen Euro kostenverursacht, obwohl er einfach nur das Wetter lesen sollte,

**[00:33:08]** dass er nicht, weil du im Zugriff gibst, dein Postfach lehrt. Es soll ja so Fälle

**[00:33:12]** gegeben haben, dass eine KI, die wir heute schon mal genannt haben, eine Produktionsdatenbank

**[00:33:18]** gelöscht hat und danach gesagt hat, das war ich nicht. Nein, nein, das musst du gewesen sein.

**[00:33:22]** Ich war das nicht. Dass solche Dinge halt nicht passieren. Und das Schöne daran ist halt schlicht und

**[00:33:28]** ergreifend, du musst dir nicht die Frage stellen, so wie wir es jetzt eben bei den Bild- und

**[00:33:34]** Ton- und Video-Agenten hatten. Wo stelle ich mein Server hin? Wie mache ich die Anmeldung?

**[00:33:40]** Wie sorg ich dafür, dass das Ding gewartet wird? Wie sorg ich dafür, dass das Ding sicher ist?

**[00:33:45]** sondern du kriegst in dem Sinne, ja, remote laufende Agenten, die nicht Programmcode,

**[00:33:53]** sondern Promts ausführen für dich, weil du sie antrickerst.

**[00:33:59]** Soweit ich das mitgekriegt habe, musst du sie immer antriggern.

**[00:34:05]** Ich habe noch nicht mitbekommen, dass sie so ein eigenes Timing-Intervall haben,

**[00:34:10]** so nach dem Motto, alle Stunde, sondern du musst dann quasi alle Stunden einen Prüchter hinschicken,

**[00:34:14]** schicken, damit das Ding wach wird und sagt, hallo, ich mach was. Aber das wäre dann wahrscheinlich

**[00:34:18]** so die nächste coole Ergänzung, wenn ich mir überlege, du baust irgendwelche Mail-Abrufe

**[00:34:25]** einerseits mit Worker und Agent in Notion und gehst auf der anderen Seite hin und sagst,

**[00:34:31]** so, ich hab hier ein paar Sachen eingetragen und mein Rechercheskill, der Details rausholen

**[00:34:39]** soll, so wie per Plexity nur nachgebaut, läuft dann unter Umständen, dort macht Faktencheck

**[00:34:45]** und Qualitätsprüfung und Aufbereitung. Du kannst so Agenten ja auch sagen, wie sie

**[00:34:50]** antworten sollen, welchem Datei-Format du das gerne hättest, also Formatierung, also

**[00:34:55]** immer eine Überschrift und ein Rundüberschrift und bitte alles mit Komma getrennt und keine

**[00:35:00]** Ahnung was. Und das würde ich schon behaupten, würde das Bild nochmal ordentlich abrunden,

**[00:35:07]** weil so kriegst du ja auch die nicht deterministische Welt da rein automatisiert.

**[00:35:12]** Aber was ich nicht verstehe ist, also ich kann aus Notion heraus ja ein Opus 4.7 nutzen und

**[00:35:19]** nehmen wir mal in der Output ist nicht eine Datei, sondern der Output ist irgendein Text,

**[00:35:24]** also irgendwas, Textarbeit, Bilder, so, also das kann ja Notion nativ. Was ist der Vorteil,

**[00:35:30]** dann einen Cloud-Agenten in der Cloud zu nutzen. Also, was kann das dann anderes, wenn

**[00:35:39]** man kurz das Teilformat eben weglassen? Weißt du, was ich mein? Also, warum sollte ich dann einen

**[00:35:44]** Agenten extern haben? Ich finde das auch erstmal toll, weil ich denke mir, die Welt nutzt halt

**[00:35:49]** Cloud und auch Notion, aber das kann man jetzt zusammenbringen, das habe ich verstanden. Aber

**[00:35:53]** warum sollte ich das tun, wenn ich mich entscheiden kann? Gibt es irgendein Vorteil,

**[00:35:57]** das Cloud 4.0, also den Opus oder was auch immer davon, nativ aus Cloud herauszunutzen anstatt

**[00:36:04]** aus Noten.

**[00:36:05]** Du kannst halt Arbeitsschritte auskliegen und es in Rechnern selten muss.

**[00:36:09]** Also wenn ich jetzt keine Ahnung, ich mache Software und jetzt checke ich Software auf

**[00:36:13]** GitHub ein, so aus Code Verwaltung und ich möchte mir das jetzt dokumentieren lassen.

**[00:36:18]** Werte mir das aus, mache mir dazu einen Onboarding-Dokument oder einen, was ist

**[00:36:23]** bisher geschehene Dokument oder keine Ahnung, was, dann kann ich das mit GitHub Actions

**[00:36:26]** machen. Also das Github-Aktionen ausführt, das kann statischer Code sein, das kann der

**[00:36:32]** Aufruf von KI sein und wenn es ein öffentliches Githubprojekt ist, kostet mich das nix, wenn

**[00:36:38]** es ein privates Githubprojekt ist, muss ich da Geld zahlen. Und solche Dinge kannst du

**[00:36:42]** dann halt schon Anthropic machen lassen. Der tut quasi was mit Dingen, die online erreichbar

**[00:36:49]** sind, ohne dass du dein Rechner aufhaben musst. Damit sticht und ergreifen, KI dann auch dann

**[00:36:57]** funktioniert, wenn alle um dich herum aufleihen sind. Dass wenn du, keine Ahnung, ob das

**[00:37:03]** jetzt ein Case ist, ja, der Kunde drückt auf ein Feedback-Formular auf hier, ich schicke

**[00:37:09]** da mal meine Issues weg und das Ding wertet das schon mal, vor ist er da und schicke

**[00:37:16]** den Antwort zurück. Das würde der Agent in Notion auch tun, wenn

**[00:37:21]** der Recher zu ist. Ja, nur, dass der Agent in Notion existiert und Anthropic auch

**[00:37:26]** noch andere Kunden als Notion hat. Anthropic hat ja auch Anwender, die nicht nur...

**[00:37:32]** Nicht mein Andersrum. Also die Möglichkeit, die jetzt seit der

**[00:37:36]** Entwicklung oder Bekanntgabe der Notion Developer-Plattform entsteht, oder die

**[00:37:41]** demnächst da ist, ist ja, dass sich externe Agenten, so wie du es

**[00:37:44]** beschrieben hast, in Notion integriert nutzen kann. Da muss ich keine nichts

**[00:37:49]** programmieren, das kann ich einfach in irgendeiner Form konfigurieren und dann

**[00:37:52]** geht das. Und in dieser Demo sah man, ich bin in so einem Task und dieser

**[00:37:57]** Task hat vielleicht vom Kunden eine Information auf unserer

**[00:38:01]** Startseite steht irgendwie noch das alte Produkt und die alte

**[00:38:07]** Produktabbildung, bitte tauscht das aus und dann kann das irgendwie weitergegeben

**[00:38:10]** werden an diesen externen Agenten und der würde das dann tun, er würde den

**[00:38:14]** Code auschecken. Von dieser Startseite würde das ändern und wieder einchecken. Das verstehe

**[00:38:18]** ich. Was ich nicht verstehe ist, also das macht aber ja Notion mit den Agenten ganz

**[00:38:24]** genauso. Die Agenten sind unterscheiden sicher von diesen persönlichen Agenten, wo

**[00:38:30]** man mit dieser Chatbot, der unten rechts in der Ecke ist, genau dadurch, dass sie

**[00:38:33]** einfach quasi bei Notion gehostet sind und einfach immer laufen. Du kannst sie,

**[00:38:39]** wenn du die geteilt hast, die Agenten, du kannst sie genauso teilen wie jede Seite

**[00:38:42]** mit 20 Leuten oder mit einer Gruppe, dann können alle diesen Agenten nutzen.

**[00:38:47]** Der ist dann nicht nur auf dich bezogen.

**[00:38:49]** Und diesen Unterschied habe ich noch nicht verstanden, warum man dann den Cloud-Agenten

**[00:38:54]** nutzen sollte und nicht den Notion-Agent.

**[00:38:58]** Ja, puh, spannende Frage.

**[00:39:03]** Wer das weiß, darf gerne einen Kommentar hinterlassen, aber soweit ich das verstanden

**[00:39:09]** habe.

**[00:39:10]** Agent ist ja in der Benutzeroberfläche und eine Funktion, die in Notion läuft und der Anthropic

**[00:39:16]** Manage Agents oder wie man das Ding, ja Manage Agents, ist quasi die dahinter liegende Cloud

**[00:39:23]** Infrastruktur, die von Anthropic da geboten wird. Ich bin mir gar nicht so sicher, ob diese

**[00:39:29]** Agenten von Notion nicht sogar da laufen. Wie weit du das dann für dich als Anwender brauchst,

**[00:39:38]** das kann ich dir gar nicht mal sagen, müsste man sich wahrscheinlich nochmal ausführlicher

**[00:39:44]** mit Beschäftigten gebe ich durchaus eine gewisse Lücke, eine gewisse Lücke zu, aber wenn ich

**[00:39:49]** mal so überlegen würde, vielleicht strafst du mich ja lügen, aber so Notion-Agent, der

**[00:39:53]** macht ja sowas wie Texterstellen, Datenbankpflegen, Notion-Seiten, analysieren und ein Managed

**[00:40:02]** Agent bei Anthropic, kann außerhalb von Notion arbeiten. Ihr kann außerhalb von Notion-Dinger

**[00:40:10]** adressieren. Ihr kann außerhalb von Notion und in Notion-Rechtigungen pflegen. Also ich glaube,

**[00:40:20]** der ist schlicht und ergreifend halt dann interessant, wenn du sagst, okay, ich habe Sachen,

**[00:40:24]** die kriege ich mit einem Worker und die kriege ich mit einem Agenten bei mir Notion alleine

**[00:40:29]** nicht geregelt oder habe vielleicht auch überhaupt nicht Notion in der Zwischenkette, weil ich sage,

**[00:40:34]** ich verbinde mal Mailpostfach mit Spotify und irgendwelche Ergebnisse interessieren mich erst

**[00:40:41]** im Nachgang, aber nicht während dieses initialen Aufrufs, dass du da Quartens weiteren Kumpen kriegst.

**[00:40:47]** Und natürlich ist es so, wenn es jetzt darum geht, wirklich Code zu schreiben auf Basis von

**[00:40:53]** von einem Trigger, der aus Notion kommt, dann ist es ja eh klar, das kann Notion meiner Meinung

**[00:40:58]** nach nicht.

**[00:40:59]** Also keine Ahnung, vielleicht habe ich es nur noch nicht verstanden, aber ich glaube nicht.

**[00:41:02]** Das bedeutet also, wenn ich dann diesen externen Agenten habe, der mein gesamtes System kennt,

**[00:41:07]** der irgendwie das GitHub versteht und der dann weiß, an der und der Stelle muss ich

**[00:41:12]** etwas auschecken, um etwas zu tun, das würde Notion alleine nicht können.

**[00:41:15]** Also es gibt bestimmt genug Anwendungsfälle, wenn man die Uniformate ausweitet.

**[00:41:19]** Aber genau.

**[00:41:20]** Ich habe jetzt eigentlich nur gedacht, gibt es wirklich einen Unterschied, wenn ich das

**[00:41:23]** gleiche Format mache.

**[00:41:25]** Wahrscheinlich gibt es den nicht, sondern es geht darum, dass es eben mit anderen Systemen

**[00:41:29]** anders interagieren kann.

**[00:41:30]** Claude zum Beispiel oder dann eben auch andere.

**[00:41:33]** Ja, okay.

**[00:41:34]** Und die Agenten können wirklich auch lange arbeiten.

**[00:41:37]** Ja, also diese Management Agents, die können auch richtig lange Tasks, gut musst du

**[00:41:42]** auch bezahlen, aber die können halt lange Workflows abbilden, wo ich jetzt nicht

**[00:41:47]** weiß, wo da die zeitliche Grenze vom klassischen Notion aufgehoben ist, ja, also von der Seite.

**[00:41:57]** Und wie würde man, wenn ich das noch kurz frage, als kleiner Überblick, wie würde man

**[00:42:01]** diese Agenten in Claude deployen, also wie, wie einfach nur so die Pferde, wie funktioniert

**[00:42:08]** das? Ist das ein, sag ich dem Ding einfach, ja, mach aus diesem Skill jetzt so ein Managed

**[00:42:12]** Das letzte Mal ist gut, das ist wahrscheinlich heute immer noch so, aber als ich meine Manage

**[00:42:19]** Agents angelegt habe, hast du in der, es gibt eine Cloud-Konsole, das ist jetzt nicht die

**[00:42:24]** Kommando-Zeile, sondern eine Webseite, da kannst du Api-Token, Api-Zugänge zu Cloud holen

**[00:42:30]** und so ein Kram und da gibt es auch Manage Agents und da kannst du durch ein Frage-Antwort-Spiel

**[00:42:36]** dir deine Manage Agents zusammen klöpeln.

**[00:42:39]** Ja, da kannst du sagen, was will möchte ich? Du kannst ihm dort schon direkt prompt zum Skills geben oder dich quasi durch ein Frage-Anfortspiegel zu diesem Managed Agent hinleiten lassen.

**[00:42:50]** Und du kannst da auch Ergebnisse, die du in Claude Code machst, auch hochladen, sinngemäß und sagen, hier, mach was draus, hat mir da schon ausführliche Gedanken gemacht, hier liegt was auf der Platte, ich hab hier, wie gesagt, Skills, ich hab hier keine Ahnung, was.

**[00:43:03]** Dann betreibt ihr die dort und macht ihr auch sowas wie eine kostenkontrolle.

**[00:43:09]** Das sagt okay, wenn wir auf wie häufig liebt denn das tierchen ja nicht, dass der quasi sieben wir in 20 läuft und du wolltest eigentlich gar nicht.

**[00:43:16]** Und das macht halt über dieses interface und wie gesagt da konnte man ganz viele sachen hochladen und bereitstellen und soweit ich das mitbekomme kannst

**[00:43:25]** Das ist mittlerweile von Claude Code aus, aus der CLI heraus auch befeuern, direkt befeuern

**[00:43:30]** und dass du irgendwie Copy-Paste in dieses Web-Interface machen musst und daher wäre

**[00:43:38]** auch meine Vermutung erst mal, vielleicht lässt sich nur eine schöne UI einfallen,

**[00:43:44]** aber wenn du das heute nutzen wolltest, würde ich fast darauf wetten, dass wenn du ein

**[00:43:50]** Account hättest, dass du das auch heute schon nutzen kannst. Weil ich sage mal, du brauchst

**[00:43:57]** nur einen Api-Token, du brauchst die Zugänge, du brauchst, das ist ja alles, was du heute

**[00:44:01]** singemäßig mit deinem Gmail auch machst. Nur, dass es halt nicht Gmail heißt, sondern

**[00:44:06]** Entwrappel. Ja, das glaube ich auch. Naja, ich meine, um nochmal ein bisschen rauszusummen,

**[00:44:11]** die Vision, die dahinter steckt, dass ich eine Verhältnismäßig, einfach zu bedienende

**[00:44:17]** Plattformen habe mit Notion, um dieses KI-Zeitalter selber auch noch ein bisschen einfacher vielleicht

**[00:44:25]** für den Einzelnen für mich nutzbar zu machen. Ich glaube, das ist tatsächlich deren Mission

**[00:44:31]** und ich finde das gelingt. Klar, ich habe am Anfang gesagt, das CLI-Thema, da war

**[00:44:35]** ich am Anfang, da bin ich immer noch auf Hilfe angewiesen, aber an sich auch der

**[00:44:41]** Weg, den sie beschreiten, ist aus meiner Sicht der Wichtige, nämlich dass sozusagen

**[00:44:46]** jeder und jede die Lage versetzt wird, sich ihr Tool zu bauen und dass ich nicht mehr ein

**[00:44:52]** politisches, also ein großes fertiges Tool, mir irgendwo Kauf oder Miete, sondern dass

**[00:44:58]** ich irgendwie Stück für Stück mir das, ich sag jetzt mal in einem Vorstrichen, mit

**[00:45:02]** wirklich einfachen Mitteln selber zusammenbauen.

**[00:45:03]** Das macht jemand wie mir, der kein richtiger Entwickler ist, total Spaß, weil auf einmal

**[00:45:08]** diese ganzen Dinge gehen und man darf eben auch nicht vergessen, die ganze Kette

**[00:45:13]** aus Requirement Engineering und dieses und Lasten und Flüchten und was es sich fällt

**[00:45:17]** alles weg, wenn jemand, wie ich quasi selber das bauen kann, sehr zum Frust manchmal meiner

**[00:45:24]** Leute, die dann irgendwie denken hat sich der komische alte Mann schon wieder irgendwas

**[00:45:28]** ausgedacht.

**[00:45:29]** Aber viel effizienter geht es, glaube ich, nicht, diese ganzen Dinge zu integrieren.

**[00:45:33]** Und das ist echt, das ist echt, muss man echt sagen.

**[00:45:36]** Also ich habe es ja beim letzten Mal, glaube ich, auch gesagt, für mich ist das echt

**[00:45:39]** so ein Tool, das mich genau so fesselt, wie damals bis heute natürlich auch Apple mit

**[00:45:44]** all den Produkten. Ich bin mal gespannt, ob das noch so bleibt.

**[00:45:47]** Ich bin gespannt, wie Sie jetzt bei der nächsten WWDC aus dem Quark kommen und jetzt wo Sie

**[00:45:54]** mit Google diesen Deal haben mit Modellen, ob da irgendwie, ob Sie wieder Vortrieb kriegen

**[00:46:02]** und ein bisschen etwas aus dieser neuen Welt zeigen, weil wir beide merken es ja jetzt,

**[00:46:07]** jetzt CLI uns gefällt oder nicht? Ich habe hier hergeleitet am Anfang damit, dass früher

**[00:46:13]** waren wir froh über die schönen Benutzerinterfaces. Heute verziehst du dich freiwillig gefügt in

**[00:46:19]** diese Kommando-Zahleninterfaces, damit Menschen wie du und ich auf einmal anfangen, fern unserer

**[00:46:26]** Professur oder fern aufgrund unseres Alters auf einmal mit Ideen um die Ecke zu kommen,

**[00:46:30]** weil wir einfach, naja, du kannst jede Idee in eine Fähigkeit, in einen Prototypen, in

**[00:46:37]** irgendwas überführen und über das Ergebnis reden, anstatt wochenlang dir irgendwie den

**[00:46:42]** Kopf zu machen, ob der Knopf rechts oder links ist, hast du auf einmal 20 Versionen im Raum

**[00:46:46]** stehen und kannst ausprobieren und weißt viel besser, funktioniert das, funktioniert

**[00:46:51]** das nicht, welche Emotionen weg das, keine Ahnung, was nicht alles, ja, möchte da

**[00:46:55]** jetzt nicht Begriff in die Welt setzen oder nutzen, die nicht in meinem täglichen

**[00:47:00]** Arbeitsleben vorkommen, aber trotzdem kriegst du ja schon mit, dass dieses, dieses Spielen,

**[00:47:06]** ich habe auch letztens mal gesagt, das ist wie so ein Text-Adventure. Früher hast du Ultimate

**[00:47:10]** Online oder wieder Grammys gespielt und hast gesagt öffne Tür, geh durch, vorsicht, Zombie,

**[00:47:16]** trete dich um, renne, ja, nimm die Farbglzünder an. So, heute schreibst du auch eigentlich,

**[00:47:20]** hätt ich, also das wäre eine total tolle Funktion, probieren wir mal aus und ach komm,

**[00:47:25]** das enter drücke ich jetzt noch und dann gehe ich ins Bett und dann auf einmal sind drei

**[00:47:28]** Stunden später und vielleicht hast du was erreicht, aber bist trotzdem müde und hast

**[00:47:34]** Augengefahr, sie hat das Spiel des Lebens gespielt mit deiner Professur, auch ganz lustig.

**[00:47:38]** Ja, KI als Textadventurer, mein guter Freund David ist Neurologe und brauchte für seine

**[00:47:45]** neue Privatpraxis ein datentechnisch gesehen wirkliches, sicheres Abrechnungs- und Verwaltungstool

**[00:47:52]** und er wollte sich nicht so ein teures Tool kaufen und irgendwelche 1000 Zertifikate

**[00:47:57]** Und dann haben wir gesagt, naja, gut, lass uns doch was mit Markdown-Dateien als Speicherung,

**[00:48:02]** Persistenzschicht bauen, MacOS in X-Code, mit Cloud natürlich, da hatten wir ja auch

**[00:48:08]** schon mal drüber gesprochen.

**[00:48:09]** Das habe ich ja von dir mit diesen Markdown-Dateien.

**[00:48:11]** Du, und dann haben wir das innerhalb von drei Stunden gebaut, der hat einen eigenen

**[00:48:15]** Rechner, der hat kein Internet, der hat kein WLAN, der hat nichts, alles abgestorbt

**[00:48:19]** sind, Alten auch sogar, also nicht ganz Alten, aber so.

**[00:48:22]** Und auf dem läuft dieses Software und ich habe ihm das dann eingerichtet, Cloud

**[00:48:26]** diese 20-Euro-Version, alles gegeben hat, keine Ahnung, und er macht jetzt genau das, was du sagst,

**[00:48:31]** nämlich am Ende des Tages macht er nochmal dreimal Klick und dann hat er wieder drei Stunden nicht

**[00:48:34]** geschlafen, weil er jetzt den Arztbrief da drin hat und diese Röntgenbilder und das noch und die

**[00:48:39]** automatische Rechnungsschreibung, und er muss ja einfach immer nur sagen, was er will. Und das wird

**[00:48:43]** einfach irgendwie gemacht. Und dann muss man bis in die Infrastruktur kennen. Und das ist für

**[00:48:47]** Nichtentwickler immer die größte Hürde, die Infrastruktur. Und wenn das aber geklärt ist,

**[00:48:51]** Das ist es halt mega. Und das ist im Grunde, wenn wir es überlegen, worüber wir heute

**[00:48:56]** gesprochen haben, Notion und Ducktape und was soll ich da für Wort im Mund genommen haben.

**[00:49:02]** Angefangen haben die als, was, Notizbuch, Notizmöglichkeit, Notizlösung, haben dann irgendwie den Bogen

**[00:49:10]** gekriegt mit Daten banken und hast sie nicht gesehen, Geschäftsprozesse zu unterstützen

**[00:49:14]** und jetzt auf einmal, das heißt auf einmal, jetzt entwickeln sie sich quasi zu etwas,

**[00:49:20]** Das tut sich auch diese ganze Komplexität von Routinearbeiten, von vielleicht kreativen

**[00:49:28]** Themen von, was auch immer, wegnimmt, weil jetzt hast du dich hingesetzt und was mit

**[00:49:34]** das CLI programmiert, das musst du ja auch nicht jeder machen.

**[00:49:37]** Das reicht ja, wenn zwei, drei Leute das machen, die Worker bereitstellen, die Agents

**[00:49:40]** bereitstellen und dann auf einmal die ganzen Menschen mit dieser neuen Möglichkeit arbeiten,

**[00:49:44]** nie was davon sehen musst, oder vielleicht ändert sich das Berufsbild an der Stelle.

**[00:49:49]** ein anderes Thema. Aber ein Tool, das du seit Jahren hast, von dem man gewohnt ist, dass es

**[00:49:56]** immer wieder ein Update bringt und dann vielleicht etwas Neues, Tolles, ändert auf einmal fundamental

**[00:50:01]** die Art, wie man damit arbeitet. Ich glaube nicht, dass du vor zwei, drei Jahren gedacht

**[00:50:04]** hättest, dass Notion zu sowas in der Lage ist. Und das finde ich...

**[00:50:08]** Ja, gerade oft. Ja. Sagt zu zähren den Entschuldigung. Ich habe dich unterbrochen.

**[00:50:13]** Aber gerade, wenn ich überlege, diese schnelllebige Zeit du hast, also ich meine, heute

**[00:50:17]** ist etwas cool und in drei Monaten kommt der Nächste ums Eck und wie sie sich gegenseitig

**[00:50:20]** challenge'n und wie sie sich gegenseitig durch den Ringzerren mit neuen Funktionen, Möglichkeiten,

**[00:50:26]** Paradigmen begriffen. Ich meine, heute, ja, du hast selbst gesagt, Modelle sind gut und

**[00:50:31]** die werden getauscht und die Laufzeit, in der sie sind, der Hahn ist, der ist quasi

**[00:50:36]** das neue Gold, ja, wie er das Wissen speichert, wie er das Modell anprägt, wie er die Abstraktion

**[00:50:42]** von dir nimmt. Und wer weiß, was es in einem halben Jahr ist, aber ich habe irgendwie

**[00:50:45]** das Gefühl Notion ist ein sehr stiller, aber ein sehr moderner Begleiter dieses Wandels.

**[00:50:53]** So, weißt du noch, was du sagen wolltest? Ja, ich finde die, die dieses Verdraht wird,

**[00:51:01]** ich wollte auf das, du hast vor drei Jahren nicht gewusst, was du da machst. Ich habe

**[00:51:03]** vor drei Jahren gewusst, ich will alles in einem System haben. Das wollte ich eben

**[00:51:07]** einfach schon immer. Das ist irgendwie so. Und ich wollte lieber ein integriertes System

**[00:51:11]** Apple als irgendwie so ein Dezentrales, wo jedes Programm seine Berechtigung hat und dann

**[00:51:17]** so best tool for the job. Das fand ich immer für mich persönlich und für meine Firma doof,

**[00:51:21]** weil ich wollte es dabei integriert haben und ich wusste natürlich noch nicht,

**[00:51:24]** dass das irgendwann mal so wichtig wird. Und heute ist es eben so, dass dadurch,

**[00:51:27]** dass da wirklich alles drin ist, ich den bestmöglichen Kontext habe und das Ding weiß

**[00:51:31]** immer schon alles. Und ich kann Finanzanalyse machen, Buchateläte jetzt immer die Sachen

**[00:51:36]** rauf, weil ich da noch kein Lust habe, das mit Datif zu verbinden. Das geht auch, aber

**[00:51:41]** habe ich nicht. Und der legt die halt rauf, dann geht der agentlos, guckt sich das an,

**[00:51:46]** guckt irgendwelche Buchungsfehler nach und so weiter. Aber diese ganzen Informationen kann

**[00:51:50]** ich auch in einem anderen Kontext nutzen. Also das Lustige, und darauf wollte ich eben

**[00:51:54]** raus, war, ich habe gerade auf LinkedIn geschrieben, wir haben aus Versehen ein Marketing-Betriebssystem

**[00:52:00]** erfunden, weil wir haben ja nicht diesen tollen strategischen Plan gehabt. Und dann

**[00:52:04]** wenn 2026 die KI soweit ist, dann haben wir das tolle Tool, sondern das hat sich halt

**[00:52:09]** zufälligerweise so ergeben und jetzt haben wir das und jetzt können wir wirklich unseren

**[00:52:13]** Kunden sagen und Kundinnen, pass mal auf, wir haben das alles da drin, die Strategie,

**[00:52:18]** das Corporate Design, die Playbooks, den ganzen Kram und natürlich können wir euch ein Teil

**[00:52:23]** dieses Vorteils weitergeben. Also wir müssen nicht den ganzen KI Vorteil nur für uns

**[00:52:29]** behalten, wir geben das für euch weiter, weil wir wissen, dass wenn du die Werkzeuge

**[00:52:33]** für den Goldgräberrausch, der verkaufst du auch ganz gut, ein ganz gutes Geschäftsmodell,

**[00:52:37]** hast du musst nicht immer nur selber schürfen. Und das wollen die Leute jetzt. Und das kann

**[00:52:40]** ich alles mit einer Plattform machen. Ich kann die iZone Ocean einladen. Und ich habe jetzt

**[00:52:44]** schon die ersten Pilotkunden, die das machen. Und die können dann KI nutzen, ohne dass

**[00:52:49]** sie sich damit beschäftigen müssen. Einfach als Service von uns. Wir richten nicht

**[00:52:53]** nur, weißt du so, wir machen nicht irgendwie diese ganzen Sachen über die wir geredet

**[00:52:57]** haben, sondern für den Kunden ist das komplett, der muss gar nichts tun. So wie so ein

**[00:53:02]** CMS früher, der kann einfach sich hinsetzen, schreibt ein Ticket und dann passiert irgendwas.

**[00:53:06]** Und entweder macht das Agent oder das macht ein Mensch oder beide und das ist halt echt

**[00:53:10]** krass.

**[00:53:11]** Und das hat das nix damit zu tun, dass wir einen gewissen Verwandtschaftsgrad haben.

**[00:53:15]** Aber ich habe auch und dann nenne ich jetzt keine Namen mit diversen anderen Firmen mal

**[00:53:21]** so zu tun.

**[00:53:22]** Auch, ich sage, na, was heißt zu tun, ne?

**[00:53:24]** Also externe Firmen, die ihre Leistungen uns darbieten und wenn man sich dann anschaut,

**[00:53:30]** man sich dort mit KÖI beschäftigt. Und wie auch die im Wandel sind, ich meine, ich hab die Weißer

**[00:53:35]** auch nicht mit Löffeln gefressen, ja, aber auch wie die im Wandel sind und ihr sicherlich auch

**[00:53:40]** eure Päckchen zu tragen habt, aber dadurch, dass das in diesem Notion drin ist, dadurch,

**[00:53:47]** dass der Hersteller Notion euch eine Lösung darbietet, die es euch jetzt nicht schenkt,

**[00:53:54]** aber die es euch leichter macht, das Wissen weiterzuverwenden ist. Es ist ja schon da,

**[00:54:00]** darauf zuzugreifen, den Agenten zu bitten, Sachen zu extrahieren, den Agenten zu bitten,

**[00:54:05]** Dinge zu tun, ohne dass du Bird Axel Powerpoint, unterschiedliche Verzeichnendstrukturen,

**[00:54:11]** unterschiedlichste, keine Ahnung, was, ja, Dateiformate, Axels, die aus der Schwarte krachen

**[00:54:17]** und mit Makros und am besten auch mit Farbkodierung arbeiten, um die Besonderheit von Zahlen

**[00:54:23]** uns hervorzuheben, was vielleicht alles geht, aber worauf ich rauswähle, die Basis, die

**[00:54:27]** Grundlage, das Fundament ist ja da und Notion entwickelt sich ja auch dahingehend weiter,

**[00:54:34]** sie binden es an, wir hatten es vorhin mit der Art der Datenverarbeitung und da gibt es

**[00:54:40]** genügend Firmen, die haben halt vielleicht ein tolles Beratungsangebot und schlaue Menschen,

**[00:54:44]** haben die alle, ja, ich meine, wir sind allen, die meinen, überall arbeiten schlaue

**[00:54:48]** Menschen, würde ich mal unterschreiben, aber sie haben halt vielleicht aufgrund

**[00:54:52]** der Werkzeuge, die sie eingesetzt haben. Früher war es mal Lotus Notes. Jetzt ist es halt

**[00:54:57]** hauptsächlich ganz viel Microsoft-Kram. Selbst wenn es Apple-Kram ist, ist es, naja, weiß

**[00:55:01]** aber nicht. Ja, aber mit Notion hast du, glaube ich, ein gutes Fundament, das ist jetzt zumindest

**[00:55:06]** auch in diesem Wandel der Zeit von N8n und Make und dann kam Codex und Cloud und Crock

**[00:55:14]** und keine Ahnung, was. Ja, eine Basis bietet, auf der du aufsetzen kannst, um weitere

**[00:55:20]** mehr Werte für Kunden, Mitarbeitende zu dazubieten. Und das finde ich tatsächlich, Schapo Hutab,

**[00:55:27]** ja, eine coole Sache. Und das macht mich auch zu positiv gelaunt. Da hingehend, dass ich denke,

**[00:55:35]** okay, Sie haben Markdown im Herzen. Sie haben KI-Ambindung im Herzen. Sie haben diese Offenheit jetzt

**[00:55:41]** mit den Worker und so nach außen, dass selbst wenn in drei Monaten oder in zwei Jahren oder in einem

**[00:55:48]** ja, irgendeine coole neue Sau durchs Dorf getrieben wird, dass sie die Chance haben aufgrund der

**[00:55:52]** guten Datenablage und der Offenheit, mindestens mal mitzugehen, wenn nicht sogar stand zu halten.

**[00:55:58]** Und das finde ich tatsächlich, das geht sehr stark unter, weil die meisten, die hören, oh,

**[00:56:02]** Anthropic hat schon wieder ein Update geschippt. Ja, oh, die wollen hier Erwachsenen, Chat und

**[00:56:08]** keine Ahnung war es, das ist ja alles, bleh. So, und Google, ah, jetzt haben sie, jetzt hat

**[00:56:12]** Google, Google hat alle wieder im Boden zerdrückt und keine Ahnung war es,

**[00:56:15]** zum Coop-Pilot war noch nie gut, ist mal mehr so kalt, Klammer auf Stereoiden.

**[00:56:19]** Von Notion hörst du nie was.

**[00:56:21]** Aber wenn du dich mit Notion beschäftigst, ist es geil.

**[00:56:25]** Ja, das war ja immer so.

**[00:56:27]** Als Apple dann an so einem Punkt war, wo sie schon gut waren, aber niemand sie kannte,

**[00:56:32]** weil eben die ganzen Sachen in Anrichtung gegangen sind.

**[00:56:36]** Ich glaube, dass das in einem okayen Tempo kommt, denn das ist schon ein großes Tempo.

**[00:56:41]** Die sind jetzt tausend Leute, das nicht viel,

**[00:56:43]** Aber es ist für die natürlich ein wahnsinniges Wachstum, die kam dann irgendwie von, keine

**[00:56:48]** Ahnung, von 300 oder so und 1.000 hört sich lächerlich wenig an für das, was die für

**[00:56:53]** ein Output haben.

**[00:56:54]** Aber die sind eben eine von diesen neuen Firmen, die nicht so viel Headcount brauchen, um

**[00:56:58]** diesen Output zu schaffen.

**[00:56:59]** Und wenn du dir diese ganzen Videos anguckst, wie die selber mit ihrem eigenen Tool arbeiten

**[00:57:03]** und natürlich haben die 1.000 Agenten dort laufen bei sich und machen damit alles

**[00:57:07]** und jedem Slack Channel ist ein Agent von Notion und beantwortet das erst mal schon

**[00:57:12]** und hört so ein bisschen mit und wenn jemand was wissen will, ich habe jetzt auch 2, 3 gebaut,

**[00:57:16]** dann sagt er für neue Leute zum Beispiel, ja, beantwortet Notion in Slack, die Fragen aufgrund

**[00:57:23]** des Kontextes in Notion. Na ja, worauf ich noch kurz eingehen wollte, man kann wirklich sagen,

**[00:57:28]** und das finde ich ist ja die große Aufgabe jetzt vor allem, wenn du das in Notion hast,

**[00:57:33]** kannst du als Mitarbeiter relativ clean und so mal so mit kleinen Schritten in diese KI-Welt

**[00:57:41]** kommen, weil dann macht ihr irgendwie mal so ein Prompt und dann macht ihr so heißt das dann bei uns

**[00:57:46]** jetzt so ein Skill und dann kannst du einfach irgendwo sagen add und dann gibt es den Skillnamen an,

**[00:57:50]** dann passiert irgendwas und auf einmal, du brauchst sich eine komplett neue Oberfläche,

**[00:57:54]** irgendwie ein neues System, du musst dich copy paste in Chatbot oder oder oder, das ist einfach da

**[00:57:59]** in der Dosis die du willst und es wird halt einfach immer sichtbarer für dich, das nämlich

**[00:58:04]** gerade unser Projekt, dass wir die Leute alle reinholen. Ich will jetzt nicht zum Schluss

**[00:58:11]** kommen, ohne da auch noch einen Satz zu sagen. Weil auch das wiederholen wir auch in dem Podcast

**[00:58:16]** regelmäßig. Die Technik ist ja da. Nur weil die Technik sich schnell entwickelt, heißt das ja nicht,

**[00:58:21]** dass die Technik wie wir sie heute haben oder wie sie vor drei Monaten war, dass sie schlecht ist.

**[00:58:25]** Sie kann total viele Dinge tun und sie scheitert nicht, weil die Technik schlecht war oder schlecht

**[00:58:30]** ist seit einer gewissen Zeit, sondern dass du halt auch Menschen auf die Reise mitnehmen musst,

**[00:58:34]** weil die Mehrheit hat immer noch nichts von KI gehört, außer in den Nachrichten vielleicht. Die,

**[00:58:39]** die, die etwas von KI gehört haben, die haben es dann vielleicht auch teilweise benutzt

**[00:58:43]** oder es in der Meinung ist, benutzt zu haben, haben sie aber irgendwie nie, benutzt es mehr

**[00:58:47]** wie Google.

**[00:58:48]** Nachdem manche etwas eingegeben ist, kam eine Antwort, danke, tschüss.

**[00:58:50]** Und die wenigsten bezahlen dafür, noch weniger machen da mit Skills und Kram oder verlieren

**[00:58:55]** sich auf der CLI und benutzen dann halt, ich sag mal, KI in Reinkultur und von der

**[00:59:00]** Seite ist dieses, wie nimmst du Menschen mit, ohne dass du sie einerseits überforderst,

**[00:59:06]** Weil zu volle Fenster, zu viele Knöpfe, typische Itile, musst du da klicken, warum klickst

**[00:59:13]** du hier?

**[00:59:14]** Ne, machst du da und dann gehst du bitte ins Untermenü und dann gibst du das ein, jetzt

**[00:59:16]** mach doch mal.

**[00:59:17]** Ja, also das ist ja so, jeder in seinem Jaguar hat unter Umständen wenig Geduld in Menschen

**[00:59:24]** eines anderen Jaguars, ist das den Ausführer zu erklären.

**[00:59:27]** Und von der Seite ist das, was du gesagt hast, natürlich auch noch mal ein Punkt,

**[00:59:31]** wenn du gewohnt bist mit Noten zu arbeiten, was sicherlich für den Menschen, der

**[00:59:35]** Nauschen-Kentenumstieg ist, kannst du das homöopathisch einführen. Und das ist sicherlich nicht zu verachten

**[00:59:46]** und zeigt auch, wenn das vielleicht damals nie der Punkt war, weswegen man sich mit Nauschen

**[00:59:50]** beschäftigt hat, dass das doch gar nicht mal so dumm war, dass du benutzt. Umsteigen für,

**[00:59:56]** wenn du mal auf etwas anderen bist, ist halt dann auch schwer. Du musst die Menschen abholen,

**[01:00:00]** du musst deine Daten reinholen. Also je größer du bist und je mehr Menschen du hast,

**[01:00:04]** glaube ich, umso schwerer ist es, einen derartigen unterschiedlichen Bedienparadigma zu bedienen.

**[01:00:15]** Aber ich fand es mal wieder toll, dass wir uns über Notion unterhalten haben. Es kommt bestimmt

**[01:00:24]** wieder. Ich habe so das ganz komische Gefühl, dass Notion irgendwann mal wieder ein Update

**[01:00:28]** schippt. Spätestens dann würde ich mir erlauben, dich wieder einzudäufigen. Vielleicht

**[01:00:32]** Ich möchte der Jens ja auch dann dabei sein, ist wahrscheinlich eine volle Ausrede, dass er kracht.

**[01:00:36]** Ja, vielleicht ist das nur eine Ausrede, aber ich würde ihn auch gerne kennenlernen.

**[01:00:41]** Also, Grüße gehen raus, wie du so schön sagst.

**[01:00:43]** Und es war sehr schön bei dir mal wieder.

**[01:00:45]** Wir sind bei einer Stunde und zwei Minuten.

**[01:00:47]** Das ist, glaube ich, die Zielzeit.

**[01:00:48]** Ja, so ungefähr.

**[01:00:50]** Das passt plus minus.

**[01:00:52]** Das passt doch sehr schön.

**[01:00:53]** Ja, vielen Dank für die Einladung.

**[01:00:55]** Und für die Erklärung im Vorfeld.

**[01:00:57]** So bin ich stolzer Besitzer von jetzt schon zwei Workers.

**[01:01:00]** Der absolute Hammer.

**[01:01:02]** Wenn es euch gefallen hat, Schinte, lasst ein Like, ein Kommentar, sagt euren Freunden,

**[01:01:05]** egal ob sie mit oder ohne Noten arbeiten, dass ihr unseren Podcast gebt und seid gespannt,

**[01:01:10]** wer das nächste Mal unser Gast ist.

**[01:01:11]** Bis dann.

**[01:01:12]** Ciao.

**[01:01:13]** Tschüss.

**[01:01:14]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[01:01:21]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden,

**[01:01:26]** sondern sie leben.

**[01:01:27]** Hier gibt es klare Einordnungen, echte Praxis-Einblicke und einen frischen Blick auf das, was möglich ist.

**[01:01:34]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[01:01:38]** KI zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
