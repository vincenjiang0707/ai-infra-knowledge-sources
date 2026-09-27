# [Issue #137] Loading Quantized Model on 2 GPU's

source: https://github.com/dropbox/hqq/issues/137
state: closed | updated: 2025-04-09T10:58:32Z
labels: 

## 正文

Hi,

Is is possible to load a quantized model onto 2 GPU's? 

I tried loading a quantized model like this:

`model = AutoHQQHFModel.from_quantized(save_dir, compute_dtype=torch.bfloat16, device=[torch.device('cuda:0'), torch.device('cuda:1')])
`

But the model only loads onto the 1st GPU.

Thanks!

## 评论 (7)

### mobicham · 2024-12-26

I think multi-gpu via the hqq lib is only supported when you quantize on-the-fly, meaning via `AutoHQQHFMode.quantize_model` and use ```device=['cuda:0','cuda:1']``` https://github.com/mobiusml/hqq/blob/master/hqq/models/base.py#L266

Otherwise, you can simply do it directly via transformers. 

hqq's lib multi-gpu implementation is a bit faster than HF though because they use accelerate and I don't use any of that by minimizing the number of transfers across layers. 

The other option is to use gpt-fast and hqq via torchao, but they don't support all models I think only Llama-like models. 

### mxtsai · 2024-12-26

Thanks for the response. Do you happen to know any examples (or similar examples) that shows how to use gpt-fast and hqq via torchao? 

### mobicham · 2024-12-26

I think it's this for gpt-fast:
https://github.com/mobicham/ao/tree/main/torchao/_models/llama
And to quantize with hqq: 
https://github.com/pytorch/ao/blob/main/torchao/quantization/README.md#a16w4-weightonly-quantization



### mobicham · 2024-12-26

Or you could simply use VLLM with HQQ, probably the best option for serving. You can use this script:
https://gist.github.com/mobicham/6efb1f7af3bf5b24fdc88f1edbcacd9a

### mxtsai · 2024-12-27

Thank you for the links. From what I understand, it seems like `gpt-fast` and `torchao` only support single device quantization + inference? It seems like they provide methods to compile the model, but I'm not sure if these can be applicable for multi-gpu model inference (i.e., tensor parallel).

If I were to use VLLM with HQQ, is there support for HQQ models like in the OpenAI compatible server API? Or is the current support only available with running from Huggingface Transfomers -> VLLM (as in your script). 

Btw, I see that `hqq` is one of the `--quantization` parameters in the VLLM OpenAI compatible server ([link](https://docs.vllm.ai/en/latest/serving/openai_compatible_server.html#cli-reference)), but I can't seem to find any script that can convert an existing HF model onto the format that can be used for serving in VLLM. The only model that I found that works is [this](https://huggingface.co/nm-testing/Llama-3.2-1B-Instruct-HQQ) Llama 8B model, but no scripts are provided to show how this model was generated.

### mobicham · 2024-12-27

The script I shared with you takes an unquantized huggingface model -> quantizes it with hqq -> saves it. Then you can load that model in VLLM directly. That should work for any huggingface model

### mobicham · 2025-04-09

Hey, I guess this is old since you can use hqq in both transformers and vllm.
