---
folge: 52
titel: "Voice notes: without an interface the archive stays a swamp"
bildtitel: "Recording is not enough"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/52-exokortex"
---

# Voice notes: without an interface the archive stays a swamp

*A dictation device on your lapel does not solve a knowledge problem. Only machine access turns 28 spoken notes into a list you can work through. A field report from a holiday, with an invoice attached.*

By Mark Zimmermann

The plan was a holiday without technology. No laptop, an e-book reader instead, the phone as rarely as possible. This episode was recorded anyway, from a Tesla in a holiday park car park in Denmark. The reason is a vendor update from 23 July: Plaud released an MCP server. That sounds like a footnote in a changelog, yet it moves the line between recording device and working tool.

> **in brief**
>
> - A voice recorder without machine access creates an archive nobody touches again
> - The MCP server makes the notes queryable from Claude, ChatGPT or Gemini
> - Apple's Voice Memos record and transcribe locally, but offer neither bulk export nor an interface
> - 28 notes from 48 hours could be sorted with a single question, and partly dealt with straight away
> - Anyone wanting to keep the data in house pulls the audio files via the API, transcribes locally with Whisper and puts their own MCP server in front

## The bottle deposit problem

The first attempt failed, and not because of the hardware. A Plaud Pin, clipped to the lapel, reliably recorded whatever it was asked to. The problem arose afterwards.

> “I record something. Yes, I record something else, I'll listen to that again tomorrow. Oh, now I have recorded 40 messages, good heavens, I will never listen to those again.”
>
> **Mark Zimmermann**, co-host

The image for it is the empties under the desk. Two bottles you take back, four as well, at twenty you give up. Recording costs five seconds, following up costs a multiple of that, and this ratio topples every archive that depends on listening back by hand. The Pin was sold on.

Note that this effect has nothing to do with recording quality. It arises wherever a store grows faster than it can be worked through. Anyone who has ever created a folder called “read later” knows the mechanics.

## What the MCP server changes

The current device, the Plaud Note, has the format of a credit card, a microphone array, its own storage and clips onto the back of the phone via MagSafe. Recording runs locally, around 30 hours fit on it. Technically this is an update, not a leap.

The leap is in the interface. Since 23 July, Plaud has provided an MCP server. The notes therefore no longer sit only in the vendor's app, but can be queried from Claude, ChatGPT, Gemini or a self-built harness.

The practical case from the holiday: 28 notes in 48 hours, recorded while cycling, at night in bed, between two excursions. Partly emails, partly reminders, partly project thoughts. A single question to the model, asking what tasks had come up in the last 48 hours, returns the sorted list, along with an offer to deal with them straight away. One of the emails was fully drafted afterwards.

Important here: the achievement is not in the model and not in the microphone. It lies in the fact that an agent can read the stock at all. That is precisely where the predecessor failed.

> ### What an MCP server does
>
> The Model Context Protocol is an open standard through which a language model accesses external data sources and tools. An MCP server publishes a manageable list of functions, for example “retrieve notes from the last 48 hours” or “search the full text”. The model decides for itself which of them to call, and receives structured data instead of a web page.
>
> The difference from a classic API lies less in the technology than in the addressee. An API is aimed at developers who hard-wire the calls. An MCP server is aimed at a model that decides at runtime what it needs. For the user this means: they phrase a question in ordinary language instead of building a query.

## Why Apple's Voice Memos stop at this point

The obvious objection is that an iPhone brings all of this along. Recording works via the Action button, on the Apple Watch Ultra as well, and transcription runs locally on the device.

The objection holds as far as the filing and no further. The files sit in the Voice Memos app, and that is where they stay. There is currently no MCP access, no bulk export and no file access from outside. That leaves out exactly the part that turns an archive into material. Apple delivers the two steps nobody struggles with anyway, and omits the third.

Do not expect a quick fix here. The missing export is not an oversight but follows the system architecture, in which user data is not meant to leave the app. For data protection that is an advantage, for the use case described it is a knock-out criterion.

Anyone who still wants to keep the data in house takes the opposite route: pull the audio files off the device via the Plaud API, transcribe locally with Whisper, put your own MCP server in front. The effort is considerable, and the result afterwards sits on your own drive.

## Two ways of working with speech

Two usage patterns compete in this episode, and the difference is practically relevant.

Jens Scharnetzki uses speech as a dialogue channel. He talks to the model because he speaks faster than he types, and expects an immediate answer. In the car, while cooking, wherever his hands are busy. The appeal lies in the back and forth, by now also combined with computer use: the model reads out the options from a travel portal, you confirm, it clicks and books.

The second pattern is asynchronous dumping. No feedback, no answer, just filing. The reason is banal and decisive nonetheless: eight topics would be eight chats, and eight parallel chats cannot be managed on a phone. Anyone who instead records unsorted and leaves the sorting to a machine later does not have to remember on the move which thought sits in which context window.

For this offloading, the episode produces the term exocortex. It hits the matter more precisely than “second brain”, because it describes what actually happens: mental work moves out of the head and onto a device. The difference from a second brain lies in the preparation. Stored and findable is the preliminary stage. It only becomes usable once a machine can work with it.

## What the setup costs

At this point the episode becomes concrete, in euros. A second brain is not a product you buy.

> “There is no voodoo in it. If someone sells you a second brain for a lot of money: run away, run even faster. Make a folder, put three markdown files in it, and you already have your first second brain.”
>
> **Mark Zimmermann**, co-host

What gets expensive is not the system but enriching the old stock. Jens Scharnetzki retrieved his X archive with around 20,000 likes via the GDPR data export. The export itself costs nothing, but on its own it is of little use: the interesting links sit in the first comment and not in the post, because the algorithm penalises posts with external links. So he sent the API after it and loaded the comments down to the second level. One day of compute, 41 euros one-off. Ongoing, the costs are in the cents, because only the new likes are added.

He considers the investment worthwhile, because a like reveals what interested him and when. From the history it is possible to derive which topics carry weight for him and which he let go. That is a different quality of context than a list of projects.

The benefit shows when changing provider. Jump from ChatGPT to Gemini or Claude, and the new model does not know who you are, what you are working on and what matters to you. A second brain carries that across.

## The openly worn microphone

One point remains explicitly unresolved in the episode, and the two say so on the record. Legal advice it is not.

The observation behind it is remarkable nonetheless. A microphone worn visibly on the lapel prompts questions. The same device in a trouser pocket, a phone, a pair of earbuds on the table, prompts none, although technically it can do the same.

> “People should know what you are carrying, people should know what you can do, what you are doing. Of course consent is always needed, and a no has to be accepted as well.”
>
> **Mark Zimmermann**, co-host

The Plaud Note has no prominent recording light. Anyone wanting to record conversations with it needs the consent of those involved, and experience with earlier devices shows how easily that goes wrong: you forget to switch off a 3D-printed microphone on a neck chain, and then half an ice cream parlour ends up in the archive.

The hope of the two lies in technical solutions rather than abstinence. A signal would be conceivable that tells the other person's device that no consent has been given, for instance through tones inaudible to humans. Only the direction is certain: as local models get smaller, more such devices will be running around us, not fewer.

## Conclusion

Only on the surface is this episode about a recording device. Underneath it is about a question that decides every knowledge system: can a machine get at the stock.

Anyone wanting to start today needs neither a product nor a budget. A folder, a few markdown files, linked to each other, that is enough for a start. The actual work comes afterwards, in enriching the old stock, and that can be quantified: one day of compute and 41 euros for 20,000 likes.

And anyone buying a device should check the interface before the recording quality. A recorder without export is an archive that grows and belongs to nobody who can read it.

> **The story continues …**
>
> At the end of the episode a point comes up that is barely discussed yet: prompt injection also works through voice messages. Anyone tipping foreign audio files into a system an agent is allowed to evaluate opens the same attack path as with manipulated text. Trust incoming audio as far as you would trust an unknown PDF.

---

The full episode: [EXOKORTEX](https://think-ai.podigee.io/52-exokortex)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
