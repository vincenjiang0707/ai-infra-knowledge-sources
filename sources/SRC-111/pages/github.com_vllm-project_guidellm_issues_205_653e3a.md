source: https://github.com/vllm-project/guidellm/issues/205

$ guidellm benchmark --target "http://localhost:11434/v1" --rate-type sweep --max-seconds 30 --model qwen3:4b --data "prompt_tokens=256,output_tokens=128"
Creating backend...
Backend openai_http connected to http://localhost:11434/v1 for model qwen3:4b.
Creating request loader...
Traceback (most recent call last):
File "/home/alex/miniconda3/lib/python3.12/site-packages/transformers/utils/hub.py", line 470, in cached_files
hf_hub_download(
File "/home/alex/miniconda3/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 106, in _inner_fn
validate_repo_id(arg_value)
File "/home/alex/miniconda3/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 160, in validate_repo_id
raise HFValidationError(
huggingface_hub.errors.HFValidationError: Repo id must use alphanumeric chars or '-', '_', '.', '--' and '..' are forbidden, '-' and '.' cannot start or end the name, max length is 96: 'qwen3:4b'.
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/utils/hf_transformers.py", line 21, in check_load_processor
loaded = AutoTokenizer.from_pretrained(
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/transformers/models/auto/tokenization_auto.py", line 950, in from_pretrained
tokenizer_config = get_tokenizer_config(pretrained_model_name_or_path, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/transformers/models/auto/tokenization_auto.py", line 782, in get_tokenizer_config
resolved_config_file = cached_file(
^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/transformers/utils/hub.py", line 312, in cached_file
file = cached_files(path_or_repo_id=path_or_repo_id, filenames=[filename], **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/transformers/utils/hub.py", line 523, in cached_files
_get_cache_file_to_return(path_or_repo_id, filename, cache_dir, revision) for filename in full_filenames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/transformers/utils/hub.py", line 140, in _get_cache_file_to_return
resolved_file = try_to_load_from_cache(path_or_repo_id, full_filename, cache_dir=cache_dir, revision=revision)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 106, in _inner_fn
validate_repo_id(arg_value)
File "/home/alex/miniconda3/lib/python3.12/site-packages/huggingface_hub/utils/_validators.py", line 160, in validate_repo_id
raise HFValidationError(
huggingface_hub.errors.HFValidationError: Repo id must use alphanumeric chars or '-', '_', '.', '--' and '..' are forbidden, '-' and '.' cannot start or end the name, max length is 96: 'qwen3:4b'.
The above exception was the direct cause of the following exception:
Traceback (most recent call last):
File "/home/alex/miniconda3/bin/guidellm", line 8, in <module>
sys.exit(cli())
^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/click/core.py", line 1161, in __call__
return self.main(*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/click/core.py", line 1082, in main
rv = self.invoke(ctx)
^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/click/core.py", line 1697, in invoke
return _process_result(sub_ctx.command.invoke(sub_ctx))
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/click/core.py", line 1443, in invoke
return ctx.invoke(self.callback, **ctx.params)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/click/core.py", line 788, in invoke
return __callback(*args, **kwargs)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/__main__.py", line 255, in benchmark
asyncio.run(
File "/home/alex/miniconda3/lib/python3.12/asyncio/runners.py", line 195, in run
return runner.run(main)
^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/asyncio/runners.py", line 118, in run
return self._loop.run_until_complete(task)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/asyncio/base_events.py", line 691, in run_until_complete
return future.result()
^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/benchmark/entrypoints.py", line 68, in benchmark_generative_text
request_loader = GenerativeRequestLoader(
^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/request/loader.py", line 90, in __init__
dataset, args_column_mappings = load_dataset(
^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/dataset/entrypoints.py", line 33, in load_dataset
return creator.create(
^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/dataset/creator.py", line 94, in create
dataset = cls.handle_create(
^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/dataset/synthetic.py", line 231, in handle_create
processor = check_load_processor(
^^^^^^^^^^^^^^^^^^^^^
File "/home/alex/miniconda3/lib/python3.12/site-packages/guidellm/utils/hf_transformers.py", line 28, in check_load_processor
raise ValueError(
ValueError: Failed to load processor/Tokenizer for Processor/tokenizer required for synthetic dataset generation..
```</div>

Errors due to an invalid processor name are inconstant and not descriptive. This need to be improved.

## Discussed in #203

Originally posted byalexhegitJune 19, 2025Ollama support openai compatilbe api. So I try use guidellm benchmark with ollama but got failed.