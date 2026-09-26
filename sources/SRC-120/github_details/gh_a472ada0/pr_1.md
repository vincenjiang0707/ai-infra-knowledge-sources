# [PR #1] Tiny index fix

source: https://github.com/gpu-mode/lectures/pull/1
state: closed | updated: 2024-01-28T10:06:44Z
labels: 

## 正文

Fix the indices typo.
If tpb.x = tbp.y and blocks.x = blocks.y wrt the following code from `def matmul_2d(m, n):`
```
    tpb = ns(x=16,y=16)
    blocks = ns(x=math.ceil(w/tpb.x), y=math.ceil(h/tpb.y))
```

then the original way gives the correct result (otherwise not).

## 评论 (1)

### jph00 · 2024-01-28

Many thanks!
