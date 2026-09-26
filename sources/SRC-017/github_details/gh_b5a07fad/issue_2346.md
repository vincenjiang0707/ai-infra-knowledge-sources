# [Issue #2346] [Issue]: NCCL RAS null communicator status leading to segfault on 2.29.7

source: https://github.com/NVIDIA/nccl/issues/2346
state: open | updated: 2026-08-27T16:07:45Z
labels: bug, triaged, ongoing

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

I've attached the torch script that I used to reproduce the issue:
- Only reproduces on 256 GPUs
- Have been able to reproduce on H200 and B200
- Only attempted to reproduce on x86 hardware

The theory is that the null `status` values appear when a communicator is being initialized, so this script churns communicators.

I was working with an AI agent to create the reproduction, and it presented a pretty compelling theory for where these null `status` values might originate: https://github.com/NVIDIA/nccl/blob/b91894bd5b190c874d98a017f93f5daa515b65d0/src/ras/collectives.cc#L684-L687

When `ncclComms[commIdx]` resolves to an uninitialized communicator, we `continue` which increments `collCommIdx` instead of `commIdx`. On the next iteration, `commIdx` is unchanged and `ncclComms[commIdx]` resolves to the same invalid communicator. I think this causes us not to fill the memory that is meant to contain valid communicators.

Downstream, I believe this can materialize as a segfault when RAS is formatting the output string. This happens because `status` is passed into CLZ, which is undefined when the input is zero: https://github.com/NVIDIA/nccl/blob/b91894bd5b190c874d98a017f93f5daa515b65d0/src/ras/client_support.cc#L1207

I switched to using the JSON serialization path, and the segfault did not reproduce (though I was still seeing null `status` values).

[nccl_ras_status_repro.py](https://github.com/user-attachments/files/31151362/nccl_ras_status_repro.py)
[nccl_ras_status_repro.txt](https://github.com/user-attachments/files/31152022/nccl_ras_status_repro.txt)

### NCCL Version

2.29.7

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (3)

### kiskra-nvidia · 2026-08-24

Thank you for the report! This code was a workaround added in NCCL 2.27 I think, to fix a race condition between when NCCL communicators are registered with RAS and when their internal state is sufficiently initialized for RAS purposes. As you found out, the workaround itself has a bug 🫤.

We could fix the bug in the workaround but I now realize that the workaround itself is subject to race conditions, so we should instead replace it with a proper fix. Due to a tight schedule it might take until NCCL 2.33 to get this fixed...

### cphalen · 2026-08-26

Thanks for the update! By the way, I've been able to mitigate this by swapping RAS to JSON mode. We still see `null` column values occasionally when communicators are initializing, but they don't cause segfaults.

### xman1979 · 2026-08-27

could you provide a patch @kiskra-nvidia 
