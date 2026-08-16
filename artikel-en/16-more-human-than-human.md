---
folge: 16
titel: "Energy instead of compute: the real currency of AI power"
bildtitel: "Energy is the currency"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/16-more-human-than-human"
---

# Energy instead of compute: the real currency of AI power

*In one study GPT-4.5 passed as human in 73 per cent of cases. More interesting than the number is the question of what a test still measures at all, and who can afford the data centres for it.*

By Mark Zimmermann

The starting point is Ridley Scott's “Blade Runner” and the Voight-Kampff test, which recognises replicants by their missing emotional micro-reactions. The question behind it is a practical one: can the classic Turing test still fulfil that role today.

The numbers say no. In an inverted experiment of our own, ChatGPT took its human counterpart for a human in 86 per cent of cases. In one study GPT-4.5 passed as a human conversation partner in 73 per cent of cases.

> **in brief**
>
> - GPT-4.5 was taken for a human in 73 per cent of cases
> - Benchmarks suffer from data contamination like exams with leaked answers
> - Small language models need different metrics: power consumption instead of world knowledge
> - Deepfake videos currently give themselves away at the pulsing artery on the forehead
> - Energy, not compute, is the scarce resource

## Why benchmarks say little

The technically most important part of the episode concerns measurement. Benchmarks for language models have the same problem as exams with leaked answers: data contamination instead of reasoning performance.

The mechanism is simple. A benchmark is public so that it is comparable. What is public ends up in the training material. A model that knows the tasks solves them well, without it following that it solves similar tasks.

For practice that means a high benchmark score is a weak argument. The robust test is your own unpublished set of tasks from your own field of application. The effort for that runs to a day and replaces every leaderboard discussion.

> ### Why small models need different metrics
>
> A large language model is measured by world knowledge and breadth of tasks. For a small language model running locally on a device, those are the wrong quantities.
>
> What counts there is **power consumption** per request, because the device has a battery. **Memory footprint**, because it determines the hardware. **Latency**, because the very purpose of local execution is the short response time. And **reliability in a narrow area** instead of breadth.
>
> A model that only understands voice commands for home automation does not need to know the history of the Roman Empire. It has to understand reliably and must barely consume any energy while doing so.
>
> The widespread practice of measuring small models against benchmarks for large ones therefore leads systematically to wrong conclusions. They score badly in disciplines that are irrelevant to their purpose.

A concrete identifying feature comes from a conference report by the Fraunhofer Institute: anyone wanting to expose deepfake videos currently watches the pulsing artery on the forehead, a detail that video generation does not yet get right cleanly. The word “yet” carries the weight here.

## Concentration of power and its currency

The second strand of the episode is the more far-reaching one. Access to the best models increasingly decides success, in small ways with homework, in large ways with the question of which states can afford data centres and the energy they need.

The decisive observation: energy, not compute, is the real currency. Chips can be bought, if you can get hold of them. The electricity to run them for years cannot be imported like hardware.

That shifts the question of location. Whoever has cheap and reliable energy becomes the site for data centres, regardless of where the development takes place. That is a question of industrial policy and it is discussed as a question of technology.

As a possible counterweight the episode brings in open-source models and the European regulatory debate, combined with a warning about a cyberpunk-like dissolution of familiar power structures, as described in novels such as “Neuromancer”.

## From thinking to personhood

At the close it becomes fundamental. When agentic systems made of several specialised models work together like an organism and machines simulate or develop emotions, the question shifts. “Can a machine think?” becomes “Whom do we accept as an equal person?”.

Using the Deckard and Rachel scene, both hosts show why a pure Turing test is no longer enough for that and why an empathy test would be the next stage.

Note that such a test would have the same problem as the original one. It measures whether something is perceived as empathetic, not whether it is empathetic. That is exactly where the Turing test failed, and the numbers above show how thoroughly.

## Conclusion

Two practical consequences and one fundamental one can be drawn from this episode.

Practical: build your own unpublished test set for your use case and measure models against it instead of against leaderboards. And measure small models by consumption, latency and reliability in a narrow area, not by world knowledge.

Fundamental: if energy is the scarce resource, the question of AI sovereignty is less a question of models than of infrastructure. A country without surplus electricity can afford models and no data centres to train them.

That models pass as human today is the least surprising news in all this. They are trained on human text. That they sound human is the fulfilment of the specification and no indication of anything beyond it.

> **The story continues …**
>
> If deepfakes are recognisable by the pulsing artery, that is a matter of months. Detection methods resting on a single technical shortcoming age quickly. Only methods that start not with the image but with its provenance remain robust: signatures, recording chains, verifiable sources.

---

The full episode: [More human than human.](https://think-ai.podigee.io/16-more-human-than-human)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
