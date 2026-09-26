# [Issue #3790] Fresh runs can save a checkpoint at step 0 and tensorboard writes unconditionally

source: https://github.com/AI-Hypercomputer/maxtext/issues/3790
state: closed | updated: 2026-05-04T23:41:01Z
labels: bug

## 正文

### Bug report

MaxText appears to perform checkpoints even when setting flags to disable it. In my case, the run used load_parameters_path, enable_checkpointing=True (to enable initial parameter loading), checkpoint_period=1000000 save_checkpoint_on_completion=False, and still attempted checkpoint-related work in a 50 step training run.

The same issue applies to enable_tensorboard, which is ignored by write_setup_info_to_tensorboard.

@giusgal and @janmarxen

### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (1)

### xuefgu · 2026-05-04

If you would like to skip saving checkpoints entirely, you can specify `enable_checkpointing=False`. It doesn't affect using `load_parameters_path` to load a checkpoint. So that should address the first concern.

The tensorboard concern should have been addressed by https://github.com/AI-Hypercomputer/maxtext/pull/3806.
