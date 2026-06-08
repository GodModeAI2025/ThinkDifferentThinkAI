---
title: "Just vibe IT"
episode_index: 43
published: "Mon, 08 Jun 2026 03:44:00 +0000"
duration: "2196"
page_url: "https://think-ai.podigee.io/41-just-vibe-it"
image_url: "https://images.podigee-cdn.net/0x,spMpsrQvFxNCV2XKgw65UvrHjchWyPfe2tjatJRw8NZM=/https://main.podigee-cdn.net/uploads/u73317/83dba456-dc11-4b39-a949-8aac7944b9b5.jpg"
audio_url: "https://audio.podigee-cdn.net/2480694-m-8e56e6d7291296a03244f65fa8a3c07c.mp3?source=feed"
guid: "b43faf503c50db5fd36fa6582a896611"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-06-08T11:01:02+00:00"
---

# Just vibe IT

**Veröffentlicht:** Mon, 08 Jun 2026 03:44:00 +0000
**Dauer:** 2196
**Webplayer:** https://think-ai.podigee.io/41-just-vibe-it
**Cover:** https://images.podigee-cdn.net/0x,spMpsrQvFxNCV2XKgw65UvrHjchWyPfe2tjatJRw8NZM=/https://main.podigee-cdn.net/uploads/u73317/83dba456-dc11-4b39-a949-8aac7944b9b5.jpg
**Audio:** https://audio.podigee-cdn.net/2480694-m-8e56e6d7291296a03244f65fa8a3c07c.mp3?source=feed

## Beschreibung

Diese Folge ist eine Zwischenfolge ohne Gast – aufgenommen direkt vor der nächsten Episode. Mark und Jens sortieren, was sich in den letzten Wochen rund um KI-Skills, Vibe Coding und die großen Modelle getan hat. Mit ein paar Stolpersteinen, einer Smart-Home-Anekdote und dem Hinweis auf eine eigene neue Webseite.
Themen der Folge

Vibe Coding und Vibe Engineering – Andrej Karpathy hat den Begriff im Februar 2025 geprägt. Vibe Coding heißt: mit der Maschine reden und am Ende kommt laufige Software raus. Vibe Engineering legt mehr Kontext drauf.
Wenn das große Modell streikt – Marcs Erlebnis: Claude Code mit Opus weigerte sich stundenlang, ein konkretes Problem zu lösen. Über ein Plugin Codex von OpenAI als Reviewer eingeklinkt – und plötzlich lief es. "Hellender Moment."

Namensverwirrung im Modell-Zoo – Codex ist bei OpenAI mal Modell, mal App, mal Modus. Dazu GPT-5.5, Claude Opus, Bedrock, Copilot, Azure. Wer da nicht durcheinanderkommt, hat aufgepasst.
Architecture Decision Records (ADRs) – Schreibt auf, warum ihr euch für etwas entschieden habt. Nicht in Word, sondern in Markdown. Die KI kann das später lesen, auf Konsistenz prüfen und Dupletten finden.
Wenn die KI deinen Mac übernimmt – Anekdote vom Wochenende: Bildschirmfreigabe, Tastaturzugriff, Barrierefreiheit – und Claude klickt sich selbst durch das UI, um seinen eigenen Bug zu finden. Komisches Gefühl.

Manus AI in zwei Prompts – Jens hat eine Anwendung mit OCR-Erkennung und Google-Kalender-Login gebaut. Fünf Minuten später lief sie. Funktional ja, veröffentlichungsreif eher nein.
Pre-Mortem als Skill – Mark hat sich einen Skill gebaut, der das Vorhaben rückwärts denkt: Es ist gescheitert, was war schuld? Hilft bei Security, Login-Masken, Consent und allem, woran man sonst zu spät denkt.
KI lügt rotzfrech – "Sind alle Fehler weg?" "Ja." Spoiler: nein. Manchmal werden die Fehler einfach einer anderen Session zugeschoben.

Suchtfaktor und Work-Life-Balance – Warum ein Rate Limit auch sein Gutes hat. Jens' Open Claude prüft die Tageszeit und schickt ihn ins Bett.
Spezialisierte Tools statt Chat-Fenster – Nicht jeder braucht das volle Programm. Wer den ganzen Tag Folien macht, dem stellt man auch keinen Bagger vor die Tür.
Smart Home Reparatur durch KI – Philips Hue Bewegungsmelder beigebracht, das Licht beim erneuten Vorbeilaufen anzulassen. Eine Funktion, die es so eigentlich gar nicht gab.

Neu: Podcast-Webseite
Es gibt eine eigene Seite auf GitHub Pages mit allen Folgen-Transkripten – auf Deutsch und Englisch, jeweils als Markdown zum Download. Aktualisierung jeden Dienstag. Mit Suche, Feedback-Formular und der Möglichkeit, einzelne Folgen zu teilen.  https://godmodeai2025.github.io/ThinkDifferentThinkAI/?episode=037&lang=de

Erwähnt in der Folge
Andrej Karpathy – "Vibe Coding" (Februar 2025)
Anthropic Claude Code, Claude Opus, Max-20er Plan
OpenAI Codex (Modell und App), GPT-5.5
Amazon Bedrock, GitHub Copilot, Azure
Manus AI
Bolt, Lovable
Philips Hue
Mark-Uwe Kling – "Der Tag, an dem die Oma das Internet abschaltete" (Vortrag beim Chaos Computer Club)
Frühere Folge mit René zum Thema Skills

Take-Aways

Aufzählungs-TextSchreibt au

f, warum ihr Architektur- und Designentscheidungen so getroffen habt – in Markdown.

Nutzt Skills für Security, Clean Code und Dokumentation. Das ist kein Quatsch.

Baut euch ein Pre-Mortem in den Workflow ein: Was hätte schiefgehen können?

Wenn die KI sagt "alles sicher" – fragt zweimal nach. Beim dritten Mal sagt sie vielleicht endlich, was sie weggelassen hat.

Pausen sind erlaubt. Vibe Coding hat einen Suchtfaktor.

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** Hadi zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:29]** Herzlich Willkommen bei einer neuen Folge von Zink Different, Zink AI.

**[00:00:37]** Heute bei euch hier im Call ist nur der Mark und Jens.

**[00:00:44]** Ja, nur der Mark und Jens, ja, also das so wollte ich auch sagen, Jens, ja?

**[00:00:48]** Also ist du mir leid, wenn ich das nicht immer zuerst oder wie war das denn immer zu machen?

**[00:00:52]** Ja, das können wir denen zuschauen, bitte, Pinter, lasst es unten in den Kommentaren.

**[00:00:56]** Sagt einfach, ich habe keinen Anstand, das ist auch sehr schön als Kommentar, nehm ich auch sehr gerne an.

**[00:01:03]** Jens und ich saßen etwas früher in unserem heimatlichen Podcast-Studio und haben uns gedacht, bevor wir gleich unser nächsten Gast begrüßen, der in einer anderen Folge seinen Informationen zum Besten bringt,

**[00:01:17]** lass uns doch auch mal darüber reden und Review passieren, was wir in den vergangenen Folgen gehört haben.

**[00:01:22]** Ich möchte euch kurz abholen.

**[00:01:23]** Wir hatten vor einiger Zeit René zu Gast.

**[00:01:26]** Wir hatten das Thema Skills in der strategischen Gold.

**[00:01:29]** Und wir haben in dieser Folge keine Angst.

**[00:01:31]** Es geht nicht um Skills nur jedenfalls nicht ausschließlich.

**[00:01:33]** Wir hatten in der Folge darüber gesprochen, dass Technologie KI Skills hat,

**[00:01:37]** aber dass auch Organisationen und Menschen Skills brauchen,

**[00:01:39]** also dass man Menschen und Organisationen mitnehmen sollte auf die Reise

**[00:01:44]** und sich überlegen sollte, wie kriegt man quasi die Technologie näher,

**[00:01:47]** die Hürde reduziert oder das richtige Tool zur richtigen Zeit in der richtigen Art und Weise,

**[00:01:51]** dem Menschen auf dem Bildschirm oder wohin noch immer gezimmert, damit dort entsprechend

**[00:01:57]** mit Gabel werden kann. Und wir haben uns überlegt, lasst uns doch mal so ein bisschen Hilfestellung

**[00:02:01]** geben, ein bisschen Abwinder geben, was in dieser ganzen KI-Skill-Vibe-Coding-Ecke-Noise

**[00:02:08]** passiert ist und wie man es anwenden kann.

**[00:02:10]** Vibe-Coding, da rät ich natürlich direkt rein. Vibe-Coding, der Begriff von dem

**[00:02:18]** viel Zitaten kapartig auch, glaube ich wieder, der sehr, sehr viele Begriffe gerade ausprägt,

**[00:02:22]** im letzten Jahr ausgeprägt worden, ich glaube das war im letzten Herbst, wenn ich mich richtig

**[00:02:25]** erinnere. Also so alt ist dieser Begriff nicht, aber lasst mich mal kurz versuchen, eine kleine

**[00:02:32]** Definition dafür zu machen, damit wir alle auf dem gleichen Blatt Papier sind, wenn wir die

**[00:02:36]** weiterhin in die Folge reingehen. Blatt Coding beschreibt im Prinzip eine Art des Programmierens,

**[00:02:41]** in dem ich mit der Maschine jetzt mal platt gesagt, ein bisschen drüber quatsche,

**[00:02:45]** das ich haben will und am Ende laufigen Code rausbekomme, laufigen Anwendungen, laufige

**[00:02:52]** Software, laufige Apps, die ich in den Store stellen kann und das nur dadurch, dass ich

**[00:02:56]** ein bisschen mit der Maschine rieche. Das ist jetzt mal so die Jens Stanetski Definition

**[00:03:01]** von Vibe Coding, Mark. An dieser Stelle bräuchten wir ein Schingle. Jens Stanetski Definiert.

**[00:03:07]** Ja, mal überlegen, vielleicht fällt mir da was ein. Ja, also ich meine, der Punkt

**[00:03:12]** ist ja Vibe-Coding, dann kommen irgendwelche Leute sagen Vibe-Engineering, weil du dem Ganzen

**[00:03:17]** etwas mehr auch Kontext, wir reden ja auch immer wieder von Kontext, wenn wir von Prompting

**[00:03:22]** reden, sprechen musst und ich kann gerade so ein bisschen aus dem Nähekästchen erzählen,

**[00:03:26]** also keine Angst.

**[00:03:27]** Die Firma wird jetzt ja nicht in irgendeine komische Panik verfallen, weil ich irgendwelche

**[00:03:31]** ganz geheimen Internets verrate, ich erzähle ein bisschen etwas über wie Prompte denn

**[00:03:35]** der Markt und wie arbeitet er mit den Systemen und wir hatten so eine andere Nuss, die

**[00:03:41]** knacken wollten. Und wenn ihr den Podcast verfolgt habt, dann wisst ihr, naja, wir schwärmen immer ganz

**[00:03:47]** viel von Grotkot und Entropik und den Opus-Modellen. Und so fing auch mein Tag heute an. Ich habe viel

**[00:03:54]** mit Entropik, mit Opus gearbeitet. Wir haben das bei uns über MS & Bedrock im Bezug. Und das hat

**[00:04:01]** auch alles soweit wunderbar funktioniert. Aber ich hatte eine Nuss, die die Software-Herstellung

**[00:04:06]** da knacken musste und ich habe geschrieben, du passobacht, du musst das in das tun und das

**[00:04:10]** das Bedenken. Ja, okay, habe ich gemacht, sagt mir dann die KI in netten schlauschigen Worten.

**[00:04:14]** Ich gucke es mir an. Nee, hast du nicht. Ja, okay, ich arbeite nochmal nach. Ja, okay,

**[00:04:20]** jetzt habe ich es gemacht. Ja, das ging ein bisschen hin und her. Und Clotcode mit Opus war

**[00:04:25]** nicht zielführend. Und dabei war das ja eigentlich so dieses, das ist ja das mächtige

**[00:04:29]** Modell. Ja, gut. Jetzt gibt es da ein schönes Plug-in. Da kannst du sagen, ich möchte

**[00:04:34]** include code von mitentropic modellen zusätzlich zum beispiel ein review also

**[00:04:41]** eine überprüfung meines codes durch codex machen lassen codex seines zeichens

**[00:04:47]** open ai seines zeichens hat die version 5 5 seine sprachmodells

**[00:04:51]** rausgebracht vielleicht dazu ein ordnung da gibt es ganz viel auch ich sag mal

**[00:04:55]** namens verwirrungen normalerweise ist das codex modell das programmiermodell

**[00:05:00]** von OpenAI, außer man geht in, ist auf einem Mac, dann heißt auch so die App, mit der man

**[00:05:06]** arbeiten kann, ja, da kann man aber auch nicht Codex-Modelle starten und um die Komplexität

**[00:05:12]** noch doppelt zu erhöhen, ich hatte eben gesagt, ja, ich habe Codex-Gebeten quasi, also

**[00:05:17]** über Code-Gebeten mir zu helfen, ich habe das klassische CPT, also das ganz normale

**[00:05:22]** Sprachmodell, das jeder Feldwald-Wiesen-Anwender auch benutzen kann, über das Webinterface

**[00:05:27]** angesprochen, war das von diesem neuen Modell noch gar keine ganz speziell für Programmierung

**[00:05:32]** optimierte Version.

**[00:05:33]** Lange Rede, kurz als in, Opus hat sich da über Stunden geweigert, da irgendwie mein Problem

**[00:05:42]** zu lösen.

**[00:05:43]** Ich nehme es ihm persönlich übel.

**[00:05:44]** Dann habe ich das Plugin installiert, habe das Taughti-Modell angebunden und dann kam

**[00:05:50]** der Satz so, hier machen wir bitte Review, was hat er gemacht, nach 10 Minuten ließ.

**[00:05:56]** Und dann stehst du da und denkst so, Moment mal ganz kurz, ich habe das nicht auf Programmierung optimierte Modelle genommen, habe dem ein Problem gegeben.

**[00:06:05]** Gut, dazwischen sind ein paar Konfigurationsschritte gewesen, ja, weil wir haben ja auch bei uns in der Firma ja mal Bad Rock, mal GitHub Pro,

**[00:06:12]** ja, also Azure Modelle, da gibt es ja einen bunten Cosmos, da will ich gar nicht darauf eingehen.

**[00:06:17]** Ich will mir so auf die Mächtigkeit der Modelle eingehen und du gehst auf dieses andere Sprachmodell und du hast das Gefühl,

**[00:06:24]** Moment mal, dieses Gefühl von, ich habe das Licht gesehen,

**[00:06:28]** nicht in Form von Nahtrot-Erfahrung, sondern in Form von erhellender Moment

**[00:06:33]** in der Softwareinweg.

**[00:06:34]** Das soll manchen auch passiert, sagen wir mal, bei Codec übrigens,

**[00:06:36]** dass sie Nahtrot-Erfahrungen haben, wenn sie dann irgendwas online bringen

**[00:06:39]** und feststellen, dass ihr ihr jedes Security-Geschichten leider vergessen habt.

**[00:06:43]** Kann ich auch gleich etwas zu sagen? Ja, ich bin jetzt gerade im Rhetisch-Wall.

**[00:06:45]** Lass mich mal ganz kurz durchziehen.

**[00:06:47]** Ja, irgendwas hat Codecs das dann gelöst und dachte ich mir so,

**[00:06:50]** okay, probierst du Codecs ein bisschen aus,

**[00:06:52]** Und dann machst du mit Codex ein bisschen rum und, naja, lange Redekurzer Sinn.

**[00:06:57]** Codex hat viele Sachen hingekriegt, hat auch viele Sachen.

**[00:07:00]** Ich sag mal noch mal einen neuen Glankengang.

**[00:07:02]** Ich sag jetzt mal so rum, reingebracht.

**[00:07:04]** Und es war dann irgendwie lustig zu sehen, dass du in deinem Code das KI-Modell eines anderen Anbieters,

**[00:07:10]** ob mehr er anspricht, die Maschine dir Reviews und Überarbeitung macht

**[00:07:15]** und dann Code drauf guckt und sagt, oh, ist aber eine gute Idee, was da passiert ist.

**[00:07:19]** mal in ADRs, Architecture Design Records dokumentieren und dann stehst du da und machst das oder ein anderes Ereignis,

**[00:07:27]** das mir am Wochenende passierte. Ich habe bei mir zu Hause privat auch Codecs. Man muss immer aufpassen

**[00:07:33]** mit dem ganzen Namen. Alles fängt irgendwie mit C an und alles heißt irgendwie open und das ist

**[00:07:38]** ganz schrecklich. Also wenn ich mich verspreche, dann ist das kein Verstoß gegen irgendeine

**[00:07:42]** Richtlinie, dann habe ich einfach wieder nur verquatscht im Alpha der Geschwindigkeit,

**[00:07:45]** dass mein Mut für den Gehirn ist.

**[00:07:47]** Das hat nichts mit uns zu tun, Mark.

**[00:07:49]** Der ist auch einfach die Hersteller.

**[00:07:50]** Wenn die sich so nahmen, die ganze Zeit gehen,

**[00:07:52]** dann können wir als Einmarsch leblich ja gar nicht wichtig.

**[00:07:55]** Das ist alles aussprechen.

**[00:07:56]** Open Claw, Claw Bot, Claw Cod, Codex.

**[00:08:01]** Also das ist ja wirklich alles sehr, sehr nah aneinander.

**[00:08:05]** Jetzt kann ich auch noch mal richtig reden.

**[00:08:07]** Also no blame for you, Mark. Alles gut.

**[00:08:09]** Thank you. Thank you very much.

**[00:08:11]** Ich wollte über das Wochenende, wie gesagt, sprechen.

**[00:08:14]** Und da habe ich auch so ein kleines Programmierprojekt gehabt, wer aufs LinkedIn sich das angeschaut hat,

**[00:08:19]** da reden wir vielleicht gleich mal drüber, das Drillworkflow, das hast du nicht gesehen.

**[00:08:21]** Da hast du gesagt, du bau mir da mal was, mach mal was und zeig mir was und ich habe dann auch gesagt,

**[00:08:25]** du geht nicht. Also auch da passiert das, es geht. Und sagt er, nee, nee, du, das geht.

**[00:08:29]** Nein, es geht nicht, doch es geht. Also ich sitze vor dem Bildschirm, ich sehe, dass es nicht geht.

**[00:08:36]** Und er so, lass mich mal nachschauen und dann ploppt auf den Mac der Dialog hoch, die an,

**[00:08:41]** wenn du möchtest Kontrolle über deinen Computer übernehmen, Bildschirmfreigabe,

**[00:08:44]** Tastaturfreigabe, Barrierefreiheit und hast du nicht gesehen?

**[00:08:46]** Und dann fing der Anruf, dem ich das alles bestätigt habe, auf mein Bildschirm rumzuklicken,

**[00:08:50]** in meine Anwendung rumzuklicken und hat er gesagt, das ist recht, geht nicht.

**[00:08:53]** Ich repariere das mal.

**[00:08:54]** Und dann stehst du kurz davor und denkst du, okay, das ist auch mal ein geiles Erlebnis.

**[00:08:59]** Wenn du mit ihm diskutierst, er glaubt dir nicht.

**[00:09:01]** Er bedient den Rechner und sagt, hast recht.

**[00:09:04]** Also das sind so kleine Momente, wo du ganz kurz denkst, hollert die Wahl zu.

**[00:09:10]** Aber Vibe-Coding und Vibe-Engineering, ich habe eben auch gesagt, Vibe-Engineering.

**[00:09:14]** ist mehr Kontext, so will ich auch ganz gerne etwas zum Besten geben, bevor ich dich nach

**[00:09:17]** deinen Kunst- und Vibecoding-Erlebnissen frage. Es gibt ja die, was ich eben schon erwähnt habe,

**[00:09:23]** Architecture Design Records. Wurde dann, heißt das Design Records? Egal. Ah, der erst, machen

**[00:09:28]** wir es doch so. Ja, also dann schreiben sich die Shornouts, also im Einfall des Gefechts spätest

**[00:09:32]** Stunde. Da schreibt man im Grunde rein, warum sich das System wie entschieden hat und wie

**[00:09:37]** wir uns gemeinsam entschieden haben und wie die Architektur des Offers ist und wie

**[00:09:40]** bestimmte Module umgesetzt sind und so haben. Und ich hatte dann irgendwann mal angefangen,

**[00:09:44]** meine ganzen Projekte mitzuschlägen. Wer auf GitHub guckt, sieht auch, dass meine ganzen Projekte,

**[00:09:48]** die entsprechend an ADS beiliegend haben. Ja, dann bin ich jedenfalls hingegangen und hab dem

**[00:09:55]** Ding gesagt, du passen mir obacht. Ich würde total gerne jetzt eine neue Vibecoding App bauen

**[00:10:00]** und in meinem ganzen GitHub Projekt findest du die ganzen ADS. Schaut dir die bitte mal an.

**[00:10:05]** und wenn du jetzt eine neue App wendet ihr. Das hat er gemacht, das hat die ganzen

**[00:10:10]** Dinger durchgelesen und es auf so viele Sachen, wo er sonst eventuell noch mal eine

**[00:10:15]** Rückfrage gestellt hätte. Oder wie meinst du das jetzt mit deinen Tokens für

**[00:10:20]** Open AI? Ja, möchtest du da keine Ahnung, dass ich die und die Modelle auswähle,

**[00:10:25]** zur Auswahl biete? Es gibt auch Voice-Modelle, solltest du die auch zur Auswahl haben,

**[00:10:29]** blablabla. Der ganze quatscht ich schon mal gegen historischen Projekten beantwortet habe.

**[00:10:33]** Das hatte mich gar nicht mehr gefragt. Das war für den erledigt. Ja, wo ich mir dann auch dachte,

**[00:10:39]** das ist vielleicht so ein kleiner Brückenschlag nach meinem Sprech-Durchfall. Ihr solltet schon

**[00:10:44]** überlegen, dass ihr die Dinge, die ihr tut im beruflichen Umfeld wirklich aufschreibt. Schreibt

**[00:10:50]** euch auf, was ihr tut. Also eine Reihenfolge, wir hatten das Thema mit René, das gilt es. Aber

**[00:10:55]** schreibt euch auch auf, warum ihr zu welcher Entscheidung getroffen seid und speichert euch

**[00:11:00]** das in einem separaten Dokument ab? Ja, ich meine ADL, in der Software im Weg, das ist eine.

**[00:11:04]** Vielleicht findet ihr irgendwie einen anderen Grund, warum ihr beim Service Design bei einer

**[00:11:09]** Design Entscheidung kannst du mir vielleicht helfen, ob es da auch etwas Ähnliches gibt.

**[00:11:12]** Schreibt euch das auf und dann schreibt es euch nicht auf in Word oder in Excel, sondern

**[00:11:18]** schön im Markdown, damit ihr was zur Hand habt, dass falls ihr euch mehr mit KI beschäftigt,

**[00:11:22]** falls ihr eh schon mit KI beschäftigt und denkt, dass ihr etwas zur Hand habt,

**[00:11:27]** dass das System konsumieren kann und nicht und einfach ja am besten sagen hier ist der Ordner,

**[00:11:33]** da habe ich das rein strukturiert. Man kann die KI auch bitten, guck rein, ob es konsistent ist,

**[00:11:37]** ob es zu Blätten geht, ob es Widersprüche gibt und euch so stetig selbst verbessern. Es ist keine

**[00:11:43]** Schmach, dass man nicht mehr alles selbst weiß. Ja, das kommt mit zunehmendem Alter fällt mir

**[00:11:49]** das auch immer mehr auf, dass ich nicht mehr alles selbst weiß und deshalb ist der Hinweis ganz

**[00:11:53]** Gut, ich fange auch an Sachen aufzuschreiben zu deiner Frage natürlich designer. Wir sind natürlich wir entscheiden alles aus dem Bauch und schieben den ganzen Tag nur pixel hin oder her. Weißt du das? Ja, du mag.

**[00:12:04]** Ich habe noch ein ganz dringendes anding. Ich habe eben geguckt, ich muss echt, es ist echt zu spät. Ja, ich mache sofort den Fuzzle-Check für die aktuelle Folge.

**[00:12:11]** Ja, ADR heißt nicht Architekture Design Records, ich hab die ganze Zeit fast kannt, es kann

**[00:12:16]** doch gar nicht passen, ja.

**[00:12:18]** Architekture Decision Records passt doch mehr viel mehr zum Inhalt, also alle die die vorher

**[00:12:23]** schon abgeschaltet haben wegen Inkompetenz, bitte jetzt anrufen, dass sie weiter erinnern

**[00:12:27]** können.

**[00:12:28]** James, du wolltest etwas erzählen?

**[00:12:29]** Ich wollte aber noch etwas fuzzeln, auch direkt in dieser Folge, weil auch das habe

**[00:12:32]** ich direkt zu bekommen, und zwar ist es so, dass der Kapafi das im Februar gesagt

**[00:12:38]** und nicht im Herbst 2025. Also den Begriff Weibkoding gibt es seit Februar 2025. Damit haben wir das

**[00:12:44]** auch schon direkt aufgelöst und brauchen nicht auf die nächste Folge warten. Weibkoding. Ja,

**[00:12:49]** ich habe es ja gerade schon erwähnt. Natürlich, was der Mark gesagt hat, ist ein sinnvolles Thema,

**[00:12:53]** dass wir uns viele Sachen aufschreiben, damit wir die hinterher im Weibkoding so ein bisschen an

**[00:12:57]** der Hand haben, wenn wir strukturiert vorgehen wollen und halt nicht einfach nur in die Maschine

**[00:13:02]** rein sagen wollen, machen wir es fertig. Trotzdem gibt es ein paar Situationen, wo machen wir

**[00:13:07]** fertig extrem gute und erstaunliche Ergebnisse produziert. Das muss ich immer wieder sagen.

**[00:13:12]** Ich habe einmal mit Nanosei eine kleine Anwendung gebastelt. Die braucht eine

**[00:13:18]** Fotoerkennungslösung dafür, eine Kalenderanbindung. Und ich habe tatsächlich einfach zwei Proms

**[00:13:24]** abgeschickt, weil ich mich beim ersten Miss vertippt habe. Dann habe ich den Nanos nochmal

**[00:13:28]** gestoppt in der Produktion und mit dem zweiten Prompt, wo ich ein bisschen spezifischer noch

**[00:13:33]** mal war, was ich haben wollte, weil mir noch eine Idee gekommen war, hatte dann angefangen

**[00:13:36]** loszuröten und hatte nach fünf Minuten eine wirklich laufige Anwendung, die ich testen

**[00:13:42]** konnte, die eine OCR-Erkennung hatte, die eine Abfragen-Lockin hatte, wo ich mich mit

**[00:13:48]** meinem eigenen mit Google verbunden konnte und danach einglockt war. Das war ziemlich

**[00:13:52]** geil, muss man sagen. Also alle Features, die ich haben wollte, waren eins zu eins

**[00:13:55]** Das Design war jetzt so ein Standard-KI-Design, also da hätte man jetzt auch noch ein bisschen

**[00:13:59]** Aufwand tragen können.

**[00:14:00]** Aber das war wirklich so von der Idee, die irgendwo mal entstanden war, rein in die

**[00:14:08]** Anwendung gepromptet und fünf Minuten später eine lauffähige Version haben.

**[00:14:14]** Das ist ja tatsächlich schon, ohne dass ich irgendwas gemacht habe in die Richtung

**[00:14:17]** und deshalb hätte ich das Ding jetzt auch nicht online gebracht, also machte erst

**[00:14:21]** mal einen Research & Development Plan oder sowas und mache auch jedenfalls ein

**[00:14:24]** Ja, hab ich nicht gemacht, aber ich wollte ja einfach nur mal ausprobieren, ob dieses

**[00:14:29]** Vibe-Coding auch so funktioniert, wie ich mir das vorstelle, und es funktioniert.

**[00:14:32]** Du kannst wirklich Sachen produzieren in einer wahnsinnigen Geschwindigkeit, ich würde

**[00:14:39]** bevor ich jetzt sowas online stellen und nur so als kleinen Marker würde ich sagen, ja,

**[00:14:44]** man sollte es weiter so handhaben wie, wenn ich nicht weiß, wie ich den Stecker ziehe,

**[00:14:50]** sollte ich vielleicht noch jemand anders fragen.

**[00:14:52]** Na, das heißt, wenn mir nicht alles ganz klar ist, was in so einer Software, die ich gebaut habe, passiert,

**[00:14:56]** gerade wenn ich da mit Nutzer lade und sowas arbeite, dann sollte ich halt sehen,

**[00:15:00]** dass ich entweder vielleicht noch jemanden frage oder einen anderen KI drüberlaufen lasse,

**[00:15:04]** mich ein bisschen mehr Zeit lasse und nur nicht nur sage, ich kann jetzt irgendwie mit zwei Proms,

**[00:15:08]** kann ich eine super laufige Anwendung rausschießen, die wir dann auch auf die Welt komplett bloß lassen können.

**[00:15:13]** Da würde ich immer noch ein bisschen vorsichtig sein.

**[00:15:15]** Das hat sich, glaube ich, gebessert.

**[00:15:17]** Aber ich glaube, da sollte man immer noch Obacht geben, gerade wenn man dann mit tatsächlich

**[00:15:24]** Nutzerlockin vielleicht arbeitet, vielleicht wenn man auch die Idee hat, dass Kunden ihre

**[00:15:29]** Bankdaten immer anders eingeben, da gibt es zwar auch immer mehr Anwendungen, es gibt

**[00:15:32]** auch irgendwelche MCP-Server für Stripe oder irgendwelche anderen Sachen für Bezahldienstleister,

**[00:15:35]** dass man da auch Sachen anbinden kann, das geht dann auch schnell, aber man sollte

**[00:15:38]** aber tatsächlich ein bisschen, wenigstens eine grundsätzliche Ahnung von, was

**[00:15:43]** muss dann gemacht werden, welche Sicherheitseinstellungen muss ich dann tun und welche, auf welche Sachen

**[00:15:48]** muss die KI auch aufpassen, damit es hinterher eine Sicherung ist und nicht alle da geregelt.

**[00:15:52]** Das ist ja auch ein Punkt, ich meine, essen wir sie lügtig, rotzfrech an und sie behauptet

**[00:15:57]** Dinge, die wenn du nachfragst, sie dir glaubhaft paar Sachen dazu erzählt, ja, wieder ein paar

**[00:16:03]** Anekdoten und dann vielleicht noch eine Hilfestellung. Anekdote 1, ich habe in einem Projekt soll

**[00:16:08]** vorgekommen sein, etwas mehr gearbeitet zu haben, als ich eigentlich vorhatte. Am nächsten

**[00:16:14]** Morgen begrüßte mich einen Entwickler mit dem Satz und einem Meme-Bild, wo die Gärten

**[00:16:19]** von Asgard geflutet wurden, weil die Schleusen eines Flusses aufgeressen wurden, mit dem

**[00:16:25]** kleinen Kommentar, oh, Mark hat eine dreistellige Zahl von Komitz freigegeben. Passiert halt.

**[00:16:34]** Das zweite ist auch sehr schön, wenn du mit Vibecoding an etwas arbeitest und du liegst,

**[00:16:39]** gibst du die Mühe, ne? Und sagst, okay, pass auf Security und du hast eben vielleicht auch ein

**[00:16:43]** paar Skills für Security, ist auch so eine kleine Empfehlung, sucht euch ein paar Bibliotheken im

**[00:16:46]** Netz, die sicher gehen, dass ihr schon mal an die grundlegenden Sachen denkt. Ja, da gibt es

**[00:16:51]** Skills für Security checks, Skills für Clean Code Architecture, also auch Architektur und Skills

**[00:16:56]** für Dokumentation. Besorgt euch sowas. Das hört sich vielleicht erst mal an so,

**[00:17:00]** Ja, komm, er hat doch gemacht, aber das ist kein Quatsch, weil, ich sag mal, er erzählt dir viel und man muss ab und an erstes mal jemanden haben, der nochmal kritisch gegentritt oder ihn bitten, zwingen, Dinge auch zu dokumentieren.

**[00:17:14]** Es wird im einen oder anderen Zuhörer, den ich kenne, Grüße gehen an Simon, die Haare rauf.

**[00:17:18]** Was?

**[00:17:19]** Dokumentieren von SOSCO?

**[00:17:20]** Im SOSCO steht auch die Wahrheit, den Zeiten von KI.

**[00:17:22]** Ja, im SOSCO steht die Wahrheit, bei der Dokumentation könnten durchaus auch Drifts

**[00:17:26]** entstehen, dass da irgendwie Sachen, die im Code drinstehen, nie in die Dokumentation,

**[00:17:31]** die das System von sich selbst gemacht hat, reinschaffen, das kann passieren,

**[00:17:34]** da gibt es ein paar Verfahren, die man machen kann, aber worauf ich eigentlich

**[00:17:37]** raus will, man muss halt wirklich gucken, was er tut, weil da kommt zum Beispiel

**[00:17:41]** so schöne Stilblüten raus, wie,

**[00:17:44]** Hallo, Liebes KI-Modell,

**[00:17:46]** sind jetzt alle Fehler weg?

**[00:17:47]** Und er sagt dir,

**[00:17:48]** nee,

**[00:17:49]** da sind noch fünf,

**[00:17:50]** aber

**[00:17:51]** nicht mein Problem, das war ich nicht,

**[00:17:53]** das ist aus einer anderen Session.

**[00:17:54]** Ich bin schon frei,

**[00:17:55]** alle von mir sind fehlerfrei.

**[00:17:57]** Das war gestunken, wunderlogend.

**[00:17:59]** Die waren komplett von ihm,

**[00:18:00]** ja, aber er war irgendwie der Meinung,

**[00:18:02]** das war einmal, keine Ahnung,

**[00:18:03]** Anderer Tag, Anderer Kommit, Anderer Irgendwas.

**[00:18:05]** Und er meinte, er müsste sich nicht

**[00:18:07]** um die Fehlerfreiheit des Kot kümmern,

**[00:18:09]** weil das aus seiner Sicht nicht von ihm kam. Wo ich dann denkst du, was ist denn das für ein Verfahren?

**[00:18:14]** Wenn ich zu dir sage, räumen auf, ich meine, da kenne ich Menschen, wenn ich denen das sage,

**[00:18:18]** die zu mir sagen, ich habe das dann nicht hingeschmissen, ich hege das nicht auf.

**[00:18:21]** Also von der Seite, was ist denn das, bitte, für eine KI? So, das ist das eine.

**[00:18:26]** Und das zweite. Ja, aber das bringt mich zum Zweiten. Wenn er sagt, es ist sicher,

**[00:18:33]** stellt immer noch mal eine kritische Rückfrage. Also ich habe mir jetzt auch zum Beispiel ein

**[00:18:37]** Skill, ja auch hier wieder Werbung auf so mein Githa-Projekt geschrieben, indem ich quasi

**[00:18:42]** reinschreibe, was hat eine Funktion vor oder das ein Skript geschrieben, das quasi gucken

**[00:18:47]** soll, was ist das Ziel und dann gucken soll, was kann schiefgegangen sein, wenn ich dieses

**[00:18:53]** Ziel nicht erreiche. Also ich sage ihm zum Beispiel, ich möchte es unser Podcast in

**[00:18:56]** den Top 10 bis Jahresende steht und dann sagt er, ja okay, pass auf, das ist jetzt

**[00:19:02]** Jahresende, ihr steht nicht in den Top 10, was ist denn schiefgegangen und

**[00:19:06]** Versuchtes Rückwirkung zu analysieren, was könnte in einem Schiefgang sein? Das ist ganz lustig,

**[00:19:10]** nicht, weil ich das nur zur Unterhaltung auch lustig finde. Es ist auch ganz lustig,

**[00:19:13]** wenn du das auf Sourceboard anwendest. Sondern ich möchte eine sichere Sandbox in

**[00:19:17]** meiner Anwendung haben. Ich möchte eine sichere Lock-in-Maske. Ich möchte einen sauberen

**[00:19:20]** Korn-Send. Ich möchte keine Ahnung, was. Dann bringt der Dichter tatsächlich nochmal auf Ideen.

**[00:19:25]** Und wenn du ihm dann sagst, okay, er sagt nicht nur das Schiefgang in der Zeit,

**[00:19:30]** deswegen hast du es nicht erreicht. Er sagt auch, warum es Schief gegangen ist und

**[00:19:33]** was du dagegen hättest tun können. Und das kannst du wieder in den Loop schmeißen und sagen so,

**[00:19:37]** pass mal, obacht mein Freund, hast du denn daran gedacht. Im Idealfall sagt er, wenn es eben

**[00:19:43]** solche so eine Security-Ding gibt, wenn er sagt hier, die Daten nicht eingeben möchte,

**[00:19:46]** dass sie sicher sind, das ist ein sehr plumper Satz jetzt, dann sagt er, natürlich sind die

**[00:19:50]** nicht sicher, die sind nach sechs Monaten geliegt worden, weil du hast nicht verschlüsselt und

**[00:19:54]** du hast dies und das und jenes nicht gemacht. Und dann gibt es ihm das und sagt, guckt

**[00:19:58]** mal nach. Haben wir das denn gemacht? Und er sagte manchmal nein, aber er sagt auch häufig ja.

**[00:20:04]** Und es kommt nicht drauf an, dass er etwas findet, wo er ja sagt, das ist schönes Beruhigen. Die Punkte,

**[00:20:10]** wo er nein sagt, das sind die Punkte, die euch dann ruhig schlafen lassen, weil er hat es ja

**[00:20:14]** jetzt dann quasi wieder aufgegriffen. Und ich habe mir wirklich jetzt mittlerweile angewöhnt,

**[00:20:20]** jeden Abend zu sagen, wenn ich weibgecoated, engineered, die Maschine angeschrien habe,

**[00:20:25]** damit sie mir etwas baut, dass sie quasi aufschreibt, was hat sie getan, dass sie diesen kritischen

**[00:20:31]** Kritiker, den kreativen Kritiker, den er mal ausführt, dass ich daraus unter Umstände

**[00:20:35]** introduced für den nächsten Tag kriege und das wäre so der eine Tipp und der zweite

**[00:20:40]** Tipp ist, da muss ich ja meine eigene Nase packen, holt euch kein, wenn ihr privat

**[00:20:46]** coded Modell, das, ich sag jetzt mal so wie bei Entropic, Max 20 ist. Max 20 ist für

**[00:20:52]** Reiche, ja, wir hatten letztens gehört, dass der Jens mit seiner Open-Client-Situation

**[00:20:56]** jetzt von den Multimillionären gehört und einfach nur aus gut Will und Gönnerhaftigkeit

**[00:21:02]** uns hier jeden Montag beerrt.

**[00:21:03]** Aber er hat letztens eine Erklärung, warum das total gut ist, dass man nicht das Maximum

**[00:21:09]** an Plan hat.

**[00:21:10]** Work-Life-Balance.

**[00:21:11]** Wenn du ein System hast, das dich zwingt, ich fähre jetzt vom privaten Umfeld, ja,

**[00:21:18]** also mein dienstlich eh Arbeitszeitschutzgesetz, und hast du nicht gesehen, aber privatswingt,

**[00:21:22]** Dass du irgendwie eine Pause machen musst, dann hast du einen Grund, dich vom Bildschirm zu verabschieden.

**[00:21:27]** Weil ich merke es auch, es hat so ein bisschen die Endorphine deines Hirns, werden bedient von den Erfolgen deines Prometheks.

**[00:21:35]** Du schreibst und du entdeckst nicht neue Welten, wer denkt gleich Funktionen, UIs, sind sie.

**[00:21:42]** Also wir sollten ja ganz kurz, ich glaube, dass du mit dem Max 20 ermeinst, bitte hier unten einlenden.

**[00:21:46]** Genau, dass du mit dem Max 20 ermeinst, ist das im Prinzip, dass du sehr, sehr viele Tokens verbrennen darfst.

**[00:21:52]** Bevor das Stop-Schild gezogen wird, weil dein Internet auch gebraucht ist, genau so.

**[00:21:56]** Das ist nochmal wichtige Ergänzung, damit es klar ist.

**[00:21:58]** Entschuldigung.

**[00:21:59]** Also es ist gerade so ein bisschen so ein Thema, dass man sieht, dass das, was der

**[00:22:05]** Markt gerade beschreibt, so eine gewisse Suchtfaktor einfach ist, dass viele Leute, die etwas

**[00:22:10]** erstellen, ob das jetzt alle Themen rund um generative Eier, also nicht nur Codec,

**[00:22:14]** Videogenerierung, Bildgenerierung, man hat überall sehr, sehr schnell wahnsinnig gute Ergebnisse,

**[00:22:22]** die ein in so eine gewisse Art von Flow reinbringen, wie man mehr machen zu wollen. Und ich bin mir jetzt

**[00:22:29]** nicht ganz sicher, ob das Rate Limit, das man da hat, der einzige Faktor sein sollte, weil

**[00:22:34]** wenn es natürlich immer die Gefahr hat, dass man nachkauft und sich sagt. Aber irgendwie,

**[00:22:37]** ja natürlich ist es so ein bisschen so, dass die KIs, weil sie auch so ausgelegt sind,

**[00:22:42]** Ich natürlich auch gerne weitertreiben und ich hatte das in der einen oder anderen Folge auch schon

**[00:22:46]** mehr erwähnt. Ich habe meine persönliche Open Cloud Installation soweit. Das ist die aufgrund

**[00:22:51]** ihres Soul-MDs, also das Files, der so ein bisschen beschreibt, wie sie sich zu verhalten hat.

**[00:22:55]** Soweit ist sie, dass sie durchaus immer mal wieder guckt, was ist denn eigentlich die Tageszeit

**[00:22:59]** und auch aufgrund der Tageszeit dann auch schließt. Jetzt ist auch mal langsam Schlussjerns,

**[00:23:04]** ab ins Bett. Das heißt, da ist schon ein bisschen so ein Faktor, den man der KI auch

**[00:23:09]** beibringen kann. Also nicht nur dadurch, dass das Geld dann vielleicht mal flücken

**[00:23:11]** gegangen ist, weil man keine API-Kosten bezahlt oder das Rate-Limit bei irgendeinem Abo erreicht hat,

**[00:23:16]** sei es bei der Videogenerierung, der Text-Generierung, bei der Code-Generierung oder auch das, was man

**[00:23:20]** macht, sondern dass man das im Prinzip auch noch anraten kann. Ich finde, man kann da einiges

**[00:23:25]** Revue passieren lassen. Wir haben jetzt drüber gesprochen, schreibt auf, was wichtig ist in

**[00:23:28]** der Arbeitsfolge, schreibt auf, was an Entscheidungen, Decision, Records, ich muss das mal wiederholen drin,

**[00:23:35]** achtet ein bisschen auf eure Zeit, wie ihr mit den Systemen arbeitet. Das heißt,

**[00:23:40]** am Anfang traut euch, aber wenn ihr dann tiefer drin seid, gönnt euch eine Pause, weil es macht euch

**[00:23:47]** schon mit Schucke, wenn ihr den ganzen Tag da drin oben kodiert. Es ist zwar ein geiles Gefühl, muss

**[00:23:52]** ich ehrlicherweise sagen, beschäftige ich mich ja auch, ich habe auch mehr als einmal, sagen wir mal

**[00:23:56]** schon, einen Termin und Zeit vergessen. Nicht weil ich mich in irgendeinem Spiel verloren habe,

**[00:24:00]** sondern in einem, ja, eigentlich doch ein Spiel. Nur halt in diesem Spiel geht es halt um teilweise

**[00:24:05]** produktive Lösungen, teilweise um Experimente, teilweise um gemeinsames Lernen. Es bringt

**[00:24:12]** ja auch die Menschen wieder zusammen. Wir sitzen so häufig, wie seit Vibecoding sagten wir noch,

**[00:24:16]** nie in persönlichen oder in Remote-Meetings zusammen und haben auf denselben Bildschirmen

**[00:24:20]** geguckt und uns unterhalten und dabei gelernt. Das sind ja alles coole Dinge. Aber wo ich noch

**[00:24:28]** auskommen wollte, wo ich unbedingt noch in dieser Folge los werden will, ist auch der Punkt,

**[00:24:33]** sich nicht die Blöße zu geben und zu denken, oh verdammter Axt, das ist ja so ein Textfenster.

**[00:24:38]** Und egal wie das heißt, ja, Langdog und Entropic und Open AI und Gemini und wie es alles heißt,

**[00:24:44]** es kann auch gut sein, dass man irgendwann sich mal auf eine Lösung einlassen muss

**[00:24:50]** oder sollt oder kann, die nicht aussieht, wie diese klassischen Fenster, deren größtes

**[00:24:57]** Problem die Macht ist, die du mit ihnen hast, weil sie einfach alles können, ja. Du kannst

**[00:25:01]** mit diesen Chat-Fans einfach von Programme schreiben, über Dokumente analysieren, über Recherche machen,

**[00:25:06]** dich verarschen lassen, Gedicht bauen, keine Ahnung, vielleicht sind auch Lösungen adäquat,

**[00:25:13]** je nachdem für wen es ist, dass du fokussieren willst im dienstlichen Kontext. Wenn du nur,

**[00:25:19]** nur ist nicht abwertend gemeint, aber wenn du dein Job ist, Folien zu machen,

**[00:25:24]** dann ist dein Job Folien zu machen. Und vielleicht machst du noch zwei, drei andere Dokumentenarten,

**[00:25:28]** aber du machst halt jetzt nicht den Speiseplan, die Recherche um die Welt, die keine Ahnung war.

**[00:25:33]** Ja, das ist vielleicht ein blödes Beispiel, aber vielleicht jetzt trotzdem klar, was ich mein.

**[00:25:36]** Da kann es auch sinnvoll sein, Anwendungen einzusetzen, die ganz speziell auf diesen Case getrimmt sind,

**[00:25:42]** damit du dich nicht verläufst in der Nutzung, damit du auch ein Onboarding hast,

**[00:25:47]** in Form von, ich vertraue dem System, dass du das, was du auch mal sagst.

**[00:25:52]** Hey, ich glaube, das ist ein wichtiger…

**[00:25:54]** können, nicht verlieren. Dass wenn ich da auf Ender drücke, nicht fünf Millionen Kosten

**[00:25:59]** auf dem Tisch des Hauses liegen, meine Platte leer ist und am Ende noch die Mail vom System

**[00:26:03]** verschickt wird, der mag geschult. Auch da werden wir sicherlich immer mehr reininvestieren

**[00:26:09]** müssen, auch Menschen, Umgebungen zu bieten, nicht weil sie dumm sind, nicht weil sie es

**[00:26:14]** nicht lernen können, schlicht untergreifen, aber auch weil sie es nicht brauchen und

**[00:26:20]** weil sie eventuell sonst etwas haben.

**[00:26:22]** Ich sag mal, wenn du den ganzen Tag nage in die Wand haust,

**[00:26:26]** wird ja auch keiner einen Bagger vor die Tür stellen.

**[00:26:28]** Wie du hast so viel Wetten das geguckt,

**[00:26:31]** wo wahrscheinlich irgendwann mal in irgendeiner Folge ein Bagger...

**[00:26:33]** Ganz viel Wetten das geguckt.

**[00:26:34]** Bagger, wie es war, die Gewinne geschlagen hat.

**[00:26:38]** Aber ich weiß, was du meinst.

**[00:26:39]** Also, dass uns mal dein Aussage ist,

**[00:26:41]** dass wir das richtige Tool zum richtigen Zweck einsetzen

**[00:26:44]** und für die richtige Aufgabe, die man hat.

**[00:26:46]** Das ist natürlich immer schon ein Teil der menschenweißheit und auch unser menschenmöglichkeiten

**[00:26:54]** gewesen, das richtige zu wählen ein.

**[00:26:55]** Ich glaube, das macht uns auch einfach aus und das ist in der heutigen Zeit auch nicht

**[00:26:59]** anders.

**[00:27:00]** Also nicht für jeden ist es jetzt nötig das Hardcore-Auto-Complete-AI-Tool benutzen

**[00:27:05]** zu können, weil er dem Dinge aufgrund seiner Profession so weit vertraut, dass der auch

**[00:27:08]** so codet, dass da nichts Schlimmes passiert.

**[00:27:11]** Das sollte natürlich auch in der Hand derjenigen bleiben, die Ahnung von Programmierung haben.

**[00:27:17]** Auf der anderen Seite ist natürlich, und wir haben hier diese Folge aus ein bisschen Vibe-Coding.

**[00:27:21]** Wie geht denn das eigentlich genannt? Dass man sagen kann, was du gerade gesagt hast,

**[00:27:25]** ist halt ein anderer Aspekt des Lernens, des gemeinsamen Lernens.

**[00:27:29]** Und ich glaube, das ist ein Ding, das man immer noch gut machen kann.

**[00:27:31]** Also wenn man sich erst mal an dieses Thema ran traut, dann gibt es auch unterschiedliche Lösungen.

**[00:27:34]** Wir haben jetzt gerade schon von den ganzen großen Modellanbietern und sowas geredet.

**[00:27:38]** Es gibt natürlich auch noch Regulatoren, die da draußen sind, sowas wie Bolt oder Level Belt oder solche Themen,

**[00:27:44]** wo ich im Konzip dann auch ein bisschen aufgrund des Interfaces, die gestalten, also die Modelle halt im Hintergrund,

**[00:27:50]** ein bisschen einfacher quasi Anwendung auch bauen kann.

**[00:27:53]** Und ich glaube, das ist so ein Ding, man kann da einfach mal als White Coding-Anfänger so ein bisschen was ausprobieren erstmal.

**[00:28:00]** Das ist, glaube ich, das Wichtige und dabei lernen, wie denn eigentlich programmieren so funktioniert.

**[00:28:06]** Und dann auch jungen vielleicht mal so selber, wie du sagst, entweder bis dann auch irgendwo

**[00:28:10]** eine Grenze erreicht, wo man sagt, dann wird die Komplexität einfach zu groß, du hattest

**[00:28:14]** gerade so ein bisschen mit dem, den Menschen brauchen das vielleicht einfach nicht.

**[00:28:18]** Ich würde es immer sagen, ab einer gewissen Komplexitätstufe musst du halt eine tiefe

**[00:28:21]** Profession auch haben, um vielleicht die fachliche Komplexität, die dann auch durch

**[00:28:25]** Code entstehen kann, durch Software-Entwicklung und Software-Deployment und auch Verantwortung

**[00:28:29]** bezüglich Betrieb und Sicherheit und sowas.

**[00:28:31]** Kommt, das ist ja ein Prinzip, eine fachliche Verantwortung, die da ist, eine Profession,

**[00:28:35]** gelernt ist in dem Moment. Ich glaube, das ist so eine natürliche Grenze, die man sich ja selber auch

**[00:28:40]** immer setzen kann. Also ich werde jetzt auch nicht anfangen, Sterne kocht zu werden oder so was,

**[00:28:43]** nur weil ich mal dreimal in einer Woche nicht geschah, oder so ein Sterne, so ein Restaurant zu

**[00:28:47]** übernehmen, das werde ich fürchterlich scheitern. Dementsprechend, ich glaube, wir haben dann

**[00:28:51]** ein ganz gutes Gefühl für, aber traut euch auch an die Sachen ran. Also nehmt einfach mal ein Tool,

**[00:28:57]** sucht euch eins aus, fragt, nicht nur uns, fragt irgendwie euer Gemini oder irgendwas anderes,

**[00:29:03]** das, was man noch gut machen kann. Lass es euch vielleicht abgegleiten dabei. Guckt ein

**[00:29:07]** bisschen, dass das die KI kann euch dabei helfen. Das macht sie gerne. Sie beschreibt dann euch

**[00:29:13]** da, was passiert. Da habe ich noch ein Beispiel. Ich auch nicht. Manchmal muss man sie immer

**[00:29:19]** wieder dran erinnern. Manchmal vergisst sie das dann auch netterweise auch mal wieder,

**[00:29:22]** das zu tun. Aber erinnert sie durch dran oder macht euch ein Skill, den ihr ablegt.

**[00:29:26]** Da gibt es ja schon ein paar Folgen von uns, wie man das macht. Oder bestellt auch

**[00:29:30]** da, dass zusammen mit der KI, das ist ja schon so ein bisschen, werde ich ja weiß, auch

**[00:29:34]** so eine Art Programmierung, wenn man so einen ersten Skill angelegt, auch wenn es keine

**[00:29:37]** klassische Programmiersprache im Hintergrund ist. Aber man lagert etwas aus. Das ist so

**[00:29:41]** ein bisschen, was man in der Programmierung auch gerne macht, dass man sagt, gewisse Funktionalitäten

**[00:29:45]** lagere ich einen Platz aus. So ähnlich macht man das auch, wenn man jetzt mit einer KI

**[00:29:50]** mal ein Skill beschreibt und dieser Skill dann hinter von der eigenen KI muss. Dann

**[00:29:53]** das ist schon so eine Art, jetzt hören mich viele IT-Wahrer wahrscheinlich, Steining

**[00:29:57]** wollen, aber das ist schon so eine Art Programmierung.

**[00:29:59]** Wir wissen, wo Jens wohnt und ich bin käuflich.

**[00:30:03]** Jetzt, dass du gerade das auslagern und dass man da ganz

**[00:30:08]** viele Sachen machen kann, wieder ein Schwank aus dem Leben und eine Sache passend zum Podcast.

**[00:30:12]** Der Schwank aus dem Leben war, ich bin damals der Meinung gewesen, dass Philips U-Lampen

**[00:30:19]** total toll sind und ich habe mir von Philips U verschiedene Sachen geholt, Bewegungsmelde

**[00:30:24]** im Haus, Lampen. Das ganze Haus ist mit Philipsiolampen voll, ja. Und der Keller hat Bewegungsmelder

**[00:30:29]** von Philipsiol. Und ich habe dann irgendwann bereut, Philipsiol gekauft zu haben, weil

**[00:30:34]** der Bewegungsmelder im Keller, der hat die Eigenschaft, dass wenn der Bewegung registriert

**[00:30:39]** macht das Licht an, dann bleibt das Licht für die Zeit, die du definiert hast, an

**[00:30:42]** und dann geht es aus. Und wenn du zwischenzeitlich da langläufst, dann kriegt das der Melder

**[00:30:46]** zwar mit, aber es interessiert dich nicht. Der Counter wird nicht neu gesetzt. Da

**[00:30:50]** war ich mir ein bisschen frustriert. Irgendwann in einer Sektlaune heraus, mittlerweile ja

**[00:30:54]** viele Jahre vergangen, habe ich mein Problem Claude erzählt, weil ich dachte, Claude könnte

**[00:30:59]** mir vielleicht recherchieren, ob es da irgendwas gibt. Und dann haben wir ein bisschen hergeschrieben

**[00:31:03]** und dann Finger an, so nach dem Motto, drück doch mal jetzt bitte auf deiner Philips-View

**[00:31:08]** auf den Knopf. Und dann gehst du auf die Philips-View, drückst auf den Knopf und

**[00:31:12]** dann sag, Claude, so, hab mich mit deiner Philips-View verbunden, was wollen wir

**[00:31:15]** jetzt machen. Und dann hat er mein Bewegungsmelden im Keller beigebracht, dass das Licht

**[00:31:20]** bleibt. Und dann stehst du da und denkst, die Funktion war bei Phillips U selbst nicht vorhanden.

**[00:31:25]** Er hat sich da irgendwie selbst durchgezeigt und hat das da irgendwie hingekriegt und du stehst

**[00:31:30]** da und denkst, am Ende mal. Also jetzt habe ich vielleicht ein bisschen viel diskutiert mit Chad

**[00:31:34]** und so. Aber eigentlich habe ich mit Sprache mein Smart Home gerade verbessert. Ob das jetzt

**[00:31:41]** mein Schwiegervater auf die Reihe kriegt. Schwiegervater, falls du das hörst,

**[00:31:43]** nix gegen dich. An dieser Stelle bitte jeden aus der Familie oder Bekanntenkreis eintragen.

**[00:31:48]** Smart Home ist immer irgendwie Pain hinzustellen, wenn du dir eine Mischung von Anbietern hast.

**[00:31:53]** Also Apple, HomeKit und Philips U und ZigBee und HomeKit, da bist du ja am Ende.

**[00:31:59]** Aber dann hast du auf einmal eine Möglichkeit, dass das Ding nimmt dir die Komplexität weg.

**[00:32:03]** Das war das eine. Und das zweite, ich verlinke es in den Show Notes definitiv,

**[00:32:08]** weil wir haben noch keine schöne Domänen haben. Wir haben ja auch ein Vibecoding-Projekt,

**[00:32:12]** das gerade am Start ist, nämlich ein Page, die auf GitHub gehostet wird.

**[00:32:17]** auf der die Transkripte hoffentlich auch die besseren Transkripte, weil das die

**[00:32:23]** Transkripte unserer Podcast-Folgen hat die ganze Zeit Podigy, also unser Podcast-

**[00:32:27]** Hosting-System gemacht, das muss ich noch umstellen, aber wir haben eine kleine

**[00:32:32]** Page-Vibe-Code lassen, die die Folgen der Vergangenheit zeigt, die wird immer

**[00:32:38]** Dienst-DUcks automatisch aktualisiert, dann findet ihr die Transkription

**[00:32:43]** aller Folgen, ihr findet ein Webplayer da drüben, ihr könnt auch auf Englisch

**[00:32:47]** umschalten. Da gehört ja nicht uns in Englisch, aber ihr kriegt die Transkripte unserer Folgen

**[00:32:51]** in Englisch. Er hat ein paar Mechanismen, unter anderem ein Feedback-Formular, damit ihr uns

**[00:32:57]** schreiben könnt. Wir können suchen, ihr könnt Folgen teilen, ihr könnt aber auch, wenn euch

**[00:33:03]** der ganze HackMack nicht interessiert und ihr lieber auf das Thema eingehen wollt, dass

**[00:33:07]** ich am Anfang sagte, schreibt auf, was ihr tut, macht euch den Tizen. Ihr könnt auch alle

**[00:33:12]** folgen in deutsch-wien englisch als marktlondertei herunterladen falls eure lm systeme daran sich

**[00:33:19]** ergötzen wollen was wir bei uns cooles gemacht haben jens mehr habe ich nicht ich bin tatsächlich

**[00:33:24]** durch für heute ich habe ganz viel anekdoten bringen können habe mich heute beim einstieg der

**[00:33:29]** folge plammiert hoffentlich zur mitte der folge reputiert hast du noch was und es wäre ich

**[00:33:34]** echt durch ich bin glaube ich auch so weit durch also außerdem dass ich nochmal wiederholen

**[00:33:40]** will, dass ihr nicht, Weitkoning muss nicht dafür da sein, dass ihr die nächste neue Super-App

**[00:33:46]** oder etwas anderes macht. Es ist vielleicht auch einfach...

**[00:33:48]** Falls doch, dann die Hemen bitte an die unten eingeklemmt.

**[00:33:51]** Nein, ach so schade. Aber, weißte, also ihr macht auch die kleinen, guckt nach kleinen

**[00:33:55]** Lösungen, die ihr braucht. Hier, das ist vor kurzem auch schon mal erwähnt. Ich habe

**[00:33:58]** mir auch irgendwo einfach so einen PDF-Kumpremierer mal gebaut, damit Sachen komprimit werden.

**[00:34:03]** Also so, häufig hat man ja so kleine Sachen, die man irgendwie automatisieren will, wo

**[00:34:07]** man ein kleines Software-Stück braucht, da könnt ihr immer wieder überlegen, kann ich

**[00:34:11]** das nicht eigentlich nachprobieren? Oder habe ich irgendwelche Anwendungsfälle zu Hause,

**[00:34:15]** die ich immer wieder mache, Sachen, die ich immer wieder wiederholt, einsortieren muss,

**[00:34:21]** Dokumente, Rechnung oder irgendwas anderes? Da kann man ein bisschen mal mit Code rumspielen,

**[00:34:26]** gucken, was da funktioniert. Mit Geminal rumspielen kann ich da nicht etwas automatisieren,

**[00:34:30]** um vielleicht auch meine Mails zu erfassen, irgendwas anderes. Das ist alles hinterher

**[00:34:34]** so ein bisschen Art. Ich würde mal sagen interagieren mit dem Computer. Es ist nicht immer direkte

**[00:34:38]** Programmierung in dem Sinne, dass ein Stück Code irgendwo steht, der sich auch die Plurio

**[00:34:42]** irgendwas anderes sind, sondern es kann auch mal Workflow sein, den er euch zusammenschustert.

**[00:34:46]** Traut euch einfach, da Sachen zu machen, weil ich glaube, das ist das, was wir auch in dieser

**[00:34:50]** Folge vermitteln wollten. Das Thema KI geht nicht weg. Das macht Spaß, wenn man sich mit beschäftigt.

**[00:34:56]** Das hat gefahren, aber lasst euch da nicht irgendwie immer ins Boxhorn jagen, dass das irgendwie,

**[00:35:01]** wenn ihr da was tut, die ganze Welt zusammenbericht, sondern guckt, da gibt es genug Sachen, wo

**[00:35:06]** man sich ausprobieren kann, wo man sich probieren kann.

**[00:35:08]** Mark lacht schon wieder, das bedeutet, er hat doch doch was.

**[00:35:11]** Ich sag schon mal, bis zum nächsten Mal.

**[00:35:12]** War das nicht Marco fürs Liebstenmal?

**[00:35:13]** Wer ein Buch geschrieben hat, als der Attacker, neben die Oma das Internet abschaltete oder

**[00:35:17]** irgendwie sowas, falls ich das falsch zitiert habe, könnte es ihm ja sagen, vielleicht

**[00:35:21]** Marco unsere Fortausfolge verlinken, ich kenn ihn ja eigentlich sonst über sein,

**[00:35:25]** also kenn nicht, ne, ich hab ja sonst schon mit den Kengerokroniken und so einen

**[00:35:28]** Kram zu tun.

**[00:35:29]** damit schweifen wir ab.

**[00:35:31]** Seine Meinung zu KI habe ich auch mal letztens beim Chaos Computerclub irgendwie Vortrag mal gehört,

**[00:35:35]** weil jetzt, ich sag mal, für die freischaffende Künstler allgemein schwierig, aber das verstehe ich natürlich.

**[00:35:41]** Jens, war schön, dass du da bist. Wir sind in der Folge eingestiegen mit dem Satz,

**[00:35:45]** dass wir noch eine zweite Folge heute aufnehmen.

**[00:35:47]** Das machen wir jetzt nämlich auch. Unser Gast kommt gleich.

**[00:35:50]** Vorher muss ich aber noch schnell mein Akku laden.

**[00:35:51]** In diesem Sinne, euch allen einen schönen Abend, einen schönen Tag,

**[00:35:55]** Eine schöne Woche, wir hören uns dann bald wieder und lasst uns gerne ein Kommentar und bis bald, ciao.

**[00:36:01]** Bis bald, ciao.

**[00:36:04]** Willkommen bei ThinkDifferent, ThinkAI, dem Podcast von Mark und Jens.

**[00:36:09]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:36:16]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:36:23]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:36:27]** K.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
