# Announcing  NeurIPS 2025 E2LM Competition: Early Training Evaluation of Language Models

source: https://huggingface.co/blog/tiiuae/e2lm-competition
published: Fri, 04 Jul 2025 12:25:00 GMT

#
[
](https://huggingface.co#announcing--neurips-2025-e2lm-competition-early-training-evaluation-of-language-models)
Announcing NeurIPS 2025 E2LM Competition: Early Training Evaluation of Language Models

[Team Article](https://huggingface.co/blog)

Join us in building benchmarks that capture early-stage reasoning & scientific knowledge in LLMs!

The development of Large Language Models (LLMs) typically begins with a series of ablation experiments, wherein various model architectures, data mixtures, and training hyperparameters are systematically evaluated. This phase is commonly referred to as the early stages of training. During this period, researchers primarily monitor two key metrics: the training loss curve and evaluation scores. However, existing evaluation benchmarks often fail to provide meaningful or discriminative signals during these initial stages where LLMs are trained on a few tokens ~200B tokens, making it challenging to derive conclusive insights from ongoing experiments.

In this competition, we want to build together new benchmarks to effectively capture relevant signals in early training stages of LLMs, specifically for scientific knowledge domain.

##
[
](https://huggingface.co#how-to-participate)
How to participate

The competition will be hosted on a dedicated Hugging Face organization - to register to the competition please follow this registration link 👉 [https://e2lmc.github.io/registration](https://e2lmc.github.io/registration).
Participants will have to submit their solutions, which will be based on [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) library through a HuggingFace Space. An active leaderboard will be maintained during the competition to track promising submissions.
The size of the models make them easily runnable for everyone, on free-tier Google Colab GPUs. We also provide [a comprehensive starting kit](https://e2lmc.github.io/starter_kit) including several notebooks to get started with the competition.

##
[
](https://huggingface.co#evaluation-metrics)
Evaluation metrics

Each submission will be evaluated using three different scores: *signal quality score (Score SQ)*,

*ranking consistency score (Score*amd

RC)*compliance with scientific knowledge score (Score*. These criteria will be combined into a global score used for the final ranking. Additionally, two validation procedures will be systematically applied to all submissions: (i) verification of alignment with established scientific knowledge domains, and (ii) detection of potential information leakage, specifically the presence of the answer within the question prompt.The overall score is computed as a weighted sum:

CS)SQ+ α2 × Score

RC+ α3 × Score

CS

where, αSQ, αRC and αCS are weighting coefficients that reflect the relative importance of each
criterion. We set the weights as α1 = 0.5, α2 = 0.1 and α3 = 0.4, thereby placing greater emphasis on signal quality and compliance to scientific knowledge, which we consider the most important metrics in evaluating submissions.

Participants will be able to compute the signal quality subscore locally using the provided model checkpoints of three Small Language Models 0.5B, 1B and 3B (ranging from 0 to 200 BT) along with the accompanying scoring algorithm (provided in a notebook in the starting kit). In contrast, the other two subscores cannot be computed independently, as the corresponding checkpoints—from 200 GT to 1 T tokens, as well as the 0.5 billion parameter model trained exclusively on web data—will remain hidden throughout the competition. Nonetheless, the global score will be automatically computed upon submission through the Hugging Face competition space, allowing participants to track their overall performance. This setup is intended to prevent overly customized solutions specifically tailored to the released checkpoints.

Further details about each evaluation metric, along with full scoring results on state-of-the-art benchmarks, are available in [the competition proposal](https://arxiv.org/abs/2506.07731)

##
[
](https://huggingface.co#competition-timeline)
Competition timeline

Competition kick-off |
14 July 2025 |
Warm-up Phase |
14 July 2025 - 17 August 2025 (5 weeks) |
Development Phase |
18 August 2025 - 26 October 2025 (10 weeks) |
Final Phase |
27 October 2025 - 03 November 2025 (3 weeks) |
Results Announcement |
04 November 2025 |
Winners' Fact Sheets & Code Release Due |
22 November 2025 |
NeurIPS Competition Workshop Presentation |
6 or 7 December 2025 |

##
[
](https://huggingface.co#prizes)
Prizes

- 🥇
**1st Place**: 6,000 USD - 🥈
**2nd Place**: 4,000 USD - 🥉
**3rd Place**: 2,000 USD - 🎓
**Student Awards**: 2x 2,000 USD for the top 2 solutions submitted by participants justifying a student status

##
[
](https://huggingface.co#support-and-contact)
Support and contact

For inquiries and support, reach out to the task coordinators at [e2lmc@tii.ae](mailto:e2lmc@tii.ae). You can also join our discord channel [here](https://discord.gg/9aYU5fA4) to directly interact with us.

##
[
](https://huggingface.co#affiliated-institutions)
Affiliated Institutions

|
|
|
|
|
|