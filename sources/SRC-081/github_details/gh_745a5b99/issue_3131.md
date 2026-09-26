# [Issue #3131] Streaming Model Saving - Integrate Checkpoint Writing into Pipeline

source: https://github.com/vllm-project/llm-compressor/issues/3131
state: open | updated: 2026-09-08T06:54:49Z
labels: enhancement

## 正文

## Objective

Integrate model saving into the sequential pipeline so that a completed subgraph can be written directly to the output checkpoint instead of remaining part of a complete in-memory or offloaded model that is saved in a final model-wide pass.

## Current Behavior

All layers are processed and retained, then the entire model is saved in a separate pass:

```text
load / process / offload every layer
...
reload model state
→ save complete checkpoint
```

This creates unnecessary storage movement and retains finalized parameters longer than needed.

## Proposed Behavior

With layerwise compression in place, a subgraph is effectively finalized once:

1. Calibration has completed
2. All algorithms have been applied
3. The module has been compressed
4. No later operation requires its mutable parameter state

At this point, it should be written directly to the output checkpoint:

```text
load
→ linearize
→ calibrate
→ optimize
→ compress
→ save
→ release
```

## Proposed Implementation

```python
with StreamingCheckpointWriter(save_dir) as writer:
    for subgraph in subgraphs:
        process(subgraph)
        compress(subgraph)

        writer.write_subgraph(subgraph)

        release(subgraph)
```

## Open Questions & Challenges

- **Shard construction:** Hugging Face checkpoints split according to max shard size. Must incrementally fill shards and finalize as they reach target size.
- **Checkpoint index:** Final `*.safetensors.index.json` cannot complete until all tensors assigned to shards, but mapping can be accumulated incrementally.
- **Save mappings:** Some architectures transform/split/merge/rename parameters during serialization. These must be layer-local or explicitly declare dependencies.
- **Tied weights:** Shared/tied parameters require special handling to avoid duplicate serialization or premature tensor release.
- **Model metadata:** Config files, quantization metadata, generation config, tokenizer assets continue to be written independently.
- **Failure recovery:** Partially written checkpoints should be resumable or clearly marked incomplete.

## Expected Benefits

- Remove final model-wide save pass
- Reduce retained state in memory/on disk
- Improved overall processing efficiency
- Foundation for true single-pass pipeline processing

## 评论 (0)
