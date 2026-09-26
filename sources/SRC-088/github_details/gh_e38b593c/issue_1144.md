# [Issue #1144] [Bug]: Evaluation raise guidellm input format error when setting "chat_template_kwargs":{"enable_thinking":false}

source: https://github.com/vllm-project/speculators/issues/1144
state: closed | updated: 2026-09-21T13:36:17Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM  v0.26.0
- Speculators  0.9.0.dev28  (main)
- PyTorch 2.10.0
- Transformers 5.14.1
- Model  Qwen3.6-35B-A3B （any model occurs）


### 🐛 Describe the bug

When performing evaluation with specific settings, for example, setting "enable_thinking":false. It is hard to get it right. I tried the following, but it failed. It seems that the logic in evaluated.py cannot handle nested dicts. 


The following one run correctly:
```
  python $SCRIPT_DIR/evaluate.py \
      --target http://localhost:9090/v1 throughput \
      --dataset ${DATADIR}/${f}.jsonl \
      --subsets ${f} \
      --data-column-mapper "kind=generative_column_mapper,column_mappings.text_column=prompt" \
      --max-requests 500 \
      --max-concurrency 8 \
      --gen-kwargs '{"temperature":1.0}'
```

The following one incurs errors:
```
  python $SCRIPT_DIR/evaluate.py \
      --target http://localhost:9090/v1 throughput \
      --dataset ${DATADIR}/${f}.jsonl \
      --subsets ${f} \
      --data-column-mapper "kind=generative_column_mapper,column_mappings.text_column=prompt" \
      --max-requests 500 \
      --max-concurrency 8 \
      --gen-kwargs '{"temperature":1.0, "chat_template_kwargs":{"enable_thinking":false}}'

```

Error log:

```
Error: Invalid value for '--backend': missing required key 'kind'.
Expected format: kind=<type>,key=value,... or JSON/YAML object with a 'kind' field
  Valid kinds: openai_http, openai_websocket, vllm_python
Traceback (most recent call last):
  File "/root/speculators/scripts/evaluate/evaluate.py", line 477, in <module>
    main()
  File "/root/speculators/scripts/evaluate/evaluate.py", line 473, in main
    run_benchmark(args)
  File "/root/speculators/scripts/evaluate/evaluate.py", line 346, in run_benchmark
    acceptance_csv, perf_csv, mt = _run_subset(
                                   ^^^^^^^^^^^^
  File "/root/speculators/scripts/evaluate/evaluate.py", line 235, in _run_subset
    run_guidellm(
  File "/root/speculators/scripts/evaluate/perf_utils.py", line 585, in run_guidellm
    subprocess.run(cmd, check=True)  # noqa: S603
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['guidellm', 'run', '--backend', "kind=openai_http,target=http://localhost:9090/v1,max_tokens=4096,extras.body.temperature=1.0,extras.body.max_completion_tokens=256,extras.body.chat_template_kwargs={'enable_thinking': False}", '--data', 'kind=json_file,path=./deepspec_eval_datasets_500_converted/gsm8k.jsonl,load_kwargs.split=train', '--data-column-mapper', 'kind=generative_column_mapper,column_mappings.text_column=prompt', '--profile', 'kind=throughput,max_concurrency=8', '--constraint', 'kind=max_requests,count=500', '--output', 'kind=json,path=_mnt_weight_Qwen3-8B_20260918_151648/artifacts/run_gsm8k.json']' returned non-zero exit status 2.
```

## 评论 (5)

### khushali9 · 2026-09-18

@zhujiem  I'd like to work on this. I've traced it to run_guidellm in scripts/evaluate/perf_utils.py, where --backend is built as a flat comma-separated string, so nested gen_kwargs (e.g. chat_template_kwargs) get stringified via repr and break guidellm's parser. I'd fix it by constructing the backend as a JSON object and passing json.dumps(...), plus a regression test. Could this be assigned to me?

### khushali9 · 2026-09-18

@zhujiem I have kept my fix out, you want to give it a try ?

### zhujiem · 2026-09-19

ok I will test it today. @khushali9 

### zhujiem · 2026-09-19

@khushali9 I had worked out a similar patch using Claude, but you were faster. Your PR works as expected. To improve conciseness, I’ve suggested some minor refinements for conciseness here: https://github.com/khushali9/speculators/pull/1

### khushali9 · 2026-09-19

@zhujiem I have merged your changes. 
