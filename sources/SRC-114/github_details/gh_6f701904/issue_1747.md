# [Issue #1747] Running Automated command for llama2-70b without downloading the model

source: https://github.com/mlcommons/inference/issues/1747
state: closed | updated: 2026-07-27T00:37:11Z
labels: Stale

## 正文

Hello mlcommons team,

I want to run the "Automated command to run the benchmark via MLCommons CM" (from the example: https://github.com/mlcommons/inference/tree/master/language/llama2-70b), but I do not want to download llama2-70b, since I already have it locally.

Is it possible to set a environment variable to point to the local directory?



## 评论 (5)

### arjunsuresh · 2024-06-25

yes @philross . We do have [this ENV Key](https://github.com/mlcommons/cm4mlops/blob/main/script/get-ml-model-llama2/_cm.json#L12) and by using `--env.LLAMA2_CHECKPOINT_PATH=<local_path>` the download should be skipped. 

### arjunsuresh · 2024-06-25

@anandhu-eng 

### philross · 2024-06-26

Thanks for the swift reponse!

If I run `cm run script --tags=run-mlperf,inference  --model=llama2-70b-99 --env.LLAMA2_CHECKPOINT_PATH=/Llama-2-70b-chat-hf --implementation=reference --backend=pytorch --device=cpu --precision=float32 --scenario=Offline --quiet` 

I get the following error: 
```
    * cm run script "get ml-model llama2 raw _pytorch _fp32"
           ! call "postprocess" from /root/CM/repos/mlcommons@cm4mlops/script/get-ml-model-llama2/customize.py
Traceback (most recent call last):
  File "/usr/local/bin/cm", line 8, in <module>
    sys.exit(run())
             ^^^^^
  File "/usr/local/lib/python3.12/dist-packages/cmind/cli.py", line 37, in run
    r = cm.access(argv, out='con')
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/cmind/core.py", line 602, in access
    r = action_addr(i)
        ^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 211, in run
    r = self._run(i)
        ^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 1490, in _run
    r = customize_code.preprocess(ii)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/script/run-mlperf-inference-app/customize.py", line 219, in preprocess
    r = cm.access(ii)
        ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/cmind/core.py", line 758, in access
    return cm.access(i)
           ^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/cmind/core.py", line 602, in access
    r = action_addr(i)
        ^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 211, in run
    r = self._run(i)
        ^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 1553, in _run
    r = self._call_run_deps(prehook_deps, self.local_env_keys, local_env_keys_from_meta,  env, state, const, const_state, add_deps_recursive, 
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 2909, in _call_run_deps
    r = script._run_deps(deps, local_env_keys, env, state, const, const_state, add_deps_recursive, recursion_spaces,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 3080, in _run_deps
    r = self.cmind.access(ii)
        ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/cmind/core.py", line 602, in access
    r = action_addr(i)
        ^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 211, in run
    r = self._run(i)
        ^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 1380, in _run
    r = self._call_run_deps(deps, self.local_env_keys, local_env_keys_from_meta, env, state, const, const_state, add_deps_recursive, 
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 2909, in _call_run_deps
    r = script._run_deps(deps, local_env_keys, env, state, const, const_state, add_deps_recursive, recursion_spaces,
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 3080, in _run_deps
    r = self.cmind.access(ii)
        ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/cmind/core.py", line 602, in access
    r = action_addr(i)
        ^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 211, in run
    r = self._run(i)
        ^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 1568, in _run
    r = prepare_and_run_script_with_postprocessing(run_script_input)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 4733, in prepare_and_run_script_with_postprocessing
    rr = run_postprocess(customize_code, customize_common_input, recursion_spaces, env, state, const,
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/automation/script/module.py", line 4785, in run_postprocess
    r = customize_code.postprocess(ii)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/CM/repos/mlcommons@cm4mlops/script/get-ml-model-llama2/customize.py", line 20, in postprocess
    env['LLAMA2_CHECKPOINT_PATH'] = env['CM_ML_MODEL_PATH']
                                    ~~~^^^^^^^^^^^^^^^^^^^^
KeyError: 'CM_ML_MODEL_PATH'

```

I now adjusted `/root/CM/repos/mlcommons\@cm4mlops/script/get-ml-model-llama2/customize.py` so that `CM_ML_MODEL_PATH` is set to `LLAMA2_CHECKPOINT_PATH` and that seems to work.

### arjunsuresh · 2024-06-26

Thank you for reporting that bug. We have just fixed that in the code. 

### github-actions[bot] · 2026-07-27

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
