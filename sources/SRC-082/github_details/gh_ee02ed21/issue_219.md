# [Issue #219]  "Expected all tensors to be on the same device" when running "Perform AWQ search"  on Llama3

source: https://github.com/mit-han-lab/llm-awq/issues/219
state: open | updated: 2025-03-05T02:57:20Z
labels: 

## 正文

When running step 1: "Perform AWQ search and save search results" on Meta-Llama-3.1-8B-Instruct according to the Usage section in Readme, I got the following error:

```
Quantization config: {'zero_point': True, 'q_group_size': 128}
* Building model /home/cju/datasets/hf/meta-llama/Meta-Llama-3.1-8B-Instruct
Loading checkpoint shards: 100%|██████████| 7/7 [09:20<00:00, 80.02s/it]
Repo card metadata block was not found. Setting CardData to empty.
 * Split into 59 blocks
Traceback (most recent call last):
  File "/home/cju/huggingface/llm-awq/awq/entry.py", line 352, in <module>
    main()
  File "/home/cju/huggingface/llm-awq/awq/entry.py", line 292, in main
    model, enc = build_model_and_enc(args.model_path)
  File "/home/cju/huggingface/llm-awq/awq/entry.py", line 211, in build_model_and_enc
    awq_results = run_awq(
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/cju/huggingface/llm-awq/awq/quantize/pre_quant.py", line 133, in run_awq
    model(samples_on_cuda)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 1189, in forward
    outputs = self.model(
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 977, in forward
    position_embeddings = self.rotary_emb(hidden_states, position_ids)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1562, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
  File "/home/cju/venv/python310-hf/lib/python3.10/site-packages/transformers/models/llama/modeling_llama.py", line 209, in forward
    freqs = (inv_freq_expanded.float() @ position_ids_expanded.float()).transpose(1, 2)
RuntimeError: Expected all tensors to be on the same device, but found at least two devices, cpu and cuda:0! (when checking argument for argument mat2 in method wrapper_CUDA_bmm)

Process finished with exit code 1
```

The fix is to move the rotary_emb to GPU as in the following in pre_quant.py:
```
def move_embed(model, device):
    if isinstance(model, LlamaForCausalLM):
        model.model.embed_tokens = model.model.embed_tokens.to(device)
        # add the following line to move rotary_emb to GPU as well
        model.model.rotary_emb = model.model.rotary_emb.to(device)
```

I am happy to make a pull request if it is needed.

## 评论 (1)

### mattam301 · 2025-03-05

Thanks a lot!
