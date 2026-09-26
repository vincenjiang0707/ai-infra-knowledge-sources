source: https://docs.nvidia.com/dynamo/zh-CN/reference/api/python/logits_processing
lastmod: 2026-09-23T23:30:39.914Z

dynamo.logits_processing


dynamo.logits_processing

`dynamo.logits_processing`

publishes 4 classes and 0 functions. Source: `lib/bindings/python/src/dynamo/logits_processing/__init__.py`


###### BaseLogitsProcessor (class)


Protocol for logits processors in Dynamo.

All logits processors must implement this interface to be compatible with backend adapters (TRT-LLM, vLLM, SGLang).

`lib/bindings/python/src/dynamo/logits_processing/base.py#L16`


###### ForcedSequenceLogitsProcessor (class)


Forces the next `len(token_ids)`

outputs, then EOS thereafter.

Stateful: keeps a position counter (`state`

) advanced each step.
Must be instantiated per request so concurrent streams don’t mix
positions.

`lib/bindings/python/src/dynamo/logits_processing/examples/forced_sequence.py#L19`


**Public methods**

**init**

No summary available.

###### HelloWorldLogitsProcessor (class)


Sample Logits Processor that always outputs a hardcoded response (`RESPONSE`

), no matter the input.

Thin wrapper over `ForcedSequenceLogitsProcessor`

: resolves the
forced token IDs from the tokenizer at construction time, then
reuses the shared forced-sequence masking and per-request state.

`lib/bindings/python/src/dynamo/logits_processing/examples/hello_world.py#L11`


**Public methods**

**init**

No summary available.

###### TemperatureProcessor (class)


Example logits processor that applies temperature scaling.

This is a simple demonstration of how to implement a logits processor that can be used with any Dynamo backend.

`lib/bindings/python/src/dynamo/logits_processing/examples/temperature.py#L11`


**Public methods**

**init**

Args: temperature: Scaling factor. Higher values make distribution more uniform, lower values make it more peaked. Must be positive.