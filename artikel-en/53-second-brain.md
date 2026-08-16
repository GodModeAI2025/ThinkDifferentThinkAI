---
folge: 53
titel: "Curation is the expensive part: what a second brain actually delivers"
bildtitel: "Curation is the expensive part"
kicker: "In conversation with Cornelius Illi"
podigee: "https://think-ai.podigee.io/53-second-brain"
---

# Curation is the expensive part: what a second brain actually delivers

*130 sources deliver 400 to 500 items a week, automatically rated and boiled down to a third. The most honest sentence of the episode: the digest still does not get read.*

By Mark Zimmermann

Cornelius Illi is product cluster lead for innovation and GenAI and runs one of the most thought-through knowledge setups presented on this podcast so far. 130 sources come in automatically, are ranked and rated, and at most a third makes it into the weekly digest.

And then he says the sentence that carries the episode: he no longer reads that digest himself.

> **in brief**
>
> - The concept comes from Tiago Forte; CODE stands for capture, organise, distill, express
> - What is new is the reinterpretation: the store is not meant for the human but as context for the AI
> - 130 sources, 400 to 500 items a week, of which at most a third makes the digest
> - What the AI does not deliver are best current practices, that is what works in this exact model version
> - Sharing fails on the terminology: whoever did not build the system does not know what to search for

## What a second brain is, and what is new about it

The concept is older than the debate about language models. Tiago Forte coined it with the CODE method: capture, organise, distill, express. Bring everything in, order it, distill the meaning out of it, and build something with it in the end.

What is new is a reinterpretation. After Andrej Karpathy presented his LLM wiki approach at the start of the year, many noticed that such a store may not be intended for the human at all. It is the context store for the machine.

That sounds like a nuance and changes the requirements entirely. A store for humans needs an overview, a structure and a way in. A store for a model needs verifiability, unambiguous terms and a format that translates economically into tokens. One is a shelf, the other a reference work.

## The numbers and what they cost

Cornelius has automated the first letter of CODE. 130 sources deliver 400 to 500 items a week. These are ranked and rated, at most a third ends up in the digest, the rest is dropped, either as irrelevant or as mere repackaging of other people's content.

He even retrieves his own LinkedIn likes, via an application he wrote himself and the data subject rights he is entitled to as an EU citizen. That is the practical use of the General Data Protection Regulation that is rarely discussed: it is also a tool for getting at your own data.

Note what has been automated here and what has not. The collecting runs by itself. The rating runs by itself. What comes after that does not run by itself, and the whole episode hangs on precisely that.

## Why the digest goes unread

The most honest moment of the episode is an admission. Cornelius no longer reads his own digest. Too much, and it does not stop at reading: afterwards you have to discuss it with the AI to arrive at any insight at all.

His finding is the most valuable part of the conversation. Curation is the genuinely difficult part, and the human will be needed in it for a long while yet.

The reasoning for it is precise. An AI can explain what harness engineering is and who coined the term. What it does not deliver are best current practices, that is the answer to the question of what actually works right now in this exact combination of model version and harness. That knowledge is a few weeks old, appears in no training set and can only be drawn from practice.

Where automation does achieve something a human cannot: in uncovering your own bias. Cornelius considered the LLM wiki topic huge and had to establish from the analysis that in a hundred days only 23 out of 5,000 items dealt with it. A niche topic that felt large in his own head.

That is an argument for measurement that reaches beyond knowledge management. What you encounter often, you take to be frequent. A count corrects that, and nothing else does.

## Two routes, one goal

On tooling the three diverge, and the disagreement is instructive, because both sides are right.

One route does without a vault.

> “Knowledge in systems like these arises through reduction, through structure, through the system being able to forget as well, and not merely through amassing as many documents as possible in as unstructured a way as possible.”
>
> **Mark Zimmermann**, co-host

Concretely that means: a single skill instead of a second brain. In it, ten years of Apple developer documentation, WWDC transcripts and the author's own technical articles. A few megabytes zipped, a few hundred unzipped, response time around two minutes. Not a RAG, not perfect, but portable and runnable in any harness, whether Codex, Claude Code or the company's own system.

> ### SkillSafe: a knowledge vault as a portable skill
>
> The setup is called SkillSafe and is publicly viewable. It answers a question classic vector databases leave open: where does a statement come from.
>
> Knowledge blocks sit in the Open Knowledge Format, and every core statement carries a source and a location. Instead of a vector black box, controlled vocabularies with synonyms are used, that is a maintained list of what the same thing can be called.
>
> To that come six iron rules, of which the first is the most important: if the holdings do not cover a question, the answer is “not in the holdings”. Model knowledge never fills the gap.
>
> That is the reversal of the usual behaviour. A language model answers plausibly in case of doubt. A knowledge system has to stay silent in case of doubt, otherwise nobody knows any more what is evidenced and what was added.

The other route needs the picture. More than 20,000 documents sit in Jens's vault. Searching for a single markdown file on purpose is laborious, but the view of the graph gives a feel for the weighting. If it looked wrong at the weekend, new logic runs over it.

The vault sits deliberately locally on a Mac Mini, with locally running Gemma models that archive and forget, an advisory board of the authors he follows most, and a guard that checks what may leave the vault for a public interface at all.

This guard is the part most setups forget. A knowledge store containing everything you know is risky for exactly that reason: with every request to an external model, it is decided which extract of it leaves the house.

## The actual problem with sharing

Because a lot of terminology goes over the airwaves in this episode, Cornelius translates two of them into plain language. A RAG, retrieval augmented generation, breaks texts into chunks, converts them into embeddings and arranges them in a high-dimensional space in which proximity means meaning. The classic example: king minus man plus woman gives queen. An ontology comes from graph theory, nodes and edges, and describes how terms relate so that paths can be followed along them.

Why that counts in practice shows up when sharing. Whoever built a knowledge system themselves knows the terms in it. Whoever inherits it cannot search for them, because the keyword is missing. A grep does not help then, and a brute force search over 200 hits knows no relevance weighting.

For companies that is the decisive point. A single source of truth for policies, FAQs, org charts, architecture documentation and contracts rarely fails on the technology. It fails because nobody knows the terms things were filed under. Anyone building such a thing builds the vocabulary first and the store afterwards.

## Conclusion

The episode delivers two recommendations for getting started, and they contradict each other only in appearance.

The first: start with skills. Do not build the monster, but work out for a concrete task which information a skill needs and how it has to be structured. A skill plus a few files in the project folder is already a small second brain.

The second shifts the perspective: away from “what else might I want to know” towards “what am I working on right now and what do I want to achieve”. Then it often takes less knowledge than expected, but a targeted search, and the store grows by itself.

To that a consolation for anyone hoping for completeness.

> “Curation cannot be outsourced entirely, and I think that will be the job, that we go in there and do a lot. If I save 90 per cent of the time spent and it gets 30 per cent wrong, I still have a large benefit.”
>
> **Cornelius Illi**, product cluster lead for innovation and GenAI

And an observation worth thinking about: we have models that generate video, and we store our knowledge in plain text files. That is not a step backwards but the realisation that format and value have little to do with each other.

> **The story continues …**
>
> Two questions are explicitly left lying in this episode: enterprise brains and the question of how a thousand second brains talk to each other. Both become interesting as soon as more than one person accesses the same store, and the invitation to a second episode with Cornelius Illi already stands for that.

---

The full episode: [Second Brain](https://think-ai.podigee.io/53-second-brain)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
