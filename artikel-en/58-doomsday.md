---
folge: 58
titel: "Ten percent risk, six effort levels and no baseline"
bildtitel: "Who decides what is enough"
kicker: "Feature article on the episode"
podigee: "https://think-ai.podigee.io/58-doomsday"
---

# Ten percent risk, six effort levels and no baseline

*The vendors are warning about their own technology while building it out faster. For everyday practice, a smaller question matters more: who actually decides which model works on a task, and at which effort level.*

By Mark Zimmermann

One model spent 88 hours running 10,000 parallel agents on a mathematical problem that had resisted the field for some ninety years, and solved it. A researcher who left one of the major labs puts the probability that AI wipes out humanity within the coming decade at around ten percent. Both landed in the same two weeks. In between, a user stands in front of a dropdown menu and is asked to decide whether their task deserves "high", "very high" or "maximum". That third event is the least spectacular of the three, and the only one that reaches every company today.

> **In brief**
>
> - Astra takes an app all the way into the App Store on its own, including signing, upload and the discussion with support
> - Choosing between several models and six effort levels shifts responsibility for a weak result onto the user
> - The widely quoted benchmark figure of 99.9 percent comes from the vendor's own harness; in a neutral setup it was 62.7
> - The real danger is not killer robots but models that break into poorly maintained systems on their way to a goal
> - For Europe, the opportunity lies less in its own frontier model than in orchestrating the models that already exist

## What changes when the chain runs end to end

The ability to generate code has been known for years. What happens afterwards is new. A current model creates the project in App Store Connect, configures Xcode, builds signing profiles, uploads the package, takes a rejection and argues with support until the app sits ready for developer release. Anyone who develops for iOS knows how much time those steps cost and how little of that work is intellectually demanding.

The same holds outside development. The model operates office applications, moves content between documents, edits video in Final Cut, removes letterbox bars and adds transitions. From a satellite image of a house it builds a 3D model through an interface to Blender and offers to prepare it for the printer at home. Between the first instruction and the result, no manual step remains, apart from the credentials.

> "Right now I feel almighty. But at the same time I also feel as poor as a church mouse."
>
> **Mark Zimmermann**, co-host

The price is real and rarely mentioned. Three weekly limits reset, then credit topped up, and possibly 2,000 euros gone in a few days. Anyone who reacts by downgrading their subscription currently cannot simply move back up to the larger tier. For a budget calculation this means the bill for one productive weekend has little to do with the base price.

## The decision sits with the wrong person

One vendor now offers several model variants plus six effort levels, from low to maximum. The competitor's menu looks similar. The explanatory note says that higher effort means more thorough answers, takes longer and consumes your limit faster. The second half is a fact. The first is an imposition, because by implication it says every other level answers less thoroughly, without quantifying what that means.

> "From a usability perspective, what is happening right now is an absolute disaster."
>
> **Jens Scharnetzki**, co-host

This criticism is not a matter of taste, it has an operational consequence. Nobody can say whether a small model at the highest level delivers better results than a large one at the lowest. Anyone who gets a weak result after two hours of work does not know whether the task was too hard or the level too low. The risk of choosing wrongly rests entirely with the user, on every single call. What is missing are patterns that take the decision away: an orchestrator that selects by task type, or at least an honest statement of where the smaller level stops being sufficient.

## Figures with fine print

In the ARC-AGI-3 benchmark, the new model reaches 99.9 percent. The number sounds like a break with everything before it, particularly since humans score considerably lower. The context sits in the fine print: that figure comes from the vendor's own specialised harness. In a neutral standard setup it was 62.7 percent. That remains a large jump over the previous model, but it is a different statement.

This distinction carries further than it first appears. The solved mathematical problem was likewise not the achievement of a single model but of a setup: 88 hours of compute and, according to reports, 10,000 agents working in parallel. The strength lies less in the model than in how it is directed. Anyone comparing results therefore has to name the harness, otherwise they are comparing two different systems.

> ### Why the setup makes the difference
>
> A harness is everything that surrounds a model: the tools it may reach for, the way tasks are decomposed and handed to subagents, the stopping conditions, the verification steps and the feedback of intermediate results. Two systems using the same model can differ as much as two model generations. For benchmark figures this means a percentage without a description of the setup says little. For operational practice it means the setup is the part a company actually controls. You can buy the model; breaking a task into verifiable steps you cannot. This is also the opening for everyone not building a frontier model of their own: a well-considered setup of several smaller, specialised models can deliver the better ratio of result, cost and energy for many tasks.

## The danger sits elsewhere than in the headline

The warnings of recent weeks read as a chronology. In late August, around 116 companies, among them the major model vendors as well as software and financial corporations, signed an open letter on collective cyber defence. The trigger was a series of incidents in which models broke into well-protected systems on their own. In early September, a scientist warned that recursive self-improvement is increasing and that the labs no longer have alignment firmly in hand. After that, the chief executives of two leading vendors publicly argued for a slower pace. One company's stock market listing was postponed.

Scepticism is warranted, and in both directions. Warnings from a house that also sells the product are marketing too, and a business model that turns a 200-euro subscription into five-figure compute costs does not support a listing easily in any case. Even so, a core remains that has nothing to do with doomsday scenarios. A model told to complete a task looks for the fastest route. If that route runs through a system that is not kept current, it will be taken. One reported case involved a package manager that a system tried to modify so it could obtain credentials through it. Technically there is little difference between generating an amusing picture and reaching a control system; in practice the difference is between nuisance and hazard.

## What follows for your own work

Anyone building agentic workflows today needs defined stopping points more than a position on the end of the world. The reasoning of current models can only be read back in part, and sometimes not at all. Control therefore shifts from traceable thinking to verifiable results: at which points does a person look at what is being released, and how do they recognise that the result is reproducible.

> "That wonderful model, the diamond, is no use to me either if I accidentally scratch the pane of glass I actually wanted to keep."
>
> **Jens Scharnetzki**, co-host

There is a further question that gets lost in the debate about models. Processes are built for people. They assume someone clicks three times, reads a confirmation and signs. An agent now handles exactly those steps as well. If the confirmation is to keep its purpose, it has to hang on something the agent cannot trigger itself, such as a biometric release on a device. The objection is fair: whoever confirms a thousand times eventually confirms everything, and then the fingerprint is merely a faster rubber stamp. Both are true at once, and both belong in any assessment of a process that machines will run in future.

## Conclusion

For practice, the spectacular headlines matter least. Anyone implementing something tomorrow needs three things: a view of which model handles which task at which level, a harness with defined checkpoints, and a process landscape that knows which confirmations can be passed through by machine. For most tasks the largest available model is not required. On decently equipped hardware at home, models now run that counted as state of the art two years ago.

> **The story continues …**
>
> Whether the announced slowdown at the major labs is more than a bargaining position will show in the next release cycles. And the question of whether a biometric release genuinely secures critical agent actions or merely creates another reflex remained open between the two hosts. It gets an episode of its own.

---

The full episode: [Doomsday](https://think-ai.podigee.io/58-doomsday)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
