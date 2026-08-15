---
folge: 45
titel: "90 minutes to shutdown: what the Fable case shows about AI sovereignty"
bildtitel: "90 minutes to shutdown"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/45-three-days-of-fable"
---

# 90 minutes to shutdown: what the Fable case shows about AI sovereignty

*Three days after launch, Fable 5 was no longer reachable for non-US citizens. Running sessions broke off, context was lost. The event works as a touchstone for your own architecture.*

By Mark Zimmermann

Anthropic released Fable 5, a model of the so-called Mythos class. This line had previously been available only to large providers such as Amazon and Google, because it is unusually good at finding security holes. At Firefox, hundreds of critical bugs were discovered and closed in a single day this way. According to a report at heise online, a security firm cracked a memory protection exploit on Apple M5 hardware with Mythos in five days.

Three days after launch the model was gone for all users outside the USA. In between lay a leaked system prompt, a hearing at the White House and the classification of Anthropic as a supply chain risk.

> **in brief**
>
> - Around 90 minutes passed from the decision to the shutdown
> - Running sessions broke off, context could not be transferred cleanly to other models
> - Open alternatives do not solve the problem fundamentally, once they become strategically relevant
> - The practical consequence is a model switcher in your own architecture
> - Knowledge belongs stored independently of the model, not in one vendor's session

## What happened technically

The actual damage lay not in the loss of the model but in the timing. The shutdown happened mid-operation. Sessions hung, projects stood still, and the context built up could not be transferred to another model without loss.

That is a point regularly overlooked in contingency plans. A model change is not a rerouting of traffic. What has emerged in a long session in the way of intermediate results, reasoning and decisions exists only there. Another model at best receives the conversation handed over and has to draw the conclusions afresh, frequently differently.

Note the difference from classic dependencies. If a database fails, the data is still there. If a model fails, the state is gone, unless it was secured outside.

## The geopolitical assessment

The obvious comparison in the episode is the kill-switch suspicion around fighter jets: the question of whether an imported system can be rendered unusable from a distance. The second comparison comes from the pandemic and concerns the realisation of how dependent Europe actually is in critical supply chains.

Both comparisons are pointed and hit a real point: a language model is an imported product with an availability that depends on trade policy.

Open models such as Kimi, MiniMax M3 or Manus soften that but do not fundamentally solve it. As soon as a model becomes strategically relevant it also becomes regulated, regardless of its country of origin. Anyone regarding open weights as permanent insurance is relying on a state of affairs, not on a property.

> ### What AI sovereignty means in practice
>
> The term is frequently reduced to the question of where a model was trained. For operations, three other levels matter more.
>
> **Availability:** can you continue using the service if a government or a vendor no longer wants that. The answer to this is a second, actually tested provider, not a contract with a second one.
>
> **Control over the environment:** who owns the harness in which the model works. If skills, context management and logs sit with you, the model is a component. If they sit with the vendor, your process is their product.
>
> **Control over the knowledge:** where does what your organisation has learned reside. As long as that sits in sessions and vendor projects, it travels with the vendor.
>
> Only the first level hangs on geopolitics. The other two are architectural decisions and can be taken without a political debate.

## The consequence: model switcher

The practical recommendation of the episode is unambiguous.

> “That is something to take away: I need some kind of intelligent model switcher.”
>
> **Mark Zimmermann**, co-host

Intelligent in this context means more than a configuration variable. A usable switcher knows the peculiarities of the models connected, knows which task tolerates which model, and has a tested replacement for every task. It is also the place where cost control can be housed, because not every request needs the largest model.

The honest restriction is supplied in the episode: in a switch, reasoning and context are lost if both are not secured separately. A switcher alone is not enough. It solves the availability problem and not the state problem.

## Knowledge belongs outside

That describes the second part of the consequence, and it is the more laborious one. What your organisation knows must not live in a model's session. It belongs in your own store, model-independent, searchable and in a format every model can process.

As a concrete approach the episode brings in Google's Open Knowledge Format. The thought behind it is unspectacular and convincing precisely for that reason: technical documentation should concentrate on content again instead of formatting. What exists as text structure can be translated economically into tokens. What exists as layout costs tokens for information nobody needs.

Anyone taking that seriously arrives at an uncomfortable conclusion about their own filing. Presentations and formatted documents are poor carriers of knowledge for machines, and the share of knowledge that exists only there is large in most organisations.

## Conclusion

The Fable case is not an argument against using American models. It is an argument against the assumption that a model is permanently available infrastructure.

Three measures follow from it, and all three can be started without a large investment. Test once a quarter whether your most important processes run on a second model. Secure intermediate states and decisions outside the session. And store knowledge so that any model can read it.

The effort for that is manageable. The effort of doing the same under time pressure while the sessions are already hanging is not.

> **The story continues …**
>
> It remains unresolved how European providers position themselves in this situation and whether a European alternative on equal footing emerges. Until then, sovereignty is less a question of the model's origin than of how quickly you can swap it out.

---

The full episode: [Three Days of Fable](https://think-ai.podigee.io/45-three-days-of-fable)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
