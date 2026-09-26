# [Issue #72] [Puzzle] Level1 cumsum_exclusive

source: https://github.com/ScalingIntelligence/KernelBench/issues/72
state: closed | updated: 2025-12-24T17:03:39Z
labels: bug

## 正文

The exclusive cumsum is the prefix sum that doesn't include the current element.

Input processing on KernelBench is implemented by prepending a zero along the scan dimension and discarding the last element:
```
exclusive_cumsum = torch.cat(
        (torch.zeros_like(x.select(self.dim, 0).unsqueeze(self.dim)), x),
        dim=self.dim
    )[:-1]
```

However, [:-1] seems to reduce the **batch dim** instead of the **scan dim**.
Is this intentional?

For example, given an input of shape `(128, 4000)` and `dim=1`:
1. t1= torch.cat((torch.zeros_like(x.select(self.dim, 0).unsqueeze(self.dim)), x), dim=self.dim)  -> (128, 4001)
2. exclusive_cumsum  = t1[:-1] -> (127, 4001)
3. return torch.cumsum(exclusive_cumsum, dim=self.dim)  ->  (127, 4001)



## 评论 (1)

### simonguozirui · 2025-12-24

Thanks for spotting and carefully highlighting the issue @AKatydid! You are right that [:-1] always slices dim 0, and we need to slice/narrow along `self.dim`. 

@bkal01 and I are putting in a fix in #109. We will compute exclusive cumsum this way

```
  def forward(self, x):
      cumsum = torch.cumsum(x.narrow(dim=self.dim, start=0, length=x.size(self.dim)-1), dim=self.dim)
      return torch.cat((torch.zeros_like(x.select(self.dim, 0).unsqueeze(self.dim)), cumsum), dim=self.dim)
```
This implementation assumes that the scan dimension has non-zero length.

This way with your example of input of shape (128, 4000) and self.dim=1:
- `x.narrow(dim=1, start=0, length=3999)` — drops the last element along the scan dimension, producing `x_short = x[:, 0:3999]` with shape `(128, 3999)`
- `torch.cumsum(x_short, dim=1)` — computes an **inclusive cumulative** sum along the scan dimension, yielding `cumsum` with shape `(128, 3999)`
- `torch.zeros_like(x.select(1, 0).unsqueeze(1))` — creates a zero tensor to prepend as the identity element for an exclusive scan, with shape `(128, 1)`
- `torch.cat((zeros, cumsum), dim=1)` — prepends zeros to shift the cumsum by one position and restore the original length, producing the exclusive cumsum with shape `(128, 4000)`

Thank you so much for your contribution and help!

