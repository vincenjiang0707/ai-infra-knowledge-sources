# [Issue #121] [Documentation]: Clarification "performance determinism"

source: https://github.com/ROCm/amdsmi/issues/121
state: closed | updated: 2025-10-07T15:19:16Z
labels: Under Investigation

## 正文

### Description of errors

The doc says:

This function will enable performance determinism mode, which enforces a
GFXCLK frequency SoftMax limit per GPU set by the user. This prevents the
GFXCLK PLL from, stretching when running the same workload on different
GPUS, making performance variation minimal. https://github.com/ROCm/amdsmi/blob/28084cbbd60dc225ba11663447c4cdd969e27593/include/amd_smi/amdsmi.h#L3919

Assuming an mi250x with a freqrange of 800-1700 MHz.

How does rocm-smi --setperfdeterminism 1700 differs from rocm-smi --setsrange 800 1700 and from rocm-smi -r (which should reset to a default range of 800-1700).

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_

## 评论 (3)

### etiennemlb · 2025-09-10

AFAIK; the stretching would imply a frequency spiking above the specified frequency. In perf determinism mode, we constrain the PLL to not produce a single that clocks higher than say, 1700 MHz.

But then, I have a workload that I run on a single GCD (there are 2 on an MI250X), and I get better perf (x1.089) using setperfdeterminism than by simply setting the freq range from 800 to 1700.

### ppanchad-amd · 2025-09-10

Hi @etiennemlb. Internal ticket has been created to assist you. Thanks!

### darren-amd · 2025-09-25

Hi @etiennemlb,

Thanks for the question. Determinism mode is usually used to ensure the same performance across different systems, which may be useful for activities such as kernel benchmarking. For this mode, there is an extra margin given to the voltage over the default compared to setting clock frequency with `setsrange`, or reseting to the default. This may explain the slight performance increase you are observing, however this is not guaranteed and the performance would depend on the workload. 
