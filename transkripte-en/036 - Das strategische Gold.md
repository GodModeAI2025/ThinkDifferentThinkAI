---
title: "Das strategische Gold"
episode_index: 36
published: "Mon, 20 Apr 2026 14:59:00 +0000"
duration: "3412"
audio_url: "https://audio.podigee-cdn.net/2449676-m-dfce48265ddf95aa1ab0f9c9fe9281b3.mp3?source=feed"
guid: "4bda80e59d1d44547f35ede6131ac0b6"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T21:10:35+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/036 - Das strategische Gold.md"
translated_at: "2026-04-29T13:44:29+00:00"
---

# The Strategic Gold

**Published:** Mon, 20 Apr 2026 14:59:00 +0000
**Duration:** 3412
**Audio:** https://audio.podigee-cdn.net/2449676-m-dfce48265ddf95aa1ab0f9c9fe9281b3.mp3?source=feed

## Description

Skills
In this episode, we take a deep dive into the world of AI skills and discuss why skill engineering is changing the game. Together with our guest, we question how teams, leadership, and entire organizations evolve when agents no longer just respond to prompts but use real skills. We share our experiences, openly discuss opportunities and risks, and provide insights into how skills redefine work and collaboration. Of course, we also take a critical look at international developments – from skill databases to cultural differences in dealing with AI. If you want to know what the working world of tomorrow might look like and what role skills will play, you are in the right place.

Notion
https://www.notion.so/de-de

Anthropic
https://www.anthropic.com/

GitHub
https://github.com/

Python
https://www.python.org/

Kaparthy
https://karpathy.ai/

Markdown
https://de.wikipedia.org/wiki/Markdown

Job to Be Done
https://de.wikipedia.org/wiki/Jobs-to-be-done

Agile Methods
https://de.wikipedia.org/wiki/Agile_Softwareentwicklung

OpenClaw
https://github.com/openclaw/openclaw

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here, you will find clear classifications, real practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Thought-provoking, amusing, and above all, engaging.

**[00:00:34]** So, remember, we had a guest in our still young podcast not too long ago

**[00:00:41]** and we invited him back because he had already discussed very interesting

**[00:00:46]** topics with us back then, and we thought, why not revisit this,

**[00:00:51]** because not much has changed in the AI world.

**[00:00:55]** That sounds strange, right?

**[00:00:56]** Everyone is always talking about how things are moving so fast or something else, and I start this podcast with the words that not much has changed.

**[00:01:02]** But in fact, either we were back then or especially you, Rene, were already so far-sighted.

**[00:01:07]** We talked back then about the topic of agents and how they actually interact with us humans.

**[00:01:15]** So how, in principle, such an IOC model was also mentioned back then, or you brought it up.

**[00:01:20]** So the intent of humans, the operations performed by the machine, and the control ultimately provided by humans again.

**[00:01:26]** If we now look a bit at the topic we want to discuss today and deepen it,

**[00:01:31]** particularly related to agents, it’s mainly the topic of skills.

**[00:01:34]** And I believe that is indeed a crucial part in order to actually perform this operations part well

**[00:01:39]** and not just throw everything into a round, these things need good skills.

**[00:01:42]** And I'm glad you are here. I'm glad my co-host Mark is with us.

**[00:01:47]** And I think this will be another good episode. We have a lot of topics, really packed, that we can discuss.

**[00:01:52]** A lot is happening in AI again, so let’s get started.

**[00:01:58]** Yes, first of all, many, many thanks for the invitation.

**[00:02:02]** Yes, you were also our first guest on the podcast.

**[00:02:06]** August, right?

**[00:02:07]** Oh God, that hasn't been so long ago.

**[00:02:08]** And when you just started, Jens, and after the Motus, not much has happened, I thought,
 
**[00:02:14]** hold on a second, even if the statements made back then in the podcast definitely, I would say,

**[00:02:20]** still hold quite well today, we'll certainly get to that later.

**[00:02:25]** A lot has actually happened.

**[00:02:28]** When we started, I was singing high praises for N8N here.

**[00:02:35]** We looked at models.

**[00:02:37]** So today, I don't even know, do you still use the models from back then?
 
**[00:02:40]** No, I don't think so, do you?
 
**[00:02:41]** No, Mark, when you think about it, when we started, we were both burdened by Nautchen.

**[00:02:46]** Back then, that was suddenly brand new, how it created connections in databases and how it quickly built content for you.

**[00:02:55]** Is today more in the background, right? Today you're taking agents, they do it anyway.

**[00:02:59]** Although, Notion is a nice keyword, my cousin, I also had him here in an episode and we talked about Notion.

**[00:03:05]** They are with Anthropic, the whole topic of Managed Agents, we discussed that in the episode that went online recently.

**[00:03:12]** And it's quite funny to see how Notion is trying to stay in the woods.

**[00:03:17]** But yes, this hot topic, look what's coming out of it, look what's happening.

**[00:03:21]** I mean, we talked about Prompt Engineers and so on back then.

**[00:03:24]** And today we're talking about, and I think that's a very nice segue, skills.

**[00:03:30]** I think that's really great, you know the saying, he who asks, leads.

**[00:03:35]** Who would like to explain to us what skills are?

**[00:03:37]** I'm always so cheeky and say, no, would you?

**[00:03:39]** Yes, I'll follow along.

**[00:03:40]** So, it’s really totally unprepared for all heights, but the way I explain it, yesterday was prompts and prompting is basically a

**[00:03:49]** elaborated text that is a bit adapted to the model, it somewhat guides the model, unfold yourself like that.

**[00:03:56]** A skill is that, but it also requires access to a lot of tools, and the access is, let's say, orchestrated and guided, and there’s also code involved.

**[00:04:06]** So, then, when needed, the entire skill also requires code to execute dedicated clear instructions.

**[00:04:13]** And the combination of everything, plus the ability to take persistent storage units along with it, is a skill.

**[00:04:21]** And that's why prompt engineering was yesterday, and skill engineering is tomorrow.

**[00:04:26]** And our, our three trial signs will be that soon the world will be full of skill engineers.

**[00:04:33]** with a flavor in purchasing or flavor in controls or flavor in logistics and so on, right?

**[00:04:39]** No, I would still like a little bit of flavor-logistics on top, delicious.

**[00:04:43]** Delicious.

**[00:04:44]** So, I actually find that it was also a bit ironic, the

**[00:04:47]** motto, Promethe-engineering is dead, it really isn't, right?

**[00:04:49]** You basically find all the rules again, you just pack them into large text files today,

**[00:04:54]** skills then have these so-called markdown files, where you write your, I’d say, work instructions

**[00:04:59]** and whether it’s the agent executing them or the human, both can

**[00:05:05]** use it. And as you said, the topic, I can also store program code in there

**[00:05:10]** and bring it to execution and thus introduce determinism into the system is just

**[00:05:15]** really cool because you can actually mix that in these skill files. I saw

**[00:05:19]** a skill the other day where you write your prompt and suddenly

**[00:05:21]** a bit of Python code comes up right in the middle of the prompt and then it just continues and you

**[00:05:25]** stand there and think damn it, how cool is that, right?

**[00:05:29]** How cool is that?

**[00:05:31]** And everything can also be generated automatically.

**[00:05:33]** That is actually the crazy thing.

**[00:05:36]** Already with the prompts, you know.

**[00:05:38]** You want a prompt, and you ask the AI to create a prompt so that the AI is better.

**[00:05:43]** That's almost like the singularity that Musk likes to talk about.

**[00:05:47]** That they AI, AI makes.

**[00:05:49]** I'm not at the point to say that we are there, we're not quite there yet.

**[00:05:52]** It has a certain flavor in that direction, doesn't it?

**[00:05:55]** Yes, the range of skills, what I find is that it does, and there's a market there

**[00:06:02]** especially right now.

**[00:06:03]** Back then we talked about models and now the skills are actually manifesting

**[00:06:07]** this removal of that discussion, because of course skills bring the nice aspect that they

**[00:06:12]** are model-agnostic.

**[00:06:13]** But I can simply create the skills somewhere, in a relatively simple format

**[00:06:17]** save them, and then make them available to any model afterwards.

**[00:06:20]** And that is, I believe, one of those incredible advantages, that you no longer look at the topic so single-layered

**[00:06:25]** like, wow, what can a model do completely, but rather

**[00:06:30]** go back a bit and say, which packages, which capabilities

**[00:06:34]** can I somehow encapsulate, without it being actual program code, but rather

**[00:06:38]** a description of what needs to happen, in which behavior it should show itself

**[00:06:42]** and that I can then, depending on which model is the best choice, also

**[00:06:47]** make that model available.

**[00:06:49]** Of course, this has a few other advantages, because we are no longer so restricted.

**[00:06:52]** We are not working on the edge of the model, but rather thinking about how

**[00:07:00]** I can orchestrate all these skills, which skills do I need, are skills

**[00:07:05]** from yesterday still the skills of tomorrow that I want to have.

**[00:07:08]** So, I am interested in the skill from yesterday.

**[00:07:10]** From an hour ago, when you say that.

**[00:07:14]** Yes, exactly.

**[00:07:15]** You know, I have your analogy. Do you remember back in the day with digital cameras when there was the so-called pixel race at the beginning?

**[00:07:22]** My camera was not 2-pixel, megapixel, yours can do 3, the other one can do 10.

**[00:07:27]** And at some point it became clear that more pixels don't fit on the chip, then it was about a different quality.

**[00:07:33]** I mean, we are still on that track, so there will be better models, so when world models come, there will be again some, but it will be so that we will also have a saturation,

**[00:07:41]** that we will be saturated and then exactly that, what you said, the system.

**[00:07:47]** So how do I utilize that in itself? How do I create impact?

**[00:07:50]** Becoming significantly more important and when? The speed is probably already quite soon that we will be in saturation.

**[00:07:58]** So what I have with all these skill topics, I admit, this thought is actually still quite new to me.

**[00:08:03]** You can feel free to laugh at me now if I am lagging behind.

**[00:08:07]** I stood recently in front of the question, ok, well, in skills you can run program code, fair point, understood.

**[00:08:13]** Actually, something like a skill and a Kaida underneath is an operating system where software can be deployed.

**[00:08:21]** I recently built a little skill, it's available in the Git repo.

**[00:08:25]** It burrows through what is inside, throws Kotlin, PHP, no idea what.

**[00:08:31]** You tell it, create a skill from that and then it considers in a sense,

**[00:08:35]** which orchestrators I need, so how do I break down the tasks that this program,

**[00:08:39]** that I found in Git, how do I break that down? And what it cannot convert into a skill

**[00:08:44]** it really runs as software in Python in your skill.

**[00:08:51]** And then I thought to myself, wow, you know? So this topic, how do we build software

**[00:08:57]** changes? How you run things changes? And how do you integrate, I’m saying now

**[00:09:03]** sorry, such an old, mothballed Githa project that suddenly gets a new life because you say, come on, migrate this to a skill and suddenly that thing is no longer alive, whatever, here Kobol, something else, well, I probably won’t find much in Gith about Kobol, but then suddenly in such a runtime, in Codex, in Opus, in, I don’t know, what.

**[00:09:22]** I always found that kind of, huh, I know it in principle, but I found that so amazing, with suddenly so many possibilities.

**[00:09:30]** You know, I recently, I follow a lot of news channels and so on and one

**[00:09:35]** unfortunately I can’t remember the name, it was a very fresh one, I believe Z51

**[00:09:40]** or something like that.

**[00:09:41]** So the name isn’t quite correct, but somewhere close, an open source

**[00:09:44]** or also a weight model, that’s just out now, they let that thing run

**[00:09:49]** and let it run autonomously for eight hours to create a Linux clone, so just completely

**[00:09:55]** fully operational with over 50 apps. Even a WhatsApp or Telegram messenger component with

**[00:10:03]** mail and everything fully operational. And now think about it, you make this horde of

**[00:10:08]** agents that create software, running through all GitHub repos. Just think about

**[00:10:13]** what will come out of that, right? If you say, okay, take the best and build a bunch

**[00:10:18]** of apps that can do this and that. Yes, yes, that’s wild and it feels a bit like,

**[00:10:23]** I had two things from Kaperfee. Kaperfee released this Wiki topic again last week

**[00:10:29]** about how it can essentially be scientific. That’s why many of

**[00:10:33]** our posts revolve around this topic. That’s another subject. It applies once

**[00:10:39]** to the topic and in the background again, that we have some kind of scientific

**[00:10:42]** that we want to use. So also outsourced from the model, so that it can also be used agnostically.

**[00:10:45]** And aside from all these bottles somehow getting complicated

**[00:10:50]** rack structures, something like that, that one thinks about in between. But what is the other course from

**[00:10:54]** him, I found even more exciting and it fits what you both are saying right now. Because the

**[00:10:57]** capabilities are so high, he also assumes that one doesn’t actually fork a Cub base in

**[00:11:03]** Github anymore, but that it’s actually only important to fork the idea markdown file,

**[00:11:10]** you know, that we’re coming into such a world where it gets much brighter

**[00:11:15]** and much more sensible that we only exchange the ideas in a token optimized way and not swap the whole

**[00:11:22]** legacy code, if you will, and then say, that was the actual idea, that’s the actual output I want to regulate.

**[00:11:28]** So if we now take, I thought this morning overnight, from such a designer-job-to-be-done perspective

**[00:11:34]** looking at it, you used to always say, if someone wants to drill a hole in the wall, yes, then they need a drill.

**[00:11:39]** And that’s basically the job I want to do, like the hardware store, us as Brosch or other manufacturers of drills.

**[00:11:45]** Nowadays, if you look at it from that perspective again, if I say the job-to-be-done, that’s basically what has to be done.

**[00:11:53]** And I can actually do it without having a pre-made piece of software.

**[00:11:57]** I also envisioned it that way at some point, but without having any pre-made piece of software at any point in the ecosystem, whether at my place, at the partner’s, at the reseller’s, wherever,

**[00:12:09]** I can actually do without it, but I just have to state in the concept of the machine that this is the job I want to do.

**[00:12:15]** Do the rest.

**[00:12:17]** Do the rest. Or suggest something to me, right?

**[00:12:19]** So it’s, and I also believe that the key is this topic that he also chose for this podcast, the skills.

**[00:12:26]** I believe, if you look back, there used to be, well, in the Internet there were the web apps, so the big thing, that you know now

**[00:12:33]** if apps became available it was the iPhone platform and so you could also make apps available to others.

**[00:12:39]** Then of course, language models can now skip some things but this idea of language models is also going into skills in a similar way. I’m not saying apps, but rather also an epitomization.

**[00:12:49]** In the general AI world, so something happens that exactly describes what is happening.

**[00:12:55]** It’s again something that we as humans might need to make it easier for ourselves.

**[00:13:00]** Maybe not wanting to accept that there is a model that could do everything.

**[00:13:04]** So, because on the other hand, let’s say if we go into the future and the models are getting larger and better.

**[00:13:10]** You just mentioned the topic of world models, and I somehow believe that even if we were to take a normal model and compare it, 

**[00:13:17]** If we were to try to fit our brain into such a model, I think we would still have 100 trillion parameters aside. 

**[00:13:24]** And I believe that even the best models in the world are still miles away from that. 

**[00:13:28]** Nature is still clearly superior to what we have built so far. 

**[00:13:32]** But nonetheless, we are heading into a future where the 

**[00:13:37]** Models always being able to do better, and then you wonder, do I need such a

**[00:13:40]** skill description?

**[00:13:41]** Because actually, these models can do everything anyway.

**[00:13:44]** And now I have a point when I let it go.

**[00:13:46]** Because you might know, I love writing here and there,

**[00:13:49]** especially with Mühlscher.

**[00:13:50]** I have a small issue.

**[00:13:51]** It's currently related to the topic of leadership and Agent DKI, because there is a paradox.

**[00:13:56]** Because I am deeply convinced and I believe I have solid evidence that jobs will only change.

**[00:14:02]** We will do a lot, because people will still work for me, so we will do a lot, but we will work differently.

**[00:14:07]** And what is that now? There is a paradox that says, the more you automate business processes,

**[00:14:14]** the more leadership you need, the more leadership.

**[00:14:17]** That's what you also talked about last time. You mentioned Intent, Operate, and Check.

**[00:14:21]** This intent aspect, this strategic leadership will become increasingly important, because the skill-overloaded agent corpus must somehow convey the impact and the results.

**[00:14:34]** In order to work with it, you always have to ask yourself how to lead this amount of agents so that something comes out of it.

**[00:14:42]** And this feedback loop is getting faster and shorter.

**[00:14:47]** This means, the people who are currently in the process, by entering something on the table, clicking something on the monitor at that point,

**[00:14:55]** at the end then dominate the output of the process, they will stand by and observe what comes out and then intervene very quickly,

**[00:15:02]** oh, dear agent, I need to give you a different strategy so that the outcome is what I want.

**[00:15:06]** That means more leadership and less operational work, more guidance.

**[00:15:10]** That means, and this is very good news for me, because you also addressed the people.

**[00:15:15]** They do not need to master the skills, but they need to focus much more on leadership in terms of how can I manage a corpus of software agents so that something comes out.

**[00:15:27]** Yes, that brings me back to a topic I had already mentioned back then, and for this we need, of course, even more of this level of trust.

**[00:15:36]** So then reflected in some form of user interface, that we can understand what is happening.

**[00:15:42]** because if I now let an agent talk to another, if I as a human need to intervene somewhere

**[00:15:48]** and it always becomes complex, thus the tasks become more diverse because much more tasks are

**[00:15:53]** completed in an even shorter time, I naturally need, so that's why I am still

**[00:15:57]** of the opinion that it will be an incredible challenge, both for the agents

**[00:16:01]** to build among themselves as well as for us humans involved, to build an interface that

**[00:16:06]** truly gives us the trust that the right things are happening in the delegation,

**[00:16:10]** that I have made?

**[00:16:12]** I also find the topic of delegation.

**[00:16:14]** One can say, well, as a leader one is used to delegating.

**[00:16:18]** When you now, then I wouldn't say we have everything better under control,

**[00:16:21]** than perhaps your employees themselves,

**[00:16:23]** but the ability to let go of things,

**[00:16:27]** to accept that the machine does not replace me now,

**[00:16:32]** but that a machine can do something,

**[00:16:34]** up to a certain quality level.

**[00:16:36]** And then I look at it later,

**[00:16:38]** What I might still release somehow afterwards and then it continues and I don’t hold back with the motto.

**[00:16:44]** Oh look, what the AI built there, that’s nonsense, I knew that right away.

**[00:16:48]** I recently had a case where a colleague looked at something, a skill, and built a little bit,

**[00:16:52]** he somehow accomplished weeks of work in hours and afterwards the feedback was,

**[00:16:56]** oh look, this is that and that is still wrong.

**[00:16:59]** Where I then said, yeah look, you read it, you corrected it,

**[00:17:03]** after two or three hours you were also done again.

**[00:17:06]** That means, if I take your two or three hours, the two or three hours from Skill,

**[00:17:10]** then you're somehow at six or seven hours straight versus a whole week or two

**[00:17:15]** weeks.

**[00:17:16]** That's a good average and be glad that the AI, that you're not just,

**[00:17:22]** I mean, I'm now the one who just ticks things off, like the flightless on the radar

**[00:17:26]** sitting and waiting for something to beep loudly, because some planes might otherwise

**[00:17:31]** be on a collision course or something, which he can just keep an eye on

**[00:17:35]** and this constant, you already think, in a state of alert, he also has to take regular breaks,

**[00:17:40]** otherwise they would lose their concentration. I heard somewhere that such things

**[00:17:45]** just like autonomous driving, it is safer to take the steering wheel out of the autonomous car,
 
**[00:17:51]** than to trust that the human will intervene when the autonomously driving car
 
**[00:17:57]** makes a mistake, because you simply find yourself in the absence of that
 
**[00:18:02]** you just drift away and the other thing you mentioned earlier, then you might later
 
**[00:18:07]** have no idea, 3, 4, 5 agents, that's just the other side of the coin, that you
 
**[00:18:11]** might be giving things over to the machine, placing it in its hands and then at some point completely

**[00:18:16]** you lose, depending on which interface we provide to people, depending on how we handle it,

**[00:18:21]** that later you say, okay, I have no idea here, counting windows open,

**[00:18:25]** whether it's a bathroom or Opus, whatever is lurking around, and then you're standing there, where

**[00:18:30]** was I with what? And I have to leave the right one for a moment, you come back after an hour, what's going on now, what is the current state of affairs?

**[00:18:37]** This also calls for a new kind of interface. How do I deal with it? How do I manage time? We really have some exciting questions ahead of us.

**[00:18:48]** And also the skillification will change the interface, the GUI will definitely change again, that's clear.

**[00:18:56]** Yes, so that's something, I'm actually curious, as I said, how that runs, and just this realization I was talking about with people, you give them something in hand, they say, come here, Kai, right? And then, well, no, did you misunderstand? I get something returned from her, I work on it again and then it falls back to us asking, okay, can we maybe get a bit more out of it because we adjust the skill again, yeah? What interests me, the skill from an hour ago, was just said, I also have something like that,

**[00:19:26]** trying to figure out through synthetic test cases how you can improve the skill overnight and hoping it works a little better the next day.

**[00:19:34]** It’s a really broad field, that, yeah, we first have to see how to position ourselves and yeah, how it all develops and the good models just come from it by themselves.

**[00:19:48]** Definitely and regarding positioning. It’s actually a bit interesting,

**[00:19:53]** now, when I think about the personal experiences we have and those that

**[00:19:58]** people outside, I believe, have on such an organizational level. So I believe,

**[00:20:01]** the ex-Twitter founder, I think his name is Jack Dorsey, he also

**[00:20:09]** published an article one or two weeks ago where he said, we actually need

**[00:20:14]** much, much flatter organizations in the future. And do not start translating your

**[00:20:20]** current org charts into agentic structures. That’s exactly one thing. So,

**[00:20:28]** I believe that’s a good impulse, you have to take that away because I think,

**[00:20:33]** there’s something in it that needs to be picked up when you now dedicate yourself to the topic and say,

**[00:20:38]** yeah well, how could my organization in the future, enhanced with skills that I

**[00:20:43]** somewhere linger, actually look, what happens, what will change

**[00:20:46]** and I believe that’s an exciting question. So this old

**[00:20:51]** pyramid is dead. You need to write a chapter in my book. So actually the old

**[00:20:58]** information brokers, i.e., leadership layers that define themselves by how

**[00:21:03]** carry a drift carrier in the message and know that A and B

**[00:21:06]** need to be together in the meeting for something to come out of this. You need them still,

**[00:21:11]** So it doesn't mean that you're doing a bad job because we're managing a complexity,

**[00:21:16]** music complexity, but that will become less and less important and it will be

**[00:21:21]** much more important to lead content-wise.

**[00:21:22]** This will naturally flatten hierarchies.

**[00:21:25]** My steak is always, hierarchies are actually always a compromise.

**[00:21:31]** Actually, I don't want to have any hierarchies at all; everything needs to be

**[00:21:34]** flat, only then do I have anarchy.

**[00:21:35]** So I have to somehow try to lead a large number of people efficiently in an organization so that the maximum productive output is generated.

**[00:21:45]** So I have to create such branching teams. And as soon as you make two teams, you have two teams that build a wall and bridge.

**[00:21:55]** That happens automatically, and at some point, when you really live it out, we in our company are fortunately not doing that,
 
**[00:22:01]** Companies, I've seen them, they have really stretched that. You need a visa for that,

**[00:22:05]** when you want to go from HR to the marketing department. So that's actually quite far apart.

**[00:22:12]** And this pyramidal setup is indeed in a world where we work

**[00:22:19]** can be divided into agentic and, let's say, strategic work, less important.

**[00:22:25]** Much less important, and you can work much more hierarchically free here. And we know that.

**[00:22:30]** Hierarchy fly is indeed the essential core of agile methods. I could remember earlier in

**[00:22:35]** other companies, when I first tried to teach management agile concepts. People said,

**[00:22:39]** agile, that's quick, then you do it faster. Yeah, no, that's not the

**[00:22:46]** idea, rather the idea is actually to work hierarchically free. No matter who has

**[00:22:52]** what rank on your shoulder, the people who know stand around a problem

**[00:22:57]** around and solve a problem to generate the best

**[00:23:04]** solution for the user groups, the customers, who have the problem. Hierarchy-free. Yes, hierarchy-free and knowledge power free. I knew

**[00:23:10]** the term knowledge power as well. It was sometimes expressed that

**[00:23:13]** certain, well, certain things should be known. Well, of course, there are still always some

**[00:23:17]** topics that have relevance, that not everyone always knows about,

**[00:23:20]** but I believe in such an organization of the future, it is actually unacceptable

**[00:23:26]** if not all knowledge is readily available and especially if knowledge

**[00:23:31]** is not just the stored data format or the file, but also the skills

**[00:23:38]** needed to simply implement certain topics. And I believe we also need to

**[00:23:41]** address that. I believe that the organization of the future needs, I think, both alongside

**[00:23:45]** the accessible knowledge in a, for example, in Markdown format or in whatever format

**[00:23:50]** so that the machine can read it well. MCP servers that can access certain units

**[00:23:54]** simply, in my opinion, also need a kind of skill database and workflow

**[00:24:00]** that is available to the entire company. Because what you are just describing. So that,

**[00:24:05]** what the energy system needs is that I basically have all the skills

**[00:24:08]** to implement things. Because as soon as I don’t have all the skills to implement a certain

**[00:24:12]** topic, the energy system fails. Because then I have to wait for someone else

**[00:24:16]** to implement it for me. And I believe we can also go there. That we

**[00:24:19]** say that in the future we can query the necessary skill to already take

**[00:24:25]** the next step. That doesn’t mean that we have to take the step entirely alone,

**[00:24:28]** but yes, we still need the other person who will maintain this skill group

**[00:24:31]** we can rely on. But I will become more flexible, simply,

**[00:24:34]** I will become significantly more flexible. We need this as organizations or

**[00:24:37]** Organizations will need some sort of skill in the future, skill, we just talked about that.

**[00:24:41]** I still remember an episode with a,
 
**[00:24:46]** with two people from a kitchen appliance manufacturer,
 
**[00:24:50]** with whom we had the discussion, Jens, you were just,
 
**[00:24:54]** I think at Carnival, whatever, we had the topic,
 
**[00:24:58]** that organizations will certainly change in the future also because
 
**[00:25:02]** boundaries will disappear that were created,
 
**[00:25:05]** because in the past people were simply given a topic as a task.
 
**[00:25:10]** And this task, there were, what I say, you had 10 people doing web,
 
**[00:25:13]** 10 people doing apps, 10 people doing backend, 10 people doing
 
**[00:25:17]** data management, 10 people doing service management.
 
**[00:25:19]** And now you find yourself with an agent or with tools that make these boundaries
 
**[00:25:24]** disappear because you are now working on a solution and not just on a
 
**[00:25:29]** very small part.
 
**[00:25:30]** You do a crash course alone, you do a feedback form alone,
 
**[00:25:36]** you click on deploy and the database learns your field, web and app get
 
**[00:25:41]** the stuff and if you say tomorrow, I’d like a new layout, then it has a new
 
**[00:25:44]** layout. Certainly, there are still people who say, okay, just a moment, this is the
 
**[00:25:49]** font that should be used and this is the color that should be used and we have
 
**[00:25:52]** perhaps a few rules we want to set, guardrails, how development occurs and
 
**[00:25:56]** what needs to be considered, please also think of testing, nobody should forget the tests and
 
**[00:25:59]** stuff like that, but still team structures will change because I also believe,
 
**[00:26:05]** when I see it alone, what people are capable of and I experience
 
**[00:26:10]** the sweet taste of honey, who previously would jump into my face with a
 
**[00:26:15]** naked ass if I had told them, your expertise is important and correct, but you leave your
 
**[00:26:21]** beaten path, you open yourself to new technologies,
 
**[00:26:26]** you are now front and back and you have seen it? They considered me crazy.
 
**[00:26:31]** And now that’s normal for you. Now they come to the office with joy,
 
**[00:26:34]** because all of a sudden boundaries disappear. You talk about solutions and he says please also,
 
**[00:26:39]** I know you’re just getting into a talking spree. We have guests, yes.
 
**[00:26:41]** I mean, hello, I also had to give the guest the floor again.
 
**[00:26:43]** But I always remember a story my teacher once
 
**[00:26:49]** told me in secondary school.
 
**[00:26:51]** She said that a person who contributes to a solution from start to finish,
 
**[00:26:57]** identifies better with the solution, so if you stand at the assembly line and just screw in a screw.
 
**[00:27:02]** Well, we have robots for screwing in screws today, fair point.
 
**[00:27:05]** But you identify with it more.
 
**[00:27:07]** But now people get the tools to do something that a customer,
 
**[00:27:14]** another user, can make something out of, and with that you identify and that
 
**[00:27:20]** brings joy.
 
**[00:27:21]** At least that’s my experience.
 
**[00:27:22]** And I believe that is also meaningful.
 
**[00:27:25]** So yesterday we trimmed organizations according to good skills and abilities, but
 
**[00:27:31]** based on a terrorist process world.
 
**[00:27:33]** Yes.

**[00:27:34]** A specialist for this, then comes a specialist for that. We do handovers and have programmed an IT interface.

**[00:27:41]** SAP did something integrative back then, but it happens one after the other, and that's how this specialization was created.

**[00:27:48]** Now, of course, domain knowledge is becoming, how shall I say it, a little less important.

**[00:27:55]** It is still important, but its significance will diminish somewhat because, somehow, when you go up to level 5, where there are 100 levels,

**[00:28:03]** anyone can tackle any topic now. Anyone who can’t godengar is godengar.

**[00:28:08]** Of course, not on a huge scale, oh, but who knows, we have a large Erdmann, but

**[00:28:13]** everyone can do piece-controlling, everyone can basically buy in, everyone can basically

**[00:28:17]** make the first competence filters for HR developments, basically. So, domain knowledge will

**[00:28:22]** be less important. This means the way we structure our teams needs to

**[00:28:25]** be adjusted. But they have to be. That is exactly what you said,

**[00:28:29]** you hit the nail on the head, because in the future we will cut much more based on

**[00:28:34]** giving people the feeling that it’s their thing, their baby, that

**[00:28:38]** is their motivation, that is their output. And that has always been my credo. All of this,

**[00:28:44]** what we collect with this wonderful technology, is still just a screwdriver. That is

**[00:28:48]** a tool. I use it in the end to either get the screw into the wall

**[00:28:52]** or to borrow the hole in the wall. That’s a tool. And the one who

**[00:28:56]** drilled or screwed is then the person who is proud of the output.

**[00:29:01]** And that’s how we need to approach it.

**[00:29:04]** Exactly, that’s how it should be, and if we directly should understand that the person actually

**[00:29:08]** wanted to hang a picture on the wall.

**[00:29:09]** That is the actual output.

**[00:29:10]** That’s also the story I started earlier, to see

**[00:29:13]** and I believe that is really important.

**[00:29:14]** I think this is exactly the topic, we need to focus more and confess

**[00:29:18]** that more on what we actually do out there as a business.

**[00:29:21]** So we as a company offer something that enables people out there at this moment,
 
**[00:29:27]** to perhaps hang the picture up for someone.

**[00:29:28]** And I believe that is exactly the topic, to focus more on the real impact.

**[00:29:32]** and less to work through layers to find someone who can catch the ball somewhere.

**[00:29:37]**.

**[00:29:38]** And I believe AI can really help there.

**[00:29:41]** I think, Mark, because there’s something positive to ask.

**[00:29:44]** I actually have two critical topics there.

**[00:29:47]** Yes, I actually wanted to pick something up.

**[00:29:49]** Before drifting too far forward, I wanted to briefly pick up the ball.

**[00:29:52]** We already talked about it; when teams are formed, bridges need to be built and such things.

**[00:29:57]** And while we were talking, a sentence came to my mind that I might not be able to

**[00:30:00]** articulate very smoothly, but in the past, you basically shared your expertise

**[00:30:05]** by specializing more and more in topics.

**[00:30:10]** You have acquired knowledge, you've applied it, you're basically, in quotes,

**[00:30:15]** you've spent a long time with it and then people called you,

**[00:30:18]** people reached out to you. Your opinion was important, not just because perhaps people

**[00:30:22]** like you as a person, but simply because you have, as someone once said, yes, you've

**[00:30:28]** seen horses throw up before, you've experienced all sorts of things

**[00:30:32]** and have an opinion and expertise based on all this experience that helps.

**[00:30:37]** now continue in the project. And if a project is in trouble, it doesn't really matter

**[00:30:41]** in which company, there was always someone you could say, oh yeah, has he then,

**[00:30:45]** Yes, has someone taken a look at it, because if someone knows, then they'll just call them.

**[00:30:50]** And that is becoming more democratic now.

**[00:30:53]** Now, it's not really the one who has the deepest knowledge

**[00:30:58]** in ABC who is automatically the most sought after, but rather the one who might be capable

**[00:31:04]** of creatively bringing together A and B, applying things, opening doors, connecting the right

**[00:31:10]** people with each other.

**[00:31:11]** So suddenly, completely different skills are emerging and adapting. I mean, who likes it when their tool, if you speak of a screwdriver, yes, today you have a screwdriver in your hand, that's a tool. Tomorrow it's a hammer, the day after it's a drill.

**[00:31:24]** Next week it's a jackhammer or something else, and then suddenly it’s a spoon. Yes, because the thing is striking and significant, new products are coming out and you have to keep your way of dealing with it always a little up to date.

**[00:31:37]** much more than before. And I believe these are some traits that we will

**[00:31:42]** increasingly encounter. I wanted to mention that. Thanks Jens for

**[00:31:46]** noticing this, so thank you for allowing me to say it again.

**[00:31:49]** Of course. You are a team. What do you see?

**[00:31:53]** Yes, definitely. Like a well-oiled machine. But only because I am always

**[00:31:58]** getting updated skills... No, no, I always get my updated skills

**[00:32:02]** in D, I throw that into my LL-M, then I know exactly how to

**[00:32:05]** And fortunately, I have to say, I made a thing on Github in my

**[00:32:11]** press information, so that all my Github pages always have that in the press information.

**[00:32:14]** And I took your Identity-MD on my Impressum’s Gill, so that I

**[00:32:20]** can always tell my AI how I think, what I expect, how I speak, so that I

**[00:32:26]** can address that and I have now also made it public, which means anyone

**[00:32:30]** could basically try out how I react, in the brand as well.

**[00:32:34]** Yes, I have my own identity in Debate, I don't even know how much I share it, but I've adjusted it a bit.

**[00:32:39]** But yes, another topic, we can also sometimes talk about that, because the issue of passing identities is also a totally important topic when I interact with an LMM.

**[00:32:48]** And especially, if we're not always working with the same one, then such identity files together with the context that I pass to the AI, whether I do it through a small database,

**[00:32:58]** or also through cat files or through prompts.

**[00:33:02]** I believe that will somewhat be the handshake of the future,

**[00:33:05]** the information handshake of the future.

**[00:33:08]** Because that’s already a different output.

**[00:33:10]** Whether it's Mark, René, you or I somehow talking to an AI

**[00:33:14]** or speaking with our trusted AIs,

**[00:33:16]** there will always be different results,

**[00:33:18]** because our identity plays a role in that.

**[00:33:20]** And I believe that's also an important core

**[00:33:22]** for the discussion for organizations that we have.

**[00:33:24]** The identity of us, that shapes an organization too.

**[00:33:28]** So, if we only start copying skills, we are now starting to describe our skills, what we do in our activities,

**[00:33:36]** then that is of course also broken down into the individual parts, as that small assembly line work,

**[00:33:42]** as described, this one small step that I take on the assembly line at that moment.

**[00:33:47]** This would probably also be reflected in our work maybe one or another time, when we describe our skills.

**[00:33:51]** But of course, additionally, it is the case with all humans that this identity comes into play.

**[00:33:56]** comes into play. And this identity changes a bit, also within organizations, because one

**[00:34:00]** has to still show certain behaviors all the time to figure out the best pathway out

**[00:34:06]** because nothing is perfect. It will never be the streamlined super AI organization.

**[00:34:11]** give in this sense. There will always be an interplay between an AI that fails, whose
 
**[00:34:15]** tokens have run out, where the server is shut down because
 
**[00:34:20]** someone just pulled the plug or something else happened. So this will also
 
**[00:34:23]** continue to happen in the future and accordingly, there is a need for identities in between,
 
**[00:34:29]** which we humans are also quite capable of, who can still react to such a system
 
**[00:34:33]**.
 
**[00:34:34]** We can also, if people are unsure, make a nice analogy.
 
**[00:34:38]** We have laws in the world, every legal state has laws, and yet we still have
 
**[00:34:42]** judges.
 
**[00:34:43]** Because what is between the laws must be interpreted and somehow weighed
 
**[00:34:47]**.

**[00:34:48]** And that can also be changed in our world just like that.

**[00:34:51]** The world is not logical at all; it's actually the opposite of logical, which unfortunately we see every day. But we need a middle ground in the sequences that happen in the processes to give a bit of an assessment, like, yes, oh, I think I'll just let this run, or no, I'd better stop this now because, for example, AI has no intention, AI wants nothing, so we first have to bring in the intention so that I want something.

**[00:35:18]** And then AI also has no risk assessment, so it can't say whether this now,
 
**[00:35:23]** I can maybe say a little bit like, okay, this could trigger a nuclear war, so I'm not going to do that. On the
 
**[00:35:28]** level, it might probably work by now, but on a, let's say, more normal level that concerns us every day, then someone says,
]}   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```  ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```  ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```  ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```   ```
**[00:35:35]** hm, maybe it's a bit too risky to let people stand ten meters closer to this high wool facility now and so,

**[00:35:42]** something like that, so this overall assessment can only be done, it can actually only be done by humans,

**[00:35:48]** and I believe always only by humans. That will be it, so the goal is also to automate this,

**[00:35:53]** but the operational side, the one that generates costs and eats up time, that's what we want to automate.

**[00:36:01]** But I would also say on some topics, I believe René, those topics could also be automated.

**[00:36:07]** So now, I'm going to take a critical look at China.

**[00:36:11]** What we are of course seeing in the factories on site is that we have a lot of workers who are basically performing repetitive tasks, and they are now being equipped with video cameras that record their manual work.

**[00:36:28]** Entire factories are completely fitted with video cameras, and the same small spot is being recorded, which you could also imagine on a larger scale.

**[00:36:36]** So not just sitting at a conveyor belt but also rolling through the offices,

**[00:36:41]** We can also document that I would do the entire roof if I went through the office,

**[00:36:44]** It was something to deduce what is needed, what does one want,

**[00:36:50]** But what does such a robot actually need, and another topic that I will just throw in as criticism,

**[00:36:56]** That was something I also saw, where I was also surprised, where fortunately quickly,

**[00:37:00]** a folding was also loaded.

**[00:37:02]** There are certain Chinese companies that are already forcing their employees to basically,

**[00:37:06]** really document their skills through their activities, in order to then say, yes, this

**[00:37:11]** I can automate later with an AI what this person does.

**[00:37:16]** Interestingly, a service was created directly, which was called, let me check,

**[00:37:19]** Anti-Distillation Skill, that's great, there's a Chinese woman,

**[00:37:24]** She wrote it directly.

**[00:37:27]** I was just about to say, one in three can probably pronounce it.

**[00:37:34]** But the skill helps you; it's like a cleaning layer.

**[00:37:39]** It pulls out all the really interesting things you wrote in your skill,

**[00:37:45]** pulls them out and leaves you just the bare essentials to tweak a bit here,

**[00:37:49]** do a bit there.

**[00:37:51]** And you can hand that over as management. You can be sure that if

**[00:37:54]** management uses the MD skill, your job will still be needed.

**[00:37:59]** Those are of course also. So the care side of the coin. We have to somehow

**[00:38:03]** talk openly about that these things happen.

**[00:38:05]** Yes, well, I lived in China for a few years and I definitely have, let's say,
 
**[00:38:10]** my own perspective. I actually find the order of freedom super,
 
**[00:38:15]** and I don’t think total surveillance is great, that's clear. But within that system,
 
**[00:38:19]** the railway itself. So it's not that bad at all. It's actually very efficient when you
 
**[00:38:27]** mention the railway, and it’s no coincidence that currently it's the
 
**[00:38:31]** global winner. First of all, they don’t make idiomatic mistakes; they function,
 
**[00:38:35]** they go in very slowly and now, if you look at the last five-year plan,
 
**[00:38:41]** which he has looked at with twelve points, there are six points where they want to become world leaders
 
**[00:38:45]** and six others where they at least want to achieve global breakthroughs, and in this, there's quantum
 
**[00:38:52]** involved, breakthroughs in that, there's also Neuralink in the brain and so on. And that,
 
**[00:38:57]** their concentrated and focused use of technology is also due to the fact
 
**[00:39:05]** that this nation will lead globally in this technology and that’s why it’s also
 
**[00:39:10]** more a business model, to try something out so that the others around the world,
 
**[00:39:14]** who then have to buy the technology to reach productivity, thus become
 
**[00:39:20]** customers. It’s quite simple. Yes, so my personal freedom is very
 
**[00:39:27]** important to me. I would never accept that. It’s probably hardly possible in a western
 
**[00:39:31]** society anyway. But we must not be so parochial and
 
**[00:39:37]** disregard that China has had a culture for thousands of years. That
 
**[00:39:42]** doesn’t mean that people there feel differently or that freedom is just valued differently.
 
**[00:39:49]** It is simply a different good, as a different good is.
 
**[00:39:53]** One is not better than the other; it’s a different valuation, a different system.
 
**[00:39:58]** We don’t have to like it, you don’t have to like us.

**[00:40:01]** I always have something that relates to a completely different example.

**[00:40:04]** When I lived there, it was still very common to spit on the street in China.

**[00:40:10]** So we find that not only spitting, but I won't demonstrate it, but you can imagine, really from the depths, because behind it was the idea of cleansing, letting the unclean out of the body.

**[00:40:24]** At the same time, all the Chinese people I spoke to looked at me with disgust when I sneezed, when I went 'Hatshi'.

**[00:40:33]** They looked at me with disgust and said, oh, what is that? Just as disgusted as I was.

**[00:40:37]** One is not better than the other, but there are simply different perspectives in a cultural context, and you have to learn that there are differences and deal with the differences without judging.

**[00:40:50]** But now back to technology.

**[00:40:52]** There is this high affinity for technology.

**[00:40:55]** I can only recommend to everyone to find some x-random video that is not older than three or four months on YouTube about Shen-Sensee.

**[00:41:03]** Man, and I have experienced parts of what is being shown live, so the technology, to already introduce skill-based work in companies now.

**[00:41:15]** Training sessions with a camera on your head so I can run alongside and that later a robotics will even, not only on the robotics and the world leaders, world market leaders, they will look at it as it is today already.

**[00:41:26]** This is part of the overall plan of this industry or this nation, let's say.

**[00:41:33]** And I dare say they will be very successful with their plan.

**[00:41:37]** So, when I think about when we made our episode from Open Claw,

**[00:41:42]** we saw in preparation how there, let's say,

**[00:41:45]** installation parties or installation services, I don’t know what else, take place.

**[00:41:49]** And when you walk through there, no matter where, and talk about Open Claw,

**[00:41:55]** you first hear, yes, help. So, no, I don’t know. More the rejection.

**[00:42:03]** Or difficult to convince, you get hit back, while there are people sitting

**[00:42:09]** with whatever drinks and notebooks and installing themselves

**[00:42:14]** the stuff, while we, so to speak, not us as a company or us as

**[00:42:19]** individuals, but more as a society, are thinking, oh, damn it and

**[00:42:24]** couldn't we regulate something or anything? Yes. And it somehow goes

**[00:42:29]** fire at will. Maybe somewhere in between lies the truth, where one

**[00:42:32]** might meet. Yes, I wanted to say, there is no truth.

**[00:42:35]** Both have their validity. We have a different culture and we want

**[00:42:38]** to understand things. It's said that the Asian way is

**[00:42:43]** more about the journey than the destination. For us, the destination is the goal. And

**[00:42:48]** both have their validity. One is not better than the other.

**[00:42:51]** Right now, it seems one is faster, okay? So we can also actually see how much in particular Europe is currently not functioning. That is also all true.

**[00:43:01]** But over the entire, let's say, the next ten years, it will also readjust. So every culture has its advantages at the moment.

**[00:43:09]** But behind it, in China, there is definitely a large business model. And Open Cloud Installation is now a service.

**[00:43:16]** Service. You go like to a kiosk, bring your device with you, and an hour later

**[00:43:19]** everything is installed by someone. That brings us back to skills. That would have

**[00:43:26]** I could have used it in the last few weeks because I've spent some nights here
 
**[00:43:30]** with one, I do it very, very carefully and very safely and I want to as well

**[00:43:33]** learn for myself again and what you do there. And I must also say, honestly

**[00:43:37]** also this process that I have now gone through again, just with this Orpenclaw installation,

**[00:43:42]** also with the topics about the Mark and which I then also exchange with Spalinkt in us,

**[00:43:46]** how to build a memory like that, how to set up a Bolt, how to essentially

**[00:43:50]** establish the handshake between agents and such. I believe it was necessary that

**[00:43:54]** I went this distance to feel it for myself again. And

**[00:43:59]** I think that's also kind of a thing, I have to say.

**[00:44:00]** Yes, it's simply valuable when you deal with technology that, to be honest,

**[00:44:07]** is also so easily accessible, is preoccupying. So, to put it bluntly, I have

**[00:44:11]** done. I basically just did this installation and keep asking

**[00:44:14]** all the time, wouldn’t another AI be different from what I’m actually doing? And let

**[00:44:17]** me explain that too. Forget it sometimes, I really don't have to. So as always

**[00:44:20]** ask again when I no longer remember the next terminal command.

**[00:44:22]** But it's possible, you know? So I’m doing things, I’ve also

**[00:44:26]** activated my GitHub, which had been dormant for five years,

**[00:44:30]** again. Careful, I put everything from back then

**[00:44:32]** on private, so it’s not so embarrassing, because they are rather old

**[00:44:34]** honestly. But despite next, so the call again,

**[00:44:39]** so get involved with these things. It’s something different when you experience it,

**[00:44:43]** because you come up with new ideas, you understand what it means. And that's why I come across topics,

**[00:44:49]** which are partly not really addressed yet. Who keeps the

**[00:44:55]** context alive in principle? So this contextual information that is necessary, which for example in

**[00:45:00]** a normal organization is maintained through meetings, through information exchange, that I am

**[00:45:05]** trained in my skills through a university or through a career path,

**[00:45:11]** that I know what norms, what security checks or any

**[00:45:15]** other things need to be done when I want to provide something. Who keeps all of that

**[00:45:19]** running in this agentic world in the future? That's going to be a totally exciting question. It is

**[00:45:23]** never really answerable, honestly. I see that right now. When I take on these things,

**[00:45:27]** these little errors keep popping up, whether they are just small,

**[00:45:31]** temporary errors. If one AI thinks that the other has already done something,

**[00:45:35]** but hasn’t finished yet. If a model on my local machine is actually supposed to

**[00:45:39]** do something, but times out because it hasn’t warmed up yet and the other

**[00:45:43]** then just going back and doing something, even if there is already confidence

**[00:45:48]** Gores or something different in the light side. So that is complex, I'm really glad,

**[00:45:53]** that I managed to push through a few night shifts over the last months and weekend shifts

**[00:45:58]** in order to get through it, because it helped me a lot to understand these things better

**[00:46:02]**. And I believe that is still valuable in this world we are in

**[00:46:05]** and engaging with these topics.

**[00:46:07]** And this is, if I support a call to action, for everyone who is currently listening,

**[00:46:12]** so not everyone has to tear themselves apart with open-cloid. That’s perhaps, only people do that

**[00:46:15]** who really have a bit of knowledge, because there’s always a security risk involved

**[00:46:20]** and you simply have to know what you are doing. But for example, to engage for

**[00:46:24]** a weekend with a topic, with cloud code, and to deal with it

**[00:46:29]** to ask or also on the i-codex or or or google i studio and maybe write a
 
**[00:46:34]** piece of software myself I am convinced that this is today a
 
**[00:46:38]** live skill just like we all know how to change a tire it can no longer
 
**[00:46:43]** be done but we understand it in principle this is a live skill that one
 
**[00:46:47]** understands the mechanics of so that it doesn’t look like one of those

**[00:46:51]** black box and I have absolutely no idea and one can

**[00:46:55]** program a small game, it doesn't have to be big, something

**[00:46:58]** Some kind of hangman game, some word guessing game, it's probably a prompt with five words and then it happens automatically anyway, but at least you can see how it works.

**[00:47:08]** So, dealing with it is really important.

**[00:47:11]** Totally, totally.

**[00:47:12]** I actually, because you mentioned the game, in my youth I played a game called Bubble Bobble.

**[00:47:18]** Back then, you controlled these little dragons that shot balloons, not soap bubbles.

**[00:47:24]** I loved that back then, but somehow you can't really find it anywhere anymore, and I think it was Gemini that built it for me again.

**[00:47:31]** To which I said, look at this and that, and here are a few websites and a few videos, check it out and do it.

**[00:47:37]** It was quite funny, and while you were talking, and you brought up the tire change example, I thought of another example.

**[00:47:43]** I mean, now we've all been betrayed, we won't reveal any details, but there may have been the odd hiccup in the IT world or seen one or the other thing.

**[00:47:51]** When I started with IT, so in my internship, there were punch cards, and later I worked with DOS Terminal, and for me, word processing didn't even have

**[00:48:01]** What you see is what you get, yeah, but you've worked a lot with text, like.

**[00:48:05]** Then eventually Windows came and the graphical user interface is like blah blah blah and that's quite nice.

**[00:48:09]** And people looked at me as if I came from another planet when I was still using Windows back then; those who know me know it must have been a long time ago.

**[00:48:18]** I then said here CMD, I think that was it back then with Windows, so you get to the terminal, i.e., DOS, and they were like, what's that black window? Where's the color? What are you doing there? And you're thinking, hey, what do you want from me? This is DOS, so you can enter something here, create, move, and delete directories, and I don't know what.

**[00:48:39]** and it was independent of the fact that I haven't actively used Windows since Windows 19

**[00:48:44]** I'm using. Is it still knowledge when you know how it is

**[00:48:48]** terminal and what is it based on? Definitely something you learn, oh I see'

**[00:48:53]** that already, shaking my head for everyone who is just listening. Is it definitely

**[00:48:58]** something that has accompanied me on my learning journey and today

**[00:49:01]** is still valuable knowledge for me to understand how the

**[00:49:05]** whole thing is connected and I believe that takes away this whole

**[00:49:08]** AI journey, when models, methodologies change every two, three, four, eight, twelve weeks.

**[00:49:13]** Whatever the case may be. It doesn't take away from us because we are on this journey, yes, because we

**[00:49:18]** walk with an open heart and accompany this journey and do not shy away from it.

**[00:49:22]** close our eyes and say it will go away and no idea, what and us

**[00:49:26]** let ourselves be surprised, but we are going on this journey. Jens, you shook your head.

**[00:49:31]** Yes, I just reacted, all good. I am, yes, I shook my head, everything,

**[00:49:34]** I am, let's say, up to a certain degree.

**[00:49:37]** Well, I actually think it's also a graphical,

**[00:49:40]** where you can use such an area well, because not everyone has to think their way

**[00:49:43]** into everything all the time, and I want to do something similar to what René just said.

**[00:49:46]** Not everyone needs to set up an Open Cloud installation outside,

**[00:49:48]** to engage with the topic of AI.

**[00:49:50]** That simply doesn't need to be the case, and similarly, not everyone has to do two Open Cloud installations.

**[00:49:54]** Exactly, it doesn't have to be any of that.

**[00:49:56]** We don't have to move around in a terminal environment anymore.

**[00:49:59]** Yes, the reason I do it now is simply because

**[00:50:02]** it is just easier to work with the Cloud Code Agent.

**[00:50:05]** also working as a terminal window, to then copy things over from one terminal window as another

**[00:50:08]** and so on. Yes, but that shouldn't be the end of the line,

**[00:50:12]** because we need to keep moving forward, ensuring that it's accessible for the

**[00:50:16]** rest as well. And I think the only point I would emphasize is,

**[00:50:21]** that fundamentally, it's understood what you're saying, how can such a thing work? What is

**[00:50:27]** perhaps a folder structure, even if I don’t need to know anymore on the iPhone,

**[00:50:31]** where the pictures are stored in which folder.

**[00:50:33]** It's still okay for me to know that, just as it was okay when I started

**[00:50:38]** back then, when it was said, yes, one didn’t work with a WYSIWYG editor, but

**[00:50:41]** rather occasionally with BabyEdit to describe the code oneself or

**[00:50:45]** something else.

**[00:50:46]** In the end, maybe with a Visibik editor, or back then already against or something like that.

**[00:50:49]** To fundamentally understand what is happening, I'm with you, because I believe René

**[00:50:53]** has already reacted, as Alte, as Thila, yes, and because we also still

**[00:50:57]** say, no, you all have to work in the terminal.

**[00:51:00]** Yes, exactly. But I want to make a point. Why? So, it's not so nerdy at all.

**[00:51:06]** Mark and I, we are of course the mega nerds, sure. I’m also hitting myself the whole time.

**[00:51:10]** But I believe, for the world out there, for the people, it's important to remain sovereign.

**[00:51:17]** So that it doesn’t feel awkward, that you don’t feel uncomfortable, because when you press the button, what happens then?

**[00:51:23]** Everyone knows you don’t feel awkward when you get in the car and drive, because somehow you know up front,

**[00:51:29]** usually in the motor, there are also people that come to mind, yes, but in principle, let’s say,

**[00:51:37]** or conversely, the people who drive with great insecurity are also the ones who have absolutely no clue about the whole thing.

**[00:51:43]** There’s a slight correlation, just a little bit, that means, since the world is increasingly being

**[00:51:52]** equipped with IT artifacts, hopefully changing our lives, simplifying it,

**[00:51:59]** but also making it very complicated. It is advisable for everyone to navigate confidently

**[00:52:06]** in this world by at least having a true sense of what is actually happening?

**[00:52:10]** That makes me, yes, sovereign, simply, I am not so dependent, I don’t feel so

**[00:52:18]** alone. I feel okay, I can handle it, I can assess what happens. I can take the

**[00:52:25]** next step, I don't stand still. When I look at it like this, I mean, what have

**[00:52:29]** we talked about today? I believe what comes across to the listeners is that skills are more

**[00:52:36]** than just the skill that the agent learns. Skills is, yes, how the agent already approaches the topic

**[00:52:43]** of work skills, but also how does the person handle it? How do we as humans

**[00:52:48]** deal with each other and with skills? And the third was also the topic of how does one

**[00:52:52]** handle it as an organization? We had the topic of boxes, flat hierarchies. And I believe, and the question

**[00:52:58]** I don't want to dwell on that too much, I just want to leave it with you for some thought,
 
**[00:53:01]** to think about it again. Last time on the podcast you said, not with the motto,
 
**[00:53:06]** What do I need soon, or what do I need in five years, but how will it be in 50 years,
 
**[00:53:13]** you had brought it up similarly, I believe, for the first time.
 
**[00:53:16]** From that perspective, I found what we discussed today totally fascinating, I also found it totally exciting,
 
**[00:53:21]** what has all happened since our last time, we hinted at it briefly at the beginning,
 
**[00:53:25]** because if we had said back then what technology is today capable of,
 
**[00:53:32]** I think we all would never have thought, and I personally do not exempt myself from that,
 
**[00:53:37]** that these technological possibilities, which emerged at the time of recording,
 
**[00:53:43]** and also the recording is on a different day than the broadcast. From that perspective,
 
**[00:53:48]** let's see what might come by then as well. This is a fascinatingly intense time.
 
**[00:53:52]** Yes, so from that perspective, I don't know how you all feel, but I found it very successful,
 
**[00:53:58]** While we were talking, I definitely want to get in touch again, so that we can
 
**[00:54:02]** have another episode someday, because I mean, this is a totally exciting
 
**[00:54:05]** topic.
 
**[00:54:06]** And from that perspective, unless someone feels they would like to give a concluding word
 
**[00:54:10]** to us.
 
**[00:54:11]** Yes, I would just give you a great tip, so try to always discuss people
 
**[00:54:15]** from a year ago and then discuss the delta basically what was discussed back then
 
**[00:54:20]** for about 10 minutes.
 
**[00:54:21]** Yes, gladly.
 
**[00:54:22]** The 10 from back then, a year later, riff again with the same person.
 
**[00:54:25]** That would certainly be exciting.
 
**[00:54:26]** I would be happy to offer that as well.
 
**[00:54:27]** And for all listeners, think briefly about yourself now and a year ago, what you believed
 
**[00:54:35]** a year ago was possible today, what is actually possible today. And this delta
 
**[00:54:40]** can also be projected forward. Then you have a little idea that the environment
 
**[00:54:44]** is inevitably approaching us, but in such a positive sense that we can draw a lot of
 
**[00:54:49]** impact from it. So engage with the topic. That’s the most important thing,
 
**[00:54:53]** that you could tell yourself and yes I think it's really great to chat with you, it's really great because we
 
**[00:54:59]** can all tell that everyone has content, everyone is talking about something and with content and Jens your open talk,
 
**[00:55:06]** I’d love to take a look at that,
 
**[00:55:10]** But with that background, man, man, then I would joyfully
 
**[00:55:17]** initiate the closing, no thanks for being here,
 
**[00:55:20]** Yes, as always a pleasure. Jens, it's nice that you're also part of an episode with a guest.
 
**[00:55:27]** I always enjoy that. By the way, we have the next one lined up.
 
**[00:55:30]** That’s carnival.
 
**[00:55:31]** That’s carnival.
 
**[00:55:32]** That’s a repeat offender.
 
**[00:55:33]** You still need to correct yourself so you don’t miss the next one.
 
**[00:55:35]** You have to say it’s carnival and not faschingen.
 
**[00:55:38]** You say that to a Hessian, you know?
 
**[00:55:40]** I can handle that, Würmscher on the Türmsche, with the Schirmscher and at the Ämge comes the Stürmscher,
 
**[00:55:43]** Würmscher with the Schirmscher and at the Ämge from the Türmsche.
 
**[00:55:45]** You know, I can do that, right?

**[00:55:47]** And I can't separate fascism and carnival there.

**[00:55:49]** Yes, I used to be from Hesse, went to school in Rhineland-Palatinate.

**[00:55:53]** Someone once said to me, so you're going over to the Lacher in the Anne Bundesland.

**[00:55:56]** Well, let's leave that aside for now.

**[00:55:58]** It was nice with you all.

**[00:56:00]** Thank you for being here.

**[00:56:01]** I'm looking forward to the next one.

**[00:56:02]** If you liked it, then leave a like.

**[00:56:04]** A comment, tell your friends and acquaintances that this podcast exists.

**[00:56:08]** Should listen to an Openclaw or a myth.

**[00:56:11]** We come in peace and are happy to have you as subscribers.

**[00:56:14]** And with that in mind, I thank you, see you soon.

**[00:56:17]** Bye.

**[00:56:19]** Welcome to ThinkDifferent, ThinkAI, the podcast by Mark and Jens.

**[00:56:25]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:56:31]** Here you will find clear classifications, real practical insights, and a fresh look at what is possible.

**[00:56:38]** Understandable, critical, and always with a wink.

**[00:56:42]** H.I. for thought, for a chuckle, and above all, for conversation.
