# [Issue #1483] moe_lb_loss should be divided by gradient_accumulation_steps for reporting.

source: https://github.com/AI-Hypercomputer/maxtext/issues/1483
state: closed | updated: 2026-04-28T18:16:14Z
labels: 

## 正文

https://github.com/AI-Hypercomputer/maxtext/blob/db89bbb818e7dc98ee9d3ad14db0a24f436f0c55/MaxText/train.py#L468

moe_lb_loss should be divided by gradient_accumulation_steps for reporting.
```py
  moe_lb_loss = aux["moe_lb_loss"] / config.gradient_accumulation_steps
```

## 评论 (3)

### RissyRan · 2025-03-31

Thanks for reaching out! I think the gradient_accumlation_steps is handled [here](https://github.com/AI-Hypercomputer/maxtext/blob/db89bbb818e7dc98ee9d3ad14db0a24f436f0c55/MaxText/train.py#L451-L454)? Inside of `if config.gradient_accumulation_steps > 1`.


https://github.com/AI-Hypercomputer/maxtext/blob/db89bbb818e7dc98ee9d3ad14db0a24f436f0c55/MaxText/train.py#L451-L454


### bzantium · 2025-03-31

you are right for loss calculation but not for moe lb loss logging on tensorboard.
https://github.com/AI-Hypercomputer/maxtext/blob/db89bbb818e7dc98ee9d3ad14db0a24f436f0c55/MaxText/train.py#L468-L486

in L485, current code provides `moe_lb_loss` which is summed through gradient accumulation if `config.gradient_accumulation_steps>1` following:
 https://github.com/AI-Hypercomputer/maxtext/blob/db89bbb818e7dc98ee9d3ad14db0a24f436f0c55/MaxText/train.py#L456

so need to fixed as suggested above.

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.
