# [Issue #1473] Issue with `bigbench_gender_inclusive_sentences_german_multiple_choice`

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1473
state: open | updated: 2026-09-18T05:38:35Z
labels: 

## 正文

While running this task I get the following error stack trace:

```
Traceback (most recent call last):
  File "/opt/conda/envs/fr-de-lb/bin/lm_eval", line 8, in <module>
    sys.exit(cli_evaluate())
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/__main__.py", line 288, in cli_evaluate
    results = evaluator.simple_evaluate(
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/utils.py", line 288, in _wrapper
    return fn(*args, **kwargs)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/evaluator.py", line 154, in simple_evaluate
    task_dict = get_task_dict(tasks, task_manager)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/tasks/__init__.py", line 412, in get_task_dict
    task_name_from_string_dict = task_manager.load_task_or_group(string_task_name_list)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/tasks/__init__.py", line 253, in load_task_or_group
    collections.ChainMap(
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/tasks/__init__.py", line 164, in _load_individual_task_or_group
    return load_task(task_config, task=name_or_config, group=parent_name)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/tasks/__init__.py", line 153, in load_task
    task_object = ConfigurableTask(config=config)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/api/task.py", line 731, in __init__
    test_target = self.doc_to_target(test_doc)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/api/task.py", line 962, in doc_to_target
    target_string = utils.apply_template(doc_to_target, doc)
  File "/home/ayushthakur/lm-eval/llm-leaderboard-fr-de/lm-evaluation-harness/lm_eval/utils.py", line 426, in apply_template
    return rtemplate.render(**doc)
  File "/opt/conda/envs/fr-de-lb/lib/python3.10/site-packages/jinja2/environment.py", line 1301, in render
    self.environment.handle_exception()
  File "/opt/conda/envs/fr-de-lb/lib/python3.10/site-packages/jinja2/environment.py", line 936, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "<template>", line 1, in top-level template code
ValueError: 'Potsdam ist eine kreisfreie Stadt und mit gut 180.000 Einwohner*innen die bevölkerungsreichste Stadt und Hauptstadt des Landes Brandenburg.' is not in list
```

I am using the following command:

```
lm_eval --model hf --model_args pretrained=microsoft/phi-2,trust_remote_code=True --tasks bigbench_gender_inclusive_sentences_german_multiple_choice --device cuda:0 --batch_size 1 --output_path output/phi-2-mmlu-arc --limit 2 --wandb_args project=lm-eval-harness-integration --log_samples
```

cc: @haileyschoelkopf 

## 评论 (2)

### chrikrah · 2026-09-10

The crash is in the generator, not the task. `generate_tasks.py:205` chooses the template from row 0 only:

```python
if set(data["default"][0]["targets"]) < set(multiple_choice_targets):
    template_file = "multiple_choice_template_a_yaml"
```

Template a resolves the answer with `{{multiple_choice_targets.index(targets[0])}}`, the call in the traceback. Template b uses `{{multiple_choice_scores.index(1)}}` and cannot raise that way. One document decides the template for the whole split, so a later row whose `targets` are not a subset of its own `multiple_choice_targets` fails at load. 118 of the 119 files in `multiple_choice/` include template a. `utils.filter_multiple_choice` already handles a sibling of this downstream.

On current main the task exists only under `generate_until/`, so it is not reproducible as filed.

Two fix shapes, differing in diff size:

1. `generate_tasks.py` only, selecting template a when every row satisfies the subset test.
2. That change plus the regenerated configs, up to 119 files.

Which do you prefer? I have not downloaded the dataset, so I have not verified which tasks change template.

### chrikrah · 2026-09-18

This one can close, and my earlier comment on it was wrong about the cause.

`gender_inclusive_sentences_german_zero_shot` carries no multiple-choice targets on any row:

```
$ python -c "import datasets; ds=datasets.load_dataset('hails/bigbench','gender_inclusive_sentences_german_zero_shot')['default']; col=ds['multiple_choice_targets']; print('rows with choices:', sum(1 for c in col if c), 'of', len(col))"
rows with choices: 0 of 200
```

So row 0 is representative here and `generate_tasks.py` is right to skip the subtask. `lm_eval/tasks/bigbench/multiple_choice/gender_inclusive_sentences_german.yaml` does not exist on `d6de816`, so there is no `bigbench_gender_inclusive_sentences_german_multiple_choice` to construct. The traceback above was real on a build that still carried that task file, and `load_task` reaching `ConfigurableTask(config=config)` shows the config was found and parsed. Nothing under `multiple_choice/` reproduces it now.

The skip check in `generate_tasks.py` also read row 0 only, and that is a real defect on a different subtask. `minute_mysteries_qa` has choices on 203 of its 477 rows and row 0 is not one of them, so its multiple-choice variant was never generated at all. #4180 takes the first row that has choices for both the skip decision and the template choice, adds that task file, and leaves this subtask skipped.

One row still decides the template for a whole split, so a later row whose `targets[0]` is absent from its own `multiple_choice_targets` would still raise the `ValueError` above. #4180 does not claim to close that.

