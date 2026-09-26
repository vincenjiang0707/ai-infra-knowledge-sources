# [Issue #2015] Recommended FP8 recipe for Blackwell (B200)? Per-tensor `FP8_DEFAULT_CFG` underperforms BF16 at prefill; NVFP4 much faster. Also: exported FP8 checkpoint has no KV `q/k/v_scale`

source: https://github.com/NVIDIA/Model-Optimizer/issues/2015
state: open | updated: 2026-08-02T22:08:52Z
labels: bug

## 正文

## Describe the bug
Quantizing Mistral-24B with `hf_ptq.py` for B200/vLLM deployment. **Per-tensor static FP8 (`FP8_DEFAULT_CFG`)
is net slower than BF16** in vLLM (prefill ~2× slower; decode faster), whereas **NVFP4 (`--qformat nvfp4`) is
~2× faster than FP8 and beats BF16 on all metrics.** Want to confirm the recommended recipe and understand two
export details.

### Steps/Code to reproduce bug
**Env:** B200 sm_100, modelopt 0.46.0, vLLM 0.25.1 + FlashInfer 0.6.13. Calib 1024 samples @ seq 2048.

**Quantization command (`hf_ptq.py`):**
```bash
# per-tensor FP8:
python examples/hf_ptq/hf_ptq.py \
  --pyt_ckpt_path <bf16-mistral-24b> \
  --export_path ./mistral_fp8 --qformat fp8 \
  --dataset <custom-calib-dataset> --calib_size 1024 --calib_seq 2048

# NVFP4 (identical, only --qformat and --export_path change):
python examples/hf_ptq/hf_ptq.py \
  --pyt_ckpt_path <bf16-mistral-24b> \
  --export_path ./mistral_nvfp4 --qformat nvfp4 \
  --dataset <custom-calib-dataset> --calib_size 1024 --calib_seq 2048
```

**Bench (`vllm bench serve`, random 300in / 64out, conc 64):**

| Config | req/s | TTFT P50 (ms) | TPOT P50 (ms) |
|---|---|---|---|
| BF16 | 44.4 | 547 | 13.7 |
| per-tensor FP8 (+FP8 KV) | 36.2 | 1010 | 7.1 |
| per-tensor FP8 (+BF16 KV) | 38.8 | 660 | 7.7 |
| NVFP4 | 84.1 | 313 | 6.8 |

Long prompts (2048in/64out, conc 32): per-tensor FP8 15.6 req/s vs NVFP4 23.1 req/s.
vllm bench command:
`vllm bench serve --model <model-path> --host <host> --port <port> --dataset-name random --random-input-len 300 --random-output-len 64 --num-prompts 1000 --max-concurrency 64'`
Note that I have issues on other models quantized in the same way and served through Tensorrt with the torch backend as well.

### Expected behavior
I expect fp8 models to go faster than bf16, both with quantized and not quantized kv cache

## System information

- Container used (if applicable): docker
- GPU name (e.g. H100, A100, L40S): B200
- Library versions (if applicable):
  - Python: 3.12.3
  - ModelOpt version or commit hash: 0.46.0
  - CUDA: 13.0
  - PyTorch: 2.13.0
  - Transformers: 5.12.1


## 评论 (3)

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: f284fea27c192d58ffb73369fbb1fa2aed7a646850b3708185c777962e1b4ac1

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: fc256f2a3c81006507e2886789898ceecc96601886cfff92b6b686f92bfcc723

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: aeb6c1bd4aa116d826f2a6ac8d03556075597403de0e4f5ab7f41abd9a2e0217

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
