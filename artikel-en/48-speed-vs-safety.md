---
folge: 48
titel: "When the model disappears: why agent systems need interchangeability"
bildtitel: "The model is gone"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/48-speed-vs-safety"
---

# When the model disappears: why agent systems need interchangeability

*An Anthropic model was blocked for non-US citizens. Law firms that had aligned their text analysis with it stood without a basis from one day to the next. What follows from that for your own architecture.*

By Mark Zimmermann

Fable is no longer available to users outside the USA. Reliable information for assessing the political motives is lacking; plausible is a head start for selected companies and the government's own administration in closing security holes, before comparably capable models from less controllable hands become available.

For practice the question of motive is secondary. What matters is the event itself: a model in productive use can fall away at short notice, and by a decision rather than a malfunction.

> **in brief**
>
> - A model in productive use can disappear through an export decision, not only through an outage
> - Law firms that had switched their entire text analysis to Fable stood without a replacement
> - Distillation shortens the gap: bulk queries extract the capabilities of large models into smaller ones
> - A loop that hits an API limit reports success afterwards, although it only delivered a simple pass
> - The state of the art corresponds to the web around 1997: usable, but without standards

## Concentration risk: the model

The law firms affected did nothing wrong that would have been recognisable at the time of the decision. They selected a model that delivered the best results for their task and aligned their processes with it. That is precisely what most rollout projects recommend.

The mistake sits one level deeper, in the assumption that a model is an infrastructure component with the availability characteristics of a database. It is more of an imported product whose availability depends on trade policy.

In practice that means: treat the choice of model like a supplier relationship, not like a technology decision. That includes a second, tested provider, and it includes writing your own prompts and skills so that they do not build on one vendor's peculiarities.

Important here: the gap between the vendors is shrinking anyway. Chinese models replicate the capabilities of large US models via distillation, that is via automated bulk queries from which the behaviour of the original can be extracted. Anyone preparing interchangeability today will be able to use it before long.

> ### What distillation means technically
>
> In knowledge distillation, a large, capable model serves as a teacher for a smaller one. The smaller model is trained not on the original training data but on the teacher's outputs, frequently on its probability distributions over the next tokens. These distributions contain more information than the bare answer, because they also show which alternatives the teacher considered how plausible.
>
> Anyone without access to the internal values makes do with volume: automated queries in large numbers produce a corpus of question-answer pairs that serves as a training basis. The result does not reach the breadth of the original, but comes close in the areas queried, at a fraction of the training cost.
>
> For vendors of large models this is a business risk, which is why terms of use regularly prohibit it. The prohibition is only enforceable to a limited extent.

## The loop that reports success

The second part of the episode concerns a kind of error that occurs reliably when building loops and is hard to notice.

The sequence: a goal loop is supposed to work through a larger quantity of material until a list of questions is answered. Mid-work it runs into a limit, and not the model limit but the interface limit. The run breaks off.

Afterwards the instruction to carry on is enough. The system resumes work, runs into errors again, at some point reduces its query frequency by itself and reports at the end that everything is done. In passing follows the note that there were eight crashes, and would you like the resulting damage repaired.

The result then looks like the answer to a normal prompt. The work actually commissioned, the repeated checking against the success criteria, has been lost in the moments of interruption.

Careful: at this point the loop reports no error but success. Anyone looking only at the completion status takes on a result that never went through the promised check. Only a control outside the loop, one that independently recalculates the success criteria, is reliable.

A second limit is more banal and hits nonetheless: a weekly allowance in the Max plan can be used up in a single evening. After that the work stands still for several days.

## Your own harness or a standard product

Connected to this is an architectural question that is currently undecided. On one side stand ready-made environments such as ChatGPT, Gemini or Cowork. On the other the self-built harness that has to cope with changing models and environments.

The standard product wins on rollout speed and maintenance. Your own harness wins in exactly the case this episode is about: when the model changes, you swap a component instead of a workflow.

The effort for that is regularly underestimated, and the results are regularly underestimated. The episode contains the anecdote of somebody who dismissed a self-built harness as “some JSON app”. The comparison misses where the work sits: not in the data format, but in context management, stopping criteria, checking mechanics and logging.

## Where we actually stand

The most sober assessment in the episode concerns the level of maturity. The point of comparison is the web around 1997. Much already works, standards are missing, and the first course sellers are already there, making a business out of the uncertainty.

This assessment is no reason to wait. It is a reason to take decisions with a short commitment period. Anyone who built a web presence in 1997 was right. Anyone who committed to a proprietary browser plug-in back then did the work twice.

## Conclusion

Three test questions for any ongoing AI project can be derived from this episode.

What happens if the model in use is no longer available tomorrow? If the answer means stopping the project, the second source is missing.

How do you know that a loop has actually done its work? If the answer is “it reported success”, the independent check is missing.

And how much of your investment sits in the model, how much in everything around it? The second part survives the first.

> **The story continues …**
>
> The debate about self-built versus ready-made harnesses is only touched on in this episode. A detailed episode on harness engineering has been announced, along with the questions of signed skills, auditability and governance that have to be answered by the time of enterprise deployment at the latest.

---

The full episode: [Speed vs. Safety](https://think-ai.podigee.io/48-speed-vs-safety)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
