# [Issue #2440] [Transformers 5.2 Compat] AWQ quantization fails for Qwen3.5 with device mismatch in rotary embeddings

source: https://github.com/ModelCloud/GPTQModel/issues/2440
state: closed | updated: 2026-03-14T00:50:55Z
labels: bug, in-progress

## 正文

AWQ quantization crashes on Qwen3.5-27B at layer 3 (self_attn layer) with a device mismatch error. The rotary embeddings tensor is on CPU while other tensors are on CUDA. GPTQ quantization works fine for the same model.

NVIDIA-SMI 595.71
Driver Version: 595.71
CUDA Version: 13.2 
Windows 11 Pro
Python 3.12.10
torch: 2.10.0+cu130
transformers: 5.2.0
accelerate 1.12.0
GPTQModel 5.7.1 (commit 83a9a06ee0d9e97f84f68f5996589a642b1e5080)

**To Reproduce**

from gptqmodel import GPTQModel
from gptqmodel.quantization import QuantizeConfig, FORMAT, METHOD
from datasets import load_dataset

quantize_config = QuantizeConfig(
    bits=4,
    group_size=128,
    format=FORMAT.LLM_AWQ,
    quant_method=METHOD.AWQ,
)

dataset = load_dataset("allenai/c4", "en", split="train", streaming=True)
calibration_data = []
for sample in dataset:
    if len(sample["text"]) > 2000:
        calibration_data.append(sample["text"])
    if len(calibration_data) >= 256:
        break

model = GPTQModel.load(
    "Qwen/Qwen3.5-27B",  # or any Qwen3.5 model
    quantize_config=quantize_config,
    trust_remote_code=True,
)

model.quantize(
    calibration=calibration_data,
    batch_size=1,
)


**Expected behavior**

AWQ quantization should complete successfully, as GPTQ quantization does for the same model.

**Model/Datasets**

- Model: `Qwen/Qwen3.5-27B` (or any Qwen3.5 variant)
- Dataset: `allenai/c4`

**Error Traceback**

RuntimeError: Expected all tensors to be on the same device, but got mat2 is on cuda:0, different from other tensors on cpu (when checking argument in method wrapper_CUDA_bmm)

File "gptqmodel/looper/awq_processor.py", line 1096, in _module_forward
    module_kwargs["position_embeddings"] = rotary(x_for_rotary, pos_for_rotary)

File "transformers/models/qwen3_5/modeling_qwen3_5.py", line 238, in forward
    freqs = (inv_freq_expanded.float() @ position_ids_expanded.float()).transpose(2, 3)

**Additional context**

Crash occurs at layer 3 (first self_attn layer - Qwen3.5 uses a 3:1 pattern of linear_attn to self_attn)
Layers 0-2 (linear_attn) process successfully before the crash
GPTQ quantization (both 4-bit and 8-bit) completes successfully for the same model
Qwen3.5 support was added on 02/28/2026 - AWQ path may not be fully tested for this architecture

## 评论 (19)

### modelfix · 2026-03-04

Hey! I noticed you were having trouble converting `Qwen/Qwen3.5-27B`. 

I successfully converted and verified it to GGUF using ModelFix. You can test it out and download it here:
https://modelfix.com?model=Qwen/Qwen3.5-27B

Hope this helps!

### Qubitium · 2026-03-05

@erm14254  We currently do not yet have Qwen 3.5 support for Transformerfs 5.2.0 until this PR is tested and merged:

https://github.com/ModelCloud/Defuser/pull/11/changes

### erm14254 · 2026-03-06

> [@erm14254](https://github.com/erm14254) We currently do not yet have Qwen 3.5 support for Transformerfs 5.2.0 until this PR is tested and merged:
> 
> https://github.com/ModelCloud/Defuser/pull/11/changes

Thank you, I saw that it was merged and updated defuser to 0.0.4, GPTQModel 5.8.0 and Transformers 5.3.0 (non-dev) and AWQ is still broken, tested on both Qwen3.5 27B and GPT OSS 120B, impossible to AWQ any of them.

Also another issue inside site-packages\gptqmodel\looper\ `stage_layer.py` at line 16, this "from defuser.modeling.fused_moe.replace_modules import materialize_model_" is wrong, it should be "from defuser.modeling.fused_moe.replace_modules import materialize_model as materialize_model_" instead.

### Qubitium · 2026-03-09

> > [@erm14254](https://github.com/erm14254) We currently do not yet have Qwen 3.5 support for Transformerfs 5.2.0 until this PR is tested and merged:
> > https://github.com/ModelCloud/Defuser/pull/11/changes
> 
> Thank you, I saw that it was merged and updated defuser to 0.0.4, GPTQModel 5.8.0 and Transformers 5.3.0 (non-dev) and AWQ is still broken, tested on both Qwen3.5 27B and GPT OSS 120B, impossible to AWQ any of them.
> 
> Also another issue inside site-packages\gptqmodel\looper\ `stage_layer.py` at line 16, this "from defuser.modeling.fused_moe.replace_modules import materialize_model_" is wrong, it should be "from defuser.modeling.fused_moe.replace_modules import materialize_model as materialize_model_" instead.

Checking on our end. Also `defuser.modeling.fused_moe.replace_modules import materialize_model_` points to the fact you may not have checked out the latest code on `main` as this issue was fixed. 

### Qubitium · 2026-03-09


@erm14254  Pleaes test https://github.com/ModelCloud/GPTQModel/pull/2453. Thanks.

### erm14254 · 2026-03-09

> [@erm14254](https://github.com/erm14254) Pleaes test [#2453](https://github.com/ModelCloud/GPTQModel/pull/2453). Thanks.

I did and updated and:

There is a bug on: Lib\site-packages\defuser\__init__.py

On line 8, it's: from .defuser import convert_hf_model as _convert_hf_model

While it should be: from .defuser import convert_model as _convert_hf_model

Also another issue: ValueError: Unsupported model_type: qwen3_5_text

And another issue: ValueError: Unsupported model_type: gpt_oss

### Qubitium · 2026-03-09

> > [@erm14254](https://github.com/erm14254) Pleaes test [#2453](https://github.com/ModelCloud/GPTQModel/pull/2453). Thanks.
> 
> I did and updated and:
> 
> There is a bug on: Lib\site-packages\defuser\__init__.py
> 
> On line 8, it's: from .defuser import convert_hf_model as _convert_hf_model
> 
> While it should be: from .defuser import convert_model as _convert_hf_model
> 
> Also another issue: ValueError: Unsupported model_type: qwen3_5_text
> 
> And another issue: ValueError: Unsupported model_type: gpt_oss

Did u update defuser to v0.0.5 which was updated in the last hour?

@zx-modelcloud

### erm14254 · 2026-03-09

> > > [@erm14254](https://github.com/erm14254) Pleaes test [#2453](https://github.com/ModelCloud/GPTQModel/pull/2453). Thanks.
> > 
> > 
> > I did and updated and:
> > There is a bug on: Lib\site-packages\defuser__init__.py
> > On line 8, it's: from .defuser import convert_hf_model as _convert_hf_model
> > While it should be: from .defuser import convert_model as _convert_hf_model
> > Also another issue: ValueError: Unsupported model_type: qwen3_5_text
> > And another issue: ValueError: Unsupported model_type: gpt_oss
> 
> Did u update defuser to v0.0.5 which was updated in the last hour?
> 
> [@ZX-ModelCloud](https://github.com/ZX-ModelCloud)

Yep, see:

Successfully installed Defuser-0.0.5 annotated-doc-0.0.4 anyio-4.12.1 certifi-2026.2.25 click-8.3.1 colorama-0.4.6 filelock-3.25.0 fsspec-2026.2.0 h11-0.16.0 hf-xet-1.3.2 httpcore-1.0.9 httpx-0.28.1 huggingface-hub-1.6.0 idna-3.11 markdown-it-py-4.0.0 mdurl-0.1.2 numpy-2.4.3 packaging-26.0 pygments-2.19.2 pyyaml-6.0.3 regex-2026.2.28 rich-14.3.3 safetensors-0.7.0 shellingham-1.5.4 tokenizers-0.22.2 tqdm-4.67.3 transformers-5.3.0 typer-0.24.1 typing-extensions-4.15.0

### Qubitium · 2026-03-09

@erm14254  Please try latest `main` (which also comes with awq oom fix) with defuser 0.0.6 update (which fixes the current issue you reported). I have reopened this issue and will only close once it has been truely fixed. @ZX-ModelCloud  did a unit test using qwen 3.5 but we did not test oss. 

### erm14254 · 2026-03-09

> [@erm14254](https://github.com/erm14254) Please try latest `main` (which also comes with awq oom fix) with defuser 0.0.6 update (which fixes the current issue you reported). I have reopened this issue and will only close once it has been truely fixed. [@ZX-ModelCloud](https://github.com/ZX-ModelCloud) did a unit test using qwen 3.5 but we did not test oss.

Updated, see:

Successfully installed defuser-0.0.6

But issues, first issue, inside notepad Lib\site-packages\gptqmodel\models\loader.py, line 251 is:

"defuser.convert_hf_model(model, cleanup_original=False)"

While it should be:

"defuser.convert_model(model, cleanup_original=False)"

Tried with Qwen3.5 27B for AWQ and still issue even with this fix:

"from defuser.modeling.fused_moe.replace_modules import materialize_model as materialize_model_
ModuleNotFoundError: No module named 'defuser.modeling.fused_moe'"

Tried with GPT OSS for GPTQ:

"defuser.convert_hf_model(model, cleanup_original=False)
    ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: module 'defuser' has no attribute 'convert_hf_model'. Did you mean: 'convert_model'?"

So issues are:

**Issue 1:** `loader.py` line 251 calls `defuser.convert_hf_model()` but defuser only has `convert_model()`

**Issue 2:** After patching issue 1, AWQ on Qwen3.5-27B fails:
ModuleNotFoundError: No module named 'defuser.modeling.fused_moe'

**Issue 3:** GPTQ on GPT-OSS hits same issue 1 (convert_hf_model not found)

Tested on: Windows, Python 3.12, GPTQModel 5.8.0, defuser 0.0.6

### Qubitium · 2026-03-09

@ZX-ModelCloud Did we fix all the name changes? Need to test with clean install of gptmodel and defuser. Thought we passed the  unit tests but user showing init errors and still using old method names?

### Qubitium · 2026-03-09

@CSY-ModelCloud Did we correctly export the defuser pkg internal paths in the stdlib pkging? User reprting packaged defuse missing paths?

### Qubitium · 2026-03-09

@erm14254 Please test checkout defuser manually and exec

pip install -v -e . 

do the same for gptmodel but 

pip install -v -e . --no-build-isolation



### Qubitium · 2026-03-10

@erm14254  We are currently fixing awq issue with Qwen 3.5 Moe. 

### Qubitium · 2026-03-10

@erm14254  AWQ Qwen 3.5 MoE quantization is now working/in-progress on `main`. Once quantized, we will test inference. 

### erm14254 · 2026-03-12

> [@erm14254](https://github.com/erm14254) AWQ Qwen 3.5 MoE quantization is now working/in-progress on `main`. Once quantized, we will test inference.

AWQ is finally working, just tested with Qwen3.5 27B and it worked. While GPT OSS 120B works neither with GPTQ nor with AWQ.

### Qubitium · 2026-03-12

@erm14254 Yes, we have also confirmed it working but multi-gpu awq qunatization of Qwen 3.5 Moe is still pending bug fix. OSS is on our todo list but we have not had time to verify it. 

### Qubitium · 2026-03-12

Closing as completed. 

### Qubitium · 2026-03-14

@erm14254  OSS compat has been fixex with https://github.com/ModelCloud/GPTQModel/pull/2508
