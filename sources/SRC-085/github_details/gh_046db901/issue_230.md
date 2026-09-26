# [Issue #230] Can EAGLE-3 be used across different machines?

source: https://github.com/SafeAILab/EAGLE/issues/230
state: open | updated: 2025-07-28T05:15:43Z
labels: 

## 正文

Can EAGLE-3 be used across multiple GPUs on different machines/nodes, or between a GPU on one machine, and a CPU on another?

## 评论 (6)

### hongdaxia · 2025-05-23

Theoretically, EAGLE-3 can accomplish all of these tasks, but its acceleration performance might not be optimal. We have conducted further work based on EAGLE-3. By employing mathematical modeling and considering actual inference costs, we can construct a near-optimal dynamic draft tree (where parameters like `total_token`, `top_k`, and `depth` are dynamically adjusted, unlike EAGLE-3's static ones) within the user's specific inference environment. This approach adapts well to various distributed inference setups (single-machine/single-GPU, single-machine/multi-GPU, multi-machine/multi-GPU, heterogeneous devices) and different inference acceleration techniques (e.g., model quantization, operator optimization). We have observed significant improvements in both single-batch and multi-batch scenarios, with multi-batch improvements exceeding 50%. This work has been submitted to NIPS, and we plan to open-source our code in the future. However, as the paper is currently under double-blind review, we cannot release the project at this time.

### ebubekir-pulat · 2025-05-23

Thank you for the response. If I were to experiment with the setups I mentioned, which method of doing so would you recommend?


Also, the work you have described is very interesting, when might the code and corresponding paper be available?

### hongdaxia · 2025-05-23

> Thank you for the response. If I were to experiment with the setups I mentioned, which method of doing so would you recommend?
> 
> Also, the work you have described is very interesting, when might the code and corresponding paper be available?

For configuration, you simply need to assign the model to different devices. The easiest way is to set the visible GPU. As for inference with the CPU, you'll need to write code to manually assign the device_map parameter, which is used when loading the EaModel. We expect to release our code once the NIPS review process is complete, around August of this year.

### hejieyuan2005 · 2025-06-27

There is no need to perform draft model inference with multi-machine and multi-GPU. The draft model is relatively small, so single-GPU inference is sufficient. Single-GPU achieves the optimal performance, while multi-GPU incurs communication cost overhead.

### ebubekir-pulat · 2025-07-27

> > Thank you for the response. If I were to experiment with the setups I mentioned, which method of doing so would you recommend?
> > Also, the work you have described is very interesting, when might the code and corresponding paper be available?
> 
> For configuration, you simply need to assign the model to different devices. The easiest way is to set the visible GPU. As for inference with the CPU, you'll need to write code to manually assign the device_map parameter, which is used when loading the EaModel. We expect to release our code once the NIPS review process is complete, around August of this year.

@hongdaxia I am a little bit confused by this advice. To make it clear, I want to experiment with EAGLE-3 where I am operating the technique over a CPU on one machine, and a GPU on another machine. In addition, I want to experiment with a setup where EAGLE-3's operation is split between a GPU on one machine and a GPU on another machine. 

I scanned the EAGLE-3 code trying to figure how to implement your suggestions, but I haven't figured out how to do multi-machine inference yet. Could you please provide more detail on how to implement these setups. Thank you.

### hongdaxia · 2025-07-28

> > > Thank you for the response. If I were to experiment with the setups I mentioned, which method of doing so would you recommend?
> > > Also, the work you have described is very interesting, when might the code and corresponding paper be available?
> > 
> > 
> > For configuration, you simply need to assign the model to different devices. The easiest way is to set the visible GPU. As for inference with the CPU, you'll need to write code to manually assign the device_map parameter, which is used when loading the EaModel. We expect to release our code once the NIPS review process is complete, around August of this year.
> 
> [@hongdaxia](https://github.com/hongdaxia) I am a little bit confused by this advice. To make it clear, I want to experiment with EAGLE-3 where I am operating the technique over a CPU on one machine, and a GPU on another machine. In addition, I want to experiment with a setup where EAGLE-3's operation is split between a GPU on one machine and a GPU on another machine.
> 
> I scanned the EAGLE-3 code trying to figure how to implement your suggestions, but I haven't figured out how to do multi-machine inference yet. Could you please provide more detail on how to implement these setups. Thank you.

You can adjust the following code to customize the device_map for your specific setup.
```python
def get_llama_custom_device_map(
    model_name_or_path: str,
    target_gpu_index: int = 0,
    dtype: torch.dtype = torch.float16,
    max_memory_per_gpu: str = None # e.g., "10GiB" or None for auto
) -> dict:
    """
    Calculates a device_map for a Llama model, forcing embeddings, head,
    first layer, and last layer onto the target_gpu_index, while letting
    accelerate automatically balance the rest.

    Args:
        model_name_or_path: Path or Hugging Face identifier for the Llama model.
        target_gpu_index: The index of the GPU to force key layers onto (default: 0).
        dtype: The torch dtype to use for memory calculation (default: torch.float16).
        max_memory_per_gpu: Optional maximum memory per GPU (e.g., "10GiB").
                           If None, uses accelerate's automatic detection.

    Returns:
        A dictionary representing the complete device map suitable for
        AutoModelForCausalLM.from_pretrained(..., device_map=...).
    """
    # 1. Get Config and Layer Count
    try:
        config = AutoConfig.from_pretrained(model_name_or_path, trust_remote_code=True)
        num_layers = config.num_hidden_layers
    except Exception as e:
        raise ValueError(
            f"Could not load config or find 'num_hidden_layers' for {model_name_or_path}. "
            f"Ensure it's a valid Llama model path/ID. Error: {e}"
        ) from e

    # 2. Define Layers to Force (Llama specific)
    layers_to_force = {
        "model.embed_tokens": target_gpu_index,
        "lm_head": target_gpu_index,
        f"model.layers.0": target_gpu_index,
        f"model.layers.{num_layers - 1}": target_gpu_index,
        "model.norm": target_gpu_index, 
    }

    # 3. Infer Auto Map using an empty model
    try:
        with init_empty_weights():
            model_empty = AutoModelForCausalLM.from_config(
                config, torch_dtype=dtype, trust_remote_code=True
            )

        # Define max_memory dictionary if specific limit is given
        max_memory = None
        if max_memory_per_gpu and torch.cuda.is_available():
             num_gpus = torch.cuda.device_count()
             max_memory = {i: max_memory_per_gpu for i in range(num_gpus)}
             # Optionally add CPU memory limit if needed, e.g., max_memory["cpu"] = "30GiB"


        device_map_auto = infer_auto_device_map(
            model_empty,
            max_memory=max_memory,
            no_split_module_classes=["LlamaDecoderLayer"], # Crucial for Llama
            dtype=dtype,
        )
        del model_empty # Free memory
    except Exception as e:
        raise RuntimeError(f"Failed during device map inference: {e}") from e

    # 4. Modify and Return
    final_device_map = device_map_auto.copy()
    final_device_map.update(layers_to_force) # Override with forced mappings

    return final_device_map
```
