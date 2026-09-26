# [Issue #1946] Linear4bit._save_to_state_dict writes QuantState keys but no _load_from_state_dict consumes them (asymmetric serialization)

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1946
state: open | updated: 2026-05-11T20:36:43Z
labels: 

## 正文

### Summary

`bitsandbytes.nn.Linear4bit` overrides `_save_to_state_dict` (`bitsandbytes/nn/modules.py:593`) to write QuantState components alongside the packed weight:

```python
def _save_to_state_dict(self, destination, prefix, keep_vars):
    super()._save_to_state_dict(destination, prefix, keep_vars)  # weight + bias
    if getattr(self.weight, "quant_state", None) is not None:
        for k, v in self.weight.quant_state.as_dict(packed=True).items():
            destination[prefix + "weight." + k] = v if keep_vars else v.detach()
```

Resulting state_dict keys for a Linear4bit (with `compress_statistics=True`):
- `weight` (packed 4-bit tensor)
- `weight.absmax`
- `weight.quant_map`
- `weight.nested_absmax`
- `weight.nested_quant_map`
- `weight.quant_state.bitsandbytes__nf4` (or `__fp4`)

`Linear4bit` does **not** define a corresponding `_load_from_state_dict`. It inherits `nn.Linear._load_from_state_dict`, which only consumes `weight` and `bias`. The QuantState keys land in `unexpected_keys` during load. With `strict=True` (the `model.load_state_dict()` default) this raises `RuntimeError`.

This is asymmetric relative to `Linear8bitLt`, which defines both `_save_to_state_dict` (line 1095) **and** `_load_from_state_dict` (line 1119), with the latter explicitly walking `unexpected_keys` to consume the SCB tensor and remove it from the unexpected list.

### Reproducer

```python
import torch
import bitsandbytes as bnb

src = bnb.nn.Linear4bit(64, 64, bias=False, quant_type='nf4',
                       compute_dtype=torch.bfloat16,
                       compress_statistics=True)
src = src.to('cuda')  # triggers quantize, populates quant_state

sd = src.state_dict()
print("state_dict keys:", list(sd.keys()))
# ['weight', 'weight.absmax', 'weight.quant_map', 'weight.nested_absmax',
#  'weight.nested_quant_map', 'weight.quant_state.bitsandbytes__nf4']

dst = bnb.nn.Linear4bit(64, 64, bias=False, quant_type='nf4',
                       compute_dtype=torch.bfloat16,
                       compress_statistics=True)
dst = dst.to('cuda')

# Fails with strict=True (the default):
dst.load_state_dict(sd)
# RuntimeError: Error(s) in loading state_dict for Linear4bit:
#     Unexpected key(s) in state_dict: "weight.absmax", "weight.quant_map",
#     "weight.nested_absmax", "weight.nested_quant_map",
#     "weight.quant_state.bitsandbytes__nf4"
```

With `strict=False`, the QuantState components are silently ignored: `dst.weight.data` becomes the packed bytes from `src`, but `dst.weight.quant_state` is the one populated during `dst.to('cuda')` — not the one from `sd`. If `src` and `dst` quantized with different inputs (very common, e.g. loading a checkpoint into a freshly-initialized module), `dst` is left in a silently-corrupt state: packed bytes from one model, QuantState scalars from another.

### Why this hasn't been reported as a user-facing bug

Standard workflows bypass `model.load_state_dict()` for bnb-quantized checkpoints:

1. **HF Transformers `from_pretrained` for pre-quantized bnb checkpoints:** uses `bnb.nn.Params4bit.from_prequantized(data, quantized_stats, device=...)` directly via `transformers/quantizers/quantizer_bnb_4bit.py::create_quantized_param`. The `quantized_stats` dict is built by walking state_dict keys with prefix `param_name + "."`. Bypasses `_load_from_state_dict` entirely.
2. **PEFT save/load:** `get_peft_model_state_dict` filters to LoRA-only keys (`"lora_" in k`); QuantState keys never enter the PEFT round-trip.
3. **Accelerate's `fsdp2_load_full_state_dict`:** has its own broadcast + `assign=True` path; PR #3982 added key-based matching that filters non-Params keys.

Paths that **do** hit the asymmetry:
- `torch.distributed.checkpoint` (DCP) when the loaded state_dict contains QuantState keys
- Custom training loops that save via `model.state_dict()` and resume via `model.load_state_dict()`
- The docstring example at `nn/modules.py:522` (`quantized_model.load_state_dict(fp16_model.state_dict())`) works only because the source is **fp16** (no QuantState keys to be unexpected) — masking the bnb→bnb round-trip case

### Discovery context

Surfaced while characterizing FSDP2 + `Params4bit` forward correctness on Jetson Orin Nano Super (sm_87) — the same investigation that led to #1945. The investigation needed to round-trip QuantState through `state_dict()` for a pre-shard-broadcast pattern; that worked on the save side and failed on the load side, leading to this finding. The two issues are unrelated mechanically — this one is a missing override, #1945 is a PyTorch FSDP2 NaN-canonicalization bug — but they share discovery provenance.

### Suggested fix

Implement `_load_from_state_dict` paralleling `Linear8bitLt`'s pattern. Sketch:

```python
def _load_from_state_dict(
    self, state_dict, prefix, local_metadata, strict,
    missing_keys, unexpected_keys, error_msgs,
):
    # Collect QuantState components in state_dict for this prefix
    qs_keys_to_consume = []
    quantized_stats = {}
    weight_dot_prefix = prefix + "weight."
    for k in list(state_dict.keys()):
        if k.startswith(weight_dot_prefix):
            qs_keys_to_consume.append(k)
            # store as `weight.<subkey>` for from_prequantized
            quantized_stats[k[len(prefix):]] = state_dict[k]

    # Standard nn.Linear path consumes 'weight' and 'bias'
    super()._load_from_state_dict(
        state_dict, prefix, local_metadata, strict,
        missing_keys, unexpected_keys, error_msgs,
    )

    # If QuantState components are present, reconstruct via from_prequantized
    if quantized_stats:
        for k in qs_keys_to_consume:
            if k in unexpected_keys:
                unexpected_keys.remove(k)

        weight_data = self.weight.data  # already loaded by super()
        self.weight = Params4bit.from_prequantized(
            data=weight_data,
            quantized_stats=quantized_stats,
            requires_grad=False,
            device=weight_data.device,
            module=self,
        )
```

Edge cases:
- If QuantState keys are absent (e.g., the existing fp16→bnb docstring example), `quantized_stats` is empty and the function falls through to standard `nn.Linear` behavior — no regression.
- The `weight_dot_prefix` match cleanly delimits per-Linear keys; the state_dict passed to `_load_from_state_dict` is already filtered to the current module's prefix by `nn.Module.load_state_dict()`'s recursion.

### Test plan (for the fix)

- [ ] Bnb→bnb round-trip: `m1.state_dict() → m2.load_state_dict(strict=True)` on CPU then CUDA Linear4bit; assert `bnb.matmul_4bit` produces identical output on synthetic input.
- [ ] Existing fp16→bnb docstring example continues to pass (no regression).
- [ ] Variant matrix: NF4 / FP4, `compress_statistics` on/off, `quant_storage` ∈ {uint8, bf16, fp16}, with/without bias.
- [ ] `strict=False` behavior with partial QuantState keys (fall back to existing `_quantize` flow on `.to(device)` if applicable).

### Severity

**Latent — currently masked.** Does not surface in standard HF + PEFT workflows because they bypass `load_state_dict`. But it's a contract violation between `_save_to_state_dict` and the standard `nn.Module` load mechanism, and surfaces for:
- `torch.distributed.checkpoint` (DCP) usage
- Custom training-loop checkpoint code
- Any tooling that round-trips through `model.state_dict()` + `model.load_state_dict()`

### Adjacent PRs (for context, do not address this)

- PR #1866 — `Params4bit.__getattr__` proxy for FSDP `_get_fqns()` traversal (state_dict *traversal*, not load).
- PR #1916 — replaces #1866's `__getattr__` with `@property` descriptors (motivated by `torch.compile` graph breaks, preserved FSDP traversal as a side effect).

Neither addresses the missing `_load_from_state_dict`.

Happy to file a PR with the fix sketch + tests if useful.


## 评论 (1)

### neil-the-nowledgeable · 2026-05-11

Follow-up: prior art and a less invasive alternative

### Prior art — this was attempted in 2023 and reverted

Cross-referencing two PRs I should have surfaced in the original "Adjacent PRs" section:

- [PR #753](https://github.com/bitsandbytes-foundation/bitsandbytes/pull/753) (merged 2023-11-08, *Save and load in NF4 / FP4 formats*) — added `Linear4bit._load_from_state_dict` to consume the QuantState components via a `Params4bit.from_state_dict()` helper, alongside the `_save_to_state_dict` that still lives today.
- [PR #864](https://github.com/bitsandbytes-foundation/bitsandbytes/pull/864) (merged 2023-11-09, *fixes to recent PR #753*) — **reverted the `_load_from_state_dict` override.** Author note in the PR body: *"The idea to override `_load_from_state_dict` for `Linear4bit` looked very elegant, with a view to simplify Transformers integration. However it has more sensitivities than I expected including one with `peft`."*

This issue's suggested fix is structurally the same intervention. I should be upfront that the prior attempt didn't survive contact with PEFT, and that I haven't yet characterized exactly which PEFT path failed. Two thoughts on how to move forward:

### Why the suggested sketch differs from the reverted code

For comparison, the relevant body of the 2023 `_load_from_state_dict` (from PR #753, removed by PR #864):

```python
def _load_from_state_dict(self, state_dict, prefix, local_metadata, strict,
                          missing_keys, unexpected_keys, error_msgs):
    # Note: super()._load_from_state_dict() is not called here intentionally.
    if self.bias is not None:
        bias_data = state_dict.pop(prefix + "bias", None)
        self.bias.data = bias_data.to(self.bias.data.device)

    self.weight, state_dict = bnb.nn.Params4bit.from_state_dict(
                    state_dict, prefix=prefix + "weight" + ".", requires_grad=False
                )
    unexpected_keys.extend(state_dict.keys())
```

The sketch in my issue body differs in four concrete ways that may matter for the PEFT case:

1. **Calls `super()._load_from_state_dict(...)` first.** The 2023 version explicitly skipped it ("not called here intentionally"). `peft.tuners.lora.Linear4bit` subclasses `bnb.nn.Linear4bit`; PEFT's LoRA-wrapped load path may depend on the standard `nn.Linear._load_from_state_dict` running to populate `weight`/`bias` before any wrapper logic. Skipping super was the most aggressive choice in the 2023 attempt and is a plausible root for the PEFT sensitivity.
2. **Only triggers QuantState reconstruction when QuantState keys are present** (`if quantized_stats:`). The 2023 version unconditionally rebuilt `self.weight` via `Params4bit.from_state_dict`, which would also alter behavior for fp16→bnb loads (the existing docstring example at `nn/modules.py:532`). The conditional gate keeps the non-quantized-source path bit-identical to today's behavior.
3. **Does not mutate the caller's `state_dict`.** The 2023 version called `state_dict.pop("bias")`, then returned a mutated `state_dict` from `from_state_dict`. The conditional gate avoids this entirely when QuantState keys are absent, and selectively removes consumed keys from `unexpected_keys` (not `state_dict`) when they are present.
4. **Uses the documented `Params4bit.from_prequantized` API** that today's HF Transformers integration uses (via `quantizer_bnb_4bit.py` → `WeightConverter` / `Bnb4bitDeserialize`), rather than a now-removed `Params4bit.from_state_dict` factory. Same machinery the production HF path exercises.

Those are differences, not proofs. I haven't yet driven a PEFT round-trip through the sketch to confirm it survives. I'd want to do that before opening a PR — happy to characterize the PEFT failure mode against the 2023 implementation as a precondition, so any new PR ships with an explicit "here is what previously broke; here is the regression test that pins it."

### Less invasive alternative: `_register_load_state_dict_pre_hook`

If the PEFT sensitivity turns out to be inherent to overriding `_load_from_state_dict` at all (rather than the specifics of the 2023 implementation), a pre-hook is strictly less invasive and follows precedent already in `Linear8bitLt` ([line 1093](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/bitsandbytes/nn/modules.py#L1093): `self._register_load_state_dict_pre_hook(maybe_rearrange_weight)`):

```python
# In Linear4bit.__init__, after super().__init__:
self._register_load_state_dict_pre_hook(_consume_quant_state_keys)

def _consume_quant_state_keys(
    self, state_dict, prefix, local_metadata, strict,
    missing_keys, unexpected_keys, error_msgs,
):
    weight_dot_prefix = prefix + "weight."
    qs_keys = [k for k in state_dict if k.startswith(weight_dot_prefix)]
    if not qs_keys:
        return  # fp16→bnb path or any non-prequantized source — defer to super

    quantized_stats = {k[len(prefix):]: state_dict.pop(k) for k in qs_keys}
    weight_data = state_dict.pop(prefix + "weight")

    self.weight = Params4bit.from_prequantized(
        data=weight_data,
        quantized_stats=quantized_stats,
        requires_grad=False,
        device=weight_data.device,
        module=self,
    )
    # After this hook returns, super()._load_from_state_dict sees a clean
    # state_dict with only 'bias' (if present) remaining for this prefix —
    # the standard nn.Linear path handles it unchanged.
```

Properties of this approach:
- Inheritance contract is untouched. `_load_from_state_dict` is whatever `nn.Linear` and `peft.tuners.lora.Linear4bit` say it should be — no override, no super-skipping, nothing in the MRO to interact with PEFT's wrapper.
- Falls through cleanly when QuantState keys are absent (early return) — the fp16→bnb docstring example continues to take the existing path.
- Doesn't touch `unexpected_keys` directly; instead pops consumed keys from `state_dict` so super never sees them as unexpected in the first place. This composes more cleanly with whatever PEFT does to `state_dict` between when it's passed in and when `nn.Linear._load_from_state_dict` reads it.
- Drops in next to the existing `_save_to_state_dict` with no inheritance-graph changes.

Trade-off: the pre-hook mutates the incoming `state_dict` (pop), where `_load_from_state_dict` overrides typically don't. PyTorch's documented contract for pre-hooks does permit `state_dict` mutation, and `Linear8bitLt` already uses the pattern, so this is consistent with current bnb conventions.

### Suggested path forward

1. Characterize the original PEFT failure against PR #753's reverted code (find the specific PEFT call site that broke) — gives the regression a name.
2. Pick between the conditional `_load_from_state_dict` override (as in the issue body) and the pre-hook (as above), based on what the PEFT failure was actually about.
3. PR with a regression test that pins the prior failure, plus the bnb→bnb round-trip + variant matrix from the original test plan.

I'll do step 1 against my local setup (bnb 0.46.1 source-built sm_87 + transformers 4.56.0 + peft 0.18.0) and follow up before opening any PR. If maintainers have intuition about which PEFT path was the original casualty, that'd shortcut the investigation considerably.

