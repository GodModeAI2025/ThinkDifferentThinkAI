---
title: "Token Budget"
episode_index: 66
published: "Sat, 14 Nov 2026 19:55:00 +0000"
duration: "3395"
page_url: "https://think-ai.podigee.io/66-token-budget"
image_url: "https://images.podigee-cdn.net/0x,s356VuCCNzCyW4gogB_5gPw8HwM4HIpqVpJtiqs2Mm-w=/https://main.podigee-cdn.net/uploads/u73317/eacc6c75-6ecd-448f-89d7-d2c27fddaa40.jpg"
audio_url: "https://audio.podigee-cdn.net/2646571-m-dbf4681966944735c8ea92f0d3280da6.mp3?source=feed"
guid: "7b1c00b7579b4b4dc1b9c59fab840ed7"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "medium"
language: "en"
language_probability: "1"
transcribed_at: "2026-11-14T22:14:29+00:00"
translated_from_language: "de"
translation_provider: "claude"
translation_model: "claude-sonnet-5-5"
translated_from_file: "transkripte/066 - Token Budget.md"
translated_at: "2026-11-14T23:00:00Z"
---

# Token Budget

**Published:** Sat, 14 Nov 2026 19:55:00 +0000
**Duration:** 3395
**Web player:** https://think-ai.podigee.io/66-token-budget
**Cover:** https://images.podigee-cdn.net/0x,s356VuCCNzCyW4gogB_5gPw8HwM4HIpqVpJtiqs2Mm-w=/https://main.podigee-cdn.net/uploads/u73317/eacc6c75-6ecd-448f-89d7-d2c27fddaa40.jpg
**Audio:** https://audio.podigee-cdn.net/2646571-m-dbf4681966944735c8ea92f0d3280da6.mp3?source=feed

## Beschreibung

Abos, API, Budgets und ein Agent auf dem iPhone
Wie viel darf KI kosten, und woran erkennt man, dass sich der Verbrauch lohnt? Mark und Jens sind wieder vollständig am Tisch, Jens ist nach einer Krankheit zurück. Sie sprechen darüber, wie schnell Abo-Kontingente aufgebraucht sind, warum der Umstieg auf die API-Abrechnung teuer werden kann und weshalb der Verbrauch allein noch nichts über die Qualität eines Ergebnisses sagt.

Ein Thema ist der Begriff Token Maximizing, mit dem Entwickler am Verbrauch gemessen wurden, und das Wechseln zwischen mehreren Abos, sobald eines leer ist. Berichten zufolge haben manche Konzerne die Tagesbudgets für ihre Entwickler gesenkt. Ist ein Token teurer geworden, oder leisten die Modelle schlicht mehr? Welche Aufgabe braucht wirklich das größte Modell? Schnelle Varianten kosten mehr, und nur weil einem ein Ferrari in die Garage gestellt wird, fährt man nicht effizient.

Der zweite Teil dreht sich um Apple. Mark hat auf seinem iPhone einen eigenen Agenten namens Hermes gebaut, mit einem notizbuchartigen Interface statt eines Chatfensters, Morgenbriefings aus Kalender und Mails und einer Frage an Apples Private Cloud Compute: Wie weit trägt der Datenschutz? Ob die kostenlosen Kontingente bleiben, ist offen.

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

**[00:00:00]** Welcome to Think Different. Think AI., the podcast with Mark and Jens.

**[00:00:07]** Two tech-obsessed minds who don't just talk about artificial intelligence, they live it.

**[00:00:14]** Here you get clear takes, real hands-on insights and a fresh look at what's possible.

**[00:00:20]** Understandable, critical and always with a wink.

**[00:00:24]** AI to think about, to smile about and above all to join the conversation.

**[00:00:33]** Welcome to Think Different. Think AI.

**[00:00:36]** The dark side of the Force is back.

**[00:00:39]** Jens has risen from the sick.

**[00:00:42]** And I don't know if you know this.

**[00:00:44]** First of all, Jens, good to have you back.

**[00:00:46]** I don't know if you know this.

**[00:00:49]** But scientists have found out

**[00:00:52]** what the infamous man flu looks like.

**[00:00:55]** They put the virus responsible

**[00:00:58]** under the microscope.

**[00:01:00]** And it looks like the Death Star.

**[00:01:02]** On that note, good to have you back and good that you weren't torn to pieces.

**[00:01:08]** A book, the Death Star, I always get a bit... But you're talking totally normally, no wheezing and no smoking.

**[00:01:14]** So on that front I don't have to call you Darth Jens either. Very nice, glad to hear it.

**[00:01:19]** Jürgen Paderan, how are you doing? And right away the critical question, the better half isn't listening.

**[00:01:25]** What do you actually spend on tokens? Oh, okay. Well, first a cheer for

**[00:01:31]** science, for this sensational breakthrough discovery that was made,

**[00:01:35]** what I spend on tokens. So, in a purely private setting I'd say it's with

**[00:01:45]** Nvidia, ChatGPT, a bit of Max at Claude. Well, I'd say in the range of 100 to 200 dollars

**[00:01:59]** a month. You said a month. I was briefly scared, because otherwise I would have had to ask

**[00:02:05]** hour, day, week, quarter. Yeah, you never know. I recently had, greetings go

**[00:02:12]** out, I don't want to name names, someone who said, listen, honestly,

**[00:02:15]** with the 20, I think he has the 20-whatever subscription, so something small, yes. And that will

**[00:02:21]** be completely enough. And I sit there thinking, how can that be? Well,

**[00:02:25]** there was my time, I have to say, we'll leave the context hanging in the room. I once had

**[00:02:31]** vacation and I didn't use any during the vacation either, and it ended up in four figures. Yes, the vacation

**[00:02:39]** was two weeks. Well, that's how it is. There was a way to expense it, though.

**[00:02:45]** What's maybe worth mentioning at this point, I think it's a, how should I put it,

**[00:02:50]** just like you say. Spending a lot doesn't automatically mean being

**[00:02:55]** wasteful, but spending a lot also doesn't automatically mean

**[00:02:59]** being a pro. That's quite a narrow line

**[00:03:02]** you're walking when you, let's say, bring the machines to

**[00:03:07]** their knees. I recently had the chance to compare this, and namely, you

**[00:03:12]** know how it is, there are subscriptions and you've heard that

**[00:03:15]** subscriptions are subsidized. I recently got to test what that's like,

**[00:03:20]** the subsidization. That means I worked on my stuff the whole livelong day

**[00:03:32]** and tried to keep up with the coding. And at some point the tokens ran out. I mean the tokens

**[00:03:40]** from the subscription. And after the tokens from the subscription were all gone, I switched to not subscription use,

**[00:03:46]** but pay-per-use, so API-token-call style. And I then found out that on

**[00:03:55]** that one day I ended up just under three figures. Just under three figures. Then I thought briefly,

**[00:04:01]** token subscriptions are worth it, purely in monetary terms, because I hadn't changed my way of working.

**[00:04:07]** I admit, boss joins in, it was for work, greetings go out. And then

**[00:04:12]** you sit there and think, okay, wait a moment, you had the subscription, the subscription ran out, putting work

**[00:04:16]** on hold isn't an option, you used lots of tokens because you had lots of things done,

**[00:04:20]** I let lots of super agents start and they work, handing each other

**[00:04:23]** the work.

**[00:04:24]** And yes, I do switch back and forth between Sonnet and Opus and stuff like that,

**[00:04:28]** but a lot simply happened, right?

**[00:04:30]** So.

**[00:04:31]** And then it was used up and the work still has to get done, so API-based.

**[00:04:34]** And then you think, okay, if on that day you spend more than

**[00:04:38]** the subscription costs per month. I see the catch, because then nobody can explain to me

**[00:04:45]** that, with API usage, the subscription models pay off for all the providers. And that

**[00:04:50]** will get exciting when they eventually go public, because then I don't think

**[00:04:54]** they'll keep feeding everyone tokens with a golden spoon, so to speak,

**[00:05:00]** subsidized. My opinion.

**[00:05:02]** Yes, good point. We'll wait and see what happens there. I'd also say again

**[00:05:05]** a bit, like I called it earlier, for me it's

**[00:05:09]** often subscription-based. I catch up on tokens, so I probably also burn

**[00:05:13]** more tokens than I actually pay for with the subscription fees

**[00:05:16]** I have. Because first, quickly, I also had a video produced in a

**[00:05:19]** setting, now shortened. That really hit hard

**[00:05:23]** fast. If I want to nail two and a half minutes reasonably

**[00:05:27]** professionally, then that was quite easily another 200

**[00:05:31]** dollars of extra tokens that I burned in one evening. But also because I then scaled

**[00:05:37]** back, and afterwards it was totally fine, since it was only demo effects,

**[00:05:42]** if you'd then had to bring it up to truly professional quality,

**[00:05:46]** probably a bit more would have gone out. But on the other hand,

**[00:05:50]** still cheaper than if I had gone the classic route, whether I'd have

**[00:05:55]** hired someone or put in the time myself to

**[00:06:00]** produce it. You should never forget that, because all the token topics we have here,

**[00:06:03]** on the other hand, there's also, apart from the AI slop and all the nonsense that gets passed around

**[00:06:10]** and texts that... Oh, a cat video. Things like that are of course nonsense to do and to

**[00:06:16]** count in, because when we talk about productive work, then of course

**[00:06:19]** you have to say, yes, if it also produces a productive result

**[00:06:23]** then it's filed away as a trophy. I'd say what matters is that

**[00:06:27]** it's a productive item, something that comes out at the end and can be used, then of course you have

**[00:06:33]** to look at the total costs. If in the past you first shuttled a briefing

**[00:06:37]** back and forth, drove it out to an amateur, when you hand off a video like that.

**[00:06:41]** like that.

**[00:06:42]** Price costs.

**[00:06:43]** Price costs.

**[00:06:44]** Set costs, hourly rates.

**[00:06:45]** Computers are running there too, though.

**[00:06:46]** Exactly. Even there computers are running that have to render something, render 3D design,

**[00:06:49]** or something else. So there are things that are simply a lot

**[00:06:52]** faster now. We've also talked about this often in earlier episodes.

**[00:06:55]** If you look ahead, a lot of things may either not happen in the cloud at all anymore, but locally on some servers,

**[00:07:01]** then it's basically a different topic, where I say, okay, not everything has to be real-time,

**[00:07:05]** not everything has to be there right away tomorrow, so it can be computed a bit more slowly too.

**[00:07:10]** And then maybe this topic of, yes, so many tokens being burned,

**[00:07:18]** if you look at it from that angle, without me being able to do the math,

**[00:07:22]** someone else is welcome to do that. Gut feeling, I'd say it's

**[00:07:26]** maybe not such a drastic break-even calculation that would come

**[00:07:30]** out of it. Maybe even more positive for the topic of AI use

**[00:07:35]** at the home front. And maybe you should also look at it in that light.

**[00:07:38]** Maybe one more thing from my own experience, since I've

**[00:07:42]** already talked about token costs. I recently had the chance to use the

**[00:07:47]** big Opus, not Opus, the ChatGPT model with the option of

**[00:07:53]** super speed. And that was fascinating, because a, it wasn't

**[00:08:00]** finished before the tokens were used up, and b, the tokens were used up after five

**[00:08:04]** hours. After five hours it had chewed through the 500 subscription, laid it to rest.

**[00:08:11]** So it was fast. Well, it also had a lot of projects that

**[00:08:15]** it was working on in parallel. It didn't get any of them properly finished, and I have to

**[00:08:20]** get by from week to week, and I thought to myself, then

**[00:08:23]** this turbo speed doesn't help you either. If you're, let's say, done after five, six

**[00:08:27]** hours, it could have run through the whole week, then the

**[00:08:30]** performance wouldn't have mattered either. Yes, then it might even

**[00:08:33]** have gotten a bit further, because this turbo speed

**[00:08:38]** costs more in proportion too. So my big resolution is,

**[00:08:42]** when Wednesday comes and the tokens refresh for me again, that I say again,

**[00:08:46]** oh come on, take your time, because then at least you're kept a bit busy throughout, and that's

**[00:08:51]** my contribution to token cost optimization. Greetings go out. Yes, speaking of token cost optimization,

**[00:09:00]** oh oh, so this week, here at the beginning of November 2026, 2026, another year like that. What

**[00:09:10]** they've all been through. I think we learned the term token maximizing very early

**[00:09:15]** at the start of the year, or got to learn it. Do you want to explain it briefly? Yes, it was about the

**[00:09:22]** idea that actually no person, and above all no programmer, was worth anything in the eyes of their

**[00:09:26]** employer if they didn't use millions of tokens per second. So a

**[00:09:31]** bit exaggerated. But that was basically it. Accepted. Exactly. This marketing

**[00:09:38]** story, also a bit from the big providers who said, oh, you have to

**[00:09:41]** have your developers really burn through the tokens, and if a developer doesn't somehow

**[00:09:46]** generate insane token costs, then he's not really a proper developer

**[00:09:49]** anymore. In all these weird excesses, this term token

**[00:09:56]** maximizer came about, so to speak. Yes, so before that we were basically measuring our work

**[00:10:04]** by the number of tokens you use for your work.

**[00:10:09]** I'd like to add one more thing.

**[00:10:11]** At least I once heard the term token maximizing used to mean that you have several subscriptions

**[00:10:18]** and when one subscription is empty, you log in to the next one, you

**[00:10:24]** switch the login, so to speak, which of course has the charm that, if you're on Claude Code, for example,

**[00:10:29]** and you had several subscriptions and you do log off, log on, log off, log on, log off,

**[00:10:32]** then you get that 200 plan or whatever it is several times and can keep working

**[00:10:40]** in the hope that when you're through the last one, the first one starts again, and I

**[00:10:45]** even know someone who has five, it's really not me, it's not like Rita, what do

**[00:10:50]** the condoms cost? No, really, five big subscriptions at Anthropic and it doesn't last him the

**[00:10:57]** week, that's wild too. Yes, that's a bit crazy. So of course there were then

**[00:11:02]** optimization topics too, like you said. We all know this weekly budget now and

**[00:11:06]** such. And then people also started looking at, okay, can I maybe build my harness so

**[00:11:11]** that it very cleverly produces the code or whatever via AI, or the

**[00:11:18]** insanely big research task you've given it, distributes it so that you basically

**[00:11:22]** then cleanly use up those budgets that you had everywhere.

**[00:11:25]** So, we were close to saying that we're actually also a, yes, the,

**[00:11:33]** now I can't think of the saying, the one with the golden whatever, I'm always like that,

**[00:11:37]** sayings, I'm not good at them, right?

**[00:11:39]** It's more about saying that we've basically been the producers

**[00:11:43]** for this gold rush at the big providers.

**[00:11:46]** Gold rush, do you know what I think of then?

**[00:11:49]** You can say the word AI, and then imagine at gold rush, please don't

**[00:11:53]** get me wrong, but what comes to mind is a cowboy, hardly any teeth left in his mouth, but

**[00:11:58]** a smile because he pulled a gold nugget out of the river, like yes, and onward,

**[00:12:03]** and that's a bit like this AI stuff.

**[00:12:05]** Yes, and we're basically also the ones who were supposed to fuel that

**[00:12:10]** on top of it.

**[00:12:11]** So if we don't fuel it, then it's basically our own fault,

**[00:12:15]** because we're not worth anything anymore, and that of course was a very, very fine

**[00:12:17]** story for the big providers, who sacrificed themselves for it.

**[00:12:20]** But it did start to reverse a little over the summer, I had the feeling.

**[00:12:28]** It was viewed a bit more critically.

**[00:12:30]** People also said, hey, just blasting out all these tokens might

**[00:12:33]** not be such a good idea.

**[00:12:34]** Environmentally maybe not the smartest either, you always have to keep that in mind.

**[00:12:38]** These huge AI centers that are actually being built next to residential areas

**[00:12:42]** in America, that's really not a nice thing they're doing.

**[00:12:44]** No, were being built.

**[00:12:45]** The midterms. Lots of states suddenly moved toward the Democrats.

**[00:12:49]** Not that the others aren't democratic, but I mean the

**[00:12:52]** Democratic Party. And as far as I picked up, in the context of the election

**[00:12:56]** there were also votes on lots of data center projects,

**[00:13:00]** in the form of what citizens think about them. And I could well

**[00:13:04]** imagine, I mean the Democrats aren't anti-business or

**[00:13:08]** anything, but I could imagine that there's simply more

**[00:13:11]** participation now, so that you don't just say, listen up,

**[00:13:15]** you're getting a data center put in your neighborhood now.

**[00:13:17]** We park the gas turbines on trucks, because then they don't count as a gas power plant,

**[00:13:21]** but as something else. Then it's no problem at all.

**[00:13:24]** I don't care what happens with water and electricity.

**[00:13:26]** And people work there at, no idea what kind of wages.

**[00:13:29]** Along the lines of, you don't get a job and everything still stinks.

**[00:13:32]** Certainly some optimizations will take place there now.

**[00:13:35]** And I also found it totally fascinating that Sam Altman,

**[00:13:37]** who just a few days ago was telling us how terrible it is

**[00:13:40]** that people have RAM in their private computers.

**[00:13:43]** You could use it so much better on your side.

**[00:13:45]** That they're now no longer talking about AI data centers either, but about superintelligence, compute campus, blah blah blah, reframing it,

**[00:13:55]** because then they wouldn't be affected by all this data center stuff, and that plays in a bit too, where I think you want to go with this topic later.

**[00:14:03]** People, maybe fewer tokens. Maybe we put a limit on it, along the lines of, maybe we'll need the compute capacity for something else in the future,

**[00:14:13]** who knows where this journey is heading.

**[00:14:15]** Yes, definitely. And that's also a bit of what surfaced in the first days of November this year.

**[00:14:22]** There were reports that larger companies, I think it's Apple, Tesla, Microsoft and co.,

**[00:14:28]** have indeed cut their budgets for their developers, non-technical people, these ones, in some cases drastically.

**[00:14:39]** Well, then somehow from 300 dollars for developers down to 200 dollars a day.

**[00:14:44]** So a completely different sum from what we just talked about.

**[00:14:46]** A day?

**[00:14:47]** A day, yes.

**[00:14:48]** That's still...

**[00:14:49]** Wait a moment, stuff for developers or for knowledge workers?

**[00:14:52]** I haven't dug that far.

**[00:14:53]** So, these were developers.

**[00:14:54]** The developers.

**[00:14:55]** No, they were definitely developers.

**[00:14:56]** Okay.

**[00:14:57]** Yes, definitely, no.

**[00:14:58]** Right, understood, for developers.

**[00:14:59]** Because knowledge workers, I think, don't burn through it.

**[00:15:01]** Yes, the kids, they went down to 25 dollars or something like that, right?

**[00:15:04]** But that doesn't matter now.

**[00:15:06]** Those are basically the individual figures. I'd read something about Tesla too,

**[00:15:10]** 200 dollars per week for some department, over 1,500 dollars for coding tools a month or something like that.

**[00:15:19]** So basically a cap was introduced. But go ahead, you first.

**[00:15:24]** I was just wondering, with this story about the RAM, as you say,

**[00:15:28]** and I heard somewhere, I don't know if it's fact or rumor,

**[00:15:30]** so I won't even frame it as either, that Microsoft is also somehow on it,

**[00:15:34]** doing something like SETI at Home, where you make graphics cards, CPU and RAM available

**[00:15:40]** to them.

**[00:15:41]** I was just wondering whether Elon will at some point get the idea of using the compute capacity

**[00:15:45]** of his Teslas while they're parked, along the lines of, so that he can compute

**[00:15:49]** for them.

**[00:15:50]** I'd find that totally funny.

**[00:15:51]** Should that be the case, Elon?

**[00:15:52]** My idea?

**[00:15:53]** I want a cut.

**[00:15:54]** Yes, maybe he's already had it and it's happening again even without you

**[00:15:58]** knowing.

**[00:15:59]** I'm trying to get rich somehow.

**[00:16:01]** It's not working.

**[00:16:02]** It's not working.

**[00:16:03]** I'm already stuck too.

**[00:16:04]** I got out of Bitcoin at 60 euros.

**[00:16:07]** With how many?

**[00:16:10]** Two.

**[00:16:11]** Two.

**[00:16:12]** Well, alright.

**[00:16:13]** Yes, alright.

**[00:16:14]** But two today?

**[00:16:15]** That would have been nice.

**[00:16:16]** Yes, an awesome vacation and more.

**[00:16:18]** But fine.

**[00:16:19]** We're at Think Different. Think AI. here, not Think Podcast, Think Missed Opportunities

**[00:16:24]** or whatever.

**[00:16:25]** Exactly.

**[00:16:26]** With heart, I'd say.

**[00:16:27]** So, to stop poking around in that wound, we're basically in

**[00:16:32]** a phase now where we're suddenly talking about budgeting tokens, and that's something

**[00:16:39]** I'd really like to talk through with you, because I think what's happening there

**[00:16:43]** is clearly connected to these IPOs, which you just hinted at. When the IPOs happen, I think OpenAI

**[00:16:49]** is also overtaking, I think,

**[00:16:53]** Anthropic, because of the speed. I think first it was Anthropic

**[00:16:56]** last week or the week before that, who announced they'd be going public soon,

**[00:17:00]** and now I've heard from OpenAI that they want to go public even faster.

**[00:17:04]** So one wants to beat the other. We'll have to see.

**[00:17:07]** You hinted earlier that in the course of this, taking another close look at the business model

**[00:17:11]** might lead to the subscriptions

**[00:17:17]** perhaps not being quite so cheap anymore, and token costs could be excluded again.

**[00:17:22]** Who knows? And I have the feeling that the big companies of the world are now saying,

**[00:17:27]** after we had a phase of "come on, everybody should get to try out AI,

**[00:17:32]** it costs nothing," that they're now thinking, aha, maybe a small limit

**[00:17:37]** isn't such a bad idea for one person or another.

**[00:17:41]** I'd like to pick up on one point.

**[00:17:44]** Yes.

**[00:17:45]** I do think these subscription prices will certainly change,

**[00:17:50]** they'll undergo a shift.

**[00:17:51]** But I find the framing "tokens are getting more expensive" not quite

**[00:17:56]** right, because if you compare what you get in performance, that's a completely

**[00:18:02]** different matter. Just because you say, okay, I don't know, the Opus model costs more and more

**[00:18:11]** tokens get used. I also think the term "burning" is funny, but

**[00:18:16]** nothing is being burned. It's converted into heat because the computer is running, but anyway, what I want to say is

**[00:18:21]** compare it to what I got a year ago for my ChatGPT subscription.

**[00:18:27]** Back then the small subscription was just as expensive as today, but

**[00:18:31]** the performance I get today for the small subscription is exorbitantly more. That I have

**[00:18:36]** higher consumption, higher usage, isn't

**[00:18:39]** because tokens per se got more expensive.

**[00:18:42]** It's simply because I push the big models to do more things,

**[00:18:45]** and maybe I say, well, come on, let me prepare a

**[00:18:50]** prototype. We discuss a finished prototype, where in the past

**[00:18:53]** we'd have said, count people onto a train, off to wherever, and off we go. Now we talk about it by

**[00:18:58]** saying, okay, I'll bring something along tomorrow and we'll talk about what we

**[00:19:02]** built there, what we identified, what we researched and so

**[00:19:05]** on. That means just because I use the system more and therefore spend more

**[00:19:09]** money doesn't mean the tokens became more expensive relative to what I get

**[00:19:14]** for them. And then when I look at what you get

**[00:19:17]** with the open-source models. I mean, people always ask, is it as good

**[00:19:20]** as the current frontier? No, or yes, or whatever, but is it as good as the

**[00:19:27]** frontier we thought was awesome a year ago? Most of them are better. And when I

**[00:19:34]** look at it, I for example love working, and I'll risk the laughter

**[00:19:39]** of our listeners here, with Sonnet and with Haiku. Haiku 5.5 is really good for standard stuff

**[00:19:46]** in terms of cost. Nothing is really measured, but I find it totally cheap for

**[00:19:53]** what it does for me. No cow-fodder could have taken it. It's like,

**[00:19:57]** you don't want to roll the dice. Okay, okay. That's a whole other story

**[00:20:02]** we're opening up there. It brings me to the topic that I always wanted to write a

**[00:20:06]** little article about. The difficulty for the ordinary user

**[00:20:12]** of making this differentiation in the first place. I think even for

**[00:20:16]** some programmers who work intensively

**[00:20:19]** with these topics it's not so easy, because you almost have to build

**[00:20:23]** your own benchmark again for your specific task, to decide whether you take this

**[00:20:27]** model or that model. We only hinted at it earlier, with which

**[00:20:31]** speed, is this an important task, the most important task in the

**[00:20:35]** world that you want to solve, or just a tough problem you

**[00:20:39]** have. That's of course really hard for us humans to judge, what is

**[00:20:42]** that actually, basically, because I have to go to my boss in a moment and present something to him, is that

**[00:20:46]** therefore the toughest problem in the world, or is it the toughest problem because

**[00:20:50]** at least somehow... Depends on your boss. Again, greetings go out to Gene.

**[00:20:54]** It could also be something else, because I want to, I don't know, understand the rules of

**[00:21:00]** the kindergarten, or have to look up whether the airport, whether the airport...

**[00:21:05]** I'm raining the kindergarten. Yes, I always say I'm not looking anything up right now. Or what counts as

**[00:21:10]** a carry-on bag and what doesn't. And for that, you'd better

**[00:21:14]** google and not ask the AI models. That's all a lot, too. All I want to say

**[00:21:17]** is that I think we'll have a topic there in the future, that

**[00:21:23]** if the providers don't do it, we should get significantly

**[00:21:28]** clearer internally and also help our people. We recently had

**[00:21:31]** an episode on AI transformation, saying that we should make much

**[00:21:36]** clearer what the models are actually for. So for example, to

**[00:21:39]** prepare a PowerPoint, if that's still necessary in my work environment,

**[00:21:45]** do I absolutely have to use the latest frontier model for it, or

**[00:21:50]** wouldn't a weaker one do, for example a locally running model that has the task

**[00:21:55]** done by tomorrow? So that's of course a really exciting question

**[00:22:00]** in this phase where apparently more is being budgeted. I think the budgeting

**[00:22:06]** also has something to do with realizing that it isn't smart to give everyone the

**[00:22:13]** Ferrari of AI with every possibility, one that can drive in every direction,

**[00:22:18]** and best case crash, or maybe not even get it to their mouth,

**[00:22:21]** when the job of an individual person is perhaps something different, someone who doesn't necessarily

**[00:22:26]** have to kick off 20 AI agents in parallel to deliver awesome programming output or

**[00:22:30]** to solve a very complex math problem or whatever. I think

**[00:22:34]** we're slowly getting into this phase where we can differentiate, because even the

**[00:22:38]** cheap models are already extremely good. You know, that's also a thing

**[00:22:41]** you just said. It's not like one

**[00:22:44]** or two years ago. The models we've gotten this year

**[00:22:47]** are still all so awesome. You can use the models from the beginning

**[00:22:51]** of the year for so many things anyway, and of course they're

**[00:22:53]** even more awesome and can do other things. But for many,

**[00:22:56]** many standard needs, even last year's models are already

**[00:23:01]** probably completely sufficient in 90 percent of the cases we actually have. And I think we've kind of developed past what we really need.

**[00:23:07]** Before we move on, we still have one topic we want to touch on, but before that, on the topic

**[00:23:14]** of token consumption and costs, let me add one more sentence. I opened with

**[00:23:19]** tokens,

**[00:23:20]** with the effort one causes, or that I partly

**[00:23:23]** cause. Now some people might think, man, what a wasteful mess.

**[00:23:27]** I have to add that of course you also use things like Ponytail here, so

**[00:23:33]** that "the best code is the code that was never written." A skill that teaches the

**[00:23:38]** agent to be frugal, to make things reusable,

**[00:23:44]** plainly and simply also to save tokens. And the thing works in that

**[00:23:48]** it somehow achieves 50 to 60 percent token reduction, because it also

**[00:23:53]** does targeted code reduction. You should do that, which of course

**[00:23:57]** also means the reverse: if you tell the thing, okay, solve this task and start 50

**[00:24:03]** sub-agents for it, highest effort level, biggest model, and repeat the whole thing 20 times

**[00:24:12]** until there really are no contradictions left, and at the end of the day it should really only

**[00:24:17]** add two numbers. That would of course also drive token costs up. So

**[00:24:22]** only, and this occurred to me when you mentioned the Ferrari, just because someone parks the Ferrari

**[00:24:27]** in my garage doesn't mean I drive it efficiently, that I don't

**[00:24:31]** wreck it, that I even master it.

**[00:24:34]** I also remember my old boss, who put me in a

**[00:24:38]** Mercedes for the first time and said, can you fetch this from the workshop

**[00:24:41]** yard for me, because the yard is being closed off. I went there, had never heard of a

**[00:24:46]** foot-operated handbrake, and proved that engine power can also release

**[00:24:52]** foot handbrakes. It tormented, it squeezed, it screamed. Everyone looked out of the window.

**[00:24:56]** I got the car out of the yard. Was that efficient? No. So from that angle

**[00:25:02]** it also applies how you handle the systems, and at this point I'd like to

**[00:25:08]** congratulate all listeners that they don't see the video of us, because Jens, with such a

**[00:25:12]** face, he didn't really say that, right in the kisser. Yes, so from that angle,

**[00:25:19]** maybe we should do it again at some point, we did want to record live again.

**[00:25:23]** Yes, I also saw that you were a guest on someone else's AI podcast.

**[00:25:26]** Well, not a guest, but a guest, so a guest guest, an audience guest.

**[00:25:30]** We'd have to manage the stage thing, but with that, this would be my closing plea.

**[00:25:36]** Watch how you spend your tokens, and just because someone says they spent a lot or not,

**[00:25:40]** that says nothing about quantity and quality.

**[00:25:43]** You do have to look at how people handle it,

**[00:25:47]** and I don't want to talk up my own case, what I reported to whom or not,

**[00:25:51]** just eyes open when buying tokens. So yes, then you may add one more sentence,

**[00:25:57]** it was never the lines of code, the famous ones, that said anything

**[00:26:02]** about the quality of a product in the end. So accordingly, you should always look at the

**[00:26:05]** right KPIs, and in the end, whether you spend tens of thousands of tokens, millions,

**[00:26:12]** or even trillions. If the problem is solved afterwards and solved better than we would have solved it in

**[00:26:19]** another way, then it made sense. And just as you make decisions otherwise in your private

**[00:26:25]** or professional life, it's now important to keep checking,

**[00:26:30]** okay, just because someone spends a lot of tokens doesn't mean they're

**[00:26:35]** wasteful. If I look at the outcome they have, not just at

**[00:26:41]** the outputs, and see that it has economic success, then it's simply also a well

**[00:26:46]** invested budget in this case.

**[00:26:50]** Well invested budget is a really great magic word.

**[00:26:53]** Yes.

**[00:26:54]** Well invested money.

**[00:26:57]** I just noticed, you can't see this, the market is the owner, the proud owner of a

**[00:27:04]** this new clamshell phone, not the new Nokia clamshell phone, but the new clamshell phone.

**[00:27:12]** Nokia Communicator 2600.

**[00:27:14]** Do people actually still say clamshell phone? Yes, actually they do. That's the class of clamshell phones.

**[00:27:18]** I haven't heard the word clamshell phone in a long time.

**[00:27:22]** When I came home with the iPhone Duo and my daughter saw it, she said at most Samsung.

**[00:27:27]** I found that kind of irritating at first.

**[00:27:30]** But yes, foldables have somehow not quite been Apple's thing. But I have to say,

**[00:27:37]** I haven't had a phone in a long time that gave me so much fun. Well,

**[00:27:40]** to be fair, even if it weren't so, at that price point you'd have to say so,

**[00:27:45]** because otherwise you'd have to admit that you spent an awkwardly large amount of money for little fun.

**[00:27:50]** But I mean it completely seriously, because this device, it's like

**[00:27:55]** a little black book, yes, you could say, old white man, little

**[00:27:59]** black book. No, that's not the point at all, because I also got that

**[00:28:02]** magnetic case from Apple. It's also what you get inside, namely the

**[00:28:07]** possibility that, depending on what you're working on, you have a small or

**[00:28:11]** a big screen. You'll say, okay, I have that with the Samsung phones

**[00:28:14]** too. But then I sat down, and we wanted to get into that, I think,

**[00:28:19]** Jens, and built myself a little harness on this device.

**[00:28:27]** Device.

**[00:28:28]** Device.

**[00:28:29]** On the device.

**[00:28:30]** Yes, the device got a harness, and before I say what the harness can do,

**[00:28:35]** I have to tell you I'm seriously irritated, because if you've followed me professionally

**[00:28:40]** so far, you'll know that I now do something with AI, but that in my

**[00:28:44]** history I was responsible for mobile app development at our company, and back then I always

**[00:28:50]** said, you know what, folks, we build beautiful apps and we place great value

**[00:28:54]** on good quality and so on, but our competence ends where the phone ends.

**[00:29:01]** So if you need server infrastructure, there are other people with the

**[00:29:05]** relevant expertise. We make sure it runs well on the phone. We don't meddle in your work,

**[00:29:08]** you don't meddle in ours, and then we all get along when it comes to the solution.

**[00:29:12]** And why am I telling this? I somehow noticed that when I started building my

**[00:29:19]** harness, it was always like this. You have a harness and the harness

**[00:29:22]** reacts to what you want from it. Usually the harness says, what can I do

**[00:29:26]** for you today? You type something into the chat and the harness does it.

**[00:29:30]** And what I've now put together on the iPhone feels like it goes a different way.

**[00:29:37]** You can type something in and it does it.

**[00:29:40]** But you can also type in, do this tomorrow at eight. Then it

**[00:29:46]** does it tomorrow at eight. Needs no server, runtime, anything. It does everything

**[00:29:51]** locally and then gives you, tomorrow for example, your daily briefing or your AI research.

**[00:29:58]** Every morning I have it tell me, what happened in the last four hours.

**[00:30:02]** And it gathers all of that, and now if someone says, and I have to say the

**[00:30:07]** word, because I coin it at least once in every episode.

**[00:30:10]** And then I went and had it do that.

**[00:30:13]** If someone now says, that's not a real harness, because you don't have a

**[00:30:15]** sandbox and so on.

**[00:30:16]** That's hilarious.

**[00:30:17]** Because it does.

**[00:30:18]** So the harness I built there, maybe a few key facts, it uses...

**[00:30:24]** Feel free to explain sandbox and harness once more.

**[00:30:27]** So a harness, for me, is, let's say, the meeting place between human and machine.

**[00:30:30]** Namely on the one hand the user interface that a human has to interact with AI systems,

**[00:30:35]** and on the other hand the runtime environment, so the program that lets me interact with an AI model,

**[00:30:42]** with the help of tools, that's MCP, and with the help of prompts and instructions, those are skills.

**[00:30:48]** And this app, this application that runs on the iPhone, represents exactly that coming together.

**[00:30:54]** That means it gives me an interface to talk to this AI model.

**[00:30:59]** And the funny thing is, this AI model is not Anthropic or OpenAI, it's Apple Private Cloud Compute.

**[00:31:09]** So the models that Apple trains itself and runs in its data center,

**[00:31:14]** where they say the privacy level is equivalent to processing on the iPhone itself,

**[00:31:20]** where up to two million app installs they don't want to charge for tokens,

**[00:31:24]** and the thing runs in this harness.

**[00:31:28]** And since you just brought up the topic of sandbox,

**[00:31:31]** you can't actually build a sandbox in iOS,

**[00:31:34]** one second, you can't build it in iOS,

**[00:31:36]** because Apple actually forbids executing code at runtime.

**[00:31:42]** And my coding agent actually thought, I've got something nice.

**[00:31:47]** Loosely put, it has an on-the-fly Python interpreter

**[00:31:51]** that then translates on the fly into something Apple-friendly.

**[00:31:54]** That means I have a sandbox and I can run skills, and with that I can for example also say,

**[00:31:58]** research this and turn it into really nice slides,

**[00:32:02]** which it assembles in this sandbox, clicking and doing things and generating program code,

**[00:32:08]** and then hands me those slides at the end. And before I keep gushing and perhaps

**[00:32:12]** mention two or three more cool Apple features, you raised your finger,

**[00:32:16]** you wanted to say something. Yes. You wait, because I have a follow-up question,

**[00:32:19]** I didn't quite understand. You briefly mentioned the 2 million apps

**[00:32:25]** that Apple expects. I had heard at some point that basically it's still

**[00:32:30]** free right now, but I didn't quite understand the 2 million apps.

**[00:32:33]** That I download 2 million apps, or what's the statement?

**[00:32:36]** No, no, no, no.

**[00:32:37]** These are different pairs of shoes.

**[00:32:39]** So first, if you use Private Cloud Compute, it counts against the user's quota.

**[00:32:44]** And the user has different things depending on what they've signed up for with Apple, iCloud Plus and so on,

**[00:32:49]** and I haven't seen conversion matrices, but I read somewhere

**[00:32:54]** on Reddit that the more expensive your subscription is, the

**[00:32:57]** more compute Apple offers you, so to speak, for the applications you have that use Apple

**[00:33:02]** Intelligence. If I build an app as an app creator, you can basically

**[00:33:09]** put it in the store or upload it to TestFlight, that's Apple's beta store, so other

**[00:33:14]** people can use it. And if two million people download it,

**[00:33:19]** then from that point it costs money, 100,000. I should check that. It's of course

**[00:33:25]** an important zero, but either would be far, far, far away for my little game.

**[00:33:30]** Yes, I think it was 200,000. I'll have to look. I'll fact-check it.

**[00:33:35]** But in any case, that's the limit for the developer to be free.

**[00:33:40]** What it costs after that, nobody knows. And what you just hinted at,

**[00:33:44]** I had it either in the pre-conversation or just now, I don't know right now, yes, I'm

**[00:33:47]** getting old, old and senile. It's somehow going through the press that Apple

**[00:33:51]** would reduce these free tokens, and I understood it like this,

**[00:33:56]** that the possibility that, if you were to load my app now, you'd trigger

**[00:34:02]** that Private Cloud Compute stuff less often before you hit a pause,

**[00:34:09]** like we know it from Anthropic and co., where it just says

**[00:34:12]** Private Cloud Compute is currently at capacity, please come back later.

**[00:34:15]** Okay, my UX heart is reacting to that again, right?

**[00:34:20]** Honestly, nothing is getting any simpler at the moment.

**[00:34:25]** So of course that's an issue for the users.

**[00:34:28]** On that topic they're already going to look at how much am I spending?

**[00:34:33]** Is the budget running out? Either the one from my company

**[00:34:36]** or the weekly budget or the daily budget

**[00:34:39]** that my AI gives me at a certain speed.

**[00:34:42]** You also say again that with Apple Intelligence that's a topic too. I think we have to,

**[00:34:47]** I don't even want to criticize that, it's all trial and error, and the vendors

**[00:34:50]** first have to find their business models and see how it works, and I think

**[00:34:54]** it's good that you can still experiment with it now. I hope that was a

**[00:34:57]** solution for Finn, because I think this is something that makes things really complicated and then

**[00:35:03]** might hold some people back afterwards, because they're afraid, maybe unfounded,

**[00:35:08]** that they'll have to spend a ton of money. That's always a bit where I say,

**[00:35:12]** we have to make all of this a bit simpler. Although, at this point I'd like to

**[00:35:16]** stand up for it, because whether I add the zero or not, 200 or 2 million,

**[00:35:22]** if you're an indie developer or even if you're releasing an app for work

**[00:35:28]** and you've got your 40, 50, 60, 70, 80, 90, 100,000 customers and you can

**[00:35:34]** provide them with an app that basically just uses the AI functionality along with it. Is

**[00:35:41]** that, not too specialized. And that limit with Private Cloud Compute, I ran

**[00:35:46]** into it myself, where it told me, you have to wait now. But this story,

**[00:35:50]** I can build myself a harness that can basically use skills, like we know it from Anthropic.

**[00:35:57]** Locally on the device, which holds everything and does everything. And you basically

**[00:36:03]** have research tasks, prepare me for the day, rate my day, like a knowledge

**[00:36:07]** navigator for the day, which has access to all the data your iPhone has,

**[00:36:13]** health, location, weather, reminders, calendar, mail not, that needs a

**[00:36:18]** bit of a different trick, but files and things like that, that's already, so I

**[00:36:24]** have real fun with this little harness, because on the one hand, I know a

**[00:36:29]** bit about iOS, what I'm doing, even if I mix up the zeros,

**[00:36:32]** I know a bit about what I'm doing and I can

**[00:36:35]** express myself a little, let's say, because I'm also thinking about it, and there

**[00:36:39]** your UX heart might beat a notch faster, thinking about what such an

**[00:36:44]** interface looks like when I don't think in chats. So the harness right now has, for example,

**[00:36:49]** an interface that looks like a notebook. You've got lots of different

**[00:36:54]** pages, from packing lists to calendars to I don't know what. You can write by hand

**[00:36:59]** and it turns that into nice handwriting, and whenever you

**[00:37:02]** write in a different color, it knows, oh, that's a command for the AI, and then it adds

**[00:37:06]** something for you, I'm trying a bit along the lines of a co-author who's always reading along,

**[00:37:12]** right. But you can also switch to chats. What's funny is, if you have a chat like that,

**[00:37:17]** you know it, lots of text and at the bottom you type something and again lots of text,

**[00:37:20]** you can take the pen and just scribble into that chat history, more

**[00:37:26]** detail here, less here, and then it reacts to that. That means you're not

**[00:37:32]** interacting just with speech, which would of course totally suit the AI system,

**[00:37:35]** but you can sit somewhere, you flip your thing

**[00:37:39]** open, up comes the chat or these pages, and you write, and it

**[00:37:43]** reacts to your handwriting. That makes the whole thing feel a bit

**[00:37:46]** more approachable. I find it extremely wild that all of this

**[00:37:53]** runs just in a phone. Fair point, the model runs in the cloud at Apple,

**[00:37:58]** but I consider Private Cloud a whole notch stricter when it comes to data protection.

**[00:38:04]** If you just look at how Apple secures its hardware, secures its infrastructure,

**[00:38:09]** how it opens up security previews, how you can check it yourself too.

**[00:38:13]** Everything's in there, theoretically my contact data would be in there too,

**[00:38:17]** everything is theoretically in there. Yeah exactly. Then I'm with you, I do assume

**[00:38:22]** the app has secured that fairly well, a few mottos, you know better, yeah, okay. So and if you

**[00:38:29]** then imagine, you've got the phone, you can fold it open and shut, unfold it, then you edit

**[00:38:33]** with the pen inside, fold it shut, then you see the status overview of your chats, the

**[00:38:38]** thing, or you've got this book mode, then you set it up, kind of like an open

**[00:38:43]** book, it's like, well, you can stand it up. And then it reacts with

**[00:38:48]** its visualization to that. That's really fun. And then, as I said,

**[00:38:53]** I'm already facing the question, if there's a bit more computing power in there,

**[00:38:56]** if you maybe have a bit more model logic in there.

**[00:38:59]** Private Cloud Compute, for example, has no image analysis. So they

**[00:39:04]** don't have that yet, in quotation marks. Then this can get really powerful

**[00:39:09]** for the classic knowledge worker. I'm standing here,

**[00:39:13]** get me, I don't know, get me a letter for the insurance

**[00:39:17]** ready, help me here, help me there. And, that's also pretty cool, it even has browser use.

**[00:39:22]** On the iPhone a little window opens on the right, looks like Safari,

**[00:39:27]** isn't Safari, but looks like Safari. And then it operates the browser in that thing.

**[00:39:33]** What I consider completely normal on a PC, it simply does on my phone.

**[00:39:37]** That really gets my eyes lighting up. I've got a bit of

**[00:39:41]** playfulness and enthusiasm there. Yes, that's basically a topic

**[00:39:47]** we two have discussed more often, whether it was something with my Mac Mini application

**[00:39:53]** or something else, that it's kind of exciting when you feel like you're a

**[00:39:58]** bit more in charge of this, I mean of the harness, either way, you build that yourself

**[00:40:05]** after all, but of what the AI does there, and not being quite so much the plaything of the big

**[00:40:10]** players. That's actually what I'm taking from your words, as I listen to you.

**[00:40:14]** already, I'm listening to you fascinated and actually wondering right now, if I need to get a Duo

**[00:40:19]** too, then we'll have to talk about that again later, what I should order

**[00:40:24]** there.

**[00:40:25]** Because it's of course pretty cool when you have it in your pocket, you just

**[00:40:32]** said it, it's of course still more of a cloud model, it's

**[00:40:34]** not a local AI model running on the Android, if I understood it correctly,

**[00:40:38]** but still your data is kind of with you, your agents with you,

**[00:40:45]** your harness is basically completely with you in your pocket, it goes along and is actually

**[00:40:51]** a bit like your real personal AI that you can carry around, the personal

**[00:40:57]** assistant in your pocket.

**[00:40:59]** Plus, which you mustn't forget, because it's Apple, plus on the

**[00:41:04]** watch, so a voice interface on the watch, plus, because you said not a local model, that's right,

**[00:41:10]** I have it with Cloud Compute now, but on the, let's say, rich board of

**[00:41:16]** extensions, there's also the question of whether you can't slam something like a Gemma model locally onto the

**[00:41:22]** box, so you get even more done locally and maybe with, no

**[00:41:28]** idea, super agents, whatever, says, okay, I'll do this and I'll send that out, and that

**[00:41:33]** you play around with that a bit, so that you become, let's say, more independent. Because

**[00:41:38]** this topic, look at my calendar, look at my tasks, look at my

**[00:41:44]** mails, fair point, you have to release those via IMAP,

**[00:41:47]** otherwise it doesn't work, otherwise Apple won't let me at

**[00:41:51]** my own mails that are in the iPhone. But look at it, prepare something for me

**[00:41:56]** and I go to my phone the next morning, I open it and the

**[00:42:00]** phone doesn't say, what can I do for you? Instead the phone says, Mark, the following things

**[00:42:04]** are open, I've prepared something for you, here, have fun. And all of that, because actually

**[00:42:09]** the model maybe locally at some point, the model otherwise remote, but all the rest

**[00:42:13]** local on your device without, I need whoever, Amazon,

**[00:42:20]** Microsoft, whoever else, some cloud instance puttering away on something, just

**[00:42:25]** in your phone. I find that impressive. Someone will say, but why don't you do

**[00:42:29]** that on your Mac. You could also ask me why you don't do it on your Windows. That

**[00:42:34]** would be out for me, because I have no Windows in my apartment. I'm a Mac user

**[00:42:41]** through and through. There are people who wouldn't even have an Apple logo tattooed on their chest.

**[00:42:45]** I don't want to give you the proof, but it's not like that. The Mac just closes and in the

**[00:42:52]** majority of cases it then shuts off. And even if you say you have a Mac Mini behind the

**[00:42:57]** TV, or mine is standing there, that's all nice, you can install your Hermes there

**[00:43:03]** and it's guaranteed more flexible right now, more capable of learning, builds skills, makes suggestions

**[00:43:10]** and so on, all fine, but it's a separate piece of craft that wants to be maintained,

**[00:43:15]** that runs somewhere, vents, somewhere, somewhere, and this thing you have in your pocket

**[00:43:21]** with you. You have it with you on vacation just the same and don't have to worry about how I connect

**[00:43:26]** to the data, and I find that so fascinating, when it clicked in my head

**[00:43:30]** to say, actually you basically have a client and

**[00:43:34]** a server, so what you used to think of as a client-server infrastructure,

**[00:43:37]** with this cloud render and co. in your pocket.

**[00:43:41]** And it is exactly that. Exactly. Only the question left is how do I get a

**[00:43:44]** sufficiently strong local model onto it.

**[00:43:47]** That would be great, because otherwise we also honestly have to

**[00:43:51]** say, you could of course also think about a virtual server solution with any mobile,

**[00:43:54]** arbitrary end device.

**[00:43:59]** Yes, of course.

**[00:44:00]** Okay, you of course have a cloud somewhere on the virtual server.

**[00:44:02]** But nobody builds that on the side either.

**[00:44:03]** Nobody builds that on the side, exactly.

**[00:44:04]** But there you basically have...

**[00:44:05]** And nobody builds my app on the side either.

**[00:44:07]** It would also work differently at the moment, but I understand what you're saying.

**[00:44:13]** It's simply what, I think, attracts us humans to some products too,

**[00:44:17]** it's a bit more convenient.

**[00:44:19]** It's not so much building it yourself and maintaining something else at another

**[00:44:23]** spot or whatever. Instead you just open it up and get going. And what really

**[00:44:28]** fascinates me too is the question of how you get it to fade into the background

**[00:44:34]** a bit again. That's what I tried with the notebook and whiteboard function

**[00:44:40]** and that kind of stuff, to say, okay, I work in there. Yes, but on my roadmap there is,

**[00:44:46]** so on my roadmap, on my personal experiment, Fatschia, something like that,

**[00:44:49]** that he wants to integrate SharePlay too, meaning multi-user, so that several people

**[00:44:54]** share a session on the whiteboard, which then takes place in the harness, where then

**[00:45:00]** the harness works in there as well, and what you can do with that.

**[00:45:04]** I think you can try out totally many cool things with something like that, although bad

**[00:45:09]** enough, right, you build a work harness, you build a private harness, at some point you should

**[00:45:15]** do something other than nothing but harnesses.

**[00:45:20]** Building harnesses is not a task that everyone out there will have to be able to do.

**[00:45:27]** Let's put it that way.

**[00:45:28]** I think it's actually a small special group that's dealing with it right now.

**[00:45:33]** Many others will simply just get it.

**[00:45:34]** That almost sounds like Alcoholics Anonymous.

**[00:45:35]** Yes, not quite that bad.

**[00:45:36]** Anonymous Ka-Elika.

**[00:45:37]** Exactly.

**[00:45:38]** I'm addicted to harnesses.

**[00:45:41]** No, so basically it's the case that I say, yes, providers are coming, whether those

**[00:45:45]** are device makers or the software providers after all, they will come and

**[00:45:48]** they will deliver you the harness, also coming there, for a small

**[00:45:54]** subscription fee, usually always. And accordingly not everyone has to

**[00:45:57]** deal with it. So what we're doing there is also a bit of

**[00:46:00]** instrumenting, also a bit of research. What's actually possible right now,

**[00:46:02]** out of professional interest, out of private curiosity, we like to take a look at

**[00:46:06]** these things and tinker around a bit and

**[00:46:08]** burn one token too many or another for our. Honestly

**[00:46:13]** so that we can then pass one or two things on to you every now and then.

**[00:46:17]** As the saying goes, let's turn the token over once more before we burn it.

**[00:46:21]** Oh, nice. That fits right in with this token rationalization phase,

**[00:46:27]** which apparently has replaced the token maximization phase.

**[00:46:30]** Well, let's see. Well, now. Right? Right? Tokens aren't getting fewer. They're apparently just

**[00:46:39]** being looked at more closely to see whether they're really productive. They're getting more and more productive. AI produces

**[00:46:45]** more and more cool stuff, honestly. We don't have time left over for that. We have to talk again

**[00:46:51]** about what's actually going on out there. We can deal with that in the next

**[00:46:53]** episodes. So in the last few weeks I've seen insanely strong

**[00:46:59]** use cases in the area of tutorials, explainers, education, where very often

**[00:47:06]** with Claude, Anthropic and an MCP connection that helps the 3D program Blender as well.

**[00:47:14]** helps.

**[00:47:15]** Or rather, when I help, yes, Blender, so the program Blender is used by

**[00:47:20]** the AI to build gigantically good, gigantically cool 3D websites

**[00:47:29]** that have fantastic teaching qualities, where you can look at technology.

**[00:47:35]** Today I still, somehow, it was from the Vercel chief, I think, he posted something

**[00:47:39]** today.

**[00:47:40]** He basically, we have a record player at home, he also rebuilt a record player

**[00:47:45]** with 3JS.

**[00:47:46]** And it runs, you can put different records on it.

**[00:47:47]** That's already awesome, spinning it and hearing the music.

**[00:47:50]** But what's fascinating is that the music doesn't simply come out of the speaker,

**[00:47:52]** but in this 3D model that runs in real time on the website,

**[00:47:58]** basically the actual vibrations of the record are queried,

**[00:48:02]** to then produce the tones again from these vibration things.

**[00:48:05]** That's kind of wild.

**[00:48:06]** And I think we should talk about things like that again in the future.

**[00:48:09]** We could do a proper episode on that.

**[00:48:10]** We'd have to make sure we put enough links for it in the show notes,

**[00:48:13]** because unfortunately we're not a visual event,

**[00:48:17]** just an audiophile event for both of us at the moment.

**[00:48:21]** But I think we have exciting topics there again, what's being done with tokens, we haven't talked about that in peace for a long time.

**[00:48:26]** We could think about, so please not as a rule, but think about whether we do a stretch, also really make the first video on our YouTube channel.

**[00:48:34]** Yes, true.

**[00:48:35]** Yes, because you first have to be very selfless to say, well, nice that we're in your podcast player of choice, do drop by YouTube, then you could see what we're doing right now.

**[00:48:45]** Exactly.

**[00:48:46]** That way we could maybe keep our channels a bit fresh.

**[00:48:50]** Maybe one last tip at the end on token minimization in your personal setup.

**[00:48:56]** What actually helps me save tokens too is a little skill I wrote for myself.

**[00:49:03]** One that takes a topic I'm planning, not only with this one, there's one called QuillMe or Superpower Brainstorming or something,

**[00:49:07]** the one is called that,

**[00:49:11]** but so that your plan is as good as possible.

**[00:49:14]** I wrote myself another skill that researches whether what I'm planning

**[00:49:18]** someone has already written up on Reddit or so,

**[00:49:20]** discussed, and also checks whether on GitHub, license-wise clean of course,

**[00:49:27]** there are already demo implementations, not to copy those demo implementations

**[00:49:32]** per se, but to take them as guidance for a plan along the lines of,

**[00:49:37]** I'm building this myself, maybe I won't fall right into all the traps that I

**[00:49:41]** had paid in for myself, plus Context 7 is a totally great MCP server when it comes to programming languages

**[00:49:46]** and in sum, but you're already taking a breath, in sum already quite

**[00:49:50]** That sounds very cool, and please share the links again, maybe in this episode too, I want to pull out one or two things from there myself.

**[00:49:57]** All I wanted to say, you just announced that in the future humanity no longer has to invent the wheel twice.

**[00:50:06]** But we're two tech nerds here. Of course we reinvent the wheel.

**[00:50:12]** This insight of saying, don't copy it, just look at all the projects.

**[00:50:18]** As I said, always keeping an eye on what is it, MIT, Apache and so on, so that you

**[00:50:25]** don't get into trouble.

**[00:50:26]** Whether you catch all of them is another matter, because some aren't so well documented

**[00:50:29]** or are irrelevant.

**[00:50:30]** This insight, I trust it, is the same topic again as in one of

**[00:50:35]** our first episodes.

**[00:50:36]** Just because the computer said it, we're not at 0 and 1, that's really

**[00:50:39]** not wrong.

**[00:50:40]** But it's still, it looked at it, when I look at it, quite honestly, you know

**[00:50:45]** yourself how I sometimes get stuck with my glasses in front of the monitor, still overlooking enough.

**[00:50:49]** And with the amount it does, let's say the correction is only one prompt away.

**[00:50:54]** And the fact that it can search for it, be it with the help of Perplexity, for example,

**[00:50:58]** or its own search queries, it's astonishing what it finds at that point,

**[00:51:05]** let's say, so that it doesn't stumble over the same mistakes itself,

**[00:51:10]** which you might not think of otherwise. Last sentence? I think by now the models

**[00:51:15]** are so strong too and when you integrate the whole thing, sometimes too many instructions make it

**[00:51:20]** worse. So when it opens that up, this does that, you rein it in, and if you

**[00:51:26]** let it run and let it make a suggestion, sometimes really cool ideas come

**[00:51:29]** out, where you say, we can talk about that, and not beforehand yes, but not that and please

**[00:51:35]** not at all, but make some suggestions, let's discuss, getting into that discussion with it

**[00:51:40]** and so keep sharpening the plan. I wanted to back up once more what you said,

**[00:51:46]** because there was another piece of news that caught my interest this week. And

**[00:51:51]** it was from Ethan Mollick, he reposted it, it's not his study, but he

**[00:51:54]** reposted it. And it was about looking at how well fact-checking is carried out

**[00:52:00]** on scientific studies. And the result was

**[00:52:05]** that humans basically only get it right around 25 percent

**[00:52:10]** of the time and have a chance of really checking the facts.

**[00:52:12]** In contrast to the models, let me look, there a Claude Opus 5 was

**[00:52:17]** tested with 90.8 percent accuracy. The GPT-5-6 from

**[00:52:23]** Solultra with 92.2 percent the best model. That means this maybe also

**[00:52:30]** overestimating of our own abilities as humans, of what we can

**[00:52:35]** actually judge, so to speak. Because just as you say, when I

**[00:52:39]** collect things together now, then I've got my average, yeah yeah, then I've got

**[00:52:43]** my good feel for whether this is AI news or

**[00:52:49]** real news, what's actually correct, that's just how I have it

**[00:52:51]** basically, when my AI brings me news research and things or I discuss something with it,

**[00:52:55]** that I do have a feeling for whether it's right or not, but just

**[00:52:59]** a feeling. Honestly only a feeling. The time when that feeling is smarter

**[00:53:06]** than an AI checking it is over. We have to be clear about that. That's

**[00:53:09]** an exciting topic, I think, that came out of this study again.

**[00:53:13]** That's of course for expert topics, but I think we can scale it down quite easily

**[00:53:16]** to everyday topics, if that's already the case with scientific studies

**[00:53:19]** by now, that AI can actually fact-check clearly, clearly better

**[00:53:23]** than a human ever could or ever could have,

**[00:53:27]** honestly. And if you add to that, and this shouldn't sound judgmental,

**[00:53:33]** that you still meet a lot of people, no matter which

**[00:53:38]** profession, whether trades, digital, IT, office administration, whatever,

**[00:53:44]** that AI exists is one thing. What it means and what it can do is still so

**[00:53:51]** different in people's perception. I still meet people who tell me, well,

**[00:53:55]** translating text, of course I use AI. And I don't want, as I said, to

**[00:54:02]** judge that, because it's quite possible that you simply don't

**[00:54:05]** know it can do more or you've never had the experience that you

**[00:54:09]** can trust it with more, because if you, for example, always work with

**[00:54:12]** the free plans, I know people who were totally appalled along the lines of

**[00:54:18]** which version was that back then, when it was said OpenAI took my friend away, that

**[00:54:22]** was the 4o or something like that. Yes, yes, that was it, I think. They were on

**[00:54:25]** old models and then OpenAI

**[00:54:30]** discontinued the models and then, ah, my model is gone, and somehow took a small

**[00:54:34]** model, because they thought small models are cheaper, yes, but

**[00:54:37]** small models aren't automatically cheaper. That's actually a

**[00:54:41]** fallacy too. And from that side, there are so many different feelings about the

**[00:54:47]** topic of AI. So many different ones from people who say, I'm on top of it, and

**[00:54:51]** maybe aren't at all. Or they say, what do I want with it? That's

**[00:54:54]** all nonsense anyway. Or it doesn't affect me. I'm not in IT.

**[00:54:58]** I do think there's definitely a change in the

**[00:55:03]** working world in IT. We've already had that as a topic, but that's being driven by

**[00:55:06]** management and Covid, which I also churn through quite differently, but I think those are

**[00:55:09]** all stories we want to get to in future episodes. So I'd like to thank you.

**[00:55:15]** Nice that the Death Star didn't get you. No, I managed

**[00:55:20]** to get through those awful, awful medications. Yes, so there the Empire

**[00:55:27]** threw everything into the balance and didn't manage it. Thanks for staying on the

**[00:55:30]** good side, on the side of AI, on the side of our listeners. And with that

**[00:55:35]** I'd say we say goodbye. We wish you a wonderful week, with whatever

**[00:55:39]** events are on the horizon. You keep hearing about new models again here,

**[00:55:43]** but that's also a truism. You hear about them constantly. And I'm looking forward to the

**[00:55:48]** next episode, Jens. Until then, all the best. Leave us a like, a comment. Feel

**[00:55:54]** free to say we're cool. And until next time. Ciao. Until next time. Ciao.

**[00:56:05]** Print Think AI, the podcast from Mark and Jens.

**[00:56:09]** Two technology-loving minds who don't just talk about artificial intelligence,

**[00:56:14]** but live it.

**[00:56:15]** Here you get clear context, real practical insights

**[00:56:19]** and a fresh look at what's possible.

**[00:56:22]** Understandable, critical and always with a wink.

**[00:56:26]** AI for thinking, for smiling and above all for joining the conversation.
