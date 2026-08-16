---
folge: 11
titel: "Spec-Driven Development: when the patch becomes the blueprint for the exploit"
bildtitel: "The specification comes first"
kicker: "In conversation with Klaus Rodewig"
podigee: "https://think-ai.podigee.io/11-ki-schreibt-code-menschen-prufen-nach"
---

# Spec-Driven Development: when the patch becomes the blueprint for the exploit

*A security update has always been a pointer to where the hole was. Until now it took days of reverse engineering experience to build an attack from it. Today minutes are enough.*

By Mark Zimmermann

Klaus Rodewig is a long-standing security specialist and penetration tester, and he describes his path from sceptic to user. He has delivered a complete software project almost exclusively with AI: embedded C on a Raspberry Pi part plus a Flutter desktop application, commissioned in small pieces and tried out model by model.

The opening is a mishap with recognition value: an outage in the AWS zone us-east-1 knocks out Perplexity, while in the background the worry circulates that a forgotten n8n workflow with a valid access token might be charging the credit card right now.

> **in brief**
>
> - Switching model does not help when the problem lies elsewhere: all of them failed at the same systemd filter
> - Spec-driven development: requirements in Gherkin, tests first, then code
> - One model changed a variable name on its own authority for weeks, with no explanation even when asked
> - Language models disassemble binaries without symbols into readable C code
> - A published security update can be turned into an exploit in minutes

## Where all models fail alike

The most instructive part of the field report concerns a limit. A simple filter problem with systemd and journalctl was solved reliably by neither Claude nor Gemini, no matter how often they were asked again.

That is the most important finding for everyone who switches model when things get difficult. When several models fail at the same point, the problem is not the model. It lies in there being little good material on the topic, or in the task being stated imprecisely.

The curious anecdote that also describes a serious pattern fits with this: for weeks a model changed a variable named “Fahrzeugkontrolle” into “Fahrzeugkontrolk” on its own authority. Without explanation, not even when asked.

Silent changes of that kind are the reason why every output should run through version control. A mistake you can see is harmless. One sitting among two hundred lines is not.

## Spec-Driven Development

The thread running through the episode is an approach that turns common practice around.

> ### How it works
>
> Instead of commissioning vaguely, requirements are broken down into small specifications, written in Gherkin, the Given-When-Then notation from behaviour-driven development.
>
> Example: *Given* a user is logged in, *When* they place an order over 500 euros, *Then* an approval is requested.
>
> From these specifications you have **tests written first** and **only then** code. The code is finished when the tests pass.
>
> The gain lies in an unexpected place. Writing the specification forces the clarification of questions that get skipped when commissioning directly: what happens at exactly 500 euros, what with stand-ins, what with cancellations. Otherwise a model answers those questions itself, silently.
>
> And the tests do not come from the same pass that produced the code. That sidesteps the basic problem of self-assessment, without a second model being necessary.
>
> GitHub SpecKit pursues the same approach.

## The security part

Rodewig extends the line consistently into security, and this part is the most unsettling of the episode.

Language models can disassemble binaries without symbol information and translate them back into readable C code. For audits that is practical: you can check what a piece of software actually does, even without source code.

For patch cycles it is a problem. A published security update has always been a pointer: anyone comparing the version before with the version after sees what was repaired, and with it where the hole was. Until now it took days of experience to build a working attack from that. With diffing and model analysis it takes minutes.

The practical consequence affects everyone who ships software: the window between the release of an update and its installation at the customer has become the critical period. Anyone with monthly maintenance windows has a month of open window.

## Rulebooks, machine-readable

At the end the subject is MISRA C, the coding standard for safety-critical automotive software, and the Cyber Resilience Act, which from 2027 brings binding security requirements for connected products.

Both are hundred-page rulebooks that can be translated into machine-readable specifications and enforced directly at the point of commissioning. That is one of the most convincing applications there is: rules nobody holds fully in their head become a precondition instead of a check at the end.

## Conclusion

Rodewig's assessment is unexcited and pointed: you do not become unemployed through AI, but by ignoring it.

Three points follow for your own work. Do not switch model when several fail at the same point. Look for the error in the way the task is stated instead.

Write specifications before the code and have tests created from them first. That is the most effective known protection against results that look good and are wrong.

And reckon with your security updates being read as a blueprint. Anyone who has lived off reverse engineering being laborious has lost that protection.

> **The story continues …**
>
> The Cyber Resilience Act takes effect from 2027. That hundred-page rulebooks can be translated into specifications a model observes while generating is one half. The other is the evidence presented to an authority, and the formats for that are still missing.

---

The full episode: [KI schreibt Code, Menschen prüfen nach !](https://think-ai.podigee.io/11-ki-schreibt-code-menschen-prufen-nach)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
