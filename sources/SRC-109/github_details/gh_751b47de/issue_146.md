# [Issue #146] Api key - vllm openai

source: https://github.com/triton-inference-server/perf_analyzer/issues/146
state: closed | updated: 2024-11-04T20:03:58Z
labels: 

## 正文

I'm trying to run some performance tests with the following:
genai-perf profile \
  -m meta-llama/Meta-Llama-3.1-70B-Instruct \
  --service-kind openai \
  --backend vllm \
  --endpoint v1/chat/completions \
  --endpoint-type chat \
  --num-prompts 100 \
  --random-seed 123 \
  --synthetic-input-tokens-mean 200 \
  --synthetic-input-tokens-stddev 0 \
  --streaming \
  --output-tokens-mean 100 \
  --output-tokens-stddev 0 \
  --concurrency 1 \
  --measurement-interval 4000 \
  --profile-export-file my_profile_export.json \
  --url 10.10.8.21:8000
Is there a way to pass the api key to the vllm request?
I have the following error: 
Failed to retrieve results from inference request.
Thread [0] had error: OpenAI response returns **HTTP code 400**


Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 200, in run
    args.func(args, extra_args, telemetry_data_collector)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/parser.py", line 875, in profile_handler
    Profiler.run(
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/wrapper.py", line 164, in run
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
  File "/usr/lib/python3.10/subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['perf_analyzer', '-m', 'meta-llama/Meta-Llama-3.1-70B-Instruct', '--async', '--input-data', 'artifacts/meta-llama_Meta-Llama-3.1-70B-Instruct-openai-chat-concurrency1/inputs.json', '-i', 'http', '--concurrency-range', '1', '--endpoint', 'v1/chat/completions', '--service-kind', 'openai', '-u', '10.10.8.21:8000', '--measurement-interval', '4000', '--stability-percentage', '999', '--profile-export-file', 'artifacts/meta-llama_Meta-Llama-3.1-70B-Instruct-openai-chat-concurrency1/my_profile_export.json']' returned non-zero exit status 99.

## 评论 (2)

### zoramt · 2024-10-23

This is important for our use case as well, where the model server is running behind an authentication gateway. It would be great to be able to pass an API key or auth token as HTTP bearer token.

### the-david-oy · 2024-10-24

Thanks for opening a GitHub issue. There is! We have a ticket open to add this documentation soon.

You'd do this by appending the below flags to the end of the command. The -- is for superuser mode to pass arguments directly into Perf Analyzer. The -H is to add headers.

`-- -H "Authorization: Bearer ${OPENAI_API_KEY}" -H "Accept: text/event-stream"`
