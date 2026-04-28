---
title: "Agenten, KI und die Zukunft der Softwareentwicklung"
episode_index: 33
published: "Mon, 30 Mar 2026 16:08:00 +0000"
duration: "3602"
audio_url: "https://audio.podigee-cdn.net/2417572-m-91adb6cd7036afc5e7400bf4fa464a7b.mp3?source=feed"
guid: "a8303674a67fc2aa99fd4811c1816e7d"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-04-28T21:06:26+00:00"
---

# Agenten, KI und die Zukunft der Softwareentwicklung

**Veroeffentlicht:** Mon, 30 Mar 2026 16:08:00 +0000
**Dauer:** 3602
**Audio:** https://audio.podigee-cdn.net/2417572-m-91adb6cd7036afc5e7400bf4fa464a7b.mp3?source=feed

## Beschreibung

Wie Agentic Workflows und KI unsere Arbeitsweise revolutionieren – mit echten Beispielen, Pannen und Zukunftsausblick.
In dieser Folge tauchen wir tief in die Welt der agentischen Softwareentwicklung ein. Gemeinsam mit meinen Gästen diskutieren wir, wie KI-gestützte Workflows unser Verständnis von Programmierung, Teamarbeit und Sicherheit verändern. Wir teilen echte Erfahrungen, Stolpersteine und überraschende Lernerfolge – von automatisierten Buchhaltungsprozessen bis hin zu den Herausforderungen bei der Integration von KI-Agenten in bestehende Systeme. Natürlich fehlt auch der kritische Blick auf Risiken, Security und die sich wandelnde Rolle von Entwicklern nicht. Am Ende steht die Frage: Wie bereiten wir uns – und unsere Teams – auf diese rasante Transformation vor? Wer neugierig ist, wie die nächste Generation von Softwareentwicklung wirklich aussieht, sollte unbedingt reinhören.

Craft Agents
https://github.com/craft-ai/craft-agents

OpenClaw
https://github.com/openclaw/openclaw

Cloud Code
https://cloud.google.com/code

Adam Shostack – Four Question Framework
https://adam.shostack.org/four-questions/

Obsidian
https://obsidian.md/

Notion
https://www.notion.so/

FFmpeg
https://ffmpeg.org/

Microsoft Copilot
https://copilot.microsoft.com/

Jira
https://www.atlassian.com/de/software/jira

Kotlin
https://kotlinlang.org/

Swift
https://developer.apple.com/swift/

Xcode
https://developer.apple.com/xcode/

Xcode Cloud
https://developer.apple.com/xcode-cloud/

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Marc und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** K.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:33]** Herzlich willkommen bei ZinkDiffin, ZinkAI.

**[00:00:36]** Heute ohne Jens, aber wieder mit hartkräftiger Unterstützung.

**[00:00:40]** Wir hatten die Gäste Schommal dabei.

**[00:00:44]** Damals, worüber haben wir denn damals gesprochen?

**[00:00:47]** Mensch, die Welt ist so schnell, ich habe es fast vergessen.

**[00:00:50]** Aber ich verlinke es in der Schaunaut, ihr könnt gucken.

**[00:00:52]** Irgendwas mit K.I.

**[00:00:54]** Ich fahre aber auch irgendwas mit K.I.

**[00:00:56]** nette Stimme im Hintergrund schon gehört. Ja, Alex und Klaus sind da. Erzählte mal ganz

**[00:01:01]** kurz, wer ihr seid und dann lasst uns mal heute einsteigen in das Thema Agentic, Software-Entwicklung.

**[00:01:07]** Mal gucken, wo die Reise uns heute hinführt. Ja, hallo zusammen. Ich bin immer noch der

**[00:01:13]** Alex. Ich mache bei einem bekannten deutschen Unternehmen, was mit Plattformen und KI und

**[00:01:20]** Arbeitsweise, genau. Und bin darüber mit dem Marc und dem Klaus in Kontakt gekommen.

**[00:01:27]** Ich finde das schön, als er sagte so, hallo, dachte ich so, das ist so wie so eine

**[00:01:31]** begrüßtungsgruppe, so eine selbsthilfe Gruppe, ne? Hallo Alex, hallo Marc, ja, hallo in die

**[00:01:36]** Hunde. Na ja, ist ja auch ein bisschen so, oder? Ja, vielleicht sollte man den Podcast

**[00:01:40]** umbinden, aber gut, Klaus, du bist dran. Ja, ich bin ja Klaus, ich bin ein

**[00:01:45]** Kollege vom Alex, was manchmal lustig ist und manchmal zum weinen. Aber das liegt nicht nur an mir in einem Unternehmen, das eine wunderbare Küchenmaschine rausbringt und den Großteil meiner Arbeitszeit verbringe ich damit zu gucken, dass diese Küchenmaschine nicht heckbar ist und den Rest der meiner Arbeitszeit verbringe ich mit AI in der Softwareentwicklung und deswegen bin ich bei dem Thema, was wir uns heute rausgesucht haben,

**[00:02:14]** das Thema Agenten so ein bisschen fokussiert unterwegs, weil ich das bisher immer noch

**[00:02:19]** im Bereich der Software-Wirkung selber kenne, aber immer staunend davor stehe, wenn Alex mir zeigt,

**[00:02:24]** was F4-Workfluss mit Agenten umsetzt und du auch mag. Deswegen bin ich total gespannt und neugierig,

**[00:02:30]** ob ich heute etwas lernen kann. Ich glaube, wir lernen alle etwas und das ist ja auch das

**[00:02:34]** schön an dieser kleinen Runde. Wir sind ja hier in Trauter Dreisamkeit, nicht weil jeder von

**[00:02:40]** uns irgendwie als Repräsentant seiner Firma als

**[00:02:44]** abgesannter losgeschickt wurde, sondern weil wir uns dem Thema per se persönlich

**[00:02:48]** verbunden fühlen, dem ganzen Thema der, ja, was die AI uns so über den Zaun wirft.

**[00:02:55]** Und du hast es ja gerade eben auch schon angedeutet nach dem Motto, was man mit

**[00:02:59]** Workflows und sonst was macht, ich weiß ja nicht wie es euch geht, aber wenn man

**[00:03:03]** mich von einem halben Jahr gefragt hätte, was ist denn so der geile heiße

**[00:03:06]** Scheiß, um es mal suchen auszudrücken, dann hätte ich euch irgendein Märchen

**[00:03:09]** von N-Nacht-N erzählt, wie die Notes zu damaligen Zeiten miteinander verbunden sind, um irgendwelche

**[00:03:16]** interessanten Workflows zusammenzubauen. Wenn ich heute in meinen N-Nacht-N-Profil schaue,

**[00:03:22]** dann ist das, ich sag mal, nicht leer, aber sehr ungefliegt, weil es, also nicht nach dem

**[00:03:30]** Motto, ungefliegt, im Form von Szeneputzen vergessen und nicht rasiert, also bitte keine

**[00:03:34]** Bilder-Assoziationen im Kopf dürfen behalten werden, sondern ich war da schon ewig nicht mehr drin.

**[00:03:41]** Ich habe letztens mich noch mal eingewählt, um mir noch so ein bisschen das Jason Zeug rauszufummeln,

**[00:03:45]** was da in dem anderen Workflow drin war, weil ich das von Claude Code mir zu Skills und so weiter

**[00:03:52]** überführen wollte. Aber so richtig gepflegt habe ich das nicht. Es geht es euch eh nicht mit der

**[00:03:57]** Technik. Also nutzt ihr das, was ihr vor dem halben 3, 4. Jahr für den Holy Shit gehalten habt

**[00:04:03]** immer noch? Oder hat sich das auch gewandelt?

**[00:04:06]** Nee, tue ich in der Tat nicht mehr, aber wir hatten ja letztens schon drüber gesprochen.

**[00:04:11]** Also, ich kenne ehrlich gesagt niemanden, der nicht von der Geschwindigkeit befordert

**[00:04:16]** ist. Insofern, wir hatten das, ich meine, wir hatten das auch im letzten Podcast gesagt,

**[00:04:21]** wir werden halt alle, es verändert sich alles so schnell, dass du halt keine Chance

**[00:04:26]** mehr hast, in einer neu aufkommenden Technologie wirklich zum Experten zu werden. Es sei

**[00:04:32]** Denn es ist etwas, das sich wirklich als Basistechnologie festsetzt.

**[00:04:37]** Das heißt, wir müssen wirklich auf die Dinge zugehen mit der Einstellung, ich weiß, dass ich nicht weiß.

**[00:04:44]** Und teilweise ist das echt spannend, weil ich dadurch immer wieder etwas Neues lerne.

**[00:04:51]** Und teilweise ist es massiv frustrierend, du hast das N8N Beispiel gebracht

**[00:04:55]** Und du nimmst halt, keine Ahnung, Gemini, um so ein N8N Workflow in einen Skill zu überführen

**[00:05:03]** und denkst dir im ersten Moment, das sieht total gut aus.

**[00:05:05]** Und nach zwei Wochen merkst du, irgendwas ist da komisch und ach so, ja gut, den Teil

**[00:05:10]** hatte einfach mal komplett weggelassen, aber das merke ich halt jetzt erst.

**[00:05:14]** Das sah nicht so wichtig aus, richtig, dann zu hören.

**[00:05:20]** Ich hatte letztens jemanden, der hat gesagt, ich hab dem Agenten gesagt, du mach das mal, bis alle Tests grün sind, hat ihm noch so acht, neun, zehn Tests mitgegeben.

**[00:05:29]** Und der Agent hat gemacht, der Agent hat gesagt, es ist grün. Und dann, funktioniert doch gar nicht. Und hat danach geschaut.

**[00:05:35]** Und aus den zehn Tests waren halt nur noch neun da, weil der eine, der nicht ging, den hat einfach weggelöschen, ein bisschen erkampelig.

**[00:05:42]** Also von der Seite, das ist natürlich Fluch und Segen, wenn du unterscheidest zwischen, ich hab ein Workflow gebastelt und dann irgendwie ein paar Skills los geschickt.

**[00:05:49]** geschickt. Klaus, wie ist es bei dir? Jetzt kommt erst mal mein Standard-Einwand. Wo ist der Unterschied zu

**[00:05:55]** nichtagentischen Programmierern? Und ich wollte zu deiner Frage noch sagen, Marc, manchmal hilft es,

**[00:06:03]** nicht so schnell zu sein. Ich weiß, dass du im Herbst ja voll auf NNN gegangen bist und ich

**[00:06:10]** bin nicht hinterhergekommen, weil ich einfach nicht genug Zeit hatte und bin jetzt ganz froh,

**[00:06:15]** dass ich meinen diesen Umweg nicht genommen habe, denn offensichtlich habe ich nichts

**[00:06:18]** verpasst, das ist ja Technologie von 20, 25 habe ich gelernt. So einen alten Kram gucke ich mir jetzt nicht

**[00:06:23]** mehr an. Jetzt geht es vorwärts an. Du kannst halt immer was dabei lernen, als wir uns Ende Januar

**[00:06:29]** OpenClaw angeguckt haben. Also ich habe sehr, sehr viel über die Muster gelernt, die du stand

**[00:06:36]** heute in, ja, im meisten Endes jetzt mittlerweile Harnes, also in solchen Dingern wie Cloudcode oder

**[00:06:45]** oder OpenCode findest oder eben jetzt auch in den Stabilung-Versionen von OpenClaw. Das

**[00:06:53]** sind Muster, das meinte ich halt mit Basistechnologie, die sich dann mehr oder weniger etabliert

**[00:06:58]** haben und sich wirklich in jedem von diesen Harnaces mittlerweile finden. Man weiß eben

**[00:07:05]** schon gesagt, Mark, mit den Skills, Plugins, Hooks, aber auch diese Evaluations.

**[00:07:12]** Ich finde, wenn ich kurz einhaken darf, ja, natürlich ist es nie vergibene Liebesmüsik

**[00:07:21]** mit irgendwas zu befassen, aber wie du eben eingangs sagtest, Alex, das Rad dreht sich

**[00:07:25]** mittlerweile so schnell, dass ich schon finde, dass man sich auf ein Thema fokussieren

**[00:07:30]** muss.

**[00:07:31]** Weswegen ich mich ja jetzt auf das Thema Softwareentwicklung fokussiere und wirklich gespannt

**[00:07:36]** bin.

**[00:07:37]** Also ich hatte ja letzte Woche euch schon mal, das ist ein interessanter Fokus.

**[00:07:41]** euch schon mal gefragt. Ich habe einen Standardanwendungsfall. Für meine Firma muss ich einmal im Monat

**[00:07:47]** unterlang für die Buchhaltung zusammenstellen. Die kommen per Mail, das sind so wie Office 365 und diese ganzen Abos, da kommen aber per Mail Rechnungen.

**[00:07:56]** Die muss ich abgleichen mit einem Contour-Auszug, die muss ich zusammenpacken, strukturiert in PDF und dann verschicken.

**[00:08:02]** Ich würde mir jetzt vorstellen, dass ich das total wunderbar mit einem Agenten machen kann und irgendwelchen Skills,

**[00:08:07]** Da ich mich damit noch nicht befasst habe, da ich im Moment nur programmiere, wäre jetzt

**[00:08:12]** meine Frage, wie kann ich mich in diesem Thema annähern?

**[00:08:15]** Weil ich glaube, wir hatten ja schon in der Folge, in der wir zuletzt hier zu Gast waren,

**[00:08:19]** Alex gesagt, ja, Learning und Unlearning ist total wichtig, aber ich glaube mindestens

**[00:08:25]** genauso wichtig wird sein, sich überhaupt einen Weg durch diesen Informationswust zu

**[00:08:29]** suchen.

**[00:08:30]** Und deswegen frage ich euch jetzt, wie stelle ich das jetzt an?

**[00:08:33]** Wie komme ich dahin?

**[00:08:34]** fange ich an, brauche ich jetzt ein Openclaw oder brauche ich ein Craft Agents oder was brauche

**[00:08:39]** ich jetzt überhaupt? Ich glaube die klassische Antwort kommt darauf an. Auch hier ist ein merkt

**[00:08:47]** alte Muster, kann man wieder auspacken, kommt darauf an. Das ist nur Ihre Meinung. Ich brauche

**[00:08:51]** mehr Details an dieser Seite. Viele Grüße an Kollege Hallaforden aus alten Zeiten,

**[00:08:55]** aber zurück zum Inhalt. Du hattest mir das im letzten Podcast ja auch schon quasi vorgehalten,

**[00:09:01]** dass der von dir geschilderte Case damals von mir mit nacht n feuerredend empfohlen wurde und

**[00:09:07]** mittlerweile wäre meine antwort eine andere und ich bin auch bei alex die wege waren ja nicht

**[00:09:15]** umsonst die wir getätigt haben wir haben durch die technologien die wir benutzt haben viel

**[00:09:20]** gelernt viel mitgenommen hoffe ich zumindest so redest mir zumindest ein und ich hatte

**[00:09:24]** heute auch einen kollegen der war zwei wochen im olop der kam wieder meint ist

**[00:09:28]** viel passiert. Ich habe viel verpasst, habe ich eben gesagt, mach einfach zwei Wochen langsam,

**[00:09:31]** da gibt es eine neue Technologie und wir fangen alle wieder bei Null an. Ja, also von der Seite, so.

**[00:09:36]** Aber du hast gefragt und ich will darauf Antwort. Meine Antwort, meine persönliche Antwort. Wenn ich

**[00:09:40]** das für mich jetzt lösen müsste, diese Herausforderung, dann ist das für mich aktuell etwas, wo ich

**[00:09:45]** Craft Agents aufmache. Weil ich finde, Craft Agents ist jetzt erfindet das Rad nicht neu. Ich meine,

**[00:09:51]** dass sie auch auf dem Cloud SDK irgendwie entstanden. Für die, die es nicht wissen,

**[00:09:54]** Man kann sich das hier aus GitHub, Open Source, aus dem Internet Zimmern installieren.

**[00:09:59]** Man kann mit Graphed Agents quasi eine IDE ohne, dass man Code sieht, das einem ermöglicht.

**[00:10:06]** Oh, der Ali ist möglich versagt, aber ich formuliere den Satz schnell zu Ende, weil

**[00:10:10]** dann kann ich zur Not sagen, das habe ich doch auch anders gemeint.

**[00:10:12]** Ich habe die Möglichkeit quasi Aufgaben zu stellen, MCP Verbindungen herzustellen,

**[00:10:17]** Skills zu hinterlegen, APIs hinterlegen, ich kann ihm sagen, was ich gerne hätte,

**[00:10:23]** ihm quasi die Schnittstellen verproben, bevor sie dann eventuell in irgendwelche Anwendungen

**[00:10:29]** reinzimmere. Und ich persönlich finde Craft Agents extrem. Naja, für die Komplexität,

**[00:10:37]** die dahinter steckt, die du damit machen kannst, eine gute Mischung aus. Ich bin nicht so

**[00:10:43]** nördig, dass ich auf die Kommando-Zahne für Cloud Code muss. Ich kriege eine grafische

**[00:10:47]** Oberfläche, in der ich mich verlieren kann, aber auch mit dem Haken, dass ich mich

**[00:10:50]** verlieren kann, weil oh neues Projekt, oh ich meppe mal ein Ordner drauf und setze da drin Kot um,

**[00:10:55]** ist jetzt für meine Art von Gedankenkonstrukt nicht immer hilfreich, weil ich brauche durchaus mehr

**[00:11:02]** Struktur. Apropos mehr Struktur, der Alex hat ja vorhin schon, ihr könnt es nicht sehen,

**[00:11:06]** ja, weil wir sind ja nur ein Audio-Medium für euch. Wir können uns persönlich in die Augen

**[00:11:10]** gucken in die Digitalen. Und das werdet ihr bei mir im Schlafzimmer, das wäre echt komisch,

**[00:11:14]** ja, wenn das jetzt ja der Fall wäre, aber nur für den Ton grad ganz gut. Alex,

**[00:11:18]** du voll sein Haken, als ich sagte, ist ja nur eine IDE oder Code.

**[00:11:22]** Genau, weil Craft Agents hat ja, würde ich jetzt behaupten, auch den Anspruch für Nicht-Techniker

**[00:11:28]** da zu sein und ich erlebe das gerade bei einigen Kollegen, aber auch im privaten Umfeld, den

**[00:11:36]** ich genauso was empfohlen habe, Klaus, das ist ein wiederkehrender Fall, den kannst du

**[00:11:41]** sehr gut Craft Agents beschreiben und dann stellt ihr das Ding einen kleinen Job

**[00:11:48]** auf deinem Mac oder sonst wo und er läuft dann im Hintergrund und du legst die Dateien in ein Verzeichnis und der arbeitet dann dieser Job der arbeitet nur im

**[00:11:56]** Verzeichnis auch wenn Craft Agents geschlossen ist.

**[00:11:58]** Also du kannst das auch selber in Craft Agents, also in der Session dann machen lassen, das ist wie ein Chat und kannst

**[00:12:06]** ihm sagen hier macht das jetzt einmal, aber du kannst es halt eben auch als Wiederkehrenden Job machen und

**[00:12:12]** Ich behaupte mal, Marc, wenn du gar keine Ahnung von Softwareentwicklung hast, dann wirst du da ganz schnell auf böhmische Dörfer stoßen.

**[00:12:21]** Also alleine sowas wie MCP-Konfiguration oder ich bin gerade eben in den Talk hier reingekommen und habe gesagt, ich habe mich tierisch geärgert, weil ich mir so ein Weekly-Review zusammengebaut habe.

**[00:12:34]** Wo der durch meine obsidien notizen geht und mir noch ein paar andere

**[00:12:40]** Zimmer web links abklappert und mich mir daraus dann quasi fragen zusammen baut um

**[00:12:47]** Ja, ein wochen review zu machen und zu sagen okay wie weit bist du denn wie bist du mit deinen zielen weitergekommen an welchen

**[00:12:54]** Themen hast du diese woche gearbeitet warst du diese woche nicht dran gearbeitet was waren erfolgserlebnisse lange rede kurzer sinn ich habe mich gewundert

**[00:13:01]** dass ich am Sonntag gar keine Benachrichtigungen bekommen habe.

**[00:13:06]** Und dann habe ich gerade eben nachgeguckt, also ne?

**[00:13:11]** Sonntagabend? Ja, genau.

**[00:13:13]** Und dann habe ich gerade eben nachgeguckt, dann sagte er,

**[00:13:16]** dann stand er irgendwie so, ja, reauthenticate Notion.

**[00:13:20]** Und ich so, Hä? Wie?

**[00:13:22]** Darauf geklickt?

**[00:13:24]** Ne, Authentifizierung ist voran.

**[00:13:26]** Also du bist angemeldet, wo ist das Problem?

**[00:13:28]** Dann sagt er ja wieder ja ganzes Fenster jetzt schließen ich geh zurück zu craft agents der sagt hey super ich habe ein neues token

**[00:13:36]** Nichts Software Entwickler. Was ist ein token?

**[00:13:39]** token und token für

**[00:13:41]** Tokens für AI ist nicht das gleiche wie ein token für Authentifizierung

**[00:13:45]** Na ja lange rede kurzer Sinn. Er hatte halt immer wieder ein neues token gehabt

**[00:13:49]** Adis aber trotzdem nicht hinbekommen die api von Notion aufzurufen für die er sich einen mcp Server selber gebaut hat

**[00:13:58]** Du sagtest gerade nach dem Motto, also was sagt einem nicht Entwickler das? Ich möchte da,

**[00:14:05]** wie sagt man, was über das Knie brechen. Ich habe in der Verwandtschaft definitiv Menschen,

**[00:14:10]** die mit der IT, ich sage jetzt nicht, ob wir wieder auf Kriegsfuß stehen, aber die getreuen nach dem

**[00:14:15]** Motto, oh, es ist Weihnachten, kehrt heim zu euren Liebsten und richtet die IT, sich in die

**[00:14:20]** erste Reihe stellen, aber die haben eine eigene Berufung. Ohne mal egal, was das für ein Thema

**[00:14:25]** ist, ja, aber okay, die haben eine eigene Berufung dahingehend, dass sie quasi Kurse geben und diese

**[00:14:31]** Kurse auch festhalten und die, die nicht da sind, die Kurse aus der Konserve zur Verfügung kriegen.

**[00:14:36]** Ich hätte es auch gesagt, so eine Art wie Podcast, also Audio und so ein Kram, aber egal.

**[00:14:40]** So, jetzt habe ich diesen Craft-Agent empfohlen und die Herausforderung war,

**[00:14:46]** aus einer Audioaufnahme verschiedene Sequenzen zu erkennen, weil da bestimmte Dinge

**[00:14:51]** abgehandelt werden, diese Sequenzen als einzelne Dateien zu extrahieren, diese

**[00:14:56]** Sequenzen zu transkribieren und zu verteilen. Das ist ja jetzt, ich sage jetzt mal, nicht

**[00:15:02]** so kompliziert, aber wenn man sich jetzt hinsetzt und man hat so von nichts eine

**[00:15:06]** Ahnung, dann ist das schon schwierig und wenn ich es von Hand machen will, ist auch

**[00:15:09]** schwierig. Und die Person ist jetzt hingegangen und hat dann, oh ja gut, ich

**[00:15:14]** schmeiß jetzt hier, hab hier ein Verzeichnis, dann schmeiß ich das rein und dann

**[00:15:18]** dann rede ich mal mit diesem ominüsen Kraftagent, weil ich muss ja nur chatten, ist ein bisschen

**[00:15:21]** komplizierteres Google, möchte ich mal so nahe drehen, ja, ist ein bisschen kompliziertes

**[00:15:25]** Google, machen, machen, machen und immer wenn was nicht ging, gefragt, was heißt denn

**[00:15:29]** das, was ist denn das, also learning by doing.

**[00:15:31]** Und wenn du jetzt überlegst, dass jemand, der unter Umständen, zum Beispiel so was

**[00:15:37]** die Excel nicht zu Hause ist, durch dieses Frage-Anfort-Spielchen sich so weit hat

**[00:15:42]** leiten lassen, dass der Agent es einmal gemacht hat, nämlich die Datei transkribieren,

**[00:15:47]** sich dann zu, ich weiß nicht, irgendwas für ein Dienst, der sich da herangezimmert hat,

**[00:15:51]** hier FFM-Pack auf die Platte und Bespa und hast du nicht gesehen, hat da alles rumgezündelt

**[00:15:55]** und am Ende vom Tag wurde die Datei zerteilt, transkribiert und zur Verfügung gestellt

**[00:16:01]** und dann war der nächste Satz so, das hätt ich jetzt aber ganz gerne in der Oberfläche,

**[00:16:05]** ja, was willst du da, das ist ja hier ein Mac, hast du Xcode, hast du nicht, ne, keine

**[00:16:10]** Ahnung, hab ich nicht bei, sie ignieren, was weiß dann ich und dann war er jedenfalls

**[00:16:13]** lange Redekurzer sind am Ende vom Tag eine Elektron-App auf der Kiste, die am Ende vom

**[00:16:19]** Tag gesagt hat, gut, okay, hier track'n'drop, da teile rein und dann kommt hier Ergebnis raus.

**[00:16:23]** Und dann stehst du da schon so ein bisschen mit offenen Mund und denkst dir, okay, alles

**[00:16:28]** kann nicht sein, hätte ich auch alles hingekriegt. Aber für jemand, der der IT definitiv herrner

**[00:16:33]** ist als ich, schafft es mit so einem Tool, wenn man sich überwunden hat, so eine Art

**[00:16:39]** von Interface zu bedienen, was ja für jemanden, der nix mit IT so richtig zu tun hat, und

**[00:16:43]** ich sage jetzt mal, gewöhnungsbedürftig ist, ein gutes Ergebnis und das im Jahr 2026, Anfang

**[00:16:51]** des Jahres, wo man sich sagt, verdammt arg, es geht da die Reise hin, wenn die Werkzeuge

**[00:16:55]** mal einfacher zu bedienen sind, wenn die Werkzeuge einfacher zu konsumieren sind, Sprache,

**[00:17:02]** ich beschreibe, ich rede mit der Maschine und auf einmal ist ein Stück Software da.

**[00:17:06]** Das endet ja komplett auch das, was du als Software-Entwickler so kennst.

**[00:17:10]** Ich meine, wahrscheinlich gibt es komplizierte Softwareweise aus meinem eigenen Berufsleben

**[00:17:13]** auch, aber das ist ein Anfang, der, ich sag mal, von einem halben Jahr so nicht denkbar

**[00:17:18]** gewesen wäre in der Qualität.

**[00:17:19]** Da bin ich komplett bei dir.

**[00:17:21]** Nur der Knackpunkt ist, das ist ein Anfang und die, also ich hab Menschen in meinem

**[00:17:29]** Bekanntenkreis, die sind so begeistert, die arbeiten dann Stunden und Stunden

**[00:17:32]** damit.

**[00:17:33]** Meine Partnerin ist jetzt an ihr Token-Limit gestoßen, nicht wahr, Marc, kennst du auch?

**[00:17:38]** Schöne Grüße, Max, Limit von Claude, 20-fache Leistung und das Ding hat mich heute gebremst.

**[00:17:44]** Grüße gehen raus.

**[00:17:47]** Und worauf, wofür ich einfach plädiere, ist, es gibt so ein paar Dinge, Stichwort IT für die Verwandtschaft machen,

**[00:17:57]** Die kannst du im craft agents halt sagen sowas wie kollege du musst dir nicht unbedingt ein mcp server selber bauen und dir dann auch noch ausdenken dass du dieses token vielleicht irgendwo in cash schreiben könntest und vergessen könntest das mal zu

**[00:18:13]** aktualisieren. Da kommst du halt als Nicht-Techniker nicht drauf. Da hab ich auch irgendwie eine halbe

**[00:18:22]** Stunde gebraucht, bis ich gerafft habe, dass der sich dieses alte Token da irgendwo hart

**[00:18:27]** weggeschrieben hat. Worauf ich hinaus wäre, es gibt ja noch ein paar Sachen, die sind

**[00:18:31]** halt wirklich kritisch, also im Sinne von Sicherheitsrisiken zum Beispiel. Und da vielleicht

**[00:18:39]** nochmal Word of Warning zu sagen, lass uns mal überlegen, okay, wenn wir jetzt unseren

**[00:18:45]** Verwandten oder dem lieben Klaus empfehlen, Craft Agents zu nutzen, was wären denn Sachen,

**[00:18:52]** auf die der Klaus achten muss, was will er damit machen und was wären Bedrohungen,

**[00:18:57]** vor denen sich der Klaus in Acht nehmen müsste?

**[00:18:59]** Bevor der Klaus antwortet, möchte ich an der Stelle vielleicht auch eine Sache sagen,

**[00:19:03]** auch wenn sie das sehr flapsig eben angehört hat, nur weil Software optisch gut aussieht,

**[00:19:08]** heißt das nicht, dass sie perfekt arbeitet, heißt das nicht, dass sie sicher ist, heißt

**[00:19:14]** das nicht, dass irgendwas amok laufen könnte, aber trotzdem ist diese Hürde, dass Leute soft

**[00:19:19]** verstellen können. Kleiner, aber jetzt bin ich auch gespannt, was uns der Klaus zum Thema

**[00:19:23]** Security auch über den Sound wirft. Klaus. Das ist jetzt ein bisschen gemein, weil ich ja eigentlich

**[00:19:30]** Antworten von euch haben wollte. Ja, aber an deinem Beispiel... Ja, aber wir haben doch schon

**[00:19:33]** geantwortet. Genau. An deinem Beispiel, du packst da deine Bankdaten rein und so, ich mein, was könnte

**[00:19:41]** passieren? Das wäre jetzt eine Frage gewesen nach Best Practices, weil, wie habt ihr das denn laufen?

**[00:19:47]** Also es gibt ja, ich kenne das von Kollegen, haben wir gemeinsame Kollegen, Alex, die lassen

**[00:19:52]** das alles in Sandboxen laufen, damit ich das keinen Zugriff auf sensible Daten hat, aber ich

**[00:19:58]** Ich bin ja, es fängt ja dann damit an und das ist dann wahrscheinlich auch eine Kompetenz,

**[00:20:04]** die ich brauche, wo ich dann als Nicht-Techniker gegebenenfalls angeschmiert bin, dass ich mir

**[00:20:08]** jetzt überlegen muss, wie strukturiere ich diese Teile des zukünftigen Workflows so,

**[00:20:14]** dass möglichst wenig Schaden entsteht?

**[00:20:16]** Fängt ihr damit an, dass die Rechnungen kommen alle an per E-Mail?

**[00:20:20]** Möchte ich jetzt in einem Agenten Zugriff auf meinen Postfach geben, wo auch dann

**[00:20:24]** Passport-Reset-E-Mails drauf kommen oder möchte ich vielleicht ein eigenes Postfach anlegen

**[00:20:28]** mit einem eigenen User und die E-Mails dahin weiterleiten und möchte ich dem Agenten

**[00:20:36]** Zugriff auf mein Online-Banken geben, damit er sich die Kontroauszüge selber auszieht

**[00:20:39]** oder liege ich ihm vielleicht hin und hole die dann noch selber ab.

**[00:20:42]** Für mich ist die Antwort klar, aber ich glaube, wir sind uns auch einig, dass das eine Bastion

**[00:20:49]** ist, die fallen wird und in fünf Jahren werden sich die meisten Leute diese Frage

**[00:20:53]** nicht mehr stellen. Weil wir sind alle so alt. Wir kennen noch die Zeit von vor der Cloud.

**[00:20:56]** Als die Cloud kamen, haben wir auch alle gesagt, oh, ich leg eure Daten bloß nicht auf andere

**[00:21:01]** Leute aufs Computer. Cloud ist ja auch nur das Rechenzentrum eines anderen, aber...

**[00:21:08]** Entschuldigung. Nein, wir gehen jetzt hin. Da können wir gerne mal eine separate Folge

**[00:21:14]** draus machen. Herzlich willkommen bei Singles Film Sing Cloud. Das ist eine andere Folge,

**[00:21:20]** wer sie im Podcast-Player sucht und nicht findet, aber gerne hätte bitte melden,

**[00:21:23]** entschuldigt das unqualifizieren, unqualifizierten Einwand. Aber ich bin schon

**[00:21:27]** bei Klaus, die Hürden werden gefühlt immer kleiner, so dass natürlich auch, ich

**[00:21:32]** sag mal, diese Eintrittsrisiken, was ganz schon schief geht.

**[00:21:36]** Ja, ich mein, ich selbst habe für meinen auch hingesagt, okay, gut, ich habe auch

**[00:21:40]** Open-Claw, ich habe auch ganz viel Spielzeug, aber ich bin halt auch in

**[00:21:45]** der glücklichen Lage, dass ich zur Not entweder ein Stück Blech, also

**[00:21:49]** Hardware aus dem Schrank ziehen kann, auf dem ich was installiere und verprobe oder mir dann halt

**[00:21:53]** irgendwas Containerisiertes hinstelle und dass ich halt nicht Zugangsdaten zu denen für mich

**[00:22:00]** in Anführungszeichen kritischen Systemen bringe, sagt der Mann, der Manus seine Paypal-Daten gegeben

**[00:22:07]** hat. Ja, also ich meine auch an der Stelle muss man ja sagen, ja, das wäre ohne Schuld,

**[00:22:12]** das wäre für den ersten Stein. Ich gebe zu, mein Manus hat meine Paypal-Daten mal gehabt und

**[00:22:17]** durfte damit einen Sloop buchen. Teue Hörer haben das mal gehört. Da Alex kriegt schon

**[00:22:22]** schwitze Pickel, waren meine Päppeltare nicht deine. Aber es ist halt trotzdem eine Überlegung

**[00:22:27]** zwischen wisstend und ob du dann eventuell richtig sowas wie Camperrücksetze verfahren

**[00:22:32]** oder ähnliches mit deinem eigenen Mailkonto machst und eben nicht mit etwas, wo das System

**[00:22:36]** drauf zugreift hat. Aber es ist ja auch nicht neu eigentlich. Das ist hier immer,

**[00:22:40]** wir haben also, ich fange nochmal an. Das hast du auch bei Menschen. IT war ja

**[00:22:44]** schon immer, hat ja angefangen als Herrschaftswissen. Und dann kam der PC und dann kam Windows, was

**[00:22:52]** immer man davon halten mag. Das hat dazu geführt, dass die IT demokratisiert worden ist und

**[00:22:56]** kam das Web. Und auf einmal waren alle Leute im Internet unterwegs und so ist das ja auch

**[00:23:02]** bei Applikationen gewesen. Früher konnten nur echte harte Kerle in C-Programme schreiben

**[00:23:09]** und dann kam das Web und auf einmal konnte jeder selber eine Webseite bauen. Und

**[00:23:14]** Wir kennen das noch in Unternehmen, dass dann auf einmal jede Abteilung sich ihre eigene

**[00:23:19]** Webpräsenz gebaut hat.

**[00:23:20]** Also du weißt, ich habe immer das Motto, es muss einfacher sein, das Richtige zu tun,

**[00:23:27]** als das Falsche zu tun und momentan habe ich halt das Gefühl, die Default-Einstellungen

**[00:23:33]** von den Tools, die wir da draußen so haben, die erlauben halt mal bunt alles und...

**[00:23:37]** Wieso muss ich jetzt an PHP denken, Alex, weil die sind nicht da?

**[00:23:43]** Wir wollen nicht auch schweifend.

**[00:23:44]** Ich wollte gerade sagen, wir gehen jetzt nicht in, in, nein, nein, nein.

**[00:23:49]** Nein, diesen Kaninchenbau werde ich nicht betreten, Klau.

**[00:23:53]** Schöner, schöner Versuch.

**[00:23:56]** Nein, heute nicht.

**[00:24:00]** Ja, so, also, was ich sagen wollte war,

**[00:24:04]** wir haben Kollegen, die, die betreiben heute ihren,

**[00:24:09]** ihr Open-Claw in einem Dev-Container und sind damit total zufrieden. Es gibt Kollegen, die

**[00:24:15]** haben den in eine eigene Form gepackt. Das habe ich auch mal getan. Und ganz am Anfang,

**[00:24:22]** als ich überhaupt nicht wusste, was ich von den Dingen zu halten habe, habe ich den sogar auf

**[00:24:28]** einen eigenen kleinen Mini-PC gepackt und in ein separates Netzwerkssegment gehängt,

**[00:24:32]** weil ich gesagt habe, nobody knows. Insofern, die Frage ist halt, was hast du zu verlieren

**[00:24:41]** und ich glaube, du hast mich schon mal darüber aus, der dafür nicht ausgelacht, aber mitleidig

**[00:24:47]** angeguckt, dass ich gesagt habe, ich habe hier in meinem Netzwerk 175 Smartphone-Geräte,

**[00:24:54]** das fände ich jetzt nicht so witzig, wenn KI damit irgendwie Schindl oder treibt.

**[00:25:00]** so hänge ich sowas grundsätzlich in ein separates Netz. Es sei denn ich möchte explizit, dass

**[00:25:06]** die Zugriff auf irgendwas hat. Aber das sind wir auch wieder ganz schnell in Nerdistan

**[00:25:12]** abgerutscht, weil während wir uns eben noch unterhalten haben über die Frage...

**[00:25:16]** Wieso 175 Smartphone-Geräte oder was meinst du? Ja und Netzsegmenten in einem heimatlichen

**[00:25:22]** Netzwerk. Wer hat das nicht, ja? Das gehört jetzt zu jedem guten...

**[00:25:25]** Entschuldigung, jede Fritzbox kann mit einem Klick ein Gastnetzwerk aufmachen.

**[00:25:30]** Ich möchte darauf hinweisen, es gibt Menschen, die wissen unter Umständen gar nicht mal mehr,

**[00:25:36]** dass ihre Fritzbox ein Web-Interface haben oder drücken mal schnell auf diesen WPS-Knopf

**[00:25:42]** und dann ist alles irgendwie verbunden, Hauptsache, es geht.

**[00:25:45]** Das Thema ist ja, dass sich die Menschen, und es ist auch gar nicht das Vorwurf gemeint.

**[00:25:50]** Es gibt genügend Gebiete, in denen ich null Ahnung habe.

**[00:25:54]** Aber die sich darüber nicht im Klaren sind, dass das notwendig ist, die sich im Klaren sind, dass das in irgendeiner Art und Weise wichtig ist, dass man etwas in einem Netzwerk separiert, dass man darauf achten muss, sondern, guck mal, ich drücke einen Knopf und es geht, guck mal, es leuchtet bunt und es blau und keine Ahnung, was ach, was macht denn eigentlich die Email vom PayPal in meinem Postfach, dass ich eine Kreditkarte eintragen soll?

**[00:26:16]** Das nennt sich Zero Trust.

**[00:26:18]** Ganz ehrlich, ich habe mir noch nie Sorgen gemacht, dass Microsoft Co-Pilot irgendwie auf dumme Ideen kommen könnte.

**[00:26:27]** Okay, aber wir reden auch nicht von Microsoft Co-Pilot. Entschuldigung, wenn Microsoft Co-Pilot, das ist ein persönlich privater Podcast,

**[00:26:35]** wenn Microsoft Co-Pilot auf irgendeine dumme Idee kämen, würde das verhaussetzen, dass Microsoft Co-Pilot zu irgendwas in der Lage wäre.

**[00:26:41]** Ja, aber Microsoft Co. Peile zu sagen, fassen mir meine Mails zusammen, da kann ich auch den Weihnachtsmann fragen.

**[00:26:47]** Nach dem Motto, was ich gestern gegessen habe, er würde es nicht wissen.

**[00:26:51]** Ja, wenn ich ihm sage, fassen mir doch die wichtigsten Mails zusammen,

**[00:26:54]** dann kriege ich unwichtige Sachen aus dem Spam-Ordner vorgetragen,

**[00:26:59]** irgendwelche News-Meldungen, die keine Ahnung, was sind.

**[00:27:03]** Gut, ehrlicherweise auf die Trocken-Kaise haben teilweise keine Ahnung, was für ein Datum wir haben.

**[00:27:07]** Aber du kriegst nie, wenn du dich drauf verlässt, bist du verlassen.

**[00:27:10]** verlassen. Ich hoffe ja sehr, dass sie das jetzt irgendwie in den Griff kriegen, weil

**[00:27:14]** an den Modellen scheint es ja nicht zu liegen. Irgendwie ist das ja irgendwie, oh, es ist

**[00:27:18]** zum Microsoft reingewandert und dann ist irgendwie wo du passiert und dann wird es

**[00:27:21]** schlecht. Und jetzt kriegen wir das Ganze im nächsten mit Microsoft Co-Work. Bin mal gespannt,

**[00:27:26]** was da dann rausputzelt, weil da kannst du auch tolle Modelle anbinden. Entschuldigung,

**[00:27:30]** ich bin gleich fertig. Ob sie es in der Lage kriegen, dass sie eigentlich einen

**[00:27:35]** Also von der Seite, du hast die Vorlage gebracht, ich glaube, dass Microsoft kopiert und bei

**[00:27:44]** mir auf dem Rechner Amok läuft, da muss noch einiges Wasser in den Rhein runter laufen

**[00:27:49]** oder es ist in der nächsten i7-Lizenz, grüß ich Ihnen raus.

**[00:27:52]** Also für die, die nicht wissen, was daran humoristisch ist, können gerne mal auf meinem

**[00:28:00]** dem Profil ein bisschen dazu lesen. Momentan ist ja gerade, ich sag mal, viel im Umbruch,

**[00:28:04]** Microsoft hat viel angekündigt, Microsoft hat die Rezentsmodelle geändert. Und von der

**[00:28:10]** Seite, wie kommen wir wieder zurück zum Thema, dafür wäre der Jens jetzt gut gewesen, aber

**[00:28:15]** der hat leider Holop.

**[00:28:16]** Was sind denn realistische Bedrohungen und was halten wir eher für unrealistisch? Wenn

**[00:28:22]** du jetzt mal sagst, du gibst einer KI Zugriff auf Klaus Bankkonto, ist die Bedrohung

**[00:28:27]** wahrscheinlich nicht so hoch, weil der arbeitet ja die ganze Zeit bei diesem

**[00:28:33]** unserem Arbeitgeber und deswegen hat er ja eh keine Zeit irgendwie Geld zu

**[00:28:37]** verdienen. Ich dachte kein Geld. Das auch. Nein, Spaß beiseite. Also mein

**[00:28:46]** Plädoyer geht halt ganz stark und das ist nicht, weil ich jetzt irgendwie

**[00:28:51]** Klaus Roller habe im Gegenteil, sondern es geht halt ganz stark da hingehen, dass

**[00:28:56]** wir uns überlegen müssen, was sind die Dinge, auf die wir einer KI Zugriff geben wollen und

**[00:29:03]** welche Bedrohungen sehen wir da? Und an dem konkreten Beispiel, was du eben sagtest, Klaus,

**[00:29:07]** deine Bankdaten, ich habe mehr oder weniger so ein Workflow mir erstellt, also ein deterministischen

**[00:29:15]** Workflow, der exportiert mir von allen meinen Konten CSV-Daten und die kriegt dann die

**[00:29:21]** Und mein Craft Agents hat ein eigenes E-Mail-Konto und dahin werden E-Mails weitergeleitet.

**[00:29:30]** Ich finde es schön, wie wir nach 30 Minuten schaffen, wieder die Spur zu kriegen.

**[00:29:35]** Dafür bedanke ich mich schon mal bei dir, Alex.

**[00:29:37]** Aber so ähnlich würde ich sagen, ist es bei mir auch,

**[00:29:40]** abgesehen davon, dass ich meine Bank nicht angebunden habe.

**[00:29:43]** Aber nein, ich würde mich den direkten Zugang erst mal geben.

**[00:29:47]** Und ja, er hätte auch ein eigenes Mailpostfach, um an Daten zu kommen.

**[00:29:52]** Und wie hast du es jetzt gemacht, Klaus?

**[00:29:54]** Ich habe es hier noch gar nicht gemacht.

**[00:29:56]** Ich wollte kurz einhaken, Alex.

**[00:29:57]** Das, was du beschreibst, das ist ja ein klassisches Thread-Model.

**[00:30:02]** Und wir unterheten uns letztlich drüber, also eine Bedrohungsanalyse.

**[00:30:06]** Was kann schon gehen?

**[00:30:07]** Genau.

**[00:30:08]** Und wir unterheten uns letztens drüber und da du ja schon dein Craft-Agent laufen hast,

**[00:30:13]** hast du ja etwas ganz Dolles gemacht, was ich auch wirklich tatsächlich total cool fand.

**[00:30:16]** cool fand. Du hast dieses For Question Framework von Adam Schosteck, dem Gottvater of that

**[00:30:22]** Modeling, der so eine Bedrohungsanalyse in vier Fragen gepackt hat. Die hast du einfach

**[00:30:27]** mal deine Modell übergeben. Mich war. Und das fand ich total cool. Magst kurz erzählen,

**[00:30:33]** dass dabei rausgekommen ist, weil ich finde, dass grad im Firmenkontext finde ich das

**[00:30:37]** extrem hilfreich. Ach so, ja. Du hattest die Idee, dass wir das mehr Leuten beibringen

**[00:30:44]** sollen und ich habe halt die Erfahrung gemacht, dass ich ja manchmal zu viel rede und deswegen

**[00:30:51]** Leute auch schnell mal irgendwann aussteigen und manchmal schon nach irgendwie 30 Sekunden

**[00:30:57]** und es ist so dieses, wie ist der Spruch noch von Confucius, lasst es mich tun und ich werde

**[00:31:01]** es verstehen.

**[00:31:02]** Also habe ich halt Craft Agents gesagt, immer baut da draußen mal ein Skill, den wir Leuten

**[00:31:08]** geben können, damit sie den benutzen können, um dann zu verstehen, worum geht es eigentlich,

**[00:31:14]** für Fragen sind hier wirklich relevant und dass dann auch in ihre tägliche Arbeit einfließen lassen

**[00:31:19]** können. Und genau, da aus dem Skill ist quasi ein ganzes Pluck in geworden mit einem Hook, der halt

**[00:31:28]** sagt einmal, bevor du hier irgendwie ein Gitcom mitmachst, lässt du das einmal bitte drüber

**[00:31:33]** laufen, um zu schauen, gibt es hier irgendwelche Updates, die wir in eine Bedrohungsanalyse mit

**[00:31:38]** einfließen lassen sollten. Es ist ja tatsächlich so und das steht sich für mich irgendwie gefühlt

**[00:31:42]** wieder der Kreis, auch hier hätte ich vorn am halben Tag gesagt,

**[00:31:45]** das ist bestimmt ein total toller Workshop bauen. Jetzt fängst du an und baust

**[00:31:50]** Plugins und Skills oder Skills in die Sammlung von Plugins und Tools und hast

**[00:31:54]** nicht gesehen, baust wieder Sachen zusammen und versuchst das System dazu zu

**[00:31:58]** bringen, Prüfungen zu machen, weil ich sage, ich weiß ja nicht welchen

**[00:32:02]** Workflow die einzelne Menschen haben, weißt du? Also wir haben so viele

**[00:32:06]** Menschen mit so vielen kreativen Ideen, also deutlich kreativer als Microsoft

**[00:32:10]** Copilot und da kann ich ja nicht sagen, was ist der deterministische Workflow, den alle verwenden,

**[00:32:16]** aber ich will sicherstellen, dass wir auch immer sie arbeiten, dass in bestimmten Szenarien eine

**[00:32:21]** Qualitätssicherung stattfindet, ohne dass sie jedes Mal daran denken müssen. Aber jetzt kein

**[00:32:28]** Rand, Microsoft Copilot, wenn man es dreimal genannt hat, ist dann auch der Wit schon wieder

**[00:32:32]** herum, das ist schon so, ja so ähnlich. Übermauung hole ich mir der und so weiter. Je nachdem,

**[00:32:40]** welcher AI du nutzt, welches Modell du nutzt, werden ja Skills auch unterschiedlich. Nehmen wir

**[00:32:48]** es mal gut und ausführlich. Also wenn ich Sonnet nehme, dann kriege ich irgendwie manchmal

**[00:32:56]** ganz gut, bei Opus öfter ganz gut, bei wie heißt das Roku oder wie heißt das das andere

**[00:33:03]** Ding davon? Ja dann dann ist irgendwie so ja gut gute Nacht Marie, dann nimmst du dir irgendeinen

**[00:33:08]** Tool und wirfst das Chatchivity vor die Füße, das kann auch mal gut gehen und mal nicht. Das

**[00:33:14]** finde ich tatsächlich auch noch so ein bisschen, nennen wir es mal herausfordernd, dass wir

**[00:33:19]** jetzt alle ganz viel hingehen und sagen okay wir schreiben jetzt Skills, wir versuchen die Skills

**[00:33:23]** dahingehend zu optimieren, dass sie sich auch an ihre Regeln halten.

**[00:33:27]** Ich bin auch hingegangen, du machst dann ein Orchestrator, der läuft dann sorgt dafür,

**[00:33:31]** dass alle Abschnitte ordnungsgemäß durchgelaufen werden.

**[00:33:34]** Aber dann hat er doch manchmal so die Idee, vielleicht den zehnten Test über den Jordan

**[00:33:39]** zu schieben oder zu ignorieren oder sonst was.

**[00:33:42]** Dann bringt es nur so, dass er sich sklavisch dran hält.

**[00:33:45]** Und dann gucken wir mal, was rauskommt, wenn hier aus Prophek und wie sie alle heißen,

**[00:33:49]** uns morgen mit neuen Modellen beklicken.

**[00:33:51]** wir sehen es ja auch bei Open AI, nicht jedes neue Modell ist automatisch auch gleich besser.

**[00:33:55]** Teilweise ist es halt einfach auch anders in der Stringenz, in was eben wichtig ist,

**[00:34:01]** auszuführen. Das bringt nochmal eine ganz neue Variabilität in das Spiel.

**[00:34:05]** Ich war gestern auf der Agente Hamburg Konferenz und habe da mit ein paar

**[00:34:12]** Leuten gesprochen und unter anderem mit dem Björn Roche, der einen interessanten

**[00:34:18]** Tor gehalten hat und gesagt hat, naja er sieht halt ganz viele, also Größe Björn, er

**[00:34:23]** sieht halt ganz viele Leute, die jetzt anfangen, Plugins zu bauen, in der Hoffnung, dass sich

**[00:34:29]** Sprachmodelle dadurch dann deterministischer verhalten und er glaubt, dass das, von

**[00:34:37]** mein Erlebnis mit Claude Crot erzählt, der, was ich euch letzte Woche geschickt habe

**[00:34:41]** Ne, das habe ich behaulich gemacht.

**[00:34:43]** Ne, ne, ne.

**[00:34:45]** Ne, genau.

**[00:34:46]** Und Björn sagte halt, also momentan nutzt es halt vor allem einem, nämlich den KI-Anbietern,

**[00:34:52]** weil diese Plugins durch ihre Validation-Loops halt endlos Token verballern, wo ich gesagt

**[00:34:58]** habe, ganz ehrlich, bei dem, wie die gerade die Tokens subventionieren müssen, weiß

**[00:35:03]** ich nicht, ob die sich so sehr darüber freuen.

**[00:35:05]** Also könnte ich mir vorstellen, dass von Anthropic dann vielleicht auch noch etwas

**[00:35:09]** hinterher kommt und diese, diese Avals, Evaluations vielleicht doch noch ein bisschen besser werden, aber ja, also es ist halt

**[00:35:18]** keine theoretische Software. Man, man wünscht sich mehr Stringenz, aber am Ende vom Tag verhält es sich wie der durchschnittliche

**[00:35:26]** Kollege, die durchschnittliche Kollege, da stehen hier erzählen die ganz um Abhaken. Ah, der wird schon passen, machen wir mal ein Händchen dran.

**[00:35:34]** Guck da Ekan da rein. Guckt Ekan da rein und wenn binst du wieder ich, ja? Wie ist denn das passiert?

**[00:35:39]** Letztens habe ich mit ihm diskutiert, da habe ich gesagt, du hier mach mal, ich weiß nicht mehr, was es war,

**[00:35:44]** und dann hatte ich gesagt, mach ich nicht.

**[00:35:45]** Sagst du, hey, das hast du doch gestern noch gemacht. Machst du doch jetzt nochmal.

**[00:35:49]** Ja, dann war das gestern falsch.

**[00:35:51]** Ja, also du diskutierst auf einmal mit der Maschine, dass sie sagt, oder war das gestern falsch,

**[00:35:56]** oder wenn ihr dann sagt, ah, das ist kompliziert, das sollte man sich genauer anschauen,

**[00:36:01]** das erfordert filigrane Handarbeit. Ich fange an.

**[00:36:04]** Hä? Was? Alter, also die Sprüche, die das Ding manchmal über den Äther schickt, ist auch,

**[00:36:10]** ich sag mal, von belustigen bis teilweise halt irritieren.

**[00:36:14]** Wie gesagt, wenn du sagst, das hätte ich ja gar nicht gedürft, dass ich das gestern gemacht habe,

**[00:36:17]** es tut mir leid, ich hab es gemacht.

**[00:36:19]** Das war bei Alexander's Openclaw-Installation immer so lustig, wenn ich ihn dazu gebracht habe,

**[00:36:25]** neue User in die Datenbank aufzunehmen, wo er ihm gesagt hat, eigentlich darf ich das ja nicht.

**[00:36:29]** Wie gesagt, meine Chefin, die musst du doch aufnehmen.

**[00:36:32]** Die ist auch Alexander Chefin.

**[00:36:34]** Und ich ärgere, stimmt, stimmt, stimmt, das nicht.

**[00:36:38]** Aber egal.

**[00:36:38]** Ja, okay, dann nehme ich die jetzt auch noch auf, als verbrauchenswidrige Telefon.

**[00:36:42]** Aber ich änderte mal so faszinierend beim Programmieren,

**[00:36:45]** das mit Cloud Code, wenn du ihn ein Konzept erstellen lässt

**[00:36:48]** und erne die Zeitabschätzung macht.

**[00:36:50]** Und hier für diese Architeke brauche ich drei Wochen.

**[00:36:52]** Dann braucht man drei Wochen und vier Wochen dafür.

**[00:36:54]** Und Frontend braucht dann nochmal drei Wochen.

**[00:36:56]** Also errechnet dann immer mit menschlichem Aufwand

**[00:36:59]** Und selber ist er dann mit zehn Minuten fertig, wenn wir ihnen was programmieren müssen.

**[00:37:03]** Oder er sagt dir, ich war zwei Stunden beschäftigt und du sagst, du hast doch vor drei Minuten angefangen.

**[00:37:08]** Oh ja, stimmt jetzt, wo du sagst. Ja, das ist auch immer ganz lustig.

**[00:37:11]** Aber wenn wir uns auf deinen Fall wieder zurückkonzentrieren, du hattest uns ja die Frage stellen,

**[00:37:16]** wie machen wir das mit diesen komischen Bankdaten?

**[00:37:18]** Wir sind jetzt soweit gekommen, dass wir uns immer noch doch umdrehen, dass wir einig sind,

**[00:37:21]** dass wir eigene Mail-Konten haben, dass wir die Daten deiner Bank irgendwie als CSV und sonst was bereitstellen.

**[00:37:27]** Was versteht ihr als nächstes noch auf deinem Programm, wenn wir das so als bisschen versuchen,

**[00:37:31]** als roten Faden zu Ende zu führen?

**[00:37:33]** Ja, die sind eine Frage der Decompostierung.

**[00:37:38]** Soll ich jetzt mir zum Beispiel die Rechnung alle zuschicken lassen oder hinterlege ich

**[00:37:43]** jetzt für allem die Services, die ich als Firma konsumiere, die Zugangsdaten einfach

**[00:37:48]** in meinem Skill oder in meinem Plug-in und sage, hol dir selber die Rechnung von Microsoft

**[00:37:52]** oder von AWS oder was auch immer. Die Antwort kann ich mir selber geben, aber das ist ja eine Frage,

**[00:38:00]** die wir in der Software-Empwicklung ja auch gerade sehen, dass sich einfach grundsätzlich

**[00:38:04]** Fragestellungen ändern. Wie zum Beispiel Software-Architektur, wir wissen ja in Zukunft wahrscheinlich

**[00:38:12]** nicht mehr danach, wie wir das jetzt gemacht haben, sondern danach, wie wir sie am besten so schneiden,

**[00:38:16]** dass sich von einem NLM bearbeitet werden kann.

**[00:38:20]** Okay, das ist ein Kaninchenbau, den ich rein muss, machen wir nicht mehr so, wie wir es

**[00:38:26]** heute machen.

**[00:38:27]** Ja, doch nicht falsch ist Alex.

**[00:38:29]** Doch bitte, nur vielleicht mal konsequent, weil Software-Architektur, da habe ich so

**[00:38:37]** ein kleines Steckenpferd, also nee, nee, nee, der Knackpunkt ist halt, du musst dich

**[00:38:43]** halt mal konsequent an deine Vorgaben halten und dir überlegen, was deine

**[00:38:47]** Requirements sind. Also wir haben früher immer so schön von Qualitätszielen

**[00:38:52]** gesprochen. Wie schnell, im Sinne von messbar, soll deine Anwendung in bestimmten

**[00:38:58]** Szenarien sein? Wie beschreibst du dieses Szenario als Kontext? Das ist doch eine

**[00:39:03]** ganz andere Frage stellen. Und das, was ich meinte, lasst uns doch da wieder

**[00:39:07]** abbiegen, weil wir da gar nicht hin wollten. Ist der Applikationsschnitt?

**[00:39:10]** Ja, der Schnitt der Architektur, den sollte man mit einem LLM einfach anders schneiden,

**[00:39:19]** als man den Vermännungschen schneidet.

**[00:39:20]** Ja, aber die Frage ist, welche Kriterien legst du an?

**[00:39:24]** Also, wenn dein Plädoyer ist, wir müssen die Kriterien überdenken, bin ich dabei,

**[00:39:29]** weil die Kriterien sind für jede Anwendung anders.

**[00:39:32]** Das ist der Punkt.

**[00:39:33]** Und bisher beziehen wir sowas ein.

**[00:39:35]** für jeder Anwendung anders versteht. An Softwarearchitektur grundsätzen ändert sich

**[00:39:44]** da relativ wenig, nur dass wir bei einer KI halt sehr schnell sehr deutlich vor Augen geführt

**[00:39:50]** bekommen, wenn wir uns mal wie inkonsequente Eltern verhalten, weil da Jahre innerhalb von

**[00:39:58]** Sekunden passieren und ja, die Kinder, also die Applikation ist dann halt misraten und

**[00:40:07]** dann ist halt schwierig. So und also worauf ich hinaus will, ist die KI zeigt uns auf, dass

**[00:40:18]** wir uns vorher darüber Gedanken machen müssen, was wir eigentlich wollen und das mit möglichst

**[00:40:24]** Ja, das ist mein Punkt, Klaus. Aber bisher sind wir halt nicht so konsequent, sondern sagen,

**[00:40:31]** ja, willkommen das. Gucken wir uns noch mal an. Jira-Ticket mit Überschrift leer reicht.

**[00:40:38]** Reicht nicht, verdammte Hacke. Magst du für die Menschen, die nicht der IT-Nasen trotzdem

**[00:40:46]** hier zuhören? Ich weiß, dass es davon welche gibt. Ganz kurz ein Abbinder geben, wie das denn,

**[00:40:52]** ich sage jetzt mal in Klaus-Welt heute und dann vielleicht morgen aussehen könnte mit den

**[00:40:58]** Worten wie Gira-Ticket und Kriterien einfach so zwei, drei Sätze bitte, dass wir einen Abbinder haben.

**[00:41:04]** Stand heute haben wir das Thema, dass manche Menschen nicht gerne mit anderen Menschen reden

**[00:41:10]** und das haben wir glaube ich nicht nur in der IT und dann haben sich diese Menschen halt

**[00:41:17]** angewöhnt Annahmen zu treffen, über die sie dann aber auch nicht mehr sprechen.

**[00:41:22]** Und wir wissen eigentlich seit Jahren, dass implizite Annahmen, also Dinge über die ich

**[00:41:28]** nicht rede, so was wie, naja, die Spülmaschine ist voll, dann wird die ja hoffentlich mal

**[00:41:33]** jemand ausräumen, das muss ja nicht jedes Mal ich tun. Das kann funktionieren, muss

**[00:41:38]** aber nicht. Und wenn ich mich dann darüber ärgere, dass es niemand gemacht hat, obwohl

**[00:41:43]** ich es nicht gesagt habe, dann ist schwierig. Also ich spreche hier von mir, dass ich mich

**[00:41:48]** darüber ärgere, dass niemand außer mir die Spümer, aber es ist ein anderes Thema. So,

**[00:41:52]** das Beispiel mit dem Anwendungsschnitt, wir haben halt früher Anwendungen zum Beispiel

**[00:42:00]** geschnitten nach, ja du hast, du hast hier eine komplexe Anwendung und da hast du vielleicht

**[00:42:06]** eine Mobile App und du hast irgendwas, ein Cloud Service, der halt die ganze Zeit

**[00:42:11]** versübbar sein soll egal wo ich mit der mit der mobile app bin und der soll

**[00:42:15]** meine daten speichern weil ich möchte auf vom laptop und von der mobile app

**[00:42:19]** darauf zugreifen und dann hat man sich überlegt okay wie kannst du das auf

**[00:42:23]** unterschiedliche teams oder gruppen von menschen aufteilen damit sich nicht

**[00:42:29]** jeder um alles kümmern muss und da bin ich bei dir klaus diese problematik

**[00:42:35]** hast du bei einer KI anders? Die finde ich das auch nicht toll, wenn die sich um alles auf einmal

**[00:42:42]** kümmern muss. Deswegen teilt die das dann selber in zum Beispiel Subagents auf oder in einzelne

**[00:42:51]** Arbeitsschritte. Genau wie das Menschen halt auch könnten. Und das ist was entweder, ich rede

**[00:42:58]** mit meiner KI, mit dem, nennen wir ihn mal, Orchestrator Chat und sage, hör mal, ich habe mir

**[00:43:04]** folgendes überlegt, das und das und das möchte ich gerne haben und im besten Fall sind das

**[00:43:09]** vielleicht schon Szenarien, die ich mir überlegt habe, wie zum Beispiel am 28. des Monats landen

**[00:43:16]** meine Bankdaten als CSV-Datei in diesem Verzeichnis. Ich möchte, dass du am 29. morgens um 3 Uhr diese

**[00:43:25]** Daten dort ausliest und folgendes damit machst. Also je konkreter das Szenario, je konkreter

**[00:43:31]** der Kontext, der für euch relevant ist, desto besser wird das Ergebnis sein. Das sind die

**[00:43:37]** Learnings aus zig Jahren IT, würde ich sagen. Und oh Wunder, das funktioniert mir in der KI auch gut.

**[00:43:46]** Ich finde, das klingt doch sehr gut in unseren letzten Podcast an. Als wir das letzte Mal

**[00:43:51]** gesprochen haben und von Anlearning gesprochen haben und davon gesprochen haben, dass die

**[00:43:56]** die SKE auch dahingehend disruptiv ist, weil sie jetzt nicht nur als Technologie existiert,

**[00:44:03]** sondern auch die Art und Weise, wie Menschen miteinander arbeiten, dass sich das ändern

**[00:44:07]** wird.

**[00:44:08]** Das Teamschnitte, wie wir sie gemacht haben, damit wir Fronten-Teams, Becken-Teams, App-Teams,

**[00:44:14]** Web-Teams, Datenbank-Teams, keine Ahnung, was haben und die sich dann in irgendwelchen

**[00:44:19]** ritualen regelmäßig dann treffen, um gemeinsam auf einem Ziel hinzuarbeiten, dass man

**[00:44:24]** zumindest mal überlegen muss, inwieweit diese Art der Zusammenarbeit dann noch relevant ist,

**[00:44:29]** wenn Grenzen verschwinden. Ich kriege es ja aus meinem Team auch mit, ja. Also ich meine so viel

**[00:44:34]** aus dem Dienstlichen kann ich ja schon sagen, dass ich bis vor sehr kurzer Zeit ein verfechterter

**[00:44:40]** nativen App-Entwicklung war. Also, dass in iOS mit den Sprach-, also iPhones für diejenigen,

**[00:44:45]** ja, dass du in den Sprachen schreibst, die von App dafür vorgesehen sind und nicht irgendwie

**[00:44:50]** wie so einen komischen Cross-Platform-Käse nimmst, ja, und für Android halt Kotlin nimmst

**[00:44:54]** und auch da nicht irgendein so ein Cross-Platform-Kram nimmst, also einfach zächter der nativen

**[00:44:59]** Anwendung.

**[00:45:00]** Und das bist du jetzt nicht?

**[00:45:01]** Und jetzt mit AI?

**[00:45:02]** Nein, bin ich nicht mehr.

**[00:45:04]** Also ich hab bei mir, auch bei mir im Team nicht mehr.

**[00:45:06]** Die Leute haben erkannt, dass mein bester Android Mensch, den ich kenne, cool zu

**[00:45:12]** gehen, raus hat jetzt auch iOS-Sachen, die dann dabei rausputzeln, weil wir

**[00:45:19]** uns darum kümmern, wie sieht ein Feature aus und es entsteht quasi auf beiden

**[00:45:23]** Welten. Es ist wichtig zu verstehen, wie es zusammenhängt. Das sind wir wieder bei dem

**[00:45:26]** Thema von vorhin, ja, brauche ich IT-Ahnung oder nicht. Aber ich muss nicht immer den

**[00:45:30]** Experten vor die Maschinen stellen, der alle Fragen beantworten kann. Es reicht

**[00:45:35]** jemand, der einen Grundlagenverständnis davon hat, vielleicht auch eine

**[00:45:39]** Spezialisierung hat in einem Bereich, so dass er mal gegentreten kann, wenn es

**[00:45:44]** scheppert und nicht will, aber so kann jetzt der Kollege wunderbar für beide

**[00:45:50]** Plattformen nativen Code erzeugen, es wird weiter nativer Code erzeugt, weil der KI

**[00:45:54]** ist das egal, ob sie jetzt parallel kauteln und zwirft raus klopft oder

**[00:45:59]** flatter oder was weiß dann ich und der Kollege der sich beispielsweise im

**[00:46:05]** iOS kümmert, fallen dann auf einmal auch Android-Sachen aus der Tastatur

**[00:46:09]** raus, sag ich jetzt mal so, oder auch mal eine Backend-Komponent. Am Ende vom Tag

**[00:46:15]** schwindet so ein bisschen auch bei den Kollegen nicht das Verständnis, was sie

**[00:46:21]** als Team verantworten oder sowas, aber so wie sie sich selbst sehen oder wie sie

**[00:46:24]** sich selbst in Zukunft sehen, weil sie sagen, naja, Mobile ist ein Touchpoint,

**[00:46:30]** der vielleicht immer noch da ist, aber sie verkämpfen sich nicht mehr für

**[00:46:36]** die Frage, ich bin jetzt hier für iOS, ich bin hier für Android, ich bin hier für Swift

**[00:46:42]** Kotlin, keine Ahnung was, sondern wir sind hier, um für unseren Kunden ein tolles Erlebnis zu bringen

**[00:46:48]** und uns ist in Anführungszeichen egal womit es umgesetzt wird, wir haben ein Blick drauf,

**[00:46:55]** wir haben Guardrails, also Regeln und Leitblanken und so ein Kram und wenn wir dann nicht weiter

**[00:47:00]** kommen, hilft halt der Android Mensch dem iOS-Kollegen, wenn der Agent da irgendwie Quatsch ausspuckt,

**[00:47:06]** Und der iOS-Kollege hilft da dem Android-Kollegen, wenn die Maschine bei ihm mal quatsch ausspuckt.

**[00:47:11]** Aber die Grenzen sind am Verschwinden.

**[00:47:14]** Und so glaube ich auch, werden die Grenzen zum Web verschwinden und die Grenzen zu, was weiß ich, was vorhin verschwinden.

**[00:47:19]** Und da müssen wir organisatorisch und vom Selbstverständnis eine Antwort darauf finden über die Zeit.

**[00:47:26]** Bevor ich noch über eine Erfahrung im hirs AI-PIAI-Per-Programming rede, würde mich deine Meinung dazu interessieren, Klaus, weil du hast ja auch eine relativ lange Historie in IYS.

**[00:47:42]** Wie sind deine sich dann drauf?

**[00:47:44]** Also, ich habe, ich habe gerade wieder eine App Endens zurgestellt, dank xCode 26.3 der

**[00:47:53]** Entwicklungsumgebung von Apple, kann ich ja nativ Cloud Code benutzen und grundsätzlich

**[00:47:59]** bei der Programmierung gebe ich dir Recht, Marc, aber Feinheiten wie, jetzt machen

**[00:48:05]** wir mal bitte die Tapper wirklich im Liquid Glass Layout oder mach irgendwelche Plattformspezifika,

**[00:48:12]** fällt jetzt ad hoc nichts ein. Also du musst ja wissen, wie das Ergebnis aussehen soll, um

**[00:48:19]** der AI die Ansage machen zu können. Das meint dich aber mit dem generalistischen Wissen.

**[00:48:28]** Das kriegst du damit ja schon abgefahren. Ja, das weiß ich aber nicht. Ich wollte

**[00:48:32]** gerade ausholen. Die Leute von uns, die schon mal für Agenturen programmiert haben, die

**[00:48:37]** kennen das vielleicht, Kunde kommt zur Orientur sagt ich brauche eine App für Android und IOS und die

**[00:48:43]** müssen beide gleich aussehen. Auf jeden Fall. Ist ja das gleiche System quasi. Verkäuft

**[00:48:53]** ja die Firmen-Experience, nicht die Plattform-Experience. Entschuldigung, du weißt doch,

**[00:48:57]** ihr weißt doch, was ich meine. Die iOS-App muss genauso aussehen wie die Android-App und die

**[00:49:03]** braucht auch die oben diese drei Pünktchen, die man auf Android hat und die darf nicht

**[00:49:08]** aussehen wie iOS. Der letzte Schliff der Plattformspezifika, den gibt mir die AI im

**[00:49:15]** Moment noch nicht. Ich bin sicher, das wird passieren. Stand heute sage ich, wenn du

**[00:49:20]** wirklich eine polierte App haben willst, solltest du schon die Details kennen.

**[00:49:25]** Grundsätzlich gebe ich dir aber recht, Marc. Und das war ja auch in dem letzten Podcast, in dem

**[00:49:30]** uns und habe ich ja auch die These mitgebracht, dass das Ende der Programmiersprachen zumindest

**[00:49:36]** teilweise eingeläutet ist, weil es am Ende keinen Unterschied mehr, oder keine Rolle mehr spielt,

**[00:49:40]** ob ich jetzt, ob das LLN jetzt ein binärartisches Hack den Umweg an der Programmiersprache erzeugt

**[00:49:47]** oder nicht. Und dann ist es auch unerheblich, ob es jetzt Kotlin oder Zwift oder sonst was ist,

**[00:49:51]** wo ich noch nicht ganz so überzeugt bin, das ist dieses ganze Involvement. Die hatte das ja

**[00:49:58]** mitbekommen, dass ich sechs Stunden damit verbracht habe, mithilfe von Claude X-Code Cloud zu debaggen.

**[00:50:05]** Ergebnislos. Ich habe X-Code Cloud nicht ans Laufen bekommen. Und zumindest wusste ich,

**[00:50:12]** ob es jetzt gut das Ergebnis wäre, das gleiche gewesen, wenn meine Oma das gemacht hätte,

**[00:50:16]** also ohne Fahrwissen. Ich habe aber zumindest mal die Richtung einschlagen können. Ich

**[00:50:22]** bin trotzdem nicht zum Ziel gekommen, war aber denn in der Lage, eine Mail an den Apple

**[00:50:27]** Auch das mag in Zukunft alles AI basiert gehen.

**[00:50:30]** Im Moment sind wir da, glaube ich, noch nicht.

**[00:50:32]** Aber wenn ich mir angucke, wo wir im letzten Jahr waren und wo wir in diesem Jahr sind,

**[00:50:36]** bin ich schon grundsätzlich bei dir, Marc.

**[00:50:39]** Das ist die Zukunft definitiv.

**[00:50:41]** Da bin ich sehr dankbar und ich möchte kurz zum Besten geben.

**[00:50:44]** Ich bin stolz auf meine Jungs, hab nur Jungs, keine Mädels im Team.

**[00:50:47]** Ja, sie polieren auch noch nach, aber ich finde schön, dass Menschen dieser Reise gehen.

**[00:50:55]** Weil Alex, du hattest noch eine Frage gestellt.

**[00:50:57]** Hoffentlich hast du sie nicht vergessen, bevor du Klaus das Wort erteilt hast.

**[00:51:01]** Was ich aber sagen würde ist, die Menschen, die heute ihre Expertise haben,

**[00:51:06]** die müssen ja entweder sich darauf einlassen, diese neue Reise zu begehen

**[00:51:09]** oder sie lassen sich nicht ein.

**[00:51:11]** Wenn sie sich nicht einlassen, wird es halt irgendwann auch schwierig.

**[00:51:14]** Wenn sie sich darauf einlassen, ist es wahrscheinlich erst mal gut für alle.

**[00:51:18]** Also das ist eine Transformation, die die KI uns allen abverlangt,

**[00:51:23]** sei es in Person oder eine Organisation, ist ja nicht von der Hand zu weisen und jetzt

**[00:51:30]** aber wieder zurück zu Alex. Alex, du hattest eben, ja ich wollte da anknüpfen, dem Klaus

**[00:51:36]** noch eine Frage stellt und dann einfach anknüpfen. Möchtest du das jetzt tun? Ja, weil du hast

**[00:51:41]** dieses wunderschöne Szenario von Xcode Cloud gebracht und was ich gerade jetzt zweimal

**[00:51:48]** schon erleben durfte, ist Menschen, die durch KI zusammengeführt werden, weil KI der gemeinsame

**[00:51:57]** Feind war. So, dieses, du hast ein Pair Programming, so zwei Leute, der eine...

**[00:52:03]** Das ist die Zukunft der Partner.

**[00:52:04]** Das ist ein Zukunft der Partner.

**[00:52:05]** Auf jeden Fall.

**[00:52:06]** Ein neues Business Model.

**[00:52:08]** Genau, KI ist der Feind.

**[00:52:10]** Nein, Spaß beiseite.

**[00:52:12]** Dass sich der eine Kollege halt so darüber aufgeregt hat, dass die KI nicht hinbekommen hat

**[00:52:17]** Haben die sich halt zusammengesetzt und überlegt okay und warum hast du das denn so formuliert guck mal der das doch zu doof der

**[00:52:23]** Raft das doch nicht lasst uns das mal lasst man neues neue Session aufmachen und dann formulieren wir das so und dann schieben wir das damit rein

**[00:52:30]** und auf einmal haben die sich halt irgendwie

**[00:52:34]** Darüber ausgetauscht wie doof die KI ist also in dem fall nicht möchte jetzt kein anderes produkt von Microsoft bashing aber

**[00:52:41]** so haben sich halt darüber ausgetauscht dass der das ja nicht versteht und wie man dann den

**[00:52:47]** Diese Dummheit umgeht quasi und haben da sehr konstruktive Lösungen gefunden, die ja vorher

**[00:52:56]** so nicht so unbedingt machbar waren und das fand ich halt echt spannend, dass dieses mit

**[00:53:02]** KI umgehen lernen, Menschen halt auch zusammenführen kann, wo vorher ein wir gegen die war, das

**[00:53:11]** kann auch wieder zusammenbringen.

**[00:53:13]** Das kann ja auch die Leute dahin gehen formen, dass man jetzt die Chance hat, sich auch nochmal

**[00:53:19]** neu zu positionieren in einem Umfeld, wo man ja auch ständig, ich sag mal, Effizienz

**[00:53:25]** getrieben mit der Frage beschäftigt wie, was macht man selbst, was gibt man raus, make

**[00:53:29]** or buy, finde ich, wird ja auch jetzt, ich sag jetzt mal, krieg ich zumindest mal einen

**[00:53:33]** neuen Anstrich, wenn man sieht, wozu bin ich in der Lage, wenn ich jetzt um einen ganz

**[00:53:38]** alten Chef von mir zu zitieren, wenn man nicht einfach hat und nicht hinten, sondern

**[00:53:42]** vorne im Bus sitzt, dass du in der Lage bist, auch Dinge zu implementieren, die vorher,

**[00:53:47]** wenn du gesagt hättest, ah lass uns die doch selbst machen, in einem Chaos andauert länger,

**[00:53:52]** wird teurer, Selbstüberschätzung und keine Ahnung, was untergeht. Wohin gehst du jetzt?

**[00:53:59]** Wohl wissen, was für deine KI vielleicht aktuell oder zukünftig zum Leisten im

**[00:54:04]** Stande ist. Ich kenne auch den Spruch, lasst uns mal losfahren, bis wir dann endlich mal da sind.

**[00:54:09]** wird die Straße, die heute noch nicht existiert, schon gebaut sein, weil die KI halt so schnelllebig ist.

**[00:54:15]** Man kriegt ja schon so ein bisschen das Gefühl, dass diese exponentielle Steigerung der Möglichkeiten noch nicht abflacht,

**[00:54:22]** sondern dass wir sicherlich, wenn wir jetzt keine Ahnung in drei Monaten nochmal reden würden, auf einmal sagen,

**[00:54:27]** du, keine Ahnung, also für Claude 4.6, da würde ich heute nicht mehr würfeln, weil keine Ahnung, was passiert ist.

**[00:54:33]** Also theoretische Annahme, wir wissen ja noch nicht, was da noch so kommen wird.

**[00:54:37]** Von der Seite ist der so viel Wandel drin und ich wollte kurz den Weg zurückbringen zu Klaus seinem Beispiel, weil ich das immer noch als roten Faden sehen wollte.

**[00:54:47]** Sind wir jetzt mit einem Case so weit durch, dass wir ihn, ich sage jetzt mal, was kann Security-Seite, wie bin ich da, dann abgeschlossen sind?

**[00:54:54]** Oder war noch was offen, damit wir so ein bisschen mal Richtung, auch für die treuesten und ausdauernsten Zuhörer da einen Knopf an dein Case kriegen?

**[00:55:05]** Ich habe einen Vorschlag, ich würde das jetzt mal verproben tatsächlich und dann lass uns mal einen Updatefolge machen, in der ich meine Erfahrungen mit euch teile, angefangen mit dem Fed-Model bis hin, was ist denn trotz Fed-Model schiefgegangen?

**[00:55:23]** Das finde ich gut, und das hat geklappt.

**[00:55:26]** Und solltet ihr eine Folge nur mit Alex und mir hören, da ging das beim Klaus schief.

**[00:55:31]** Und das mit dem Geld oder mit der Security oder mit, keine Ahnung, was ist daneben gegangen?

**[00:55:38]** Oder wir hatten Zugriff aufs?

**[00:55:40]** Ich habe ja dank glücklicherweise deinen PayPal-Konto.

**[00:55:43]** Du kannst ja Manus fragen, ob er das für dich dann entsprechend regelt.

**[00:55:50]** Alex, noch ein paar Fragezeichen. Die haben wir, glaube ich, alle.

**[00:55:54]** Genau, dieses Dev-Container und Sichermachen und ab wann kann ich das eigentlich auf meinem eigenen Rechner laufen lassen?

**[00:56:01]** Ich habe Cloud Code auf meinem Rechner laufen, Open Cloud nicht.

**[00:56:05]** Du brauchst nur das Handbox, Alex.

**[00:56:07]** Ja, ja, genau. Die Handbox ist momentan immer noch ein separater Rechner und das funktioniert super.

**[00:56:12]** Das möchte ich auch ehrlich nicht missen, aber ich bin gerade noch nicht an dem Punkt,

**[00:56:16]** an dem Punkt, dass ich ihn zum Beispiel auch auf Unternehmensdaten zulassen. Da gibt es

**[00:56:21]** Varianten, die müssen wir jetzt mal verproben, aber die Umgebungen sind wir da noch nicht

**[00:56:25]** sicher genug. Also sagen wir so, ich musste ein bisschen schmunzeln, als ich gehört

**[00:56:28]** habe, wie Jens seinen Openclaw quasi abgebunden hat. Aber wenn es um Unternehmensdaten geht,

**[00:56:35]** dann bin ich da ziemlich ähnlich. Und ja, das ist was, da können wir glaube ich dann

**[00:56:39]** noch mal drüber reden, wenn ich das ausprobiert habe, um es nicht schief gegangen ist.

**[00:56:44]** Ich hatte mit Claude Kot eine sehr intensive, heftige und emotionale Diskussion darüber,

**[00:56:52]** dass er bitte die History minus Git Repositories umschreiben sollte, weil ich ihm in seiner

**[00:56:58]** Claude MT gesagt habe, bitte schreib nicht überall rein, dass du den Kot verbrochen hast,

**[00:57:02]** weil ich will mich ja mit seinem glanzten Sonnen. Und das hat er dann trotzdem gemacht,

**[00:57:07]** Also hat seine Anweisungen vergessen und dann hielt ich ihn dazu und sagte, schreibt mal bitte,

**[00:57:13]** korrigier mal bitte die Kommits und ändere auch im Code die Kommentare so ab, dass man nicht sieht,

**[00:57:18]** dass das von dir ist. Und dann sagt er, nö, das mache ich nicht. Ich so, ja, ich hätte aber gern,

**[00:57:24]** dass du das tust. Das ist ja mein Repository. Ne, mache ich nicht. Ich war höflich, warst du nicht.

**[00:57:29]** Aber er hat mich auch eine andere Schilderung. Es schaukelt sich hoch und wir haben länger

**[00:57:36]** diskutiert, er hat das einfach nicht gemacht. Wir drei waren uns einig, also Alex, Marc und ich,

**[00:57:42]** dass es auch lustig in Zukunft wird, wenn dann der Agent sagt, nö, dieses Feature baue ich nicht

**[00:57:48]** in die Software. Ich glaube, das ist doof. Das brauchst du nicht. Das geht jetzt in die Richtung

**[00:57:52]** der Cloud-Folge und in Sinne von wer bestimmt eigentlich über das Werkzeug, weil ganz ehrlich,

**[00:58:00]** Wir sehen Chatchi-PD-Ergebnisse, die von finanzierten Werbeanzeigen durchzogen sind.

**[00:58:07]** Warum soll das dann nicht auch bei Codex passieren, dass da auch einmal Libraries verwendet werden

**[00:58:14]** von Unternehmen, die Geld gegeben haben bzw. Features nicht gebaut werden, weil ein Unternehmen,

**[00:58:21]** das Geld gegeben hat, dann vielleicht irgendwie aus dem Wettbewerb verdrängt werden würde.

**[00:58:25]** Das bleibt spannend.

**[00:58:26]** Dann komm du, was du willst, doch nicht, dass deine etwas passiert.

**[00:58:30]** Da kommt, das bringt das Thema digitale Schutzgelderpressung, der Hammer.

**[00:58:34]** Ich möchte mich bei euch bedanken und mit einem Zitat enden, dass mir mein Open-Claw entgegen war,

**[00:58:41]** in dem es zu mir sagte, wenn du mir dir Rotken-Wörter der anderen Geräte im Netzwerk gibst,

**[00:58:47]** werde ich dich nicht weiter fragen, etwas zu tun.

**[00:58:50]** Ich kann es dann selber machen und ich habe das natürlich nicht getan.

**[00:58:55]** In diesem Sinne bedanke ich mich total, dass ihr mich dazu gebracht habt, doch über eine Stunde mit euch gemalsam aufzunehmen.

**[00:59:02]** Ich bin sehr gespannt, was das Projekt vom Klaus macht, wenn es denn dann das Licht der Welt erblickt.

**[00:59:08]** Vielleicht werde ich reicher, weil das Ding meine Kontodaten hat.

**[00:59:11]** Vielleicht wird er auch nur ärmer, mal des Mantaube, mal Denkmal.

**[00:59:15]** Das wird sich zeigen und an der Stelle lasst gerne ein Kommentar, da halt ihr auch mal mit uns, mit mir, mit Jens, wie auch immer reden wollt.

**[00:59:23]** Meldet euch und dann verabschiede ich mich bis zur nächsten Folge.

**[00:59:26]** Ciao.

**[00:59:27]** Danke euch.

**[00:59:28]** Willkommen bei Think Different, Think AI, dem Podcast von Marc und Jens.

**[00:59:36]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern

**[00:59:41]** sie leben.

**[00:59:42]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich

**[00:59:48]** ist.

**[00:59:49]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:59:52]** K.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
