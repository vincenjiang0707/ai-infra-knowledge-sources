# [Issue #9674] [Feature] Create benchmark and dataset usage scripts for embedding models

source: https://github.com/sgl-project/sglang/issues/9674
state: open | updated: 2026-09-23T18:56:55Z
labels: good first issue, help wanted

## 正文

Look at the following for related tests, and the benchmark script should be similar to `bench_serving`
Existing Tests:
``` 
models/test_embedding_models.py — Backend, 73s — PR: core embedding model implementations (covers srt/models/*_embedding.py, srt/entrypoints/openai/serving_embedding.py).

models/test_encoder_embedding_models.py — Backend, 100s — Post-merge: encoder-based embedding models (BERT/Roberta-style).

models/test_cross_encoder_models.py — Backend, 100s — Post-merge: cross-encoder/reranker models (related to embedding-based tasks but a different architecture).

openai_server/basic/test_serving_embedding.py — Frontend/unit, 10s — Run on all PRs: embedding serving layer (validates the serving path).

openai_server/basic/test_openai_embedding.py — Frontend, 141s — Frontend (PR/post-merge as listed): end-to-end OpenAI embedding API endpoints.

test_input_embeddings.py — Backend, 38s — Post-merge: tests the input embedding handling/path.
```

## 评论 (9)

### JustinTong0323 · 2025-08-27

@vincentzed 

### AuruTus · 2025-08-28

Hi, I'm interested in this issue. Is the `bench_serving` you mentioned the file at `python/sglang/bench_serving.py` ? I'm reading the code base and try to find an entry.

### vincentzed · 2025-08-29

@AuruTus I attach examples of the testing for embedding just to show what we can do, but when we actually make the benchmark, we want to start up the server OR run a batch, you can see the offline script too. In practice the second is used way more, so that one is probably more important, but I reccomend creating:
- A online-serving (HTTP endpoint) embedding benchmark
- And a offline one, like : https://github.com/sgl-project/sglang/blob/3aec3d4f8b9f4c2cc84df13b71c9880a4ec2a6aa/python/sglang/bench_offline_throughput.py#L10 for but embedding

### AuruTus · 2025-09-03

hi @vincentzed , I'm a bit confused for which metric is necessary for embedding models, for encoding only has embedding tensor output. Are these output ok for embedding benches ?

```
====== Offline Throughput Benchmark Result =======
Backend:                                 engine    
Successful requests:                     1000      
Benchmark duration (s):                  15.48     
Total input tokens:                      296523    
Average e2e latency (s):                 8.01      
Last generation throughput (tok/s):      0.00      
Request throughput (req/s):              64.60     
Input token throughput (tok/s):          19156.40  
==================================================
```

I just remove total and output token things, and just add an e2e_latency.


### SiluPanda · 2026-04-27

Hi, I'd like to take this up if it's still available. I can start with an offline embedding benchmark modeled after `bench_offline_throughput.py`, then follow up with an HTTP-serving embedding benchmark and sample dataset usage. Please let me know if there are preferred metrics beyond request/input-token throughput and e2e latency.

### GoyalIshaan · 2026-06-17

Hi, I’m interested in helping here, but I see #9974 and #25534 are already open. Is there any remaining subtask that maintainers still want help with, or should I avoid duplicating those PRs?

### devinhuang2001 · 2026-09-01

I reviewed the previous attempts in #9974 and #25534, which are now closed. I am working on the remaining dataset-usage part: adding an `embedding` JSONL dataset to the current `bench_serving` flow, supporting both string and string-array `input` values and pass-through OpenAI embedding parameters such as `dimensions` and `encoding_format`. I have a local implementation with unit coverage and documentation; I will open a PR after validating it against the current main branch.

### devinhuang2001 · 2026-09-02

I opened draft PR #37501 (https://github.com/sgl-project/sglang/pull/37501) for the remaining dataset-usage part. It adds an `embedding` JSONL dataset to the current benchmark flow, supporting string/list inputs and pass-through embedding parameters. The PR is intentionally draft pending maintainer confirmation that this is the desired split from the earlier closed benchmark attempts.

### natsu-git-hub · 2026-09-23

Hi @JustinTong0323, looks like this is mostly covered:

- Serving benchmark: #20017 (merged) added a `sglang-embedding` backend to `bench_serving`. It didn't link this issue.
- Dataset support: #37501 (open draft) adds a JSONL embedding dataset.
- Offline benchmark: tried in #23892, closed without review.

Is anything still needed beyond #37501? If the offline benchmark is wanted, I'm happy to add it inside the existing benchmark structure. Otherwise this could close once #37501 lands.
