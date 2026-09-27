# [Issue #3339] Repeats is not working in Class

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3339
state: open | updated: 2026-09-26T15:55:39Z
labels: 

## 正文

I created the python task class and want to apply repeats. So, I tried passing the repeats in **Instance** but still it was creating single response.
Please help me out.

```python
def construct_requests(
    self, doc, ctx, chat_template=None, apply_chat_template=False, **kwargs
):
    task=kwargs["metadata"][0]
    doc_id=kwargs["metadata"][1]
    repeats=5
    kwargs.pop("metadata", None)
    return  [
        Instance(
            request_type="generate_until",
            doc=doc,
            arguments=(ctx, {"until": ["\n"], "max_gen_toks": 1048}),
            metadata=(task, doc_id, repeats),
            idx=0,
            **kwargs,
        )
    ]
````

## 评论 (1)

### mgillr · 2026-09-26

Diagnosis and a fix for the config-path variant of this are up in #4247.

The short answer for your repro: the harness does not read `repeats` from the `Instance` metadata tuple — the repeat count is taken from `TaskConfig.repeats` when requests are built (`lm_eval/api/task.py`, `build_requests`). Setting it in metadata is silently ignored, which is why you saw a single response.

The supported routes after #4247:

```python
# 1. Per-call, from the Python API
simple_evaluate(model=..., tasks=[...], repeats=5,
                gen_kwargs="do_sample=True,temperature=0.7")

# 2. Per-task, in the task config
TaskConfig(repeats=5, output_type="generate_until", ...)
```

#4247 also fixes a silent bug where a `TaskConfig` object passed to a Task was unpacked as `**kwargs` and every dataclass field (including `repeats`) reset to its default — so even config-set values were being lost on one path — and adds a warning when `repeats > 1` runs without a `filter_list`, since the default `take_first` filter discards all but the first sampled response.
