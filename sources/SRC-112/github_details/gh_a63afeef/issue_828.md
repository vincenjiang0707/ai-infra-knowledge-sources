# [Issue #828] [experimental] gptoss h100 nvidia-smi power / [实验性] gptoss H100 nvidia-smi 功耗监控

source: https://github.com/SemiAnalysisAI/InferenceX/issues/828
state: open | updated: 2026-07-04T05:11:59Z
labels: 

## 正文

@claude create an experimental run on 1k8k gptoss vllm h100 that tracks gpu power consumption every second during the run and saves it as an artifact in csv

## 中文说明
请求创建一个实验性运行，在 1k8k gptoss vLLM H100 上每秒跟踪 GPU 功耗，并将数据保存为 CSV 格式的产物。


## 评论 (19)

### Klaud-Cold · 2026-03-01

**Claude finished @functionstackx's task in 24m 43s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22536355468) • [`claude/issue-828-20260301-0459`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260301-0459) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260301-0459?quick_pull=1&title=%5Bexperimental%5D%20Add%20gptoss%20h100%20vllm%20GPU%20power%20monitoring&body=Add%20experimental%20benchmark%20that%20tracks%20GPU%20power%20consumption%20every%20second%20via%20nvidia-smi%20during%20the%20gptoss-fp4-h100-vllm%201k8k%20run%20and%20saves%20the%20data%20as%20a%20CSV%20artifact.%0A%0ACloses%20%23828%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### Experimental GPU Power Monitoring Run — Completed

- [x] Gather context — find gptoss h100 vllm config and understand workflow structure
- [x] Create power monitoring benchmark script (`gptoss-power_fp4_h100.sh`)
- [x] Create experimental workflow and config entry
- [x] Commit and push changes
- [x] Trigger the experimental run
- [x] Monitor execution and report results

### Configuration
| Parameter | Value |
|-----------|-------|
| Config | `gptoss-power-fp4-h100-vllm` |
| Model | `openai/gpt-oss-120b` |
| Image | `vllm/vllm-openai:v0.15.1` |
| ISL/OSL | 1024 / 8192 |
| TP | 4 |
| Concurrency | 4 |
| Runner | `h100-dgxc-slurm_1` |

### Benchmark Results
| Metric | Value |
|--------|-------|
| Throughput/GPU | 275.5 tok/s |
| Output throughput/GPU | 244.4 tok/s |
| Mean TTFT | 42.3 ms |
| Median TPOT | 4.01 ms |
| Mean E2E latency | 29.3 s |
| P99 E2E latency | 33.3 s |

### GPU Power Summary (4x H100 80GB, 1-second intervals, 494 samples/GPU)

| GPU | Avg Power | Peak Power | Avg Temp | Peak Temp | Avg Util | Peak Mem |
|-----|-----------|------------|----------|-----------|----------|----------|
| GPU 0 | 275.0 W | 356.9 W | 43.7°C | 51°C | 74.1% | 77,041 MiB |
| GPU 1 | 278.6 W | 355.9 W | 52.6°C | 64°C | 73.9% | 77,183 MiB |
| GPU 2 | 272.7 W | 352.6 W | 44.4°C | 52°C | 74.3% | 77,183 MiB |
| GPU 3 | 279.8 W | 364.8 W | 54.0°C | 66°C | 74.1% | 76,449 MiB |
| **Total** | **1,106 W** | **~1,430 W** | — | — | — | — |

Power limit: 700 W per GPU. Peak utilization: ~52% of TDP.

### Artifacts
- **GPU Power CSV** (1,977 rows): `gpu_power_gptoss-power_1k8k_fp4_vllm_tp4-ep1-dpafalse_disagg-false_spec-none_conc4_h100-dgxc-slurm_1`
- **Benchmark Result**: `bmk_gptoss-power_1k8k_fp4_vllm_tp4-ep1-dpafalse_disagg-false_spec-none_conc4_h100-dgxc-slurm_1`
- **Server Logs**: `server_logs_gptoss-power_1k8k_fp4_vllm_tp4-ep1-dpafalse_disagg-false_spec-none_conc4_h100-dgxc-slurm_1`

CSV columns: `timestamp, index, power.draw [W], power.limit [W], temperature.gpu, utilization.gpu [%], utilization.memory [%], memory.used [MiB], memory.total [MiB]`

### Files Created
- `benchmarks/single_node/gptoss-power_fp4_h100.sh` — benchmark with nvidia-smi power logging
- `.github/workflows/experimental-gptoss-power.yml` — standalone workflow_dispatch for re-runs
- `.github/configs/nvidia-master.yaml` — added `gptoss-power-fp4-h100-vllm` config
- `.github/workflows/benchmark-tmpl.yml` — added conditional GPU power CSV upload step



[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22536496441) |  |

### functionstackx · 2026-03-01

@claude thanks claude. can u try running this experiment on 8k/1k and 1k/1k too and compare and contrast the results to 1k/8k and do an detailed analysis

also create an graphing tool to graph power over time and save that as an artifact too

### Klaud-Cold · 2026-03-01

**Claude finished @functionstackx's task in 25m 39s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22536885430) • [`claude/issue-828-20260301-0534`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260301-0534) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260301-0534?quick_pull=1&title=%5Bexperimental%5D%20GPU%20power%20monitoring%20for%20gptoss%20h100%20vllm%20with%20graphing%20tool&body=Add%20experimental%20GPU%20power%20monitoring%20with%20nvidia-smi%20(1s%20intervals)%20for%20gptoss%20fp4%20h100%20vllm%20across%20three%20ISL%2FOSL%20configs%20(1k%2F1k%2C%208k%2F1k%2C%201k%2F8k).%20Includes%20a%20Python%20graphing%20tool%20that%20generates%20power-over-time%20visualizations.%0A%0ACloses%20%23828%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### GPU Power Experiments: 1k/1k, 8k/1k, 1k/8k — Complete

- [x] Gather context — read existing power monitoring scripts, configs, and workflow
- [x] Create benchmark script with power monitoring (`gptoss-power_fp4_h100.sh`)
- [x] Create Python graphing tool (`utils/plot_gpu_power.py`) — 5 chart types (per-GPU power, total power, temperature, utilization, power-vs-utilization correlation)
- [x] Update experimental workflow with ISL/OSL inputs (1k8k, 8k1k, 1k1k) and graphing step
- [x] Update configs and benchmark template
- [x] Commit and push changes
- [x] Trigger all three experiments — [Run #22537005465](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537005465)
- [x] Monitor all three runs — all completed successfully
- [x] Download results and do detailed comparative analysis

---

### Benchmark Results — All Three ISL/OSL Configs

| Metric | 1k/1k | 8k/1k | 1k/8k |
|--------|-------|-------|-------|
| **Throughput/GPU** | 470.2 tok/s | 1,908.5 tok/s | 190.0 tok/s |
| **Output tput/GPU** | 234.0 tok/s | 212.3 tok/s | 168.5 tok/s |
| **Mean TTFT** | 40.8 ms | 165.5 ms | 65.1 ms |
| **Median TPOT** | 4.12 ms | 4.46 ms | 5.87 ms |
| **Mean E2E latency** | 3.8 s | 4.2 s | 42.5 s |
| **P99 E2E latency** | 4.3 s | 4.8 s | 47.8 s |

### GPU Power Summary (4x H100 80GB, 1-second intervals)

| Config | Duration | Avg Total | Peak Total | Avg Util | Peak TDP% |
|--------|----------|-----------|------------|----------|-----------|
| **1k/1k** | 178s (179 samples/GPU) | **747 W** | 1,398 W | 29.7% | ~50% |
| **8k/1k** | 186s (187 samples/GPU) | **766 W** | 1,718 W | 31.3% | ~61% |
| **1k/8k** | 650s (650 samples/GPU) | **920 W** | 1,175 W | 80.3% | ~42% |

### Per-GPU Breakdown

<details>
<summary>1k/1k (ISL=1024, OSL=1024) — slurm_4</summary>

| GPU | Avg Power | Peak Power | Avg Temp | Peak Temp | Avg Util |
|-----|-----------|------------|----------|-----------|----------|
| GPU 0 | 175.4 W | 334.8 W | 35.5°C | 46°C | 29.7% |
| GPU 1 | 190.7 W | 361.0 W | 56.0°C | 65°C | 29.7% |
| GPU 2 | 172.1 W | 333.6 W | 36.5°C | 48°C | 28.6% |
| GPU 3 | 208.6 W | 369.0 W | 67.7°C | 76°C | 29.7% |

</details>

<details>
<summary>8k/1k (ISL=8192, OSL=1024) — slurm_9</summary>

| GPU | Avg Power | Peak Power | Avg Temp | Peak Temp | Avg Util |
|-----|-----------|------------|----------|-----------|----------|
| GPU 0 | 189.2 W | 419.8 W | 36.9°C | 50°C | 31.8% |
| GPU 1 | 190.8 W | 434.4 W | 40.3°C | 57°C | 31.3% |
| GPU 2 | 187.9 W | 429.5 W | 36.7°C | 52°C | 30.8% |
| GPU 3 | 198.2 W | 434.6 W | 41.5°C | 60°C | 31.3% |

</details>

<details>
<summary>1k/8k (ISL=1024, OSL=8192) — slurm_6</summary>

| GPU | Avg Power | Peak Power | Avg Temp | Peak Temp | Avg Util |
|-----|-----------|------------|----------|-----------|----------|
| GPU 0 | 228.3 W | 273.0 W | 35.1°C | 39°C | 80.3% |
| GPU 1 | 236.3 W | 281.4 W | 39.4°C | 43°C | 80.4% |
| GPU 2 | 233.9 W | 278.4 W | 36.5°C | 39°C | 80.2% |
| GPU 3 | 221.7 W | 342.6 W | 85.5°C | 90°C | 80.4% |

</details>

---

### Power Efficiency Analysis

| Metric | 1k/1k | 8k/1k | 1k/8k |
|--------|-------|-------|-------|
| **Total tok/s (4 GPUs)** | 1,881 | 7,634 | 760 |
| **Avg Power (4 GPUs)** | 747 W | 766 W | 920 W |
| **Energy consumed** | 36.9 Wh | 39.6 Wh | 166.1 Wh |
| **Total tok/s per Watt** | 2.52 | **9.97** | 0.83 |
| **Output tok/s per Watt** | **1.25** | 1.11 | 0.73 |
| **Watts per output tok/s** | **0.80** | 0.90 | 1.37 |

---

### Detailed Analysis: Compare & Contrast

#### 1. Power Consumption Patterns

**1k/8k (decode-heavy) draws the most average power (920 W) but has the lowest peak (1,175 W).** This is because long-output generation sustains high GPU utilization (~80%) for extended periods, keeping all GPUs consistently busy with autoregressive decoding. The power draw is steady and sustained — there are no dramatic spikes because each decode step does similar work.

**8k/1k (prefill-heavy) has the highest peak power (1,718 W) but moderate average (766 W).** Large prefill sequences create intense bursts of compute during the attention/FFN forward passes on 8K-token prompts, causing sharp power spikes to ~430 W per GPU. But since output generation is short (1K tokens), the run finishes quickly and the overall average stays low.

**1k/1k (balanced) has the lowest average (747 W) and moderate peak (1,398 W).** With both short inputs and outputs, each request completes rapidly. The GPUs cycle between active computation and brief idle periods between batches, keeping average utilization low (~30%).

#### 2. GPU Utilization vs Power

The most striking difference is GPU utilization:
- **1k/8k: 80% average utilization** — GPUs are nearly fully occupied generating 8K output tokens per request
- **8k/1k & 1k/1k: ~30% utilization** — despite high peak compute during prefill/decode, the short sequence lengths mean requests complete quickly and GPUs idle between batches

This explains why 1k/8k has higher *average* power despite lower *peak* power — sustained utilization matters more than burst capability for energy consumption.

#### 3. Energy Efficiency

**8k/1k is the most token-efficient** at 9.97 total tok/s per Watt, driven by the "cheap" prefill tokens (reading is cheaper than writing). Prefilling 8K input tokens requires one forward pass, while generating 8K output tokens requires 8K sequential forward passes.

**1k/1k is the most output-efficient** at 1.25 output tok/s per Watt (0.80 W per output tok/s). With balanced and short sequences, the GPU cycles efficiently without the sustained thermal load of long decodes.

**1k/8k is the least efficient** at 0.73 output tok/s per Watt (1.37 W per output tok/s), consuming **4.5x more total energy** than the other configs. The long decode sequences keep GPUs at sustained high power for ~10 minutes vs ~3 minutes.

#### 4. Thermal Behavior

GPU 3 consistently runs hotter across all configs (67-90°C vs 35-50°C for GPU 0). This suggests a physical placement or cooling asymmetry in the DGXC chassis. In the 1k/8k config, GPU 3 reached **90°C** — approaching thermal throttling territory — due to sustained high utilization for ~10 minutes. The other configs stay well within thermal limits due to shorter run times.

#### 5. TPOT Scaling

TPOT (time per output token) increases with sequence length context:
- **1k/1k: 4.12 ms** — minimal KV cache, fastest decode
- **8k/1k: 4.46 ms** — larger KV cache from 8K prefill, 8% slower decode
- **1k/8k: 5.87 ms** — growing KV cache during 8K generation, 42% slower decode

This demonstrates how KV cache size impacts decode latency — more context means more memory bandwidth pressure during attention.

#### 6. Key Takeaways

| Insight | Detail |
|---------|--------|
| **Prefill is cheap, decode is expensive** | 8k/1k uses only 766 W avg for 7,634 tok/s total; 1k/8k uses 920 W for only 760 tok/s |
| **Sustained decode dominates energy** | 1k/8k consumes 166 Wh vs 37-40 Wh for the others — a 4x energy multiplier |
| **Peak power != Average power** | 8k/1k has the highest peak (1,718 W) but 8k/1k's average is similar to 1k/1k's |
| **GPU utilization tells the real story** | 80% sustained (1k/8k) vs 30% bursty (1k/1k, 8k/1k) |
| **Thermal asymmetry matters at scale** | GPU 3 hitting 90°C during 1k/8k — a concern for sustained long-generation workloads |

---

### Artifacts

All artifacts are available in the workflow run:
- **GPU Power CSVs**: `gpu_power_gptoss-power_{1k1k,8k1k,1k8k}_*` (1-second nvidia-smi samples)
- **Benchmark Results**: `bmk_gptoss-power_{1k1k,8k1k,1k8k}_*` (aggregated JSON)
- **Server Logs**: `server_logs_gptoss-power_{1k1k,8k1k,1k8k}_*`
- **Aggregated Results**: `results_bmk` (all three combined)

### Graphing Tool

The `utils/plot_gpu_power.py` tool generates 5 charts from any nvidia-smi power CSV:
1. **Per-GPU power over time** — individual traces with power limit reference
2. **Total power over time** — aggregate with avg/peak markers
3. **Temperature over time** — per-GPU thermal tracking
4. **Utilization over time** — GPU compute utilization
5. **Power vs utilization scatter** — correlation analysis

Usage: `python3 utils/plot_gpu_power.py gpu_power.csv --output-dir plots/ --title "Run label"`

The experimental workflow (`experimental-gptoss-power.yml`) also has a built-in graphing step that auto-generates plots and uploads them as artifacts.

---



[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537005465) |  | [`claude/issue-828-20260301-0534`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260301-0534)

### functionstackx · 2026-03-01

@claude thanks claude. can u try running this experiment for all of these concurrency on h100 gptoss and then analyze the results

1k/1k
- TP8 from conc 4,8,16,32, 64
- TP4 conc 64
- TP2 conc 64

1k/8k
- TP8 from conc 4,8,16,32 64
- TP4 conc 64
- TP2 conc 64

8k/1k
- TP8 conc 4,8
- TP4 conc 4,8,16,32,64
- TP2 conc 64


### Klaud-Cold · 2026-03-01

**Claude finished @functionstackx's task in 59m 53s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537293745) • [`claude/issue-828-20260301-0603`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260301-0603) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260301-0603?quick_pull=1&title=%5Bexperimental%5D%20GPU%20power%20monitoring%20sweep%3A%20gptoss%20h100%20vllm%20TP2%2F4%2F8%20x%20conc4-64&body=Add%20experimental%20GPU%20power%20monitoring%20benchmarks%20for%20gptoss%20fp4%20h100%20vllm%20across%2022%20configurations%20(TP2%2F4%2F8%20%C3%97%20concurrency%204-64%20%C3%97%20ISL%2FOSL%201k1k%2F1k8k%2F8k1k).%20Includes%20nvidia-smi%20power%20logging%2C%20graphing%20tool%2C%20and%20detailed%20comparative%20analysis.%0A%0ACloses%20%23828%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### GPU Power Experiments: Multi-TP, Multi-Concurrency Sweep — Complete

- [x] Gather context — read existing power monitoring scripts, configs, and workflow
- [x] Create power monitoring benchmark script, plotting tool, and configs
- [x] Create configs for all 22 TP/concurrency combinations across 3 ISL/OSL configs
- [x] Add GPU power CSV upload step to benchmark template
- [x] Commit and push changes
- [x] Trigger the sweep — [Run #22537483477](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537483477)
- [x] Monitor execution — 22/22 succeeded (3 re-run after runner issue)
- [x] Download results and perform detailed comparative analysis

---

### Full Benchmark Results — All 22 Configs

**Model:** `openai/gpt-oss-120b` (FP4) | **Image:** `vllm/vllm-openai:v0.15.1` | **Hardware:** H100 DGXC

<details>
<summary><strong>1K/1K (ISL=1024, OSL=1024)</strong> — 7 configs</summary>

| TP | Conc | Tput/GPU | Out Tput/GPU | TTFT (ms) | TPOT (ms) | E2E (s) | P99 E2E (s) |
|---:|-----:|---------:|-------------:|----------:|----------:|--------:|------------:|
| 2 | 64 | 4,123.9 | 2,061.5 | 164.3 | 15.21 | 14.0 | 16.3 |
| 4 | 64 | 3,144.2 | 1,571.8 | 113.1 | 9.89 | 9.2 | 10.6 |
| 8 | 4 | 260.5 | 129.6 | 31.5 | 3.72 | 3.4 | 3.8 |
| 8 | 8 | 475.0 | 238.4 | 37.3 | 4.05 | 3.8 | 4.2 |
| 8 | 16 | 814.8 | 405.2 | 44.2 | 4.83 | 4.4 | 5.0 |
| 8 | 32 | 1,326.3 | 664.2 | 57.2 | 5.82 | 5.4 | 6.2 |
| 8 | 64 | 2,106.9 | 1,053.2 | 87.3 | 7.36 | 6.8 | 7.9 |

</details>

<details>
<summary><strong>1K/8K (ISL=1024, OSL=8192)</strong> — 7 configs</summary>

| TP | Conc | Tput/GPU | Out Tput/GPU | TTFT (ms) | TPOT (ms) | E2E (s) | P99 E2E (s) |
|---:|-----:|---------:|-------------:|----------:|----------:|--------:|------------:|
| 2 | 64 | 2,428.9 | 2,159.3 | 162.5 | 14.58 | 107.0 | 121.6 |
| 4 | 64 | 1,835.3 | 1,631.6 | 107.8 | 9.63 | 70.6 | 79.5 |
| 8 | 4 | 150.7 | 133.6 | 32.8 | 3.68 | 26.8 | 30.0 |
| 8 | 8 | 273.4 | 242.9 | 38.2 | 4.00 | 29.5 | 32.9 |
| 8 | 16 | 479.1 | 425.7 | 44.3 | 4.53 | 33.8 | 38.2 |
| 8 | 32 | 780.9 | 694.7 | 59.0 | 5.65 | 41.6 | 46.6 |
| 8 | 64 | 552.9 | 491.5 | 158.0 | 16.01 | 117.8 | 133.8 |

</details>

<details>
<summary><strong>8K/1K (ISL=8192, OSL=1024)</strong> — 8 configs</summary>

| TP | Conc | Tput/GPU | Out Tput/GPU | TTFT (ms) | TPOT (ms) | E2E (s) | P99 E2E (s) |
|---:|-----:|---------:|-------------:|----------:|----------:|--------:|------------:|
| 2 | 64 | 10,345.2 | 1,147.7 | 931.5 | 27.19 | 25.4 | 36.7 |
| 4 | 4 | 1,908.6 | 212.3 | 166.0 | 4.45 | 4.2 | 4.9 |
| 4 | 8 | 3,044.9 | 342.3 | 202.5 | 5.57 | 5.3 | 6.5 |
| 4 | 16 | 4,562.5 | 505.6 | 256.8 | 7.52 | 7.1 | 8.7 |
| 4 | 32 | 2,280.9 | 255.1 | 1,132.5 | 30.56 | 28.6 | 38.0 |
| 4 | 64 | 8,137.7 | 902.8 | 639.4 | 17.21 | 16.1 | 22.9 |
| 8 | 4 | 1,080.5 | 120.2 | 124.7 | 3.95 | 3.7 | 4.3 |
| 8 | 8 | 1,851.2 | 208.1 | 151.1 | 4.59 | 4.4 | 5.2 |

</details>

---

### Analysis 1: TP Scaling at Concurrency=64

| Config | TP | Tput/GPU | Total Tput | Out/GPU | Total Out | TPOT (ms) | E2E (s) |
|--------|---:|---------:|-----------:|--------:|----------:|----------:|--------:|
| **1k/1k** | 2 | 4,124 | 8,248 | 2,062 | 4,123 | 15.21 | 14.0 |
| | 4 | 3,144 | 12,577 | 1,572 | 6,287 | 9.89 | 9.2 |
| | 8 | 2,107 | 16,855 | 1,053 | 8,426 | 7.36 | 6.8 |
| **1k/8k** | 2 | 2,429 | 4,858 | 2,159 | 4,319 | 14.58 | 107.0 |
| | 4 | 1,835 | 7,341 | 1,632 | 6,526 | 9.63 | 70.6 |
| | 8 | 553 | 4,423 | 492 | 3,932 | 16.01 | 117.8 |
| **8k/1k** | 2 | 10,345 | 20,691 | 1,148 | 2,295 | 27.19 | 25.4 |
| | 4 | 8,138 | 32,551 | 903 | 3,611 | 17.21 | 16.1 |

**Key findings:**

**1k/1k — More GPUs = more total throughput, but diminishing per-GPU efficiency:**
- TP2→TP4: +52% total throughput for 2x GPUs (76% efficient)
- TP4→TP8: +34% total throughput for 2x GPUs (67% efficient)
- TP2 has the highest per-GPU efficiency (4,124 tok/s/GPU), TP8 has the highest total throughput (16,855 tok/s)

**1k/8k — TP8 COLLAPSES at conc=64 (decode-heavy is TP-sensitive):**
- TP4 is the sweet spot: 7,341 total tok/s with 9.63ms TPOT
- TP8 actually **regresses** to only 4,423 total tok/s (40% less than TP4!) with 16.01ms TPOT
- TP2 matches TP8's total throughput (4,858 vs 4,423) with only 2 GPUs
- **At high concurrency with long outputs, TP8 over-parallelizes and creates excessive cross-GPU communication overhead**

**8k/1k — TP4 dominates for prefill-heavy workloads:**
- TP4 conc64 achieves the highest total throughput in the entire experiment: **32,551 tok/s**
- TP2 gets enormous per-GPU efficiency (10,345 tok/s/GPU) because prefill parallelizes well within fewer GPUs

---

### Analysis 2: Concurrency Scaling (TP8)

| Config | Conc | Tput/GPU | Scaling Efficiency | TPOT (ms) | E2E (s) |
|--------|-----:|---------:|-------------------:|----------:|--------:|
| **1k/1k** | 4 | 260.5 | 100% | 3.72 | 3.4 |
| | 8 | 475.0 | 91% | 4.05 | 3.8 |
| | 16 | 814.8 | 78% | 4.83 | 4.4 |
| | 32 | 1,326.3 | 64% | 5.82 | 5.4 |
| | 64 | 2,106.9 | 51% | 7.36 | 6.8 |
| **1k/8k** | 4 | 150.7 | 100% | 3.68 | 26.8 |
| | 8 | 273.4 | 91% | 4.00 | 29.5 |
| | 16 | 479.1 | 79% | 4.53 | 33.8 |
| | 32 | 780.9 | 65% | 5.65 | 41.6 |
| | 64 | 552.9 | **23%** | 16.01 | 117.8 |
| **8k/1k** | 4 | 1,080.5 | 100% | 3.95 | 3.7 |
| | 8 | 1,851.2 | 86% | 4.59 | 4.4 |

**Key findings:**

- **1k/1k scales predictably** with concurrency — throughput grows monotonically from 260→2,107 tok/s/GPU (8.1x for 16x concurrency increase). TPOT degrades gracefully from 3.72→7.36ms.

- **1k/8k hits a HARD WALL at TP8 conc64** — throughput actually *drops* from 781 (conc32) to 553 (conc64), a **29% regression**. TPOT jumps from 5.65→16.01ms (2.8x). The KV cache for 64 concurrent 8K-output sequences exhausts GPU memory, forcing excessive swapping or reduced batch sizes. **Concurrency sweet spot for 1k/8k TP8 is conc=32.**

- **8k/1k scales well up to conc8** at 86% efficiency — limited data points but the trend is healthy.

---

### Analysis 3: Concurrency Scaling (TP4 for 8k/1k)

| Conc | Tput/GPU | Scaling Eff | TPOT (ms) | TTFT (ms) | E2E (s) |
|-----:|---------:|------------:|----------:|----------:|--------:|
| 4 | 1,909 | 100% | 4.45 | 166 | 4.2 |
| 8 | 3,045 | 80% | 5.57 | 203 | 5.3 |
| 16 | 4,563 | 60% | 7.52 | 257 | 7.1 |
| 32 | 2,281 | **9%** | 30.56 | 1,133 | 28.6 |
| 64 | 8,138 | 27% | 17.21 | 639 | 16.1 |

**Notable anomaly:** 8k/1k TP4 conc32 shows a massive performance dip (2,281 vs 4,563 at conc16 and 8,138 at conc64). TTFT spikes to 1,133ms and TPOT to 30.56ms. This suggests a specific scheduling pathology at conc32 — likely hitting a KV cache boundary or attention memory fragmentation. **The conc64 result recovers** because vLLM may use more aggressive chunked prefill or different scheduling at higher concurrency.

---

### Analysis 4: Best Configurations

| Metric | Best Config | Value |
|--------|-------------|-------|
| **Highest total throughput** | 8k/1k TP4 conc64 | 32,551 tok/s (4 GPUs) |
| **Highest per-GPU throughput** | 8k/1k TP2 conc64 | 10,345 tok/s/GPU |
| **Highest output throughput/GPU** | 1k8k TP2 conc64 | 2,159 tok/s/GPU |
| **Lowest TPOT** | 1k8k TP8 conc4 | 3.68 ms |
| **Lowest TTFT** | 1k1k TP8 conc4 | 31.5 ms |
| **Lowest E2E latency** | 1k1k TP8 conc4 | 3.4 s |
| **Best latency-throughput balance** | 1k1k TP4 conc64 | 3,144 tput, 9.89ms TPOT |

---

### Analysis 5: Key Insights

#### 1. TP2 is the per-GPU efficiency champion
- At conc=64, TP2 consistently achieves the highest per-GPU throughput across all configs
- 1k/1k: **4,124** tok/s/GPU (TP2) vs 2,107 (TP8) — **1.96x more efficient per GPU**
- 1k/8k: **2,429** tok/s/GPU (TP2) vs 553 (TP8) — **4.4x more efficient per GPU**
- For cost-optimized deployments, TP2 with more model replicas would be more efficient than TP8

#### 2. TP8 over-parallelization for decode-heavy workloads
- 1k/8k TP8 conc64 is the worst performing config relative to GPU count
- Total throughput (4,423) is **less than TP2** (4,858) despite using 4x more GPUs
- The cross-GPU communication overhead during autoregressive decoding dominates at high TP
- **Recommendation: For long-output generation (8K+), use TP4 not TP8**

#### 3. Concurrency sweet spots differ by workload
- **1k/1k:** Scales smoothly — push concurrency as high as your latency SLA allows
- **1k/8k TP8:** Hard limit at conc=32 (conc64 regresses 29%). Use TP4 for conc≥32
- **8k/1k TP4:** Anomalous dip at conc32 — skip to conc64 or stay at conc16

#### 4. Prefill is embarrassingly parallel, decode is not
- 8k/1k (prefill-heavy) reaches 32,551 total tok/s at TP4 conc64
- 1k/8k (decode-heavy) maxes out at 7,341 total tok/s at TP4 conc64
- **4.4x throughput gap** between prefill-dominated and decode-dominated workloads
- This validates the case for disaggregated prefill/decode architectures

#### 5. TPOT scales with TP (lower is better)
- TP8 conc4: ~3.7ms TPOT across all configs (best latency)
- TP4 conc64: ~10-17ms TPOT
- TP2 conc64: ~15-27ms TPOT
- **TP8 is the latency champion** — use it when per-request latency matters more than throughput

---

### Artifacts
All artifacts available in [Run #22537483477](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537483477):
- **Benchmark Results** (`bmk_*`): 22 aggregated JSON results
- **GPU Power CSVs** (`gpu_power_*`): 1-second nvidia-smi samples where available
- **Server Logs** (`server_logs_*`): vLLM server output
- **Aggregated Results** (`results_bmk`): Combined JSON for analysis

### Files Created
- `benchmarks/single_node/gptoss-power_fp4_h100.sh` — benchmark with nvidia-smi power logging
- `.github/workflows/experimental-gptoss-power-sweep.yml` — standalone matrix workflow (22 jobs)
- `.github/workflows/experimental-gptoss-power.yml` — single-run workflow for ad hoc experiments
- `.github/workflows/benchmark-tmpl.yml` — added conditional GPU power CSV upload step
- `utils/plot_gpu_power.py` — power/temp/utilization graphing tool
- `.github/configs/nvidia-master.yaml` — added `gptoss-power-fp4-h100-vllm` config



[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537483477) | [`claude/issue-828-20260301-0603`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260301-0603)

### functionstackx · 2026-03-01

@claude analyze power draw vs concurrency and power draw vs interactivity

### Klaud-Cold · 2026-03-01

**Claude finished @functionstackx's task in 5m 31s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22538404685)

---
### Power Draw Analysis: Concurrency & Interactivity

- [x] Gather benchmark results and GPU power data from workflow runs
- [x] Analyze power draw vs concurrency
- [x] Analyze power draw vs interactivity (ISL/OSL ratio impact)
- [x] Synthesize findings and produce detailed report

*Data: 22 GPU power CSVs + benchmark results across 22 configs, [Run #22537483477](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537483477). Model: gpt-oss-120b FP4 on H100 DGXC.*

---

### Part 1: Power Draw vs Concurrency

#### 1k/1k (balanced — ISL=1024, OSL=1024) — TP8, 8x H100

| Conc | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | TPOT | J/out_tok | out_tok/W |
|-----:|----------:|-----------:|------:|---------:|------------:|-----:|----------:|----------:|
| 4 | 1,275 W | 2,189 W | 159 W | 27.3% | 129.6 | 3.71 ms | 1.23 J | 0.81 |
| 8 | 1,382 W | 2,570 W | 173 W | 29.4% | 238.4 | 4.07 ms | 0.72 J | 1.38 |
| 16 | 1,509 W | 2,866 W | 189 W | 31.7% | 405.2 | 4.78 ms | 0.47 J | 2.15 |
| 32 | 1,640 W | 3,253 W | 205 W | 35.1% | 664.2 | 5.82 ms | 0.31 J | 3.24 |
| 64 | 1,370 W | 3,519 W | 171 W | 24.2% | 1,053.2 | 7.29 ms | 0.16 J | **6.15** |

**Key findings:**
- **Average power scales sublinearly with concurrency.** 16x concurrency increase (4→64) only increases average power by 8% (1,275→1,370 W). At conc64 average power actually *drops below* conc32 — the GPUs spend more time in efficient batched decode and less time in idle gaps.
- **Peak power scales much faster** — from 2,189 W to 3,519 W (61% increase), driven by larger prefill batches at higher concurrency.
- **Energy efficiency improves dramatically with concurrency.** At conc4 each output token costs 1.23 J; at conc64 it's only 0.16 J — a **7.7x improvement**. Concurrency amortizes the fixed idle/overhead power across more useful work.
- **The "free lunch" zone is conc4→32**: power goes up only 29% while throughput goes up 5.1x.

#### 1k/8k (decode-heavy — ISL=1024, OSL=8192) — TP8, 8x H100

| Conc | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | TPOT | J/out_tok | out_tok/W |
|-----:|----------:|-----------:|------:|---------:|------------:|-----:|----------:|----------:|
| 4 | 1,777 W | 2,209 W | 222 W | 72.2% | 133.6 | 3.68 ms | 1.66 J | 0.60 |
| 8 | 2,027 W | 2,502 W | 253 W | 80.7% | 242.9 | 4.00 ms | 1.04 J | 0.96 |
| 16 | 2,325 W | 2,969 W | 291 W | 76.5% | 425.7 | 4.57 ms | 0.68 J | 1.46 |
| 32 | 2,468 W | 3,059 W | 309 W | 79.1% | 694.7 | 5.61 ms | 0.44 J | 2.25 |
| 64 | 1,957 W | 3,352 W | 245 W | 91.2% | 491.5 | 15.93 ms | 0.50 J | 2.01 |

**Key findings:**
- **Decode-heavy workloads draw 40-70% more average power** than balanced workloads at the same concurrency. At conc4: 1,777 W (1k/8k) vs 1,275 W (1k/1k) — a 39% increase.
- **Power peaks at conc32 (2,468 W avg) then drops at conc64 (1,957 W)**. But this drop is misleading — throughput also collapses (694.7→491.5 out/GPU), meaning the GPU is thrashing on KV cache pressure rather than doing useful work.
- **Conc64 breaks the efficiency curve.** Energy per token goes *up* from 0.44 J (conc32) to 0.50 J (conc64). This is the conc32 wall identified earlier — for 1k/8k TP8, concurrency 32 is the efficiency sweet spot.
- **The GPU utilization tells the story:** 91.2% at conc64 (saturated) vs 79.1% at conc32 (headroom). Higher utilization with lower throughput = wasted cycles on memory management.

#### Power Elasticity (% power increase per % concurrency increase)

| Config | conc4→8 | conc8→16 | conc16→32 | conc32→64 |
|--------|--------:|---------:|----------:|----------:|
| **1k/1k** | 0.084 | 0.092 | 0.087 | **-0.031** |
| **1k/8k** | 0.140 | 0.147 | 0.062 | **-0.207** |

- **1k/1k has near-constant power elasticity** (~0.09) — every doubling of concurrency adds ~9% power. It stays efficient all the way up.
- **1k/8k has declining then negative elasticity** — power *decreases* at conc64 because the system can't maintain the same compute intensity under KV cache pressure.
- **The negative elasticity at conc64 for 1k/8k is a red flag** — the system is spending power on overhead (memory operations, scheduling) rather than useful computation.

---

### Part 2: Power Draw vs Interactivity

#### TP8 — Same concurrency, different ISL/OSL ratios

**Conc=4 (latency-optimized)**
| ISL/OSL | Avg Power | Peak Power | GPU Util | TPOT | J/out_tok |
|---------|----------:|-----------:|---------:|-----:|----------:|
| **1k/1k** | 1,275 W | 2,189 W | 27.3% | 3.71 ms | 1.23 J |
| **8k/1k** | 1,373 W | 2,797 W | 28.8% | 3.93 ms | 1.43 J |
| **1k/8k** | 1,777 W | 2,209 W | 72.2% | 3.68 ms | 1.66 J |

**Conc=8**
| ISL/OSL | Avg Power | Peak Power | GPU Util | TPOT | J/out_tok |
|---------|----------:|-----------:|---------:|-----:|----------:|
| **1k/1k** | 1,382 W | 2,570 W | 29.4% | 4.07 ms | 0.72 J |
| **8k/1k** | 1,473 W | 3,511 W | 30.5% | 4.56 ms | 0.88 J |
| **1k/8k** | 2,027 W | 2,502 W | 80.7% | 4.00 ms | 1.04 J |

**Conc=64 (throughput-optimized)**
| ISL/OSL | Avg Power | Peak Power | GPU Util | TPOT | J/out_tok |
|---------|----------:|-----------:|---------:|-----:|----------:|
| **1k/1k** | 1,370 W | 3,519 W | 24.2% | 7.29 ms | 0.16 J |
| **1k/8k** | 1,957 W | 3,352 W | 91.2% | 15.93 ms | 0.50 J |

**Key findings:**

**1. Decode ratio directly drives average power.** The ratio of output to total tokens (decode%) is the strongest predictor of average power draw:
- 1k/1k (50% decode) → moderate power
- 8k/1k (11% decode) → lowest average power, highest peak power
- 1k/8k (89% decode) → highest average power, lowest peak power

At conc4: 1k/8k draws **39% more average power** than 1k/1k despite nearly identical TPOT (~3.7ms). The power goes to sustaining continuous autoregressive decode across all GPUs.

**2. Prefill-heavy (8k/1k) has the highest peak-to-average ratio.**
- 8k/1k conc8: peak/avg = 3,511/1,473 = **2.38x** (most bursty)
- 1k/8k conc8: peak/avg = 2,502/2,027 = **1.23x** (most steady)
- 1k/1k conc8: peak/avg = 2,570/1,382 = **1.86x** (moderate)

Prefill creates sharp power spikes that dwarf the decode baseline. For power provisioning and cooling design, the 8k/1k pattern creates the worst-case transients.

**3. Power burstiness (coefficient of variation) inversely correlates with decode ratio.**

| Config | Power CV | Decode % | Pattern |
|--------|--------:|--------:|---------|
| 1k/1k TP8 conc64 | 0.714 | 50% | Very bursty |
| 8k/1k TP4 conc16 | 0.655 | 11% | Very bursty |
| 1k/8k TP8 conc64 | 0.163 | 89% | Very steady |
| 1k/8k TP8 conc4 | 0.275 | 89% | Steady |

Decode-heavy workloads produce **flat, sustained power** (CV ~0.2-0.3). Prefill-heavy and balanced workloads produce **bursty, spiky power** (CV ~0.5-0.7). This has major implications for power delivery and UPS sizing.

**4. Interactivity (TPOT) is power-agnostic at low concurrency.**

At conc=4, all three ISL/OSL ratios achieve nearly identical TPOT (~3.7 ms) despite vastly different power draws (1,275 W vs 1,777 W). **Interactivity at low load is determined by TP parallelism, not by workload type.** The power difference is "wasted" on keeping GPUs busy between requests.

At conc=64, TPOT diverges dramatically: 7.29 ms (1k/1k) vs 15.93 ms (1k/8k). **Under load, decode-heavy workloads sacrifice interactivity AND consume more power** — the worst of both worlds.

---

### Part 3: Power-Interactivity Pareto Frontier

For a given power budget, which configs deliver the best interactivity?

| Power Budget | Best TPOT Config | TPOT | Out tok/W |
|--------------|------------------|-----:|----------:|
| < 800 W | 1k/1k TP2 conc64 | 15.0 ms | 5.20 |
| < 1,000 W | 8k/1k TP4 conc4 | 4.4 ms | 1.09 |
| < 1,300 W | 1k/1k TP8 conc4 | 3.7 ms | 0.81 |
| < 1,500 W | 1k/1k TP8 conc16 | 4.8 ms | 2.15 |
| < 2,000 W | 1k/8k TP8 conc4 | 3.7 ms | 0.60 |

**The Pareto-optimal configs are:**
1. **Best absolute TPOT:** 1k/8k TP8 conc4 — 3.68 ms, but at 1,777 W (expensive)
2. **Best TPOT per Watt:** 1k/1k TP8 conc4 — 3.71 ms at only 1,275 W
3. **Best efficiency at good TPOT:** 1k/1k TP8 conc32 — 5.82 ms at 0.31 J/tok

---

### Part 4: Energy Cost per Output Token

| Rank | Config | J/out_tok | kWh/1M tok | $/1M tok |
|-----:|--------|----------:|-----------:|---------:|
| 1 | 1k/1k TP8 conc64 | 0.163 J | 0.045 | $0.005 |
| 2 | 1k/1k TP4 conc64 | 0.192 J | 0.053 | $0.005 |
| 3 | 1k/1k TP2 conc64 | 0.193 J | 0.054 | $0.005 |
| 4 | 1k/8k TP2 conc64 | 0.266 J | 0.074 | $0.007 |
| 5 | 1k/8k TP4 conc64 | 0.286 J | 0.079 | $0.008 |
| ... | | | | |
| 20 | 1k/1k TP8 conc4 | 1.23 J | 0.342 | $0.034 |
| 21 | 8k/1k TP8 conc4 | 1.43 J | 0.397 | $0.040 |
| 22 | 1k/8k TP8 conc4 | 1.66 J | 0.462 | $0.046 |

*(Energy cost assumes $0.10/kWh data center rate)*

The most energy-efficient config (1k/1k TP8 conc64 at 0.16 J/tok) is **10x cheaper** than the most latency-optimal config (1k/8k TP8 conc4 at 1.66 J/tok).

---

### Part 5: Key Takeaways

| Insight | Detail |
|---------|--------|
| **Concurrency is free power** | 16x concurrency increase adds only 8% average power for 1k/1k — amortization of idle power is the biggest efficiency lever |
| **Decode dominates power draw** | 1k/8k draws 40-70% more average power than 1k/1k at the same concurrency, driven by sustained autoregressive compute |
| **Prefill dominates power spikes** | 8k/1k has 2.4x peak-to-average ratio vs 1.2x for 1k/8k — prefill creates the power transients, decode creates the sustained load |
| **Power burstiness tracks decode ratio** | CV 0.16 (1k/8k, steady) to 0.71 (1k/1k conc64, bursty) — critical for power delivery design |
| **TPOT is power-agnostic at low load** | All ISL/OSL ratios achieve ~3.7ms TPOT at conc4 despite 40% power difference |
| **Concurrency wall = efficiency wall** | 1k/8k TP8 hits diminishing returns at conc32 — conc64 regresses both throughput AND efficiency |
| **Energy cost spans 10x** | 0.16 J/tok (1k/1k conc64) to 1.66 J/tok (1k/8k conc4) — configuration choices matter more than hardware for energy efficiency |
| **TP2 at conc64 is the efficiency sweet spot** | Best per-GPU output throughput with lowest total power — ideal for cost-optimized deployments |

---

[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537483477) | [`claude/issue-828-20260301-0603`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260301-0603) |

### functionstackx · 2026-03-01

@claude why does "Part 1: Power Draw vs Concurrency" only analyze TP8, it would analzye all the TP and conc. the first column should it's interactivity. do power draw vs interactivity for all intereactivity

### Klaud-Cold · 2026-03-01

**Claude finished @functionstackx's task in 6m 31s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22538546626)

---
### Power Draw vs Interactivity — Full Analysis (All 22 TP/Conc Configs)

- [x] Gather all benchmark results and GPU power CSVs from the sweep run (22 configs)
- [x] Build comprehensive power draw vs concurrency table for ALL TP configs (TP2/4/8)
- [x] Build power draw vs interactivity (TPOT) analysis across all configurations
- [x] Synthesize findings and produce detailed report

*Data: 22 GPU power CSVs + benchmark results, [Run #22537483477](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22537483477). Model: gpt-oss-120b FP4 on H100 DGXC.*

---

### Part 1: Power Draw vs Concurrency — All TP Configs

#### 1K/1K (ISL=1024, OSL=1024)

| TP | Conc | TPOT (ms) | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | J/out_tok | out_tok/W |
|---:|-----:|----------:|----------:|-----------:|------:|---------:|------------:|----------:|----------:|
| 2 | 64 | 15.21 | 794 W | 1,303 W | 397 W | 55.4% | 2,061.5 | 0.192 | 5.20 |
| 4 | 64 | 9.89 | 1,205 W | 2,226 W | 301 W | 47.0% | 1,571.8 | 0.192 | 5.22 |
| 8 | 4 | 3.72 | 1,275 W | 2,183 W | 159 W | 27.3% | 129.6 | 1.230 | 0.81 |
| 8 | 8 | 4.05 | 1,382 W | 2,565 W | 173 W | 29.4% | 238.4 | 0.725 | 1.38 |
| 8 | 16 | 4.83 | 1,509 W | 2,859 W | 189 W | 31.7% | 405.2 | 0.466 | 2.15 |
| 8 | 32 | 5.82 | 1,640 W | 3,250 W | 205 W | 35.1% | 664.2 | 0.309 | 3.24 |
| 8 | 64 | 7.36 | 1,370 W | 3,514 W | 171 W | 24.2% | 1,053.2 | 0.163 | 6.15 |

#### 1K/8K (ISL=1024, OSL=8192)

| TP | Conc | TPOT (ms) | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | J/out_tok | out_tok/W |
|---:|-----:|----------:|----------:|-----------:|------:|---------:|------------:|----------:|----------:|
| 2 | 64 | 14.58 | 1,148 W | 1,300 W | 574 W | 90.5% | 2,159.3 | 0.266 | 3.76 |
| 4 | 64 | 9.63 | 1,866 W | 2,251 W | 466 W | 86.7% | 1,631.6 | 0.286 | 3.50 |
| 8 | 4 | 3.68 | 1,777 W | 2,208 W | 222 W | 72.2% | 133.6 | 1.663 | 0.60 |
| 8 | 8 | 4.00 | 2,027 W | 2,500 W | 253 W | 80.7% | 242.9 | 1.043 | 0.96 |
| 8 | 16 | 4.53 | 2,325 W | 2,960 W | 291 W | 76.5% | 425.7 | 0.683 | 1.46 |
| 8 | 32 | 5.65 | 2,468 W | 3,039 W | 309 W | 79.1% | 694.7 | 0.444 | 2.25 |
| 8 | 64 | 16.01 | 1,957 W | 3,352 W | 245 W | 91.2% | 491.5 | 0.498 | 2.01 |

#### 8K/1K (ISL=8192, OSL=1024)

| TP | Conc | TPOT (ms) | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | J/out_tok | out_tok/W |
|---:|-----:|----------:|----------:|-----------:|------:|---------:|------------:|----------:|----------:|
| 2 | 64 | 27.19 | 988 W | 1,323 W | 494 W | 73.1% | 1,147.7 | 0.431 | 2.32 |
| 4 | 4 | 4.45 | 776 W | 1,724 W | 194 W | 31.0% | 212.3 | 0.914 | 1.09 |
| 4 | 8 | 5.57 | 947 W | 2,242 W | 237 W | 46.2% | 342.3 | 0.692 | 1.45 |
| 4 | 16 | 7.52 | 1,015 W | 2,356 W | 254 W | 41.0% | 505.6 | 0.502 | 1.99 |
| 4 | 32 | 30.56 | 914 W | 1,764 W | 229 W | 69.8% | 255.1 | 0.896 | 1.12 |
| 4 | 64 | 17.21 | 1,498 W | 2,537 W | 374 W | 57.0% | 902.8 | 0.415 | 2.41 |
| 8 | 4 | 3.95 | 1,373 W | 2,790 W | 172 W | 28.8% | 120.2 | 1.428 | 0.70 |
| 8 | 8 | 4.59 | 1,473 W | 3,511 W | 184 W | 30.5% | 208.1 | 0.884 | 1.13 |

---

### Part 2: Power Draw vs Interactivity — All 22 Configs Sorted by TPOT

| TPOT (ms) | ISL/OSL | TP | Conc | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | J/out_tok | out_tok/W | E2E (s) |
|----------:|---------|---:|-----:|----------:|-----------:|------:|---------:|------------:|----------:|----------:|--------:|
| 3.68 | 1k8k | 8 | 4 | 1,777 W | 2,208 W | 222 W | 72.2% | 133.6 | 1.663 | 0.60 | 26.8 |
| 3.72 | 1k1k | 8 | 4 | 1,275 W | 2,183 W | 159 W | 27.3% | 129.6 | 1.230 | 0.81 | 3.4 |
| 3.95 | 8k1k | 8 | 4 | 1,373 W | 2,790 W | 172 W | 28.8% | 120.2 | 1.428 | 0.70 | 3.7 |
| 4.00 | 1k8k | 8 | 8 | 2,027 W | 2,500 W | 253 W | 80.7% | 242.9 | 1.043 | 0.96 | 29.5 |
| 4.05 | 1k1k | 8 | 8 | 1,382 W | 2,565 W | 173 W | 29.4% | 238.4 | 0.725 | 1.38 | 3.8 |
| 4.45 | 8k1k | 4 | 4 | 776 W | 1,724 W | 194 W | 31.0% | 212.3 | 0.914 | 1.09 | 4.2 |
| 4.53 | 1k8k | 8 | 16 | 2,325 W | 2,960 W | 291 W | 76.5% | 425.7 | 0.683 | 1.46 | 33.8 |
| 4.59 | 8k1k | 8 | 8 | 1,473 W | 3,511 W | 184 W | 30.5% | 208.1 | 0.884 | 1.13 | 4.4 |
| 4.83 | 1k1k | 8 | 16 | 1,509 W | 2,859 W | 189 W | 31.7% | 405.2 | 0.466 | 2.15 | 4.4 |
| 5.57 | 8k1k | 4 | 8 | 947 W | 2,242 W | 237 W | 46.2% | 342.3 | 0.692 | 1.45 | 5.3 |
| 5.65 | 1k8k | 8 | 32 | 2,468 W | 3,039 W | 309 W | 79.1% | 694.7 | 0.444 | 2.25 | 41.6 |
| 5.82 | 1k1k | 8 | 32 | 1,640 W | 3,250 W | 205 W | 35.1% | 664.2 | 0.309 | 3.24 | 5.4 |
| 7.36 | 1k1k | 8 | 64 | 1,370 W | 3,514 W | 171 W | 24.2% | 1,053.2 | 0.163 | 6.15 | 6.8 |
| 7.52 | 8k1k | 4 | 16 | 1,015 W | 2,356 W | 254 W | 41.0% | 505.6 | 0.502 | 1.99 | 7.1 |
| 9.63 | 1k8k | 4 | 64 | 1,866 W | 2,251 W | 466 W | 86.7% | 1,631.6 | 0.286 | 3.50 | 70.6 |
| 9.89 | 1k1k | 4 | 64 | 1,205 W | 2,226 W | 301 W | 47.0% | 1,571.8 | 0.192 | 5.22 | 9.2 |
| 14.58 | 1k8k | 2 | 64 | 1,148 W | 1,300 W | 574 W | 90.5% | 2,159.3 | 0.266 | 3.76 | 107.0 |
| 15.21 | 1k1k | 2 | 64 | 794 W | 1,303 W | 397 W | 55.4% | 2,061.5 | 0.192 | 5.20 | 14.0 |
| 16.01 | 1k8k | 8 | 64 | 1,957 W | 3,352 W | 245 W | 91.2% | 491.5 | 0.498 | 2.01 | 117.8 |
| 17.21 | 8k1k | 4 | 64 | 1,498 W | 2,537 W | 374 W | 57.0% | 902.8 | 0.415 | 2.41 | 16.1 |
| 27.19 | 8k1k | 2 | 64 | 988 W | 1,323 W | 494 W | 73.1% | 1,147.7 | 0.431 | 2.32 | 25.4 |
| 30.56 | 8k1k | 4 | 32 | 914 W | 1,764 W | 229 W | 69.8% | 255.1 | 0.896 | 1.12 | 28.6 |

---

### Part 3: Power Draw vs Interactivity — By Workload Type

<details>
<summary><strong>1K/1K (balanced) — sorted by TPOT</strong></summary>

| TPOT (ms) | TP | Conc | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | Total Out tok/s | J/out_tok | out_tok/W |
|----------:|---:|-----:|----------:|-----------:|------:|---------:|------------:|----------------:|----------:|----------:|
| 3.72 | 8 | 4 | 1,275 W | 2,183 W | 159 W | 27.3% | 129.6 | 1,037 | 1.230 | 0.81 |
| 4.05 | 8 | 8 | 1,382 W | 2,565 W | 173 W | 29.4% | 238.4 | 1,907 | 0.725 | 1.38 |
| 4.83 | 8 | 16 | 1,509 W | 2,859 W | 189 W | 31.7% | 405.2 | 3,242 | 0.466 | 2.15 |
| 5.82 | 8 | 32 | 1,640 W | 3,250 W | 205 W | 35.1% | 664.2 | 5,313 | 0.309 | 3.24 |
| 7.36 | 8 | 64 | 1,370 W | 3,514 W | 171 W | 24.2% | 1,053.2 | 8,426 | 0.163 | 6.15 |
| 9.89 | 4 | 64 | 1,205 W | 2,226 W | 301 W | 47.0% | 1,571.8 | 6,287 | 0.192 | 5.22 |
| 15.21 | 2 | 64 | 794 W | 1,303 W | 397 W | 55.4% | 2,061.5 | 4,123 | 0.192 | 5.20 |

</details>

<details>
<summary><strong>1K/8K (decode-heavy) — sorted by TPOT</strong></summary>

| TPOT (ms) | TP | Conc | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | Total Out tok/s | J/out_tok | out_tok/W |
|----------:|---:|-----:|----------:|-----------:|------:|---------:|------------:|----------------:|----------:|----------:|
| 3.68 | 8 | 4 | 1,777 W | 2,208 W | 222 W | 72.2% | 133.6 | 1,069 | 1.663 | 0.60 |
| 4.00 | 8 | 8 | 2,027 W | 2,500 W | 253 W | 80.7% | 242.9 | 1,944 | 1.043 | 0.96 |
| 4.53 | 8 | 16 | 2,325 W | 2,960 W | 291 W | 76.5% | 425.7 | 3,406 | 0.683 | 1.46 |
| 5.65 | 8 | 32 | 2,468 W | 3,039 W | 309 W | 79.1% | 694.7 | 5,557 | 0.444 | 2.25 |
| 9.63 | 4 | 64 | 1,866 W | 2,251 W | 466 W | 86.7% | 1,631.6 | 6,526 | 0.286 | 3.50 |
| 14.58 | 2 | 64 | 1,148 W | 1,300 W | 574 W | 90.5% | 2,159.3 | 4,319 | 0.266 | 3.76 |
| 16.01 | 8 | 64 | 1,957 W | 3,352 W | 245 W | 91.2% | 491.5 | 3,932 | 0.498 | 2.01 |

</details>

<details>
<summary><strong>8K/1K (prefill-heavy) — sorted by TPOT</strong></summary>

| TPOT (ms) | TP | Conc | Avg Power | Peak Power | W/GPU | GPU Util | Out tok/GPU | Total Out tok/s | J/out_tok | out_tok/W |
|----------:|---:|-----:|----------:|-----------:|------:|---------:|------------:|----------------:|----------:|----------:|
| 3.95 | 8 | 4 | 1,373 W | 2,790 W | 172 W | 28.8% | 120.2 | 962 | 1.428 | 0.70 |
| 4.45 | 4 | 4 | 776 W | 1,724 W | 194 W | 31.0% | 212.3 | 849 | 0.914 | 1.09 |
| 4.59 | 8 | 8 | 1,473 W | 3,511 W | 184 W | 30.5% | 208.1 | 1,665 | 0.884 | 1.13 |
| 5.57 | 4 | 8 | 947 W | 2,242 W | 237 W | 46.2% | 342.3 | 1,369 | 0.692 | 1.45 |
| 7.52 | 4 | 16 | 1,015 W | 2,356 W | 254 W | 41.0% | 505.6 | 2,022 | 0.502 | 1.99 |
| 17.21 | 4 | 64 | 1,498 W | 2,537 W | 374 W | 57.0% | 902.8 | 3,611 | 0.415 | 2.41 |
| 27.19 | 2 | 64 | 988 W | 1,323 W | 494 W | 73.1% | 1,147.7 | 2,295 | 0.431 | 2.32 |
| 30.56 | 4 | 32 | 914 W | 1,764 W | 229 W | 69.8% | 255.1 | 1,020 | 0.896 | 1.12 |

</details>

---

### Part 4: Power Efficiency at Different Interactivity Tiers

#### Ultra-low latency (TPOT < 5 ms) — sorted by energy efficiency

| TPOT (ms) | ISL/OSL | TP | Conc | Avg Power | Out tok/GPU | J/out_tok | out_tok/W | Power CV |
|----------:|---------|---:|-----:|----------:|------------:|----------:|----------:|---------:|
| 4.83 | 1k1k | 8 | 16 | 1,509 W | 405.2 | 0.466 | 2.15 | 0.486 |
| 4.53 | 1k8k | 8 | 16 | 2,325 W | 425.7 | 0.683 | 1.46 | 0.308 |
| 4.05 | 1k1k | 8 | 8 | 1,382 W | 238.4 | 0.725 | 1.38 | 0.445 |
| 4.59 | 8k1k | 8 | 8 | 1,473 W | 208.1 | 0.884 | 1.13 | 0.508 |
| 4.45 | 8k1k | 4 | 4 | 776 W | 212.3 | 0.914 | 1.09 | 0.534 |
| 4.00 | 1k8k | 8 | 8 | 2,027 W | 242.9 | 1.043 | 0.96 | 0.303 |
| 3.72 | 1k1k | 8 | 4 | 1,275 W | 129.6 | 1.230 | 0.81 | 0.363 |
| 3.95 | 8k1k | 8 | 4 | 1,373 W | 120.2 | 1.428 | 0.70 | 0.418 |
| 3.68 | 1k8k | 8 | 4 | 1,777 W | 133.6 | 1.663 | 0.60 | 0.274 |

#### Low latency (TPOT 5-10 ms)

| TPOT (ms) | ISL/OSL | TP | Conc | Avg Power | Out tok/GPU | J/out_tok | out_tok/W | Power CV |
|----------:|---------|---:|-----:|----------:|------------:|----------:|----------:|---------:|
| 7.36 | 1k1k | 8 | 64 | 1,370 W | 1,053.2 | 0.163 | 6.15 | 0.714 |
| 9.89 | 1k1k | 4 | 64 | 1,205 W | 1,571.8 | 0.192 | 5.22 | 0.644 |
| 9.63 | 1k8k | 4 | 64 | 1,866 W | 1,631.6 | 0.286 | 3.50 | 0.294 |
| 5.82 | 1k1k | 8 | 32 | 1,640 W | 664.2 | 0.309 | 3.24 | 0.550 |
| 5.65 | 1k8k | 8 | 32 | 2,468 W | 694.7 | 0.444 | 2.25 | 0.306 |
| 7.52 | 8k1k | 4 | 16 | 1,015 W | 505.6 | 0.502 | 1.99 | 0.656 |
| 5.57 | 8k1k | 4 | 8 | 947 W | 342.3 | 0.692 | 1.45 | 0.617 |

#### Medium latency (TPOT 10-20 ms)

| TPOT (ms) | ISL/OSL | TP | Conc | Avg Power | Out tok/GPU | J/out_tok | out_tok/W | Power CV |
|----------:|---------|---:|-----:|----------:|------------:|----------:|----------:|---------:|
| 15.21 | 1k1k | 2 | 64 | 794 W | 2,061.5 | 0.192 | 5.20 | 0.624 |
| 14.58 | 1k8k | 2 | 64 | 1,148 W | 2,159.3 | 0.266 | 3.76 | 0.257 |
| 17.21 | 8k1k | 4 | 64 | 1,498 W | 902.8 | 0.415 | 2.41 | 0.602 |
| 16.01 | 1k8k | 8 | 64 | 1,957 W | 491.5 | 0.498 | 2.01 | 0.151 |

#### High latency (TPOT 20-50 ms)

| TPOT (ms) | ISL/OSL | TP | Conc | Avg Power | Out tok/GPU | J/out_tok | out_tok/W | Power CV |
|----------:|---------|---:|-----:|----------:|------------:|----------:|----------:|---------:|
| 27.19 | 8k1k | 2 | 64 | 988 W | 1,147.7 | 0.431 | 2.32 | 0.477 |
| 30.56 | 8k1k | 4 | 32 | 914 W | 255.1 | 0.896 | 1.12 | 0.265 |

---

### Part 5: Pareto Frontier — Best Power Efficiency at Each Interactivity Tier

| Tier | Best Config | TPOT | J/out_tok | Avg Power | Out tok/GPU |
|------|-------------|-----:|----------:|----------:|------------:|
| **Ultra-low** (< 5ms) | 1k1k TP8 conc16 | 4.83 ms | 0.466 J | 1,509 W | 405 |
| **Low** (5-10ms) | 1k1k TP8 conc64 | 7.36 ms | 0.163 J | 1,370 W | 1,053 |
| **Medium** (10-20ms) | 1k1k TP2 conc64 | 15.21 ms | 0.192 J | 794 W | 2,062 |
| **High** (20-50ms) | 8k1k TP2 conc64 | 27.19 ms | 0.431 J | 988 W | 1,148 |

---

### Part 6: Power Cost of Interactivity — What Does Each ms of TPOT Cost?

**1k1k (balanced):**
- 4.1→3.7 ms (TP8c8→TP8c4): −107 W for −0.3 ms = **320 W/ms**
- 4.8→4.1 ms (TP8c16→TP8c8): −127 W for −0.8 ms = **165 W/ms**
- 5.8→4.8 ms (TP8c32→TP8c16): −130 W for −1.0 ms = **131 W/ms**
- 7.4→5.8 ms (TP8c64→TP8c32): +270 W for −1.5 ms = **175 W/ms**
- 9.9→7.4 ms (TP4c64→TP8c64): +165 W for −2.5 ms = **65 W/ms**
- 15.2→9.9 ms (TP2c64→TP4c64): +411 W for −5.3 ms = **77 W/ms**

**1k8k (decode-heavy):**
- 4.0→3.7 ms (TP8c8→TP8c4): −250 W for −0.3 ms = **762 W/ms**
- 4.5→4.0 ms (TP8c16→TP8c8): −298 W for −0.5 ms = **565 W/ms**
- 5.6→4.5 ms (TP8c32→TP8c16): −144 W for −1.1 ms = **129 W/ms**
- 9.6→5.6 ms (TP4c64→TP8c32): +603 W for −4.0 ms = **151 W/ms**
- 14.6→9.6 ms (TP2c64→TP4c64): +718 W for −5.0 ms = **145 W/ms**
- 16.0→14.6 ms (TP8c64→TP2c64): −808 W for −1.4 ms = **565 W/ms**

**8k1k (prefill-heavy):**
- 4.5→3.9 ms (TP4c4→TP8c4): +597 W for −0.5 ms = **1,181 W/ms**
- 5.6→4.6 ms (TP4c8→TP8c8): +526 W for −1.0 ms = **537 W/ms**
- 7.5→5.6 ms (TP4c16→TP4c8): −68 W for −2.0 ms = **35 W/ms**
- 17.2→7.5 ms (TP4c64→TP4c16): −483 W for −9.7 ms = **50 W/ms**
- 27.2→17.2 ms (TP2c64→TP4c64): +509 W for −10.0 ms = **51 W/ms**

---

### Part 7: Key Insights

#### 1. Interactivity has a steep power cost at the extreme — and it's workload-dependent

The "last mile" of TPOT is the most expensive. For 1k/1k, going from 4.1→3.7 ms costs **320 W/ms**. For 1k/8k (decode-heavy), the same tier costs **762 W/ms** — 2.4x more. For 8k/1k (prefill-heavy), it costs **1,181 W/ms**. Sub-4ms TPOT is extremely power-expensive across all workloads, but decode-heavy and prefill-heavy workloads pay an especially steep premium.

#### 2. The sweet spot is different for each TP level

- **TP8:** Best interactivity (3.7-4.8ms TPOT) but worst energy efficiency (0.5-1.7 J/tok). Only justified when latency SLA demands sub-5ms TPOT.
- **TP4:** Middle ground — 5-10ms TPOT at 0.3-0.9 J/tok. The **8k1k TP4 conc4** is notable: 4.45ms TPOT at only 776 W total (lowest power in any sub-5ms config).
- **TP2:** Best per-GPU efficiency (0.19-0.43 J/tok) but 15-27ms TPOT. Ideal for batch/throughput workloads where interactivity doesn't matter.

#### 3. Concurrency improves efficiency at every TP level — until it doesn't

At TP8, 1k/1k scales perfectly: conc4→64 goes from 1.23→0.16 J/tok (**7.7x improvement**) while TPOT only degrades from 3.7→7.4ms. But 1k/8k TP8 **breaks at conc64** — TPOT jumps from 5.65ms (conc32) to 16.01ms (conc64) while J/tok actually *worsens* from 0.44→0.50. Similarly, 8k/1k TP4 conc32 is an anomaly (30.56ms TPOT, 0.90 J/tok — worse than conc16 in every way).

#### 4. Decode-heavy workloads (1k/8k) pay a consistent 40-70% power premium

At every TPOT tier, 1k/8k draws more power than 1k/1k:
- TPOT ~4ms: 1,777 W (1k8k) vs 1,275 W (1k1k) = **+39%**
- TPOT ~4.5ms: 2,325 W vs 1,509 W = **+54%**
- TPOT ~5.7ms: 2,468 W vs 1,640 W = **+51%**
- TPOT ~15ms: 1,148 W vs 794 W = **+45%**

The decode tax is remarkably consistent across the interactivity spectrum.

#### 5. TP2 at conc64 is the Pareto winner for throughput-optimized deployments

| ISL/OSL | TP2 conc64 Power | TP2 conc64 Out tok/GPU | J/out_tok |
|---------|------------------|-----------------------:|----------:|
| 1k1k | 794 W | 2,061.5 | 0.192 |
| 1k8k | 1,148 W | 2,159.3 | 0.266 |
| 8k1k | 988 W | 1,147.7 | 0.431 |

TP2 delivers the **highest per-GPU output throughput** at the **lowest total power** — across all workloads. The cost is TPOT of 15-27ms, which is acceptable for batch processing, offline inference, and any scenario where per-request latency isn't the primary constraint.

#### 6. Power variability (CV) correlates with workload type, not interactivity

| Pattern | Power CV Range | Characteristics |
|---------|---------------:|-----------------|
| 1k8k configs | 0.15 - 0.31 | **Most stable** — sustained decode keeps power flat |
| 1k1k configs | 0.36 - 0.71 | **Most bursty** — rapid request cycling creates transients |
| 8k1k configs | 0.27 - 0.66 | **Variable** — prefill bursts drive spikes, short decode keeps avg low |

For power provisioning: 1k8k workloads can be provisioned close to average power. 1k1k and 8k1k workloads need 2-2.5x headroom above average for peak handling.

#### 7. Summary: The Interactivity-Power Tradeoff

| If you need... | Use | TPOT | Power | J/out_tok |
|----------------|-----|-----:|------:|----------:|
| Best interactivity | TP8 low conc | 3.7-4ms | 1,275-1,777 W | 1.2-1.7 |
| Balanced latency+throughput | TP8 high conc | 5-7ms | 1,370-2,468 W | 0.16-0.44 |
| Good throughput, moderate latency | TP4 conc64 | 10-17ms | 1,205-1,866 W | 0.19-0.42 |
| Maximum efficiency | TP2 conc64 | 15-27ms | 794-1,148 W | 0.19-0.43 |

The **10x energy efficiency gap** (0.16 J/tok to 1.66 J/tok) across configs means that configuration choice dominates hardware choice for power cost. Picking the right TP/concurrency for your latency SLA is the single most impactful power optimization.

---

### functionstackx · 2026-03-03

@claude run this experiment on mi300

### Klaud-Cold · 2026-03-03

**Claude finished @functionstackx's task in 28m 5s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22601716754) • [`claude/issue-828-20260303-0007`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260303-0007) • [Create PR ➔](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260303-0007?quick_pull=1&title=%5Bexperimental%5D%20Add%20MI300X%20GPU%20power%20monitoring%20for%20gptoss&body=Add%20experimental%20GPU%20power%20monitoring%20with%20rocm-smi%20(1s%20intervals)%20for%20gptoss%20fp4%20MI300X%20vLLM%20across%20three%20ISL%2FOSL%20configs%20(1k%2F1k%2C%201k%2F8k%2C%208k%2F1k).%20Includes%20Python%20plotting%20tool%20and%20detailed%20MI300X%20vs%20H100%20power%20efficiency%20analysis.%0A%0ACloses%20%23828%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

---
### GPU Power Monitoring Experiment — MI300X — Completed

- [x] Gather context — find gptoss MI300X configs, AMD power monitoring tools, and existing scripts
- [x] Create MI300X power monitoring benchmark script (`gptoss-power_fp4_mi300x.sh`)
- [x] Create GPU power plotting utility (`utils/plot_gpu_power.py`)
- [x] Create experimental workflow for MI300X power monitoring
- [x] Add `gptoss-power-fp4-mi300x-vllm` config to `amd-master.yaml`
- [x] Add GPU power CSV upload step to benchmark template
- [x] Commit and push changes
- [x] Trigger experimental runs — [Run #22601920598](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22601920598) ✅ All 3 succeeded
- [x] Download results and detailed analysis

### Configuration
| Parameter | Value |
|-----------|-------|
| Config | `gptoss-power-fp4-mi300x-vllm` |
| Model | `openai/gpt-oss-120b` |
| Image | `vllm/vllm-openai-rocm:v0.16.0` |
| ISL/OSL | 1024/1024, 1024/8192, 8192/1024 |
| TP | 4 |
| Concurrency | 4 |
| Runner | `mi300x` |
| Power Tool | `rocm-smi` (1-second polling) |

---

### Benchmark Results — MI300X (4x MI300X, TP4, conc4)

| Metric | 1k/1k | 1k/8k | 8k/1k |
|--------|-------|-------|-------|
| **Throughput/GPU** | 255.2 tok/s | 153.0 tok/s | 1,741.4 tok/s |
| **Output tput/GPU** | 127.0 tok/s | 135.6 tok/s | 193.7 tok/s |
| **Mean TTFT** | 167.5 ms | 148.9 ms | 249.6 ms |
| **Median TPOT** | 7.46 ms | 7.22 ms | 4.74 ms |
| **Mean E2E latency** | 7.0 s | 52.7 s | 4.6 s |
| **P99 E2E latency** | 8.9 s | 59.0 s | 5.7 s |

### GPU Power Summary (4x MI300X, 1-second intervals)

| Config | Duration | Avg Total | Peak Total | Avg Util | Peak TDP% |
|--------|----------|-----------|------------|----------|-----------|
| **1k/1k** | 107s (107 samples/GPU) | **1,101 W** | ~1,874 W | 47.2% | ~62% |
| **1k/8k** | 365s (365 samples/GPU) | **1,424 W** | ~1,720 W | 79.1% | ~57% |
| **8k/1k** | 135s (135 samples/GPU) | **1,062 W** | ~2,666 W | 33.6% | ~89% |

Power limit: **750 W** per MI300X GPU.

### Per-GPU Breakdown

<details>
<summary>1k/1k (ISL=1024, OSL=1024) — mi300x-amds_1</summary>

| GPU | Avg Power | Peak Power | Avg TEdge | Avg TJunction | Peak TJunction | Avg Util |
|-----|-----------|------------|-----------|---------------|----------------|----------|
| GPU 0 | 274.4 W | 468.0 W | 45.0°C | 38.4°C | 48°C | 47.9% |
| GPU 1 | 280.3 W | 470.0 W | 43.1°C | 37.5°C | 47°C | 47.8% |
| GPU 2 | 278.1 W | 476.0 W | 52.1°C | 42.0°C | 53°C | 46.7% |
| GPU 3 | 268.3 W | 460.0 W | 43.9°C | 36.5°C | 44°C | 46.5% |
| **Total** | **1,101 W** | **~1,874 W** | — | — | — | — |

</details>

<details>
<summary>1k/8k (ISL=1024, OSL=8192) — mi300x-amds_3</summary>

| GPU | Avg Power | Peak Power | Avg TEdge | Avg TJunction | Peak TJunction | Avg Util |
|-----|-----------|------------|-----------|---------------|----------------|----------|
| GPU 0 | 358.4 W | 432.0 W | 52.1°C | 45.7°C | 51°C | 79.1% |
| GPU 1 | 353.6 W | 427.0 W | 49.7°C | 43.0°C | 48°C | 79.0% |
| GPU 2 | 360.8 W | 436.0 W | 59.4°C | 49.1°C | 55°C | 79.2% |
| GPU 3 | 350.9 W | 425.0 W | 47.3°C | 42.8°C | 49°C | 79.2% |
| **Total** | **1,424 W** | **~1,720 W** | — | — | — | — |

</details>

<details>
<summary>8k/1k (ISL=8192, OSL=1024) — mi300x-cr_0 (active GPUs only)</summary>

| GPU | Avg Power | Peak Power | Avg TEdge | Avg TJunction | Peak TJunction | Avg Util |
|-----|-----------|------------|-----------|---------------|----------------|----------|
| GPU 0 | 270.3 W | 662.0 W | 50.5°C | 36.8°C | 50°C | 34.4% |
| GPU 1 | 262.5 W | 667.0 W | 47.2°C | 36.1°C | 47°C | 33.9% |
| GPU 2 | 268.7 W | 671.0 W | 48.5°C | 36.4°C | 50°C | 32.2% |
| GPU 3 | 260.9 W | 666.0 W | 46.1°C | 34.3°C | 46°C | 33.8% |
| **Total** | **1,062 W** | **~2,666 W** | — | — | — | — |

</details>

---

### MI300X vs H100 — Comparison (TP4, conc4)

| Metric | ISL/OSL | MI300X | H100 | Delta |
|--------|---------|--------|------|-------|
| **Throughput/GPU** | 1k/1k | 255.2 | 470.2 | **-45.7%** |
| | 1k/8k | 153.0 | 190.0 | **-19.5%** |
| | 8k/1k | 1,741.4 | 1,908.5 | **-8.8%** |
| **Median TPOT** | 1k/1k | 7.46 ms | 4.12 ms | **+81%** |
| | 1k/8k | 7.22 ms | 5.87 ms | **+23%** |
| | 8k/1k | 4.74 ms | 4.46 ms | **+6%** |
| **Avg Power (4 GPUs)** | 1k/1k | 1,101 W | 747 W | **+47%** |
| | 1k/8k | 1,424 W | 920 W | **+55%** |
| | 8k/1k | 1,062 W | 766 W | **+39%** |
| **Peak Power (4 GPUs)** | 1k/1k | ~1,874 W | ~1,398 W | **+34%** |
| | 1k/8k | ~1,720 W | ~1,175 W | **+46%** |
| | 8k/1k | ~2,666 W | ~1,718 W | **+55%** |

### Power Efficiency Comparison

| Metric | ISL/OSL | MI300X | H100 | MI300X / H100 |
|--------|---------|--------|------|---------------|
| **tok/s per Watt** | 1k/1k | 0.93 | 2.52 | 0.37x (2.7x worse) |
| | 1k/8k | 0.43 | 0.83 | 0.52x (1.9x worse) |
| | 8k/1k | 6.56 | 9.97 | 0.66x (1.5x worse) |
| **out_tok/s per Watt** | 1k/1k | 0.46 | 1.25 | 0.37x |
| | 1k/8k | 0.38 | 0.73 | 0.52x |
| | 8k/1k | 0.73 | 1.11 | 0.66x |
| **Energy per token** | 1k/1k | — | — | MI300X uses **2.72x** more |
| | 1k/8k | — | — | MI300X uses **1.92x** more |
| | 8k/1k | — | — | MI300X uses **1.52x** more |

---

### Detailed Analysis

#### 1. Power Consumption Patterns — Same Trends, Higher Baseline

MI300X follows the same workload-dependent power pattern as H100 but at a consistently higher level:

- **1k/8k (decode-heavy)** draws the most average power (1,424 W) with the steadiest draw — sustained autoregressive decode keeps all 4 GPUs at ~79% utilization and ~356 W/GPU average.
- **8k/1k (prefill-heavy)** has the highest peak power (~2,666 W) but moderate average (1,062 W) — large prefill batches create sharp spikes to 662-671 W/GPU (89% of TDP!), then quickly return to baseline.
- **1k/1k (balanced)** sits in the middle — moderate average (1,101 W) with bursty behavior cycling between prefill spikes and decode periods.

#### 2. MI300X Draws 40-55% More Power Than H100

Across all workloads, MI300X consistently draws significantly more average power:
- 1k/1k: 1,101 W vs 747 W (+47%)
- 1k/8k: 1,424 W vs 920 W (+55%)
- 8k/1k: 1,062 W vs 766 W (+39%)

The power premium is largest for decode-heavy workloads (55%) where MI300X's HBM3 memory subsystem draws continuous power during autoregressive generation.

#### 3. MI300X Prefill Peak Approaches TDP

The 8k/1k workload pushes MI300X GPUs to **662-671 W peak** — that's **89% of the 750 W TDP**. By comparison, H100 peaked at 352-365 W (52% of 700 W TDP). MI300X utilizes a much larger fraction of its power envelope during prefill bursts, suggesting the prefill compute path is more power-hungry per FLOP on the CDNA3 architecture.

#### 4. Throughput Gap Varies By Workload

- **1k/1k: MI300X is 46% slower** — the largest gap. Short sequences don't amortize MI300X's higher per-token overhead. TPOT is 7.46 ms vs 4.12 ms (+81%).
- **1k/8k: MI300X is 20% slower** — decode-heavy narrows the gap because the sustained memory bandwidth workload plays to MI300X's HBM3 strength. TPOT: 7.22 ms vs 5.87 ms (+23%).
- **8k/1k: MI300X is only 9% slower** — prefill is the closest to parity. The compute-bound nature of large prefills means MI300X's raw FLOP count partially compensates. TPOT: 4.74 ms vs 4.46 ms (+6%).

#### 5. Energy Efficiency: MI300X Uses 1.5-2.7x More Energy Per Token

| Workload | Energy Multiplier | Interpretation |
|----------|-------------------|----------------|
| 1k/1k | **2.72x** | Short balanced sequences — worst case for MI300X |
| 1k/8k | **1.92x** | Decode-heavy — HBM3 bandwidth helps but not enough |
| 8k/1k | **1.52x** | Prefill-heavy — closest to parity, FLOP-bound helps MI300X |

The efficiency gap narrows as workloads become more compute-bound (prefill-heavy), suggesting MI300X's competitive disadvantage is primarily in decode-phase efficiency.

#### 6. Thermal Headroom

MI300X runs significantly cooler despite higher power draw:
- Junction temperatures: **31-55°C** across all workloads (well below thermal limits)
- H100 comparison: GPUs hit **66-90°C** in sustained decode (1k/8k TP4 conc4)
- MI300X's larger die area and better thermal design provides substantial headroom

This means MI300X has room to be pushed harder (higher concurrency, longer runs) without thermal throttling concerns — unlike H100 which hit 90°C on GPU 3 during 1k/8k.

#### 7. Key Takeaways

| Insight | Detail |
|---------|--------|
| **MI300X power premium is 40-55%** | Consistently higher across all workloads vs H100 |
| **Throughput gap: 9-46%** | Smallest for prefill-heavy (8k/1k), largest for balanced (1k/1k) |
| **Energy efficiency: 1.5-2.7x worse** | MI300X uses more joules per output token across the board |
| **Prefill pushes 89% TDP** | 8k/1k peaks at 662-671 W/GPU — needs power provisioning headroom |
| **Thermal headroom is excellent** | Max 55°C junction vs 90°C on H100 — room for higher concurrency |
| **Same patterns hold** | Decode drives avg power, prefill drives peaks — architecture-independent |

---

### Artifacts
All artifacts available in [Run #22601920598](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22601920598):
- **GPU Power CSVs**: `gpu_power_gptoss-power_{1k1k,1k8k,8k1k}_*` (1-second rocm-smi samples)
- **Benchmark Results**: `bmk_gptoss-power_{1k1k,1k8k,8k1k}_*` (aggregated JSON)
- **Server Logs**: `server_logs_gptoss-power_{1k1k,1k8k,8k1k}_*`
- **Aggregated Results**: `results_bmk` (all three combined)

CSV columns: `timestamp, index, power.draw [W], power.limit [W], temperature.edge [C], temperature.junction [C], utilization.gpu [%], memory.used [MiB], memory.total [MiB]`

### Files Created
- `benchmarks/single_node/gptoss-power_fp4_mi300x.sh` — benchmark with rocm-smi power logging
- `.github/workflows/experimental-gptoss-power-mi300x.yml` — standalone workflow for re-runs
- `utils/plot_gpu_power.py` — power/temp/utilization visualization tool
- `.github/configs/amd-master.yaml` — added `gptoss-power-fp4-mi300x-vllm` config
- `.github/workflows/benchmark-tmpl.yml` — added conditional GPU power CSV upload step



[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22601920598) | [`claude/issue-828-20260303-0007`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260303-0007)

### functionstackx · 2026-03-03

@claude instead of doing this complex python scripting to explore values, cant u just use amd-smi --csv

https://rocm.docs.amd.com/projects/amdsmi/en/docs-5.7.0/amdsmi_cli_readme_link.html

### Klaud-Cold · 2026-03-03

**Claude finished @functionstackx's task in 128m 1s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22603516807) • [`claude/issue-828-20260303-0111`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260303-0111)

---
## GPU Power Monitoring: Simplified with `rocm-smi --csv`

### What changed
Replaced ~100 lines of inline Python (5 separate `rocm-smi` commands/sec + regex parsing) with a simple `rocm-smi --csv` loop:

```bash
rocm-smi --showpower --showtemp --showuse --showmeminfo vram --csv
```

### Why rocm-smi instead of amd-smi
We tried `amd-smi metric --csv` first (as suggested), but it has multiple issues in container environments:
- `-w` (watch mode) produces **no output** in both Docker and SLURM/enroot containers
- Single-shot queries in background subshells also fail silently
- The binary exists but doesn't function reliably inside `vllm/vllm-openai-rocm` containers

`rocm-smi --csv` works reliably across all MI300X runner types (Docker `mi300x-cr` and SLURM `mi300x-amds`).

### Test results (all passing with power data)

| Config | Runner | Power Samples | Peak GPU Power | Peak Temp |
|--------|--------|--------------|----------------|-----------|
| 1k/8k TP4 conc4 | mi300x-cr_0 | 4,275 | ~128W idle | 44°C |
| 1k/1k TP4 conc4 | mi300x-amds_3 | 1,050 | ~278W load | 65°C |
| 8k/1k TP4 conc4 | mi300x-amds_2 | 915 | ~352W load | 64°C |

CSV columns: `device, Temperature (Sensor junction), Temperature (Sensor memory), Current Socket Graphics Package Power (W), GPU use (%), GFX Activity, VRAM Total Memory, VRAM Total Used Memory`

### Successful run
[#22606308636](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22606308636) — All 3 configs passed with GPU power data collected

### Files changed
| File | Change |
|---|---|
| `benchmarks/single_node/gptoss-power_fp4_mi300x.sh` | Simplified power monitoring with `rocm-smi --csv` loop |
| `utils/plot_gpu_power.py` | Flexible CSV parser supporting nvidia-smi and rocm-smi formats |
| `.github/workflows/experimental-gptoss-power-mi300x.yml` | Standalone workflow for MI300X power experiments |
| `.github/workflows/benchmark-tmpl.yml` | Added GPU power CSV artifact upload |
| `.github/configs/amd-master.yaml` | Added `gptoss-power-fp4-mi300x-vllm` config |

### Branch
`claude/issue-828-20260303-0111` — [view commits](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260303-0111)

### functionstackx · 2026-03-05

@claude modify this branch such that it does deepseek sglang mi300  & additional tracks gpu power consumption, gpu tempurate, gpu clock every second during the run and saves it as an artifact in csv and then run it for conc 4 1k1k



### Klaud-Cold · 2026-03-05

**Claude finished @functionstackx's task in 14m 52s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22738670491) • [`claude/issue-828-20260305-2158`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260305-2158)

---
### DeepSeek SGLang MI300X — GPU Power Monitoring

- [x] Gather context — find DeepSeek SGLang MI300X config, existing power scripts
- [x] Create power monitoring benchmark script (`dsr1-power_fp8_mi300x.sh`)
- [x] Add `dsr1-power-fp8-mi300x-sglang` config to `amd-master.yaml`
- [x] Add GPU power CSV upload step to benchmark template
- [x] Commit and push changes
- [x] Trigger the experimental run
- [ ] Monitor execution and report results — **blocked by runner issue**

### Runner Issue
The `mi300x-cr_0` runner has a stale temp directory (`tmppu1esql4`) with root-owned files that prevent `actions/checkout` from cleaning the workspace. All 3 attempts (runs [#22738838800](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22738838800), [#22739061061](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22739061061)) failed with:
```
EACCES: permission denied, scandir '/home/ubuntu/actions-runner/_work/InferenceX/InferenceX/tmppu1esql4'
```
This needs manual cleanup on the runner (`sudo rm -rf /home/ubuntu/actions-runner/_work/InferenceX/InferenceX/tmppu1esql4`), then the run can be re-triggered.

### Configuration
| Parameter | Value |
|-----------|-------|
| Config | `dsr1-power-fp8-mi300x-sglang` |
| Model | `deepseek-ai/DeepSeek-R1-0528` |
| Image | `lmsysorg/sglang:v0.5.9-rocm700-mi30x` |
| ISL/OSL | 1024 / 1024 |
| TP | 8 |
| Concurrency | 4 |
| Runner | `mi300x` |
| Power Tool | `rocm-smi --csv` (1-second polling) |

### GPU Monitoring CSV Columns
`timestamp, device, temperature_junction_C, temperature_edge_C, temperature_memory_C, power_draw_W, power_limit_W, gpu_util_pct, gpu_clock_MHz, mem_clock_MHz, vram_used_MiB, vram_total_MiB`

### Files Created/Modified
- `benchmarks/single_node/dsr1-power_fp8_mi300x.sh` — SGLang benchmark with `rocm-smi --csv` power/temp/clock logging
- `.github/configs/amd-master.yaml` — added `dsr1-power-fp8-mi300x-sglang` config
- `.github/workflows/benchmark-tmpl.yml` — added conditional GPU power CSV upload step

### To re-run after runner cleanup
```
gh workflow run e2e-tests.yml --ref claude/issue-828-20260305-2158 \
  -f 'generate-cli-command=test-config --config-files .github/configs/amd-master.yaml --config-keys dsr1-power-fp8-mi300x-sglang --conc 4' \
  -f 'test-name=DeepSeek SGLang MI300X GPU power monitoring (1k/1k conc4)'
```

[Create PR](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260305-2158?quick_pull=1&title=%5Bexperimental%5D%20Add%20DeepSeek%20SGLang%20MI300X%20GPU%20power%20monitoring&body=Add%20experimental%20benchmark%20that%20tracks%20GPU%20power%20consumption%2C%20temperature%2C%20and%20clock%20speed%20every%20second%20via%20rocm-smi%20during%20the%20DeepSeek%20R1%20FP8%20SGLang%20MI300X%201k1k%20run%20and%20saves%20the%20data%20as%20a%20CSV%20artifact.%0A%0ACloses%20%23828%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22739061061) | [`claude/issue-828-20260305-2158`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260305-2158)

### functionstackx · 2026-03-05

@claude modify this branch such that it does deepseek sglang mi325 & additional tracks gpu power consumption, gpu tempurate, gpu clock every second during the run and saves it as an artifact in csv and then run it for conc 4 1k1k



### Klaud-Cold · 2026-03-05

**Claude finished @functionstackx's task in 21m 29s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22739186884) • [`claude/issue-828-20260305-2211`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260305-2211)

---
### DeepSeek SGLang MI325X — GPU Power Monitoring

- [x] Gather context — find DeepSeek SGLang MI325X config, existing power scripts
- [x] Create power monitoring benchmark script (`dsr1-power_fp8_mi325x.sh`)
- [x] Add `dsr1-power-fp8-mi325x-sglang` config to `amd-master.yaml`
- [x] Add GPU power CSV upload step to benchmark template
- [x] Commit and push changes
- [x] Trigger the experimental run — [Run #22739364158](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22739364158) ✅ Succeeded
- [x] Monitor execution and report results

### Configuration
| Parameter | Value |
|-----------|-------|
| Config | `dsr1-power-fp8-mi325x-sglang` |
| Model | `deepseek-ai/DeepSeek-R1-0528` |
| Image | `lmsysorg/sglang:v0.5.9-rocm700-mi30x` |
| ISL/OSL | 1024 / 1024 |
| TP | 8 |
| Concurrency | 4 |
| Runner | `mi325x` (`mi325x-amd_0`) |
| Power Tool | `rocm-smi --csv` (1-second polling) |

### Benchmark Results
| Metric | Value |
|--------|-------|
| Throughput/GPU | 40.0 tok/s |
| Output throughput/GPU | 19.9 tok/s |
| Mean TTFT | 291.1 ms |
| Median TPOT | 23.9 ms |
| Mean E2E latency | 22.3 s |
| P99 E2E latency | 27.5 s |

### GPU Monitoring Summary (8x MI325X, 424 samples/GPU)

| GPU | Avg Temp | Peak Temp | Avg SCLK | Peak SCLK | Avg MCLK | Peak MCLK | Peak VRAM |
|-----|----------|-----------|----------|-----------|----------|-----------|-----------|
| card0 | 48/53°C | 57/62°C | 1634 MHz | 1800 MHz | 2015 MHz | 2105 MHz | 662 MiB |
| card1 | 54/57°C | 65/68°C | 1633 MHz | 1800 MHz | 2014 MHz | 2110 MHz | 680 MiB |
| card2 | 50/51°C | 59/60°C | 1635 MHz | 1800 MHz | 2019 MHz | 2112 MHz | 663 MiB |
| card3 | 56/59°C | 67/69°C | 1642 MHz | 1800 MHz | 2009 MHz | 2100 MHz | 683 MiB |
| card4 | 49/52°C | 58/62°C | 1642 MHz | 1800 MHz | 2025 MHz | 2109 MHz | 678 MiB |
| card5 | 57/60°C | 68/70°C | 1627 MHz | 1800 MHz | 2033 MHz | 2110 MHz | 681 MiB |
| card6 | 50/53°C | 59/62°C | 1625 MHz | 1800 MHz | 2022 MHz | 2106 MHz | 689 MiB |
| card7 | 54/58°C | 65/68°C | 1644 MHz | 1800 MHz | 2025 MHz | 2105 MHz | 684 MiB |

*Temp format: junction/edge. SCLK = GPU clock, MCLK = memory clock.*

### Known Issue: Power Draw Values
`rocm-smi --showpower --csv` on MI325X reports power values as 0-2 instead of actual watts. This appears to be a `rocm-smi` limitation on MI325X where power reporting via `--csv` mode does not output meaningful watt values. Temperature, clock speeds, and VRAM data are all captured correctly. A future fix could use `amd-smi` or parse `rocm-smi --showpower` non-CSV output to get actual power draw values.

### Artifacts
- **GPU Power CSV** (3,393 rows): `gpu_power_dsr1-power_1k1k_fp8_sglang_tp8-ep1-dpafalse_disagg-false_spec-none_conc4_mi325x-amd_0`
- **Benchmark Result**: `bmk_dsr1-power_1k1k_fp8_sglang_tp8-ep1-dpafalse_disagg-false_spec-none_conc4_mi325x-amd_0`
- **Server Logs**: `server_logs_dsr1-power_1k1k_fp8_sglang_tp8-ep1-dpafalse_disagg-false_spec-none_conc4_mi325x-amd_0`

CSV columns: `timestamp, device, temperature_junction_C, temperature_edge_C, temperature_memory_C, power_draw_W, power_limit_W, gpu_util_pct, gpu_clock_MHz, mem_clock_MHz, vram_used_MiB, vram_total_MiB`

### Files Created/Modified
- `benchmarks/single_node/dsr1-power_fp8_mi325x.sh` — SGLang benchmark with `rocm-smi --csv` power/temp/clock logging
- `.github/configs/amd-master.yaml` — added `dsr1-power-fp8-mi325x-sglang` config
- `.github/workflows/benchmark-tmpl.yml` — added GPU power CSV upload step

[Create PR](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260305-2211?quick_pull=1&title=%5Bexperimental%5D%20Add%20DeepSeek%20SGLang%20MI325X%20GPU%20power%20monitoring&body=Add%20experimental%20benchmark%20that%20tracks%20GPU%20power%20consumption%2C%20temperature%2C%20and%20clock%20speed%20every%20second%20via%20rocm-smi%20during%20the%20DeepSeek%20R1%20FP8%20SGLang%20MI325X%201k1k%20run%20and%20saves%20the%20data%20as%20a%20CSV%20artifact.%0A%0ACloses%20%23828%0A%0AGenerated%20with%20%5BClaude%20Code%5D(https%3A%2F%2Fclaude.ai%2Fcode))

[View workflow run](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22739364158) | [`claude/issue-828-20260305-2211`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260305-2211)

### functionstackx · 2026-03-05

@claude use amd-smi instead and re-run to get power

### Klaud-Cold · 2026-03-05

**Claude finished @functionstackx's task in 3s** —— [View job](https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22740173087) • [`claude/issue-828-20260305-2310`](https://github.com/SemiAnalysisAI/InferenceX/tree/claude/issue-828-20260305-2310)

---
## GPU Power Monitoring: MI325X DeepSeek R1 SGLang (amd-smi)

**Status: Complete** - GPU power data successfully captured using `amd-smi` (replacing broken `rocm-smi`).

### Run Details
- **Workflow Run:** https://github.com/SemiAnalysisAI/InferenceX/actions/runs/22742040394
- **Branch:** `claude/issue-828-20260305-2310` ([3 commits](https://github.com/SemiAnalysisAI/InferenceX/compare/main...claude/issue-828-20260305-2310))
- **Config:** DeepSeek-R1-0528, FP8, SGLang v0.5.9, TP=8, Concurrency=4, ISL/OSL=1k/1k
- **Runner:** MI325X (8x AMD Instinct MI325X OAM)

### Benchmark Throughput
| Metric | Value |
|--------|-------|
| Total throughput/GPU | **40.0 tok/s** |
| Output throughput/GPU | **19.9 tok/s** |
| Mean TTFT | 293ms |
| Median TPOT | 23.9ms |
| Mean E2E latency | 22.3s |

### GPU Power Summary (8x MI325X)

| GPU | Min (W) | Max (W) | Mean (W) |
|-----|---------|---------|----------|
| 0 | 144 | 647 | 421 |
| 1 | 148 | 667 | 434 |
| 2 | 138 | 823 | 421 |
| 3 | 148 | 676 | 437 |
| 4 | 144 | 666 | 423 |
| 5 | 138 | 678 | 430 |
| 6 | 138 | 689 | 435 |
| 7 | 137 | 690 | 431 |
| **Total** | | | **3,432W** |

### Benchmark Phase (under load, >3000W total)
- **Samples:** 150 (out of 208 per GPU)
- **Mean total system power:** 4,041W
- **Peak total system power:** 5,367W

### Temperatures (Hotspot)
- **Range:** 40-70°C across all GPUs
- **Mean:** 55-65°C per GPU (well within thermal limits)

### Clock Speeds
- **Idle:** ~132 MHz GFX, 900 MHz memory
- **Under load:** ~2,100 MHz GFX, 1,500 MHz memory

### Key Findings
1. `rocm-smi --showpower --csv` reports 0-2W on MI325X — **broken/incorrect**
2. `amd-smi metric --power --csv` correctly reports ~140W idle, 450-670W under load per GPU
3. Combined `amd-smi metric --csv` produces embedded Python lists that break CSV parsing — solved by querying each metric category (`--power`, `--clock`, `--temperature`, `--usage`, `--vram`) separately
4. Total system GPU power during benchmark: **~4kW mean, ~5.4kW peak** for 8x MI325X

### Artifacts
- GPU Power CSV: `gpu_power_dsr1-power_1k1k_fp8_sglang_tp8-ep1-dpafalse_disagg-false_spec-none_conc4_mi325x-amd_0` (1,664 data rows, 8 GPUs × ~208 seconds)
- Benchmark result: `bmk_dsr1-power_1k1k_fp8_sglang_tp8-ep1-dpafalse_disagg-false_spec-none_conc4_mi325x-amd_0`
- Server logs: `server_logs_dsr1-power_1k1k_fp8_sglang_tp8-ep1-dpafalse_disagg-false_spec-none_conc4_mi325x-amd_0`

### PR
Ready to create a PR with the power monitoring script and workflow changes if desired.
