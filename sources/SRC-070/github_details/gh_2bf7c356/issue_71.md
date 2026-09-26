# [Issue #71] Confues about the Low-latency kernels data issue

source: https://github.com/deepseek-ai/DeepEP/issues/71
state: closed | updated: 2026-09-20T01:56:30Z
labels: 

## 正文

Hello DeepEP developers, appreciate the solid works! 
I have two questions about the Low-latency kernels with pure RDMA displayed on homepage, thanks :
1,  Is the low_latency data displayed the average, maximum or minimum value of all ranks?  Which method makes more sense?
2, Why does the bandwidth decrease as the number of #EP increases?

## 评论 (1)

### sphish · 2025-03-13

1. The performance values indicated in the README are averages, and in a stable network environment, these three values generally only vary by a few microseconds.

2. Here are some potential impacts when the number of #EP increases:
   a. The gap for synchronization becomes larger, and all-to-all communication effectively acts as an implicit synchronization operation.
   b. The NICs needs to handle more sending destinations, which can impact performance.
   c. It becomes more susceptible to network fluctuations and congestion.
   d. There are fewer experts per rank, making load imbalance more apparent.
