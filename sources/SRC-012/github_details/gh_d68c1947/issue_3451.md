# [Issue #3451] [Feature Request] Tracking first-class embedding serving path in MLC-LLM

source: https://github.com/mlc-ai/mlc-llm/issues/3451
state: open | updated: 2026-08-31T01:03:34Z
labels: feature request

## 正文

## Feature

Introduce a first-class embedding serving/runtime path in MLC LLM.

The current `/v1/embeddings` API support is already in place, but the execution path is still relatively lightweight and does not yet have a dedicated embedding runtime/serving architecture underneath. I would like to propose making embedding a more explicit and general path inside MLC LLM, while keeping the normal chat model serving path unchanged.

The goal is to support embedding models more naturally inside MLC LLM, instead of treating embedding inference mainly as a thin serving wrapper on top of the existing runtime assumptions.

## Motivation

I have been working on local agent-style systems recently, and that made me look more closely at the embedding path in MLC LLM.

For agent workloads, embedding is a core primitive for retrieval, memory, indexing, and ranking. In practice, embedding latency and throughput can matter just as much as generation performance. Part of why I want to build on MLC LLM is that it is a hardware-aware local serving stack, so it seems like a good place to support more optimized embedding serving as well.

Earlier, I contributed some of the initial `/v1/embeddings` support. At the time, because of time and engineering scope, I intentionally kept the implementation lightweight. That was enough to establish the API contract, but it did not yet introduce a task-specific embedding serving engine or a first-class embedding execution path.

From my current understanding, the main gap is no longer the API itself, but that embedding is still not modeled as a first-class serving/runtime path. This makes it harder to:
- support both encoder and decoder-only embedding models cleanly
- introduce optimizations that depend on embedding model structure
- add backend-specific optimizations in a general way later
- keep the embedding stack aligned with the broader serving/runtime architecture of MLC LLM

This proposal is intended to be aligned with the earlier tracking issue for generic sentence embedding models in MLCEngine: #2324.

## Additional context

My current implementation plan is to break this into several smaller steps instead of trying to do everything in one PR:

1. Metadata abstraction  
   Branch: `feature/embedding/metadata-abstraction`  
   Make embedding traits explicit in metadata/config instead of relying on function-name-based detection.

2. Dedicated TVM-native embedding runtime  
   Branch: `feature/embedding/runtime-tvm-native`  
   Introduce a clearer embedding runtime boundary while keeping the existing TVM-native path as the default implementation.

3. First-class encoder embedding path  
   Branch: `feature/embedding/encoder-first-class`  
   Make encoder embedding models first-class, instead of relying on Python-side pooling/runtime glue.

4. First-class decoder-only embedding path (starting from qwen3-embedding)  
   Branch: `feature/embedding/decoder-first-class-qwen3`  
   Start with qwen3-embedding as the first concrete decoder-only embedding family, while keeping the overall design general.

5. Backend registry for future hardware-specific optimization  
   Branch: `feature/embedding/backend-registry`  
   Add a cleaner extension point for backend-specific optimization later.

A few important non-goals for the initial stages:
- no change to the `/v1/embeddings` API contract
- no disruption to the normal chat model serving path
- no requirement to solve every backend/hardware-specific optimization in the first step

If this direction sounds reasonable, I plan to use this issue as the main tracking thread and link the staged PRs back here.


## 评论 (4)

### MasterJH5574 · 2026-03-13

@xthomaswang Thanks for the tracking issue and the proposed plan! The plan looks solid to me.

My only comment at this moment is that, it might better help understand if we can have some code/command example of the final goal. For example, what command to use to serve an embedding model, how to send request with python (or in command line), and what output we expect to see. My understanding is that it's mostly following `/v1/embeddings`, but I just would love to have more clarity here in this issue.

### xthomaswang · 2026-03-13

Thanks for the suggestion — I agree that a concrete end-to-end example would make the goal much easier to understand.

At the user-facing level, my expectation is still that embedding follows the standard OpenAI-compatible `/v1/embeddings` flow. 

## Expected final goal

For example, using `Qwen3-Embedding-0.6B`:

### 1. Convert weights

```bash
mlc_llm convert_weight ./path/to/Qwen3-Embedding-0.6B \
  --quantization q0f32 \
  --model-type qwen3-embedding \
  -o ./dist/Qwen3-Embedding-0.6B-q0f32-MLC
```

### 2. Generate config

```bash
mlc_llm gen_config ./path/to/Qwen3-Embedding-0.6B \
  --quantization q0f32 \
  --model-type qwen3-embedding \
  --conv-template qwen2 \
  -o ./dist/Qwen3-Embedding-0.6B-q0f32-MLC
```

### 3. Compile

```bash
mlc_llm compile ./path/to/Qwen3-Embedding-0.6B-q0f32-MLC/mlc-chat-config.json \
  --model-type qwen3-embedding \
  --device metal \
  -o ./dist/libs/Qwen3-Embedding-0.6B-q0f32-metal.dylib
```

### 4. Serve the embedding model

```bash
mlc_llm serve ./path/to/Qwen3-Embedding-0.6B-q0f32-MLC \
  --model-lib ./dist/libs/Qwen3-Embedding-0.6B-q0f32-metal.dylib \
  --host 127.0.0.1 \
  --port 8000
```

### 5. Request in Python

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="none")

resp = client.embeddings.create(
    model="Qwen3-Embedding-0.6B-q0f32-MLC",
    input=["text1", "text2"],
)

print(len(resp.data))
print(len(resp.data[0].embedding))
print(resp.usage)
```

### 6. with curl

```
curl http://127.0.0.1:8000/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen3-Embedding-0.6B-q0f32-MLC",
    "input": ["hello world", "goodbye world"]
  }'
```

Expected response format (OpenAI-compatible):

```
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [ ... ]
    },
    {
      "object": "embedding",
      "index": 1,
      "embedding": [ ... ]
    }
  ],
  "model": "Qwen3-Embedding-0.6B-q0f32-MLC",
  "usage": {
    "prompt_tokens": 6,
    "total_tokens": 6
  }
}
```

So from the API perspective, I expect the external contract to remain `/v1/embeddings`; the main change is that embedding becomes a first-class serving/runtime path internally.

## Multi-model direction (additional thougts)

A related part of the end goal is to make multi-model serving simpler and more uniform.

What I would ultimately like is a single `serve` entrypoint where the engine reads each model's config/metadata and automatically determines whether it is a chat model or an embedding model, instead of requiring separate CLI concepts such as `--embedding-model` or `--additional-models`.

For example, something along the lines of:

```bash
mlc_llm serve \
  ./path/to/Qwen3.5-0.8B-q4f16_1-MLC \
  ./path/to/bge-m3-q0f32-MLC \
  ./path/to/Qwen3-Embedding-0.6B-q0f32-MLC
```

Then the server would register them in order and print a routing table such as:

```text
Served models: 1 chat model, 2 embedding models
  [chat]  Qwen3.5-0.8B-q4f16_1-MLC
  [embed] bge-m3-q0f32-MLC
  [embed] Qwen3-Embedding-0.6B-q0f32-MLC
```

In that design:
- `/v1/chat/completions` would route to served chat models
- `/v1/embeddings` would route to served embedding models
- the request-side `model` field would continue to follow the current OpenAI-compatible style, i.e. using the served model name
- `/v1/models` would list the currently served models

I hope no one serve same model multiple times, if that happen maybe need to give each model a specific id like 
chat 'c1' 'c2' 
emb 'e1' 'e2'



### xthomaswang · 2026-08-31

## Status update(2026-08)

### Merged so far

- #3430 — `/v1/embeddings` endpoint + `AsyncEmbeddingEngine` (merged): encoder and decoder-only (Qwen3-Embedding) support behind the OpenAI-compatible API
- #3436 — greedy sub-batching for decoder embedding within `prefill_chunk_size` (merged)
- #3452 — **Phase 1: metadata abstraction** (merged): embedding traits (`model_task`, pooling strategy, normalize) are now explicit in metadata/config instead of relying on function-name-based detection

### Still open
- #3461 / #3481 / #3488 — Phase 2/3/4 as originally scoped are open, but have gone stale against main (now conflicting after the TVM runtime / tvm-ffi / tirx refactors landed in May–July)

### Problem 
- Hard to review with so many conflict and code changes.
- Following Phase change could cause older version Incompatible problem, away from original plan.
- Should make abstraction useful when actual performance change observed which is the core motivation of this proposal.

Combined above problems, I am thinking to revise the plan to avoid any potential conflict and let performance driven first. 


## Revised plan (2026-08)

### Phase 2 (re-scoped) — single-task serving + serving-grade runtime

Split #3461 into two smaller non-breaking PRs:

- **Phase 2a — single-task serve**: `mlc_llm serve <embedding-model>` works directly. The server reads `model_task` from Phase-1 metadata and starts an embedding-only server (`/v1/embeddings`, `/v1/models`, health). `--embedding-model` / `--embedding-model-lib` still work with a deprecation notice; chat serve keeps `/v1/embeddings` unchanged.
- **Phase 2b — cross-request dynamic batching**: today `async_embed` runs on `ThreadPoolExecutor(max_workers=1)`, so concurrent requests are fully serialized — under agent-style load the GPU processes tiny batches one at a time. Add a request collector that coalesces concurrent requests into one GPU forward (token budget within `prefill_chunk_size`, or a short collection window). The PR will include before/after throughput numbers (e.g. bge-m3, Qwen3-Embedding-0.6B).

The `EmbeddingRuntime` abstraction from the original Phase 2 is deferred to Phase 3/4, where the C++ lanes actually need a boundary to slot in under.

### Phase 3 — first-class encoder path (deferred, gated on Phase 2b benchmarks)

Convert #3481 to draft for now. Re-propose the encoder C++ lane only if benchmarks still show headroom that Python-side batching cannot reach.

### Phase 4 — first-class decoder path (deferred, same gate)

Convert #3488 to draft for now. Same as above, re-proposed the decoder starting with qwen3-embedding, then expland to other family if needed. 

### Phase 5 — backend registry (superseded by TIRx)

Backend-specific optimization now should focus on mainline TVM's TIRx (hardware-native kernel DSL + the tirx-kernels library). If embedding-specific kernels (e.g. fused pooling + normalize) are important, I will think to contribute them along the TIRx path instead.


### xthomaswang · 2026-08-31

@MasterJH5574, here is the updated plan, and I will keep using this issue as the tracking thread.
