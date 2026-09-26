# [Issue #1755] Automated command for llama2-70b: Cannot take a larger sample than population

source: https://github.com/mlcommons/inference/issues/1755
state: closed | updated: 2026-07-27T00:37:09Z
labels: Stale

## 正文

Hello mlcommons team,

I want to run the "Automated command to run the benchmark via MLCommons CM" (from the example: https://github.com/mlcommons/inference/tree/master/language/llama2-70b), but I am getting the following error:

```

/root/mambaforge/bin/python3 processorca.py --dataset_pq_path=/root/CM/repos/local/cache/6b2eec484ab2492f/repo/1M-GPT4-Augmented.parquet --model_dir=/Llama-2-70b-chat-hf --seqlen_limit=2048 --export_dir=/root/CM/repos/local/cache/afd6cc85da314087/processed-openorca --num_total_samples=60
Creating /root/CM/repos/local/cache/afd6cc85da314087/processed-openorca
Tokenizing input
Loaded parquet and tokenized in 1141.6977050304413 sec.
Unique sample origin datasets: ['flan' 't0' 'cot' 'niv']
Subset 'cot' has 69699 samples
Subset 'flan' has 379312 samples
Subset 'niv' has 25501 samples
Subset 't0' has 110258 samples
Sampling 15 from cot
Sampling 15 from flan
Sampling 15 from niv
Sampling 15 from t0
Traceback (most recent call last):
  File "/root/CM/repos/local/cache/c0f962d0a3104acb/inference/language/llama2-70b/processorca.py", line 274, in <module>
    ds_gen.generate(
  File "/root/CM/repos/local/cache/c0f962d0a3104acb/inference/language/llama2-70b/processorca.py", line 244, in generate
    calib_ds = sampled_df.sample(n=self.calibration_subset_size,
  File "/root/mambaforge/lib/python3.10/site-packages/pandas/core/generic.py", line 6118, in sample
    sampled_indices = sample.sample(obj_len, size, replace, weights, rs)
  File "/root/mambaforge/lib/python3.10/site-packages/pandas/core/sample.py", line 152, in sample
    return random_state.choice(obj_len, size=size, replace=replace, p=weights).astype(
  File "numpy/random/mtrand.pyx", line 1024, in numpy.random.mtrand.RandomState.choice
ValueError: Cannot take a larger sample than population when 'replace=False'

CM error: Portable CM script failed (name = get-preprocessed-dataset-openorca, return code = 256)

```

I added some debugging line to `/root/CM/repos/local/cache/c0f962d0a3104acb/inference/language/llama2-70b/processorca.py` and noticed that it tries to sample 1000 samples from a df shape of (60, 10).

I am running the following command: 
```
cm run script --tags=run-mlperf,inference  --model=llama2-70b-99 --env.LLAMA2_CHECKPOINT_PATH=/Llama-2-70b-chat-hf
 --implementation=reference --backend=pytorch --device=cpu --precision=float32 --scenario=Offline --quiet
```


## 评论 (7)

### philross · 2024-07-01

@arjunsuresh Do you have any idea why this fails?

### arjunsuresh · 2024-07-01

@philross Can you please try adding `--adr.numpy.version=1.26.4` to the run command?

### philross · 2024-07-02

@arjunsuresh  Thanks for the swift response, but I am getting the same error:

```
Installing collected packages: safetensors, regex, numpy, huggingface-hub, tokenizers, transformers
  Attempting uninstall: numpy
    Found existing installation: numpy 2.0.0
    Uninstalling numpy-2.0.0:
      Successfully uninstalled numpy-2.0.0
Successfully installed huggingface-hub-0.23.4 numpy-1.26.4 regex-2024.5.15 safetensors-0.4.3 tokenizers-0.19.1 transformers-4.42.3
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
             ! cd /root/CM/repos/local/cache/b05d53c7d4f54104
             ! call /root/CM/repos/mlcommons@cm4mlops/script/get-generic-python-lib/run.sh from tmp-run.sh
             ! call "postprocess" from /root/CM/repos/mlcommons@cm4mlops/script/get-generic-python-lib/customize.py
            Detected version: 4.42.3

      * cm run script "get ml-model llama2"
           ! load /root/CM/repos/local/cache/9053ddd372794622/cm-cached-state.json

LLAMA2 checkpoint path: /Llama-2-70b-chat-hf

           ! cd /root/CM/repos/local/cache/08e8714020ca47f6
           ! call /root/CM/repos/mlcommons@cm4mlops/script/get-preprocessed-dataset-openorca/run.sh from tmp-run.sh
/root/mambaforge/bin/python3 processorca.py --dataset_pq_path=/root/CM/repos/local/cache/08ff3d7d410c4d24/repo/1M-GPT4-Augmented.parquet --model_dir=/Llama-2-70b-chat-hf --seqlen_limit=2048 --export_dir=/root/CM/repos/local/cache/08e8714020ca47f6/processed-openorca --num_total_samples=60
Creating /root/CM/repos/local/cache/08e8714020ca47f6/processed-openorca
Tokenizing input
 Loaded parquet and tokenized in 1565.8836648464203 sec.
Unique sample origin datasets: ['flan' 't0' 'cot' 'niv']
Subset 'cot' has 69699 samples
Subset 'flan' has 379312 samples
Subset 'niv' has 25501 samples
Subset 't0' has 110258 samples
Sampling 15 from cot
Sampling 15 from flan
Sampling 15 from niv
Sampling 15 from t0
Traceback (most recent call last):
  File "/root/CM/repos/local/cache/550c6613c996438b/inference/language/llama2-70b/processorca.py", line 274, in <module>
    ds_gen.generate(
  File "/root/CM/repos/local/cache/550c6613c996438b/inference/language/llama2-70b/processorca.py", line 244, in generate
    calib_ds = sampled_df.sample(n=self.calibration_subset_size,
  File "/root/mambaforge/lib/python3.10/site-packages/pandas/core/generic.py", line 6118, in sample
    sampled_indices = sample.sample(obj_len, size, replace, weights, rs)
  File "/root/mambaforge/lib/python3.10/site-packages/pandas/core/sample.py", line 152, in sample
    return random_state.choice(obj_len, size=size, replace=replace, p=weights).astype(
  File "numpy/random/mtrand.pyx", line 1001, in numpy.random.mtrand.RandomState.choice
ValueError: Cannot take a larger sample than population when 'replace=False'

CM error: Portable CM script failed (name = get-preprocessed-dataset-openorca, return code = 256)
```

I ran this command:   

```
cm run script --tags=run-mlperf,inference  --model=llama2-70b-99 --env.LLAMA2_CHECKPOINT_PATH=/Llama-2-70b-chat-hf --adr.numpy.version=1.26.4 --implementation=reference --backend=pytorch --device=cpu --precision=float32 --scenario=Offline --quiet
```

Looking at the log above, it seems that numpy was installed with version `numpy-1.26.4`

### arjunsuresh · 2024-07-02

Unfortunately, I'm not able to reproduce this issue - so should be an issue with some python package version in use. You can try the same command in docker by doing:
```
cm pull repo
```
Add `--docker` to the run command used before.


### mydragonfly00 · 2024-07-03

--tags=run-mlperf,inference,_full     That might solve the problem 

### philross · 2024-07-08

Adding `_full ` seems to fix my problem, thank you @mydragonfly00 

### github-actions[bot] · 2026-07-27

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
