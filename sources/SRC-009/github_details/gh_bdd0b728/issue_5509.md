# [Issue #5509] [TRT Executor] Setting stop_words in requests leads to memory leak

source: https://github.com/NVIDIA/TensorRT-LLM/issues/5509
state: closed | updated: 2026-09-20T01:59:40Z
labels: bug, LLM API

## 正文

### System Info

The issue is not platform-specific, but we observed it with a DGX host (H100 GPUs), using multiple TensorRT-LLM versions (`0.20.0rc3` and `0.21.0rc1`) and CUDA `12.8`. The issue appears when using the TRT workflow in TensorRT-LLM with the `Executor` bindings.

### Who can help?

_No response_

### Information

- [ ] The official example scripts
- [x] My own modified scripts

### Tasks

- [x] An officially supported task in the `examples` folder (such as GLUE/SQuAD, ...)
- [ ] My own task or dataset (give details below)

### Reproduction

The issue appears to be model-agnostic and can be reproduced with different model types. In this specific case, we reproduce it using a Llama3 8B engine built as follows:

`trtllm-build --checkpoint_dir ./llama3-8b-trt_chkpt --output_dir ./llama3-8b-engine --gemm_plugin bfloat16 --remove_input_padding enable --gpt_attention_plugin bfloat16  --max_batch_size 256 --use_paged_context_fmha enable`

We then prepared a reproducer script to highlight the issue. This will keep issuing randomly-generated requests to the engine, while tracking the memory usage of the process (in terms of RSS and VMS). The `--stop_words` option allows to enable passing a list of stop words to the `Executor` bindings' `Request`s, which triggers the issue:

```
import argparse, time, random, sys
import psutil
import tensorrt_llm
import tensorrt_llm.bindings.executor as trtllm

from datetime import datetime

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Executor Bindings Example")
    parser.add_argument("--model_path", type=str, required=True, help="Directory containing model engine")
    parser.add_argument("--stop_words", action="store_true", help="Pass stop words list to request")

    args = parser.parse_args()
    exec_conf = trtllm.ExecutorConfig(max_beam_width=1, kv_cache_config=trtllm.KvCacheConfig(enable_block_reuse=True))
    this_process = psutil.Process()
    prompt_length, gen_length = 20, 10
    max_batch_size = 256
    sleep_time_ms = 1
    request_cnt = 0
    active_requests = 0

    stop_words_list = [[100123], [100124], [100125], [100126, 100127]] if args.stop_words else None
    sampling_conf = trtllm.SamplingConfig(top_k=0, top_p=1.0, temperature=20.0)
    output_config = trtllm.OutputConfig(
        return_log_probs=False,
        exclude_input_from_output=False,
        return_context_logits=False,
        return_generation_logits=False,
        additional_model_outputs=None,
    )

    with trtllm.Executor(args.model_path, trtllm.ModelType.DECODER_ONLY, exec_conf) as executor:
        if executor.can_enqueue_requests():
            print(f"TensorRT-LLM version : {tensorrt_llm.__version__}")
            while True:
                # Awaiting any available responses
                if executor.get_num_responses_ready() > 0:
                    responses = executor.await_responses()
                    request_cnt += len(responses)
                    active_requests -= len(responses)
                    print(f"Requests so far = {request_cnt}, received = {len(responses)}, active = {active_requests}.")
                    mem_info = this_process.memory_info()
                    print(f"[{datetime.now()}] RSS = {mem_info.rss / 1024 ** 2}, VMS = {mem_info.vms / 1024 ** 2}.")
                    sys.stdout.flush()

                requests_to_submit = max_batch_size - active_requests
                for _ in range(0, requests_to_submit):
                    request = trtllm.Request(
                        input_token_ids=[random.randint(0, 60000) for _ in range(prompt_length)],
                        max_tokens=gen_length,
                        sampling_config=sampling_conf,
                        output_config=output_config,
                        stop_words=stop_words_list,
                        end_id=None,
                    )

                    request_id = executor.enqueue_request(request)
                    active_requests += 1

                # Sleep before issuing new requests
                time.sleep(sleep_time_ms / 1000)
``` 

### Expected behavior

We expect the `Executor` instance to stabilize around a certain memory usage (in this case, CPU memory) in all scenarios.

### actual behavior

Setting the `--stop_words` flag (thus passing a list of stop words to each `Executor` request) leads to what effectively appears to be a memory leak: the monitored RSS of the process keeps increasing over time, with a rate of ~0.6GB per hour. We confirmed the same behavior in more complex production scenarios, as well as over a range of TRT-LLM versions.

### additional notes

Simply allocating `Request` objects repeatedly (with stop words set) is not enough to trigger the memory leak, and they need to be passed to the `Executor` instance - this indicates that the issue most likely lies deeper in the runtime.

## 评论 (2)

### karljang · 2026-08-20

Sorry we never replied to this one. Closing as stale since the TensorRT engine-build path is deprecated in favor of the PyTorch backend. Please open a new issue if the problem persists in the latest version.


### austingg · 2026-09-20

Pytorch backend also has memory leak 
