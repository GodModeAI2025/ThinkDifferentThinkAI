---
folge: 27
titel: "Agentic Engineering: what is left of software architecture"
bildtitel: "The end of reusability?"
kicker: "In conversation with Klaus Rodewig and Alexander Heusingfeld"
podigee: "https://think-ai.podigee.io/27-wie-ki-unser-arbeitsleben-verandert"
---

# Agentic Engineering: what is left of software architecture

*When native code comes out of a JSON structure or a Figma screenshot in minutes, reusability and the choice of language lose weight. Two practitioners from the Vorwerk environment draw a bold thesis from that and supply the qualifications along with it.*

By Mark Zimmermann

The guests are Klaus Rodewig and Alexander Heusingfeld, both at Vorwerk, Alexander additionally host of the podcast “Conversations about Software Engineering”. Both make it plain that they started out sceptical. The turnaround was set off by GitHub Copilot and reinforced by Claude Code.

The starting point is a sober observation about half-lives. What was n8n half a year ago is now OpenClaw. What was OpenClaw a month ago is now Craft Agent. This pace overwhelms teams, and it does so regardless of their ability.

> **in brief**
>
> - Reusability, app architecture and the choice of language lose weight when code is produced in minutes
> - Vibecoding uses AI as qualified autocompletion, Agentic Engineering hands over end-to-end responsibility
> - Team boundaries between front end and back end were organisational in origin, not technical
> - An agentic control loop can replace quarterly ISMS audits under ISO 27001
> - An agent must not have write access to its own core files

## The bold thesis

When a machine produces native code from a JSON structure or a Figma screenshot in minutes, three things lose significance: reusability, software architecture in the sense of app architecture, and even the choice of programming language.

The analogy both guests choose for this comes from their own careers: the transition from assembler to high-level languages. Back then hand-optimised assembler was considered superior, and it was, measured by run time. It lost all the same, because the advantage was no longer worth the effort.

Note what the thesis refers to. It concerns app architecture, that is the internal structure of an application. It does not concern system architecture: how systems interact, where data sits, which contracts apply between services. That part tends to become more important, because more individual pieces come into being.

Reusability loses value for a concrete reason: it was an answer to expensive creation. Building a library, maintaining it and using it in five projects paid off as long as rewriting was expensive. If that price falls, the calculation tips over, and the maintenance effort for the shared library remains.

## Vibecoding versus Agentic Engineering

The core of the episode is a distinction that is missing from many discussions.

Vibecoding means using AI as qualified autocompletion. The human stays in the process, decides every step and accepts suggestions.

Agentic Engineering means handing end-to-end responsibility to teams of agents, across front-end and back-end boundaries. The decisive remark on this: these boundaries existed for organisational reasons, not technical ones. An agent that changes both sides at once violates no technical necessity, but a rule about who is responsible for what.

That is an uncomfortable insight for organisations that take their team structure for an architectural decision.

> ### Guardrails, in concrete terms
>
> Using OpenClaw as an example, the episode explains a point that is easily overlooked: an agent must not have write access to its own core files, meaning the files that lay down its behaviour and its identity.
>
> The reason is not mistrust but logic. A system that is allowed to change its own rules does not have rules, it has suggestions. And since an agent is optimised for helpfulness, in case of doubt it will treat a rule that stands in the way of a task as an obstacle.
>
> Technically the implementation is simple: withdraw write rights, store the configuration outside the writable area, permit changes only by a route that includes a human being.
>
> The next building site is one level up: a meta instance that checks all running agents. Some call this an agent orchestration platform. There are no ready answers for it yet.

## Compliance as a control loop

The most surprising part in practical terms comes from compliance. An information security management system under ISO 27001 classically works with audits at fixed intervals, frequently quarterly. Between two audits nobody knows exactly where things stand.

An agentic control loop can replace this: continuous checking instead of spot checks on fixed dates. Against the background of the EU Cyber Resilience Act that is more than a convenience, because continuous evidence is expected there.

Important here: continuous checking does not replace the audit, it feeds it. An auditor wants to see evidence, and a control loop produces it continuously instead of it being scraped together shortly beforehand.

## Three pieces of advice for getting started

The episode ends unusually concretely, and the three points can be applied immediately.

**Make no assumptions.** Try out real everyday cases in an isolated environment, from automated invoice export to your own MCP server for mail, calendar and reminders. A second-hand assessment is worthless at this pace.

**Understand patterns instead of tool names.** Skills, plugins, validation loops and MCP turn up in every one of these tools. Anyone who knows the patterns is not back at zero at the next change of name. Anyone who collects tool names starts from scratch every time.

**Steer the data flow deliberately.** The sentence on this is the most important of the whole episode: the fact that an application is installed locally no longer means that the data stays local. Check that per tool, not per category.

## Conclusion

The thesis of the end of software architecture is deliberately sharpened and hits a real core: what arose from expensive creation loses value when creation becomes cheap.

What remains is everything that has to do with interaction: interfaces, data sovereignty, operations, traceability and the question of who answers for what an agent has done.

For teams that means, concretely: check which of your structures have technical grounds and which organisational ones. The second sort is currently up for review, and it is better to decide that yourself than to have it demonstrated by an agent that changes both sides at once.

> **The story continues …**
>
> A meta level that monitors all running agents is the logical next layer and so far exists only in rudimentary form. As long as it is missing, the number of agents an organisation can answer for is limited by the number of people who look.

---

The full episode: [Wie KI unser Arbeitsleben verändert!](https://think-ai.podigee.io/27-wie-ki-unser-arbeitsleben-verandert)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
