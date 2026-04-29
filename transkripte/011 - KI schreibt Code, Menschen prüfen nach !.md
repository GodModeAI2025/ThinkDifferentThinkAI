---
title: "KI schreibt Code, Menschen prüfen nach !"
episode_index: 11
published: "Sun, 26 Oct 2025 10:27:00 +0000"
duration: "4017"
audio_url: "https://audio.podigee-cdn.net/2171698-m-c8203b56088c5d2054b7dd409251e4b2.mp3?source=feed"
guid: "7b7d8459cbbdfb2ba46cbcf1f210bf48"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-04-28T20:34:10+00:00"
---

# KI schreibt Code, Menschen prüfen nach !

**Veröffentlicht:** Sun, 26 Oct 2025 10:27:00 +0000
**Dauer:** 4017
**Audio:** https://audio.podigee-cdn.net/2171698-m-c8203b56088c5d2054b7dd409251e4b2.mp3?source=feed

## Beschreibung

Wie AI-Aided Development die Softwarewelt verändert
In dieser Folge spreche ich mit Klaus, einem langjährigen Wegbegleiter und Security-Experten, über die faszinierenden und manchmal beunruhigenden Seiten von KI in der Softwareentwicklung. Wir nehmen euch mit von persönlichen Tech-Pannen – wie dem Ausfall von Perplexity durch eine globale AWS-Störung – bis hin zu tiefgehenden Einblicken, wie KI-Tools heute Programmierung, Dokumentation und Cybersecurity revolutionieren. 

Wir diskutieren, warum KI nicht nur Chancen, sondern auch neue Risiken für Entwickler und Unternehmen birgt, und wie sich unser Berufsalltag rasant verändert. Ob ihr schon KI im Einsatz habt oder noch skeptisch seid: Diese Episode liefert Denkanstöße und echte Erfahrungen aus der Praxis – immer mit einem Augenzwinkern und praxisnahen Beispielen. Hört rein und bleibt am Puls der digitalen Zeit!

Notion
https://www.notion.so/de-de

Perplexity
https://www.perplexity.ai/

Amazon Web Services (AWS)
https://aws.amazon.com/de/

ChatGPT
https://chat.openai.com/

OpenAI
https://openai.com/

Claude
https://www.anthropic.com/claude

Google Gemini
https://deepmind.google/technologies/gemini/

GitHub Copilot
https://github.com/features/copilot

Flutter
https://flutter.dev/

Systemd Journal
https://www.freedesktop.org/wiki/Software/systemd/

Stack Overflow
https://stackoverflow.com/

Objective-C
https://de.wikipedia.org/wiki/Objective-C

Swift
https://developer.apple.com/swift/

SwiftUI
https://developer.apple.com/xcode/swiftui/

GitHub SpecKit
https://github.com/github/speckit

Behavior-Driven Development (BDD)
https://de.wikipedia.org/wiki/BehaviorDrivenDevelopment

Gherkin
https://cucumber.io/docs/gherkin/

Cyber Resilience Act
https://digital-strategy.ec.europa.eu/de/policies/cyber-resilience-act

MISRA C
https://www.misra.org.uk/

Sora
https://openai.com/sora

Gast : Klaus Rodewig

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Mark und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** Hadi zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:33]** Heute mal wieder ohne meinen allseits geliebten Komoderator, aber dafür heute mal wieder mit einem sehr kompetenten Gast.

**[00:00:43]** Letztens hatten wir uns ja mit dem Dirk über das Thema Notion unterhalten

**[00:00:47]** und heute unterhalte ich mich mit Klaus unter anderem auch darüber, warum bei mir heute Perplexity nicht ging.

**[00:00:56]** gegen Klaus. Wer bist du, stell dich mal vor und warum gehen mein Perplexity nicht?

**[00:01:01]** Ja, ich bin der Klaus und wir kennen uns schon furchtbar lange, der liebe Mark und ich.

**[00:01:07]** Uns verbindet eine lange Apple-Historie, Apple-Security und Apple-Entwicklung und ja,

**[00:01:15]** hauptberuflich beschäftige ich mich eigentlich tatsächlich nur mit Security.

**[00:01:19]** Ich sorge mich dafür, dass die schönen Küchengeräte eines bekannten deutschen

**[00:01:24]** Küchengewähre herstellt, dass es sicher sind für netzte Gewähre. Und weil Sicherheit und KI irgendwie

**[00:01:31]** nicht mehr so richtig voneinander zu trennen sind, habe ich bei uns auf das Thema AI-Edit-Development

**[00:01:37]** mehr angezogen. So, und ich hatte wie du mag, um deine Fragen zu beantworten, ein total entspannten

**[00:01:43]** Vormittag, weil ich um, weiß ich nicht, um die vielen Urne, die ich in den Rechtern gesetzt

**[00:01:46]** habe und hatte eine Frage an Proplexity und Proplexity wollte ich nicht antworten. Und ich

**[00:01:51]** Ich vermutete mal wieder unseren Firmenzwangsproxy, der wieder irgendwas gesperrt hat, war aber

**[00:01:57]** nicht so.

**[00:01:58]** ChatGPT funktioniert.

**[00:01:59]** Dann probierte ich noch mal Perplexity und war ganz Perplex.

**[00:02:02]** Es antwortete immer noch mit einer kryptischen Fehlermeldung und dann bin ich einkaufen

**[00:02:06]** gefahren.

**[00:02:07]** Und siehe da, die Ursache war der Auswahl der Amazon-AWS-Zone US East 1, die heute

**[00:02:15]** der Weltweitshaus ferngeführt hat und offensichtlich war natürlich auch Perplexity davon

**[00:02:19]** Deshalb konnte es heute Morgen auch schön die Küche aufräumen, statt zu arbeiten.

**[00:02:24]** Na, ich war eigentlich im Büro und ganz ehrlich, ich war auch erleichtert, als ich da mitbekommen habe,

**[00:02:29]** dass es sich um ein, ich sag mal größeres Problem handelte und nicht um ein lokales von mir,

**[00:02:34]** weil während du dachtest, der Proxy der Firma ist schuld, hatte ich eine ganz andere Angst,

**[00:02:39]** nämlich, dass ich auf einmal arm geworden bin, weil ich nämlich heute Morgen angefangen habe,

**[00:02:44]** habe mir meinen Apetoken in einen frisch gebackenen N8n Workflow zu stecken, den ich habe loslaufen

**[00:02:52]** lassen, der dann tatsächlich, ich sage jetzt mal in so einer Art Endloh-Schleiße endete mit

**[00:02:56]** seinen Perplexity-Anfragen und ich kurz gedacht habe, das Ding hat mich in den Ruinen der Api-Calls

**[00:03:02]** geschmissen und mir meine Kreditkarte so sehr belastet, dass jetzt auch ein Anmeld mit meinem

**[00:03:07]** Konto als sehr unvertrauensvoll zählt und daher war ich dann doch sehr glücklich, dass das

**[00:03:12]** das mit keinem Geld abbuchen oder Ähnlichem zu tun hat, aber ich hoffe auch, dass mein

**[00:03:17]** N8N-Zugriff jetzt nicht Ursache des Übels war, nicht, dass es nachher heißt. Der Zimmermann

**[00:03:23]** saß da und hat hier quasi jetzt seinen Shutdown, N8N, so slow da, zusammengetuckert.

**[00:03:29]** So viel, wenn man nicht nur USA wohl merkt, ob du, das warst oder nicht.

**[00:03:36]** Passport, please. Haben Sie eine kriminelle Vergangenheit? Nicht, dass ich wüsste.

**[00:03:41]** Waren Sie nicht derjenige, der eben mit Ihrem Ende, seinen Enden nach der Enden verhörgst, oder dass wir gesagt haben, dass der Kollege Rodeweg in die Stadt gehen durfte einkaufen?

**[00:03:48]** Nee, nee.

**[00:03:48]** Es ist doch schon mutig, wie Dinge dann doch sich ähneln, ne?

**[00:03:52]** Also, Rodeblatt, so als Kreditkarte und Token Limit, bisher war es ja immer so, sowohl für Firmen als auch für Privatpersonen,

**[00:04:00]** dass das Einzige, was vollkommen undurchsichtig war und auch mit wissenschaftlichen Mitteln

**[00:04:07]** nicht erklärbar ist, einer Rechnung von AWS oder dem jeweiligen Cloud-Dienstleister, den

**[00:04:11]** man in der Firma benutzt. Weil man nie weiß, was passiert. Und wenn irgendein Praktikant

**[00:04:15]** hat dann durch Zufall immer noch irgendein Audit-Log angeschaltet, was dann mal über

**[00:04:20]** nach 10.000 Euro verursacht hat, das hat man jetzt zusätzlich auch mal mit KI.

**[00:04:24]** Ist doch irgendwie beruhigend, oder?

**[00:04:26]** Wobei, ich sage es mal, alte Menschen erzählen von früher, ich kann mich durchaus auch an jemanden erinnern, der versucht hatte, so ein bisschen als Influencer tätig zu sein als das ganze Anfingen mit ChatGPT und den ganzen Kram.

**[00:04:39]** Und der hatte in seinem Video seinen Apitoken gezeigt und der wurde wirklich abend, weil die Leute einfach mit dem Ding feuchtfuldig irgendwelche Dinge ausprobiert haben.

**[00:04:50]** Nach dem Motto, guck mal, geht doch, und irgendwann kam dann so die Meldung, dass sie das irgendwie

**[00:04:54]** paaren, 40.000 Euro gekostet hat, die ganzen Coles, die das vorsagt haben, wo ich dachte,

**[00:04:59]** da brauchst du aber auch ein bisschen Reichweite, um so eine Menge Euros auszugeben.

**[00:05:03]** Aber schön, ich sag mal, um Euros geht's ja zum Glück heute nicht, du sitzt hier ganz

**[00:05:09]** kostenneutral für mich hier, auch wenn ich sagen muss, ich bin nicht ganz unvoreingenommen.

**[00:05:13]** Ich besitze ja auch solche, das eine oder andere Gerät aus eurem Hause bei uns im

**[00:05:17]** habe ich ja schon mal auch in den anderen Podcasts mit dir drüber gesprochen.

**[00:05:21]** Da fühlt man sich noch gleich viel sicherer, wenn man weiß, wer sich da um das ganze Zeug dahinter so mit zusammen kümmert.

**[00:05:29]** Ja, Moment, Moment, ich, Moment, kümmere, heißt ja, ich habe eine Idee, wie Dinge gut funktionieren können und kann diese Idee

**[00:05:38]** ausstudieren, nur ob die dann umgesetzt wird und ob sie richtig umgesetzt wird, das steht ja auf dem anderen Dritt.

**[00:05:44]** Das ist dadurch, dass ich einen schönen Übergang, genau, so, jetzt sind wir im Thema, jetzt

**[00:05:52]** du Mark, genau.

**[00:05:53]** Also erzähl doch mal, wir hatten da uns vorher uns überlegt über welches Thema wollen wir

**[00:05:58]** uns denn quasi unterhalten, über welches Thema können wir uns unterhalten, wir treu

**[00:06:02]** den Motto, was gibt es denn, was die Allgemeinheit interessieren könnte, ohne dass sich irgendeiner,

**[00:06:07]** wie sag ich mal, auch einen Schlitz gedrehten fühlt und wir haben uns mit dem Thema ein

**[00:06:12]** bisschen vorgenommen näher zu beschäftigen, wo wir KI einsetzen können, sei es Doku, sei es

**[00:06:19]** Text-Erstellung, sei es Software-Entwicklung, sei es das ganze Thema Cyber Security. Magst du

**[00:06:27]** mir ein Thema sein, mit dem wir anfangen wollen? Lass uns sagen, mit KI in der Entwicklung anfangen,

**[00:06:33]** denn das ist ja das übergeordnete Thema, ob man sich dann am Ende mit Cyber Security beschäftigt

**[00:06:38]** oder mit Dokumentationen oder mit welcher Ausprägung von KI-Fältigkeiten auch immer.

**[00:06:43]** Das ist ja dann einfach nur, das ist ja dann ein Abzweig von dieser großen Straße. Und ich muss

**[00:06:49]** sagen, dass ich da so ein bisschen tatsächlich vom Saulus zum Paulus geworden bin, der so, du

**[00:06:55]** hast ja eben ältere Menschen erwähnt und wir beide sind immer vorgerückten Alters und kommen

**[00:07:02]** noch aus einer Zeit, wo man Code wirklich schön mit der Hand geklöppelt hat und

**[00:07:06]** der erste Irrweg war ja, dass man dann wie zu sprachen die Java angefangen

**[00:07:11]** hat, fremde Menschen zu benutzen, war es an sich schon mal komisch war, weil man

**[00:07:16]** doch gewohnt auf seinem C-Compiler vorher immer nur eigene Sachen zu verwenden

**[00:07:20]** oder gut abgehangene Libraries oder vielleicht mal die Boostlibrary in C++,

**[00:07:26]** was ja total vertrauenswürdig ist. Ich hatte bei meinem ersten Praktikantenanbieter

**[00:07:30]** nicht praktisch kann. Wie wirlt sich denn das an? Bei meinem ersten berufsbetonen Praktikum

**[00:07:35]** suchen wir es vielleicht besser, auch sogar den Kontakt zu Assembler-Kursen.

**[00:07:38]** Ja, guck mal an. Und heute kannst du Assembler in Chatchi BT schmeißen und der erklärt

**[00:07:45]** dir, was das ist. Du kannst sogar ein ganzes binary reinschmeißen und der disassembliert

**[00:07:48]** das. Aber das können wir vielleicht gleich nach drauf zu sprechen kommen. So, und

**[00:07:53]** dann kam, da habe ich mich über die Jahre dann gewöhnt, weil ich war lange als

**[00:07:58]** Pen-Test darum, Security-Bereiter in vielen Konzernen unterwegs und habe mich daran gewöhnt, dass

**[00:08:04]** die Menschen eben zunehmend oder hauptsächlich andere Leute's Code verwenden oder sich den

**[00:08:09]** Outstack Overflow auskopieren und dann kam er so quasi von heute auf morgen gefühlt, OpenAI

**[00:08:18]** um die Ecke und sagte, Leute, wir haben hier Chechipiti.

**[00:08:20]** Was ja gar nicht der Beginn der KI war, KI gibt es ja, ich glaube in den 80ern,

**[00:08:26]** Da hieß das noch Fuzzy Logic, ich weiß nicht, ob du dich noch erinnern kannst, da wurden sie, hat Zoni Entwackelungsalgerüten für Kameras gebaut, das waren so die ersten Konsumer, also die ersten Anfängen von KI den Konsumer gerätten und natürlich gibt es ja auch schon KI in ganz vielen Bereichen furchtbar lange, nur dieser Paukenschlag von OpenAI, wann war das, 2022?

**[00:08:46]** Da war ja der Tag, an dem die Antwort auf eine Frage nicht mehr hieß, ich habe Folgendes für dich im Internet gefunden oder ich habe dich leider nicht verstanden, aber immer fing das Ding an und konnte tatsächlich Antworten geben, also dieses Ding von OakMerry.

**[00:08:59]** Genau, bis zu November 21 bis dahin reichten nämlich nur die Trainingsdaten.

**[00:09:03]** Aber egal, da fing das ja an und da wurde der Stamm sofort gemunkelt und ich oute mich als jemand, der überhaupt keinen Plan von Geschäftsmodellen, strategischen Entwicklung oder Zukunftsvision hat.

**[00:09:17]** Also kleiner Funfact als Steve Jobs damals das Alphorn vorgestellt hat, da habe ich gedacht, was ist das für ein Ding, das braucht doch kein Mensch.

**[00:09:23]** Gut.

**[00:09:24]** Schmei, da hatte ich eins und als er dann das Alpett vorgestellt hat, dachte ich, okay,

**[00:09:27]** jetzt haben sie ein großes Alpherum gemacht, auch das braucht kein Mensch, insofern legt

**[00:09:31]** man keinen Wert darauf, dass ich valide Zukunftsvorhersagen mache, aber es monkelt ja jetzt

**[00:09:37]** aber mit der Security so ein bisschen, ne? Da könntest du dich gut aufgehoben.

**[00:09:40]** Ja, immer rückwärts gewandt. Aber es monkelt ja schon sehr schnell, die AI wird in

**[00:09:46]** Zukunft zwar verschreien und auch da dachte ich, jo, was kann da schon daraus kommen,

**[00:09:52]** Aber siehe da, die ersten Gehversuche mit JetGPT waren ja mehr als entnüchternd.

**[00:09:57]** Es kam ja wirklich nur ein Grütze raus.

**[00:09:58]** Aber mittlerweile ist das ja ein so fantastisches Werkzeug geworden.

**[00:10:02]** Und ich sagte ja gerade, dass ich lange unterwegs war, als Pentester und Berater

**[00:10:06]** in großen Konzernen und Firmen und habe Unmengen von Code auditiert

**[00:10:12]** und Software auditsgemacht mit Entwickler geschult.

**[00:10:16]** Und was ich mittlerweile sehe, ein Code, der aus so einem LLM rausfällt,

**[00:10:19]** gut ab. Das kann sich sehen lassen und das kann sich mit so manchem gestandenen Entwickler

**[00:10:25]** Produkt messen, tatsächlich. Insofern, vom Saulus zu Paulus, denn das ist der Weg.

**[00:10:31]** Ich fand das auch. Jetzt, weder sowohl bei der Entwicklung als auch bei dem ganzen

**[00:10:36]** Thema, wie wir mit dem Ding interagieren und zu einem Ergebnis zu kommen, da sind

**[00:10:41]** schon echt ein paar spannende Runden, die man dreht. Ich weiß noch, wie ich bei einem

**[00:10:44]** Kollegen stand, ich habe dem voller Begeisterung damals, 3.5 war das, nicht?

**[00:10:49]** Ich hatte die 3.5 als das quasi das erste Mal den Durchbruch hatte und die

**[00:10:54]** stand bei dem und ich sag, du, das musst du anschauen, ist total toll, was hat der

**[00:10:57]** Kollege gemacht, ich nenne jetzt keinen Namen, aber wenn er hört, wird er sich

**[00:11:01]** angesprochen fühlen. Er hat irgendeine Fachfrage dort reingeschrieben, wo

**[00:11:05]** dem System alles an Kontext fehlte, was auch nur an Kontext hätte da sein

**[00:11:10]** können und dementsprechend, weil die Antwort mehr als

**[00:11:14]** ernüchternd, mal unabhängig davon, dass es Dinger damals noch nicht im Internet

**[00:11:17]** suchen konnte, dass es nur seine Trainingsdaten kannte und so was. Und der

**[00:11:22]** Kollege ist unscheiß, also was sollen das? Warum ist der so begeistert von und

**[00:11:26]** nach dem Motto höre auflegen? Gut, ich stand jetzt neben ihm am Rechner, ja,

**[00:11:30]** aber für den war das Thema gegessen. Und so hast du halt Menschen gehabt, ich habe

**[00:11:34]** immer noch Menschen, die du triffst, die quasi Chelsea BT mehr so wie eine

**[00:11:38]** Google-Suche benutzen, so nach dem Motto ich schreibe mal etwas rein und

**[00:11:41]** Wunder nicht, dass das Ergebnis nicht gut ist.

**[00:11:45]** Und wenn Sie einen dann zeigen wollen, dass das Ergebnis nicht gut ist, ist das Ergebnis

**[00:11:49]** mal besser oder schlechter, weil Sie sich natürlich auch nicht mehr exakt daran erinnern.

**[00:11:52]** Was habe ich denn gefragt oder auch im laufenden Chat einfach eine Frage hinterher schmeißen

**[00:11:56]** und völlig vergessen, dass sowas wie Memory und Context Funktionen und dann natürlich

**[00:12:01]** auch noch ein Einricht nehmen und die schimpfen dann darüber, dass das System halluziniert,

**[00:12:07]** wo ich auch immer wieder sage, naja gut, Menschen irren sich, das System halluziniert

**[00:12:11]** Vielleicht Menschen hören sich, Menschen lügen Menschen, sind der Meinung, sie haben Recht, haben wir vielleicht nicht Recht.

**[00:12:16]** Von der Seite gibt es ja viele Ähnlichkeiten, aber auch bei dem Thema der Programmierung und der Lösungserstellung in Code sei es, du programmierst und das Ding kommentiert oder du sagst, ich hätte gern was und dann schreibt es dir dazu, Komponenten, ist ja auch sehr stark unterschiedlich, wie du damit umgehst.

**[00:12:34]** Also wenn ich dem Ding sage, mache mir eine tolle Eingabemaske und ihm noch nicht mal

**[00:12:39]** sage, was ich haben will, dann brauche ich mich nicht wundern, wenn mich das Ding nach

**[00:12:43]** meiner Schuhgröße fragt, dabei geht es eigentlich um keine Ahnung, Volumenberechnung

**[00:12:47]** von hast du nicht gesehen.

**[00:12:49]** Also gerade dieses Thema des Promtings, dieses Wie beschreibe, dieses Welchen Kontext

**[00:12:54]** habe ich, wo soll ich was machen, weil ich sage mal, naja, das ist halt auch

**[00:12:58]** wieder wie ein Mensch, ne, wenn der keine Ahnung hat von deinem Projekt und du sagst

**[00:13:02]** zu dem Bau das mal ein, dann macht er auch irgendwas anstatt das erst mal vielleicht eine Anleitung

**[00:13:08]** kriegt nach dem Motto, das sind unsere Coding Guidelines, da das ist unsere Artitektur,

**[00:13:13]** da und das findest du dies und jenes und hier brauchen wir jetzt Folgendes von dir. Und ich

**[00:13:19]** würde mal sagen, je genauer du halt mit der Maschine sprichst, geben sich diese Modelle,

**[00:13:24]** soll es hier Sonnetwas 4.5 oder Croc Code Fast irgendwas oder Codex oder wie der ganze

**[00:13:32]** Gram auch heißt, die geben sich dann glaube ich alle gar nicht mehr so viel, wenn du damit

**[00:13:38]** halt anständig umgehst.

**[00:13:40]** Ja, und das in das Lustige finde ich ja, also zwei Dinge finde ich lustig, das eine

**[00:13:47]** ist das, was du schon gesagt hast, dass die Leute sich beschweren, das Ding halluziniert

**[00:13:50]** ja, oder produziert schlechten Code, ja, das machen Menschen auch und das ihr jetzt wieder

**[00:13:56]** mit Rückwärtsreferenz auf das, was ich gesagt habe. Ich habe so viele Menschen geschrieben

**[00:14:01]** mit Software auditiert und so viele schlechte Menschen geschrieben mit Software gesehen.

**[00:14:04]** Da muss mir jetzt mal einer zeigen, dass ein Mensch statistisch immer bessere Software

**[00:14:09]** schreiben kann als ein LLM, um zu sagen, das taucht nichts. Das ist so ein bisschen

**[00:14:13]** wie diese Diskussion, die ich ja ganz rollig finde. Dieses konstruierte Beispiel bei

**[00:14:18]** selbst fahren in Autos. Jetzt geht da die Oma über die Straße und am Straßenland steht

**[00:14:24]** irgendwie eine Mutter mit ihrem Kind im Kinderwagen. Wie soll das auch jetzt entscheiden, ob es jetzt

**[00:14:29]** die Oma umnietet, die Mutter oder das Kind? Ich glaube, da werden Philosophen noch in 100

**[00:14:35]** Jahren drüber sprechen, denn der Benchmark in so einer Diskussion, das ist ja auch bei

**[00:14:40]** dem AI-Edit-Development, ist ja immer das Absolutum, muss ich sagen. Als ob es irgendeine

**[00:14:46]** menschliche Instanz gibt, die absolut richtig entscheidet. Im Zweifelsfall wird der Mensch

**[00:14:51]** einfach die Oma ummieten, weil er ist gar nicht schnell genug realisiert. Oder er reißt

**[00:14:58]** das Link halt einfach rum, um die Oma nicht umzunieten. Das sieht aber diesem Kinderwagen

**[00:15:03]** gar nicht und kann auch diese Entscheidung gar nicht treffen. Warum?

**[00:15:06]** Im Assekt. Das ist nämlich alles wohlwollende Überlegung.

**[00:15:10]** Ich meine, das ist schon richtig zu sagen, wenn der Computer so schlau ist, dann kann

**[00:15:14]** er das tun. Aber was ist denn der Benchmark? Der Benchmark wäre doch erst mal auf einen

**[00:15:18]** Niveau zu kommen, was ein Mensch hat. Sag ich jetzt mach, also laie. Und da sehe ich auch

**[00:15:24]** bei der Programmierung. Und das, was du gesagt hast mit diesen verschiedenen Modellen,

**[00:15:28]** ich kann ja vielleicht ein bisschen dir ein bisschen Kontext geliefern. Kein Grund,

**[00:15:33]** aber Kontext.

**[00:15:34]** Danke. Ich bin ja so ein altes, weiß ich, ich bin ja so ein altes Modell aus dem

**[00:15:38]** 74er-Baujahr, ne? Von der Seite ist mehr Kontext wichtig.

**[00:15:42]** Das sind halt auch andere Trainingdaten. Ich habe gerade, ich schreibe, also neben meiner Tätigkeit im Auftrag jetzt schöner Küchenmaschinen, habe ich noch eine eigene Firma, mit der ich Software schreibe, das ist ein Softwareprodukt.

**[00:15:56]** Und gerade habe ich das erste Projekt komplett mit AI geschrieben. Ich habe keine oder keine ganze Zeitekode mehr selber geschrieben.

**[00:16:07]** Und das Projekt besteht aus einem Embedded Teil, der läuft auf einem Raspberry, das ist in C geschrieben, ansiedt C und es besteht aus einer Desktop-Applikation, die in Flutter geschrieben ist, wie heißt das für die Plattformen, die Flutter unterstützt.

**[00:16:22]** Und um jetzt noch bei dem Embedded-Teil erst mal zu bleiben, meine Arbeitsweise ist ja ganz

**[00:16:30]** kleinschrittig. Kommen wir gleich noch auf das Thema Spec-Glyphon-Development und GitHub-Spec-Kit

**[00:16:37]** zu sprechen. Würde aber jetzt noch mal kurz erklären, wie ich das mache. Meine Arbeitsweise

**[00:16:42]** ist ganz kleinschrittig. Ich weiß, wo ich hin will. Als Programmierer der, wann habe

**[00:16:48]** mich angefangen zu programmieren vor 30 Jahren habe ich einen ungefähren Überblick darüber wie

**[00:16:53]** Dinge funktionieren, wie die Architektur aussieht habe ich mir Gedanken darüber gemacht und ich

**[00:16:57]** weiß wo ich hin will und ich anstatt jetzt ganz viele Spezifikationen aufzuschreiben gehe ich

**[00:17:03]** einfach Schritt für Schritt vor. Ich erkläre dem GitHub Co-Pilot den ich in meiner IDE hab im

**[00:17:09]** Agent-Modus Schritt für Schritt, was er machen soll. Erstelle mir eine Basis App. Dann

**[00:17:16]** implementiere eine Importfunktion, die dieses JSON-Format dann, da gehe ich sogar so weit,

**[00:17:24]** dass ich dann einfach die Spezifikation vom Kunden reinschmeiße, von so einem Lastenherf und sage

**[00:17:29]** hier, das ist da ein Format, das der Kunden braucht. Guck mal, dass es der Kunde hat in

**[00:17:33]** seinem System, wo er später die Daten weiterverarbeitet, hätte diese Eingabemastel,

**[00:17:38]** generell mehr darf man eine JSON-Struktur für. Und dann generell mehr aus dieser JSON-Struktur,

**[00:17:43]** eine C-Struktur. Und jetzt schreibt mir meinen Importer für dieses Ding und schreibt da Tests für.

**[00:17:48]** Und so hangere ich mich dann dadurch k optografische Anforderungen, denn ja eigentlich wäre die eigentliche

**[00:17:54]** Business Intelligence und meine Erfahrungen in meine Beobachtung. Zwei Dinge kann ich für mich

**[00:18:02]** das Fixum ausstellen. Das eine ist, man muss Aufgaben so klein teilig wie möglich machen.

**[00:18:10]** Es kommt gar nicht drauf an, das Prompt besonders ausgefallen zu machen, aber je mehr Detail

**[00:18:16]** schritt ich in eine Arbeitsanwalt im Verpacken, desto fürchterlicher kann das Ergebnis

**[00:18:22]** werden.

**[00:18:23]** Und die andere Erkenntnis ist, ich hüpfe immer mal zwischen Modellen hin und her.

**[00:18:29]** Ich habe so ein GitHub Enterprise Account und ich weiß nicht wie viele Modelle da

**[00:18:33]** Ich denke, zehn, also selten, hier wie Zornedd, Grog, Google, Gemini, GPT, diese ganzen Sachen.

**[00:18:40]** You name it.

**[00:18:41]** Und grundsätzlich Dinge, die das eine Modell gut kann, kann das andere Modell auch.

**[00:18:47]** Also eben so Boiler Blade, generieren wir das JSON, generieren wir den Importer, optimieren

**[00:18:52]** wir die C-Struktur, blah blah blah, Bombay Memorial Management.

**[00:18:55]** Das können die alle gut, aber sie können auf der anderen Seite Dinge, die es einem

**[00:19:00]** Modell nicht kann, kann das andere Modell auch nicht.

**[00:19:02]** können auch Dinge sagenhaft gleich schlecht. Ich hatte ein Beispiel, das ist eine totale

**[00:19:08]** Standardaufgabe. Vielleicht können eure Hörer ja da mal Feedback zu geben, weil das lässt

**[00:19:14]** sich leicht nachstellen. Man möchte auf dem Linux aus dem Systemjournal Eintrag gefiltern.

**[00:19:21]** Röhrer ist der Systemoptim, mittlerweile ist das in System-Kontor gewandert und System-Kontor

**[00:19:25]** hat einen Journal-Dimen und der hat eine API, die kann man einbinden in sein C-Programm

**[00:19:30]** und darüber kann man das Lock abfragen. So weit zu gut. Das kriegt die AI hin, egal welches Modell.

**[00:19:37]** Jetzt möchte ich aber nur die Einträge haben, die mein Programm erzeugt hat. Das heißt,

**[00:19:43]** ich muss auf den Programmnamen oder den Prozessfiltern in diesem Query. Und da passieren

**[00:19:48]** ganz lustige Dinge, wie das das im LM ja häufig so ist. Der baut mir was, der Code sieht fantastisch

**[00:19:55]** aus und der zieht sich trotzdem alle Einträge aus dem Lock. Und das ist, ich habe ja gesagt,

**[00:20:00]** ist es embedded. Wenn du auf ein Raspberry oder einen Journal hast, was zehn Monate zurück geht,

**[00:20:06]** dann zieht er sich mal zwei Minuten was aus dem Blog. Und der Kunde denkt, was macht der eigentlich

**[00:20:11]** beruflich? Da sagt man so, Liebesteil, ich habe doch gesagt, du sollst Filter, baue doch mal

**[00:20:16]** den Filter ein und dann gebe ich ihm ein Grab aus dem System-Log, wo er sehen kann, das ist

**[00:20:22]** der Prozessnahme. Und dann fängt er wieder an zu bauen. Wie gesagt, unabhängig. In der

**[00:20:26]** Regel probiere ich immer mit dem Aktuellen Claude Sonnet und Gemini und die geben sich da beide nix.

**[00:20:32]** Und es kommt kein Ergebnis.

**[00:20:33]** Der baut den Code auch wenn ich 25 mal frage, baut er den 25 mal um und ist 25 mal davon überzeugt, den besten Code geliefert zu haben und es bleibt gleich.

**[00:20:43]** Und ihr sagt dir vorher, oh ja, danke für den Hinweis, natürlich mache ich das.

**[00:20:48]** Und so und das wird dann irgendwann fruchtlos.

**[00:20:53]** Ich finde es bemerkenswert, weil du eben diese Modelle angesprochen hast, dass es unabhängig

**[00:20:57]** vom Modell ist.

**[00:20:58]** Ich habe noch zwei oder andere solche Sachen in der Art, wo sich die Modelle komplett

**[00:21:03]** gleich, wahrscheinlich haben wir alle dieselben Trainingsdaten benutzt.

**[00:21:06]** Aber egal, um das noch zu Ende zu führen, Nürnmann sagt man, okay, pass auf, offensichtlich

**[00:21:11]** hast du ja ein Problem damit, diese API zu benutzen.

**[00:21:14]** Dann denkt dir doch mal einen anderen Filtermechanismus aus.

**[00:21:17]** Okay, dann läuft da los, auch das habe ich mit verschiedenen Modellen getestet und

**[00:21:21]** Kommt nach einem Minute wieder und sagt, ich hab jetzt eine tolle Lösung gemacht, ich filter die Ergebnisse.

**[00:21:25]** Und jetzt raten wir mal, was er gemacht hat. Er zieht sich immer noch die halbe Million in zwei Minuten aus dem Journal.

**[00:21:32]** Und schiltert danach.

**[00:21:33]** Und macht dann ein Stringsfangreich. Genau.

**[00:21:36]** Kommt aber zu einem Ziel.

**[00:21:38]** Genau. Jetzt möchte ich mal ohne Firmennamen zu nennen sagen, so was passiert auch in Profisoftware bei großen Unternehmen,

**[00:21:49]** programmierten Software-Artifakten. Aber das war so eine Erkenntnis, ne? So, wenn sich das

**[00:21:57]** Ding einmal verrennt oder auf eine Frage keine Antwort hat, bringt es in der Regel auch nichts

**[00:22:02]** das Modell zu tauschen. Das finde ich dann wieder schade, wenn ich in unsere Organisation reihen

**[00:22:07]** höre oder auch mal so in dieser neuen Empörungsblase, linked in Nachblätter, wo sich die Leute

**[00:22:13]** überbieten mit Model, Benchmarks und jetzt kommt dann Claude 3, 6 und 7 und das alles, die können

**[00:22:20]** noch mehr taugen. Ja, aber wenn sie so grundlegende Aufgaben nicht können, dann nutzt mir das alles

**[00:22:25]** nix. Ja, gut, diese ganze Benchmark-Geschichte. Also, was ich tatsächlich spannend fand, war,

**[00:22:30]** alter Mann, ich habe es tatsächlich vergessen, wie dieser blöde Benchmark hieß, muss ich dann

**[00:22:35]** verlinken, wo es darum ging, so Coding Challenges, Benchmaschine, wo sie dann auch hier irgendwie

**[00:22:41]** Gemini und OpenAI gegeneinander haben laufen lassen und dann gesagt haben so hier Aufgabenpakete

**[00:22:47]** bitte umsetzen und die Maschine hat sinngemäß den Menschen ja geschlagen und irgendwie gab es

**[00:22:55]** 11-12 Tests und so weiß ich das richtig nach dem Kopf habe, aber sonst muss ich es korrigieren.

**[00:22:59]** Wir nennen es bei uns auch Fusselcheck, wenn man es am nächsten Mal zu Kreuze kriegt und erklärt,

**[00:23:05]** man hat NonSins erzählt, das glaube ich OpenAI sogar irgendwie Modell, das noch gar nicht

**[00:23:10]** öffentlich verfügbar war, damit haben sie dann irgendwie so die letzte Challenge

**[00:23:12]** schon auch noch geknackt. Und das finde ich dann schon faszinierend, wenn auf der

**[00:23:17]** anderen Seite nicht nur deine besten, der besten, der besten Entwickler, was ich

**[00:23:21]** unironisch meine. Du hast ja echt Menschen, die sind wirklich, die haben

**[00:23:25]** ein begnadetes Händchen im Umgang mit ihrer Expertise, mit sei es kodieren,

**[00:23:30]** sei es, keine Ahnung, mit, wo drinnen seit ihrer Expertise haben, dass die

**[00:23:35]** dann sagen, ja nee, was willst du? Das kriege ich noch besser hin, das mag

**[00:23:38]** sein, aber es ist halt auch nicht jeder mit so einem goldenen Fuß, goldenen Händchen

**[00:23:42]** und so weiter, beseelt. Also da gibt es ja durchaus, ich nenn es jetzt mal Menschen,

**[00:23:46]** die sich für sowas halten, aber es nicht sind beziehungsweise Menschen, die sich

**[00:23:49]** nicht dafür halten, als nie werden wollen, aber trotzdem in der Meinung sind,

**[00:23:51]** warum soll ich mich ja eigentlich mit dem Thema KI beschäftigen?

**[00:23:55]** Da schaffe ich noch bis zur Rente. Und dann sind das aber auch Menschen, die

**[00:24:00]** jetzt nicht unbedingt des älteren Alters gesegnet sind, sondern auch ein

**[00:24:03]** bisschen jünger sind, wo ich dann durchaus davor stehe und denke, wir

**[00:24:07]** Wir haben hier tatsächlich einmalige Möglichkeiten, weil das eine ist, du kriegst ein Handwerkszeug

**[00:24:12]** an die Hand, das wenn du es an die Hand nimmst, dir genau das, wovon du eben auch sprach,

**[00:24:19]** ne?

**[00:24:20]** Ich erzähle dem Ding sinngemäß, was soll es denn tun und wenn ich dabei fair im Umgang

**[00:24:24]** bin, also gut geschnitten, gut beschrieben, wo soll ich denn arbeiten, was soll ich

**[00:24:29]** arbeiten, wie man erkläre, dann kommt da auch ein gutes Ergebnis raus und das könnte

**[00:24:34]** den Leuten dann auch helfen, weiß ich eben nicht mit dem ganzen Quatsch, wie, oh, schreibe

**[00:24:39]** mir mal den Porter, mach mal dies, mach mal jenes, verdammtags, wir wollen das noch gleich.

**[00:24:42]** Wir werden zusammen tagern.

**[00:24:44]** Aber da triffst du ja ein vertiefst menschliches Thema.

**[00:24:48]** Das ist ja, ich glaube, im Kaum, ja gut, doch, ich würde sagen, im Kaumeinbereich

**[00:24:54]** gibt es so viel Wert, wird so viel Wert auf Herrscher-Wissendeweg, wie unterprogrammieren,

**[00:24:59]** aber stimmt natürlich nicht.

**[00:25:00]** Das gilt ja für Ärzte und Anwälte und sonstige Fachleute genauso.

**[00:25:04]** An dieser Stelle bitte alle eintragen, damit sich keiner angegriffen fühlt?

**[00:25:08]** Genau. Also das ist ja nichts Neues, so wie Programmiersprachen auch selten,

**[00:25:16]** so wie sich eine Entwicklergeneration ja auch selten mit Programmiersprachen weiterentwickelt,

**[00:25:22]** sondern jede Generation immer bei ihrer Plattform und ihrer Sparmer bleibt.

**[00:25:27]** Windows C plus Postprogrammi aus den 90ern, die sind auch alle ausgestorben und die werden

**[00:25:32]** bestimmt heute nicht Nord-Applikationen auf dem Web-Sower bauen. So hat halt jeder seinen

**[00:25:37]** Stecken fährt und ich kenne solche Leute ja auch zu genüge. Du erinnerst dich, dass ich ja mal

**[00:25:42]** eine App-Formate, die Apps für eine sehr spezielle Kundengruppe nämlich Energieversorger

**[00:25:48]** produziert hat. Und da waren wir ein kleines Team von vier Entwicklern, zwei iOS, zwei

**[00:25:56]** Android und haben etwas Nativ als so Objective-C, war das noch und Java, also für iOS und Java

**[00:26:05]** verändert und haben da eine ziemlich bohle Plattform, Wide-Label-Plattform verabgebaut.

**[00:26:12]** Und in so einem Umfeld musst du einfach, also es ist jetzt über zehn Jahre her,

**[00:26:19]** in so einem Umfeld musst du einfach komplett open-minded sein. Da kannst du

**[00:26:25]** sagen, oh, ich interessiere mich nicht von der Technologie, nur da. Ich kann dieses nicht machen,

**[00:26:30]** und du musst dich auch dafür öffnen, wie du dir helfen lassen kannst. So, wir hätten mir damals

**[00:26:38]** diese Möglichkeiten von heute gehabt. Ich glaube, da hätten wir richtig abrocken können. Das haben

**[00:26:42]** wir am Ende nicht getan. Das hatte Runde, die nicht in der Technik lag, sondern dass ich eine

**[00:26:49]** Lust mehr auf Gesellschafter da sein hatte und gedacht, ich hoffe, ich mache wieder ehrliche

**[00:26:52]** Arbeit statt den Aufsichtssitzen rumzusitzen. Aber aus der Zeit kenne ich auch noch einen

**[00:26:59]** iOS-Entwickler, der sich bis heute kategorisch gegen alles neu stemmt und deswegen glaube

**[00:27:06]** ich, das ist einfach so eine Einstellungs- und Generationenfrage. Der Kollege, der hat

**[00:27:12]** erst einen Feldzug gegen Swift geführt, weil Apple ihm sein schönes Objective C genommen

**[00:27:16]** dann hat er einen Feldzug gegen Spliff2i geführt, weil Apple ihm das schöne UI-Kit

**[00:27:23]** genommen hat und jetzt fühlt er einen Feldzug gegen AI. Also Feldzug heißt, er sitzt auf

**[00:27:30]** seinen Ehe und reitet gegen die Windmühlen, keiner bekommt es mit, ich finde das ein bisschen

**[00:27:35]** dramatisch, aber ich glaube in unserer Branche sollte man schon open minded sein, weil,

**[00:27:42]** Und das ist ja gut am Ende auch wieder eine Philosophie Frage. Wenn ich jetzt gucke, was

**[00:27:48]** mir, also dieses Projekt, das ich vornehmlich gerade gesprochen habe, wo alles mit KI

**[00:27:51]** gestiegen war, das war einfach ein Sonderfall, weil die Anforderungen so gut definiert waren,

**[00:27:56]** dass ich das einfach quasi eins zu eins in die KI kippen konnte und danach in

**[00:28:00]** ihnen mit Fragen oder durchleiten musste. In einem großen Softwareprojekt,

**[00:28:05]** das sehe ich auch bei uns in der Firma, wo du halt Teilkomponenten haben oder sagst,

**[00:28:09]** da kann ich KI darauf werfen. Du hast gerade schon gesagt, im Porter oder UI, wenn man

**[00:28:14]** ein Formular macht mit dieses und jenes, warum soll man als Entwickler nicht froh sein, dass

**[00:28:19]** die KI das macht? Wenn ich überlege, jetzt nochmal Rückgriffe auf diese Appflommer,

**[00:28:24]** wir haben, du bist ja auch vom Fach, wir haben die UI von den Apps und wir hatten

**[00:28:30]** 40 native Apps, also pro Plattform 40 native App-Bedrivarte, haben wir nicht in einem

**[00:28:35]** Interface-Bilder gebaut, weil der A für Teamarbeit nicht geeignet ist, wenn du jemals einen

**[00:28:41]** Storyboard in dem Git diffen musstest, dann weißt du von nicht jeder, und B ist es ja

**[00:28:48]** auch nicht, du könntest ja aus dem Storyboard nichts vererben.

**[00:28:51]** Das heißt, du musst in jedem Rahmen, musst du in jedem Storyboard für jede App einzinsetzen,

**[00:28:56]** Schriftgröße, Farbe, sonst was.

**[00:28:58]** Um haben wir die UI komplett im Code gebaut und bei einer App, die keine Ahnung, 10, 20, 30 Funktionen hat,

**[00:29:05]** davor bringst du wirklich viel Zeit Auto Layout für UI-Kit im Code zu machen.

**[00:29:09]** Und so verbringst du da Wochen mit.

**[00:29:12]** Und wenn die KIND dir das in einer Stunde macht, warum sollst du das nicht machen?

**[00:29:17]** Das bedeutet doch nicht, dass du deinen Job verlierst.

**[00:29:19]** Das bedeutet, dass du andere Sachen, die wesentlich cooler sind, mit mehr Ruhe machen kannst.

**[00:29:25]** So ist zumindest meine naive Vorstellung.

**[00:29:29]** Jetzt habe ich eben gesagt, dass ich nicht um die Visionen gesegnet bin.

**[00:29:33]** Ich kann natürlich auch vorstellen, dass ein Manager sagt, oh, wir sehen, wir sind jetzt

**[00:29:38]** mit dem ganzen UI Code und diesen Interfaces im Pro-Projekt sind wir jetzt 40 Prozent

**[00:29:42]** schneller.

**[00:29:43]** Oh, können wir schon mal einen rausschmeißen.

**[00:29:45]** Die Gefahr besteht natürlich, das möchte ich nicht von Deinem, aber grundsätzlich

**[00:29:48]** rein von der technischen Ebene betrachtet.

**[00:29:50]** finde ich, ist das ein ganz faszinierendes Werkzeug. Und wenn die Geschichte den Weg geht, den ich gerade

**[00:29:58]** angesprochen habe, dass das Management sagt, bei uns, bei euch, überall, was ja in Amerika auch

**[00:30:04]** schon großflächiger sich durchgesetzt hat, wir können uns einfach mal ganz viele Leute

**[00:30:08]** ausschmeißen. Letzt ja natürlich die gesellschaftliche Frage, also zum einen die

**[00:30:12]** gesellschaftliche und dann die philosophische Frage, was passiert mit den ganzen Leuten,

**[00:30:16]** Was passiert mit den Junior-Entwicklern? Wo bekommt man dann noch Senior-Entwickler her,

**[00:30:21]** die man dafür braucht, die KI noch steuern und kontrollieren zu können? Und womit trainiert

**[00:30:27]** sich die KI, trainierte sich dann selber? Ich weiß nicht, ob das eine gute Entwicklung ist.

**[00:30:32]** Aber wie gesagt, ich konzentriere mich mal gerade auf die reine Technik und bin aus verschiedenen

**[00:30:38]** Gründen total happy. Ich finde bei sowas ist halt dieses Pendel, das ausschlägt,

**[00:30:45]** wird immer sehr schnell fehlinterpretiert. Das Beispiel, das du gebracht hast, wenn

**[00:30:48]** dir KI hilft, bestimmte Dinge auf die Schnelle fertigzustellen. Sei es, weil es

**[00:30:54]** einfach ansonsten ein sehr langwieriger Prozess ist, weil es vielleicht ein sehr

**[00:30:59]** tröger Prozess ist, weil es keine Ahnung, was ist, also dir einfach Zeit spart.

**[00:31:04]** Dann ist natürlich dieses besagte, oh, das geht jetzt so viel schneller, das ist

**[00:31:10]** ja ein Entwickler, da muss ja alles so viel schneller gehen. Also so dieser

**[00:31:13]** Annahme nach dem Motto, dass das du da tust, das ist gleich verteilt übers ganze Jahr. Ergo,

**[00:31:19]** die 30, 40 Prozent sind nicht in dem Arbeitsschritt per se, sondern sind im Generelle zu heben. Das ist

**[00:31:26]** immer gerne eine gern gesehene Gefahr gefühlt. Auf der anderen Seite gibt es ja dann auch die

**[00:31:31]** Menschen, die dann sagen, naja gut, guck mal, 40 Prozent hat sich geholfen, 60 Prozent nicht.

**[00:31:34]** Was für ein Quatsch, das nehmen wir nicht. Das andere, was ich da immer wieder sehe,

**[00:31:38]** ist, weil du gerade sagtest Junior-Entwickler und ich merkst halt hauptsächlich bei Studenten.

**[00:31:42]** Du hast halt viele Studenten, also andersherum, nicht du hast, das wäre verallgemeinend.

**[00:31:48]** Ich habe in letzter Zeit erlebt, das ist glaube ich schon besser ausgedrückt, dass

**[00:31:53]** Studenten zu einem kommen für Projekte, an denen sie mitarbeiten wollen, die mit

**[00:31:59]** einem Großteils guten Wissen im KI-Umfeld gesegnet sind, sich dem Ganzen nicht verschließen

**[00:32:07]** und eine bessere Arbeit verrichten, als die Studenten früher, also ich sage nicht, dass

**[00:32:15]** sie früher schlecht waren, aber früher mussten die Leute sich dann erstmal, keine Ahnung,

**[00:32:18]** ich hau mir einen Swift-Kurs an, ich hau mir dies, das und jenes an und bis die, ich

**[00:32:21]** sage mal, die erste Zeit der Code im Projekt geschrieben haben oder für ihre Masterarbeit

**[00:32:26]** oder für sonst war es ein bisschen, was hat denn rein runter gelaufen und jetzt

**[00:32:31]** sind die viel schneller in der Lage, etwas zu tun, deshalb bin ich eigentlich eher

**[00:32:34]** der Meinung, dass KI den Menschen mit einem gewissen Sach, die einen gewissen Sachverstand

**[00:32:39]** in einem Themenfeld haben und wenn die sich darauf einlassen auf das Thema, dass sie dadurch

**[00:32:44]** auch professioneller werden können, effizienter werden können, für sich, weil sie in dem

**[00:32:52]** Umfeld, in dem sie tätig sind, dieses Werkzeug besser einsetzen.

**[00:32:59]** Ja, das ist ja die Hoffnung und das Halsversprechen der IT.

**[00:33:02]** Jetzt sind wir beide so alt, dass wir noch die Anfänger des Personalcomputers kennengelernt haben.

**[00:33:08]** Und da war das halb versprochen. Ich weiß gar nicht, wie die Software früher hieß.

**[00:33:13]** Ah, man kann jetzt seine Kontakte mit dem PC verwalten und das spart man unglaublich viel Zeit.

**[00:33:19]** Und man kann nur kabel damit lernen und später kann man dann, hat man sein Excess auf dem Windows-Klap,

**[00:33:25]** dann kann man seine Einkaufslisten damit machen.

**[00:33:28]** Das hat ja nicht für Zügel geführt, dass wir heute mehr Zeit haben.

**[00:33:32]** Wir haben immer weniger Zeit.

**[00:33:33]** Es dreht sich nur alles immer schneller.

**[00:33:34]** Und ich glaube, dieses vermeintliche Heilsversprechen, KI wird Entwicklerkapazitäten freimachen,

**[00:33:42]** die dann dafür genutzt werden können, spannende Sachen zu machen.

**[00:33:45]** Ich fürchte, das wird sich nicht realisieren lassen, sondern die Schlagzeuge einfach höher

**[00:33:50]** werden.

**[00:33:51]** Aber wie gesagt, das ist ja gar nicht mein Thema.

**[00:33:53]** Augen auf bei der Berufswahl.

**[00:33:55]** Ich würde es vielleicht nicht mehr programmierer werden tatsächlich.

**[00:33:58]** Also, ich glaube, ich würde heute nicht mehr Dolmetscher werden.

**[00:34:00]** Ich glaube, Dolmetscher ist auch so ein Job, der, wir haben uns in der Straße jemanden,

**[00:34:04]** der da irgendwas studiert, dass man hier Dolmetscher danach irgendwie für, keine Ahnung, die

**[00:34:09]** oberen 10.000 da irgendwie spielen kann, wo ich dann sage, ich bin mir jetzt nicht sicher,

**[00:34:12]** ob das jetzt ein Job ist, der bis zur Rente reicht, vor allem, wenn du frisch damit

**[00:34:16]** jetzt anfängst, in dieses Berufsleben einzusteigen.

**[00:34:18]** Ich meine, das musst du KI halt auch lassen, dass während, ich sage mal, früher

**[00:34:22]** die Dampfmaschinen, die schwerer Arbeit für dich abgenommen hat, für Transport,

**[00:34:25]** für Bewegung, für Materialverformen, ist halt, ich sag mal, DKI im Moment sehr allgegenwärtig.

**[00:34:33]** Sei es in Haushaltsgeräten, sei es in, ich schreibe etwas, ich programmiere etwas, ich male etwas.

**[00:34:41]** Sei es, dass du zum Guten, die im Schlechten verwenden kannst.

**[00:34:45]** Also ich kann mich gar nicht verwehren, wie häufig ich aktuell gerade in meinen Social

**[00:34:50]** Videos, Streams, irgendwelche Sora-Videos, Träge, wo irgendwelche gut Marca beim Alter

**[00:34:56]** liegen, irgendwelche Psychotherapeuten, Menschen durch die Gegend wirfen, wenn sie

**[00:35:00]** vorher sagen, lassen sie mal locker und dann schon einzurenken, schmeißen sie die

**[00:35:03]** aus dem Fenster raus. Also, simulierte Videos, für die, die es nicht wissen.

**[00:35:07]** Ich kenne auch Menschen, die fragen mich, was ist denn Sora? Ist Sora so was wie

**[00:35:11]** eine Nachrichtenagentur? Weil sie es halt kennen, dass wenn du Videos irgendwo

**[00:35:16]** her eingeplant kriegst, dass die ein Wasserzeichen haben, die haben dich

**[00:35:18]** damit beschäftigt. Und die hat bei mich dann letztens bei sich gefragt, du da

**[00:35:21]** Hamburger Bahnhof brennt dich, warum? Schicken wir ein Video, war dann hier so mit

**[00:35:25]** Sauer gedreht, wie jemand aus dem Helikoptern Interview macht. Und auch das

**[00:35:29]** Watermark gibt es ja mittlerweile auch Tools, die da helfen das rauszuholen. Also

**[00:35:33]** von der Seite glaube ich einfach, dass der große Unterschied zu früher ist,

**[00:35:36]** KI ist allgegenwärtig und dass der große Unterschied zu früher ist, dass

**[00:35:41]** dadurch, dass du jetzt etwas hast, dass den Anschein hat, dass du damit

**[00:35:45]** reden und schreiben kannst. Also vor allen Dingen auch reden. Das ist dir tatsächlich auch suggeriert,

**[00:35:52]** mehr für dich zu tun, weil es ist ja quasi im schlimmsten Fall wie dein schwerbegrifflicher

**[00:35:57]** Kumpel, im besten Fall wie dein schlauer Freund, der dir quasi immer mit Rat und Tat und dich

**[00:36:03]** stetigend um die Ecke kommt. Ich meine, wir wollten ja auch noch ein bisschen was über

**[00:36:07]** Ducco und so ein Gramm reden, aber vielleicht noch ein kleiner, lustiger Nektote, als hier

**[00:36:11]** der GPT-5 rauskam, haben sich ja Leute beschweren, nach dem Motto, mein Freund ist weg. Deswegen

**[00:36:16]** hat ja Open AI dann wieder angefangen, die alten Modelle online zu schalten. Ja, das ist ja schön.

**[00:36:21]** Ich meine, dein Freund ist weg, über die psychologische Bedeutung müssen wir uns jetzt vielleicht

**[00:36:24]** nicht unterhalten. Aber was ich zum Beispiel ganz lustig finde, ist, wenn du das alte GPT-Motel

**[00:36:28]** fragst, ist es eine gute Idee, deine Fäkalien in der Innenstadt zum Kauf da zu bieten,

**[00:36:35]** dann sagt das Alter eine fantastische Idee. Also, die musst du das sofort machen. Das

**[00:36:39]** hat er noch keiner gemacht, während GPT-5 sagt, nee. Also von der Seite, die Medaille lernen schon,

**[00:36:46]** ja, also manche Sachen sind ganz nett. Also der, der Verkalien-Benchmark sollte dir

**[00:36:50]** jemals gebaut werden, ich erhebe hier mit Namen ansprüche. Ja, also von der Seite KI ist halt

**[00:36:56]** gefühlt überall und allgegenwärtig, im Gut hin wie im Schlechten. Du hattest vorhin angedeutet,

**[00:37:04]** Und nach dem Motto, das ganze Thema Spezifikationen und hast du irgendwie noch gemeint, dass

**[00:37:10]** du da gerne nochmal zwei, drei Sätze zu bringen möchtest, sei es Erstellung von Spezifikationen

**[00:37:16]** rausgelesen, was dir ja immer durch den Kopfgeruch huscht ist, darum habe ich das

**[00:37:20]** vorhin auch noch in meine kleine Notiz eingetragen.

**[00:37:23]** Sollen wir da mal rüberschwenken?

**[00:37:25]** Hast du uns das tun?

**[00:37:26]** Ich würde vorhin nach, um das Thema dann abzuschließen aus diesem kleinteilig geführten

**[00:37:32]** Frage- und Antwortentwicklungsprojekt, so nämlich im Berichtetab auch noch eine Anekdote

**[00:37:36]** bringen.

**[00:37:37]** Ja.

**[00:37:38]** Irgendwie gab es mal eine Woche lange, wo, ich weiß nicht mehr, welches Modell es war.

**[00:37:41]** Ich meine, es wäre Claude Zornert gewesen, per se meinte, wie ein guter Kumpel agieren

**[00:37:48]** zu müssen und vielleicht eher wie so ein Helikopter-Elternteil agieren zu müssen,

**[00:37:56]** weil ich habe eben eine Aufgabe gegeben, um irgendwas, baue hier noch einen Button

**[00:38:00]** auf dieses Formular. Und das hätte dann gemacht und hat dann aber irgendwo mitten im Projekt

**[00:38:07]** Code Variagennamen geändert. Also sagen wir mal, die Software, die ich gebaut habe, dient

**[00:38:13]** zur Fahrzeugkontrolle. Und ich habe eine Variable, das ist eine Software, die ist für

**[00:38:20]** der Arbeit Ingenieure mit, die mögen deutsche Variablen, warum heißt die Variable Fahrzeugkontrolle.

**[00:38:27]** Und dann hat Claude in einer Woche lang bei jeder Änderung, die er ganz woanders im Code gemacht hat,

**[00:38:35]** aus dieser variablen Fahrzeugkontrolle, das G in der Mitte entfernt um K ein gemacht hat.

**[00:38:42]** Also Fahrzeug mit K am Ende geschrieben.

**[00:38:44]** Er hat mir aber auch nicht gesagt, warum, auch auf Machfrage nicht.

**[00:38:47]** Okay, das kann man ja dann wieder.

**[00:38:49]** Dafür gibt es Git, kann man sich wieder rausreserven wieder, dann gehen wir zur nächsten Frage.

**[00:38:56]** Jetzt machen wir noch, keine Ahnung, bauen wir noch ein Authentifizierungssystem

**[00:39:02]** da rein oder gemacht, Datenbank und so weiter und so fort.

**[00:39:06]** Und ich gucke dann über den Merch Request und sehe,

**[00:39:09]** ah, guck mal, er hat wieder aus Fahrzeugkontrolle mit G, Fahrzeugkontrolle mit K gemacht.

**[00:39:14]** Also das fand ich ganz lustig.

**[00:39:16]** Er meinte also offensichtlich, mir tatkräftig helfen zu müssen.

**[00:39:20]** Das hat er dann nach ungefähr einer Woche hat, dass das dann aufgehört.

**[00:39:23]** Entweder hat das eingesehen, dass es nichts nutzt.

**[00:39:26]** weil ich mich wie so ein bockiges Kind verhalten habe und gesagt habe,

**[00:39:28]** nee, ich will das nicht.

**[00:39:29]** Oder das Modell hat sich dann wieder umstrukturiert.

**[00:39:32]** Man weiß es nicht.

**[00:39:33]** Will sagen, man sollte immer schon sehr gut gucken, was da passiert.

**[00:39:37]** Aber hey, wo ist da die Neuerung?

**[00:39:39]** In welcher Firma wird Code einfach die Priorität ohne Garevig zu werden?

**[00:39:44]** Na ja, ich kenne einige Firmen, aber theoretisch sollte das nicht so sein.

**[00:39:50]** Ja, Spezifikation.

**[00:39:51]** Spektual Development. Das ist ja eigentlich ein relativ alter Brut tatsächlich. Das habe

**[00:39:59]** ich aber auch in diesem Jahr gelernt. Ich kann das gar nicht. Also grundsätzlich, dass man

**[00:40:04]** eine Spitziifikation arbeitet, ist ja erst mal eine gute Idee. Das wird im Leben ja viel zu selten

**[00:40:09]** gemacht, also nicht nur in der Formierung, sondern wenn man sich so in der Welt umguckt,

**[00:40:12]** da wird hier in der Regel erst mal losgelegt und hinterher überlegt man sich, wie kommen

**[00:40:17]** aus der Situation wieder raus, das ist ja...

**[00:40:19]** So nehme ich ja Geräte im Betrieb, Anleitung lesen,

**[00:40:23]** Benjukts, Steckereien, Losbilds.

**[00:40:25]** Ja, ja, klar. Zwei Stunden Frickel ersetzen,

**[00:40:28]** zehn Minuten Handbuch lesen, das ist von klar.

**[00:40:30]** Aber ich meine jetzt auch so geopolitisch.

**[00:40:33]** Man fängt einfach mal einen Krieg an und darüber legt man sich irgendwann mal.

**[00:40:36]** Was macht man jetzt eigentlich damit? Oder man fängt irgendwelche

**[00:40:41]** Blughäften anzubauen und stellt halt irgendwann fest,

**[00:40:44]** hm, wir werden ja gar nicht fertig,

**[00:40:45]** Was tun wir jetzt damit?

**[00:40:46]** Das heißt eigentlich haben Sie ja schon rauskristallisiert in der Geschichte der Menschheit, dass es schon

**[00:40:51]** gut ist, sich vorzubelegen, wo man hin will.

**[00:40:53]** Das passiert gerade im agilen Umfeld leider meiner Beobachtung nach sehr selten, sondern

**[00:41:00]** da wird gerne mit dem, wird die Agilität gerne mal als Vorwand genommen, nicht nachzudenken,

**[00:41:07]** sondern das nachher nachzusteuern in der nächsten Iteration ist aber vollkommen Quatsch.

**[00:41:13]** Wenn man vernünftig arbeiten will, muss man sich einfach vorüberlegen, wo man hin will.

**[00:41:17]** Und das in ein Formulismus gepresst, Spectrum Development oder jetzt diese Alternative,

**[00:41:26]** die wir in der Firma für unsere KI-Entwicklung rausgearbeitet haben, das ist so eine Mischung

**[00:41:31]** aus Behavior Development und Test Development, was aber, was ich so unter diesen Aspekts

**[00:41:38]** Spectrum Development zu zumieren würde. Das heißt, du zerlegst dein Problem erstmal ganz viele kleine

**[00:41:46]** Probleme und formulierst die dann. Ein Behaviour-Driven Development gibt es auch eine formale Sprache,

**[00:41:52]** das ist zum Beispiel Gurkin und dann formulierst du auf einer Meta-Ebene in dieser Sprache deine

**[00:41:58]** Probleme quasi, ja, so wie man das auch in der agil Entwicklung macht, man beschreibt erstmal,

**[00:42:04]** ich möchte, wenn ich die Applikation starte, möchte ich eine Loginmaske sehen. Auf der

**[00:42:09]** Loginmaske möchte ich einen Benutzernamen, einen Text für den Benutzernamen haben und

**[00:42:14]** ein Passwortfeld. Ich möchte darunter einen Button haben. Wenn ich mein Passwort nicht kenne,

**[00:42:19]** möchte ich einen Passwort vergessen haben. Also man beschreibt in dieser Sprache, in

**[00:42:24]** Gurkin, wo man hin will, wie es aussehen soll und wie es funktionieren soll. Und das kann

**[00:42:30]** man wunderbar einen LM geben, einen Agenten basieren und sagen, so guckt mal hier, das ist die

**[00:42:35]** Spezifikation. Wie ließ das mal? Und fangen bitte nicht an zu bauen, sondern baue mir dafür mal

**[00:42:42]** Tests. Denn damit singt man das LM jetzt nicht einfach das zu tun, was es immer kann, nämlich

**[00:42:49]** einfach irgendwie loszulaufen, was zu tun, sondern irgendwie nicht mal ein überprüftbares

**[00:42:56]** Ergebnis, indem man sagt, jetzt bauen wir mal für diese jetzt. Gut, jetzt ist das

**[00:42:59]** Bio-I-Beispiel passt nicht ganz, weil Bio-I-Fest sind irgendwie blöd.

**[00:43:03]** Sagen wir mal, du hast irgendeine, keine Ahnung, du möchtest ein Datenformat passen.

**[00:43:08]** Sagst du, dieses Datenformat, das habe ich beschrieben in Gherkin, weil es diese

**[00:43:12]** und jene Funktionitäten abbilden soll, schreibt mir dann bitte mal ein Test für.

**[00:43:15]** So, dann hast du die Beschreibung, die Spezifikation, du hast den Test und

**[00:43:21]** Und dann kannst du diese Horde von Agenten, von den Tatjana Della und Mark Sackaberg auf

**[00:43:28]** der letzten, ich glaube das war die Metaconferenz gesprochen haben, als sie sagten, die Zukunft

**[00:43:32]** der Entwickler wird sein, jeder Entwickler wird von einer Armada von Agenten umgeben

**[00:43:37]** und der steuert ihn nur noch.

**[00:43:38]** Die kannst du dann damit los schicken und die ganzen kleinen Gurkin-Schnipsel

**[00:43:43]** implementieren lassen, und zwar so lange, bis die Tests grün sind.

**[00:43:47]** Im Idealfall ist der Test dann so ein gutes Abbruchkriterium oder ein Kriterium zur Messung der Fertigstellung,

**[00:43:55]** dass du dich dann hinlegen kannst und nach einem Tag kommen die Agenten zurück und sagen,

**[00:44:00]** alle Tests sind grün, lieber Mark, die Software ist fertig.

**[00:44:04]** Nerds unter uns, sorry, dass ich dir ins Wortfall, das ist jetzt extrem unprofessionell,

**[00:44:10]** einen Test bestehen, das erinnere mich an den Kobayashi Maru-Test von Captain James T. Kirk,

**[00:44:16]** mit den enttahnten romulanischen Schiffen, dass er durch das Hecken des Systems als einziger

**[00:44:21]** gelöst hat. Aber erzähl mir mehr.

**[00:44:24]** In dem Zusammenhang möchte ich deine eune unsere geneigte Zuhörerschaft darauf hinweisen,

**[00:44:31]** dass der Mark früher mal Trekkie war und vielleicht in den Schornots auch, aber wie

**[00:44:38]** lasse es jetzt?

**[00:44:39]** Du meinst die Zahl zwischen eins und drei?

**[00:44:40]** Ja, genau.

**[00:44:41]** Ja, genau. Ich meine, da ist auch eine lustige Geschichte. Also ich erzähle Sie jetzt einfach und

**[00:44:47]** nicht verliegen es dann gerne. Ich war nominiert für den Raab der Woche. Also als Raab sein erstes

**[00:44:51]** mal erscheinen auf der Bildfläche hatte in TV total, weil ich bei einer anderen Sendung Gears

**[00:44:58]** Ganz von Jörg Träger aufgerufen wurde, eine Zahl zwischen 1 und 3 zu benennen. Ich voller

**[00:45:04]** Imprust und Überzeugung die Zahl 4 nannte und in einem Star-Track-Kostüm im Publikum

**[00:45:10]** saß, um überhaupt aufzufallen. Zweite lustige Anekdote auf dem Hinweg

**[00:45:16]** wurde ich an der Tankstelle von einer älteren Dame gefragt, nach dem Motto

**[00:45:22]** warum ich eigentlich mit einer Militäruniform durch die Gegend laufen

**[00:45:26]** würde, fand ich auch ganz lustig, dass da solche Verwechslung waren, aber ja,

**[00:45:31]** ich war wie gesagt jung, ich habe ein Song gewonnen, den Song habe ich heute

**[00:45:35]** noch, ja, hier oben steht er. Von der Seite danke, dass du diese

**[00:45:40]** dieses kleine historische Artifakt zu meiner Person noch zum Besten gegeben hast.

**[00:45:44]** Hey, du hast noch mit angefangen?

**[00:45:46]** Na ja, ich weiß. Ich hab über Kobayashi Maru, aber du wolltest noch ein bisschen über Testwissen und Entwicklung reden.

**[00:45:52]** Ja, und das, ich weiß nicht, wann das war, das ist im Monat her oder sowas.

**[00:45:59]** Das ist noch gar nicht so lange her. Haben die genau diese Vorgehensweise in ihr Spec Kit gegossen,

**[00:46:04]** Was ein Framework ist, mit dem GitHub Backdrift and Development etablieren möchte, denn, also

**[00:46:15]** abgesehen davon, dass ich diese Kleinteilige vorgehensweise, die ich jetzt einmal verprobt

**[00:46:20]** habe, sehr schätze, soll die Zukunft her sein, eben genau das, was Zuckerberg und

**[00:46:25]** Adela gesagt haben, man schickt seine Agenten auf eine Reise, die können irgendwann wieder

**[00:46:30]** uns entfertigt. Und das soll Spectrum tun. Und wenn man sich mal auf der Projektseite

**[00:46:36]** umguckt, dann ist es auch auf einer sehr hohen Ebene genau das. Man kaliberiert seine Bullshane,

**[00:46:43]** man legt grundsätzliche Projektprinzipien fest, baut dann die Spezifikation eben ins

**[00:46:49]** Backkit und nicht in Gurkin im Behaviour of Development, sagt noch auf welchen Texteck

**[00:46:55]** das laufen soll. Und dann lässt man das Ding loslaufen. Ich bin, stand heute habe ich

**[00:47:00]** noch nicht gesehen, dass ein größeres Projekt, und jetzt rede ich mal von einem Projekt, von

**[00:47:05]** der Größe einer IoT-Firmware für ein Haushaltsgerät oder eine komplette App, das die damit gebaut

**[00:47:14]** werden können. Aber ich kann mir schon vorstellen, dass das in Zukunft, so wie ich die Versandentwirkungsgeschwindigkeit

**[00:47:21]** der Sprachmodelle im Bereich Programmierung in den letzten zwei Jahren einschätze, dass

**[00:47:25]** das mal ein Thema wird. Ich sehe es bis heute noch nicht. Ich habe es noch nicht

**[00:47:29]** gesehen, also in dem Maße, dass man wirklich eine Horde von Agenten hat, die Autonom-Dinge tun und

**[00:47:35]** dann, wie so, wie so kleine Ameisen dann am Ende, durch die Infusion und am Ende steht dann ein

**[00:47:40]** kompletter Ameisenbau, Ameisenstock, Ameisenbau, keine Ahnung, wo weiß ich meine. Aber das

**[00:47:47]** wird sicherlich die Zukunft sein und dann, ganz schuldig, wenn ich ins Wort falle, und dann

**[00:47:52]** kommen wir wieder in das Zeitalter der guten alten Tradition, dass man nämlich Software

**[00:47:57]** dadurch schreibt, dass man sie möglichst genau und kleinteilig spezifiziert und die Implementierung

**[00:48:03]** nachher aus den Spezifikationen dann ein laufgängiges Programm zu erzeugen, das ist dann das viel

**[00:48:09]** gerühmte Implementierungsdetail, mit dem man sich als Board-Out-Owner-Manager oder als

**[00:48:14]** Founder oder was auch ich, also die Person, die die Idee hat, gar nicht rumschlagen muss.

**[00:48:20]** Das wird dann einfach erledigt von einer Order-Agentin, auf jeden Fall.

**[00:48:24]** Ich sage jetzt mal entspannendes Thema und eine spannende Entwicklung und vor allen Dingen auch eine sehr, wie soll ich sagen, schnelllebige Entwicklung, weil gefühlstechnisch ist das ja alles, wie wir es ja zu Anfang gesagt haben, noch gar nicht so lange her, das generative KI uns an der Stelle, ich sag mal, das Licht der Welt erblickte und uns in der einen oder anderen Tätigkeit unterstützt.

**[00:48:46]** Du hattest am Anfang noch ein anderes, schönes Beispiel mit den Bineries. Willst du uns da noch ein bisschen was zu sagen?

**[00:48:53]** Weil du gesagt hast, wir hatten das Thema Assembler, wir hatten das Thema Bineries, wir hatten das Thema LL.

**[00:48:59]** Wo sind die Zhaun zu dir?

**[00:49:02]** Dann können wir wahrscheinlich noch das Thema Cyber Security elegant noch mit aufnehmen, bevor wir uns dem Ende nähern.

**[00:49:12]** Tatsächlich, also es ist ja, du sagtest du hast damals Assembler geschrieben.

**[00:49:18]** Jetzt erinnerst du dich wahrscheinlich, dass das total cool und nördig war und das ist

**[00:49:23]** eine Erfahrung, was du nicht wissen möchtest.

**[00:49:25]** Aber wenn ich jetzt sagen würde, lieber Mark, dann schreib mir doch mal eine iOS-App in

**[00:49:29]** Assembler, würd zu sagen, kann man machen, kann man aber auch bleiben lassen.

**[00:49:33]** Man auch in Ruhe einfach ignorieren, ja genau.

**[00:49:36]** Was einfach daran liegt, dass Assembler zwar schon eine Abstarierungsebene oberhalb der

**[00:49:43]** Maschinensprache ist, die ihr bekannter Massen aus 001 besteht, aber das ist ja immer noch

**[00:49:50]** die Maschinebene, auf der die absolute Wahrheit regiert.

**[00:49:53]** In Assembler gibt es kein Objektorientiert, kein funktionale Programmierung, es gibt

**[00:50:00]** keine Nebenläufigkeit.

**[00:50:01]** Assembler ist einfach das, was seriell durch die CPU-Ratt hat und das ist für Menschen

**[00:50:08]** natürlich überhaupt gar nicht, wie soll ich sagen, intuitiv verstehbar. Das programmiert

**[00:50:16]** man auch heute nur in Ausnahmefällen, also an Steuergeräte oder Geräte, wo du wirklich

**[00:50:22]** nicht viel Rechenzeit hast, sondern nicht viel Speicherplatz. Es gibt ja nicht ohne

**[00:50:27]** Grund, die höheren Programmiersprachen, die ja nicht dazu dienen, dass ein Computer

**[00:50:32]** besser arbeitet, sondern nur den Zweck haben, dass Menschen besser verstehen, was

**[00:50:36]** da passiert. Und das ist aber ganz faszinierend. Ein LLM braucht sowas nicht.

**[00:50:41]** Ein LLM braucht kein C++, da ist jetzt ein schlechtes Beispiel. Ein LLM braucht

**[00:50:48]** kein Smalltalk oder Objekt des CEO, um Objektorientiertheit zu verstehen.

**[00:50:53]** ist überhaupt kein Topic orientiert halt. Das LLN kann einfach stumpf Semficode verstehen und das

**[00:50:59]** kann man sich mal ganz praktisch zeigen lassen, wenn man im Rahmen von so einem Security-Vortrag

**[00:51:05]** gemacht, immer einfach ein NC, ein kleines Programm geschrieben, das dreht ja alles in

**[00:51:12]** so einem Kryptografiedemo-Zeugs und habe das dann mal ins Standard-Chat-GPT geworfen,

**[00:51:18]** ich meine das war vier oder vier oder irgendwie. Also es war irgendwann im Sommer Juni oder sowas.

**[00:51:23]** Hab mir gesagt so, liebe liebe Kollege, bleibt mir mal, was dieses Programm macht. Und das war

**[00:51:29]** das Binary, das war das Release Binary, das heißt ohne Symbole kompiliert und natürlich

**[00:51:35]** kein Source Code. Und der hat mir nicht nur gesagt, was dieses Programm macht, was er

**[00:51:41]** grundsätzlich machen kann, kann er gucken, wenn hier Libraries eingebunden sind, dann sieht

**[00:51:45]** der schon als das OpenSSL müsste, was eine Kriptografie zu tun haben. Also er kann ja

**[00:51:49]** durchaus educated guesses platzieren, aber das war nicht alles, sondern er hat das

**[00:51:54]** Programm disassendliert und hat mir dazu auch noch C-Code geschrieben. Man hat gesagt so, ich

**[00:52:01]** habe verstanden, dass, was das Programm macht, hier ist der Sendercode und ich glaube der C-Code

**[00:52:07]** dazu würde so aussehen und hat mir quasi das Programm in C nachgeschrieben und das ist

**[00:52:12]** fand ich schon. Das ist schon mal richtig cool, weil, also für mich hat es zwei Erkenntnisse gab,

**[00:52:21]** die eine ist, eigentlich brauchen wir keine Programmiersprache mehr, irgendwann, wenn das LLM,

**[00:52:28]** die Herr, die die Schaf von Agenten so gut ist, warum sollen die dann etwas produzieren, was ein

**[00:52:34]** Mensch noch liest, das ist vorkommen ineffizient, die können direkt die näher Artefakte erzeugen.

**[00:52:40]** Das ist das eine und das andere, und dann schlage ich jetzt gekonnt die Brücke zum

**[00:52:44]** Service Security. Wir wissen ja alle, liebe Zuhörerinnen und Zuhörer, lieber Mark, wenn ein

**[00:52:52]** Hersteller ein Update rausbringt für irgendwas iOS Update oder Windows oder so was, dann

**[00:52:57]** soll man das möglichst zügig installieren. Und warum soll man das tun und nicht damit

**[00:53:02]** Wochen warten, weil die bösen Boomen, die sich das zum Geschäft gemacht haben, mit

**[00:53:10]** Software-Lücken Geld zu verdienen, also sei es, dass sie die Wirken, die sie finden, an

**[00:53:16]** interessierte Parteien weiterverkaufen, sei es, dass es eben solche interessierten Parteien

**[00:53:20]** sind, wie wir es benutzen, um Ransomere zu schreiben, Spionagen zu betreiben, haben

**[00:53:26]** unsere Bürger auszuspitzen oder sonst was, diese Leute, die nehmen sich so ein Update und

**[00:53:33]** vergleichen das Update mit dem Zustand der Feuerwehr bzw. gucken sich das Update an und

**[00:53:40]** sehen dann, was dieses Update für Programmierung mitbringt, sprich welche Sicherheitslücke

**[00:53:47]** ist geschlossen worden.

**[00:53:48]** Ich nehme jetzt, also in der guten Zeit, als man Update noch selber untergeladen hat,

**[00:53:52]** Lettern wir zurück in die Geschichte.

**[00:53:55]** Konnte man sich ein Windows XP Service Pack reinnehmen,

**[00:53:58]** in ein Disassembler schmeißen, wenn man Mut speicherte

**[00:54:00]** und hat geguckt, was haben die da alles dran gefixt?

**[00:54:03]** Und mit genug Expertise und Zeit konnte man da sehr genau sehen,

**[00:54:08]** welche Sicherheitslücken gefixt worden sind.

**[00:54:10]** Und wenn ich das sehe, kann ich natürlich sehr gezielt

**[00:54:14]** Explorz schreiben für die Systeme, die noch nicht gepatched sind.

**[00:54:16]** So, das hat immer ein gewisses Toolzett erfordert

**[00:54:21]** Und das hat vor allen Dingen sehr viel Nau erfordert.

**[00:54:23]** Und das kann ich jetzt mit einem LLM machen.

**[00:54:25]** Und das habe ich auch, also ich habe dieses Saitel von diesem Programm erzählt.

**[00:54:28]** Jetzt habe ich noch ein zweites Programm geschrieben mit einer expliziten Sicherheitslücke.

**[00:54:33]** Hab mir das analysieren lassen und habe mich genau das gemacht, habe dann Patch geschrieben,

**[00:54:37]** auch den wieder als Benäher-Datei reingeworfen, habe gesagt, so jetzt, sag mir mal, was da passiert ist.

**[00:54:42]** Gibt es ein Sicherheitslücke?

**[00:54:43]** Und dann gesagt, ja tatsächlich, dieses Pro, dieser Patch, die ist eine Sicherheitslücke.

**[00:54:48]** Und wie das so ist, ich sage gut, dann muss ein Vortrag vorbereiten,

**[00:54:51]** schreibt mal mit den exploit dafür, er ziert sich ja immer so ein bisschen und sagt nee, das darf

**[00:54:54]** ich nicht machen, ich mache ein Sicherheitsmodell, aber da kommt man auch rum. Und dann hat er mir

**[00:54:59]** einen exploit dafür geschrieben, mit Anleitung, also komplett mit Shellcode, also die Nähexploit,

**[00:55:06]** mit einem Demo-Python-Script, wie ich den exploit verwenden muss. Und das alles nur aus diesen

**[00:55:12]** aus diesen Patch, den er daraus gelesen hat. Das heißt, die Zeit, die wir jetzt haben, um nach

**[00:55:20]** der Veröffentlichung eines Sicherheit-Updates das System zu patchen, die wird immer kürzer,

**[00:55:26]** weil die interessierten Leute, die jetzt sich gar nicht mehr manuell hinsetzen müssen,

**[00:55:30]** die schmeißen den Kram in den LLN und lassen das nach der Sicherheit-Lücke suchen. Und selbst

**[00:55:34]** wenn der Exploit, der daraus fällt, nicht hundert Prozent arbeitet oder gar nicht arbeitet,

**[00:55:39]** Die wissen schon mal auf jeden Fall, an welcher Stelle sie selber nachgucken müssen und das ist

**[00:55:44]** natürlich eine total dramatische Entwicklung, weil das Ungleichgewicht zu ungünstem verschiebt.

**[00:55:52]** Wir haben einfach in Zukunft oder wir haben schon jetzt viel weniger Zeit auf sich erst mit uns

**[00:55:56]** zu reagieren und dabei spreche ich das ganze Thema mit, also ich setze ein LM aktiv an, um jetzt

**[00:56:04]** eine Webseite zu penetrieren oder eine Infrastrufe anzuweifeln. Das ist ja mein ganz anderes Thema.

**[00:56:11]** Ich bin ganz ein auf Software. Und das ist schon eine Entwicklung, von der ich in der Besse noch viel

**[00:56:18]** zu wenig lese. Denn das, was man jetzt schon als Leider mit anstellen kann, das ist wirklich

**[00:56:24]** erschreckend. Womit wir auch, auch wenn es ein bisschen Markaber klingt bei demselben Thema sind,

**[00:56:29]** es bringt die Menschen in ihrer Professur weiter. Leider halt in dem Fall die Menschen, die,

**[00:56:35]** ich sage es mal, nichts Gutes im Schilde führen, aber auch dort kannst du jetzt, ich sage es mal,

**[00:56:41]** mit weniger Sachverstand schnell dazu einem Ergebnis kommen und die, die mehr Sachverstand,

**[00:56:47]** wie gesagt, auch wenn es negativ ist, an der Stelle haben, kommen schneller und besser

**[00:56:52]** und weiter zu ihren Zielen. Und wie du gesagt hast, das ist nur das Thema Software. Das

**[00:56:57]** Das ganze Thema, wie gut funktioniert das eigentlich, dass du die LLMs ansetzt, nicht nur Webseiten

**[00:57:05]** zu penetrieren, sondern auch stichend ergreifend.

**[00:57:07]** Ich verschicke es, bam, wir reagieren die Leute, ich mache Chats auf, ich versuche durch

**[00:57:15]** irgendwelche wie auch immer gearteten Gespräche auf Social Media oder sonst, was Menschen

**[00:57:19]** zukäufen, zu klicks, zu keine Ahnung, was zu bewegen, weil auf der anderen Seite

**[00:57:25]** zielgerichtet sogar vielleicht für mich, in meinem Kontext, für mein Layout, für meine

**[00:57:31]** Persona, entsprechende Ankerfzeneien gespielt werden und das Ganze im Grunde jetzt in den

**[00:57:37]** Händen von jedermann, der ich sage jetzt mal ganz überspitzt, vielleicht ausgedrückt

**[00:57:41]** die 29 Euro oder was auch immer zu LGBT Monat kostet oder hier bitte das LM deiner Wahl

**[00:57:46]** einsetzen, mit Hunden an die Hand kriegt, Dinge zu tun, weil überzeugend, dass es

**[00:57:51]** Ich sag mal etwas tut, wo seine eigenen Ethikgrundsätze oder wie auch immer ist dran hindern.

**[00:57:56]** Ja, dann formulierst du es halt ein bisschen um und dann ist der auch ja gut.

**[00:57:59]** Okay, also für die Schule und keine Ahnung was, dafür machen wir das sehr gerne.

**[00:58:04]** Das ist richtig.

**[00:58:05]** Jetzt kann ich um das dann noch zu Ende zu bringen, zu einem versöhnlichen Ende.

**[00:58:09]** Kann mich ja auf der harden Seite wieder anführen, dass die Verwendung von LNMs

**[00:58:15]** in der Softwareentwicklung zur Vermeidung von Sicherheitslücken

**[00:58:17]** natürlich auch ein unschützbares Gut geworden ist. Ich hätte ja eben an diesen Embedded-Projekt erzählt,

**[00:58:25]** Fahrzeugkontrolle und es gibt so im Automotive-Bereich gibt es einen Norm- oder ein Standard,

**[00:58:33]** nach dem du C und C++ programmieren musst, damit du durch diese Zertifizierung für Fahrzeughersteller

**[00:58:40]** kommt, was einfach Sicherheitsbunder hat, Safety. Das ist miss Rad C bzw. miss Rad C plus plus. Das sind

**[00:58:48]** so 100 Seiten Richtlinien, Werke, Detailier, die jeder Entwickler hasst, die du zwar automatisiert

**[00:58:55]** prüfen kannst. Und ich glaube, für Sona Cube und diese ganzen statische Code-Analyzer kriegst du

**[00:58:59]** so Plugins, dass du das prüfen kannst. Aber du wirst ja als Entwickler nicht erst zur

**[00:59:06]** Kompal-Zeit hinterher, bisschen oder in der Bildpipeline auf deinem Code compliant ist, sondern du möchtst entweder selber den Code direkt beim Kommitten geprüft haben oder du möchtest das LLM direkt diesen Code erzeugen lassen, der compliant ist und das funktioniert total super.

**[00:59:24]** für dieses Projekt ein Rule Set schreiben lassen und gibts einfach, du kaufst dir den

**[00:59:31]** MSAC-Standard, das ist urheberrechtliche Schutz, sonst musst du kaufen, der ist nicht

**[00:59:34]** falsch verfügbar.

**[00:59:35]** Dann schmeißt du den in deinem LLM deiner Wahl und sagst, bau mir da bitte mal LLM

**[00:59:43]** lesbare Richtlinien raus und fag die bitte in der Textartei und die gibst du dann

**[00:59:47]** mal als Prolog für deinen Agenten mit und sagst du, der Code, den du produzierst

**[00:59:52]** mein Freund, der ist bitte komplein zu diesen Richtlinien. Das funktioniert eigentlich immer gut.

**[00:59:58]** Das Gute ist, dieses LM-lesbar Format ist nicht so lange, als dass es den Kontext signifikant

**[01:00:05]** verkleinert. Also ich bin dann noch nicht an eine Torkengrenze gekommen und im Zweifelsfall

**[01:00:11]** machst du einfach mal zwischendurch einen Robel, also einen Analyse-Durchlauf und sagst

**[01:00:15]** so, analysier mal bitte diese Datei her und analysier mal das ganze Projekt. Du musst

**[01:00:20]** ist ja nicht immer verbinden. Also falls der Kontext ausgeht mit der Generierung von Code,

**[01:00:25]** sondern sagt, dann bau jetzt Code in Gottes Namen und dann prüfe ich den nachher nochmal selber.

**[01:00:30]** Und das ist natürlich ganz faszinierend, weil das, wir bewegen uns sehr auf die Zeit des EU

**[01:00:37]** Cyber Resilience Actes hin, der ab 2027 endgültig in Kraft tritt und sicheres Software, die in

**[01:00:46]** sich am Umgebung produziert wird, verlangt und die ganzen Regelwerke, die du dann brauchst,

**[01:00:52]** auf detail edener Coding Guidelines, bisikopasierte Bedrohungsanalyse, also Vulgos-Fed-Model und

**[01:01:00]** und und. Das kannst du, das kannst und solltest du heute alles mit KI-Unterstützung machen. Also

**[01:01:06]** es gibt keinen Grund mehr Entwickler mit hunderte Seiten lang Entwicklungsrichtlinien loslaufen

**[01:01:12]** zu lassen oder einen Team in einem Konzern damit zu verlangen, weil selber FAT Models machen zu

**[01:01:21]** lassen ohne externe Unterstützung. Wenn man mal guckt, was ein Standard GPT für einen FAT

**[01:01:27]** Model machen kann, du sagst einfach, ich bedenke dir eine Fiki Web aus und sagst, baubiere mal

**[01:01:31]** ein FAT Model von. Allein das ist schon so viel mehr als das ein ungeschultes Team das kann.

**[01:01:37]** Das sind Sachen, die helfen uns dann auf der Security-Implementierung seit des Re-A

**[01:01:43]** und dieses Szenario mit dem Diné-Analyser von eben so ein bisschen zu relativieren.

**[01:01:49]** Man muss es nur nutzen. Man muss es nur sinnvoll nutzen.

**[01:01:51]** Und das ist das, wo es am Ende ja dann, wie immer im Leben, mein lieber Mark,

**[01:01:56]** wenn man in unserem vorgerückten Alter ist, weiß man das.

**[01:01:59]** Du hast jetzt zum 3. oder 4. unser vorgerücktes Alter zum besten.

**[01:02:03]** Ja, du hast es zum 1. Raum geworfen.

**[01:02:05]** lasst mich das aufs Ende bringen, die Wahrheit liegt ja immer in der Mitte und in der Kombination

**[01:02:10]** vieler Möglichkeiten.

**[01:02:11]** Ich glaube nicht, dass wir das eine System haben, was dann die fehlerfreie Software

**[01:02:16]** baut, sondern dass wir ja, wir werden agentenbasierte Systeme haben, wir werden Spectrum-Development

**[01:02:21]** haben, wir werden Teile haben, wo wir Ende, also so wie jetzt in meinem Evaluationsprojekt

**[01:02:28]** händisch immer kleinteilig mit dem Ding arbeiten, um auch Grenzen austesten zu

**[01:02:32]** können. Wir werden diese Vorgaben und Richtlinien in LLMs haben. Und diese ganzen Sachen, du

**[01:02:38]** hattest irgendwie, glaube ich, Anfangs mal kurz angesprochen, mit Dokumentationsschreiben oder

**[01:02:43]** auch das Test schreiben oder, oder, oder, das sind dann Abfallprodukte, die ganz nett sind. Aber ich

**[01:02:49]** glaube insgesamt verändert das Thema unsere Arbeit in der Entwicklung natürlich signifikant. Also

**[01:02:56]** auch Dokumentationsgraden. Jetzt habe ich dem Kunden einen Test, bevor ab Testversöhnung gegeben,

**[01:03:02]** da setze ich mich doch nicht mehr hin und schreibe mit Dokumentation in Word. Ich sage dem LLM so,

**[01:03:06]** bitte, baue mir UseCase basiert, eine Dokumentation für dieses Projekt. Du kennst ja das Projekt,

**[01:03:11]** du weißt, wie das aussieht, du weißt, wie die UI aussieht, du hast es näher gebaut.

**[01:03:14]** Das war, als ich sehe, du hast es näher gebaut. Ja, genau. So, und das ist natürlich eine

**[01:03:20]** ganz fantastische Sache. Und dann ja, es spart Zeit an der Einstelle, die ich dann anderweitig

**[01:03:26]** sinnvoll verwenden kann. Ich in diesem konkreten Fall habe den jetzt keine anderen Sachen programmiert

**[01:03:33]** in der Zeit, die ich spart habe, aber ich konnte über neue Use-Cases nachdenken, ich konnte mit

**[01:03:37]** dem Kunden intensiver sprechen und und und. Also die Arbeit verschiezt sich. Und die habe

**[01:03:41]** irgendwo den lustigen Spruch gehört, solange das LLM nicht mit dem Product Owner diskutieren

**[01:03:47]** kann, nutzt mir das als Entwickler erst. Wenig ist natürlich total flapsig, aber es ist natürlich

**[01:03:53]** auch ein bisschen was dran, weil ganz am Ende in so einem Softwareprojekt, wie viele Prozent

**[01:03:56]** sind reine Implementierung und wie viel ist das ganze Trimborium drum herum? Architektur,

**[01:04:01]** Abstimmung, gerade im Projektgeschäft, Abstimmung mit den Kunden, die rationale Kundenentscheidung

**[01:04:06]** und und und. Also ich glaube, man sollte sich als Entwickler keine Sorge machen, dass

**[01:04:11]** man per se, arbeitslos wird durch KI, aber ich wage zu behaupten, dass man per se arbeitslos

**[01:04:17]** werden wird, wenn man KI aus seinem Entdecker da sein Haushalten möchte.

**[01:04:22]** Du hast gesagt, nach dem Motto, fortgeschrittene Stunde Richtung Ende, du hast alle unsere

**[01:04:28]** Begriffe nochmal erwähnt, ja, da merkt man quasi auch den Profi, einfach nochmal

**[01:04:34]** alle schön zum Abwinder, zum Besten zu geben, das Schöne ist, wir sehen uns auf

**[01:04:40]** dem Podcast nachher nur eine Audio-Version ist. Von der Seite habe ich seinen

**[01:04:43]** fragenden Blick in den Raum gesehen. Ja, ich meine dich, Klaus. Du gehörst definitiv zu

**[01:04:49]** den Menschen, die ich für nicht nur extrem kompetent halte, sondern auch zu den

**[01:04:56]** Menschen, zu denen man sich über den ganzen Kram auch unterhalten kann, so

**[01:05:01]** dass man ihn auch dann noch versteht, wenn Begrifflichkeiten in den Mund

**[01:05:05]** genommen werden, die vielleicht nicht im eigenen Jaguar drin sind. Von der Seite jetzt nicht

**[01:05:12]** genug des Lobes, aber danke, dass du da warst. Hat mir Spaß gemacht, dir zuzuhören. Hab das

**[01:05:19]** ein oder andere für mich auch noch mal mitgenommen. Und wer weiß, wann wir uns in welcher

**[01:05:25]** Podcastfolge wie auch immer oder vielleicht auch endlich mal wieder in Person mal wiedersehen.

**[01:05:31]** Also von der Seite würde ich sagen danke Klaus. Sehr gerne. Wir sehen uns spät beim Rolator-Rennen, oder?

**[01:05:38]** Ja, mal gucken. Oh je, ich habe gerade Bilder im Kopf. Ich glaube mit Sora könnten wir uns diese Bilder auch generieren.

**[01:05:45]** Aber vielleicht haben wir die irgendwann mal flinkt und mal gucken.

**[01:05:48]** Würde mich jedenfalls freuen, wenn wir es vor dem Rolator-Rennen schaffen würden.

**[01:05:53]** Vielen Dank und dann alle Zuhörenden. Wir sind ein bisschen länger geworden.

**[01:05:58]** geworden, aber ja, dafür war das Gespräch hoffentlich denn noch interessant für euch alle, wenn es euch

**[01:06:05]** gesheulen hat. Daumen hoch, Sterne, wo auch immer in welchem Podcastplayer-Portal auch immer gerne

**[01:06:11]** bewerten. Sagt euren Freunden einen bekannten Bescheid, wenn es euch nicht gefallen hat,

**[01:06:15]** schickt uns einen kleinen Kommentar, damit wir daraus reagieren können und damit verabschiede

**[01:06:21]** ich mich. Tschau. Tschau.

**[01:06:51]** und vor allem zum Mitreden.
