# [Issue #155] GL2C (L2 cache) performance counters read 0 on gfx1201 (RDNA4 / Navi 48) — every path, every privilege; compute counters work

source: https://github.com/ROCm/rocprofiler-sdk/issues/155
state: closed | updated: 2026-07-25T07:10:02Z
labels: status: triage

## 正文

## Summary

On gfx1201 (Radeon AI PRO R9700, RDNA4/Navi 48), **all `GL2C_*` memory-cache performance counters read `0`**, while compute counters (e.g. `SQ_WAVES`) on the *identical* collection path read correct values. This reproduces across every userspace path we could construct — windowed PMC, direct SPM sampling, as root with `CAP_SYS_PERFMON`, with a patched kernel and patched aqlprofile — and the RADV/Vulkan path does not expose these counters at all on this GPU. The evidence points to a gap **below userspace** (kernel perfmon readback / firmware / RLC SPM enable for the GL2C block on gfx12), not in tool configuration.

Filing so the counter path for the GL2C block on gfx12 can be traced end-to-end.

## Environment

| Component | Version |
|---|---|
| GPU | 2× AMD Radeon AI PRO R9700 (gfx1201, RDNA4 / Navi 48), PCI `04:00.0`, `8a:00.0` |
| Kernel | `6.17.0-35-generic` |
| amdgpu | DKMS `6.19.4` (srcversion `30F5626…`) |
| ROCm | `7.2.4` |
| rocprofiler-sdk | `v1.1.0` (git `97f5574fe2fdc7bef44fb01545347912ee9f1779`) |
| aqlprofile | ROCm 7.2.4 build (+ local patch, see below) |
| Mesa / RADV | `25.2.8` (cross-check only) |

## Expected vs actual

- **Expected:** with a memory-bound workload, `GL2C_EA_RDREQ_sum`, `GL2C_HIT`, `GL2C_MISS` increment proportional to L2 traffic (as `SQ_WAVES` tracks dispatched waves).
- **Actual:** every `GL2C_*` counter reads `0`; `SQ_WAVES` on the same run reads correctly.

## Reproduction

A trivial memory-read kernel (a `memread`/`membench` looping over a large device buffer — ~1.5 TB of reads across 6000 iterations), collected two ways:

**A) Windowed PMC (rocprofv3):**
```
HIP_VISIBLE_DEVICES=0 rocprofv3 --pmc SQ_WAVES GL2C_EA_RDREQ_sum --output-format csv -- ./membench
```
```
Kernel                 Counter_Name        Counter_Value
memread(...)           GL2C_EA_RDREQ_sum   0.0
memread(...)           SQ_WAVES            32768.0
```

**B) Direct SPM sampling** (rocprofiler-sdk `CounterClientSample`, `GL2C_EA_RDREQ_sum` + all 16 `GL2C_HIT` instances + `SQ_WAVES`), run as **root with `CAP_SYS_PERFMON`** (no "could not be locked / SYS_PERFMON degraded" warning):
```
Counter: GL2C_EA_RDREQ_sum  Value: 0   (DIMENSION_INSTANCE 0)
Counter: GL2C_HIT           Value: 0   (DIMENSION_INSTANCE 0..15, all 0)
Counter: SQ_WAVES           Value: 116768   ✅
```

## What we ruled out

| Hypothesis | Test | Result |
|---|---|---|
| Tool/permission (SYS_PERFMON) | re-ran SPM PoC as **root + CAP_SYS_PERFMON** | GL2C still **0** |
| Windowed-vs-SPM collection path | direct rocprofiler-sdk SPM sampling PoC | GL2C still **0** |
| Wrong SPM block id enum (Mesa vs aqlprofile) | flipped `spm_block_id` **7 → 8** | GL2C still **0** |
| Insufficient traffic / timing window | sustained ~1.5 TB reads, 6000 iters | GL2C still **0** |
| CP ME filter-CAM coalescing of `*_SELECT` writes | added `RESET_FILTER_CAM` (PM4 hdr bit 1) to perf-cnt select writes, mirroring RADV `ac_cmdbuf_set_ucfg_perfctr_reg_seq` (aqlprofile never sets it — 0 occurrences) | Debug build confirmed all 32 per-instance GL2C SELECT writes carry the bit (`header=0xc0017902`); `LD_DEBUG` confirmed patched lib loaded. **GL2C still 0 — correct fix, but not sufficient.** |
| Counter block genuinely dead vs collection-side | `SQ_WAVES` on the identical path | reads correctly → **collection harness is sound; GL2C-block-specific** |

**Control:** `GRBM` (also a global block, same windowed path) reads non-zero, and `SQ_WAVES` reads non-zero, on the same runs — so the issue is specific to the GL2C block's counter readback, not the collection mechanism.

## Vulkan / RADV cross-check (falsifies the "read it via SPM like RADV does" assumption)

A common assumption is that GL2C is readable via the streaming/SPM path (as RADV/RGP is presumed to do). On this stack that does **not** hold:

- A headless `VK_KHR_performance_query` probe reports the extension is **not exposed** on gfx1201 (RADV, Mesa 25.2.8), even with `RADV_PERFTEST=perfcounters`.
- The RADV binary carries live gating strings: `radv: SPM isn't supported for this GPU (%s)!` and `radv: Failed to initialize SPM because perf counters aren't implemented.`

So neither the ROCm SPM path nor the RADV SPM path yields GL2C counters on this GPU.

## Assessment / suspected root cause

The counter readback for the GL2C block on gfx12 appears **not wired below userspace** — i.e. in the kernel perfmon readback path and/or firmware/RLC SPM enable for the GL2C block — rather than in tool configuration. Two concrete kernel-side observations that may be related (or may be red herrings):

- `gfx_v12_0_get_tcc_info()` in amdgpu is an **empty stub `{}`** (vs `gfx_v11_0` which is implemented). RDNA4 renamed TCC→GL2 and split the harvest register (`regCC_GC_GL2C_DISABLE_{0,1}` / `regGC_USER_GL2C_DISABLE_{0,1}`, field bits `[31:16]`). We wrote a candidate port, but the empty stub leaves `mask = 0` ("all active"), a valid default — so this is likely **necessary-but-not-sufficient**; it does not by itself explain 0-counters.

## Questions for maintainers

1. Is GL2C (L2) perf-counter **SPM/streaming readback implemented for gfx12 (gfx1201)** in the kernel `amdgpu` perfmon path and/or firmware? If not, is that the expected reason these counters read 0?
2. Is there a known-good sequence (GRBM SE/SH broadcast for the global GL2C block, `CP_PERFMON_CNTL` START, any GL2C block-level enable) that userspace must issue on gfx12 that differs from gfx11, which aqlprofile/rocprofiler is not doing?
3. Is this tracked anywhere? (We could not find an existing issue specific to gfx1201 GL2C=0; rocprofiler-sdk #73 is a different, closed "--list-avail crashes" bug and was previously mis-referenced for this.)

Happy to provide the PoC (`CounterClientSample` + membench), full CSV/log captures, and the RESET_FILTER_CAM patch on request.


## 评论 (7)

### The-Monk · 2026-07-10

Withdrawing this for now — consolidating with additional local findings (thread-trace/SQTT behaves differently from the windowed-PMC path) before re-filing a more complete, better-scoped report. Apologies for the noise.

### The-Monk · 2026-07-10

Reopening — withdrawing was premature. An additional finding **narrows the scope** of this issue and is worth recording: **SQTT thread-trace works on gfx1201, while the GL2C counters do not.**

Using `rocprofv3 --att` (Advanced Thread Trace) on a gfx1201 (Radeon AI PRO R9700) HIP compute kernel, SQTT capture **succeeds** and the trace decoder returns valid per-instruction latency and **stall** data (e.g. `s_wait_loadcnt` stall cycles dominating a memory-bound GEMV decode kernel; real non-empty `*_shader_engine_*.att` output + decoded occupancy timeline).

On the *same* GPU, by contrast:
- windowed-PMC `GL2C_*` counters read **0** (this issue),
- SPM streaming of `GL2C_*` also reads **0**,
- while `SQ_WAVES` / `GRBM` read correctly on the identical PMC path.

Implication: the defect looks specific to the **GL2C-block counter readback on the counter (PMC/SPM) path** — not a blanket failure of the perf/trace infrastructure, since the SQ thread-trace path streams fine. And for anyone currently blocked by the dead GL2C counters, **`rocprofv3 --att` is a viable workaround** for memory-behavior / stall analysis in the meantime.

Happy to share the SQTT capture recipe and the counter-path PoC.

### The-Monk · 2026-07-13

## Update (2026-07-13): still 0 on ROCm 7.13, firmware ruled out, and the sibling RDNA arch (gfx1151) got GL2C support in 7.13 while gfx1201 was left out

Three new data points that narrow this considerably.

### 1. Still dead on ROCm 7.13.0-preview
Re-ran on the TheRock 7.13 toolchain (`rocprofv3` 1.3.0, git `3309c611`) — identical outcome to the 7.2.4 report:

```
rocprofv3 --pmc GL2C_EA_RDREQ_sum GL2C_HIT SQ_WAVES -- <memory-bound llama.cpp decode>
  GL2C_EA_RDREQ_sum = 0
  GL2C_HIT          = 0
  SQ_WAVES          = 293,694,024      # control, reads correctly
```
50,066 dispatches; `SQ_WAVES` tracks on the *same* dispatches. So the gap persists 7.2.4 → 7.13, and the GL2C counter **definitions are present** in `share/rocprofiler-sdk/basic_counters.xml` (rocprofv3 accepts and runs them) — the `0` is the hardware/firmware readback, not a missing definition.

### 2. Firmware ruled out — it is not stale microcode
The loaded RLC (`FW_ID RLC, FW_VERSION 12484000`, from `gc_12_0_1_rlc.bin`) is **byte-identical** (SHA-256 `6ba4459532246a5c415d3cb33c9b1248294e48f67b827e2accb292a8d1a5c0ec`) to `linux-firmware` git HEAD's `amdgpu/gc_12_0_1_rlc.bin`, and AMD's newest packaged firmware (`amdgpu-dkms-firmware 31.30.0.0`, May 2026) is exactly what is installed. So the newest RLC microcode that exists anywhere still does not arm the GL2C perfmon on gfx1201 — this is not an "update your firmware" situation.

### 3. gfx1151 (RDNA3.5) got GL2C support in 7.13 — gfx1201 (RDNA4) did not
ROCm 7.13 `rocprofiler-compute` shipped **full GL2 cache profiling for gfx1151**: a `soc_gfx1151.py`, `analysis_configs/gfx1151/`, GL2C counter panels, and a documented [GL2 cache page](https://rocm.docs.amd.com/projects/rocprofiler-compute/en/7.13.0-preview/conceptual/rdna/gl2-cache.html). There is **no gfx1201 equivalent** — no `soc_gfx1201.py`, no `analysis_configs/gfx1201`, and the GL2 cache doc is scoped to gfx1151 only. (I ported a `soc_gfx1201.py` locally so `rocprof-compute` runs on gfx1201; the compute sections populate correctly, but the GL2C/L2-Fabric sections read 0 — confirming the gap is below the tool layer, consistent with the above.)

### Suggested framing
Since gfx1151 and gfx1201 share the RDNA GL2C counter block, this reads as **extending the gfx1151 GL2C perfmon enablement that shipped in 7.13 to gfx1201** — plus whatever kernel/RLC-side SPM-enable the readback needs for the gfx12 GL2C block. Happy to run any targeted collection on the hardware (dual R9700, gfx1201) to help trace the counter path end-to-end.

**Environment (this update):** ROCm 7.13.0-preview (TheRock `gfx1201-7.13.0`), rocprofv3 1.3.0, amdgpu-dkms 6.19.4, firmware 31.30.0.0 (RLC 12484000), kernel 6.17.0-35-generic, 2× Radeon AI PRO R9700 (gfx1201).


### The-Monk · 2026-07-13

## Update (2026-07-13, part 2): the gap is broader than GL2C — ~90% of hardware counters read 0 on gfx1201; plus a partial rocprofiler-compute enablement

Profiling deeper on ROCm 7.13 (via a locally-ported `soc_gfx1201.py` — see below) and then inspecting the raw `pmc_perf.csv` directly, the dead-counter set is **much larger than the GL2C block**.

### Scope: only 18 of 176 collected counters ever read nonzero on gfx1201
Verified against ROCm 7.13's **authoritative native gfx1201 counter catalog** (correct block/event pairs, not a mis-mapping — 22 block/event conflicts vs a naive gfx1151 mirror were caught and corrected first).

**Read correctly (18):** coarse `GRBM_*` busy-bits (GPU Busy 100%, CP Busy, TA Busy), `SQ_WAVES` (149,108,040 on the test workload), `SQ_BUSY_CYCLES`, `SQC_ICACHE` hit rate (99.77%), and the per-dispatch kernel timeline.

**Read 0 (the other ~158), all on the authoritative native events:**
- `GL2C_*`, `GL1C_*`, `GCEA_*` — the L2/memory-fabric block (this issue's original scope)
- `TCP_*`, `CPC_*`, `SPI_*`, `SQC_DCACHE/LDS/TC_*`
- **most `SQ_INSTS_*` / `SQ_WAIT_*`** — VALU/SALU/SMEM/FLAT/LDS instruction counts
- `SQ_WAVE_CYCLES` (→ wavefront occupancy)

Consequence: rocprofiler-compute's **Speed-of-Light VALU FLOPs / IPC / Wavefront-Occupancy panels and the entire Wave Instruction-Mix panel read 0.00** — not just the L2 cache panel.

### Pattern → same root cause, wider blast radius
The counters that **work** are the coarse always-on `GRBM` busy-registers and a couple of `SQ`-level aggregates. The counters that read **0** are the detailed per-block / per-instruction perfmon counters that require the perfmon block to be **armed and read back** (SPM/windowed PMC). This is consistent with the below-userspace GL2C diagnosis in the original report — but it means the broken readback covers **most gfx12 perfmon blocks (SQ instruction counters, TCP, CPC, SPI, SQC data caches, GL1/GL2/GCEA)**, not GL2C alone. gfx1151 (RDNA3.5) exposes these same blocks correctly in 7.13; gfx1201 (RDNA4) does not.

### Partial enablement offered (tooling side, not the fix)
To even get this far I ported a `soc_gfx1201.py` (+ `mi_gpu_spec.yaml` gfx1201 entry, `analysis_configs/gfx1201/`, `profile_configs/sets/gfx1201_sets.yaml`, and 172 authoritative counter defs into `sdk_config.yaml`) into 7.13 rocprofiler-compute so `rocprof-compute profile/analyze` runs on gfx1201 and gives **per-kernel time attribution** (which *does* work). Happy to share the port if it's useful as a starting point for official gfx1201 rocprofiler-compute support — but it only surfaces the 18 live counters; the underlying **hardware/firmware perfmon readback for the other blocks is the actual blocker.**

**Env:** ROCm 7.13.0-preview (TheRock `gfx1201-7.13.0`), rocprofiler-compute 3.6.0 / rocprofv3 1.3.0, amdgpu-dkms 6.19.4, firmware 31.30.0.0 (RLC 12484000 = upstream `linux-firmware` HEAD, byte-identical), kernel 6.17.0-35, 2× Radeon AI PRO R9700 (gfx1201).


### The-Monk · 2026-07-13

## Full counter-coverage census (2026-07-13, part 3): exhaustive map — 15/356 counters live (4.2%) on gfx1201, and a *second* distinct gap

Ran the complete gfx1201 counter catalog from ROCm 7.13's authoritative `sdk_config.yaml` — **356 counters (207 raw block:event + 149 derived)** — against a workload audited to exercise VALU/dp4a (`mul_mat_vec_q`), WMMA+LDS (`flash_attn_ext_f16`), LDS reduction (`rms_norm`), and memory (`mul_mat_q`, `quantize_q8_1`). 103 batches respecting per-block simultaneous limits; `SQ_WAVES`+`GRBM_GUI_ACTIVE` in every batch as attachment controls (both nonzero in all 103 → 100% attachment confirmed).

### Census — by block
| block | total | LIVE | DEAD (read 0) | NOTFOUND |
|---|---|---|---|---|
| CPC | 28 | 0 | 0 | **28** |
| GCEA | 17 | 0 | 0 | **17** |
| GL1C | 18 | 0 | 0 | **18** |
| SPI | 16 | 0 | 0 | **16** |
| GL2C | 24 | 0 | 10 | 14 |
| TCP | 13 | 0 | 2 | 11 |
| TA | 1 | 0 | 1 | 0 |
| SQ | 79 | 5 | 16 | 58 |
| GRBM | 11 | 2 | 0 | 9 |
| DERIVED | 149 | 8 | 28 | 113 |
| **TOTAL** | **356** | **15** | **57** | **284** |

**15 LIVE (4.2%)** — and 8 of those 15 are static device constants (`CU_NUM=64`, `SE_NUM=4`, `SIMD_NUM=128`, `GPU_UTIL`, etc.), so only **~7 real hardware counters** produce data: `GRBM_COUNT`, `GRBM_GUI_ACTIVE`, `SQ_WAVES`, `SQ_BUSY_CYCLES`, `SQC_ICACHE_{HITS,MISSES,REQ}`.

### Two distinct problems
1. **Hardware-readback gap (57 DEAD):** counters that resolve and collect, but read **0** despite the workload provably issuing the traffic — all of GL2C's read/write/hit counters, TCP cache requests, TA busy, and every SQ per-instruction counter (`SQ_INSTS_VALU`, `SQ_INSTS_LDS`, `SQ_INST_CYCLES_VALU`, `SQ_WAIT_*`). This is the original card-115 gap, now shown to be block-wide, not GL2C-specific.
2. **Cataloging/registration gap (284 NOTFOUND) — new:** counters declared valid for gfx1201 in the shipped `sdk_config.yaml` that `rocprofv3 --pmc` **cannot resolve by name at all** (tested both `CPC_CPC_STAT_BUSY` and `CPC_STAT_BUSY` alias forms). **Four entire blocks — CPC, GCEA, GL1C, SPI (79 counters, 22% of the catalog) — are 100% NOTFOUND**, so they can't even be windowed-tested through the standard CLI.

### SPM cross-check (stock kernel — no DKMS reload, per prod guardrail)
An independent rocprofiler-sdk tool-client (`libgl2c_spm_poc.so`, continuous 50 ms sampling, ~500 samples, `membench_loop` saturating memory BW) read `GL2C_EA_RDREQ_sum` and `GL2C_HIT` = **0 across every sample** while `SQ_WAVES` climbed live (116,496→116,800+, attachment proven) — a second, independent tool confirming GL2C-dead, and streaming does not rescue a windowed-dead counter (consistent with the original patched-kernel SPM finding). Honest caveat: SQ_INSTS_VALU/TCP/TA were **not** independently SPM-retested (the PoC is hardcoded to GL2C); the block-wide inference is well-supported by the windowed pattern but is not proof for those specific counters.

### Characterization
On gfx1201/RDNA4, only the always-on GRBM global-busy aggregates and a narrow SQ front-end slice (wave dispatch count, gross busy-cycles, instruction-*cache* hit/miss/req) return live values. Every counter that characterizes the *actual work* — VALU/LDS/VMEM instruction counts, all GL2C/TCP cache traffic, TA busy — reads 0 or is unresolvable, while the same blocks work on **gfx1151 (RDNA3.5) in the same ROCm 7.13**. So the ask stands: extend the gfx1151 perfmon enablement to gfx1201, and separately fix the 4 blocks / 284 counters that the SDK counter-registry doesn't recognize for gfx1201.

**Artifact:** full per-counter CSV `gfx1201-full-counter-coverage.csv` (356 rows: name, block, event, status, max_value). Happy to attach it or run any targeted collection on the hardware (dual R9700, gfx1201).

**Env:** ROCm 7.13.0-preview (TheRock `gfx1201-7.13.0`), rocprofv3 1.3.0, amdgpu-dkms 6.19.4 (stock, srcversion E3A6FA…), firmware 31.30.0.0 (RLC = upstream `linux-firmware` HEAD, byte-identical), kernel 6.17.0-35, 2× Radeon AI PRO R9700.


### The-Monk · 2026-07-24

Closing — this is **not a bug**. GL2C (and TA / SQ_INSTS_VALU / GRBM_COUNT / FETCH_SIZE) reading 0 on gfx1201 is the documented **performance-level gating** tracked in ROCm/rocm-systems#5953: these counters require the workload GPU at a `stable` perf level.

Verified on our gfx1201 (Radeon AI PRO R9700):
```
sudo amd-smi set --gpu <N> --perf-level STABLE_STD      # or sysfs: echo profile_standard > .../power_dpm_force_performance_level
```
On the same membench where SQ_WAVES already read correctly, under STABLE_STD:
- GL2C_EA_RDREQ_sum: 0 → 1,100,489
- GL2C_EA_WRREQ_sum: 0 → 16,810
- GRBM_COUNT: 0 → 3,045,156

Our earlier SPM/kernel investigation chased a firmware root-cause because we had only tested the `high` perf level, never `stable`. Apologies for the noise. (Note this repo is deprecated → ROCm/rocm-systems; upstream enablement is PR #7455.)

### The-Monk · 2026-07-25

**Follow-up: use `profile_peak`, not `profile_standard` — same counters, no clock throttle**

Refining the perf-level workaround: the gating unlocks these counters under **any fixed DPM profile**, not `profile_standard`/STABLE_STD specifically. `profile_standard` un-gates them but **throttles the GPU to ~1593 MHz** (vs ~2472 MHz boost) — so any benchmark run *alongside* the counter collection is silently slowed, and the memory-roofline is measured at a non-representative clock.

**`profile_peak` un-gates the same counters at *peak* clocks:**
```
echo profile_peak > /sys/class/drm/cardN/device/power_dpm_force_performance_level
#   rocprofv3 --pmc GL2C_EA_RDREQ_sum ...
echo auto        > /sys/class/drm/cardN/device/power_dpm_force_performance_level   # restore
```

Verified on gfx1201 (Radeon AI PRO R9700), ROCm 7.14, `rocprofv3` @ `profile_peak` (2332 MHz):
- `GL2C_EA_RDREQ_sum` = **1,319,235** on `mul_mat_vec_q<Q2_0>` (reads 0 under `auto`)
- `GRBM_COUNT` / `TA_*` / `SQ_INSTS_VALU` / `FETCH_SIZE` un-gate the same way

Net: use `profile_peak` for memory-roofline profiling on RDNA4 — you get the counters **and** representative peak-clock timing in the same run.

