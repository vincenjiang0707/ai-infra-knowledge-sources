# [Issue #925] `guidellm benchmark from-file` crashes with `ValidationError` when output includes `console` format

source: https://github.com/vllm-project/guidellm/issues/925
state: closed | updated: 2026-07-15T20:03:19Z
labels: bug, cli

## 正文

### Bug Description

With version v0.7.1, `guidellm benchmark from-file` fails with a Pydantic `ValidationError` whenever the requested (or default) output formats include `console`. Since `--output-formats` defaults to `("console", "json")`, this crashes on **every** invocation of `from-file` unless `console` is explicitly excluded via `--output-formats json` (or another non-console-only list) — it happens before any output is produced.


### Expected Behavior

`guidellm benchmark from-file --output-formats console` should print the console table like `guidellm run` does, without requiring/attaching a `path`.

### Steps to Reproduce

Start the built-in mock server in the background:
```bash
guidellm mock-server --port 8000 --model gpt2 &
sleep 2
```

Run a quick benchmark to generate the JSON report:
```bash
# Probably needed only on macOS to prevent a segfault during worker startup:
export GUIDELLM__MP_CONTEXT_TYPE="spawn"

guidellm run --backend "kind=openai_http,target=http://localhost:8000,model=gpt2" \
  --data "kind=synthetic_text,prompt_tokens=128,output_tokens=128" \
  --profile "kind=concurrent,streams=4" \
  --constraint "kind=max_duration,seconds=10" \
  --output "kind=json,path=./benchmarks.json"
```

Then trigger the crash:
```bash
guidellm benchmark from-file ./benchmarks.json --output-formats console
```


### Operating System

macOS 26.5.2, but also tested on Linux

### Python Version

Python 3.14.6

### GuideLLM Version

guidellm version: 0.7.1

### Installation Method

pip install guidellm

### Installation Details

_No response_

### Error Messages or Stack Traces

```shell
% guidellm benchmark from-file ./benchmarks.json --output-formats console
ℹ Import of old benchmarks complete; loaded 1 benchmark(s)
Traceback (most recent call last):
  File "/Users/mpfister/git/tender-benchmark/.venv/bin/guidellm", line 6, in <module>
    sys.exit(cli())
             ~~~^^
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/click/core.py", line 1514, in __call__
    return self.main(*args, **kwargs)
           ~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/click/core.py", line 1435, in main
    rv = self.invoke(ctx)
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/click/core.py", line 1902, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/click/core.py", line 1902, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/click/core.py", line 1298, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/click/core.py", line 853, in invoke
    return callback(*args, **kwargs)
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/guidellm/cli/benchmark/from_file.py", line 45, in from_file
    asyncio.run(reimport_benchmarks_report(path, output_path, output_formats))
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.6/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/runners.py", line 205, in run
    return runner.run(main)
           ~~~~~~~~~~^^^^^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.6/Frameworks/Python.framework/Versions/3.14/lib/python3.14/asyncio/runners.py", line 128, in run
    return self._loop.run_until_complete(task)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/guidellm/benchmark/entrypoints.py", line 593, in reimport_benchmarks_report
    output_args.append(BenchmarkOutputArgs.model_validate(data))
                       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
  File "/Users/mpfister/git/tender-benchmark/.venv/lib/python3.14/site-packages/pydantic/main.py", line 732, in model_validate
    return cls.__pydantic_validator__.validate_python(
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^
        obj,
        ^^^^
    ...<5 lines>...
        by_name=by_name,
        ^^^^^^^^^^^^^^^^
    )
    ^
pydantic_core._pydantic_core.ValidationError: 1 validation error for BenchmarkOutputArgs
console.path
  Extra inputs are not permitted [type=extra_forbidden, input_value=PosixPath('/Users/mpfiste...ark/benchmarks.console'), input_type=PosixPath]
    For further information visit https://errors.pydantic.dev/2.13/v/extra_forbidden
```

### Additional Context

Claude and Antigravity tell me this:

#### Root cause (from reading `src/guidellm/benchmark/entrypoints.py`)

`reimport_benchmarks_report()` builds output args like this:

```python
for fmt in output_formats:
    data: dict[str, Any] = {"kind": fmt}
    data["path"] = base_path / f"benchmarks.{fmt}"
    output_args.append(BenchmarkOutputArgs.model_validate(data))
```

`path` is attached unconditionally for every format, but the `console` variant of `BenchmarkOutputArgs` forbids extra fields (including `path`) — console output isn't file-based. This makes `from-file` unusable with `console` in the requested formats. By contrast, `guidellm run`'s own `--output kind=console` works fine, since it doesn't synthesize a `path` for non-file kinds.

#### Suggested fix

Only set `data["path"]` for file-based output kinds, e.g.:

```python
for fmt in output_formats:
    data: dict[str, Any] = {"kind": fmt}
    if fmt != "console":
        data["path"] = base_path / f"benchmarks.{fmt}"
    output_args.append(BenchmarkOutputArgs.model_validate(data))
```


## 评论 (2)

### dbutenhof · 2026-07-10

Thanks for pointing this out, and apologies -- we did a massive CLI refactor for `run` in 0.7.0 and apparently missed some inconsistencies in `from-file`.

The best fix may include a general "lift and shift" to upgrade `from-file` to match the new CLI style of `run` -- which we've intended anyway. (The fact that it's currently broken elevates the priority!)

(As an aside ... you say you're on Python 3.14. GuideLLM has not been fully qualified on 3.14 because, last time this was actually investigated, there were some GuideLLM dependencies that were not fully compatible with 3.14. If it works, that's great, but we can't guarantee it at this point.)

### martin-pfister · 2026-07-10

Thanks for your prompt reply – and thanks for the valuable work on `guidellm` in general, including the recent CLI refactor!

Re Python 3.14: That was me being lazy – in production we use the docker container from GHCR, which of course uses Python 3.13.
