---
title: "Wie KI unser Arbeitsleben verändert!"
episode_index: 27
published: "Tue, 17 Feb 2026 09:28:10 +0000"
duration: "3195"
audio_url: "https://audio.podigee-cdn.net/2360415-m-6d3d5c3e28d769e1c76a37c25379928f.mp3?source=feed"
guid: "a16109cc4a10cc37c66b3c63c19b2f4e"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-04-28T20:55:58+00:00"
---

# Wie KI unser Arbeitsleben verändert!

**Veröffentlicht:** Tue, 17 Feb 2026 09:28:10 +0000
**Dauer:** 3195
**Audio:** https://audio.podigee-cdn.net/2360415-m-6d3d5c3e28d769e1c76a37c25379928f.mp3?source=feed

## Beschreibung

Wie Künstliche Intelligenz unsere Arbeitswelt und Softwareentwicklung auf den Kopf stellt. Zwischen Veränderungsdruck, Neugier und echter Praxis.
In dieser Folge spreche ich mit Klaus Rodewig LinkedIn und Alexander Heusingfeld LinkedIn darüber, wie Künstliche Intelligenz die Art und Weise verändert, wie wir Software entwickeln, testen und betreiben. Wir diskutieren, warum klassische Rollenbilder, gewohnte Programmiersprachen und liebgewonnene Prozesse plötzlich ins Wanken geraten – und was das für uns als Entwickler, Architekten und Entscheider bedeutet.

Gemeinsam blicken wir auf echte Aha-Momente, Hürden im Alltag und den rasanten Fortschritt von Tools wie OpenClaw und Craft-Agent. Wir fragen uns, wie wir als Menschen in dieser Geschwindigkeit mithalten, welche Fähigkeiten künftig zählen und warum lebenslanges Lernen jetzt eine neue Dimension bekommt. Wer wissen will, wie die Arbeit mit und in KI-Teams wirklich aussieht und welche Chancen und Herausforderungen auf uns warten, sollte reinhören.

Podcast
Conversations about Software Engineering

## Transkript

**[00:00:00]** Ein Disclaimer am Anfang. Alle Aussagen von mir und meiner Gäste sind unsere persönlichen

**[00:00:06]** Meinungen entsprechend nicht automatisch der Sicht unserer Arbeitgeber.

**[00:00:10]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens. Zwei technologieverliebte

**[00:00:20]** Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben. Hier gibt es klare

**[00:00:25]** Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:30]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:34]** KI zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:44]** Herzlich Willkommen zu einer neuen Folge von Think Different, Think AI.

**[00:00:48]** Heute sind wir ohne den Jens unterwegs.

**[00:00:51]** Der feiert nämlich, was? Fasching, Kölralaf, ach, ich bin Hesse, ich hab keine Ahnung.

**[00:00:57]** Aber jetzt sitze ich hier alleine, habe mir doch trotzdem noch Unterstützung geholt,

**[00:01:04]** nämlich nicht einen Gast, sondern gleich zwei. Den einen Gast, den hatten wir hier tatsächlich schon mal.

**[00:01:11]** Klaus Rodeweg ist nämlich heute wieder mit dabei und er wird begleitet von Alexander Häusingfeld.

**[00:01:19]** Und ich möchte euch einfach bitten, stellt euch kurz vor, wer seid ihr, was macht ihr und dann

**[00:01:25]** steigen wir doch einfach mal in das Thema ein, alles um das Thema Arbeitswelt im Umfeld von AI.

**[00:01:31]** Ja, ich bin Herr Klaus. Ich war glaube ich tatsächlich zwei, drei mal hier und ich kenne den Markt

**[00:01:39]** schon furchtbar lange. Das habe ich beim letzten Mal auch schon gesagt. Wir haben eine gemeinsame

**[00:01:43]** iOS-Vergangenheit, haben zusammen Vorträge gehalten und schlimme Apps verbrochen.

**[00:01:47]** Zusammen Vorträge halten hieß, er hat auf der Bühne gebastelt, während ich mir den

**[00:01:52]** Text habe einfallen lassen müssen, aber machen wir weiter.

**[00:01:56]** Das geht ja schon in agentisches Arbeiten, oder?

**[00:01:59]** Ist toll.

**[00:02:00]** So, und in meinem Beruf beschäftige ich mich mit Security und mit AI, da beides meiner Meinung

**[00:02:08]** nach untrennbar miteinander verbunden sind, d.h. von AI meine ich den Teil AI, Formats

**[00:02:16]** AI, Edit Development.

**[00:02:17]** Ich würde es jetzt nur noch als Genetic AI oder AI-Base-Developer nehmen, da man von Hilfe

**[00:02:26]** nicht mehr sprechen kann, sondern, und da werden wir wahrscheinlich heute drüber sprechen,

**[00:02:30]** die AI ganz signifikante Teile des Entwicklungsprozesses einfach mal schlichtweg übernehmen wird.

**[00:02:36]** Wir haben ja auch noch einen zweiten Gast in der Runde.

**[00:02:39]** Alex, magst du auch noch zwei, drei Sätze zu dir sagen?

**[00:02:41]** Ja, dann nochmal vielen Dank für die Einladung, lieber Mark.

**[00:02:46]** Alex Häusingfeldt, mein Name. Ich bin selber Podcaster im Conversations about Software Engineering Podcast.

**[00:02:53]** Und bin Klaus Kollege bei den, bei Vorwerk, früher auch bei den Elektro-Werken.

**[00:02:59]** Hab da die Cookie-Doo, die Rezeptplattform mit aufgebaut.

**[00:03:03]** Und davor war ich sehr viel im Bereich Software-Architektur, Consulting, Software-Entwicklung unterwegs.

**[00:03:09]** Und wir unterhalten uns hoffentlich heute ein bisschen über, wie sich Softwareentwicklung

**[00:03:14]** so verändert in den nächsten Monaten, oder wie sich auch in den letzten Monaten verändert hat.

**[00:03:18]** Jetzt ist Zeit für eine Werbeeinblendung, denn du hast ja den Namen unseres Arbeit genannt,

**[00:03:24]** der Vorwerk, der diesen schönen Thermomix herstellt.

**[00:03:27]** Und ich bin dafür verantwortlich, dass der Thermomix sicher ist und dass wir dich in

**[00:03:32]** Zukunft mit AI tun.

**[00:03:33]** Und ich hoffe, ihr habt alle einen Thermomix.

**[00:03:37]** Aber Mark, du wolltest was sagen.

**[00:03:39]** Ja, ich wollte gerade überlegen, ob ich jetzt, also eigentlich wollte ich ja dann noch Alex ein Podcast an die Show Notes packen.

**[00:03:45]** Vielleicht kriegen wir ja auch noch einen Link auf euren Shop, dann gleich damit, dass entsprechende Produkte erworben werden kann.

**[00:03:51]** Aber schauen wir mal, was trotz wird.

**[00:03:53]** Ihr hattet es ja schon angedeutet, nach dem Motto, wie verändert KI, das Arbeitsleben beziehungsweise das Leben derer,

**[00:04:00]** den mit IT viel zu tun haben, mit Blick auf Software-Entwickler.

**[00:04:05]** Wir hatten in der Vorbereitung so ein paar schöne Überschriften uns mal so zugeworfen,

**[00:04:11]** die wir als roten Faden durch unser heutiges Potpourri der Unterhaltung mitnehmen können.

**[00:04:17]** Da kam als allererstes für unseren Einstieg.

**[00:04:20]** Was, KI, da ändert sich was?

**[00:04:22]** Ne, also, ist das mal so gut, ist das, dass mir quasi

**[00:04:27]** sei es in der Softwareinfektion, sei es in der Infektion, sei es an welcher Stelle,

**[00:04:30]** wo auch immer mit Text gearbeitet wird, auch immer.

**[00:04:33]** Das ist doch alles nur Science-Fiction und Demo-Zeug und das funktioniert doch alles noch gar nicht

**[00:04:38]** so richtig.

**[00:04:39]** Kennt ihr das?

**[00:04:40]** Oder ist das bei euch natürlich in der Ausmöglichung, ist immer alles anders, ist auch klar.

**[00:04:44]** Aber jetzt mal Hand aus Herz, kennt ihr das oder wie sieht das aus?

**[00:04:48]** Ja, ich muss jetzt mal meinen Hut fressen, weil das ist noch gar nicht so lange her.

**[00:04:52]** Da habe ich mich insbesondere mit dem Alex in leidenschaftlich darüber gestritten,

**[00:04:58]** wie wir in Zukunft arbeiten werden und der Streit entbrannte an so simplen Dingen wie welche

**[00:05:04]** Metrik wollen wir eigentlich in Zukunft an unsere Softwareentwicklung hängen.

**[00:05:09]** Das war zu einer Zeit, wo ich intensiv mit GitHub Copilot gearbeitet habe und schon

**[00:05:14]** ziemlich geflasht war von dem, was da rauskommt.

**[00:05:16]** Aber mir noch nicht vorstellen konnte, dass das quasi eine Zäsur ist, die nicht nur

**[00:05:24]** das Programmieren selber, sondern die gesamten Entwicklungszyklus auf den Kopf stellt.

**[00:05:27]** Und jetzt habe ich die letzten Wochen sehr intensiv damit verbracht, mit Claude Code mich zu beschäftigen.

**[00:05:34]** Ich bin übrigens auch total begeistert von der Integration in Xcode 26.3 am Rande erwähnt.

**[00:05:42]** Und das war so ein Eye Opener Moment, wo mir klar wurde, okay, in Zukunft wählen wir

**[00:05:47]** nicht mehr Lines of Code oder als Testmessen, sondern wir werden einfach messen, wieviel

**[00:05:51]** Apps haut ein Mensch in der Woche noch raus.

**[00:05:53]** Und das ist, ja, ich kann das gut verstehen.

**[00:05:57]** Das gibt ja sowas. Manche Sachen muss man einfach mal gesehen haben oder den Schreer gehabt haben, um zu wissen, was die für den Trag weiterhaben.

**[00:06:05]** Ich meine, die beide seid ja quasi auch, ich sag mal, vorbelastet von meinen Wochenend Eskapaden, nicht weil ich irgendwie mit euch auf eine Besäufnestour gehe oder nicht, sondern weil ihr manchmal das ertragen müsst, wenn ich irgendwie auf irgendwas gestolpert bin und wir uns dann gegenseitig irgendwie in unserer kleinen Chatbubble

**[00:06:27]** Mit Informationen des Hochten habe ich einen Haken, das war es nicht weiter vor zwei Wochen oder Samstagabend, wo du uns beiden geschrieben hast,

**[00:06:35]** Boah, ich bin so sauer, ich schmeiß gleich mein Mac-Mini an die Wand.

**[00:06:39]** Ich wollte Open-Claw, da hieß der noch, wie hieß der denn noch?

**[00:06:42]** Open-Claw-Bot auf dem lokalen Modell umstellen und das Ding ist komplett kaputt gegangen.

**[00:06:47]** Ich gehe jetzt filmen gucken und nach einer Stunde hast du dann geschrieben, oh, er hat mir gerade eine WhatsApp-Nachricht geschrieben,

**[00:06:53]** dass ich ja wohl Feierabend gemacht habe, aber er alles retteriert hat für mich, wo ich denn sei.

**[00:06:59]** Ja, ich habe auch in der letzten Folge tatsächlich auch hier auf dem Kanal davon berichtet und das war Telegram und nicht WhatsApp.

**[00:07:05]** Ja, also ihr seid quasi im Guten wie im Schlechten, aber es ist doch auch Wahnsinn, wie schnell sich der ganze Kram gerade so dreht.

**[00:07:12]** Also wenn ich vor einem halben Jahr ein N8N gesessen habe, würde ich heute ehrlicherweise für N8N gar nicht mehr würfeln gehen.

**[00:07:21]** Ja, das ist irgendwie bei mir schon wieder vom Tisch irgendwie, keine Ahnung.

**[00:07:25]** Die Herausforderung, die ich halt sehe, ist, dass wir unsere Kollegen damit, glaube ich,

**[00:07:30]** auch zwischendurch nicht abholen.

**[00:07:32]** Also, ich sehe das bei mir, dass ich schaue, okay, habe ich ein Testsystem, auf den ich

**[00:07:41]** das testen kann, was sind die Use-Cases, mit denen ich das testen will und während

**[00:07:46]** dann halt andere Kollegen quasi gerade so mit aufspringen und eigentlich sind die halt auch

**[00:07:52]** mit dabei, sind dann halt andere schon bei jetzt Craft Agents zum Beispiel gelandet und sagen,

**[00:07:58]** das ist aber, also das ist ja viel sinnvoller als Openclaw und die ganzen Installationen,

**[00:08:04]** die ich von Openclaw hatte, die brauche ich gar nicht mehr. Und wenn du die nach N8n fragst,

**[00:08:07]** dann war das so, warte, das war doch 2025, oder? Also die Geschwindigkeit, in der wir wirklich

**[00:08:16]** brauchbare Tools haben und in der wir die ersetzen, die überfordert viele und da bin ich halt wieder

**[00:08:23]** bei dem Punkt den Klaus eben angebracht habe. Ich versuche seit geraumer Zeit Software-Architektur

**[00:08:30]** Mahut, versuche ich so dieses Prinzip von Build for Replacement in meine Kollegen, in unsere

**[00:08:39]** Entwicklungsteams reinzukriegen, weil in der klassischen Softwareausbildung hast du ja so

**[00:08:45]** Sachen wie don't repeat yourself und du musst Abtraktionen finden und du musst Dinge wiederverwendbar

**[00:08:52]** machen und dass diese klassische Software Ausbildung aus den Menschen rauszukriegen ist wirklich schwer.

**[00:09:01]** So dieses Nein, das ist nicht dein Baby, das ist Pets versus Kettle, das ist Kettle,

**[00:09:06]** das ist nicht böse gemeint, sondern es ist einfach eine Menge und es geht halt durch und

**[00:09:12]** Wir brauchen dafür, glaube ich, in Zeiten, wo wir unsere Ernährung umstellen sollten,

**[00:09:16]** vielleicht irgendwie ein anderes Bild, aber ihr wisst, was ich meine.

**[00:09:19]** Also dieses Bildverreplacement.

**[00:09:21]** Was ist gegen Pizza einzuwenden?

**[00:09:23]** Was?

**[00:09:24]** Das verstehe ich nicht.

**[00:09:25]** Was ist gegen Pizza einzuwenden?

**[00:09:26]** Ich meinte Airpads vs. Kettle und ich weiß nicht, wie du bei beiden auf Pizza, aber

**[00:09:30]** ist egal.

**[00:09:31]** Gut.

**[00:09:32]** Pizza.

**[00:09:33]** Aber das ist ein ganz anderes Thema.

**[00:09:36]** Ja.

**[00:09:37]** Ich würde ja noch eine provokante Tee in den Raum stellen für den Rest des Podcasts.

**[00:09:41]** Ich prophezeihe das Ende der Wiederverwertbarkeit, ich prophezeihe das Ende der Software-Architektur,

**[00:09:49]** nicht der Übergreifende-Architektur, sondern sowas wie der App-Architektur.

**[00:09:54]** Und ich prophezeihe auch das Ende von Formiersprach.

**[00:09:56]** Ich fand das ganz lustig. Ich hatte letztens tatsächlich mit ein paar Kollegen,

**[00:10:00]** die mich dann völlig entgeistert angeguckt haben, so nach dem Motto,

**[00:10:03]** aber ich bin doch jetzt sinngemäß Experte in einer Sprache, was er sich,

**[00:10:07]** Was nehmen wir jetzt mal PRP? Einfach nehmen wir mal PRP. Nehmen wir mal die Sprache, die

**[00:10:11]** erst zur Laufzeit sich überlegt, bin ich eine Zahl oder ein Text? Entschuldigung, wenn es so nötig

**[00:10:15]** war. Nein, nein, schon. Und ich bin da, ja? Ich sag mal so, du bist jetzt drin, ja? Du kennst

**[00:10:20]** das, du kannst das runterbeten, du kannst es lesen, du bist da der Crack unterm Herrn. Und da

**[00:10:26]** kann man die Frage, meinst du denn wirklich, dass das kommt? Das war doch noch nie der Fall.

**[00:10:32]** Und da war quasi die Gnade meiner frühen Geburt mir zur Hilfe gekommen, weil ich hatte damals

**[00:10:39]** tatsächlich auch sowas wie Assemblermal in den Fingern und dann kam halt irgendwann auch mal sowas

**[00:10:46]** komisches wie PRP und Turbo Pascal, wie der ganze Quad-Standard zwischenzeitlich so hieß. Also

**[00:10:52]** wir hatten das schon mal nur mit dem Unterschied, ich sag mal, es hat erstens länger gedauert und

**[00:10:58]** Und zweitens wurde die Sprach ja dann verständlicher für den Menschen, damit der Mensch ihn nicht,

**[00:11:04]** also, Assempler zu schreiben, das ist mal als Party-Gag heute lustig, aber das will ja

**[00:11:10]** heute auch keiner, so wirklich, vielleicht beim Thermomix, keine Ahnung.

**[00:11:13]** Aber will vielleicht jetzt so, um der normalen Software entwickeln, vielleicht keiner machen.

**[00:11:16]** Ich sehe schon, Alex zuckt schon, der will vielleicht etwas sagen, aber worauf ich

**[00:11:19]** raus wollte, ist dieser, diesen Blick in den Augen der Menschen, weil sie dann doch

**[00:11:24]** irgendwie merken, ich will jetzt nicht von Einschlägen sprechen.

**[00:11:28]** hin zu, wir müssen nicht alles mehr modular machen, sondern auch ein gutes Stück

**[00:11:35]** Wegwerfssoftware. Du hast was gebaut, es ist da, es funktioniert und im halben Jahr

**[00:11:40]** funktioniert es vielleicht anders. Das ist etwas, da muss man auch die Menschen

**[00:11:44]** mitnehmen, weil die Technik, müssen wir mal ehrlich sein, die kann es.

**[00:11:47]** Die entscheidende Frage für mich ist oder andersrum, wenn ich mit

**[00:11:54]** mit Kollegen oder auch mit Leuten im Netzwerk über KI sprechen. Da kommt relativ schnell

**[00:12:00]** dann irgendwann, ich frage hoch, ja gut, aber was ist dann eigentlich noch mein Job? Wofür

**[00:12:06]** bin ich eigentlich noch da? Und dieses Bewusstsein, und du hast eben das Assembler-Beispiel gebracht,

**[00:12:13]** da habe ich eine andere Anekdote zu, da habe ich mich, was nicht letzte Woche sogar klaust,

**[00:12:18]** wo wir uns mit einem Kollegen drüber unterhalten haben.

**[00:12:22]** Die bestrittenen haben. Nee, das war eben noch was.

**[00:12:24]** Nee, das war das andere.

**[00:12:26]** Wo wir uns darüber unterhalten haben, dass wir gesagt haben, naja,

**[00:12:29]** Kotmetriken, die wir früher halt wirklich als so Qualitätsansprüche hatten,

**[00:12:34]** und gesagt haben, naja, Kotqualität ist halt wichtig,

**[00:12:38]** die sind halt heute nicht mehr so relevant.

**[00:12:41]** Weil warum waren die früher wichtig?

**[00:12:43]** Na ja, weil Menschen es schaffen mussten, diesen Kot zu verstehen,

**[00:12:47]** zu verstehen, was soll das eigentlich Ende zu Ende tun? Was ist der Teil, den ich hier vor Augen habe,

**[00:12:53]** bei den ich gerade in meinen Kopf kriege, Stichwort Context Window, und was ist sein Beitrag zu Ende

**[00:13:00]** zu Ende? Und so wie das damals bei Assembler war, ich kann mich daran erinnern, als ich Ende der 90er

**[00:13:06]** damit mit Hochsprachen angefangen habe, da hatte ich auch zwei Kollegen, die die Assembler

**[00:13:12]** programmiert haben und mir gesagt haben, ah, mit den Hochsprachen, das wird sich nicht

**[00:13:16]** durchsetzen. Das setzt sich nicht durch. Also wir brauchen ja effiziente Programme und nichts ist

**[00:13:22]** so effizient wie Assembler. Und diese Art von Effizienz, die spielt halt heute nur noch in Nischen

**[00:13:29]** eine Rolle. Also es gibt Nischen, da brauchst du die. Also ich will jetzt nicht auf so Bremsentechnik,

**[00:13:36]** aber es gibt halt einfach Sachen, da bist du schon im Untermillisekundenbereich, wo du sagst,

**[00:13:41]** Nee, das muss schon, das muss bitte schon irgendwie sehr, sehr effizient sein, dass da die

**[00:13:47]** Response sein kann.

**[00:13:48]** Und dann kam Java.

**[00:13:50]** Ja gut.

**[00:13:51]** Da geht mein Point, glaubst du, genau.

**[00:13:54]** Genau.

**[00:13:55]** Und Microservices in der Bremseinlage, genau, genau.

**[00:13:58]** Ich verstehe natürlich schon, wenn du das eine ist, ich kann mir jetzt zu Hause

**[00:14:04]** auf die Schnelle irgendwie Software zurecht dängeln, ich habe mich heute Morgen

**[00:14:08]** an ein Stück Software gesetzt, das mir hilft, warum ich solche Hobbys habe, weiß ich auch nicht,

**[00:14:14]** aber so Pumped Injections ins Guilds zu erkennen und so ein Kram. Also habe ich mir so ein Stückchen

**[00:14:19]** Software zusammengekotet mit einem Agenten, um probier halt aus, wie gut funktioniert das und

**[00:14:25]** du baust ja quasi deine Helferlein. Für eine Unternehmensanwendung wirst du wahrscheinlich

**[00:14:30]** schon nochmal so zwei, drei extra Schleifen drehen müssen, das ist noch die Worte, was

**[00:14:33]** befinden. Da wirklich starte, bevor ich das vielleicht auf Kunden oder interne Prozesse

**[00:14:37]** rauslassen. Aber nichtsdestotrotz, es geht ja genau in diese Richtung hin und die Menschen mitzunehmen

**[00:14:42]** auf eine Reise. Wie arbeite ich denn mit so was? Wie gehe ich denn damit um? Ja, ich meine, dass die

**[00:14:49]** einen sagen Vibecoding, die anderen sagen Agentic Engineering. Je nachdem, wie du die Rolle auch

**[00:14:54]** immer wieder prägst, ist das ja durchaus ein Wandel in der Arbeitswelt. Zum einen in der

**[00:15:00]** Befähigung der Menschen, aber auch zum anderen in der Frage, was ist denn da mein Job? Was darf

**[00:15:06]** darf ich denn in Zukunft machen? Ab wann gucke ich wieder drauf? Gebe ich frei? Bestimme

**[00:15:12]** ich? Keine Ahnung, was? Da wird sich garantiert eine Menge ändern, oder?

**[00:15:15]** Absolut. Ich sehe nicken. Das schöne für ein Audio-Podcast, man muss das nicken, dann

**[00:15:20]** auch auditiv bestätigen. Ich sehe nicken. Und ich glaube es ist auch schwer, die Leute

**[00:15:26]** wirklich gesagt auf diesem Weg zu begleiten, weil es ist ja alles so schnelllebig, dass

**[00:15:29]** man ja gar keine Ahnung hat, ehrlicherweise. Was ist denn in drei Monaten wieder die

**[00:15:33]** die nächste Sau, die aufgetrieben wird, die wieder alles auf links dreht, weil ich weiß ja nicht, wie es euch geht.

**[00:15:39]** Mit diesem Craft-Agent, als ich damit das letzte Mal mich da beschäftigt hatte, ist es noch nicht so lange her.

**[00:15:45]** Da war vorher dann Open-Claw und dann war vorher Cloudcode und dann war vorher, keine Ahnung, was.

**[00:15:52]** Und irgendwann davor war Gemini. Das ist ja irgendwie mega schnell alles.

**[00:15:57]** Ja, du siehst ja, du siehst ja da ein Problem, was wir schon haben, seit IT existiert,

**[00:16:02]** dass man immer vorschnell, also man neigt ja immer dazu, man im Sinne von Unternehmen

**[00:16:09]** vorschnell mit Lösungen auf Probleme zu werfen, ohne vorhin man nachgelacht zu haben.

**[00:16:14]** Und ich glaube, so die Frage, die Antwort auf die Frage, welche Rolle spielt ich als

**[00:16:21]** Einzelner in diesem Prozess, die kann ich natürlich beantworten.

**[00:16:24]** Aber ich glaube, um als Unternehmen zu sein, müsste man jetzt mal einen Schritt zurücktreten

**[00:16:30]** und sich überlegen, was bedeutet denn agentische Arbeitsweise für uns, egal ob ich das jetzt

**[00:16:35]** mit NLN-Orchestriere, mit Open Claw oder mit Tralala ist ja voll komwurscht.

**[00:16:40]** Das schlechteste, was passieren kann, ist, dass man einfach alte Arbeitsweisen nimmt

**[00:16:45]** und mit KI unterführt hat, was wir ja schon eigentlich in der Geschichte der IT immer

**[00:16:50]** sehen.

**[00:16:51]** Schlechte Prozesse sind einfach digitalisiert worden, war nachher noch genau so schlecht und hat

**[00:16:57]** sie jetzt nur digital und es ist teurer. Sie laufen vielleicht ein bisschen schneller,

**[00:17:01]** aber es ist ja keine Lösung. Und ja, ich glaube, was du ansprichst mit der Frage,

**[00:17:05]** was ist meine persönliche Aufgabe? Du hattest das eben, glaube ich, schon erwähnt, Alex,

**[00:17:12]** dass die Fähigkeit des Anlearnings und des Learnings wird immer wichtiger. Ich weiß noch,

**[00:17:19]** als ich Abitur gemacht habe, ist jetzt auch schon ein, zwei Jahre her. Da hieß es immer so, ja, da gab es

**[00:17:26]** noch den Freizeitpark Deutschland, den hat der damalige Kanzler so genannt und da hieß es so,

**[00:17:30]** wir müssen uns einstellen auf lebenslanges Lernen. Ja und jetzt kommt noch hinzu auf lebenslanges

**[00:17:36]** Unlearning, was glaube ich noch eine viel größere Herausforderung ist, denn irgendwas hat

**[00:17:41]** ihr eben schon gesagt, Alex, das aus den Köppen zu kriegen, was ja irgendwie so ganz viele,

**[00:17:46]** ja auch psychologische Facetten hat. Also man möchte das persönlich überflüssig werden. Man hat sich vielleicht auch über Jahrzehnte Wissen aufgebaut.

**[00:17:54]** Und man jetzt merkt, oh, verdammte, den kann das, was ich mir über Jahrzehnte, ich mein mag, du hast, wir beide haben viel publiziert.

**[00:18:03]** Ich habe viele Bücher über Epic-Infection geschrieben. Jetzt sehe ich mir ein Code, da brauche ich kein Einzelnsbuch zu lesen.

**[00:18:09]** zu lesen, und es kommt eine fertige Entdauer raus.

**[00:18:11]** Und welche Fähigkeiten ich dann dafür brauche?

**[00:18:13]** Ich glaube, das sind nicht solche Fähigkeiten, wie sie im Moment immer postuliert werden,

**[00:18:18]** wie, oh, jomenende Lob, und jemand muss ja nach diesen Source Code lesen und alles prüfen,

**[00:18:23]** ob das richtig ist.

**[00:18:24]** Das ist eine typisch menschliche Selbstüberhöhung.

**[00:18:28]** Wenn das LLM, der Code der Code der vom Aus-n-LLM-Feld, der ist gut, und wenn

**[00:18:33]** ich dann noch ein anderes draufsetze und den prüfen lasse, dann weiß ich, dass

**[00:18:36]** der gut ist, dann muss ich da nicht noch als Mensch drüber gucken.

**[00:18:39]** Zumal in LLM ja sehr viele von den Tasken, die du machen kannst, wie zum Beispiel in

**[00:18:43]** Linter benutzen, kann das, kann Cloudcode ja auch, aus meiner Sicht ist halt relativ

**[00:18:50]** wichtig, dass wir, dass wir uns anschauen, was sind, was sind heute Sachen, an denen

**[00:18:55]** Menschen halt finden und viele finden halt, an zum Beispiel ihrer Rollen bezeichnen, dass

**[00:19:01]** sie sagen, ich bin Entwickler und voller Stolz, genau, aber das finde ich, das

**[00:19:06]** finde ich halt schwierig, weil also mich macht ja nicht meine Rollenbezeichnung aus, sondern

**[00:19:12]** die Dinge, die ich tue und für die ich für dich irgendwie ein Herzblut empfinde, insofern

**[00:19:18]** eine Rolle ist halt immer, was temporäres, was ich einnehme, eine Verantwortung, die ich

**[00:19:22]** übernehme und die kann sich halt morgen ändern und ja, was, was mir wichtig ist,

**[00:19:28]** ist a, was trage ich eigentlich zum Endergebnis bei, was ist das Endergebnis, kann ich

**[00:19:32]** da kann ich dafür, also möchte ich dazu beigetragen haben, möchte ich dazu beitragen und auf der

**[00:19:39]** anderen Seite, mit wem arbeite ich daran, macht mir das Freude, erfüllt mich das. Das klingt

**[00:19:46]** vielleicht ein bisschen pathetisch, aber das ist mir unheimlich wichtig. Ich weiß,

**[00:19:50]** dass du meinst, dass ich morgens aufstehe und weiß, ich arbeite mit Menschen, die

**[00:19:54]** die A genauso Bock darauf haben und B auch noch kompetent sind, ihren Beitrag dazu zu

**[00:20:02]** parken.

**[00:20:03]** Aber ich glaube schon, dass das, es hört sich immer so an wie man weiß es besser, man ist

**[00:20:08]** ja auch selbst Bestandteil dieser Maschinerie und auch betroffener, beteiligter, ja.

**[00:20:16]** Trotzdem, wenn ich mal so ganz kurz in die Vergangenheit guck, als ich bei der MBW angefangen

**[00:20:21]** habe, konnte ich vor mehr als drei Menschen keinen flüssigen Satz sagen. Ich war mehr

**[00:20:24]** so der Kellerkindentwickler. Das hat sich dann irgendwann geändert. Zum Glück entwickle ich

**[00:20:29]** nicht mehr, nicht weil jetzt hier KI vor der Tür steht, sondern weil ich dann doch die

**[00:20:33]** Professorin etwas anderem gefunden habe. Aber trotzdem gibt es ja Menschen, die, ich

**[00:20:39]** sage jetzt mal das Thema Softwareentwicklung, Softwarearchitektur, die Schönheit, Verständlichkeit

**[00:20:43]** von Code, das Durchdringen von Nüssen, wo man früher vielleicht keine Ahnung mit

**[00:20:48]** ewig langen Studium von Stack Overflow und Nechten voller Bier und Rum, sich irgendwelche Sachen

**[00:20:54]** zu ausgedacht hat und die da total geil waren. Und jetzt auf einmal kommt, ich sage jetzt mal der

**[00:20:59]** Kollege, die Kollegin der Student wie auch immer um die Ecke hat irgendwie drei Tolle Poms geschrieben

**[00:21:05]** und hat ein besseres Ergebnis vielleicht in der Wahrnehmung oder in der Geschwindigkeit wie

**[00:21:11]** ein Ziel erreicht wird. Ist vielleicht nicht die saubeste Architektur hinten rum, aber

**[00:21:15]** ist interessiert halt auch kein mehr. Ja, genau. Programmierer würde ich heute auch nicht

**[00:21:20]** mehr unbedingt schwer werden. Wobei die Fähigkeit, Dinge in einem größeren Zusammenhang zu sehen,

**[00:21:26]** bleibt ja unbestehen. Also, was ich eben sagte mit das Ende der Softwarearchitektur. Du

**[00:21:35]** musst jetzt nicht mehr diskutieren, ob du eine iOS App mit Viper oder MVV, Pralala, wie

**[00:21:41]** wie diese, so kennst du diese ganzen, das haben wir uns da früher drüber zur Tode diskutiert,

**[00:21:47]** das ist alles hinfällig. Aber so eine Gesamtarchitektur, wenn ich das auch so testen kann.

**[00:21:51]** Aber im Space diskutieren wir immer noch, oder? Ja, genau. Eine Gesamtarchitektur von

**[00:21:56]** Embedded Controller, von dem Motor, von der Heizung im Thermomix bis in die Cloud über

**[00:22:02]** mobile App, da brauchst du ja schon noch ein bisschen was am Erfahrung, wobei ich

**[00:22:09]** bei der Geschwindigkeit, wie diese AI dazulehrend auch sagen würde, dann müssen wir uns jetzt

**[00:22:14]** aber auch nicht zu hoch einordnen. Auch das wird architektonisch auch mal in nicht allzu

**[00:22:21]** ferner Zukunft so ein Ding mindestens gut können.

**[00:22:24]** Aber der Punkt, auf den ich eigentlich raus wollte, vielleicht habe ich mich auch fegaloppiert

**[00:22:29]** in meinem Sprachdurchfall. Ich erinnere mich, als wir vor kurzem das Thema Native versus

**[00:22:36]** Cross-Plattform-App-Entwicklung. Womit gehe ich denn zum Ziel? Da gab es ja durchaus, ich

**[00:22:43]** sage mal, Lager, die gibt es wahrscheinlich immer noch, die das eine oder andere favorisieren

**[00:22:47]** und sich auf dem jeweiligen Lager auch so weiterbilden, dass sie sei es Kotlin, sei es

**[00:22:52]** Wilf, sei es keine Ahnung, zu einem sehr guten Software-Ergebnis kommen und das wird

**[00:22:57]** halt immer mehr irrelevant.

**[00:22:58]** Kennst du diese verlorenen Seelen, die Webviews in nativen Apps für gute Ideen

**[00:23:05]** halten?

**[00:23:06]** Eyeframes auch war auch schon. Ja, okay.

**[00:23:10]** Ja, ja, aber das sind halt Dinge, die ändern sich, ja. Also von der Seite

**[00:23:14]** letzten standen einer bei mir und meinte so, das ist ja so ähnlich wie der Einführung der Dampfmaschine, wo ich meinte, bist du JAK?

**[00:23:19]** Die Dampfmaschine hat damals ewig viel Zeit gebraucht, bis die quasi mal so in Masse überall war.

**[00:23:25]** Du musst das Gebäude hinstellen, du musst das Maschinen hinstellen, die Menschen sind zu den Maschinen, ja.

**[00:23:29]** Dann hast du das ganze Thema, wie betreibst du die, okay, Strom kam dann irgendwann in die Ecke, aber worauf ich raus tu, das hat halt Zeit gebraucht.

**[00:23:35]** Und heute sitzt hier, Grüße gehen an Peter, ja, der Open Clore da irgendwie über den

**[00:23:41]** Etter geschmissen hat, drückt auf Deploy und wie viele Wochen ist das jetzt her, vier

**[00:23:45]** oder fünf oder sechs?

**[00:23:46]** Keine Ahnung.

**[00:23:47]** Jetzt ist er quasi Adelaide von Sam Altman bei Open AI und schwupp die Wupp, ja, das

**[00:23:53]** hätte also, das geht alles so schnell, das kann überfordern.

**[00:23:58]** Aber nochmal auf den Boden der Tatsachen zurückzukommen, dieses Beispiel mit diesen

**[00:24:01]** Webviews in den nativen Apps.

**[00:24:05]** Ich finde, das ist ein schönes Beispiel dafür, wie sich, wie die KI solche architektonischen

**[00:24:11]** Fragen beantwortet.

**[00:24:12]** Früher oder bisher ist es, die Argumentationen gewesen, kommen wir in den Webview, da sind

**[00:24:17]** wir schneller.

**[00:24:18]** Wir bauen einfach diese Webseite ein, müssen nicht nativ in der App irgendwas anpassen,

**[00:24:21]** vor allem in die Webseite, die sich verändert.

**[00:24:23]** Das spielt heute keine Rolle mehr.

**[00:24:24]** Wenn sich das Ding ändert, dann schmeiße ich die neue JSON-Struktur da rein oder

**[00:24:29]** bis Figma oder was weiß ich und dann wird das einfach nativ umgesetzt und zwar

**[00:24:32]** innerhalb von Minuten und nicht innerhalb von Tagen.

**[00:24:34]** hängt von deinem Prozess ab, Klaus. Also du hast da implizit, lass uns mal so in von

**[00:24:40]** weiß ich nicht, glaube ich nicht, kann ich mir nicht vorstellen, in konkrete Beispiele

**[00:24:43]** kommen, weil du hast es ja konkret gemacht. Du hast ja konkret da so ein

**[00:24:47]** Prozess aufgesetzt. Und ich glaube, das ist relativ wichtig, dass wir solche

**[00:24:52]** Praxisbeispiele halt mal, also da mal kurz drüber sprechen, weil ansonsten

**[00:24:58]** bleibt das halt beim ja weiß ich nicht, glaube ich nicht, aber nicht bei uns.

**[00:25:02]** Also, ganz konkret, wenn du halt ein App-Deployment-Prozess hast, der einfach so viele Freigabestufen

**[00:25:11]** und manuelle Schritte hat, dass du irgendwie drei Tage brauchst, bis du irgendwas bei

**[00:25:17]** Apple einreist, dann verstehe ich nicht.

**[00:25:19]** Wie verstehe ich dich?

**[00:25:21]** Was ist denn das für eine Moderation hier?

**[00:25:25]** Was verstehst du nicht?

**[00:25:28]** Was will mein Kollege damit sagen?

**[00:25:30]** Wer, ich will sagen, deine Hypothese ist, naja, die KI kann dir schnell eine neue Version von der App bauen und zum Review einreichen und da das eine kleine Änderung ist, wird dieser Review wahrscheinlich schnell durchgehen.

**[00:25:44]** Nie, das ist ja wieder eine viel zu große Spezifizierung eines Spezialfalls.

**[00:25:50]** Es geht hier darum, du hast ein schimmeliges Formular, was du in der Webseite hast oder

**[00:25:54]** ein Online-Shop, wo du dann bisher gesagt hast, den packen wir jetzt einfach in die App

**[00:25:59]** rein, weil wir keine Lust haben, den Nativ nachzubauen.

**[00:26:03]** Das ist halt Arbeit, die App sei es in Zwift, in Kotlin oder sonst was, das Nativ zu bauen

**[00:26:07]** ist einfach Arbeit.

**[00:26:08]** Das lassen wir jetzt tun.

**[00:26:09]** Es geht ja nicht darum, dass du den jeden Tag ändern kannst, das ist sicherlich

**[00:26:12]** auch ein Aspekt.

**[00:26:13]** Aber überhaupt erst mal zu sagen, wir nehmen jetzt einfach die API statt der Webseite und

**[00:26:18]** lassen die UI von der, wir geben dem mit dem screenshot von der Webseite und sagen,

**[00:26:22]** bauen wir das in Zwift nach, das ist no-brainer, funktioniert out of the box.

**[00:26:26]** Ja, aber auch die Änderung, das ist ja der Punkt.

**[00:26:30]** Bisher war es ja, oh nee, wir lassen das mal beim Backend und das Backend liefert

**[00:26:34]** dann mit die Webseite aus, weil separation of concerns und das ist Concern beim Backend-Team

**[00:26:39]** und das Backend-Team und die Datenstruktur.

**[00:26:42]** Und jetzt sagst du halt, wir hätten einen Explicitag, lass mal die unflittige Ausdrücke weg.

**[00:26:48]** Nee, du hast ein Agent-Team und das ist Ende zu Ende verantwortlich.

**[00:26:52]** Ja, okay.

**[00:26:53]** Das ist Ende zu Ende verantwortlich und das ändert jetzt gleichzeitig den Code der iOS-App

**[00:26:58]** und im Backend und sorgt dafür, dass der Bums gleichzeitig gegottet wird.

**[00:27:02]** Und das ändert Denke und Arbeitsweise.

**[00:27:04]** Ja, also das geht.

**[00:27:08]** Wenn du es denn denkst, das ist mein Punkt.

**[00:27:10]** Punkt. Wenn du aber in deinen Strukturen verhaust, dass du sagst, naja, ich habe ein Backend-Team

**[00:27:15]** und wenn die jetzt nicht mehr alleine verantwortlich sind, dann müssen die sich hier erst mal mit

**[00:27:18]** dem Frontend-Team abstimmen und dann müssen die jeweils getrennt ihre Agents aufsetzen.

**[00:27:23]** Nein, nein, nein. Das ist das Thema mit, wenn du einen nicht ganz so guten Prozess hast,

**[00:27:28]** dann kommt auch ein nicht ganz so gutes Ergebnis raus.

**[00:27:30]** Aber dadurch zum Anfang hast du Vibecoding, Vibecoding populär worden, irgendwie so

**[00:27:35]** einen schönen Quote gesehen, wo einer sagte, solange die KI nicht die Diskussion

**[00:27:39]** mit dem Product Manager ersetzen kann, hilft mir das überhaupt nicht. Ich glaube, das geht ja

**[00:27:45]** schon mal in die Richtung. Das reine Codein am Ende ist ja nur ein kleiner Teil des gesamten

**[00:27:50]** Prozesses und man muss diesen ganzen Prozess anschauen und auf den Prüfstand stellen und nicht

**[00:27:55]** sagen, wir benutzen jetzt KI als qualifizierte Autokompletion. Bei Vibecoding muss ich übrigens

**[00:28:03]** immer noch an dieses Nie mit dem Klopapier denken, so nach dem Motto, naja, das ist jetzt mal

**[00:28:09]** da hingerotzt, aber dann möchten wir es irgendwann auch wieder weg tun, weil es fängt an zu riechen.

**[00:28:13]** Ich würde mal die Haupt- also aus meiner Berufserfahrung, was würde ich mal die

**[00:28:17]** Behauptung in den Raum stellen, das geht für 80 Prozent der Software, die auf

**[00:28:20]** diesem Planeten bisher geschrieben worden ist, unbesehbar.

**[00:28:23]** Ich sage nochmal, Bild vor Replace, wenn das anfängt zu riechen, sollte man es vielleicht erwärmen.

**[00:28:30]** den Windows Core noch einschmeißen kann. Ich überlege gerade, wie groß müsste das Windows sein, damit wir das machen können? Aber da war wieder der Nerd in mir. So, ich sag mal, ich würde nochmal zurückkommen wollen auf das Thema Ende zu Ende. Also, was für mich halt super klar ist, wenn du, wenn du halt nur in deiner, in deiner IDE Realität bleibst und sagst, naja, die, die iOS Entwicklung

**[00:29:00]** Die sind halt den Xcode unterwegs und dann gibt es noch irgendwelche, die nutzen IntelliJ

**[00:29:05]** und andere sind noch bei Emacs.

**[00:29:07]** Hat ihr Emacs gesucht?

**[00:29:09]** Das kannst du halt so machen, dann musst du dich halt nicht wundern, dass die KI irgendwie,

**[00:29:19]** naja, auch nicht so das Ende zu Ende Verständnis hast.

**[00:29:23]** Wenn du aber sagst, warte mal kurz, Agentic Engineering ist halt mehr als nur das Coding

**[00:29:29]** meines Backends oder meiner App, sondern es geht halt um Ende zu Ende Verständnis. Was wollen

**[00:29:36]** wir eigentlich erreichen? Was ist der Wert oder das Problem des Kunden? Was ist das Problem

**[00:29:41]** des Kunden, was wir adressieren wollen? Was ist der Mehrwert, den wir dem Kunden bieten

**[00:29:44]** wollen? Und das gemeinsam in einem kleinen Team aus Subject Matter Experts durchdenkst,

**[00:29:50]** dann hast du erstmal das richtig volle Potenzial der heutigen KI-Agenten auf

**[00:29:56]** auf deiner Seite. Und das ist ein Thema, was aus meiner Sicht noch nicht in allen Köpfen

**[00:30:02]** angekommen ist. Das eine ist, was kann das jetzt schon in bestehenden Prozessen machen?

**[00:30:06]** Das andere ist, aber wenn ich bereit bin, mal kurz den Schritt zurückzugehen und zu sagen,

**[00:30:11]** warte mal, was wollten wir eigentlich mit dieser Teamstruktur, mit diesem Organisationsjagd

**[00:30:15]** einmal erreichen?

**[00:30:16]** Warum haben wir das so gewählt?

**[00:30:17]** Ich meine, das, was ihr vorhin auch sagt, nach dem Motto, die modulare Entwicklung

**[00:30:20]** und die ganzen Vorgaben waren dafür da, damit du verteilte Entwicklung über den

**[00:30:25]** Klobos hinweg am besten noch in großen Teams irgendwie hinkriegst und irgendwie backend und keine Ahnung was.

**[00:30:32]** Dann hast du da eine Organisationsstruktur drüber gestürbt, damit die ganzen Menschen eine Heimat haben in persönlicher Entwicklung, in organisatorischer Zusammenarbeit.

**[00:30:40]** Wie arbeiten wir auf einem Team?

**[00:30:43]** Dann kam der ganze Agile-Kram um die Ecke, hat versucht, wie die Teams zu formen und zu führen.

**[00:30:48]** Und jetzt kommt auf einmal Agentin um die Ecke und sagt, du passt mal ober, wir haben vielleicht ein Werkzeug, das ist nicht nur.

**[00:30:55]** Ich sag mal schnelllebig in der Technologie, die es bereitstellt und was es kann.

**[00:30:59]** Es ist nicht nur der Mensch, der sich darauf einlassen muss, vielleicht etwas mehr Generalist

**[00:31:04]** und mutiger und gesamthaft draufschauen zu sein.

**[00:31:08]** Aber dann ist es auch das Thema nicht nur das Einzeln, sondern auch der Organisation.

**[00:31:13]** Selbst, in der man seine Arbeit verrichtet, in mehr wie groß oder klein die Firmen auch

**[00:31:19]** immer sind, die Frage aufzuwerfen, wie muss man sich organisatorisch aufstellen, um

**[00:31:24]** das bestmögliche da herauszuholen, damit nicht Team A sagt, ich habe einen ganz tollen Agent,

**[00:31:29]** der läuft aus Copilot und hast du nicht gesehen und der druckt dir hier, weißt du, ich druckt

**[00:31:33]** dir ein Word aus, damit dies wohin fachse, damit dies irgendwo einscanner, damit dort Nano-Banana

**[00:31:38]** mehr wieder ein editierbares Formulat rausmacht. Dass das halt nicht passiert. Wie gesagt,

**[00:31:45]** es gibt das Fax-GPT, da bin ich immer noch geistig abhässend, aber…

**[00:31:49]** Bist du da?

**[00:31:52]** Nein.

**[00:31:53]** Ja, ich weiß.

**[00:31:54]** Die Erfahrung mit der Hand an dem Prozess, das klingt gerade so an der Seite.

**[00:31:59]** Aber dann sind das noch eins, drei echt große Dinge, an denen, ich hört es jetzt auch wieder

**[00:32:04]** komisch an, man Hand anlegen müsste, weil in allen drei Feldern ist ein weiter so

**[00:32:10]** wie jetzt veralessig.

**[00:32:12]** Kurzer Disclaimer, Beispiele die Mark bringt sind nicht zur Implementierung gedacht.

**[00:32:19]** Ich werde dich beim nächsten Wochenend-Chent dran erinnern, ja, aber...

**[00:32:24]** Aber das bringt...

**[00:32:30]** Nein, aber Spaß beiseite. Wenn wir das jetzt halt so sagen, von wegen, ja, du musst halt auch...

**[00:32:36]** Du musst halt auch überlegen, dass du mal outside the box denkst und sagst, okay,

**[00:32:41]** was könnten wir vielleicht an der Organisation ändern.

**[00:32:44]** Das ist jetzt kein, das ist jetzt kein, kein Appell für,

**[00:32:49]** oh ja, in der Organisation kann ich ja nichts ändern.

**[00:32:51]** Dann, dann bin ich ja komplett macht,

**[00:32:53]** bloß dann kann ich das ja eh nicht entscheiden,

**[00:32:54]** dann bringt mir das ja nichts, ne?

**[00:32:56]** Sondern in die Richtung gehst du.

**[00:32:57]** Ich hatte kurz gedacht, du gehst hier in die Richtung,

**[00:32:59]** dass Kollegen von uns jeweils zuhören und denken,

**[00:33:02]** um Gottes Willen, was kommt um die Ecke.

**[00:33:04]** Ich dachte, du bringst jetzt den Disclaimer.

**[00:33:06]** Ja, aber natürlich, das ist...

**[00:33:09]** Nee, die wissen das schon.

**[00:33:11]** Also bei Klaus und mir wissen die Kollegen das schon.

**[00:33:15]** Nein, also worauf ich hinauswollte ist, wenn wir sagen, Agentic Engineering ist halt mehr

**[00:33:21]** als Software programmieren.

**[00:33:23]** Ich habe bis vor zwei Jahren bei uns noch auch den Betrieb geleitet und alleine, wenn

**[00:33:29]** ich mir überlege, welche Möglichkeiten da sind, bestehende Denke oder bestehende Prozesse

**[00:33:38]** in Betrieb zu ersetzen. Welche Chancen ich habe, auf einmal so etwas wie klassische Anomalie-Detections

**[00:33:46]** zu unterstützen, durch einen LLM oder überhaupt durch Agents, die auf verschiedene Aspekte,

**[00:33:56]** also so verschiedene Personas mitbringen und mit diesen Personas auf zum Beispiel Logfiles

**[00:34:01]** gucken und Logfile-Analyse machen, das ist großartig, dass du auf einmal auf Dinge

**[00:34:06]** hingewiesen wirst und ich werde auch nicht müde, Kollegen, das zu erzählen, wenn du dann es schaffst,

**[00:34:13]** für deine Software mal Spezifikation zu schreiben, zu sagen, was erwarte ich eigentlich, was die

**[00:34:18]** Software tut. Stellt ihr das mal vor, man könnte das, weil dann könnten die Agents im Betrieb

**[00:34:23]** sagen, du sag mal, du hast ja aufgeschrieben, die Software soll das tun und das tun und das

**[00:34:27]** andere hier nicht tun. Die macht aber auch dieses komische Zeug hier. Ist das erwartet oder ist

**[00:34:32]** Ich habe doch gestern, das kannst du nicht wissen, der Alex Weiß ist, weil ich es Ihnen gesagt habe,

**[00:34:38]** davon fabuliert, dass das ISMS, das Informationssicherheitsmanagement System, nach ISO 7291, das wir

**[00:34:47]** gerne aufbauen, um Compliance zum EU Cyber Resilience-Aktion zu bekommen, damit wir auch in Zukunft

**[00:34:53]** noch schöne Thermobics verkaufen können. Ich hoffe, ihr habt allein, dass auch dieses ISMS,

**[00:34:59]** das ja eigentlich ein total sperriges, starres, organisatorisch, prozessuales Rahmenwerk ist,

**[00:35:05]** bei uns als agentische Implementierung funktionieren muss, eingebettet in diesen, also übergeordnet,

**[00:35:16]** der Software, der Software-Weltungsprozess eingebettet in dieses ISMS, aber so Sachen wie,

**[00:35:21]** ich habe das noch nicht ganz durchdacht, aber wenn man sich jetzt mal vorstellt,

**[00:35:24]** dieses ICMS besteht im Kern aus einem Regularium und einem KVP, also einem Regelkreis.

**[00:35:30]** Und wenn ich mich jetzt nicht mehr Menschen hinsetzen und sage, guck mal, jetzt überprüft

**[00:35:36]** mal einmal im Quartal, sind wir besser geworden, sondern agenten das kontinuierlich machen

**[00:35:41]** und zwar mit all diesen Möglichkeiten, die sie haben, aus dem Entwicklungszyklus, aus

**[00:35:44]** dem Betrieb, das du gerade angesprochen hast, Alex, aus Architektur, was, was ich immer,

**[00:35:50]** kriegst du ja eine so umfassende Feedback-Schleife für deinen Regelpreis, wie du sie zu Fuß überhaupt

**[00:35:57]** nicht bekommen kannst und von so Sachen wie die Anforderungen, die dieses Regelwerk bis

**[00:36:03]** in die Entwicklung stellt, also CQ-Coding, System-Herrtung, Patchmanagement, das kannst du auch

**[00:36:09]** alles agentisch umsetzen und über Agenten in deinen Code, in deinen Betrieb einfließen lassen.

**[00:36:14]** Das ist unsere große Baustelle, die dieses hier ansteht, das alles mal zu durchdenken und

**[00:36:21]** so zu implementieren, dass es auch zeitgemäß ist.

**[00:36:24]** Ich sehe halt eine Herausforderung beim Thema Überprüfung.

**[00:36:31]** Manche nennen das auch Guardrails, dass du halt sagst, wenn ich irgendwo Agenten einsetze,

**[00:36:37]** dann möchte ich halt prüfen, dass die auch in die Richtung arbeiten, die wir mal gesetzt

**[00:36:44]** haben und dass die vielleicht nicht so, also nicht wie der gute Waffenhändler, beide Seiten

**[00:36:51]** beliefern. Bei euch prüfen und dem Angreifer was in die Hand rücken. Ja ja, schon klar.

**[00:36:56]** So ungefähr. Ja, aber ich finde halt, dass das Beispiel bei OpenClaw halt ganz interessant

**[00:37:06]** von der Architektur her, du kannst ihm ja zum Beispiel Schreibzugriff auf seine, seine

**[00:37:12]** Kerndateien, also Soul, MD, Identity, kannst du ihm ja sperren, dass er die nicht bearbeiten darf.

**[00:37:19]** Also Dateisystemzugriff. Und solche, so was sind halt harte Grenzen, wo du sagst so und das kannst

**[00:37:28]** du selber nicht manipulieren. Du darfst deine Konfiguration nicht umschreiben und spätestens

**[00:37:33]** auf der obersten Ebene möchtest du halt, möchtest du halt irgendwie, ich sag mal,

**[00:37:38]** Metaprüfprozessen, Qualitätssicherungsprozess haben, der kontinuierlich über deine Agenten

**[00:37:44]** drüber geht und schaut, halten die sich an die Rahmenbedingungen, die wir ihnen gesetzt haben,

**[00:37:49]** haben sie die Rahmenbedingungen irgendwo manipuliert, zahlen die noch aufs Unternehmensziel ein,

**[00:37:55]** arbeiten die gerade eigentlich oder sind die in so einem Deadlock, wo sie sich gegenseitig die

**[00:37:59]** ganze Zeit bestätigen und eigentlich nur Token verbrennen. Diese Meta-Ebene, manche nennen

**[00:38:06]** das Agent-Orchestration-Platform, manche nennen das Developer-Management-Platform, wie auch immer.

**[00:38:12]** Ich denke, diese Meta-Ebene, dass du sagst, da hast du eine Möglichkeit, die Agenten,

**[00:38:20]** die bei dir laufen, zu überprüfen. Und gar nicht im Sinne von, da ist eine Instanz one thing to

**[00:38:27]** rule them all, sondern, dass du schaffst halt eine, im Endeffekt eine Infrastrukturkomponente,

**[00:38:33]** wo man das prüfen kann, das ist aus meiner Sicht so die Herausforderung, vor der wir gerade stehen.

**[00:38:38]** Und nein, niemand hat das Wort enterpreisiert.

**[00:38:40]** Ja, genau.

**[00:38:41]** Wenn das auch nur die einzige Herausforderung wäre, vor der wir stehen.

**[00:38:45]** Was würdet ihr denn Leuten mitgeben, wie sie sich jetzt, ich sage jetzt mal auf diese

**[00:38:50]** neue Zukunft vorbereiten oder diese Reise mitgehen?

**[00:38:55]** Also ich denke mal vor, vielleicht findet ihr, was, womit ihr einsteigen wollt, ich

**[00:39:00]** Ich würde einfach mal sagen, naja, wenn der jetzt etwas gesagt hat, da ist das Thema quasi schon vergeben und dann freut man sich über andere Informationen von den Gästen.

**[00:39:09]** Daher lege ich vor, dass ich möchte im Grunde auf das Aussetzen, was Klaus mit der iOS-Entwicklung und dem Veröffentlichen von Dokumenten mal gesagt hat, also mit Büchern und Artikeln.

**[00:39:20]** Ich bin der Meinung, er glaubt, dass seine Expertise ihn unersetzbar macht.

**[00:39:24]** macht, der hat die Dynamik nicht verstanden. Die KI, vor die KI uns jetzt setzt. Das heißt,

**[00:39:31]** ich bin Experte auf einem Thema. Hier bitte das Experten-Tum eintragen. Ist nichts, was tragfähig

**[00:39:39]** ist für die Masse als Aussage. Es wird sicherlich Ausnahmen geben, wo Menschen irgendwie aufgrund

**[00:39:46]** einer gewissen Expertise irgendwie noch hervorstechen. Aber ich würde eher darauf drängen, dass

**[00:39:52]** euch darauf ein, versucht das Zeug zu nutzen, entweder um noch besser zu werden oder um gemeinsam

**[00:40:00]** mit KI Multiplikationseffekte zu bewerkstelligen. Was habt ihr denn noch so vielleicht, was ihr

**[00:40:07]** mitgeben könnt? Also für mich ist das, ich spreche jetzt exzellentwickler, für mich als

**[00:40:14]** Seniorentwickler, wo ich insbesondere die Anzahl meiner Lebensjahre meine, natürlich auch damit die

**[00:40:20]** Anzahl der Jahre, in denen ich Erfahrung sammeln konnte. Für mich ist KI ein Superboost. Also es ist

**[00:40:25]** nicht so, dass ich das, was ich jetzt... Also ich hatte, ich glaube am Wochenende war es, da

**[00:40:30]** hatte ich vier Cloud Sessions offen und habe vier iOS Apps parallel gebaut. Das kann man jetzt

**[00:40:37]** auch ohne jegliches Fach wissen, nur an dem ersten Punkt, an dem es nicht funktioniert und das

**[00:40:42]** ist bei iOS dann unweigerlich Co-Signing, stehst du da. Dann fängst du an, dann ist das

**[00:40:47]** Projekt gelaufen. Und mit der Erfahrung, die ich in dem Bereich habe, kann ich eigentlich komplett,

**[00:40:53]** ohne Unterbrechung von der Spezifikation bis das Ding steht bei AppStoreConnect zum Beta-Testen,

**[00:41:00]** bei TestFlight, kann ich das durchziehen. Also ich kann meine Expertise nutzen, um die Vorteile

**[00:41:07]** der KI, also diese enorme Verarbeitungsgeschwindigkeit, ja quasi als verlängerte Werkbahn zu verwenden.

**[00:41:14]** und ich gebe mich der Illusion hin, dass das auch in Zukunft zu sein wird. Man muss ja nicht

**[00:41:22]** mit der KI konkurrieren. Ich muss jetzt nicht mehr dasselbe programmieren, aber ich verstehe

**[00:41:27]** grundsätzlich wie so eine iOS App aufgebaut ist. Ich verstehe grundsätzlich, wann man jetzt Core

**[00:41:34]** Data benutzen sollte oder wann man auch irgendwas in der SQL-Lite-Datenbank packt oder in der

**[00:41:39]** Textertei oder wie auch immer. Ja, die KI wird da immer besser, aber manche Dinge, gerade wenn man

**[00:41:46]** Software für Menschen baut, sind halt mich immer trennscharf, digital zu beantworten. Wie das in

**[00:41:55]** zwei Jahren aussieht, keine Ahnung. Im Moment geb ich mich noch der Illusion hin, dass ich quasi

**[00:42:00]** als der Orchesterator der vielen Agenten hier da rumlaufen, die gut im Griff habe. Aber ich

**[00:42:07]** Ich möchte auch nicht ausschließen, dass dieses Wissen auch in zwei Jahren vollkommen ersetzt werden kann.

**[00:42:13]** Es muss sich doch keine Gedanken mehr drum machen.

**[00:42:15]** Es fragt sich, was aus der schönen WWDC dann, wenn wir uns nur noch Werbevideos angucken,

**[00:42:23]** von Herr Force One und den Rest, die Agenten machen lassen.

**[00:42:27]** Heute sind so viele Insider drin.

**[00:42:30]** Es ist unglaublich.

**[00:42:32]** jetzt schon wieder auf die Kommentare wo es dann heißt entweder es war sehr nerdig oder viele

**[00:42:37]** Fachbegriffe oder keine ahnung was wäre es eigentlich her force one das kann man googeln das ist

**[00:42:44]** dieses alte let me google it for you gibt es leider nicht mehr aber keine ahnung chatty chatty

**[00:42:50]** chatty wir nennen das einig ne chatty chatty ist ja klippi war die ja der folginger

**[00:42:58]** Ja, vom Co-Pilot und damit bin ich da auch mit meiner persönlichen Bootfüllung raus.

**[00:43:02]** Alex, ich versuch das noch zu retten.

**[00:43:05]** Du musst jetzt noch irgendwas Intelligentes vom Stapel lassen.

**[00:43:08]** Du, das ist nicht nur die, sagen wir schnell, das ist nicht nur deine persönliche Einschätzung.

**[00:43:18]** Ich glaube, das ist eine allgemein bekannte, wie soll ich sagen, Einschätzung der Value-Contribution

**[00:43:25]** der Microsoft-Eigene KI.

**[00:43:28]** Keine Ahnung, was die Kollegen gemacht haben, ist schade.

**[00:43:31]** Genau, ich habe drei Punkte, die ich die Leuten mitgeben würde.

**[00:43:36]** Und das erste ist etwas, dass ich vom Lieben Klaus selber

**[00:43:41]** erst mal so ins Gesicht gefärfert bekommen musste.

**[00:43:44]** Don't assume, du.

**[00:43:45]** Also striff keine Annahmen fürs Aus.

**[00:43:47]** Ärmel hoch, konkrete Use Cases ausprobieren.

**[00:43:50]** Keine Angst, sondern ich habe am Ende gesagt, OK,

**[00:43:54]** dann nehme ich mir jetzt einen separaten Rechner,

**[00:43:56]** weil ich habe Schiss, dass meine Daten geklaut werden. Also nehme ich mir einen

**[00:43:59]** separaten und überlege mir, okay, was sind denn Sachen, die mich so im Alltag nerven?

**[00:44:06]** Oh ja, diese PDFs aus irgendwelchen E-Mails rausziehen und dann das Vorbereiten

**[00:44:12]** für die Steuererklärung. Also jeder hat irgendwo so Use Cases, wo du sagst,

**[00:44:16]** jetzt wollte ich immer schon mal automatisieren. Ärmel hochkrempeln,

**[00:44:21]** machen. Weil nichts, nichts gibt so viel wie das zu machen. Das zweite ist, wenn du das tust,

**[00:44:29]** durchdringe die Muster. Sowas wie Skills, Plugins, Validation Loops sind MCP. Kannst

**[00:44:38]** dir jetzt sagen, ja das ist alles von Anthropic, aber ja und gleichzeitig das, was wir in

**[00:44:45]** in OpenClaw gesehen haben, an Mustern, also würde ich jetzt sagen, war vorher nicht so

**[00:44:51]** ganz so bekannt, mittlerweile gibt es jede Menge Frameworks, die darauf aufsetzen.

**[00:44:55]** Das sind Dinge, wenn man die verstanden hat, dann versteht man besser, wofür ist so eine

**[00:45:01]** Technologie überhaupt nutzbar und wofür halt nicht, übrigens genau das Gleiche für

**[00:45:05]** LLMs, wer immer noch meint, LLMs müssen wir aber dahintrainieren, dass die 100%

**[00:45:10]** deterministisch sind, der hat nicht verstanden, was das für eine Technologie ist.

**[00:45:13]** Und das Dritte ist ohne und steuere den Datenfluss. Also wisse, wem du wann, wo welche Daten gibst

**[00:45:23]** und wo die hingehen. Es gibt dafür keine Entschuldigung mehr zu sagen, ja, aber ich habe gedacht,

**[00:45:30]** die Daten bleiben auf meinem Rechner, weil ich habe doch die App bei mir auf dem Rechner

**[00:45:33]** installiert. Sorry, nee, das ist Ignoranz und Ignoranz sollte nicht bezahlt werden.

**[00:45:40]** wird es aber schwierig, wenn du sagst, do it und jetzt denke ich auch Tanja, ihr habt,

**[00:45:45]** hat mir glaube ich schon mal darüber gesprochen, dass ich gefragt habe, wie würdet ihr das

**[00:45:48]** denn tun?

**[00:45:49]** Einmal im Monat muss ich meine, aus den Emails meine PDF-Rechnungen rauspokeln und muss

**[00:45:55]** dann irgendwie bei Microsoft mir noch meine Rechnung abholen, bei den anderen Providern

**[00:45:59]** zusammenstellen, mit Contour Auszüge abgleichen und an die Beratung schicken.

**[00:46:04]** Würdest du dem Open Cloud denn auch jetzt sagen, ruhig ruft mal meine Contour Auszüge

**[00:46:08]** ab?

**[00:46:09]** Ja, ne. Sind die zugegenst zu meinem Ordnern Banking?

**[00:46:12]** Ne, ich bin ja nie wahnsinnig, aber ich kann dem Jahr ein Teil CSV-Export aus meiner Banking App geben, dass er das aufbereitet.

**[00:46:23]** Aber weniger. Ja, aber vielleicht...

**[00:46:27]** Ne, es geht ja nicht um Schwarz-Weiß, es geht darum, was... Also alleine, dass ich mir...

**[00:46:35]** Jeder von uns hat ja wahrscheinlich irgendwelche Apple Subscriptions.

**[00:46:39]** Wir haben auch Android-Zuhörer.

**[00:46:41]** Es könnte sein, dass jemand so einen Spotify auf Android hat oder so, ja?

**[00:46:44]** Also, ich würde den Podcast so machen, Mark.

**[00:46:49]** Das mag sein.

**[00:46:51]** Ich will damit sagen, ich kriege von Apple immer diese wunderschönen E-Mails und ich,

**[00:46:55]** also ich kann es schon nicht mehr an zwei Händen abzählen,

**[00:46:58]** wie viele Diskussion ich mit Finanzamtsmitarbeitern hatte.

**[00:47:01]** Ja, dann rufen Sie doch mal bei Apple ab.

**[00:47:03]** Keine gültige Steuerrechnung.

**[00:47:05]** Könnte sich ein Openclaw machen, so wisst man drauf, ihr lernetzt.

**[00:47:08]** Ja, aber da könntest du halt hingehen und sagen, okay, du leidest das vielleicht auf ein zweites Mail-Postfach weiter, da kannst du dann Openclaw oder...

**[00:47:15]** Ja, ich habe jetzt solche, diesem Craft-Agent gesagt, du, ich habe hier auf dem Mac, ich habe hier Mail, ich habe hier Kalender, ich habe hier Erinnerungen.

**[00:47:23]** Und dann fing das Ding an und hat mir ein MCP-Server dafür gebaut, der auf meinem Rechner läuft und

**[00:47:28]** ich kann jetzt quasi mit einem LLM meiner Wahl, mit meinen Daten chatten. Ist das eine gute Idee?

**[00:47:34]** Ja, ich glaube zumindest mal, dass das ein guter Versuch war. Aber wie du schon vorhin sagtest,

**[00:47:40]** nach dem Motto, die Daten hinfließen, das ist natürlich auch in Zeiten von AI nochmal eine

**[00:47:46]** Nummer härter, weil du hast ja nicht nur die Daten per se als dumpfe Information, sondern

**[00:47:53]** so ein AI-System hat. Die Memory von dir, also nicht von dir, sondern durch die Arbeit,

**[00:47:58]** die es mit dir vielleicht zusammen hatte, kann viel mehr Zusammenhänge schneller erkennen,

**[00:48:02]** als es dir eventuell möglich war. Von der Seite, ja, auch spannender, aber ausprobieren,

**[00:48:08]** ausprobieren, ausprobieren. Also, als du deinen Case da geschildert hast mit hier,

**[00:48:11]** eine Ahnung, einmal im Monat dachte ich mir gut, aber das ließ sich damit wunderbar lösen.

**[00:48:16]** Ja, aber du hast mir eine total altbackende Empfehlung jeweils gesagt. Benutzt N8N,

**[00:48:21]** das ist ja auch nicht. Moment, N8N habe ich heute nicht gesagt, das hat mein altes Ich gesagt,

**[00:48:27]** mein heutiges Ich sagt, nimm Craft-Agent, also Alter, hast du mal gesehen, wie viel

**[00:48:32]** Ja, ich finde, dass wir tatsächlich, das finde ich wirklich, das fällt sich immer so pathetisch

**[00:48:40]** irgendwie an.

**[00:48:41]** Wenn du denkst, du hast ein Berg gesehen und erklummen, weil eine neue Technologie da ist,

**[00:48:46]** also eine neue Art von Lösung in diesem AI-Sektor, und dann denkst du, ja, das hast du nicht

**[00:48:51]** erklummen.

**[00:48:52]** Jetzt geht es weiter, jetzt geht es Richtung Sonnenschein, keine Ahnung, Skiapphang, irgendwas

**[00:48:57]** hübsches und dann kommt auf einmal so ein neuer Berg hoch, weil, oh, jetzt gibt es eine neue

**[00:49:02]** Technologie und verdammter Arx, das, was ich eben bisher die ganze Zeit mich beschäftigt habe,

**[00:49:05]** auch das ist etwas, wo wir, glaube ich, lernen müssen und zugehen.

**[00:49:10]** Man sagt ja schon immer an der IT, das geht immer alles so schnell, aber in dieser

**[00:49:15]** Geschwindigkeit, das ist neu für mich.

**[00:49:17]** Also das ist auf die IT-ler neu, ne?

**[00:49:19]** Ja, das meine ich.

**[00:49:21]** Oh, Alex sieht es nicht.

**[00:49:23]** Ja, ja, und gleichzeitig, gleichzeitig, nee, ehrlich nicht, weil ich kann euch nicht sagen,

**[00:49:34]** wenn ich das letzte Mal, wenn ich das letzte Mal so ein zehenseitiges Tutorial gelesen habe

**[00:49:39]** oder noch mehr.

**[00:49:40]** Also, was ich halt faszinierend finde, jetzt seit irgendwie zwei Jahren, also im Prinzip

**[00:49:47]** seit ich den, den, oh naja, so länger scheint. Also seitdem ich den LGBT-Account habe, du

**[00:49:55]** kannst ja mit der KI über die, über die Anwendungsmöglichkeiten checken. Und das ist

**[00:50:00]** ganz oft, verhaut sich das Ding nochmal mit einem Dracen, aber es gibt ja halt Referenzen,

**[00:50:05]** wo du nachgucken kannst. Und das finde ich ein unschätzbaren Vorteil, dass du mit

**[00:50:11]** der KI die KI troubleshooting kannst. Ja, nichts ist so, trotz wird die Geschwindigkeit

**[00:50:16]** der trotzdem immer schneller. Und das hatten wir in dieser Taktung nicht. Da gab es mal

**[00:50:21]** oh, jetzt haben wir Op-Pack und rote Programme erfunden. Jetzt haben wir das WBW erfunden.

**[00:50:26]** Jetzt kommt Javascript. Dann kam die Blockchain, aber das war alles so. Und jetzt ist es ein

**[00:50:35]** Wochen-Takt oder, sagen wir mal, im Monatstag. Das finde ich schon sehr krass. Also die

**[00:50:40]** Anforderungen an das Anlaming, die sind schon enorm.

**[00:50:43]** Die passen.

**[00:50:44]** Kennt ihr noch diese Sendung aus den 80ern?

**[00:50:50]** Es war einmal der Mensch mit diesem Trailer.

**[00:50:53]** Was ist Zeit?

**[00:50:54]** Ich habe dann nur mit Greibern geguckt, ich bin ja leid, Leute.

**[00:50:57]** Was ist Zeit?

**[00:50:58]** Da könnte ich aus der Dose Spreichhölzer im Auto bauen, ihr nicht.

**[00:51:02]** Hä?

**[00:51:03]** Das war Ende der 80er.

**[00:51:04]** Ich meine, Anfang der 80er.

**[00:51:05]** Greibern jeden bedrohen können, dann war dann eine Büroklamate, also von der

**[00:51:08]** Seite.

**[00:51:09]** Ich bin jetzt mal einfach so frech mit Blick auf den Timer.

**[00:51:12]** Ich mache ein Abbinder, weil Klaus hatte mir so ein schönes Bild in Vorbereitung geschickt.

**[00:51:18]** Klaus ist schon in Continent, wo hast du ein Abbinder?

**[00:51:21]** Na ja, Klaus sitzt, von der Seite krieg ich das im Bild nicht mit.

**[00:51:25]** Ja, das muss ich doch explizit machen, von dem habe ich mir persönlich explizit gemacht.

**[00:51:30]** Er hat ein schönes Bild geschickt, so nach dem Motto, sinngemäß, wer braucht schon ein Skript.

**[00:51:34]** Ja, wir haben uns einigermaßen daran gehalten.

**[00:51:38]** Ich bedanke mich bei euch, dass ihr da wart.

**[00:51:40]** Alex, du musst mir noch den Link zu deinem Podcast schicken,

**[00:51:43]** damit ich den die schon noch reinknallen kann.

**[00:51:44]** Das würde ich dich total gerne tun.

**[00:51:46]** Ich bedanke mich bei allen, die zugehört haben.

**[00:51:47]** Danke, dass ihr da wart.

**[00:51:49]** Wenn es euch gefallen hat, lasst uns ein Like da.

**[00:51:51]** Wie gesagt, wenn ein Bot zugehört haben sollte,

**[00:51:53]** abonniert gern den Kanal und macht ein Spam auf allen Kanälen,

**[00:51:56]** damit möglichst viele diesen Podcast sich anhören.

**[00:52:00]** Ich bedanke mich bei euch.

**[00:52:01]** Und falls der Jens zuhört, können alle auf...

**[00:52:04]** Moment, Moment, Moment.

**[00:52:05]** So, so kommt es jetzt aber nicht nach.

**[00:52:07]** Genau.

**[00:52:08]** Nein.

**[00:52:09]** Es ist aber jetzt philosophisch sehr interessant, weil du sagst ja jetzt für alle, die sich

**[00:52:13]** das angehört haben, aber sie haben es ja noch nicht angehört.

**[00:52:15]** Ich weiß.

**[00:52:16]** Ja, aber sie werden es sich angehört haben, ist das nicht Futur 2?

**[00:52:21]** Das hört sich so an wie bei mir zu Hause, da haben nämlich gerade die Kids nicht Fähen,

**[00:52:25]** sondern Schulcamp für die Abschlussprüfung des Schuljahres.

**[00:52:28]** Von, da möchte ich jetzt nicht darauf eingehen, ja.

**[00:52:30]** Schulausbildung ist ein anderes Thema.

**[00:52:32]** Ich wünsche euch eine gute Zeit.

**[00:52:35]** Ich bedanke mich, dass ihr da wart.

**[00:52:37]** Ciao. Tschüss.

**[00:52:40]** Danke euch. Ciao.

**[00:52:43]** Willkommen bei Think Different, Think AI,

**[00:52:46]** den Podcast von Mark und Jens.

**[00:52:49]** Zwei technologieverliebte Köpfe,

**[00:52:51]** die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:52:55]** Hier gibt es klare Einordnungen, echte Praxiseinblicke

**[00:52:59]** und einen frischen Blick auf das, was möglich ist.

**[00:53:02]** Verständlich, kritisch und immer mit einem Auge zwingt er.

**[00:53:06]** K.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
