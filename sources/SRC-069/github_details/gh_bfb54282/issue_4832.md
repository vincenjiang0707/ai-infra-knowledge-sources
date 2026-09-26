# [Issue #4832] [Feature]: TRTLLM-GEN FMHA graph-safe request permutation and length-aware scheduling for ragged decode

source: https://github.com/flashinfer-ai/flashinfer/issues/4832
state: open | updated: 2026-09-25T02:13:04Z
labels: feature request, needs-triage, model: qwen3.5 / 3.6 / 3.8, op: attention

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

TRTLLM-GEN paged decode loses substantial throughput when requests in the same batch have highly variable KV lengths. An experimental SGLang-side prototype demonstrates that two forms of length-aware scheduling can recover this loss:

- For batch sizes at or below the SM count, partitioning length-sorted requests into a small number of subgroups improves CTA allocation and reduces the longest-KV tail within each launch.
- For batch sizes above the SM count, keeping one persistent FMHA launch but changing request-entry order reduces persistent-scheduler tail imbalance.

On 4 x GB300 with Qwen3.5-397B-A17B-NVFP4-V2, the prototype improves full-model fixed-acceptance output throughput by a geometric mean of **6.816% across eight formally valid AgentX-ragged points**, while all ten uniform-length controls remain within the -1% no-regression gate. At B192, the full-model gain is **10.846%** and the same persistent FMHA kernel is **34.39% faster for Q1** after request reordering.

The measured prototype demonstrates that the performance is recoverable, but it requires serving-layer tensor permutation, output scatter, multiple CUDA Graph variants, and serial subgroup launches. We would like to discuss two FlashInfer capabilities:

1. An optional graph-safe request-order indirection for TRTLLM-GEN FMHA.
2. Longer term, a kernel-owned length-aware work scheduler for the low-batch ragged regime.

#### Performance evidence

The table below reports full-model fixed-acceptance output tok/s/GPU. `Control mean` is the mean of same-node control runs immediately before and after the prototype run. Uniform and ragged rows use separate matched controls; the percentages are never computed by dividing ragged throughput by uniform throughput.

| B/rank | Prototype strategy on ragged KV | Uniform control mean -> prototype | AgentX-ragged control mean -> prototype | Maximum control drift |
|---:|---|---:|---:|---:|
| 1 | N/A | 309.718 -> 311.945 (`+0.719%`) | N/A | 0.741% |
| 8 | NoSplit | 1,961.726 -> 1,985.144 (`+1.194%`) | 1,789.307 -> 1,776.897 (`-0.694%`) | 1.298% |
| 27 | Split2 | 3,760.041 -> 3,743.209 (`-0.448%`) | 3,164.617 -> 3,372.984 (`+6.584%`) | 0.564% |
| 32 | Split2 | 4,349.527 -> 4,318.366 (`-0.716%`) | 3,702.620 -> 3,909.861 (`+5.597%`) | 0.742% |
| 64 | Split4 | 5,527.886 -> 5,566.670 (`+0.702%`) | 4,590.968 -> 4,949.703 (`+7.814%`) | 0.468% |
| 128 | Split6 | 6,528.995 -> 6,518.155 (`-0.166%`) | 5,369.393 -> 5,838.822 (`+8.743%`)* | 2.196%* |
| 160 | NoSplit + descending reorder | 6,311.164 -> 6,304.193 (`-0.110%`) | 5,905.991 -> 6,373.150 (`+7.910%`) | 0.182% |
| 192 | NoSplit + descending reorder | 6,850.475 -> 6,835.488 (`-0.219%`) | 6,129.925 -> 6,794.770 (`+10.846%`) | 0.418% |
| 224 | NoSplit + descending reorder | 7,287.384 -> 7,284.583 (`-0.038%`) | 6,407.039 -> 6,919.727 (`+8.002%`) | 0.720% |
| 256 | NoSplit + descending reorder | 7,046.431 -> 7,047.866 (`+0.020%`) | 6,523.702 -> 7,101.724 (`+8.860%`) | 0.295% |

All ten uniform rows pass the -1% no-regression gate; the worst result is -0.716%. Eight ragged rows pass the 2% control-repeat-drift gate and have a +6.816% geometric-mean change. Including B128 gives a nine-point measured geometric mean of +7.028%.

`*` B128 reproduced the gain direction in a second A/B/A run at +8.681%, but control drift was 2.196% in the first run and 2.495% in the retry. We therefore treat the approximately +8.7% gain as directional rather than a formal absolute estimate.

For B192 AgentX-ragged, Nsight Systems captured 200 CUDA Graph replays before and after descending request reorder:

| Path | Q length 1 | Q length 6 |
|---|---:|---:|
| FMHA without reorder | 1,480.966 us | 1,924.955 us |
| FMHA with reorder | 971.639 us | 1,304.136 us |
| FMHA change | **-34.39%** | **-32.25%** |
| Added gather + scatter | 6.313 us | 10.715 us |
| Full kernel-window change | **-33.97%** | **-31.69%** |

Both paths execute the same `VarSeq...Persistent...ForGen` FMHA kernel with grid Z=192, identical block shape and shared-memory size, and the same launch count. The improvement therefore comes from reducing the persistent scheduler's request-entry tail, not from selecting a different kernel. The serving-layer gather/scatter cost is small relative to the observed kernel gain, but it introduces framework-owned buffers and CUDA Graph state that should not be necessary for a native kernel capability.

#### Problem scope and scheduling regimes

This request concerns fixed query length within each decode or verification call and variable KV length across requests. It is separate from variable query-length support discussed in [#1832](https://github.com/flashinfer-ai/flashinfer/issues/1832) and [#3131](https://github.com/flashinfer-ai/flashinfer/issues/3131).

We observed two distinct regimes on GB300, which has 152 SMs:

| Regime | Observed limitation | Prototype treatment |
|---|---|---|
| Padded B <= 152 | Subgroup shape controls static multi-CTA versus persistent dispatch; the longest KV length in each subgroup controls the tail | Capture at most one CTA-aware Split-N candidate and select it only when a KV-length proxy predicts at least 15% less work |
| Padded B > 152 | Multiple serial launches regress; request-entry order affects lane balance inside one persistent kernel | Keep NoSplit and optionally reorder requests by descending KV length when a cyclic-lane proxy predicts at least 2% less work |

A single batch-size threshold is insufficient. Controlled Split3 versus NoSplit sweeps changed sign multiple times because subgroup size, CTA/request allocation, and the actual KV-length distribution interact. We do not propose upstreaming the prototype's 15% and 2% thresholds as fixed FlashInfer policy; they are serving-side selectors used to demonstrate the underlying opportunity.

### Requested outcome

#### Graph-safe request-order indirection

For the high-batch persistent regime, would FlashInfer consider adding an optional device pointer to the TRTLLM-GEN generation runner parameters, conceptually:

```cpp
struct TllmGenFmhaRunnerParams {
  // Existing fields...
  int32_t const* requestOrderPtr;  // nullptr preserves identity order.
};
```

The proposed mapping is:

```text
requestOrderPtr[launch_slot] = original_request_index
```

For a non-null pointer, the kernel would use `original_request_index` consistently when reading Q, `seqLensKvPtr`, `kvPageIdxPtr`, and other per-request metadata. It would write the result to the original request's output row, preserving the caller-visible logical layout without separate Q/page-table gathers or output scatter.

The requested behavior is:

1. `nullptr` preserves the existing identity path without measurable overhead.
2. The pointer is device-resident and may be updated in place between CUDA Graph replays without changing its address.
3. A single captured graph can replay with different valid permutations.
4. The initial scope may be paged-KV generation with a fixed Q length per request if speculative verification complicates the first implementation.
5. The permutation applies consistently to Q, KV lengths, page-table rows, optional per-request scaling or metadata, and output placement.

This primitive would remove SGLang-side Q/page-table gathers, output scatter, and duplicate graph variants in the B > SM regime.

#### Length-aware kernel work scheduling

Request-order indirection does not fully address B <= SM, where the prototype currently issues multiple serial FMHA calls to obtain a more favorable CTA/request shape. A longer-term kernel-owned solution could use a per-request KV-tile work queue, per-request CTA budgets, or another segmented work-distribution mechanism that supports different KV work for each request within one launch.

The desired property is one graph-stable kernel launch that preserves uniform-workload performance while reducing the long-request tail for ragged KV distributions.

### Target hardware

SM103 (B300, GB300)

### Inference engine

SGLang; TRT-LLM integration path through FlashInfer TRTLLM-GEN FMHA.

### Affected model or model family

Qwen3.5-397B-A17B-NVFP4-V2. The requested scheduling capability is model-independent for fixed-Q paged decode with ragged KV lengths.

### Current workaround

This is an experimental SGLang-side treatment used to quantify attainable performance; it is not the current upstream SGLang implementation and is not proposed as the final serving-layer design.

- Prototype branch: [`agentx-upstream/mha-adaptive-scheduler-clean-20260830`](https://github.com/YAMY1234/sglang/tree/agentx-upstream/mha-adaptive-scheduler-clean-20260830)
- Exact measured commit: [`f8151ab14e`](https://github.com/YAMY1234/sglang/commit/f8151ab14e3d00d0c55c6408f91930cba527120a)
- Upstream base snapshot: `sgl-project/sglang@4bb8de34cc`

Relevant prototype code:

- [CTA-cost and persistent-lane proxies](https://github.com/YAMY1234/sglang/blob/f8151ab14e3d00d0c55c6408f91930cba527120a/python/sglang/srt/layers/attention/trtllm_mha_backend.py#L78-L180)
- [CUDA Graph variant selection](https://github.com/YAMY1234/sglang/blob/f8151ab14e3d00d0c55c6408f91930cba527120a/python/sglang/srt/layers/attention/trtllm_mha_backend.py#L441-L514)
- [Request sort, metadata gather, split launches, and output scatter](https://github.com/YAMY1234/sglang/blob/f8151ab14e3d00d0c55c6408f91930cba527120a/python/sglang/srt/layers/attention/trtllm_mha_backend.py#L1477-L1569)
- [Generic graph-variant plumbing required by the workaround](https://github.com/YAMY1234/sglang/blob/f8151ab14e3d00d0c55c6408f91930cba527120a/python/sglang/srt/layers/attention/base_attn_backend.py#L36-L47)

Even after keeping backend-specific policy inside `TRTLLMHAAttnBackend`, the adaptive prototype adds approximately 455 production lines. Those lines implement request permutation, graph-safe metadata ownership, variant capture and replay, subgroup launches, and output restoration. This integration cost is the primary reason for requesting a lower-level FlashInfer capability rather than proposing the prototype as upstream SGLang production code.

### Workload and configuration

#### Benchmark contract

- Hardware: 4 x GB300, 152 SMs per GPU.
- Model: Qwen3.5-397B-A17B-NVFP4-V2.
- Software: FlashInfer 0.6.17, CUDA 13, PyTorch 2.13.
- Parallelism: DP4 / TP4 / EP4.
- Attention: TRTLLM-GEN MHA, 8 Q heads, 1 KV head, head dimension 256, page size 64.
- Fixed B/rank on all four ranks, CUDA Graph enabled, scheduler queue empty.
- Simulated acceptance length 4.8 and `ignore_eos=true`.
- Measurement OSL 860, except the B1 long-window retry, which used OSL 4096 in all three arms.
- Same-node `control_before -> prototype -> control_after`; prototype throughput is compared with the mean of the two controls.
- Control-repeat-drift limit 2%; no-regression limit -1%.

The AgentX-ragged workload is a deterministic decode-isolation cohort rather than a live traffic replay. It keeps an AgentX-derived distribution of per-request KV lengths while removing request-arrival, prefill, and P/D-transfer variance from the measured phase. A common token prefix is truncated to each selected context length, every required prefix is primed before measurement, all connections wait on one barrier, and the full cohort starts together.

The base per-rank KV-length vector is:

```python
AGENTX_PATTERN_16 = [
    8193,
    57345,
    73729,
    81921,
    98305,
    106497,
    114689,
    131073,
    139265,
    147457,
    163841,
    180225,
    196609,
    212993,
    229377,
    237569,
]

RAGGED_PATTERNS = {
    8: [8193, 81921, 106497, 131073, 147457, 180225, 196609, 237569],
    16: AGENTX_PATTERN_16,
    32: AGENTX_PATTERN_16 * 2,
    64: AGENTX_PATTERN_16 * 4,
    128: AGENTX_PATTERN_16 * 8,
    160: AGENTX_PATTERN_16 * 10,
    192: AGENTX_PATTERN_16 * 12,
    224: AGENTX_PATTERN_16 * 14,
    256: AGENTX_PATTERN_16 * 16,
}
```

The values were sampled from observed AgentX prompt lengths and rounded to the nearest 8,192-token Mamba checkpoint plus one token. The range is 8,193-237,569 tokens and the exact mean is 136,193 tokens. B8 selects one representative from each adjacent quantile pair and retains the same mean. B32 and larger points repeat the frozen 16-value distribution.

B27 uses the following frozen per-rank vector and executes in the B32 CUDA Graph bucket:

```python
RAGGED_PATTERNS[27] = [
    8193, 57345, 73729, 81921, 98305, 106497, 114689, 131073,
    139265, 147457, 163841, 180225, 196609, 212993, 229377, 237569,
    8193, 73729, 81921, 106497, 114689, 139265, 147457, 180225,
    196609, 212993, 237569,
]
```

For DP4 and batch `B` per rank, the client creates `4 * B` requests. Request `i` is routed to rank `i % 4`, and its context length is `RAGGED_PATTERNS[B][(i // 4) % B]`. All four ranks therefore receive the same ordered length vector. The client first sends a one-output-token primer for every unique context length to each rank, then a 64-output-token warmup cohort, followed by the measured cohort.

The percentage columns in the performance table use:

```text
control_mean = (control_before + control_after) / 2
change = (prototype / control_mean - 1) * 100%
control_drift = (control_after / control_before - 1) * 100%
```

#### Source and A/B toggle

```bash
git clone https://github.com/YAMY1234/sglang.git
cd sglang
git checkout f8151ab14e3d00d0c55c6408f91930cba527120a
git show --stat --oneline HEAD
```

Both arms use this exact checkout. The common settings disable the older static split and reorder controls:

```bash
export SGLANG_TRTLLM_MHA_DECODE_SEQ_LEN_SPLITS=1
export SGLANG_TRTLLM_MHA_DECODE_SEQ_LEN_SPLIT_HEURISTIC=false
export SGLANG_TRTLLM_MHA_DECODE_REORDER_REQUESTS=false

# Control arm
export SGLANG_TRTLLM_MHA_DECODE_ADAPTIVE_SCHEDULER=false

# Prototype arm; restart the server after changing the value
export SGLANG_TRTLLM_MHA_DECODE_ADAPTIVE_SCHEDULER=true
```

The fixed-acceptance settings are identical in both arms:

```bash
export SGLANG_SIMULATE_ACC_LEN=4.80
export SGLANG_SIMULATE_ACC_METHOD=match-expected
export SGLANG_SIMULATE_ACC_TOKEN_MODE=fixed
export SGLANG_SIMULATE_ACC_TOKEN_ID=64
export SGLANG_ENABLE_SPEC_V2=1
```

#### Server and client commands

The final matrix used three graph-bucket groups:

| Group | Measured B/rank | `CUDA_GRAPH_BS` |
|---|---|---|
| Low | 1, 8, 32 | `1 8 32` |
| Split | 27, 64, 128 | `32 64 128` |
| Persistent | 160, 192, 224, 256 | `160 192 224 256` |

The following command shows the split group; substitute the corresponding graph-bucket row for the other groups:

```bash
export CUDA_GRAPH_BS="32 64 128"
export MODEL_PATH=/path/to/Qwen3.5-397B-A17B-NVFP4-V2

python3 -m sglang.launch_server \
  --model-path "${MODEL_PATH}" \
  --served-model-name Qwen3.5-397B-A17B-NVFP4-V2 \
  --host 0.0.0.0 \
  --port 8000 \
  --attention-backend trtllm_mha \
  --chunked-prefill-size 8192 \
  --cuda-graph-bs ${CUDA_GRAPH_BS} \
  --cuda-graph-max-bs 256 \
  --data-parallel-size 4 \
  --tensor-parallel-size 4 \
  --expert-parallel-size 4 \
  --enable-dp-attention \
  --enable-dp-lm-head \
  --disable-prefill-cuda-graph \
  --kv-cache-dtype fp8_e4m3 \
  --page-size 64 \
  --quantization modelopt_fp4 \
  --moe-a2a-backend flashinfer \
  --moe-runner-backend flashinfer_cutedsl \
  --speculative-algorithm NEXTN \
  --speculative-num-steps 5 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 6 \
  --speculative-moe-a2a-backend flashinfer \
  --speculative-moe-runner-backend deep_gemm \
  --enable-linear-replayssm-spec \
  --linear-replayssm-cache-len 32 \
  --linear-attn-decode-backend triton \
  --mamba-track-interval 8192 \
  --mamba-scheduler-strategy extra_buffer \
  --mamba-max-states-per-path 32 \
  --max-mamba-cache-size 4096 \
  --max-running-requests 1024 \
  --max-prefill-tokens 32768 \
  --mem-fraction-static 0.7 \
  --disable-shared-experts-fusion \
  --enable-cache-report \
  --enable-metrics \
  --trust-remote-code
```

After the server is healthy, a B192 ragged point is launched with:

```bash
python3 async_direct_decode_cohort.py \
  --contract contract.json \
  --url http://127.0.0.1:8000/v1/chat/completions \
  --output ragged-b192.json \
  --model Qwen3.5-397B-A17B-NVFP4-V2 \
  --mode ragged \
  --batch-per-rank 192 \
  --ranks 4 \
  --warmup-output-tokens 64 \
  --output-tokens 860 \
  --between-phases-seconds 2
```

The matched uniform point uses the same command with `--mode uniform`. Each matrix group is executed as `control_before -> prototype -> control_after`, restarting the server for each arm and changing only `SGLANG_TRTLLM_MHA_DECODE_ADAPTIVE_SCHEDULER`.

### Impact

- Throughput.
- API usability and integration complexity.
- Testing and maintainability.

### Acceptance criteria

1. Identity-order correctness and performance parity with the existing API.
2. Random-permutation correctness against physically permuted Q and KV metadata followed by output unpermutation.
3. CUDA Graph capture once, followed by replay with at least two different device-side permutations.
4. No meaningful regression for uniform KV lengths.
5. Reduced persistent-kernel tail for representative ragged batches above the SM count on Blackwell.
6. Paged-KV coverage with shared and non-shared page indices, or an explicitly documented initial subset.

### Related work, dependencies, or suggested scope

- [#1832](https://github.com/flashinfer-ai/flashinfer/issues/1832) and [#3131](https://github.com/flashinfer-ai/flashinfer/issues/3131) discuss variable query-length support; this request concerns fixed Q within a call and variable KV lengths across requests.
- The request-order pointer can be implemented independently as a first step for the B > SM persistent regime.
- The length-aware work scheduler is a larger follow-up for B <= SM and does not need to block the request-order API.

We can contribute a standalone FlashInfer microbenchmark using the frozen length distribution above and help validate an API direction preferred by the maintainers.

### Request-ordered generated export follow-up (2026-09-13)

Draft [PR #5181](https://github.com/flashinfer-ai/flashinfer/pull/5181) continues the integration after merged [PR #4980](https://github.com/flashinfer-ai/flashinfer/pull/4980). The current generated route accepts positive uniform integer Q lengths for 8Q/1KV and 32Q/2KV (D256/P64, BF16 Q/O, FP8 KV), retaining Q1/Q6 specialized schedules, caller-owned CUDA Graphs and direct device request ordering without external gather/scatter. Finite validation coverage is reported explicitly in the PR.

All 102 fresh GB300 source/export rows qualified (86 canonical plus 16 balanced supplemental). Source/export latency geomeans were 870.401806 → 870.333420 µs (1.000078574×), 2184.795260 → 2185.053695 µs (0.999881726×), 15.787895 → 15.767921 µs (1.001266756×) and 19.507227 → 19.523190 µs (0.999182338×), respectively. The final 64-file export passed all 53 installed-wheel cases, including the original 11, with zero skips. Test runtime was 204.881 s and physical turnaround 239.370 s. The two reference-loader failures in the first 51/53 attempt are preserved with the narrowly repaired selector and successful follow-up.

The generic-Q fallback remains slower than TRTLLM-GEN on the four B6 Q2/Q8 peer comparisons: ratios 0.617409×, 0.788110×, 0.697791× and 0.648575×. The PR bodies retain their absolute latencies, prior failed export measurements and all campaign durations. Export parity and wheel correctness do not establish a generic-Q or full-model speedup.

This issue remains open for final NVRTC 13.2 serving validation, the frozen 19-point/57-arm/nine-server-start A/B/A campaign and the historical FP8-Q targets: Q1 971.639 µs / 1.5242× against 1480.966 µs, and Q6 1304.136 µs / 1.4759× against 1924.955 µs. Current BF16-Q results do not establish those targets. Closure follows completed qualification and delivery.


## 评论 (4)

### yzh119 · 2026-09-15

Length-aware work scheduler is the way to go.
We are working on these kernels in cake (while the tile-wise computation use same dataflow with trtllm-gen).

### yyihuang · 2026-09-25

@YAMY1234 Update for this request: [feat(cake_fmha): add sm100/103 paged-attention](https://github.com/flashinfer-ai/flashinfer/pull/4980) was merged on 2026-09-11 (UTC).

The Blackwell Cake paged-attention backend related to this request is merged.

- Adds explicit decode/context entry points and a backend="cake" selector with exact SM100a/SM103a generated-source selection.
- Includes D256 FP8 speculative-decode coverage for Q1 through Q8 and the associated paged-attention integration.

This is the base backend delivery, not a claim that #5181 was merged or that all requested scheduling behavior came from this PR. The kernel-owned length-aware path is delivered separately in #5474 and #5490.


### yyihuang · 2026-09-25

@YAMY1234 Update for this request: [feat(cake_gqa): experimental on-device load-balanced BF16 paged GQA decode (balanced_gqa_decode) on SM100/SM103](https://github.com/flashinfer-ai/flashinfer/pull/5474) was merged on 2026-09-23 (UTC).

The kernel-owned length-aware GQA decode scheduler requested here is merged as an experimental backend.

- prepare_balanced_batch_decode_with_kv_cache(..., backend="cake") returns a runner whose persistent kernel reads device seq_lens and distributes KV work on chip.
- The same captured CUDA Graph can replay with changed KV-length distributions, without host request permutations, per-length host plans, or separate gather/scatter buffers.

Supported scope is BF16 paged GQA on SM100/SM103, head dimension 128, Hq/Hkv=8 and HND pages of 16; it is a separate experimental path, not a universal replacement for the TRTLLM-GEN API.


### yyihuang · 2026-09-25

@YAMY1234 Update for this request: [perf(cake_backend): packed-row MTP fast path for the experimental balanced_gqa_decode (q_len_per_req 3..8) on SM100/SM103](https://github.com/flashinfer-ai/flashinfer/pull/5490) was merged on 2026-09-24 (UTC).

The MTP/speculative-verification performance follow-up to the balanced GQA scheduler is merged.

- Adds packed-row programs for q_len_per_req=3..8, loading each KV block once per request work item rather than once per draft row.
- Retains on-device length-aware scheduling and graph-safe replay; q_len_per_req=1/2 keeps the original program.

Use the updated workspace-sizing helper when preparing the MTP runner; the larger MTP partial slots increase workspace requirements.

