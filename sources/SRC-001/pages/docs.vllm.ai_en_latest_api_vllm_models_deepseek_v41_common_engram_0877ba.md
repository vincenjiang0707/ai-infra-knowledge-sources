source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/common/engram/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v41.common.engram`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram)

Engram: n-gram hash lookups gated into the hyper-connection stream.

Port of the reference `inference/engram.py`

+ `Engram`

/ `ParallelEngramEmbedding`

from `inference/model.py`

(DeepSeek V4.1 checkpoint layout). Engram modules live on the backbone layers listed in `engram_layer_ids`

only.

Two pieces of cross-forward state are needed because vLLM streams tokens chunk-by-chunk while an n-gram at position `p`

needs the token ids at `p-1..p-3`

:

`token_map`

: token id -> compressed vocab id, built once from the model's tokenizer at init (deterministic; asserted against`engram_compressed_vocab_size`

).`hash_cache`

: one int32 slot per KV slot of the first local layer's sliding-window cache, holding the compressed id (or DEAD) of the token last written to that slot. Slots are stable per (request, position) — the block table pins a position to a physical slot, prefix-cache hits reuse both the physical blocks and the identical token ids, and spec-decode rollbacks rewrite the same slots — so lookbacks read back exactly what the owning request wrote. Lookback depth (3) is far inside the sliding window (128), so window eviction never frees a block a live lookback still needs.

Slots are not part of the KV cache, so KV loaded from another instance (P/D, offload connectors) leaves them unwritten. The runner therefore passes `lookback_token_ids`

, the ids just before each request's chunk start, which take precedence over the slots. The V2 runner reads them from its device-resident token history and needs no slot cache; the V1 runner's CPU token table holds placeholders for generated tokens under async scheduling, so it passes prompt positions only and keeps the slot cache for the rest.

Classes:

-
–[Engram](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram)Writes an n-gram lookup into the residual stream, gated by how well it

-
–[EngramLayout](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.EngramLayout)Bucket layout of the n-gram hash tables.

-
–[NgramHashState](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState)Maps each position to the hash ids of the n-grams ending there.

-
–[ParallelEngramEmbedding](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding)TP-sharded hash heads with FP8 rows and per-block E8M0 scales.


Functions:

-
–[build_compressed_token_map](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.build_compressed_token_map)Map every token id onto a smaller id space where tokens that normalize

-
–[compute_hash_multipliers](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.compute_hash_multipliers)One multiplier per (layer, lookback), from a per-layer RNG so layers

-
–[find_next_prime](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.find_next_prime)The smallest prime above

`start`

that has not been handed out yet.

##

`Engram`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Writes an n-gram lookup into the residual stream, gated by how well it matches that stream.

The hash ids fetch `n_hash_cols`

rows; `wkv`

turns them into one key per hc copy plus a shared value. The gate is a normalized dot product of the stream against the key, signed-sqrt'ed before the sigmoid (matching the training kernel).

Methods:

-
–[embed](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram.embed)Gather heads, returning only local tokens when SP is enabled.

-
–[forward](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram.forward)hidden_states: [T, hc_mult, dim]; hash_ids: [T, n_hash_cols] (all

-
–[prepare_embeddings](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram.prepare_embeddings)Look up rows before the decoder layers consume them.


## Source code in `vllm/models/deepseek_v41/common/engram.py`


|
|

###

`embed(hash_ids)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram.embed)

Gather heads, returning only local tokens when SP is enabled.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


###

`forward(hidden_states, hash_ids, token_mask=None)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram.forward)

hidden_states: [T, hc_mult, dim]; hash_ids: [T, n_hash_cols] (all tokens, pre sequence-parallel shard); token_mask: [T], False shuts the gate so those positions pass through untouched.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


|
|

###

`prepare_embeddings(hash_ids)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.Engram.prepare_embeddings)

Look up rows before the decoder layers consume them.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`EngramLayout`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.EngramLayout)

Bucket layout of the n-gram hash tables.

A position is hashed as `max_ngram_size - 1`

n-grams (2-gram .. max), each split over `n_heads`

heads. Every (n-gram size, head) pair owns its own prime-sized bucket range in the layer's table; the primes are drawn in order and never reused, which keeps the ranges disjoint.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`NgramHashState`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Maps each position to the hash ids of the n-grams ending there.

Stateless on the V2 runner, which supplies every lookback token id. On the V1 runner it also keeps `hash_cache`

, the slot-keyed rolling store of compressed ids (see module docstring), for generated tokens.

Methods:

-
–[dummy_hashes](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState.dummy_hashes)Participate in DP lookups without valid rows or hash-cache updates.

-
–[ensure_cache](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState.ensure_cache)Lazily size the slot-keyed cache from the bound SWA KV cache.

-
–[forward](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState.forward)Compute [tokens, layers, hash columns] int32 n-gram hashes.


## Source code in `vllm/models/deepseek_v41/common/engram.py`


|
|

###

`dummy_hashes(input_ids)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState.dummy_hashes)

Participate in DP lookups without valid rows or hash-cache updates.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


###

`ensure_cache()`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState.ensure_cache)

Lazily size the slot-keyed cache from the bound SWA KV cache.

Returns False while the KV cache is unbound (profile run); the caller skips engram hashing then. Without the slot cache only that check remains.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


###

`forward(input_ids, positions, query_start_loc, dead_mask, lookback_token_ids, lookback_dead_mask, slot_mapping, block_table)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.NgramHashState.forward)

Compute [tokens, layers, hash columns] int32 n-gram hashes.

History comes from the current chunk, then the runner's lookback window, then the optional V1 slot cache. V2 needs only one launch.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


|
|

##

`ParallelEngramEmbedding`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

TP-sharded hash heads with FP8 rows and per-block E8M0 scales.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding.forward)indices: [num_tokens, n_hash_cols] -> [num_tokens, n_hash_cols, dim]

-
–[lookup](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding.lookup)Look up local heads of [T, heads] into [T, local_heads, dim] bf16.


## Source code in `vllm/models/deepseek_v41/common/engram.py`


|
|

###

`forward(indices)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding.forward)

indices: [num_tokens, n_hash_cols] -> [num_tokens, n_hash_cols, dim] bf16, gathered from all shards for this replica's tokens.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


###

`lookup(indices, out, background=False)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.ParallelEngramEmbedding.lookup)

Look up local heads of [T, heads] into [T, local_heads, dim] bf16.

`background`

limits the grid to leave SMs for concurrent work.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`_engram_head_shard_weight_loader(param, loaded_weight)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram._engram_head_shard_weight_loader)

Load this rank's complete head buckets. ue8m0 scales arrive as float8_e8m0fnu; keep the raw bytes (the param stores uint8).

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`_engram_lookup_kernel(weight, scales, ids, out, vocab_start, vocab_end, num_rows, ids_stride_t, ids_stride_h, HEAD_START, LOCAL_HEADS, TOTAL_HEADS, DIM, QUANT_BLOCK, BLOCK_R, GRID)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram._engram_lookup_kernel)

Gather fp8 rows, apply their ue8m0 block scales, write bf16.

Only this rank's heads are read; padded heads write zeros for all-gather. `weight`

/`scales`

may address pinned host memory through UVA.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`_engram_select_rows(gathered, output, source_tokens, token_start, local_width)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram._engram_select_rows)

Copy one token window out of a rank-major gathered buffer.

Both gathers land rank-major ([rank](https://docs.python.org/3/library/token.html#module-token)[local width]); this walks the window the rank keeps and lays its ranks out side by side as width.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`_is_prime(n)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram._is_prime)

Deterministic Miller-Rabin for n < 2**32 (avoids a sympy import).

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`build_compressed_token_map(tokenizer)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.build_compressed_token_map)

Map every token id onto a smaller id space where tokens that normalize alike collapse together.

N-grams are hashed over these compressed ids, so " The", "the" and "THE" all hash the same way. The compressed size matters beyond bounds checking: every hash multiplier is derived from it.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`compute_hash_multipliers(layer_ids, max_ngram_size, compressed_vocab_size)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.compute_hash_multipliers)

One multiplier per (layer, lookback), from a per-layer RNG so layers hash differently. Kept odd and bounded so `token_id * multiplier`

cannot overflow int64.

## Source code in `vllm/models/deepseek_v41/common/engram.py`


##

`find_next_prime(start, seen_primes)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.engram.find_next_prime)

The smallest prime above `start`

that has not been handed out yet.