# [Issue #2761] train_compile fails on gpu for compile_topology_num_slices > 1

source: https://github.com/AI-Hypercomputer/maxtext/issues/2761
state: closed | updated: 2026-04-28T18:24:43Z
labels: bug

## 正文

### Bug report

`MaxText.train_compile` fails if compile_topology_num_slices > 1. Jax gets initialized in `pyconfig.initialize` by default.  Since `train_compile` calls it before `get_topology_mesh` updates `mock_num_gpu_processes`, the update has no consequences on the `topology_devices`. Setting `quantization_local_shard_count=1` solves it. Seems like jax devices get initialized at `maxtext/src/MaxText/configs/types.py:1666` when figuring out the value of `quantization_local_shard_count`

### Logs/Output

``` bash
python3 -m MaxText.train_compile ./src/MaxText/configs/base.yml compile_topology=a3 hardware=gpu compile_topology_num_slices=8 compiled_trainstep_file=./out/compiled_train_step.pkl
Starting train_compile.py...
...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/opt/maxtext/src/MaxText/train_compile.py", line 264, in <module>
    app.run(main)
  File "/usr/local/lib/python3.12/dist-packages/absl/app.py", line 316, in run
    _run_main(main, args)
  File "/usr/local/lib/python3.12/dist-packages/absl/app.py", line 261, in _run_main
    sys.exit(main(argv))
             ^^^^^^^^^^
  File "/opt/maxtext/src/MaxText/train_compile.py", line 209, in main
    topology_mesh = get_topology_mesh(config)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/maxtext/src/MaxText/train_compile.py", line 81, in get_topology_mesh
    topology_device_mesh = maxtext_utils.create_device_mesh(config, topology_devices)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/maxtext/src/MaxText/maxtext_utils.py", line 1054, in create_device_mesh
    ici_parallelism = max_utils.fill_unspecified_mesh_axes(config.ici_parallelism.copy(), num_devices_per_slice, "ICI")
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/maxtext/src/MaxText/max_utils.py", line 353, in fill_unspecified_mesh_axes
    determined_val >= 1 and determined_val.is_integer
AssertionError: Unspecified value unable to be determined with the given      ICI parallelism values
```

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (2)

### RissyRan · 2026-01-26

Hi @nathanLaubeuf, 

Thanks for reporting the issue! Are you still facing this compile issue? 

I see cmd with a specific compile file `compiled_trainstep_file=./out/compiled_train_step.pkl`. Could you provide the full repo? 

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.
