# [Issue #1589] `get_tokenizer` should fall back to `PreTrainedTokenizerFast` when `AutoTokenizer.from_pretrained` cannot resolve `model_type` (mirroring SGLang server fallback) / `get_tokenizer` 在 `AutoTokenizer.from_pretrained` 无法解析 `model_type` 时应回退到 `PreTrainedTokenizerFast`

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1589
state: closed | updated: 2026-09-09T21:11:22Z
labels: 

## 正文

**Describe the bug**

`utils/bench_serving/backend_request_func.py:get_tokenizer` calls `AutoTokenizer.from_pretrained(...)` and crashes for any model whose `config.json` does not register custom config/tokenizer classes via `auto_map`. With `trust_remote_code=True` set, transformers v5 still takes the `PreTrainedConfig` fallback in `tokenization_auto.py:686` when `CONFIG_MAPPING` does not contain the `model_type`, and that fallback then crashes with `AttributeError: 'PreTrainedConfig' object has no attribute 'max_position_embeddings'`.

Concrete failure: `benchmark_serving.py` against `deepseek-ai/DeepSeek-V4-Pro` (`model_type: deepseek_v4`) raises `KeyError: 'deepseek_v4'` from `AutoTokenizer.from_pretrained` — even though the SGLang server itself handles the same model fine by falling back to `PreTrainedTokenizerFast.from_pretrained` directly. The benchmark client has no such fallback.

Server log line that proves the server path works on the same model: `Loading tokenizer for deepseek-ai/DeepSeek-V4-Pro directly as PreTrainedTokenizerFast (bypassing AutoTokenizer)`.

**To Reproduce**

Steps to reproduce the behavior:
1. Start an SGLang server hosting `deepseek-ai/DeepSeek-V4-Pro` with `--trust-remote-code` (any working sglang container that loads this model — e.g. `lmsysorg/sglang:deepseek-v4-blackwell@sha256:df18bfc4aa9ecf59451002b49ba00cae58042de9e2a96378bbd21b404dd62c7b`) on a B200 host (8×B200, tp=8).
2. From a clone of `SemiAnalysisAI/InferenceX` (commit `12fb33eafab5daacd76cdebf2cd671c0309f3a74`), run on a separate client host that can reach the server:
   ```
   python utils/bench_serving/benchmark_serving.py \
     --model deepseek-ai/DeepSeek-V4-Pro --backend vllm \
     --base-url http://0.0.0.0:8888 --dataset-name random \
     --random-input-len 1024 --random-output-len 1024 \
     --num-prompts 10 --max-concurrency 1 \
     --trust-remote-code --dsv4
   ```
3. Observe the client crash before the first request — see "Actual behavior" below.

**Expected behavior**

Tokenizer loads (using `PreTrainedTokenizerFast.from_pretrained` as a fallback, the same workaround the SGLang server already implements), and the benchmark runs to completion as it does for any model whose tokenizer `AutoTokenizer` *can* resolve. A successful run prints `Successful requests: 10` and the standard throughput / TTFT / TPOT block.

**Actual behavior**

`benchmark_serving.py` aborts inside `get_tokenizer` before any HTTP request is issued. The exact sequence in transformers v5 is:

1. `AutoTokenizer.from_pretrained(...)` calls `AutoConfig.from_pretrained(...)`.
2. `CONFIG_MAPPING[config_dict["model_type"]]` raises `KeyError: 'deepseek_v4'` at `transformers/models/auto/configuration_auto.py:405`.
3. The handler in `tokenization_auto.py:686` then falls through to `PreTrainedConfig.from_pretrained(...)` (because `trust_remote_code=True` is set but the model's `config.json` has no `auto_map`), which raises `AttributeError: 'PreTrainedConfig' object has no attribute 'max_position_embeddings'` from `modeling_rope_utils.standardize_rope_params`.
4. `benchmark_serving.py:main` exits with a non-zero status. No `Successful requests:` line is ever printed and no metrics are produced.

Redacted traceback tail:

```
Traceback (most recent call last):
  File ".../utils/bench_serving/backend_request_func.py", line ..., in get_tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
  File ".../transformers/models/auto/tokenization_auto.py", line 686, in from_pretrained
    ...
  File ".../transformers/models/auto/configuration_auto.py", line 405, in __getitem__
    raise KeyError(key)
KeyError: 'deepseek_v4'
```

The SGLang server reachable on the same host has already logged `Loading tokenizer for deepseek-ai/DeepSeek-V4-Pro directly as PreTrainedTokenizerFast (bypassing AutoTokenizer)` and is serving requests fine. Only the benchmark client lacks that fallback.

**Screenshots**

N/A — failure is a Python traceback, included verbatim under "Actual behavior" above.

**Desktop (please complete the following information):**

N/A — `benchmark_serving.py` is a server-side Python benchmark tool, not a desktop app. Equivalent runtime environment used to reproduce:
- OS: Linux (container `lmsysorg/sglang:deepseek-v4-blackwell@sha256:df18bfc4aa9ecf59451002b49ba00cae58042de9e2a96378bbd21b404dd62c7b`; also reproducible on `lmsysorg/sglang:dev`)
- Hardware: 8×NVIDIA B200, tp=8
- Python: 3.12
- `transformers`: v5 (the version pinned by the SGLang containers above)
- InferenceX: commit `12fb33eafab5daacd76cdebf2cd671c0309f3a74` (any commit ≥ `b286b28e` reproduces — the `trust_remote_code` forward in `get_tokenizer` is already in place; this issue is about the lack of fallback after that call fails)

**Smartphone (please complete the following information):**

N/A — server-side benchmark tool.

**Additional context**

Suggested patch — wrap the existing `AutoTokenizer.from_pretrained` call in `get_tokenizer` to fall back to `PreTrainedTokenizerFast.from_pretrained` on `KeyError` / `ValueError` / `AttributeError` (the exact exceptions transformers raises when `CONFIG_MAPPING` lookup + `PreTrainedConfig` fallback both fail). This mirrors the bypass SGLang's server already implements:

```python
try:
    tokenizer = AutoTokenizer.from_pretrained(
        pretrained_model_name_or_path,
        trust_remote_code=trust_remote_code,
        **kwargs,
    )
except (KeyError, ValueError, AttributeError):
    from transformers import PreTrainedTokenizerFast
    tokenizer = PreTrainedTokenizerFast.from_pretrained(
        pretrained_model_name_or_path,
        trust_remote_code=trust_remote_code,
    )
```

Validation: this exact patch was runtime-applied to a fresh `lmsysorg/sglang:deepseek-v4-blackwell` container and the previously-failing benchmark commands above completed normally (`Successful requests: 10`, throughput numbers reported). Negative control: with the recipe flags `--trust-remote-code --dsv4` but *without* the patch, the benchmark client crashes identically with the same `KeyError: 'deepseek_v4'`. Searched the InferenceX repo for an existing tracker (`get_tokenizer`, `AutoTokenizer`, `PreTrainedTokenizerFast`, `deepseek_v4`, `backend_request_func`, `trust_remote_code tokenizer`) and found none. Adjacent context: PRs #1450 and #1455 ran into the same `KeyError: 'deepseek_v4'` symptom; both were attributed to the generic image's `transformers` not registering `deepseek_v4`, but the underlying benchmark client never gets a chance to fall back to `PreTrainedTokenizerFast` even when `trust_remote_code=True` is honored. This issue is requesting that fallback in `get_tokenizer` so the benchmark client behaves like the SGLang server.

This issue has been co-authored by Claude Opus 4.7

## 中文说明
`get_tokenizer` 在 `AutoTokenizer.from_pretrained` 无法解析模型类型时（如 DeepSeek-V4-Pro 的 `model_type: deepseek_v4` 未在 transformers v5 的 `CONFIG_MAPPING` 中注册）会直接崩溃，而 SGLang 服务端已有回退到 `PreTrainedTokenizerFast.from_pretrained` 的逻辑。建议在 `get_tokenizer` 中添加相同的回退机制：捕获 `KeyError`/`ValueError`/`AttributeError` 后改用 `PreTrainedTokenizerFast`，使基准测试客户端能正常加载 tokenizer 并完成测试。


## 评论 (1)

### janbernloehr · 2026-09-09

no longer reproducible after Transformers 5.8.1.
