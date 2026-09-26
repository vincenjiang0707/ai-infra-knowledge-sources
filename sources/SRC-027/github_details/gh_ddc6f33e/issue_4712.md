# [Issue #4712] Multimodal SFT: Conversion errors to HF Safetensors

source: https://github.com/AI-Hypercomputer/maxtext/issues/4712
state: open | updated: 2026-08-04T16:54:40Z
labels: bug

## 正文

### Bug report

python3 -m maxtext.checkpoint_conversion.to_huggingface \
  model_name=${MODEL_NAME?} \
  load_parameters_path=${POST_TRAIN_PATH?} \
  base_output_directory=${HF_EXPORT?} \
  scan_layers=True \
  use_multimodal=True \
  weight_dtype=bfloat16

### Logs/Output

1. I get the following error, while `rngs` and `aqt` should be ignored: [full_error.log](https://github.com/user-attachments/files/30669717/full_error.log).

2. Once this error was fixed by manually stripping those, I got the following error:
```
I0803 16:00:42.236964 126572543616832 utils.py:920] Detected NNX-SFT checkpoint structure
I0803 16:00:42.238894 126572543616832 to_huggingface.py:321]
Proccessing weight...
0%| | 0/571 [00:00<?, ?it/s, RAM: 75.0/1417.3GB (5.3%)]I0803 16:00:42.239622 126572543616832 utils.py:226] maxtext param: params-token_embedder-embedding
I0803 16:00:42.239660 126572543616832 utils.py:242] unscan
0%|▎ | 1/571 [00:00<02:21, 4.04it/s, RAM: 76.3/1417.3GB (5.4%)]I0803 16:00:42.487491 126572543616832 utils.py:226] maxtext param: params-decoder-decoder_norm-scale
I0803 16:00:42.487586 126572543616832 utils.py:242] unscan
I0803 16:00:42.521244 126572543616832 utils.py:226] maxtext param: params-vision_encoder-Gemma3VisionEncoderLayer_0-embedding-kernel
I0803 16:00:42.521318 126572543616832 utils.py:242] unscan
I0803 16:00:42.571363 126572543616832 utils.py:226] maxtext param: params-vision_encoder-Gemma3VisionEncoderLayer_0-embedding-bias
I0803 16:00:42.571458 126572543616832 utils.py:242] unscan
I0803 16:00:42.571536 126572543616832 utils.py:226] maxtext param: params-vision_encoder-Gemma3VisionEncoderLayer_0-pos_embedding
I0803 16:00:42.571563 126572543616832 utils.py:242] unscan
1%|█ | 4/571 [00:00<00:48, 11.60it/s, RAM: 76.3/1417.3GB (5.4%)]
Traceback (most recent call last):
File "<frozen runpy>", line 198, in _run_module_as_main
File "<frozen runpy>", line 88, in _run_code
File "/home/dgouju_google_com/maxtext_venv/lib/python3.12/site-packages/maxtext/checkpoint_conversion/to_huggingface.py", line 368, in <module>
app.run(main)
File "/home/dgouju_google_com/maxtext_venv/lib/python3.12/site-packages/absl/app.py", line 367, in run
_run_main(main, args)
File "/home/dgouju_google_com/maxtext_venv/lib/python3.12/site-packages/absl/app.py", line 312, in _run_main
sys.exit(main(argv))
^^^^^^^^^^
File "/home/dgouju_google_com/maxtext_venv/lib/python3.12/site-packages/maxtext/checkpoint_conversion/to_huggingface.py", line 333, in main
processed_params = process_maxtext_param(key, weight, param_map, hook_fn_map, shape_map, config)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "/home/dgouju_google_com/maxtext_venv/lib/python3.12/site-packages/maxtext/checkpoint_conversion/utils/utils.py", line 244, in process_maxtext_param
_process(
File "/home/dgouju_google_com/maxtext_venv/lib/python3.12/site-packages/maxtext/checkpoint_conversion/utils/utils.py", line 183, in _process
numpy_slice = convert_jax_weight_to_numpy(processed_slice, save_dtype).reshape(target_hf_shape)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'float' object cannot be interpreted as an integer
```
Sounds like standard/multimodal layer shape translations (the shape_map) where dimensions are derived via standard division `/` rather than floor/integer division `//`, or when floating-point configuration parameters are propagated through the MaxText model configs.

A hotfix was to patch `numpy_slice` creation in `_process()` in `maxtext/checkpoint_conversion/utils/utils.py` with:
```
int_target_hf_shape = tuple(int(dim) for dim in target_hf_shape) if isinstance(target_hf_shape, (tuple, list)) else int(target_hf_shape)
numpy_slice = convert_jax_weight_to_numpy(processed_slice, save_dtype).reshape(int_target_hf_shape)
```

### Environment Information

Installed with `uv pip install maxtext[tpu-post-train]==0.2.2 --resolution=lowest`

### Additional Context

_No response_

## 评论 (0)
