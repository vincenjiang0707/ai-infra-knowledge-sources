# [Issue #231] In getkacc(), should 'total[kk]' be updated when pre_len+kk>=seq_len?

source: https://github.com/SafeAILab/EAGLE/issues/231
state: closed | updated: 2025-06-05T17:48:18Z
labels: 

## 正文

Hi, thank you for sharing this excellent work.

While reviewing the getkacc() function, I noticed that when the k-th predicted token is incorrect, the following code updates total[kk] for subsequent steps:

```
else:
  for kk in range(k + 1, max_length):
      total[kk] += 1
```

However, it seems that total[kk] may still be incremented even when there is no valid target token to compare, especially when pre_len + kk >= seq_len.

For example:

Assume seq_len = 2048

pre_len = 2046, and max_length = 5

Then pre_len + kk can become 2049, which is beyond the valid sequence range. In this case, total[kk] will be incremented, although there is no corresponding ground-truth token to evaluate against.

Would it be more appropriate to add a condition such as:


```
else:
  for kk in range(k + 1, max_length):
    if pre_len + kk >= seq_len or loss_mask[bid, pre_len + kk] == 0:
        break
    total[kk]+=1
```
to avoid including invalid steps in the metric?

Looking forward to your clarification—thanks again for your work!

## 评论 (1)

### hongyanz · 2025-05-23

It is based on the rule that if one previous token is rejected, we deem all remaining tokens (up until max_length) will be rejected, even though the token id might be out of the boundary. You are also right, just with a different definition of acc. The two definitions of acc should vary very little.
