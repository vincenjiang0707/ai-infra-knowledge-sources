# [Issue #1143] [Bug]: Evaluation raise AttributeError: 'DatasetDict' object has no attribute 'info'

source: https://github.com/vllm-project/speculators/issues/1143
state: closed | updated: 2026-09-19T02:06:53Z
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

An error occurs when performing evaluation on a single gsm8k dataset jsonl. The error shows `AttributeError: 'DatasetDict' object has no attribute 'info'`. The error occurs in the guidellm package `/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/preprocessors/mappers.py` since load_dataset from json_file should specify the dataset split to get dataset.info or else a DatasetDict returns.

```bash
#!/bin/bash
export PYTHONPATH=/root/speculators/src:${PYTHONPATH}
DATADIR=./deepspec_eval_datasets_500_converted
SCRIPT_DIR=/root/speculators/scripts/evaluate

for f in gsm8k humaneval; do
  python $SCRIPT_DIR/evaluate.py \
      --target http://localhost:9090/v1 throughput \
      --dataset ${DATADIR}/gsm8k.jsonl \
      --subsets ${f} \
      --data-column-mapper "kind=generative_column_mapper,column_mappings.text_column=prompt" \
      --max-requests 500
done
```


Error log:

```log
✔ OpenAIHTTPBackend backend validated with model /mnt/weight/Qwen3.6-35B-A3B
  {'kind': 'openai_http', 'target': 'http://localhost:9090', 'model': '/mnt/weight/Qwen3.6-35B-A3B', 'request_format': '/v1/chat/completions', 'api_key': None, 'api_routes': {'/health':  
  'health', '/v1/models': 'v1/models', '/v1/completions': 'v1/completions', '/v1/chat/completions': 'v1/chat/completions', '/v1/embeddings': 'v1/embeddings', '/v1/responses':             
  'v1/responses', '/v1/audio/transcriptions': 'v1/audio/transcriptions', '/v1/audio/translations': 'v1/audio/translations', '/pooling': 'pooling'}, 'timeout': None, 'timeout_connect':    
  5.0, 'http2': True, 'follow_redirects': True, 'verify': False, 'validate_backend': True, 'stream': True, 'extras': {'method': None, 'stream': None, 'headers': None, 'params': None,     
  'body': {'temperature': 1.0, 'max_completion_tokens': 256}, 'files': None, 'content': None}, 'max_tokens': 4096, 'server_history': False, 'tool_call_missing_behavior': 'error_stop',    
  'multiturn_reasoning': False}                                                                                                                                                            
✔ Tokenizer resolved, using model '/mnt/weight/Qwen3.6-35B-A3B' as tokenizer
  {'kind': 'huggingface_auto', 'model': '/mnt/weight/Qwen3.6-35B-A3B', 'load_kwargs': {}}                                                                                                  
/usr/local/python3.12.13/lib/python3.12/importlib/__init__.py:90: UserWarning: A NumPy version >=1.22.4 and <2.3.0 is required for this version of SciPy (detected version 2.4.6)
  return _bootstrap._gcd_import(name[level:], package, level)
Generating train split: 500 examples [00:00, 171419.98 examples/s]
✔ 1 datasets resolved
  [{'kind': 'json_file', 'load_kwargs': {}, 'path': 'deepspec_eval_datasets_500_converted/gsm8k.jsonl'}]                                                                                   
✔ 2 preprocessors resolved
  [{'kind': 'generative_column_mapper', 'column_mappings': {'text_column': 'prompt'}}, {'kind': 'encode_media', 'audio_kwargs': {}, 'image_kwargs': {}, 'video_kwargs': {}}]               
✔ Finalizer resolved
  {'kind': 'generative', 'tool_call_mode': 'client'}                                                                                                                                       
Traceback (most recent call last):
  File "/usr/local/python3.12.13/bin/guidellm", line 6, in <module>
    sys.exit(cli())
             ^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/click/core.py", line 1569, in __call__
    return self.main(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/click/core.py", line 1490, in main
    rv = self.invoke(ctx)
         ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/click/core.py", line 1970, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/click/core.py", line 1353, in invoke
    return ctx.invoke(self.callback, **ctx.params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/click/core.py", line 907, in invoke
    return callback(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/utils/click_pydantic.py", line 387, in wrapper
    return func(**kw)
           ^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/cli/run.py", line 149, in run
    asyncio.run(
  File "/usr/local/python3.12.13/lib/python3.12/asyncio/runners.py", line 195, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/benchmark/entrypoints.py", line 492, in benchmark_generative_text
    request_loader: DataLoader[GenerationRequest] = await create_data_loader(
                                                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/entrypoints.py", line 122, in create_data_loader
    data_loader = DataLoaderRegistry.create(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/loaders/loader.py", line 56, in create
    return data_loader_cls(
           ^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/loaders/torch.py", line 175, in __init__
    iterator: DatasetsIterator[DataT] = DatasetsIterator(
                                        ^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/loaders/torch.py", line 68, in __init__
    preprocessor.setup_data(
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/preprocessors/mappers.py", line 265, in setup_data
    self.datasets_column_mappings = self.datasets_mappings(
                                    ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.12.13/lib/python3.12/site-packages/guidellm/data/preprocessors/mappers.py", line 193, in datasets_mappings
    if dataset.info and dataset.info.dataset_name
       ^^^^^^^^^^^^
AttributeError: 'DatasetDict' object has no attribute 'info'
[ERROR] 2026-09-18-12:44:16 (PID:12636, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
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
subprocess.CalledProcessError: Command '['guidellm', 'run', '--backend', 'kind=openai_http,target=http://localhost:9090/v1,max_tokens=4096,extras.body.temperature=1.0,extras.body.max_completion_tokens=256', '--data', 'kind=json_file,path=./deepspec_eval_datasets_500_converted/gsm8k.jsonl', '--data-column-mapper', 'kind=generative_column_mapper,column_mappings.text_column=prompt', '--profile', 'kind=throughput,max_concurrency=8', '--constraint', 'kind=max_requests,count=500', '--output', 'kind=json,path=_mnt_weight_Qwen3.6-35B-A3B_20260918_124343/artifacts/run_gsm8k.json']' returned non-zero exit status 1.
[ERROR] 2026-09-18-12:44:18 (PID:12620, Device:-1, RankID:-1) ERR99999 UNKNOWN applicaiton exception
```

## 评论 (1)

### RainieLLM · 2026-09-19

Opened [#1150](https://github.com/vllm-project/speculators/pull/1150) to fix this.

Local JSON/JSONL data was missing an explicit split, so GuideLLM could return a `DatasetDict`. The PR selects `train` and adds regression tests, theHugging Face path is unchanged.

Thanks for point this out!

