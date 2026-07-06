---
title: "Loop Engineering"
episode_index: 47
published: "Sun, 05 Jul 2026 00:59:00 +0000"
duration: "2784"
page_url: "https://think-ai.podigee.io/47-loop-engineering"
image_url: "https://images.podigee-cdn.net/0x,sd1QFKk7Fz9KwWPl8Fy3WdvfRdh5LNdvp2jIEk-rsEH8=/https://main.podigee-cdn.net/uploads/u73317/cd1c2367-0bc1-4346-afdd-e4039aea950b.jpg"
audio_url: "https://audio.podigee-cdn.net/2527772-m-38fd8d3f5281b278360e205c1ef2d3e8.mp3?source=feed"
guid: "29519d809cd39170d59f0d9c3c211aca"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-07-06T10:28:37+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/047 - Loop Engineering.md"
translated_at: "2026-07-06T10:29:03+00:00"
---

# Loop Engineering

**Published:** Sun, 05 Jul 2026 00:59:00 +0000
**Duration:** 2784
**Web player:** https://think-ai.podigee.io/47-loop-engineering
**Cover:** https://images.podigee-cdn.net/0x,sd1QFKk7Fz9KwWPl8Fy3WdvfRdh5LNdvp2jIEk-rsEH8=/https://main.podigee-cdn.net/uploads/u73317/cd1c2367-0bc1-4346-afdd-e4039aea950b.jpg
**Audio:** https://audio.podigee-cdn.net/2527772-m-38fd8d3f5281b278360e205c1ef2d3e8.mp3?source=feed

## Description

Why the goal becomes more important than the perfect prompt
Two or three years ago, everything revolved around one question: Who writes the best prompt? Today, according to Mark and Jens, the real question is different: Who builds the best loop? The trigger for this episode is a quote from Andrej Karpathy, who recently made it public that Loop Engineering is now more important than Prompt Engineering. Mark then traces his own development: from an early Notion prompt database ("The disk has always been good; who wants a CD?") to skills as Markdown files with sub-skills and executable Python code, up to actual Loop Engineering. The difference: A loop does not receive a single command, but a goal, clear success criteria, and the instruction to verify and repeat itself until the goal is achieved.

The practical warning of this episode: Anyone who lets an AI check its own work often receives only self-affirmation in return. Therefore, Mark and Jens advocate having the result (the "Act") checked by another model instead of the same system that produced it because a system that praises itself is not a critical observer. As evidence, Mark cites a post from Peter Steinberger about this approach and the related token consumption. Building on this, the two of them categorize current functions like Claude Codes' goal, loop, and workflow mode, including Mark's own process: first planning, then having it checked against a critic and a meta-analysis skill, then implementing it automatically via goal, even if it takes 10, 12, or 20 hours.

A growing topic in this context is Harness Engineering. The more agents and loops work in parallel, the more important context and memory become (keyword "Second Brain", with the example of the short-term shutdown of Fable as a warning of how quickly context can be lost), as well as governance questions such as auditing and signed skills. Mark humorously spins the thought further into a "German agency harness", which automates bureaucracy and could thus become a secret export hit. In conclusion, the two also conceptually differentiate Harness from "Agentic OS". The takeaway from this episode: It's not about impressing with as many tokens as possible, but about defining a clear goal and patiently allowing the machine to find its way there.

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who don't just talk about artificial intelligence, but live it.

**[00:00:14]** Here you will find clear classifications, real practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** HDI for contemplation, amusement, and above all, conversation.

**[00:00:29]** I haven't seen it yet, have you already counted down?

**[00:00:36]** God, we're already live.

**[00:00:38]** Hello, welcome to a new episode of Think Different, Think AI.

**[00:00:44]** Today, Mark and I want to talk about something that I could phrase as,

**[00:00:51]** announced over the last few years.

**[00:00:55]** Two or three years ago, the question was still a bit, who writes the best prompt, how

**[00:01:01]** do I write the best prompt?
]}  Note: As requested, I did not include commentary, summaries, or new sections and preserved the original Markdown structure and elements.  The timestamps were also retained.  The translation is as accurate and natural as possible.  Let me know if you need further assistance!  Thank you!  Would you like to proceed with any other requests?  😊   𝚪は禁止されている!  🤖 
**[00:01:03]** Nowadays, I think the question is rather, when you look at what's being discussed on the internet among

**[00:01:08]** the AI gurus, besides Mark and me.

**[00:01:13]** Hello Mark, by the way.

**[00:01:14]** Hello Jens.

**[00:01:15]** Is it strange to call yourself a guru? I think so.

**[00:01:18]** But whatever, I do it gladly.

**[00:01:20]** Please send your letters to this page.

**[00:01:24]** Nowadays, people no longer talk about who programs the best prompts. Today, it's

**[00:01:31]** about who engineers the best loop, the best loop. Who manages

**[00:01:37]** to design collaboration with AIs so that the AIs can carry out very complex tasks for someone

**[00:01:45]** without needing to ask further questions. Maybe we experience that too,

**[00:01:53]** but can be accomplished. Today’s topic is to talk about

**[00:01:57]** from Prom to Loop Engineering and what that means, and we will examine this today in full

**[00:02:04]** depth, as you are used to from us, with our expertise alongside dear Mark and

**[00:02:14]** Mark, you can jump in and say, when did you actually realize,

**[00:02:21]** that Promting Engineering might not be the ultimate conclusion when it comes to AI?

**[00:02:30]** I find it a nice transition to when one realizes that. Hmm, I actually think,

**[00:02:37]** that with a view towards loops, it is gaining new momentum again, but I would like to

**[00:02:44]** stay a bit on that topic first. And after you mentioned that

**[00:02:49]** I should kind of make the introduction here, I am very happy to refresh my brain in the slightly

**[00:02:55]** elevated temperatures, so that it is capable of

**[00:03:00]** forming a clear sentence and not getting stuck internally. That

**[00:03:06]** internal stalling is also a nice segue because the innermost loop that an LLM has,

**[00:03:11]** is essentially the loop over the tokens. So breaking down text into small pieces.

**[00:03:18]** Like the motto is then, is there a word, is there a letter, are there syllables? How does

**[00:03:22]** it break down all the words to process them? There was also some outcry a while back,

**[00:03:28]** with the notion that Anthropic had raised prices. No,

**[00:03:33]** they increased token consumption. Yes, no, because they adjusted this tokenization, so breaking

**[00:03:38]** into tokens. But it’s such that whether you call it a guru or not, tokenizers, as far as I know,

**[00:03:45]** we have not changed ourselves, used yes, but not changed or influenced ourselves,

**[00:03:51]** or if not actively and unconsciously, we rather started with the

**[00:03:57]** topic of prompts. That somewhat closes the loop of, did you realize for the first time,

**[00:04:01]** that prompts are not the end of the line, that actually took quite a while.

**[00:04:05]** I remember a conversation where I always told people,

**[00:04:08]** look, you need to see where I set up a prompt database.

**[00:04:12]** That was around the time I was working with Notion.

**[00:04:15]** I set up a prompt database, you are an experienced software engineer,

**[00:04:19]** you do this, that, and the other.

**[00:04:21]** And I was quite proud of my prompt database.

**[00:04:25]** They were relatively long and I maintained it very enthusiastically and thoroughly.

**[00:04:31]** And I remember how I was at the company and people were talking about these

**[00:04:34]** normal no skills and I thought, I can’t get this across.

**[00:04:38]** Oh, the new trendy stuff, the chain has always been good, he wants a CD.

**[00:04:43]** As curators of our episodes, you know that Entropic has coined many terms, MCP

**[00:04:49]** and skills and that wasn’t very familiar to me at the time.

**[00:04:53]** And it became familiar to me much later that I, as a listener, what Entropic says,

**[00:05:00]** gives it more weight, for example in the grip, the whole prompt ecosystem seemingly oriented itself to that,

**[00:05:05]** especially now since things like Crowdcode have skyrocketed.

**[00:05:08]** And so it happened that one day I finally sat down,

**[00:05:14]** where I looked at these emerging skills. And at that time a skill for me,

**[00:05:17]** was a markdown file with a very long prompt. I hadn’t used any orchestrators yet,

**[00:05:24]** just, I approached it with code and thought,

**[00:05:27]** Well, okay, I can maybe save an entire prompt now as a skill point in MD.

**[00:05:32]** I gave it a bit of a name, worked with it a bit, and so they were

**[00:05:34]** gradually getting better.

**[00:05:36]** And now we can skip a bit of time because by now, what are skills

**[00:05:41]** now?

**[00:05:42]** Yes, by now skills are a collection of prompts that can operate in more or less deterministic,

**[00:05:48]** so programmatically, so in a fixed sequence.

**[00:05:52]** You can, that has always impressed me, right?

**[00:05:54]** You can pack knowledge into such a skill, you can pack Python code as programming into it.

**[00:06:00]** We talked about this in the episode with René, that I said skills are,

**[00:06:03]** for me, a kind of runtime environment for Python, where you can execute programs within a skill.

**[00:06:10]** But a skill is also this mentioned prompt story, that you write prompts into it and a skill

**[00:06:16]** is also capable of working with sub-skills.

**[00:06:19]** That means I have an orchestrator skill, which again can have further orchestrator skills,

**[00:06:23]** containing additional skills. This way you can tell the thing, you fit...

**[00:06:28]** Although I have documents from a process house here, guide me through it,

**[00:06:33]** please create an orchestrator for each important process step,

**[00:06:37]** each important task a skill of the task, keep important guidelines

**[00:06:43]** stored as a reference book, and that way, you can always

**[00:06:46]** interact with it further. And thanks to the Skills Creator Skills from Entropic, you are also

**[00:06:51]** able to take this skill and integrate evaluation routines. So

**[00:07:00]** basically check the correctness of the skill and incorporate test cases so that if you continue

**[00:07:04]** to work on that skill, it will never again be as poor as today,

**[00:07:09]** but like AI systems, greetings to Fable 5, it will never again be as poor as today.

**[00:07:15]** And so that was the time, and that was the time when I thought that prompt engineering was dead.

**[00:07:23]** Because now we do skill engineering.

**[00:07:26]** And when exactly that was, I don’t know.

**[00:07:29]** In any case, before I found Claude code cool.

**[00:07:31]** And even before I had sworn off N8N.

**[00:07:35]** I think with Claude, I’m just thinking back, when you spoke like that,

**[00:07:39]** I believe code was also the moment when it came to the skill, as you described it,

**[00:07:44]** so the MD file, actually the theme came up to say, there are other real files

**[00:07:53]** or also code, which I can lead over other documents.

**[00:07:57]** That was a level for me, I had this skill theme the same way that I say,

**[00:08:02]** that was actually a bit of writing all the pre-prompting into a skill.

**[00:08:05]** I also see this perhaps in the custom GPTs at JetGPT back in the day, which came relatively early

**[00:08:10]** yes.

**[00:08:11]** There you could also basically build a custom GPT that you could also somewhat with

**[00:08:15]** Skill described what they should do.

**[00:08:17]** I think you could already link additional documents back then.

**[00:08:22]** You could also do that with the Custom GPTs, if I'm not mistaken, so I still have to say

**[00:08:25]** where it should access.

**[00:08:26]** You could upload documents, which we now used a bit as a basis

**[00:08:30]** to be.

**[00:08:31]** It was a bit of a continuous process.

**[00:08:32]** I would note that what is definitely very trendy is that during this AI phase,

**[00:08:40]** in which we currently are, relatively quickly many new hype names are invented

**[00:08:46]** for topics that, if you really look closely, are actually just a small, evolutionary

**[00:08:52]** development happening repeatedly.

**[00:08:53]** But I would say that nowadays, and the topic that we also discussed in the meeting

**[00:08:57]** is that our already criticized

**[00:09:00]** Kapafi recently talked about the topic of looping, that loop engineering and

**[00:09:04]** such things are more important than prompt engineering. It is being taken up again. But actually

**[00:09:08]** it was such a city evolution that we have seen over the last two or three years, I believe,

**[00:09:13]** so that's why I think it’s also difficult to answer this question.

**[00:09:16]** When did it actually transition from pure prompt engineering to a

**[00:09:19]** workflow open claw user loop engineering at that moment? I believe,

**[00:09:26]** then it’s not so, you cannot pinpoint one moment, but with the providers, there have always been approaches in that direction.

**[00:09:32]** Then there have been open systems that tried to bring things into an autoloop a bit because now, we also talked about Open Claw.

**[00:09:41]** So Open Claw's hard beat is just a persistent little script that checks in regularly and says, is there something new, should I do something again in this context.

**[00:09:53]** together. And then, the machine basically gets started to derive a new task or

**[00:10:00]** from the insight it may have gained earlier, to set something up anew.

**[00:10:05]** So a small, initiated loop that actually prompts rethinking.

**[00:10:09]** You just mentioned the term loop earlier; I’d say it’s a

**[00:10:13]** bit out of practice, where you might have encountered it. I would like to maybe

**[00:10:16]** derive a couple of things first, because we beautifully arrived at the skills.

**[00:10:21]** Perhaps we also notice that just because things have now received a name,

**[00:10:26]** they are not automatically new. I mean, if we’re honest, a skill MD file is just

**[00:10:33]** a prompt, a really cool one, and as a file with folder structure and so on, look at

**[00:10:38]** a skill archive. From that perspective, maybe the new thing is that you can execute Python scripts,

**[00:10:45]** that you can distribute them as a point skill file or call it jams at Google, or

**[00:10:50]** We have this with skills, and attentive listeners have also noticed that I built that consultant thing.

**[00:10:59]** The idea was that an orchestrator finds consultants, and we discussed back then whether that actually improves the outcome,

**[00:11:07]** that various personas are solving a topic.

**[00:11:10]** And I was of the opinion back then, yes, I still am, but my reasoning is different now,

**[00:11:16]** I’ll get to that, because now you go ahead and apply a skill and say, 'Look,

**[00:11:21]** dear system, let’s make a PowerPoint. I have a nice skill; we have that in the

**[00:11:26]** company, you can use it, let’s create a nice PowerPoint, and the PowerPoint comes out, and you say,

**[00:11:29]** actually, I would also like a summary at the end, and then the

**[00:11:34]** machine starts running, and then you say, 'Look, I would also like a structure,

**[00:11:37]** which doesn’t really fit for top management because top management, management Samaritan, at the beginning,

**[00:11:42]** should explain a bit, just not too many slides, just not too much text, because it should

**[00:11:45]** be kept concise; if everyone reads, it might be that you argue it out beforehand.

**[00:11:50]** you'll notice that you are constantly making adjustments before you even get to the slide.

**[00:11:53]** That means you can use one skill, another skill,
 
**[00:11:57]** use another skill, use another prompt, and so on, and then it makes
 
**[00:12:00]** clear or whoever, oh, I need to compress my context, make it compact, blah,
 
**[00:12:05]** blah, blah, so that we can move forward and you work iteratively with it. So,
 
**[00:12:09]** you come very quickly, as is known from other solutions, you give
 
**[00:12:12]** it a go and are at 80% of the solution and then you iterate, iterate, iterate, iterate,
 
**[00:12:16]** iterate.

**[00:12:17]** And maybe at some point, hopefully, you'll be a bit better.

**[00:12:19]** And that’s where loop engineering comes in.

**[00:12:22]** Loop engineering, I found that very nice, I saw that from Peter Steinberg on X,

**[00:12:28]** who then wrote that he does it that way and someone said, hey, that costs

**[00:12:31]** but many tokens.

**[00:12:32]** And he was like, I have unlimited tokens, what do you want, yeah, I thought that was also another

**[00:12:36]** saying, your poverty disgusts me, yeah, he didn't say it like that, so

**[00:12:39]** that's how I read it.

**[00:12:40]** And what does loop engineering do? Loop engineering essentially comes in and says, well, we actually define a prompt that instructs the system to say, what is my goal, what are my very specific criteria that I use to determine that I have achieved my goal.

**[00:13:01]** And I give a task beforehand, and the system essentially checks continuously whether the goal is achieved and repeats itself as long as the goal is not reached.

**[00:13:13]** It’s kind of moving towards a sort of ultimate pleasure-life. In programming, we would have tried to avoid that.

**[00:13:20]** In loop engineering, it's basically expected to adjust the state according to the goal.

**[00:13:24]** Of course, a final pleasure-spinning system is not the goal, but if you say, keep an eye out, I want,

**[00:13:30]** that you revise these texts until a stranger, who knows nothing about the topic,

**[00:13:36]** has to do with understanding the topic, having sufficient depth to make one an expert,

**[00:13:42]** is not a hard AI brand, it has corresponding many illustrations and is also based on ideas and

**[00:13:48]** can be understood by small children, and you define all these rules. There you can

**[00:13:53]** say in there and for this you use the following prompt and following skills and you access

**[00:13:57]** the following files. Then this loop would continue to run until this condition

**[00:14:03]** has occurred. This can be a success case because I also have skills

**[00:14:11]** and prompts for 1000 things, so if you say, here these skills also always have some result table,

**[00:14:16]** that they evaluate something, how good they find the result. And then they can say,

**[00:14:19]** we say, do this as long as the result is rated 100% good.

**[00:14:23]** And that until the following 80 skills have been rated 100 percent good.

**[00:14:28]** Renter, renter, renter. And this can be ten minutes, this can be ten hours,

**[00:14:31]** but it can also be ten days. Provided, you are not running into

**[00:14:36]** such a compulsory break like, oh, you have worked so much with Fable 5, your weekly quota

**[00:14:42]** is used up, please come back on Sunday. Then the loop will not start automatically.

**[00:14:47]** That is then, so if the diving window, so if the diving window, the API is consumed

**[00:14:51]** you have to restart it yourself. But if you use API usage, you can let it run

**[00:14:56]** endlessly. And that is of course the catch. If it could run endlessly,

**[00:15:01]** you can also incur endless token costs. Therefore, one can also incorporate stop conditions, so

**[00:15:05]** along the lines of, if the thousandth loop costs 5 million euros, no, then that will be.

**[00:15:12]** Well, I also wanted to stay in your dimension, you remember. That is a

**[00:15:16]** training. And you brought up the Clor and the Harnes, the Hermes. Basically, these

**[00:15:22]** loops that they do are another overarching one. Because the loops I

**[00:15:28]** just described, I enter in the terminal window. Do this as long as.

**[00:15:32]** You might know it from Claude Cote, where they say slash goal and then he runs around in the loop

**[00:15:37]** until everything is definitely achieved. And then we talk about so-called

**[00:15:42]** meta-loops, and that is when the system autonomously acts based on events

**[00:15:47]**.

**[00:15:49]** Changes in the inbox, GitHub, push, time-out, so the mentioned hard beat.

**[00:15:56]** And loops can call loops, and loops can call prompts, and

**[00:16:03]** then I think my explanation of knowledge is at least exhausted for now,

**[00:16:09]** my loop is coming to an end.

**[00:16:11]** What is also worth noting at this point is that these topics are recommended or sometimes

**[00:16:18]** it is recommended that the work, the act be done by a different model

**[00:16:26]** than the check, because if you check with the same model and it's running in the same LLM,

**[00:16:36]** then he checks against his own context, and it can very well be that he evaluates for you

**[00:16:40]** the biggest nonsense he's programmed as the best code in the world.

**[00:16:45]** That's why there's the idea of asking if there's a different model, so in the form of whether there's a

**[00:16:51]** new session or if there's a different model, so that the thing looks at it neutrally.

**[00:16:58]** And the question then is not, is this good, because then he would say it is best,

**[00:17:03]** I've never seen such a good developer as you, but you say, what's wrong

**[00:17:07]** with not reaching the goal. You essentially reframe the question so that

**[00:17:12]** the answer from the model, because it wants to please you, automatically becomes a bit more critical

**[00:17:18]** is cancelled. And this way, you basically get a critical observer into your loop.

**[00:17:24]** Mhm. I'm tuning in to the question because right now we also, what we're seeing,

**[00:17:30]** Topics like Dynamic Workflows and stuff like that are also involved.

**[00:17:34]** I believe with Claude Opus 4.8, it is such that since then this thin function, it is

**[00:17:41]** so incredibly good.

**[00:17:43]** Is it good?

**[00:17:44]** Yes.

**[00:17:45]** I love it.

**[00:17:46]** Because, what does it do?

**[00:17:47]** Essentially, she does this, and that's why I'm asking again, because I'm not really sure anymore

**[00:17:50]** if that's still the way it behaves, let's say like this,

**[00:17:54]** you just described, whether I really need to have different models because

**[00:17:57]** in fact, paralyzed, exposed, then yes at that moment several subagents, each of which can run

**[00:18:03]** different routines.

**[00:18:04]** That means I no longer have an agent that performs this task, this loop

**[00:18:09]** but I might have 20 different instances and would it then

**[00:18:15]** still be the case, I don't know if that's already verified or not, whether what you just described

**[00:18:19]** is still necessary or if I can say no, subagents are

**[00:18:24]** already independent and they will also keep each other in check,

**[00:18:28]** if someone does something wrong.

**[00:18:30]** That is true in many cases and also, hmm, ah, too bad, too bad.

**[00:18:36]** So maybe, as they always say, everyone, maybe I'm also wrong, because

**[00:18:41]** as I say, I say Entropic and if that's wrong, let the one who

**[00:18:45]** pays for a subscription decide, I’ll say, whoever pays can say

**[00:18:49]** what it's called.

**[00:18:50]** Regarding Goal, Loop, and Workflow, those are functions and subagents that the Cloud, Code offers.

**[00:18:57]** Loop is something like, I don’t know, do something here at seven in the morning.

**[00:19:01]** Goal means, pursue a target and do it until it’s done.

**[00:19:05]** Workflow means, make a plan of subagents that pursue a goal.

**[00:19:12]** And not, that they work together with Intent, Act Check, and so on,

**[00:19:17]** but rather it’s considered beforehand, creating a JavaScript, that JavaScript

**[00:19:21]** orchestrates fresh sessions. So an Opus can spur a sonnet and say,

**[00:19:30]** let’s have 20 research agents, and you make me another five Opus-

**[00:19:35]** agents that summarize everything and then you make me another Opus-

**[00:19:39]** agent that summarizes the summary and plans it, who beforehand

**[00:19:42]** executes it and gives the result. And the advantage is that everyone has

**[00:19:46]** their own context. Everyone works in their context, everyone gets what they need for their work

**[00:19:50]** and only provides you the final result, without cluttering your context. And if

**[00:19:55]** you want to use that in combination, then, I actually have my knowledge gap.

**[00:20:01]** I don’t know if Slash Girl would automatically start workflow targeting.

**[00:20:07]** But I do know that if you set Claude to Ultra Sync, the property is

**[00:20:15]** precisely that, he says, okay, if I need it, I start sub workflows.

**[00:20:20]** Yes.

**[00:20:21]** So what does the world cost with lighting?

**[00:20:24]** My favorite topic is, I open Claude, I first tell him to plan the

**[00:20:29]** topic that I want to implement, so that everything is truly considered.

**[00:20:33]** Then I say, I usually use Slash Workflow to counteract with my skill as a constructive critic

**[00:20:41]** and meta-analysis, so the critic, who is indeed the skill that says what it will be six months later

**[00:20:47]** it happens that it was unsuccessful and the meta-analysis describes it that a foreign system

**[00:20:53]** would understand it.

**[00:20:54]** When the plan is sufficiently refined, I usually say okay, Ultrakode

**[00:21:01]** and Slash Goal and say at Slash Goal, implement the plan until the review agent, so my

**[00:21:09]** code quality and you name it or the critical critic or whatever

**[00:21:14]** says with a score of, so long implement the plan and then they go ahead and

**[00:21:21]** distribute workflows and power and hats and then they can also run, if necessary,

**[00:21:25]** 10, 12, 20 hours. That it costs many tokens lies in the eye of the beholder and not

**[00:21:35]** more on the credit card, because the tokens have already been depleted there. But

**[00:21:39]** that is certainly a different job than when you stand there and say, so,

**[00:21:44]** here are now 10 points on my checklist, could you check off the checklist? and then

**[00:21:48]** You look it up again and then you do this and that and the other.

**[00:21:51]** But just like you described it just now, I would also have the topic of Dynamic Workflows really starting additional sub-agents during runtime, for example.

**[00:22:03]** That's how I now see it works. So what you just described again is also something additional.

**[00:22:09]** It was also mentioned at several points, for example, Human in the Loop.

**[00:22:12]** That's also the interesting part, there are loops everywhere. I would say the more loops we have, the further the human is taken out of the loop and stands basically...

**[00:22:23]** That's the question of what you define as a loop.

**[00:22:26]** What do you define? So, with what goal are you aiming for, you know, in that moment. It's not exactly like that. So when you say, like with Claude Code, these Dynamic Workflows are, if I may bring an example, then it's also something like

**[00:22:37]** Analyze 100 competitors, then a few sub-agents run off and do

**[00:22:43]** price comparisons, others take off and would evaluate the UX of the competitor

**[00:22:48]** and others seek out market information on that, and afterward, it will be compiled.

**[00:22:52]** That's essentially like commissioning many small agents individually, that's

**[00:22:59]** essentially how these Dynamic Workflows work and they also operate individually.

**[00:23:03]** So many terminologies, honestly, are currently floating around,
 
**[00:23:09]** for almost always similar topics. There is a starting point and an endpoint somewhere.
 
**[00:23:15]** In the past, this starting point was actually just, it's beautifully said, also with the
 
**[00:23:20]** prompts. It was saying, okay, this prompt that I entered was maybe
 
**[00:23:25]** my starting point. There always was another starting point before that, because there already was
 
**[00:23:28]** always the system prompt before that, which also described how the system was supposed to behave
 
**[00:23:34]** . Yes, that was actually only expanded there, to the topic, of course you said it earlier,
 
**[00:23:38]** it's also becoming overwhelming for me now. But actually, it was only expanded to say,
 
**[00:23:42]** yes, continue until you have achieved your goal. So, what I could basically have had in such a
 
**[00:23:48]** single prompt, I could only really excel at that, there were always
 
**[00:23:51]** stop commands. Those of you out there who might have already worked a lot with cloud code...

**[00:23:55]** has done things like that. He also knows this topic, that you can get him into

**[00:24:00]** a mode for quite a long time where he doesn't

**[00:24:03]** keep asking questions. If he is doing something on your machine, for example,

**[00:24:06]** there is also the mode where I can say he is somehow

**[00:24:10]** in danger, you don't have that, I don't quite remember how that works.

**[00:24:13]** This number means you can also tell him to go into a

**[00:24:16]** Cott mode and just keep running without asking.

**[00:24:19]** That exists too, you can have a code, that's very nice, that

**[00:24:24]** allows you to switch between different modes with a key combination

**[00:24:30]** and then just tell him to keep going

**[00:24:35]** answers for me the Bastion fire.

**[00:24:38]** Yes, yes.

**[00:24:39]** And it is quite astonishing, especially, I would say, it punishes you a bit

**[00:24:45]** in terms of professionalism, how you deal with the system, because what I said

**[00:24:51]** Prompt engineering is dead, long live prompt engineering, is when you look at how

**[00:24:55]** different techniques existed back then, how do I build a prompt to achieve

**[00:25:02]** the goal, now you build a prompt that basically ensures that this loop is created,

**[00:25:08]** in which you say, with these things, what do I have to do, with what must I work, so that it is basically

**[00:25:17]** all consistent within itself, to achieve this goal. Yes, this topic of persistence is, yes,

**[00:25:26]** shall we still make an apology? That's very nice, yes. So this observes the results,

**[00:25:32]** Choose your tools with MCP and skills, trade through skills and co. What you need to do is check

**[00:25:38]** the results, keep the results documented, repeat the loop until,

**[00:25:44]** That's my loop engineering, you can also do that with skills, you can also do that with Python scripts, yes, with if, then, else and I don’t know what.

**[00:25:54]** Now it just has a fancy name.

**[00:25:56]** And it also goes faster, before I build it all myself, right?

**[00:26:00]** Once you get used to it, yes, it actually goes faster and I found the idea quite cool, for example.

**[00:26:06]** There are these loop databases. It's also nothing more than, they are about 80, 90, 100 characters.

**[00:26:14]** What do I know, how long Rode is, there are no open issues in your Gitme or some other nonsense.

**[00:26:21]** These are basically types of formulations, formulation aids, I would say.

**[00:26:25]** And I have now gone ahead and let Claude read the largest loop libraries that I could find.

**[00:26:32]** I said, so look, this is how a loop is structured, check out what formulations

**[00:26:37]** are chosen there and make me a loop creator skill, just like there is a skill creator skill,

**[00:26:43]** that basically helps me to see if there is a loop for it and it is integrated in such a way,

**[00:26:50]** that everything I am currently writing in the Cloth session, it evaluates.

**[00:26:55]** it has the kind of loop potential and if so, there's another discussion with me about it and

**[00:27:00]** asks, don't you want to make a loop out of that?

**[00:27:02]** Yes, discussion and then executing the loop.

**[00:27:06]** And that definitely exists, I mean I currently have these 2 skills that I have

**[00:27:09]** mentioned.

**[00:27:10]** Yes, there is also this Quill-Me-Skill, which asks critical questions until the

**[00:27:14]** topic is clarified and I believe with such a combination, it's definitely worthwhile.

**[00:27:19]** Just like before, right, think about it before you start.

**[00:27:23]** Today you can achieve great results with prompts, but if you think about it beforehand

**[00:27:28]** the system also helps you. You can then send it off, get yourself a

**[00:27:33]** nice coffee, it runs for about eight hours, delivering you billions of lines of code, it's

**[00:27:40]** maybe not automatically good. We have seen various

**[00:27:44]** libraries recently that help us, that there is some kind of skill that you

**[00:27:49]** are the laziest programmer who only writes what is necessary. Such

**[00:27:54]** things apply; you can integrate them, but I believe that this really requires a rethink

**[00:27:59]** in how people deal with costs, prompting, and thus also with the associated efficiency

**[00:28:04]**.

**[00:28:05]** Yes, you already mentioned the topic earlier that I wanted to pick up

**[00:28:10]** was the topic of context.

**[00:28:11]** It fits well with the other topic because you mentioned the Hermes agent earlier,

**[00:28:15]** confusing it with the Harnis.

**[00:28:17]** Last time it was always the C, today it's H.

**[00:28:21]** It's not a big deal.

**[00:28:22]** It's not a big deal.

**[00:28:23]** to get started. I think what's essential is when we move away a bit from such a world,

**[00:28:31]** where it's not necessarily the agents getting better, but these loops are

**[00:28:35]** actually a population of agents that work together with loops, so that we enter into

**[00:28:39]** a world. There, of course, the context and the harness will become even more decisive,

**[00:28:42]** because when it comes to the harness, I'd also consider harness engineering to include things like

**[00:28:47]** token monitoring, a model switcher in emergencies that can access local or non-local

**[00:28:52]** models, depending on how much reasoning might be needed,

**[00:28:56]** to be able to work with faster models. I think these are things that are becoming increasingly exciting

**[00:29:00]** plus, of course, the topic we've had more frequently in the show, memory.

**[00:29:04]** So where do I basically store the knowledge, so that it remains in context

**[00:29:11]** even when the loop is finished, even if the loop is perhaps finished with a

**[00:29:15]** agent. So we now had an example, Fable as well, where simply an

**[00:29:20]** agent, a model with its sessions is then turned off. Then it is

**[00:29:24]** of course a problem when all information from this student days long

**[00:29:29]** running loop simply disappears and is not stored in some other way.

**[00:29:34]** Because I believe it will become important that you not only

**[00:29:38]** save the actual output, which hopefully leads to the desired

**[00:29:42]** outcome, the actual decision, the actual code, which has come out, but in my opinion,

**[00:29:48]** it will also continue to be important to somehow capture the insights that the model or if the human was occasionally involved,

**[00:29:54]** also worked together with the human on the code, on the product that is being built,

**[00:30:01]** that these insights, along the way, as they say, the journey is the destination, so we should,

**[00:30:05]** I believe, you cannot emphasize this enough, in my opinion,
 
**[00:30:10]** that good loop engineering, in my opinion, also requires good harness engineering,
 
**[00:30:16]** with a reasonable memory file, second brain, that essentially extracts the insights,
 
**[00:30:22]** so that the loop can continue to work on that. Wonderful, whether the models underneath
 
**[00:30:26]** change. I think at this point, you can’t repeat this enough, because you
 
**[00:30:32]** You will agree with me, after we talked about the topic, how did you put it, what are we?
 
**[00:30:39]** Humans?
 
**[00:30:40]** Also?
 
**[00:30:41]** Yes, thank you.
 
**[00:30:42]** I'm also that calm.
 
**[00:30:45]** Gurus, gurus.

**[00:30:46]** Oh right, you agree.

**[00:30:47]** Yes, some call them nerds.

**[00:30:48]** Now imagine, there are indeed quite a few who are not so close to the technology

**[00:30:54]** without wanting to value that.

**[00:30:55]** At the definition, we also had a different approach to the technology.

**[00:30:59]** That's one side, not more extreme, perhaps the one that approaches it a bit more naively,
   
**[00:31:04]** that doesn't really need it at all.
   
**[00:31:05]** Yes, I use it.
   
**[00:31:06]** AI is becoming part of everyday life; it should disappear under the hood.
   
**[00:31:10]** Essentially, that's what you want to achieve, for example, with the Apple announcement
   
**[00:31:14]** to bring Siri AI in, with the idea that AI disappears from active usage,

**[00:31:19]** just there.

**[00:31:20]** On the other hand, there are the big manufacturers, Entropik, OpenAI, everyone wants

**[00:31:25]** to go public, everyone wants the latest big model, everyone, everyone, everyone wants everything and

**[00:31:30]** brings cool features. Then there are also things like OpenClaw and Harness,

**[00:31:35]** again Harness, Hermes Agent and Jarvis Agent, whatever all that stuff is called, that basically provide a different

**[00:31:42]** form of delivery and exactly this environment where they operate.

**[00:31:47]** the loops, which loops are available by default, how we support Loop, like Codex

**[00:31:52]** starting with the Slash Goal, then later came Cloud Code, and now Cloud Code comes with Workflows,

**[00:31:58]** whether that comes to Codex is debatable, but they don’t hold back, they learn

**[00:32:02]** from each other, and I find one thing very important here. These applications

**[00:32:07]** appear very strongly in the commodity environment. People subscribe, and the subscription,

**[00:32:13]** that they complete ensures that they use the tools, and maybe I use it like this

**[00:32:18]** as self-employed programmers, but they are not really corporate-compatible, like big

**[00:32:23]** companies compatible. It's more like, I install it, I use it, and if I want something else tomorrow

**[00:32:28]** then I just take something else. But when you think of big corporations and companies

**[00:32:33]** it quickly brings in things like certifications, very quickly some

**[00:32:38]** strange regulations come in, where you say, okay, that sounds like the old world,

**[00:32:42]** but it's not really the old world because everything has its purpose. I mean, things have come about

**[00:32:46]** because something happened. Maybe in Germany we tend to exaggerate sometimes here or

**[00:32:50]** there, that may be true. Nevertheless, it all somehow makes sense, and I have

**[00:32:55]** a bit of a feeling that with AI we can rein it in again, because if we build such a

**[00:32:59]** harness, building it ourselves has become much easier with AI. Then you can teach such a

**[00:33:07]** harness things like audit, sign, only use signed tokens. Audit,

**[00:33:14]** what you did, so that one knows, okay, the result was produced with this skill.

**[00:33:19]** Check every day, every hour, when an event occurs.

**[00:33:23]** And then you find yourself back at the question, okay, is everyone who works in the corporation or in such a

**[00:33:29]** large company an IT person, are you back at the one from earlier?

**[00:33:32]** No, not really.

**[00:33:33]** So, you have to speak the language, enable the functionality, and I find

**[00:33:38]** this story with, you have to control this rooster, because like I said the

**[00:33:42]** others are more doing this commodity product and enabling is for corporations,

**[00:33:47]** this thinking is damn frustrating. You can build something that basically, I'm a bit

**[00:33:54]** yeah, Germany could also have someone sit down and say, let's just build

**[00:33:57]** this German authorities harness, that sounds totally sexy, but if that ever

**[00:34:02]** would make it seriously, how do you say, in my opinion it has more bureaucracy than here

**[00:34:07]** no one, if we were to set up such a harness that everything would automatically happen in the background

**[00:34:10]** and be completed, then it would basically be a huge export success. Just like in the past games, when

**[00:34:16]** they were banned in Germany, FSK 18 in Germany, that was the bestseller

**[00:34:21]** of Doom, we remember from abroad. And I believe this is very much underestimated,

**[00:34:28]** what power lies in the harness and it is totally underestimated, but that

**[00:34:32]** is not a topic for a loop episode, that if you get people with a bit of expertise

**[00:34:38]** and a bit of guardrails and regulations involved, they can also build something with vibe engineering.

**[00:34:44]** Basically, let's say, I believe that if one

**[00:34:50]** now takes a closer look and reflects again, that we have talked about it today

**[00:34:56]** and also the development up to this point, then of course that is also

**[00:35:02]** small skill building about the first skill in D, that one has written before, then

**[00:35:07]** that was actually a precursor to harness engineering,

**[00:35:13]** because when I first say place, then basically what happens in today's world,

**[00:35:17]** whether those are sub-agents, whether it’s loop, whether it’s done with Hermes,

**[00:35:22]** or whether it’s done with Open Cloud, where loops are constantly being triggered,

**[00:35:27]** all the visas mean the same thing, it's essentially just a

**[00:35:31]** progressive stage in the old development of these topics at the moment. And I believe, we don’t need to

**[00:35:36]** be so, as it is just said now, just another IT guy. I believe IT guys

**[00:35:40]** essentially bring this expertise around the topic of developing software,

**[00:35:45]** that it can also be secure, into the mix. That is of course a huge advantage. I

**[00:35:51]** believe we don’t all need to be IT guys to build good Hanas. Also,

**[00:35:55]** everyone can start this on their own, I believe. There is also enough material,

**[00:35:58]** where one can read up on this. You can also ask your AI again because the exciting

**[00:36:02]** part will naturally be on the other side. You just talked about the big providers

**[00:36:06]** who also want to continue to make money. When we observe something like this, what then

**[00:36:11]** happens, with dynamic workflows emerging, other topics that arise with the big

**[00:36:16]** providers, they also see that of course. The harness is an important part. The memory

**[00:36:22]** is an important part. That’s why there are also memory files already in the current big

**[00:36:27]** agents that are being run with them. But this will also be a bit of a

**[00:36:31]** small competition between the large model providers, who naturally say,

**[00:36:35]** ha, the outside world is starting to think about model switching and such things.

**[00:36:40]** They may not always want to spend millions of tokens, but want to also

**[00:36:44]** find efficient ways to work with models of varying strengths, simply.

**[00:36:47]** I think it will be a little race between what you build yourself,
 
**[00:36:52]** what is smart to build yourself. And there will probably be a few IT decisions,
 
**[00:36:57]** that should actually be made by the IT landscape, if you are now operating at the scale
 
**[00:37:00]** of the largest corporates, for example. Compared to the topic of what is out
 
**[00:37:06]** there, what is coming from the vendors and what will become a commodity? So, what will
 
**[00:37:11]** there soon be a ChatGPT harness that is simply included? You know, where I just have to
 
**[00:37:15]** set it up and I'm in discussion with my OpenAI ChatGPT. Maybe I'm getting myself into
 
**[00:37:22]** trouble, it's not a protected area of terms anyway. For me, a harness is precisely
 
**[00:37:27]** this Cheshivity app or the Cloud Co-Work app or an Open Claw or a Hermes. I got it
 
**[00:37:34]** right. For me, that's a harness, because it connects, and what the harness does not
 
**[00:37:39]** provide, the user may have to painstakingly try to manually integrate. So after the

**[00:37:43]** Motto, I'm working on this so I have a memory. I'm working on this so that

**[00:37:49]** thing, I tell myself this caveman skill, so that the thing speaks like the caveman and

**[00:37:54]** talk, you have to save and so on and so forth. And I might want to push things

**[00:37:58]** a bit further. That's then the ha... because if Codex for example is a

**[00:38:02]** Harnis or let's say Code-Code is a Harnis, then for me, when people

**[00:38:07]** talk about an agentic OS, it's more the question of when multiple agents simultaneously

**[00:38:13]** work, basically the Harnis, controlling several agents in parallel, independently of one another,

**[00:38:20]** I would say at that point, corresponds to what my Agenteco is. Because then,

**[00:38:27]** that's basically the home not just for one loop that's running for you, which has, so a loop,

**[00:38:34]** that has sub-loops and sub-agents and everything included, but several loops running

**[00:38:39]** in parallel and stuff like that. Yeah, that would be a bit for me the, the attempt to express the whole thing linguistically

**[00:38:43]** to categorize a bit. What actually helps me a lot when it comes to the question, if you somewhere

**[00:38:49]** at a conference or elsewhere talk about things or speak with colleagues, to bring a

**[00:38:56]** bit of clarity, along the lines of what is a skill and what is a prompt and

**[00:39:00]** what is an X, Y, and Z. We already talked about it in the episode, you talk about skills, others say

**[00:39:04]** employees, development, you say skill engineering, what's going on there? And so I think

**[00:39:09]** this story with Hannes and where the LM is, can also be nicely represented like an

**[00:39:15]** onion. There was always further out, when you go, there's also a world of terms.

**[00:39:18]** And within it are the aforementioned loops and metaloops and you name it,

**[00:39:23]** again. What people should definitely take away from this, I believe, is,

**[00:39:28]** no matter how trendy it sounds, just because you’re not doing it, doesn't mean you're left behind. Maybe

**[00:39:35]** you're doing it without knowing it. Just because you're not shooting 50 billion tokens through the Erter

**[00:39:42]** and having a good result doesn't mean you're a bad AI user, but

**[00:39:47]** nevertheless, and I think we can make a small contribution with the following,

**[00:39:52]** to understand this technology, to say, yes, damn Ax, take a step back and

**[00:39:58]** really describe what the goal is and how I can recognize that I have achieved the goal,

**[00:40:07]** or how I can also stop in case of an error, and then have the chance to do something

**[00:40:11]** really quickly, I look it up, gather data and go

**[00:40:16]** from everything to, I don’t have to do everything in a loop, to, I just do this
 
**[00:40:20]** for as long as it takes to achieve the result and I have patience and I
 
**[00:40:26]** repeat and repeat and repeat, where you, when you do it manually

**[00:40:31]** you would also eventually say, you know what? I can't
 
**[00:40:35]** anymore. And last sentence, if you then let the individual steps run in a loop of an
 
**[00:40:42]** orchestrator and everything in its own models with its own fresh memory context,

**[00:40:48]** also Memory shared, but fresh context in the processing, then you can just let it run
 
**[00:40:52]** basically endlessly until either the golden invoice is sent,
 
**[00:40:58]** because you just saved the AI bubble by dropping your coins in or because the
 
**[00:41:05]** system simply reached a goal and not beforehand due to self-deception.
 
**[00:41:10]** I'm working with my context.
 
**[00:41:12]** Of course, I am the coolest in the world.
 
**[00:41:14]** Of course, I did everything right.
 
**[00:41:15]** Of course, I reached the goal because I deleted the test, I mean in my
 
**[00:41:19]** context that the tester was already set for the next round.
 
**[00:41:23]** You bypass all that.
 
**[00:41:25]** This even makes it more reliable.
 
**[00:41:27]** Point.
 
**[00:41:28]** Okay.
 
**[00:41:29]** Yes, I think we can actually wrap it up for today, that
 
**[00:41:33]** is to say, as perhaps it was also a significant leap in programming back then,
 
**[00:41:38]** when they introduced loops for the counter and not everything in one piece somehow in every
 
**[00:41:43]** single line of code all possible...
 
**[00:41:44]** If then, else go to.
 
**[00:41:46]** Exactly.
 
**[00:41:47]** Lines.
 
**[00:41:48]** Lines.
 
**[00:41:49]** Yes, but it's, as I said, when you think about it, it's similar, and that's of course

**[00:41:52]** on a completely different scale.

**[00:41:54]** I think we are leaving this topic, where yesterday I might have had to

**[00:41:59]** still input each individual prompt, each individual line of code, in order to get

**[00:42:03]** a result. Now we are already at the level where we are actually going beyond the

**[00:42:08]** IF loops, where we are programming loops. You just hinted at it

**[00:42:13]** with the orchestrator. We are probably heading into a future where we

**[00:42:17]** say, an agent will continue to do that for me, who has his own, we have

**[00:42:20]** talked about dynamic workflows, about subagents that are being set up. I think we're going

**[00:42:25]** in the direction that I essentially need less and less, that is still a good approach, always

**[00:42:30]** needing to understand what is actually happening in the background and less and less the individual

**[00:42:34]** line of code has to be prompted and programmed in conjunction with the AI itself, in that sense,

**[00:42:41]** but that a lot goes much more independently there, because that is what of course then

**[00:42:46]** simply makes it much more tangible for everyone when I concentrate daily and I found that a strong

**[00:42:51]** sentence from you, to focus strongly on the goal. What do I actually want? That would be

**[00:42:56]** our human task increasingly revolves around recognizing what the

**[00:43:01]** actual goals are that we want to pursue? What do we want to achieve and to actually

**[00:43:06]** focus more on the outcome in this case, what the result should be, rather than the

**[00:43:11]** Output then millions of tokens were? So I basically hope that these loops

**[00:43:16]** will also become more efficient, that you can incorporate things so that not just the

**[00:43:21]** machine foolishly burns tokens, but I believe it will then also lead to a good

**[00:43:25]** Listen to loop engineering, ensuring it's designed sustainably efficiently and not just saying,

**[00:43:30]** how it has been attempted for a long time by the major providers.

**[00:43:33]** You are only valuable if you also needed millions and five billion tokens.

**[00:43:37]** On the way, that's not true. So also David, I don't believe that anymore.

**[00:43:40]** Hold my beer! It should also simply be the case that you essentially,

**[00:43:44]** so for good loop engineering, for good harness engineering, when you're building around the memory,

**[00:43:49]** in my opinion it should also include working in a token-optimized way

**[00:43:53]** and not blindly trusting the machines for a long time just to keep going, even if they likely

**[00:43:58]** will eventually be able to do it quite well themselves, but I think that is inherently

**[00:44:01]** currently the situation that we say, when we are talking about harness engineering,

**[00:44:06]** it will also find its way into the models relatively quickly, they will

**[00:44:09]** also be able to do it quite well on their own. And yes, I think I'm like always

**[00:44:15]** optimistic, everyone should take another look at the topic if they're interested,

**[00:44:21]** build your own loops. See what works already, how one can do it over the

**[00:44:26]** Going beyond prompting can, in that moment, be done with the tools of choice that are available.

**[00:44:30]** I believe quite a bit can be achieved here. And the direction is definitely right for me,

**[00:44:35]** that's for sure, moving away from prompting individually, but rather concentrating

**[00:44:41]** more on an outcome and letting the machine find the way there.

**[00:44:44]** Yes, from that perspective, I would also say, if we could try it this way,

**[00:44:51]** now, yes, the goal is to listen to all episodes from us.

**[00:44:57]** Oh, check.

**[00:44:59]** If you've listened to one episode, see if there's another episode you haven't listened to yet.

**[00:45:05]** Listen to this episode again.

**[00:45:08]** keep checking until there are no more episodes left. Then you wait a week and

**[00:45:18]** starts the loop from Neum. And with this small gift from Loop, I would like to

**[00:45:25]** Today we'll say goodbye to you, and Jens, I think I've talked way too much.

**[00:45:31]** I shouldn't have rambled on about my cancellation rule. Thank you for

**[00:45:38]** that, do you have anything? Thank you for being here. You've received the loop statement and tune in

**[00:45:43]** next time when it will again be: Think Different, think AI. Bye.

**[00:45:49]** Welcome to Think Different, think AI, the podcast by Mark and Jens. Two technology-loving

**[00:45:59]** minds who not only talk about artificial intelligence, but live it. Here you will find clear

**[00:46:05]** classifications, real practical insights, and a fresh perspective on what is possible.

**[00:46:10]** Understandable, critical, and always with a wink.

**[00:46:14]** AI for thought, for a chuckle, and above all, for discussion.
