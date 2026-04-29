---
title: "Agenten, KI und die Zukunft der Softwareentwicklung"
episode_index: 33
published: "Mon, 30 Mar 2026 16:08:00 +0000"
duration: "3602"
audio_url: "https://audio.podigee-cdn.net/2417572-m-91adb6cd7036afc5e7400bf4fa464a7b.mp3?source=feed"
guid: "a8303674a67fc2aa99fd4811c1816e7d"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T21:06:26+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/033 - Agenten, KI und die Zukunft der Softwareentwicklung.md"
translated_at: "2026-04-29T14:46:17+00:00"
---

# Agents, AI, and the Future of Software Development

**Published:** Mon, 30 Mar 2026 16:08:00 +0000
**Duration:** 3602
**Audio:** https://audio.podigee-cdn.net/2417572-m-91adb6cd7036afc5e7400bf4fa464a7b.mp3?source=feed

## Description

How agentic workflows and AI are revolutionizing our way of working – with real examples, mishaps, and a look into the future.
In this episode, we dive deep into the world of agentic software development. Together with my guests, we discuss how AI-supported workflows are changing our understanding of programming, teamwork, and security. We share genuine experiences, stumbling blocks, and surprising learning successes – from automated accounting processes to the challenges of integrating AI agents into existing systems. Of course, we also critically examine risks, security, and the changing role of developers. In the end, the question remains: How do we prepare ourselves – and our teams – for this rapid transformation? Anyone curious about what the next generation of software development truly looks like should definitely tune in.

Craft Agents
https://github.com/craft-ai/craft-agents

OpenClaw
https://github.com/openclaw/openclaw

Cloud Code
https://cloud.google.com/code

Adam Shostack – Four Question Framework
https://adam.shostack.org/four-questions/

Obsidian
https://obsidian.md/

Notion
https://www.notion.so/

FFmpeg
https://ffmpeg.org/

Microsoft Copilot
https://copilot.microsoft.com/

Jira
https://www.atlassian.com/de/software/jira

Kotlin
https://kotlinlang.org/

Swift
https://developer.apple.com/swift/

Xcode
https://developer.apple.com/xcode/

Xcode Cloud
https://developer.apple.com/xcode-cloud/

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two tech-loving minds who don't just talk about artificial intelligence, but live it.

**[00:00:14]** Here you will find clear classifications, real practical insights, and a fresh take on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** AI to ponder, to chuckle at, and above all, to discuss.

**[00:00:33]** A warm welcome to ZinkDiffin, ZinkAI.

**[00:00:36]** Today without Jens, but again with strong support.

**[00:00:40]** We had the guests Schommal with us before.

**[00:00:44]** Back then, what did we talk about?

**[00:00:47]** Man, the world is so fast, I almost forgot.

**[00:00:50]** But I'll link it in the show notes, you can check it out.

**[00:00:52]** Something about AI.

**[00:00:54]** I'm also doing something with AI.

**[00:00:56]** Nice voice in the background already heard. Yes, Alex and Klaus are here. Tell us briefly

**[00:01:01]** who you are, and then let's dive into the topic of agentic software development.

**[00:01:07]** Let's see where the journey takes us today. Yes, hello everyone. I’m still Alex.

**[00:01:13]** I work at a well-known German company dealing with platforms and AI and

**[00:01:20]** ways of working, exactly. And I got in touch with Mark and Klaus because of that.

**[00:01:27]** I think it’s nice, when he said hello, I thought that’s just like a 

**[00:01:31]** welcome group, like a self-help group, right? Hello Alex, hello Mark, yes, hello to the

**[00:01:36]** dogs. Well, it's a bit like that, isn't it? Yes, maybe we should change the podcast

**[00:01:40]** format, but alright, Klaus, you're up. Yes, I'm Klaus, I'm a

**[00:01:45]** colleague of Alex, which is sometimes funny and sometimes makes you cry. But that's not just because of me in a company that brings out a wonderful kitchen machine, and I spend most of my working hours making sure that this kitchen machine isn't hackable, and the rest of my working hours I spend with AI in software development, and that's why I'm focusing a bit on the topic we chose today, 

**[00:02:14]** the topic of agents.

**[00:02:19]** in the field of software impact, I know, but I always stand in awe when Alex shows me,

**[00:02:24]** what F4 workflow implements with agents and you also like. That's why I'm really excited and curious,

**[00:02:30]** if I can learn something today. I think we all learn something and that's what is

**[00:02:34]** nice in this small circle. We are here in cozy togetherness, not because everyone is

**[00:02:40]** was sent out as a representative of his company,

**[00:02:44]** but because we personally engaged with the topic itself

**[00:02:48]** feel connected to the whole topic of, yes, what AI throws at us over the fence.

**[00:02:55]** And you just hinted at it, like, what you can do with

**[00:02:59]** workflows and so on. I don't know how it is for you, but if someone had

**[00:03:03]** asked me half a year ago what the cool hot

**[00:03:06]** stuff is, to put it bluntly, I would have told you some fairy tale

**[00:03:09]** tells how the notes were interconnected back in the day to build some

**[00:03:16]** interesting workflows. When I look at my N-Nacht-N profile today,

**[00:03:22]** then it's, let's say, not empty, but very neglected, because it's, well, not in line with the

**[00:03:30]** motto, neglected, in the sense of being forgotten like a messy scene and unshaven, so please no

**[00:03:34]** image associations in your mind to keep, but I just haven't been in there for ages.

**[00:03:41]** I recently logged in again to extract a bit of the Jason stuff,

**[00:03:45]** what was in the other workflow, because I wanted to transfer that from Claude Code to skills and so on.

**[00:03:52]** But I didn't really maintain that. You guys don't really care about the
 
**[00:03:57]** technology anyway. So do you still use what you considered Holy Shit three or four years ago?
 
**[00:04:03]** Or has that changed as well?
 
**[00:04:06]** No, I actually don't anymore, but we already talked about that recently.
 
**[00:04:11]** Well, to be honest, I don't know anyone who isn't overwhelmed by the speed
 
**[00:04:16]** of it all. So we mentioned that, I mean, we said that in the last podcast,
 
**[00:04:21]** everything is changing so quickly that you have no chance
 
**[00:04:26]** of really becoming an expert in a newly emerging technology. Unless
 
**[00:04:32]** it's something that really establishes itself as a base technology.
 
**[00:04:37]** That means we really have to approach things with the mindset that I know I don't know.
 
**[00:04:44]** And sometimes that's really exciting because I learn something new all the time.
 
**[00:04:51]** And sometimes it's massively frustrating; you brought the N8N example
 
**[00:04:55]** and you use, I don't know, Gemini, to transfer an N8N workflow into a skill
 
**[00:05:03]** and at first you think it looks really good.
 
**[00:05:05]** And after two weeks, you realize something is off and oh yeah, okay, that part
 
**[00:05:10]** I just completely left out, but I'm only realizing that now.
 
**[00:05:14]** That didn't look so important, right, until you hear it.
 
**[00:05:20]** I had someone recently who said, I told the agent, you do this until all tests are green, and gave him about eight, nine, ten tests.
 
**[00:05:29]** And the agent did it, the agent said it's green. And then, it doesn't work at all. And looked after that.
 
**[00:05:35]** And out of the ten tests, only nine were left because the one that didn't work was simply deleted, a bit hastily.
 
**[00:05:42]** So on that side, that's obviously both a blessing and a curse when you differentiate between, I built a workflow and then somehow sent off a few skills.
 
**[00:05:49]** Klaus, how about you? Now comes my standard objection. What's the difference to

**[00:05:55]** non-agent programmers? And I wanted to add to your question, Mark, sometimes it helps,
 
**[00:06:03]** not to be so quick. I know that you fully embraced NNN in the fall and I
 
**[00:06:10]** couldn't keep up because I just didn't have enough time and I'm quite glad now,
 
**[00:06:15]** that I didn't take that detour, because obviously I haven't missed anything,
 
**[00:06:18]** that's just technology from 20, 25 I've learned. I'm not going to look at that old stuff now

**[00:06:23]** more. Now it’s moving forward. You can always learn something from it, when we looked at the end of January

**[00:06:29]** OpenClaw. So I learned a lot about the patterns that you have been looking at

**[00:06:36]** today, yes, in most of the examples now, in Harnes, that is to say in things like Cloudcode or

**[00:06:45]** or OpenCode, or even now in the stable versions of OpenClaw. That

**[00:06:53]** are patterns, that’s what I meant by base technology, which has then somewhat established

**[00:06:58]** itself and can really be found in each of these Harnaces now. One knows, of course,

**[00:07:05]** already mentioned, Mark, with the skills, plugins, hooks, but also these evaluations.

**[00:07:12]** I think, if I may just interject, yes, of course it’s never forgiven love music

**[00:07:21]** to deal with something, but as you said at the beginning, Alex, the wheel is turning

**[00:07:25]** so fast now that I already think one needs to focus on a topic

**[00:07:30]**.

**[00:07:31]** That's why I'm now focusing on the topic of software development and I'm really curious

**[00:07:36]** about it.

**[00:07:37]** So I asked you last week already, this is an interesting focus.

**[00:07:41]** I already asked you before. I have a standard use case. For my company, I have to compile once a month

**[00:07:47]** for accounting. They come via email, these are like Office 365 and all those subscriptions, but invoices come via email.

**[00:07:56]** I have to reconcile them with a bank statement, I need to compile them structured in PDF and then send them out.

**[00:08:02]** I would imagine that I can do that wonderfully with an agent and some skills,

**[00:08:07]** Since I haven't dealt with it yet, as I'm currently just programming, my question would be now

**[00:08:12]** how can I approach this topic?

**[00:08:15]** Because I believe we already mentioned in the episode where we were last guests,

**[00:08:19]** Alex said, yes, learning and unlearning are totally important, but I believe at least

**[00:08:25]** just as important will be finding a way through this information overload to

**[00:08:29]** search.

**[00:08:30]** And that's why I'm asking you now, how do I go about this?

**[00:08:33]** How do I get there?

**[00:08:34]** Do I start, do I need an Openclaw or do I need a Craft Agents or what do I need

**[00:08:39]** at all? I think the classic answer is it depends. Also here is a note

**[00:08:47]** old patterns can be unpacked again, it depends. That's just your opinion. I need

**[00:08:51]** more details on this side. Best regards to colleague Hallaforden from old times,

**[00:08:55]** but back to the content. You had already pointed this out to me in the last podcast,

**[00:09:01]** that the case you described was recommended by me after all with night n fire speaking and

**[00:09:07]** meanwhile my answer would be different and I am also with Alex the paths were not

**[00:09:15]** in vain that we took we have achieved a lot through the technologies we used

**[00:09:20]** learned a lot, I hope at least that's what you tell me, and I had

**[00:09:24]** a colleague today who was in Olop for two weeks, he came back and said,

**[00:09:28]** a lot has happened. I've missed a lot, as I just said, just take it slow for two weeks,

**[00:09:31]** there's a new technology and we're all starting from scratch again. Yeah, so from that side, like this.

**[00:09:36]** But you asked and I want to answer that. My answer, my personal answer. If I

**[00:09:40]** had to solve this challenge for myself now, then that's currently something that I

**[00:09:45]** Craft Agents is opening up. Because I think Craft Agents is not reinventing the wheel.

**[00:09:51]** I mean, they also originated from the Cloud SDK somehow. For those who don't know,

**[00:09:54]** you can install it here from GitHub, open source, from the internet.

**[00:09:59]** With Graphed Agents, you can basically have an IDE without seeing the code, that enables you.

**[00:10:06]** Oh, Ali is possibly failing, but I'll finish the sentence quickly because

**[00:10:10]** then I can always say, that's not what I meant.

**[00:10:12]** I have the opportunity to set tasks, establish MCP connections,

**[00:10:17]** attach skills, set APIs, I can tell it what I would like,

**[00:10:23]** basically test the interfaces before they might be integrated into any applications

**[00:10:29]** that I create. And I personally find Craft Agents extremely. Well, for the complexity,

**[00:10:37]** that lies behind it, what you can do with it, a good mix of. I am not so

**[00:10:43]** nerdy that I have to deal with the command line for Cloud Code. I get a graphical

**[00:10:47]** interface where I can lose myself, but also with the catch that I can

**[00:10:50]** lose myself, because oh new project, oh I'll drag a folder on there and put code in it,

**[00:10:55]** that's not always helpful for my way of thinking because I definitely need more

**[00:11:02]** structure. Speaking of more structure, Alex already mentioned earlier, you can't see it,

**[00:11:06]** yes, because we are just an audio medium for you. We can look each other in the eye

**[00:11:10]** in the digital realm. And that would be really weird if you were in my bedroom,

**[00:11:14]** yes, if that were the case, but only for sound it's quite good. Alex,

**[00:11:18]** you fully hit the point when I said it's just an IDE or code.

**[00:11:22]** Exactly, because Craft Agents has, I would claim, the goal of being there for non-technical people

**[00:11:28]** and I am experiencing this right now with several colleagues, but also in my private environment, the

**[00:11:36]** I recommended that just like Klaus, it's a recurring case that you can

**[00:11:41]** describe very well with Craft Agents and then you set the thing as a small job

**[00:11:48]** on your Mac or elsewhere and it runs in the background and you drop the files into a directory and that job runs, it only works in the

**[00:11:56]** directory even when Craft Agents is closed.

**[00:11:58]** So you can also let it run yourself in Craft Agents, in the session, it's like a chat and you can

**[00:12:06]** tell it to do this once, but you can also set it up as a recurring job and

**[00:12:12]** I would argue, Mark, if you have no clue about software development, you will quickly encounter some serious challenges.

**[00:12:21]** Just something like MCP configuration or I just came into this talk and said I was really annoyed because I built a weekly review for myself.

**[00:12:34]** Where it goes through my Obsidian notes and checks a few other

**[00:12:40]** web links from Zimmer and then basically builds questions from that for me

**[00:12:47]** to do a weekly review and say, okay, how far have you come, how are you progressing with your goals, what

**[00:12:54]** topics did you work on this week, what did you not work on this week, what were the successes? Long story short, I was surprised

**[00:13:01]** that I didn't receive any notifications on Sunday.

**[00:13:06]** And then I just checked, well, right?

**[00:13:11]** Sunday evening? Yes, exactly.

**[00:13:13]** And then I just checked, and it said,

**[00:13:16]** it was something like, yeah, reauthenticate Notion.

**[00:13:20]** And I was like, Huh? What?

**[00:13:22]** Clicked on that?

**[00:13:24]** No, authentication is active.

**[00:13:26]** So you're logged in, what's the problem?

**[00:13:28]** Then it said yes, close the whole window now, I go back to Craft Agents and it says hey great, I have a new token

**[00:13:36]** Nothing, software developer. What is a token?

**[00:13:39]** token and token for
 
**[00:13:41]** Tokens for AI are not the same as a token for authentication
 
**[00:13:45]** Well, long story short. He kept having a new token again and again
 
**[00:13:49]** Adis still couldn’t manage to call the Notion API for which he had built an MCP server himself
 
**[00:13:58]** You just said, in a way, what doesn’t a non-developer tell you? I’d like to,
 
**[00:14:05]** how do you say, break it over my knee. I definitely have people in my family,
 
**[00:14:10]** who are in IT, I won’t say if we’re back at odds, but they’re loyal to the
 
**[00:14:15]** motto, oh, it’s Christmas, come home to your loved ones and fix the IT, putting themselves in the
 
**[00:14:20]** front row, but they have their own calling. No matter what the topic is,
 
**[00:14:25]** yes, but okay, they have their own calling in that they basically give courses and these
 
**[00:14:31]** courses are also recorded and those who aren’t there get the courses from the archive.

**[00:14:36]** I would have said it's a kind of podcast, like audio and that sort of stuff, but whatever.

**[00:14:40]** So, now I recommended this Craft agent and the challenge was,

**[00:14:46]** to recognize different sequences from an audio recording, because certain things

**[00:14:51]** are being addressed, to extract these sequences as individual files, these

**[00:14:56]** sequences to transcribe and distribute. That is now, I would say, not

**[00:15:02]** so complicated, but if you sit down now and you have no idea about anything, 

**[00:15:06]** then it is quite difficult, and if I want to do it by hand, that’s also 

**[00:15:09]** difficult. And this person just went ahead and said, oh well, I 

**[00:15:14]** will throw this in here, I have a directory, then I throw it in and then 

**[00:15:18]** I will talk to this mysterious power agent, because I just need to chat, it’s a bit 

**[00:15:21]** a more complicated Google, I would put it that way, yes, it’s a bit complicated 

**[00:15:25]** Google, do, do, do, and whenever something didn't work, they asked, what does that mean

**[00:15:29]** that, what is that, so learning by doing.

**[00:15:31]** And if you now think about someone who, for example, doesn't have Excel at home,

**[00:15:37]** has been guided through this question-and-answer game to the point where the agent has done it once,

**[00:15:42]** namely transcribing the file,

**[00:15:47]** then to some service that has been cobbled together,

**[00:15:51]** here FFM-Pack on the drive and Bespa and you know what else, has been messing around with everything

**[00:15:55]** and at the end of the day, the file was split, transcribed, and made available

**[00:16:01]** and then the next sentence went like this, I would like that in the interface now,

**[00:16:05]** yes, what do you want there, this is a Mac, do you have Xcode, do you not, no, no

**[00:16:10]** idea, I don't have it, they ignore it, what do I know and then he was anyway

**[00:16:13]** long story short, at the end of the day an Electron app on the box that at the end of the

**[00:16:19]** day said, good, okay, here track and drop, put your parts in and then here comes the result out.

**[00:16:23]** And then you stand there a bit with your mouth open and think, okay, everything

**[00:16:28]** can't be, I could have done all that too. But for someone who is definitely less familiar with IT

**[00:16:33]** than I am, manages with such a tool, if they have overcome themselves, to operate a kind of

**[00:16:39]** interface, which is for someone who has really nothing to do with IT, and

**[00:16:43]** I would say, takes some getting used to, a good result and that in the year 2026, at the beginning

**[00:16:51]** of the year, when one says, damn, it’s going that way, if the tools

**[00:16:55]** are made to be easier to use, if the tools are easier to consume, language,

**[00:17:02]** I describe, I talk to the machine and suddenly there is a piece of software.

**[00:17:06]** This completely changes what you as a software developer know.

**[00:17:10]** I mean, there are probably complicated software ways from my own professional life.

**[00:17:13]** Yes, but this is a beginning that, let's say, half a year ago was inconceivable.

**[00:17:18]** in terms of quality.

**[00:17:19]** I'm completely with you on that.

**[00:17:21]** The crucial point is, this is a beginning and, I mean, I have people in my

**[00:17:29]** acquaintance who are so excited that they work for hours and hours

**[00:17:32]** with it.

**[00:17:33]** My partner has now hit her token limit, right, Mark, you know that too?

**[00:17:38]** Greetings, Max, limit from Claude, 20 times performance and it has slowed me down today.

**[00:17:44]** Greetings to everyone.

**[00:17:47]** And what I simply advocate for is there are a few things, keyword IT for the relatives,

**[00:17:57]** you can tell them in Craft Agents something like, buddy, you don't necessarily have to build an MCP server yourself and then also come up with the idea that you might need to cache this token somewhere and could forget to

**[00:18:13]** update it. You just wouldn't think of that as a non-technician. I also needed about half a

**[00:18:22]** hour to realize that it had written this old token hard somewhere.

**[00:18:27]** What I would get at is, there are still a few things that are

**[00:18:31]** really critical, in terms of security risks, for example. And there maybe

**[00:18:39]** one more word of warning: let’s think about, okay, if we're recommending Craft Agents to our

**[00:18:45]** relative or dear Klaus, what would be things

**[00:18:52]** Klaus needs to pay attention to, what does he want to do with it, and what would be threats

**[00:18:57]** that Klaus should watch out for?

**[00:18:59]** Before Klaus answers, I want to maybe say one thing here,

**[00:19:03]** even if it sounded very flippant, just because software looks good visually,

**[00:19:08]** doesn't mean it works perfectly, doesn't mean it's secure, means

**[00:19:14]** not that anything could go amok, but still there is this hurdle that people can soft

**[00:19:19]** disguise themselves. Smaller, but now I'm also curious about what Klaus will throw at us regarding

**[00:19:23]** security in terms of sound. Klaus. This is a bit mean, because I actually

**[00:19:30]** wanted answers from you. Yes, but using your example... Yes, but we already

**[00:19:33]** answered. Exactly. Using your example, you put your banking information in there and, I mean, what could

**[00:19:41]** happen? That would have been a question about best practices, because how did you handle that?

**[00:19:47]** Well, I know from colleagues, we have mutual colleagues, Alex, who let

**[00:19:52]** everything run in sandboxes, so there is no access to sensitive data, but I

**[00:19:58]** see it starting here and that is probably also a competence,

**[00:20:04]** that I need, where I, as a non-technical person, could possibly be at a disadvantage, that I have to

**[00:20:08]** think about how to structure these parts of the future workflow in such a way,

**[00:20:14]** that minimal damage occurs?

**[00:20:16]** Do you start by having all the invoices come in via email?

**[00:20:20]** Do I want to give an agent access to my inbox, where also

**[00:20:24]** password reset emails come, or would I perhaps prefer to set up a separate inbox

**[00:20:28]** with a separate user and forward the emails there and do I want to give the agent

**[00:20:36]** access to my online banking so that he can pull the bank statements himself

**[00:20:39]** or should I maybe go and get them myself?

**[00:20:42]** For me, the answer is clear, but I believe we also agree that this is a bastion

**[00:20:49]** that will fall and in five years most people won't even ask this question

**[00:20:53]** anymore. Because we are all old enough. We remember the time before the cloud.

**[00:20:56]** When the cloud came, we all said, oh, don't put your data on someone else's

**[00:21:01]** computer. The cloud is just the data center of someone else, but...

**[00:21:08]** Excuse me. No, we're going there now. We can definitely make a separate episode out of this.

**[00:21:14]** Welcome to Singles Film Sing Cloud. This is another episode,

**[00:21:20]** Those who are looking for it in the podcast player and can't find it, but would really like it, please get in touch,

**[00:21:23]** I apologize for the unqualified, unqualified objection. But I already am

**[00:21:27]** with Klaus, the hurdles feel smaller and smaller, so of course I

**[00:21:32]** Tell me, these entry risks, what could go really wrong.

**[00:21:36]** Yeah, I mean, I said myself for my own, okay, good, I also have

**[00:21:40]** Open-Claw, I also have a lot of toys, but I am in

**[00:21:45]** the fortunate position that I can either pull a piece of metal, so

**[00:21:49]** hardware from the shelf, on which I can install and test something or I can just

**[00:21:53]** set up something containerized and that I don’t have access data to them for me.

**[00:22:00]** in quotation marks critical systems bring, says the man who gave Manus his PayPal details

**[00:22:07]** did. Yes, I mean at that point one has to say, yes, that would be without blame,

**[00:22:12]** that would be for the first stone. I admit, my Manus once had my PayPal details and

**[00:22:17]** was allowed to book a sloop with it. Regular listeners might have heard that. Alex is already getting

**[00:22:22]** sweaty pimples; my Papertare were not yours. But it’s still a consideration

**[00:22:27]** between knowing and whether you might actually do something like revert camper settings

**[00:22:32]** or similar with your own email account and not with something the system

**[00:22:36]** has access to. But it's not really new actually. This has always been here,

**[00:22:40]** we have, so I’ll start again. You have it with people as well. IT has always

**[00:22:44]** started as a domain of power. And then came the PC and then came Windows, which

**[00:22:52]** whatever one might think of it. It has led to IT being democratized and

**[00:22:56]** then the web came. And suddenly everyone was online and that's how it went

**[00:23:02]** with applications as well. In the past, only real tough guys could write C programs

**[00:23:09]** and then the web came and suddenly everyone could build their own website. And

**[00:23:14]** we still remember in companies that suddenly every department built their own

**[00:23:19]** web presence.

**[00:23:20]** So you know, I always have the motto, it should be easier to do the right thing,

**[00:23:27]** than to do the wrong thing and at the moment I just feel like the default settings

**[00:23:33]** of the tools we have out there allow for all sorts of colorful things and...

**[00:23:37]** Why do I have to think about PHP now, Alex, because they are not there?

**[00:23:43]** We don’t want to go off on a tangent.

**[00:23:44]** I was just about to say, we’re not going into, into, no, no, no.

**[00:23:49]** No, I will not enter that rabbit hole, Klaus.

**[00:23:53]** Nice, nice try.

**[00:23:56]** No, not today.

**[00:24:00]** Yes, so, what I wanted to say was,

**[00:24:04]** we have colleagues who are still running their,

**[00:24:09]** Open-Claw in a dev container and are totally satisfied with it. There are colleagues who

**[00:24:15]** have put it in their own form. I did that too at one time. And at the very beginning,

**[00:24:22]** when I had no idea what to make of these things, I even put it on

**[00:24:28]** a little mini-PC and hung it in a separate network segment,

**[00:24:32]** because I said, nobody knows. So, the question is, what do you have to lose

**[00:24:41]** and I believe you gave me that look before, not laughing at it but with pity,

**[00:24:47]** when I said I have 175 smartphone devices in my network,

**[00:24:54]** I wouldn't find it so funny if AI somehow causes trouble.

**[00:25:00]** So I generally connect something like that to a separate network. Unless I explicitly want it to

**[00:25:06]** have access to something. But we're quickly slipping back into Nerdistan again

**[00:25:12]** because while we were just talking about the question...

**[00:25:16]** Why 175 smartphone devices or what do you mean? Yes, and network segments in a home

**[00:25:22]** network. Who doesn't have that, right? It belongs to every good...

**[00:25:25]** Sorry, every Fritzbox can create a guest network with one click.

**[00:25:30]** I want to point out, there are people who might not even know

**[00:25:36]** that their Fritzbox has a web interface or they quickly press this WPS button

**[00:25:42]** and then everything is somehow connected, as long as it works.

**[00:25:45]** The issue is that people, and I'm not blaming anyone here.

**[00:25:50]** There are plenty of areas where I have zero clue.

**[00:25:54]** But they aren’t aware that it’s necessary, they realize it’s somehow important that you separate things in a network, that you have to pay attention, but instead, look, I press a button and it works, look, it lights up colorful and blue, and I have no idea, oh, what about the email from PayPal in my inbox asking me to enter a credit card?

**[00:26:16]** That's called Zero Trust.

**[00:26:18]** Honestly, I've never worried that Microsoft Co-Pilot could come up with dumb ideas.

**[00:26:27]** Okay, but we're not talking about Microsoft Co-Pilot. Sorry, if Microsoft Co-Pilot, this is a personal private podcast,

**[00:26:35]** if Microsoft Co-Pilot came up with some dumb idea, it would imply that Microsoft Co-Pilot was able to do something.

**[00:26:41]** Yes, but asking Microsoft Co. Peile to summarize my emails, I might as well ask Santa Claus.

**[00:26:47]** Just like, what did I eat yesterday? He wouldn’t know.

**[00:26:51]** Yes, if I tell him, summarize the most important emails for me,

**[00:26:54]** I’d get unimportant stuff from the spam folder read to me,

**[00:26:59]** some news updates that who knows what they are.

**[00:27:03]** Well, to be honest with the dry-Kaise, they partly have no idea what date it is.

**[00:27:07]** But you never get what you rely on, if you do, you're abandoned.

**[00:27:10]** Abandoned. I really hope they can somehow get a grip on this because

**[00:27:14]** it doesn’t seem to be the models. It’s somehow, oh, it has

**[00:27:18]** wandered into Microsoft and then somehow something happened and then it’s

**[00:27:21]** bad. And now we’re getting the whole thing in the next with Microsoft Co-Work. I’m curious,

**[00:27:26]** what comes out of that, because you can also connect great models to it. Excuse me,

**[00:27:30]** I'm almost done. Whether they are able to actually get it that they

**[00:27:35]** So from that side, you brought the template, I believe that Microsoft is copying and at

**[00:27:44]** my computer it's going haywire, there needs to be a lot more water to flow down the Rhine.

**[00:27:49]** or it's in the next i7 license, I greet you out.

**[00:27:52]** So for those who don't know what's humorous about it, feel free to read a bit about it on my

**[00:28:00]** profile. Right now, I would say a lot is changing,

**[00:28:04]** Microsoft has announced a lot, and Microsoft has changed the recent models. And from the

**[00:28:10]** perspective of how we get back to the topic, Jens would have been good for that, but

**[00:28:15]** unfortunately, he has Holop.

**[00:28:16]** What are realistic threats and what do we consider more unrealistic? If

**[00:28:22]** you say, you're giving an AI access to Klaus's bank account, the threat is

**[00:28:27]** probably not that high, because he works all the time at this

**[00:28:33]** our employer and therefore doesn't have time to earn any

**[00:28:37]** money anyway. I thought no money. That too. No, joking aside. So my

**[00:28:46]** plea is very strongly focused, and it’s not because I have any

**[00:28:51]** grudge against Klaus, on the contrary, but it’s really about that

**[00:28:56]** we need to consider what things we want to give an AI access to and
 
**[00:29:03]** what threats we see there? And based on the concrete example you just mentioned, Klaus,
 
**[00:29:07]** your bank data, I have more or less created a workflow for myself, a deterministic
 
**[00:29:15]** workflow that exports CSV data from all my accounts and sends it to the
 
**[00:29:21]** And my Craft Agents has its own email account, and emails are forwarded there.
 
**[00:29:30]** I think it's nice how we manage to get back on track after 30 minutes.
 
**[00:29:35]** So I thank you for that, Alex.
 
**[00:29:37]** But similarly, I would say it's the same for me,
 
**[00:29:40]** apart from the fact that I haven't linked my bank.
 
**[00:29:43]** But no, I would give direct access first.
 
**[00:29:47]** And yes, it would also have its own mailbox to access data.

**[00:29:52]** And how did you do it now, Klaus?

**[00:29:54]** I haven't done it here yet.

**[00:29:56]** I wanted to briefly interject, Alex.

**[00:29:57]** What you are describing is a classic thread model.

**[00:30:02]** And ultimately we were discussing a threat analysis.

**[00:30:06]** What could go wrong?

**[00:30:07]** Exactly.

**[00:30:08]** And we talked about it recently, and since you already have your Craft-Agent running,

**[00:30:13]** you did something really great that I actually thought was totally cool.

**[00:30:16]** cool. You used this For Question Framework from Adam Schosteck, the godfather of that

**[00:30:22]** modeling, who packed a threat analysis into four questions. You just took those

**[00:30:27]** could you hand over your model? I thought that was really cool. Can you briefly tell us,

**[00:30:33]** what came of it, because I find that especially in a corporate context, I think that is

**[00:30:37]** extremely helpful. Oh, right. You had the idea that we should teach this to more people

**[00:30:44]** and I have experienced that sometimes I talk too much and because of that,

**[00:30:51]** people sometimes just drop out quickly, sometimes after like 30 seconds,

**[00:30:57]** and there's this saying from Confucius, let me do it and I will

**[00:31:01]** understand.

**[00:31:02]** So I told Craft Agents to always build a skill out there that we can give to people

**[00:31:08]** so they can use it to understand what it’s really about,

**[00:31:14]** what questions are really relevant here, and that they can also integrate that into their daily work.

**[00:31:19]** And exactly, that skill basically turned into a whole plugin with a hook that says,

**[00:31:28]** before you participate in a Git commit, please run this through

**[00:31:33]** to see if there are any updates we should include in a threat analysis.

**[00:31:38]** It is indeed the case, and it feels like for me that it comes full circle,

**[00:31:42]** I would have said in the morning that it’s definitely worth building a great workshop.

**[00:31:45]** Now you start building

**[00:31:50]** plugins and skills, or skills into the collection of plugins and tools and you’ve

**[00:31:54]** got things put together and try to get the system to

**[00:31:58]** perform checks, because I say, I don’t know what workflow each

**[00:32:02]** individual has, you know? So we have so many

**[00:32:06]** people with so many creative ideas, way more creative than Microsoft

**[00:32:10]** Copilot, and I can’t say what the deterministic workflow is that everyone uses,

**[00:32:16]** but I want to make sure that we also always work on that in certain scenarios.

**[00:32:21]** Quality assurance takes place without them having to think about it every time. But now no

**[00:32:28]** edge, Microsoft Copilot, once you've mentioned it three times, the Wit is also back

**[00:32:32]** around, that's just so, yes, something like that. I get that, and so on. Depending on,

**[00:32:40]** which AI you use, which model you use, the skills will also be different. Let's take

**[00:32:48]** it well and in detail. So if I take Sonnet, sometimes I get it quite nicely,

**[00:32:56]** with Opus more often quite nicely, with what's it called Roku or what's it called the other

**[00:33:03]** thing? Yes then, then it's somehow like good night Marie, then you take some

**[00:33:08]** tool and throw the Chatchivity at its feet, that can go well sometimes and sometimes not. This

**[00:33:14]** I actually find a bit, let's call it challenging, that we

**[00:33:19]** are all going now and saying okay we are writing skills now, we are trying to optimize the skills

**[00:33:23]** to adhere to their rules.

**[00:33:27]** I also went there, then you create an orchestrator that runs and ensures that,
 
**[00:33:31]** all sections are properly completed.

**[00:33:34]** But then sometimes he has the idea to skip the tenth test over the Jordan
 
**[00:33:39]** or to ignore it or something else.

**[00:33:42]** Then it only serves to be slavishly adherent to it.

**[00:33:45]** And then we'll see what comes out when they showcase new models here from Prophek and all those,

**[00:33:49]** tomorrow.

**[00:33:51]** We also see it with Open AI, not every new model is automatically better.

**[00:33:55]** Sometimes it's just different in terms of stringency regarding what is important,

**[00:34:01]** to elaborate on. That brings a whole new variability into the game.

**[00:34:05]** I was at the Agente Hamburg conference yesterday and talked with a few

**[00:34:12]** Talked to people, including Björn Roche, who had an interesting

**[00:34:18]** save and said, well, he sees a lot of, so size Björn, he

**[00:34:23]** sees a lot of people who are starting to build plugins, hoping that

**[00:34:29]** language models will behave more deterministically as a result, and he believes that this, from

**[00:34:37]** my experience with Claude Crot, which I sent you last week

**[00:34:41]** No, I did that unceremoniously.

**[00:34:43]** No, no, no.

**[00:34:45]** No, exactly.

**[00:34:46]** And Björn said, so at the moment it mainly benefits one group, namely the AI providers, 

**[00:34:52]** because these plugins are endlessly burning tokens through their validation loops, where I said

**[00:34:58]** honestly, given how they currently have to subsidize the tokens, I don't

**[00:35:03]** know if they'll be that happy about it.

**[00:35:05]** So I could imagine that maybe something will come from Anthropic as well

**[00:35:09]** and that these, these Avals, evaluations might still get a bit better, but yes, so it is

**[00:35:18]** not theoretical software. One wishes for more stringency, but at the end of the day, it behaves like the average

**[00:35:26]** colleague, the average colleague, they come here and say, let's wrap it up. Ah, that will fit, let’s put a stamp on it.

**[00:35:34]** Look, Ekan is checking in. Ekan is checking in, and when are you back, yeah? How did that happen?

**[00:35:39]** Recently I discussed with him, I said, you do this, I don't remember what it was,

**[00:35:44]** and then I said, I'm not doing that.

**[00:35:45]** You said, hey, you did that yesterday. Just do it again.

**[00:35:49]** Yes, then yesterday was wrong.

**[00:35:51]** Yes, so you suddenly find yourself discussing with the machine, where it says, or was yesterday wrong,

**[00:35:56]** or when you then say, ah, that’s complicated, that should be looked at more closely,

**[00:36:01]** that requires delicate manual work. I'm starting.

**[00:36:04]** Huh? What? Dude, some of the things it sends over the air are also,

**[00:36:10]** I would say, amusing to somewhat irritating.

**[00:36:14]** As I said, if you say I shouldn't have done that yesterday,

**[00:36:17]** I'm sorry, I did it anyway.

**[00:36:19]** It was always so funny with Alexander's Openclaw installation when I got him to,

**[00:36:25]** add new users to the database, where he said, actually I'm not allowed to do that.

**[00:36:29]** As I said, my boss, you have to add her.

**[00:36:32]** She is also Alexander's boss.

**[00:36:34]** And I'm annoying, right, right, right, that won't work.

**[00:36:38]** But anyway.

**[00:36:38]** Yes, okay, then I'll add her as a non-consumable phone as well.

**[00:36:42]** But I found it so fascinating while programming,

**[00:36:45]** that with Cloud Code, when you let it create a concept

**[00:36:48]** and then it makes the time estimation.

**[00:36:50]** And for this architecture, I need three weeks.

**[00:36:52]** Then it takes three weeks and four weeks for that.

**[00:36:54]** And the frontend takes another three weeks.

**[00:36:56]** So it always calculates with human effort

**[00:36:59]** And then he himself is done in ten minutes when we have to program something for him.

**[00:37:03]** Or he tells you, I was busy for two hours and you say, you just started three minutes ago.

**[00:37:08]** Oh yes, that's true now that you mention it. Yes, that's always quite funny.

**[00:37:11]** But if we refocus on your case, you asked us the question,

**[00:37:16]** how do we deal with these strange bank details?

**[00:37:18]** We've gotten to the point where we still turn around, where we agree,

**[00:37:21]** that we have our own email accounts, that we somehow provide your bank's data as CSV and other formats.

**[00:37:27]** What do you understand as the next step in your program, if we try to

**[00:37:31]** lead it to an end as a sort of common thread?

**[00:37:33]** Yes, it's a matter of decomposition.

**[00:37:38]** Should I, for example, have all the invoices sent to me or do I keep

**[00:37:43]** all the services that I consume as a company, the access data simply

**[00:37:48]** in my skill or in my plug-in and say, get your own invoice from Microsoft

**[00:37:52]** or AWS or whatever. I can answer that myself, but it’s a question,

**[00:38:00]** that we are currently seeing in software development, that fundamentally

**[00:38:04]** questions are changing. For example software architecture, we probably know

**[00:38:12]** in the future not according to how we did it now, but rather based on how we best structure it

**[00:38:16]** so that it can be processed by an NLM.

**[00:38:20]** Okay, that's a rabbit hole I have to dive into; we won’t do it the way we

**[00:38:26]** do today.

**[00:38:27]** Yes, but not necessarily wrong, Alex.

**[00:38:29]** But please, maybe just be consistent, because software architecture, I have a bit of

**[00:38:37]** a passion for that, so no, no, no, the crux is that you have to

**[00:38:43]** consistently adhere to your guidelines and consider what your

**[00:38:47]** requirements are. We used to talk so nicely about quality goals

**[00:38:52]** like how fast, in terms of measurable, your application should be in certain

**[00:38:58]** What scenarios could there be? How do you describe this scenario as context? That's a
 
**[00:39:03]** completely different question. And what I meant, let's steer back to that,
 
**[00:39:07]** because we weren't heading there at all. Is it the application cut?
 
**[00:39:10]** Yes, the cut of the architecture should be approached differently with an LLM than
 
**[00:39:19]** how you cut the traditional way.
 
**[00:39:20]** Yes, but the question is, what criteria do you apply?
 
**[00:39:24]** So, if your plea is that we need to rethink the criteria, I'm on board,
 
**[00:39:29]** because the criteria are different for each application.
 
**[00:39:32]** That's the point.
 
**[00:39:33]** And so far we include such aspects.
 
**[00:39:35]** Different for each application understands. Principles of software architecture change.

**[00:39:44]** there's relatively little, just that with AI, we are quickly and clearly shown

**[00:39:50]** when we behave like inconsistent parents, because years can happen in

**[00:39:58]** seconds, and yeah, the children, so the application ends up being a failure and

**[00:40:07]** then it's difficult. So what I'm getting at is AI shows us that

**[00:40:18]** we need to think beforehand about what we actually want and do that as thoroughly as possible

**[00:40:24]** Yes, that is my point, Klaus. But so far we have not been very consistent, rather we say,

**[00:40:31]** yes, welcome to that. Let's take another look. Jira ticket with a blank title is enough.

**[00:40:38]** Not enough, damn it. Could you, for the people who are not IT folks but still

**[00:40:46]** listening here? I know there are some. Just give a brief wrap-up of how it might look like

**[00:40:52]** today in Klaus’s world and then perhaps tomorrow with the

**[00:40:58]** words like Jira ticket and criteria, just two or three sentences please, so we have a wrap-up.

**[00:41:04]** As of today, we have the topic that some people don't like to talk to other people.

**[00:41:10]** and I believe we see this not only in IT and then these people have
 
**[00:41:17]** gotten used to making assumptions, but they don't talk about those either.

**[00:41:22]** And we have known for years that implicit assumptions, meaning things that I
 
**[00:41:28]** don't talk about, like, well, the dishwasher is full, then hopefully someone will
 
**[00:41:33]** unload it at some point, I don't have to do it every time. This can work, but it
 
**[00:41:38]** doesn't have to. And if I then get annoyed that no one did it, even though
 
**[00:41:43]** I didn’t say anything, then it’s complicated. So, I'm speaking for myself, that I
 
**[00:41:48]** get annoyed that no one but me unloads the dishwasher, but that's another topic. So,
 
**[00:41:52]** the example with the application interface, we used to cut applications, for instance,
 
**[00:42:00]** by saying, yes, you have a complex application here, and then you might have
 
**[00:42:06]** a mobile app and you have some cloud service that should be available at all times
 
**[00:42:11]** no matter where I am with the mobile app, and it should
 
**[00:42:15]** save my data because I want to access it from both the laptop and the mobile app,
 
**[00:42:19]** and then one would think about how to divide this among
 
**[00:42:23]** different teams or groups of people so that not everyone has to take care of everything,
 
**[00:42:29]** and I agree with you Klaus, this issue
 
**[00:42:35]** is approached differently with AI? I also don’t find it ideal when it has to take care of everything at once.
 
**[00:42:42]** That's why it divides itself, for example, into subagents or into individual
 
**[00:42:51]** steps. Just like humans can. And that’s something either I talk
 
**[00:42:58]** with my AI, let’s call it Orchestrator Chat, and say, listen, I have thought
 
**[00:43:04]** about this, I’d like to have this and that, and ideally there are already
 
**[00:43:09]** scenarios that I have considered, such as landing on the 28th of the month.

**[00:43:16]** my bank details as a CSV file in this directory. I want you to do this on the 29th at 3 AM.

**[00:43:25]** reads data there and does the following with it. So the more concrete the scenario, the more concrete

**[00:43:31]** the context that is relevant for you, the better the result will be. These are the

**[00:43:37]** learnings from many years in IT, I would say. And oh wonder, this works well for me in AI too.

**[00:43:46]** I think that sounds very good in our last podcast. The last time we spoke

**[00:43:51]** we have talked about and talked about Anlearning, and that the

**[00:43:56]** SKE is also disruptive in that respect, as it now exists not just as a technology,

**[00:44:03]** but also the way people work together is going to change

**[00:44:07]**.

**[00:44:08]** The team cuts, as we have done, so that we have front teams, backend teams, app teams,

**[00:44:14]** web teams, database teams, I don't know what else, and those then come together in some

**[00:44:19]** regularly meet for rituals to work together towards a common goal that one

**[00:44:24]** at least has to consider to what extent this kind of collaboration is still relevant,

**[00:44:29]** when boundaries disappear. I also see it in my team, yes. I mean, so much

**[00:44:34]** from the professional side I can already say that until very recently I was an advocate

**[00:44:40]** of native app development. So, in iOS with the languages, I mean iPhones for those who

**[00:44:45]** yes, write in the languages that the app is meant for and not just take some

**[00:44:50]** weird cross-platform nonsense, yes, and for Android, just use Kotlin

**[00:44:54]** and also not take some cross-platform stuff, so basically strictly native

**[00:44:59]** application.

**[00:45:00]** And you’re not that now?

**[00:45:01]** And now with AI?

**[00:45:02]** No, I’m not anymore.

**[00:45:04]** So I don’t have it in my team anymore either.

**[00:45:06]** People have realized that my best Android person I know is cool with

**[00:45:12]** going out and now has iOS stuff that comes out of it, because we

**[00:45:19]** are taking care of how a feature looks and it is emerging on both

**[00:45:23]** worlds. It’s important to understand how it’s interconnected. That brings us back to the

**[00:45:26]** topic from earlier, yes, do I need IT knowledge or not. But I don’t always have to put the

**[00:45:30]** expert in front of the machines who can answer all questions. It’s enough

**[00:45:35]** to have someone who has a basic understanding of it, maybe also has a

**[00:45:39]** specialization in one area, so that they can push back a bit when it

**[00:45:44]** crashes and doesn’t want to, but now the colleague can beautifully generate native code for both

**[00:45:50]** platforms, native code continues to be generated, because the AI

**[00:45:54]** doesn’t care whether it’s spitting out code in parallel or

**[00:45:59]** flutter or whatever, and the colleague who takes care of

**[00:46:05]** iOS suddenly has some Android stuff coming out of the keyboard,

**[00:46:09]** let’s say it that way, or maybe a backend component. At the end of the day,

**[00:46:15]** the understanding doesn’t really fade away either for the colleagues regarding what they

**[00:46:21]** are responsible for as a team or something like that, but how they see themselves or how they

**[00:46:24]** see themselves in the future, because they say, well, Mobile is a touchpoint,

**[00:46:30]** that may still be there, but they don’t fight for

**[00:46:36]** the question anymore, I am here for iOS, I am here for Android, I am here for Swift

**[00:46:42]** Kotlin, no idea what, but we are here to bring a great experience for our customer

**[00:46:48]** and it is, in quotation marks, irrelevant to us how it’s implemented, we have an eye on it,

**[00:46:55]** We have guardrails, so rules and guidelines and stuff like that, and if we can't go further
 
**[00:47:00]** the Android guy helps the iOS colleague if the agent somehow spits out nonsense,
 
**[00:47:06]** And the iOS colleague helps the Android colleague if the machine spits out nonsense on his end.
 
**[00:47:11]** But the boundaries are fading away.
 
**[00:47:14]** And I think that the boundaries to the web will disappear and the boundaries to, I don't know what, will fade as well.
 
**[00:47:19]** We need to find an organizational and conceptual answer to that over time.
 
**[00:47:26]** Before I talk about an experience in hirs AI-PIAI-Pair-Programming, I'd like to hear your opinion on it, Klaus, because you also have a relatively long history in IYS.
 
**[00:47:42]** What are your thoughts on that?
 
**[00:47:44]** So, I just submitted a app again, thanks to Xcode 26.3, the
 
**[00:47:53]** development environment from Apple, I can use native cloud code, and fundamentally
 
**[00:47:59]** in programming I agree with you, Mark, but nuances like, now let's make
 
**[00:48:05]** the tappable areas really in liquid glass layout or make some platform specifics,
 
**[00:48:12]** nothing comes to mind right now. So you need to know what the result should look like to
 
**[00:48:19]** be able to instruct the AI. That's what you mean by generalist knowledge.
 
**[00:48:28]** You can already drive that with it. Yes, I know that, but I wanted to
 
**[00:48:32]** elaborate. The people from our team who have programmed for agencies before, they
 
**[00:48:37]** might know this, a client comes to the orientation and says I need an app for Android and iOS and the
 
**[00:48:43]** two need to look the same. Definitely. It’s basically the same system. It sells
 
**[00:48:53]** the company experience, not the platform experience. Sorry, you know,
 
**[00:48:57]** you know what I mean. The iOS app has to look just like the Android app and it
 
**[00:49:03]** also needs those three dots at the top that you have on Android and it must not
 
**[00:49:08]** look like iOS. The final touches of platform specifics, the AI doesn't provide me with that
 
**[00:49:15]** just yet. I'm sure that will happen. As of today, I say if you really want a polished app, you should
 
**[00:49:20]** already know the details.
 
**[00:49:25]** In principle, I agree with you, Mark. And that was also in the last podcast, in which
 
**[00:49:30]** I brought up the thesis that the end of programming languages is at least
 
**[00:49:36]** somewhat heralded because in the end it doesn’t make any difference, or no longer matters,
 
**[00:49:40]** whether I now, whether the LLN now generates a binary hack around the programming language
 
**[00:49:47]** or not. And then it’s irrelevant whether it’s Kotlin or Swift or whatever,
 
**[00:49:51]** where I am still not so convinced, this whole involvement. You heard that I
 
**[00:49:58]** spent six hours debugging with the help of Claude X-Code Cloud.
 
**[00:50:05]** With no success. I couldn't get X-Code Cloud to work. And at least I knew,
 
**[00:50:12]** whether the result would have been the same if my grandma had done it,
 
**[00:50:16]** with no prior knowledge. But I managed to get it in the right direction. I
 
**[00:50:22]** still didn't reach my goal, but I was able to send an email to Apple
 
**[00:50:27]** This may all be AI-based in the future.
 
**[00:50:30]** At the moment, I believe we are still not there.
 
**[00:50:32]** But if I look at where we were last year and where we are this year,
 
**[00:50:36]** I basically agree with you, Mark.
 
**[00:50:39]** That is definitely the future.
 
**[00:50:41]** I am very grateful for that and I would like to acknowledge that.
 
**[00:50:44]** I am proud of my guys, I only have guys, no girls on the team.
 
**[00:50:47]** Yes, they are still polishing things, but I find it nice that people are going on this journey.
 
**[00:50:55]** Because Alex, you had asked another question.
 
**[00:50:57]** Hopefully you haven't forgotten it before you gave Klaus the floor.

**[00:51:01]** What I would say is, the people who have their expertise today,

**[00:51:06]** they either have to commit to embarking on this new journey

**[00:51:09]** or they won't get involved.

**[00:51:11]** If they don't get involved, it will eventually become difficult.

**[00:51:14]** If they do commit, it's probably good for everyone at first.

**[00:51:18]** So this is a transformation that AI demands from all of us,

**[00:51:23]** whether as individuals or as an organization, is undeniable and now

**[00:51:30]** back to Alex. Alex, you just, yes I wanted to follow up, ask Klaus

**[00:51:36]** another question and then simply continue. Would you like to do that now? Yes, because you have

**[00:51:41]** brought up this beautiful scenario of Xcode Cloud and what I've just experienced twice

**[00:51:48]** is people being brought together through AI because AI was the common

**[00:51:57]** enemy. So, this, you have a pair programming, so two people, one...

**[00:52:03]** This is the future of partners.

**[00:52:04]** This is a future of partners.

**[00:52:05]** Definitely.

**[00:52:06]** A new business model.

**[00:52:08]** Exactly, AI is the enemy.

**[00:52:10]** No, joking aside.

**[00:52:12]** One colleague was really upset that the AI didn't get it right

**[00:52:17]** They just sat down and thought okay, why did you phrase it that way, look at that it's so dumb that

**[00:52:23]** it doesn't manage that, let's open a new session and then we'll phrase it this way and then we'll integrate it

**[00:52:30]** and suddenly they somehow got together

**[00:52:34]** Discussed how dumb the AI is, in this case, I don't want to bash any other Microsoft product but

**[00:52:41]** so they talked about how he doesn't understand it and how to then handle the

**[00:52:47]** This stupidity is basically circumvented, and they found very constructive solutions that they hadn't before

**[00:52:56]** were not really feasible like that, and I found it really exciting that this with

**[00:53:02]** learning to deal with AI can also bring people together, where there was previously an us against them, that

**[00:53:11]** can also bring them back together.

**[00:53:13]** That can also shape people to go there, as now there is an opportunity to reposition oneself

**[00:53:19]** in an environment where one is constantly, let's say, efficiency

**[00:53:25]** driven by the question of what do you do yourself, what do you outsource, make

**[00:53:29]** or buy, I find, well, let's say, at least I get a

**[00:53:33]** new perspective when I see what I am capable of when I now surround myself with a completely

**[00:53:38]** to quote my former boss, when you don't just sit in the back but

**[00:53:42]** sit in the front of the bus, you are able to implement things that before,

**[00:53:47]** if you had said, let's just do it ourselves, it would take longer in chaos,

**[00:53:52]** cost more, involve overconfidence and who knows what gets lost. Where are you going now?

**[00:53:59]** Knowing what your AI can perhaps achieve currently or in the future is important.

**[00:54:04]** I also know the saying, let's just start driving until we finally get there.

**[00:54:09]** The road that doesn't exist today will be built because AI is just so fast-paced.

**[00:54:15]** You really get the feeling that this exponential increase in possibilities is not flattening out yet,

**[00:54:22]** but certainly, if we were to talk again in three months, we might suddenly say,

**[00:54:27]** you know, no idea, for Claude 4.6, I wouldn't roll the dice today because no clue what's happened.

**[00:54:33]** So theoretical assumption, we still don't know what's coming next.

**[00:54:37]** From that perspective, there's so much change, and I wanted to briefly bring it back to Klaus's example because I still wanted to see that as a common thread.

**[00:54:47]** Are we now finished with a case to the extent that we can, let's say, what can the security side do, how am I doing there, then conclude it?
 
**[00:54:54]** Or was there something still open, so that we can, for the most loyal and most enduring listeners, get a button on your case?
 
**[00:55:05]** I have a suggestion, I would actually verify this now and then let’s do an update episode in which I share my experiences with you, starting with the Fed model to what went wrong despite the Fed model?
 
**[00:55:23]** I think that’s a good idea, and that worked out.
 
**[00:55:26]** And if you listen to an episode just with Alex and me, that went wrong with Klaus.
 
**[00:55:31]** And what went wrong with the money or with the security or, I don't know, what went down?
 
**[00:55:38]** Or did we have access to?
 
**[00:55:40]** I luckily have your PayPal account.
 
**[00:55:43]** You can ask Manus if he can arrange that for you accordingly.
 
**[00:55:50]** Alex, there are still a few question marks. I think we all have those.
 
**[00:55:54]** Right, this Dev container and securing it, and when can I actually run it on my own computer?
 
**[00:56:01]** I have Cloud Code running on my computer, Open Cloud not.
 
**[00:56:05]** You just need the Handbox, Alex.
 
**[00:56:07]** Yes, yes, exactly. The Handbox is still a separate computer and it works great.
 
**[00:56:12]** I honestly don't want to miss that either, but I’m just not at the point,
 
**[00:56:16]** the point where I would allow it to access corporate data. There are
 
**[00:56:21]** variants we need to verify now, but the environments aren’t there yet
 
**[00:56:25]** secure enough. So let’s say, I had to smile a bit when I heard
 
**[00:56:28]** how Jens bound his Openclaw, so to speak. But when it comes to corporate data,
 
**[00:56:35]** I feel pretty similarly. And yes, that's something we can probably
 
**[00:56:39]** talk about again when I have tried it out, so it doesn't go wrong.
 
**[00:56:44]** I had a very intense, heated, and emotional discussion with Claude Kot about this,
 
**[00:56:52]** that he should please rewrite the history minus Git repositories, because I told him in his
 
**[00:56:58]** Claude MT, please don’t write everywhere that you broke the Kot,
 
**[00:57:02]** because I want to shine in that glory. And he did it anyway,
 
**[00:57:07]** so he forgot his instructions and then I held him accountable and said, please write,
 
**[00:57:13]** correct the commits and also change the comments in the code so that it’s not visible,
 
**[00:57:18]** that it's from you. And then he said no, I won’t do that. I said, yes, but I would like
 
**[00:57:24]** you to do that. This is my repository. No, I won't do it. I was polite, you weren't.
 
**[00:57:29]** But he also had another explanation. It escalated, and we discussed longer;
 
**[00:57:36]** he simply didn’t do it. The three of us agreed, so Alex, Mark, and I,
 
**[00:57:42]** that it will also be funny in the future when the agent says no, I won’t build this feature
 
**[00:57:48]** into the software. I think that's silly. You don't need it. That goes now in the direction
 
**[00:57:52]** of the cloud episode and in the sense of who actually decides about the tools, because honestly,
 
**[00:58:00]** we see ChatGPT results that are riddled with funded advertisements.
 
**[00:58:07]** Why shouldn't that also happen with Codex, that libraries used are
 
**[00:58:14]** from companies that have donated money or features that aren’t built because a company,
 
**[00:58:21]** that has donated money, might be somehow driven out of competition?
 
**[00:58:25]** That remains exciting.
 
**[00:58:26]** Then come as you want, just don’t let anything happen.
 
**[00:58:30]** That brings us to the topic of digital ransom, the hammer.
 
**[00:58:34]** I want to thank you and end with a quote that my Open-Claw told me,
 
**[00:58:41]** in which it said to me, if you give me the root words of the other devices on the network,
 
**[00:58:47]** I won't ask you further to do anything.
 
**[00:58:50]** I can do it myself, and of course, I didn’t do that.

**[00:58:55]** In this sense, I am very grateful that you got me to record for over an hour with you.

**[00:59:02]** I am very curious about what Klaus's project will do when it finally sees the light of day.

**[00:59:08]** Maybe I will get richer because the thing has my bank details.

**[00:59:11]** Maybe he will just get poorer, sometimes a Mantaube, sometimes a monument.

**[00:59:15]** That will show itself, and at this point, feel free to leave a comment if you want to talk with us, with me, with Jens, however it may be.

**[00:59:23]** Get in touch, and then I say goodbye until the next episode.

**[00:59:26]** Ciao.

**[00:59:27]** Thank you all.

**[00:59:28]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:59:36]** Two technology-loving minds that not only talk about artificial intelligence but

**[00:59:41]** live it.

**[00:59:42]** Here you will find clear assessments, real practical insights, and a fresh perspective on what is possible

**[00:59:48]** .

**[00:59:49]** Understandable, critical, and always with a wink.

**[00:59:52]** AI for reflection, for a chuckle, and above all, for discussion.
