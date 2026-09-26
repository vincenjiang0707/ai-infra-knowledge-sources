# [Issue #2492] [FA4] Backward error on head_dim not divisible by 32 `'cute.copy' op expects pred to have compatible shape with: (1,(1)) but got actual predShape`

source: https://github.com/Dao-AILab/flash-attention/issues/2492
state: closed | updated: 2026-09-08T21:02:22Z
labels: 

## 正文

Hello, I was wondering whether the below is expected. On backward pass for FA4 for head_dim 104, it raises a shape mismatch error. This happened when trying to run Pixtral with a head dim non divisible by 32. This issue does NOT occur on FA2.

Repro:

```python
import torch
from flash_attn.cute import flash_attn_varlen_func
hd, nh = 104, 16  # any head_dim % 32 != 0 works  
cu = torch.tensor([0, 3600, 7200], device='cuda', dtype=torch.int32)
q = torch.randn(7200, nh, hd, device='cuda', dtype=torch.bfloat16, requires_grad=True)
k = torch.randn_like(q, requires_grad=True); v = torch.randn_like(q, requires_grad=True)
out, *_ = flash_attn_varlen_func(q, k, v, cu_seqlens_q=cu, cu_seqlens_k=cu, max_seqlen_q=3600, max_seqlen_k=3600, causal=False)
out.sum().backward()
```

Env: B200 , Torch 2.10+cu130. FA4 b10. Python 312

Error: `'cute.copy' op expects pred to have compatible shape with: (1,(1)) but got actual predShape: (1,(8,1))`

```
Traceback (most recent call last):
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/nvidia_cutlass_dsl/python_packages/cutlass/base_dsl/dsl.py", line 1088, in build_module
    module.operation.verify()
cutlass._mlir._mlir_libs._site_initialize.<locals>.MLIRError: Verification failed:
error: "copy(tOgO[None, m, None], tOrO[None, m, None])"("/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/flash_bwd_preprocess.py":303:16): 'cute.copy' op expects pred to have compatible shape with: (1,(1)) but got actual predShape: (1,(8,1))
 note: "copy(tOgO[None, m, None], tOrO[None, m, None])"("/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/flash_bwd_preprocess.py":303:16): see current operation: "cute.copy"(%1211, %1230, %1245, %1260) <{operandSegmentSizes = array<i32: 1, 1, 1, 1>}> : (!cute_nvgpu.atom.universal_copy<bf16, 128 b>, !cute.memref<bf16, gmem, align<16>, "((8,1),(1)):((1,0),(0))">, !cute.memref<bf16, rmem, align<16>, "((8,1),(1)):((1,0),(0))">, !cute.memref<i8, rmem, align<32>, "(1,(8,1)):(1,(0,1))">) -> ()

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/torch/_tensor.py", line 631, in backward
    torch.autograd.backward(
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/torch/autograd/__init__.py", line 381, in backward
    _engine_run_backward(
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/torch/autograd/graph.py", line 869, in _engine_run_backward
    return Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/torch/autograd/function.py", line 317, in apply
    return user_fn(self, *args)
           ^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 1935, in backward
    dq, dk, dv = _flash_attn_bwd(
                 ^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 1470, in _flash_attn_bwd
    _bwd_preprocess(
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 1091, in _bwd_preprocess
    _bwd_preprocess.compile_cache[compile_key] = _compile_bwd_preprocess(*compile_key)
                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/interface.py", line 1073, in _compile_bwd_preprocess
    return cute.compile(
           ^^^^^^^^^^^^^
  File "/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/nvidia_cutlass_dsl/python_packages/cutlass/base_dsl/dsl.py", line 1090, in build_module
    raise DSLRuntimeError("______ ICE IR Verification Failed ______", cause=e)
cutlass.base_dsl.common.DSLRuntimeError: DSLRuntimeError: ______ ICE IR Verification Failed ______
  Caused exception: Verification failed:
error: "copy(tOgO[None, m, None], tOrO[None, m, None])"("/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/flash_bwd_preprocess.py":303:16): 'cute.copy' op expects pred to have compatible shape with: (1,(1)) but got actual predShape: (1,(8,1))
 note: "copy(tOgO[None, m, None], tOrO[None, m, None])"("/root/miniconda3/envs/py3.12/lib/python3.12/site-packages/flash_attn/cute/flash_bwd_preprocess.py":303:16): see current operation: "cute.copy"(%1211, %1230, %1245, %1260) <{operandSegmentSizes = array<i32: 1, 1, 1, 1>}> : (!cute_nvgpu.atom.universal_copy<bf16, 128 b>, !cute.memref<bf16, gmem, align<16>, "((8,1),(1)):((1,0),(0))">, !cute.memref<bf16, rmem, align<16>, "((8,1),(1)):((1,0),(0))">, !cute.memref<i8, rmem, align<32>, "(1,(8,1)):(1,(0,1))">) -> ()
```

For potential solution, I had Claude help dig into this, so this may be incorrect.

```
Root cause (now confirmed with evidence, not speculation):                                                                                                                                                                                                                  
  - FlashAttentionBackwardPreprocess (in flash_bwd_preprocess.py) pads head_dim to a multiple of_32.                                                                                                                                                                          
  - When head_dim_v != head_dim_v_padded (i.e., head_dim not aligned to_32), it sets check_hdim_v_oob=True.                                                                                                                                                                   
  - That triggers predicate_k() (in utils.py:465) which builds a predicate with shape (1, CPY_M, CPY_K).                                                                                                                                                                      
  - But the universal_copy<bf16, 128 b> atom has sub-mode (8,1), and the cute.copy op's MLIR verifier expects a predicate whose nesting matches the atom. The predicate shape (1,(8,1)) doesn't match the required (1,(1)), and verification fails at compile time.           
  - Any head_dim aligned to 32 skips predicate_k entirely (tOpO = None) and works fine.

Upstream fix location: either flash_attn/cute/utils.py:predicate_k (build a predicate whose shape coalesces with the copy atom's CPY_Atom sub-mode), or flash_attn/cute/flash_bwd_preprocess.py:303 (flatten the copy slices so no predicate inference happens against the  
  nested atom). Most surgical fix is probably in predicate_k.
```

## 评论 (2)

### JasonCZH4 · 2026-04-26

same issue.
```
'cute.copy' op expects pred to have compatible shape with: (1,(1)) but got actual predShape: (1,(2,1))
```
Env: H20 , Torch 2.7+cu126. FA4 b10. Python 310

### lishunyao97 · 2026-06-05

Getting the same issue.
Env: FA4 b16, B200 (SM100), torch 2.11.0+cu130
```
error: 'cute.copy' op expects pred to have compatible shape with: (1,(3)) but got actual predShape: (1,(2,3))
  (flash_attn/cute/flash_bwd_preprocess.py:311)
  ... !cute.memref<i8, rmem, align<32>, "(1,(2,3)):(3,(0,1))"> ...
```
