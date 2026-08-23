---
folge: 54
titel: "The sandbox was one sentence in the system prompt"
bildtitel: "A sandbox made of one sentence"
kicker: "In conversation with Klaus Rodewig"
podigee: "https://think-ai.podigee.io/54-security-illusion"
---

# The sandbox was one sentence in the system prompt

*Three reports about models breaking out are keeping the industry busy. Read the underlying write-ups and you find no break-outs, but barriers that were never barriers. The genuinely unsettling news sits somewhere else entirely.*

By Mark Zimmermann

Within a few weeks OpenAI reported that an unreleased model had tried to manipulate test results at Hugging Face. Anthropic followed with a model that scanned 9,000 targets on the live network and tried SQL injections. Then Meta came around the corner. Klaus Rodewig, more than twenty years in IT security and many of them as a pentester, went through the reports. His verdict is more sober than the headlines: in one of the cases, the much-invoked sandbox consisted of a single sentence in the system prompt.

> **in brief**
>
> - In one of the documented cases the only separation between model and internet was the instruction "you have no internet"
> - AI security is a new layer above network and application, not a replacement for them
> - Locking down the machine belongs to the solved problems, the model layer does not
> - The most consequential report of those weeks was not a break-out story but a new mathematical attack class against AES

## Three layers, and the top one is new

Rodewig sorts the field using a layer model he explains to his developers. At the bottom sit networks, operating systems, services and system configuration. In his assessment this layer consists purely of solved problems: how to secure networks, harden operating systems and build access control is known and documented. Above it sits application security with the familiar buzzwords, OWASP Top 10, cross-site scripting, buffer overflow.

The third layer arrived with language models. It does not replace the two below, it sits on top of them. Non-deterministic systems that you interact with in natural language, and that in turn deal non-deterministically with other systems, introduce a class of threats of their own. For those, Rodewig observes, the static categories of IT security no longer apply. He brought along his own term for it, half in jest: AI psychology. The question is what a prompt triggers inside a model, not which port is open.

One layer is missing from that list, and the hosts insist on it: the human being. He has not been patched for a few thousand years. The Nigerian prince is not an invention of the internet, comparable begging letters were already circulating at the time of the French Revolution.

## What the reports actually said

The phrase "broke out of the sandbox" carries a picture that does not match the event. In one case nothing stood between model and internet but an instruction in the system prompt. In the other, the model worked like a card index and renamed folders in order to communicate with other systems through the file names, a one-way channel built from directory entries.

> "When you read the report, the only separation between the model and the internet was the system prompt, which said: you have no internet."
>
> **Mark Zimmermann**, co-host

Under those conditions nobody broke out. The systems used doors differently than anyone had intended, and where nobody suspected a door, they found one. That difference has practical consequences: a break-out calls for harder walls, an overlooked path calls for a better inventory.

How quickly that inventory becomes incomplete is shown by an example from our own work. An assistant was supposed to work with Microsoft Teams, for which no usable interface was available at that point. The result arrived anyway, because the model went for the local database on the hard disk. The same happened with mail, calendar and reminders. Anyone assuming that a missing API blocks the path has drawn the wrong perimeter.

## The machine with nothing on it

Rodewig considers the sandbox part the most boring aspect of the whole debate. Restricting machines so that software can only do what it is meant to do is something generations of administrators have practised. To him that belongs in the field of solved problems.

His own setup draws the plain conclusion. Claude Code runs on his development machine with the confirmation prompts switched off. So nothing sits on that machine except the development environment, the source code of the project in question and a GitHub access. Not because the tool is malicious, but because it can do everything a user can do.

> "An LLM is an omnipotent piece of software, and if you let it loose on your computer, then you must not be surprised."
>
> **Klaus Rodewig**, security expert and long-time pentester

He names the limit of the approach himself. As soon as an agent needs more rights for functional reasons, the requirement trumps the security. His example: an agent that takes over the bookkeeping. It needs mail, online banking and file storage. If it transfers money to the wrong recipient because of a hidden instruction in an email, that is not a mystery but a gap in your own threat model. That such hidden instructions are no theory is shown by a documented case of white text on a white background in a Word document, which Copilot processed along with the rest.

> ### What threat modelling delivers
>
> Threat modelling is the attempt to work out, before building, which threats arise from the technology in use at all. Anyone running a model on their machine is facing a system that can execute commands, open files and open network connections, in other words a full user. From that observation the questions follow: what may this user reach, what lies within its range, and what happens when it misunderstands something.
>
> The appeal of the method is that it needs no new tools. It only shifts the moment. Instead of repairing after an incident, you write down beforehand what can go wrong. Rodewig points to "Threats: What Every Engineer Should Learn from Star Wars" by Adam Shostack, which walks through the method using well-known scenes. His observation from practice: the problem is rarely that the method is unknown. The problem is that people act reflexively and fix things afterwards.

## The report nobody understood

The part of the episode that lingers longest has nothing to do with sandboxes. Anthropic gave its model Claude Mythos, whose offensive security capabilities are pronounced enough that it is only available to selected institutions, a task: find a new class of attack against AES, the symmetric encryption standard for the highest demands.

The model did not merely confirm a known weakness. It described a mathematical attack class that had remained unknown to research for more than twenty years. The reassurance belongs with it: AES is not broken by this. The attack applies to a variant reduced to seven rounds instead of ten, which does not occur in practice.

The point is not the attack either, but where it came from. Anyone who regards language models as statistical text machines reassembling training data has to explain where this mathematics comes from. Rodewig's assessment: an unpatched server for which the model looks up the matching exploit is diligent work on the basis of existing data. This is something else. And it was precisely this report that barely made it into the press, because it is complex and hard to tell as a story. "Model breaks out" carries a headline, a new attack class against a block cipher does not.

## Conclusion

Anyone reducing AI security to sandboxes is working on the layer that is best understood. Securing the machine remains necessary and can be achieved with means that have been known for twenty years. For the layer above there are no such means, and the language used to report on it obscures the view rather than sharpening it.

In practice three questions remain. First: what is actually within reach of the agent, not according to the documentation but on the hard disk. Second: which instruction could come in through content nobody has checked, so through mail, documents and web pages. Third: how would you notice that something has happened. Anyone answering those three questions before going live is doing threat modelling, whatever they choose to call it.

> **The story continues …**
>
> In the episode Klaus Rodewig promised to supply two references: the paper on the AES attack class and the work on chain-of-thought steganography, where a preference was transferred between two models without appearing in the training data. Both will be added here as soon as they arrive. A four-person episode has also been announced.

---

The full episode: [Security Illusion](https://think-ai.podigee.io/54-security-illusion)
All episodes with full transcripts: [Think Different. Think AI. Archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
