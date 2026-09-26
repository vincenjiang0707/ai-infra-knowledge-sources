# [Issue #3119] [Bug]: broadcast_qparams_and_cleanup silently corrupts weight_scale on non-src ranks when modules use CPUCache offload

source: https://github.com/vllm-project/llm-compressor/issues/3119
state: closed | updated: 2026-09-24T11:58:50Z
labels: 

## 正文

### ⚙️ Your current environment

```
OS: Linux-5.15.0-151-generic-x86_64-with-glibc2.35
Python: 3.10.12
llm-compressor: 0.11.1.dev4 (fix/broadcast-qparams-writeback branch)
compressed-tensors: 0.17.1.dev0
transformers: 5.10.1
torch: 2.11.0+cu128
CUDA: 8× NVIDIA L20 (48 GB each)
```

### 🐛 Describe the bug

**Summary:** When running multi-GPU DDP GPTQ quantization, `broadcast_qparams_and_cleanup` silently produces stale/NaN values for `weight_scale`, `weight_zero_point`, and `weight_g_idx` on all non-owning ranks. The quantization completes without any exception — the corruption is invisible until the saved checkpoint is inspected.

**Trigger conditions:**
- `world_size ≥ 2` — multi-GPU DDP used to parallelize activation collection over a large calibration set (throughput bottleneck, not memory)
- GPTQ quantization with sequential pipeline and `auto_offload=True`
- Owning and non-owning ranks each hold **independent** CPUCache entries for qparams (the default when using sequential pipeline with CPU offloading)

**Root cause:**

`CPUCache.__getattr__` does not return the underlying CPU storage tensor. Each call allocates a **new temporary CUDA tensor** (onloaded from CPU):

```python
tmp1 = getattr(module, "weight_scale")   # data_ptr: 0xAAA ─┐
tmp2 = getattr(module, "weight_scale")   # data_ptr: 0xBBB ─┘ different each call
```

`dist.broadcast` modifies `tmp1` in-place. When `tmp1` goes out of scope at the end of the broadcast loop, the result is discarded. The underlying CPUCache storage on the non-src rank retains its original stale (or uninitialized) value.

**Large-scale empirical evidence** (8× L20, Qwen3.5-122B-A10B, N=8192, seq=6144):

| | Run A (with fix) | Run B (upstream / no fix) |
|---|---|---|
| Subgraphs completed | 49/49 ✅ | 49/49 ✅ |
| SCALE_CHECK rank 0 | ✅ CLEAN | ⚠️ nan=31924 neg=402 huge=18 |
| SCALE_CHECK rank 1 | ✅ CLEAN | ⚠️ nan=840 inf=1 neg=3139 |
| SCALE_CHECK rank 4 | ✅ CLEAN | ⚠️ nan=3829 neg=3 |
| All 8 ranks (total=37056) | All CLEAN ✅ | Multiple ranks CORRUPTED ⚠️ |

Corruption concentrates in `weight_scale`/`weight_zero_point` of the first-quantized layer on non-owning ranks. **Both runs complete without any exception.**

---

### 🛠️ Steps to reproduce

No model weights or calibration data are required for either reproduction.

**Layer 1 — Root cause proof (1 GPU, no distributed setup):**

```bash
pytest tests/llmcompressor/utils/test_cpucache_temporary_tensor.py -m unit -v
```

This test demonstrates that:
1. Each `getattr` on a `CPUCache`-offloaded registered parameter returns a different `data_ptr` (new temporary CUDA tensor)
2. An in-place `fill_()` on that temporary does not persist to CPU storage (`test_inplace_modification_lost_without_writeback`)
3. `update_offload_parameter()` correctly flushes the modification back (`test_update_offload_parameter_persists_modification`)

Expected output: **3 passed**

---

**Layer 2 — 2-GPU DDP integration test (real `dist.broadcast` + real CPUCache):**

```bash
pytest tests/llmcompressor/utils/test_broadcast_qparams_ddp_integration.py \
  -m multi_gpu -v -s
```

Expected output demonstrating the bug (Phase A) and fix (Phase B) in a single session:
```
[rank 1] Phase A BUG CONFIRMED: weight_scale=[0.0, 0.0, 0.0, 0.0] (stale, not 42.0)
[rank 1] Phase B FIX CONFIRMED: weight_scale=[42.0, 42.0, 42.0, 42.0]
[rank 0] Phase B FIX CONFIRMED: weight_scale=[42.0, 42.0, 42.0, 42.0]
```

Key design: `offload_module` is called **before** `dist.init_process_group()` so that `OffloadCache.cls_from_device('cpu')` selects `CPUCache` (not `DistributedCPUCache`), giving each rank independent CPU storage — exactly mirroring the real DDP GPTQ scenario.

---

### 🔍 Affected code

`src/llmcompressor/utils/dist.py` — `broadcast_qparams_and_cleanup()`

The function calls `dist.broadcast(as_broadcastable(param), ...)` but never calls `update_offload_parameter()` afterward. On non-src ranks, the broadcast target is a temporary tensor that is discarded when the loop advances to the next module.

**Affected versions:** v0.10.0 – v0.12.0 (all releases since DDP GPTQ was introduced in #2333).

---




## 评论 (6)

### xesdiny · 2026-09-01

@HDCharles @kylesayrs — FYI, this is a bug I discovered while running 
large-scale DDP GPTQ quantization (Qwen3.5-122B-A10B, 8× L20, N=8K S_Len=6144).
The quantization completes silently, but weight_scale values on 
non-owning ranks are stale/NaN in the saved checkpoint.

A fix is ready in PR #3066. The PR includes two new test files:
a single-GPU root-cause proof and a 2-GPU end-to-end reproduction.

(Note: this supersedes issue #2949 which was about a related 
but differently-framed topic.)

### dsikka · 2026-09-10

@soyr-redhat 

### soyr-redhat · 2026-09-11

reprod on 2xh100 w/ qwen3.5-moe architecture. pre-fix run did indeed show NaNs and #3066 produced clean qparams across ranks in repeated runs. Nice work @xesdiny!

### kylesayrs · 2026-09-18

@xesdiny Are you sure that this is an issue? `CPUCache` should essentially never be initialized in a distributed context. Is it possible that, in your example, you [call `oneshot` without calling `init_dist`](https://github.com/vllm-project/llm-compressor/pull/3202)?

If you can, please provide what script you called to trigger this issue

### xesdiny · 2026-09-20

Thanks for the review and for PR #3202, @kylesayrs — the guard against calling `oneshot` without `init_dist` is a useful safety net.

To clarify the scenario this PR targets: `init_dist()` _is_ called in the example script (it is the first non-import statement). The failure is not a missing `init_dist` issue.

---

## Why CPUCache for expert tensors at all?

`DistributedCPUCache.offload()` stores each tensor in a POSIX `/dev/shm` file (`tmpfs` — backed by physical RAM). For a 256-expert-per-layer model like Qwen3.5-122B-A10B this means 36,864 expert shm files, and the physical RAM is exhausted before `linearize_moe` can finish converting all 48 layers.

```
from_pretrained()
  gate_up_proj[256, 2×mid, 7168] + down_proj[256, 7168, mid] loaded to CPU
         │
         ▼ (device_map="auto_offload")
DistributedCPUCache.offload(tensor)
  ├── storage._share_filename_cpu_()
  │       └── creates /dev/shm/torch_XXXXX    ← tmpfs, directly consumes physical RAM
  └── dist.broadcast_object_list(handle)      ← other ranks attach the same shm file
         │
         ▼
shm baseline after from_pretrained: ~231 GB   (dispatch completes normally on all ranks)

load_context.__exit__() → linearize_moe()
         │
         ▼
LinearExperts2D.from_experts_module()   ← standard impl
  for i in range(256):
      expert.gate_proj.weight.copy_(gate_up_proj[i, :mid])  ← .copy_() → new tensor
      expert.up_proj.weight.copy_(gate_up_proj[i, mid:])    ← .copy_() → new tensor
      expert.down_proj.weight.copy_(down_proj[i])           ← .copy_() → new tensor
  → offload_module() → DistributedCPUCache.offload()
      └── new /dev/shm file per expert tensor  ← new physical RAM per file

shm growth (256 × 3 × 48 = 36,864 new shm files, accumulated layer by layer):
  after from_pretrained (baseline)   :  231 GB  (RAM avail: 469 GB)
  linearize_moe step 34/48 (measured):  388 GB  (RAM avail:  24 GB)
  step ~36/48                        :  OOM kill (SIGTERM cascade)   ✗
                                        GPTQ calibration never starts
```

Empirical measurements on L20×8 (768 GB total RAM), Qwen3.5-122B-A10B:

| | After `from_pretrained` | `linearize_moe` step 34/48 |
|---|---|---|
| `/dev/shm` used | 231 GB | **388 GB** (+157 GB) |
| Physical RAM available | 469 GB | **24 GB** → OOM kill |

This is physical RAM exhaustion via tmpfs — increasing `shmmni` or `shmmax` would not help.

---

## CPUCache via slice views: zero extra RAM

The fix patches `LinearExperts2D.from_experts_module` with a zero-copy alternative:

```
from_pretrained()
  same as above — shm baseline: ~231 GB (all ranks, dispatch normal)

linearize_moe()
         │
         ▼
_ddp_from_experts_module()   ← monkey-patch
  for i in range(256):
      expert.gate_proj._parameters["weight"] = gate_up_proj[i, :mid]  ← slice view
      expert.up_proj._parameters["weight"]   = gate_up_proj[i, mid:]  ← slice view
      expert.down_proj._parameters["weight"] = down_proj[i]           ← slice view
         │   views share the SAME physical shm pages — no new allocation
         ▼
CPUCache.from_mapping(module._parameters)
  └── wraps existing tensor refs, zero new shm files, zero new RAM

  original Experts module GC'd → its /dev/shm files released

shm:
  after from_pretrained  :  231 GB  (RAM avail: 469 GB)
  after linearize_moe    :  ~231 GB (views share pages; fused tensors GC'd)
  after oneshot          :  ~231 GB (+<1 GB for qparam shm files)      ✓
```

Empirical measurements on the same node, Qwen3.5-122B-A10B with CPUCache patch (8 ranks, N=32):

| Stage | `/dev/shm` | Δ from baseline | RAM avail |
|---|---|---|---|
| Before `from_pretrained` | 2 GB | — | ~695 GB |
| After `from_pretrained` | 231 GB | +229 GB | 469 GB |
| After `linearize_moe` | **~231 GB** | **0 GB** ← slice views, no new shm files | ~469 GB |
| After `oneshot` | ~231 GB | +<1 GB (qparam shm only) | ~436 GB |

SCALE_CHECK: **CLEAN** — NaN 0 / 37056 on all 8 ranks. ✓

`CPUCache` is only strictly necessary for models where the expert shm footprint would exhaust available physical RAM. Since `/dev/shm` is tmpfs, it is backed by physical RAM — every byte in `/dev/shm` is a byte subtracted from `MemAvailable`. Without the patch, `DistributedCPUCache` OOMs on 122B-A10B during `linearize_moe` step ~36/48 (see the section above). On Qwen3.5-35B-A3B (4 ranks), `DistributedCPUCache` completes successfully and GPTQ runs; the CPUCache patch also produces SCALE_CHECK CLEAN on all 4 ranks.

---

## Why the naive fix fails: meta tensor at `OffloadCache.cls_from_device` override

The root cause is that `OffloadCache.cls_from_device` — when overridden to return `CPUCache` — is invoked during `from_pretrained` **before** the fused 3D expert tensors have been dispatched to non-rank-0 ranks. At that point, non-rank-0 ranks still hold meta tensors, so `CPUCache.from_mapping` raises:

```
RuntimeError: Cannot copy out of meta tensor; no data!
```

The fix patches `LinearExperts2D.from_experts_module` instead, which is called **after** the 3D broadcast completes, so all ranks already have real tensors in shm.

---

## The `broadcast_qparams_and_cleanup` writeback fix

Even with CPUCache slice views for expert weights, the qparams (`weight_scale`, `weight_zero_point`) still go through `broadcast_qparams_and_cleanup`. The writeback bug (detailed in the issue body) means non-src ranks silently retain zero-initialized qparams. The fix in PR #3066 adds an explicit `update_offload_parameter` writeback after `dist.broadcast` completes. Empirical result (same 122B-A10B, N=32):

| Config | All 8 ranks |
|---|---|
| pre-fix (no writeback) | **CORRUPTED** — max NaN 4879 / 37056 weight_scales (per rank) |
| PR  fix | **CLEAN** — NaN 0 / 37056 |

### xesdiny · 2026-09-24

Resolved by #3202 (merged 2026-09-23): a guard was added to the oneshot entrypoint that raises a ValueError when torchrun is detected without a properly initialized distributed process group via init_dist(). This prevents the silent corruption described in this issue.
