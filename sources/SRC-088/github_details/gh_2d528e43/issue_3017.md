# [Issue #3017] Support for using a remote /tokenize API endpoint as the tokenizer

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3017
state: open | updated: 2026-08-19T10:01:33Z
labels: feature request

## 正文

I am trying to evaluate a fully closed source model that neither model nor tokenizer publicly available. The model is only accessible via API endpoints, including an endpoint for tokenization.

**command:**
lm_eval --model local-completions --tasks mmlu \
--model_args model=custom_model, base_url=http://XX.XX.XX.XX:8000/v1/completions,num_concurrent=1,max_retries=3,tokenized_requests=False 

**result:**
OSError: custom_model is not a local folder and is not a valid model identifier listed on 'https://huggingface.co/models'
If this is a private repository, make sure to pass a token having permission to this repo either by logging in with `huggingface-cli login` or by passing `token=<your_token>`

lm-eval attempts to instantiate a tokenizer using custom_model as if it were a local path or Hugging Face Hub identifier.

Would it be possible to add support in lm-eval to use such a remote /tokenize API endpoint for its internal tokenization needs?



## 评论 (2)

### baberabb · 2025-05-24

Hi! We would welcome a PR.  The main changes would be adding a new conditional block to set `self.tokenizer` with the new `tokenizer_backend`, similar to how the HF one is set. (e.g., storing the tokenizer API endpoint URL from model_args)
https://github.com/EleutherAI/lm-evaluation-harness/blob/7aaceeec2e7b686d95d0e55b43af641dc2484b4a/lm_eval/models/api_models.py#L193-L201

and appropriately call it in`tok_encode` to call the remote tokenizer API with the input string and return the received token IDs.

https://github.com/EleutherAI/lm-evaluation-harness/blob/7aaceeec2e7b686d95d0e55b43af641dc2484b4a/lm_eval/models/api_models.py#L368





### St4r4x · 2026-08-19

Looks like this has already been addressed — PR #3185 (co-authored by @baberabb) added a `tokenizer_backend="remote"` option wired through `tok_encode`/`decode_batch`/`eot_token_id`/etc., backed by a `RemoteTokenizer` class in `lm_eval/utils.py` that POSTs to `{base_url}/tokenize` / `/detokenize`. That's the feature described here, just never linked back to this issue.

One nuance worth flagging: `RemoteTokenizer` validates the server via vLLM's `/tokenizer_info` endpoint, which is narrower than "any arbitrary `/tokenize` endpoint" — so it covers vLLM-compatible servers specifically rather than a fully generic remote tokenizer. Might be worth a decision on whether that gap is worth closing, but the core ask here looks resolved. Could this be closed (or re-scoped if the vLLM-specific constraint is a problem for your use case)?
