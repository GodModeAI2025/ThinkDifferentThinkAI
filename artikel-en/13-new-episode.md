---
folge: 13
titel: "The browser as an actor: what Atlas can do and why caution is warranted"
bildtitel: "The browser clicks by itself"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/13-new-episode"
---

# The browser as an actor: what Atlas can do and why caution is warranted

*Atlas clicks, fills in forms and posts on its own in Agent Mode. That is impressive, and it opens an attack route against which there is currently no robust defence.*

By Mark Zimmermann

The arc of this episode runs from an AOL advert featuring Boris Becker through to Atlas, the AI browser from OpenAI. The difference to everything before it: the browser is no longer a tool, it is an actor.

Among other things it was tried out for an automated LinkedIn post and for clearing out one's own inbox.

> **in brief**
>
> - Atlas works independently in Agent Mode: clicking, filling in forms, researching, posting
> - What is new is less the capability than the visibility of what happens on the page
> - Prompt injection via invisible text on web pages is the central attack route
> - Inbox access means, in practice, access to every password reset
> - More than half of all online content is now machine generated

## What is actually new about it

Summaries and sidebar interaction have long been on offer from Microsoft with Copilot in Edge, and Perplexity and Manus are experimenting with agentic browsing as well.

The difference with Atlas lies in the visibility. You see more directly what is currently happening on the page while tasks are being worked through in Agent Mode: price research, competitor comparisons, automated assessments of a website from the perspective of different user groups.

The last use case is the most useful in practice and is rarely mentioned. Having a website assessed from the perspective of different target groups replaces no user research, and it delivers a usable first pass for a fraction of the effort.

## The attack route

Things become critical when it comes to security, and fundamentally so.

> ### Why prompt injection weighs especially heavily in the browser
>
> A language model distinguishes only weakly between instruction and content. Both reach it as text.
>
> In the browser an agent reads pages that others have written. If text stands there that a human does not see, white on white for instance, in a hidden element or in an attribute, the agent reads it all the same. If that text contains an instruction, there is a possibility that it will follow it.
>
> The attacker needs no access to your computer for this. It is enough that they get you to visit their page.
>
> Effective countermeasures start outside the model: the agent may only act on selected pages, every action with an outward effect needs an approval, and the agent works with its own tightly permissioned access instead of with yours.
>
> An instruction in the system prompt not to follow instructions from web pages helps only to a limited degree. It sits in the same channel as the attack.

Access to your own inbox is particularly delicate. Whoever grants it grants, in practice, access to every password reset and thereby indirectly to all services that can be recovered via that inbox.

With online banking the same question arises even more sharply. The assessment in the episode is unambiguous: an exciting field that is to be treated with caution at present.

## The Habsburg effect

The second point of contention is a number: more than half of all online content is now machine generated, and the trend is rising.

From this follows a problem for which the episode picks the image of the Habsburg effect. When language models are increasingly trained on machine generated data, the gene pool narrows. Errors and idiosyncrasies reinforce themselves across generations instead of being balanced out by new sources.

For website operators an unfamiliar task follows from this: in future, content will have to be optimised not for humans alone, but also for the agents that read it. That concerns structure, unambiguous information and machine readable data, and it contradicts much of what has counted as good web design in recent years.

## Conclusion

Agentic browsing is the first application in which a model acts in the open web instead of in a controlled environment. That explains both the benefit and the risk.

Anyone who wants to deploy it clarifies three things beforehand. On which pages may the agent act and not merely read? With which access does it work, and is that an access of its own with narrow rights? And which actions require an explicit approval?

For the inbox, the bank and everything touching money or access, the usable answer at present is: no automatic actions. Reading yes, acting no.

That is not a rejection of the technology. It is the recognition that an attack route is open for which there is as yet no solution.

> **The story continues …**
>
> As a tool tip the episode presents WhisperFlow, a speech to text tool that transfers dictation directly into any text field. According to one observation quoted, some developer teams use it after a few months for around 75 per cent of their text input. The change of input channel proceeds more quietly than the change of model, and it alters the work at least as much.

---

The full episode: [THE BROWSER STRIKES BACK](https://think-ai.podigee.io/13-new-episode)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
