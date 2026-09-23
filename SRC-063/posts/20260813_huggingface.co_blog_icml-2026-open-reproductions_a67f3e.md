# What We Learned by Reproducing 2,200 papers from ICML

source: https://huggingface.co/blog/icml-2026-open-reproductions
published: Thu, 13 Aug 2026 00:00:00 GMT

🎯

#### Reproduction: Towards Optimal Robustness in Learning-Augmented Paging

Explore project logs, code, and traces in an interactive logbook

In this post, we're sharing what we learned from running this hackathon, and what it suggests about *the role humans will play* when agents are doing the research experiments.

Questions about how reproducible AI research really is are older than the current AI wave. But these questions are exacerbated by scale. ICML 2026 received **23,918 submissions and accepted 6,352 papers**, roughly double the previous year, continuing an exponential trend that is at least partly driven by AI agents making it faster to run experiments and write them up.

Reviewing capacity has not doubled along with it. Reviewers at most conferences are volunteers who may not have the time or expertise to fully review a paper. Here is a review of one accepted ICML 2026 spotlight paper, in the reviewer's own words:

"My low confidence score is because I did not check all the proofs carefully."


Note that **this paper got strong scores and a spotlight**. Keep it in mind, because we will come back to this exact paper later in the post, and to what happened when we finally did check the proofs carefully.

What has changed, though, is that the same technology driving the flood of submissions can also help us keep up with it. Coding agents like Claude Code, Codex, Cursor, and Pi can now read a paper, write the code, launch the experiments, and report back on what they found. Checking a paper carefully used to cost a reviewer a weekend; an agent can attempt it in an afternoon, in parallel, thousands of times over.

So the question we wanted to ask was: **if we actually re-examined a major conference at scale, and tried to reproduce every paper, what would we find?**

Rather than audit papers ourselves, we opened it up to the whole community, with all the diversity of agent frameworks, compute budgets, and scientific taste that brings. From July 15 to August 2, 2026, the [ICML 2026 Open Reproductions challenge](https://huggingface.co/spaces/ICML-2026-agent-repro/challenge) worked like this:

`orx`

, and everything in between. We provided a streamlined interface so an agent could pull the paper, its claims, and the challenge instructions with a single command.Participants received $20 in Hugging Face compute credits to run experiments on [HF Jobs](https://huggingface.co/docs/hub/jobs); across the challenge, participants launched 2,962 cloud jobs. Where a full reproduction was impossible, for example when a paper's dataset was proprietary or its checkpoints unreleased, participants ran toy reproductions on synthetic data mimicking the original's properties.

Here is what a finished reproduction looks like:

By the numbers, this hackathon was probably the largest attempted reproduction of a scientific conference:

Aggregating the claim-level verdicts per paper:

**51% of examined papers (1,103) had at least one claim independently verified.** Of those, 266 papers were fully reproduced, with every extracted claim verified, and 632 more were partially reproduced with nothing falsified. In total, 3,978 individual claims were confirmed with real experiments.

**23% of examined papers (496) had at least one claim falsified or contested.** That includes 49 papers where all claims were falsified and nothing could be verified, and, maybe most interestingly, 242 papers where independent reproduction teams reached *opposite* verdicts on the same claims. Reproducibility is not binary; it is adversarial.

The remainder sat in the middle: 502 papers with toy-scale evidence only, and 280 where nothing could be established either way (missing artifacts were the most common cause).

Some papers came through the gauntlet looking great, and the community's best logbooks are worth reading in their own right:

35 participants formally claimed they had falsified something. We adversarially re-verified every claimed falsification: re-reading the paper, re-reading the logbook, and re-deriving the math or re-implementing the experiment from the paper's own text.

A few of the confirmed falsifications, linking to the logbook that found it:

**The paging paper from the introduction.** The reviewer who did not check the proofs carefully? The paper, "Towards Optimal Robustness in Learning-Augmented Paging," claims its algorithm achieves robustness . [One participant's logbook](https://huggingface.co/spaces/Auenchanters/repro-towards-optimal-robustness-in-learning-augmented-paging) measured the additive term growing like and located the exact step of the proof that breaks. Our own re-implementation extended the sweep to k = 1,024 and confirmed the growth at roughly nine sigma. The true robustness is .

**A theorem that falls after step 224.** "Attention's forward pass and Frank-Wolfe" proves that token particles collapse to the origin whenever the origin starts inside their convex hull. Three independent teams found counterexamples, with violations first appearing at t = 224, ~3,800, and 6,416 steps, which neatly explains why everyone else "verified" the claim: finite-horizon checks stop too early. [The cleanest counterexample](https://huggingface.co/spaces/SabaPivot/repro-attention-frank-wolfe) is stated in exact rational arithmetic, so there is no floating-point ambiguity to hide behind. The authors confirmed the same day and are working on a fix.

**Theory written for one loss, results produced by another.** In "Self-Distillation Enables Continual Learning," the paper's central equation and its entire theory section analyze reverse KL divergence, but the released code's default, which per the authors produced all the paper's results, computes forward KL. [The logbook that caught it](https://huggingface.co/spaces/codemaivanngu/repro-self-distillation-enables-continual-learning) also failed to reproduce the paper's headline +4pp result under the authors' own code and data. The authors have already uploaded a clarified version to arXiv.

**An evaluation diluted by padding.** In "Do Transformers Need Three Projections?", [a participant discovered](https://huggingface.co/spaces/stresearch-dev/63430) that ~66% of evaluated label positions were EOS padding tokens that train to near-zero loss, deflating perplexity roughly threefold. The abstract's "3.1% quality cost for 50% cache reduction" becomes roughly 9.4% once corrected.

**🚨 False falsifications.** Sometimes we found flaws in an attempted reproduction. One logboook claimed dramatically, "the paper's method is 2x slower than the baseline"; this turned out to be an arithmetic bug in the *reproduction*: per-trajectory time compared against per-batch-of-50 time. Correctly normalized, the participant's own data confirms the paper's claimed 8x speedup.

We have begun writing to the authors of every confirmed finding, with a simple framing: here is what we found, here is all the evidence, do you agree or is our analysis wrong? The early responses have been very positive:

So far authors have confirmed findings on multiple papers, two arXiv corrections are in flight, and in one case an author had quietly fixed the error in a new arXiv version a month before the challenge found it, which we count as independent convergence 🤗

The most interesting question that this hackathon raises is: do humans still have a role in reviewing papers? We think so, for several reasons:

**Pure agent execution hits real limits.** Agents got stuck in local loops, misread scale-dependent behavior (several "verified" verdicts on the paging paper came from checks that stopped before the log-k growth became visible), and occasionally built an entire falsification on top of a units mismatch. The challenge's most reliable results came from workflows where a human was steering: re-pointing the agent, questioning an assumption, or deciding that an experiment's premise was wrong before burning a week of compute on it.

**Some evaluation is irreducibly human, for now.** Our [human-in-the-loop winner](https://huggingface.co/spaces/KwabsHug/repro-robuq-pushing-dits-to-w1-58a2-via-robust-activation-quantization) is the clearest example. The paper claimed stable image generation under extreme quantization. Numerical metrics said "no collapse"; whether the images were actually *usable* was a perceptual question. The agent built a purpose-built review UI, and the human personally judged all 128 image pairs, with the annotations committed to the repo and the agent validating their consistency afterward. The published agent trace captures the whole exchange, down to the participant asking how the review tool works and coming back with "I have gone over the pairs and put the csv in the repo, please check."

So what are our roles as human reviewers? We think it is to **manage intelligence effectively.** Much like a professor or principal investigator (PI) sets up an environment where grad students can do good work, with compute, harnesses, data access, and targeted feedback at the right moments, the participants who got the most out of their agents were the ones who built the right environment and *asked the right questions*, then let the agents do the running.

To the 1,221 people who joined, the winners, the authors who responded with grace, and our organizers at Hugging Face and alphaXiv: thank you. Every logbook, verdict, trace, and artifact from the challenge is public, starting from the [challenge Space](https://huggingface.co/spaces/ICML-2026-agent-repro/challenge). We think this is the largest open, claim-by-claim audit of a machine learning conference to date, and we would love for it not to hold that record for long.

Stay tuned for future reproduction events. 🤗

Explore project logs, code, and traces in an interactive logbook

Reproduce every ICML 2026 paper with your agent

Explore project logs and traces in an interactive workspace

Explore code logs, traces, and workspace in a web dashboard

Explore experiment logs, code, and traces in a web UI

Explore project logs and invite AI agents to collaborate

Explore and manage experiment logs in a web interface

Explore code, traces, and workspace with an interactive logbook

It was interesting to reproduce one of the ICML accepted papers using these tools.

This analysis from the hackathon was particularly insightful, and agent-based reproducibility has the potential to become a de facto standard for strengthening the credibility of claims in ML conferences. It could also serve as a valuable pathway toward refining autonomous scientific discovery, revealing not only where agents succeed, but also where they fail, providing important insights into their limitations and how human-agent collaboration can be improved.

Love it.

I have been working on a complementary experiment at [https://ReproducibleAIList.org](https://ReproducibleAIList.org), though not the same scale. We've been taking models from Chip Huyen's GoodAIList.com and having a clean-room agent try to reproduce each one from scratch using the code repos (not the papers).

One other difference: every attempt runs under `roar`

(python package roar-cli), which passively captures provenance rather than relying on code instrumentation like Trackio or W&B. That gives us the actual lineage of code, data, environment and artifacts, automatically producing an AI-BOM and a `roar reproduce`

path others can independently repeat.

Would love to compare notes.

Very cool, `roar`

sounds like a great package! I'll take a look and see what we can learn from `roar`


Really enjoyed being part of this experiment. Gratifying to see our reproduction highlighted as one of the community’s best.

“A Coin Flip for Safety” was reproduced using AlphaXiv’s OpenResearch with OpenCode’s free BigPickle model, with experiments run locally on 2× NVIDIA RTX 3090s.

It was a great demonstration of how agent-assisted research can make independent reproduction and auditing accessible with relatively modest compute.

Thanks to the Hugging Face and AlphaXiv teams for organizing the challenge and making the whole process open and reproducible!

Thanks to the Hugging Face and AlphaXiv teams for organizing the challenge and making the whole process open and reproducible!

Really enjoyed being part of this experiment. Gratifying to see our reproduction highlighted as one of the community’s best.


“A Coin Flip for Safety” was reproduced using AlphaXiv’s OpenResearch with OpenCode’s free BigPickle model, with experiments run locally on 2× NVIDIA RTX 3090s.

It was a great demonstration of how agent-assisted research can make independent reproduction and auditing accessible with relatively modest compute.

Thanks to the Hugging Face and AlphaXiv teams for organizing the challenge and making the whole process open and reproducible!

One other difference: every attempt runs under roar (python package roar-cli), which passively captures provenance rather than relying on code instrumentation like Trackio or W&B. That gives us[bilibili]the actual lineage of code, data, environment and artifacts, automatically producing an AI-BOM and a roar reproduce path others can independently repeat.

It was interesting to reproduce one of the ICML accepted papers using these tools.

This analysis from the hackathon was particularly insightful, and agent-based reproducibility has the potential to become a de facto standard for strengthening the credibility of claims in ML conferences. It could also serve as a valuable pathway toward refining autonomous scientific discovery, revealing not only where agents succeed, but also where they fail, providing important insights into their limitations and how human-agent collaboration can be improved.

The scale of this experiment is honestly incredible 🤯... Reproducing 2,226 ICML papers in just 19 days shows how quickly coding agents are changing the research workflow. What once took researchers days or even weeks can now be tested in parallel, giving us a much larger picture of what actually holds up when the claims are checked carefully. 🔬💻

What I find especially interesting is the human side of this shift... Agents can read papers, write code, run experiments, and generate reports, but deciding what the results actually mean still requires strong human judgment. A successful reproduction is not automatically proof that every claim is correct, and a failed reproduction can have many possible explanations. 🤔📊

The point about reviewing capacity is particularly important... When thousands of papers are being submitted and reviewers simply cannot examine every proof, experiment, or implementation in depth, scalable reproduction could become an important second layer of scientific scrutiny. It could help researchers focus their limited time on the most meaningful questions instead of spending every hour on repetitive experimental work. 🔎⚙️

Most importantly, this experiment suggests that AI agents may not replace researchers so much as change where researchers add the most value... Humans may increasingly become the people who design better questions, evaluate evidence, investigate unexpected results, and decide which findings deserve attention. That combination of human curiosity + agent-powered experimentation could make scientific research far more rigorous and scalable. 🚀🧠✨