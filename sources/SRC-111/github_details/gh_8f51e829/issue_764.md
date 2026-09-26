# [Issue #764] SecretStr api_key crashes report serialization (no output when api_key is set)

source: https://github.com/vllm-project/guidellm/issues/764
state: closed | updated: 2026-07-09T15:25:52Z
labels: 

## 正文

## Bug Description

A benchmark run against an endpoint that has an `api_key` set produces **no output files** (`benchmark.json` / `report.csv` / `report.html`).

`OpenAIHTTPBackendArgs.api_key` is a `SecretStr`. `OpenAIHTTPBackend.info` returns `self._args.model_dump()` (python mode), so `api_key` stays a raw `SecretStr` object. That dict becomes `benchmark.config.backend` (via `InfoMixin.extract_from_obj`), and the CSV writer does `json.dumps(benchmark.config.backend)` (`src/guidellm/benchmark/outputs/csv.py`), which raises `TypeError: Object of type SecretStr is not JSON serializable`. The HTML/JSON writers hit the same unmasked dict.

Runs **without** an `api_key` are unaffected (it defaults to `None`), which is why unauthenticated/local runs never see it — but any run against an endpoint that needs a key fails to produce a report.

## Expected Behavior

A run with an `api_key` set completes and writes its reports, with the key **masked** (`**********`) in any persisted output — never crashes, and never leaks the real key.

## Steps to Reproduce

1. Start any OpenAI-compatible server that requires a bearer token (or just pass a dummy key).
2. Run:
   ```bash
   guidellm benchmark run \
     --target http://localhost:8000 \
     --api-key sk-test-123 \
     --profile sweep \
     --data "kind=synthetic_text,prompt_tokens=128,output_tokens=64" \
     --max-requests 10 \
     --outputs "benchmark.json,report.csv"
   ```
3. The run computes but crashes during output with `TypeError: Object of type SecretStr is not JSON serializable`; no report files are written.

## Environment

- **Operating System:** macOS 15.6
- **Python Version:** 3.12.12
- **GuideLLM Version:** `main` @ `96f8355c`
- **Installation Method:** editable install from a `main` checkout

## Error Messages or Stack Traces (representative)

```
TypeError: Object of type SecretStr is not JSON serializable
  File ".../guidellm/benchmark/outputs/csv.py", line 291, in ...
    json.dumps(benchmark.config.backend)
```

## Additional Context

Root cause: `OpenAIHTTPBackendArgs.api_key` has no JSON-safe serializer, and `info()` returns a python-mode `model_dump()` that downstream writers `json.dumps`. A `field_serializer` on `OpenAIHTTPBackendArgs` that masks the key in all dump modes fixes it (PR attached). An alternative root fix would be for `info()` to return `model_dump(mode="json")`, but that changes its contract for other consumers, so the field-level serializer is the more surgical option.


## 评论 (2)

### DaAitch · 2026-07-06

While it was fixed for JSON, it still crashes for CSV.

Tested on latest commit https://github.com/vllm-project/guidellm/commit/6500bcd78719122f1647d791d2237da4b32046ae

```toml
[project]
dependencies = [
    "guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git@6500bcd78719122f1647d791d2237da4b32046ae",
]
```

### dbutenhof · 2026-07-07

> While it was fixed for JSON, it still crashes for CSV.

Thanks. CSV serialization goes through a completely different path and skipped the fix.
