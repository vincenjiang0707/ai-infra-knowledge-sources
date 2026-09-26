# [Issue #670] [BUG] DeepEPv2 internode num_worst_tokens tests

source: https://github.com/deepseek-ai/DeepEP/issues/670
state: closed | updated: 2026-08-26T03:19:36Z
labels: 

## 正文

**Error log:**
```log
Traceback (most recent call last):
  File "/home/test/DeepEP/tests/legacy/test_internode.py", line 395, in <module>
    torch.multiprocessing.spawn(test_loop, args=(num_processes, args), nprocs=num_processes)
  File "/home/test/DeepEP/venv/lib/python3.10/site-packages/torch/multiprocessing/spawn.py", line 340, in spawn
    return start_processes(fn, args, nprocs, join, daemon, start_method="spawn")
  File "/home/test/DeepEP/venv/lib/python3.10/site-packages/torch/multiprocessing/spawn.py", line 296, in start_processes
    while not context.join():
  File "/home/test/DeepEP/venv/lib/python3.10/site-packages/torch/multiprocessing/spawn.py", line 211, in join
    raise ProcessRaisedException(msg, error_index, failed_process.pid)
torch.multiprocessing.spawn.ProcessRaisedException: 

-- Process 0 terminated with the following error:
Traceback (most recent call last):
  File "/home/test/DeepEP/venv/lib/python3.10/site-packages/torch/multiprocessing/spawn.py", line 87, in _wrap
    fn(i, *args)
  File "/home/test/DeepEP/tests/legacy/test_internode.py", line 341, in test_loop
    ref_hash += test_main(args, i, local_rank, num_local_ranks, num_ranks, num_nodes, rank, buffer, group,
  File "/home/test/DeepEP/tests/legacy/test_internode.py", line 179, in test_main
    recv_worst_x, recv_worst_topk_idx, recv_worst_topk_weights, empty_list, _, event = buffer.dispatch(**dispatch_args)
  File "/home/test/DeepEP/venv/lib/python3.10/site-packages/deep_ep-2.0.0+local-py3.10-linux-x86_64.egg/deep_ep/buffers/legacy.py", line 379, in dispatch
    assert num_worst_tokens == 0, 'Internode dispatch does not support `num_worst_tokens > 0`'
AssertionError: Internode dispatch does not support `num_worst_tokens > 0`
```


**When testing DeepEP v2 internode mode with with_topk enabled, the code will assign a value to num_worst_tokens.**

https://github.com/deepseek-ai/DeepEP/blob/main/tests/legacy/test_internode.py#L175
```py
                    # Test `num_worst_tokens != 0`
                    if with_topk:
                        num_worst_tokens = num_tokens * num_ranks
                        dispatch_args.update({'num_worst_tokens': num_worst_tokens})
                        recv_worst_x, recv_worst_topk_idx, recv_worst_topk_weights, empty_list, _, event = buffer.dispatch(**dispatch_args)
                        event.current_stream_wait() if async_mode else ()
                        recv_worst_x = per_token_cast_back(*recv_worst_x) if isinstance(recv_worst_x, tuple) else recv_worst_x
                        assert len(empty_list) == 0
                        assert num_worst_tokens == recv_worst_x.size(0)
                        assert num_worst_tokens == recv_worst_topk_idx.size(0)
                        assert num_worst_tokens == recv_worst_topk_weights.size(0)
                        assert torch.equal(recv_x, recv_worst_x[:recv_x.size(0)])
                        assert torch.equal(recv_topk_idx, recv_worst_topk_idx[:recv_x.size(0)])
                        assert torch.equal(recv_topk_weights_clone, recv_worst_topk_weights[:recv_x.size(0)])
                        assert torch.all(recv_worst_topk_idx[recv_x.size(0):] == -1).item()
```

**However, there is a strict assertion check inside Buffer::dispatch for multi-RDMA-rank internode scenarios:**


https://github.com/deepseek-ai/DeepEP/blob/main/deep_ep/buffers/legacy.py#L378
```py
        # Internode
        if self.runtime.get_num_rdma_ranks() > 1:
            assert num_worst_tokens == 0, 'Internode dispatch does not support `num_worst_tokens > 0`'
            return self.internode_dispatch(x, handle, num_tokens_per_rank, num_tokens_per_rdma_rank, is_token_in_rank,
                                           num_tokens_per_expert, topk_idx, topk_weights, expert_alignment, config, previous_event,
                                           async_finish, allocate_on_comm_stream)
```

**Could we resolve the incompatibility between with_topk and internode dispatch, or add parameter pre-judgment to avoid this conflict?**


## 评论 (2)

### GeofferyGeng · 2026-06-23

Temporary fix: comment out relevant code in internode tests.

### tommy85 · 2026-08-18

This is fixed by #697 (the `num_worst_tokens != 0` block in `tests/legacy/test_internode.py` is dead code copy-pasted from the intranode test — internode dispatch rejects `num_worst_tokens > 0` by design). Reproduced and verified on a 2-node × 8-GPU H20 cluster: with that block skipped, the legacy internode suite passes 32/32 sub-cases. Details in https://github.com/deepseek-ai/DeepEP/pull/697#issuecomment-5328539472
