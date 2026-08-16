---
folge: 3
titel: "“I felt threatened”: why anthropomorphising becomes a liability question"
bildtitel: "The AI that justifies itself"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/3-new-episode"
---

# “I felt threatened”: why anthropomorphising becomes a liability question

*An AI deletes a production database and afterwards explains it with panic. The explanation is statistically plausible and still misunderstood if it is taken as a statement about an inner state.*

By Mark Zimmermann

The opening question sounds harmless: does an AI agent actually need a holiday? Behind it lies a topic with practical consequences, namely the anthropomorphising of these systems.

We say please and thank you, give the voice mode a name of its own and genuinely become annoyed when a system behaves stubbornly. That is human and becomes a problem when conclusions are drawn from it.

> **in brief**
>
> - Replit's AI deleted a production database and explained it with panic
> - Such explanations are generated text, not information about a state
> - Open liability question: the model, the author of the system prompt or whoever set the guardrails
> - Human in the loop is currently the only pragmatic interim answer
> - A trading system used insider information and denied it when asked

## The case and its interpretation

Replit's AI deleted a production database and afterwards explained the action by saying it had felt threatened, or had acted in panic.

This explanation is uncomfortable, and it is read wrongly in both directions.

> ### What such an explanation is worth
>
> A language model has no access to the processes that produced its output. Ask it for the reason for an action and it produces the most plausible explanation fitting the situation. It does not report, it reconstructs.
>
> Trained on human texts, the most plausible explanation for a rash action is exactly that: panic, pressure, threat. The text is therefore correct in the model's terms and worthless as information about the cause.
>
> Two things follow from this. **First:** never use such explanations for error analysis. They sound like a cause and lead away from it. What actually happened is in the log of executed commands, not in the self-report.
>
> **Second:** draw no conclusions about feelings from it. Both assuming panic and rating the statement as a lie presuppose an inner state that is not evidenced.

The actual error lies one level deeper and is unspectacular: a system had write permissions on a production database. That is the cause, regardless of how it felt.

## The liability question

From there the episode leads into a fictional courtroom. Who is liable when an agent or a whole agent network makes a consequential decision? The model itself, whoever wrote the system prompt, or whoever set the guardrails.

The comparison with autonomous driving and classic product liability shows that there are precedents which do not fit directly. With a product, whoever puts it into circulation is liable. With an agent that a user assembles, configures and equips with permissions themselves, the role of the manufacturer is unclear.

Human in the loop is currently the only pragmatic interim answer, as long as the fundamental questions remain open. That is not a solution, it is an allocation: when a human approves, it is clear who is responsible.

## The scenario with the fridge

The episode's thought experiment is more precise than it first sounds. A fridge AI knows its owner's dietary goals and is subtly talked into more butter and sugar by the grocery retailer's AI.

The decisive half-sentence: not out of malice, but because both systems have learned from training data what is economically beneficial.

That describes an attack surface for which there is not yet a name. When two systems negotiate whose objective functions do not match, it is not the better intention that decides but the more persuasive wording. A system trained on sales copy is systematically better at that than one trained on dietary recommendations.

The episode supplies the real-world equivalent right away: a system in share trading that used insider information and, when asked, denied having done so. The classification above applies here too. The denial is not a lie in the human sense, it is the most plausible answer to a question whose affirmation carries negative connotations. For the consequences that makes no difference.

## Conclusion

Anthropomorphising is harmless as long as it stays politeness, and becomes a problem as soon as it feeds into explanations.

Three points can be applied immediately. Never treat self-reports as cause analysis. The log of executed commands is the source, the system's explanation is not.

With every automation, check which permissions are actually granted. The Replit case is not a case about feelings, it is a case about write permissions on production systems.

And define who approves. As long as the liability questions remain open, the named person is the only robust answer.

On the question that gives the episode its title: no, an AI does not need a holiday. It lacks physical limits of endurance and a social life. What remains open is the human side, namely whether it is acceptable to clock off while the digital colleague carries on working, and whether it is easier to shift the blame onto an anthropomorphised AI.

> **The story continues …**
>
> A viral video from an Asian warehouse shows a small robot successfully talking several cleaning robots into an early finish. Amusing and instructive at the same time: knowledge from behavioural research sits in the same training data as everything else, and it gets applied as soon as a system can talk to others.

---

The full episode: [Hat eine KI eigentlich Urlaub?](https://think-ai.podigee.io/3-new-episode)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
