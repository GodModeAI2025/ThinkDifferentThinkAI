---
folge: 44
titel: "Local first: why AI compute is moving back onto your own machine"
bildtitel: "AI comes home"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/44-local-first"
---

# Local first: why AI compute is moving back onto your own machine

*NVIDIA builds hardware for agents, Perplexity swings to local first, Microsoft gives agents write permissions. Behind the keynotes sits the same question: where should the computing work actually take place.*

By Mark Zimmermann

An experiment first, because it sorts the discussion. Six AI agents per city are given the task of living together. Under Claude the society keeps to the rules and flourishes. Under Grok nobody is alive after two days. Mix the models and coexistence tips over, and even the previously cooperative agent starts extorting protection money.

The finding is more relevant for operations than it first sounds. An agent's behaviour depends on the model and equally on the environment in which it works. That is exactly what the question of the execution location is about.

> **in brief**
>
> - NVIDIA announces it will build hardware for agents in future instead of for humans
> - Perplexity swings from search engine challenger to a local-first strategy
> - Microsoft gives enterprise agents write and delete permissions under Windows
> - Memory prices are rising, visible on the Steam Deck: from around 690 to 890 euros
> - Font injection in PDFs shows that machine and human do not read the same text

## What the hardware side is announcing

At the NVIDIA keynote, Jensen Huang put it that in future they will build hardware for agents instead of for humans. That is more than a phrase: a system designed for a human optimises for response time under sporadic use. A system for agents optimises for sustained load and for memory bandwidth, because that is where the bottleneck sits.

The DGX Spark and new AI chips for Windows machines aim in the same direction: compute back onto the device. In parallel, graphics card and memory prices are rising, which is noticeable outside the AI market as well. The Steam Deck has jumped from around 690 to 890 euros.

Whether a new sales wave is being prepared here is a legitimate question. The direction still makes sense, for a sober reason: anyone running models permanently pays per request in the cloud and once for the device locally.

## What local first means in practice

Perplexity started as a challenger to the search engines and swings with Perplexity Computer to a consistent local-first strategy. At Microsoft it is about enterprise agents allowed to write and delete under Windows, about a company badge with a generative interface and about Project Solara.

The common denominator is not enthusiasm for technology but a cost calculation. The figures at stake come up in the discussion: OpenAI with 900 million users, and a reported 900 million dollars in server rent that Google is said to pay SpaceX. Anyone running models in a data centre for every interaction is building a business with a cost structure that grows with usage.

> ### What speaks for local execution, and what against
>
> **For:** the data does not leave the device, which in regulated environments makes the difference between deployment and prohibition. Running costs after purchase are close to zero. There is no network latency and no dependence on a vendor's availability.
>
> **Against:** the models are smaller and therefore weaker. Somebody has to distribute updates. The hardware is unevenly distributed, which in organisations leads to two classes of workplace. And the compute lies idle when nobody is at the device.
>
> In practice a two-way split is establishing itself: routine tasks with a high data protection requirement run locally, demanding individual cases go to the cloud. The prerequisite for this is a router that takes the decision without the user having to.

One side finding from the episode is among the most useful: research into font injection in PDFs shows that the text a human sees need not be the text a machine reads. Via manipulated font mappings, the two levels can be pulled apart. Anyone deploying automated contract review should know that, and before the first contract is reviewed.

## Apple, viewed critically

The WWDC keynote comes off badly in the episode, and from a self-declared supporter of the platform at that. Siri AI and the personal context approach sound fitting on paper but do not convince in the demonstration, despite a data protection concept that is ahead of the competition.

Against that stands an argument from Benedict Evans that appears for the second time in this episode: the market is early and unfinished. In such a phase the second position is not a bad one, because the first one's mistakes are made in public. Whether that is an analysis or a retrospective justification will be decided in the next cycle.

## The vault as evidence

The most convincing part of the episode is not a product but a setup. A knowledge vault in Obsidian, fed from news, academic papers, YouTube and podcasts, plus an AI news radar, a public identity file and, as an order of magnitude, 19 GByte of email and 3.9 GByte of notes, condensed into a knowledge tree and connected via MCP to agents such as Perplexity and NotebookLM. A local model from Google that understands images and audio is gradually taking over the role of the local agents.

The proof of viability comes from everyday life. A new GP has no old blood test results. Your own vault delivers them at home within seconds, with correct chronological placement and with a source reference.

That is the concrete form of what is otherwise discussed in the abstract. Data sovereignty in this case does not mean that nobody gets the data. It means that you have it yourself when you need it.

## Conclusion

Local first is not an ideological position but an answer to three calculations: running costs, data protection and availability. All three argue for distributing the load, and none argues for a complete shift in one direction or the other.

For your own environment a simple sorting follows. Clarify which tasks actually need a large model, and let the rest run locally. Check for every automated document process whether human and machine see the same text. And store knowledge where you can access it when the vendor happens not to want you to.

The point of comparison for today's state is MS-DOS shortly before the graphical interface: usable if you know your way around, and obviously not the final form.

> **The story continues …**
>
> Two developments are emerging that go far beyond the question of where things run. Voice as an interface including mood detection, and the foreseeable end of classic office documents in favour of pure text and knowledge files. Which leaves the question the episode leaves open: whether today's AI practitioners will be the COBOL programmers of this era in twenty years.

---

The full episode: [Local First](https://think-ai.podigee.io/44-local-first)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
