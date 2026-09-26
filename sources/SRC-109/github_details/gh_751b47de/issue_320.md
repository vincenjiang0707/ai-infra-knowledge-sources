# [Issue #320] "Failed to retrieve results from inference request." with high concurrency

source: https://github.com/triton-inference-server/perf_analyzer/issues/320
state: closed | updated: 2025-03-12T08:32:04Z
labels: 

## 正文

I am using version **0.0.11** of `genai-perf` to benchmark a locally deployed vllm inference service. Everything works fine when I set `--concurrency` to a low value, but when I increase it to 64 or higher, the logs show `Failed to retrieve results from inference request.`, and the process hangs for ever, requiring `Ctrl+C` to exit. The logs is shown below:

```bash
$ genai-perf profile   -m deepseek   --tokenizer /t9k/mnt/DeepSeek-R1-Distill-Qwen-7B   --service-kind openai   --endpoint-type chat   --url http://xxx   --endpoint v1/chat/completions   --streaming   --synthetic-input-tokens-mean 128   --synthetic-input-tokens-stddev 0   --output-tokens-mean 128   --output-tokens-stddev 0   --concurrency 128   --measurement-interval 20000   --generate-plots
2025-03-06 13:59 [INFO] genai_perf.parser:112 - Profiling these models: deepseek
2025-03-06 13:59 [INFO] genai_perf.subcommand.common:225 - Running Perf Analyzer : 'perf_analyzer -m deepseek --async --input-data artifacts/deepseek-openai-chat-concurrency128/inputs.json -i http --concurrency-range 128 --endpoint v1/chat/completions --service-kind openai -u http://xxx --request-count 0 --warmup-request-count 0 --profile-export-file artifacts/deepseek-openai-chat-concurrency128/profile_export.json --measurement-interval 20000 --stability-percentage 999'
Failed to retrieve results from inference request.
^CTraceback (most recent call last):
  File "/t9k/mnt/.local/bin/genai-perf", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/t9k/mnt/.local/lib/python3.11/site-packages/genai_perf/main.py", line 54, in main
    run()
  File "/t9k/mnt/.local/lib/python3.11/site-packages/genai_perf/main.py", line 47, in run
    args.func(args, extra_args)
  File "/t9k/mnt/.local/lib/python3.11/site-packages/genai_perf/subcommand/profile.py", line 64, in profile_handler
    run_perf_analyzer(
  File "/t9k/mnt/.local/lib/python3.11/site-packages/genai_perf/subcommand/common.py", line 230, in run_perf_analyzer
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)  # nosec
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/lib/python3.11/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/lib/python3.11/subprocess.py", line 1201, in communicate
    self.wait()
  File "/opt/conda/lib/python3.11/subprocess.py", line 1264, in wait
    return self._wait(timeout=timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/conda/lib/python3.11/subprocess.py", line 2053, in _wait
    (pid, sts) = self._try_wait(0)
                 ^^^^^^^^^^^^^^^^^
  File "/opt/conda/lib/python3.11/subprocess.py", line 2011, in _try_wait
    (pid, sts) = os.waitpid(self.pid, wait_flags)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
```

I checked the logs of the vllm service, and there are no error messages:

```
INFO:     10.233.66.164:0 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 03-05 23:33:05 async_llm.py:159] Added request chatcmpl-6a2e591b-e842-41b9-8269-46672ef25479.
INFO 03-05 23:33:05 logger.py:37] Received request chatcmpl-b977dd67-98a1-4c09-b547-685cd1e6e165: prompt: '<｜begin▁of▁sentence｜><｜User｜> fear\n To cope malicious censurers, which ever,\n As ravenous fishes, do a vessel follow\n That is new-trimmed, but benefit no further\n Than vainly longing. What we oft do best,\n By sick interpreters, once weak ones, is\n Not ours or not allowed; what worst, as oft,\n Hitting a grosser quality, is cried up\n For our best act. If we shall stand still\n In fear our motion will be mocked or carped at,\n We should take root here where we sit,\n Or sit state-statues only.\n \n KING.\n Things done well,\n And with a<｜Assistant｜>', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO:     10.233.66.164:0 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 03-05 23:33:05 async_llm.py:159] Added request chatcmpl-b977dd67-98a1-4c09-b547-685cd1e6e165.
INFO 03-05 23:33:05 logger.py:37] Received request chatcmpl-54ce492b-22a7-4fb2-8ceb-f05ce84c46bb: prompt: '<｜begin▁of▁sentence｜><｜User｜>, cried to those that fled\n ‘Our Britain’s harts die flying, not our men.\n To darkness fleet souls that fly backwards! Stand;\n Or we are Romans and will give you that,\n Like beasts, which you shun beastly, and may save\n But to look back in frown. Stand, stand!’ These three,\n Three thousand confident, in act as many—\n For three performers are the file when all\n The rest do nothing—with this word ‘Stand, stand!’\n Accommodated by the place, more charming\n With their own nobleness, which could have turn’d\n A distaff to a<｜Assistant｜>', params: SamplingParams(n=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, min_p=0.0, seed=None, stop=[], stop_token_ids=[], bad_words=[], include_stop_str_in_output=False, ignore_eos=False, max_tokens=128, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, truncate_prompt_tokens=None, guided_decoding=None), prompt_token_ids: None, lora_request: None, prompt_adapter_request: None.
INFO:     10.233.66.164:0 - "POST /v1/chat/completions HTTP/1.1" 200 OK
INFO 03-05 23:33:05 async_llm.py:159] Added request chatcmpl-54ce492b-22a7-4fb2-8ceb-f05ce84c46bb.
INFO 03-05 23:33:10 loggers.py:69] Avg prompt throughput: 156.5 tokens/s, Avg generation throughput: 1455.8 tokens/s, Running: 0 reqs, Waiting: 0 reqs GPU KV cache usage: 0.0%.
INFO 03-05 23:33:15 loggers.py:69] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs GPU KV cache usage: 0.0%.
INFO 03-05 23:33:20 loggers.py:69] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs GPU KV cache usage: 0.0%.
INFO 03-05 23:33:25 loggers.py:69] Avg prompt throughput: 0.0 tokens/s, Avg generation throughput: 0.0 tokens/s, Running: 0 reqs, Waiting: 0 reqs GPU KV cache usage: 0.0%.
```

Could you please help identify the issue?

Best regards.

## 评论 (3)

### nv-hwoo · 2025-03-06

Could you try running with verbose mode 
```
genai-perf profile ... -v
```
Or/and with super verbose mode
```
genai-perf profile ... -v -- -v -v
```
to see more logs?

### xyxxxxx · 2025-03-07

Thanks for your reply!

Running with verbose mode:

```bash
$ genai-perf profile   -m deepseek   --tokenizer /t9k/mnt/DeepSeek-R1-Distill-Qwen-7B   --service-kind openai   --endpoint-type chat   --url http://app-vllm-fc8b3065.dev-xyx.nc201.ksvc.tensorstack.net   --endpoint v1/chat/completions   --streaming   --synthetic-input-tokens-mean 128   --synthetic-input-tokens-stddev 0   --output-tokens-mean 128   --output-tokens-stddev 0   --concurrency 128   --measurement-interval 20000   --generate-plots -v
2025-03-07 11:00 [INFO] genai_perf.parser:112 - Profiling these models: deepseek
2025-03-07 11:00 [INFO] genai_perf.subcommand.common:225 - Running Perf Analyzer : 'perf_analyzer -m deepseek --async --input-data artifacts/deepseek-openai-chat-concurrency128/inputs.json -i http --concurrency-range 128 --endpoint v1/chat/completions --service-kind openai -u http://app-vllm-fc8b3065.dev-xyx.nc201.ksvc.tensorstack.net --request-count 0 --warmup-request-count 0 --verbose --profile-export-file artifacts/deepseek-openai-chat-concurrency128/profile_export.json --measurement-interval 20000 --stability-percentage 999'
 Successfully read data for 1 stream/streams with 100 step/steps.
*** Measurement Settings ***
  Service Kind: OPENAI
  Using "time_windows" mode for stabilization
  Stabilizing using average throughput
  Measurement window: 20000 msec
  Using asynchronous calls for inference

Request concurrency: 128
Failed to retrieve results from inference request.
^CInterrupt signal (2) received.
Exiting immediately...
Traceback (most recent call last):
......
```

with super verbose mode:

[log.txt](https://github.com/user-attachments/files/19119472/log.txt)

### xyxxxxx · 2025-03-12

I finally found the cause of this issue at https://github.com/vllm-project/vllm/issues/2484. It was neither a problem with the service nor the CLI, but a proxy server in between, which had a 60-second timeout setting.

So close this issue.
