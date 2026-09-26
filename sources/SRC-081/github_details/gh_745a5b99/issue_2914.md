# [Issue #2914] [Bug]: IMatrixMSEObserver crashes in sequential pipeline when IMatrixGatherer is followed by GPTQModifier

source: https://github.com/vllm-project/llm-compressor/issues/2914
state: closed | updated: 2026-07-28T21:23:23Z
labels: bug

## 正文

### ⚙️ Your current environment

## Environment Information ###
Operating System: `Linux-6.17.0-1026-nvidia-aarch64-with-glibc2.39`
Python Version: `3.12.13 (main, Jun 23 2026, 15:19:07) [Clang 22.1.3 ]`
llm-compressor Version: `0.12.0`
compressed-tensors Version: `0.17.1`
transformers Version: `5.10.1`
torch Version: `2.13.0`
CUDA Devices: `['NVIDIA GB10']`
AMD Devices: `None`
NPU Devices: `None`

### 🐛 Describe the bug

New to this cool project, hit this error and sent `opencode + kimi-2.7-code` on it and this is what it came back with. The code appears to work, minus correctness because I do not know enough to validate that yet. Working towards getting the evals setup as a basic sanity check.


## Summary
When using `IMatrixGatherer` followed by `GPTQModifier` with `pipeline="sequential"`, calibration crashes on the second subgraph with:

```text
AttributeError: 'Linear' object has no attribute '_imatrix_sum'. Did you mean: '_imatrix_hook'?
```

The crash originates in `src/llmcompressor/observers/imatrix.py:108` inside the `_hook` closure registered by `IMatrixMSEObserver.attach`.

## Reproduction
Run the following recipe against a model such as `Qwen/Qwen3.6-27B`:

```python
import torch
from compressed_tensors.quantization import preset_name_to_scheme
from datasets import load_dataset
from transformers import AutoProcessor, Qwen3_5ForConditionalGeneration

from llmcompressor import oneshot
from llmcompressor.modifiers.gptq import GPTQModifier
from llmcompressor.modifiers.transform.imatrix import IMatrixGatherer
from llmcompressor.utils import load_context

MODEL_ID = "Qwen/Qwen3.6-27B"
SCHEME = "NVFP4A16"
NUM_CALIBRATION_SAMPLES = 512
MAX_SEQUENCE_LENGTH = 8192
IGNORE = [
    "re:.*lm_head.*",
    "re:.*embed_tokens.*",
    "re:model.visual.*",
    "re:.*mlp.gate.*",
    "re:.*linear_attn.*",
]

scheme = preset_name_to_scheme(SCHEME, ["Linear"])
scheme.weights.observer = "imatrix_mse"

with load_context(Qwen3_5ForConditionalGeneration):
    model = Qwen3_5ForConditionalGeneration.from_pretrained(MODEL_ID)
processor = AutoProcessor.from_pretrained(MODEL_ID)

recipe = [
    IMatrixGatherer(targets="Linear", ignore=IGNORE),
    GPTQModifier(config_groups={"group_0": scheme}, ignore=IGNORE),
]

ds = load_dataset(
    "HuggingFaceH4/ultrachat_200k",
    split=f"train_sft[:{NUM_CALIBRATION_SAMPLES}]",
)
ds = ds.select_columns(["messages"])
ds = ds.shuffle(seed=42)


def preprocess_function(example):
    messages = [
        {"role": m["role"], "content": [{"type": "text", "text": m["content"}]}
        for m in example["messages"]
    ]
    return processor.apply_chat_template(
        messages,
        tokenize=True,
        return_dict=True,
        add_generation_prompt=False,
        processor_kwargs={
            "return_tensors": "pt",
            "padding": False,
            "truncation": True,
            "max_length": MAX_SEQUENCE_LENGTH,
            "add_special_tokens": False,
        },
    )


ds = ds.map(preprocess_function, batched=False, remove_columns=ds.column_names)


def data_collator(batch):
    assert len(batch) == 1
    return {key: torch.tensor(value) for key, value in batch[0].items()}


oneshot(
    model=model,
    recipe=recipe,
    pipeline="sequential",
    dataset=ds,
    max_seq_length=MAX_SEQUENCE_LENGTH,
    num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    shuffle_calibration_samples=False,
    data_collator=data_collator,
)
```

The first sequential subgraph calibrates successfully, but the second subgraph fails immediately.

## Expected behavior
The sequential pipeline should complete all subgraphs without crashing, and the importance matrix gathered by `IMatrixGatherer` should be available to the `imatrix_mse` weight observer used by `GPTQModifier`.

## Actual behavior
Calibration fails on the first forward of the second subgraph:

```text
(2/65): Calibrating:   0%|          | 0/512 [00:00<?, ?it/s]
Traceback (most recent call last):
  ...
  File ".../llmcompressor/observers/imatrix.py", line 108, in _hook
    mod._imatrix_sum = mod._imatrix_sum.to(device)
                       ^^^^^^^^^^^^^^^^
AttributeError: 'Linear' object has no attribute '_imatrix_sum'. Did you mean: '_imatrix_hook'?
```

## Root cause
`IMatrixMSEObserver.attach` has two code paths:

1. **First attach** (e.g. `IMatrixGatherer.on_initialize`): creates `_imatrix_sum` and `_imatrix_count` directly on the `Linear` module and registers a forward-pre hook that updates those module attributes.
2. **Second attach** (e.g. `GPTQModifier.on_calibration_start`): when it sees `_imatrix_sum` already on the module, it copies them into the observer, deletes them from the module, and returns **without removing the previously registered hook**.

In `pipeline="sequential"`, the first hook is still active when the second observer attaches. The old hook fires for modules in later subgraphs, but `_imatrix_sum` has already been deleted from the module, causing the `AttributeError`.

This was verified by instrumenting `IMatrixMSEObserver.attach`:

- First attach: `has_sum=False has_hook=False` → creates `_imatrix_sum` + hook.
- Second attach: `has_sum=True has_hook=True` → copies sum, deletes it from module, leaves stale hook.
- Crash: `[IMATRIX HOOK ERROR] ... has_hook=True` on the module that lost `_imatrix_sum`.

## Proposed fix
In `src/llmcompressor/observers/imatrix.py`, when `attach` finds an existing `_imatrix_sum` and an active hook (sequential mode), it should:

1. Copy the accumulators to the observer.
2. Remove the stale hook from the module.
3. Re-register a hook that accumulates into the observer's own buffers (`self._imatrix_sum`) so importance collection continues until the module is actually observed/quantized.

`detach` should also move accumulators back to the module if they live on the observer, preserving the existing cleanup contract.

A patch that resolves the crash is shown below. It removes the stale hook when an existing accumulator is taken over, re-registers accumulation on the observer's own buffers, and moves accumulators back to the module in `detach` so the existing cleanup contract is preserved.

```diff
diff --git a/src/llmcompressor/observers/imatrix.py b/src/llmcompressor/observers/imatrix.py
index b653d5f..833623d 100644
--- a/src/llmcompressor/observers/imatrix.py
+++ b/src/llmcompressor/observers/imatrix.py
@@ -71,13 +71,22 @@ class IMatrixMSEObserver(Observer):
 
         If raw accumulators (``_imatrix_sum`` / ``_imatrix_count``) already
         exist on the module (second pass after IMatrixGatherer), copy them
-        to the observer and skip hook registration.
+        to the observer. When the previous observer's hook is still active
+        (e.g. the sequential pipeline), remove it and re-register on this
+        observer so accumulation continues into ``self._imatrix_sum``.
         """
         if hasattr(module, "_imatrix_sum"):
             self._imatrix_sum = module._imatrix_sum
             self._imatrix_count = module._imatrix_count
             del module._imatrix_sum
             del module._imatrix_count
+
+            # Sequential pipeline: the gatherer hook is still active. Transfer
+            # it to this observer so calibration keeps accumulating importance.
+            if hasattr(module, "_imatrix_hook"):
+                module._imatrix_hook.remove()
+                del module._imatrix_hook
+                self._register_hook(module, on_self=True)
             return
 
         if not hasattr(module, "in_features"):
@@ -86,6 +95,15 @@ class IMatrixMSEObserver(Observer):
         in_features = module.in_features
         module._imatrix_sum = torch.zeros(in_features, dtype=IMATRIX_PRECISION)
         module._imatrix_count = torch.tensor(0, dtype=torch.int64)
+        self._register_hook(module, on_self=False)
+
+    def _register_hook(self, module: torch.nn.Module, on_self: bool) -> None:
+        """Register a forward-pre hook that accumulates E[x²].
+
+        :param module: module whose inputs are being observed
+        :param on_self: if True, accumulate into this observer's buffers;
+            otherwise accumulate directly on the module
+        """
 
         def _hook(mod, args):
             if (
@@ -105,11 +123,16 @@ class IMatrixMSEObserver(Observer):
             n_tokens = math.prod(x_f.shape[:-1])
             token_sum = x_f.pow(2).sum(dim=list(range(x_f.dim() - 1)))
 
-            mod._imatrix_sum = mod._imatrix_sum.to(device)
-            mod._imatrix_count = mod._imatrix_count.to(device)
-
-            mod._imatrix_sum.add_(token_sum)
-            mod._imatrix_count += n_tokens
+            if on_self:
+                self._imatrix_sum = self._imatrix_sum.to(device)
+                self._imatrix_count = self._imatrix_count.to(device)
+                self._imatrix_sum.add_(token_sum)
+                self._imatrix_count += n_tokens
+            else:
+                mod._imatrix_sum = mod._imatrix_sum.to(device)
+                mod._imatrix_count = mod._imatrix_count.to(device)
+                mod._imatrix_sum.add_(token_sum)
+                mod._imatrix_count += n_tokens
 
         module._imatrix_hook = module.register_forward_pre_hook(_hook)
 
@@ -119,12 +142,19 @@ class IMatrixMSEObserver(Observer):
         Case 1 – accumulators present on module: leave them for next
         observer's ``attach()`` to pick up.
 
-        Case 2 – no accumulators (second-pass cleanup): nothing to do.
+        Case 2 – accumulators live on this observer: move them back to the
+        module so downstream cleanup can find them.
+
+        Case 3 – no accumulators (second-pass cleanup): nothing to do.
         """
         if hasattr(module, "_imatrix_hook"):
             module._imatrix_hook.remove()
             del module._imatrix_hook
 
+        if self._imatrix_sum is not None and not hasattr(module, "_imatrix_sum"):
+            module._imatrix_sum = self._imatrix_sum
+            module._imatrix_count = self._imatrix_count
+
     # ------------------------------------------------------------------
 
     def update_statistics_from_observed(self, observed: torch.Tensor) -> None:
```

This has been tested locally against `Qwen/Qwen3.6-27B` with the sequential pipeline; calibration proceeds past the previously failing subgraph.


### 🛠️ Steps to reproduce

_No response_

## 评论 (2)

### brian-dellabetta · 2026-07-13

Hi @verdverm , I believe your issue would be resolved by #2698 (one of the accompanying PRs at least). There are a few out, i will raise internally and try to get that in

### verdverm · 2026-07-14

Yeah, that looks like the cleaner / correct solution if IMatrix is an observer vs gatherer. I will let my agent keep patching the site-packages until the merge and a release lands 🙈 
