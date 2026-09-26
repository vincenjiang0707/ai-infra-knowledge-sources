# [Issue #3046] Cache fails when repeats are greater than 1

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3046
state: open | updated: 2026-08-22T21:33:15Z
labels: bug

## 正文

In evaluator.py at line 560, the request (req) is expanded using req.repeats. However, this process doesn't differentiate between the individual repeated queries. Consequently, the cache only stores the prediction for the first query instance.

```
# create `K` copies of each request `req` based off `K = req.repeats`
cloned_reqs = []
for req in reqs:
    cloned_reqs.extend([req] * req.repeats)
```

```
for generated_text, context in zip(
                    self.parse_generations(
                        outputs=outputs,
                        contexts=contexts,
                    ),
                    contexts,
                ):
    if generated_text is not None:
        res.append(generated_text)
        # partial caching
        if context is not None:
            self.cache_hook.add_partial(
                "generate_until",
                (context, all_gen_kwargs[0]),
                generated_text,
            )
            pbar.update(1)
```


## 评论 (1)

### feiiiiii5 · 2026-08-22

Verified against current `main`: this is already fixed. `CachingLM._fn` (`lm_eval/api/model.py`) now bypasses the cache entirely for non-greedy generation:

```python
if attr == "generate_until" and req.args[1].get("do_sample", False):
    # when we are doing non-greedy generation, don't use the cache
    # (else every "randomly sampled" generation would be identical for repeats > 1).
    res.append(None)
    remaining_reqs.append(req)
```

Sampled requests are re-run every time instead of being replayed from the sqlite db, so repeats > 1 no longer collapse to identical cached generations. Greedy requests still cache correctly (they are deterministic by construction), which matches the original report's failure shape: all K clones hash to the same `(context, gen_kwargs)` key, so only the first draw survived.

Given this, the issue can likely be closed as fixed.

