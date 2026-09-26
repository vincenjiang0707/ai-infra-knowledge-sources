# [Issue #1590] CNNDM download script is broken for python 3.10+

source: https://github.com/mlcommons/inference/issues/1590
state: closed | updated: 2026-05-08T00:40:48Z
labels: Stale

## 正文

CNNDM download script fails if we use python 3.10 but works fine for python3.9. The exact error is added below.
```
$ cm run script --tags=get,dataset,cnndm,_calibration -j
* cm run script "get dataset cnndm _calibration"
  * cm run script "get sys-utils-cm"
  * cm run script "get python3"
      - More than 1 cached script output found for "get,python3":

        0) /home/arjun/CM/repos/local/cache/47e468d62f934cfc (get,python3,python,get-python,get-python3,script-artifact-d0b5dd74373f4a62,version-3.10.12,non-virtual) (Version 3.10.12)
        1) /home/arjun/CM/repos/local/cache/b7ed227bf39747c9 (get,python3,python,get-python,get-python3,script-artifact-d0b5dd74373f4a62,version-3.8.0,non-virtual) (Version 3.8.0)
        2) /home/arjun/CM/repos/local/cache/b9077d04fbdb4323 (get,python3,python,get-python,get-python3,script-artifact-d0b5dd74373f4a62,version-3.9.12,non-virtual) (Version 3.9.12)

        Make your selection or press Enter for 0 or use -1 to skip:

        Selected 0: /home/arjun/CM/repos/local/cache/47e468d62f934cfc
  * cm run script "mlperf inference source"
  * cm run script "get generic-python-lib _package.simplejson"
  * cm run script "get generic-python-lib _datasets"
  * cm run script "get generic-python-lib _package.tokenizers"
  * cm run script "get generic-python-lib _numpy"
Using MLCommons Inference source from '/home/arjun/CM/repos/local/cache/b8f775cf8d554c5f/inference'
/usr/bin/python3 prepare-calibration.py --calibration-list-file calibration-list.txt --output-dir /home/arjun/CM/repos/local/cache/4ceead8552d044c0/install
Downloading and preparing dataset None/1.0.0 to /home/arjun/.cache/huggingface/datasets/parquet/1.0.0-3e4b881106bdbe0d/0.0.0/14a00e99c0d15a23649d0db8944380ac81082d4b021f398733dd84f3a6c569a7...
Downloading data files: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 10547.29it/s]
Extracting data files: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:00<00:00, 1603.33it/s]
Traceback (most recent call last):
  File "/home/arjun/CM/repos/local/cache/b8f775cf8d554c5f/inference/language/gpt-j/prepare-calibration.py", line 59, in <module>
    main()
  File "/home/arjun/CM/repos/local/cache/b8f775cf8d554c5f/inference/language/gpt-j/prepare-calibration.py", line 56, in main
    prepare_calibration_data(args.calibration_list_file, args.output_dir)
  File "/home/arjun/CM/repos/local/cache/b8f775cf8d554c5f/inference/language/gpt-j/prepare-calibration.py", line 28, in prepare_calibration_data
    dataset = load_dataset("cnn_dailymail", name="3.0.0", split='train')
  File "/home/arjun/.local/lib/python3.10/site-packages/datasets/load.py", line 1797, in load_dataset
    builder_instance.download_and_prepare(
  File "/home/arjun/.local/lib/python3.10/site-packages/datasets/builder.py", line 909, in download_and_prepare
    self._download_and_prepare(
  File "/home/arjun/.local/lib/python3.10/site-packages/datasets/builder.py", line 1022, in _download_and_prepare
    verify_splits(self.info.splits, split_dict)
  File "/home/arjun/.local/lib/python3.10/site-packages/datasets/utils/info_utils.py", line 100, in verify_splits
    raise NonMatchingSplitsSizesError(str(bad_splits))
datasets.utils.info_utils.NonMatchingSplitsSizesError: [{'expected': SplitInfo(name='train', num_bytes=1261703785, num_examples=287113, shard_lengths=None, dataset_name=None), 'recorded': SplitInfo(name='train', num_bytes=3785111355, num_examples=861339, shard_lengths=[115705, 115704, 115704, 115705, 121408, 115705, 115704, 45704], dataset_name='parquet')}, {'expected': SplitInfo(name='validation', num_bytes=57732412, num_examples=13368, shard_lengths=None, dataset_name=None), 'recorded': SplitInfo(name='validation', num_bytes=173197236, num_examples=40104, shard_lengths=None, dataset_name='parquet')}, {'expected': SplitInfo(name='test', num_bytes=49925732, num_examples=11490, shard_lengths=None, dataset_name=None), 'recorded': SplitInfo(name='test', num_bytes=149777196, num_examples=34470, shard_lengths=None, dataset_name='parquet')}]
```

## 评论 (1)

### github-actions[bot] · 2026-05-08

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
