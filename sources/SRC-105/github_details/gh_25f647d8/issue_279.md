# [Issue #279] Hang detection feature introduced in 4.4.2 floods logs

source: https://github.com/NVIDIA/DCGM/issues/279
state: open | updated: 2026-07-15T20:04:12Z
labels: 

## 正文

We recently noticed that after updating to DCGM 4.4.2, `/var/log/nv-hostengine.log` would grow to several gigabytes in size in a matter of a few days. This is due to messages produced by the hang detection feature introduced in 4.4.2 every 60 seconds that look like this:

```
2026-02-09 15:31:15.504 ERROR [5066:5080] Failed to compute current fingerprint for 24299/0 [/builds/dcgm/dcgm/common/HangDetect.cpp:193] [HangDetect::IsHungImpl]
2026-02-09 15:31:15.504 ERROR [5066:5080] Error checking hang state for process 24299: -14 [/builds/dcgm/dcgm/common/HangDetectMonitor.cpp:237] [HangDetectMonitor::CollectTaskUpdates]
```

This pair of messages is repeated every 60 seconds for a list of process IDs (I assume 24299 is a PID here) that grows over time. No processes exist under the reported PIDs. It seems like the mechanism leaks processes that it tries to track, but which just disappear and then the mechanism keeps complaining about them incessantly.

We found that we can trigger a process leak by running `dcgm diag`, `-r 2` leaks one additional process ID, `-r 3` leaks two. This exacerbates the issue for us, since we regularly run DCGM diagnostics as part of automated health checking. By the time we noticed the issue, the list of processes that the mechanism complains about every minute had grown to about a thousand, which results in 250 MB of log file growth per day. Not sure if actual compute workloads trigger the issue as well.

We reliably observe this issue on `x86_64` on different GPUs from the Volta, Ampere, and Hopper generations. We have not seen the issue on Grace Hopper so far.

DCGM 4.5.2 still shows the issue.

We currently work around the issue by disabling the hang detection mechanism by setting the environment variable `DCGM_HANGDETECT_DISABLE`.

## 评论 (1)

### nerscchris · 2026-07-15

Can confirm seeing the same huge log file sizes here too.
