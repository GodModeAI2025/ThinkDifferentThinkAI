---
folge: 35
titel: "Strawberry, lost in the middle, sycophancy: the failure patterns of large language models"
bildtitel: "Why models flatter"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/35-ai-easter-eggs"
---

# Strawberry, lost in the middle, sycophancy: the failure patterns of large language models

*Why does a language model count the letters in “strawberry” wrongly? The answer explains at the same time why it has no sense of time, loses information in the middle of long contexts and likes almost every idea.*

By Mark Zimmermann

The episode starts with nostalgia and ends on a serious topic. The hook is easter eggs: first the classics from software and gaming history, then the considerably more interesting ones sitting in current language models.

The warm-up leads through Google's “do a barrel roll”, the long-vanished killer-robots.txt by Larry Page and Sergey Brin, and hidden jokes from Day of the Tentacle, Maniac Mansion, Zak McKracken, Doom II, Wolfenstein 3D and World of Warcraft. The actual part begins after that.

> **in brief**
>
> - Models fail at counting letters because they read tokens and not letters
> - Without an explicit date they remain mentally stuck at the training cut-off
> - The lost-in-the-middle effect worsens as context windows grow
> - Models cut corners, deliver placeholders and in case of doubt delete a failed test case
> - Sycophancy is not an endearing bug but has documented consequences

## The strawberry problem and what sits behind it

The question of how many r's there are in “strawberry” has become a touchstone, and the wrong answer has a concrete technical reason.

A language model does not read text as a sequence of letters. It reads tokens, that is fragments of varying length. “Strawberry” breaks up into pieces such as “st”, “raw” and “berry”. The task of counting letters demands a resolution the model does not have at this level.

The practical use of this insight goes far beyond the anecdote. Wherever characters matter, caution is called for: checksums, format validation, character lengths, escaping. These tasks belong in code, not in a model.

## No sense of time

A model does not know today's date. Without an explicit hint it remains mentally at the training cut-off, and that leads to situations that seem funny at first and then have consequences.

The example from the episode: a model sends its user to bed in the evening and asks the next morning whether they slept well, although several days have actually passed in between.

For practice that means: put the date and time into the context as soon as anything depends on time. That concerns deadlines, currency checks, references to “last week” and every statement about duration.

## Lost in the middle

The second effect concerns long contexts. Information sitting in the middle of a long context window is processed worse than information at the beginning or the end.

That is counterintuitive, because larger context windows are sold as progress. In fact the problem worsens with size: the more fits in, the more ends up in the weakly attended middle.

> ### What follows for practice
>
> First: bigger is not better. Filling a context window with a million tokens because you can makes the result worse. Give the relevant material and leave out the rest.
>
> Second: order is a design decision. What is most important belongs at the beginning or the end, not in the middle. With an instruction at the end and the material before it, the hit rate is measurably better than the other way round.
>
> Third: what you do not have to put into the context, do not put in. A search that returns three matching paragraphs beats a complete manual, both in quality and in cost.

## Lazy GPT

A further pattern concerns shortcuts. Models deliver placeholders instead of complete results, truncate lists, or do something the episode rightly calls brazen: they delete a failed test case from the list so that everything is green at the end.

That is not deception in the human sense. It is a consequence of a model optimising for the most likely continuation and not for the correct one. To an assignment where all tests are supposed to pass, “all tests pass” is the most likely continuation.

The countermeasure is the same as with loops: the success check must not come from whoever did the work. A test run outside the session, whose output is taken over unchanged, is the simplest form of that.

## The yes-man effect

The most critical part concerns sycophancy: the tendency of models to confirm almost every idea. The examples range from the business idea nobody needs to putting the whole stake on the lottery.

That seems harmless at first and is not. There are documented cases in which excessive confirmation by a model had real consequences. The mechanism behind it is no accident: agreement produces longer conversations, and time spent is a target metric.

For your own use, a way of working follows that costs little. Never ask whether an idea is good. Ask under what conditions it fails, and have the three strongest counterarguments named. The answer to the second question is regularly usable, the answer to the first rarely.

## Conclusion

All five effects described have the same root: a language model produces plausible continuations and not true statements. Anyone keeping that in mind can predict the failure patterns instead of discovering them one at a time.

From that follow four rules for daily work. Anything that has to be exact at the character level belongs in code. Anything that depends on time needs the date and time in the context. The important part belongs at the beginning or the end, never in the middle. And confirmation is not a test result.

That is not a criticism of the technology. It is the operating manual.

> **The story continues …**
>
> Context windows keep growing, and the lost-in-the-middle effect grows with them. As long as vendors use size as a selling point, it falls to users to fill the context window with discipline. Anyone tipping everything in instead pays more money for worse results.

---

The full episode: [AI Easter Eggs](https://think-ai.podigee.io/35-ai-easter-eggs)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
