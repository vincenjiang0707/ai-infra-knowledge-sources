# [Issue #5229] [Issue]: gfx1201 (R9700) — Triton unified_attention overflows RDNA's LDS budget, and the ROCm 10.0 vLLM container ships no gfx1201 code objects

source: https://github.com/ROCm/aiter/issues/5229
state: open | updated: 2026-09-19T09:09:35Z
labels: 

## 正文

### Problem Description

The AITER README lists **AMD Radeon AI PRO R9700 / gfx1201 (RDNA4)** under Supported Hardware with status *Experimental*, and the footnote states that on RDNA, Triton and most FlyDSL kernels run, as do most HIP kernels — naming *norm*, RoPE, quant and activation, plus some GEMM/attention — with only most CK and ASM kernels being CDNA-only. The library backs this up: gfx1201 has an arch-table entry, an FP8 E4M3FN mapping, a purpose-written FlyDSL flash-attention kernel, GDN support, and RDNA4-tuned conv configs.

On an actual R9700 I ran into two separate problems, which I want to keep distinct because they
sit at different layers:

- **A kernel-level bug.** The Triton unified-attention kernel *is* compiled for gfx1201 and then
  overflows RDNA's LDS budget at launch. Triton compiles at runtime for the local arch, so this is
  independent of how the package was built.
- **A distribution gap.** The prebuilt HIP modules in the container I tested
  (`rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0`) carry code objects for
  **gfx942 and gfx950 only** — 0 of 123 `.so` files include gfx1201. So in this image the HIP
  kernels named in the footnote (norm, RoPE, quant, activation) have no device code for the GPU at
  all. I have only checked this one image and can't speak for the published wheels or other
  distributions.

Separately, `VLLM_ROCM_USE_AITER_RMSNORM` at its default raises a `TypeError` from the pybind
binding. I initially assumed this was the distribution gap surfacing, but the error is an overload
resolution failure at the binding layer, which implies the module loaded and the binding
registered — so the two are not the same problem. Section 4 traces it to a pybind11 module-local
type registration split across two extension modules (`rmsnorm` is bound in
`module_rmsnorm_quant`; `aiter_tensor_t` is registered in `module_aiter_core`), which appears to
be architecture-independent rather than an RDNA issue.

On top of all this, vLLM's own gate keeps AITER out of auto-discovery on all RDNA parts, so none of it is selected without an explicit backend override. The one component that can be forced to run is slower than the default backend.

Details, in the order they are hit:

**1. vLLM gates AITER to CDNA 3+, which contradicts AITER's own Experimental listing for gfx1201**

`vllm/_aiter_ops.py`:

```python
def is_aiter_found_and_supported() -> bool:
    """Checks: platform (ROCm), device arch is CDNA 3 or better, and library existence."""
    if current_platform.is_rocm() and IS_AITER_FOUND:
        from vllm.platforms.rocm import get_cdna_version
        return get_cdna_version() > 2
    return False
```

On R9700 `get_cdna_version()` returns `0`, so auto-discovery never selects an AITER backend. `vllm/platforms/rocm.py` likewise keeps gfx1201 out of `_ON_MI3XX`:

```python
_ON_GFX12X  = any(arch in _GCN_ARCH for arch in ["gfx12"])
_ON_MI3XX   = any(arch in _GCN_ARCH for arch in ["gfx942", "gfx950"])   # gfx1201 not included
```

**2. LDS overflow in `aiter/ops/triton/attention/unified_attention.py` (the main bug)**

Forcing the backend with `--attention-backend ROCM_AITER_UNIFIED_ATTN` on a hybrid GDN model (`Qwen/Qwen3.5-9B`):

```
File "aiter/ops/triton/attention/unified_attention.py", line 631, in unified_attention
    kernel_unified_attention_3d[...]
triton.runtime.errors.OutOfResources: out of resource: shared memory,
Required: 66048, Hardware limit: 65536.
Reducing block sizes or `num_stages` may help.
```

Cause chain:

1. Qwen3.5 is a hybrid GDN model, so vLLM enlarges the attention block size to align pages: `Setting attention block size to 528 tokens to ensure that attention page size is >= mamba page size`.
2. `unified_attention.py` computes `TILE_SIZE = min(64, triton.next_power_of_2(block_size))` → `min(64, 1024)` = **64**, the maximum.
3. RDNA's LDS budget is 64 KB per workgroup (vs 160 KB on CDNA), so the 66048 B request overflows by **512 B**.

The same file already special-cases gfx1201 on the other code path:

```python
TILE_SIZE = 32 if arch.name == "gfx1201" else 16 if arch.is_rdna else 64
```

so the architecture has clearly been considered — but the `min(64, next_power_of_2(block_size))` path bypasses that logic entirely. Note that neither path derives `TILE_SIZE` from the device's reported shared-memory capacity; both encode it as an arch-name literal, so any block size or dtype combination that shifts the LDS request can re-break this on a different RDNA part. **What is the intended tile-size policy for RDNA on this path?**

FP8 does not help and can make it worse:

```python
elif q_dtype == e4m3_dtype and kv_cache_dtype == e4m3_dtype:
    TILE_SIZE = max(32, TILE_SIZE)
```

**3. The tested container contains no gfx1201 device code**

Every prebuilt module in `aiter/jit/` inside this container is compiled for gfx942 and gfx950 only
— there is no gfx1201 device code anywhere in the package:

```console
$ for f in aiter/jit/*.so; do strings "$f" | grep -oE "amdgcn-amd-amdhsa--gfx[0-9]+"; done \
    | sort | uniq -c | sort -rn
   4904 amdgcn-amd-amdhsa--gfx950
   4904 amdgcn-amd-amdhsa--gfx942

$ # .so files containing a gfx1201 code object:
0 / 123

$ # e.g. the module that owns the rmsnorm binding discussed in section 4:
$ strings aiter/jit/module_rmsnorm_quant.so | grep -oE "amdgcn-amd-amdhsa--gfx[0-9]+" | sort -u
amdgcn-amd-amdhsa--gfx942
amdgcn-amd-amdhsa--gfx950
```

gfx1201 *is* a legal build target for AITER — it appears in `allowed_archs` in `aiter/jit/core.py`:

```python
# aiter/jit/core.py:487
archs = os.getenv("GPU_ARCHS", "native").split(";")
# aiter/jit/core.py:~505
allowed_archs = [..., "gfx1200", "gfx1201", "gfx1250", "gfx950", ...]
```

so the module was simply not built for it in this image. I have not checked the published wheels
or other ROCm images, so I can't say how widely this applies — but it means that on the container
AMD publishes for this ROCm release, a gfx1201 user gets no AITER HIP kernels at all.

What makes this look unintentional rather than a deliberate scope decision is that the
Triton/FlyDSL gfx1201 assets *are* shipped in the same package — e.g.
`ops/flydsl/kernels/flash_attn_func_gfx1201.py` and a large set of tuned
`ops/triton/configs/gemm/gfx1201-GEMM-A8W8*.json` files, including FP8/A8W8 shapes. The Python and
Triton side is populated for gfx1201; the binary side is not.

**4. AITER RMSNorm `TypeError`: `rmsnorm` and `aiter_tensor_t` live in different pybind modules**

On `Qwen/Qwen3-1.7B` (no LDS overflow) with `VLLM_ROCM_USE_AITER=1` and
`VLLM_ROCM_USE_AITER_RMSNORM` left at its default (`True`):

```
TypeError: rmsnorm(): incompatible function arguments. The following argument types are supported:
    1. (out: aiter_tensor_t, input: aiter_tensor_t, weight: aiter_tensor_t, epsilon: typing.SupportsFloat | typing.SupportsIndex, gemma_norm: bool = False) -> None

Invoked with: <aiter.jit.module_aiter_core.aiter_tensor_t object at 0x770d0e66b970>, <aiter.jit.module_aiter_core.aiter_tensor_t object at 0x770d0e66bcf0>, <aiter.jit.module_aiter_core.aiter_tensor_t object at 0x770d0e66bc70>, 1e-06
```

This is **not** the missing-code-object problem from section 3: a missing device image would
surface at launch as a HIP "no kernel image is available" error, whereas this fails earlier, at
the pybind binding layer.

What is odd is that the call looks well-formed. Arity matches (four positional arguments, with
`gemma_norm` defaulted), and the three tensors are `aiter_tensor_t` — the same type name the
signature asks for. `1e-06` is a plain Python float and should satisfy `SupportsFloat`.

**Cause: pybind11 module-local type registration across two extension modules.** The first hint is
inside the error message — the two sides name the type differently:

| | rendered as |
|---|---|
| expected, in the signature | `aiter_tensor_t` (bare) |
| actually passed | `aiter.jit.module_aiter_core.aiter_tensor_t` (fully qualified) |

pybind11 renders a parameter's type as the fully-qualified `module.qualname` when `get_type_info()`
resolves that type, and falls back to the demangled C++ name when it cannot. Note this lookup runs
when the binding is *registered*, not when it is called — so on its own the bare name only says
that `aiter_tensor_t` was unresolvable at `rmsnorm`'s registration time, which module
initialization order alone could produce. What makes it interesting is the combination: the type
was unresolvable at registration time *and* the call fails at overload resolution, while the
argument's repr shows its type is registered in `module_aiter_core`. A benign ordering artifact
would render bare and still bind successfully.

Corroborating, `module_aiter_core.so` does carry a module-local marker, and the type is touched
widely across the package:

```console
$ strings aiter/jit/module_aiter_core.so | grep -E "pybind11_module_local|^aiter_tensor_t$"
__pybind11_module_local_v11_system_libstdcpp_gxx_abi_1xxx_use_cxx11_abi_1__
aiter_tensor_t

$ # .so files that touch this type at all:
66 / 123
```

(That marker alone only shows *some* type in that module is module-local, not which one — which
is why it is corroboration rather than the main evidence. To restate what is actually
load-bearing: not the naming asymmetry by itself, which module initialization order could explain
benignly, but the asymmetry *together with* the call failing overload resolution.)

The two registration sites are identifiable from the shipped package. `aiter.rmsnorm` is bound to
`module_rmsnorm_quant`:

```python
# aiter/ops/rmsnorm.py:625
@compile_ops("module_rmsnorm_quant", develop=True)
def rmsnorm(
```

while `aiter_tensor_t` is registered in a different module, `module_aiter_core`:

```console
$ python3 -c "import aiter.jit.module_aiter_core as c; print(c.aiter_tensor_t.__module__)"
aiter.jit.module_aiter_core
```

and `module_rmsnorm_quant` does not register that type itself:

| | registers `aiter_tensor_t` | `module_local` marker | gfx code objects |
|---|---|---|---|
| `module_rmsnorm_quant` (owns `rmsnorm`) | **no** (0 occurrences) | yes | gfx942, gfx950 |
| `module_aiter_core` (owns the type) | **yes** | yes | none (pure binding module) |

With `py::module_local()`, a type registered in one extension module is not visible to another. So
`module_rmsnorm_quant` cannot resolve `aiter_tensor_t` when it registers `rmsnorm` — which is
exactly why the signature renders the bare demangled name — and at call time an object belonging
to `module_aiter_core`'s local registry cannot satisfy that parameter. Every step of that chain is
observable from outside the library, and each matches what the error shows.

**This is not gfx1201-specific.** Nothing in the chain involves the GPU architecture; it would
reproduce wherever these two modules are crossed. It surfaces here because RDNA users are the ones
pushed into unusual flag combinations to get AITER to start at all. If CDNA users do not hit it,
the interesting question is what makes their path differ — e.g. whether `VLLM_ROCM_USE_AITER_RMSNORM`
routes to a different entry point (`rmsnorm2d_fwd*` rather than `rmsnorm`) on those platforms.

Setting `VLLM_ROCM_USE_AITER_RMSNORM=0` allows startup.

**Net effect:** the acceleration-carrying flags (`LINEAR`, `MOE`, `RMSNORM`, `MHA`, `MLA`,
`FP8BMM`, `TRITON_GEMM`) are all enabled by default, and getting AITER to start on this
architecture required turning several of them off. To be precise about what I established:
`RMSNORM` provably has to be off (section 4); five others I disabled together as a block, copying
a community configuration, without re-testing them individually; `MLA` and `TRITON_GEMM` were left
at their defaults and startup still succeeded. So the honest statement is that AITER starts here
only in a reduced configuration whose minimal form I did not determine — with unified attention as
the one component I confirmed doing work, and in an A/B benchmark it is **slower than the default
`ROCM_ATTN`** (see Additional Information).


### Operating System

Ubuntu 24.04.4 LTS (kernel 7.0.0-28-generic)

### CPU

AMD Ryzen 5 7400 6-Core Processor

### GPU

1× AMD Radeon AI PRO R9700, 32 GB — gfx1201 (RDNA4), device ID `1002:7551`

### ROCm Version

ROCm 10.0.0 (inside container) / host ROCm 7.14.0, amd-smi 26.5.0, amdgpu driver 31.40.1 (`amdgpu-install 31.40.1.26130000-2383377.24.04`)

### ROCm Component

HIP

### Steps to Reproduce

Container image: `rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0`
(PyTorch 2.12.0+rocm10.0.0, vLLM 0.27.1.dev5+gf46a9dfe2.d20260827, Python 3.14)

**A. Reproduce the LDS overflow (hybrid GDN model):**

```bash
docker run --rm \
  --device /dev/kfd --device /dev/dri \
  --group-add video --group-add render \
  --security-opt seccomp=unconfined --ipc=host \
  -e VLLM_ROCM_USE_AITER=1 \
  -e VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION=1 \
  -e VLLM_ROCM_USE_AITER_RMSNORM=0 \
  -e VLLM_ROCM_USE_AITER_MHA=0 \
  -e VLLM_ROCM_USE_AITER_MOE=0 \
  -e VLLM_ROCM_USE_AITER_LINEAR=0 \
  -e VLLM_ROCM_USE_AITER_FP8BMM=0 \
  -e VLLM_ROCM_USE_AITER_FP4BMM=0 \
  -e VLLM_ROCM_USE_AITER_TRITON_ROPE=0 \
  rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0 \
  vllm serve Qwen/Qwen3.5-9B \
    --attention-backend ROCM_AITER_UNIFIED_ATTN \
    --max-model-len 8192 --gpu-memory-utilization 0.85
```

→ `OutOfResources: Required: 66048, Hardware limit: 65536` at kernel launch.

**B. Reproduce the RMSNorm `TypeError` (plain transformer):**

Same command with `Qwen/Qwen3-1.7B` and `VLLM_ROCM_USE_AITER_RMSNORM` removed (i.e. left at its default `1`) → `TypeError: rmsnorm(): incompatible function arguments`.

**C. A configuration that does start on gfx1201:**

Command A with `Qwen/Qwen3-1.7B` — unified attention, with six fused subsystems explicitly
disabled. I did not narrow this down, so it is a configuration that works, not the minimal one:
`RMSNORM` is the only flag I confirmed has to be off.

**D. Verify the shipped build targets (no GPU required):**

```bash
docker run --rm rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0 bash -lc '
AI=/opt/python/lib/python3.14/site-packages/aiter/jit
for f in "$AI"/*.so; do strings "$f" | grep -oE "amdgcn-amd-amdhsa--gfx[0-9]+"; done \
  | sort | uniq -c | sort -rn
echo "--- .so files containing a gfx1201 code object ---"
c=0; for f in "$AI"/*.so; do strings "$f" | grep -q "amdgcn-amd-amdhsa--gfx1201" && c=$((c+1)); done
echo "$c / $(ls "$AI"/*.so | wc -l)"
'
```

Output on this image:

```
   4904 amdgcn-amd-amdhsa--gfx950
   4904 amdgcn-amd-amdhsa--gfx942
--- .so files containing a gfx1201 code object ---
0 / 123
```

| Model | Architecture | Result with AITER |
|---|---|---|
| `Qwen/Qwen3.5-9B` | Hybrid GDN (gated delta net) + attention | ❌ LDS overflow at kernel launch |
| `Qwen/Qwen3-1.7B` | Plain transformer | ✅ Starts in the reduced configuration above (minimal set not determined) |

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.21
Runtime Ext Version:     1.26
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  ENABLED
XNACK enabled:           NO
DMAbuf Support:          YES
VMM Support:             YES
Fabric Support:          NO

==========               
HSA Agents               
==========               
*******                  
Agent 1                  
*******                  
  Name:                    AMD Ryzen 5 7400 6-Core Processor  
  Uuid:                    CPU-XX                             
  Marketing Name:          AMD Ryzen 5 7400 6-Core Processor  
  Vendor Name:             CPU                                
  Feature:                 None specified                     
  Profile:                 FULL_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        0(0x0)                             
  Queue Min Size:          0(0x0)                             
  Queue Max Size:          0(0x0)                             
  Queue Type:              MULTI                              
  Node:                    0                                  
  Device Type:             CPU                                
  Cache Info:              
    L1:                      32768(0x8000) KB                   
  Chip ID:                 0(0x0)                             
  ASIC Revision:           0(0x0)                             
  Cacheline Size:          64(0x40)

Agent 2                  
*******                  
  Name:                    gfx1201                            
  Uuid:                    GPU-f4260aceb5c9da73               
  Marketing Name:          AMD Radeon AI PRO R9700            
  Vendor Name:             AMD                                
  Feature:                 KERNEL_DISPATCH                    
  Profile:                 BASE_PROFILE                       
  Float Round Mode:        NEAR                               
  Max Queue Number:        128(0x80)                          
  Queue Min Size:          64(0x40)                           
  Queue Max Size:          131072(0x20000)                    
  Queue Type:              MULTI                              
  Node:                    1                                  
  Device Type:             GPU                                
  Cache Info:              
    L1:                      32(0x20) KB                        
    L2:                      8192(0x2000) KB                    
    L3:                      65536(0x10000) KB                  
  Chip ID:                 30033(0x7551)                      
  ASIC Revision:           1(0x1)                             
  Cacheline Size:          256(0x100)                         
  Max Clock Freq. (MHz):   2350                               
  BDFID:                   768                                
  Internal Node ID:        1                                  
  Compute Unit:            64                                 
  SIMDs per CU:            2                                  
  Shader Engines:          4                                  
  Shader Arrs. per Eng.:   2                                  
  WatchPts on Addr. Ranges:4                                  
  Coherent Host Access:    FALSE                              
  Memory Properties:       
  Features:                KERNEL_DISPATCH 
  Fast F16 Operation:      TRUE                               
  Wavefront Size:          32(0x20)                           
  Workgroup Max Size:      1024(0x400)                        
  Workgroup Max Size per Dimension:
    x                        1024(0x400)                        
    y                        1024(0x400)                        
    z                        1024(0x400)                        
  Max Waves Per CU:        32(0x20)                           
  Max Work-item Per CU:    1024(0x400)
```

</details>

### Additional Information

**Benchmark: AITER unified attention vs default `ROCM_ATTN`**

Same GPU, same model (`Qwen/Qwen3-1.7B`), same image, identical flags apart from the attention backend. `vllm bench serve`, random dataset, input 512 / output 256, 100 prompts, concurrency 8, seed 42.

| Metric | AITER unified attn | `ROCM_ATTN` (default) | Delta |
|---|---|---|---|
| Output throughput | 708.63 tok/s | **755.18 tok/s** | ROCM_ATTN +6.6% |
| Mean TTFT | 527.20 ms | **437.03 ms** | ROCM_ATTN −17.1% |
| Mean TPOT | 8.94 ms | **8.59 ms** | ROCM_ATTN −3.9% |
| Failed requests | 0 | 0 | — |

This is not a like-for-like AITER-vs-CK comparison: it is *AITER with unified attention active and
several fused subsystems disabled* vs *the full default path*. I did not establish the minimal set
of disables, so a better-tuned AITER configuration may well exist — but since `RMSNORM` at its
default prevents startup outright, some reduction is unavoidable, and this reflects a
configuration that actually runs on gfx1201 today.

**Full AITER flag status on gfx1201 (vLLM 0.27.1)**

| Env var | Default | Status on gfx1201 |
|---|---|---|
| `VLLM_ROCM_USE_AITER` | `False` | must set `1` |
| `VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION` | `False` | ✅ only working component |
| `VLLM_ROCM_USE_AITER_RMSNORM` | **`True`** | ❌ **verified failure** — `TypeError`, cross-module pybind type identity (section 4); likely not arch-specific |
| `VLLM_ROCM_USE_AITER_LINEAR` | **`True`** | ⚠️ not individually tested — disabled pre-emptively |
| `VLLM_ROCM_USE_AITER_MOE` | **`True`** | ⚠️ not individually tested — disabled pre-emptively |
| `VLLM_ROCM_USE_AITER_MHA` | **`True`** | ⚠️ not individually tested — disabled pre-emptively |
| `VLLM_ROCM_USE_AITER_FP8BMM` | **`True`** | ⚠️ not individually tested — disabled pre-emptively |
| `VLLM_ROCM_USE_AITER_FP4BMM` | **`True`** | ⚠️ not individually tested — disabled pre-emptively (RDNA4 has no FP4: `is_fp4_avail()=False`) |
| `VLLM_ROCM_USE_AITER_MLA` | **`True`** | ✅ left at default — startup still succeeded |
| `VLLM_ROCM_USE_AITER_TRITON_GEMM` | **`True`** | ✅ left at default — startup still succeeded |
| `VLLM_ROCM_USE_AITER_CUSTOM_AR` | **`True`** | untested (single GPU) |
| `VLLM_ROCM_USE_AITER_LINEAR_HIPBMM` | `False` | off by default |
| `VLLM_ROCM_USE_AITER_FP4_ASM_GEMM` | `False` | off by default |
| `VLLM_ROCM_USE_AITER_TRITON_ROPE` | `False` | off by default |
| `VLLM_ROCM_USE_AITER_FUSION_SHARED_EXPERTS` | `False` | off by default |

To be explicit about what this table is and isn't: the only flag I proved must be off is
`RMSNORM`. The five marked ⚠️ were disabled together, copying a community configuration, and never
re-enabled one at a time — so I can't claim each one individually breaks. `MLA` and `TRITON_GEMM`
were left at their defaults and startup still succeeded.

## 评论 (12)

### taisunyoung · 2026-09-03

Same card (R9700, gfx1201) and the same image you tested — `rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0`. We had been sweeping it for an unrelated spawn-to-spawn throughput issue (ROCm/legacy-rocm-build#6347) when we ran into the same wall, so we have a fair amount of runtime data on the exact container you are describing. Two things that may be useful, plus one that is not in your report.

**Inference does run on this image, through the Triton path.** Your distribution-gap finding predicts the HIP kernels have no device code, and that matches what we saw — but the server still comes up and serves. Two models, 26 cold spawns total, all measured single-stream (2 warmup calls then 10 measured, `max_tokens=100`):

```
gemma-4-12B-it-FP8-Dynamic   10 spawns   33.57 - 33.73 tok/s   (spread 0.16)
Qwen3-14B-FP8                16 spawns   26.81 - 27.59 (15 of them), one at 35.13
```

So the 0-of-123 gap is not fatal for a plain serve path. Worth stating explicitly since "no device code for the GPU at all" reads worse than it turned out to be for us — whatever is missing, the Triton kernels cover enough of the decode path to work.

For scale, our production stack (`vllm/vllm-openai-rocm:v0.23.0`, ROCm 7.2.3, same box, same model and flags) measures 34.05 on that gemma model. So this image costs us about 1.3 % on that path. I would not read that as a ROCm 10 number, though — per your finding it is a *ROCm 10 minus the AITER HIP kernels* number, which is exactly the ambiguity your issue is about.

**Your LDS overflow reproduces one layer up, and it is not new to ROCm 10.** We hit the identical failure on `vllm/vllm-openai-rocm:v0.28.0` (ROCm 7.2.3, so nothing to do with the ROCm 10 packaging), starting gemma-4-12B with `VLLM_ROCM_USE_AITER=1 --attention-backend ROCM_AITER_UNIFIED_ATTN`:

```
triton.runtime.errors.OutOfResources: out of resource: shared memory,
Required: 65792, Hardware limit: 65536
RuntimeError: Engine core initialization failed.
```

Byte-identical numbers to vllm-project/vllm#48723 and ROCm/aiter#4329, which pin it to `select_3d_config` producing a non-gfx1250 Wave32 configuration. Since Triton compiles at runtime for the local arch, as you say, this is orthogonal to the packaging problem — same overflow on a 7.2.3 image with fully-populated code objects.

**One thing not in your report: this image will not start Gemma 4 at all without a downgrade.**

```
transformers.integrations.heterogeneity.configuration_utils.AmbiguousGlobalPerLayerAttributeError:
'head_dim' is a per-layer attribute and may vary across layers
```

The container ships transformers 5.16.1, and the vLLM snapshot in it (`0.27.1.dev5+gf46a9dfe2`, built 2026-08-27) predates vllm-project/vllm#49797 ("Fix Gemma 4 for upcoming Transformers version", merged 2026-08-10). vllm-project/vllm#52768 is the same crash reported against v0.27.1 and closed as already fixed. `pip install transformers==5.12.0` inside the container works around it and is what all the numbers above were measured with — but the real fix is a newer vLLM snapshot, so this should disappear on the next image build rather than needing anything from AITER.

Happy to run anything specific on this box if it helps narrow the packaging question — we have the image, the card, and it is not carrying production traffic.


### xy7ra · 2026-09-09

Follow-up with a second, independent reproduction of the LDS overflow, plus perf numbers that may bear on whether this backend should be opt-in on RDNA.

### Reproduced on a different model, same overflow

2x Radeon AI PRO R9700 (gfx1201), ROCm 7.14 wheel stack (torch 2.12.0+rocm7.14.0, triton 3.7.1), aiter installed from source, vLLM built for gfx1201. Model: **Qwen3.6-35B-A3B-FP8** (hybrid GDN + MoE), TP=2, `--enforce-eager`. Byte-identical failure to the original report:

```
triton.runtime.errors.OutOfResources: out of resource: shared memory,
Required: 65792, Hardware limit: 65536.
  File "aiter/ops/triton/attention/unified_attention.py", line 603, in unified_attention
    kernel_unified_attention_3d[
```

Two details that were not obvious to me at first and may help others:

1. **A single short request succeeds.** The overflow only fires once a request needs the `_3d` (split-KV) path — i.e. at concurrency, or with a long prompt. A one-shot smoke test passes and the engine looks healthy, then dies under real load. I lost a benchmark run to this.
2. **It takes the engine down**, not just the request: `EngineDeadError`, all in-flight requests 500, server unrecoverable.

Required is only **256 bytes** over the limit (65792 vs 65536), so a modest reduction in the 3d kernel's block/stage sizing on RDNA — or an arch-aware config that keeps it under 64 KB — looks like it would be enough. The 2d path appears unaffected.

### Related vLLM-side gate

On RDNA, vLLM force-selects this backend at priority 0 whenever `VLLM_ROCM_USE_AITER=1`, ignoring `VLLM_ROCM_USE_AITER_UNIFIED_ATTENTION`, so there is currently no way to keep aiter's linear GEMM while avoiding this kernel. Filed separately with a patch: https://github.com/vllm-project/vllm/issues/56021

### Perf data: aiter regresses this MoE model on RDNA4

With that gate patched locally I could finally isolate aiter's linear path from its attention path. Four alternating arms, same fused-MoE config and the same `ROCM_ATTN` backend in both, medians, both arms reproducible to <1%:

| workload | `AITER=0` | `AITER=1` (linear only, unified attn off) |
|---|---:|---:|
| decode, 1 stream | 24.9 tok/s | 19.9 tok/s (**-20%**) |
| decode, 8 streams | 183.1 tok/s | 142.7 tok/s (**-22%**) |
| decode, 8 streams TTFT | 246 ms | 538 ms (**-118%**) |
| prefill, 4 streams | 31.5 tok/s | 29.6 tok/s (-6%) |
| prefill, 1 stream TTFT | 195 ms | 194 ms (flat) |

To be clear this is **not** a blanket anti-aiter result: on a **dense** FP8 model (Qwen3-32B-FP8) on the same box, `AITER=1` + `AITER_LINEAR=1` is worth roughly **+15%** single-stream. The regression looks specific to MoE, and the likely reason is structural: Qwen3.6-35B-A3B activates ~3B params, so the bulk of the FLOPs sit in the expert FFNs (`fused_moe`) rather than the dense projections `AITER_LINEAR` accelerates — so you pay dispatch overhead without the corresponding win.

Two suggestions, take or leave:
- Consider making the unified-attention backend opt-in on RDNA until the LDS sizing is fixed, since today it is both default-on and non-functional there.
- `aiter.fused_moe` may deserve an explicit RDNA guard as well: on gfx1201 the CK 2-stage path JIT-compiles and runs but returns wrong results (relerr ~1.4 vs `aiter.fused_moe.torch_moe`), silently, unlike the a8w8 GEMMs which are correctly gated. I am carrying a local `NotImplementedError` guard for it.

Happy to test any patch on this hardware.


### amd-xavierwang · 2026-09-19

Hello, I hope below should help a bit:
1. `is_aiter_found_and_supported()` is intentionally left out for gfx1201, because this is the flag that enables some Gluon/other unsupported kernel backends on RDNA. a similar function, [`is_aiter_found_and_supported_on_rdna4()`](https://github.com/vllm-project/vllm/blob/038cb14bd7874030e98bb6edc4b6f4efe649fff7/vllm/_aiter_ops.py#L219) is used.
2. For your problem 2 and 4, can you try if they are fixed after https://github.com/ROCm/aiter/pull/4868 this? The RMS_NORM problem should be solved in main branch as well.
3. For your problem 3, gfx1201 right now only uses Triton kernels for hot ops which shouldn't require any pre-build.(unlike CK kernels used on CDNA). However, I am not too sure about this. If you have further thoughts, please let me know and we can look into this.

### taisunyoung · 2026-09-19

Thanks for the detail. Point 3 lines up with what we measured on that image, and it means one of our own labels in this thread was wrong.

**On point 3 — the missing gfx1201 device code.**

We ran 26 cold spawns on the exact image in the report (`rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0`) on a single R9700: gemma-4-12B-it-FP8-Dynamic 10 spawns at 33.57–33.73 tok/s, Qwen3-14B-FP8 16 spawns at 26.81–27.59 with one at 35.13. Single-stream, two warmup calls then ten measured, `max_tokens=100`. Nothing degraded gracefully or fell over; the server simply worked.

When we posted those numbers we described them as "ROCm 10 **minus** the AITER HIP kernels", which implies they were handicapped by the packaging gap. If gfx1201 goes through Triton for the hot ops by design, that framing is wrong — they are just the normal path for this card, not a reduced one. I'm taking your "not too sure" at face value rather than treating it as settled, so the accurate statement is: our measurements are consistent with your explanation, and we have no evidence that the absent code objects cost us anything on a plain serve path. We should not have implied otherwise.

If it would help pin point 3 down, say which ops you expect to be HIP versus Triton on gfx1201 and we can log what actually gets dispatched at runtime on this card.

**On point 2 — whether #4868 fixes the LDS overflow. We can't answer that cleanly from our environment, and I'd rather say why than give you a result that doesn't mean anything.**

Our production stack is `vllm/vllm-openai-rocm:v0.23.0` (ROCm 7.2.3). The aiter tree inside it is dated 2026-06-02 by file timestamps, and the parts #4868 touches are not there:

- `aiter/ops/triton/utils/unified_attention_utils.py` — does not exist in our tree
- `aiter/ops/triton/configs/gfx1201/…` — no such directory. Our `configs/` holds `gfx942-*.json`, `gfx950-*.json` and `gfx1250-*.json` plus `gemm`, `hstu_attn` and `moe`; there is no per-arch directory for any gfx12xx part
- `select_3d_config` does exist, but inside `aiter/ops/triton/attention/unified_attention.py`, i.e. before the refactor your PR builds on

So applying the patch isn't a few lines here; it means replacing aiter wholesale with a tree roughly four months newer. If we did that and the overflow disappeared, we could not tell you whether #4868 fixed it or one of the other changes in that window did, and if it broke we could not tell you whether that was aiter or an API mismatch with the vLLM snapshot we run. Either outcome would be noise in your issue rather than a data point.

What we can offer is the repro, and a box to run it on when a build with #4868 in it exists. The failure we hit is the same byte counts as the original report, on **ROCm 7.2.3, not ROCm 10** — `vllm/vllm-openai-rocm:v0.28.0`, gemma-4-12B (head_size 256), `VLLM_ROCM_USE_AITER=1` with `--attention-backend ROCM_AITER_UNIFIED_ATTN`, failing at engine init with `Required: 65792, Hardware limit: 65536`. That may be worth noting for triage: the overflow is not specific to the ROCm 10 packaging, so the fix matters for the 7.x images too. The machine is a dedicated test box with no production traffic, so we can run whatever a newer image needs.

For what it's worth on the practical side, we read the note in your PR that for head_size 256/512 vLLM's upstream `TRITON_ATTN` is generally faster than the aiter 3D configs. That matches how we ended up running: gemma-4-12B on `TRITON_ATTN` is our production path, at the 34.05 tok/s quoted in our earlier comment. We have no aiter-side number to compare it against, because that combination is exactly the one that fails to start.


### amd-xavierwang · 2026-09-19

Hi thanks for the follow up.
I want to make things bit more clear:
1. We are the ROCm on RDNA team, and we never used any HIP/CK based backend so far in aiter. If we do so in the future, we will make sure to handle it.
2. I am happy as long as the LDS issue has been fixed for you, whether it's by #4868 or some other changes.:)
3. For gemma4, I only tried at decode kernel level that TRITON_ATTN is better than AITER_UNIFIED_ATTN. However, I never tried model e2e inference level because I was looking into 26b model and it's hard to run with single gfx1201.
4. I am currently working on gemm4 for another GPU: https://github.com/ROCm/aiter/pull/5601. For this GPU, it looks like AITER attn can be better at prefill so I wouldn't conclude `TRITON_ATTN` is universally a better option for gemma4. As gfx1151 is bit different from gfx1201, it may be worth it to actually compare A/B the 2 backends, for aiter supports gemma4 now. In addition, if you feel gemma4 performance is not too optimal, feel free to tune it similarly to this PR or you can ping our team and we can do it.:)

Thank you for the patience and we are open to any future defects support! Again I am from the ROCm team, so feel free to ping me if you encounter any similar RDNA issues that needs to be addressed.

### taisunyoung · 2026-09-19

That settles point 3 — if the RDNA path has never used a HIP/CK backend in aiter, the absent gfx1201 code objects are the design rather than a packaging gap, and we will stop attaching that caveat to our numbers.

On the prefill point, I would like to take you up on the A/B, because prefill is the part of our workload that actually decides what the user feels. Our system prompt is fixed and gets prefix-cached, but the retrieval chunks we attach change with every question, so they are paid in full on every request. Decode we are comfortable with; prefill is the number we watch.

**Where we are today, so the comparison has a baseline.**

Single Radeon AI PRO R9700 (gfx1201), `vllm/vllm-openai-rocm:v0.23.0`, ROCm 7.2.3, gemma-4-12B-it-FP8-Dynamic, `TRITON_ATTN`, `cudagraph_mode=FULL_AND_PIECEWISE`, `--kv-cache-dtype fp8`, `--max-model-len 8192`.

| | |
| --- | --- |
| prefill, cache-missing | **993 tok/s** (per-spawn medians 992 - 994 across 6 cold spawns) |
| same, wall time | 7.82 s for a prompt of 7,765 - 7,770 tokens (the per-request ID shifts it slightly) |
| decode, single stream | 33.7 tok/s |

We quoted 34.05 for this model earlier in the thread. The box's host kernel moved from 6.17 to 7.0 in between (an unattended upgrade that a power cut applied), and the same image in the same harness now reads 33.7. I am not claiming the kernel caused that — a single measurement through our production path on the new kernel came back at 34.03 — so treat it as our current baseline rather than a result.

Method for the prefill row, since a shared prompt would have made it meaningless: each request carries a unique ID at the **front** of the prompt so nothing hits the prefix cache, `max_tokens=1`, and the rate is `usage.prompt_tokens` divided by wall time. One warmup then four measured requests per spawn, sequential, no concurrency.

One observation that is part of why I want to measure rather than assume: running the same model and flags on your `rocm/vllm:rocm7.14.1_rdna_ubuntu24.04_py3.14_pytorch_2.11_vllm_0.23.0` image instead, prefill went to 1102 tok/s (1100 - 1103, six spawns, same harness, alternated with the baseline on the same day) while decode moved only from 33.73 to 33.90. We cannot attribute that 11 % — ROCm, torch, Python and the vLLM snapshot all differ between the two images, and we separately ruled out the one environment variable that differed on the BLAS path (`ROCBLAS_USE_HIPBLASLT`, A/B'd at 6 spawns per arm: 994 vs 994 tok/s, no effect). So prefill on this card clearly moves with something below the model, which makes the backend question worth answering properly.

**What I need from you to run it.**

The A/B itself is clean — same container, same flags, only `--attention-backend` changes between arms, so whatever build we stand it up on, the comparison is single-variable. The problem is which build. The aiter tree in our production image is dated 2026-06-02 and predates gemma4 support entirely, and the newest RDNA image we have tested (the `rocm7.14.1_rdna` one above, built around 2026-09-01) still predates #4868. So:

- is there a nightly or newer image that already carries aiter with #4868 in it, or
- which vLLM version would you pair with aiter installed from main, so that I am not reporting an API mismatch as a performance result?

Once you point at a combination you would trust, we will run gemma-4-12B with `TRITON_ATTN` and `ROCM_AITER_UNIFIED_ATTN` back to back and report cache-missing prefill, single-stream decode and aggregate throughput at concurrency. The box is a dedicated test machine with no production traffic, so the run itself is not a problem.


### amd-xavierwang · 2026-09-19

Unfortunately, I am not aware any nightly/new image that would include #4868. That was merged this Tuesday and likely you have to "build" from source, main branch. The good thing like I said is gfx1201 so far only uses Triton kernels, so you don't "build" anything. Don't anticipate any build errors and you can just follow the regular aiter source installation from README.

For vLLM, I am confident you can use any recent public vLLM release images. Again gfx1201 uses Triton based attn now, so version vise it should be lenient. Obviously the more recent version vLLM you use, more optimization potential you get. One thing I am not sure about is whether vLLM can properly pick up build-from-source aiter if vLLM itself is not installed from source. Likely it will work.

So my recommendation: any good image with vLLM installed, clone aiter and install main branch.

One thing: aiter attn only supports causal, so it only makes sense to compare if your usage is LLM only. I assume TRITON_ATTN is necessary for multi-modal.

### amd-xavierwang · 2026-09-19

we can close this issue with all points addressed from the beginning. Any gemm4 perf can go to a new issue for cleaness.

### taisunyoung · 2026-09-19

Before this closes — one thing I should flag, because I acted on it publicly and I may have been too quick.

I took "we never used any HIP/CK based backend so far in aiter" to mean the absent gfx1201 code objects in point 3 are the design rather than a gap, and I said so above. But aiter's own README says something different in the supported-hardware footnote for RDNA:

> On RDNA, Triton and most FlyDSL kernels run, as do most HIP kernels (norm, RoPE, quant, activation, plus some GEMM/attention). Most CK and ASM kernels are CDNA-only.

That reads as HIP kernels being expected to run on RDNA, with CK and ASM being the CDNA-only part — which is closer to the original report than to my reading of your reply.

I can see at least three ways this fits together and I can't tell which from outside: the footnote is stale; "run" means they compile and work if built for the arch, not that the shipped `.so` files carry gfx1201; or your team's RDNA path deliberately routes around HIP kernels even though they would work. Any of those is fine, they just have different consequences for whoever reads point 3 next.

If the footnote is the accurate one, then point 3 is a real packaging gap and my correction above was wrong, and I'd rather have that on the record than leave a misleading endorsement behind. If the footnote is out of date, updating it would save the next person on RDNA the same detour.

This is a documentation question rather than a defect, so it shouldn't hold the issue open by itself.

One thing might be worth a short wait, though. We are setting up `rocm/vllm:latest` with aiter installed from main right now, exactly as you recommended, on the gfx1201 box. That run will say whether #4868 actually clears the overflow on this arch — right now point 2 is "merged" rather than "verified on gfx1201", and as far as I can see neither the reporter nor the second reproducer has confirmed it on hardware yet. It is a day or two of work, not weeks. I'll post the result here if the issue is still open, or in the new gemma4 issue if it has closed by then, and the gemma4 performance numbers will go to the new issue either way.


### amd-xavierwang · 2026-09-19

Your understanding is right. At kernel level, our team member verified that those HIP kernels would work stand alone on gfx1201, for the sake of investigation. However, we haven't enabled/tried them in model serving environment, for instance in vLLM. The reason is they are not bottlenecks to models and so far we only attempts hot ops like attn and gemm, which are so far all Triton based.

RDNA kernel optimization in vLLM upstream is hard, and that's why we started to migrate hot OPs to Aiter to have more control, a few months ago. Before that, aiter was not even officially supported/usable on RDNA, despite those small HIP would technically work. That's why we assumed no users demands to those HIP kernels for gfx12. 

### taisunyoung · 2026-09-19

Ran it on the hardware. Writing this out in more detail than usual so you don't have to guess at any part of our setup, and so it's clear where I'm reporting an observation versus where I'd be inferring something.

**Setup.** Your image, unmodified: `rocm/vllm:latest`, digest `sha256:30761c2125ce150d556bef46406a0158446421886bf83a2e60154c6e4ca17a13`. One thing worth flagging so nobody assumes we tested something newer — the tag was pushed 2026-09-18, but `docker inspect` says `Created: 2026-08-27`, and the contents match the `rocm10.0.0_…_vllm_0.27.0` build: ROCm 10.0.0, torch 2.12.0+rocm10.0.0, vLLM 0.27.1.dev5+gf46a9dfe2.d20260827, Python 3.14.7, Triton 3.8.0, bundled amd-aiter 0.1.20.post1. Host untouched throughout — Ubuntu 24.04, kernel 7.0.0-31, in-tree amdgpu, host ROCm 7.2.3, one R9700, no `PYTORCH_*_ALLOC_CONF` set anywhere.

aiter from source exactly as the README has it, `git clone --recursive` then `python3 setup.py develop`, landing on `amd-aiter==0.1.1.dev50+g6214264b1` at HEAD `6214264` (2026-09-19). You were right that gfx1201 needs nothing prebuilt — no build errors, and it finished quickly. Triton stayed at 3.8.0, before and after.

Model is gemma-4-12B-it-FP8-Dynamic with `--attention-backend ROCM_AITER_UNIFIED_ATTN`, `VLLM_ROCM_USE_AITER=1`, gpu-mem-util 0.90, max-model-len 8192, fp8 KV cache. Three cold spawns.

**Point 2 — the overflow is gone.** The engine starts and serves. Same combination that used to die at init with `Required: 65792, Hardware limit: 65536`, which for what it's worth we had also hit on `vllm/vllm-openai-rocm:v0.28.0` with ROCm 7.2.3, so it was never a ROCm 10 packaging thing.

I can't tell you #4868 is what fixed it, and I'd rather not have that on the record as though I'd checked. The files that PR touches are in main, but we cloned `--depth 50`, so `git log -- <path>` just returns the oldest commit in that window — it pointed at an unrelated revert. What I can say is that on main at `6214264` the overflow doesn't happen on gfx1201.

Minor thing while I was looking: `RDNA_LDS_LIMIT` from the PR description isn't anywhere in the tree, and `RDNA_ARCHS` lives in `aiter/ops/triton/_triton_kernels/flash_attn_triton_amd/utils.py` rather than the attention path. What's actually there is per-arch `TILE_SIZE_MIN`/`TILE_SIZE_MAX` in the config JSON, clamped by `compute_tile_params()`, with a `configs/gfx1201/` directory. Same guard in effect — the PR text just names symbols that aren't what got merged, which had me hunting for the wrong thing for a few minutes.

**Point 4 — RMSNorm is fine at the default.** I left `VLLM_ROCM_USE_AITER_RMSNORM` alone instead of forcing it to 0, so this actually tested your claim rather than working around it. No pybind `TypeError`, clean start, correct output.

**Point 3 — still reproduces on `latest`, and the kernels do build.** Your explanation holds, but I'd rather put evidence beside it than just agree twice. The shipped package in today's `latest` still carries no gfx1201 code:

```
123 .so files, 0 containing gfx1201
   4904  amdgcn-amd-amdhsa--gfx942
   4904  amdgcn-amd-amdhsa--gfx950
```

So what the original reporter measured on 2026-09-03 is still true of the current image. But with the source install active, aiter builds the module for gfx1201 on demand in 27.7 seconds:

```
[aiter] finish build [module_aiter_core], cost 27.7s
[aiter] import [module_aiter_core] under /opt/aiter/aiter/jit/module_aiter_core.so
```

Which is exactly what you described — they work standalone, they're just not shipped. To be clear about what that observation is worth: it shows the module builds and imports, not that those HIP kernels would buy anything in serving. You already said they aren't the hot ops and nothing here argues otherwise.

**The trap, which answers the question you weren't sure about.** You said you didn't know whether vLLM would pick up a source-built aiter when vLLM itself isn't built from source. It doesn't, and it fails quietly. After `setup.py develop`, `easy-install.pth` has `/opt/aiter` in it, but `site-packages` comes first on `sys.path`, so `import aiter` still resolved to the shipped 0.1.20.post1. Following your advice as written, we'd have believed we were on main while measuring the shipped package, and every number below would have been wrong in a way that looks completely normal. Moving the bundled one aside fixes it:

```bash
SP=/opt/python/lib/python3.14/site-packages
mv $SP/aiter $SP/aiter.bundled.bak
mv $SP/amd_aiter-0.1.20.post1.dist-info $SP/amd_aiter-0.1.20.post1.dist-info.bak
```

Probably worth a line in the README beside the source-install steps, since anyone on an image that ships aiter will walk into it. Same category, different problem: `transformers` 5.16.1 in the image refuses Gemma 4 with `AmbiguousGlobalPerLayerAttributeError: 'head_dim' is a per-layer attribute`, so we pinned 5.12.0.

**On multimodal.** You assumed `TRITON_ATTN` would be needed since aiter attention is causal-only. With the aiter backend a 256x256 red-circle-on-white PNG came back as "흰색 배경 위에 빨간색의 둥근 모양이 있습니다", which is correct, so it runs. I wouldn't call that multimodal being correct under aiter attention though — one simple shape won't expose a subtle problem with the bidirectional mask over image tokens, and that distinction is the thing standing between us and using this in production. If you can name an image case that would actually stress that path, we'll run it and report whichever way it goes.

**Performance went to its own issue** as you suggested: ROCm/aiter#5683. Short version, on this build `ROCM_AITER_UNIFIED_ATTN` is 4.65x faster than `TRITON_ATTN` at cache-missing prefill (5107 vs 1098 tok/s), decode within 2.6%. Opposite direction from the head_size 256/512 note in #4868, and closer to what you were seeing on gfx1151.

No objection to closing this. Thanks for the detail in your answers — the RDNA background explained a fair bit we'd been guessing at from the outside.


### taisunyoung · 2026-09-19

One more data point, and then I'll stop filling up your issue.

In my last comment I said the overflow is gone on main but I had not checked whether the image that ships today still hits it — we had moved the bundled aiter aside rather than testing it. That was an inference, so I went back and ran it properly. Same image and digest as before, bundled `amd-aiter 0.1.20.post1` left exactly as shipped, `transformers==5.12.0` as the only change (otherwise Gemma 4 will not load at all), gemma-4-12B with `VLLM_ROCM_USE_AITER=1` and `--attention-backend ROCM_AITER_UNIFIED_ATTN`.

It hits both of them, one after the other:

| aiter | `VLLM_ROCM_USE_AITER_RMSNORM` | result |
|---|---|---|
| shipped 0.1.20.post1 | default | `TypeError: rmsnorm(): incompatible function arguments` — point 4 |
| shipped 0.1.20.post1 | `0` | `OutOfResources: out of resource: shared memory, Required: 66048, Hardware limit: 65536` — point 2 |
| main `6214264` | default | starts and serves |

So the first run never reached the LDS path — RMSNorm killed it first, which is why I had not seen the overflow in what I posted earlier. With RMSNorm out of the way it surfaces immediately.

Small detail on that number: we get **66048** here, but on `vllm/vllm-openai-rocm:v0.28.0` back in August the same model gave **65792**. Your #4868 description mentions the estimate sometimes needing an extra 256 B depending on Triton version and target, which would account for the difference — same bug, two faces, rather than two bugs.

One thing I did not expect to see, and which supports what you said about point 3:

```
[aiter] [module_rmsnorm_quant] prebuilt .so targets ['gfx942', 'gfx950']
        but not the running arch gfx1201; rebuilding for gfx1201
[aiter] finish build [module_rmsnorm_quant], cost 30.6s
```

aiter notices the missing device code and rebuilds for gfx1201 by itself. So the 0-of-123 count is a designed fallback rather than a broken state, which is what you told us. The visible cost is about 30 s added to first start on this arch.

Both problems are fixed in main, and both are present in what ships today. Whether that is worth a refreshed image is your call and not something I have an opinion on — I'm only closing the loop on the verification, since it looked like nobody had run it on gfx1201 hardware yet. Still no objection to closing this.

