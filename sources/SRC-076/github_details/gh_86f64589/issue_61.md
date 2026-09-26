# [Issue #61] --max-iters CLI argument ignored in dispatch step

source: https://github.com/meta-pytorch/KernelAgent/issues/61
state: closed | updated: 2026-02-05T01:34:11Z
labels: bug, good first issue

## 正文

### 🐛 Describe the bug

**Summary:**
`--max-iters` is not passed to `dispatch_kernel_agent.run()`, causing `TritonKernelAgent` to use hardcoded `max_rounds=10`.


**Root Cause:**
1. `dispatch_kernel_agent.run()` lacks `max_iters` parameter
2. `pipeline.py` doesn't pass `max_iters` to dispatch call

**Fix:**

`dispatch_kernel_agent.py`:
```python
def run(
    subgraphs_path: Path,
    out_dir: Path,
    agent_model: str | None = None,
    jobs: int = 1,
    target_platform: str = "cuda",
    max_iters: int = 10,  # ← Add
) -> Path:
```

`pipeline.py` - add to `dispatch_kernel_agent.run()` call:
```python
dispatch_kernel_agent.run(
    ...
    max_iters=max_iters,  # ← Add
)
```

### Platform and Version

Last main branch, any Linux 

## 评论 (1)

### Jack-Khuu · 2025-12-15

Nice catch
