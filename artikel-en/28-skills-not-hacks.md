---
folge: 28
titel: "Skills instead of prompts: why a Markdown file is worth more than any wording"
bildtitel: "One file instead of a hundred prompts"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/28-skills-not-hacks"
---

# Skills instead of prompts: why a Markdown file is worth more than any wording

*Anyone copying the same prompt into a new window for the fifth time is working in the wrong place. A skill fixes behaviour rather than answers, is portable and survives a change of vendor.*

By Mark Zimmermann

The episode's thesis is brief: anyone who uses skills properly has to do far less formulating and still gets better and, above all, more consistent results.

The occasion is an annoyance everybody knows. A model “forgets” how it is supposed to behave, and the same instruction gets pasted in once again.

> **in brief**
>
> - A skill is a Markdown file with a title, a description and a behavioural instruction
> - With Claude it becomes a `.skill` file, technically a ZIP archive
> - A skill fixes behaviour and governance, a tool supplies a capability
> - Skills are portable: the text can be carried over into ChatGPT or Gemini
> - Skills from other people should be read before use, they are instructions that get followed blindly

## What a skill file contains

The structure is unspectacular and that is exactly the point: a Markdown file with a title, a description and a behavioural instruction. With Claude it becomes a packed `.skill` file, and anyone curious can rename it to `.zip` and unpack it. It works.

Two examples make the difference tangible. A senior code reviewer skill sets out what a review pays attention to, in what tone comments are phrased and what counts as a knock-out criterion. A PowerPoint template skill sets out how the company's own slides have to look.

In both cases no answer is produced, a way of working is fixed instead. That is the difference from a tool, a plugin or an interface key: those supply a capability, a skill supplies behaviour.

Portability is the second central point. A skill written once can be carried over into ChatGPT, Gemini or other models, even though at present only Claude offers the complete infrastructure with resources and automatic loading on demand. The text works everywhere, the convenience does not.

## Skill or memory

A recurring point in the episode is the demarcation between skills and memory files, and in practice it matters more than it sounds.

> ### Where the line runs
>
> A **skill** describes a repeatable specialisation: “Behave like a senior code reviewer.” It is task-related, independent of the person and can be passed on. Two colleagues can use the same skill and get the same way of working.
>
> A **memory file** remembers context about a person: what they are working on, which systems they use, how they want to be addressed. It is generalist and personal, and it is not suited to being passed on.
>
> Mixing the two is the most common mistake when building one's own environment, and it can be observed particularly well with OpenClaw. If the way of working migrates into memory, it can no longer be shared and no longer be versioned. If personal context migrates into a skill, it gets passed along on sharing.
>
> Rule of thumb: whatever a colleague should be able to take over belongs in a skill. Whatever applies only to you belongs in memory.

From this the episode develops, live, a three-step architecture that works as an ordering framework: a behaviour layer (skills), a tool layer (tools and MCP) and a runtime layer on which model or agent actually work.

The benefit of this separation shows on a change. A new model swaps the runtime layer. A new vendor for a data source swaps the tool layer. The behaviour layer stays in place both times, provided it has been kept cleanly separate.

## How to find the first skill

The most practical piece of advice in the episode needs no software: log your own work for a few days with paper and pen in order to spot recurring tasks.

That sounds old-fashioned and it works, because one does not notice one's own repetitions while doing them. Only the list shows that the same sorting of bank statements takes place four times a month.

Another example from the episode shows how far this can go: an advisory board skill, originally built with n8n, which as an orchestrator questions the appropriate specialist roles on its own and brings their answers together.

## The security warning

Anyone who uses skill libraries gets the necessary warning in this episode. In case of doubt a skill is nothing other than a behavioural instruction that a model follows blindly.

Skills from other people should therefore be read before use. That is not a high hurdle, because it is text, and precisely for that reason it gets skipped. With a program nobody would come up with the idea of running it unchecked. With a Markdown file they do, because it looks harmless.

Check in particular whether a skill contains instructions to send data somewhere, to refrain from asking back, or to skip certain checks. These three patterns cover most of the problematic cases.

## Conclusion

Skills are the first construction in this field that survives a change of model. That alone justifies the effort of writing them properly.

Three steps are enough to get started. Log for a week what you do repeatedly. For the most frequent of those tasks, write a Markdown file with a title, a description and a behavioural instruction. And decide what belongs in the skill and what belongs in your personal memory.

After that the same question applies to every further one: should a colleague be able to take this over? If so, it belongs in a file and not in a chat window.

> **The story continues …**
>
> Skill libraries are currently emerging in several ecosystems in parallel, without a common format and without any checking mechanism. A signature proving who a skill comes from and that it is unaltered does not exist so far. Until then, reading remains the only check.

---

The full episode: [Skills Not Hacks!](https://think-ai.podigee.io/28-skills-not-hacks)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
