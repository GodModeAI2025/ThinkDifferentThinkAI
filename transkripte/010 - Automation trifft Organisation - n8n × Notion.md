---
title: "Automation trifft Organisation: n8n × Notion"
episode_index: 10
published: "Sun, 19 Oct 2025 02:55:00 +0000"
duration: "4253"
audio_url: "https://audio.podigee-cdn.net/2160435-m-68cc27d9dd04b9b4b792179852421201.mp3?source=feed"
guid: "06f4724a07d5e8732afbee5ef860252b"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-04-28T20:34:41+00:00"
---

# Automation trifft Organisation: n8n × Notion

**Veröffentlicht:** Sun, 19 Oct 2025 02:55:00 +0000
**Dauer:** 4253
**Audio:** https://audio.podigee-cdn.net/2160435-m-68cc27d9dd04b9b4b792179852421201.mp3?source=feed

## Beschreibung

Wie Notion und KI unseren digitalen Alltag revolutionieren – ein Crossover-Gespräch voller Aha-Momente.
In dieser (Crossover) Episode diskutiert  Mark Zimmermann (leider ohne Jens) und unser Gast  Dirk Beckmann die Entwicklungen in der digitalen Welt, insbesondere die Rolle von Notion und KI in modernen Arbeitsabläufen. Sie beleuchten die Funktionen von Notion, die Integration von KI und die praktischen Anwendungen in Agenturen. Die beiden teilen persönliche Erfahrungen und Einsichten über die Herausforderungen und Möglichkeiten, die diese Technologien bieten. In dieser Episode diskutieren Dirk Beckmann und Mark Zimmermann die Rolle von Agenten in Notion, die Integration von KI und Automatisierungstools wie N8N sowie die Zukunft von Notion in der digitalen Welt. Sie betonen die Bedeutung von Masterprompts und individuellen Anpassungen, um die Effizienz und Produktivität zu steigern. Die beiden Experten teilen ihre Erfahrungen und geben wertvolle Tipps für den Umgang mit Notion und KI.

Gast: Dirk Beckmann

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** KD zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:29]** Herzlich willkommen bei der neuen Ausgabe von ZinkDiffinZink AI.

**[00:00:38]** Heute wird es agentisch, heute wird es ein bisschen mit Workflows zu tun haben und

**[00:00:42]** heute ist es ohne Jens, aber dafür trotzdem mit einem sehr kompetenten Gast, der sich

**[00:00:49]** sicherlich auch gleich vorstellen wird.

**[00:00:50]** Ja, willkommen zu einer neuen Folge der digitalen Zeit, meinem Podcast, den ich

**[00:00:57]** in Corona angefangen habe und immer noch sporadisch weiterführe. Heute mit einer

**[00:01:02]** besonderen Folge, Mark hat sie eben Crossover genannt und mag das der Name des Gastes in

**[00:01:07]** dieser Folge, die digitale Zeit heute mit Themen wie Notion, N8N, Workfloss und dem allgegenwärtigen

**[00:01:17]** Thema KI. Willkommen, Mark. Ja, willkommen, Dirk. Ich fand die Idee tatsächlich mit so einer

**[00:01:23]** Cross-Over-Folge bindert verrückt, aber wenigstens sind unsere Podcasts, können wir halten und

**[00:01:28]** schalten. Wie der Dachdecker, wie wir es so wollen. Ich habe angefangen, also frage ich

**[00:01:33]** zuerst, Mark, so kurz was zu dir erzählen, bevor ich mich vielleicht bei euch auch vorstellen darf.

**[00:01:38]** Ja, sehr gerne. Ich bin Dirk, ich bin Geschäftsführer und Gründer von Art und Weise,

**[00:01:44]** beruflich seit über 35 Jahren mit der digitalen Zeit, so wie dieser Podcast heißt, beschäftigt

**[00:01:50]** Und immer wieder passieren neue Dinge und ich werde euch jetzt nicht 35 Jahre nach erzählen, aber die letzten, sagen wir zwei Jahre, sind doch recht beeindruckend und stellen alles in den Schatten, was wir davor erlebt haben, finde ich zumindest.

**[00:02:06]** Und speziell mit meinem Sonderthema Notion, wo Spoiler, ich sagen würde, diese Marke und dieses Unternehmen finde ich so toll wie Apple und das will was heißen.

**[00:02:17]** Speziell mit diesem Thema und KI ist das wirklich eine tolle Sache, dass wir uns heute hier sehen.

**[00:02:23]** Also ich bin sozusagen im echten dem Geschäft zu einer Digitalagentur namens Art und Weise,

**[00:02:28]** 60 Mitarbeitende in Bremen und jetzt zu dir Mark, wer bist du denn eigentlich?

**[00:02:33]** Ja, also für die Hörer deines Podcasts, Mark Magzerman, ich bin bei der NBW angestellt,

**[00:02:41]** verantwortet dort alles, was das Thema Mobile Loss Entwickler angeht, also alle Apps für

**[00:02:46]** Entkunden für den internen Einsatz. Ich mache das jetzt schon seit 2009.

**[00:02:51]** Man wird irgendwie auch nicht jünger, also der Spruch alteweise graue Männer

**[00:02:55]** stehen vorne und versuchen die Welt zu erzählen, trifft das Schüler auf mich zu.

**[00:02:58]** Ein Job ist hauptsächlich, ich sag mal, die Politik im Hintergrund, die Ideen

**[00:03:03]** für neue Produkte bei uns im Konzern für mobile Endgerät umzusetzen und so wie

**[00:03:08]** du gesagt hast vor zwei Jahren ist ein bisschen, was passiert ist bei mir

**[00:03:10]** eigentlich mehr so der Jahresanfang gewesen, nämlich dieses Thema

**[00:03:14]** Seit dem Tag kommt ja so etwas Neues am Horizont, nennt sich KI, was ist denn damit alles möglich?

**[00:03:21]** Und vielleicht, du hast vorhin schon die Vorschau quasi gebracht, dass wir auch über Notion reden werden.

**[00:03:27]** Vielleicht ein lustiger Funfact.

**[00:03:30]** Dirk und ich sind verwandt.

**[00:03:33]** Wir gehören demselben Stammbaum an, muss man dazu sagen.

**[00:03:37]** und früher hat Dirk sich sehr viel schon mit App-Rechtern beschäftigt und ich habe damals ein bisschen Schmunzeln geguckt,

**[00:03:47]** weil ich war doch mehr so in der Microsoft-Windows-MCSE-Ausbildung, Windows NT als Betriebssystem.

**[00:03:54]** War ich mehr zu Hause, bis ich dann irgendwann mal aufs Macbook mikriert bin und mir seitdem nichts Besseres vorstellen konnte,

**[00:04:02]** als den Mac zu benutzen, was dann auch später durchaus maßgeblich auch mit meinem Job zu tun hat.

**[00:04:09]** Ich meine, wer weiß, was ich tue, mit welchen Firmen ich interagiere, welche Lösungen ich baue,

**[00:04:14]** wozu ich erzähle, das ist doch alles sehr Apple-lastig. Und irgendwie wiederholt sich Geschichte.

**[00:04:20]** Nicht, dass mir die Mode von damals passt, also das definitiv nicht.

**[00:04:25]** Weder vom Leibesumfang noch, also ich sage jetzt mal, optisch würde es mir vielleicht auch nicht stehen.

**[00:04:30]** Nein, mit Notion hat sich durchaus auch etwas Ähnliches ergeben und N nach N, weil das sind

**[00:04:37]** durchaus noch verspannene Dinge, von denen ich hoffe ich auch noch ein bisschen etwas von dir

**[00:04:39]** höre heute, wo ich auch sehr viel von dir lerne und lernen kann, weil du ja ein sehr starker

**[00:04:44]** Notionverfechter der rechtig der Weise bist. Ja, das ist schön, dass du das sagst, weil ich

**[00:04:50]** will gleich mal disclaim für alle, die aus meiner Firma, die diesen Podcast dann irgendwann

**[00:04:55]** hören. Ich fühle euch, ich liebe euch alle, aber dass ich jetzt so total nördig bin auf Notion und

**[00:05:03]** das euch manchmal nervt. Wie gesagt, das verstehe ich. Ich finde das auch, wir arbeiten daran.

**[00:05:08]** Es gibt viele Leute mittlerweile, die mich unterstützen, damit das besser wird. Aber

**[00:05:13]** Notion ist das Stück Software, das nach so vielen Jahren digitale Zeit mich wirklich in den

**[00:05:20]** Bann gezogen hat seit Jahren jetzt. Und ich muss wirklich sagen, dass, was da, was damit

**[00:05:25]** möglich ist, aber vor allem, was die Vision von dem, von dem, von dem Hauptgründer, sage

**[00:05:30]** ich jetzt mal, Ivan Sao ist, ist einfach Wahnsinn, nämlich mein Lieblingsspruch, nämlich

**[00:05:36]** alles ist mit allem verbunden, ist da drin. Und vor ein paar Wochen kam dann irgendwie

**[00:05:40]** narschend 3.0, also diese KI-Version, über die jetzt durchaus ein paar Leute reden

**[00:05:45]** raus. Und das hat dem Ganzen jetzt die Krone aufgesetzt. Aber darüber reden wir

**[00:05:48]** Also, ja, vielen Dank. Ich sage jetzt mal was aus meiner Sicht. Vielen Dank, dass du da bist.

**[00:05:52]** Wir waren ja schon mal zusammen mit meinem Podcast, und dann waren wir, glaube ich,

**[00:05:55]** noch nicht zusammen. Nee, einem Premiere ist für dich und für mich. Und umgekehrt,

**[00:06:00]** man erinnert sich an das Bild mit der Apple Vision Pro. Das ist das Cover von dem Podcast mit dir.

**[00:06:06]** Und ich freue mich auf heute Abend. Ich finde, dass du eben gesagt hast,

**[00:06:10]** da war auch schon etwas drin, was viele gerne vergessen, wenn sie sich über

**[00:06:15]** für KI-Systeme unterhalten und keine Sorge, das wird hier jetzt keine zu starker Abschweifung,

**[00:06:20]** ist nämlich das Thema Mensch. Also zwischen du hast einen Tun, du hast ein Werkzeug zur

**[00:06:24]** Hand, mit dem du etwas tun willst, aber was nützt dir das beste Werkzeug, wenn du niemand

**[00:06:28]** hast, der mitmacht. Also wer das vielleicht schlecht findet, von der Seite finde ich auch

**[00:06:33]** den Punkt, dass man vielleicht auch mal im Guten, wie im Schlechsten auch mal sagt,

**[00:06:37]** so nach dem Motto, worauf stoßen wir denn, wenn wir Technologie auch noch in dieser

**[00:06:41]** Art und Weise, die so mit Hype verknüpft wird in Form von das ist das Seelenheil oder der

**[00:06:46]** Untergang der Menschheit, je nachdem wen du das fragst, dass man sich damit auch mal vielleicht

**[00:06:51]** zwei, drei Sätze nachher noch mal vielleicht beschäftigt. Aber du sagtest Notion, kannst

**[00:06:56]** du mir oder den Zuhörern wahrscheinlich am besten mal kurz erklären, was ist eigentlich

**[00:07:00]** Notion? Ja, gute Frage. Notion ist ein cloudbasierte App, also ein Dienst, an dem man sich

**[00:07:07]** zunächst mal, wenn man will kostenlos anmelden kann, der vieles ist. Also eine Datenbank,

**[00:07:13]** ein Notizzettel-Tool, ein Projektmanagement-Tool, ein Wiki, eine Wissensdatenbank und so

**[00:07:21]** weiter und so fort. Aber vor allem ist Notion die Möglichkeit, dass fast jeder Mensch,

**[00:07:27]** der so ein bisschen mit dem Computer sich zurechtfindet, sein eigenes Umfeld, sein

**[00:07:34]** eigenes, wie will ich meine Daten pflegen? Wie will ich mich selber organisieren, um Feld

**[00:07:38]** sich bauen kann? Und diese Idee, dass jeder und jeder sein ihre Welt bauen kann, das ist

**[00:07:47]** eigentlich die Grundidee von Notion gewesen, als sie angefangen haben. Dann hat die KI und

**[00:07:53]** die KI-Revolution sozusagen Notion begleitet, schon relativ früh. Man muss auch sagen die

**[00:07:58]** ersten KI-Versionen, die Notion eingebaut hat, die waren so, boah ja, ne, dann gehe ich

**[00:08:02]** lieber zu chat GPT. Das war alles noch nicht so richtig geil. Und jetzt ist es eben die

**[00:08:08]** ultimative App, wenn ich quasi mich nicht für KI interessiere aus technischer Sicht, sondern

**[00:08:14]** nur aus Ergebnissicht. Und das ist auch dieses Thema, was ich mit Apple habe. Apple hat

**[00:08:19]** ja ganz oft in den Vordergrund gestellt, was ist das, was ich damit tun kann. Macht

**[00:08:24]** demokratisierbar die Möglichkeit mit einem Computer zu arbeiten, baue den Mac, diesen

**[00:08:29]** kleinen Kasten und macht eine Maus dran und das hat schon noch einmal kann jeder Mensch

**[00:08:34]** so ist die Vision damit arbeiten.

**[00:08:37]** Apple hat 1984 etwas vorgestellt, dass ich fast genauso, nee, dass ich genauso revolutionär

**[00:08:43]** finde, wie die 3.0 Version von Notion, nämlich die Möglichkeit in diesem Zeitalter KI für

**[00:08:50]** mich zu nutzen, ohne tausend Sachen zu können, ohne Agenten und das alles richtig hundertprozentig

**[00:08:56]** zu verstehen.

**[00:08:57]** Ich kann diesem Ding einfach sagen, was ich will und relativ viel davon kann es jetzt schon

**[00:09:02]** tun.

**[00:09:03]** Es ist genauso unperfekt wie der erste Mac, natürlich aus heutiger Sicht, aber es ist

**[00:09:07]** genauso revolutionär, wenn du alles davor siehst für mich.

**[00:09:11]** Handt das ja ganz lustig.

**[00:09:13]** Du, so wie du damals mit deinem, das waren richtig größer hatte dein Macbook, du hattest

**[00:09:18]** doch dieses riesen Ding, dieses Riesenschiff, bestimmt von 15 Zolligen.

**[00:09:24]** Was halt, sagen wir einfach mal der ganz große so und ich fand das immer irgendwie

**[00:09:30]** merkwürdig, wie man mit dem Mac arbeiten konnte und so gings mir auch lange Zeit mit

**[00:09:33]** Notion. Du hast schon lange von Notion erzählt und ich habe es immer wieder mal angeschaut

**[00:09:38]** und ich fand es am Anfang erst mal abstoßend, weil ich sage mal dieses weichste Platt Papier.

**[00:09:44]** Du hast da etwas und du musst dir, ich sage jetzt mal Gedanken machen, wie sie fange ich jetzt an,

**[00:09:48]** habe ich immer gesagt, nee, da fasse ich kein Neff und um keine Ahnung,

**[00:09:51]** Was? Aus heutiger Sicht muss ich sagen, was für eine dumme Geschichte. Ich wäre so froh, wenn

**[00:09:56]** viele Sachen in Lauschen schon drin wären und ich sie mir jetzt nicht importieren müsste,

**[00:09:59]** weil, was habe ich gemacht, anstatt in einem Tool, egal wie gut oder schlecht abgelegt, habe

**[00:10:05]** ich alles in Apple Notizen reingeschrieben. Hab jetzt 3,8 Gigabyte Daten, schöne Grüße gehen

**[00:10:10]** raus, Lauschen hat geschwitzt beim Importieren. Habe ich mir so ein kleines Tool, dass das

**[00:10:14]** das die Notizen exportiert, damit ich sie in Lauschen importieren kann, aber lange

**[00:10:17]** kurzer Sinn. Meine Alternative war ja nicht gut. So, und dann kam tatsächlich dieser

**[00:10:23]** Magische und ich erinnere mich noch, wie du mir geschrieben hast, hier gleiches

**[00:10:26]** Keynote bei Notch. Und dann dachte ich mir so, ja guck an, die haben auch eine

**[00:10:31]** Keynote, das ist ja cool. Schalt mal rein. Und dann machst du diese Keynote auf und

**[00:10:37]** guckst dir das an und denkst ja, ja gut, das ist so eine Mischung aus Apple und

**[00:10:40]** Sam Ordman. Da ist so eine kleine Bühne, da ist ein bisschen

**[00:10:43]** Präsentation dahinter, da wird ein bisschen was erzählt und dann holen

**[00:10:46]** sie dich sehr schnell ab mit dem Thema, was sie mit KI vorhaben bzw. was sie jetzt auch als erste

**[00:10:52]** Funktionalität herausbringen. Und auf einmal warst du nicht mehr in dem Punkt, dass du ein weißes

**[00:10:57]** Blatt Papier selbst beschreiben musst, sondern du konntest ihm sagen, was du willst. Und das

**[00:11:03]** finde ich heute immer noch. Wenn ich Leuten zeige, wie cool ist Notion, dann fragt man so ein

**[00:11:09]** bisschen was, dann gibt es so Dinge, das weiß ich, manchmal interessieren sich dann Menschen

**[00:11:12]** für das Wetter am Urlaubsort oder irgendwas und du gehst einfach in diesen Assistenten rein, sagst

**[00:11:17]** Datenbank anlegen, mit KI gestürzt, schreibst rein, was, keine Ahnung, Urlaubsort, Wetter,

**[00:11:22]** was auch immer. Und dann fängt der an, macht dir eine Struktur-Resenvorschlage, züllt dir die

**[00:11:26]** Wetterdaten schon mal ein. Das ist, also das ist so der erste Moment, wo du bei deinem

**[00:11:31]** Gegend über ein Lächeln siehst und das ist ja, weiß Gott, noch nicht alles, was Notion,

**[00:11:36]** was Snowshin hingeht. Also für mich ist Snowshin seit Diversion und das ist quasi nachguckt.

**[00:11:42]** Ja, wir haben jetzt oben, falls das irgendwann mal einer hört, im Jahr 2025. Das ist noch nicht

**[00:11:47]** so lange her, dass Snowshin 3 rauskam und es gehört zu den Tools, die für mich zu den Top 3

**[00:11:55]** meiner Werkzeugen gehört. Leider nicht im Firmumfeld. Da sind wir ein sehr Microsoft-flastiges

**[00:12:02]** Unternehmen. Es ist ja nicht so, dass ich nicht auch da schon versuche, irgendwie mal noch

**[00:12:07]** Fuß zu fassen mit dem Ding. Aber es ist ein Tool, wo ich sage, das dreht solche Runden um

**[00:12:13]** das, was Microsoft macht. Solche Runden um das, was Google Workspace und wie der ganze

**[00:12:18]** Kram heißt, macht. Es ist so mächtig und aus meiner Sicht, gleich benörd, von Menschen

**[00:12:23]** auch bedienbar und es braucht. Wenn du dann merkst, was für Konzepte entlegen ist,

**[00:12:28]** ist es unglaublich. Ich komme gerade ins Wärmen. Entschuldigung, ich gehe dir gleich

**[00:12:31]** für das Wort, aber als du sagtest, alles sind, was war das hoch? Alles sind Daten, alles ist,

**[00:12:35]** die wollen der Satz? Ja genau, das finde ich so faszinierend, wenn du da in den Assistenten

**[00:12:41]** aufrufst und du machst seinen Adzeichen und du verkniffst die Komponenten miteinander,

**[00:12:45]** du kannst zeilen, du kannst zellen, du kannst tabellen, du kannst Ordner, du kannst Dokumente

**[00:12:52]** miteinander in einer agentischen Anfrage verknüpfen und beeinflussen. Das ist,

**[00:12:58]** Das ist mein Blowing, das überrascht mich jedes Mal, wenn ich das Ergebnis sehe.

**[00:13:04]** Ja.

**[00:13:05]** Und das Verrückte ist einfach, wenn man jetzt sozusagen davor steht, hat man eine Lernkurve

**[00:13:11]** und das ist etwas, was normalerweise auf verschiedene Weisen versucht, seit Jahren zu

**[00:13:15]** lösen.

**[00:13:16]** Mal besser, mal schlechter.

**[00:13:17]** Die haben Features, auch Features gebaut, die schlechter sind, weil sie dann so komische,

**[00:13:21]** so eingebaute Templates, so Wiki Funktionen, so komische Sachen gebaut haben.

**[00:13:27]** niemand will das, die Ambassador raten denen auch die ganze Zeit bitte macht das aus, das will keiner haben, weil ihr müsst das anders lösen mit der Hilfe von Leuten, die Templates bauen oder mit der Hilfe von YouTuber, das ist eine tolle YouTuber zu noschen, ein Deutschen, der sehr, sehr bekannt ist, Matthias Frank aus Berlin, den finde ich aus Deutschland auf jeden Fall am besten, der spricht zwar Englisch, also auf seinen Videos, weil er halt natürlich international sich positioniert, aber das ist einer meiner Lieblings und Thomas Frank aus den USA, ist super und der aller Liebste, den ich habe, ist natürlich Simon.

**[00:13:57]** aus England mit Better Creating. Das ist der, der auch den tollen Agenten gebaut hat. Was

**[00:14:02]** ich eigentlich sagen wollte ist, Notion hat eine Lernkurve, aber es ist sozusagen so ähnlich

**[00:14:09]** wie Demokratie, die Europäische Union und damals auch Apple. Es ist ein bisschen komplizierter

**[00:14:15]** eigentlich. Das ist ein bisschen ungewöhnlicher. Aber am Ende, wenn du dann zurückblickst

**[00:14:21]** darauf, dass du diese Lernkurve durchgemacht hast, dann sagst du, okay, wie konnte ich

**[00:14:24]** ohne Leben. Also wie könnte man ohne ein Apple-Ökosystem leben, wo die Uhr, das

**[00:14:32]** Division Pro, das Tablet, das alles miteinander verbunden ist? Und das hat Apple erfunden.

**[00:14:38]** Wir wissen alle, wie schlecht es war am Anfang, die iCloud und so weiter von Apple.

**[00:14:41]** Zürich du. Ja, zum Beispiel. Ich bin nur noch einsatz, aber bei Norschen ist es genauso.

**[00:14:47]** Ich habe die ganze Zeit immer so ein Gefühl bei Norschen, wie für Apple in den 90ern

**[00:14:51]** gehabt bis 3.0 kam. Okay, ich weiß, für irgendwas ist das gut, dass ich zu Norschen stehe und

**[00:14:57]** ich fand das schon alles immer toll und ich bin total tief drin. Aber mit dem Lounge von vor

**[00:15:03]** paar Wochen muss man wirklich sagen, das ist quasi so wie Think Different, der Spot kommt

**[00:15:08]** raus, Steve kommt zurück und alles wird gut. So ist das Gefühl gerade. Weil es in

**[00:15:13]** diesen ganzen Dingen verbindet. Also sagt das, wir wissen alle noch, wie es früher war,

**[00:15:18]** aber muss ich sagen, falls du noch nicht in den Spiel geguckt hast,

**[00:15:21]** wir sind beide schon älteren Kaliber.

**[00:15:24]** Ich habe letztens Menschen getroffen, die kennen die Einführung des iPhones

**[00:15:29]** nur aus Geschichtsbüchern, weil sie zu dem Zeitpunkt höchstens

**[00:15:32]** im Kindergarten waren, die Zuordnung nicht hatten.

**[00:15:36]** Und die standen dann vor mir mit dem Wissen der Keynote,

**[00:15:39]** die haben dir gesehen gehabt auf YouTube,

**[00:15:41]** und haben mir erklärt, wie das wohl damals war,

**[00:15:44]** als das iPhone rausgab.

**[00:15:45]** Und ich hatte damals, als ich den Mac noch nicht so mochte,

**[00:15:50]** in meinem Arbeitsumfeld einen Kollegen, dem habe ich geholfen,

**[00:15:53]** am Apple Newton eine PCMCA-Karte reinzumachen, um Sachsen zu können.

**[00:15:59]** Weißt du? Und diese Kollegen und Kolleginnen erzählen dir,

**[00:16:02]** wie die Welt funktionierte, als das iPhone rauskam

**[00:16:06]** und bewerten es nur durch den immer noch ikonischen Auftritt

**[00:16:10]** von Steve auf der Bühne, als er sagte, ein iPhone,

**[00:16:13]** Ein Internet-Communication-Device und nur White-Screen-Eye-Port oder andersrum.

**[00:16:17]** Ist ja auch egal, ich bin ja nicht Stief.

**[00:16:19]** Und das finde ich so krass, dass Dinge wie, wenn du sagst,

**[00:16:22]** okay, wie du es früher kennst, ihr kennt die nicht.

**[00:16:24]** Ja, das ist wie, wenn ich meinen Kids irgendwie keine Ahnung,

**[00:16:26]** Wildheim-Telefonen-Hinhalt und die sagen,

**[00:16:28]** hm, das ist ja sehr nett, aber was ist denn das?

**[00:16:30]** Ja, also, was soll ich denn damit an?

**[00:16:33]** Also von der Seite kann man sagen, es war kompliziert.

**[00:16:35]** Und als du sagtest, es ist gewöhnungsbedürftig,

**[00:16:38]** ich würde auch sagen, Notion ist nicht kompliziert,

**[00:16:39]** Notion ist gewöhnungsbedürftig.

**[00:16:41]** Ich hab mich einmal dran gewöhnt, dass du ihm Dinge anvertrauen kannst, dass du was du von ihm verlangen kannst.

**[00:16:49]** Ich behaupte, weiß Gott nicht, dass ich schon alles irgendwie erkannt hab.

**[00:16:52]** Aber auch, als ich zum Beispiel diese Notizen importiert habe, war das total faszinierend.

**[00:16:56]** Du hattest dann nach einmal sechhunderttausend geschülte Einträge, weil die Notizen waren alles andere als cool.

**[00:17:02]** Und dann hab ich ihm gesagt, du pass mal auf, mach mir das bitte in der Datenbank.

**[00:17:05]** Teck es bitte, mach und tu und keine Ahnung was, dann war der wieder und irgendwann hat es so eine Datenbank mit ein bisschen Tagging da dran, bekommt es die original Notiz in der Datenbank öffnen.

**[00:17:16]** Das ist es magie.

**[00:17:19]** Das ist echt ein magischer Moment und ich hatte es ja auch letztens dir mal geschrieben und auf LinkedIn geteilt.

**[00:17:25]** Also wenn Apple mal irgendwann aufs Popping Tour gehen würde, also ganz ehrlich, also egal wer von Apple zuhört, kauft den Laden.

**[00:17:32]** Das macht solche Runden um den ganzen anderen Rest.

**[00:17:36]** Wobei, manchmal sind Dinge, die Apple Caster nachher auch kaputt sehe.

**[00:17:40]** Siri konnte damals auch mehr bevor er die Musik gekauft hat.

**[00:17:44]** Man darf auch nicht vergessen.

**[00:17:46]** Dieser Ivan Sauer ist ein extrem präziser Mensch.

**[00:17:50]** Das ist ein Typ, der ist ein bisschen schüchtern,

**[00:17:53]** der ist nicht wie Steve oder so.

**[00:17:55]** Der wusste genau, was er will.

**[00:17:58]** Diese Gründungs-Stories ist total interessant.

**[00:18:00]** Interessant, weil er hatte dieses erste Notion so als irgendwie so Cloud-Lotids-Dingsbums

**[00:18:05]** dann irgendwie gedacht hat, das gebaut, das war nicht erfolgreich und das hat erst nicht

**[00:18:09]** geklappt und dann ist er mit seinem Kumpel nach Kyoto gefahren, er ist Südkoreaner,

**[00:18:13]** aber er ist trotzdem nach Kyoto, nach Japan gefahren und da haben die sich acht Wochen

**[00:18:16]** eingeschlossen, er ist selber auch Entwickler und haben einfach an dieser Vision gearbeitet

**[00:18:22]** und die Grundidee von Notion ist ja, dass das alles aus Lego-Blocks basiert, also

**[00:18:26]** Das heißt, ein Datenbankeintrag, eine Zeile in Excel ist eigentlich eine Seite und die

**[00:18:35]** nennen intern die Datenbank auch nicht Datenbank, sondern Collection.

**[00:18:39]** Es ist eine Collection of pages.

**[00:18:42]** Das heißt also, du hast hundert Zeilen, das sind die pages und die Datenbank selbst

**[00:18:47]** in Collections.

**[00:18:48]** Und dass du da dann solche Felder hast, wie in einer Datenbank, also Spalten in

**[00:18:52]** Excel gesprochen.

**[00:18:53]** Das ist natürlich notwendig und klar aber du kannst deswegen auch ein ein element auf einer seite adressieren und du kannst halt sozusagen ein ein element markieren und sagen copy gehst irgendwo anders hin und sag sing also paste und dann kannst du fragte dich ob er das sinken soll und dann sinkt er das und dann macht er wie so ein.

**[00:19:13]** Also denn, denn iframed er dieses Element irgendwo hin und jetzt stell dir mal bitte vor, du hast Templates und du hast irgendwo so eine zentrale, dann baust du dir irgendwo diese, diese Grundlagen, packst die in die Templates, wenn du die Templates dann nutzt, dann zünkt er dir das dahin.

**[00:19:29]** Wenn du dann aber bei der Grundlage etwas ändern, geht das durch alle Instanzen hindurch. Das ist total irre und deswegen ist die KI jetzt gerade so irre, weil du nämlich so ein, du hast eigentlich so ein Inception-Ding.

**[00:19:40]** Du kannst jetzt einen Prompt, mit einem Prompt, mit einem Prompt, mit einem Prompt verknüpfen, wenn du das brauchst.

**[00:19:46]** Und das ist eben dieses Grundprinzip dieser, die nennt das Building Blocks, also alles ist ein Block.

**[00:19:52]** Alles ist ein Neoblock.

**[00:19:54]** Also gerade, was du mit deinem iFrame-Beispiel gebracht hast, muss ich das gerade ehrlicherweise zugeben.

**[00:19:59]** Stimmt.

**[00:20:00]** Ich habe den Menüpunkt gesehen und dachte so, hey, wat dillen du da von mir?

**[00:20:04]** Muss ich mir nach der Folge tatsächlich auch nochmal anschauen?

**[00:20:07]** immer noch in dem Augen öffnenden KI-Part, dass ich den Assistenten in der Ecke, aber

**[00:20:14]** auch in den, Entschuldige, wenn ich die falsche Vokabularie wahrscheinlich wähle, in den

**[00:20:19]** Spalten, also Eigenschaften. Versuch es, ich versuch es. Sage zum Beispiel, okay, ich

**[00:20:23]** habe hier Eigenschaften für diese Datenbank oder Sanbello oder wie auch immer und diese

**[00:20:28]** werden vielleicht nicht von Hand gefüllt, weil ich einen Text oder eine Select Mehrfachauswahl

**[00:20:33]** oder so was habe, sondern auch da kannst du sagen, Zölle, diese Eigenschaft mit KI.

**[00:20:37]** Ja, habe ich auch gedacht. Halter Falter, ja? Also, wie krank ist das denn, dass ich in

**[00:20:42]** der Datenbank lege? Also, meine Excel-Zellen sind gemäß und bestimmte Felder füllte halt dann aus,

**[00:20:49]** weil es liegen genügend Daten da und ich habe ihm gesagt, er soll das mit so einer KI-Regel des

**[00:20:54]** Zöllen und dann stehst du da und denkst so, okay, er hat mir gerade Kategorien eingetragen

**[00:20:59]** und abgeleitet aus dem, was sie vorher geschrieben habe.

**[00:21:02]** Er hat gerade keine Ahnung, was gemacht.

**[00:21:04]** Und dann kannst du ja sogar noch hingehen und sagen,

**[00:21:07]** ich füge jetzt auch noch Ansichten drüber und dann habe ich auch immer ein Diagramm

**[00:21:10]** und dann habe ich wieder eine Tabelle und dann habe ich die Tabelle mit Filter.

**[00:21:14]** Und du stehst davor mit offenem Mund und denkst so,

**[00:21:18]** wie viel Arbeit hätte mich alleine das klassischen Bürowerkzeugen gekostet.

**[00:21:24]** Ich bin ja zum Beispiel ein Verfechter von Keynote.

**[00:21:27]** Ja, da sind wir wahrscheinlich, glaube ich, mittlerweile unterschiedlich.

**[00:21:29]** soweit ich das Erinnerung habe, bist du nicht ganz so auf der Keynote-App, auf den App.

**[00:21:35]** Ich bin jetzt wieder, ich bin halt irgendwann auf Google gegangen, weil wir so viel im

**[00:21:38]** Team machen in der Firma. Und es ist zwar, alle die aus dem Design kommen oder von Apple

**[00:21:42]** kommen, hassen mich dafür. Alle Leute, die neu anfangen und denken, wir sind doch die

**[00:21:47]** coolste Apple-Firma. Und dann merken, dass wir auf Google Presentations arbeiten. Wir

**[00:21:51]** kriegen diese. Also das muss ich, verstehe ich auch voll. Aber wenn du zusammenarbeiten

**[00:21:55]** auf diese Weise ist das halt einfach ungeschlagen für dir.

**[00:21:59]** Ich kenne das Problem bei uns, das ist Powerpoint, da stehst du dann da.

**[00:22:02]** Da sind wir quasi das kleine galische Dorf, das alles, was wir präsentieren, machen wir mit Keynote

**[00:22:08]** und alles, was quasi Konzern kompatibel verteilt werden muss, wir sind Powerpoint.

**[00:22:13]** Grüße an alle aus der Firma, die mich kennen gehen raus, aber ihr wisst ja,

**[00:22:17]** gefühlt auch, worauf euch bei uns einlasst. Aber trotzdem auch da,

**[00:22:21]** gar überhaupt raus wollte ist. Keynote ist auch mächtiger als man auf dem ersten Blick vermutet,

**[00:22:29]** vielleicht jetzt nicht unbedingt im Austausch und keine Ahnung, mit Datenquellen anbinden und

**[00:22:34]** was weiß ich, aber wenn du schnell schöne Präsentationen hinzimmern wolltest, ging

**[00:22:39]** gefühlt an Keynote nichts vorbei. Es ging dir gefühlt sogar leichter in Keynote von den

**[00:22:43]** Fingern als zum Beispiel mit Powerpoint, so wie zum Teil an Können der Bedienung,

**[00:22:48]** Also PowerPoint, ich krieg da jedes Mal Angst und Schrecken, wenn ich PowerPoint dann doch

**[00:22:53]** mal anfassen muss.

**[00:22:54]** Letztens tuf ich dich auf dem Windows-Rechner, was präsentieren.

**[00:22:57]** Ich wurde schon von den Kollegen gefragt, ob ich dann zu staubt sehr falleweilig so ein

**[00:23:01]** Windows-Rechner anfasse.

**[00:23:02]** Ich hab kurz überlegt, ob ich sicher als Handschuhe anziehe.

**[00:23:05]** Aber ein ganz anderes Thema.

**[00:23:06]** Und das finde ich, ist bei Notion dann halt auch so ein Punkt.

**[00:23:09]** Es kommt so unscheinbar daher und ist dann doch so extrem mächtig.

**[00:23:15]** Was macht ihr denn so mit Notion?

**[00:23:17]** Also, das kann du da was sagen.

**[00:23:19]** Vielleicht auch gut, als auch, wo hängt es vielleicht auf.

**[00:23:24]** Also ich sag mal, es gibt ja auch bestimmte Dinge, die da vielleicht zum Ausblick sind.

**[00:23:27]** Ja.

**[00:23:28]** Also erst mal habe ich angefangen, die damals hatten wir ein bisschen Finanzenkram in,

**[00:23:35]** wie heißt das dann auch bei Google, nicht Excel, sondern Tabellen oder so, Google-Tabellen

**[00:23:42]** und in Google, in dem Word von Google, in den Docs, genau.

**[00:23:46]** Und da hatte ich so ein paar Sachen gebaut, weil meine damalige Kollegin wünschte sich für die Finanzplanung und so weiter da was und.

**[00:23:53]** Wir haben da jetzt nicht so viel Mühe gegeben, da habe ich einfach etwas gebaut, wollte keine Software nutzen.

**[00:23:57]** Genau das wurde aber immer größer und als ich dann merkte so, okay, ich kann das alles in Google, aber irgendwie ist das komisch da diese Fehler Anfälligkeit.

**[00:24:06]** Hab ich dann dieses Notion aus Versehen auf dem Tisch gekriegt und hab dann da mich, mich reingefummelt und darin was gebaut.

**[00:24:12]** Das heißt, den Anfang hat gemacht eigentlich so eine Art Liquiditätsplanung, wann schreiben

**[00:24:18]** wir welche Rechnungen, so zahlen Welt und dann kamen irgendwie relativ viel Zeug dazu, was

**[00:24:26]** so mit Datenablage zu tun hat oder einfach eine Datenbank brauchst und dann kannst du

**[00:24:30]** einfach sagen, ich will eine Datenbank haben und folgende Felder sollen da sein und die

**[00:24:33]** Leute sollen zugruf haben und das soll so und so sein und dann funktioniert das und

**[00:24:37]** dann aber und das ist das Herzstück heute war irgendwann die Frage, wie lösen wir

**[00:24:42]** eigentlich jetzt sozusagen in Zukunft unsere Kapazitätenplanung.

**[00:24:46]** Die Kapazitätenplanung ist bei Nagentour mit vielen Kunden, vielen Projekten, vielen

**[00:24:52]** Mitarbeitenden, wechselnden Strukturen und so weiter, gar nicht so ohne, das ist

**[00:24:56]** keine, keine IT-technisch gesehen keine einfache Sache, da kannst du zwar, was

**[00:25:03]** das Marketing angeht, einfache Lösungen im Netz finden, aber wenn du es

**[00:25:07]** wirklich ernst meint, ist es nicht trivial. Da haben wir uns dann angefangen,

**[00:25:13]** einen bestimmten halben Jahr lang erstmal selbst, dann mit einem Kollegen zusammen,

**[00:25:17]** dann mit anderen zusammen mit testen und so weiter zu basteln und habe dann irgendwann

**[00:25:21]** die Version gebaut, die wir ungefähr vor anderthalb Jahren, etwas mehr als anderthalb

**[00:25:25]** Jahren, dann eingeführt haben und das ist eben so eine typisches Kunde-Projekt-Ticket-System,

**[00:25:32]** Zeiterfassung, wo man eben vor allem die Arbeit mit organisiert. Und das ist relativ fett. Ich glaube,

**[00:25:38]** nicht dass es eine große Reinstallation gibt, sondern Situation gibt es die. Und das ist der

**[00:25:46]** zweite Teil in der Frage, was auch die Down-Zeit ist. Notion ist super in Daten, in Meetings,

**[00:25:52]** in KI jetzt und so weiter, aber Notion ist nicht so gut in dem, wo Excel einfach richtig gut ist,

**[00:25:56]** nämlich so, ich habe zwölf Monate und ich habe tausende von Daten und ich will

**[00:26:01]** da mit irgendwelche Formeln verbinden und so weiter. Wenn du das bauen willst in Notion,

**[00:26:05]** dann musst du so Relationen auf sich selbst machen und ganz komische Rollups und ganz

**[00:26:11]** komische Alkulationen und bis vor einem halben Jahr wurde Notion dann so langsam,

**[00:26:15]** dass meine Leute gesagt haben, ich kann damit nicht mehr arbeiten, dann hat Notion den

**[00:26:20]** Summer of Excellence gemacht und ihre gesamte Entwicklerkompetenz nur in Performance investiert

**[00:26:25]** und in keinem. Und die Performance Investition hat sich total ausgezahlt. Jetzt ist alles

**[00:26:31]** schnell oder schnell genug. Aber das ist so, das ist so das, na also du kannst, du kannst

**[00:26:36]** alles damit machen. Ich habe jedes Problem damit gelöst, was wir hatten, aber es ist eben

**[00:26:40]** an der Stelle so ein bisschen so, dass du noch so ein Schlauch aus dem, aus der Maschine

**[00:26:45]** rausführst, durch die Fensterscheibe, durch den Schiebedach wieder rein und mal hinten

**[00:26:49]** sterben und blitzigen. Dieses Gefühl hast du bei, bei manchen Sachen, bei Norschen.

**[00:26:53]** Aber ich sage mal, mit solchen Excel-Tapeten hat ja auch nicht jeder jeden Tag zu

**[00:26:59]** tun. Ja, also ich meine, natürlich findet man bestimmte Edge-Cases, wo man sagt, okay,

**[00:27:05]** da ist jetzt keine Ahnung, Excel war es doch immer besser oder schneller am Ziel oder was weiß ich,

**[00:27:14]** aber was ich halt der Notion so schön finde, es ist einfach so omnipräsent für mich in so

**[00:27:21]** vielelei Dinge. Also ich meine, ich habe jetzt nicht so einen Kapazitäten, Einsatzplanung und so

**[00:27:25]** weiter. Wie gesagt, ich benutze es ja quasi nur privat, um Dinge zu evaluieren und meine

**[00:27:32]** Sachen zu strukturieren. Ich habe jetzt zum Beispiel dem Leo Becker Grüße den raus,

**[00:27:37]** einen heißen Verlag. Da bin ich übermorgen, glaube ich, wieder in dem Podcast drin. Wo

**[00:27:41]** würde die Apple Vision Pro reden? Dem habe ich das auch mal gezeigt, wie man sich quasi

**[00:27:45]** so Show-Notes sich vorschlagen lassen könnte. Was für Themen hat man denn? Du kannst

**[00:27:49]** den Agenten los, schicken, dass der Webseiten absucht nach Nachrichten. Also Nein

**[00:27:54]** 2.5 Mac und die Decoder und was weiß ich was, dass ihr das in dann so eine Datenbank trägt.

**[00:27:59]** Du kannst ihn dann bitten, dass er, du bleibst noch rausholt, du kannst ihn bitten, dass

**[00:28:02]** er zusammenhängende Sachen, die die gleiche durch die KI generierten Kategorien zusammenfasst.

**[00:28:08]** Du kannst ihn dann bitten daraus, Steepfunk-Listen, was willst du eigentlich vielleicht in

**[00:28:13]** deinem Podcast besprechen, das ist schon faszinierend, oder ein anderes Thema ist,

**[00:28:18]** dass ich gesagt habe, hier recherchieren wir immer folgendes Zeug und dann hatte

**[00:28:22]** mehr da auch tabeln und so ein Kram draus gemacht, auch da ist wieder Abstand draufgestellt.

**[00:28:26]** Und was ich an Notions total geil finde, ist es halt kein geschlossenes System, ist es offen.

**[00:28:30]** Also du kannst andere Sachen anbinden und du kannst Notions selbst anbinden.

**[00:28:35]** Also vielleicht können wir da nochmal zwei, drei Sätze drauf verlieren.

**[00:28:38]** Also ich zum Beispiel bin es hingegangen, nutze total gern OpenAI im Original, also in der

**[00:28:44]** Vanilla Edition sagen wir mal, wenn wir ein bisschen mit Android uns da kappeln wollten, keine Sorge,

**[00:28:49]** mehr Android Sprüche kriegt, kommt zwar nicht. Und Manus. Und sowohl Open AI als auch Manus

**[00:28:56]** erlauben mir zu sagen, du pass mal obaucht, ich connectiere Notion. Und ich kann dann

**[00:29:00]** hingehen und sagen, so pass mal obaucht, ich mach da meine mit Manus, meine Recherchen

**[00:29:04]** und Kram und sag dann am Schluss, wenn alles fertig ist, so und jetzt machst du mir bitte

**[00:29:08]** eine Tabelle im Ort nach Schnickschnack-Schnuck und da machst du bitte die Einträge, die

**[00:29:13]** du gefunden hast, direkt in Notion rein. Dann hast du in Notion entweder eine

**[00:29:17]** Tabelle, die erweitert wird, weil sie schon da ist oder ein Tabelle, die angelegt wird.

**[00:29:21]** Und das finde ich auch so, ich meine klar, du könntest sagen exportiere als CSV oder importiere

**[00:29:27]** ich mir das CSV oder du sagst einfach, es ist da. Und wenn du dann sowas im Manus nutzen sagst,

**[00:29:32]** du machst dann daraus einen täglichen Arbeitsauftrag. Ich lasse dann Manus dann auch verschiedene

**[00:29:37]** Internetquellen quasi abscannen und dann automatisch diese Tabellen füllen und dann hast du

**[00:29:42]** wenn du morgens quasi dein Notion aufmachst, immer eine fruelle Tabelle mit aktuellen Nachrichten,

**[00:29:48]** mit KI-generierten Keywords und Aufbereitung und noch einen Nöcher, oder dann auch denkst, okay,

**[00:29:54]** das ist durchaus auch für Recherche und Ablage und Anbindung an KI-Systeme, auch da ein Game-Changer

**[00:30:02]** mit mir. Absolut. Aber was ich noch eben ergänzen will ist, ich komme auch gleich zu KI. Ich

**[00:30:07]** Ich wollte nur sagen, dieses Acetetensystem hat dazu, also vorher Daten, also erst Finanzen,

**[00:30:13]** dann alle möglichen Daten, Wissen, bla bla bla, und dann wirklich das Herzstück, also

**[00:30:19]** wie organisierst du dich?

**[00:30:20]** Also das Ticket-System.

**[00:30:21]** Ja, ja.

**[00:30:22]** Das Ticket-System schafft folgende Zahl.

**[00:30:25]** Wie viel habe ich als Mensch, der in dieser Firma arbeitet, diese Woche kalkulatorisch

**[00:30:32]** zu tun, kommt das hin oder nicht. Inklusive meiner Teilzeit, inklusive meines Urlaubs,

**[00:30:38]** inklusive meiner Krankheit und inklusive aller Sachen, die ich tun muss, komme ich irgendwie

**[00:30:41]** auf diese 5 Tage, wenn ich 5 Tage arbeite. So, das ist nicht trivial, weil wenn ich aber

**[00:30:47]** diese Zahl belastbar habe, und die haben wir jetzt halt überall im Jahr belastbar, über

**[00:30:50]** eineinhalb Jahren, dann kann ich mich daran orientieren, da kann der Teamleiter darauf

**[00:30:54]** gucken, da kann jeder darauf gucken. Das ist irre und das ist in so einer Timeline

**[00:30:57]** dargestellt. So, jetzt pass auf. Dann kommt diese scheiß KI. Und jetzt kannst du diesem

**[00:31:02]** Ding sagen, hab ich so ein Masterprompt gemacht, wo ich das alles erkläre, wie alles funktioniert,

**[00:31:07]** was, wie, wo gemeint ist. Und jetzt kann ich mit der KI reden. Wie viel Zeit, wer könnte

**[00:31:12]** der nächste sein? Wer könnte daran arbeiten? Welches Team hat noch Kapazität? Das ist

**[00:31:18]** noch nicht perfekt. Das ist am Anfang. Aber ich kann jetzt ernsthaft mit einer künstlichen

**[00:31:23]** Intelligenz für die Kapazitätenplanung reden. Ich kann darüber reden, wann können wir den

**[00:31:29]** nächsten Auftrag im Web-Bereich machen? Wann können wir den nächsten Auftrag im Social

**[00:31:33]** Media-Bereich machen und im Video-Bereich machen? Das ist nicht perfekt, aber das ist alles

**[00:31:37]** jetzt da. Und das macht mich so verrückt, weil ich denke so, oh mein Gott, was bedeutet

**[00:31:42]** das? Ich kann auf einmal mit einer 24-7 niemals müde, immer schlau Entität reden und

**[00:31:50]** zu Themen, die wirklich wichtig sind, was sie, die sozusagen wirklich im Kern der Firma sind.

**[00:31:55]** Und das macht es so verrückt und sie hat einfach den Kontext wirklich dessen, worum es in so

**[00:32:01]** einer Firma wie unserer geht, nämlich wer arbeitet wann, woran, mit wie viel, wie viel

**[00:32:06]** Geld kriegen wir dafür, wie viel, wie viel haben wir schon daran gearbeitet.

**[00:32:09]** Ich kann fragen, wo läuft es schlecht, wo läuft es gut und ich habe die ganze Zeit

**[00:32:13]** echte, wichtige Daten dafür.

**[00:32:16]** Ich bereue ja schon, dass ich eben diesen Absprung-Zucker-I-System gemacht habe, weil ich gerade während du gesprochen hast, überlegt habe,

**[00:32:24]** ich kann dir das immer nur aus meinem Arbeitsumfeld sagen, wie lange sind Menschen vielleicht beschäftigt,

**[00:32:30]** Dinge herauszukriegen, die vielleicht einer Selbstverständlichkeit sein müssten,

**[00:32:35]** wenn man sich nicht mit dem Thema beschäftigt, um solche einfachen Fragen zu beantworten,

**[00:32:39]** wie, was läuft gut, was läuft schlecht, wann haben wir wieder Zeit für etwas?

**[00:32:42]** auch hier grüße an mein team, ja, wo ich meine, das Agenturgeschäft könnte ich mir auch durchaus aus der, ich sag mal spontan teilweise vorstellen, weiß ich nicht, also wenn

**[00:32:52]** für Kunden wie wir um die Ecke kommen und sagen, wir brauchen mal ganz schnell und dringend und bitte hier und bitte anders und keine Ahnung was,

**[00:32:58]** zumindest ist es aber auch bei uns intern so, dass natürlich auch mal Dinge hoch kommen, weil keine Ahnung, Marketing um die Ecke gekommen oder Produktlaunch ist oder

**[00:33:04]** eine regulatorische Anforderung gesetzt werden will und was weiß dann ist nicht alles, ja,

**[00:33:08]** will ich jeder Veralbern noch irgendwie zu ernst gerade darstellen, oder schlimmer darstellen, als es ist.

**[00:33:14]** Aber das, was du gerade sagst, als du sagst, ich kann mit dem Ding quasi chatten

**[00:33:18]** und ich habe einen Sachverstand über Projekt-Statee, über Belegschaftsstatus, über...

**[00:33:26]** Was habe ich das letztes Mal mit dem Kunden besprochen?

**[00:33:29]** Hat es ja auch diese Meting-Funktion, glaube ich, erwähnt, weiß ich gar nicht,

**[00:33:33]** nur für das mit dem Meting-Aufzeichen?

**[00:33:35]** Ich möchte da kurz einhagen, die Meeting Aufzeichnung ist für uns fast schon das Killer Feature,

**[00:33:41]** also das war der Moment, wo die meisten PMs gesagt haben, alles klar, wir wollen das alles

**[00:33:46]** haben mit der KI, weil das wird nicht nur aufgezeichnet und dann gibt es die Zusammenfassung,

**[00:33:50]** sondern ich habe ja gesagt, bei uns heißt das Tickets und da habe ich so ein Prompt

**[00:33:54]** gebaut, mit dem kannst du aus dieser Aufzeichnung, so wie das das Ding selber ja schon macht,

**[00:34:00]** diese To-dos raus extrehen, aber in dem Fall macht die KI automatisch, wenn du das willst,

**[00:34:07]** in dem Projekt des Meetings, die To-dos für die richtigen Leute, wenn du ein bisschen

**[00:34:13]** daran längst, das so zu sagen. Und das geht so. Das Meeting ist zu Ende und die PM sitzt

**[00:34:17]** da, klickt auf das kleine Männchen unten rechts und sagt, erzeuge Tickets, add,

**[00:34:23]** KI, Ticketmaker, Enter, geht Kaffee trinken, kommt wieder, hat alles vorgeschlagen, kriegt

**[00:34:30]** vielleicht das immer mit Checkliste und Freigabe mache, dann sagst du Go, sind die ganzen

**[00:34:36]** Dinge da, da sind die Tickets mit der Kapazität an die Leute dran gebucht, im richtigen Projekt,

**[00:34:44]** es ist unfassbar.

**[00:34:45]** Ich meine, ich weiß nicht, wieviel von den Zuhörenden das jetzt nachvollziehen können, aber ich

**[00:34:54]** würde am nächsten auflegen und ganz viele neue Ideen, die sich daraus ergeben, allein

**[00:34:58]** aus dem Gespräch jetzt wieder.

**[00:34:59]** Da bin ich auch schon sehr glücklich, dass wir uns jetzt hier zu dieser Crossover-Sendung

**[00:35:03]** zusammentreffen konnten, weil bisher haben wir uns immer Sprachnachrichten aus dem Auto

**[00:35:06]** oder so, wenn ihr mehr gesteckt, hast du das ausprobiert, guckt mal, hier sind kaum

**[00:35:09]** so und da und überhaupt und keine Ahnung, so und der ist das total schön.

**[00:35:12]** Aber das, was du gerade beschreibst, sollte eigentlich, ich meine, was man halt nicht versteht,

**[00:35:20]** warum gibt es so wenig Wissende?

**[00:35:23]** Also, unabhängig davon, ob es vielleicht noch andere coole Tools gibt, frage ich mich,

**[00:35:29]** an welcher Stelle müsste Notion auch noch ein bisschen auf den Putz hauen, um bekannter

**[00:35:35]** zu werden?

**[00:35:36]** Weil das Problem, dass du schilderst, ich will dir nicht so nah treten, aber das

**[00:35:40]** haben ganz viele.

**[00:35:41]** Und ich möchte sagen, dass ich durchaus auch mich in einer Situation befinde, wo ich sage,

**[00:35:45]** ich wäre sehr dankbar, wenn ich ad hoc besser Fragen stellen könnte, um Antworten zu kriegen.

**[00:35:51]** Allein noch nicht mal die Kapazitätsplanung und so ein Kram. Aber natürlich auch das.

**[00:35:55]** Ja, alles von der Seite.

**[00:35:57]** Ich kann dir noch ein Beispiel machen, was ich auch sehr faszinierend finde.

**[00:36:00]** Und zwar haben wir in einem Teamleitermeting irgendwann geredet und sie die Teamleitern

**[00:36:05]** mit uns aus der Agenturleitung und haben Ideen gesponnen.

**[00:36:10]** Und da meinten die ja es wäre schön, wenn wir so Monitore hätten, wo so ja, wenn die

**[00:36:14]** Firma wüsste, was die Firma war, wo so alle mögliche Sachen, die so passieren

**[00:36:17]** stehen, in der Firma. Und da habe ich gesagt, naja, Leute, ihr seid hybrid. Also ihr seid

**[00:36:21]** höchstens die Hälfte der Zeit in der Firma, wenn es gut läuft. Also wenn, dann

**[00:36:24]** muss das ja auf einen digitalen Ort auch sein. Ja, okay. Ja, kannst du da

**[00:36:28]** irgendwas machen? Dann kam dieses Motion 3.0 mit der KI raus und mein

**[00:36:32]** prompt dafür heißt kaibinde strich whatsapp also was ist los whatsapp und danke ja ich sage das

**[00:36:41]** weil es gibt gab es einen tollen werbe werbeswort früher der egal so pass auf und der sucht

**[00:36:47]** durch alle angeschlossenen tuets inklusive slack drive dokumente kommentare und so weiter nach

**[00:36:56]** Interessanten, lustigen, das habe ich mit Beispielen und so weiter unterlegt, Themen und ich mache

**[00:37:02]** mal nur ein Beispiel. Mal gestartet im PM-Team Willkommen zurück im Norden. Das ist der Einsatz,

**[00:37:09]** das Ziel ist immer, es darf nur ein Satz sein und es muss so eine kleine Karte ergeben, die

**[00:37:14]** dann auf dem Dashboard der Mitarbeitenden rechts so runterläuft. Oder nach diversen

**[00:37:20]** Verhandlungsrunden ist der schriftliche Auftrag von der Insert-Kundennahme. Wir haben den

**[00:37:25]** Pitch gewonnen. Diese ganzen Informationen, lustige Informationen, was jemand kommentiert

**[00:37:29]** hat in Slack, also bei euch in Teams wie Chat oder so und so weiter. Diese ganzen Sachen stehen

**[00:37:35]** jetzt einfach so, die kommen so rein, wie so ein Social Network. Die kommen da so rein,

**[00:37:41]** das macht diese KI. Und bis jetzt lasse ich das noch meine Kolleginnen aus dem Office kuratieren,

**[00:37:46]** damit da nicht irgendwie, weißte, so ein Trauerfall oder irgendwas zwischenkommt.

**[00:37:50]** Ja, es ist absolut irre, was du auf einmal hoch holst und wo die Leute auf einmal sehen

**[00:37:55]** können, was alles so los ist, weil das kriegst du ja nicht mehr mit, wenn du nicht mehr jeden

**[00:38:00]** Tag den ganzen Tag in der Firma bist.

**[00:38:02]** Das stimmt.

**[00:38:03]** Ja.

**[00:38:04]** Also ich bin ja auch sehr gerne im Büro nicht nur wegen, weil ich die Kollegen beim

**[00:38:08]** Arbeiten sehen möchte, sondern auch, weil man durchaus auch Dinge mitkriegen will,

**[00:38:12]** was passiert auch sicherlich auch gut, das wie schlecht ist, aber natürlich auch,

**[00:38:17]** passiert in anderen Projekten und auch dieses Moment, ob du das schön, dass du da bist,

**[00:38:23]** lass uns mal gerade ein Thema besprechen. Aber das, was du beschreibst, ist ja wahrscheinlich,

**[00:38:28]** egal wie mächtig das jetzt gerade schon ist, auch weiterhin der Anfang von dem, was da möglich ist.

**[00:38:34]** Wenn ich überlege, die haben ja auch sowas angekündigt, wenn ich das richtig noch im

**[00:38:38]** Kopf habe, dass du in Zukunft auch Agenda von sich aus zeitgesteuert irgendwie starten kannst,

**[00:38:42]** das ist glaube ich noch nicht da. Oder ich habe es nicht gefunden und du sagst mir jetzt,

**[00:38:46]** hättest du mal auf dieses Menü Funktion geklickt, dann wärst du da.

**[00:38:49]** Ich will es so sagen, haben die das offiziell angekündigt, dass es Agenten gibt?

**[00:38:53]** Also ich sage mal so, ich habe es so mitgenommen, dass da Sende-Empfänger-Probleme ist.

**[00:38:59]** Ich hab in der Chemie an so eine Tacheldarstellung, wo das verschieben Rollen vergeben haben

**[00:39:06]** und gesagt haben so durgenwürst getriggerte durch und da hab ich schon auch gedacht,

**[00:39:09]** verdammter Ax, wenn die anfangen und auch noch selbst getriggert los treten und

**[00:39:13]** sich vielleicht gegenseitig trickern können, dann bist du ja tatsächlich in so einem agentischen

**[00:39:19]** System, weil Prompts dann ein Ziel verfolgen und dadurch andere Prompts quasi anstoßen können.

**[00:39:25]** Und dann, glaube ich, wird es nochmal... Ui! Es ist ja so, wenn man so ein Notion Nerd ist wie ich,

**[00:39:33]** dann kann man sich bewerben bei einem Programm, das Notion Ambassador heißt. Und da gibt es

**[00:39:40]** sind so verschiedene Sachen, die man machen muss. Keine Ahnung, das ist nicht so schwer, aber die suchen

**[00:39:45]** dann natürlich auch sozusagen Leute raus, die so ein bisschen multiplizieren und ich bin da drin

**[00:39:49]** schon seit einem Jahr oder so und wir haben jetzt gestern die Test-Version bekommen und ich darf

**[00:39:56]** das deswegen sagen, weil sie haben das tatsächlich in dem Keynote erwähnt. Und ich habe

**[00:40:01]** jetzt zwei Agenten gebaut, den einen, den WhatsApp-Agenten, den ich gerade gesagt habe.

**[00:40:05]** Das ist tatsächlich genau dieser, der einfach morgens um 7.15 Uhr guckt und meiner Kollegin diese

**[00:40:12]** Cards baut, wie ich das nenne, also dieser News.

**[00:40:14]** Ich bin jetzt offiziell neidisch.

**[00:40:17]** Ach, schon. Du warst schon bei den WWDCs dieser Welt und hast total die Connections zu Apple.

**[00:40:23]** Da war ich auch immer neidisch, da bin ich immer.

**[00:40:26]** Ja, okay. Lass mal, lass mal, lass mal so im Raum stehen. Also von der Seite gibst du mir quasi damit das Signal,

**[00:40:31]** das Warten lohnt sich, es könnten noch coole Sachen kommen, die wir ja aus der Profitation

**[00:40:36]** angekündigt bekommen haben. Also, uns lohnt das kurz zu sagen, diese Agenten haben jeder

**[00:40:44]** einzelne Agent eigene Zugriffsrechte. Das bedeutet, du kannst denen halt sagen, okay,

**[00:40:50]** ich gebe dich frei für bla, bla, bla, du hast Zugriffsrechte auf Datenbank eben,

**[00:40:54]** wenn man kann sich das nicht vorstellen, das ist einfach ein fucking User-Trilium diese

**[00:40:59]** Wortwahl rausschneiden. Also ich fange noch mal an. Ich schreibe einfach rauf explizit.

**[00:41:04]** Hallo? Okay. Das ist nicht vor 18, unter 18. Es ist einfach ein User. Mein Agent heißt

**[00:41:12]** Mut, also Stimmung. Und da sage ich, suche in allen internen Quellen wie E-Mails, Meeting

**[00:41:17]** Tickets und so weiter, Slack nach Kommentaren, filte sie nach gut oder schlechter Stimmung.

**[00:41:21]** Alles dazwischen ist mir egal, recherchiere gründlich, bla, bla, bla. Und dann kriege

**[00:41:25]** ich einfach auf dem Weg, den ich möchte, so oft ich möchte das Zug. Und die Zugriffsrechte

**[00:41:31]** kann ich an jeder Datenbank in jedem Dings, wie die Zugriffsrechte funktionieren, auf

**[00:41:36]** dieses Ding geben. Das ist wirklich krass. Das Ding kann Mitglied einer Gruppe sein.

**[00:41:40]** Also, dass die Leute bei Notion haben durch diese Blockstruktur, was ich am Anfang

**[00:41:45]** sagte, also dadurch, dass das sozusagen so eine Art, ja, jedes Element hat seine,

**[00:41:51]** ist eine, ich nenne das jetzt mal einfach Entität, kann referenziert werden, ist irgendwie dadurch,

**[00:41:57]** haben die einfach so eine kraftvolle Grundidee, die jetzt in der Karriere...

**[00:42:02]** Eine gute Basis.

**[00:42:03]** Eine extrem gute Basis, ja.

**[00:42:05]** Da hat man wahrscheinlich damals gedacht, oh, irgendwie geile Idee, aber nicht erahnen

**[00:42:09]** können, was das eigentlich bedeutet und das ist, glaube ich, auch ein entscheidendes

**[00:42:14]** Vorteil, warum vielleicht diese anderen großen Player am Markt sich schwer tun, wenn

**[00:42:19]** immer allein guckst, Karl Klammer, sorry, Microsoft Co-Pilot, soweit Auseinander sind die gar nicht.

**[00:42:27]** Das ist meine persönliche Meinung, kein offizielles Statement, ist einfach nur sehr beeinträchtigt

**[00:42:33]** in der Art und Weise, was er kann und dann auch noch wie er es kann. Also wenn ich dem

**[00:42:36]** Ding sage, fülle mir eine Excel-Tabelle aus, dann bin ich jetzt mit Leute glücklich,

**[00:42:39]** dass ich gleich Co-Pilot schreiben kann, sind gemiss. Aber alleine diese Geschichten,

**[00:42:45]** Schreibt mir das um, schreibt mir ein Text, verwende beim Text diesen Stil und das, was du da jetzt gerade noch aus seiner Zauberkiste rausgeholt hast, das ist undenkbar mit der heutigen Architektur.

**[00:42:56]** Und von der Seite glaube ich schon, dass nauschen an der Stelle eine sehr, sehr, sehr gute Grundlage geschossen hat.

**[00:43:01]** Wenn du jetzt nicht doch irgendwie noch so noch die Spitze auf den Eiswerk drauf haust, würde ich kurz nochmal auf die offensichtlich externe KI-Tools trotzdem noch eingehen.

**[00:43:08]** Ich würde gerne noch eine Sache sagen für alle die, die sich jetzt mit KI beschäftigen, aber vielleicht noch am Anfang stehen, weil wir sind ja auch schon Notions ein bisschen tiefer eingetaucht.

**[00:43:18]** Ich finde, wenn du alles, was wir bis jetzt gesagt haben, vergisst und einfach nur sagst, okay, offensichtlich ist das mit der KI jetzt irgendwie mit dem Internet, das geht nicht mehr weg, das ist jetzt irgendwas, womit ich mich beschäftigen muss.

**[00:43:31]** Dann mach einfach so ein Free-Notion-Hoff, mach so 2-3 Tutorials und spiel damit rum und

**[00:43:38]** denk gar nicht in dieser Welt von diesen alten Männern, die hier reden, sondern das ist

**[00:43:42]** einfach eine neue Welt.

**[00:43:43]** Das ist alles vorbei.

**[00:43:44]** Du musst gar nicht mehr dich darüber freuen, dass du das nicht mehr alles von Hand machen

**[00:43:48]** musst in Excel.

**[00:43:49]** Du musst dich nicht darüber freuen, was sind jetzt hier nochmal Spalten und Zeilen

**[00:43:52]** und es ist einfach vorbei.

**[00:43:54]** Du kannst einfach in dieses Fenster, was reinschreiben und du kriegst höchstwahrscheinlich

**[00:43:58]** aus unserer Sicht zu 80, 90 Prozent, zu 80 Prozent, extrem gute Antwort. Wenn du ein bisschen mit den

**[00:44:03]** Dingen chattest, wird sie noch besser. Und in Norschen kannst du eben einen, kannst du in einem,

**[00:44:09]** in einer App Store Promts kaufen? Du kannst sie Promts kaufen. Du kannst sie auch umsonst kriegen.

**[00:44:16]** Aber es gibt einen Promt, den ich hier unbedingt erwähnen möchte von Simon.

**[00:44:19]** Gerne.

**[00:44:20]** ist dieser dieser, dieser Prompt, den ich dir auch empfohlen habe, der nennt sich auch Simon mit S-A-I wegen A-I-Men und dieser Prompt kostet 79 Euro und wer 79 Euro zur Verfügung hat, sollte diese 79 Euro investieren, es ist nicht auszuhalten, was damit möglich ist und damit kommst du Jumpstart, ach du, du überholst dann die 20.000 Autos auf der linken Spur mit 300 und bist einfach an dem Punkt, wo man heute sein kann. Das wollte ich nochmal sagen.

**[00:44:49]** Also es ist nicht nur für Nerds, sondern du kannst dir das Norschel runterladen.

**[00:44:53]** Wenn du AI machen willst, lädst du dieses Simon-Ding runter und da bist du am Start.

**[00:44:58]** Also vielleicht, das ist ja doch noch mal, noch mal, auch von mir noch mal

**[00:45:03]** der Satz, auch dieses Thema mit Notion, sich mit Themen zu beschäftigen,

**[00:45:08]** die du vielleicht sonst in anderen KAE-Systemen mühsam zurechtformeln musst,

**[00:45:12]** kannst du in Notion halt auch sehr schnell erst mal verprumen.

**[00:45:15]** Ja, also ich habe zum Beispiel auch Sachen und damit mache ich jetzt

**[00:45:18]** Da sehe ich mal so eine Überleitung zu sowas wie N8n.

**[00:45:21]** Ich probiere Dinge in Notion aus und dann mit dem Wissen, wie gut Proms miteinander arbeiten,

**[00:45:27]** welche Daten brauche ich denn über N8n dahin gehen zu perfektionieren, weil ich halt auch

**[00:45:32]** nicht die neuen Agenten so ein Kram habe, dass ich zum Beispiel sage, okay, wie müsste

**[00:45:36]** ich denn mein Promt schreiben, damit ich zum Beispiel aus einem Text das und das

**[00:45:40]** träge, das und das mache und keine Ahnung, was.

**[00:45:43]** Und dann gehe ich jetzt mich ein Ende nach Ende, bauen wir da den Work-Slog quasi nach und das coole Annotion ist, du kannst ja sogar über die Webhook-Sache,

**[00:45:53]** danke an dich, hast du mir auch auf eine Audio-Spur mitgegeben, weil man irgendwo im Wässe da bewerten kann, sag Bescheid, ne, gebe ich fünf Sterne.

**[00:46:01]** Dass man sagen kann, okay, Aktionen auf dieser Datenbank, wenn da was passiert, folgende Trigger, löst folgende Aktionen aus und habe ich mir zum Beispiel auch eine Datenbank gebastelt, vorne schreibt ein Text rein, hinten ist ein Status-Feld, Status steht da auf TWD und wenn ich das auf Innenbearbeitung setze, löst da ein Webhook aus, der Webhook ruft ein N8n Workflow aus, der N8n Workflow, das ist so ein agentisches Workflow-System, Open Source, Berliner Startup.

**[00:46:31]** hoch bewertet sehr interessant habe ich auch schon mal hier bei mir in der folge schon mal was von erzählt

**[00:46:36]** das nimmt dann quasi die einträge geht damit zu

**[00:46:40]** gamma gamma ist ja so eine ai mit der du folie machen kannst

**[00:46:44]** nimmt den ganzen kram lässt dort folien generieren und wenn die folien fertig sind

**[00:46:50]** schreibt es mit die die folien wieder zurück als verlinkung als dativerlinkung in den notion rein und so habe ich so eine

**[00:46:58]** Delegationszeitbälle gebastelt nach dem motto

**[00:47:00]** Wenn je nachdem, was für ein Tech ich vergebe, werden Folien generiert, werden Infografiken

**[00:47:05]** generiert, werden Texte generiert in der Stimmlage eines anderen Persona oder auch Audiofalls.

**[00:47:13]** Und das ist auch der Hammer, wenn du dir überlegst, du schreibst da Dinge rein, sei es von Hand,

**[00:47:18]** sei es über KI, sei es über das Wächterquelle auch immer, und das Ding fängt dann an

**[00:47:23]** und integriert sich so gut in diese KI-Welt, dass du auch Funktionalitäten, die dir

**[00:47:28]** vielleicht den Noten zählen nachrüsten kann, durch zum Beispiel n8n durchmake.com, durchsapier.com,

**[00:47:35]** wie auch immer der ganze Kram heißt. Und dann auf einmal auch, ich sage jetzt mal, keine Ahnung,

**[00:47:41]** Content ausspielen auf Lead-In, Content ausspielen auf, keine Ahnung, was damit automatisieren

**[00:47:47]** kann in einer Güte und Qualität. Das haut mir auch jedes Mal gefühlt, das hören weg,

**[00:47:54]** Wenn ich dann sehe, ich trage da etwas ein, den Kaffee trinken, komme wieder und in der

**[00:47:59]** Tabelle steht eine Aufgabe erledigt und hier sind übrigens die Dateien, die du wolltest.

**[00:48:04]** Das ist, also auch da würde ich sagen, egal wie gut er nach der Endung coh sind, an

**[00:48:10]** die Integrationsmöglichkeit in andere Tohlen, das ist der Hammer.

**[00:48:14]** Ja, ich habe ja ganz am Anfang, als ich erzählte, als ich mit Norschen angefangen

**[00:48:18]** habe, waren natürlich Norschen, hatten keine Automatisierung, hatte keine KI, hatte

**[00:48:22]** das war alles nicht.

**[00:48:23]** auf ein Script-Tool auf irgendeine Welt zurückgreifen, da habe ich Make genommen, weil das erschien mir irgendwie gut und massiv und toll und es ist glaube ich auch aus Europa.

**[00:48:35]** Chase over Kai oder nee, so heißt das nicht mehr, so ein Tschechchen und das ist alles cool, naja und damit habe ich einfach keine Ahnung, ich glaube wir geben 3.000 Euro im Jahr für Lizenzen, für Make aus oder für, also damit machen wir schon relativ viel, damit ist die Datefanbindung, Personioanbindung.

**[00:48:53]** Da werden alte Erinnerungen beim ersten Arbeitgeber, die viel mit Datav zu tun.

**[00:48:58]** Wir haben Datav als Buchhaltungssystem und deswegen mussten wir das anbinden,

**[00:49:03]** unsere ganzen Sachen. Das habe ich als Mehl gemacht oder wir.

**[00:49:05]** Dann habe ich bei N8N entdeckt und dann habe ich gemerkt,

**[00:49:09]** das war das erste Tool, dass diese ganze Kali-Sache so ein bisschen mehr geliebt hat.

**[00:49:15]** Und diesen Agenten, der dann selber rausfindet, dieses zentrale Tool,

**[00:49:19]** das dann selber rausfindet, das mache ich mit dem, das mache ich mit dem, das mache ich mit dem.

**[00:49:22]** Also man so ja agentisch arbeiten konnte und dann habe ich irgendwie keine Ahnung so unsere E-Mail Eingang wenn Anfragen kommen oder Eingangsrechnung.

**[00:49:31]** Diese ganze Triage da dass man herausfindet wer was das jetzt sein soll und so gebaut und bin nach wie vor ein riesiger Fan dann habe ich erst geschnallt dass es aus Berlin ist und das sowieso noch mal besser gefunden.

**[00:49:43]** Und überhaupt finde ich die Typen cool und wie das alles so ist und dass die eine sehr schöne Notion Integration haben und so weiter.

**[00:49:50]** Naja, und jetzt muss man aber fairerweise sagen, dass dadurch das Notion so weitergegangen ist,

**[00:49:54]** brauche ich es natürlich immer weniger, also es geht ja immer mehr in Notion alleine.

**[00:49:59]** Ich bin ja vorher rausgegangen, um eine wichtige KI zu nutzen.

**[00:50:03]** Mittlerweile habe ich in Notion Gemini, ich habe Claude und ich habe GPD in der jeweils

**[00:50:09]** neuesten Version.

**[00:50:10]** An dem Tag, als GPD 5 rauskam, sechs Stunden früher, weil in Europa in Notion GPD 5 verfügbar

**[00:50:17]** Also 6 Stunden früher. Das heißt die sind nicht mehr mit Versatz, sondern klar ist das Chat GPT 5 mit

**[00:50:25]** Bildbearbeitung bla bla bla irgendwie natürlich in der normalen Version kann das mehr, aber trotzdem.

**[00:50:30]** Das ist so ein bisschen so, dass das Ding trotzdem nutze ich ein Nacht ein jeden Tag, um irgendwas zu

**[00:50:36]** oder abgenutzt und muss es jeden Tag maintain, dass es irgendwie läuft und dass es angebunden ist. Also ich finde genau diese Sache, die du sagst,

**[00:50:45]** dass Norschen so ein offenes System ist und sich in die Mitte setzen will und lieber mehr Leute und

**[00:50:53]** Systeme integriert als sein Geschäftsmodell zu beschützen. Das finde ich nach wie vor richtig

**[00:50:59]** klug. Also sie sind offen für alles. Sie sind offen für Microsoft, sie sind offen für die

**[00:51:05]** ganzen GitHub, Bitbucket und wie das alles heißt. Sie sind offen für die ganzen Tools und

**[00:51:10]** Systeme und genau das macht es einfach aus.

**[00:51:14]** Ich meine, das war so bei meinem Seitentieb oder der Hinweis, ja so gewählt nach dem

**[00:51:20]** Wort, du hast das Agentische in Notion, brauchst du deswegen weniger N8n?

**[00:51:25]** Nichtsdestotrotz finde ich diese Macht, die darin liegt, open source, offene Standards,

**[00:51:31]** Integrationsschähigkeit und auch die Einfachheit, Dinge zu tun, beeindruckend, ob ich jetzt

**[00:51:37]** Sie sagt mal, alles, was ich mir in den Nachtenden zusammengedengelt habe, so einfach dann auch

**[00:51:42]** in Noten halten kann, zumal ich auch noch ein bisschen Welt außen rum bedienen will, weiß

**[00:51:46]** ich nicht, wird sich dann zeigen.

**[00:51:47]** Das ist auf jeden Fall ein spannendes Konstrukt.

**[00:51:49]** Und seit gestern haben wir bei den Nachtenden ja auch diesen Workslow-Bilder, dass du per

**[00:51:54]** Prompt ganze Workflows bauen kannst, wo ich dann gestern Abend auch ein bisschen

**[00:51:58]** wenig Schlaf hatte, weil ich versucht habe, Workflows, die ich besitze, damit

**[00:52:03]** optimieren zu lassen bzw. neue Workflows erzeugen zu lassen, erkläre es selbst

**[00:52:07]** Ich habe das nicht gesehen.

**[00:52:10]** Normalerweise fängst du in dem Ding ja an, dass du sagst, ich setze eine Note, was löst mein Event aus,

**[00:52:21]** mache mir meine Prozesse hätte mit Notes die Variablen definieren, die Internet-Zurkrüfe machen, die Agenten mit LLM-Modellen steuern

**[00:52:29]** und du musst es quasi dir die Ablauflogik selbst zusammenklicken, indem du die Notes miteinander verbindest

**[00:52:36]** ist und dann so eine mehr oder weniger große Workflows dir zusammenticken kannst.

**[00:52:42]** Und ich glaube gestern war das, oder ich habe zumindest gestern gesehen, dass sie in der

**[00:52:47]** Cloud-Version eine Beta rausgebracht haben mit einem Workflow-Bilder, d.h. du kriegst

**[00:52:53]** jetzt, wenn du ein Workflow aufmachst, nicht mehr den klassischen Trübchen aus Plus,

**[00:52:58]** um eine Note auszuwählen, sondern dem dran ist, KI-Gestütz des Workflow-Bauen.

**[00:53:03]** Und dann chattest du mit dem Workflow und du schreibst rein, was hätte ich gerne.

**[00:53:07]** Ich habe dem Ding gesagt, wenn wir auf LinkedIn folgt weiß, dass ich so ein Advisory Board

**[00:53:12]** mir mal gebastelt habe, so 20 namhafte Personen, die ich mir als Personaprompt hinterlegt habe,

**[00:53:18]** die von einem Agent zu einem bitteren Gespräch geladen werden zu einem Thema, das ich dem

**[00:53:24]** Board stelle, der Konsultant wählt aus, mit dem er diskutiert, diskutiert mit den

**[00:53:30]** weltentsprechende Regeln für die Diskussion zwischen den Proms aus und gibt mir dann das Ergebnis.

**[00:53:35]** So und das habe ich als Frage an den Workshop-Bilder gestellt.

**[00:53:40]** Ich habe dem gesagt, du passst umwacht, ich habe jetzt 20 Proms, da brauche ich Platzhalt dafür.

**[00:53:44]** Ich habe webinterface, also das das das das nrnd da bietet.

**[00:53:49]** Möchte Teilablog machen für Unterstützende Teiltypen, möchte, dass es einen Konsalten gibt,

**[00:53:54]** der prüft, welcher meiner Proms sind die besten dafür, der dann überprüft,

**[00:53:59]** mit welcher Methodik kann ich zu einem guten Ergebnis kommen, also Moderationstechnik anwenden,

**[00:54:05]** dass du zusammenfasst. Das hatte ich erst so auf 1600 Zeichen, dem kommt, das war zu

**[00:54:09]** lang, ich musste dann auf 1000 kürzen, habe dann Inter gedrückt und dann fing der an,

**[00:54:12]** hat gebaut. Und das, was er gebaut hat, hat funktioniert. Es ist nicht so, dass du dann

**[00:54:17]** auf einmal so einen Kasten beim Fragezeichen hast, wie wenn du dann dir deinen N8n Workflow

**[00:54:22]** mit ZTT oder aus Hoppig gedönsbaus, sondern es war ein voll funktionsfähiger Workflow,

**[00:54:29]** mit dem du auch weiter tetten konntest. Gut, es ist Beta, manchmal ging mir der Workflow dann

**[00:54:34]** auf Flöten, dann musste ich dann mir angewöhnen, rechtzeitig zu speichern. Aber die haben jetzt

**[00:54:40]** quasi dieses ganze Citizen Developer und jeder kann hier Workflow bauen, nochmal auf eine

**[00:54:44]** Vereinfachung gehoben, weil du jetzt mit dem Ding tetten kannst in der Beta. Sie haben gesagt,

**[00:54:50]** das geht auch erstmal nur in der Cloud, aber ich habe meine die schlimmsten Workflows, die ich bei

**[00:54:55]** mir quasi habe. Glimm, weil sie sind groß, weil sie auch dort, learning by doing, ich habe nicht

**[00:55:00]** 50.000 Kurse gelesen, ich probiere sie auch aus. Meine schlimmsten Workflows waren innerhalb von 8

**[00:55:06]** Minuten nachgebaut. Mit CELAS-Hellenabfangen, also ich sag mal in einer besseren Qualität als

**[00:55:12]** meine alten Workflows. Auch dass sie so eine Note reingesetzt haben und an dieser Stelle ist

**[00:55:17]** ist jetzt JavaScript Code und da war da JavaScript Code in dieser Note und er hat sich dann da

**[00:55:22]** geholfen, Dinge, die er, ihr sagt jetzt mal, mit den klassischen Notes nicht hingekommen

**[00:55:26]** hätte, weil es auch nicht, aber alle Custom Notes kamen, also Custom Notes sind ja Notes

**[00:55:31]** aus der Community zur Anbindung von, was weiß ich, was, ob es da da auch teufel gibt,

**[00:55:34]** weil sie nicht, muss ich gucken.

**[00:55:35]** Mhm.

**[00:55:36]** Aber das war so beeindruckend, dass ich dem Ding sage, du, ich habe dir folgendes

**[00:55:39]** Problem, mach mir doch mal ein Workflow und du trugst auf Play und der läuft.

**[00:55:43]** Ja, da denkst du dir auch so, halter, halter, das ist doch auch mal eine Ansage von etwas,

**[00:55:50]** das auch als Open Source angefangen hat, das aus Deutschland kommt, dass sich so gut in

**[00:55:55]** Notion, man muss fair sein, auch ganz viele andere Dinge, so gut integrieren lässt.

**[00:55:58]** Und für mich ist das echt das zweite Tool aus dieser Dreierreihe, ja, das erste ist

**[00:56:05]** Manus.

**[00:56:06]** Manus ist für mich echt so der Hammer für Recherchen im Internet, das zweite ist

**[00:56:09]** dann Notion und das dritte ist dann End nach End.

**[00:56:11]** Das ist echt ein Konsprucht, das ist gefühlt magisch.

**[00:56:15]** Ja, also wenn man Entwickler ist oder sich mit, ja so, das alles studiert hat und das tagtäglich macht,

**[00:56:24]** dann ist das Anbinden von Datenquellen, des Verknüpfen von Datenquellen, alltag und dann kostet das irgendwie PT,

**[00:56:31]** also Personentage oder Schründen oder was, dann kann man das.

**[00:56:34]** Wenn man dann aber auf einmal Make oder später dann in Nacht End kennenlernt und weiß,

**[00:56:39]** Okay, da löst jemand das Problem dieser Verbindung von der Datenschwelle mit einer Zentrale und mit der anderen Datenschwelle auch.

**[00:56:49]** Und jetzt muss ich eigentlich nur noch schlau sein, aber nicht mehr schlau sein und irgendwelche Objekte instanzieren und ich weiß nicht, was alles tun soll.

**[00:56:57]** Ich muss das jetzt quasi nur noch so zusammenstecken wie so ein Telefonist früher und diese Steckerstecken.

**[00:57:03]** Und das heißt, ich kann mich quasi um das Problem kümmern.

**[00:57:07]** Und deswegen finde ich ist das halt diese lowcode Norquold Welt für mich so spannend, weil ich bin ja kap von Haus aus kein Entwickler,

**[00:57:14]** sondern eher Designer oder irgendwas anderes, aber auf jeden Fall nicht Kern im Kern Entwickler.

**[00:57:19]** Aber ich möchte unbedingt immer, dass diese Sachen laufen, deswegen passt für mich diese Reihe Make, Einacht End,

**[00:57:25]** die ganzen KI Tools, das White Coding und natürlich Norschen total zusammen,

**[00:57:30]** weil es eben mehr ermöglicht, der die Sache versteht, die ich machen will, mehr ermöglicht, die zu machen.

**[00:57:36]** Dass ich jetzt auch noch irgendwie innerhalb von so einer Firma bin, wie gesagt, Grüße gehen raus, wie du so schön sagst, an die Leute, die das vielleicht hören.

**[00:57:43]** Ich weiß, ihr findet das nervig, dass der Chef was programmiert, alles gut, aber trotzdem ist es eben aus meiner Sicht, aus meiner Perspektive, aus meiner Rolle,

**[00:57:55]** das Beste, das passieren kann und über die Vision von Norschi, dass die Leute, die ein Problem haben, sich dieses Problem selber lösen.

**[00:58:01]** Also, das ist einfach ein Ernährung.

**[00:58:04]** Also, so viel Wahres dran, was du sagtest, Leute, die technologischen Tiefgang nicht haben Lösungen schaffen können, war das eine.

**[00:58:14]** Und jetzt zieht halt immer mehr an immer mehr verschiedenen Stellen ein,

**[00:58:18]** dass du auch noch nicht mal mehr diese Linien ziehen musst und überlegen musst.

**[00:58:22]** Was brauche ich eigentlich für die Lösung meines Problems, sondern ich schmeiße,

**[00:58:26]** Das bin ich aber magentisch. Mein gewünschter Zielsverstand in den Raum, mal weniger gut

**[00:58:32]** oder schlecht formuliert zu noten, muss ich halt weiterchatten und ich kriege die Lösungen.

**[00:58:36]** Lösungen, die, wenn du von PT angefangen, auch wir reden dann von Personentagen, heißt

**[00:58:42]** dann IBL, interne Mitarbeiter, externe Mitarbeiter, hast du nicht gesehen? Nee, externe Mittelabflüsse

**[00:58:48]** rum. Egal, spätestunde, ne? Es ist 20 vor 10, es ist nicht so spätestunde, aber vielleicht

**[00:58:53]** relativiert, diesen freudschen Versprecher. Aber das wird auch in der Lage, bis zu sagen,

**[00:58:58]** ich rede mit dem Kram, ich kriege eine Lösung und so notrede ich halt länger mit dem Kram,

**[00:59:04]** bis die Lösung so steht, wie ich es gerne hätte. Und als ich in Nacht Ende zum ersten Mal

**[00:59:09]** aufgemacht habe, habe ich auch gedacht, ich fühle mich so ein bisschen in die Vergangenheit

**[00:59:11]** erinnert, erst hat es mich abgeschreckt, weil ich dachte, was ist denn das?

**[00:59:14]** Siegästchen und dann mache ich Linie, wo sind wir denn? Also ich meine, ich seh

**[00:59:18]** Sauscode. Im Sauscode steht die Wahrheit. Auch hier grüße

**[00:59:22]** an die Entwickler. Die wahre Wahrheit steht im Sauscode, nicht in der Doku, der Sauscode

**[00:59:26]** weiß. Und als ich das gesehen habe, fühlte ich mich an etwas erinnert, das ist schon

**[00:59:30]** sehr, sehr lange her. Yahoo Pipes. Vielleicht hat das wirklich

**[00:59:33]** jemals gesehen. Yahoo, lange ist her. Yahoo. Also ich kann nicht sehen. Und da gab es

**[00:59:39]** auch die Möglichkeit, Dinge mit so Pipes miteinander zu verbinden. Das war auch sehr viel

**[00:59:43]** bunter und alles. Hatte definitiv nichts von KI. Aber du stehst dann da und

**[00:59:48]** und denkst, damit sollst du was Geiles hinstellen.

**[00:59:50]** Und jetzt merkst du, damit stellst du geile Dinge hin.

**[00:59:54]** Und wir haben quasi mit diesen zwei Tools die IT-Landschaft auf den Kopf geträgt.

**[00:59:58]** Also wenn du überlegst, ich meine, du hast jetzt von Datives gesprochen,

**[01:00:02]** das ist gegen Datives, das ist natürlich alles bei Überrat und Buchhaltung alles sehr wichtig und richtig.

**[01:00:06]** Aber ich sag mal, Datives, SAT und Konsorten sind alle aus einer Zeit,

**[01:00:11]** wo große Datenbanksysteme, feste Datenflüsse,

**[01:00:14]** Alles wird hart kodieren, wie etwas ist, es wird nicht interpretiert und es hast du auf einmal Systeme,

**[01:00:20]** die dich besser verstehen, die deine Kollegen und Kolleginnen, Mitarbeiter, Freunde, Bekannte besser verstehen

**[01:00:26]** und ermöglichen mit kompetizierten Sachverhalten, wie deine Einsatzplanung, wie was ist denn passiert beim Kunden,

**[01:00:33]** warum hängt denn das schief und gibt es ja vielleicht auch Pattern, die immer wiederkehren und dass man einfach auch Daten und Zusammenhänge vielleicht besser versteht.

**[01:00:41]** Das ist der Hammer. Und weil du sagst, das ist nicht immer das Perfekt, also ich sage mal so rum. Ich ür mich auch manchmal.

**[01:00:48]** Es gibt Menschen, die lügen dich an. Es gibt Menschen, die irren sich und vertreten ihr Mangel ein Wissen als Wissen, weil sie glauben, sie liegen richtig.

**[01:00:55]** Beim Computer sind wir es halt nicht gewöhnt. Der Computer, da wartene ich, die Antwort ist korrekt.

**[01:01:00]** Da war nenn sich das beim Computer halt hallucinieren. Und ich bin echt gespannt, wohin die Reise dieser Tools und der Möglichkeiten.

**[01:01:07]** Und waren wir endlich normalsterblich in diese Notion-Version kriegen und was da vielleicht noch alles hinter mir kommt, das ist eine tolle Zeit.

**[01:01:17]** Es ist eine tolle Zeit, aber ich habe noch einen, wir können das ja sonst schneiden, aber ich habe noch einen für mich zumindest bespannenen Punkt.

**[01:01:25]** Und zwar, ich habe eben gesagt für alle, die sozusagen irgendwie etwas ganz anderes machen, irgendwas machen, das ist völlig egal was.

**[01:01:32]** Für alle wird es notwendig sein, sich mit KI zu beschäftigen.

**[01:01:36]** So wie es für alle notwendig war, sich mit PC zu beschäftigen.

**[01:01:39]** Und Apple hat die Liberalisierung oder für jeden den Mac.

**[01:01:45]** Der Mac ist für alle.

**[01:01:47]** Und so würde ich im Moment sagen, es ist ein Menschenfall.

**[01:01:50]** Sobald es Aktien gibt, kaufe ich alle Aktien, die ich kaufen kann.

**[01:01:53]** Das ist total klar.

**[01:01:55]** Keine Finanzentzählung hier?

**[01:01:57]** Nein, nein, wir machen keine Rechtsberatung.

**[01:01:58]** Finanzentwicklung, Steuerberatung, Disclaimer, Impressum, bitte auf www.sv.gov. Was ich sagen

**[01:02:04]** will ist.

**[01:02:05]** Wir müssen das noch einmal kurz uns da rein meditieren.

**[01:02:08]** Norschen hat diese KI reingebaut.

**[01:02:11]** Wir haben ein bisschen darüber geredet, aber jetzt gibt es etwas, dass ich finde, wenn

**[01:02:15]** du jetzt, du hörst zu und bist eine Firma, du hast einen Unternehmen, du arbeitest

**[01:02:20]** in einem Unternehmen, du hast irgendein Wissen, was du verwaltest, was du kennst.

**[01:02:25]** Du weißt selber, du lernst, du studierst, das ist egal was.

**[01:02:29]** Stell dir einfach vor, du packst das aus irgendwelchen Gründen alles in dieses Norschen rein,

**[01:02:33]** so wie du deine Notizen oder so.

**[01:02:35]** Und dann hat Norschen gesagt, alles gleich, baue eine Karriere ein.

**[01:02:38]** Aber dann haben sie auch noch gesagt, ich baue dir die Möglichkeit,

**[01:02:42]** einen Master Prompt zu hinterlegen.

**[01:02:45]** Und jetzt habe ich in meinen Master Prompt geschrieben, wer ich bin, was ich finde.

**[01:02:51]** Mein Mitarbeiter aus der Redaktion, der die Redaktion leitet,

**[01:02:55]** vielen Dank, hat mir 40 Fragen zusammengestellt, den Prust-Fragebogen aus

**[01:03:01]** FACET und noch ganz viele andere Fragen, die ich alle beantwortet habe. Natürlich habe

**[01:03:05]** ich gesprochen, transkribiert, zusammengefasst, dareingeteilt. Ich habe

**[01:03:09]** meinen Masterprom komplett mit mir geprimed. Und wenn ich jetzt diesem

**[01:03:14]** Ding sage, ach so, und Norschen hat den gesamten Kontext meiner Firma. Und

**[01:03:20]** im Übrigen auch meinen privaten Kontext. Wenn ich meinen Haus saniert habe,

**[01:03:23]** dann habe ich alles in Norrschen natürlich organisiert und so weiter.

**[01:03:26]** Das heißt, alles, was ich bin und kann und es ist da drin.

**[01:03:30]** Meine beiden Bücher, die ich geschrieben habe, sind da drin.

**[01:03:32]** Es ist alles da drin.

**[01:03:33]** Und wenn ich jetzt etwas schreibe, dann wird das alles ganz doll so wie ich.

**[01:03:38]** Und dann fragen mich Leute, hast du das mit KI geschrieben oder selbst geschrieben?

**[01:03:42]** Und das fragen Leute, denen ich vorher gesagt habe, ich habe das mit KI geschrieben.

**[01:03:48]** Ich will damit sagen, es ist so verrückt, wenn du diese Dreise,

**[01:03:53]** Also wenn du den Kontext und den Prom zusammen nimmst, wenn du dir sagst,

**[01:03:57]** okay, ich schaffe einfach den ganzen Kontext, weil ich alles einfach da rein tue, stumpf,

**[01:04:02]** einfach ab in jede Daten, meine Ideen, von mir aus, was ist ich, meine Rezepte,

**[01:04:08]** alle meine Rezepte sind da drin. Alle Rezepte, die ich koche sehr gerne.

**[01:04:11]** Alle Rezepte sind da drin. Und dann habe ich ein Prom,

**[01:04:14]** dem ich erkläre, wer ich bin, dem ich erkläre, wie meine Firma funktioniert,

**[01:04:17]** was ich zu KI finde, wie meine Haltung zur Strategie ist, wie meine Haltung zu dem ist.

**[01:04:21]** Und egal, was ich die KI frage, ich habe ein kleines Chatfenster unten rechts, egal, was ich sie frage, es wird immer in dem Kontext in der Art und Weise antworten, wie ich bin.

**[01:04:31]** Und das muss man sich kurz vorstellen, man muss nichts kompliziertes machen, man muss sich programmieren können, man muss sich KI verstehen, man muss einfach nur verstehen, ich pack alles in dieses Norschen rein und ich gebe mir Mühe mit diesem Master Prompt und wenn ich mir keine Mühe geben will, 79€, Simon, Kauf und Wiedersehen, dann bin ich fertig, dann bin ich einfach, habe ich alle überholt.

**[01:04:50]** überholt. Jeden Rat, der mir irgendein Rat wählen will. Ich habe alle überholt. Ich bin einfach

**[01:04:55]** Joch Morch. Das ist wirklich ever. Wir müssen da gar nichts schneiden. Das passt total gut,

**[01:05:01]** weil wir, wenn es mal in unserer Ausgabe sind, wir gewohnt, immer mal in den Themen zu springen.

**[01:05:06]** Grüße gehen an Jens, das liegt nicht nur an dir, das liegt auch an uns allen. Ob du in deiner

**[01:05:11]** Folge das dann anders sortieren willst, kannst du dir überlegen. Aber auch hier gilt wieder,

**[01:05:17]** Während du sprichst, wird einem klar, was Notion bedeutet, wenn man es erstens mal länger benutzt hat,

**[01:05:27]** weil es einfach nicht nur KI jetzt hat und Dinge geiler adressieren kann, sondern weil es einfach auch Wissen hat

**[01:05:36]** und Zusammenhänge kennt und je mehr es quasi kennt, wo du es einsetzt, umso besser gibt es dann auch die Ergebnisse aus

**[01:05:45]** Und diese Idee mit dem Master Prompt, ich hab das Pack und ich versuchte immer noch ein paar Sachen auch daraus zu lernen, weil der das ja doch ziemlich cool gemacht hat, dass er auch überlegt nach dem Motto hier, sein AgentOS, so nach dem Motto, wie gehen wir denn jetzt eigentlich weiter und wie kommt es eigentlich, also welche Funktionität des Prompts wird jetzt gezogen für die Frage, die er gestellt kriegt?

**[01:06:06]** Das ist schon inspirierend, zeigt, aber wirklich, wir stehen vor großen Zeiten, bei denen aber die

**[01:06:18]** Lösung nicht automatisch heißt, du musst die größten Cloud-Pakete der großen Hersteller in

**[01:06:25]** großer Zülle abschließen. Ich habe auch letztens in der Studie, das ist ja keine Studie in

**[01:06:31]** ein Bericht gelesen, wie wenige angeblich zum Beispiel Co-Pilot licensieren.

**[01:06:35]** Ich meine, ich verstehe das, aber das sagt ja auch etwas darüber aus, ob die Lösung

**[01:06:40]** dir hilft oder nicht.

**[01:06:41]** Und wenn du auch nur den Funken einer Idee darin siehst, dass KI theoretisch helfen

**[01:06:49]** könnte, ist im Grunde diese Empfehlung, die du schön ausgesprochen hast, holt

**[01:06:53]** euch den Außen, probiert es aus, also ich werde von außen nicht bezahlen, ob du

**[01:06:58]** Du von Notion bezahltest, würdest du sagen, ne, aber du hast es doch nicht gesagt, ne.

**[01:07:01]** Okay, dann ist einfach, nimm dir Notion, probier es aus, guck dir einfach an und stell einfach mal eine dumme Frage an das System

**[01:07:09]** und lass dich quasi überraschen, was da als Ergebnis herausgeputzt wird, kommt

**[01:07:14]** und ich würde die Wette eingehen, jede, der sich Notion installiert und eine ernsthafte Frage reinstellt, wird dabei bleiben.

**[01:07:23]** Ja, das glaube ich auch.

**[01:07:25]** Es ist ja so schön, dass es ja sehr gut mit deinen Bedürfnissen wachsen kann.

**[01:07:30]** Du kannst anfangen und hast eine kleine, eine kleine Riefmarkensammlung, die du archivieren möchtest

**[01:07:35]** oder wo du so eine Datenbank brauchst, dann kannst du das genauso machen, schön mit Bildern und schön

**[01:07:40]** ein bisschen gestalten und so weiter, wie eben diese komplexen Systeme.

**[01:07:44]** Und was ich auch noch sagen muss, ist die Community der Leute, die mit Notion arbeiten,

**[01:07:49]** egal ob du jetzt auf Social Media bist oder auf Slack in diesen Dingern, das ist wirklich,

**[01:07:54]** sind wirklich nette Leute, es ist sehr weltoffen, es ist sehr multi-culti, es sind aus aller

**[01:08:00]** Herren Länder, sind da die Leute, also super interessant, auch was sie damit machen, wie

**[01:08:05]** die das machen, teilweise total wirrsachen, teilweise ganz inspirierende Geschichten und

**[01:08:10]** was ich wirklich jedem empfehle, das ich für Neuschel Interstit sind, die drei, beziehungsweise

**[01:08:15]** habe ich drei genannt, ich glaube drei Podcasts, Videos, Videokanäle, also wie hast du es

**[01:08:20]** YouTube-Kanäle, genau. Simon as Better Creating, Thomas Frank und Matthias Frank aus Berlin,

**[01:08:26]** das sind die drei, wenn man die guckt, da hat man einfach das Komplettpaket und eine

**[01:08:30]** Supergrundversorgung oder eine Komplettversorgung eigentlich. Den kann total viel lernen von

**[01:08:35]** denen, ja.

**[01:08:36]** Also mit dem Thema Grundversorgung kennen ich mich jetzt auch beruflich aus, aber

**[01:08:40]** der meint natürlich dann das Thema. Das ist eine andere Grundversorgung.

**[01:08:44]** Du musst mit Energieversorgung, glaube ich, oder?

**[01:08:47]** Ich möchte.

**[01:08:48]** Ja, das ist schön, bei uns im Podcast ist es meistens dann Schluss für Schluss, also wir sagen dann so Danke und wenn es euch gefallen hat, dann sagt es euren Freunden der Familie und allen und lasst uns ein Like da und teilt den Podcast usw.

**[01:09:05]** Was dürfen wir denn für dich noch machen?

**[01:09:07]** Also bei mir gibt es normalerweise, aber das haben wir schon gemacht, so eine A oder B-Frage, das habe ich geklaut von alles gesagt und das machen wir heute nicht.

**[01:09:17]** Ich bedanke mich auf jeden fall bei dir lieber marktest du bei uns was und ich bei dir war und wir einen podcast gehabt haben

**[01:09:24]** Wo wir uns gegenseitig erzählt haben

**[01:09:27]** Was wir so in dieser in dieser digitalen zeit um diesen namen noch mal zu nutzen alles zu erleben und ich freue mich sehr dass ich dich noch

**[01:09:34]** Mal inspirieren konnte mit einer technologie weil jetzt habe ich endlich einen gesprächspartner

**[01:09:40]** der fast wahrscheinlich genauso oder fast genauso verrückt ist, was das angeht, wie ich. Also,

**[01:09:47]** was KI angeht, bist du verrückt, als ich aber KI und Notch, das ist auf jeden Fall etwas,

**[01:09:51]** was uns, was uns eint. Also, vielen Dank, dass du hier warst. Danke, dass du mir quasi

**[01:09:56]** Hausaufgaben auch mitgegeben hast, wenn wir jetzt hier gleich die Aufzeichnung beenden,

**[01:09:59]** weiß ich nicht nur, dass ich die Aufzeichnung dir natürlich gerne zur Verfügung stelle,

**[01:10:04]** sondern auch, dass ich noch sein Beantragsfeaturel Notion ausprobieren werde.

**[01:10:09]** Danke, dass du da warst. Danke euch allen fürs Zuhören.

**[01:10:12]** Wir machen jetzt die Klappe zu.

**[01:10:14]** In diesem Sinne, bis zum nächsten Mal.

**[01:10:17]** Ciao. Bis bald. Tschüss.

**[01:10:21]** Willkommen bei Think Different, Think AI.

**[01:10:24]** Den Podcast von Mark und Jens.

**[01:10:26]** Zwei technologieverliebte Köpfe,

**[01:10:29]** die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[01:10:33]** Hier gibt es klare Einordnungen, echte Praxis-Einblicke und einen frischen Blick auf das, was möglich ist.

**[01:10:39]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[01:10:43]** H.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
