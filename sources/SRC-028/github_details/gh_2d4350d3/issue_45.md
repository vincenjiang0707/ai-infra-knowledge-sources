# [Issue #45] Refactor jestream to allow different tokenizers

source: https://github.com/AI-Hypercomputer/JetStream/issues/45
state: open | updated: 2024-05-02T17:19:36Z
labels: 

## 正文

## Issue

Currently we assume few things in jetstream which hinders it's generalization:

1. tokenizer is SentencePiece based.
2. pad_id is 0
3. after encode, we pad to nearest power of 2
4. ResultToken itself is jax specific (the @struct.dataclass annotation requires it's Jax pytreeable).

These assumptions hinders generalization (i.e. support wider varieties of models). 
Examples:
1. llama3 uses tiktoken instead of SentencePiece
2. llama3 uses pad_id of -1
3. Pytorch GPU does NOT need to pad to nearst power of 2.
4. Pytorch GPU version of jetstream would like to use `torch.Tensor` to hold the data, which is not jax-pytreeable.

## Proposal:

1. `EngineAPI.get_tokenizer` which returns the tokenizer, should be any object that implements the following interface:

```
def encode

def decode

@property
def pad_id

@property
def eos_id
```
Uses of tokenizer should restrict to only this methods.

In particular: `encode` should do both encoding and padding. So jetstream doesnt do any padding itself; the engine can choose how to pad (or not to pad) by returning a custom tokenizer object whose encode also does the padding.

2. Allow use different implementation for `ResultTokens`; same as `Prefix` and `DecodeState`. Implementations of the Engine can choose implementation of ResultTokens. jestream should interact with it only through it's 3 public methods (https://github.com/google/JetStream/blob/main/jetstream/engine/engine_api.py#L83)

```python
def get_result_at_slot
def convert_to_numpy
def copy_to_host_async
```
and are not allowed to access it's fields directly.


## 评论 (1)

### bhavya01 · 2024-05-02

#53, #67 adds the interface for tokenizer. Still need to work on ResultTokens.
