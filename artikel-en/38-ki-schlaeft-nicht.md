---
folge: 38
titel: "When the agent works through the night: sandbox, watchdog and the price of thinking depth"
bildtitel: "What does the agent do at night?"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/38-ki-schlaeft-nicht"
---

# When the agent works through the night: sandbox, watchdog and the price of thinking depth

*A coding agent that loses context after 20 minutes is a tool. One that runs for eight hours is a colleague with system access. What that demands in safeguards, and what the highest thinking level actually costs.*

By Mark Zimmermann

This episode manages without a guest and with a lot of news from an industry that by now releases models more often than other people change their underwear.

The core is nonetheless a single question: what happens when an agent no longer breaks off after 20 minutes but works through the night.

> **in brief**
>
> - Claude Opus 4.7 brings effort modes from medium to max; in maximum mode up to 40 per cent higher costs can arise
> - An autonomously running agent needs a sandbox, hooks, a watchdog with heartbeat and a log of its decisions
> - Claude Design attacks Figma and imports existing design systems
> - Trust in a vendor counts as much for tool choice as benchmark figures
> - A lot of tokens burn on people shuttling results between two models

## The price of thinking depth

Claude Opus 4.7 introduces effort modes: medium, high, x-high and max, plus finer tokenisation. Both increase accuracy and both cost.

The order of magnitude is relevant for any calculation: in maximum mode, up to 40 per cent higher costs can arise. That is not a rounding error but a factor that decides the economics of a use case.

From this follows a control question many tools do not yet answer: how much control do you want over automatic delegation to smaller models. A system that switches to a weaker model by itself saves money and possibly changes the result. A system that never does is expensive. Running either without transparency is the worst variant.

Important here: in the end, tool choice does not only count the yardstick. Trust in the vendor plays a part, because you leave them running processes and data. Benchmark figures change quarterly, a vendor relationship does not.

## The agent that runs through

The actual core of the episode is a setup called Claude Night Shift: a combination of skills and shell scripts with runbooks, hooks, a macOS sandbox and a watchdog with heartbeat monitoring. That turns an interactive tool into an autonomously working process that blocks destructive commands and documents its decisions traceably.

The components are individually unspectacular and in combination precisely what is missing when people let agents run unsupervised.

> ### What an autonomously running agent needs
>
> **Sandbox.** A bounded area in which the agent may write. Without that boundary, the wording of the assignment alone decides which files are affected, and that is not a safety measure.
>
> **Hooks.** Intervention points before and after certain actions. There, destructive commands can be caught before they are executed, and results checked before they are accepted.
>
> **Watchdog with heartbeat.** A process that monitors whether the agent is still alive and still making progress. Without it, a hung run looks no different from a working one from the outside, and that is only noticed the next morning.
>
> **Runbook.** The written statement of what to do when something goes wrong. On overnight runs there is nobody there to improvise.
>
> **Decision log.** A traceable record of why the agent chose a route. Without this log, a result in the morning cannot be assessed, only accepted or discarded.

Anyone who does not have these five points and still runs overnight is operating not an autonomous system but an unsupervised one.

## Claude Design and the toolbox

The other focus is Claude Design, Anthropic's design and prototyping tool. The feature set ranges from wireframes through functional animations to importing existing Figma files and design systems, and one weekend of trying it out was enough to think seriously about switching.

The import is the interesting part here. A tool that takes in existing design systems does not attack the drawing process but the switching costs. That is exactly where previous challengers such as Google Stitch failed.

In parallel, image generation has arrived in everyday use: Nano Banana at Gemini, GPT Image 1.5, plus tools such as Manus or Crea.ai that solve subsequent editing of text on generated infographics. That was long the practical weak point, because a chart with a misspelt label is useless.

## The token waste nobody talks about

Finally an observation that saves money as soon as you have seen it once. A considerable share of consumption arises from people shuttling AI-generated documents between two models. Copy the result out of one system, paste it into another, copy the answer back.

Each of these steps costs tokens for content that has already been processed once. The alternative is direct connections between the systems, via A2A or MCP. The effort for that is one-off, the saving runs on.

Connected to this is a question the episode leaves open: when does automation stop being procrastination and start getting work done. A setup that costs three days of tinkering and saves ten minutes a week is a hobby. That is fine, but it should be called that.

## Conclusion

The episode delivers a clear dividing line. An agent you watch needs a good model. An agent that runs unsupervised needs an environment.

Before you start the first overnight run, clarify five things: where may it write, what may it not execute, who notices that it has hung, what happens then, and how do you recognise in the morning whether the result is usable.

And check your cost calculation against the highest effort mode, not against the middle one. The difference of up to 40 per cent decides the economics more often than the choice of model itself.

> **The story continues …**
>
> On the side, a meeting assistant for an Even Realities AR headset came about over a weekend. Such setups are currently one-offs. They become interesting as soon as somebody answers the question of how an agent that listens permanently deals with the rights of those present.

---

The full episode: [KI schläft nicht !](https://think-ai.podigee.io/38-ki-schlaeft-nicht)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
