---
title: "Wie KI unser Arbeitsleben verändert!"
episode_index: 27
published: "Tue, 17 Feb 2026 09:28:10 +0000"
duration: "3195"
audio_url: "https://audio.podigee-cdn.net/2360415-m-6d3d5c3e28d769e1c76a37c25379928f.mp3?source=feed"
guid: "a16109cc4a10cc37c66b3c63c19b2f4e"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T20:55:58+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/027 - Wie KI unser Arbeitsleben verändert!.md"
translated_at: "2026-04-29T12:08:26+00:00"
---

# How AI is Changing Our Work Life!

**Published:** Tue, 17 Feb 2026 09:28:10 +0000
**Duration:** 3195
**Audio:** https://audio.podigee-cdn.net/2360415-m-6d3d5c3e28d769e1c76a37c25379928f.mp3?source=feed

## Description

How Artificial Intelligence is turning our work environment and software development upside down. Between pressure for change, curiosity, and real practice.
In this episode, I talk with Klaus Rodewig LinkedIn and Alexander Heusingfeld LinkedIn about how Artificial Intelligence is changing the way we develop, test, and operate software. We discuss why classical role models, familiar programming languages, and beloved processes suddenly become unstable – and what that means for us as developers, architects, and decision-makers.

Together, we look at real aha moments, hurdles in everyday life, and the rapid progress of tools like OpenClaw and Craft-Agent. We ask ourselves how we, as humans, can keep up with this speed, which skills will count in the future, and why lifelong learning is gaining a new dimension now. Anyone who wants to know what working with and in AI teams really looks like and what opportunities and challenges await us should tune in.

Podcast
Conversations about Software Engineering

## Transcript

**[00:00:00]** A disclaimer at the beginning. All statements from me and my guests are our personal

**[00:00:06]** opinions and do not automatically reflect the views of our employers.

**[00:00:10]** Welcome to Think Different, Think AI, the podcast by Mark and Jens. Two technology-loving
 
**[00:00:20]** minds who not only talk about artificial intelligence but live it. Here you'll find clear
 
**[00:00:25]** classifications, real practical insights, and a fresh perspective on what is possible.
 
**[00:00:30]** Understandable, critical, and always with a wink.
 
**[00:00:34]** AI to ponder, to chuckle at, and above all, to discuss.
 
**[00:00:44]** A warm welcome to a new episode of Think Different, Think AI.
 
**[00:00:48]** Today, we're out without Jens.
 
**[00:00:51]** He's celebrating, what? Carnival, Kölralaf, oh, I'm from Hesse, I have no idea.
 
**[00:00:57]** But now I'm sitting here alone, yet I've still brought support,
 
**[00:01:04]** namely not one guest, but two. One of the guests we've actually had here before.
 
**[00:01:11]** Klaus Rodeweg is back with us today and he will be joined by Alexander Häusingfeld.

**[00:01:19]** And I would simply like to ask you to introduce yourselves briefly, who are you, what do you do, and then

**[00:01:25]** let's dive into the topic, everything related to the world of work in the context of AI.

**[00:01:31]** Yes, I am Mr. Klaus. I think I've actually been here two or three times and I know the market

**[00:01:39]** for a terribly long time. I already said that last time. We have a shared

**[00:01:43]** iOS background, we've given talks together and committed terrible apps.

**[00:01:47]** Giving talks together meant he was tinkering on stage while I had to come up with the

**[00:01:52]** script, but let's move on.

**[00:01:56]** That already falls into agentic work, right?

**[00:01:59]** It's great.

**[00:02:00]** So, in my profession, I deal with security and AI, as both are, in my opinion,

**[00:02:08]** inseparably connected, meaning by AI I mean the part AI, formats,

**[00:02:16]** AI, Edit Development.

**[00:02:17]** I would now only refer to it as Genetic AI or AI-Base-Developer, since one can no longer speak of help

**[00:02:26]** but rather, and we will probably talk about this today,

**[00:02:30]** the AI will simply take over significant parts of the development process.

**[00:02:36]** We also have a second guest in the round.

**[00:02:39]** Alex, would you like to say a few words about yourself as well?

**[00:02:41]** Yes, then once again thank you for the invitation, dear Mark.

**[00:02:46]** My name is Alex Häusingfeldt. I am also a podcaster on the Conversations about Software Engineering Podcast.

**[00:02:53]** And I am Klaus's colleague at Vorwerk, previously also at the Elektro-Werken.

**[00:02:59]** I helped to build the Cookie-Doo, the recipe platform.

**[00:03:03]** And before that, I spent a lot of time in software architecture, consulting, software development. 

**[00:03:09]** And we hope to discuss a bit today about how software development

**[00:03:14]** so has changed in the next months, or how it has also changed in the last months.

**[00:03:18]** Now it's time for a commercial break, because you mentioned the name of our work,

**[00:03:24]** the Vorwerk, which makes this beautiful Thermomix.

**[00:03:27]** And I am responsible for ensuring that the Thermomix is safe and that we will use AI with you in the

**[00:03:32]** future.

**[00:03:33]** And I hope you all have a Thermomix.

**[00:03:37]** But Mark, you wanted to say something.

**[00:03:39]** Yes, I was just thinking about whether I should, well actually I wanted to add a podcast by Alex to the show notes.

**[00:03:45]** Maybe we can also get a link to your shop, so that the corresponding products can be purchased.

**[00:03:51]** But let’s see what happens anyway.

**[00:03:53]** You already hinted at it, in the sense of how AI changes work life or the lives of those,

**[00:04:00]** who deal a lot with IT, looking especially at software developers.

**[00:04:05]** In preparation we threw a few nice headlines at each other,

**[00:04:11]** which we can take as a red thread through today’s potpourri of conversation.

**[00:04:17]** The first one that came up for our introduction.

**[00:04:20]** What, AI, is something changing?

**[00:04:22]** No, so, is it good, is that to me practically

**[00:04:27]** whether in software infection, whether in infection, wherever,

**[00:04:30]** wherever text is worked with, whatever.

**[00:04:33]** Isn’t this all just science fiction and demo stuff and doesn’t this all really work

**[00:04:38]** properly yet?

**[00:04:39]** Do you know that?

**[00:04:40]** Or is it, of course, in your situation, everything is always different, that's clear too.

**[00:04:44]** But now, hand on heart, do you know that or what does it look like?
 
**[00:04:48]** Yes, I have to eat my hat now, because that wasn't that long ago.

**[00:04:52]** I had a passionate argument about this particularly with Alex,
 
**[00:04:58]** about how we will work in the future, and the dispute arose over such simple things as which
 
**[00:05:04]** metric we actually want to attach to our software development in the future.

**[00:05:09]** This was at a time when I was actively working with GitHub Copilot and was already
 
**[00:05:14]** quite amazed at what was coming out.

**[00:05:16]** But I still couldn't imagine that this is basically a turning point that not only
 
**[00:05:24]** turns programming itself upside down, but the entire development cycle as well.

**[00:05:27]** And now I've spent the last few weeks very intensively working with Claude Code.

**[00:05:34]** By the way, I am totally thrilled with the integration in Xcode 26.3, just a side note.

**[00:05:42]** And that was an eye-opener moment, where I realized, okay, in the future we will no longer measure
 
**[00:05:47]** lines of code or as test metrics, but we will simply measure how many
 
**[00:05:51]** apps a person puts out in a week.

**[00:05:53]** And that’s, yes, I can understand that well.

**[00:05:57]** There are such things. Some things you just have to have seen or experienced to know what they impact.

**[00:06:05]** I mean, both of you are kind of, I would say, affected by my weekend escapades, not because I’m somehow partying with you, but because you sometimes have to endure it when I stumble upon something and then we share information in our little chat bubble.
 
**[00:06:27]** With information I mentioned, that wasn’t long ago, or Saturday night, when you both wrote to us,
 
**[00:06:35]** Wow, I’m so angry, I’m about to throw my Mac Mini against the wall.

**[00:06:39]** I wanted to switch Open-Claw, back then it was still called that, what was it called again?
 
**[00:06:42]** Open-Claw Bot to the local model and the thing completely broke.

**[00:06:47]** I’m going to go watch a movie now and after an hour you then wrote, oh, he just sent me a WhatsApp message,

**[00:06:53]** that I have actually called it a day, but he has restructured everything for me, asking where I was.

**[00:06:59]** Yes, I actually reported on that in the last episode here on the channel, and it was Telegram and not WhatsApp.

**[00:07:05]** Yes, so you are basically involved for better or worse, but it’s also insane how quickly everything is turning right now.

**[00:07:12]** So, if I had been sitting with an N8N half a year ago, I honestly wouldn't even try to roll the dice for N8N today.

**[00:07:21]** Yes, that's somehow already off the table for me, I don't know.

**[00:07:25]** The challenge I see is that I think we don't really bring our colleagues along with it,

**[00:07:30]** in between.

**[00:07:32]** So, I see it in myself that I'm looking, okay, do I have a test system on which I

**[00:07:41]** can test this, what are the use cases I want to test, and while

**[00:07:46]** other colleagues are just jumping in and actually they are also

**[00:07:52]** involved, then others have already landed with Craft Agents for example and say,

**[00:07:58]** but that is, well, that is much more sensible than Openclaw and all the installations,

**[00:08:04]** that I had from Openclaw, I don't need them anymore. And if you ask them about N8n,

**[00:08:07]** then it was like, wait, that was in 2025, right? So the speed at which we actually

**[00:08:16]** have usable tools and at which we replace them overwhelms many, and I'm back to

**[00:08:23]** the point Klaus just made. I have been trying for some time to introduce software architecture

**[00:08:30]** principles like Build for Replacement into my colleagues, into our

**[00:08:39]** development teams, because in classical software education you have things like

**[00:08:45]** don't repeat yourself and you have to find abstractions and you have to make things reusable,

**[00:08:52]** and getting this classical software education out of people is really hard.

**[00:09:01]** So this no, that's not your baby, that's Pets versus Kettle, that's Kettle,

**[00:09:06]** it’s not meant to be malicious, but it’s just a lot and it just goes through and

**[00:09:12]** I think we need, at times when we should change our diet,

**[00:09:16]** maybe a different image, but you know what I mean.

**[00:09:19]** So this image replacement.

**[00:09:21]** What's wrong with pizza?

**[00:09:23]** What?

**[00:09:24]** I don't understand that.

**[00:09:25]** What's wrong with pizza?

**[00:09:26]** I meant Airpads vs. Kettle and I don't know how you got to pizza with both, but

**[00:09:30]** it doesn't matter.

**[00:09:31]** Good.

**[00:09:32]** Pizza.

**[00:09:33]** But that's a whole different topic.

**[00:09:36]** Yes.

**[00:09:37]** I would like to throw in a provocative tea for the rest of the podcast.

**[00:09:41]** I predict the end of recyclability, I predict the end of software architecture,

**[00:09:49]** not the overarching architecture, but something like app architecture.

**[00:09:54]** And I also predict the end of formal languages.

**[00:09:56]** I found that quite funny. I actually had the other day with a few colleagues,

**[00:10:00]** who looked at me completely incredulously, like,

**[00:10:03]** but I'm now essentially an expert in a language, what he means,

**[00:10:07]** Let's take PRP, for example. Let's take the language that

**[00:10:11]** decides at runtime, am I a number or a text? Excuse me if it was so necessary

**[00:10:15]** it was. No, no, it was. And I'm there, yeah? Let's say you're in now, yeah? You know

**[00:10:20]** yes, you can recite that, you can read it, you’re the expert here. And then

**[00:10:26]** one can ask the question, do you really think that’s going to happen? That has never been the case.

**[00:10:32]** And the grace of my early birth came to my aid because back then

**[00:10:39]** I actually had something like assembly language at my fingertips and then eventually something

**[00:10:46]** weird like PRP and Turbo Pascal came along, as the entire Quad standard was called at the time. So

**[00:10:52]** we already had that, just with the difference that, I’d say, it took longer and

**[00:10:58]** secondly, the language then became more understandable for humans, so that humans didn’t

**[00:11:04]** have to, I mean, writing assembly is funny as a party gag today, but no one really wants to

**[00:11:10]** do that today, maybe for the Thermomix, I don’t know.

**[00:11:13]** But maybe no one wants to do that for normal software development now.

**[00:11:16]** I can see Alex is twitching, he probably wants to say something, but what I’m

**[00:11:19]** wanted to get out, is this, this look in the eyes of the people, because they then somehow
 
**[00:11:24]** realize, I don't want to talk about impacts now.
 
**[00:11:28]** towards, we don't have to make everything modular anymore, but also a good portion
 
**[00:11:35]** of disposable software. You built something, it's there, it works, and in half a year
 
**[00:11:40]** it might work differently. That's something where you also have to take the people
 
**[00:11:44]** along, because technology, let's be honest, can handle it.
 
**[00:11:47]** The crucial question for me is or rather, when I talk with
 
**[00:11:54]** colleagues or also with people in the network about AI. It quickly comes up
 
**[00:12:00]** at some point, I ask, well, but what is actually still my job? Why am I
 
**[00:12:06]** even here? And this awareness, and you just brought up the assembler example,
 
**[00:12:13]** I have a different anecdote about that, I found myself, not even last week, actually,

**[00:12:18]** where we were discussing it with a colleague.

**[00:12:22]** The disputed ones. No, that was something else.

**[00:12:24]** No, that was the other one.

**[00:12:26]** Where we talked about the fact that we said, well,

**[00:12:29]** metrics that we used to have as quality standards,

**[00:12:34]** and said, well, the quality of the metrics is important,

**[00:12:38]** they are no longer so relevant today.

**[00:12:41]** Because why were they important before?

**[00:12:43]** Well, because people had to manage to understand these metrics,

**[00:12:47]** to understand what it should actually do end to end? What is the part that I have here in mind,

**[00:12:53]** that I'm currently processing, keyword Context Window, and what is its contribution to the end

**[00:13:00]** to end? And just like it was back in assembler times, I can remember, when I started with high-level languages in the late 90s,

**[00:13:06]** I also had two colleagues who programmed in assembler

**[00:13:12]** and told me, ah, with high-level languages, that won’t catch on,

**[00:13:16]** that won’t prevail. We need efficient programs and nothing is

**[00:13:22]** as efficient as assembler. And that kind of efficiency is only relevant today in niches,

**[00:13:29]** so there are niches where you need it. I don't want to get into brake technology,

**[00:13:36]** but there are just things where you're already in the sub-millisecond range, where you say,

**[00:13:41]** no, it needs to be somehow very, very efficient so that the

**[00:13:47]** response can happen.

**[00:13:48]** And then Java came along.

**[00:13:50]** Yeah, well.

**[00:13:51]** That’s my point, do you believe, exactly.

**[00:13:54]** Exactly.

**[00:13:55]** And microservices in the brake pads, exactly, exactly.

**[00:13:58]** I understand, of course, if that's one thing, I can now somehow whip up software at home

**[00:14:04]** quickly, I sat down this morning

**[00:14:08]** to work on a piece of software that helps me, I don't even know why I have such hobbies,

**[00:14:14]** but recognizing Pumped Injections in the Guilds and stuff like that. So I put together a little piece

**[00:14:19]** of software with an agent, to just try out how well that works and

**[00:14:25]** you basically build your little helpers. For a business application, you probably

**[00:14:30]** would still have to go through two or three extra loops, that's still the wording, what

**[00:14:33]** to find out. I really want to start before I might roll this out to clients or internal processes

**[00:14:37]** But nevertheless, it is exactly heading in this direction and bringing people along.

**[00:14:42]** on a journey. How do I work with something like that? How do I handle it? Yes, I mean that the

**[00:14:49]** some say Vibecoding, others say Agentic Engineering. Depending on how you shape the role again,

**[00:14:54]** this is certainly a shift in the world of work. On one hand in the

**[00:15:00]** empowerment of people, but also on the other hand in the question, what is my job? What am I allowed

**[00:15:06]** to do in the future? When do I start looking again? Do I let go? Do I determine

**[00:15:12]** me? No idea, what? There will definitely be a lot of changes, right?

**[00:15:15]** Absolutely. I see nodding. The nice thing about an audio podcast, you have to confirm the nodding

**[00:15:20]** also audibly. I see nodding. And I think it's also hard for people

**[00:15:26]** really said to accompany this way, because everything is so fast-paced that

**[00:15:29]** one honestly has no idea. What will happen in three months again?

**[00:15:33]** the next thing that comes up that turns everything inside out, because I don't know how it is for you. 

**[00:15:39]** With this Craft agent, the last time I dealt with it wasn't that long ago.

**[00:15:45]** Before that, there was Open-Claw, and before that, Cloudcode, and before that, I don't know what.

**[00:15:52]** And sometime before that was Gemini. It's all happening really fast.

**[00:15:57]** Yeah, you see, you see a problem that we've had since IT exists,

**[00:16:02]** that one always tends to rush in, I mean companies

**[00:16:09]** tend to rush to throw solutions at problems without having thought it through first.

**[00:16:14]** And I believe the question, the answer to the question, what role do I play as

**[00:16:21]** I can of course answer the individual ones in this process.

**[00:16:24]** But I think, to be a company, you would need to take a step back now

**[00:16:30]** and consider what agentic working means for us, no matter if I do this

**[00:16:35]** with NLN-orchestrate, with Open Claw, or with Tralala, it really doesn’t matter. 

**[00:16:40]** The worst that can happen is that you just take old working methods

**[00:16:45]** and have incorporated AI, which we have actually always seen in the history of IT

**[00:16:50]**.

**[00:16:51]** Bad processes have just been digitized, and it was still just as bad afterward, and now it has

**[00:16:57]** just become digital and it's more expensive. They might run a bit faster,

**[00:17:01]** but it's not a solution. And yes, I think what you're touching on with the question,

**[00:17:05]** what is my personal task? You mentioned this earlier, I believe, Alex,

**[00:17:12]** that the ability to unlearn and to learn is becoming increasingly important. I still remember,

**[00:17:19]** when I graduated from high school, which is already a year or two ago. It was always said, yes, there was

**[00:17:26]** even the theme park Germany, which the then Chancellor called it, and it was said,

**[00:17:30]** we need to prepare for lifelong learning. Yes, and now it's also added to lifelong

**[00:17:36]** unlearning, which I believe is an even greater challenge, because something has

**[00:17:41]** you said earlier, Alex, that getting things out of our heads, which has many,
 
**[00:17:46]** psychological facets. So, you want to become personally obsolete. Perhaps you've built up knowledge over decades.
 
**[00:17:54]** And now you realize, oh damn, everything I’ve built up over decades, I mean, you have, we both have published a lot.
 
**[00:18:03]** I've written many books on Epic Infection. Now I look at code, and I don’t need to read a single book.
 
**[00:18:09]** to read, and a finished solution comes out.
 
**[00:18:11]** And what skills do I actually need for that?
 
**[00:18:13]** I don't think they are the kinds of skills that are currently being postulated,
 
**[00:18:18]** like, oh, someone has to read this source code and check everything,
 
**[00:18:23]** if it’s correct.
 
**[00:18:24]** That's a typical human self-aggrandizement.
 
**[00:18:28]** If the LLM, the code from the out-of-LLM field, is good, and if
 
**[00:18:33]** I then add another layer on top and have it checked, then I know that
 
**[00:18:36]** it's good, and I don’t need to look at it as a person afterwards.
 
**[00:18:39]** Especially since many of the tasks that you can do, like for example, in
 
**[00:18:43]** using a linter, can also be done by Cloudcode, from my perspective it’s relatively
 
**[00:18:50]** important that we look at what are today’s things that
 
**[00:18:55]** people still value, and many value, for example, their role designation, that
 
**[00:19:01]** they say, I am a developer and proudly so, exactly, but I find that,
 
**[00:19:06]** I find that difficult because it’s not my role designation that defines me, but
 
**[00:19:12]** the things I do and for which I feel a passion for you, so in that sense
 
**[00:19:18]** a role is always a temporary position I take, a responsibility that I
 
**[00:19:22]** assume and that can change tomorrow and yes, what’s important to me,

**[00:19:28]** is a, what do I actually contribute to the end result, what is the end result, can I

**[00:19:32]** I can, so I would like to have contributed, I want to contribute and on the

**[00:19:39]** other hand, who am I working with on this, does it bring me joy, does it fulfill me. That sounds

**[00:19:46]** maybe a bit sentimental, but that is immensely important to me. I know,

**[00:19:50]** that you mean that I get up in the morning and know I'm working with people who

**[00:19:54]** who A are just as eager for it and B are also competent in contributing to it

**[00:20:02]** parking.

**[00:20:03]** But I do believe that it often sounds like one knows better, one is

**[00:20:08]** part of this machinery oneself and also affected, involved, yes.

**[00:20:16]** Nevertheless, if I look back just briefly, when I started at MBW

**[00:20:21]** I couldn't form a coherent sentence in front of more than three people. I was more

**[00:20:24]** So, the basement kid developer. That eventually changed. Fortunately, I no longer develop

**[00:20:29]** not because AI is now at the door, but because I found something else with the

**[00:20:33]** professor. But still, there are people who, I

**[00:20:39]** would say the topic of software development, software architecture, the beauty, understandability

**[00:20:43]** of code, the cracking of nuts, which previously might have been approached with

**[00:20:48]** an eternity of studying Stack Overflow and nights full of beer and rum, coming up with some stuff

**[00:20:54]** that were totally cool. And now suddenly, I would say the

**[00:20:59]** colleague, the student, whatever, comes around the corner, has somehow written three cool POMs

**[00:21:05]** and maybe achieves a better result in perception or in the speed at which

**[00:21:11]** a goal is reached. It might not be the cleanest architecture behind it, but

**[00:21:15]** no one is really interested anymore. Yeah, right. I wouldn't be a programmer today either

**[00:21:20]** necessarily. Although the ability to see things in a larger context,

**[00:21:26]** remains unchanged. So, what I just said about the end of software architecture. You

**[00:21:35]** don't need to discuss whether you build an iOS app with Viper or MVV, Pralala, like

**[00:21:41]** you know all these, we used to debate them to death back then,

**[00:21:47]** that's all irrelevant. But a complete architecture, if I can also test it that way.

**[00:21:51]** But in the space, we're still discussing it, right? Yes, exactly. A complete architecture of

**[00:21:56]** embedded controllers, from the motor, from the heating in the Thermomix to the cloud via

**[00:22:02]** mobile app, you'll still need a bit of experience for that, although I

**[00:22:09]** would say, with the speed at which this AI is learning, we shouldn't rate ourselves too highly now.

**[00:22:14]** That too will architecturally be able to do something well at least in the not too distant

**[00:22:21]** future.

**[00:22:24]** But the point I wanted to make, maybe I got a bit sidetracked.

**[00:22:29]** in my language overflow. I remember when we recently discussed the topic of Native versus

**[00:22:36]** Cross-platform app development. What should I aim for? There were certainly, I

**[00:22:43]** would say, camps, which probably still exist, that favor one or the other

**[00:22:47]** and continue to educate themselves in those camps, whether it's Kotlin, whether it's

**[00:22:52]** Wilf, or I don’t know, achieving very good software results, and that is

**[00:22:57]** becoming increasingly irrelevant.

**[00:22:58]** Do you know those lost souls who think web views in native apps are a good idea

**[00:23:05]**?

**[00:23:06]** Eyeframes were also already a thing. Yes, okay.

**[00:23:10]** Yes, yes, but these are things that change, yes. So from that side

**[00:23:14]** someone was standing by me the other day and said, that's similar to the introduction of the steam engine, where I said, are you JAK?

**[00:23:19]** The steam engine took a long time back then before it was practically everywhere in mass.

**[00:23:25]** You have to set up the building, you have to set up the machines, the people go to the machines, yes.

**[00:23:29]** Then you have the whole issue of how to operate it, okay, electricity came into play at some point, but what I’m getting at is that it took time.

**[00:23:35]** And today, here we are, greetings to Peter, yes, who somehow threw over the Open Clore there,

**[00:23:41]** hits deploy, and how many weeks has it been now, four

**[00:23:45]** or five or six?

**[00:23:46]** No idea.

**[00:23:47]** Now he is basically Adelaide of Sam Altman at Open AI and just like that, yes, that

**[00:23:53]** would, that all goes so fast, it can be overwhelming.

**[00:23:58]** But coming back down to earth, this example with those

**[00:24:01]** webviews in the native apps.

**[00:24:05]** I think that’s a nice example of how AI answers such architectural

**[00:24:11]** questions.

**[00:24:12]** Previously or up until now, the argument has been, let’s go into the webview, there we are

**[00:24:17]** faster.

**[00:24:18]** We just build this website in, we don’t have to adjust anything native in the app,

**[00:24:21]** especially since the website changes.

**[00:24:23]** That doesn’t matter anymore today.

**[00:24:24]** If that thing changes, then I throw the new JSON structure in there or

**[00:24:29]** through Figma or whatever, and then it is simply implemented natively and

**[00:24:32]** within minutes, not within days.

**[00:24:34]** Depends on your process, Klaus. So you have implicitly, let’s put it this way, from

**[00:24:40]** I don’t know, I don’t believe it, I can’t imagine, into concrete examples.

**[00:24:43]** come, because you made it concrete. You specifically set up a
 
**[00:24:47]** process. And I think it is relatively important that we talk about such
 
**[00:24:52]** practical examples, because otherwise,
 
**[00:24:58]** it remains at the level of 'I don't know, I don't believe it,' but not for us.
 
**[00:25:02]** So, very concretely, if you have an app deployment process that has so many approval stages
 
**[00:25:11]** and manual steps that you need like three days before you submit something to
 
**[00:25:17]** Apple, then I don’t understand.
 
**[00:25:19]** How do I understand you?
 
**[00:25:21]** What kind of moderation is this?
 
**[00:25:25]** What don't you understand?
 
**[00:25:28]** What does my colleague mean by that?
 
**[00:25:30]** Who, I want to say, your hypothesis is, well, the AI can quickly build a new version of the app and submit it for review, and since that's a small change, this review will probably go through quickly.
 
**[00:25:44]** No, that is again a much too large specification of a special case.
 
**[00:25:50]** It's about, you have a moldy form that you have on the website or
 
**[00:25:54]** an online shop, where you then previously said, we'll just put it in the app
 
**[00:25:59]** because we don't want to rebuild it natively.
 
**[00:26:03]** That's work, whether it's in Zwift, Kotlin, or whatever, building it natively
 
**[00:26:07]** is just work.
 
**[00:26:08]** We'll let that happen now.
 
**[00:26:09]** It's not about whether you can change it every day, that's certainly
 
**[00:26:12]** also an aspect.
 
**[00:26:13]** But first of all to say, we're just taking the API instead of the website and
 
**[00:26:18]** letting the UI from there, we give them a screenshot of the website and say,
 
**[00:26:22]** let's rebuild that in Zwift, that's a no-brainer, works out of the box.
 
**[00:26:26]** Yes, but also the change, that's the point.
 
**[00:26:30]** Until now it was, oh no, we'll leave that to the backend and the backend delivers
 
**[00:26:34]** the website because separation of concerns and that is a concern for the backend team
 
**[00:26:39]** and the backend team and the data structure.
 
**[00:26:42]** And now you say, we would have an explicit tag, let's leave out the dubious expressions.
 
**[00:26:48]** No, you have an agent team and that is responsible end-to-end.
 
**[00:26:52]** Yes, okay.
 
**[00:26:53]** That is responsible end-to-end and it now simultaneously changes the code of the iOS app
 
**[00:26:58]** and in the backend and ensures that the stuff is deployed at the same time.
 
**[00:27:02]** And that changes thinking and working methods.
 
**[00:27:04]** Yes, so that works.
 
**[00:27:08]** If you think so, that's my point.
 
**[00:27:10]** Point. But if you mess up in your structures, saying, well, I have a backend team
 
**[00:27:15]** and if they're not solely responsible anymore, then they first have to coordinate with
 
**[00:27:18]** the frontend team and then they both have to separately set up their agents.
 
**[00:27:23]** No, no, no. That's the issue with when you have a not-so-good process,
 
**[00:27:28]** then a not-so-good result also comes out.
 
**[00:27:30]** But from the beginning you have vibe coding, vibe coding becoming popular, somehow you saw
 
**[00:27:35]** a nice quote where someone said, as long as AI can't replace the discussion
 
**[00:27:39]** with the product manager, that doesn't help me at all. I think that's going
 
**[00:27:45]** already in that direction. The pure coding at the end is just a small part of the entire 

**[00:27:50]** Processes and you have to look at the whole process and put it to the test and not

**[00:27:55]** say, we are now using AI as qualified autocompletion. By the way, with Vibecoding, I still have

**[00:28:03]** to think about that 'never with toilet paper' idea, like, well, it’s just been thrown there,

**[00:28:09]** but then we would eventually want to get rid of it again because it starts to smell.

**[00:28:13]** I would like to put this main- so from my professional experience, what I would claim is

**[00:28:17]** that it applies to 80 percent of the software that has been written on

**[00:28:20]** this planet so far, invisible.

**[00:28:23]** I say again, picture before replace, if it starts to smell, maybe you should warm it up.

**[00:28:30]** I am considering how big Windows should be for us to be able to do that? But then again, the nerd in me came out. So, I would like to come back to the topic of end to end. So, what is super clear to me is that if you, if you stay only in your, in your IDE reality and say, well, the iOS development

**[00:29:00]** They are just on Xcode and then there are some who use IntelliJ

**[00:29:05]** and others are still on Emacs.

**[00:29:07]** Have you searched for your Emacs?

**[00:29:09]** You can do it that way, then you shouldn't be surprised that the AI somehow,

**[00:29:19]** well, also doesn't have that end to end understanding.

**[00:29:23]** But if you say, wait a second, agentic engineering is more than just the coding

**[00:29:29]** of my backend or my app, but it’s about end to end understanding. What do we actually want

**[00:29:36]** to achieve? What is the value or the problem of the customer? What is the problem

**[00:29:41]** of the customer that we want to address? What is the added value that we want to offer

**[00:29:44]** to the customer? And if you think through that together in a small team of subject matter experts,

**[00:29:50]** then you initially have the real full potential of today's AI agents on

**[00:29:56]** your side. And that is a topic that from my perspective has not yet reached everyone's minds.

**[00:30:02]** The one thing is, what can it already do in existing processes?

**[00:30:06]** The other thing is, if I'm ready to take a step back for a moment and say,

**[00:30:11]** wait a minute, what did we actually want to achieve with this team structure, with this organizational setup?

**[00:30:15]** What was our goal?

**[00:30:16]** Why did we choose it this way?

**[00:30:17]** I mean, what you mentioned earlier, like the modular development,

**[00:30:20]** and all the specifications were meant to enable distributed development across the

**[00:30:25]** You can best handle Klobos in large teams somehow, and something with backend and no idea what.

**[00:30:32]** Then you have imposed an organizational structure over it so that all the people have a home in personal development, in organizational collaboration.

**[00:30:40]** How do we work in a team?

**[00:30:43]** Then the whole Agile stuff came around, trying to shape and lead the teams.

**[00:30:48]** And now suddenly an agent comes around the corner and says, you might want to take a look, we might have a tool that is not only.

**[00:30:55]** I would say rapidly changing in the technology it provides and what it can do.

**[00:30:59]** It’s not just about the individual, perhaps needing to be a bit more of a generalist,
 
**[00:31:04]** and braver and looking at the big picture.

**[00:31:08]** But then there’s also the topic not only of the individual but also of the organization.

**[00:31:13]** Even within which one performs their work, no matter how big or small the companies are,
 
**[00:31:19]** it raises the question of how one needs to organize themselves to
 
**[00:31:24]** get the best possible outcome, so that Team A doesn't say, I have a really great agent,
 
**[00:31:29]** which is running on Copilot, and you haven't seen it, and it prints for you, you know, I print
 
**[00:31:33]** a Word document so that this goes here, you know, I print
 
**[00:31:38]** you an editable form again. That this doesn't happen. As I said,
 
**[00:31:45]** there’s the Fax-GPT, and I’m still mentally struggling with that, but…
 
**[00:31:49]** Are you there?

**[00:31:52]** No.

**[00:31:53]** Yes, I know.

**[00:31:54]** The experience of getting hands-on with the process sounds a bit sidelined right now.

**[00:31:59]** But then there are still one, three really big things that I’m hearing again now
 
**[00:32:04]** that sound strange, that we should really be hands-on with because in all three areas, it's a continuation.

**[00:32:10]** just like now with vinegar.

**[00:32:12]** Short disclaimer, the examples Mark brings are not intended for implementation.

**[00:32:19]** I will remind you at the next weekend chat, yes, but...
 
**[00:32:24]** But that’s bringing...
 
**[00:32:30]** No, but jokes aside. If we say it like this, in terms of, yes, you also have to...
 
**[00:32:36]** You have to consider that you might think outside the box and say, okay,
 
**[00:32:41]** what could we perhaps change in the organization?
 
**[00:32:44]** This is not a, this is not a call for,
 
**[00:32:49]** oh yes, I can't change anything in the organization.
 
**[00:32:51]** Then, then I am completely powerless,
 
**[00:32:53]** but then I can't decide anything anyway,
 
**[00:32:54]** then that doesn't help me, right?
 
**[00:32:56]** Rather, you go in that direction.

**[00:32:57]** I briefly thought you were heading in the direction,
 
**[00:32:59]** that colleagues of ours are listening and thinking,
 
**[00:33:02]** oh my God, what’s coming around the corner.
 
**[00:33:04]** I thought you were bringing the disclaimer.
 
**[00:33:06]** Yes, but of course, that’s...
 
**[00:33:09]** No, they know that already.

**[00:33:11]** So Klaus and I, the colleagues already know that.

**[00:33:15]** No, so what I was getting at is, when we say, agentic engineering is actually more
 
**[00:33:21]** than just programming software.

**[00:33:23]** Until two years ago, I was still managing operations, and just thinking about
 
**[00:33:29]** the possibilities that exist to replace existing thinking or existing processes
 
**[00:33:38]** in operations. What opportunities I have suddenly to support something like classical anomaly detections
 
**[00:33:46]** through an LLM or generally through agents that bring different aspects,
 
**[00:33:56]** different personas, and with these personas, for example, look at log files
 
**[00:34:01]** and perform log file analysis, it’s fantastic that suddenly you're pointed out to things
 
**[00:34:06]** and I will not tire of telling colleagues this, when you manage to
 
**[00:34:13]** write specifications for your software, to say what do I actually expect of the
 
**[00:34:18]** software. Just imagine, because then the agents in operations
 
**[00:34:23]** can say, hey, you’ve written down that the software should do this and that and that
 
**[00:34:27]** but it shouldn’t do this strange stuff here. Is that expected or is
 
**[00:34:32]** what I told you yesterday, you can't know, Alex Weiß was saying, because I told you,
 
**[00:34:38]** rambling about the ISMS, the Information Security Management System, according to ISO 7291, that we
 
**[00:34:47]** would like to implement to achieve compliance with the EU Cyber Resilience Act, so that we can also continue to sell
 
**[00:34:53]** nice thermobics in the future. I hope, assuming, that this ISMS,
 
**[00:34:59]** which is actually a very cumbersome, rigid, organizational, procedural framework,
 
**[00:35:05]** must function for us as agentic implementation, embedded in this, so overarching,
 
**[00:35:16]** the software development process embedded in this ISMS, but things like,

**[00:35:21]** I haven't thought this through completely, but if we imagine now,
 
**[00:35:24]** this ICMS consists essentially of a regulation and a KVP, so a control loop.
 
**[00:35:30]** And if I no longer sit people down and say, look, now check
 
**[00:35:36]** once every quarter if we have improved, but rather let agents do this continuously
 
**[00:35:41]** and with all these opportunities they have from the development cycle, from
 
**[00:35:44]** the operations, as you just mentioned, Alex, from architecture, what I always,
 
**[00:35:50]** you get such a comprehensive feedback loop for your regulation that you can't get
 
**[00:35:57]** by traditional means and from things like the requirements that this regulation imposes
 
**[00:36:03]** on development, so CQ-Coding, system maintenance, patch management, you can also
 
**[00:36:09]** implement all of that agentically and let it flow into your code, into your operations.
 
**[00:36:14]** This is our big project that is pending, to think through all this and
 
**[00:36:21]** implement it in a way that is also contemporary.
 
**[00:36:24]** I see a challenge with the topic of verification.
 
**[00:36:31]** Some also call this guardrails, that you say, if I use agents somewhere,
 
**[00:36:37]** then I want to check that they are also working in the direction we set
 
**[00:36:44]** and that they might not be, well, not like the good arms dealer, supplying both sides.
 
**[00:36:51]** Checking with you and handing something to the attacker. Yes, yes, sure.
 
**[00:36:56]** More or less. Yes, but I find the example with OpenClaw quite interesting
 
**[00:37:06]** in terms of architecture, you can, for example, deny it write access to its core
 
**[00:37:12]** files, so Soul, MD, Identity, you can prevent it from editing them.
 
**[00:37:19]** So filesystem access. And such hard limits are where you say, and you cannot
 
**[00:37:28]** manipulate that yourself. You must not rewrite your configuration and at the latest

**[00:37:33]** at the highest level, you want to, you want to somehow, I’ll say,

**[00:37:38]** have meta-review processes, quality assurance processes that continuously monitor your agents

**[00:37:44]** and see if they are adhering to the framework conditions we have set for them,

**[00:37:49]** have they manipulated the framework conditions somewhere, are they still contributing to the corporate goal,
 
**[00:37:55]** are they actually working right now or are they in such a deadlock where they keep confirming each other
 
**[00:37:59]** all the time and are actually just burning tokens. This meta-level, some call it

**[00:38:06]** the agent orchestration platform, some call it the developer management platform, whatever you prefer.

**[00:38:12]** I think this meta-level, where you say, you have a way to manage the agents,

**[00:38:20]** to check what is running with you. And not at all in the sense of, there is one instance

**[00:38:27]** to rule them all, but rather that you create, ultimately, an infrastructure component,

**[00:38:33]** where you can check that, from my perspective, is the challenge we are currently facing.

**[00:38:38]** And no, no one has coined the word entrapreneurial.

**[00:38:40]** Yes, exactly.

**[00:38:41]** If that were the only challenge we faced.

**[00:38:45]** What would you advise people on how to prepare for this, let's say,
 
**[00:38:50]** new future or how to embark on this journey?
 
**[00:38:55]** So I think maybe you should find something with which you want to start, I

**[00:39:00]** I would just say, well, if he has said something, the topic is basically already taken, and then you look forward to other information from the guests.

**[00:39:09]** Therefore, I propose that I want to basically build on what Klaus has said about iOS development and publishing documents, so with books and articles.

**[00:39:20]** I believe he thinks that his expertise makes him irreplaceable.

**[00:39:24]** makes, he has not understood the dynamics. The AI that is now putting us before. This means,

**[00:39:31]** I am an expert in a topic. Here please register the expert status. Is nothing that is sustainable

**[00:39:39]** as a statement for the masses. There will certainly be exceptions where people somehow due to

**[00:39:46]** stand out in a certain area of expertise. But I would rather emphasize that

**[00:39:52]** you try to use the stuff, either to get even better or to work together

**[00:40:00]** with AI to achieve multiplication effects. What else do you perhaps have that you

**[00:40:07]** can contribute? For me, I’m speaking now as a developer, for me as

**[00:40:14]** a senior developer, where I particularly mean the number of my years of life, of course also the

**[00:40:20]** number of years during which I could gather experience. For me, AI is a super boost. So it’s

**[00:40:25]** not like what I’m doing now… I think it was last weekend, when

**[00:40:30]** I had four cloud sessions open and was building four iOS apps in parallel. You can do that

**[00:40:37]** even without any technical knowledge, only at the first point where it doesn’t work, and that

**[00:40:42]** is inevitably Co-Signing with iOS, you hit a wall. Then you start, then that’s the

**[00:40:47]** project done. And with the experience I have in that area, I can actually go from

**[00:40:53]** specification to having the thing up on AppStoreConnect for beta testing,

**[00:41:00]** on TestFlight, without interruption. So I can utilize my expertise to leverage the advantages

**[00:41:07]** of AI, this enormous processing speed, almost like an extended production line.

**[00:41:14]** And I still indulge in the illusion that this will also be the case in the future. You don’t have to

**[00:41:22]** compete with AI. I don’t have to program the same thing anymore, but I understand

**[00:41:27]** the basic structure of how an iOS app is built. I fundamentally understand when to use Core

**[00:41:34]** Data or when to pack something into the SQLite database or the

**[00:41:39]** text data or however. Yes, AI is getting better at that, but some things, especially when you

**[00:41:46]** are building software for humans, are always hard to answer digitally. What it looks like in

**[00:41:55]** two years, I have no idea. At the moment, I still indulge in the illusion that I am quasi

**[00:42:00]** the orchestrator of the many agents running around here, that I have well under control. But I

**[00:42:07]** I also don't want to rule out that this knowledge could be completely replaced in two years.

**[00:42:13]** One shouldn't have to worry about it anymore.

**[00:42:15]** The question is, what will happen to the beautiful WWDC if we're only watching promotional videos,

**[00:42:23]** from Mr. Force One and the rest, letting the agents do the work.

**[00:42:27]** There are so many insiders involved today.

**[00:42:30]** It's unbelievable.

**[00:42:32]** now already again on the comments where it says either it was very nerdy or a lot
 
**[00:42:37]** of technical terms or no idea what it would actually be her force one you can google that it's
 
**[00:42:44]** this old let me google it for you unfortunately no longer exists but no idea chatty chatty
 
**[00:42:50]** chatty we call it some kind of chatty chatty is yes klippi was that yes the following
 
**[00:42:58]** Yes, from the co-pilot and with that I'm also done with my personal boot filling out.

**[00:43:02]** Alex, I'm trying to salvage this.

**[00:43:05]** You need to come up with something intelligent now.

**[00:43:08]** You know, that's not just your personal assessment, let's say quickly.

**[00:43:18]** I believe this is a generally known, how should I say, assessment of the value contribution

**[00:43:25]** of Microsoft's own AI.

**[00:43:28]** No idea what the colleagues did, it's a shame.

**[00:43:31]** Exactly, I have three points that I would like to share with the people.

**[00:43:36]** And the first one is something that I personally had to get face-to-face from dear Klaus.

**[00:43:41]**

**[00:43:44]** Don't assume, dude.

**[00:43:45]** So don't make any assumptions for the output.

**[00:43:47]** Roll up your sleeves and try out specific use cases.

**[00:43:50]** Don't be afraid, instead I said in the end, OK,

**[00:43:54]** then I'll take a separate computer now,

**[00:43:56]** because I'm scared my data will be stolen. So I'll take a

**[00:43:59]** separate one and think about, OK, what are the things that annoy me in everyday life?

**[00:44:06]** Oh yes, extracting these PDFs from some emails and then preparing

**[00:44:12]** for the tax declaration. So everyone has some use cases where you say,

**[00:44:16]** I always wanted to automate this. Roll up your sleeves,

**[00:44:21]** do it. Because nothing, nothing gives as much as doing that. The second is, when you do this,

**[00:44:29]** penetrate the patterns. Things like skills, plugins, validation loops are MCP. You can

**[00:44:38]** tell yourself, yes that's all from Anthropic, but yes and at the same time what we saw in

**[00:44:45]** OpenClaw, in terms of patterns, I would now say was not so

**[00:44:51]** well-known before, by now there are plenty of frameworks that build on it.

**[00:44:55]** Those are things, if you understand them, then you understand better what such a

**[00:45:01]** technology is actually useful for and what it is not for, by the way exactly the same for

**[00:45:05]** LLMs, whoever still thinks we need to train LLMs so that they are 100%

**[00:45:10]** deterministic, has not understood what kind of technology this is.

**[00:45:13]** And the third is without and control the data flow. So know who you give which data to when and where

**[00:45:23]** and where it's going. There are no excuses anymore to say, yes, but I thought,

**[00:45:30]** the data stays on my computer because I have the app installed on my computer.

**[00:45:33]** Sorry, no, that's ignorance and ignorance should not be paid for.

**[00:45:40]** but it becomes difficult when you say, do it and now I also think Tanja, you all have,

**[00:45:45]** I think you've talked to me about this before, that I asked how would you do that

**[00:45:48]** what to do?

**[00:45:49]** Once a month I have to pull my PDF invoices out of the emails and have to

**[00:45:55]** somehow collect my invoice from Microsoft and from the other providers

**[00:45:59]** compile them, compare them with the Contour statements, and send them to the consulting.

**[00:46:04]** Would you now also tell the Open Cloud, feel free to fetch my Contour statements

**[00:46:08]**?

**[00:46:09]** Yes, right. Are they present in my banking folders?

**[00:46:12]** No, I’m not crazy, but I can give the year a part CSV export from my banking app so that it can process it.

**[00:46:23]** But less. Yes, but maybe...

**[00:46:27]** No, it's not about black and white, it's about what... So just the fact that I...

**[00:46:35]** Each of us probably has some Apple subscriptions.

**[00:46:39]** We also have Android listeners.

**[00:46:41]** It might be that someone has Spotify on Android or something, right?
 
**[00:46:44]** So, I would do the podcast like this, Mark.

**[00:46:49]** That may be.

**[00:46:51]** What I want to say is, I always get these beautiful emails from Apple and I,
 
**[00:46:55]** well, I can no longer count them on two hands,

**[00:46:58]** how many discussions I had with tax office employees.

**[00:47:01]** Yes, then you should call Apple.

**[00:47:03]** No valid tax invoice.

**[00:47:05]** You could make an Openclaw, so you know about it, your learning network.

**[00:47:08]** Yes, but you could go there and say, okay, you might forward it to a second email inbox, then you can use Openclaw or...

**[00:47:15]** Yes, I just told this Craft-Agent, you know, I have here on the Mac, I have Mail, I have Calendar, I have Reminders.

**[00:47:23]** And then the thing started and built me an MCP server that runs on my computer, and
 
**[00:47:28]** I can now chat with an LLM of my choice, using my data. Is that a good idea?
 
**[00:47:34]** Yes, I at least think it was a good attempt. But as you said earlier,
 
**[00:47:40]** the data flowing in, that's of course a lot harder in times of AI,
 
**[00:47:46]** because you don't just have the data as dumb information, but
 
**[00:47:53]** such an AI system has. Its memory of you, not from you, but from the work,
 
**[00:47:58]** it might have done with you, can recognize connections much faster,
 
**[00:48:02]** than you could possibly do. From that side, yes, it's also more exciting, but try it out,
 
**[00:48:08]** try it out, try it out. So, when you described your case there with here,
 
**[00:48:11]** once a month I thought well, but that could be solved wonderfully with it.
 
**[00:48:16]** Yes, but you gave me a totally outdated recommendation. Use N8N,
 
**[00:48:21]** that’s also not right. Wait, I didn't say N8N today, my old self said that,
 
**[00:48:27]** my current self says, use Craft-Agent, so dude, have you ever seen how much
 
**[00:48:32]** Yes, I think that we actually, I really think, it always sounds so pathetically
 
**[00:48:40]** somehow.
 
**[00:48:41]** When you think you've seen and climbed a mountain because there's a new technology,
 
**[00:48:46]** a new kind of solution in this AI sector, and then you think, yes, you didn't
 
**[00:48:51]** climb it.
 
**[00:48:52]** Now it's continuing, now it's heading towards sunshine, I don't know, ski slope, something
 
**[00:48:57]** pretty and then suddenly a new mountain rises, because, oh, now there's a new
 
**[00:49:02]** technology and damn it, what I've occupied myself with all this time,
 
**[00:49:05]** that's also something we, I believe, have to learn and approach.
 
**[00:49:10]** They always say in IT that everything goes so fast, but at this
 
**[00:49:15]** speed, that's new for me.
 
**[00:49:17]** So that's new to IT folks, right?
 
**[00:49:19]** Yes, that's what I mean.
 
**[00:49:21]** Oh, Alex doesn't see it.
 
**[00:49:23]** Yes, yes, and at the same time, at the same time, no, honestly not, because I can’t tell you,
 
**[00:49:34]** when the last time was, when I last read a ten-page tutorial
 
**[00:49:39]** or even more.
 
**[00:49:40]** So, what I find fascinating, now for about two years, so basically
 
**[00:49:47]** since I've had, well, it seems longer. So since I've had the LGBT account, you
 
**[00:49:55]** can check the application possibilities with the AI. And that's
 
**[00:50:00]** often, the thing messes up once more with a dracen, but there are references,
 
**[00:50:05]** where you can look it up. And I find that an invaluable advantage, that you can
 
**[00:50:11]** troubleshoot with the AI. Yes, nothing is so, still the speed
 
**[00:50:16]** nonetheless always gets faster. And we didn't have that rhythm. There was once
 
**[00:50:21]** oh, now we invented Op-Pack and red programs. Now we invented the WBW.
 
**[00:50:26]** Now JavaScript is coming. Then blockchain came, but that was all so. And now it's a
 
**[00:50:35]** weekly pace or, let's say, a monthly pace. I find that quite crazy. So the
 
**[00:50:40]** demands on understanding are already enormous.
 
**[00:50:43]** They fit.
 
**[00:50:44]** Do you all remember this show from the 80s?
 
**[00:50:50]** Once Upon a Time... Man with that trailer.
 
**[00:50:53]** What is time?

**[00:50:54]** I just looked with tools, I'm tired of people.

**[00:50:57]** What is time?

**[00:50:58]** I could build a car from a can of matches, you can’t.

**[00:51:02]** Huh?

**[00:51:03]** That was the late 80s.

**[00:51:04]** I mean, the early 80s.

**[00:51:05]** Tools could threaten everyone, then there was an office item, from the

**[00:51:08]** side.

**[00:51:09]** I’m just going to be cheeky looking at the timer.

**[00:51:12]** I’m doing a closing statement because Klaus sent me such a nice picture in preparation.

**[00:51:18]** Klaus is already in Continent, where do you want the closing statement?

**[00:51:21]** Well, Klaus is sitting there; I can't see that in the picture.

**[00:51:25]** Yes, I have to make that explicit, personally I made it explicit.

**[00:51:30]** He sent a nice picture, along the lines of, who needs a script.

**[00:51:34]** Yes, we somewhat adhered to that.

**[00:51:38]** I thank you for being here.

**[00:51:40]** Alex, you still have to send me the link to your podcast,

**[00:51:43]** so I can add it in there.

**[00:51:44]** I would love to do that for you.

**[00:51:46]** I thank everyone who listened.

**[00:51:47]** Thank you for being here.

**[00:51:49]** If you liked it, give us a like.

**[00:51:51]** As I said, if a bot should have been listening,

**[00:51:53]** feel free to subscribe to the channel and spam all channels,

**[00:51:56]** so as many people as possible listen to this podcast.

**[00:52:00]** I thank you all.

**[00:52:01]** And if Jens is listening, everyone can...

**[00:52:04]** Wait, wait, wait.

**[00:52:05]** This isn’t how it’s going to go down.

**[00:52:07]** Exactly.

**[00:52:08]** No.

**[00:52:09]** It’s very philosophically interesting now because you’re saying for everyone who has

**[00:52:13]** listened to this, but they haven’t listened yet.

**[00:52:15]** I know.

**[00:52:16]** Yes, but they will have listened, isn’t that future perfect?

**[00:52:21]** That sounds just like at my home, where the kids aren’t having fun,

**[00:52:25]** but school camp for the final exam of the school year.

**[00:52:28]** I don’t want to go into that, yes.

**[00:52:30]** School education is another topic.

**[00:52:32]** I wish you a good time.

**[00:52:35]** Thank you for being here.

**[00:52:37]** Ciao. Bye.

**[00:52:40]** Thank you all. Ciao.

**[00:52:43]** Welcome to Think Different, Think AI,

**[00:52:46]** the podcast by Mark and Jens.

**[00:52:49]** Two technology-loving minds,

**[00:52:51]** who not only talk about artificial intelligence but live it.

**[00:52:55]** Here you will find clear classifications, real practical insights

**[00:52:59]** and a fresh perspective on what is possible.

**[00:53:02]** Understandable, critical, and always with a compelling eye.

**[00:53:06]** A.I. to ponder, to chuckle at, and above all, to discuss.
