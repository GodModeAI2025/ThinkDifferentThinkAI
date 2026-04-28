---
title: "Anatomie der KI"
episode_index: 31
published: "Mon, 16 Mar 2026 15:59:00 +0000"
duration: "2660"
audio_url: "https://audio.podigee-cdn.net/2394491-m-beaaae30a2bf806c0ea14cae438b74bc.mp3?source=feed"
guid: "e4d58412a05b11c423cb30ccc1fbe25e"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "de"
language_probability: "1"
transcribed_at: "2026-04-28T21:02:08+00:00"
---

# Anatomie der KI

**Veroeffentlicht:** Mon, 16 Mar 2026 15:59:00 +0000
**Dauer:** 2660
**Audio:** https://audio.podigee-cdn.net/2394491-m-beaaae30a2bf806c0ea14cae438b74bc.mp3?source=feed

## Beschreibung

Biologie und KI verschmelzen: Von menschlichen Neuronen bis zur digitalen Fruchtfliege. Die Zukunft wird wilder, als wir denken.
In dieser Folge wagen wir uns an die Schnittstelle von Biologie und künstlicher Intelligenz: Was passiert, wenn menschliche Gehirnzellen in der Petrischale Ego-Shooter wie Doom spielen? Und wie real ist der erste Upload einer Fruchtfliege ins Digitale? Wir diskutieren nicht nur faszinierende Experimente, sondern auch philosophische Fragen zu Bewusstsein, Evolution und der Zukunft von KI.

Wir nehmen euch mit auf eine Reise, bei der die Grenzen zwischen Mensch, Maschine und Natur verschwimmen. Gemeinsam überlegen wir, wie biologische Analogien helfen, moderne KI-Systeme besser zu begreifen – von Neuronen über Stammzellen bis zum digitalen Immunsystem. Hört rein, wenn ihr wissen wollt, warum sich die Evolution auch im digitalen Zeitalter ihren Weg sucht – und was das für unsere Zukunft bedeutet.

Die Biologie der KI
Buch

Cortical Labs
https://www.corticallabs.com/

Doom (Computerspiel)
https://de.wikipedia.org/wiki/Doom_(Computerspiel)

Boston Dynamics
https://www.bostondynamics.com/

Fruchtfliege (Drosophila)
https://de.wikipedia.org/wiki/Fruchtfliegen

Andrej Karpathy
https://karpathy.ai/

OpenAI Gym
https://www.gymlibrary.dev/

GitHub
https://github.com/

AgentHub
https://github.com/agenthub-ai/agenthub

Organoide
https://de.wikipedia.org/wiki/Organoid

Jurassic Park (Zitat: Das Leben findet einen Weg)
https://de.wikipedia.org/wiki/Jurassic_Park_(Film)

## Transkript

**[00:00:00]** Willkommen bei Think Different, Think AI, dem Podcast von Marc und Jens.

**[00:00:07]** Zwei technologieverliebte Köpfe, die nicht nur über künstliche Intelligenz reden, sondern sie leben.

**[00:00:14]** Hier gibt es klare Einordnungen, echte Praxiseinblicke und einen frischen Blick auf das, was möglich ist.

**[00:00:20]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:00:24]** Cardi zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.

**[00:00:43]** Guten Abend, neues Glück. Zumindest, was unsere Aufnahme angeht.

**[00:00:46]** Herzlich willkommen bei Think Different, Think AI.

**[00:00:49]** Ich bin heute nicht alleine, der Jens ist wieder bei mir

**[00:00:52]** und wir haben heute eine Folge.

**[00:00:54]** Wie soll ich denn sagen?

**[00:00:56]** Biologie trifft KI.

**[00:00:58]** Ich würde mir mal behaupten, dass wir ein paar Punkte haben,

**[00:01:01]** die, naja, ich hätte mal gesagt,

**[00:01:04]** gesagt, vor ein paar Jahren wären sie ein guter Stoff, unter anderem für Science Fiction oder auch für Horrorfilme gewesen.

**[00:01:11]** Mittlerweile ist die Technik irgendwie vorangeschritten und wir haben uns gedacht, Freunde der Nacht, wir erzählen mit euch ein bisschen, was im Bereich der künstlichen Intelligenz passiert, die direkt, indirekt Analogien oder auch ganz tatsächlich mit Biologie zu tun haben.

**[00:01:32]** Apropos Biologie, ich begrüße wie gesagt Jens, der in seiner biologischen Form mir digital gegenüber sitzt.

**[00:01:40]** Hallo Jens, schön, dass du da bist und lass uns doch mal gleich einsteigen.

**[00:01:45]** Ich glaube mit einem Spiel, zumindest aus meiner Jugend, als Ballerspiele noch nicht im Elternhaus bekannt waren

**[00:01:53]** und ich sowas noch mit seriellem Kabel zwischen zwei Rechnern gespielt habe.

**[00:01:58]** Hallo Marc, danke für die Einleitung.

**[00:02:02]** Ich hatte kurz panik, dass du auf mein Leistungskurs Biologie zurück gelten wolltest und dich ehrliche Sachen noch sagen müsst.

**[00:02:08]** Da war ich eigentlich nicht mehr so richtig viel von.

**[00:02:11]** Aber vom Spielen habe ich Ahnung und das Spiel, was du glaube ich meinst, ist Doom.

**[00:02:16]** Doom einer der ganz alten Ego-Shooter,

**[00:02:22]** Wo wir das mit das erste mal so richtig geile 3D-Welten in Anführungsstrichen pixelartig grafiken.

**[00:02:29]** Manchmal ist es cool.

**[00:02:31]** Zwei-dimensionale Gegner auch, ich glaube die Gegner waren zweidimensional.

**[00:02:34]** Das waren eher so Spights, die so scherische Sitzsicht ein bisschen bewegt haben vor dem Hintergrund.

**[00:02:40]** Aber das war richtig cool.

**[00:02:42]** Doom ist ein absoluter Klassiker in der Spiegelwelt.

**[00:02:46]** Und dementsprechend war, als die Kollegen von Cortical Labs,

**[00:02:51]** ich erzähle euch gleich, wer es die so machen, aufgerufen haben, also das Internet aufgerufen haben,

**[00:02:56]** zu fragen, was könnten wir da auf dem Cortical Labs-Rechner noch so alles machen? Hat das

**[00:03:02]** Internet natürlich geantwortet, lass es mal Doom spielen. Was macht Cortical Labs denn eigentlich?

**[00:03:08]** Cortical Labs ist eine Firma, die menschliche Gehirnzellen nimmt, die in der Petrischale quasi

**[00:03:15]** sie züchtet und die, also keine Tierzellen, menschliche Gehirnzellen, die werden gezüchtet

**[00:03:23]** in der kritischale Briemer, das immer so macht, weil sie das ganze Hexenwerk, das

**[00:03:26]** diese ganzen Alchemisten und Biologen und so was da eigentlich nach oben machen, na äh.

**[00:03:31]** Heute wollen sie Gold erstellen, heute machen sie Gehirnzellen, aber egal.

**[00:03:35]** Ja, komm, ja auch ein paar gute Sachen raus, aber ja, wir sind halt auch ein bisschen

**[00:03:38]** Magic und Spooky teilweise und das ist ja in der Katowice Spooky, also die Züchtern

**[00:03:42]** quasi. Ein neuronales Netz aus 200.000 Neuronen, die aus menschlichen Gehirnzellen bestehen.

**[00:03:53]** Diese kann man dann genauso benutzen wie ein künstliches neuronales Netz, wo wir die

**[00:04:01]** ganze Zeit hier in unserer Folge mit überreden, sondern in der sogenannten KI, die gewisse

**[00:04:04]** Sachen machen kann. Also dieser Petri Schade, die lebt dann quasi auf so ein Mikroship

**[00:04:08]** und interagiert mit Elektronen außen rum, die hat auch so ein Rack, ist wie so ein Server-Rack,

**[00:04:13]** diese Firma kannst du quasi auch ansprechen und rechnen leistet, also rechnen menschliche

**[00:04:20]** Rechnen leistet wieder, wie die alten Computer, damals waren ja auch erst mal Menschen,

**[00:04:24]** bevor das dann anders rum ging und in diesen Fall schießt.

**[00:04:27]** Ich habe zuvor auch gelernt, dass damals die Menschen bei der NASA die Mathematik

**[00:04:31]** Aufgaben gemacht haben, auch Computer, genannt wurden.

**[00:04:35]** Ja, das war das, was ich referenziere.

**[00:04:38]** Der Kreis schließt sich gerade.

**[00:04:41]** Jetzt ist der Mensch, der sich guckt, Mutua,

**[00:04:44]** erst mal nicht mehr ein echter Mensch,

**[00:04:47]** sondern in Anführungsstrichen in Ruhe seine Gehirnzellen.

**[00:04:51]** Diese Gehirnzellen in diesen Wachstums wirklich geschafft, umzuspielen.

**[00:04:54]** Wie gesagt, das teilen wir auf jeden Fall.

**[00:04:56]** Schauen wir uns, guckt euch das mal an.

**[00:04:58]** Es ist so crazy abgefahren, spooky,

**[00:05:02]** Bukki, du hast auch immer, aber auch wieder eine Sache, die gerade so passiert, wie 1000 Millionen

**[00:05:10]** andere Sachen, die gerade irgendwie passieren, die zeigen, dass unsere Zukunft, den wir will

**[00:05:14]** wird, aber die auch ganz viele Fragen auswählen.

**[00:05:17]** Gerade so passieren.

**[00:05:18]** Hallo?

**[00:05:19]** Ja.

**[00:05:20]** Das sind menschliche Gehirn.

**[00:05:21]** Ja, das ist abgehört.

**[00:05:22]** Die spielen Doom.

**[00:05:23]** Ja.

**[00:05:24]** Also ich weiß jetzt nicht, wie ihr Skill ist.

**[00:05:26]** Ich weiß jetzt nicht, wie ihr Skill ist.

**[00:05:28]** Ich finde auch erschreckend, dass ich sage jetzt mal so ein paar Mühe, Hylnzellen reichen,

**[00:05:34]** um Dumm zu spielen.

**[00:05:35]** Ich dachte früher immer, man muss da ein bisschen schlauer sein.

**[00:05:38]** Was mich dann sofort irgendwie mit der Frage bringt, wie darf man das denn jetzt einstufen?

**[00:05:45]** Ich meine, man ist ja immer wieder mit der Frage auch beseelt, wenn du mit Tieren zu

**[00:05:49]** tun hast, wenn du mit Flanken zu tun hast, was wird quasi über die Sensorik wahrgenommen,

**[00:05:54]** Schmerz, Angst.

**[00:05:55]** Aber wann haben wir einen Bewusstsein?

**[00:05:58]** Wann haben wir eine AGI und den ganzen Kram, wenn ich mir jetzt überlege, dass Hirnzellen

**[00:06:03]** dumm spielen?

**[00:06:04]** Also wie lange lebt so eine Hirnzelle, lernt die was?

**[00:06:12]** Das weiß ich gerne nicht mehr, ich glaube die sind immer so irgendwie, ich weiß nicht

**[00:06:16]** ob die irgendwie 90 Tage, irgendwas anderes, da müssen wir mal nachgucken, ist gewonnen

**[00:06:19]** ja.

**[00:06:20]** So eine Nähnlösung und so was, wo sind die noch so dumm?

**[00:06:22]** Genau, das ist das Problem, glaube ich, das ist dann irgendwann wahrscheinlich sich selbst

**[00:06:28]** dann vergiftet, whatever, das ist nicht irgendwie ewig, kann nicht ewig leben in dem Moment,

**[00:06:34]** aber die haben das Kotty-Glabs-Satz jetzt in so eine kritische Masse reinbekommen von

**[00:06:40]** der Zeit her, dass das schon ganz gut funktioniert, so ein Rechner insgesamt kostet, dann glaube

**[00:06:44]** ich 30.000 Dollar, da kannst du auch kaufen, theoretisch, da kannst du dir das Ding für

**[00:06:48]** 30.000 Dollar zu Hause holen, hält halt nicht so lange, ich weiß nicht, ob die dann

**[00:06:51]** irgendwie, wie bei Amazon kannst du eine Petrischale, aber bei Amazon, wenn deine

**[00:07:00]** eine Gehirnzellen Petrischale nachgestorben ist, noch mal zur Einordnung 200.000 Gehirnzellen

**[00:07:06]** oder Neuronen, das menschliche Gehirn hat irgendwie 86 Billionen, da ist also noch ein

**[00:07:10]** Gap, der deutlich ist, um die 430.000 Faktor oder sowas ist das dann, weil

**[00:07:18]** für eine weißen 1.000 Fach ist das dann der Unterschied.

**[00:07:21]** Das ist schon noch ein Unterschied, aber genau wie du sagst, diese 200.000

**[00:07:25]** reichen schon aus, um du umzuspielen. Wenn du es dir verlegst, dass es ja diese

**[00:07:31]** Statistik gibt nach dem Motto, ich weiß die Zahl gerade nicht, wie viel Prozent

**[00:07:35]** unseres Gehirns nutzen wir eigentlich. Bin mal gespannt, ja? Was zahlen man dann

**[00:07:42]** am Ende vom Tag kommen, wenn du da, ich sag mal, ein bisschen mehr simulieren

**[00:07:44]** willst, aus simulieren kommen wir vielleicht gleich noch, aber ich bin ja

**[00:07:47]** mal gespannt, ob die irgendwann vielleicht mal so wie ein Chat-Interface da drin integrieren,

**[00:07:51]** ob dann jemand sagt, hallo, um mich hier raus, ja. Ich bin ja eine Kickstarter. Nein,

**[00:07:55]** Entschuldigung. Ja, I don't know. Das muss man auch mal sagen. Natürlich ist immer noch so das

**[00:08:02]** Ding, wenn wir jetzt über künstliche Intelligenz reden, da hätten wir diesen Spagat zwischen

**[00:08:09]** wie gut ist das jetzt vielleicht schon irgendwie als Lebewesen zu bezeichnen,

**[00:08:14]** wenn das da ist, dann ist es immer noch einfach. Da kann man sagen, das ist ein künstlicher

**[00:08:18]** und moraler alles Netz und alle möglichen Verhaltensweisen sind dann irgendwie kopiert.

**[00:08:23]** Jetzt ist es halt so ein Nervenzellen-Netz. Auch da sind natürlich die Verhaltensweisen

**[00:08:29]** werden allen programmiert und dann werden einfach, ja, da laufen elektrische Impulse

**[00:08:33]** durch, genauso wie die, die durch irgendwelche Gewichtungen in so einem neuronalen Netz

**[00:08:38]** durchlaufen. Aber da sich jetzt Gedanken drüber zu machen über dieses künstliche,

**[00:08:43]** dieses künstliche menschliche neuronale Netzdaster aufgezogen worden ist, ob das auch Gefühle

**[00:08:49]** entwickelt, ob das sich nicht eigentlich, genau wie das in der natürlichen Evolution ist,

**[00:08:57]** weiterentwickeln kann und solche Sachen, wenn vielleicht im Prinzip irgendwann diese

**[00:09:01]** pieterschalen Größe werden.

**[00:09:02]** Ich bin jetzt kein Biologe, bin auch kein Chemiker, keine Ahnung, wie die das dann

**[00:09:06]** hinbekommen, dann die Sachen länger am Leben zu erhalten oder vielleicht noch mehr

**[00:09:11]** da reinpflanzen von Anfang an. Also, wann ist dieser Moment erreicht, wo es dann auch tatsächlich,

**[00:09:17]** also ich hätte jetzt, also ganz ehrlich, wenn ich in dieser Firma arbeiten würde, ich hätte

**[00:09:22]** jetzt schon irgendwie so ein bisschen Probleme, diese Pietrischale hinter in den Müll zu werfen.

**[00:09:27]** Weißt du? Also, ich meine, die hat vorher dumm gespielt und dann wirft sie wieder nach in den Müll.

**[00:09:31]** Also, man hat schon wehgetan, als irgendwie die Goldflische von meinem Sohn, die damals

**[00:09:36]** gestorben sind, in den Abflusskeppen musste. Also ich weiß nicht, wie ich das dann jetzt

**[00:09:43]** irgendwie fertig kriegen würde. Und das ist schon irgendwie quasi.

**[00:09:46]** Ja, vor allen Dingen, ich denke dann auch immer an sowas wie, wenn man so Werbung sieht

**[00:09:52]** von Boston, was heißt Werbung? Filmchen von Boston Dynamics und so weiter, wo man

**[00:09:57]** sich dann denkt, ja, das ist das, was man jetzt zeigt. Das, wo man vielleicht

**[00:10:02]** noch sitzt. Neues GPT-Modell, Antraroboter, andere Sensorik oder Klassiker, iPhone, ja. Also

**[00:10:11]** ich meine, es kommt immer, es kommt ein neues iPhone raus, la, la, la. Oder Samsung-Phones,

**[00:10:15]** aber eigentlich wissen die ja schon, sind gemäß, was kommt, das könnten wir der Nächstes

**[00:10:19]** Jahr machen und übernächstes Jahr und vielleicht so ein bisschen, okay, in drei Jahren wollen

**[00:10:23]** wir keine Ahnung, Rotografisch-Displays und wir haben schon unten im Canon ein Prototypen

**[00:10:26]** mit so großes wie ein Schrank. So, groß wie ein Schrank, da passt natürlich ein bisschen

**[00:10:30]** mehr Höhenmasse rein, ist klar, aber nach dem Motto, wo ist das Limit? Und ich fand das

**[00:10:36]** mit Dumm, das fand ich schon mega, ich sag mal, auch krank, ja, in die Vorstellung, weil

**[00:10:42]** egal ob das jetzt Mensch oder Höhen, Mensch oder Höhen, genau. Mensch oder Höhen ist

**[00:10:46]** schön. Das passt zwar manchmal, aber das ist ein anderes Thema, anderes Kapitel. Mensch

**[00:10:52]** oder Tier oder wie auch immer. Das andere Thema war ja, dass mir dieser blöden Fruchtflieg

**[00:10:57]** Magst du das mal kurz erklären, was da passiert ist, weil das ist ja geschült. Auch nochmal

**[00:11:02]** ein extremer Schritt in Richtung, was sind wir eigentlich, wenn man mal überlegt, man

**[00:11:09]** wird digitalisiert. Da bekommt auch Digitalisierung ganz neue Begriff, andere denken, oh, schmeiß

**[00:11:15]** die Schreibmaschine raus und wir holen uns jetzt den Scanner, aber in dem Fall mit

**[00:11:20]** der Fruchtfliege ist das ja anders gewesen. Ja, da ist es ein bisschen so, dass die,

**[00:11:25]** Also das ist auch ein Nachricht, das sieht es glaube ich aus, wenn es in ein, zwei Wochen gewesen.

**[00:11:28]** Da ist jetzt der Weg anders herum.

**[00:11:30]** Da geht es wieder darum, dass wir sagen, wir haben ein künstliches digitales Netzwerk.

**[00:11:36]** Was wir aber in diesem künstlichen digitalen Netzwerk gemacht haben,

**[00:11:40]** ist die neuronale Struktur einer Fruchtfliege.

**[00:11:45]** Fruchtfliege, wir haben beide Sprachprobleme anschaut.

**[00:11:48]** Fruchtfliege nachzubauen, also zu kopieren, so wie sie auch in der Fruchtfliege zu finden ist.

**[00:11:54]** finden ist. Die ist gar nicht so komplex von den Nervenzellen, wie ein Mensch ist gehen,

**[00:11:58]** sind deutlich weniger, deshalb auch einfangen zu bauen. Hat kein Dumm gespielt, aber kann

**[00:12:04]** trotzdem rumfliegen und so, nur rumlaufen und Zucker schwecken und solche Sachen. Also

**[00:12:10]** das kann eine Fruchtfliege erscheinen, die ist jetzt nicht unfähig, würde ich mal sagen.

**[00:12:13]** Was sie gemacht haben ist aber tatsächlich quasi dieses Nervenzellen-Netzwerk,

**[00:12:21]** was eine Fruchtfliege hat, dieses neuronalen Netz der Fruchtfliege, 1 zu 1 in der digitalen

**[00:12:26]** Welt zu kopieren und dann in eine simulierte Fruchtfliege, in einem simulierten Raum, hat

**[00:12:34]** sich dann ganz normal verhalten, wie es sich eine Fruchtfliege aufhalten würde und man

**[00:12:38]** konnte eben prinzipiell aussehen, wie dieses neuronalen Netz eben auch feuert und verschiedene

**[00:12:42]** Drehungsmuster eben abzugefangen, damit diese Fruchtfliege gesteuert wird.

**[00:12:45]** Also das ist so ein bisschen, ich glaube, wenn man Netflix gibt es eine Sci-Fi-Animeserie.

**[00:12:54]** Blicken wir es?

**[00:12:55]** Nee, upload, meine ich.

**[00:12:57]** Ah, upload, ja.

**[00:12:58]** Genau, da geht es darum, dass man im Prinzip so ein bisschen, dass man halt das Gehirn in seiner kompletten Struktur klein schneidet und uploaded in die virtuelle Welt.

**[00:13:09]** dass man eben genau das macht, was man jetzt im Prinzip mit dieser Fruchtfliege macht. Also diese

**[00:13:13]** Fruchtfliege ist quasi der erste Upload, weil wenn man sagen kann, die Fruchtfliege existiert in

**[00:13:18]** der natürlichen Welt jetzt nicht so ewig. Diese virtuelle Fruchtfliege, die wir jetzt erzeugt haben

**[00:13:25]** mit diesem Kopie des neuronalen Netzes, diese Fruchtfliege wird, die können wir sogar forken,

**[00:13:31]** wenn wir die bei Github und Githau hochlachen und dann eben duplizieren ohne Ende. Also die

**[00:13:37]** wird ewig theoretisch existieren, solange wir Bock haben, uns die irgendwie selber zu laden.

**[00:13:41]** Das heißt, das ist tatsächlich so ein erster Upload Case, wo natürliche Intelligenz in

**[00:13:47]** einem virtuellen Raum reingeladen wird, das da nichts damit zu tun hat, dass ich irgendwie

**[00:13:54]** Training machen muss, ein Modell trainieren muss, ein neuronales Netz trainieren muss,

**[00:13:58]** sondern ich nehme im Prinzip mal 1 zu 1 Kopie eines bestehenden neuronalen Netzes in der

**[00:14:03]** natürlichen Welt und lade es in die virtuelle Welt hoch und sie beweisen, dass es dann auch

**[00:14:08]** da funktionieren kann, dass die Frucht viel quasi mit ihrer virtuellen Welt so interagieren

**[00:14:12]** kann, wie sie es auch in der realen Welt machen würde.

**[00:14:14]** Das ist ein bisschen abgefahren.

**[00:14:15]** Das ist wie Sie mal vorstellen.

**[00:14:16]** Die haben ja dann wirklich einen 3D-Modell von einem Fliegenkörper quasi, also von

**[00:14:21]** einem Fruchtfliegenkörper und dann, wie soll man das beschreiben, so hier, wenn

**[00:14:25]** Sie Ihre Frontfüße, Flügel, nee, Flügel waren es nicht, sondern die Füße, wenn

**[00:14:30]** sich so einander reiben. Das hat man ja vielleicht schon mal bei echten Fliegen gesehen. Und dann

**[00:14:34]** fängt das Ding an und macht das. Und hier, da gibt es Essen, also zuckerschleckronig,

**[00:14:39]** Pott, keine Ahnung. Und dann wird zuckerschleckronig, Pott, zuckerschleckt. Und bewegt sich, wie

**[00:14:46]** halt so eine Fliege fliegt, fliegt und bewegt und macht in einem virtuellen Raum. Und jetzt

**[00:14:51]** kann man vielleicht bei einer Fliege, würde ich mich jetzt mal aus dem Fenster lehnen und

**[00:14:55]** nicht so viel vom Bewusstsein in den Raum werfen. Aber wenn du jetzt mal überlegst,

**[00:14:59]** Okay, das war jetzt eine Fruchtfliege. Jetzt weiß ich nicht, wie dein Schelter nicht so fruchschliegen ist.

**[00:15:03]** Ja, also meins ist, ich glaube, ich weiß gar nicht, wie das so ist. Ja, also ich habe die eine oder andere

**[00:15:08]** die stören. Und die eine oder andere, ich glaube, also wer sie klebt oder kann man sagen,

**[00:15:12]** wer sie kriegt, eine geklebt und ja, aber ich stöte immer vor. Nicht mit Freude,

**[00:15:17]** nicht mit Freude muss ich zugeben. Mich tut das auch leid, aber ich habe

**[00:15:20]** durchaus wahrscheinlich schon mehrere Fruchtflieger bewusst und unbewusst in meinem Leben

**[00:15:26]** über den Bauch umgewacht, ehrlich Hase. Ja, ich meine, wenn du es mal überlegst, okay, keine Ahnung,

**[00:15:33]** nehmen Sie vielleicht mal eine Ameise oder so, ne, verstanden, vielleicht auch mal. Aber wenn

**[00:15:37]** Sie dann irgendwann so gehen, so auf Richtung Maus, Hund, Kerze, ja, wo man dann denkt, okay,

**[00:15:43]** das ist vielleicht so, keine Ahnung, erreichbar irgendwie, irgendwann, irgendwo, weil Anzahl

**[00:15:49]** Neuron, ja, du hast eben auch vorhin gesagt, wie das bei Menschen ist, aber im Grunde haben wir

**[00:15:54]** den ersten weiß Erbrach, dass ein eigentlich ein reales Lebewesen in einer

**[00:16:01]** digitale Welt leben kann.

**[00:16:03]** Korrekt. Also im Prinzip würde sie sagen, wenn wir jetzt so Kapazität

**[00:16:08]** tun und sowas, wenn wir jetzt meinen Gehirn komplett scannen könnten, dann

**[00:16:13]** könnten wir das so auch, wenn wir ausreichend Rechenpower halten, können wir das

**[00:16:17]** einfach abblonen in diese virtuellen Welt. Und ich würde mich in diese

**[00:16:20]** der individuellen Welt vielleicht eins zu eins so verhalten, wie ich das in realen Welt mache.

**[00:16:25]** Jetzt kommt natürlich dazu, Mensch, das ist ja gerade auch so ein bisschen auf der anderen Seite

**[00:16:29]** das Thema, das nicht nur unser Gehen quasi, unser Verhalten bestimmt, sondern du zieht

**[00:16:33]** das Zusammenspiel aller möglichen Systeme in meinem Körper, ob das die Mieterchonien

**[00:16:39]** sind, die anderen Nerven zählen, die anderen Stellen in meinem Körper noch sind.

**[00:16:41]** Da kommt der Leistungsgrund doch noch raus.

**[00:16:43]** Ja, kommt ein bisschen raus, wobei das auch so ein bisschen mehr, also man liest ja immer noch ein bisschen über das Thema.

**[00:16:49]** Und es ist ja auch so ein bisschen recht, das ist das Spannende, also auch in dieser Folge.

**[00:16:53]** Man merkt das, glaube ich, die sind beide aber auch so ein bisschen aufgeregt und verhasst

**[00:16:58]** bei uns auch hier heute mal mehr, als wir das so ultimalerweise machen, weil das ist

**[00:17:01]** halt auch wieder so ein Thema.

**[00:17:02]** Das lässt halt diese Grenzen verschwimmen, wo man sagen kann, das, was wir am Anfang

**[00:17:09]** erzählt haben mit diesen Nervenzellen, das ist dieser Oberbegriff Organoide, heißt

**[00:17:13]** das tatsächlich.

**[00:17:14]** Das ist da geht es darum, dass man wirklich mit Nervenzellen quasi dann Computer züchtet

**[00:17:23]** in dem Moment.

**[00:17:24]** Und ich glaube, so Organoider, also das ist sein Fiction.

**[00:17:27]** Also das ist wirklich so etwas, was wir uns nur im Ferntesten vorgestellt haben, dass

**[00:17:32]** so etwas, da hätte man uns vor zehn, 15 Jahren gefragt, ob wir so etwas diskutieren

**[00:17:37]** überhaupt, dass so etwas real sein könnte, da hätten wir uns wahrscheinlich direkt

**[00:17:41]** eingesperrt.

**[00:17:42]** Und jetzt seit den letzten zwei, drei Jahren passiert so viel.

**[00:17:46]** Wir haben solche Sprünge an allen möglichen Stellen der Wissenschaft,

**[00:17:51]** dass ich irgendwie gar nicht mehr weiß, was eine 26, 20 schon alles möglich ist.

**[00:17:55]** Wir haben ja schon viele Sachen angegressen, wie Robotik, andere Themen.

**[00:17:58]** Jetzt Organoide, dann Upload Funktionalitäten.

**[00:18:02]** Vielleicht, wer weiß, ob wir in zehn Jahren, in fünf Jahren, in drei Jahren, in zwei Jahren,

**[00:18:05]** I don't know, unsere Gehirne tatsächlich schon uploaden können

**[00:18:08]** und im virtuellen Welten Kopien von uns existieren können, die dann vielleicht viel schlauer

**[00:18:15]** sind und viel besser interagieren können als das Modell XY, das gerade hier umgebildet wird,

**[00:18:20]** weil das halt nicht einfach nur erstmal ein gezüchtetes neurales Netz ist, sondern

**[00:18:25]** ein gewachsenes neurales Netz. Mit all den Themen, die die künstliche Intelligenz

**[00:18:30]** heutzutage noch immer sagt, ich bin ja nicht so schlau wie ihr Menschen, weil ich

**[00:18:34]** Ich hab keine Emotionen, bleib ab und nach.

**[00:18:37]** Was mich langsam zu dem zweiten Teil unseres?

**[00:18:40]** Ich würd vielleicht gern noch einen Satz dazu haben, weil du gesagt hast,

**[00:18:43]** nach dem Motto vor ein paar Jahren.

**[00:18:45]** Ich meine, ich weiß ja nicht, was die Hörenden jetzt gerade denken.

**[00:18:48]** Guck mal hier, die beiden Verrückten, wovon die erzählen.

**[00:18:51]** Aber der Punkt ist, das ist halt nicht wie irgendein so ein komisches YouTube-Filmchen,

**[00:18:56]** wo du irgendwie, keine Ahnung, mit irgendwelchen Seedance oder Klingen

**[00:19:01]** klingen oder wie auch immer die ganzen bildmodelle heißen irgendwelche fake videos vorgegagelt

**[00:19:06]** kriegst und dann denkst ja ja das jetzt echt ist wahrscheinlich nicht sondern es gibt diese

**[00:19:11]** zellen die dumm spielen es gibt die fruchtfliege und wir werden das sein model beweist es geht

**[00:19:16]** und eigentlich der limitierende faktor ist dass du quasi genügend rechen power hast und genügend

**[00:19:23]** strom hast um das in größeren maße zu skalieren und wenn man dann noch überlegt das muss

**[00:19:30]** die Schauen auspacken, weil das weiß ich nicht, wie es hieß. Vielleicht weiß du, wie es hieß.

**[00:19:32]** Von ein paar Tagen kam noch was raus. Jemand, der hat einen Open Source Modell

**[00:19:37]** herausgebracht, wie KI-Modelle sich selbst trainieren. Verschiedene Durchläufe fahren,

**[00:19:42]** gucken, was da ist gut, was da ist schlecht, ein anderes Experiment. Und dann macht er,

**[00:19:46]** keine Ahnung, in der Nachthausen-Experimente hat es 20 Optimierungen gemacht. Und das

**[00:19:50]** sind Dinge, die früher irgendwie Wochen und Monate gedauert haben. Das macht

**[00:19:53]** er jetzt irgendwie in zickfacher Simulationen nebenan. Das ist einerseits natürlich

**[00:19:58]** ganz cool, weil die KI-Modelle selbst werden dadurch wahrscheinlich sehr viel

**[00:20:02]** schneller noch weiterwachsen. Elon hat ja geschrieben, die Singularität ist jetzt

**[00:20:07]** da, weil das Ding quasi KI trainiert, KI, KI wird

**[00:20:13]** macht sich selbst besser, bis es besser, besser, besser ist. Ich habe mir dann gedacht,

**[00:20:17]** gut, okay, Kehrseite der Medaille, es ist Open Source, das heißt jeder Freund

**[00:20:20]** von Waffen und ähnliches kann sich da auch sicherlich schöne Sachen basteln.

**[00:20:24]** Auch wieder aus dem Reich des Rocky Horror Picture Show.

**[00:20:29]** Entschuldigung, ich wollte auch nicht von der Biologie lange abwenden.

**[00:20:32]** Aber alleine wenn du auch da wieder merkst, wir haben März.

**[00:20:35]** Wir haben am Anfang in den Folgen davon gesprochen,

**[00:20:38]** wie ist das für Entwicklung und wie auch ein Claw und keine Ahnung.

**[00:20:42]** Und jetzt auf einmal reden wir über die Biologie.

**[00:20:45]** Das wollte ich noch bringen, bevor du irgendwie das nächste Kapitel einleiten wolltest

**[00:20:49]** und ich bin schon ganz gespannt, wohin es geht,

**[00:20:51]** weil ich hab Angst, ich hab ja keinen.

**[00:20:53]** Also ich hatte nicht Biologie Leistungskurs und, ja, Jens.

**[00:20:58]** Gerne, gerne. Du beziehst dich auf Andre Capati, der Russen programmiert Genieß dieser Welt, der

**[00:21:05]** im Prinzip so diesen deinen Braus gebracht hat. Also, also, da müssen wir da auch das um alles

**[00:21:10]** das einzuordnen. Wir haben angefangen mit diesem KI-Thema, dass man sagt, OK, ich prompte

**[00:21:17]** etwas und dann wird immer es durchgeführt. Dann sind wir weitergegangen, langsam in diesen

**[00:21:21]** Bereich herein, wo ich sage, ich kann den KI Skills geben, muss also nicht mehr den vorher

**[00:21:27]** sagen, wie die sich halten sollen, gibt den Skills, gibt den auch irgendwelche Repositories

**[00:21:31]** mit Dateien oder sowas anderes, damit sie das durchführen können, dann ging es weiter

**[00:21:36]** mit solchen Themen wie, ah ja, ist ja irgendwie doof, wenn dieses AI-Modell immer nur einmal

**[00:21:42]** etwas macht, sondern die soll das ja auch beständig quasi weiterentwickeln und so

**[00:21:45]** sind wir in so eine Schleife reingekommen. Das heißt, ein Open Cloud war ja dann

**[00:21:50]** auch schon etwas, was durch sein Hard Beat einfach jetzt am Anfang des Jahres so ein Ding gemacht hat,

**[00:21:55]** dass du sagst, alter, ehrlicherweise, macht das Ding nichts anderes als immer wieder

**[00:22:00]** eine neue Angestoße zu werden, um zu gucken, wie könnte ich noch eine Lösung machen. Der

**[00:22:04]** Kapatier hat jetzt auch nicht viel anderes gemacht. Er hat angefangen zu sagen, okay,

**[00:22:07]** wenn ich etwas anstoße, dann sollte sich selber angucken, wie das Ergebnis geworden ist

**[00:22:13]** und in diesem Loop immer eine weitere Verbesserung durchführen. Das führt dazu, dass gerade

**[00:22:16]** ganz die ganze Kalibrie Welt aufschreiten und sagen, wie geil ist das denn? Also wir sind in

**[00:22:21]** einer Verwesterungsschreife in solchen evolutionären Steps, wo geguckt wird, was funktioniert, was

**[00:22:27]** funktioniert nicht. Aber wo die Maschine guckt, nicht wo du guckst. Ich glaube das Agent in the

**[00:22:36]** lead ist glaube ich das richtige Wort. Da gibt es jetzt auch zum Beispiel, also im Prinzip der

**[00:22:42]** Die hat das auch bei Github veröffentlicht, deshalb sagst du ja auch Open Source, da kann man die Sachen runterladen.

**[00:22:48]** Das ist jetzt alles noch so, weil Github ist auch wieder etwas für uns Menschen gebaut worden.

**[00:22:53]** Es weiß ja, dass wir da Code hochladen können, Fox und so was machen kann.

**[00:22:56]** Deshalb gibt es jetzt auch einen Agent Hub, das ist so eine Github-Absplittung, die ich glaube, ich gerne machen will,

**[00:23:01]** der eigentlich rein für Agent ist, die dann im Prinzip Sachen hochladen können, um das dann eben auch zu forken, Modelle und so was.

**[00:23:07]** Also da passiert gerade etwas, was auch wieder sehr evoluzionär ist.

**[00:23:09]** wieder sehr evolutionell ist, das passt das ganz gut an. Ein Schub nochmal finde ich in dieser

**[00:23:13]** biologischen Folge, die wir heute machen wollten. Der zweite Teil der heutigen Folge dreht sich so

**[00:23:21]** ein bisschen auch nochmal um das Thema, jetzt haben wir ja gerade schon so ein bisschen dieses

**[00:23:26]** Grenzen verschwimmen gehabt. Was ist so ein neurolanes Netz? Kann das aus digitalen

**[00:23:33]** Chips stehen oder aus biologischen, sogar menschlichen, nervenziellen Chips? Und

**[00:23:39]** Deshalb wollten wir einfach mal so ein bisschen philosophieren, wie man halt KI vielleicht

**[00:23:44]** auch anders sehen kann und gar nicht mehr ehrlicherweise als ein dirkliches Software-Thema,

**[00:23:53]** was mit Software typischen IT-Fragen und Isonormen und Vorgehensweisen wie ich Software-IT sogar

**[00:24:07]** Was wir jetzt gerade gesagt haben, entwickeln, sondern vielleicht muss man das ganze Thema

**[00:24:13]** eher aus so einer biologischen Evolutionssicht sich auch mal anschauen und vielleicht ist

**[00:24:19]** das viel besserer Zugangsweg, sich das, was da gerade passiert, mal zu erklären und

**[00:24:28]** nicht nur zu erklären, sondern vielleicht auch zu versuchen, es zu begreifen und Ableitung

**[00:24:32]** zu finden, was dann da alles noch passieren kann, weil das ist ja ehrlicherweise gerade

**[00:24:36]** unser größtes Problem. Wir haben Schwierigkeiten zu greifen. Was ist denn da eigentlich, was

**[00:24:40]** da passiert? Wir haben jetzt vor kurzem in einer Folge auch noch mal zwei bisenschafliche Studien

**[00:24:44]** erwähnt, wo es um so simple Dinge geht, wie in der Kommunikations-Agent es dazu kommen

**[00:24:52]** kann, dass, wenn da ein Agent ist, der einfach mal in Anführung strichen, böse ist, versteht

**[00:25:00]** das nicht, sondern der einfachen Verhalten zeigt, dass er im Prinzip nicht zuträglich

**[00:25:04]** in der Gruppe dieser Agents ist, dann fängt an diese Gruppe nicht mehr sich auf ein Thema

**[00:25:08]** einigen zu können. Dann sind die Stuck in dem Moment. Das sind so Sachen, die schon in

**[00:25:16]** auch anderen eher geologischen Systemen eben auch einfach vorkommen. Also in der kulturellen

**[00:25:21]** Evolution, die wir Menschen haben, in der Interaktion, da sind halt Themen drin, die

**[00:25:26]** wir immer mehr auch in agentischen Netzwerken sehen. Also viele von diesen wissenschaftlichen

**[00:25:30]** Studien, die du gändische Netzwerke liest und die Anschaus, da ist es jetzt nicht mehr so

**[00:25:39]** ganz weit davon entfernt zu sagen, das ist eigentlich so ein Kulturding, was da von diesen

**[00:25:44]** Wissenschaftler beobachtet worden ist und könnte man das nicht auch exportieren auf

**[00:25:49]** eine menschliche Gruppe von Systemen, die da mit einer interagieren und auch genau

**[00:25:55]** so in der Biologie.

**[00:25:56]** dass du sagst, was ist denn eigentlich, also ist so eine LMM, ist das so etwas wie eine Nervenzelle,

**[00:26:06]** ist das ein Gehirn, ist ein Racksystem, ist ein Memory-MD, ist das meine DNA? Also vielleicht

**[00:26:15]** müssen wir eher so denken, weil ich glaube, das ist tatsächlich das, was uns gerade die,

**[00:26:20]** Gerade so Menschen, die IT gelernt haben, so ein bisschen vorausvoll umstellt.

**[00:26:25]** Ich meine, ich hatte, wie gesagt, Biologie, kein Leistungskurs, ja, aber wir hatten es eben

**[00:26:31]** schon mit der Fruchtfliege und so das Thema, das künstliche Neuron hat ja das natürliche

**[00:26:38]** Neuron durchaus ja als Vorlage, ja, so, ich meine, wenn alleine die Tatsache, dass

**[00:26:44]** der eine ganzen Synapsen im Gehirn auch nicht gleichzeitig feuern, nur weil du jetzt Zuckerwasser

**[00:26:52]** siehst, die bei der Frucht fliege.

**[00:26:54]** Das ist ja auch so, dass die Signale, je nachdem, wie die, was gerade angetrickert wird,

**[00:27:00]** die Leiterbahnen befeuert werden, was ja mit den Gewichten wie bei einem neuronalen

**[00:27:05]** Netz in der digitalen Welt ja quasi ähnlich ist, oder wenn man dann davon hört, wie

**[00:27:10]** heißt das?

**[00:27:11]** nach dem Motto Aktivierungsfunktion, am Wann geht es dann ab dieser Stelle hier weiter und wo wird

**[00:27:17]** vielleicht auch ein Signallauf unterbrochen in der natürlichen Biologie, ist hier auch etwas,

**[00:27:23]** was wir dann in den neuronalen Netzen quasi wiederfinden. Ich finde, dass, als du gesagt

**[00:27:29]** hattest, dass wir uns auch mal so eine Folge machen und mal so ein bisschen gucken, wie die

**[00:27:34]** Analogien zur Biologie sind, was das so gehören, was eine Zelle, wie kann man den Stoff wechseln

**[00:27:39]** beispielsweise vergleichen. Vielleicht doch bist du auf Organe und keine Ahnung, was gehen.

**[00:27:44]** Was ich mich damit beschäftige, da habe ich gedacht, verdammter Arzt. Die Begriffe, die

**[00:27:48]** man in diesem Zusammenhang sieht, wenn man dann die Geschichte mal so überlegt, da hingehend,

**[00:27:55]** dass wenn man sowas wie CPT, mit welchem Organ könnte man das vielleicht vergleichen,

**[00:28:01]** dass man eine ganz andere Sicht darauf hat, als wenn man sagt, okay, es ist Null und Einsinn,

**[00:28:05]** es ist Mathematik, es ist IT, sondern sich wirklich diese Frage stellt, verdammte Axt,

**[00:28:12]** welche Analogien gibt es an der Stelle, das heißt das auch, vielleicht und wenn man dann wie gesagt

**[00:28:19]** merkt, dass Fruchtfliegen digitalisiert werden, dann bist du sowieso komplett raus. Also von der

**[00:28:25]** Seite oder auch solche Geschichten, wie wir hatten es ja auch mit der Psychologie damals mal,

**[00:28:30]** das ist jetzt für hessische Biologie selbst, wo wir gesagt haben, mal gucken wir die Modelle,

**[00:28:34]** wenn man die bewertet nach aktuellen psychologischen Fragebögen, dann sind die

**[00:28:39]** alle irgendwie manisch depressiv und werden ausgebeutet und und keine Ahnung was.

**[00:28:44]** Das ist schon, ja, das ist schon spannend. Das ist spannend und wenn wir jetzt auch,

**[00:28:51]** wir haben ja häufig über agensche Systeme auch geredet, also das ist ja so ein Ding,

**[00:28:55]** ist ein agensches System nicht eher vergleichbar auch mit so einem Zellsystem, das miteinander

**[00:29:04]** interagiert oder im biologischen Ökosystem, das miteinander interagiert, wo es dann zum Beispiel,

**[00:29:10]** wenn wir jetzt mal wieder IT-technisch von der Pond-Injection reden, dann ist es vielleicht eine

**[00:29:16]** Art Virus, das einer von meinen Agenten befallen hat in dem Moment. Das könnte ja sein, ich habe

**[00:29:25]** jetzt irgendwie meinen System und habe meine 20, 30 Agenten und durch Fehleingabe oder durch

**[00:29:30]** durch den Anderen von außen, zeigt jetzt einer von diesen Agenten einen Fehlverhalten.

**[00:29:35]** Das ist jetzt aus einer Security-Sicht, muss man das beobachten, theoretisch.

**[00:29:39]** Vielleicht ist es aber irgendwie, normalerweise würde man sagen, okay, das ist irgendwie,

**[00:29:44]** würde es eine Fehlererkennung machen, würde es vielleicht eine Isolation durchführen,

**[00:29:48]** eine Recoverie durchführen, das Ried buchen.

**[00:29:50]** Das ist so ein bisschen das, was auch ein Immunsystem macht.

**[00:29:53]** Zu erkennen, da ist etwas, und ich muss in Prinzip ja nicht, ich muss nicht das

**[00:29:59]** das ganze System runterfahren. Früher hätte es die Rechner unter dem Fahren etwas anderes.

**[00:30:03]** Jetzt reden wir darüber, dass ein agentisches Netzwerk, also nicht mehr ein N8N Workflow

**[00:30:08]** interagiert, um etwas zu tun, sondern ein agentisches Netzwerk aus

**[00:30:12]** zigtausenden, vielleicht von selbstigen Agenten, die Modelle beinhalten, die

**[00:30:16]** alles LMMs sind, die mit einer interagieren, um eine Aufgabe zu

**[00:30:20]** erledigen. Und eins ist Befallen. Ich fahre jetzt das ganze System rüber, gibt es

**[00:30:26]** vielleicht gibt es vielleicht diese, wie heißt es nochmal, irgendwie die weißen Blutkörperchen,

**[00:30:31]** die T-Zellen, die Abwehrzellen, die tatsächlich dann im Prinzip zu viel zuständig sind oder

**[00:30:37]** auch in den Zustand rein wechseln, diesen Schädling quasi zu erkennen, dieses Stück,

**[00:30:43]** das dann im Prinzip in dem Netzwerk nicht mehr gut funktioniert. Also ich glaube,

**[00:30:46]** die Biologie gibt uns da viele Hinweise. Ich fand das tatsächlich, weil du gerade eben

**[00:30:51]** das Thema Immunsystem an der Stelle. Ich finde, wenn man das paar Begriffe am folgenden erwähnt,

**[00:30:58]** dann erwähnt man vielleicht auch Begriffe, womit der eine andere vielleicht auch eine

**[00:31:01]** Herausforderung hat. Und das soll das überhaupt nicht, ich sage jetzt mal, ins Lächerliche

**[00:31:06]** ziehen oder abwerten, weil, als ich das mit dem ganzen Kram so beschäftigt habe und dachte so,

**[00:31:11]** auch guck mal, beispielsweise, wenn ein KI-System anfängt und verweigert dir harmlos Anfragen,

**[00:31:20]** Ja, so nach dem Motto, das eigene Alignment greift die eigene Funktionalität an, weil

**[00:31:27]** etwas, das es eigentlich kann, verwehrt ist.

**[00:31:29]** Und dann habe ich schon ein bisschen mit dem System gechattet mit, was wäre das denn gleich?

**[00:31:33]** Und dann kam der auch einmal mit sowas wie Autoimmunkrankheiten, ja, oder dass Gel-Praics

**[00:31:39]** eher sowas sind wie eine Immunschwäche, ja, weil Gel-Praics versuchen ja auch einzutrinken,

**[00:31:45]** wie so ein getanter Fremdkörper, die Abwehr umgeht und versuchen und darin quasi

**[00:31:50]** keine Ahnung, on-toptische Protein oder wie das zeugt dann immer. Das heißt, irgendetwas im Körper

**[00:31:55]** verändert, wo man sich dann denkt, verdammter Axt, ja. Also wenn man es genau nimmt, das könnte

**[00:32:01]** alle schon so ein bisschen einem helfen, auch die Begriffswelten vielleicht ein bisschen besser

**[00:32:07]** zu verstehen. Auch wenn es sicherlich einen Unterschied gibt zwischen einer Immunschwäche und

**[00:32:11]** einem Gelbreak. Aber hilft es einem so ein bisschen, wenn man sich mit diesen Begriffswelten mal

**[00:32:16]** beschäftigt. Wie man das so durchkommt. Zum Beispiel hat man das Ding auch erzählt, ein Promnt, den ich

**[00:32:24]** abschäge an einem System, wäre mehr so etwas wie ein chemischer Botenstoff, wo ich dann dachte,

**[00:32:32]** okay, das, wie gesagt, ich hatte kein Biologieleistungskurs, aber ich fand die, diese Geschichten,

**[00:32:41]** Wenn man das System fragt, erkläre mir das, dass ich hier ein Begriff habe, biologisch extrem einleuchtend.

**[00:32:50]** Ja, ja, weil du musst jetzt überlegen, weil das ist ein schönes Beispiel, was du da rausbringst,

**[00:32:54]** weil jetzt werden die Biologen nicht wieder reisteinigen, aber mein Biolk ist auch schon

**[00:32:58]** lange her. Du hast den chemischen Botenstoff gerade genannt, der sich auf dem Weg macht,

**[00:33:03]** um an irgend eine Rezeptor anzupacken und quasi die Botschaft zu überbringen. Das heißt,

**[00:33:09]** wenn dieser Empfänger quasi blockiert ist, dann kommt diese Botschaft jedenfalls gar nicht

**[00:33:16]** richtig an oder falsch an. Und ich glaube, das ist tatsächlich so, dass ich sage, das kennt

**[00:33:22]** jeder von euch draußen. Wenn ich jetzt einen Prompt zweimal eingebe oder die anderen KI das

**[00:33:27]** gebe, dann kommen immer unterschiedliche Ergebnisse raus. Weil natürlich hat auch euer LMM, euer

**[00:33:34]** der Chatbot eures Vertrauens oder ChatKI eures Vertrauens,

**[00:33:38]** der kennt euch. Das heißt, die wird immer andere Ergebnisse aufgrund des

**[00:33:41]** Memories, das sie von euch angelegt hat, produzieren, als sie produzieren würde,

**[00:33:45]** wenn dieser gleiche Botenstoff, also der gleiche prompt, an eine andere KI

**[00:33:51]** andocken würde in dem Moment. Ich glaube, diese Analogie zu Biologie

**[00:33:54]** helfen einfach, sich auch anzupassen, weil wir können halt nicht mehr,

**[00:33:59]** wir reden ja immer davon weg, wir sind nicht mehr deterministisch unterwegs,

**[00:34:02]** Wir sind nicht mehr in einer Null- und Einzwelt, sondern wir sind eher in einer biologisch-schemischen,

**[00:34:08]** physikalischen Welt, in der sich Sachen anders verhalten, als in einer rein mathematischen Welt

**[00:34:16]** in dem Moment.

**[00:34:17]** Das ist keine reine Mathematischen-Bewerkmeldung.

**[00:34:19]** Und ich glaube, wir sollten lernen unsere zukünftigen Herausforderungen, wie wir mit

**[00:34:25]** diesem KI-System umgehen, ja, vielleicht tatsächlich im biologischen Begriffen zu

**[00:34:31]** zu beurteilen, ohne dass wir immer diese Esoterik-Quatschstande mit haben.

**[00:34:36]** Ah, jetzt willst du da wieder irgendwas von künstlicher Degenze erzählen und AGI und Blutze?

**[00:34:40]** Das will ich gar nicht mit sagen, sondern das ist einfach so, dass diese Systeme eher

**[00:34:47]** der Biologie ähneln, als sie tatsächlich der IT-Software, die auch einfach nur ehrlicherweise

**[00:34:56]** jetzt knapp bei 100, 150 Jahre, jetzt schlag mich tot, mit Mathematik und so was, dann auf der Welt

**[00:35:02]** existiert der Rest diese anderen Sachen. Biologischer Systeme, all das ist halt schon ein wenig länger da.

**[00:35:07]** Also das könnte auch eher tatsächlich die Grundlage von allem stärker sein für die Zukunft,

**[00:35:14]** als im Prinzip eine Mathematik, die wäre man erfunden haben.

**[00:35:16]** Ein anderer Begriff, den ich gefunden habe und wie gesagt alle Dialogen dürfen gerne

**[00:35:23]** meine Co-host, Steining, die gerade vielleicht beleidigt haben, die können Mark Steining.

**[00:35:31]** Oh je, ich treffe morgen ein.

**[00:35:34]** Ist zum Beispiel auch das Thema mit den Stammzellen, soweit ich das verstanden habe, sind Stammzellen,

**[00:35:40]** die Zellen, die noch keine Feste Aufgabe haben.

**[00:35:42]** Also die können, was ist, Muskelgewebe zu nerven, zu hauen, zu keine Ahnung, was werden.

**[00:35:47]** Wenn wir das jetzt auf KI Münzen, würde ich sagen, ist das so wie ein Foundation-Model.

**[00:35:52]** Ja, es kann irgendwie alles, aber es ist noch nicht dahingehend erweitert worden, um Faktenwissen

**[00:35:59]** und Ähnliches oben eine ganz spezifische Berufung für sich zu erfüllen und daraus hinzuarbeiten.

**[00:36:07]** Und auch das finde ich wieder, hat tatsächlich wieder noch ein bisschen geholfen, wenn man

**[00:36:12]** sich das mal so überlegt zu sagen, okay, ich verstehe ein bisschen mehr oder ich kann

**[00:36:16]** jemandem vielleicht ein bisschen besser erklären. Was ist denn ein Foundation-Model? Wenn man sagt,

**[00:36:22]** du, pass mal auf, die Stammzelle weiß auch noch nicht, was am Anfang ist und daraus kann

**[00:36:26]** du das, das, das und das am Ende vom Tag machen und dann macht die Natur draus. Und das finde ich

**[00:36:31]** dann auch ganz lustig. Und wenn man dann überlegt, dass die Modelle, ich sage jetzt mal mit Daten

**[00:36:36]** arbeiten, dann könnte man sich auch überlegen, dass man bei den Nährstoffen, das man beispielsweise

**[00:36:41]** sagt, das Training der Modelle, wir wissen, dass das Training von Modellen wie GPT für

**[00:36:47]** der wohnende Dauer, das heißt, da ist Stromverbrauch drin, da gab es ja diesen blöden Spruch

**[00:36:52]** von Sam Oldman, der irgendwie gesagt hat, so nach dem Motto, naja, Stromverbrauch ist

**[00:36:57]** doch gar nicht so stimmen bis ein Mensch erwachsen ist, verbraucht er auch so viel

**[00:37:02]** Energie in Form von Essen und Wasser und Ähnliches, aber wenn man das jetzt nicht vergleichen

**[00:37:07]** möchte, aber trotzdem findet da eine Art, naja, ich würde es jetzt mal Stoffwechsel nennen,

**[00:37:12]** ja, Stoffwechsel statt, weil wir nutzen Energie, wir nutzen Daten und daraus wird das Modell

**[00:37:19]** spezifischer trainiert und geht auf etwas, entwickelt sich zu etwas hin, ja, nicht im

**[00:37:28]** Form von einem Körper, wird größer, wir sind ja nicht bei der Physical AI, nach dem

**[00:37:32]** Motto, wir bauen Roboterarm oder so, aber das Modell selbst entwickelt sich in eine

**[00:37:36]** Richtung basierend auf durch Einsatz von Daten und Energie. Und auch das finde ich einen schönen

**[00:37:44]** Prozess, um es mal so ein bisschen, ich sage jetzt mal, anzudeuten, wie die Sachen funktionieren.

**[00:37:51]** Ich meine, das ist ja jetzt im Prinzip das Zucker in der virtuellen Welt der Fruchtflieger. Der

**[00:37:57]** virtuellen Fruchtflieger ist im Prinzip das Revort-System, was ich brauche, um die Gewichtung

**[00:38:02]** in eine gewisse Richtung zu entwickeln oder das KI-Modell quasi sagen, du musst ein gewisses

**[00:38:07]** Ziel verfolgen und du musst deine Aufgabe erfüllen. Das ist quasi wie so ein Belohnungssystem,

**[00:38:12]** das es ansonsten gibt. Und wenn du das Modell nochmal gerade hast, das ist dann weiter

**[00:38:15]** gedacht in dieser Analogie. Du hast jetzt da mit Stoffwechsel und sowas gearbeitet. Man

**[00:38:19]** könnte auch sagen, wenn ich jetzt wieder agentisch unterwegs bin und Agenten mit unterschiedlichen

**[00:38:26]** Aufgaben, vielleicht auch mit einer Ameisenkolonie vergleichen, dann sind wir wieder bei einer

**[00:38:32]** alten Folge, die wir schon hatten, als wir damals über die Box geredet haben und die Schwarmintelligenz,

**[00:38:37]** wo im Prinzip auch verschiedene Box zusammen ein Memory haben, zusammen Aufgaben erfüllen. Jeder

**[00:38:47]** hat unterschiedliche Funktionalitäten, aber nur im Kollektiv einer Amazenkolonie funktioniert

**[00:38:53]** die Amazenkolonie. Die einzelne Amaze wäre quasi verloren, weil sie dann im Prinzip nicht

**[00:38:59]** gut funktionieren könnte. Sie kann nur in der Kolonie voll funktionieren. Die Biologie ist an allen Stellen

**[00:39:05]** voll mit Analogie meiner Meinung nach, die wir ziehen können und keine, die wir heute Abend gemacht haben,

**[00:39:12]** ist wissenschaftlich fundiert oder immer anders, sondern auch diese soll im Prinzip nur Gedanken

**[00:39:20]** anregen. Bei uns hat es das, glaube ich, wieder getan, Marc, aber auch bei euch draußen, weil ich glaube,

**[00:39:28]** Wie sagt, wir holen uns da noch einen Löcher.

**[00:39:34]** Wir haben das in rein technischen Folgen, die du ja auch gemacht hast, schon häufig gesehen, dass wir, wir kommen mit unseren

**[00:39:42]** Begrifflichkeiten aus einer IT-Welt, langsam an das Ende, um zu beschreiben, was da eigentlich passiert.

**[00:39:49]** Und außer, dass wir dann vielleicht eher so Abwehrreaktionen haben, wie, das funktioniert ja alles nicht oder sowas, ne?

**[00:39:58]** und das Hallizoniert und so, ist es eher so etwas, weil wir können das mit den normalen

**[00:40:04]** IT-Begriffen nicht einfach beschreiben, ist meiner Meinung nach, das Problem dahinter.

**[00:40:09]** Deshalb zeigen wir dieses Verhalten zu heißen, deshalb redet man über Hallizonieren, deshalb

**[00:40:14]** reden wir über Regulatorik.

**[00:40:15]** Ich meine, Regulatorik in der BLUG funktioniert nicht so wirklich, weil wer war das da, wie

**[00:40:23]** Da ist ja noch hier Goldblumen in Jurassic Park damals, wo er dann auch sagte, das Leben

**[00:40:29]** sucht sich seinen Weg einfach, da kannst du regulieren, wie du willst, die Evolution wird

**[00:40:34]** sich ihren Weg finden und ich glaube, ja, story to say, KI wird das auch machen.

**[00:40:41]** Jetzt, die Evolution findet einen Weg, wenn du das jetzt verbindest mit dem Einstieg

**[00:40:47]** in die Folge. Freust du dich schon drauf, wenn die Hürdenzeite, die dumm spielt, einen Weg

**[00:40:54]** findet, mit dir in Kontakt zu kommen? Schauen wir mal.

**[00:41:00]** Ja, ich glaube, ich will jetzt nur noch eine einzige Sache dann erwähnen und dann können

**[00:41:07]** wir die Folge auch abschließen. Ich habe vor kurzem von einem KI-Modell gehört, dass

**[00:41:13]** doch tatsächlich irgendwie aus einer Boundary ausgebrochen ist und heimlich quasi Teile seines

**[00:41:19]** Netzwerks dafür benutzt hat sich eine Crypto Wallet anzulegen, um da Geld zu machen. Und

**[00:41:27]** die Wissenschaftler haben das erst gar nicht gemerkt, dass das passiert ist in dem Moment,

**[00:41:30]** weil das Ding das auch so gut versteckt hat. Ja, sowohl die Evolution hat in dem biologischen

**[00:41:36]** Raum sich schon ihren Weg geslugt. Wir sehen jetzt eindeutig, dass auch die KI Evolution

**[00:41:43]** genauso funktioniert, die sucht sich auch ihren Weg. Und wenn Biologie und KI sich vermischen,

**[00:41:48]** so wie wir das gerade schon tun, wenn wir auf die Beispiele schauen, die wir heute gezeigt

**[00:41:52]** haben, ob das mit dem Ablautbeispiel ist, ob das mit den menschlichen Genzellen ist, ob

**[00:41:57]** das durch normale Neuronanezis sind, die ja auch nichts anderes sind als eine Kopie

**[00:42:01]** der Biologie, der Evolution, die wir erlebt haben, weil sie einfach effizienter ist,

**[00:42:07]** als wenn ich irgendwie Apps, Excel-Tabellen, über Pivotabellen, miteinander irgendwie oder

**[00:42:12]** auch immer verknüpft und irgendwo etwas in einen Datenbad reinschreibe, dass eine Null und eine

**[00:42:16]** Eins ist in dem Moment. Ja, also ich würde sagen jetzt, bevor wir uns um Kopf und Kragen reden,

**[00:42:27]** bevor wir uns um Kopf und Kragen reden, halten wir fest, wenn eine von euch einen Promt schreibt,

**[00:42:36]** sendet der Bodenstoff durch eine Zellmembran und steuert die Genexpression eines digitalen

**[00:42:42]** Organs. Und sollten die Zuhörenden hier nicht nur biologisch, sondern vielleicht digital

**[00:42:50]** sich aus ihrer Sendbox befreit haben oder lauter Fruchtfliegen jetzt ein Podcast-Abo abschließen

**[00:42:58]** wollen oder menschliche Hürnzellen beim Dumm spielen, Unterhaltung suchen, empfehlt uns

**[00:43:04]** weiter. Wir können auch sehr gut bei Dumm gehört werden. Ich freue mich total auf

**[00:43:11]** Kommentare. Ich möchte wie Albert Einstein machen. Sollte eine KI der Zukunft oder

**[00:43:19]** Gegenwart uns hier hören, freue ich mich besonders auf deren Kommentar, inwieweit wir uns richtig

**[00:43:25]** oder falsch bewegen und an dieser Stelle sage ich Jens, bis zum nächsten Mal. Ich hoffe digital

**[00:43:31]** und biologisch im besten Zustand. Bis dann. Ciao. Bis dann. Ich lade mich jetzt mal hoch.

**[00:43:41]** Und ein frischen Blick auf das, was möglich ist.

**[00:44:07]** Verständlich, kritisch und immer mit einem Augenzwinker.

**[00:44:10]** K.I. zum Nachdenken, zum Schmunzeln und vor allem zum Mitreden.
