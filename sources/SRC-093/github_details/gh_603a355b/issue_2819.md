# [Issue #2819] [Bug] Sync prefix indexer hashes every block of a BlockStored event against the first block's parent

source: https://github.com/vllm-project/aibrix/issues/2819
state: open | updated: 2026-09-26T03:03:05Z
labels: area/gateway, kind/misc, area/batch

## 正文

### What's wrong

`SyncPrefixHashTable.ProcessBlockStored` (`pkg/utils/syncprefixcacheindexer/sync_hash.go`) computes the AIBrix hash of every block in a `BlockStored` event from the same parent:

```go
for i, engineBlockHash := range event.BlockHashes {
    ...
    var parentAibrixHash = s.seed
    if event.ParentBlockHash != nil {
        if ph, exists := hashMapping.engineToAibrix[*event.ParentBlockHash]; exists {
            parentAibrixHash = ph
        }
    }
    aibrixHash := s.computeHash(parentAibrixHash, s.getBlockTokens(event, i))
```

`ParentBlockHash` is the parent of the first block only. Block `i > 0` should chain from block `i-1` of the same event. On the request path `GetPrefixHashes` builds a proper chain (`H(seed, b0)`, `H(h0, b1)`, ...), so every block after the first in a multi-block event gets a hash the gateway never produces.

vLLM emits one `BlockStored` per batch of newly full blocks, so a long prefill arrives as a single event with many blocks (the decoder splits the tokens per block in `convertTokenIDs`). In practice prefix matching from KV events stops after the first block of each event.

### Repro

Table with block size `bs`, three blocks `b0 b1 b2`:

```go
table.ProcessBlockStored(BlockStored{BlockHashes: []int64{1, 2, 3}, Tokens: [][]byte{b0, b1, b2}, ...})
table.MatchPrefix(model, -1, b0+b1+b2, {pod})
```

Expected 100, got 33. Same for an event whose first block was already known (33), and an event continuing from a parent block (66 instead of 100).

The existing `TestProcessBlockStored` only counts mappings, so it passes either way.

### Fix

Look up the parent once, then carry the previous block's AIBrix hash through the loop, including the already-mapped branch.


## 评论 (2)

### ankit373 · 2026-09-26

Put up a fix in #2820. It carries the previous block's hash through the loop, and there's a test covering the three cases above.

### github-actions[bot] · 2026-09-26

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

