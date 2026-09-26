# [Issue #1508] [DLRM_v2] Torch Reshape Error during loading model weights

source: https://github.com/mlcommons/inference/issues/1508
state: closed | updated: 2026-05-11T00:43:14Z
labels: Stale

## 正文

I set up the (CPU) docker container, processed the dataset, and downloaded the model weights as mentioned in the README file. When I try to run the benchmark with dummy weights on the full dataset (eg, `./run_local.sh multihot-criteo cpu --max-ind-range=10000000 --debug`) it runs fine and reports stats. However, when I try to use the actual model weights (by removing the `--debug` option), it results in the following error:
```
Loading model weights...
INFO:torchsnapshot.scheduler:Set process memory budget to 34359738368 bytes.
Traceback (most recent call last):
  File "python/main.py", line 566, in <module>
    main()
  File "python/main.py", line 448, in main
    model = backend.load(args.model_path, inputs=args.inputs, outputs=args.outputs)
  File "/root/mlcommons/recommendation/dlrm_v2/pytorch/python/backend_pytorch_native.py", line 137, in load
    snapshot.restore(app_state={"model": self.model})
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/snapshot.py", line 411, in restore
    event_loop=event_loop,
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/snapshot.py", line 662, in _load_stateful
    event_loop=event_loop,
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/scheduler.py", line 459, in sync_execute_read_reqs
    rank=rank,
  File "/opt/anaconda3/lib/python3.7/asyncio/base_events.py", line 579, in run_until_complete
    return future.result()
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/scheduler.py", line 437, in execute_read_reqs
    read_pipeline: _ReadPipeline = d.result()
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/scheduler.py", line 377, in consume_buffer
    await self.read_req.buffer_consumer.consume_buffer(self.buf, executor)
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/io_preparers/sharded_tensor.py", line 300, in consume_buffer
    buf=buf, entry=self.entry
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/io_preparers/tensor.py", line 324, in deserialize_tensor
    memoryview(buf), dtype=dtype, shape=entry.shape
  File "/root/.local/lib/python3.7/site-packages/torchsnapshot/serialization.py", line 244, in tensor_from_memoryview
    return torch.reshape(torch.frombuffer(mv, dtype=dtype), shape)
RuntimeError: shape '[1048576, 128]' is invalid for input of size 65536000
```

I assume there is something wrong with the `.snapshot_metadata` file, but I am not sure what the correct dimensions should be/how to fix it. I would appreciate it if someone could throw some light on the issue.

## 评论 (1)

### github-actions[bot] · 2026-05-11

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
