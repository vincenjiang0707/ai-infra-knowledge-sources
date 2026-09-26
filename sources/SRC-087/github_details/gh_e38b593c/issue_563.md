# [Issue #563] [RFC]: Support Qwen3 base architecture for eagle3 & p-eagle

source: https://github.com/vllm-project/speculators/issues/563
state: closed | updated: 2026-07-03T15:04:13Z
labels: good first issue, RFC

## 正文

### Motivation.

As proven by DFlash, the Qwen3 base architecture is more stable for EAGLE3 training due to the extra norms in the attention module. We can improve performance of EAGLE3 and P-EAGLE by using Qwen3 as a base architecture and leveraging the higher learning rates now possible in training. Inference is enabled by this [branch](https://github.com/vllm-project/vllm/pull/43132) in vllm.

### Proposed Change.

Qwen3 base components are defined in [src/speculators/models/base_components.py](https://github.com/vllm-project/speculators/blob/main/src/speculators/models/base_components.py) and in eagle3/model_definitions.py, `Qwen3DecoderEagle3FirstLayer` is implemented and registered in the model_classes dict under "qwen3". Make sure to update `transformer_layer_config` to use `qwen3`. Test if we get performance boost. 

### Any Other Things.

_No response_

## 评论 (9)

### orestis-z · 2026-06-01

Most of the Qwen3 support is already in place (`base_components`, `model_definitions`, P-EAGLE via inheritance, `--draft-arch qwen3` in training). The only gap is the converter, which always creates a `LlamaConfig`. Will fix that and open a PR.

For performance testing, planning to train two Eagle3 drafters (llama vs qwen3 arch) on the same data and compare acceptance rates with higher LRs.

### orestis-z · 2026-06-02

@shanjiaz, @fynnsu after digging deeper, the converter fix seems to be forward-looking: all existing Eagle3 checkpoints for Qwen3 targets that I found (e.g. nvidia/Qwen3-235B-A22B-Eagle3) use Llama draft arch, and I couldn't find a legacy-format Qwen3-arch checkpoint. If that's confirmed, then there would not be an immediate value for today and we would have to guess what a future Qwen3-arch legacy checkpoint would look like. What are your thoughts?

The immediate value is def. on the training side: benchmarking `--draft-arch qwen3` vs `llama`.

### shanjiaz · 2026-06-02

@orestis-z 
I agree, we can definitely start with training since there are no existing checkpoints with qwen3 structure yet. Thank you!


### orestis-z · 2026-06-02

## Eagle3 Llama vs Qwen3 Draft Arch: LR Sweep Results

**Setup**: Qwen/Qwen3-8B target, 5k ShareGPT, 5 epochs, vLLM spec decode eval (20 prompts, 256 tok)

| LR | Llama Acc Len | Qwen3 Acc Len | Δ |
|------|:-:|:-:|:-:|
| 1e-4 | 1.433 | 1.454 | +0.021 |
| 3e-4 | 1.632 | 1.653 | +0.021 |
| 5e-4 | 1.561 | **1.672** | +0.111 |
| 7e-4 | 1.436 | 1.645 | +0.209 |
| 1e-3 | 1.308 | 1.586 | +0.278 |

**Llama peaks at 3e-4 then collapses. Qwen3 peaks at 5e-4 and degrades gracefully** — even at 1e-3 it outperforms llama's best. The extra attention norms clearly stabilize training at higher LRs.

<img width="2084" height="1475" alt="Image" src="https://github.com/user-attachments/assets/c6fb668b-d81a-4760-a47e-f7eed5698dac" />

### shanjiaz · 2026-06-02

@orestis-z Looks great! Thanks for running the test.

### orestis-z · 2026-06-05

### P-EAGLE LR Sweep: Qwen3 vs Llama Draft Arch

Setup: Qwen/Qwen3-8B target, 5k ShareGPT, 5 epochs, offline training, validation full_acc

| LR | Llama full_acc | Qwen3 full_acc | Δ |
|------|:-:|:-:|:-:|
| 1e-4 | 0.352 | 0.348 | -0.004 |
| **3e-4** | **0.427** | **0.435** | **+0.008** |
| 5e-4 | 0.404 | 0.432 | +0.028 |
| 7e-4 | 0.351 | 0.418 | +0.067 |
| 1e-3 | 0.206 | 0.390 | +0.184 |

Both peak at 3e-4. Llama collapses at higher LRs — at 1e-3 it's nearly untrained (0.206). Qwen3 degrades gracefully and at 1e-3 still nearly matches Llama's best.

<img width="2082" height="1465" alt="Image" src="https://github.com/user-attachments/assets/7a849c1b-2442-4c79-9d6a-e1c35069a908" />

### orestis-z · 2026-06-08

## Full Training Results: Llama vs Qwen3-arch Eagle3 Drafter

Trained a Qwen3-arch Eagle3 drafter for Qwen/Qwen3-8B on 508k samples (magpie + ultrachat from `inference-optimization/Qwen3-8B-Regenerated-Collection`), 2 epochs, online mode.

### Acceptance lengths (Qwen3-arch vs Llama-arch)

Both drafters trained on the same dataset (`Qwen3-8B-Regenerated-Collection`, 508k samples), same hyperparameters (2 epochs, `--draft-vocab-size 32000`, online mode), evaluated with the same sampling params (temp=0.6, top_p=0.95, top_k=20). Format: **Qwen3** (Llama).

| Use Case | k=1 | k=2 | k=3 | k=4 | k=5 | k=6 | k=7 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Coding | **1.81** (1.79) | **2.40** (2.35) | **2.80** (2.71) | **3.06** (2.88) | **3.22** (3.00) | **3.30** (3.06) | **3.33** (3.10) |
| Math | **1.83** (1.81) | **2.50** (2.42) | **2.95** (2.87) | **3.28** (3.12) | **3.45** (3.30) | **3.61** (3.42) | **3.68** (3.45) |
| Summarization | **1.69** (1.67) | **2.11** (2.05) | **2.35** (2.25) | **2.46** (2.33) | **2.50** (2.37) | **2.52** (2.38) | **2.52** (2.39) |

Qwen3-arch outperforms Llama-arch across all benchmarks and all k values. The improvement is consistent at ~3-7%, with the gap widening at higher k (math k=7: 3.68 vs 3.45, +6.7%).

<img width="2085" height="695" alt="Image" src="https://github.com/user-attachments/assets/02032b7f-4cb5-4a80-99c6-2b74224b8d72" />

### Training config

| | Llama-arch | Qwen3-arch |
|---|---|---|
| **Architecture** | `--draft-arch llama` | `--draft-arch qwen3` |
| **LR** | 3e-4 | 5e-4 |
| **Model** | [llamaarch-ckpt1](https://huggingface.co/inference-optimization/Qwen3-8B-from-Qwen3-8B_regen-speculators.eagle3-llamaarch-ckpt1) | [qwen3arch-ckpt1](https://huggingface.co/inference-optimization/Qwen3-8B-from-Qwen3-8B_regen-speculators.eagle3-qwen3arch-ckpt1) |

- Dataset: `Qwen3-8B-Regenerated-Collection` (magpie + ultrachat), 508k samples
- 2 epochs, `--draft-vocab-size 32000`
- 7 GPUs: 2 vLLM (DP=2) + 5 training (FSDP), online mode
- Qwen3-arch requires vLLM qwen3 eagle3 support ([vllm#43132](https://github.com/vllm-project/vllm/pull/43132)) + [architecture resolution fix](https://github.com/vllm-project/vllm/pull/43132#issuecomment-4602782987)

### Convergence

Both drafters used a cosine LR schedule over 2 epochs (~81k steps), fully decaying to ~zero by the end.

| | Llama-arch (lr=3e-4) | Qwen3-arch (lr=5e-4) |
|---|---|---|
| **Val loss epoch 0** | 6.079 | 5.480 |
| **Val loss epoch 1** | 5.974 (-1.7%) | 5.318 (-3.0%) |

The Llama-arch drafter showed minimal improvement between epochs (1.7%), while the Qwen3-arch was still improving more meaningfully (3.0%). Both LR schedules fully decayed by the end of epoch 2.

---
**Edit (2026-06-10):** Updated baseline from RedHatAI/Qwen3-8B-speculator.eagle3 (different training data) to a [Llama-arch drafter](https://huggingface.co/inference-optimization/Qwen3-8B-from-Qwen3-8B_regen-speculators.eagle3-llamaarch-ckpt1) trained on the same dataset for an apples-to-apples architecture comparison.

### orestis-z · 2026-06-16

## Full Training Results: Llama vs Qwen3-arch P-EAGLE Drafter

Trained a Qwen3-arch P-EAGLE drafter for Qwen/Qwen3-8B on [Qwen3-8B-Regenerated-Collection](https://huggingface.co/datasets/inference-optimization/Qwen3-8B-Regenerated-Collection), using the same hyperparameters as the [Llama-arch baseline](https://huggingface.co/shanjiaz/qwen3-8b-peagle-speculators) (5 epochs, lr=6e-4, cosine schedule, 2 GPUs).

### Acceptance lengths (Qwen3-arch vs Llama-arch)

Evaluated on [RedHatAI/speculator_benchmarks](https://huggingface.co/datasets/RedHatAI/speculator_benchmarks) (9 subsets) via vLLM throughput mode. Format: **Qwen3** (Llama).

| Subset | k=5 | k=7 |
|---|:-:|:-:|
| HumanEval | **3.51** (3.01) | **3.73** (3.50) |
| Math Reasoning | **3.73** (3.28) | **4.04** (3.82) |
| QA | **2.81** (2.40) | **3.01** (2.83) |
| Question | **2.99** (2.63) | **3.27** (3.03) |
| RAG | **3.06** (2.49) | **2.98** (2.93) |
| Summarization | **2.72** (2.03) | **2.55** (2.48) |
| Tool Call | **2.71** (2.45) | **2.97** (2.87) |
| Translation | **2.80** (2.26) | 2.81 (**2.89**) |
| Writing | **3.00** (2.63) | **3.37** (3.05) |
| **Average** | **3.04** (2.58, +18%) | **3.19** (3.04, +5%) |

Qwen3-arch outperforms Llama-arch on all 9 subsets at k=5 and 8/9 at k=7 (only regression: translation k=7, -2.5%).

<img width="2384" height="1033" alt="Image" src="https://github.com/user-attachments/assets/925d33bd-41bb-4636-86ff-d1ad9acfe8a6" />

### Training config

| | Llama-arch | Qwen3-arch |
|---|---|---|
| **Architecture** | (default) | `--draft-arch qwen3` |
| **LR** | 6e-4 | 6e-4 |
| **draft_vocab_size** | 151936 | 32000 |
| **Model** | [shanjiaz/qwen3-8b-peagle-speculators](https://huggingface.co/shanjiaz/qwen3-8b-peagle-speculators) | [peagle-qwen3arch-ckpt4](https://huggingface.co/inference-optimization/Qwen3-8B-speculators.peagle-qwen3arch-ckpt4) |

- Dataset: [Qwen3-8B-Regenerated-Collection](https://huggingface.co/datasets/inference-optimization/Qwen3-8B-Regenerated-Collection)
- 5 epochs, cosine schedule, 2 GPUs (nproc_per_node=2)
- 4 layers, 7 depths, down-sample ratio 0.6 (min 0.2)
- `--no-norm-before-residual`
- Qwen3-arch serving requires [vllm#43132](https://github.com/vllm-project/vllm/pull/43132) + [architecture resolution fix](https://github.com/vllm-project/vllm/pull/43132#issuecomment-4602782987)

Raw Llama-arch results: [spreadsheet](https://docs.google.com/spreadsheets/d/1wDT_k76G-mNnOv-PJqgr3Cu5nUjoSqChQjQLE0YSlDU)

### shanjiaz · 2026-06-16

Looks great!
