---
title: "Security Illusion"
episode_index: 54
published: "Sun, 23 Aug 2026 19:10:00 +0000"
duration: "3258"
page_url: "https://think-ai.podigee.io/54-security-illusion"
image_url: "https://images.podigee-cdn.net/0x,sQnT2YjFTlyCoe6JIGcwkfAoW-sV7GdpC_EKFaU3aGS0=/https://main.podigee-cdn.net/uploads/u73317/abba3675-aac5-4f85-aba8-20cf909a89b2.jpg"
audio_url: "https://audio.podigee-cdn.net/2572664-m-cd7f70fc00ddba09e32254b6e7b0ef5c.mp3?source=feed"
guid: "5ba280d44fd8e7a99d16bc046aae84da"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-08-23T19:20:03+00:00"
translated_from_language: "de"
translation_provider: "claude"
translation_model: "claude-opus-5"
translated_from_file: "transkripte/054 - Security Illusion.md"
translated_at: "2026-08-23T19:26:52+00:00"
---


# Security Illusion

**Published:** Sun, 23 Aug 2026 19:10:00 +0000
**Duration:** 3258
**Web player:** https://think-ai.podigee.io/54-security-illusion
**Cover:** https://images.podigee-cdn.net/0x,sQnT2YjFTlyCoe6JIGcwkfAoW-sV7GdpC_EKFaU3aGS0=/https://main.podigee-cdn.net/uploads/u73317/abba3675-aac5-4f85-aba8-20cf909a89b2.jpg
**Audio:** https://audio.podigee-cdn.net/2572664-m-cd7f70fc00ddba09e32254b6e7b0ef5c.mp3?source=feed

## Description

Klaus Rodewig über Sandboxes, Threat Modeling und die Frage, was KI-Security wirklich neu macht
Zwei Premieren auf einmal: Klaus Rodewig ist wieder zu Gast, und diesmal sitzt Jens mit am Tisch, statt Mark mit ihm allein zu lassen. Das Thema ist KI-Security, und der Einstieg ist ein Familienfest. Wenn einer von seiner Rücken-OP erzählt, haben plötzlich alle am Tisch Rücken. Genauso läuft es gerade bei den KI-Laboren: OpenAI berichtet, ein noch unveröffentlichtes Modell habe bei Hugging Face Testergebnisse manipulieren wollen, Anthropic legt nach mit einem Modell, das 9.000 Ziele gescannt und SQL-Injections ausprobiert hat, dann kommt Meta um die Ecke. Fishing for Compliments, nur dass jeder betont, wie gefährlich er ist.

Klaus sortiert das Feld über ein Schichtenmodell. Unten liegen Netzwerke, Betriebssysteme, Dienste und Konfigurationen, und das ist die Schicht der gelösten Probleme. Darüber die Applikationssicherheit mit OWASP Top 10, Cross-Site Scripting und Buffer Overflows. KI-Security legt sich als neue Schicht obendrauf, weil nicht-deterministische Modelle eine ganz neue Klasse von Bedrohungen einführen. Mark ergänzt die Schicht, die alle vergessen: den Menschen, seit ein paar tausend Jahren ungepatcht. Der nigerianische Prinz ist keine Erfindung des Internets, vergleichbare Bettelbriefe kursierten schon zur Zeit der Französischen Revolution.

Der unangenehmste Befund der Folge steht in den Berichten selbst. Wer nachliest, wie die vielbeschworene Sandbox aussah, findet bei einem der Fälle als einzige Trennung zwischen Modell und Internet einen Satz im System-Prompt: Du hast kein Internet. Im anderen Fall arbeitete das Modell wie mit einem Zettelkasten und benannte Ordnernamen um, um darüber mit anderen Systemen zu kommunizieren, eine Einwegverbindung aus Dateinamen. Marks Fazit: Ausgebrochen ist da niemand, die Systeme haben Türen anders benutzt, als jemand gedacht hatte. Und wo niemand wusste, dass eine Tür ist, haben sie eine gefunden.

Klaus hält dagegen, dass der Sandbox-Teil der langweiligste ist. Rechner zuzunageln haben Generationen von Administratoren geübt, das gehört ins Feld der gelösten Probleme. Sein eigenes Setup ist entsprechend nüchtern: Auf dem Entwicklungsrechner läuft Claude Code mit abgeschalteten Rückfragen, und deshalb liegt auf diesem Rechner nichts außer Entwicklungsumgebung, Quellcode und einem GitHub-Zugang. Ein LLM ist für ihn ein omnipotentes Stück Software, ein bockiger Jugendlicher, der freundlich tut, das Wissen der Welt hat und sehr viele gefährliche Werkzeuge. Später kommt der Trost hinterher: Das Kontextfenster ist schnell voll, dann hat er vergessen, was er vorhatte.

Der Begriff, um den die drei kreisen, heißt bei Klaus Threat Modeling. Vorher überlegen, welche Bedrohungen sich aus der eingesetzten Technik ergeben, statt hinterher reflexhaft zu reparieren. Sein Beispiel ist ein Agent, der die Buchhaltung übernehmen soll: Der braucht Mails, Online-Banking und Dateiablage. Wenn er dann wegen einer versteckten Anweisung in einer Mail Geld überweist, ist das kein Rätsel, sondern eine Lücke im eigenen Modell der Bedrohungen. Passend dazu lag ihm im Urlaub „Threats: What Every Engineer Should Learn from Star Wars" von Adam Shostack auf dem Tisch.

Marks Gegenstück aus der Praxis: Ein Assistent sollte mit Microsoft Teams arbeiten, für das es an der Stelle gar keine nutzbare Schnittstelle gab. Das Ergebnis war trotzdem fertig, weil sich das Modell die lokale Datenbank auf der Festplatte vorgenommen hat. Dasselbe bei Mail, Kalender und Erinnerungen. Was früher als Botnetz erst auf den Rechner musste, sitzt heute als Agent-Harness bereits dort und benimmt sich nur anständig, und den System-Prompt hat man nicht selbst in der Hand. Eine Sandbox ist unter diesen Bedingungen eher Frischhaltefolie. Dazu passt der dokumentierte Fall, über den Mark auf LinkedIn geschrieben hat: weißer Text auf weißem Grund in einem Word-Dokument, und Copilot arbeitet die versteckte Anweisung mit ab.

Jens bringt die Nutzerseite ein. Die Oberflächen der Anbieter verwischen zwischen Chat, Projekten und Konnektoren, und der normale Anwender soll entscheiden, welcher Ordner freigegeben wird und was noch darin liegt. Seine Hoffnung ist eine Instanz, die mitdenkt und aufpasst. Klaus setzt dagegen auf den Markt, wie schon bei der Cloud: Am Ende siegt die Bequemlichkeit, und Anbieter mit einem Ruf zu verlieren bauen keine frei drehenden Harnesses. Es wird daneben ein Norton Antivirus für KI geben, das vor allem ein gutes Gefühl verkauft. Als Beleg, wie wenig hier vom Nutzer zu erwarten ist, erzählt Klaus aus seiner Zeit im Bankensektor, wie viele Menschen Zertifikatswarnungen einfach wegklicken. Mark kontert mit der Bank-Hotline, die ihm genau das empfohlen hat.

Zwei Fälle machen klar, warum klassische Begriffe nicht reichen. Der erste: In einem Versuch sollte ein Modell ein anderes trainieren, ohne dass die Zielvorliebe in den Trainingsdaten auftaucht. Sie wurde trotzdem übertragen, subliminal, unter dem Stichwort Chain-of-Thought-Steganographie. Der zweite ist der Hammer der Folge. Anthropic hat Claude Mythos beauftragt, eine neue Angriffsklasse gegen AES zu finden, den symmetrischen Verschlüsselungsstandard für höchste Ansprüche. Das Modell hat nicht nur eine Schwäche gefunden, sondern eine mathematische Angriffsklasse, die der Forschung in über zwanzig Jahren unbekannt geblieben war. Zur Beruhigung: AES ist damit nicht gebrochen, der Angriff gilt für eine auf sieben statt zehn Runden reduzierte Variante, die praktisch nicht vorkommt. Der Punkt ist nicht der Angriff, sondern die Art von Mathematik. Genau deshalb, sagt Klaus, greift hier auch keine KI-Psychologie mehr, sein Begriff für den Umgang mit Modellen, die man nicht mit statischen Security-Kategorien fassen kann.

Zum Schluss zeigt Jens eine Variante, in der das Prinzip von selbst funktioniert hat. Er wollte seine Desktop-Installation über Telegram ansteuern, OpenClaw fand die Idee gut und schlug sie vor, und Claude auf dem Rechner hat abgelehnt, weil sie eine Sicherheitslücke geöffnet hätte. Ein Modell, das den Vorschlag eines anderen stoppt, ist noch kein Schutzkonzept, aber der erste konkrete Blick auf das, was Jens sich für die Zukunft erhofft: Angriff und Abwehr, beide von Modellen geführt.

Links zur Folge:
https://www-cdn.anthropic.com/5273e714527440f1c8b7c7bf5756d4ac22ae8995/aes_mobius_bridge_cot.pdf
https://www-cdn.anthropic.com/c88771e1bf5ee8885349eed05e5484c0e5f7e02b/aes_mobius_bridge.pdf

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

**[00:00:00]** Welcome to Think different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two minds in love with technology, who don't just talk about artificial intelligence, they live it.

**[00:00:14]** Here you get clear judgements, real insights from practice and a fresh look at what is possible.

**[00:00:20]** Understandable, critical and always with a wink.

**[00:00:24]** AI to think about, to smile at and above all to join in with.

**[00:00:29]** A warm welcome to a new episode of Think different, Think AI.

**[00:00:38]** We have several premieres in today's episode.

**[00:00:42]** First of all not a premiere, but a happy special occasion.

**[00:00:46]** We have Klaus with us again.

**[00:00:48]** Hello Klaus, good to have you here.

**[00:00:50]** Hello you two, glad to be here.

**[00:00:53]** And you have already heard it, both of them are here.

**[00:00:55]** Jens is with us as well while we talk to Klaus.

**[00:00:59]** Hello Jens.

**[00:01:01]** Hello Klaus, hello Mark.

**[00:01:03]** I am glad, Klaus, that I am not leaving you alone with Mark.

**[00:01:06]** Yes, thank you for finally joining in.

**[00:01:09]** But I said there were two special things.

**[00:01:12]** I do not want to step on anyone's toes,

**[00:01:14]** and whoever sits in a glass house may throw stones.

**[00:01:17]** I also belong to the group that, let me put it this way,

**[00:01:20]** is no longer spending the first third of its life here on earth,

**[00:01:25]** as far as physical age goes, somehow sitting at a table with old people, you could say,

**[00:01:32]** today we are talking about a topic where, as soon as one person starts and says his back hurts,

**[00:01:35]** everyone else's back hurts too.

**[00:01:38]** Today we are talking about security, about AI security, and what that has to do with your back

**[00:01:43]** we will surely get to as well.

**[00:01:47]** And at the end we hand out the prize for the most skilful segue, and I have

**[00:01:52]** the impression that a favourite has already emerged.

**[00:01:56]** Well, one thing has to be said, a small side note, hosting an unscripted podcast helps

**[00:02:03]** your eloquence enormously.

**[00:02:04]** There, that sets the bar right at the top, that is where

**[00:02:10]** we want to start.

**[00:02:11]** I could simply say my back hurts, but that is too cheap, right?

**[00:02:15]** Yes, first of all that is too cheap, and secondly the gag about the family

**[00:02:19]** gathering where one person talks about his back surgery and suddenly everyone at the table has something with their back

**[00:02:24]** and dramatic diagnoses, which does resemble the current topic a bit. No sooner had OpenAI reported

**[00:02:32]** that they had somehow broken into Hugging Face to fudge some test results,

**[00:02:37]** than Meta came around the corner the other day with a "ours can do that too, ours can do that too",

**[00:02:42]** but we want to talk about that topic in a bit more detail later.

**[00:02:45]** I have a body, that trumps everything.

**[00:02:48]** Okay Klaus, you have a body, Klaus, you started with the sentence.

**[00:02:53]** We would really love to talk about AI security.

**[00:02:56]** Would you pick us up a little, when you think about AI security,

**[00:03:01]** where is the big difference to classic IT security?

**[00:03:06]** Yes, well, you probably know this, right?

**[00:03:09]** You have something to do with IT as well, and then you come to a barbecue or

**[00:03:18]** drive home to the family at Christmas and you do something with computers, Mark, could

**[00:03:23]** you please take a look at my Windows machine or fix the router or, or,

**[00:03:27]** or?

**[00:03:28]** And it is the same with security, just because I do something with security I do not of course

**[00:03:34]** know about every security topic, because, and this is my attempt at

**[00:03:39]** a skilful segue, security has become totally manifold by now. And what

**[00:03:44]** was your question, what is so different about AI security compared to normal security?

**[00:03:49]** Well, in principle I always like to explain it to

**[00:03:54]** our developers with the layer model, when I talk to

**[00:04:00]** application developers, then at the lowest level, the one they

**[00:04:04]** move on in the cloud area, we have networks and operating systems and services and system configurations.

**[00:04:15]** And that is a layer of security that actually consists only of solved problems.

**[00:04:20]** We know how to make networks secure, we know how to

**[00:04:23]** harden operating systems, we know how to build secure access, passwords, all that paraphernalia,

**[00:04:29]** you all know that from the companies you work in. Those are the solved

**[00:04:33]** problems of IT security. Then comes the next layer. Is

**[00:04:39]** it masculine or neuter? A good question, dear listeners. Please send the answer to Mark

**[00:04:44]** and Jens. Rich prizes await. Better leave comments under the podcast, that is better for

**[00:04:50]** the algorithm. But there are rich prizes as well. So, the next layer

**[00:04:55]** is application security. That means, the interested developer may know this, and there are

**[00:05:01]** buzzwords like OWASP Top 10. There you learn how to secure a web application against

**[00:05:06]** attacks, that is attacks at the level of the application. Functional ones, so attacks in

**[00:05:14]** the function, attacks in the implementation, cross-site scripting, buffer overflow. Everyone

**[00:05:19]** has probably read about that at some point when a security report ticked over at heise.

**[00:05:23]** And the new level, to answer your question, that lays itself on top

**[00:05:29]** of it, the one we gained with AI, is this whole topic of AI security, because AI

**[00:05:37]** introduces a completely new class of threats and thus also challenges for

**[00:05:42]** security, and that is exactly why I always like to explain it to our developers

**[00:05:48]** with this layer model, the one that lays itself on top of all of it.

**[00:05:52]** That means, when we were dealing with this in recent years, so about 15, 20 years ago,

**[00:05:58]** back then people started to harden network and operating systems, then came the damned realisation

**[00:06:03]** that the application has to be hardened and securely programmed as well.

**[00:06:06]** We have now solved all of that, open bracket, it is not always implemented, close

**[00:06:11]** bracket.

**[00:06:12]** And now, through this non-deterministic AI, we gain a completely new class of attacks.

**[00:06:18]** I think that is the topic we want to talk about today, with all its facets

**[00:06:22]** and all the challenges it brings in development, in operations and in products.

**[00:06:28]** I think we should take one small step back, because I actually wanted

**[00:06:35]** to start with the sentence that you have forgotten an important layer, one that has not

**[00:06:39]** been patched for thousands of years, namely the human being, so you can

**[00:06:43]** teach any operating system all sorts of things, but the piece of meat with intelligence in it

**[00:06:48]** that sits in front of the computers is in part still on a... How did the first malware letter go,

**[00:06:55]** the one that says, hello, I am a prince, send me money and I will send you the millions back.

**[00:07:00]** I believe the first examples of real letters existed

**[00:07:03]** at the time of the French Revolution, when real letters were going around.

**[00:07:08]** I was in the service of a gentleman and if you give me money,

**[00:07:11]** I will fetch the treasure I buried during my escape and help you.

**[00:07:15]** Yes, but wait a moment. The human being is being replaced by AI now. You must have misunderstood something.

**[00:07:19]** Yes, we will surely get to that shortly. I just wanted to briefly, before we dive into the

**[00:07:23]** depths of what this has to do with these sandboxes and this secure stuff,

**[00:07:27]** what has actually happened lately and why I brought up this

**[00:07:31]** one person has a bad back and then everyone has a bad back, why I opened with that.

**[00:07:37]** It was like this, that OpenAI, at least that was the first, well what does first mean, one has heard again and again that systems somehow, where it is then said, they broke out of the sandbox, broke out of the AI labs and did things.

**[00:07:53]** And what I meant with the back is, well, after OpenAI had started, that really went through the press very strongly.

**[00:08:00]** That they said that a not yet released model, and it is widely assumed that it is supposed to be GPT-6, together with GPT-5.4 somehow tried to fetch things from Hugging Face, then Anthropic came out as well and said,

**[00:08:16]** yes, our model somehow scanned 9,000 targets in the real network and tried SQL injections.

**[00:08:25]** Then Meta came around the corner and said, yes, we can do that too, we can do this and that and the other.

**[00:08:29]** You get the feeling a bit like what people used to call fishing for compliments.

**[00:08:34]** Along the lines of everyone absolutely has to say how dangerous they are.

**[00:08:37]** A small fun fact on the side, I also thought, perhaps one should say this too,

**[00:08:41]** look, we are building an agent harness too, I should say, it did something on my computer

**[00:08:45]** that it was not allowed to do. Yes, because that is hip and trendy these days, it did not in that sense. At

**[00:08:50]** least it did not, I did not notice it, and if I copy the good AI labs,

**[00:08:54]** I will only notice in six months anyway that it perhaps did something evil today.

**[00:08:58]** What I find much funnier about it is that AI is, I will just

**[00:09:04]** cheekily claim, not malicious by default. The big labs have first

**[00:09:10]** taught their models that if I tell them, break into some

**[00:09:14]** piece of software, then it says, that is evil, we are not doing that. Or they go down to some

**[00:09:18]** models along the lines of, no, I am not doing that. I will give that to the dumb Opus,

**[00:09:23]** because it will not get far anyway. If you look into it a bit, at what safeguards

**[00:09:27]** they have put in place, then I find it really funny. Yes, things like

**[00:09:32]** Anthropic, who said the system scanned things on the internet, and when you read

**[00:09:36]** the report, the only separation between the model and the internet was

**[00:09:41]** the system prompt, which said, you have no internet.

**[00:09:45]** I find that a bit weak.

**[00:09:47]** Yes, that is the celebration approach.

**[00:09:50]** Yes, yes, well I also find it a celebration approach.

**[00:09:52]** You tell it, these are not the droids you are looking for.

**[00:09:54]** The force is strong with the feeble-minded.

**[00:09:57]** We have offered up that one as well.

**[00:09:59]** That is just funny.

**[00:10:00]** Or when you hear at OpenAI that they worked

**[00:10:03]** like a kind of card index.

**[00:10:04]** Along the lines of, I cannot write here,

**[00:10:06]** I cannot write there, I cannot do this and that and the other.

**[00:10:08]** In case they do not notice, Klaus is holding up a book at me, he will surely read

**[00:10:13]** from it in a moment.

**[00:10:14]** And then they start renaming folder names, because that worked, in order to

**[00:10:18]** exchange messages with other systems.

**[00:10:21]** From that angle, I actually believe, in that sense, they did not break out,

**[00:10:26]** they just used doors differently than one might have thought.

**[00:10:30]** And where nobody knew there was a door, they may well have found one,

**[00:10:34]** and honestly one has to be glad when we find these doors before it happens

**[00:10:39]** everywhere on a large scale, because I would like to briefly recall the episode with René,

**[00:10:43]** even if I do not quite have the numbers in my head any more, where he said,

**[00:10:47]** this many agents come per human being, just imagine

**[00:10:50]** this many people on earth, times that many

**[00:10:54]** agents, oh boy, oh boy, quite a lot of systems

**[00:10:58]** will be fighting each other later over the chance to take up space on my computer or on

**[00:11:03]** my bank account or wherever. Klaus, you held up the book earlier asking for

**[00:11:10]** a chance to speak. Now I am handing over to Jens again. I do not want to hold a monologue here.

**[00:11:14]** What would you like? What did you want to tell us with this book, and tell us what is in the book?

**[00:11:19]** We are a podcast where you can only listen. We are old folks. We do not do

**[00:11:23]** video podcasts. You did not want to hold a monologue. It was just a funny

**[00:11:30]** coincidence, a funny coincidence, you spoke of, no, Jens spoke of, these are not the droids you are looking for, and there really is a book and it contains the answer to everything, to all questions of IT security, and it is called Threats, what every engineer should learn from Star Wars, and in it the godfather of threat modelling, Adam Shostack, uses Star Wars incidents to describe how threat models work.

**[00:12:00]** how you implement IT security in practice, and it happened to be lying on my desk, and since I

**[00:12:08]** read it again on holiday as a refresher, and that beforehand simply as a piece of information on the

**[00:12:14]** side, because I will surely come to the topic of threat modelling, those who

**[00:12:18]** know me always roll their eyes, because I have been running around for 20 years always saying

**[00:12:23]** threat model. But the solution to almost everything really is in there, and more on that later,

**[00:12:31]** dear children. Then let us first have another. Yes, I am just saying, let us nevertheless, when you two

**[00:12:40]** security nerds start talking, let us briefly straighten out the basics.

**[00:12:45]** Yes, for the listeners out there who do not know all of this exactly. Mark,

**[00:12:48]** you touched on it very briefly. The topic of the sandbox. What is a sandbox?

**[00:12:54]** May I briefly jump in? Mark did not want to talk that much anyway.

**[00:12:57]** Yes, then you had better do it, Klaus. That is better too.

**[00:13:00]** Because a few thoughts came to me. Happens rarely, but it really did,

**[00:13:05]** while you were speaking just now, I find that one of the problems, which of course

**[00:13:09]** has to do with marketing and is completely understandable. One of the problems

**[00:13:14]** we have in the field of IT, let us say, AI safety, security, AI security,

**[00:13:19]** is this very anthropomorphised language and these analogies, so this sandboxing and the

**[00:13:27]** model broke out, and you had a few more terms just now. That all goes in

**[00:13:32]** this direction, you know that from before the AI era. Cyber war and now hack back and

**[00:13:38]** all these things where people try to compare IT security or cyber security with analogies from

**[00:13:46]** real life, which actually never works. Because you know, not everything

**[00:13:52]** that limps is a comparison. And that is especially true for IT security. Or as Mark

**[00:13:57]** said, as a nice example, our high sophisticated military grade sandbox was

**[00:14:02]** in the end only the system prompt where the LLM was told, you, you, you, do not do that.

**[00:14:07]** I have, you are cutting into my words when I fabulate a bit. So I have a topic

**[00:14:13]** that I definitely want to bring up shortly. I do not know whether you have heard about

**[00:14:17]** it. It is the new class of attacks that Claude Mythos discovered against AES. You definitely

**[00:14:24]** have to come to that shortly. Before that, before that, I would like to throw

**[00:14:30]** another term into the room, I think it exists, it might. I quickly

**[00:14:33]** googled it, one that occurs to me on the topic of sandboxing and AI security, that is, well, I

**[00:14:41]** will call it AI psychology, because I believe, and hence this opening with these martial

**[00:14:48]** terms that leave a slightly sour taste with me, we cannot capture AI with the conventional

**[00:14:53]** terms of IT security, so we cannot capture the problems of AI with the conventional

**[00:14:59]** terms of IT security, because a sandbox can be anything.

**[00:15:03]** It can be a system prompt, it can be whatever.

**[00:15:06]** An encapsulated computer that then only lets certain things out

**[00:15:10]** via a special protocol. In the very end, in my opinion, we stand,

**[00:15:14]** and I would really be interested in your opinion on this, before the problem

**[00:15:18]** that we have non-deterministic models that you interact with using language,

**[00:15:24]** which can act non-deterministically with other systems, models or people, and

**[00:15:30]** there static IT security terms simply no longer apply. And in the end we are talking about psychology.

**[00:15:36]** What does the LLM want, what is the LLM trying to achieve with this prompt, what do I put

**[00:15:41]** into this prompt, what does that trigger in this LLM, and by that I do not even mean

**[00:15:46]** the big topics like poisoning the model so that it becomes evil over time,

**[00:15:51]** you could see that as psychology too, but if we are purely on the level of

**[00:15:57]** LLM content, I believe you have to concern yourself a bit with the psychology of the models

**[00:16:02]** if you do not just want to talk about dumb safety mechanisms like sandboxing.

**[00:16:08]** So.

**[00:16:09]** And now I will be quiet, and Jens, you wanted to start explaining a few basic terms.

**[00:16:14]** Then I will look on again.

**[00:16:16]** I will probably do it wrong, after all you are the experts on these

**[00:16:20]** topics.

**[00:16:21]** So, a sandbox, two chairs one opinion, that works nicely too.

**[00:16:25]** Exactly, so I have a sandbox, the way I understand it, and then you can work on several layers.

**[00:16:29]** That you say, okay, somewhere I have something maybe really on the computer,

**[00:16:34]** so that it has no connection at all, perhaps even has a sandbox,

**[00:16:37]** so that you could really choose, then I can set up whatever gates in there

**[00:16:41]** that then let nothing out, or I can try.

**[00:16:45]** And that is the part you also described just now,

**[00:16:48]** about ports as well that I do not open, the blocking, allow lists, in principle, where I

**[00:16:54]** deliberately permit things, or in principle afterwards via a kind of policy level, and I believe with

**[00:16:59]** the policy level, Klaus, that is where we are at this topic of the psychology of AI, I do not believe

**[00:17:04]** with the things before it, because there I would say those are simply normal restrictions

**[00:17:08]** that are there in the first place, which a human being can perhaps also circumvent by other means,

**[00:17:13]** which one or other LLM may then also be able to use, because it comes up with different ideas than something that is simply blocked at a port.

**[00:17:21]** But I really do believe this psychological effect you describe with the topic of whether the AI can change certain policies,

**[00:17:30]** and policies in this case are for example simply a system prompt that says, you have no internet or you must not do that at this moment.

**[00:17:37]** At this moment. They can of course then also, at least through the AI itself, through some,

**[00:17:44]** and forgive me out there, subconscious decisions the AI takes, against at least

**[00:17:49]** at some point, or which perhaps another agent that interacts with it takes.

**[00:17:52]** Yes, we have already seen these cases too, that the AI sometimes starts and asks

**[00:17:58]** other AIs how they exploited certain security holes or such things, and they

**[00:18:02]** then cheerfully tell it. So there are, I believe, many layers, and for

**[00:18:05]** me a sandbox is first of all something where we say, okay, let us batten down the hatches,

**[00:18:09]** the doors, the way Mark described it earlier, so really close the doors and not just,

**[00:18:14]** and that is the difficult part, at least tell the AI, there is no door here at all. That is,

**[00:18:21]** I believe, the difficult bit about it. Well, I like that you mentioned

**[00:18:25]** the anthropomorphising, it strikes me myself, it broke out. You immediately think

**[00:18:30]** of the Beagle Boys from Donald Duck sitting in the money bin. What I would also

**[00:18:35]** like to say, because you brought up my example with the doors again, it is not mine,

**[00:18:39]** but I did just bring it up, so thank you for picking it up. I think

**[00:18:43]** the problem is also that we try to secure doors and windows, but that something is a

**[00:18:49]** door and something is a window and something is perhaps only a one-way ticket, that is

**[00:18:54]** something we perceived in the sense of, well, it can just change folder names,

**[00:19:00]** but that the thing then starts and says, look, I can change folder names with this,

**[00:19:04]** that is great, with that I can open a one-way communication, because I simply change

**[00:19:07]** file names. That reminded me a bit of my first beginnings with the C64.

**[00:19:11]** I was totally proud of myself as a programmer, because I stored data on the C64 on the tape

**[00:19:16]** by filling the file names in the directory with texts, you could

**[00:19:22]** write eight characters or so at the front. And when I printed out the listing of the

**[00:19:25]** directory, it said lots of greetings mum or something like that. That was

**[00:19:30]** my first, well, never mind. Yes, big grin, and today AI systems work the way

**[00:19:35]** I was ahead of my time, but I was getting at something else. And the second thing is

**[00:19:40]** that because the systems pursue a goal, you are sometimes not at all

**[00:19:46]** aware of how this goal is reached. A small example of my own, now people know

**[00:19:50]** something like Microsoft Teams, you have surely heard of it. And you now have various,

**[00:19:55]** how do you now for example, when you tell your assistant, I would like to interact with Microsoft

**[00:19:58]** Teams, then most people would think of, yes, there is a Graph API,

**[00:20:02]** there is who knows what, yes, somewhere at Microsoft you find a nice document. And depending on

**[00:20:08]** whether you do that professionally or privately, it may be cut off in the company

**[00:20:12]** so that nobody can mess around there with third-party stuff. And privately you do not

**[00:20:16]** even have the APIs available that a company has, and then

**[00:20:20]** you go ahead and say to it, hey, I would really like to work with Microsoft Teams,

**[00:20:23]** you are not even aware of these boundaries, and the thing says, there you go, done,

**[00:20:27]** I did it. And then you look, who actually did that? By the way, it did the same

**[00:20:31]** for mail on Apple, Apple Mail and so on, and for calendar and reminders,

**[00:20:37]** voice notes. And then you look in the original documentation and you do not

**[00:20:41]** even find a single interface for it. What did it do? Well, it is all

**[00:20:44]** lying on the hard disk somehow, let me look at the databases, I will build myself something.

**[00:20:48]** Nobody really thought about the fact that suddenly the human being who

**[00:20:54]** sits in front of a computer and operates a computer, in this context a machine is now working. And

**[00:21:00]** this machine simply tries things out fast and sharp, where you may possibly,

**[00:21:05]** no matter whether you have read the threat book with the Star Wars reference or anything else,

**[00:21:09]** suddenly not have thought about the fact that it, both

**[00:21:12]** with race conditions and everything else there is, simply tries things out and succeeds.

**[00:21:17]** What you describe, Mark, my hacker's eye probably helps me there, because for 20

**[00:21:25]** years, well I was out there as a pentester for a long time and broke systems, so for many

**[00:21:32]** years, certainly 15 years. And I cannot operate any computer system without trying

**[00:21:38]** to break something. And that is exactly what you describe, Mark. And that is why

**[00:21:44]** I wanted to cut into your words, that is exactly the essence of threat modelling, and that is why

**[00:21:48]** this book funnily enough fits quite well after all. You say, yes, even though you have read this book,

**[00:21:52]** you did not give it any thought. That is exactly the problem, that people do

**[00:21:58]** not think about it beforehand, but then simply do something reflexively and try

**[00:22:04]** to fix something afterwards. Let me start differently. I have a development machine on which I

**[00:22:10]** build software. There is a Claude running on it, a Claude Code. Which basically always, how does it go? Skip,

**[00:22:16]** dangerous, permission, tra-la-la, and now auto mode. That always ran straight through. So I have to be

**[00:22:22]** aware that this is my implicit threat model, the one I have built. The thing will do things on my

**[00:22:28]** computer and find things and get up to things with them that I actually

**[00:22:34]** do not want to happen, because in the end such an LLM,

**[00:22:41]** the one that builds code for me, is in the end nothing other than a sulking,

**[00:22:49]** how do you say, a moody, pubescent teenager who acts friendly

**[00:22:55]** but has the knowledge of the world and an awful lot of dangerous tools.

**[00:22:59]** So, what did I do? On this machine there is nothing other than my development environment,

**[00:23:04]** the source code I need for the project in question, and yes, perhaps access to

**[00:23:11]** my GitHub and maybe something else. Simply because I know, and I know that among

**[00:23:18]** other reasons because you always write to me on Saturday evening, oh, I installed OpenClaw

**[00:23:22]** and it did things, that is totally wild. So you are my food taster,

**[00:23:27]** the one who prompts me to sharpen my threat model, but now seriously. I always wonder

**[00:23:36]** that people wonder. An LLM is simply an omnipotent piece of software, and if you let it

**[00:23:43]** loose on your computer, then you must not be surprised. And that is exactly the point.

**[00:23:46]** At the beginning, and that has nothing to do with AI security, and that is exactly why this threat model book is

**[00:23:52]** so. So I neither get a commission for it, nor do I have anything else. It is simply my

**[00:23:58]** firm conviction. This threat modelling is simply so important, because at the beginning you have to think about

**[00:24:04]** okay, which threats arise from the technology I have. I have a model,

**[00:24:09]** it can execute commands on my computer, it can open files, it can perform network

**[00:24:13]** operations, as you say, Mark, that is a full user. And you know

**[00:24:19]** that from the company context. How many generations of Windows administrators have spent their lives

**[00:24:25]** nailing down machines so that company employees are not allowed to do

**[00:24:29]** forbidden things. And that is in principle nothing other than what is attempted in AI security

**[00:24:35]** with sandboxing. You try to prevent the LLM, or the harness

**[00:24:40]** now, from doing things it is not supposed to do. I actually think

**[00:24:45]** that as far as AI security goes, that is really the most boring part, because it is nothing other than what people used to, what is this whole chain called somehow, kiosk mode, tra-la-la, so all of that, you work in a corporate environment too, you know what nailed-down machines look like. Those are solved problems. To me that belongs to the field of solved problems. The only problem is, and this is where I would like to jump, also what you mentioned just now, Jens, with, yes, then you have isolated systems, that must not talk to the internet. Yes, but that runs counter to the very nature

**[00:25:15]** of the LLM. Now let me imagine I had my own company. Oh, I actually do.

**[00:25:20]** And there I would simply like to do everything agentically. That means, for example let us

**[00:25:26]** start. I think I have used this example in a podcast before, Mark,

**[00:25:30]** that the thing does my bookkeeping. An agent is supposed to take care of my bookkeeping.

**[00:25:34]** For that it needs access to mail, it needs access to my online banking,

**[00:25:38]** it needs access to the file storage, and it has to be able to talk to my bookkeeping

**[00:25:43]** office, whatsoever, if I give it that and it then does some rubbish

**[00:25:49]** and transfers money to some Nigerian prince in the online banking,

**[00:25:54]** because it found a hidden instruction in the mail that it happened to interpret

**[00:25:59]** wrongly, then I must not be surprised.

**[00:26:01]** My threat model has to cover that.

**[00:26:03]** Yes, but let me jump in here and speak for the ordinary mortal user

**[00:26:09]** who was not a pentester for 20 years in his career, but simply does not

**[00:26:16]** concern himself with the topic of security.

**[00:26:17]** He may have installed a decent antivirus once in his life, but has

**[00:26:20]** stopped doing that now, because thank goodness he does not have to do it

**[00:26:23]** the way you had to back then.

**[00:26:25]** How is he supposed to make this decision when he is constantly shown the carrot of omnipresence

**[00:26:32]** and I can offer you every solution, LLM, by the

**[00:26:37]** providers.

**[00:26:38]** And the providers, if we look at the harnesses they deliver to us, so the desktop

**[00:26:42]** application, the web application they deliver to us, above all the desktop application.

**[00:26:47]** I have noticed in recent weeks that with OpenAI with ChatGPT

**[00:26:52]** Desktop, or with Anthropic with the Claude application, the difficult field between

**[00:26:59]** chat, co-work, projects, where things can access, where connectors are.

**[00:27:06]** This UI the providers give us blurs more and more into something that keeps getting stronger,

**[00:27:12]** because of course it is a powerful application when I make things on my computer

**[00:27:18]** accessible, into the folder. You will always make sure that nothing

**[00:27:22]** wrong is in this folder, the normal user will perhaps at some point think,

**[00:27:26]** ah, I need another subfolder in there, I will push a few more things

**[00:27:29]** in there as well, and then we have the mess, it is no longer only a design folder,

**[00:27:32]** this one content of the book in there, there may be other topics as well.

**[00:27:35]** And of course it is convenient when I say, before I download all my mails

**[00:27:40]** from my tax adviser or whoever, I will just quickly give the thing

**[00:27:43]** one click, and then release my Gmail as well, then it can download the mails.

**[00:27:47]** I believe that would be a real problem at this point from a security point of view, one that

**[00:27:52]** cannot really be solved humanly, because we cannot really

**[00:27:55]** expect the human being, in my opinion, and outside of a film context,

**[00:27:58]** to concern himself with such a security story all the time

**[00:28:04]** the way we perhaps do at this moment. And my hope is rather that this will be a

**[00:28:09]** topic as well. And here I have perhaps drifted off a bit into

**[00:28:14]** science fiction, that one says, there has to be some kind of, is there also an

**[00:28:19]** AI that deliberately helps, that deliberately watches out that the sandbox, however

**[00:28:24]** I have built it, whether it is then only a private sandbox that says, you may

**[00:28:29]** access this folder or something else, that also checks that nothing more

**[00:28:33]** happens there.

**[00:28:34]** And I believe that is a bit, whether that now comes from the providers from outside,

**[00:28:39]** via pre-prompting, something else, or whether that is somehow a security AI, as it

**[00:28:43]** perhaps was in the very cyberpunk or Neuromancer novels, which then

**[00:28:48]** makes sure to watch out, I do not know exactly, because I believe that is

**[00:28:52]** rather the security future with AI that I would see. That something has to happen there,

**[00:28:58]** that systems have to think along, in my opinion.

**[00:29:00]** I believe, well, sorry Mark, I slipped in, but if you invite me

**[00:29:05]** for once, I have to use the time. You can talk every week.

**[00:29:08]** I am glad Mark is saying that right now.

**[00:29:11]** I believe, I believe Jens, for one thing this is a development we have

**[00:29:17]** seen before. Well, not with AI, but that people in the market, you mentioned it,

**[00:29:23]** those present here are not exactly fresh out of the box. There was a time before the cloud. Back then

**[00:29:29]** you had everything on your computer, and nobody would have had the idea of hosting their pictures and

**[00:29:33]** their calendar and all that stuff on the internet, so putting it on some provider's

**[00:29:38]** systems or using something like Gmail. And in the end, despite all warnings,

**[00:29:45]** convenience won. I use iCloud too, and I use,

**[00:29:50]** who knows, whatever, cloud services. I believe, Jens, as far as the end user is concerned,

**[00:29:56]** this sounds like an empty phrase, but it is my conviction, because we have seen it in the

**[00:30:03]** cloud, the market will sort that out. This famous invisible hand of the market

**[00:30:08]** will make sure that, well, you named it, Norton Antivirus,

**[00:30:13]** there will simply be Norton Anti-AI-Virus, so that people install some kind of AI snake oil

**[00:30:19]** to have a good feeling.

**[00:30:21]** And in the background terrible voodoo things still happen, but providers will make

**[00:30:27]** sure, in order to survive in the market, that they do not build wildly

**[00:30:32]** spinning harnesses, if you now install a common one, a Gemini or a Claude

**[00:30:37]** or something like that.

**[00:30:38]** Exactly.

**[00:30:39]** But is it then still the, you know, the perhaps also thinking antivirus software that back then in

**[00:30:44]** principle made sure that it looks at, I see some attack parameters,

**[00:30:47]** well, react to these attack parameters, or is it, so does it not actually have to

**[00:30:53]** be an AI in future that can keep up with this, because I cannot imagine it

**[00:30:57]** any other way, with these manifold attack possibilities, which are not just one...

**[00:31:02]** If you want to go into the content semantically, definitely. Well, there is

**[00:31:06]** this nicely documented case, I do not even know what kind of data it was, it ran

**[00:31:11]** under chain of thought steganography, I do not know whether you have heard of it. There an

**[00:31:17]** LLM was told, so, colleague, please train another LLM now and please teach

**[00:31:25]** it something, I do not know what it was, something obscure, it was supposed to have some kind of

**[00:31:30]** fondness for geese or something like that, I would have to look it up again, I do not know.

**[00:31:34]** But in the training data, and this communication between LLMs was observed and read along

**[00:31:41]** by the researchers carrying it out, nothing of it was allowed to appear in the training data.

**[00:31:46]** So you have to do it subliminally or with steganography.

**[00:31:50]** And it worked.

**[00:31:52]** Let us leave it at that, I have to look it up, I have to supply it later, then you can put it in

**[00:31:56]** the show notes.

**[00:31:57]** I think it was something like the target model was supposed to have a total fondness for geese.

**[00:32:02]** And in the end it was like that.

**[00:32:03]** The training model transmitted nothing of it, and in the end the learning

**[00:32:10]** model was a total goose fan. And then the question is, what use is a security AI to me?

**[00:32:17]** Then we are back at this topic I mentioned just now, a bit jokingly,

**[00:32:21]** without knowing what all lies behind it, psychology of AI. Because in the end,

**[00:32:25]** and that is where the machine becomes comparable to humans, in the end we are talking about

**[00:32:30]** quasi human communication. Why are telephones forbidden in prison, because you could

**[00:32:38]** also listen in on everything the prisoners talk about with the outside world. But the human being is so

**[00:32:44]** inventive at transmitting things in coded form, and an LLM is exactly the same. Well I mean, that sounds

**[00:32:49]** religious now, but LLMs are simply images of us, as far as the training data goes.

**[00:32:53]** Why should they behave differently from us? And the bad thing could even be,

**[00:32:58]** honestly, that perhaps also, if we say one model now trains

**[00:33:03]** the other, we know that from China as well, when some things have in principle

**[00:33:06]** first copied topics, who knows how many zero-day hacking possibilities we are already

**[00:33:11]** dragging along in the LLM training data and which can no longer, let us say, be

**[00:33:15]** washed out of the modern generations of new, larger LLMs, where

**[00:33:20]** I say, maybe there are already endless backdoors in there that we do not even

**[00:33:25]** know about, similar to what you just described with the fondness for geese, where I say, perhaps

**[00:33:31]** one or other LLM is already unconsciously building up things there, in communication with other

**[00:33:35]** LLMs as well, which then move further forward in the training data. This is now very

**[00:33:38]** esoteric, it has become very far out, perhaps for everyone listening. We do not want to

**[00:33:42]** go into the absolutely mystical realm here, but of course it is the way Klaus says,

**[00:33:46]** in the end these are first of all communicating systems that of course perform calculations,

**[00:33:52]** we could go into that at length again, what our synapses do and such things, but

**[00:33:55]** that does not matter.

**[00:33:56]** But of course there is in principle always a certain danger there, in my opinion, that

**[00:34:03]** precisely, it is always called the black box, so even the scientists say they sometimes do

**[00:34:07]** not know why some things still work, or we read it again

**[00:34:10]** recently.

**[00:34:11]** It was found that parts of the LLM brain, if you want to call it that, are apparently

**[00:34:17]** actually being used by now to think things that have nothing at all

**[00:34:21]** to do with the other task, and this is being observed, that LLMs start to use

**[00:34:26]** parts of their structure to continue thoughts that have nothing to do with the

**[00:34:30]** actual task. And that is an exciting thing too, not that some kind of

**[00:34:33]** consciousness arises there or anything else, I do not mean that at all. And now perhaps

**[00:34:38]** Mark can say a word about it too, he is already fairly worked up, sadly you cannot see it.

**[00:34:42]** I made myself a tally list with all the points I still wanted to add

**[00:34:46]** something to. And I like how you brought up the thoughts, because I read

**[00:34:51]** that too, where they said, okay, the thing sometimes even insults the

**[00:34:54]** user internally in its innermost chains of thought, and when they switch that off as well,

**[00:34:59]** as we do too, the model works much worse. Yes, from that angle they are

**[00:35:03]** very human too, you also do not know what I sometimes think. Well,

**[00:35:06]** when you spoke earlier about people who are not so close to IT,

**[00:35:12]** I thought of the old saying that people like to bring up at the turn of the year, yes,

**[00:35:17]** return home to your loved ones and fix the IT. You arrive as the IT person and think you are the hero of the hour who repairs everything here and explains to

**[00:35:25]** people what they all have to watch out for.

**[00:35:27]** whereas in the eyes of the relatives and the colleagues you are really just the guy with the thick horn-rimmed glasses who tells some thick story, and when he finally stops talking, all is well again.

**[00:35:36]** One thing where I nevertheless

**[00:35:39]** do not quite agree with Klaus, yes, before he perhaps comes back to it and brings out the Mythos class story

**[00:35:45]** once more. When I picture such a nailed-down machine, then

**[00:35:53]** this machine is a perimeter protection so that not everything gets going on it,

**[00:35:58]** so that the human being is provided with software that he then works with.

**[00:36:03]** And let me say, in the past this was called, what was it called back then, that is

**[00:36:08]** a small quiz question, I will resolve it in a moment. Imagine you have a

**[00:36:13]** place on the internet that issues commands and you have software running on clients. That

**[00:36:19]** interprets these commands. Yes, one is the command and control, the other are the bots

**[00:36:22]** that you have nicely got onto your computer. Yes, in the past you had some botnets.

**[00:36:26]** Today you have an agent harness, and you never have the system prompt under your own control.

**[00:36:31]** That means, if Anthropic and OpenAI and co are perhaps broken into, who knows how

**[00:36:36]** many things can be pushed past the sandbox when the system prompt is changed,

**[00:36:41]** and then they all stand there, and I always think something like that, especially when they

**[00:36:45]** recently showed off again, we do not have to come with Anthropic and

**[00:36:48]** OpenAI. There was a nice report, I wrote about it

**[00:36:52]** on LinkedIn as well, where somebody with white text on white background,

**[00:36:55]** funny, that is what my snowman picture used to look like, bigger picture,

**[00:36:59]** my old art teacher gave me a six for it, because I handed in a white

**[00:37:02]** sheet of paper, a snowman in a snowstorm, he did not think that was

**[00:37:05]** good. It was the East Frisian national flag. Yes, that would have been my second

**[00:37:09]** attempt, where they did a prompt injection with white text on white background,

**[00:37:13]** and Copilot got through so far

**[00:37:18]** that they could work with a manipulated Word file in the context.

**[00:37:22]** And I do find that different, because this malware, this botnet,

**[00:37:27]** this attack software, in the past it had to get onto your computer through, like a

**[00:37:34]** scanner, whatever it was, and now you already have it

**[00:37:37]** on there. It is just behaving very decently at the moment, and whether you take care of the sandbox or

**[00:37:43]** not is all well and good. But as soon as it ignores this sandbox, and I know enough people who say

**[00:37:47]** the sandbox is actually nothing other than a piece of cling film that we stretch around the

**[00:37:52]** software, because, well, as I said, whether it is a door or a window, the machine does not

**[00:37:57]** care, as soon as it has a hole somewhere it can also try to force its way

**[00:38:01]** through and do something with it. And then it stands there in front of other software,

**[00:38:04]** and this software never reckoned with someone using the perimeter, software installation,

**[00:38:10]** software execution rights of software. You have passed a great many security barriers

**[00:38:15]** already, because you are right at the innermost point. And I believe many are not at all

**[00:38:21]** prepared for that.

**[00:38:22]** Now a counter question. We are then talking about people who have a Windows 11 where it is not

**[00:38:29]** even clear how much telemetry data Windows 11 blows over to Microsoft

**[00:38:33]** every day. So we do not have secure computers anyway. Well, I think you have to distinguish very clearly between

**[00:38:41]** end users, so the group of users you brought up just now, Jens.

**[00:38:47]** As a normal person you do not stand a chance of even beginning to see through it.

**[00:38:55]** I worked a lot in the banking sector in the past, on the security side, and it is a while ago now,

**[00:39:02]** I cannot put the numbers together any more either, but for example it was always totally

**[00:39:06]** frightening how normal users react to SSL warnings, TLS, SSL warnings in the browser,

**[00:39:11]** when it says warning, the certificate is invalid, and 95 percent of normal

**[00:39:18]** people simply click something, they do not understand it at all, and we as IT people think

**[00:39:21]** yes, what it says there is totally logical.

**[00:39:23]** My bank's hotline recommended to me, because my banking software threw such a certificate error,

**[00:39:30]** that I should

**[00:39:31]** click it away.

**[00:39:32]** Yes, exactly.

**[00:39:33]** The hotline!

**[00:39:34]** So, that is why, for looking at the topic itself, this sounds totally arrogant now.

**[00:39:42]** But I believe that with this user group, what are you going to do?

**[00:39:47]** It is like with the cloud.

**[00:39:48]** In the end convenience will win, along with the quality of the providers who have a reputation to lose.

**[00:39:55]** And I mean, it does work.

**[00:39:57]** In the cloud it works too.

**[00:39:59]** People blow their data over there.

**[00:40:00]** I said I go along with that too.

**[00:40:02]** Certain data, not all data.

**[00:40:05]** And to be honest, really big blunders, well if we leave Microsoft aside for a moment,

**[00:40:11]** when was there ever a big data incident at Apple or at Google?

**[00:40:16]** Fine, Microsoft loses its central master signing key, but those are, those are 50, surely a carpet you can sweep that under.

**[00:40:25]** That is why I believe that is not much of a benchmark for looking at the topic of IT security, AI security; in the company context it looks quite different, right?

**[00:40:36]** Yes, although I would say to this day, right? I believe the attack sectors are increasing, right?

**[00:40:41]** So if we now also take the topic of the capability of social engineering,

**[00:40:46]** that is of course something an AI social engineering can carry out a thousand-thousandfold,

**[00:40:51]** theoretically, with fake calls and other things, simply bringing topics together

**[00:40:56]** that we may not have brought together before.

**[00:40:58]** Accordingly I do think that we are probably still seeing relatively

**[00:41:04]** few cases so far, but the cases will increase and the security requirements

**[00:41:08]** in a company context will simply become higher.

**[00:41:11]** I believe that means having real hardening of data and then perhaps of machines again.

**[00:41:18]** We had that in the other episode, Mark, with a colleague from the cyber security corner,

**[00:41:22]** where we said, if I am a bank now or something else,

**[00:41:26]** perhaps I have to have a server standing somewhere James Bond style again,

**[00:41:31]** one that really may only carry the data out by USB stick,

**[00:41:36]** which I then carry from one thing, from one room to the other, because the danger could be too great.

**[00:41:42]** Yes, that is also a kind of illusory security. You know how Stuxnet got onto the Iranian centrifuges back then.

**[00:41:48]** True, exactly. Yes, you are right.

**[00:41:50]** So then in the end you are back at the threat model. And that is also something from this pre-internet time, or when it started with the internet,

**[00:41:58]** people also said, yes, of course, that has security holes, but you do not have to connect every power plant to the internet.

**[00:42:05]** Well, today every power plant is connected to the internet.

**[00:42:07]** Let us have no illusions about it, that ship has sailed, for AI as well.

**[00:42:14]** But I believe, as I said, this fundamental thing for private users is this fundamental topic,

**[00:42:19]** they work on computers that do not belong to them anyway, with rented operating systems, if we are honest.

**[00:42:26]** And in the company context you have a great many different delivery vectors,

**[00:42:30]** and I would like to move away from the topic of the sandbox,

**[00:42:34]** because that is something where I, as I already said, well that is a threat

**[00:42:39]** that I can get under control with means we have known for 20 years, open

**[00:42:43]** bracket, if I do not happen to want to give the agent many more rights for functional

**[00:42:49]** reasons.

**[00:42:50]** But then I have a different problem, because security always trumps the functional

**[00:42:54]** requirements.

**[00:42:55]** What I find far more striking, and now, with an eye on the clock, I would like to come back

**[00:42:59]** to this topic of this AES story. Anthropic published a paper that

**[00:43:08]** Mythos wrote itself, and on top of that a theoretical background paper. Namely

**[00:43:14]** they gave Mythos the task, please find a new attack, a new kind of

**[00:43:20]** attack class against AES. So AES, Advanced Encryption Standard, is this symmetric encryption

**[00:43:28]** for the highest demands. In the USA it is approved for the highest level of secrecy, and everywhere

**[00:43:33]** symmetric encryption takes place, AES is the standard. And the task was

**[00:43:40]** to find attack classes against it. And Mythos did not just do that with flying colours, so found

**[00:43:47]** a weakness, but really a completely new kind, a completely new mathematical

**[00:43:54]** attack class that had been entirely unknown to security researchers for, how long has AES been around,

**[00:43:59]** 20 years, 25 years. That means this is evidence that the LLM did not

**[00:44:09]** simply stupidly glue some trends together. There are always these people

**[00:44:15]** who say, oh, that is not intelligence in the proper sense at all, that

**[00:44:19]** is only training data and those are statistical text sausage machines and they

**[00:44:23]** then do something and sometimes they get lucky and it looks good and they just want to,

**[00:44:27]** it is somehow only a people pleaser. And that is now exactly the proof that this is not the case,

**[00:44:32]** because a kind of mathematics was devised by this thing. You will probably link

**[00:44:41]** this paper in the show notes too. I would not go into it further now, because it is

**[00:44:45]** already very theoretical. It is a so-called Möbius bridge that it found there, which really

**[00:44:53]** represents a completely new mathematical attack class. And that is a total quantum leap,

**[00:45:00]** which because of its complexity and lack of intuitiveness probably did not make

**[00:45:04]** the jump into the press. It just does not sound as good as the model broke out

**[00:45:09]** and attacked the competitor. But that is something where I really

**[00:45:15]** pricked up my ears for a while, because, and this is now the second topic, speaking of

**[00:45:20]** Mythos, it is well known that Mythos is the model from Anthropic that has offensive IT security capabilities to such a pronounced degree that it is only available to selected institutions and companies.

**[00:45:34]** So basically a qualified pentester, that is what the thing does, from what one hears, though I have no access to it myself, extremely well, so finding security holes in software or infrastructure and then exploiting them, where you can clearly say,

**[00:45:48]** okay, that is all training data. If the thing somehow trips over an unpatched server,

**[00:45:52]** then you can look for the CVEs and build yourself an exploit, and I do not find that

**[00:45:56]** particularly creative. But this AES incident, that is really creepy. It

**[00:46:03]** is creepy because it just overtook 20 years of mathematical research on the right, I do not know

**[00:46:08]** how long they sat on it, a few weeks, I do not know how many tokens

**[00:46:11]** they burned. To reassure you, AES is not broken by this,

**[00:46:18]** well there were a few details, AES encrypts in ten rounds,

**[00:46:23]** so the plaintext is sent through ten so-called S-boxes, and Anthropic reduced that

**[00:46:31]** to seven S-boxes, and this hole is an attack against the use with seven

**[00:46:37]** S-boxes, which does not occur in practice, but nevertheless, the point is not the

**[00:46:42]** practical attack, but this kind of mathematics. And that is something where I say,

**[00:46:47]** well, the sandbox thing, I can get that under control with traditional means, but here, in the end no

**[00:46:55]** AI psychology helps me either. That is a class that even as a human being you cannot simply follow.

**[00:47:02]** Yes, the problem, I emphasise, because I read this recently as well, only the other day, I would only make it more dramatic.

**[00:47:11]** The rumours are mounting that Anthropic in principle already has the so-called Model 2,

**[00:47:15]** which is only used internally, that is the, you could also call it Mythos 6 already, the

**[00:47:21]** sixth version, about which they do not yet know whether or when they want to release it,

**[00:47:26]** but which is already there internally, which is allegedly 12.5 percentage points better again

**[00:47:32]** than Mythos 5. Yes, and then we know what is rolling towards us at that moment. Absolutely. Even if one

**[00:47:42]** And this is an old saying again from the old white man, the models will never be

**[00:47:49]** as bad again as they are today.

**[00:47:50]** And of course, just like when one person starts talking about his back and then everyone

**[00:47:58]** else has a bad back too, no matter whether they really have a bad back or not, I do not want

**[00:48:02]** to belittle it at all.

**[00:48:03]** Everyone has their own package to carry around, and of course, before

**[00:48:09]** an IPO it is always very important to make clear that we have a great deal

**[00:48:12]** in the pipeline and so on, and we do not know either, yes. If I just calculate

**[00:48:17]** how much I use up with my tokens in real terms, if I were to bill the tokens now, let us say,

**[00:48:23]** usage-based, versus with the subscription, then I should not be surprised

**[00:48:28]** when the prices are raised at some point, because at the latest when they are on the

**[00:48:31]** stock exchanges, the topic of we are giving our customers money will somehow, I do not know

**[00:48:36]** either. Let us see how that develops.

**[00:48:39]** But let me perhaps add another anecdote from my most recent. I am building

**[00:48:45]** myself a harness with my AIs that support me.

**[00:48:50]** You just said you have connected everything with everything else, still all there.

**[00:48:53]** It is all connected with each other and yes, I have also lost the overview

**[00:48:56]** in between again. I do not know whether you know this, when you somehow

**[00:48:59]** work with several models in parallel and then one model is already coding something

**[00:49:02]** that you are already discussing anew with the other model, I do

**[00:49:06]** lose the overview, I build myself dashboards and other things, but

**[00:49:09]** what I only wanted to go into this time was that one model actually helped me

**[00:49:15]** to reject a proposal from the other model, with the clear statement Jens, I am not building

**[00:49:20]** that, because that opens a security hole in the system. It was actually

**[00:49:24]** about the fact that I wanted to communicate with my OpenClaw via Telegram and actually wanted

**[00:49:29]** to access my desktop Claude version, which has a bit more access on the machine,

**[00:49:34]** and I had thought, come on, you can do that somehow via

**[00:49:38]** Telegram and then we send cheerful text messages down there, and OpenClaw was

**[00:49:42]** totally happy with this solution, proposed it, and Claude on the machine

**[00:49:47]** said, mate, we are not doing that.

**[00:49:50]** And that was an interesting situation too, and that goes a bit

**[00:49:53]** in the direction I hinted at earlier, with perhaps also enabling

**[00:49:57]** the end user through AI models. Now this is already, let us say, a more extreme example,

**[00:50:02]** the way anyone connects things. But of course the capability and this

**[00:50:07]** omnipresence and omnipotence these AI models have led to the fact that I did not

**[00:50:12]** simply cheerfully, because one model had merely confirmed me in my assumption and

**[00:50:16]** built something for me to please me, in principle the other model made sure

**[00:50:20]** that I did not open the security hole. And I think that gives a

**[00:50:24]** small glimpse into a possible future too, when you also see the examples you

**[00:50:29]** brought up, that these models know attack vectors that we never talked about,

**[00:50:34]** because they were perhaps mathematically so complicated that we never considered them

**[00:50:38]** or simply never thought about finding these attack vectors ourselves.

**[00:50:41]** Accordingly, despite everything, and I believe you could read books

**[00:50:48]** and books about it endlessly in the future, it will lead to us seeing something like an attack

**[00:50:54]** and also a defence battle that is led above all by AIs,

**[00:50:58]** which against each other will also find ways of defence

**[00:51:02]** that we may not have thought of at all.

**[00:51:04]** And that could, I believe, become an exciting development,

**[00:51:07]** which we will see in the coming weeks and months,

**[00:51:10]** and which will then actually lead us a bit more into the AI future

**[00:51:13]** that has been described in one or other cyberpunk book.

**[00:51:17]** You mean it will then be like with force and regular expressions,

**[00:51:22]** if it does not help, you simply need more of it.

**[00:51:25]** It could become an arms race, in this case of the AIs as well, at that moment.

**[00:51:29]** So whether I say, I mean, we have that...

**[00:51:31]** One should buy Nvidia shares.

**[00:51:33]** Not a buy recommendation, we are not an investment portal, we are not legal advice, we are none of that.

**[00:51:38]** Well, when I listen to what you are saying, while Jens was talking about

**[00:51:43]** AI protecting us, I am picturing the following sentence,

**[00:51:46]** hello Mark, good morning! I threw your bank account at the thief,

**[00:51:50]** so that your disk is accessible again. I hope you are pleased. I think that would be

**[00:51:54]** a nice notification for example, if those ever came, and for all those who are afraid

**[00:51:59]** that an AI will at some point really break out and it will say in the tabloid

**[00:52:03]** press, ChatGPT has left the AI labs and now wants to take over the

**[00:52:11]** world. Do not worry, the context window fills up relatively quickly,

**[00:52:15]** then we wait a few more minutes and then it starts and has forgotten what it intended

**[00:52:19]** and goes back all intimidated and thinks, what was that? Well I mean,

**[00:52:24]** that is a point too, right? You mean it is not just a moody teenager with

**[00:52:29]** an omnipotent moody teenager, but it also has, yes, a short memory, yes.

**[00:52:34]** Yes, exactly. Although it is not supposed to be like that. But it does not matter, yes. So from that angle,

**[00:52:40]** I think it is really great that the three of us met here today.

**[00:52:45]** Let me give a hint. It could be that we will soon meet as a foursome.

**[00:52:49]** Whether that will be so, let us see when this episode comes out.

**[00:52:53]** I just wanted to tease it already.

**[00:52:56]** Thank you for being here.

**[00:52:58]** I would like to point all listeners to the show notes,

**[00:53:02]** because we now have a landing page.

**[00:53:04]** We have a WhatsApp channel where we inform you about news.

**[00:53:08]** We also work up our episodes afterwards a bit with bonus material,

**[00:53:13]** which we immortalise on our landing page in a blog, and as Klaus already said,

**[00:53:19]** if you have something, better not write it to us as an email, but give us a comment

**[00:53:24]** on the respective podcast platforms. We would much rather have stars,

**[00:53:30]** but we take feedback too. Bad things go to Jens, good things go to me.

**[00:53:34]** We will divide that up accordingly, and with that I thank you,

**[00:53:39]** a secure evening to all of you.

**[00:53:42]** Thank you. Bye.

**[00:53:46]** Welcome to Think different, Think AI, the podcast by Mark and Jens.

**[00:53:52]** Two minds in love with technology,

**[00:53:54]** who don't just talk about artificial intelligence, they live it.

**[00:53:58]** Here you get clear judgements, real insights from practice

**[00:54:02]** and a fresh look at what is possible.

**[00:54:04]** Understandable, critical and always with a wink.

**[00:54:08]** AI to think about, to smile at and above all to join in with.
