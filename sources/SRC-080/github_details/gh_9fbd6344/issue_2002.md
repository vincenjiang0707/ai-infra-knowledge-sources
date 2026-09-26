# [Issue #2002] [QAD] Request for exact training configurations used in arXiv:2601.20088

source: https://github.com/NVIDIA/Model-Optimizer/issues/2002
state: open | updated: 2026-09-02T13:21:37Z
labels: 

## 正文

## Question

Thank you for releasing Model Optimizer and the QAD examples. I am trying to understand and reproduce the accuracy recovery reported in [*Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery* (arXiv:2601.20088v3)](https://arxiv.org/abs/2601.20088).

The paper reports near-BF16 recovery for several models. It provides the loss (forward KL), temperature (`T=1`), approximate token counts, and a few learning rates, but I could not find the exact per-model training configurations used to produce the reported checkpoints.

Could you please share the exact configs/commands (or point me to them) for the paper experiments?

## Repository path and scripts I used

I used the **Hugging Face/FSDP2 path in `examples/llm_qat`**, not the Megatron-LM path in `examples/llm_qad`.

Model Optimizer revision:

```
7ed19b290692f801a54be7266de0c34871a58949
modelopt 0.46.0.dev164+g7ed19b290
```

The two entry points were:

1. Pre-quantization: [`examples/llm_qat/quantize.py`](https://github.com/NVIDIA/Model-Optimizer/blob/7ed19b290692f801a54be7266de0c34871a58949/examples/llm_qat/quantize.py)
2. QAD training: [`examples/llm_qat/train.py`](https://github.com/NVIDIA/Model-Optimizer/blob/7ed19b290692f801a54be7266de0c34871a58949/examples/llm_qat/train.py), which constructs `QADTrainer`

The training command was equivalent to:

```bash
accelerate launch \
  --config-file configs/accelerate/fsdp2.yaml \
  --num_processes 4 \
  train.py --config /path/to/qad.yaml
```

The FSDP2 config used BF16 mixed precision, transformer-based wrapping of `Qwen3DecoderLayer`, activation checkpointing, sharded state dicts, `reshard_after_forward: true`, and no CPU parameter offload.

## Important quantizer caveat

These experiments are **not a direct NVFP4 reproduction**. I tested ordinary symmetric integer quantization:

- Model/teacher: Qwen3-8B; the original BF16 Qwen3-8B was also the teacher.
- Weights: signed symmetric **INT4, group size 64**, static per-group max scale, narrow range (`[-7, 7]`).
- Activations: signed symmetric **INT8, group size 64**, dynamic per-token/per-group max scale, narrow range (`[-127, 127]`).
- KV cache: not quantized.
- Quantized modules: the 252 decoder GEMM weights (`q/k/v/o_proj` and `gate/up/down_proj`); embedding, norms, and `lm_head` were not quantized.
- Fake quantization was used in the forward pass with STE in backward.

The ordinary dynamic INT8-g64 fused CUDA fake-quant path was **added locally by me** because it was not supported by the repository. It computes a fresh symmetric INT8 scale for each contiguous group of 64 activation values. This is **not MXINT8, MXFP8, or NVFP4**, and I am not claiming that it is an official Model Optimizer quantizer. I mention this explicitly because the different number format may be relevant to the result.

## Shared QAD training configuration

Both runs used:

```yaml
distill: true
criterion: logits_loss
temperature: 1.0
liger_jsd_beta: 0.0       # forward KL
num_train_epochs: 1.0
learning_rate: 1.0e-5
weight_decay: 0.0
lr_scheduler_type: cosine
warmup_ratio: 0.05
per_device_train_batch_size: 2
per_device_eval_batch_size: 2
gradient_accumulation_steps: 2
model_max_length: 8192
use_liger_kernel: true
manual_gc: true
bf16: true
seed: 42
```

Additional optimizer settings:

- 4 × A100-SXM4 80 GB, global training batch size = `2 × 4 × 2 = 16`
- `adamw_torch_fused`, betas `(0.9, 0.999)`, epsilon `1e-8`
- Gradient clipping: `1.0`
- All student parameters remained trainable (`trainable_params: null`, `frozen_params: null`), including embedding, norms, and `lm_head`; the teacher was frozen.
- Static INT4 `amax` values were buffers and were not learnable.
- Loss was forward KL after the causal shift, reduced as the mean over positions where shifted `labels != -100`.
- With the chat-template preprocessing in `examples/llm_qat/dataset_utils.py`, this meant that KL was applied to assistant-response tokens rather than every non-padding token.

Environment:

```
PyTorch 2.11.0+cu128
Transformers 5.12.1
Accelerate 1.14.0
Datasets 5.0.0
CUDA 12.8
```

## Dataset blend

Both runs used the repository's default QAD/SFT mixture with a 90/5/5 train/eval/test split and the following relative source weights:

| Source | Subset | Ratio |
|---|---|---:|
| `nvidia/Nemotron-SWE-v1` | `r2e_gym` | 6000 |
| `nvidia/Nemotron-Math-v2` | `medium` | 2500 |
| `nvidia/Nemotron-Science-v1` | `MCQ` | 1500 |
| `nvidia/Nemotron-Science-v1` | `RQA` | 1500 |
| `nvidia/Nemotron-Instruction-Following-Chat-v1` | `chat_if` | 5000 |
| `nvidia/Nemotron-Post-Training-Dataset-v2` | `chat` | 1500 |
| `nvidia/Nemotron-Competitive-Programming-v1` | `competitive_coding_python_part00` | 1000 |

## Two completed QAD runs

| Setting | Run 1 | Run 2 |
|---|---:|---:|
| `blend_size` | 20,000 | 100,000 |
| `train_samples` | 20,000 | 100,000 |
| Actual cached training examples | 16,580 | 89,959 |
| Approx. non-padding training tokens | 89.3M | 457.7M |
| Approx. assistant/loss tokens | 45.2M | 233.8M |
| Optimizer steps | 1,036 | 5,622 |
| Epochs | 1 | 1 |
| `eval_samples` | 2,000 (921 available) | 200 |
| `eval_steps` | 50 | 100 |
| Final validation KL | 0.02480 | 0.02552 |

Run 2 was a fresh run from the same pre-quantized student, not a continuation of Run 1.

## Observed behavior

Training and validation KL decreased normally, and increasing the blend improved held-out output fidelity slightly. However, the final QAD checkpoints still did not outperform my GPTQ/AutoRound PTQ baselines.

For a controlled full-model comparison, I baked the final INT4 fake-quantized values into BF16 tensors, loaded the result as a normal Hugging Face model, and applied the same dynamic symmetric AINT8-g64 fake quantizer to all 252 decoder linear inputs during evaluation.

Forward `KL(BF16 teacher || quantized model)`, each on 512 held-out samples of length 2,048:

| Model | Pile held-out KL | OpenOrca KL |
|---|---:|---:|
| QAD Run 1 | 0.04901 | 0.14227 |
| QAD Run 2 | 0.04678 | 0.13437 |
| AutoRound best WINT4-g64 + the same AINT8-g64 evaluation quantizer | 0.02718 | 0.09104 |

For Run 1, five-run downstream evaluation with the same AINT8-g64 activation fake quantizer gave:

| Model | AIME-2026 | GPQA-Diamond | Simple average |
|---|---:|---:|---:|
| QAD Run 1 | 0.6000 | 0.5778 | 0.5889 |
| AutoRound best WINT4-g64 | 0.6400 | 0.5616 | 0.6008 |

I understand that:

1. the paper evaluates NVFP4 rather than this custom integer W4A8 format;
2. QAD is not necessarily expected to beat every advanced PTQ algorithm; and
3. model family, post-training history, data volume, and checkpoint selection can materially change the result.

I am therefore mainly trying to determine whether my training setup differs from the setup that produced the paper's reported recovery.

## Details that would help reproduce the paper

Could you share the following **for each reported model/checkpoint**, ideally as runnable YAML and launch commands?

1. Which code path was used: `examples/llm_qad` (Megatron-LM), `examples/llm_qat` (HF Transformers), or the NeMo path?
2. Exact optimizer, LR, scheduler, warmup, weight decay, gradient clipping, global/micro batch size, gradient accumulation, sequence length, number of steps/epochs, and distributed configuration.
3. Exact training-data mixture and preprocessing: packing, truncation, chat template, whether responses were generated by the teacher, and whether samples were reused across epochs.
4. Was KL reduced over **all non-padding tokens** or only assistant/response tokens? Was it a global token mean across data-parallel ranks?
5. Which student parameters were updated: all weights, only quantized GEMM weights, `lm_head`, embeddings, norms, and/or quantizer scales?
6. Exact NVFP4 recipe and calibration details: quantized/excluded modules, weight and activation scale behavior during QAD, calibration algorithm/size, KV-cache format, and whether scales were fixed or learnable.
7. Validation/checkpointing details: validation set size, validation metric/reduction, evaluation interval, save interval, and how the “top 10 lowest-validation-loss checkpoints” were selected and then ranked on downstream benchmarks.
8. Do you expect the same QAD recipe to improve ordinary symmetric INT4-g64 / INT8-g64 fake quantization, or are there NVFP4-specific considerations that make a different recipe necessary?

Publishing the exact configs used for the paper (even for one model such as AceReason Nemotron 1.1 7B or Nemotron Nano 9B V2) would be extremely helpful.

Thank you.


## 评论 (5)

### mxinO · 2026-07-22

Thank you for contacting, here are the details for Acereason Nemotron 1.1 7B,
1. NeMo is used, but that is based on Megatron, so you can use Megatron-LM, which is more actively maintained.
2. Your optimizer configs are mostly good. The main issue is on your other configs, **you need longer seq len and larger gbs**, it's hard to get improvement with gbs=16 and seq len =8192.
```
seq_len= 32768 (sequence packing is used)
global_batch_size=100 (equivalent to ~1024 samples due to seq packing)
warmup_steps=10
```
  The best ckpt is usually gained between 200-600 steps. Don't reuse the samples if you have enough data. The total token is around ~1B. The best ckpt is selected by actual benchmarks, not only by validation loss.

3. **The data is the original SFT data of the model**, this is emphasized in the report. So for public models without original training data, it may affect the result, the nemotron data you tried is a good starting point. The final benchmark is not that sensitive to the data blend in our tests as if the format is correct (chat template is correctly applied).
4. Loss is reduced over all valid tokens including the prompt.
5. All weights are updated.
6. All GEMM are quantized to W4A4. Other components are BF16, e.g. embedding and lm head. KV cache is not quantized. It can be easier if you only quantize MLP layers. Scales are fixed. Calibration uses ~1024 samples of its original SFT data.
7. The final selection is based avg of the benchmarks (AIME, LCB, etc), selecting from 10 ckpts with lowest validation loss. Saving per 10 steps. Validation has 1024 held-out samples. Note the benchmarks like AIME/LCB have large variance, so use repeating multiple times is important. Detail is in the report.
8. W-Int4-g64 A-Int8-g64 may degrade too much. comparing the PTQ, the NVFP4 W4A4 performs similarly/slightly better than Int4-g16 weight only. If the gap between PTQ and BF16 is too large, the QAD may not recover the model (the large gap case is not tested), extensive QAT in pretraining/posttraining may be a better choice for large gaps. 


### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 42a30d2d21787bd569379ed3b9e9a38ed56db9f56e3f752d820728a22c12cf6a

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 7c02735a33ca92cb26e68a738d19cc59977fa755557cc50f3cd2c0979b040651

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 937dec58d8d68b55d44960fba8f3ab03d5447c0bb884bf087ed0417a0ea4953c

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### jenchen13 · 2026-09-02

@Sekri0 do you still have any questions? If not we will close this issue, thank you!
