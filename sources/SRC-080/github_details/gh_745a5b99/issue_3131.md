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

## 评论 (1)

### LOGO127 · 2026-09-08

I'd like to help with this, subject to scope/assignment confirmation. I have not started a competing pipeline or writer implementation.

I checked the current save path at `8f96fe61feb501b98c2f1c61de2053b50f8d8534` and the streaming pipeline in #3111 at `5e2340078593fa991a884287de812de4f3667b66`. A few integration constraints seem important:

- `oneshot` finalizes the session after the pipeline returns; #3111 also materializes remaining/untraced modules before `calibration_end`. A traced-subgraph-only writer would not cover the complete model.
- `modify_save_pretrained` currently performs compression, re-ties value-identical input/output embeddings, delegates serialization to Transformers, updates quantization config/recipe, and copies MTP tensors absent from the loaded model. Streaming output needs to preserve these behaviors, not just write each subgraph's state dict.
- #3111 already covers adjacent staging/prefetch work but retains processed weights for final saving. I would prefer a shared, explicitly finalized-tensor/subgraph boundary over another streaming pipeline.

Would you want #3131 built on #3111, or should the finalized-output contract be shared with the existing sequential pipeline first? Is someone already handling the writer/save-mapping side privately?

If this is available, I can start with an RFC and real small-model serialization/reload parity tests: shard boundaries and oversized tensors, tied weights, untraced modules/buffers, save mappings, and injected save failures. The proposed complete feature would include bounded retention and an explicit incomplete-output/publication contract; a standalone writer utility would not by itself close this issue. We should agree on whether resumability is required versus safely marking failed outputs incomplete.

My local resources support CPU/small-model correctness work, not representative very-large-model GPU/storage benchmarking. That performance validation would need later collaboration. This investigation was AI-assisted; no runtime or performance results are claimed yet.

