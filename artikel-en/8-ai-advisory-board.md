---
folge: 8
titel: "Three personas beat twenty: what an AI advisory board actually delivers"
bildtitel: "Three beat twenty"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/8-ai-advisory-board"
---

# Three personas beat twenty: what an AI advisory board actually delivers

*Twenty personas, eight to thirteen pages of description per role, a moderator agent that delegates and weights. The result was unambiguous: three well-chosen perspectives deliver better answers than a full panel.*

By Mark Zimmermann

The setup came about during a holiday and is remarkably thorough: a complete AI advisory board, built with n8n, the automation tool from Germany that according to Handelsblatt is now valued at 2.4 billion euros.

Instead of a single chatbot, behind it stand twenty system prompts that turn agents into personalities such as Steve Jobs, Angela Merkel, Elon Musk, Jeff Bezos, Tim Cook and Jonathan Ive. Eight to thirteen A4 pages per persona, not a “behave like” instruction.

> **in brief**
>
> - Eight to thirteen pages per persona instead of a single line of instruction
> - Without a detailed description the answers turn out noticeably more superficial
> - A moderator agent delegates, has relevance self-assessed from 0 to 1 and weights accordingly
> - Twenty personas need 20 to 30 minutes per run and deliver worse results
> - Three well-chosen, differing perspectives beat the full panel

## Why the effort pays off

The direct comparison is the interesting part. The same assignment without the detailed persona descriptions delivers markedly more superficial answers.

The presumption behind it, explicitly marked as a presumption in the episode: a language model needs a world model that is as concrete as possible in order to stay consistent in a role. Where that is missing, it falls back into its neutral default behaviour.

That matches what is described in other contexts as context engineering. A role is not an instruction but a frame of reference: which experiences shape the judgement, which priorities apply, what gets rejected and why. Without that frame, a role instruction remains a note on style.

> ### How the panel is built
>
> A **moderator agent** in the style of a senior consultant takes in the question and delegates it to the appropriate personas.
>
> Each persona provides a **self-assessment from 0 to 1** of how relevant it considers itself for this question. That is the cleverest part of the construction: instead of weighting all of them equally, a measure emerges of who has anything to contribute at all.
>
> The moderator then **weights** the answers along that assessment.
>
> Via a **Perplexity connection** the agents fetch current information from the net, so that a persona does not argue exclusively with training data from the day before yesterday.
>
> The self-assessment does, however, have the same weakness as any self-evaluation: a model asked about its own relevance tends towards agreement. Anyone rebuilding the setup should keep an eye on the values. If all of them sit above 0.8, the scale is measuring nothing.

## The finding on panel size

The practically most valuable insight of the episode is a reduction. Twenty personas at once are too many, both in terms of compute time, meaning 20 to 30 minutes per run, and in terms of susceptibility to errors.

Three well-chosen, differing perspectives deliver better results than an overcrowded panel.

That corresponds to the experience with human panels and has an additional technical cause here. The more contributions are merged, the more strongly the summary averages them out. Twenty voices produce an average, three produce a contradiction, and the contradiction is where the value sits.

What matters is therefore not the number but the difference. Three personas that all come from the same school of thought deliver the same answer three times.

## The self-experiment

Remarkably honest is the part in which the panel is set on one of the hosts himself, fed with references from previous employers and feedback conversations, in order to obtain an assessment for a board presentation.

That is the most obvious and at the same time the most delicate application. Anyone who feeds in assessments of themselves gets back an evaluation that inherits the blind spot of the original assessors. A reference describes how someone was seen, not how someone is.

For the intended purpose that is still enough, because a board presentation likewise lives on how someone is seen.

## The question of bias

The episode touches on a topic that reaches beyond the setup: how strongly do training data and vendor specifications shape a model's world view. Mentioned are the suspicion of bias in US models compared with Asian ones, and the well-known story that Grok is said to have been instructed not to criticise Elon Musk.

For an advisory board made of personas that is immediately relevant. If all the personas run on the same model, they share its basic outlook. The difference between them is then a difference in manner of speaking, not in judgement. Anyone who wants real diversity distributes the personas across different vendors.

## Conclusion

An advisory board made of personas is one of the few constructions where the effort can be evidenced: the comparison with and without a detailed description comes out unambiguously.

Three rules apply for rebuilding it. Write the personas out in detail, with background of experience and priorities, not as a note on style. Take three instead of twenty, and select them for difference. And distribute them across different models if real contradiction matters to you.

The episode's conclusion does not sound like an AI conclusion at first, and it lands: anyone who can deal well with people also copes better with the differing personalities of agents. Soft skills, long derided as the soft counterpart to IT competence, become a core competence in dealing with multi-agent systems.

> **The story continues …**
>
> The paper “Psychologically Enhanced AI Agents” gets a mention, and with it the question of whether diversity in an AI team delivers measurably better results. That is the study that would give this setup the empirical basis it so far lacks.

---

The full episode: [AI ADVISORY BOARD](https://think-ai.podigee.io/8-ai-advisory-board)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
