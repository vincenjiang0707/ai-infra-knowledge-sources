# [Issue #1896] Run downstream eval, e.g., mmlu, every n iterations during  mbridge distillation

source: https://github.com/NVIDIA/Model-Optimizer/issues/1896
state: closed | updated: 2026-07-23T18:01:46Z
labels: feature request, waiting for feedback, torch.distillation, feature

## 正文

### Detailed description of the requested feature

While [distilling mbridge model](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/megatron_bridge/README.md#distillation), enable running downstream task evaluation every n iterations. This will let to analyze mmlu (and other tasks) over time.

## 评论 (8)

### h-guo18 · 2026-07-05

Hi @AAnoosheh ,could you take a look into this feature request or re-assign it to others. Thanks!

### Surya-5555 · 2026-07-12

Hi @danielkorzekwa @h-guo18 - can I pick this up? It's been a couple weeks without an update, so wanted to check before starting.

I dug into this and confirmed the pieces needed already exist, though the wiring needs some care:


- Model-Optimizer already has a working in-memory MMLU evaluator for Megatron models: modelopt/torch/utils/plugins/megatron_mmlu.py, already used the same way (periodic eval on a live model) in examples/megatron_bridge/prune_minitron.py.
- Megatron-Bridge's bridge.training.eval.evaluate() runs at every eval_interval and accepts non_loss_data_func / process_non_loss_data_func hooks. However, megatron_mmlu() doesn't fit that signature directly - it's a self-contained function that takes the full model and runs its own MMLU dataset loop, whereas those hooks are designed to process per-batch outputs already collected via forward_step_func.


So the cleanest approach I'm considering is intercepting the evaluation phase at the distill.py script level (e.g. wrapping/patching the evaluate call) so megatron_mmlu() runs exactly once per eval_interval rather than trying to force it into the per-batch hook signature. Still no changes needed upstream in Megatron-Bridge itself.

If this hasn't already been picked up, I'd like to take it on - happy to share the exact approach once I've prototyped it.

### danielkorzekwa · 2026-07-12

This has been already implemented in https://github.com/NVIDIA/Model-Optimizer/pull/1897 just waiting to merge to main this one first: https://github.com/NVIDIA/Model-Optimizer/pull/1888.

Effectively, I added a logic to enable exporting HF checkpoints every n distillation iters, and then they could be evaluated. I then evaluate those checkpoint just asking codex to do it (codex skill will go to main in a few weeks for it).

Thanks for interest, and feel free to do code review, but best to wait till 1872 is merged first.

### Surya-5555 · 2026-07-12

Thanks for the context, @danielkorzekwa! Decoupling the evaluation via exported HF checkpoints is a solid architectural choice to keep the main training loop unblocked.

I see #1872 is already merged! I'll track the merge queue for #1888 next. Once it gets merged and #1897 is ready, I'll jump in for the code review.

While waiting on those, could you point me to another open issue? I'd be happy to take one on if there's anything I can be assigned to.

### danielkorzekwa · 2026-07-17

The best would be taking some sota model, can be small and try to compress it (either with puzzletron or minitron method) to obtain some nice results and share the compressed model on HF. 

During this process you will likely observe things that can be improved in ModelOpt. If you like this plan I could help in selecting some model to try to compress.

### danielkorzekwa · 2026-07-17

https://github.com/NVIDIA/Model-Optimizer/pull/1897 is under code review now, facing issues during hf checkpoint export (setting activation_func to None) see the lasted commit for more details

### Surya-5555 · 2026-07-17

That sounds great, @danielkorzekwa! I am in. Which SOTA models do you recommend starting with for the Puzzletron or Minitron compression? 

While waiting, I will review the latest commit on PR #1897. I will see if I can find where the activation function drops during the Megatron to HF export and leave a comment there. 

Thanks for the pointers!

### danielkorzekwa · 2026-07-23

Done: https://github.com/NVIDIA/Model-Optimizer/pull/1897
