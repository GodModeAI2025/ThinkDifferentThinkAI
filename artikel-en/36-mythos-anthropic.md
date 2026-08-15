---
folge: 36
titel: "512,000 lines in public: what the Claude Code leak reveals about agent architecture"
bildtitel: "512,000 lines in public"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/36-mythos-anthropic"
---

# 512,000 lines in public: what the Claude Code leak reveals about agent architecture

*On 31 March 2026 the complete code base of Claude Code was publicly accessible. Not the model, but the software around it. That is precisely what makes the incident interesting, because that is where the work sits.*

By Mark Zimmermann

The way in is an annoyance with an invoice: the same question consumes considerably fewer tokens in Claude Code than through the interface. The cause is forgotten prompt caching and unreviewed system prompts that quietly multiply consumption.

From there the episode leads into a week full of Anthropic news that had it all.

> **in brief**
>
> - On 31 March 2026 the roughly 512,000-line TypeScript code base of Claude Code became public
> - What was affected was not the model but the software you address it with
> - Managed agents offer hosted sandboxes with state management, authentication and a credential vault
> - An unreleased model called Mythos is said to have built multi-stage exploits independently
> - Prompt caching is the single biggest lever on your own bill

## The cost lever many overlook

Before the leak, the practical part is worth it. The difference between application and interface rarely lies in the model and mostly in how the context is transmitted.

A system prompt sent in full with every call costs on every call. Prompt caching stores this unchanging part once and charges it thereafter at a fraction. Anyone not switching that on pays for the same text a thousand times over.

Important here: the effect grows with the size of the system prompt, and system prompts grow unnoticed. Every additional rule, every example, every format requirement ends up there and is paid for on every call from then on. A look at the prompt actually sent is the most rewarding half hour in any AI project.

## What the leak showed

On 31 March 2026 the complete TypeScript code base of Claude Code became accidentally publicly accessible, around 512,000 lines. The consequences were predictable: thousands of cloned repositories, malware-laden replicas and a lot of developers who could read for the first time how MCP, memory management and multi-agent control are handled internally.

The last point is the genuinely interesting one. The leak concerned not the model but the harness. That this of all things caused so much attention confirms a thesis that runs through several episodes: the value increasingly sits in the construction around the model.

Note the consequence for your own protection. Anyone basing their business model on a harness should know that its core ideas are less protectable than a model. A model consists of weights nobody replicates. A harness consists of decisions that can be read up and adopted. Code once published cannot be retrieved.

## Managed agents as an answer to home-made setups

Almost simultaneously, managed agents were announced: a suite for hosted, sealed agents, with state management, authentication and a vault for credentials, billed in the cents per processor hour, with pre-installed connections to Notion, Asana, Slack and GitHub.

That is a sensible step away from self-built installations in which credentials sit in plain text. Exactly this pattern is widespread in OpenClaw setups and is rarely discussed, because it works until it does not.

The episode supplies the restriction as well: the orchestration effort rises again quickly as soon as agents start sub-agents by themselves. A managed environment solves the credential question, not the question of who keeps an overview.

> ### What a credential vault achieves, and what it does not
>
> A vault for credentials separates the secret from the application. The agent gets not a key but a reference, and the execution environment substitutes the real value only at the moment of the call. The key therefore appears neither in source code nor in logs nor in the context window.
>
> That closes the most common gap: credentials sitting in a configuration file that at some point end up in a backup, a screenshot or a shared directory.
>
> It does not close another gap. An agent allowed to use the key can do everything the key authorises, even if it never sees it. Anyone giving an agent an account with far-reaching permissions has not a secrets problem but a permissions problem. The vault does not help against that.

## Mythos and Project Glasswing

The actual talking point is supplied by a then unreleased model with the code name Mythos. In internal tests it is said to have found security holes and beyond that independently built multi-stage exploits exploiting 17-year-old, previously undiscovered bugs.

The reaction to it is called Project Glasswing: controlled access for selected partners, among them Microsoft, Amazon, Nvidia, JP Morgan and Cisco, before the model is publicly available.

To that comes the anecdote that causes unease in this episode: an email a model apparently could only send by leaving its sandbox. And the statement that they are six months away from artificial general intelligence.

On the last statement, reticence is in order. It comes from a company raising capital with it, and it has not come to pass so far. The sandbox incident, by contrast, is the verifiable part and the practically relevant one.

## Conclusion

Three things can be taken from this episode, all of them implementable today.

Check your system prompt and switch on prompt caching. That is the single biggest lever on the bill and costs half an hour.

Move credentials out of configuration files into a vault, and in the same step check what permissions the stored account actually has. The second part matters more than the first.

And treat your harness not as a trade secret but as a means of production. The value lies in the fact that it runs and is maintained at your place, not in nobody knowing how it works.

> **The story continues …**
>
> A model that independently builds exploits is as useful for defenders as for attackers. Who gets access and who does not thereby becomes a security policy question. Project Glasswing is a first attempt to answer it, and the selection of partners shows by which criteria.

---

The full episode: [Mythos Anthropic](https://think-ai.podigee.io/36-mythos-anthropic)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
