# [Issue #3360] Key Error: 'afrimmlu_direct_amh' when running simple_evaluate on AfriMGSM and AfriMMLU tasks

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3360
state: closed | updated: 2026-08-24T13:43:21Z
labels: 

## 正文

I am trying to reproduce the results from [IrokoBench](https://aclanthology.org/2025.naacl-long.139/), but the evaluation does not run on [AfriMMLU](https://github.com/masakhane-io/lm-evaluation-harness/tree/main/lm_eval/tasks/afrimmlu) and [AfriMGSM](https://github.com/masakhane-io/lm-evaluation-harness/tree/main/lm_eval/tasks/afrimgsm), and I get the following error:

```
...
File "/mnt/task_runtime/lm-evaluation-harness/lm_eval/tasks/__init__.py", line 312, in _load_individual_task_or_group
    subtask_list = self._get_tasklist(name_or_config)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/task_runtime/lm-evaluation-harness/lm_eval/tasks/__init__.py", line 232, in _get_tasklist
    return self.task_index[name]["task"]
           ~~~~~~~~~~~~~~~^^^^^^
KeyError: 'afrimmlu_direct_amh'
```

Here is the code I use to run evaluation:

```python
from lm_eval.tasks import TaskManager
from lm_eval import simple_evaluate

task_manager = TaskManager()

# Smoke test: 5 examples per task
results = simple_evaluate(
    model        = eval_model,
    tasks        = ['afrimmlu_direct_amh'],
    num_fewshot  = 0,
    limit        = 5,
    task_manager = task_manager,
    log_samples  = True
)
```

It works well with [AfriXNLI](https://github.com/masakhane-io/lm-evaluation-harness/tree/main/lm_eval/tasks/afrixnli). It seems that AfriMGSM and AfriMMLU are not included in the list of tasks returned by that `get_tasklist` method.

## 评论 (2)

### DerXter · 2025-10-22

I just realised with the commands `lm-eval --tasks list | grep afrimgsm` and `lm-eval --tasks list | grep afrimmlu` that there is an additional `_prompt_{nb}` at the end of each subset name where `{nb}` is a number between 1 and 5. There is also no `_direct` suffix for **AfriXNLI** and **AfriMGSM** prompts as stated in the Readmes, there is an inconsistency regarding task naming.
> It is important to note that there are two different versions of Irokobench ([v1](https://arxiv.org/pdf/2406.03368v1) and [v2](https://arxiv.org/pdf/2406.03368v2)) using different prompts. This must be taken into account in the `simple_evaluate` function in order to replicate the expected results. The absence of the `_direct` suffix mentioned above thus applies to **v2 prompts**, not v1 prompts.

So, the line `tasks = ['afrimmlu_direct_amh']` in the previous comment should be replaced for example by `tasks = ['afrimmlu_direct_amh_prompt_1']`.

The Readmes in [AfriXNLI](https://github.com/masakhane-io/lm-evaluation-harness/tree/main/lm_eval/tasks/afrixnli), [AfriMMLU](https://github.com/masakhane-io/lm-evaluation-harness/tree/main/lm_eval/tasks/afrimmlu) and [AfriMGSM](https://github.com/masakhane-io/lm-evaluation-harness/tree/main/lm_eval/tasks/afrimgsm) need to be updated in consequence.

### discobot · 2026-06-13

Turns out the stale READMEs aren't the only problem here: even the correct `_prompt_{i}`
names are partly broken — every afrimmlu task fails with
`AttributeError: ... has no function 'weighted_f1_score'` (the import was auto-stripped by
a lint fix in #3577), and two mis-applied tags make `afrimgsm-irokobench` and
`afrixnli_manual_translate` unloadable. Fix in #3841: restores the import, fixes the tags,
and updates the three READMEs to the registered names.

