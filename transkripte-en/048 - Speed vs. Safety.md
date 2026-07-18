---
title: "Speed vs. Safety"
episode_index: 48
published: "Sun, 12 Jul 2026 20:45:00 +0000"
duration: "1375"
page_url: "https://think-ai.podigee.io/48-speed-vs-safety"
image_url: "https://images.podigee-cdn.net/0x,ssU3eIDt4PMhj5EhrwWKUk1v5vCaSqSQEYpBnNyOK6lM=/https://main.podigee-cdn.net/uploads/u73317/a0832141-5b78-438a-a0b5-a34268a38a5f.jpg"
audio_url: "https://audio.podigee-cdn.net/2532882-m-e89974e8241169c3f9d0e6554501c339.mp3?source=feed"
guid: "b5407179e715825a43366ef5c3613e16"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-07-13T09:29:16+00:00"
translated_from_language: "de"
translation_provider: "local"
translation_model: "Helsinki-NLP/opus-mt-de-en"
translated_from_file: "transkripte/048 - Speed vs. Safety.md"
translated_at: "2026-07-18T13:29:27+00:00"
---

# Speed vs. Safety

**Published:** Sun, 12 Jul 2026 20:45:00 +0000
**Duration:** 1375
**Web player:** https://think-ai.podigee.io/48-speed-vs-safety
**Cover:** https://images.podigee-cdn.net/0x,ssU3eIDt4PMhj5EhrwWKUk1v5vCaSqSQEYpBnNyOK6lM=/https://main.podigee-cdn.net/uploads/u73317/a0832141-5b78-438a-a0b5-a34268a38a5f.jpg
**Audio:** https://audio.podigee-cdn.net/2532882-m-e89974e8241169c3f9d0e6554501c339.mp3?source=feed

## Description

Myth, Fable and the Return of Limited Models
What do you do if your own loop engineering episode of last week is overtaken by reality before the ink is dry? That's exactly what happened to Mark and Jens, so there's this spontaneous addition. The trigger is Fable, the Anthropic model that was blocked for non-US citizens a few days ago.

The strategy of the U.S. government could be to give selected companies and their own administration a lead in closing precisely these gaps before models become similarly efficient from a less controllable hand. From there it goes to distillation: Chinese models build up the capabilities of large U.S. models by practically extracting the knowledge from the Token Prediction with automated mass inquiries. This is also hard for companies that had directed their processes too early on a single model. Mark and Jens report from law firms that had converted their complete text analysis to Fable and are now faced with exactly this problem when the model is shut down. In addition, a new challenger named Fuku (from a provider whose name must first be remembered in the conversation) also emerges, claiming his own record benchmarks.

Directly after the loop engineering episode of the previous week, it's about the practical limits of loops: Jens reports about a multi-day lock at Anthropic, after he had used up his weekly limit in the Max plan on a single evening. A second case is even more treacherous: If a loop hits an API limit in the middle of the work instead of a model limit, it breaks off, but after a simple "go ahead" it returns as if everything had been done, along with the casual remark that there were eight crashes to be repaired. In the end, a result that looks like a normal prompt, not like the actually desired thorough iteration. The call of the episode: away from pure prompt engineering, to the loop engineer.

At the end of the day, the two consider how early this phase of AI development is actually, comparable to the Internet around 1997: many things are already working, but there are still no established standards, but the first price sellers who promise the big money are already doing so. One point of contention is commodity-harnesses such as ChatGPT, Gemini or Anthropics Cowork compared to their own self-made agent Harness, who has to cope with constantly changing models and environments. Mark tells of someone who has dismissed his self-made Harness result as "such a JSON app", an occasion for their own, more detailed Harness engineering episode, which the two announce. Despite all the setbacks, Mark and Jens remain optimistic: they compare the current phase with the iPhone moment, after which only applications like WhatsApp were created, which no one has seen before, and expect similar results for spontaneously generated software instead of ready-purchased programs.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence, but live it.

**[00:00:14]** Here there are clear classifications, real practical insights and a fresh look at what is possible.

**[00:00:20]** Understandable, critical and always with an eye tinker.

**[00:00:24]** Hadi to think, to smile and above all to share.

**[00:00:33]** Welcome to Think Different, Think AI.

**[00:00:37]** Jens and I met in person again.

**[00:00:40]** Unfortunately not in such a beautiful hotel lobby as last time.

**[00:00:43]** But nevertheless, with a cool drink after the hot days in hand.

**[00:00:47]** And we have determined for ourselves,

**[00:00:49]** that the last episode we recorded,

**[00:00:52]** you could hear last week,

**[00:00:54]** so current is that we had to saddle up on it again. Jens, we have the last time about such

**[00:01:02]** Things spoken, like prompting, skills, loops, and in the run-up to that, we had at some point

**[00:01:08]** we talked about Favel 5 and now we've said it all hangs somehow

**[00:01:12]** What hasn't happened or happened since then? Yes, of course we have this,

**[00:01:21]** We have recorded the loop sequence and I think it fits quite well that we now

**[00:01:24]** again make this current addition to this loop sequence, because the listener among you

**[00:01:29]** And the AI enthusiast, as we are, has embarrassed him who has noticed.

**[00:01:34]** Fabel had, or Atrophic became quite familiar with Fabel a few days ago, then is

**[00:01:40]** it's been turned off, we've done a whole episode about it, you'll know it.

**[00:01:43]** The subject.

**[00:01:44]** Now this weekend is again, such things happen apparently always

**[00:01:48]** on weekends.

**[00:01:49]** And it has nothing to do with VW or BSF.

**[00:01:52]** No, but they are existing stories.

**[00:01:54]** Apparently, where things from America swarm over here and are decided.

**[00:01:57]** In fact, it's another model.

**[00:02:00]** once again unlocked,

**[00:02:03]** and another model, however, has announced that your model,

**[00:02:06]** that you planned, the way they are, if I'm right,

**[00:02:08]** that of OpenAI, that was the 5.5 that actually blew.

**[00:02:13]** No, 5.6, 5.6 there is.

**[00:02:15]** It's so funny, no, because the one gets a call,

**[00:02:18]** that he should hold back his model a little bit more and not first

**[00:02:21]** I want you to release according to the motto, you don't want to, that means with you what happens.

**[00:02:25]** And the other one released Fable 5.

**[00:02:28]** Unlike what we have known so far, the whole situation with

**[00:02:32]** around AI, that the things have actually been cheerfully posted into the world,

**[00:02:36]** We seem to be entering a new phase now.

**[00:02:40]** What speaks for the quality of the models, of course.

**[00:02:42]** These models are to constantly develop them.

**[00:02:46]** In other words, they are getting better and better, and, of course, they are becoming more and more dangerous.

**[00:02:53]** that they outperform us in many abilities and, above all, now in ability,

**[00:02:58]** we used to show, we thought we programmed something well, we did

**[00:03:00]** which certainly programmed earlier.

**[00:03:02]** Now the things come around the corner and discover relatively quickly that this is not so, yes,

**[00:03:06]** that we were god-like programmers we used to be, but not so error-free

**[00:03:10]** Errors free. Exactly, errors free, until now not so many errors were free and accordingly, because somewhere are relatively many security gaps, which are cracked by these new models in a winch rope.

**[00:03:22]** I believe that somehow the government has also said that the American government has also cracked its systems of myth in a few hours.

**[00:03:29]** So this is really a range that requires a regulatory approach.

**[00:03:34]** But on the other hand, of course, also a bit of time, how dependent we are now.

**[00:03:40]** I mean, faithful, listening to our podcast, we've certainly noticed too.

**[00:03:45]** There are not only American models, there are also, for example, Kinese models.

**[00:03:51]** Yes, here we want the French model with Ralf out of the way in the explanation

**[00:03:58]** And now that we're supposed to be an insinuation or something.

**[00:04:02]** But also the Chinese models will probably notice what's going on here, because that's a

**[00:04:07]** or other model you have read or heard at least once, is by distillation

**[00:04:13]** ==References====External links==

**[00:04:15]** So you have to imagine that providers, let's say, have a lot of inquiries.

**[00:04:21]** and talks with the US models have been automated to

**[00:04:26]** virtually replicating and replicating these models.

**[00:04:29]** It's Art Ree ingenuities.

**[00:04:31]** They've actually rehearsed, they've seen you say I'm making 100,000 requests.

**[00:04:35]** on the topic, how to go fishing best, then these models answer yes also in 100,000

**[00:04:43]** Variants that are very similar.

**[00:04:45]** So that basically the right guide comes out, that I take a fishing or something

**[00:04:47]** other and the bait and whatever.

**[00:04:51]** And get a dynamite, you've seen so many movies.

**[00:04:53]** And from this, so this, with a certain probability, because we

**[00:04:56]** I've all heard of the subject of probability calculation in Mittehrund, the Token Prediction.

**[00:05:01]** And in order to get them out again, quite a lot of inquiries were made to these American models.

**[00:05:06]** And that's how you basically understood how this model works and built it afterwards.

**[00:05:11]** There were stories that some of the Chinese models were put on like this.

**[00:05:15]** And what I thought was funny is the other thing, that there are even companies in the eye that go to court,

**[00:05:23]** Because immediately after the appearance of Fabel they had recognized the potential and their business processes

**[00:05:32]** have already optimized on it and said that this is practically a model that so good it in

**[00:05:37]** the text analysis, I think that was a sugar lawyer, so good in the text analysis that they

**[00:05:43]** no one wanted to do without it anymore, have changed everything on it and then is

**[00:05:46]** of course double annoying, if then at once it is said, so, we put

**[00:05:51]** the model one, where it is fair to say that the model has not been officially discontinued

**[00:05:56]** The only thing they said was that you have to make it happen to the US government.

**[00:06:00]** This is of course a bit difficult in times of Amazon badrock access,

**[00:06:05]** APKs and didn't see it. So they generally turned it off.

**[00:06:09]** It says there, as a company. And there is also such a bit of the circle to this

**[00:06:13]** Loop sequence. If you always try to be in front of bleeding edge, then

**[00:06:18]** you can't just fall on your nose because, well, you're just going into new land and causing

**[00:06:23]** either cost or need to learn how to deal with it.

**[00:06:26]** Never!

**[00:06:27]** It may even be that your business process is based on it, because the model is sounding off.

**[00:06:32]** Here again a good point, because I was not so aware that I now

**[00:06:35]** Of course, it wasn't until a day when you were talking.

**[00:06:37]** Also other model ambitions, whether by destination or by own model development, are

**[00:06:41]** It is highly likely that we will come to the status that we now have in the large models.

**[00:06:45]** have.

**[00:06:46]** nice with how much thought you go in here and you say it American

**[00:06:52]** As always, the government has been thinking very carefully about what I am doing.

**[00:06:57]** it was quite funny, myth appeared as a myth and it was still said that it was just

**[00:07:02]** a very limited user group available, we also had in the podcast

**[00:07:06]** from the report, it was also listed as a model at Amazon Badrock in the EU zone, in

**[00:07:13]** Frankfurt, where I then also thought to myself, hey, if there is this ominous superduper and

**[00:07:18]** I break out of everything model is whether now the Eurozone Frankfurt at Bad Rock so the

**[00:07:23]** I don't know, we'll have to see if that's still there.

**[00:07:29]** I'm sorry, but do you remember what this model is called, and now it's out.

**[00:07:33]** that a bit says it has Fable 5 options, because it's not a model,

**[00:07:40]** It's more of an orchestrator.

**[00:07:44]** I think something about Fuku, I'm afraid I might have to call it up.

**[00:07:50]** Honestly, I have no idea what they say, maybe it's the same to us.

**[00:07:54]** We'll talk to you for sure. That's what I thought was funny, like models at once.

**[00:07:58]** sprout from the ground or process from the ground that claims to be,

**[00:08:04]** the benchmarks that these large models have presented for a few days and from

**[00:08:14]** the side, I like it, what's it called? Schalkana, AI, Fuku. Yes, that's what I know,

**[00:08:21]** that I always love to do the podcast with you, because you're just the one who's made.

**[00:08:27]** but that's like again on the subject that I just had a few moments ago with the

**[00:08:31]** Looping, because we did some loops.

**[00:08:35]** Looping, yeah, we'll do loops, then we'll have looping.

**[00:08:38]** Looping.

**[00:08:39]** He'll tell you before.

**[00:08:40]** Exactly.

**[00:08:41]** It is clear, of course, that the consequences of this

**[00:08:45]** We have to make a baking operation now, if we, as we have introduced Poland,

**[00:08:49]** World are where I can no longer be sure that a large model that is outside

**[00:08:56]** is still on the market when I wake up in the morning.

**[00:09:00]** So this beautiful storyline, I'm gonna put on a loop here, and maybe hundreds of them,

**[00:09:05]** So we always hear that, when we look at it, hardly one of the big models

**[00:09:10]** is still programmed by programmers at all, this is only being lubricated, so many

**[00:09:14]** of the large AI programmers and sizes that sit in the model companies, say we

**[00:09:20]** don't do it myself anymore, I'm just there to build loops.

**[00:09:25]** So, if the essential part of a loupe then disappears, the AI model in the background,

**[00:09:32]** Well, then your boobs are just for an ass, honestly,

**[00:09:35]** But they can't get any further.

**[00:09:36]** So that's how we have to, everyone has to, I think, think about it.

**[00:09:40]** And we've often talked about it before, so the subject of Harnes Engineering,

**[00:09:44]** how do I build up my entire AI setup, how is my AI architecture actually?

**[00:09:49]** You might have to think about this two or three milliseconds longer and not

**[00:09:54]** I think it would be a good idea if we were to be able to do something about it, so that in principle we could build a system, which would then have to do something about it, so that we could do something about it.

**[00:09:58]** is also robust and also prevent or avoid such failures in an emergency

**[00:10:04]** can or can at least intercept in such a way that there are not so critical situations

**[00:10:08]** Somewhere.

**[00:10:09]** I would have fallen for another thing too, which on loops on the boards

**[00:10:14]** (Parliament adopted the legislative resolution)

**[00:10:15]** If they follow me like this, they'll have seen that I was forcibly locked up again the other day because I'm afraid of all the tokens that detropic in the big Max plan.

**[00:10:27]** Well, no, but I was kind of banished for several days because I used up my weekly limit.

**[00:10:34]** You should just use this fee-workflow-slashcode.

**[00:10:39]** This is a fair point when the models come to token limits, if you

**[00:10:47]** the one or the other thing that struck me,

**[00:10:52]** I noticed my attempts to work with loops.

**[00:10:57]** You give the system a lot of data, and you say do your loops over it.

**[00:11:02]** If you do not make sure, for example, that text blocks are sufficient

**[00:11:11]** are large or small, with sufficient size or small, is chosen extra spongy,

**[00:11:15]** Because I don't know what's big or small, but you'll soon notice what's going on.

**[00:11:18]** you want out.

**[00:11:19]** Because I told that thing you'd watch out, big books here, mill you.

**[00:11:23]** I want you to do this with a Goal Loop.

**[00:11:28]** so do until the following questions are answered and all at once everything is

**[00:11:32]** All shot into Nirvana. It was in yellow on the screen.

**[00:11:37]** AP Limit Reached, cling to it. It's not the Model Limit, but you have

**[00:11:44]** simply bombards the API. We don't go on. So, then you say to him,

**[00:11:49]** And then he says, oh yes, totally great. You, I'll continue, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah, blah

**[00:11:55]** work again, error again. At some point he noticed, oh you, I should maybe my

**[00:11:58]** Reduce queries so that this doesn't run against the limit and all, quite, at the end he says,

**[00:12:04]** You're done with everything, by the way, we've had eight crashes.

**[00:12:08]** what's broken and you think so, okay, the go-loop's broken,

**[00:12:14]** then you have to keep on saying and the result was like when I had a normal

**[00:12:19]** Promptly would have written everything I checked on you and make sure and that's

**[00:12:25]** The KPIs. He pushed it all over the aether for these moments of demolition.

**[00:12:30]** So I thought I didn't even need an American government.

**[00:12:34]** which shuts down more modernly. There is also one inability of its own and I call with it,

**[00:12:38]** No longer for prompt engineering, but for loop engineer. Yes, but the loop engineer,

**[00:12:45]** I think this is a special point, we have to think about this whole AI-Hab topic and

**[00:12:50]** We are also always at the forefront of this, if we are conceptually

**[00:12:53]** We're going to throw around, then we're going to come around the corner with new topics.

**[00:12:58]** Experience of the last two, three years now with the topics shows simply, we are all

**[00:13:04]** still early. All things are just relatively new. That means there is not yet

**[00:13:12]** the optimal loop engineering school you say, if you do that, then it's running

**[00:13:18]** That, too.

**[00:13:19]** I'm sure there's an influencer who'll give you that for a course.

**[00:13:21]** That's right, definitely, you can make money in the millions right now if you do.

**[00:13:26]** Anyone who's tried a workflow before, let's just build two AI mutals in a row.

**[00:13:33]** He'll notice that he'll have to work again and again.

**[00:13:36]** There are always these places where we are currently working, where we must always be the famous man of Belup,

**[00:13:42]** who just can't just be on-belup and somehow can sit on his ascienda

**[00:13:47]** and can enjoy the sunshine and the coyotes want to count.

**[00:13:50]** No, we still have to wait indefinitely, we don't know exactly how

**[00:13:56]** That's when our Temporary Execution is over, too, which we used to do.

**[00:13:59]** We don't know exactly when we're going to have to intervene again.

**[00:14:02]** maybe just a notification that's pleasant, which says the loop is ready or just

**[00:14:07]** Just as you just described it, which says, um, here's a bunch of them.

**[00:14:10]** Everybody's on fire.

**[00:14:11]** Everyone's on fire.

**[00:14:12]** One short, one short, one short.

**[00:14:13]** Could you come over for a second, please?

**[00:14:14]** So that means, yes, so if you want to do things right now, you have to do things

**[00:14:18]** be almost felt in such a 24-7 readiness, if one now also on critical systems

**[00:14:24]** If I had some kind of book project, yes, something else, then

**[00:14:28]** it's not so bad if you maybe reboot that thing at the weekend

**[00:14:31]** But on all the other issues, I think we're ready to say,

**[00:14:38]** a little bit of things to think about, a little bit from an ITG perspective to look at things,

**[00:14:43]** What we said earlier, try to build up robustly, maybe not directly the loop

**[00:14:49]** just big running things, but is also there, as then again the small part smaller

**[00:14:53]** cut, make watchable, make verifiable, that you look what can

**[00:14:59]** That's where you're going.

**[00:15:00]** And I think that's a little bit of what I'm taking from this AI phase right now,

**[00:15:04]** which we are, now without any such a Gartner half-show, because success

**[00:15:09]** It's all right.

**[00:15:10]** But I think we're a little...

**[00:15:11]** Part of the tears?

**[00:15:12]** Yeah, I don't know about the tears.

**[00:15:13]** So that's not how it feels.

**[00:15:14]** I've been through this a couple of times.

**[00:15:15]** It's both more loved and private.

**[00:15:18]** I think I'm already at prom engineering and look engineering and everyone else.

**[00:15:22]** Things go through again and again and also went up into the half-cycle and something like that.

**[00:15:25]** I think it is more likely that we are already heading in the direction of the platform.

**[00:15:30]** productivity.

**[00:15:31]** There's just things missing.

**[00:15:33]** We talked about it recently.

**[00:15:35]** We're like 97 or something.

**[00:15:36]** You know, the Internet is there, things work, websites are there in general.

**[00:15:40]** Google has not yet become pronounced, great usability, stories are not yet

**[00:15:46]** not yet know where a navigation is best accommodated or so

**[00:15:49]** what.

**[00:15:50]** We still try in many places, that leads to cool creative results

**[00:15:55]** Honestly.

**[00:15:56]** So there's so much hot shit being done outside with AI, too, where stuff

**[00:16:00]** to be raced, animations to be made, info-websites to be built with us

**[00:16:05]** behind earlier could not have imagined so at a speed like the

**[00:16:08]** ==References==--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**[00:16:09]** many creative topics just made. Loop are set up, there will be marketing systems

**[00:16:14]** automatic, program forges are built. All other many places go things

**[00:16:19]** Yes, but it's not like you can copy it 1 to 1. So we haven't got it yet.

**[00:16:24]** this, there's an Amazon and I can build a number one out of it. So this moment

**[00:16:28]** isn't there yet, because you can't copy it over like 1 to 1.

**[00:16:31]** we are in its early phase, the Internet is actually straight.

**[00:16:34]** This is also noticeable on another topic, namely that we had a little bit of it today.

**[00:16:39]** so the binder over models that can break away at once.

**[00:16:43]** Then we spoke from Skills and Loops as a Fortlet and you also determined

**[00:16:47]** the other episodes of such times the topic Agent Harness heard and at the end of the day runs

**[00:16:52]** it always felt like you'd find a lot of comedy Harnesses today,

**[00:16:58]** You have a chat TBT, you have a Gemini, you have the next Siri AI, you have from

**[00:17:05]** Antropi Cross Co-Work, but so this whole theme, how do I play the service use,

**[00:17:10]** how do I play the scientist, how do I play the professional people,

**[00:17:15]** which tries with these tools to create surplus value, without, yes, I install myself today

**[00:17:21]** Open AI, I'll make the next subscription tomorrow, the next subscription, the next subscription or install

**[00:17:26]** here open code of GitHub or no idea, or maybe I even sit down and

**[00:17:32]** build your own Harnis and then it gets really funny when these environments constantly

**[00:17:38]** But on the other hand you build something that this constant change of the

**[00:17:42]** Environment wants to intercept, want to make sure you can work productively, rest in the system

**[00:17:48]** bringst, models exchangeable, yet skills, functional, standardized loops,

**[00:17:54]** without the user having to say it extra.

**[00:17:56]** How do I present it to my user?

**[00:17:58]** I told someone about it the other day, you like great Agent Harness you built there.

**[00:18:03]** But he always tells me I have such a JSON app.

**[00:18:08]** Yeah, I miss that, too. What does the person want?

**[00:18:11]** All right, it just stood there, JSON generated.

**[00:18:13]** So how do I talk to my user?

**[00:18:16]** That you're such a broad fur, where I'm still asking,

**[00:18:20]** How do you operate in a world where, virtually every three days, new models, new techniques, new channels, no idea what will come out and be banned?

**[00:18:27]** Coming out and being banned?

**[00:18:29]** Oh, yeah, if my Harnis was banned, it would be famous.

**[00:18:32]** So right there, yeah, it'd be good for marketing.

**[00:18:36]** But I think Agent Harnis would be another episode, because we haven't announced any more episodes for a long time.

**[00:18:41]** Oh, yeah, who knows, so you can...

**[00:18:43]** Yeah, but definitely a Harni's engineering episode.

**[00:18:45]** A Harni's engineering episode, yes, I'm looking forward to it.

**[00:18:48]** Yeah, but otherwise, like I said, I'm looking at the clock and the train in your neck,

**[00:18:55]** So I just said it that we are moving to the plateau of productivity,

**[00:19:00]** that there is in this Gardner-Hype-Beikel, that's this phase, where everything then just

**[00:19:04]** works well that you are out of this superhype phase, out of the Valley of Tears

**[00:19:08]** It's out and that you're going on now.

**[00:19:10]** I think this path is now so fast with AI that you can already see this productivity platoon.

**[00:19:19]** But the path will be a bit stony.

**[00:19:21]** I think he will still have some bands on his way, some harms will break, some loops will undetectably hope to make in the wrong loops.

**[00:19:32]** And there's, I think, a lot of things going to happen before we maybe have something like what we used to have,

**[00:19:39]** that then such a stable Internet that all people can use,

**[00:19:43]** that the meanness is then also available.

**[00:19:47]** This is going to take a bit longer, I think, in fact, we're going to have it all over the place.

**[00:19:52]** But I don't want to end up positive, as always.

**[00:19:55]** I'm looking forward to it, because even there will be quite new things that don't even know it.

**[00:20:01]** So if you're thinking about the iPhone moment, which software was created after that, which

**[00:20:07]** Interaction possibilities arose afterwards, something like WhatsApp and Co. this appointment

**[00:20:11]** And things like that.

**[00:20:12]** All of this only came about when this technology was there.

**[00:20:14]** And now, I think, we are still in such a situation where a lot of new

**[00:20:18]** Technology, quite a lot of new use cases for us will actually come to

**[00:20:23]** that we don't even think today, that just then, you know, software,

**[00:20:27]** which I generate on-the-fly, because at least I no longer have any graphics program from the

**[00:20:31]** I have to buy poles, but get with the graphics that I need at the moment, just

**[00:20:35]** Now you see more and more people say, oh, I've got the PDF-Smallmacher.

**[00:20:41]** somehow built or anything else done with the PDFs and built a splucking

**[00:20:46]** I think there's gonna be a lot of cool stuff going on.

**[00:20:49]** But I'm sure it'll all be great, and I've been talking a little while you've been talking about it.

**[00:20:54]** Business idea. Oh, now I'm curious. Should we stop or we want to go to the

**[00:20:57]** No, no, of course I want to share it with my listeners, that's a little bit, I don't know.

**[00:21:02]** Imagine that the topic would start driving now, that models are always available in America or in China,

**[00:21:09]** Because, I mean, there's something like export control, isn't there?

**[00:21:12]** Perhaps in Europe too, yes, we all keep our fingers crossed.

**[00:21:15]** Now, just imagine where that would come from.

**[00:21:17]** I've got memories of old times, so I've only ever heard of listeners, no?

**[00:21:21]** Pirate Bay and like the Alice Napster. I kind of have the weird feeling that someday

**[00:21:26]** we see people who then somehow live in the said countries, are country citizens

**[00:21:30]** and put any Rex systems in closet and rut virtually their personal,

**[00:21:36]** So not as a personal, but as a result of their state-male access, whether or not

**[00:21:41]** which is then legal, probably not because you use it to export controls and walk away,

**[00:21:44]** I could imagine that something like this is being built, then we have to

**[00:21:47]** Thomas asks with his Ford GPT and stuff.

**[00:21:49]** Maybe there's something there.

**[00:21:51]** Thomas, if you hear anything, we need to talk.

**[00:21:53]** There they smuggled the model almost locally at their festivals.

**[00:21:56]** I wore it on paper.

**[00:21:57]** Like KGB.

**[00:21:58]** Printed model, I'm sure it'll be fun.

**[00:22:01]** From the side, today a colorful potpourri was hurried at the various things of Jens

**[00:22:07]** now to his train, which is due to its classic delay in time,

**[00:22:12]** when he comes so long.

**[00:22:13]** We wish you a good time and look forward to it.

**[00:22:16]** Soon again guests and turn on again, when it is called Think Different.

**[00:22:19]** Think AI. Ciao.

**[00:22:23]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:22:28]** Two technology-loving minds that don't just talk about artificial intelligence,

**[00:22:33]** But they live.

**[00:22:35]** Here there are clear classifications, real practical insights

**[00:22:39]** and a fresh look at what is possible.

**[00:22:41]** Understandable, critical and always forced with one eye.

**[00:22:46]** to think, to smile and above all to share.
