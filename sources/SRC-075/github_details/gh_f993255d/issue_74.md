# [Issue #74] [Roadmap] Fall 2025 KernelBench Maintenance + Improvement Plan

source: https://github.com/ScalingIntelligence/KernelBench/issues/74
state: open | updated: 2026-04-15T12:34:07Z
labels: documentation, enhancement, good first issue, help wanted

## 正文

This fall, the KernelBench team will continue to maintain and improve the repo. This issue serves as a roadmap and a document that we might continue to update. If you have concrete feature requests, please post them below or ideally open an issue on the repo.

We have a fantastic group of Stanford undergrads: @AffectionateCurry @nathanjpaek @pythonomar22 @Marsella8 as core maintainers, with @ethanboneh on RL framework integration. We very much welcome community contributions in these directions (we try our best to review the PRs). Thank you to @alexzhang13 @hqjenny for the feedback.

### Goal & Motivation 
KernelBench has quickly become _the standard_ for evaluating LLM Kernel Generation capabilities. As pointed out by many others in the community and we found in our [follow-up work](https://arxiv.org/abs/2507.11948), there are aspects of the benchmark that could be improved to make it a more valuable tool for the community. We already started with this over the summer with [KernelBench v0.1](https://scalingintelligence.stanford.edu/blogs/kernelbenchv01/) by @AffectionateCurry @nataliakokoromyti  @anneouyang.

Ultimately, We want to make KernelBench **easy** (push-button eval), **usable** (easy to integrate), and **referenceable** (compare across various approaches)

Overall Milestone
- **Milestone 1:** By October (SF GPU mode hackathon), resolve all previous PRs and Issues (at least have an answer regarding it)
- **Milestone 2:** Various integrations with community project for future research directions (RL, evolutionary search, more languages) and for people to experiment with various approaches
- **Milestone 3:** Create a Referenceable, Reproducible Pipeline

We hope we could have an update/announcement by early Dec / NeurIPS.

Below are the concrete goals and (tempororay) assignments. We will try our best to realize all of these features, but we make no guarantees. **We would love to welcome community contributions!**

### **Milestone 1**:  Improve KernelBench itself

- [x] Collect community feedback on how we can improve KernelBench 
- [ ] Go through all the current issues & PRs on KernelBench repo. For Issues, reply them. For PR, close them, merge them, or abandon them, make a decision
- [x] Refactor Codebase to make them easier to play with (including LiteLLM Integration #78, better dataset object #71, use TOML-based prompt template #85, #114, #111) @pythonomar22 @AffectionateCurry 
- [ ] Robust and realistic shapes (Llama shapes) and correctness eval.
- [x] Implementations on different ways to do timing eval, such as do_bench, host_side timing, cache clearing. w @Marsella8 @PaliC @simonguozirui  #89 
- [ ] Writeup / Blog to understand and showcase the difference between do_bench, ncu profiling, cuda event through benchmarking guide + blog #106 
- [x] Create adversarial tests (cache attacks, zero mean, low overhead, etc) @bkal01  #82 
- [x] Create checks against reward hacking #110 
- [x] Precision Support #80 
- [ ] Create variable shape inputs [sweep across shapes]
- [ ] Create a SoL roofline model (theoretically max speedup on input shape and hardware spec) [high priority]
- [ ] Detail study of Torch Compile and new default as baseline for Level 2 and 3 baseline @PaliC 
- [ ] Potential New Problems and Workloads @nathanjpaek @simonguozirui 

### **Milestone 2**:  Framework Integration 
- [x] Curate a doc of how KernelBench has been used and various approaches tackling it. 

DSL (NVIDIA hardware) support.
- [x] ThunderKittens @Willy-Chan @willhu-jpg  #101 #104 #107 
- [x] Triton @PaliC @AffectionateCurry #35 
- [x] CuTe @nathanjpaek #35 
- [x] TileLang Support @nathanjpaek @AffectionateCurry  #80 
- [ ] CUTLASS support
- [ ] Helion Support

Alternative Hardware platform support. 
- [ ] AMD HiP Support
- [ ] Google TPU support

RL and Search Framework Integration. See #73 for detail. 
- [ ] RL env integration @ethanboneh @nataliakokoromyti 
- [ ] OpenEvolve Search integration @ethanboneh 

### **Milestone 3**:  Referenceable, Reproducible Pipeline
To make KernelBench an actual standard, led by @pythonomar22 @AffectionateCurry 
- [x] Easy-to-use CoLab notebook #93 
- [x] Create a Modal-based (cloud executable) Pipeline for standard evaluation #83 and #100 
- [ ] Create a leaderboard of frontier model performance
- [ ] Create a project website

## 评论 (2)

### jhinpan · 2025-11-10

Hi Simon, Appreciate all your hard work first! KernelBench is indeed really powerful and useful. This summer I interned at AMD and used KernelBench to integrate RL framework [slime](https://github.com/THUDM/slime), post-training on both AMD and NV framework. The project is named as [TritonForge](https://github.com/RLsys-Foundation/TritonForge), inspired by [Kevin](https://cognition.ai/blog/kevin-32b). Please let me know if there is anything that I can help on RL and AMD framework integration!

### pengchengneo · 2026-04-15

Hi, I’m a developer from SGLang, focusing on TPU backend training and inference. I'm interested in migrating KernelBench to the TPU platform and adding support for JAX and Pallas. May I take ownership of this part?  @simonguozirui 
