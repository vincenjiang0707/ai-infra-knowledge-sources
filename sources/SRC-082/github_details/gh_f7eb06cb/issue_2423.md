# [Issue #2423] [BUG]: Transformers 5.x fails to correctly load Qwen 3/3.5 MoE quantized weights

source: https://github.com/ModelCloud/GPTQModel/issues/2423
state: closed | updated: 2026-03-16T22:20:30Z
labels: bug, in-progress

## 正文

**Describe the bug**

GPTQ model produce repeat "!!!!!!" junk output in llama 3.2 1B example and other Qwen3 models

Example code:
```
from gptqmodel import GPTQModel

MODEL_ID = "ModelCloud/Llama-3.2-1B-Instruct-gptqmodel-4bit-vortex-v2.5"

model = GPTQModel.load(MODEL_ID, device="cuda:0",).eval()
out = model.generate("The Capital of France is", max_new_tokens=80, do_sample=False)[0]
print(model.tokenizer.decode(out, skip_special_tokens=True))
```

Output:
```
The Capital of France is...

 programme..." your Ref spared Re Re!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

**GPU Info**

RTX pro 6000 using nvcc 12.8

```
qwen3-gptq) kurty@cst20258:~/Project/transformer_inference$ nvidia-smi
Sat Feb 21 22:53:43 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.126.09             Driver Version: 580.126.09     CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:C1:00.0 Off |                  Off |
| 30%   49C    P8              5W /  300W |   88050MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA RTX PRO 6000 Blac...    Off |   00000000:F1:00.0 Off |                  Off |
| 30%   30C    P8              5W /  300W |     248MiB /  97887MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

**Software Info**

Ubuntu 24.04 + python 3.12

Show output of:
```
pip show gptqmodel torch transformers accelerate triton


Name: GPTQModel
Version: 5.7.0

Name: torch
Version: 2.10.0+cu128

Name: transformers
Version: 5.2.0

Name: accelerate
Version: 1.12.0

Name: triton
Version: 3.6.0
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

How to reproduce this bug if possible.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (16)

### Qubitium · 2026-02-22

Going to check this soon. Maybe a regression of pkg with latest transformers

### ZX-ModelCloud · 2026-02-26

Could you provide a detailed log? I'm unable to reproduce this issue on both RTX 4090 and A100.

### Qubitium · 2026-02-27

@babyplutokurt We are unable to reproduce this error for now.

### babyplutokurt · 2026-02-27

@Qubitium @ZX-ModelCloud 

Here is my complete command:

```
conda create -n gptqmodel python=3.11 -y
conda activate gptqmodel
pip install -U pip setuptools wheel

export CUDA_HOME=/usr/local/cuda-12.8
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH

pip install -U -v gptqmodel --no-build-isolation
```

```
python - <<'PY'                                 
import torch
print("torch:", torch.__version__)
print("torch cuda version:", torch.version.cuda)
print("cuda available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))
    x = torch.randn(1024, 1024, device="cuda")
    y = x @ x
    print("matmul ok:", y[0,0].item())
PY
torch: 2.10.0+cu128
torch cuda version: 12.8
cuda available: True
gpu: NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition
matmul ok: -1.720400333404541
```

I am using script:
```
from gptqmodel import GPTQModel

MODEL_ID = "Qwen/Qwen3-30B-A3B-GPTQ-Int4"

model = GPTQModel.load(MODEL_ID, device="cuda:0",).eval()
out = model.generate("The Capital of France is", max_new_tokens=80, do_sample=False)[0]
print(model.tokenizer.decode(out, skip_special_tokens=True))
```


The output:
```
The Capital of France is organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers organisers
```

### Qubitium · 2026-03-02

@ZX-ModelCloud  @babyplutokurt  We will try to test this on our 5090 to see if this is env or gpu specific. 5090 is not the same gpu but at least has the same blackwell arch. 

### Qubitium · 2026-03-02

@babyplutokurt  We have just reproduced this issue. Checking the core cause now. 

### Qubitium · 2026-03-02

@babyplutokurt Transformers 5.0+ broke many MoE quantization inference due to a total rewrite/redesign of the MoE module forwarding by naively fusing all the applicable weights (i.e gate + up are now auto fused by HF). Previously, the models are using un-fused modeling code. 

Unfortunately transformers code doesn't actually check if the module weights are fusable as quantized weights require special fused handling and you cannot just merge weights together gunho style. 

We will need to rewrite the modeling codes for the MoE modules (Qwen3 moe for example) and monkeypatch a unfused version so the quantized gptq/awq weights can load/execute correctly. 

```py
'model.layers.45.mlp.experts.75.down_proj.g_idx', 'model.layers.8.mlp.experts.3.up_proj.qweight', 'model.layers.18.mlp.experts.47.gate_proj.qzeros', 'model.layers.20.mlp.experts.7.up_proj.g_idx', 'model.layers.44.mlp.experts.126.up_proj.g_idx', 'model.layers.36.mlp.experts.85.down_proj.scales', 'model.layers.23.mlp.experts.116.down_proj.qweight', 'model.layers.1.mlp.experts.63.down_proj.scales', 'model.layers.29.mlp.experts.34.gate_proj.g_idx', 'model.layers.1.mlp.experts.86.down_proj.qzeros', 'model.layers.40.mlp.experts.81.gate_proj.scales', 'model.layers.25.mlp.experts.101.up_proj.scales', 'model.layers.5.mlp.experts.95.gate_proj.qzeros', 'model.layers.35.mlp.experts.99.down_proj.scales', 'model.layers.34.mlp.experts.90.down_proj.qzeros', 'model.layers.30.mlp.experts.30.up_proj.scales', 'model.layers.4.mlp.experts.10.up_proj.g_idx'}. This may or may not be an issue - make sure that the checkpoint does not have unnecessary parameters, or that the model definition correctly corresponds to the checkpoint.
```

You should see a lot of warnings like this when loading qwen3 moe using Transformers 5.x. This means these weights are not correctly loaded so they are effectively all `0`/`empty` values, thus you don't get inference error but the output is utter non-sense. 

imho, tranformers should detect quantization, it has the ability to do so, and reject loading without special handlers monkey patched. Regardless we will fix it but it will take a few days.

Please use pre 5.x Transformers if you want to these models for now. 

### Qubitium · 2026-03-04

@babyplutokurt Code has been pushed to `main` which added Transformers 5.2+ support for Qwen3 quantized. Qwen 3.5 is on our next to do list. This TODO is now partially completed. 

You need to install `defuser`. `pip install defuser`. 

### Nero10578 · 2026-03-06

> [@babyplutokurt](https://github.com/babyplutokurt) Code has been pushed to `main` which added Transformers 5.2+ support for Qwen3 quantized. Qwen 3.5 is on our next to do list. This TODO is now partially completed.
> 
> You need to install `defuser`. `pip install defuser`.

Does this commit not add support for Qwen 3.5 models GPTQ quantizing? https://github.com/ModelCloud/GPTQModel/commit/00293f305044ff2efbc7ef9b2030c10239808c80

### Qubitium · 2026-03-06

> > [@babyplutokurt](https://github.com/babyplutokurt) Code has been pushed to `main` which added Transformers 5.2+ support for Qwen3 quantized. Qwen 3.5 is on our next to do list. This TODO is now partially completed.
> > You need to install `defuser`. `pip install defuser`.
> 
> Does this commit not add support for Qwen 3.5 models GPTQ quantizing? [00293f3](https://github.com/ModelCloud/GPTQModel/commit/00293f305044ff2efbc7ef9b2030c10239808c80)

@babyplutokurt  Qwen 3.5 is Transformers 5.2.0 exclusive model and it is very different from Qwen 3 in terms of how weights are stored so need special code. So our Qwen 3 fix does not apply/fix Qwen 3.5. Qwen 3.5 fix should be merged later today. The commit you mentioned was prematurely added but actually does not work until we fix it later today.

### Nero10578 · 2026-03-06

> > > [@babyplutokurt](https://github.com/babyplutokurt) Code has been pushed to `main` which added Transformers 5.2+ support for Qwen3 quantized. Qwen 3.5 is on our next to do list. This TODO is now partially completed.
> > > You need to install `defuser`. `pip install defuser`.
> > 
> > 
> > Does this commit not add support for Qwen 3.5 models GPTQ quantizing? [00293f3](https://github.com/ModelCloud/GPTQModel/commit/00293f305044ff2efbc7ef9b2030c10239808c80)
> 
> [@babyplutokurt](https://github.com/babyplutokurt) Qwen 3.5 is Transformers 5.2.0 exclusive model and it is very different from Qwen 3 in terms of how weights are stored so need special code. So our Qwen 3 fix does not apply/fix Qwen 3.5. Qwen 3.5 fix should be merged later today. The commit you mentioned was prematurely added but actually does not work until we fix it later today.

Ah okay, will wait for it to be merged. Thanks!

### Qubitium · 2026-03-06

@Nero10578 Qwen 3.5 MoE merged to `main`. You also need to update `defuser` via `pip install -U defuser`. Unfortunately there was some last minute changes even in the latest code so not sure if we have regressions. 

### Nero10578 · 2026-03-07

> [@Nero10578](https://github.com/Nero10578) Qwen 3.5 MoE merged to `main`. You also need to update `defuser` via `pip install -U defuser`. Unfortunately there was some last minute changes even in the latest code so not sure if we have regressions.

Awesome. Going to try it soon. Thanks for the update.

### Nero10578 · 2026-03-07

> [@Nero10578](https://github.com/Nero10578) Qwen 3.5 MoE merged to `main`. You also need to update `defuser` via `pip install -U defuser`. Unfortunately there was some last minute changes even in the latest code so not sure if we have regressions.

I am trying to quant Qwen 3.5 27B at the moment and it seems to be going alright so far. However I am not sure how to install Defuser 0.0.4? Googling it turns up nothing and doing the command you said it just stayed at 0.0.3.

### Qubitium · 2026-03-08

@Nero10578 There was an CI bug causing failed Defuser 0.0.4 release. Just fix it. Try it now.

### Nero10578 · 2026-03-16

> [@Nero10578](https://github.com/Nero10578) There was an CI bug causing failed Defuser 0.0.4 release. Just fix it. Try it now.

I wanted to try it but now I found a different issue. Turtle model no longer works? I don't have a big enough RAM for the larger 397B model and I tried with older GLM 4.6 that I know worked but it does not work. It doesn't create the offload folder and it tries to load all in RAM. https://github.com/ModelCloud/GPTQModel/issues/2538

Tried Qwen 3.5 27B version and the same thing, it uses so much CPU RAM. I have 512GB RAM so I can load this one, and after the initial load I seem to see the gptqmodel offload folder though but the RAM usage is still high.
