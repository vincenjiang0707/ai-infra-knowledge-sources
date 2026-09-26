# [Issue #336] Question about Nsight Compute results for sm100_fp8_fp4_mega_moe_impl on B300/Blackwell

source: https://github.com/deepseek-ai/DeepGEMM/issues/336
state: open | updated: 2026-07-01T04:58:54Z
labels: 

## 正文


## Question about Nsight Compute results for `sm100_fp8_fp4_mega_moe_impl` on B300/Blackwell

Hi, thanks for providing the `scripts/run_ncu_mega_moe.sh` script.

I am trying to profile the Mega-MoE kernel on B300/Blackwell using Nsight Compute. The code provides `scripts/run_ncu_mega_moe.sh`, and I modified the `ncu_args` by adding `--set full` in order to collect more metrics.

The relevant NCU arguments are:

```bash
ncu_args=(
    --config-file off
    --force-overwrite
    --kernel-name sm100_fp8_fp4_mega_moe_impl
    --import-source yes
    --replay-mode application
    --section PmSampling
    --section SourceCounters
    --rule LocalMemoryUsage
    --set full
    --launch-skip 0
    --launch-count 1
    --lockstep-kernel-launch
    --communicator tcp
    --clock-control none
    --pm-sampling-interval 1000
    --pm-sampling-max-passes 1
    --disable-pm-warp-sampling
    --communicator-tcp-num-peers "$num_processes"
    --kill yes
    --app-replay-buffer memory
)
````

However, the generated NCU report shows very low utilization:

* SM throughput is only around **1%**
* Memory throughput is only around **7%**

The detailed throughput numbers are also very low, as shown in the screenshots below.

![NCU Speed of Light / Throughput screenshot](https://github.com/user-attachments/assets/1c97393a-f33c-4c29-8926-81637802b821)

![NCU detailed metrics screenshot](https://github.com/user-attachments/assets/490bfc53-10b3-4951-9a9c-09b178cc1525)

I am not sure whether this result is expected.

My understanding is that this kernel should use Blackwell-specific features such as:

* UMMA / `tcgen05.mma` for matrix computation
* TMA for memory movement
* Tensor Memory / TMEM as part of the Blackwell MMA pipeline

So I would not expect the overall SM and memory utilization to be this low, unless the standard Nsight Compute `SpeedOfLight` metrics do not properly reflect UMMA/TMA/TMEM activity, or unless I am collecting the wrong metrics.

Could you please clarify the following?

1. Is it expected that the standard NCU `SpeedOfLight` page reports such low SM and memory utilization for this Mega-MoE kernel on B300/Blackwell?

2. Does `--set full` include the right metrics for analyzing Blackwell UMMA/TMA/TMEM usage, or should I explicitly collect metrics such as:

```bash
sm__inst_executed_pipe_tc.sum
sm__inst_executed_pipe_tc.avg.pct_of_peak_sustained_elapsed
sm__inst_executed_pipe_tma.sum
sm__inst_executed_pipe_tma.avg.pct_of_peak_sustained_elapsed
sm__inst_executed_pipe_tmem.sum
sm__inst_executed_pipe_tmem.avg.pct_of_peak_sustained_elapsed
sass__inst_executed_per_opcode
sass__inst_executed_per_opcode_pipeline
```


3. Is there a recommended Nsight Compute command or metric set for profiling this kernel on B300/Blackwell, especially for checking UMMA, TMA, Tensor Memory, and NVLink/communication behavior?

I would like to understand whether the low utilization numbers indicate a real performance issue, or whether they are simply not the right metrics for this Blackwell Mega-MoE kernel.

Thanks!


## 评论 (1)

### wenqinI · 2026-07-01

what's your `num-tokens` and how many GPUs did you use? did you use the default value 8192 for the `num-tokens` ? if so I guess there is a communication bound, which means all most of time is running on NVLink, so the utilization of tensor core and HBM is low.
