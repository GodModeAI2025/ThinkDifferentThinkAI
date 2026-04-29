---
title: "Automation trifft Organisation: n8n × Notion"
episode_index: 10
published: "Sun, 19 Oct 2025 02:55:00 +0000"
duration: "4253"
audio_url: "https://audio.podigee-cdn.net/2160435-m-68cc27d9dd04b9b4b792179852421201.mp3?source=feed"
guid: "06f4724a07d5e8732afbee5ef860252b"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T20:34:41+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/010 - Automation trifft Organisation - n8n × Notion.md"
translated_at: "2026-04-29T17:15:01+00:00"
---

# Automation Meets Organization: n8n × Notion

**Published:** Sun, 19 Oct 2025 02:55:00 +0000
**Duration:** 4253
**Audio:** https://audio.podigee-cdn.net/2160435-m-68cc27d9dd04b9b4b792179852421201.mp3?source=feed

## Description

How Notion and AI are revolutionizing our digital lives – a crossover conversation full of aha moments.
In this (crossover) episode, Mark Zimmermann (unfortunately without Jens) and our guest Dirk Beckmann discuss the developments in the digital world, particularly the role of Notion and AI in modern workflows. They highlight the functions of Notion, the integration of AI, and the practical applications in agencies. The two share personal experiences and insights about the challenges and opportunities these technologies present. In this episode, Dirk Beckmann and Mark Zimmermann discuss the role of agents in Notion, the integration of AI, and automation tools like n8n, as well as the future of Notion in the digital world. They emphasize the importance of master prompts and customizations to enhance efficiency and productivity. The two experts share their experiences and provide valuable tips for working with Notion and AI.

Guest: Dirk Beckmann

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two tech-loving minds who don’t just talk about artificial intelligence but live it.

**[00:00:14]** Here you'll find clear classifications, real practical insights, and a fresh perspective on what's possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** KD for reflection, for a smile, and above all for joining the conversation.

**[00:00:29]** Welcome to the new episode of ZinkDiffinZink AI.

**[00:00:38]** Today it's all about agency, today it will have a bit to do with workflows and

**[00:00:42]** today it's without Jens, but still with a very competent guest who will

**[00:00:49]** surely introduce himself shortly.

**[00:00:50]** Yes, welcome to a new episode of the digital time, my podcast that I

**[00:00:57]** started during Corona and still continue sporadically. Today with a

**[00:01:02]** special episode, Mark just called it a crossover and that's the name of the guest in

**[00:01:07]** this episode, the digital time today with topics like Notion, N8N, Workflows and the ubiquitous

**[00:01:17]** topic of AI. Welcome, Mark. Yes, welcome, Dirk. I actually found the idea of such a

**[00:01:23]** crossover episode a bit crazy, but at least our podcasts, we can hold on to and

**[00:01:28]** tuning in. Like the roofer, as we want it. I started, so I'm asking

**[00:01:33]** first, Mark, maybe tell us a bit about yourself before I may introduce myself to you as well.

**[00:01:38]** Yes, very gladly. I'm Dirk, I'm the managing director and founder of Art und Weise,

**[00:01:44]** professionally involved with the digital age for over 35 years, just like this podcast is called,

**[00:01:50]** And new things keep happening, and I won’t recount all 35 years, but the last, let’s say, two years have been quite impressive and overshadow everything we experienced before, at least in my opinion.

**[00:02:06]** And especially with my special topic Notion, where spoiler, I would say this brand and this company are as amazing as Apple, and that says a lot.

**[00:02:17]** Especially with this topic and AI, it’s really great that we’re here today.

**[00:02:23]** So, I work in a digital agency called Art und Weise,

**[00:02:28]** with 60 employees in Bremen, and now to you, Mark, who are you actually?

**[00:02:33]** Yes, so for the listeners of your podcast, Mark Magzerman, I am employed at NBW,

**[00:02:41]** responsible for everything regarding mobile loss developers, so all apps for

**[00:02:46]** internal use. I’ve been doing this since 2009.

**[00:02:51]** One doesn’t get any younger, so the saying about wise old gray men

**[00:02:55]** standing in front trying to tell the world definitely applies to me.

**[00:02:58]** My main job is, let’s say, the politics behind the scenes, the ideas

**[00:03:03]** to implement new products in our corporation for mobile devices, just as

**[00:03:08]** you said a little bit, what’s been happening with me for the last two years

**[00:03:10]** has actually been more like the beginning of the year, namely this topic

**[00:03:14]** Since that day, something new has been coming over the horizon, called AI, what is all possible with that?

**[00:03:21]** And maybe, you already hinted earlier that we’ll also be talking about Notion.

**[00:03:27]** Perhaps a fun fact.

**[00:03:30]** Dirk and I are related.

**[00:03:33]** We belong to the same family tree, I should say.

**[00:03:37]** And in the past, Dirk was very much involved with app rights, and I used to chuckle a bit,

**[00:03:47]** because I was more into Microsoft Windows MCSE training, Windows NT as an operating system.

**[00:03:54]** That was more my home, until I eventually switched to a MacBook and since then couldn't imagine anything better,

**[00:04:02]** than using a Mac, which later also had a significant impact on my job.

**[00:04:09]** I mean, who knows what I do, which companies I interact with, what solutions I build,

**[00:04:14]** what I'm talking about is very Apple-centric. And history seems to repeat itself.

**[00:04:20]** Not that I like the fashion from back then, definitely not.

**[00:04:25]** Neither in terms of body size, nor, let's say, visually would it suit me either.

**[00:04:30]** No, something similar has emerged with Notion, and N after N, because those are

**[00:04:37]** definitely still tense matters, from which I hope to get a little something from you

**[00:04:39]** listen today, where I also learn a lot from you and can learn, because you are a very strong

**[00:04:44]** proponent of Notion in the right way. Yes, it's nice that you say that, because I

**[00:04:50]** want to disclaim right now for everyone from my company who will eventually

**[00:04:55]** hear this podcast. I feel you, I love you all, but the fact that I’m totally nerdy about Notion and

**[00:05:03]** that it sometimes annoys you, I get it. I think so too, we're working on it.

**[00:05:08]** There are many people now who support me to make it better. But

**[00:05:13]** Notion is the piece of software that has truly impressed me in all these years of digital time

**[00:05:20]** has been put under a spell for years now. And I really have to say that what is possible with it,

**[00:05:25]** but especially what the vision of the main founder is, I would say

**[00:05:30]** I'm going to say, Ivan Sao is just madness, namely my favorite saying, namely
 
**[00:05:36]** everything is connected to everything. And a few weeks ago, somehow
 
**[00:05:40]** Narschend 3.0 came out, so this AI version that quite a few people are talking about.

**[00:05:45]** out. And that has now crowned the whole thing. But we'll talk about that

**[00:05:48]** So, yes, thank you very much. I'll say something from my perspective. Thank you for being here.

**[00:05:52]** We were already together with my podcast, and then I think we weren't together yet.

**[00:05:55]** No, it's a premiere for you and for me. And vice versa,

**[00:06:00]** one remembers the image with the Apple Vision Pro. That's the cover of the podcast with you.

**[00:06:06]** And I'm looking forward to tonight. I think you said something earlier,

**[00:06:10]** there was also something in there that many like to forget when they talk about

**[00:06:15]** AI systems, and don't worry, this won't be too strong of a digression,

**[00:06:20]** because it's about the human aspect. So, you have something to do, you have a tool at hand,

**[00:06:24]** with which you want to do something, but what's the use of the best tool if you have no one

**[00:06:28]** who collaborates. So if someone thinks that’s bad, from that side, I think too.

**[00:06:33]** the point that perhaps one should also speak, both in good and in bad,

**[00:06:37]** along the lines of, what do we encounter when we also incorporate technology in this

**[00:06:41]** The manner in which this is linked to hype in the form of either salvation or

**[00:06:46]** the downfall of humanity, depending on whom you ask, that one also might just

**[00:06:51]** two or three sentences maybe later occupied. But you mentioned Notion, can

**[00:06:56]** you or the listeners probably best explain to me briefly, what is actually
 
**[00:07:00]** Notion? Yes, good question. Notion is a cloud-based app, so a service that you can

**[00:07:07]** first of all, if you want to register for free, there are many things. So a database,

**[00:07:13]** a note-taking tool, a project management tool, a wiki, a knowledge database, and so on

**[00:07:21]** and so forth. But above all, Notion is the possibility that almost everyone,

**[00:07:27]** who can find their way a bit with the computer, can create their own environment, their

**[00:07:34]** own, how do I want to manage my data? How do I want to organize myself to build a field

**[00:07:38]** that can be built? And this idea that everyone can build their own world, that is

**[00:07:47]** actually the basic idea of Notion when they started. Then the AI and

**[00:07:53]** the AI revolution is, so to speak, accompanied by Notion, quite early on. One has to say that the
 
**[00:07:58]** first AI versions that Notion integrated were like, oh yeah, no, then I'd rather go
 
**[00:08:02]** to chat GPT. It wasn't really great back then. And now it is the

**[00:08:08]** ultimate app, if I'm not interested in AI from a technical perspective, but

**[00:08:14]** only from a results perspective. And that's also this topic I have with Apple. Apple has

**[00:08:19]** often highlighted what can I do with it. It makes

**[00:08:24]** the possibility to work with a computer democratized, build the Mac, this

**[00:08:29]** little box and attach a mouse, and that has already made it so that anyone can

**[00:08:34]** so this is the vision to work with it.

**[00:08:37]** Apple presented something in 1984 that I find almost, no, that I find just as revolutionary

**[00:08:43]** as the 3.0 version of Notion, namely the ability to use AI in this era for

**[00:08:50]** me, without needing to know a thousand things, without agents and understanding everything perfectly

**[00:08:56]** one hundred percent.

**[00:08:57]** I can just tell this thing what I want, and it can already do a lot of that now

**[00:09:02]**.

**[00:09:03]** It is just as imperfect as the first Mac, of course from today’s perspective, but it is

**[00:09:07]** just as revolutionary when you look at everything before it for me.

**[00:09:11]** It’s quite funny, actually.

**[00:09:13]** You, just like back then with your, it was really bigger had your Macbook, you had

**[00:09:18]** this giant thing, this huge ship, definitely a 15 inch one.

**[00:09:24]** What holds, let's just say the very big one and I always found it somehow
 
**[00:09:30]** strange how you could work with the Mac and I felt that way for a long time with
 
**[00:09:33]** Notion. You've been talking about Notion for a long time and I kept looking at it
 
**[00:09:38]** and at first I found it off-putting because, let's say, this soft flat paper.
 
**[00:09:44]** You have something there and you have to, let's say, think about how to start,
 
**[00:09:48]** I always said no, I won't touch it and I don't know,
 
**[00:09:51]** what? In retrospect, I have to say, what a stupid story. I would be so glad if
 
**[00:09:56]** many things were already in Notion and I wouldn't have to import them now,
 
**[00:09:59]** because, what did I do instead of using a tool, no matter how well or poorly organized, I put
 
**[00:10:05]** everything into Apple Notes. Now I have 3.8 gigabytes of data, greetings to
 
**[00:10:10]** the team, Notion was sweating during the import. I got myself a small tool to
 
**[00:10:14]** export the notes so I could import them into Notion, but to make a long
 
**[00:10:17]** story short. My alternative wasn't good. So then this actually came,
 
**[00:10:23]** the magical moment and I still remember how you wrote to me, here's the same
 
**[00:10:26]** keynote at Notion. And then I thought to myself, well look at that, they also have a
 
**[00:10:31]** keynote, that’s cool. Let's check it out. And then you open this keynote and
 
**[00:10:37]** look at it and think, yeah, okay, this is a mix of Apple and
 
**[00:10:40]** Sam Altman. There’s a little stage, there’s some
 
**[00:10:43]** presentation behind it, they tell a bit and then they quickly grab
 
**[00:10:46]** you with the topic of what they want to do with AI or what they’re now also releasing as their first
 
**[00:10:52]** functionalities. And suddenly you were no longer in the position where you had to describe a white
 
**[00:10:57]** sheet of paper yourself, but you could tell it what you wanted. And that

**[00:11:03]** I still find that today. When I show people how cool Notion is, they ask a bit about it.

**[00:11:09]** Some things that I know sometimes interest people

**[00:11:12]** are the weather at the vacation spot or something, and you just go into this assistant, say,

**[00:11:17]** create a database, powered by AI, you write in, I don't know, vacation spot, weather,

**[00:11:22]** whatever. And then it starts, it gives you a structure, suggestions, fills in the

**[00:11:26]** weather data for you. That's the first moment where you see a smile on your

**[00:11:31]** face about your area, and that's certainly not all that Notion does,

**[00:11:36]** what Snowshin does. For me, Snowshin since Diversion is like a look-up.

**[00:11:42]** Yes, we have up here, in case someone hears this someday, in the year 2025. It hasn't been

**[00:11:47]** that long since Snowshin 3 was released, and it's one of the tools that is in my top 3

**[00:11:55]** tools. Unfortunately not in the company environment. We are a very Microsoft-heavy

**[00:12:02]** company. It’s not that I haven’t tried to somehow get a foothold with that tool.

**[00:12:07]** But it’s a tool that I say runs circles around

**[00:12:13]** what Microsoft does. Circles around what Google Workspace and whatever the whole

**[00:12:18]** thing is called does. It’s so powerful and from my perspective, very user-friendly

**[00:12:23]** and it needs. When you realize what concepts are possible,

**[00:12:28]** it’s incredible. I’m getting warmed up. Sorry, I’ll give you the floor in a moment,

**[00:12:31]** but when you said everything is, what was that again? Everything is data, everything is,

**[00:12:35]** the sentence? Yes, exactly, I find that so fascinating when you call up the assistant

**[00:12:41]** and you create your connections and tie the components together,

**[00:12:45]** you can link rows, you can link cells, you can link tables, you can link folders, you can link documents

**[00:12:52]** together in an agentic query. That’s,

**[00:12:58]** it’s mind-blowing, it surprises me every time I see the result.

**[00:13:04]** Yes.

**[00:13:05]** And the crazy thing is, when you're standing in front of it now, you have a learning curve

**[00:13:11]** and that is something that has usually been tried to solve in various ways for years

**[00:13:15]**.

**[00:13:16]** sometimes better, sometimes worse.

**[00:13:17]** They have features, they've even built features that are worse because they made these strange,

**[00:13:21]** embedded templates, like wiki functions, these strange things.

**[00:13:27]** No one wants that, the ambassadors keep advising them to please turn it off, no one wants it because you have to solve it differently with the help of people who build templates or with the help of YouTubers. There’s a great YouTuber, a German, who is very, very well-known, Matthias Frank from Berlin, I definitely think he's the best from Germany. He does speak English in his videos, of course, because he positions himself internationally, but he is one of my favorites. And Thomas Frank from the USA is great, and my absolute favorite is of course Simon.

**[00:13:57]** from England with Better Creating. He is the one who also built the great agent. What

**[00:14:02]** I actually wanted to say is, Notion has a learning curve, but it is kind of similar

**[00:14:09]** to democracy, the European Union, and also back then with Apple. It’s a bit more complicated.

**[00:14:15]** actually. That's a bit unusual. But in the end, when you look back

**[00:14:21]** on that, having gone through this learning curve, you say, okay, how could I

**[00:14:24]** live without it. I mean, how could one live without an Apple ecosystem where the watch, the

**[00:14:32]** Division Pro, the tablet, everything is connected? And Apple invented that.

**[00:14:38]** We all know how bad it was in the beginning, the iCloud and so on from Apple.

**[00:14:41]** Zurich you. Yes, for example. I’m only still using it, but it’s the same with Norschen.

**[00:14:47]** I've always had a feeling with Norschen, like with Apple in the 90s,

**[00:14:51]** until 3.0 came out. Okay, I know, it’s good for something that I stand by Norschen and

**[00:14:57]** I always found it great and I'm totally deep into it. But with the launch from a few

**[00:15:03]** weeks ago, you really have to say, it’s basically like Think Different, the ad comes

**[00:15:08]** out, Steve comes back, and everything will be fine. That's how it feels right now. Because it's in

**[00:15:13]** connects all these things. So say that, we all still remember how it used to be,

**[00:15:18]** but I must say, if you haven't looked at the game yet,

**[00:15:21]** we are both of the older caliber.

**[00:15:24]** I recently met people who only know the introduction of the iPhone

**[00:15:29]** from history books, because at that time they were at most

**[00:15:32]** in kindergarten, they had no association with it.

**[00:15:36]** And they were standing in front of me with the knowledge of the keynote,

**[00:15:39]** they had seen it on YouTube,

**[00:15:41]** and explained to me how it was back then,

**[00:15:44]** when the iPhone was released.

**[00:15:45]** And back then, when I didn't quite like the Mac yet,

**[00:15:50]** I had a colleague in my work environment whom I helped,

**[00:15:53]** to put a PCMCIA card into the Apple Newton, to be able to connect.

**[00:15:59]** You know? And these colleagues tell you,

**[00:16:02]** how the world functioned when the iPhone came out

**[00:16:06]** and evaluate it only through the still iconic appearance

**[00:16:10]** of Steve on stage, when he said, an iPhone,

**[00:16:13]** an Internet communication device and just white screen eye port or the other way around.

**[00:16:17]** It doesn't matter, I'm not Stief.

**[00:16:19]** And I find it so crazy that things like, when you say,

**[00:16:22]** okay, how you know it from before, you don't know them.

**[00:16:24]** Yes, it's like when I try to explain to my kids, I don't know,

**[00:16:26]** old phone jokes and they say,

**[00:16:28]** hm, that's very nice, but what is that?

**[00:16:30]** Yeah, well, what am I supposed to do with that?

**[00:16:33]** So, from that perspective, one can say it was complicated.

**[00:16:35]** And when you said it's something you need to get used to,

**[00:16:38]** I would also say, Notion is not complicated,

**[00:16:39]** Notion is something you need to get used to.

**[00:16:41]** Once I got used to it, you can trust it with things, you can ask it for things.

**[00:16:49]** I claim, God knows, that I haven't figured everything out yet.

**[00:16:52]** But even when I imported these notes, it was totally fascinating.

**[00:16:56]** Then I had six hundred thousand trained entries after a while, because the notes were anything but cool.

**[00:17:02]** And then I said to it, look, please make this for me in the database.

**[00:17:05]** Just do it, make it happen, no idea what, then it was back and at some point it has a database with a bit of tagging on it, it opens the original note in the database.

**[00:17:16]** That's magic.

**[00:17:19]** This is truly a magical moment, and I had mentioned it to you recently and shared it on LinkedIn.

**[00:17:25]** So if Apple ever decided to go on a Popping Tour, honestly, no matter who from Apple is listening, buy the store.

**[00:17:32]** It makes such rounds around all the other stuff.

**[00:17:36]** Although sometimes there are things that I see Apple Caster break afterwards.

**[00:17:40]** Siri could do more back then before he bought the music.

**[00:17:44]** One must not forget either.

**[00:17:46]** This Ivan Sauer is an extremely precise person.

**[00:17:50]** He's a guy who's a bit shy,

**[00:17:53]** he's not like Steve or anything.

**[00:17:55]** He knew exactly what he wanted.

**[00:17:58]** These founding stories are really interesting.

**[00:18:00]** Interesting because he had this initial notion as some sort of cloud-lotids-thingamajig

**[00:18:05]** then somehow thought he built that, it wasn't successful and it didn't work out at first

**[00:18:09]** and then he went to Kyoto with his buddy, he is South Korean,

**[00:18:13]** but he still went to Kyoto, Japan, and they locked themselves in for eight weeks

**[00:18:16]** he is also a developer and they just worked on this vision

**[00:18:22]** and the core idea of Notion is that it's all based on Lego blocks, so

**[00:18:26]** that means a database entry, a row in Excel is actually a page and they

**[00:18:35]** internally call the database not a database, but a collection.

**[00:18:39]** It’s a collection of pages.

**[00:18:42]** That means you have a hundred rows, those are the pages and the database itself

**[00:18:47]** in collections.

**[00:18:48]** And that you have fields there, like in a database, so columns in

**[00:18:52]** Excel terms.

**[00:18:53]** That is obviously necessary and clear, but you can also address an element on a page and you can mark an element and say copy, go somewhere else and say paste and then it asks you if it should sync and then it syncs it and it basically does like this.

**[00:19:13]** So then it iframes this element somewhere and now just imagine you have templates and you have a central place, then you build these foundations somewhere, pack them into the templates, when you use the templates, it syncs them there.

**[00:19:29]** But if you change something in the foundation, it goes through all instances. That’s totally crazy and that’s why AI is so incredible right now, because you have like an Inception thing.

**[00:19:40]** You can link a prompt, with a prompt, with a prompt, with a prompt if you need to.

**[00:19:46]** And that is the basic principle of this, they call it Building Blocks, so everything is a block.

**[00:19:52]** Everything is a Neoblock.

**[00:19:54]** So just what you did with your iFrame example, I have to honestly admit that.

**[00:19:59]** That’s true.

**[00:20:00]** I saw the menu option and thought, hey, what are you talking about?
 
**[00:20:04]** Do I really need to take another look after the episode?
 
**[00:20:07]** still in that eye-opening AI part, where I have the assistant in the corner, but
 
**[00:20:14]** also in the, excuse me if I probably choose the wrong vocabulary, in the
 
**[00:20:19]** columns, so properties. I try, I try. For example, I say, okay, I
 
**[00:20:23]** have properties here for this database or Sanbello or whatever, and these
 
**[00:20:28]** might not be filled out by hand because I have a text or a multi-select
 
**[00:20:33]** or something like that, but you can also say, tariffs, this property with AI.
 
**[00:20:37]** Yes, I thought that too. Holder Falter, right? So how crazy is it that I'm putting in
 
**[00:20:42]** the database? So my Excel cells are set and certain fields just get filled out,
 
**[00:20:49]** because there’s enough data available and I told it to do it with an AI rule.

**[00:20:54]** Customs and then you stand there and think, okay, he just assigned me categories.

**[00:20:59]** and derived from what they wrote earlier.

**[00:21:02]** He has no idea what's going on.

**[00:21:04]** And then you can even go ahead and say,

**[00:21:07]** I'm adding views on top of that and then I always have a diagram.

**[00:21:10]** and then I have a table again and then I have the table with a filter.

**[00:21:14]** And you stand in front of it with your mouth open and think,

**[00:21:18]** how much work would that have cost me alone with traditional office tools. 

**[00:21:24]** For example, I am a proponent of Keynote.

**[00:21:27]** Yes, I think we are probably different on that now.

**[00:21:29]** as far as I remember, you're not really into the keynote app, into the app.

**[00:21:35]** I'm back now, I eventually went on Google because we do so much in the

**[00:21:38]** team at the company. And it's true, everyone who comes from design or from Apple

**[00:21:42]** hates me for it. All the people who are new and think we're the

**[00:21:47]** coolest Apple company. And then realize that we work on Google Presentations. We

**[00:21:51]** get this. So I totally understand that. But when you collaborate

**[00:21:55]** this way, it's just unmatched for you.

**[00:21:59]** I know the problem with us, it's PowerPoint, you're standing there.

**[00:22:02]** We're basically the little Gallic village, everything we present, we do with Keynote.

**[00:22:08]** And everything that has to be distributed in a corporate-compatible way, we use PowerPoint.

**[00:22:13]** Greetings to everyone at the company who knows me, but you know,

**[00:22:17]** you also feel what you're getting into with us. But still, even there,

**[00:22:21]** whether you actually wanted to get out. Keynote is also more powerful than one might suspect at first glance,

**[00:22:29]** maybe not necessarily in the exchange and I don’t know, connecting to data sources and

**[00:22:34]** whatever, but if you wanted to quickly create nice presentations, it felt like

**[00:22:39]** nothing could compete with Keynote. It even felt easier in Keynote with your

**[00:22:43]** fingers than, for example, with PowerPoint, considering the level of handling,

**[00:22:48]** I mean PowerPoint, every time I use it I feel fear and dread when I finally have to use PowerPoint.

**[00:22:53]** has to be touched.

**[00:22:54]** Recently I showed you on the Windows computer, what to present.

**[00:22:57]** I was already asked by colleagues if I'm really going to drop such a dusty thing.

**[00:23:01]** Touch Windows computers.

**[00:23:02]** I briefly thought about whether I should definitely wear gloves.

**[00:23:05]** But a completely different topic.

**[00:23:06]** And I think that's also a point with Notion.

**[00:23:09]** It appears so unassuming and yet is extremely powerful.

**[00:23:15]** What are you all doing with Notion?

**[00:23:17]** So, you can say something about that.

**[00:23:19]** Maybe it's also good to mention where it might get stuck.

**[00:23:24]** I would say there are certain things that might be worth looking into.

**[00:23:27]** Yes.

**[00:23:28]** So first I started, back then we had some financial stuff in,

**[00:23:35]** what is it called on Google, not Excel, but Sheets or something, Google Sheets

**[00:23:42]** and in Google, in the Google Word, in the Docs, exactly.

**[00:23:46]** And I had built a few things there because my former colleague wanted something for financial planning and so on there.

**[00:23:53]** We didn't put much effort into it, I just built something, didn't want to use any software.

**[00:23:57]** But exactly that kept growing and when I realized, okay, I can do everything in Google, but somehow it feels strange with all these errors.

**[00:24:06]** I then accidentally got Notion on the table and then I fiddled around in it and built something.

**[00:24:12]** So, the beginning was actually a sort of liquidity planning, when to write

**[00:24:18]** which invoices, paying world and then relatively a lot of stuff came along, which

**[00:24:26]** so it has to do with data storage or you simply need a database and then you can

**[00:24:30]** just say, I want a database and the following fields should be there and the

**[00:24:33]** people should have access and it should be like this and that, and then it works, and

**[00:24:37]** then, but this is the core today, at some point the question was how do we actually solve

**[00:24:42]** our capacity planning in the future.

**[00:24:46]** Capacity planning at Nagentour involves many clients, many projects, many

**[00:24:52]** Working with employees, changing structures, and so on, is not quite simple, that's

**[00:24:56]** from an IT perspective, it's not an easy thing, you can find some

**[00:25:03]** simple solutions online regarding marketing, but when you really

**[00:25:07]** mean it seriously, it's not trivial. So we started for about

**[00:25:13]** half a year doing it ourselves first, then with a colleague together,

**[00:25:17]** then with others testing together and so on, and at some point I

**[00:25:21]** built the version that we introduced about a year and a half ago, a bit more than a year and a half

**[00:25:25]** ago, and that is a typical customer project ticket system,

**[00:25:32]** time tracking, which mainly organizes the work. And that's relatively substantial. I believe,

**[00:25:38]** there isn't a major reinstallation, but the situation exists. And that is the

**[00:25:46]** second part of the question, which also includes the downtime. Notion is great for data, for meetings,

**[00:25:52]** in AI now and so on, but Notion is not as good in the areas where Excel is just really good,

**[00:25:56]** namely, I have twelve months and thousands of data points and I want

**[00:26:01]** to connect that with some formulas and so on. If you want to build that in Notion,

**[00:26:05]** then you have to create relationships to itself and really strange rollups and very

**[00:26:11]** odd calculations, and until about half a year ago, Notion had become so slow,

**[00:26:15]** that my people said, I can’t work with this anymore, then Notion did the

**[00:26:20]** Summer of Excellence and invested all their developer skills only in performance

**[00:26:25]** and none in anything else. And the performance investment really paid off. Now everything

**[00:26:31]** is fast or fast enough. But that is so, well you can, you can

**[00:26:36]** do everything with it. I've solved every problem we had with it, but it's just

**[00:26:40]** at this point a bit like you’re still pulling a hose out of the machine

**[00:26:45]** through the window, back in through the sunroof and out the back.

**[00:26:49]** dying and flashing. You get that feeling with, with certain things, with Norschen.

**[00:26:53]** But I mean, not everyone deals with such Excel wallpaper every day.

**[00:26:59]** Yes, I mean, of course you find certain edge cases where you say, okay,

**[00:27:05]** there is no idea, Excel was always better or faster to the goal or whatever,

**[00:27:14]** but what I find so nice about Notion is that it is just so omnipresent for me in so

**[00:27:21]** many things. I mean, I don't have such capacities, like workforce planning or so

**[00:27:25]** on. As I said, I basically only use it privately to evaluate things and structure my

**[00:27:32]** stuff. For example, I gave a shout-out to Leo Becker,

**[00:27:37]** a hot publisher. I think I'm back in that podcast the day after tomorrow. Where

**[00:27:41]** we would talk about the Apple Vision Pro? I also showed him how you could

**[00:27:45]** suggest show notes like that. What topics do you have? You can

**[00:27:49]** send the agents out to scan the website for news. So no

**[00:27:54]** 2.5 Mac and the decoders and I don't know what else, so that you put that into a database. 

**[00:27:59]** You can ask him to pull out what's still left, you can ask him to

**[00:28:02]** summarize coherent things that are grouped by the same AI-generated categories.

**[00:28:08]** You can then ask him to create straight-up lists from that, what do you actually want maybe in

**[00:28:13]** discussing your podcast, that's already fascinating, or another topic is,

**[00:28:18]** that I said, here we always research the following stuff and then I had

**[00:28:22]** made more tables and that kind of stuff from it, again there is a distance applied on it.

**[00:28:26]** And what I totally love about Notion is that it's not a closed system, it's open.

**[00:28:30]** So you can integrate other things and you can integrate Notion itself.

**[00:28:35]** So maybe we can spend another two or three sentences on that.

**[00:28:38]** For example, I went ahead and really like using OpenAI in its original form, so in the

**[00:28:44]** vanilla edition, let's say, when we wanted to mess around a bit with Android, no worries,

**[00:28:49]** you won't get more Android quotes, that's not coming. And Manus. Both OpenAI and Manus

**[00:28:56]** allow me to say, hey, pass, I connect Notion. And then I can

**[00:29:00]** go ahead and say, hey, pass, I'm doing my research with Manus

**[00:29:04]** and stuff, and then at the end, when everything is done, I say, now please make me

**[00:29:08]** a table in the place of Schnickschnack-Schnuck and please put the entries that

**[00:29:13]** you found directly into Notion. Then you either have a

**[00:29:17]** table in Notion that gets expanded because it's already there, or a table that gets created.

**[00:29:21]** And I think that's also cool, I mean sure, you could say export as CSV or import

**[00:29:27]** that CSV for me, or you just say it’s there. And if you then use something like Manus and say,

**[00:29:32]** you turn that into a daily work assignment. I also let Manus scan various

**[00:29:37]** internet sources and then automatically fill these tables, and then you have

**[00:29:42]** when you open your Notion in the morning, always a fresh table with current news,

**[00:29:48]** with AI-generated keywords and formatting, and even a reminder, or then also think, okay,

**[00:29:54]** that's definitely also a game-changer for research and filing and linking to AI systems

**[00:30:02]** with me. Absolutely. But what I want to add is, I'll get to AI shortly. I

**[00:30:07]** just wanted to say, this accent system has, so first data, then finances,

**[00:30:13]** then all kinds of data, knowledge, blah, blah, blah, and then really the heart, so

**[00:30:19]** how do you organize yourself?

**[00:30:20]** So the ticket system.

**[00:30:21]** Yes, yes.

**[00:30:22]** The ticket system creates the following number.

**[00:30:25]** How much do I, as a person working in this company, have to calculate this week?

**[00:30:32]** Does it add up or not? Including my part-time hours, including my vacation,

**[00:30:38]** including my sickness, and including all the things I need to do, I somehow

**[00:30:41]** reach these 5 days if I work 5 days. So, that's not trivial, because if I have

**[00:30:47]** this number reliably, and we now have it reliably across the year, over

**[00:30:50]** one and a half years, then I can orient myself by that. The team leader can look at it,

**[00:30:54]** anyone can look at it. That's incredible, and it's represented in such a timeline.

**[00:30:57]** So, now pay attention. Then this damn AI comes along. And now you can tell this

**[00:31:02]** thing, I made such a master prompt where I explain everything, how everything works,

**[00:31:07]** what is meant by what and where. And now I can talk to the AI. How much time, who could

**[00:31:12]** be the next one? Who could work on this? Which team still has capacity? This is

**[00:31:18]** not perfect yet. This is in the beginning. But now I can seriously talk to an artificial

**[00:31:23]** intelligence about capacity planning. I can talk about when we can start the

**[00:31:29]** next project in the web area? When can we start the next project in the social

**[00:31:33]** media area and in the video area? This is not perfect, but all of this is

**[00:31:37]** now available. And that drives me crazy because I think, oh my God, what does

**[00:31:42]** this mean? I can suddenly talk to a 24/7 entity that is never tired, always smart, and

**[00:31:50]** discuss topics that are truly important, those which are really at the core of the company.

**[00:31:55]** And that makes it so crazy, and it really has the context of what it's about in a

**[00:32:01]** company like ours, namely who works when, on what, with how much, how much

**[00:32:06]** money do we get for it, how much have we already worked on it.

**[00:32:09]** I can ask where things are going poorly, where things are going well, and I have all the time

**[00:32:13]** real, important data for that.

**[00:32:16]** I already regret having made that jump to sugar I system, because while you were talking, I was thinking,

**[00:32:24]** I can only tell you from my work environment how long people might be busy,

**[00:32:30]** figuring out things that should perhaps be a matter of course,

**[00:32:35]** if they weren't dealing with the topic to answer such simple questions,

**[00:32:39]** like, what’s going well, what isn’t, when will we have time for something again?

**[00:32:42]** Also greetings to my team, yes, where I think the agency business could also be imagined partially spontaneously, I don’t know, so when

**[00:32:52]** clients like us come around the corner and say, we need this really quickly and urgently and please here and please differently and no idea what,

**[00:32:58]** at least with us internally, things come up sometimes, because I don’t know, marketing has come around or there’s a product launch or

**[00:33:04]** a regulatory requirement needs to be set and what does know everything, yes,

**[00:33:08]** I don’t want to make it worse or more serious than it is.

**[00:33:14]** But what you just said, when you said, I can chat with the thing

**[00:33:18]** and I have expertise about project states, about workforce status, about…

**[00:33:26]** What did I discuss with the client last time?

**[00:33:29]** It even has this meeting function, I believe, I’m not sure,

**[00:33:33]** just for that meeting recording?

**[00:33:35]** I want to interject here, the meeting recording is almost the killer feature for us,

**[00:33:41]** so that was the moment when most PMs said, all right, we want everything

**[00:33:46]** with the AI, because not only is it recorded and then there’s the summary,

**[00:33:50]** but as I said, with us it’s called tickets and I have built a prompt

**[00:33:54]** with which you can extract these to-dos from this recording, just like the thing itself does already,

**[00:34:00]** but in that case the AI does it automatically, if you want it,

**[00:34:07]** in the meeting project, the to-dos for the right people, if you add a little

**[00:34:13]** for a long time, so to speak. And this is how it goes. The meeting is over and the PM is sitting

**[00:34:17]** there, clicks on the little man in the bottom right and says, generate tickets, add,

**[00:34:23]** AI, Ticketmaker, Enter, goes for a coffee, comes back, has suggested everything, gets

**[00:34:30]** maybe I always do it with a checklist and approval, then you say Go, all the

**[00:34:36]** things are there, the tickets are booked with the capacity assigned to the people, in the right project,

**[00:34:44]** it's unbelievable.

**[00:34:45]** I mean, I don't know how many of the listeners can relate to this now, but I

**[00:34:54]** would put it down next and a lot of new ideas that arise from it, just

**[00:34:58]** from this conversation now again.

**[00:34:59]** I am also very happy that we could meet here for this crossover show

**[00:35:03]** because so far we have always been sending voice messages from the car

**[00:35:06]** or so, if you've invested more, have you tried that, look here, there are hardly any

**[00:35:09]** like this and that and in general, I have no idea, and it's all really nice.

**[00:35:12]** But what you're describing should actually, I mean, what one doesn't understand,

**[00:35:20]** why are there so few knowledgeable people?

**[00:35:23]** So, regardless of whether there might be other cool tools, I'm wondering,

**[00:35:29]** at what point should Notion also ramp up a bit to become more well-known

**[00:35:35]**?

**[00:35:36]** Because the problem you're describing, I don't want to step on your toes, but that

**[00:35:40]** is something many people have.

**[00:35:41]** And I would like to say that I also find myself in a situation where I say,

**[00:35:45]** I would be very grateful if I could ask better questions ad hoc to get answers.

**[00:35:51]** Alone, not even the capacity planning and such stuff. But of course that too.

**[00:35:55]** Yes, all from that side.

**[00:35:57]** I can give you another example, which I also find very fascinating.

**[00:36:00]** Namely, we talked in a team leader meeting at some point, and the team leaders

**[00:36:05]** with us from the agency management and we brainstormed ideas.

**[00:36:10]** And they said it would be nice if we had monitors where, yes, if the

**[00:36:14]** The company would know what the company was, where all the possible things that happen are

**[00:36:17]** in the company. And I said, well, guys, you are hybrid. So you are

**[00:36:21]** at most in the company half the time, if it goes well. So, if that's the case,

**[00:36:24]** it has to be on a digital platform as well. Yes, okay. So, can you do

**[00:36:28]** anything there? Then this Motion 3.0 with the AI came out and my

**[00:36:32]** the prompt for this is kaibinde strich whatsapp so what's up whatsapp and thank you yes I say that

**[00:36:41]** because there was a great advertising slogan earlier that doesn't matter so listen up and it looks for

**[00:36:47]** through all connected tools including Slack, Drive, documents, comments, and so on for

**[00:36:56]** interesting, funny, I have illustrated this with examples and so on, topics and I'm doing

**[00:37:02]** just one example. Started in the PM team Welcome back to the North. That's the assignment,

**[00:37:09]** the goal is always it can only be one sentence and it has to result in a small card that

**[00:37:14]** then runs down on the dashboard of the employees on the right. Or after various

**[00:37:20]** rounds of negotiations, the written order from the Insert-customer's name. We have won the

**[00:37:25]** pitch. All this information, funny information, what someone commented

**[00:37:29]** in Slack, so for you in Teams like chat or whatever. All this stuff is now

**[00:37:35]** just coming in, like a social network. They just come in like that,

**[00:37:41]** this is done by this AI. And so far I'm still having my colleagues from the office curate it,

**[00:37:46]** so that there isn't somehow, you know, a funeral or something coming up in between.

**[00:37:50]** Yes, it's absolutely insane what you suddenly get up and where people suddenly see

**[00:37:55]** can see what all is going on, because you don't get that anymore if you're not in the

**[00:38:00]** office every single day.

**[00:38:02]** That's right.

**[00:38:03]** Yes.

**[00:38:04]** Well, I also really like being in the office not just because I want to see my colleagues while

**[00:38:08]** they’re working, but also because you definitely want to pick up on things that are happening,

**[00:38:12]** which is certainly good, as well as bad, but of course also,

**[00:38:17]** things that happen in other projects, and also this moment, whether you like it, that you're there,

**[00:38:23]** let's just discuss a topic right now. But what you're describing is probably,

**[00:38:28]** no matter how powerful this already is, it's still just the beginning of what is possible.

**[00:38:34]** If I think about it, they announced something like this too, if I remember correctly,

**[00:38:38]** that in the future you can also start agendas automatically based on time somehow,

**[00:38:42]** I don't think that is there yet. Or I couldn't find it and you're going to tell me now,

**[00:38:46]** if you had just clicked on this menu function, you would have been there.

**[00:38:49]** Let me put it this way, did they officially announce that there are agents?

**[00:38:53]** I mean, I took it as there being sender-receiver problems.

**[00:38:59]** In chemistry, I think of a tactile representation where roles were assigned

**[00:39:06]** and they said it was triggered by some mechanism, and I was already thinking,

**[00:39:09]** damn it, if they start and also initiate themselves and

**[00:39:13]** maybe can trigger each other, then you are indeed in such an agentic

**[00:39:19]** System, because prompts then pursue a goal and can thereby trigger other prompts.

**[00:39:25]** And then, I think it will be again... Wow! It's like this, if you are a Notion nerd like me,

**[00:39:33]** then you can apply for a program called Notion Ambassador. And there are
 
**[00:39:40]** various things you have to do. I don't know, it's not that hard, but they are looking

**[00:39:45]** for people who can sort of multiply, and I've been in it
 
**[00:39:49]** for about a year or so, and we just got the test version yesterday and I am allowed

**[00:39:56]** saying that because they actually mentioned it in the keynote. And I have

**[00:40:01]** now built two agents, the one, the WhatsApp agent, that I just mentioned.

**[00:40:05]** This is actually the one that just looks at 7:15 AM and creates these

**[00:40:12]** cards, as I call them, so this news.

**[00:40:14]** I am now officially envious.

**[00:40:17]** Oh, already. You’ve already been to the WWDCs of this world and have total connections to Apple.

**[00:40:23]** I’ve always been jealous of that, I really have.

**[00:40:26]** Yeah, okay. Let's just leave that hanging in the air. So from that angle, you're giving me the signal,

**[00:40:31]** that the wait is worth it, there could still be cool things coming that we've basically heard from the Profitation

**[00:40:36]** announcements. So it's worth mentioning briefly that these agents each

**[00:40:44]** have their own access rights. That means you can tell them, okay,

**[00:40:50]** I'm giving you access to blah, blah, blah, you have access rights to the database,

**[00:40:54]** you can’t really imagine that, it’s just a fucking user trilium this

**[00:40:59]** word choice needs to be cut out. So I'll start again. I’ll just write down explicitly.

**[00:41:04]** Hello? Okay. This is not for under 18. It’s just a user. My agent is called

**[00:41:12]** Mood, so atmosphere. And I say, search in all internal sources like emails, meetings

**[00:41:17]** tickets, and so on, Slack for comments, filter them by good or bad mood.

**[00:41:21]** Everything in between is irrelevant to me, research thoroughly, blah, blah, blah. And then I get
 
**[00:41:25]** to use the method I want, as often as I want with the train. And the access rights
 
**[00:41:31]** I can manage for any database in any thing, how the access rights work, to
 
**[00:41:36]** give this thing. That's really crazy. This thing can be a member of a group.
 
**[00:41:40]** So, that the people at Notion have through this block structure, what I mentioned at the beginning
 
**[00:41:45]** said, because it’s sort of like this, yes, each element has its,
 
**[00:41:51]** I’ll just call it an entity, can be referenced, is somehow through that,
 
**[00:41:57]** they simply have such a powerful foundational idea, which is now in the career...
 
**[00:42:02]** A good basis.
 
**[00:42:03]** An extremely good basis, yes.
 
**[00:42:05]** Back then, they probably thought, oh, somehow cool idea, but couldn’t foresee

**[00:42:09]** can understand what it actually means, and I think that is also a decisive

**[00:42:14]** advantage, why maybe these other big players in the market are struggling, when

**[00:42:19]** you look at it alone, Karl Klammer, sorry, Microsoft Co-Pilot, they are not that far apart.

**[00:42:27]** This is my personal opinion, not an official statement, it is simply very affected

**[00:42:33]** in the way it works and then also how it works. So if I look at that,

**[00:42:36]** Ding says, fill out an Excel sheet for me, then I'll be happy with people now,

**[00:42:39]** that I can write Co-Pilot soon, is missed. But just these stories alone,

**[00:42:45]** Rewrite this for me, write me a text, use this style for the text and what you just pulled out of his magic box, that is unthinkable with today's architecture.

**[00:42:56]** And from that perspective, I believe that nauschen has really laid a very, very good foundation at this point.

**[00:43:01]** If you don't somehow add the finishing touch to the icing, I would briefly like to address the obviously external AI tools anyway.

**[00:43:08]** I'd like to mention one more thing for all those who are now dealing with AI but might still be at the beginning, because we've already delved a bit deeper into Notions.

**[00:43:18]** I think if you forget everything we've said so far and just say, okay, obviously this whole thing with AI and the internet isn't going away, it's something I have to deal with now.

**[00:43:31]** Then just do a free Notion experiment, do a couple of tutorials and play around with it, and

**[00:43:38]** don't think in this world of these old men talking here, rather this is

**[00:43:42]** simply a new world.

**[00:43:43]** It's all over.

**[00:43:44]** You don't even have to be happy anymore that you don't have to do everything by hand.

**[00:43:48]** you have to in Excel.

**[00:43:49]** You don't have to be happy about it, what are columns and rows again?
 
**[00:43:52]** and it's just over.

**[00:43:54]** You can just write in this window and you will most likely
 
**[00:43:58]** from our perspective get an extremely good response, 80 to 90 percent, 80 percent. If you play around with the

**[00:44:03]** If you chat about things, it gets even better. And in Norschen you can buy one, you can in an,

**[00:44:09]** in an app store purchase prompts? You can buy prompts. You can also get them for free.

**[00:44:16]** But there is one prompt I absolutely want to mention from Simon.

**[00:44:19]** Please go ahead.

**[00:44:20]** This is this, this, this prompt that I also recommended to you, it's called Simon with S-A-I because A-I-Men and this prompt costs 79 euros and anyone who has 79 euros available should invest these 79 euros, it’s unbearable what is possible with it and with that you get a jumpstart, oh you, you overtaking then 20,000 cars in the left lane at 300 and you're just at the point where one can be today. I wanted to mention that again.

**[00:44:49]** So it’s not just for nerds, but you can download the Norschel.

**[00:44:53]** If you want to do AI, you download this Simon thing and you’re good to go.

**[00:44:58]** So maybe, this is indeed something to, again, from me once more

**[00:45:03]** the statement, also this topic with Notion, to engage with topics,

**[00:45:08]** that you might otherwise have to laboriously formulate in other KAE systems,

**[00:45:12]** you can also quickly first prompt in Notion.

**[00:45:15]** Yes, for example, I also have things and with that I am now

**[00:45:18]** I see a segue to something like N8n.

**[00:45:21]** I’m trying things out in Notion and then with the knowledge of how well prompts work together,

**[00:45:27]** what data I need to perfect it through N8n, because I also

**[00:45:32]** don't have the new agents and stuff like that, so I might say, okay, how should

**[00:45:36]** I write my prompt to, for example, extract this and that from a text,

**[00:45:40]** do this and that, and I don't know what.

**[00:45:43]** And then I go ahead and build the work slug step by step, and the cool thing about Notion is that you can even use the webhook feature,

**[00:45:53]** thanks to you, you also provided me with an audio track, because somewhere in the workbook you can rate it, just let me know, I’ll give it five stars.

**[00:46:01]** So you can say, okay, actions on this database, if something happens, the following trigger will trigger the following actions, and for example, I also built a database where you enter text at the front, and at the back is a status field, the status is set to TWD, and when I set it to ‘in processing’, it triggers a webhook that calls an N8n workflow. The N8n workflow is an agent-based workflow system, open source, a Berlin startup.

**[00:46:31]** Highly rated, very interesting, I’ve already talked about this in my episode.

**[00:46:36]** It takes the entries and sends them to

**[00:46:40]** Gamma, which is an AI with which you can create slides.

**[00:46:44]** It takes all that stuff, generates the slides, and when the slides are ready,

**[00:46:50]** it sends them back as a link, as a data link in Notion, and so I’ve constructed a

**[00:46:58]** delegation time table based on this idea.

**[00:47:00]** Depending on what type of tech I assign, slides will be generated, infographics

**[00:47:05]** will be generated, texts will be written in the voice of a different persona, or even audio files.

**[00:47:13]** And that’s also amazing when you think about it, you write things in there, whether by hand,

**[00:47:18]** through AI, through the source, whatever, and then it starts

**[00:47:23]** and integrates so well into this AI world that you can also retrofit functionalities that might

**[00:47:28]** count in notebook ratings, through N8n, through make.com, through zapier.com,

**[00:47:35]** whatever all that stuff is called. And then suddenly also, I’d say, I don’t know,

**[00:47:41]** Playing out content on lead-in, playing out content on, I don't know, what to automate with it

**[00:47:47]** can be done with a quality and standard. That hits me every time, it feels like, that disappears in the listening,

**[00:47:54]** When I then see, I enter something, drink the coffee, come back and in the

**[00:47:59]** table there is a task completed and here are, by the way, the files you wanted.

**[00:48:04]** That is, I would also say, no matter how good it is after the ending, coh is, at

**[00:48:10]** the integration possibilities into other tools, that is amazing.

**[00:48:14]** Yes, I mentioned at the beginning when I started with Norschen

**[00:48:18]** that, of course, Norschen had no automation, had no AI, had

**[00:48:22]** none of that.

**[00:48:23]** We relied on a scripting tool from some world, and I used Make because it seemed somehow good and massive and great, and I believe it's also from Europe.

**[00:48:35]** Chase over Kai or no, that's not what it's called anymore, some Czech thing, and it's all cool, well, and with that I simply have no idea, I think we spend 3,000 euros a year for licenses, for Make or for, so we do relatively a lot with it, with the database connection, Personio connection.

**[00:48:53]** Old memories are coming up with the first employer, which had a lot to do with Datav.

**[00:48:58]** We used Datav as an accounting system, and that's why we had to connect it,

**[00:49:03]** all our things. I did that as flour or we did.

**[00:49:05]** Then I discovered N8N and then I realized,

**[00:49:09]** it was the first tool that made the whole Kali thing a bit more loved.

**[00:49:15]** And this agent that finds out on its own, this central tool,

**[00:49:19]** that finds out on its own, I do this with that, I do this with that, I do this with that.

**[00:49:22]** So you could work in an agent-like way, and then somehow I had no idea like our email inbox when inquiries come or incoming invoices.

**[00:49:31]** This whole triage to find out who what this is supposed to be and so I built, and I'm still a huge fan, then I first realized it's from Berlin, which I found even better.

**[00:49:43]** And overall, I think the guys are cool and how everything is, and that they have a very nice Notion integration and so on.

**[00:49:50]** Well, and now, I have to say fairly, that since Notion has progressed so much,

**[00:49:54]** I naturally need it less and less, as it's increasingly all going into Notion alone.

**[00:49:59]** I went out earlier to use an important AI.

**[00:50:03]** Meanwhile, I have Notion Gemini, I have Claude, and I have GPD in the respective

**[00:50:09]** latest version.

**[00:50:10]** On the day GPD 5 was released, six hours earlier, because in Europe, Notion GPD 5 was available

**[00:50:17]** So, six hours earlier. That means they are no longer offset, but it’s clear that Chat GPT 5 has

**[00:50:25]** image processing blah blah blah, somehow in the regular version it can do more, but still.

**[00:50:30]** It’s a bit like this, that I still use it every night, every day, to do something

**[00:50:36]** or it wears out and I have to maintain it every day so that it runs somehow and is connected. So I find exactly this thing that you say,

**[00:50:45]** that Notion is such an open system and wants to position itself in the middle and would rather integrate more people and

**[00:50:53]** systems than protect its business model. I still think that is wise

**[00:50:59]** clever. So they are open to everything. They are open to Microsoft, they are open to the

**[00:51:05]** the whole GitHub, Bitbucket and whatever it’s all called. They are open to all the tools and

**[00:51:10]** systems and that's exactly what makes it easy.

**[00:51:14]** I mean, that was like with my side project or the note, yes chosen after the

**[00:51:20]** word, you have the agentic in Notion, do you need less N8n for that reason?

**[00:51:25]** Nevertheless, I find this power that lies in open source, open standards,

**[00:51:31]** Integration capability and also the simplicity of doing things are impressive, whether I'm now

**[00:51:37]** She says, everything I have cobbled together in the evenings is also so easy to

**[00:51:42]** keep in notes, especially since I also want to accommodate a bit of the world around me, I know

**[00:51:46]** not me, it will show up later.

**[00:51:47]** This is definitely an exciting construct.

**[00:51:49]** And since yesterday, we also have this Workslow-images at the night ends, that you can per

**[00:51:54]** You can build entire workflows where I also had a little

**[00:51:58]** lack of sleep yesterday evening because I was trying to optimize the workflows I own,

**[00:52:03]** or create new workflows, I'll explain it myself.

**[00:52:07]** I didn't see that.

**[00:52:10]** Normally, you start in that thing by saying, I set a note, what triggers my event,

**[00:52:21]** create my processes, I would define the variables with notes, make the internet calls, control the agents with LLM models.

**[00:52:29]** and you have to kind of click together the process logic yourself by connecting the notes.

**[00:52:36]** and then you can tick off a more or less large workflows for yourself.

**[00:52:42]** And I believe it was yesterday, or at least I saw yesterday that they released a beta version in the

**[00:52:47]** cloud version with a workflow builder, meaning you now get

**[00:52:53]** when you open a workflow, no longer the classic little plus sign,

**[00:52:58]** to select a note, but to build a workflow supported by AI.

**[00:53:03]** And then you chat with the workflow and you write in what you would like.

**[00:53:07]** I told the thing that when we follow on LinkedIn, it knows that I have an advisory board

**[00:53:12]** I put together, like 20 notable people, which I have stored as persona prompts,

**[00:53:18]** who are invited to a discussion on a topic that I present to the

**[00:53:24]** board, the consultant chooses whom he will discuss with, discusses with the

**[00:53:30]** relevant rules for the discussion between the prompts and gives me the result.

**[00:53:35]** So I asked that as a question to the workshop facilitator.

**[00:53:40]** I told him, you wait, I now have 20 prompts, I need placeholders for that.

**[00:53:44]** I have a web interface, so that the nrnd provides.

**[00:53:49]** I want to make a sub-blog for supporting types, I want there to be a consultant,

**[00:53:54]** who checks which of my prompts are the best for that, who then verifies,

**[00:53:59]** with what methodology can I achieve a good result, so applying moderation techniques,
 
**[00:54:05]** that you summarize. I initially had it at 1600 characters, but that was too
 
**[00:54:09]** long, I then had to shorten it to 1000, pressed enter, and then it started,
 
**[00:54:12]** it built. And what it built worked. It's not like you then
 
**[00:54:17]** suddenly have a box with a question mark, like when you look at your N8n workflow

**[00:54:22]** not with ZTT or from Hoppig nonsense constructs, but it was a fully functional workflow,

**[00:54:29]** that you could also continue working with. Well, it's beta, sometimes the workflow would

**[00:54:34]** fail on me, then I had to get used to saving on time. But they have now

**[00:54:40]** practically elevated this whole Citizen Developer and anyone can build workflows idea to a

**[00:54:44]** simplification because you can now work with this tool in beta. They said,

**[00:54:50]** it will only be available in the cloud for now, but I have my worst workflows that I had at

**[00:54:55]** I basically have. Glimm, because they are big, because they also there, learning by doing, I haven't

**[00:55:00]** read 50,000 courses, I also try them out. My worst workflows were rebuilt within 8

**[00:55:06]** minutes. With CELAS-Hellenabfangen, so I would say in a better quality than

**[00:55:12]** my old workflows. Also that they set some kind of note, and at this point is

**[00:55:17]** is now JavaScript code and there was JavaScript code in this note and he then helped himself there

**[00:55:22]** with things that he, let's say, couldn't achieve with the classic notes

**[00:55:26]** because it also wasn't, but all custom notes came, so custom notes are notes

**[00:55:31]** from the community for connecting to, I don't know what, whether there are also devils there,

**[00:55:34]** because they don't, I have to look.

**[00:55:35]** Mhm.

**[00:55:36]** But it was so impressive that I tell the thing, you know, I have the following

**[00:55:39]** Problem, create a workflow for me and you hit play and it runs.

**[00:55:43]** Yes, you think to yourself, hold on, hold on, that's quite a statement about something,

**[00:55:50]** that started as Open Source, that comes from Germany, that integrates so well into

**[00:55:55]** Notion. One must be fair, it integrates really well with many other things too.

**[00:55:58]** And for me, it really is the second tool in this trio, yes, the first is

**[00:56:05]** Manus.

**[00:56:06]** Manus is really amazing for internet research, the second is

**[00:56:09]** then Notion and the third is then End to End.

**[00:56:11]** It's really a wonder, it feels magical.

**[00:56:15]** Yes, so if you're a developer or have studied all this and do it every day,

**[00:56:24]** then connecting data sources, linking data sources, is everyday work, and it costs somehow PT,

**[00:56:31]** like person days or headaches or whatever, then you can do that.

**[00:56:34]** But then when you suddenly get to know Make or later End to End and realize,

**[00:56:39]** Okay, someone is solving the problem of connecting these data sources with one central hub and the other data source too.

**[00:56:49]** And now I just have to be smart, but not too smart and instantiate some objects and I don’t know what else to do.

**[00:56:57]** I basically just have to put it together like an operator used to do with phone connections.

**[00:57:03]** And that means I can focus on the actual problem.

**[00:57:07]** And that's why I find this low-code workflow world so exciting for me, because I'm not a developer by background,

**[00:57:14]** but more a designer or something else, but definitely not a core developer.

**[00:57:19]** But I really want these things to work, so for me this series Make, End to End,

**[00:57:25]** all the AI tools, the whitespace coding and of course Notion fit together perfectly,

**[00:57:30]** because it enables more for someone who understands the things I want to do, enables me to do more of those.

**[00:57:36]** That I'm also somehow within a company, as I said, greetings to, as you say so nicely, to the people who might hear this.

**[00:57:43]** I know you find it annoying that the boss is programming, it's all good, but still, from my perspective, from my role,

**[00:57:55]** this is the best thing that can happen, and about Norschi's vision, that people who have a problem can solve this problem themselves.

**[00:58:01]** So, that’s just a nutrition.

**[00:58:04]** There's so much truth to what you said, people who don't have technological depth cannot create solutions, that was one point.

**[00:58:14]** And now it's increasingly being implemented in more and more different places,

**[00:58:18]** that you don't even have to draw these lines and think about it.

**[00:58:22]** What do I actually need for the solution to my problem, rather I throw,

**[00:58:26]** This is me but magnetically. My desired target understanding in the room, less well

**[00:58:32]** or poorly formulated to note, I just have to chat longer and I get the solutions.

**[00:58:36]** Solutions that, when you started from PT, we’re also talking about person days, meaning

**[00:58:42]** then IBL, internal employees, external employees, you haven't seen? No, external fund outflows

**[00:58:48]** around. Anyway, late hour, right? It’s twenty to ten, it’s not that late, but maybe

**[00:58:53]** that puts this Freudian slip in perspective. But one will also be able to say,

**[00:58:58]** I talk with the stuff, I get a solution, and thus I have to talk longer with the stuff,

**[00:59:04]** until the solution is as I would like it to be. And when I first opened it up at night

**[00:59:09]** I also thought I was reminded a bit of the past,

**[00:59:11]** at first it scared me because I thought, what is this?

**[00:59:14]** Victory tree and then I make a line, where are we? I mean, I see

**[00:59:18]** Sauscode. In Sauscode lies the truth. Also here, greetings

**[00:59:22]** to the developers. The real truth is in the Sauscode, not in the documentation, the Sauscode

**[00:59:26]** knows. And when I saw that, I was reminded of something that’s been

**[00:59:30]** very, very long ago. Yahoo Pipes. Maybe that really had

**[00:59:33]** ever seen. Yahoo, it's been a while. Yahoo. So I can't see. And there was

**[00:59:39]** also the possibility to connect things with pipes. That was a lot more

**[00:59:43]** colorful and everything. It definitely had nothing to do with AI. But then you stand there and

**[00:59:48]** think, you're supposed to create something cool with this.

**[00:59:50]** And now you realize, you're creating cool things with this.

**[00:59:54]** And we basically turned the IT landscape upside down with these two tools.

**[00:59:58]** So when you think about it, I mean, you just talked about Datives,

**[01:00:02]** that's against Datives, of course everything in consulting and accounting is very important and correct.

**[01:00:06]** But I mean, Datives, SAT, and their peers all come from a time,

**[01:00:11]** where large database systems, fixed data flows,

**[01:00:14]** everything is hard-coded, as it is, it is not interpreted and then suddenly you have systems,

**[01:00:20]** that understand you better, that understand your colleagues, employees, friends, acquaintances better,

**[01:00:26]** and enable competent matters, like your deployment planning, like what happened with the customer,

**[01:00:33]** why is this going wrong and maybe there are patterns that keep recurring and that you can simply understand data and connections better.

**[01:00:41]** That's amazing. And because you say, that's not always perfect, well, I would say it like this. I sometimes get surprised too.

**[01:00:48]** There are people who lie to you. There are people who are mistaken and present their lack of knowledge as knowledge because they believe they're right.

**[01:00:55]** With computers, we're not used to it. The computer, you expect the answer to be correct.

**[01:01:00]** It's called hallucinating with computers. And I'm really curious where the journey of these tools and possibilities will go.

**[01:01:07]** And when we finally get a mortal version in this Notion version and what else might come behind it, it's a great time.

**[01:01:17]** It’s a great time, but I still have one, we can cut this later, but I have one point that is, at least for me, relevant.

**[01:01:25]** And namely, I just said for everyone who does something completely different, anything at all, it really doesn't matter what.

**[01:01:32]** For everyone, it will be necessary to deal with AI.

**[01:01:36]** Just as it was necessary for everyone to deal with PCs.

**[01:01:39]** And Apple has liberalized or made the Mac available for everyone.

**[01:01:45]** The Mac is for everyone.

**[01:01:47]** And so I would currently say it’s a case for humanity.

**[01:01:50]** As soon as there are stocks, I will buy all the stocks I can buy.

**[01:01:53]** That’s totally clear.

**[01:01:55]** No financial accounting here?

**[01:01:57]** No, no, we are not providing legal advice.

**[01:01:58]** Financial development, tax consulting, disclaimer, impressum, please visit www.sv.gov. What I want to say

**[01:02:04]** is.

**[01:02:05]** We need to meditate on this again briefly.

**[01:02:08]** Norschen has built this AI in.

**[01:02:11]** We talked a bit about it, but now there is something that I think, if

**[01:02:15]** you are listening now and you are a company, you have a business, you work

**[01:02:20]** in a company, you have some knowledge that you manage, that you know.

**[01:02:25]** You know yourself, you learn, you study, it doesn’t matter what.

**[01:02:29]** Just imagine you put all this into this Norschen for some reason,

**[01:02:33]** just like you do with your notes or something.

**[01:02:35]** And then Norschen said, everything is the same, build in a career.

**[01:02:38]** But then they also said, I will provide you the opportunity,

**[01:02:42]** to set a master prompt.

**[01:02:45]** And now I have written in my master prompt who I am, what I think.

**[01:02:51]** My colleague from the editorial team, who leads the editorial team,

**[01:02:55]** thank you very much, I put together 40 questions, the Prust questionnaire from

**[01:03:01]** FACET and many other questions that I have all answered. Of course, I

**[01:03:05]** spoke, transcribed, summarized, categorized. I have

**[01:03:09]** completely primed my master prompt with me. And when I now say to this

**[01:03:14]** thing, oh, and Norschen has the entire context of my company. And

**[01:03:20]** by the way, also my personal context. When I have renovated my house,

**[01:03:23]** I have organized everything in Norschen of course, and so on.

**[01:03:26]** That means everything I am and can do is contained in it.

**[01:03:30]** My two books that I have written are in there.

**[01:03:32]** Everything is in there.

**[01:03:33]** And when I write something now, it all becomes just like me.

**[01:03:38]** And then people ask me, did you write that with AI or by yourself?

**[01:03:42]** And those are the people I previously told that I wrote it with AI.

**[01:03:48]** I want to say, it's so crazy when you take these prompts,

**[01:03:53]** So when you take the context and the prompt together, when you say to yourself,

**[01:03:57]** okay, I just create the whole context because I just put everything bluntly in there,

**[01:04:02]** just dump every data, my ideas, if I want, what is me, my recipes,

**[01:04:08]** all my recipes are in there. All the recipes I love to cook.

**[01:04:11]** All recipes are in there. And then I have a prompt,

**[01:04:14]** in which I explain who I am, in which I explain how my company works,

**[01:04:17]** what I think about AI, what my position on strategy is, what my position on that is.

**[01:04:21]** And no matter what I ask the AI, I have a little chat window at the bottom right, no matter what I ask it, it will always respond in the context in the way I am.

**[01:04:31]** And you have to imagine this briefly, you don't have to do anything complicated, you don’t have to know how to program, you don't have to understand AI, you just have to understand, I put everything in this Norschen and I put effort into this master prompt and if I don’t want to make an effort, 79€, Simon, buy and goodbye, then I’m done, then I have simply surpassed everyone.

**[01:04:50]** overtaken. Any advice that wants to choose some advice for me. I've overtaken everyone. I'm just

**[01:04:55]** Joch Morch. This is really ever. We don't need to cut anything. It fits perfectly,

**[01:05:01]** because when it comes to our release, we’re used to jumping around in topics.

**[01:05:06]** Greetings to Jens, it’s not just on you, it’s also on all of us. Whether you want to arrange it differently in your

**[01:05:11]** episode, you can think about that. But again, it applies here,

**[01:05:17]** While you're speaking, one realizes what Notion means, when you've used it a bit longer,

**[01:05:27]** because it not only has AI now and can address things cooler, but it also simply has knowledge

**[01:05:36]** and knows relationships and the more it knows, where you use it, the better the results it gives back

**[01:05:45]** And this idea with the Master Prompt, I have the pack and I'm still trying to learn a few things from it because he did that quite cool, also thinking along the lines of, here, his AgentOS, so how do we actually move forward, and how does it actually work, so which functionality of the prompt is now pulled for the question he gets asked?

**[01:06:06]** That's already inspiring, shows, but really, we are facing great times, but the

**[01:06:18]** solution doesn’t automatically mean you have to sign the largest cloud packages of the big manufacturers in

**[01:06:25]** large quantities. I also recently read in a study, that's not really a study in

**[01:06:31]** a report, about how few people supposedly license Co-Pilot.

**[01:06:35]** I mean, I understand that, but it also says something about whether the solution

**[01:06:40]** helps you or not.

**[01:06:41]** And if you see even just a spark of an idea in there that AI could theoretically help

**[01:06:49]** could, is basically this recommendation, which you beautifully expressed, go

**[01:06:53]** try it out, so I won’t pay from the outside, whether you

**[01:06:58]** You would say, no, but you didn’t say it, did you?

**[01:07:01]** Okay, then it’s simple, take Notion, try it out, just look at it and just ask a silly question to the system

**[01:07:09]** and let yourself be surprised by what comes out as a result,

**[01:07:14]** and I would bet that everyone who installs Notion and asks a serious question will stick with it.

**[01:07:23]** Yes, I believe that too.

**[01:07:25]** It's so nice that it can grow very well with your needs.

**[01:07:30]** You can start with a small stamp collection that you want to archive

**[01:07:35]** or where you need a database, you can do it just like that, nicely with images and nicely

**[01:07:40]** design it a bit, and so on, like these complex systems.

**[01:07:44]** And what I also have to mention is the community of people who work with Notion,

**[01:07:49]** whether you're on social media or on Slack in those things, they are really,

**[01:07:54]** really nice people, it's very open-minded, it's very multi-cultural, there are people from all

**[01:08:00]** corners of the world, so super interesting, also what they do with it, how

**[01:08:05]** they do it, sometimes totally crazy, sometimes really inspiring stories and

**[01:08:10]** what I really recommend to everyone who is new to Notion are these three, or rather,

**[01:08:15]** I mentioned three, I believe three podcasts, videos, video channels, so how you have it

**[01:08:20]** YouTube channels, exactly. Simon as Better Creating, Thomas Frank, and Matthias Frank from Berlin,

**[01:08:26]** those are the three, if you watch them, you simply have the complete package and a

**[01:08:30]** super foundational supply or a complete supply actually. You can learn a lot from

**[01:08:35]** them, yes.

**[01:08:36]** So, with the topic of foundational supply, I am now familiar with it professionally, but

**[01:08:40]** he means, of course, the topic. That's another foundational supply.

**[01:08:44]** You must mean energy supply, right?

**[01:08:47]** I want to.

**[01:08:48]** Yes, that's nice, in our podcast it usually ends then at the end, so we say thank you and if you liked it, then tell your friends, family, and everyone and leave us a like and share the podcast, etc.

**[01:09:05]** What else can we do for you?

**[01:09:07]** So usually I have, but we already did that, an A or B question, I stole that from alles gesagt and we are not doing that today.

**[01:09:17]** I definitely want to thank you, dear Mark, for being with us and for having a podcast together.

**[01:09:24]** Where we shared with each other

**[01:09:27]** What we are experiencing in this digital age, using that name one more time, and I'm very happy that I could still inspire you

**[01:09:34]** With a technology because now I finally have a conversation partner

**[01:09:40]** who is probably just as or almost as crazy about it as I am. So,

**[01:09:47]** when it comes to AI, you are crazy, as I am, but AI and Notch, that's definitely something,

**[01:09:51]** that unites us. So, thank you for being here. Thank you for giving me, in a way,

**[01:09:56]** homework as well, when we finish recording here in a moment,

**[01:09:59]** I not only know that I am happy to provide you with the recording,

**[01:10:04]** but also that I will try your feature in Notion.

**[01:10:09]** Thank you for being here. Thank you all for listening.

**[01:10:12]** We are now going to wrap it up.

**[01:10:14]** In that sense, until next time.

**[01:10:17]** Ciao. See you soon. Bye.

**[01:10:21]** Welcome to Think Different, Think AI.

**[01:10:24]** The podcast by Mark and Jens.

**[01:10:26]** Two tech-loving minds,

**[01:10:29]** who don’t just talk about artificial intelligence but live it.

**[01:10:33]** Here you will find clear categorization, real practical insights, and a fresh perspective on what is possible.

**[01:10:39]** Understandable, critical, and always with a wink.

**[01:10:43]** H.I. to think about, to chuckle at, and above all, to discuss.
