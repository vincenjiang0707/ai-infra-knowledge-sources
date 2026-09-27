# [Issue #4204] [Bug] server CLI crashes on startup via bigtable adapter protobuf TypeError (load_all_adapters only catches ImportError)

source: https://github.com/LMCache/LMCache/issues/4204
state: open | updated: 2026-09-21T01:52:33Z
labels: stale

## 正文

## Description

`lmcache server` (and even `lmcache server --help`) crashes on startup when the
installed `google-cloud-bigtable` is incompatible with the environment's
`protobuf` version. The crash happens during L2 adapter enumeration for the CLI
help string, before any server logic runs.

Root cause: `load_all_adapters()` only catches `ImportError`, but the bigtable
adapter's protobuf conflict raises `TypeError`, which escapes the handler and
crashes the CLI. This affects users who never use the Bigtable adapter, because
adapter enumeration is mandatory at CLI construction time.

## Environment

- lmcache: 0.5.2
- vLLM: 0.24.0
- Python: 3.12
- GPU: B200
- Model: GLM-5.2-NVFP4
- `protobuf`: >= 4.x (pulled in by vLLM/torch)
- `google-cloud-bigtable`: version requiring `protobuf<4.0` (e.g. 1.7.3)

## Reproduction

1. Install lmcache 0.5.2 in an env where `google-cloud-bigtable` resolves to a
   version requiring `protobuf<4.0` while vLLM pulls `protobuf>=4`.
2. Run `lmcache server --help` (or any server start).

## Error

```
Traceback (most recent call last):
  File ".../lmcache/cli/main.py", line 30, in main
    cmd.register(subparsers)
  File ".../lmcache/cli/commands/server.py", line 58, in add_arguments
    add_storage_manager_args(parser)
  File ".../lmcache/v1/distributed/config.py", line 524, in add_storage_manager_args
    add_l2_adapters_args(parser)
  File ".../lmcache/v1/distributed/l2_adapters/config.py", line 434, in add_l2_adapters_args
    + ", ".join(sorted(get_registered_l2_adapter_types()))
  File ".../lmcache/v1/distributed/l2_adapters/config.py", line 126, in get_registered_l2_adapter_types
    return get_all_registered_names()
  File ".../lmcache/v1/distributed/l2_adapters/factory.py", line 161, in get_all_registered_names
    load_all_adapters()
  File ".../lmcache/v1/distributed/l2_adapters/factory.py", line 147, in load_all_adapters
    importlib.import_module(mod_path)
  ...
  File ".../lmcache/v1/distributed/l2_adapters/bigtable_l2_adapter.py", line 19, in <module>
    from google.cloud.bigtable.data import (
  ...
  File ".../google/cloud/bigtable_v2/proto/data_pb2.py", line 33, in <module>
    _descriptor.FieldDescriptor(
  File ".../google/protobuf/descriptor.py", line 675, in __new__
    _message.Message._CheckCalledFromGeneratedFile()
TypeError: Descriptors cannot be created directly.
If this call came from a _pb2.py file, your generated code is out of date and must be regenerated with protoc >= 3.19.0.
```

## Root cause

1. `add_l2_adapters_args` builds the `--l2-adapter` help string by calling
   `get_registered_l2_adapter_types()` (config.py:434) → `get_all_registered_names()`
   (factory.py:155) → `load_all_adapters()` (factory.py:161).
2. `load_all_adapters()` force-imports **all** pending adapter modules to list
   type names, and only catches `ImportError` (factory.py:148).
3. The bigtable adapter imports `google.cloud.bigtable` at module top
   (bigtable_l2_adapter.py:19); with an incompatible protobuf this raises
   `TypeError: Descriptors cannot be created directly` — **not** an `ImportError` —
   so it escapes the `except` and crashes the CLI.
4. #2905 introduced lazy import (`ensure_adapter_loaded`) which protects the
   runtime path, but the CLI-help path still goes through `load_all_adapters()`
   and was not protected. PR #2905's own risk note already flagged
   "CLI adapter listing" as exposed to import-time side effects / missing deps.

## Suggested fix

- **Minimal**: broaden the exception in `load_all_adapters()` (and
  `ensure_adapter_loaded()`) from `except ImportError` to `except Exception`,
  logging at debug.
- **Better**: `get_all_registered_names()` could list type names from the
  registry without force-importing all modules (true lazy listing), reserving
  imports for actual use.

## Workaround

- `export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python`, or
- `pip install -U google-cloud-bigtable` to a version compatible with protobuf>=4.

## Notes

- `google-cloud-bigtable` is listed in `requirements/common.txt` without a
  version bound, so pip may resolve to an old release incompatible with
  protobuf 4.x/5.x.
- I could not find an existing issue for this; searched the tracker for
  "Descriptors cannot be created", "bigtable", "protobuf", "load_all_adapters".
- Bigtable adapter was introduced via #3885.

## 评论 (1)

### github-actions[bot] · 2026-09-21

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
