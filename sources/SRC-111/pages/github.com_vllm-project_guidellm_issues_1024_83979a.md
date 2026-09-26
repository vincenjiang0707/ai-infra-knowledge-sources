source: https://github.com/vllm-project/guidellm/issues/1024

## Summary

guidellm can generate multi-turn conversation datasets in-memory via `SyntheticTextDataset`

and serialize each conversation as a dict containing a `conversation_turns`

key (a `ConversationGraphData`

payload with `graph_id`

and `turns`

). However, there is no way to **load these serialized conversations back from a JSONL file** using the existing `json_file`

deserializer.

This means:

- You cannot pre-generate a multi-turn dataset, save it, and replay the same dataset across multiple benchmark runs for reproducibility.
- Large datasets with many turns (e.g. 540-turn agentic workloads with 160K first-prompt tokens) take a long time to generate — being able to generate once and reuse would save significant time.
- External tooling that generates conversation datasets in guidellm's own format has no way to feed them back.

## Current behavior

`SyntheticTextDataset`

yields dicts like:

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

-
Saving these to a JSONL file (one JSON object per line) creates a valid file.

-
Loading that file with `--data 'kind=json_file,path=dataset.jsonl'`

goes through `JSONFileDatasetDeserializer`

→ HuggingFace `load_dataset("json", ...)`

→ flat `Dataset`

rows. Each row has a `conversation_turns`

column but the `generative_column_mapper`

doesn't know how to handle it as a pre-built graph — it expects flat columns (`text_column`

, `prompt_tokens_count_column`

, etc.) or needs a `conversation_turns_column`

mapping that preserves the nested structure through the HuggingFace Dataset layer.


## Expected behavior

A new deserializer kind (e.g. `conversation_file`

) or an enhancement to the existing `json_file`

deserializer that:

- Reads a JSONL file where each line is a JSON object containing a
`conversation_turns`

key
- Parses each line's
`conversation_turns`

into a `ConversationGraphData`

object
- Yields them in a format compatible with
`turns_from_mapped_items()`

in `conversation_graph.py`

(which already handles `conversation_turns_column`

)

This would close the loop: generate → serialize → deserialize → benchmark with the same data.

## Use case

We run large-scale agentic inference benchmarks (e.g. Nemotron-3-Ultra-550B with 30-540 turn conversations, 160K first-prompt tokens, 3K shared prefix, inter-turn delays). Generating these datasets takes 5-15 minutes with multiprocessing. Being able to pre-generate once and replay across different cluster configurations, concurrency levels, and P/D splits would significantly improve reproducibility and iteration speed.

## Suggested approach

A `conversation_file`

deserializer that:

- Accepts
`kind=conversation_file,path=dataset.jsonl`

- Reads line-by-line, parses each JSON object
- Extracts the
`conversation_turns`

value and validates it as `ConversationGraphData`

- Returns an iterable of dicts with
`conversation_turns_column`

set, compatible with the existing `turns_from_mapped_items()`

pipeline

This keeps the existing finalizer/graph infrastructure unchanged — only the deserialization layer needs the new entry point.

## Summary

guidellm can generate multi-turn conversation datasets in-memory via

`SyntheticTextDataset`

and serialize each conversation as a dict containing a`conversation_turns`

key (a`ConversationGraphData`

payload with`graph_id`

and`turns`

). However, there is no way toload these serialized conversations back from a JSONL fileusing the existing`json_file`

deserializer.This means:

## Current behavior

`SyntheticTextDataset`

yields dicts like:Saving these to a JSONL file (one JSON object per line) creates a valid file.

Loading that file with

`--data 'kind=json_file,path=dataset.jsonl'`

goes through`JSONFileDatasetDeserializer`

→ HuggingFace`load_dataset("json", ...)`

→ flat`Dataset`

rows. Each row has a`conversation_turns`

column but the`generative_column_mapper`

doesn't know how to handle it as a pre-built graph — it expects flat columns (`text_column`

,`prompt_tokens_count_column`

, etc.) or needs a`conversation_turns_column`

mapping that preserves the nested structure through the HuggingFace Dataset layer.## Expected behavior

A new deserializer kind (e.g.

`conversation_file`

) or an enhancement to the existing`json_file`

deserializer that:`conversation_turns`

key`conversation_turns`

into a`ConversationGraphData`

object`turns_from_mapped_items()`

in`conversation_graph.py`

(which already handles`conversation_turns_column`

)This would close the loop: generate → serialize → deserialize → benchmark with the same data.

## Use case

We run large-scale agentic inference benchmarks (e.g. Nemotron-3-Ultra-550B with 30-540 turn conversations, 160K first-prompt tokens, 3K shared prefix, inter-turn delays). Generating these datasets takes 5-15 minutes with multiprocessing. Being able to pre-generate once and replay across different cluster configurations, concurrency levels, and P/D splits would significantly improve reproducibility and iteration speed.

## Suggested approach

A

`conversation_file`

deserializer that:`kind=conversation_file,path=dataset.jsonl`

`conversation_turns`

value and validates it as`ConversationGraphData`

`conversation_turns_column`

set, compatible with the existing`turns_from_mapped_items()`

pipelineThis keeps the existing finalizer/graph infrastructure unchanged — only the deserialization layer needs the new entry point.