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

## 评论 (5)

### simonguozirui · 2026-01-07

Thanks for flagging this and @AffectionateCurry for looking into this. We typically use KernelBench as a git submodule, so the path resolution assumed the repo structure was always present. When installed as a pip dependency, `the prompts.toml` file wasn't being included in the package and the path resolution was breaking.

We'll add a fix in the our PR that includes the `.toml` in package-data and uses `importlib.resources` for path resolution so it works both as a submodule and as an installed dependency


### jiito · 2026-01-07

Sweet. Thank you! Was just about to open a pr with those changes—let me know if that would be helpful. Otherwise, please let me know when it's merged. Thanks again!

### AffectionateCurry · 2026-01-07

Ah yes if you already have the pr ready feel free to open it and we can reference it for ours! 

We will let you know when we merged the pr and let us know if there are still problems that come up!

### simonguozirui · 2026-01-08

We put the fix in #105! Let us know if the problem still persists. 

### jiito · 2026-01-08

Will do! Thank you 🙏
