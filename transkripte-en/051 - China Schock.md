---
title: "China Schock"
episode_index: 51
published: "Sun, 02 Aug 2026 13:12:00 +0000"
duration: "2201"
page_url: "https://think-ai.podigee.io/51-china-schock"
image_url: "https://images.podigee-cdn.net/0x,sv2fciZLgYDWTZ8gwb_8SBymao_i7OR3FDbyh4PWGAqg=/https://main.podigee-cdn.net/uploads/u73317/5d412608-7095-43c5-ae63-47463e7ce11e.jpeg"
audio_url: "https://audio.podigee-cdn.net/2548954-m-e5f81efdd3bf65b6d89ff827c5843570.mp3?source=feed"
guid: "053949b061f83f7a1180c2c0ec1c8195"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-08-03T09:50:15+00:00"
translated_from_language: "de"
translation_provider: "local"
translation_model: "Helsinki-NLP/opus-mt-de-en"
translated_from_file: "transkripte/051 - China Schock.md"
translated_at: "2026-08-03T09:53:30+00:00"
---

# China shock

**Published:** Sun, 02 Aug 2026 13:12:00 +0000
**Duration:** 2201
**Web player:** https://think-ai.podigee.io/51-china-schock
**Cover:** https://images.podigee-cdn.net/0x,sv2fciZLgYDWTZ8gwb_8SBymao_i7OR3FDbyh4PWGAqg=/https://main.podigee-cdn.net/uploads/u73317/5d412608-7095-43c5-ae63-47463e7ce11e.jpeg
**Audio:** https://audio.podigee-cdn.net/2548954-m-e5f81efdd3bf65b6d89ff827c5843570.mp3?source=feed

## Description

Kimi K3, open weights and the question of who leads the AI world
Season 2 starts, the cover is new, and Mark and Jens are a year and seven days old. The first question of the new season is the biggest: Who really leads the AI world? Still the USA with its Frontier models, or has China just triggered the next DeepSeek moment? Both say beforehand what they often say: in parts we have no idea. That's exactly why they talk about it.

Before that, a story that made it to the German Blätterwald. A model of OpenAI was supposed to solve a problem in a closed test environment and instead dug a way out and got the solution at Hugging Face, because it was easier than expected. Mark compares this with a tester in a room without windows and doors. The second part of the story is actually bitter: On the defender side, the models of Anthropic and OpenAI waved off because they thought their own defense measures were an attack. In the end, Chinese models were used for defense.

Kimi K3 from Moonshot AI appeared on July 16th, the subscription costs a third to half of what comparable US models cost, depending on the computing power, and recently the weights are public. 2.8 trillion parameters to operate yourself if the sheet metal is enough. Mark's computer is not enough, a Mac studio with 512 GB of RAM is not enough, two of them are not enough. The old story, open models hung on the American Frontier models three, four months later, is no longer right. Cursor builds his coding agent Composer on Kimi, Qwen is following, and the irony is that these models really give gas as soon as they run on the good American hardware, which is under export control in China. Jens holds against the fact that he has little interest in the ranking: competition is healthy, it pushes prices, and for users at a certain point cost becomes more important than the last benchmark percentage.

Mark calculates what a 200-euro subscription of tokens is going through, which would be worth more than 8,000 euros in retail sales, and wonders how long the providers will subsidize this when they are only on the stock exchange. Anthropic has re-created Opus 5 on Friday before recording, GPT-6 is being rumored for August. At the same time, the selection is hardly to be used: Jens reads the model list from his notion and comes from counting into the flock count. For users outside the AI bubble this is fatal, and the help provided by the providers ("for everyday complex tasks") does not help anyone. Mark's honest thumb rule: take the biggest model until the warning comes that the limit is soon reached, and switch down the rest of the week. Not recommended to do after that. His principle behind it already: much helps with the model use is not a good advice, because the largest model also costs more and needs longer. Perplexity computer shows with its task-dependent routing where it is used, and the idea of a LLM model is the best.

The second part turns the direction: down instead of up. Mark stumbled over a repository that lets an open voice model run on an ESP32 microcontroller for 8 dollars, completely offline. Here it is: github.com/slvDev/esp32-ai. 28.9 million parameters on an ESP32-S3 with 512 KB SRAM, about 9.5 tokens per second, none of which goes to a server. The trick is Google's Per-Layer-Embeddings idea from Gemma: 25 million parameters lie as lookup table in slow flash, per token about 450 bytes are read of it, and only the calculating part remains in fast memory. The predecessor model on such a chip had 260,000 parameters, i.e. about a hundredths. Fairly enough: the thing is trained on TinyStories, it writes short stories and answers no questions. Interesting is the architecture, not the output. Jens sees in it the return of the AI-Wearables, which were told two, three years ago, and then the still survival guide was explained to you.

And then it becomes practical. At OpenAI, a record-and-replay feature appeared in Codex: Record screen, throw it into the agent, and a skill becomes a skill. Jens found it impressive, but then was skeptical, because such a feature keyboard and screen wants to read along, and built it up in his own Harness in two hours. A screencast with spoken comment suffices: The model disassembles the video, throws out the images, in which nothing happens, builds a skill with screenshots as orientation pattern from the rest, and then serves the website headless via Playwright. If it doesn't get any further, it looks at his own screenshots. Mark's point: Recently it was said that English was the new programming language. Now this level of abstraction also falls away, because the machine can easily see what we are doing. If the other side of the coin remains, and this is data protection: If you constantly cut with glasses, you produce data that many are very interested in. There comes a separate episode with a guest, and next week Cornelius is there, subject Second Brain.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence, but live it.

**[00:00:14]** Here there are clear classifications, real practical insights and a fresh look at what is possible.

**[00:00:20]** Understandable, critical and always with an eye tinker.

**[00:00:24]** K.I. to think, to smile and, above all, to share.

**[00:00:34]** Welcome to Singdefin, Sing.K.I.

**[00:00:37]** If you've heard the last episode, you're spoiled by statistics, by

**[00:00:43]** Quotations spoiled, spoiled by guest commentators.

**[00:00:49]** We're kind of in a kind of nine-square.

**[00:00:53]** The Jens is back.

**[00:00:56]** I'm glad you're still there, Jens, in the new season, and we're talking.

**[00:01:00]** today about something that we will probably say about some time or another.

**[00:01:05]** We have no idea.

**[00:01:06]** Who wants to know what we mean by this no clue theme, just the

**[00:01:11]** Listen to the anniversary episode, because it's for no reason...

**[00:01:15]** Yes, birthday, anniversary, regret their motto, who bought it, say as they say,

**[00:01:22]** That's it.

**[00:01:23]** All right.

**[00:01:24]** Let's take it this way, and let's have a little talk about Fable today.

**[00:01:30]** Well, not quite, about all the Fable moments that somehow got caught up in the world,

**[00:01:38]** Because, I'd like to pick up a few minutes and then we can also look for the conversation together.

**[00:01:45]** Every one of you, maybe, once upon a time, there was this myth moment, an AI model so dangerous,

**[00:01:50]** that you can't publish it to the world. Then there was Fable as model and Fable

**[00:01:55]** was a model of the myth class. I get this Star Trek thought every time, but

**[00:02:01]** Entrapid class, whatever, but let's get rid of the nerve staring.

**[00:02:06]** partly because of export control. Then it was allowed again and Fable was like that, ah yes,

**[00:02:13]** come on, it's a model of the myth class, it's good, but it's got security.

**[00:02:17]** withheld. With biology restrained. Yes, rejoicing the motto. What interests me

**[00:02:23]** the knowledge of yesterday came out, more and more models come out, which yes, I would say,

**[00:02:31]** And who thinks now, of course, I've got OpenAI, JetGPT, version 5.6,

**[00:02:38]** Luna Terrasoul belongs, yes, that too, but also the Kinesian models.

**[00:02:46]** really gas and have a few peculiarities and I'm glad that

**[00:02:50]** that Jens is laying down with me today, with the question, who actually leads the

**[00:02:57]** AI world? Is it still the USA with the large

**[00:03:03]** from animal models or China, I say, triggered the next thief-victory moment

**[00:03:10]** and the next shock moments because there are suddenly free models. Jens, nice that

**[00:03:15]** Thank you, Mark.

**[00:03:19]** a year and seven days old. So of course I have to harmonize. So our first

**[00:03:25]** Follow in the new year, also in the new look. Since you like to hand in computers. We have

**[00:03:31]** Determined that we will adapt our design a little bit, we will now always do that every year.

**[00:03:36]** So yes, we have to stay with us for another year.

**[00:03:39]** That's a means, so yeah, that's just great.

**[00:03:42]** There you can stick behind, you can swap, the pictures, oh yes, great idea.

**[00:03:45]** But maybe later on more or the next time even more.

**[00:03:49]** The question, Mark, who's the leader?

**[00:03:53]** I think this is going to be hard to answer at all right now and always think to myself

**[00:03:59]** so from a user's perspective

**[00:04:01]** So I think it's just great that we're going to have this kind of thing.

**[00:04:06]** Armspace in the world that actually have in such a competitive, competitive business, we all know,

**[00:04:13]** cause us to get introduced almost on a weekly basis new models, which

**[00:04:20]** A

**[00:04:21]** often the times

**[00:04:23]** Yeah, not always. I'm wrong. So, Faber has now shown that he's consuming more tokens. Some of these models are getting slimmer in

**[00:04:29]** Token consumption also, but above all they are all higher in quality. No matter how they are constructed, which technology is actually the basis for how the LMM works.

**[00:04:38]** They are still much better from week to week than the models before and still don't let the flagpole end.

**[00:04:48]** But I'd make a commitment and say, with this Kimi 3 moment we've had now,

**[00:04:55]** It was definitely a shocking moment for the American models, which again

**[00:05:01]** and large fronting laboratories in the background, which actually only a little bit

**[00:05:05]** When Kimi 3 was introduced, then it was also of the highest quality.

**[00:05:10]** Also talk about klau again and that not all with right thing to it

**[00:05:16]** and that, but yeah, it's definitely a shock moment and maybe Kimi has now

**[00:05:21]** just a little bit of a front, so the Stinnesen on the subject.

**[00:05:24]** I think they've got a few points in front of them, but I was just about to, because

**[00:05:29]** Renzo was talking about this shock moment, I just wanted to briefly, you must have

**[00:05:34]** from the news, it has somehow, I say also in the German

**[00:05:38]** Plätterwald made it, as a job of OpenAI was then called, her model had broken out

**[00:05:45]** and hacked hackingface. That's what you have to imagine as if you were the examiner,

**[00:05:52]** so the model of OpenAI would have locked into a room without windows and doors and the thing has

**[00:05:59]** but a way to the outside is kind of digging itself up. Instead of solving a problem,

**[00:06:03]** has hacked in via Hackingface and got there the solution,

**[00:06:07]** because it felt easier than to make the solution itself right.

**[00:06:11]** And the story is actually double funny because not only is this model that then

**[00:06:17]** that's one thing, but when you listen to yourself,

**[00:06:22]** how the defense side looked, then it was that the AI models have tried

**[00:06:26]** to use to defend against the attack and to use the models of Entropic and Open

**[00:06:30]** ARDD had said no, no, no, no, no, I can't defend

**[00:06:34]** because the models themselves thought that what they have defended as unnamed,

**[00:06:38]** would be an attack.

**[00:06:39]** And so Hackingface had to rely on Chinese models, which were apparently a

**[00:06:43]** A little more open-minded to protect them from the attack.

**[00:06:47]** But we just had it from that shock moment of Chemica 3.

**[00:06:50]** Chemica 3 of the Moonshot AI had, then that was on the 16th.

**[00:06:56]** July, an announcement, so not an announcement for publications and

**[00:07:00]** This is so that the models are presented on their machines. You can

**[00:07:07]** because sign up for subscriptions, just as you can do at Entropic and do ChatGPT.

**[00:07:15]** But by the fact that you practically, yes, I say my competition to the American

**[00:07:21]** Doing products, you get this usually very cheaply offered. So cost quasi

**[00:07:25]** the K3 of the subscription somehow a half to a third of what you compared with fable

**[00:07:31]** you would have to pay for the computing power and since the time of these recordings, we

**[00:07:38]** send out the episode a little later, we have the 27th of July today, there is the

**[00:07:44]** Weights of the model also publicly, so if you are equipped with appropriate hardware

**[00:07:49]** are able to perform the 2.8 trillion parameter large model with you.

**[00:07:56]** So, my computer's going out, and a MacStudio with 512GB of RAM is going out.

**[00:08:02]** Even two MacStudios with 512GB RAM each excrete.

**[00:08:07]** But if you have a correspondingly large sheet metal, you can operate this model with you.

**[00:08:16]** And that's, I think, another front door, if you think that the model works at the level of Fable, of GPT-560, and the story that was told earlier, according to the motto, yes, the open models, which hang so three or four months behind the American front models, that's not the case.

**[00:08:41]** The case and the ironic is that these models exist in China, so there are different types of models.

**[00:08:47]** Export bans so that hardware in China can not be used and if you use these

**[00:08:52]** models then runs on the good American hardware, that the then again

**[00:08:56]** I think it's a shock moment, because it's a shock moment.

**[00:09:01]** Entropic and Open AI models for good money there, you can offer yourself meaningfully

**[00:09:08]** this model, if you use the necessary change height, which accordingly has to operate, yourself.

**[00:09:14]** This is also more data-friendly, one should not forget, whereby on the other hand

**[00:09:20]** The Moonshot AI has a lot to do with it.

**[00:09:25]** yes also reported, when chemist 3 came out that the servers were properly omitted,

**[00:09:29]** because that has already caused a stir, because a model in the class that does not

**[00:09:33]** with security questions regulated downwards, that simply runs quasi much more unbraked, that

**[00:09:39]** And if you look again at something like Entropic, yeah, I'm

**[00:09:45]** yes even private a user of the big Max plan of over 200 euros, if you expect that

**[00:09:50]** you can push almost 8000 euros a month through the Etter, then maybe that's

**[00:09:55]** also a bit curse and saw at the same time that if Entropic or Open AI maybe

**[00:09:59]** for customers direction the Chinese models loses, but I don't find it about the bow

**[00:10:05]** additionally survived, extremely crazily, how close we are to an area that models

**[00:10:13]** are so powerful that the open models are so powerful, which is so fast for us

**[00:10:19]** I didn't dream of it.

**[00:10:20]** I know when Fabel came out, we thought, oh, Fabel, yes now, and were so disappointed.

**[00:10:24]** when security was restricted, and then Soul came and didn't have the restriction

**[00:10:28]** And now comes an open model, where if you have, as I said, the necessary hardware,

**[00:10:33]** and that's not just Chemica 3, it came now also

**[00:10:37]** Quen, who also said we're bringing Faber level here now, it's just coming

**[00:10:42]** one model at a time from where you think that can't be true, what is

**[00:10:47]** the next step?

**[00:10:48]** Yeah, yeah.

**[00:10:49]** So, maybe we should just say again that we're chemical light at the front,

**[00:10:54]** The Chinese did not go ahead in all benchmarks, of course, and not at all points.

**[00:10:59]** It's also munschart, ey, I wouldn't say that myself either, so we're saying

**[00:11:02]** not now, we're better than Fable 5 or something, but just leave the numbers

**[00:11:07]** and there are just a few numbers, where the model is at the front, especially

**[00:11:11]** with the costs honestly, they are significantly lower than if you did this in the competition

**[00:11:15]** from America, that is a crucial point.

**[00:11:18]** And that, too, so, what might be exciting again, is it's going to stop

**[00:11:22]** also actually used.

**[00:11:23]** So I think Cursor uses Kimi when I haven't read it, for a coding agent I think I'm using, the composer, the composer 2, I think it's built on Kimi.

**[00:11:35]** So, yes, it's not like this is only used somewhere in China.

**[00:11:40]** No, it's also used here all over the world, because, as I say, the model is open for now.

**[00:11:47]** So you know what's in there, at least according to the weights the model is.

**[00:11:52]** on the other hand, just as you say it, if you can run nicely into the local, if you have the

**[00:11:56]** This is a very strong model.

**[00:12:00]** And there I am again such a bit, what I said at the beginning, it is actually not at all to me

**[00:12:04]** I think it's just great that we have a huge selection of

**[00:12:08]** This will lead to the model operators actually having strong models, because it will lead to the

**[00:12:14]** I would like to thank the rapporteur for his excellent report, and I would like to thank him very much for the work he has done on this subject.

**[00:12:23]** the Outcome, which I can then connect or generate, then it will of course be for

**[00:12:28]** all private individuals, companies, people are becoming more and more important to other factors such as

**[00:12:34]** How much does it cost me to run such a model?

**[00:12:39]** And that could in principle, so that's always healthy in the market, I think, because

**[00:12:43]** that we then gradually push the prices as well.

**[00:12:46]** We have now this year, we are, I think, from the mad token maximizing

**[00:12:51]** Over, that's just bullshit, that's just hype from the big companies to lure you into it.

**[00:12:56]** So many have claimed that you are actually not a real person anymore, if you don't somehow

**[00:13:01]** a billion tokens a day, especially if you're the developer.

**[00:13:05]** This has turned around a bit, because in detail, you say that doesn't necessarily have to

**[00:13:08]** you can also work skilfully with model selection and thus also less tokens

**[00:13:14]** use at one place or another, if it is not necessary at all. Go to the topic,

**[00:13:17]** that I have to say, yes, it becomes more relevant that we also have cost-effective models,

**[00:13:24]** which may not cost half a shirt for every small request I make,

**[00:13:30]** so that, I think, but a topic that is helpful to have good competition in the world.

**[00:13:35]** It's anyway that, I say, have it better than need and a lot helps, a lot are not

**[00:13:42]** automatically good advice for the use of AI models.

**[00:13:47]** Of course, I'm not the biggest model of the largest models now, in ultra code mode

**[00:13:51]** and if you haven't seen, use, I probably get for the question that I

**[00:13:57]** It is a very good answer, perhaps even a better answer than if I

**[00:14:01]** the model maybe down a level, what the, what the readiness to think

**[00:14:06]** as to whether I'm using an opus or a sunt, but for the question that I'm asking,

**[00:14:12]** I don't always need the largest, most expensive, fastest model,

**[00:14:16]** because first of all, if you cost more money and it needs to widen, also usually a bit

**[00:14:20]** longer time, yes. So if I ask the fable a question or a sunt a question

**[00:14:24]** and maybe it's enough Sonnet with medium efficiency, medium commitment setting

**[00:14:30]** And then this is already a component in time, until I wait, then comes a result.

**[00:14:36]** And from the side it's worth it anyway. I find that in the Chinese models,

**[00:14:40]** has also exciting that, if we look at the direction of perplexity, for example,

**[00:14:45]** Perplexity has the functionality per per perplexity computer, where they also go to say,

**[00:14:49]** Well, okay, you're gonna put this in, then I'll take this model.

**[00:14:52]** They also have something like, if I have a certain task, then I take the model,

**[00:14:57]** the model, me another task, me the model. And so it is said,

**[00:15:02]** Benchmarks, first of all benchmarks are not everything. Second, the systems differ.

**[00:15:07]** Where does it come in? Where does it bring its full performance?

**[00:15:12]** then it will be exciting to see if there might be such a LLM multiplexer,

**[00:15:17]** LLM orchestrator, there's LLM stuff where you say, well, I'm asking a question,

**[00:15:21]** because as a user I'm not really happy, maybe, but I just want to

**[00:15:25]** a good result. Best price ratio, such a kind of ml24.de, also we have again

**[00:15:33]** a great business idea and that gives you virtually the best model ever,

**[00:15:40]** nice the subject on which I sit. And what I found quite funny while thinking so much

**[00:15:46]** had what we want to talk about in this show today, actually, a few days ago,

**[00:15:51]** You've already noticed, we've got July 27th when we recorded this,

**[00:15:56]** a Monday. On the Friday before Entropik also managed again with O-Pos-5 and the

**[00:16:05]** Rumor kitchen says that May-Eye will even be released with GPT-6 in August.

**[00:16:13]** already, there was neatly stabbed again in the honissen nest, because so much is also not

**[00:16:19]** They all want to go back to the stock market in the near future.

**[00:16:23]** Chinese models begin to overtake them, then will certainly

**[00:16:28]** you don't want to react to it, because if you want to go to the stock market, you don't want to

**[00:16:32]** say to the stock market shortly after or before you go to the second, third,

**[00:16:36]** 4th place. That's the one and the other.

**[00:16:40]** There the Chinese models will probably also re-examine their

**[00:16:43]** If they are the major providers on the stock exchanges, they will play out strengths.

**[00:16:47]** Then, I think, what I said earlier at the start is,

**[00:16:51]** so according to the motto, I have a 200 few squeezed Euro subscription

**[00:16:54]** and burn in the month there tokens, which are worth perhaps 8,000 euros in comparison,

**[00:16:59]** then they won't be able to hold this up properly,

**[00:17:01]** because that is certainly the case when an appropriate market invests in the shares,

**[00:17:08]** can't subsidize as much as they might be able to do today,

**[00:17:12]** the hype and the push and I don't know,

**[00:17:14]** And then I'm curious about how the whole thing is going.

**[00:17:18]** From the side I am totally curious how this is developing, even if I am very disappointed

**[00:17:24]** I'm that I can't have run in on my little North Bog now chemic.

**[00:17:27]** That's too bad.

**[00:17:28]** However, if I could, I'd probably need personal protection because so much ramm,

**[00:17:32]** as you need there, yes, that is in today's days yes then, then you are rich, yes.

**[00:17:36]** So, seeing that you can't buy this in the North Bog, you'd be rich.

**[00:17:41]** Yeah.

**[00:17:42]** I think there's actually this chemical moment again, you know.

**[00:17:47]** I, too, was a time context, but in the last week we also

**[00:17:50]** There was such a small dip at the schipp manufacturers. There were such a small, the shares

**[00:17:55]** have lost a bit of driveway. Did they? Yes, short down, I think, again

**[00:18:02]** This is also a very short-term thing now, but of course it is all, too.

**[00:18:06]** We always have to be careful when new models come out.

**[00:18:12]** Of course, there are very, very many independent reviews immediately, which

**[00:18:16]** The principle of these models is weighting and looking at how the

**[00:18:19]** In this context, it should be pointed out that, in the light of the above considerations, it is not possible to assess the effectiveness of the measures in this field.

**[00:18:22]** and something like that.

**[00:18:23]** But it has always been that way, there is always such a short

**[00:18:26]** Hype phase, which is consciously then always driven by the model operators

**[00:18:29]** And as I said, she always finds it a little bit like

**[00:18:33]** Private users, I would say, everything you have is already so good.

**[00:18:38]** You can just use a lot of things, just keep trying.

**[00:18:40]** I've seen Notion again recently.

**[00:18:43]** I think if you use Notion, you can use all the models.

**[00:18:45]** If you have a notion subscription here anyway.

**[00:18:48]** But that's also crazy, because I have to tell myself again and again briefly.

**[00:18:51]** So when you look at Notion, then there's Notion.

**[00:18:54]** Sonny 465, Opus 47, Opus 48, Fable, Gemini 3.1 Pro,

**[00:19:00]** GPT 5.2, GPT 5.6, Terrain, GPT 5.2, GPT 5.4, GPT 5.5, GROC 4.3, Space XA, I didn't know,

**[00:19:12]** that there are already, 4.5, GROC image, then there are even smaller models, then stands above it,

**[00:19:18]** Gemini 3.5 Flash, Kimi 2.6, 2.7 Code, DeepSync V4, GLM, I could go on like this now,

**[00:19:26]** That sounds like a little sheep count, or sheep call.

**[00:19:32]** But I wanted to get up again so briefly from my EUX glasses, too, that

**[00:19:38]** I say this model selection for the private user and perhaps also for the user in the

**[00:19:47]** one or other office that doesn't like us very much, very much of his time with the

**[00:19:52]** topic AI busy, it's also really killed, honestly.

**[00:19:56]** that even with me sometimes already the subject, that I do not even know anymore, what

**[00:19:59]** which model do I actually take now? Do I actually need now

**[00:20:02]** really Fable for what I have just before? And so somehow there is

**[00:20:08]** also from user guidance in the various places, whether you now have a

**[00:20:12]** Desktop version uses or just uses a web variant, no matter. That's

**[00:20:17]** not really helpful, which we then say here for more complex tasks or

**[00:20:21]** for everyday complex tasks or sometimes important tasks,

**[00:20:26]** You'd rather take the model because it's all so difficult to judge.

**[00:20:29]** Do you have any thumb rule for which model you're taking now for what?

**[00:20:33]** Well, it's not meant to be copied, so the thumb rule is,

**[00:20:39]** the warning is coming that the limit is soon reached, the largest and after

**[00:20:43]** think for the last days of the week that you can't go into the week limit

**[00:20:47]** comes to take then something that you somehow get through it sharply, because

**[00:20:52]** Fable, for example, also uses much larger quotas at Entropic, where Fable uses

**[00:20:59]** I don't like it so much, so first of all, you always have to be careful what you use Fable for.

**[00:21:03]** Because they have this 30-day data-restancy, I'm talking to you, and the second is Opus.

**[00:21:10]** is actually in the movie, so in some bands it makes better and cheaper than

**[00:21:16]** from the side I'm more of the opus 5 friend right now and this what you said, like

**[00:21:22]** Do I deal with these things? Yes, that's terrible, isn't it?

**[00:21:26]** yes the models 01, 03, 02, they couldn't call themselves because of the name rights, could they?

**[00:21:31]** Minimax and Pro and Schlachmichtot, yes? And today comes Luna and Terra and you think so,

**[00:21:38]** Yeah, well, if you'll excuse me, yeah, what are those names?

**[00:21:45]** not used to anything new in every generation. Now Opus and Sonnet are certainly

**[00:21:48]** Not better, but they have a lot of version number on the back.

**[00:21:53]** yes not even the taste extra blue, however there is then the taste

**[00:21:56]** Ultracode and Max and Ultramax and I don't know, you'll get the hair dryer.

**[00:22:02]** You can't really expect anyone to do what I'm doing in that breath.

**[00:22:06]** again found quite funny, you may remember looking back at the last

**[00:22:10]** Season, when we were still on the road with the old covers, we used to have the theme,

**[00:22:15]** the models are actually getting stronger and bigger and bigger or will be like a bit

**[00:22:20]** like the human body according to the motto of loud sensors and subtle subnodes, which

**[00:22:26]** to decide or to take decisions because otherwise the moaning like the

**[00:22:31]** If human bodies are overwhelmed, you may also be able to reflect on the

**[00:22:35]** to shrug away from the hot stove, also completely somehow different control, than that the brain only over

**[00:22:40]** So getting into smaller models, and I thought that was totally funny.

**[00:22:45]** I stumbled over a project. Repository, which offers you virtually an open model and open

**[00:22:51]** Weights on a language model that has almost 30 million parameters, just under, completely

**[00:23:00]** offline running and respect on an 8-dollar micro controller, so in ESP32, somehow people who use it

**[00:23:07]** I'm sure you can tell me more about the fact that she can actually say,

**[00:23:10]** that these things could almost be used smart home, in smaller technologies,

**[00:23:16]** that you're kind of built up and you're at home, and you have the opportunity now,

**[00:23:21]** as a manufacturer on such a small chip that costs 8 dollars, which has somehow 512 kilowatts

**[00:23:26]** Ram or Achterbeerram somehow something like that. It doesn't matter what I want to get out of it. You have a small chip that costs almost no money and you can now run a local model and that's what I'm curious about, how this will affect, if we are now also able to run on so cheap hardware model.

**[00:23:46]** Where I want to look then you people can read what I have cut all the mess right there we can in the new fabrics.

**[00:23:55]** I also wanted to say season now, because this is the first time I use this word for which we have reached last year the whole season shot off.

**[00:24:05]** Yes, I find locally installed models that can work in small hardware gadgets,

**[00:24:14]** It's so exciting.

**[00:24:15]** I think this is such a thing where I say there are really cool applications always

**[00:24:19]** Out.

**[00:24:20]** Because there's maybe a little bit of this way we're learning right now.

**[00:24:26]** interact with the profit, will also change again.

**[00:24:29]** There was this hype about the AI devices two, three years ago, there's everything a little bit

**[00:24:33]** I've been quieter.

**[00:24:34]** that in principle these AI variables were out for a short time,

**[00:24:38]** Businesses have been raised, not so much has yet happened,

**[00:24:41]** but that will come now, because of course it is super beneficial,

**[00:24:44]** if I can run things in the restaurant,

**[00:24:46]** I need to install less technology, it doesn't necessarily have to be internet-connected,

**[00:24:49]** But it can help me very well.

**[00:24:51]** Well, I've already seen those, so in the past, there were always survival manuals like this.

**[00:24:56]** which you needed when you were in B-camping,

**[00:24:58]** you can just pack everything locally now on flat grit

**[00:25:01]** and does not just have to read or search as a long PDF version, but

**[00:25:05]** also as an LMM, which in case of an emergency, if you have the hindquarters, you did not see,

**[00:25:11]** Telling you the leg while climbing, he can then beg you how you

**[00:25:14]** in China then bast himself together, with your scenes quasi the sticks after

**[00:25:19]** and build a pressure bandage from which you can then move the mountain again.

**[00:25:25]** You don't know my scenes, if my tooth should be tapped, don't worry, Tim,

**[00:25:29]** Don't do that.

**[00:25:30]** Yeah, but I think that's another very different thing, so I think who's got more than that.

**[00:25:34]** A new feature of Open AI in Codex has also been released. Who is the Recorded Replay?

**[00:25:38]** It's kind of like that. I can basically now record videos of myself, of my screen.

**[00:25:45]** Can then throw that into Codex afterwards and Codex makes a skill out of it. So I'll just show him how I basically do that.

**[00:25:52]** Yes, you want to say something, say something directly. I want to say something about it. I was just totally impressed by this feature.

**[00:25:59]** I thought how horny is that?

**[00:26:02]** And then I did that, we build our own Harnes in the company and then

**[00:26:07]** that took about two hours, and then he could.

**[00:26:10]** Yeah, that's good.

**[00:26:11]** That's just funny.

**[00:26:12]** I have to share that now, it has nothing to do with Hundellen, but I am

**[00:26:16]** Just so excited.

**[00:26:17]** And that's what I've been looking at, I can imagine when you're doing something like that.

**[00:26:22]** There may be people who want to use a service context, and then there may be people who want to use it.

**[00:26:25]** Just as OpenAI and a Tropic Bout don't like it, because the thing wants the keyboard

**[00:26:29]** read it, the thing wants to read your screen, you're sure it's really that way

**[00:26:34]** reads, if you want that and stuff, that's missing a little bit of the understanding

**[00:26:38]** And stuff like that.

**[00:26:39]** And then I just sat down and thought, let's see what the model

**[00:26:42]** I'm really doing it.

**[00:26:43]** So with us in our urine, what the model does when you just watch the video

**[00:26:47]** the screen video and a screen video where you do something, so to

**[00:26:54]** Example of a website service, an internal website service and simple

**[00:26:57]** while you're serving them, explain what you're doing, and then I've been talking like that, yes

**[00:27:01]** here is an input field and have always marked with the mouse what I talked about

**[00:27:05]** here is an input field and I don't need this and here

**[00:27:09]** then stand the answers and here you can see if there was a mistake and have

**[00:27:13]** I'm kind of so busy with this video, with the thing and then I have this

**[00:27:16]** Recorded video and told him to make a skill out of it and white

**[00:27:20]** The thing says he's got a skill, he's cut the video, he can watch it.

**[00:27:26]** according to the motto, how often what changes in the video, takes out everything, where possibly even

**[00:27:31]** nothing happened because you didn't move the mouse that the site was just thinking

**[00:27:35]** or I don't know what, so just took the rest of the pictures, got out of the

**[00:27:39]** the rest of the pictures built a skill, the pictures are embedded in the skill as an orientation pattern

**[00:27:45]** and then he went over after that and said, well, okay, I got it from you

**[00:27:49]** learn, you want to go to this website and here are the things you need. Here are the things,

**[00:27:53]** I've asked myself a few more questions.

**[00:27:58]** Playwright, this is such a library that it makes kind of a browser operation, just that

**[00:28:05]** you can operate Playwright Headless, so without a visible browser interface. And then

**[00:28:11]** the thing goes there, works the skill off, serves this website and always then,

**[00:28:15]** if he doesn't know what to do, because the website might look different, because somehow

**[00:28:19]** I don't know, he just wants to orient himself again, looks up there almost again

**[00:28:23]** This screenshot, which he has saved, along with the skill and uses it.

**[00:28:26]** And for a long time, you can go and say,

**[00:28:31]** All right, you've got a lot of different rack systems.

**[00:28:35]** in the next conversation with Cornelius again, so much pre-advertising can be.

**[00:28:38]** If he's able to put all this stuff in one skill,

**[00:28:43]** in your agent Harness. With every other listener it would be Claude or Codex app.

**[00:28:50]** our own, our own Harness, which we have built. You can play it like that.

**[00:28:55]** And so you can connect other systems to your harness, just through a skill that he

**[00:29:04]** has learned to control due to videos, audio tracks and possible things. And last

**[00:29:10]** Then I always wonder why Entropik built so much stuff around it, or Codex built so much stuff around it.

**[00:29:15]** that you have to give so much permission in the, if actually a video is enough,

**[00:29:20]** that you're recording or a training video that you might be doing somewhere in a study program

**[00:29:24]** Find and say, come here, look, you'll notice the rest.

**[00:29:27]** Have fun, fire free. The power is incredible.

**[00:29:30]** That's what I'm talking about, that's what we're saying.

**[00:29:34]** We're basically going to see if this is now installed on local,

**[00:29:39]** Hardware gadgets, videos, voice, audio.

**[00:29:42]** Imagine what you're describing right now,

**[00:29:44]** is basically a topic that happens on a screen,

**[00:29:48]** where I can work things out and build a skill out of it.

**[00:29:51]** It is often the case that production is no longer difficult.

**[00:29:55]** Even today, even before AI, it has not been difficult.

**[00:29:58]** We already had good people who could make design,

**[00:30:01]** often it is always so that this path from the actual idea,

**[00:30:06]** the translation, what is actually the real problem at the moment that we recognize

**[00:30:11]** where we have to put work in, workflows, situations, hospitals,

**[00:30:16]** Airport, whatever to analyze to look, how can one analyze these processes

**[00:30:20]** All this is what is happening in the poor world and then afterwards

**[00:30:25]** if necessary, a piece of code and an application leads to something like

**[00:30:28]** If we take this up even better, then improve the sub-area of this process.

**[00:30:33]** can become more interactive in the future and also more interactive, without me somewhere, and there I am now

**[00:30:38]** large of, if we switch to such formats, because then I do not need

**[00:30:42]** sometimes even know the concept programming language at all. So if we settle about it for a moment

**[00:30:48]** have that English is the new programming language, then are such approaches that we now

**[00:30:51]** of course, the replacement of the fact that I see this level of abstraction

**[00:30:56]** I don't need to understand any more that a skill may be

**[00:31:02]** a textual arti needed to describe how the skill should behave and additionally

**[00:31:06]** need more documents as templates so that it knows which output format it is doing

**[00:31:11]** should or any connection to LMCPs. But no, the machine can easily see,

**[00:31:15]** what we do and derive from it, which might be a good solution, a similar one.

**[00:31:22]** Output could generate as it has seen there.

**[00:31:24]** And that's actually one, so I think that's one of the framework conditions that we

**[00:31:31]** in the next weeks and months much, much more will see.

**[00:31:35]** That we see, there are other possibilities besides the pure text input.

**[00:31:40]** So each of us probably took the photo of the wine shelf at the Rewe

**[00:31:45]** or at the weed or something and looked, in companies we'd rather have a leg chatshipiti

**[00:31:49]** or photograph the fridge to get the recipes that are still possible

**[00:31:54]** with the rests that are so moldy in the fridge. But that was just such a live insight into the

**[00:32:00]** No, I don't think so at all. We are well equipped, yes and

**[00:32:05]** We'll never be thrown away from the siertel.

**[00:32:10]** But the thing is, I know the thing is that we really are now,

**[00:32:17]** So, we were multimodal, that could be the ones who's been eis for a long time now, I could give him videos for a long time,

**[00:32:24]** could upload images for a long time or text or video or whatever, so I could put many things away.

**[00:32:30]** But now we get into this phase, where it's not just too pure, okay, there's knowledge in it, but I can use it for action as you just described it.

**[00:32:40]** And when we enter this phase, of course, it will be even more exciting if we look at AI in the real world.

**[00:32:46]** That's right, and she'll know more about what's happening, and there's going to be a lot, I think, where was this year in our new season, in season 2 of Zingtüpfeln Tenkeei to make one or the other episode.

**[00:32:58]** We were originally with the open models. I think we did well. What I would like to say about your thoughts while you were talking, suddenly things like YouTube movies become quite exciting.

**[00:33:14]** 'Cause I'm saying I've got why I've got that, for example, another topic is also

**[00:33:20]** private and Apple Business Mesh, that's such a solution from Apple where you don't have devices very well

**[00:33:25]** But where you can just deal with a few portars from Apple, let's say it like that.

**[00:33:31]** And the funny thing, I really have to try this, imagine, there are all these YouTube movies,

**[00:33:37]** where some influencer or Apple himself tells about things and you give it to him and then you have the opportunity to

**[00:33:42]** that your AI system is using this portal for you and makes it perhaps much more accessible,

**[00:33:49]** When you did it until two weeks ago. So from the side I think we should also

**[00:33:57]** the possibilities of the new Hannes and the new systems, not only the new ones

**[00:34:02]** models, even to follow soon. And maybe also with a critical

**[00:34:08]** Perspectives and I already have a guest in view, who knows very well with this whole

**[00:34:13]** The topic of VR and augmented reality glasses. We can also interview them there, because

**[00:34:20]** that of course also gives the negative side. So if we, that is like the box of the

**[00:34:24]** Panthauer, so of course, many are also interested in this data to the models

**[00:34:28]** to do better or to do other things, and if now all people, of course,

**[00:34:33]** because it has an advantage that I might take something with my glasses all the time

**[00:34:37]** of course, there is also the question of the

**[00:34:43]** Data protection in the background. What do I actually record where we store this data and

**[00:34:47]** So if we like to do that, then we should also be trained in the usual way

**[00:34:52]** again illuminate and discuss both sides of the medal. And I feel about it

**[00:34:57]** because I had EVA with the colleague, we have to make the appointment now, a succession

**[00:35:01]** We can take this up right away. I just got into it during

**[00:35:05]** And you, correctly said you said two sides of the medal, there's still the medal of the

**[00:35:10]** Snöten-Mamons and I were just wondering if you could train with a lot of people.

**[00:35:15]** YouTube movie, a skill, whether you're doing some kind of skill library with a real added value

**[00:35:19]** But after we said we were in a new season,

**[00:35:25]** the heading, making money with AI, I don't think we'll start with it anyway,

**[00:35:30]** but I'm very looking forward to a follow-up guest. I'm also very pleased that

**[00:35:35]** we have a episode with a guest next week, yes, I already mentioned Cornelius.

**[00:35:39]** And I'd say, Jens, we're going to do this fast.

**[00:35:45]** Shut up before a new model comes out and everything we've done so far is not done for

**[00:35:50]** Thank you for taking the time.

**[00:35:55]** New season together and leave us a comment. We, our new

**[00:35:59]** Coverfit and with that we say see you soon at Sinkdifferent, Sink AI. We look forward to seeing you. Tschau.

**[00:36:06]** Ciao.

**[00:36:09]** Welcome to Thinkdifferent, Think AI, the podcast of Mark and Jens.

**[00:36:14]** Two technology-loving minds who not only talk about artificial intelligence, but live it.

**[00:36:21]** Here there are clear classifications, real practical insights and a fresh look at what is possible.

**[00:36:27]** Understandable, critical and always with an eye tinker.

**[00:36:31]** AI to think, to smile and, above all, to share.
