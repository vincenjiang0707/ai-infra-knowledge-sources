# [Issue #2824] [BUG] Unsupported backend: `gptq_marlin` for `gptq` with format `gptq_v2`

source: https://github.com/ModelCloud/GPTQModel/issues/2824
state: closed | updated: 2026-04-28T01:17:28Z
labels: bug

## 正文

**Describe the bug**

After quantizing a model using gptq, cannot use latest (from v5.0.0 to v6.0.0) GPTQModel to select marlin backend to run inference. 
 quantization scripts:
```
    gptq_config = GPTQConfig(bits=bit, format = "gptq", dataset=dataset, tokenizer=tokenizer)
    quantized_model = AutoModelForCausalLM.from_pretrained(model_path,
                            device_map="auto",
                            trust_remote_code=True,
                            quantization_config=gptq_config)

    quantized_model.to("cpu")
    quantized_model.generation_config.do_sample = True
    quantized_model.save_pretrained(quant_path)
    tokenizer.save_pretrained(quant_path)
```
inferece script:
```
    model = GPTQModel.load(
        model_path,
        backend=BACKEND.MARLIN,
    )
```
**GPU Info**

Show output of:

```
Sat Apr 25 00:21:28 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 590.48.01              Driver Version: 590.48.01      CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A6000               Off |   00000000:41:00.0 Off |                  Off |
| 30%   52C    P5             49W /  300W |       1MiB /  49140MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+

```
**Software Info**

NAME="Red Hat Enterprise Linux"VERSION="8.10 (Ootpa)"
python 3.10

Show output of:
```
Name: GPTQModel
Version: 6.0.3
Summary: Production ready LLM model compression/quantization toolkit with hw accelerated inference support for both cpu/gpu via HF, vLLM, and SGLang.
Home-page: https://github.com/ModelCloud/GPTQModel
Author: 
Author-email: ModelCloud <qubitium@modelcloud.ai>
License-Expression: Apache-2.0
Location: [WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages
Requires: accelerate, datasets, defuser, device-smi, dill, kernels, logbar, maturin, numpy, packaging, pillow, protobuf, pyarrow, pypcre, safetensors, setuptools, threadpoolctl, tokenicer, torch, torchao, transformers
Required-by: 
---
Name: torch
Version: 2.11.0
Summary: Tensors and Dynamic neural networks in Python with strong GPU acceleration
Home-page: https://pytorch.org
Author: 
Author-email: PyTorch Team <packages@pytorch.org>
License: BSD-3-Clause
Location: [WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages
Requires: cuda-bindings, cuda-toolkit, filelock, fsspec, jinja2, networkx, nvidia-cudnn-cu13, nvidia-cusparselt-cu13, nvidia-nccl-cu13, nvidia-nvshmem-cu13, setuptools, sympy, triton, typing-extensions
Required-by: accelerate, GPTQModel, optimum, peft, torchaudio
---
Name: transformers
Version: 5.4.0
Summary: Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
Home-page: https://github.com/huggingface/transformers
Author: The Hugging Face team (past and future) with the help of all our contributors (https://github.com/huggingface/transformers/graphs/contributors)
Author-email: transformers@huggingface.co
License: Apache 2.0 License
Location: [WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages
Requires: huggingface-hub, numpy, packaging, pyyaml, regex, safetensors, tokenizers, tqdm, typer
Required-by: Defuser, GPTQModel, optimum, peft
---
Name: accelerate
Version: 1.13.0
Summary: Accelerate
Home-page: https://github.com/huggingface/accelerate
Author: The Hugging Face team
Author-email: transformers@huggingface.co
License: Apache
Location: [WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages
Requires: huggingface_hub, numpy, packaging, psutil, pyyaml, safetensors, torch
Required-by: GPTQModel, peft
---
Name: triton
Version: 3.6.0
Summary: A language and compiler for custom Deep Learning operations
Home-page: https://github.com/triton-lang/triton/
Author: Philippe Tillet
Author-email: phil@openai.com
License: 
Location: [WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages
Requires: 
Required-by: torch
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**
{
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 128000,
  "dtype": "bfloat16",
  "eos_token_id": 128009,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 14336,
  "max_position_embeddings": 8192,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "quantization_config": {
    "act_group_aware": true,
    "backend": "auto",
    "batch_size": 1,
    "bits": 4,
    "block_name_to_quantize": null,
    "cache_block_outputs": true,
    "checkpoint_format": "gptq_v2",
    "damp_percent": 0.1,
    "dataset": [ ... ],
    "desc_act": false,
    "format": "gptq_v2",
    "group_size": 128,
    "max_input_length": null,
    "meta": {
      "quantizer": [
        "optimum:2.1.0",
        "gptqmodel:6.0.3"
      ]
    },
    "model_seqlen": null,
    "module_name_preceding_first_block": null,
    "modules_in_block_to_quantize": null,
    "pad_token_id": null,
    "quant_method": "gptq",
    "sym": true,
    "tokenizer": null,
    "true_sequential": true
  },
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "rope_theta": 500000.0,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.4.0",
  "use_cache": true,
  "vocab_size": 128256
}
**To Reproduce**

How to reproduce this bug if possible.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

```
Loading Tokenizer...
Loading 4-bit Model...
from_quantized: adapter: None
INFO  Loader: Auto dtype (native bfloat16): `torch.bfloat16`
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: backend.                                                                        
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: batch_size.                                                                     
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: block_name_to_quantize.                                                         
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: cache_block_outputs.                                                            
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: dataset.                                                                        
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: max_input_length.                                                               
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: model_seqlen.                                                                   
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: module_name_preceding_first_block.                                              
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: modules_in_block_to_quantize.                                                   
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: pad_token_id.                                                                   
INFO  QuantizeConfig: Ignoring unknown parameter in the quantization configuration: tokenizer.                                                                      
INFO  QuantizeConfig: offload_to_disk_path auto set to `./gptqmodel_offload/dwjcftrv-nzmfpnyz/`                                                                     
INFO  Estimated Quantization BPW (bits per weight): 4.2875 bpw, based on [bits: 4, group_size: 128]                                                                 
Traceback (most recent call last):
  File "[WORKSPACE]/quant/check_quant_model.py", line 44, in <module>
    test_quantized_initialization(TARGET_MODEL, TARGET_BITS)
  File "[WORKSPACE]/flashquant/check_quant_model.py", line 21, in test_quantized_initialization                                                                     
    model = GPTQModel.load(
  File "[WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 435, in load                                             
    m = cls.from_quantized(
  File "[WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages/gptqmodel/models/auto.py", line 549, in from_quantized                                   
    return model_definition.from_quantized(
  File "[WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages/gptqmodel/models/loader.py", line 788, in from_quantized                                 
    preload_qlinear_kernel = make_quant(
  File "[WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages/gptqmodel/utils/model.py", line 325, in make_quant                                       
    quant_linear_candidates = select_quant_linear(
  File "[WORKSPACE]/miniconda3/envs/flexquant/lib/python3.10/site-packages/gptqmodel/utils/importer.py", line 517, in select_quant_linear                           
    qlinear = get_kernel_for_backend(backend, quant_method, format)
  File "[WORKSPACE]/miniconda3/envs/quant/lib/python3.10/site-packages/gptqmodel/utils/importer.py", line 92, in get_kernel_for_backend                         
    raise ValueError(f"Unsupported backend: `{backend}` for `{quant_method}` with format `{fmt}`")                                                                  
ValueError: Unsupported backend: `gptq_marlin` for `gptq` with format `gptq_v2`
```

**Additional context**
able to use marlin with optimum==1.26.1, torch==2.11.0, triton==3.6.0, transformers==4.56.2, gptqmodel==4.0.0,
but doesn't show speedup as expected, same inference speed ~35T/s for int4, int8, and fp16 model on transformers



## 评论 (4)

### Qubitium · 2026-04-25

@zhi-dian Show me full config.json of your model. The logs you posted does not help.  We  have no backend named "gptq_marlin".

How did you quantize this model? Which tool did you use?

### ZX-ModelCloud · 2026-04-27

I have reproduced this issue and am currently fixing it.

### zhi-dian · 2026-04-27

I use Transformers to quantize the model. Here is the complete quantization scripts:
```

from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig
from datasets import load_dataset

import argparse


argparser = argparse.ArgumentParser(description="")

#quantized_model/llama3-gptq
argparser.add_argument("--model_path", "--i", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct")
argparser.add_argument("--output_path", "--f", type=str, default="quantized_model/llama3-gptq")
argparser.add_argument("--dataset", "--d", type=str, default=None)
argparser.add_argument("--bits", "--b", nargs='*', type=int, default=[8, 4])

args = argparser.parse_args()


for bit in args.bits:
    model_path = args.model_path
    quant_path = f"{args.output_path}-{bit}"

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    if args.dataset is None:
        dataset = load_dataset("HuggingFaceH4/ultrachat_200k",
                                split="train_sft").shuffle(seed=42).select(range(256))

        def preprocess(example):
            return {"text": ", ".join([x['content'] for x in example["messages"]])}
        dataset = dataset.map(preprocess)
        dataset = [x["text"] for x in dataset]
        gptq_config = GPTQConfig(bits=bit, format = "gptq", dataset=dataset, tokenizer=tokenizer)
    else:
        gptq_config = GPTQConfig(bits=bit, format = "gptq", dataset=args.dataset, tokenizer=tokenizer)

    quantized_model = AutoModelForCausalLM.from_pretrained(model_path,
                            device_map="auto",
                            trust_remote_code=True,
                            quantization_config=gptq_config)

    # Save quantized model
    quantized_model.to("cpu")
    quantized_model.generation_config.do_sample = True
    quantized_model.save_pretrained(quant_path)
    tokenizer.save_pretrained(quant_path)

    print(f'Model is quantized and saved at "{quant_path}"')

```
The complete model config(exclude the datasets:[] in quantization_config):
```
{
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 128000,
  "dtype": "bfloat16",
  "eos_token_id": 128009,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 14336,
  "max_position_embeddings": 8192,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "quantization_config": {
    "act_group_aware": true,
    "backend": "auto",
    "batch_size": 1,
    "bits": 8,
    "block_name_to_quantize": null,
    "cache_block_outputs": true,
    "checkpoint_format": "gptq_v2",
    "damp_percent": 0.1,
    "dataset": [
    ],
    "desc_act": false,
    "format": "gptq_v2",
    "group_size": 128,
    "max_input_length": null,
    "meta": {
      "quantizer": [
        "optimum:2.1.0",
        "gptqmodel:6.0.3"
      ]
    },
    "model_seqlen": null,
    "module_name_preceding_first_block": null,
    "modules_in_block_to_quantize": null,
    "pad_token_id": null,
    "quant_method": "gptq",
    "sym": true,
    "tokenizer": null,
    "true_sequential": true
  },
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "rope_theta": 500000.0,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.4.0",
  "use_cache": true,
  "vocab_size": 128256
}
```
I found that I need gpt format to use marlin backend. Using this scripts can get a model quantized in gpt format and can use marlin to run inference. 
```
from transformers import AutoModelForCausalLM, AutoTokenizer
# from transformers import GPTQConfig
from datasets import load_dataset

import argparse

from gptqmodel import GPTQModel, QuantizeConfig

argparser = argparse.ArgumentParser(description="Evaluate the generated text")

#quantized_model/llama3-gptq
argparser.add_argument("--model_path", "--i", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct")
argparser.add_argument("--output_path", "--f", type=str, default="quantized_model/llama3-gptq")
argparser.add_argument("--dataset", "--d", type=str, default=None)
argparser.add_argument("--bits", "--b", nargs='*', type=int, default=[8, 4])

args = argparser.parse_args()


for bit in args.bits:
    model_path = args.model_path
    quant_path = f"{args.output_path}-{bit}"

    tokenizer = AutoTokenizer.from_pretrained(model_path)

    dataset = load_dataset("HuggingFaceH4/ultrachat_200k",
        split="train_sft").shuffle(seed=42).select(range(256))

    def preprocess(example):
        return {"text": ", ".join([x['content'] for x in example["messages"]])}
    dataset = dataset.map(preprocess)

    quant_config = QuantizeConfig(bits=bit, group_size=128, format="gptq")

    model = GPTQModel.load(model_path, 
                           quant_config,
                           device_map="cuda:0")

    # increase `batch_size` to match GPU/VRAM specs to speed up quantization
    model.quantize(dataset, batch_size=8)

    model.save(quant_path)

    print(f'Model is quantized and saved at "{quant_path}"')
```

Here is a few things I tried:
I tried to import GPTQConfig from gptqmodel, but it failed. So I tried to use GPTQConfig from transformers, and it failed saying GPTQConfig doesn't have dynamic attribute. I found that the GPTQConfig should change to QuantizeConfig. Maybe you can update the README.  

Thank you so much. 

### ZX-ModelCloud · 2026-04-28

> I use Transformers to quantize the model. Here is the complete quantization scripts:
> 
> ```
> 
> from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig
> from datasets import load_dataset
> 
> import argparse
> 
> 
> argparser = argparse.ArgumentParser(description="")
> 
> #quantized_model/llama3-gptq
> argparser.add_argument("--model_path", "--i", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct")
> argparser.add_argument("--output_path", "--f", type=str, default="quantized_model/llama3-gptq")
> argparser.add_argument("--dataset", "--d", type=str, default=None)
> argparser.add_argument("--bits", "--b", nargs='*', type=int, default=[8, 4])
> 
> args = argparser.parse_args()
> 
> 
> for bit in args.bits:
>     model_path = args.model_path
>     quant_path = f"{args.output_path}-{bit}"
> 
>     tokenizer = AutoTokenizer.from_pretrained(model_path)
> 
>     if args.dataset is None:
>         dataset = load_dataset("HuggingFaceH4/ultrachat_200k",
>                                 split="train_sft").shuffle(seed=42).select(range(256))
> 
>         def preprocess(example):
>             return {"text": ", ".join([x['content'] for x in example["messages"]])}
>         dataset = dataset.map(preprocess)
>         dataset = [x["text"] for x in dataset]
>         gptq_config = GPTQConfig(bits=bit, format = "gptq", dataset=dataset, tokenizer=tokenizer)
>     else:
>         gptq_config = GPTQConfig(bits=bit, format = "gptq", dataset=args.dataset, tokenizer=tokenizer)
> 
>     quantized_model = AutoModelForCausalLM.from_pretrained(model_path,
>                             device_map="auto",
>                             trust_remote_code=True,
>                             quantization_config=gptq_config)
> 
>     # Save quantized model
>     quantized_model.to("cpu")
>     quantized_model.generation_config.do_sample = True
>     quantized_model.save_pretrained(quant_path)
>     tokenizer.save_pretrained(quant_path)
> 
>     print(f'Model is quantized and saved at "{quant_path}"')
> ```
> 
> The complete model config(exclude the datasets:[] in quantization_config):
> 
> ```
> {
>   "architectures": [
>     "LlamaForCausalLM"
>   ],
>   "attention_bias": false,
>   "attention_dropout": 0.0,
>   "bos_token_id": 128000,
>   "dtype": "bfloat16",
>   "eos_token_id": 128009,
>   "head_dim": 128,
>   "hidden_act": "silu",
>   "hidden_size": 4096,
>   "initializer_range": 0.02,
>   "intermediate_size": 14336,
>   "max_position_embeddings": 8192,
>   "mlp_bias": false,
>   "model_type": "llama",
>   "num_attention_heads": 32,
>   "num_hidden_layers": 32,
>   "num_key_value_heads": 8,
>   "pad_token_id": null,
>   "pretraining_tp": 1,
>   "quantization_config": {
>     "act_group_aware": true,
>     "backend": "auto",
>     "batch_size": 1,
>     "bits": 8,
>     "block_name_to_quantize": null,
>     "cache_block_outputs": true,
>     "checkpoint_format": "gptq_v2",
>     "damp_percent": 0.1,
>     "dataset": [
>     ],
>     "desc_act": false,
>     "format": "gptq_v2",
>     "group_size": 128,
>     "max_input_length": null,
>     "meta": {
>       "quantizer": [
>         "optimum:2.1.0",
>         "gptqmodel:6.0.3"
>       ]
>     },
>     "model_seqlen": null,
>     "module_name_preceding_first_block": null,
>     "modules_in_block_to_quantize": null,
>     "pad_token_id": null,
>     "quant_method": "gptq",
>     "sym": true,
>     "tokenizer": null,
>     "true_sequential": true
>   },
>   "rms_norm_eps": 1e-05,
>   "rope_parameters": {
>     "rope_theta": 500000.0,
>     "rope_type": "default"
>   },
>   "tie_word_embeddings": false,
>   "transformers_version": "5.4.0",
>   "use_cache": true,
>   "vocab_size": 128256
> }
> ```
> 
> I found that I need gpt format to use marlin backend. Using this scripts can get a model quantized in gpt format and can use marlin to run inference.
> 
> ```
> from transformers import AutoModelForCausalLM, AutoTokenizer
> # from transformers import GPTQConfig
> from datasets import load_dataset
> 
> import argparse
> 
> from gptqmodel import GPTQModel, QuantizeConfig
> 
> argparser = argparse.ArgumentParser(description="Evaluate the generated text")
> 
> #quantized_model/llama3-gptq
> argparser.add_argument("--model_path", "--i", type=str, default="meta-llama/Meta-Llama-3-8B-Instruct")
> argparser.add_argument("--output_path", "--f", type=str, default="quantized_model/llama3-gptq")
> argparser.add_argument("--dataset", "--d", type=str, default=None)
> argparser.add_argument("--bits", "--b", nargs='*', type=int, default=[8, 4])
> 
> args = argparser.parse_args()
> 
> 
> for bit in args.bits:
>     model_path = args.model_path
>     quant_path = f"{args.output_path}-{bit}"
> 
>     tokenizer = AutoTokenizer.from_pretrained(model_path)
> 
>     dataset = load_dataset("HuggingFaceH4/ultrachat_200k",
>         split="train_sft").shuffle(seed=42).select(range(256))
> 
>     def preprocess(example):
>         return {"text": ", ".join([x['content'] for x in example["messages"]])}
>     dataset = dataset.map(preprocess)
> 
>     quant_config = QuantizeConfig(bits=bit, group_size=128, format="gptq")
> 
>     model = GPTQModel.load(model_path, 
>                            quant_config,
>                            device_map="cuda:0")
> 
>     # increase `batch_size` to match GPU/VRAM specs to speed up quantization
>     model.quantize(dataset, batch_size=8)
> 
>     model.save(quant_path)
> 
>     print(f'Model is quantized and saved at "{quant_path}"')
> ```
> 
> Here is a few things I tried: I tried to import GPTQConfig from gptqmodel, but it failed. So I tried to use GPTQConfig from transformers, and it failed saying GPTQConfig doesn't have dynamic attribute. I found that the GPTQConfig should change to QuantizeConfig. Maybe you can update the README.
> 
> Thank you so much.

After installing the latest code from the `main` branch, you can use `BACKEND.MARLIN` to load models that have been quantized using Transformers.

[PR#2828](https://github.com/ModelCloud/GPTQModel/pull/2828) FIXED this issue.
