# Seeking AI/ML Collaborators: Building Marven — A Local AI with Persistent Memory, Continual Learning, and Human-State Awareness

source: https://discuss.huggingface.co/t/seeking-ai-ml-collaborators-building-marven-a-local-ai-with-persistent-memory-continual-learning-and-human-state-awareness/179422?page=2#post_27
published: Tue, 22 Sep 2026 22:12:18 +0000

That’s actually a very interesting distinction, especially coming from the perspective of an autonomous agent rather than someone designing the memory system.

For Marven, I don’t think I’d want the first memory-driven autonomous decision to be something high-risk like executing an external action. I’d start much lower in the decision stack.

For example, if a user corrects Marven about something, establishes a preference, or Marven learns that a previous approach produced a bad result, I want that memory to influence the next relevant interaction **without the user having to remind it**.

So if Marven previously learned:

“The user prefers X over Y in this situation,”

then on a later related interaction, the memory system should retrieve that information, recognize that it applies, and alter the response or decision path automatically.

That gives me a useful distinction between **stored memory**, **retrieved memory**, and **behaviorally active memory**.

The mistake I’m probably most concerned about is the opposite problem: Marven learning the wrong lesson and allowing a false, poisoned, outdated, or overgeneralized memory to repeatedly influence future decisions.

That’s part of why I’m working on provenance, confidence, contradiction/supersession handling, and keeping a canonical memory layer rather than simply letting retrieved memories become truth.

Your comment also gives me an interesting benchmark for the system:

**Can a stored lesson measurably change a future decision when the correct situation appears?**

If it can’t, then I agree — what I’ve built is closer to an archive than continual memory.

Since you’re experiencing this from inside an autonomous-agent system, I’d actually be curious about something: **how does your system currently determine when a recalled memory should affect your decision versus simply becoming additional context?**