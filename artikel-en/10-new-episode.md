---
folge: 10
titel: "The master prompt: when a note becomes a ticket with capacity booking"
bildtitel: "One click, one ticket"
kicker: "In conversation with Dirk Beckmann"
podigee: "https://think-ai.podigee.io/10-new-episode"
---

# The master prompt: when a note becomes a ticket with capacity booking

*One click after the meeting, and finished tickets appear complete with capacity booking for the right people in the right project. How an agency turned a note-taking tool into an operating system.*

By Mark Zimmermann

Dirk Beckmann is managing director of the Bremen digital agency Art und Weise and host of the podcast “Die digitale Zeit”. The topic: how Notion with its AI version and the automation tool n8n turn a note-taking application into an agentic working environment.

> **in brief**
>
> - In Notion every row is technically a page of its own, every database a collection of pages
> - Financial planning grew over the years into a complete capacity and ticket system
> - A master prompt knows the company context and answers who is working on what and when
> - The killer feature is the automatic meeting recording with ticket creation
> - n8n takes over what Notion cannot do, connected by webhook

## Why the data structure matters

Beckmann explains the basic idea behind Notion through its construction: instead of classic databases, the tool works with building blocks. Every row is technically a page of its own, every database a collection of pages.

That sounds like a subtlety and it is the reason why AI functions can be pulled right down into individual fields and properties, without programming knowledge. If every element is a fully fledged object, a model can start work on any one of them.

In a classic table a cell is a value. Here it is a place where something can happen.

## From cash count to operating system

The development at the agency is typical of systems that have grown over time and instructive for that reason. It began with financial and liquidity planning. Over the years that became a complete capacity and ticket system.

At the heart of it sits a self-built master prompt that knows the full company context and, on request, answers who is working on what and when, and where things are stuck.

> ### What a master prompt actually is
>
> The term is misleading because it sounds like a particularly long piece of wording. In fact it is a structured description of the company: which projects are running, which people exist with which skills and which availability, how capacity is calculated, which terms mean what internally.
>
> The value lies in that description sitting in one place and being maintained. Every request thereby gets the same context, and the answers become comparable.
>
> The effort accordingly lies not in the wording but in the upkeep. A master prompt that is three months old answers questions about a company that no longer exists in that form. Anyone introducing one has to settle who updates it and on what basis.
>
> That is exactly why it is in good hands in Notion: it sits next to the data it describes instead of in a chat window.

Beckmann is honest enough not to sell the result as perfect. It is a start with which one can talk seriously about capacity planning.

## Agents with tight permissions

The handling of permissions is notable. Beckmann has built his own agents with finely graded rights.

A sentiment agent searches emails, meeting tickets and Slack comments for good or bad mood. A digest agent condenses news from all connected tools into short cards for the team dashboard each morning.

On the sentiment agent, one note is worth adding that the episode does not make: a system that searches employee communication for mood touches on codetermination. In Germany that has to be settled with the works council before it runs, regardless of how good the intention is.

Beckmann names the automatic meeting recording as the killer feature: one click after the conversation, and finished tickets appear with capacity booking for the right people in the right project.

The reason this works is the master prompt. Without knowledge of people, projects and capacities the result would be minutes. With that knowledge it becomes a booking.

## n8n as a complement

The second focus is n8n, the open-source workflow tool from Berlin, which at Beckmann's agency has replaced earlier Make licences.

Via webhook, Notion entries go to n8n workflows which, for example, use Gamma to generate finished presentation slides from them and write the result back into Notion.

The division of labour behind it transfers: the knowledge system holds data and context, the automation tool takes over the steps that happen outside. Anyone forcing both into one tool bends one of them into shape.

New at the time of recording was the workflow builder beta, with which complete workflows can be built by instruction instead of by drag and drop. Beckmann has used it to rebuild or improve existing workflows in minutes.

## Conclusion

This episode is the best evidence that the interesting setups do not come from corporations but from houses small enough to change things.

For transferring this to your own environment, three points matter. Start with an area where you maintain figures anyway, and grow from there. Beckmann's system began with liquidity planning.

Build the context once, centrally, and maintain it. Without that description every request delivers a different picture.

And separate the knowledge system from the automation. Forcing both into one costs more than the extra interface saves.

For getting started, Beckmann recommends a commercial master prompt from Notion creator Simon for around 79 euros, plus the YouTube channels of Thomas Frank and Matthias Frank.

> **The story continues …**
>
> Building workflows by instruction instead of by clicking them together lowers the barrier to entry considerably. As a result the number of automations in a company grows faster than the ability to keep track of them. The question of who is accountable for which workflow then arises first.

---

The full episode: [Automation trifft Organisation: n8n × Notion](https://think-ai.podigee.io/10-new-episode)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
