# [Issue #1226] Request for AdamW8bit support on CPU (would help TorchTune)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1226
state: closed | updated: 2026-05-08T17:21:51Z
labels: Intel, Cross Platform, x64 CPU, Optimizers

## 正文

### Feature request

Port AdamW8bit support for CPU from `multi-backend-refactor` branch to the main branch 

### Motivation

Public cloud providers' machines with GPUs are usually expensive while datacenter-grade CPUs are more readily available at lower prices. Towards the goal of making Deep Learning more accessible to developers & learners, the ability to finetune with AdamW8bit on CPU seems like a good milestone. `TorchTune` is currently unable to support[ full fine-tuning on CPU with `AdamW8bit`](https://github.com/pytorch/torchtune/blob/main/recipes/configs/llama3/8B_full_single_device.yaml) because it uses `bitsandbytes`' AdamW8bit optimizer.

<strike>#898 enabled `AdamW8bit` for CPU in `multi-backend-refactor` branch, but the main branch doesn't have it. </strike>

It'd be great if we could enable AdamW8bit for CPU in bitsandbytes main branch before TorchTune's next release (provided there would be a `bitsandbytes` release before that), so that users who'd install TorchTune would automatically end up installing a version of `bitsandbytes` that'd support `AdamW8bit` on CPU.

Thanks!

### Your contribution

@jianan-gu could port over his code from multi-backend-refactor branch to the main branch.

cc @mingfeima @ashokei @TimDettmers 

## 评论 (6)

### sanchitintel · 2024-05-28

<strike>#1220 will fix this issue.</strike>

### matthewdouglas · 2024-05-29

> #1220 will fix this issue.

I don't recall seeing any optimizers implemented yet for CPU, but may be mistaken.

Paged optimizer doesn't make sense to me for CPU, but I can understand the request for AdamW8bit.

### sanchitintel · 2024-05-29

Thanks for pointing that out, @matthewdouglas! I've revised the description.

@jianan-gu @xia-weiwen, please clarify if you had added `AdamW8bit` implementation for CPU to `bitsandbytes`. If not, do you have plans to add it? Thanks!

### Xia-Weiwen · 2024-05-29

@sanchitintel Yes, we are going to do it. cc. @jianan-gu @jiqing-feng

### Titus-von-Koeller · 2024-06-03

@sanchitintel thanks for raising this. When is the next torchtune release foreseen?

Hmm, the problem is that the device abstraction / dispatcher situation is still not stable. Things will change fundamentally in the next 3 weeks. Not sure if this can be done as a PR to `main` in isolation? @Xia-Weiwen could you sketch out a bit more how you think this would make sense?

### matthewdouglas · 2026-05-08

Resolved by #1901.
