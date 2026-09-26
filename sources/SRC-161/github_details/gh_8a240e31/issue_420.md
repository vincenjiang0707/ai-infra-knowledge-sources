# [Issue #420] [Feature Request] Data Initialization Hints in FlashInfer Trace

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/420
state: closed | updated: 2026-05-28T23:59:59Z
labels: 

## 正文

## 1. Background

A `Definition` today specifies an op's interface (`axes`, `inputs`, `outputs`, `reference`) and a `Workload` specifies a concrete instance (`axes` values, `inputs` as `random | scalar | safetensors`). When a downstream consumer (NVIDIA kernel team, third-party benchmark harness, BYOK developer) wants to run a kernel against synthetic data — i.e. `RandomInput` — they have to *guess* how to fill each tensor:

- `q`, `k_cache`, `v_cache` — should they be standard-normal? RMS-normed? Scaled by `1/sqrt(d)`?
- `kv_indptr` — must be a non-decreasing cumulative sum starting at 0 and ending at `num_kv_indices`.
- `kv_indices` — integers in `[0, num_pages)`, no duplicates within a request.
- `sm_scale` — a small positive float, conventionally `1/sqrt(head_dim)`.
- LoRA / MoE routing weights — sparsely populated, often softmaxed.

Today this knowledge lives only in (a) the benchmarking framework flashinfer-bench, (b) actual workload if we have dumped in real inference. As soon as (a) we might bring flashinfer-trace to variant benchmarking framework and (b) we might generate random inputs from the logged problem shape rather always collecting the real workload, that knowledge is lost. NVIDIA's request is to make these hints first-class so a benchmark harness can produce a *valid* and *representative* random workload from the trace alone.

## 2. Goals / Non-goals

**Goals**
- Make synthetic random workloads reproducibly valid for any op in the trace.
- Cover the common cases declaratively (no Python execution required to *read* the spec).
- Provide an escape hatch for inputs with cross-tensor invariants (indptr + indices + page-table consistency, paged KV layouts, etc.).

## 3. Proposal

In short: we have two options. (a) using both tier A and B; (b) using only tier B.

Two-tier design that mirrors the rest of the schema (declarative metadata + code reference):

### 3.1 Tier A — Per-input declarative `init` tag

Add an optional `init` field on `TensorSpec`. Closed enum of `kind`s, each with typed args. The harness can execute these without `eval`-ing user code.

```jsonc
"inputs": {
  "q":          { "shape": ["batch_size", "num_q_heads", "head_dim"], "dtype": "bfloat16",
                  "init": {"kind": "normal", "mean": 0.0, "std": 1.0} },
  "k_cache":    { "shape": ["num_pages", "page_size", "num_kv_heads", "head_dim"], "dtype": "bfloat16",
                  "init": {"kind": "normal", "mean": 0.0, "std": 1.0} },
  "kv_indptr":  { "shape": ["batch_size_plus_1"], "dtype": "int32",
                  "init": {"kind": "indptr", "segment_axis": "batch_size", "total_axis": "num_kv_indices"} },
  "kv_indices": { "shape": ["num_kv_indices"], "dtype": "int32",
                  "init": {"kind": "index", "range_axis": "num_pages", "unique_per_segment": "kv_indptr"} },
  "sm_scale":   { "shape": null, "dtype": "float32",
                  "init": {"kind": "constant", "value": 0.08838834764} }
}
```

Initial `kind` set (extensible):

| kind | args | semantics |
|---|---|---|
| `constant` | `value` | fill |
| `uniform` | `low`, `high` | `U[low, high)` |
| `normal` | `mean`, `std` | `N(mean, std)` |
| `normalized` | `axis`, `eps` | normal then L2- or RMS-normed along `axis` |
| `index` | `range_axis`, `unique_per_segment?` | int in `[0, axes[range_axis])` |
| `indptr` | `segment_axis`, `total_axis` | non-decreasing cumsum, `[0]=0`, `[-1]=axes[total_axis]` |
| `permutation` | `range_axis` | permutation of `[0, axes[range_axis])` |
| `one_hot` / `routing` | `num_experts_axis`, `top_k` | sparse top-k routing weights |
| `custom` | `func`, `extra_args?` | falls through to Tier B |

A global `seed` lives at the workload level (see §3.3) so the entire init is deterministic.

### 3.2 Tier B — Definition-level `init()` code (escape hatch) [preferred now]

For inputs with cross-tensor invariants the declarative form can't cleanly express (paged KV with `kv_indptr` + `kv_indices` + `kv_last_page_len` consistency, MLA's tied q/k projections, MoE's routing-determined expert workloads), Yingyi's original proposal applies: a Python source string parallel to `reference`, with an `init()` function.

```python
def init(*, batch_size: int, num_pages: int, page_size: int, num_kv_indices: int,
         num_q_heads: int, num_kv_heads: int, head_dim: int, dtype, device, seed: int):
    g = torch.Generator(device=device).manual_seed(seed)
    # ... cross-tensor logic here ...
    return {
        "q": q, "k_cache": k_cache, "v_cache": v_cache,
        "kv_indptr": kv_indptr, "kv_indices": kv_indices,
        "kv_last_page_len": last_page_len, "sm_scale": 1.0 / math.sqrt(head_dim),
    }
```

Rules:
- `init()` keyword args are exactly the union of `axes` keys plus `dtype`/`device`/`seed`.
- Returns a dict whose keys exactly match `Definition.inputs`.
- Validated at load time (shape/dtype must match `TensorSpec`).
- Tier A and Tier B can coexist — Tier B fills any input whose Tier A `init` is `{"kind":"custom"}` or absent. (Decision point — see §6.)

### 3.3 Workload-level overrides (not working)

We always provide valid safetensors.

### 3.4 Benchmarking framwork support (not working)

For each kernel definition, benchmarking framework knows how to randomly init all tensors.

## 4. Schema changes (3.1, 3.2)

```python
# flashinfer_bench/data/definition.py
class TensorSpec(BaseModelWithDocstrings):
    shape: Optional[List[NonEmptyString]]
    dtype: DType
    description: Optional[str] = None
    init: Optional[InitSpec] = None          # NEW

class Definition(BaseModelWithDocstrings):
    ...
    init: Optional[NonEmptyString] = None    # NEW — Python source w/ top-level `init`

# flashinfer_bench/data/workload.py
class RandomInput(BaseModelWithDocstrings):
    type: Literal["random"] = "random"
    seed: int = 0                            # NEW
    init: Optional[InitSpec] = None          # NEW — workload-level override
```

`InitSpec = Annotated[Union[Constant, Uniform, Normal, Normalized, Index, Indptr, Permutation, Routing, Custom], Field(discriminator="kind")]`.

Validation (added to `Definition` model validators):
- For each input with declarative `init`, axis names referenced by the spec must exist in `axes`.
- If `Definition.init` is present, parse it, require a top-level `init` function, and check the parameter names are a subset of `axes ∪ {dtype, device, seed}`.
- All inputs must be initializable: every input has a Tier A `init`, or `Definition.init` exists and Tier B covers it.

## 5. Open questions

1. **Tier B granularity:** one `init()` per Definition (proposed), vs. one per input via `{"kind":"custom","func":...}` referencing named functions inside a shared `init` module. The first is simpler to validate; the second composes better. Leaning toward (1) for v1.
2. **Where does `seed` default live?** Workload (proposed) vs. global benchmark config. If two workloads sharing a seed *must* produce the same tensors, we need the seed in the workload.
3. **Should `RandomInput` be inferred?** If a Definition declares `init` for every input, can the Workload omit `inputs` entirely and default to "random with the Definition's hints"? This would be a nice ergonomic win for the NV team.
4. **`init` vs. `reference` reuse:** for ops where the reference already takes ground-truth pre-computed inputs (e.g. attention), should `init` get a `from_reference: true` shorthand that runs a smaller "naive" computation to derive coupled tensors? Probably premature.
5. **Sandboxing Tier B:** Tier B code runs in the harness process. Same trust model as `reference` today, but worth calling out for the NV team since they may run untrusted traces.

## 6. Migration

- Field is optional → existing 700+ definitions are valid as-is.
- Add `init` opportunistically: start with the kernels NV is consuming (MLA paged, GQA paged, MoE) — those are exactly the ones where ad-hoc init is most painful.
- Provide a `flashinfer-bench init-lint` subcommand that flags definitions missing `init` so we can drive coverage to 100% over time. Make another pull request at fiashinfer side to update the template.
- Update the `extract-kernel-definitions` skill to populate Tier A `init` from SGLang test fixtures where possible.

## 评论 (1)

### yyihuang · 2026-05-28

Closed with PR #3221 closed.
