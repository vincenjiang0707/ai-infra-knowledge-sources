# [Issue #108] RuntimeError: Expected in.dtype() == at::kInt to be true, but got false.

source: https://github.com/dropbox/hqq/issues/108
state: closed | updated: 2024-08-27T13:27:08Z
labels: 

## 正文

I want to reproduce Whisper + HQQ example but getting error:

```
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
[<ipython-input-7-c2efaa80e4eb>](https://localhost:8080/#) in <cell line: 1>()
----> 1 prepare_for_inference(model.model.decoder, backend="torchao_int4")

7 frames
[/usr/local/lib/python3.10/dist-packages/torch/_ops.py](https://localhost:8080/#) in __call__(self_, *args, **kwargs)
    852         # We save the function ptr as the `op` attribute on
    853         # OpOverloadPacket to access it here.
--> 854         return self_._op(*args, **(kwargs or {}))
    855 
    856     # TODO: use this to make a __dir__

RuntimeError: Expected in.dtype() == at::kInt to be true, but got false.  (Could this error message be improved?  If so, please report an enhancement request to PyTorch.)
```

My colab shows the issue: 

https://colab.research.google.com/drive/1V4EJVKBKbayMNQPptpnls6c3ayWm5EO1?usp=sharing

---

Can you please suggest what is wrong in my code?


## 评论 (9)

### mobicham · 2024-08-26

Can you try with the torch nightly and hqq from master not pip `pip install git+https://github.com/mobiusml/hqq.git` 
Also make sure you use a supported gpu for the fast backends, at least Ampere

### egorsmkv · 2024-08-26

Tried with nightly:

https://colab.research.google.com/drive/10OigWCwUMSKE9o9JKwrywBCY-qeRrg5Q?usp=sharing (you can see all info with logs here)

Now, it successfully runs that line of code:

```
prepare_for_inference(model.model.decoder, backend="torchao_int4")
```

but fails during transcribing:

```
RuntimeError: Error: accessing tensor output of CUDAGraphs that has been overwritten by a subsequent run. Stack trace: File "/usr/local/lib/python3.10/dist-packages/transformers/models/whisper/modeling_whisper.py", line 1377, in forward
    layer_outputs = decoder_layer(
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/whisper/modeling_whisper.py", line 769, in forward
    hidden_states, self_attn_weights, present_key_value = self.self_attn(
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/whisper/modeling_whisper.py", line 578, in forward
    key_states = self._shape(self.k_proj(current_states), -1, bsz)
  File "/usr/local/lib/python3.10/dist-packages/transformers/models/whisper/modeling_whisper.py", line 321, in _shape
    return tensor.view(bsz, seq_len, self.num_heads, self.head_dim).transpose(1, 2).contiguous(). To prevent overwriting, clone the tensor outside of torch.compile() or call torch.compiler.cudagraph_mark_step_begin() before each model invocation.
```


### mobicham · 2024-08-26

Does it work without compiling ? 
@Jiltseb have you seen this error before?

### Jiltseb · 2024-08-26

The Huggingface `pipeline` is yet to support the torch.compile()+static cache for E-D models. This means, you won't be able to use pipeline even in fp16 with higher speed.

You can instead use `model.generate(**inputs`) for long-form transcription(see [doc](https://huggingface.co/docs/transformers/main/en/llm_optims?static-kv=advanced+usage%3A+end-to-end+generate+compilation#static-kv-cache-and-torchcompile)). HQQ works fine on top of this set-up.

### egorsmkv · 2024-08-26

> Does it work without compiling ? @Jiltseb have you seen this error before?

Yes, it works correctly

### egorsmkv · 2024-08-26

> The Huggingface `pipeline` is yet to support the torch.compile()+static cache for E-D models. This means, you won't be able to use pipeline even in fp16 with higher speed.
> 
> You can instead use `model.generate(**inputs`) for long-form transcription(see [doc](https://huggingface.co/docs/transformers/main/en/llm_optims?static-kv=advanced+usage%3A+end-to-end+generate+compilation#static-kv-cache-and-torchcompile)). HQQ works fine on top of this set-up.

Thank you!

### egorsmkv · 2024-08-26

One last question:

Can I just `torch.compile` like the following:

```
model.forward = torch.compile(model.forward, mode="reduce-overhead", fullgraph=True)
```

or I need to do it as it in HQQ's examples? 

Like this:

```
model.model.encoder.forward = torch.compile(model.model.encoder.forward, mode="reduce-overhead", fullgraph=True)
model.model.decoder.forward = torch.compile(model.model.decoder.forward, mode="reduce-overhead", fullgraph=True)
```


### mobicham · 2024-08-26

You don't need to compile the encoder, only the decoder's forward pass needs to be compiled
```Python
model.model.decoder.forward = torch.compile(model.model.decoder.forward, mode="reduce-overhead", fullgraph=True)
```

### egorsmkv · 2024-08-26

Thank you, @mobicham 
