# [Issue #3441] RULER task crashes with API models (local-chat-completions): TypeError: unhashable type: 'dict'

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3441
state: closed | updated: 2026-08-28T18:16:38Z
labels: 

## 正文

When running the ruler task group using the local-chat-completions model type, the evaluation crashes.

```
$ lm-eval --model local-chat-completions     --tasks ruler_qa_hotpot     --model_args model=ibm-granite/granite-4.0-h-1b,base_url=http://localhost:8080/v1/chat/completions --gen_kwargs temperature=0 --apply_chat_template
2025-12-02:01:20:18 INFO     [__main__:465] Selected Tasks: ['ruler_qa_hotpot']
2025-12-02:01:20:18 INFO     [evaluator:202] Setting random seed to 0 | Setting numpy seed to 1234 | Setting torch manual seed to 1234 | Setting fewshot manual seed to 1234
2025-12-02:01:20:18 WARNING  [evaluator:214] generation_kwargs: {'temperature': 0} specified through cli, these settings will update set parameters in yaml tasks. Ensure 'do_sample=True' for non-greedy decoding!
2025-12-02:01:20:18 INFO     [evaluator:240] Initializing local-chat-completions model, with arguments: {'model': 'ibm-granite/granite-4.0-h-1b', 'base_url':
        'http://localhost:8080/v1/chat/completions'}
2025-12-02:01:20:18 INFO     [models.api_models:172] Using max length 2048 - 1
2025-12-02:01:20:18 INFO     [models.api_models:175] Concurrent requests are disabled. To enable concurrent requests, set `num_concurrent` > 1.
2025-12-02:01:20:18 INFO     [models.api_models:193] Using tokenizer None
2025-12-02:01:20:22 WARNING  [api.task:990] ruler_qa_hotpot: Custom kwargs can be passed to `--metadata` in console (as json string) or to the TaskManager.
For example --metadata='{"max_seq_lengths":[4096, 8192]}'. For details see task Readme.
Traceback (most recent call last):
  File "/home/mramendi/lmeval/bin/lm-eval", line 8, in <module>
    sys.exit(cli_evaluate())
             ~~~~~~~~~~~~^^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/__main__.py", line 474, in cli_evaluate
    results = evaluator.simple_evaluate(
        model=args.model,
    ...<25 lines>...
        **request_caching_args,
    )
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/utils.py", line 458, in _wrapper
    return fn(*args, **kwargs)
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/evaluator.py", line 283, in simple_evaluate
    task_dict = get_task_dict(
        tasks,
        task_manager,
    )
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/__init__.py", line 645, in get_task_dict
    task_name_from_string_dict = task_manager.load_task_or_group(
        string_task_name_list
    )
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/__init__.py", line 427, in load_task_or_group
    collections.ChainMap(
    ~~~~~~~~~~~~~~~~~~~~^
        *map(
        ^^^^^
    ...<2 lines>...
        )
        ^
    )
    ^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/__init__.py", line 429, in <lambda>
    lambda task: self._load_individual_task_or_group(task),
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/__init__.py", line 327, in _load_individual_task_or_group
    return _load_task(task_config, task=name_or_config)
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/__init__.py", line 287, in _load_task
    task_object = ConfigurableTask(config=config)
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/api/task.py", line 865, in __init__
    self.download(self.config.dataset_kwargs)
    ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/api/task.py", line 994, in download
    self.dataset = self.config.custom_dataset(
                   ~~~~~~~~~~~~~~~~~~~~~~~~~~^
        **(self.config.metadata or {}), **(self.config.dataset_kwargs or {})
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/ruler/qa_utils.py", line 240, in get_hotpotqa
    return get_qa_dataset("hotpotqa", **kwargs)
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/ruler/qa_utils.py", line 230, in get_qa_dataset
    list(itertools.chain.from_iterable(df)), split=datasets.Split.TEST
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/ruler/qa_utils.py", line 224, in <genexpr>
    get_dataset(pretrained=pretrained, docs=docs, qas=qas, max_seq_length=seq)
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mramendi/lmeval/lib64/python3.13/site-packages/lm_eval/tasks/ruler/qa_utils.py", line 205, in get_dataset
    tokenizer = get_tokenizer(pretrained)
TypeError: unhashable type: 'dict'
```

An AI-provided monkey-patch workaround hardcodes the model. In `lm_eval/tasks/ruler/qa_utils.py` at the start of `get_dataset()` I replace 

`tokenizer = get_tokenizer(pretrained)`

with 

`tokenizer = get_tokenizer("ibm-granite/granite-4.0-h-1b" if isinstance(pretrained,dict) else pretrained)`

Then things work. But I would appreciate a proper fix if possible.


## 评论 (3)

### jannalulu · 2025-12-09

I've always added `tokenizer=[model name]` in the model_args so it doesn't crash. So it'd be like `--model_args model=ibm-granite/granite-4.0-h-1b,base_url=http://localhost:8080/v1/chat/completions,tokenizer=ibm-granite/granite-4.0-h-1b`

### annafontanaa · 2025-12-12

> I've always added `tokenizer=[model name]` in the model_args so it doesn't crash. So it'd be like `--model_args model=ibm-granite/granite-4.0-h-1b,base_url=http://localhost:8080/v1/chat/completions,tokenizer=ibm-granite/granite-4.0-h-1b`

Could you share the exact command you’re using to launch it please? I tried adding the tokenizer argument the same way, but it doesn’t work on my side. Thanks!


### rafaelhferreira · 2026-02-12

From my observation, it looks like the model, tokenizer, and other metadata are not reaching the task when it is using `custom_dataset` argument in the yaml of the task.

To address this, I added the following logic in `lm_eval/tasks/__init__.py`, inside the `_load_task` function, **before** the line:

```python
if self._config_is_python_task(config):
```

#### Added code

```python
if self.metadata is not None:
    print("Passing metadata in new format")
    config["metadata"] = config.get("metadata", {}) | self.metadata
else:
    print("No metadata found, passing empty metadata")
    config["metadata"] = config.get("metadata", {})
```

With this change, the metadata and related extra information seems to reach the task. However, one should check if this alters the behavior for existing tasks.
