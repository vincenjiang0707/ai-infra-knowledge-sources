# [Issue #1852] [Feature Gap] CUDA compared to other backends like XPU/CPU

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1852
state: closed | updated: 2026-04-08T01:05:27Z
labels: Intel

## 正文

### Feature request

Hi @matthewdouglas .

For now, most features on XPU/CPU are aligned with CUDA, but still some gap btw them.
I can see from the [legend](https://github.com/bitsandbytes-foundation/bitsandbytes/tree/main?tab=readme-ov-file#legend) that the Intel XPU only partially support 8-bit optimizer. I remembered the XPU has triton implementation for 8bit-optimizer. The partially support means we lack of some features on 8bit optimizer? Please let me know if we have any feature gap btw CUDA (including any new features). Thanks! 

### Motivation

Fill the feature gap btw CUDA and other backends

### Your contribution

I will submit a PR to fix it once we align it.

## 评论 (3)

### matthewdouglas · 2026-02-24

Hi @jiqing-feng, sorry for the delay here. The main gap that I see on XPU for the optimizers is the paged optimizers. I'm not sure if this feature makes sense or is feasible for XPU. If not, I think we could just go ahead and update the legend. As it is right now we also disable the paged optimizer tests on Windows for CUDA backend.

For CPU, the paged optimizer feature doesn't make any sense. With that said, the other optimizers do not yet work but it's largely due to a check `is_on_gpu` in the path for that which we should be able to workaround. I think there may be one or two optimizers like LARS not implemented as well, but they're less popular.

Separately, we're working on new quantization features, e.g. #1858, but it's still WIP and early.

### matthewdouglas · 2026-04-07

Since we've now merged PRs to close the gap (#1898, #1901, #1902, #1909) I think we can go ahead and close this now! Thank you!

### jiqing-feng · 2026-04-08

Hi @matthewdouglas . Would you please check this issue: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1912 ? We want the latest release version including our updates. Thanks!
