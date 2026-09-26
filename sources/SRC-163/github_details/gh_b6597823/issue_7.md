# [Issue #7] missing SimulatorConfig.profiler_data_path when runing offline.py

source: https://github.com/LLMServe/DistServe/issues/7
state: closed | updated: 2024-06-14T07:24:25Z
labels: bug

## 正文

missing SimulatorConfig.profiler_data_path when runing offline.py

## 评论 (3)

### llx-08 · 2024-06-11

If your intention is merely to run `offline.py`, you can manually modify the `class OfflineLLM` in the `/distserve/llm.py` file by adding a `SimulatorConfig` instance and setting `is_simulator_mode` to `False`.
like this
```
       # modified
       simulator_config = SimulatorConfig(is_simulator_mode=False,
                                           profiler_data_path='',
                                           gpu_mem_size_gb=70)

        self.engine = LLMEngine(
            model_config,
            disagg_parallel_config,
            cache_config,
            context_sched_config,
            decoding_sched_config,
            simulator_config
        )
```

### PKUFlyingPig · 2024-06-11

This bug has been fixed in PR(#11), please try again.

### interestingLSY · 2024-06-14

Closing this issue. Reopen it if you encountered any further issues.
