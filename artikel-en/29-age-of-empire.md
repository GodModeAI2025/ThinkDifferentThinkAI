---
folge: 29
titel: "Ten agents, ten terminal windows: why the chat interface reaches its limit"
bildtitel: "Ten agents, one window"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/29-age-of-empire"
---

# Ten agents, ten terminal windows: why the chat interface reaches its limit

*Building simulations have made thousands of units and supply chains manageable for decades. Agents, by contrast, are steered through terminal windows placed side by side. That is not a detail, it is the bottleneck.*

By Mark Zimmermann

One prompt, one answer: for a conversation with a model that is the right form. For steering several agents working in parallel it is not, as soon as skills, MCP connections, memory files and budget consumption all have to stay in view at the same time.

The episode's title is a bow to Age of Empires, and the analogy carries further than the joke.

> **in brief**
>
> - The chat interface does not scale beyond a handful of parallel agents
> - Building simulations have been solving the same problem visually for decades
> - First approaches present agents as figures in a game world, complete with zones for permissions
> - Four gradations of human control: in the loop, on the loop, in the lead, out of the loop
> - Trust is not decided by control but by comprehensibility

## Why games can do this better

Factory and economic simulations make thousands of units, supply chains and production lines manageable. They do so with means that barely appear in developer tools: an overview map, status colours, warning symbols at the location of the problem, grouping of similar units, and the possibility of switching between overview and detail without giving up one for the other.

A terminal window can do none of that. It shows one thing, chronologically, and whoever has ten of them open has ten chronicles and no overview.

First approaches in this direction do exist. Tools such as Agent Craft or the mentioned pixel-agents project present agents as figures in a game world, including safety zones which, through the assignment of permissions, determine where an agent is allowed to walk at all.

The last point is the most interesting one. Presenting permissions spatially makes them verifiable. Nobody reads a permission matrix. A zone a figure cannot walk into is understood by everyone.

## Four levels of control

A second focus concerns a sharpening of terms that constantly gets muddled in discussions.

> ### Human in the loop through to human out of the loop
>
> **Human in the loop:** the human is part of the process. Nothing happens without their approval. Safe, slow, and beyond a certain number of operations not sustainable, because approval degenerates into a formality.
>
> **Human on the loop:** the process runs on its own, the human observes and can intervene. This is the level most productive systems end up at. It only works if anomalies become visible without anyone having to search for them.
>
> **Human in the lead:** the human sets goals and boundaries, the system finds the way. Control takes place through specifications and checking of results, not through individual steps.
>
> **Human out of the loop:** no human involved. Defensible for narrowly bounded, well understood tasks with limited damage, otherwise not.
>
> The levels are not maturity grades in which the last one would be the best. They are a selection, and the right choice depends on the possible damage. The most common mistake is to work de facto at level two while formally claiming level one.

As the number of agents rises, this distinction becomes more important, because the first level simply no longer carries.

## Gaming experience as a working skill

With a wink, but not without substance, the thesis is put forward that experience with real-time strategy and World of Warcraft is becoming a sought-after skill. Delegating to many units acting at the same time and supervising them is exactly what strategy players have been training for years.

Viewed soberly, this is about the distribution of attention: recognising where something is going wrong right now without observing everything at once. That is a learnable skill and it is barely contained in classic IT training.

## What happened alongside

The news section of the episode contains a remarkable juxtaposition. Anthropic under Dario Amodei turns down a Pentagon contract because mass surveillance and autonomous weapon systems cannot be ruled out. OpenAI signs the same contract shortly afterwards.

Alongside that, a very practical question: how does one move one's AI history between vendors. Via the data export at ChatGPT and a migration prompt at Claude it works in part. That this question comes up at all shows how far everyday work and choice of model have become interwoven by now, and how little scope for switching actually exists.

## Conclusion

The episode ends with a sentence that works as a leitmotif: trust remains the real final challenge to the user interface.

The point behind it is precise. Whether we trust a system with many autonomous parts is not decided by control but by comprehensibility. A system that shows its processes traceably will be accepted even when not every step is approved. A system that works opaquely does not become trustworthy even with an approval button, because nobody knows what they are approving.

For your own environment a simple test follows from this. Can you see at a glance how many agents are running, what they are doing and which of them needs attention? If the answer is “I have the windows side by side”, the interface is the bottleneck and not the model.

> **The story continues …**
>
> Two side topics from this episode deserve their own treatment: the MIT experiment in which AI agents independently developed cultures, currencies and religions in a Minecraft world, and biological neuron chips that play Doom by now. Both sound like curiosities and touch on questions nobody has sorted out yet.

---

The full episode: [Age of Agents](https://think-ai.podigee.io/29-age-of-empire)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
