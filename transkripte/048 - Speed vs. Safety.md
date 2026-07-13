---
title: "Speed vs. Safety"
episode_index: 48
published: "Sun, 12 Jul 2026 20:45:00 +0000"
duration: "1375"
page_url: "https://think-ai.podigee.io/48-speed-vs-safety"
image_url: "https://images.podigee-cdn.net/0x,ssU3eIDt4PMhj5EhrwWKUk1v5vCaSqSQEYpBnNyOK6lM=/https://main.podigee-cdn.net/uploads/u73317/a0832141-5b78-438a-a0b5-a34268a38a5f.jpg"
audio_url: "https://audio.podigee-cdn.net/2532882-m-e89974e8241169c3f9d0e6554501c339.mp3?source=feed"
guid: "b5407179e715825a43366ef5c3613e16"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-07-13T09:29:16+00:00"
---

# Speed vs. Safety

**Veröffentlicht:** Sun, 12 Jul 2026 20:45:00 +0000
**Dauer:** 1375
**Webplayer:** https://think-ai.podigee.io/48-speed-vs-safety
**Cover:** https://images.podigee-cdn.net/0x,ssU3eIDt4PMhj5EhrwWKUk1v5vCaSqSQEYpBnNyOK6lM=/https://main.podigee-cdn.net/uploads/u73317/a0832141-5b78-438a-a0b5-a34268a38a5f.jpg
**Audio:** https://audio.podigee-cdn.net/2532882-m-e89974e8241169c3f9d0e6554501c339.mp3?source=feed

## Beschreibung

Mythos, Fable und die Rückkehr eingeschränkter Modelle
Was macht man, wenn die eigene Loop-Engineering-Folge von letzter Woche von der Realität überholt wird, bevor die Tinte trocken ist? Genau das ist Mark und Jens passiert, deshalb gibt es diese spontane Zusatzfolge. Auslöser ist Fable, das Anthropic-Modell, das vor wenigen Tagen für Nicht-US-Bürger gesperrt wurde.

Die Strategie der US-Regierung könnte sein, ausgewählten Firmen und der eigenen Verwaltung einen Vorsprung beim Schließen genau dieser Lücken zu verschaffen, bevor Modelle aus weniger kontrollierbarer Hand ähnlich leistungsfähig werden. Von dort geht es zu Destillation: Chinesische Modelle bauen die Fähigkeiten großer US-Modelle nach, indem sie ihnen mit automatisierten Massenanfragen quasi das Wissen aus der Token Prediction herausextrahieren. Das trifft auch Unternehmen hart, die ihre Prozesse zu früh auf ein einzelnes Modell ausgerichtet hatten. Mark und Jens berichten von Kanzleien, die ihre komplette Textanalyse auf Fable umgestellt hatten und jetzt vor genau diesem Problem stehen, wenn das Modell abgeschaltet wird. Nebenbei taucht auch noch ein neuer Herausforderer namens Fuku (von einem Anbieter, an dessen Namen sich Jens im Gespräch selbst erst erinnern muss) auf, der eigene Rekord-Benchmarks für sich beansprucht.

Direkt anschließend an die Loop-Engineering-Folge der Vorwoche geht es um die praktischen Grenzen von Loops: Jens berichtet von einer mehrtägigen Sperre bei Anthropic, nachdem er sein Wochenlimit im Max-Plan an einem einzigen Abend verbraucht hatte. Noch tückischer ist ein zweiter Fall: Trifft ein Loop mitten in der Arbeit auf ein API-Limit statt ein Modell-Limit, bricht er zwar ab, meldet sich aber nach einem einfachen "mach weiter" so zurück, als sei alles erledigt, samt der beiläufigen Bemerkung, es habe acht Abstürze gegeben, die man reparieren solle. Am Ende steht ein Ergebnis, das aussieht wie ein normaler Prompt, nicht wie die eigentlich gewünschte gründliche Iteration. Der Aufruf der Folge: weg vom reinen Prompt Engineering, hin zum Loop-Ingenieur.

Zum Schluss ordnen die beiden ein, wie früh diese Phase der KI-Entwicklung eigentlich noch ist, vergleichbar mit dem Internet um 1997: vieles funktioniert schon, aber es gibt noch keine etablierten Standards, dafür aber schon die ersten Kurs-Verkäufer, die das große Geld versprechen. Ein Streitpunkt dabei sind Commodity-Harnesses wie ChatGPT, Gemini oder Anthropics Cowork gegenüber dem eigenen, selbstgebauten Agent Harness, der mit ständig wechselnden Modellen und Umgebungen klarkommen muss. Mark erzählt von jemandem, der sein selbstgebautes Harness-Ergebnis als "so eine JSON-App" abgetan hat, ein Anlass für eine eigene, ausführlichere Harness-Engineering-Folge, die die beiden ankündigen. Trotz aller Rückschläge bleiben Mark und Jens optimistisch: Sie vergleichen die aktuelle Phase mit dem iPhone-Moment, nach dem erst Anwendungen wie WhatsApp entstanden sind, die vorher niemand kommen sah, und erwarten Ähnliches für spontan generierte Software statt fertig gekaufter Programme.

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** Hadi zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:33]** Herzlich willkommen bei Think Different, Think AI.

**[00:00:37]** Jens und ich haben uns mal wieder persönlich getroffen.

**[00:00:40]** Leider nicht in so einer schönen Hotel-Lobby wie beim letzten Mal.

**[00:00:43]** Aber nichtsdestotrotz mit einem kühlen Getränk nach den heißen Tagen in der Hand.

**[00:00:47]** Und wir haben für uns festgestellt,

**[00:00:49]** dass die letzte Folge, die wir aufgenommen haben,

**[00:00:52]** die ihr letzte Woche hören konntet,

**[00:00:54]** so aktuell ist, dass wir da noch mal drauf aufsatteln mussten. Jens, wir haben das letzte Mal über solche

**[00:01:02]** Dinge gesprochen, wie Prompting, Skills, Loops und in der Folge davor hatten wir irgendwann

**[00:01:08]** auch mal über Favel 5 gesprochen und jetzt haben wir uns gesagt, das hängt alles irgendwie

**[00:01:12]** zusammen. Was ist denn seitdem nicht passiert, oder passiert? Ja, natürlich haben wir diese,

**[00:01:21]** Wir haben die Loopfolge aufgenommen und ich glaube, das passt ganz gut, dass wir jetzt

**[00:01:24]** nochmal diese aktuellen Ergänzung zu dieser Loopfolge machen, weil der Hörer unter euch

**[00:01:29]** und der KI-Begeisterte, so wie wir das sind, hat es beschämt, der mitbekommen.

**[00:01:34]** Fabel hatte, oder Atrophic wurde ja mit Fabel ganz bekannt vor ein paar Tagen, dann ist

**[00:01:40]** es abgeschaltet worden, haben wir eine ganze Folge drüber gemacht, das kennt ihr bestimmt

**[00:01:43]** das Thema.

**[00:01:44]** Jetzt ist dieses Wochenende auch wieder, solche Sachen passieren anscheinend immer

**[00:01:48]** am Wochenende.

**[00:01:49]** Und es hat nichts mit VW oder BSF zu tun.

**[00:01:52]** Nein, es sind aber vorhandene Geschichten.

**[00:01:54]** Anscheinend, wo dann Sachen aus Amerika hier rüber schwappen und entschieden werden.

**[00:01:57]** Es ist nämlich ein weiteres Modell,

**[00:02:00]** einmal wieder freigeschaltet worden,

**[00:02:03]** und ein anderes Modell hat aber angekündigt, dass Sie Ihr Modell,

**[00:02:06]** das Sie geplant haben, so wie die sind, wenn ich es richtig bin,

**[00:02:08]** das von OpenAI, das ist dann die 5.5 gewesen, die eigentlich geauscht hat.

**[00:02:13]** Nee, 5.6, 5.6 gibt es.

**[00:02:15]** Ist total lustig, ne, weil der eine kriegt einen Anruf,

**[00:02:18]** dass er doch bitte sein Modell noch ein bisschen zurückhalten soll und nicht erst

**[00:02:21]** releasen soll nach dem Motto, du willst doch nicht, das heißt bei dir, was passiert.

**[00:02:25]** Und der andere hat Fable 5 veröffentlicht.

**[00:02:28]** Anders als wir das wir bis jetzt kennengenannt haben, die ganze Situation mit

**[00:02:32]** rund um KI, dass die Sachen eigentlich mal fröhlich in die Welt gepostet worden sind,

**[00:02:36]** scheinen wir jetzt in eine neue Phase zu kommen.

**[00:02:40]** Was für die Qualität der Modelle natürlich einmal spricht.

**[00:02:42]** Diese Modelle sind, sie stetig dran weiterzuentwickeln.

**[00:02:46]** Das heißt, sie werden immer besser, dementsprechend natürlich auch immer gefährlicher, da entgegen,

**[00:02:53]** dass sie uns in vielen Fähigkeiten übertreffen und vor allem anstand jetzt bei Fähigkeiten,

**[00:02:58]** die wir früher gezeigt haben, wir dachten, wir haben was gut programmiert, wir haben

**[00:03:00]** was sicher programmiert früher.

**[00:03:02]** Jetzt kommen die Dinger um die Ecke und entdecken relativ zügig, dass dem nicht so ist, ja,

**[00:03:06]** dass wir gottgleichen Programmierer, die wir früher waren, doch nicht so fehlerfrei

**[00:03:10]** Fehler frei. Genau, Fehler frei, bis jetzt doch nicht so Fehler frei waren und dementsprechend, da irgendwo relativ viele Sicherheitslücken sind, die durch diese neuen Modelle in einer Windeseile geknackt werden.

**[00:03:22]** Ich glaube, irgendwie auch die Regierung hat auch gesagt, die amerikanische Regierung, dass auch ihre Systeme von Mythos in wenigen Stunden geknackt worden sind.

**[00:03:29]** Das ist also wirklich eine Bandbreite, die durchaus eine Regulatorik erfordert.

**[00:03:34]** Aber auf der anderen Seite natürlich auch ein bisschen Zeit, wie abhängig wir mittlerweile auch da sind.

**[00:03:40]** Ich meine, treue, hörende unseres Podcasts haben wir sicherlich auch mitbekommen.

**[00:03:45]** Es gibt nicht nur die amerikanischen Modelle, es gibt auch beispielsweise kinesische Modelle.

**[00:03:51]** Ja, jetzt wollen wir mal hier die französische Modell mit Ralf jetzt mal aus dem Vorlassen bei der Erklärung

**[00:03:58]** und das jetzt, dass wir eine Unterstellung oder sowas sein sollen.

**[00:04:02]** Aber auch die chinesische Modelle werden wahrscheinlich merken, was jetzt hier los ist, weil das ein

**[00:04:07]** oder andere Modell hat man zumindest mal so gelesen oder gehört, ist durch Distillation

**[00:04:13]** der großen Modelle entstanden.

**[00:04:15]** Also man muss sich das quasi so vorstellen, dass Anbieter, sagen wir mal so, viele Anfragen

**[00:04:21]** und Gespräche mit den US-amerikanischen Modellen geführt haben automatisiert, um

**[00:04:26]** diese Modelle quasi nachzubauen und nachzubilden.

**[00:04:29]** Sondern Art-Ree-Ingenierungen.

**[00:04:31]** Sie haben tatsächlich geprozbt, geguckt, dass du sagst, ich stelle 100.000 Anfragen

**[00:04:35]** zu dem Thema, wie geht man am besten angeln, dann antworten diese Modelle ja auch in 100.000

**[00:04:43]** Varianten, die aber sehr ähnlich sind.

**[00:04:45]** Damit im Prinzip die richtige Anleitung rauskommt, dass ich eine Angel mitnehme oder irgendwas

**[00:04:47]** anderes und den Köder und was auch immer.

**[00:04:51]** Und eine Dynamit steigen, da hat man so viele Filme gesehen.

**[00:04:53]** Und aus dieser, also diese, mit einer gewissen Wahrscheinlichkeit, denn wir

**[00:04:56]** Ich kenne ja alle das Thema, dass da Wahrscheinlichkeitsrechnung im Mittehrund passiert, die Token Prediction.

**[00:05:01]** Und um die wieder rauszukriegen, wurden ganz, ganz viele Anfragen an diese amerikanischen Modelle gestellt.

**[00:05:06]** Und so hat man im Prinzip dann verstanden, wie dieses Modell funktioniert und das danach gebaut.

**[00:05:11]** Da gab es in Geschichten, dass einige von den chinesischen Modellen so aufgesetzt sind.

**[00:05:15]** Und was ich halt auch ganz lustig fand, ist das andere, dass es Augenscheimi sogar schon Firmen gibt, die vor Gericht ziehen,

**[00:05:23]** Weil die unmittelbar nach Erscheinen von Fabel das Potenzial erkannt hatten und ihre Geschäftsprozesse

**[00:05:32]** schon darauf optimiert haben und gesagt haben, das ist quasi ein Modell, dass so gut es in

**[00:05:37]** der Textanalyse, ich glaube das war ein Zuckeranwält, so gut war in der Textanalyse, dass sie da

**[00:05:43]** keinen nicht mehr darauf verzichten wollte, haben alles darauf umgestellt und dann ist

**[00:05:46]** natürlich doppelt ärgerlich, wenn dann mal auf einmal es heißt, so, wir stellen

**[00:05:51]** das Modell ein, wobei fairerweise muss man sagen, das Modell wurde ja offiziell nicht eingestellt

**[00:05:56]** von der US-Regierung. Die haben ja nur gesagt, ihr müsst dich erstellen, dass das nur US-amerikanische

**[00:06:00]** Bürger benutzen. Das ist halt natürlich ein bisschen schwer in Zeiten von Amazon-Badrock-Zugängen,

**[00:06:05]** APKs und hast nicht gesehen. Also haben sie es generell abgeschaltet. Aber dann

**[00:06:09]** steht es da, als Firma. Und da steht sich auch so ein bisschen der Kreis zu dieser

**[00:06:13]** Loopfolge. Wenn du versuchst immer bleeding edge vorne mit dabei zu sein, dann

**[00:06:18]** kannst du nicht nur auf die Nase fallen, weil, naja, du gehst halt in Neuland und verursacht

**[00:06:23]** entweder Kosten oder musst lernen, damit umzugehen.

**[00:06:26]** Nie!

**[00:06:27]** Es kann sogar noch sein, dass dein Geschäftsprozess danach steht, weil das Modell abgeschallt.

**[00:06:32]** Hier nochmal ein guter Punkt, weil das war mir gar nicht so bewusst, dass es mir jetzt

**[00:06:35]** klar, erst ein Tag geworden, als du geredet hast.

**[00:06:37]** Auch andere Modellambiter, ob durch Destination oder durch eigene Modellentwicklung, werden

**[00:06:41]** höchstwahrscheinlich auf den Status kommen, den wir jetzt bei den großen Modellen

**[00:06:45]** haben.

**[00:06:46]** schön mit wie viel Überlegung du hier reingehst und sagst du es amerikanische

**[00:06:52]** Regierung hat wie immer sehr ausführlich über nachgedacht. Was ich

**[00:06:57]** daran ganz lustig fand, Mythos als Mythos erschien und es noch hieß, es ist nur

**[00:07:02]** ein sehr eingeschränkt Benutzerkreis zur Verfügung, hatten wir auch im Podcast

**[00:07:06]** vom Bericht, war es ja auch als Modell gelistet bei Amazon Badrock in der EU-Zone, in

**[00:07:13]** Frankfurt, wo ich mir dann auch dachte, hey, wenn es doch dieses ominöse Superduper und

**[00:07:18]** ich breche aus allem Ausmodell ist, ob jetzt die Eurozone Frankfurt bei Bad Rock so der

**[00:07:23]** beste Platz ist. Dafür weiß ich nicht. Müssen wir gleich gucken, ob das noch da ist. Ja,

**[00:07:29]** tschuldigung. Aber weißt du noch, wie dieses Modell heißt, dass jetzt rausgekommen ist,

**[00:07:33]** dass so ein bisschen heißt, es hätte Fable 5 möglichkeiten, weil es ist kein Modell,

**[00:07:40]** ist es mehr so ein Orchestrator. Ja, ja, das ist japanische, aber komme ich jetzt auf die Namen,

**[00:07:44]** ich glaube irgendwas mit Fuku, ich muss es leider nachrufen vielleicht. Ja, ja, also ich weiß ganz

**[00:07:50]** ehrlicherweise, ich habe auch keine Ahnung, wie es heißt, vielleicht fällt es uns ja auch gleich,

**[00:07:54]** wir werden reden einem bestimmt. Das fand ich halt auch ganz lustig, wie auf einmal Modelle

**[00:07:58]** aus dem Boden sprießen bzw. Verfahren aus dem Boden sprießen, die von sich behaupten,

**[00:08:04]** die Benchmarks zu schlagen, die diese Großmodelle für ein paar Tage dargeboten haben und von

**[00:08:14]** der Seite, es geht mir gerne, wie heißt es? Schalkana, AI, Fuku. Ja, darum weiß ich ja,

**[00:08:21]** dass ich den Podcast immer sehr gerne mit dir mache, weil du bist halt so der Gebildete. Ja,

**[00:08:27]** aber das ist gerne nochmal einmal zu dem Thema, das ich gerade kurz angestätten hatte mit dem

**[00:08:31]** Looping, weil wir ja auch ein bisschen Loops gerätet haben.

**[00:08:35]** Looping, ja, das machen wir Loops, dann haben wir Looping.

**[00:08:38]** Looping.

**[00:08:39]** Er merkt es euch schon mal.

**[00:08:40]** Genau.

**[00:08:41]** Ja, das hat natürlich, das ist gerade schon deutlich, das Konsequenzen, über die man sich

**[00:08:45]** jetzt gebacken machen muss, wenn wir, wie wir das Polen eingeführt haben, in einer

**[00:08:49]** Welt sind, wo ich nicht mehr sicher sein kann, dass ein großes Modell, das draußen

**[00:08:56]** veröffentlicht wird, noch am Markt ist, wenn ich morgens wieder aufwache.

**[00:09:00]** Also diese schöne Storyline, ich setze hier mal ein Loop auf und vielleicht davon hunderte,

**[00:09:05]** also das hören wir ja auch immer, wenn wir sich dagegen gucken, kaum eine der großen Modelle

**[00:09:10]** wird überhaupt noch von Programmierern programmiert, das wird auch nur noch gelubt, also viele

**[00:09:14]** von den großen AI-Programmierern und Größen, die in den Modellfirmen sitzen, sagen, wir

**[00:09:20]** machen das gar nicht mehr selber, ich bin nur noch quasi dafür da, um Loops zu bauen.

**[00:09:25]** So, wenn aber der wesentliche Teil eines Loupes dann verschwindet, sprich das KI-Modell im Hintergrund,

**[00:09:32]** ja dann sind deine Loups auch einfach nur noch für ein Arsch, ehrlicherweise,

**[00:09:35]** aber da kommen sie nicht mehr weiter.

**[00:09:36]** Also dementsprechend müssen wir, muss jeder sich, glaube ich, da Gedanken drüber machen.

**[00:09:40]** Und wir haben da ja häufig schon mal darüber geredet, also das Thema Harnes Engineering,

**[00:09:44]** wie baue ich dann im Prinzip mein ganzes KI-Setup auf, wie ist meine KI-Architektur eigentlich?

**[00:09:49]** Da muss man diesen zwei, drei Millisekunden vielleicht länger drüber nachdenken und nicht

**[00:09:54]** nur prompten, was man da machen könnte, damit man im Prinzip ein System aufbaut, was dann

**[00:09:58]** eben auch robust ist und auch solche Ausfälle im Notfall dann verhindern oder vermeiden

**[00:10:04]** kann oder wenigstens dahingehend abfangen kann, dass es nicht so kritischen Situationen

**[00:10:08]** irgendwo führt.

**[00:10:09]** Da wäre ich mir ein anderes Ding auch noch reingefallen, was bei Loops auf die Bretter

**[00:10:14]** gehen kann.

**[00:10:15]** Wenn man mir so folgt, wird man gesehen haben, dass ich letztens wieder zwangsgesperrt wurde, weil ich die ganzen Tokens, die mir enttropik im großen Max-Plans befürchtet.

**[00:10:27]** Na ja, nee, aber ich wurde irgendwie für mehrere Tage gebannt, weil ich meinen Wochenlimit verbraucht habe.

**[00:10:34]** Man sollte halt diese fees-workflow-slashcode.

**[00:10:39]** Das ist das eine okay fairer Punkt, wenn die Modelle an token limits kommen, sofern man

**[00:10:47]** nicht pay per use hat, ist das eine oder das andere, was mir beaufgefallen war, was bei

**[00:10:52]** meinen Versuchen mit Loops zu arbeiten mir aufgefallen ist.

**[00:10:57]** Du gibst dem System große Mengen an Daten und sagst, mach deine Loops da drüber.

**[00:11:02]** Wenn du da nicht von vornherein darauf achtest, dass beispielsweise Textblöcke ausreichend

**[00:11:11]** groß oder klein sind, wobei ausreichend groß oder klein ist, ist extra schwammig gewählt,

**[00:11:15]** weil ich nicht weiß, was groß oder klein ist, aber ihr werdet gleich merken, worauf

**[00:11:18]** ihr raus will.

**[00:11:19]** Ich habe dem Ding nämlich gesagt, du pass mal auf, hier große Bücher, lefräst dich

**[00:11:23]** mal durch und werte mir folgende Sachen aus, mach das bitte mit einem Goal Loop,

**[00:11:28]** also mache so lange, bis folgende Fragen beantwortet sind und auf einmal ist alles

**[00:11:32]** abgebrochen. Alles ins Nirwana geschossen. Es stand in gelber Schrift auf dem Bildschirm.

**[00:11:37]** AP Limit Reached, klammer auf. Es handelt sich nicht um das Modell Limit, sondern du hast

**[00:11:44]** schlicht und ergreifend die API bombardiert. Wir machen nicht weiter. So, dann sagst du zu ihm,

**[00:11:49]** mach weiter. Und dann sagt er, oh ja, total toll. Du, ich setze es fort, blablabla. Er hat dann

**[00:11:55]** wieder gearbeitet, wieder fehler. Irgendwann hat er gemerkt, oh du, ich sollte vielleicht meine

**[00:11:58]** Abfragen reduzieren, damit das nicht gegen das Limit läuft und ganz, ganz, ganz am Schluss sagt er,

**[00:12:04]** du bist mit allem fertig. Auch übrigens, wir hatten acht Abstürze. Soll ich das reparieren,

**[00:12:08]** was dabei kaputt gegangen ist und du denkst ja so, okay, der Go-Loop ist gebrochen,

**[00:12:14]** dann musst du ständig sagen weiter und das Ergebnis war so wie, als wenn ich einen normalen

**[00:12:19]** Prompt geschrieben hätte, alles, was ich so an überprüft dich und stell sicher und das sind

**[00:12:25]** die KPIs. Das hat er alles über den Äther geschoben für diese Abbruchmomente.

**[00:12:30]** Ja. Also da habe ich auch gedacht, da brauche ich nicht mal eine amerikanische Regierung,

**[00:12:34]** die mehr modern abschaltet. Da reicht auch mal eine eigene Unfähigkeit und ich rufe damit auf,

**[00:12:38]** nicht mehr zum Prompt-Engineering, sondern zum Loop-Engineer. Ja, aber der Loop-Engineer,

**[00:12:45]** das ist glaube ich ein Sonderpunkt, wir müssen glaube ich bei diesem ganzen KI-Hab-Thema und

**[00:12:50]** wir beide sind ja auch immer durchaus ganz vorne dabei, wenn wir mit Begrifflichkeit

**[00:12:53]** um uns herumwerfen, dann werden wir mit neuen Themen um die Ecke kommen. Ich glaube, die

**[00:12:58]** Erfahrung der letzten zwei, drei Jahre jetzt mit den Themen zeigt einfach, wir sind alle

**[00:13:04]** noch früh dabei. Alle Sachen entstehen gerade relativ neu. Das heißt, es gibt noch nicht

**[00:13:12]** die optimale Loop Engineering-Schule, die ihr sagt, wenn du das so machst, dann läuft

**[00:13:18]** das auch noch.

**[00:13:19]** Es gibt bestimmt einen Influencer, der dir das für einen Kurs vergrößt.

**[00:13:21]** Genau, auf jeden Fall. Damit kannst du auch in die Millionen sofort verdienen, wenn du das machst.

**[00:13:26]** Jeder, der schon mal versucht hat, ein Workflow mit, lasst es nur zwei KI-Mutellen hintereinander aufzubauen.

**[00:13:33]** Der wird merken, dass er immer wieder nacharbeiten muss.

**[00:13:36]** Es gibt immer diese Stellen, wo wir momentan nacharbeiten, wo wir der berühmte Mensch immer den Belup sein müssen,

**[00:13:42]** der eben noch nicht einfach nur On-Belup sein kann und irgendwie auf seiner Ascienda sitzen kann

**[00:13:47]** und den Sonnenschein genießen kann und die Kojoten zählen möchte.

**[00:13:50]** Ne, wir müssen halt immer noch nach unbestimmter Zeit, das wissen wir nicht ganz genau, wie

**[00:13:56]** da vorbei ist auch unsere Temporary-Exfolge auch, die wir mal gemacht haben.

**[00:13:59]** Wir wissen auch nicht hundertprozentig genau, wann wir eigentlich wieder eingreifen müssen,

**[00:14:02]** vielleicht eben eine Notification, die angenehm ist, die sagt der Loop ist fertig oder eben

**[00:14:07]** so wie du es gerade beschrieben hast, die sagt, hm, hier ist ein Grupp eben.

**[00:14:10]** Hier brennt alle.

**[00:14:11]** Alle brennt alle.

**[00:14:12]** Einmal kurz, kurz, kurz.

**[00:14:13]** Könntest du mal kurz kommen, ja?

**[00:14:14]** Also das heißt, ja, also wenn man Sachen gerade machen will, dann muss man auch

**[00:14:18]** fast gefühlt in so einer 24-7 Bereitschaft sein, wenn man das jetzt auch auf kritisches Systemen

**[00:14:24]** loslassen würde. Wenn ich jetzt da irgendwie so ein Buchprojekt habe, ja, was anderes, dann

**[00:14:28]** ist es nicht so schlimm, wenn man da mal am Wochenende vielleicht das Ding nochmal nachstartet

**[00:14:31]** oder sowas. Aber bei allen anderen Themen sind wir, glaube ich, so weit, dass man sagen muss,

**[00:14:38]** bisschen Dinge drüber nachdenken, bisschen aus einer ITG-Perspektive die Sachen betrachten,

**[00:14:43]** Was wir vorhin gesagt haben, versuchen robust aufzubauen, vielleicht nicht direkt den Loop

**[00:14:49]** einfach großlaufen Sachen, sondern ist auch da, wie dann nochmal den kleinen Teil kleiner

**[00:14:53]** schneiden, überwachbar machen, überprüfbar machen lassen, dass man schaut, was kann

**[00:14:59]** da gehen.

**[00:15:00]** Und ich glaube, das ist so ein bisschen das, was ich zurzeit mitnehme aus dieser KI-Phase,

**[00:15:04]** die wir sind, jetzt ohne irgendwie so ein Gartner-Halbzeig, da nämlich Erfolg zu

**[00:15:09]** kramen.

**[00:15:10]** Aber ich glaube, wir sind jetzt so ein bisschen...

**[00:15:11]** Im Teil der Tränen?

**[00:15:12]** Ja, Teil der Tränen weiß ich gar nicht.

**[00:15:13]** Also so fühlt es sich nicht an.

**[00:15:14]** Das bin ich schon ein paar Mal durchlaufen.

**[00:15:15]** Sowohl liebster als auch privat.

**[00:15:18]** Ich glaube, das bin ich schon beim Promt-Engineering und beim Look-Engineering und bei allen anderen

**[00:15:22]** Sachen immer wieder durchlaufen und auch wieder in den Halb-Cycle hochgegangen und so was.

**[00:15:25]** Ich glaube, es ist tatsächlich eher so, dass wir schon auf diesem Weg in die Richtung des Plattforms

**[00:15:30]** der Produktivität sind.

**[00:15:31]** Da fehlen aber einfach Sachen.

**[00:15:33]** Wir hatten jetzt vor kurzem ja drüber geredet.

**[00:15:35]** Wir sind so wie 97 oder sowas.

**[00:15:36]** Weißt du, das Internet ist da, Sachen funktionieren, Webseiten sind generell da.

**[00:15:40]** Google hat sich aber noch nicht ausgeprägt, große Usability, Geschichten sind noch nicht

**[00:15:46]** ausbrücht und wissen noch nicht, wo am besten eine Navigation untergebracht wird oder so

**[00:15:49]** was.

**[00:15:50]** Wir probieren an vielen Stellen noch aus, das führt zu coolen kreativen Ergebnissen

**[00:15:55]** ehrlicherweise.

**[00:15:56]** Also es gibt ja so viel heißen Scheiß, der draußen gemacht wird mit KI auch, wo Sachen

**[00:16:00]** gerennert werden, Animationen gemacht werden, Info-Webseiten gebaut werden, die bei uns

**[00:16:05]** hinter früher hätten nicht so vorstellen können in einer Geschwindigkeit, wie das

**[00:16:08]** gemacht wird.

**[00:16:09]** viele kreative Themen gerade gemacht. Es werden Loop aufgesetzt, es werden Marketing-Systeme

**[00:16:14]** automatisiert, es werden Programmschmieden gebaut. Alle anderen vielen Stellen gehen Sachen

**[00:16:19]** schon, aber es ist nicht so, dass man es 1 zu 1 kopieren kann. Also wir haben noch nicht

**[00:16:24]** dieses, es gibt eine Amazon und ich kann ein Zahlander daraus bauen. Also dieser Moment

**[00:16:28]** ist noch nicht da, weil du kannst es noch nicht so 1 zu 1 rüber kopieren. Ich glaube

**[00:16:31]** wir sind in seiner frühen Phase, das Internet ist tatsächlich gerade.

**[00:16:34]** Das merkt man auch an einem anderen Thema, nämlich wir hatten ja jetzt heute ein bisschen

**[00:16:39]** so den Abbinder über Modelle, die auf einmal wegbrechen können.

**[00:16:43]** Dann haben wir von Skills und Loops als Fortlet zum Gesprachen und ihr habt ja auch bestimmt

**[00:16:47]** den anderen Folgen von so mal das Thema Agent Harness gehört und am Ende vom Tag läuft

**[00:16:52]** es ja gefühlt immer wieder darauf hinaus, dass du heute viel Comedy Harnesses findest,

**[00:16:58]** Du hast einen Chat-TBT, du hast einen Gemini, du hast den nächsten Siri AI, du hast von

**[00:17:05]** Antropi Cross Co-Work, aber so dieses ganze Thema, wie bespiele ich den Dienstecheneinsatz,

**[00:17:10]** wie bespiele ich den Wissenschaftler, wie bespiele ich den professionellen Menschen,

**[00:17:15]** der mit diesen Werkzeugen versucht, Mehrwert zu schaffen, ohne, ja, installe ich mir heute

**[00:17:21]** Open AI, mache ich morgen das nächste Abo, das nächste Abo, das nächste Abo oder installe

**[00:17:26]** mir hier Open Code von GitHub oder keine Ahnung, oder setze ich mich vielleicht sogar hin und

**[00:17:32]** baue den eigenen Harnis und dann wird es richtig lustig, wenn sich diese Umgebungen ständig

**[00:17:38]** ändern. Du aber auf der anderen Seite etwas baust, dass diese ständige Veränderung der

**[00:17:42]** Umgebung ja abfangen will, dafür sorgen will, dass du produktiv arbeiten kannst, Ruhe ins System

**[00:17:48]** bringst, Modelle austauschbar, trotzdem Skills, funktionsfähig, standardisierte Loops,

**[00:17:54]** ohne dass der Anwender es extra sagen muss.

**[00:17:56]** Wie präsentiere ich es meinem Anwender?

**[00:17:58]** Ich hatte letztens jemanden dazu mir gesagt, du mag toller Agent Harness, den du da gebaut hast.

**[00:18:03]** Aber der sagt mir immer, ich hätte so eine JSON-App.

**[00:18:08]** Ja, da fehlen mir dann auch, was will denn die Person?

**[00:18:11]** Na ja gut, der stand halt da, JSON generiert.

**[00:18:13]** Dabei hätte, also wie spreche ich mit meinem Anwender?

**[00:18:16]** Dass du auch da so ein breites Fell, wo ich dann noch mit der Frage,

**[00:18:20]** Wie machst du da Betrieb in einer Welt, wo quasi alle drei Tage neue Modelle, neue Techniken, neue Kanäle, keine Ahnung, was rauskommen und verboten werden?

**[00:18:27]** Rauskommen und verboten werden?

**[00:18:29]** Oh ja, wenn mein Harnis mal verboten wird, dann wär's da berühmt.

**[00:18:32]** Also an der Stelle, ja, fürs Marketing wär's gut.

**[00:18:36]** Aber ich glaub Agent Harnis wär auch nochmal ne Folge, wir haben ja schon lange nicht mehr Folgen angekündigt.

**[00:18:41]** Ach ja, wer weiß, also ihr könnt gerne...

**[00:18:43]** Ja, aber auf jeden Fall eine Harnis Engineering-Folge.

**[00:18:45]** Eine Harnis Engineering-Folge, ja, freu ich mich drauf.

**[00:18:48]** Ja, aber ansonsten, wie gesagt, ich mit Blick auf die Uhr und der Bahn in deinem Nacken ist die,

**[00:18:55]** also ich habe es ja gerade so gesagt, dass wir uns auf das Plateau der Produktivität bewegen,

**[00:19:00]** dass es in diesem Gardner-Hype-Seikel, das ist dann diese Phase, wo alles dann eben

**[00:19:04]** gut funktioniert, dass man aus dieser Superhype-Phase raus ist, aus dem Tal der Tränen

**[00:19:08]** raus ist und dass man jetzt weitergeht.

**[00:19:10]** Ich glaube, dieser Weg ist momentan bei KI so schnell, dass man da dieses Produktivitäts-Platot schon sieht.

**[00:19:19]** Der Weg wird aber noch ein bisschen steinig werden.

**[00:19:21]** Ich glaube, der wird noch einige Bands auf dem Weg haben, einige Harnisse werden brechen, einige Loops werden unentdeckend hoffen, in die falsche Loopings machen.

**[00:19:32]** Und da ist, glaube ich, da wird noch viel passieren, bevor wir vielleicht so etwas haben, wie wir das früher hatten,

**[00:19:39]** dass dann so ein stabiles Internet, das alle Leute benutzen können,

**[00:19:43]** dass der Gemeinheit dann auch zur Verfügung steht.

**[00:19:47]** Das wird noch ein bisschen dauern, glaube ich, tatsächlich, dass wir das überall durchgängig haben werden.

**[00:19:52]** Aber nicht so trotz will ich, wie immer, positiv enden wollen.

**[00:19:55]** Ich freue mich drauf, weil auch da werden sich ja ganz neue Sachen noch ausbringen, die dem auch gar nicht kennen.

**[00:20:01]** Also wenn ihr jetzt an den iPhone-Moment denkt, welchen Software danach entstandet, welcher

**[00:20:07]** Interaktionsmöglichkeiten danach entstanden, sowas wie WhatsApp und Co. dieses Verabreden

**[00:20:11]** und solche Sachen.

**[00:20:12]** All das ist erst entstanden, als diese Technologie da war.

**[00:20:14]** Und wir sind jetzt, glaube ich, noch in so einer Situation, wo noch ganz viele neue

**[00:20:18]** Technologie, ganz viele neue Use-Cases für uns eigentlich erst kommen werden, an

**[00:20:23]** die wir heute noch gar nicht denken, die einfach dann, weißt du so, Software,

**[00:20:27]** die ich on-the-fly generiere, weil ich jedenfalls kein Grafikprogramm mehr von der

**[00:20:31]** Stangen kaufen muss, sondern mit der Grafik bekommen, dass ich in dem Moment brauche, einfach

**[00:20:35]** generiere. Man sieht man heute immer mehr, dass Leute sagen, oh, ich habe mir den PDF-Smallmacher

**[00:20:41]** irgendwie gebaut oder irgendwas anderes mit den PDFs gemacht und einen Splucking gebaut

**[00:20:46]** und sowas liest man da ab und so. Ich glaube, da werden noch viele, viele coole Sachen passieren.

**[00:20:49]** Aber das wird bestimmt alles geil und ich habe während du gesprochen hast eine

**[00:20:54]** Geschäftsidee. Oh, jetzt bin ich gespannt. Sollen wir stoppen oder wollen wir zu den

**[00:20:57]** Nein, nein, die möchte ich natürlich mit meinen Hörern teilen, das ist auch ein bisschen, ich weiß nicht.

**[00:21:02]** Stell dir mal vor, das Thema würde jetzt doch Fahrt aufnehmen, dass Modelle immer erst mal in Amerika verfügbar sind oder in China,

**[00:21:09]** weil, ich meine, da gibt es ja auch sowas wie Exportkontroll, ne?

**[00:21:12]** Vielleicht auch in Europa, ja, wir drücken uns allen die Daumen.

**[00:21:15]** So, jetzt stell dir einfach mal vor, wo das würde kommen.

**[00:21:17]** Ich habe so Erinnerungen, an ganz alte Zeiten, also immer nur von Hörern sagen, ne?

**[00:21:21]** Pirate Bay und wie die Alice Napster. Ich habe irgendwie so das komische Gefühl, irgendwann

**[00:21:26]** sehen wir Menschen, die wohnen dann irgendwie in den besagten Ländern, sind Landesbürger

**[00:21:30]** und stellen sich irgendwelche Rex-Systeme in Schrank und ruten quasi ihren persönlichen,

**[00:21:36]** also nicht quasi als persönlichen, aber denen durch ihren staatsmännischen Zugang, ob

**[00:21:41]** das dann legal ist, wahrscheinlich nicht, weil du ja damit Exportkontrollen und Gehsabt,

**[00:21:44]** ich könnte mir vorstellen, dass so etwas auch mal gebaut wird, dann müssen wir

**[00:21:47]** Thomas fragt mit seinem Ford-GPT und so.

**[00:21:49]** Vielleicht gibt es da schon was.

**[00:21:51]** Thomas, falls du etwas hörst, wir müssen reden.

**[00:21:53]** Da hat man schmuggelt das Modell quasi lokal auf seiner Feste.

**[00:21:56]** Ich trug es auf Papier.

**[00:21:57]** So wie KGB.

**[00:21:58]** Ausgedrucktes Modell, wird bestimmt lustig.

**[00:22:01]** Von der Seite, heute war ein buntes Potpourri an den verschiedensten Dingen der Jens eilt

**[00:22:07]** jetzt zu seiner Bahn, die aufgrund ihrer klassischen Verspätung rechtzeitig ist,

**[00:22:12]** wenn er so lang kommt.

**[00:22:13]** Wir wünschen euch eine gute Zeit und freut euch drauf.

**[00:22:16]** Bald wieder Gäste und schalte wieder ein, wenn es heißt Think Different.

**[00:22:19]** Think AI. Ciao.

**[00:22:23]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:22:28]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden,

**[00:22:33]** sondern sie leben.

**[00:22:35]** Hier gibt es klare Einordnungen, echte Praxiseinblicke

**[00:22:39]** und einen frischen Blick auf das, was möglich ist.

**[00:22:41]** Verständlich, kritisch und immer mit einem Auge zwingt.

**[00:22:46]** zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
