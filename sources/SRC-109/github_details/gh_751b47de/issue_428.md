# [Issue #428] GenAI perf sweeps with multiple models fails

source: https://github.com/triton-inference-server/perf_analyzer/issues/428
state: open | updated: 2025-08-05T04:04:26Z
labels: 

## 正文

Current multiple models specified in config will use `model_selection_strategy` to send request to specific model. 

But when sweeping (analyze), I want to run for a specific model rather than selecting different models in one run.
This function seems not working currently.

My config is like below:
```
model_names: ["mistral:7b", "llama2:7b"]

analyze:
  input_sequence_length:
    start: 50
    stop: 2000
```

Run `genai-perf config -f config.yml` causes the following errors.
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/main.py", line 52, in main
    run()
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/main.py", line 45, in run
    args.func(config, extra_args)
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/subcommand/config.py", line 46, in config_handler
    analyze_handler(config, extra_args)
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/subcommand/analyze.py", line 73, in analyze_handler
    analyze.sweep()
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/subcommand/analyze.py", line 139, in sweep
    for count, objectives in enumerate(
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/config/generate/sweep_objective_generator.py", line 61, in get_objectives
    yield from self._create_objectives()
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/config/generate/sweep_objective_generator.py", line 71, in _create_objectives
    self._create_list_of_model_search_parameter_combinations(model_name)
  File "/usr/local/lib/python3.12/dist-packages/genai_perf/config/generate/sweep_objective_generator.py", line 118, in _create_list_of_model_search_parameter_combinations
    search_parameters = self._model_search_parameters[model_name]
                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
KeyError: 'llama2:7b'
[2025-08-04 05:01:47] ERROR    'llama2:7b'
```

I think this tool requires two things to make it work better, one is to keep using `model_selection_strategy` for sweeping parameters, another is supporting sweep models for testing.

## 评论 (1)

### ExplorerRay · 2025-08-05

Finding that class `Subcommand` only specifies one model name which causes this issue. I don't know why it only uses one in this class.

ref: https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/genai_perf/subcommand/subcommand.py#L64
