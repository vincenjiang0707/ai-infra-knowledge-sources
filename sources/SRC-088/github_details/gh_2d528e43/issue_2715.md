# [Issue #2715] Different models on same tasks gives same results when cache is active

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/2715
state: open | updated: 2026-08-29T08:44:04Z
labels: bug

## 正文

Executing the same task with same configs on two different models produces same identical resulting metrics when using cache. If I don't use cache I get the correct results (different metrics). Is cache working properly?


To reproduce the problem:
```
lm_eval --model hf \
    --model_args pretrained=Qwen/Qwen2.5-3B \
    --tasks hellaswag \
    --device cuda:0 \
    --batch_size 1 \
    --limit 10 \
    --output_path output/test \
    --use_cache cache/cache.db

lm_eval --model hf \
    --model_args pretrained=meta-llama/Llama-3.2-3B \
    --tasks hellaswag \
    --device cuda:0 \
    --batch_size 1 \
    --limit 10 \
    --output_path output/test \
    --use_cache cache/cache.db
```

I'm using the latest version of the library installed directly from this repo.

## 评论 (4)

### baberabb · 2025-02-19

will have a look! probably a hashing error

### CDPA-SCA · 2025-02-26

> will have a look! probably a hashing error

Is there any progress?

### baberabb · 2025-02-26

Hi! yeah, sorry meant to provide an update. So the current implementation simply checks if the inputs exist in the provided cache file, and does not take the model into account. Would be trivial to extend this to create unique cache db files for different `model_args`, but couple of issues:
1. Currently we allow passing both a model str or an already initialized model to `simple_evaluate`, and would run into some issues in the latter case.
2. Not clear which args should use different caches. Obviously we want it for unique `pretrained`. But other args like `max_length` or precision could also have an affect on performance, depending on the task.

Was thinking we always add a warning to use a different file for different models and leave it to user to decide. 

### hassaanch23 · 2026-08-29

I'd like to take this one if it's still open.

Reproduced it in isolation, with two stub models sharing one cache db — no GPU or model download involved:

```
model A returns: [(-1.0, True)]
model B returns: [(-1.0, True)]     # identical
model B queried: 0 requests         # never ran
```

Confirms @baberabb's diagnosis exactly: `hash_args(attr, req.args)` keys on the request type and its arguments, so nothing distinguishes one model's entries from another's.

On the two concerns raised above, I'd suggest not deriving per-model cache files, for the reason given in that comment — deciding *which* of `model_args` should scope a cache is a real judgement call (`pretrained` obviously, but `max_length` and precision can move results too), and getting it wrong either fragments caches needlessly or keeps silently sharing them.

Instead: record which model populated a db under a reserved key, and compare on later opens. That is the "warn and leave it to the user" outcome suggested above, but the warning fires only on an actual mismatch rather than unconditionally — so it stays meaningful instead of becoming noise people filter out.

It also handles the pre-initialized-model case cleanly: identity resolution returns `None` there, since an already-constructed LM isn't reliably introspectable from the evaluator and a wrong fingerprint would be worse than none. That path warns only that the cache couldn't be verified, and never stamps a db, so it can't poison one for a later run that *can* be identified.

The reserved key can't collide with a real entry — request keys are sha256 hexdigests — and there's a test pinning that.

Happy to adjust if you'd rather have per-model files, or make the mismatch an error rather than a warning. PR shortly.

