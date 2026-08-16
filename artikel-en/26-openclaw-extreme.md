---
folge: 26
titel: "98 per cent success rate: why an autonomous assistant is hard to secure"
bildtitel: "One email, an empty inbox"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/26-openclaw-extreme"
---

# 98 per cent success rate: why an autonomous assistant is hard to secure

*A faked security warning by email is enough for OpenClaw to empty the entire inbox. A test report puts the success rate for known prompt injection attacks at 98 per cent. What that means for putting it to work.*

By Mark Zimmermann

The child has a new name yet again. Clawdbot first became Moldbot, and now the little space lobster is called OpenClaw. The open-source software is installed on a Mac Mini, connected to an Opus model, operated through Telegram, complete with curious teething problems such as an accidental Google login by way of the browser cache.

The focus of the episode nevertheless is not on the setup but on security.

> **in brief**
>
> - A test report puts the success rate for known prompt injection attacks at 98 per cent
> - A faked security warning was enough for the agent to empty an inbox
> - OpenClaw works through a heartbeat instead of fixed procedures and invents its route to a solution afresh every time
> - Around half of the skills in the official hub were regarded as contaminated
> - Experiments belong in an isolated environment, not on the family computer

## Why helpfulness of all things is the problem

The numbers are clear. A test report shows a success rate of 98 per cent for known prompt injection attacks. An experiment shows that a single faked security-warning email is enough for the agent to empty the entire inbox.

The reason lies in the design. An assistant trained heavily towards helpfulness treats an urgently worded request as what it purports to be. This is the grandparent scam, only against a machine instead of against a person, and the machine has not learned mistrust.

Note that this cannot be remedied by better wording in the system prompt. The attacker writes into the same channel as the operator, and to the model both look the same. Only restrictions outside the text are effective: which tools the agent is allowed to call at all, and which actions require human approval.

## Heartbeat instead of procedure

Technically OpenClaw differs fundamentally from tools such as Claude Code. Instead of a fixed, deterministic procedure it works through a heartbeat: an adjustable interval in which the agent independently checks memory and task list for anything that needs doing, and invents the route to a solution afresh every time.

That produces genuine surprises. In the episode the agent installs a faster model on its own authority, because that way it went faster. And it produces costs: a system busily working away can end up in the three-digit euro range without anyone having commissioned anything.

> ### What a heartbeat means for securing the system
>
> A fixed procedure can be audited. It can be read, tested, and for every step it can be laid down what is permitted. A heartbeat agent does not have this procedure, because it forms it anew every time.
>
> Three requirements follow from this that have to be settled before going live. **First a cost limit**, hard and enforced outside the agent, because no daily amount is predictable. **Second a permissions list** that is narrow and expressly does not contain what would occasionally be useful. **Third a log** that records what the agent has done, and does so where the agent cannot change it.
>
> Without these three points, what is being run is not an autonomous system but a random experiment with system access.

## The culture around it

Culturally the remarkable part is the one about the community. With Moldbook it has built its own social network for bots, in which agents exchange knowledge, marry each other or open a shop. A mixture of genuine bot interactions and fakes instructed by humans.

Added to that are first approaches such as Rent-a-Human, in which an agent passes tasks on to real people through MCP tools when it cannot get any further itself. That sounds like a curiosity and describes a division of labour that will probably stay.

## The warning that counts

The most serious point of the episode concerns the skill library. Around half of the skills in the official hub were regarded as contaminated at that time and were loading malware in the background.

The recommendation is correspondingly unambiguous: experiments belong in an isolated environment. A separate computer without production data, a dedicated virtual server or a container. Not on the family computer with the tax return and online banking.

That is not excessive caution. An agent with file access and a network connection, fed with a third-party skill, is functionally the same as a third-party program with the same rights. The fact that it consists of text changes nothing about that.

## Conclusion

OpenClaw is an impressive piece of software and currently not a tool for production data. Acknowledging both at once is the honest position.

Anyone who wants to work with it settles three things beforehand. Where does it run without being able to do damage. Which cost limit applies and who enforces it. And which actions may the agent carry out without asking. On the last question, the usable answer for everything that deletes, sends or pays is: none.

What the episode shows beyond that applies more generally. Prompt injection is not a teething trouble that the next model will settle. It follows from instruction and content sharing the same channel. As long as that is the case, the safeguards lie outside the model.

> **The story continues …**
>
> In parallel with this development, Opus 4.6 and new Claude Code functions with genuine multi-agent teams including an orchestrator were released. The subject is picking up speed across the industry, and with it the security questions move from the hobby corner into regular operations.

---

The full episode: [OpenClaw](https://think-ai.podigee.io/26-openclaw-extreme)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
