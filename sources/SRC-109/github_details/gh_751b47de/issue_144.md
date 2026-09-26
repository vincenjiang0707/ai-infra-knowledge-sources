# [Issue #144] error: Failed to init manager inputs: Input data file is malformed

source: https://github.com/triton-inference-server/perf_analyzer/issues/144
state: closed | updated: 2024-11-07T18:10:07Z
labels: bug

## 正文

when i run cmd below, there is an " Input data file is malformed" Error
genai-perf profile \
	-m ensemble \
	--service-kind triton \
	--backend tensorrtllm \
	--num-prompts 1 \
	--random-seed 123 \
	--synthetic-input-tokens-mean 200 \
	--synthetic-input-tokens-stddev 0 \
	--streaming \
	--output-tokens-mean 50 \
	--output-tokens-stddev 0 \
	--output-tokens-mean-deterministic \
	--tokenizer ~/Model/llama-tokenizer \
	--concurrency 1 \
	--measurement-interval 2000 \
	--profile-export-file qwen2_7b_export.json \
	--url localhost:8001

the input data is below
root@iv-ydge5uwdtsxjd1ti241r:~/artifacts/ensemble-triton-tensorrtllm-concurrency1# cat inputs.json 
{
  "data": [
    {
      "model": "ensemble",
      "text_input": "hi hi hi have been a uniform sacrifice of inclination to the\nspirit of criticism, the constancy of your support was\nconviction that the step is compatible with both.\nfeelings do not permit me to suspend the deep\nadminister the executive government of the United\ntender of service which silence in my situation might\namong the number of those out of whom a choice is to be made.\nadmonishes me more and more that the shade of\npublic voice, that I should now apprise you of the\nconfidence with which it has supported me; and for\nthe best exertions of which a very fallible judgment\nto be your desire. I constantly hoped that it would\npenetrated with this idea, I shall carry it with me to\nIf benefits have resulted to our country from these\narrived when your thoughts must be employed in\nthe preparation of an address to declare it to ",
      "max_tokens": [
        50
      ],
      "stream": [
        true
      ],
      "min_length": [
        50
      ]
    }
  ]
}

error information here
Traceback (most recent call last):_
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 214, in main
    run()
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/main.py", line 205, in run
    args.func(args, extra_args, telemetry_data_collector)
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/parser.py", line 915, in profile_handler
    Profiler.run(
  File "/usr/local/lib/python3.10/dist-packages/genai_perf/wrapper.py", line 167, in run
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
  File "/usr/lib/python3.10/subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['perf_analyzer', '-m', 'ensemble', '--async', '--input-data', 'artifacts/ensemble-triton-tensorrtllm-concurrency1/inputs.json', '-i', 'grpc', '--streaming', '--shape', 'max_tokens:1', '--shape', 'text_input:1', '--concurrency-range', '1', '--service-kind', 'triton', '-u', 'localhost:8001', '--measurement-interval', '2000', '--stability-percentage', '999', '--profile-export-file', 'artifacts/ensemble-triton-tensorrtllm-concurrency1/profile_export.json']' returned non-zero exit status 99.
2024-10-18 09:48 [ERROR] genai_perf.main:218 - Command '['perf_analyzer', '-m', 'ensemble', '--async', '--input-data', 'artifacts/ensemble-triton-tensorrtllm-concurrency1/inputs.json', '-i', 'grpc', '--streaming', '--shape', 'max_tokens:1', '--shape', 'text_input:1', '--concurrency-range', '1', '--service-kind', 'triton', '-u', 'localhost:8001', '--measurement-interval', '2000', '--stability-percentage', '999', '--profile-export-file', 'artifacts/ensemble-triton-tensorrtllm-concurrency1/profile_export.json']' returned non-zero exit status 99.



## 评论 (1)

### the-david-oy · 2024-11-05

Thanks for submitting this issue!

Can you try running GenAI-Perf [off the main branch](https://github.com/triton-inference-server/perf_analyzer/blob/main/genai-perf/README.md#install-genai-perf-from-source)? A bug was released into the code around 24.09-24.10. It was fixed [here](https://github.com/triton-inference-server/perf_analyzer/pull/151).
