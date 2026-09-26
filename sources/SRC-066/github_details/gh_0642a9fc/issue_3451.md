# [Issue #3451] [BUG] CuTe DSL TMEM allocator triggers internal struct.scalar pointer deprecation warnings

source: https://github.com/NVIDIA/cutlass/issues/3451
state: open | updated: 2026-09-23T05:20:32Z
labels: CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report
[
**Describe the bug**
Not high pri but im tyring to drop my deprecation warnings to 0 

Compiling a Blackwell CuTe DSL kernel through the public `cutlass.utils.TmemAllocator` API emits deprecation warnings from inside CuTe DSL:

```text
nvidia_cutlass_dsl/python_packages/cutlass/cute/core.py:5811: DeprecationWarning:
Use explicit `struct.scalar.ptr` for pointer instead.
```

The user kernel does not access `struct.scalar.value` directly. The warning stacks lead to CuTe DSL's own TMEM helpers:

- `cutlass/cute/arch/tmem.py::alloc_tmem` accesses `smem_ptr_to_write_address.value`
- `cutlass/cute/arch/tmem.py::retrieve_tmem_ptr` accesses `ptr_to_buffer_holding_addr.value`

Both values can be `struct.scalar` pointer wrappers, whose `.value` property is deprecated in favor of `.ptr`.

**Steps/Code to reproduce bug**

1. Compile a Blackwell CuTe DSL kernel that allocates TMEM with `cutlass.utils.TmemAllocator` and calls `retrieve_ptr()`.
2. Force compilation rather than loading a cached artifact and enable deprecation warnings:

```bash
CUTE_DSL_NO_CACHE=1 PYTHONWARNINGS=always::DeprecationWarning python kernel.py
```

The relevant warning stacks are:

```text
cutlass/utils/tmem_allocator.py:444 in then_block_1
  cute.arch.alloc_tmem(...)
cutlass/cute/arch/tmem.py:155 in alloc_tmem
  smem_ptr_to_write_address.value
cutlass/cute/core.py:5811 in value
  warnings.warn("Use explicit `struct.scalar.ptr` for pointer instead.")
```

and:

```text
cutlass/utils/tmem_allocator.py:480 in retrieve_ptr
  return cute.arch.retrieve_tmem_ptr(...)
cutlass/cute/arch/tmem.py:110 in retrieve_tmem_ptr
  ptr_to_buffer_holding_addr.value
cutlass/cute/core.py:5811 in value
  warnings.warn("Use explicit `struct.scalar.ptr` for pointer instead.")
```

The same internal `.value` accesses are present in the published 4.7.0 wheel and on `main`:

- https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/cute/arch/tmem.py#L100-L111
- https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/cute/arch/tmem.py#L151-L160
- https://github.com/NVIDIA/cutlass/blob/main/python/CuTeDSL/cutlass/cute/core.py#L5886-L5894

**Expected behavior**

Using the public TMEM allocator API should not trigger CuTe DSL's own pointer deprecation warnings. The internal TMEM helpers should extract the explicit pointer (`struct.scalar.ptr`) when passed a scalar pointer wrapper while continuing to support ordinary `Pointer` arguments.

**Environment details**

- Environment location: bare metal
- GPU: NVIDIA GB300
- Driver: 580.126.20
- CUDA toolkit: 13.1
- Architecture: aarch64
- Python: 3.13.12
- Observed with `nvidia-cutlass-dsl==4.6.0.dev0`
- Confirmed the same internal accesses remain in the published `nvidia-cutlass-dsl==4.7.0` wheel

**Additional context**

In one training workload, four identical warnings appear because two separately compiled backward kernels each allocate TMEM and retrieve its pointer. Capturing full warning stacks confirms all four warnings originate in the two CuTe DSL internal helper paths above, rather than direct use of the deprecated property by the user kernels.


## 评论 (2)

### brandon-yujie-sun · 2026-09-07

@LongshengDu 

### LongshengDu · 2026-09-23

The fix is included in v4.8 update, please check again using updated version.
