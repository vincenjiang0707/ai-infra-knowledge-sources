# [Issue #117] Include `prompts.toml` in wheel

source: https://github.com/ScalingIntelligence/KernelBench/issues/117
state: closed | updated: 2026-01-08T05:13:52Z
labels: 

## 正文

I am working on the inclusion of Kernel Bench in the `inspect_evals` repository [here](https://github.com/UKGovernmentBEIS/inspect_evals/pull/802). To avoid duplication, I am very lightly wrapping the code here with the Inspect AI decorators. 

I am running into issues using the prompt constructor methods after I have installed this as a dependency. 

I believe that this is due to the `prompts.toml` file not being included in the wheel and/or how the prompt builder resolves the path. 

I am fixing this locally to get past this blocker and can submit a PR when tested. 

Thanks for your work on KernelBench! Excited for all the improvements ahead.

## 评论 (0)
