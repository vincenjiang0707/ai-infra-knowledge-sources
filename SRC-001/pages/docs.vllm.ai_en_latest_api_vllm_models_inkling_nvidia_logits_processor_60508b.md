source: https://docs.vllm.ai/en/latest/api/vllm/models/inkling/nvidia/logits_processor/
lastmod: 2026-09-23

#

`vllm.models.inkling.nvidia.logits_processor`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor)

Inkling logits processor (muP + LoRA aware).

Inkling divides the final logits by a muP width multiplier (`logits_mup_width_multiplier`

). This applies it two ways, depending on whether an lm_head LoRA is attached:

- No LoRA: fold
`1/mup`

into the lm_head GEMM alpha (fp32 epilogue) -- no separate elementwise kernel, no extra rounding, no weight mutation. - LoRA attached: the LoRA manager wraps this layer in
`LogitsProcessorWithLoRA`

, whose`forward`

calls`type(base_layer).forward(self=wrapper)`

-- so this`forward`

runs with`self`

bound to the wrapper. We detect that via`base_layer`

and take the LoRA path: run the wrapper's`_get_logits`

(base logits + the lm_head LoRA delta), then divide the full logits by the multiplier so the delta is scaled too. muP thus composes with the LoRA delta, with the dispatch as the only model-side branching.

Classes:

-
–[InklingLogitsProcessor](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor)`LogitsProcessor`

that applies Inkling's muP logits width multiplier.

##

`InklingLogitsProcessor`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor)

Bases: [LogitsProcessor](https://docs.vllm.ai/model_executor/layers/logits_processor/#vllm.model_executor.layers.logits_processor.LogitsProcessor)

`LogitsProcessor`

that applies Inkling's muP logits width multiplier.

Parameters:

-

(`vocab_size`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor(vocab_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Padded vocabulary size.

-

(`org_vocab_size`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor(org_vocab_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)| None`None`

) –Unpadded vocabulary size (defaults to

`vocab_size`

). -

(`scale`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor(scale))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`1.0`

) –Base logits scale (kept

`1.0`

for the served checkpoint). -

(`logits_as_input`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor(logits_as_input))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Whether the input is already logits.

-

(`soft_cap`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor(soft_cap))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –Optional logit soft cap (

`None`

for the served checkpoint). -

(`logits_mup_width_multiplier`

[¶](https://docs.vllm.ai#vllm.models.inkling.nvidia.logits_processor.InklingLogitsProcessor(logits_mup_width_multiplier))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)| None`None`

) –muP width divisor for the final logits;

`None`

or`0`

disables it.

## Source code in `vllm/models/inkling/nvidia/logits_processor.py`


|
|