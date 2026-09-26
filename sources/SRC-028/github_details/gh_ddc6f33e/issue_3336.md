# [Issue #3336] [Bug]: TypeError in train_rl.py - RolloutConfig gets unexpected keyword arguments (rollout_vllm_*) from Tunix

source: https://github.com/AI-Hypercomputer/maxtext/issues/3336
state: closed | updated: 2026-05-01T22:16:43Z
labels: bug

## 正文

### Bug report

### Bug Description 
When running the RL post-training script (`train_rl.py`) from the current `main` branch, it immediately crashes with a `TypeError` when initializing `RolloutConfig`.

It appears that recent commits added new vLLM-specific arguments (like `rollout_vllm_hf_config_path` and `rollout_vllm_additional_config`) to the rollout instantiation in MaxText. However, the `tunix` package (specifically `base_rollout.RolloutConfig`) does not accept these arguments, leading to an initialization crash. 

### Point of Failure
The crash occurs here in train_rl.py:
https://www.google.com/search?q=https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/trainers/post_train/rl/train_rl.py%23L563

This creates a version mismatch where git clone pulls the bleeding-edge MaxText sending these kwargs, but the installed tunix dependency rejects them.

### Temporary Workaround
To get the training loop to compile, I had to dynamically monkey-patch base_rollout.RolloutConfig.__init__ in memory to filter out any **kwargs starting with rollout_vllm_ before loading MaxText.


### Logs/Output

### Error Trace
```python
Traceback (most recent call last):
  File "/workspace/train.py", line 122, in <module>
    rl_train(trainer_config, sampler_config, trainer_devices, sampler_devices)
  File "/usr/local/lib/python3.12/site-packages/maxtext/trainers/post_train/rl/train_rl.py", line 552, in rl_train
    rollout_config=base_rollout.RolloutConfig(
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: RolloutConfig.__init__() got an unexpected keyword argument 'rollout_vllm_hf_config_path'
```

(Note: If you bypass the first one, it throws the exact same error for rollout_vllm_additional_config).


### Environment Information

Hardware: TPU v5e (2x4 slice)

Model: Llama 3.1 8B (GRPO)

MaxText Version: main (latest)

### Additional Context

_No response_

## 评论 (5)

### karajendran · 2026-03-06

**Quick Update:** 
It looks like this version mismatch isn't just limited to the `rollout_vllm_*` kwargs. The script also crashes on `expert_parallel_size` being passed to `RolloutConfig`.

For anyone else blocked by this while waiting for the Tunix PyPI package to catch up to MaxText `main`, you can dynamically patch `base_rollout.RolloutConfig.__init__` using the `inspect` module to act as an auto-firewall. 

Just run this before importing `rl_train`:

```python
import inspect
from tunix.rl.rollout import base_rollout
original_init = base_rollout.RolloutConfig.__init__
valid_params = set(inspect.signature(original_init).parameters.keys())

def patched_init(self, *args, **kwargs):
    filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_params}
    original_init(self, *args, **filtered_kwargs)

base_rollout.RolloutConfig.__init__ = patched_init

### karajendran · 2026-03-06

**Update 2:** The version mismatch isn't just in the rollout logic; it extends to `rl_cluster.ClusterConfig` as well. The script crashes when MaxText passes the new `role_to_logical_axis_rule` argument, which the stable Tunix release rejects.

I've updated the workaround to apply the `inspect` firewall to both configuration classes. For anyone blocked, run this before `rl_train`:

```python
import inspect
from tunix.rl.rollout import base_rollout
from tunix.rl import rl_cluster

def build_firewall(config_class):
    original_init = config_class.__init__
    valid_params = set(inspect.signature(original_init).parameters.keys())
    def patched_init(self, *args, **kwargs):
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_params}
        original_init(self, *args, **filtered_kwargs)
    config_class.__init__ = patched_init

build_firewall(base_rollout.RolloutConfig)
build_firewall(rl_cluster.ClusterConfig)

### A9isha · 2026-03-06

Hi @karajendran thank you for raising this. We have been working on making this less painful. As a part of it, we now have a new way of installation [locally](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/rl.html#option-1-from-pypi-releases-recommended) and also when building the docker image with [stable release](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/rl_on_multi_host.html#option-1-install-stable-releases-of-post-training-dependencies) [this option is no longer broken]

This will help bridge these version mismatches and resolve the issue.

### SurbhiJainUSC · 2026-04-27

@karajendran - Could you please confirm if the installation method mentioned by @A9isha resolves the crash for your environment?

### sarunsingla11722 · 2026-05-01

Closing this as its no longer a valid issue.
