# [Issue #82] Running HQQ Quantized Models on CPU

source: https://github.com/dropbox/hqq/issues/82
state: closed | updated: 2024-06-05T11:49:59Z
labels: 

## 正文

Hi, I am trying to run HQQ quantized models on CPU, however I got the following error:

```
Failed to load the weights
Traceback (most recent call last):
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/hqq/models/base.py", line 461, in from_quantized
    weights = cls.load_weights(save_dir)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/hqq/models/base.py", line 234, in load_weights
    return torch.load(cls.get_weight_file(save_dir), map_location=map_location)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 1025, in load
    return _load(opened_zipfile,
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 1446, in _load
    result = unpickler.load()
             ^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 1416, in persistent_load
    typed_storage = load_tensor(dtype, nbytes, key, _maybe_decode_ascii(location))
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 1390, in load_tensor
    wrap_storage=restore_location(storage, location),
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 390, in default_restore_location
    result = fn(storage, location)
             ^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 265, in _cuda_deserialize
    device = validate_cuda_device(location)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/torch/serialization.py", line 249, in validate_cuda_device
    raise RuntimeError('Attempting to deserialize object on a CUDA '
RuntimeError: Attempting to deserialize object on a CUDA device but torch.cuda.is_available() is False. If you are running on a CPU-only machine, please use torch.load with map_location=torch.device('cpu') to map your storages to the CPU.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/user/Documents/test.py", line 8, in <module>
    model = HQQModelForCausalLM.from_quantized(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/hqq/engine/base.py", line 87, in from_quantized
    model = cls._get_hqq_class(arch_key).from_quantized(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/user/anaconda3/envs/hqq/lib/python3.11/site-packages/hqq/models/base.py", line 464, in from_quantized
    raise FileNotFoundError
FileNotFoundError
``` 

I am trying to use the inference demo in the examples:
```
from hqq.core.quantize import *

from hqq.engine.hf import HQQModelForCausalLM
HQQLinear.set_backend(HQQBackend.PYTORCH)
# HQQLinear.set_backend(HQQBackend.PYTORCH_COMPILE)


model_id = "mobiuslabsgmbh/Llama-2-7b-chat-hf_1bitgs8_hqq"

model = HQQModelForCausalLM.from_quantized(
    model_id,
    compute_dtype=torch.float32,
    device="cpu",
)
```

However it fails to load the weights by throwing the above error. I have tried with both backends `PYTORCH` and `PYTORCH_COMPILE`. 

My environment:
```yaml
HQQ: Installed from source `pip install git+https://github.com/mobiusml/hqq`
Pytorch:
```
```
torch                    2.3.0
torchaudio               2.3.0
torchvision              0.18.0
```

Any reason why it doesn't work on CPU?

## 评论 (3)

### mobicham · 2024-06-05

Hi, CPU support is limited. It works if you quantize on the fly, and it's actually slow and takes more memory since Pytorch doesn't support fp16 on cpu, everything would run with fp32. 

That saved quantized model you are trying to load was saved with CUDA tensors, since you don't have a GPU on your machine, it cannot convert those CUDA tensors to the CPU, hence the error.

I recommend you simply use a free gpu on google colab if you just want to test, we focus mainly on gpu runtime since the bottleneck is VRAM not the RAM. 

### 49Simon · 2024-06-05

Oh okay. I actually have a GPU and tested it and works fine. I am interested in running models locally on CPU. HQQ quantized models have very good performance while saving memory. Converting a model to GGUF format is the best way of running models on CPU. Llama.cpp does not have support for HQQ models though. Thank you for your reply. 

### mobicham · 2024-06-05

I see, I mean you can run them on cpu if you quantize on-the-fly, but transformers on CPU is quite slow.

Or if someone wants to convert HQQ to GGUF format, it would be great. Unfortunately I am swamped with too many things so I don't have the time to look into it, but I think it should be possible if it's simple asymmetric quantization with grouping. 
