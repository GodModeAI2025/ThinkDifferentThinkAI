---
folge: 47
titel: "Loop engineering: why the goal has become more important than the prompt"
bildtitel: "Goal instead of prompt"
kicker: "Article on the episode"
podigee: "https://think-ai.podigee.io/47-loop-engineering"
---

# Loop engineering: why the goal has become more important than the prompt

*A loop receives no command but a goal, measurable success criteria and the instruction to check itself. That works, but it has a blind spot: a system that assesses itself assesses itself well.*

By Mark Zimmermann

Two or three years ago the question was who writes the best prompt. By now it is who builds the best loop. Andrej Karpathy recently made public that he considers loop engineering more important than prompt engineering, and that matches what is happening in practice.

The route there ran in stages. At the start stood a prompt database in Notion, that is a collection of formulations that had worked once. Then came skills: markdown files with sub-skills and executable Python code that an agent loads when needed. The step to the loop is the third and changes the human role more than the two before it.

> **in brief**
>
> - A loop receives a goal and success criteria, not a single assignment
> - It checks itself and repeats until the criteria are met
> - The checking belongs with a different model: whoever assesses themselves confirms themselves
> - Run times of 10 to 20 hours for one task have become normal
> - With the number of parallel loops, context management becomes the actual bottleneck

## What separates a loop from a prompt

The definition is brief and carries a long way.

> “We define a prompt that instructs the system: what is my goal, what are my very concrete criteria by which I establish that I am reaching my goal. And the system continuously checks whether the goal has been reached, and repeats itself until the goal is reached.”
>
> **Mark Zimmermann**, co-host

The difference lies in the shift of responsibility. With a prompt, the human describes the route and judges the result. With a loop, the human describes the goal and the yardstick, and the machine looks for the route.

That also shifts the human's work. It no longer lies in the formulation but in the question of how you actually recognise success. That is a specification task, and it is more uncomfortable because it permits no vague goals. “Do this well” is not a success criterion. “All ten test cases pass, and the report names each individually with its status” is one.

> ### Why loops of all things
>
> The term seems surprising at first, because loops are among the oldest constructs in programming. What is new is what sits inside the loop.
>
> Text generation itself is already a loop: the model predicts a token, appends it and starts again. Loop engineering sits one level above that. There, what sits in the loop is not a token but a complete work step with tool calls, and the stopping condition is not a character limit but a domain criterion.
>
> In practice such a loop needs three specifications: the goal, the verifiable criteria and an upper bound. Without the upper bound, the loop either runs into a quota or produces side effects nobody ordered.

## The blind spot: self-assessment

The most important warning in the episode concerns the check. Anyone letting a system assess its own work generally gets agreement back.

That is not malice on the machine's part but a consequence of how the assessment comes about. The same model with the same context that produced a solution considers it correct on review, because it brings the same assumptions along. An error that went unnoticed during generation goes unnoticed during checking as well.

The way out is organisational, not technical: the result is checked by a different model. Peter Steinberger has publicly described the approach along with the token consumption it incurs, and the consumption is the price for it.

A proven sequence looks like this: first have a plan drawn up, then have the plan checked by a critic skill and a meta-analysis skill, then start the implementation as a goal loop. That such a run takes 10, 12 or 20 hours is not a fault but the operating mode.

## Harness engineering becomes the bottleneck

The more agents and loops work in parallel, the less the model decides and the more the frame decides. Two topics stand out.

The first is context and memory. A loop running for hours has to know what applied earlier and must not start from scratch at every restart. How quickly context is lost was shown by the short-notice shutdown of a model: what sat in its sessions was gone. Everything that is meant to survive belongs in your own, vendor-independent store.

The second is governance. As soon as skills contain executable code and agents access company systems, the usual questions arise: who may put a skill into circulation, how is it signed, how can it be traced afterwards what an agent did. These questions are not new, they are known from software distribution. What is new is that they now apply to text files any business unit can write.

A terminological distinction is worthwhile: a harness is the frame in which agents work, that is tools, context, rules and checking. An agentic OS would be a level above, with resource management and scheduling across competing agents. What is being built today are harnesses.

## Conclusion

Loop engineering is not a new technique but a relocation of care. It moves from the formulation to the specification, and it is better placed there, because specifications survive a model change.

Three rules are enough to start. Define the goal so that a machine can check whether it has been reached. Have the checking done by something other than what did the work. And set an upper bound before you start the run.

It is not about impressing with as many tokens as possible. It is about defining a clear goal and leaving the route there to the machine.

> **The story continues …**
>
> The question of auditability in enterprise use remains open. Signed skills, traceable agent logs and an approval chain for executable instructions are currently largely manual work. Until standards exist for this, the same applies as with macros twenty years ago: whoever collects and checks them has less work later.

---

The full episode: [Loop Engineering](https://think-ai.podigee.io/47-loop-engineering)
All episodes with full transcripts: [Think Different. Think AI. archive](https://godmodeai2025.github.io/ThinkDifferentThinkAI/)
