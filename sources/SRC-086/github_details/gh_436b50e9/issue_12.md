# [Issue #12] train_vicuna_7b.sh script does not install dataset from git-lfs

source: https://github.com/FasterDecoding/Medusa/issues/12
state: closed | updated: 2023-09-14T14:39:50Z
labels: 

## 正文

# Issue
The `train_vicuna_7b.sh` currently fails, as when it clones the `ShareGPT_Vicuna_unfiltered` dataset, it does not download the data `ShareGPT_V4.3_unfiltered_cleaned_split.json` from `git-lfs` by default. This should either be fixed or documented in the README.

# Workaround

```
cd ShareGPT_Vicuna_unfiltered/
git lfs pull
```

# Full log

```
Downloading (…)l-00001-of-00002.bin: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 9.98G/9.98G [05:25<00:00, 30.6MB/s]
Downloading (…)l-00002-of-00002.bin: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████| 3.50G/3.50G [01:55<00:00, 30.4MB/s]
Downloading shards: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [07:21<00:00, 220.67s/it]
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:05<00:00,  2.99s/it]
Downloading (…)neration_config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 132/132 [00:00<00:00, 525kB/s]
Downloading (…)okenizer_config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 727/727 [00:00<00:00, 3.14MB/s]
Downloading tokenizer.model: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 500k/500k [00:00<00:00, 36.5MB/s]
Downloading (…)cial_tokens_map.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 435/435 [00:00<00:00, 1.64MB/s]
You are using the default legacy behaviour of the <class 'transformers.models.llama.tokenization_llama.LlamaTokenizer'>. If you see this, DO NOT PANIC! This is expected, and simply means that the `legacy` (previous) behavior will be used so nothing changes for you. If you want to use the new behaviour, set `legacy=False`. This should only be set if you understand what it means, and thouroughly read the reason why this was added as explained in https://github.com/huggingface/transformers/pull/24565
Loading data...
Traceback (most recent call last):
  File "/home/guberti/Medusa/medusa/train/train.py", line 402, in <module>
    train()
  File "/home/guberti/Medusa/medusa/train/train.py", line 363, in train
    data_module = make_supervised_data_module(tokenizer=tokenizer, data_args=data_args)
  File "/home/guberti/Medusa/medusa/train/train.py", line 288, in make_supervised_data_module
    train_json = json.load(open(data_args.data_path, "r"))
  File "/usr/lib/python3.10/json/__init__.py", line 293, in load
    return loads(fp.read(),
  File "/usr/lib/python3.10/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.10/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.10/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
[2023-09-13 15:49:40,518] torch.distributed.elastic.multiprocessing.api: [ERROR] failed (exitcode: 1) local_rank: 0 (pid: 147902) of binary: /usr/bin/python3
Traceback (most recent call last):
  File "/home/guberti/.local/bin/torchrun", line 33, in <module>
    sys.exit(load_entry_point('torch==2.2.0.dev20230907+cu121', 'console_scripts', 'torchrun')())
  File "/home/guberti/.local/lib/python3.10/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 346, in wrapper
    return f(*args, **kwargs)
  File "/home/guberti/.local/lib/python3.10/site-packages/torch/distributed/run.py", line 806, in main
    run(args)
  File "/home/guberti/.local/lib/python3.10/site-packages/torch/distributed/run.py", line 797, in run
    elastic_launch(
  File "/home/guberti/.local/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 134, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/home/guberti/.local/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 264, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================
medusa/train/train.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2023-09-13_15:49:40
  host      : guberti-thelio
  rank      : 0 (local_rank: 0)
  exitcode  : 1 (pid: 147902)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
```

Also - this is a very cool repo. I'm a big fan :)

## 评论 (2)

### leeyeehoo · 2023-09-14

Thank you Gavin, I will cc @ctlllll to see if he can fix it!

### ctlllll · 2023-09-14

Added, thank you for pointing it out!
