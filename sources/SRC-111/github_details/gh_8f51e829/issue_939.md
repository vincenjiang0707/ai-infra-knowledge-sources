# [Issue #939] 'guidellm benchmark from-file' crashes on console output in pip release 0.7.1

source: https://github.com/vllm-project/guidellm/issues/939
state: closed | updated: 2026-07-23T20:06:32Z
labels: duplicate, bug, escape, cli

## 正文

## Description

`guidellm benchmark from-file ./benchmarks.json` crashes with a pydantic validation error on the pip release (0.7.1).

### Reproduction

```bash
pip install guidellm  # installs 0.7.1
guidellm run --backend kind=openai_http,target=http://127.0.0.1:8000 --profile kind=sweep --constraint kind=max_duration,seconds=30 --data kind=synthetic_text,prompt_tokens=256,output_tokens=128
guidellm benchmark from-file ./benchmarks.json
```

### Error

```
pydantic_core._pydantic_core.ValidationError: 1 validation error for BenchmarkOutputArgs
console.path
  Extra inputs are not permitted [type=extra_forbidden, input_value=PosixPath('/home/user/benchmarks.console'), input_type=PosixPath]
```

### Root cause

In `benchmark/entrypoints.py`, `reimport_benchmarks_report()` unconditionally sets `path` for every output format:

```python
for fmt in output_formats:
    data: dict[str, Any] = {"kind": fmt}
    data["path"] = base_path / f"benchmarks.{fmt}"  # <-- console doesn't accept path
    output_args.append(BenchmarkOutputArgs.model_validate(data))
```

The `console` output kind's schema doesn't accept a `path` field, so pydantic raises `Extra inputs are not permitted`.

### Fix

This is already resolved on `main` by #927 ("Modernize benchmark from-file"), which replaced `--output-path` / `--output-formats` with the registry-based `--output` option. But users on the current pip release (0.7.1) hit this crash.

A minimal fix for 0.7.1 would be to skip setting `path` for console:

```python
for fmt in output_formats:
    data: dict[str, Any] = {"kind": fmt}
    if fmt != "console":
        data["path"] = base_path / f"benchmarks.{fmt}"
    output_args.append(BenchmarkOutputArgs.model_validate(data))
```

### Suggested action

Cut a new pip release that includes #927, or backport the fix above to a 0.7.2 patch release.

### Environment

- guidellm 0.7.1 (pip)
- Python 3.12
- Fedora 44

## 评论 (1)

### dbutenhof · 2026-07-23

We just released v0.7.2, which fixes this issue and others.

Check the migration guide -- `guidellm benchmark from-file` (which was always an awkward name) has been renamed to `guidellm export`.
