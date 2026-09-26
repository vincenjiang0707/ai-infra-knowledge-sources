# [Issue #53] AttributeError: module 'torch_npu.npu' has no attribute 'profile' 

source: https://github.com/Ascend/pytorch/issues/53
state: open | updated: 2024-10-15T11:55:12Z
labels: 

## 正文

test: **Add with torch_npu.npu.profile(profiler_result_path="./result",use_e2e_profiler=True): to get the profile data**
```
import torch
import torch_npu
from melo.api import TTS
import time
from torch_npu.contrib import transfer_to_npu

speed = 1.0
device = 'npu'
model = TTS(language='ZH', device=device,config_path= "../model/melotts/config.json", ckpt_path="../model/melotts/checkpoint.pth")

speaker_ids = model.hps.data.spk2id

start = time.time()
text = """
你好
"""
for i in range(2):
        start = time.time()
        with torch_npu.npu.profile(profiler_result_path="./result",use_e2e_profiler=True):
          model.tts_to_file(text, speaker_ids['ZH'], output_path = "../test_0926_nobert.wav", speed=speed)
        end = time.time()
        print(end-start)

```

* It report missing **profile**
```
Traceback (most recent call last):
  File "/home/zhongyunde/tts/app_server/test2.py", line 22, in <module>
    with torch_npu.npu.profile(profiler_result_path="./result",use_e2e_profiler=True):
AttributeError: module 'torch_npu.npu' has no attribute 'profile'
[ERROR] 2024-10-12-11:58:06 (PID:1727, Device:0, RankID:-1) ERR99999 UNKNOWN application exception
```
* tool version:
-- CANN ：7.3
-- Python  : Python 3.10.0
-- torch  2.1.0, torch_npu 2.1.0.post6

## 评论 (1)

### yunyiyun · 2024-10-15

你所使用的版本，对应profiling使用请参考
https://www.hiascend.com/document/detail/zh/canncommercial/80RC2/devaids/auxiliarydevtool/atlasprofiling_16_0006.html
