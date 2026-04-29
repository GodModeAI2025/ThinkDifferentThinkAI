---
title: "Das strategische Gold"
episode_index: 36
published: "Mon, 20 Apr 2026 14:59:00 +0000"
duration: "3412"
audio_url: "https://audio.podigee-cdn.net/2449676-m-dfce48265ddf95aa1ab0f9c9fe9281b3.mp3?source=feed"
guid: "4bda80e59d1d44547f35ede6131ac0b6"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-04-28T21:10:35+00:00"
---

# Das strategische Gold

**Veröffentlicht:** Mon, 20 Apr 2026 14:59:00 +0000
**Dauer:** 3412
**Audio:** https://audio.podigee-cdn.net/2449676-m-dfce48265ddf95aa1ab0f9c9fe9281b3.mp3?source=feed

## Beschreibung

Skills
In dieser Folge wagen wir einen Deep Dive in die Welt der KI-Skills und diskutieren, warum Skill Engineering gerade dabei ist, die Spielregeln zu verändern. Gemeinsam mit unserem Gast hinterfragen wir, wie sich Teams, Führung und ganze Organisationen entwickeln, wenn Agenten nicht mehr nur auf Prompts reagieren, sondern echte Fähigkeiten einsetzen. Wir teilen unsere Erfahrungen, sprechen offen über Chancen und Risiken und geben Einblicke, wie Skills Arbeit und Zusammenarbeit neu definieren. Natürlich werfen wir auch einen kritischen Blick auf internationale Entwicklungen – von Skill-Datenbanken bis hin zu kulturellen Unterschieden beim Umgang mit KI. Wenn du wissen willst, wie die Arbeitswelt von morgen aussehen könnte und welche Rolle Skills dabei spielen, bist du hier genau richtig.

Notion
https://www.notion.so/de-de

Anthropic
https://www.anthropic.com/

GitHub
https://github.com/

Python
https://www.python.org/

Kaparthy
https://karpathy.ai/

Markdown
https://de.wikipedia.org/wiki/Markdown

Job to Be Done
https://de.wikipedia.org/wiki/Jobs-to-be-done

Agile Methoden
https://de.wikipedia.org/wiki/Agile_Softwareentwicklung

OpenClaw
https://github.com/openclaw/openclaw

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** Hadi zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:34]** So, erinnert ihr euch, wir hatten in unserem noch jungen Podcast vor gar nicht allzu langer

**[00:00:41]** Zeit ein Gast da, den wir wieder eingeladen haben, weil er damals schon sehr interessante

**[00:00:46]** Themen besprochen hat mit uns und wir dachten, warum sollten wir das nicht wieder aufgreifen,

**[00:00:51]** weil so viel hat sich in der TIE-Welt nicht geändert.

**[00:00:55]** Das hört sich komisch an, ne?

**[00:00:56]** alle reden immer von, dass es total schnell abgeht oder irgendwas anderes und ich fange hier diesen Podcast an mit den Worten und so viel hat sich nicht geändert.

**[00:01:02]** Aber tatsächlich entweder waren wir da damals oder vor allem du, Rene, schon so weitblickend.

**[00:01:07]** Wir haben nämlich damals über das Thema Agents geredet und wie die im Prinzip eigentlich mit uns Menschen zusammen interagieren.

**[00:01:15]** Also wie im Prinzip so ein IOC-Modell hat man das damals auch genannt oder du das auch aufgebracht.

**[00:01:20]** Also der Intent von Menschen, die Operations macht die Maschine und der Control hinten macht noch wieder der Mensch im Prinzip.

**[00:01:26]** Wenn wir jetzt heute so ein bisschen auf das Thema gucken, auf das wir heute gucken wollen und das vertiefen wollen,

**[00:01:31]** im Zusammenhang mit so Agents ist das vor allem das Thema Skills.

**[00:01:34]** Und ich glaube, das ist ja auch so dieser wesentliche Teil, um diesen Operations-Part tatsächlich gut machen zu können

**[00:01:39]** und nicht alles irgendwie in einem Rund reinzuhauen, brauchen die Dinger gute Skills.

**[00:01:42]** Und ich freue mich, dass du da bist. Ich freue mich, dass mein Co-host Mark mit dabei ist.

**[00:01:47]** Und das wird wieder eine gute Folge, denke ich mal. Wir haben echt Picklepacker voll mit viele Themen, die wir besprechen können.

**[00:01:52]** Es ist wieder total viel, natürlich passiert in der KI, weil die entsprechend lasst uns losstarren.

**[00:01:58]** Ja, also erst mal auch vielen, vielen herzlichen Dank für die Einladung.

**[00:02:02]** Ja, du, du warst ja auch unser erster Gast in dem Podcast.

**[00:02:06]** August, ne?

**[00:02:07]** Ach Gott, das ist noch gar nicht so lange her.

**[00:02:08]** Und als du eben angefangen hast, Jens, und nach dem Motus, es ist gar nicht so viel passiert, dachte ich,

**[00:02:14]** warte mal ganz kurz, auch wenn die Aussagen, die damals in dem Podcast getroffen wurden, ja durchaus, ich sag mal,

**[00:02:20]** Heute immer noch ganz gut greifen, da schnappen wir uns ja nachher sicherlich alles noch.

**[00:02:25]** Es ist ja schon eine Menge passiert.

**[00:02:28]** Also wir angefangen haben, da habe ich hier für N8N quasi hochgetragende Lobeshymnen gesungen.

**[00:02:35]** Wir haben uns Modelle angeschaut.

**[00:02:37]** Also heute, ich weiß gar nicht, du nutzt die Modelle von damals noch?

**[00:02:40]** Nee, ich glaube nicht, oder?

**[00:02:41]** Nee, du, Mark, wenn du mal überlegst, als wir angefangen haben, haben wir beide von Nautchen beschwernt.

**[00:02:46]** Das war damals, das war urplötzlich ganz neu, wie der in Datenbanken Verbindung gebaut hat und wie er ganz schnell dir Content gebaut hat.

**[00:02:55]** Ist heute eher im Hintergrund, ne? Heute nimmst du Agenten, die machen es sowieso.

**[00:02:59]** Wobei, Notion ist ein schönes Stichwort, mein Cousin, der hatte ich ja auch mal hier als Folge und haben über Notion gesprochen.

**[00:03:05]** Die sind ja mit Anthropic, das ganze Thema Managed Agents, das hatten wir in der Folge, die die Letzens online ging.

**[00:03:12]** Und das ist schon ganz lustig zu sehen, wie Notion da versucht, auch im Wald zu bleiben.

**[00:03:17]** Aber ja, so dieses heiße Eisen, guck mal, was da rausgeht, guck mal, was da geht.

**[00:03:21]** Ich meine, wir haben damals vom Promt Engineers und so weiter gesprochen.

**[00:03:24]** Und heute reden wir und das ist eine sehr schöne Überleitung, glaube ich, über Skills.

**[00:03:30]** Ich finde das total toll, man kennt den Spruch, wer fragt, der führt.

**[00:03:35]** Wer mag uns dann mal erklären, was sind denn Skills?

**[00:03:37]** Ich bin immer so frech und sage, ne, magst du?

**[00:03:39]** Ja, ich folge mal an.

**[00:03:40]** Also völlig, das sind wirklich, für alle Höhe ist es total unvorbereitet, aber wie ich mir das erkläre, gestern war es Promts und Promting ist ja quasi ein

**[00:03:49]** elaborierter Text, der so ein bisschen an das Modell angepasst ist, so ein bisschen das Modell führt, verfalte dich so.

**[00:03:56]** Ein Skill ist das, aber dazu auch Zugriff auf ganz viele Tools und der Zugriff ist, sag mal, orchestriert und geführt und dazu auch Code.

**[00:04:06]** Also, dann, wenn man braucht in den ganzen Skill auch ein Code, um dedizierte klare Anweisungen auszuführen.

**[00:04:13]** Und die Menge aus allem, plus die Möglichkeit, persistente Speichereinheiten auch noch mit dazu zu nehmen, das ist ein Skill.

**[00:04:21]** Und deswegen prompt Engineering ist gestern und Skill Engineering ist morgen.

**[00:04:26]** Und unsere, unsere drei Probezeichen wird sein, dass bald die Welt voller Skill Engineers sein wird.

**[00:04:33]** mit ein Flavor in Eikauf oder Flavor in Kontrollen oder Flavor in Logistik und so weiter, ne?

**[00:04:39]** Ne, ich hätte gerne noch ein bisschen Flavor-Logistik dazu, lecker.

**[00:04:43]** Lecker.

**[00:04:44]** Also, ich finde ja auch tatsächlich, das war ja auch ein bisschen ironisch, hat der

**[00:04:47]** Motto, Promethe-Engineering ist tot, ist ja gar nicht, ne?

**[00:04:49]** Du findest im Grunde die ganzen Regeln wieder, du packst die halt heute in große Text-Dateien,

**[00:04:54]** Skills haben ja dann diese besagten Markdown-Dateien, wo du deine, ich sag es mal, Arbeitsanweisungen

**[00:04:59]** reinschreibst und ob es jetzt der Agent ausführt oder der Mensch für beide könnt

**[00:05:05]** nutzen. Und wie du schon sagtest, das Thema, ich kann Programmcode auch da drin

**[00:05:10]** ablegen und zum Ausführen bringen und so Determinismus ins System bringen, ist halt

**[00:05:15]** schon cool, weil du kannst das in diesen Skill-Dateien ja sogar mischen. Ich habe

**[00:05:19]** letztens auch wieder ein Skill gesehen, da schreibst du dein Prompt und auf einmal

**[00:05:21]** kommt ein bisschen Python-Code, mitten dem Prompt und dann geht es einfach weiter und du

**[00:05:25]** Du stehst dann davor und denkst verdammter Axt, wie cool ist das denn, ne?

**[00:05:29]** Wie cool ist das denn?

**[00:05:31]** Und alles kann auch automatisch generiert werden.

**[00:05:33]** Das ist eigentlich das Verrückte.

**[00:05:36]** Schon bei den Promts, weißt du schon.

**[00:05:38]** Du willst ein Promt und du bittest die KI ein Promt zu machen, damit die KI besser ist.

**[00:05:43]** Das ist ja schon fast die Singularität, die ihr um Maske mal so gerne sagt.

**[00:05:47]** Dass sie KI, KI macht.

**[00:05:49]** Ich bin nicht so weit zu sagen, dass wir da sind, soweit sind wir nicht.

**[00:05:52]** Es hat so Geschmäckle in dieser Richtung schon ein bisschen, oder?

**[00:05:55]** Ja, der Spanne bei den Skills, das, was ich finde, ist, es macht so, und markt dort das

**[00:06:02]** auch gerade.

**[00:06:03]** Wir haben damals über Modelle geredet und jetzt die Skills manifestieren eigentlich

**[00:06:07]** dieses Abnehmen dieser Diskussion, weil natürlich Skills das Schöne mitbringen, dass sie mal

**[00:06:12]** modellagnostisch sind.

**[00:06:13]** Aber ich kann einfach die Skills irgendwo erstellen, in einem relativ einfachen Format

**[00:06:17]** abspeichern und kann sie danach jedem Modell zur Verfügung stellen.

**[00:06:20]** Und das ist, glaube ich, auch eines dieser wahnsinnigen Vorteile, dass man nicht mehr so single-layer

**[00:06:25]** auf das Thema guckt, wow, was kann denn so ein Modell komplett machen, sondern das war

**[00:06:30]** jetzt schon so ein bisschen wieder hingehen und sagen, welche Pakete, welche Fähigkeiten

**[00:06:34]** kann ich denn irgendwie kapseln, ohne dass das echter Programmcode ist, sondern eher

**[00:06:38]** eine Beschreibung, was denn eigentlich da passieren muss, in welchem Verhalten sie sich zeigen

**[00:06:42]** soll und dass ich das dann, je nachdem welchem Modell dann die beste Wahl ist, dann

**[00:06:47]** auch diesen Modell zur Verfügung stellen kann.

**[00:06:49]** Das haben natürlich ein paar andere Vorteile, weil wir sind jetzt nicht mehr so gebunden.

**[00:06:52]** Wir arbeiten nicht auf der Ecke des Modells, sondern wir denken eher auch in Richtung, wie

**[00:07:00]** kann ich denn diese Skills alle orchestrieren, welche Skills brauche ich denn dann, sind Skills

**[00:07:05]** von gestern, eigentlich noch die Skills von morgen, die ich noch haben möchte.

**[00:07:08]** Also, das interessiert mich das Skill von gestern.

**[00:07:10]** Von vor einer Stunde, wenn man das sagt.

**[00:07:14]** Ja, genau.

**[00:07:15]** Du, ich hab deine Analogie. Erinnert euch noch früher an die Digitalkameras und damals gab's am Anfang das sogenannte Pixel-Rennen.

**[00:07:22]** Meine Kamera war kein 2-Pixel, Megapixel, deine kann 3, die eine kann 10.

**[00:07:27]** Und irgendwann mal war klar, mehr Pixel passen gar nicht auf den Ship, dann ging's um eine andere Qualität.

**[00:07:33]** Ich mein, wir sind auf dem noch, also es wird noch bessere Modelle geben, so dass wenn Weltmodelle kommen, es gibt ja noch mal, aber das wird so, wir werden auch eine Saturierung,

**[00:07:41]** dass wir es gesättigt werden und dann ist genau das, jenes, was du gesagt hast, das System.

**[00:07:47]** Also wie nutze ich denn das in sich? Wie schaffe ich Wirkung?

**[00:07:50]** Bedeutend wichtiger werden und wann? Die Geschwindigkeit ist wahrscheinlich schon recht bald, dass wir also in der Saturigen sind.

**[00:07:58]** Also was ich ja bei den ganzen Skill-Thematiken, ich gebe zu, dieser Gedanke ist bei mir tatsächlich auch noch sehr neu.

**[00:08:03]** Ihr dürft gerne mich jetzt auslachen, falls ich damit weit hinten anhäng.

**[00:08:07]** Ich stand letztens vor der Frage, ok, gut, in Skills kannst du Programmcode ausführen, fairer Punkt, verstanden.

**[00:08:13]** Eigentlich ist ja dann sowas wie in Skill und eine Kaida darunter ein Betriebssystem, auf dem Software deploit werden kann.

**[00:08:21]** Ich habe mir letztens ein kleines Skill gebaut, den gibt es in Gitrepo.

**[00:08:25]** Der fräst sich da durch, was da drinnen ist, wirft Kotlin, PHP, keine Ahnung, was.

**[00:08:31]** Dem sagst du, mach mir mal daraus ein Skill und dann überlegt das Ding sinngemäß,

**[00:08:35]** welche Orchestratoren brauche ich, also wie teile ich mir die Aufgaben, die dieses Programm,

**[00:08:39]** das ich im Git gefunden habe, wie teile ich das auf? Und das, was er quasi nicht in Skill

**[00:08:44]** überführt kriegt, das lässt er wirklich dann als Software in Python in deinem Skill laufen.

**[00:08:51]** Und dann dachte ich mir auch so, alter Falter, ja? Also dieses Thema, wie bauen wir Software

**[00:08:57]** ändert sich? Wie lässt du Sachen laufen, ändert sich? Und wie integrierst du, ich sage jetzt

**[00:09:03]** Entschuldigung, so ein altes, eingemottetes Githa-Projekt, das auf einmal einen neuen Clans erfährt, weil du sagst, komm, migrier mir das mal auf ein Skill und auf einmal lebt das Ding dann nicht mehr, was weiß ich, hier Kobol, sonst was, gut, Kobol werde ich in Gith wahrscheinlich wenig finden, aber dann auf einmal in so einer Runtime, in Codex, in Opus, in, in, keine Ahnung, was.

**[00:09:22]** Das fand ich schon wieder immer so, hä, ich weiß es grundsätzlich, aber das fand ich so amazing, damit auf einmal so, was für Möglichkeiten.

**[00:09:30]** Du, ich habe neulich, ich verfolge auch ganz viele Newschammers und so weiter und eine

**[00:09:35]** hat, die ist leider nicht auswärtig im Kopf, das war ein ganz frisches, ich glaube, Z51

**[00:09:40]** oder so heißt es.

**[00:09:41]** Also der Name ist nicht ganz korrekt, der irgendwo so in der Nähe, ein Open Source

**[00:09:44]** oder auch ein Weight Model, das gerade jetzt draußen ist, die haben das Ding laufen lassen

**[00:09:49]** und acht Stunden autonom laufen lassen, um ein Linux-Lagiat, also einfach komplett

**[00:09:55]** komplett mit über 50 Apps komplett lauffähig. Sogar eine eigene WhatsApp oder Telegram Messenger-Komponente mit

**[00:10:03]** Mail und allem komplett lauffähig. Und jetzt überleg dir mal, du machst diese Horde von

**[00:10:08]** Agenten, die Software kreieren, über alle GitHub-Repos laufen lassen. Das war überlegen,

**[00:10:13]** was dann rauskommt da, ne? Also wenn du sagst, okay, nimm die besten und bau dafür eine Menge

**[00:10:18]** von Apps, die dieses und jedes können. Ja, ja, das ist wild und das fühlt so ein bisschen auch,

**[00:10:23]** Ich hatte zwei Sachen von Kaperfee. Kaperfee hat die letzte Woche dieses Wikithema nochmal

**[00:10:29]** rausgebracht, wie im Prinzip wissenschaftleriert werden kann. Deshalb sind ja auch viele von

**[00:10:33]** unseren Posts voll um dieses Thema herum. Das ist ein weiteres Thema. Das gilt einmal

**[00:10:39]** das Thema und im Hintergrund nochmal, dass wissenschaftleriert irgendwo haben,

**[00:10:42]** das man benutzen möchte. Also auch ausgelagert von dem Modell, sodass es auch agnostisch

**[00:10:45]** benutzen kann. Und abseits von dieser ganzen Flasche schon irgendwie zu komplizierten

**[00:10:50]** Rackstrukturen, sowas, die man sich zwischendurch überlegt hat. Aber was ist der andere Kurs von

**[00:10:54]** ihm, der fand ich noch spannender und das passt zu dem, was ihr beide gerade sagt. Weil die

**[00:10:57]** Fähigkeiten so hoch sind, geht er ja auch davon aus, dass man eigentlich gar nicht mehr jetzt in

**[00:11:03]** Github ein Cub-Basis forkt, sondern dass es eigentlich nur noch wichtig ist, den Ideen-Markdown-Pfeil

**[00:11:10]** quasi zu forken. Weißt du, dass wir in so eine Welt reinkommen, wo es viel brillanter

**[00:11:15]** wird und viel sinnvoller ist, dass wir uns quasi auch token optimiert, nur die Idee tauschen und gar nicht irgendwie den ganzen

**[00:11:22]** Legacy-Code tauschen, wenn du so möchtest, und dann sagen, das war die eigentliche Idee, das ist der eigentliche Output, den ich geregeln will.

**[00:11:28]** Also wenn wir jetzt mal, ich habe heute Morgen über Nacht gedacht, so aus so einer, aus so einer Designer-Job-to-be-dannen-Perspektive

**[00:11:34]** draufgucken, da hast du früher immer gesagt, wenn jemand ein Loch bohren will an die Wand, ja, dann braucht er ein Bohrer.

**[00:11:39]** Und das ist eigentlich so der Job, den ich als Baumarkt, uns als Brosch oder als andere Hersteller von Bohrmaschinen da irgendwie machen möchte.

**[00:11:45]** Jetzt heutzutage, wenn man sich das aus so einer Perspektive noch mal anguckt, wenn ich sage, der Job-Tubi dann, das ist das eigentliche, was gemacht werden zu können.

**[00:11:53]** Und ich kann das eigentlich, ohne dass ich noch irgendwie ein vorgefertigtes ist.

**[00:11:57]** Ich fadte sie auch ja auch mal vorne, aber ohne dass ich irgendein vorgefertigtes Stück Software an irgendeiner Stelle des Ökosystems, also bei mir, bei dem Partner, bei dem Reseller, wo auch immer,

**[00:12:09]** Kann ich eigentlich darauf verzichten, sondern ich muss eigentlich nur noch im Konzept der Maschine sagen, das ist das Job, den ich machen möchte.

**[00:12:15]** Mach den Rest.

**[00:12:17]** Mach den Rest. Oder macht mir mal einen Vorschlag, ne?

**[00:12:19]** Also es ist, und ich glaube auch, der Türöffner ist das Thema, das er auch für den Podcast hier gewählt hat, sind die Skills.

**[00:12:26]** Ich glaube, also wenn mal guckst du, so früher gab es, also das Internet da waren die Web-Apps, so das Große, dass man da so jetzt

**[00:12:33]** Ob sich apps verfügbar machte dann war das iphone platform und also apps auch zu verfügen stellen bei anderen.

**[00:12:39]** Dann kann natürlich sprachmodelle jetzt überspringen paar sachen aber so eine idee sprachmodelle und die gehen jetzt mit skills in so eine ähnliche ich sage nicht apps aber es sondern auch so eine epifizierung.

**[00:12:49]** Der generell AI welt so so was passiert das genau das was beschreibt jetzt.

**[00:12:55]** Ist das ist das ist das wieder was wir vielleicht als menschen brauchen dass wir es uns wieder einfacher machen.

**[00:13:00]** Vielleicht gar nicht so akzeptieren wollen dass es wollen dass es ein modell gibt dass er alles könnte.

**[00:13:04]** Also, weil auf der anderen Seite sagen wir mal wenn wir jetzt in die zukunft reingehen und die modelle immer größer werden und immer besser werden.

**[00:13:10]** Du hast gerade das Thema weltmodelle angesprochen und ich glaube irgendwie selbst wenn wir jetzt irgendwie so ein normales modell nehmen würde und vergleichen würde.

**[00:13:17]** Unser Gehirn mal in so ein versuchen würde in so ein modell rein zu zwingen dann werden wir glaube ich irgendwie dann werden wir immer noch 100 Trillionen Parameter neben wir haben können.

**[00:13:24]** Und ich glaube da sind die die besten modelle der welt noch meilenweit von entfernt.

**[00:13:28]** Da ist die Natur immer noch deutlich überlegen, über dem, was wir da bis jetzt gebaut haben.

**[00:13:32]** Aber nichtsdestotrotz ist es ja schon so, dass wir in so eine Zukunft reingehen und die

**[00:13:37]** Modelle immer das besser können und dann fragt man sich ja schon, brauche ich dann so eine

**[00:13:40]** Skill Beschreibung?

**[00:13:41]** Weil eigentlich können diese Modelle ja alles, gilt es eh schon.

**[00:13:44]** Und da habe ich jetzt einen Punkt, wenn ich mal ran gebe.

**[00:13:46]** Weil ihr wisst ja vielleicht, ich liebe es ja hier und da haben wir auch Mühlscher

**[00:13:49]** zu schreiben.

**[00:13:50]** Ich habe ein kleines Mühlschlein.

**[00:13:51]** Das ist gerade dabei in dem Thema Leadership und Agent DKI, weil es gibt ein Paradox

**[00:13:56]** Weil ich bin zu tief dafür überzeugt und ich glaube, ich habe auch stichhaltige Beweise, dass die Jobs sich nur ändern werden.

**[00:14:02]** Wir werden ganz viel, weil Menschen, die mir sowieso zu arbeiten, also wir werden viel, aber wir werden anders arbeiten.

**[00:14:07]** Und was ist das jetzt? Es gibt so ein Paradoxum, das sagt, je mehr du in Geschäftsprozessen automatisierst,

**[00:14:14]** desto mehr Führung brauchst du, desto mehr Leadership.

**[00:14:17]** Das ist das, was Sie auch beim letzten Mal gesprochen haben. Sie haben das selber Intent, Operate und Check.

**[00:14:21]** Diese Intenzsache, dieses strategische Führen wird immer wichtiger sein, weil der Skill überladene Agenten-Korpus muss ja irgendwo die Wirkung und das Ergebnis erzählen.

**[00:14:34]** Damit du damit arbeiten kannst, musst du dich immer selber fragen, wie führe ich diese Menge von Agenten, damit etwas rauskommt.

**[00:14:42]** Und diese Feedback-Schleife wird immer schneller und kürzer.

**[00:14:47]** Das heißt, die Menschen, die heute in den Prozess darauf, dadurch, dass sie auf die Tabelle was eintragen, auf die Monitor, an der Stelle was klicken,

**[00:14:55]** am Ende dann den Output des Prozesses dominieren, werden die es an der Seite stehen und beobacht, was rauskommt und dann ganz schnell eingreifen,

**[00:15:02]** oh, lieber Agent, ich muss dir eine andere Strategie geben, damit das rauskommt, was ich will.

**[00:15:06]** Das heißt, mehr Führung und weniger operatives Arbeiten, mehr Liederschere.

**[00:15:10]** Das heißt, und das ist für mich eine ganz frohe Botschaft, weil du hast auch die Menschen angesprochen.

**[00:15:15]** Sie müssen nicht die skills beherrschen, aber sie müssen viel mehr in Sinne von leadership in Sinne von wie kann ich einen Corpus an Software Agenten so steuern, dass was rauskommt.

**[00:15:27]** Ja, was mich wieder zu einem Thema bringt, was ich auch damals schon gesagt hatte, mit dem und dafür brauchen wir natürlich noch mehr diese Vertrauensebene.

**[00:15:36]** Also dann wiedergespiegelt in irgendwelche Art User Interface ist, dass wir nachvollziehen können, was da passiert.

**[00:15:42]** weil wenn ich jetzt eine Agentin miteinander reden lasse, wenn ich als Mensch irgendwo eingreifen muss

**[00:15:48]** und das immer komplex wird, also die Aufgaben ja vielfältiger werden, weil viel mehr Aufgaben in

**[00:15:53]** noch kürzerer Zeit erledigt werden, brauche ich natürlich tatsächlich, also deshalb bin ich immer

**[00:15:57]** noch der Meinung, dass wird eine wahnsinnige Herausforderung, das sowohl für die Agenten

**[00:16:01]** unter sich zu bauen als auch für uns Menschen involut oder enveloped, einen Interface zu

**[00:16:06]** bauen, das uns wirklich das Vertrauen gibt, da passiert auch das Richtige, in der Delegation,

**[00:16:10]** die ich gemacht habe?

**[00:16:12]** Ich finde auch das Thema Delegation.

**[00:16:14]** Das kann man sagen, gut, als Führungskraft ist man es gewohnt, zu delegieren.

**[00:16:18]** Wenn du jetzt, dann würde ich nicht sagen, wir haben alles besser im Griff,

**[00:16:21]** als vielleicht dein Mitarbeitende selbst,

**[00:16:23]** aber die Fähigkeit zu haben, auch mal Dinge abzugeben,

**[00:16:27]** zu akzeptieren, dass die Maschine mich jetzt nicht ersetzt,

**[00:16:32]** aber dass eine Maschine etwas kann,

**[00:16:34]** bis zu einem gewissen Qualitätsgrad.

**[00:16:36]** Und ich dann später draufschaue,

**[00:16:38]** Was freigebe vielleicht noch irgendwie was nachfahre und dann geht es weiter und mich nicht zurückziehe nach dem Motto.

**[00:16:44]** Ach guck mal, das, was die KI da gebaut hat, das ist ja Quatsch, habe ich ja gleich gewusst.

**[00:16:48]** Ich hatte letztens einen Fall, da hat ein Kollege sich etwas angeschaut, ein Skill hat ein bisschen was gebaut,

**[00:16:52]** der hat irgendwie Wochenarbeit in Stunden erledigt und danach war das Feedback,

**[00:16:56]** ach guck mal, das sind das und das ist immer noch falsch.

**[00:16:59]** Wo ich dann meinte, ja guck mal, du hast es gelesen, du hast es korrigiert,

**[00:17:03]** warst nach zwei, drei Stunden selbst auch nochmal fertig.

**[00:17:06]** Das heißt, wenn ich deine zwei, drei Stunden nehme, die zwei, drei Stunden vom Skill nehme,

**[00:17:10]** dann bist du irgendwie bei sechs, sieben Stunden am Stück gegen eine ganze Woche oder zwei

**[00:17:15]** Wochen.

**[00:17:16]** Das ist doch ein gutes Mittel und sei doch auch froh, dass die KI, dass du nicht nur,

**[00:17:22]** ich sag mal, ich bin jetzt der, der einfach nur abhakt, der wie der Fluglose am Radar

**[00:17:26]** sitzt und wartet, ob irgendwas laut piep, weil irgendwelche Flugzeuge eventuell sonst

**[00:17:31]** auf Kollisionskursen sind oder ähnliches, die er dann einfach nur aufgrund des Aufpassens

**[00:17:35]** und dieses ständigen, man denkt schon, Habachtstellung quasi auch regelmäßig Pausen machen müssen,

**[00:17:40]** weil sie sonst auch ihre Konzentration verlieren. Ich habe irgendwo auch mal gehört, so etwas

**[00:17:45]** wie autonomes Fahren ist es sicherer, das Lenkrad aus dem autonomen Auto rauszuholen,

**[00:17:51]** als darauf zu vertrauen, dass der Mensch eingreift, wenn das autonomfahrende Auto

**[00:17:57]** einen Fehler macht, weil man schlicht und ergreifen sich in die Abwesenheit, dass

**[00:18:02]** man einfach weg trifftet und das andere, was du gesagt hast vorhin mit, dann hast du nachher

**[00:18:07]** vielleicht keine Ahnung, 3, 4, 5 Agents, das ist halt die andere Seite der Medaille, dass du

**[00:18:11]** vielleicht Dinge abgebst, der Maschine, das in die Hand drückst und dann irgendwann völlig

**[00:18:16]** verlierst, je nachdem welches Interface wir den Menschen bieten, je nachdem wie wir damit umgehen,

**[00:18:21]** dass du nachher sagst, okay, ich habe jetzt hier keine Ahnung, zählen Fenster offen,

**[00:18:25]** ob es jetzt Klo oder Opus, was auch immer da herum schlumpft und dann stehst du nachher da, wo

**[00:18:30]** wo war ich denn mit was? Und ich muss den rechten mal kurz verlassen, du kommst nach einer Stunde wieder, was ist denn da jetzt, was ist denn hier Stand der Dinge?

**[00:18:37]** Auch das ruft ja auch nach einer neuen Art von Interface. Wie gehe ich damit um? Wie managere ich Zeit? Wir haben echt noch ein paar spannende Fragen vor uns.

**[00:18:48]** Und auch die Skillifizierung wird auch die Interface ist, das GUI auch echt wieder mal verändern, völlig klar.

**[00:18:56]** Ja, also das ist etwas, also da bin ich tatsächlich auch mal gespannt, wie gesagt, wie das läuft und allein auch diese Erkenntnis, von der ich eben sprach bei den Menschen, du gibst ihm was in die Hand, sie sagen, komm mal hier, Kai, ne? Und dann, naja, nee, hast du verabverstanden? Ich kriege etwas von ihr zurückgeliefert, ich arbeite nochmal nach und dann legts halt auf, wieder an uns zu fragen, okay, kriegen wir da vielleicht noch ein bisschen was raus, weil wir den Skill nochmal anpassen, ja? Was interessiert mich, der Skill von vor einer Stunde, wurde eben gesagt, ich habe ja auch so ein Ding nach dem Motto,

**[00:19:26]** Versucht durch synthetische Testfälle herauszukriegen, wie du den Skill verbessern kannst in der Nacht und hoffst, dass am nächsten Tag noch ein Tick besser funktioniert.

**[00:19:34]** Das ist ein echt so breites Feld, das, ja, da müssen wir erstmal gucken, wie man sich da aufstellt und ja, wie sich das Ganze entwickelt und die guten Modelle mit der Grunde kommt von alleine.

**[00:19:48]** Bestimmt und bezüglich aufstellen. Das ist ja im Prinzip so ein bisschen interessant,

**[00:19:53]** jetzt mal, wenn ich das von den persönlichen Erfahrungen, die wir so haben und die, die

**[00:19:58]** Leute auch draußen, glaube ich, haben, auf so einer Organisations-Ebenhebe. Also ich glaube,

**[00:20:01]** der Ex-Twitter-Gründner, der Jack Dorsey, heißt er, glaube ich, der hat jetzt auch

**[00:20:09]** irgendwie vor ein, zwei Wochen Artikel veröffentlicht, wo es darum ging, dass er sagte, wir brauchen

**[00:20:14]** eigentlich noch viel, viel flacher Reachien in der Zukunft. Und fangt nicht an, quasi eure

**[00:20:20]** jetzigen Orkshards quasi in agentische Strukturen zu übersetzen. Das ist genau so ein Ding. Also,

**[00:20:28]** ich glaube, das ist ein guter Impuls, man muss sich ihm alles fortnehmen, weil ich glaube,

**[00:20:33]** da steckt was drin, was man aufgreifen muss, wenn man sich jetzt in das Thema kümmert und sagt,

**[00:20:38]** ja gut, wie könnte denn jetzt meine Organisation in Zukunft, Enhanced with Skills, die ich

**[00:20:43]** irgendwo verweilt, denn eigentlich kann er aussehen, was passiert da, was wird anders

**[00:20:46]** werden und ich glaube das ist eine spannende Fragestellung. Also da, also dieser alte

**[00:20:51]** Pyramide ist tot. Du musst mal ein Papitel in mein Buch. Also tatsächlich die alten

**[00:20:58]** Information Broker, also Führungsschichten, die sich dadurch definieren, dass sie wie

**[00:21:03]** ein Driftträger in der Nachricht weitertragen und wissen, dass A und B

**[00:21:06]** zusammen am Meeting sein müssen, damit etwas hier rauskommt. Die braucht man noch,

**[00:21:11]** Also es heißt nicht, dass Sie schlechten Job machen, weil wir sind um eine Komplexität,

**[00:21:16]** Musikkomplexität, managen, aber das wird zusehends weniger wichtig werden und es wird

**[00:21:21]** viel wichtiger werden, inhaltlich zu führen.

**[00:21:22]** Dadurch werden Hierarchien natürlich flacher.

**[00:21:25]** Mein Steak ist sowieso immer, Hierarchien sind eigentlich immer Kompromiss.

**[00:21:31]** Eigentlich möchte ich überhaupt keine Hierarchien haben, eigentlich muss alles

**[00:21:34]** flach sein, nur dann habe ich Anarchie.

**[00:21:35]** Also muss ich irgendwie versuchen eine große Menge Menschen, effizient in einer Organisation, so zu führen, dass der maximale produktive Output entsteht.

**[00:21:45]** Also muss ich solche Verästelung Teams machen. Und sobald ihr zwei Teams macht, habt ihr zwei Teams, die sich eine Mauer bilden und die Brücke bauen.

**[00:21:55]** Das ist ganz automatisch und irgendwann, wenn man das so richtig auslebt, wir in unserer Firma machen das glücklicherweise nicht,

**[00:22:01]** Firmen, die habe ich gesehen, die haben das richtig ausgelehnt. Da braucht man ein Visum,

**[00:22:05]** wenn man von der HR in die Marketingerteilung gehen möchte. Also das ist da so richtig weit entfernt.

**[00:22:12]** Und diese pyramidische Aufstellung ist tatsächlich in einer Welt, wo wir Arbeit

**[00:22:19]** verteilen können in agentisches und in, sagen wir, strategisches Arbeiten, weniger wichtig.

**[00:22:25]** Viel weniger wichtig und man kann auch viel hierarchiefreier arbeiten. Und wir kennen das.

**[00:22:30]** Hierarchie-Fly ist ja der wesentliche Kern von agilen Methoden. Ich könnte doch erinnern früher in

**[00:22:35]** anderen Firmen, als ich das erst mal versucht habe, Management Agile beizubringen. Da haben

**[00:22:39]** Leute gesagt, agil, das ist ja flott, dann macht man es schneller. Ja, nee, das ist nicht der

**[00:22:46]** Gedanke, sondern der Gedanke ist tatsächlich halt hierarchiefrei zu arbeiten. Egal, wer da

**[00:22:52]** welchen Berang auf deiner Schulter hat, die Leute, die Ahnung haben, stehen um ein Problem

**[00:22:57]** herum und lösen ein Problem, um für die Usergruppen, die Kunden, die das Problem haben, die beste

**[00:23:04]** Lösung zu generieren. Hierarchiefrei. Ja, hierarchiefrei und Herrschaftswissen frei. Ich kannte

**[00:23:10]** den Begriff Herrschaftswissen auch noch. Der wurde dann manchmal auch ausgeprägt, dass

**[00:23:13]** gewisse, eben gewisse Sachen eben wissen. Na, also klar, gibt es auch immer noch irgendwelche

**[00:23:17]** Themen, die ebenfalls eine Relevanz haben, dass nicht alle Leute das immer so fortwissen,

**[00:23:20]** aber ich glaube in so einer Organisation der Zukunft ist es eigentlich nicht tragbar,

**[00:23:26]** wenn nicht alles Wissen instan zur Verfügung steht und vor allem, wenn eigentlich auch Wissen

**[00:23:31]** nicht nur das abgespeicherte Datenformat oder die Datei ist, sondern es eben auch die Skills sind,

**[00:23:38]** die benötigt werden, um gewisse Themen einfach umzusetzen. Und ich glaube auch da müssen wir

**[00:23:41]** hätten können. Ich glaube, dass die Organisation der Zukunft brauchen, glaube ich, sowohl neben

**[00:23:45]** dem zugreifbaren Wissen in einer von mir aus im Markdown-Format oder in welchem Format auch

**[00:23:50]** immer so, dass die Maschine es gut lesen kann. MCP-Server, die auf gewisse Einheiten

**[00:23:54]** einfach zugreifen können, eben auch meiner Meinung nach so einer Art Skill, Datenbank und Workflow,

**[00:24:00]** der der ganzen Firma zur Verfügung steht. Weil das was du ja gerade beschreibst. Also das,

**[00:24:05]** was das Energien-System ja nötig ist, dass ich im Prinzip alle Fähigkeiten habe,

**[00:24:08]** die Sache noch umzusetzen. Weil sobald ich nicht alle Fähigkeiten habe, um ein gewisses

**[00:24:12]** Thema umzusetzen, scheitert das Energien-System. Weil ich dann wieder auf jemanden anders warten

**[00:24:16]** muss, das er es mir erst umsetzen kann. Und ich glaube, auch da können wir hingehen. Das wir

**[00:24:19]** sagen, wenn wir in Zukunft dann eben den nötigen Skill eben abfragen können, um schon mal den

**[00:24:25]** nächsten Schritt zu gehen, dann heißt ja nicht, dass wir den Schritt ganz alleine geben müssen,

**[00:24:28]** sondern ja, wir brauchen dann auch immer noch die andere Person, die diese Skrillgruppe

**[00:24:31]** pflegen wird, auf die wir zugreifen können. Aber ich werde flexibler werden, einfach,

**[00:24:34]** ich werde deutlich flexibler werden. Ich habe, wir brauchen das als Organisationen oder

**[00:24:37]** Organisationen brauchen das in Zukunft auch so eine Art Skill, Skill, da hatten wir

**[00:24:41]** gerade mal gemacht. Ich erinnere mich noch an eine Folge von einem mit einem,

**[00:24:46]** Mit zwei Menschen eines Küchenmaschinenherstellers,

**[00:24:50]** mit denen wir die Diskussion hatten, Jens, da warst du gerade,

**[00:24:54]** ich glaube beim Fasching, egal, wo wir das Thema auch hatten,

**[00:24:58]** dass sich Organisationen zukünftig sicherlich auch deswegen ändern werden,

**[00:25:02]** weil auch Grenzen verschwinden, die entstanden sind,

**[00:25:05]** weil man früher einfach Menschen ein Thema als Aufgabe gegeben hat.

**[00:25:10]** Und diese Aufgabe, da waren dann, was ich, du hattest 10 Leute, die haben Web gemacht,

**[00:25:13]** 10 Leute, die haben App gemacht, 10 Leute, die haben Backend gemacht, 10 Leute, die haben

**[00:25:17]** Datemann gemacht, 10 Leute, die haben Servicemanagement gemacht.

**[00:25:19]** Und jetzt stehst du da und hast quasi einen Agenten oder hast Tools, die diese Grenzen

**[00:25:24]** verschwinden lassen, weil du bist dann einer Lösung dran und nicht mehr nur noch an einem

**[00:25:29]** ganz kleinen Teilchen.

**[00:25:30]** Du machst dann eine Absturzstrecke alleine, du machst einen Feedback-Formular alleine,

**[00:25:36]** du drückst auf Deploy und die Datenbank lernt ihr Feld, Web und App kriegt

**[00:25:41]** das Zeug und wenn du morgen sagst, ich hätte gerne ein neues Layout, dann hat es halt ein neues

**[00:25:44]** Layout. Sicherlich gibt es da immer noch Menschen, die sagen, okay, pass mal auf, das ist die

**[00:25:49]** Schrift, die zu verwenden ist und das ist die Farbe, die zu verwenden ist und wir haben

**[00:25:52]** vielleicht ein paar Regeln, die wir uns geben wollen, Guardrails, wie wird entwickelt und

**[00:25:56]** was muss man denken, bitte auch an Testing, hat dann keiner die Tests vergessen und

**[00:25:59]** so ein Kram, aber trotzdem werden sich Teamstrukturen ändern, weil ich bin auch der Meinung,

**[00:26:05]** wenn ich es alleine sehe, wozu Menschen in der Lage sind und ich Menschen erlebe,

**[00:26:10]** vom süßen Geschmack des Honigs genascht haben, die vorher sich als, ich sag mal, die, die mir vor

**[00:26:15]** einem nackten Arsch ins Gesicht gesprungen werden, wenn ich den gesagt hätte, deine Expertise ist zwar

**[00:26:21]** wichtig und richtig, aber du verlässt deine eingetretenen Fahde, du öffnest dich neuen Technologien,

**[00:26:26]** du bist mal front and back and ab und hast du nicht gesehen? Die hat mich für verrückt erklärt.

**[00:26:31]** Und jetzt ist das für dich normal. Jetzt kommen die mit einer Freude ins Büro,

**[00:26:34]** weil auf einmal Grenzen verschwinden. Du redest über Lösungen und der sagt bitte noch,

**[00:26:39]** Ich weiß, ihr kommt gerade in so eine Redeschwahl. Wir haben Gäste, ja.

**[00:26:41]** Ich meine, hallo, ich musste auch dem Gast wieder das Wort geben.

**[00:26:43]** Aber da habe ich mich immer dran erinnert an eine Geschichte, die mir meine Lehrerin damals

**[00:26:49]** in der Weiterführenden-Schule gesagt hat.

**[00:26:51]** Die gesagt hat, dass ein Mensch, der an einer Lösung mitwirkt und von Anfang bis Ende,

**[00:26:57]** besser sich mit der Lösung identifiziert, also wenn du am Fließband stehst und immer nur die Schraube festrätst.

**[00:27:02]** Gut, an der Schraube festrätten haben wir heute Roboter, fairer Punkt.

**[00:27:05]** Aber du identifizierst dich damit mehr.

**[00:27:07]** Aber die Leute jetzt hin, die Leute kriegen das Handwerkzeug, das zu tun, womit ein Kunde,

**[00:27:14]** ein anderer Anwender, irgendetwas, was anfangen kann und damit identifizierst du dich und das

**[00:27:20]** ermittelt Freude.

**[00:27:21]** So zumindest ist mein Erlebnis.

**[00:27:22]** Und ich glaube, das ist auch sinnstiftend.

**[00:27:25]** Also gestern haben wir Organisation so beschnitten nach gutem Skills und Fähigkeiten, aber

**[00:27:31]** auf Basis einer terroristischen Prozesswelt.

**[00:27:33]** Ja.

**[00:27:34]** Ein Spezialist für das, dann kommt ein Spezialist für das. Wir machen Übergaben, Handovers und haben IT-Hand-Schnittstelle programmiert.

**[00:27:41]** SAP hat damals etwas Integratives gemacht, aber das wird nur so eins nach dem anderen und so hat sich diese Spezialisierung kreiert.

**[00:27:48]** Jetzt entsteht natürlich, dass Domänenwissen wird, wie sage ich es, es wird etwas weniger wichtig werden.

**[00:27:55]** Es ist natürlich noch wichtig, aber es wird etwas in der Bedeutung verlieren, weil irgendwie, wenn man so bis auf Level 5, wo es da 100 Level gibt,

**[00:28:03]** kann eigentlich jeder jetzt jedes Thema angehen. Jeder, der nicht godengar kann, ist godengar.

**[00:28:08]** Natürlich jetzt nicht riesengroß, oh, wobei, wer weiß, wir haben ein großes Erdmann, aber

**[00:28:13]** jeder kann Stück-Controlling, jeder kann es in Prinzip einkaufen, jeder kann in Prinzip

**[00:28:17]** die ersten Kompetenzfilter für HR-Entwicklungen machen, im Prinzip. Also Domänen wissen wird

**[00:28:22]** weniger wichtig. Das heißt, die Art und Weise, wie wir unsere Team schneiden, müssen

**[00:28:25]** anders beschnitten werden. Aber sie müssen. Das ist nämlich genau das, was du gesagt

**[00:28:29]** du trittst es also voll in schwarze, weil wir werden in Zukunft viel mehr danach schneiden,

**[00:28:34]** dass wir den Leuten das Gefühl geben, ihr seid es. Das ist euer Ding, euer Baby, das

**[00:28:38]** ist eure Motivation, das ist euer Output. Und das ist auch immer mein Credo. All das,

**[00:28:44]** was wir diese wunderbare Technologie sammeln, ist immer noch ein Schraubenzieher. Das ist

**[00:28:48]** ein Tool. Das nutze ich damit am Ende, damit ich irgendwie die Schraube in den Wand

**[00:28:52]** kriege oder das Loch in der Wand borgen kann. Das ist ein Tool. Und derjenige,

**[00:28:56]** der gebohrt oder geschraubt hat, ist dann der Mensch, der stolz ist auf den Output.

**[00:29:01]** Und so müssen wir dann muslimusikieren.

**[00:29:04]** Genau, so muss es sein und wenn direkt müssen wir hinterher verstehen, dass der Mensch eigentlich

**[00:29:08]** ein Bild an die Band hängen wollte.

**[00:29:09]** Das ist der eigentliche Output.

**[00:29:10]** Das ist auch nochmal die eine Geschichte, die ich vorhin angefangen habe, um zu sehen

**[00:29:13]** und ich glaube, das ist total wichtig.

**[00:29:14]** Ich glaube, das ist genau dieses Thema, wir müssen uns mehr fokussieren und bekennen

**[00:29:18]** das auch mehr auf das, was wir draußen eigentlich als Geschäft machen.

**[00:29:21]** Also wir als Unternehmen bieten ja etwas an, was da draußen Menschen in diesem Moment ermöglicht,

**[00:29:27]** eben das Bild vielleicht an jemanden zu hängen.

**[00:29:28]** Und das ist, glaube ich, genau das Thema, stärker darauf zu fokussieren auf die echte Wirkung

**[00:29:32]** und weniger auf, um durch Schichten sich durchzuarbeiten und jemanden zu finden, der irgendwo

**[00:29:37]** den Ball auffangen kann.

**[00:29:38]** Und ich glaube, da kann KI echt helfen.

**[00:29:41]** Ich glaube, Mark, weil noch etwas Positives zu fragen.

**[00:29:44]** Ich habe nämlich noch zwei kritische Themen da.

**[00:29:47]** Ja, ich wollte tatsächlich noch etwas aufgreifen.

**[00:29:49]** Vorwärts zu weit abdriften, wollte ich kurz mal den Ball aufgreifen.

**[00:29:52]** Wir hatten es ja eben, wenn Teams entstehen, müssen Brücken gebaut werden und so ein Kram.

**[00:29:57]** Und während wir gesprochen haben, fiel mir da einen Satz ein, den kriege ich vielleicht

**[00:30:00]** gar nicht mehr so flüssig über die Lippen, aber früher hast du ja quasi deine Expertise

**[00:30:05]** auch dadurch zum Besten gegeben, indem du dich in Themen immer mehr spezialisiert hast.

**[00:30:10]** Du hast dir Wissen angeeignet, du hast es angewendet, du bist quasi in Anführungszeichen,

**[00:30:15]** du hast dich lange damit beschäftigt und dann haben die Leute dich angerufen,

**[00:30:18]** Leute haben dich kontaktiert. Deine Meinung war wichtig, nicht nur weil man dich vielleicht

**[00:30:22]** als Mensch mag, sondern weil du schlicht untergreifend schon. Wie hat man einer gesagt, ja, hast

**[00:30:28]** früher schon mal Pferde kotzen sehen, du hast alles Mögliche schon mal irgendwie erlebt

**[00:30:32]** und hast quasi aufgrund dieser ganzen Erfahrung eine Meinung und ein Fachwissen, das hilft

**[00:30:37]** jetzt in dem Projekt weiter. Und wenn ein Projekt Schieflage hatte, das ist ja auch egal

**[00:30:41]** in welcher Firma, dann gab es immer irgendjemanden, wo man sagte, ah ja, hat dann der,

**[00:30:45]** Ja, da schon mal drauf geguckt, weil wenn einer das weißt, dann der ruft den doch mal an.

**[00:30:50]** Und das demokratisiert sich jetzt ja auch.

**[00:30:53]** Jetzt ist ja nicht in Grunde der, würde ich jetzt mal behaupten, der das tiefste Wissen

**[00:30:58]** in ABC hat automatisch der meistgefragteste, sondern der, der eventuell in der Lage ist

**[00:31:04]** A und B, kreativ zusammenzubringen, Sachen anzuwenden, Türen zu öffnen, die richtigen

**[00:31:10]** Menschen miteinander zu verbinden.

**[00:31:11]** Also es werden auf einmal ganz andere Fähigkeiten und sich auch anzupassen. Also ich meine wer mag denn, dass sich sein Werkzeug, wenn du es vom Schraubenzieher gesprochen hast, ja, heute hast du ein Schraubenzieher in der Hand, das ist ein Werkzeug. Morgen ist es ein Hammer, übermorgen ist es ein Bohrmaschine.

**[00:31:24]** Nächste Woche ein Pressloft Hammer oder irgendwas anderes und dann auf einmal ist es ein Löffel. Ja, weil das Ding sticht und ergreifend, es kommen neue Produkte raus und du musst deine Art und Weise, wie du dich daran wachst, immer wieder ein bisschen up to date halten.

**[00:31:37]** viel mehr als früher. Und ich glaube, das sind so ein paar Eigenschaften, die werden uns

**[00:31:42]** jetzt immer mehr begegnen. Das wollte ich noch zum Besten geben. Danke Jens, dass

**[00:31:46]** ihr das aufgefallen ist, darum danke, dass ich noch mal sagen durfte.

**[00:31:49]** Natürlich. Ihr seid ein Team. Was seht ihr?

**[00:31:53]** Ja, definitiv. Wie so eine eingespielte Maschine. Aber auch nur, weil ich immer

**[00:31:58]** sein aktualisiertes Skill... Nein, nein, ich kriege ja mal sein aktualisiertes Skill

**[00:32:02]** im D, das hau ich in meinen LL-M rein, dann weiß ich genau, wie ich mich in

**[00:32:05]** Da hab ich aber gellicherweise, das muss ich auch noch sagen, ich hab mir auf Github im

**[00:32:11]** Pressums Ding gemacht, damit meine ganzen Github-Pages immer so im Pressum haben.

**[00:32:14]** Und da hab ich mir das von dir, die Identity-MD, auf meinem Impressums-Gill hoch, damit ich

**[00:32:20]** immer meiner KI sagen kann, wie denke ich, was erwarte ich, wie rede ich, damit ich

**[00:32:26]** das da adressieren kann und das hab ich jetzt auch auf Public, das heißt jeder

**[00:32:30]** könnte quasi der, der Meinung ist wie reagiert, in der Marke auch was, das mal ausprobieren.

**[00:32:34]** Ja, ich habe meine eigene Identity im Debate, weiß gar nicht, wie stark ich sie freigebe, aber ich habe sie ein bisschen angepasst.

**[00:32:39]** Aber ja, noch mal ein anderes, da können wir auch immer mal darüber reden, dass das Thema mit den Identities übergeben auch ein total wichtiges Thema ist, wenn ich mit einem LMM reagiere.

**[00:32:48]** Und vor allem, wenn wir im Prinzip nicht mehr immer mit dem Gleichen arbeiten, dann werden solche Identity-Files zusammen mit dem Kontext, den ich der KI übergebe, ob ich das über eine kleine Datenbank mache,

**[00:32:58]** oder ebenfalls über Katte-Dateien oder durch Prompenden.

**[00:33:02]** Das wird meiner Meinung nach so ein bisschen der Handshake der Zukunft,

**[00:33:05]** der Informationshandshake der Zukunft.

**[00:33:08]** Weil das ist schon ein anderes Output.

**[00:33:10]** Ob es jetzt Mark, René, du oder ich irgendwie mit einer KI redest

**[00:33:14]** oder mit unseren KI unsere Vertrauensreden,

**[00:33:16]** da werden immer andere Ergebnisse rauskommen,

**[00:33:18]** weil unsere Identity spielt damit.

**[00:33:20]** Und ich glaube, das ist auch ein wichtiger Kern

**[00:33:22]** für die Diskussion für Organisationen, die wir haben.

**[00:33:24]** Die Identity von uns, auch das macht eine Organisation auch.

**[00:33:28]** Also, wenn wir jetzt nur Platz Skills kopieren, also wir fangen jetzt an, unsere Skills zu beschreiben, was wir in unserer Tätigkeit zu tun,

**[00:33:36]** dann ist das natürlich auch hinter runtergebrochen in den einzelnen Part, dass die kleine Fließbandarbeit,

**[00:33:42]** wie man es mal gerade beschrieben hat, diese eine kleine Schritt, die ich am Fließband tue in dem Moment.

**[00:33:47]** Auch das würde sich wieder finden bei unserer Tätigkeit wahrscheinlich ein oder anderes Mal, wenn wir unsere Skills beschreiben.

**[00:33:51]** Aber natürlich ist es zusätzlich, bei allen Menschen so, dass diese Identity mit reinkommt.

**[00:33:56]** mit reinkommen. Und diese Identity verändert ein bisschen, auch in Ordnisation, weil man

**[00:34:00]** ständig trotzdem noch gewisse Verhaltensweisen zeigen muss, den doch dem besten Weg rausfinden

**[00:34:06]** muss, weil alles ist nicht perfekt. Es wird niemals auch das Streamline SuperKI Ordnisation

**[00:34:11]** in dem Sinne geben. Es wird immer ein Zusammenspiel zwischen auch einer KI, die ausfällt, deren

**[00:34:15]** Tokens zu Ende gelaufen sind, wo der Server Schrankern doch ausgeschaltet wird, weil

**[00:34:20]** gerade jemand da den Stecker gezogen hat oder irgendwas anderes. Also auch das wird

**[00:34:23]** in Zukunft immer noch passieren und dementsprechend braucht es dann die Identitäten dazwischen,

**[00:34:29]** die wir Menschen dann auch durchaus sind, die immer noch auf so einem System einfach reagieren

**[00:34:33]** können.

**[00:34:34]** Da können wir auch, falls Leute da unsicher sind, kann man eine schöne Analogie machen.

**[00:34:38]** Wir haben ja Gesetze in der Welt, jeder Rechtsstaater sei eine Rechtsgesetze und wir haben trotzdem

**[00:34:42]** Richter.

**[00:34:43]** Weil das, was zwischen den Gesetzen ist, muss interpretiert und muss irgendwie abgewogen

**[00:34:47]** werden.

**[00:34:48]** Und das lässt sich genau so eben auch auf unsere Welt ändern.

**[00:34:51]** Die Welt ist überhaupt nicht logisch, sie ist eigentlich das Gegenteil von logisch, das sieht man ja leider auch jeden Tag, aber wir müssen also in den Abfolgen, die in den Prozessen passieren, braucht man das Mittelding dazwischen, um so ein bisschen eine Einschätzung zu geben, sie eine ja, das ach, ich glaub, ich lass das mal so laufen, oder nee, das stoppe ich doch lieber jetzt, weil ich hab zum Beispiel, also KI hat ja keine Intention, KI will nichts, also müssen wir erstmal die Intention überhaupt reinbringen, damit ich was will.

**[00:35:18]** Und dann hat KI auch keine Risiko-Wertung, kann also nicht sagen, ob das jetzt,

**[00:35:23]** also kann ich vielleicht ein bisschen so sagen, okay, das könnte ein Atomkrieg auslösen, das mache ich jetzt mal nicht, auf der

**[00:35:28]** Ebene wird es mit wahrscheinlich mittlerweile schon funktionieren, aber auf einer, sagen wir eher normalen Ebene, die jetzt uns jeden Tag angeht, dass dann jemand sagt,

**[00:35:35]** hm, vielleicht ist es doch ein bisschen zu risikoreich, dass ich den Menschen jetzt zehn Meter näher an diese Hochwoll-Anlage stehen lasse und so,

**[00:35:42]** so was, also diese Gesamteinschätzung, das können auch, das können eigentlich nur Menschen,

**[00:35:48]** und ich glaube auch immer nur Menschen. Das wird es also, das ist auch ganz ziel dieses zu automatisieren,

**[00:35:53]** sondern das operative Renat, das, was Kosten generiert und Zeit frisst, das will man ja automatisieren.

**[00:36:01]** Aber ich natürlich auch sagen würde bei manchen Sachen, glaube ich René, da würde ich, da werden solche Themen auch automatisiert werden können.

**[00:36:07]** Also wenn wir jetzt dann immer den, ich werde jetzt mal den kritischen Blick nach China haben.

**[00:36:11]** Was wir natürlich da sehen in den Fabriken vor Ort, ist natürlich, dass wir sehr, sehr viele Arbeiter, die dann im Prinzip wiederkehrende Tätigkeiten ausführen, jetzt mittlerweile schon mit Videokameras ausgestattet werden und ihre händische Arbeit quasi aufgenommen wird.

**[00:36:28]** Also ganze ganze fabriken sind komplett mit videokameras ausgestattet und wir die gleiche kleine stelle gemacht wird wird quasi schon aufgenommen das könnte man sich natürlich auch größer vorstellen

**[00:36:36]** Also nicht nur an so einer fließbantehigkeit sitzen sondern auch durch boro rollen wir durchlaufen

**[00:36:41]** Da können wir auch mal protokollieren dass ich denn so den ganz dach mache wenn ich durch das office war

**[00:36:44]** Es war so was nao da aus zu erschließen was braucht denn was braucht es will keiner

**[00:36:50]** Aber was braucht denn so ein robot tatsächlich vielleicht und ein anderes thema was ich noch als kritik nur rein werfen werde

**[00:36:56]** Das war, was ich auch gesehen habe, wo ich auch erstaunt war, wo es Gott sei Dank schnell

**[00:37:00]** einen Anfalt auch zugeladen war.

**[00:37:02]** Es gibt gewisse chinesische Unternehmen, die auch ihre Mitarbeiter schon zwingen, quasi

**[00:37:06]** Skill im Defiles wirklich abzulegen über ihre Tätigkeit, um dann zu sagen, ja, das

**[00:37:11]** kann ich dann hinterher mit einer KI automatisieren, was diese Person macht.

**[00:37:16]** Interessante Weise ist direkt ein Service entstanden, der hieß eben wie, ich muss

**[00:37:19]** mal nachgucken, Anti-Distellation Skill, das ist super, da ist eine Chinesin,

**[00:37:24]** Die hat es direkt geschrieben.

**[00:37:27]** Ich wollte gerade sagen, einer von drei kann es wahrscheinlich aussprechen.

**[00:37:34]** Aber der Skill hilft dir, der ist wie so ein Cleaning Layer.

**[00:37:39]** Der zieht quasi alle wirklich interessanten Sachen, die du in deinem Skill reingeschrieben hast,

**[00:37:45]** zieht da raus und lässt dir quasi nur das Nackte ein bisschen hier schrauben,

**[00:37:49]** ein bisschen da was machen.

**[00:37:51]** zurück. Und das kannst du dann als Management übergeben. Da kannst du sicher sein, wenn

**[00:37:54]** Management den MD-Skill einsetzt, dann wird dein Job trotzdem noch weiter benötigt.

**[00:37:59]** Das sind natürlich auch so. Also die Care-Seiten der Medaille. Da müssen wir auch irgendwie

**[00:38:03]** offen darüber reden, dass solche Sachen passieren.

**[00:38:05]** Ja, also ich habe ein paar Jahre in China gelebt und habe da durchaus, sagen wir so,

**[00:38:10]** meine eigene Sicht. Ich bin gar, also erst mal die Freiheitsordnung finde ich super

**[00:38:15]** und die totale Überwachung finde ich nicht super, das ist klar. Aber in dem System

**[00:38:19]** Schiener selber. Also so schlecht ist es gar nicht. Also es ist schon sehr effizient, wenn man

**[00:38:27]** den Schiener nennt und es ist nicht umsonst, dass das macht meinem dafür halt nach dem Momentan der

**[00:38:31]** globale Gewinner ist. Erst einmal machen sie keine idiomatischen Triege, sondern die funktionieren,

**[00:38:35]** sie gehen ganz langsam rein und haben sich jetzt, also wenn er den letzten fünf Jahresplan,

**[00:38:41]** den er jetzt 12 Punkten angeschaut hat, da sind sechs Punkte, wo sie Weltmattführer werden

**[00:38:45]** wollen und sechs andere, wo sie zumindest globale Durchbrüche erreichen wollen und es ist Quantum

**[00:38:52]** dabei, das Durchbrüche dabei, das ist also auch Neurolink im Gehirn und so weiter. Und das,

**[00:38:57]** die so konzentriert und fokussiert Technologie einsetzen, hat, ist auch dem Umstand geschuldet,

**[00:39:05]** dass diese Nation weltweit führen werden wird in dieser Technologie und damit ist das auch

**[00:39:10]** eher ein Geschäftsmodell, also etwas auszuprobieren, damit dann die anderen auf der ganzen Welt,

**[00:39:14]** die dann die Technologiebeeren kaufen müssen, um die Produktivität zu erreichen, da eben

**[00:39:20]** Kunden werden. Das ist ganz simpel. Ja, also da meine persönliche Freiheit, die ist mir

**[00:39:27]** sehr wichtig. Das würde ich nie akzeptieren. Das wird wahrscheinlich in einer westlichen

**[00:39:31]** Gesellschaft sowieso kaum möglich sein. Aber wir dürfen auch nicht so boniert sein und

**[00:39:37]** missachten, dass in China seit tausend von Jahren, vier Jahren Kultur herrscht. Das

**[00:39:42]** Es ist also nicht, dass dort Menschen sich anders fühlen oder Freiheit wird einfach anders bewertet.

**[00:39:49]** Es ist einfach ein anderes Gut, als anderes Gut ist.

**[00:39:53]** Das eine ist nicht besser als das andere, es ist eine andere Bewertung, ein anderes System.

**[00:39:58]** Wir müssen das nicht gut finden, Sie müssen uns nicht gut finden.

**[00:40:01]** Ich habe da immer etwas, das angeht, ein völlig anderes Beispiel.

**[00:40:04]** Als ich da gelebt habe, war es noch sehr usus, dass man in China auf die Straße gespuckt hat.

**[00:40:10]** Also das finden wir, um nicht nur Spucken, sondern ich mach das nicht vor, aber ihr könnt euch vorstellen, so richtig, aus dem tiefsten Innern, weil dahinter steckte die Idee, sich zu reinigen, also das Unrein aus dem Körper zu lassen.

**[00:40:24]** Gleichzeitig haben alle Chinesen, die ich gesprochen habe, mich angeeckelt angeguckt, wenn ich genießt habe, wenn ich Hatshi gemacht habe.

**[00:40:33]** Da haben die mich angeeckelt und sagen, oh, was ist das denn? Also genauso angeeckelt, wie ich angeeckelt habe.

**[00:40:37]** Das ist nur, das eine ist nicht besser als das andere, aber es sind einfach verschiedene Sichtweisen in einem kulturellen Bezug und man muss es eher lernen, dass es Unterschiede gibt und mit den Unterschieden umgehen und nicht bewerten.

**[00:40:50]** Aber jetzt zurück zur Technologie.

**[00:40:52]** Da gibt es diese hohe Technologieaffinität.

**[00:40:55]** Ich kann nur jedem anraten, weil irgendein x-bedehmiges Video, das nicht älter als drei, vier Monate ist, in YouTube über Shen-Sensee finden.

**[00:41:03]** Mann, und ich habe Teile, was da gezeigt wird, habe ich auch live erlebt, also die Technologie, also in den Unternehmens, skillbasiertes Arbeiten jetzt schon einzuführen.

**[00:41:15]** Trainingseinheit mit Kamera, auf dem Kopf zu, dass ich mitlaufen kann und dass dann später eine Robotik, das sogar nicht über die Robotiken und die Weltführer, Weltmarktführer werden, werden sie aussehen zum Grunde heute ja schon.

**[00:41:26]** Das ist Teil des Gesamtplans dieser Industrie oder dieser Nation, sagen wir mal.

**[00:41:33]** Und ich behaupte mal, die werden da auch sehr erfolgreich sein mit ihrem Plan.

**[00:41:37]** Also, wenn ich mir überlege, als wir von Open Claw unsere Folge gemacht haben,

**[00:41:42]** wir in der Vorbereitung gesehen haben, wie dann dort, ich sag mal so,

**[00:41:45]** Installationspartys oder Installationsdienst leisten und keine Ahnung, was stattfindet.

**[00:41:49]** Und wenn du dann, mal egal, wo du selbst da langläufst und über Open Claw sprichst,

**[00:41:55]** sprichst, dann erstmal so, ja, Hilfe. Also, nee, weiß nicht. Also, mehr die Ablehnung.

**[00:42:03]** Oder Schwieriges Überzeugen, dich entgegen schallert, während dort da hocken Menschen

**[00:42:09]** mit welchen Getränken auch immer und Notebooks und in Herrschaden und installieren sich

**[00:42:14]** den Kram, während wir also quasi sinngemäß, jetzt also nicht wir als Firma oder wir als

**[00:42:19]** Personen, sondern mehr so als Gesellschaft, uns überlegen, ah, verdammte Axt und

**[00:42:24]** könnten wir da nicht was regulieren oder irgendwas? Ja. Und da geht es irgendwie

**[00:42:29]** feuerfrei. Vielleicht ist es irgendwo auch dazwischen irgendwo die Wahrheit, wo man

**[00:42:32]** sich vielleicht treffen sollte. Ja, ich wollte sagen, es gibt keine Wahrheit.

**[00:42:35]** Beides hat seine Berechtigung. Wir haben eine andere Kultur und wir wollen

**[00:42:38]** Dinge verstehen. Es ist ja der, der, der, also man sagt ja, der Asiatische ist ja

**[00:42:43]** eher der Weg, das Ziel und nicht das Ziel. Bei uns ist das Ziel das Ziel. Und

**[00:42:48]** beides hat seine Berechtigung. Das eine ist nicht besser als das andere.

**[00:42:51]** Momentan wirkt es eine schneller, okay? Also wir können auch tatsächlich auch feststellen, wie viel in besonderes Europa gerade nicht funktioniert. Das ist auch alles wahr.

**[00:43:01]** Aber über die gesamte, sagen wir jetzt, die nächsten zehn Jahre wird sich das auch wieder justieren. Also jede Kultur hat so seine Vorzüge momentan.

**[00:43:09]** Aber dahinter steht auf jeden Fall in China ein großes Geschäftsmodell auf jeden Fall. Und Open Cloud Installation ist da jetzt ein Service.

**[00:43:16]** Service. Da gehst du wie zu Kiosk hin, bringst deine Gräte mit und hast eine Stunde später

**[00:43:19]** alles drauf installiert von irgendjemandem. Damit sind wir wieder bei Skills. Das hätte

**[00:43:26]** ich gebrauchen können in den letzten Wochen, weil ich hier einige Nächte verbracht habe

**[00:43:30]** mit einer, ich mache es ja auch sehr, sehr vorsichtig und sehr sicher und will es auch

**[00:43:33]** wieder selber für mich lernen und was man da so tut. Und muss auch sagen, ehrlicherweise

**[00:43:37]** auch dieser Prozess, den ich jetzt wieder durchlebt habe, alleine bei dieser Orpenclaw-Installation,

**[00:43:42]** auch bei den Themen über die Mark und die ich dann ja auch über Spalinkt in uns mal austauschen,

**[00:43:46]** wie man da jetzt im Prinzip so ein Memory aufbaut, wie man so ein Bolt aufbaut, wie man im Prinzip

**[00:43:50]** den Handshake auch zwischen Agents und sowas anrichtet. Ich glaube, es war nötig, dass

**[00:43:54]** ich diese Strecke gegangen bin, dass ich jetzt wieder selber so gefühlt habe. Und

**[00:43:59]** das ist, glaube ich, auch so ein Ding, muss ich sagen.

**[00:44:00]** Ja, das ist einfach wertvoll, wenn man sich mit Technologie, die ehrlicherweise

**[00:44:07]** auch so einfach zugänglich ist, beschäftigt. Also jetzt mal platt gesagt, das habe

**[00:44:11]** gemacht. Ich habe einfach im Prinzip diese Installation gemacht und frage die

**[00:44:14]** ganze Zeit, wäre nicht das Tour ne andere KI, was ich da eigentlich tue? Und lass

**[00:44:17]** mir das auch erklären. Vergess es auch teilweise weder muss. Also wie immer

**[00:44:20]** wieder nachfragen, wenn ich dann den nächsten Terminalbefehl dann nicht mehr

**[00:44:22]** weiß. Aber das ist möglich, weißt du? Also ich mache da Sachen, hab jetzt auch

**[00:44:26]** mein Github, was irgendwie seit fünf Jahren stillgelegt war, mal wieder

**[00:44:30]** aktiviert. Vorsicht, ich habe mal alle Sachen von damals auf

**[00:44:32]** privat gestellt, damit es nicht mal so peinlich ist, weil sie schon älter

**[00:44:34]** sind, ehrlicherweise. Aber nächstes und trotz, also der Aufruf da noch

**[00:44:39]** mal, also beschäftigt euch mit den Sachen. Also es ist dann auch wieder was anderes, wenn du das mitbekommst,

**[00:44:43]** weil du kommst auf neue Ideen, du verstehst, was es bedeutet. Und deshalb komme ich auf so Themen,

**[00:44:49]** die teilweise auch noch nicht richtig adressiert sind. Wer hält denn im Prinzip hinterher den

**[00:44:55]** Kontext am Leben? Also diese Kontextinformationen, die nötig sind, die jetzt zum Beispiel in

**[00:45:00]** so einer normalen Organisation durch Meetings, durch Informationsaustausch, dass ich Leute

**[00:45:05]** dass ich ausgebildet bin in meinen Skills durch eine Universität oder durch einen Berufsweg,

**[00:45:11]** den ich gemacht habe, dass ich weiß, welche Dienorm, welche Security-Checks oder irgendwelche

**[00:45:15]** anderen Sachen gemacht werden müssen, wenn ich etwas dienen will. Wer hält das alles so am

**[00:45:19]** Laufen in dieser agentischen Welt in Zukunft? Das wird eine total spannende Frage. Das ist

**[00:45:23]** nie zu beantwortet, ehrlicherweise. Das sehe ich gerade. Wenn ich mich an diese Sachen

**[00:45:27]** ran nehme, dann kommen nämlich immer wieder diese kleinen Fehler, ob das reine kleine,

**[00:45:31]** temporale Fehler sind. Wenn die eine KI schon denkt, dass die andere etwas schon gemacht

**[00:45:35]** hat, aber noch gar nicht fertig ist. Wenn ein Modell das Lokal auf meinem Rechner eigentlich

**[00:45:39]** was machen sollte, dann ein Timeout hat, weil es noch nicht warm gelaufen war und der andere

**[00:45:43]** dann eben zurückgeht und einfach irgendwas macht, auch selbst wenn da schon Confidence

**[00:45:48]** Gores oder was anders ist in der Lichtsenseit. Also das ist eine komplexe, ich bin heilfroh,

**[00:45:53]** dass ich mich jetzt wieder durch so ein paar Nachtschichten die letzten Monate und Wochenendschichten

**[00:45:58]** quasi da durchgefuddelt habe, weil es hat mir da total geholfen, diese Sachen besser

**[00:46:02]** zu verstehen. Und ich glaube, das ist weiter ein Wertvoll in dieser Welt, in der wir uns

**[00:46:05]** bewegen und sich mit diesen Themen zu beschäftigen.

**[00:46:07]** Und das ist, wenn ich auch einen Aufruf dabei unterstütze, für jeden, der gerade zuhört,

**[00:46:12]** also jeder muss sich nicht open-cloid zertehren. Das ist vielleicht, das machen nur die Leute

**[00:46:15]** auf wirklich ein bisschen Ahnung, weil da ist in Ruhe Sicherheitsrisiko immer noch dabei

**[00:46:20]** und das muss man einfach wissen, was man da tut. Aber sich zum Beispiel mal für

**[00:46:24]** ein Wochenende mit einem Trophic, mit Cloud Code auseinanderzusetzen und mal ihn

**[00:46:29]** zu bitten oder auch auf dem i-codex oder oder oder google i studio und mal ein

**[00:46:34]** stück software selber zu schreiben ich bin der überzeugung das ist heute ein

**[00:46:38]** live skill genauso wie wir alle wissen wie ich im reifen wechsel kann es nicht

**[00:46:43]** mehr tun aber wir wissen es im präzit ist das ein live skill dass man das

**[00:46:47]** versteht die mechanie der versteht damit das nicht aussieht wie so einer

**[00:46:51]** black box und ich habe überhaupt keine keine vorstellung und man kann

**[00:46:55]** sich ein kleines spiel programmieren das muss ja nicht groß sein irgendwas

**[00:46:58]** Irgend so ein Hangman-Spiel, irgendein Worterrat-Spiel, das ist wahrscheinlich ein Prompt mit fünf Worten und dann geschieht es sowieso automatisch, aber man kann zumindest sehen, wie es funktioniert.

**[00:47:08]** Also, sich damit auseinanderzusetzen ist echt wichtig.

**[00:47:11]** Total, total.

**[00:47:12]** Ich habe mir ja tatsächlich, weil du sagst, das Spiel, in meiner Jugend habe ich ein Spiel gespielt, das hieß Bubble Bobble.

**[00:47:18]** Da hast du so kleine Trachen gesteuert, die Ballons nicht so Seifenblasen geschossen haben.

**[00:47:24]** Das geliebt damals, aber irgendwie gibt es das irgendwie nirgends mehr so richtig und das hat mir dann, ich glaube das war Gemini, dass mir das dann wieder gebaut hat.

**[00:47:31]** Dem ich gesagt habe, hier guck mal das und das und hier sind ein paar Website und ein paar Videos, schau dir das an und mach.

**[00:47:37]** Das war ganz lustig und während ihr gesprochen habt und du von dem Reifenwechselbeispiel kamst, fiel mir ein anderes Beispiel ein.

**[00:47:43]** Ich meine, jetzt sind wir alle da verraten, wir verraten keine Details, aber auch schon das eine oder andere Jächen auf der Welt haben in der IT vielleicht oder das eine oder andere gesehen.

**[00:47:51]** Als ich mit IT angefangen habe, also in meinem Praktikantenplatz gab es Lochkarten und später habe ich dann mit DOS Terminal und bei mir hatte quasi Textverarbeitung noch kein

**[00:48:01]** What you see is what you get, ja, sondern du hast so mit Texte gearbeitet, so.

**[00:48:05]** Dann kam irgendwann Windows und kraftliche Benutzinterface ist so bla bla bla und das ist ganz schön.

**[00:48:09]** Und die Leute haben mich angeguckt, wie, als ob ich vom anderen Stern kommen, als ich dann damals habe ich noch Windows bedient, Leute, die mich kennen, wissen, das muss schon sehr lange her sein.

**[00:48:18]** habe ich dann gesagt hier CMD, glaube ich, war das damals bei Windows, dass du auf das Terminal, also DOS kommst und die so, was ist denn das für ein schwarzes Fenster? Wo ist denn die Farbe? Was machst du da? Und du denkst da so, hey, was willst denn du von mir? Das ist DOS, also da kann man doch was eingeben hier, Verzeichnissen erstellen und verschieben und löschen und machen. Und keine Ahnung, was.

**[00:48:39]** und war unabhängig davon, dass ich Windows schon seit Windows 19 nicht mehr aktiv

**[00:48:44]** im Einsatz habe. Ist das denn noch ein Wissen, wenn du weißt, wie ist das

**[00:48:48]** Terminal und worauf fußt das denn? Durchaus etwas, das lernst du, oh ich seh'

**[00:48:53]** den jetzt schon, Kopfschütteln für alle, die es nur hören. Ist das durchaus

**[00:48:58]** etwas, das mich auf meiner Lernreise durchaus begleitet hat und heute

**[00:49:01]** immer noch ein wertvolles Wissen für mich ist, um zu verstehen, wie die

**[00:49:05]** Schose zusammenhängt und ich glaube, das nimmt uns auch diese ganze

**[00:49:08]** KI-Reise, wenn sich alle zwei, drei, vier, acht, zwölf Wochen Modelle, Verfahrentechniken

**[00:49:13]** wie auch immer ändern. Das nimmt uns nicht, weil wir diese Reise halt, ja, weil wir

**[00:49:18]** offenen Herzens damit gehen und diese Reise begleiten und uns dem Ganzen nicht

**[00:49:22]** verschließen und sagen, das wird schon weggehen und keine Ahnung, was und uns

**[00:49:26]** überraschen lassen, sondern wir gehen diese Reise. Jens, du hast den Kopf geschüttelt.

**[00:49:31]** Ja, ich hab nur reagiert, alles gut. Ich bin, ja, ich hab den Kopf geschüttelt alles,

**[00:49:34]** ich bin ja, sagen wir mal so, bis zu einem gewissen Grad.

**[00:49:37]** Na, ich glaube tatsächlich ist es natürlich auch eine gravische,

**[00:49:40]** wo man benutzt so eine Fläche auch gut, weil nicht jeder sich immer überall rein

**[00:49:43]** denken muss und ich will auch so ähnlich wie René das glaube ich gerade gesagt hat.

**[00:49:46]** Nicht jeder muss jetzt draußen eine Open Cloud Installation machen,

**[00:49:48]** um sich mit dem Thema KI zu beschäftigen.

**[00:49:50]** Das muss einfach nicht sein und genauso muss nicht jeder zwei Open Cloud Installation muss jeder machen.

**[00:49:54]** Genau, muss auch nicht irgendeinig.

**[00:49:56]** Müssen wir uns nicht mehr in einer Terminal Landschaft bewegen.

**[00:49:59]** Ja, ich, dass ich es jetzt mache, ist dann einfach einfach dem Thema

**[00:50:02]** wie schuldet, dass es einfach einfacher ist, mit dem Cloud Code Agent

**[00:50:05]** auch als Terminalfenster zu arbeiten, um dann von einem Terminalfenster als andere die Sachen

**[00:50:08]** rüberzukupieren und so was. Ja, aber das darf natürlich nicht das Ende der Fahnensteige sein,

**[00:50:12]** weil wir müssen da, glaube ich, uns auch weiter bewegen, dass es eben zugänglich ist für den

**[00:50:16]** Rest auch. Und ich glaube, was du gesagt hast, der einzige Punkt, den ich unterstreiche, ist,

**[00:50:21]** dass grundsätzlich verstanden zwar, dass du sagst, wie kann denn sowas funktionieren? Was ist

**[00:50:27]** vielleicht eine Ordnerstruktur auch, wenn ich auch mal am iPhone nicht mehr wissen muss,

**[00:50:31]** wo die Bilder in welchem Ordner gespeichert werden.

**[00:50:33]** Ist es trotzdem okay, ich das zu wissen, genauso wie es okay war, als ich damals angefangen

**[00:50:38]** habe, wenn man gesagt hat, ja, man hat es nicht mit einem Visibik-Editor gemacht, sondern

**[00:50:41]** hat man zwischendurch doch mal mit BabyEdit noch mal den Code selber beschrieben oder

**[00:50:45]** etwas anderes.

**[00:50:46]** Auf den Endes vielleicht mit einem Visibik-Editor, oder damals noch schon gegen oder so etwas.

**[00:50:49]** Um es grundsätzlich verstehen, was da passiert, da bin ich bei euch, weil ich glaube René

**[00:50:53]** ist auch gerade schon reagiert, als Alte, als Thila, ja, und weil wir mir auch noch

**[00:50:57]** sagen, nein, ihr müsst alle im Terminal arbeiten.

**[00:51:00]** Ja, genau. Aber ich will doch einen Punkt. Warum? Also, es ist gar nicht so nördig.

**[00:51:06]** Mark und ich, wir sind natürlich die Mega-Nerds, klar. Ich prüge mir auch die ganze Zeit vor mich hin.

**[00:51:10]** Aber ich glaube, für die Welt draußen, für die Menschen ist es wichtig, souverän zu bleiben.

**[00:51:17]** Also, dass es kein Eier tanzt, dass du dich nicht unwohl fühlst, denn auf den Knopf drückst du, was passiert denn da?

**[00:51:23]** Das weiß du jeder Mensch fühlt sich nicht unwohl, wenn er ins Auto steigt haben macht und fährt, weil er weiß irgendwie vorne,

**[00:51:29]** meistens in der Motor, irgendwie, da fallen mir auch Menschen ein, ja, aber im Prinzip, sagen wir mal,

**[00:51:37]** oder andersherum, die Menschen, die ganz unsicher fahren, sind auch die, die überhaupt keine Ahnung haben von dem Ganzen.

**[00:51:43]** Es gibt so eine leichte Korrelation, so ein ganz bisschen, das heißt, da ja die Welt immer mehr,

**[00:51:52]** mit IT-Atefakten ausgestattet werden wird, nie unser Leben verändern, hoffentlich vereinfachen,

**[00:51:59]** aber auch sehr kompliziert machen. Ist es jeden Mensch angeraten, darin sich souverän zu bewegen

**[00:52:06]** in dieser Welt, indem ich zumindest eine wahre Vorstellung habe, was passiert da eigentlich?

**[00:52:10]** Das macht mich, ja, souverän, einfach, ich bin nicht so abhängig, ich fühle mich nicht so

**[00:52:18]** allein. Ich fühle mich okay, ich kann damit umgehen, ich kann das einschätzen, was passiert. Ich kann den

**[00:52:25]** nächsten Schritt gehen, ich bleibe nicht stehen. Wenn ich mir das so anschaue, ich meine, was haben

**[00:52:29]** wir denn heute gesprochen? Ich glaube, was bei den Hörenden rüber kommt ist, Skills ist mehr

**[00:52:36]** als nur der Skill, den der Agent lernt. Skills ist das, ja, wie der Agent schon das Thema

**[00:52:43]** Arbeiten Skills ist, aber auch das, wie geht der Mensch damit um? Wie gehen wir als Menschen

**[00:52:48]** miteinander und Skills um? Und das dritte war halt auch noch das Thema, wie geht man als

**[00:52:52]** Organisation um? Wir hatten das Thema Kästchen, flache Hierarchien. Und ich glaube, und die Frage

**[00:52:58]** möchte ich gar nicht so sehr, die will ich einfach nur mal so zum Nachdenken ein,

**[00:53:01]** nochmal mitgeben. Das letzte Mal im Podcast hast du gesagt gehabt, nicht nach dem Motto,

**[00:53:06]** Was brauche ich demnächst, sondern was brauche ich in fünf Jahren, sondern wie wird es in 50 Jahren sein,

**[00:53:13]** hattest du mal so ähnlich, glaube ich, das erste Mal gebracht.

**[00:53:16]** Von der Seite, ich fand das total spannend, was wir heute besprochen haben, ich fand auch total spannend,

**[00:53:21]** was seit unserem letzten Mal alles passiert ist, wir hatten es am Anfang kurz angedeutet,

**[00:53:25]** weil wenn wir uns damals gesagt hätten, wozu technologisch heute in der Lage ist,

**[00:53:32]** ist. Hätten wir, glaube ich, alle, und da möchte ich auch mich selbst überhaupt nicht ausnehmen,

**[00:53:37]** niemals nicht gedacht, dass diese technologischen Möglichkeiten, die zum Zeitpunkt der Aufnahme

**[00:53:43]** entstanden sind und auch die Aufnahme ist ein anderer Tag als ausstrahlen. Von der Seite,

**[00:53:48]** mal gucken, was auch vielleicht noch bis dahin kommen wird. Das ist eine faszinierend krasse Zeit.

**[00:53:52]** Ja, also von der Seite, ich weiß nicht, wie es euch geht, aber ich fand das sehr gelungen,

**[00:53:58]** Wobei wir gesprochen haben, ich will auf jeden Fall mich gerne wieder melden, dass wir uns

**[00:54:02]** noch wieder mal irgendwann eine Folge machen, weil ich meine, das ist ja ein total spannendes

**[00:54:05]** Thema.

**[00:54:06]** Und von der Seite, also falls jetzt nicht irgendeiner der Meinung ist, er möchte noch einen Abschlusswort

**[00:54:10]** zu uns geben.

**[00:54:11]** Ja, ich würde gerade für euch einen tollen Tipp, also mach doch, versuch doch immer Leute

**[00:54:15]** vor einem Jahr und dann das Delta quasi auch zu besprechen, was man damals besprochen

**[00:54:20]** hat, so 10 Minuten.

**[00:54:21]** Ja, gerne.

**[00:54:22]** Die 10 von damals, ein Jahr später, noch mal riftet mich mit derselben Person.

**[00:54:25]** Das wäre sicherlich spannend.

**[00:54:26]** Würde ich mich natürlich auch gerne mit anbieten.

**[00:54:27]** Und für alle Hürrenden überlegt man ganz kurz selbst jetzt und vor einem Jahr, was ihr vor

**[00:54:35]** einem Jahr glaubt, was heute möglich ist, was heute wirklich möglich ist. Und dieses Delta

**[00:54:40]** kann man auch mal vorne projizieren. Dann hat man ein bisschen die Idee, dass die Umweltsung

**[00:54:44]** unaufhaltsam auf uns zukommt, aber in so einen positiven Sinne, dass wir da sehr viel

**[00:54:49]** Wirkung rausziehen können. Also beschäftigt euch mit dem Thema. Das ist so das Allerwichtigste,

**[00:54:53]** Was du dir gleich sagen könnt und ja ich find's auch ja echt super mit euch zu plaudern ist echt super weil wir

**[00:54:59]** Merkt man alle haben kontent alle reden über etwas und zwar mit content und jens dein open talk

**[00:55:06]** guck ich mir gerne mal an

**[00:55:10]** Das ist aber dem hintergrund mann mann dann würde ich in guter mannier

**[00:55:17]** Den den abschluss einleuten nee danke dass du da warst

**[00:55:20]** Ja, war wie immer eine Freude. Jens, schön, dass du auch bei einer Folge mit Gast dabei bist.

**[00:55:27]** Das fähl ich immer gerne. Wir haben übrigens im nächsten wieder eingest.

**[00:55:30]** Das ist Karneval.

**[00:55:31]** Das ist Karneval.

**[00:55:32]** Das ist wieder ein Wiederholingstäter.

**[00:55:33]** Du musst dich noch korrigieren, damit du nicht die nächste Mal rausfuß.

**[00:55:35]** Du musst es ist Karneval entkönnen und nicht faschigen.

**[00:55:38]** Das sagst du dem Hesse, weißt du?

**[00:55:40]** Ich kann sowas stehte, Würmscher auf dem Türmsche, mit dem Schirmscher und am Ämge kommt das Stürmscher,

**[00:55:43]** Würmscher mit dem Schirmscher und am Ämge vom Türmsche.

**[00:55:45]** Weißt du, sowas kann ich, ja?

**[00:55:47]** Und faschigen und Karneval auseinander halten, dort kann ich nicht.

**[00:55:49]** Ja, mir war das, ich war früher Hesse, bin in Rheinland-Pfalz zur Schule gegangen.

**[00:55:53]** Da hat einer zu mir gesagt, du gehst also zum Lacher rüber in der Anne Bundesland.

**[00:55:56]** Gut, lassen wir mal dahingestellt.

**[00:55:58]** War schön mit euch.

**[00:56:00]** Danke, dass ihr da wart.

**[00:56:01]** Freue mich aufs Nächsten.

**[00:56:02]** Mal wenn es euch gefallen hat, dann lasst ein Like.

**[00:56:04]** Ein Kommentar erzählt euren Freunden um Bekannten davon, dass es diesen Podcast gibt.

**[00:56:08]** Sollte einen Openclaw oder einen Mythos zuhören.

**[00:56:11]** Wir kommen in Frieden und freuen uns auch über euch als Abonnenten.

**[00:56:14]** Und in diesem Sinne bedanke ich mich bis bald.

**[00:56:17]** Ciao.

**[00:56:19]** Willkommen bei ThinkDifferent, ThinkAI, dem Podcast von Mark und Jens.

**[00:56:25]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:56:31]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:56:38]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:56:42]** H.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
