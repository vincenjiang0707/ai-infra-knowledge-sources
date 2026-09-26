# [Issue #47] Question：Why use torch.cuda.Event instead of torch.profiler for performance measurement?

source: https://github.com/ScalingIntelligence/KernelBench/issues/47
state: open | updated: 2025-10-12T03:51:05Z
labels: 

## 正文

Hi~  I've noticed that using torch.cuda.Event for measuring kernel performance can lead to significant timing variance across multiple runs, affecting stability. Given that torch.profiler offers more stable and robust measurements of pure kernel execution time, was there a specific reason for choosing cuda.Event in the benchmark's design?

## 评论 (3)

### yuxuan-z19 · 2025-07-03

Agree. Given that tools like `torch.profiler`, `nsys`, or `ncu` provide more stable and precise kernel-level timing — as also adopted in [sakana.ai's leaderboard](https://pub.sakana.ai/ai-cuda-engineer/leaderboard) — I'm wondering if there's a specific reason behind choosing cuda.Event here? 
Switching to system-level profilers could make the benchmarking results more robust and reliable. Would love to hear your thoughts!

### wqd008 · 2025-09-23

I also have this question. But there was a blog (https://www.speechmatics.com/company/articles-and-news/timing-operations-in-pytorch) shows the usage of `torch.cuda.event` for accurate measurement. I wonder which one should I use: `torch.cuda.event` or `torch.profiler` ? And what is the difference?

### yuxuan-z19 · 2025-10-12

For CUDA kernel profiling, you might find this implementation **more practical and professional**: [robust_kbench’s cuda_profile.py](https://github.com/SakanaAI/robust-kbench/blob/main/robust_kbench/primitives/cuda_profile.py?utm_source=chatgpt.com)
