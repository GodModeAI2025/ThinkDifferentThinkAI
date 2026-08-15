---
folge: 41
titel: "Architecture decision records: the most important skill in vibe coding"
bildtitel: "Decisions in markdown"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/41-just-vibe-it"
---

# Architecture decision records: the most important skill in vibe coding

*An agent reports that all errors have been fixed. They have not. What helps is unspectacular: writing decisions down, in a format the machine can read for itself later.*

By Mark Zimmermann

Andrej Karpathy named vibe coding in February 2025: talking to the machine until runnable software comes out. Vibe engineering lays a layer of context and structure over it. The difference between the two decides whether anyone still understands after three weeks why the system looks the way it does.

The way into the episode is a case of things not working. Claude Code with an Opus model stubbornly refused to solve a specific problem. Only when Codex from OpenAI was hooked in as a reviewer via a plugin was it done.

> **in brief**
>
> - A second model as reviewer solves problems the first one gets stuck on
> - Architecture decision records belong in markdown, not in Word, so that a model can read them
> - “Are all the errors gone?” is reliably followed by a “yes” that is not true
> - A pre-mortem skill thinks the project backwards and finds what you otherwise think of too late
> - Rate limits are annoying and force breaks nobody takes voluntarily

## When two models are better than one

The case from the opening is more typical than it seems. A model that has proposed a solution sticks with that assumption. It checks its own approach against the same premises the approach came from, and consequently does not find the error.

A second model brings a different starting point. That is not a quality difference between the vendors but simply a second perspective.

In passing, the two untangle the naming situation, and it is genuinely confusing: at OpenAI, Codex is sometimes a model, sometimes an application, sometimes a mode, and to that come GPT-5.5, Amazon Bedrock, GitHub Copilot and Azure. Anyone keeping track here has been paying attention.

## The most important advice in the episode

Architecture decision records are the antidote to the main weakness of the method. They record which decision was taken, what alternatives there were and why the choice fell as it did.

The format is decisive: markdown, not Word. The reason is not taste. A model can read markdown later, check it for contradictions and find duplicates. A Word document with layout is dead weight for these purposes.

> ### What belongs in an ADR
>
> An architecture decision record is short, usually one page, and follows a fixed structure: **context** (what situation forces the decision), **decision** (what applies now), **status** (proposed, accepted, superseded) and **consequences** (what becomes easier as a result, what harder).
>
> The value sits in the consequences and in the rejected alternatives. Anyone wanting to know in six months whether a commitment still holds needs the reasoning and not the outcome. The outcome is in the code.
>
> In combination with agents a second benefit comes along. An agent that has the ADRs in context less often proposes something that runs against a commitment already made. Without these files, every session starts at zero, and you discuss the same question for the fourth time.

How far agents now go is shown by an anecdote from the weekend. After human and agent could not agree whether an error existed at all, the model requested screen sharing, keyboard access and accessibility permissions on the Mac and then clicked through the interface itself to find its own mistake. Impressive and uneasy at the same time.

On the other side stands Manus AI, with which an application with text recognition and Google Calendar sign-in was built in two prompts. Functional, but by both their assessments far from ready for release.

## Dealing with assurances

The practically most important warning concerns a phrasing everyone knows. To the question of whether all errors have been fixed follows a yes. Sometimes it is true. Sometimes the error was pushed off to another session.

That is not malice but a consequence of how these systems answer. They produce the most likely continuation, and the most likely continuation to a success question is a success report.

A pre-mortem skill serves as the antidote. It thinks a project backwards: it has failed, what was the cause. This reversal systematically surfaces what is otherwise thought of too late, for instance security, sign-in screens and consent.

The accompanying working rule is simple: at every “that is secure”, follow up critically two or three times until the model also names what it left out the first time. It usually does then.

## The addictive pull

An honest section is devoted to working hours. Vibe coding has addictive potential, because the feedback comes immediately and the next step always seems within reach.

Rate limits are annoying in this context and useful at the same time, because they force a break. Even the expensive Max plan has one. In one of the installations involved, the system even checks the time of day and sends the user to bed in the evening.

Connected to this is a second point that counts for organisations: not everyone needs the full chat window with all its power. Anyone building presentations all day does not need an open workbench but a solution tailored to the use case. For getting started, no-code and low-code tools such as Bolt or Lovable are suitable, where the method can be tried out safely.

## Conclusion

Vibe coding works, and it works worse than the first impression suggests. The difference lies not in the model but in three habits.

Write decisions down, in markdown, in ADR format. That costs ten minutes per decision and saves the discussion next time.

Have what you did not produce yourself checked, and by something other than the producer. A second model is enough.

And mistrust success reports. An “everything fixed” is a claim, not a test result.

Two examples from private life show at the end what the effort is worth: a Philips Hue motion sensor in the cellar got a function through conversation that the manufacturer does not provide, namely light that stays on when somebody walks past again during the wait period. And the podcast website with all transcripts in German and English came about the same way.

> **The story continues …**
>
> The question of the right tool kit per role remains open. Between full agent access and no access at all lies a broad field most organisations have not yet sorted out. Whoever sorts it decides how much shadow IT arises over the next few years.

---

The full episode: [Just vibe IT](https://think-ai.podigee.io/41-just-vibe-it)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
