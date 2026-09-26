# [Issue #2171] nixlbench error message on exit: "ERROR cuDevicePrimaryCtxGetState"

source: https://github.com/ai-dynamo/nixl/issues/2171
state: closed | updated: 2026-08-31T07:41:04Z
labels: 

## 正文

When I run nixlbench I get an error message at exit:
```
nixlbench --initiator_seg_type=VRAM --target_seg_type=VRAM --start_block_size=65536 --max_block_size=65536

cuda_ctx.c:23   UCX  ERROR cuDevicePrimaryCtxGetState(cuda_device, &flags, &active) failed: unrecognized error code 4
```


## 评论 (1)

### iyastreb · 2026-08-27

https://github.com/openucx/ucx/pull/11846
