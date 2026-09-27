# [Issue #95] OSError: libnvrtc.so.12: cannot open shared object file: No such file or directory

source: https://github.com/dropbox/hqq/issues/95
state: closed | updated: 2024-07-17T05:51:31Z
labels: 

## 正文

Code:
```python
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

model_id      = "distil-whisper/distil-large-v3"
compute_dtype = torch.bfloat16 # please don't change this
device        = "cuda:0"

model     = AutoModelForSpeechSeq2Seq.from_pretrained(model_id, torch_dtype=compute_dtype) 
processor = AutoProcessor.from_pretrained(model_id)


##############################################################################
#No quantize
#model = model.to(device)

##############################################################################
from hqq.models.hf.base import AutoHQQHFModel
from hqq.core.quantize import *

# Please keep  nbits=4 and axis=1
quant_config = BaseQuantizeConfig(nbits=4, group_size=64, quant_scale=False, quant_zero=False, axis=1) 
HQQLinear.set_backend(HQQBackend.PYTORCH)

AutoHQQHFModel.quantize_model(model.model.encoder, quant_config=quant_config, compute_dtype=compute_dtype, device=device)
AutoHQQHFModel.quantize_model(model.model.decoder, quant_config=quant_config, compute_dtype=compute_dtype, device=device)

#Replace HQQLinear layers matmuls to support int4 mm
import hqq.models.base as hqq_base
hqq_base._QUANT_LAYERS = [torch.nn.Linear, HQQLinear]

from hqq.utils.patching import prepare_for_inference

AutoHQQHFModel.set_auto_linear_tags(model.model.encoder)
prepare_for_inference(model.model.encoder)

AutoHQQHFModel.set_auto_linear_tags(model.model.decoder)
prepare_for_inference(model.model.decoder, backend="torchao_int4")

model.model.encoder.forward = torch.compile(model.model.encoder.forward, mode="reduce-overhead", fullgraph=True)
model.model.decoder.forward = torch.compile(model.model.decoder.forward, mode="reduce-overhead", fullgraph=True)
# ##############################################################################

import time 
import numpy as np 

encoder_input = torch.randn([1, 80, 3000], dtype=compute_dtype, device=device)
def run_encoder():
	with torch.no_grad():
		model.model.encoder(encoder_input)
	torch.cuda.synchronize()

t = []
for _ in range(200):
	t1 = time.time()
	run_encoder()
	t2 = time.time()
	t.append(t2-t1)
print("Encoder", np.mean(t[-100:]), "sec / sample")


decoder_input = torch.randint(0, 1000, [1, 1], dtype=torch.int64, device=device)
def run_decoder():
	with torch.no_grad():
		out = model.model.decoder(decoder_input)
	torch.cuda.synchronize()


t = []
for _ in range(200):
	t1 = time.time()
	run_decoder()
	t2 = time.time()
	t.append(t2-t1)
print("Decoder", np.mean(t[-100:]), "sec / sample")
```

Error Message:
```
  File "/root/new/hqq_test.py", line 31, in <module>
    from hqq.utils.patching import prepare_for_inference
  File "/usr/local/lib/python3.10/dist-packages/hqq/utils/patching.py", line 11, in <module>
    from ..backends.bitblas import patch_hqq_to_bitblas
  File "/usr/local/lib/python3.10/dist-packages/hqq/backends/bitblas.py", line 10, in <module>
    import bitblas
  File "/usr/local/lib/python3.10/dist-packages/bitblas/__init__.py", line 19, in <module>
    from . import gpu  # noqa: F401
  File "/usr/local/lib/python3.10/dist-packages/bitblas/gpu/__init__.py", line 7, in <module>
    from .fallback import Fallback  # noqa: F401
  File "/usr/local/lib/python3.10/dist-packages/bitblas/gpu/fallback.py", line 25, in <module>
    from tvm import tir
  File "/usr/local/lib/python3.10/dist-packages/bitblas/3rdparty/tvm/python/tvm/__init__.py", line 26, in <module>
    from ._ffi.base import TVMError, __version__, _RUNTIME_ONLY
  File "/usr/local/lib/python3.10/dist-packages/bitblas/3rdparty/tvm/python/tvm/_ffi/__init__.py", line 28, in <module>
    from .base import register_error
  File "/usr/local/lib/python3.10/dist-packages/bitblas/3rdparty/tvm/python/tvm/_ffi/base.py", line 78, in <module>
    _LIB, _LIB_NAME = _load_lib()
  File "/usr/local/lib/python3.10/dist-packages/bitblas/3rdparty/tvm/python/tvm/_ffi/base.py", line 64, in _load_lib
    lib = ctypes.CDLL(lib_path[0], ctypes.RTLD_GLOBAL)
  File "/usr/lib/python3.10/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libnvrtc.so.12: cannot open shared object file: No such file or directory
```

## 评论 (1)

### mobicham · 2024-07-17

This issue is fixed in the master branch `pip uninstall hqq; pip install git+https://github.com/mobiusml/hqq.git` 
Or simply use a newer version of CUDA, looks like you use a very old version.
