# [Issue #3133] Group Disk Reads by Safetensors File - Reduce File/Mapping Overhead

source: https://github.com/vllm-project/llm-compressor/issues/3133
state: open | updated: 2026-09-17T20:53:40Z
labels: enhancement

## 正文

## Objective

Reduce per-read overhead by grouping parameter reads according to their backing safetensors file and keeping frequently accessed files open during a subgraph load.

## Current Behavior

A single logical subgraph may reference many tensors. If each parameter access independently opens, maps, reads, and closes its backing safetensors file, repeated file setup becomes significant overhead for very large checkpoints.

## Proposed Improvement

Group accesses by file to:

1. Reduce redundant file open/close and mapping operations
2. Enable more effective use of acceleration mechanisms like `instanttensor`, where opening/preparing a file has up-front cost but subsequent reads are faster

## Proposed Implementation

```python
for subgraph in subgraphs:
    with disk_load_context():
        subgraph(batch)
```

Within `disk_load_context()`, backing files would be lazily opened when first referenced and cached for the context lifetime:

```python
with disk_load_context():
    tensor_a = load_tensor(...)  # opens shard-01
    tensor_b = load_tensor(...)  # reuses shard-01
    tensor_c = load_tensor(...)  # opens shard-02
    tensor_d = load_tensor(...)  # reuses shard-01
```

At the end of the context, cached handles and any associated per-file resources would be released.

## Possible Extension

If checkpoint metadata is available ahead of time, the loader could explicitly determine required files:

```python
files = files_required_by(subgraph)

with disk_load_context(files):
    onload(subgraph)
```

This would make file lifetime deterministic and allow more intelligent read reordering/prefetching.

**Tradeoff:** Increased memory usage from file-level acceleration mechanisms. Cache should have explicit lifetime and memory bounds.

## Expected Benefits

- Reduced per-read overhead for large checkpoints
- Better file handle utilization
- Foundation for more intelligent I/O optimization (read reordering, prefetching)

## 评论 (2)

### amacharla15 · 2026-09-11

Hi @kylesayrs , I'd be interested in working on this issue.

My understanding from the proposed design is that we'd introduce a context-scoped cache for backing safetensors files, so repeated tensor loads from the same shard can reuse the file during a subgraph load and release the resources when the context exits.

If this is still available for an external contributor, I'd like to start by tracing the current disk-loading path and determining the right place for the context/cache before implementing it. Does that sound like the intended direction?


### ishrith-gowda · 2026-09-16

The per-read open this targets is in `compressed-tensors`, not here: `DiskCache.onload` does `with safe_open(file) as f: f.get_tensor(name)` and closes immediately, once per parameter.

I measured it before building anything. `safe_open` parses a header describing every tensor in the file, so one open costs O(N) in the file's tensor count and a group of N reads is O(N**2). Single shard, warm page cache, median of 9:

```
  tensors  per-open ms  grouped ms   speedup    us/open
        8         0.41        0.18      2.3x       29.0
       32         1.59        0.30      5.4x       40.4
      128        10.24        0.75     13.7x       74.2
      384        65.42        1.92     34.1x      165.4
      768       235.46        3.70     63.6x      301.8
```

The last column is the quadratic term.

One scoping note that changes the framing: the sequential pipeline wraps its batch loop in `disable_offloading()`, so weights onload once per subgraph rather than per batch. A dense 7B does roughly 288 reads across a whole run and saves about 11ms, which is nothing. The win is MoE and large sharded checkpoints, where a single subgraph references hundreds of expert tensors from one file. Worth stating in the issue so nobody benchmarks this on a dense model and concludes it does not help.

I put up the `compressed-tensors` half as vllm-project/compressed-tensors#883: `disk_load_context()`, opt in, thread local, nesting supported, bounded handle count, with tests and the benchmark above.

@amacharla15 you said on Sep 11 you were interested in this one. I deliberately did not take the pipeline side, which is the larger part and the actual subject of this issue. #883 is just the primitive it needs. Happy to hand it over or close it if you already have something.

