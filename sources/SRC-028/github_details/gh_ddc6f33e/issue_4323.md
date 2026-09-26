# [Issue #4323] Removing --degenerate_group_masking as this field has been removed from Tunix.

source: https://github.com/AI-Hypercomputer/maxtext/issues/4323
state: closed | updated: 2026-07-07T20:37:59Z
labels: 

## 正文

In latest version of Tunix, --degenerate_group_masking has been deprecated (whole feature removed). We need to remove this field as well.

## 评论 (2)

### AntonyMei · 2026-07-01

See: https://github.com/google/tunix/pull/1637

### github-actions[bot] · 2026-07-02

### 🤖 CI Failure Investigation Report

I have analyzed the recent test failures in the CI pipeline and identified the following:

#### 🔍 What Failed
* **Job/Matrix**: `MaxText Package Tests`
* **Failing Test**: `train_rl.py::AgenticGrpoConfig` initialization
* **Error**: `TypeError: __init__() got an unexpected keyword argument 'degenerate_group_masking'`

#### 🪵 Error Details & Stack Trace
```python
# The traceback is expected to resemble:
# File "src/maxtext/trainers/post_train/rl/train_rl.py", line 548, in train_rl
#   grpo_config = AgenticGrpoConfig(
#       ...
#       degenerate_group_masking=trainer_config.rl.degenerate_group_masking,
#       ...
#   )
# TypeError: __init__() got an unexpected keyword argument 'degenerate_group_masking'
```

#### 💡 Root Cause Analysis & Context
**Confidence:** high

The failure is caused by an upstream change in the `tunix` library. In the latest version of Tunix, the `degenerate_group_masking` feature and its corresponding parameter have been entirely deprecated and removed from `AgenticGrpoConfig` (see [Tunix PR #1637](https://github.com/google/tunix/pull/1637)).

MaxText was still specifying `degenerate_group_masking` during the instantiation of `AgenticGrpoConfig` inside `src/maxtext/trainers/post_train/rl/train_rl.py`, and also declaring it as a config option in:
1. `src/maxtext/configs/post_train/rl.yml`
2. `src/maxtext/configs/types.py`

When the package tests run, they pull the latest version of Tunix, which results in a keyword argument mismatch (`TypeError`) during initialization of the GRPO learner config. This has been tracked in Issue #4323.

#### 🛠️ Recommended Fix
Apply the changes proposed in open Pull Request [#4334](https://github.com/AI-Hypercomputer/maxtext/pull/4334) to remove the stale `degenerate_group_masking` configurations:

```diff
diff --git a/src/maxtext/configs/post_train/rl.yml b/src/maxtext/configs/post_train/rl.yml
index 3ecdd3b981..5eb63c6208 100644
--- a/src/maxtext/configs/post_train/rl.yml
+++ b/src/maxtext/configs/post_train/rl.yml
@@ -66,8 +66,6 @@ rl:
   off_policy_steps: 0
   # System prompt injected into the agent at rollout time.
   system_prompt: ''
-  # If true, mask degenerate groups (all-zero advantages) from contributing to the loss.
-  degenerate_group_masking: true
   # Upper-bound clipping epsilon for GRPO loss; defaults to grpo_epsilon when null.
   epsilon_high: null
   # Number of model keys to chunk for resharding tensors between trainer and rollout devices.
diff --git a/src/maxtext/configs/types.py b/src/maxtext/configs/types.py
index 769a8c1745..73b7ba70f8 100644
--- a/src/maxtext/configs/types.py
+++ b/src/maxtext/configs/types.py
@@ -2156,10 +2156,6 @@ class RL(BaseModel):
       "",
       description="System prompt injected into the agent at rollout time (agentic only).",
   )
-  degenerate_group_masking: bool = Field(
-      True,
-      description="Mask degenerate groups (all-zero advantages) from contributing to loss (agentic only).",
-  )
   epsilon_high: Optional[float] = Field(
       None,
       description="Upper-bound clipping epsilon for GRPO loss. Defaults to epsilon when None (agentic only).",
diff --git b/src/maxtext/trainers/post_train/rl/train_rl.py b/src/maxtext/trainers/post_train/rl/train_rl.py
index bd60747aeb..66a9bd858b 100644
--- b/src/maxtext/trainers/post_train/rl/train_rl.py
+++ b/src/maxtext/trainers/post_train/rl/train_rl.py
@@ -555,7 +555,6 @@ def _reward_fn(**kwargs):
         max_concurrency=trainer_config.rl.max_concurrency,
         off_policy_steps=trainer_config.rl.off_policy_steps,
         system_prompt=trainer_config.rl.system_prompt,
-        degenerate_group_masking=trainer_config.rl.degenerate_group_masking,
         epsilon_high=trainer_config.rl.epsilon_high,
     )
     # Instantiate the custom MaxText chat parser
```
