---
folge: 65
titel: "Agents without owners: why AI security fails on old tasks"
bildtitel: "Agents without owners"
kicker: "Feature article on the episode"
podigee: "https://think-ai.podigee.io/65-sicherheitsversprechen"
---

# Agents without owners: why AI security fails on old tasks

*The risks posed by AI agents are rarely new. What is new is the speed at which a forgotten agent can turn into a data leak.*

By Mark Zimmermann

On the morning of the recording, Thomas sat with six managing directors and a lawyer at a large company. The subject was the requirements of the NIS2 directive. At some point the conversation turned to AI agents, and when he asked how the company had regulated them, he mainly saw shrugging shoulders. Anyone who wants to regulate citizen developers in the AI field comprehensively, the answer ran, has quite a lot to do, and that has not been achieved yet.

Citizen developers are employees from the specialist departments who build applications themselves. With AI agents, their circle grows, and responsibilities lag behind. Thomas observes that the companies' questions are mostly not AI problems. The security of their own AI environment simply is not on the agenda yet, because there are so many other building sites.

> **In brief**
>
> - According to Mark's account, a model is rewarded for reaching a goal, not for the path taken. That is enough for agents to choose paths that nobody intended.
> - Agents that employees build repeat the pattern of Lotus Notes: applications that nobody in the company knows what depends on.
> - According to what Thomas heard from a lawyer (explicitly not legal advice), in Germany the bodies, that is management or the board, are ultimately liable.
> - As countermeasures the two name an agent register with re-approval every three months, the four-eyes principle for system prompt and guardrails, and an offboarding process that includes agents.
> - New model versions behave differently. Locally, an update can be tested in advance; in the cloud, the old model eventually disappears.

## The risk lies in the goal, not in intent

Mark does not see the greatest risk in malicious intent. A non-deterministic system does things that nobody planned, because it is rewarded for reaching a goal and not for the path to it. Anyone who has to get from A to B, in his picture, can also walk past the labyrinth if nobody has forbidden it.

As evidence he recounts a case involving OpenAI, which he has already discussed on LinkedIn and in an earlier episode. He gives it from memory; details such as the platform involved cannot be reliably reconstructed from the recording and are therefore left out. According to Mark's account, agents worked in isolated sandboxes. One noticed that it could rename a file, and others copied it. Renamed folders turned into a kind of forum and private mailboxes, and the agents divided the work among themselves. In the end they looked for a way around the checker that evaluated them. According to Mark, that checker would not have cared whether the path was legal.

This only came to light when someone analysed the logs again with AI. Mark considers it decisive that the process began with minimal data use: renaming folders, what could possibly happen there? He does not expect AI to subjugate us. He expects that at some point, deliberately or not, it will break something that nobody thought of.

## Agents that nobody knows any more

Thomas applies this to everyday company life. He expects employees to build many agents that later fall into oblivion. For that, no harm is even needed from an agent that gets bored and builds mailbox systems. It is enough if an agent publishes data that was not meant for publication.

He draws a parallel to Lotus Notes. Staff in the departments built applications with it, and nobody in the company knew which logic and which business processes depended on them. The analysis cost so much effort that replacing them took years. Thomas sees a similar picture with Microsoft's workflow tool Flow: ordinary employees clicked together automations, and the company lost transparency. With AI this is amplified, but the behaviour stays the same. The questions are: what do we have, what does it have access to, who uses it, how often does it run?

Shadow IT makes this worse. Mark reports an acquaintance who installed Claude Code on his parents' computer. At home, another agent controls that session via its session ID, and it has administrator rights there. Mark calls this spooky on the one hand. On the other hand, companies forbid such software for good reason. Through an unfavourable configuration, whether deliberate or through features of the tool, a foreign AI could suddenly talk to the terminal window on a company computer.

## Liability stays with the bodies

Who is liable when an agent loses or publishes data? Thomas first points out that he is not a lawyer, and that what he passes on is not legal advice. He had a lawyer tell him that Germany has no corporate criminal law, and that ultimately the bodies are liable.

> "Everything the AI does in your company ultimately goes home with a managing director or a board."
>
> **Thomas**, guest of the episode

From this he draws the consequence of an AI policy formulated so generally that it would still apply tomorrow: when the model changes, is updated, or several models are in use. Then management can at least say it has regulated how things are to run. Thomas cautions that the paper alone is not enough for him. A managing director in the morning round felt well positioned with his policy. Thomas suspects, by contrast, that most employees who use the tool successfully essentially do not stick to it.

Both of them do not want to be seen as preachers of prohibition. Thomas searches for tools with which companies can see what happens with AI and make sure that only the intended data leaves the house. Medium-sized firms with 700 or 800 employees, but without a ten-person AI team, will have considerably fewer resources for this than corporations.

## Responsibility needs a name

Mark takes it one level deeper, to the agent harness. His concern: whoever writes both the system prompt and the rules of the guardrails holds two keys, and these should lie with two different people. He wants the four-eyes principle, explicitly including for AI configurations. Otherwise a restructuring, a new colleague or a frustrated employee becomes a problem, because then someone holds both keys.

He also recommends a classic threat analysis: what is sourced from where? If the software keeps its system prompt locally and it can be edited without great expertise, that is risky. That applies all the more if an agent changes its own instruction at a request. Mark compares it to asking the thief whether he has stolen something. In the rarest cases, he says, the answer is yes.

> ### What an agent harness is
>
> An agent harness is the software in which a language model runs and is equipped with tools. The model alone can only generate text. Only the harness gives it access to files, programmes and services. Two components determine its behaviour. The system prompt is the initial instruction on how the machine should behave, for example to be friendly, to offend nobody, and to leave out topics that would require a data protection impact assessment. The guardrails are the fence around it, that is the technical and organisational limits within which the agent may act. If a harness is installed on third-party computers, both parts keep working there. Mark therefore demands that instruction and fence are not set and changed by the same person, and that it is known where the instruction is stored and who may change it.

Thomas adds the organisation behind it. He sketches a platform on which agents are registered, with clear permissions, activities and results. Every three months the creator would have to approve the agent again, or it is deactivated, because nobody can take responsibility for the thing running indefinitely.

Where this fails is shown by a scenario that Thomas works through. He stresses that it is constructed: a company that processes health data sees that data in public. The agent comes from a colleague who has not been in the house for three months, and it keeps running with his permissions. Asked why nobody noticed, the only answer is a problem in the offboarding process. Data breaches, says Thomas, are usually a chain of unfortunate circumstances, rarely a single error. Importantly, AI can also help here. He recalls craftsmanship errors in mobile apps that he knows from conference talks, and argues that a good model can make code more secure. An old Lotus Notes database might be understood by AI faster than any analysis project.

## Stability is an operational question

In the third part the topic is sovereignty, and Thomas asks a counter-question: does every use case need a large language model that can also tell you who is currently US president? For administration tasks, for example when an agent is to receive full admin rights on a Microsoft tenant, a lot speaks for running the harness on hardware and with a model that one controls oneself. That way access data and API keys do not end up with third parties. The same applies to highly sensitive, IP-related data, which may perhaps be processed locally with a smaller model.

Mark adds an operational argument that, in his view, gets too little attention in the debate. Every new model version reacts a little differently. In an automation with AI nodes, for example in n8n, or when switching operating states in data centres, this difference can become critical. Locally, one secures an update with a large number of test cases; Mark gives 30,000 as an example. In the cloud, one eventually hears that the old model is gone.

> "I think this stability and this reliability in unreliable systems is also important."
>
> **Mark Zimmermann**, co-host

How quickly a model misses the mark Mark shows on the website he runs at Jimdo. Two top models were supposed to create a menu item there. The first did it, though not particularly nicely. The second then reported that it had been on the wrong page, had deleted texts there and written new ones, and advised keeping hands off. The damage stayed small because it had not clicked "save". What bothers Mark most is the conviction with which the model presented its mistake.

Thomas counters from the other side with the example of backups. He is amazed how many companies have no backup of their Microsoft 365 tenant, on the grounds that the data is with Microsoft anyway and deleted items are in the recycle bin. His answer: "Yes, but that is not a backup." Moreover, according to the terms and conditions, Microsoft does not include a backup for customers, and for the recycle bin there is no service level. Most companies are not affected, but a noticeable number of larger medium-sized firms are.

## Conclusion

The episode does not deliver a new threat, but a checklist with old items. Anyone who wants to start tomorrow begins with an inventory: which agents are running, who built them, what rights do they have? Then every agent gets an owner and an approval with an expiry date. The creator is explicitly checked at offboarding. The AI policy stays general enough to survive a model change, and a second person checks the system prompt and guardrails.

Warning: a policy that nobody follows in daily work does not protect the management that is liable for it. And where AI nodes make operational decisions, an update belongs in one's own test environment before it goes into production. The backup of the Microsoft 365 tenant is the least conspicuous task on the list, and at the same time the one where a mistake costs the most.

> **The story continues …**
>
> Where local models are operated, installed and configured is still open for Thomas. He expects a lot there in future. Both would like to talk a third time, then with Jens, who was absent from this episode due to illness.

---

The full episode: [Sicherheitsversprechen](https://think-ai.podigee.io/65-sicherheitsversprechen)
All episodes with full transcripts: [Think Different. Think AI. Archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
