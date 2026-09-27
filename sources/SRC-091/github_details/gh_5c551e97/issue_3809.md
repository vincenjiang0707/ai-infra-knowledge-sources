# [Issue #3809] [Bug] lmcache bench engine fails when vLLM uses --served-model-name: model alias vs HF path mismatch

source: https://github.com/LMCache/LMCache/issues/3809
state: closed | updated: 2026-09-22T02:23:01Z
labels: stale

## 正文

# Describe the bug
When vLLM is started with --served-model-name (to expose a model under an alias different from its HF path), lmcache bench engine cannot run because a single --model value is used for three incompatible purposes, and the LMCache server's /status endpoint does not expose the served-model-name alias.

# To Reproduce
1. Start vLLM with an alias:

vllm serve /llm2/Moonshotai/Kimi-K2.5 \
  --served-model-name kimi-k2.5 \
  --tensor-parallel-size 8 \
  --kv-transfer-config '{"kv_connector":"LMCacheMPConnector", "kv_role":"kv_both"}'
2. Start LMCache server:

lmcache server --l1-size-gb 1024 --eviction-policy LRU
3. Run bench with the alias:

lmcache bench engine \
  --engine-url http://localhost:8000 \
  --workload long-doc-qa \
  --lmcache-url http://localhost:8080 \
  --model kimi-k2.5
Error:

RuntimeError: Model 'kimi-k2.5' not found on LMCache server. Available: /llm2/Moonshotai/Kimi-K2.5
4. Run bench with the HF path (workaround attempt):

lmcache bench engine ... --model /llm2/Moonshotai/Kimi-K2.5
Error:

ErrorInfo(message='The model `/llm2/Moonshotai/Kimi-K2.5` does not exist.', type='NotFoundError', param='model', code=404)
There is no --model value that satisfies both sides.

# Root Cause
The bench tool's --model / config.model value is used for three mutually incompatible purposes:

Purpose	Location	Required value
Match LMCache /status	config.py:_find_model_meta	HF model path (vllm_config.model_config.model)
vLLM OpenAI API requests	request_sender.py	served-model-name alias
Tokenizer loading	workloads/prefix_suffix_tuner.py	HF model path
The LMCache server's cache_context_meta stores model_name from vllm_config.model_config.model (the HF path), while vLLM's /v1/models returns the --served-model-name alias. The MP connector (lmcache_mp_connector.py:532,542) passes vllm_config.model_config.model to the adapter, never served_model_name. So the /status response has no alias field to reconcile the two.

auto_detect_model() fetches from /v1/models and returns the alias — correct for API requests but wrong for LMCache matching and tokenizer loading.

# Expected behavior
lmcache bench engine --model kimi-k2.5 (the alias) should work end-to-end when vLLM is started with --served-model-name kimi-k2.5.

# Suggested fix
Server side: Propagate served_model_name through the registration chain so /status exposes it alongside model_name:
MP connectors pass vllm_config.model_config.served_model_name to adapters
REGISTER_KV_CACHE / CB_REGISTER_KV_CACHE protocols carry served_model_name (append as last payload, str | None)
ContextEntry / NonGPUContextEntry / BlendModule meta store it
report_status() includes "served_model_name" in each meta entry
Same for SGLang and TRT-LLM adapters
Bench side:
_find_model_meta matches against both model_name and served_model_name; falls back to model_name-only when served_model_name is absent (backward compat with old servers)
Tokenizer loading falls back to the HF path from /status when the alias fails to load

# Environment
LMCache: v0.4.7
vLLM connector: LMCacheMPConnector
OS: Linux
Workaround
Remove --served-model-name from the vLLM launch command so the alias equals the HF path, then pass the HF path to --model.

## 评论 (2)

### github-actions[bot] · 2026-08-22

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-22

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
