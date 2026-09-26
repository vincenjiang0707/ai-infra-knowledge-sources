# [Issue #3010] hellaswag not working: "no tasks specified" and "Keyerror: 'train'

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3010
state: closed | updated: 2026-08-24T18:18:18Z
labels: asking questions

## 正文

Hi, 

with latest 0.4.8:

`lm_eval --model hf --model_args pretrained=EleutherAI/pythia-160m --tasks arc_easy` works fine.

However `lm_eval --model hf --model_args pretrained=EleutherAI/pythia-160m --tasks arc_easy,hellaswag`  gives me the following error:

```
INFO:lm_eval.__main__:Selected Tasks: ['arc_easy', 'hellaswag']
INFO:lm_eval.evaluator:Setting random seed to 0 | Setting numpy seed to 1234 | Setting torch manual seed to 1234 | Setting fewshot manual seed to 1234
INFO:lm_eval.evaluator:Initializing hf model, with arguments: {'pretrained': 'EleutherAI/pythia-160m'}
INFO:lm_eval.models.huggingface:Using device 'cuda:0'
INFO:lm_eval.models.huggingface:Model parallel was set to False, max memory was not set, and device map was set to {'': 'cuda:0'}
Traceback (most recent call last):
  File "dev/.venv/bin/lm_eval", line 8, in <module>
    sys.exit(cli_evaluate())
             ^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/__main__.py", line 389, in cli_evaluate
    results = evaluator.simple_evaluate(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/utils.py", line 422, in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/evaluator.py", line 240, in simple_evaluate
    task_dict = get_task_dict(tasks, task_manager)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/tasks/__init__.py", line 619, in get_task_dict
    task_name_from_string_dict = task_manager.load_task_or_group(
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/tasks/__init__.py", line 415, in load_task_or_group
    collections.ChainMap(*map(self._load_individual_task_or_group, task_list))
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/tasks/__init__.py", line 315, in _load_individual_task_or_group
    return _load_task(task_config, task=name_or_config)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/tasks/__init__.py", line 281, in _load_task
    task_object = ConfigurableTask(config=config)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/api/task.py", line 855, in __init__
    if self.fewshot_docs() is not None:
       ^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/api/task.py", line 1004, in fewshot_docs
    return super().fewshot_docs()
           ^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/api/task.py", line 323, in fewshot_docs
    return self.training_docs()
           ^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/api/task.py", line 962, in training_docs
    self.dataset[self.config.training_split]
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/datasets/dataset_dict.py", line 81, in __getitem__
    return super().__getitem__(k)
           ^^^^^^^^^^^^^^^^^^^^^^
KeyError: 'train'
```

Just `lm_eval --model hf --model_args pretrained=EleutherAI/pythia-160m --tasks arc_easy,hellaswag`:
```
INFO:lm_eval.__main__:Selected Tasks: []
INFO:lm_eval.evaluator:Setting random seed to 0 | Setting numpy seed to 1234 | Setting torch manual seed to 1234 | Setting fewshot manual seed to 1234
Traceback (most recent call last):
  File "dev/.venv/bin/lm_eval", line 8, in <module>
    sys.exit(cli_evaluate())
             ^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/__main__.py", line 389, in cli_evaluate
    results = evaluator.simple_evaluate(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/utils.py", line 422, in _wrapper
    return fn(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^
  File "dev/.venv/lib/python3.12/site-packages/lm_eval/evaluator.py", line 174, in simple_evaluate
    raise ValueError(
ValueError: No tasks specified, or no tasks found. Please verify the task names.
```

## 评论 (8)

### baberabb · 2025-05-22

Hi! I can't reproduce this. ([colab](https://colab.research.google.com/drive/1H_uehqnaX6tpWSrEE_zaiWfAT51qDJdS?usp=sharing)). Seems a `train` set doesn't exist in the HF dataset. Maybe the dataset for hellaswag was changed in the config?

Unsure about the second part. Seems it isn't parsing the inputs passed to `--tasks`? Could try calling with `LOGLEVEL` env variable e.g. `LOGLEVEL=DEBUG lm_eval ...` and see if something comes up.


### matthijsvk · 2025-05-27

Hi,

I set `dataset_path: Rowan/hellaswag` in `lm_eval/tasks/hellaswag/hellaswag.yaml`. ([huggingface page](https://huggingface.co/datasets/Rowan/hellaswag))
This fixes the `train` issue!

second part: with the above fix, I found that `--tasks hellaswag,hellaswag` works fine. It's weird that it fails only for hellaswag; `--tasks winogrande` works fine. LOGLEVEL=DEBUG didn't give me anything unfortunately.


### StellaAthena · 2025-06-03

> second part: with the above fix, I found that `--tasks hellaswag,hellaswag` works fine. It's weird that it fails only for hellaswag; `--tasks winogrande` works fine. LOGLEVEL=DEBUG didn't give me anything unfortunately.

This seems like it must be a string parsing error, but it's hard for me to imagine what the string parsing error might be.

### nloughl · 2026-03-26

> i

I had the same "no task found" issue with ```--tasks mbpp``` and ```--tasks humaneval```.  Using ```---tasks mbpp,mbpp``` or ```--tasks humaneval,humaneval``` fixed it for me too. 

### StellaAthena · 2026-03-31

@nloughl When you type `ls`, what do you see? I'm wondering if the cause could be that you have a local `mbpp` directory or something like that.

### nloughl · 2026-04-01

Yes i had a mbpp output dir which was causing the issue. I created a PR here to address that:
[https://github.com/EleutherAI/lm-evaluation-harness/pull/3670](url)

### StellaAthena · 2026-04-08

> Yes i had a mbpp output dir which was causing the issue. I created a PR here to address that: https://github.com/EleutherAI/lm-evaluation-harness/pull/3670

When I click that link nothing comes up.

### baberabb · 2026-08-24

PR #3670 should fix this, if it was a name shadowing bug
