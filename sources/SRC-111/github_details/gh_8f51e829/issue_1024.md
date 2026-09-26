# [Issue #1024] Support loading pre-generated multi-turn conversation datasets from file

source: https://github.com/vllm-project/guidellm/issues/1024
state: open | updated: 2026-09-09T19:33:47Z
labels: 

## 正文

## Summary

guidellm can generate multi-turn conversation datasets in-memory via `SyntheticTextDataset` and serialize each conversation as a dict containing a `conversation_turns` key (a `ConversationGraphData` payload with `graph_id` and `turns`). However, there is no way to **load these serialized conversations back from a JSONL file** using the existing `json_file` deserializer.

This means:
- You cannot pre-generate a multi-turn dataset, save it, and replay the same dataset across multiple benchmark runs for reproducibility.
- Large datasets with many turns (e.g. 540-turn agentic workloads with 160K first-prompt tokens) take a long time to generate — being able to generate once and reuse would save significant time.
- External tooling that generates conversation datasets in guidellm's own format has no way to feed them back.

## Current behavior

1. `SyntheticTextDataset` yields dicts like:
```json
{
  "conversation_turns": {
    "graph_id": "abc123",
    "turns": [
      {"node_id": "turn_0", "agent_id": "default", "parents": [], "columns": {"text_column": [...], "prompt_tokens_count_column": [...], "output_tokens_count_column": [...]}},
      {"node_id": "turn_1", "agent_id": "default", "parents": [{"parent_node_id": "turn_0", "history_context": "full"}], "columns": {...}}
    ]
  }
}
```

2. Saving these to a JSONL file (one JSON object per line) creates a valid file.

3. Loading that file with `--data 'kind=json_file,path=dataset.jsonl'` goes through `JSONFileDatasetDeserializer` → HuggingFace `load_dataset("json", ...)` → flat `Dataset` rows. Each row has a `conversation_turns` column but the `generative_column_mapper` doesn't know how to handle it as a pre-built graph — it expects flat columns (`text_column`, `prompt_tokens_count_column`, etc.) or needs a `conversation_turns_column` mapping that preserves the nested structure through the HuggingFace Dataset layer.

## Expected behavior

A new deserializer kind (e.g. `conversation_file`) or an enhancement to the existing `json_file` deserializer that:

1. Reads a JSONL file where each line is a JSON object containing a `conversation_turns` key
2. Parses each line's `conversation_turns` into a `ConversationGraphData` object
3. Yields them in a format compatible with `turns_from_mapped_items()` in `conversation_graph.py` (which already handles `conversation_turns_column`)

This would close the loop: generate → serialize → deserialize → benchmark with the same data.

## Use case

We run large-scale agentic inference benchmarks (e.g. Nemotron-3-Ultra-550B with 30-540 turn conversations, 160K first-prompt tokens, 3K shared prefix, inter-turn delays). Generating these datasets takes 5-15 minutes with multiprocessing. Being able to pre-generate once and replay across different cluster configurations, concurrency levels, and P/D splits would significantly improve reproducibility and iteration speed.

## Suggested approach

A `conversation_file` deserializer that:
- Accepts `kind=conversation_file,path=dataset.jsonl`
- Reads line-by-line, parses each JSON object
- Extracts the `conversation_turns` value and validates it as `ConversationGraphData`
- Returns an iterable of dicts with `conversation_turns_column` set, compatible with the existing `turns_from_mapped_items()` pipeline

This keeps the existing finalizer/graph infrastructure unchanged — only the deserialization layer needs the new entry point.

## 评论 (2)

### LOGO127 · 2026-09-08

I reproduced a specific failure on current main `fc2dbe9edd4f7f1a4e9ccd752f6f43591adbcb73`. The default mapper already recognizes `conversation_turns`; uniformly shaped graph payloads can round-trip. The failing case is heterogeneous turn columns passing through the Arrow-backed JSON loader.

For example, with `{"text_column": ["first"]}` on the root and `{"text_column": ["second"], "output_tokens_count_column": [7]}` on its child, loading the nested graph adds `output_tokens_count_column: None` to the root. `GenerativeRequestFinalizer` then raises `TypeError: 'NoneType' object is not iterable`. Prefix/image/audio column containers have the same failure. The test loads actual JSONL and calls the mapper and full graph finalizer, without a model/tokenizer mock replacing those components.

I have a local candidate that treats top-level null column containers as absent in `ConversationTurnData` validation. It preserves nested nulls, empty lists and zero counts, and does not introduce a new file format or special-case the generic loader. Would that bounded normalization policy be appropriate here?

Validation so far:
- Identical 16-case, two-row JSONL integration suite: unmodified main **8 failed / 8 passed**; candidate **16 passed**. Covers streaming/nonstreaming dataset loading, nested/string graph payloads, settings and runtime dependency edges. All eight baseline failures reach the actual finalizer.
- Candidate unit suite: **3032 passed, 31 skipped, 163 xfailed**.
- Configured lint/import-layer checks and mypy pass.

This is an AI-assisted local candidate, not yet a submitted PR or a claim to cover every possible nested JSON schema. No live inference benchmark or GPU validation is claimed.


### LOGO127 · 2026-09-09

Update to my earlier reproduction: I rechecked clean main `8bdb96cd603c0c7f245569a815f81c5dd7cd260f` with its locked development dependencies, after #1092 merged. The identical 16-case JSONL integration probe now passes **without** my local null-container normalization patch. A same-process source-path assertion also passed, confirming the probe imported the clean current checkout rather than my older candidate (17 checks total).

This covers nested/string graph payloads, streaming/nonstreaming loading, heterogeneous token/prefix/image/audio column containers, two graph rows and runtime graph finalization. It is CPU data-path validation, not a live-model benchmark. I have not bisected the precise source/dependency change responsible, and this does not establish that every use case requested in #1024 is covered.

I'll set aside the proposed normalization patch rather than submit a fix whose original failure no longer reproduces on the current locked environment. The earlier red/green numbers apply only to the older snapshot. Thanks for the deserialization work; this recheck was performed with Codex assistance.

