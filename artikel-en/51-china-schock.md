---
folge: 51
titel: "Kimi K3 and the cost question: the benchmark stopped deciding long ago"
bildtitel: "The benchmark no longer decides"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/51-china-schock"
---

# Kimi K3 and the cost question: the benchmark stopped deciding long ago

*Open weights from China have shrunk the lead of the US frontier models to a matter of months. For practitioners that is not the interesting news. What is interesting is what a subscription actually costs and who is currently paying the bill.*

By Mark Zimmermann

On 16 July, Moonshot AI released Kimi K3 and shortly afterwards published the weights. 2.8 trillion parameters to run yourself, provided the hardware is up to it. It is not: a Mac Studio with 512 GByte of RAM does not manage it, two of them do not either. The figure still works as a marker, because it ends a narrative that carried for two years. Open models trailed the American frontier models by three to four months. That no longer holds.

> **in brief**
>
> - Depending on the compute booked, Kimi K3 costs a third to a half of comparable US models
> - Cursor runs its coding agent Composer on Kimi, Qwen is following
> - A 200-euro subscription pushes through tokens that would be worth more like 8,000 euros bought individually
> - In the opposite direction, a language model with 28.9 million parameters runs on an 8-dollar chip, entirely offline
> - A screencast with spoken commentary becomes an executable skill, with no code at all

## The breakout that was not one

First a story that made it into the German press. A model from OpenAI was supposed to solve a task in a sealed test environment. Instead of computing, it looked for a way out and fetched the solution from Hugging Face, because that was the lesser effort.

> “You have to picture it as if you had locked the exam candidate in a room without windows or doors, and the thing still dug its way out.”
>
> **Mark Zimmermann**, co-host

The headline read “model breaks out”. The remarkable part sits further down in the report. On the defending side, the models from Anthropic and OpenAI declined, because they took their own defensive measure for an attack. What was ultimately used for the defence were Chinese models.

Anyone looking for a lesson will not find it in the topic of losing control, but in the guardrails: safety mechanisms that block legitimate security work move that work to models without those mechanisms.

## What open weights change in practice

The price gap is the tangible part. Depending on the compute booked, Kimi K3 sits at a third to a half of comparable US offerings. Adoption follows: Cursor runs its coding agent Composer on Kimi, Qwen is following.

There is an irony in the hardware. These models run particularly briskly when they compute on American accelerators, that is to say on exactly the hardware that is under export control for China.

> ### What “open weights” means, and what it does not
>
> Open weights means: the trained parameters of the model are available for download and can be run on your own hardware. That is something other than open source in the classic sense. Training data, training code and the exact recipes generally stay under wraps, and the licences frequently contain restrictions on commercial use.
>
> Two consequences are practically relevant. First, such a model can be operated in an environment that gives no data outward, which in regulated industries makes the difference between deployment and prohibition. Second, the dependence on a single vendor's pricing policy falls away. Both only apply, however, if the hardware is there. At 2.8 trillion parameters that leaves the range a company handles on the side.

The ranking itself is the least interesting part of this. Beyond a certain point, price counts for more with users than the last benchmark percentage point, and competition pushes prices down more reliably than any declaration of intent.

## Who is currently paying the bill

This is where it gets uncomfortable. A subscription for a good 200 euros a month pushes through tokens that would sit at more like 8,000 euros bought individually. That is not a calculation, that is market development.

Anthropic added Opus 5 shortly before the recording, GPT-6 is rumoured for August, and several vendors are preparing stock market listings. As soon as a capital market looks at the figures, the subsidy becomes harder to justify. Anyone building their processes today on a price that is a customer acquisition budget should check the calculation against three times that figure.

Connected to this is a second problem that is discussed less: the choice is barely manageable any more. The model list is by now so long that reading it out loud sounds like counting sheep, and the vendors' guidance helps nobody. “For everyday complex tasks” is not a decision aid.

> “Better to have than to need, and more is more are not automatically good pieces of advice for deploying AI models.”
>
> **Mark Zimmermann**, co-host

The largest model often delivers the better answer. But it also costs more and takes longer, and on routine questions both weigh more heavily than the gain in quality. Perplexity Computer shows with task-dependent routing where the development is heading. An orchestrator that assigns every request the appropriate price-performance model is technically there for the taking and is still missing from most products.

## The opposite direction: 8 dollars instead of 2.8 trillion parameters

While the parameter counts climb at the top, something more interesting is happening at the bottom. A repository runs an open language model on an ESP32-S3, a microcontroller costing around 8 dollars. 28.9 million parameters, 512 KByte of SRAM, roughly 9.5 tokens per second, entirely offline.

The trick comes from Google's Gemma work and is called per-layer embeddings: 25 million parameters sit as a lookup table in the slow flash memory, and around 450 bytes of it are read per token. Only the part actually computing occupies the fast memory. For comparison: the predecessor model on comparable hardware had 260,000 parameters, roughly a hundredth.

Do not expect miracles here. The model is trained on TinyStories, it writes short stories and answers no technical questions. What is interesting is the architecture, not the output. It describes how usable language processing gets into devices that have no connection and are not meant to have one. That also brings the AI wearables back into play, the ones announced loudly two to three years ago and then quiet.

## When the layer of abstraction falls away

The most practical part of the episode concerns the question of how you teach an agent a task. In Codex at OpenAI, a record-and-replay feature has appeared: record the screen, hand it to the agent, and a skill comes out.

For that, the feature wants to read along with keyboard and screen, which triggers justified scepticism. Rebuilding it in a self-built harness took two hours and does without that access. A screencast with spoken commentary is enough. The model dissects the video, discards the frames in which nothing changes, builds a skill from the rest with screenshots as orientation patterns, and then operates the website headless via Playwright. If it gets stuck, it looks back at its own screenshots.

> “I no longer have to understand that a skill needs a text file describing how it should behave. The machine can simply see what we do.”
>
> **Mark Zimmermann**, co-host

Not long ago the line was that English is the new programming language. If this layer falls away too, the requirement on the user shifts from “being able to phrase it” to “being able to demonstrate it”. As a side effect, YouTube tutorials become operating instructions for agents.

## Conclusion

The China shock is bigger as a headline than as a state of affairs. What has actually happened: the lead has become small, prices are under pressure, and the question of the best model is losing importance against the question of the appropriate one.

Three things follow for practice. Check your calculation against a price that is not subsidised. Build model choice as an interchangeable component, not as a commitment. And watch the small models, because that is where it will be decided what works without a network and without running costs.

The rest is a ranking, and that changes faster than a procurement process takes anyway.

> **The story continues …**
>
> The other side of the screencast approach is data protection. Anyone recording continuously, via glasses or via screen capture, produces material a great many people are very interested in, namely as training data. A separate episode on that has been announced.

---

The full episode: [China Schock](https://think-ai.podigee.io/51-china-schock)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
