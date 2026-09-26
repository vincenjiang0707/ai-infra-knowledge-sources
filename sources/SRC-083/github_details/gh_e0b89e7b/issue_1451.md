# [Issue #1451] LoRA + deepspeed zero3 finetuing using 8bit quantization of base weights results in increased loss

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1451
state: closed | updated: 2026-02-21T20:10:07Z
labels: Bug, Contributions Welcome

## 正文

### System Info

latest releases of transformers, bnb, peft, accelerate, python 2.5.1, deepspeed 0.16.1

### Reproduction

see axolotl config here: https://wandb.ai/axolotl-ai/lora-3b-ds-zero3/runs/c4b1agng/files/tmp/axolotl_config_az8clerk.yml

### Expected behavior

the loss value is off by an order of magnitude @ ~13, whereas zero2 and zero1 are correct. I also tried changing the `llm_int8_threshold` in the bnb config to 0.0 and 1.0. 0.0 results in 0.0 loss, and 1.0 results in the same original defect.

## 评论 (1)

### TimDettmers · 2026-02-21

Closing this issue due to no activity for over a year. DeepSpeed ZeRO-3's weight partitioning is not compatible with bitsandbytes 8-bit quantized weights — ZeRO-3 expects standard floating-point parameters, but quantized weights have a different internal structure that doesn't partition correctly, which can cause loss anomalies like what you observed.

Consider using ZeRO stage 1 or 2 with quantized models instead. If you're still experiencing this on the latest versions and have new information, please feel free to reopen or file a new issue.
