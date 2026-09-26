# [Issue #2165] gfx1010 (RDNA1) support: patch + build guide for ROCm 6.3, 3-GPU AllReduce verified

source: https://github.com/ROCm/rccl/issues/2165
state: closed | updated: 2026-03-19T13:56:33Z
labels: status: triage

## 正文

## Summary

I successfully compiled RCCL from source with `--amdgpu_targets gfx1010` on ROCm 6.3 and verified **3-GPU AllReduce on AMD RX 5700 XT (RDNA1)**. Posting the full patch and findings here for the community and for potential upstream consideration.

**Repo with patch, build guide and test scripts:** https://github.com/Marissccal/rccl-gfx1010

---

## Hardware

- 3x AMD RX 5700 XT (gfx1010, 8 GB VRAM each = 24 GB total)
- AMD Ryzen 7 5700G, B550 chipset
- Ubuntu 22.04, ROCm 6.3
- **AllReduce 3-GPU: PASS ✓**

---

## Problem: `hipStreamBatchMemOpParams` not declared (ROCm 6.3)

When compiling the `develop_deprecated` branch against ROCm 6.3, `ce_coll.cc` fails with:

```
error: 'hipStreamBatchMemOpParams' was not declared in this scope
```

`hipStreamBatchMemOp` and related types were added in ROCm 6.4. They are used exclusively in `ce_coll.cc` (Copy Engine collectives for NVLink/NVLS), which is **never invoked on consumer PCIe GPUs** — gfx1010 has no NVLink capability.

## Fix: compatibility stub in `src/include/rocmwrap.h`

```c
// ROCm <6.4 compatibility stub for hipStreamBatchMemOpParams
// CE collectives are not available on gfx1010 (no NVLink/NVLS).
#ifndef RCCL_HIP_STREAM_BATCH_MEM_OP_COMPAT
#define RCCL_HIP_STREAM_BATCH_MEM_OP_COMPAT
struct hipStreamBatchMemOpWaitValueParams_st {
  unsigned int operation;
  hipDeviceptr_t address;
  union { unsigned int value; unsigned long long value64; };
  unsigned int flags;
  hipDeviceptr_t alias;
};
struct hipStreamBatchMemOpWriteValueParams_st {
  unsigned int operation;
  hipDeviceptr_t address;
  union { unsigned int value; unsigned long long value64; };
  unsigned int flags;
  hipDeviceptr_t alias;
};
union hipStreamBatchMemOpParams {
  unsigned int operation;
  hipStreamBatchMemOpWaitValueParams_st  waitValue;
  hipStreamBatchMemOpWriteValueParams_st writeValue;
};
#define CU_STREAM_WAIT_VALUE_EQ       0x1
#define CU_STREAM_WRITE_VALUE_DEFAULT 0x0
static inline hipError_t hipStreamBatchMemOp(
    hipStream_t, unsigned int, hipStreamBatchMemOpParams*, unsigned int) {
  return hipSuccess; // stub: CE collectives not supported on gfx1010
}
#endif // RCCL_HIP_STREAM_BATCH_MEM_OP_COMPAT
```

---

## Other build blockers (resolved)

| Blocker | Fix |
|---------|-----|
| `fmt` git clone slow (~45 min) | `apt install libfmt-dev` — cmake uses system version |
| `hipify-perl not found` | `apt install hipify-clang` from ROCm 6.4 repo |
| `rocm-device-libs` version conflict | Use ROCm version (`1.0.0.60300`), not Ubuntu's (`5.0.0`) |

---

## Critical: PCIe topology requirement

Even with RCCL compiled correctly, 3-GPU AllReduce will fail if any GPU is connected via **chipset** instead of **CPU-direct PCIe**.

On AMD B550 boards, the physical "PCIe x4" slot near the bottom is wired to the 400 Series chipset — runs at x1 Gen2 (~0.5 GB/s). RCCL AllReduce requires substantially more bandwidth and fails with `hipErrorIllegalState`.

**Diagnosis:**
```bash
lspci -vv | grep -A 3 "LnkSta"
# Look for "downgraded" — means chipset-connected
```

**Fix:** Use M.2 Socket 3 (CPU PCIe x4) with an M.2-to-PCIe adapter. Even x1 Gen3 CPU-direct (~1 GB/s) is sufficient.

Also required: `iommu=pt` in GRUB cmdline.

---

## Note on `roc-obj-ls` false negative

`roc-obj-ls librccl.so.1.0` returns empty on the compiled binary. This is a false negative — the tool does not handle the CCOB compressed format used in ROCm 6.x. Manual extraction confirms gfx1010 code objects are present:

```
amdgcn-amd-amdhsa--gfx1010
hipv4-amdgcn-amd-amdhsa--gfx1010
```

---

## Test result

```
[rank 0] PASS: [6.0, 6.0, 6.0, 6.0]
[rank 1] PASS: [6.0, 6.0, 6.0, 6.0]
[rank 2] PASS: [6.0, 6.0, 6.0, 6.0]
```

---

Full patch file, build script and test: https://github.com/Marissccal/rccl-gfx1010

I hope this is useful for anyone with RDNA1 hardware, and potentially for adding official gfx1010 support in a future release.

— Hernan Sebastian Abeldaño  
Researcher in AI, Blockchain Technologies and Cybersecurity  
https://www.linkedin.com/in/hernan-abelda%C3%B1o/

## 评论 (1)

### huanrwan-amd · 2026-03-04

Hi @Marissccal,

Thank you for the detailed write-up and for sharing the full patch repository. Getting a verified 3-GPU AllReduce working on gfx1010 with documented PCIe topology requirements is a genuinely useful community contribution.

We can confirm the root cause: hipStreamBatchMemOpParams, hipStreamBatchMemOp(), and related symbols were not present in ROCm 6.3 — they were introduced in ROCm 6.4. RCCL's Copy Engine collectives reference these types in ce_coll.cc, but that code path is gated on NVLink/NVLS capability, which gfx1010 (a consumer PCIe GPU) does not have. The stub approach is correct: since hipStreamBatchMemOp is never actually called at runtime on gfx1010, the stub is never reached and its return value is irrelevant.


Thanks again for sharing this — it will be useful for other gfx1010 users in the community.
