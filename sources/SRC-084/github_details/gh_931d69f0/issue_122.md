# [Issue #122] KeyError: 'offload_meta'

source: https://github.com/dropbox/hqq/issues/122
state: closed | updated: 2024-11-01T18:45:49Z
labels: 

## 正文

Code:

```python
import torch
from whisperplus.pipelines.whisper import SpeechToTextPipeline
from transformers import HqqConfig

audio_path = "test.mp3"

q4_config = {'nbits':4, 'group_size':64, 'quant_zero':False, 'quant_scale':False}
q3_config = {'nbits':3, 'group_size':32, 'quant_zero':False, 'quant_scale':False}
quant_config  = HqqConfig(dynamic_config={
  'self_attn.q_proj':q4_config,
  'self_attn.k_proj':q4_config,
  'self_attn.v_proj':q4_config,
  'self_attn.o_proj':q4_config,

  'mlp.gate_proj':q3_config,
  'mlp.up_proj'  :q3_config,
  'mlp.down_proj':q3_config,
})

model = SpeechToTextPipeline(
    model_id="distil-whisper/distil-large-v3", quant_config=quant_config, flash_attention_2=True)  # or bnb_config

start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)

start_event.record()
transcript = model(
    audio_path=audio_path,
    chunk_length_s=30,
    stride_length_s=5,
    max_new_tokens=128,
    batch_size=100,
    language="english",
    return_timestamps=False)
end_event.record()

torch.cuda.synchronize()
elapsed_time_ms = start_event.elapsed_time(end_event)
seconds = elapsed_time_ms / 1000
print(f"Elapsed time: {seconds} seconds")
```

Error Message:
```bash
    self.quant_config.pop("offload_meta")
KeyError: 'offload_meta'
```

## 评论 (1)

### mobicham · 2024-10-02

```
pip install --upgrade git+https://github.com/huggingface/transformers.git
pip install --upgrade git+https://github.com/mobiusml/hqq.git 
```
