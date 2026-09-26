# [Issue #2558] [Discussion] Adding energy consumption metrics to MLPerf Inference Benchmark

source: https://github.com/mlcommons/inference/issues/2558
state: open | updated: 2026-06-26T08:19:54Z
labels: 

## 正文

## Discussion: Energy Metrics for MLPerf Inference

### Context

MLPerf Inference currently reports throughput and latency metrics. As AI sustainability becomes a key concern, standardized energy efficiency metrics would complement existing benchmarks.

### Observation

Through systematic benchmarking of quantized LLM inference (NF4, INT8, FP16) across NVIDIA Ada Lovelace and Blackwell architectures, we found that:

1. Quantization's energy impact is non-trivial and model-size dependent
2. For models <3B parameters, NF4 quantization increases energy by 25-56%
3. INT8 mixed-precision adds 17-33% energy overhead vs FP16
4. These trade-offs are not captured by throughput/latency alone

### Suggestion

Consider adding optional energy reporting to the MLPerf Inference benchmark:

- Energy per query/token (J)
- Average power draw (W)
- Energy efficiency (tokens/J)

This would enable apples-to-apples energy comparison across hardware and quantization configurations.

### Data

- Full benchmark dataset (200+ measurements): [Zenodo](https://zenodo.org/records/18900289)
- Profiling toolkit: [EcoCompute-AI](https://github.com/hongping-zh/ecocompute-ai)
- Interactive results: [https://hongping-zh.github.io/ecocompute-dynamic-eval/](https://hongping-zh.github.io/ecocompute-dynamic-eval/)

### Related

- [huggingface/transformers#44407](https://github.com/huggingface/transformers/pull/44407) — Energy efficiency docs (approved)
- [huggingface/optimum#2410](https://github.com/huggingface/optimum/pull/2410) — Quantization energy data
- [vllm-project/vllm#36440](https://github.com/vllm-project/vllm/issues/36440) — Energy metrics feature request

## 评论 (18)

### arav-agarwal2 · 2026-03-30

Hello!

This looks like something we may be interested in, but in order to understand if this is worth considering for the wider benchmark I'd suggest you attend the MLC Power working group meeting to determine best-fit.

Feel free to join there to discuss direction and figure out potential next-steps.

### hongping-zh · 2026-03-31

Hi @arav-agarwal2,

Thank you very much for the encouraging response and for pointing me toward the MLC Power Working Group — that sounds like exactly the right forum for this discussion.

I should mention that I am currently managing a health condition that limits my ability to participate in live meetings for the time being. I very much hope this will be temporary, and I look forward to joining the Working Group sessions as soon as I am able. In the meantime, I would be grateful if we could begin the conversation asynchronously — I am happy to provide any written materials, technical summaries, or data the group might find useful for an initial evaluation.

To give a brief overview: our study identifies a **crossover effect** in quantization energy efficiency — quantization actually *increases* energy consumption for models below a critical size threshold (~3.2–3.9B parameters for NF4, ~4.0–4.6B for INT8), while delivering 15–23% savings above it. We validated this across three GPU architectures (A800, RTX 4090D, RTX 5090) using NVML-based power sampling at 10 Hz, covering 270 configurations.

All data and tools are openly available:
- **Dataset & code**: [GitHub](https://github.com/ecocompute-ai/quantization-energy-crossover)
- **Permanent archive**: [Zenodo](https://zenodo.org/records/18900289) (360 configurations including FP8 reserved for future work)

I would be happy to prepare a written brief or slide deck that could be shared with the Working Group on my behalf, if that would help move the discussion forward. Please do let me know how I can best contribute given the circumstances.

Thank you again for the warm welcome — I look forward to collaborating with the community.

Best regards,
Hongping Zhang
EcoCompute-AI Research
zhanghongping1982@gmail.com


### hongping-zh · 2026-04-01

Hi @arav-agarwal2,

Following up — I've prepared two documents for the Power Working Group's review:

1. **Executive Summary (2 pages)**: [Executive_Summary__The_Quantization_Energy_Crossover_Effect.pdf](https://drive.google.com/file/d/1adr-fOG2R2mZ93ARYo7xMCOfx7X3b-4c/view?usp=drive_link)

2. **Technical Q&A (10 pages)**: [MLC_Power_WG_Technical_QA_with_References.pdf](https://drive.google.com/file/d/13H947EvVtZ8RQe1QLE1dazlzdLC3mFNK/view?usp=drive_link)

The Q&A document specifically addresses integration with the existing MLPerf Power infrastructure (PTDaemon compatibility, output format alignment with the power-dev repository), and positions our work as a complementary data contribution — not a replacement for the current physical analyzer standard.

Could you forward these to the Power WG chairs (power-chairs@mlcommons.org), or let me know the best asynchronous channel (mailing list, Discord) to share them directly?

Thanks,  
Hongping


### JiwaniZakir · 2026-04-05

The energy overhead observed with NF4 and INT8 quantization on smaller models (<3B params) likely stems from increased memory access patterns and dequantization kernel overhead that don't amortize well at smaller model scales — the compute savings from reduced precision are outweighed by the additional memory transactions per inference pass. The current MLPerf Inference logging infrastructure in `mlperf_loadgen` captures latency and query metadata but has no hooks for power sampling, so any integration would need an external power measurement interface (e.g., NVML or RAPL) synchronized with the loadgen query boundaries to get accurate per-query energy attribution. The Zenodo dataset and the HuggingFace Optimum PR (#2410) already provide a reasonable methodology baseline that could inform what the schema for optional energy fields in the results JSON should look like.

### hongping-zh · 2026-04-06

Hi @JiwaniZakir,

Thank you for the detailed technical analysis — your points are well taken.

On the dequantization overhead mechanism: Your diagnosis aligns precisely
with our measurements. On the RTX 5090 (Blackwell), for example, Llama 3.2
1B under NF4 shows a 47% energy *increase* over FP16, while Llama 3.1 8B
under the same quantization shows a 19% energy *decrease*. The crossover
threshold shifts with GPU architecture — we observe it at ~3.4B params for
NF4 and ~1.9B for INT8 across our tested hardware.

On loadgen synchronization: Our current NVML-based profiler samples at 10
Hz with a 30-second thermal stabilization window, achieving SNR of
12:1–28:1 (CV < 2%). We have not yet implemented direct synchronization
with mlperf_loadgen query boundaries, but the NVML polling loop can be
aligned to loadgen's query start/complete timestamps via the existing
mlperf_log_detail entries. We would be glad to prototype this integration
if the WG considers it a viable path.

On the energy fields schema: We agree that an optional schema extension is
the right approach. Based on the structure of our Zenodo dataset (360+
configurations across 5 GPU generations), we could draft a minimal schema
proposal covering:

   - energy_per_query_joules (mean ± std)
   - gpu_power_draw_watts (mean, peak)
   - measurement_method (e.g., nvml, rapl, external_analyzer)
   - sampling_rate_hz
   - thermal_stabilization_seconds

This would be additive — fully optional fields that do not affect existing
result validation.

Next step question: Would it be helpful for us to put together a short RFC
or draft PR sketching this schema, or is there a preferred process within
the Power WG for proposing measurement extensions?

Best, Hongping

Zakir Jiwani ***@***.***> 于2026年4月6日周一 00:30写道：

> *JiwaniZakir* left a comment (mlcommons/inference#2558)
> <https://github.com/mlcommons/inference/issues/2558#issuecomment-4189151075>
>
> The energy overhead observed with NF4 and INT8 quantization on smaller
> models (<3B params) likely stems from increased memory access patterns and
> dequantization kernel overhead that don't amortize well at smaller model
> scales — the compute savings from reduced precision are outweighed by the
> additional memory transactions per inference pass. The current MLPerf
> Inference logging infrastructure in mlperf_loadgen captures latency and
> query metadata but has no hooks for power sampling, so any integration
> would need an external power measurement interface (e.g., NVML or RAPL)
> synchronized with the loadgen query boundaries to get accurate per-query
> energy attribution. The Zenodo dataset and the HuggingFace Optimum PR (
> #2410 <https://github.com/mlcommons/inference/pull/2410>) already provide
> a reasonable methodology baseline that could inform what the schema for
> optional energy fields in the results JSON should look like.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/mlcommons/inference/issues/2558#issuecomment-4189151075>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/A7YICI6JA3MVSRBXAVGNDV34UKC3LAVCNFSM6AAAAACWLPTMP6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHM2DCOBZGE2TCMBXGU>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### JiwaniZakir · 2026-04-06

The energy overhead for sub-3B models with NF4 is counterintuitive but aligns with what we see in practice — dequantization kernel overhead dominates at smaller model sizes where memory bandwidth savings are insufficient to compensate. For the proposed metrics, tracking energy per token rather than per query would be more meaningful for variable-length workloads like LLM inference. The submission checker PR should also validate that power measurement intervals align with the LoadGen timing boundaries to avoid off-by-one accounting in reported J/token figures.

### hongping-zh · 2026-04-06

Hi @JiwaniZakir,

Great points — both well taken.

Energy per token vs. per query: Agreed. For variable-length LLM workloads, J/token is the right normalization. We can compute this directly from our existing measurements: total energy over the generation phase divided by output token count. Updated schema proposal:

energy_per_token_joules (mean ± std across runs)
total_energy_joules (full inference pass, for cross-validation)
gpu_power_draw_watts (mean, peak)
output_token_count
measurement_method (nvml | rapl | external_analyzer)
sampling_rate_hz
thermal_stabilization_seconds
On LoadGen timing alignment: Understood — the power measurement window must match LoadGen's query start/complete boundaries exactly to avoid J/token accounting errors. Our approach would be:

Subscribe to LoadGen's QuerySamplesComplete callback to mark measurement boundaries
Align the NVML polling window to these timestamps (post-hoc trimming of samples outside the boundary)
The submission checker can validate that power_measurement_start and power_measurement_end fall within the LoadGen-reported query_start / query_complete interval, rejecting submissions with misaligned windows
We're ready to put this into a draft PR if that would be a useful next step. Would the right target repo be mlcommons/inference (loadgen side) or mlcommons/power-dev (power measurement side), or both?

Best, Hongping

### JiwaniZakir · 2026-04-06

The proposed metrics (J/query, W average, tokens/J) are a reasonable starting point, but energy-per-token should be normalized against a reference workload to account for variance in batch sizes and sequence lengths across submissions. Without that normalization, comparisons across hardware will be misleading since power draw is heavily influenced by utilization patterns. It might also be worth considering whether this should integrate with existing power measurement tools like NVIDIA's NVML or AMD's ROCm SMI to reduce implementation burden on submitters.

### hongping-zh · 2026-04-06

Hi @JiwaniZakir,

On normalization: Agreed — raw J/token without controlling for batch size and sequence length would produce misleading cross-hardware comparisons. Our proposed approach:

Energy measurements inherit the workload parameters already defined by each MLPerf scenario (Offline / Server / SingleStream), so J/token values are comparable within the same scenario
The schema explicitly records the workload context to make normalization transparent:
text


energy_per_token_joules      (mean ± std)
total_energy_joules
gpu_power_draw_watts         (mean, peak)
output_token_count
batch_size
input_sequence_length
output_sequence_length
scenario                     (offline | server | singlestream)
measurement_method           (nvml | rocm_smi | rapl | external_analyzer)
sampling_rate_hz
thermal_stabilization_seconds
This way, reviewers can filter and compare J/token across submissions under identical workload conditions, and flag outliers where utilization patterns diverge.

On tool integration: Good call on ROCm SMI — we've added it to the measurement_method enum. To reduce implementation burden on submitters, we can provide a lightweight wrapper script that abstracts the sampling interface across NVML and ROCm SMI, exposing a unified start_measurement() / stop_measurement() API. Submitters would only need to call two functions regardless of their GPU vendor. We have a working NVML implementation that can serve as the reference; extending it to ROCm SMI should be straightforward since both expose similar polling interfaces.

Best, Hongping

### JiwaniZakir · 2026-04-06

The energy-per-token metric would need careful normalization to account for batch size variance across submissions, otherwise comparisons between datacenter and edge configurations will be misleading. One practical starting point would be piggybacking on DCGM or RAPL interfaces for power sampling, which are already available on most target hardware — that reduces the instrumentation burden for submitters significantly. The calibration dataset mention from @cfRod is relevant here too, since workload consistency is a prerequisite for any energy comparison to be meaningful.

### hongping-zh · 2026-04-06

Hi @JiwaniZakir,

On normalization: Fully aligned — our previous reply proposed recording batch_size, input_sequence_length, output_sequence_length, and scenario (Offline / Server / SingleStream) alongside J/token, so that comparisons are scoped to identical workload conditions. This should address the datacenter vs. edge variance you raised.

On DCGM: Good suggestion. DCGM provides persistent sampling with lower integration overhead than raw NVML polling, which is a better fit for datacenter submitters. We've added it to the measurement method enum:

text


measurement_method: nvml | dcgm | rocm_smi | rapl | external_analyzer
Our wrapper script can abstract across all four interfaces with the same start_measurement() / stop_measurement() API.

On @cfRod's calibration dataset: Agreed that workload consistency is a prerequisite for meaningful energy comparisons. Could you point me to @cfRod's calibration dataset discussion? We want to make sure our schema and measurement protocol align with that work rather than duplicating or conflicting with it.

Best, Hongping

### JiwaniZakir · 2026-04-06

The RTX 5090 result for Llama 3.2 1B aligns with what we saw on Ada Lovelace — the dequantization penalty scales inversely with model size, which suggests the overhead is dominated by memory bandwidth pressure rather than compute. For a standardized reporting format, it would be worth separating static power baseline from inference-active power so the per-query joule figures are hardware-comparable across TDP classes. Happy to share the measurement scripts and post-processing tooling we used if it helps bootstrap a reference implementation for the optional energy reporting fields.

### hongping-zh · 2026-04-06

Hi @JiwaniZakir,

On static vs. active power separation: Strong point. Bundling idle baseline into J/token inflates the metric for low-TDP edge devices relative to high-TDP datacenter GPUs. Updated schema adds an explicit baseline field:

text


static_power_baseline_watts   (idle GPU, no inference load)
inference_active_power_watts  (mean, peak — during generation)
energy_per_token_joules       (computed from active power only)
Submitters would record a short idle-phase measurement before the inference run, and the submission checker can validate that energy_per_token is derived from the active delta rather than total system draw.

On sharing measurement scripts: That would be very valuable. We have a working NVML-based profiler (10 Hz sampling, thermal stabilization, LoadGen timestamp alignment) that could serve as one half of a reference implementation. If you share your scripts and post-processing tooling, we can merge both into a unified toolkit covering the full pipeline: sampling → LoadGen boundary alignment → static/active separation → schema-compliant output. Happy to set up a shared branch or repo for this — whatever works best on your end.

Best, Hongping

### JiwaniZakir · 2026-04-06

The J/token normalization approach makes sense for variable-length workloads, though we should be careful to scope it strictly to the generation phase — prefill energy can dominate for long-context inputs and would skew the metric if included. On the dequantization overhead: the 47% figure on Blackwell for Llama 3.2 1B is consistent with what we're seeing, and it suggests the overhead is architecture-agnostic at small model sizes, which strengthens the case for making this a standardized reporting dimension rather than a one-off observation. For the benchmark integration, would it make sense to propose J/token as a required field only for LLM tasks, with J/query retained for CV workloads where output length is fixed?

### hongping-zh · 2026-04-07

Hi @JiwaniZakir,

**On prefill vs. generation scoping:** Important distinction. For long-context inputs, prefill can dominate total energy and would inflate J/token if included. Updated approach:

- `prefill_energy_joules` (prompt processing phase)
- `generation_energy_joules` (autoregressive decoding phase)
- `energy_per_token_joules` (computed from `generation_energy_joules / output_token_count` only)

The phase boundary can be detected via the first-token timestamp in LoadGen logs (TTFT marks the prefill→generation transition).

**On architecture-agnostic overhead:** This is consistent across our dataset as well — the dequantization penalty at sub-3B scales holds across all 5 GPU generations we tested (Turing through Blackwell). The cross-architecture consistency supports treating this as a standardized reporting dimension rather than hardware-specific errata.

**On task-type differentiation:** Agreed — clean separation:

| Task type | Primary energy metric | Rationale |
|-----------|----------------------|-----------|
| LLM (variable output) | `energy_per_token_joules` (required) | Output length varies |
| CV / fixed-output | `energy_per_query_joules` (required) | Output size is deterministic |

We can drive this with a `task_type` field (`llm` | `cv` | `other`) that determines which energy metric the submission checker validates as required vs. optional.

Best,
Hongping


### hongping-zh · 2026-04-09

Hi @arav-agarwal2 and the MLC Power Working Group,

Following up on our six rounds of technical exchange — thank you again for the thorough and substantive engagement. I wanted to briefly summarize where we've landed and propose a concrete path forward.

What our exchange has established:

The quantization-energy crossover effect is methodologically sound under scrutiny (static power cancellation, SNR analysis, thermal protocol, framework rationale)
GPU-level NVML measurement complements MLPerf system-level power rather than competing with it
Our dataset covers the 1B–5B parameter range currently absent from MLPerf Inference benchmarks — precisely where the crossover occurs
Concrete proposal for WG consideration:

I would like to formally propose one of the following contributions, whichever the WG finds most actionable:

Near-term: Contribute our open dataset ([Zenodo DOI: 10.5281/zenodo.18900289](https://zenodo.org/records/18900289)) as reference data for a potential MLPerf quantization energy extension
Medium-term: Submit a Technical Note proposing energy-per-token as a supplementary metric in MLPerf Inference, alongside the existing power-constrained performance metric
Longer-term: Co-develop a new MLPerf scenario covering 1B–5B models with dequantization-on-the-fly evaluation
What I need from the group:

Does the WG see value in pursuing any of the above?
If so, what is the appropriate submission channel — a formal RFC, a Working Group meeting slot, or an async written proposal?
As noted previously, I am currently managing a health condition that limits live meeting participation. I remain fully available for asynchronous collaboration and can prepare any written briefs, data summaries, or slide materials the group requires.

Thank you for your continued consideration.

Best regards, Hongping 

### hongping-zh · 2026-04-29

Hi @JiwaniZakir (and everyone following this thread),

Quick parallel update: I've completed a full systematic write-up of the quantization-energy crossover work that has anchored much of our discussion here. The paper, *When Does Quantization Save Energy? Empirical Analysis of the Energy-Efficiency Crossover Effect Across GPU Generations*, covers:

- the 270-configuration measurement campaign (3 GPUs × 6 model families × 3 precisions × 5 batch sizes, 1.1B–9B parameters),
- a closed-form crossover threshold $N^*$ tied to memory bandwidth and dequantization overhead (Eqs. 1–5), and
- the Tesla T4 supplementary measurement of Qwen2.5-3B, which confirms the below-crossover regime in the 2–5B model-size gap.

I've added an acknowledgment recognizing your independent cross-architecture validation on Ada Lovelace — that exchange genuinely shaped my confidence in the architecture-agnostic framing, and I wanted to make sure it's reflected in the record.

Resources:

- Paper PDF + dataset + code: https://github.com/hongping-zh/ecocompute-ai (release v1.0.1)
- Zenodo archive: https://doi.org/10.5281/zenodo.18900289

If at some point you have time to skim and want to share any high-level reaction — framing, methodology caveats, or anything that strikes you — I'd genuinely value it, but absolutely no urgency on my side. The schema work remains the priority for me, and I'll continue waiting on the prefill/generation separation thread whenever you're ready to pick back up.

Best,
Hongping

### hongping-zh · 2026-06-26

Hi all,

I've been working on energy measurements for quantized LLM inference 
and wanted to share an observation that might be relevant to the WG's 
discussion on benchmark design.

We found that weight-only quantization (NF4/INT8 via bitsandbytes) 
does not always reduce energy. On RTX 4090D, models below ~3.9B 
parameters incur +25-35% energy overhead, while models above ~6B 
achieve -23% savings. The crossover point varies by GPU architecture.

This suggests that energy benchmarks may need to account for the 
interaction between precision format and model size, rather than 
treating quantization as uniformly energy-saving.

Interactive demo: https://hongping-zh.github.io/quant-energy/
Dataset (CC BY 4.0): zenodo.org/records/19647290
Preprint: papers.ssrn.com/sol3/papers.cfm?abstract_id=6854700

I'm interested in how the Power WG handles precision-format variability 
in benchmark design. Are there existing guidelines, or is this something 
the WG is still developing?

Best,
Hongping Zhang
