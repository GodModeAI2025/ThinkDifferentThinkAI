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
translation_provider: "claude"
translation_model: "claude-opus-5"
translated_from_file: "transkripte/048 - Speed vs. Safety.md"
translated_at: "2026-08-15T00:00:00+00:00"
---

# Speed vs. Safety

**Published:** Sun, 12 Jul 2026 20:45:00 +0000
**Duration:** 1375
**Web player:** https://think-ai.podigee.io/48-speed-vs-safety
**Cover:** https://images.podigee-cdn.net/0x,ssU3eIDt4PMhj5EhrwWKUk1v5vCaSqSQEYpBnNyOK6lM=/https://main.podigee-cdn.net/uploads/u73317/a0832141-5b78-438a-a0b5-a34268a38a5f.jpg
**Audio:** https://audio.podigee-cdn.net/2532882-m-e89974e8241169c3f9d0e6554501c339.mp3?source=feed

## Description

Mythos, Fable and the return of restricted models
What do you do when your own Loop Engineering episode from last week is overtaken by reality before the ink is dry? That is exactly what happened to Mark and Jens, which is why there is this spontaneous bonus episode. The trigger is Fable, the Anthropic model that was blocked for non-US citizens a few days ago.

The US government's strategy could be to give selected companies and its own administration a head start in closing exactly these gaps, before models from less controllable hands become similarly capable. From there the conversation moves on to distillation: Chinese models replicate the capabilities of large US models by extracting the knowledge out of their token prediction with automated mass requests. This also hits companies hard that had aligned their processes with a single model too early. Mark and Jens report on law firms that had switched their entire text analysis over to Fable and are now facing exactly this problem when the model gets shut down. Along the way, a new challenger called Fuku turns up as well (from a provider whose name Jens first has to remember during the conversation), claiming record benchmarks of its own.

Picking up directly from the previous week's Loop Engineering episode, the topic is the practical limits of loops: Jens reports on a multi-day block at Anthropic after he had burned through his weekly limit on the Max plan in a single evening. A second case is even trickier: if a loop runs into an API limit instead of a model limit in the middle of its work, it does abort, but after a simple "keep going" it reports back as if everything were done, including the casual remark that there had been eight crashes that someone should repair. What is left at the end is a result that looks like a normal prompt, not like the thorough iteration that was actually wanted. The call of this episode: away from pure Prompt Engineering, towards the loop engineer.

Finally, the two of them put into perspective how early this phase of AI development still is, comparable to the internet around 1997: a lot already works, but there are no established standards yet, while the first course sellers promising big money are already there. One point of contention is commodity harnesses like ChatGPT, Gemini or Anthropic's Cowork versus your own, self-built Agent Harness, which has to cope with constantly changing models and environments. Mark tells of someone who dismissed the result of his self-built harness as "some kind of JSON app", an occasion for a separate, more detailed Harness Engineering episode that the two announce. Despite all the setbacks, Mark and Jens remain optimistic: they compare the current phase to the iPhone moment, after which applications like WhatsApp emerged that nobody had seen coming, and they expect something similar for spontaneously generated software instead of ready-bought programs.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who don't just talk about artificial intelligence, but live it.

**[00:00:14]** Here you get clear classifications, real practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** An invitation to think, to smile, and above all to join the conversation.

**[00:00:33]** A warm welcome to Think Different, Think AI.

**[00:00:37]** Jens and I have met up in person again.

**[00:00:40]** Unfortunately not in such a nice hotel lobby as last time.

**[00:00:43]** But nevertheless with a cold drink in hand after these hot days.

**[00:00:47]** And we realized for ourselves,

**[00:00:49]** that the last episode we recorded,

**[00:00:52]** the one you got to hear last week,

**[00:00:54]** is so current that we had to build on it once more. Jens, last time we talked about things

**[00:01:02]** like prompting, skills, loops, and in the episode before that we had at some point

**[00:01:08]** also talked about Fable 5, and now we said to ourselves, this all hangs together

**[00:01:12]** somehow. So what hasn't happened since then, or what has happened? Yes, of course we have this,

**[00:01:21]** We recorded the loop episode and I think it fits quite well that we now

**[00:01:24]** do this current addition to that loop episode, because the listener among you

**[00:01:29]** and the AI enthusiast, the way we are, will certainly have noticed it.

**[00:01:34]** Fable had, or rather Anthropic became really well known with Fable a few days ago, then

**[00:01:40]** it was shut down, we did a whole episode about it, you surely know

**[00:01:43]** that topic.

**[00:01:44]** Now this weekend again, such things apparently always happen

**[00:01:48]** on the weekend.

**[00:01:49]** And it has nothing to do with VW or BSF.

**[00:01:52]** No, but those are existing stories.

**[00:01:54]** Apparently, where things from America spill over here and get decided.

**[00:01:57]** Because there is another model,

**[00:02:00]** that has been unlocked again,

**[00:02:03]** and another model announced that they, their model,

**[00:02:06]** the one they had planned, the way they are, if I've got it right,

**[00:02:08]** the one from OpenAI, that would have been the 5.5, which was actually supposed to come out.

**[00:02:13]** No, 5.6, there is a 5.6.

**[00:02:15]** It's totally funny, right, because one of them gets a phone call,

**[00:02:18]** saying he should please hold his model back a bit and not

**[00:02:21]** release it just yet, along the lines of, you don't want something to happen to you, do you.

**[00:02:25]** And the other one released Fable 5.

**[00:02:28]** Unlike what we have known so far, the whole situation

**[00:02:32]** around AI, where things were actually just cheerfully posted out into the world,

**[00:02:36]** it seems we are now entering a new phase.

**[00:02:40]** Which of course speaks for the quality of the models.

**[00:02:42]** These models are being continuously developed further.

**[00:02:46]** That means they keep getting better, and accordingly of course also more dangerous, in that

**[00:02:53]** they surpass us in many capabilities, and above all now in capabilities

**[00:02:58]** that we used to show off, we thought we had programmed something well, we had

**[00:03:00]** programmed something securely back then.

**[00:03:02]** Now these things come around the corner and discover fairly quickly that this is not the case, yes,

**[00:03:06]** that we godlike programmers we used to be were not so error-free after all

**[00:03:10]** Error-free. Exactly, error-free, were not so error-free after all, and accordingly there are relatively many security holes somewhere that get cracked in no time at all by these new models.

**[00:03:22]** I think somehow the government also said, the American government, that their systems too were cracked by Mythos within a few hours.

**[00:03:29]** So that really is a scope that definitely calls for regulation.

**[00:03:34]** But on the other hand it also shows a bit how dependent we have become there by now.

**[00:03:40]** I mean, loyal listeners of our podcast will certainly have noticed as well.

**[00:03:45]** There are not only the American models, there are also Chinese models, for example.

**[00:03:51]** Yes, let's leave the French model with Ralf out of the explanation here for now

**[00:03:58]** and not have that be an insinuation or anything like that.

**[00:04:02]** But the Chinese models will probably also notice what's going on here, because one

**[00:04:07]** or the other model, at least that's what one has read or heard, came about through distillation

**[00:04:13]** of the big models.

**[00:04:15]** So you basically have to imagine it like this, that providers, let's say, ran a lot of requests

**[00:04:21]** and conversations with the US American models, automated, in order to

**[00:04:26]** basically rebuild and replicate these models.

**[00:04:29]** A kind of reverse engineering.

**[00:04:31]** They actually prompted, watched, so you say, I send 100,000 requests

**[00:04:35]** on the topic of how best to go fishing, then these models answer in 100,000

**[00:04:43]** variants, which are however very similar.

**[00:04:45]** So that in principle the right instructions come out, that I take a fishing rod with me or something

**[00:04:47]** else and the bait and whatever.

**[00:04:51]** And set off some dynamite, you've seen so many movies.

**[00:04:53]** And out of this, well this, with a certain probability, because we

**[00:04:56]** we all know the topic, that probability calculation happens in the background there, the token prediction.

**[00:05:01]** And to get that back out again, very, very many requests were sent to these American models.

**[00:05:06]** And that way you basically understood how this model works and then built it accordingly.

**[00:05:11]** There were stories that some of the Chinese models are set up like that.

**[00:05:15]** And what I also found quite funny is the other thing, that apparently there are even companies going to court,

**[00:05:23]** because immediately after Fable appeared they had recognized the potential and had already optimized their business processes

**[00:05:32]** for it and said, this is basically a model that is so good in

**[00:05:37]** text analysis, I think it was a law firm, was so good at text analysis that they

**[00:05:43]** didn't want to do without it anymore, switched everything over to it, and then it's

**[00:05:46]** of course doubly annoying when all of a sudden it's like, right, we're discontinuing

**[00:05:51]** the model, although to be fair one has to say the model was not officially discontinued

**[00:05:56]** by the US government. They only said, you have to make sure that only US American

**[00:06:00]** citizens use it. That is of course a bit difficult in times of Amazon Bedrock access,

**[00:06:05]** APKs and what have you. So they shut it down in general. But then there

**[00:06:09]** you stand, as a company. And that also closes the circle a bit back to this

**[00:06:13]** loop episode. If you always try to be right at the bleeding edge, then

**[00:06:18]** you can not only fall flat on your face because, well, you're going into new territory and cause

**[00:06:23]** either costs or you have to learn to deal with it.

**[00:06:26]** Never!

**[00:06:27]** It can even be that your business process comes to a standstill afterwards because the model got switched off.

**[00:06:32]** Another good point here, because I wasn't really aware of that at all, it only became

**[00:06:35]** clear to me, only dawned on me, as you were talking.

**[00:06:37]** Other model providers too, whether through distillation or through their own model development, will

**[00:06:41]** most likely reach the status that we currently have with the big

**[00:06:45]** models.

**[00:06:46]** nice, with how much deliberation you go into this and say the American

**[00:06:52]** government has, as always, thought it through very thoroughly. What I

**[00:06:57]** found quite funny about it: when Mythos appeared and it was still said that it is only

**[00:07:02]** available to a very limited group of users, we also reported on that

**[00:07:06]** in the podcast, it was also listed as a model at Amazon Bedrock in the EU zone, in

**[00:07:13]** Frankfurt, where I then also thought, hey, if it really is this ominous super-duper and

**[00:07:18]** I-break-out-of-everything model, whether the euro zone Frankfurt at Bedrock is really the

**[00:07:23]** best place. I don't know about that. We'll have to check in a moment whether it's still there. Yes,

**[00:07:29]** sorry. But do you still remember what this model is called that has now come out,

**[00:07:33]** the one that sort of claims it has Fable 5 capabilities, because it isn't a model,

**[00:07:40]** it's more of an orchestrator. Yes, yes, it's Japanese, but the name escapes me right now,

**[00:07:44]** I think something with Fuku, I'm afraid I'll have to look it up. Yes, yes, so honestly I

**[00:07:50]** have no idea what it's called either, maybe it'll come to us in a moment,

**[00:07:54]** we'll certainly keep talking. I also found that quite funny, how models suddenly

**[00:07:58]** sprout out of the ground, or rather methods sprout out of the ground, that claim of themselves

**[00:08:04]** to beat the benchmarks that these big models had presented for a few days, and from

**[00:08:14]** that side, it's coming to me, what's it called? Sakana, AI, Fuku. Yes, that's exactly why I know

**[00:08:21]** that I always really enjoy doing the podcast with you, because you're the educated one. Yes,

**[00:08:27]** but I'd like to come back once more to the topic I just briefly touched on with

**[00:08:31]** looping, because we did talk about loops a bit.

**[00:08:35]** Looping, yes, we do loops, then we have looping.

**[00:08:38]** Looping.

**[00:08:39]** Just remember that.

**[00:08:40]** Exactly.

**[00:08:41]** Yes, that of course has, as has just become clear, consequences that you now have to

**[00:08:45]** worry about, if we, the way we introduced the loops, are in a

**[00:08:49]** world where I can no longer be sure that a big model that is released

**[00:08:56]** out there is still on the market when I wake up in the morning.

**[00:09:00]** So this nice storyline, I'll set up a loop here and maybe hundreds of them,

**[00:09:05]** well, that's also what we always hear when we look at it, hardly any of the big models

**[00:09:10]** is even programmed by programmers anymore, that is only looped as well, so many

**[00:09:14]** of the big AI programmers and big names who sit in the model companies say, we

**[00:09:20]** don't do it ourselves at all anymore, I'm basically only there to build loops.

**[00:09:25]** So, but if the essential part of a loop then disappears, meaning the AI model in the background,

**[00:09:32]** well then your loops are simply worthless too, honestly,

**[00:09:35]** they don't get any further from there.

**[00:09:36]** So accordingly we have to, everyone has to think about that, I believe.

**[00:09:40]** And we have often talked about that, the topic of harness engineering,

**[00:09:44]** how do I basically build up my whole AI setup, what does my AI architecture actually look like?

**[00:09:49]** You have to think about that for maybe two or three milliseconds longer and not

**[00:09:54]** just prompt what you could do there, so that you basically build a system that

**[00:09:58]** is then also robust and can prevent or avoid such outages in an emergency

**[00:10:04]** or at least catch them in such a way that it doesn't lead to critical situations

**[00:10:08]** somewhere.

**[00:10:09]** That reminds me of another thing that can go badly wrong

**[00:10:14]** with loops.

**[00:10:15]** If you follow me, you'll have seen that I got forcibly blocked again recently, because all the tokens that Anthropic grants me in the big Max plan were used up.

**[00:10:27]** Well, no, but I was somehow banned for several days because I had used up my weekly limit.

**[00:10:34]** You really should watch out with these /workflow slash code things.

**[00:10:39]** That's the one thing, okay, fair point, when the models hit token limits, as long as you

**[00:10:47]** don't have pay per use, that's the one thing. The other thing that struck me, what came up in

**[00:10:52]** my attempts to work with loops.

**[00:10:57]** You give the system large amounts of data and say, run your loops over it.

**[00:11:02]** If you don't make sure from the outset that, for example, blocks of text are sufficiently

**[00:11:11]** large or small, whereby sufficiently large or small is deliberately chosen to be vague,

**[00:11:15]** because I don't know what large or small is, but you'll notice in a moment what

**[00:11:18]** I'm getting at.

**[00:11:19]** Because I told the thing, listen up, here are big books, chew your way

**[00:11:23]** through them and evaluate the following things for me, please do that with a goal loop,

**[00:11:28]** so keep going until the following questions are answered, and all of a sudden everything

**[00:11:32]** had aborted. Everything shot off into nirvana. It said on the screen in yellow letters.

**[00:11:37]** API limit reached, open parenthesis. This is not about the model limit, you have

**[00:11:44]** quite simply bombarded the API. We're not continuing. Right, so then you say to it,

**[00:11:49]** keep going. And then it says, oh yes, totally great. Listen, I'll continue, blah blah blah. It then

**[00:11:55]** worked again, errors again. At some point it noticed, oh listen, maybe I should reduce my

**[00:11:58]** queries so this doesn't run into the limit, and at the very, very, very end it says,

**[00:12:04]** you're done with everything. By the way, we had eight crashes. Should I repair

**[00:12:08]** what broke in the process, and you think to yourself, okay, the goal loop is broken,

**[00:12:14]** then you constantly have to say continue, and the result was as if I had written a normal

**[00:12:19]** prompt, everything I put in about verify yourself and make sure and these are

**[00:12:25]** the KPIs. It pushed all of that out over the airwaves during these abort moments.

**[00:12:30]** Yes. So I also thought, I don't even need an American government

**[00:12:34]** that shuts a model down. My own incompetence is enough as well, and with that I'm calling

**[00:12:38]** no longer for prompt engineering, but for the loop engineer. Yes, but the loop engineer,

**[00:12:45]** that is, I think, a special point, I think with this whole AI hype topic and

**[00:12:50]** the two of us are always right at the front too when it comes to throwing terms

**[00:12:53]** around, we'll keep coming around the corner with new topics. I think the

**[00:12:58]** experience of the last two or three years with these topics simply shows, we are all

**[00:13:04]** still early. All the things are emerging relatively new right now. That means there isn't yet

**[00:13:12]** the optimal loop engineering school that tells you, if you do it like this, then it

**[00:13:18]** will keep running.

**[00:13:19]** There's definitely an influencer who will sell you that as a course.

**[00:13:21]** Exactly, absolutely. And you can immediately make millions with that if you do it.

**[00:13:26]** Anyone who has ever tried to build a workflow with, let's say just two AI models in a row.

**[00:13:33]** will notice that they have to rework things again and again.

**[00:13:36]** There are always these places where we currently rework, where we, the famous human, always have to be in the loop,

**[00:13:42]** who can't just be on the loop yet and somehow sit on his hacienda

**[00:13:47]** and enjoy the sunshine and count the coyotes.

**[00:13:50]** No, we still always have to, after an indefinite time, we don't know exactly how

**[00:13:56]** long that is, that was also our Temporal UX episode that we did once.

**[00:13:59]** We also don't know one hundred percent exactly when we actually have to step in again,

**[00:14:02]** maybe a notification that is pleasant, that says the loop is finished, or else

**[00:14:07]** the way you just described it, that says, hm, there's a problem here.

**[00:14:10]** Everything's on fire here.

**[00:14:11]** Everything's on fire.

**[00:14:12]** Just briefly, briefly, briefly.

**[00:14:13]** Could you come over for a second, yes?

**[00:14:14]** So that means, yes, so if you want to do things right now, then you also have to

**[00:14:18]** be in something like 24/7 standby, if you were to let that loose on critical systems

**[00:14:24]** as well. If I have some kind of book project there, yes, something different, then

**[00:14:28]** it's not so bad if you restart the thing again on the weekend

**[00:14:31]** or something. But with all other topics we are, I think, at the point where you have to say,

**[00:14:38]** think about things a bit, look at things a bit from an IT perspective,

**[00:14:43]** what we said earlier, try to build robustly, maybe don't just let the loop

**[00:14:49]** run wild on things, but there too, cut the small part into smaller

**[00:14:53]** pieces, make it monitorable, have it made verifiable, so that you look at what can

**[00:14:59]** go wrong there.

**[00:15:00]** And I think that's a bit of what I'm taking away at the moment from this AI phase

**[00:15:04]** we're in, now without digging out some kind of Gartner hype cycle

**[00:15:09]** thing.

**[00:15:10]** But I think we're now a little bit...

**[00:15:11]** In the valley of tears?

**[00:15:12]** Yes, valley of tears, I don't even know.

**[00:15:13]** It doesn't feel like that.

**[00:15:14]** I've been through that a few times already.

**[00:15:15]** Both professionally and privately.

**[00:15:18]** I think I've been through that with prompt engineering and with loop engineering and with all the other

**[00:15:22]** things over and over again, and gone back up into the hype cycle and things like that.

**[00:15:25]** I think it's actually more that we are already on this path in the direction of the plateau

**[00:15:30]** of productivity.

**[00:15:31]** But things are simply missing.

**[00:15:33]** We talked about it recently.

**[00:15:35]** We're like in '97 or something.

**[00:15:36]** You know, the internet is there, things work, websites are generally there.

**[00:15:40]** But Google hasn't taken shape yet, big usability stories aren't

**[00:15:46]** worked out yet and we don't know yet where a navigation is best placed or something

**[00:15:49]** like that.

**[00:15:50]** We're still trying things out in many places, and that leads to cool creative results

**[00:15:55]** honestly.

**[00:15:56]** I mean, there's so much hot stuff being made out there with AI too, where things

**[00:16:00]** get rendered, animations get made, info websites get built, which back in

**[00:16:05]** our day we couldn't have imagined, at a speed like it's

**[00:16:08]** being done.

**[00:16:09]** lots of creative topics are being done right now. Loops are set up, marketing systems are

**[00:16:14]** automated, program forges are built. In many other places things already

**[00:16:19]** work, but it's not the case that you can copy it one to one. So we don't yet have

**[00:16:24]** this, there's an Amazon and I can build a Zalando out of it. So that moment

**[00:16:28]** isn't here yet, because you can't copy it over one to one like that yet. I think

**[00:16:31]** we're in an early phase, the way the internet actually is right now.

**[00:16:34]** You also notice that with another topic, namely today we had a bit of

**[00:16:39]** a closing note about models that can suddenly break away.

**[00:16:43]** Then we talked about skills and loops as a continuation, and you've certainly also heard

**[00:16:47]** the topic of Agent Harness in the other episodes, and at the end of the day it always

**[00:16:52]** seems to come down to the fact that today you find a lot of commodity harnesses,

**[00:16:58]** You have a ChatGPT, you have a Gemini, you have the next Siri AI, you have

**[00:17:05]** Cowork from Anthropic, but this whole topic of how do I serve the service worker,

**[00:17:10]** how do I serve the scientist, how do I serve the professional person

**[00:17:15]** who tries to create added value with these tools, without, well, do I install

**[00:17:21]** OpenAI today, do I take out the next subscription tomorrow, the next subscription, the next subscription, or do I install

**[00:17:26]** Open Code from GitHub here, or who knows, or do I maybe even sit down and

**[00:17:32]** build my own harness, and then it gets really funny when these environments keep

**[00:17:38]** changing. But on the other hand you build something that wants to absorb this constant change of

**[00:17:42]** the environment, wants to make sure that you can work productively, brings calm into the system,

**[00:17:48]** models interchangeable, skills still functional, standardized loops,

**[00:17:54]** without the user having to say so separately.

**[00:17:56]** How do I present it to my user?

**[00:17:58]** Someone recently said to me, hey, great Agent Harness you built there.

**[00:18:03]** But he always tells me that I have some kind of JSON app.

**[00:18:08]** Yes, that leaves me wondering too, what does that person want?

**[00:18:11]** Well okay, it just said there, JSON generated.

**[00:18:13]** Whereas, so, how do I talk to my user?

**[00:18:16]** That you also need a thick skin there, where I then also have the question,

**[00:18:20]** How do you run operations in a world where basically every three days new models, new techniques, new channels, who knows what, come out and get banned?

**[00:18:27]** Come out and get banned?

**[00:18:29]** Oh yes, if my harness ever gets banned, then it would be famous.

**[00:18:32]** So at that point, yes, for marketing that would be good.

**[00:18:36]** But I think Agent Harness would be another episode, we haven't announced episodes in a long time.

**[00:18:41]** Oh well, who knows, so feel free to...

**[00:18:43]** Yes, but in any case a harness engineering episode.

**[00:18:45]** A harness engineering episode, yes, I'm looking forward to it.

**[00:18:48]** Yes, but otherwise, as I said, with a look at the clock and the train breathing down your neck, the,

**[00:18:55]** so I just said that we're moving towards the plateau of productivity,

**[00:19:00]** that in this Gartner hype cycle, that's then the phase where everything

**[00:19:04]** works well, that you're out of this super hype phase, out of the valley of tears

**[00:19:08]** and that you now move on.

**[00:19:10]** I think this path is currently so fast with AI that you can already see this productivity plateau.

**[00:19:19]** But the path will still get a bit rocky.

**[00:19:21]** I think it will still have a few bumps along the way, some harnesses will break, some loops will, hopefully undetected, do the wrong loopings.

**[00:19:32]** And there, I think, a lot will still happen before we perhaps have something like we used to have,

**[00:19:39]** that we then have a stable internet that all people can use,

**[00:19:43]** that is then also available to the general public.

**[00:19:47]** That will take a while longer, I think, actually, until we have that consistently everywhere.

**[00:19:52]** But nevertheless I want to, as always, end on a positive note.

**[00:19:55]** I'm looking forward to it, because there too completely new things will emerge that we don't even know yet.

**[00:20:01]** So if you think now of the iPhone moment, which software emerged afterwards, which

**[00:20:07]** interaction possibilities emerged afterwards, things like WhatsApp and co., this arranging to meet

**[00:20:11]** and things like that.

**[00:20:12]** All of that only came about once this technology was there.

**[00:20:14]** And I think we're now still in a situation where a lot of new

**[00:20:18]** technology, a lot of new use cases are actually only going to come for us, ones

**[00:20:23]** that we're not even thinking about today, that simply, you know, software

**[00:20:27]** that I generate on the fly, because I don't have to buy a graphics program off the

**[00:20:31]** shelf anymore, but instead simply get the graphic that I need in that moment,

**[00:20:35]** generate it. You see more and more today that people say, oh, I built myself the PDF shrinker

**[00:20:41]** somehow, or did something else with PDFs, and built a Splunking

**[00:20:46]** and you read about things like that here and there. I think a lot, a lot of cool things will still happen.

**[00:20:49]** But it'll all definitely be awesome, and while you were talking I had a

**[00:20:54]** business idea. Oh, now I'm curious. Should we stop or do we want to go to the

**[00:20:57]** No, no, of course I want to share it with my listeners, that's also a bit, I don't know.

**[00:21:02]** Just imagine the topic really did pick up speed, that models are always only available in America first, or in China,

**[00:21:09]** because, I mean, there is such a thing as export control, right?

**[00:21:12]** Maybe in Europe too, yes, we're keeping our fingers crossed for everyone.

**[00:21:15]** So, now just imagine that this were to come.

**[00:21:17]** I have memories of very old times, well, only ever from what listeners say, right?

**[00:21:21]** Pirate Bay and the likes of Napster. I somehow have this strange feeling that at some point

**[00:21:26]** we'll see people who then live somehow in the countries in question, are citizens of those countries

**[00:21:30]** and put some kind of rack systems in the cupboard and basically route their personal,

**[00:21:36]** well, not exactly personal, but route them through their state-citizen access, whether

**[00:21:41]** that's then legal, probably not, because with that you'd be up against export controls,

**[00:21:44]** I could imagine that something like that will get built at some point, then we'll have to

**[00:21:47]** ask Thomas with his Ford GPT and so on.

**[00:21:49]** Maybe there's already something out there.

**[00:21:51]** Thomas, if you're hearing this, we need to talk.

**[00:21:53]** Then you basically smuggle the model locally onto your hard drive.

**[00:21:56]** I carried it on paper.

**[00:21:57]** Just like the KGB.

**[00:21:58]** A printed-out model, that'll definitely be funny.

**[00:22:01]** On that note, today was a colorful potpourri of the most varied things, Jens is now rushing

**[00:22:07]** off to his train, which thanks to its classic delay is on time,

**[00:22:12]** if he takes that long to get there.

**[00:22:13]** We wish you a good time and look forward to it.

**[00:22:16]** Guests again soon, and tune in again when it's called Think Different.

**[00:22:19]** Think AI. Ciao.

**[00:22:23]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:22:28]** Two technology-loving minds who don't just talk about artificial intelligence,

**[00:22:33]** but live it.

**[00:22:35]** Here you get clear classifications, real practical insights

**[00:22:39]** and a fresh perspective on what is possible.

**[00:22:41]** Understandable, critical, and always with a wink.

**[00:22:46]** to think, to smile, and above all to join the conversation.
