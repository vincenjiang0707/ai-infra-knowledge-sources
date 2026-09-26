# [Issue #868] Unable to recover after checkpoint saving

source: https://github.com/AI-Hypercomputer/maxtext/issues/868
state: closed | updated: 2026-04-28T19:25:40Z
labels: bug

## 正文

I am suddenly seeing crashes after saving checkpoints. This is with code that did run perfectly earlier. However, it is after a system reinstall. Wonder if someone have seen the same issue.

The checkpoints are successfully saved. Training is however not recovering, and crashing with this error:
```
I0907 22:26:01.536684 139725339944960 utils.py:253] [process=24][thread=MainThread] Waiting with jax/sync_global_devices("CheckpointManager:old_steps_to_remove.20000")
I0907 22:26:01.539081 139725339944960 utils.py:260] [process=24][thread=MainThread] Done waiting with jax/sync_global_devices("CheckpointManager:old_steps_to_remove.20000")
I0907 22:26:01.539187 139725339944960 checkpoint_manager.py:1744] [host=24][thread=MainThread][step=20000] CheckpointManager Save Finalize is syncing with other hosts...
Traceback (most recent call last):
  File "/home/perk/maxtext/MaxText/train.py", line 687, in <module>
    app.run(main)
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/absl/app.py", line 308, in run
    _run_main(main, args)
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/absl/app.py", line 254, in _run_main
    sys.exit(main(argv))
  File "/home/perk/maxtext/MaxText/train.py", line 683, in main
    train_loop(config)
  File "/home/perk/maxtext/MaxText/train.py", line 606, in train_loop
    if save_checkpoint(checkpoint_manager, int(step), state, config.dataset_type, data_iterator):
  File "/home/perk/maxtext/MaxText/train.py", line 184, in save_checkpoint
    return checkpoint_manager.save(
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1253, in save
    self._finalize(step, steps_to_remove)
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 1751, in _finalize
    barrier_sync_fn = self._create_thread_safe_barrier_sync_fn()
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/orbax/checkpoint/checkpoint_manager.py", line 722, in _create_thread_safe_barrier_sync_fn
    or multihost.get_barrier_sync_fn(
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/orbax/checkpoint/multihost/utils.py", line 154, in get_barrier_sync_fn
    client = _get_jax_distributed_client()
  File "/home/perk/maxtext-env/lib/python3.10/site-packages/orbax/checkpoint/multihost/utils.py", line 113, in _get_jax_distributed_client
    raise ValueError(
ValueError: Distributed system is not available; please initialize it via `jax.distributed.initialize()` at the start of your program.
I0907 22:26:01.596143 139677066847808 grain_pool.py:397] Grain pool is exiting.     
```

## 评论 (3)

### jonb377 · 2024-09-17

Thanks for reporting! A patch is in the works in https://github.com/google/maxtext/pull/895.

As an immediate workaround, you can enable async checkpointing with the config `async_checkpointing=true`, which initializes the jax distributed client.

### peregilk · 2024-09-18

Awesome. Thanks. 

### gobbleturk · 2026-04-28

Closing as this is likely solved / obsolete
