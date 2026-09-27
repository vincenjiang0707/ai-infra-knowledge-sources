# [Issue #4547] [Feature] Implement /v1/embeddings endpoint

source: https://github.com/InternLM/lmdeploy/issues/4547
state: closed | updated: 2026-05-13T04:20:59Z
labels: 

## 正文

## Motivation

The `/v1/embeddings` endpoint is a standard OpenAI API supported by vLLM, SGLang, and TGI. Many downstream tools (LangChain, LlamaIndex, RAG pipelines) depend on it to generate text embeddings.

Currently lmdeploy's `/v1/embeddings` is a stub that returns `Unsupported by turbomind`. The infrastructure to pass `last_hidden_state` through the pipeline already exists at the high level (`Response`, `EngineOutput`, `GenOut` all have the field), but the PyTorch engine's internal pipeline never populates it.

## Related resources

- OpenAI Embeddings API: https://platform.openai.com/docs/api-reference/embeddings
- vLLM implementation for reference: https://github.com/vllm-project/vllm
- lmdeploy already has: `EmbeddingsRequest`/`EmbeddingsResponse` protocol classes, `output_last_hidden_state` in `GenerationConfig`, TurboMind C++ engine support for `output_last_hidden_state`
- lmdeploy has related endpoints: `/v1/encode` (tokenization), `/pooling` (pooling API)

## Additional context

I have a working implementation on branch `feat/embeddings-endpoint` that:

1. Replaces the stub with a real endpoint that calls the engine with `max_new_tokens=0` + `output_last_hidden_state='all'`, then mean-pools the hidden states
2. Threads `last_hidden_states` through the PyTorch engine pipeline (`BatchedOutputs` → `InferOutput` → `EngineOutput`), since previously only TurboMind supported hidden state extraction
3. Supports both `float` and `base64` encoding formats per OpenAI spec

**Changes**: ~160 lines across 9 files (mostly plumbing existing types).

Before opening a PR, I'd like to confirm:
- Is this feature direction aligned with the project? (vs. focusing on the existing `/pooling` endpoint)
- Any concerns about the PyTorch engine hidden states pipeline changes?

Happy to open a PR if the direction is approved.

## 评论 (2)

### lvhan028 · 2026-04-23

Hi, @ZhijunLStudio 
Thank you for your interest in contributing this feature.

We welcome your PR. This feature aligns well with LMDeploy's roadmap. As for the impact on hidden_state, we will evaluate it further after your PR is submitted.



### lvhan028 · 2026-05-12

Hi, @ZhijunLStudio 
I want to be upfront about something: I realize I gave you the wrong guidance when I said this feature aligns with the roadmap. After further investigation, I need to correct myself and I apologize for the confusion.

Here's the core issue: The /v1/embeddings endpoint in the OpenAI API specification is designed specifically for embedding models, which are purpose‑built to generate vector representations of text for retrieval, clustering, and semantic search. LMDeploy currently focuses on serving generative (decoder‑only) LLMs, not embedding models.

To illustrate why this matters,  I ran a quick experiment. I started vLLM serving a generative model (Qwen3-30B-A3B) and tried to call its v1/embeddings endpoint. The request failed with a 404 Not Found:
```
    resp = client.embeddings.create(**create_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/openai/resources/embeddings.py", line 132, in create
    return self._post(
           ^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/openai/_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/py3/lib/python3.12/site-packages/openai/_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.NotFoundError: Error code: 404 - {'detail': 'Not Found'}
```
However, when I switched the model to a proper embedding model [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B), the same endpoint worked correctly.

So while your implementation in PR #4550  is technically clever — threading hidden states through the pipeline, applying mean pooling, and producing something that looks like an embedding — it ultimately gives users a false impression. A generative model's hidden states simply aren't equivalent to a real embedding model's output.

Given this, I believe we should not merge #4550  as-is. Supporting `/v1/embeddings` properly will require first adding native support for embedding model inference in LMDeploy. Only then can we implement the endpoint with correct semantics.

Again, I appreciate your effort and I'm sorry for the earlier misdirection. I hope this explanation makes sense. Please let me know if you'd like to discuss further.
