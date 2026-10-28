---
title: "Software Ade"
episode_index: 63
published: "Sat, 24 Oct 2026 04:05:00 +0000"
duration: "2983"
page_url: "https://think-ai.podigee.io/63-software-ade"
image_url: "https://images.podigee-cdn.net/0x,sqmwLflMfYYnJwucrFtHlrDpgblFlaD9a8_x3gu2iNRk=/https://main.podigee-cdn.net/uploads/u73317/ddd28ccb-e968-4e50-a3f3-09921f4150c5.png"
audio_url: "https://audio.podigee-cdn.net/2624616-m-0d39cdde5392f974275af124f00f1467.mp3?source=feed"
guid: "39734ac334898b210b22fb485bdae3d7"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "medium"
language: "en"
language_probability: "1"
transcribed_at: "2026-10-28T18:10:38+00:00"
translated_from_language: "de"
translation_provider: "claude"
translation_model: "claude-haiku-5-5"
translated_from_file: "transkripte/063 - Software Ade.md"
translated_at: "2026-10-28T19:07:49+00:00"
---


# Software Ade

**Published:** Sat, 24 Oct 2026 04:05:00 +0000
**Duration:** 2983
**Web player:** https://think-ai.podigee.io/63-software-ade
**Cover:** https://images.podigee-cdn.net/0x,sqmwLflMfYYnJwucrFtHlrDpgblFlaD9a8_x3gu2iNRk=/https://main.podigee-cdn.net/uploads/u73317/ddd28ccb-e968-4e50-a3f3-09921f4150c5.png
**Audio:** https://audio.podigee-cdn.net/2624616-m-0d39cdde5392f974275af124f00f1467.mp3?source=feed

## Description

What is software still worth when everything can be rebuilt?
Reverse engineering used to be a high art. With AI it becomes an everyday tool, and that calls into question the business model of many software houses. Mark and Jens discuss what software is still worth when foreign programs can be rebuilt in hours. The episode starts with TV habits from Mark's childhood and ends with game ideas and a look ahead to a future episode.

The opening runs through games that can be mixed. Mario in Fortnite, Bubble Bobble crossed with Populous: whoever pulls characters and mechanics out of other games creates combinations nobody has come up with before. Whether that is legal, the two leave open. It is not legal advice and not an invitation, but an observation of what is happening out there right now.

With graphics software such as Figma, a different question arises than whether it can be rebuilt. Why copy a tool built for a way of working from 30 years ago? Mark describes how a colleague, using Opus, quickly built an interactive 3D model in the browser, with dials you operate yourself. The tool is tailored to your own work, instead of paying for a license to a general-purpose program.

One experiment goes further: an existing app is rebuilt so that it runs as an MCP server. An AI can then talk directly to the backend, without an interface. A user interface becomes an interface for machines. When software is easy to rebuild, the finished product loses value, and the service around it gains. Maintenance, adaptation and the business relationship remain. For vendors, that means rethinking license terms and contracts, and perhaps selling consulting instead of packages. Existing customers are an advantage that a fresh rebuild does not have right away.

Old hardware falls under this as well. Devices whose manufacturers no longer provide updates can be analyzed and brought back to life. Mark mentions an old speaker box with a glowing ring, on which he wants to run his own AI voice.

The flip side: whoever has access to good models, to tokens and to time can use this. Whoever does not stays on the outside. The group that actually builds software this way is small. In the episode's example calculation, an agency charges a five-figure sum for a small app, while the tokens for it come to a few euros. The two see this more as a gap that AI can narrow than one that it widens.

Finally it gets playful. Maniac Mansion, Zak McKracken and Manor Lords are on the table. Mark would cross the medieval building game Manor Lords with a global simulation that reaches from the backyard to the planet. The idea of using game interfaces as an interface for AI systems also comes up. For a future episode, the two suggest discussing the skills in their own AI system.

—
Think Different. Think AI. with Mark Zimmermann and Jens Scharnetzki.

Listen: Apple, Spotify, YouTube, RSS
https://think-ai.podigee.io

New episode first in the WhatsApp channel
https://whatsapp.com/channel/0029VbDJ4ZlGufIrpquad004

If the episode gave you something, rate us once on Apple. That decides whether someone new finds us.
https://podcasts.apple.com/de/podcast/think-different-think-ai/id1828021699

Feedback and guests: via the show page.

## Transcript

**[00:00:00]** Welcome to Think Different. Think AI., the podcast by Mark and Jens.

**[00:00:07]** Two tech-loving minds who don't just talk about artificial intelligence, but live it.

**[00:00:14]** Here you get clear classifications, real practical insights and a fresh look at what's possible.

**[00:00:20]** Understandable, critical and always with a wink.

**[00:00:24]** AI to think about, to smile about and, above all, to join the conversation about.

**[00:00:33]** Welcome to Think Different. Think AI.

**[00:00:37]** And before I say something wrong: Jens, is that you?

**[00:00:42]** Of course it's me, who else would it be?

**[00:00:44]** Yes, live and in color.

**[00:00:45]** Could be, Reverse Engineer Anything.

**[00:00:48]** could just as well have knocked a new Jens together for me.

**[00:00:51]** I haven't even tried that yet.

**[00:00:52]** Nice to have you here, Jens.

**[00:00:54]** Thanks, thanks.

**[00:00:55]** Already a nod to the show.

**[00:00:57]** I just noticed, "live and in color," for the younger listeners among us.

**[00:01:01]** That goes back to the time, I might as well admit it, when there was no

**[00:01:06]** color television yet.

**[00:01:07]** People always said "live and in black and white."

**[00:01:11]** I still know two sentences from TV, when they said, "We have an [unclear] so that, when"

**[00:01:17]** people, when the presenters on TV called in from somewhere, that they were in the sound booth,

**[00:01:21]** they knew when to switch.

**[00:01:22]** And you're talking to a living remote control.

**[00:01:26]** I vaguely remember, and greetings go out to my parents, who are listening too:

**[00:01:31]** that's how it stayed in my memory, even if they meant it differently.

**[00:01:34]** that it happened quite often that I was sent to the TV to switch channels,

**[00:01:38]** because there was no remote control, and I was then

**[00:01:42]** basically the human remote control. My father was also a magician,

**[00:01:47]** who then just, the TV is off. What I didn't see

**[00:01:51]** was that he, behind the wall, stretched his arm out so far

**[00:01:54]** that he touched the fuse box, and I was fascinated.

**[00:01:59]** That was still the phase when there were no couch potatoes yet, because you still had to get up

**[00:02:04]** to walk over to the TV.

**[00:02:06]** Yes, I don't know which vice people had back then, or why people thought, back when

**[00:02:12]** I was basically a youngster, that "the youth of today is a lost cause," which is somehow

**[00:02:20]** in every generation.

**[00:02:21]** Somewhere I recently heard a quote, I can't quite recall it,

**[00:02:22]** and then it turned out it came from ancient Greece, from a time long

**[00:02:26]** before our world.

**[00:02:27]** Whatever.

**[00:02:28]** I'd say not everything was better in the past.

**[00:02:30]** Let's just note that.

**[00:02:32]** But not everything was bad either.

**[00:02:34]** So, come on.

**[00:02:35]** Now we've covered quite a lot of general ground.

**[00:02:38]** Let's talk about the value of software.

**[00:02:46]** Without wanting to step on anyone's professorial toes.

**[00:02:49]** We had [unclear] on here.

**[00:02:51]** We also have people in the listener circle who deal with it.

**[00:02:55]** But let's get to the real question:

**[00:02:56]** what is the value of software in this day and age? I came at it via [unclear], where a framework is taking off on social media

**[00:03:03]** that basically lets you, or promises you, that we can perhaps still talk a bit about

**[00:03:09]** copying software, just by "here's a file,

**[00:03:16]** here's a link, I don't even need access," and what kind of stylistic blunders come out of that.

**[00:03:22]** We can discuss that in a moment too. But what does it mean for our time? Or shall we

**[00:03:26]** first listen to what happened? Sure. So the topic is

**[00:03:30]** reverse engineering, looking at something and then basically, by

**[00:03:35]** taking it apart, working out how it was actually put together.

**[00:03:39]** That's one of the high arts of software development,

**[00:03:44]** because it's not that easy. You have to know that

**[00:03:46]** the average software developer doesn't always follow Plan A,

**[00:03:50]** and I don't want to step on the professor's toes here either, it's

**[00:03:53]** sometimes code that gets a bit complicated here and there. You resolve

**[00:03:57]** to comment every single line you write. That's what you forget

**[00:04:02]** quite often. From page 30 of code you've written, it's no longer that clean.

**[00:04:07]** Accordingly, it's not that easy to look at complicated pieces of

**[00:04:11]** software, where millions of lines of code often come together, and to work out

**[00:04:17]** from the code alone what this

**[00:04:21]** software actually does. Or, in very, very complicated cases,

**[00:04:24]** because in the last few weeks, complicated games, for example,

**[00:04:28]** were reverse-engineered and made browser-capable. What does

**[00:04:32]** a character do that hops around somewhere in such a game? It's all

**[00:04:35]** hidden in the code, and just by looking at the

**[00:04:41]** files, as you just described, the source code in these

**[00:04:44]** files, turning it back into a working version is

**[00:04:49]** truly a herculean task if you do it without AI.

**[00:04:54]** What you said about games, that's also what I first stumbled over.

**[00:04:57]** It's actually about two things. One is this Sony PlayStation business, whether it has

**[00:05:02]** anything to do with it, I don't know, but there's a bit of hype right now,

**[00:05:05]** that not just a jailbreak for the PlayStation is coming out, but

**[00:05:10]** that now, somehow, everything that isn't quite all there

**[00:05:13]** can run on the PC from the PlayStation 5 and be combined. Greetings go out

**[00:05:18]** to the topic "software no longer belongs to you." Maybe the manufacturer will reconsider that.

**[00:05:22]** Another topic. And no, once more: this has already happened

**[00:05:26]** many years ago, too. Sony as well, from that side. One shouldn't

**[00:05:30]** underestimate it. Nowadays the kiddies have even more powerful

**[00:05:34]** tools at their disposal. But where it hit me more definitely with Rea

**[00:05:39]** was the topic of mixing games. So that you

**[00:05:44]** walk around with Super Mario in Fortnite, and it goes so far that you don't just have the character,

**[00:05:49]** you don't just have the sound, but also these glitches, these peculiarities

**[00:05:58]** from a game, from which you basically pull out the character, you also have in there. They had

**[00:06:03]** something like: when Mario walks backwards up the stairs and jumps through the

**[00:06:06]** door at the top so that he then flies to the next stage, and that happened

**[00:06:12]** in Fortnite, or that in Super Mario Kart you have someone sitting at the sniper

**[00:06:18]** sorry, shooting out of the cars, and then you think, the damned [unclear],

**[00:06:24]** how cool is that? Not because of the snipers and the cars, but because you basically have the

**[00:06:29]** chance, and I don't want to judge at all whether I'm allowed to, and yes, but simply

**[00:06:34]** let your imagination run free and say, I suddenly connect the heroes

**[00:06:40]** of my games, my favorite games, everything together, blend it into a new game,

**[00:06:47]** into a new game experience. And then it also raises the question: games come into being,

**[00:06:55]** we had the Gamescom episode and other places talking about it for a long time, and partly

**[00:07:00]** also with, I'd say, love in it, at least love for detail, depending on which game one

**[00:07:04]** takes. If it's called Wolverine, and then suddenly something like this comes around the corner

**[00:07:10]** and says, I always thought it was good to cross Populous with Fortnite and Bubble Bobble, and

**[00:07:15]** suddenly you wonder why your characters are wrapped in soap bubbles by little dragons.

**[00:07:20]** That's already a bit wild. So we should come back to this topic right away, as you invited us to:

**[00:07:26]** what is software still worth? But of course we can

**[00:07:30]** also take a small look in there, because it naturally brings an explosion of

**[00:07:34]** creativity again. Because this combination you just mentioned,

**[00:07:38]** nobody had thought of until now.

**[00:07:41]** Well, licenses are attached to that too.

**[00:07:44]** Licenses are attached, all fine, all good,

**[00:07:46]** but of course it's still somehow in a different way

**[00:07:49]** exciting again, what's in principle possible,

**[00:07:52]** now very different game characters, game ideas

**[00:07:56]** to combine super quickly with each other.

**[00:07:58]** Accordingly, I'm very often positive about things like this,

**[00:08:03]** to be honest, and I think this could be another one of those...

**[00:08:05]** That's already, well, the internet went wild over it.

**[00:08:09]** So there's an explosion of creativity there, whether it's always legal?

**[00:08:14]** No, half of it is efficient.

**[00:08:16]** No lawyers, no legal advice.

**[00:08:18]** Exactly, no legal advice.

**[00:08:20]** We don't know.

**[00:08:22]** But accordingly, of course, that's not everything, no matter what gets done there.

**[00:08:24]** But it shows where we're heading.

**[00:08:26]** So, to really say it, I can actually build pretty much everything I

**[00:08:35]** need, whether that's a game or a piece of software. That moment has now, for the time being,

**[00:08:41]** been reached, and it's always built securely. You know the other things. There are plenty of

**[00:08:44]** right now again on Instagram or elsewhere, where people say, yes, we love

**[00:08:49]** bad code. You of course forget, here are the 110 things you forgot to do,

**[00:08:53]** like security or other things, so your app isn't secure or whatever.

**[00:08:56]** Stick around until the end, then I'll tell you the most important one.

**[00:08:59]** Exactly. Accordingly, of course, it isn't always one hundred percent secure and clean right away,

**[00:09:07]** but AI can solve that too and help you, even if you've never done it in your

**[00:09:11]** life before. So things are now such that I say we're entering

**[00:09:17]** an age where, really, it's never been like this with this value software,

**[00:09:23]** but of course it's one aspect. For me, the more exciting aspect is that I

**[00:09:27]** say we have to rethink everything now, because software too, just like a game,

**[00:09:34]** the respective developer thought inside a certain box, to solve a certain problem in a

**[00:09:38]** certain situation.

**[00:09:39]** And even if he did it so well that in principle it helps many people, then

**[00:09:43]** in principle many people have bought that software too.

**[00:09:46]** Now here's the thing: if we look at graphics software, there was

**[00:09:51]** also a famous example in the last few weeks, there was this, I

**[00:09:55]** think it's called Handcraft, that someone in the Photoshop approach...

**[00:09:59]** Isn't it called Figma too?

**[00:10:00]** Figma too, I hadn't even noticed that.

**[00:10:02]** So Figma now too, by now.

**[00:10:03]** For everyone who now thinks we're a decent podcast, yes, we are, the ones who

**[00:10:09]** say it that way.

**[00:10:10]** That's not the Hessian way.

**[00:10:11]** Yes, not Hessian Figma, and always Azure with Azure, yes, but software is called Figma.

**[00:10:16]** Good heavens.

**[00:10:17]** Okay, yes.

**[00:10:18]** Spelled F-I-G-M-A. They also had a funnier name, I think,

**[00:10:23]** in German.

**[00:10:24]** they also introduced a whiteboard, a collaboration board, which was called Jam, so that was

**[00:10:28]** FigJam, the name of Figma's whiteboard tool, also somehow odd. Everything

**[00:10:33]** whatever, you can't always get the localization of names right across the whole

**[00:10:37]** world, that's a tricky business too.

**[00:10:39]** Back to the topic: all of this can basically be rebuilt now. Does it make sense to rebuild it?

**[00:10:45]** No, it makes sense if you want to save money, that's one angle,

**[00:10:49]** one could take.

**[00:10:50]** What I think is much more exciting about this topic is that you can now ask yourself, do I need

**[00:10:55]** this software that already exists anyway? Then I could just buy it, couldn't I?

**[00:11:00]** Always that way?

**[00:11:01]** Or do I actually need something else? For me it's a bit of a survival question,

**[00:11:04]** slowly coming around to saying, yes, it's of course cool to have a graphics editing tool like

**[00:11:09]** that, but honestly, I can almost make all the graphics I need

**[00:11:13]** with AI like this.

**[00:11:15]** What do I need?

**[00:11:16]** Really a tool that helps me in a very specific way, maybe as an editor for this graphic in my

**[00:11:23]** personal way, so that I can influence it, and not, as it has been common for the last 20

**[00:11:29]** or 30 years in desktop publishing, where you somehow use a mouse pointer to draw a

**[00:11:34]** frame around several objects, select them, give them a color, give them

**[00:11:39]** a line weight, a background color and a foreground color. That's basically what

**[00:11:44]** those graphics programs have been doing for the last 30 years, with a bit more fancy stuff.

**[00:11:49]** I think that's the really exciting thing I'm seeing right now: we're in a phase

**[00:11:54]** where everyone out there can build their own tools for their situation.

**[00:12:00]** And they don't have to be the same tools, because that would actually be silly.

**[00:12:02]** Rebuilding the same tools that already exist, now with AI, is nice to look at,

**[00:12:07]** but apart from a certain kind of maybe modern piracy, it's nothing

**[00:12:14]** world-shaking at the moment. It just shows where AI is more capable,

**[00:12:19]** in my view it shows zero creativity for the people doing it right now.

**[00:12:23]** Creativity comes more from what we've now seen with the games, where people

**[00:12:27]** combine things, or where other people build their own way of

**[00:12:32]** doing things on devices, on appliances, because reverse engineering

**[00:12:36]** works just the same for, I don't know, the stereo system at home, which is

**[00:12:40]** somehow connected, or the light switching I have in my house

**[00:12:43]** right now. I found that really great about this reverse engineering, so this

**[00:12:47]** Rea GitHub. What are the top projects? The top projects don't even

**[00:12:51]** start there. Rebuilding Word, Excel, PowerPoint. Greetings go out, as I said, to Adobe, Word, Excel

**[00:12:55]** PowerPoint, blah blah, all of that has been tinkered with by now. Surprisingly,

**[00:12:59]** in fact the topic is old things: reactivating drivers, for

**[00:13:05]** old things, reactivating connections, bringing back support for old file formats

**[00:13:10]** that, I found quite astonishing, that it was

**[00:13:15]** way up front in the statistics. I noticed that I was the old

**[00:13:20]** white man again, and the uncreative one, while you were talking, because for me

**[00:13:24]** the first thing that went through my head was, what does this mean for the software market, what

**[00:13:28]** software licenses are concerned, what does it mean for the software market, what it then

**[00:13:33]** means that companies, let's say in quotation marks, whether with or

**[00:13:36]** without AI, make an effort for software, if it's, well, stolen again or whatever

**[00:13:42]** anyway, yes.

**[00:13:43]** So as I said, whether it's legal, illegal, or wherever in the world

**[00:13:47]** it's done, that's completely irrelevant, just evaluate the result, what that means and

**[00:13:53]** my creativity isn't such that I didn't even try the

**[00:13:57]** thing.

**[00:13:58]** My creativity was actually a completely different topic, namely, I took one

**[00:14:02]** and said: just watch, don't rebuild the app. So a bit of Xcode and such

**[00:14:08]** I can handle, I manage that quite well with Claude, I don't need anyone to tell me,

**[00:14:12]** rebuild an app. My question was: look at the app, rebuild the app for me, but as an MCP server,

**[00:14:19]** so that you basically don't have the app front end, but something that AI can consume.

**[00:14:30]** And then I thought, okay, I can give it away up front: the result was

**[00:14:35]** that it works, and then you basically had something you can plug in as a tool in Codex

**[00:14:43]** or wherever else, and then, after you've done a login,

**[00:14:48]** you can talk to the backend that would actually have spoken to you yourself.

**[00:14:54]** I'd find it fascinating to ask what the backend thinks, so thinking is also

**[00:14:58]** relevant, but what the backend thinks, what it speaks with, whether it was then that Android version

**[00:15:02]** that served as the basis, or whether it noticed, haha, that's something else. And that

**[00:15:09]** isn't meant as a call to imitation at all, but the point is, suddenly you can also do

**[00:15:13]** conversions, saying, I have a result here, damn it, make it work again,

**[00:15:19]** runnable, make it run on another system, like PlayStation players suddenly running in the

**[00:15:24]** browser, and suddenly an app runs there as an MCP server. The boundaries are dissolving. So

**[00:15:31]** things are changing extremely right now. And you also recently showed me various videos

**[00:15:36]** by someone who tries to present knowledge with HTML pages, perhaps

**[00:15:42]** run again. You can explain that better than I can. If you now go and say,

**[00:15:46]** okay, I like the idea, I want to apply it to another topic. Dear Rea or

**[00:15:51]** by now Claude can surely do a lot of that on its own,

**[00:15:54]** let's leave that open. But dear AI, with whatever tools, take that as your guide,

**[00:15:58]** bring it to this and that level, bring something new into it. I think

**[00:16:03]** we'll see more and more of this exponential growth in floods of

**[00:16:09]** faster, higher, further, that the system really picks up speed, because software is no longer

**[00:16:16]** copied, cloned, because software is being merged, because software, I'd call it

**[00:16:22]** a different state of matter, so a front end becomes an interface,

**[00:16:27]** an interface becomes... no idea what. So suddenly completely new things emerge

**[00:16:32]** will. The question that remains, of course, critical for society, for me is

**[00:16:35]** what does it mean for the people who tinker with software today? What does it mean

**[00:16:39]** for people investing in software today? What does it mean for startups, when no

**[00:16:46]** idea what will happen. Suddenly anyone can rebuild any character they like,

**[00:16:54]** replay it. What does that mean for copyright? I'm not allowed to copy Lara Croft, but I could

**[00:17:00]** in theory, in theory, no call to do so, rebuild the whole game and just let the

**[00:17:05]** textures change. Is it still Lara Croft then, or is it like back then with Mario and

**[00:17:10]** Yes, so suddenly it really gets wild.

**[00:17:15]** Definitely, and let me just quickly, what you just wrote, this

**[00:17:20]** example, we can put the link in too. It's a colleague who is actually

**[00:17:24]** right now, with Opus, quickly building three-dimensional, clearly understandable things that you can

**[00:17:35]** fully rotate in the browser. These things he builds, that means he has built something

**[00:17:38]** like a cardiovascular simulator, how erosion happens in a valley

**[00:17:47]** when a river winds through it, and how a turbine, how a rocket turbine works.

**[00:17:52]** All these things, you can still play with sliders, you can view it from all sides...

**[00:17:56]** So interactive information graphics, three-dimensional, in the browser.

**[00:18:01]** Yes, and he has, in principle, a bit of, that was for me,

**[00:18:05]** and we both talked about it too, it was a bit of the reason when I saw that

**[00:18:09]** and all the dials he built in, and that it was built so fast each time,

**[00:18:12]** we thought, that's actually a good idea, to say, okay, why doesn't one build that

**[00:18:19]** basically for the workflows one has, as I just described?

**[00:18:22]** Do I actually still have to learn Figma or Adobe programs somehow to edit graphics?

**[00:18:29]** Or shouldn't I just tell myself, look, if I can build an interactive module like that

**[00:18:34]** to work out a cardiovascular system, then I'll also be able to build an interactive module

**[00:18:38]** to change the color of an image from black to colorful or introduce some style

**[00:18:45]** or to say, make a three-dimensional object out of this two-dimensional one, and I can

**[00:18:50]** do that with my own sliders, because I might then still want to fine-tune it a bit

**[00:18:54]** and every time by text again, maybe with the AI, the prompt image,

**[00:18:59]** I need my own tool landscape. That's why it fascinated me, and that is

**[00:19:03]** I think, a bit of what I notice, what I see, what's

**[00:19:07]** happening out there right now. And of course, that has an impact on the software industry, as

**[00:19:13]** it currently still operates. It will also keep working that way for a while

**[00:19:18]** longer, no question, but let's maybe slice that a bit more

**[00:19:21]** finer. When I introduce software, for example in a large

**[00:19:25]** company, there's often also a big cost driver that

**[00:19:30]** hides in the fact that this software only fits partly, at 80 or 90 percent, the

**[00:19:37]** respective company. Whether it's the skills of the people in the

**[00:19:41]** company, who first have to be trained on it, or that in principle

**[00:19:43]** some topics actually still have to be ported differently, other

**[00:19:48]** data has to be connected, then there are structures that are perhaps

**[00:19:51]** a bit different, the workflows were different. It doesn't fit exactly,

**[00:19:54]** the way the software designer imagined it, or the

**[00:19:57]** big company that came up with it. And a lot of

**[00:19:59]** money gets invested there, in success managers, software, people who come into the company

**[00:20:05]** to help the company learn and adapt this software.

**[00:20:10]** I'd say that's already a first big lever for the software companies, to

**[00:20:15]** think about how they can actually take a different approach in the future,

**[00:20:19]** by making this part of their software much more personalized for each

**[00:20:25]** company, because I simply say, what people out there can do, if

**[00:20:29]** my software can be completely reverse-engineered, why not offer it as a service

**[00:20:34]** for example, saying: dear company X and dear company A, you get here on

**[00:20:40]** this proven product that has run stably for years, that was developed

**[00:20:47]** according to software development principles, that is secure, that you already use, or

**[00:20:50]** if you've heard it works well at other companies,

**[00:20:52]** we can personalize it perfectly for you, so that the phase in which you basically

**[00:20:58]** have a long onboarding phase gets much shorter. And your processes are then much shorter too,

**[00:21:03]** because this software will keep adapting to you, because we can keep

**[00:21:07]** bringing the topic in further with AI help. That's how I'd do it. That's a change,

**[00:21:11]** the software. You may not need so many people to, in principle,

**[00:21:15]** run trainings, because the training will become less. But you can use the

**[00:21:19]** people for other things. So that means you have to adapt. That

**[00:21:23]** has always been the case when progress came. We all know that with AI this

**[00:21:27]** has become a bit crazier, that things happen fast. But there's really also

**[00:21:32]** a lot of opportunity in it, also for existing software vendors out there, who shouldn't just throw in the towel

**[00:21:37]** and say, yo, sorry, everything can be reverse-engineered anyway now. We

**[00:21:42]** close up shop, because anyone off the street can now rebuild our software.

**[00:21:46]** No, I think there's also a chance in it, to keep saying, yes, business is also

**[00:21:51]** not just about putting a piece of tool out there, but also includes a business relationship

**[00:21:54]** that I have with someone. I do have that, and it's an asset that many who now

**[00:21:59]** first rebuild new software may not have yet. That can be used really well

**[00:22:04]** for a while, and to position yourself in this market, so that you also

**[00:22:07]** learn how this software market can also work in the future. Because I don't

**[00:22:15]** think, and feel free to correct me, that now every software, in every situation,

**[00:22:23]** is automatically generated by an AI, even though our beloved NVIDIA boss once said

**[00:22:28]** that in the future, NVIDIA pixels will be generated. Yes, that may be in some distant future.

**[00:22:33]** Is it economical that we say everyone in the world now builds their own

**[00:22:37]** word processor, or their own adapted one, if you like? No, probably not

**[00:22:42]** either, honestly. It also makes sense that, for my part, someone builds a hand-coded

**[00:22:47]** writing document or little writing editor software that's better than perhaps established ones,

**[00:22:53]** But not everyone has to build after it. I think there's also room and music in it to say, yes, I have a piece of software for you here, whether it's AI generated or not doesn't matter.

**[00:23:07]** But it will help you in a certain situation. Feel free to pay a few euros for the right to use it. That will carry on.

**[00:23:15]** I think, this will change the way we build software once more.

**[00:23:20]** Because the time when you say, I now have a project.

**[00:23:25]** This project builds a piece of code.

**[00:23:28]** This code gets used in something like [unclear], on the website, in one piece, a kitchen appliance, I have no idea, whatever.

**[00:23:37]** And then you sit there with big teams in rituals and somehow build

**[00:23:44]** a year on something like that and look forward to a release like an Apple operating system

**[00:23:49]** coming out, like every year, and that it gets modernized a bit so that one

**[00:23:57]** sees adaptations faster, sees topics adopted faster, along the lines of

**[00:24:03]** Yes, who knows. People, so a fictional example. You now have Mac OS from Windows, and there are people

**[00:24:10]** who have Mac OS but still miss Windows when they see Windows Explorer,

**[00:24:15]** the file manager, because the Mac Finder can't do it. Now, you basically

**[00:24:20]** as a user are able to say, let's build a thing like that, that looks like the

**[00:24:25]** Explorer, I want that for Mac. But you could also, as Apple, which you could do before too,

**[00:24:30]** you maybe had limited resources, limited time. You thought, I'm not going to build

**[00:24:34]** that, and that's part of the peculiarities of my operating system, blah blah.

**[00:24:38]** I'm not doing that, I don't want to, I can't, I don't have time or whatever.

**[00:24:41]** And I think at that point we'll see a change, which in turn ends in a

**[00:24:46]** speed-up, because suddenly the possibility, how long does it take between,

**[00:24:51]** I have the idea, a vision for my product, to, it's been tested in 40,000

**[00:24:58]** different variants. You run a test or whatever, along the lines of Monday

**[00:25:02]** a quick idea, Friday in the product. So, you now have this possibility, and you

**[00:25:07]** can test things much more easily. You can simply create facts

**[00:25:12]** and if it doesn't fit, I change it again. You have a much

**[00:25:16]** more dynamic setup, that you, in quotation marks, with fewer people in

**[00:25:20]** the shortest time can run things. And that, I think, is what we'll notice.

**[00:25:25]** No matter how big or small it is, whether you're a consultancy or a software vendor, this will

**[00:25:34]** change it, and thereby also make the fundamental question harder for the people who say,

**[00:25:40]** but this is handmade here, this is crafted, this is, I need, the

**[00:25:46]** question earlier, when you say you're building software, I need four weeks.

**[00:25:50]** People thought, why do you need four weeks, the screens are finished, aren't they?

**[00:25:54]** because I still have to do this and that. Today someone says, I still need four

**[00:25:59]** weeks, and then he says, why? You don't even have the screens yet, but that doesn't matter. Today

**[00:26:02]** evening everything's done, thanks to the AI. What more do you want? Well, I still find that

**[00:26:08]** difficult. That will of course change, and the cycles are shorter

**[00:26:13]** definitely, and I think I'd also say that with the

**[00:26:17]** classic license sale, often in the corporate environment of software licenses

**[00:26:23]** they're often sold for one, two, three years, or even longer. I think this will

**[00:26:30]** partly become an exciting question for one or another decision maker. For how long do I buy

**[00:26:37]** software now? So something will simply change there. There the cycles will

**[00:26:40]** partly, I think, get shorter. What I think could also happen, and

**[00:26:44]** maybe is also a chance for one or another to say, yes, you don't buy any

**[00:26:48]** finished software piece anymore. I simply deliver you a solution. I'm simply the

**[00:26:52]** one with my software who helps you actually always have the right

**[00:27:00]** software solution in your workflow.

**[00:27:01]** Because we both know that in this AI world, everything may be different again in five months anyway,

**[00:27:07]** so I simply sell you my consulting contract

**[00:27:12]** and no longer a fixed piece of software at that moment for the partial area

**[00:27:15]** of this assignment.

**[00:27:16]** And then that scales, because I'm a software house, I have the people, I basically have

**[00:27:20]** the software engineers, I have the success managers who can be on site with you and observe

**[00:27:24]** how software is in principle used, what needs your internal people have in

**[00:27:29]** principle, in order to access things.

**[00:27:31]** Let me into your house, or rather your company, and I'll basically build with

**[00:27:37]** my two-year program that I have, you'll basically have 400 versions over the next two years

**[00:27:44]** of this software.

**[00:27:45]** And at the end of those two years you'll probably look completely different,

**[00:27:48]** these software solutions you bought on day one. I also have something like that to offer.

**[00:27:52]** I think one would have to figure out now how such business models can work.

**[00:27:56]** These also require new contracts, because one simply no longer

**[00:27:59]** buys the package the way one may have been used to earlier. But I think there is definitely,

**[00:28:04]** there's also always a theme there, as I said, now it's a question of trust

**[00:28:09]** of course too. Do I trust some software first, which was quickly

**[00:28:14]** reverse-engineered somewhere. Or do I rather trust the software partner

**[00:28:19]** I've been working with for a bit longer. I think

**[00:28:21]** pressure will come onto the market. Expectations are going to rise at the moment. The

**[00:28:25]** expectations regarding pricing too. But I've just given a few

**[00:28:29]** hints on how one might be creative there. Still, to cut off another slice of the

**[00:28:33]** pie. But of course there will be a change there. I think,

**[00:28:38]** This is actually now, this has already been the case since the AI phase,

**[00:28:44]** I mean, the software industry was the first where producing pure code

**[00:28:51]** was then sold best, as it used to be, in a shoebox

**[00:28:56]** and installed in the Mercedes. That phase is over.

**[00:29:00]** You can't whine it back now, however much you want.

**[00:29:03]** it will of course still take some time, we're not all different right away,

**[00:29:09]** but it's slowly going away now. Because there one can really say, okay, that can

**[00:29:15]** happen differently. The phase of sky-high prices for software is possibly over too. That

**[00:29:21]** means the actual piece of product is no longer the decisive thing. The product is

**[00:29:27]** today, if it's digital, very, very quickly copyable. We also see physical products,

**[00:29:33]** it's coming bit by bit, it will also become very, very quickly copyable at some point. But above all digital

**[00:29:37]** products, at this moment, the product is no longer worth that much. And the product,

**[00:29:43]** if it's software, is simply no longer worth much. The service around it is what

**[00:29:46]** is worth something. The maintenance, the adaptation, that costs us money and time at this moment. And

**[00:29:52]** for me that actually belongs to a complete product development. People always

**[00:29:56]** forget that. And that's also the thing where, but of course, that means

**[00:30:01]** of course, it's also the place where people tend to look at the one-time price

**[00:30:08]** rather than the long-term service, at first glance too, along the lines of, yes, look

**[00:30:13]** it costs 80 euros and not 300. For the 80 euros I can buy it three times new

**[00:30:19]** before I reach the 300. Why on earth should I, once more,

**[00:30:23]** buy anew, take the more expensive product, there is, that's a very simple calculation now,

**[00:30:28]** I admit that. But as you said, that will bring movement.

**[00:30:33]** Yes, definitely. Now let's have the microphone briefly off. Definitely.

**[00:30:39]** By the way, the AI cuts that out again. That means nobody noticed the pause, and you

**[00:30:45]** say the microphone is gone. So Jens had a really long pause at that moment

**[00:30:50]** and I was briefly afraid that he was gone.

**[00:30:52]** No, no, all good.

**[00:30:53]** But you see, that shows we're still real.

**[00:30:56]** Real handwork is still being done here.

**[00:30:58]** When we talk here, mistakes are allowed to happen too.

**[00:31:01]** I'll slip away for a moment with my mic button.

**[00:31:04]** I've found the following on the internet for you.

**[00:31:07]** Oh, I see.

**[00:31:08]** I've found the following for...

**[00:31:09]** That's Siri when she doesn't understand you.

**[00:31:11]** Damn it, I wanted to make a little joke there

**[00:31:14]** and you stab me in the back like that.

**[00:31:16]** Well, carry on.

**[00:31:17]** Which series?

**[00:31:19]** Siri, not series, Siri, when we...

**[00:31:22]** Oh, Siri, Siri.

**[00:31:25]** You'll have to work on our mumbling, Mark.

**[00:31:27]** Mumbling?

**[00:31:28]** Well, ash with ash.

**[00:31:30]** Really?

**[00:31:31]** Yes, well.

**[00:31:33]** In any case, let's come back to reverse engineering,

**[00:31:35]** which also simply offers possibilities.

**[00:31:37]** Well, we've now talked a bit about the

**[00:31:38]** fact that it will change the software industry,

**[00:31:40]** I think we've now beaten that to death enough.

**[00:31:43]** That's part of this AI revolution.

**[00:31:46]** And that should now become clear to the last person,

**[00:31:48]** since the last two, three weeks, since this topic has become so hot.

**[00:31:50]** What's really exciting is what we may have somewhat neglected

**[00:31:54]** so far, that it's not only, when you think of reverse engineering,

**[00:31:59]** that you always think of the digital products you come across.

**[00:32:03]** Because we just had this topic of hardware too, where software is partly

**[00:32:08]** inside. There are chips running, little things that run on there, which

**[00:32:12]** partly connect to the internet and other things.

**[00:32:14]** All of that, of course, can in principle also be reverse-engineered now.

**[00:32:18]** So that means old products I may have at home, where a software provider

**[00:32:23]** or the product manufacturer from back then says, you know what, the device, your old fridge,

**[00:32:28]** or something else, that's no longer maintained, there's no more update for it, something else

**[00:32:32]** for.

**[00:32:33]** All these topics can now basically be, whether it's that some connection

**[00:32:37]** is there, can also be reverse-engineered, and I can write my own software again

**[00:32:41]** for other things.

**[00:32:42]** For example, I've got a small box lying around here somewhere from a larger provider.

**[00:32:47]** Back then, some more bad than good pseudo-AI voice ran on it, which wanted to answer me.

**[00:32:55]** They're good, though, because they have a nice ring that lights up when you talk to them.

**[00:33:01]** For their size, they actually have decent quality in the speaker, too.

**[00:33:07]** I'm now simply going to, well, reverse-engineer that thing, and put my own AI variant

**[00:33:13]** on it, and connect it with my Second Brain and so on.

**[00:33:15]** to then, in principle, build it here in the household.

**[00:33:17]** I think that's a bit cool, you know, I paid for this product years ago.

**[00:33:21]** paid.

**[00:33:22]** I think that's a bit nerdy too, but that's...

**[00:33:23]** Yes, but it's awesome, you know, I briefly considered it, because I wanted

**[00:33:28]** to finally build a physical product with AI here for once, and had

**[00:33:32]** already again looked around for, you know, which microphone to buy and which

**[00:33:37]** I then buy a 3D printer too, so that I can basically pack this microphone into the speaker, into a great 3D case.

**[00:33:44]** Yes, that was again one of those things that somehow feels like a huge project again.

**[00:33:50]** So then I stumbled on something else through this reverse engineering business and thought, well.

**[00:33:55]** I'm not going up there. I'll just look at this device from the manufacturer, whom I won't name now, that I have here at home

**[00:34:02]** and see whether I can't figure it out with Claude's help too.

**[00:34:06]** The device is already decades old, and this could finally get it fit again.

**[00:34:09]** Otherwise we wouldn't be using it anymore.

**[00:34:10]** Accordingly, I actually find that quite nice, then,

**[00:34:14]** that you can, you know, breathe new life into old hardware like that.

**[00:34:19]** That's also one of those things.

**[00:34:20]** So just now we talked about

**[00:34:21]** how I can personalize software,

**[00:34:25]** that I can adapt it to my needs.

**[00:34:27]** And that goes further.

**[00:34:28]** I can actually also, well, do hardware,

**[00:34:30]** in ways it was perhaps never intended, or perhaps with that one device. I mean,

**[00:34:34]** everyone probably knows this, whether you have a smart vacuum cleaner, a fan

**[00:34:39]** or whatever else in your household. The software solutions, the apps,

**[00:34:44]** that the manufacturer partly provided for them were sometimes only so-so,

**[00:34:48]** to be honest. For one or another that's perhaps yesterday's news

**[00:34:53]** again, because we can simply go and say, on this hardware solution

**[00:34:59]** that I have there, I'll just build my own ventilation software in my

**[00:35:04]** own design, with my own [unclear]. And then I think what I see is just awesome.

**[00:35:08]** And I can maybe look at my own house in 3D, and see where the

**[00:35:13]** various devices are currently using which energy, which airflows they produce,

**[00:35:17]** whatever. That's simply nice. I was just thinking, I'm sitting here in front of

**[00:35:22]** one of those Dyson hot-and-cold air gizmos, what I could do with you while I

**[00:35:29]** have my little kids' AI bot running on my watch. I wanted to show such a small prototype to the colleague once

**[00:35:37]** along the lines of, oh yes, look, it can answer questions here in a child-friendly way, and such a

**[00:35:42]** thing. Not because I wanted to release it, but he had the idea to make something there, and then

**[00:35:47]** I thought I'd knock together a prototype for him so he can see how it feels.

**[00:35:51]** Different topic, I don't want to digress, but that too is simply a source of possibilities. But

**[00:35:56]** But, that's like, how do I put this properly, so as not to get into trouble

**[00:36:01]** with it, so that I like it hot again, the village put it that way. [unclear]

**[00:36:04]** Access to education, access to opportunities, access to tokens, access to good models

**[00:36:12]** increasingly decides what you're enabled to do, and where you maybe

**[00:36:19]** get to know something but can't do it, or where you maybe don't even know

**[00:36:23]** that it works like that. So I mean, we mustn't think here, just because we

**[00:36:28]** have a podcast and talk about how here Vertex is copied for PowerPoint and

**[00:36:33]** lofty pontificating about what that means for software development and how processes

**[00:36:37]** change, out there there are still people who, on the one hand, I'd say first, are receptive to it

**[00:36:42]** are along the lines of, I can save a subscription price that would be very hard for me to

**[00:36:48]** afford from my wallet, or those who only really see the results and

**[00:36:53]** maybe can judge again, what that means socio-politically, simply

**[00:36:56]** using it, simply applying it, who knows what tools and solutions there will be in the future

**[00:37:00]** or simply not catching any of it at all, because they're cut off

**[00:37:04]** from enablement and access and I have no idea what, regardless of age, money or region

**[00:37:11]** in the world. I think the scissors of knowledge and possibility will

**[00:37:17]** cut in even harder, more than just, you can't see my air quotes,

**[00:37:23]** so I'm mentioning it, more than just the question of which parental home, with which

**[00:37:28]** you were equipped as a young person, or whatever, to get access to

**[00:37:32]** such things. Now all of that is somehow getting much, much more extreme.

**[00:37:36]** Yes, definitely. Yes, totally. I mean, I also had, in parallel, from the

**[00:37:42]** [name unclear], again, whom we have also already quoted once or

**[00:37:46]** twice on the show, who is also a bit of the

**[00:37:49]** namesake of this Second Brain topic, a tweet

**[00:37:52]** I searched for, which unfortunately I didn't find so quickly, I

**[00:37:54]** had to look it up again, that's how it went, and therefore I don't want to

**[00:37:56]** state the numbers too exactly now either,

**[00:37:59]** because I'll get it wrong anyway, but it was a bit about

**[00:38:01]** him saying that we're of course still early on, that

**[00:38:04]** means, and we're a small group, we will, we have

**[00:38:07]** by now, I think, admittedly, that there's a billion

**[00:38:10]** people with access to AI, but that billion is then also more in the area

**[00:38:16]** of chatting.

**[00:38:17]** And then there's another small group that deals with writing code

**[00:38:22]** and another small group that maybe deals with the agentic topic

**[00:38:26]** and then another small group that basically says, yes, we

**[00:38:29]** also need to rebuild all software again, sometime.

**[00:38:31]** Yes, what we're describing right now of course has to do with it, first, whether

**[00:38:38]** I'm privileged enough to have the time for it, to deal with the topics,

**[00:38:42]** how I basically am, either through the company or in private life, that one

**[00:38:46]** can in principle afford all these things too, no question at all, that is

**[00:38:50]** of course completely fine, but despite all that, the needle is of course shifting in

**[00:38:56]** the direction that more becomes possible with it anyway.

**[00:38:59]** We've just described that we can say software too, which

**[00:39:03]** I until now had to buy, also costs money.

**[00:39:06]** And if these software solutions, which I no longer have to pay a lot for, because,

**[00:39:12]** whether I now reverse-engineer them and then get the same product more cheaply,

**[00:39:15]** or with AI can build something in between, which perhaps saves time and money,

**[00:39:19]** because I don't first have to load a Word document, or whatever Drive document, back and forth

**[00:39:26]** had to convert into a PowerPoint, a presentation, and afterwards from that became a

**[00:39:30]** requirements document, which afterwards a software developer again turned into code in another

**[00:39:34]** program. That's not weeks and days of work either, that went

**[00:39:39]** into it. Such things are then of course, possibly, in the situation for

**[00:39:45]** someone who until then didn't have the show [unclear]. He of course then actually has to

**[00:39:50]** spend money on tokens, but that's by far much less than he would have spent

**[00:39:55]** if he had sat down and said, now I want my own app

**[00:39:59]** for my flea market or for my flower shop. Then it would also have cost 10,000 euros

**[00:40:05]** yesterday. Today and tomorrow, of course, that's maybe a few hundred,

**[00:40:11]** if that, maybe even only 10 euros in token costs that he has to generate,

**[00:40:16]** to build his solution. So I think, yes, you're completely right, that still exists in

**[00:40:21]** principle, that we have a gap there. But that gap is closing, in my opinion,

**[00:40:27]** more through AI than through anything else. And people may now stone me for it,

**[00:40:33]** but I think AI can really help there. Before they stone you, I want to plant an image

**[00:40:37]** in everyone's head. You just gave me an aha moment. No, we didn't

**[00:40:44]** shower during this podcast, but while you were speaking, I suffered a mental

**[00:40:50]** relaxation. And an idea came to me that I'd test with Rea. So could,

**[00:40:56]** or you put it like this, I know someone who would then try it out,

**[00:41:02]** if it were so. Imagine, you say, there are these code management systems,

**[00:41:08]** let's call it Git, as an example. And there are systems like OneDrive, Dropbox, Box.net.

**[00:41:14]** What if you asked the system, let's do something like

**[00:41:20]** file management with Git functionality, so versioning that's so easy to access.

**[00:41:26]** I think that would be something where the nerd heart could be really happy there. Let's see what comes

**[00:41:32]** out of it. I think we should always do an episode, not along the lines of, what have we

**[00:41:35]** rebuilt, but what little helpers have we actually built for ourselves? What skills

**[00:41:41]** do we actually use in our AI system? We should definitely do an episode

**[00:41:44]** on that too. I've also said that very often, I have to apologize again. It's

**[00:41:48]** probably the late hour. In truth it's 10 p.m., I'm an old man, I have to go to bed.

**[00:41:52]** Should definitely happen again too. But before we do that. Jens. I started with the sentence,

**[00:41:58]** Jens, is that you? You confirmed it. We also suspect, because of the microphone business,

**[00:42:05]** that we've picked that up. If you allow this assumed sphere,

**[00:42:11]** which games would you cross? I have an idea. You have an idea of what I would cross,

**[00:42:22]** or do you have an idea of what you'd cross? I have an idea of what I'd cross. Okay,

**[00:42:27]** good, then let me think for a moment. And then I'll pass the ball back first,

**[00:42:32]** because the question is so good that I don't want to answer off the cuff right now. To me

**[00:42:36]** the answer also came to mind while I was asking, yes? I would... Warning, totally boring.

**[00:42:42]** Maniac Mansion and Zak McKracken. Why?

**[00:42:47]** Maniac Mansion and Zak McKracken. Okay, interesting.

**[00:42:50]** Why? In Maniac Mansion you had a chainsaw. In Zak McKracken, the fuel for the chainsaw was in the camper on Mars.

**[00:43:00]** But there was no chainsaw.

**[00:43:02]** I'd really love to see what you could do with the chainsaw in the game.

**[00:43:06]** So I'd like to cross those games.

**[00:43:08]** Are you sure there's no chainsaw in the bug?

**[00:43:09]** Okay.

**[00:43:10]** Yes, yes, okay.

**[00:43:11]** Yes, yes.

**[00:43:12]** So.

**[00:43:13]** You're back now.

**[00:43:14]** But couldn't you in Zak McKracken, on one of those game consoles, play Maniac Mansion

**[00:43:19]** [unclear]?

**[00:43:20]** Yes, but you can't bring the fuel in there.

**[00:43:23]** That's true.

**[00:43:24]** That's true.

**[00:43:25]** Yes, yes.

**[00:43:26]** Okay.

**[00:43:27]** Good.

**[00:43:28]** I would have thought more of something like that.

**[00:43:29]** And that was in Edgar's room.

**[00:43:30]** Mm-hm.

**[00:43:31]** Whatever.

**[00:43:32]** Yes, I'd have rather gone with...

**[00:43:35]** No, right, wrong, it was Day of the Tentacle where that worked, that wasn't...

**[00:43:38]** Ah, okay, okay, yes, very good, you saved us from the Puzzle Shack.

**[00:43:42]** I'd have crossed something like that, I'd have one, I'm a big

**[00:43:48]** fan of Manor Lords, it's still in the, in the early, that kind of simulation game,

**[00:43:54]** where you build medieval worlds, yes, it's still in early access, accordingly

**[00:43:59]** not quite finished and therefore always a bit limited. I'd cross that with a

**[00:44:05]** yes, interestingly, with a global simulation, like SimCity or something like that.

**[00:44:18]** You know how you can say, because in Manor Lords you can more in a small

**[00:44:21]** area, very, very small, down to the individual farm, and decide what on the individual farm,

**[00:44:26]** in the backyard, so to speak, whether chickens or pigs are raised, looked after and cared for

**[00:44:32]** or whether carrots are grown there, with a bigger world simulation, where you

**[00:44:36]** can then basically conquer the whole planet bit by bit.

**[00:44:41]** That's what I'd combine, I'd find that very, very nice, because there's always only

**[00:44:44]** one of the two.

**[00:44:45]** You know, where you either move the big troops on the very large level, on a hex-grid level,

**[00:44:48]** and then the cities only get simulated very roughly

**[00:44:52]** can you?

**[00:44:53]** the two of them properly. That's what I'd do, for example. But only because you asked me like that,

**[00:45:03]** if you had asked me what I'd want to learn from the reverse engineering approach

**[00:45:10]** to then make a really new, awesome game, then it would more likely be

**[00:45:14]** some really cool space simulator with combat content, which doesn't exist yet in that form

**[00:45:20]** yet, in fact I'm currently considering whether to build such a game of my own,

**[00:45:25]** because interestingly, we also talked about that in the Gamescom episode, through the topic of

**[00:45:31]** reverse engineering, the momentum in the games industry is turning. In this episode we

**[00:45:36]** talked about how the games industry is still proceeding very, very cautiously with the topic,

**[00:45:40]** how much software may be developed with AI, and how to even deal with it also in

**[00:45:45]** public, because there has been super backlash from the gaming scene so far

**[00:45:48]** because players didn't want so many AI-generated contents in there.

**[00:45:52]** Now players suddenly think, wow, what's possible there? I can basically take Super Mario

**[00:45:58]** and walk around in some shooters, which is fun after all, and then play it freely in the

**[00:46:03]** browser world. Microsoft was among the first to react, Microsoft's lab is going all in

**[00:46:09]** on this topic and wants to look at it really quickly, so that one can say,

**[00:46:12]** how can we actually now, from our games,

**[00:46:15]** that we've released, make game combinations available much, much faster in principle,

**[00:46:18]** to create new things with players, so a lot is happening right now. You have creators

**[00:46:24]** who basically generate their own game worlds. And I think the games industry will now also

**[00:46:29]** adopt that very, very quickly. And it's usually the case that, when the

**[00:46:36]** old software, games are software too, but the old software houses with normal

**[00:46:40]** software for regular people, and games were always a bit of something different. I

**[00:46:43]** think we'll first see the cool ideas in the games industry, in the media industry,

**[00:46:49]** and then, half a year later, a year later, they can also be transferred to the regular software industry

**[00:46:54]** as well. So much for that for now. First of all, what was the

**[00:47:00]** game with the AI and the humans that you showed me recently? The AI with the humans,

**[00:47:05]** I showed you many of them, I don't know. AI-human work and AI-human

**[00:47:12]** working was it. Maybe it'll come back to me at some point.

**[00:47:16]** It was just that I thought I wanted to check that again, so

**[00:47:18]** sorry, that's a private question. At this point, perhaps, we just had it, when

**[00:47:23]** Microsoft is dealing with it, it's still a question of licensing, so it's

**[00:47:27]** not a call along the lines of legalizing it, rebuild and mix whatever you want.

**[00:47:32]** Yes, so from that side, as I said, no legal advice, no call

**[00:47:36]** to commit crimes or anything like that. Just that

**[00:47:40]** is happening out there. I also think that what you said, that it's in the

**[00:47:45]** games industry, is well founded. If you had asked me, what would you build for

**[00:47:50]** a game, then I would have picked up on what you once

**[00:47:54]** mentioned, whether game interfaces won't become interfaces for AI systems, whether

**[00:47:59]** one couldn't say, take Maniac Mansion, SimCity, and make

**[00:48:05]** an interface for you out of it, so for Claude or something like that, I would have found that quite

**[00:48:11]** exciting. But before we talk ourselves into trouble, Jens, time can't be

**[00:48:16]** reverse-engineered, as of today. We're at 49 minutes on the clock now. I'd say,

**[00:48:23]** we'll put a little button on it, maybe a bigger one too, maybe a colorful one,

**[00:48:28]** a pretty one, whatever. We could maybe reverse-engineer that too.

**[00:48:33]** No, there's no need. We've done enough of that today. We'll build it with the 3D printer.

**[00:48:36]** Whatever, you wanted something physical. I'm looking forward to your game. I'm just as

**[00:48:40]** much looking forward to the next episode with you. And Jens, at this point I'd say, let's say goodbye

**[00:48:45]** to our viewers, listeners, whoever. If you liked the episode,

**[00:48:50]** leave a like. Promote us, tell others about it. The more people hear from us, the more

**[00:48:55]** can share in our intellectual [unclear]. If you liked it, tell

**[00:49:00]** your friends. If you didn't like it, tell us. And at this point we wish

**[00:49:05]** you a lovely day. Until next time. Ciao. Ciao, ciao.

**[00:49:09]** Welcome to Think Different. Think AI., the podcast by Mark and Jens. Two tech-loving

**[00:49:18]** minds who don't just talk about artificial intelligence, but live it. Here

**[00:49:23]** you get clear classifications, real practical insights and a fresh look at what

**[00:49:28]** is possible. Understandable, critical and always with a wink.

**[00:49:33]** AI to think about, to smile about, and above all to join the conversation about.
