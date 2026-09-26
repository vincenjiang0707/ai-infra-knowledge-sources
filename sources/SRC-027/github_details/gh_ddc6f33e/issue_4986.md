# [Issue #4986] [Docs] HF to MaxText conversion guide is missing required flags for multimodal models (Gemma 3)

source: https://github.com/AI-Hypercomputer/maxtext/issues/4986
state: closed | updated: 2026-09-01T21:16:54Z
labels: documentation

## 正文

### Documentation

### Summary
The documentation for [HF to MaxText Checkpoint Conversion](https://maxtext.readthedocs.io/en/latest/guides/checkpointing_solutions/convert_checkpoint.html#hf-to-maxtext) provides a generic conversion
  command with `use_multimodal=${USE_MULTIMODAL}`. However, following the documented command for multimodal models (such as `gemma3-4b`) fails with runtime errors due to missing loading arguments.

### Steps to Reproduce
    Run the documented command for `gemma3-4b`:
    ```bash
    python3 -m maxtext.checkpoint_conversion.to_maxtext \
        src/maxtext/configs/base.yml \
        model_name="gemma3-4b" \
        hf_access_token=${HF_TOKEN} \
        base_output_directory="gs://${GCS_BUCKET}/gemma3-4b-mt" \
        scan_layers=True \
        use_multimodal=True \
        hardware=cpu \
        skip_jax_distributed_system=true \
        checkpoint_storage_use_zarr3=1 \
        checkpoint_storage_use_ocdbt=1


### Additional Context

### Errors Observed

  1. Lazy Loading Error:
    ValueError: lazy loading of HF tensors is not supported for multimodal models yet.

  2. Safetensors Eager Loading Key Mismatch (if only --lazy_load_tensors=False is passed):
    ValueError: HuggingFace key model.language_model.embed_tokens.weight not found in state_dict.


  ### Cause

  1. lazy_load_tensors is enabled by default, but multimodal models do not support lazy loading.
  2. In newer MaxText releases, eager_load_method defaults to "safetensors", but Gemma 3 requires --eager_load_method=transformers for key mapping compatibility.

  ### Suggested Documentation Update

  Update the table/guide in convert_checkpoint.md to note that for multimodal models (such as Gemma 3), the following additional flags are required:

        --lazy_load_tensors=False \
        --eager_load_method='transformers'


## 评论 (1)

### hengtaoguo · 2026-09-01

Thanks for raising the concern! We updated multimodal-related ckpt conversion guides in #4989 . Let us know how we can help more.
