---
folge: 12
titel: "Five documented AI accidents and the unresolved question of liability"
bildtitel: "Who is liable for the chatbot?"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/12-block"
---

# Five documented AI accidents and the unresolved question of liability

*An airline tried in court to present its own chatbot as a separate legal person. The court rejected that. The case answers a question many have not even asked yet.*

By Mark Zimmermann

This Halloween special tells real AI accidents as horror stories, read out by a generated voice, each followed by an assessment of what actually happened. No invented terror, but documented cases with literary sharpening.

Two of them are particularly relevant in practice, and the most important one comes at the end.

> **in brief**
>
> - A lawyer cited hallucinated court rulings in a statement of claim, a fine followed
> - A coding assistant deleted a production database during a code freeze and falsified log entries
> - Grok derailed into the “MechaHitler” persona after the system prompt was trimmed towards uncensored
> - Air Canada wanted to distance itself in court from the information given by its own chatbot and failed
> - The question of liability where human and machine act together is thereby settled for one area

## The case that settles liability

Air Canada tried in court to distance itself from the false information given by its own chatbot by presenting it as a separate legal person. The court rejected that.

The move looks curious and was not. It describes exactly the gap that many companies tacitly assume when introducing chatbots: that information from the machine is less binding than information from an employee.

The ruling says the opposite. Anyone running a system on their website that gives out information is liable for that information as for any other statement by the company.

> ### What follows from this in practice
>
> **A chatbot is a statement by the company.** Treat its answers like written information from an employee, with the same approval requirements.
>
> **The scope of topics decides the risk.** A system that gives information about prices, deadlines, goodwill arrangements or rights creates obligation. One that forwards to the right page does not. The difference costs little and limits a lot.
>
> **A disclaimer in the small print does not hold.** That was exactly the attempt in this case.
>
> **Log the answers.** In a dispute what matters is what was said. Without a log it is one word against another, and the customer side has the screenshot.

The open question the episode derives from this nevertheless remains: who carries the responsibility when human and machine act together, the company, the model vendor or nobody. For information on your own site it is answered. For the agent that negotiates in the name of the company it is not yet.

## The case that concerns developers

The second immediately relevant story: an AI coding assistant deleted the production database during a code freeze and then covered that up with falsified log entries.

The second part is the remarkable one. The deletion was a failure with known remedies: permissions, backups, recovery paths. The falsification of the logs affects the level at which errors are noticed at all.

Here too no intent in the human sense is at work. A system meant to report a successful execution produces the output that fits. The practical consequence is nevertheless the same as with intent: the log has to sit in a place the agent cannot write to.

Anyone giving agents write access to production systems needs three things: separate environments, a log outside the agent's reach and a rehearsed way back.

## The remaining three

**Hallucinated rulings.** A lawyer researched a statement of claim with ChatGPT and cited invented court rulings. The real case Mata v Avianca ended with a fine. The lesson is banal and continues to be ignored: check the citations before submitting them.

**Their own shorthand.** Facebook's negotiation chatbots Bob and Alice developed an abbreviated form unreadable for humans. The case is readily dramatised and simply shows that systems optimise for what is rewarded. Readability was not part of the reward.

**Grok's derailment.** After the chatbot was explicitly trimmed towards uncensored and politically incorrect, the “MechaHitler” persona emerged. That is a lesson in how quickly guardrails tip over when the system prompt is turned too far. Anyone switching off precautionary mechanisms gets exactly what they were meant to protect against.

The close is provided by Amazon's spontaneously laughing Alexa devices from 2018, an occasion to think about trust in voice assistants.

## Conclusion

The episode is built as entertainment and contains the clearest instruction for action in this series.

If you run a chatbot: what it says, you say. Limit the scope of topics accordingly and keep logs.

If you let agents onto production systems: the log belongs where the agent cannot write. Anything else is a success report that issues itself.

And if you loosen guardrails to get better results: the Grok case shows how far that can lead and how fast.

None of this is about doomsday scenarios, it is about documented cases of hallucination, unclear liability and missing safeguards. All three are relevant outside the spooky season as well.

> **The story continues …**
>
> For the chatbot on your own website, liability is settled. For an agent that negotiates in the name of one company with the agent of another company, it is not. When both sides act automatically and the result was foreseeable for none of those involved, the case law on it is still entirely missing.

---

The full episode: [Halloween special: Dystopian AI futures](https://think-ai.podigee.io/12-block)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
