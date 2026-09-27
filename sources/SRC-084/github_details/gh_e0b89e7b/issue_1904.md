# [Issue #1904] Params4bit.__getattr__ breaks torch.compile - use @property instead

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1904
state: closed | updated: 2026-04-10T05:57:43Z
labels: torch.compile, FSDP

## 正文

### System Info

PR #1866 added `__getattr__` to `Params4bit` for FSDP state_dict support. This works fine for FSDP, but it breaks `torch.compile`.

`Params4bit` is a `torch.Tensor` subclass. PyTorch's Dynamo (the compiler frontend) doesn't know how to trace tensor subclasses that define `__getattr__`, so it creates graph breaks whenever it encounters attribute access on such objects. With activation checkpointing, these graph breaks multiply across layers, resulting in many more subgraphs than necessary and significant compilation overhead.

We noticed this when running `torch.compile` on a QLoRA fine-tuning workload (LLaMA 70B, HuggingFace, activation checkpointing). With `__getattr__` present, we saw significant performance degradation caused by graph breaks. Removing `__getattr__` (or replacing with `@property` as proposed below) restores expected performance.

### Reproduction

I put together a minimal repro using `torch._dynamo.explain()` on a small model with `Linear4bit` and activation checkpointing. With `__getattr__` present it showed graph breaks; after removing it, they were gone. The script is rough, so I'd appreciate it if you could verify this with a more representative test — or suggest one if you have something better suited.

### Expected behavior

Replace `__getattr__` + `_QUANT_STATE_ATTR_MAP` with `@property` descriptors. Properties are resolved at the class level through Python's descriptor protocol — Dynamo handles them fine, no graph breaks. FSDP still works because `getattr(weight, "absmax")` resolves the same way. Example:

```python
    @property
    def absmax(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None:
            return qs.absmax
        raise AttributeError("'Params4bit' object has no attribute 'absmax'")

    @property
    def code(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None:
            return qs.code
        raise AttributeError("'Params4bit' object has no attribute 'code'")

    @property
    def quant_map(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None:
            return qs.code
        raise AttributeError("'Params4bit' object has no attribute 'quant_map'")

    @property
    def offset(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None:
            return qs.offset
        raise AttributeError("'Params4bit' object has no attribute 'offset'")

    @property
    def state2(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None:
            return qs.state2
        raise AttributeError("'Params4bit' object has no attribute 'state2'")

    @property
    def nested_absmax(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None and qs.state2 is not None:
            return qs.state2.absmax
        raise AttributeError("'Params4bit' object has no attribute 'nested_absmax'")

    @property
    def nested_blocksize(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None and qs.state2 is not None:
            return qs.state2.blocksize
        raise AttributeError("'Params4bit' object has no attribute 'nested_blocksize'")

    @property
    def nested_quant_map(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None and qs.state2 is not None:
            return qs.state2.code
        raise AttributeError("'Params4bit' object has no attribute 'nested_quant_map'")

    @property
    def nested_dtype(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None and qs.state2 is not None:
            return qs.state2.dtype
        raise AttributeError("'Params4bit' object has no attribute 'nested_dtype'")

    @property
    def nested_offset(self):
        qs = self.__dict__.get("quant_state")
        if qs is not None:
            return qs.offset
        raise AttributeError("'Params4bit' object has no attribute 'nested_offset'")
```

## 评论 (2)

### Titus-von-Koeller · 2026-04-02

Thanks for the detailed report, @kbabiuchx — this is a real and well-understood issue. `__getattr__` on a `torch.Tensor` subclass is indeed a Dynamo graph-break trigger, and the `@property` approach is the right fix, I think.

A few things we'd like to nail down before implementation:

1. **Attribute collisions with instance attrs.** `Params4bit.__new__` sets `self.blocksize`, `self.compress_statistics`, `self.quant_type`, `self.quant_storage`, and `self.module` directly on the instance. The current `_QUANT_STATE_ATTR_MAP` also proxies `blocksize`, `dtype`, `shape`, and `quant_type` from `quant_state` — but your proposed properties omit those. Was that intentional? We think it's correct to omit them (a read-only `@property` would shadow the instance attribute and break `__new__`), but want to confirm FSDP doesn't actually traverse `weight.blocksize` etc.

2. **`QuantState.__getattr__`** — we plan to keep this as-is since `QuantState` isn't a `Tensor` subclass and Dynamo doesn't have the same issue with it. Agreed?

3. **Regression test** — would you be able to share your `torch._dynamo.explain()` repro (even rough) so we can turn it into a proper test asserting zero graph breaks? We'd like to land the fix with a test that prevents this from regressing.

### Titus-von-Koeller · 2026-04-07

Update: we've implemented and validated this fix. The approach is exactly as you proposed — replace `__getattr__` + `_QUANT_STATE_ATTR_MAP` with `@property` descriptors on `Params4bit`.

A few details from the implementation:

**Attributes that got `@property`:** `absmax`, `code`, `quant_map`, `offset`, `state2`, `nested_absmax`, `nested_blocksize`, `nested_quant_map`, `nested_dtype`, `nested_offset` (10 total).

**Attributes intentionally omitted:** `blocksize`, `quant_type`, `dtype`, `shape` — these collide with instance attributes set in `Params4bit.__new__` or inherited from `torch.Tensor`. A read-only `@property` would break `self.blocksize = 64` etc. This is safe because these values are packed into the `bitsandbytes__*` blob by `as_dict(packed=True)` and are never separate state_dict keys — FSDP doesn't traverse them via `getattr(weight, "blocksize")`.

**`QuantState.__getattr__`** was left as-is — `QuantState` is not a `torch.Tensor` subclass, so Dynamo has no issue tracing it.

**Validation:** We added a regression test (`test_linear4bit_torch_compile_activation_checkpointing`) that compiles a `Linear4bit` network with `torch.utils.checkpoint` and `fullgraph=True`. Verified across three states:
- Before #1866 (no `__getattr__`): **passes** ✓
- At #1866 (with `__getattr__`): **fails** (graph break) ✓
- After fix (`@property`): **passes** ✓

Existing `torch.compile` and FSDP attribute access tests all continue to pass.

PR: #1916
