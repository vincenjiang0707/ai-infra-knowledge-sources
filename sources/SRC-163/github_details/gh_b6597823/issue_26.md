# [Issue #26] Why appear 0 unaccepted, 0 waiting, 0 processing？

source: https://github.com/LLMServe/DistServe/issues/26
state: open | updated: 2024-08-14T12:36:42Z
labels: 

## 正文

I use offline example.
When I use tensor_parallel_size=1, pipeline_parallel_size=1, the result is correct. But when tensor_parallel_size=2, pipeline_parallel_size=2， it will loop infinitely. As show below.

```bash
INFO 03:52:48 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 03:52:49 (context) 0 waiting, 0 finished but unaccepted, 6 blocks occupied by on-the-fly requests
INFO 03:52:49 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 03:52:49 (decoding) GPU blocks: 0 / 2916 (0.00%) used, (0 swapping out)
INFO 03:52:49 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 03:52:50 (context) 0 waiting, 0 finished but unaccepted, 6 blocks occupied by on-the-fly requests
INFO 03:52:50 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 03:52:50 (decoding) GPU blocks: 0 / 2916 (0.00%) used, (0 swapping out)
INFO 03:52:50 (decoding) 0 unaccepted, 0 waiting, 0 processing
INFO 03:52:51 (context) 0 waiting, 0 finished but unaccepted, 6 blocks occupied by on-the-fly requests
INFO 03:52:51 (decoding) CPU blocks: 0 / 128 (0.00%) used, (0 swapping in)
INFO 03:52:51 (decoding) GPU blocks: 0 / 2916 (0.00%) used, (0 swapping out)
INFO 03:52:51 (decoding) 0 unaccepted, 0 waiting, 0 processing
```

Here is my code. Thank you.
```python
import argparse
import os
from distserve import OfflineLLM, SamplingParams
from distserve.config import (
    ModelConfig,
    DisaggParallelConfig,
    ParallelConfig,
    CacheConfig,
    ContextStageSchedConfig,
    DecodingStageSchedConfig
)
os.environ['CUDA_VISIBLE_DEVICES']='2,3,4,5,6,7'
parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, help='The model to use', default='/home/xiaoxu/test/Llama-2-7b-hf')
args = parser.parse_args()

prompts = [
    "Life blooms like a flower. Far away or by the road. Waiting",
    "A quick brown fox",
    "Artificial intelligence is",
    "To be or not to be,",
    "one two three four"
]
sampling_params = SamplingParams(
    temperature=0.8, top_p=0.95, max_tokens=64, stop=["\n"]
)
llm = OfflineLLM(
    model_config=ModelConfig(
        model=args.model,
        tokenizer=None
    ),
    disagg_parallel_config=DisaggParallelConfig(
        context=ParallelConfig(
            tensor_parallel_size=2,
            pipeline_parallel_size=2
        ),
        decoding=ParallelConfig(
            tensor_parallel_size=1,
            pipeline_parallel_size=1
        )
    ),
    cache_config=CacheConfig(
        block_size=16,
        max_num_blocks_per_req=1024,
        gpu_memory_utilization=0.9,
        cpu_swap_space=1.0
    ),
    context_sched_config=ContextStageSchedConfig(
        policy="fcfs",
        max_batch_size=4,
        max_tokens_per_batch=16384
    ),
    decoding_sched_config=DecodingStageSchedConfig(
        policy="fcfs",
        max_batch_size=4,
        max_tokens_per_batch=16384
    )
)
outputs = llm.generate(prompts=prompts, sampling_params=sampling_params)
for prompt, step_outputs in zip(prompts, outputs):
    # new_token_ids = [step_output.new_token_id for step_output in step_outputs]
    # output_text = llm.tokenizer.decode(new_token_ids)
    print(
        f"Prompt: {prompt!r}, Generated text: {' '.join([step_output.new_token for step_output in step_outputs])} ({len(step_outputs)} tokens generated)."
    )
```

## 评论 (5)

### Avabowler · 2024-08-09

hi Le, I had the same problem, have you solved it yet?

### Youhe-Jiang · 2024-08-12

I face the same problem, I think you can also see the problem like this:

(ParaWorker pid=1955026) Error: Peer-to-peer access is unsupported on this platform.
(ParaWorker pid=1955026) In the current version of distserve, it is necessary to use a platform that supports GPU P2P access.
(ParaWorker pid=1955026) Exiting...

Idk how to solve the problem, maybe you can @me if you have any solutions, thank you.

### LeSoleilGo · 2024-08-13


> hi Le, I had the same problem, have you solved it yet?你好，Le，我也遇到了同样的问题，你现在解决了吗？

I think if you want to use pp, you need to have multiple nodes. This is my guess。And TP can be used correctly.

### TZHelloWorld · 2024-08-14





> > hi Le, I had the same problem, have you solved it yet?你好，Le，我也遇到了同样的问题，你现在解决了吗？
> 
> I think if you want to use pp, you need to have multiple nodes. This is my guess。And TP can be used correctly.

i use `CUDA_VISIBLE_DEVICES=0 python examples/offline.py` , and it show :

```
(autoscaler +6s) Tip: use `ray status` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0.
(autoscaler +6s) Error: No available node types can fulfill resource request defaultdict(<class 'float'>, {'GPU': 2.0}). Add suitable node types to this cluster to resolve this issue.
(autoscaler +41s) Error: No available node types can fulfill resource request defaultdict(<class 'float'>, {'GPU': 2.0}). Add suitable node types to this cluster to resolve this issue.
```

It doesn't seem to be a problem with multiple nodes, but it may be caused by specifying the local model with --model.
You can convert the model like I did, copy the relevant configuration file, and then use the converted model to verify it:

```
python distserve/downloader/converter.py \
--input "/workspace/models/opt-13b/*.bin" \
--output /workspace/models/distserve/opt-13b \
--dtype float16 \
--model opt

cp *.{json,txt} /workspace/models/distserve/opt-13b
```

and then  use：

` --model  /workspace/models/distserve/opt-13b`

### Avabowler · 2024-08-14

> > > hi Le, I had the same problem, have you solved it yet?你好，Le，我也遇到了同样的问题，你现在解决了吗？
> > 
> > 
> > I think if you want to use pp, you need to have multiple nodes. This is my guess。And TP can be used correctly.
> 
> i use `CUDA_VISIBLE_DEVICES=0 python examples/offline.py` , and it show :
> 
> ```
> (autoscaler +6s) Tip: use `ray status` to view detailed cluster status. To disable these messages, set RAY_SCHEDULER_EVENTS=0.
> (autoscaler +6s) Error: No available node types can fulfill resource request defaultdict(<class 'float'>, {'GPU': 2.0}). Add suitable node types to this cluster to resolve this issue.
> (autoscaler +41s) Error: No available node types can fulfill resource request defaultdict(<class 'float'>, {'GPU': 2.0}). Add suitable node types to this cluster to resolve this issue.
> ```
> 
> It doesn't seem to be a problem with multiple nodes, but it may be caused by specifying the local model with --model. You can convert the model like I did, copy the relevant configuration file, and then use the converted model to verify it:
> 
> ```
> python distserve/downloader/converter.py \
> --input "/workspace/models/opt-13b/*.bin" \
> --output /workspace/models/distserve/opt-13b \
> --dtype float16 \
> --model opt
> 
> cp *.{json,txt} /workspace/models/distserve/opt-13b
> ```
> 
> and then use：
> 
> ` --model /workspace/models/distserve/opt-13b`

Your comment works well, now I can run it. Thanks for your help!
