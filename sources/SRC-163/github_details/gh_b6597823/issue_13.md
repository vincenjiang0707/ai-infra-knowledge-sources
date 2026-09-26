# [Issue #13] How to profile

source: https://github.com/LLMServe/DistServe/issues/13
state: open | updated: 2024-06-14T08:15:00Z
labels: help wanted

## 正文

I want to get the profile data in my own experimental environment. How can I do it?
It seems to be able to do this with this command: "python distserve/example/profile.py --model facebook/opt-1.3b --tokenizer facebook/opt-1.3b --beam_width 1 --file_path <file_path>"
But I didn't find profile.py or similar code.

## 评论 (7)

### interestingLSY · 2024-06-14

Just ignore the profiling file. It is not used in the current scheduler.

### YLSnowy · 2024-06-14

Oh, I mean I want to get my profile data. It is used in all the scripts in "ae-scripts/e2e" or "evaluation/e-benchmark/serving"


### PKUFlyingPig · 2024-06-14

It is only needed when using the simulator to find the optimal placement strategy. If you only have limited number of GPUs, you can manually set the parallelism strategy by yourself.

### YLSnowy · 2024-06-14

> It is only needed when using the simulator to find the optimal placement strategy. If you only have limited number of GPUs, you can manually set the parallelism strategy by yourself.

Yeah. I want to quickly find the best parallel strategy in my experimental environment for e2e latency. I hope to use the simulator instead of the exhaustive method. However, some of the parallel strategies I want to try are not in the profiling data, so can I ask how you profiled them?

### PKUFlyingPig · 2024-06-14

What is the cluster setting? e.g., #nodes, #gpus, GPU type, intra-/inter-node network bandwidth?

### PKUFlyingPig · 2024-06-14

The profiling process is quite straightforward, you profile the forward-pass time of the model under various parallelism strategies to get sufficient data to fit the latency model as proposed in Appendix A of our paper. Then you can use our simulator to find the optimal placement.

### YLSnowy · 2024-06-14

Thank you
