---
title: "Just vibe IT"
episode_index: 43
published: "Mon, 08 Jun 2026 03:44:00 +0000"
duration: "2196"
page_url: "https://think-ai.podigee.io/41-just-vibe-it"
image_url: "https://images.podigee-cdn.net/0x,spMpsrQvFxNCV2XKgw65UvrHjchWyPfe2tjatJRw8NZM=/https://main.podigee-cdn.net/uploads/u73317/83dba456-dc11-4b39-a949-8aac7944b9b5.jpg"
audio_url: "https://audio.podigee-cdn.net/2480694-m-8e56e6d7291296a03244f65fa8a3c07c.mp3?source=feed"
guid: "b43faf503c50db5fd36fa6582a896611"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-06-08T11:01:02+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/043 - Just vibe IT.md"
translated_at: "2026-06-08T11:01:29+00:00"
---

# Just vibe IT

**Published:** Mon, 08 Jun 2026 03:44:00 +0000
**Duration:** 2196
**Web player:** https://think-ai.podigee.io/41-just-vibe-it
**Cover:** https://images.podigee-cdn.net/0x,spMpsrQvFxNCV2XKgw65UvrHjchWyPfe2tjatJRw8NZM=/https://main.podigee-cdn.net/uploads/u73317/83dba456-dc11-4b39-a949-8aac7944b9b5.jpg
**Audio:** https://audio.podigee-cdn.net/2480694-m-8e56e6d7291296a03244f65fa8a3c07c.mp3?source=feed

## Description

This episode is an interim episode without a guest – recorded just before the next episode. Mark and Jens sort through what has been happening around AI skills, Vibe Coding, and the major models in recent weeks. With a few stumbling blocks, a smart home anecdote, and a mention of a new website of their own.
Topics of the episode

Vibe Coding and Vibe Engineering – Andrej Karpathy coined the term in February 2025. Vibe Coding means: talking to the machine, and in the end, usable software comes out. Vibe Engineering adds more context.
When the large model fails – Marc's experience: Claude Code with Opus refused for hours to solve a specific problem. Plugged in OpenAI's Codex as a reviewer – and suddenly it worked. "Eye-opening moment."

Name confusion in the model zoo – Codex is sometimes a model, sometimes an app, sometimes a mode at OpenAI. Additionally, there's GPT-5.5, Claude Opus, Bedrock, Copilot, Azure. If you don't get mixed up, you're paying attention.
Architecture Decision Records (ADRs) – Write down why you decided on something. Not in Word, but in Markdown. The AI can read that later, check for consistency, and find duplicates.
When the AI takes over your Mac – Anecdote from the weekend: screen sharing, keyboard access, accessibility – and Claude clicks through the UI by itself to find its own bug. Weird feeling.

Manus AI in two prompts – Jens built an application with OCR recognition and Google Calendar login. Five minutes later, it was running. Functionally yes, ready for release, rather no.
Pre-mortem as a skill – Mark built a skill that thinks backwards: It has failed, what was to blame? Helps with security, login screens, consent, and everything you think about too late.
AI lies shamelessly – "Are all errors gone?" "Yes." Spoiler: no. Sometimes errors are just attributed to a different session.

Addiction factor and work-life balance – Why a rate limit can also have its benefits. Jens' Open Claude checks the time of day and sends him to bed.
Specialized tools instead of chat windows – Not everyone needs the full program. If someone spends all day making slides, you wouldn’t put a digger in front of their door.
Smart home repair through AI – Taught Philips Hue motion sensor to leave the light on when passing by again. A function that actually didn’t exist.

New: Podcast Website
There is a dedicated page on GitHub Pages with all episode transcripts – in German and English, each available for download as Markdown. Updated every Tuesday. With search, feedback form, and the option to share individual episodes. https://godmodeai2025.github.io/ThinkDifferentThinkAI/?episode=037&lang=de

Mentioned in the episode
Andrej Karpathy – "Vibe Coding" (February 2025)
Anthropic Claude Code, Claude Opus, Max-20 plan
OpenAI Codex (model and app), GPT-5.5
Amazon Bedrock, GitHub Copilot, Azure
Manus AI
Bolt, Lovable
Philips Hue
Mark-Uwe Kling – "The Day Grandma Turned Off the Internet" (Lecture at the Chaos Computer Club)
Previous episode with René on the topic of skills

Take-aways

Enumeration text writes down

why you made architectural and design decisions like this – in Markdown.

Use skills for security, clean code, and documentation. This is no joke.

Incorporate a pre-mortem into the workflow: What could have gone wrong?

When the AI says "everything is safe" – ask twice. On the third time, it might finally tell you what it left out.

Breaks are allowed. Vibe coding has an addictive factor.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here you will find clear classifications, real practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Food for thought, for a chuckle, and above all for joining in the conversation.

**[00:00:29]** Welcome to a new episode of Zink Different, Zink AI.

**[00:00:37]** Today, it's just Mark and Jens on the call.

**[00:00:44]** Yes, just Mark and Jens, yes, that's what I wanted to say too, Jens, right?

**[00:00:48]** Sorry if I don't always do this first or how was this usually done?

**[00:00:52]** Yes, we can let them watch, please, Pinter, leave it down in the comments.

**[00:00:56]** Just say, I have no manners, that's also a nice comment, I'll gladly accept that.

**[00:01:03]** Jens and I sat a bit earlier in our home podcast studio and thought, before we welcome our next guest, who will share his insights in another episode,

**[00:01:17]** let's also talk about and review what we've heard in the past episodes.

**[00:01:22]** I want to give you a brief update.

**[00:01:23]** Some time ago, we had René as a guest.

**[00:01:26]** We discussed the topic of skills in strategic gold.

**[00:01:29]** And in this episode, we are not afraid.

**[00:01:31]** It's not just about skills, at least not exclusively.

**[00:01:33]** We talked in the episode about how technology has AI skills,

**[00:01:37]** but that organizations and people also need skills,

**[00:01:39]** so that people and organizations should be taken along on the journey

**[00:01:44]** and should consider how to bring technology closer,

**[00:01:47]** reduce the hurdle or find the right tool at the right time in the right way,

**[00:01:51]** to the person on the screen or wherever they are set up, so that they can properly

**[00:01:57]** use it. And we thought, let's provide a bit of assistance

**[00:02:01]** and a bit of support regarding what has happened in the whole AI-skill-vibe-coding corner noise

**[00:02:08]** and how it can be applied.

**[00:02:10]** Vibe-Coding, I would naturally jump right in. Vibe-Coding, the term that

**[00:02:18]** has a lot of quotations as well, I believe encapsulates many terms that are currently being defined,

**[00:02:22]** has been coined last year, I think it was last autumn, if I remember correctly.

**[00:02:25]** So this term isn't that old, but let me try to make a little

**[00:02:32]** definition for it, so we're all on the same page as we continue

**[00:02:36]** into the episode. Vibe Coding essentially describes a way of programming,

**[00:02:41]** where I, to put it bluntly, talk a bit to the machine about what I want,

**[00:02:45]** and in the end end up with runnable code, runnable applications, runnable

**[00:02:52]** software, runnable apps that I can put in the store, just by

**[00:02:56]** messing around with the machine a little. This is the Jens Stanetski definition

**[00:03:01]** of Vibe Coding, Mark. At this point, we would need a jingle. Jens Stanetski defines.

**[00:03:07]** Yes, let me think, maybe something will come to mind. So, I mean, the point

**[00:03:12]** is vibe-coding, then some people come in saying vibe-engineering, because you need to give the whole thing

**[00:03:17]** a bit more context, we keep talking about context when we talk about prompting

**[00:03:22]** and I can share a bit from my insider perspective right now,

**[00:03:26]** so no worries.

**[00:03:27]** The company is not going to fall into some weird panic because I say something like this.

**[00:03:31]** I'll reveal something from the top-secret internet, I'm going to talk a little about how prompts work

**[00:03:35]** in the market and how they interact with the systems, and we had another nut to crack that

**[00:03:41]** we wanted to solve. And if you've been following the podcast, then you know, well, we always rave quite

**[00:03:47]** a bit about Grotkot and Entropik and the Opus models. And that's how my day started today. I worked a lot

**[00:03:54]** with Entropik and Opus. We implemented it over MS & Bedrock in relation to that. And that has

**[00:04:01]** everything is working wonderfully so far. But I had a nut that the software development

**[00:04:06]** had to crack, and I wrote, hey, pay attention, you need to do this and that

**[00:04:10]** the considerations. Yes, okay, I did that, then the AI tells me in nice smart words.

**[00:04:14]** I look at it. No, you didn’t. Yeah, okay, I’ll work on it again. Yes, okay,

**[00:04:20]** now I did it. Yes, it went back and forth a bit. And Clotcode with Opus was

**[00:04:25]** not helpful. And it was supposed to be, this is actually the powerful

**[00:04:29]** model. Yes, good. Now there’s a nice plug-in. You can say I want

**[00:04:34]** to include code from entropic models, in addition, for example, a review, so

**[00:04:41]** to have my code reviewed by Codex, Codex by the way

**[00:04:47]** OpenAI by the way has released version 5 of its language model

**[00:04:51]** maybe there’s some clarity on that; there’s a lot of what I would call

**[00:04:55]** naming confusions; normally the Codex model is the programming model.

**[00:05:00]** from OpenAI, unless you go in, it’s on a Mac, then the app is also called that, with which you
 
**[00:05:06]** can work, yes, but you can’t start Codex models and to double the complexity
 
**[00:05:12]** I just said, yes, I had basically Codex requests, so
 
**[00:05:17]** asking for help with code, I used the classic CPT, so the regular
 
**[00:05:22]** language model that any average user can also use via the web interface
 
**[00:05:27]** addressed, this new model didn’t have a specifically optimized version for programming yet.
 
**[00:05:32]**
 
**[00:05:33]** Long story short, Opus refused to solve my problem for hours.
 
**[00:05:42]**
 
**[00:05:43]** I take it personally.
 
**[00:05:44]** Then I installed the plugin, connected the Taughti model, and then came
 
**[00:05:50]** the sentence, so please do a review, what did it do, after 10 minutes left.
 
**[00:05:56]** And then you’re standing there thinking, wait a minute, I didn't take the programming-optimized models, I gave it a problem.
 
**[00:06:05]** Well, there were a few configuration steps in between, yes, because we also have at our company sometimes Bad Rock, sometimes GitHub Pro,
 
**[00:06:12]** yes, so Azure models, there is a colorful cosmos, I don’t want to go into that.
 
**[00:06:17]** I want to talk about the power of the models and you go into this other language model and you have the feeling,
 
**[00:06:24]** wait a minute, this feeling of, I’ve seen the light,
 
**[00:06:28]** not in the form of a near-death experience, but in the form of an enlightening moment
 
**[00:06:33]** in software development.
 
**[00:06:34]** That has happened to some as well, let’s say, with Codec by the way,
 
**[00:06:36]** that they have near-death experiences when they then bring something online
 
**[00:06:39]** and realize that they unfortunately forgot all your security issues.
 
**[00:06:43]** Can I say something about that too? Yes, I’m just in the rhetorical wall.
 
**[00:06:45]** Let me just briefly finish my thought.
 
**[00:06:47]** Yes, something Codecs then solved and I thought to myself,
 
**[00:06:50]** okay, let’s try out Codecs a bit,
 
**[00:06:52]** And then you mess around with Codex a bit and, well, long story short.
 
**[00:06:57]** Codex managed a lot of things, it also did a lot of things.
 
**[00:07:00]** I will say it again, a new approach.
 
**[00:07:02]** I’ll put it this way, brought in.
 
**[00:07:04]** And it was somehow funny to see that in your code the AI model from another provider,
 
**[00:07:10]** whether it addresses more, the machine does reviews and revisions for you
 
**[00:07:15]** and then looks at the code and says, oh, that’s a good idea, what happened there.
 
**[00:07:19]** Let's document it in ADRs, Architecture Design Records and then you stand there and do that or another event,
 
**[00:07:27]** that happened to me over the weekend. I also have Codecs privately at home. You always have to be careful
 
**[00:07:33]** with all the names. Everything starts somehow with C and everything is called somehow open and that’s
 
**[00:07:38]** terrible. So if I misspeak, it’s not a violation of any
 
**[00:07:42]** guideline, then I just got carried away in the alpha of the speed,
 
**[00:07:45]** that my brain is.
 
**[00:07:47]** That has nothing to do with us, Mark.
 
**[00:07:49]** That is just the manufacturer itself.
 
**[00:07:50]** If they set their names so closely,
 
**[00:07:52]** then we as an audience can’t be important at all.
 
**[00:07:55]** That’s all to express.
 
**[00:07:56]** Open Claw, Claw Bot, Claw Cod, Codex.

**[00:08:01]** So that's all really very, very close together.

**[00:08:05]** Now I can also really talk again.

**[00:08:07]** So no blame for you, Mark. Everything's good.

**[00:08:09]** Thank you. Thank you very much.

**[00:08:11]** I wanted to talk about the weekend, as I said.

**[00:08:14]** And I also had a little programming project, for those who checked it out on LinkedIn,

**[00:08:19]** we might talk about that later, the drill workflow, you didn't see that.

**[00:08:21]** You said, build me something, do something, and show me something, and I also said,

**[00:08:25]** no, it won't work. So it happens there too, it works. And then he says, no, no, you, it works.

**[00:08:29]** No, it doesn't work, yes, it works. So I'm sitting in front of the screen, I see that it doesn't work.

**[00:08:36]** And he goes, let me check, and then the dialog pops up on the Mac, the one,

**[00:08:41]** if you want to take control of your computer, screen sharing,
 
**[00:08:44]** keyboard sharing, accessibility, and you name it?
 
**[00:08:46]** And then the call I confirmed all this with started clicking around on my screen,
 
**[00:08:50]** clicking around in my application and he said, that's right, it's not working.
 
**[00:08:53]** I'll fix it.
 
**[00:08:54]** And then you're standing there and thinking, okay, that's quite an interesting experience.
 
**[00:08:59]** When you discuss with him, he doesn't believe you.
 
**[00:09:01]** He operates the computer and says, you are right.
 
**[00:09:04]** So those are small moments where you briefly think, holy moly.
 
**[00:09:10]** But vibe coding and vibe engineering, I also just mentioned vibe engineering.
 
**[00:09:14]** is more context, so I would also like to share something before I ask you about

**[00:09:17]** your art and vibe coding experiences question. There are, as I just mentioned,

**[00:09:23]** Architecture Design Records. Was it called Design Records? Never mind. Ah, the first thing, let's

**[00:09:28]** do it this way. Yes, so the Shornouts are written down, so in the heat of the moment at the latest

**[00:09:32]** hour. Basically, you write down why the system made its decisions and how

**[00:09:37]** we decided together and what the architecture of the offering is like and how

**[00:09:40]** certain modules are implemented and so on. And at some point, I started,

**[00:09:44]** including all my projects. If you look at GitHub, you can see that all my projects,

**[00:09:48]** which are included in ADS. Well, then I went ahead and said to him,

**[00:09:55]** pay attention. I would really like to build a new vibe coding app now

**[00:10:00]** and in my entire GitHub project, you will find all the ADS. Please take a look at them.

**[00:10:05]** and if you are developing a new app. He did that, he read through all the

**[00:10:10]** things and it was so many aspects where he might have otherwise had a

**[00:10:15]** follow-up question. Or what do you mean by your tokens for

**[00:10:20]** Open AI? Yes, wouldn't you want to provide, I don’t know, these and those models,

**[00:10:25]** for selection? There are also voice models, should you have those available,

**[00:10:29]** blah blah blah. I have already answered all that chitchat with historical projects.

**[00:10:33]** He didn't ask me about that anymore. That was done for him. Yes, and then I thought,

**[00:10:39]** this might be a little bridge after my speech failure. You should really

**[00:10:44]** consider writing down the things you do in your professional environment. Write

**[00:10:50]** down what you do. So a sequence, we had that topic with René, it applies. But

**[00:10:55]** also write down why you made certain decisions and save that

**[00:11:00]** in a separate document? Yes, I mean ADL, in the software in the way, that is one.

**[00:11:04]** Maybe you will find some other reason why you are in service design at a

**[00:11:09]** Design decision, could you maybe help me if there's something similar?

**[00:11:12]** Write it down and then don't write it down in Word or Excel, but

**[00:11:18]** nicely in Markdown, so you have something at hand for when you deal more with AI,

**[00:11:22]** if you're already dealing with AI and think you have something at hand,

**[00:11:27]** that the system can consume and not just say, here is the folder,

**[00:11:33]** where I've structured it. You can also ask the AI to check if it's consistent,

**[00:11:37]** if it goes to sheets, if there are contradictions and continuously improve yourself this way. It's not a

**[00:11:43]** disgrace that you don't know everything yourself anymore. Yes, I notice it increasingly with age,

**[00:11:49]** that I don't know everything myself anymore, and that's why the note is very

**[00:11:53]** good. I also start writing things down to your question, of course, designer. We naturally decide everything from our gut and just move pixels around all day. You know that? Yes, you like it.

**[00:12:04]** I have a very urgent thing. I just looked, I really have to, it's really too late. Yes, I will do the Fuzzle check for the current episode immediately.

**[00:12:11]** Yes, ADR does not stand for Architecture Design Records, I was almost certain it could

**[00:12:16]** not fit, yes.

**[00:12:18]** Architecture Decision Records fits much more with the content, so all those who

**[00:12:23]** have already switched off because of incompetence, please call now, so they can remember

**[00:12:27]** it.

**[00:12:28]** James, you wanted to tell something?

**[00:12:29]** I still wanted to mention a bit, also directly in this episode, because I have

**[00:12:32]** just received that directly, and namely, it was said by Kapafi in February

**[00:12:38]** and not in autumn 2025. So the term Weibkoding has existed since February 2025. With that we have

**[00:12:44]** also already resolved it directly and do not need to wait for the next episode. Weibkoding. Yes,

**[00:12:49]** I have just mentioned it. Of course, what Mark said is a meaningful topic,

**[00:12:53]** that we write down a lot of things so that we have them later in Weibkoding as a bit of a guide

**[00:12:57]** when we want to proceed in a structured way and not just want to say into the machine

**[00:13:02]** let's finish it. Still, there are a few situations where we do

**[00:13:07]** finished extremely good and astonishing results. I have to say that again and again.

**[00:13:12]** I once created a small application with Nanosei. It needs a

**[00:13:18]** photo recognition solution for that, a calendar connection. And I actually just made two Proms

**[00:13:24]** sent because I made a typo on the first mistake. Then I stopped the Nanos again

**[00:13:28]** in production and with the second prompt, where I was a bit more specific still

**[00:13:33]** there was something I wanted, because I had another idea come to me, so I had started

**[00:13:36]** to solder it up and after five minutes I had a really basic application that I could test

**[00:13:42]** could, which had an OCR recognition, which had a query lock-in where I was with

**[00:13:48]** I was able to connect to my own account with Google and then I was logged in. That was pretty

**[00:13:52]** awesome, I must say. So all the features I wanted were exactly

**[00:13:55]** The design was a standard AI design, so they could have put in a bit more

**[00:13:59]** effort.

**[00:14:00]** But it really went from an idea that had formed somewhere to being

**[00:14:08]** prompted into the application, and five minutes later having a working version.

**[00:14:14]** This is actually already, without me doing anything in that direction

**[00:14:17]** and therefore I wouldn’t have brought the thing online, so first I would

**[00:14:21]** make a Research & Development Plan or something and do at least a

**[00:14:24]** Yes, I didn’t do that, but I just wanted to try out if this

**[00:14:29]** vibe-coding works the way I imagine it, and it works.

**[00:14:32]** You can really produce things at an insane speed, I would

**[00:14:39]** before I put something online like this, and just as a small marker, I would say, yes,
 
**[00:14:44]** one should continue to handle it as if when I don't know how to unplug it,
 
**[00:14:50]** I should maybe ask someone else.
 
**[00:14:52]** Well, that means if everything isn't quite clear to me about what happens in such software that I built,
 
**[00:14:56]** especially when I'm working with user loading and such, then I should see,
 
**[00:15:00]** that I either maybe ask someone else or let another AI run over it,
 
**[00:15:04]** take a bit more time and not just say, I can somehow launch a super smooth application with two proms,
 
**[00:15:08]** that we can then just leave completely out in the world.
 
**[00:15:13]** I would still be a bit careful about that.
 
**[00:15:15]** I think that has improved.
 
**[00:15:17]** But I believe one should still be cautious, especially when actually
 
**[00:15:24]** working with user lock-in maybe, especially if one also has the idea that customers enter their
 
**[00:15:29]** bank details differently each time, although there are definitely more applications now, there are
 
**[00:15:32]** also some MCP servers for Stripe or other things for payment service providers,
 
**[00:15:35]** that you can also connect things to quickly, but one should
 
**[00:15:38]** actually have at least a basic understanding of what
 
**[00:15:43]** needs to be done, what security settings I then need to make and what,
 
**[00:15:48]** things does the AI also need to pay attention to, so that it’s secure in the end and not just handled carelessly.
 
**[00:15:52]** That's also a point, I mean, it makes it all sound clever, cheeky, and it claims
 
**[00:15:57]** things that if you ask follow-up questions, it credibly tells you a few things about it, yes, then again a few
 
**[00:16:03]** anecdotes and maybe some guidance. Anecdote 1, I was supposed to have
 
**[00:16:08]** worked a bit more on a project than I actually intended. The next

**[00:16:14]** In the morning, a developer greeted me with a sentence and a meme image where the gardens

**[00:16:19]** of Asgard were flooded because the gates of a river were torn open, with the

**[00:16:25]** small comment, oh, Mark has released a three-digit number of commits. It just happens.

**[00:16:34]** The second one is also very nice, when you're working with vibe coding and you find yourself,

**[00:16:39]** you put in the effort, right? And say, okay, pay attention to security and you might also have a

**[00:16:43]** few skills for security, it's also a little recommendation, look for some libraries on the

**[00:16:46]** web that ensure you're already thinking about the basics. Yes, there are

**[00:16:51]** skills for security checks, skills for clean code architecture, so also architecture and skills

**[00:16:56]** for documentation. Get something like that. It might sound at first like,

**[00:17:00]** Yeah, come on, he already did it, but this is no nonsense, because, let's say, he tells you a lot and you need someone every now and then to critically counter or to ask him to document things.

**[00:17:14]** There will be a few listeners I know, greetings to Simon, tearing their hair out.

**[00:17:18]** What?

**[00:17:19]** Documenting SOSCO?

**[00:17:20]** The truth is also in SOSCO, in the times of AI.

**[00:17:22]** Yes, the truth is in SOSCO, documentation could certainly have drifts

**[00:17:26]** arise, where somehow things that are in the code never make it into the documentation,

**[00:17:31]** that the system has created on its own, that can happen,

**[00:17:34]** there are a few procedures you can undertake, but what I really want

**[00:17:37]** to get at is, you really have to look at what it does, because for example

**[00:17:41]** there come out some nice floral expressions, like,

**[00:17:44]** Hello, dear AI model,

**[00:17:46]** are all the errors gone now?

**[00:17:47]** And it tells you,

**[00:17:48]** no,
 
**[00:17:49]** there are still five,
 
**[00:17:50]** but
 
**[00:17:51]** not my problem, that wasn't me,
 
**[00:17:53]** that's from another session.
 
**[00:17:54]** I'm already free,
 
**[00:17:55]** all of mine are flawless.
 
**[00:17:57]** That stank, wonderfully.
 
**[00:17:59]** They were completely his,
 
**[00:18:00]** yes, but he somehow thought,
 
**[00:18:02]** that was once, I don’t know,
 
**[00:18:03]** Another day, Another commit, Another something.
 
**[00:18:05]** And he meant he didn’t have to
 
**[00:18:07]** worry about the flawlessness of the code,
 
**[00:18:09]** because from his perspective, it didn’t come from him. Where I then think, what kind of procedure is that?
 
**[00:18:14]** If I tell you to tidy up, I mean, I know people, when I tell them that,
 
**[00:18:18]** they say to me, I didn’t throw that, I don’t collect that.
 
**[00:18:21]** So from that side, what is that please, for an AI? So, that’s one thing.
 
**[00:18:26]** And the second. Yes, but that brings me to the second point. If he says it’s safe,
 
**[00:18:33]** always ask a critical follow-up question. So I’ve now also written a
 
**[00:18:37]** skill, yes, again promoting my GitHub project, in which I basically
 
**[00:18:42]** write down what a function is supposed to do or I’ve written a script that’s supposed to check
 
**[00:18:47]** what the goal is and then check what could have gone wrong if I don’t
 
**[00:18:53]** achieve this goal. So I tell it, for example, I want our podcast to
 
**[00:18:56]** be in the top 10 by the end of the year and then it says, yes, okay, look, that’s now
 
**[00:19:02]** the end of the year, you’re not in the top 10, what went wrong and
 
**[00:19:06]** tries to analyze retrospectively what could have been a failure? That’s quite funny,
 
**[00:19:10]** not just because I find it entertaining. It’s also quite funny,
 
**[00:19:13]** when you apply that to Sourceboard. But I want a secure sandbox in
 
**[00:19:17]** my application. I want a secure lock-in mask. I want a clean
 
**[00:19:20]** corn send. I want no idea what. Then the poet actually brings you new ideas.
 
**[00:19:25]** And if you then tell him, okay, he doesn’t just say the failure in the time,
 
**[00:19:30]** that’s why you didn’t achieve it. He also says why it went wrong and
 
**[00:19:33]** what you could have done about it. And you can throw that back in the loop and say, so,
 
**[00:19:37]** pay attention, my friend, did you think about that? Ideally, he says that if there is such
 
**[00:19:43]** a security thing, when he says here, the data you don’t want to enter,
 
**[00:19:46]** that they are secure, that’s a very blunt sentence now, then he says, of course, they are
 
**[00:19:50]** not secure, they were leaked after six months because you didn’t encrypt them and
 
**[00:19:54]** you didn’t do this and that and the other. And then he gives that to him and says, look
 
**[00:19:58]** for that. Did we do that? And he sometimes says no, but he also often says yes.
 
**[00:20:04]** And it doesn’t matter that he finds something where he says yes, that’s nice calming. The points,
 
**[00:20:10]** where he says no, those are the points that let you sleep peacefully, because he has
 
**[00:20:14]** now basically picked that up again. And I’ve really gotten used to
 
**[00:20:20]** saying every evening, when I’ve yelled at the machine,
 
**[00:20:25]** to build something for me, that it writes down what it did to achieve that critical

**[00:20:31]** Critics, the creative critic, which he expresses, I might get from it under circumstances

**[00:20:35]** introduced for the next day, and that would be one tip, and the second

**[00:20:40]** tip is, I need to look in the mirror myself, don't get a, if you are private

**[00:20:46]** coded model, which, let's say like at Entropic, Max 20 is. Max 20 is for

**[00:20:52]** the wealthy, yes, we heard recently that Jens with his open client situation

**[00:20:56]** now heard about the multimillionaires and simply out of goodwill and generosity

**[00:21:02]** treats us here every Monday.

**[00:21:03]** But he recently gave an explanation as to why it is totally good that you don't have the maximum

**[00:21:09]** of a plan.

**[00:21:10]** Work-life balance.

**[00:21:11]** If you have a system that forces you, I now depart from the private environment, yes,

**[00:21:18]** so my workplace's working time protection law, and you haven't seen it, but personally swings,

**[00:21:22]** that you somehow have to take a break, then you have a reason to say goodbye from the screen.

**[00:21:27]** Because I notice it too, it slightly serves the endorphins of your brain, from the successes of your Prometheus.

**[00:21:35]** You write and you don't discover new worlds, who thinks immediately functions, UIs, they are.

**[00:21:42]** So we should briefly clarify, I believe what you mean by Max 20, please clarify down here.

**[00:21:46]** Exactly, that you mean with Max 20, is basically that you can burn very, very many tokens.

**[00:21:52]** Before the stop sign is pulled, because your internet is also needed, exactly.

**[00:21:56]** That is another important addition to make it clear.

**[00:21:58]** Excuse me.

**[00:21:59]** So right now there is a bit of a topic that you see, that what the

**[00:22:05]** market is currently describing has a certain addictive factor, simply that many people who create something,

**[00:22:10]** whether it's all topics around generative eggs, not just codec,

**[00:22:14]** video generation, image generation, you get incredibly good results very quickly everywhere,

**[00:22:22]** which brings you into a certain kind of flow, wanting to do more. And I'm not quite sure now

**[00:22:29]** if the rate limit you have is the only factor, because

**[00:22:34]** if it naturally always carries the risk that you buy more and say to yourself. But somehow,

**[00:22:37]** yes, of course, it is a bit like that, the AIs, because they are also designed that way,

**[00:22:42]** of course I also want to keep pushing, and I've mentioned this in one or the other episode already

**[00:22:46]** more often. I have my personal open cloud installation set up. This is because of

**[00:22:51]** its soul-MDs, the files that describe a bit how it should behave.

**[00:22:55]** So far it checks what time of day it is pretty regularly

**[00:22:59]** and also based on the time of day, then closes. Now it’s slowly coming to an end, Jens,

**[00:23:04]** time for bed. That means there is already a bit of a factor that you can also

**[00:23:09]** teach the AI. So not only because the money may have run out,

**[00:23:11]** because you didn't pay API costs or reached the rate limit at some subscription,

**[00:23:16]** be it with video generation, text generation, code generation, or also what you

**[00:23:20]** do, but that you can actually advise it as well. I think you can reflect on a lot

**[00:23:25]** here. We’ve now talked about it, write down what is important in

**[00:23:28]** the work process, write down what decisions, decision records, I have to repeat that in,

**[00:23:35]** pay a little attention to your time, how you work with the systems. That means,

**[00:23:40]** at first trust yourselves, but when you are deeper in, give yourselves a break, because it makes you

**[00:23:47]** already feel somewhat sluggish if you code there the whole day. It is indeed a great feeling, I must

**[00:23:52]** honestly say, I’ve already lost track of appointments and time more than once, let's say

**[00:23:56]** not because I got lost in some game,

**[00:24:00]** but in a, yes, actually a game. Just that in this game, it's partly about

**[00:24:05]** productive solutions, partly experiments, partly about shared learning. It brings

**[00:24:12]** people back together. We sit so often, as we said since Vibecoding,

**[00:24:16]** never together in personal or remote meetings looking at the same screens

**[00:24:20]** and have talked and learned from each other. Those are all cool things. But where I still

**[00:24:28]** wanted to go, what I absolutely want to get across in this episode, is also the point,

**[00:24:33]** of not exposing oneself and thinking, oh damn it, that’s just a text window.

**[00:24:38]** And no matter what it’s called, yes, Langdog and Entropic and Open AI and Gemini and whatever else it’s called,

**[00:24:44]** it may also be good that at some point you have to accept a solution

**[00:24:50]** or should or can that doesn’t look like these classic windows, whose biggest

**[00:24:57]** problem is the power you have with them because they can literally do everything, yes. You can

**[00:25:01]** just write programs with these chat fans, analyze documents, do research,

**[00:25:06]** be fooled, create poems, I don’t know, maybe some solutions are also appropriate,

**[00:25:13]** depending on who you want to focus on in the work context. If your only,

**[00:25:19]** only is not meant derogatorily, but if your job is to create slides,

**[00:25:24]** then your job is to create slides. And maybe you create two or three other types of documents,

**[00:25:28]** but you’re not doing the meal plan, the research around the world, which, I don’t know.

**[00:25:33]** Yes, that may be a silly example, but maybe it’s still clear what I mean.

**[00:25:36]** It can also be beneficial to use applications that are specifically tailored to this case,

**[00:25:42]** so you don’t get lost in usage, so that you have an onboarding,

**[00:25:47]** in the form of, I trust the system that you say what you might say.

**[00:25:52]** Hey, I think that’s an important…

**[00:25:54]** can’t, not lose. That when I press Ender, not five million costs

**[00:25:59]** lying on the table of the house, my plate is empty and in the end the email from the system

**[00:26:03]** gets sent, they may be trained. There too we will certainly have to reinvest more

**[00:26:09]** have to, also offer people environments, not because they are stupid, not because they

**[00:26:14]** can’t learn, simply undermine, but also because they do not need it and

**[00:26:20]** because they might have something else.

**[00:26:22]** I'll say, if you're beating nails into the wall all day long,

**[00:26:26]** nobody is going to park an excavator at your door.

**[00:26:28]** What, you watched so much Wetten dass,

**[00:26:31]** where probably at some point in some episode a digger...

**[00:26:33]** Watched a lot of Wetten dass. 

**[00:26:34]** Excavators, as it was, that have beaten the profits.

**[00:26:38]** But I know what you mean.

**[00:26:39]** So, what you’re saying is,

**[00:26:41]** that we use the right tool for the right purpose

**[00:26:44]** and for the right task we have.

**[00:26:46]** That has always been part of human wisdom and our human capabilities

**[00:26:54]** to choose the right one.

**[00:26:55]** I believe that sets us apart and that’s not

**[00:26:59]** different in today’s time.

**[00:27:00]** So it’s not necessary for everyone to use the hardcore auto-complete AI tool

**[00:27:05]** because they are so familiar with things in their profession that they also

**[00:27:08]** code in a way that nothing bad happens.

**[00:27:11]** Of course, that should remain in the hands of those who have knowledge of programming.

**[00:27:17]** On the other hand, we have a bit of vibe coding in this episode.

**[00:27:21]** What is that actually called? The ability to say what you just said,

**[00:27:25]** is another aspect of learning, of collaborative learning.

**[00:27:29]** And I believe that is something you can still do well.

**[00:27:31]** So once you dare to tackle this topic, there are also various solutions.

**[00:27:34]** We have just talked about all the big model providers and such.

**[00:27:38]** There are of course also regulators out there, like Bolt or Level Belt or such topics,

**[00:27:44]** where I can also design a bit based on the interface, so that the models in the background,

**[00:27:50]** I can build applications a bit more easily, so to speak.

**[00:27:53]** And I think that's something you can just try out a bit as a beginner in white coding.

**[00:28:00]** I think that is the important thing, learning how programming actually works.

**[00:28:06]** And then perhaps also letting young people experience it themselves, as you say, either until they reach a point

**[00:28:10]** where you say, then the complexity just becomes too great, you had

**[00:28:14]** just a bit with the idea that people might simply not need it.

**[00:28:18]** I would always say, at a certain level of complexity, you just need a deeper

**[00:28:21]** To have a profession in order to perhaps manage the technical complexity that can arise from

**[00:28:25]** code, software development, and software deployment, as well as the responsibility

**[00:28:29]** regarding operation and security and such.

**[00:28:31]** Comes, this is indeed a principle, a professional responsibility that exists, a profession,

**[00:28:35]** learned at that moment. I believe this is a natural boundary that one can set for oneself.

**[00:28:40]** For example, I will not start becoming a chef or something like that now,

**[00:28:43]** just because I didn't achieve anything three times in a week, or something like that, a star, a restaurant to

**[00:28:47]** take over, I'm going to fail terribly. Accordingly, I think we then have

**[00:28:51]** a pretty good feel for it, but also dare to tackle things. So just pick a tool,

**[00:28:57]** choose one, ask not just us, ask your Gemini or something else,

**[00:29:03]** something that can still be done well. Maybe let it slip a bit while doing this. Look a

**[00:29:07]** little, the AI can help you with that. It likes to do that. It will describe to you

**[00:29:13]** there, what happens. I don't have an example. Sometimes you just have to remind them

**[00:29:19]** again. Sometimes she forgets that too, nicely every once in a while,

**[00:29:22]** to do that. But remind them about it or create a skill that you deactivate.

**[00:29:26]** There are already a few episodes from us on how to do that. Or also order

**[00:29:30]** there, that together with AI, that's already a bit, I know, also

**[00:29:34]** a kind of programming, when you create a first skill, even if it’s not a

**[00:29:37]** classic programming language in the background. But you delegate something. That’s

**[00:29:41]** a bit like what you often do in programming, saying that certain functionalities

**[00:29:45]** I delegate to another place. You do something similar when you describe a skill with

**[00:29:50]** an AI, and this skill then has to come from your own AI. Then

**[00:29:53]** that’s already a kind of, now many IT specialists are probably listening, Steining.

**[00:29:57]** want, but that is already a kind of programming.

**[00:29:59]** We know where Jens lives and I am for sale.

**[00:30:03]** Now that you mentioned outsourcing and that one can do a lot there

**[00:30:08]** many things, here's a story from life and something fitting for the podcast.

**[00:30:12]** The story from life was that I used to think Philips U-lamps

**[00:30:19]** are really great and I got various things from Philips U, motion sensor

**[00:30:24]** in the house, lights. The whole house is filled with Philips lights, yes. And the basement has motion detectors

**[00:30:29]** from Philips. And at some point, I regretted buying Philips lights because

**[00:30:34]** the motion detector in the basement has the property that when it detects movement

**[00:30:39]** it turns the light on, then keeps the light on for the time you've defined

**[00:30:42]** and then it goes off. And if you walk by in between, the detector

**[00:30:46]** picks it up, but it doesn't matter. The counter is not reset. I

**[00:30:50]** was a bit frustrated by that. At some point, in a bubbly mood, many years have passed now,

**[00:30:54]** I told my problem to Claude, because I thought Claude could

**[00:30:59]** possibly research if there’s something out there. And then we exchanged a few messages

**[00:31:03]** and then fingers on, so to speak, please press your Philips button now

**[00:31:08]** on your Philips View. And then you go to the Philips View, press the button and

**[00:31:12]** then say, Claude, well, I connected to your Philips View, what do we

**[00:31:15]** want to do now. And then he taught my motion detector in the basement that the light

**[00:31:20]** stays on. And then you stand there and think, that function wasn’t even present in Philips U.

**[00:31:25]** He somehow showed himself through and managed to get that done and you stand

**[00:31:30]** there thinking, in the end. So now I might have discussed a bit too much with Chad

**[00:31:34]** and so on. But actually, I just improved my smart home with language. Whether that is something my

**[00:31:41]** father-in-law can handle. Father-in-law, if you're listening,

**[00:31:43]** nothing against you. At this point, please insert anyone from the family or acquaintances.

**[00:31:48]** Smart home is always somewhat of a pain when you have a mix of providers.

**[00:31:53]** So Apple, HomeKit and Philips U and ZigBee and HomeKit, in the end you are overwhelmed.

**[00:31:59]** But then suddenly you have a way that takes the complexity away from you.

**[00:32:03]** That was one thing. And the second, I will definitely link it in the show notes,

**[00:32:08]** because we don’t have a nice domain yet. We also have a Vibecoding project,

**[00:32:12]** which is currently starting, namely a page that is hosted on GitHub.

**[00:32:17]** On which the transcripts hopefully also the better transcripts, because those are the

**[00:32:23]** transcripts of our podcast episodes have been done by Podigy, our podcast-

**[00:32:27]** hosting system, which I still have to change, but we have a little

**[00:32:32]** page Vibecode that shows the episodes from the past, it will always

**[00:32:38]** automatically update, then you will find the transcription

**[00:32:43]** of all episodes, you’ll find a web player over there, you can also switch to English,

**[00:32:47]** though that doesn’t belong to us in English, but you’ll get the transcripts of our episodes

**[00:32:51]** in English. It has a few mechanisms, including a feedback form, so you can

**[00:32:57]** write to us. You can search, you can share episodes, but you can also, if you don't care about

**[00:33:03]** all the hackiness and prefer to go into the topic that

**[00:33:07]** I mentioned at the beginning, write down what you are doing, make your Tizen. You can also download all

**[00:33:12]** episodes in German or English as marked versions if your LM systems want to indulge in

**[00:33:19]** what we’ve done cool here. Jens, I have nothing more, I am actually

**[00:33:24]** done for today, I was able to bring a lot of anecdotes, I did kind of fumble the beginning

**[00:33:29]** of the episode, hopefully redeemed myself by the middle of the episode. Do you have anything else,

**[00:33:34]** and I would be really out of it. I think I’m also about done, aside from wanting to repeat

**[00:33:40]** that you don’t, Vibecoding does not have to be for you to create the next new super app

**[00:33:46]** or something else. It may just be...

**[00:33:48]** If so, then please send the Hemen to the one pinned below.

**[00:33:51]** No, oh so sad. But, you know, you also do the small things, look for the small

**[00:33:55]** Solutions you need. Here, this was mentioned recently. I have

**[00:33:58]** also built a PDF compressor somewhere just to compress things.

**[00:34:03]** So often you have little tasks you want to automate, where

**[00:34:07]** you need a small piece of software, you can always consider, can I

**[00:34:11]** not try this again? Or do I have any use cases at home,

**[00:34:15]** that I repeatedly do, tasks that I constantly have to sort,

**[00:34:21]** documents, invoices, or something else? You can play around a bit with code,

**[00:34:26]** see what works. Can I play around with Geminal to automate something,

**[00:34:30]** maybe to capture my emails, or something else. In the end, it's

**[00:34:34]** kind of art. I would say interacting with the computer. It's not always direct

**[00:34:38]** Programming in the sense that a piece of code is somewhere, which also includes the Plurio

**[00:34:42]** could be something else, but it can also be a workflow that he puts together for you.

**[00:34:46]** Just go for it and try things out, because I believe that's what we wanted to convey in this

**[00:34:50]** episode. The topic of AI isn't going away. It's fun to engage with it.

**[00:34:56]** That has its challenges, but don't let yourselves be intimidated into thinking that it somehow,

**[00:35:01]** if you do something there, the whole world comes together, but look, there's enough stuff where

**[00:35:06]** you can try things out, where you can test yourself.

**[00:35:08]** Mark is laughing again, that means he actually has something.

**[00:35:11]** I'll say already, see you next time.

**[00:35:12]** Wasn't that Marco for the dearest time?

**[00:35:13]** Whoever wrote a book, as the attacker, turned off the internet next to grandma or

**[00:35:17]** something like that, if I quoted that wrong, he could tell me, maybe

**[00:35:21]** Marco link our previous episode, I actually know him through his,

**[00:35:25]** well, I don't know, no, I have already dealt with the Kengerokroniken and such

**[00:35:28]** stuff.

**[00:35:29]** With that, we digress.

**[00:35:31]** I also heard his opinion on AI recently at some talk at the Chaos Computer Club,

**[00:35:35]** because now, let's say, it's difficult for freelance artists in general, but I understand that, of course.

**[00:35:41]** Jens, it was nice that you are here. We started the episode with the sentence,

**[00:35:45]** that we are recording a second episode today.

**[00:35:47]** We are going to do that now as well. Our guest will be here shortly.

**[00:35:50]** First, I need to quickly charge my battery.

**[00:35:51]** In this sense, wish you all a lovely evening, a nice day,

**[00:35:55]** a great week, we'll hear from each other soon, and feel free to leave us a comment, and see you soon, bye.

**[00:36:01]** See you soon, bye.

**[00:36:04]** Welcome to ThinkDifferent, ThinkAI, the podcast by Mark and Jens.

**[00:36:09]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:36:16]** Here you will find clear classifications, real practical insights, and a fresh look at what is possible.

**[00:36:23]** Understandable, critical, and always with a wink.

**[00:36:27]** AI for thought, for a chuckle, and above all, for discussion.
