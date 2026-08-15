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
translation_provider: "claude"
translation_model: "claude-opus-5"
translated_from_file: "transkripte/051 - China Schock.md"
translated_at: "2026-08-15T00:00:00+00:00"
---

# China Schock

**Published:** Sun, 02 Aug 2026 13:12:00 +0000
**Duration:** 2201
**Web player:** https://think-ai.podigee.io/51-china-schock
**Cover:** https://images.podigee-cdn.net/0x,sv2fciZLgYDWTZ8gwb_8SBymao_i7OR3FDbyh4PWGAqg=/https://main.podigee-cdn.net/uploads/u73317/5d412608-7095-43c5-ae63-47463e7ce11e.jpeg
**Audio:** https://audio.podigee-cdn.net/2548954-m-e5f81efdd3bf65b6d89ff827c5843570.mp3?source=feed

## Description

Kimi K3, open weights and the question of who leads the AI world
Season 2 begins, the cover is new, and Mark and Jens are one year and seven days old. The first question of the new season is the biggest one right away: who actually leads the AI world? Still the USA with their frontier models, or has China just triggered the next DeepSeek moment? Both say up front what they often say: in parts, we have no idea. Which is exactly why they talk about it.

Before that, a story that made it into the German press. A model from OpenAI was supposed to solve a task in a sealed-off test environment and instead dug itself a way out and fetched the solution from Hugging Face, because that was easier than working it out itself. Mark compares it to an exam candidate in a room without windows or doors. The second part of the story is the genuinely bitter one: on the defender side, the models from Anthropic and OpenAI waved it off because they took their own countermeasure for an attack. What ended up being used for the defense were Chinese models.

Then the numbers at the heart of it. Kimi K3 from Moonshot AI appeared on July 16, the subscription costs between a third and half of what comparable US models cost, depending on compute, and the weights have recently been made public. 2.8 trillion parameters to run yourself, if your hardware can take it. Mark's machine can't, a Mac Studio with 512 GB of RAM can't, two of them can't either. The old story that open models trail the American frontier models by three or four months no longer holds. Cursor builds its coding Agent Composer on Kimi, Qwen is following, and the irony is that these models really pick up speed as soon as they run on the good American hardware that is under export control in China. Jens pushes back that the leaderboard doesn't interest him much: competition is healthy, it pushes prices down, and past a certain point, cost matters more to users than the last benchmark percentage point.

Which brings both of them to the everyday problem. Mark works out how many tokens a 200-euro subscription pushes through, tokens that would be worth more like 8,000 euros bought individually, and wonders how much longer the providers will subsidize that once they are listed on the stock market. Anthropic added Opus 5 on the Friday before the recording, and GPT-6 is rumored for August. At the same time, the selection is barely manageable: Jens reads out the model list from his Notion and goes from counting to counting sheep. For users outside the AI bubble this is overwhelming, and the providers' guidance ("for everyday complex tasks") helps no one. Mark's honest rule of thumb: take the biggest model until the warning comes that the limit is nearly reached, then downshift for the rest of the week. Not recommended for imitation. The principle behind it is: more is more is bad advice for choosing a model, because the biggest model also costs more and takes longer. Perplexity Computer shows where this is heading with its task-dependent routing, and the idea of an LLM orchestrator that assigns you the best price-performance model for every question is lying right there in the street.

The second part turns the direction around: downward instead of upward. Mark stumbled across a repository that runs an open language model on an ESP32 microcontroller for 8 dollars, completely offline. Here it is: github.com/slvDev/esp32-ai. 28.9 million parameters on an ESP32-S3 with 512 KB of SRAM, around 9.5 tokens per second, none of it goes to a server. The trick is Google's per-layer embeddings idea from Gemma: 25 million parameters sit as a lookup table in slow flash, about 450 bytes of them are read per token, and only the computing part stays in fast memory. The predecessor model on a chip like that had 260,000 parameters, so roughly one hundredth. To be fair: the thing is trained on TinyStories, it writes short stories and answers no questions. The architecture is what's interesting, not the output. Jens sees in it the return of the AI wearables that were hyped hard two or three years ago and then went quiet, including the survival manual that explains to you on the mountain how to build yourself a splint.

And then it gets practical. At OpenAI a record-and-replay feature appeared in Codex: record your screen, throw it into the agent, and out comes a Skill. Jens found it impressive at first, then grew skeptical because a feature like that wants to read along with your keyboard and screen, and rebuilt it in his own harness in two hours. A screencast with spoken commentary is enough: the model breaks the video apart, throws out the frames where nothing happens, builds itself a Skill from the rest with screenshots as orientation patterns, and then operates the website headless via Playwright. When it gets stuck, it looks at its own screenshots. Mark's point: not long ago the line was that English is the new programming language. Now this abstraction layer falls away too, because the machine can simply see what we do. That leaves the other side of the coin, and that is data protection: anyone constantly recording with a pair of glasses produces data that a great many people are very interested in. There's a separate episode with a guest coming on that, and next week Cornelius is here, on the topic of Second Brain.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who don't just talk about artificial intelligence, they live it.

**[00:00:14]** Here you get clear perspective, real hands-on insight and a fresh look at what's possible.

**[00:00:20]** Understandable, critical and always with a wink.

**[00:00:24]** AI to think about, to smile about and above all to talk about.

**[00:00:34]** A warm welcome to Think Different, Think AI.

**[00:00:37]** If you listened to the last episode, then you've been spoiled with statistics, spoiled with

**[00:00:43]** quotes, spoiled with guest commentators.

**[00:00:49]** We're basically in a kind of new season.

**[00:00:53]** Jens is back on board as well.

**[00:00:56]** Glad you're still with us, Jens, in the new season, and today we're going to talk

**[00:01:00]** about something where we'll probably say, more than once,

**[00:01:05]** we have no idea.

**[00:01:06]** Anyone who wants to know what we mean by this "no idea" business, just go and listen to the

**[00:01:11]** anniversary episode again, because for "no idea"...

**[00:01:15]** Yes, birthday, anniversary, along the lines of, whoever bought it gets to say what it's called,

**[00:01:22]** yeah, like that.

**[00:01:23]** All right then.

**[00:01:24]** say, let's put it that way. And today we want to talk a bit about Fable,

**[00:01:30]** well, not quite, about all the Fable moments that have somehow caught up with the world,

**[00:01:38]** because I'd like to bring everyone up to speed first and then we can get into the conversation together.

**[00:01:45]** Maybe you still remember, there was this Mythos moment, an AI model so dangerous

**[00:01:50]** that you couldn't release it to the world. Then there was Fable as a model and Fable

**[00:01:55]** was a model of the Mythos class. I get this Star Trek thought every time, but

**[00:02:01]** Intrepid class, whatever, let's leave the nerd stuff out of it. Then it was banned

**[00:02:06]** in part because of export controls. Then it was allowed again and Fable was like, ah yes,

**[00:02:13]** come on, it's a Mythos class model, it's good after all, but then it held back on security.

**[00:02:17]** Held back on biology. Yeah, along those lines. What do I care

**[00:02:23]** about yesterday's knowledge, more and more models keep coming out that, I'd say,

**[00:02:31]** are overtaking Fable. And if you're thinking now, sure, I've heard of OpenAI, ChatGPT, version 5.6,

**[00:02:38]** Luna Terra Soul, yes, that too, but the Chinese models as well. They're

**[00:02:46]** really putting their foot down and have a few peculiarities, and I'm glad that

**[00:02:50]** Jens is getting into it with me today, with the question of who's actually leading

**[00:02:57]** the AI world? Is it still the USA with the big

**[00:03:03]** frontier models, or has China, let's say, triggered the next DeepSeek moment

**[00:03:10]** and the next shock moments, because suddenly there are free models. Jens, good

**[00:03:15]** to have you here. Thanks, Mark. It's nice that we're now

**[00:03:19]** one year and seven days old. So of course I have to fall in line. So our first

**[00:03:25]** episode in the new year, in a new look as well. Happy to hand the computer over too. We've

**[00:03:31]** decided that we're going to adjust our design a bit, and we'll be doing that every year from now on.

**[00:03:36]** So yes, we have to stay with ourselves for another year.

**[00:03:39]** That's one way to do it, so yes, that's just great.

**[00:03:42]** You can paste things behind it, you can swap the pictures, oh yes, great idea.

**[00:03:45]** But maybe more on that later, or more next time.

**[00:03:49]** The question, Mark, who's leading?

**[00:03:53]** I think that's getting hard to answer at all at the moment, and from a user perspective

**[00:03:59]** I always think

**[00:04:01]** I don't really care either, you know? I just think it's great that we have such a

**[00:04:06]** marketplace in the world that, in this kind of competitive situation, a competition-driven business, we all know that,

**[00:04:13]** means we get new models presented to us on almost a weekly basis, which

**[00:04:20]** A

**[00:04:21]** often, well

**[00:04:23]** Yeah, not always. I'm wrong. Fable has now shown that it burns more tokens. Some of these models are getting leaner in

**[00:04:29]** token consumption too, but above all they're all getting better in quality. No matter how they're built, what technology actually underlies it, how the LLM works.

**[00:04:38]** From week to week they're still noticeably better than the models before them, and still give no hope of an end to the flagpole.

**[00:04:48]** But I would commit myself and say that with this Kimi 3 moment we've just had,

**[00:04:55]** it was definitely a shock moment for the American models, which again

**[00:05:01]** and the big frontier labs in the background, which actually did react a bit

**[00:05:05]** put out again when Kimi 3 was introduced, and then there was talk from the highest

**[00:05:10]** levels again about theft and about this not all being above board

**[00:05:16]** and so on, but yes, it's definitely a shock moment and maybe Kimi is

**[00:05:21]** a bit ahead right now, so the Chinese, on this topic.

**[00:05:24]** I think they're ahead on a few points, but I just wanted to, since

**[00:05:29]** you were talking about this shock moment, I just wanted to briefly, you've surely

**[00:05:34]** heard it in the news, it somehow made it, let's say, into the German

**[00:05:38]** press as well, when word from OpenAI was that their model had broken out

**[00:05:45]** and had hacked Hugging Face. You have to picture it as if you'd locked the exam candidate,

**[00:05:52]** meaning the OpenAI model, into a room with no windows and no doors, and the thing

**[00:05:59]** still basically dug itself a way out. Instead of solving a problem,

**[00:06:03]** it basically hacked into Hugging Face and fetched the solution there,

**[00:06:07]** because it found that easier than producing the solution properly itself.

**[00:06:11]** And the story is actually doubly funny, because whether this model

**[00:06:17]** really pulled that off and did it is one thing, but when you listen to

**[00:06:22]** what the defender side looked like, it turned out that they tried to use the AI models

**[00:06:26]** to fend off the attack, and the models from Anthropic and Open

**[00:06:30]** AI said, no, no, no, no, I can't do any defense here,

**[00:06:34]** because the models themselves thought that what they'd flagged as defense

**[00:06:38]** would be an attack.

**[00:06:39]** And so Hugging Face had to fall back on Chinese models, they were apparently a

**[00:06:43]** bit more open-hearted about protecting them from the attack.

**[00:06:47]** But we were just on this shock moment from Kimi 3.

**[00:06:50]** Kimi 3 from Moonshot AI, that was on the 16th of

**[00:06:56]** July, an announcement, well not an announcement for publications, and with

**[00:07:00]** them it works so that the models are basically served up on their machines. You can

**[00:07:07]** take out subscriptions there, just like you can with Anthropic and with ChatGPT.

**[00:07:15]** But because you're basically, well, I'd say competing with the American

**[00:07:21]** products, you usually get it offered very cheaply. So the K3

**[00:07:25]** subscription costs something like half to a third of what you'd have to pay with Fable

**[00:07:31]** for comparable compute, and as of the time of this recording, we're

**[00:07:38]** sending the episode out a bit later, today is July 27, the

**[00:07:44]** weights of the model are public as well, so that if you're equipped with the right hardware

**[00:07:49]** you're able to run the 2.8 trillion parameter model yourself.

**[00:07:56]** So, my machine is out. A Mac Studio with 512GB of RAM is out too.

**[00:08:02]** Even two Mac Studios with 512GB of RAM each are out.

**[00:08:07]** But if you have a suitably big piece of metal, you can run this model yourself.

**[00:08:16]** And that, I think, is a whole different front door, when you consider that the model works at the level of Fable, of GPT-560, and the story people used to tell, along the lines of, yeah, the open models trail the American frontier models by three or four months, that's just not the case.

**[00:08:41]** And the ironic thing is that these models, in China there are, well, there are various

**[00:08:47]** export bans, so that certain hardware can't be used in China, and if you let these

**[00:08:52]** models run on the good American hardware, they really put their foot down

**[00:08:56]** on top of that, and I do think that's a shock moment, because while

**[00:09:01]** Anthropic and OpenAI offer models for good money, you can, in effect,

**[00:09:08]** run and use this model yourself if you have the necessary spare change for the hardware.

**[00:09:14]** That's also more privacy-friendly, you shouldn't forget that either, though on the other

**[00:09:20]** hand there's one thing you also shouldn't leave out of account. Moonshot AI did

**[00:09:25]** report, when Kimi 3 came out, that the servers were properly overloaded,

**[00:09:29]** because it really caused a stir, because a model in that class that doesn't

**[00:09:33]** dial itself down on security questions, that basically runs much more unrestrained, that

**[00:09:39]** they're running it. And if you look again at something like Anthropic, well, I'm

**[00:09:45]** privately a user of the big Max plan myself, over 200 euros, and if you work out that

**[00:09:50]** you can basically push 8000 euros a month through the pipe there, then that's maybe

**[00:09:55]** a bit of a blessing and a curse at once, that if Anthropic or OpenAI maybe

**[00:09:59]** loses customers toward the Chinese models, but coming back around, I still find it

**[00:10:05]** extremely wild how close we are to a point where models

**[00:10:13]** are so powerful, where the open models are so powerful, something we wouldn't have

**[00:10:19]** dreamed of happening this fast.

**[00:10:20]** I know, when Fable came out we thought, oh, Fable, now we're talking, and were so disappointed

**[00:10:24]** when security was restricted, and then Soul came and didn't have the restriction

**[00:10:28]** And now an open model comes along where, as I said, if you have the necessary hardware,

**[00:10:33]** you can just let it run, and it's not only Kimi 3, now there's also

**[00:10:37]** Qwen, who also said, we're delivering Fable level here, one model after another

**[00:10:42]** is coming out right now where you think, this can't be true, what's

**[00:10:47]** the next step?

**[00:10:48]** Yeah, yeah.

**[00:10:49]** Well, maybe we should also say, to be fair, that when we say Kimi is ahead,

**[00:10:54]** the Chinese are ahead, of course that's not in all benchmarks and not on all points.

**[00:10:59]** Moonshot say it too, hey, I wouldn't say it myself either, so we're not

**[00:11:02]** saying now, we're better than Fable 5 or anything like that, but rather just let the numbers

**[00:11:07]** speak, and there are simply a few numbers where the model is out in front, above all

**[00:11:11]** on cost, honestly, which is significantly lower than if you do it with the competition

**[00:11:15]** from America, that's a decisive point.

**[00:11:18]** And on top of that, what's maybe also interesting is that it's actually

**[00:11:22]** being used.

**[00:11:23]** I believe Cursor uses Kimi, if I read it right, for a coding Agent that I think they use, the Composer, Composer 2 I think it is, that's built on Kimi.

**[00:11:35]** So yeah, it's not like it's only being used somewhere in China.

**[00:11:40]** No, it's being used everywhere in the world here too, because the model, as I say, is open in the first place.

**[00:11:47]** So you know what's in it, at least as far as the weights of the model go.

**[00:11:52]** on the other hand, as you say, if you can nicely run it locally, if you have the

**[00:11:56]** compute power, then it's also a strong model. It's a really strong model.

**[00:12:00]** And there I'm back a bit to what I said at the beginning, it's actually not

**[00:12:04]** that important to me who's out in front right now. I just think it's great that we have a huge selection of

**[00:12:08]** really strong models, because that will mean the model providers actually have to

**[00:12:14]** think about it, if we're always very, very comparable at the front with the output and

**[00:12:23]** the outcome that I associate with it or can generate from it, then of course for

**[00:12:28]** all private individuals, companies, people it will become more and more important to look at other factors, like

**[00:12:34]** cost, quite simply. What does it cost me to run a model like that?

**[00:12:39]** And that could in principle, well, that sort of thing is always healthy in a market, I think, because

**[00:12:43]** it means we then gradually push the prices down too.

**[00:12:46]** This year, I think, we've gone from the insane token maximizing

**[00:12:51]** over, that's nonsense, that's just hype from the big companies to lure you in.

**[00:12:56]** So a lot of people claimed you're not really a proper human being any more if you don't somehow

**[00:13:01]** use billions of tokens a day, especially if you're a developer.

**[00:13:05]** That's shifted a bit, toward saying that doesn't necessarily have to be

**[00:13:08]** the case. You can also work cleverly with model selection and thereby use fewer tokens

**[00:13:14]** in one place or another, when it isn't needed at all. Toward the topic where

**[00:13:17]** I have to say, yes, it's becoming more relevant that we also have cost-effective models

**[00:13:24]** that don't cost you an arm and a leg for every little request I make,

**[00:13:30]** so that's a topic, I think, where it's helpful to have good competition in the world.

**[00:13:35]** It's the case anyway that, let's say, better to have than to need, and more is more are not

**[00:13:42]** automatically good advice for using AI models.

**[00:13:47]** Of course, if I use the biggest model of the biggest models, in ultra code mode

**[00:13:51]** and whatever else, then for the question I'm

**[00:13:57]** asking I'll probably get a very good answer too, maybe even a better answer than if I

**[00:14:01]** shift the model down a level, in terms of, in terms of how much thinking effort

**[00:14:06]** it puts in, whether I use an Opus or a Sonnet. But for the question I'm

**[00:14:12]** asking, maybe I don't always need the biggest, most expensive, most powerful model,

**[00:14:16]** because first, it costs more money, and second, it usually also takes a bit

**[00:14:20]** longer, yeah. So if I ask Fable a question or ask a Sonnet a question

**[00:14:24]** and maybe Sonnet with medium efficiency, medium effort setting is enough

**[00:14:30]** And then there's a time component to it too, how long I wait until a result comes back.

**[00:14:36]** And from that angle it pays off anyway. What I find exciting about the Chinese models

**[00:14:40]** in that respect is that, if we look toward Perplexity for example,

**[00:14:45]** Perplexity has this functionality with Perplexity Computer, where they go and say,

**[00:14:49]** well okay, you've got this in mind, so I'll take this model.

**[00:14:52]** They also have something like, if I have a certain task, then I take that model,

**[00:14:57]** for me that model, for me another task, for me that model. And as you just said,

**[00:15:02]** benchmarks, first of all benchmarks aren't everything. Second, that's where the systems

**[00:15:07]** differ. Where does it settle in? Where does it deliver its full performance? And

**[00:15:12]** then it does get exciting to see whether at some point there might be an LLM multiplexer,

**[00:15:17]** LLM orchestrator, LLM something, where you say, right, I ask a question,

**[00:15:21]** because as a user I don't really care, maybe, I just want

**[00:15:25]** a good result. Best price-performance ratio, a kind of ml24.de, there we go, we've got another

**[00:15:33]** great business idea, that basically provides you the best model ever,

**[00:15:40]** for the topic I'm sitting on. And what I found quite funny, while I was thinking about

**[00:15:46]** what we wanted to talk about in this show today, a few days ago to be precise,

**[00:15:51]** you've already picked up on it, today is July 27 as we're recording this,

**[00:15:56]** a Monday. On the Friday before that, Anthropic went and delivered again with Opus 5, and the

**[00:16:05]** rumor mill says that OpenAI will even come out with GPT-6 in August. You can really tell

**[00:16:13]** that someone poked the hornets' nest properly, because none of this is

**[00:16:19]** that secret. They all want to go public soon as well. If the

**[00:16:23]** Chinese models now start overtaking them, then they'll certainly

**[00:16:28]** want to react to that, because if you want to go public, you don't want to

**[00:16:32]** let's say go public just after, or just before, being pushed down to second, third,

**[00:16:36]** fourth place. That's one thing, and the other.

**[00:16:40]** The Chinese models will probably play to their

**[00:16:43]** strengths again once the big providers are listed on the exchanges.

**[00:16:47]** Then, I think, what I said earlier at the start,

**[00:16:51]** along the lines of, I have a subscription for 200-odd euros

**[00:16:54]** and burn tokens per month that are worth maybe 8,000 euros by comparison,

**[00:16:59]** then they won't really be able to keep that up either,

**[00:17:01]** because then surely, once a corresponding market is investing in the shares,

**[00:17:08]** they can't subsidize as much as they maybe can today,

**[00:17:12]** to drive the hype and the push and who knows

**[00:17:14]** what a bit further up, and then I'm curious to see how the whole thing plays out.

**[00:17:18]** From that side I'm totally curious how it develops further, even if I'm very disappointed

**[00:17:24]** that I can't run Kimi on my little notebook now.

**[00:17:27]** That's a real shame.

**[00:17:28]** Although, if I could, I'd probably need a bodyguard, because that much RAM,

**[00:17:32]** as much as you need there, yeah, these days that means, well, then you're rich, yeah.

**[00:17:36]** So, quite apart from the fact that you can't buy that in a notebook, you'd be rich.

**[00:17:41]** Yes.

**[00:17:42]** since you mention rich. I think this Kimi moment, I don't know

**[00:17:47]** whether there was a timing connection there, but last week we also saw

**[00:17:50]** a small dip with the chip manufacturers. There was a small one, the shares

**[00:17:55]** lost a bit of momentum. Did they? Yes, briefly down and, I think, back

**[00:18:02]** up again. It's a very short-term thing, but of course all of this is also,

**[00:18:06]** we always have to be careful there too, even when new models come out.

**[00:18:12]** Of course there are very, very many independent evaluations straight away that basically

**[00:18:16]** weigh these models and look at how they behave

**[00:18:19]** compared with other models and whether they're better or worse, which tests they

**[00:18:22]** pass and so on.

**[00:18:23]** But it's still always the case, there's also always a short

**[00:18:26]** hype phase that's deliberately driven by the model providers.

**[00:18:29]** And as I said, it always strikes me a bit that as a

**[00:18:33]** private user I'd say, everything you have is already so good.

**[00:18:38]** You can just use a lot of things there, just keep trying things out.

**[00:18:40]** I recently had another look at Notion.

**[00:18:43]** There, I think, if you use Notion, you can nicely use all the models

**[00:18:45]** if you have a Notion subscription anyway.

**[00:18:48]** But that's crazy too, I have to remind myself of that every time.

**[00:18:51]** So, if you look at Notion, then in Notion there's

**[00:18:54]** Sonnet 465, Opus 47, Opus 48, Fable, Gemini 3.1 Pro,

**[00:19:00]** GPT 5.2, GPT 5.6, Terra, GPT 5.2, GPT 5.4, GPT 5.5, Grok 4.3, SpaceX AI, I didn't even know

**[00:19:12]** that existed yet, 4.5, Grok Image, and then there are smaller models, listed separately above,

**[00:19:18]** Gemini 3.5 Flash, Kimi 2.6, 2.7 Code, DeepSeek V4, GLM, I could go on like this,

**[00:19:26]** It sounds a bit like counting sheep, or like calling sheep.

**[00:19:32]** But I wanted to briefly step in again with my UX glasses on and

**[00:19:38]** say that this model selection, for the private user and maybe also for the user in

**[00:19:47]** some office or other who doesn't spend, like we do, a very, very large part of their time on

**[00:19:52]** the topic of AI, is honestly overwhelming. So I sometimes have the

**[00:19:56]** issue myself that I no longer know what,

**[00:19:59]** which model should I actually take now? Do I really need

**[00:20:02]** Fable for what I've got in front of me right now? And somehow the

**[00:20:08]** user guidance in the various places, whether you're using a

**[00:20:12]** desktop version or a web version, doesn't matter. That's

**[00:20:17]** not really helpful, where they say, here for more complex tasks or

**[00:20:21]** for everyday complex tasks or for sometimes important tasks,

**[00:20:26]** better take this model, because it's all so hard to judge.

**[00:20:29]** Do you have any rule of thumb for which model you take for what?

**[00:20:33]** Well, it's not suitable for copying. The rule of thumb is,

**[00:20:39]** until the warning comes that the limit will soon be reached, the biggest one, and after that

**[00:20:43]** think a bit about the last days of the week, so you don't run into the weekly limit,

**[00:20:47]** and then take something so you somehow scrape through, because

**[00:20:52]** Fable, for example, uses much larger quotas at Anthropic, though I don't like using Fable

**[00:20:59]** all that much. So first, you always have to watch what you use Fable for,

**[00:21:03]** because they have this 30-day data retention, tongue twister. And the second thing is Opus

**[00:21:10]** actually does better and cheaper in some areas than

**[00:21:16]** so from that side I'm more of an Opus 5 friend at the moment, and this thing you said, how

**[00:21:22]** do I deal with all this stuff? Yeah, it's, it's, it's terrible, right? Because the models used to

**[00:21:26]** be called 01, 03, 02, they couldn't call themselves that because of naming rights, right? Then

**[00:21:31]** Minimax and Pro and whatnot, right? And today Luna and Terra come along and you think,

**[00:21:38]** well, excuse me, right? What kind of names are those? You have to get used to

**[00:21:45]** something new with every generation. Now Opus and Sonnet certainly aren't

**[00:21:48]** any better, but at least they have a version number on the end. And there isn't

**[00:21:53]** an extra-blue flavor on top of that, although there is the flavor

**[00:21:56]** ultra code and Max and Ultramax and who knows what, it really does your head in, you

**[00:22:02]** can't really expect that of anyone. But something I found quite funny in the same

**[00:22:06]** breath, maybe you remember, looking back at the last

**[00:22:10]** season, when we were still out with the old covers, we had this topic once,

**[00:22:15]** are the models actually going to keep getting stronger and bigger, or is it going to be a bit

**[00:22:20]** like the human body, along the lines of lots of sensors and lots of subtle sub-nodes that

**[00:22:26]** somehow decide or take decisions off your hands, because otherwise the brain, like the

**[00:22:31]** brain of the human body, would be overloaded, maybe you can also handle the reflex of

**[00:22:35]** flinching away from a hot stove completely differently than having the brain think about it

**[00:22:40]** first. So breaking it out into smaller models. And I found that really funny. I

**[00:22:45]** stumbled across a project. A repository that basically offers you an open model and open

**[00:22:51]** weights for a language model that has just under 30 million parameters, just below, runs

**[00:23:00]** completely offline and, get this, on an 8-dollar microcontroller, an ESP32, people who know about

**[00:23:07]** this stuff will certainly be able to say more about it, that basically, you could say

**[00:23:10]** these things could be used in smart home settings, in smaller technologies

**[00:23:16]** that you build in and put up at home, and that you now have the option,

**[00:23:21]** as a manufacturer, on such a small chip, it costs 8 dollars, it has something like 512 kilowatts

**[00:23:26]** of RAM or eight-something RAM, something like that. Doesn't matter, you get what I'm driving at. You have a small chip that costs almost nothing and on it you can now run a local model, and I'm curious to see what effect that will have, now that we're also able to run models on hardware that cheap.

**[00:23:46]** Where I want to go with this, we'll see, then people can read what I've cut together in such a muddle here, exactly, we can do that in the new season.

**[00:23:55]** I wanted to say season too, because that's the first time I'm using this word for what we achieved last year, a whole season shot and recorded.

**[00:24:05]** Yes, I find locally installed models that can work in small hardware gadgets

**[00:24:14]** really exciting.

**[00:24:15]** I think that's one of those things where I'd say some really cool applications will

**[00:24:19]** come out of it.

**[00:24:20]** Because that might also change the way we currently learn

**[00:24:26]** to interact with the product.

**[00:24:29]** There was this hype around AI devices two or three years ago, and it all got a bit

**[00:24:33]** quieter.

**[00:24:34]** that these AI wearables were basically out there briefly,

**[00:24:38]** companies were hyped up, not much has happened there yet,

**[00:24:41]** but it's going to come now, because of course it's hugely advantageous

**[00:24:44]** if I can run things locally,

**[00:24:46]** I need to build in less technology, it doesn't necessarily have to be internet-connected,

**[00:24:49]** but it can help me enormously.

**[00:24:51]** I can already see things like, well, there always used to be survival manuals

**[00:24:56]** that you needed when you were out camping,

**[00:24:58]** these days you can put all of that locally onto an off-grid device

**[00:25:01]** and not just have to read through or search a long PDF version, but

**[00:25:05]** have it as an LLM that, in an emergency, if you have the bad luck, whatever,

**[00:25:11]** to break your leg while mountaineering, can then explain to you how to

**[00:25:14]** rig up a splint yourself, how to lash the sticks together with your laces

**[00:25:19]** and build a pressure bandage out of it, so you can get back down the mountain.

**[00:25:25]** You don't know my laces, they'd have to hold, don't worry, Tim, I'm

**[00:25:29]** not going to do that.

**[00:25:30]** Yes, but I think that's yet another thing entirely. I think there's more to it as well.

**[00:25:34]** A new feature came out from OpenAI in Codex too. It's called record and replay?

**[00:25:38]** It's that kind of thing. I can basically record videos of myself, of my screen, now.

**[00:25:45]** I can then throw that into Codex afterwards and Codex makes a Skill out of it. So I just show it how I basically do it.

**[00:25:52]** Yes, you want to say something, go right ahead. I want to say something about that in a moment. I was totally impressed by this feature at first.

**[00:25:59]** I thought, how cool is that?

**[00:26:02]** And then I, well, we build our own harness at the company too, and then

**[00:26:07]** it took about two hours and then it could do that too.

**[00:26:10]** Yes, that's good.

**[00:26:11]** It's just funny.

**[00:26:12]** I have to share this now, it doesn't really have anything to do with the topic, but I'm

**[00:26:16]** just so excited about it.

**[00:26:17]** So I had a look at the thing, I can well imagine that if you use something like that

**[00:26:22]** in a work context, then there could be people who

**[00:26:25]** don't like the way OpenAI and Anthropic built it, because the thing wants to read along with your keyboard,

**[00:26:29]** the thing wants to read along with your screen, are you sure it really only

**[00:26:34]** reads along when you want it to, and so on, there's a bit of a lack of consent

**[00:26:38]** and that kind of stuff.

**[00:26:39]** And so I just sat down and thought, let's see what the model

**[00:26:42]** actually does.

**[00:26:43]** So with us, in our harness, what the model does when you only give it the video,

**[00:26:47]** just the screen video, and specifically a screen video where you're doing something, so for

**[00:26:54]** example operating a website, operating an internal website, and simply

**[00:26:57]** explaining what you're doing while you operate it, and so I talked along, saying, right,

**[00:27:01]** here's an input field, and always marked with the mouse what I was talking

**[00:27:05]** about, like, here's an input field and I don't need this one and here

**[00:27:09]** are the answers and here you can see whether there was an error, and basically

**[00:27:13]** worked through the thing with this video and then fed this

**[00:27:16]** video in and told it, make a Skill out of this, and you know what,

**[00:27:20]** the thing goes and makes itself a Skill, it broke the video apart, it can then look

**[00:27:26]** at, along the lines of, how often does something change in the video, takes out everything where possibly

**[00:27:31]** nothing happened at all, because you didn't move the mouse, because the website was busy thinking

**[00:27:35]** or whatever, so it only took the remaining frames, built itself a Skill out of the

**[00:27:39]** remaining frames, put the images into the Skill as orientation patterns

**[00:27:45]** and then moved on and said, right, okay, I've learned it from

**[00:27:49]** you, you want to go to this website and here are the things you need. Here are the things

**[00:27:53]** you ask. It asked me a few follow-up questions. Long story short. It then used

**[00:27:58]** Playwright, that's a library that basically does a kind of browser operation, except that

**[00:28:05]** you can run Playwright headless, so without a visible browser interface. And then

**[00:28:11]** the thing basically goes and works through the Skill, operates this website with it, and whenever

**[00:28:15]** it doesn't know how to go on, because the website maybe looks different, because somehow

**[00:28:19]** whatever, it just wants to orient itself again, it basically looks again at

**[00:28:23]** these screenshots it saved for itself, together with the Skill, and operates it.

**[00:28:26]** And long story short, you can go and say, for example,

**[00:28:31]** all right, you have lots of different RAG systems. I think we'll be talking about RAG

**[00:28:35]** next time with Cornelius, that much promo is allowed.

**[00:28:38]** Is it then basically able to package the whole lot into a Skill,

**[00:28:43]** in your agent harness. For any other listener that would be Claude or the Codex app. With us it's

**[00:28:50]** our own, our own harness that we built. You can then basically replay it.

**[00:28:55]** And that's how you can connect other systems to your harness, purely through a Skill it

**[00:29:04]** learned on the basis of videos, audio tracks and the possible things to control. And last

**[00:29:10]** I always wonder then, why did Anthropic, or Codex, build so much stuff around it,

**[00:29:15]** so that you have to hand over so many permissions, when actually a video is enough,

**[00:29:20]** one you record, or a training video you maybe find somewhere in a learning

**[00:29:24]** program, and you say, here you go, take a look, you'll figure out the rest.

**[00:29:27]** Have fun, fire at will. The power of it is unbelievable.

**[00:29:30]** Yes, that's true. That's exactly what I mean. That's what I mean when we say,

**[00:29:34]** We will basically, whether that's on locally installed

**[00:29:39]** hardware gadgets, videos, voice, audio.

**[00:29:42]** Imagine that what you're describing right now

**[00:29:44]** is basically a matter that happens on a screen,

**[00:29:48]** where I work through things and a Skill can be built from it.

**[00:29:51]** It's often the case that production isn't the hard part any more.

**[00:29:55]** It wasn't the hard part even before AI these days.

**[00:29:58]** We already had good people before who could do design,

**[00:30:01]** who could code well. It's often the case that this path from the actual idea,

**[00:30:06]** the translation, what actually is the real problem in that moment, that we have to

**[00:30:11]** recognize where we have to put work in, analyzing workflows, situations, hospitals,

**[00:30:16]** airports, whatever, to see how you can improve these

**[00:30:20]** processes. All of that is what happens in the real world, and then afterwards

**[00:30:25]** possibly leads to a piece of code and to an application or something that

**[00:30:28]** improves part of that workflow. If we can capture that considerably better

**[00:30:33]** in the future and more interactively, without me having to, and I'm now a

**[00:30:38]** big fan of this, if we switch to formats like that, because then I don't even

**[00:30:42]** need to know the concept of a programming language at all. So if we just talked about

**[00:30:48]** English being the new programming language, then approaches like the ones we're seeing

**[00:30:51]** right now are of course also the replacement for having to understand this

**[00:30:56]** abstraction level at all. I no longer have to understand that a Skill possibly

**[00:31:02]** needs a text file to describe how the Skill should behave, and additionally

**[00:31:06]** needs further documents as templates so it knows which output format it should

**[00:31:11]** produce, or some connection to MCPs. But no, the machine can simply see

**[00:31:15]** what we do and derive from it what might be a good solution that could generate a

**[00:31:22]** similar output to what it saw there.

**[00:31:24]** And that is actually one, well, I think that's one of the conditions we'll be

**[00:31:31]** seeing much, much more of in the coming weeks and months.

**[00:31:35]** That we see there are other options besides pure text input.

**[00:31:40]** So every one of us has probably taken the photo of the wine shelf at Rewe

**[00:31:45]** or at Wiedel or wherever and checked, let's ask ChatGPT which wine to take,

**[00:31:49]** or photographed the fridge to get the recipes that are still possible

**[00:31:54]** with the leftovers going moldy in the fridge. But that was a live glimpse into the

**[00:32:00]** Scharnetzki household. No, I don't think so at all. We're extremely well stocked, yes, and

**[00:32:05]** nothing ever gets thrown away at ours. Yeah, all good. No, joking aside,

**[00:32:10]** but the thing is, I know, the thing is that we really actually now,

**[00:32:17]** Well, we were multimodal, the AIs have been able to do that for a while now, I've been able to give it videos for a while,

**[00:32:24]** been able to upload images to it for a while, or text or video or whatever, so I could hand over a lot of things.

**[00:32:30]** But now we're entering this phase where it's not just about, okay, there's knowledge in there, but I can also use it for action, exactly as you just described.

**[00:32:40]** And when we enter this phase, then of course it gets even more exciting, when we give AI eyes in the real world.

**[00:32:46]** Exactly. And it picks up even more of what's happening. There'll be a huge amount there, I think, where this year, in our new season, in season 2 of Think Different, Think AI, there's certainly an episode or two to be made.

**[00:32:58]** We were originally on the open models. I think we covered that well too. Something I also want to say about your thought while you were talking, all of a sudden things like little YouTube clips become quite interesting too.

**[00:33:14]** because let's say, I now have, why I have it is another topic, for example also

**[00:33:20]** privately, Apple Business Manager, that's a solution from Apple where these days you can manage devices

**[00:33:25]** not too badly. But where you simply have to get to grips with a few portals from Apple, let's put it that way.

**[00:33:31]** And the funny thing, I absolutely have to try this out, just imagine, there are all these little YouTube clips

**[00:33:37]** where some influencer or Apple itself talks about things, and you give it that, and then all of a sudden you have the option

**[00:33:42]** that your AI system operates this portal for you and thereby maybe makes it much more accessible

**[00:33:49]** than you managed by hand up until two weeks ago. So from that angle I think we should

**[00:33:57]** definitely do episodes soon about the possibilities of the new harnesses and the new systems, not just the new

**[00:34:02]** models. And maybe also with a critical

**[00:34:08]** perspective, and I already have a guest in mind who knows a great deal about this whole

**[00:34:13]** topic of VR and augmented reality glasses. We could interview him about it too, because

**[00:34:20]** of course there's the negative side as well. So if we, it's like Pandora's

**[00:34:24]** box, of course a lot of people are interested in this data too, to make the models

**[00:34:28]** better or to do other things with it. And if now, of course, everyone,

**[00:34:33]** because there's an advantage in maybe being able to record something constantly with my glasses,

**[00:34:37]** being able to optimize workflows that way, then of course the question of data

**[00:34:43]** protection comes up in the background. What am I actually recording, where is this data stored and

**[00:34:47]** is it being trained on. So if we do want to do that, then in the usual way we should

**[00:34:52]** shed light on both sides of the coin again and discuss them. And I'd be

**[00:34:57]** glad to, because I've been meaning to with the colleague anyway, we need to set a date now, to do an episode

**[00:35:01]** on the topic. We can record that at the same time. I was just, while

**[00:35:05]** And you, quite rightly, you said two sides of the coin, there's still the coin of

**[00:35:10]** filthy lucre, and I was just wondering whether you could train a Skill, simply with a whole lot of

**[00:35:15]** little YouTube clips, whether you could sell a kind of Skill library with real added value

**[00:35:19]** for people. But since we said we're in a new season,

**[00:35:25]** the segment "making money with AI" is probably not what we'll start with anyway,

**[00:35:30]** but I'm very much looking forward to an episode with a guest. I'm also very glad that

**[00:35:35]** we have an episode with a guest next week, yes, I've already mentioned Cornelius. It'll be about

**[00:35:39]** Second Brain and that kind of thing, yes, stay tuned. And I'd say, Jens, let's quickly

**[00:35:45]** wrap up before a new model comes out and makes everything we've discussed so far

**[00:35:50]** moot. Thanks for taking the time. I'm glad we're going into this

**[00:35:55]** new season together, and do leave us a comment. How you like our new

**[00:35:59]** cover, and with that we say see you soon at Think Different, Think AI. We look forward to you. Bye.

**[00:36:06]** Ciao.

**[00:36:09]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:36:14]** Two technology-loving minds who don't just talk about artificial intelligence, they live it.

**[00:36:21]** Here you get clear perspective, real hands-on insight and a fresh look at what's possible.

**[00:36:27]** Understandable, critical and always with a wink.

**[00:36:31]** AI to think about, to smile about and above all to talk about.
