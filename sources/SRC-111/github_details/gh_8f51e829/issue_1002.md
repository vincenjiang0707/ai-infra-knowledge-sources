# [Issue #1002] Bug: AttributeError when using JSON/CSV/Parquet file datasets

source: https://github.com/vllm-project/guidellm/issues/1002
state: closed | updated: 2026-08-10T17:35:35Z
labels: 

## 正文

## Issue Description

When running `guidellm run` with a `json_file`, `csv_file`, or `parquet_file` data source, the benchmark fails with:

```
Traceback (most recent call last):
  File ".../guidellm/data/preprocessors/mappers.py", line 192, in datasets_mappings
    if dataset.info and dataset.info.dataset_name
       ^^^^^^^^^^^^
AttributeError: 'DatasetDict' object has no attribute 'info'
```

## Root Cause

The file-based dataset deserializers (`JSONFileDatasetDeserializer`, `CSVFileDatasetDeserializer`, `ParquetFileDatasetDeserializer`) in `.venv/lib/python3.12/site-packages/guidellm/data/deserializers/file.py` are calling `load_dataset()` directly, which returns a `DatasetDict` object for these file types.

However:
1. The type annotations specify `-> Dataset` as the return type
2. Downstream code in `guidellm/data/preprocessors/mappers.py:192` expects a `Dataset` with an `.info` attribute
3. `DatasetDict` is dict-like and doesn't have an `.info` attribute - individual splits like `DatasetDict['train']` do

## Expected Behavior

The benchmark should complete successfully, processing the dataset file correctly.

## Actual Behavior

The benchmark fails during dataset preprocessing initialization with `AttributeError: 'DatasetDict' object has no attribute 'info'`.

## Fix

Modified the three deserializers to extract the 'train' split from the `DatasetDict` when it's returned:

1. Added `DatasetDict` to imports: `from datasets import Dataset, DatasetDict, load_dataset`
2. Changed each deserializer to check if the result is a `DatasetDict` and extract the train split:
   ```python
   dataset = load_dataset("json", data_files=str(path), **config.load_kwargs)
   if isinstance(dataset, DatasetDict):
       dataset = dataset["train"]
   return dataset
   ```

This ensures the deserializers return a `Dataset` object as typed, matching the behavior of other deserializers like `TextFileDatasetDeserializer`.

I've prepared a patch file which got it working on my machine: [guidellm_fix.patch](https://github.com/user-attachments/files/30828792/guidellm_fix.patch)

Maybe I find the time to open a PR, but currently I don't thinks so. Sorry 😬

## 评论 (1)

### Pragadeesh122 · 2026-08-08

Thanks for the detailed root-cause analysis @Basster  — picking this up. I've extended the fix to also cover the `arrow_file` and `tar_file` deserializers, which hit the same `DatasetDict` issue via the same `load_dataset` path. PR incoming.
