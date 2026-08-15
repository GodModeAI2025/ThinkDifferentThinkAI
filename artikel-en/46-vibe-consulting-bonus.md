---
folge: 46
titel: "Vibe coding meets specification: where the shortcut in software development ends"
bildtitel: "The prompt is the specification"
kicker: "Live from adesso Digital Day"
podigee: "https://think-ai.podigee.io/46-vibe-consulting-bonus"
---

# Vibe coding meets specification: where the shortcut in software development ends

*Applications seem to appear on request. Prof Dr Volker Gruhn and Stephan Kempf explain why that is enough for toy apps and not for an ERP system, and where the actual work has moved to.*

By Mark Zimmermann

This double episode was recorded live from adesso Digital Day 2026, with two guests who look at the same question from different directions. Prof Dr Volker Gruhn is chairman of the supervisory board of adesso SE and teaches software engineering at the University of Duisburg-Essen. Stephan Kempf works at adesso mobile solutions on mobile, on-device AI and agent harnessing and is co-author of “Corporate LLM”.

The question is: what happens to software development, consulting and make-or-buy decisions when applications come about by prompt.

> **in brief**
>
> - Vibe coding carries for toy applications and does not carry for production-ready systems
> - The bottleneck is not the code but the specification
> - Natural language becomes a specification language, with all its ambiguities
> - Architecture and requirements engineering gain weight instead of disappearing
> - The model deployed is largely interchangeable, the harness is not

## The dotcom parallel

Gruhn places the current mood historically, and the comparison lands.

> “When the internet came up: whether you are a baker or a butcher, today you are a perfect website writer.”
>
> **Prof Dr Volker Gruhn**, chairman of the supervisory board of adesso SE

Back then a training course in HTML was enough to call yourself a web developer. Some of the pages that came about worked, a larger share was unmaintainable after two years. The difference between the two was rarely visible in the result, only at the first larger change.

Exactly that is repeating itself. Vibe coding produces runnable applications, and for a narrowly defined purpose that is a genuine acceleration. The break comes later: at the second requirement, at the data protection concept, at the question of what happens when two users write at the same time.

## Where the bottleneck really sits

The central sentence of the episode concerns the condition under which the shortcut works: a prompt only carries if it amounts to a complete specification of the software system.

The work has therefore not disappeared but moved. Anyone unable to formulate what they need, which cases occur and how fulfilment is recognised will not get a viable solution from a model either. At this point natural language becomes a specification language, and it brings along its known weakness: it is ambiguous, and ambiguity does not become visible to a model as a question but as a decision.

> ### Why specification is the harder discipline
>
> A specification describes not how a system is built but what it has to achieve and under what conditions. That includes functional requirements, non-functional requirements such as response times or availability, edge cases and explicit non-goals.
>
> The effort sits in the edge cases. What happens if a booking is aborted midway, how does the system behave with contradictory master data, which permissions apply to deputies. An experienced developer asks these questions in conversation, because they know the failure patterns. A model asks them only when prompted to, and otherwise answers them itself.
>
> Requirements engineering was long regarded as an administrative discipline and is currently gaining importance, because it has become the actual input.

Software architecture likewise does not lose weight in this. It decides whether a system can be replaced in parts, whether responsibilities are separated and whether a change in one place does not have consequences in three others. A model optimises for the task set, not for the one after next.

## Make-or-buy shifts

For consulting decisions the calculation changes. If creation becomes cheaper, the line between standard product and in-house development moves.

The argument cuts both ways, however. Building it yourself becomes more attractive because the initial effort falls. At the same time the operating phase gains importance, and that does not become cheaper. Anyone justifying an in-house development on creation costs alone is leaving out the more expensive part.

A simple separation works in practice: what makes the business distinguishable belongs in house, because that is where the specification sits. What everyone does the same way you buy, because nobody gains an advantage there from their own solution.

## The model is interchangeable, the harness is not

The term agent harness is barely known in the audience, and the panel explicitly pauses in the conversation to explain it. That is telling for the state of the debate: a lot is said about models, little about the environment in which they work.

Kempf's conclusion is the practically most valuable statement of the episode. The AI model deployed is in the end almost interchangeable; what matters is how robustly the harness around it is built.

That matches what operators report. A model change costs a regression round if skills, context management and checking mechanics are cleanly separated. It costs a project if the workflow and the vendor's peculiarities are interwoven.

For assessing an offer, a usable test question follows: how much of the effort sits in things that survive a model change. If the emphasis is on well-thought-out skills, test cases and context handling, the investment is long-lived. If it is on finely polished prompts for a particular model, it is not.

## Conclusion

Vibe coding is a genuine advance and a dangerous narrative at the same time. The advance lies in ideas becoming runnable faster. The danger lies in concluding that software development is thereby taken care of.

What has actually happened: the coding effort has fallen, the specification effort has not. Anyone who was previously good at describing what is needed gains substantially. Anyone who never learned that now produces, faster, systems nobody can maintain.

The advice from the two guests is accordingly unspectacular and correct: take skills seriously and build yourself a stable harness. The model underneath will change anyway.

> **The story continues …**
>
> The question of whether agents should describe requirements themselves in future remains open. Technically that already works, and a model does ask the right questions when following up. What is unresolved is who is accountable for the specification that results, when it later forms the basis of an acceptance.

---

The full episode: [Vibe Consulting & Bonus](https://think-ai.podigee.io/46-vibe-consulting-bonus)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
