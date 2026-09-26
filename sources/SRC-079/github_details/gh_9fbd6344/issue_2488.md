# [Issue #2488] StaticLossBalancer warns "weights do not sum to 1.0" with a config that does sum to 1.0

source: https://github.com/NVIDIA/Model-Optimizer/issues/2488
state: closed | updated: 2026-09-23T17:28:18Z
labels: bug

## 正文


## Describe the bug

I noticed that passing a `StaticLossBalancer` configuration where the weights sum to exactly `1.0` still triggers the following warning:

```text
UserWarning: `StaticLossBalancer` weights do not sum to 1.0. Argument `student_loss`
should be passed into `DistillationModel.compute_kd_loss`.
```

I may be misunderstanding the intended usage of `StaticLossBalancer`, so I wanted to clarify this behavior.

The warning mentions that `student_loss` should be passed into `compute_kd_loss()`. This made me wonder whether the ground-truth / CE loss is expected to be supplied separately through the `student_loss` argument, rather than being declared as a named key such as `ce_loss` inside the `StaticLossBalancer` dictionary.

With the configuration below, I expected the weights to represent `0.7` for KD loss and `0.3` for CE loss, since they sum to exactly `1.0`.

I eventually bypassed the balancer and computed the weighted KD and CE losses manually in a custom `Trainer.compute_loss()` override.

**Impact:** The warning message is confusing about the expected API usage, and I could not find documentation that clearly explained the intended way to combine KD loss with the ground-truth CE loss.

During my initial test, I also observed unstable training loss values, ranging from approximately `79` to `1836` during the first 500 steps, without a clear convergence trend. I am not sure whether this is related to the warning or to my configuration, so I would appreciate some guidance.

### Steps/Code to reproduce bug

```python
distillation_config = {
    "teacher_model": teacher_model,
    "criterion": mtd.LogitsDistillationLoss(temperature=2.0),
    "loss_balancer": mtd.StaticLossBalancer({
        "kd_loss": 0.7,
        "ce_loss": 0.3,
    }),
}

distillation_model = mtd.convert(
    student_model,
    mode=[("kd_loss", distillation_config)],
)
```

Train normally via `Trainer.train()`.

The warning appears immediately during training.

### Expected behavior

Since `0.7 + 0.3 = 1.0`, I expected that no warning would be raised.

Could someone please clarify whether the dictionary form:

```python
{"kd_loss": 0.7, "ce_loss": 0.3}
```

is the intended way to combine the KD loss with the ground-truth CE loss?

If this is not the intended API, could the documentation or examples clarify that the CE / ground-truth weight should instead be supplied through the `student_loss` argument to `compute_kd_loss(student_loss=...)` at call time?

I would appreciate any clarification on the expected usage here.

### Who can help?



## System information

* Container used (if applicable): none / bare venv
* OS: Ubuntu Linux
* CPU architecture: x86_64
* GPU name: NVIDIA DGX B200
* GPU memory size: 192GB
* Number of GPUs: 1
* Library versions:

  * Python: 3.12.3
  * ModelOpt version or commit hash: 0.46.1
  * CUDA: 13.2.86
  * PyTorch: 2.12.0.dev20260408+cu128
  * Transformers: 5.14.1
  * TensorRT-LLM: N/A
  * ONNXRuntime: N/A
  * TensorRT: N/A
* Any other details: Teacher and student differ in vocabulary size (`152,064` vs `151,936`). I am mentioning this in case it could be relevant, although I have not confirmed that it is related to the warning or training behavior.


## 评论 (10)

### TheSabari07 · 2026-09-22

Hi @kevalmorabia97, I’d love to work on this issue. If it’s okay, could you please assign it to me?


### AAnoosheh · 2026-09-23

Hi, this part is definitely not the most intuitive.  
The StaticLossBalancer must receive a float or list[float] as input, not dict.

But luckily, the loss balancer design is essentially deprecated, as it is unused everywhere by now except the Megatron plugin, where we will likely soon remove it as well. 

I assume you wish to use the HF Transformers based distillation? This is now done without any balancers altogether. Please see `https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/llm_distill` for more.

Thanks!

### AAnoosheh · 2026-09-23

Also now I have realized the documentation for the `llm_distill` example is outdated and will need updating soon

### TheSabari07 · 2026-09-23

Hi @AAnoosheh,

Thank you so much for the clear explanation! It makes perfect sense that the loss balancer is being deprecated and that writing a custom loss class is the intended way to handle these specific model scenarios.

Since you mentioned that the llm_distill documentation is currently outdated, would it be helpful if I submitted a Pull Request to help update it? I'd be very happy to contribute.

### AAnoosheh · 2026-09-23

I think it'll be faster if I do it from my side, since then we avoid a back-and-forth review process if I need to nitpick wording, style, etc, but I do appreciate your enthusiasm.

But one more caveat to the new HF KD trainer loss function: it currently doesn't combine ce_loss and kd_loss (only returns kd_loss), so you'd need to modify/overwrite the `KDTrainer.compute_loss()` method to compute `ce_loss` during training too and then combine both losses in order to achieve the StaticLossBalancer equivalent.  
If that's something you want to contribute, you're welcome to!

### TheSabari07 · 2026-09-23

Okay @AAnoosheh,

That makes total sense regarding the documentation
Regarding the KDTrainer.compute_loss() enhancement, I would love to contribute that. Could you please assign this to me? I will take a look and open a PR soon.

### AAnoosheh · 2026-09-23

Okay I'll close this and make a new issue

### TheSabari07 · 2026-09-23

> Okay I'll close this and make a new issue

Sure @AAnoosheh 

### AAnoosheh · 2026-09-23

Seems I can't assign new issues to someone outside the org unless they themselves open the issue.  
Can you create a new one with this description:
```
The new HF KD trainer loss function `KDTrainer.compute_loss()` currently doesn't combine ce_loss and kd_loss (only returns kd_loss), so we'd need to compute ce_loss during training too and then combine both losses.   
Ideally it should: 
1. Combine them as: alpha * kd_loss + (1-alpha) * ce_loss
2. Not compute ce_loss during training if alpha = 1.0 (default)
```

### TheSabari07 · 2026-09-23

> Seems I can't assign new issues to someone outside the org unless they themselves open the issue. Can you create a new one with this description:
> 
> ```
> The new HF KD trainer loss function `KDTrainer.compute_loss()` currently doesn't combine ce_loss and kd_loss (only returns kd_loss), so we'd need to compute ce_loss during training too and then combine both losses.   
> Ideally it should: 
> 1. Combine them as: alpha * kd_loss + (1-alpha) * ce_loss
> 2. Not compute ce_loss during training if alpha = 1.0 (default)
> ```

Okay @AAnoosheh, thank you
I will do it right now
