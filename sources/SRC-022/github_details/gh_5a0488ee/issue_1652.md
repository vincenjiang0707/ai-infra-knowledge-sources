# [Issue #1652] How to select the rtc frequency in RCCL?

source: https://github.com/ROCm/rccl/issues/1652
state: closed | updated: 2025-04-22T03:26:10Z
labels: Under Investigation

## 正文

Dear developer,

I have noticed that the vega_gpu_rtc_freq  is set to 1.0E8 or 2.5E7 for different topo, can you help to explain why the vega_gpu_rtc_freq chosed like this?
Is there any command to check the rtc frequency real time?


```
      if (strncmp(prop.gcnArchName, "gfx942", 6) == 0)
        vega_gpu_rtc_freq = 1.0E8;
      else
        vega_gpu_rtc_freq = 2.5E7;
```


Thank you.



## 评论 (5)

### ppanchad-amd · 2025-04-21

Hi @shanleo2024.  Internal ticket has been created to assist with your issue. Thanks!

### gilbertlee-amd · 2025-04-21

Hi @shanleo2024 - This code preceded the HIP functionality that allows for querying the wall clock rate:

`hipDeviceGetAttribute(&clockRate, hipDeviceAttributeWallClockRate, deviceId);`

### shanleo2024 · 2025-04-22

Hi @gilbertlee-amd ,can we get the clock rate using this parm? and what is the different?
hipDeviceGetAttribute(&clockRate, **hipDeviceAttributeClockRate**, deviceId);

Actually, in the end, I want to get the time  consumed, can you give me an example kidly?
Thanks.




### gilbertlee-amd · 2025-04-22

The device wall-clock rate is fixed in terms of time and doesn't change on the fly like the device clock rate.

Please refer to: https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html#timer-functions





### shanleo2024 · 2025-04-22

> The device wall-clock rate is fixed in terms of time and doesn't change on the fly like the device clock rate.
> 
> Please refer to: https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_cpp_language_extensions.html#timer-functions

Thank a lot!
