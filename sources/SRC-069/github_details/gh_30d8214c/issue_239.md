# [Issue #239] [Feature Request] Maybe we can add env var to control whether use min sms?

source: https://github.com/deepseek-ai/DeepGEMM/issues/239
state: closed | updated: 2026-01-19T03:44:50Z
labels: 

## 正文

I found in kernel `get_best_config` function, there exist some logic to compute the kernel minimum use sm:
```
// Recompute the minimal number of SMs required
    // NOTES: less L2 cache usage and less GPU frequency drop
    int num_min_sms = num_sms;
    if (ArchSpec::should_minimize_num_sms()) {
        num_min_sms = ceil_div(ceil_div(m, best_block_m) * ceil_div(n, best_block_n) * num_groups, best_num_waves);
        num_min_sms = align(num_min_sms, best_multicast_config.num_multicast);
        DG_HOST_ASSERT(num_min_sms <= num_sms);
    }
```
It invoke kernel compilation many times, which cause unstable ttft time, maybe we should add envvar to control

## 评论 (1)

### MARD1NO · 2026-01-19

The latest version fix this issue
