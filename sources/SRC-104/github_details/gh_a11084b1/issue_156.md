# [Issue #156] GL2C (L2) performance counters read 0 on gfx1201 (RDNA4/Navi48) — reproducible on stock ROCm 7.14; compute counters work

source: https://github.com/ROCm/rocprofiler-sdk/issues/156
state: closed | updated: 2026-07-24T04:18:51Z
labels: 

## 正文

# GL2C (L2 cache) performance counters read 0 on gfx1201 (RDNA4 / Navi 48) — reproducible on stock ROCm 7.14; compute counters work

## Summary

On gfx1201 (Radeon AI PRO R9700, RDNA4 / Navi 48), **all `GL2C_*` memory-cache performance counters read `0`**, while compute/activity counters (`SQ_WAVES`, `SQ_BUSY_CYCLES`, `GRBM_GUI_ACTIVE`) on the *identical* collection path read correct values. Because the derived memory-bandwidth metric (`FETCH_SIZE`) is defined on `GL2C_EA_RDREQ_*`, **there is no working memory-bandwidth counter on this GPU** — memory-roofline profiling is not possible on RDNA4.

This reproduces **out-of-the-box on stock ROCm 7.14** (no patches, windowed PMC), and separately survives an exhaustive userspace/kernel exclusion: direct SPM sampling, root + `CAP_SYS_PERFMON`, a patched kernel (ported gfx12 SPM funcs), and a patched aqlprofile (corrected SPM block-id + CP filter-CAM). The RADV/Vulkan SPM path does not expose these counters at all on this GPU. The evidence points to a gap **below userspace** — kernel perfmon readback and/or firmware/RLC SPM enable for the GL2C block on gfx12 — not tool configuration.

**Persistence across releases:** first observed on ROCm 7.2.4 (rocprofiler-sdk v1.1.0), **re-confirmed unchanged on ROCm 7.14 (rocprofiler-sdk / rocprofv3 v1.3.1)** — so this is not a transient packaging or version regression.

## Environment (current — the stock repro)

| Component | Version |
|---|---|
| GPU | 2× AMD Radeon AI PRO R9700 (gfx1201, RDNA4 / Navi 48), PCI `04:00.0`, `8a:00.0` |
| Kernel | `7.0.0-28-generic` |
| amdgpu | **stock** DKMS `6.19.4` (srcversion `E3A6FA6…`) — no local kernel patch for this repro |
| ROCm | `7.14.0a` (TheRock `rocm-sdk`) |
| rocprofiler-sdk / rocprofv3 | **`v1.3.1`** (git `1b2a555677ae5ed2e859d22db97b12ff69b343bd`) |
| Original investigation stack | ROCm `7.2.4`, kernel `6.17.0-35`, rocprofiler-sdk `v1.1.0` (deeper SPM/kernel exclusion below was done here; finding re-confirmed on the row above) |

## Expected vs actual

- **Expected:** under a memory-bound workload, `GL2C_EA_RDREQ_sum` / `GL2C_EA_WRREQ_sum` / `GL2C_HIT` increment proportional to L2 traffic, as `SQ_WAVES` tracks dispatched waves.
- **Actual:** every `GL2C_*` counter reads `0`; `SQ_WAVES`, `SQ_BUSY_CYCLES`, `GRBM_GUI_ACTIVE` on the same run read correctly.

## Reproduction A — stock ROCm 7.14, windowed PMC (no patches, ~2 minutes)

A trivial memory-read kernel (`membench_loop`: 6000 iterations over a large device buffer ≈ **1.5 TB** of reads), collected with the shipped `rocprofv3`:

```
HIP_VISIBLE_DEVICES=0 rocprofv3 \
  --pmc GL2C_EA_RDREQ_32B GL2C_EA_RDREQ_sum GL2C_EA_WRREQ_sum SQ_WAVES SQ_BUSY_CYCLES GRBM_GUI_ACTIVE \
  --output-format csv -d ./out -- ./membench_loop
```

Max value seen on the `memread` kernel (per-dispatch, ROCm 7.14 / rocprofv3 v1.3.1):

| Counter | max on `memread` | |
|---|---|---|
| `GL2C_EA_RDREQ_32B` | `0.0` | ❌ |
| `GL2C_EA_RDREQ_sum` | `0.0` | ❌ |
| `GL2C_EA_WRREQ_sum` | `0.0` | ❌ |
| `SQ_WAVES` | `32768` | ✅ |
| `SQ_BUSY_CYCLES` | `100077477` | ✅ |
| `GRBM_GUI_ACTIVE` | `~6.0e6` | ✅ |

The whole GL2C block (reads **and** writes, all size buckets) is 0 while the two SQ counters and GRBM read real values on the identical sampling path. Consequently the derived `FETCH_SIZE` / memory-bandwidth expression (defined on `GL2C_EA_RDREQ_*`) evaluates to 0. `GL1C` exposes only `*_REQ_LEVEL` (occupancy, not throughput) and `GRBM_*_BUSY` are activity ratios — so **no alternative memory-throughput counter is available**.

## Reproduction B — deeper exclusion (ROCm 7.2.4 investigation, re-confirmed)

Direct SPM sampling (rocprofiler-sdk `CounterClientSample`, `GL2C_EA_RDREQ_sum` + all 16 `GL2C_HIT` instances + `SQ_WAVES`), run as **root with `CAP_SYS_PERFMON`** (no "SYS_PERFMON degraded" warning):

```
Counter: GL2C_EA_RDREQ_sum  Value: 0        (all instances)
Counter: GL2C_HIT           Value: 0        (DIMENSION_INSTANCE 0..15, all 0)
Counter: SQ_WAVES           Value: 116768   ✅
```

## What we ruled out

| Hypothesis | Test | Result |
|---|---|---|
| Tool / version regression | re-ran on **stock ROCm 7.14 + rocprofv3 v1.3.1** (above) | GL2C still **0** |
| Tool / permission (SYS_PERFMON) | SPM PoC as **root + CAP_SYS_PERFMON** | GL2C still **0** |
| Windowed-vs-SPM collection path | direct rocprofiler-sdk SPM sampling PoC | GL2C still **0** |
| Missing kernel SPM support | ported `gfx_v12_0_spm_funcs` (gfx10→gfx12 + KIQ), loaded patched amdgpu | SPM path samples `SQ_WAVES` correctly; GL2C still **0** |
| Wrong SPM block-id enum (Mesa vs aqlprofile) | corrected `spm_block_id` **7 → 8** (7 = GL2A, 8 = GL2C in aqlprofile's own enum) | GL2C still **0** |
| CP ME filter-CAM coalescing of `*_SELECT` writes | added `RESET_FILTER_CAM` (PM4 hdr bit 1) to perf-cnt select writes, mirroring RADV `ac_cmdbuf_set_ucfg_perfctr_reg_seq` (aqlprofile never sets it) | Debug build confirmed all 32 GL2C SELECT writes carry the bit; patched lib loaded. GL2C still **0** — correct alignment, not sufficient. |
| Insufficient traffic / timing window | sustained ~1.5 TB reads, 6000 iters | GL2C still **0** |
| Counter block dead vs collection-side | `SQ_WAVES` / `GRBM_GUI_ACTIVE` on the identical path | read correctly → **collection harness sound; GL2C-block-specific** |

**Control:** `GRBM` (also a global block, same windowed path) and `SQ_*` read non-zero on the same runs → the issue is specific to the GL2C block's counter readback, not the collection mechanism.

## Vulkan / RADV cross-check (falsifies the "read it via SPM like RADV does" assumption)

- A headless `VK_KHR_performance_query` probe reports the extension is **not exposed** on gfx1201 (RADV, Mesa 25.2.8), even with `RADV_PERFTEST=perfcounters`.
- The RADV binary carries live gating strings: `radv: SPM isn't supported for this GPU (%s)!` and `radv: Failed to initialize SPM because perf counters aren't implemented.`
- Force-enabling the RADV gate and issuing a query **hangs the GPU** at `vkAcquireProfilingLockKHR` → SMU reset (reproduced 3×, all recovered).

So neither the ROCm SPM path nor the RADV SPM path yields GL2C counters on this GPU.

## Impact

No `GL2C_*` counter → no `FETCH_SIZE` / memory-bandwidth metric → **memory-roofline analysis is impossible on RDNA4**. `rocprof-compute` runs end-to-end on gfx1201 but its memory-chart / L2 panels are empty for exactly this reason. For a bandwidth-bound workload class (LLM decode), this removes the single most important profiling signal.

## Assessment / suspected root cause

GL2C counter readback for gfx12 appears **not wired below userspace** — kernel perfmon readback and/or firmware/RLC SPM enable for the GL2C global block on Navi48. Our kernel SPM port + aqlprofile block-id/filter-CAM fixes are each necessary-or-correct but **none flips GL2C off 0**, which localizes the residual gap beneath both layers. One related kernel observation (possibly a red herring): `gfx_v12_0_get_tcc_info()` in amdgpu is an empty stub `{}` (vs the implemented `gfx_v11_0`); RDNA4 renamed TCC→GL2 and split the harvest register, but the empty stub leaves `mask = 0` ("all active"), a valid default — so it does not by itself explain 0-counters.

## Questions for maintainers

1. Is GL2C (L2) perf-counter **SPM/streaming readback implemented for gfx12 (gfx1201)** in the kernel `amdgpu` perfmon path and/or firmware/RLC? If not, is that the expected reason these counters read 0?
2. Is there a gfx12-specific enable sequence (GRBM SE/SH broadcast for the global GL2C block, `CP_PERFMON_CNTL` START, a GL2C block-level enable) that userspace must issue and that aqlprofile/rocprofiler is not doing?
3. Is this tracked anywhere? We could not find an existing issue specific to gfx1201 GL2C=0 (rocprofiler-sdk #73 is the unrelated closed `--list-avail` crash).

Happy to provide: the standalone `membench` + `CounterClientSample` PoC, full CSV/log captures, and the 4 exclusion patches (2 amdgpu-kernel, 2 aqlprofile) as reference — framed as exclusion evidence, not proposed fixes.



## 评论 (1)

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
