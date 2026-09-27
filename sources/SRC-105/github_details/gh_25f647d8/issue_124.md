# [Issue #124] How do I inject errors into the GPU hardware?

source: https://github.com/NVIDIA/DCGM/issues/124
state: closed | updated: 2026-01-28T21:18:29Z
labels: 

## 正文

https://github.com/NVIDIA/DCGM/blob/cc3fe64d966d956cebba3e3ff1334786dd767d35/dcgmlib/src/DcgmCacheManager.cpp#L4878C21-L4878C21
Hi, I'm using the error injection function of dcgm, and from the code, I don't find that the error is actually injected into the GPU hardware. I'd like to ask, is there any way to inject real errors into GPU hardware, such as ECC Errors?

## 评论 (7)

### glowkey · 2023-10-30

There is no way to inject the error into the GPU hardware. The injection API only injects the error into DCGM's internal cache.

### yaoyinnan · 2024-12-20

@glowkey I need your help. Can the xid fault injected by dcgmi be monitored by `nvml.WaitForEvent`? For example, when using `dcgmi test --inject --gpuid 0 -f 230 -v 79` to inject a fault, it seems that only dcgmi's own `dcgmi policy --reg` can monitor it.
If I want to simulate injecting a fault that nvml can monitor, how can I implement it?

### nikkon-dev · 2024-12-20

@yaoyinnan,

I'd say this is mostly impossible to do in a general case. NVML works in a process and directly communicates with the driver. Another process cannot "inject" anything into this communication. This could be quasi-solved if you use a proxy between the NVML and your application in a way that you call a proxy function instead of the NVML one. This way, you are in control of what that function returns, and you can check how your application reacts to this.

We did a similar solution for our testing needs, and you can check it [here](https://github.com/NVIDIA/DCGM/tree/master/nvml-injection)

### jiayelamazon · 2026-01-28

Is there anyway we can inject error and let DCGM diagnostic test to fail? How can we mock a failed DCGM diagnostic test? 

### maxweiss · 2026-01-28

> Is there anyway we can inject error and let DCGM diagnostic test to fail? How can we mock a failed DCGM diagnostic test?

For example:
```
dcgmi test --inject --gpuid 0 -f 202 -v 99999
```

See https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-error-injection.html.

### jiayelamazon · 2026-01-28

Have tried to use the following but the diagnostic test Level 2 still passed. 
Is there any other config we need to set like loop?

```
dcgmi test --inject --gpuid 0 -f 202 -v 99999
```

```
PCIe replay count: 99999
Timestamp: Wed Jan 28 00:34:23 2026
A PCIe replay event has violated policy manager values.
PCIe replay count: 99999
```

```
dcgmi diag -r 2 -i 0
Successfully ran diagnostic for group.
+---------------------------+------------------------------------------------+
| Diagnostic                | Result                                         |
+===========================+================================================+
|-----  Metadata  ----------+------------------------------------------------|
| DCGM Version              | 4.4.2                                          |
| Driver Version Detected   | 580.105.08                                     |
| GPU Device IDs Detected   | 2237                                           |
|-----  Deployment  --------+------------------------------------------------|
| software                  | Pass                                           |
|                           | GPU0: Pass                                     |
+-----  Hardware  ----------+------------------------------------------------+
| memory                    | Pass                                           |
|                           | GPU0: Pass                                     |
+-----  Integration  -------+------------------------------------------------+
| pcie                      | Pass                                           |
|                           | GPU0: Pass                                     |
+---------------------------+------------------------------------------------+
```


### nikkon-dev · 2026-01-28

@jiayelamazon,

The diagnostics only check for the errors that happen after the diag is run. It ignores any errors prior to the diag start time.
