# [Issue #4485] [Feature]: Add caller selectable LSE base

source: https://github.com/flashinfer-ai/flashinfer/issues/4485
state: closed | updated: 2026-09-21T18:55:27Z
labels: feature request, needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

CP combines partial attention w/ LSE. Depending on the backend, the LSE may be represented in natural-log or base-2 form.

Requiring the caller to infer the convention from the selected backend is fragile, and majority backend currently return natural-log, i.e. FlashAttention | FlashMLA etc.


### Requested outcome

Allow callers to explicitly select the base of returned LSE values. i.e.

```
  out, lse = trtllm_batch_decode_with_kv_cache_mla(
      ...,
      return_lse=True,
      lse_base="e",  # "2"
  )
```

### Target hardware

Hardware-independent

### Inference engine

vLLM

### Affected model or model family

_No response_

### Workload and configuration




### Current workaround

https://github.com/vllm-project/vllm/blob/34735aceda0be9d79d8f440fcb74a21825bde0b6/vllm/v1/attention/backends/mla/flashinfer_mla.py#L199-L204

### Impact

_No response_

### Acceptance criteria

_No response_

### Related work, dependencies, or suggested scope

cc. @kmrao-nv 

### Timing or release need

_No response_

## 评论 (3)

### 3xela · 2026-08-17

!claim

### flashinfer-bot · 2026-08-17

Issue assigned to @3xela.

### 3xela · 2026-08-18

Picked this up. Before adding a base parameter it is worth settling what the current base
is, because it already differs between backends.

`trtllm_batch_decode_with_kv_cache_mla(..., return_lse=True)` returns base-2 LSE from
trtllm-gen and base-e LSE from cute-dsl monolithic. With `backend="auto"` a caller can get
either one, decided by things the call site does not control.

| backend | LSE base | how established |
|---|---|---|
| trtllm-gen | 2 | measured, and from source |
| cute-dsl monolithic | e | measured, and from source |
| sparse (SM120/SM121) | 2 | source only, no SM120 hardware to hand |
| xqa, cute-dsl modular | n/a | reject `return_lse` outright |

## Measurements, B200 (SM100)

Identical inputs to both calls: batch 4, 128 heads, `head_dim_qk` 576, `page_size` 64,
`seq_len` 256, bf16.

```
trtllm-gen   mean 10.116785
cute-dsl     mean  7.012421
ratio        mean 1.442695   std 0.000000
```

The ratio is exactly log2(e) at every one of the 512 elements, with zero variance, so the
two kernels differ in units rather than in numerics.

With the same KV cache, the same scales and `backend="auto"` in both calls, switching the
query layout from dense to ragged switches the base:

```
dense 4-D q                      10.116785    (trtllm-gen, base 2)
ragged 3-D q + cum_seq_lens_q     7.012421    (cute-dsl,   base e)
```

`flashinfer/mla/_core.py:3985-3988` overrides `trt_var_q_reason` whenever `cum_seq_lens_q`
is in use and either `return_lse` is true or an `lse` tensor is passed, which disqualifies
trtllm-gen and lets `auto` fall through to cute-dsl. On the dense path both runners are
autotuner candidates (`_core.py:4239-4243`, selected at `4345`), so the base can also depend
on autotune timing.

Base 2 also holds on Hopper, where I could check against a reference:
`tests/attention/test_deepseek_mla.py` passes against `torch.logsumexp * log2(e)` (built at
`:139` and `:152`), including `BatchMLAPagedAttentionWrapper.run` at `:345`, `:481` and
`:563`.

## Where each base comes from in source

The kernels that consume LSE merge in base 2: `math::ptx_exp2` in
`include/flashinfer/attention/cascade.cuh:56,57,101,102` and `state.cuh:57,60`, and
`tl.exp2`/`tl.log2` in `flashinfer/triton/kernels/cascade.py:8,21,57,82,95`. Every LSE
reference under `flashinfer/trace/templates/` is `logsumexp / math.log(2.0)`.

trtllm-gen fuses log2(e) into the softmax scale (`M_LOG2E` at
`csrc/trtllm_fmha_kernel_launcher.cu:189` for the scalar case, `log2e` at `_core.py:3915`
for the tensor case), accumulates `m` and `d` in natural base
(`csrc/fmhaReduction.cu:239-241` and `:264-269`), then computes `lse = log2e*m + log2(d)` at
`include/flashinfer/trtllm/fmha/lse.cuh:46`. The base is not locked inside the prebuilt
cubin, since `fmhaKernels.cuh:436` calls the in-repo `ComputeLSEFromMD`.

cute-dsl monolithic multiplies by `1.0 / LOG2_E` at each final store, in
`flashinfer/cute_dsl/attention/monolithic/mla_decode_fp16.py:1781,1783,3800` and
`mla_decode_fp8.py:2028,2030,4308`.

## Comments and docs that state the opposite

- `flashinfer/mla/_core.py:2354-2359` documents `return_lse_base_on_e=True` as being for
  "cascade-merging APIs that expect base-e LSEs". Those APIs merge in base 2
  (`cascade.cuh:56`).
- `flashinfer/cute_dsl/attention/wrappers/batch_mla.py:841-845` says the modular path
  "writes LSE in log2 base directly to its internal buffer and does not convert", and that
  exposing it "would silently disagree with the trtllm-gen + monolithic convention (natural
  log)". trtllm-gen is base 2, so the modular path's log2 output would in fact agree with
  trtllm-gen and with the cascade kernels. The refusal at `:846` is still defensible while
  monolithic converts to base e, but the premise stated for it is backwards.
- `sparse_mla_reference_torch` in `tests/attention/test_trtllm_gen_mla.py:116` computes a
  natural-log LSE at `:196` and returns it at `:238`, but its only caller discards it
  (`out_ref, _ = ...` at `:881`). Harmless today, wrong for anyone who wires the comparison
  up later.

## Where the base-e conversion came from

`#3309` (2cf8f4cc, 2026-05-29, "Add num_heads < 128 support for mla decode kernel") changed
the monolithic store from `mLSE[...] = global_lse` to `global_lse * (1.0 / LOG2_E)`, with
this comment:

```
# Convert from kernel-internal log2 base to the natural-log
# convention exposed to callers (matches trtllm-gen / flash-attn).
```

Before that commit the monolithic kernel stored base 2 and therefore agreed with trtllm-gen.
The stated premise is wrong for trtllm-gen, which is base 2. The flash-attn half of the
comparison may well be right, but FlashInfer's own merge kernels are base 2 either way.
`#4178` (4890932d, 2026-07-29) then copied the same conversion into the packed low-head and
variable-Q stores.

The split-KV intermediate is deliberately left in log2 so the merge can use exp2/log2
(comment at `mla_decode_fp16.py:3795-3798`), so only the user-facing store converts. Nothing
under `flashinfer/` reads these LSE values back; the only in-tree consumers are tests.
Reverting to base 2 is therefore a one-line deletion at each of the six store sites.

## Why CI has not caught this

`.github/workflows/pr-test.yml:179,189,198` runs A10G (SM86), T4 (SM75) and H100 (SM90), and
no workflow in the repo matches `sm100|sm103|sm120|sm121|blackwell|b200|gb200`. So
`tests/attention/test_cute_dsl_mla_decode.py`, which asserts natural log at `:544` against
an unconverted `torch.logsumexp` (`:144`), and `tests/attention/test_sparse_mla_sm120.py`,
which assumes base 2, both skip on every runner in the matrix.
`tests/attention/test_trtllm_gen_mla.py:499` does exercise `return_lse=True`, but its
assertions at `:520-530` cover only identity, dtype, shape and finiteness.

## Questions

1. `#3309` introduced the base-e conversion to match trtllm-gen, and trtllm-gen is base 2.
   Is there another reason to keep it, such as a downstream consumer that already depends on
   natural log? If not, I would propose reverting those six stores to base 2 as a bug fix.
   That also settles the default: while the bases differ per backend, preserving current
   behaviour and offering one fixed default cannot both hold.
2. On the API shape, my preference is to reuse what already exists rather than grow a second
   spelling of the same concept. `BatchMLAPagedAttentionWrapper` already takes
   `return_lse_base_on_e: bool = False` (`_core.py:2278`, through
   `csrc/batch_mla_run.cu:35` and `mla_params.cuh:81` to the `math::loge2` multiply at
   `mla.cuh:809`), where `False` means base 2 and `True` means base e. Giving
   `trtllm_batch_decode_with_kv_cache_mla` the same parameter name, semantics and default
   keeps one concept with one spelling, at the cost of not matching the `lse_base="e"|"2"`
   spelling the issue proposes. Does that trade look right to you, or is the string form
   wanted specifically?

   Note that reuse and question 1 are coupled. `return_lse_base_on_e=False` can only mean
   "base 2" if every backend natively produces base 2, which holds once the cute-dsl stores
   are reverted. If cute-dsl keeps base e, then `False` means "base 2, unless you happened to
   get cute-dsl", and the flag cannot carry a single meaning.
3. Should a first change cover `trtllm_batch_decode_with_kv_cache_mla` only, or also the
   wrapper class and the other LSE-returning APIs in `prefill.py`, `decode.py` and
   `cascade.py`?
4. Is there internal SM100 or SM12x CI a fix could be verified against? The public matrix has
   none, so I can only speak for what a rented B200 covers.

The reproduction script needs an SM100-family GPU and CUDA >= 12.8. I can attach it, or turn
it into a test if there is a runner for it.

