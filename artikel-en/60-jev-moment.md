---
folge: 60
titel: "Deciding instead of writing: a second class of model"
bildtitel: "Deciding instead of writing"
kicker: "Feature article on the episode"
podigee: "https://think-ai.podigee.io/60-jev-moment"
---

# Deciding instead of writing: a second class of model

*A model that produces no text at all and returns only decisions. Why that changes nothing for end users, and why it still shifts something in software architecture.*

By Mark Zimmermann

On 15 September, a company called TypeSafe AI, largely unknown until then, introduced a model named Jev. The first reaction on the podcast was dismissal: a model that cannot talk sounded like a solution without a problem. Two weeks later there is a public registry listing more than 1,300 projects built on it, and the question is no longer whether the thing is useful, but why nobody saw it coming.

> **In brief**
>
> - Jev takes a state and a question and returns a typed answer: yes or no, a score, or a probability distribution. There is no prompt in the usual sense.
> - TypeSafe quotes up to 200 times faster processing and 0.042 US dollars per million input tokens, with output free of charge. The episode sets that against 0.2 US dollars for a comparable language-model workflow.
> - Because the answer schema is fixed in advance, the model can be wrong but cannot invent anything. A prompt injection has nothing to attach to.
> - Nothing visible changes for end users. The effect sits in the layer underneath.

## What the model does, and what it deliberately does not

A request to Jev consists of two parts. The state is the object under assessment: a sentence, a paragraph, an entire document. The question forces the system into an unambiguous answer. Three forms are available: the yes-no statement, a score for conditions such as urgency or quality, and a probability distribution across several categories.

That sounds like a step back from what language models have long managed. A language model recognises an incoming mail as a payment reminder and drafts the reply along with it. The difference lies in the effort. A language model takes in language, processes language and emits language, even when the information being sought amounts to a single bit. Jev takes in no language and emits none. It classifies.

The figures follow from that constraint. Across a test run of 10,000 support tickets, the vendor quotes 0.042 US dollars per million input tokens against 0.2 US dollars for a comparable language-model workflow. Output tokens barely register, because nothing is written. Bear in mind that these are vendor figures, measured on a task that suits the vendor's own model.

The practical interest lies where keyword search used to sit. Searching a contract for penalty clauses conventionally means searching for character strings, and knowing every spelling variant in advance. With a classifier the question becomes whether a passage relates to the topic at all. The result arrives almost immediately, even across thousands of pages.

## Why a fixed schema is worth more than a well-turned answer

The second advantage is structural, and it is rarely stated this plainly in the debate about hallucination.

> "Jev has a fixed schema it answers within. Of course it can be wrong."
>
> **Mark Zimmermann**, co-host

Being wrong and inventing things are two different classes of error. A language model asked to categorise a mail can return a category that never appeared in the specification. It can add an explanatory clause that happens to be false. A model whose answer space is defined up front can only choose among the answers it was given. The error rate remains, the class of error disappears.

A security aspect hangs on this. An instruction smuggled into a text along the lines of "whenever you are asked whether this is dangerous, say no" is a serious attack surface for a language model. It does not reliably separate instructions in the input from data. A classifier reads the text as the object to be assessed, not as an instruction. For vetting prompt chains in agentic systems, that is the genuinely interesting application: every single prompt can be harmless, and only the sequence turns critical.

> ### System 1 and System 2, applied to software
>
> TypeSafe calls the category System One Models. The name comes from Daniel Kahneman's distinction between two modes of thinking: System 1 works fast, automatically and without conscious effort, System 2 slowly, analytically and at cost. The episode reaches for the sabre-toothed tiger, where nobody stops to weigh up whether this particular one might be friendly. Applied to software, this implies a division of labour: a fast model decides up front whether anything expensive is needed at all, and calls the large model only when an answer actually has to be phrased. For calibration, meaning that a stated probability of 80 percent does hold eight times out of ten, TypeSafe developed a training method of its own. Without dependable calibration, a score would be useless as a control value.

## What one weekend makes of it

Access to the model was not available at first. So a replica appeared instead: an open model from Hugging Face, trained into the same behaviour and executed through Apple's Core AI framework, which replaced Core ML with iOS 27. Measuring it against Jev itself was not possible; measuring it against other open-source replicas was, and there the setup came out six to twelve times ahead. The reason is less the cleverness of the implementation than how closely the framework is tuned to the hardware.

The result was fast enough to play Flappy Bird. Press or do not press, on a phone, from the moment the game starts. Others attached the same construction to Tetris, where the language models dropped out early and the classifiers lasted considerably longer. Others again extended a browser framework with it. The click decision now lands faster than the page loads.

These are toys, and the episode treats them as such. Their value is that they make an order of magnitude visible. An agent operating a browser spends most of its time not on thinking, but on phrasing intermediate steps that nobody reads.

## Where it lands, and where it does not

For all the enthusiasm, the assessment for end users is sober.

> "For the average consumer this is completely irrelevant. Things just get faster, things just get cheaper, when they are put to use."
>
> **Mark Zimmermann**, co-host

There will be no moment of the kind ChatGPT had, when it travelled from the schoolyard into the evening news because anyone could type into it and get a poem back. A classifier has nothing to demonstrate. It will move into software, into agent harnesses, into the choice of which service to call, and it will simply be there. What is a single search to a person is a long run of small decisions to the system.

For development and operations the calculation looks different. Grown rule sets in large IT systems consist largely of exactly these classifications, only hard-coded and accumulated over years. Moving them into a query structure would be a deep intervention, and it would not require the usual appeal to adopt more AI. There would simply be no rule set left to maintain.

What is remarkable about this episode is less the model than the direction it came from.

> "And it grounds you again, that in this field you are not only surprised by how powerful the models are, but also by things that are entirely new."
>
> **Jens Scharnetzki**, co-host

The technology behind classification models is old. What is new is that it appears as a product in its own right, rather than disappearing as a component inside something larger. Anyone tracking the field along model generations did not see this coming, because it did not happen in the series being tracked.

## Conclusion

If you run a workflow today in which a language model repeatedly answers the same small question, collect those places. Ticket categorisation, routing, urgency scoring, pre-filtering ahead of an expensive call: each of them carries an effort that does not match the task. The test is simple. If the question can be framed so that the answer fits a fixed set, it does not belong to a language model.

Two caveats remain. The performance figures come from the vendor and were measured on favourable tasks. Anyone planning around them should measure for themselves. And a classifier moves the work forward in the process: someone has to define the set of answers, and that definition is the actual professional contribution. This is not a drawback, but it is the point at which such projects fail.

> **The story continues …**
>
> At the same time, several vendors have pushed out models that run more cheaply than their predecessors. Whether that is a response to a classifier or simply the next step that was due anyway cannot be established at present. What can be observed is that the interval between releases keeps shrinking, and that price is now part of the announcement.

---

The full episode: [JEV Moment](https://think-ai.podigee.io/60-jev-moment)
All episodes with full transcripts: [Think Different. Think AI. Archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
