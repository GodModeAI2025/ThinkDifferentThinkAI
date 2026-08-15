---
folge: 33
titel: "Temporal UX: why waiting time with AI agents is a design problem"
bildtitel: "Waiting needs designing"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/33-termporal-ux"
---

# Temporal UX: why waiting time with AI agents is a design problem

*An agent works for ten minutes. What happens on the screen during that time decides whether the productivity gain arrives or seeps away in checking glances. A concept from service design that has barely been thought through in the AI context.*

By Mark Zimmermann

Airports offer a well-known example of designed time. If the walk to the baggage belt is deliberately lengthened, travellers experience the waiting time as shorter, although it is the same length or longer. The waiting time was not shortened but filled.

Precisely this principle is almost entirely missing in work with AI agents. Under the name temporal UX it has been circulating in the service design world for some time; in the AI context it is barely thought through.

> **in brief**
>
> - Current models have no sense of elapsed time and assert durations that are not true
> - From five to six agents running in parallel the error rate rises noticeably, because the overview is lost
> - Reasoning models show their thinking process partly because visible progress creates trust
> - Timeouts and heartbeats are unresolved as soon as agents talk to each other instead of to humans
> - Without deliberate time design, the management load eats up the productivity gain

## The starting case

The occasion is an experience of their own. During joint vibe coding, a task was handed to an agent, implemented with Craft Agents on the basis of an Opus model. The other participants received only sporadic second-hand updates in the meantime.

The result was a six-point list being worked through. In effect that resembles an installation bar stuck at 98 per cent: there is progress to see, and nobody knows how much longer it will take.

The analogies in the episode are all older than AI and describe the same problem: swapping floppy disks, loading screens with hidden jokes in old video games, Pong mini-games on Flash websites. All early solutions for making waiting time bearable without lying about its length.

## Why models show their thinking process

One central strand concerns trust. Reasoning models display their train of thought, and the obvious explanation is transparency.

The second explanation is at least as important: visible progress keeps people engaged. Anyone who sees that something is happening waits longer and mistrusts the result less. That is not manipulation, as long as the steps displayed actually take place. It is, however, a design decision, not a technical necessity.

Note the flip side. A visible thinking process binds attention. Anyone who stays and watches gains no time. The actual benefit only arises when you can let the agent work and do something else, and for that it takes a reliable notification instead of a captivating screen.

## The problem with several agents

Beyond a certain number of parallel agents, the benefit tips over. In the episode the limit sits at five to six: after that the error rate rises noticeably, because you lose track of who is working on what and where a prompt or a checking step is missing.

That is not a question of compute but of human management load. Every running agent occupies a slot in working memory, and that slot is limited.

As a picture of what is wanted, the episode brings in an old Palm Pilot application called Agendus: tasks that travel with you until they are done, plus a simple wrap-up and the ability to merge contexts from different conversations. That is not nostalgia but a precise requirements description that today's agent tools do not meet.

## Models have no sense of time

The finding with the greatest practical consequences is also the easiest to overlook. Current models have no sense of elapsed time. Anyone not explicitly supplying the date and time in the prompt gets statements such as “I researched for two hours” while two minutes have actually passed.

For reports, minutes and anything containing time references that means: supply timestamps explicitly and do not have the model estimate durations.

> ### Why timeouts between agents are unresolved
>
> As long as a human waits for a model, the matter is simple: the human notices that nothing is happening and breaks off.
>
> Between agents this instance falls away. If an agent waits for another's answer, it needs a time limit after which it treats the attempt as failed. If the limit is too short, it discards results that would have arrived shortly afterwards. If it is too long, it blocks.
>
> This is aggravated by cascades. If ten thousand agentic systems wait for each other and one does not answer, in the unfavourable case all the others hang idle without an error being reported anywhere. Heartbeat mechanisms, that is regular signs of life independent of the result, are the established answer from distributed systems engineering. In agent tools they are so far the exception.

How concrete that gets is shown by an anecdote from the episode: a timeout in the frontend swallowed the finished answer of an n8n workflow. The work was done, the result was there, and it never arrived. That is not a model problem and not an automation problem but a time design problem.

## Conclusion

Time design must not be left to chance. It belongs deliberately considered on two levels: in the interface and in the organisation, that is in workflows, notifications and handover points.

Three practical steps follow for your own environment. Supply models with the date and time instead of believing time statements. Limit the number of agents running simultaneously to what you can keep track of, four rather than eight. And make sure a finished result reaches you even if you have done something else in the meantime.

Otherwise the paradoxical state the episode describes arises: the machine works faster, and overall performance falls, because managing the waiting time costs more than the work saved.

A sentence from Benjamin Franklin fits at the end, with which the episode closes: lost time is never found again.

> **The story continues …**
>
> Agent tools such as n8n or Claude barely consider time design so far. As long as that stays the case, it falls to users to build notifications, time limits and handovers themselves. Anyone doing that today has less to change later.

---

The full episode: [Temporal UX](https://think-ai.podigee.io/33-termporal-ux)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
