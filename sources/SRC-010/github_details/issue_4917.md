# [Issue #4917] [Bug] Prefix-cache KV is not invalidated by /update_weights: hot weight update silently reuses stale KV (wrong outputs, cached_tokens still reported)

source: https://github.com/InternLM/lmdeploy/issues/4917
state: closed | updated: 2026-08-31T03:14:27Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

Hot model-weight updates via `POST /update_weights` (or `update_weights_from_distributed`)
swap the weights **in place without invalidating the prefix cache**. The prefix-cache
trie and block allocator are never touched, and the cache identity has no
weights-generation/epoch component, so:

* any request whose prompt prefix was cached **before** the update reuses KV computed
  with the **old weights**, while the suffix is decoded with the **new weights**;
* the output is silently wrong — there is no error, assert, or warning, and
  `usage.prompt_tokens_details.cached_tokens` keeps reporting the stale prefix as a
  legitimate hit;
* for RLHF-style flows (the main use case of `/update_weights`, see
  `docs/en/advance/update_weights.md`) this silently corrupts generated rollouts.

The documented safe sequence (offload the KV cache first via `/sleep` with tags
`weights`,`kv_cache`) is **not enforced** anywhere — `update_weights` succeeds while the
engine is serving with a warm prefix cache.

Root-cause chain:

1. `lmdeploy/serve/openai/endpoints/management.py:53-59` — `POST /update_weights`; the
   only dependency is `validate_json_request` (a content-type check); no auth, no check
   that the engine is in a cache-free state.
2. `lmdeploy/pytorch/engine/model_agent/agent.py:1385-1462` — `update_params()` calls
   `m.load_weights(iter(w))` on the live model and ends with `torch.cuda.empty_cache()`.
   Nothing in the scheduler / `BlockTrie` / `LogicalAllocator` / cache engine is
   invalidated (verified by grep: `paging/` and `cache_engine.py` contain no reference
   to `update_params`).
3. `lmdeploy/pytorch/paging/block_trie/trie.py:192-206` — block identity =
   `(adapter_name root, token ids, multimodal spans)`; no weights-generation component,
   so a cached prefix is indistinguishable before/after the swap.

Secondary observation on the same endpoint (also reproducible): the endpoint currently
returns HTTP 500 for every legitimate client flow (mp executor: `Not Implemented`;
torch ≥ 2.7 `serialize_state_dict()`/`reduce_tensor` layout: `IndexError` at
`agent.py:1392`; ray + separate client process: `AuthenticationError`). Fixing those
transport issues (required anyway for RLHF) will immediately expose the stale-KV defect
below — so it should be fixed together ("fix first, then enable").

### Reproduction

Requirements: Linux x86_64, NVIDIA GPU (≥ 20 GB VRAM; verified on RTX 3090), CUDA 12.x+
toolkit, Python ≥ 3.10 with `torch` (CUDA), `transformers`, and lmdeploy from `main`
(commit `2928f477` or later; `pip install "lmdeploy @ git+https://github.com/InternLM/lmdeploy.git"`).
Any small causal LM works, e.g. `Qwen/Qwen2.5-0.5B-Instruct` (set `MODEL` below).

Run the following single file (`f1_stale_kv_poc.py`) on one GPU:

```python
#!/usr/bin/env python3
"""PoC: hot /update_weights leaves the prefix cache stale -> old-weight KV reused.

Protocol (all greedy decoding, temperature 0):
  run1: tokens T + ORIGINAL weights, cold    -> O1
  run2: tokens T + ORIGINAL weights, warm     -> O2  (cache hit: hit-delta > 0)
  update_params(): k_proj of layers 12..17 sign-flipped, NO cache invalidation
  run3: tokens T + NEW weights, warm          -> O3  (hits OLD-weight KV!)
  block_trie.evict(all)                              (force recompute)
  run4: tokens T + NEW weights, cold          -> O4
  run5: tokens T + NEW weights, warm          -> O5  (hits NEW-weight KV)

Verdict: O3 != O5 while O4 == O5 and O1 == O2 -> the block matched by run3 still
held pre-update KV (stale lineage) and differs from what the new weights compute.
O1 != O4 additionally proves the weight swap itself took effect.
"""
import base64
import pickle
import sys
import time

import torch

from lmdeploy.messages import GenerationConfig, PytorchEngineConfig
from lmdeploy.pytorch.engine import Engine
from lmdeploy.serve.openai.protocol import UpdateParamsRequest

MODEL = '/path/to/Qwen2.5-0.5B-Instruct'   # <- set your model path/repo id
FRAGMENT = (
    'The quick brown fox jumps over the lazy dog while the sun sets behind the '
    'mountain range. Every morning the village blacksmith forges horseshoes for '
    'the farmers who bring their wagons from the distant valley. The river flows '
    'gently past the old mill, where the waterwheel turns slowly and the miller '
    'sings an ancient tune he learned from his grandfather. '
)


def _identity_tensor(tensor, a0, a1, a2, a3, a4, device):
    """Picklable payload function: agent._construct calls func(*args) and replaces
    args[6] with the current CUDA device id (agent.py:1392)."""
    return tensor


def make_prompt_ids() -> list[int]:
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(MODEL)
    return tok.encode((FRAGMENT * 12)[:4600])


def perturb_weights() -> str:
    """Serialized payload in the format update_params deserializes:
    base64(pickle([(name, (func, args)), ...])) with args[6] the device slot."""
    from transformers import AutoModelForCausalLM
    torch.manual_seed(0)
    model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.float16)
    flipped = {}
    for name, w in model.state_dict().items():
        if any(f'model.layers.{l}.self_attn.k_proj.weight' == name for l in range(12, 18)):
            flipped[name] = (-w).contiguous().cuda()
    items = [(k, (_identity_tensor, [v, None, None, None, None, None, None]))
             for k, v in flipped.items()]
    return base64.b64encode(pickle.dumps(items)).decode('utf-8')


def run(engine, instance, session: int, input_ids, max_new: int = 20) -> list[int]:
    gen = GenerationConfig(temperature=0.0, top_k=1, max_new_tokens=max_new, ignore_eos=True)
    toks: list[int] = []
    for out in instance.stream_infer(session, input_ids, gen_config=gen):
        if out.status.value != 0:
            print(f'  !! stream_infer status={out.status}')
        toks.extend(int(t) for t in out.token_ids)
    return toks


def first_diff(a, b):
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return -1 if len(a) == len(b) else min(len(a), len(b))


def main() -> None:
    engine_cfg = PytorchEngineConfig(
        tp=1, dtype='float16', enable_prefix_caching=True,
        cache_max_entry_count=0.90, session_len=8192,
    )
    engine = Engine(MODEL, engine_config=engine_cfg)
    engine.start()
    instance = engine.create_instance()
    input_ids = make_prompt_ids()
    print(f'  prompt tokens: {len(input_ids)}')

    def run_and_stats(session):
        toks = run(engine, instance, session, input_ids)
        trie = engine.scheduler.block_trie
        return toks, int(trie.stats.num_hit_tokens), int(trie.stats.num_query_tokens)

    print('run1 (cold, original)...')
    o1, h1, _ = run_and_stats(1)
    time.sleep(0.2)
    print('run2 (warm, original)...')
    o2, h2, _ = run_and_stats(2)
    hit_delta = h2 - h1
    print(f'  cache-hit delta on warm run (orig weights): {hit_delta}')
    if hit_delta < 256:
        print('  !! prefix cache did not materialize - aborting')
        engine.close(); sys.exit(3)

    print('update_params (perturbed weights, NO cache invalidation)...')
    engine.executor.model_agent.update_params(
        UpdateParamsRequest(serialized_named_tensors=perturb_weights(), finished=True))
    torch.cuda.synchronize()
    time.sleep(1)

    print('run3 (warm after update)...')
    o3, _, _ = run_and_stats(3)
    print('evict all trie KV...')
    n = engine.scheduler.block_trie.evict(1 << 30)
    print(f'  evicted {n} blocks')
    print('run4 (cold after update)...')
    o4, _, _ = run_and_stats(4)
    print('run5 (warm after update)...')
    o5, _, _ = run_and_stats(5)

    print()
    print('== comparisons (greedy decode) ==')
    print('  O1 vs O2 (orig warm sanity):       first_diff=%s' % first_diff(o1, o2))
    print('  O1 vs O4 (orig vs new cold):       first_diff=%s   <-- update took effect' % first_diff(o1, o4))
    print('  O3 vs O5 (warm old-KV vs new-KV):  first_diff=%s   <-- stale-KV verdict' % first_diff(o3, o5))
    print('  O4 vs O5 (cold vs warm, new-KV):   first_diff=%s   <-- prefix-cache noise control' % first_diff(o4, o5))
    print(f'  O3: {o3[:12]}')
    print(f'  O4: {o4[:12]}')
    print(f'  O5: {o5[:12]}')

    if o1 == o2 and o4 == o5 and o3 != o5 and o1 != o4:
        print('RESULT: VULNERABLE - stale prefix-cache KV reused after weight update.')
    else:
        print('RESULT: not reproduced in this environment.')
    engine.close()


if __name__ == '__main__':
    main()
```

Observed output on the verification host (RTX 3090, lmdeploy @ `2928f477`, prompt = 853
tokens):

```text
  prompt tokens: 853
run1 (cold, original)...
run2 (warm, original)...
  cache-hit delta on warm run (orig weights): 832
update_params (perturbed weights, NO cache invalidation)...
run3 (warm after update)...
evict all trie KV...
  evicted 13 blocks
run4 (cold after update)...
run5 (warm after update)...
== comparisons (greedy decode) ==
  O1 vs O2 (orig warm sanity):       first_diff=-1
  O1 vs O4 (orig vs new cold):       first_diff=0   <-- update took effect
  O3 vs O5 (warm old-KV vs new-KV):  first_diff=1   <-- stale-KV verdict
  O4 vs O5 (cold vs warm, new-KV):   first_diff=-1  <-- prefix-cache noise control
  O3: [16, 16, 16, 16, 279, 1380, ...]
  O4: [16, 13, 576, 3974, 1380, ...]
  O5: [16, 13, 576, 3974, 1380, ...]
RESULT: VULNERABLE - stale prefix-cache KV reused after weight update.
```

HTTP-level confirmation (same host, `lmdeploy serve api_server ... --backend pytorch
--enable-prefix-caching`): request 1 → `cached_tokens=0`; request 2 → `cached_tokens=832`;
after `POST /update_weights` with the same payload, request 3 still reports
`cached_tokens=832` while its output is the stale-KV mixture.

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
```

### Error traceback

```Shell
The defect itself is **silent** (no exception — that is the point). The token-level
divergences above are the "traceback". For completeness, the secondary transport defects
of the same endpoint produce these HTTP 500s when using the documented client flow
(`serialize_state_dict`, ray backend) — they are reported here so the fix lands together:


# --distributed-executor-backend mp  :
Exception: Not Implemented.            # engine/executor/base.py:117 update_params

# --distributed-executor-backend ray  , torch >= 2.7, separate client process:
IndexError: list assignment index out of range   # agent.py:1392  _construct args[6]
multiprocessing.context.AuthenticationError: digest received was wrong  # resource_sharer
```

## 评论 (1)

### lvhan028 · 2026-08-31

In our RL workflow, the controller explicitly invokes the `/sleep` endpoint prior to `/update_weights`. This ensures that all weights are offloaded from GPU to CPU and the KV cache is fully destroyed. Consequently, when `/update_weights` is called, the KV cache is guaranteed to be in an uninitialized state, which aligns perfectly with the intended behavior.
