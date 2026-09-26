# [Issue #3029] [BUG][Fuzzer][ice-on-valid-code] Binding `T.rng_init()`'s documented state handle to a variable emits `void state = ;` and nvcc rejects the kernel

source: https://github.com/tile-ai/tilelang/issues/3029
state: open | updated: 2026-09-17T10:13:57Z
labels: 

## 正文


### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported.

### What version of TileLang are you using?

0.1.13 (reproduced on 0.1.13).

### System information

TileLang 0.1.13; NVIDIA L40S (sm_89), CUDA 12.8. The defect is in the frontend `rng_init` return type + the generic C codegen of a `void`-typed variable binding, so it is not specific to one GPU.

### Problem description

`T.rng_init(...)` documents its return value as the RNG state handle (`Returns — state: PrimExpr — The random number generator state handle`). Capturing it the natural, documented way — `state = T.rng_init(seed)` — makes the kernel fail to compile: the emitted CUDA contains `void state = ;`, which nvcc rejects with `error: incomplete type "void" is not allowed`. The byte-for-byte identical kernel that *discards* the return value compiles and runs correctly (uniform values in `[0,1)`), so the RNG lowering itself is fine — only capturing the documented handle breaks it.

The abort happens the moment the binding exists, even if `state` is never read again and no random number is ever drawn.

### Reproducible example code

```python
import tilelang, tilelang.language as T
N = 256

# CRASHES: bind the rng_init state handle to a variable (the documented "Returns: state" usage)
@T.prim_func
def rng_bind(B: T.Tensor((N,), "float32")):
    with T.Kernel(1, threads=256) as bx:
        tx = T.get_thread_binding()
        state = T.rng_init(1234)                 # docstring: "Returns state: the RNG state handle"
        B[tx] = T.rng_rand_float(32, "uniform")

# CONTROL: identical kernel, rng_init result NOT bound -> compiles & runs, values in [0,1)
@T.prim_func
def rng_nobind(B: T.Tensor((N,), "float32")):
    with T.Kernel(1, threads=256) as bx:
        tx = T.get_thread_binding()
        T.rng_init(1234)                         # same call, return value discarded
        B[tx] = T.rng_rand_float(32, "uniform")

try:
    tilelang.compile(rng_bind, out_idx=[0])()
    print("bind:   compiled")
except Exception as e:
    print("bind:   CRASH", type(e).__name__)          # -> CRASH RuntimeError (nvcc: incomplete type "void")

b = tilelang.compile(rng_nobind, out_idx=[0])().cpu().numpy()
print("nobind: min", b.min(), "max", b.max())          # -> min ~0.004  max ~0.998 (uniform [0,1))
```

### Traceback

No Python-level traceback with a clean message — the failure is an nvcc compile error surfaced as a `RuntimeError` from `tilelang.contrib.nvcc.compile_cuda`.

<details><summary>Emitted CUDA (the malformed line) + nvcc error (0.1.13, sm_89)</summary>

```cpp
curandStatePhilox4_32_10_t __random_generator_state;
curand_init(1234, ((int)threadIdx.x), 0, &__random_generator_state);
void state = ;                                             // <- the bound handle; void-typed, empty init
B[((int)threadIdx.x)] = curand_uniform(&__random_generator_state);
```
```
tvm_kernels.cu(22): error: incomplete type "void" is not allowed
      void state = ;
tvm_kernels.cu(22): error: expected an expression
      void state = ;
2 errors detected in the compilation of "tvm_kernels.cu".
```

`rng_init` lowers to a `void`-typed intrinsic, so binding it produces a `void`-typed variable declaration with no initializer — `void state = ;` — which is doubly illegal (void has no storage, and the RHS is empty). The discard-the-result control never forms a binding, so this line is never emitted.
</details>

### Expected behavior

Either the kernel should compile — capturing the state handle the docstring's `Returns` section describes should be a legal, no-op-if-unused binding — or `rng_init` should not advertise a returnable handle it cannot actually hand back. The RNG codegen (`curand_init`/`curand_uniform`) is already present and correct (the discard control produces valid uniform values), so the value is computable; the defect is that a documented return handle is `void` and binding it emits illegal CUDA. Making `rng_init` return a usable handle type (or the codegen elide a `void` binding) would honor the docstring; alternatively the docstring should stop promising a bindable state handle.

### Additional context

**Root cause.** `rng_init` builds its call with a `void` result dtype, while its docstring promises a returnable `state` handle. At [`tilelang/cuda/language/random.py#L39`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/cuda/language/random.py#L39):

```python
return tirx.call_intrin("void", tirx.op.Op.get("tl.rng_init"), seed, seq, off, generator)
```

but the [docstring (L8-L27)](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/cuda/language/random.py#L8-L27) states `Returns — state: PrimExpr — The random number generator state handle`. When the caller follows that and writes `state = T.rng_init(...)`, the frontend forms a variable binding whose value is this `void`-typed expression; the C codegen prints the binding's declaration as `PrintType(void) name = <value>`, i.e. `void state = ;`, which nvcc rejects. The actual curand state is a separate module-level variable (`__random_generator_state`) the intrinsic writes to as a side effect — so the intrinsic genuinely has nothing to return, and the docstring's "returns a handle" is the inaccurate half.

**Suggested fix.** Make the documented contract and the implementation agree: either return a real handle to the curand state (so binding it is meaningful and codegens as a reference to `__random_generator_state`), or change `rng_init` to not claim a returnable handle (return `None`/no value and update the docstring), so a user cannot form a `void state = ;` binding. A narrower codegen guard — refuse to emit (or elide) a `void`-typed variable binding with a clear frontend error — would at least turn the opaque nvcc failure into an actionable one.

**Provenance.** The RNG API (`rng_init` returning a `void`-typed intrinsic while documenting a state handle) was added by [#1461](https://github.com/tile-ai/tilelang/pull/1461) (merged 2025-12-18). The `void`-return + documented-handle mismatch is present as written at the v0.1.13 tag (`random.py#L39` vs the `Returns` docstring). Reproduced at runtime on 0.1.13 this session (bind → nvcc `void state = ;`; discard control → uniform `[0,1)`). Not a recent regression.

> Note: on 0.1.9 the same binding aborted *earlier*, inside `VerifyParallelLoop` (an `InternalError: A fixed length vector doesn't have a vscale factor.` from feeding the `void` let-value to the arithmetic analyzer). That pass path no longer forms the constraint on 0.1.13, so the crash now surfaces downstream in nvcc codegen; the underlying cause (a `void`-typed `rng_init` handle bound to a variable) is the same.

**Generalization (tested this session, 0.1.13, L40S sm_89).**

<details><summary>Two-level root, 4-axis sweep, and example-run result</summary>

**Root — two levels.**
- **SOURCE-level (fragile implementation).** `rng_init` returns `tirx.call_intrin("void", tl.rng_init, ...)` at [`random.py#L39`](https://github.com/tile-ai/tilelang/blob/8001cc4ccf6149382d2019654a19f59c1d4d0482/tilelang/cuda/language/random.py#L39) while its `Returns` docstring (L23-26) names a `state` handle. Downstream, the generic C codegen prints a let-binding as `PrintType(dtype) name = <value>;`; when `dtype` is `void` and the intrinsic hands back no value, it emits `void state = ;`. The fragile code is the pairing of a *no-value* frontend intrinsic dtype with the let-binding codegen — nothing rejects a valueless capture at the frontend.
- **OPERATOR-level (what correlates).** Any TileLang frontend op that returns `call_intrin("void"/"handle", ...)` (a valueless/side-effect-only intrinsic) and is allowed to be bound to a variable hits the same `PrintType(dtype) name = ;` codegen. `rng_init` is the *only* such op whose own docstring documents a returnable handle, so it is the in-contract representative; the others are out-of-contract siblings.

**4-axis sweep (every cell RUN, result observed):**

| axis | cell tested | observed result | same-root? |
|---|---|---|---|
| the knob | `state = T.rng_init(1234)` with NO subsequent `rng_rand*` | `void state = ;` → nvcc `incomplete type "void"` | yes (binding alone triggers; drawing RNG irrelevant) |
| similar-logic / related-operator | bind void intrinsic `s = T.sync_warp()` | `void s = ;` → nvcc `incomplete type "void" is not allowed` | **same root** |
| related-type (intrinsic dtype) | bind `handle`-typed `h = T.named_barrier_arrive(0,256)` | `void* h = ;` → nvcc `expected an expression` (only) | same mechanism (empty-RHS let-binding), **distinct face**: `void*` is a complete type, so no "incomplete type" error |
| related-source / related-type | bind non-void sibling `r = T.rng_rand()` (uint32, same file) | compiles + runs; samples 546353992, 3507855656 | no — non-void return binds fine (control: confirms root is the `void`/no-value dtype, not "rng ops") |

- **Boundary — kept specific.** Reframed the *class* to "binding a valueless (`void`/`handle`) intrinsic → empty-RHS declaration", but the FILED bug stays the `rng_init` documented-handle case, because `rng_init` is the only op whose docstring invites the capture. `sync_warp`/`named_barrier_arrive` have no documented return (their docstrings show bare-statement use), so binding them is user error — recorded here as **distinct-adjacent, not filed**.

**Example-run result (PART 1).** Both cited RNG sites run clean on 0.1.13 and dodge the bug: `examples/rand/rand_uint.py` compiles + passes its Triton `assert_close` for all 3 default configs; `testing/python/language/test_tilelang_language_rand.py` → `6 passed`. Every shipped `rng_init` call is a bare discard statement (verified: `random.py` example + all 4 test-file call sites), so no shipped code exercises the crash.
</details>

**Dedup.** I searched the open and closed tracker (`rng_init`, `void state`, `VerifyParallelLoop`, `incomplete type void`) and found no existing report of this defect. Two related-but-distinct issues exist:
- **#2625** also concerns `rng_init` but is a different defect (default `seq` giving y/z threads one stream — a silent wrong result, not a compile crash) — different operator behavior, unrelated root.
- **#2667** (closed) shares the *downstream codegen symptom* — a `void`-typed op bound to a variable emits an empty-initializer declaration nvcc rejects (`int prev = ;` there, `void state = ;` here). But the *root differs*: #2667 is an atomic op-selection bug (`atomic_min`/`max` `return_prev=True` wrongly dispatches the void `*_elem_op` when it should return a value), whereas here `rng_init` genuinely has nothing to return and the docstring over-promises a handle. Fixing #2667 (route min/max to a value-returning path) does not fix this (rng has no value); they are the same codegen weakness reached from two different fronts, not the same bug. That #2667 was accepted and fixed confirms this class of empty-binding crash is treated as a real defect.

**Reach.** The trigger is a documented input: `rng_init`'s docstring names its return value the RNG state handle, and capturing a documented return value in a variable is the ordinary way to use an API. Ran the shipped RNG sites verbatim on 0.1.13 this session: `examples/rand/rand_uint.py` (`python rand_uint.py`, all 3 default configs) compiles and passes its Triton `assert_close`; `testing/python/language/test_tilelang_language_rand.py` runs `6 passed`. Every shipped site calls `T.rng_init(...)` as a bare statement and discards the return, so all of them dodge the crash and CI stays green — i.e. the shipped examples do NOT exercise this bug. A user who instead follows the docstring's `Returns` section and binds the handle hits the crash on the first compile.

**Impact.** The trigger is narrow — it needs the specific act of binding `rng_init`'s documented `void`-typed return handle to a variable (a code-shape gate, not a data value). When it fires it is a compile-time abort (an nvcc `void state = ;` error surfaced as a `RuntimeError`), so it is loud and caught on the first build, blocks that one kernel, and cannot silently corrupt output. Fixing it makes a documented `rng_init` usage compile as the docstring implies, removing a docstring/implementation disagreement.

## 评论 (2)

### 0z5a · 2026-09-17

I would like to take this.

### 0z5a · 2026-09-17

I'd like to take this together with #2625, #3029 and #3034 as one focused CUDA RNG hardening PR.

Planned scope:

1. make the `rng_init` API contract consistent with its actual hidden-state implementation,
2. reject `rng_rand` / `rng_rand_float` cleanly when no `rng_init` exists in the function,
3. make `rng_init(seq=None)` derive a unique default sequence across all launch dimensions,
4. add regression coverage for all three cases.

I'll keep the patch limited to the RNG frontend/codegen/tests. If you would prefer #2625 to be split from the state-lifecycle/API fixes, I can separate it.

The patch is up as #3239 (Fixes #2625, #3029, #3034). The PR description has the baseline-vs-patched reproducer output, an end-to-end stream-quality measurement (16/256 distinct per-thread streams before, 256/256 after), and the test results (8 failed/13 passed on baseline, 21 passed with the patch).

---

For #3029 specifically: my current interpretation is to preserve TileLang's existing hidden RNG-state model and make `rng_init` explicitly side-effect-only, rather than introducing a new public state-handle API. `rng_rand` / `rng_rand_float` do not consume an explicit handle today. If an explicit state handle is the intended API direction, please let me know before I lock this in.

