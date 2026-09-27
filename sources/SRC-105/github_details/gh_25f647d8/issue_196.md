# [Issue #196] Questions about privilege

source: https://github.com/NVIDIA/DCGM/issues/196
state: open | updated: 2025-10-01T14:46:50Z
labels: 

## 正文

Hi, 
I found on the [DCGM document](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/getting-started.html#:~:text=In%20both%20modes%20the%20DCGM%20library%20should%20be%20run%20as%20root): the Embedded Mode should be run as root. Some 3rd-party DCGM Agent like [dcgm-exporter](https://github.com/NVIDIA/dcgm-exporter) will raise runtime error: "FATA[0000] Failed to watch metrics: Error watching fields: Host engine is running as non-root." without SYS_ADMIN privilege. And the error might be raised by [dcgmWatchFields](https://github.com/NVIDIA/DCGM/blob/903d745504f50153be8293f8566346f9de3b3c93/dcgmlib/dcgm_agent.h#L943C30-L943C45) interface.
I wonder what operation in dcgmWatchFields is checking the privilege, and Could there be a non-privilege solution for agents to just extract the metrics?

## 评论 (3)

### qaccd · 2024-11-04

+1, why would dcgm require the sysadmin privilege to function properly???? 

### jksjaz · 2025-01-24

I recently started exploring dcgm api and I might be wrong here but I believe it's because of the lock on the hardware when you read stats from it. Possible that needs elevated privileges to execute at low level.

### bluayer · 2025-10-01

Is there any updates? I just wanna know latest dcgm still needs SYS_ADMIN
