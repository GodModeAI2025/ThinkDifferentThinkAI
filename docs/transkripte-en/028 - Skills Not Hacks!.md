---
title: "Skills Not Hacks!"
episode_index: 28
published: "Mon, 23 Feb 2026 20:48:07 +0000"
duration: "2118"
audio_url: "https://audio.podigee-cdn.net/2371082-m-8ebcaf2f208d0560668bb1e81d5169b9.mp3?source=feed"
guid: "04446b3d50eb91eade28f7905a15da26"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T20:53:45+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/028 - Skills Not Hacks!.md"
translated_at: "2026-04-29T08:42:09+00:00"
---

# Skills Not Hacks!

**Published:** Mon, 23 Feb 2026 20:48:07 +0000
**Duration:** 2118
**Audio:** https://audio.podigee-cdn.net/2371082-m-8ebcaf2f208d0560668bb1e81d5169b9.mp3?source=feed

## Description

Why prompting less brings more and how skills revolutionize AI interaction. With real examples and practical tips.
In this episode, we dive deep into the world of skills and show why they are the better alternative to constant prompting. Together, we discuss how AI systems, with the right skills, become not only more efficient but also more user-friendly. Using practical examples, from baking bread to automated PowerPoint presentations, we explain how skills work, how to create them, and how to use them effectively. We talk about skill libraries, security aspects, and the difference from classic prompt strategies. If you want to know how to really make your AI productive, tune in now!

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here there are clear classifications, real practical insights, and a fresh perspective on what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Food for thought, to chuckle, and above all to discuss.

**[00:00:33]** Welcome to a new episode of Singtiff and Sing AI.

**[00:00:37]** We thought today we would talk about how to use skills to prompt less.

**[00:00:44]** Today I'm once again not alone, but today I'm in familiar company, namely without a guest,

**[00:00:52]** but instead with Jens. Hi Jens, great to have you here.

**[00:00:56]** Hi Mark, yes, every now and then it still happens that I can't be in an episode.

**[00:01:02]** I'm already looking forward to the episode when I will be here alone and do an episode.

**[00:01:07]** You could be very curious about that.

**[00:01:09]** I don't know the topic yet, but I'll think of something.

**[00:01:11]** This time I'm really glad to be here, Mark.

**[00:01:14]** And we really have such an exciting topic,

**[00:01:17]** because we've been talking about new bot forms and such things lately.

**[00:01:22]** We're talking about what connects all of this, no matter which company these things come from,

**[00:01:27]** that now agent skills are somehow different, I've said that before, this word skills,

**[00:01:30]** you just mentioned it too, today we want to shed some light on it. What are

**[00:01:34]** these skills, these abilities that I can give to my agents so that they in the

**[00:01:41]** end deliver better results? You've already said something important, it's

**[00:01:46]** not about the skill I have as a person, that I’ve gotten some certificates

**[00:01:52]** from somewhere and can prove that I've attended great trainings, but rather about the possibility

**[00:01:57]** to give skills to the systems so that we can move away from that. I mean, what was the

**[00:02:03]** term that was all the rage a while back, yes prompting strategies, prompt frameworks,

**[00:02:10]** prompt engineering. At the end of the day, all of that ends up being reflected here, but I would

**[00:02:16]** suggest we start with a little overview. What are skills actually,

**[00:02:22]** I'm going to say now, include, before we might take a deeper look.

**[00:02:27]** I will put something in the room and then you can correct again. So I would say,

**[00:02:32]** that it is quite similar to the example with humans. So a skill is,

**[00:02:37]** for example, if I can bake good bread. That is a skill where I say, if someone now

**[00:02:44]** prompts me to make breakfast and I have this skill of baking good bread, then that is already

**[00:02:50]** not a bad quality to produce a good breakfast, and in that case if

**[00:02:56]** someone just says make a good breakfast, I will start because of this skill that is available to me

**[00:03:01]** to also bake bread beforehand, I would set my alarm earlier in the evening

**[00:03:06]** so that I can get up at night and bake the bread, that's how I want to

**[00:03:11]** make a little bit of space, but that's how it is. So it is a bit like what you can also

**[00:03:14]** compare with human qualities first, so the human additional

**[00:03:18]** Skills that we learned in social situations, learned in the family,

**[00:03:23]** learned in friendships, through hobbies or in school, in training

**[00:03:27]** and at work, those skills enable us to perform certain specialized tasks

**[00:03:34]** effectively.

**[00:03:35]** And if someone calls you and says, 'I would like some bread,' you'll be able to

**[00:03:40]** look it up. And I want to briefly shift to technology now,

**[00:03:44]** yes, because if I ask Cloud Code or ChatGPT to bake me some bread, right now

**[00:03:51]** not much comes out. Unless I have the skill that talks to my bread machine,

**[00:03:56]** but briefly, what are such skills, yes. So skills are either

**[00:04:02]** with a point skill or they contain things like Skill MD. MD stands for Markdown,

**[00:04:08]** which is a kind of text format, where you used to say pig's card back then,

**[00:04:15]** today people say Heschzeichen, for example outline level, how to define headings.

**[00:04:20]** And then you basically write in what is the trading instruction?

**[00:04:25]** You also give an overall header, they call it Jammel-Hetter, but let's set that aside,

**[00:04:30]** there is basically a title and a description, the title could be.

**[00:04:35]** What shall we take that is nice? Write me a totally great text for social media to promote podcasts.

**[00:04:43]** So you have a title, podcast advertising. You have a description, which states, I am the great image that is capable of,

**[00:04:51]** finding exactly the right tone for the mega-successful ZinkGIF and ZinkAI podcast for promotion on social media.

**[00:05:00]** The Markdown part would then describe how such a message is structured? Yes, you had a title, you had content.

**[00:05:05]** So no title today means it is Huck, so that people stick around when they see it on social media.

**[00:05:11]** Perhaps there are also specific commands in there, like how to generate images, so with Claude I am also able,

**[00:05:20]** to provide resources in such a skill, provide AP calls, MCP calls.

**[00:05:27]** I can even provide Python code, which is then really processed rigorously and then you could take it that far,

**[00:05:36]** that if I have written this skill correctly, the system does not process it rigidly like a program code,
 
**[00:05:43]** but nonetheless, instead of me writing 30, 40 prompts here, give me a hook, give me a text, make me an image, upload this for me,
 
**[00:05:52]** Can you give different capabilities to such a skill when I interact with my AI system in the future and I write something and the system notices,
 
**[00:06:04]** Mark is currently writing podcast promotions on social media, he surely means this skill,
 
**[00:06:11]** because there is something in the description and the title that suggests he thinks this can be used.
 
**[00:06:17]** that it kind of gradually works through it to produce a result.
 
**[00:06:23]** And maybe now a small different example, before I take a breath again.
 
**[00:06:27]** If one thinks, okay, we all don't have podcasts, what is this example about?
 
**[00:06:31]** I want to take a much more striking example.
 
**[00:06:34]** Perhaps we all know, who work for a company, the topic of PowerPoint templates.
 
**[00:06:41]** PowerPoint templates are characterized by sometimes being more or less extensive.

**[00:06:46]** But they have a corporate document, they have a title, there are various pages that show, then there were transfers, graphics, charts, bullet points on title slides, subtitle slides, closing slides.

**[00:07:00]** People such stuff there are color values there might also be somewhere such pictogram databases

**[00:07:08]** where you get a whole bunch of pictograms like how do I show a tree and how do I show a dog and

**[00:07:14]** I don't know what in corporate style and it could, for example, go to Claude and say you

**[00:07:20]** run that through, look at that, build a skill, discuss with me until I

**[00:07:28]** I believe you've represented the skill well. There are test runs involved. There are

**[00:07:33]** then feedback included. I still remember, because the first time I said,

**[00:07:39]** why did you actually learn that, it doesn't look like it's supposed to. He then

**[00:07:44]** apologized. Yes, and at the end of the day, when you are finished, you have a skill,

**[00:07:49]** that is capable of making slides. They might not be at the level of the

**[00:07:55]** star designer, but I don't know if you recently saw anything from me, they don't look like they come from a star designer either.

**[00:08:00]** No comment.

**[00:08:01]** But you have it immediately in the right font, in the right layout, with the right imagery, and that is really cool.

**[00:08:11]** Especially when you also make it available to others.

**[00:08:15]** Exactly, that's another interesting point we'll go into shortly, this making available to others.

**[00:08:21]** I want to bring up another example, because you've already mentioned high sophisticated again,

**[00:08:25]** and you've even created your skill with AI again.

**[00:08:28]** Well, but if we simplify it again, it is, as I said, the skill is,

**[00:08:32]** basically, it's important to understand that it is not a tool, it is not a plug in that sense,

**[00:08:36]** and it is not an API key that I just use, but it is a bit

**[00:08:40]** about describing behaviors, what should happen.

**[00:08:45]** For example, if I say you are now the skill for a senior code reviewer.

**[00:08:52]** So a person who should look at the code again from a senior perspective,

**[00:08:56]** he has to go through several steps where he would independently read the code,

**[00:09:01]** define it in the skill. He should follow certain standards, programming standards,

**[00:09:05]** that he looks at. Then he should see that he maybe creates a test plan,

**[00:09:09]** then he should give a structured review, and then he should maybe create a risk level for any errors,

**[00:09:15]** he found during this review. That would be a very simplified depiction of the skill I could have.

**[00:09:23]** This is interesting and what I've already hinted at. This is that this skill now, because it exists in such an MD,

**[00:09:29]** or in such a Markdown file and is actually just a description of

**[00:09:34]** governance, of a behavior, is of course totally portable. That means, once I have created it,

**[00:09:41]** I can also make it available to any other model, any other bot. That I say,

**[00:09:47]** this skill is so well described and regardless of which model is working with it, it fulfills

**[00:09:53]** its purpose completely. I think that's another really interesting point because it's so,

**[00:09:57]** that's why there are already some skill libraries like this, but I also believe

**[00:10:02]** there's a whole new world beside tools, plugins, blah blah blah, all that is out there

**[00:10:08]** that there are now skill libraries where I can download good, verified, hopefully

**[00:10:15]** skills so that my AI doesn't misfire,

**[00:10:20]** at that moment.

**[00:10:21]** And today, we will again open the big security topic, as we've discussed in some previous episodes,

**[00:10:24]** but of course, also take caution with the skill download mode,

**[00:10:30]** that you are using.

**[00:10:31]** So always make sure that your skills are also reviewed again when you

**[00:10:33]** perhaps download them.

**[00:10:34]** What does that essentially say to your AI, how it should behave?

**[00:10:37]** That's what I meant before with the markdown file.

**[00:10:41]** Yes, you have a text file that describes what the thing does,

**[00:10:46]** and it's worth taking a look at it because it looks nicer in markdown.

**[00:10:51]** There are tools on the market where you can throw it in and get it nicely formatted.

**[00:10:55]** You can print it out, you can view it on the screen, it's no big deal.

**[00:10:59]** And now maybe unfortunately, something technical again,

**[00:11:03]** if you get a point-skill part and you think, 'Now I was told,

**[00:11:10]** markdown, I'll go into the editor,' you won't see anything because this

**[00:11:16]** point-skill part is actually a zip file, which means you have to rename point-skill

**[00:11:21]** to point zip, then you can unpack it, inside you will find the

**[00:11:24]** markdown files. Why is that? Well, you are delivering a container, so

**[00:11:30]** this point skill file, where various things are included.

**[00:11:33]** There are resources included, such as you can provide images, there are

**[00:11:38]** Markdown files included, these descriptions of the instructions, there is the

**[00:11:42]** header included, and so you don't have to provide everything in individual files to the system

**[00:11:47]** you can also develop it in the software, there are things like

**[00:11:51]** cursor and vintner, whatever they are called, you can drop all the

**[00:11:55]** skills in there, the point skill files, and so that you only have to drop this

**[00:11:59]** file, as I said, once and not all the little contents individually,

**[00:12:03]** it is saved by the system as a pump skill, which is actually just a zip archive

**[00:12:09]** with a fancy name for those who were paying attention earlier. What did you call the hashtag

**[00:12:15]** called? Pig Gutter? I had to quickly chime in here, I have five or six

**[00:12:19]** minutes. I learned on a typewriter. A nice lady came

**[00:12:24]** with a towel and laid it over her hands and it was still called Pig Gutter back then.

**[00:12:30]** Okay. So in our case, it was called Pig Gutter. I have a technical training. Maybe that’s

**[00:12:37]** still important for the context. Okay. Now not everyone among our listeners is always

**[00:12:45]** the one who deals with Sipfalt or other topics. Where can he find skills today?

**[00:12:50]** are there in the normal chatbots from OpenAI, from CloudCord. Are there already skills,

**[00:12:59]** that can be used, that I can turn on? To be honest, I stumbled into the topic of skills

**[00:13:07]** by trying it out. I uploaded my first skill with CloudCord without zip folding.

**[00:13:13]** I just told it, look, I need a skill, I've heard,

**[00:13:17]** they are cool and then basically asked it to help me with it and then you immediately notice they are already grabbing

**[00:13:25]** skills because you see in the chat how it states or the user wants to create a skill I

**[00:13:29]** will load the skill creator skill, and then you can have a kind of conversation with it.

**[00:13:35]** playing a long question-answer game until at the end of the day he is of the opinion that he can give me a skill
 
**[00:13:41]** and I promise then that it will stop and then hopefully, it will start again at some point
 
**[00:13:46]** I hope at least, then you'll get, if it’s a very simple skill that you
 
**[00:13:51]** don’t need any resources or anything for, you’ll also get the skill point MD file,
 
**[00:13:56]** so just this Markdown file and then it offers you, should I include this in my library
 
**[00:14:02]** would you like to download it, and when you download it, you’ll get
 
**[00:14:07]** this Markdown file and you can throw it everywhere, you can throw it in the Geminer
 
**[00:14:11]** Just like how you would also throw in a prompt. So copy and paste,
 
**[00:14:19]** name it whatever you want. However, it would then also only stay in context. So for the
 
**[00:14:24]** normal standard user now at OpenAI, if I would do that then it would
 
**[00:14:27]** essentially behave in that thread that I have open, in that case, the AI would
 
**[00:14:33]** actually behave like that. I think I should also mention, it also depends
 
**[00:14:35]** on whether you are only a non-paying user in quotation marks. Also, the
 
**[00:14:39]** things that are at Claude are also the pro and enterprise and such variants and
 
**[00:14:45]** max variants that you can buy, where you can work with the skills. But of course
 
**[00:14:50]** I can, and this might be important to mention as well, I can of course take skills
 
**[00:14:55]** in this structured form, get them from elsewhere and then also throw them into a thread like this,
 
**[00:15:01]** so the AI can handle better, because that is a structured
 
**[00:15:04]** way of how it behaved. Just important, if you are not
 
**[00:15:08]** going there, in case we paid at the moment, then it would only be provided to you in that
 
**[00:15:11]** fractal, again depending on which provider you are currently at.
 
**[00:15:15]** I think the skills system at OpenAI is even stronger, so they are still working on it,

**[00:15:19]** coming. That is actually the output of the cloud, I believe that is among the

**[00:15:22]** farthest with the skill topics. They introduced it relatively early on.

**[00:15:27]** They also started it with CPTGPT; if you

**[00:15:32]** create the event CPT there, for example, it also says,

**[00:15:36]** What should the agent's behavior be and so on, you can also copy these

**[00:15:41]** Markdown contents very nicely so that you basically

**[00:15:48]** have it like that, why approximately?

**[00:15:52]** You can only get the Markdown part in there.

**[00:15:56]** You can't just throw in everything, like saying, okay, I'm just going to

**[00:15:59]** throw in all the resources, you can get everything in the chat,

**[00:16:02]** but it doesn't behave quite the same way as with the skill.

**[00:16:05]** With the skill, it knows that it belongs together, it works together, it is addressed

**[00:16:12]** in the context of the chat, when I need it, while if you just copy it into the prompt

**[00:16:17]** then you just have the system instruction, so the Markdown part thrown in,

**[00:16:24]** then maybe you later throw in some files, the qualitative

**[00:16:27]** result at the end is not quite as good, but if you stick to these skills,

**[00:16:33]** say, this is how you research. This is how you prepare something for me. That is important for me to

**[00:16:38]** generate a hook. This is it, that, the other. Then the systems do not

**[00:16:44]** make a distinction, and then you can create skills, even with tools of your choice.

**[00:16:49]** You don't need to conduct the interview in Claude for a skill. You can

**[00:16:53]** simply say, dear Stretchability, dear Gemini, dear

**[00:16:56]** Mistral. I am providing you with some information here,

**[00:17:01]** structure it for me so that it is in nice Markdown; then you basically have a skill, also a

**[00:17:08]** One would say this is a work instruction, and it's somewhat similar for a career.

**[00:17:13]** Yes, I believe, to offer nothing to make it good again, to come with Gemini, I think the skills are

**[00:17:20]** closest. Yes, I think there are gems or something like that at. These are kind of role stories at Gemini, in principle,

**[00:17:25]** that are somewhat similar, where there is a role description. Because we knew that from this

**[00:17:29]** early time of prompt engineering, where it was always said, if I want to write a good prompt

**[00:17:35]** then I have to formulate my goal clearly and ideally, I also have to tell the AI buddy

**[00:17:41]** what kind of behaviors it should exhibit. And that is what is now

**[00:17:46]** actually in skills or jams or whatever you want to call it. And these behaviors,

**[00:17:49]** that has opened up. Because it's smart to out-source that. If

**[00:17:53]** it's essentially from the, from the interaction, so from the communication with the bot, which is then, in

**[00:18:00]** principle, the prompting in that moment. If I don't have to say again every time, behave like

**[00:18:05]** my uncle hasn't seen or something like that. Or am I behaving like Steve Stocks, or am I behaving

**[00:18:11]** like this or that, or am I behaving like a good programmer, or am I behaving like a teacher

**[00:18:14]** for languages or something like that. So I don't need those kinds of things to prompt over and over again,

**[00:18:20]** Essentially, we're talking about the idea today that it means,

**[00:18:26]** I have to prompt less to get better results because the AI understands through the skills,

**[00:18:35]** that I either provide in the moment or as a file somewhere,

**[00:18:40]** where she can then still access it or smartly access it herself,

**[00:18:44]** Because of course, when you offer thousands of skills or 100,000,

**[00:18:50]** Providing skills is, of course, also smart, so that the career doesn't load all skills

**[00:18:53]** but just an image, as you described, simply loads the skills as well,

**[00:18:56]** that are necessary to inherit a certain task well.

**[00:19:01]** One must not forget also the selection of a skill, but rather the invitation

**[00:19:06]** into the system.

**[00:19:07]** The system then notices, okay, there is a skill that I need, or is there even

**[00:19:11]** one.

**[00:19:12]** I load this in, that’s already the so-called tokens for your request. This means,

**[00:19:18]** it makes sense, if you want to operate more professionally,

**[00:19:23]** maybe also to start with something like orchestrator skills, that you say, okay, I have

**[00:19:28]** a skill that basically selects the appropriate skill and has its own set of rules so that you

**[00:19:33]** don’t just have a list of 1000 skills, but the orchestrator essentially says,

**[00:19:39]** okay, fine, we are developing, maybe it will lean more towards this guild,

**[00:19:43]** a text will be created and maybe this will be the guild. But those are, I’d say

**[00:19:47]** advanced technologies. And as you mentioned earlier with discussions,

**[00:19:52]** like those jobs and so on, we talked about it in my episode, I had built this advisory board

**[00:19:57]** back then with N8N. I then went and threw this advisory board into the

**[00:20:02]** AI and said, can you please provide this as a guild? And

**[00:20:06]** it did exactly that. It created an orchestrator skill, which is the one that defines

**[00:20:13]** the topic, selects the experts, and then interviews the experts accordingly.

**[00:20:19]** All the information was processed in there. It ultimately became a huge

**[00:20:23]** part of skills at the end of the day, but only partially, due to zip, compression,

**[00:20:29]** but that’s another topic. And then you can give it this, and when you tell it,

**[00:20:34]** ‘Hey, I need the advice of the experts,’ then the team goes and says, ‘Advice of the experts,’

**[00:20:40]** experts.

**[00:20:41]** I’ll look for it and check it out and then you see it gets really lively in the chat because then

**[00:20:47]** he starts and says, yes, now Elon has to be with Steve, with the Osnack, with whom

**[00:20:51]** always discussing that, and in the end, something comes out.

**[00:20:55]** You're thinking, okay, we talked about this topic last time when we discussed it back then,

**[00:21:00]** does it actually make sense to give the different people with

**[00:21:03]** or not, but I still think that it's a very cool result

**[00:21:08]** that is much more than if you don't have all this contextual knowledge of the person from them

**[00:21:13]** you had given. And maybe, with all the nerdy talk today, which might

**[00:21:20]** be a bit difficult for one or another, I just realized how

**[00:21:24]** often I've completely lost the context in my head with Skill and Skill MD

**[00:21:29]** could. An important story that each of us can tell is to take a piece of paper and

**[00:21:34]** a pen and according to the old process knowledge, write down what you are doing, what you have written down,

**[00:21:40]** because when you document that for some time, you're getting into your topic, what occupies

**[00:21:45]** you constantly, what are the topics that may just annoy you, yes, because I have to

**[00:21:49]** here again, no idea, end of the month, collect all the receipts from the bank and

**[00:21:55]** I sort them by the term ABC and for taxes, it's important with the VAT

**[00:22:00]** as well. You could also consider, I say, you know what, I'll make myself

**[00:22:05]** a skill. The thing should take the PDFs or whatever I get from the bank in statement extracts,

**[00:22:10]** read them out, create folders, place the stuff there, and then you already have

**[00:22:17]** written a work instruction that the agent processes. It helps you. Yes,

**[00:22:23]** it frees you from the terrible things and the annoying things, and you can assume that if ever

**[00:22:29]** a mistake should happen, you adjust the skill and from then on it will work better in the future.

**[00:22:35]** As bad as today, AI will never be again. And the point you had in the preparation, 

**[00:22:41]** when you throw over the fence, I think it's worth mentioning at this point again,

**[00:22:46]** that these skills not only serve to give you a better result.

**[00:22:52]** So I distribute the bank bookings into a folder for accounting or I create

**[00:22:59]** a PowerPoint, but also to guide him on how he goes about this, so that he keeps following this path,

**[00:23:07]** step 1, step 2, step 3,

**[00:23:13]** and that he also documents what have I just done? Because imagine, you give him the

**[00:23:21]** task to reorganize my hard drive.

**[00:23:24]** I also mentioned this recently with Claude Co-Work, you have a 4TB drive

**[00:23:29]** and he is supposed to come up with a folder structure and naming conventions, and if he does this

**[00:23:35]** without you telling him, then he will do it, but eventually you will notice,

**[00:23:39]** why are the folder names different now and the file names have changed, why?

**[00:23:44]** He has changed the scheme, and that is simply because

**[00:23:48]** at some point the context was so full that he no longer knew, like a goldfish, what was

**[00:23:53]** happening just two minutes ago? But if you tell him, create a memory, save your

**[00:23:58]** decisions, save special cases, note the follow-up questions, then at least you have more

**[00:24:04]** security for this work case, 100 percent doesn't exist, but more security that he stays

**[00:24:11]** on track. And if you store this more generally, then you quickly return to

**[00:24:16]** our favorite crab OpenClaw and Co. That remembers not only step by step,

**[00:24:22]** but in a more general way. But I know. Yes, yes, all good. But then, because you just brought up a

**[00:24:28]** good point. Now you've mentioned memories. So now for example, I think,

**[00:24:32]** we can make a little distinction here. Just a Skill and Memory Files. No,

**[00:24:37]** because of course with OpenAI, I don't even know if that is included in this $20 paid version

**[00:24:42]** and not in the lower ones. Essentially, there you can also say Open-R, remember 

**[00:24:49]** I want a text, for example, to be written with emojis. When

**[00:24:54]** I say, write me the next link in the article, then use some emojis because

**[00:24:59]** that’s my style. What we are discussing, that I discussed with my Chatchapity variant

**[00:25:04]** is partly stored in this memory file, because it knows,

**[00:25:09]** for example, that I am discussing such an episode, that I will soon do an episode about some topic

**[00:25:14]** about the market, then ChatGPT knows the context from this memory file. Why,

**[00:25:21]** what I mean with my podcast and what I then do with it. That’s just a bit

**[00:25:25]** different than skill. Skill is more clearly defined behavior in my opinion

**[00:25:31]** and should still be established, so to set the governance. Memory goes a bit beyond that.

**[00:25:34]** I think that’s a slight difference that isn’t always so clear,

**[00:25:40]** which should be distinguished.

**[00:25:42]** Between a memory case that knows all context and more about my personalities.

**[00:25:48]** And skills that actually describe potential specialization abilities at the moment.

**[00:25:57]** So I would roughly distinguish that, because I think it's also important to understand.

**[00:26:01]** Memory overall file might be even more powerful, but it will also become
 
**[00:26:08]** larger and could also have more errors compared to perhaps a very specialized skill.

**[00:26:13]** the file that I can also port when I can load the motor and other things like that I would

**[00:26:16]** then distinguish clearly and I have that it is also not like you have to remember that

**[00:26:23]** the thing if it now structures my hard drive has to remember for eternity

**[00:26:27]** what the file names are, while whether I eventually, I don't know, drink my beer more on Sundays

**[00:26:33]** and accordingly more recommendations for my future brewing, could possibly

**[00:26:39]** depending on the situation be more important to me than, as I said, the mentioned file folders from the backup hard drive.

**[00:26:45]** What I believe should stay with you all from this episode today is,

**[00:26:51]** that if you've never dealt with prompt engineering and so on, basically,

**[00:26:56]** just write it down and it will produce results, results are good. Then that's fine. Personally, I have now

**[00:27:02]** also come to the realization that I can find a more sustainable solution with these skills,

**[00:27:09]** because it definitely provides more fun, joy, and better results to engage with the topic of

**[00:27:17]** skills. Yes, I am more of a skills person, yes, others might be more the

**[00:27:23]** jams person, and others I don’t know, whatever the systems are called, but because

**[00:27:28]** it's open source, and I will say, in various software products it is also

**[00:27:37]** supported, maybe today in software movement, but who knows, maybe some

**[00:27:42]** requirements engineers, tax consultants, I don’t know what else, people who

**[00:27:47]** work in their systems with one system, and that system maybe internally

**[00:27:53]** uses different skills to provide features or acts as a partner

**[00:27:59]** or whatever is available, and I would like to promote that.

**[00:28:04]** What I mentioned earlier with paper and pen, also write down what you do,

**[00:28:09]** and what you have written down. First of all, to find out for yourself what the

**[00:28:11]** annoying tasks are, because we should look at those first and then also

**[00:28:15]** think about how to transfer it into markdown, then it already looks nice, yeah,

**[00:28:20]** then you can also give it to your colleague as a vacation substitute or at least

**[00:28:25]** see how the machine handles it, and yes, I think that would be my message that I

**[00:28:31]** would really like to share with everyone. I think that's good, I would go one level of action higher

**[00:28:36]** and say, actually it's also a bit, if you want to make a very

**[00:28:40]** light architectural image, to say how these different things

**[00:28:45]** are, I would say then this skills layer is clearly one, this behavior and reward layer, where I apply different behaviors,

**[00:28:54]** secondly, different rewards according to the norms, when you look for errors or similar things,

**[00:29:00]** I can place that in the skills.

**[00:29:02]** Then you have the next layer, something like, we often talked about the MCP or the Tool Layer.

**[00:29:09]** If you will, the AI then accesses its skills, its behavior, how it should behave, to possible tools, whether that is web browsing, whether it's 3D rendering, or whatever, then executing those through a tool.

**[00:29:27]** Baking.

**[00:29:28]** Bread baking.

**[00:29:29]** The bread machine in case of emergency, that can then be, the skill would be that the bread

**[00:29:35]** must be kneaded with love again, and other things about what you do.

**[00:29:40]** And then I essentially have the third layer for me, the One Time layer, where that

**[00:29:43]** actually happens.

**[00:29:44]** There we are then at the layer of the actual, whether that's a AI model in a

**[00:29:51]** context window only, whether that's an open cloud in the one time, on which these things

**[00:29:56]** can run in that moment. I think that's a little bit, if you want to place it electronically.

**[00:30:00]** This skill against an AI model, or an agent network,

**[00:30:06]** or a bot like an open cloud that tries to independently continue to do things, so that you can somewhat differentiate.

**[00:30:11]** Skills, behaviors,

**[00:30:16]** to the tooling layer and then you have the one-time layer where something happens, where also things

**[00:30:21]** are executed, which then essentially uses the available tools as well as skills.

**[00:30:27]** And all of this is supplemented by the actual prompt that comes from us, which contains the

**[00:30:32]** task I want to have done. I find it really difficult today, I think,

**[00:30:39]** to follow us. I'm never sure. I'm very curious about the comments. But also something like that

**[00:30:45]** needs to be addressed because we had, if we briefly touch on the last

**[00:30:49]** Yes, listen to the episodes. Greetings again to Alex, Klaus from last time, where we said,

**[00:30:55]** it's not just the technology that there is a new model. It's not just the human who has to figure out

**[00:31:02]** how to use this new world. Yes, we are now writing the skills, for example. It’s

**[00:31:06]** also the complete interaction, when you think about how things work together, because now

**[00:31:12]** I write a skill that perhaps deals with a topic that I work on, but if I

**[00:31:16]** include two or three things from my colleague, I am practically cutting work packages. From

**[00:31:22]** that perspective, it is a very powerful world, and that's why I found it very important that we talk about

**[00:31:28]** this technological basis, skills today. Maybe a funny anecdote,

**[00:31:34]** a colleague of mine today was told by Claude that Claude couldn't solve a problem.

**[00:31:40]** That’s good, that shows that the human is still in the loop. I found that very funny,

**[00:31:45]** yes, so from that side a little humorous activity. You’ve already hinted a bit,

**[00:31:51]** pre-discussion, about what we will talk about next time, and I would like to tease a little

**[00:31:55]** for next time. Could you maybe give us two teaser points,

**[00:32:01]** before we wrap up for today? So if we take a look,

**[00:32:06]** if we quickly glance over the last few years of AI,

**[00:32:10]** we have come from the Ahamut, to JGPT, we’ve gone through prompt engineering,

**[00:32:15]** we’ve gone through possible workflows, through workflow engines, to now

**[00:32:21]** in 2026 nearly self-working AI bots that are out there,

**[00:32:29]** running around the internet in crab forms.

**[00:32:32]** And we are slowly entering a world where it’s not just one of these bots,

**[00:32:37]** where I don't just have one bot equipped with skills and tools and you name it,

**[00:32:41]** but certainly in my orchestration layer, I then have many of such bots

**[00:32:50]** out there.

**[00:32:51]** And what Mark and I have observed in the past weeks is a trend

**[00:32:55]** on the internet, that some of these colleagues, who also run 15, 16 AI agents in parallel

**[00:33:02]** are starting to equip them with a so-called gaming UI, where they can then observe

**[00:33:09]** and also orchestrate what these AI agents are doing, because you might not want

**[00:33:13]** to give everything via prompts anymore, but perhaps want to display a kind of cafeteria

**[00:33:20]** where the bots that are currently busy meet during their idle time and

**[00:33:26]** I can then decide as a human again in Belube that I say,

**[00:33:29]** You know what? If the watcher is hanging out in the cafeteria all the time and using idle time,

**[00:33:34]** then I’ll kill him now, because I’d rather wait for a new task to come.

**[00:33:39]** No, of course, I’m not going to kill him, I really won’t kill him.

**[00:33:42]** Not kill, man, you should assign the tasks, so.

**[00:33:44]** Yes, yes, yes, exactly.

**[00:33:45]** Ah yes, but as I said, there are definitely things, now, that you can do outdoors

**[00:33:50]** really to conduct such an Orkestation, building gaming UIs and we will or gaming

**[00:33:57]** similar UIs and we would really like to talk about that in a complete episode and I'm very much looking forward to it because it's one of my favorite topics.

**[00:34:04]** And Mark is also very eager for this episode and we've been planning it for ages, I think, it's been ages in this AI.

**[00:34:11]** You've nearly, well, for about three months, and we've been planning it for ages and now we're doing it.

**[00:34:18]** And if you don't want to miss it, tune in next time. We've never hinted so strongly beforehand that it will happen.

**[00:34:24]** But this time we are doing the fire-sage, Jens.

**[00:34:27]** Yes, next time we will do the episode.

**[00:34:29]** Let's see if it works out, if you liked the episode,

**[00:34:31]** then leave a comment, stars,

**[00:34:34]** whatever is possible on your platform.

**[00:34:37]** And we look forward to the next time at Age of Agents.

**[00:34:42]** Until then.

**[00:34:43]** Ciao.

**[00:34:44]** Until then.

**[00:34:46]** Welcome to Think Different, Think AI.

**[00:34:49]** The podcast by Mark and Jens.

**[00:34:52]** Two tech-loving minds who not only talk about artificial intelligence but live it.

**[00:34:58]** Here you'll find clear categorization, real practical insights, and a fresh perspective on what's possible.

**[00:35:05]** Understandable, critical, and always with a wink.

**[00:35:08]** HDI to ponder, to chuckle about, and above all, to discuss.
