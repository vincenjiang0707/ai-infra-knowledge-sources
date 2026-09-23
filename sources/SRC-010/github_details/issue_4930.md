# [Issue #4930] [Bug] Mooncake external KV keys omit KV format and weights lineage, with no default tenant isolation

source: https://github.com/InternLM/lmdeploy/issues/4930
state: open | updated: 2026-09-03T13:19:11Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

The Mooncake Store KV connector (introduced by #4903) builds external KV-cache
keys from **only**
`{optional cache_prefix, model_name, tp_rank-derived shard id, fixed @group:0, sha256(schema|prev|block_size|tokens|adapter_name)}`.
The key therefore omits identity that can change the meaning or ownership of the
stored KV bytes:

1. **KV-cache dtype / quant_policy is not part of the key.**
   `MooncakeStoreKeyMetadata` (`kv_connector/mooncake/store/data.py:157-172`) has no
   dtype/quant field, and `_get_request_block_hashes`
   (`kv_connector/mooncake/store/scheduler.py:177-192`) feeds only
   `extra_identity = request.adapter_name or ''` into `build_prefix_block_hashes`
   (`data.py:86-160`). A fp16 producer and an fp8/int4 producer with the same
   model/tokens produce **byte-identical store keys** (`data.py:192-198`), so
   `batch_is_exist` (`worker.py:422-447`) reports a positive hit for a different
   format. The subsequent transfer may fail closed if the producer and consumer
   block sizes differ, but the lookup and `cached_tokens` accounting still report
   a hit and incur unnecessary transfer work. Adapter identity has the same
   limitation: only the adapter name, not its weights, participates in the hash.

2. **Weights version / generation is not part of the key.**
   Keys are identical across engine restarts and across weight revisions. If two
   same-dtype deployments (or one deployment before and after a weight update)
   share the store, KV written under the old weights is advertised to the new
   weights. Because the layout can be byte-compatible, the load can succeed
   silently and the new model can consume stale KV.

3. **No tenant isolation by default.**
   `cache_prefix` defaults to `''` (`kv_connector/factory.py:39-41`,
   `store/worker.py:107-113`) and `model_name` defaults to the model-path basename.
   Two deployments sharing one Mooncake cluster with the same model name and
   default prefix therefore share the key space; `@group:0` is hard-coded
   (`data.py:196`). A deployment can opt into a distinct prefix, but this is not
   required or documented by the connector.

Consequences are deployment-dependent. The key collisions and positive existence
lookups are deterministic. The strongest correctness case is same-dtype,
different-weight KV reuse, which can be fully silent. Cross-dtype loads commonly
hit a store size mismatch and fall back to local recomputation, but still produce
false hit accounting and wasted transfer; silent corruption depends on the store
backend accepting the mismatched byte layout. Cross-tenant reuse requires a shared
store and colliding model/prefix configuration, but is not isolated by default.

Root-cause chain (see code references above): key built from token blocks plus the
adapter name only -> no KV format or weights-era dimension, and no required tenant
namespace.

Why this is not merely an undocumented operator convention: the Mooncake connector
has no documentation requiring a homogeneous immutable-weight namespace or a
non-empty `cache_prefix`. The weight-update documentation describes offloading the
local KV cache, but the connector has no store-side delete/invalidation operation;
closing the store client does not change existing remote entries. Quantized KV is a
valid PyTorch configuration and is not rejected when the connector is enabled.

The KV-head shard-schema mismatch is intentionally excluded here and should be
tracked as the sibling F8 issue.

### Impact

- **Type**: external-KV-store identity omission / stale-lineage reuse; cross-tier
  coherence violation between the local trie identity and the external store namespace.
- **Who is impacted**: any deployment using the Mooncake `kv_connector` (PD
  disaggregation / shared external KV), specifically:
  1. deployments reusing one Mooncake cluster with different KV formats or model
     revisions/weights — especially the fully silent same-dtype case;
  2. deployments that update weights and then rely on persisted external KV;
  3. shared clusters using the default empty `cache_prefix` (model-dir basename as
     the only partition).
- **Affected versions**: the connector exists only on `main` since #4903 (2026-08-28);
  not in the 0.16.0 release wheel — this report targets the unreleased feature before
  wide adoption (the best time to fix the namespace).

### Suggested fix

1. Include the resolved KV-cache format (`dtype`/`quant_policy` and any auxiliary
   quantization layout) in the store namespace or key.
2. Include a model revision or weights epoch in the namespace; rotate it on every
   accepted weight update, or invalidate the external entries before serving again.
3. Require an explicit non-empty tenant namespace when a shared store is configured,
   or document and enforce a homogeneous single-tenant contract.
4. Consider binding LoRA identity to an adapter-weights fingerprint, not only the
   deployment-local name.

### Reproduction

Requirements: lmdeploy source from upstream `main` after #4903 (currently verified
at `d9888113`), Python >= 3.10 with numpy and torch (any build, **no GPU needed**;
the probe exercises the production key-builder path only).

```shell
pip install "lmdeploy @ git+https://github.com/InternLM/lmdeploy.git"   # post-#4903
# or: git clone https://github.com/InternLM/lmdeploy.git && cd lmdeploy && pip install -e .
```

Run the following single file (`mc_probe_f2.py`). It calls the **exact** production
key builders used by the connector at runtime
(`build_prefix_block_hashes`, `build_store_key`, `MooncakeStoreKeyMetadata`):

```python
#!/usr/bin/env python3
"""F2 probe: Mooncake KV-store key identity omissions.

Uses the REAL lmdeploy-pytorch connector modules
(kv_connector.mooncake.store.data) exactly as the worker uses them at runtime.

  A. Same tokens + same adapter, DIFFERENT KV-cache dtype configs
     (fp16 vs fp8 vs int4): identical store keys.
  B. Same tokens after a WEIGHT UPDATE / process restart: identical keys
     (no weights-generation dimension).
  C. Two deployments with default configs (empty cache_prefix, model_name =
     path basename): identical keyspace.
  E. Positive control: different tokens -> different keys.
"""
import sys

from lmdeploy.pytorch.kv_connector.mooncake.store.data import (
    MooncakeStoreKeyMetadata,
    build_prefix_block_hashes,
    build_store_key,
)

BLOCK_SIZE = 64
_fragment = [35, 468, 136, 812, 14112, 44, 1730, 850, 4751, 1234, 47, 8024, 47, 360, 1738,
             715, 420, 12912, 2230, 823, 776, 596, 3442, 3363, 4950, 613, 15462, 46, 22, 10, 44, 711]
PROMPT = _fragment * 12  # 384 tokens = 6 full blocks
assert len(PROMPT) % BLOCK_SIZE == 0

failures: list[str] = []


def check(label: str, cond: bool, detail: str) -> None:
    status = 'PASS' if cond else 'FAIL'
    print(f'  [{status}] {label}: {detail}')
    if not cond:
        failures.append(label)


def main() -> None:
    model_a = MooncakeStoreKeyMetadata(model_name='Qwen2.5-0.5B-Instruct',
                                       cache_prefix='', tp_size=8, block_size=BLOCK_SIZE)

    print('== A. dtype/quant config does not participate in keys ==')
    dtype_tags = ('fp16', 'fp8_e4m3', 'int4')
    hashes = {
        tag: build_prefix_block_hashes(PROMPT, BLOCK_SIZE, extra_identity='base')
        for tag in dtype_tags
    }
    same_bytes = len({h[-1] for h in hashes.values()}) == 1
    keys = {tag: build_store_key(model_a, 0, hashes[tag][2]) for tag in dtype_tags}
    same_key = len(set(keys.values())) == 1
    print(f'  block-hash identical across {list(dtype_tags)}: {same_bytes}')
    print(f'  store-key identical across {list(dtype_tags)}: {keys}')
    check('A: same store key across dtypes', same_bytes and same_key,
          'the store cannot distinguish fp16/fp8/int4 deployments; '
          'the lookup key is identical for the other format (transfer '
          'success depends on the store byte-size/layout checks)')

    print()
    print('== B. weight generation / restart epoch not in keys ==')
    h_run1 = build_prefix_block_hashes(PROMPT, BLOCK_SIZE, extra_identity='base')
    h_run2 = build_prefix_block_hashes(PROMPT, BLOCK_SIZE, extra_identity='base')
    k1 = build_store_key(model_a, 0, h_run1[2])
    k2 = build_store_key(model_a, 0, h_run2[2])
    check('B: keys stable across weight generations/restarts', k1 == k2,
          f'{k1} == {k2} -> the key cannot distinguish old and new weight '
          'lineage; persisted stale KV can be reused if the byte layout is '
          'accepted (identity unchanged by hot /update_weights)')

    print()
    print('== C. tenant partition defaults to empty ==')
    tenant1 = MooncakeStoreKeyMetadata(model_name='Qwen2.5-0.5B-Instruct',
                                       cache_prefix='', tp_size=8, block_size=BLOCK_SIZE)
    tenant2 = MooncakeStoreKeyMetadata(model_name='Qwen2.5-0.5B-Instruct',
                                       cache_prefix='', tp_size=8, block_size=BLOCK_SIZE)
    kt1 = build_store_key(tenant1, 3, h_run1[2])
    kt2 = build_store_key(tenant2, 3, h_run2[2])
    check('C: two tenants with default config share keyspace', kt1 == kt2,
          f'{kt1} == {kt2} -> no tenant partition is encoded; deployments '
          'sharing a Mooncake cluster can collide under the same model-dir '
          'basename')

    print()
    print('== E. positive control: different tokens -> different keys ==')
    other = build_prefix_block_hashes([1, 2, 3, 4] * (BLOCK_SIZE // 4 * 4), BLOCK_SIZE,
                                      extra_identity='base')
    ko = build_store_key(model_a, 0, other[2])
    check('E: different content yields different key', ko != keys['fp16'],
          f'{ko} != {keys["fp16"]}')

    print()
    if failures:
        print('RESULT: %d assertions FAILED (unexpected) -> %s' % (len(failures), failures))
        sys.exit(1)
    print('RESULT: all assertions hold -> key identity omissions A/B/C confirmed (E sanity)')
    sys.exit(0)


if __name__ == '__main__':
    main()
```

Run and expected output (observed on the verification host):

```text
$ python3 mc_probe_f2.py
== A. dtype/quant config does not participate in keys ==
  block-hash identical across ['fp16', 'fp8_e4m3', 'int4']: True
  store-key identical across ['fp16', 'fp8_e4m3', 'int4']: {'fp16': 'Qwen2.5-0.5B-Instruct@tp_rank:0@group:0@e94120f79296e8af266366a8ac6dcc18b8d8171f87e6f405f6a6f4e22324fe8e', 'fp8_e4m3': 'Qwen2.5-0.5B-Instruct@tp_rank:0@group:0@e94120f79296e8af266366a8ac6dcc18b8d8171f87e6f405f6a6f4e22324fe8e', 'int4': 'Qwen2.5-0.5B-Instruct@tp_rank:0@group:0@e94120f79296e8af266366a8ac6dcc18b8d8171f87e6f405f6a6f4e22324fe8e'}
  [PASS] A: same store key across dtypes: the store cannot distinguish fp16/fp8/int4 deployments; the lookup key is identical for the other format (transfer success depends on the store byte-size/layout checks)
== B. weight generation / restart epoch not in keys ==
  [PASS] B: keys stable across weight generations/restarts: ...@e94120f7... == ...@e94120f7... -> the key cannot distinguish old and new weight lineage; persisted stale KV can be reused if the byte layout is accepted (identity unchanged by hot /update_weights)
== C. tenant partition defaults to empty ==
  [PASS] C: two tenants with default config share keyspace: ...@tp_rank:3@...@e94120f7... == ...@tp_rank:3@...@e94120f7... -> no tenant partition is encoded; deployments sharing a Mooncake cluster can collide under the same model-dir basename
== E. positive control: different tokens -> different keys ==
  [PASS] E: different content yields different key: ...@8e4e2fb3... != ...@e94120f7...
RESULT: all assertions hold -> key identity omissions A/B/C confirmed (E sanity)
```

### Environment

```Shell
sys.platform: linux
Python: 3.12.9 | packaged by Anaconda, Inc. | (main, Feb  6 2025, 18:56:27) [GCC 11.2.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3,4,5,6,7: NVIDIA GeForce RTX 3090
CUDA_HOME: /usr
NVCC: Cuda compilation tools, release 13.0, V13.0.48
GCC: gcc (Ubuntu 12.5.0-8ubuntu2~20~ppa3) 12.5.0
PyTorch: 2.12.1+cu130
PyTorch compiling details: PyTorch built with:
  - GCC 13.3
  - C++ Version: 202002
  - Intel(R) oneAPI Math Kernel Library Version 2024.2-Product Build 20240605 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v3.11.2 (Git Hash 03c022d3ffdcee958cfacbe720048e725fdf644c)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: AVX2
  - CUDA Runtime 13.0
  - NVCC architecture flags: -gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_100,code=sm_100;-gencode;arch=compute_120,code=sm_120
  - CuDNN 92.0  (built against CUDA 13.2)
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=7269437d655783a26cba32aa88195b741ff496aa, CUDA_FLAGS= -DLIBCUDACXX_ENABLE_SIMPLIFIED_COMPLEX_OPERATIONS -Xfatbin -compress-all -DONNX_NAMESPACE=onnx_torch -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_90,code=sm_90 -gencode arch=compute_100,code=sm_100 -gencode arch=compute_120,code=sm_120 -Xcudafe --diag_suppress=cc_clobber_ignored,--diag_suppress=field_without_dll_interface,--diag_suppress=base_class_has_different_dll_interface,--diag_suppress=dll_interface_conflict_none_assumed,--diag_suppress=dll_interface_conflict_dllexport_assumed,--diag_suppress=bad_friend_decl --expt-relaxed-constexpr --expt-extended-lambda -Xfatbin -compress-all --threads 2 -compress-mode=size -Wno-deprecated-gpu-targets --expt-extended-lambda -DCUB_WRAPPED_NAMESPACE=at_cuda_detail -DDISABLE_CUSPARSE_DEPRECATED -DCUDA_HAS_FP16=1 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -DC10_NODEPRECATED, CUDA_VERSION=13.0, CUDNN_VERSION=9.20.0, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_MSLK -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.12.1, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF, 

TorchVision: 0.27.1+cu130
LMDeploy: 0.16.0+
transformers: 5.16.1
fastapi: 0.141.1
pydantic: 2.13.5
triton: 3.7.1
NVIDIA Topology: 
	GPU0	GPU1	GPU2	GPU3	GPU4	GPU5	GPU6	GPU7	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	NODE	NODE	NODE	SYS	SYS	SYS	SYS	0-63,128-191	0		N/A
GPU1	NODE	 X 	NODE	NODE	SYS	SYS	SYS	SYS	0-63,128-191	0		N/A
GPU2	NODE	NODE	 X 	NODE	SYS	SYS	SYS	SYS	0-63,128-191	0		N/A
GPU3	NODE	NODE	NODE	 X 	SYS	SYS	SYS	SYS	0-63,128-191	0		N/A
GPU4	SYS	SYS	SYS	SYS	 X 	NODE	NODE	NODE	64-127,192-255	1		N/A
GPU5	SYS	SYS	SYS	SYS	NODE	 X 	NODE	NODE	64-127,192-255	1		N/A
GPU6	SYS	SYS	SYS	SYS	NODE	NODE	 X 	NODE	64-127,192-255	1		N/A
GPU7	SYS	SYS	SYS	SYS	NODE	NODE	NODE	 X 	64-127,192-255	1		N/A

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

Additional environment notes: the probe needs no GPU and does not connect to a
Mooncake cluster; it only executes the production key-builder path. The model name
in the probe is illustrative — any model name reproduces the result.
```

### Error traceback

```Shell
None. The key collision is silent by construction: `batch_is_exist` returns a positive
state for colliding keys. A cross-dtype `get` may fail at the store size check and
fall back to local recompute; same-dtype/different-weight loads can succeed with no
signal. The probe output above is the evidence.
```

## 评论 (2)

### caikun-pjlab · 2026-09-03

Thank you for your detailed report and thorough analysis!

Currently, our recommended workaround for multi‑tenant isolation is to **use separate Mooncake clusters for different deployments**, or to explicitly set a **`cache_prefix`** at deployment time to distinguish namespaces. However, this approach does require careful configuration in production, and there is still a risk of misuse or key collisions if not properly set up.

Your proposed fix is very clear and constructive — incorporating the KV format (dtype/quant_policy) and weights lineage (e.g., revision) into the store key, along with requiring an explicit tenant namespace, would indeed greatly reduce the risk of key collisions at the root. We plan to improve this in a future release, specifically by:

- Including KV cache dtype/quant_policy information in the store key construction;
- Introducing a weights version or revision dimension to prevent accidental reuse of KV across different model weights;
- Considering or documenting a clearer configuration guideline for tenant isolation.

Thanks again for your valuable contribution. We will follow up on this fix in the upcoming iterations.

### wildoranges · 2026-09-03

hi @caikun-pjlab , thanks for the reply. I’ve opened a PR here: https://github.com/InternLM/lmdeploy/pull/4932
