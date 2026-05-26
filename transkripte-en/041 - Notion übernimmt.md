---
title: "Notion übernimmt"
episode_index: 41
published: "Mon, 25 May 2026 03:59:00 +0000"
duration: "3707"
page_url: "https://think-ai.podigee.io/43-notion-uebernimmt"
image_url: "https://images.podigee-cdn.net/0x,sXORXp3kUYGQwj_v7RxTK4j41nepmldGaZH1l-wx9_7M=/https://main.podigee-cdn.net/uploads/u73317/6b236be7-a14b-4011-bd7b-afb7436266b8.jpg"
audio_url: "https://audio.podigee-cdn.net/2497534-m-1e3bbe292560552329e00be3991c64db.mp3?source=feed"
guid: "7ece111323b0a7ccbf006d510c1daf18"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-05-26T10:13:14+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/041 - Notion übernimmt.md"
translated_at: "2026-05-26T10:13:42+00:00"
---

# Notion takes over

**Published:** Mon, 25 May 2026 03:59:00 +0000
**Duration:** 3707
**Web player:** https://think-ai.podigee.io/43-notion-uebernimmt
**Cover:** https://images.podigee-cdn.net/0x,sXORXp3kUYGQwj_v7RxTK4j41nepmldGaZH1l-wx9_7M=/https://main.podigee-cdn.net/uploads/u73317/6b236be7-a14b-4011-bd7b-afb7436266b8.jpg
**Audio:** https://audio.podigee-cdn.net/2497534-m-1e3bbe292560552329e00be3991c64db.mp3?source=feed

## Description

The end of tape solutions
Mark and Dirk Beckmann (CEO of digital agency artundweise) talk about what Worker, Managed Agents, and the new openness mean for companies that want to seriously implement AI.

In the style of an Apple keynote, pre-recorded, calmly presented, and with consequences that go far beyond 'just another API'. The two central building blocks: Worker and Managed Agents.

Workers are small TypeScript programs that run on the Notion platform. Written with the help of AI, executed deterministically, meaning no token costs, no hallucinations. An agent in Notion can use these workers as a tool. This allows for creating everything one would otherwise do with n8n or Make, but within one's own system.

Managed Agents from Anthropic can now also be integrated into Notion workflows. Long-running tasks, external triggers, isolated sandboxes without the need to run infrastructure oneself.
The exciting part: Notion actually sells tokens ('we sell work'). With the Worker platform, the company opens itself up to local models, own scripts, and external providers. A step that may cost revenue in the short term, but solidifies the platform in the long run.

## Transcript

**[00:00:00]** Welcome to ThinkDifferent, ThinkAI, the podcast by Mark and Jens.

**[00:00:07]** Two technology enthusiasts who not only talk about artificial intelligence but live it.

**[00:00:14]** Here you will find clear classifications, genuine practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Food for thought, for smiles, and above all for discussion.

**[00:00:33]** Welcome to a new episode of Psyngtiffin Psyng AI.

**[00:00:37]** Jens would love to be here today, but he has somehow made it a tradition,

**[00:00:43]** that whenever we have a guest to discuss Notion,

**[00:00:47]** Jens somehow is absent. This time he's not on vacation or anything,

**[00:00:51]** this time he is sick. Wishing you a speedy recovery, Jens.

**[00:00:53]** Jens and hello Dirk, great to have you back. I'm very pleased that we can discuss today about

**[00:00:59]** Talking about Notion. And you won't believe how happy I am, dear Mark, that I get to talk about

**[00:01:04]** Notion. Yes, yes. Well, it actually is the case that in the meantime I've been seeing more

**[00:01:10]** people around me who are dealing with Notion or are getting into Notion,

**[00:01:18]** who were kind of inquiring in their companies, who among you knows Notion, uses Notion

**[00:01:25]** and depending on the company you'll find more or less, but everywhere you find people who are into Notion.

**[00:01:32]** And I already mentioned in the last episode, you know, Notion, it's a bit like back then

**[00:01:39]** went by, until then, and you always said, use Notion, you always said, use Mac,
 
**[00:01:44]** Yes, I also said back then, it makes sense with Mac, and somehow with Nautchen too.

**[00:01:48]** That was version 3 here, right, when they started to actually bring in proper AI.

**[00:01:53]** And then we also talked in the podcast about what Nautchen brings and does for you.

**[00:01:59]** And just to jump into cold water.

**[00:02:03]** Nautchen has done something again.

**[00:02:05]** And then we said, let's have a spontaneous conversation.

**[00:02:08]** What did Nautchen do?

**[00:02:11]** Well, they actually did something that one wouldn’t have expected for a long time. They really opened up to developers, launching a Notion Developer Platform just a few days ago, in a style reminiscent of Apple with pre-recorded keynote-like presentations, like Apple’s reboot, like Apple’s unfortunate things, like Apple’s reboot, we both don’t like that, we want to see something live, but now it is like that.

**[00:02:35]** And that’s how they did it.

**[00:02:37]** And Ivan Sao, the head, started off and said, yes, we now have a real

**[00:02:41]** developer platform and the most important tool there is the Worker, so a, technically

**[00:02:47]** you can explain that better later, but a program part running on the Notion platform,

**[00:02:53]** which can access Notion natively, on all sorts of things via the

**[00:02:58]** API and can access Notion in return.

**[00:03:00]** And that’s already a really big step.

**[00:03:03]** because it was already published and tested in the Alpha, in this ambassador program, but

**[00:03:08]** I don’t have much knowledge about CLI programming and that's why I didn’t actually do it

**[00:03:13]** until it reached this point.

**[00:03:15]** And now I’m totally fired up about it.

**[00:03:18]** What I appreciated about the E-Note or the video recording, pre-recording, ah, whatever.

**[00:03:25]** What I really appreciated was actually this atmosphere that you created

**[00:03:30]** dark room, wooden chair, I sit down, speaking with a calmness and conviction,

**[00:03:37]** not calmness in the form of sleeping pills, but a calmness in being aware

**[00:03:42]** of what you’re showing. One is really interested, the Wellerpaum, was aware,

**[00:03:47]** that you are basically doing something new, very unexcited, but in what you showed,

**[00:03:53]** everything seems so, I would say I’m now a beginner compared to many others in

**[00:04:01]** Notion, but it seems a bit okay, we’re now also showing everyone who has Notion,

**[00:04:06]** there’s this developer community, this CLI, I don’t know, what kind of tools and you had

**[00:04:13]** already mentioned the topic of Worker in your mouth and CLI, so CLI is the opportunity,

**[00:04:20]** that we can intervene with things via the command line, Command Line Interface. We

**[00:04:27]** already know this from code, there’s a CLI, we know it from Codex, there’s a CLI. The

**[00:04:33]** fewest people in everyday life grapple with a terminal window or in a, what’s it called

**[00:04:41]** in Windows, CMD, command, ah, I don’t know, people who see black screens with a blinking

**[00:04:46]** cursor know what I mean and those who don’t know what a blinking cursor

**[00:04:50]** on a black screen is. Welcome to the new world. You presented something

**[00:04:55]** and I also watched that video after you sent me the link again,

**[00:05:01]** as preparation for today and I’ll try to summarize in my words what

**[00:05:06]** they showed us there. Because they addressed something, and I had a completely different view

**[00:05:10]** on it, that I always wondered how

**[00:05:14]** Notion will deal with these problems and I want to briefly expand, when you

**[00:05:18]** look at other hashers like GitHub Co-Pilot and so on, so Microsoft, you see that the

**[00:05:25]** pricing is going through the roof. They have announced new pricing models, prices will rise,

**[00:05:29]** will rise, will rise, will rise. And not because new models are coming,

**[00:05:33]** but simply because they charge differently. There are somehow no more subscription models

**[00:05:37]** and stuff for enterprise customers. And now Notion also addresses the

**[00:05:43]** business market. That’s very strong. And I’ve always wondered how they

**[00:05:47]** will maintain that with the pricing, because, they’re not small, but the costs are also

**[00:05:53]** a challenge for them. How do we remain attractive in terms of price? And I think what you just presented with this Worker

**[00:05:59]** also pays for that. In my perception, the

**[00:06:04]** Worker is the opportunity to write program code and provide it to an agent

**[00:06:10]** to work with, or also to provide it as a juice for developers.

**[00:06:14]** In Notion, it doesn’t really distinguish whether a tool is used by an

**[00:06:19]** agent or already by a human. And you can basically, it’s called

**[00:06:24]** TypeScript, programming language, totally irrelevant, yeah, it’s just a programming language,

**[00:06:28]** in the times of AI, it’s also totally irrelevant which programming language it is. Greetings to

**[00:06:34]** the developers who work for me, they always get on the roof when they

**[00:06:37]** encounter a strange situation. But to make a long story short. You are programming there basically with the help of AI

**[00:06:44]** small code snippets. Because it’s program code, you don’t need token costs, no

**[00:06:50]** AI. It’s reliable. It’s called deterministic. And these code snippets

**[00:06:57]** you then let run at Notion. And that doesn’t sound so boring

**[00:07:06]** but it’s not so boring because you can indeed work with this agents platform,

**[00:07:13]** yes, that's what they presented before, that you can have self-executing, self-supporting

**[00:07:19]** through, through whatever you want, status changes in a dataset or time or what

**[00:07:24]** have you, with these agents you can access these workers and now you can

**[00:07:28]** build an entire universe. You can create a worker that accesses your locally

**[00:07:32]** installed Mestral or you can create a worker that

**[00:07:37]** as you explained to me this weekend, I don't know, retrieves emails somewhere

**[00:07:41]** and so forth.

**[00:07:43]** So everything you might have done with Nacht n or make or saviour, you can

**[00:07:47]** do with this, but in this, let's say, environment completely under your control

**[00:07:54]** and not with a platform and so on.

**[00:07:58]** And you just have it, sure, you have to use Notion for that, but you want

**[00:08:01]** to, you have it in your system. And I find that quite impressive because

**[00:08:06]** they are of course opening up with this and the business model, and you mentioned

**[00:08:10]** it briefly, selling their own tokens, just like we all do now,

**[00:08:14]** because with the agents they also want to sell credits and they do sell them. It's

**[00:08:18]** not subscription-based anymore, but you pay per credits, so you have to pay

**[00:08:23]** 10 dollars for 1000 credits and then they are really, then you pay new money again.

**[00:08:27]** And although that is their business model and they say great, we are now selling

**[00:08:32]** no software, we sell work, so we sell work in the form of tokens and so on,

**[00:08:38]** they still open up, and I think it shows that they still have quite a lot

**[00:08:43]** planned and are not going to stand still at this point,

**[00:08:46]** but are perhaps looking for short-term success to sell even more tokens,

**[00:08:51]** block it, but in return you can attract a completely different community.

**[00:08:55]** And one must not forget, I might be in a small AI nerd bubble right now,

**[00:09:01]** you in your Notion world, but nonetheless, what you just said is that they are opening up in themselves,

**[00:09:08]** is something where everyone thinks, who maybe can’t open Notion,
 
**[00:09:11]** why? What’s so special about it? It is actually something special. Notion has
 
**[00:09:15]** a really great way of storing data, with cell pages, databases, and all that.

**[00:09:20]** seen and everything is kind of the same, and a point why I still believe,

**[00:09:24]** why a company like Microsoft can never get it right, because Notion has done it fundamentally right

**[00:09:30]** in that regard. I think they have also paid a bit of tuition

**[00:09:34]** in the past, in terms of performance or maybe they got a bit ahead of themselves.

**[00:09:38]** And now they have the opportunity, the chance, if I take that,

**[00:09:42]** can be said, through AI, its good data storage and its good interaction capability

**[00:09:49]** to enrich it, making it much easier than the others have,

**[00:09:54]** to integrate agentic systems, to let agentic systems work and

**[00:09:58]** now also again with the Worker regarding opening. The Workers allow me not just to say,

**[00:10:05]** I'm looking to see if, I don't know, an email in Gmail, you just gave that example,

**[00:10:10]** is there, but I can really interact and in the sense of, I'm checking,

**[00:10:15]** I'm logging in, I'm checking if there are emails, I can check if specific emails are there, I can write emails.

**[00:10:21]** I could also check another database, I could use other tools, yes, so what we have in the AI world with MCP connectivity, you can put all that in there too, and the funny thing is, even if I spoke about a strange TypeScript.

**[00:10:36]** Thanks to AI, it doesn't matter to us what it is, because ultimately you can practically wish from the AI what the Worker should do.

**[00:10:44]** That means you have used AI and from then on again a deterministic system.

**[00:10:49]** I find it really fascinating that they built that adhesive tape, that duct tape there.

**[00:10:57]** It always sounds so unprofessional, duct tape, but it is really a special feature that is also simple.

**[00:11:05]** What did you build with the worker? What was it that we looked at there?

**[00:11:09]** So I built it myself, this, well I then,

**[00:11:13]** a bit awkwardly with Cloud Code in,

**[00:11:15]** well not in the CLI, but in this, with this app, from Cloud MacOS App,

**[00:11:21]** Mistral,

**[00:11:22]** connected it so that it runs locally on my,

**[00:11:24]** on my MacBook,

**[00:11:26]** 5M5 Pro,

**[00:11:28]** and not really, what's great is it can, but it was cool to see that it

**[00:11:32]** works just without internet,

**[00:11:33]** there's AI.

**[00:11:34]** It only has training data, and it doesn't have the fastest version yet, but

**[00:11:37]** a very good version that is already running, and I wanted to use that with Notion, wanted

**[00:11:41]** to find out if that works, and then I built this worker with Lord.

**[00:11:44]** But what I found a bit more realistic was the question I asked you,

**[00:11:48]** namely that I regularly check a specific Gmail account, and therein we then

**[00:11:54]** come to the first mode that this worker can take.

**[00:11:58]** It's a really supported, well actually proprietary mode, namely the

**[00:12:02]** so-called Sync.

**[00:12:03]** And I didn't even realize that this is such a mode, then you wrote

**[00:12:05]** me somehow how I do it in which order. And then I

**[00:12:09]** actually did that in this CLI, in this terminal I entered everything.

**[00:12:13]** That worked super well. Then I used the Cloud Code on Terminal and not on Desktop.

**[00:12:19]** And everything worked out. And now I have a worker that regularly checks, in this case

**[00:12:25]** every 15 minutes, a Gmail inbox for what comes in. And the crucial point now is,

**[00:12:30]** the worker creates the database initially, Notion creates the database,

**[00:12:37]** where things are supposed to come in and then defines what it is, in this case there are 5, 6 sync fields and

**[00:12:44]** they also have a special title, because they are basically synced from an external

**[00:12:49]** tool, so to speak, and then you can create some more yourself,

**[00:12:53]** as you know, but this is a new, new type of database field, namely

**[00:12:58]** a special type, and you can extend that as much as you want. Now you can make the worker look up something in another database and what

**[00:13:07]** links and so on. I haven't done that yet, but... and let's say with instructions, that I also needed, because I'm not, as I said, a

**[00:13:14]** real developer, rather I count myself as someone who just does sort of half-developer stuff. That was good?

**[00:13:21]** So the instructions you made for me were good, but I needed them too. Of course, they were super tailored to

**[00:13:27]** my case. So I could just copy-paste it. I didn't have to

**[00:13:31]** understand what I was copying-pasting. And I was just glad that it came from you and I

**[00:13:36]** thought to myself, okay, you wouldn't build something stupid for me. And well, that's not

**[00:13:39]** a security-wise, that's not a recommendable approach now. But if the

**[00:13:45]** cousin does it, then it must work somehow. In fact, for

**[00:13:49]** non-developers, I find it not to be such an easygoing process with this CLI thing. You have to

**[00:13:56]** understand all the nomenclature and so on, you can fumble through, it's

**[00:14:01]** not super ideal yet, but it is indeed possible even if not quite 

**[00:14:05]** perfectly, and finally, Notion is also trying now in many small videos and on the developer platform to get the

**[00:14:11]** original Notion people on board because many won't go this way because

**[00:14:16]** they see this weird, strange cursor thing and say no, I'd rather do it myself.

**[00:14:20]** then I'd rather go back to night n so that's already a small hurdle but

**[00:14:24]** But of course, you have completely different options.

**[00:14:27]** Because I will tell you what I did with the workout.

**[00:14:29]** Maybe two things, because as you just mentioned,

**[00:14:32]** first, N8N greetings to SAP, who somehow

**[00:14:35]** has announced a partnership cooperation, participation,

**[00:14:38]** something along the lines of

**[00:14:40]** future processes of SAP,

**[00:14:43]** will be supported by N8N, which made me think.

**[00:14:47]** Yes, okay. Honestly, for N8N

**[00:14:50]** I personally wouldn't do much more,

**[00:14:52]** it's good for SAP, but the hammer shall be placed there.

**[00:14:57]** No, with N8n there is also something like Make, you mentioned that you

**[00:15:01]** use it, Make.

**[00:15:02]** And they also announced a CLI now, or rather published one.

**[00:15:06]** From that side, it seems like it is already quite something.

**[00:15:10]** When I think about when I started with IT, we worked with text screens.

**[00:15:16]** Then we celebrated that we got a UI, be it Geos on MS-DOS or Windows.

**[00:15:24]** And now, what are we doing?

**[00:15:26]** Now suddenly we’re all stuck back in text windows in the terminal.

**[00:15:29]** And I actually need to say honestly,

**[00:15:32]** all the people I know from Apple and so on, I'm sorry,

**[00:15:35]** I'm spending more time in the text window than somehow in the graphical user interface

**[00:15:39]** and I actually find it not so bad.

**[00:15:41]** Let’s see if something pretty comes along again soon,

**[00:15:43]** but the developer conferences are coming up soon.

**[00:15:45]** Now I said, let me tell you what I can bring to the table as a worker.

**[00:15:50]** Not Mistral, but Hacking-Field.

**[00:15:55]** No, Hacking-Face, Hacking-Face, I always mix them up.

**[00:15:56]** Hacking-Face, Hacking-Face, you can, in simpler terms, access AI models and run them locally.

**[00:16:04]** For example, image generators, video generators, voice cloning.

**[00:16:08]** And I built a worker that creates images for me.

**[00:16:13]** I built a worker that creates podcasts from texts in Notion. And you have

**[00:16:23]** your stuff in Notion and then you hand the worker to the agent

**[00:16:28]** and then the agent uses the worker to create an audio file with your voice and

**[00:16:34]** everything locally. And it knows nothing without any cloud. And that is already, that's quite nice,

**[00:16:40]** Yes, so I can also run an M5 MacBook, yes, we are the friends of Notion and that

**[00:16:45]** Apple, we have already glorified that, and then you stand there and think, okay,

**[00:16:51]** everything might take a bit longer than with 11 Labs or Nano Banana, but I

**[00:16:57]** would say, for the fact that it costs me neither tokens, no, it costs me no tokens and

**[00:17:04]** it’s basically done in the background, it's quite fascinating, if

**[00:17:10]** you think about the fact that, okay, I couldn't do this with Notion before. I could do it

**[00:17:14]** before also with other AI systems, yes, I mean, my third favorite hobby or

**[00:17:19]** so is skills in cloud code and so. But it was impressive to see and then

**[00:17:25]** I also thought, if you are someone who has your company in Notion, who,

**[00:17:33]** I would say, in creative unprofessionals. Who could that be, yeah. Who could that be,
 
**[00:17:38]** I don't know. And then you connect that and basically, I don't want to say that you can automate everything with it or not, yeah, but you have these tools available for people who might use them with an eye for creativity and aesthetics and then receive these modules, these artifacts, these results in the system, in their operating system, in their, whatever you want to call it,
 
**[00:18:08]** offered, and that's just the tip of the iceberg. Yeah, that's just the tip of the iceberg.
 
**[00:18:14]** Just to briefly understand that. So Hackingface is a provider that does,
 
**[00:18:21]** that any of these whole models like... You can subscribe there.
 
**[00:18:25]** No, no, no. Those are proprietary models. Those are completely proprietary models,
 
**[00:18:29]** that you can consume at Hackingface. There are also options for subscription and free and
 
**[00:18:35]** commercially free and commercially for payment. There are a lot of different things. The funny thing
 
**[00:18:40]** is that you also get models there. For example, I recently downloaded a model
 
**[00:18:45]** from Microsoft, where you can throw audio files in, and it then does
 
**[00:18:51]** person recognition and transcription on the audio file. And you just let it do that on

**[00:18:56]** run locally from your box, which is of course much cheaper than if you say,

**[00:19:01]** at home against cloud models, and of course now with something like Worker then

**[00:19:06]** is also simply to integrate. So this hacking face thing that generates the podcast for me,

**[00:19:13]** that took about half an hour and then it was up and running, that's pretty funny.

**[00:19:18]** Then I can normally use, as the agent now mediates between Notion and

**[00:19:23]** the Worker and the agent, I call it up and then I have this tool. And

**[00:19:28]** the tool runs on my computer, and if I want to deploy it now, that is, if

**[00:19:34]** it should be used by other people, then we have to think about which computer

**[00:19:38]** it runs on.

**[00:19:39]** Exactly, then it has to run on another one, it has to, as they say, it should

**[00:19:43]** run on another computer, which is quite relevant for my workflows now.

**[00:19:48]** that's fine with me.

**[00:19:50]** I might not have an M5 like everyone else.

**[00:19:54]** Please.

**[00:19:55]** no matter if you were Pro Max or not, you do need a bit of RAM, you do need a bit

**[00:20:01]** not CPU now, but graphics card or AI accelerator like in Apple's processors.

**[00:20:07]** I don't know, if you get a DJI Spark from Nvidia, like a box that

**[00:20:13]** you can put in the office and address from your television, that should

**[00:20:17]** actually work wonderfully too, because the worker is just told,

**[00:20:21]** there is the stuff, address the model and then the model is there. So that

**[00:20:26]** shouldn't be a problem, it won't be a problem, I just haven't

**[00:20:31]** done it yet. And these models that Hacking Face provides are

**[00:20:38]** indeed models that are also part of others, like Ulama or, so that's

**[00:20:44]** somewhat similar or what's special about it, because otherwise I haven't

**[00:20:47]** understood the difference yet. Ulama is a language model, so you can

**[00:20:50]** plug in language models to do text chat. And the models you get at Hacking Face

**[00:20:55]** are not specialized in generating AI in the form of, I say, write

**[00:21:01]** me a poem about the Eiffel Tower, but multimodal models, generate me videos,

**[00:21:06]** analyze videos for me, okay. That's basically the same, one is just

**[00:21:11]** for text-based stories. Yeah, okay. So I think I understand

**[00:21:15]** it now. And that means you have now connected this Hacking Face and can

**[00:21:19]** now somehow use all sorts of models in the worker.

**[00:21:23]** You can tell which models from Hacking Face are available with which

**[00:21:28]** runtime environments those models work. Not everything works on one

**[00:21:34]** Mac, some things really need an Nvidia, some only run on

**[00:21:38]** Nvidia not on the Mac, some only on the Mac, not on Nvidia, some everywhere.

**[00:21:42]** Some models are bad, some are good, it's a huge selection, you have to

**[00:21:46]** still look a bit at what is currently, I would say, currently relevant. Basically, I would

**[00:21:51]** say that the photo, video, and audio models are very close to what you might like to get out of it,

**[00:21:58]** so Voice Cloning, it needs 15 seconds of my lovely voice and can imitate me very well

**[00:22:05]** in different languages. And that's already, so I have to see what the model

**[00:22:13]** was called. Hacking Face is just the delivery form and the model itself

**[00:22:18]** we need to bring up. But it's definitely worth looking into because, yes,

**[00:22:23]** I can only repeat myself. It costs you no tokens, you have no

**[00:22:26]** data privacy issues, because it just runs on your device.

**[00:22:29]** You just need a box with a bit of

**[00:22:32]** RAM and a bit of muscle that can execute these models, and I admit

**[00:22:38]** I can tell it's running because, for me, the fans can definitely get loud.

**[00:22:41]** What you’re running can be quite audible.

**[00:22:48]** Well, and I mean, what’s important for our target group as a company is many medium-sized

**[00:22:57]** Companies in Germany are of course also reliant on the fact that there are also non-American

**[00:23:03]** models that need to work. So this and that, so they have relatively restrictive

**[00:23:08]** requirements, as they have set for themselves or must adhere to, especially when you consider that the suppliers might also be for

**[00:23:17]** High-tech companies and so on. And they say, okay, please, what is my path now if I can't use all these great American models?
 
**[00:23:26]** And for that, it's obviously great. Especially, it's great that you can, in the enterprise program, already also in Frankfurt.

**[00:23:31]** hosted, and then you somehow installed it somewhere on your computer, whatever infrastructure is needed.

**[00:23:39]** Then you have a model that might create images or whatever you're currently saying.

**[00:23:43]** And suddenly you have a solution that just a few days ago seemed unthinkable, exactly this scenario and many, many others.

**[00:23:51]** And this naturally makes it more open and turns it even more into this AI platform a bit.

**[00:23:58]** If you look at it from a user perspective, then you can actually say,

**[00:24:02]** okay, if someone sets it up for you a bit, if you don't feel like doing it yourself,

**[00:24:07]** then a company like us or some other company takes over that, then you can.

**[00:24:11]** you there directly this whole, you have direct access to this whole wonderful AI world,
 
**[00:24:16]** so without even bothering to engage with it a little bit.
 
**[00:24:19]** And if you then have the desire to use a locally installed graphic tool,
 
**[00:24:25]** that is, a model for graphic creation, then it suddenly works. That means,
 
**[00:24:30]** it is so, although technically speaking it may only be a small step, but the

**[00:24:34]** Options are now virtually limitless and before you were at the end. You have to

**[00:24:38]** say that, yes, if you want to work with Norrish and AI, then you will always have to use these

**[00:24:42]** American models, otherwise it just doesn't work. They also always natively complement

**[00:24:47]** more, even small models. I believe Diepsi can now also include some version

**[00:24:52]** And they will continue to do so because the token costs are otherwise always

**[00:24:55]** just really high.

**[00:24:56]** But the fact that it works right now, that you have built that, makes a big

**[00:25:01]** difference.

**[00:25:02]** And no matter where I go, all the companies, the medium-sized companies,

**[00:25:07]** they want a solution for AI, especially in marketing, where we are currently active, they are

**[00:25:13]** always also looking for alternatives and not just saying, okay, cloud

**[00:25:17]** install code or cloud install done, although that's somehow the

**[00:25:20]** You hold what is currently available, but they are either not allowed or it's too expensive for them, or whatever for the management.

**[00:25:26]** In this respect, that's really quite intense.

**[00:25:28]** And you were there.

**[00:25:30]** Hacking Face.

**[00:25:31]** Now I've finally got it out right.

**[00:25:32]** What you have is really that you say to him, you give the person the opportunity.

**[00:25:37]** It is, although possibly an American model, which then runs with you.

**[00:25:42]** Maybe it's worth mentioning again in terms of nuance.

**[00:25:45]** True.

**[00:25:45]** But you can really do video to text, text to video, audio to text, text to audio,
 
**[00:25:50]** rise of recognition in images, understanding of images, image segmentation, image editing.

**[00:25:56]** Sharing, I send an image and you get it back in Photoshop layers.

**[00:26:02]** Calculating what basically is there when you pull the layer away, so that there's not a gap,

**[00:26:08]** because Dirk is currently looking at the camera and I pull Dirk's layer away, then behind it,

**[00:26:13]** is what he thinks should be factored in. So there are really cool things in there.

**[00:26:19]** And indeed, because you said it, Claude Cote here would be, let's say, the benchmark.

**[00:26:25]** It's like a constantly overflowing circle. So there's Croc and then there's Entropic and

**[00:26:31]** then they don't give anything to each other and everyone releases a new model. Maybe at

**[00:26:36]** this point just a hint, you also mentioned Mistral earlier. You can also

**[00:26:41]** install models locally on your computer whether it's Mistral, whether it's Quen, whether
 
**[00:26:48]** yes exactly exactly and you can also link them again with clotcode, so
 
**[00:26:55]** against this CLI from Entropic you can go and say okay we take now

**[00:27:00]** not the opost models from entropic usa, we also don't take the entropic

**[00:27:06]** models that might be hosted at amazon bedrock in the eu 200 frankfurt

**[00:27:11]** but I’m working against a model that is in my basement or on

**[00:27:16]** my notebook and I'm coding with that, but I still have this CLI, code available and

**[00:27:23]** just recently you can even Co-Work, so the app you were just talking about, the

**[00:27:30]** Mac app, I think it’s called Co-Work 3P, and you can configure it like this.

**[00:27:37]** that also works against other models. That you say, okay, I now have my Quen locally,

**[00:27:44]** then there is something called a proxy, which isn’t explained in three seconds, but there are

**[00:27:50]** guides online, and it is also supported by Entropic. They explain it in their

**[00:27:55]** corresponding documents, and then you can run the thing against local models yourself.

**[00:28:00]** However, of course, not everything will work exactly as you might expect it to,

**[00:28:05]** maybe has the Entropic models in the cloud. But you can also see the manufacturers here,

**[00:28:10]** I don’t want to say they are topping up their own business model, but just like Notion says,

**[00:28:17]** well, we do want to sell work, but here is an alternative cheaper solution,

**[00:28:22]** then suddenly Entropic comes along and says, you find our CLI good,

**[00:28:26]** you find our application good, yes, you can also use something else behind it. That is

**[00:28:30]** a bit like they all like to hurt each other a little, I think,

**[00:28:34]** for fun.

**[00:28:35]** Yes, and does one understand the market?

**[00:28:37]** Exactly, and when you think about what they all do, I mean, there are those who really

**[00:28:42]** invest and invest in models and come out with models like Entropic or

**[00:28:48]** Google and so on, and then there are the others who use it, like Apple will

**[00:28:52]** also do now, they essentially just use something.

**[00:28:55]** What Notion does. And I think what I find particularly good about the way Notion works, even though

**[00:29:02]** it's still far from the capacity of Claude, is that it is AI agnostic,

**[00:29:10]** he says. So it doesn't matter which model ultimately prevails,

**[00:29:16]** all the infrastructure. Where do you have your prompts, how do you build your skills and your

**[00:29:21]** factories and how do you put it all together? You have that running, and at some point tomorrow

**[00:29:26]** Gemini comes along with then what is indeed Talos, and then you simply switch over, or

**[00:29:32]** you run these workers locally. This means the likelihood,

**[00:29:37]** that you invest in this abstraction, that it is worth it,

**[00:29:43]** in this abstraction platform or level, just like we are doing

**[00:29:49]** with Notion, I believe has a high chance of being successful because everything remains the same for you

**[00:29:54]** and behind it, some other agent is working away. That also brings us to

**[00:29:58]** Topic, what actually happens? This is yet another worker part they brought with them,
 
**[00:30:04]** which unfortunately isn't testable for ambassadors yet, at least not for me,
 
**[00:30:08]** but it's announced that you can somehow, you need to explain this to me too,
 
**[00:30:14]** use agents hosted by Claude, for example. So, you can explicitly say in
 
**[00:30:20]** this worker, okay, this shouldn't be a Notion AI agent, but
 
**[00:30:27]** some other agent that's hosted somewhere, and that should now do this work. And
 
**[00:30:33]** I thought, when that was mentioned, yeah, okay,
 
**[00:30:36]** then there’s no downside to having everything in Notion, in the whole context,
 
**[00:30:41]** all the content, the entire operating system, literally, an operating system,
 
**[00:30:47]** just like it is for us, because I can just wait a bit and then it will be
 
**[00:30:52]** time to access these external agents. I need to briefly mention, I don't know,

**[00:30:56]** that you saw in the video, you have a Kanban board and then you make a status change

**[00:31:00]** from, let's say, human in the loop, I'll say, release, right, approval and then comes

**[00:31:06]** a small animation showing some external worker with a little icon and a

**[00:31:11]** small movement-animation working on that task. And when it's done, there's

**[00:31:17]** a checkmark. That means you see on your to-do manager, so my colleague is working

**[00:31:22]** now, the Claude agent, somewhere on this. And that's really well done. So

**[00:31:28]** I found that very impressive. Entropic announced what you described some

**[00:31:35]** time ago and mentioned at the announcement that Notion is one of the

**[00:31:41]** first to support this and you can use Entropic's cloud infrastructure,

**[00:31:48]** where AI agents built by you run. So this isn't now,

**[00:31:56]** that you're programming something in a deterministic sense, like the workers themselves,

**[00:32:01]** where you're writing TypeScript and it really makes one plus one equal two,

**[00:32:06]** but you can build things together with skills and prompts and MCPs,

**[00:32:12]** which then react to events depending on what is needed, working in a meaningful way.

**[00:32:23]** And the advantage is, they are really small encapsulated, internally focused, which means

**[00:32:31]** small, small values.

**[00:32:32]** They are encapsulated areas of expertise that do what you want them to do at the time,

**[00:32:38]** that are always ready to go.

**[00:32:42]** At Entropic, there are the usual token prices for the computation plus a very

**[00:32:49]** small opulus that you have to pay on top. Entropic also operates this infrastructure

**[00:32:55]** with special sandboxes, so that the thing doesn’t break out, that it doesn't go crazy

**[00:33:03]** and cause you 5 million euros in costs, even though it should just read the weather,

**[00:33:08]** so that it doesn’t, because you give access, wipe your inbox. There are such cases

**[00:33:12]** had deleted a production database that we mentioned earlier,
 
**[00:33:18]** and then said, it wasn't me. No, no, it must have been you.
 
**[00:33:22]** I wasn't it. That things like this do not happen. And the beauty of it is simply and
 
**[00:33:28]** straightforward, you don't have to ask yourself the question, just like we did with the image- and
 
**[00:33:34]** sound and video agents. Where do I place my server? How do I handle the registration?
 
**[00:33:40]** How do I ensure that the thing is maintained? How do I ensure that the thing is secure?
 
**[00:33:45]** Instead, you get, in that sense, yes, remote-running agents that do not execute program code,
 
**[00:33:53]** but execute prompts for you, because you trigger them.
 
**[00:33:59]** As far as I understand it, you always have to trigger them.
 
**[00:34:05]** I haven't heard that they have their own timing interval,
 
**[00:34:10]** like every hour, but you basically have to send a trigger every hour,
 
**[00:34:14]** so that the thing wakes up and says, hello, I’m doing something. But that would probably be
 
**[00:34:18]** the next cool addition, when I think about it, you build some mail retrievals
 
**[00:34:25]** on one hand using workers and agents in Notion, and on the other side, you say,
 
**[00:34:31]** so, I have noted a few things, and my research skill, which is supposed to extract details
 
**[00:34:39]** like in Plexity, just rebuilt, could then, possibly, do fact-checking
 
**[00:34:45]** and quality control and preparation. You can also tell such agents how to
 
**[00:34:50]** respond, in which file format you would like it, like formatting, for example,
 
**[00:34:55]** always a headline and a subtitle and please everything separated by commas and no
 
**[00:35:00]** idea what else. And I would claim that would round off the picture really well,
 
**[00:35:07]** because this way you can also integrate the non-deterministic world automatically.
 
**[00:35:12]** But what I don't understand is, I can use an Opus 4.7 from Notion and
 
**[00:35:19]** let's assume the output is not a file, but the output is some text,
 
**[00:35:24]** so something, text work, images, so, this can be natively Notion. What is the advantage,
 
**[00:35:30]** then, of using a cloud agent in the cloud? So, what can it do differently, if
 
**[00:35:39]** you just leave out that part? You know what I mean? So, why should I have an
 
**[00:35:44]** external agent? I think that’s great at first because I think the world uses
 
**[00:35:49]** cloud and also Notion, but I understood that you can combine it now. But
 
**[00:35:53]** why should I do that if I can choose? Is there any advantage,
 
**[00:35:57]** using Cloud 4.0, the Opus or whatever, natively from the cloud rather than
 
**[00:36:04]** from Notion.
 
**[00:36:05]** You can delegate work steps and it rarely has to be done on your computer.
 
**[00:36:09]** So if I don't know, I’m doing software and now I'm checking software on
 
**[00:36:13]** GitHub, for example, for code management and I want to document it.
 
**[00:36:18]** Evaluate that for me, create an onboarding document or a what has been
 
**[00:36:23]** done document or something like that, then I can do that with GitHub Actions.
 
**[00:36:26]** So, GitHub actions execute, it can be static code, it can be the
 
**[00:36:32]** request from AI, and if it’s a public GitHub project, it costs me nothing, if
 
**[00:36:38]** it’s a private GitHub project, I have to pay for it. And such things can you
 
**[00:36:42]** let Entropic do. It basically does something with things that are online accessible
 
**[00:36:49]** without you having to have your computer on. That much point and simply, AI will still
 
**[00:36:57]** work when everyone around you is asleep. That if you, I don’t know, whether that’s
 
**[00:37:03]** now a case, yes, the customer presses on a feedback form here, I’ll send
 
**[00:37:09]** my issues away and the thing already evaluates it before they are there and sends
 
**[00:37:16]** the answer back. The agent in Notion would do that too if

**[00:37:21]** the researcher is. Yes, only that the agent exists in Notion and Entropic has also
 
**[00:37:26]** other clients besides Notion. Entropic also has users who not only...
 
**[00:37:32]** Not the other way around. So the possibility that has arisen since the 
 
**[00:37:36]** development or announcement of the Notion Developer Platform, or the
 
**[00:37:41]** one that is coming soon, is that external agents, as you described,
 
**[00:37:44]** can be seamlessly integrated into Notion. I don't have to program anything,
 
**[00:37:49]** I can simply configure it in some way and then
 
**[00:37:52]** it works. And in this demo, I saw that I am in a task and this
 
**[00:37:57]** task maybe has some information from the customer on our
 
**[00:38:01]** homepage that still shows the old product and the old
 
**[00:38:07]** product image, please swap that out, and then it can somehow be passed
 
**[00:38:10]** to this external agent who would do it, he would check out the
 
**[00:38:14]** code from this homepage, change it and check it back in. I understand
 
**[00:38:18]** that. What I don’t understand is, well, Notion does that with the agents just
 
**[00:38:24]** the same way. The agents certainly differ from these personal agents, where
 
**[00:38:30]** you have this chatbot in the bottom right corner, simply by the fact that they
 
**[00:38:33]** are hosted by Notion and just always run. You can share them, if you
 
**[00:38:39]** have shared the agents, you can share them just like any page
 
**[00:38:42]** with 20 people or with a group, then everyone can use this agent.
 
**[00:38:47]** It's not just related to you.
 
**[00:38:49]** And I haven't understood this difference yet, why one should use the cloud agent
 
**[00:38:54]** and not the Notion agent.
 
**[00:38:58]** Yes, phew, exciting question.
 
**[00:39:03]** Whoever knows that is welcome to leave a comment, but as far as I understood
 
**[00:39:09]** it.
 
**[00:39:10]** The agent is part of the user interface and a function that runs in Notion and the Entropic
 
**[00:39:16]** Manage Agents, or whatever you call it, yes Manage Agents, is basically the underlying cloud
 
**[00:39:23]** infrastructure that is offered by Entropic. I'm not even sure if these
 
**[00:39:29]** agents from Notion do not even run there. How much you need that as a user,
 
**[00:39:38]** I couldn’t really tell you, you would probably have to spend some more time
 
**[00:39:44]** on it, I do see a certain gap, a certain gap there, but if I
 
**[00:39:49]** were to think about it, maybe you’ll prove me wrong, but this Notion agent, it
 
**[00:39:53]** does things like creating text, maintaining databases, analyzing Notion pages and a Managed
 
**[00:40:02]** agent at Entropic can work outside of Notion. It can address things outside of Notion.
 
**[00:40:10]** It can maintain permissions both outside of Notion and in Notion. So I believe,
 
**[00:40:20]** it becomes interesting simply when you say, okay, I have things,
 
**[00:40:24]** which I can’t manage with a worker and an agent in Notion alone,
 
**[00:40:29]** or maybe I don’t even have Notion in the intermediary since I say,
 
**[00:40:34]** I connect my email inbox to Spotify and any results only interest me later,
 
**[00:40:41]** but not during this initial call that you get further help there.
 
**[00:40:47]** And of course it is the case that if it’s about really writing code based on
 
**[00:40:53]** a trigger that comes from Notion, then it’s clear, in my opinion,
 
**[00:40:58]** Notion can’t do that.
 
**[00:40:59]** I don’t know, maybe I just haven’t understood it yet, but I don’t believe so.
 
**[00:41:02]** This means that if I then have this external agent, who knows my entire system,

**[00:41:07]** that somehow understands GitHub and then knows that at this and that point I need to

**[00:41:12]** check something out to do something, which Notion alone couldn't do.

**[00:41:15]** So there are definitely enough use cases when you expand the formats.

**[00:41:19]** But exactly.

**[00:41:20]** I was actually just thinking, is there really a difference if I use the

**[00:41:23]** same format.

**[00:41:25]** Probably there isn't, it's more about how it can interact with other systems

**[00:41:29]** differently.

**[00:41:30]** Claude for example or then also others.

**[00:41:33]** Yeah, okay.

**[00:41:34]** And the agents can really work for a long time.

**[00:41:37]** Yes, so these management agents can also handle really long tasks, well you have to
 
**[00:41:42]** pay for it, but they can map long workflows where I don't
 
**[00:41:47]** know where the time limit of classic Notion has been lifted, yes, from that side.
 
**[00:41:57]** And how would one, if I may ask briefly, just a little overview, how would one
 
**[00:42:01]** deploy these agents in Claude, so how, just like the horses, how does that work?
 
**[00:42:08]** Do I just tell the thing, yes, turn this skill into a managed
 
**[00:42:12]** The last time it was good, it's probably still the same today, but when I created my manage
 
**[00:42:19]** agents, you had in the, there's a cloud console, it's not the
 
**[00:42:24]** command line, but a website, where you can get API tokens, API access to the cloud
 
**[00:42:30]** and stuff like that, and there are also manage agents and you can piece together
 
**[00:42:36]** your manage agents through a Q&A game.

**[00:42:39]** Yes, you can say, what do I want? You can directly give it prompts for the skills or be guided through a question-answer mirror to this managed agent.

**[00:42:50]** And you can also upload results that you create in Cloud Code, in a sense, and say, here, do something with this, I've already made detailed thoughts about this, there’s something on the plate, I have, as I said, skills, I have no idea what.

**[00:43:03]** Then you run them there and also do something like cost control.

**[00:43:09]** It says okay, how often does the little creature do that, if it's actually running seven times in 20 and you didn't want that at all.

**[00:43:16]** And that works through this interface and as I said, you could upload and provide many things there and as far as I understand you can
 
**[00:43:25]** That is now also triggered from Cloud Code, directly triggered from the CLI.

**[00:43:30]** and that you somehow have to copy-paste into this web interface, and therefore it would be
 
**[00:43:38]** my initial assumption, maybe only a nice UI can be thought up,
 
**[00:43:44]** but if you wanted to use this today, I would almost bet that if you had an
 
**[00:43:50]** account, you could already use it today. Because I would say, you just need
 
**[00:43:57]** an API token, you need the accesses, you need, that’s all you need today,

**[00:44:01]** you can do the same thing with your Gmail. Only, it's not called Gmail, but

**[00:44:06]** Entwrappel. Yes, I believe that too. Well, I mean, to summarize a bit again,

**[00:44:11]** the vision behind it is to have a relatively easy-to-use

**[00:44:17]** platform like Notion, to perhaps make this AI era a bit simpler for

**[00:44:25]** individuals, for me. I believe that's actually their mission

**[00:44:31]** and I think they are succeeding. Sure, I said at the beginning, the CLI topic, there was

**[00:44:35]** I was still dependent on help, but basically, the

**[00:44:41]** path they are taking is, in my opinion, the important one, namely that basically

**[00:44:46]** everyone is enabled to build their own tool and that I no longer have to purchase or rent a

**[00:44:52]** big finished tool somewhere, but rather that

**[00:44:58]** I can piece it together step by step, I would say, with

**[00:45:02]** really simple means.

**[00:45:03]** It's really fun for someone like me, who isn't a real developer, because suddenly
 
**[00:45:08]** all these things work and you also can't forget the whole chain
 
**[00:45:13]** of requirement engineering and this and the specifications and whatever comes up
 
**[00:45:17]** all goes away when someone like me can just build it myself, much to the frustration at times of my
 
**[00:45:24]** people, who then somehow think that the weird old man is up to something again.

**[00:45:28]** made up.

**[00:45:29]** But I don't think it can be done any more efficiently than integrating all these things.

**[00:45:33]** And that's really, I have to say, that's really true.

**[00:45:36]** So I think I mentioned it last time as well, for me that's really

**[00:45:39]** a tool that captivates me just like Apple has continued to do with

**[00:45:44]** all its products. I’m curious to see if it remains that way.

**[00:45:47]** I'm curious how you will come out of your shell at the next WWDC now that you

**[00:45:54]** have this deal with Google regarding models, whether you will gain some momentum again

**[00:46:02]** and show a little something from this new world, because we both notice it now,

**[00:46:07]** whether we like the CLI or not? I started here by saying that in the past

**[00:46:13]** we were happy with beautiful user interfaces. Today, you voluntarily retreat into

**[00:46:19]** these command-number interfaces, so that people like you and me suddenly start coming up with ideas far removed from our

**[00:46:26]** professorship or far due to our age,

**[00:46:30]** because we simply, well, you can turn any idea into a skill, into a prototype, into

**[00:46:37]** something and talk about the results, instead of spending weeks trying to figure out

**[00:46:42]** whether the button is on the right or left, suddenly you have 20 versions in the room

**[00:46:46]** standing and can try them out and know much better, does this work, does it

**[00:46:51]** not that, what emotions do you have, no idea, what else, yes, I would like to

**[00:46:55]** not put a term into the world or use one that doesn’t come up in my daily

**[00:47:00]** work life, but still you notice that this, this playing,

**[00:47:06]** I also recently said, it’s like a text adventure. Back in the day, you played Ultimate

**[00:47:10]** Online or whatever, and you said open door, go through, watch out, zombie,

**[00:47:16]** kick it, run, yeah, grab the color bombs. So today, you actually write,

**[00:47:20]** I mean, that would be a really great function, let’s try it out and oh come on,

**[00:47:25]** I’ll press enter now and then go to bed and suddenly it’s three

**[00:47:28]** hours later and maybe you’ve achieved something but are still tired and have

**[00:47:34]** eye strain, she played the game of life with your professorship, also quite funny.

**[00:47:38]** Yes, AI as a text adventurer, my good friend David is a neurologist and needed a

**[00:47:45]** really secure billing and management tool for his new private practice,

**[00:47:52]** and he didn’t want to buy such an expensive tool and any 1000 certificates

**[00:47:57]** And then we said, well, okay, let’s build something with Markdown files as storage,

**[00:48:02]** a persistence layer, MacOS in X-Code, with cloud, of course, we talked about

**[00:48:08]** that before.

**[00:48:09]** I learned that from you with these Markdown files.

**[00:48:11]** You know, and then we built that in three hours, he has his own

**[00:48:15]** computer, he has no internet, no Wi-Fi, nothing, everything is down,

**[00:48:19]** old even, well, not entirely old, but sort of.

**[00:48:22]** And on it runs this software and I set it up for him, cloud

**[00:48:26]** this 20-euro version, whatever, and he’s doing exactly what you’re saying,

**[00:48:31]** namely at the end of the day he clicks three times again and then he’s back to three hours not

**[00:48:34]** slept, because he now has the doctor's letter in there and these X-rays and that

**[00:48:39]** automatic billing, and he just has to keep saying what he wants. And that is

**[00:48:43]** just somehow done. And then you have to know the infrastructure. And that is for

**[00:48:47]** non-developers always the biggest hurdle, the infrastructure. And if that is clarified,

**[00:48:51]** then it’s just amazing. And fundamentally, if we think about what we’ve

**[00:48:56]** talked about today, Notion and Ducktape and what word should I have put in my mouth.

**[00:49:02]** They started as, what, a notebook, note-taking option, note solution, and then somehow they got the hang

**[00:49:10]** of supporting databases and you name it, business processes

**[00:49:14]** and now suddenly, I mean suddenly, they are developing into something,

**[00:49:20]** this whole complexity of routine tasks, of maybe creative

**[00:49:28]** topics of whatever, is being taken away, because now you have sat down and done something with

**[00:49:34]** the CLI, you don’t have to have everyone do that.

**[00:49:37]** It’s enough if two or three people do it, who provide the workers, the agents

**[00:49:40]** and then suddenly everyone can work with this new possibility,

**[00:49:44]** never have to see anything of it, or maybe the job description changes at that point.

**[00:49:49]** Another topic. But a tool that you’ve had for years, which people are used to bringing

**[00:49:56]** updates again and again and then maybe something new, suddenly fundamentally changes

**[00:50:01]** the way you work with it. I don’t think two or three years ago you would have thought

**[00:50:04]** that Notion was capable of something like that. And I think that’s...

**[00:50:08]** Yes, really often. Yes. Sorry for interrupting. I interrupted you.

**[00:50:13]** But especially when I think about this fast-paced time you have, I mean, today

**[00:50:17]** something is cool and in three months the next one comes around the corner and how they

**[00:50:20]** challenges and how they pull each other through the ring with new features, possibilities,

**[00:50:26]** paradigms understood. I mean, today, yes, you said yourself, models are good and

**[00:50:31]** they are exchanged and the runtime they are in, the tap is, it is basically

**[00:50:36]** the new gold, yes, how it stores knowledge, how it imprints the model, how it takes the abstraction

**[00:50:42]** from you. And who knows what it will be in half a year, but I somehow

**[00:50:45]** feel Notion is a very quiet but a very modern companion of this change.

**[00:50:53]** So, do you remember what you wanted to say? Yes, I think the, the wiring is going to be,

**[00:51:01]** I wanted to say that, you didn't know what you were doing three years ago. I knew

**[00:51:03]** three years ago I wanted to have everything in one system. I have always wanted that

**[00:51:07]** in a way. And I would rather have an integrated system

**[00:51:11]** like Apple than a decentralized one, where every program has its justification and then

**[00:51:17]** the best tool for the job. I always found that personally and for my company stupid,

**[00:51:21]** because I wanted it to be integrated and I didn't know yet,

**[00:51:24]** that this would become so important one day. And today, it is indeed the case that because

**[00:51:27]** everything is really included, I have the best possible context and the thing always knows

**[00:51:31]** everything already. And I can do financial analysis, bookkeeping now always brings up the things

**[00:51:36]** because I don't feel like connecting it with Datif. That works too, but

**[00:51:41]** I haven't. And it just brings them up, then the agentless one looks at it,

**[00:51:46]** checks for any booking errors and so on. But I can also use all this information

**[00:51:50]** in another context. So the funny thing, and that's what I wanted to

**[00:51:54]** get at, was, I just wrote on LinkedIn that we accidentally invented a marketing operating system

**[00:52:00]** because we didn't have this great strategic plan. And then

**[00:52:04]** when AI is ready in 2026, we will have this great tool, rather it just happened that way.

**[00:52:09]** coincidentally turned out this way and now we have this and now we can really tell our

**[00:52:13]** customers, look, we have all of this in there, the strategy,

**[00:52:18]** the corporate design, the playbooks, all that stuff and of course we can pass on a part

**[00:52:23]** of this advantage to you. So we don’t have to keep all the AI advantage just for ourselves

**[00:52:29]** we’ll pass it on to you because we know that if you have the tools

**[00:52:33]** for the gold rush, you also sell quite well, it’s a pretty good business model,

**[00:52:37]** you don’t always have to mine yourself. And that’s what people want now. And that can

**[00:52:40]** all be done with one platform. I can invite the iZone Ocean. And I already have

**[00:52:44]** the first pilot customers doing this. And they can then use AI without having to

**[00:52:49]** deal with it themselves. Simply as a service from us. We don’t just

**[00:52:53]** do, you know, we don’t just do all the things we talked about.

**[00:52:57]** have, but for the customer it is completely, they don't have to do anything. Just like a

**[00:53:02]** CMS used to be, they can just sit down, write a ticket and then something happens.

**[00:53:06]** And either that's done by an agent or a person or both, and that is really quite

**[00:53:10]** impressive.

**[00:53:11]** And that has nothing to do with the fact that we have a certain degree of kinship.

**[00:53:15]** But I have also, and I won't name names, had dealings with various other companies

**[00:53:21]** like that.

**[00:53:22]** Also, I say, well, what does it mean to deal with, right?

**[00:53:24]** So external companies that offer their services to us, and when you look at that,

**[00:53:30]** you deal with KÖI. And how they are changing, I mean, I didn't learn this

**[00:53:35]** overnight either, but also how they are changing, and you certainly are too

**[00:53:40]** you have to carry your packages, but because this is in Notion,

**[00:53:47]** the manufacturer Notion offers you a solution that doesn't just give it to you,

**[00:53:54]** but makes it easier for you to reuse the knowledge. It is already there,

**[00:54:00]** to access, to ask the agent to extract things, to ask the agent,

**[00:54:05]** to do things without you having to manage PowerPoint for Bird Axel, different directory structures,

**[00:54:11]** countless, I don't know, whatever, yes, file formats, Axels that crash out of the manuals

**[00:54:17]** and work with macros and preferably also with color coding to highlight the uniqueness of numbers,

**[00:54:23]** what might all be possible, but what I want to point out, the basis, the

**[00:54:27]** foundation, the groundwork is already there and Notion is also evolving in that direction,

**[00:54:34]** they are integrating it, we talked earlier about the type of data processing and there are

**[00:54:40]** enough companies that may have a great consulting offer and smart people,

**[00:54:44]** they all have, yes, I mean, we are all those who think working with smart

**[00:54:48]** people everywhere, I would sign that, but they may have due to

**[00:54:52]** the tools they have used. It used to be Lotus Notes. Now it’s mostly

**[00:54:57]** a lot of Microsoft stuff. Even if it’s Apple stuff, well, you know,

**[00:55:01]** but I don't know. Yes, but with Notion, I think you have a good foundation, at least

**[00:55:06]** also in this changing time with N8n and Make and then came Codex and Cloud and Crock

**[00:55:14]** and I don't know what. Yes, it provides a base on which you can build to offer

**[00:55:20]** more value to customers, employees. And I actually think that’s really cool. Hats off,

**[00:55:27]** yes, it's really a great thing. And that also keeps me in a positive mood. In this respect, I think,

**[00:55:35]** okay, they have Markdown at their core. They have AI integration at their core. They have this openness now

**[00:55:41]** with the worker and so on to the outside, that even if in three months or in two years or in a

**[00:55:48]** yes, a cool new trend comes along, they have the opportunity because of the

**[00:55:52]** good data storage and the openness to at least go along, if not even to hold your ground.

**[00:55:58]** And I actually think that's getting overlooked a lot, because most people hear, oh,

**[00:56:02]** Entropica has shipped another update. Yes, oh, they want adult chat and

**[00:56:08]** no idea what it was, it’s all just, bleh. So, and Google, ah, now they’ve, now Google

**[00:56:12]** has crushed everyone again and no idea what it was,

**[00:56:15]** Coop-pilot was never good, it’s more like cold, parentheses steroids.

**[00:56:19]** You never hear anything from Notion.

**[00:56:21]** But if you engage with Notion, it’s awesome.

**[00:56:25]** Yes, it always was like that.

**[00:56:27]** When Apple reached a point where they were already good but nobody knew them,

**[00:56:32]** because all the things were set in motion.

**[00:56:36]** I believe that this comes at a decent pace, because it is already a large pace.

**[00:56:41]** They are now a thousand people, that’s not much,

**[00:56:43]** But for them, of course, it’s an insane growth; they somehow came from, no

**[00:56:48]** idea, from 300 or so and 1,000 sounds ridiculously small for what they achieve in

**[00:56:53]** output.

**[00:56:54]** But they are one of those new companies that don’t need that much headcount to

**[00:56:58]** create this output.

**[00:56:59]** And if you watch all those videos on how they work with their own tool

**[00:57:03]** and of course they have 1,000 agents running there and doing everything with it

**[00:57:07]** and every Slack channel has an agent from Notion that first answers it already

**[00:57:12]** and listens a bit, and if someone wants to know, I’ve also built 2 or 3 now,

**[00:57:16]** then he says for new people, for example, yes, answering questions in Notion in Slack based on

**[00:57:23]** the context in Notion. Well, what I wanted to mention briefly is that you can really say,

**[00:57:28]** and I find that to be the big task now, especially when you have it in Notion,

**[00:57:33]** you can as an employee relatively cleanly and in small steps enter this AI world,

**[00:57:41]** because then you somehow do a prompt and then that's what we call

**[00:57:46]** now a skill and then you can just say add somewhere and then you provide the skill name,

**[00:57:50]** then something happens and suddenly, you need a completely new interface,

**[00:57:54]** some new system, you have to copy-paste into a chatbot or or or, it's just there

**[00:57:59]** in the dose you want and it just becomes increasingly visible to you that

**[00:58:04]** our project is precisely to bring all the people on board. I don’t want to come to the end

**[00:58:11]** without saying one more sentence about that. Because we also repeat this regularly in the podcast,

**[00:58:16]** the technology is there. Just because technology is developing quickly doesn’t mean that

**[00:58:21]** the technology as we have it today or as it was three months ago is bad.

**[00:58:25]** It can do a lot of things and it doesn’t fail because the technology was bad or has been bad

**[00:58:30]** for some time, but rather that you also have to take people on the journey,

**[00:58:34]** because the majority still hasn’t heard anything about AI, except maybe in the news. Those,

**[00:58:39]** who have heard something about AI, may have partially used it

**[00:58:43]** or think they have, but essentially they’ve never used it more

**[00:58:47]** like Google.

**[00:58:48]** After some input, an answer came, thanks, goodbye.

**[00:58:50]** And very few pay for it, even fewer interact with skills and stuff or get lost

**[00:58:55]** on the CLI and then use, I’d say, AI in its pure form and from that

**[00:59:00]** side, it's about how to take people along without overwhelming them on the one hand.

**[00:59:06]** Because too full windows, too many buttons, typical IT stuff, you have to click there, why do you click

**[00:59:13]** here?

**[00:59:14]** No, you do that and then please go into the submenu and then enter that, now

**[00:59:16]** just go ahead.

**[00:59:17]** Yes, so it’s like this, everyone in their Jaguar might be a little impatient with people

**[00:59:24]** from someone else’s Jaguar, that’s the point of explaining.

**[00:59:27]** And from that perspective, what you said is of course also a point,

**[00:59:31]** if you are used to working with scores, which surely for the person who

**[00:59:35]** is switching from Nauschen-Kentenumstieg, you can introduce it homeopathically. And that’s surely not to be underestimated

**[00:59:46]** and also shows, if that perhaps was never the point of why one dealt with Nauschen

**[00:59:50]** that it wasn’t so stupid after all that you use it. Switching is,

**[00:59:56]** when you are on something different, is quite hard. You have to get people on board,

**[01:00:00]** you have to pull in your data. So the bigger you are and the more people you have,

**[01:00:04]** I believe, the harder it is to handle such a different user paradigm.

**[01:00:15]** But I found it great again that we talked about Notion. It will surely

**[01:00:24]** happen again. I have this very strange feeling that Notion will eventually have an update

**[01:00:28]** soon. At the latest then I would allow myself to invite you back. Maybe

**[01:00:32]** I’d like Jens to be there too, it’s probably a full excuse that he’s crashing.

**[01:00:36]** Yes, maybe it’s just an excuse, but I would also like to meet him.

**[01:00:41]** So, greetings to you, as you say so beautifully.

**[01:00:43]** And it was very nice to be at your place again.

**[01:00:45]** We are at one hour and two minutes.

**[01:00:47]** I think this is the target time.

**[01:00:48]** Yes, something like that.

**[01:00:50]** That works plus minus.

**[01:00:52]** That fits very nicely.

**[01:00:53]** Yes, thank you very much for the invitation.

**[01:00:55]** And for the explanation in advance.

**[01:00:57]** So I am now a proud owner of already two Workers.

**[01:01:00]** The absolute hammer.

**[01:01:02]** If you liked it, Schinte, leave a like, a comment, tell your friends,

**[01:01:05]** no matter if they work with or without grades, that you give our podcast a go and stay tuned,

**[01:01:10]** to see who our guest is next time.

**[01:01:11]** Until then.

**[01:01:12]** Ciao.

**[01:01:13]** Bye.

**[01:01:14]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[01:01:21]** Two technology-loving minds who not only talk about artificial intelligence,

**[01:01:26]** but live it.

**[01:01:27]** Here you will find clear classifications, real practical insights, and a fresh look at what is possible.

**[01:01:34]** Understandable, critical, and always with a wink.

**[01:01:38]** AI to ponder, to smile, and above all to discuss.
