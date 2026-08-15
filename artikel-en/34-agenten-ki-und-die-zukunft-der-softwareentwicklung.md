---
folge: 34
titel: "Threat modelling for agents: four questions before the AI reaches the bank account"
bildtitel: "Four questions before access"
kicker: "In conversation with Alex and Klaus"
podigee: "https://think-ai.podigee.io/34-agenten-ki-und-die-zukunft-der-softwareentwicklung"
---

# Threat modelling for agents: four questions before the AI reaches the bank account

*An agent is supposed to take over the monthly bookkeeping: invoices from the inbox, bank statement, PDF export. As soon as it reaches bank data, a tooling question turns into a security question.*

By Mark Zimmermann

This episode is made without Jens for once, but with two recurring guests. The starting point is a use case of the kind found in many small offices: the monthly bookkeeping is to be automated, invoices arrive by email, plus a bank statement and a PDF export. The question is whether OpenClaw or Craft Agents is the right tool for it.

The answer is a well-founded “it depends”, and the interesting part sits behind it.

> **in brief**
>
> - Craft Agents is a graphical alternative to Claude Code based on the Claude SDK, without a terminal
> - Tasks keep running there even when the application is closed
> - Across Claude Code, OpenCode and OpenClaw a common pattern book has established itself: skills, plugins, hooks, evaluations
> - Adam Shostack's four-question framework can be run as a skill of its own before every commit
> - The biggest security risk is that many users do not know what a token is

## Tool choice without a terminal

Craft Agents enters as a graphical alternative to Claude Code, built on the Claude SDK. No terminal, but MCP connections, skills and tasks that keep running when the application is closed.

This last property is in practice the decisive difference. An agent that only runs while a window is open is fine for interactive work. An agent working through assignments over hours needs execution that is independent of the screen.

The everyday examples in the episode are tellingly unspectacular: a Notion token that has to be re-authenticated constantly, and an application for audio transcription for colleagues who have nothing to do with IT. Neither is a software project, they are points of friction somebody removes.

What is remarkable is what has emerged across the tools in the process. Skills, plugins, hooks and evaluations appear in comparable form in Claude Code, OpenCode and OpenClaw. A common pattern book is emerging before there is a standard. Anyone who has understood the terms in one tool finds their way around the others.

## When the agent reaches the account

It gets serious at the point where the agent is to be given access to bank data or the inbox. The panel discusses sandboxing, network segmentation and zero trust principles, and the tone stays pleasantly level-headed.

The core statement is not a warning about the technology but an observation about the users: many simply do not know what a token is. Precisely that becomes the security risk. Anyone who does not understand that a string in a configuration file carries the same rights as their own password treats it accordingly.

> ### Adam Shostack's four questions
>
> The four-question framework is the shortest usable form of threat modelling and manages without a tool chain:
>
> **What are we building?** A diagram or a list of the components involved and the paths between them. Without this step everyone discusses different systems.
>
> **What can go wrong?** The actual threat analysis. Who might want to achieve what, and via which of the paths drawn.
>
> **What are we doing about it?** For every threat found, a measure or a conscious decision to accept it.
>
> **Did we do a good job?** The review that turns the exercise into a habit.
>
> Klaus built this as a skill of his own in Craft Agents and has it run automatically before every commit. That is the most effective form: not one workshop a year, but four questions at every change.

For practice it is worth keeping to the order. Anyone starting at question two collects horror scenarios with no relation to the system. Anyone starting at question three buys measures against threats they do not have.

## What that does to software architecture

The second large block concerns team structures. Klaus reports how his earlier purism has softened: strictly native iOS in Swift, strict Kotlin for Android, no cross-platform. That stance was justified as long as native code was expensive and cross-platform tools forced compromises.

By now agents produce native code for both platforms, and the team boundary between iOS and Android development is blurring. What originally justified the separation was specialisation in one language and one framework. If that specialisation loses weight, the separation loses its reason too.

From this arises the further question the episode discusses and does not answer conclusively: does the classic application split into frontend team, backend team and app team still hold at all? It is drawn along technology boundaries, and precisely those boundaries are becoming permeable.

Note what does not disappear in the process. Knowledge of the platform, its release processes, its peculiarities and its failure patterns remains necessary. Somebody has to be able to assess what an agent produces.

## Conclusion

The episode delivers a practical order of steps for anyone wanting to let an agent near real data.

Clarify first whether the tool executes tasks without an open window. That determines whether you are automating at all or merely assisting.

Second, work through the four questions before you store credentials. That takes twenty minutes and is the only step in this list nobody catches up on once they have skipped it.

And third, make sure everyone working with such tools knows what a token is and what rights hang on it. That is not a training course but a sentence in the induction, and it prevents more damage than any additional software.

The tone of the episode is the model here: no panic about agents hacking everything, but the sober observation that ignorance is the actual risk.

> **The story continues …**
>
> If technology boundaries between teams become permeable, the question of the right split arises anew. An obvious option would be a split along domain responsibility instead of along the platform. Anyone seriously attempting that will first notice that career paths in organisations still run along the old boundaries.

---

The full episode: [Agenten, KI und die Zukunft der Softwareentwicklung](https://think-ai.podigee.io/34-agenten-ki-und-die-zukunft-der-softwareentwicklung)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
