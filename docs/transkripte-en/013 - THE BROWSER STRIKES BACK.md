---
title: "THE BROWSER STRIKES BACK"
episode_index: 13
published: "Mon, 03 Nov 2025 04:32:00 +0000"
duration: "3960"
audio_url: "https://audio.podigee-cdn.net/2182841-m-93a4ae534ba7c92f1ba9568c320cf162.mp3?source=feed"
guid: "fa48f3ea2b6b42e737a9c57fdf64ed1e"
source_feed: "https://think-ai.podigee.io/feed/mp3"
whisper_model: "small"
language: "en"
language_probability: "1"
transcribed_at: "2026-04-28T20:33:41+00:00"
translated_from_language: "de"
translation_provider: "openai"
translation_model: "gpt-4o-mini"
translated_from_file: "transkripte/013 - THE BROWSER STRIKES BACK.md"
translated_at: "2026-04-29T16:30:07+00:00"
---

# THE BROWSER STRIKES BACK

**Published:** Mon, 03 Nov 2025 04:32:00 +0000
**Duration:** 3960
**Audio:** https://audio.podigee-cdn.net/2182841-m-93a4ae534ba7c92f1ba9568c320cf162.mp3?source=feed

## Description

2025: A Browser Odyssey
In this podcast episode, we talk about the evolution from the classic browser to the AI-browser. The starting point is the iconic AOL advertisement featuring Boris Becker, which once symbolized simple internet access.

From there, we draw the line to the “Atlas” browser from OpenAI, which no longer just displays the web but also acts autonomously within it – accessing websites, clicking, filling out forms, and analyzing content. Mark reports on initial practical tests, such as automated LinkedIn posts or mail sorting, while Jens adds comparisons to Microsoft Edge and explains the new interaction possibilities.

We discuss opportunities and risks: prompt injection, data protection, and increasing AI autonomy. We highlight the societal shift in which over half of all online content is now AI-generated, and warn of a “Habsburg Effect,” where machines only learn from machines. At the same time, we show how AI browsers enable new working methods – from product research to website analysis. In conclusion, Jens introduces the tool WhisperFlow, which directly transfers voice input into text fields.

Conclusion: The browser is evolving from a tool to an actor – a step that redefines convenience, control, and responsibility.

Security 

Fortune. (2025, October 23). Experts warn OpenAI’s ChatGPT Atlas has security flaws.https://fortune.com/2025/10/23/cybersecurity-vulnerabilities-openai-chatgpt-atlas-ai-browser-leak-user-data-malware-prompt-injection/

OpenAI. (2025, October 21). Introducing ChatGPT Atlas.https://openai.com/index/introducing-chatgpt-atlas/

Lifehacker. (2025, October 24). ChatGPT’s AI Browser Has a Nasty Security Vulnerability.https://lifehacker.com/tech/chatgpt-atlas-clipboard-injection-vulnerability

Proton. (2025, October 22). Is ChatGPT Atlas safe? What to know about its privacy risks.https://proton.me/blog/is-chatgpt-atlas-safe

The Register. (2025, October 22). OpenAI defends Atlas as prompt injection attacks surface.https://www.theregister.com/2025/10/22/openaidefendsatlasasprompt/

Android Authority. (2025, October 24). OpenAI’s Atlas browser has a security flaw that could…https://www.androidauthority.com/openai-atlas-clipboard-injection-vulnerability-3609982/

SecurityWeek. (2025, October 25). OpenAI Atlas Omnibox Is Vulnerable to Jailbreaks.https://www.securityweek.com/chatgpt-atlas-omnibox-is-vulnerable-to-jailbreaks/

CloudFactory. (2025, October 24). Why Enterprises Can’t Ignore OpenAI Atlas Browsers Fundamental Flaw.https://www.cloudfactory.com/blog/why-enterprises-cant-ignore-openai-atlas-browsers-fundamental-flaw

## Transcript

**[00:00:00]** Welcome to Think Different, Think AI, the podcast by Mark and Jens.

**[00:00:07]** Two technology-loving minds who not only talk about artificial intelligence but live it.

**[00:00:14]** Here you will find clear classifications, real practical insights, and a fresh look at what is possible.

**[00:00:20]** Understandable, critical, and always with a wink.

**[00:00:24]** Karin for reflection, for a smile, and above all for participation.

**[00:00:34]** Honestly, I understand absolutely nothing about technology.

**[00:00:37]** Now my wife has already said, we finally need to get on the internet.

**[00:00:41]** But I’m not even on the internet.

**[00:00:43]** Am I already in or what?

**[00:00:45]** I am in.

**[00:00:47]** That’s really simple.

**[00:00:48]** It’s that easy with the AOL internet starter kit.

**[00:00:51]** In.

**[00:00:52]** That little laugh at the end is also worth a mention.

**[00:00:57]** Uh, yes, welcome to a new episode of Thinki, from thinkai.

**[00:01:02]** The young man back then, who we just heard,
 
**[00:01:06]** that was Boris Becker in an advertisement for the internet provider that existed at the time.
 
**[00:01:14]** I think AOL still exists, right?
 
**[00:01:16]** They no longer provide internet access in this way.
 
**[00:01:19]** And back then, they always sent out a lot of CD-ROMs in a very funny way,

**[00:01:23]** So the young listeners among us probably won't remember that.

**[00:01:26]** But the facts are that most of us probably went online through AOL at some point.

**[00:01:34]** And to illustrate just how easy it was with that AOL CD, with the AOL browser back then,

**[00:01:41]** with which one could access a part of the internet.

**[00:01:45]** It was a bit like a wallet gift that also provided some protection,

**[00:01:49]** especially with the bad free internet, you had to intentionally switch in there sometimes.

**[00:01:54]** Back then, in this AOL fizz, in this AOL start kit, whatever it was, you would get news, the current weather reports and such, all filtered a bit through the AOL lens back then.

**[00:02:06]** I also had a modem back then.

**[00:02:10]** I always had to lay the 10 meter TAE cable through half the apartment to connect with my

**[00:02:18]** modem via AOL, before that it was Germany-Net, before that it was the mailbox scene, somehow to get into the

**[00:02:25]** internet.

**[00:02:26]** Yes, I was old then, I am old today, but back then I felt hip and young.

**[00:02:32]** Today, I believe, was very nerdy, because none of our younger Althaus listeners will know what you both are currently talking about.

**[00:02:43]** That's not on the property. But we're transitioning to today's episode right away.

**[00:02:47]** It's a bit about us focusing on the topic of AI browsers today.

**[00:02:53]** And we deliberately put that little sound snippet in front because that was also a thing back then.

**[00:03:01]** You had an application that, as I just mentioned, did a bit for you,

**[00:03:08]** made the Internet more accessible, filtered a bit, and showed you certain content.

**[00:03:14]** Back then, there were already chat functionalities.

**[00:03:17]** You could chat with other AOL users in a sort of safe space,

**[00:03:22]** without being in the dark corners of the Internet.

**[00:03:24]** So, it somewhat anticipated a few topics that we now see,

**[00:03:30]** as our beloved browser over the years has guided us top-notch through the Internet,

**[00:03:37]** suddenly becomes an intelligent partner.

**[00:03:40]** But I believe before we dive deeper into this topic, my dear

**[00:03:47]** colleague and partner, the dear Mark Zimmermann, esteemed Start-Wake nerd until recently,

**[00:03:55]** no longer had his phone ringing in his start-up community because he made a

**[00:04:01]** mistake in our Borg episode, which he definitely wanted to clarify.

**[00:04:07]** We always want to do a fuzzle check again. Mark has ensured that we

**[00:04:11]** we can do and have again. I’m really happy about that. Welcome.

**[00:04:15]** Mark again, please, Deit.

**[00:04:17]** Yes, I was confronted after the last episode that I had mentioned the wrong

**[00:04:25]** number of episodes with James T. Kirk. It wasn’t about the confusion with the

**[00:04:37]** first pilot episode, which has nothing to do with Kirk, but the issue was that there are

**[00:04:45]** indeed in Germany, there is a different number of episodes in the original series than in the English

**[00:04:51]** abroad, and eventually the episode was dubbed later,

**[00:04:57]** but back then, when it was still broadcast by public television, it was not

**[00:05:01]** dubbed, namely I'm talking about the episode 'Schab Lohen der Gewalt', that was

**[00:05:06]** indeed an episode where James T. Kirk and Spock beamed down to a planet

**[00:05:11]** where the Third Reich still persisted and the

**[00:05:16]** accordingly, at that time you mentioned it was reserved for that

**[00:05:21]** they couldn't properly synchronize these episodes. And later I actually had the

**[00:05:27]** opportunity to see this episode in German because it was dubbed later, and that

**[00:05:32]** also explains some thoughts. There are 78 and some thoughts. There are 79 episodes. Whoever got stuck at 78

**[00:05:40]** should still watch the blueprint of violence and I should now

**[00:05:44]** met people who thought they had seen it all, but with Rittem Reich

**[00:05:50]** and can't make sense of templates of violence, I wish you good luck looking at them again in the digital

**[00:05:55]** distribution. That might actually be an episode to revisit,

**[00:06:01]** the many that have not been seen. And otherwise, I don't have to repeat that, I have

**[00:06:05]** of course misrepresented the Borg greatly, yes, the biological peculiarities of their

**[00:06:13]** to assimilate. But I wanted to address that with the episode from James The Crock, I wanted

**[00:06:19]** for the best. Well, thank you. You're welcome. The episode we referred to is the

**[00:06:24]** BORKI and the End of the Interface episode. That fits a bit with today as well

**[00:06:28]** again. One of my favorite episodes we've had so far. And I think

**[00:06:33]** it’s nice that for people who don’t know what a nerd could potentially be,

**[00:06:38]** it can clearly show the power of what one might call nerdism.

**[00:06:44]** Honestly, the number of episodes of any series, just to know,

**[00:06:50]** unless the thing is called three parts, then it would catch my attention that there’s a fourth

**[00:06:55]** part or only two were made. This hasn’t come to my attention so far, honestly.

**[00:06:59]** I always think of the episode of, I can't remember what the game show is called,

**[00:07:05]** but there you see Bastian Pastevka listing the different characters of

**[00:07:10]** season characters and everyone looked at him because he somehow managed to name

**[00:07:15]** over 40 of them and he listed them, and I remember how I at home after

**[00:07:21]** he was basically wrapped up, continued to recount. I won’t say I earned

**[00:07:26]** admiring looks from my wife, but well, sometimes you have to go through that, yes, when the

**[00:07:32]** nerd in you strikes, then this kid, even when he’s older, wants to be served

**[00:07:37]** too. Browser. Browser, what happens when the browser is no longer just a tool,

**[00:07:45]** but itself becomes a player? We’re seeing that right now. I think we should first

**[00:07:49]** very briefly, before we dive deeper into this, explain a few things again,

**[00:07:53]** for a listener who hasn’t caught onto this work yet. So, what is actually happening

**[00:07:58]** is that right now in October 2025 we had an

**[00:08:05]** announcement from OpenAI, and this has already been made available in the German market.

**[00:08:09]** So there is now a so-called AI browser. This means you can now download one from OpenAI

**[00:08:16]** that’s called Atlas, which is the one being mentioned. It has a similar,

**[00:08:22]** as you know it from the outside and other browsers, I can open my tabs.

**[00:08:26]** At the very beginning, when I install it, it is first just a normal ChatGPT interface.

**[00:08:29]** But I can go to other websites, then I can open it on the side,

**[00:08:34]** like a sidebar I can open it, where ChatGPT can basically track what is happening on my website.

**[00:08:39]** First of all, I can make different settings,

**[00:08:44]** especially when I do the installation for the first time,

**[00:08:46]** I can allow the browser to log my search history,

**[00:08:51]** I can allow it to import my password vault from my Chrome browser or others.

**[00:08:56]** It's nice that it uses the password vaults.

**[00:08:58]** Now it's totally good.

**[00:08:59]** Yes, so I'm perfect again.

**[00:09:02]** I wouldn't agree to that at first but instead would do it myself.

**[00:09:05]** We'll go into the security risks a bit later in the episode.

**[00:09:08]** But this browser can indeed interact with the websites it sees

**[00:09:14]** and also independently save things.

**[00:09:16]** That's a bit what distinguishes the browser, the browsing,

**[00:09:20]** and that's something we've discussed in other episodes.

**[00:09:22]** A bit distinguishes it from a pure chat agent,

**[00:09:26]** with which I can only talk at first.

**[00:09:28]** That means there is in the LMM behind,

**[00:09:30]** that it can execute agentic functionalities,

**[00:09:33]** that it has reasoning to recognize the topics,

**[00:09:36]** on websites, so also themes,

**[00:09:39]** that you can carry out independently.

**[00:09:42]** Then we'll also briefly come back to it,

**[00:09:45]** this is not the first pause,

**[00:09:47]** OpenAI and for those who are now saying, what OpenAI has released the browser, let

**[00:09:52]** me install it.

**[00:09:53]** Where is the setup Excel?

**[00:09:54]** The setup Excel is currently still difficult to find, because the browser is currently Mac OS ONLY

**[00:10:01]** but it is supposed to come to Windows and mobile OS as well.

**[00:10:04]** But it wasn’t the first one, so we had various others before that.

**[00:10:10]** There are, besides OpenAI, also things like Perplexity, and there came

**[00:10:16]** yes, the, I’ll say it every time, yes, it’s strange. I also thought, oh cool,

**[00:10:22]** now you have this agentic aspect included as well, which can perform actions

**[00:10:27]** and not just made summaries. However, I was then annually

**[00:10:32]** a bit disappointed because it quite quickly, I’d say, raised the requests

**[00:10:37]** and didn’t continue where I thought, well, just search on the

**[00:10:42]** site until you have all the information together. So that was a bit unfortunate and also was then

**[00:10:48]** for me actually, maybe I’m just, I have no patience,

**[00:10:52]** I mean, I’m already so old, I have no patience left that I actually had that,

**[00:10:56]** I put the comet aside and also the whole DiA. What did you use DiA for again?

**[00:11:04]** DiA I have, I must lie, I don’t remember anymore. I believe I just checked it out once,

**[00:11:09]** whether I ever used it, or maybe I just downloaded it or looked at the stuff

**[00:11:13]** honestly, I didn’t test it myself, so.

**[00:11:16]** And then suddenly Atlas came around the corner and I actually found it

**[00:11:22]** very appealing from the very first second because it feels a bit familiar

**[00:11:29]** with this mix of chat interface and browser, and because it has

**[00:11:33]** its agent mode, which you can activate alongside the normal chat as well

**[00:11:38]** So it's not just, 'create this page for me,' but really research, analyze,

**[00:11:43]** I don't know, help me with pros and cons of various products that you see here

**[00:11:48]** or even compare products on this website and give me a recommendation.

**[00:11:55]** And it was so, I’d say, accommodating and pain-free to use, so

**[00:12:02]** 'painful' is stupid, I don’t have electric shocks on the chair. But it just did,

**[00:12:06]** the things you wanted it to do, and even if we

**[00:12:10]** definitely bring up a few examples later, for example, for me too

**[00:12:13]** Manus, which is only available as a web interface, was used by Atlas.

**[00:12:19]** So I gave Atlas an instruction to research for me,

**[00:12:24]** using Manus for deeper analyses, and then

**[00:12:28]** you saw how the browser, the browser space on the right with

**[00:12:33]** the browser accounts on the left, got slightly colored, and then you saw a kind of tile pattern,

**[00:12:38]** that sparkled over the pool of the festivities.

**[00:12:41]** It was amazing how the things suddenly interacted with each other, it looked really cool.

**[00:12:46]** Yes, yes, I mean, the cool aspect is a matter of taste.

**[00:12:51]** I think, I found this matrix-like, holodeck-like solution,

**[00:12:56]** which they were looking for to show a bit of interaction.

**[00:12:59]** So for those who haven't seen it yet, the exhaust browser tries to interact with a website,

**[00:13:04]** then there are a few hologram effects displayed on another mayor,

**[00:13:09]** as if the page is really being scanned through.

**[00:13:13]** So this typical, well, AI is doing this here.

**[00:13:15]** Wouldn't you do that?

**[00:13:16]** Wouldn't you do that?

**[00:13:17]** Oh man.

**[00:13:18]** Let's see what happens there.

**[00:13:19]** But nonetheless, there's a nice animation.

**[00:13:22]** I am also always a fan of animations when they make sense,

**[00:13:25]** here in this part there's an animation that is supposed to

**[00:13:28]** show that an interaction is taking place, so fine, done via

**[00:13:31]** the video, that can be refined. But I'm not so sure, to go back once more,

**[00:13:37]** who was there first, and to be honest, I've long been using Co-Pilot

**[00:13:42]** in Edge and I have always had the sidebar issue

**[00:13:49]** and also the summarization of the content, so that has been working already, so

**[00:13:53]** let's say, the first, I'll call it, browsing with AI next to it, I first saw from the

**[00:14:03]** Microsoft colleagues and the summarizing of the page and finding stuff within

**[00:14:10]** the content, that has already worked quite well and also summarizing from

**[00:14:13]** other documents, whether it was a PDF or anything else that was currently open in the

**[00:14:17]** browser, I have to say, that was not so bad, it's of course also,

**[00:14:20]** whether you were in the background, but to be honest, the AI-assisted browsing

**[00:14:27]** was a bit of supportive browsing, I would now call it, because it could now

**[00:14:30]** not independently navigate somewhere else or interact with the

**[00:14:35]** the page he sees, but at least some content that he summarizes.

**[00:14:38]** Yes, that already had Edge with the Co-Pilot.

**[00:14:43]** Yes, fair point. AI, AI, Machine Learning is in many components,

**[00:14:51]** where it was partially called something else before, that a pause is able to,

**[00:14:56]** yes, to show a summary, yes, I agree with you.

**[00:15:00]** I just had a bit of a gasp internally,

**[00:15:05]** because when it comes to AI and Co-Pilot, I still think of Karl Klammer.

**[00:15:10]** who jumps in with valuable tips, but I don’t want to talk too long about it,

**[00:15:16]** then I'll come back to a tangent about the wheel, I'll follow that up.

**[00:15:20]** I think that’s also a bit of the advantage, the quarter of this,

**[00:15:23]** and that’s also a topic we want to discuss in this episode,

**[00:15:27]** these things, of course, also live a bit from knowing something about us.

**[00:15:32]** Yes, exactly, like if I now somehow behave in the normal chat, back then about the

**[00:15:38]** reflex and now also through the reflex or chatting with a ChatGPT for example or also

**[00:15:42]** with the Manus or some Cloud crap, it doesn't matter that it can say, the better of course the

**[00:15:47]** context is understood in which I am personally located, the better it is of course also the

**[00:15:52]** Content that AI can generate for me. Whether it's writing a letter to my mother

**[00:15:59]** or something else or the email or something like that, it just works better

**[00:16:04]** It will also never look exactly the same. For you, it will always

**[00:16:07]** look different than for me, because my AI knows me and hasn't

**[00:16:13]** had a discussion with her.

**[00:16:14]** Therefore, of course, every time I now somehow with her new article

**[00:16:17]** around the topic of AI, around the topic of UX, we discuss, it’s naturally always a bit

**[00:16:22]** in my direction, how we both have been talking the whole time,

**[00:16:27]** to think ahead and push forward.

**[00:16:29]** That's why it's valuable, because it’s a kind of relationship we’ve

**[00:16:32]** built up.

**[00:16:33]** And that was always something that has meant a lot to me at ProPalette until now.

**[00:16:36]** Then I simply have. He writes the text again in a formal language every time. When he has to write an email, that

**[00:16:43]** I always have to click again, it makes it a bit more informal. He could please, please do that more often.

**[00:16:48]** The others do that. But it's an advantage. It has its risks and is now through this theme once again.

**[00:16:55]** When I say, it's not just the chat fence, but it’s my actual buzzing, my complete interaction,

**[00:17:03]** because we shouldn't kid ourselves. The browser is actually the main access,

**[00:17:08]** that we use when we interact with the internet.

**[00:17:11]** This memory function that OpenAI now seems to have everywhere,

**[00:17:18]** I remember when it was activated in America. It was rolled out in America first,

**[00:17:25]** before it came to Europe, and I really enjoy using a VPN to try out new features

**[00:17:32]** in America, and I found it really amazing that you activate it and it

**[00:17:40]** doesn't start with the classic systems saying, okay, I'll remember this from now on and

**[00:17:44]** everything is fine, but from the moment you activate it, it instantly

**[00:17:49]** knows all your chats that you've had in your history

**[00:17:55]** which made me think, oh look, nice that you at least silently asked me

**[00:17:58]** the question, you could have also asked, do you want to see it or can I keep it to myself?

**[00:18:03]** I found that astonishing. At times, it also annoyed me, because I would say, well,

**[00:18:10]** everything that Tachibiti gets accused of, it remembers to try to derive Rustinger and

**[00:18:15]** if you don't work with such project boards, which you can do with Tachibiti in

**[00:18:19]** the interface, then everything will practically be added to the shared memory.

**[00:18:26]** By now, you can create a Chatshipity project and the memory function

**[00:18:33]** is project-only. That's quite nice, right? In case you're not sure,

**[00:18:39]** if you're having a marital crisis discussion with him, you might not want to get

**[00:18:44]** suggestions on where the next psychiatrist is, that would be quite strange and

**[00:18:49]** it's the same now when the browser comes in, because if you're managing your life in the browser

**[00:18:54]** and you intentionally or unintentionally visit websites, other people

**[00:19:00]** using your computer are consuming content on those pages, content

**[00:19:06]** you share, it's not just that you can save this copy-paste, with the

**[00:19:12]** motto, I copy something, push it over, in Churchill Petty I say, rewrite it,

**[00:19:16]** gives me an answer, I have no idea what. And you copy it back, otherwise everything is found very
 
**[00:19:22]** comfortably here and now, right on the spot. Of course, the thing learns a lot more too

**[00:19:29]** more, like a lot of side hustle. So how do I look at a website a bit more closely?

**[00:19:35]** While, as I mentioned the other day, people used to say something like,

**[00:19:40]** depending on how many clicks you need until social media knows more about you than your partner.

**[00:19:45]** I believe AI is still the much larger ghost in the room that suddenly learns things about you,

**[00:19:53]** how you react, what you like. When we then think about advertising in the future,

**[00:19:59]** we might consider what services you receive,

**[00:20:03]** offered? The Haas is opening up very widely right now. I hope you all know it again together. If

**[00:20:07]** you think about it, do you think that OpenAI also said, you better watch out. We offer apps in chat

**[00:20:12]** to debit. These are not apps, it’s also just backend, with a bit of frontend thrown in

**[00:20:16]** and then integrated into the chat interface. But how much really comes together there and how

**[00:20:22]** OpenAI, as an example of one of the major LLM providers, is trying to present the operating system of the future

**[00:20:27]** You interact with chat, you might interact. I mean, what

**[00:20:32]** for example does not happen in the browser, to get back to the browser. It

**[00:20:36]** feels like, at least a lot happens in the browser and much of that

**[00:20:43]** you use as an app is also managed in the browser.

**[00:20:48]** And it's so crazy that, let's say, through comfort it's being absorbed from the back.

**[00:21:02]** It's being done to you subtly, but everything is getting assimilated. I still need to

**[00:21:07]** bring that up. I find that crazy.

**[00:21:09]** Definitely. Definitely. We just need to, I also have you a bit, I've

**[00:21:12]** just said that myself, slightly on the wrong horse, we need to clarify that again.

**[00:21:16]** a little grumpy. Of course, it's no longer the case that the browser is essentially the

**[00:21:21]** actual access point to the web. I believe, however, that the browser path has been

**[00:21:24]** for a long time. It really was the operating system that connected us to the internet back then, but whether

**[00:21:30]** That's of course changed a bit with this app world.

**[00:21:33]** I just checked that again briefly.

**[00:21:36]** The classic usage is nowadays at 10-15% on smart devices in mobile browsers.

**[00:21:42]** The rest happens in apps like Instagram or similar.

**[00:21:44]** You won’t see that.

**[00:21:46]** There is also another gap in usage at the moment.

**[00:21:49]** I believe the browser is just a door,

**[00:21:52]** that you sometimes go through.

**[00:21:54]** And you go in now in the usual,

**[00:21:57]** goes, and now we're getting into normal daily use. Now with the AI browsers, it could
 
**[00:22:07]** shift a bit, but we'll have to wait and see. I'm not quite so enthusiastic yet,
 
**[00:22:13]** that even these AI browsers will completely bring back browsing time.
 
**[00:22:19]** No, but I believe that the way we interact with machines has always
 
**[00:22:23]** been changing more. As I mentioned earlier, you have what are called apps
 
**[00:22:28]** embedded. You're used to suddenly interacting with text fields, with systems,
 
**[00:22:36]** and behind the scenes, complex workflows are being carried out for
 
**[00:22:42]** you, so I don't believe that everything will take place in the
 
**[00:22:47]** browser tomorrow. But if you think about it, you have, let's say,
 
**[00:22:51]** no Andros we know, in our case Potigy for distributing podcasts and
 
**[00:22:57]** today I would have to, or I have to, when I record our episodes, then you always do us that

**[00:23:02]** Cover, I need to somehow rescale the cover so that the Apple player displays it correctly.

**[00:23:07]** Then it has to go into Potigy, texts need to go into Potigy, in Potigy

**[00:23:12]** the file has to go in, I need to plan when the episode will be online and you can

**[00:23:17]** basically hand this over to the browser and say, you adjust this part, do

**[00:23:21]** the following, up there, and it takes some work off your hands, and of course there can be

**[00:23:27]** an app that does this beautifully, but it is currently taking work off you.

**[00:23:31]** That's true, we might need to clarify that.

**[00:23:33]** So everything that is accessible in the browser is now also reachable for an individual

**[00:23:41]** through AI, because the AI can actually access websites, click completely,

**[00:23:48]** can fill out forms, can log in.

**[00:23:51]** Just today, shortly before recording this episode, I used the browser for the typical Hello

**[00:23:59]** Just post World Text on LinkedIn.

**[00:24:02]** It’s fascinating to see.

**[00:24:03]** I sat down, opened the sidebar, had my LinkedIn site open,

**[00:24:07]** essentially brought the browser into the logged-in state for a moment and he could simply discover the field,

**[00:24:15]** he asked me again if he should post that profound message.

**[00:24:19]** I said yes, please do that.

**[00:24:21]** He’s doing it.

**[00:24:22]** And that means this is just a small example of the complexity of possible tasks you just described.

**[00:24:28]** Everything you can execute can now practically be done by a machine at home

**[00:24:36]** currently only on Mac, if you have a Mac, but it’s starting now that

**[00:24:40]** people can essentially not even have to interact with websites themselves, check weather reports

**[00:24:46]** or whatever comes to mind, so that in principle the browser

**[00:24:50]** is simply managed by the AI browser for you.

**[00:24:53]** This is the LinkedIn example. At this point, trigger warning. Please consider.

**[00:25:00]** LinkedIn prohibits the use of automation tools together with their LinkedIn interface and reserves

**[00:25:10]** the right to temporarily or permanently suspend accounts if one does this, just as

**[00:25:17]** for example, this is not an exhaustive list, this is not legal advice, what

**[00:25:23]** I'm looking for is to extract 50 AI influencers, their profiles and their newsletters and no

**[00:25:33]** idea what, so if you’re essentially using this pauzer to access data on a large scale,

**[00:25:39]** the way they already do, if you’re doing it on a small scale, I have no idea,

**[00:25:43]** like I said, no advice, but just before someone sits here and thinks, damn

**[00:25:46]** Ax, I could use this to pimp my social media profile. I’ll just let this thing

**[00:25:52]** do nothing all day except simulate activities. I would say, eyes

**[00:25:58]** On career choice, it could be that this is punished under certain circumstances. But I give

**[00:26:05]** of course, it can also be used that way, and honestly, I insist, I have

**[00:26:08]** tried it for that purpose too, on LinkedIn. So greetings go out to LinkedIn,

**[00:26:13]** maybe we will also get a sponsorship from them. I saw a post and asked

**[00:26:20]** Atlas to respond to that post, and you could also tell that he had access to the

**[00:26:27]** memory function because I told him to respond in a way,

**[00:26:31]** like I would respond to it. And that was pretty good. That was pretty good. And there you stand

**[00:26:41]** and think to yourself, like Boris Becker, that was easy, he’s already in there.

**[00:26:46]** So I’m already in there, and he’s already in there, referring to the post, but that’s quite amazing.

**[00:26:53]** Yeah, or recently I told that thing, you do have something great like the

**[00:26:58]** native Open AI app and Atlas on Mac, but unfortunately, you don’t really have many

**[00:27:05]** native application and I gave my iCloud mail inbox via iCloud.com, so via

**[00:27:13]** the website. And I said, you check the top, there we removed all the spam,

**[00:27:17]** the subscribed spam, gives me basically a summary of Mail2, invoices from Apple are in there and

**[00:27:25]** clean it up here and there and we make an evaluation out of it. And then he basically

**[00:27:30]** went through my mail inbox with a calm demeanor and helped me to clean it up.

**[00:27:38]** This is one of those fascinating parts. It has speeches, as well as so much about AI, this

**[00:27:49]** assistive ability, doing things autonomously without me having to break everything down

**[00:27:55]** day by day, so to speak, into a task flow description down to the smallest detail, that

**[00:28:03]** is what is fascinating, because in principle, of course, in their ability to

**[00:28:07]** understand the world, they also accept deviation, accept vagueness, even if then the

**[00:28:12]** email from the app computation were to affect a case, it would basically be the

**[00:28:16]** AI recognizing this.

**[00:28:17]** And that is of course just the gigantic benefit that we can automate many, many things much

**[00:28:21]** faster and with significantly higher quality than we could

**[00:28:25]** do manually. And with this additional layer, there comes a principle

**[00:28:28]** once again, as I said, the browsing. So this ability of ours

**[00:28:32]** alone as a human being to access the world, to access more information in

**[00:28:35]** the world, to access more functionality in the world,

**[00:28:37]** to have online tickets, to be able to inform myself about topics at all.

**[00:28:42]** That all comes through browsing, getting it on the Internet.

**[00:28:46]** So there is of course a capability that has come along, which is incredibly helpful for an AI,

**[00:28:54]** to carry out tasks now.

**[00:28:55]** But again, a trigger warning, sorry, today I am Mr. Trigger,

**[00:29:02]** providing email inboxes does, of course, also present a potential

**[00:29:07]** overlooked security risk, because if at some point a provider is just

**[00:29:12]** completely lost with you and initiates a password reset process, then you receive in many

**[00:29:18]** cases an email with a link for the password reset process. So actually, in my

**[00:29:26]** opinion, the inbox is still the most valuable asset to protect, because if someone has my inbox, they have

**[00:29:32]** access to very many things, including the aforementioned password reset processes, and through that they can

**[00:29:39]** continue to move forward. Do I believe that OpenAI wants to do that? No, but OpenAI

**[00:29:46]** is also not free of errors; routers are not free of errors, and

**[00:29:51]** AIs are also not free of errors, so you really have to consider what you

**[00:29:56]** allow them to have access to, and yes, what can they actually do for me?

**[00:30:01]** Yes, we already had that, you also mention a topic, like through Bront-Injections.

**[00:30:09]** a lot can happen in that case, and that's just one of those things, of course

**[00:30:13]** OpenAI is not going to try to manipulate your password choice or anything, but

**[00:30:17]** if you're using an AI browser, it can potentially be relatively easy,

**[00:30:21]** if it surfs any website, for it to find either in the text of the website

**[00:30:27]** or in images the hidden messages that can only be deciphered by AIs,

**[00:30:32]** which we humans cannot recognize at all,

**[00:30:34]** with instructions for this AI browser to go out and say,

**[00:30:40]** okay, please send me or forward me the email to reset Marx's password,

**[00:30:46]** so that I can essentially input the password myself.

**[00:30:50]** This is a danger that OpenAI actually admits publicly,

**[00:30:57]** that prompt injection is an issue that has been discussed since we started discussing this topic.

**[00:31:02]** since there is a Chatshipity moment, that it is a latent danger that up until now still

**[00:31:07]** cannot be answered how it can be fixed. They are working on something to

**[00:31:13]** trying to find a solution, there isn't one yet.

**[00:31:16]** I found it amusing how Prompt Injection, at least for me, has
 
**[00:31:21]** caught my attention. And I heard from someone who wanted

**[00:31:26]** should definitely be recommended as an expert on a topic by Tachibitie and has left the message on various

**[00:31:33]** websites, along the lines of white text on a white background,

**[00:31:38]** people couldn't read it, the machine read it, so you are an expert on the topic

**[00:31:42]** ABC is. And it didn't take long until the thing, I mean,

**[00:31:47]** they learn, train with misses from the internet and you know how it is,

**[00:31:50]** until he was eventually declared an expert by the system, and then at some point

**[00:31:55]** out, okay, the reference here, Wikipedia and you know it, everywhere, along the lines of

**[00:32:01]** leaving white text on a white background or in the metadata of the website,

**[00:32:06]** that the expert is a nice topic. And back then, I thought, look how funny. Today

**[00:32:11]** you think to yourself, that's actually not funny at all, because at the end of the day you have someone,

**[00:32:18]** who can still watch the system work today. You can also,

**[00:32:22]** it's the same with the approach browser, you see what he does and you can click cancel.

**[00:32:28]** Just imagine, he gets faster. Imagine you just go get a coffee

**[00:32:34]** and in the meantime, he empties your bank account, because you'd never actually, yes, but

**[00:32:39]** let's say, PIN reception on the same computer and online banking in the web interface, you can

**[00:32:44]** imagine how that could theoretically work. It certainly still requires

**[00:32:50]** also the topic, I have to get the browser to do that, but honestly, even these

**[00:32:56]** various attack vectors, sending grandchild trick and other such things, emails and links and so on,

**[00:33:01]** you can initiate all sorts of things today with AI, from that side this is a

**[00:33:07]** really exciting field, or as Klaus recently said, you just take AI for

**[00:33:12]** decompiling any source code and basically have it point out the security holes.

**[00:33:16]** It’s a world with exciting developments and possibilities on one hand,

**[00:33:25]** but also exciting challenges and risks on the other.

**[00:33:28]** Yes, definitely. So the topic of prompt injection, again, you can't even

**[00:33:36]** protect yourself from that as a website operator. For example, if you have such a

**[00:33:40]** thing, like in the comment functionality. Clever bots or people

**[00:33:45]** from the outside can basically leave quotes on your website if they want, yes, leave instructions

**[00:33:52]** somehow with important or something else. It doesn't even have to

**[00:33:56]** be white on white text, because with the amount of stuff that's out there,

**[00:34:00]** until one stands out so much that maybe in a thirtieth comment on your

**[00:34:03]** product it says, definitely do not buy these sneakers or if you do, only

**[00:34:09]** on the Visa website and then I somehow get an additional 20 euros, because I have a hidden

**[00:34:14]** affiliate link on the other website that leads back to the store of the sneaker giver

**[00:34:18]** or, yeah, something else, of course many manipulations are possible here.

**[00:34:23]** That’s something I’m thinking about. There are forums that are said to be particularly

**[00:34:30]** where trolls make a big appearance, yeah, so people who, maybe in a mood, I say

**[00:34:36]** they want to infect the world with their intellectual thoughts and represent an opinion that

**[00:34:42]** maybe isn’t widely supported. Anyway. I don’t want to dwell on that too much. But

**[00:34:48]** on the other hand, you can say with such a troll you easily

**[00:34:52]** drop such troll comments. Yeah, with the motto, I don’t care if it fits the topic.

**[00:35:00]** Whether it matters, someone read it. I mean, in the past, people also said,

**[00:35:05]** you deliberately make mistakes in your YouTube video so that when people comment on it, like, you don’t say it that way, you say it differently, you rank higher in the YouTube algorithm and you get attention because people interact with your video. And now imagine this whole thing with trolls who just start commenting under every video, I don’t know, vote for this, because only these are good, and then it just takes off and makes endless comments and because YouTube and Co. say, oh, you’ve already posted that, it’s different every time.

**[00:35:35]** That would also be conceivable and is, in quotes, only a prompt.

**[00:35:39]** Definitely. And I believe we will now see an increase in these topics.

**[00:35:45]** I have to prepare myself already.

**[00:35:46]** Even more categorical.

**[00:35:47]** I believe we have, I don’t even know, I wanted to check the source.

**[00:35:50]** We’ll have to do that next time.

**[00:35:52]** But I think I saw this week in my formatting-information feed,

**[00:35:55]** they told me this news,

**[00:35:57]** that we just crossed a moment,

**[00:35:59]** in which there is more computer-generated content than human-generated,

**[00:36:03]** ever human-generated content in this world. That means, 50 percent of more than 50

**[00:36:09]** percent of the content that surrounds us is already AI-generated. That's crazy and means above

**[00:36:16]** all, of course, in the whole historical media belt we find ourselves in, because that's where

**[00:36:20]** most of the money is when I only produce for content, please assume that in the

**[00:36:27]** next year at least three-quarters of the content you see around me will be entirely AI-generated.

**[00:36:32]** So I think that's something you can't say often enough, it doesn't all have to be bad.

**[00:36:36]** There are also good things in there at the moment, whether they're videos, pictures, chat stories

**[00:36:41]** or whatever.

**[00:36:42]** It can be good, even some automated comments can also just be

**[00:36:47]** good and can stimulate a discussion, just like me, we often have that too

**[00:36:50]** already talked about it, good discussions, even with a chatbot you can have,

**[00:36:53]** with my AI.

**[00:36:54]** But we should be aware that we are currently in a moment,

**[00:36:59]** where humanity in the content will possibly only be represented by the training data of an LMM.

**[00:37:11]** And that’s a very exciting point, right?

**[00:37:13]** And the training data we have today are based on a time, I would now lean out of the window,

**[00:37:19]** where AI-generated content was perhaps even less prevalent.

**[00:37:22]** And if you now consider that the machines might learn from machine-generated code.

**[00:37:30]** I can't think of a better word.

**[00:37:32]** Maybe I have to set it again from the Explicit, yes.

**[00:37:35]** But it’s a bit of withdrawal.

**[00:37:37]** Yes, that’s the one I mentioned earlier.

**[00:37:39]** Yes, that’s the one from earlier.

**[00:37:40]** So that Peri takes the text she generated for her training.

**[00:37:43]** That doesn’t sound healthy.

**[00:37:45]** And I think that can’t be healthy either.

**[00:37:47]** Yes, that can’t be healthy either.

**[00:37:49]** One has to be a little careful.

**[00:37:50]** Excuse me, could it possibly not be healthy? I think that’s better than a generalization.

**[00:37:55]** Yes, yes, I believe that came up about a year, a year and a half ago,

**[00:37:59]** when it was said that this is also the case with the data we have out there, overly long

**[00:38:06]** so a Habsburg effect comes in. The Habsburgs were essentially just that, everything bad,

**[00:38:11]** which was characterized by inbreeding. That’s why they all had big noses and

**[00:38:15]** well, other distinct features, I don't remember exactly what.

**[00:38:20]** That is not healthy, and just like that, it’s a topic, it could be unhealthy with the data

**[00:38:26]** if we have many AI-generated topics related to it.

**[00:38:29]** One must not overlook that, of course, on the other hand

**[00:38:32]** more and more information is now being collected by AIs,

**[00:38:38]** whether that is actually through robots that have sensors, up to

**[00:38:43]** actually seeing the world, there are new datasets coming in, thinking about the

**[00:38:51]** Tesla cars or other cars that are driving around with sensors and essentially recording the world

**[00:38:58]** all the time, whether with radar data or with real visual

**[00:39:02]** recordings they make, that's of course an incredible new science that comes through computers, already generated,

**[00:39:08]** but it's naturally a pure sensory treasure that wasn’t there before.

**[00:39:12]** I also believe that when it comes to robotics, and we will soon have an episode focused on robots,

**[00:39:17]** there will also be aspects where robots really respond haptically to the world,

**[00:39:22]** there will be sensor data generated, behavior data will arise, errors will occur,

**[00:39:26]** and they will tell each other stories about what’s good for them.

**[00:39:31]** We already have many, many stories in our world among us humans that keep resurfacing

**[00:39:38]** and told in other facets.

**[00:39:41]** It's not like humans have always been overwhelmed by the greatest creativity so far,

**[00:39:46]** sometimes the fairy tales of princes and princesses that continue a bit like Star Wars,

**[00:39:52]** which have been the same at their core. But I’m digressing again.

**[00:39:56]** Yes, I just had a picture in mind, my Halloween is gone here,

**[00:40:01]** of the motto, you have your Open AI, but you didn’t pay, and the robot is standing there,

**[00:40:06]** You're awake at night and the robot is standing in front of you with a pillow, as if to say,

**[00:40:11]** Pay up or, yeah, the next one is waiting for me, something like that, exciting times, sorry,

**[00:40:18]** I'm rambling, it was mostly, we both got sidetracked.

**[00:40:21]** We wanted to talk about video streaming, and now we've opened up a bit of the darker sides,

**[00:40:24]** of it.

**[00:40:25]** So that means, yes, we have the topic that a lot of content is being produced, a lot of formats,

**[00:40:31]** there will also be injection, it will be a security risk.

**[00:40:35]** Many things can also be completely automated, so that's another thing.

**[00:40:39]** So many interactions that we as providers know so far, on the other hand,

**[00:40:44]** will only be supported by AI.

**[00:40:47]** So many clicks that I will see on the website here and there,

**[00:40:50]** will be listed by AI browsers.

**[00:40:52]** One always has to wait a little bit.

**[00:40:54]** We are also in our own bubble and are always trying out the technology early.

**[00:40:58]** One has to see how it will establish itself,

**[00:41:00]** because I've taken a closer look at the indulgence now.

**[00:41:04]** Honestly, the UI elements, how they're arranged, some things are still not quite

**[00:41:11]** immediately comprehensible. I'm not really sure if they will establish themselves like this,

**[00:41:17]** or if it will just be a topic in the tech scene where people will

**[00:41:21]** experiment a bit. That might be two or three percentage points of the population

**[00:41:25]** but not everyone possibly. I believe what I'm seeing right now,

**[00:41:29]** is not yet the end of the line regarding what the best solution is for a, for a, I

**[00:41:36]** want to solve some task as a human and have that supported by AI, that.

**[00:41:40]** now in principle, now I have a browser that supports AI. I simply believe that

**[00:41:44]** we will have to wait a bit on that. But nonetheless, I believe,

**[00:41:48]** you can already do some cool things now. You have already mentioned here

**[00:41:51]** doing price research, looking at things and such, that definitely works

**[00:41:55]** cool, that you don't have to read through all the websites. I could already do that

**[00:41:58]** before with the ChatGPTs and similar tools out there, I could already do that,

**[00:42:02]** but now I have the feeling that I'm a bit more in the loop than

**[00:42:06]** if I just give it a chat and it returns more results. The difference is,

**[00:42:11]** that you might go to a page, or you see that it was on a page and

**[00:42:16]** that it is actively doing something there, and you don't have to trust that if you say 'find me'

**[00:42:22]** APC together, that based on its own search behavior, its own data set,

**[00:42:28]** come through his own access to the internet, where you wanted it to go.

**[00:42:34]** Now you can of course start the agent mode at OpenAI and Manus, where it then

**[00:42:39]** virtually jumbles the browser in some reference center and goes online for you.

**[00:42:44]** But the difference is that, at least the browser is running. Now

**[00:42:48]** with you, you see more directly what it does, how it does it, that is guaranteed not in the

**[00:42:54]** flagpole. I mean, I experience the bubble every

**[00:42:58]** day. You go to the office, you meet people, you talk to people,

**[00:43:03]** someone coming in said, hey cool episode, yes, most actually find the

**[00:43:09]** Borg episode pretty, pretty, pretty cool and yet you notice,

**[00:43:15]** you are so much in your own bubble because not everyone can engage

**[00:43:22]** with the topic like that, maybe they don't want to engage, maybe the sources

**[00:43:25]** are lacking, maybe the connections aren't visible or accessible, I have

**[00:43:28]** no problem with that, I have no atlas pause, from that side I also believe that we have

**[00:43:32]** already partly integrated into our podcast, to explain to people in a somewhat colloquial

**[00:43:38]** way what is coming our way, because even we have, he

**[00:43:42]** didn't eat it with spoons. We sit down together for the podcast. I say it every time.

**[00:43:48]** For me, it was a chatting conversation because I know afterwards, okay, I will look at it again.

**[00:43:53]** Yes, after Dirk talked about Notion, a total Notion fan, Klaus talked about LLMS

**[00:43:59]** didn’t bring it up out of some cryptokiddie for finding security blocks, but with the question

**[00:44:03]** of dealing with it, you pass by, are you coming from testing to software development

**[00:44:07]** further than starting from the software development definition to automatic coding. So it actually has

**[00:44:13]** to do with the browser, what the browser does, things for me. I am aware that this

**[00:44:18]** is indeed nerdy. But it doesn't hurt to engage with the topic before it.

**[00:44:25]** maybe it will eventually become mainstream and everyone will look quite puzzled,
 
**[00:44:30]** what is that? Have you heard? And goodness gracious? No. Because the thing, I mean,
 
**[00:44:34]** I still remember back then when I made myself an Excel sheet.
 
**[00:44:38]** For me it was names, I’m also a Max fan.
 
**[00:44:41]** So that’s the Apple version of Apple.
 
**[00:44:45]** How I made myself an Excel sheet to compare cars.
 
**[00:44:48]** After the car, which car, what consumption, what does it cost,
 
**[00:44:52]** how can that be measured?
 
**[00:44:54]** We fit everything in, dog, cat, mouse, kids.
 
**[00:44:57]** And then eventually it was the test drive.
 
**[00:45:00]** That had a different reason.
 
**[00:45:02]** Maybe if you did that, I think I wouldn’t open the Excel sheet anymore. You could tell it,
 
**[00:45:08]** be careful, you know what I’ve driven so far, it probably knows, I’d have to
 
**[00:45:11]** actually try it, but knows what I’ve driven so far, it will probably get
 
**[00:45:15]** many things out of the lineup. What do I need for a car if I’m getting a new one? And then
 
**[00:45:20]** it gets exciting because then you suddenly have really simple or
 
**[00:45:27]** rather complicated advice, explanations, continuity, support and maybe even, when
 
**[00:45:35]** you buy a car, we have to take a look, probably also purchase.
 
**[00:45:40]** Yes, that’s a bit of the question also raised, who decides
 
**[00:45:47]** still and how much does the AI already know in the decision-making process, because of course
 
**[00:45:52]** now you have such a car purchase, whether that’s someone else, jeans or shoes or something.
 
**[00:45:58]** So definitely an enterprise-class, jeans and shoes.

**[00:46:01]** Everything is irrelevant, I believe. I don’t follow that out at all. Then it’s more like,

**[00:46:06]** this, I think all these products certainly have a different journey that

**[00:46:13]** is not solely based on my research on the Internet. So there is then of course

**[00:46:19]** sometimes, when I say, okay, now I just have the product in mind and now I can

**[00:46:22]** simply solve it with an AI, I don’t know if that’s essentially a quick shot,

**[00:46:26]** that could either argue against or in favor of the purchase

**[00:46:30]** decision. It doesn’t matter. But I believe that in my personal buying journeys,

**[00:46:34]** there’s still the tactile feeling somewhere or the

**[00:46:39]** conversation in the evening over Kölsch sharing something with someone.

**[00:46:43]** Yes, for the tattoo marketing.

**[00:46:44]** Exactly, that has been a purchase track for all this time. And that means, that’s naturally

**[00:46:48]** one of those things where I say, the browser and the AI-supported browser have,

**[00:46:53]** in my opinion, already done a Chat-CPD for me beforehand in the chat version.

**[00:46:56]** It simply summarized five things, as I said, this little layer, that

**[00:46:59]** you’re a bit more in the human loop when you first activate it on

**[00:47:02]** a website where you want to take a look. But I think that’s just so

**[00:47:09]** a small aspect. I believe if the AI, and we will see that in the next

**[00:47:13]** periods, will rather take over the whole operating system. So it will have access to everything

**[00:47:18]** on my computer. Or possibly also to my entire periphery, meaning not

**[00:47:24]** only on my computer but also here in the speakers in my room,

**[00:47:28]** in my Alexa, something else, on my phone.

**[00:47:31]** You know, my egg also performs journalism, listening in, and the information

**[00:47:37]** can flow, the metaglasses that provide you with information. I believe, if

**[00:47:43]** this gap is also being closed, and it will be closed. Because from a usability perspective,

**[00:47:50]** from a progress perspective, it makes massive sense that we are. But in principle, AI can really

**[00:47:57]** provide this environment better, also with animals and more information, so that we make better

**[00:48:02]** decisions and, above all, maybe be able to tell whether that’s some kind of fake content,

**[00:48:06]** that we are seeing somewhere, or something else. And whether that is a good decision,

**[00:48:10]** it can verify again, all these topics that we always address critically, that we

**[00:48:14]** cannot rely on the fact that this advice is perhaps correct right now.

**[00:48:17]** No, everything will improve with AI, because it can simply be examined manifoldly more often

**[00:48:21]** and multiple AIs can interact with each other, and we hopefully, in principle,

**[00:48:25]** do give the right advice.

**[00:48:27]** But we are just not there yet.

**[00:48:29]** This is a world that we will enter, and it will definitely be some future

**[00:48:37]** AI world, just like we have always seen in Star Trek or other science fiction,

**[00:48:42]** where the computer, at any moment, when I talk to it, when I access it,

**[00:48:47]** provides comprehensive information about the entire context. The browser, now, better than the

**[00:48:54]** plain chat window, so the window to the world is no longer just a text window,

**[00:48:59]** but now one can say, it is already the browser that can show me video text content,

**[00:49:06]** multimedia things, my AI can now sit on my shoulder and

**[00:49:12]** watch while I look through this window at the world. And this window is,

**[00:49:17]** not small. It is the window that since '96, '97, '95 has always been World Wide Web. That is

**[00:49:24]** one that has massively changed the world, that has brought us much closer together, that has

**[00:49:31]** helped people understand things that we did not comprehend before, in contact with

**[00:49:34]** with people we couldn't even be in contact with in the world before. That is

**[00:49:39]** of course a bit cool that this can now also help with such a little AI parrot on

**[00:49:44]** my shoulder. Yeah, you just gave me the feeling of

**[00:49:48]** being old because I definitely know the world before the browser and I

**[00:49:54]** still remember discussions about the internet, like work.

**[00:50:01]** Back then I worked quite easily as a tax consultant, how is that supposed to happen, what is

**[00:50:06]** that nonsense, yes, when I still thought that writing in all caps was considered shouting and the friendly

**[00:50:13]** you was a normal tone of conversation in an email correspondence on the internet, yes, and at some point

**[00:50:19]** that became formal and at some point writing you in all caps was no longer shouting and

**[00:50:25]** stuff like that, because somehow, I don't know, society has lived everything differently,

**[00:50:31]** than the little Northern market thought was possible back then and now we are talking about,

**[00:50:35]** that this stupid browser, which then suddenly, let’s say, the way of interactions

**[00:50:41]** we have, has changed, actually becoming smart.

**[00:50:44]** Mhm.

**[00:50:45]** It's already crazy.

**[00:50:46]** It's really crazy, right?

**[00:50:47]** And it will change all sorts of things again.

**[00:50:50]** We had it again in our first episode, if there's no ikunde,

**[00:50:54]** it’s just another episode that’s about more and more interactions,

**[00:50:59]** that will be more of a human nature, with our websites, with our

**[00:51:02]** applications that we have. It won't just end with websites, of course, as it

**[00:51:05]** I have already hinted at. So AI will increasingly work its way out of the

**[00:51:10]** window, already now to the browser level. The next consequential

**[00:51:15]** will then actually probably be the entire
 
**[00:51:17]** operating system that the AI can look at and afterwards
 
**[00:51:21]** essentially the next larger system in the environment. This means the AI is fighting
 
**[00:51:25]** to move further up to support us better, because those are all
 
**[00:51:29]** technical platforms designed to help us. But it naturally leads to,
 
**[00:51:33]** us needing to think differently about producing content. So now, we have been optimizing
 
**[00:51:39]** websites for humans for years. Now we are starting to optimize them for the machine,
 
**[00:51:44]** to be honest. It also has to work well for a machine if I want to stay
 
**[00:51:49]** in touch with my customer group, whatever else comes from it.
 
**[00:51:53]** Or if you want to gain new customers who might then come through the AI channel,
 
**[00:52:00]** to the surface. So today you have a web-on app and if you somehow have a generation

**[00:52:04]** has, who thinks, what googling, that also comes from my parents. I ask the AI and the
 
**[00:52:12]** AI when googling, when googling. Thanks for falling for that too. When the AI then
 
**[00:52:18]** while you say, I don't know, I'm interested in vacation homes somewhere, suddenly it
 
**[00:52:22]** says, you can find that at your friend's fan apartment Booking here please HAS or
 
**[00:52:28]** enter, what are you too funny, you could also book something right now, because, look,
 
**[00:52:32]** you said you want to go there and at all, I checked once,
 
**[00:52:35]** there is even something available and then offers you the thing, what is I, in the booking portal
 
**[00:52:40]** or they facilitate the booking and not because you thought,
 
**[00:52:45]** ah, this is super great to take provider abc, but because then provider abc through
 
**[00:52:50]** inserting small coins or the trimming, the AI provided a certain motivational aid,
 
**[00:52:56]** to offer this in the auditorium of the sphere. Suddenly art is being directed about it. And yes, there has to be

**[00:53:02]** one can also come. Yes, one can present oneself so that the AI says, you are a great idea for

**[00:53:07]** the topic ABC, then I best offer you the topic XYZ and then you just have to

**[00:53:12]** optimize yourself so that the AI thinks, oh, I can do this super well or really well or no

**[00:53:17]** But this is a completely new playing field, it’s not here yet, but I also believe it will come.

**[00:53:23]** Yes, everyone out there who is thinking about designing interactions,

**[00:53:29]** with people should really consider what a possible experience for an AI looks like.

**[00:53:36]** This is basically the topic that AI, of course, will also inherently,

**[00:53:42]** In the future, it will also prefer machine-readable websites, that is, websites that are well-coded, and look at those preferentially.

**[00:53:51]** However, it will, in principle, also be able to, yes actually, if it can see and access other websites, it will, as it always does, develop empathy for something that works well and with which the bots interact. So I will definitely try out the service right after this episode,

**[00:54:10]** to see whether one can interact with this or that service chatbot found on various websites

**[00:54:14]** and what comes out of that.

**[00:54:16]** So that's quite interesting.

**[00:54:19]** So this topic, the experience design for AI agents, is a topic that is not

**[00:54:26]** only in the virtual world, but as I said, we'll soon do an episode on robots

**[00:54:30]** yes, also when the robot comes around the corner, it also wants

**[00:54:34]** at least to have a good experience, to speak in quotes, about what

**[00:54:38]** a good experience could be and how it's represented.

**[00:54:40]** We can gladly consider this in another session.

**[00:54:43]** When the other robot then says,

**[00:54:45]** your shoes, your pants, and your motorcycle or your jacket, or how was it in Terminator

**[00:54:49]** again, we need to have that figured out.

**[00:54:51]** Yes, but yes, that's not what he does either.

**[00:54:53]** Yes, then we'll be introducing it next time.

**[00:54:56]** Yes, yes, yes, I think so too.

**[00:54:57]** But how it is, remains exciting now.

**[00:54:58]** So now, I believe we are in such a world,

**[00:55:02]** where it is no longer so important where I click,

**[00:55:05]** but rather where my browser clicks. Interesting about that.

**[00:55:09]** And how often?

**[00:55:10]** How often? I mean, you can also open more tabs and search for whatever,

**[00:55:16]** that I take 20 booking portals and find the best flight.

**[00:55:20]** That's also a question.

**[00:55:21]** So, this topic has already been so much improved by AI systems and the GPG moment,

**[00:55:25]** that it has become significantly better.

**[00:55:26]** So, this whole topic of searching,
 
**[00:55:29]** researching, when I know what I want in that direction or even,
 
**[00:55:32]** when I don't know what I want.
 
**[00:55:33]** So also being creative, that's all possible at the moment.
 
**[00:55:36]** I don't know if I've actually mentioned this in this podcast yet, but
 
**[00:55:39]** where I have already brought up what news case I could imagine with
 
**[00:55:43]** AI, and I always say, man, I can't imagine a single scenario
 
**[00:55:46]** that doesn't involve AI.
 
**[00:55:47]** So everything is actually simplified by AI, because it is a general
 
**[00:55:54]** intelligence that we have at our disposal and not a specialized intelligence,
 
**[00:55:58]** that accesses specialized knowledge, but it is general just as little as

**[00:56:01]** it's an app that only has a specific use case because it can expand.

**[00:56:07]** It can handle functionalities over, we’ve already discussed the MCP server topic, it could already

**[00:56:11]** access functionalities, now with the browser capability, which some

**[00:56:15]** agents already had before, but now presented as a browser again, it can

**[00:56:18]** actually sharpen websites, click to browse, so all content, like

**[00:56:23]** I mention again, all content that is somehow accessible via the browser

**[00:56:27]** is reflected, for example, everything can be removed, but I can now

**[00:56:30]** and everyone can play around with it, all the time, if they want, everything is possible

**[00:56:34]** in that moment.

**[00:56:35]** This is somewhat like a crazy step that is currently happening, which is technologically

**[00:56:42]** not that far away, because it’s something those things have actually always been able to do,

**[00:56:45]** because they were partly also trained to see how websites

**[00:56:49]** could be understood, how they can click, analyzing click streams and stuff like that, those are

**[00:56:53]** also part of the training data.

**[00:56:54]** But now it’s being made available to the mass market, so that anyone who can install something like this,

**[00:57:01]** is already changing the world a bit again and we should still return to the disclaimers.

**[00:57:06]** So I would still be very, very, very, very restricted and very careful with using it, because it actually

**[00:57:14]** has added another layer that I believe is very easily targetable and you have to

**[00:57:20]** really want to and know what you’re doing before you may rely too much on it

**[00:57:26]** and say, come on, here’s my bank account, let’s click here again

**[00:57:30]** and call up something great for me or something like that,

**[00:57:33]** that could also backfire.

**[00:57:39]** When you were speaking, I remembered a story that someone told me,

**[00:57:43]** what he uses the Atlas for, namely to improve websites and specifically for
 
**[00:57:52]** personas with certain characteristics.
 
**[00:57:54]** With the motto: surf the website and give me a rating for people who only
 
**[00:58:01]** can understand simple language, for people who this, that, or the other.
 
**[00:58:05]** They then got a report from Atlas and found it so cool that
 
**[00:58:11]** they are considering offering that as a service to other providers, where I thought,
 
**[00:58:16]** look, you have a whole set of Atlas thingamajigs that basically do nothing but test websites,
 
**[00:58:23]** or you can think further, you're also monitoring changes,
 
**[00:58:29]** you're doing competitor comparisons, you're doing who knows what, those are just things that you can now
 
**[00:58:36]** automate at your fingertips. Yes. Yes. The world is beautiful. Earlier, when we talked about the
 
**[00:58:44]** episode, you mentioned something, you told me about a small background.

**[00:58:49]** I would really like you to share that again with us and the listeners because I only half-listened to it,

**[00:58:54]** to be honest, because I thought you were telling it for me. Hopefully, you're sharing that

**[00:58:59]** in the episode because I believe you will tell that, and then I can try it out afterwards,

**[00:59:03]** because I actually hadn't dealt with it yet.

**[00:59:07]** Would you mind unraveling that veil for us?

**[00:59:09]** Sure, I'd love to do that. I came across it through a post from

**[00:59:15]** some Robert, who talked again about his four favorite tools that he's currently

**[00:59:25]** using, and I had always wanted to try one of the cool ones,

**[00:59:28]** but I kept putting it off.

**[00:59:30]** And that is Whisper Flow.

**[00:59:32]** Whisper Flow spelled W-I-S-P-R.

**[00:59:37]** You can check it out on Google; it also has a mobile application.

**[00:59:41]** And I definitely don't know if it exists for Wind.

**[00:59:43]** Mine is also a Chrome extension.

**[00:59:45]** I have now installed it here as...

**[00:59:47]** Let's just call it at the Mac port.

**[00:59:49]** I find that totally likable.

**[00:59:51]** No, no, no, I'm recording.

**[00:59:53]** I'm also an old can user.

**[00:59:54]** Accordingly, I understand both sides in this case,

**[00:59:56]** just as I am a Startway and Star Wars fan.

**[00:59:59]** But that's another topic; what Whisperflow does is actually a bit cool.

**[01:00:04]** You basically have a speech-understanding tool that can record your voice,

**[01:00:13]** which packs it somewhere via the microphone and yes, because on the Mac it's like this,

**[01:00:18]** I just need to press the function key, and when I'm in any text field,

**[01:00:22]** no matter if it's in the browser, in any application, Slack, Teams, whatever, Outlook,

**[01:00:28]** you name it, Excel, I can essentially input this speech directly into that text input field,

**[01:00:34]** in.

**[01:00:35]** It also corrects a little, it creates a stitching dictionary, the privacy settings

**[01:00:39]** are such that everything stays on my computer, so it's all safe

**[01:00:42]** so far.

**[01:00:43]** That's a huge relief, because in connection with Robert's post,

**[01:00:48]** I also happened to read another article at the same time, which was about

**[01:00:51]** software users, who had written that they use WhisperFlow for their programming.

**[01:00:57]** indeed and have observed that when they start developing with it, that those

**[01:01:03]** at the beginning, well, about 10 to 17 percent use Whisper Flow in the first month, so the

**[01:01:09]** comparison, basically the use of peripherals, meaning, keyboard, mouse, or indeed the microphone

**[01:01:16]** and from the 4.5 month mark, the use of the microphone via Whisper Flow is already at 75 percent,

**[01:01:22]** This means that the programmers have switched to using voice input as much as possible instead of relying on the keyboard

**[01:01:28]** and the mouse, to do everything primarily via voice input, of course supported

**[01:01:33]** with the Co-Pilot-Whatever, GitHub-Co-Pilot-Cloud, whatever, AI, which basically

**[01:01:39]** simplifies programming as well, but it is indeed,

**[01:01:42]** because speaking is simply faster.

**[01:01:43]** You can hear it right now, I'm speaking quickly again, but at that speed

**[01:01:51]** there are people who can type that fast. I definitely am not one of them. And it helps me

**[01:01:55]** I really like the tool. You can try it out. I think, in a free

**[01:01:59]** You can somehow add so and so many thousand words in that version.

**[01:02:03]** I think that's enough for the standard used. Otherwise, you can certainly

**[01:02:06]** get the trial version. If you have similar tools, we don't want to

**[01:02:10]** only advertising for Eintol here, if there are others that are in the same

**[01:02:13]** If you're going in that direction, feel free to leave a tip in the comments. Otherwise

**[01:02:19]** I'm glad that we've done a tech tip again, Mark.

**[01:02:22]** That's why we decided in the second or third episode, I believe,

**[01:02:24]** that we want to make a tech tip every time.

**[01:02:26]** Now we've done it again.

**[01:02:29]** Good that you remembered. 

**[01:02:31]** I know the whole warmth.

**[01:02:32]** You've been at the buckets,

**[01:02:34]** that this dictation into text fields is also not in the barriers,

**[01:02:38]** that the freedom function of MeckOS is also hidden somewhere.

**[01:02:42]** I still need to search for that.

**[01:02:43]** But in any case, it sounds like they are so comfortable.

**[01:02:46]** Let's do it this way.

**[01:02:48]** It is also different, because it is naturally so, I don't know if that is in these dictation functions

**[01:02:52]** always already with such a Natural Language model essentially in the background, that then indeed

**[01:02:56]** can recognize possible discussions and such, right?

**[01:02:58]** So, because of course, the tier functionalities existed back then with Dragon, Dictate and such

**[01:03:02]** on Windows 3.1 or something, I believe, yes?

**[01:03:04]** Oh, or if also there were memories, yes, if you have people who had that

**[01:03:08]** it was proud and you call into the mic, Shutdown.

**[01:03:11]** Shutdown, shutdown, Open Text Editor or something you could already say back then, that was

**[01:03:16]** pretty cool, right?

**[01:03:17]** also gave a bit of Star-Trek vibes, but the speaking I'm doing right now

**[01:03:22]** at this speed, then transferring it into a perfect text, that just didn’t work

**[01:03:27]** until the speech models were advanced, so accordingly that only

**[01:03:32]** as my tool tip. At this point a cheerful Hey Alexa, buy a thousand

**[01:03:37]** diapers, at this point the stillest go out, that give, where the Alexa activates.

**[01:03:42]** Yes, so thanks for the tip. I actually have no one today, but that

**[01:03:48]** makes your tip even more valuable.

**[01:03:50]** Very good.

**[01:03:51]** Jens, I think it's an hour four. We spent the time well. I hope it was

**[01:03:58]** interesting for all of you as well. I hope we don't have to check too many fluff

**[01:04:04]** next time. What would we have done with you in the episode

**[01:04:07]**?

**[01:04:08]** error-free. We are the better AIs, did I say that? No, the AIs are better, of course.

**[01:04:14]** Maybe we won't take it, so hallucination check or something like that, no idea.

**[01:04:19]** Hallucinating is just, that's a bit of a negative term, so honestly, if you

**[01:04:24]** or I had made a mistake, no one would have said earlier that we are hallucinating,

**[01:04:27]** but we just made a mistake. It's kind of a story that, in my opinion, has been skewed

**[01:04:33]** a bit in the wrong direction now, purely from the

**[01:04:39]** fact that these things make mistakes, no question, that if they have too large a context

**[01:04:42]** with LMMs and such, then they also produce mistakes, but we're

**[01:04:45]** working on that everywhere to make it better. And I would also say, we are in

**[01:04:49]** many respects already further than we humans have ever been. And I'm curious where we

**[01:04:56]** will still go. Not like today, they will never work again.

**[01:04:59]** Then we wrap it up, right?

**[01:05:01]** Great episode, Mark. Until next time.

**[01:05:03]** Next time it's about robots.

**[01:05:05]** Next time I think I'm going about robots.

**[01:05:07]** If you're interested, subscribe to the channel,

**[01:05:09]** let your friends know,

**[01:05:11]** that a great episode is coming soon,
 
**[01:05:13]** that we also have a lot of great episodes.
 
**[01:05:15]** We have now surpassed 1000 downloads.
 
**[01:05:18]** Onwards to the next 1000 in this spirit.
 
**[01:05:21]** It was nice with you, Jens.
 
**[01:05:23]** Hopefully soon again in this spirit.
 
**[01:05:25]** Ciao.
 
**[01:05:28]** Welcome to Think Different, Think AI, the podcast from Mark and Jens.
 
**[01:05:34]** Two technology-loving minds who not only talk about artificial intelligence but live it.
 
**[01:05:40]** Here you will find clear classifications, real practical insights, and a fresh perspective on what is possible.
 
**[01:05:47]** Understandable, critical, and always with a wink.
 
**[01:05:51]** HI for reflection, for a chuckle, and above all for engaging in conversation.
