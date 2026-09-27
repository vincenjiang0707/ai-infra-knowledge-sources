# [Issue #76] No module named 'hqq.engine' Error.

source: https://github.com/dropbox/hqq/issues/76
state: closed | updated: 2024-05-28T10:23:23Z
labels: 

## 正文

Hi, thanks for the amazing project!.
I quant the Mistral-7x8 successfully on the slurm machine. But, when I download the model and want to use it to inference. I met an error:

```
ModuleNotFoundError: No module named 'hqq.engine'; 'hqq' is not a package
```

Here is my code (same with samples):

```
import transformers 
from threading import Thread
from hqq.core.quantize import *
from hqq.engine.hf import HQQModelForCausalLM, AutoTokenizer
transformers.logging.set_verbosity_info()

tokenizer = AutoTokenizer.from_pretrained(quant_path)
model = HQQModelForCausalLM.from_quantized(quant_path)

print("load model")

def chat_processor(chat, max_new_tokens=100, do_sample=True):
    tokenizer.use_default_system_prompt = False
    streamer = transformers.TextIteratorStreamer(tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True)

    generate_params = dict(
        tokenizer("<s> [INST] " + chat + " [/INST] ", return_tensors="pt").to('cuda'),
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        top_p=0.90,
        top_k=50,
        temperature= 0.6,
        num_beams=1,
        repetition_penalty=1.2,
    )

    t = Thread(target=model.generate, kwargs=generate_params)
    t.start()
    outputs = []
    for text in streamer:
        outputs.append(text)
        print(text, end="", flush=True)

    return outputs

################################################################################################
#Generation
outputs = chat_processor("What is finance?", max_new_tokens=1000, do_sample=False)
```

I used two different machines (3090) to test this code, but it still has errors. 

## 评论 (2)

### yixuantt · 2024-05-28

Here is my environment.

```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005–2022. NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0
```

```
torch              2.0.1+cu118
torchaudio         2.0.2+cu118
torchvision        0.15.2+cu118
```

I also tested installing from the source. But the error remains.

### yixuantt · 2024-05-28

Oh. Sorry. It was my mistake. Close with thanks.
