# [Issue #185] [Issue]: `amdsmi_get_cpusocket_handles` does not give socket handles

source: https://github.com/ROCm/amdsmi/issues/185
state: closed | updated: 2026-03-23T15:23:32Z
labels: 

## 正文

### Problem Description

Hello,

Running:

```python
import amdsmi

amdsmi.amdsmi_init()

device_handles = amdsmi.amdsmi_get_processor_handles()

print("gpu device_handles", device_handles)

cpu_device_handles = amdsmi.amdsmi_get_cpusocket_handles()

print("cpu_device_handles", cpu_device_handles)

for device_handle in cpu_device_handles:
    power_info = amdsmi.amdsmi_get_cpu_socket_power(device_handle)  # current power in Watt
    print(power_info["socket_power"])
```

I get:


```
gpu device_handles [c_void_p(738491984), c_void_p(738001072), c_void_p(740803792), c_void_p(740804880), c_void_p(740805248), c_void_p(740805568), c_void_p(740805936), c_void_p(740806304)]
cpu_device_handles []
```

Do you know why no cpu device handles are returned? Does it require some dependency?

Thank you!

(using `amdsmi.__version__ == 26.0.0+37d158ab`)

### Operating System

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 9575F 64-Core Processor

### GPU

AMD Instinct MI355X

### ROCm Version

7.2.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### fxmarty-amd · 2026-03-20

Maybe related to https://github.com/ROCm/amdsmi/issues/84#issuecomment-3628662676 ?

### fxmarty-amd · 2026-03-23

Solved.

One needs:

```python
amdsmi.amdsmi_init(amdsmi.AmdSmiInitFlags.INIT_ALL_PROCESSORS)
```

and in case hitting `AMDSMI_STATUS_FAIL_LOAD_SYMBOL` later on:

- have amdsmi compiled with `-DENABLE_ESMI_LIB=1`
- Load `hsmp_acpi` module from https://github.com/amd/amd_hsmp
- Launch docker container with `--device=/dev/hsmp --device=/dev/cpu -v /sys:/sys:ro`
