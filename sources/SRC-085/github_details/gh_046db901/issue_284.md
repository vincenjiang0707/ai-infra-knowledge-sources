# [Issue #284] sglang 运行AngelSlim/Qwen3-4B_eagle3 问题

source: https://github.com/SafeAILab/EAGLE/issues/284
state: open | updated: 2025-11-03T08:59:38Z
labels: 

## 正文

您好，我这边使用lmsysorg/sglang:latest的镜像运行模型，
使用的命令如下：
python3 -m sglang.launch_server --model /models/Qwen3-4B --speculative-algorithm EAGLE3 --speculative-draft-model-path /models/Qwen3-4B_eagle3 --speculative-num-steps 5 --speculative-eagle-topk 8 --speculative-num-draft-tokens 32 --mem-fraction 0.5 --served-model-name codeqwen --cuda-graph-max-bs 2 --dtype float16
最终报如下错误：
  File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 2555, in run_scheduler_process
    scheduler = Scheduler(
                ^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 329, in __init__
    self.draft_worker = EAGLEWorker(
                        ^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/speculative/eagle_worker.py", line 125, in __init__
    super().__init__(
  File "/sgl-workspace/sglang/python/sglang/srt/managers/tp_worker.py", line 84, in __init__
    self.model_runner = ModelRunner(
                        ^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/model_executor/model_runner.py", line 242, in __init__
    self.initialize(min_per_gpu_memory)
  File "/sgl-workspace/sglang/python/sglang/srt/model_executor/model_runner.py", line 288, in initialize
    self.load_model()
  File "/sgl-workspace/sglang/python/sglang/srt/model_executor/model_runner.py", line 679, in load_model
    self.model = get_model(
                 ^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/model_loader/__init__.py", line 22, in get_model
    return loader.load_model(
           ^^^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/model_loader/loader.py", line 444, in load_model
    model = _initialize_model(
            ^^^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/model_loader/loader.py", line 186, in _initialize_model
    return model_class(
           ^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/models/llama_eagle3.py", line 183, in __init__
    self.model = LlamaModel(
                 ^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/models/llama_eagle3.py", line 130, in __init__
    self.midlayer = LlamaDecoderLayer(config, 0, quant_config, prefix)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/models/llama_eagle3.py", line 50, in __init__
    super().__init__(config, layer_id, quant_config, prefix)
  File "/sgl-workspace/sglang/python/sglang/srt/models/llama.py", line 227, in __init__
    self.self_attn = LlamaAttention(
                     ^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/models/llama.py", line 170, in __init__
    self.rotary_emb = get_rope(
                      ^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/layers/rotary_embedding.py", line 1716, in get_rope
    rotary_emb = RotaryEmbedding(
                 ^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/layers/rotary_embedding.py", line 107, in __init__
    from vllm._custom_ops import rotary_embedding
ModuleNotFoundError: No module named 'vllm'

想请问一下可以运行AngelSlim/Qwen3-4B_eagle3模型的版本号是多少，需要安装对应的vllm，vllm的版本号是多少，有相应的可以运行的镜像提供吗

## 评论 (1)

### wjiannan · 2025-11-03

请问解决了不，我这边pip install vllm以后，出现新的报错：AttributeError: 'VocabParallelEmbedding' object has no attribute 'weight'
