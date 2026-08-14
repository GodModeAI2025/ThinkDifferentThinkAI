---
title: "Age of Agents"
episode_index: 29
published: "Mon, 02 Mar 2026 20:36:55 +0000"
duration: "3152"
audio_url: "https://audio.podigee-cdn.net/2381794-m-d7c482dddf5cf5c319f57e1e2fa44ea1.mp3?source=feed"
guid: "16286dd4ee583068998983e6167ed0ba"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T21:00:33+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/029 - Age of Agents.md"
translated_at: "2026-04-29T12:38:44+00:00"
---

# Age of Agents

**Published:** Mon, 02 Mar 2026 20:36:55 +0000
**Duration:** 3152
**Audio:** https://audio.podigee-cdn.net/2381794-m-d7c482dddf5cf5c319f57e1e2fa44ea1.mp3?source=feed

## Description

How gaming UIs are revolutionizing the future of AI orchestration and why this changes our thinking.
In this episode, we take you on a journey through the new era of AI agents. We discuss how classic chat interfaces are reaching their limits and why inspiring approaches from the gaming world could be the key to controlling and understanding complex agent systems. With a dash of humor and plenty of practical examples, we show how visual interfaces and orchestrated AI agents redefine working and decision-making. We talk about current developments, ethical questions, and why the skills of strategy gamers are suddenly in demand in business. Tune in to find out how the future of human-machine interaction really looks and how trust becomes the biggest challenge.

https://x.com/tom_doerr/status/2027791060873711658?s=46

https://x.com/alexfinn/status/2024169334344679783?s=46

https://github.com/pablodelucca/pixel-agents

https://x.com/idosal1/status/2021661865588535599?s=46

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here you will find clear classifications, real practical insights, and a fresh look at what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** KDI for thinking, chuckling, and especially for joining the conversation.

**[00:00:33]** Hello, welcome back to a new episode of Think Different, Think AI.

**[00:00:38]** Today with the well-known and always present Mark Zimmermann

**[00:00:43]** and my person Jens Scharnetzki.

**[00:00:46]** I am ridiculously happy that we are making a really cool episode today,

**[00:00:50]** which I have wished for a long time, titled Age of Agents.

**[00:00:55]** You know what I think is great?

**[00:00:57]** I believe we have mentioned our first and last names for the first time.

**[00:01:01]** Crazy, right? That I have both and both are correct...

**[00:01:03]** Hansin! Yeah, probably people are hanging up now and saying,

**[00:01:05]** oh, that's them!

**[00:01:06]** No, I don't hear myself in that.

**[00:01:07]** I just don't find it appealing.

**[00:01:09]** The two of them are crazy, no.

**[00:01:10]** Yeah, no idea why.

**[00:01:11]** It's just the way it came to me.

**[00:01:13]** I thought we should make an episode.

**[00:01:15]** Uh, yeah.

**[00:01:16]** Age of Agents.

**[00:01:18]** It’s of course a little reference to Age of Empires

**[00:01:21]** and other games.

**[00:01:23]** It’s also a little hint towards what we will be talking about today.

**[00:01:27]** In this episode, we will mainly talk about the design of surface-user, surface-UIs,

**[00:01:37]** user-faces, whatever you want to call them, that function in a similar way

**[00:01:43]** to games, in order to control larger amounts of agents.

**[00:01:49]** Before we do that, let's touch on some current topics, what we've been up to in the last few days, since we don't need to check the fluff,

**[00:01:58]** fluff check is unnecessary. We have hardly messed up in recent weeks and months.

**[00:02:01]** Yeah, we are just too good.

**[00:02:03]** Where we are, is perfect.

**[00:02:08]** Yeah, there’s also an almost perfect prediction that has happened in the last few days.

**[00:02:13]** You wanted me to count something, Mark.

**[00:02:16]** So it's not humorous in that sense, but nonetheless, I would say it's impressive,

**[00:02:23]** that Croc, we know it, yes, Elon’s favorite AI, predicted the attack on Iran very accurately

**[00:02:31]** in terms of timing, I couldn't help but

**[00:02:38]** write a post that said, Croc predicted the timing well, but

**[00:02:45]** this happens when the Pentagon uses Croc and forgets to switch our data not

**[00:02:50]** to be used for training the model, probably everything

**[00:02:55]** is not right.

**[00:02:56]** But I still found it somewhat ironic when the War Department uses Croc and

**[00:03:04]** for the average person Croc makes a pretty accurate prediction about the timing of

**[00:03:09]** yes, that’s already interesting.

**[00:03:11]** battles or activities, or however you’d want to call it now.

**[00:03:15]** Yes.

**[00:03:16]** It predicts beforehand.

**[00:03:17]** That's true.

**[00:03:18]** It’s, as I said...

**[00:03:21]** even if these events are horrible as they are,

**[00:03:24]** but it also shows this topic we’ve brought up before,

**[00:03:28]** security or not,

**[00:03:30]** this thought of having really forgotten to switch

**[00:03:33]** it on or not, whatever happened there,

**[00:03:35]** remains to be seen.

**[00:03:37]** But the Department of War has produced other AI news in recent weeks.

**[00:03:46]** There was still quite a bit that had the AI community excited.

**[00:03:53]** On one hand, there was the case that was made public last week, or was in many

**[00:03:59]** media, that Enttrophic, with its CEO Dario, said they want to collaborate with the

**[00:04:09]** Department of Defense, or how did you actually say it? I just said it

**[00:04:14]** correctly. Department of War. Exactly, because they were not secure about it.

**[00:04:21]** it can be, that the AIs, if they also hand over the models openly to the Pentagon, that the

**[00:04:27]** are not used to conduct mass surveillance, nor to

**[00:04:32]** be used to actually independently finalize weapons in combat operations,

**[00:04:42]** thereby also killing people and something else. That could not be promised.

**[00:04:47]** Accordingly, he did not sign the contract, did not say,

**[00:04:52]** I completely reveal myself and give my model completely free for you. As a result, I think he got kicked out of everything. That is, I believe, some 200 million dollar contract.

**[00:05:01]** I believe Trump and Co. immediately posted that one must absolutely not use it, that no employee should use a trophy anymore, because it's now a devil's tool and I think this has also been put on the

**[00:05:11]** list of

**[00:05:13]** risks or something. What is happening there is quite massive.

**[00:05:22]** One must mention it. I mean, that is my word now. Yes, I am allowed to enter the States. Thank you.

**[00:05:30]** And then one must know on the other side that the attack

**[00:05:34]** was directed at Ela, which is being viewed as an operation, whether one approves of it or not, but it was relatively

**[00:05:40]** successful in that sense, so to speak, well executed in that regard,

**[00:05:47]** that things went well from the perspective of the Americans and the idea they had back there.

**[00:05:52]** This was also helped by the Trophy Cooperative. The AI actually helped out quite a bit

**[00:05:57]** apparently, from what has become known, which makes it even more astonishing.

**[00:06:00]** But there is not just one AI successor in this world, another is directly in the

**[00:06:07]** jumped into the breach, I would say. Our dear Sam from Open AI. He then

**[00:06:14]** announced shortly afterward that he would sign the contract with the Pentagon, with the Department of Defense

**[00:06:21]** and that it wouldn't be a problem at all. They would adhere to the fact that

**[00:06:25]** essentially, no mass surveillance would be implemented, although that is somewhat

**[00:06:31]** amusingly worded. So Sam's tweet is kind of strange,

**[00:06:35]** the community reacted a bit oddly to it. I don't know if you've noticed

**[00:06:37]** I read through a few things, a few comments. People aren't quite

**[00:06:40]** convinced whether the way Sam wrote it in that

**[00:06:45]** tweet actually means that he's saying nothing other than, well, the actual law

**[00:06:51]** states anyway that this cannot be done, that there cannot be mass surveillance

**[00:06:56]** permitted by the police, and that no autonomous weapon systems are allowed in that sense

**[00:07:00]** give, the self-employed should decide. The way he expressed it is actually

**[00:07:05]** interpretable in such a way that we say, well, as the sender says, then of course

**[00:07:11]** then some general can still decide as a human in the loop, that but a

**[00:07:15]** million drones can now actually decide for themselves whether to attack someone

**[00:07:19]** or do something else.

**[00:07:20]** So that's a bit what the drone Rupus means.

**[00:07:23]** Yes, it's really a bit wild and he also presented it in his tweet so

**[00:07:27]** that this is a totally cool solution, this contract he made

**[00:07:30]** that can now also be offered to all other AI companies, which then

**[00:07:33]** somehow totally becomes an issue because one thing that Entophic with Dario rejected,

**[00:07:39]** is supposedly because Sam then simply comes up with the exact same contract, that has now just

**[00:07:44]** well, so it becomes a bit of a topic where we have to say, but this has to be

**[00:07:46]** observe how it develops further. What we see in the teeth, I don't know,

**[00:07:52]** if this is the case for everyone, but what we see in the teeth is that very, very many users

**[00:07:57]** have been happily switching from Open AI, from GPD, to Cloud, to Entrathic since this news.

**[00:08:07]** And I believe there is even a functionality now for this, that what was basically

**[00:08:13]** a bit difficult before. I mean, if he ever moved from his Spotify account

**[00:08:18]** to an Apple Music account or vice versa, transferring playlists is quite

**[00:08:23]** sometimes a bit tricky. You sometimes surprisingly need an AI-for or a

**[00:08:31]** software solution or something like that.

**[00:08:34]** With

**[00:08:35]** AI relocations, I have also always thought about it, I now have a lot of knowledge, basically my ChatGPT has revealed, yes.

**[00:08:42]** Now to move with it, I was already afraid I would have to copy all the threads somehow and copy the rober

**[00:08:48]** into another AI, but I believe there is another solution, there's somehow an export or something.

**[00:08:52]** There are actually two solutions by now. You can both in ChatGPT itself say, I want a copy of my data and then you get a hint,

**[00:09:01]** so to speak, when it's ready, you'll get an email and then you have an email and a link and then you can click, you get a zip.

**[00:09:08]** I can recommend everyone to do this, regardless of whether you want to switch or not, because then you first see what they actually have collected about you,

**[00:09:18]** which is not so little, and if you don't take this function, because everything is actually included,

**[00:09:26]** what you have chatted in your life, files and chats and whatnot,

**[00:09:32]** if you want that a little bit more compressed, Claude offers you a relocation function,

**[00:09:39]** not that you just press a button and then he talks to Chatchivity, but he gives you a prompt.

**[00:09:45]** A prompt that instructs the AI system to disclose data about you in a structured form.

**[00:09:52]** And then you basically have a prompt window in ChatchiBT.

**[00:09:56]** You copy your prompt out, don't go into ChatchiBT in Cloud, you have a prompt.

**[00:10:02]** You can copy that, go into ChatchiBT, and enter the prompt.

**[00:10:05]** The prompt instructs ChatchiBT to fill this out based on knowledge.

**[00:10:09]** You take the result, copy it back into ChatchiBT in the Cloud.

**[00:10:13]** back to Claude. Man, too many words with looking and then he can basically his memory

**[00:10:21]** about you. But one has to say, if you export this in ChatGPT at OpenAI via

**[00:10:28]** the data export, it's much, much larger, much, much more powerful. For that you have

**[00:10:33]** the problem, how do you play this back in? Because it definitely doesn't fit into the

**[00:10:38]** small text window that Claude would actually offer you for that. But those are

**[00:10:42]** both ways that work. And I have to say here, the Chat-GPT moment started for me with AI,

**[00:10:50]** but at the moment I have no active subscription with Chat-GPT, because I actually find,

**[00:10:56]** the models and the offered functionality right now are not state-of-the-art, which however

**[00:11:03]** really doesn't change, was state-of-the-art. But everyone can decide that for themselves,

**[00:11:07]** whether politically or idealistically motivated, or for technological reasons,

**[00:11:11]** usability reasons, at which motel it is. There are definitely ways to

**[00:11:14]** transfer that. I find it a bit unfortunate, since you were just talking about that, that it

**[00:11:17]** basically, I know that the topic of context windows is just difficult

**[00:11:20]** for an AI, to copy in too much content. But honestly, it wouldn't be

**[00:11:25]** that hard to say, even if I receive something there,

**[00:11:28]** that I first split the content of this file. So I have

**[00:11:33]** often found myself in situations where I copy something in and still get

**[00:11:36]** one of those error messages today saying, but that is

**[00:11:41]** too long at that moment. I actually find that a bit unfortunate, but there is still no

**[00:11:43]** solution to say, okay, I'll just cut that part off and put it in

**[00:11:47]** put in the second prompt machine. I shouldn't have to do that as a human, honestly.

**[00:11:50]** and so that almost hits me a little again.

**[00:11:52]** We're maybe slowly getting to the topic

**[00:11:54]** Orchestration and that kind of thing, but what I actually find astonishing

**[00:11:57]** is how quickly also the way you say is

**[00:12:01]** is spoiled. So something like Claude creates nice Excels, Power Points. You get Markdown

**[00:12:09]** files, then it continues in ChatGbt, you start there, that just had a preliminary meeting for me,

**[00:12:13]** then you start in this kosher html thing and try to copy that out and

**[00:12:18]** then it gets interrupted and then yes Gemini reacts differently somehow.

**[00:12:23]** I also gave this prompt to Gemini. Like, look up everything you have from me.

**[00:12:27]** Gemini then said, what do you mean, I don't know anything about you.

**[00:12:30]** Yes, where I then thought, what is this? I've been using it for half a year, what is going on here?

**[00:12:34]** Yes, so you've really gotten used to it, and I also find the philosophies behind it quite interesting,

**[00:12:38]** yes, with Gemini, that's James, while this is block the last room. And with Open Air

**[00:12:43]** it's called Skilds and with JetGPT it's called no Ahnowatt, yes, up yours, the thieves,

**[00:12:49]** that's all somehow very different. And in between comes Croc, who answers

**[00:12:54]** some very nice chemistry questions and questions about the American invasion or questions

**[00:12:59]** about X from Reddit, but otherwise he's a bit, I would say, well, I don't really know.

**[00:13:04]** So Supercrug and Heavy-Crug haven't convinced me so far.

**[00:13:09]** Yes, and that's why it's even more important that we, let's say, I would have

**[00:13:12]** a bigger reading again and then we can smoothly transition to the topic.

**[00:13:15]** So the models are increasingly becoming about comedy, so about the topic, what

**[00:13:19]** is actually not so important anymore and interchangeable at that moment, but

**[00:13:23]** the combination of the model weather is more interesting. Well, how can I orchestrate that

**[00:13:27]** with various agents, we keep saying, it's no longer just the model,

**[00:13:33]** it's the skills that are perhaps important, what I do locally, what I might

**[00:13:37]** do in the cloud, so this combination of topics is becoming increasingly important and the

**[00:13:41]** usability of that is becoming more critical. And we are slowly getting to the topic of today's

**[00:13:46]** show, because we have actually called it the Age of Agents, saying that we have

**[00:13:53]** for a long time thought that the main interaction with AIs, whether it's Weibkohle

**[00:13:59]** or something else or just asking how my next trip is, would be the chat window and

**[00:14:03]** the pure chat, but somehow that has surpassed itself. Ever since, basically, an AI is no longer just

**[00:14:10]** a prompt and an answer, so my prompt and the answer, but that it actually

**[00:14:13]** persistent is that it performs actions. That's a certain API action, whether I

**[00:14:20]** now have with the workflow system that you also sometimes like to use. There are

**[00:14:24]** tool calls with existing packings being triggered, skills need to

**[00:14:27]** be updated, memory files need to be written somewhere. API actions that

**[00:14:32]** also actually cost no money are performed in the background. So there is

**[00:14:35]** budget consumption, these topics are there. Well, I certainly have an AI that or

**[00:14:40]** an agent who might position himself as the head of the other agents about this

**[00:14:45]** talks about what they have to do and such things. All of that is in

**[00:14:48]** principle now there and leads to the fact that you actually can't handle it over a

**[00:14:54]** can solve simple chat windows but needs something else, something different

**[00:14:57]** Layer needs to process that so we can keep humans a bit in the loop, so to speak. This means chat works well for

**[00:15:01]** keeping us engaged a little.

**[00:15:06]** I need something and get an answer. For a

**[00:15:10]** orchestration, a chat is rather moderately suitable, to be honest.

**[00:15:16]** Before you dive into these new interfaces with all of us, maybe just

**[00:15:22]** briefly, one more overview to what is currently happening and what is

**[00:15:28]** there regarding orchestration, maybe precisely because I would say briefly, Perplexity

**[00:15:31]** has brought you something out, Perplexity Computer, where you’re somewhat back in this text world

**[00:15:37]** albeit with images, but the system doesn’t just try to imitate a bit of Open Clown

**[00:15:41]** like that.

**[00:15:42]** The motto is, I solve tasks and install things, and I do and act, but they actually mix

**[00:15:47]** between Kimi and Gemini and Open AI and Cloud quite casually

**[00:15:54]** and start various activities, depending on which model is active.

**[00:15:58]** can help the best.

**[00:15:59]** Croc has also done something like that, where you have agents warming up and agents that they start and orchestrate separately because there is an orchestrator agent that gives its commands.

**[00:16:15]** And since we were talking about Claude, I mean, Claude has also, when was that, the day before yesterday, I can’t remember again, they started doing something like, okay, you can now plan tasks,

**[00:16:26]** Plan, which means prompts are filled out at certain times, so that they can

**[00:16:30]** send you summaries, create something for you on social media

**[00:16:33]** post, I don’t know, whatever. You can now also operate it remotely,

**[00:16:39]** whether you got a Telegram connection, for example, with Kimi,

**[00:16:43]** so you can write to your friends over Telegram

**[00:16:47]** or with Claude, for example this Remote Claude, that you can chat from your phone

**[00:16:53]** to your computer at home. So everyone is currently making a lot of attempts,

**[00:16:58]** to delight you with orchestration possibilities. But now I will close this circle and

**[00:17:06]** I'm returning back to the broadcasting house. This orientation in these long chats

**[00:17:14]** in Telegrams becomes confusing. If you have five different topics going on,

**[00:17:18]** it's like in a family chat. Then suddenly grandpa writes, where are you and refers to the

**[00:17:24]** message you got three weeks ago. That’s complete madness for these AI times.

**[00:17:30]** And the other thing is, whether it’s perplexed computers or whatever your

**[00:17:35]** interface is, as soon as you have this project list on the left, I don't know how you feel, but I

**[00:17:40]** find it super confusing. Where were you last? What is currently being worked on?

**[00:17:46]** Is this an old version? Is this already a new working state? That's really outdated. From

**[00:17:51]** that perspective, I’m glad about this topic, as you raised it, that other

**[00:17:56]** interfaces give us different possibilities. Yes, definitely. I also believe

**[00:18:02]** that no matter how wild the times are right now and how wild the possibilities are, 

**[00:18:09]** that we have through AI, the UIs that we currently offer to orchestrate these topics

**[00:18:15]** are still very text-heavy, terminal-heavy,

**[00:18:19]** development-heavy, because we also have to say, many things that we talk about in this

**[00:18:24]** scope are again not accessible to everyone. Anyone

**[00:18:28]** can somehow install pipes or something else to then

**[00:18:31]** run certain things, can present a GitHub account to upload topics there,

**[00:18:36]** upload other things. It's all still very, very

**[00:18:39]** development-heavy. I believe there's

**[00:18:41]** just such a gap that needs to be closed, especially when I dive into the topic of

**[00:18:45]** orchestration, which is already in the gaming world, and there are now a few approaches that

**[00:18:52]** have been taken up, that have been closed for a long time, in a very playful way.

**[00:18:57]** I mean, especially the German developer scene has always been very well known for

**[00:19:02]** Construction simulation games. So, I would now consider the big series as the

**[00:19:08]** Anno comes from Germany, the Anno series, which has tons of variants, from Anno you haven't seen,

**[00:19:13]** so Anno you haven't seen, where it’s always about being a manager of a certain

**[00:19:21]** system for people who are not familiar with playing, it often involves

**[00:19:25]** somehow building my little village in the Middle Ages, something else, I have to fell trees,

**[00:19:32]** of course, I also need to add a forester who reforests the trees,

**[00:19:36]** when such a system functions, there are always simple rules, like

**[00:19:39]** sending the miner or something like that.

**[00:19:41]** If I have two tree fellings, then I need a forester, then that is enough, then I can

**[00:19:46]** add the sailmaking and then it works and then my people can eventually

**[00:19:49]** build houses from that.

**[00:19:50]** And so there is a complex fuss going on behind these topics,
 
**[00:19:56]** often these surfaces look like a bumpy picture, that will
 
**[00:19:59]** then in the more modern games, modern is a good word, they look
 
**[00:20:03]** a bit like old games from The Refactory or something, it's really about
 
**[00:20:07]** the orchestration of vast supply chains, factories that I then build to produce optimal products,
 
**[00:20:13]** to produce.
 
**[00:20:14]** The supply chains also need to be optimized, short supply chains that players
 
**[00:20:18]** simulate in the game.
 
**[00:20:21]** So, now back to the lumberjack, he has to walk a few meters
 
**[00:20:25]** to the sawmill, which is smart, it's silly if I have the sawmill on one side
 
**[00:20:28]** of the pixel map and my lumberfalls on the other side,

**[00:20:32]** have.

**[00:20:33]** should be relatively short. So these are highly complex management games that allow us

**[00:20:39]** to really run a highly complex system. That means we

**[00:20:45]** are managing a kind of virtual person in these games who is doing something. And this analogy

**[00:20:54]** was recognized by one or another AI expert who is out there, who

**[00:20:59]** has worked a lot with agent orchestrations, where they pack different agents together,

**[00:21:05]** to solve tasks, whether that's, in the simplest case, three coding agents,

**[00:21:09]** a research agent, and a testing agent who basically just looks at the topic

**[00:21:14]** of what the coding agents are doing, then I might have four or five agents running around, who

**[00:21:18]** I can view in the background through terminal windows, I can control them through chat windows,

**[00:21:21]** I can check what they are currently programming in the project folders.

**[00:21:25]** I can control that.

**[00:21:26]** I can also see the API costs on another website, theoretically, that they produce

**[00:21:31]** or the tokens they are burning in this model.

**[00:21:33]** However, I could represent that just as I am doing in the games, which we have been doing

**[00:21:38]** for decades now, and say, wow, I just have five virtual

**[00:21:44]** agents running around on such a surface where I can perhaps see if they are

**[00:21:49]** currently active or if they are hanging out in the break room of my virtual office that I

**[00:21:54]** built, yes, or if they are burning money or if they are currently programming.

**[00:21:59]** I'm currently imagining how the little agents stand by the oven and shovel the

**[00:22:03]** virtual money in. But what you're saying is really great because

**[00:22:07]** while you were describing it, right? Let's stick with the example, you

**[00:22:12]** had it, I believe, a simple example, the three coding agents are building three apps.

**[00:22:15]** I had a lot of discussions today, yes, I sat down with three apps in parallel
 
**[00:22:20]** and in a world where you're working with text windows. Even though I come from IT,

**[00:22:28]** I don't necessarily find text windows to be the most appealing format. Then you have

**[00:22:33]** three windows open and I noticed that each agent also started the app
 
**[00:22:38]** and validated the app. Then the app opens, and you start working inside it already

**[00:22:42]** just typing around, while it wasn't even finished yet. So it's fundamentally through

**[00:22:47]** overlapping of the windows is confusing. If I now imagine that you don't have all of this in

**[00:22:53]** a text desert and additional windows, but really, as it is in these games,

**[00:22:59]** that you say, okay, you see, up there are the three miners or the three

**[00:23:03]** programmers who are working away in their winter gear. And if they have something where you

**[00:23:09]** might need to do QA or something, then these typical symbols, as they say

**[00:23:14]** you can play. I have a quest for you. You can submit your quest. So you can submit your

**[00:23:20]** task and look at the results. No idea what such mechanics make you think of,

**[00:23:24]** what such mechanics reveal transparency, because I think of those little characters,

**[00:23:32]** that run across the screen, I always think of Lemmings, that's a very old game,

**[00:23:36]** the very old games. Although Lemmings, well, they probably all fell to their deaths,

**[00:23:40]** but it must be much simpler than all of this here in

**[00:23:49]** Zerlich-Grad-What and here something shines blue and yellow and red and green, but at

**[00:23:52]** the end of the day, it's still just text. Exactly, let's travel out of such a

**[00:23:55]** situation, in which we often find ourselves as knowledge workers,

**[00:23:59]** staring at a monitor and doing something,

**[00:24:01]** when I say, if I'm going to sew a complicated factory alone, that

**[00:24:06]** I say, I have a factory plant that does chemical processing

**[00:24:09]** something else. So the control room of this factory is then

**[00:24:16]** also not a terminal window at that moment. Individual steps are of course programmed down,

**[00:24:21]** all the software solutions, the individual conveyor belt, that's all of course program code,

**[00:24:27]** programming, the orchestration of it is actually maybe represented again as

**[00:24:31]** a map, as a control chart that I have somewhere, where red lights

**[00:24:37]** light up when some production chain fails, so that I know I have to look there, whether

**[00:24:41]** afterwards, what went wrong, whether the software is wrong or something has

**[00:24:44]** fallen into the conveyor belt, whatever, it doesn't matter, but this...

**[00:24:48]** It does matter, but you have gained attention.

**[00:24:52]** Yes, and that is definitely the attention. But this, I think we humans have to abstract.

**[00:24:58]** We do that as we develop language, we develop other things, we abstract

**[00:25:03]** in principle of course, and that is the same with complete situations, we need to abstract.

**[00:25:08]** So I wouldn't say, I'm glad that there is in principle a visual

**[00:25:11]** representation of a radar in a, in an airport tower and not just

**[00:25:16]** lines of program code standing underneath each other that I somehow have to calculate or read

**[00:25:20]** through to see which 50 is currently the case, but that people can visually recognize,

**[00:25:23]** oh, a plane is coming from the left or another, it might be a bad

**[00:25:26]** idea that they are both on the same runway now. So, that means we humans are

**[00:25:31]** So it is not usual, it is our preferred means in complex systems,

**[00:25:37]** to abstract things, to represent them differently, to represent them as visually as possible, to not have in context

**[00:25:42]** there.

**[00:25:43]** We are indeed speaking about visual interfaces in complex matters endlessly.

**[00:25:49]** everywhere.

**[00:25:50]** And such complex relationships are really extremely represented in games.

**[00:25:55]** So far, there haven't been any AI components in the background, but if you

**[00:25:59]** now have a real-time strategy game or any other game like Starcraft or

**[00:26:03]** the big games that exist, there are really often thousands of

**[00:26:08]** units that are produced somewhere in factories, these are all supply chains

**[00:26:12]** troop movements, combat actions represented on a map with other visualizations where

**[00:26:17]** represented, this is a very, very complex system that is influenced by humans

**[00:26:23]** the presiding, so the Human Invaluable, or maybe already in this case Onvaluable, we can

**[00:26:29]** perhaps delve a little into the two terms that are also floating around a bit in the

**[00:26:31]** AI discussions regarding this complex matter in various

**[00:26:36]** can orchestrate zoom or abstraction stages, because it is visually represented. And that is

**[00:26:43]** actually a bit of what perhaps the near future is. When we talk about

**[00:26:49]** how we will engage with agents, especially with the

**[00:26:55]** orchestration of agents, that

**[00:26:57]** such game UIs might gradually become more prominent

**[00:27:01]** and also the business applications that we have.

**[00:27:03]** Because I can quite well imagine how

**[00:27:06]** you wrote it just now, whether I now say, now
 
**[00:27:08]** I have that, I can observe a coding window like that the whole time,
 
**[00:27:12]** of course, and wait until eventually I get an
 
**[00:27:14]** error report, but I can of course also

**[00:27:16]** similarly take a look again somewhere at the

**[00:27:19]** virtual office and see that one of my agents is waving a caution sign

**[00:27:24]** all the time to get my attention, because he might be basically waiting for

**[00:27:29]** some input from me. This is a much quicker way to recognize when I then

**[00:27:35]** dismiss it again. If I say there are maybe 1000 agents programming and ten

**[00:27:41]** of them have problems, then I might see at that one spot, the virtual location on

**[00:27:45]** my map, called Cologne, Düsseldorf, Karlsruhe, whatever, Berlin, then

**[00:27:50]** the programmers in Berlin, they have a problem right now, then I can maybe

**[00:27:54]** look into that and then I recognize that it's just that one single agent, and then

**[00:27:57]** I can maybe take another look at this code and see why this

**[00:28:01]** one agent has stayed stuck, whether he has a budget problem or a technical problem

**[00:28:05]** or something else at the moment, I think we need something like this, and that’s why

**[00:28:09]** I think it’s great that we are already seeing such things, they are indeed

**[00:28:12]** meant to explain this to you. There are all kinds of things. There is something like Agent Craft, where

**[00:28:16]** I can really play similarly to Starcraft with orcs and so on, they run

**[00:28:21]** around there. These are the agents, I can further build and construct them and such things. There are

**[00:28:24]** indeed very, very many applications, rather small bustling applications, where AI agents

**[00:28:31]** are then depicted in such an office situation. Then really one comes in who is

**[00:28:35]** the programmer, the other one is the researcher, the other is the boss. Then there is the

**[00:28:38]** easel, then there’s the tester who runs around and then they sometimes meet

**[00:28:42]** at the coffee corner and also chat during coffee because they just

**[00:28:46]** have nothing else to do.

**[00:28:47]** Then I can simply say, I’ll delete him now and throw him out, because then

**[00:28:52]** he no longer uses Idol Time or somehow takes money from you.

**[00:28:55]** So, what are the kinds of things that you find instead?

**[00:28:57]** In Baden-Württemberg, they call teachers in the summer phases, in Baden-Württemberg

**[00:29:00]** I believe teachers are always let go during the summer phases and then

**[00:29:05]** reappointed after the summer phases, but that's a different topic.

**[00:29:08]** I think it was like this, so if it's different, please comment, but I'm

**[00:29:12]** pretty sure that this is in Baden-Württemberg, I don't really know how

**[00:29:15]** many other federal states it seems to be the case in one way or another.

**[00:29:19]** What I find quite funny about it while you were telling that

**[00:29:23]** is problems that I've really encountered over the last weeks again and again,

**[00:29:27]** namely, you might know that a lot means a lot when one

**[00:29:32]** once you've had a good experience with a good model, you stay

**[00:29:35]** my good model, yes in my case with Claude, that's Opus. But actually, you need

**[00:29:39]** Opus isn't always the answer. There are, let's say, things where Opus might be a bit too

**[00:29:44]** heavy-duty for the task at hand, and when you're working with it, you don't really

**[00:29:51]** have an immediate sense of how many resources I've just used, or is it

**[00:29:56]** that is necessary. And for both I have an example where I think that such a

**[00:30:00]** interface will probably help us in the future. One topic is,

**[00:30:04]** what I just mentioned about resources, yes, so if you perhaps have time and the progress bar is allowed

**[00:30:08]** gradually move forward, then you can also take another model, because maybe the

**[00:30:12]** other solutions might also need a bit more time. It’s not like you can do everything by yourself.

**[00:30:16]** you decide for yourself, but sometimes you might rely on cooperation from others

**[00:30:20]** Processes have been assigned, and if that, let's say, needs to be finished by 9 AM, then it has to be done

**[00:30:25]** maybe not with the Ladies and Creators and I can do everything and in general

**[00:30:29]** reasoning and maximum and you see what I mean, but maybe the small one will do here,

**[00:30:33]** quickly borrow a helper. When it comes to formatting texts, it's

**[00:30:36]** perhaps a perfect example, but you can still imagine that.

**[00:30:39]** And the other thing is, we had, since you already mentioned tools, we had

**[00:30:43]** worked with a few tools, in this case again in software development, how

**[00:30:47]** to handle different components, so task lists, where it says what the

**[00:30:52]** software developer needs to do or other components with which the developer

**[00:30:55]** normally needs to collaborate, we had all that over MCP, we have

**[00:30:59]** explained that in a podcast before, what that is, it is the

**[00:31:02]** possibility for agents to interact with tools, data provided by the

**[00:31:08]** neighboring system.

**[00:31:10]** And we had taken a very weak AI model, and the AI model said, yes,

**[00:31:15]** so this MCP thing, that doesn't work, so ah, no, no, no, that's

**[00:31:19]** the MCP server, it is broken.

**[00:31:21]** Then we took a slightly stronger model, which said, no, no, super,

**[00:31:24]** the MCP server is running, then it took a little while and then you saw in the chat history

**[00:31:27]** oh yes, I forgot what I wanted. I think that was the goal and just

**[00:31:34]** continue. And when you took the really good model, it already ran through it

**[00:31:38]** from the beginning. So it recognized that MCP had to be running, and didn't do any nonsense during

**[00:31:43]** the MCP communication. And that's how they behaved differently. If I relate that

**[00:31:47]** back to games, then it's similar to the simple character,

**[00:31:52]** that I used, who can then, let's say, carry the tree. And if

**[00:31:56]** it takes a little longer, that's not a problem. Carrying the tree is something she can do. A builder takes

**[00:31:59]** on a master's role. And if you're back in your military exercises, you take

**[00:32:04]** someone who maybe has a sword and a club. And not the one who is currently

**[00:32:08]** holding a tree because he has an advantage on the battlefield, like the odds.

**[00:32:11]** Exactly. And in this way, you can also control faster. So, you say, okay,

**[00:32:14]** if, for example, you were to define zones that would represent a certain security zone in such a

**[00:32:20]** real system. If

**[00:32:23]** an agent then perhaps has the wrong permissions, then he shouldn't even

**[00:32:28]** enter that other zone. So you would also see that, okay, I might have

**[00:32:31]** done something wrong with the security settings of this agent, who simply doesn't

**[00:32:36]** have certain permissions. Did I do that wrong? Because he's now running around here,

**[00:32:40]** where he shouldn't be. So something like that can help. The complexity,

**[00:32:45]** that we might not otherwise see in the system, that is hidden in the prompts, in the

**[00:32:50]** lines of code in the skills that we give to the agents, we can obviously

**[00:32:54]** visualize there. So streamline. That is simply a huge advantage that we have from such

**[00:33:00]** interfaces. Because, as I said, we humans are also visual. We are not only focused on text

**[00:33:05]** we need visual input, that's why we also look for signals, now from

**[00:33:11]** a classic signal design. There, signs are also important, because they are not just long

**[00:33:16]** texts, but basically work through symbolism.

**[00:33:21]** Exactly, symbolism helps. So we also need this abstraction, because then

**[00:33:29]** you can simply react faster in crisis situations. So now in such a

**[00:33:34]** long, so if he somehow becomes prompt to get our result,

**[00:33:37]** that's often already the case, it's always such a wild thing, then the

**[00:33:40]** AI just throws out a five-page response that just scrolls past you,

**[00:33:44]** where you often find yourself going, wow, now I have to scroll back up and such

**[00:33:48]** what. If there's a hidden danger message in there, it could very well be that I

**[00:33:53]** overlook it. So alone, that's not what I wish? Yes, exactly, I wish for example in

**[00:33:59]** such a case a visual hint of a danger. And you can solve that wonderfully with such

**[00:34:06]** gaming interfaces. Mark, I wanted to briefly mention, before we continue,

**[00:34:10]** because I just called it up. I want to briefly address the two terms that I

**[00:34:14]** threw in, human envelope and envelope, to go a bit deeper. Can you briefly

**[00:34:20]** explain them, why they are interesting right now? I find it totally funny because I wanted

**[00:34:24]** to say another sentence just before we get to these terms, from that perspective I now

**[00:34:29]** use the word allocation and afterwards I would like to explain that too. Another point is also,

**[00:34:34]** I find, is the topic of delegation. Now not everyone in professional life is someone,

**[00:34:42]** who distributes work. Some people have a boss who tells them, this

**[00:34:48]** is what I need from you. Depending on what you work on, how you work, that might also be,

**[00:34:52]** I would say, standardized or not, but in the long run, the shorter version is,

**[00:34:56]** the delegation of work, the trust that what is being done,

**[00:35:00]** is good and that it is correct, and the trust in the person behind it is,

**[00:35:03]** one thing. But delegating always sounds so easy, but sometimes it's not always so

**[00:35:09]** simple. And especially, if you are new in a position where you might come to delegation,

**[00:35:14]** it always feels strange. Until now, it was always that I was used to doing it myself.

**[00:35:18]** Now someone else does it. So not according to the definition of what it stands for, that a team

**[00:35:22]** great, someone else does it. No, rather in the sense that you say, okay, I’m giving this

**[00:35:27]** as an order, and when it comes back, yes, maybe there can be further adjustments,

**[00:35:31]** but overall I have to live with what is there, and I trust that it’s

**[00:35:34]** good.

**[00:35:35]** And that is already a change in thinking, and I believe that such

**[00:35:42]** interfaces could help with that.

**[00:35:43]** Now you just asked me to dive into the topic of Human in the Loop and what else

**[00:35:50]** there is, I’d like to briefly outline, so Human in the

**[00:35:57]** That characterizes systems where humans are actively involved in the decision-making processes.

**[00:36:03]** The AI prepares, the human checks and decides, gives approvals, is essentially right in the middle,

**[00:36:09]** instead of just being present. And with Human on the Loop, that describes systems where the AI is largely

**[00:36:15]** acts autonomously. The human supervises, can intervene, but actually the AI,
 
**[00:36:22]** let's say the AI works autonomously and the human bears the responsibility and the
 
**[00:36:29]** human can, as I said, oversee, but the AI mostly does things on its own. Now I would like
 
**[00:36:37]** to say, for the sake of fairness, that I would still want to know a thing or two additionally.
 
**[00:36:42]** Loyal listeners also know that we should actually not talk about human, but about expert,
 
**[00:36:48]** shout out. Still, I would like to also add one or two more terms
 
**[00:36:55]** since there’s also something called Human Intelli... In the Lead, yes, that characterizes
 
**[00:36:59]** systems where the human retains full control and leadership, but the AI makes analyses and
 
**[00:37:06]** offers suggestions, while the human is basically the main actor. There are always slight,
 
**[00:37:13]** subtle differences. We had once, when René was our guest, talked about such things
 
**[00:37:18]** yes, again. And if we complete the four conceptual worlds,

**[00:37:23]** there is still Human Out of the Loop. This is basically completely autonomous. The human only has at most

**[00:37:29]** some peripheral issues to deal with, but the AI carries out protein processes completely independently

**[00:37:37]**. We might still have that as our best practice.

**[00:37:41]** And to place this a bit more in our gaming world, this means essentially the

**[00:37:46]** topic of Hume Invalu, would be after the wood, the wood-felling AI has felled the wood and

**[00:37:54]** it is lying somewhere, it might still be the case that it has this largely autonomous

**[00:37:58]** operation, but the next step, whether it should also store the wood somewhere or

**[00:38:02]** take it to the lumber mill or something, would mean that I would then

**[00:38:07]** need to intervene and say, yes, please do that. In Schumen-Onvelu, we are

**[00:38:13]** then already at these orchestration surfaces. That I say, okay, I then look more at

**[00:38:17]** ensuring that the flow is running properly, that the resource chain is

**[00:38:22]** closed, now perhaps initially only for wood required

**[00:38:27]** for houses or then maybe the second production chain comes along,

**[00:38:30]** which delivers stones and then there's also food when we finish that and

**[00:38:34]** then of course at some point this Humen in Beloop will expand, if it is like this, I believe,

**[00:38:38]** in this third or fourth stage, as you just described.

**[00:38:41]** So, when is an individual Humen in Beloop in the combination, in the orchestration not

**[00:38:47]** perhaps Humen in lead only in principle, because then very, very many autonomous systems

**[00:38:53]** indeed still show me what is happening, but at many, many points

**[00:38:59]** intervene very, very independently and that's why it becomes extremely important that we then

**[00:39:03]** find visual solutions, interfaces that go far beyond the normal prompting, beyond the

**[00:39:09]** usual coding display that we are familiar with, which are important for me to

**[00:39:15]** orchestrate that. And for example, I had that now a time or two.

**[00:39:18]** is already totally exciting in reading, which also brings up this topic that maybe the gaming skills,

**[00:39:26]** the people who have played a lot, who might bring the skills needed in

**[00:39:31]** searching. I am an expert.

**[00:39:35]** World of Warcraft, over a year in gameplay time, over a year, guys,

**[00:39:41]** strap yourself in, strap yourself in, strap yourself in. I knew it was good.

**[00:39:45]** Maybe it's good. Of course, there’s a bit of a thing behind it,

**[00:39:48]** when you, as I said, do 1000 hidden object games or production chains over several

**[00:39:55]** I was a warlock.

**[00:39:56]** Which command stations and yes, there’s also always everything, so, what all exists.

**[00:40:01]** Then coordinating and orchestrating it, that’s also a human envelope, yes, and

**[00:40:08]** this orchestration ability, this optimization ability, then indeed going down at the right moment

**[00:40:14]** and maybe again being the human envelope and not the human envelope

**[00:40:18]** being and grabbing someone in certain situations, because something reacts, because something

**[00:40:22]** isn't working so well, is a skill that if you want to play successfully, you have to bring along

**[00:40:28]** or learn. I don't even think that what some claim is so absurd, that

**[00:40:34]** this ability might not be one of the worst skills in future

**[00:40:39]** AI agents that we are currently stepping into. It will also be really exciting to see,

**[00:40:44]** not that I want to dismiss this now, but I just had the chance

**[00:40:49]** to discuss how the current interfaces for the masses look, that you

**[00:40:57]** can now from anywhere time-controlled, start automations, start actions,

**[00:41:04]** have things installed, the way you described, how correctly I am in

**[00:41:09]** a GitHub and how correctly with Python one. You theoretically don’t even need to do all that anymore

**[00:41:14]** to know, because when you say to that thing, I need this, then it installs

**[00:41:18]** the stuff on your machine and does what it does, and when you're on the go, you have to

**[00:41:23]** give an okay while you're out and about. So I do believe that once these foundations

**[00:41:29]** are laid, the big players will also start to pay attention. If that

**[00:41:35]** really takes hold, not that Grandma Erna, no offense to Grandma Erna, yes, just figuratively speaking

**[00:41:42]** here as a persona for this topic, I write a birth poem with an AI that

**[00:41:47]** serves a purpose, but that really all the concepts we've discussed in previous episodes, MCP tool integration,

**[00:41:52]** skills, i.e., work instructions according to the systems, then performing tasks. Suddenly, you are

**[00:41:59]** working with multiple agents. If we look at the consulting thing I had back then on

**[00:42:04]** N8N, which I've now built as a skill collection with subagents in Claude, if that

**[00:42:11]** increases, then you won't be able to get around the fact that the interface will change, but this

**[00:42:17]** foundation that you have now, that, let's say, every morning at nine the harngrät or in our case

**[00:42:22]** a report is generated, that things can somehow be controlled from everywhere,

**[00:42:26]** that things can somehow orchestrate, install things technologically, do stuff, that the

**[00:42:32]** next logical step will bring me into something graphical, bring me into something spatial. So along the lines of

**[00:42:39]** up in the right corner, there's, let's say, the library city and down in the left is the

**[00:42:43]** developer city and up in the left is the resource pool or in your case now the coffee kitchen

**[00:42:49]** and the cloud and the office for working and no idea, because as a human you can navigate in

**[00:42:55]** this spatiality, in the visual spatiality, that

**[00:42:59]** you can also interact with the acoustics, yes, you hear an Ibi, yes, it means that or like

**[00:43:05]** were there not some games that when you said, bark the tree, they always

**[00:43:08]** said AI Sir or something like that, yes, there was also something, so you are

**[00:43:11]** capable, so to speak, of your stimuli. Acoustically, visually, spatially, that you are able to interact

**[00:43:16]** quick to find you, quick to act, and then you have to think about it, yes you as a person

**[00:43:21]** have a sack full of agents with dubious skills, you have a sack full of budget,

**[00:43:26]** so tokens that you work with, but next to you sits someone who also works

**[00:43:32]** in their company, on the same topic, also has their agents, you work together with all your

**[00:43:37]** troop members and little men and agents on topics. That's pretty crazy. And I just thought,

**[00:43:44]** while I was rambling on, maybe we’ll get something back like these Jamba savings subscriptions.

**[00:43:49]** Jamba savings subscription, not Jamba savings subscription, here ringtone, everyone

**[00:43:53]** can get their own skin. So the idea is, you have your orc skin and I

**[00:43:57]** have my bird of War-craft skin. No idea. So I'm really curious when we will see

**[00:44:03]** this in broad masses and not, and I do not mean it derogatorily, I mean, guitar projects become

**[00:44:08]** quickly successful, greetings to Peter, built Open Claw once and then became rich for the second

**[00:44:14]** time in his life. This will definitely be a point that differentiates

**[00:44:22]** the big players from each other again, who this mystery of

**[00:44:28]** usability and controllability and simplicity. Yes, this is something Apple has also claimed

**[00:44:35]** about themselves, like 1000 times saying no before they say yes once. I believe they have

**[00:44:40]** said yes more often than no recently, but that's another topic. Maybe one gets tangled

**[00:44:44]** up there still, but just bringing that thinking into this complexity will

**[00:44:49]** change a lot in terms of acceptance, usability, adaptability,

**[00:44:54]** resource avoidance, and we had the topic of resources. Also cost-saving,

**[00:45:00]** so you don't start by saying, I've burned 500 euros on AI tokens. Just the

**[00:45:07]** whole AI firms, if there’s an interest in them, because they burn out the servers in the cellar, the water

**[00:45:11]** and the electricity, if the application people don't always choose the largest model,

**[00:45:16]** but maybe also the small one. That fits in the context. Exactly. I think,

**[00:45:21]** but that’s why it’s like, one could slowly say,

**[00:45:25]** it should also slowly lead to wrapping up the show.

**[00:45:31]** The idea of putting the topic aside is wrong because we will definitely pick it up again.

**[00:45:36]** No, you do that so you never bring it up again.

**[00:45:40]** No, we will bring it up, of course.

**[00:45:41]** Because I think, let me say this sentence now,

**[00:45:44]** but I think the UX and I-concepts will probably be the next,

**[00:45:48]** probably will not follow these classic interface rules that we currently

**[00:45:52]** have for apps or websites, but actually need to orient themselves more towards strategy games honestly

**[00:45:58]** because perhaps there really lies more potential and more to learn,

**[00:46:05]** as if you look at how websites have been designed in the last 20 years or the apps that

**[00:46:08]** have been created over the last 10, 15 years, because they are actually not designed

**[00:46:12]** to orchestrate topics, but in principle, they have always been single-feature applications,

**[00:46:20]** that we built to solve things very, very simply in the moment, then just

**[00:46:23]** functionality, a weather app or something else, the weather icon or so. But they were not

**[00:46:27]** also designed, so to speak, to orchestrate things. I think everyone had to deal with that,

**[00:46:32]** who are currently working with AI orchestrations and how it can be represented,
 
**[00:46:35]** they should probably take a look at what it looks like in this
 
**[00:46:40]** Gaming is already involved, and as always, we will share some links in the show
 
**[00:46:43]** notes, so the things we just mentioned, like Agent Force, how that works,
 
**[00:46:48]** you can explore that a bit. But I find it a totally
 
**[00:46:51]** exciting field. You know I come from the third area, I find it super exciting,

**[00:46:56]** barely noticeable, I find it super exciting for this human component, but I
 
**[00:47:01]** actually also find it quite challenging again, when you really get into it,
 
**[00:47:06]** that you say and the agents interact here in these worlds
 
**[00:47:10]** with each other and they also have directives, and that's why I say, we will
 
**[00:47:14]** definitely not mute the topic, because we have already mentioned it before, that

**[00:47:18]** there were such experiments from MIRT, where they let AIs play in a Minecraft world

**[00:47:24]** together, where the lab started to build cultures,

**[00:47:28]** communicated with each other, invented currency, and so on, and

**[00:47:31]** then traded with each other, invented a religion while they were

**[00:47:33]** playing. And that's yet another aspect we must never forget about AI.

**[00:47:38]** Everything we've just described sounds very linear and predictable.

**[00:47:43]** You just mentioned Open Cloud. There are a few things that are somehow

**[00:47:46]** surprising, not just that letting an AI agent run a bit more freely.

**[00:47:51]** It does things that you wouldn't have thought before, we've discussed that occasionally in the last

**[00:47:54]** episodes. And when I imagine that in such a

**[00:47:58]** game world, the AIs with the Human Invaluable on the loop then at

**[00:48:05]** one point act, but there are also other AIs out there, maybe also foreign game worlds

**[00:48:10]** to Frank, foreign, orchestrated agent systems, docking onto my agent systems, creating a

**[00:48:17]** new world for us to explore and engaging with it.

**[00:48:19]** I believe there's also material for episodes in there, that makes it worthwhile.

**[00:48:25]** Which brings me to the topic, we still haven't talked about, what were they called

**[00:48:35]** again?

**[00:48:36]** Bio-Needle?

**[00:48:37]** No, we called this combination of neural, so real nerve cells, which

**[00:48:43]** are programmed into neurochips.

**[00:48:45]** Ah these height chips there, that are on height mass...

**[00:48:47]** Yes, yes.

**[00:48:48]** So not that we're already revealing the material for the next episode.

**[00:48:51]** No, I don’t want to do that in the next episode, and we’re not making any predictions.

**[00:48:55]** No, we won’t.

**[00:48:56]** But we will make some episode about it, because I just think it fits simply to the

**[00:48:59]** topic.

**[00:49:00]** There is actually a start-up that has racks where, in principle, these nerve cells

**[00:49:06]** you can basically rent it in such gluristic standings, you can

**[00:49:10]** request it as a sort of cloud service, so you can have computing power on these

**[00:49:15]** nerve cells to prove how powerful they are, the internet has

**[00:49:20]** again cried out and demanded, let them play Doom. Yes, and it's true, these

**[00:49:26]** artificially cultivated nerve cells can indeed play a round of Doom, which is somehow

**[00:49:32]** mind-blowing that we now have neural networks made up of nerve cells that

**[00:49:37]** are capable of playing Doom independently. We live in the following time. Before we finish,

**[00:49:44]** a little anecdote from my youth. Doom, that's the time when I was using a computer

**[00:49:49]** And back then, my computer didn't have Ethernet, so no network, instead you

**[00:49:55]** had to connect two computers with a serial cable, and we played Doom there.

**[00:50:00]**

**[00:50:01]** And if you know what Doom is, you look it up on Google, it was cool back then, today you would

**[00:50:06]** not for rolling dice.

**[00:50:07]** I would definitely roll dice for our podcast.

**[00:50:10]** Hopefully, we didn't chase a dinosaur through our SimCity city.

**[00:50:14]** That's also a point when all the agents are running around here.

**[00:50:17]** doesn't matter. If you enjoyed the episode, leave a like, a five-star rating, and write

**[00:50:26]** a note to your neighbor on a napkin with a little love message. I'm done. I would like to

**[00:50:32]** say goodbye, unless Jens wants to add a sentence. Very gladly. I leave

**[00:50:36]** him the floor. I'm already out. Ciao.

**[00:50:39]** Thank you, Mark. And thanks also for the last sentence. I can't resist saying it,

**[00:50:44]** because some people know me and especially like it when it's mentioned again, that the
 
**[00:50:47]** topic of visual representation, user interface is very dear to me, this interaction.

**[00:50:53]** between human and machine, so my main theme is, and I keep saying it again, that

**[00:50:58]** in this world we are currently in, the topic of trust is actually really

**[00:51:04]** this final UI challenge and now with this episode today I wanted to touch on it again,

**[00:51:09]** that we say trust actually does not arise from control,

**[00:51:12]** trust does not arise from control, but that in the future we need this system dynamics

**[00:51:17]** understand better.

**[00:51:18]** That it becomes comprehensible to us.

**[00:51:20]** And here, in my opinion, gaming interfaces can, we can

**[00:51:25]** learn a lot from them, and accordingly, this statement is even truer than it was before

**[00:51:30]** in this episode.

**[00:51:32]** Trust remains the final UI challenge, especially in this AI image landscape we are in.

**[00:51:37]** let's listen through and work on our nice, lovely podcast.

**[00:51:43]** Mark and I are working on it by discussing the whole scene, thinking about it.

**[00:51:47]** We're trying to incorporate it into our private world, into our work world.

**[00:51:52]** It remains exciting and is a lot of fun.

**[00:51:54]** I'm looking forward to the next episode.

**[00:51:55]** Wishing you a great week and see you soon.

**[00:52:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:52:06]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:52:12]** Here you will find clear categorizations, genuine practical insights, and a fresh perspective on what's possible.

**[00:52:19]** Understandable, critical, and always with a wink.

**[00:52:22]** AI for thought, for a chuckle, and above all for joining the conversation.
