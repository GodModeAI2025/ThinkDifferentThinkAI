---
folge: 24
titel: "From the folder to the whole machine: where personal AI assistants become dangerous"
bildtitel: "Access to everything"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/24-clawdbot"
---

# From the folder to the whole machine: where personal AI assistants become dangerous

*Claude Code works in one directory. Clawdbot gets the whole machine if left to it. That difference decides more about the risk than any choice of model.*

By Mark Zimmermann

The question of the episode is an old one and is becoming topical again: how close are we to a real Jarvis. The route there can be told as a sequence of stages, and every stage shifts a boundary.

Right at the bottom stand Alexa and Siri, which could barely chain anything together beyond weather queries. That is not derision, it is the sober balance after ten years.

> **in brief**
>
> - Claude Code works in the terminal and organises whole directories, at times over-eagerly
> - Claude Co-Work is the graphical variant for knowledge workers, with skills and MCP servers
> - Clawdbot runs locally on a Mac Mini, Raspberry Pi or virtual server and is operated by messenger
> - Its memory sits in Markdown files and persists between sessions
> - Unlike the others it is not restricted to one directory

## The stages and their limits

The biggest leap is marked by Claude Code as a terminal tool. It organises whole directories, renames files and, with the right dose of over-eagerness, also does things that were not meant that way. The decisive point is the limitation: it works in one directory.

Claude Co-Work is the graphical variant for knowledge workers without a fear of the terminal. Added to that are skills, that is Markdown instructions with optional deterministic code, and MCP servers, through which tools such as Blender can be controlled directly.

Clawdbot, affectionately called Space Lobster, is something else. It runs locally on a Mac Mini, a Raspberry Pi or a virtual server, is addressed via messenger, that is Signal, Telegram, WhatsApp or iMessage, and builds itself a persistent memory out of Markdown files.

> ### Why the directory boundary matters so much
>
> An agent restricted to one directory has a limited damage radius. If something goes wrong, the damage is in the directory, and what usually sits there is a project under version control.
>
> An agent with access to the whole machine does not have that limitation. Its damage radius covers everything the executing user can reach: documents, keychain, network drives, signed-in services.
>
> On top of that comes a chain that is frequently overlooked. Access to a mailbox means in practice access to password resets and in many cases to the second factor. An agent with mailbox access therefore has indirect access to everything that can be reset through that mailbox.
>
> This chain can be broken: a separate user with separate rights for the agent, a separate mailbox without password resets, a second factor on a device the agent cannot get to. The effort is manageable if it is made beforehand.

## What has already gone wrong

The episode collects examples that are not thought experiments.

The best known: a faked mail about an alleged security incident got the bot to empty the entire mailbox. The attack consisted of one mail. No vulnerability, no password, no technical trick.

A second example shows the other direction: an apple cake poem in a LinkedIn profile exposed which recruiters use AI tools, because their replies contained the poem. The same mechanism, a harmless occasion.

Then there is the satirical piece about the assistant that resigns on its own initiative, files for divorce and takes over the house. Entertainment with a serious core, because the rights that would be needed for it are ones people actually hand out at the moment.

## What follows from it

For practical use there is an order of operations that holds regardless of the tool.

Clarify the damage radius first. Not what the agent is supposed to do, but what it can reach at most. Those two sets almost never coincide.

Second, separate the identity. An agent should not work as you but as a separate user with its own narrow rights. That is the difference between a mistake and an incident.

And third, define which actions never take place without a query back. Deleting, sending, paying and changes to permissions belong on that list, regardless of how reliably the system has worked so far.

## Conclusion

Personal assistants have reached the point where they become useful, and for exactly that reason the point where the question of rights counts. The tools differ less in their capability than in their limitation.

The most usable test question before setting one up is therefore not what the tool can do, but what it cannot do. With Claude Code the answer is: nothing outside the directory. With a locally running full-access assistant it is: everything you can do.

Either can be the right choice. The mistake lies in not knowing the difference.

> **The story continues …**
>
> The episode announces two topics that both deserve their own treatment: how the waiting times of agents can be designed so that users do not lose confidence at night, and the orchestration of whole swarms of agents, for which of all fields it is currently the gaming scene that supplies the most usable models.

---

The full episode: [Clawdbot](https://think-ai.podigee.io/24-clawdbot)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
