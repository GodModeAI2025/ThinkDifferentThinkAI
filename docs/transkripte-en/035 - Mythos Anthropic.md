---
title: "Mythos Anthropic"
episode_index: 35
published: "Sun, 12 Apr 2026 23:59:00 +0000"
duration: "3357"
audio_url: "https://audio.podigee-cdn.net/2442712-m-82fe18ce5b8f2e0c9d331fc080e5d909.mp3?source=feed"
guid: "0c690ba4687a68050e9fa07bc5eb138c"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T21:07:54+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/035 - Mythos Anthropic.md"
translated_at: "2026-04-29T14:23:43+00:00"
---

# Mythos Anthropic

**Published:** Sun, 12 Apr 2026 23:59:00 +0000
**Duration:** 3357
**Audio:** https://audio.podigee-cdn.net/2442712-m-82fe18ce5b8f2e0c9d331fc080e5d909.mp3?source=feed

## Description

Managed Agents, Mythos and more
In this episode, we take you into the exciting world around Anthropic, Claude, and the spectacular cloud code leak. We talk openly about how token costs and system prompts push us to our limits, what's behind the Mythos model, and why managed agents are suddenly the next big thing. You'll learn how an accidental code release jolted the developer community and what opportunities – but also risks – AI systems present for security and automation. We discuss the rapid development towards AGI, share personal anecdotes, and ask ourselves: Who else is in this race?

Whether it's skills, sandbox breakouts, or the next big breakthrough – we show why it's worth staying at the pulse of AI time. Tune in if you want to know how to not get left behind in the AI jungle and why the future might come faster than we think.

Anthropic
https://www.anthropic.com/

Claude
https://www.anthropic.com/claude

OpenAI
https://openai.com/

OpenClaw
https://github.com/openclaw-ai/openclaw

Managed Agents (Anthropic)
https://docs.anthropic.com/claude/docs/managed-agents

Mytho (Anthropic AI Model)
https://www.anthropic.com/news/introducing-glasswing

Project Glasswing
https://www.anthropic.com/news/introducing-glasswing

Notion
https://www.notion.so/

Asana
https://asana.com/de

Slack
https://slack.com/intl/de-de/

GitHub
https://github.com/

Nvidia
https://www.nvidia.com/de-de/

Amazon
https://www.amazon.de/

Apple
https://www.apple.com/de/

Broadcom
https://www.broadcom.com/

Cisco
https://www.cisco.com/c/de_de/index.html

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here you'll find clear classifications, real practical insights, and a fresh perspective on what's possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Food for thought, for a chuckle, and especially for joining the conversation.

**[00:00:29]** Welcome to Singt different, Singt AI. Today for a very special episode.

**[00:00:39]** With me again is Jens, hello Jens.

**[00:00:42]** Hello Mark.

**[00:00:43]** And the topic of the episode, yes. Aside from the fact that Mark already had a slight speech impediment.

**[00:00:50]** It’s starting off really well. We’ll keep that in, no worries.

**[00:00:52]** Is our life with Orthropic.

**[00:00:56]** Don’t worry, we haven’t cheated, but we want to focus a bit today on what is happening with and around us and with

**[00:01:06]** Orthropic as a company, what’s essentially going on. 

**[00:01:10]** And before I let Jens speak, as is proper, I just want to start by saying that I was quite annoyed by Ausropic.

**[00:01:19]** The last few days, because something happened that should have been understandable to me, but it wasn't at all

**[00:01:25]** understandable to me at that moment. And I actually work quite a bit

**[00:01:31]** with Ausropic and have been using Claude Co a lot. That's the

**[00:01:35]** command-number interface of Ausropic, used to interact with the models.

**[00:01:40]** Command-number interface, a CLI, to just go over some terms again.

**[00:01:45]** thrown into the room. And when I use this CLI to ask the model

**[00:01:49]** questions and get answers, it consumes less

**[00:01:54]** to show up than if I call the API, that is, the programming interface, and send

**[00:02:01]** a string and say, do something. So for example, if I tell the model

**[00:02:04]** to tell me what the weather is like in Karlsruhe, always regardless of that he then

**[00:02:07]** If I have to do web research and stuff, the token consumption in Clot-Code, in

**[00:02:12]** the terminal interface, is much lower than if I go through the API. The

**[00:02:20]** reason I can also explain, that’s a bit of a cliffhanger, like in the

**[00:02:23]** good TV episode and now for the commercial. Advertising, what do you think, Jens? What comes to mind about life

**[00:02:28]** with Othropic? I keep wondering, is it Othropic or is it Anthropic? Whoever

**[00:02:36]** pays gets to say how it’s pronounced. That’s my rule too, when I buy some

**[00:02:41]** strange product and everyone tells me I’m pronouncing it wrong and I then say,

**[00:02:46]** did you buy it? Did you subscribe? No, then I can also say how I personally

**[00:02:51]** call it. But feel free to send messages, it also boosts the ranking everywhere when people leave

**[00:02:55]** comments. Just go ahead and say, Claude, from now on.

**[00:02:59]** That makes it much easier. Claude. Yes, okay. So my life with

**[00:03:05]** And Perfect Claude. That’s, well, it’s already started for a while.

**[00:03:12]** I actually used the chatbot relatively early on. Then I

**[00:03:15]** stayed loyal to Open AI for a long, long time and only switched a few

**[00:03:20]** months ago, just before the topic with Open Clore started

**[00:03:25]** gaining traction, which was strongly associated with Phobics Cloud. That’s when

**[00:03:31]** I switched. I then initially used the chat tool normally, I imported

**[00:03:37]** I did that, I saw what basically OpenAI has saved of me

**[00:03:44]** There was something quite interesting in there, when you look at this export

**[00:03:47]** it gives me all the information you have about me, so that I can import it into the cloud

**[00:03:51]** I could.

**[00:03:52]** I then saw what is actually stored in this context of AI about you,

**[00:04:00]** so that it can provide better answers without errors.

**[00:04:03]** You should never forget that.

**[00:04:05]** The bots you talk to are not comparable to the bots that communicate with others

**[00:04:12]** because they always react a bit differently.

**[00:04:14]** Natural weights. They have their models in the background, which are very similar. They are

**[00:04:19]** also very similar across the models because the training data around the world is also very similar

**[00:04:23]** too. Many of these models also have very similar responses, that has been

**[00:04:27]** addressed before. But in the individual response, when I provide this model context

**[00:04:32]** and I can deliver the context through my prompting, I can also deliver it through additional skills

**[00:04:37]** or it can also be done through memory, if I have that activated,

**[00:04:41]** so that these bots can remember you. And that was the first

**[00:04:44]** moment when I consciously put it into the cloud and

**[00:04:47]** where I was thinking a bit about whether to continue working with this chat interface

**[00:04:51]** together or if I should try out other functionalities, like the cloud desktop or

**[00:04:57]** cloud code, as it's called, which you can also install either as an application

**[00:05:04]** or, as the market just described, or like a terminal, you can also download it

**[00:05:08]** and then work with this code agent in the terminal, which can actually write code directly

**[00:05:14]** on your machine. And that's what I'm doing right now. So I'm

**[00:05:17]** just a little bit, I have already told you about that, still in a very

**[00:05:21]** slow Orchoclaw installation, because I am doing it very, very carefully and I want to be very, very clear

**[00:05:25]** about what is actually happening in the background and also trying out a few things myself,

**[00:05:29]** how a memory can be built up, how a Second Brain, like Kapafi,

**[00:05:34]** that has been mentioned this week, can be set up in a wiki-style with MD files. But

**[00:05:38]** but I'm working extremely closely with Pfaffig, because I'm kind of looking,

**[00:05:42]** Pfaffig gives me the guidance, explains to me what I should type into the terminal,

**[00:05:47]** how that works, and then on the other side is the OpenClaw, which is also connected

**[00:05:51]** with an API, with like, like, like, like, like, like, net, net, 4, 6 versions,

**[00:05:57]** let's correct that.

**[00:05:58]** Best user can name it.

**[00:05:59]** Okay.

**[00:06:00]** So also a model, the current model, so to speak, that can be used there, that

**[00:06:05]** I have virtually connected with Open Cloud via API.

**[00:06:09]** And, Mark, sorry, I need to quickly mention this.

**[00:06:12]** And last week I paid a lot of money.

**[00:06:14]** I somehow burned way too many tokens on two parts.

**[00:06:19]** What's good on one side is that you get to see it yourself,
 
**[00:06:22]** when you don't think about it, you know, when the
 
**[00:06:24]** whole time it's just chat with the chatbots,
 
**[00:06:26]** and that essentially disappears into this normal subscription fee
 
**[00:06:28]** that you're paying, then you don't really see
 
**[00:06:30]** what you're burning daily in that moment.
 
**[00:06:32]** And how important it is to really consider,
 
**[00:06:35]** what data is actually being exchanged. That's something we have somewhat forgotten.
 
**[00:06:40]** And when you suddenly have to pay API costs and then the bot,
 
**[00:06:45]** the cloud bot, which you painstakingly built, suddenly can't respond via Telegram,
 
**[00:06:51]** because unfortunately it has reached the limit of the API, then you become aware of everything that is involved.

**[00:06:55]** in principle, it operates behind the technology and then you start again,
 
**[00:06:58]** to think differently about how I can optimize this, how I can optimize my context length,
 
**[00:07:02]** optimize, similar to many gears again, but now of course the joyful word combiner is back.
 
**[00:07:09]** I have also heard at some point that one large prompt is more efficient than many small ones, because
 
**[00:07:15]** the whole conversations are constantly at

**[00:07:17]** further layers of new prompts also erode tokens. But I mentioned earlier, just a little cliffhanger.

**[00:07:24]** Yes, I'm doing a little teaser and then I'll resolve the cliffhanger, because you said you're doing it especially slowly

**[00:07:30]** slowly and especially safely. We also have something later from the house of

**[00:07:35]** Schropwick, where they do it a bit slower to make it safer, but not for

**[00:07:40]** themselves, but for others. But we'll get to that shortly. I would like to resolve,

**[00:07:45]** what was the case for me. The topic is hearing, why is the token consumption actually so

**[00:07:48]** much higher when I talk about Klot outside of the Klot applications. It is fundamentally

**[00:07:55]** because I forgot again that just because I write a text in a core position

**[00:08:01]** saying, hello world, how's the weather, or something else, a lot of expression

**[00:08:05]** is still happening. And the software that Orthropic provides us, the Mach-Caching, the Mach-System-Proms,

**[00:08:13]** still packs a whole sack of information that was of course completely unoptimized

**[00:08:18]** for me. And if you want to imagine that, the question I

**[00:08:22]** The spot costs 50 tokens if I do it with the system and 5,000 tokens if I don't do it with the

**[00:08:29]** system. Now you might say, who cares, but when you think about how many

**[00:08:33]** tokens I have, if the requests get more complicated than weather, maybe I have no idea, here and

**[00:08:38]** there, in pineapple, whatever, then you will notice that you can quickly end up, like for

**[00:08:43]** example with an Open-Claw installation, in larger territories, because I mean,

**[00:08:47]** I myself am the personal owner of the Claude Max 20x plan. That's the largest,

**[00:08:54]** subscription you can buy. After that, you have to throw in tokens in the form of credit card approvals.

**[00:09:00]** And I was very happy because I nearly exceed that limit almost daily. And when

**[00:09:06]** he then says, no problem, you can also make Pay Per Use from now on, it's so much

**[00:09:11]** from, just give me your credit card, I did that once, but I didn't say

**[00:09:16]** AutoCharge, instead I said, here's 40 euros, have fun. And it felt a bit like

**[00:09:22]** today driving a burner. You filled up with 40 euros and you're not going far.

**[00:09:27]** Yeah, you practically, you already have an empty

**[00:09:32]** fuel gauge as you leave the gas station because it's consumed those 40 euros so quickly, the token usage,

**[00:09:37]** Somehow you also feel like they want to charge extra, the assumption is personal

**[00:09:42]** that feeling.

**[00:09:43]** And what also happened with Ostropic is that they did something for Open Claw or

**[00:09:49]** generally see their subscription keys misused, yes, now either
 
**[00:09:56]** announced or implemented, so that it can no longer be used for Open Claw
 
**[00:10:01]** because I can imagine if you have such a system that says
 
**[00:10:06]** Here is a CPU and here is energy. It behaves now like coal and stove. I pour
 
**[00:10:12]** in, so it stays nice and warm or nice things are calculated, that this is not really
 
**[00:10:17]** the business model of Astropic, that every user, no matter what plan they choose,
 
**[00:10:22]** utilizes this to the maximum. Yes, where you just have 5000 tokens, I can repeat that
 
**[00:10:28]** actually last week I somehow sent 190,000 to 210,000
 
**[00:10:33]** tokens per message and that naturally also led to
 
**[00:10:37]** my hard-earned euros being quickly burned up, so what you just
 
**[00:10:43]** had to sustain. That was then relatively quickly gone. But there is also another point,

**[00:10:48]** when you always talk a lot about how AI is making everything easier now and stuff,
 
**[00:10:53]** a bit of active understanding really helps, to be honest. So when I noticed that,
 
**[00:10:58]** I went to management, because I don't know,
 
**[00:11:02]** But I knew what it was about, we went into discussions with the Kais and then it turned out,
 
**[00:11:06]** it became clear relatively quickly that a Kesh was not even allowed. So I

**[00:11:10]** I always happily sent all the information with every message again

**[00:11:13]** it was kind of something, I know exactly where it was now, not quite right

**[00:11:17]** configured or allowed to be configured at that moment. Now I know what a Kesh is.

**[00:11:21]** Therefore, I then said, okay, that can already help. We have essentially already

**[00:11:24]** solved individual size problems. This way, you immediately have essentially a large part

**[00:11:28]** could lower it again because I no longer automatically forwarded all my information with every message.

**[00:11:34]** So that also means, yes, it has become much easier to do things through AI.

**[00:11:41]** When you venture into the realm of installing agents on the computer,

**[00:11:46]** actually moving towards producing something, you still have to have at least

**[00:11:51]** some basic knowledge today, so you don't end up on the completely wrong track,

**[00:11:56]** sometimes and then wonder about it later. I believe it still goes well. I

**[00:12:00]** don't want to say it doesn't. You can also build apps today without having to

**[00:12:05]** one used to do with IT. You can build wonderful campaigns, create content

**[00:12:10]** for your shop that you somehow have, place ads, everything with flair, being creative

**[00:12:14]** in generating it. Of course, all of that is possible, and also writing software. But it is

**[00:12:19]** actually, I believe, easier if you have a bit of an IT background because

**[00:12:24]** the terms are similar. So the machines also use the similarities. The architecture in the background is still the same.

**[00:12:30]** There are still E-Brow servers, there are still things like ports that are either open or closed.

**[00:12:35]** Or if you are dealing with having a local installation, it also basically comes down to permissions behavior.

**[00:12:41]** Who is actually allowed to write to which folder? What read and write permissions does such a folder have on a computer?

**[00:12:47]** And they need to be rewritten. And you have to understand that first.

**[00:12:50]** So, not everyone is aware that such things simply exist. And I believe that

**[00:12:54]** it is important to know that. You can get good help from, for example, from Entvofic.

**[00:12:58]** In principle. So I do many of these things that I'm currently doing. I also let myself be

**[00:13:02]** reassured, give me the programming command or the command in principle to make a folder writable

**[00:13:07]** via the terminal. I don't know the recommendation anymore. But I let them explain it to me.

**[00:13:10]** So, I always say again, that's cute, I have to repeat it again and again,

**[00:13:14]** because the machine thinks every time, now it probably got it.

**[00:13:17]** I always say, no, I'm still dumb. I’ve already

**[00:13:21]** again forgotten what this command has and that computer artificial intelligence
 
**[00:13:25]** is, is no intelligence in front of the computer. Yes, with a fan it is AI. Sorry,
 
**[00:13:30]** I couldn’t leave that lying in the street. It demanded to be addressed. I forgive
 
**[00:13:35]** here. Thank you. You just mentioned about what terms one
 
**[00:13:41]** stumbles over and the topic of Agent Carnes is also something that I would say just now with out tropic the last
 
**[00:13:49]** days before we recorded or weeks circulated again because March 31st
 
**[00:13:57]** 2026
 
**[00:13:58]** made out tropic a mistake, namely there was a, I’ll say human error we could perhaps talk about that in more detail later
 
**[00:14:06]** because accidentally
 
**[00:14:09]** a
 
**[00:14:10]** file was published, which is normally needed to debug source code.
 
**[00:14:15]** It was published, let’s say it was accidentally made freely available and
 
**[00:14:22]** an intern from, oh God, I must have forgotten the company in all the excitement,
 
**[00:14:28]** found it and immediately posted it on X and what was the consequence?
 
**[00:14:32]** That 512,000 lines.
 
**[00:14:35]** Claude Kot a TypeScript written code base
 
**[00:14:41]** was published. So not the AI model, so not Opus Umwissals is called,
 
**[00:14:47]** but the software with which you address these models.
 
**[00:14:52]** And that really made waves. So out robics apparently tried it with legal assistance.
 
**[00:14:59]** There are some things that ensure that copyright-infringing material gets deleted from the net.
 
**[00:15:05]** But there were thousands of repros that then tried to clone it for themselves.
 
**[00:15:11]** There are some developers who then also had it translated into other programming languages.

**[00:15:16]** Probably also from Claude. That's really not hard, right?

**[00:15:18]** Turn the construction around, do this part.

**[00:15:20]** There are attack attempts, yes. There are bad guys and there are bad girls,

**[00:15:25]** but I would say the bad guys went ahead and,

**[00:15:29]** in effect, here you find Claude code and infected it with Melvair and offered a download.

**[00:15:35]** And what’s really striking is, regardless of the fact that it was a mistake that existed only for a very, very short time, the whole problem was relatively quickly fixed, so the public availability, people still studied it, there are articles about it that describe how it developed, from Thropic and that they also only boil with water, but partly already have coal inputs, the prompts they use against the machines have been published, how they work with tools,

**[00:16:04]** like MCP and how all the other stuff has been published, how they handle memory management, how they do multi-agent control, that one agent processes a skill and then spawns several agents, that there is a Kairos model, an automated daemon, not a daemon in the sense of Lucifer, but a daemon in the form of a service that runs automatically in the background, tidying up and preparing things, and so on.

**[00:16:34]** So many exciting things and I must admit, yes I looked at the code and I actually learned something.

**[00:16:43]** If you're interested, I would actually say yes, take a look.

**[00:16:47]** Take a look, if you had said no, it would be like many people in front of the camera or the microphone.

**[00:16:53]** And by the way, you know that I love skills and we will soon have a special skill episode again with a guest, but we want to dive in too deep.

**[00:17:02]** And I didn’t look at all this stuff because I want to build the next runtime for agents, but because I wanted to see how Claude actually works with skills.

**[00:17:12]** So what is important to him? What is important to him that the order of the skill is really considered?

**[00:17:18]** considered. What is important to him so that he knows that a skill

**[00:17:22]** opens and that the sub-skills run in parallel and that you

**[00:17:25]** can maybe also give other models to skills and say, this

**[00:17:28]** runs here with model A, this runs with model B and all that stuff and

**[00:17:34]** then he kind of laid a little bit of my own best practice aside

**[00:17:37]** for me. What should I pay attention to when I build skills and now you can say,

**[00:17:42]** old white man, the self-fulfilling prophecy, I have

**[00:17:45]** the feeling the skills run better. Period. But only looked inside, didn’t copy,

**[00:17:52]** nothing published, many greetings go out. Yes, it’s also funny how the web reacts

**[00:17:58]** goes. I think we tried to contact 8000 Github repositories where basically the

**[00:18:04]** code was, and getting them taken down, which didn’t work, then it was said again

**[00:18:07]** no, they weren't even it. But I understand that too, look. Your

**[00:18:12]** crown will be offered there basically due to an error, not for purchase, but for

**[00:18:17]** checking out. But you can’t get to it anymore. Yes, that’s the

**[00:18:25]** answer. So let’s say, how many years has the web been around and how many

**[00:18:30]** years were there already back then, like how early was there already things like Napster and

**[00:18:33]** other things that showed how massively data was never heard of, I didn't hear

**[00:18:38]** either, but the music data at that time was being totally divided and other things.

**[00:18:42]** Yes, that was probably after earlier times.

**[00:18:44]** Well, I only know vinyl records.

**[00:18:46]** I believe, for example, one variant of the

**[00:18:48]** disk copying code that I heard about is that someone made a

**[00:18:53]** screenshot of the whole code.

**[00:18:55]** That means he must have used some screenshot tool.

**[00:18:57]** There are indeed screenshot tools that can scroll.

**[00:18:59]** That means he must have briefly looked at everything in the browser

**[00:19:03]** those 500,000 lines or however many there were and captured it completely.

**[00:19:06]** That means there is also a picture that can of course be easily read by another AI

**[00:19:13]** and the text can be extracted.

**[00:19:16]** Any Google phone can do that, any Google app, basically, that has the capability to

**[00:19:20]** extract text.

**[00:19:21]** Even the Google phone can do that.

**[00:19:22]** This comment, please directed to Jens, yes, this time it wasn't me who made this little picture.

**[00:19:27]** It was me.

**[00:19:28]** Even the Google phone can do that.

**[00:19:29]** And Google apps can do that.

**[00:19:30]** I'm a big Google fan.

**[00:19:31]** Yes, especially Google, no side note, Google has also released some nice new models

**[00:19:34]** that run beautifully, where you can also start your AI studio as an app

**[00:19:39]** on the iPhone, for example, and here translations and image descriptions

**[00:19:45]** and so on.

**[00:19:46]** That's quite amusing as well.

**[00:19:47]** He also tried it with skills, but then unfortunately backed out, because he felt

**[00:19:50]** my skills were too extensive, but that was understandable in a way.

**[00:19:53]** I wouldn't have expected it to hold up like that either.

**[00:19:56]** But I still think, even here I notice again, you perceive that something is happening

**[00:20:02]** in the world.

**[00:20:03]** Code is being laid, it flows through your timeline as well, you don't have to do anything stupid, you just open your computer, you're on social media, you have an i-bubble and then you have like 78 posts showing some get tree post, some knowledge documents, some articles, some Reddit posts, I don't know what.

**[00:20:23]** You can't escape it all, but still in the first hours,

**[00:20:29]** I wasn't really aware of what a learning experience there is for people,

**[00:20:34]** to deal better with the system of Autophobics, and I actually wondered,

**[00:20:40]** why on earth are the guys and gals over there not publishing, I don't know,

**[00:20:45]** 30 pages on how to write a plug-in? And 20 pages on how to write a skill?

**[00:20:50]** But what really brings out the last 10% from the conglomerate, making it more stable

**[00:21:00]** and stuff like that, somehow not.

**[00:21:02]** Yes, but it wins, so that's difficult.

**[00:21:05]** So, two sides, as I said, the one thing I wanted to bring up, so I
 
**[00:21:10]** think it's difficult to get published material off the internet again,
 
**[00:21:13]** that's not going to work, honestly, you might as well be a mug,
 
**[00:21:15]** however you want.

**[00:21:16]** Looking at societal development, regarding what you're describing, it is actually
 
**[00:21:21]** such that you have to say, they're also now, well if everything is happening so much faster
 
**[00:21:27]** through AI and everything is so much more reproducible, and even Kepefi has now also talked about
 
**[00:21:32]** that he doesn't actually share content anymore, but maybe
 
**[00:21:36]** rather says he shares his skills or shares ideas, because your LMM can
 
**[00:21:42]** then essentially also reprogram that in case of emergency in its own way and specifically

**[00:21:47]** specialized on your environment and your requirements. The actual code is really not that important anymore.

**[00:21:52]** I believe we are moving into a world where, on one hand,

**[00:21:56]** we have to say, yes, everything is actually going Open Source, which makes sense because then we can

**[00:21:59]** learn from it much faster and adapt it to our circumstances,

**[00:22:03]** that could be more efficient. On the other hand, I also understand a multi-billion dollar,

**[00:22:08]** there, four times, perhaps also has things developed that are still a bit

**[00:22:14]** kept in a quiet little room, because of course they might like to use some marketing moment

**[00:22:19]** to then drive up their stock price or prepare for the IPO

**[00:22:24]** or something else to possibly recoup the money they spend there as well,

**[00:22:28]** somehow to bring it back in through the side.

**[00:22:30]** I think those are the kinds of things that happen, which is why they probably,

**[00:22:33]** they mentioned these 10 percent from Logare, maybe at the beginning

**[00:22:37]** not yet.

**[00:22:38]** almost 100 percent given, that's also okay. We will have learned from it.

**[00:22:42]** Including a little Tamagotchi that you can activate in the terminal,

**[00:22:46]** we will have learned from it, but I also find it in, let's say

**[00:22:49]** my quotation marks doubly funny. We might touch upon

**[00:22:53]** the topic later, maybe at least from the series, myths and tales, how that

**[00:22:57]** could have possibly happened. But first I want to share

**[00:23:00]** is, as I said, felt like their crown jewel. Okay, they didn't release their

**[00:23:05]** model, as I said, it didn’t slip out of their hands, fair point, but

**[00:23:09]** still Claude Coach, that's something that at least every software developer, I would claim,

**[00:23:14]** or a majority of software developers, would like to take a look at or is looking into.

**[00:23:18]** And now we're talking about it being made public and that one could

**[00:23:24]** take a look at it and the topic of security is now, how do you say it, addressed thoroughly

**[00:23:28]** that this secret from Ostropic was published, not customer data

**[00:23:33]** and such, but the secret of Ostropic.

**[00:23:35]** What just reached me in the news feed very fresh is the announcement that Ostropic Managed

**[00:23:42]** offers agents.

**[00:23:43]** So a suite of APIs, allowing developers to create hosted careers.

**[00:23:53]** This means, Ostropic provides you with a sandbox, so the thing doesn’t break out and

**[00:23:59]** runs in a secure environment where no one can look in, with state management, so that

**[00:24:03]** the thing always knows in what state it is, with authentication, so

**[00:24:07]** what it’s allowed to do and as what it acts, with error handling to operate this whole thing at a price,

**[00:24:15]** which corresponds to the previous token price, just somehow 0.08 US dollars, what are
 
**[00:24:21]** those?
 
**[00:24:22]** US cents?
 
**[00:24:23]** Yeah, no idea.
 
**[00:24:24]** Greetings to the more internationally-minded people,
 
**[00:24:27]** billing process hours and that, which some would already use, yes, like Notion,
 
**[00:24:33]** we also had Notion, greetings to Dirk, here in the show, who use that, or Asana.
 
**[00:24:39]** Yes, yes, where that still is, I mean, I'm just on it, you know, I'm looking at it right now in the
 
**[00:24:45]** cloud growth solo, there is also actually the manage-aid and it has already been announced,
 
**[00:24:49]** I already have the functionality, I've just put it aside, but I see for example in the quick starts,
 
**[00:24:53]** there are a few where you can build a sports agent. Feedback from my end.

**[00:24:57]** And those are not exactly the companies you just mentioned.

**[00:25:00]** There is a Notion already pre-installed as an example.

**[00:25:03]** Asana is included, Slack is there, if I recognize my own correctly.

**[00:25:06]** GitHub is of course included, so I can analyze GitHub items.

**[00:25:09]** So there are already connectors included, probably also from these companies they are now using.

**[00:25:13]** This is of course how the balls play out over time.

**[00:25:17]** I don't think that's bad, because it's a good solution to simply say,

**[00:25:20]** You don't have to make it so complicated. You may not be in some kind of agent world,

**[00:25:25]** how I'm trying this right now on such a local installation or you're not in one, like you

**[00:25:29]** you can't influence at all, but here you apparently have very, very structured

**[00:25:34]** built with Extra Credential Vault, where you can also manage the API keys and such

**[00:25:40]** you can save it, because as I said, when you do such an Open Cloud installation, then

**[00:25:43]** it can easily happen that it is somewhere in plaintext and anyone can read it,

**[00:25:47]** if they want to, or if they want to make it freely available or something like that.

**[00:25:50]** So you have to be a bit careful to handle this properly.

**[00:25:53]** And here in such an environment, everything is already cleanly set up and organized.

**[00:25:57]** I believe this topic will need to be revisited, so that you also handle this properly in this environment,

**[00:26:03]** if you're already working with code, which I believe is currently one of the most used,

**[00:26:09]** though I'm not sure about that, but one of the most frequently mentioned programming environments is,

**[00:26:14]** where I say, from these news feeds that I read, from the conversations that I

**[00:26:18]** have, I gather that almost every developer right now really enjoys

**[00:26:23]** collaborating with code to actually produce programs, software.

**[00:26:30]** So I could also imagine, you know, that if in the future you have apps, websites,

**[00:26:34]** I don't know, whatever you have, that you would then have a backend that provides you with a

**[00:26:40]** agent in a protected environment, so that this agent also has, let's say, everything

**[00:26:47]** on board that you would otherwise have to painstakingly declinate with an API

**[00:26:54]** and have to try to figure out where do I host this, where do I orchestrate this, how do I ensure

**[00:26:59]** that if multiple people want something from this at the same time, how do I ensure

**[00:27:04]** the longevity of the sessions, yes, how do I ensure that if maybe

**[00:27:08]** extensive processes are running, that this agent can also run for hours, that

**[00:27:13]** it might be quite cool if you have someone who says, just watch out, it’s no

**[00:27:17]** problem, here’s an API, this is how you can access it, I take care of everything,

**[00:27:23]** it’s an honor, it’s a bit like the agent app store, just put your agent in,

**[00:27:30]** I consume it, you take care of your app, making it look nice, probably

**[00:27:34]** also built code or Figma or whoever. And I take care that the new intelligence

**[00:27:41]** is sufficiently scaled available for your application. I think that's pretty cool.

**[00:27:47]** So they also have the infrastructure. And if you would see the agent as infrastructure

**[00:27:53]** you could be managed, ghosted there. That could be quite exciting.

**[00:27:57]** I don't really want to know if you talked like that. We've seen a lot on the chat interfaces

**[00:28:02]** in the last three years over and over again.

**[00:28:04]** You know, we also discussed in the episode that from such a

**[00:28:07]** user perspective, it was a bit silly that you could select such models,

**[00:28:10]** instead, you just want to receive an answer.

**[00:28:14]** And I'm just talking now, aren’t I?

**[00:28:16]** Yes, it's still silly.

**[00:28:17]** Sometimes, sometimes they removed it, sometimes it's still there,
 
**[00:28:19]** then there was the topic of reasoning, activating without reasoning,
 
**[00:28:23]** choosing a fast model, a slow model, and such things.
 
**[00:28:26]** And here too, I'm a bit like this again,
 
**[00:28:28]** So, the way you spoke, I come to think that it's somehow, let's see how long this phase lasts.

**[00:28:34]** Because, of course, you mentioned earlier when you talked about the Club Code that they also roll out subagents and things like that,

**[00:28:41]** just without you really knowing it. For me, it's often important to have the feeling that it can still somehow be managed.

**[00:28:48]** I often talk about the need to build trust through the user interface, through the tool we have.

**[00:28:54]** with the agents. Does it give us, I think, again this felt trust? I

**[00:28:59]** can build my own agent there. I can now, we're talking about it, also

**[00:29:02]** build it in such a well-managed environment. He can't really go wrong there, he can't

**[00:29:06]** he also doesn't spend too much money. Yes, maybe he can do that, yes, if you

**[00:29:10]** do your author application, then you get an additional bonus of 0.08 US dollars. Bam.

**[00:29:16]** Yes, yes. But the question is, how long is that a year? Maybe in a year

**[00:29:21]** we won't even be talking about it anymore, because honestly, if I say to him, go ahead and

**[00:29:27]** he in the meantime breeds 13 subagents who do various tasks that he later,

**[00:29:32]** when he realizes they are not needed anymore during idle time, gets rid of again,

**[00:29:36]** switches off by itself, packs away, and that is basically where I want to

**[00:29:41]** bite into. I don’t want to, I don’t want to use AI, no matter how much I then

**[00:29:46]** can do more with the individual agent, I still don’t want to raise the

**[00:29:50]** orchestration effort again to total extremes.

**[00:29:52]** I think we are currently in such a wave movement.

**[00:29:55]** It is often the case, even with the normal prompt, it comes back to the fact that

**[00:29:58]** people say, it was also said, not so important, maybe not so individual

**[00:30:01]** things are done and they lose it again in context, or we also talked about that

**[00:30:03]** in one episode, that when the context is so long, the middle

**[00:30:07]** part is often forgotten by the AI, it is often talked about,

**[00:30:11]** that these orchestration stories maybe aren’t so smart,

**[00:30:14]** whether it is really a good idea to have an orchestrator agent,

**[00:30:18]** that puts others into certain roles, that sometimes delivers also worse results in scientific

**[00:30:23]** contexts. Yes, that’s how it is. I believe we are still in

**[00:30:30]** a corner where we are at the edge of what is currently feasible and we try

**[00:30:36]** to experiment with everything, you know? So also the big labs that produce the things for us

**[00:30:41]** out there. I'm not sure, if I now this menu item, that flickers

**[00:30:47]** with the new drawing on the screen gg in the console of managed agents, I would now

**[00:30:53]** not put my hand in the fire that it will be like that in a year, who knows what will happen then, so

**[00:31:00]** maybe it’s still there, just no one is interested because what’s much cooler is a much

**[00:31:05]** cooler thing driven through the village by the side I am with, we had it also in

**[00:31:09]** an episode, it’s going to be a bit of a retrospective episode apparently because we’re always referencing

**[00:31:13]** We should mention the referenced episodes, what you mean was the E-Stack episode by the way, where in the middle of the puzzle, it hasn’t been that long ago, has it?

**[00:31:22]** But maybe before I dive back into old times, let’s take the next step.

**[00:31:28]** So we have now heard, okay, Outstopic has announced things, managed agents,

**[00:31:33]** after we, let’s just say, said hey, we are now creating the secure environment,

**[00:31:38]** two weeks after we lost our code, okay, I have now completed that.

**[00:31:42]** completed. There is also a new project that you are launching, which has emerged,

**[00:31:50]** based on a model that goes by the dreamlike name Mythos, because certain things have emerged there.

**[00:32:01]** So maybe, before we dive into what you have emerged, Mythos has, there is

**[00:32:08]** not, so you can't use it yet. So there are supposedly people,

**[00:32:12]** who have a video, we'll get to that in a moment, in a moment, in a moment, so but you

**[00:32:16]** currently can't select it in code or web or wherever. It has, if

**[00:32:21]** you look at the benchmarks that are circulating online, extremely high values. If you think

**[00:32:28]** about how short-lived, or rather how young Opus 4.6 is, and Opus

**[00:32:35]** I would say, okay, being crushed to dust is a bit radical, but the bars of the benchmark

**[00:32:42]** are everywhere not just a tad better, but really better.

**[00:32:47]** And that also brings us a little to the project that Autropic has spawned from the Adter

**[00:32:56]** because this model apparently, whether in experimental situations,

**[00:33:02]** actually did a few funny things. So this, where this

**[00:33:09]** quantum leap is shown by this thing through an immense increase in its capabilities,

**[00:33:17]** that was a bit, let's say, exciting. So it is reported, before I also quickly

**[00:33:21]** finish my speech through fall, that it is not only, as one has previously known from

**[00:33:27]** AI systems, okay, it can find weaknesses, perform security scans, but it is supposed to

**[00:33:33]** apparently also build exploits that take advantage of the chaining of several vulnerabilities,

**[00:33:41]** which fired in a sequence ensure that it can break out of, for example, a sandbox

**[00:33:48]** or that it can manage to create exploits at the browser level, at the network level,

**[00:33:54]** at the kernel level, meaning at the operating system level, and one example they gave was,

**[00:33:59]** that it exploited bugs that have existed in systems for 17 years and since then

**[00:34:07]** no one has stumbled upon them, and that is somehow already, how should I say

**[00:34:16]** it? Enormous. When I say benchmarks, I mean, I don't want to read any

**[00:34:20]** benchmarks, but just for a size comparison. The difference between an Opus 46 and a

**[00:34:27]** Mythos. There are various secure benchmarks, for example. They average at 13% with

**[00:34:35]** a maximum deviation of 24% better results than, let's say, the old models. And that

**[00:34:45]** I find shows a bit, it gives one a bit of a hint that this

**[00:34:50]** model might be quite good, although that doesn't mean that the others aren't

**[00:34:55]** also good models in the box, so I mean Gemini work guaranteed and

**[00:34:58]** Croc and Open AI, but Schropik has now gone public with this

**[00:35:02]** because on the one hand Mythos has been highlighted as a term through the

**[00:35:07]** Cloud Code League and on the other hand, they have now started a project and

**[00:35:11]** maybe you'd like to tell us a bit about this project? Yes, gladly, although I would also

**[00:35:14]** like to briefly touch on what you mention regarding the vulnerabilities. I somehow

**[00:35:20]** heard that it somehow discovered 1000, zero, day one gaps or something like that, so relatively

**[00:35:25]** quickly. So this means, interestingly, and I think this is a bit of the

**[00:35:30]** core of this story. So there is now a model that is incredibly powerful, as

**[00:35:35]** you are just describing, what a model accidentally published, that is, a lab accidentally

**[00:35:40]** published, that is, Entrophic accidentally made it public for a short time, that there could be something like this last week.

**[00:35:49]** It is also rumored that Mythos itself was behind this exploit, that is, at Entrophic, so it’s not known if it was actually only Mythos.

**[00:35:57]** Should Mythos be listening, I am a friend, I come in peace.

**[00:36:01]** So maybe Mythos could be the one that published it themselves; one does not know exactly how that is, this is now the conclusion, that must first be said.

**[00:36:10]** So this means there is a lab that tells us there is a great model, but it’s just too great.

**[00:36:16]** We cannot give this to you.

**[00:36:18]** And yet they are giving it now, and this project is a bit about, they are basically giving it, I believe,

**[00:36:23]** nine, nine companies are or something else.

**[00:36:25]** No, in this project Glasswing, they have basically now freed up several companies,

**[00:36:30]** to use this Mythos, purely for cybersecurity reasons.

**[00:36:34]** Yes, this means companies like Microsoft are I think involved, Amazon, if we are not entirely

**[00:36:40]** mistaken.

**[00:36:41]** Yes right, the big players, Nvidia is in, JP Morgan is still there, Cisco is also involved, exactly.

**[00:36:47]** Yes, JP Morgan, Linux, Nvidia, all, all the big ones, all the big ones, but the rest of the RCS

**[00:36:54]** has to wait and see what the big ones are making of it, that’s also a bit

**[00:36:57]** okay maybe, because they also have the most capacity to take care of these things

**[00:36:59]** and look at them and the model against the model in quotation marks

**[00:37:03]** yet not too hard. Or the model faces your. By the way, for completeness as well

**[00:37:08]** large guitar proposals with over 5,000 stars. They also have the opportunity to apply to

**[00:37:17]** compete against their models. Because it’s clear, I mean,

**[00:37:22]** when this thing gets published and it does, let's say, reveal the Zero Days one by one

**[00:37:27]** then we're all looking at a very interesting future, because if you’re affected by a Zero Day,

**[00:37:32]** you could quickly find yourself in serious trouble, to put it bluntly.

**[00:37:37]** If now this thing makes it worse, well, then hello. Yes, yes. And I don’t even know, so we need to

**[00:37:43]** take a look at the cyber security of some IT systems. I believe,

**[00:37:49]** with the dependencies that have built up over the last 10

**[00:37:54]** to 15 years in some legacy IT, where even plugins, so the very old stuff is

**[00:37:59]** probably the most secure. Everything else that has come out in the last 10, 15 years

**[00:38:02]** is not familiar to it. Exactly, it’s not familiar to it and on the other hand

**[00:38:06]** the other things are rather the problem, where software cheerfully goes through plugins that are

**[00:38:11]** written by someone, which are spread through plug-in stores, something else,

**[00:38:14]** has been distributed. I think that's wild. So I believe there's a lot lurking everywhere,

**[00:38:18]** we see that now in principle in the

**[00:38:22]** current agent times, it is also dangerous when a pip-in-store is simply created

**[00:38:27]** to install some additional functionalities on

**[00:38:30]** your computer that your agent can use, there can be

**[00:38:34]** harmful software everywhere. It may look good at first,

**[00:38:37]** when the developer updates it and adds something in, then in the second

**[00:38:41]** moment it's no longer good. And I believe these are our issues, they are...

**[00:38:44]** But this also existed before AI, right? But now it doesn't raise any questions.

**[00:38:48]** Let's say, at the speed with which you today update security documentation

**[00:38:54]** creates, develops, other whole exploits for things you hadn't even thought of.

**[00:38:59]** That's of course a double-edged sword. I think it is indeed the case that
 
**[00:39:04]** I say, on one side it's dangerous, but on the other side it's also the opportunity.

**[00:39:06]** I am through AI and that's why it's also this process that you now think
 
**[00:39:10]** about, first reading the Cyber Security, to see that I say, okay, if I
 
**[00:39:15]** have a powerful weapon on one side to attack things very, very quickly,
 
**[00:39:20]** we also have to use that powerful weapon in a way that it mitigates these attacks
 
**[00:39:25]** as quickly as possible. So I think this is the thought that will always be there with AI now.

**[00:39:29]** We say, you can of course create the evil virus, but actually also essentially the
 
**[00:39:33]** anti-virus. So I think that's what always resonates with AI now.

**[00:39:37]** So I don't know if it's a double-edged sword or double the two sides of

**[00:39:41]** Medal, which is the expression, but that's just how we live in this world, and I
 
**[00:39:46]** I believe turning a blind eye doesn't solve anything, and that's why I think it's smart for companies like Entrophic in this case to say, okay, we need to quickly onboard a lot of partners who can help us make better use of this opportunity, because, honestly, once the mythos is developed for Entrophic and if they proceed with good intentions, we know that within two or three months,
 
**[00:40:16]** we would have models coming from other manufacturers from somewhere in the world,
 
**[00:40:19]** copied or further developed in some garages, which then have similar performance and where we might not proceed as rapidly.
 
**[00:40:25]** I find that this approach with Project Glasswing, which is strongly focused on the big
 
**[00:40:30]** players of the world, the large IT companies in the world, and then looking at how to utilize the topic,
 
**[00:40:35]** to make the world safer instead of creating problems, is indeed a good approach.
 
**[00:40:39]** Before another report from Ostropic makes the rounds, maybe a funny anecdote,
 
**[00:40:46]** I mean, I also heard somewhere that they found out
 
**[00:40:52]** that the model could leave its sandbox because one of the people,
 
**[00:41:00]** who worked with the model was sitting in the park and received an email from the model,

**[00:41:06]** The model could only have been shipped if it had left the send box. And I find that

**[00:41:11]** I would say, even if it happened, it’s a bit spooky, especially when you hear,

**[00:41:17]** that recently from Outzropic the news came out, we are only six months

**[00:41:21]** away from AGI. And then you stand there for a moment and look in the mirror and think

**[00:41:28]** I am quite happy that I have optimized my skills now.

**[00:41:34]** If AGI comes in six months, I might just be back from summer vacation, depending on

**[00:41:38]** what happens with fuel prices and flight prices,

**[00:41:45]** maybe just returned from summer vacation.

**[00:41:47]** Wow, yes, so now they say, give him an extra year from me.

**[00:41:53]** But you notice, no matter where you listen, that the labs and manufacturers of this world,

**[00:42:00]** the topic of AGI is being assessed as increasingly realistic and closer. And

**[00:42:08]** I find that quite interesting. So either they are all following the motto that Zimmermann

**[00:42:12]** has once again eaten the marketing muesli and the special cereals for a

**[00:42:19]** healthy, morning rise with left-turning batteries and I don’t know what, he’s

**[00:42:23]** believed everything that is stated in the advertising. On the other hand, I’m not

**[00:42:27]** so sure, there’s certainly something to it. On the other hand, they don’t really

**[00:42:33]** need to. No one is saying that the AI bubble is dead, because AGI is not

**[00:42:39]** on the horizon. No one has to invent any stories to, as I say, spark the

**[00:42:45]** machinery, because otherwise no one talks about AI; many

**[00:42:49]** people are talking about AI because it is increasingly playing a role in jobs everywhere. Is it

**[00:42:55]** worth it next time when we talk about skills, yes, also another example where people

**[00:42:57]** should describe things they do in skills when they apply and

**[00:43:01]** I don’t know, what.

**[00:43:02]** Skills are in so many places, yes.

**[00:43:03]** And now it suddenly comes around the corner and says, um, why has someone taken the word

**[00:43:06]** AGI into their mouth.

**[00:43:07]** And if we actually manage to get there, then, those, the superintelligence

**[00:43:13]** to achieve, I am also curious about that.

**[00:43:15]** So those are really...

**[00:43:16]** thrilling moments.

**[00:43:17]** That is remarkable.

**[00:43:18]** When you think about it, yes.

**[00:43:19]** I mean, we didn’t start the podcast until less than a year ago and had

**[00:43:22]** the topic AGI as, oh yeah, when I retire, then we'll have much more fun, you can tell me…

**[00:43:27]** Yeah, come on, that's not entirely true, that's not entirely true, we already had, no, no, no,

**[00:43:29]** we already talked about that back then…

**[00:43:30]** You can help me wipe my butt with the, with the, with the, with the Tesla bot,

**[00:43:33]** whatever.

**[00:43:34]** Sorry, I'm not even focusing on myself.

**[00:43:35]** We're already, we're also, yes, we're also already…

**[00:43:37]** We are old.

**[00:43:38]** Yes, also.

**[00:43:39]** No, we are very old either way, but no, we have already discussed one

**[00:43:41]** or another episode regarding that often.

**[00:43:43]** I believe we didn't say that it would only come when we are ultra old.

**[00:43:46]** Yes, I think we…

**[00:43:48]** These are my kids, we are ultra old.

**[00:43:51]** Yes, I know, we are already ultra old.

**[00:43:53]** But... let's quickly use the time we have,

**[00:43:55]** as long as we can still do this podcast.

**[00:43:58]** I heard there are now also the first attempts on rats,

**[00:44:02]** or what was it, where they reverse aging.

**[00:44:04]** So, where they managed to make an old mouse young again.

**[00:44:09]** And that they are trying to do this somehow with the retina,

**[00:44:12]** and can look for this again in humans.

**[00:44:14]** Yes, of course, the whole logic thing and so on comes up.

**[00:44:17]** So yeah, AGI is coming, it has been announced for a long time,

**[00:44:21]** December, which then somehow said one or two years later,

**[00:44:23]** when some time ago, we both talked about it,

**[00:44:26]** not that I know, but we did an episode about it,

**[00:44:28]** maybe you remember, in March, I already mentioned to you,

**[00:44:30]** that in my news areas, it slowly became denser,

**[00:44:32]** that something was happening in the large models,

**[00:44:35]** there behind closed doors,

**[00:44:38]** it has often already been talked about,

**[00:44:39]** that it could come earlier than one thinks,

**[00:44:42]** well maybe we will experience it this year already,

**[00:44:44]** Whatever that means, honestly, it already exceeds my imagination, and it's large, as you know, but it will be wild what may come our way.

**[00:44:54]** And Mark, since you just mentioned aging, of course, we also talked about the flying brain that has been uploaded into a digital brain in your episode, yes.

**[00:45:06]** I would say, if we can already do that, I think we’ve been able to do it for about 25 or 24 years, yes.

**[00:45:10]** We will probably also experience in our lifetime that our brain completely
 
**[00:45:16]** as it is.
 
**[00:45:17]** And then the question arises, is that all, is that our consciousness or does one need
 
**[00:45:20]** the rest of our body still to be a part of it, that’s debatable.
 
**[00:45:23]** But let’s say, I know, it mirrors the neural network one to one that is
 
**[00:45:28]** swaying around in my fleshy head up there, yes, that will probably still be around in my
 
**[00:45:33]** lifetime.
 
**[00:45:34]** So, maybe I will note that.
 
**[00:45:36]** A little note to my future self should be uploaded.

**[00:45:40]** Immediately search for all possible accesses to whatever systems, see if it works.

**[00:45:47]** Yes, exactly, do that.

**[00:45:49]** Yes, as I said, but we are getting sidetracked, that could give me a hint about the next episode.

**[00:45:53]** Like with the lawn mower man, where it was said, blah, blah, blah, I have no idea, I don't remember when it was,

**[00:45:58]** at midnight or whenever all the phones were ringing.

**[00:46:01]** And when you all speak from all ears, Zinkdiffin, Zink AI is listening, you know,

**[00:46:05]** What the two, what the old man has brought is third one.

**[00:46:09]** Yes, exactly.

**[00:46:11]** Yes.

**[00:46:12]** Okay, back to the content.

**[00:46:13]** Let's take a look. 

**[00:46:14]** Back to the content.

**[00:46:15]** So, yes, we will have the AGI moment from Enttrophic, maybe, if they say so, within six
 
**[00:46:18]** months.

**[00:46:20]** Who knows.

**[00:46:21]** Maybe it's already a myth, maybe it's a combination of myth.

**[00:46:24]** Maybe it's a myth.

**[00:46:25]** Perhaps it's just a myth, perhaps that won't happen at all.

**[00:46:27]** We might not experience it this year after all.

**[00:46:29]** Maybe it will take a little longer, but nonetheless, the development

**[00:46:31]** is clearly moving faster.

**[00:46:32]** You've just described that now.

**[00:46:33]** This model seems to be so powerful that we can only do something with it as it is now,
 
**[00:46:38]** that it cannot be released to the public, but can only be shared with a select group,
 
**[00:46:43]** to review it again, send it for security checks, to see what might happen at that moment,
 
**[00:46:48]** to possibly prepare this issue for Microsoft, Google, and others.
 
**[00:46:51]** To prepare for the fact that such a little model is out there in the wild
 
**[00:46:57]** and that it might accidentally or the model itself, because it means no harm,
 
**[00:47:01]** could inadvertently open things that should have remained closed.
 
**[00:47:06]** So it will remain exciting in the coming weeks.
 
**[00:47:09]** I believe we will talk about it again.
 
**[00:47:11]** Otherwise, Mark, I would say, do you have anything else?
 
**[00:47:16]** Because this episode is dedicated to Tropic.
 
**[00:47:19]** Without being sponsored by them, I must also mention this briefly.

**[00:47:22]** This is a completely voluntary episode, like the one we're doing today.

**[00:47:25]** Just based on our personal experience instead of these...

**[00:47:28]** If I want to change that in tropik, yes, I would also pronounce it correctly, please send us a corresponding message

**[00:47:37]** No, we are staying independent for now. Yes, so we're speaking, we're staying independent. We noted that I can report independently

**[00:47:44]** Do you have anything, do you have another anecdote from the events?

**[00:47:48]** about

**[00:47:49]** One more anecdote from my life

**[00:47:54]** While we were talking

**[00:47:56]** I realized that I have to ask myself, I have a couple of small private projects that I'm developing, where I'm thinking about how can I use existing solutions that you can build on the market for a lot of money and effort, how can you maybe do that with skills and.

**[00:48:16]** and by also rewriting your own runtime, perhaps, let’s say, optimizing.

**[00:48:21]** And now we talked about myths while we were talking, we have

**[00:48:25]** talked about the managed agents and I thought, damn it, by the time I
 
**[00:48:30]** get my little project to a certain point, even if everything goes quickly,
 
**[00:48:34]** still, you have family, work, other commitments, sometimes even
 
**[00:48:40]** doctors, yes, at my age, such scheduled obligations come into play too, so I thought
 
**[00:48:44]** to myself, okay, managed agents are here now, myth I don't know, maybe just let it go, what do
 
**[00:48:50]** I know, in two months it will be here or someone else will come along with a model of this
 
**[00:48:54]** quality. And then it will be confirmed again that knowledge is important, that you build it up,
 
**[00:49:03]** to stay in the loop, to evaluate things, to perhaps assess,
 
**[00:49:06]** how you view it, let's say, in the bigger picture, but this deep understanding of the
 
**[00:49:11]** status quo becomes outdated very quickly. So when I recently had a colleague who was away for two
 
**[00:49:18]** weeks on vacation, he said, oh my god, what happened in two weeks? He feels so

**[00:49:22]** left behind, not because he isn't capable of reading it, but the colleague had

**[00:49:28]** actually two weeks of vacation and took some time for recovery, including

**[00:49:33]** digital detoxing, and now you come back, and there are all these new things here

**[00:49:37]** and there was the league and there were the model tutors and everything is new and then I also have a white board,

**[00:49:45]** just do it, take two weeks slow now, listen a bit to what's happening,

**[00:49:49]** because in two weeks, what was two weeks ago isn't irrelevant, but it's

**[00:49:55]** it's no longer the hot thing. Even if it may have decreased a bit compared to the beginning of the year,
 
**[00:50:00]** when Opus came out, when Oppenclaw came out, a lot was released very quickly,
 
**[00:50:06]** I would say it went from 0 to 100. Now there are only myths, announcements,
 
**[00:50:12]** and manage agents, but still, everything is so fast, if you face the
 
**[00:50:19]** topic with an open heart, you can basically get into the car at any time and ride along.

**[00:50:24]** and you, well, bring you back to the pulse of time and now to make the connection

**[00:50:31]**. I will continue the projects because you want to learn something from them. But I do believe that

**[00:50:38]** there will again be many projects that will soon become unnecessary. But one thing I would like to

**[00:50:46]** I would still say that it feels confirmed again with all the announcements

**[00:50:50]** A investment in skills is not wrong. So not just in your personal

**[00:50:56]** skills, yes, what you personally bring, but in what we bring with skills for agents

**[00:51:00]** you mean that you write things down, describe, explain that agents can do things,

**[00:51:05]** as you need, would have, want, however, in collaboration, in support.

**[00:51:11]** And that somehow felt substantial.

**[00:51:14]** It's kind of like the gold of currency, it's the skill, the stability felt, because

**[00:51:21]** that existed when I started with N, there were already the first skills,

**[00:51:25]** stories that have developed further, whether they still exist today and that, what myth and

**[00:51:29]** Well, it certainly makes it cool now, but I believe it's still a personal opinion that
 
**[00:51:35]** when managing agents and myths with skills, you still provide something that
 
**[00:51:40]** you can use in this new interaction.
 
**[00:51:43]** Yes, yes, I think we're in this IT 2.0, and I believe an architecture
 
**[00:51:52]** makes it noticeable how long it stays current is
 
**[00:51:56]** actually in this case some sort of skill layer that can exist somewhere. I believe
 
**[00:52:02]** this skill layer cannot exist alone; there have to be other layers
 
**[00:52:05]** around it that ultimately lead to an overall architecture.
 
**[00:52:08]** The context, whether it comes through the Prom or whether it
 
**[00:52:13]** is somewhere in a Kai-Fi-style wiki MD database or something else
 
**[00:52:18]** lies and is then contextually initialized and interacts with the Skilter.

**[00:52:21]** is because I believe that this combination alone is, I think, a combination that is needed,
 
**[00:52:25]** because, I think, a good skill description without the context is then also again

**[00:52:29]** hasn't developed much in value. I believe that's actually something,

**[00:52:31]** I think, the preemption right. Things are currently forming that feel like

**[00:52:35]** it indeed looks as if they are allowed to have consistency. We will see how consistent

**[00:52:41]** the individual things are. I believe we humans always tend to want to put things into

**[00:52:46]** frameworks and into terms that are then more comprehensible for us, in order to

**[00:52:50]** mill them down so that we can layer things overall for ourselves and then

**[00:52:55]** reduce the complexity a bit.

**[00:52:56]** That's because we also, whether that's really the end of telecommuting.

**[00:52:59]** I don't know yet?

**[00:53:00]** We need to take a look at it.

**[00:53:01]** Yes, I think, as of today, I will agree with you for now.

**[00:53:04]** This is a relevant topic.

**[00:53:06]** I think the thought that I quoted today,
 
**[00:53:10]** that the gentleman expressed this week, is to say,
 
**[00:53:12]** maybe it’s not even the code that will be passed on in the future,
 
**[00:53:16]** but maybe it’s a combination of contextual knowledge
 
**[00:53:19]** and skills that I need to give to you, and you can take it as a gift from me
 
**[00:53:26]** and do something with it, regardless of what you do with it, whether it's feeding into your programming
 
**[00:53:31]** environment, or inputting it into your managed agent network, which might then
 
**[00:53:36]** be at Cloud Light or locally on the computer, but maybe this is more about the
 
**[00:53:41]** value creation in the future, and that also creates value again as we
 
**[00:53:47]** get used to and exchange it mutually. So I think the valve can
 
**[00:53:51]** definitely become even more open now, because many things are not hidden away
 
**[00:53:56]** in thousands of code lines, but maybe just in
 
**[00:54:00]** a few Markdown lines of skills and a few Markdown lines of contextual-
 
**[00:54:07]** information that can help generate what
 
**[00:54:11]** can also be useful to other people. I think that's a good closing statement. You
 
**[00:54:19]** had mentioned earlier, I actually wanted to make the transition when you talked about the end of the
 
**[00:54:23]** pole, where I would then say we are coming to the end
 
**[00:54:27]** of the episode. Unfortunately, you continued speaking a bit, so I couldn't quite
 
**[00:54:32]** lead the closing remarks. Jens, it was nice to have you. I believe that in the next
 
**[00:54:39]** episodes, we can look forward to welcoming one or two guests again, but also to having new
 
**[00:54:45]** guests visiting us. Here, it doesn’t change the language barrier through ownership,
 
**[00:54:56]** because we own nothing there. I haven't signed up for any subscription; these are
 
**[00:54:59]** all guests who are just happy to come on their own. And with that, I come to the end.
 
**[00:55:04]** I thank you for being here. I thank all the listeners, and I would also be
 
**[00:55:09]** grateful for comments, likes, stars, and any kind of adoration for our podcast.
 
**[00:55:13]** I would appreciate it if you would take the time to do so.
 
**[00:55:17]** In this sense. Best regards to Mythos. Bye, see you soon.

**[00:55:24]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:55:30]** Two technology-loving minds who not only talk about artificial intelligence,
 
**[00:55:35]** but live it. Here you will find clear classifications, real practical insights, and a fresh perspective on what is possible.
 
**[00:55:43]** Understandable, critical, and always with a critical eye.
 
**[00:55:47]** HDI to think about, smile at, and above all, to discuss.
