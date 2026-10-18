---
title: "Wissensraum"
episode_index: 62
published: "Sun, 18 Oct 2026 08:57:40 +0000"
duration: "4864"
page_url: "https://think-ai.podigee.io/62-new-episode"
image_url: "https://images.podigee-cdn.net/0x,sjmFsm-v_dUnwrU5KyOdwW93laYNgw1IMrMqp_mXACqY=/https://main.podigee-cdn.net/uploads/u73317/e2719f1c-086b-4ecf-bed4-c92f86eb0a52.png"
audio_url: "https://audio.podigee-cdn.net/2615056-m-46dc5d51a89aecb59a7ea4d29ef32216.mp3?source=feed"
guid: "56b89471c65ae640fbec7027c5061ea6"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-10-18T18:07:40+00:00"
translated_from_language: "de"
translation_provider: "claude"
translation_model: "claude-haiku-5-5"
translated_from_file: "transkripte/062 - Wissensraum.md"
translated_at: "2026-10-18T18:16:40+00:00"
---


# Wissensraum

**Published:** Sun, 18 Oct 2026 08:57:40 +0000
**Duration:** 4864
**Web player:** https://think-ai.podigee.io/62-new-episode
**Cover:** https://images.podigee-cdn.net/0x,sjmFsm-v_dUnwrU5KyOdwW93laYNgw1IMrMqp_mXACqY=/https://main.podigee-cdn.net/uploads/u73317/e2719f1c-086b-4ecf-bed4-c92f86eb0a52.png
**Audio:** https://audio.podigee-cdn.net/2615056-m-46dc5d51a89aecb59a7ea4d29ef32216.mp3?source=feed

## Description

From the inbox folder to shared memory: storing knowledge so that AI can work with it
Alexander Heusingfeld is back as a guest, this time without Jens. The question at hand is one the two of them have been passing back and forth in voice messages for weeks: how do you build a knowledge space that an AI system can really work with? The starting point is simple. What an agent achieves depends not only on the model and the harness, but on the context you give it. With good context, a casually spoken prompt is enough. Without it, even a long one accomplishes little.

Before getting to tools, it's about data. Alex has the new agent offerings from OpenAI and Meta's assistant Muse in view and asks whether people realize what happens to their entire life, health data included. There are plenty of examples of the power of linked data, such as movement patterns from location data that show where someone works and sleeps. Mark sees the biggest risk in companies as a new kind of shadow IT: sentences and documents end up in AI systems whose data processing agreements nobody has settled. Then a story from private life. Someone who uploads their pet's insurance contract for analysis may, in the unlucky case, be shown a passage from a stranger's dental insurance contract, complete with name and contract number.

Mark's alternative to the built-in memory features of the big apps starts with chaos: a folder called Inbox, holding emails, chat messages, PowerPoints and transcripts. A skill converts this into Markdown, builds a wiki with a knowledge graph from it, and adds a file that defines how the system should answer: with a source or without, with the internet or without. That is how SkillSafe came about. The knowledge ends up in a directory that runs offline and anywhere an agent can read skills. Alex highlights what many RAG systems cannot do: qualify the relationships between nodes. Whether someone is a partner, a child or a colleague, we know from everyday life. In a knowledge graph, it first has to be spelled out.

Then it gets practical. Mark packed two matters with a combined 28 GB of payload data into one SkillSafe each and had the system look for the differences. He turned the talks from Apple's developer conference into a skill and sent an agent through his own projects in Azure DevOps with it. The result was a list of what is outdated and where new features are an opportunity. Alex brings in the layers: organization, area, team, person. And versioning, familiar from everyday life without anyone calling it that. Grandma isn't coming on Thursday after all but on Wednesday, and everyone should have the current state.

Two more building blocks come in. ContextMe doesn't determine knowledge but relevance: once a day, it looks at mails, Teams messages and projects to see what currently occupies Mark, professionally and privately. An app Mark is building, which is currently in review, uses this. It collects screenshots, breaks them down with a local model into text, dates, links and QR codes, and only notifies him about what matters. His daughter's riding tournament needs no push notification. An interesting Git repo perhaps does.

The last big block concerns collaboration. The SkillSafe workshop keeps knowledge alive rather than frozen, and so it has to answer questions that a single skill never faces: Does only the new information apply, or the old too? Who checks that everything is still consistent? What happens when two agents write at the same time? Alex works with colleagues through a shared OneDrive folder. From imported meeting transcripts, the workshop found contradictory decisions, asked for votes, created a template for decision records and pulled tasks over from Jira. Much of this was not built in at all.

Finally, about getting started. Mark describes how, after a weekend, he had a usable solution while others had spent months on concepts. Alex, by his own account a chronic overthinker, argues for a protected framework in which the worst case is that little happens, and for small experiments. His tip: the command-line tools of Claude and Codex can now see each other's sessions. If you're stuck, open a new window and get help there.

—
Think Different. Think AI. with Mark Zimmermann and Jens Scharnetzki.

Listen: Apple, Spotify, YouTube, RSS
https://think-ai.podigee.io

New episodes first in the WhatsApp channel
https://whatsapp.com/channel/0029VbDJ4ZlGufIrpquad004

If this episode was useful to you: rate us once on Apple. That decides whether new people find us.
https://podcasts.apple.com/de/podcast/think-different-think-ai/id1828021699

Feedback and guests: via the show page.

## Transcript


**[00:00:00]** Welcome to Think Different. Think AI., the podcast by Mark and Jens.

**[00:00:07]** Two tech-loving minds who don't just talk about artificial intelligence, but live it.

**[00:00:14]** Here you get clear classifications, real practical insights and a fresh look at what's possible.

**[00:00:20]** Down to earth, critical, and always with a wink.

**[00:00:24]** Something to think about, to smile about, and above all to join in on.

**[00:00:29]** Welcome to Think Different, Think AI.

**[00:00:36]** Actually, I wanted to start completely differently.

**[00:00:39]** I wanted to start with "Think different, Think Alex."

**[00:00:42]** And welcome our guest right away.

**[00:00:45]** Sometimes introduced as a camera kid, sometimes as co-host,

**[00:00:49]** sometimes together with other people,

**[00:00:52]** but still happy to be our guest on his own, again and again.

**[00:00:56]** Today we talk about a lot when it comes to knowledge.

**[00:00:59]** And when we talk about knowledge and brains and such,

**[00:01:03]** Alex, as I said, can't be far away.

**[00:01:05]** Alex, great that you're here.

**[00:01:08]** Thanks for the invitation, and for having me back.

**[00:01:11]** Apparently the comments on the last podcast weren't that bad,

**[00:01:15]** even though we talked for an hour and twenty or so.

**[00:01:18]** Yes, maybe it wasn't that bad.

**[00:01:20]** Maybe the people who listened to it

**[00:01:23]** fell into some kind of waking coma

**[00:01:25]** and couldn't even write that it was too long, or people listen to it

**[00:01:31]** in stages.

**[00:01:32]** Or as a sleep aid.

**[00:01:33]** Yes, as a sleep aid.

**[00:01:34]** We talked earlier about all kinds of aids, and I said it sounds like a compression stocking.

**[00:01:40]** At this point, maybe some self-promotion: I'm building a podcast app

**[00:01:44]** that doesn't play whole podcasts anymore. Instead, you say which topics

**[00:01:49]** interest you, and it checks which episodes or seasons

**[00:01:54]** or special episodes covered the topic, then pulls the passages out of the transcription and chapter marks

**[00:02:00]** and builds a new podcast out of them, perhaps one that's just about Jev, for instance.

**[00:02:05]** That's really funny: one day you think you'd like something like that,

**[00:02:14]** and a day later Claude has hacked it together for you.

**[00:02:19]** In software development you upload to Apple so often, because you want to test it on

**[00:02:25]** TestFlight, that at some point TestFlight sends you the message

**[00:02:30]** that you've made too many uploads and are now blocked for 24 hours. I've learned a lot

**[00:02:34]** with this project. But today we don't want to talk about podcast projects

**[00:02:38]** on the podcast. That would be something like a Möbius strip or so. No idea,

**[00:02:43]** I don't know much about that, sorry to all the mathematicians and so on.

**[00:02:46]** Wrong podcast, we're talking about AI here, and about focus, Alex.

**[00:02:51]** That's interesting, because my hobby app is basically, I'm having Codex right now

**[00:02:59]** build something that a very respected colleague we both know recommended to me,

**[00:03:04]** namely a focus tool.

**[00:03:06]** It asks: what's your context right now, for the next 25 minutes or for the appointment,

**[00:03:13]** and what do you need for it?

**[00:03:15]** Hide everything first. I don't know if you know this, with 570 tasks and 73 tabs open,

**[00:03:24]** what do I need right now for the next topic, to get through the next topic. That's

**[00:03:31]** a bit of a theme, I think, that you mentioned to me in our pre-chat, under the keyword

**[00:03:36]** complexity of knowledge work. I'd like to digress briefly, as is customary.

**[00:03:43]** So when you said focus and app, and that you should keep your focus,

**[00:03:51]** for whatever reason I had to think of Die Hard with Bruce Willis,

**[00:03:57]** where he has a sign around his neck, and I briefly imagined him having "Focus" written on it,

**[00:04:02]** but that wasn't the case, and I don't want to repeat

**[00:04:05]** what was on the sign. I'm pretty sure otherwise I'd get some kind of

**[00:04:08]** letters. We're still too early in the episode for that. You know, we're still

**[00:04:12]** much too early, because we haven't lost that many listeners yet. We've come together today

**[00:04:17]** here because we have a topic that keeps coming up for us, either in

**[00:04:24]** our little one-message exchanges or in the discreet voice notes

**[00:04:28]** that I sometimes send, longer than my newsletters,

**[00:04:33]** which I write, but that's another topic too. We have to make longer podcast episodes,

**[00:04:39]** so your voice notes can get longer accordingly.

**[00:04:42]** Oh, I see.

**[00:04:43]** My problem is always that I want to refer back to something you said at minute 8:16,

**[00:04:50]** that's the thing.

**[00:04:52]** Yes, maybe you should build an app for that, some kind of commenting feature for voice notes.

**[00:04:59]** We could call it "Einmessage" in the... wait.

**[00:05:01]** Yes, I think that name is already protected.

**[00:05:04]** Greetings go out to Annette.

**[00:05:06]** The whole topic of Second Brain, how do you build one? This came up for me as well

**[00:05:12]** not in preparation for this episode, but through a conversation today,

**[00:05:17]** which I had with my boss, who also raised with me, this

**[00:05:22]** "T-Motor": whether we could take another look at how to

**[00:05:25]** set that up nicely. And I have one or two GitHub projects,

**[00:05:30]** so that the self-promotion is completely finished and hopefully wrapped up.

**[00:05:33]** I don't think so, we still talk about it quite a lot.

**[00:05:37]** Well, we'll see. But then you may talk a bit too. You know, when you talk about it yourself it's a bit tricky.

**[00:05:43]** Because I think we probably agree this far: when you talk to AI systems, what differs is not only the model or the harness you use it in, but, mind you, the context you give the system.

**[00:06:00]** So that even with a casually spoken prompt it delivers a much better result,

**[00:06:08]** than someone else, who is missing a lot of context around it, but maybe

**[00:06:13]** so the prompt was long, and that's why we wanted to talk about Second Brains today.

**[00:06:17]** Right, let's talk about it.

**[00:06:18]** Exactly. And I'll claim that neither of us is an absolute expert in information management.

**[00:06:27]** We've simply tried out a lot, and I've already said that I

**[00:06:33]** don't know whether it's a kind of paranoia, but when I look at presentations like

**[00:06:39]** yesterday's from OpenAI's dots, for example, I ask myself, do people actually see

**[00:06:47]** what happens to their data there? I mean, Cambridge Analytica was an eye-opener,

**[00:06:53]** we know Meta probably does a few things with the data, and whether you'd then want Meta's

**[00:06:59]** personal assistant Muse to entrust your entire life to, including health data,

**[00:07:07]** and who knows what else. Everyone decides for themselves. But it would also be quite

**[00:07:13]** interesting to understand what that actually means. What parts does it consist of, and

**[00:07:19]** what alternatives do I actually have. And as you said, you've built something like

**[00:07:25]** SkillSafe, you have the SkillSafe workshop, you've built a Knowledge Distiller that

**[00:07:30]** can ultimately build a knowledge graph, and you've built ContextMe, and last week

**[00:07:37]** you also talked about Jev. So there are loads of building blocks, and I understand

**[00:07:46]** completely why people say, okay, on the one hand I've got all these building blocks,

**[00:07:51]** and on the other side I've got my personal knowledge, oh wait, that's not even

**[00:08:01]** personal, because I have topics that are more private,

**[00:08:06]** friends, family, hobbies, whatever, and work. With work I'm bound by contracts

**[00:08:13]** and compliance, whatever. So I'd have to make sure the data and the tasks,

**[00:08:18]** responsibilities and goals I have are organized in such a way that it

**[00:08:23]** complies with the company. On the other hand, it would also be good if I didn't forget

**[00:08:28]** the kids' dentist appointments. So, you've laid that out nicely.

**[00:08:34]** Thanks. Well, maybe not wrong, and the question is simply: how do you not get lost in

**[00:08:43]** it all. It feels like everything around us gets more complicated, and there are more and more variables,

**[00:08:49]** and I completely understand that a lot of people say, no, really not. Oh,

**[00:08:55]** OpenAI's dots, yes, yes, let's do it. So before we really get into the topic,

**[00:09:02]** and maybe you could, I mean, we're an audio podcast, but it might help us

**[00:09:07]** with structure if you bring up that nice little diagram again,

**[00:09:11]** so we can move along it, how you do this with knowledge

**[00:09:15]** work. But while you're looking for the document for the old white man, on your side

**[00:09:20]** of the monitor, I wanted to say something more about the dots. Basically, I found

**[00:09:25]** the dots cool, the whole idea that the agent doesn't just work on your

**[00:09:31]** computer, the agent has its own environment, the agent has a way to keep working

**[00:09:37]** even when I've closed my laptop, or to build its own tools. But I found

**[00:09:44]** a few things there really efficient. One is that they said

**[00:09:48]** there's a collaboration space, and you can use it together in teams and so on,

**[00:09:53]** but you can also let them talk to each other. I briefly wondered

**[00:09:58]** whether the fine print says you can stay at home, yes, the dots

**[00:10:02]** will sort it out among themselves. And the other thing is, all the data you give, now, I think it's

**[00:10:09]** of course understandable that the more data systems have, the better they can

**[00:10:15]** answer. And you also have the case, back then it was still called Facebook, I think,

**[00:10:20]** Meta, the renaming, which came later. The power that lies in your data also surprises

**[00:10:31]** me quite regularly, what conclusions you can draw when you connect a lot of

**[00:10:38]** things together. And that's a bit of what this whole thing is about,

**[00:10:44]** what we want to discuss in this episode. Another good case for why data

**[00:10:50]** might be worth protecting: greetings to Flübcke, a VW data scandal involving the

**[00:10:56]** geodata. You can also derive movement patterns from location data. Where

**[00:11:03]** does that person probably work? Where do they sleep? During the day, though, they're often in the

**[00:11:11]** forest, what's in that forest? Well, if it were only the forest. Yes, yes, exactly. And so

**[00:11:19]** from my point of view it should prompt some thought, to say, okay, everything I do somewhere,

**[00:11:26]** do, say, can and will be used against me in court. No, just kidding.

**[00:11:34]** But the question is, how do you

**[00:11:39]** how do you, I like this phrasing,

**[00:11:43]** about the data, but how do you manage to keep track of what actually

**[00:11:49]** goes where? Well, I can at least speak for myself, in a company context this is

**[00:11:56]** already expected, that you know what you're doing and how you handle the data

**[00:12:00]** responsibly. Some people are even paid for it. I'm not, but are you

**[00:12:07]** simply a natural talent? Now you should talk to them about a salary negotiation.

**[00:12:11]** I think at that point, regardless of which tools you've been cleared to use in a

**[00:12:19]** company, the biggest risk alone is what's developing in companies,

**[00:12:25]** what we used to call shadow IT, which I think becomes much, much more critical with AI.

**[00:12:34]** Because I don't want to play it down, yes, to all the colleagues listening who'll say, well, he didn't really say that.

**[00:12:41]** But if you've typed something into a Google window, nothing against Google, but you may have entered a sentence there,

**[00:12:50]** triggered a search, and then, well, that's that.

**[00:12:52]** So when you enter sentences into AI systems today whose data processing agreement you haven't settled,

**[00:13:01]** where you think, come on, it's not that bad, just throw the sentence in, you mustn't forget,

**[00:13:08]** the more people do it, the more it adds up, right?

**[00:13:12]** So you're handing out units of a certain IP range just by uploading documents into systems,

**[00:13:20]** how quickly it's able to put together not just a nice answer from a document,

**[00:13:24]** a nice picture, a little video, a short summary, and we don't really

**[00:13:31]** know what becomes of it. From my private life I had a case recently,

**[00:13:36]** where I had to look something up, or wanted to, whether the vet's

**[00:13:43]** insurance for our dog had an update on a certain matter. And then I couldn't

**[00:13:51]** find it, so I took all the papers, put them into a scanner app,

**[00:13:55]** a fast duplex scanner, uploaded the PDF to ChatGPT, and said,

**[00:14:00]** come on, do it. For my dog's contract data I didn't think that was so bad.

**[00:14:05]** Unless somebody calls to say the dog has data protection rights too,

**[00:14:10]** dogs still count as property, I think, but I don't want to debate that.

**[00:14:14]** Then I uploaded it, and ChatGPT came back and said, yes, there it is.

**[00:14:18]** So I'm blind now, I can see that, I know it, but it's not on page 2.

**[00:14:25]** And ChatGPT said, yes, it's on page 2.

**[00:14:27]** Okay, please show me the text excerpt.

**[00:14:29]** But not from the document.

**[00:14:31]** Wait, here it comes, yes, I don't see that.

**[00:14:34]** And then it offers me: shall I show you the document with the highlighted passage?

**[00:14:38]** And then there was a health insurance contract,

**[00:14:43]** not for the dog,

**[00:14:45]** but with name and contract number.

**[00:14:49]** And then you stand there and think,

**[00:14:51]** where on earth did it get that from, you ask.

**[00:14:55]** And then it says, let's sing it too:

**[00:14:57]** that should never have happened.

**[00:14:58]** And then you think, well, firstly, right,

**[00:15:02]** so a lot failed there, right.

**[00:15:05]** Firstly, right, that's what showed it to me.

**[00:15:06]** Secondly, where did it come from? Not from old books they shred to scan,

**[00:15:11]** it can't have come from that. And it was even from the same insurer. So

**[00:15:20]** they were also the right ones, because there are companies with certain color values,

**[00:15:24]** that recognize documents when they reach you in their postal state,

**[00:15:30]** you know them. And it all matched, but it was

**[00:15:34]** not a dog. The person wasn't called Hund either. But it was about teeth. Well, at least that. And

**[00:15:45]** probably he wanted insurance too, if you know someone. And probably

**[00:15:50]** he didn't want me looking at it on my computer. I'll assume that for now.

**[00:15:54]** And from that side it's a big deal, if you potentially

**[00:16:01]** upload something like that. Regardless of whether you're allowed to or not, the whole point is, when

**[00:16:07]** data is made available to an AI, it's a curse and a blessing. It can

**[00:16:13]** be very powerful and also very risky.

**[00:16:16]** In a company context we now have the option to say, we use, for

**[00:16:23]** example, one of the big hyperscalers, who say, well, we guarantee that

**[00:16:30]** the models are hosted with us and don't leave any EU country. They have a

**[00:16:37]** redundancy, no idea, Stockholm, Paris, Frankfurt, and it stays there. Unless you

**[00:16:46]** at certain times used Fable, or they at least guarantee it. There are also

**[00:16:50]** some who guarantee it contractually, but those things still sit somewhere

**[00:16:54]** overseas, which is funny too. Those exist as well, and I think that's great.

**[00:16:58]** Good, but let's say, in theory it's all fine, but you lose

**[00:17:05]** convenience, because with the standard thing, oh yes, I have a

**[00:17:14]** ChatGPT app and a memory gets created there. In that moment I

**[00:17:19]** simply don't have that anymore. On the other hand, personally I see it as an advantage, because

**[00:17:26]** with a memory, yes, what if we, for example, work on a topic together and we both on

**[00:17:36]** this, let's not call it memory, but maybe a knowledge trail or knowledge

**[00:17:42]** trace, and we both contribute to it? That's a use case that, from my point of view,

**[00:17:49]** the standard systems don't support? Well. Let me put it bluntly.

**[00:17:55]** The standard systems are very strongly oriented toward individuals,

**[00:18:01]** commodity-oriented, and the whole question of what requirements a company like that has,

**[00:18:06]** what requirements teams of two or more people have,

**[00:18:12]** what requirements you have? Even requirements in a family context.

**[00:18:17]** Along the lines of, I share, I'd offer something like family accounts and maybe also say what counts as family knowledge or not. They haven't got there yet.

**[00:18:27]** At the moment the race is faster, higher, further, give me your data. Today a model comes out so that tomorrow the next model comes out.

**[00:18:35]** But this topic of collaboration, I think, is still in its infancy.

**[00:18:42]** Exactly, I see it gradually coming, that once you have a team account, at some point you can say, okay,

**[00:18:48]** for this entire team of 200 people,

**[00:18:54]** for this whole team you can then

**[00:18:57]** define a shared memory, but we wanted to talk about alternatives.

**[00:19:02]** So I'd suggest we dive into this use case and say,

**[00:19:07]** okay, personal memory is fine.

**[00:19:10]** Can we briefly say how we're doing it right now, because we both use, I think,

**[00:19:17]** the ContextMe plug-in, right? I like that we both use

**[00:19:22]** the ContextMe plug-in, so maybe just as a... So we're not using the same thing,

**[00:19:26]** we're using... I've installed it and you've installed it, but...

**[00:19:29]** Hold on a second, I have to switch off yours, it always gets transferred to me, trust

**[00:19:33]** the skill you've loaded. Always check which one you're using,

**[00:19:38]** That's also funny, because depending on that, there was a nice security scan

**[00:19:43]** recently, where people said that some skills hide things,

**[00:19:47]** where they might call up a website.

**[00:19:50]** In MCP servers.

**[00:19:52]** Pretty funny.

**[00:19:53]** How many people do you know who look at the installers for such a skill?

**[00:19:58]** I mean, when you copy and paste, they usually have on their websites

**[00:20:06]** Yes, you just copy this command and paste it into your terminal command line.

**[00:20:12]** And every time it's some bash thing, run this shell script, and I think,

**[00:20:20]** okay, should I maybe download it first and check what gets executed?

**[00:20:24]** Oh, come on.

**[00:20:27]** Ah, it'll be fine.

**[00:20:32]** Exactly, nothing has ever happened.

**[00:20:36]** No, let's stay focused on the use case. Say we both work together in the team now. How would you set that up?

**[00:20:45]** That's a real trick question, if you come with the argument that we both use, let's say, the same technology and at least the same basic origin.

**[00:20:54]** I'd like to get into the topic of when people say, I'm building

**[00:20:58]** a Second Brain, a knowledge space, for themselves or for the team, where then

**[00:21:03]** first comes that entry hurdle: what do I need to watch out for, what do I need to

**[00:21:09]** think about what goes in there.

**[00:21:11]** I'd like to start there first, before we maybe get into collaboration

**[00:21:16]** or the organizational levels.

**[00:21:18]** And at this point, hard to believe, chaos is your best friend.

**[00:21:24]** Because when you grab an inbox and say, I'm throwing in whatever's on my mind,

**[00:21:32]** then at least that's my beginning.

**[00:21:34]** I'll come to context in a moment, in case that helps.

**[00:21:37]** But in the first step, from the history, when I started with SkillSafe,

**[00:21:44]** the best result was that I said, look out.

**[00:21:47]** I've got a whole pile of topics here, process documentation, descriptions, emails, PowerPoints from a project.

**[00:21:56]** Then I created the folder called Inbox, threw things in and built a system that pulls something out of the inbox,

**[00:22:05]** converted to Markdown, because I, old white man that I am, I stand

**[00:22:11]** by it and say Markdown is still, I think, the best format ever for an AI system, and

**[00:22:18]** not HTML. I never jumped on that HTML trip, because there's so much

**[00:22:24]** clutter in it that an AI isn't really interested in, that only humans care about, or

**[00:22:29]** whatever. And then SkillSafe came along and said,

**[00:22:34]** okay, I'll structure it in the Open Knowledge Format from Google, and store it in a kind of LLM wiki, the way we heard about from Karpathy,

**[00:22:44]** so that the skill has a kind of structure, so that the AI system that loads the skill

**[00:22:53]** can consume this knowledge and give me answers based on it.

**[00:22:57]** So at some point I realized, damn it, with what you put in, it's maybe quite funny

**[00:23:03]** to explain to the system what I actually expect when I ask it something. So do I want

**[00:23:08]** a long-winded answer from you, or bullet points, do I want you to

**[00:23:13]** always name the source, do I want you to, if you're unsure,

**[00:23:17]** look things up on the internet or not, and then, alongside the wiki that emerges in the skill,

**[00:23:23]** something like a SOUL.md, so it knows how it should react. So,

**[00:23:29]** if I don't know something, should it fetch something from the internet? Yes, no. Or if I

**[00:23:33]** know something, should it always name the source, in the form of which document I

**[00:23:37]** originally pieced it together from? And how should it cite that? And I found that

**[00:23:41]** pretty cool for a long time, because loyal podcast listeners have noticed it too.

**[00:23:46]** Skills are kind of the big magic of teaching the system to do things repeatably,

**[00:23:51]** and to retrieve knowledge too, repeatability of things. And

**[00:23:58]** and then you stand there, and people like you come around the corner and say, yes,

**[00:24:02]** that's us, when you work with different departments.

**[00:24:06]** That's us, when you work with different people.

**[00:24:09]** And when it came to SkillSafe, I notice I'm already rambling again like an old man with verbal diarrhea,

**[00:24:15]** I thought, okay, damn it, he's not wrong,

**[00:24:19]** because there is, whether it's at home or not,

**[00:24:23]** the motto: family knowledge above all, or someone who, for example, has a company's compliance knowledge

**[00:24:30]** above all, corporate guidelines and whatever else there is, you could

**[00:24:36]** throw a SkillSafe at that, but then it would be nice if such a SkillSafe were aware of

**[00:24:40]** where it's organizationally deployed. Along the lines of, what is

**[00:24:46]** my scope, can my knowledge be overwritten by someone else, or am I

**[00:24:52]** not so overarching that other rules have to subordinate themselves to me. That may

**[00:25:00]** already be in the name with a corporate guideline, but in an AI system that's pretty

**[00:25:04]** irrelevant, what the file is called. Context definitely helps, so the system knows how to sort itself

**[00:25:10]** in, and so SkillSafes got a property. First, you can

**[00:25:15]** address other SkillSafes, that's given to you. Second, another SkillSafe can

**[00:25:20]** have its organizational assignment passed along.

**[00:25:23]** Along the lines of, I'm a personal SkillSafe, I'm a team SkillSafe,

**[00:25:27]** I'm a project or department SkillSafe, or I'm an organization SkillSafe.

**[00:25:31]** You can already tell, all of these things have a somewhat business character.

**[00:25:35]** That was the first attempt.

**[00:25:37]** Did that surprise you?

**[00:25:39]** Nobody at home deals with this stuff otherwise, right?

**[00:25:42]** Well, what do you mean, deals with?

**[00:25:44]** I think, well, let's say,

**[00:25:46]** in the family you don't have that, right?

**[00:25:49]** You deal with it...

**[00:25:51]** In the family, that counts for real.

**[00:25:53]** No, but...

**[00:25:55]** That's a different family, more like the mafia, greetings to Italy.

**[00:25:58]** You don't have that many different... Yes, exactly.

**[00:26:00]** I was just going to say, you don't have that many different groups.

**[00:26:02]** If you were to say, well...

**[00:26:05]** There's information that should stay within the family.

**[00:26:08]** There's information I want to share with the grandparents.

**[00:26:12]** But certainly not everything we discuss in the family.

**[00:26:15]** There's also information I maybe only want to

**[00:26:18]** share with my partner and not with the kids. So, when something like that comes in,

**[00:26:23]** then you can say, well, there are actually already different groups for different

**[00:26:27]** knowledge spaces. You can of course make it as complex as you like, but at first you can also

**[00:26:33]** start simply, the way you just described. The nice thing, but we're getting into the

**[00:26:38]** north of these SkillSafes, is that you can, it's kind of a skill, distribute it

**[00:26:43]** And you can also maintain it like a skill, with the help of the skill.

**[00:26:49]** And you can also, let's say, freeze it.

**[00:26:51]** Yes, version states, along the lines of the skill that's available,

**[00:26:58]** aha, he's smiling, he wants to jump in, I'll finish the sentence before he says anything.

**[00:27:02]** You can bring it to version states.

**[00:27:05]** And when you then distribute the skill and make it available to the AI system,

**[00:27:09]** you can assume, okay, this is in there and that isn't.

**[00:27:12]** And that's the version, not some interim state or anything, a certain reliability.

**[00:27:19]** Or would you like to disagree with me there?

**[00:27:21]** No, no, that's fine.

**[00:27:23]** At this point I'd like to ask a question to the listeners of the podcast.

**[00:27:31]** Be honest, please, who among you uses version control or versioning for your files?

**[00:27:39]** And who says, knowledge management, yes, I've heard of that, that was the neighbor, he was a librarian.

**[00:27:49]** I notice, Mark, that I often make assumptions about what technical background people have.

**[00:27:58]** And I'm always surprised how many colleagues and friends

**[00:28:05]** use AI agents, on their computers, privately or professionally, some even use their private

**[00:28:14]** AI agents on their work computer, without really knowing what's

**[00:28:20]** actually happening underneath, and how do you secure fine data, and how do you version it?

**[00:28:25]** And this versioning, that's not, so you'll perhaps have to briefly explain,

**[00:28:30]** why you want that, also for a knowledge store like this.

**[00:28:34]** I also think it's lovely how you gave the example of versioning,

**[00:28:40]** another anecdote, people who use Photoshop know that Photoshop

**[00:28:45]** has different layers.

**[00:28:47]** And layers give you the chance to change things, let's say, non-destructively,

**[00:28:53]** because you move things back and forth and the background stays intact,

**[00:28:58]** and you move elements back and forth in front, and you get that through the

**[00:29:02]** layers.

**[00:29:03]** And I never learned Photoshop, and sometimes I sit in front of Photoshop and then you stand

**[00:29:09]** there and say, merge all layers.

**[00:29:12]** Every graphic designer's toenails curl up immediately when you say to merge everything onto one layer,

**[00:29:18]** but let's leave that aside.

**[00:29:20]** Versioning is, if I'm honest, something I actually

**[00:29:28]** use very rarely, only in the very few cases. Because with me, I mean,

**[00:29:38]** something like a contract, that I file away, and so on, I don't get

**[00:29:43]** new versions of it that often, new editions. Yes, I have a contract for my car insurance

**[00:29:48]** and that's that. The highest feeling is that I might get dropped and sign a new

**[00:29:52]** car insurance at some point. Yes, okay, fair point, but that's the

**[00:29:57]** kind of case where nothing happens, I don't know. Every ten years I add a new thing to it.

**[00:30:01]** I actually have little of this versioning at home, but in the

**[00:30:06]** company, knowing what applied when, what the basis was, which decision was made at which

**[00:30:13]** period and point in time, what was a quotation mark for the validity of the law and

**[00:30:19]** money, a guideline and statement, and also binding nature and reliability, when you look today at

**[00:30:27]** a matter, so you know in what context it took place, what the

**[00:30:33]** rules were, what was valid and binding at the time, and what is it today?

**[00:30:42]** I'd argue that we implicitly do this in private life too, when you say, hey, we had

**[00:30:51]** that appointment, but I can't make it, I'm sorry I can't come, because I

**[00:30:56]** have to go to the parents' evening.

**[00:30:57]** That's surely implicit, so an implicit example would be a different scenario

**[00:31:03]** would be.

**[00:31:04]** I was just wondering whether you should file the parents' council elections in GitHub.

**[00:31:09]** Sorry.

**[00:31:10]** Yes, no.

**[00:31:11]** There are definitely people who set up a meal plan and say, no idea,

**[00:31:21]** what we have to buy, and then we rebuild again, and because Grandma comes Thursday,

**[00:31:27]** oh no, she isn't coming Thursday after all, she's coming Wednesday now, those are the kinds of changes.

**[00:31:33]** Only that's not exclusive versioning.

**[00:31:36]** But anyway, what I was getting at is, you open these different levels,

**[00:31:43]** where you said, in your SkillSafe there's a level 1, in a company you would

**[00:31:49]** say, that's organization-wide, level 2 is then a smaller group, could

**[00:31:56]** be the entity, department, whatever, level 3 would then be a team level

**[00:32:02]** and level 4 is the personal. And at first I thought, wow, that's such

**[00:32:09]** complexity, you'll never need that. And then there are situations where you notice, yes,

**[00:32:15]** colleagues made a decision that contradicts a decision at

**[00:32:23]** organization level, say, the Chief Information Security Officer

**[00:32:29]** said you're not allowed to do something. But the team did it anyway. Or the head of

**[00:32:35]** Corporate Communications said we'll only use the following wording from now on, and you notice

**[00:32:43]** your team unfortunately still used something old in the app. Those are classic cases

**[00:32:50]** where you want to, and in my view that has not so much

**[00:32:56]** to do with carelessness, but rather with information gaps. For me it's about making sure everyone

**[00:33:01]** always has the currently valid information. And so I'd argue that in situations like this,

**[00:33:09]** where you want to make sure everyone knows, hey, Grandma isn't coming

**[00:33:14]** on Thursday, but on Wednesday, you version the data and make sure that

**[00:33:19]** only the most current state is there. And if someone then says, well, I thought

**[00:33:24]** Grandma was coming Thursday, it's clear, yes, that was the original plan,

**[00:33:29]** but it changed, on Monday evening, because Grandma said she's already coming

**[00:33:34]** on Wednesday. That saves a lot of trouble. It definitely saves a lot of trouble if it's

**[00:33:41]** easy to trace it like that, especially with partners,

**[00:33:49]** and with colleagues or, well, partners.

**[00:33:54]** Can you tell me? No.

**[00:33:57]** I basically only talk about people who are present.

**[00:34:00]** Hoping I haven't lost everyone by now, I'd come back briefly to the

**[00:34:04]** starting point, which is, what is this little bit of, let's say, knowledge trail for.

**[00:34:07]** How does knowledge relate to others, so that we have some foundation for it.

**[00:34:11]** But originally I came in with the sentence,

**[00:34:13]** unstructured chaos is my friend, that's how it really started,

**[00:34:17]** throwing everything into the inbox. And when I say everything, I mean chat messages,

**[00:34:21]** emails, documents like PowerPoints, transcriptions, whatever. And the astonishing thing is,

**[00:34:29]** that the topic account can do something with that quite well. Then I made SkillSafes for the

**[00:34:33]** most varied topics. That means, quite concretely, you had, for example, a Claude

**[00:34:40]** Code, and you installed this, the SkillSafe or the SkillSafe workshop plug-in, on it.

**[00:34:46]** Well, at that point I still had SkillSafe.

**[00:34:50]** And then you simply said, what you give it, basically.

**[00:34:54]** Here's a directory, build something out of it, or if you already have something, supplement the existing one.

**[00:35:03]** Exactly, yes.

**[00:35:04]** I can remember that.

**[00:35:05]** And then came discussions, hmm, and how do we structure this differently?

**[00:35:10]** Yes, exactly.

**[00:35:11]** But what's maybe funny at this point, greetings to all the friends

**[00:35:14]** who always put RAG systems somewhere in the wallpaper, along the lines of, yes, you need

**[00:35:19]** a RAG system now, which answers questions as an expert system, for, I have

**[00:35:25]** a strange data set and have questions about it. Basically, that's possible

**[00:35:31]** to do with a SkillSafe. So I don't want a RAG system...

**[00:35:35]** Because your, your, your, no, that, yes, implicit praise, sorry, but what I find really great is that you don't just have a RAG setup, you have above all a knowledge graph, and you can qualify the connections between the nodes, not just information at the nodes.

**[00:36:01]** Maybe you know this: you don't just say, I have a relationship with another person,

**[00:36:09]** but you maybe also want to know what kind of relationship it is, what it expresses.

**[00:36:13]** In task management you say, this one ticket depends on the other in the project.

**[00:36:19]** It has to be done before the other one can be done.

**[00:36:23]** Among people, you want to know: is that a partner, is that a friend,

**[00:36:30]** is that a child, is that a colleague? So that's normal.

**[00:36:36]** No, it's several of those.

**[00:36:38]** Yes, the child is the colleague.

**[00:36:43]** Lovely.

**[00:36:44]** Take the trash out, no, the work one says, doesn't matter. What I mean is, in private

**[00:36:51]** life we're completely used to qualifying such relationships between these nodes in a knowledge

**[00:37:00]** graph. We just don't put it that way. So a term like

**[00:37:06]** knowledge graph is simply foreign to us. But actually, implicitly, we know it,

**[00:37:14]** that we, well, sorry for the word, entities, so nodes, which can

**[00:37:22]** be documents, which can be people carrying some information, that we

**[00:37:28]** have certain attributes, have properties. We're used to qualifying the

**[00:37:33]** relationship. And in a RAG system, in most RAG systems, it's not

**[00:37:39]** common. Above all, even if you implement it there, setting it up, we

**[00:37:47]** do then chances and whatever, and then it's queried, and all of that takes time,

**[00:37:51]** effort and money. And you have to plan what you're doing, and that's also

**[00:37:55]** a complexity you can see. I once created, with SkillSafe, 28 GB of payload data, to compare two

**[00:38:07]** matters. So for each matter I built a SkillSafe and told the system, in the cloud: you've got two SkillSafes here, go and see where they differ. It then chewed through both knowledge graphs and told me at the end of the day where the differences are, in a very reasonable time, and nobody sets anything up just for something like that.

**[00:38:37]** You don't do that. And that was also the motivation for the

**[00:38:45]** SkillSafe, when I understood. Damn it, it can't just contain work instructions,

**[00:38:50]** but also spread knowledge, hold knowledge, and

**[00:38:53]** be responsible for questions and show connections between each other. That's

**[00:38:59]** also a capability you simply give it, because at the end of the day it's all Markdown files

**[00:39:05]** And yes, it's ultimately in a directory, and you hand over all the knowledge and have it available offline in the end too.

**[00:39:15]** You have it on the laptop, you can install it anywhere you have Claude Code.

**[00:39:20]** You don't even need code, even Copilot can do that, so it works everywhere.

**[00:39:26]** Because at the end of the day it's really nothing more than a directory structure with Markdown documents and sufficient links between them,

**[00:39:34]** where you have to be a bit careful with the SOUL.md and such,

**[00:39:38]** so that it's read properly.

**[00:39:40]** But as they say, in most cases,

**[00:39:42]** you tell the thing, here's a directory,

**[00:39:44]** work through it, answer my questions, and that's that.

**[00:39:47]** And yes, you can, but you can also,

**[00:39:51]** and I've actually done that in one case,

**[00:39:53]** say what's especially important to you during the import.

**[00:39:57]** So what should it please include in the knowledge graph?

**[00:40:01]** Not just saying, ah, okay,

**[00:40:03]** a document, and there's certain information in it, but you can

**[00:40:06]** also tell it what you want to pull out, whether you

**[00:40:10]** want decisions as their own elements or nodes,

**[00:40:15]** certain kinds of insights, when you say, I have a

**[00:40:20]** research task, and I have these questions that I need

**[00:40:24]** answered, works great. Before I get to context in the

**[00:40:30]** conversation. Maybe one more use case. I think we have so much,

**[00:40:36]** we talk, you know, about nodes and we talk about the inbox and we talk about

**[00:40:39]** blah blah blah. I think sometimes you should also give a few more

**[00:40:43]** examples. Where does it actually help you? I have one example of my own, because you have

**[00:40:48]** different matters and you want to compare the differences. The other

**[00:40:51]** example was, you want to keep knowledge for an expert system,

**[00:40:54]** so that you don't constantly have to query some database somewhere and

**[00:40:58]** ask, how does this look, and set up a big database, but that in your

**[00:41:02]** agentic system you can play out your chat-window question and answer, but also use it in the

**[00:41:07]** agent context to act on it. And one example of context was, your drive

**[00:41:13]** has picked up on it a lot. I'm not related to Apple and I'm not in-laws with them

**[00:41:17]** and I don't have any shares and I don't get any money from them, but I find

**[00:41:21]** the company quite good anyway, and the products too. And accordingly I

**[00:41:25]** always follow their developer conference, and so I went and got the

**[00:41:29]** whole transcripts, that's the spoken word of the presenters, which over a week

**[00:41:34]** or across the last few days, I think, was all published the same day.

**[00:41:40]** But you've got this whole bag of transcripts on the most varied topics, from the most varied

**[00:41:45]** frameworks, from the most varied programming paradigms, from the most varied rules that

**[00:41:50]** you build software with, for example, or for the Apple operating system.

**[00:41:53]** And for Apple's operating system topics, and so on.

**[00:41:56]** And there I simply went and said, look out here, there's YouTube,

**[00:42:01]** Apple has published all of that there, so please download all of it and throw

**[00:42:04]** it all into a directory, and then I built the SkillSafe out of it.

**[00:42:09]** And then had a WWDC skill.

**[00:42:13]** And now you could ask this skill what Apple has brought out new, the management,

**[00:42:19]** and what you have to watch out for, what's deprecated now, that was the one thing.

**[00:42:22]** But the other thing was, I could tell the system, that is, tell the co-work.

**[00:42:28]** Look, here you have an Azure DevOps, that's a lot of our projects.

**[00:42:33]** You see that in the word map, you see what people are working on right now.

**[00:42:37]** You see bugs there, you see the knowledge documentation.

**[00:42:41]** But you also see the source code there.

**[00:42:43]** And then I went and said, look here.

**[00:42:46]** Do you see all of that?

**[00:42:47]** Just take a look.

**[00:42:49]** For your view, use this SkillSafe. And then the thing went and looked at the

**[00:42:55]** projects one by one, one by one, and then told me afterwards, look out.

**[00:43:00]** In that project, the following things are deprecated. In that project you got the feedback,

**[00:43:06]** this offers this functionality from iOS 27, and so on. So it basically made a

**[00:43:13]** mapping with the knowledge that Apple had conveyed, with active challenges

**[00:43:19]** you have in projects right now, or where changes are coming up, and it

**[00:43:23]** basically superimposed them, and then you sit there, you can barely

**[00:43:28]** wipe the smile off your face, because at that speed, dependencies,

**[00:43:33]** changes, opportunities and risks come out, and if the

**[00:43:39]** answer of one or the other listener is, it thought of 1000 percent of all topics,

**[00:43:44]** yes, I know, 1,000 percent gets difficult when 100 percent is basically the limit. But

**[00:43:49]** no, probably not. But it probably thought of a lot more

**[00:43:55]** than I did. And above all, you had a system and could go to the product owners and

**[00:44:01]** say, look out, things are changing here. Here's the SkillSafe, ask it.

**[00:44:07]** Talk it through with your project again, discuss it again with your developers, and so on.

**[00:44:12]** And I find this question, how do I write a work instruction as a skill, is one thing.

**[00:44:19]** But how do I store knowledge so that the skill can work even better,

**[00:44:23]** so that you can work even better with your system?

**[00:44:25]** There's so much gold hidden there, because AI systems are already smart.

**[00:44:33]** But the more context they have about what's occupying you, what you want to do right now,

**[00:44:40]** where you need help right now, the more it helps them focus and bring you

**[00:44:47]** support.

**[00:44:48]** And we're not even at collaboration with people yet.

**[00:44:50]** We're also not at what they promised here with their dots.

**[00:44:54]** We're simply at the question of how the system gets equipped so that

**[00:44:59]** it helps you here and now, that it understands you, that it supports you, that it

**[00:45:06]** starts actions that are simply more than if I'd just asked

**[00:45:12]** for another classic case, research what Apple has released on the internet and tell me what

**[00:45:16]** that means for my project?

**[00:45:17]** You'd get an answer too, but I'd bet on it, it would be

**[00:45:22]** by a long way worse.

**[00:45:24]** And once you've got used to building a SkillSafe like that, and you can

**[00:45:29]** also build your capacity wickeys or whatever, however you like, but once you've started

**[00:45:34]** throwing things in there to make the AI system more digestible, usable,

**[00:45:41]** you see what data is, the gold of the future, blah, blah, blah,

**[00:45:46]** yes, we've heard those stories very often, for a very long time,

**[00:45:49]** but you get a sense of, yes, that's right.

**[00:45:53]** And I'll even top that.

**[00:45:55]** I have, as I said, Apple and so on.

**[00:45:58]** I'd like to chime in briefly.

**[00:46:00]** I just want to remind people once more.

**[00:46:02]** This is the alternative to the memory solutions that the standard apps are bringing along right now.

**[00:46:12]** And what Mark just said about the new scales, that's not only in use with him,

**[00:46:16]** but with me too, where we say there's information that is not

**[00:46:22]** volatile, but should be available for a few more sessions, or for a somewhat longer

**[00:46:29]** runtime. And for use cases like that you can very well pack it into such a skill,

**[00:46:34]** into such a knowledge draft, because I assume you delegate something to an agent

**[00:46:40]** platform, right? New buzzword, but everyone offers all kinds of things, you can

**[00:46:46]** piece it together now even at the hyperscalers, a bit of hot air with it, but you can

**[00:46:54]** simply hand such a SkillSafe along as a skill and say, by the way, this is your main context,

**[00:46:59]** and this SkillSafe, you can, which you haven't said yet, you can also repackage again and again,

**[00:47:03]** so you say, okay, first I thought, we'll do, no idea,

**[00:47:08]** all the groups in the company, all company-wide policies we pack into one skill, and

**[00:47:14]** then you notice, ah yes, good, the purchasing policy and the controlling policy are now

**[00:47:20]** perhaps irrelevant for the software developer, so let's make

**[00:47:26]** a knowledge store that's relevant for software developers, and one for controllers, or

**[00:47:32]** one for purchasing policy.

**[00:47:33]** And you can repack them again and again, and at first I thought, oh well, then

**[00:47:38]** I'd be throwing tokens out of the window every time.

**[00:47:41]** No. You can take the original SkillSafe or the original knowledge, as a

**[00:47:48]** base, right?

**[00:47:49]** Because you have the knowledge graph, which is an abstraction, but this knowledge is

**[00:47:54]** the relevant part.

**[00:47:55]** Unless you say, no, if I'm now extracting for the controller, then

**[00:47:59]** different rules apply to the extraction, then I want

**[00:48:03]** different nodes and relationships in the knowledge draft.

**[00:48:06]** But again, that's of value to you too. If you say, no, I want to reprocess this information for the controller, then it's of value when exactly that happens.

**[00:48:19]** And now let me ask, how well do the standard systems support that, the ones you can buy outside for big money and big convenience?

**[00:48:29]** Not that I want to advertise for your skills, but they're available, and I have to

**[00:48:37]** occupy myself with them a bit at the start, although the documentation, even though it's

**[00:48:41]** in German, I find quite incomprehensible.

**[00:48:44]** You can already get dissed for German documentation.

**[00:48:47]** That's what it is, I find that nice, that pleases me, but ...

**[00:48:50]** I can't really diss German documentation, I don't even know, is "dissen" a German

**[00:48:54]** word?

**[00:48:55]** Am I allowed to do that?

**[00:48:56]** Whatever.

**[00:48:57]** Whatever.

**[00:48:58]** What I was getting at, I always try, you named the use cases, each of you

**[00:49:06]** can download it, so essentially they can point their Claude Code,

**[00:49:11]** or Codex or Gemini or whatever, at the address.

**[00:49:14]** Yes, sorry, exactly, because we're not sponsored, your podcast,

**[00:49:20]** but you can take it and simply explore, nothing bad happens there.

**[00:49:26]** This data, depending on what subscription you have, or whether you say it's on

**[00:49:33]** Bedrock, AI Foundry, GCP Model Garden, wherever.

**[00:49:38]** Whatever you choose, wherever your GPUs run.

**[00:49:44]** Or locally. You decide. You have the option.

**[00:49:49]** Just try it out.

**[00:49:50]** And I was just trying to catch my breath, but I'd originally also said, once you've

**[00:49:57]** played around with it, you get a feeling at some point, I'm saying feeling here,

**[00:50:04]** for what else you can use it for? Where else does it help you, and one application, as I

**[00:50:10]** just... I honestly simply installed it and said, I'll just let it run

**[00:50:16]** in the background and ask it things in between, and now something where I

**[00:50:20]** could use SkillSafe. Look at our last few sessions, if I could optimize this somewhere

**[00:50:26]** with SkillSafe. And its answer would be, yes, I've already done that. But even now

**[00:50:32]** I'd still like to come back to the topic briefly, because what you say

**[00:50:37]** is of course true, that you can say, dear system, look, here you have a lot of

**[00:50:42]** options, now, never mind, that applies to all skills and plug-ins, that you can

**[00:50:48]** ask the system where it might have helped me if it had been used, or

**[00:50:53]** can you give me a recommendation. Where I'm currently using it too, and the app is unfortunately

**[00:50:58]** not in the store yet, where I also noticed, first with initial curiosity and then, because

**[00:51:05]** I can't get my hands on it anymore, that I already have the app on my phone,

**[00:51:09]** it's an application that does nothing other than pack the screenshots I take

**[00:51:13]** into a SkillSafe. Because I'm quite, we had it in the

**[00:51:20]** pre-discussion, yes, greetings to people who can't stand it

**[00:51:24]** when a mail icon shows more than the number 1 in red for unread mails, yes.

**[00:51:31]** I'm at a large four-digit number, but only because

**[00:51:35]** I now and then just say, select all and mark as read, done, so I don't

**[00:51:39]** have that issue, I see something, whether it's on social media or somewhere else, yes,

**[00:51:45]** and then I take a screenshot on the device I'm on. And a screenshot is,

**[00:51:51]** well, it's a photo, right? A photo of the screen content, there can be text in it,

**[00:51:56]** there can be anything else in it. Or QR codes, or whatever. And then I built

**[00:52:02]** a small application that does nothing else for you than be a kind of screenshot vacuum cleaner,

**[00:52:06]** and use a local model to break these things down, the way you know it from the Knowledge

**[00:52:12]** Distiller and the SkillSafe, and it tries to get everything possible out of the image,

**[00:52:18]** basically.

**[00:52:19]** So if there's a photo, it tries to understand with Apple's Vision framework,

**[00:52:24]** aha, there's a tree and a laughing child.

**[00:52:26]** It tries to extract the texts, it has data, selectors, what it picks up,

**[00:52:30]** are addresses, dates, links in it, reads QR codes and all that stuff.

**[00:52:36]** The app is not yet available to everyone, right?

**[00:52:41]** Well, it's currently in review.

**[00:52:45]** And that's really funny, because I started the thing on my phone.

**[00:52:51]** Honestly, the phone got a bit warm, because it had to somehow.

**[00:52:55]** Well, the first number was a four, and then a few more numbers came,

**[00:52:59]** because it's the number of screenshots it should import from the last twelve months.

**[00:53:03]** And when it was finished

**[00:53:05]** and you then also in the app on the iPhone, I then had it with chat and with this day view,

**[00:53:12]** and you navigate through it, but there's also a Mac version for that, and I have MCP support,

**[00:53:18]** so I can then go at it with Claude or whatever, and suddenly all

**[00:53:23]** these screenshots that I've taken over the last 15 months, I don't want

**[00:53:29]** to sound pathetic, but living knowledge, because I took the screenshots

**[00:53:34]** and I've forgotten most of it, yes. The ADHD comes to mind, like when I recently

**[00:53:38]** found my company badge at the coal machine, my bag in the room where I started the

**[00:53:43]** meeting of the day, only that in the meantime it was six p.m. And at that point it helps

**[00:53:49]** me a lot, because I can now just take a screenshot, and I know, if

**[00:53:57]** there's an appointment on it that I want to be reminded of, if there's a link on it

**[00:54:01]** that I don't want to forget, if there's anything else, that this system collects it and then sends me a push message and so on.

**[00:54:09]** And now you might ask, hey, a push message, that's where the circle closes to the context,

**[00:54:14]** yes. I wrote this small skill for myself, which basically tries not to store knowledge for you,

**[00:54:21]** but to determine the relevance of knowledge for you. Until recently, for example, I was

**[00:54:28]** responsible for everything at our company that was mobile app development. That means my professional interest is

**[00:54:33]** very strongly mobile. iOS, Android, yes, for the most varied projects that

**[00:54:38]** you're standing there. That means ContextMe didn't exist back then, but I could try it out on this

**[00:54:44]** example. If you had run it back then, it would have said, look out

**[00:54:49]** for iOS, Apple and Google and Samsung and so on, very important, very important. Today I'm interested

**[00:54:55]** in none of that anymore. iOS only privately, and professionally more the whole topic of AI. So

**[00:55:03]** above all, higher in importance than mobile. And ContextMe picks that up over

**[00:55:10]** time, because I tell it, please look over a period X, what mail I have,

**[00:55:15]** what Teams messages I have, which projects I'm in, in which

**[00:55:20]** role I work, and from that the system learns, roughly, what the market is interested in,

**[00:55:24]** right now, how it's changing, professionally and privately, and that then feeds back into

**[00:55:33]** the SkillSafe and into the app that's on its way right now, just briefly...

**[00:55:36]** Yes, wait, wait, just briefly, so, quite

**[00:55:39]** concretely, you've installed ContextMe and then really use it as a slash

**[00:55:47]** command.

**[00:55:48]** No, no, no, it's different, I've set it on a timer, so it goes once

**[00:55:54]** a day over all mails, all projects, all Teams messages, and updates. That's

**[00:56:02]** once a day a good rhythm, maybe once a week or once a month would be enough, so not that erratic

**[00:56:07]** I am, that might be enough, so it's simply set up that way for now.

**[00:56:11]** So that it looks at what interests Mark.

**[00:56:16]** I have it running as jobs on my inbox, you just mentioned the Inbox directory.

**[00:56:22]** On the Mac mini at home I have an import job running, and it uses

**[00:56:27]** context, like, on the different import directories, and I have a daily briefing, where my

**[00:56:37]** day is summarized, yesterday's day, all the information, that is relevant today,

**[00:56:43]** which appointments I have, what I have to keep in mind. And that's also where

**[00:56:49]** context is included. It's then used read-only, basically. So I take it

**[00:56:57]** to work out what interests me, and then I take this

**[00:57:01]** ContextMe result and bring it, for example, into this app that

**[00:57:08]** manages the screens, these screenshots. Along the lines of, I don't want to

**[00:57:13]** get a push message for every bit of stuff, like, tomorrow at 12:00 there's

**[00:57:17]** this, which I maybe screenshotted because my daughter is into horses.

**[00:57:21]** I personally have nothing against horses, but full stop.

**[00:57:26]** But I don't want it to immediately go, oh, very important tomorrow,

**[00:57:30]** drive to the stable at 1 p.m. tomorrow, right away.

**[00:57:32]** But if, for example, it's a screenshot of some cool

**[00:57:36]** gadget, then I do, possibly, want

**[00:57:40]** it ranked higher for me, and that I can then

**[00:57:44]** basically consume it faster, have it prepared for me, and I use it there

**[00:57:50]** just like for my personal second brain: I tell it, look out,

**[00:57:55]** throw the things in there, and you know, along the lines of, okay, the iPhone

**[00:58:02]** I've always liked and still do, but when I use it

**[00:58:05]** professionally, it knows, look out, that now the

**[00:58:09]** iPhone Duo is coming out, which the market finds totally great, but which is now

**[00:58:13]** secondary in its professional context. There, maybe it's more important right now that

**[00:58:19]** Maestro 6.1 has done something. And that's how ContextMe helps my second brain and me keep an overview in

**[00:58:30]** a world, and bring order to the chaos I mentioned at the start.

**[00:58:38]** We opened with knowledge management being complex, and that fits too.

**[00:58:45]** I think anyone who's listened to us until now deserves congratulations too.

**[00:58:49]** They're entitled to basically a SkillSafe...

**[00:58:52]** Exactly, everyone who has listened so far

**[00:58:55]** is entitled to a special edition of SkillWorkshop instead of a SkillSafe download.

**[00:59:00]** Because I was just about to say,

**[00:59:02]** because so far we've only talked about SkillSafe,

**[00:59:06]** the history, and above all about you or me doing something for

**[00:59:13]** ourselves or for others, but not yet with others. And that's something we both

**[00:59:20]** have already done, that we said, I want to maintain such a SkillSafe with others.

**[00:59:26]** And for that I used, for example, the SkillSafe workshop, which

**[00:59:32]** at least for me answered the question, okay, I just said, in the family there are

**[00:59:41]** situations where you say, well, I have things I discuss with my partner, and

**[00:59:46]** no idea, we somehow have to make decisions on certain topics,

**[00:59:49]** but there we definitely don't want to involve Grandma, but for some other things we want

**[00:59:55]** maybe to keep Grandma informed too, and you have that kind of situation in a company context too,

**[01:00:00]** where you say, in a project team you work out something, and one thing is directed

**[01:00:08]** stakeholder communication, where you say, well, that one I have to, there I have to regularly

**[01:00:14]** somehow align expectations. But there's also undirected stakeholder communication,

**[01:00:19]** where you say, well, in general other colleagues may also be interested

**[01:00:24]** in finding out what the project is actually about. What are they doing right now? What

**[01:00:28]** learnings could they share with me, and want to, especially when it's about the AI field,

**[01:00:34]** there are a lot of people who are really interested in that. And for exactly that kind of thing, from my

**[01:00:40]** point of view you have quite a good solution, with which the SkillSafe workshop was created, because on the one hand

**[01:00:45]** we can basically have internal knowledge, for example in a SharePoint directory or another

**[01:00:52]** synchronized directory. And on the other hand, you've already said,

**[01:00:58]** versioned knowledge, so to say, okay, now we have this knowledge sitting in a directory.

**[01:01:05]** Greetings to all the department directories of this world, well, information goes to die.

**[01:01:09]** Now it would be very good if we could curate that and then make it available to others too,

**[01:01:16]** in a way where they know, okay, this is current, and that is, that is,

**[01:01:22]** the other is no longer current, that was last week's state. This knowledge

**[01:01:26]** is outdated now, though. And for that you've, you've created a way

**[01:01:31]** to automate it via Git and something like CI-CD, that is pipelines, workflows,

**[01:01:40]** to automate releases. Shall we talk about that briefly?

**[01:01:43]** Well, I think at this point I've tried to lead over a bit, because these changes, along the lines of ContextMe, I did say help me with this connection to the screenshots, but it actually helps me mainly with the workshop, because the SkillSafe created a skill with knowledge.

**[01:02:03]** And then you distributed it, the workshop says, okay, I'm not alone in the world.

**[01:02:09]** I have people, agents, whatever, who consume it together with me, but also maintain it.

**[01:02:16]** And that's where the topic comes in, damn it, I can't lock it away in that sense,

**[01:02:23]** instead I need it, or want it, jointly consumable, jointly maintainable.

**[01:02:30]** And the idea behind the SkillSafe workshop was to say, okay, if you don't lock it up,

**[01:02:37]** then you have additional challenges, something like temporal assignment.

**[01:02:43]** Yes, yes.

**[01:02:44]** Yes, that gets complicated, but temporal assignment, I mean, what does temporal

**[01:02:47]** assignment mean?

**[01:02:48]** It's the question of how you deal with newer information.

**[01:02:53]** So does only the new information apply, or does historical knowledge also need to be

**[01:02:58]** kept, like, what Mark has, he has an annual salary of two million, it has to

**[01:03:04]** be said out loud, yes. And now he's had since the first... But the whole

**[01:03:08]** thing yesterday, he got a salary cut. Exactly. And then it's already

**[01:03:16]** important to know over what period Mark had the two million, or whether

**[01:03:21]** it's really only to know that Mark is now down to 20,000. So, and

**[01:03:26]** those are the things. The second thing is that the knowledge isn't locked up and distributed in a SkillSafe, but is alive.

**[01:03:36]** Do you have a certain curation obligation? Is it all still consistent in itself, check routines you want to run.

**[01:03:48]** Above all when several people work on the system, so you don't end up running into the pre-dule,

**[01:03:54]** where, due to some error, branches of knowledge get cut off, and that the system also

**[01:04:01]** is able to restructure itself. So this workshop has the topic that

**[01:04:08]** you can also talk with it about how the branches look. In the system, what

**[01:04:15]** are the clusters the SkillWorkshop arranges itself by, and if you now say, okay,

**[01:04:21]** the classes have changed, then you can also ask the workshop why.

**[01:04:26]** The workshop can also export it, and then we're back at the

**[01:04:31]** SkillSafe.

**[01:04:32]** And the workshop has something where I thought, damn it, because that's

**[01:04:36]** the next problem when you work with several people: either you invite them

**[01:04:40]** all over for coffee and cake, to your computer, and avoid competing

**[01:04:44]** write access by letting them all at your keyboard, or you try

**[01:04:49]** to come up with something that helps, so that when people sit at distributed systems,

**[01:04:56]** they can still work on the system. But what do they have access to then? And there you

**[01:05:02]** very quickly end up with things like iCloud or Dropbox or OneDrive, or I also wanted a few

**[01:05:10]** other tools that aren't from Microsoft, so to speak, like the Rediff of iCloud.

**[01:05:15]** Like Transferner, although Wrenswehr has no live file access, it only has download...

**[01:05:21]** Google Drive.

**[01:05:23]** Exactly, and how do you deal with people being able to do that?

**[01:05:27]** There's another sound too, next.

**[01:05:28]** Super.

**[01:05:29]** Yes, thanks.

**[01:05:31]** Sovereignty comes first.

**[01:05:33]** And how do you manage it so that people, on their own devices, are able

**[01:05:41]** to consume the knowledge, to maintain the knowledge. Not because it's a backup of files,

**[01:05:47]** but because it's the representation of connected knowledge in it. And also approaches

**[01:05:54]** to sync conflicts, written at the same time with locks, so that you prevent writing at the same time

**[01:06:01]** in this value, so you give the system something that, when the

**[01:06:06]** agents do the maintenance, because you're still interacting with the agent,

**[01:06:09]** you tell your Claude and your Gemini, maintain this here, here's the budget for it, go, go, go, go.

**[01:06:15]** That the system says, I can't right now, because another agent is on it, I'll check something else first,

**[01:06:21]** I'll restructure it so that you, I don't know, the physical limit of simultaneous humans is,

**[01:06:31]** but that you get a bit of order into it, and that you also have the chance here.

**[01:06:35]** To put it bluntly, to have a collaboration platform for cheap money,

**[01:06:40]** where you can know, edit together and share, because for that money, that's fun, you

**[01:06:45]** can also think in the process about how to do it well.

**[01:06:47]** Yes, but the interesting thing I found, and there I wondered how much

**[01:06:56]** of that you've actually built in?

**[01:06:58]** You have a few basic rules in SkillSafe workshop, along the lines of, that

**[01:07:02]** you have to agree on as a group working together on the vault, so that's something like a

**[01:07:08]** maintainer list, and what I found totally fascinating, again a question for the

**[01:07:18]** listeners: who of you has ever worked with decision records, that is, basically

**[01:07:24]** decision templates, and I was constantly confronted with those as SkillSafe

**[01:07:31]** workshop imported them, basically. We have, in OneDrive, in our case we have

**[01:07:38]** a Vault-Inbox directory, and we said, okay, everyone just throws their stuff in there,

**[01:07:43]** and then you can have the SkillSafe workshop import it regularly. So

**[01:07:49]** we throw PowerPoints in there, we throw meeting transcripts in there.

**[01:07:54]** The SkillSafe workshop imported the stuff and then said, in the meeting you

**[01:07:59]** by the way made the following decisions.

**[01:08:01]** Oh, wait, only one of you was in that meeting, and by the way the following

**[01:08:05]** things were discussed.

**[01:08:06]** There's again a contradiction to the decision you made last week in that and that

**[01:08:10]** meeting.

**[01:08:11]** And now you have to please carry out a conflict resolution here.

**[01:08:14]** I expect votes from each one of you, and I've set up the template here

**[01:08:19]** already.

**[01:08:20]** Please always use that for such decisions from now on, and now everybody

**[01:08:24]** vote, please.

**[01:08:25]** I've also set up task management for everyone in the vault, and if now, well,

**[01:08:32]** I have no idea, I do that, then it works out, that's completely absurd, it looks

**[01:08:37]** it up, when I say, what are my tasks, it looks up, who is my, who's actually talking

**[01:08:42]** to me here, hello, who are you, it then looks at the machine name somehow,

**[01:08:46]** some cryptic corporate computer, then next it looks at, ah,

**[01:08:52]** Ah, there, he has a Git directory in his home directory.

**[01:08:56]** Ah, look, there's a name and an email address in it.

**[01:08:59]** Look at you.

**[01:09:03]** I know, Schiere, I know where you live and where your car is parked.

**[01:09:06]** Yes, yes, yes, of course.

**[01:09:08]** I found that super fascinating, and then next up is Mr. Gagau, and he said,

**[01:09:12]** ah, wait a moment, in the meeting you talked about

**[01:09:15]** this project, where two of you are working on it,

**[01:09:18]** there's also this Jira project. I'm syncing the tasks that influence this other vault, the ones the group works on together, and I'm bringing them over here, because the others in the group should weigh in too and should know about it, so I'm putting the information in here, but keeping the reference to Jira.

**[01:09:40]** And so, Jira is a task management system from the company.

**[01:09:45]** I think anyone who's listened this far will get Jira sorted out.

**[01:09:49]** Okay.

**[01:09:50]** Because I think we've probably already lost some of the listeners,

**[01:09:53]** but the topic, I mean, the longer we talk about it and the more small examples and anecdotes we give,

**[01:10:00]** they basically show one thing, right:

**[01:10:06]** it's not that Mark uploaded a cool GitHub project, but that the systems are able

**[01:10:12]** to do many things you wouldn't have trusted them with.

**[01:10:16]** And when you introduced that.

**[01:10:20]** That's not so cool for me.

**[01:10:22]** The thing looks at it.

**[01:10:24]** What needs do we have as a group, and it makes suggestions about them?

**[01:10:28]** I hope what I wanted to get at, before I get to the sentence,

**[01:10:33]** is that it's basically an intrinsic enrichment for every further use.

**[01:10:37]** So, the more SkillSafes and knowledge spaces and workshops you have,

**[01:10:43]** or whatever you call them, the more intelligently, let's say, they can support you.

**[01:10:49]** Because at some point these systems know more and more about what matters to you,

**[01:10:52]** what matters to the group, what matters to the project, what they pay attention to.

**[01:10:56]** And that way you also manage not to be the smartest person in the room

**[01:11:00]** to set up such a thing, but the thing is basically the sum of all the decisions

**[01:11:06]** you've made in the past. Probably not all of them, and some things also get lost there,

**[01:11:09]** but it complements itself. And I already have the feeling

**[01:11:14]** that, like back in the day with "let me google that for you", there were people who

**[01:11:18]** entered a search term and got hits, while others thought of the same search term

**[01:11:21]** but never found anything, so that at some point, on the one hand,

**[01:11:25]** you have a knack for it, and on the other hand so does the machine. A knack for you,

**[01:11:28]** your needs, your concerns, whether it's you as an individual person or you

**[01:11:32]** in professional contexts. But what I also wanted to get at in this context

**[01:11:37]** and I find this is also something that has nothing to do with Second Brain and workshop and

**[01:11:42]** so on, but it's a nice example for explaining it. I know someone

**[01:11:47]** who once said to me, Mark, you know, I don't want to quote it, because

**[01:11:52]** it really came out wrong, let's say, it drove me crazy. I sat

**[01:11:56]** for three months thinking, how do I build myself a second brain?

**[01:12:00]** And then you come along, well, me, after a weekend, and say, hey,

**[01:12:04]** I've got something, and it works, and it has somehow 80, 90 percent of his thoughts in it.

**[01:12:09]** And then he says, honestly, I'm making the months-long head, how do you do that?

**[01:12:13]** And there it is again, you know, I've got the knack, I said, blond.

**[01:12:17]** Yes, no, that too, but I think the art simply lies in you,

**[01:12:21]** when you don't know how things will turn out at that point,

**[01:12:24]** what might not have been thought of, or what you have to think about, that you approach this

**[01:12:30]** with, let's call it, a kind of grounded attitude, combined with, yes, I've now also been

**[01:12:37]** over 20 years in the corporate world, so, let's call it life experience, professional

**[01:12:43]** life experience, we don't want to talk about private life, simply professional

**[01:12:46]** life experience, you bring in professional life experience, you have a tool

**[01:12:50]** at hand that empowers you rather than hinders you, because it's also gotten used to, and you have

**[01:12:55]** not seen it.

**[01:12:56]** And then you try things out, and based on your experience you notice, okay, there one should

**[01:12:59]** maybe pay attention to version conflicts, there one should pay attention to binding commitments,

**[01:13:04]** one should pay attention to, to, to, and so on, and so you come closer to this solution and

**[01:13:07]** don't lose yourself in months of conceptual work.

**[01:13:12]** Exactly, because you do it, and that's what I have to say brought me the

**[01:13:17]** greatest added value. Those who may have stumbled across my blog already

**[01:13:22]** will know it's called Overthinker's Thoughts, and that was really my hobbyhorse. The

**[01:13:30]** whole time thinking about things, and seriously, no joke, five years ahead,

**[01:13:35]** thinking about what will all happen and what the influencing factors are, and with all

**[01:13:40]** that thinking not managing to take the first step. And that's why

**[01:13:45]** my plea from the beginning is also: install it, and create an environment in which

**[01:13:51]** I once said, reduced blast radius. So where you ask, what's the worst that can happen?

**[01:13:57]** Okay, I can handle that. Once you've reached that situation, then you have

**[01:14:03]** a safe space, an area created for you, where you can run small experiments,

**[01:14:11]** where you can use such a thing and simply try it out.

**[01:14:15]** And honestly, the moment seems to come, greetings to my colleagues, where you

**[01:14:21]** feel overwhelmed, where you see that Alex made this thing,

**[01:14:26]** which is really great.

**[01:14:27]** And now let's say, my Copilot should show me the things I

**[01:14:35]** have to do, and Copilot buries you in 80 decision records, where it says, yes,

**[01:14:43]** by the way, Alex has imported your meeting minutes from the last three months from the

**[01:14:48]** whole projects and initiatives you're running, and by the way, these are all contradictory

**[01:14:53]** things and decisions you wanted to make. And sometimes the reaction of

**[01:15:00]** the colleagues is just to close it again and ask whether I've

**[01:15:03]** been drinking varnish. So I'm now running to Copilot's rescue, well, you can do all of that with Copilot too. What's nice about the non-Copilot things,

**[01:15:18]** classic Copilot, that we can use the skills, not because we have a SKILL.md file for it, a maximum of 13, sorry, the teasing,

**[01:15:30]** but that we can have real skills in the deterministic, not the generative data, you didn't see that, everything finds a home.

**[01:15:38]** But if you take something away from this, look at the blog and try the skills out.

**[01:15:47]** The skills don't break anything for you, except that they pull the rug out from under you a bit,

**[01:15:54]** namely understanding what I actually have hidden in your data. I said you can use it for small things, for 70 Apple talks or 28 gigabytes of data.

**[01:16:04]** And I think.

**[01:16:06]** As you also said, we're not the experts here, we're just trying things out and seeing what comes of it.

**[01:16:12]** This exploratory thing, I tinker with it and make it usable, and if it's good I talk about it, and if it isn't, I explain that it isn't.

**[01:16:22]** That helps. That's a hard thing to carry. But you report it, you pass it on right away.

**[01:16:27]** One tip I definitely want to share, because I've

**[01:16:32]** already had feedback on it several times: it really was a game changer, you

**[01:16:36]** didn't have it. It's not only the command lines, the CLIs of Claude, of Codex, etc.,

**[01:16:46]** that they can now see each other's sessions. So if I have one chat window

**[01:16:52]** open, the other chat window can see it. That means, if you say, you've

**[01:16:59]** tried something and you're stuck and say, damn it, I'm

**[01:17:05]** not getting anywhere, open a new window and say to Claude or ChatGPT, hey, I

**[01:17:12]** have a separate session open with you and I'm not getting anywhere.

**[01:17:16]** Please look at this and give me tips.

**[01:17:19]** Tell me what I can do.

**[01:17:21]** How do I get further?

**[01:17:22]** That's my goal.

**[01:17:23]** So you can step up to a meta level at any point and talk with another instance,

**[01:17:30]** so to speak, with another window of Claude or of ChatGPT,

**[01:17:33]** about how to get further in that original window.

**[01:17:38]** And that's a real advantage.

**[01:17:41]** I'd sometimes wish for that with people: you step out of your body, take Holger out of your body, talk to him about it, and the problem is putting him back in.

**[01:17:57]** What's wrong with Holger? Why doesn't he understand me?

**[01:18:03]** I've got much more trouble engaging with my new project, but unfortunately it's already late, and no matter how long we've been doing this, we've set a new record.

**[01:18:16]** I'm pretty sure that if we keep going like this, I'd like to quote a few rain.

**[01:18:22]** He had a child the first time, twins the second time, and a third time he didn't want to risk it, because he didn't know how the Wattmarsch rule goes.

**[01:18:30]** goes on. At this point, I'll definitely invite you again. For everyone who's listened so far,

**[01:18:36]** of course, we'll put it all in the show notes, so maybe also a

**[01:18:42]** small note there. All the episodes we have are also published on GitHub as a

**[01:18:48]** transcript, things like that. If someone says, oh, they talked for so long, I switched off,

**[01:18:53]** or I'll ask the system. I fell asleep, which,

**[01:18:56]** at what point did they talk about what, and will you tell me that?

**[01:18:59]** I always find that very exciting too, for us, when Jens

**[01:19:06]** then goes over the podcast episodes again and looks at what

**[01:19:10]** we talked about in there.

**[01:19:11]** It's always nice to have the material on hand for a guest too.

**[01:19:16]** On that note, a second brain won't run out on us. We may still have

**[01:19:21]** more second brains, and then the term second brain probably won't be

**[01:19:24]** quite right anymore.

**[01:19:25]** I once had a colleague who always called his dog Unudor Stresquattro and so on.

**[01:19:32]** But I don't know what his dog is called today, or whether he still kept to that rule.

**[01:19:36]** But I digress. Next time, you were here.

**[01:19:39]** Yes, maybe.

**[01:19:41]** Thanks for being here.

**[01:19:42]** And greetings to Jens too, because I think we haven't greeted him yet.

**[01:19:46]** But maybe next time with Jens again.

**[01:19:49]** Yes, I'm looking forward to next time with Jens too.

**[01:19:52]** We'll see, maybe I'll want to, sure, Jens, then... Oh no, I actually recorded with him then. Well,

**[01:19:56]** I have it in my calendar, my second brain knows about it too,

**[01:20:00]** maybe it's in the eight houses and unread emails. And at this

**[01:20:04]** point, if you liked the episode, leave a thumbs up and a like, if

**[01:20:07]** you didn't like it, please write us a comment, because then too

**[01:20:12]** we know you've listened until now, and wish you a pleasant

**[01:20:17]** night, a pleasant day with lots of people, especially those for whom a

**[01:20:22]** second brain would also have done others good. And with that, until next time. Ciao.

**[01:20:28]** Thanks. Ciao.

**[01:20:32]** Welcome to Think Different. Think AI., the podcast by Mark and Jens.

**[01:20:38]** Two tech-loving minds who don't just talk about artificial intelligence, but live it.

**[01:20:44]** Here you get clear classifications, real practical insights and a fresh look at what's possible.

**[01:20:51]** Down to earth, critical, and always with a wink.

**[01:20:55]** Something to think about, to smile about, and above all to join in on.
