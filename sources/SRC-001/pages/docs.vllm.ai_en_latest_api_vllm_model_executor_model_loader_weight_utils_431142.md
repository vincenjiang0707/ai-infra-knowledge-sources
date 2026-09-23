source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/weight_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.weight_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils)

Utilities for downloading and initializing model weights.

Functions:

-
–[atomic_writer](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.atomic_writer)Context manager that provides an atomic file writing routine.

-
–[composed_weight_loader](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.composed_weight_loader)Create a weight loader that post-processes the weights after loading

-
–[default_weight_loader](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.default_weight_loader)Default weight loader.

-
–[download_safetensors_index_file_from_hf](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf)Download hf safetensors index file from Hugging Face Hub.

-
–[download_weights_from_hf](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf)Download model weights from Hugging Face Hub.

-
–[enable_xet_high_performance](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.enable_xet_high_performance)Automatically activates xet high performance mode

-
–[fastsafetensors_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.fastsafetensors_weights_iterator)Iterate over the weights in the model safetensor files

-
–[filter_files_not_needed_for_inference](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.filter_files_not_needed_for_inference)Exclude files that are not needed for inference.

-
–[instanttensor_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.instanttensor_weights_iterator)Iterate over the weights in the model safetensor files

-
–[maybe_download_from_modelscope](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_download_from_modelscope)Download model from ModelScope hub if VLLM_USE_MODELSCOPE is True.

-
–[maybe_remap_kv_scale_name](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_kv_scale_name)Remap the name of FP8 k/v_scale parameters.

-
–[maybe_remap_moe_expert_param_name](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_moe_expert_param_name)Remap MoE expert parameter names to account for routed_experts hierarchy.

-
–[multi_thread_pt_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.multi_thread_pt_weights_iterator)Multi-Thread iterate over the weights in the model bin/pt files.

-
–[multi_thread_safetensors_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.multi_thread_safetensors_weights_iterator)Multi-Thread iterate over the weights in the model safetensor files.

-
–[np_cache_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.np_cache_weights_iterator)Iterate over the weights in the model np files.

-
–[pt_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.pt_weights_iterator)Iterate over the weights in the model bin/pt files.

-
–[remap_moe_expert_weights](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.remap_moe_expert_weights)Remap MoE expert parameter names for backward compatibility.

-
–[row_parallel_weight_loader](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.row_parallel_weight_loader)Load weights that are row-parallelized.

-
–[runai_safetensors_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.runai_safetensors_weights_iterator)Iterate over the weights in the model safetensor files.

-
–[safetensors_weights_iterator](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.safetensors_weights_iterator)Iterate over the weights in the model safetensor files.

-
–[sharded_weight_loader](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.sharded_weight_loader)Create a weight loader that shards the weights along the given axis


##

`_get_available_ram_bytes()`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils._get_available_ram_bytes)

Return available RAM, honoring cgroup limits.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`_get_checkpoints_size_bytes(files)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils._get_checkpoints_size_bytes)

Return the total size of the checkpoint files in bytes.

##

`_get_fs_type(files)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils._get_fs_type)

Get the filesystem type of the first file in *files* (Linux only).

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`_natural_sort_key(filepath)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils._natural_sort_key)

Natural sort key for filenames with numeric components, such as model-00001-of-00005.safetensors -> ['model-', 1, '-of-', 5, '.safetensors']

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`_prefetch_all_checkpoints(sorted_files, num_prefetch_threads=DEFAULT_SAFETENSORS_PREFETCH_NUM_THREADS, block_size=DEFAULT_SAFETENSORS_PREFETCH_BLOCK_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils._prefetch_all_checkpoints)

Start prefetching checkpoint files into page cache in a background thread.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`_prefetch_checkpoint(file_path, block_size=DEFAULT_SAFETENSORS_PREFETCH_BLOCK_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils._prefetch_checkpoint)

Prefetch a checkpoint file into the OS page cache.

Reads the file in blocks so the kernel caches its pages before workers load the same file.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`atomic_writer(filepath, mode='w', encoding=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.atomic_writer)

Context manager that provides an atomic file writing routine.

The context manager writes to a temporary file and, if successful, atomically replaces the original file.

Parameters:

-

(`filepath`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.atomic_writer(filepath))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)or[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)The path to the file to write.

-

(`mode`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.atomic_writer(mode))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'w'`

) –The file mode for the temporary file (e.g., 'w', 'wb').

-

(`encoding`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.atomic_writer(encoding))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`None`

) –The encoding for text mode.


Yields:

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`composed_weight_loader(loader, fn)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.composed_weight_loader)

Create a weight loader that post-processes the weights after loading

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`default_weight_loader(param, loaded_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.default_weight_loader)

Default weight loader.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`download_safetensors_index_file_from_hf(model_name_or_path, index_file, cache_dir, subfolder=None, revision=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf)

Download hf safetensors index file from Hugging Face Hub.

Parameters:

-

(`model_name_or_path`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf(model_name_or_path))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The model name or path.

-

(`index_file`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf(index_file))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The safetensors index file name

-

(`cache_dir`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf(cache_dir))`Optional[`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The cache directory to store the model weights. If None, will use HF defaults.

-

(`subfolder`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf(subfolder))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –The subfolder within the model repository to download weights from.

-

(`revision`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_safetensors_index_file_from_hf(revision))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –The revision of the model.


## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`download_weights_from_hf(model_name_or_path, cache_dir, allow_patterns, revision=None, subfolder=None, ignore_patterns=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf)

Download model weights from Hugging Face Hub.

Parameters:

-

(`model_name_or_path`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf(model_name_or_path))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The model name or path.

-

(`cache_dir`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf(cache_dir))`Optional[`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The cache directory to store the model weights. If None, will use HF defaults.

-

(`allow_patterns`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf(allow_patterns))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The allowed patterns for the weight files. Files matched by any of the patterns will be downloaded.

-

(`revision`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf(revision))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –The revision of the model.

-

(`subfolder`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf(subfolder))`Optional[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`None`

) –The subfolder within the model repository to download weights from.

-

(`ignore_patterns`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.download_weights_from_hf(ignore_patterns))`Optional[Union[`

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]]`None`

) –The patterns to filter out the weight files. Files matched by any of the patterns will be ignored.


Returns:

-
(`str`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The path to the downloaded model weights.


## Source code in `vllm/model_executor/model_loader/weight_utils.py`


|
|

##

`enable_xet_high_performance()`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.enable_xet_high_performance)

Automatically activates xet high performance mode

##

`fastsafetensors_weights_iterator(hf_weights_files, use_tqdm_on_load)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.fastsafetensors_weights_iterator)

Iterate over the weights in the model safetensor files using fastsafetensor library.

Uses ParallelLoader for pipelined loading: the producer thread prepares metadata for the next shard while the consumer yields tensors from the current shard.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


|
|

##

`filter_files_not_needed_for_inference(hf_weights_files)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.filter_files_not_needed_for_inference)

Exclude files that are not needed for inference.

See https://github.com/huggingface/transformers/blob/v4.34.0/src/transformers/trainer.py#L227-L233

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`instanttensor_weights_iterator(hf_weights_files, use_tqdm_on_load)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.instanttensor_weights_iterator)

Iterate over the weights in the model safetensor files using instanttensor library.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`maybe_download_from_modelscope(model, revision=None, download_dir=None, ignore_patterns=None, allow_patterns=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_download_from_modelscope)

Download model from ModelScope hub if VLLM_USE_MODELSCOPE is True.

Returns the path to the downloaded model, or None if the model is not downloaded from ModelScope.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`maybe_remap_kv_scale_name(name, params_dict)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_kv_scale_name)

Remap the name of FP8 k/v_scale parameters.

This function handles the remapping of FP8 k/v_scale parameter names. It detects if the given name ends with a suffix and attempts to remap it to the expected name format in the model. If the remapped name is not found in the params_dict, a warning is printed and None is returned.

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_kv_scale_name(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The original loaded checkpoint parameter name.

-

(`params_dict`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_kv_scale_name(params_dict))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)Dictionary containing the model's named parameters.


Returns:

-
(`str`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe remapped parameter name if successful, or the original name if no remapping is needed.

-
(`None`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneIf the remapped name is not found in params_dict.


## Source code in `vllm/model_executor/model_loader/weight_utils.py`


|
|

##

`maybe_remap_moe_expert_param_name(name, params_dict)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_moe_expert_param_name)

Remap MoE expert parameter names to account for routed_experts hierarchy.

This handles the transition from the old FusedMoE structure where weights were directly in the experts module, to the new MoERunner → RoutedExperts structure.

## Checkpoint weights have names like

layers.0.mlp.experts.w13_weight layers.0.feed_forward.experts.w2_input_scale

But actual parameters are now: layers.0.mlp.experts.routed_experts.w13_weight layers.0.feed_forward.experts.routed_experts.w2_input_scale

This function inserts 'routed_experts.' into the path when needed.

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_moe_expert_param_name(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Parameter name from checkpoint

-

(`params_dict`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.maybe_remap_moe_expert_param_name(params_dict))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Parameter]Dictionary of model parameters (from named_parameters())


Returns:

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


|
|

##

`multi_thread_pt_weights_iterator(hf_weights_files, use_tqdm_on_load, pt_load_map_location='cpu', max_workers=4)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.multi_thread_pt_weights_iterator)

Multi-Thread iterate over the weights in the model bin/pt files.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`multi_thread_safetensors_weights_iterator(hf_weights_files, use_tqdm_on_load, max_workers=4)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.multi_thread_safetensors_weights_iterator)

Multi-Thread iterate over the weights in the model safetensor files.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`np_cache_weights_iterator(model_name_or_path, cache_dir, hf_folder, hf_weights_files, use_tqdm_on_load)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.np_cache_weights_iterator)

Iterate over the weights in the model np files.

Will dump the model weights to numpy files if they are not already dumped.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`pt_weights_iterator(hf_weights_files, use_tqdm_on_load, pt_load_map_location='cpu')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.pt_weights_iterator)

Iterate over the weights in the model bin/pt files.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`remap_moe_expert_weights(weights, params_dict)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.remap_moe_expert_weights)

Remap MoE expert parameter names for backward compatibility.

This allows models with custom weight loading to automatically handle both old and new checkpoint formats without needing model-specific remapping code.

## Usage

params_dict = dict(model.named_parameters()) for name, weight in remap_moe_expert_weights(weights, params_dict): # name is automatically remapped if needed param = params_dict[name] ...

Parameters:

-

(`weights`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.remap_moe_expert_weights(weights))

) –[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]Iterator of (name, tensor) tuples from checkpoint

-

(`params_dict`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.remap_moe_expert_weights(params_dict))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Parameter]Dictionary of model parameters (from named_parameters())


Yields:

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`row_parallel_weight_loader(param, loaded_weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.row_parallel_weight_loader)

Load weights that are row-parallelized.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`runai_safetensors_weights_iterator(hf_weights_files, use_tqdm_on_load, is_distributed=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.runai_safetensors_weights_iterator)

Iterate over the weights in the model safetensor files.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


##

`safetensors_weights_iterator(hf_weights_files, use_tqdm_on_load, safetensors_load_strategy=None, local_expert_ids=None, *, safetensors_prefetch_num_threads=DEFAULT_SAFETENSORS_PREFETCH_NUM_THREADS, safetensors_prefetch_block_size=DEFAULT_SAFETENSORS_PREFETCH_BLOCK_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.safetensors_weights_iterator)

Iterate over the weights in the model safetensor files.

When *local_expert_ids* is provided, expert weights not belonging to this rank are skipped **before** reading from disk, which drastically reduces storage I/O for MoE models under EP.

## Source code in `vllm/model_executor/model_loader/weight_utils.py`


|
|

##

`sharded_weight_loader(shard_axis)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.weight_utils.sharded_weight_loader)

Create a weight loader that shards the weights along the given axis