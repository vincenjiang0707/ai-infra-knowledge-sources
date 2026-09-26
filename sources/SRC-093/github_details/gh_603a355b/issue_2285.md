# [Issue #2285] KV event decoder drops group_idx/medium/lora_name, breaking prefix matching for hybrid and multi-tier models

source: https://github.com/vllm-project/aibrix/issues/2285
state: open | updated: 2026-08-20T04:59:35Z
labels: kind/bug, area/gateway

## 正文

### Describe the bug

Our ZMQ decoder reads only the first four positional fields of vLLM's `BlockStored` (block_hashes, parent_block_hash, token_ids, block_size) and drops the rest. Upstream `BlockStored` (`vllm/distributed/kv_events.py`) now also carries `medium`, `lora_name`, `extra_keys`, and `group_idx`. Two of these affect correctness:

- `group_idx`: hybrid-attention models (sliding-window + full layers — Gemma, Ministral, Llama-4) hash the same token range into different KV-cache groups. Collapsing all groups into one hash space can produce false prefix matches.
- `medium`: with KV offloading, blocks live on CPU/remote tiers, but we count every block as a GPU hit, so prefix routing over-credits pods that only hold the prefix on a slower tier.

`lora_name` is also the canonical adapter id (`lora_id` is deprecated upstream); `prefix_cache.go` currently passes `loraID=-1` everywhere, so adapters aren't isolated in the index.

Relevant: `pkg/cache/kvcache/msgpack_decoder.go` (`parseEventArray`), `pkg/plugins/gateway/algorithms/prefix_cache.go`.

### Steps to Reproduce

1. Serve a hybrid-attention model (e.g. `google/gemma-2-9b-it`) with `--kv-events-config` enabled.
2. Send shared-prefix traffic across ≥2 replicas with the kv-event prefix router.
3. Observe requests routed to pods that don't actually have a GPU prefix hit.

### Expected behavior

Decoder parses `group_idx`/`medium`/`lora_name`; the index keys prefix entries by `(model, lora_name, group_idx)` and scores non-GPU mediums lower.

### Environment

AIBrix: main · vLLM: main (kv-events enabled).


## 评论 (2)

### pjdurden · 2026-06-21

Picking this up. Plan to split it so the keying change can be reviewed on its own:

PR1 (decoder + types): parseEventArray reads lora_id/medium/lora_name/group_idx (msgspec positions 5-9, bounds-checked so older vLLM arrays still decode) and BlockStoredEvent carries them, with decoder tests against the raw vLLM array layout. No routing/keying change, just stops dropping the fields.

PR2 (keying + scoring): key prefix entries by (model, lora_name, group_idx) and score non-GPU mediums lower, plumbing the fields through the kvevent handler into the indexer. That changes the MatchPrefix/AddPrefix signature across the indexers, so I would rather land it after PR1 and once you have looked at the keying approach.

Will open PR1 shortly. Happy to do it as one PR if you prefer.

### wuyan-zs · 2026-08-20

Found a larger compatibility break while working on this: **the decoder cannot decode current vLLM payloads at all.**

## The wire format changed under us

vLLM switched KV event encoding from positional arrays to **msgpack maps** in [vllm-project/vllm#42892](https://github.com/vllm-project/vllm/pull/42892) (merged 2026-06-09). `BlockStored`/`BlockRemoved` are now flat maps with a `type` key:

```json
{"type": "BlockStored", "block_hashes": [...], "parent_block_hash": null, "token_ids": [...], "block_size": 4, "lora_id": null, "medium": "GPU", "lora_name": null, "extra_keys": null, "group_idx": 1}
```

The current `DecodeEventBatch` unmarshals into a `[ts, events]` positional-array shape, so **every** map payload fails: `msgpack: invalid code=0x88 decoding array length` (verified against byte-exact payloads produced by the real `msgspec` encoder). The legacy publisher also sent ONE event per ZMQ message (tag-first array, no `[ts, events]` wrapper), so the batch assumption never matched the real wire format for either encoding.

## Fix (PR [#2587](https://github.com/vllm-project/aibrix/pull/2587))

1. **Decoder** — `DecodeEventBatch` now accepts all three shapes: map single event (current vLLM), tag-first array single event (legacy vLLM), and `[ts, events]` batch (older code paths / aibrix's own test encoder). All `BlockStored`/`BlockRemoved` fields are parsed: `lora_id`, `medium`, `lora_name`, `extra_keys`, `group_idx`, `kv_cache_spec_kind`, `kv_cache_spec_sliding_window`, `locality`.
2. **Tier-aware scoring** — `syncprefixcacheindexer` records the storage `medium` per (prefix, pod) and weights `MatchPrefix` scores (GPU=1.0, CPU=0.5, STORAGE=0.25; unspecified keeps full score for backward compat), covering the "score non-GPU mediums lower" half of this issue.
3. **Plumbing** — `medium`/`lora_name`/`group_idx` are carried through the `kvevent` handler and `store_providers` adapter (previously dropped at the handler).

Tests decode against **byte-exact msgspec-generated payloads** for both formats; existing tests keep passing.

## Open question: (model, lora_name, group_idx) index keying

The remaining half of this issue (keying the index by `(model, lora_name, group_idx)`) needs a request-side adapter id: `types.RoutingContext` has no LoRA/group field today and `prefix_cache.go` hardcodes `loraID = -1`. Before changing the `ModelContext` key (touches ~70 call sites), how should the request's adapter id be propagated (header? model-name convention?), and should `group_idx` be folded into the index key or into the hash? Happy to implement either direction as a follow-up.
