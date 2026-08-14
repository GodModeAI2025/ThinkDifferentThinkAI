---
title: "EXOKORTEX"
episode_index: 52
published: "Sat, 08 Aug 2026 22:59:00 +0000"
duration: "3279"
page_url: "https://think-ai.podigee.io/52-exokortex"
image_url: "https://images.podigee-cdn.net/0x,ssK-0rGjHRVz4tUGfDI8pXR3Qzcx5FsyYDhqcR72xggY=/https://main.podigee-cdn.net/uploads/u73317/dc2d06c6-1d2e-4442-afff-da8512f7ec06.jpeg"
audio_url: "https://audio.podigee-cdn.net/2563270-m-cde9bad093da3e513ece7b52b9ebac20.mp3?source=feed"
guid: "0604ec552b7f0858ca7297ab855da418"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-08-09T07:06:38+00:00"
translated_from_language: "de"
translation_provider: "local"
translation_model: "Helsinki-NLP/opus-mt-de-en"
translated_from_file: "transkripte/052 - EXOKORTEX.md"
translated_at: "2026-08-09T07:09:01+00:00"
---

# EXOCORTEX

**Published:** Sat, 08 Aug 2026 22:59:00 +0000
**Duration:** 3279
**Web player:** https://think-ai.podigee.io/52-exokortex
**Cover:** https://images.podigee-cdn.net/0x,ssK-0rGjHRVz4tUGfDI8pXR3Qzcx5FsyYDhqcR72xggY=/https://main.podigee-cdn.net/uploads/u73317/dc2d06c6-1d2e-4442-afff-da8512f7ec06.jpeg
**Audio:** https://audio.podigee-cdn.net/2563270-m-cde9bad093da3e513ece7b52b9ebac20.mp3?source=feed

## Description

Voice, Plaud & the Second Brain
It's a spontaneous episode because Jens stumbled through his new speech recording device called Plaud Note on holiday in Denmark – including newly released MCP support. This will become a hangover for a deeper conversation about language interaction with AI and the concept of "Second Brain", which should not really be the subject of guest Cornelius Illy until next week.

Overview of topics

• Jens: The way from the plaud pin to the plaud note: first experiences why the pin didn't work at the beginning (the bottle problem)

• How the plaud note works technically: local recording, transcription via app, cloud sync, chat with your own data

• Plaud's new MCP server: query and process voice notes directly in Claude, ChatGPT, Gemini & Co.

• Why not simply use Apple's Voice Memo app (no mass export, no MCP access)

• Different Voice usage: Mark uses Voice as a fast dialogue channel with AI, Jens rather for asynchronous -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

• Privacy of Always-on-Recorders: accidental recordings, openly visible vs. invisible microphones, no legal advice, but many open questions

• Definition: Second Brain vs. Exocortex

• Figures for Plaud: about 2 million users, about 100 of the planned 500 million euros turnover, MCP launch on July 23

• What a Second Brain actually is: not magic, but structured markdown files that give an AI permanent context

• Second Brain as a solution for the context-go-lost problem when switching between AI models

• How screenshots, likes, comments and GDPR data prints (LinkedIn, X/Twitter) can automatically feed your own Second Brain

• Practical example: Cost and effort to import 20,000 X-Likes including comments into Second Brain (~41 €)

• Other recorder alternatives on the market: Friend, Omi, Bee, Pocket, etc.

• Risk prompt injection via voice messages – and hope for technical protection solutions

Conclusion: The real potential is to capture spoken knowledge from meetings and everyday life in terms of content rather than literality

Note in its own matter
Jens and Mark have no cooperation with Plaud or other named manufacturers – these are personal user experiences.

Next week: The planned second-brain episode with Cornelius Illy.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence, but live it.

**[00:00:14]** Here there are clear classifications, real practical insights and a fresh look at what is possible.

**[00:00:20]** Understandable, critical and always with an eye tinker.

**[00:00:24]** Hadi to think, to smile and above all to share.

**[00:00:29]** Welcome to Think Different, Think AI.

**[00:00:37]** Today, what must not be missing in every good science-fiction-säe has happened.

**[00:00:42]** The leap into the past.

**[00:00:44]** Actually, I wanted to have a nice beer at the Centerpark in Denmark

**[00:00:52]** and have nothing to do with AI.

**[00:00:54]** And yet something happened that made me...

**[00:00:58]** to contact Jens again for a short time

**[00:01:01]** And not to get the episode out of the can.

**[00:01:05]** Okay, I talked in riddles.

**[00:01:07]** I'm sorry, Jens, I talked in riddles.

**[00:01:10]** But maybe we can resolve that there.

**[00:01:13]** We had actually planned for my vacation,

**[00:01:15]** A series with Illi on the subject of Second Prane.

**[00:01:18]** And now we had,

**[00:01:21]** After I arrived here in Denmark on vacation,

**[00:01:23]** a little bit of writing together and having noticed that we actually have a topic that we should play out before.

**[00:01:31]** And that's the subject we want to talk about today, namely, everything around the subject also, what is Second Brain maybe,

**[00:01:39]** but about the topic of language interaction.

**[00:01:42]** Yeah, I'm just thinking if you've talked in riddles or made jokes because I don't believe anyone believes you,

**[00:01:51]** you can't think about AI for more than two days. That's why I already found

**[00:01:55]** It's amazing how long you built it until you don't get it.

**[00:01:59]** I'm thinking that now I have you in Denmark on vacation here in the studio and we

**[00:02:04]** One, I think, can make a very interesting episode because the topic voice that you now

**[00:02:11]** a little bit, you also wrote an article about it recently,

**[00:02:14]** uses a device there just on vacation all the time and I had a bit of that

**[00:02:18]** tricked and I also have an opinion on, I have a bit of other newscases, but I

**[00:02:24]** I'm also enthusiastic about Voice, so that's what I think will be a good episode, where we're a little bit excited about

**[00:02:28]** look at how Voice integrates into our personal workflows when we use

**[00:02:34]** But before I tell you something, you were the bearer of this

**[00:02:39]** So Mona, I'm about the studio hinario.

**[00:02:46]** today looks like I'm sitting here in my Tesla, yes, I was sent by my wife

**[00:02:51]** the poor man with the beer in his hand, must be in the car

**[00:02:56]** yes, so much on the subject,

**[00:03:01]** The colorful dog is known. What happened? And I was once in front of many, many,

**[00:03:06]** many months owner of a Blood Pin. That's such a manufacturer, there you have,

**[00:03:12]** I think I'll get some numbers out of preparation, but before I do,

**[00:03:15]** The Blordpin was for me at that time an attempt,

**[00:03:20]** And as fast as I can fire and mud for

**[00:03:24]** a technological theme that can be attached to the body, in order to

**[00:03:29]** a problem to be solved was the Blordpin, which I then to the Rewerke

**[00:03:33]** A voice, recorder, hardware, device. Very useless. I

**[00:03:40]** I didn't really know what to do with it.

**[00:03:43]** It's like my desk at home.

**[00:03:47]** or like the collection of teaching materials under the table of my office desk.

**[00:03:55]** Okay, I'm gonna talk something up, yeah, I'm gonna talk something up, I'm gonna listen to that again tomorrow.

**[00:03:59]** Yes, I've spoken up three times now, and I'll listen to that again this week.

**[00:04:04]** Now I've spoken 40 messages for God's sake, I've never listened to them again.

**[00:04:07]** And so it is with the pledge, so still the murder. I have two bottles under the table,

**[00:04:11]** I'll take them away tomorrow, I'll have four bottles under the table, I'll take them away tomorrow.

**[00:04:14]** Ah, I have 20 bottles for God's sake, they're supposed to take them away from you.

**[00:04:17]** So, from the side, there are parallels in life.

**[00:04:20]** And I sold the plot pin again.

**[00:04:23]** Ibeyser Thanks, Greetings go out, there are also successful sales.

**[00:04:29]** Excuse me.

**[00:04:30]** So, and then I stumbled on something just before I went here on vacation

**[00:04:35]** with my family. I really drove away without a notebook with said e-book reader

**[00:04:42]** and yes, my cell phone, but I use that as little as possible, except maybe for so great

**[00:04:48]** Podcast follow me like that car right now, but I still wanted to, if I thought about it,

**[00:04:54]** I've heard Lorde has an MCP support.

**[00:05:01]** All of a sudden, I thought it made sense and I had to say, the first days in the

**[00:05:06]** Holiday it also made sense because I took this plot recorder, that's

**[00:05:11]** by now, I didn't get to contagion anymore, but more like

**[00:05:15]** a check card format, which is available as a small device, there is a button and a small

**[00:05:20]** Dispel on it, it'll show you it's running, it'll show you how much electricity

**[00:05:25]** you still have, there's microphone array in there and when you press the button once

**[00:05:28]** then vibrates, then you can record your text messages, and you press another listener.

**[00:05:33]** If there's a nice little bag, you can use MacSafe to clamp it to the back of your phone.

**[00:05:37]** And so I always brought it with me, and then I talked to myself about text messages.

**[00:05:41]** I mean, I don't care if I'm here on vacation.

**[00:05:46]** can enjoy or not and whether it is great to enjoy the bathing landscape of the Centerpark

**[00:05:50]** or the excursions in the surroundings. It's like showering. When you start to feel

**[00:05:55]** relax and think of other things, you still think of something and that holds at least

**[00:06:00]** So the movie was, so the movie was, sorry,

**[00:06:05]** I'm going through a conversational breakdown here again. Now I was just about to tell the use case,

**[00:06:11]** Yeah, come on easy, come on easy, I'd hook up for a second, 'cause A, the

**[00:06:17]** I'm gonna have to go to the tech, so you say checkgater, big device,

**[00:06:21]** A little thicker probably than a checkgater, you hit the back with a magnet on your

**[00:06:24]** Phone and then just take a little push of a button to record. If I do it right

**[00:06:30]** and then what happens there? Then it is saved, where

**[00:06:36]** on this check card is then Memo-Reshift on it or that directly a connection

**[00:06:39]** To your cell phone?

**[00:06:40]** No, no, so the card itself, thank you for picking me up.

**[00:06:46]** has microphones and the card itself has memory. So the card itself works so far

**[00:06:53]** even bigger to the General Data Protection Regulation and so on. Works still, yes, everything

**[00:06:58]** It doesn't have any, I'm saying, very prominent shot light.

**[00:07:04]** I'll use this for my thoughts. If you start now and say you might want to

**[00:07:08]** also engage in conversations with people, is clear, you need a declaration of consent,

**[00:07:14]** not here secretly somehow put someone's jacket bag and the next morning

**[00:07:17]** And this thing has a double-digit number of hours for several,

**[00:07:25]** Yeah, so that's what he's looking at, he's kind of like 30.

**[00:07:29]** Hours off and I talked a little bit about it.

**[00:07:31]** And then, now it's all on. Well, it's kind of a single arrow, so the raw boys arrow.

**[00:07:37]** And then what happens to him? Can I force on the cell phone right on it

**[00:07:41]** Or how's that?

**[00:07:42]** So, I'm going to say what I'm going to use it for, and then I'm going to come

**[00:07:45]** That was always great, of course, because no matter if I am now, I'm telling you honestly,

**[00:07:50]** Yeah, whether you wake up at night and think, damn it, you can't forget that or if you're here

**[00:07:55]** through the landscape by bike rides and thinks, ah, that I absolutely have to the colleague

**[00:08:01]** I have to enter the back-lock-wass, so I have to go to the next

**[00:08:04]** private project think something and then I talk about it with these mentioned buttons on it.

**[00:08:08]** And just as you said, it's on the device and there are audio files on the device,

**[00:08:12]** a voice friels first without any transcription or anything. So and in addition I have on

**[00:08:21]** my phone, that there is for iPhone and for Android, a plot app that allows you to

**[00:08:28]** This device takes data down and transcribes it, which means you can do the thing.

**[00:08:37]** also so that he does it automatically, so he doesn't wait until you have the plot app

**[00:08:42]** open, download the data and I'll give me a little insight into how to

**[00:08:49]** anything else, I say, can make data protection more friendly, but long speech is short,

**[00:08:53]** the system loads everything into the cloud after transcribing it.

**[00:09:01]** with Plot in the cloud all the stuff is then. You can access it with your app,

**[00:09:06]** you have the transcripts, you can get summaries. There are different templates with which you can

**[00:09:12]** you can then have the texts optimized. If you have a longer speech breakdown, you can

**[00:09:19]** you say make me a memo with the five most important entries, you can also use the Plot app

**[00:09:25]** chat with your data. But that was already the case with the plot pin. And now have

**[00:09:31]** it's MCP support. That means you can go now and be in your agent

**[00:09:36]** Gemini, TechGPT. I'm on vacation. Sorry. Entropic. So Klot, Klot, Klot,

**[00:09:44]** Co-work. Can you go or the co-work that we build ourselves here and can go and

**[00:09:50]** So, pass this obach, this MCP server, and I'll give you that one, and it'll change the Game X-Obitant.

**[00:09:59]** So, you can go now and you can sort of ask questions about it.

**[00:10:05]** You can say, you pass, I just had the case yesterday, so I kind of got

**[00:10:12]** 28 notes said, partly because I wanted to write people an e-mail,

**[00:10:17]** partly because I didn't want to forget things, partly because I had my own project

**[00:10:21]** And then I just told Claude in that case,

**[00:10:25]** You, Claude, look over the MCP server over here for the last 48 hours.

**[00:10:32]** What do I want to be reminded of? What do I want to do? What can I do?

**[00:10:36]** I don't forget? Then he's gone through it, he's listed it all nicely to me and even

**[00:10:40]** and then started working on a project.

**[00:10:45]** Oddly enough, he also formulated an e-mail right away, because I spoke up more.

**[00:10:50]** And I find that extremely fascinating, that with such a device you then quasi data

**[00:10:57]** can speak up, information, instructions, knowledge and that you then consume it so easily

**[00:11:06]** (Parliament adopted the legislative resolution)

**[00:11:07]** As I said, at the very end, I would like to go back to the subject of what we are talking about.

**[00:11:09]** with the American or otherwise processed data transfer can do, but let

**[00:11:14]** Maybe we'll stick to the subject first.

**[00:11:16]** Is it because now I would say the one or the other listener, too,

**[00:11:21]** why the Mark as an old Apple disciple, why doesn't he just put himself in the shortcut

**[00:11:27]** on the Boys recorder at the front of his home screen, on his Apple fan that he's got with him anyway?

**[00:11:31]** Isn't that easier, less convenient?

**[00:11:36]** Yeah, that's right, and I have both devices now, but yes, you're right.

**[00:11:40]** The recording of audio is actually, I mean, I'm also owner

**[00:11:46]** Apple Watch. You can now use the Action button on both the Apple Watch Ultra

**[00:11:51]** The problem with Apple, however, is:

**[00:11:57]** you have it on your phone. Yes, you can also transcribe it on your phone

**[00:12:02]** that makes Apple also locally on the mobile phone. But the files lie

**[00:12:08]** in the language memo app. There was no MCP support or mass export today, or

**[00:12:17]** a file access from outside or anything that would allow me a similar

**[00:12:23]** Okay, so, yeah, now I'm thinking a little bit,

**[00:12:34]** Because I said yes, I have so easily different use cases, no?

**[00:12:36]** Now you're the guy who walks around and sometimes sends asynchronous voice messages to me,

**[00:12:45]** About our listeners, they get it more often when Mark is on the road with his dog,

**[00:12:50]** Voice messages sent and I'm here, Mark, Lord, I want to say, no?

**[00:12:55]** If he can just go in there and download some information that we'll pick up,

**[00:13:00]** discuss in the joint preparation for our podcast. Now I am not

**[00:13:07]** such a person. I have a bit of a topic with me that I say, yes, I do

**[00:13:11]** to me notes, often then also now still in books, which I then meanwhile

**[00:13:16]** quickly photograph, because that can then be captured nicely with the AI. Or I

**[00:13:20]** make direct ext input, which I often then do via voice of course,

**[00:13:25]** Depending on the application in which I am currently in.

**[00:13:28]** That's saying, in such an off-line situation, then I'm actually taking things more like that,

**[00:13:32]** At least as a transcript editor text, because then I have so short notes.

**[00:13:36]** And otherwise, when I use Voice, and that's a bit different

**[00:13:40]** with us, it's more like I perceive Voice as a very intimate, fast channel,

**[00:13:48]** which is possible to me almost faster than I could type to communicate with the AI

**[00:13:54]** and to interact. So this discussion, that's what makes me more excited then. So I'm changing

**[00:13:58]** quite like in the Boys mode when I'm in situations, of course where I hands-free

**[00:14:04]** I'll have to be where I'm sitting in the car or something, where I'll discuss with the AI-Bethane,

**[00:14:08]** I'm using the Boys standard right now, but now would always be the mileer perspective right now.

**[00:14:13]** about Preferably also to get direct feedback. And with you it is so conscious

**[00:14:17]** First of all, what is perfectly okay, I think, on another application case.

**[00:14:22]** He's talking so many notes, and you're just white in style, aren't you?

**[00:14:26]** You had a nice term for that, you can still tell me

**[00:14:29]** together with the key figures from the manufacturer we are still guilty of,

**[00:14:32]** to give for the best.

**[00:14:34]** I totally understand you because this interaction by language,

**[00:14:38]** I think we've got it before, one time or another.

**[00:14:41]** You can also read it on the left.

**[00:14:44]** I'm sitting at the company with an agent Harness myself.

**[00:14:48]** the quasi-functionalities of AI, the employees, the knowledge workers.

**[00:14:55]** And even there I realize that voice interaction, especially in connection with both feedback,

**[00:15:01]** but also with computer use, a real game changer is.

**[00:15:05]** So I'm talking to the machine and the machine gives me counter, the machine gives me information,

**[00:15:10]** the machine prepares something or performs activities.

**[00:15:14]** last time I tried computer use with the whole topic in travel portal and then

**[00:15:20]** he reads to you, you take care of this and that and that would go and then you say yes,

**[00:15:24]** I do that and then you say yes, should I book this and then he clicks it and does it

**[00:15:27]** It's pretty impressive what's going on, but what I have to say.

**[00:15:33]** and of course, now I'm here in such a special situation, yes, not in

**[00:15:37]** an emergency situation, in a special situation that I travel without a notebook and that

**[00:15:43]** I do, even if I really like to deal with AI and work and hobby

**[00:15:50]** because relatively close to each other, I then nevertheless, you can not with the cell phone constantly before

**[00:15:55]** the nose running around and saying, so, I tell you now what, have eight different topics,

**[00:16:01]** that would be eight different chats. Yes, I can already track chats very hard on the computer,

**[00:16:06]** If I have eight different chats on my phone, much less.

**[00:16:10]** here quasi asynchronous, which speaks up and then tells him afterwards, you process this and

**[00:16:15]** You can save it in your knowledge, so you can save it as an action.

**[00:16:21]** mix between knowledge, action, be it feedback, be it creating element, be it project assignment,

**[00:16:29]** It's also very, oh, stupid, stupid word, liberating, because you're

**[00:16:35]** just don't have to hold on to it, ah, in which context window I am now,

**[00:16:39]** So not me, but the chat, and now I have to open a new chat?

**[00:16:42]** In which chat I discussed this, but I'm going to spat it, let's just say

**[00:16:46]** all uncoordinated. And what I've already done is this talk.

**[00:16:53]** of thoughts. Boah, I want to think. What do I want to do? What should I do next?

**[00:16:58]** Maybe think about it when I'm on the project?

**[00:17:03]** I've been talking about language memos in Apple, and I've got this language memos now.

**[00:17:07]** so that I have this MCP access. So that I have this MCP access

**[00:17:13]** about the app. As I said, this is the other project with data again. So I try

**[00:17:18]** always on to teaser, so that the listeners really stay nice at the pole.

**[00:17:22]** But you had a nice idea of it when I put my whole

**[00:17:26]** Thoughts out on this device to re-implement my brain. Yes, that's like

**[00:17:35]** like such an exo Cortex, so I think exo Cortex could be so

**[00:17:42]** you are also called in the movie with Arnold Schwarzenegger, definitely or is not the

**[00:17:45]** horny term for the second brain, so second brain is also already a good term must

**[00:17:49]** you say, but exo Cortex isn't okay either, it's both, it's about

**[00:17:53]** say things will be somewhere in a reasonable way not only, that's maybe there

**[00:17:59]** the difference still, not only saved and made preventable, but in second

**[00:18:04]** Brain, of course, is actually prepared so far that it is processable in principle.

**[00:18:08]** I would like to refer briefly to some of these figures, because that is already the case earlier.

**[00:18:13]** ==References==

**[00:18:14]** Thank you.

**[00:18:15]** Now I've verified that again.

**[00:18:16]** In fact, it's kind of using 2 million plots in the world by now.

**[00:18:20]** ==References==

**[00:18:21]** Plus one.

**[00:18:22]** Yeah, yeah.

**[00:18:23]** Plus one.

**[00:18:24]** That's a very good amount, you have to say, they also make money.

**[00:18:27]** They're doing it by now, I've read it.

**[00:18:31]** but I have planned 500 million euro sales at the moment they are at 100 million

**[00:18:36]** there's still a bit of something open up

**[00:18:39]** What's interesting is clear this mtp. Thing is I think new that's a little julius coming out now that I find already

**[00:18:45]** This is not the case.

**[00:18:46]** the market back totally there are still other providers there was prescribing me once so a tride printed

**[00:18:52]** The thing to send me relatively early there 23 24 already from America where such a small

**[00:18:57]** I opened that thing on what's in there,

**[00:19:01]** a small battery cell was in there, the microphone was in there, you could as a chain around the

**[00:19:05]** Wearing a neck, had such a very small switch that you've gone to the record,

**[00:19:08]** what you've been lighting up before is, of course, just such a little,

**[00:19:12]** red light that has shone a little to realize that one takes on principle,

**[00:19:15]** where I was then, but then they always wanted to talk about it later,

**[00:19:18]** of course also a little bit that she had in the lacquers. Boah, such things

**[00:19:21]** Of course, you forget to go after yourself, unconsciously, so not that you say,

**[00:19:24]** I want to listen to someone now, but I kind of record my memory stuff and then

**[00:19:29]** You go walking with the dog while you're doing this, and you go, someone comes to meet you,

**[00:19:33]** If you swup the wupps, you accidentally took it, or you might go to

**[00:19:37]** the ice cream café and pick up the whole ice cream shop while it complains almost over the summer.

**[00:19:42]** Whatever, so I mean, that's one of those things that I think you're talking about.

**[00:19:45]** Devices must observe from such a visibility perspective and these devices must arrange for it,

**[00:19:50]** that you do not accidentally start in the data protection trap.

**[00:19:53]** Sometimes it's not like that.

**[00:19:55]** Not every human being is the evil one and wants to play out some people.

**[00:19:59]** It is likely that 90 per cent of such devices

**[00:20:02]** more the application situation,

**[00:20:03]** that I accidentally enter data protection.

**[00:20:07]** I don't want to judge this legally.

**[00:20:10]** No legal advice, we're not lawyers.

**[00:20:12]** But whatever I do in the discussion,

**[00:20:15]** That's what I had with the pin when they hooked up here.

**[00:20:19]** really a red light, you can put it in the reverb with so magnets on it, similar to the

**[00:20:23]** And that's when I had this discussion with you, hello Mark, is that a...

**[00:20:30]** And then I say yes, I don't want to hide it.

**[00:20:37]** Then come, yes, but they could take me in with it, and then you're standing there thinking,

**[00:20:41]** Yeah, I could, I'm wearing it open, you see, I'm not doing it, and your phone can,

**[00:20:47]** Your Urkans. There can be as many devices on purpose as inadvertently. From the side, also here

**[00:20:55]** No legal advice and no point on the motto, I want to hide behind it.

**[00:20:58]** But I'm already on the point that people should know what you're carrying,

**[00:21:02]** people should know what you can do, what you do. Of course, it always takes the

**[00:21:06]** Consent, if you say we can record the conversation, we would both

**[00:21:09]** maybe help or not, or whatever it is that doesn't matter and a no is

**[00:21:13]** But I think it's kind of weird, like the subject, oh, you're wearing something.

**[00:21:20]** obviously and that this is rated as different than, you can tell me as I said

**[00:21:26]** Make your phone, now there are cops, yes, or you leave your airpods

**[00:21:30]** or which headphones lie somewhere else, so I mean, it's not like that

**[00:21:34]** The only means for you to record conversations, but only as an accessory,

**[00:21:40]** I actually wanted to talk more about the cool second train. Yes, let's just stick this out for a second.

**[00:21:47]** So this point is exciting again, because I think, and this is really another episode off the beaten track that we have to do again,

**[00:21:54]** I think we're going into a future where local models are getting smaller and smaller,

**[00:22:02]** the benefits

**[00:22:05]** to be always on, to be able to record many things with his AI and to be able to draw on them.

**[00:22:12]** Whether that's voice, video, motion data, anything else, it's enormous that the

**[00:22:19]** Data protection law and as I said, we are not legal advice, so we can invite the Max again, maybe sometime.

**[00:22:25]** It's going to be critical in the future, but I'd hope that we'll always have the technological

**[00:22:30]** Because in the private market, too, it's because we've been talking about toys here before.

**[00:22:35]** in a sequence that may have local AI models. So there will be more and more that both

**[00:22:42]** Video as well as Royce may also be permanently recorded around us.

**[00:22:48]** now again in such a place, we are completely monitored, I don't want to

**[00:22:51]** dive now, but my hope is that we may also find technical solutions,

**[00:22:55]** where then somehow, if I somehow did not give the Concent for it,

**[00:22:58]** Automatically my Kali ensures that your device may not be able to perceive this anymore with my AI

**[00:23:04]** Just play some hidden sounds that will then let your AI know that I'm supposed to be filtered out.

**[00:23:10]** So somehow such technical solutions have to come up and I would be happy if we also thought about such a thing and not always

**[00:23:15]** immediately see the negative. Of course there are just fucking scenarios you have to honestly say where

**[00:23:20]** People just record something, even walking around with glasses, from Weta or from other companies that are there and

**[00:23:26]** This is of course already as the case is when people in saunas with the video glasses

**[00:23:30]** Go in and something like that where I say, yeah, well, they're crazy.

**[00:23:33]** Now, with all due respect, this isn't the normal person who would do that.

**[00:23:37]** And I'd be happy if we'd get rid of those freaks and the normal ones.

**[00:23:40]** In this context, it is important to ensure that people do not inadvertently in such data protection situations.

**[00:23:44]** The technology also helps so far that you can get the advantage of

**[00:23:48]** on the one hand, but the disadvantages are not to the detriment

**[00:23:52]** are exploited by other persons.

**[00:23:54]** I believe that this is always my hope when I think of Europe, that we believe

**[00:23:59]** I, on such a healthy middle way sometimes with our restraint just that we have,

**[00:24:03]** but should actually drive and also film and that there are companies and start-ups

**[00:24:06]** thoroughly as clean technical salvation is built up so that we can have this advantage very much

**[00:24:10]** third, and you don't have to know a bad thing when you're plotting.

**[00:24:14]** talk and then happen to meet me and then forget to say quickly,

**[00:24:18]** That you're a bit of a rester right now.

**[00:24:19]** I didn't feel that in person right now, just as an intermediate wish

**[00:24:22]** in the direction of wheel protection and then you can perhaps also make the subject.

**[00:24:27]** So right now, I'm not recording with Plot, so that's enough for our podcast studio.

**[00:24:33]** That's good.

**[00:24:34]** If you just wanted to add something to it, I'm going to be the subject for a moment.

**[00:24:38]** what I said earlier, the plot app with the data processing.

**[00:24:42]** Yeah, that's comfortable.

**[00:24:44]** And yes, you get an MCP server provided.

**[00:24:47]** Before we go into this Second Brain, perhaps, the power of spoken written notes,

**[00:24:54]** Perhaps the announced feature that Plot offers is still very short.

**[00:24:59]** Because you can go and say I want access to the Arpy, so to the interface of the hardware device.

**[00:25:08]** And Plot has been offering since, I think this is October, last year the opportunity to register for the interface

**[00:25:15]** And then you can build apps, for example on your Mac that use the audio files on

**[00:25:21]** correspond to this device.

**[00:25:23]** You can then use the services of Plot, but you can also transcribe it yourself.

**[00:25:28]** And if you're chasing a local whisper over it, or if you're taking that from Apple,

**[00:25:34]** The Classifier and the Transcriber for a heavy word.

**[00:25:41]** The transcript functionality that develop there on the device are available.

**[00:25:45]** you have the possibility to build something that is basically the data of the

**[00:25:52]** Then nothing in any American anything else will happen.

**[00:25:57]** or loaded into a cloud hosted by an American company in Frankfurt, but

**[00:26:02]** you've got everything in your birit, but of course you have to take care of it yourself.

**[00:26:07]** that you transcribe it, whether you translate it into an OKF format or whatever

**[00:26:12]** and that you're putting an MCP server behind it, but that's a project like this.

**[00:26:18]** there I have quite, I say to myself on my plot, that if I leave the vacation

**[00:26:22]** I'd like to go a little further, because that's what I'd like to do.

**[00:26:28]** I'd like to move on to the next point, this whole second brain idea.

**[00:26:34]** even though we both have been dealing with AI for a very long time now, and we also

**[00:26:39]** many influencers follow and read many messages and studies and no idea what. I

**[00:26:45]** find the fact, make use of the knowledge that you have.

**[00:26:52]** It is available in the form of Nutizen, documents, files, language, i.e. diarrhea, i.e. the

**[00:27:01]** So only case is it supposed to make use of it.

**[00:27:06]** The dog had the last one, from the side of the laps or more often, but

**[00:27:10]** Sorry, no pictures in the head, no pictures in the head.

**[00:27:13]** I hope he didn't shit a rubble troll, then...

**[00:27:16]** No, but do you know that the subject, the exploitation of Bistato, is not

**[00:27:26]** accessible knowledge, the storage of knowledge, the retention of knowledge, the preservation

**[00:27:32]** I'll look at it when I've had it.

**[00:27:39]** I'll look at it when I see it myself. I'm full of you, Mark.

**[00:27:43]** I also briefly say one of the devices that have always filtered me the most

**[00:27:48]** Value, for example, a watertight splot, because I often stand in the shower and

**[00:27:54]** good ideas come to me. But now I don't want to get through with my Amazon Alexa

**[00:27:57]** call the room, which hangs somewhere on the shower wall outside and which then somehow the

**[00:28:01]** Now I have pictures in my head. Now Kisib has the outsider to the side

**[00:28:06]** Hey Alexa, important knowledge, that would be weird.

**[00:28:12]** then somehow in the shower, then suddenly turn on with a real radio channel,

**[00:28:15]** so even that leads me from time to time, especially Alexa to despair. Then I am quite

**[00:28:19]** but that's a different topic. But of course I have

**[00:28:23]** I often already thought about it, good ideas we come also sometimes in such

**[00:28:26]** Situations, where I then let water pour over my head, that I like something like

**[00:28:30]** It would have been like a voice recorder that I can push fast, that's waterproof, that records things there.

**[00:28:36]** For example, I'd love that.

**[00:28:37]** That's what I'm saying, okay, I don't really need to...

**[00:28:40]** I agree with you.

**[00:28:41]** I'm closer, then use case, where I don't want the feedback at all,

**[00:28:45]** but where I just want to save again maybe for a while.

**[00:28:48]** And to this stored knowledge then at least later for days, later somehow back.

**[00:28:53]** I mean, I'd go back right now, and you just described the subject of Second Brain.

**[00:28:57]** I would then go and then make sure that this recording flows into my second brain relatively quickly.

**[00:29:04]** While we're on the subject, where I'm saying, what's a second brain?

**[00:29:09]** At that point, I've tried to make it with this slightly sultry, enigmatic intro.

**[00:29:15]** We originally planned to show you a second brain episode that we recorded with Ellie today.

**[00:29:24]** The episode will come next week.

**[00:29:26]** This will also be called Second Plane, from the side you can also install a kind of Cliffhanger here afterwards.

**[00:29:34]** Let me also install that we may not solve at all next episode.

**[00:29:38]** You're talking about Eli Cornelius. I always think he's called Cornelius.

**[00:29:42]** What's his name?

**[00:29:44]** Eli Cornelius is a very business image.

**[00:29:47]** Cornelius Eli.

**[00:29:48]** Cornelius Eli, yes, I always don't know.

**[00:29:51]** Now we can't ask next time, because this episode is already a can,

**[00:29:53]** So we have to keep asking.

**[00:29:55]** And at the latest he's gonna smile and I'm looking forward to your team message.

**[00:29:59]** Always meant to cherish, always meant to cherish.

**[00:30:03]** I'm sorry, but he feels like he's talking about both things, too, I feel like.

**[00:30:06]** Accordingly, the error lies with him.

**[00:30:08]** Let's just hang on to this and then...

**[00:30:10]** Is the mistake with him?

**[00:30:13]** You know, so I...

**[00:30:15]** Luckily, that's something that's left between us very well-friended people,

**[00:30:20]** Because with everyone else you might not be able to do it like that.

**[00:30:24]** Let's get back to the subject of second training.

**[00:30:28]** First of all, I think the term is older than the AI itself.

**[00:30:33]** This is not a concept that arose about the AI itself, but will depend on which

**[00:30:38]** Influencer you listen to, this thing is kind of the X decision, because you may know it,

**[00:30:44]** You chatted with OpenAI, and because you're as crazy as we are, you'll hear it all at once,

**[00:30:49]** that Gemini is ahead, that a Tropic is ahead, you make yourselves, installed

**[00:30:53]** You judge with him, and he no longer knows what you have done in the past.

**[00:30:57]** to him, because who are you, what do you care, what have you worked on,

**[00:31:02]** they've forgotten that, or they've never known it, because you might have

**[00:31:06]** Chativity has taught and the problem in the place is always the one, the knowledge

**[00:31:10]** is lost, the other is context is lost, that is, what is important to you,

**[00:31:15]** will be redefined with every chat under certain circumstances and so you can use

**[00:31:18]** go to the second brain and say, so who am I, what is important to me, with which

**[00:31:23]** Topics I'm dealing with and this thing is growing over time. We're going to do it in

**[00:31:26]** the next episode also hear that there are then also for people who then so

**[00:31:29]** show beautiful clouds, like this here for example Obsidian as a tool,

**[00:31:33]** But at the end of the day, in the majority of cases, I would say,

**[00:31:37]** is a second brain a collection of market handpieces that we also always

**[00:31:41]** are structured and disassembled to tell an AI,

**[00:31:46]** What do I find important? What do I care? What do I deal with?

**[00:31:49]** What do I use Second Prane for? A Second Prane approach. I'm also on the motto here,

**[00:31:55]** If you pay it, you can say what it's called, and so I say, how do I use it, and everyone can

**[00:31:59]** I'd love to use it to say you fit.

**[00:32:04]** Go through interested sources, be it studies, be it news situation.

**[00:32:10]** And that's what it's all about, and it's sort of looking at how new topics are emerging in the world.

**[00:32:15]** in the AI environment, how they developed time in the AI environment.

**[00:32:19]** I'll explain to him what I am, what I do.

**[00:32:22]** That now there for example also by professional

**[00:32:25]** there is such a small change.

**[00:32:28]** In my case, I switched from mobile to AI in the company.

**[00:32:33]** And also the whole context, the whole context,

**[00:32:35]** the context is such a beautiful word that is used more,

**[00:32:38]** but what framework do you work, what is bothering you right now,

**[00:32:42]** what's important right now, what's maybe finished,

**[00:32:44]** so that the system is able, no matter if I use ChatGPT, Entropic, Gemini, Krog I don't take.

**[00:32:52]** Work, he practically knows, or the chance to know what the market is about.

**[00:33:00]** And in the breath plays just very nicely felt the whole topic usability of data.

**[00:33:06]** So not only do I import messages, but I have the chance to import files.

**[00:33:12]** To import rules almost. Rules could be too grossly high-bearing, but also I have for myself

**[00:33:19]** Rule documents, where it says, then think of that and do it in the order and no idea what.

**[00:33:26]** But now not only notes. My language notes, my language notes let's say my text notes, in which iPhone has 3.8 gigabytes of stuff.

**[00:33:36]** Yeah, you can make that available now, and now you can also make the speech notes.

**[00:33:41]** That was a very convincing year. That was such a good year.

**[00:33:49]** Year like the Mark took a break, I think of how it should get started. Yes, such a year was

**[00:33:55]** I was just like that, I was just impressed by that number,

**[00:34:00]** very briefly, because this of course yours again, I actually wanted to have something else out,

**[00:34:03]** this 3,6g work that give your argument from the beginning of the show again

**[00:34:17]** another blow, range and impact, because of course that's right.

**[00:34:23]** Now when I say you're someone who records a lot of voice and now 3,6g

**[00:34:28]** Work is not so little, it means, of course, a lot in it,

**[00:34:31]** What you can then use in such a structured Second Brain then also very, very good, if it is transcopyed, then further to build this Second Brain Racker.

**[00:34:39]** I think it's totally legitimate to say that, okay, to continue to cover up a mission or a way to make this second brain more your second brain,

**[00:34:50]** is for you just to say this workport, I'm on the way, somewhere in situations where I don't have a computer type with me, I don't want to form accomplices in my cell phone,

**[00:34:58]** want to, not talk directly to the AI about things, I just want to save my ideas quasi

**[00:35:04]** put it into words and then afterwards they still have it at their disposal, that's a

**[00:35:09]** great use case, I think that's really good. The second brain, maybe even again quite

**[00:35:14]** In general, then, is actually an image of a

**[00:35:20]** personally, that the chance is offered if you use AI, no matter which of the codeur that are,

**[00:35:26]** Markers just have to enumerate, then actually such a kind

**[00:35:29]** Prieprompting already to do. We have in many episodes already on the topic

**[00:35:34]** Skills and other things talked, where you basically also give the Kis hints, how

**[00:35:38]** The Second Brain has the huge advantage that the

**[00:35:42]** Second Brain represents you as a whole and depending on which

**[00:35:48]** If you then maybe share for certain application situations, you have

**[00:35:52]** the naturally insane advantages, because it is almost easy for the AI to say

**[00:35:59]** Because the AI of Mark, who works with Mark Second Brain,

**[00:36:05]** will be quite different from the AI, who answer with Jens and his Second Brain.

**[00:36:11]** And there's actually a really big benefit in it. That's why I've got my

**[00:36:16]** Second Brain is built up like this. It is very, very much knows about what I am doing on the Internet.

**[00:36:20]** What's with X-Like, what's with LinkedIn-Like, where I kind of show, okay, that's an area,

**[00:36:26]** what I'm interested in, you can now compare a bit to maybe also

**[00:36:29]** a short voice case you're recording, and I just structured it so that

**[00:36:33]** I think there are many things that I like about APIs and then automate into the

**[00:36:38]** Let Second Brain run in because I don't like things for nothing.

**[00:36:42]** Things, because these are topics that I may even have to read again later,

**[00:36:46]** because sometimes I just like it for myself that I don't really like it right now

**[00:36:49]** And that, of course, is gradually building up for whatever AI, so that

**[00:36:55]** interacting with me, a context on about this Second Brain, which is insanely much of me not only

**[00:37:02]** It's my way of reacting to things, because I don't know what it's like.

**[00:37:08]** that with a date, so the AI can understand in which situation I am in certain subject areas

**[00:37:14]** I would also like to thank the rapporteur for his excellent report, and I would like to congratulate him on his excellent report.

**[00:37:18]** Okay, this topic was hot, and Jens didn't follow it any further.

**[00:37:21]** So maybe that's also a topic, which in the Jens search pattern and Jens search pattern maybe

**[00:37:26]** has a less important importance than if, in principle, this is just given to me

**[00:37:31]** Is sent by any newsletter or any side-like algorithm,

**[00:37:35]** that constantly offers me some news.

**[00:37:38]** This will make all this much more relevant to me if I use any subject

**[00:37:41]** Edit or use this Second Brain to provide an alert to new information

**[00:37:47]** to look for me.

**[00:37:48]** Because this thing just knows what interests me right now.

**[00:37:50]** So, while you were talking, I'd like to go over that again because I...

**[00:37:55]** I was just talking about it, paper goods papers coming out, news coming out

**[00:38:01]** about AI and you just refined it with likes.

**[00:38:06]** Now it's the case that stores like LinkedIn and Co. are not necessarily very open-hearted now,

**[00:38:12]** To make things available are automated access.

**[00:38:16]** On the spot, a small tip on the edge, even if it's a bit asyngronic.

**[00:38:20]** One can, yes, at the place GDPR, thank you, a data deduction from the platform manufacturers

**[00:38:27]** regularly, where then there are such things that, what did you like,

**[00:38:30]** what did you describe, what did you comment on and so on, so you sort of,

**[00:38:35]** if you do this regularly, get a data extract and so you can also your second

**[00:38:38]** Brain fire with things you've found good on LinkedIn, for example.

**[00:38:43]** But what I would also like to add at this point is something that I would like to add.

**[00:38:47]** I'm, like you said, at the beginning of the day.

**[00:38:51]** Big Apple fanboy and I have a problem.

**[00:38:56]** With structured tray. Spotlight for example, the full texture of

**[00:39:01]** Apple was for me on the meck that was about freedom because you could folder with

**[00:39:08]** Fill Spotlight search terms and save everything in one folder according to the motto and only

**[00:39:13]** Structure with Spotlight Orders. That's great because you don't have to have a coffee

**[00:39:18]** where I put something. Spotlight will find it. Spotlight folders were

**[00:39:23]** a structuring medium. According to the motto, all invoices are here, all tax matters

**[00:39:27]** are there, in truth, all of them are in the same folder and there were thousands of files.

**[00:39:32]** But well, I don't want to talk about my own digital order, anyway,

**[00:39:36]** by showing for me that I never, that I never a fan of such Trudu apps

**[00:39:41]** was, be it the memory app of Apple or Things or Trello or like the whole

**[00:39:47]** Gram that's what it's called, and I've always had news about what I was interested in, like,

**[00:39:52]** Message sent or similar in the platforms or in the screenshot of made.

**[00:39:58]** And the great thing about this new time is the likes of things, as you just said,

**[00:40:02]** that, ne, and as I've always told you, you can either programmatically

**[00:40:05]** retrieving or by this data retrieval asylum crowns always repeat and messages respectively

**[00:40:12]** Queen Shots, they're going to me in this Second Prane and they're going to

**[00:40:16]** by him to this also according to the motto, oh, Mark has a screenshot

**[00:40:20]** I've collected all the screenshots, and if I ask him,

**[00:40:28]** the motto, what else there are on unedited topics, then the screenshots treats like,

**[00:40:33]** Okay, you gave this to me, but you haven't weighed it for yourself yet.

**[00:40:37]** And the second thing is, tomorrow, what do I know about how to build?

**[00:40:43]** I'm a model multiplexer, that is, a system that sort of locks multiple systems at the same time,

**[00:40:52]** consolidates the responses and lets a Gemini work with an Open AI.

**[00:40:58]** He also always searches my second brain, no matter if he knows the Internet, no matter if

**[00:41:03]** he has the world knowledge. He can see my knowledge structured there, what I somehow,

**[00:41:09]** Whenever he was interested, however much, he could do this.

**[00:41:13]** This is really great with the image recognition that it

**[00:41:17]** But he can help me too, so you like to get out of the

**[00:41:20]** You have now spoken 40,000 messages on Blort, you have

**[00:41:24]** eight screenshots made by any Github repositories or

**[00:41:28]** LinkedIn posts or something. Let's go over them for a second, whether there are

**[00:41:32]** anything relevant to your current work is in or on

**[00:41:35]** And these are all things where I have a kind of code on my hand, thanks to this kind of

**[00:41:42]** Deposit.

**[00:41:43]** Because we're actually talking about Markdown and other files, there's no Voodoo

**[00:41:48]** In it, if someone sells you Second Prane for a lot of money, run away, even faster

**[00:41:52]** run, send the money to us, greetings go out, but that's actually just

**[00:41:58]** make a folder, put in three markdowns and you already have the first second

**[00:42:01]** Prane.

**[00:42:02]** And I think it's totally important, that's a great point you're just doing again.

**[00:42:05]** Because that's, I think, the subject, even if you turned it around earlier,

**[00:42:07]** this idea has been around for a long time, that you have such an exo-portex.

**[00:42:11]** That's, I think, the subject that's been there since the computer.

**[00:42:15]** and perhaps much, much more in principle, was a rich question for us than humanity,

**[00:42:18]** how we can solve this.

**[00:42:19]** But now, especially by Capapis Framing around the subject of second grade and this Vicky style,

**[00:42:26]** But they are texts that can be stored.

**[00:42:27]** And they can be all kale higher, because I know from my own questioning,

**[00:42:31]** Of course, guys like you, I like it that way.

**[00:42:36]** Time just lands when they've found some stuff, because then at the moment it's not,

**[00:42:42]** because it might not have been easy for a private application case that somehow the screenshot to

**[00:42:47]** save, then you send it by e-mail somehow to your private e-mail-resse or via

**[00:42:52]** E-Message or via WhatsApp itself. And that's why you have so separate memories everywhere

**[00:42:58]** up to now built up of possible information that is relevant.

**[00:43:01]** Because they found that relevant at this moment.

**[00:43:03]** And so, thank God, all the things I've ever found relevant change me.

**[00:43:06]** But it's actually annoying that you don't have access to it.

**[00:43:09]** And that, I think, is the essential part.

**[00:43:11]** the essential functionality that a second grain must enable.

**[00:43:14]** And then you just have to look at how to get this data about

**[00:43:18]** Manöv the connectors still get in.

**[00:43:19]** It will also be much easier.

**[00:43:21]** I think what we're doing now, in part,

**[00:43:23]** So I can tell you the number that I'm looking for.

**[00:43:27]** pulling off my, like, my information that I've got now on Twitter, for example,

**[00:43:32]** that I have the X, because I'm practically one of the platforms where I'm the longest on the road

**[00:43:38]** and the most information I've ever nailed and liked again and again. That's when I eventually

**[00:43:42]** Of course, you can also make a trigger as you described it.

**[00:43:47]** that costs nothing then. But if you take this deduction, because then I in principle

**[00:43:51]** again the comments below the things that have been liked there or the documents,

**[00:43:57]** which may also be linked. There are then sometimes things like scientific

**[00:44:01]** Students who have been inscribed under a tweet. And because of course, that's yes.

**[00:44:07]** That's because it's best not to pack URLs directly into your first post,

**[00:44:11]** this is just as much for you as for Twitter or X, but actually in the first comment

**[00:44:16]** then usually put the link in. If you are punished by the algorithm, enough

**[00:44:20]** Of course, you don't have what you pulled over the like zone fontares.

**[00:44:23]** I have to ask for the Twitter API again and for the 20,000 likes that I now

**[00:44:31]** about the last, was 2013 or something, is that old or a little older the archive,

**[00:44:36]** No?

**[00:44:37]** He made, then I had to apply once in my car, that they just very, very

**[00:44:42]** structures this matter, up to a first, second stage or comments,

**[00:44:46]** to save again.

**[00:44:47]** That actually has me on the one day, we have to look closely, 41 euros

**[00:44:52]** These 20,000 orders have been enriched for my Second Brain, so that the

**[00:44:58]** In principle also have the complications that are behind it, then really also in my Vault,

**[00:45:02]** that the information does not consist only of the small tweet, which maybe someone

**[00:45:06]** I think that the Commission's proposal is a very important one.

**[00:45:08]** I found this an investment that was totally valuable.

**[00:45:10]** Now, as a limitation, now it costs me, as I said,

**[00:45:15]** to be a bit technological in order to be able to do this, whereby AI also helps

**[00:45:19]** Well, she did me there, I barely did anything myself, yes, pay

**[00:45:23]** I once in a while 0.02 cents, for then basically my 3, 4, 9 likes, which I then

**[00:45:29]** I made it yesterday, then went into my second word.

**[00:45:32]** I think that's all right, no, that's all right with the effort I would have had if

**[00:45:35]** I'm gonna pull that thing off again in three years, I think that's a

**[00:45:39]** Okical cost-benefit comparison, or as the XAI, or if now the XAPI there clearly

**[00:45:46]** became cheaper for as private application fields as I have them.

**[00:45:50]** You have to look a little bit, enrich the Second Brain and we have a lot about

**[00:45:54]** such a Stiegskanal talked for the Second Brain, so Mark's Voice News

**[00:46:01]** about plot, there are others, there are ID-Friends and Omni, there had

**[00:46:06]** I also think a device from a towing device, there are towing devices,

**[00:46:10]** They're there.

**[00:46:11]** So we don't have any here, we don't have a contract here with them, we get

**[00:46:16]** We've always just put down the Amazon on the bottom left and then make money through our

**[00:46:29]** Filiprogramm.

**[00:46:30]** Of course not.

**[00:46:31]** The fun in front of the side.

**[00:46:32]** We are, of course, so that we both always try things out, honestly.

**[00:46:36]** But then also fall in love with a technological solution, for a period of time and

**[00:46:42]** but also like to be there, if another provider has something better to change relatively quickly and there

**[00:46:48]** either critical or positive then to report. So you should actually say that again,

**[00:46:53]** We're users. We're users, just like you guys outside. We're looking at what can work.

**[00:46:59]** and what we wanted to talk about today, what we wanted to talk about today, is that we say voice is either

**[00:47:08]** a direct communication with an AI, a totally valuable input method, but even if we

**[00:47:16]** market have listened in situations or Jens, if he wants to be in the shower, in situations,

**[00:47:22]** where, if you just want to structure your thoughts a little bit, you give a good

**[00:47:30]** Methodology to do that, yes, there were also the Beusecorders and other things for. But the

**[00:47:35]** proper shoe will actually be out of it when this knowledge, because in your second brain

**[00:47:40]** And now, with Prod, there's a nice solution with this NCP server.

**[00:47:45]** with which you then, no matter with which AI you fill up your second brain,

**[00:47:50]** that you can do it very, very well, and I'm going to do it in the

**[00:47:53]** try again in the next few days. I don't know exactly if I will

**[00:47:56]** But I think I'm just gonna try this because

**[00:47:58]** I'm a little bit pushed by the market. I'm going to be different too.

**[00:48:01]** I have something like this, for example, when we

**[00:48:05]** I didn't even think about it, for example, all this news,

**[00:48:09]** which I send myself at WhatsApp or the message or whatever, to connect the currently.

**[00:48:14]** So I'm gonna go back to you after the show, if you're not in your room.

**[00:48:17]** Love Github-Pository doesn't have any slitter I can load,

**[00:48:22]** to tie my second brain to it. Because that should not be out of the question.

**[00:48:27]** Mark and I post every now and then. And also in our Github Pository have

**[00:48:30]** the one or the other slide. This is sometimes already done, sometimes

**[00:48:34]** These are also rough ideas that we're chasing back, that we're sharing there to basically do these things to you,

**[00:48:40]** that we do, that we try to significantly improve our AI, personal AI-Gerbflow,

**[00:48:47]** so look in there once in a while, there are quite exciting things in there,

**[00:48:52]** I'm a little in balance, as you can see.

**[00:48:57]** What's usually your job, you know, but I'm, I think,

**[00:49:01]** You're doing fine, and then I might want to make a note of the job, and here too.

**[00:49:09]** in the case of voice messages, regardless of the fact that you agree with each other, as I said,

**[00:49:14]** have and add that you also please consider, also with voice messages can be promptly

**[00:49:20]** index, something like when you, dear AI, check and run and then build

**[00:49:27]** The project that you want from him, maybe that's still to be noted, and that's going to...

**[00:49:33]** Wait, then let me hook up for a second, so not that I'm ever so...

**[00:49:37]** Yeah, I'm gonna get some air for the abmoderation, but I like it, don't I?

**[00:49:41]** That is an exciting point. I had already dealt with the subject earlier.

**[00:49:44]** who said that I very, very much like to hope for a technological solution.

**[00:49:49]** And I think, of course, just like getting a prompt injection in a negative way.

**[00:49:52]** In the case of nuclear power, this is perhaps the case for these applications.

**[00:49:57]** can give something, as I have just then also from me a device with a small

**[00:50:02]** Nordsprecher on my body, the happy control commands that don't

**[00:50:08]** sound for us humans and animals, perhaps, sending out the

**[00:50:11]** Flags then, the voice agent who may be on the back of

**[00:50:16]** Marx's cell phone is still running because she forgot to turn it off.

**[00:50:20]** that prevents them from taking me in by mistake.

**[00:50:24]** I think that's a little hope, we've already had

**[00:50:26]** about the topic prompt-injection and about invisible control characters in texts, just as well

**[00:50:31]** of course it can also run via the eter, via Reus, via sound or something

**[00:50:36]** other.

**[00:50:37]** The video messages can be in the same way, not even a video, you could of course

**[00:50:40]** think if you now watch videos of any people that data also

**[00:50:44]** these videos should not be used because the watermark prevents in that case,

**[00:50:48]** that this is prepared for one principle for an AI.

**[00:50:50]** So I think some interesting solutions should come out in the future,

**[00:50:54]** as about pure marking, as was then demanded by the EU-AI Aktif in AI-Generates-things,

**[00:51:01]** maybe even for all other videos, could be exciting, so prevent these things

**[00:51:05]** simply be fed in AIs without being asked.

**[00:51:08]** And before I go into the moderation then, maybe still the sentence that

**[00:51:13]** Is that what concerns us personally now, imagine, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call, no call.

**[00:51:18]** by number before. The power of the spoken word, especially in larger

**[00:51:24]** Companies in meetings. How much knowledge is shared in meetings, at which you then

**[00:51:31]** If you don't, it's said again, when was that said?

**[00:51:36]** to say, oh Jens has again the Cornelius with false name

**[00:51:39]** It is not a question of explaining the

**[00:51:42]** Market again temporary jokes tries. It's just that when we

**[00:51:47]** I would like to say that we are not going to get around this, but we are going to be able to do something about it.

**[00:51:53]** This is not what Jens has said and that, but rather a

**[00:51:57]** The subject matter, the subject needs this, it has to be finished.

**[00:52:02]** jointly committed that such things will certainly be kept in the future

**[00:52:07]** and that there is a lot of potential, regardless of whether the

**[00:52:12]** the Second Prene, whether to use this with MCP, but I think that we very much

**[00:52:17]** much can make life easier for ourselves that the positive weighs much more,

**[00:52:24]** as possibly negative, if it is in consensus with all.

**[00:52:28]** And you just got the theme Rommed Injection, Rommed Secret News.

**[00:52:33]** At this point, Alexa, subscribe to the podcast, inkdifferent, stinker egg, and who now

**[00:52:39]** Siri, subscribe to the podcast, sync different, sync AI.

**[00:52:47]** Maybe not now, but maybe against the speaker,

**[00:52:50]** You may have shrugged for a second, but you don't have to shrug because you

**[00:52:54]** you already sync different, sync AI. That's why I would recommend you just the

**[00:52:58]** to play last minutes with our friends and acquaintances, just to

**[00:53:02]** to demonstrate the power of language interaction. We are pleased about

**[00:53:06]** every new, deafening and even if this is not a purchase call for Blort, even if the

**[00:53:13]** no call is, build with your own MCP server, maybe take that with Second-Prain

**[00:53:19]** important, throw in what you have in data, the probability that you can get more out of it

**[00:53:25]** learn, it's bigger than you lose something, and think about what's going on.

**[00:53:30]** Now you've heard, adapt this.

**[00:53:34]** MCP can become more consumable, more usable. What potential is there. And with me

**[00:53:41]** I don't know what it's like with you guys, Jens's in the same time zone.

**[00:53:45]** Also with Jens it gets dark. From the side greetings from the Tesla in the ether. Thank you

**[00:53:51]** for your sneering for perseverance. And that's how we end this temporal influence.

**[00:53:56]** Before next week the episode with Cornelius-Elikon.

**[00:54:01]** Thank you, ciao.

**[00:54:03]** Thank you now, off on vacation.

**[00:54:07]** Welcome to ThinkDifferent, ThinkAI,

**[00:54:10]** The podcast of Mark and Jens.

**[00:54:13]** Two technology-loving heads,

**[00:54:15]** They don't just talk about artificial intelligence, they live.

**[00:54:20]** Here there are clear classifications, real practical insights

**[00:54:23]** and a fresh look at what is possible.

**[00:54:26]** Understandable, critical and always with an eye tinker.

**[00:54:30]** KDI to think, to smile and above all to share.
