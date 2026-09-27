# [Issue #4367] cannot run glm4.7-flash on 4*32GB V100

source: https://github.com/InternLM/lmdeploy/issues/4367
state: open | updated: 2026-04-07T18:23:48Z
labels: 

## 正文

cannot run glm4.7-flash on 4*32GB V100 by lmdeploy pytroch

report error:OutOfResources: out of resource: shared memory, Required: 102400, Hardware limit: 98304.

## 评论 (21)

### RunningLeon · 2026-02-26

@RNGMARTIN Hi, it may be due to the large head_dim in MLA.  Sadly, we don't have v100 on hands, pls. check if this the reason.

### valentijnvenus · 2026-02-26

Eager to know too 

### RNGMARTIN · 2026-02-27

> [@RNGMARTIN](https://github.com/RNGMARTIN) Hi, it may be due to the large head_dim in MLA. Sadly, we don't have v100 on hands, pls. check if this the reason.

Is there any solution? or it prove that V100 cannot set up Glm4.7 through lmdeploy?

### grimoire · 2026-02-28

https://github.com/InternLM/lmdeploy/blob/e5cd040c3665bd897fa0a1ea90c118f0a370fe5b/lmdeploy/messages.py#L382

Small block size might reduce smem usage.

### simonjhy · 2026-03-05

现在最新的docker image能够支持glm-4.7-flash的turbomind加速了吗？

### RunningLeon · 2026-03-06

> 现在最新的docker image能够支持glm-4.7-flash的turbomind加速了吗？

Hi, the pr is merged in https://github.com/InternLM/lmdeploy/pull/4362
You can try with `docker pull openmmlab/lmdeploy:latest-cu12.8`

### simonjhy · 2026-03-09

我拉取了这个cu12.8的image，但是依然有这个提示
soft@AI:/data/ai/dockers/composes/glm-4.7-flash-gguf-llama$ docker logs -f 6c37f6725ef5
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-03-09 07:41:00,846 - lmdeploy - INFO - async_engine.py:105 - input backend=turbomind, backend_config=TurbomindEngineConfig(dtype='auto', model_format=None, tp=4, dp=1, cp=1, device_num=None, attn_tp_size=None, attn_cp_size=None, attn_dp_size=None, mlp_tp_size=None, mlp_dp_size=None, outer_dp_size=None, nnodes=1, node_rank=0, dist_init_addr=None, devices=None, session_len=None, max_batch_size=128, cache_max_entry_count=0.8, cache_chunk_size=-1, cache_block_seq_len=64, enable_prefix_caching=False, quant_policy=0, rope_scaling_factor=0.0, use_logn_attn=False, download_dir=None, revision=None, max_prefill_token_num=8192, num_tokens_per_iter=0, max_prefill_iters=1, async_=1, empty_init=False, communicator='nccl', hf_overrides=None, enable_metrics=True)


这个是什么意思，就是说不完全支持glm-4.7-flash？

### simonjhy · 2026-03-09

我在测试的时候发现日志中提示
2026-03-09 07:57:19,727 - lmdeploy - ERROR - turbomind.py:764 - internal error. status_code 6
2026-03-09 07:57:19,727 - lmdeploy - ERROR - async_engine.py:519 - session 88 finished, ResponseType.INPUT_LENGTH_ERROR, reason "error"

这个是什么错误？需要设置什么参数来控制的吗?

### simonjhy · 2026-03-09

另外，这个glm-4.7在vllm中使用时候的下面这些参数
     --tool-call-parser glm47 \
     --reasoning-parser glm45 \
     --enable-auto-tool-choice \

在lmdeploy加载的时候需要使用什么参数？

### simonjhy · 2026-03-09

而且我在运行的时候，总是出现[TM][WARNING] [ProcessInferRequests] [2] total sequence length (12817 + 183791) exceeds `session_len` (42880), `max_new_tokens` is truncated to 30063，我如何配置才能避免生成的token不被truncated

### simonjhy · 2026-03-09

另外在opencode和claudecode中使用这个lmdeploy加载的glm-4.7-flash，均出现无法识别模型的情况，但是通过web接口访问时候没有问题。应该是需要的某些api接口lmdeploy中无法提供，导致识别不出来相应的模型


### simonjhy · 2026-03-09

还有现在没有添加上glm模型的工具调用参数，  这两个在lmdeploy中如何调用？
--tool-call-parser glm47  \
--reasoning-parser glm45 \

### RunningLeon · 2026-03-10

> 我在测试的时候发现日志中提示 2026-03-09 07:57:19,727 - lmdeploy - ERROR - turbomind.py:764 - internal error. status_code 6 2026-03-09 07:57:19,727 - lmdeploy - ERROR - async_engine.py:519 - session 88 finished, ResponseType.INPUT_LENGTH_ERROR, reason "error"
> 
> 这个是什么错误？需要设置什么参数来控制的吗?

输入tokens数大于session-len, 启动服务时调大--session-len 


> 我拉取了这个cu12.8的image，但是依然有这个提示 soft@AI:/data/ai/dockers/composes/glm-4.7-flash-gguf-llama$ docker logs -f 6c37f6725ef5 The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors. The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored. You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors. 2026-03-09 07:41:00,846 - lmdeploy - INFO - async_engine.py:105 - input backend=turbomind, backend_config=TurbomindEngineConfig(dtype='auto', model_format=None, tp=4, dp=1, cp=1, device_num=None, attn_tp_size=None, attn_cp_size=None, attn_dp_size=None, mlp_tp_size=None, mlp_dp_size=None, outer_dp_size=None, nnodes=1, node_rank=0, dist_init_addr=None, devices=None, session_len=None, max_batch_size=128, cache_max_entry_count=0.8, cache_chunk_size=-1, cache_block_seq_len=64, enable_prefix_caching=False, quant_policy=0, rope_scaling_factor=0.0, use_logn_attn=False, download_dir=None, revision=None, max_prefill_token_num=8192, num_tokens_per_iter=0, max_prefill_iters=1, async_=1, empty_init=False, communicator='nccl', hf_overrides=None, enable_metrics=True)
> 
> 这个是什么意思，就是说不完全支持glm-4.7-flash？

可以忽略这个日志




> 另外，这个glm-4.7在vllm中使用时候的下面这些参数 --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice \
> 
> 在lmdeploy加载的时候需要使用什么参数？
还未加glm相关的parser，欢迎提pr加，参考:
- https://github.com/InternLM/lmdeploy/blob/af88290c2cc07aca652c44c25a45f289e14ffd64/lmdeploy/serve/openai/reasoning_parser/qwen_qwq_reasoning_parser.py#L11
- https://github.com/InternLM/lmdeploy/blob/af88290c2cc07aca652c44c25a45f289e14ffd64/lmdeploy/serve/openai/tool_parser/qwen3_parser.py#L33



> 另外在opencode和claudecode中使用这个lmdeploy加载的glm-4.7-flash，均出现无法识别模型的情况，但是通过web接口访问时候没有问题。应该是需要的某些api接口lmdeploy中无法提供，导致识别不出来相应的模型

可以调`/v1/models` 接口如`curl http://0.0.0.0:23333/v1/models` 查看部署模型文名

### simonjhy · 2026-03-10

这个在opencode中不识别，在网页端和curl可以识别，我猜测是不是有一些API接口和opencode Claude code不兼容。关于session-len我设置了192k,实际输入值不太可能超过这个，作压力测试时候，没输入过这么长的上下文

### simonjhy · 2026-03-14

[TM][WARNING] [SegMgr] prefix caching is enabled
[TM][INFO] max cached tokens: 42880
[TM][WARNING] `session_len` truncated to 42880 due to limited KV cache memory
[TM][WARNING] [SegMgr] prefix caching is enabled
[TM][INFO] max cached tokens: 42880
[TM][WARNING] `session_len` truncated to 42880 due to limited KV cache memory
[TM][WARNING] [SegMgr] prefix caching is enabled
[TM][INFO] max cached tokens: 42880
[TM][WARNING] `session_len` truncated to 42880 due to limited KV cache memory
[TM][WARNING] [SegMgr] prefix caching is enabled
[TM][INFO] max cached tokens: 42880
[TM][WARNING] `session_len` truncated to 42880 due to limited KV cache memory


我在启动的时候总是显示这个提示？是什么意思？显存不够支持192K了？

### simonjhy · 2026-03-14

发现一个新的问题，在claude code中使用的时候，一个非常简单的"你好",我看到lmdeploy后台输出了很多的错误，
INFO:     172.18.0.4:35798 - "POST /v1/chat/completions HTTP/1.1" 200 OK
2026-03-14 14:13:32,995 - lmdeploy - ERROR - turbomind.py:764 - internal error. status_code 6
2026-03-14 14:13:32,995 - lmdeploy - ERROR - async_engine.py:519 - session 13 finished, ResponseType.INPUT_LENGTH_ERROR, reason "error"

我在docker compose的启动中使用如下的配置，是哪个地方不对吗？
    command: >
      lmdeploy serve api_server
      /models/GLM-4.7-Flash-AWQ
      --model-name GLM_4.7_30B
      --server-name 0.0.0.0
      --server-port 8000
      --backend turbomind
      --tp 4
      --session-len 196608
      --cache-max-entry-count 0.85
      --cache-block-seq-len 128
      --max-batch-size 8
      --quant-policy 4
      --enable-prefix-caching
      --max-concurrent-requests 6
      --max-prefill-token-num 16384
      --max-prefill-iters 12
      --rope-scaling-factor 0.0
      --log-level INFO
      --communicator nccl
      --tool-call-parser qwen3



### simonjhy · 2026-03-16

当我在vscode的cline插件中使用这个模型的时候，发现总是在报下面的错误，这个是什么意思？
internal error happened, status code ResponseType.INPUT_LENGTH_ERROR


### simonjhy · 2026-03-16

@RunningLeon 这个internal error happened, status code ResponseType.INPUT_LENGTH_ERROR错误是什么原因？在cline和opencode中，glm4.7的模型基本不能用，稍微处理点长文本就是ResponseType.INPUT_LENGTH_ERROR。这个怎么解决？谢谢

### lvhan028 · 2026-03-21

"[TM][WARNING] session_len truncated to 42880 due to limited KV cache memory"
这个表示 token的最大容量是 42880，因为 kv cache mem 有限。

```bash
--session-len 196608 # 并不是设置多长就能有多长，它和系统能分配出多少 kv cache 资源强相关。
--cache-max-entry-count 0.85
--cache-block-seq-len 128 # 用默认值
--max-batch-size 8
--quant-policy 4   # 不建议，4bit kv 在这个模型中是否有用，我们没有验证过
--enable-prefix-caching
--max-concurrent-requests 6 # lmdeploy 没这个参数吧。
--max-prefill-token-num 16384  # 不要设置那么大，要么用默认值，要么调小
--max-prefill-iters 12 # 不要设置
--rope-scaling-factor 0.0 # 不要设置
```

建议，当不了解推理引擎的各选项含义的时候，先用默认值。


### lvhan028 · 2026-03-21

@simonjhy This issue was originally intended to investigate running the glm-4.7-flash model on V100 with the PyTorch engine. If you have questions about the TurboMind engine, please open a separate issue.


### jagmarques · 2026-04-07

The  being truncated to 42880 despite setting 192K is a pure KV cache memory budget issue — the engine computes how many KV blocks fit given  of available VRAM and caps  to whatever that allows. With 4×32GB V100s and a large MLA head_dim model, 80% of free VRAM after weights often isn't enough to fit a 192K KV buffer.

A few things worth trying:

1. **Reduce ** won't help here — you need more tokens, not fewer. Instead, reduce model weight memory first: use  (8-bit weight quantization) to free up VRAM for KV cache. On V100 with FP16 weights, this alone can double the available KV budget.

2. **Reduce ** from 64 to 32 — smaller blocks mean finer granularity and the engine may pack more usefully.

3. **Check actual free VRAM after model load** with  right after the engine initializes. If weights consume >28GB across 4 GPUs, there's simply not enough headroom for 192K × KV_head_dim × 2 bytes.

4. For the  with a simple "你好" query: this usually means the model's context window baked into its config is shorter than . GLM-4.7-Flash may have a max_position_embeddings that conflicts. Check  in the model directory.

Longer-term: KV cache compression (quantizing cached KV entries to 3–4 bits instead of 16-bit) would multiply your effective context window 4–5x without adding GPUs. The lmdeploy  flag covers weight quantization but not KV quantization yet — worth tracking as a feature request for V100-class deployments where memory is the hard constraint.
