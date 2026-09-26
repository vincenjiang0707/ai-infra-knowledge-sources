# [Issue #205] Improve error handling around invalid tokenizer names

source: https://github.com/vllm-project/guidellm/issues/205
state: open | updated: 2026-07-01T17:07:08Z
labels: internal, needs followup, cli

## 正文

Errors due to an invalid processor name are inconstant and not descriptive. This need to be improved.

### Discussed in https://github.com/neuralmagic/guidellm/discussions/203

<div type='discussions-op-text'>

<sup>Originally posted by **alexhegit** June 19, 2025</sup>
Ollama support openai compatilbe api. So I try use guidellm benchmark with ollama but got failed.


```shell
$ guidellm benchmark   --target "http://localhost:11434/v1"   --rate-type sweep   --max-seconds 30   --model qwen3:4b --data "prompt_tokens=256,output_tokens=128"
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

## 评论 (5)

### mmarriot · 2025-08-03

Hi @sjmonson, thanks for opening this and flagging the issue!

I’d be happy to take this on. My proposed plan is:

1. **Pre-validate processor names** against the allowed pattern (alphanumeric, `-`, `_`, or `.`, no leading/trailing punctuation) before invoking Hugging Face.  
2. **Catch `HFValidationError`** in `utils/hf_transformers.py` (or at the CLI layer) and re-raise a clear, user-friendly `ValueError`, for example:  
   > **Error:** Invalid processor name `qwen3:4b`. Names may only contain letters, numbers, `-`, `_`, or `.`, and cannot start or end with `-` or `.`.  
3. **Add unit tests** covering both valid and invalid names to ensure the new validation works and prevents regressions.  
4. **Update the documentation** (README or relevant docs) to clearly call out the naming rules for processor/model IDs.

If there’s any preferred wording for the error message or other edge cases I should consider, please let me know. Otherwise, I’ll get started on a PR soon!


### markurtz · 2025-09-18

Hi @MaxMarriottClarke, this sounds reasonable. One note is there is a large refactor in progress currently for 0.4. I can point you to those if you'd like to contribute on top of it


### dbutenhof · 2026-01-22

This has been idle for a long time. I decided to investigate as a way to get my feet slightly damp in GuideLLM code without getting too deep.

So, a few observations -- and these are with respect to the current main branch (basically v0.5.2) rather than the original (presumably 0.3) used to generate the behavior described in this issue. I'm not going to pretend I know anything about how v0.3 was supposed to work.

1. GuideLLM doesn't appear to do anything to validate the `--model` value. In fact, if I specify the total nonsense token `--model '..:æ→'`, GuideLLM is completely happy, even though the OpenAI API server returns a 404 which GuideLLM logs (albeit only at DEBUG level) and otherwise completely ignores. Furthermore, GuideLLM clearly does know how to query the inference server to correctly default the model when not specified (the first value returned by `/v1/models`). So it seems we should likely validate that the specified model is supported, and fail early. (This would be one way to interpret a resolution for issue #205, since the text does focus on the model name.)
2. At least for v0.5.2, what actually happens in this command is that dataset *args* are being deserialized as a dataset (`--data`). The error is `"Error: Invalid value: Data deserialization failed, likely because the input doesn't match any of the input formats. See the 15 error(s) that occurred while attempting to deserialize the data prompt_tokens=256,output_tokens=128:"`... followed by a list of specific messages from each deserializer, one of which is the huggingface message `"Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'prompt_tokens=256,output_tokens=128'"`. 
3. A smaller issue here is that the error message is being obscured by a massive traceback. This is because the deserializers trigger inside the `run` method rather than during Click option decoding, and the resulting `ValueError` propagates through Click as an unexpected exception.

As an excuse for a first "very low key" GuideLLM PR, I'm going to just catch that `ValueError` and raise the proper `click.BadParameter` to avoid the traceback: which won't really change anything, but will make the failure look a bit neater. I think I could see several follow-on issues, which we might consider:

- Validate the `--model` token against `/v1/models` to be sure the server supports it, and issue a parameter validation error if not;
- As a failsafe, (even if the model is validated up front), I would think that a 404 error from the OpenAI inference call ought to trigger a GuideLLM failure rather than simply continuing to make non-operative calls through the programmed sweep or other sequence, because the data's not going to be very useful and the summary doesn't clearly expose the problem.
- @jaredoconnell mentioned some discussion earlier about some new command syntax to avoid the blind search (and ensuing ambiguity) of 15 separate deserializers for the dataset, like `--data-type huggingface` or even standardizing `--data hf:<name>` as I've seen in some examples (vs `--data json:<file>`, etc.)

### jaredoconnell · 2026-06-09

Testing with the latest command format:
`guidellm benchmark   --target "http://localhost:8000"   --profile kind=synchronous   --max-seconds 30   --model qwen3:4b --data "kind=synthetic_text,prompt_tokens=256,output_tokens=128"`

I got the same error, with contained these lines:
`
huggingface_hub.errors.HFValidationError: Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'qwen3:4b'.
`
and
`
OSError: Repo id must use alphanumeric chars, '-', '_' or '.'. The name cannot start or end with '-' or '.' and the maximum length is 96: 'qwen3:4b'.
`

Do we wish to pre-validate the input, or do we wish to remove the stacktrace from the error? Because the error itself is pretty clear.

### dbutenhof · 2026-06-09

> Do we wish to pre-validate the input, or do we wish to remove the stacktrace from the error? Because the error itself is pretty clear.

I'd love to drop the stack traces on straightforward CLI syntax errors like this--there's some concern in practice that we may have validation errors after we get to the benchmarker rather than only in the "setup" part of `benchmark_generative_text`... as well as that even in "the setup phase" we might have a "validation error" that's not so simple to interpret. (See #550.) So the important question is exactly how we scope a solution.
