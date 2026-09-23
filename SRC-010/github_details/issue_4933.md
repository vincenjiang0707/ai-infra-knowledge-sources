# [Issue #4933] [Bug] input_embeddings are omitted from prefix-cache identity, causing wrong KV reuse

source: https://github.com/InternLM/lmdeploy/issues/4933
state: open | updated: 2026-09-13T08:25:48Z
labels: 

## 正文

## Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

## Describe the bug

With PyTorch prefix caching enabled, `input_embeddings` content is not included in
the prefix-cache trie identity. Two requests can have identical token IDs and
embedding spans but different embedding values. The second request then reuses KV
computed from the first request's embeddings.

The relevant path is:

- `pytorch/messages.py:875-902`: `get_prefix_cache_extra_identity()` indexes
  `multimodal_spans`, but not embedding content.
- `pytorch/messages.py:954-962`: `_update_embeddings()` stores embeddings in
  `history_embeddings` without adding them to the trie key identity.
- `pytorch/messages.py:904-936`: embedding ranges are considered only for cache
  boundary safety; embedding content is not compared or hashed.
- `pytorch/engine/engine.py:496-513`: requests accept and propagate
  `input_embeddings`.
- `pytorch/models/qwen2.py:339-344`: the model replaces token embeddings with the
  supplied values before the forward pass.

Therefore, request 1 with embeddings `E1` can populate a cache entry that request 2
with the same token IDs and different embeddings `E2` treats as a valid hit. This is
a silent correctness bug: no exception is raised, and the output differs from a
cold computation using `E2`. Text-only requests without `input_embeddings` are not
affected by this specific path.

## Reproduction

Use the reproducer `f4_embeddings_demo.py` from the reporter's verification
checkout. It uses the production PyTorch engine and request path, with only the
`input_embeddings` field added to the upstream `ADD_MESSAGE` payload.

Requirements: a PyTorch-capable GPU, the Qwen2.5-0.5B-Instruct model (or an
equivalent supported model), and a checkout containing the code above. Set the
`MODEL` constant in the script to the local model path, then run:

```shell
python verify/f4_embeddings_demo.py
```

The script performs three runs with the same token IDs:

```text
run1: tokens + E1 (cold)
run2: tokens + E2=-E1 (identity-complete cache would MISS)
      prefix-cache hit; 448 tokens reused from run1
evict trie KV
run3: tokens + E2 (cold recompute)

O1 vs O3: first_diff=1 (E content matters)
O2 vs O3: first_diff=1
RESULT: EMBEDDINGS-BLIND REUSE CONFIRMED
```

`O2` is the warm result for `E2`, but it differs from the clean `E2` result `O3`,
proving that the hit reused KV computed from `E1`.

## Environment

The e2e reproduction was run on Linux with the PyTorch backend, prefix caching
enabled, `tp=1`, model `Qwen2.5-0.5B-Instruct`, and 8 NVIDIA RTX 3090 GPUs
available on the verification host. The recorded run used the `lmdeploy`
`0.16.0+` Python sources at commit `2928f477`; the same relevant path remains
unchanged in the current checkout checked above. Run `python -m lmdeploy check_env`
on the target host for the complete environment.

## Error traceback

None. The incorrect cache hit and output difference are silent.

## Identified reason and suggested fix

Include an identity for every embedding span, such as `(start, end,
hash(embedding content))`, in the prefix-cache key. The matching logic must use the
same embedding-aware identity, and a regression test should verify that same-token
requests with different embedding values miss the cache and match their respective
cold outputs.


## 评论 (2)

### modelpath-dev · 2026-09-10

I will take this issue. Please assign it to me.

The bug seems to be that `input_embeddings` are not included in the prefix-cache identity, leading to incorrect KV reuse. I will first inspect `get_prefix_cache_extra_identity()` in `pytorch/messages.py` to ensure it indexes the embedding content. Then, I'll check `_update_embeddings()` to see how embeddings are stored without affecting the trie key identity. A small fix would involve modifying these functions to incorporate embedding content into the cache identity. I will verify the fix using the provided `f4_embeddings_demo.py` script to ensure the cache behaves correctly with different embeddings.


### modelpath-dev · 2026-09-13

I am working on inspecting the functions mentioned to address the issue with the prefix-cache identity. I will update once I have a fix ready and tested with the `f4_embeddings_demo.py` script. Let me know if there are any additional details or considerations I should keep in mind.

