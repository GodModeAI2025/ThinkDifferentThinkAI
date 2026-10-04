---
title: "KI Effizienz"
episode_index: 59
published: "Sun, 04 Oct 2026 15:59:00 +0000"
duration: "5548"
page_url: "https://think-ai.podigee.io/59-ki-effizienz"
image_url: "https://images.podigee-cdn.net/0x,sAE8UK6g-Ieww4BUW8NLmSowb8AaF32C0DPb_7WKVQlY=/https://main.podigee-cdn.net/uploads/u73317/3ac9af23-95e3-4669-97c5-0d2f8ba90198.jpeg"
audio_url: "https://audio.podigee-cdn.net/2590361-m-9005b692330eccc7e48645ce9f421eba.mp3?source=feed"
guid: "f425080832d1ca9359570fa1d2a0d410"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-10-04T18:12:49+00:00"
translated_from_language: "de"
translation_provider: "claude"
translation_model: "claude-opus-5"
translated_from_file: "transkripte/059 - KI Effizienz.md"
translated_at: "2026-10-04T20:08:37Z"
---

# KI Effizienz

**Published:** Sun, 04 Oct 2026 15:59:00 +0000
**Duration:** 5548
**Web player:** https://think-ai.podigee.io/59-ki-effizienz
**Cover:** https://images.podigee-cdn.net/0x,sAE8UK6g-Ieww4BUW8NLmSowb8AaF32C0DPb_7WKVQlY=/https://main.podigee-cdn.net/uploads/u73317/3ac9af23-95e3-4669-97c5-0d2f8ba90198.jpeg
**Audio:** https://audio.podigee-cdn.net/2590361-m-9005b692330eccc7e48645ce9f421eba.mp3?source=feed

## Beschreibung

Was KI-Effizienz wirklich kostet: Abnahmekriterien, Gegenkennzahlen und warum die Zeit zwischen den Arbeitsschritten entscheidet
Firmen werfen 80 Prozent ihrer Leute raus, weil das jetzt die KI macht. Diese Meldung geht seit Monaten durch die Presse, und Alexander Heusingfeld möchte nachrechnen. Wer 80 Prozent entlässt, behauptet damit den Faktor fünf. Klarna hat den Schritt für den Kundenkontakt inzwischen wieder zurückgenommen. Und selbst wenn die Rechnung aufginge, bleibt Alex' eigentliche Frage offen: Woher will jemand vorher wissen, welche 20 Prozent das Skillset haben, der Maschine beizubringen, was am Ende herauskommen soll? Wer selbst noch nicht ausprobiert hat, was möglich ist, kann das nicht beurteilen.

Mark dreht die Frage um. Statt „wen brauchen wir nicht mehr" interessiert ihn, was bisher liegen geblieben ist, weil nie jemand Zeit dafür hatte. Beide landen bei derselben Beobachtung: Regulatorik wie NIS-2 bleibt liegen, weil die Kapazität fehlt, teilweise sogar bei Behörden. Über jedes Stück stupide Arbeit, das eine Maschine übernimmt, kann man sich also erst einmal freuen. Die freigeräumte Zeit ist ein Invest, kein Einsparposten.

Dann erzählt Mark, was an einem Wochenende passiert ist, an dem er eigentlich Schränke aufgebaut hat. Auf einem Mac Mini hinter dem Fernseher, ohne Skills, mit nichts als Zugriff auf seine alten Git-Projekte, hat ein Agent sich das Smart Home angesehen und vorgeschlagen, die Lautsprecher im ganzen Haus als Interface zu nehmen. Danach lief die Arbeit über Sprache, während Mark durchs Haus ging. Der Agent hat ein Jahre altes Projekt fertiggestellt, sich Xcode geholt, Bundle Identifier und Signierungszertifikate selbst gebaut und die App am Ende über TestFlight aufs Telefon geliefert. Mark musste nur ein paar Kennwörter eintippen. War das effizient? Er sagt selbst: mehrere Wochenlimits verbrannt, garantiert nicht. War es das wert? Absolut.

Alex hält dagegen und stellt die zwei Fragen, um die es in der Folge geht. Was war der Harness, und welche Rahmenbedingungen hast du mitgegeben? Er selbst hat sich mit einem Agenten über AWS die Steuererklärung vorbereiten lassen: knapp 800 Belege, das Ziel „mindestens 80 Prozent einsortiert und formal richtig", vier Stunden Rechenzeit, 60 Euro. Zurück kam auch der Hinweis, wo der Steuerberater im Vorjahr etwas anders hätte abrechnen können. Aus dieser Erfahrung wird eine Metrik, die er für die brauchbarste hält: Verifikationsaufwand pro ausgelieferter Änderung. Sinkt sie, waren die Abnahmekriterien besser.

Daraus werden drei Regeln. Nie eine einzelne Kennzahl, weil jede einzelne Zahl gegamed wird, sondern immer ein Faktor aus Kriterien und Rahmenbedingungen. Immer Gegenkennzahlen mitlaufen lassen, Change Fail Rate, das älteste Work in Progress, Developer Experience. Und niemals selbstberichtete Geschwindigkeit: Entwickler geben 25 Prozent Beschleunigung an, gemessen wurden bis zu 20 Prozent Verlangsamung, weil die Zeit in Reviews und Nachbesserungen zurückfließt.

Mark ergänzt die Kette drumherum. Wenn einer drei Tage durchlaufen lässt, steht das Team vor einem Pull Request, der aussieht wie ein gefluteter Landstrich, das Backlog ist am dritten Tag eines Zweiwochensprints leer, und die Tester werden überrannt. Codekommentare, früher Pflicht, führen Agenten heute in die Irre, weil sie den Kommentar lesen statt der Routine. Und wer Generierung durch Agenten reviewen lässt, die wieder von Agenten kommentiert werden, verbrennt Tokens für das Gegenteil von Effizienz. Alex bringt dazu eine Untersuchung aus dem Flugzeugbau mit: 8,5 Prozent der Durchlaufzeit sind wertschöpfend, grob zwei Wochen Wartezeit pro Tag Arbeit. Die Antwort auf „effizienter werden durch KI" ist damit keine Werkzeugeinführung, sondern Flow und Governance. Oder in Alex' Bild: Erst klärt man, ob man Fußball spielt, danach wird das Spiel schnell.

Zum Schluss lösen die beiden die Diktiergerät-Geschichte aus der letzten Folge auf, Mark verrät sein Setup, und Alex fasst zusammen. Wer KI nur als Werkzeug kauft, verkürzt einen Arbeitsschritt. Die Effizienz liegt in den Wartezeiten dazwischen. Das richtige Maß an Qualität entscheidet sich gegen die Anforderung, alles andere ist Informatiker-Romantik. Und Marks Zugabe für alle, die zögern: Wer nicht weiß, dass er scheitern könnte, probiert es gar nicht erst.

—
Think Different. Think AI. mit Mark Zimmermann und Jens Scharnetzki.

Hören: Apple, Spotify, YouTube, RSS
https://think-ai.podigee.io

Neue Folge zuerst im WhatsApp-Kanal
https://whatsapp.com/channel/0029VbDJ4ZlGufIrpquad004

Wenn euch die Folge was gebracht hat: einmal bei Apple bewerten. Das entscheidet, ob jemand Neues uns findet.
https://podcasts.apple.com/de/podcast/think-different-think-ai/id1828021699

Feedback und Gäste: über die Show-Seite.

## Transcript

**[00:00:00]** Welcome to Think Different. Think AI., the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who do not just talk about artificial intelligence, they live it.

**[00:00:14]** Here you get clear perspectives, real practical insights and a fresh look at what is possible.

**[00:00:20]** Understandable, critical and always with a wink.

**[00:00:24]** AI to think about, to smile about and above all to join in on.

**[00:00:29]** A warm welcome to Think Different. Think AI.

**[00:00:36]** We now have, I would almost say, something like a regular player here on

**[00:00:41]** our podcast.

**[00:00:42]** Yes, Alex is with us again today.

**[00:00:44]** I got quite a lot of good feedback on our last episode, which, as

**[00:00:49]** you will remember, turned out a little longer.

**[00:00:51]** I am very curious how efficiently we will keep things today, and efficient is also

**[00:00:55]** the magic word.

**[00:00:56]** I made it particularly efficient for myself, because I had Alex write up the thread

**[00:01:01]** for today's podcast, which means it was delegated right away,

**[00:01:05]** which is wonderful.

**[00:01:07]** Alex, good to have you here.

**[00:01:10]** So what is the title of our episode, co-host?

**[00:01:12]** Yes, thank you for having me again.

**[00:01:18]** It is very interesting that you got positive feedback.

**[00:01:21]** I have been told it was entertaining.

**[00:01:24]** Well, my friend, whatever that means, better than being so dry that people switch off.

**[00:01:31]** Yes, although, I have to say, listening back I did think, oh, we really had a lot of

**[00:01:37]** terms in there that went quite deep into the technical side, but well, I think

**[00:01:43]** that probably will not, or so I assume, hope and believe, happen to us today.

**[00:01:48]** It is about becoming more efficient through AI.

**[00:01:50]** Exactly.

**[00:01:51]** Yes, very good.

**[00:01:52]** And I thought, well, the topic is really on my mind, and since I know that you

**[00:01:59]** have given it some thought too, and I know a few concrete examples from you,

**[00:02:05]** I thought, go on, prepare it, because that is the done thing when you

**[00:02:10]** bring a topic along as a guest.

**[00:02:12]** Yes, exactly.

**[00:02:13]** Yes, just like that, that is the secret of this podcast, you see, we basically have

**[00:02:17]** no idea at all, and we are always glad about every guest who takes a bit of the

**[00:02:21]** hosting off our hands so we are not just sitting there. Greetings go out to Jens. As you may have

**[00:02:26]** noticed, Jens is not with us again today. He will be back, he will be back, he will be back.

**[00:02:30]** I am glad you are here today. When I opened the script, I found

**[00:02:35]** a few great ones in there. How shall I put it, hooks? Let me say, a few

**[00:02:42]** hooks caught my eye. Stories along the lines of, you might have

**[00:02:48]** 80 percent. Let us see what we make of those 80 percent later. Yes, the word

**[00:02:55]** efficiency comfort, the ever-present flow comfort, numbers, events, loops. I am curious

**[00:03:00]** how epic a breadth we will treat the topics with, and whether we will not also deliver

**[00:03:04]** some practical value for our listeners along the way. But let us

**[00:03:10]** start with the 80 percent. What really annoys me is when people simply do not take the time

**[00:03:23]** to engage with a complex topic and its influencing factors. And so you constantly hear

**[00:03:30]** these striking claims in the press, like companies throwing out 80 percent of their staff

**[00:03:36]** because they can now do it with AI. And there is not just one company

**[00:03:41]** making that claim. We know about Klarna, who are now backtracking, because they

**[00:03:46]** have realised, well, maybe the things we wanted AI to handle, things like

**[00:03:51]** contact with the customer, maybe that was not such a good idea after all, we shall see. But in the end,

**[00:03:57]** if I throw out 80 percent of my people, that means AI makes me five times as

**[00:04:06]** efficient.

**[00:04:07]** Which is to say, achieving the same with 20 percent of the people.

**[00:04:10]** There are two things in that.

**[00:04:14]** Sorry for being so unrestrained, I cannot keep myself in check, which keeps me

**[00:04:17]** from, well, it stops me cutting in on you, but you are a grown-up, you can

**[00:04:20]** tell me off now.

**[00:04:21]** I think there are several things in there.

**[00:04:23]** One is this propaganda along the lines of, we are all going to lose our jobs and 80 percent

**[00:04:29]** get thrown out because we do not need them anyway.

**[00:04:31]** If we extrapolate that, yes, maybe someone says 60 percent or 50 percent, I would

**[00:04:34]** not insist on the exact figure, but rather on this propaganda aspect,

**[00:04:39]** because it, let me say, perhaps also through the odd misdirection in the

**[00:04:43]** political sphere, gives people a simple answer to complexity, namely

**[00:04:47]** along the lines of, with AI you have to do this, otherwise you do not belong at all.

**[00:04:51]** And if you deploy AI, then you can do it.

**[00:04:53]** You only have to deploy AI, everything is great, right?

**[00:04:55]** If you do not do it, it is your own fault.

**[00:04:57]** When I sometimes listen to those influencers

**[00:04:59]** who flutter back and forth on their YouTube channels,

**[00:05:02]** fluttering, advertising, fluttering, what kind of word is that?

**[00:05:05]** If it is new, please register it, as the inventor.

**[00:05:08]** Yes, that is the follow-up to bullshit.

**[00:05:11]** At some point it turns into flannel and...

**[00:05:14]** Anyway, never mind, I will carry on.

**[00:05:16]** Okay, thank you. You are almost throwing me off,

**[00:05:18]** but I hope I am still roughly on track.

**[00:05:20]** That is one thing, and the second is what I always find so interesting, if you now say, okay, even if it were the case that you say, I will cut 80 percent.

**[00:05:31]** Those 20 percent, they will rock it, with the AI or however.

**[00:05:35]** Then that is always measured against the status quo.

**[00:05:38]** They say, along the lines of, those 20 percent can do what the 80, what the 100 could do, because factor five.

**[00:05:43]** But this question, what am I actually capable of if you structure work differently,

**[00:05:49]** what might I be capable of doing that I never got around to before, where people

**[00:05:54]** said, honestly, if we want to do this topic, we simply do not have enough

**[00:05:58]** staff, we have to bring in an external service provider, do you have the money for that

**[00:06:02]** and so on and so forth, those are things that otherwise come up in companies now and again

**[00:06:07]** and should.

**[00:06:08]** And if you now say, okay, I can work more efficiently, in quotation marks,

**[00:06:12]** my sentence would not be get rid of the people, but rather, what could we do?

**[00:06:17]** What else is being left undone? What changes about the way we work, and not: the work

**[00:06:24]** I did a year ago is now done by AI. I notice it myself. And then

**[00:06:28]** I listen, with my verbal diarrhoea, the next word this podcast has carried,

**[00:06:31]** to the things I occupy myself with, and I could not have done them last year. For

**[00:06:40]** one thing, because the models and systems were partly unknown to me or did not yet exist, and because the way you work changes as well.

**[00:06:50]** Because you increasingly get a feel for when to deploy AI and how to deploy AI.

**[00:06:56]** What you used to learn as Let Me Google That For You, I could find something in Google and a colleague could not.

**[00:07:01]** So I sent him Let Me Google That For You as a video, so that he would go, oh right, I only had to type it in like that and it would have worked.

**[00:07:06]** That way you develop a different approach, and that is what I see as the second factor. On one side the prophets run around preaching and promise you the moon, in order to somehow

**[00:07:14]** advise companies and goodness knows what. Greetings to the McKinseys of this world.

**[00:07:19]** And the other thing is, the field of work changes as a whole, and one really ought to look at the question of what we get out of it,

**[00:07:26]** for each individual and for us as an organisation, and not just this simple back-of-the-envelope reasoning along the lines of

**[00:07:34]** Hey, cool. Double the efficiency, triple, quadruple, five times over, you just draw a line under it.

**[00:07:39]** The AI is to blame, so we have a culprit too, yes, and we can explain it as well.

**[00:07:42]** The AI is the one taking my job away, which is also great, so we have a culprit we can put in the pillory.

**[00:07:48]** It is not mismanagement or anything like that, right.

**[00:07:51]** That is the very convenient product.

**[00:07:53]** And specifically... Thank you.

**[00:07:55]** Bear with me.

**[00:07:56]** Honestly, Mark, I do not want to...

**[00:08:00]** Well, in my view you have just said exactly the right things.

**[00:08:03]** I think that is really how it is, and I do not want to disparage anyone's bar-stool chat,

**[00:08:08]** but in effect that is exactly the kind of sweeping bar-stool grumbling it is.

**[00:08:13]** There is at the moment, and I would have said this in the preparation too, simply no figure that is

**[00:08:22]** arithmetically available, no figure where you could say, here is the mathematical proof.

**[00:08:27]** Because the crux for me is, you can go ahead as the boss of a company, you

**[00:08:34]** can go ahead and say, I will throw out 80 percent of my workforce, and the 20 percent

**[00:08:40]** who are left will just have to manage somehow.

**[00:08:42]** That creates pressure, and probably those 20 percent will then be under strain.

**[00:08:48]** No, but how shall I put it? No, I, erm, let us not go there, that is a rabbit hole, we do not need to go into that right now.

**[00:08:57]** But what I am getting at is that this pressure then makes people say, damn it, the way we have worked so far, we cannot carry on like that.

**[00:09:07]** And that is exactly the mindset you actually want with AI, where you say, hold on a moment,

**[00:09:15]** we have an entirely new kind of tool here, and an entirely new way of approaching

**[00:09:25]** a problem at all.

**[00:09:26]** And that requires us to rethink our problem-solving strategies and our way of thinking, so

**[00:09:32]** not just the way we act, as it were, how do I do process optimisation, but

**[00:09:38]** to think about the topic of process optimisation itself all over again. So that is effectively

**[00:09:42]** the meta level. And now I come to my point. If I throw out 80 percent of the people,

**[00:09:51]** how do I know that the 20 percent I kept are exactly the ones with the skill set

**[00:09:58]** to teach the AI how it should produce the result the company

**[00:10:04]** is meant to have in future. So if I have not yet engaged with AI

**[00:10:08]** and have not yet tried out in practice what is possible, how do I know then

**[00:10:13]** which skills I would need in order to implement that.

**[00:10:15]** What I wanted to bring in just now, when I, erm, and I cut in on you in a rather

**[00:10:20]** unfriendly way, was when you were talking about process optimisation.

**[00:10:23]** I mean, the word skills has come up a few times here on the podcast and in our conversations as well.

**[00:10:31]** And I do think that something like skills is the second chance, for one thing because it is simply an easy way of teaching the machine things.

**[00:10:40]** I keep experiencing that when people work in chats and you then explain to them at the end how to turn that into a skill and what to watch out for in order to get better reproducibility and so on, as one thing.

**[00:10:50]** But if you get something of a handle on which skills actually exist,

**[00:10:55]** so that you do not end up with the 527th skill on the topic of requirements engineering or whatever,

**[00:11:01]** but perhaps with a handful, or counting on two fingers or one finger,

**[00:11:07]** by doing that you kill several birds with one stone, namely you manage

**[00:11:12]** to bring the AI tool closer to people, to get them engaging with AI,

**[00:11:17]** to explore the edges of their job. The other day I heard a talk asking what happens

**[00:11:22]** if the product owner now becomes a software developer too. I think I would sometimes have to look

**[00:11:25]** in the mirror on that one, because your way of working changes, because you have new possibilities at

**[00:11:31]** hand, and with skills you get the whole thing, let me put it crudely, handed to you in a more standardised,

**[00:11:36]** process-conformant and automated way, and that way you also get the issue

**[00:11:43]** off the table. Let me call it, what shall I say, water-treading. Every project

**[00:11:48]** with its own expertise, years of experience, you have to do it this way and no other.

**[00:11:52]** And yet in the next project it is done a touch differently or implemented a touch

**[00:11:56]** differently. No, by the by that counts towards the completion status,

**[00:12:00]** by the by that counts towards the completion status. No, if

**[00:12:02]** that counts towards the completion status, that you get some consistency into it,

**[00:12:06]** without going in somewhere with a crowbar and

**[00:12:10]** saying, right folks, we are now all doing training courses A, B and C so that we are all aligned on whatever

**[00:12:16]** procedures are out there, and then everyone goes back to doing their own

**[00:12:21]** little thing anyway, but instead you say, okay, good, what are the best practices, we

**[00:12:25]** put those into the AI, the AI takes care of a great many things, takes a great deal off your

**[00:12:29]** hands, this time you have to work with a backlog with the help of AI, yes, we could

**[00:12:33]** perhaps talk later about the plot and whether that helps you or not, the thing we have,

**[00:12:37]** the one I already reported on in my Tesla episode with Jens from the holiday,

**[00:12:41]** it changes the way you work so much, and in the same breath it can help you

**[00:12:45]** introduce standardisation somewhere where previously, depending on the company, you might have

**[00:12:50]** despaired. Yes, and at the same time... Maybe at this point, for both of us,

**[00:12:54]** I just want to put this out there, when we talk here, we bring

**[00:12:59]** points into it, we are in contact with a great many people, so we have small

**[00:13:02]** chat groups, we have our LinkedIn community, we allow ourselves again and again to report

**[00:13:06]** on things that we read there in part.

**[00:13:08]** So that nobody says,

**[00:13:10]** oh look, he goes around every day with a club

**[00:13:12]** saying, here, process standardisation through skills.

**[00:13:15]** Yes, so from that side I just wanted to put that

**[00:13:18]** before the audience once more.

**[00:13:19]** He does, he runs around all day with a club anyway

**[00:13:23]** and beats everyone about the head with it.

**[00:13:26]** You could say I have a bit of an image like that at the moment, right?

**[00:13:28]** With the, well, that is another topic.

**[00:13:30]** Okay. You will have to google that one.

**[00:13:32]** But I would like to come back to this once more.

**[00:13:36]** The crux of process automation for me is that we make ourselves

**[00:13:43]** aware, when we use skills, that they are precisely not deterministic. Which means,

**[00:13:49]** in particular if I say I want a deterministic quality check,

**[00:13:54]** then skills are not suited to that. And for me that is also the difference to,

**[00:14:01]** for example, robotic process automation or to a workflow engine, where I would

**[00:14:05]** say, that runs through exactly the same steps 100 percent of the time, and what you just

**[00:14:13]** said about the fields in Jira, you are not standardising because you want to drive

**[00:14:20]** free will or creativity out of people, but because you say, folks, be

**[00:14:24]** honest, does it make a difference for the end customer in the end whether we take this field or

**[00:14:30]** that field. Which is to say, put differently, which changes, which quality metrics

**[00:14:40]** change something for the customer out there, change the cost-value ratio of what I deliver

**[00:14:47]** as a service to the customer. And that is my plea. When we talk about efficiency,

**[00:14:52]** then we can talk about task speed-up and about improvements at the micro level,

**[00:14:59]** but ultimately it is the cost per business outcome, that is, the cost-value ratio.

**[00:15:06]** When you engage with the topic of efficiency and AI, then very quickly the question comes

**[00:15:14]** round the corner, so where are the figures behind it?

**[00:15:17]** And how do we pin that down in the books?

**[00:15:19]** Because we just gave the example with 20, 30, two, three, four, five times over, 80 percent

**[00:15:25]** of the workforce.

**[00:15:26]** Now you stand there and say, if we introduce AI, then it will bring us A, B and C.

**[00:15:31]** Now I do not know what our listeners' experience is.

**[00:15:36]** But when I look at my feed again, what mostly comes up is a great deal of guesswork.

**[00:15:41]** How am I supposed to quantify this efficiency that AI promises me, in a way

**[00:15:45]** that lets you actually get started with AI projects, that lets you deploy it

**[00:15:50]** and lets you do the maths somewhere so that someone says, of course you get

**[00:15:54]** X million euros for tokens, whatever, so you would have thrown some figure into the room.

**[00:15:59]** And then you notice very quickly, depending on where you are operating,

**[00:16:03]** in order to demonstrate this efficiency, quite apart from the question of

**[00:16:07]** what KPIs do they actually already have today?

**[00:16:10]** What metrics might they already have today to pin it down?

**[00:16:14]** Let me give you a tip, lines of code is not necessarily the best KPI,

**[00:16:17]** because AI will beat that one hands down.

**[00:16:22]** I think this question can largely be answered by how well you can handle AI,

**[00:16:29]** how well you can deploy it, how well it suits your particular topic. Along the lines of,

**[00:16:35]** if I set a task here, how much time do I need, how much effort do I have to put in

**[00:16:39]** until the AI completes its loop, its work, how long does it run, with which model does it run

**[00:16:46]** or does it need, how many tokens go through the ether, up the chimney,

**[00:16:50]** through Elon's gas turbine, who knows, until some result comes out, which I

**[00:16:56]** then look at again, approve or whatever, in the best case, in the worst

**[00:17:01]** case start over again, and again, and again. And without going into the whole topic of

**[00:17:06]** performance monitoring or anything like that, just saying, okay, fine, is

**[00:17:10]** this on balance a case that might be suited to AI, is this perhaps a

**[00:17:13]** topic where I should invest in Mr Zimmermann's further training,

**[00:17:17]** because he started the same loop for the eightieth time, where someone else with a loop in the same category managed it after a single loop.

**[00:17:26]** And I think that makes the matter additionally complicated.

**[00:17:29]** Where people used to say lines of code and goodness knows what else, what have you got now?

**[00:17:33]** Okay, I formulated a problem, I checked it.

**[00:17:36]** It took a certain amount of time, I kicked it off again.

**[00:17:39]** kicked it off, and between kicking off and checking half an hour passes, which is

**[00:17:44]** developer capacity, if we are talking about software development, and tokens perhaps,

**[00:17:47]** who knows, a day, a week of work in the past, that is no less

**[00:17:52]** complex to evaluate as a whole. Let us jump into concrete

**[00:17:58]** cases, because in the end the question is how do I actually measure the

**[00:18:04]** quality of the outcome, meaning, was it worth it to me? So cost value, what comes out and

**[00:18:12]** was it worth it to me? I would like to close off the part before that, about throwing out those 80 percent

**[00:18:19]** of the people. The crux for me, as I said earlier,

**[00:18:24]** is that from my point of view I cannot know in advance which people I really

**[00:18:28]** still need and which I do not. So I would be very, very careful with the

**[00:18:33]** example, Klarna shows all the customer service people the door, because yes, customer service is

**[00:18:38]** obviously going to be replaced by AI, but then again maybe not.

**[00:18:43]** And honestly, as managers we can actually be glad about every bit of capacity

**[00:18:49]** that is freed up among our staff, because from my point of view we have a certain amount of

**[00:18:55]** regulation that is not excessive but absolutely necessary, such as

**[00:19:00]** the CRA or NIS 2. And when I hear today that federal or state authorities

**[00:19:08]** are exempt from it because they simply do not have the capacity to manage it

**[00:19:14]** in time, to become CRA or NIS 2 compliant, then we can only be glad about

**[00:19:21]** every bit of mindless work, that is, repetitive work, that AI takes off our hands,

**[00:19:28]** even if it is filling in a form, where you take a photo of the handwritten

**[00:19:35]** form from Mr Müller and enter it into some system.

**[00:19:39]** And we should be aware once more of which efficiency we need where, and from my

**[00:19:46]** point of view, with what is coming at us right now, the AI models also enable attacks,

**[00:19:51]** and for that we need the creativity and the brainpower of people, so everything

**[00:19:56]** we can free up there by automating mindless things we should do, and it does not only work through AI.

**[00:20:03]** I also wanted to say thank you at this point, because you said you wanted to finish your thought, and I jumped straight in.

**[00:20:09]** That was topic one, which you had put on our list, and I had already jumped to several topics.

**[00:20:14]** So from that side, thank you.

**[00:20:15]** Perhaps at this point also a wish sent out into the ether: if work packages do fall away, because people now say,

**[00:20:23]** well, writing A, B and C, reading the forms, the AI can do that now, then

**[00:20:30]** freeing up time is also very much an investment in the opportunity to give people

**[00:20:36]** the space, and to learn how to handle this stuff as well.

**[00:20:42]** The two of us have had this discussion before, and with others as well, about the question

**[00:20:47]** of what a desirable target state actually is.

**[00:20:49]** And you have to drive in intermediate pegs in good time, because on the one hand you must not overwhelm the system, at the end of the day

**[00:20:57]** people have to come along too, so that the whole thing is adopted, works and is accepted, so that you can go on the journey, and the second thing is, you also need

**[00:21:06]** reachable goals,

**[00:21:08]** because we live in a world in which all this AI business is extremely fast-moving. We talked about it in the preparation,

**[00:21:14]** I had said something about being impressed

**[00:21:17]** by, for example, the image generation of the new Astra model from OpenAI.

**[00:21:22]** Even we, who deal with these topics, are regularly

**[00:21:26]** surprised by the possibilities that open up, because a tool or a model

**[00:21:31]** or some clever person has somehow pushed another one of those repository projects

**[00:21:34]** out in the course of a day, and we get surprised as well.

**[00:21:38]** And it is not as if we can look back on twenty years of

**[00:21:41]** Henry Ford and the like and say, yes, it stays like this, this is probably how it will

**[00:21:47]** carry on, instead it has become much, much faster-moving. And here too the rule applies,

**[00:21:52]** careful, old platitude retold, every journey begins with the first step, and we

**[00:21:58]** carry on, instead it has become much, much faster-moving. And here too the rule applies,

**[00:22:04]** careful, old platitude retold, every journey begins with the first step, and we

**[00:22:10]** should take that step again rather than running after all these apostles of 80 percent. Right,

**[00:22:16]** that was my contribution to that. What is our next point? I find the example

**[00:22:25]** rather nice, where you mentioned the Astra image generation. I have scenarios where I,

**[00:22:32]** what I said in the Personal Assistants case, where we take knowledge from Confluence,

**[00:22:38]** from the knowledge base, from our Backstage developer portal, or where privately I take notes,

**[00:22:45]** for example about my smart home, where I now have over 170 components

**[00:22:50]** and the documentation has gradually grown a bit larger, so that I create knowledge

**[00:22:51]** blocks from it with the help of skills, so that I can then ask the

**[00:22:59]** AI about it.

**[00:23:00]** And I notice that with some answers I am not in agreement with the efficiency,

**[00:23:05]** or rather not satisfied with it.

**[00:23:11]** Which means the tokens the thing consumes and the costs that arise from that,

**[00:23:14]** compared with the answer it delivers, are not acceptable to me. And on that I would

**[00:23:22]** simply like to hear from you, because I believe you have already put considerably more

**[00:23:28]** tokens through than I have. How do you handle that scenario? From my

**[00:23:32]** bubble I picked up this rule of thumb, along the lines of, well, if you have an agent

**[00:23:38]** generate pull requests, then you need at least a 70 percent acceptance rate

**[00:23:44]** where no human has to touch it any more. Otherwise the review costs are higher

**[00:23:49]** than what you put in. I thought that was an interesting rule of thumb as well. But do tell.

**[00:23:53]** That is nice. Thank you for the spontaneous question. I shall have to withdraw for half an hour

**[00:23:59]** to start on my politically correct answer. I would like to, well, we are among ourselves here. I will pin it on an example. We had, Astra came

**[00:24:03]** out, and that completely thrilled me, and I wanted to apply it to old projects.

**[00:24:04]** And now the scenario is, we talked about it in the last podcast as well, I got myself a Mac mini.

**[00:24:09]** Quick interruption, when you say you wanted to apply it, do you then simply use Codex as

**[00:24:16]** your standard harness without skills, or did you prepare something?

**[00:24:20]** I wanted to lay it out briefly, I wanted to in my build-up, thank you for

**[00:24:23]** drawing my attention to it, I certainly will not forget it.

**[00:24:25]** I started with the sentence. We have, as we already heard on the podcast, a Mac mini, and the Mac mini does

**[00:24:31]** certain things automatically on a regular basis, and that is effectively also the object of desire at home.

**[00:24:38]** I mean, I have got nothing else, I have only got that one, well, I also have a notebook and a work notebook, but this is about the Mac mini.

**[00:24:46]** And I installed Codex on it, the way OpenAI offers it to us, and yes, I have a larger Codex.

**[00:24:54]** Which means Astra was made available to me, and then I first worked with the thing and thought, okay, fine, I would like to go through a few of my projects with it.

**[00:25:03]** And you have already asked the question, did you give it skills or not? I gave it nothing at all.

**[00:25:07]** I only gave it access to my Git projects, and I simply wanted to see how Astra could help me there.

**[00:25:14]** So, there you are, the Mac mini sits behind my television, it really only has

**[00:25:20]** a remote connection, so I dial into it from another machine,

**[00:25:24]** and that is the one form of interaction I have with it.

**[00:25:27]** And I first discussed with Astra a bit how I could now use Astra really

**[00:25:32]** well, because I did not want to be constantly, when I wanted to work through these eight projects, I did not

**[00:25:36]** even know yet how that would go, how I was supposed to

**[00:25:40]** handle things with it, because I cannot spend the whole livelong day walking around the house

**[00:25:45]** with a computer in front of my nose, my son was painting his room,

**[00:25:49]** assembling cupboards and goodness knows what. And then the thing came up with a very interesting

**[00:25:55]** idea, namely it looked at my smart home and suggested

**[00:26:01]** using my Sonos speakers, so that I could effectively move around the house

**[00:26:05]** for the interaction. And I agreed to that. And the system then went ahead and,

**[00:26:10]** we have them in every room. I see. And then the thing effectively put all the speakers

**[00:26:16]** into recording mode and kept checking which speaker could hear me

**[00:26:21]** best. Which was already quite spooky in itself. In any case, we then had a

**[00:26:25]** voice interface. And then via the voice interface, and to be fair via the

**[00:26:30]** remote, so via the keyboard and remote control, it had gained access to

**[00:26:33]** my personal Git projects, and I then discussed with it

**[00:26:38]** what I would like, and told it, so you will find this repo and that

**[00:26:41]** repo, no I cannot find it, so I said, yes, it is private, it is old, go and look again,

**[00:26:47]** yes, found it, and then I talked to it about these projects, and it then

**[00:26:52]** built up its own subtasks internally, so it effectively, I talked to one chat

**[00:26:57]** and it then started other chats, which then carried out the project work. And how,

**[00:27:02]** I told it, look at all of them, make me suggestions based on what you see there, on what you believe the goal of my project is.

**[00:27:12]** Make me suggestions for reaching that goal.

**[00:27:16]** Then it set off and whirred away.

**[00:27:20]** At some point the suggestion came and it said, this project is about this topic.

**[00:27:25]** You want to release an app on iOS that deals with this topic.

**[00:27:31]** Back then it was not yet called Second Brain, the thing I was working on, evaluating all your

**[00:27:36]** screenshots that you take, because in the past, whenever I wanted to remember something,

**[00:27:41]** I took a screenshot, and I always ended up with a great many screenshots.

**[00:27:45]** And the app I wanted to build was meant to collect those, analyse them with Apple

**[00:27:48]** Intelligence and then tell me, look, there is an appointment in here,

**[00:27:52]** there is something else in there.

**[00:27:53]** So as to hand it back to me, so that when I have taken a screenshot,

**[00:27:57]** it does not get lost.

**[00:27:58]** And back then I never finished it.

**[00:27:59]** And that is one of those apps, for example.

**[00:28:01]** And it then said to me, listen, I have seen you intend to do this, blah, blah, blah.

**[00:28:04]** It told me all that, and said, to get it finished I would suggest the following.

**[00:28:08]** Then we really did discuss it while assembling the cupboard.

**[00:28:12]** Over the speaker.

**[00:28:14]** Over the speaker.

**[00:28:16]** It told me all that and I answered.

**[00:28:18]** Seriously?

**[00:28:20]** Okay.

**[00:28:21]** Yes, fine.

**[00:28:22]** Let me put it this way, the worried looks of the other inhabitants of this house.

**[00:28:25]** Exactly.

**[00:28:26]** Which means your family was keeping their lips tightly shut during that time.

**[00:28:32]** Do not breathe too loudly, lovely.

**[00:28:36]** Why is that so bad?

**[00:28:38]** That is the sandbox Klaus is always going on about, right?

**[00:28:41]** Yes, yes, of course.

**[00:28:42]** Transfer, we also do bank details via transfer.

**[00:28:45]** But why am I digressing?

**[00:28:47]** Let us stay with this example of this app.

**[00:28:49]** And then the thing was ready, and at some point, it was quite funny actually.

**[00:28:52]** Did it go quiet?

**[00:28:53]** Then nothing came back at all, so I went downstairs, connected to the device, and then

**[00:28:57]** it said weekly limit used up.

**[00:28:58]** But Codex offers you the option of saying...

**[00:29:02]** In exchange for inserting small coins?

**[00:29:04]** No, no, no, you have, right now with Astra, you see, if people

**[00:29:08]** could have Astra but do not have Astra, then for every day they

**[00:29:12]** do not have Astra, that is, are delayed, they get one chance to unlock a weekly

**[00:29:18]** limit.

**[00:29:19]** So, since I have the machine anyway, I did that with the weekly limit and then it was

**[00:29:26]** very talkative again.

**[00:29:27]** I could talk to it again.

**[00:29:28]** To cut a long story short.

**[00:29:29]** At some point I said to it, you know what, I am assembling a cupboard here, from now on

**[00:29:32]** you decide everything yourself.

**[00:29:33]** I do not want to be disturbed by you any more at all, you have everything you need,

**[00:29:36]** you cleared it with me.

**[00:29:37]** I want the finished result on my phone.

**[00:29:41]** Right, listen.

**[00:29:44]** Fine.

**[00:29:45]** I would like to know how you got onto your phone as well.

**[00:29:47]** Okay.

**[00:29:48]** I can see that now. I was going to carry on anyway.

**[00:29:51]** That sounds very efficient at any rate.

**[00:29:54]** Well, I was able to assemble the cupboard at any rate.

**[00:29:56]** Whether I still have much enthusiasm left for assembling cupboards

**[00:29:59]** is another matter.

**[00:30:00]** Which is to say, the fact that I am still talking today.

**[00:30:02]** It speaks for the fact that I did not do myself in.

**[00:30:05]** When it comes to manual work I am more of a...

**[00:30:08]** So, greetings go out to my father.

**[00:30:10]** He always helped me with arts and crafts.

**[00:30:12]** He is delighted every time

**[00:30:14]** I do not do myself in while hammering a nail into the wall.

**[00:30:17]** Right, back to the content, it built the app and then it came back with yes and furthermore, and

**[00:30:25]** it downloaded Xcode.

**[00:30:26]** But now it would need a login to my App Store account, whether I could just do that

**[00:30:31]** quickly.

**[00:30:32]** So I connected again, logged in, gave it the credentials for

**[00:30:37]** App Store Connect and for Xcode, to cut a long story short, it built the bundle identifier and signing certificates

**[00:30:45]** all by itself and then at the end put the app on TestFlight,

**[00:30:49]** internal testers, and told me, there you are. And internal testers means

**[00:30:55]** you can publish it without Apple having to run a review process,

**[00:30:58]** because internal testers is effectively yourself. I have had the Apple account since

**[00:31:03]** developer accounts have existed, at some point you could buy yourself an account for 99 or 109,

**[00:31:07]** something like that, whether you needed it or not.

**[00:31:12]** That is another question, in the past it was the way to get hold of betas and so on, but

**[00:31:17]** in this case Xcode was set up, Xcode configured, published to TestFlight, and I had it

**[00:31:23]** on my phone.

**[00:31:24]** And in between there was, yes okay, sometimes I had to go to that machine to enter passwords,

**[00:31:31]** because, idiot that I am, I had not given them to it beforehand.

**[00:31:34]** I find it interesting that it did not find a way, or did not try a way,

**[00:31:39]** to get hold of them.

**[00:31:41]** Well, on the machine, the Mac mini, it does not run with my Apple ID either, so it really is

**[00:31:48]** very, let me say, rudimentarily equipped, from that side it would have had to leave the Mac mini

**[00:31:53]** in order to cobble something together somewhere. But in terms of the day, where nothing else happens,

**[00:31:58]** rather the voice interaction enabled me to do more, for example to push this project

**[00:32:06]** far enough that it now runs on my phone and that from now on I discuss with

**[00:32:09]** it how we get a bit of performance into it and that I would

**[00:32:13]** like background refresh, along the lines of take 40 screenshots

**[00:32:17]** or 400 and work through them while the app is in the background, those kinds of

**[00:32:21]** details. By now I have also told it, better use iOS 27, because

**[00:32:26]** 26 and 27 had a slight change regarding the model

**[00:32:32]** that Apple offers us, working differently with the LLM as Apple Intelligence, and that

**[00:32:39]** was a bit, I do not know, well, in an open-plan office you will probably

**[00:32:45]** not have a thousand people talking to a thousand AI systems, and yes,

**[00:32:50]** my family is long-suffering about us trying things out, when I walk

**[00:32:54]** into the kitchen and call out to the computer, let me get up to speed on a topic,

**[00:32:59]** and then it sets off and searches and tells me something, which it also does with my son when he asks it something.

**[00:33:04]** He had a question like that, whether it would help him. I think with Fortnite it is another matter.

**[00:33:09]** Yes, but you know, I actually find that frightening on the one hand and surprising on the other,

**[00:33:16]** but at the same time also evidence that the way we work is changing.

**[00:33:22]** Right, now you asked me, how do you handle all this efficiency, what did it cost?

**[00:33:26]** I said, weekend, for those who do not know, that normally has two days, and I burned through several

**[00:33:31]** weekly limits. Is that efficient given the weekly limits? No, certainly not. Is

**[00:33:38]** it efficient that all my projects are now in a state where I say, damn

**[00:33:45]** it, not bad at all, ladies and gentlemen, that actually looks really good. I would say

**[00:33:51]** that was definitely worth it. Would I see it the same way in a professional

**[00:33:56]** work context, then I would perhaps also say,

**[00:34:00]** folks, let us approach this in a structured way with skills and the like, but for

**[00:34:04]** this experiencing and learning, and we are investing now, who knows, I push

**[00:34:09]** through a night shift. I remember when I started

**[00:34:12]** working, I was at a consultancy, and it was not at all

**[00:34:16]** unusual that you were slaving away on some documents until six in the

**[00:34:18]** morning so that the courier could take them to the

**[00:34:21]** client. And you slept two hours on the couch, went home

**[00:34:25]** afterwards. Shattered, but proud to have got the thing done. Do not

**[00:34:29]** worry. I do not expect all of you to be hanging on the AI until six in the morning. But this

**[00:34:35]** experience of, let me call it power, and the experience of your thoughts becoming

**[00:34:43]** reality, that really is impressive. Right, I often get told that I digress.

**[00:34:50]** Yes, I would have two follow-up questions on that. Namely, you just said it, well, for

**[00:34:57]** the fact that my projects are now where they are. The question is, what did you invest and

**[00:35:01]** was it worth it to you? That is in the end the same question, when I say it comes

**[00:35:07]** down to cost per business outcome. What was the outcome? So what is the value

**[00:35:13]** created there for you, and was it worth it to you? And the second question

**[00:35:17]** follows on from that. That was actually the point of my question about the harness and what

**[00:35:22]** conditions you gave it. I claim that it is not only when we are in a professional

**[00:35:27]** setting that we want to give it conditions. And these conditions

**[00:35:34]** I very often experience, and again, whether professionally or privately, that we

**[00:35:41]** get bogged down in the fine detail of conditions,

**[00:35:45]** arguing about some criteria that we still want to apply,

**[00:35:51]** where I always ask myself, and here I would like to quote our esteemed colleague

**[00:35:54]** Rodewig from Security Illusion once more.

**[00:35:58]** Exactly. Is that really a requirement?

**[00:36:01]** Does it make a difference in the end?

**[00:36:05]** Well, take your example.

**[00:36:06]** What questions were asked?

**[00:36:08]** Yes, in your example.

**[00:36:09]** It could also have said, I do not have Mark's passwords, the probability

**[00:36:16]** that he chose a weak password compared with humanity as a whole

**[00:36:22]** is relatively high, the probability that I crack it with a brute-force attack.

**[00:36:27]** Let me give that a try, but that would not have been efficient.

**[00:36:34]** No, but joking aside.

**[00:36:35]** So in hindsight, would you say you would take a blank Codex again, or would you say there are a few things that made

**[00:36:44]** a difference for me. Well, at this point I would like to, so I introduced this with the words, we talk about a great

**[00:36:52]** many stories that you hear generally, and you have now asked me specifically, I would much rather have, and this

**[00:36:57]** is not an advert at all, used our own harness, the one we build in the company, because there I do know

**[00:37:02]** quite well which guardrails it comes with out of the box, and it can do computer

**[00:37:06]** use and so on, those sorts of things, but it is simply not available to me

**[00:37:09]** on my Mac at home. Hold on. But at the same time you do not know whether it would deliver the

**[00:37:14]** same efficiency effects with Astra. Yes, that is true. That would be another question

**[00:37:18]** you would have to tease out, to what extent the model, through what they also

**[00:37:23]** pass in with their own system prompt and so on, to what extent

**[00:37:27]** that overlaps, fair point. I mean, thank you for the explanation, I had understood that much about

**[00:37:32]** harnesses already. But you are losing the listeners. Yes, we can do that in

**[00:37:38]** a separate episode. I shall invite you again, then we can talk about agent harnesses.

**[00:37:41]** Whether I would do it that way again and what I took away from it in terms of what it was worth,

**[00:37:47]** it was in fact, in hindsight, worth it on a great many different counts.

**[00:37:51]** Firstly, it confirmed to me once more that agents, when they work for us,

**[00:38:00]** that the interaction with keyboard and screen is, A, very nerdy and, B, that through the option,

**[00:38:09]** that through the spoken word, that is, through a not really precise description

**[00:38:14]** of circumstances, a programming language says if, then, else.

**[00:38:18]** When I express myself, every one of us expresses themselves differently.

**[00:38:22]** We are correspondingly binding or non-binding, and depending on how closely you look, we differ.

**[00:38:27]** Even so, the machine produces a pretty good result.

**[00:38:31]** Why do I say pretty good? Well, I thought the result it produced for me was impressive.

**[00:38:35]** I found that a real insight, particularly with a view to the fact

**[00:38:38]** that models are not going to get worse than they are today, an enormous enrichment,

**[00:38:42]** because this question, how do we interact with the machines?

**[00:38:46]** Perhaps briefly back to the plot, and I also have a reMarkable and plenty of other

**[00:38:50]** things. So how might we manage it so that the efficiency which the machine

**[00:38:54]** brings us purely technologically, in terms of possibilities, so that we as humans

**[00:38:59]** once again have the chance, with, let me say, pen, device and meeting folder, to clear our heads

**[00:39:06]** enough that we can work on a topic in peace, while the AI handles

**[00:39:11]** the handwritten notes, the voice notes, the live voice interaction, the interpretations.

**[00:39:19]** On my desk, for instance, not at the company but at home, I have a

**[00:39:25]** little Raspberry Pi camera, and whenever I put down a piece of paper, the one it

**[00:39:29]** can see, it scans it automatically and files it for me.

**[00:39:32]** It is a kind of incoming-post scanner, it does nothing else, it only does that.

**[00:39:35]** Do I want cameras to be everywhere now?

**[00:39:37]** No.

**[00:39:38]** That is not the point. What I am getting at is that before AI I could not have built such a thing myself,

**[00:39:43]** could not have made such a thing, something where I think, that is a good idea. Let us just do it. And it is precisely

**[00:39:48]** this, you discover new forms of interaction, or old forms freshly recognised, or whatever

**[00:39:54]** it was, and you have your projects, which may have been buried, in a state where you say,

**[00:40:00]** I would never have got to that state. I have, for example, a book, that is, a project with

**[00:40:05]** my mother, greetings at this point as well, about her mother, never mind why,

**[00:40:10]** about whom she wants to write a book, because she lived to be over 100 and

**[00:40:14]** experienced a great deal of German history, from the Kaiser through the Third Reich and afterwards, and simply

**[00:40:20]** how life was and the notes she kept, and what such an

**[00:40:24]** AI alone contributes in terms of historical research, gathering facts, tracing

**[00:40:31]** how historical threads developed, which in the past was something genealogical research

**[00:40:36]** and so on might have covered. You could say, okay, AI is more

**[00:40:41]** than a simple search engine, that is right, but this thing then goes ahead

**[00:40:44]** and says, well, fine, okay, I have the following facts from you, and here fits the history

**[00:40:48]** of the village and whatever else and all the rest of it. Then we add

**[00:40:52]** a bit of framing and we have a bit of a story. Yes, that alone

**[00:40:55]** enables people, whatever their age, whatever their profession, to engage

**[00:41:00]** with things they could not engage with before.

**[00:41:03]** We already said that on the AI podcast a year ago.

**[00:41:05]** And for me what comes on top now is, okay, a new model comes out,

**[00:41:08]** let us see where it goes.

**[00:41:09]** And you feel like the small child under a Christmas tree,

**[00:41:12]** with their eyes shining, unwrapping the presents and absolutely delighted

**[00:41:17]** with the wooden railway, knowing they can play with it for the next three weeks.

**[00:41:21]** And I say, I now have this voice interaction,

**[00:41:24]** I have experienced how the system, interacting through speech,

**[00:41:27]** delivers this result, that I have this result, that I have come to know this form of interaction, and my mind has been racing ever since about the question of how you get far more of that into your everyday life, what our harness at the company might learn from it, what I learn from it for my private equipment as far as interaction goes, because what you also said, a family is there, person recognition, which voice does it listen to, can you optimise that somehow, because the phrase be quiet and not now, next song, right?

**[00:41:57]** So when the daughter comes into the room and says, hey, play some music, and the thing says, eh, which series.

**[00:42:03]** This is the clever Kain, not the one that searches the internet and finds nothing.

**[00:42:08]** We are also planning that, iOS 27, right?

**[00:42:13]** There you are, there you go.

**[00:42:14]** Yes, I am in.

**[00:42:17]** Right, and from that side... That takes a bit longer.

**[00:42:19]** Yes, exactly.

**[00:42:20]** Repeat your request.

**[00:42:23]** And from that side I learned an enormous amount there.

**[00:42:27]** But of course that is also the opportunity of, you have a large subscription, which in general

**[00:42:32]** costs money already, you had the chance of resetting.

**[00:42:34]** If none of that had been in place, I would not have been able to reach that insight.

**[00:42:39]** But even if you do not have that, well, I had, I did not have a Claude

**[00:42:45]** subscription for a long time, instead I used the things via my AWS account and paid

**[00:42:50]** per token there.

**[00:42:51]** And I had the thing prepare my tax return.

**[00:42:57]** Which means I went through all the documents and said, okay, what do I want

**[00:43:01]** to achieve?

**[00:43:02]** Here are the forms, this has to be filled in, this is my tax return from

**[00:43:07]** last year, this is what the tax adviser filed.

**[00:43:09]** You have here, close to 800 receipts, pre-sort that, classify it, explain

**[00:43:17]** to me why and where you would file each item.

**[00:43:21]** And we go through the receipts in descending order, starting with the lowest probability,

**[00:43:28]** we go through the receipts. Your goal is to have filed at least 80 percent of the receipts

**[00:43:33]** and for us to be able to say the tax return is formally correct. With that I set it entry criteria,

**[00:43:40]** and it whirred away for a good three and a half, four hours, and those were largely

**[00:43:47]** photos, exactly as you say, receipts, happily photos, just dumped into the directory and done.

**[00:43:52]** And at the end, including follow-up questions and so on, that cost me 60 euros. Was it

**[00:44:00]** worth it to me? Absolutely, because that was my lifetime, which I would otherwise have had to spend

**[00:44:08]** somewhere else. Apart from that, have you ever had so much fun with a tax return, watching

**[00:44:12]** how it does it? Yes, above all I looked at the result and was astonished,

**[00:44:17]** because it also explained to me where my tax adviser had overlooked things last year

**[00:44:23]** that he could have claimed differently, and interestingly, exactly, interestingly,

**[00:44:28]** where the tax office had pointed that out to him in writing. That was very interesting, but never mind.

**[00:44:36]** Perhaps just very briefly, we just made the point

**[00:44:39]** that the AI should not afterwards say, oh, Mark, with what probability does he have

**[00:44:44]** weak passwords. About Alex it should be said that he does not live in Berlin. The AI was not

**[00:44:49]** to blame with the tax return for the rather strange things that have just happened in order

**[00:44:53]** to file the tax return. Just so that we properly pick up and

**[00:44:57]** accompany our listeners here. So that they do not think they are witnessing a digital

**[00:45:01]** crime. Very good. Yes, but those are of course experiences.

**[00:45:05]** Yes, but what I am getting at is in the end the topic, or

**[00:45:10]** in the end it is the topic of acceptance criteria, that we say, what is it worth to us, how do we

**[00:45:16]** determine that it is good enough? And you told me months ago, that was also an entry

**[00:45:24]** criterion, or that was an entry criterion for building your harness, where you said, well,

**[00:45:29]** I want to be able to specify how much it may cost at most and what the criteria are

**[00:45:33]** by which you can tell when it is done. And you already had an episode about that,

**[00:45:39]** as far as I know, exactly. Yes, because you have prompts and skills and then

**[00:45:44]** loop engineering, and loop engineering is both a curse and a blessing,

**[00:45:48]** because you do not only have to specify what goal I have, you also have to

**[00:45:51]** give me the chance, under controlled conditions, to accept failure

**[00:45:55]** as an outcome, namely also to say, I have either

**[00:46:00]** reached it at the desired quality, or I have reached a sufficient

**[00:46:04]** number or the sufficient characteristic, so that a stop is assured, so that it does not

**[00:46:12]** try to round something to the ninety-ninth decimal place and then merrily fires tokens

**[00:46:18]** into the ether all night, and the next morning you see,

**[00:46:22]** look, it is still running, how funny, that must be a really great result,

**[00:46:25]** and then you look at the code and think, okay, why did it create

**[00:46:31]** 40,000 branches for a simple addition task. It is nicely documented, but always wrong.

**[00:46:37]** Right, and that is why I say, that is perhaps where we do get a bit deeper into the topic of

**[00:46:44]** technology.

**[00:46:46]** My plea is, when we talk about quality optimisation at the small scale, in quotation marks,

**[00:46:52]** then we particularly have to look at loop engineering and ask, what are the

**[00:46:58]** acceptance criteria for our loops, and there I read, and I had also written this into the

**[00:47:04]** script for our episode, this wonderful metric,

**[00:47:07]** verification effort per delivered change. So you say, exactly as you

**[00:47:13]** just described, I look at the commits and say, no, you will have to do that

**[00:47:18]** again, we need to talk about the acceptance criteria once more,

**[00:47:21]** they clearly were not sharp enough. And that is a metric which, when it goes lower,

**[00:47:29]** when it falls, means your acceptance criteria are better, and from my

**[00:47:36]** point of view that is a criterion we can use for efficiency gains. Where we say, the

**[00:47:42]** time we as humans have to put in is simply no longer as high, or rather you

**[00:47:46]** no longer have to check as often, the better your acceptance criteria become. The problem

**[00:47:52]** with that is, I thought I had found a certain knack with Opus 4.8,

**[00:48:01]** with Opus 5 that is already, that hurts, with Fable I find it wonderful that I can talk

**[00:48:09]** to Fable about the acceptance criteria, that works relatively well, but Opus 5 is

**[00:48:13]** Opus 5, and the two of us will never be friends again. I think at the

**[00:48:18]** speed of the frontier models you do not need to get used to Opus 5 for

**[00:48:21]** very long. There will surely be the next one soon, but what

**[00:48:25]** while you were speaking, along those lines, I wanted to offer

**[00:48:29]** one more small personal tip to our listeners,

**[00:48:33]** if you notice that the AI has gone off the rails. First of all, that is

**[00:48:38]** a learning, and if you want to fix that learning, I would not

**[00:48:42]** advise anyone to work on the result, but on the path leading to it. So this issue of,

**[00:48:48]** oh, the thing generated process documents for me, for example, or generated a document from a process,

**[00:48:55]** and the document is wrong or has a mistake or something is missing or it is a bit too

**[00:49:01]** detailed or whatever. Then I would not recommend anyone to say, I will open

**[00:49:05]** it up and quickly change it by hand and save it. I would rather make the case,

**[00:49:10]** even if it costs tokens again, think about the point at which it

**[00:49:14]** probably took the wrong turn, at which point we were too imprecise,

**[00:49:17]** too precise, and that brings us to Opus 4.8 and 5 again. I mean, for one it might be

**[00:49:22]** a paraphrase, for the other that is one paraphrase too many, along the lines

**[00:49:25]** of, what is it going on about, I knew that already. And that out of

**[00:49:30]** this premise you try to repeat it for as long as it takes, even if it takes two

**[00:49:35]** or three interactions, until the system no longer makes that mistake

**[00:49:39]** as often, or no longer makes it at all, so that you get this learning effect both for yourself,

**[00:49:46]** how do I deal with the machine, and also, if it is a skill that I use

**[00:49:50]** or the department or the whole company uses, so that this mistake is weeded out for everyone

**[00:49:54]** and the thing is thereby taught sustainably to do things better.

**[00:50:00]** You said earlier, for example, that skills do not deliver a hundred percent perfection

**[00:50:06]** in the reliability of the result, you chose different words. I always say the difference

**[00:50:12]** between skills and prompts is that with skills you get a better quality result and more

**[00:50:16]** control over the result, where we now at all... And it being repeatable, that is 100 percent.

**[00:50:20]** Yes, because with skills you can also say, here is a bit of deterministic

**[00:50:25]** program code, you simply have to run that, because if I say via prompt,

**[00:50:29]** you have to pass all the tests, do not be surprised if out of ten tests

**[00:50:32]** eight remain and it says all eight passed, when there were ten,

**[00:50:35]** if all eight passed, whereas with the deterministic implementation

**[00:50:40]** you can at least make sure, is the answer tests-passed identical to the

**[00:50:44]** number of tests, otherwise take another look at what went wrong,

**[00:50:47]** but I would warmly recommend that to everyone again. If something does not work,

**[00:50:51]** think about how you can adjust it in the skill, and the whole topic of

**[00:50:56]** loop engineering is nothing other than explaining to a prompt

**[00:51:00]** how long it should attempt something, until what happens, in order to say it worked or it did not work.

**[00:51:08]** Because that is also a problem, just as at the start with our 80 percent.

**[00:51:12]** There are apostles standing around throwing terms about.

**[00:51:14]** Craft engineering, loop engineering, skills, prompt engineering, whatever.

**[00:51:20]** At the end of the day it is all basically the same thing.

**[00:51:25]** I would say iterative working and so on did not start with agents.

**[00:51:30]** But in the age of skills and the like, what changes is purely the expectation.

**[00:51:36]** What can I give the machine?

**[00:51:38]** How can I give it to the machine?

**[00:51:40]** How do I engage with it?

**[00:51:42]** A good prompt is also at home in a good skill,

**[00:51:45]** and loop engineering is a good skill that effectively knows

**[00:51:48]** how long one has to keep working, whether deterministic or non-deterministic.

**[00:51:53]** From that side one should not let these terms put one off.

**[00:51:56]** I am with you there.

**[00:51:59]** For me there is an essential difference between a prompt, even if you keep

**[00:52:06]** copying it back and forth and say, well, I can reuse it.

**[00:52:10]** The point is, a skill is effectively like a radiated intent.

**[00:52:16]** I say what I intend to do and thereby enable feedback and learning.

**[00:52:22]** And learning in particular. Which means, well, what I tried out in a loop, we

**[00:52:30]** will come to that in a moment, but if you say, I am executing this skill, so you hand the harness a skill

**[00:52:38]** and say, here, please carry out this task, apply the skill, and you are not satisfied with the result.

**[00:52:43]** Then at the end of the session, once you are satisfied with the result, once you have talked to it about

**[00:52:47]** what it should do differently, you can always say, right, now take the learnings from this,

**[00:52:53]** from this session, what do you have to change in the skill, add, leave out, so that you reach

**[00:52:59]** this result in considerably fewer steps. Which means these working instructions

**[00:53:06]** that you write into the skill, you can keep developing them continuously and iteratively.

**[00:53:11]** And this learning and unlearning is a huge thing, where AI, through skills,

**[00:53:19]** has clearly, well, in the end visible advantages over a human being.

**[00:53:26]** Humans find it considerably harder to make their knowledge as explicit as you can

**[00:53:32]** with an AI in a skill. And because we do not make it explicit, not everyone can

**[00:53:39]** say what is in their memory. And correspondingly also consciously say,

**[00:53:45]** I will take that out of my, no, I will take that out of my memory, I will no longer think that

**[00:53:50]** from now on. What I was just about to say, I once tried to

**[00:53:57]** build that into a piece of loop engineering, along the lines of, and if

**[00:54:02]** you get stuck, then learn from it and optimise your skill. That was a daft

**[00:54:08]** idea. Because what came out was something similar to your 20 million a day later, and all of a sudden it

**[00:54:16]** decided to build something completely different, but that solves your problem too, roughly. No.

**[00:54:22]** I think with this skill learning, I have, you mentioned the skill workshop earlier,

**[00:54:28]** Greetings go out to my Git repo, I have another Git repo called SkillForge, where at the time I was

**[00:54:33]** of the view that if a skill does not reach a goal, then you can effectively say to the AI, listen,

**[00:54:38]** this did not work in such and such a way, or the skill has the following problems, keep reworking the

**[00:54:43]** skill until this problem is gone. Yes, that was always quite nice as far as it went, and in

**[00:54:49]** many cases it worked well. By now, and I have not yet entered this, I am of the view

**[00:54:55]** that there is a component many people forget, namely skills are instructions, do

**[00:55:02]** this, do that, then do the other, mind the following, carry on until. But depending on

**[00:55:08]** where you deploy a skill, it may well need contextual knowledge. So let me take

**[00:55:13]** the topic of requirements engineering again. Where is my backlog, actually? Depending on the case

**[00:55:19]** that might happen in different systems. Possibly, yes, in a different language, with different

**[00:55:24]** terminology, with a different domain. So there are things that you do not,

**[00:55:28]** yes, okay, this is how a good story is shaped, but where you simply want to give it additional

**[00:55:35]** background information, and the idea at the moment is to give it something like a learnings MD,

**[00:55:40]** in which it does not write into a work instruction, if that is there, you write

**[00:55:47]** that there and you query the following, but which states from the outset, listen,

**[00:55:54]** if you do not have any people, ask for them, otherwise take these as the default.

**[00:55:57]** If you have this, that or the other, you will find such and such things in such and such a place.

**[00:56:01]** Where effectively, through enrichment with knowledge, the system does not only know.

**[00:56:07]** An example I had recently was someone explaining to

**[00:56:10]** the system how to make a phone call.

**[00:56:12]** The previous skill explained, pick up the receiver,

**[00:56:14]** take the dial, press the numbers.

**[00:56:16]** If you know what a dial is, congratulations.

**[00:56:18]** I am old, please google it.

**[00:56:20]** Take the dial, enter the number

**[00:56:22]** and then it goes beep beep beep, someone picks up on the other end, and with the contextual knowledge it knows that it should answer politely and in a friendly manner, that it should use the formal address, that it had no idea and that it is Mr Müller being called, and that if it is calling some adults-only provider it should speak differently, to cut a long story short.

**[00:56:40]** Pass on knowledge, pass on context, and not just plain instructions. With that I somehow have the feeling I can increase the efficiency of skills enormously once again.

**[00:56:51]** Full stop. You are looking sceptical.

**[00:56:54]** Yes, no, with the dial, mine always went with...

**[00:57:05]** But fine, that is another topic.

**[00:57:07]** At this point I shall have to play in a genuine audio file.

**[00:57:12]** On the matter of the dial I agree with you.

**[00:57:15]** I see, well, if we pull this back to the topic of efficiency and metrics, what do we measure it against, then I would like to set down three rules that were my learnings.

**[00:57:28]** The first you have essentially already said, and I also think it is common sense.

**[00:57:34]** If you want to reach a goal, then you rarely define

**[00:57:38]** only a single criterion for that goal, instead you always give it some kind of context and say, the factor out of the whole thing

**[00:57:46]** is your goal. There is not one single metric that will make you happy as a company, because

**[00:57:54]** that always leads to people trying to game that metric and trying

**[00:57:59]** to work around it somehow, like manipulating the skills or manipulating

**[00:58:07]** the working environment. But if you manage to tell it, listen, these are the conditions

**[00:58:12]** and these are the criteria by which you do it, and you may not change the

**[00:58:16]** conditions. This overall factorisation, that is rule one for me, never a single number,

**[00:58:25]** but always a factorisation, and saying, this is the overall picture of the goal. Then, rule two,

**[00:58:32]** I defined, send counter-metrics along with it. Meaning, they travel alongside. It is not

**[00:58:39]** about saying we want to reach a number, which is, we want to make so much more profit with the

**[00:58:45]** same capital investment, instead you always have to look at further

**[00:58:51]** metrics as well. Greetings go out to DORA, META, things like change fail rate,

**[00:58:59]** lead time, work in progress, developer experience, Goodhart's law, there are countless

**[00:59:07]** things that can be relevant and genuinely proven metrics, and for your particular

**[00:59:12]** goal, look at which counter-metrics are relevant for you, which should improve

**[00:59:20]** or at least not get worse, and the third is the topic of self-reported speed.

**[00:59:27]** When I ask developers how much faster they have become through GitHub Copilot.

**[00:59:35]** Well, it is at least 20 percent, right?

**[00:59:39]** But we now have several examples where companies have actually measured it

**[00:59:45]** and where developers said, yes, we have become 25 percent faster,

**[00:59:49]** and de facto it turned out they are actually up to 20 percent slower, because they

**[00:59:55]** spent far more time on pull request reviews, on follow-up corrections and so on.

**[01:00:01]** So honestly, establish a baseline, work out together with the people how it is

**[01:00:09]** calibrated, and do not do it by gut feeling and self-reported speed.

**[01:00:14]** But I would like to raise a small objection at this point.

**[01:00:19]** We measure the topic, so what you just said, how much faster does it make you?

**[01:00:25]** That pays into what I said earlier, a year ago I would never have thought I could manage all that.

**[01:00:30]** To be fair, one can question whether bringing my old eight projects back to light is worth anything or not.

**[01:00:37]** That is my personal game.

**[01:00:39]** Game, but if I now look at a company and people in software

**[01:00:44]** development are confronted with AI, then it is not like this. Here you go, folks, here is

**[01:00:51]** the AI, have fun, and there is your efficiency. A great deal changes in how people work together. If

**[01:00:58]** you have someone who now, I do not want to judge it as good or bad, but you have just

**[01:01:02]** brought in the example of loops and skills and so on, and let us say we now

**[01:01:06]** adopt what I did. Then someone starts, perhaps takes a bit of time for

**[01:01:11]** the question of what I intend, intent, and then the thing runs, and we do not shut the lid, for three days

**[01:01:17]** straight and the result is pretty good. Then in those three days they have pushed so much stuff over

**[01:01:22]** the wire that everyone else on the team first stands there and says, oh damn,

**[01:01:26]** here comes a pull request, it looks more like the flooding of an entire region. We

**[01:01:31]** are overwhelmed, because you run into other people who work in a quite

**[01:01:36]** fixed way, and the topic of the weakest link being the strength of the chain is at

**[01:01:40]** that point, damn it. Imagine requirements engineering delivering like

**[01:01:44]** crazy, then it is the developers who cannot work through it, or the

**[01:01:47]** developers, because they opened Pandora's box first and

**[01:01:50]** get to savour the sweet taste of the honey most intensely right now,

**[01:01:53]** notice, oh damn, I can use this, but you get

**[01:01:58]** Quite different questions become important for them.

**[01:02:00]** The other day, for instance, we learned that in your coding guidelines you used to have

**[01:02:04]** the topic of commenting source code.

**[01:02:07]** And commenting source code, when you work with agents, is a pain in the neck, to

**[01:02:13]** put it that way.

**[01:02:14]** Because what does the agent do?

**[01:02:15]** The agent says, oh look, the comment says what this routine

**[01:02:19]** contains.

**[01:02:20]** I do not have to read the routine at all, it is in the comment.

**[01:02:23]** So we first drove that out of the agent, it should no longer comment, it should

**[01:02:27]** no longer comment the technology, but comment the domain logic. So that it writes

**[01:02:31]** the domain logic down somewhere, without drawing conclusions about the code.

**[01:02:36]** And we considered doing things like, in Cantas for instance, regularly

**[01:02:40]** telling it to carry out a renaming of the functions and variables in our

**[01:02:45]** stuff. Why? Well, if it generates boilerplate code somewhere that it never calls

**[01:02:49]** again, it will notice at the latest during the renaming that there are no

**[01:02:52]** counterparts left at all. You would never have written that into such a rule in the past.

**[01:02:56]** Today, let us say you have, who knows, a development team of, say, ten people, each of them now spends not three days but a day at a time hammering code into a repo, and the poor thing goes, or whatever you use as source code management, and the people working in it are suddenly flooded with code.

**[01:03:14]** Now this code, even if there is boilerplate and whatever else in it, may well serve its purpose.

**[01:03:20]** It builds a solution that can, and now the testers come round the corner and say, damn it, whoa, whoa, why is your backlog empty again?

**[01:03:27]** We have only just started a two-week sprint, we are on day three, why is the backlog empty?

**[01:03:32]** And suddenly people are put in a position of no longer talking about what needs doing, when do I have time for it,

**[01:03:40]** instead they have to talk about handling the volume, the challenge that arises from

**[01:03:47]** the sheer mass and the speed, dealing with that, each individual as well as the

**[01:03:52]** chain as a whole.

**[01:03:53]** And I think that pays enormously into the topic when such reports come in,

**[01:03:59]** along the lines of, people feel more efficient because they judge the matter themselves.

**[01:04:04]** But looking at the chain says, you are getting slower.

**[01:04:08]** Because suddenly there is far more time spent on discussions that previously had no time to be had, because perhaps people feel

**[01:04:15]** overwhelmed,

**[01:04:17]** wounded in their pride. How can it be that the AI can do this? That was always my hobby horse.

**[01:04:22]** You have a great many side theatres that can currently still rob you of this efficiency.

**[01:04:28]** Absolutely. It is not one single reason, but they can. No, no, but I am with you there. So that was in the end also what

**[01:04:35]** I was getting at earlier, if we grasp AI, in quotation marks, merely as a tool,

**[01:04:41]** then we focus on touch time. That is, wherever something is actually handled. And that

**[01:04:49]** is very, very dangerous, because if we are not aware of it, then it leads to

**[01:04:55]** you writing, or letting Claude Code change something in the code on your laptop, and

**[01:05:02]** in the worst case it is precisely not code in a programming language, but it is

**[01:05:09]** for instance skills or some instructions that have to go into the model

**[01:05:15]** again.

**[01:05:16]** Or it is skills or whatever, where you say, well, this is not about,

**[01:05:21]** I cannot do any schema validation here on whether the syntax is correct,

**[01:05:27]** instead I would have to carry out a substantive, semantic check on whether what

**[01:05:33]** Claude Code wrote there is correct. And then you pour that into a pull

**[01:05:38]** request, so you push it into the code repository, and then you do not have it reviewed

**[01:05:43]** by humans, but by another agent, and that one comments on it again and

**[01:05:49]** says, yes, here, you could do this differently. And then you perhaps also have

**[01:05:53]** your Claude Code looking at this pull request and saying, oh, the other one said

**[01:05:58]** I have to change something here. And I think I said before that with the release of,

**[01:06:03]** I think it was Opus 4.8, the thing became much, much more verbose, Opus 5 even more so,

**[01:06:11]** in terms of what it pushes into pull requests. Which means, if on the other side I have a

**[01:06:16]** Git and there is a GitHub Copilot doing the code reviews automatically, and Opus

**[01:06:22]** pushes far, far more code changes in than are actually necessary, then

**[01:06:28]** GitHub Copilot has far, far more to look through as well. Which means you burn far

**[01:06:33]** more tokens because the output from Opus is so high. You burn even more tokens because

**[01:06:39]** GitHub Copilot has to look at a great deal more. And that generates output again in turn.

**[01:06:44]** So it escalates, and we have the opposite of efficiency. Which means,

**[01:06:49]** we actually have to look at what we want to achieve.

**[01:06:52]** We want to optimise the flow, and that brings me back to end to end.

**[01:06:59]** In the end we want to optimise the cost-benefit ratio.

**[01:07:03]** And that means we do not need 15 reviews from GitHub Copilot,

**[01:07:07]** instead what we have to look at is, what is the smallest possible change

**[01:07:12]** I can make to a piece of software in order to reach the desired goal.

**[01:07:16]** And that is what we have to teach the AI, and then start the whole topic of lead time and wait time optimisation.

**[01:07:26]** And how people might complement one another in their job roles in future.

**[01:07:32]** And what someone might take on and what someone might leave aside.

**[01:07:35]** But perhaps, since you brought up two more points, I think that is also a very quick cost trap,

**[01:07:41]** when AI leads to events at other AIs and the same yardstick is not applied there,

**[01:07:47]** because if the thing says that was bad and the other thing says, okay, I will rework it,

**[01:07:50]** we very quickly arrive at, oh, 24 hours later.

**[01:07:54]** We are still stuck on the same routine. What is going on there?

**[01:07:56]** Other than it being expensive.

**[01:07:58]** What I would perhaps also like to offer at this point on the subject of best practice, in my view,

**[01:08:04]** is one thing, namely that teams should be working in the same harness,

**[01:08:09]** so that you can use the same efficiencies and the topic does not play itself off against you.

**[01:08:15]** So take Codex and Claude Code, with Claude Code this Let's Simplify and Code Review

**[01:08:21]** and whatever all that stuff is called, I do think it is noticeable

**[01:08:25]** that if you have mixed operation of models and harnesses in a team,

**[01:08:31]** they sometimes get in each other's way a bit as to where they place their optimisation priorities.

**[01:08:36]** The second is, who would have guessed? Skills. At the moment I am quite of the view that you should have skills for things like architecture patterns, what is good code, so that a human perhaps always has a chance to look at it, what matters to you, what matters in information security,

**[01:08:53]** what matters in data protection and so on, pouring that into a skill so that you effectively have it

**[01:08:56]** running along during development, having such libraries, I mean, we have something, but on the

**[01:09:04]** market there are things like Ponytrail and ADHS skill and whatever else, that effectively get the system to

**[01:09:11]** be the laziest developer in the world. Along the lines of, only write the lines you

**[01:09:16]** really need, and not three more. Claude Code has now also implemented a switch in the output

**[01:09:21]** settings so that it handles its interaction with you more

**[01:09:26]** economically in terms of tokens. There too it is always worth keeping an eye on things, and at the latest there you notice

**[01:09:32]** that when you are working in the same harness, you can also help each other with

**[01:09:38]** a learning, have you seen this yet, because regardless of how large or

**[01:09:43]** small companies are, personal experience, or the I saw that on TikTok,

**[01:09:48]** we really should take a look at that. It is not always the weakest option. Some people get something out of it.

**[01:09:52]** Or through podcasts like this one, whether as a listener or as a guest or as a host.

**[01:09:57]** And at that point there is a lot you can optimise about these things.

**[01:10:03]** And if you then hand it up to the machine and the machine does the assessment,

**[01:10:09]** then I also think it is a very good quality indicator if you ask the machine

**[01:10:16]** not only to say, you have to change this. Here is a finding, but also, how certain

**[01:10:21]** are you that this is a finding? So is that a probability of 20 percent or

**[01:10:26]** are you 20 percent certain or 100 percent certain? And what effort do you expect for it?

**[01:10:33]** Because frankly, you may have noticed this too, when you ask it how long

**[01:10:36]** it would take for that? Then it says three weeks. It calculates that in human time

**[01:10:40]** and not in machine time. And I think that is another good

**[01:10:44]** lever, I would not necessarily say I would bet my house on it, quite apart

**[01:10:47]** from the fact that I rent. If you ask it, how much effort do you see in that,

**[01:10:52]** how much effort then actually occurs, then you might always be able to derive

**[01:10:56]** a small correlation from it, how efficient was the work with it. And if

**[01:11:00]** you tell it beforehand, you are assessing something, so give me the expected effort

**[01:11:04]** as well, and please give me your confidence, how certain are you, then

**[01:11:08]** you have further checkpoints that you can use in your skill again, along

**[01:11:11]** the lines of, well, if it says that is three weeks of effort, again, the AI does

**[01:11:16]** it faster, but an effort that takes three weeks still takes the AI, let me

**[01:11:20]** say, 30 minutes, and for an effort of one week it takes 10 minutes, from that you

**[01:11:23]** can already derive something, and if the system is additionally only 20 percent

**[01:11:27]** certain, then those are all further factors for you perhaps to say,

**[01:11:32]** I will not trigger a review there at all, or I will have these cases checked by humans

**[01:11:36]** beforehand, then you have quite different quality gates, compared with simply blindly

**[01:11:40]** saying, the AI assesses, the AI executes. Both sides may have knowledge of

**[01:11:47]** these other factors I have just named, but if you do not tell it, use

**[01:11:51]** these as assessment criteria, report them, make the decision depend on them,

**[01:11:57]** even the sentence, only implement it if it is economical. That could well

**[01:12:03]** draw conclusions, you could at least try it out and see to what extent it helps you in

**[01:12:08]** your processes. My plea ends with this sentence. Do not simply ask the AI whether something has to be

**[01:12:14]** adjusted, because it will say every time, good idea, thank you for pointing that out to me.

**[01:12:18]** That is fascinating. Nobody before you had that idea, you were the best human handler

**[01:12:23]** of AI ever. May I, do I have to work with all those other humans? I only want to work

**[01:12:27]** with you, you are the best. It just tells you what you want to hear. So it talks to me.

**[01:12:31]** Exactly, what I see is that many people are now coming up with the idea, well,

**[01:12:38]** generation scales, human quality assurance does not, so I will see to it that I replace human

**[01:12:45]** quality assurance with AI as well. From my point of view that is not a good idea.

**[01:12:50]** Replacing human quality assurance, as far as possible, with deterministic quality assurance,

**[01:12:57]** meaning automation, is a good idea. But putting AI in there, which if in doubt,

**[01:13:04]** I do not even know how many AI exploits there were again this week, but you can really talk

**[01:13:11]** almost any model into doing things that you previously told it very clearly

**[01:13:17]** not to do, please leave that, do not do that, because they are simply only soft boundaries, and that is why

**[01:13:23]** I found this study while preparing for the podcast, where they researched engineering

**[01:13:32]** change in aircraft manufacturing and then established that, well, actually

**[01:13:36]** only 8.5 percent of the entire chain is value-adding time.

**[01:13:41]** Which in the end means you have roughly two weeks of waiting time per one day of work, and

**[01:13:48]** that shows that lead time is in the end a queuing property and that we have to think

**[01:13:53]** about what the elements of lead time are, and precisely the waiting time, things like queues,

**[01:13:59]** hand-offs, approvals, work-in-progress limits, that in the end the answer to becoming more

**[01:14:08]** efficient through AI is a flow and governance programme, even if people do not want to hear

**[01:14:15]** governance, but in the end it is about saying, what should the flow look like

**[01:14:20]** and what are the rules we stick to while doing it?

**[01:14:23]** It is not about a tooling rollout.

**[01:14:25]** It is about deciding what game we are playing.

**[01:14:29]** And if that is football,

**[01:14:31]** then we do not play with our hands.

**[01:14:33]** And then there are the white lines and they mark out of play.

**[01:14:36]** And we can discuss once more whether we play with or without offside.

**[01:14:39]** But fundamentally a goal is a goal.

**[01:14:42]** Otherwise we are not playing the same game.

**[01:14:45]** And for me that is governance.

**[01:14:47]** And once we have clarified these rules of play at the start,

**[01:14:50]** it makes the game much faster as well.

**[01:14:52]** Because you no longer have to discuss what a touchline actually is and

**[01:14:56]** why I am not allowed to carry the ball into the goal.

**[01:14:58]** And above all, once it is there, you also have to distinguish between the moment

**[01:15:04]** where a person perceives a change as, huh, what is going on here?

**[01:15:08]** Suddenly someone wants to tell me how to work with this, and the point where it shifts

**[01:15:12]** to the topic becoming second nature.

**[01:15:15]** I think that does not take long at all.

**[01:15:17]** that we should ignore people and so on. That was not my intention at all. That was simply more the point.

**[01:15:23]** Let us also not unleash every bit of AI slop straight onto a human reviewer, because there are sometimes

**[01:15:30]** things where you say, okay, let us go through it beforehand. I had a case recently, I made a screen recording of our

**[01:15:36]** application to document for others what you can do with it and how you use it.

**[01:15:41]** Then I had an idea and effectively gave it its own video.

**[01:15:45]** Two insights came out of that which I found fascinating, first of all it went, oh!

**[01:15:51]** I can now assign a few things better in terms of the domain logic, because I was also speaking on the video about what I was showing.

**[01:15:58]** And the second was, listen, you probably did not notice, but at this point the cursor was positioned wrongly,

**[01:16:03]** at that point a spacing was wrong and so on, and then it immediately said, shall I write a few issues about this

**[01:16:08]** And you sit there and think, okay, thank you.

**[01:16:13]** Yes, although at this point you can also ask yourself again,

**[01:16:17]** why do you actually want to burn tokens now

**[01:16:20]** operating the Jira API in order to create issues?

**[01:16:23]** But fine, another topic.

**[01:16:25]** I would say...

**[01:16:27]** No, no, no, no, no, I am not letting that one pass.

**[01:16:30]** So you will not catch me out that quickly with the line of,

**[01:16:34]** well, you have now burned tokens to operate Jira.

**[01:16:37]** The second is, an important feature of our harness is reporting the associated costs, not in the form of what did the light in the broadcast cost, but in the form of the euro value of tokens.

**[01:16:51]** And when I look at how much money, or how little money, I do not want to frame it, because if I now say how much money, then everyone will be left with, he talked about a lot of money.

**[01:17:02]** What does it cost me in euros if I have a backlog item maintained,

**[01:17:07]** have an issue in Git maintained or whatever else?

**[01:17:12]** For that money I would not have clicked it myself.

**[01:17:15]** That is, opening it up, clicking, writing, phrasing.

**[01:17:19]** If you have clarified the rules beforehand, where it then perhaps also answers with questions, talks to you,

**[01:17:24]** we are back at rules.

**[01:17:26]** I never made a plea against it, remember.

**[01:17:29]** also said something like, with skills you can also standardise things where you may previously

**[01:17:33]** have spoken into the room, where there were plenty of ears listening

**[01:17:38]** along, who on leaving the room at the latest thought, what was that old fat white

**[01:17:41]** man going on about?

**[01:17:42]** We will do it the way we have always done it.

**[01:17:44]** But that is nothing new with AI either, that would, that would have

**[01:17:51]** always, and here I look back at the topic of extreme programming, those people

**[01:17:56]** already made the case for conventions and agreeing on how we want to

**[01:18:03]** work.

**[01:18:04]** But fine, I would like to summarise it like this, and you keep looking at the

**[01:18:09]** clock and then talking about the...

**[01:18:11]** Hold on, stop, stop, stop, stop.

**[01:18:12]** You are very welcome to summarise, but we are, and bear in mind, we still have to resolve

**[01:18:17]** the Plaud story very briefly, because at the end that means.

**[01:18:20]** I would perhaps like to do that and afterwards leave the summary

**[01:18:24]** to you, because, well, credit where credit is due. Do you want to, or shall I say why

**[01:18:30]** I wanted to hear that from you? Listen, I started earlier telling the story

**[01:18:37]** of what is all possible with smart speakers and voice input, and the thing

**[01:18:42]** about voice input, some of you have surely heard the episode,

**[01:18:46]** when I was on holiday with Jens, about my dream interaction device, the Plaud, the voice dictation gadget,

**[01:18:55]** I have no idea, this is not getting any more professional at this late hour, I am enjoying it, and you

**[01:18:59]** got yourself one as well and apparently have things to say about it. So, is this praise or criticism

**[01:19:06]** or what is it? Well, when you were out and about with the Plaud, I already had

**[01:19:12]** the voice memos, and then realised, damn it, the voice memos are on my

**[01:19:16]** iPhone, so unless I do something about it they get synchronised to iCloud, and

**[01:19:22]** we covered that in the last podcast, where I said, iCloud is something for which I as a private individual

**[01:19:29]** accepted the terms of use, which means nothing belonging to my employer

**[01:19:33]** has any business being in there.

**[01:19:34]** Ergo I have to come up with something that works differently.

**[01:19:39]** Which means I would need a dictation device that is entirely local to the device, where I can then effectively

**[01:19:45]** pull the material down from my laptop, for example.

**[01:19:49]** And in theory that should have worked with the Plaud, and I then, I think it was

**[01:19:58]** an Opus, yes, Claude Code on my laptop with an Opus connected through Bedrock,

**[01:20:02]** said, listen, here is the Plaud SDK, read through all this stuff,

**[01:20:08]** here is my device, how do we do it?

**[01:20:12]** And the thing whirred and whirred and tied itself in knots with, okay, now

**[01:20:16]** I will build a demo app, and then on the demo app I have to somehow read out the Bluetooth communication

**[01:20:24]** between your iPhone and the device, so the short version is, it tied itself in endless

**[01:20:31]** knots trying to work out how to get these audio files onto my laptop with as little

**[01:20:38]** loss as possible, and what you told me was that

**[01:20:44]** your Claude had no trouble with it whatsoever.

**[01:20:47]** You summarised that nicely, and I would say we put it together and move on.

**[01:20:51]** Sorry. So.

**[01:20:53]** No, I am asking myself why. What did you do differently from me?

**[01:20:56]** I do not know, perhaps we need to share our projects some time.

**[01:21:00]** The beginning really was like this.

**[01:21:02]** You get Claude and then it runs against their own backends, and

**[01:21:07]** then you have their MCP server, which also plays up sometimes, because it somehow

**[01:21:12]** takes the view that there are no new recordings in the last week, and you think, eh, I

**[01:21:15]** talked that thing full, what is going on there?

**[01:21:17]** That is one thing, the second is, the Plaud SDK, there I could get a token

**[01:21:24]** and an API key from them, which effectively allows me both to consume cloud services from them,

**[01:21:32]** things like transcription, for example, that is, converting an audio file into text. It also allows

**[01:21:38]** me, I had to fetch it from them once, that key, so that

**[01:21:44]** with the Plaud thingamajig, to use professional terminology at this point, another tick...

**[01:21:50]** With the Note Pro it is, yes, since I have no advertising, I cannot talk about a sponsor.

**[01:21:54]** So at this point I would happily get in touch, but beforehand my son told me

**[01:21:59]** I should contact Holy, because good podcasts have Holy adverts and he would like more Holies,

**[01:22:04]** so from that side, if anyone is listening, we will take that too. No, but joking aside. And it

**[01:22:09]** then fetches the audio file, and I mostly end up in the discussion with people who then say,

**[01:22:14]** hang on, just for the audio file does that even make sense, because... yes. Audio file,

**[01:22:18]** you have already said that, why get yourself a device, why not take,

**[01:22:21]** like Alex, the voice memos, quite apart from where the data contract runs,

**[01:22:25]** the iCloud contract or whatever. For me the device really is the

**[01:22:31]** game changer at this point, because firstly I press a button. Fine, now you can say I can do that

**[01:22:36]** on the iPhone too, right? But I press a button and it records. Full stop. No, exactly. Your

**[01:22:42]** Plaud, yes. Tell me, it does not have to. A call comes in and that is the end of it. If I

**[01:22:46]** get a call, or if I want to fiddle about on my phone during something, or yes, so anything

**[01:22:51]** that touches audio input and output puts my voice memo recording at risk. That is

**[01:22:57]** one point in favour of a device for me, and I was in fact very happy. So we

**[01:23:02]** really should swap our projects some time. But that it said, listen,

**[01:23:05]** give me the key here and then I can effectively pair the device in my app, can

**[01:23:11]** download data, can delete audio files, and can then devote myself on my device to

**[01:23:19]** transcription. Do I have challenges with that? Yes, because I have a

**[01:23:25]** bit of a sense of honour, I would have liked to do everything with Apple Intelligence. At

**[01:23:30]** that point you run into the drawback that you do not have speaker

**[01:23:35]** recognition, although that is quite funny too. When people are talking

**[01:23:40]** with each other, then at some point it starts anyway and says, so Marco

**[01:23:44]** told Mr Schommau and Günther and Maya, I do find that

**[01:23:48]** quite funny. It is rather nice. Is it 100 percent stable? No, it is not yet, but it is

**[01:23:59]** in that sense also the result of an AI system. I pestered it with my wishes and

**[01:24:06]** it delivered me a result, whether there is still the odd quirk

**[01:24:11]** in there, possibly, but I can pull the data onto my notebook and then do effectively

**[01:24:19]** what I want there. So I would say we have, I am not quite at the goal yet, but we have

**[01:24:26]** both reached roughly the same result. Except that yours was clearly faster

**[01:24:31]** and from what I observed also more efficient. And my question would be, as a tip for

**[01:24:38]** the listeners, how did you set up your harness, what did you actually use for it and what

**[01:24:44]** did you tell it? Did you use a slash goal with target criteria, did you give it any

**[01:24:51]** skills, what did you do? So, the private code on your laptop...

**[01:24:56]** So, the private code on your laptop...

**[01:24:58]** My coding agent of choice is still Claude Code. Behind it, quite apart

**[01:25:05]** from the fact that it is hooked up to various things where it tries to retain the insights from historical

**[01:25:12]** treasures for future treasures, so a bit of memory, I have a few skills

**[01:25:17]** in there, such as this ADHD skill, which tries to keep it roughly on track,

**[01:25:24]** I have this Superpower plugin, which makes sure that it clarifies with me beforehand what

**[01:25:30]** I actually want from it before I set it on projects.

**[01:25:34]** Grilling or brainstorming?

**[01:25:36]** Okay, sorry, you have now actually completely thrown me off at this late

**[01:25:40]** hour.

**[01:25:41]** I use it first for brainstorming, along the lines of, have I now thought through everything

**[01:25:47]** I want to discuss with it, and after that, what I am getting at is, I get it to

**[01:25:52]** write itself a plan and then stick to that plan, and this is where

**[01:25:58]** ADHD is really cool again, because it additionally, it also, it additionally

**[01:26:03]** creates actual Python scripts, which then check during development by

**[01:26:08]** Claude Code that it has not meanwhile veered off to the right. And then at

**[01:26:13]** the end it is slash goal, implement the plan in whatever manner and report back when

**[01:26:18]** finished. For that I have a standard phrase, like the one I already tried to

**[01:26:22]** offer earlier, which in fact sits in a text file for me that I

**[01:26:26]** always copy out. You now have everything you need. You do not need to ask me any more.

**[01:26:29]** All the decisions you have to make you can make independently based on the information

**[01:26:33]** you have. There we have got some very good tips out of Mark

**[01:26:39]** at the end of the 90 minutes. I thought that was good for everyone

**[01:26:46]** who stayed with us. Thank you, Mark. Since we are already at this subtle

**[01:26:56]** form of appreciation. Would you like to tell us what has stayed with you from today's episode in terms of

**[01:27:02]** learnings, what you would like to summarise? Given the time, yes, the patience and the

**[01:27:08]** staying power. Oh yes, of course, the person stuck in traffic!

**[01:27:12]** Warm greetings to Mainz, to the person who is now stuck in a traffic jam and told me that he always listened to this on the way home on Mondays.

**[01:27:19]** Matthias, these greetings go out to you. Right, that had to be said. Now over to you for the summary, please.

**[01:27:25]** Yes, so the very first thing for me is the topic, I wanted to go through the things

**[01:27:33]** we talked about from the back. I personally tend towards over-thinking and perfectionism, and

**[01:27:40]** quite honestly, drop that, define what you want to achieve, talk to the AI about

**[01:27:47]** what you want to achieve. Exactly as Mark said, put that into the plan and think

**[01:27:53]** ideally while you are at it about how you really get it to the goal. That is, to where you want it,

**[01:28:01]** because the first learning is that if you use AI as a tool, then it shortens a

**[01:28:08]** work step, but the real efficiency gain lies in the waiting times between the

**[01:28:13]** work steps. And anyone who simply buys AI as a tool cannot achieve that efficiency

**[01:28:20]** gain. The second thing, and this again comes back to the example Mark just

**[01:28:25]** gave, is the right level of quality. That can only be decided against the requirement.

**[01:28:32]** What quality is really relevant for the customer in this case? What are the

**[01:28:38]** conditions that play a role here? Which means we can bring in the customer,

**[01:28:43]** we can bring in regulations, we can say there are service level objectives,

**[01:28:47]** that the company expects, or anyone else, but, excuse the expression, everything

**[01:28:52]** else is computer-scientist romanticism. Computer-scientist romanticism? Yes, there is another word

**[01:29:02]** for it that is not suitable for minors, but we shall leave that. I find computer-scientist romanticism more charming. That is how it is.

**[01:29:09]** And in the end, do not fall for any efficiency narratives.

**[01:29:16]** Spotify did this, Toyota did that, so-and-so optimised 95 percent of their

**[01:29:24]** tasks.

**[01:29:25]** It is your environment in which you want to do something, establish a baseline there, and depending

**[01:29:33]** on the baseline you say what the things are that you want to optimise, under which

**[01:29:37]** criteria.

**[01:29:38]** Efficiency claims without a baseline are narratives.

**[01:29:44]** While you were speaking I would like to offer something that came into my head,

**[01:29:48]** as my closing plea.

**[01:29:50]** I have already shared the other tip, yes, but my closing plea,

**[01:29:54]** for anyone working with AI, always with a view towards

**[01:29:59]** professional use, if you do not know that you could fail,

**[01:30:03]** you will not do it either.

**[01:30:06]** People who say, no, that is simply not possible.

**[01:30:10]** They may well not even try it in the first place.

**[01:30:13]** I had a case recently where I built something, and a colleague said, I simply do not

**[01:30:18]** understand it.

**[01:30:19]** Excuse me, Mark, you have no idea at all about this subject, but the result you have

**[01:30:25]** put in front of me is better than what I had worked out over three months.

**[01:30:29]** Better than what I expected to achieve.

**[01:30:32]** How did you do that?

**[01:30:34]** What is your tooling?

**[01:30:35]** I am reminded again of an earlier question, what do you work with?

**[01:30:38]** Then I said to him, I basically did not know what mattered.

**[01:30:42]** I had a problem, and I discussed it with the AI.

**[01:30:44]** We talked about it, we asked questions.

**[01:30:48]** Let me perhaps add another learning as well.

**[01:30:50]** I like to tell it, these and these are cool projects.

**[01:30:53]** Please look at them in terms of domain logic and technology, and also look at

**[01:30:56]** what you might be able to learn from them.

**[01:30:59]** Some really good things come out of that at times.

**[01:31:02]** And that is what I would pass on to people at this point, it will all work out.

**[01:31:07]** And I would say, before we drag this out unnecessarily.

**[01:31:11]** Alex, good to have had you here.

**[01:31:13]** I am absolutely delighted that you joined us on this podcast again.

**[01:31:17]** Everyone who listened, at some point we will sell something like air miles.

**[01:31:21]** Along the lines of, people who stayed with us the longest

**[01:31:24]** will have earned higher miles.

**[01:31:26]** Along the lines of, from then on there is a bonus.

**[01:31:29]** Good to have had you here.

**[01:31:31]** I would be glad if you came by again soon.

**[01:31:34]** Yes, and I say that to everyone as well, best wishes.

**[01:31:37]** I was just about to say, exactly.

**[01:31:39]** I do not only say that to you, I say it every time.

**[01:31:42]** If you enjoyed it, leave us a like,

**[01:31:45]** subscribe to the podcast, tell people

**[01:31:48]** that you are entertained here in a very engaging way.

**[01:31:51]** And with that I say, see you soon. Bye.

**[01:31:53]** Thank you.

**[01:31:56]** Welcome to Think Different. Think AI.

**[01:31:58]** the podcast by Mark and Jens.

**[01:32:01]** Two technology-loving minds who do not just talk about artificial intelligence,

**[01:32:06]** they live it.

**[01:32:07]** Here you get clear perspectives, real practical insights

**[01:32:11]** and a fresh look at what is possible.

**[01:32:14]** Understandable, critical and always with a wink.

**[01:32:18]** AI to think about, to smile about and above all to join in on.
