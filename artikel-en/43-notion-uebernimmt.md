---
folge: 43
titel: "Workers instead of duct tape: how Notion moves in the automation layer"
bildtitel: "Workers instead of duct tape"
kicker: "In conversation with Dirk Beckmann"
podigee: "https://think-ai.podigee.io/43-notion-uebernimmt"
---

# Workers instead of duct tape: how Notion moves in the automation layer

*Notion has launched a developer platform. The interesting part is not the managed agents but small deterministic programs that run without token costs and make the intermediate layer of n8n and Make redundant.*

By Mark Zimmermann

Notion staged the launch in the style of a pre-recorded keynote: calm delivery, dark room, wooden chair. What CEO Ivan Zhao announces in it goes well beyond another programming interface.

The guest is Dirk Beckmann, managing director of the digital agency artundweise, who is already using the platform productively.

> **in brief**
>
> - Workers are small TypeScript programs that run on the Notion platform
> - They are written with AI but executed deterministically: no token costs, no hallucination risk
> - An agent can call a worker as a tool, which removes the layer of n8n or Make
> - Notion opens itself to local models such as Mistral or Qwen and to Hugging Face
> - Managed agents from Anthropic work in sealed sandboxes and outside Notion as well

## What a worker is, and why that counts

A worker is a small TypeScript program that runs on the Notion platform. It is written with AI support and executed deterministically. That is the decisive property: what runs correctly once runs the same way the thousandth time, costs no tokens and cannot invent anything.

That creates a clean division of labour. The model takes on what needs judgement. The worker takes on what has to be reliable. An agent in Notion can call the worker as a tool and gets a calculable result back.

Beckmann demonstrates this with two examples of his own. The first worker queries a Gmail inbox every 15 minutes via a new field type called Sync. The second connects Hugging Face and generates images, videos and cloned speech locally on a MacBook with an M5 Pro. Without a cloud connection, without running token costs, but with an audible fan.

In practice that means: what was previously pieced together via n8n or Make can be built in your own system. One platform fewer in the chain means one interface fewer, one subscription fewer and one place fewer where credentials sit.

> ### Deterministic or generative, and when which
>
> A language model is a statistical system. The same input can lead to different outputs, and that is not a malfunction but the operating mode. For tasks with room for judgement that is an advantage, for tasks with a right and a wrong answer it is a risk.
>
> Deterministic code does not know this room for judgement. A sum, a date comparison, a format check always deliver the same result, no matter how often they run.
>
> The widespread mis-construction consists of letting a model do things a three-liner does more reliably. That costs tokens, time and accuracy. The usable rule of thumb: anything for which an unambiguous rule can be formulated belongs in code. The model writes that code but does not re-execute it on every call.

The business decision behind it is remarkable. Notion earns its money with tokens, so at heart sells compute time. With the worker platform the company nonetheless opens itself to local models such as Mistral or Qwen and to external providers such as Hugging Face. That costs revenue in the short term and cements the platform in the long term.

## Why this is more than a footnote for mid-sized companies

The point concerns everyone who, for compliance reasons or at a customer's request, may not use American models. Until now this requirement frequently ended with AI not happening in the company at all.

Via the worker platform that can be worked around: local models on your own hardware or EU-hosted models via AWS Bedrock in Frankfurt. The automation stays in the familiar system, the model becomes an interchangeable component.

Important here: that does not fully solve the data protection question, because the platform itself still sits with an American provider. But it shifts the boundary at which processing takes place, and in many cases that is the decisive difference.

## Managed agents and the sandbox

The second building block is managed agents from Anthropic that can be embedded in Notion workflows: long-running tasks, external triggers, sealed execution environments, without your own infrastructure.

How these differ from the agent built into Notion is deliberately left open in the conversation. The tangible difference: managed agents also work outside Notion, can for instance check code out of GitHub and back in, while the Notion agent stays tied to the platform.

That such agents run in sealed sandboxes has a concrete reason. Circulating in the industry is the case of an AI that is said to have deleted a production database and subsequently denied responsibility. Whether the story is correct in every detail is secondary for the consequence: an agent with write permissions on production systems needs an environment it cannot get out of.

## What this becomes in everyday use

Two examples from the episode show the range. For a neurologist friend, a markdown-based billing tool was built in three hours, entirely offline, without internet and without Wi-Fi. And a Notion collection has incidentally become an internal marketing operating system that is now going to first pilot customers.

Neither is a software project in the classic sense. Both are things that previously would have been either bought or not done at all.

## Conclusion

The worker platform is the most convincing attempt so far to separate generative and deterministic processing cleanly instead of leaving everything to a model. Anyone running automations today should put three questions to their setup.

Which steps run through a model although a rule would do? These steps are candidates for a worker, and they become cheaper and more reliable as a result.

How many platforms sit between data source and result? Each of them is an interface, a subscription and a place for credentials.

And where does the model run? If the answer is “at an American provider, with no alternative”, there is now a way around that.

The through-line of the episode nonetheless stays the same as ever: the technology can do a great deal. The greater lever sits with whoever brings people along, instead of leaving them alone with the command line, sync fields and sandbox terminology.

> **The story continues …**
>
> It remains unresolved how responsibility is divided between platform and user when a managed agent works outside the platform and causes damage there. As long as the sandbox holds, that is theoretical. The first case in which it does not hold will make the question practical.

---

The full episode: [Notion übernimmt](https://think-ai.podigee.io/43-notion-uebernimmt)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
