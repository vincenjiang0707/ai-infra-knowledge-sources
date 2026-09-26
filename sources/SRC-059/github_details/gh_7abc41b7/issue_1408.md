# [Issue #1408] ERNIE-4.5-VL-28B-A3B-Paddle sft 训练报错：AssertionError: weight_idxs' length should be greater than 0

source: https://github.com/PaddlePaddle/ERNIE/issues/1408
state: open | updated: 2026-01-13T04:54:38Z
labels: 

## 正文

根据官方环境：
paddle_xpu             0.0.1
paddle2onnx            2.0.1
paddleformers          0.4.0
paddlepaddle-xpu       3.3.0.dev20251016

启动命令：erniekit train  examples/configs/xpu/ERNIE-4.5-VL-28B-A3B/sft/run_sft_32k.yaml

[2025-12-23 12:07:45,066] [    INFO] pp_layers.py:854 - start segment network..
Traceback (most recent call last):
  File "/work/ERNIE/erniekit/launcher.py", line 58, in <module>
    launch()
  File "/work/ERNIE/erniekit/launcher.py", line 46, in launch
    run_tuner()
  File "/work/ERNIE/erniekit/train/tuner.py", line 82, in run_tuner
    _training_function(config={"args": args})
  File "/work/ERNIE/erniekit/train/tuner.py", line 59, in _training_function
    run_vl_sft(
  File "/work/ERNIE/erniekit/train/vl_sft/workflow.py", line 517, in run_vl_sft
    model = Ernie4_5_VLMoeForConditionalGenerationPipe.from_pretrained(
  File "/usr/local/lib/python3.10/dist-packages/paddleformers/transformers/model_utils.py", line 2965, in from_pretrained
    model = cls(config, *init_args, **model_kwargs)
  File "/usr/local/lib/python3.10/dist-packages/paddleformers/transformers/utils.py", line 290, in __impl__
    init_func(self, *args, **kwargs)
  File "/work/ERNIE/ernie/modeling_moe_vl_pp.py", line 1908, in __init__
    PipelineLayer.__init__(
  File "/usr/local/lib/python3.10/dist-packages/paddle/distributed/fleet/meta_parallel/parallel_layers/pp_layers.py", line 506, in __init__
    self._segment_network(seg_method)
  File "/usr/local/lib/python3.10/dist-packages/paddle/distributed/fleet/meta_parallel/parallel_layers/pp_layers.py", line 858, in _segment_network
    self.segment_parts = seg.do_segment()
  File "/usr/local/lib/python3.10/dist-packages/paddle/distributed/fleet/meta_parallel/parallel_layers/pp_layers.py", line 187, in do_segment
    weight_idxs = self._gen_layer_weight(layername)
  File "/usr/local/lib/python3.10/dist-packages/paddle/distributed/fleet/meta_parallel/parallel_layers/pp_layers.py", line 234, in _gen_layer_weight
    assert len(weight_idxs) > 0, (
AssertionError: weight_idxs' length should be greater than 0

## 评论 (1)

### DongBaiYue · 2026-01-13

dev分支的XPU支持被破坏了，可以暂时使用这个特定版本。
```
# paddle
pip uninstall paddle_xpu
python -m pip install --pre paddlepaddle-xpu -i https://www.paddlepaddle.org.cn/packages/nightly/xpu-p800/
# PaddleFormers
git clone https://github.com/PaddlePaddle/PaddleFormers.git
cd PaddleFormers
git checkout 95efaadff11a0d730833eb13db8a08f6857ac3c0
pip install -e .
cd ..
# ERNIE
git clone https://github.com/PaddlePaddle/ERNIE.git -b develop
cd ERNIE
git checkout 6357e913103adc829846ead3bd4cef6f8b3a1c55
pip install -r requirements/gpu/requirements.txt
pip install -e .

```
