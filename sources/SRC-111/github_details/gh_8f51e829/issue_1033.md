# [Issue #1033] Enhancement: Persistent dataset generation with parallel workers and deterministic seeding

source: https://github.com/vllm-project/guidellm/issues/1033
state: open | updated: 2026-08-27T20:39:05Z
labels: 

## 正文

## Problem

Currently, guidellm generates synthetic datasets **in-memory** at runtime. This creates three significant problems for benchmarking workflows:

### 1. Results are not comparable across runs
Each benchmark run generates a different random dataset, even with identical configuration. When comparing TP=4 vs TP=8, each configuration gets different prompts with different token lengths — the dataset itself becomes an uncontrolled variable.

### 2. Prefix cache benchmarks are unreliable
Prefix cache hit rates depend on exact prompt content. When the dataset changes between runs, the cache behavior changes too, making cache sweep results noisy and unreproducible.

### 3. Large dataset generation is slow and memory-intensive
For large-scale benchmarks (100K+ rows, ISL=15000), generating the dataset in a single process consumes significant memory and time. Multi-turn conversation datasets with 540 turns and 160K first_prompt_tokens can easily exhaust pod memory.

## Proposed Solution

Add support for **persistent, pre-generated datasets** with three key features:

### Feature 1: Deterministic seed-based dataset identity

Generate a deterministic seed from the workload configuration so the same config always produces the same dataset:

```python
import hashlib

seed_input = f"{model_name}:{isl}:{osl}:{hit_pct}:{isl_stdev}:{osl_stdev}:{cache_mode}:{groups}"
seed = int(hashlib.sha256(seed_input.encode()).hexdigest()[:8], 16)
```

The dataset filename includes the seed, enabling automatic reuse:
```
prefix-cache-identical-3510887134.jsonl   # Same config → same seed → reuse
calibration-decode-1-1000-1184319629.jsonl
```

When a benchmark run starts, check if the dataset file already exists before regenerating:
```python
dataset_path = f'/datasets/prefix-cache-{cache_mode}-{seed}.jsonl'
if os.path.exists(dataset_path):
    print(f"Reusing existing dataset: {dataset_path}")
else:
    generate_dataset(config, seed, output=dataset_path)
```

### Feature 2: Multi-worker parallel generation

Split dataset generation across multiple workers using `multiprocessing.Pool`. Each worker generates a chunk with a deterministic seed offset:

```python
import multiprocessing
import random

def _generate_chunk(chunk_args):
    start_idx, count, seed, isl, osl, isl_stdev, osl_stdev, model_name = chunk_args
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    vocab = [t for t in tokenizer.get_vocab().keys()
             if len(t) > 2 and t.isascii() and t.isalpha()]
    
    rows = []
    for i in range(count):
        rng = random.Random(seed + start_idx + i + 1)
        row_isl = isl + int(rng.random() * isl_stdev) if isl_stdev > 0 else isl
        row_osl = osl + int(rng.random() * osl_stdev) if osl_stdev > 0 else osl
        
        # Generate token-accurate prompt using actual model tokenizer
        words = [rng.choice(vocab) for _ in range(row_isl * 2)]
        text = ' '.join(words)
        tokens = tokenizer.encode(text, add_special_tokens=False)
        if len(tokens) > row_isl:
            text = tokenizer.decode(tokens[:row_isl], skip_special_tokens=True)
        
        rows.append(json.dumps({'prompt': text, 'output_tokens_count': row_osl}))
    return rows

def generate_parallel(config, seed, output_path):
    num_workers = min(multiprocessing.cpu_count(), 8)
    chunk_size = config.rows // num_workers
    
    chunks = []
    offset = 0
    for w in range(num_workers):
        n = chunk_size + (1 if w < config.rows % num_workers else 0)
        chunks.append((offset, n, seed, config.isl, config.osl, 
                       config.isl_stdev, config.osl_stdev, config.model))
        offset += n
    
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.map(_generate_chunk, chunks)
    
    with open(output_path, 'w') as f:
        for chunk_rows in results:
            for row in chunk_rows:
                f.write(row + '\n')
```

This produces identical results to sequential generation (same seed → same output) but runs N× faster. For 100K rows with ISL=15000, 8 workers complete in ~30 seconds vs ~4 minutes single-threaded.

### Feature 3: Prefix cache simulation modes

Support three cache simulation modes for realistic prefix cache benchmarking:

**Identical mode** — A percentage of rows share the exact same prompt (simulating FAQ bots, fixed system prompts):
```python
def generate_cache_dataset(config, seed, output_path, hit_pct):
    # Generate one shared prompt at max ISL
    shared_rng = random.Random(seed)
    max_isl = config.isl + config.isl_stdev
    shared_prompt = make_prompt(max_isl, shared_rng, tokenizer, vocab)
    
    hit_count = int(config.rows * hit_pct / 100)
    unique_count = config.rows - hit_count
    
    rows = []
    # hit_pct% of rows use the shared prompt (truncated to their ISL)
    for i in range(hit_count):
        rng = random.Random(seed + i)
        row_isl = isl + int(rng.random() * isl_stdev)
        prompt = tokenizer.decode(
            tokenizer.encode(shared_prompt)[:row_isl])
        rows.append({'prompt': prompt, 'output_tokens_count': osl})
    
    # Remaining rows get unique prompts (cache misses)
    for i in range(unique_count):
        rng = random.Random(seed + hit_count + i + 1)
        rows.append(make_unique_row(rng, ...))
    
    random.Random(seed + 999).shuffle(rows)  # Mix hits and misses
    write_jsonl(rows, output_path)
```

**Prefix group mode** — N groups of rows share a common prefix (simulating multi-tenant platforms, multi-repo coding assistants):
```python
def generate_prefix_group_dataset(config, seed, output_path, 
                                   num_groups, prefix_pct):
    # Generate N unique group prefixes
    group_prefixes = []
    for g in range(num_groups):
        grng = random.Random(seed + g * 10000)
        prefix_tokens = int(config.isl * prefix_pct / 100)
        group_prefixes.append(
            make_prompt(prefix_tokens, grng, tokenizer, vocab))
    
    # Each row gets: group_prefix + unique_suffix
    for i in range(config.rows):
        group_idx = i % num_groups
        prefix = group_prefixes[group_idx]
        suffix = make_prompt(isl - len(prefix_tokens), rng, ...)
        prompt = prefix + '\n' + suffix
        rows.append({'prompt': prompt, ...})
```

**Multi-turn conversation persistence** — For multi-turn datasets, use guidellm's existing `SyntheticTextDataset` but persist to disk with parallel workers:
```python
from guidellm.data.deserializers.synthetic import (
    SyntheticTextDataArgs,
    SyntheticTextDataset,
)

def _worker_generate_turns(worker_args):
    worker_id, model_name, config_dict, num_rows, seed = worker_args
    config = SyntheticTextDataArgs(**config_dict)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    ds = SyntheticTextDataset(
        config=config, processor=tokenizer, random_seed=seed)
    
    results = []
    for i, sample in enumerate(ds):
        results.append(json.dumps(sample))
        if i + 1 >= num_rows:
            break
    return results

# Split across workers with different seed offsets
worker_args = []
for w in range(num_workers):
    worker_seed = seed + w * 10000  # Deterministic per-worker seed
    worker_args.append((w, model, config_dict, chunk_size, worker_seed))

with multiprocessing.Pool(num_workers) as pool:
    chunks = pool.map(_worker_generate_turns, worker_args)
```

## CLI Interface

```bash
# Single-turn with prefix cache simulation
guidellm generate-dataset \
    --model google/gemma-4-26B-A4B \
    --isl 15000 --osl 1000 \
    --isl-stdev 5000 --osl-stdev 500 \
    --mode cache --hit-pct 40 \
    --rows 100000 --seed 3510887134 \
    --output /datasets/benchmark.jsonl

# Multi-turn conversations
guidellm generate-dataset \
    --model RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-FP8-block \
    --isl 1500 --osl 425 \
    --first-prompt-tokens 160000 \
    --prefix-tokens 3000 --prefix-count 1 \
    --turns 540 --rows 100 --seed 42 \
    --output /datasets/agentic.jsonl

# Prefix group mode (multi-tenant simulation)
guidellm generate-dataset \
    --model meta-llama/Llama-3.1-70B-Instruct \
    --isl 4000 --osl 500 \
    --mode prefix_group --prefix-groups 10 --hit-pct 60 \
    --rows 50000 --seed 12345 \
    --output /datasets/multi-tenant.jsonl
```

## Then use the pre-generated dataset in benchmarks

```bash
# All benchmark runs use the EXACT same dataset
guidellm run \
    --data '{"kind":"json_file","path":"/datasets/benchmark.jsonl"}' \
    --backend "http://localhost:8000/v1" \
    --profile "concurrent:30"
```

## Why This Matters

In our benchmarking platform ([ServeIt Studio](https://github.com/openshift-psap/serveit-studio)), we test 10-30 different deployment configurations per optimization run. Each configuration needs identical input data to produce comparable results. We implemented this externally using the approach above, and it solved:

- **A/B test accuracy**: TP=4 vs TP=8 comparisons now show real performance differences, not dataset noise
- **Cache sweep reliability**: Testing 0%/20%/40%/60%/80% cache hit rates with deterministic prefix sharing produces clean, reproducible curves
- **Generation speed**: 100K rows with ISL=15000 generates in ~30s with 8 workers vs ~4 minutes single-process
- **Memory efficiency**: Workers process chunks independently — no 100K×15K token array in memory at once
- **Reuse**: Same model+workload config auto-detects existing dataset and skips regeneration, saving minutes per run

We're happy to contribute the implementation if there's interest. The code is MIT-licensed at:
- Single-turn generator: [`docker/scripts/generate_dataset.py`](https://github.com/openshift-psap/serveit-studio/blob/main/docker/scripts/generate_dataset.py)
- Multi-turn generator: [`docker/scripts/generate_turn_dataset.py`](https://github.com/openshift-psap/serveit-studio/blob/main/docker/scripts/generate_turn_dataset.py)

## 评论 (3)

### sjmonson · 2026-08-19

I have been thinking of something related to this as an update to the `guidellm preprocess` command to allow users to run the full data generation pipeline and output a dataset though I do have a couple points to make on the plan here. For "Feature 1" we already have a deterministic seed for dataset generation "Results are not comparable across runs" is not true, if you are seeing that problem then it is likely a bug. "Feature 2" is already an unused feature in the code, we use torch data-generation workers rather then Python MP for that portion. The limitation right now is that the synthetic dataset generator needs to be tweaked to properly shard work. I think "Feature 3" is completely reasonable, the current `synthetic_text` does not have the best controls from this workload so it makes sense to me to add a new synthetic dataset fitting these requirements.

### sjmonson · 2026-08-19

This also relates to #1024 since if we rework `preprocess` into a dataset pre-generator it would be a good idea to have a standard `jsonl` format that can be exported as a normal output.

### bbenshab · 2026-08-19

Yeah, I forgot about [#1024](https://github.com/vllm-project/guidellm/issues/1024), you can close it as a duplicate if you wish, but it might be worth keeping it separately without all the other stuff 
