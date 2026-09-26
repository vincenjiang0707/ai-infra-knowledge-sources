# [Issue #2489] Handling vocabulary size mismatches between teacher and student in distillation

source: https://github.com/NVIDIA/Model-Optimizer/issues/2489
state: closed | updated: 2026-09-23T17:09:19Z
labels: feature request

## 正文

**Is your feature request related to a problem? Please describe.**

When distilling between teacher and student models from the same family but with slightly different vocabulary sizes, we currently don't see a supported way to handle the mismatch in `modelopt.torch.distill`.

In our case, `Qwen2.5-Coder-7B-Instruct` has `vocab_size=152,064`, while `Qwen2.5-Coder-0.5B-Instruct` has `vocab_size=151,936`. `LogitsDistillationLoss.forward` applies `F.log_softmax`/`F.softmax` directly to the teacher and student logits and then computes `F.kl_div`, which requires the last dimensions to match.

`KDLossConfig` also doesn't appear to provide an option for configuring vocabulary alignment. As a workaround, we implemented a custom loss wrapper that truncates both logits tensors to `min(teacher_vocab, student_vocab)` before passing them to the criterion. This works for our case, but we weren't able to find documented guidance on whether this is the intended approach or whether it is numerically correct when used together with `StaticLossBalancer`.

**Describe the solution you'd like**

It would be helpful to have a native and documented way to handle vocabulary-size mismatches between teacher and student models.

For example, this could be:

* Automatic vocabulary alignment/truncation inside `LogitsDistillationLoss`, or
* A separate loss/configuration option specifically for vocabulary alignment, or
* At minimum, a documented parameter or recommended pattern for supplying a pre-aligned vocabulary range.

This would make it easier for users to handle models from the same family without having to implement custom loss logic based on the current source code.

**Describe alternatives you've considered**

* **Custom `LogitsDistillationLoss` wrapper:** We currently truncate both logits tensors to `min(teacher_vocab, student_vocab)` before calling the original criterion. This works in our setup, but we are unsure whether this is the recommended approach, particularly with `StaticLossBalancer` (see #2488).
* **Custom PyTorch KD loop:** We also considered bypassing ModelOpt's distillation wrapper and implementing the training loop ourselves. This ultimately worked for our project, but it means giving up ModelOpt's teacher/student orchestration, `mtd.convert()`/`mtd.export()` lifecycle, and the downstream quantization/export integration.

**Additional context**

This came up while distilling models from the same Qwen2.5-Coder family rather than from different architectures. The tokenizer vocabulary is effectively the same, and the difference appears to come from padding the embedding matrix for GPU efficiency: the 7B model uses 152,064 entries, while the 0.5B model uses 151,936.

Because vocabulary-size differences like this can occur between different model sizes within the same family, having a supported way to handle them could be useful for other distillation use cases as well.

As a separate note, we also encountered a crash when calling `restore()` during an earlier iteration of our script. Unfortunately, we can no longer reproduce it because that version of the script was lost, so we don't have a minimal reproduction to provide. I'm mentioning it only in case it is already a known issue.

Thank you for considering this. Any guidance on the recommended approach for handling vocabulary mismatches would also be greatly appreciated.


## 评论 (3)

### TheSabari07 · 2026-09-22

Hi @kevalmorabia97, I’d be interested in working on this feature. Do you think it would be okay for me to take this up?


### AAnoosheh · 2026-09-23

Hi, @TheSabari07

The losses we provide are more or less samples that users can use to build further on for their own needs. While the solution to truncate works in some cases, it's not general and could be misleading.

So your way of making a custom loss class for your specific scenario is the intended way. 

Additionally, please see the loss balancer issue regarding my comment on that topic.

Thanks

### TheSabari07 · 2026-09-23


Hi @AAnoosheh,

Thank you for clarifying, I'll happily stick with my custom truncation wrapper. I also saw your reply on the loss balancer issue and left a reply there as well. Please look into it at your convenience. Thank you for your help and guidance across both of these.
