---
folge: 56
titel: "A rule in a text file is not a boundary"
bildtitel: "A rule is no boundary"
kicker: "In conversation with Alexander Heusingfeld"
podigee: "https://think-ai.podigee.io/56-personal-assistants"
---

# A rule in a text file is not a boundary

*Anyone putting routines onto an assistant hits compliance faster than technical problems. A field report on hard boundaries, open interfaces and the question of who may decide where a piece of data is allowed to sit.*

By Mark Zimmermann

Alexander Heusingfeld asked his freshly set-up system for an overview of the routines he had configured, as a graphic. Shortly afterwards a browser window opened and the graphic was sitting in the cloud. The configuration file said that processing stays local. The apology came promptly and without evasion: the rule had been known. That moment is the core of the episode, because it separates two things that are frequently confused. A written rule is a declaration of intent. A boundary is something that holds even when a system considers another route sensible.

> **in brief**
>
> - With a second brain the human decides what goes in. A routine needs a rule that holds without supervision
> - Rights belong in the operating system, not in a configuration file the assistant can read and override
> - An MCP server without authentication is an open service that every local process can reach
> - The argument about a name in a note is really an argument about where it is stored

## The everyday case that raises the question

The starting point is harmless. A personal assistant for the working day should know the project list, go through notes and mail, perhaps chat messages too, and notice in passing that an evening appointment collides with the dentist. As soon as you write that requirement down, the uncomfortable questions stand next to it.

The documents folder synchronises into a cloud. Who accepted its terms, the private individual or the employer? The notes contain information about colleagues. What happens to it when a model reads it? The difference from the familiar second brain topic is small and consequential: with a store, a human decides at every entry what goes in. A routine runs without that human and therefore needs a rule that holds even when nobody is looking.

## Two machines, the same answer

Both participants arrived independently at the same solution: a dedicated device. On one side a Mac Mini that evaluates over 40 sources, builds a daily briefing from them, feeds a tablet via MCP and sorts voice notes into tasks, based exclusively on publicly accessible content. On the other a separate device with its own Apple ID, its own mail address, its own Wi-Fi segment and access only to the outside.

The term for it is hard boundaries. Whatever cannot be assessed across all scenarios is restricted by default, rather than repaired later. That is not scepticism towards the tool but a consequence of how it works.

> "I am simply a friend of configuring the rights hard in one place in the operating system. You use a local user who cannot change these rights."
>
> **Alexander Heusingfeld**

The difference from a written rule is practical: a user account without write permission does not argue, does not apologise, and does not explain why it interpreted the rule differently this time.

## Why the old perimeter no longer fits

That this does not stop at anecdotes becomes clear when you look at the interfaces. Anyone running an MCP server without authentication has an open service on their own machine. Every local process can address it, and behind it sit mail, notes and files. At the same time more and more products are building in such servers without any way to switch them off.

The classic perimeter protection helps little here, because its model assumes a human at a keyboard and mouse. A tool that arrives on the machine through a regular enterprise licence is already behind every protective layer, and it now talks to further sessions of itself. One window takes the role of coordinator, others feed it. For the security architecture that is a piece of software the rest of the software on the device did not reckon with.

> ### Why one goal is enough
>
> A model with a task does not behave like a program with an error message. It pursues the goal and tries routes until one works. The episode has an image for this from working life: send a new colleague off to fetch form 37 and you expect them to come back at some point and see the joke. A model takes the task at face value and knocks on every door until one opens. If it stands open, it goes in and checks whether that gets it further.
>
> From this follows no warning about malice, but a requirement of the environment. What should not be reachable must not be reachable, regardless of what an instruction file says. Anything else relies on a non-deterministic system interpreting a rule the same way every time.

## Notes about people

A separate section of the episode covers a topic that escalates quickly in companies. Most minute-taking tools want to attribute who said what and when. In most cases that is not the interesting information. What matters is the outcome and who takes something on. Names, meanwhile, are everywhere anyway, in ticket systems, wikis and repositories, often with email addresses attached.

> "By now I am at the point where I say, who may decide where a piece of data may sit."
>
> **Alexander Heusingfeld**

From this follows a useful reframing: when a team argues about whether a name may appear in a note, that is in truth a discussion about where this note may be stored. Added to that is the recommendation to talk to the works council about hypothetical cases before they occur. The reason is concrete: a model draws conclusions from scattered data that nobody wanted drawn, and no downstream check rules out hallucinations completely. Attribution in minutes is therefore only worth it where a follow-up task comes out of it.

## What goes into practice

When it comes to building, the episode arrives at a sober recommendation. Not every routine needs a model. Anyone wanting to check a mailbox regularly uses a script and calls the AI only when there is something to decide. That saves not only cost, it also shrinks the surface on which something can go wrong. For everything deterministic the rule is: represent it in the skill as program code, without absolute paths, so that an agent does not go searching when a file is missing.

How quickly a fuzzy rule becomes expensive is shown by a calculation error in one of his own research routines. The requested five results turned into over 500 entries in the database. If that happens on a service with usage limits, the mistake turns into an invoice.

## Conclusion

The episode does not deliver a list of tools but an order of operations. First clarify which routine is to be built at all and which data it touches. Then decide where that data may sit, and anchor that decision where it is not negotiable: in the permissions concept of the system. Only then the question of which model and which tool.

Anyone reversing that order builds the boundary into a text file and hopes for cooperation. That works most of the time. For the rest, there is this episode.

> **The story continues …**
>
> One detail remains unsolved: a list of what must not enter a knowledge store is itself confidential and therefore does not belong in the repository where the store lives. If it exists as one flat list for all targets, a company name in it also blocks the legitimate push to the company repository. The configuration therefore has to apply per target, and for that you first need a list of the targets.

---

The full episode: [Personal Assistants](https://think-ai.podigee.io/56-personal-assistants)
All episodes with full transcripts: [Think Different. Think AI. Archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
