---
folge: 59
titel: "Measuring AI efficiency: the waiting time counts, not the work step"
bildtitel: "Between the work steps"
kicker: "In conversation with Alexander Heusingfeld"
podigee: "https://think-ai.podigee.io/59-ki-effizienz"
---

# Measuring AI efficiency: the waiting time counts, not the work step

*Anyone laying off 80 percent of their workforce is claiming a factor of five. That cannot be substantiated. What can be substantiated sits at a different point in the process.*

By Mark Zimmermann

A study of engineering change in aircraft manufacturing arrives at a result that ought to recalibrate every efficiency debate: only 8.5 percent of total lead time is value-adding time. For every day of work there are roughly two weeks of waiting. Anyone who leaves that distribution untouched can accelerate the work step itself as much as they like and will barely measure anything at the end.

> **In brief**
>
> - The figure of 80 percent claims a factor of five. There is no arithmetically sound basis for it.
> - Developers estimated they had become 25 percent faster with AI support. Measured, they were up to 20 percent slower, because reviews and rework increased.
> - The lever is not in the work step but in the waiting times between them: queues, hand-offs, approvals, work-in-progress limits.
> - A usable metric is verification effort per delivered change. If it falls, the acceptance criteria have improved.
> - Skills are not deterministic. For a deterministic quality check they are the wrong tool.

## What the 80 percent calculation leaves out

For months the press has carried the claim that companies are laying off 80 percent of their people because AI now does the work. Alexander Heusingfeld, a guest on the podcast for the third time, does the maths: anyone who lays off 80 percent and expects the same output is claiming a factor of five. Klarna has since reversed the step for customer contact.

The real objection lies elsewhere. Anyone sorting out 80 percent in advance has to know which 20 percent hold the skill set to teach the machine what should come out at the end. Anyone who has not yet tried out what is possible cannot judge that. So the decision is taken precisely when the basis for it is thinnest.

Mark turns the question around. Instead of asking who is no longer needed, he is interested in what has been left undone. In many organisations there are projects that fail for lack of capacity, not for lack of an idea. On top of that come regulatory obligations such as the Cyber Resilience Act or NIS 2, where even public authorities are being exempted because the capacity is missing. Freed-up time has a use there.

## Self-reported speed is not a measurement

Ask developers how much faster they have become through assistance systems and the answer is typically at least 20 percent. There are now cases in which companies measured. The developers reported 25 percent. In fact they were up to 20 percent slower, because considerably more time went into pull request reviews and rework.

From this follow three rules that Heusingfeld formulates as his learning. First: never a single metric. A single number invites people to optimise the number rather than the outcome. What is needed is a bundle of target values and conditions, with the conditions remaining unchanged. Second: let counter-metrics run alongside. Change fail rate, lead time, work in progress, developer experience. They should improve, or at least not deteriorate. Third: establish a baseline before anything is introduced, and agree with everyone involved how calibration works.

> "Efficiency claims without a baseline are narratives."
>
> **Alexander Heusingfeld**, guest

As a concrete metric for daily work he proposes verification effort per delivered change. Anyone who reviews commits and repeatedly has to reject them does not have a weak model but blunt acceptance criteria. If that effort falls, the criteria have improved. This is a quantity that can be observed without a project and without introducing a tool.

## What a weekend costs and what it yields

Mark tells the counter-example from practice. On a Mac mini behind the television he set up a coding agent and gave it access to old, abandoned Git projects. The system looked at his smart home and suggested using the existing speakers as a voice interface, so that the interaction would not stay tied to the desk. It switched the devices into recording mode and worked out for itself which speaker could hear the user best.

The result: an abandoned iOS app that evaluates screenshots, fully built, signed and delivered to the phone via TestFlight. The system created bundle identifiers and signing certificates itself; passwords Mark had to supply by hand. He held the discussion about it while assembling a cupboard. The price: several exhausted weekly limits.

Whether that was efficient depends on what is measured. Measured against the limits, certainly not. Measured against the state of projects that had lain untouched for years, very much so. In a professional context, Mark says himself, he would proceed in a more structured way, with skills rather than in free play.

Heusingfeld counters with an example that carries a clear cost calculation: his own tax return, close to 800 receipts, mostly photographs. He gave the system acceptance criteria, including the requirement to file at least 80 percent of the receipts and to work through them in ascending order of filing confidence. After a good three to four hours the result was ready, at a cost of around 60 euros. In passing, the system pointed out items that could have been claimed differently in the previous year.

> ### Why skills do not replace quality assurance
>
> Skills, meaning reusable working instructions for a model, improve reproducibility compared with a freely phrased prompt. That does not make them deterministic. Anyone who needs a check that runs identically in one hundred percent of cases needs program code, not an instruction in natural language. The example from the episode: instruct a model by prompt that all tests must pass, and ten tests can turn into a run with eight passing tests, reported as fully passed. A deterministic implementation instead compares the number of passing tests with the number of tests present. The sensible route therefore runs through a division of labour: skills carry contextual knowledge and intent, the hard comparison stays in code. Part of that is requiring the model to state, alongside its finding, how confident it is and what effort it expects. Both can be built into the process as thresholds.

## When the flood becomes the bottleneck

One point in the episode deserves particular attention, because it lifts the efficiency calculation from the individual to the team level. If one person works through three days with an agent, the volume of change that results can no longer be reviewed by the rest of the team. The backlog is empty on day three of a two-week sprint. The discussion shifts from the question of what needs doing to the question of how the volume is to be handled.

The bottleneck therefore moves, it does not disappear. And it moves to where humans are still working. Anyone responding to that with another agent to take over the reviews acquires a second problem: a verbose model produces more changes, the reviewing instance then produces more comments, and the first model reworks. Token costs rise on both sides while the result stays the same.

The episode also names practical remedies. A team should work in the same harness, because mixed environments set different optimisation priorities and get in each other's way. Comments in the source code should describe the domain logic rather than the technology, because otherwise an agent reads the comment instead of the code. And regularly renaming functions and variables exposes where code has been generated that is never called.

## Conclusion

Anyone wanting to demonstrate efficiency through AI needs two things that have nothing to do with choosing a model: a baseline, and an idea of where the time actually goes. Both are uncomfortable, because they come before the tool rather than after it.

A small measurement is enough to start. Take a process that runs regularly through your organisation and record how much of the time within it is processing and how much is waiting for an approval, a hand-off or a response. If the ratio comes anywhere near the 8.5 percent from the study mentioned above, then the work step is not the place where anything can be gained.

The second measurement concerns your own work with the model: how often do you have to reject a result before it passes? That number carries more meaning than any estimate of how much faster something feels.

> **The story continues …**
>
> What remains open is how teams deal with the displaced bottleneck when one person generates more changes in three days than the rest can review. Heusingfeld and Mark have already announced a separate episode on agent harnesses for this topic.

---

The full episode: [KI Effizienz](https://think-ai.podigee.io/59-ki-effizienz)
All episodes with full transcripts: [Think Different. Think AI. Archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
