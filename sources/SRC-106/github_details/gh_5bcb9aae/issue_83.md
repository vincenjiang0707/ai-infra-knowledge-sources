# [Issue #83] [Issue]: Clock metrics issue

source: https://github.com/ROCm/amdsmi/issues/83
state: closed | updated: 2025-05-12T15:19:38Z
labels: Under Investigation

## 正文

### Problem Description

We can get correctly all the available clock frequencies with `amdsmi_get_gpu_metrics_info` function, but not with the functions dedicated to the clock information :

- `amdsmi_get_clock_info` : The values that we retrieve are correct, but we can't to obtain all available and really existing clock frequencies on our GPU, I can log that in my program as error :
`Failed to get GPU frequency for AmdsmiClkTypeDf clock type : RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function.`
`Failed to get GPU frequency for AmdsmiClkTypeDcef clock type : RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function.`
`Failed to get GPU frequency for AmdsmiClkTypeSoc clock type : RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function.`
`Failed to get GPU frequency for AmdsmiClkTypePcie clock type : RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function.`

- `amdsmi_get_clk_freq` : Get inconsistent values like "65535" for invalid u16 parameters. Morever, I was able to observe that some variables for invalid metrics are set to "65535" (for exemple for voltage and some other currents values too).

### Operating System

GNU/Linux Red Hat

### CPU

AMD EPYC 7413 24-Core Processor

### GPU

Instinct MI210

### ROCm Version

6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (15)

### ppanchad-amd · 2025-04-07

Hi @victoryeagle77. Internal ticket has been created to investigate your issue. Thanks!

### tcgu-amd · 2025-04-10

Hi @victoryeagle77, thanks for reporting the issue! We have root-caused it and are working on a patch. Thanks! 

### dmitrii-galantsev · 2025-04-10

yeahh looks like a bunch gets set to uintmax by default: https://github.com/ROCm/amdsmi/blob/e46546f4c2e0f84f23ac5e236f895ffeb6d1ae14/src/amd_smi/amd_smi.cc#L2990

### victoryeagle77 · 2025-04-11

A little additional clarification if it can help you :

I'm discovering this for clock metrics when using the Rust interface, but similar issue can be observed, as I said before, for others metrics. 

Comparing the output results provided by the "amd-smi" command with non-accessible values ​​correctly set to print N/A, we have here only 65535.

I have only observed such values ​​for u16 (i.e. 2^16 values) but perhaps this can be extended to other numeric types, I have not had the case so far.

### tcgu-amd · 2025-04-11

Hi @victoryeagle77,

Regarding your first issue, it is caused by an early exit here
https://github.com/ROCm/amdsmi/blob/e46546f4c2e0f84f23ac5e236f895ffeb6d1ae14/src/amd_smi/amd_smi.cc#L3364-L3367
A patch has been risen internally to fix it and is currently under review. 

For your second issue regarding seeing max value for some of the metrics, I am afraid this is just how amd_smi handles N/A cases, as you can see from these lines here:
https://github.com/ROCm/amdsmi/blob/e46546f4c2e0f84f23ac5e236f895ffeb6d1ae14/py-interface/amdsmi_interface.py#L2425-L2427
, also this function:
https://github.com/ROCm/amdsmi/blob/e46546f4c2e0f84f23ac5e236f895ffeb6d1ae14/py-interface/amdsmi_interface.py#L679-L699

### tcgu-amd · 2025-04-11

Hey @victoryeagle77, what kind of outputs are you looking for regarding the  `AmdsmiClkTypeDcef ` and `AmdsmiClkTypePcie` clock types? 

I am asking because even with `amdsmi_get_gpu_metrics_info`, only these clock frequencies will be returned

https://github.com/ROCm/amdsmi/blob/e46546f4c2e0f84f23ac5e236f895ffeb6d1ae14/rocm_smi/include/rocm_smi/rocm_smi.h#L1194-L1200


### victoryeagle77 · 2025-04-11

Except for current_vclk1 and current_dclk1 which return 65535 (but this is apparently normal because they are not socialized or exist according to the comment above), I have consistent frequencies (when I run encoding with ffmpeg each of those values increase consistently)

### tcgu-amd · 2025-04-11

@victoryeagle77, thanks for the quick response! In other words, the list of the clocks above is conclusive of the clock information you are looking for? Am I correct in assuming that you are not looking for frequencies for the PCIE and DCEF clocks? In which case, getting 
`Failed to get GPU frequency for AmdsmiClkTypePcie clock type : RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function.`
and 
`Failed to get GPU frequency for AmdsmiClkTypeDcef clock type : RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function.`
should be expected. 

### victoryeagle77 · 2025-04-14

While it would be nice to have them, what I'm really looking for is to get the same clocks that I'm able to retrieve here:

uint16_t current_gfxclk;
uint16_t current_socclk;
uint16_t current_uclk;
uint16_t current_vclk0;
uint16_t current_dclk0;
uint16_t current_vclk1;

But with the Rust function `amdsmi_get_clock_info`, which, by the way, is very well done and catches errors accurately.

### tcgu-amd · 2025-04-14

@victoryeagle77, Sorry, just to make sure, are you not able to retrieve them right now? Based on your error log the only ones that cannot be retrieved should be  `Df, DCEF, SOC , PCIE` types. 

### victoryeagle77 · 2025-04-14

Yeah sorry, I didn't write the whole error log but just the ones with a specific error returned, but currently via the `amdsmi_get_gpu_metrics_info` I can't get these clocks :

- `Df`
- `Dcef`
- `Soc`
- `Pcie`
- `Vclk0`
- `Vclk1`
- `Dclk0`
- `Dclk1`

### tcgu-amd · 2025-04-15

@victoryeagle77 Ah I see, thanks for the clarification! 

Edit: I was just trying to make sure we were understanding the issue correctly. So you are getting 65535 for these clocks instead of an error, is that correct? 

### victoryeagle77 · 2025-04-24

The real problem is that the `amdsmi_get_clock_info` function collects fewer clock frequency metrics than `amdsmi_get_gpu_metrics_info`, we can almost get all clock frequencies with `amdsmi_get_gpu_metrics_info` (exept Dclk1 and Vclk1 but I think it's normal) but only 2 clocks with `amdsmi_get_clock_info`, the others can't be retrieved. 

### tcgu-amd · 2025-05-07

@victoryeagle77, Hi, I think [this commit](https://github.com/ROCm/amdsmi/commit/4d92dea079814e8afa777f94750fd42cc848e77c), now part of amd-mainline, should be able to fix your issue. If it works please let us know. Thanks! 

### tcgu-amd · 2025-05-12

I will be closing this issue for now. However, please feel free to re-open if the issue persists. Thanks! 
