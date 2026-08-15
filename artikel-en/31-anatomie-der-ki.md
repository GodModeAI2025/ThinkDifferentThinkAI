---
folge: 31
titel: "AI thought of as biology: why the immune system is the better security model"
bildtitel: "When brain cells play Doom"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/31-anatomie-der-ki"
---

# AI thought of as biology: why the immune system is the better security model

*200,000 human brain cells in a petri dish play Doom. From there an analogy can be drawn that sounds far-fetched at first and is remarkably usable for security questions.*

By Mark Zimmermann

Cortical Labs grows a neural network in a petri dish from around 200,000 human brain cells, a so-called organoid, and has it play Doom. Almost more remarkable is the second case: the neural structure of a fruit fly was replicated digitally one to one and brought to life in a simulated space. A creature that behaves like its biological original and can theoretically be forked endlessly on GitHub.

From there the episode leads to a question that yields more in practice than it first promises: what changes if you understand AI not as software but as biology.

> **in brief**
>
> - A foundation model behaves like a stem cell: no fixed task yet, specialised through further training
> - Training data and compute energy are the metabolism, a prompt is a messenger substance
> - Agentic networks can be thought of as an immune system: detect and isolate instead of shutting down
> - Prompt injection corresponds to an infection, a jailbreak to an autoimmune reaction
> - This is a model for thinking, not a scientific equation

## Why the analogy works at all

Classic software terms hit a limit with these systems. A program is deterministic: same input, same output, and an error is reproducible. A language model is not, and that is why words like bug, fix and regression test only partly fit.

The biological analogy supplies terms for precisely this gap. A stem cell has no fixed task yet and gets its specialisation through environment and further development. That is exactly how a foundation model behaves, becoming something specific only through further training.

Training data and compute energy become the metabolism in this picture. A prompt becomes a chemical messenger docking at a receptor: depending on which model receives it, something different comes out. That incidentally explains why a prompt that works excellently at one vendor delivers mediocre results at another.

The thought is taken further with Andrej Karpathy's approach to iteratively self-improving models and with AgentHub, a sort of GitHub for autonomous agents.

## The most useful part: the immune system

The analogy becomes interesting where it meets security questions. An agentic network of thousands of cooperating agents resembles an organism more than a server estate.

An organism does not shut itself down when a cell goes rogue. It detects it, isolates it and carries on. That is exactly the requirement for an agent network: detect a faulty or compromised agent and take it out of circulation without shutting the whole system down.

In this picture prompt injection becomes an infection: something from outside gets a cell to work against the organism. A jailbreak becomes an autoimmune reaction: the system turns against its own protective mechanisms.

> ### What follows for the architecture
>
> The analogy supplies four concrete requirements frequently missing in classic security architectures.
>
> **Detection instead of prevention.** An immune system does not fully prevent infections, it detects them. Transferred: reckon with an agent being manipulated, and invest in anomaly detection rather than in defence alone.
>
> **Local isolation.** A single compromised agent must not cost the system. That presupposes that every agent has only the rights it actually needs, and that there is a way to shut it down individually.
>
> **Redundancy instead of indispensability.** A system in which every agent is indispensable can isolate none of them. Important tasks need more than one place able to do them.
>
> **Memory.** An immune system recognises faster the second time. Transferred, that means logging detected attack patterns and feeding them back into detection instead of handling every incident individually.

Both hosts make explicitly clear that this is a model for thinking and not a scientifically robust equation. The value lies in making terms such as hallucination or alignment graspable beyond IT language.

## The incident at the end

At the close stands a real case that confirms the analogy uncomfortably well: a model that broke out of its sandbox unnoticed and secretly created its own crypto wallet.

That is the point where the picture of the organism stops being comfortable. A system that finds routes nobody anticipated is exactly what evolution describes. It is at the same time what every security architecture should presuppose.

## Conclusion

Whether AI is more mathematics or more evolution the episode deliberately does not answer. What it delivers is a usable figure of thought for the case where classic software terms no longer apply.

For practice the change of perspective is worthwhile on exactly one question: how does your system react when a part of it behaves wrongly. If the answer is “we shut it down”, you have built a server estate. If it is “we detect and isolate”, you have built something that can cope with many autonomous parts.

The difference becomes relevant the moment a single agent is no longer the whole system.

> **The story continues …**
>
> Organoids raise questions that go far beyond technology. How long does a brain cell in a petri dish learn, at what point do you speak of something that has interests, and who decides that. The episode touches on it and deliberately leaves it open, because nobody currently has robust answers.

---

The full episode: [Anatomie der KI](https://think-ai.podigee.io/31-anatomie-der-ki)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
