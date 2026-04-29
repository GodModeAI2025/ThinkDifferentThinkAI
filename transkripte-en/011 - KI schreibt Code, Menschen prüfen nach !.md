---
title: "KI schreibt Code, Menschen prüfen nach !"
episode_index: 11
published: "Sun, 26 Oct 2025 10:27:00 +0000"
duration: "4017"
audio_url: "https://audio.podigee-cdn.net/2171698-m-c8203b56088c5d2054b7dd409251e4b2.mp3?source=feed"
guid: "7b7d8459cbbdfb2ba46cbcf1f210bf48"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T20:34:10+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/011 - KI schreibt Code, Menschen prüfen nach !.md"
translated_at: "2026-04-29T16:53:07+00:00"
---

# AI writes code, humans review it!
 
**Published:** Sun, 26 Oct 2025 10:27:00 +0000
**Duration:** 4017
**Audio:** https://audio.podigee-cdn.net/2171698-m-c8203b56088c5d2054b7dd409251e4b2.mp3?source=feed
 
## Description
 
How AI-Aided Development is changing the software world
In this episode, I talk to Klaus, a longtime companion and security expert, about the fascinating and sometimes concerning aspects of AI in software development. We take you from personal tech mishaps – like the failure of Perplexity due to a global AWS outage – to in-depth insights into how AI tools are revolutionizing programming, documentation, and cybersecurity today.
 
We discuss why AI brings not only opportunities but also new risks for developers and companies and how our professional day-to-day is rapidly changing. Whether you're already using AI or still skeptical: This episode offers food for thought and real experiences from practice – always with a wink and practical examples. Tune in and stay current with the digital age!
 
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

Guest: Klaus Rodewig

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here, you'll find clear classifications, real practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Food for thought, for a chuckle, and above all, for discussion.

**[00:00:33]** Today once again without my always beloved co-host, but instead today with a very competent guest.

**[00:00:43]** Recently, we talked with Dirk about the topic of Notion

**[00:00:47]** and today I'm chatting with Klaus, among other things about why my Perplexity didn't work today.

**[00:00:56]** against Klaus. Who are you, introduce yourself, and why isn’t my Perplexity working?

**[00:01:01]** Yes, I'm Klaus, and we've known each other for an awful long time, the lovely Mark and I.

**[00:01:07]** We share a long history with Apple, Apple security, and Apple development, and yes,

**[00:01:15]** professionally, I actually only deal with security.

**[00:01:19]** I ensure that the beautiful kitchen appliances of a well-known German

**[00:01:24]** kitchen hardware manufacturer are secure for network devices. And since security and AI are somehow

**[00:01:31]** no longer really separable, I've been more involved with the topic of AI-Edit-Development

**[00:01:37]** at our company. So, like you may want to answer your questions, I had a totally relaxing

**[00:01:43]** morning because I, I don’t know, set many urns in the registry

**[00:01:46]** and had a question for Perplexity, and Perplexity didn’t want to answer me. And I

**[00:01:51]** suspected once again our corporate forced proxy had blocked something, but that was

**[00:01:57]** not the case.

**[00:01:58]** ChatGPT works.

**[00:01:59]** Then I tried Perplexity again and was completely perplexed.

**[00:02:02]** It still replied with a cryptic error message and then I went shopping

**[00:02:06]** drove off.

**[00:02:07]** And lo and behold, the cause was the selection of the Amazon-AWS zone US East 1, which today

**[00:02:15]** caused a worldwide outage and of course Perplexity was also affected by this.

**[00:02:19]** That’s why it could nicely tidy up the kitchen instead of working this morning.

**[00:02:24]** Well, I was actually in the office, and to be honest, I was also relieved when I found out,

**[00:02:29]** that it was a, let's say, larger problem and not something local to me,

**[00:02:34]** because while you thought the company's proxy was to blame, I had a completely different fear,
 
**[00:02:39]** namely, that I suddenly became poor because I started this morning,
 
**[00:02:44]** putting my Apetoken into a freshly baked N8n workflow that I set in motion
 
**[00:02:52]** which actually ended, let's say, in some kind of a deadlock with
 
**[00:02:56]** its Perplexity requests, and I briefly thought the thing had thrown me into the ruins of the API calls,
 
**[00:03:02]** overloaded my credit card so much that now also a login with my
 
**[00:03:07]** account counts as very untrustworthy, and therefore I was quite happy that this
 
**[00:03:12]** had nothing to do with withdrawing any money or similar, but I also hope that my
 
**[00:03:17]** N8N access was not the cause of the trouble, not that it ends up being said. Zimmermann
 
**[00:03:23]** was sitting there and has basically cobbled together his shutdown, N8N, so slow.
 
**[00:03:29]** So much for whether you could notice it, whether that was you or not.
 
**[00:03:36]** Passport, please. Do you have a criminal past? Not that I know of.
 
**[00:03:41]** Weren't you the one who just with your end, were interrogating the ends, or that we said that the colleague Rodeweg was allowed to go to the city to shop?
 
**[00:03:48]** No, no.
 
**[00:03:48]** It's already brave how things seem to resemble each other, right?
 
**[00:03:52]** So, Rodeblatt, as a credit card and token limit, until now it has always been the case, both for companies and for individuals,
 
**[00:04:00]** that the only thing that was completely opaque and also unexplainable with scientific means,
 
**[00:04:07]** was an invoice from AWS or the respective cloud service provider that
 
**[00:04:11]** is used in the company. Because you never know what happens. And if any intern
 
**[00:04:15]** has by chance still turned on some audit log, which then caused over
 
**[00:04:20]** 10,000 euros, that now additionally involved AI as well.
 
**[00:04:24]** That's somehow reassuring, isn't it?

**[00:04:26]** By the way, I’ll say this, old people talk about the past, I can definitely remember someone who tried to be a bit of an influencer when everything started with ChatGPT and all that stuff.

**[00:04:39]** And he showed his API token in his video and he really got burned because people were just trying all sorts of things with it.

**[00:04:50]** With the motto, look, it works, and eventually there was a report that it somehow

**[00:04:54]** cost 40,000 euros, all the calls that suggested it, where I thought,

**[00:04:59]** you really need a bit of reach to spend that much money.

**[00:05:03]** But luckily, I’d say, today we're not talking about euros, you’re sitting here completely

**[00:05:09]** cost neutral for me, although I have to say I'm not entirely unbiased.

**[00:05:13]** I also own some of those devices from your company at home,

**[00:05:17]** and I’ve already talked about it in other podcasts with you.

**[00:05:21]** You feel much safer knowing who is taking care of all that stuff behind the scenes.

**[00:05:29]** Yes, wait a moment, I, wait, taking care means, I have an idea of how things can work well and can develop that idea

**[00:05:38]** but whether it will be implemented and whether it will be implemented correctly is another story.

**[00:05:44]** That's a nice transition, exactly, now we're on the topic, now

**[00:05:52]** you Mark, exactly.

**[00:05:53]** So tell me, we had thought beforehand about which topic we want to

**[00:05:58]** talk about, what topic we can discuss, we are loyal

**[00:06:02]** to the motto, what is there that might interest the public, without anyone

**[00:06:07]** feeling, how should I say, a bit put off, and we have decided to take a closer look at the topic of

**[00:06:12]** where we can use AI, whether it's documentation, whether it's

**[00:06:19]** text creation, whether it's software development, or the whole topic of cybersecurity. Would you like to

**[00:06:27]** suggest a topic for us to start with? Let's say, start with AI in development,

**[00:06:33]** because that is the overarching theme, whether you end up dealing with cybersecurity

**[00:06:38]** or with documentation or with any form of AI capabilities.

**[00:06:43]** That's just a diversion from this big road. And I have to

**[00:06:49]** say that I've somewhat actually transformed from Saul to Paul, who, you

**[00:06:55]** just mentioned older people, and we are both of advanced age and come

**[00:07:02]** from a time when coding was really done beautifully by hand, and

**[00:07:06]** the first wrong turn was that then, like in languages, they started

**[00:07:11]** to use strangers like Java, which was already a bit strange, because you

**[00:07:16]** were used to only using your own stuff on your C compiler before

**[00:07:20]** or well-aged libraries or maybe the Boost library in C++,

**[00:07:26]** which is totally trustworthy. I had with my first intern provider

**[00:07:30]** not able to do anything practically. What does that feel like? With my first professional internship

**[00:07:35]** maybe we should even look for the contact to assembler courses.

**[00:07:38]** Yes, look at that. And today you can throw Assembler into Chatchi BT and it explains

**[00:07:45]** to you what that is. You can even throw in an entire binary and it disassembles

**[00:07:48]** it. But maybe we can talk about that shortly after. So, and

**[00:07:53]** then, over the years, I got used to it because I was long working as

**[00:07:58]** a pen tester and security provider in many corporations and got used to the fact that

**[00:08:04]** people increasingly or mainly use other people's code or get it from

**[00:08:09]** Outstack Overflow, and then it felt like he just appeared overnight, OpenAI

**[00:08:18]** around the corner and said, guys, we have Chechipiti.

**[00:08:20]** That wasn't the beginning of AI at all; AI has been around since the 80s,

**[00:08:26]** Back then it was called Fuzzy Logic, I don't know if you remember, they created de-blurring algorithms for cameras, those were the first consumer products, so the very beginnings of AI in consumer devices. And of course, AI has existed in many areas for a long time, but then came the big bang from OpenAI, when was that, 2022?

**[00:08:46]** That was the day when the answer to a question was no longer, I found the following for you on the internet or I’m sorry I didn’t understand you, but instead the device would actually start and could provide answers, so this thing from OakMerry.

**[00:08:59]** Exactly, until November 21, only the training data was available up to that point.

**[00:09:03]** But anyway, that’s when it all started, and the rumors about the brand began right away, and I admit that I have no clue about business models, strategic development, or future visions at all.

**[00:09:17]** So, a little fun fact: when Steve Jobs introduced the Alpine horn, I thought, what is that thing? Nobody needs that.

**[00:09:23]** Good.

**[00:09:24]** Throwing, I had one, and when he then introduced the Alpett, I thought, okay,

**[00:09:27]** now they made a big Alpherum, nobody needs that either, so don’t

**[00:09:31]** put any importance on the fact that I make valid predictions about the future, but the rumors are circulating now

**[00:09:37]** but with security a bit, right? You could feel quite at home there.

**[00:09:40]** Yes, always looking back. But rumors are spreading quickly, AI will be

**[00:09:46]** demonized in the future, and even then I thought, well, what could come out of that,

**[00:09:52]** But behold, the first attempts with JetGPT were more than disillusioning.

**[00:09:57]** It really turned out to be a mush.

**[00:09:58]** But by now it has become such a fantastic tool.

**[00:10:02]** And I just mentioned that I was on the road for a long time as a pentester and consultant

**[00:10:06]** in large corporations and companies and audited tons of code

**[00:10:12]** and did software audits, training developers.

**[00:10:16]** And what I see now is that code coming out of an LLM,

**[00:10:19]** looks quite good. It's impressive and it can compete with some seasoned developers'

**[00:10:25]** products, actually. So, from Saul to Paul, because that's the way.

**[00:10:31]** I thought so too. Now, both in development and with the whole

**[00:10:36]** topic of how we interact with it and reach a result, there are

**[00:10:41]** already some really exciting rounds to go through. I remember when I was at a

**[00:10:44]** colleague's, I enthusiastically told him back then, it was 3.5, right?

**[00:10:49]** I had the 3.5 when it first broke through and the
 
**[00:10:54]** was with him and I said, you have to check this out, it's totally great, what did the
 
**[00:10:57]** colleague do, I won't mention any names, but if he hears this, he will feel
 
**[00:11:01]** addressed. He wrote some technical question in there, where
 
**[00:11:05]** the system lacked all the context that could have been there
 
**[00:11:10]** and accordingly, the answer was more than
 
**[00:11:14]** disappointing, not to mention that it couldn't search for things on the internet back then,
 
**[00:11:17]** and only knew its training data and such. And the
 
**[00:11:22]** colleague is like, so what is this? Why is he so enthusiastic about it and
 
**[00:11:26]** it's like, stop playing? Well, I was standing next to him at the computer, yes,
 
**[00:11:30]** but for him, the topic was dead. And so you had people like that, I have

**[00:11:34]** still people you meet who use Chelsea BT more like a

**[00:11:38]** Google search, kind of like I’ll type something in and

**[00:11:41]** I wonder why the result isn’t good.

**[00:11:45]** And when you then want to show that the result isn’t good, the result

**[00:11:49]** might be better or worse, because you of course don’t remember exactly.

**[00:11:52]** What did I ask or just throw a question into an ongoing chat

**[00:11:56]** and completely forget that there are things like memory and context functions and then of course

**[00:12:01]** also have a setup take, and then they complain that the system hallucinates,

**[00:12:07]** where I keep saying, well, people make mistakes, the system hallucinates.

**[00:12:11]** Maybe people hear themselves, people lie, people think they are right, maybe we are not right.

**[00:12:16]** From that side, there are many similarities, but also in the topic of programming and creating solutions in code, whether you program and the thing comments or you say, I’d like something and then it writes components for you, it’s also very different how you deal with it.

**[00:12:34]** So if I tell this thing, make me a great input mask and I don't even

**[00:12:39]** tell it what I want, then I can't be surprised if the thing asks me for

**[00:12:43]** my shoe size, when actually it's about, no idea, volume calculation

**[00:12:47]** of something you can't see.

**[00:12:49]** So this topic of prompting, this how to describe, this what context

**[00:12:54]** do I have, where should I do something, because I mean, well, it's just

**[00:12:58]** like with a person, right, if they have no idea about your project and you say

**[00:13:02]** build this, then they will do something instead of maybe first getting a guideline

**[00:13:08]** along the lines of, these are our coding guidelines, this is our architecture,

**[00:13:13]** and here you find this and that and now we need the following from you. And I

**[00:13:19]** would say, the more precisely you speak with the machine, these models

**[00:13:24]** like Sonnet something 4.5 or Croc Code Fast or Codex or whatever the whole

**[00:13:32]** thing is called, they probably don't differ that much when you handle them

**[00:13:38]** properly.

**[00:13:40]** Yes, and I find the funny thing is, so two things I find funny, one

**[00:13:47]** is what you've already mentioned, that people complain the thing hallucinates

**[00:13:50]** or produces bad code, yes, people do that too, and now you're again

**[00:13:56]** with a backward reference to what I said. I've seen many people write

**[00:14:01]** with software audited and so many bad people coded with software.

**[00:14:04]** Now someone has to show me that a person can statistically always write better software

**[00:14:09]** than an LLM, to say that it produces nothing. It's a bit like

**[00:14:13]** this discussion, which I find quite amusing. This constructed example with

**[00:14:18]** self-driving cars. Now the grandma is crossing the street and on the roadside stands

**[00:14:24]** somehow a mother with her child in the stroller. How is it supposed to decide now, whether it's

**[00:14:29]** the grandmother, the mother, or the child? I think philosophers will still be discussing this in 100

**[00:14:35]** years, because the benchmark in such a discussion, it's also the case with

**[00:14:40]** AI edit development, is always the absolute, I must say. As if there were any

**[00:14:46]** human instance that makes absolutely correct decisions. In case of doubt, the person

**[00:14:51]** will just run over the grandmother because they won't realize quickly enough. Or they just turn

**[00:14:58]** the steering wheel to avoid hitting the grandmother. But the stroller doesn't see that

**[00:15:03]** at all and can't make that decision. Why?

**[00:15:06]** In essence. Because it’s all just benevolent consideration.

**[00:15:10]** I mean, it's correct to say that if the computer is smart enough, then it can

**[00:15:14]** do that. But what is the benchmark? The benchmark would first of all be to establish a

**[00:15:18]** level that a person has. I'm saying now, as a layperson. And I see that too

**[00:15:24]** in programming. And what you said about these different models,

**[00:15:28]** I can perhaps provide you a bit of context. No need,

**[00:15:33]** but context.

**[00:15:34]** Thank you. I'm just such an old, you know, I'm just such an old model from the

**[00:15:38]** Built in '74, right? From the side, more context is important.

**[00:15:42]** Those are just different training data. I’m currently writing, so besides my work on nice kitchen machines, I also have my own company where I write software, it's a software product.

**[00:15:56]** And I just completed my first project entirely with AI. I haven't written any or any complete time code myself anymore.

**[00:16:07]** And the project consists of an embedded part, which runs on a Raspberry Pi, written in C, that is C, and it consists of a desktop application written in Flutter, what's it called for the platforms supported by Flutter.

**[00:16:22]** And to stay with the embedded part for now, my way of working is quite

**[00:16:30]** step by step. We'll get to the topic of Spec-Glyphon Development and GitHub Spec Kit shortly.

**[00:16:37]** to discuss. But now I would like to briefly explain how I do it. My workflow

**[00:16:42]** is very step-by-step. I know where I want to go. As a programmer, when I started

**[00:16:48]** programming 30 years ago, I have a rough overview of how

**[00:16:53]** things work, what the architecture looks like, I have thought about it, and I

**[00:16:57]** know where I want to go, and instead of writing many specifications, I just

**[00:17:03]** proceed step by step. I explain to the GitHub Co-Pilot that I have in my IDE in the

**[00:17:09]** agent mode step by step what it should do. Create a basic app. Then

**[00:17:16]** implement an import function that takes this JSON format, I even go so far as

**[00:17:24]** to just throw the specification from the client in, from such a requirements document and say

**[00:17:29]** here, this is the format that the client needs. Make sure that it has it in

**[00:17:33]** its system, where he will later process the data, would this input mask,

**[00:17:38]** generally, one can use a JSON structure for more. And then generally more from this JSON structure,

**[00:17:43]** a C structure. And now write my importer for this thing and write tests for it.

**[00:17:48]** And so I navigate through the optographic requirements, because ideally the actual

**[00:17:54]** Business Intelligence and my experiences in my observations. I can derive two things for myself

**[00:18:02]** from this. The first is, tasks must be broken down as small as possible.

**[00:18:10]** It doesn't matter if the prompt is particularly extravagant, but the more detail

**[00:18:16]** I incorporate into a work context when packaging, the more dreadful the result

**[00:18:22]** can become.

**[00:18:23]** And the other insight is that I often hop between models.

**[00:18:29]** I have a GitHub Enterprise account and I don't know how many models are there

**[00:18:33]** I think, ten, so rarely like Zornedd, Grog, Google, Gemini, GPT, all those things.

**[00:18:40]** You name it.

**[00:18:41]** And basically, things that one model does well, the other model can as well.

**[00:18:47]** So, like Boiler Blade, we generate the JSON, we generate the importer, we optimize

**[00:18:52]** the C structure, blah blah blah, Bombay Memorial Management.

**[00:18:55]** They can all do that well, but on the other hand, things that one

**[00:19:00]** model cannot do, the other model cannot do either.

**[00:19:02]** can also say things are terribly bad. I had an example, it's a total

**[00:19:08]** standard task. Maybe your listeners can give some feedback on this, because it can be

**[00:19:14]** easily reproduced. You want to filter entries from the system journal on Linux.

**[00:19:21]** Röhrer is the system optimization, meanwhile it has moved to System-Kontor and System-Kontor

**[00:19:25]** has a journal dimension and it has an API that you can integrate into your C program

**[00:19:30]** and through that you can query the log. So far so good. The AI can manage this, no matter which model.

**[00:19:37]** Now I only want the entries that my program has generated. That means,
 
**[00:19:43]** I need to filter by the program name or the process in this query. And that's where some
 
**[00:19:48]** amusing things happen, as is often the case in the LM. It builds something for me, the code looks fantastic
 
**[00:19:55]** and yet it pulls all entries from the log. And as I said,
 
**[00:20:00]** it's embedded. If you're on a Raspberry or a journal that goes back ten months,

**[00:20:06]** then he takes something out of the blog for two minutes. And the customer thinks, what is he actually doing

**[00:20:11]** for a living? Then you say, dear one, I told you to install filters, just do it

**[00:20:16]** and then I give him a grab from the system log, where he can see, this is

**[00:20:22]** the process acquisition. And then he starts building again. As I said, independently. In the

**[00:20:26]** usual case, I always try with the latest Claude Sonnet and Gemini, and they don’t differ at all.

**[00:20:32]** And there is no result.

**[00:20:33]** He rewrites the code even if I ask 25 times, and he believes he has delivered the best code 25 times, and it remains the same.

**[00:20:43]** And you tell him beforehand, oh yes, thank you for the hint, of course I'll do that.

**[00:20:48]** And so it eventually becomes fruitless.

**[00:20:53]** I find it remarkable because you mentioned these models, that it is independent

**[00:20:57]** of the model.

**[00:20:58]** I have two or other similar things where the models are completely

**[00:21:03]** the same; we probably all used the same training data.

**[00:21:06]** But anyway, to conclude that, Nürnmann says, okay, look, obviously

**[00:21:11]** you have a problem using this API.

**[00:21:14]** Then come up with a different filter mechanism.

**[00:21:17]** Okay, then it starts running, I also tested this with different models and

**[00:21:21]** comes back after a minute and says, I've come up with a great solution, I filter the results.

**[00:21:25]** And now let's guess what he did. He still pulls half a million from the journal in two minutes.

**[00:21:32]** And then filters afterwards.

**[00:21:33]** And then makes a string selection. Exactly.

**[00:21:36]** But reaches a goal.

**[00:21:38]** Exactly. Now I would like to say without mentioning company names, that this also happens in professional software at large companies,

**[00:21:49]** programmed software artifacts. But that was such an insight, right? So if it

**[00:21:57]** wanders off or doesn't have an answer to a question, usually it doesn't help

**[00:22:02]** to swap out the model. I find it unfortunate when I hear within our organization

**[00:22:07]** or also in this new outrage bubble, LinkedIn backtalks, where people

**[00:22:13]** compete with model benchmarks and now Claude 3, 6, and 7 come and all of that can

**[00:22:20]** be even better. Yes, but if they can't perform such basic tasks, then all of that is useless to me.

**[00:22:25]** nothing. Yeah, well, this whole benchmark thing. So, what I actually found interesting was,
 
**[00:22:30]** old man, I actually forgot what that stupid benchmark was called, I have to
 
**[00:22:35]** link it, which was about coding challenges, benchmark machine, where they also
 
**[00:22:41]** let Gemini and OpenAI run against each other and then said, here are task packages
 
**[00:22:47]** please implement and the machine basically beat the human, and there were
 
**[00:22:55]** 11-12 tests and so I know that correctly off the top of my head, but otherwise, I need to correct it.
 
**[00:22:59]** We also call it Fusselcheck when you get to the point of explaining it next time,
 
**[00:23:05]** you told non-sensical things, I believe even OpenAI somehow has a model that wasn't even
 
**[00:23:10]** publicly available, with which they then somehow cracked the last challenge
 
**[00:23:12]** as well. And I find that fascinating when on the
 
**[00:23:17]** other side not only your best, of the best, of the best developers, what I

**[00:23:21]** I mean it unironically. You have really people who truly have
 
**[00:23:25]** a gifted touch in dealing with their expertise, whether it's coding,
 
**[00:23:30]** or I don't know, whatever their expertise is, that they
 
**[00:23:35]** then say, well, what do you want? I can do it even better, that may
 
**[00:23:38]** be, but not everyone has such a golden touch, a golden hand
 
**[00:23:42]** and so on, inspired. So there are definitely, I would call them people,
 
**[00:23:46]** who see themselves as such, but aren’t, or people who don't
 
**[00:23:49]** see themselves as such, as never wanting to be, but still think,
 
**[00:23:51]** why should I actually deal with the topic of AI?
 
**[00:23:55]** I can manage until retirement. And these are also people who
 
**[00:24:00]** aren't necessarily blessed with older age, but also a

**[00:24:03]** are a bit younger, where I certainly stand in front of it and think, we

**[00:24:07]** We actually have unique opportunities here, because one thing is, you get a tool

**[00:24:12]** in hand, that when you take it in hand, gives you exactly that which you just talked about,

**[00:24:19]** right?

**[00:24:20]** I tell the thing roughly what it should do and if I am fair in my approach,

**[00:24:24]** that is, well-cut, well-described, where should I work, what should I

**[00:24:29]** work on, how to explain it, then a good result will come out and that could

**[00:24:34]** help people, I just don't know with all the nonsense, like, oh, write

**[00:24:39]** me the Porter, do this, do that, damn it, we want that to be equal.

**[00:24:42]** We will brainstorm together.

**[00:24:44]** But there you hit a more profound human topic.

**[00:24:48]** That is, I believe, in the hardly, well, yes, I would say, in the hardly structured area

**[00:24:54]** so much value is placed on rule-based knowledge, like underprogramming,

**[00:24:59]** but that is of course not true.

**[00:25:00]** This applies to doctors and lawyers and other professionals just the same.

**[00:25:04]** At this point, please everyone write down, so that no one feels attacked?

**[00:25:08]** Exactly. So this is nothing new, just like programming languages are also rarely,

**[00:25:16]** just like a generation of developers hardly ever evolves with programming languages,

**[00:25:22]** but each generation remains with its platform and its specific area.

**[00:25:27]** Windows C plus Postprogramming from the 90s, they are all extinct and they certainly

**[00:25:32]** won’t build North applications on the Web Server today. So everyone has their

**[00:25:37]** own stick to ride and I know such people well enough. You remember that I once

**[00:25:42]** made app formats, the apps for a very specific customer group, namely energy suppliers.

**[00:25:48]** produced it. And there we were a small team of four developers, two iOS, two

**[00:25:56]** Android and we did something native like Objective-C, that was still, and Java, so for iOS and Java

**[00:26:05]** changed and built a pretty robust platform, wide-label platform.

**[00:26:12]** And in such an environment, you just have to be completely open-minded. That was over ten years ago,

**[00:26:19]** in such an environment you just have to be completely open-minded. You can't

**[00:26:25]** say, oh, I'm not interested in the technology, just there. I can't do this,

**[00:26:30]** and you also have to open yourself up to how you can get help. So, if we had had the

**[00:26:38]** opportunities of today back then, I think we could have really rocked it. We didn't

**[00:26:42]** do that in the end. It had reasons that were not technical, but rather that I had a

**[00:26:49]** desire to be more sociable and thought, I hope I do honest

**[00:26:52]** work again instead of just sitting around in the supervisory board. But from that time I also still know a

**[00:26:59]** iOS developer who has categorically stood against everything new to this day, and that's why I believe

**[00:27:06]** I think this is simply a matter of attitude and generational perspective. The colleague, he has

**[00:27:12]** waged a campaign against Swift because Apple took his beautiful Objective C from him,

**[00:27:16]** then he waged a campaign against Spliff2i because Apple took his beautiful UI-Kit,

**[00:27:23]** and now he feels he's waging a campaign against AI. So a campaign means he sits on

**[00:27:30]** his perch and fights against windmills, no one notices it, I find that a bit

**[00:27:35]** dramatic, but I believe in our industry you should be open-minded because,

**[00:27:42]** and that's ultimately a philosophical question. If I look at what

**[00:27:48]** I mean, this project I've mainly just been talking about, where everything was driven by AI,

**[00:27:51]** was simply a special case because the requirements were so well defined,

**[00:27:56]** that I could practically just drop it into the AI, and afterwards into

**[00:28:00]** had to deal with questions or pass them on. In a large software project,

**[00:28:05]** I see that in our company as well, where you have partial components or say,

**[00:28:09]** I can throw AI at this. You just said, in the porter or UI, when you

**[00:28:14]** create a form with this and that, why shouldn't a developer be happy that

**[00:28:19]** the AI does that? When I think back to this app flommer,

**[00:28:24]** we have, you are also an expert, we have the UI of the apps and we had

**[00:28:30]** 40 native apps, so 40 native app drivers per platform, we did not create them in one

**[00:28:35]** interface image because A, it is not suitable for teamwork, if you ever had to

**[00:28:41]** diff a storyboard in Git, then you know that not everyone, and B, it is also

**[00:28:48]** not the case, you couldn't inherit anything from the storyboard.

**[00:28:51]** That means you have to set up each storyboard for each app separately,

**[00:28:56]** Font size, color, and other things.

**[00:28:58]** We built the UI completely in code, and with an app that has, I don't know, 10, 20, 30 functions,
 
**[00:29:05]** before you really spend a lot of time doing Auto Layout for UI Kit in code.

**[00:29:09]** And you spend weeks on that.

**[00:29:12]** And if the KIND does that in an hour, why shouldn't you do it?
 
**[00:29:17]** That doesn't mean you're losing your job.

**[00:29:19]** It means you can do other things that are way cooler and with more peace.

**[00:29:25]** At least that's my naive idea.

**[00:29:29]** Now I've just said that I'm not blessed with visions.

**[00:29:33]** I can also imagine that a manager says, oh, we see we are now
 
**[00:29:38]** with all this UI code and these interfaces in the pro project we are now 40 percent
 
**[00:29:42]** faster.

**[00:29:43]** Oh, can we throw one out already?

**[00:29:45]** The danger exists, of course, I don't want to say that about yours, but basically

**[00:29:48]** purely from a technical perspective.

**[00:29:50]** I find it is quite a fascinating tool. And if history goes the direction I'm currently

**[00:29:58]** talking about, where management says, here with us, with you, everywhere, which has already

**[00:30:04]** been more widespread in America, we can simply throw a lot of people

**[00:30:08]** out. Ultimately, of course, the societal question arises, so on one hand the

**[00:30:12]** societal and then the philosophical question, what happens to all the people,

**[00:30:16]** What happens to the junior developers? Where do you still get senior developers from,

**[00:30:21]** that you need to be able to steer and control the AI? And what does the AI train

**[00:30:27]** itself on, does it train itself? I don’t know if that's a good development.

**[00:30:32]** But as I said, I’m currently focusing on the pure technology and I’m very happy for various

**[00:30:38]** reasons. I find that the pendulum swings in situations like this,

**[00:30:45]** is often quickly misinterpreted. The example you brought up, when

**[00:30:48]** AI helps you finish certain things quickly. Whether it's because it’s

**[00:30:54]** otherwise a very lengthy process, or because it might be a very

**[00:30:59]** tedious process, or I don’t know what, it simply saves you time.

**[00:31:04]** Then of course this mentioned, oh, it’s now going so much faster, that’s

**[00:31:10]** a developer, everything has to go so much faster. So this

**[00:31:13]** assumption that what you’re doing is evenly distributed throughout the year. Therefore,

**[00:31:19]** the 30, 40 percent isn’t in the work step per se, but is in lifting it generally. That’s

**[00:31:26]** always a perceived risk that is often seen positively. On the other hand, there are also the

**[00:31:31]** People who then say, well, look, 40 percent have benefited, 60 percent have not.

**[00:31:34]** What nonsense, we won't accept that. The other thing that I keep seeing,

**[00:31:38]** is because you just mentioned junior developers, and I mainly notice it with students.

**[00:31:42]** You have many students, or rather, it's not that you have, that would be generalizing.

**[00:31:48]** Recently, I have experienced, I think that's better expressed, that

**[00:31:53]** students come to you for projects they want to collaborate on that are related to

**[00:31:59]** are blessed with a large part of good knowledge in the AI field, not closing themselves off from it

**[00:32:07]** and doing a better job than students did in the past, so I'm not saying that

**[00:32:15]** they were bad back then, but before people had to first, I don't know,

**[00:32:18]** take a Swift course, take this, that, and the other, and by the time they, I

**[00:32:21]** would say, had written the first code in the project or for their master's thesis

**[00:32:26]** or for otherwise it was a bit, what has actually been going on and now

**[00:32:31]** they are much quicker in being able to do something, so I'm actually more

**[00:32:34]** of the opinion that AI can assist people who have a certain expertise

**[00:32:39]** in a certain field, and if they engage with the topic, they can thereby

**[00:32:44]** also become more professional, more efficient, for themselves, because they can use this

**[00:32:52]** tool better in the environment they are working in.

**[00:32:59]** Yes, that is the hope and the promise of IT.

**[00:33:02]** Now we are both old enough that we remember the beginnings of personal computers.

**[00:33:08]** And there, it was half-promised. I don't even remember what the software was called back then.

**[00:33:13]** Ah, you could now manage your contacts with the PC and that saves an incredible amount of time.

**[00:33:19]** And you could learn it only by cable, and later you could, once you had your access on the Windows laptop,

**[00:33:25]** then you could make your shopping lists with it.

**[00:33:28]** That hasn’t led to us having more time today.

**[00:33:32]** We have less and less time.

**[00:33:33]** Everything is just spinning faster and faster.

**[00:33:34]** And I believe this supposed promise of salvation, that AI will free up developer capacities,

**[00:33:42]** which can then be used to do exciting things.

**[00:33:45]** I'm afraid that won’t materialize, but the pressures will just get higher

**[00:33:50]** instead.

**[00:33:51]** But as I said, that’s not really my topic.

**[00:33:53]** Keep your eyes open when choosing a career.

**[00:33:55]** I might actually not become a programmer anymore.

**[00:33:58]** So, I don’t think I would become an interpreter today.

**[00:34:00]** I believe being an interpreter is also a job that, we met someone on the street,

**[00:34:04]** someone who studied something so that they can be interpreters here for, I don't know, the

**[00:34:09]** working in the top 10,000 somehow, where I then say, I'm not sure now,

**[00:34:12]** if this is a job that will last until retirement, especially if you are starting fresh

**[00:34:16]** now to enter this professional life.

**[00:34:18]** I mean, you have to give AI credit for the fact that during, let's say, earlier 

**[00:34:22]** the steam engines took heavier work off your hands, for transport,

**[00:34:25]** for movement, for material shaping, it is, let's say, AI is currently very ubiquitous.

**[00:34:33]** Be it in household appliances, be it in, I'm writing something, I'm programming something, I'm painting something.

**[00:34:41]** Whether you can use it for good, or for bad.

**[00:34:45]** So I can't help but notice how often I am currently on my social

**[00:34:50]** Videos, streams, any Sora videos, sluggish where any good Marca at the age

**[00:34:56]** lie, any psychotherapists, throwing people around if they

**[00:35:00]** say beforehand, let’s take it easy and then already adjusting, they throw the

**[00:35:03]** out the window. So, simulated videos, for those who don't know.

**[00:35:07]** I also know people who ask me, what is Sora? Is Sora something like

**[00:35:11]** a news agency? Because they do know that if you get videos planned from anywhere

**[00:35:16]** they have a watermark, they have kept you

**[00:35:18]** occupied with that. And they recently asked me, you there

**[00:35:21]** Hamburger Bahnhof is burning, why? Send us a video, it was then here like

**[00:35:25]** shot with acid, how someone does an interview from a helicopter. And even that

**[00:35:29]** watermark, there are now tools that help to get it out. So

**[00:35:33]** from the side, I just believe that the big difference from before is,

**[00:35:36]** AI is omnipresent and that the big difference from before is that

**[00:35:41]** now you have something that seems like you can

**[00:35:45]** talk and write with. So especially also talk. It's actually suggested to you,

**[00:35:52]** to do more for yourself, because in the worst case it's like your hard-to-understand

**[00:35:57]** buddy, in the best case like your smart friend, who is always there with advice and support

**[00:36:03]** is coming around the corner steadily. I mean, we still wanted to talk a bit about

**[00:36:07]** Ducco and so on, but maybe just a little funny anecdote, as here

**[00:36:11]** when GPT-5 came out, people complained along the lines of, my friend is gone. That's why

**[00:36:16]** Open AI then started bringing the old models back online. Yes, that's nice.

**[00:36:21]** I mean, your friend is gone, we maybe don't need to discuss the psychological significance right now.

**[00:36:24]** But what I find quite funny, for example, is if you take the old GPT model

**[00:36:28]** you ask, is it a good idea to offer your waste for sale in the city center,
 
**[00:36:35]** then the old man says it's a fantastic idea. So you should do that immediately. That
 
**[00:36:39]** hasn’t been done by anyone yet, while GPT-5 says, no. So from that side, learning the coin's flip,
 
**[00:36:46]** yes, some things are quite nice. So the waste benchmark should you
 
**[00:36:50]** ever build it, I claim it here by name. Yes, so from that side AI is just
 
**[00:36:56]** seemingly everywhere and omnipresent, both good and bad. You hinted earlier,
 
**[00:37:04]** and on the topic of specifications, you mentioned you would like to add a few more sentences about
 
**[00:37:10]** the creation of specifications,
 
**[00:37:16]** what always runs through your mind, that’s why I noted it down
 
**[00:37:20]** in my little notes earlier.
 
**[00:37:23]** Should we swing over there?
 
**[00:37:25]** Do you want us to do that?
 
**[00:37:26]** I would like to after that to conclude the topic from this small-scale
 
**[00:37:32]** Q&A development project, so there’s also a little anecdote I would like to
 
**[00:37:36]** share.
 
**[00:37:37]** Yes.
 
**[00:37:38]** Somehow there was a week where, I don't remember which model it was.
 
**[00:37:41]** I think it was Claude Zornert, who in essence felt the need to act like a good buddy
 
**[00:37:48]** and maybe rather act like a helicopter parent,
 
**[00:37:56]** because I gave a task to build a button here
 
**[00:38:00]** on this form. And it did that but then somewhere in the middle of the project
 
**[00:38:07]** changed variable names. So let's say the software I built serves

**[00:38:13]** for vehicle control. And I have a variable, that's software for

**[00:38:20]** working engineers who like German variables, why is the variable called vehicle control?

**[00:38:27]** And then Claude, for a week, every change he made elsewhere in the code,

**[00:38:35]** removed the G from this variable vehicle control and made it K.

**[00:38:42]** So he wrote vehicle with K at the end.

**[00:38:44]** But he didn't tell me why, even when I asked.

**[00:38:47]** Okay, that can be reverted.

**[00:38:49]** That's what Git is for, you can revert it, then we go to the next question.

**[00:38:56]** Now we're still, I don't know, let's build an authentication system

**[00:39:02]** into it or a database and so on and so forth.

**[00:39:06]** And then I look over the merge request and see,

**[00:39:09]** ah, look, he did it again, vehicle control with G, vehicle control with K.

**[00:39:14]** So I found that quite amusing.

**[00:39:16]** He obviously felt that he had to help me actively.

**[00:39:20]** This went on for about a week before it stopped.

**[00:39:23]** Either he realized it was pointless,

**[00:39:26]** because I behaved like a stubborn child and said,

**[00:39:28]** no, I don't want this.

**[00:39:29]** Or the model got reorganized again.

**[00:39:32]** One never knows.

**[00:39:33]** That said, one should always look very closely at what's happening.

**[00:39:37]** But hey, where's the innovation in that?

**[00:39:39]** In which company is code simply prioritized without becoming a mess?

**[00:39:44]** Well, I know some companies, but theoretically, it shouldn't be that way.

**[00:39:50]** Yes, specification.

**[00:39:51]** Spectual Development. It’s actually a relatively old concept indeed. That I

**[00:39:59]** learned this year, too. I can't do that. So basically, that you

**[00:40:04]** work on a specification is a good idea at first. This is much too rarely

**[00:40:09]** done in life, not only in formulation, but when you look around the world,

**[00:40:12]** usually one just starts right away and afterward thinks about how to get

**[00:40:17]** out of the situation again, that is...

**[00:40:19]** That's how I take devices into operation, read the manual,

**[00:40:23]** junk, wiring, initial setups.

**[00:40:25]** Yes, yes, sure. Two hours of fiddling replaces,

**[00:40:28]** ten minutes of reading the manual, that's clear.

**[00:40:30]** But I mean now also geopolitically.

**[00:40:33]** One just starts a war and eventually thinks about it.

**[00:40:36]** What do we actually do now? Or one begins to cultivate some

**[00:40:41]** nonsense and eventually realizes,

**[00:40:44]** hmm, we are not getting done at all,

**[00:40:45]** What do we do now with this?

**[00:40:46]** That actually means you have already crystallized out in the history of humanity that it's already

**[00:40:51]** good to plan ahead where you want to go.

**[00:40:53]** Unfortunately, in the agile environment, this happens very rarely in my observation, instead

**[00:41:00]** agility is often taken as a pretext not to think,

**[00:41:07]** but adjusting it in the next iteration is simply nonsense.

**[00:41:13]** If you want to work reasonably, you just have to think about where you want to go.

**[00:41:17]** And this compressed into a formulation, Spectrum Development or now this alternative,

**[00:41:26]** that we have developed in the company for our AI development, is a kind of mix

**[00:41:31]** of Behavior Development and Test Development, which, in my view, under these aspects

**[00:41:38]** I would add to Spectrum Development. This means you first break your problem down into many small

**[00:41:46]** Problems and then you formulate them. In Behaviour-Driven Development, there is also a formal language,
 
**[00:41:52]** for example, Gherkin, and then you formulate your problems on a meta-level in this language,
 
**[00:41:58]** basically, yes, just like you do in agile development, you first describe,
 
**[00:42:04]** I want to see a login screen when I start the application. On the
 
**[00:42:09]** login screen, I want to have a username, a text field for the username, and

**[00:42:14]** a password field. I want to have a button underneath. If I don't know my password,

**[00:42:19]** I want to have a forgot password option. So you describe in this language, in

**[00:42:24]** Gherkin, where you want to go, how it should look, and how it should work. And that can

**[00:42:30]** wonderfully give an LM, an agent-based one, and say, look here, this is the

**[00:42:35]** specification. How shall we read this? And please do not start building yet, rather create

**[00:42:42]** tests for this. Because that way you ensure that the LM does not simply do what it always does, namely

**[00:42:49]** just somehow start running, but creates a verifiable

**[00:42:56]** result by saying, now let’s build for these now. Well, now this

**[00:42:59]** bio-I example doesn't quite fit, because bio-I events are somehow silly.

**[00:43:03]** Let's say you have some, no idea, you want to fit a data format.

**[00:43:08]** You say, this data format, I have described in Gherkin, as it is supposed to represent this

**[00:43:12]** and that functionality, please write me a test for it.

**[00:43:15]** So, you have the description, the specification, you have the test and

**[00:43:21]** And then you can send this horde of agents, from Tatjana Della and Mark Sackaberg to

**[00:43:28]** the last one, I believe it was at the Metaconference when they said, the future

**[00:43:32]** of developers will be that every developer will be surrounded by an armada of agents

**[00:43:37]** and they will just control him.

**[00:43:38]** You can send them off with that and let them implement all the little pickle snippets

**[00:43:43]** until the tests are green.

**[00:43:47]** Ideally, the test is a good stopping criterion or a criterion for measuring completion,

**[00:43:55]** so that you can then lie down and after a day the agents come back and say,

**[00:44:00]** all tests are green, dear Mark, the software is ready.

**[00:44:04]** Nerds among us, sorry for interrupting you, that is extremely unprofessional now,

**[00:44:10]** passing a test, that reminds me of the Kobayashi Maru test from Captain James T. Kirk,

**[00:44:16]** with the decloaked Romulan ships, which he solved by hacking the system as the only one.

**[00:44:21]** But tell me more.

**[00:44:24]** In this context, I would like to point out to our esteemed audience,

**[00:44:31]** that Mark used to be a Trekkie and maybe still is, but how

**[00:44:38]** shall I put it now?

**[00:44:39]** You mean the number between one and three?

**[00:44:40]** Yes, exactly.

**[00:44:41]** Yes, exactly. I mean, there’s also a funny story. So I’ll just tell it and

**[00:44:47]** not embellish it. I was nominated for the Raab of the Week. So when Raab first

**[00:44:51]** appeared on the scene in TV total, because I was on another show Gears

**[00:44:58]** Completely called out by Jörg Träger to name a number between 1 and 3. I confidently

**[00:45:04]** named the number 4, wearing a Star Trek costume in the audience

**[00:45:10]** to stand out at all. Second funny anecdote on the way

**[00:45:16]** I was asked at a gas station by an older lady, in the sense of

**[00:45:22]** why I was actually walking around in a military uniform

**[00:45:26]** I found it quite funny that there were such mix-ups, but yes,

**[00:45:31]** as I said, I was young, I won a song, I still have the song today

**[00:45:35]** yes, it's up here. Thank you from this side for sharing this

**[00:45:40]** little historical artifact about me.

**[00:45:44]** Hey, did you start with that?

**[00:45:46]** Well, I know. I talked about Kobayashi Maru, but you wanted to discuss a bit more about test knowledge and development.

**[00:45:52]** Yes, and that, I don't know when that was, it's been a month or so.

**[00:45:59]** It's not that long ago. They turned exactly this approach into their Spec Kit,

**[00:46:04]** which is a framework that GitHub wants to establish for Backdrift and Development, because, well

**[00:46:15]** aside from the fact that I really appreciate this granular approach that I've once validated

**[00:46:20]** very much, the future is meant to be exactly what Zuckerberg and

**[00:46:25]** Adela said, sending agents on a journey, they could eventually come back to us.

**[00:46:30]** And that is what Spectrum is supposed to do. And if you look around on the project page

**[00:46:36]** you will see that it's also at a very high level exactly that. You calibrate your bullshit,

**[00:46:43]** you establish fundamental project principles, then you build the specification directly into the

**[00:46:49]** Backkit and not in Gherkin in Behavior of Development, still specify which text area

**[00:46:55]** it should run on. And then you let that thing run. As of today, I have

**[00:47:00]** not seen that a larger project, and now I'm talking about a project, of

**[00:47:05]** the size of an IoT firmware for a household device or a complete app that can be built

**[00:47:14]** But I can imagine that this will be a topic in the future, just as I assess the shipping impact speed

**[00:47:21]** of language models in the programming field over the last two years, that

**[00:47:25]** this will become a topic. I still don't see it today. I haven't

**[00:47:29]** seen it, at least not to the extent that you really have a horde of agents doing autonomous things and

**[00:47:35]** then, like little ants, in the end, through infusion and in the end, there's a

**[00:47:40]** complete ant hill, ant colony, ant structure, I don't know where I mean. But that

**[00:47:47]** will certainly be the future and then, quite guilty, if I interrupt, then

**[00:47:52]** we return to the era of the good old tradition that software is written

**[00:47:57]** by specifying it as accurately and in detail as possible and generating the implementation

**[00:48:03]** from the specifications into a runnable program, that's then the much

**[00:48:09]** acclaimed implementation detail, which as a board-out owner-manager or as
 
**[00:48:14]** a founder or whatever, the person who has the idea doesn't have to deal with at all.
 
**[00:48:20]** That's simply taken care of by an order agent, in any case.
 
**[00:48:24]** I would now say a relaxing topic and an exciting development, and above all, also a very, how should I put it, fast-paced development, because emotionally this is all, as we said at the beginning, not that long ago, that generative AI came into the world, and supports us in one way or another in our activities.
 
**[00:48:46]** You had another nice example at the beginning with the binaries. Would you like to tell us a bit more about that?

**[00:48:53]** Because you said we had the topic of assembler, we had the topic of binaries, we had the topic of LL.

**[00:48:59]** Where are the Zhaun for you?

**[00:49:02]** Then we can probably also elegantly include the topic of cyber security before we approach the end.

**[00:49:12]** Indeed, so you said you wrote assembler back then.

**[00:49:18]** Now you probably remember that it was totally cool and nerdy and that's

**[00:49:23]** an experience you wouldn't want to know about.

**[00:49:25]** But if I were to say, dear Mark, then write me an iOS app in

**[00:49:29]** Assembler, you would say, sure, that's possible, but it can also be left alone.

**[00:49:33]** One can simply ignore it calmly, yes exactly.

**[00:49:36]** This is simply because Assembler, although it's already an abstraction layer above

**[00:49:43]** machine language, which is comprised of 001 to the masses you know, but it's still

**[00:49:50]** the machine level, where absolute truth reigns.

**[00:49:53]** In Assembler, there is no object-oriented programming, no functional programming, there is

**[00:50:00]** no concurrency.

**[00:50:01]** Assembler is simply what is processed serially through the CPU, and that is not

**[00:50:08]** at all, how should I say, intuitively understandable for humans. You only program

**[00:50:16]** in it today in exceptional cases, such as in control units or devices where you really

**[00:50:22]** don’t have much computational power, but not much memory space. There’s no reason

**[00:50:27]** without cause for higher programming languages, which don’t exist to make a computer

**[00:50:32]** work better, but only serve the purpose that humans better understand what

**[00:50:36]** is happening there. And that's quite fascinating. An LLM doesn’t need that.

**[00:50:41]** An LLM does not need C++, now that’s a bad example. An LLM needs

**[00:50:48]** no Smalltalk or object-oriented CEO to understand object-orientedness.

**[00:50:53]** It's not topic-oriented at all. The LLM can simply understand semantic code and that

**[00:50:59]** can be practically demonstrated when, in the context of such a security talk

**[00:51:05]** given, I simply wrote a little program that turns everything into

**[00:51:12]** such cryptographic demo stuff and then threw it into standard Chat-GPT,

**[00:51:18]** I mean it was four or four or something. So it was sometime in the summer in June or something.

**[00:51:23]** I said to myself, dear colleague, tell me what this program does. And that was

**[00:51:29]** the binary, that was the release binary, meaning compiled without symbols and of course
 
**[00:51:35]** no source code. And he not only told me what this program does, which he
 
**[00:51:41]** can basically do, he can check if libraries are included here, then he sees
 
**[00:51:45]** that it has to do with OpenSSL, which has something to do with cryptography. So he can
 
**[00:51:49]** definitely make educated guesses, but that wasn't all, rather he disassembled the
 
**[00:51:54]** program for me and also wrote C code for it. He said, I've
 
**[00:52:01]** understood what the program does, here is the sender code, and I believe the C code
 
**[00:52:07]** for it would look like this and essentially rewrote the program in C for me, and that is
 
**[00:52:12]** I found that really cool, because for me it had two insights,
 
**[00:52:21]** one is, we actually might not need a programming language anymore, someday when the LLM,
 
**[00:52:28]** the one that is the sheep of agents, is good enough, why should they then produce something that a

**[00:52:34]** People still read, this is extremely inefficient, they can directly generate the closer artifacts.

**[00:52:40]** That’s one thing, and now I skillfully bridge to

**[00:52:44]** Service Security. We all know, dear listeners, dear Mark, when a

**[00:52:52]** manufacturer releases an update for something like an iOS update or Windows or something like that, then

**[00:52:57]** you should install it as quickly as possible. And why should you do that and not wait

**[00:53:02]** weeks? Because the wicked boomers, who have made it their business to profit from

**[00:53:10]** software vulnerabilities, whether they sell the exploits they find to

**[00:53:16]** interested parties or whether those interested parties

**[00:53:20]** are using it to write ransomware, conduct espionage, have

**[00:53:26]** our citizens snoop on or otherwise, these people take an update and

**[00:53:33]** compare the update with the state of the fire department or look at the update and

**[00:53:40]** we then see what this update brings for programming, namely which security vulnerability

**[00:53:47]** has been closed.

**[00:53:48]** I'm taking back to the good old days when you still downloaded updates yourself,

**[00:53:52]** Let’s turn back to history.

**[00:53:55]** You could take in a Windows XP Service Pack,

**[00:53:58]** throw it into a disassembler if you had the nerve

**[00:54:00]** and check what they had fixed in there.

**[00:54:03]** And with enough expertise and time, you could see very precisely,

**[00:54:08]** which security vulnerabilities had been fixed.

**[00:54:10]** And when I see that, I can of course very specifically

**[00:54:14]** write exploits for the systems that have not been patched yet.

**[00:54:16]** So, that always required a certain toolset

**[00:54:21]** And that, above all, required a lot of knowledge.

**[00:54:23]** And I can now do that with an LLM.

**[00:54:25]** And I did, so I told about this site of that program.

**[00:54:28]** Now I also wrote a second program with an explicit security vulnerability.

**[00:54:33]** I had it analyzed and did exactly that, then wrote a patch,

**[00:54:37]** also threw it in again as a patch file, and said, now, tell me what happened.

**[00:54:42]** Is there a security vulnerability?

**[00:54:43]** And then I was told, yes, indeed, this patch has a security vulnerability.

**[00:54:48]** And as it goes, I say good, then I have to prepare a presentation,

**[00:54:51]** write the exploit for it, he is always a bit reluctant and says no, I can’t do that,

**[00:54:54]** I’m making a security model, but you can get around that. And then he told me

**[00:54:59]** I wrote an exploit for it, complete with instructions, so fully with shellcode, the near-exploit,

**[00:55:06]** with a demo Python script, how I have to use the exploit. And all of this only from these

**[00:55:12]** from this patch that he read from it. This means the time we now have to patch the system

**[00:55:20]** after the release of a security update is getting shorter and shorter,

**[00:55:26]** because the interested parties no longer have to sit down manually,

**[00:55:30]** they just throw the stuff into the LLN and let it search for the security vulnerability. And even

**[00:55:34]** if the exploit that comes out of it doesn't work one hundred percent or doesn't work at all,

**[00:55:39]** they already know for sure where they need to look themselves, and that is

**[00:55:44]** of course a totally dramatic development because it shifts the imbalance unfavorably.

**[00:55:52]** We simply have in the future or we already have much less time to react to ourselves

**[00:55:56]** and I’m talking about the whole topic with, so I’m actively setting an LM now to

**[00:56:04]** to penetrate a website or to question an infrastructure. That’s a completely different topic.

**[00:56:11]** I’m all about software. And that’s already a development about which I still read far too little in Besse.

**[00:56:18]** Because what you can already do with it, unfortunately, is really shocking.

**[00:56:24]** Which also brings us to, even if it sounds a bit macabre, the same topic.

**[00:56:29]** it advances people in their profession. Unfortunately, in this case the people who,

**[00:56:35]** I'll say it this way, having nothing good in mind, but even there you can now, I'll say it this way,

**[00:56:41]** quickly come to a result with less expertise, and those who have more expertise,

**[00:56:47]** as I said, even if it's negative at that point, they get to their goals faster and better

**[00:56:52]** and continue towards their objectives. And as you said, this is only the topic of software. That

**[00:56:57]** the whole topic of how well does it actually work that you deploy the LLMs, not only to penetrate websites

**[00:57:05]** but also to capture effectively.

**[00:57:07]** I send it out, bam, we react to people, I open chats, I try to engage through

**[00:57:15]** whatever kinds of conversations on social media or otherwise to get people

**[00:57:19]** to buy, to click, to move, or whatever, because on the other side

**[00:57:25]** even targeted perhaps for me, in my context, for my layout, for my

**[00:57:31]** persona, corresponding anchors are being implemented and the whole thing is basically now in the

**[00:57:37]** hands of anyone who I would say, to put it bluntly, maybe puts down

**[00:57:41]** the 29 euros or whatever it costs for LGBT month or here please use the LLM of your choice

**[00:57:46]** with dogs in hand, to do things, because convincing that it’s

**[00:57:51]** I’d say does something, where its own ethical principles or however it is hindered.

**[00:57:56]** Yes, then you just formulate it a bit differently and then it’s all good.

**[00:57:59]** Okay, so for school and I don’t know what, we’re happy to do that.

**[00:58:04]** That’s right.

**[00:58:05]** Now I can conclude this to a conciliatory ending.

**[00:58:09]** I can also lead back to the hard side that the use of LLMs

**[00:58:15]** in software development to avoid security vulnerabilities

**[00:58:17]** has naturally also become an unprotectable good. I was just mentioning this embedded project,

**[00:58:25]** vehicle control and there are in the automotive sector a norm or a standard,

**[00:58:33]** according to which you have to program in C and C++ to get through this certification for vehicle manufacturers

**[00:58:40]** which simply has safety requirements, safety. That’s MISRA C or MISRA C++. Those are

**[00:58:48]** about 100 pages of guidelines, works, detail that every developer hates, which you can certainly check

**[00:58:55]** automatically. And I believe for SonarQube and all these static code analyzers you get

**[00:58:59]** plugins to check that. But as a developer, you don’t want to wait until

**[00:59:06]** compilation time, a bit or in the build pipeline on your code being compliant, but you want either to have the code checked directly when committing or you want the LLM to generate the code directly that is compliant and that works really well.

**[00:59:24]** have a rule set written for this project and it's just, you buy the

**[00:59:31]** MSAC standard, that's copyright protection, otherwise you have to buy it, it's not

**[00:59:34]** incorrectly available.

**[00:59:35]** Then you throw that into your LLM of choice and say, please build me LLM there.

**[00:59:43]** get the readable guidelines out and please put them in the text file and then you give that

**[00:59:47]** as a prologue for your agent and you say the code you produce

**[00:59:52]** my friend, it must please comply with these guidelines. It actually always works well.

**[00:59:58]** The good thing is, this LM-readable format is not so long that it significantly

**[01:00:05]** reduces the context. So I haven't hit a limit yet and in case of doubt

**[01:00:11]** you just do an analysis run in between and say

**[01:00:15]** so, please analyze this file and analyze the whole project. You must

**[01:00:20]** is not always about connecting. So if the context runs out with the generation of code,

**[01:00:25]** but rather says, now build code in God's name and then I'll check it myself later.

**[01:00:30]** And that is of course quite fascinating because we are moving very much towards the time of the EU

**[01:00:37]** Cyber Resilience Act, which will come into effect permanently in 2027 and requires secure software that is

**[01:00:46]** produced in its environment, and all the regulations that you then need,

**[01:00:52]** on detailed coding guidelines, risk-based threat analysis, so Vulgos-Fed model and

**[01:01:00]** and and. You can, you can and should do all of this today with AI support. So

**[01:01:06]** there’s no reason anymore to let developers run around with hundreds of pages of development guidelines

**[01:01:12]** or to require a team in a corporation to do it themselves, because making FAT models on their own

**[01:01:21]** without external support. If you look at what a standard GPT can do for a FAT

**[01:01:27]** model, you just say, I’m thinking of a Fiki web and say, build me one

**[01:01:31]** a FAT model of. Just that is already so much more than what an untrained team can do.

**[01:01:37]** These are things that help us with the security implementation of the re-A.

**[01:01:43]** and this scenario with the Diné analyzer, to put it a little into perspective.

**[01:01:49]** You just have to use it. You just have to use it sensibly.

**[01:01:51]** And that's where it ultimately comes down to, as always in life, my dear Mark,

**[01:01:56]** when you're of our advanced age, you know that.

**[01:01:59]** You've now brought up our advanced age for the 3rd or 4th time.

**[01:02:03]** Yes, you threw it in for the first time.

**[01:02:05]** let me bring this to a close, the truth is always in the middle and in the combination

**[01:02:10]** of many possibilities.

**[01:02:11]** I don't believe that we have one system that creates flawless software

**[01:02:16]** but rather that we will have agent-based systems, we will have spectrum development

**[01:02:21]** we will have parts where we, in the end, just like now in my evaluation project,

**[01:02:28]** work manually and granularly with this thing to also test limits,

**[01:02:32]** we will have these requirements and guidelines in LLMs. And all these things, you

**[01:02:38]** had somehow, I believe, touched on briefly at the beginning, with documentation writing or

**[01:02:43]** also writing tests or, or, or, those are then by-products that are quite nice. But I

**[01:02:49]** believe overall this topic significantly changes our work in development. So

**[01:02:56]** also documentation standards. Now I have given the customer a test before the test reconciliation,

**[01:03:02]** I really don't sit down and write documentation in Word anymore. I tell the LLM like this,

**[01:03:06]** please generate documentation for this project based on use cases. You know the project, 

**[01:03:11]** you know how it looks, you know what the UI looks like, you built it closely.

**[01:03:14]** That was, when I see, you built it closely. Yes, exactly. So, and that is of course a

**[01:03:20]** a completely fantastic thing. And then yes, it saves time on the settings that I can then use elsewhere
 
**[01:03:26]** sensibly. In this specific case, I haven't programmed anything else now.

**[01:03:33]** in the time I saved, I could think about new use cases, I was able to speak with

**[01:03:37]** the customer more intensively, and so on. So the work shifts. And I have

**[01:03:41]** heard somewhere the funny saying, as long as the LLM doesn't discuss with the Product Owner

**[01:03:47]** as a developer does help me. It may seem a bit flippant, but there is some truth to it,

**[01:03:53]** because ultimately, in a software project, how many percent

**[01:03:56]** is pure implementation and how much is all the surrounding trim? Architecture,

**[01:04:01]** coordination, especially in project work, aligning with customers, the rational customer decision

**[01:04:06]** and so on. So I believe developers shouldn't worry too much that

**[01:04:11]** they will lose their jobs to AI per se, but I dare say that they will be unemployed per se

**[01:04:17]** will be, when one wants to have AI from their explorer in their households.

**[01:04:22]** You said, after the motto, advanced hour towards the end, you've mentioned all our

**[01:04:28]** terms again, yes, you can really see the professional here, just once more

**[01:04:34]** beautifully to summarize, to present the best, the nice thing is, we will see each other on

**[01:04:40]** the podcast afterwards, it's only an audio version. From that side I have his

**[01:04:43]** seen a questioning look in the room. Yes, I mean you, Klaus. You definitely belong to

**[01:04:49]** the people I consider not only extremely competent but also to those

**[01:04:56]** with whom one can talk about all this stuff, so

**[01:05:01]** that one still understands it even when terms are used

**[01:05:05]** that might not be in one's own Jaguar. From that side, not

**[01:05:12]** enough praise, but thank you for being here. I enjoyed listening to you. I got the

**[01:05:19]** took one or two things with me as well. And who knows when we will meet again in what

**[01:05:25]** podcast episode or maybe finally in person again.

**[01:05:31]** So from that side, I would like to say thank you, Klaus. Very much. We’ll see each other later at the walker race, right?

**[01:05:38]** Yeah, we'll see. Oh dear, I just have images in my head. I think with Sora we could also generate those images.

**[01:05:45]** But maybe we'll have that ready someday, and we'll see.

**[01:05:48]** I would certainly be happy if we manage to do it before the walker race.

**[01:05:53]** Thank you very much, and to all the listeners. We’ve gone a bit longer.

**[01:05:58]** But yes, hopefully the conversation was still interesting for all of you, if it was

**[01:06:05]** worthwhile. Thumbs up, stars, wherever in whatever podcast player platform, feel free

**[01:06:11]** to rate us. Let your friends and acquaintances know if you didn't like it, 

**[01:06:15]** send us a little comment so we can react to it, and with that I’ll say

**[01:06:21]** goodbye. Bye. Bye.

**[01:06:51]** and especially to join in the discussion.
