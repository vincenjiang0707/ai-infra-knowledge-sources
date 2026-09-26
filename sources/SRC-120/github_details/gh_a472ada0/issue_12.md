# [Issue #12] Code license

source: https://github.com/gpu-mode/lectures/issues/12
state: closed | updated: 2024-03-13T01:36:13Z
labels: 

## 正文

Just stumbled upon this amazing repo. Thanks so much for sharing this!

Someone recommended the CUDA benchmarking code from lecture 1

```python
def time_pytorch_function(func, *input, num_repeats = 1_000):
    # CUDA IS ASYNC so can't use python time module
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)

    # Warmup
    for _ in range(5):
        func(*input)
    torch.cuda.synchronize()

    start.record()
    for _ in range(num_repeats):
        func(*input)
        torch.cuda.synchronize()
    end.record()
    return start.elapsed_time(end) / num_repeats
```

and I was wondering, in general, if the code is open source? Could you perhaps add a license to the repo to clarify? Thanks!

## 评论 (3)

### msaroufim · 2024-03-12

I think as open as possible lemme push a license right now

### msaroufim · 2024-03-12

Just pushed MIT license

### rasbt · 2024-03-13

Awesome, thanks!
