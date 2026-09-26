# [Issue #3034] [BUG][Fuzzer][ice-on-invalid-code] `T.rng_rand`/`T.rng_rand_float` with no preceding `T.rng_init` emit `curand…(&)` and crash nvcc, instead of a clean "init required" error

source: https://github.com/tile-ai/tilelang/issues/3034
state: open | updated: 2026-09-17T10:15:47Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported.

### What version of TileLang are you using?

0.1.13

### System information

- Installed via pip into a clean venv
- Python 3.13
- `tilelang` 0.1.13, `torch` 2.8.0
- GPU: NVIDIA L40S (sm_89); CUDA 12.x, `nvcc` invoked with `-arch=sm_89`

### Problem description

Calling `T.rng_rand()` (or `T.rng_rand_float()`) in a kernel that does **not** also call `T.rng_init()` produces a kernel that fails to compile with an opaque nvcc error, instead of a clean TileLang-level message that `rng_init` is required first.

The CUDA codegen for `rng_rand` emits `curand(&<state>)`, where `<state>` is the name of the curand state variable. That name is only ever set when an `rng_init` call is codegen'd; with no `rng_init` present it stays the empty string, so the emitted line is literally `curand(&)` — a bare `&` with no operand — and nvcc aborts:

```
/tmp/.../tvm_kernels.cu(20): error: expected an expression
    B[((int)threadIdx.x)] = curand(&);
                                    ^
```

The same kernel *with* an `T.rng_init(...)` compiles and codegens correctly (control below), so the failure is specific to the missing-init case.

Not a regression — see Provenance.

### Reproducible example code

```python
import tilelang
import tilelang.language as T


def build(with_init):

    @T.prim_func
    def main(B: T.Tensor((128,), "uint32")):
        with T.Kernel(1, threads=128) as _:
            tx = T.get_thread_binding()
            if with_init:
                T.rng_init(0)        # -> curand_init(...); state var declared
            B[tx] = T.rng_rand()     # -> curand(&<state>)

    return main


# CONTROL: identical kernel WITH T.rng_init -> compiles fine
tilelang.compile(build(True), target="cuda")     # OK
#   emitted: curandStatePhilox4_32_10_t __random_generator_state;
#            curand_init(0, ((int)threadIdx.x), 0, &__random_generator_state);
#            B[((int)threadIdx.x)] = curand(&__random_generator_state);

# TRIGGER: identical kernel WITHOUT T.rng_init -> nvcc "expected an expression"
tilelang.compile(build(False), target="cuda")     # RuntimeError
#   emitted: B[((int)threadIdx.x)] = curand(&);   <-- bare '&', no operand
```

`T.rng_rand_float()` (which emits `curand_uniform(&<state>)` etc.) fails identically for the same reason.

### Traceback

```pytb
Traceback (most recent call last):
  ...
    raise RuntimeError(msg)
RuntimeError: ...
Compilation error:
/tmp/.../tvm_kernels.cu(20): error: expected an expression
    B[((int)threadIdx.x)] = curand(&);
                                    ^
1 error detected in the compilation of "/tmp/.../tvm_kernels.cu".
```

### Expected behavior

A `T.rng_rand` / `T.rng_rand_float` used without a preceding `T.rng_init` reads an uninitialized (in fact, never-declared) curand state, so there is no valid value to produce. The natural expectation is a clear error at build time — e.g. "`rng_rand` used without a preceding `rng_init`" — rather than emitting `curand(&)` and surfacing an opaque `expected an expression` from nvcc. The frontend already asserts other RNG preconditions eagerly (`random.py` asserts the `generator`/`bit`/`dist` values), so an early check here would be consistent with that.

### Additional context

**Root cause.** The CUDA codegen prints the curand state operand from a member string that is only assigned inside the `rng_init` branch, with no check that an `rng_init` was seen for the current function; with no `rng_init` the member stays empty and the emit collapses to `curand(&)`.

<details>
<summary>Where the empty state name comes from (pinned to v0.1.13)</summary>

`rng_rand` emits [`curand(&" << this->curand_random_generator_state << ")"`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L4797-L4799) and `rng_rand_float` [does the same](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L4801-L4807). `curand_random_generator_state` is a plain [`std::string` member](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.h#L92-L93) that defaults to empty and is set only in the [`rng_init` branch](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L4781-L4788). The per-function pre-scan in `AddFunction` that declares the state variables walks the body [only for `rng_init` calls](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L6143-L6158); when the body has `rng_rand` but no `rng_init`, nothing is declared and the member stays empty, so the emit becomes `curand(&)`. Nothing in the [frontend `rng_rand`/`rng_rand_float`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/cuda/language/random.py#L42-L50) requires or checks for a prior `rng_init` either.

</details>

**Impact.** A user who forgets (or mis-scopes) the `rng_init` call gets no TileLang-level guidance — the kernel is accepted through the whole frontend and lowering pipeline, then dies deep in `nvcc` with `expected an expression` on a machine-generated `.cu` line the user never wrote. The failure surfaces far from its cause (a missing frontend call), so the message is actively misleading rather than merely unhelpful; diagnosing it requires reading the emitted CUDA. It is a build-time failure, not a silent miscompile, so no wrong results reach silicon — but it costs debugging time on a precondition the compiler already knows how to detect.

**Suggested fix.** Add a frontend guard that a function using `rng_rand`/`rng_rand_float` contains at least one `rng_init`, raising a clear error otherwise. Alternatively the codegen could `ICHECK(!curand_random_generator_state.empty())` at the `rng_rand`/`rng_rand_float` emit sites (the `rng_init` branch already `ICHECK`s its own pre-scan registration), turning the silent `curand(&)` into an actionable message.

**Provenance.** Introduced with the RNG feature in [#1461](https://github.com/tile-ai/tilelang/pull/1461) ("[Language] Adds a random number generation capability through curand_kernel", merged 2025-12-18): as first written, `rng_rand` emitted `curand(&" << this->curand_philox_state << ")"` where the state member is set only in the `rng_init` branch — the same missing-precondition gap. [#2297](https://github.com/tile-ai/tilelang/pull/2297) (2026-06-02) only relocated the code into a backend namespace and renamed the member to `curand_random_generator_state`; it did not introduce or fix the gap. The pattern has therefore shipped since RNG first landed; not a regression.

**Dedup.** I searched the open and closed tracker and found no existing report of this defect. The nearest reports are a different RNG bug — [#2625](https://github.com/tile-ai/tilelang/issues/2625) (`rng_init`'s default `seq` is x-dim-only; a silent wrong-value bug in `rng_init`, not a compile failure) — and a same-shaped-but-unrelated emit — [#2667](https://github.com/tile-ai/tilelang/issues/2667) (`atomic_min`/`atomic_max` `return_prev=True` emits `int prev = ;`); both have a different root and site.

**Reach.** Triggering requires calling `rng_rand`/`rng_rand_float` with no `rng_init` anywhere in the function. Every RNG site shipped at 0.1.13 pairs them, so no shipped example or test exercises the no-init path (which is why CI does not catch it). **Verified by running the shipped example on 0.1.13 (L40S, sm_89):** `examples/rand/rand_uint.py` — where `T.rng_init` is on L18 and `T.rng_rand()` on L23 of the same kernel — runs to completion (exit 0; all three configs `(1024,42)/(512,123)/(128,0)` pass its torch-vs-triton `assert_close`). It **dodges the bug because it always calls `T.rng_init` before `T.rng_rand`**. The RNG tests likewise precede every producer with a `T.rng_init` in the same kernel: `testing/python/language/test_tilelang_language_rand.py` (including `test_rand_init_in_split_guard`, which puts the init in a runtime guard — the pre-scan still registers it), and `testing/python/language/test_tilelang_cast_rounding.py` (`T.rng_init(42)` L473 before `T.rng_rand()` L475). No shipped site hits the no-init path.

**Generalization / boundary (all cells run on 0.1.13, L40S, sm_89).**

- **SOURCE-level root:** `CodeGenTileLangCUDA::VisitExpr_` in `src/cuda/codegen/codegen_cuda.cc`. The `curand_random_generator_state` `std::string` member is assigned *only* in the `rng_init` branch ([L4787](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L4787)) and read unconditionally by the two producer branches ([L4799](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L4799), [L4806](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L4806)), with no non-empty guard. The `AddFunction` pre-scan ([L6143-L6158](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/src/cuda/codegen/codegen_cuda.cc#L6143-L6158)) only registers `rng_init` calls, so absent any init the member stays empty and every producer collapses to `curand…(&)`.
- **OPERATOR-level root:** the curand *producer* intrinsics that consume the shared state member — `tl.rng_rand` and the four `tl.rng_rand_float` shapes.

| axis | cell tested | result | same-root? |
|---|---|---|---|
| related-operator | `rng_rand_float()` (uint→f32 uniform), no init | `curand_uniform(&);` → nvcc `expected an expression` | **same root** |
| related-operator | `rng_rand_float(bit=64)`, no init | `curand_uniform_double(&);` → same nvcc error | **same root** |
| related-operator | `rng_rand_float(dist="normal")`, no init | `curand_normal(&);` → same nvcc error | **same root** |
| related-operator | `rng_rand_float(bit=64, dist="normal")`, no init | `curand_normal_double(&);` → same nvcc error | **same root** |
| related-source | `rng_init` alone, no producer | compiles OK | n/a (no producer reads the member) |
| related-source (boundary) | `rng_init` inside runtime guard `if d!=0:` then top-level `rng_rand` | compiles OK — pre-scan is `PostOrderVisit`, not flow-sensitive | boundary: crash needs *total absence* of `rng_init`, not scope/branch mismatch |
| similar-logic | any other codegen intrinsic reading a `std::string` member set in a sibling branch | none exist — `curand_random_generator_state[_type]` are the only such members in `codegen_cuda.h` (L92-93) | class confined to RNG |
| related-type | `generator` knob (Philox/MRG32k3a/XORWOW) | does not apply — the generator name is only consumed inside `rng_init`, which is absent in the trigger; the empty-state emit is generator-independent | n/a |

All five producer shapes (`rng_rand` + 4 × `rng_rand_float`) share one root; the fix (frontend "`rng_init` required" guard, or an `ICHECK(!curand_random_generator_state.empty())` at the producer emit sites) covers the whole class. The nearest same-*shape* emit, `atomic_min/max` `return_prev=True` emitting `int prev = ;` ([#2667](https://github.com/tile-ai/tilelang/issues/2667)), is a **distinct-adjacent bug (not filed here)** — different site (atomic branch ~L4839) and a different empty-operand mechanism. No new bug was found while sweeping.

## 评论 (3)

### jjppp · 2026-08-31

I think there's a gap here, as cuda connects `curand_init` and `curand` with an explicit `state` variable, while tilelang implicitly pairs each `rng_rand` to the last occurrence of `rng_init`, **regardless of scoping**.
The situation would be much better if the semantics of `rng_init` and `rng_random` can be further clarified, either via returning a state variable, or stating that `rng_random` should be bound to the first visible `rng_init` **invoked in its scope**.

Some other notes on the documentation: `rng_init` claims to return an explicit state, yet it does not.
https://github.com/tile-ai/tilelang/blob/2fb445bacd88d2e2d11fec606dbf0ebd944fcb22/tilelang/cuda/language/random.py#L23-L26

### 0z5a · 2026-09-17

I would like to take this and the other two.

### 0z5a · 2026-09-17

Planned scope:

1. make the `rng_init` API contract consistent with its actual hidden-state implementation,
2. reject `rng_rand` / `rng_rand_float` cleanly when no `rng_init` exists in the function,
3. make `rng_init(seq=None)` derive a unique default sequence across all launch dimensions,
4. add regression coverage for all three cases.

I'll keep the patch limited to the RNG frontend/codegen/tests. If you would prefer #2625 to be split from the state-lifecycle/API fixes, I can separate it.

The patch is up as #3239 (Fixes #2625, #3029, #3034). The PR description has the baseline-vs-patched reproducer output, an end-to-end stream-quality measurement (16/256 distinct per-thread streams before, 256/256 after), and the test results (8 failed/13 passed on baseline, 21 passed with the patch).

---

For #3029 specifically: my current interpretation is to preserve TileLang's existing hidden RNG-state model and make `rng_init` explicitly side-effect-only, rather than introducing a new public state-handle API. `rng_rand` / `rng_rand_float` do not consume an explicit handle today. If an explicit state handle is the intended API direction, please let me know before I lock this in.

