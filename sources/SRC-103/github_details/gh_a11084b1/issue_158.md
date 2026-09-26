# [Issue #158] [Issue]: GL2C EA size-split counters (GL2C_EA_RDREQ_32B/64B/128B, WRREQ_64B) always read zero on gfx1201 while base GL2C counters work

source: https://github.com/ROCm/rocprofiler-sdk/issues/158
state: open | updated: 2026-08-15T12:46:37Z
labels: 

## 正文

### Summary
On gfx1201 (RDNA4, Radeon AI PRO R9700), the GL2C EA request-size-split counters — `GL2C_EA_RDREQ_32B`, `GL2C_EA_RDREQ_64B`, `GL2C_EA_RDREQ_128B`, `GL2C_EA_WRREQ_64B` — always collect **zero**, while the base GL2C counters (`GL2C_HIT`, `GL2C_MISS`, `GL2C_EA_RDREQ`, `GL2C_EA_WRREQ`) and `SQ_WAVES` collect healthy values in the same run. All documented preconditions are satisfied, so this looks like the size-split variants are unimplemented or mis-plumbed for gfx12 rather than an environment problem.

### Environment
- GPU: AMD Radeon AI PRO R9700 (gfx1201), VBIOS 113-APM107573-101
- rocprofv3 / rocprofiler-sdk: 1.3.2 (git 2b22ab0195cc1461cd9abf3b969e9dd7c10af350), ROCm 7.14
- Kernel 7.0.0-28-generic, amdgpu DKMS 6.19.4
- `power_dpm_force_performance_level = profile_standard` on the measured GPU (verified — the AUTO/perfmon-clock trap is handled)
- `amdgpu.ppfeaturemask=0xffffffff` (default was `0xfff7bfff`; explicitly tested both — no effect on this symptom)

### Reproduction
```bash
echo profile_standard | sudo tee /sys/class/drm/card1/device/power_dpm_force_performance_level
rocprofv3 --pmc "SQ_WAVES GL2C_HIT GL2C_MISS GL2C_EA_RDREQ GL2C_EA_WRREQ" \
          --pmc "GL2C_EA_RDREQ_32B GL2C_EA_RDREQ_64B GL2C_EA_RDREQ_128B GL2C_EA_WRREQ_64B" \
          --output-format csv -d out -o run -- <any GPU workload; we used llama-bench>
```
All four counters in the second group are listed by `--list-avail` and accepted without error; every dispatch row reports 0 for them. Same-run first-group totals (LLM decode workload, for scale): `GL2C_HIT` 61.2M, `GL2C_MISS` 18.9M, `GL2C_EA_RDREQ` healthy and consistent with hit/miss, `SQ_WAVES` 2.77M.

### Secondary observation (same setup)
Base GL2C counter absolute values appear to under-report by a roughly constant ~4x versus hardware-timestamp-derived bandwidth on the same kernels (ratios are self-consistent; absolute magnitudes are not). If GL2C is instanced on gfx1201 and only a subset of instances is sampled, that would explain both the ~4x and possibly the size-split zeros — mentioning in case it localizes the bug.

### Questions
1. Are the `GL2C_EA_*_<size>` derived counters expected to work on gfx12, or are they gfx9-only definitions that happen to be listed?
2. If unimplemented: is there any counter route on RDNA4 for DRAM request-size distribution?


## 评论 (1)

### The-Monk · 2026-08-15

Follow-up: we kept digging and can now answer both of our own questions, with a working workaround. Root cause is **not** clock gating, powerplay masks, or driver state — it's missing entries in aqlprofile's internal gfx1201 counter table, plus an undocumented offset in the custom-counter path.

### Root cause

1. `share/rocprofiler-sdk/basic_counters.xml` has **no gfx12 arch block** (blocks stop at `<gfx11>`). But this turns out to be a red herring: the XML appears to serve as a name catalog, while actual event programming for stock counters comes from aqlprofile's internal per-arch tables.
2. Those internal tables are **correct for gfx1201 base counters** — we verified `GL2C_HIT`/`GL2C_MISS` program the true gfx12 selects (see anchoring below) — but the **EA size-split entries are missing/dead** for gfx1201, hence the zeros. (gfx12 renumbered the GL2C perf selects: per the amdgpu DKMS header `soc24_enum.h`, `GL2C_PERF_SEL_EA_RDREQ_32B = 0x5e` (94) vs gfx11's `0x63` (99), etc.)
3. The `-E/--extra-counters` custom path has an **off-by-two**: a custom definition's `event: N` programs raw perf-select `N − 2`. Empirically anchored with exact value matches on a deterministic workload: custom `event: 41` returned byte-identical totals to stock `GL2C_HIT` (raw select 39 = gfx12 `GL2C_PERF_SEL_HIT`), and custom `event: 42` matched stock `GL2C_MISS` (raw 40) exactly.

### Working workaround (gfx1201, rocprofv3 1.3.2 / ROCm 7.14)

Custom counters via `-E`, using soc24 raw selects **plus 2**:

```yaml
rocprofiler-sdk:
  counters-schema-version: 1
  counters:
    - name: GL2C_RD32B_G12   # soc24 raw 0x5e (94) -> event 96
      description: "gfx1201 EA_RDREQ_32B"
      properties: []
      definitions:
        - architectures: [gfx1201]
          block: GL2C
          event: 96
    - name: GL2C_RD64B_G12   # raw 95 -> 97
      ...same shape, event: 97
    - name: GL2C_RD128B_G12  # raw 97 -> 99
      ...event: 99
    - name: GL2C_WR64B_G12   # raw 81 -> 83
      ...event: 83
```

Result on an LLM decode workload (deterministic, repeated runs): non-zero, reproducible-to-the-decimal read-size distribution (62.4% 32B / 4.2% 64B / 33.4% 128B), where the stock names in the same runs still read zero.

### Remaining observations

- The 96B event (raw 0x60 → event 98) returns anomalously large values on this workload; we've excluded it pending verification.
- `MC_RDREQ` (raw 0x5b) reads zero — presumably the legacy MC interface is dead on client gfx12 and `EA_*` are the live selects; if so, listing `GL2C_MC_*` for gfx1201 is also misleading.
- The ~4x absolute under-report mentioned in the original report persists for base counters and looks like partial instance sampling; ratios are self-consistent.

Happy to test candidate fixes. It would be great to have (a) the size-split entries added to the gfx1201 internal table, (b) the `-E` event-field offset documented or normalized, and (c) `--list-avail` not listing counters that the active arch table can't program.

