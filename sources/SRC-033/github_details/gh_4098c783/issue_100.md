# [Issue #100] 模型是否支持FP8格式模型推理？

source: https://github.com/Ascend/pytorch/issues/100
state: open | updated: 2026-02-13T01:36:32Z
labels: 

## 正文

看到`https://gitcode.com/Ascend/pytorch/pull/26135` 这个PR，不知道当前torch_npu插件对于FP8的支持情况
当前有将npu驱动升级到25.5.0：

<img width="1320" height="1265" alt="Image" src="https://github.com/user-attachments/assets/67c3063b-1830-4ea6-b42c-afd94f65ef7a" />

Ascend-cann-toolkit版本：Ascend-cann-toolkit_8.5.0.alpha002_linux-aarch64.run
Ascend-cann-kernels版本：Ascend-cann-kernels-910b_8.5.0.alpha002_linux-aarch64.run
pytorch_npu插件源码版本：v2.6.0，安装版本：2.6.0.post6+gitacf101a

<img width="873" height="1532" alt="Image" src="https://github.com/user-attachments/assets/ec6ec94d-5628-49f6-8264-41173abd2f67" />

推理模型为：[qwen_image_edit_2509_fp8_e4m3fn.safetensors](https://www.modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/master/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors)


Comfyui执行日志为：

```
comfyui) root@10:/data/software/comfyui# tail -f comfyui.log 
** User directory: /data/software/comfyui/user
** ComfyUI-Manager config path: /data/software/comfyui/user/__manager/config.ini
** Log path: /data/software/comfyui/user/comfyui.log
Using Python 3.11.14 environment at: /root/miniconda3/envs/comfyui
Using Python 3.11.14 environment at: /root/miniconda3/envs/comfyui
[PRE] ComfyUI-Manager

Prestartup times for custom nodes:
   0.0 seconds: /data/software/comfyui/custom_nodes/comfyui-easy-use

get env ASCEND_HOME_PATH = /usr/local/Ascend/ascend-toolkit/latest
Checkpoint files will always be loaded safely.
Total VRAM 62420 MB, total RAM 2062686 MB
pytorch version: 2.6.0+cpu
Set vram state to: NORMAL_VRAM
Device: npu
Using pytorch attention
Python version: 3.11.14 | packaged by conda-forge | (main, Oct 22 2025, 22:39:18) [GCC 14.3.0]
ComfyUI version: 0.7.0
ComfyUI frontend version: 1.35.9
[Prompt Server] web root: /root/miniconda3/envs/comfyui/lib/python3.11/site-packages/comfyui_frontend_package/static
[START] ComfyUI-Manager
get env COMFYUI_PATH = /data/software/comfyui
[ComfyUI-Manager] network_mode: public
onnxruntime cpuid_info warning: Unknown CPU vendor. cpuinfo_vendor value: 15
Total VRAM 62420 MB, total RAM 2062686 MB
pytorch version: 2.6.0+cpu
Set vram state to: NORMAL_VRAM
Device: npu
Blocked by policy: /data/software/comfyui/custom_nodes/ComfyUI-Manager
get env LD_LIBRARY_PATH = /usr/local/Ascend/nnal/asdsip/latest//lib:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64:/usr/local/Ascend/ascend-toolkit/latest/tools/aml/lib64/plugin:/usr/local/Ascend/ascend-toolkit/latest/lib64:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/opskernel:/usr/local/Ascend/ascend-toolkit/latest/lib64/plugin/nnengine:/usr/local/Ascend/ascend-toolkit/latest/opp/built-in/op_impl/ai_core/tbe/op_tiling/lib/linux/aarch64::/usr/local/Ascend/driver/lib64/common:/usr/local/Ascend/driver/lib64/driver
/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/timm/models/layers/__init__.py:49: FutureWarning: Importing from timm.models.layers is deprecated, please import via timm.layers
  warnings.warn(f"Importing from {__name__} is deprecated, please import via timm.layers", FutureWarning)
/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/amp/autocast_mode.py:266: UserWarning: User provided device_type of 'cuda', but CUDA is not available. Disabling
  warnings.warn(
[ComfyUI-RMBG] v2.9.6 | 33 nodes Loaded
WAS Node Suite: OpenCV Python FFMPEG support is enabled
WAS Node Suite Warning: `ffmpeg_bin_path` is not set in `/data/software/comfyui/custom_nodes/was-ns/was_suite_config.json` config file. Will attempt to use system ffmpeg binaries if available.
WAS Node Suite: Finished. Loaded 220 nodes successfully.

	"The only limit to our realization of tomorrow will be our doubts of today." - Franklin D. Roosevelt

### Loading: ComfyUI-Impact-Pack (V8.28.2)
[Impact Pack] Wildcard total size (0.00 MB) is within cache limit (50.00 MB). Using full cache mode.
[Impact Pack] Wildcards loading done.
[Crystools INFO] Crystools version: 1.27.4
get env PATH = /root/miniconda3/envs/comfyui/bin:/root/.cargo/bin:/usr/local/Ascend/ascend-toolkit/latest/bin:/usr/local/Ascend/ascend-toolkit/latest/compiler/ccec_compiler/bin:/usr/local/Ascend/ascend-toolkit/latest/tools/ccec_compiler/bin:/root/miniconda3/envs/comfyui/bin:/root/miniconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/decord
[Crystools INFO] Platform release: 5.10.0-136.49.0.127.10.oe2203.bclinux.aarch64
[Crystools INFO] JETSON: Not detected.
[Crystools INFO] CPU: Kunpeng-920 - Arch: aarch64 - OS: Linux 5.10.0-136.49.0.127.10.oe2203.bclinux.aarch64
[Crystools ERROR] pynvml is not installed. No module named 'pynvml'
[Crystools WARNING] No GPU monitoring libraries available.
get env TORCHINDUCTOR_CACHE_DIR = /tmp/torchinductor_root
[ComfyUI-Easy-Use] server: v1.3.3 Loaded
[ComfyUI-Easy-Use] web root: /data/software/comfyui/custom_nodes/comfyui-easy-use/web_version/v2 Loaded
Web extensions folder found at /data/software/comfyui/web/extensions/ComfyLiterals

============================================================
✅ ComfyUI自定义节点加载成功: maskadd_up_cc
   节点: 遮罩向上延伸
   分类: mask
============================================================

[/data/software/comfyui/custom_nodes/comfy_mtb] | INFO -> loaded 111 nodes successfuly
[/data/software/comfyui/custom_nodes/comfy_mtb] | INFO -> Some nodes (2) could not be loaded. This can be ignored, but go to http://None:8888/mtb if you want more information.

Import times for custom nodes:
   0.0 seconds: /data/software/comfyui/custom_nodes/websocket_image_save.py
   0.0 seconds: /data/software/comfyui/custom_nodes/necklace_cc
   0.0 seconds: /data/software/comfyui/custom_nodes/maskadd_up_cc
   0.0 seconds: /data/software/comfyui/custom_nodes/ComfyLiterals
   0.0 seconds: /data/software/comfyui/custom_nodes/comfyui-inpaint-cropandstitch
   0.0 seconds: /data/software/comfyui/custom_nodes/comfyui_essentials
   0.0 seconds: /data/software/comfyui/custom_nodes/comfyui-custom-scripts
   0.0 seconds: /data/software/comfyui/custom_nodes/comfyui_segment_anything
   0.0 seconds: /data/software/comfyui/custom_nodes/comfyui-kjnodes
   0.1 seconds: /data/software/comfyui/custom_nodes/comfyui-impact-pack
   0.1 seconds: /data/software/comfyui/custom_nodes/ComfyUI_LayerStyle_Advance
   0.2 seconds: /data/software/comfyui/custom_nodes/comfyui_layerstyle
   0.5 seconds: /data/software/comfyui/custom_nodes/ComfyUI-Crystools
   0.5 seconds: /data/software/comfyui/custom_nodes/comfy_mtb
   1.9 seconds: /data/software/comfyui/custom_nodes/was-ns
   2.1 seconds: /data/software/comfyui/custom_nodes/comfyui-easy-use
   2.9 seconds: /data/software/comfyui/custom_nodes/comfyui-rmbg

setup plugin alembic.autogenerate.schemas
setup plugin alembic.autogenerate.tables
setup plugin alembic.autogenerate.types
setup plugin alembic.autogenerate.constraints
setup plugin alembic.autogenerate.defaults
setup plugin alembic.autogenerate.comments
Context impl SQLiteImpl.
Will assume non-transactional DDL.
No target revision found.
Starting server

To see the GUI go to: http://0.0.0.0:8888
got prompt
# 😺dzNodes: LayerStyle -> ImageScaleRestore V2 Processed 1 image(s).
device_str: npu
get env ASCEND_OPP_PATH = /usr/local/Ascend/ascend-toolkit/latest/opp
get env HOME = /root
get env TE_AUTO_RESTART_COUNTER = 0
[W116 10:38:22.382615888 compiler_depend.ts:250] Warning: CAUTION: The operator 'torchvision::roi_align' is not currently supported on the NPU backend and will fall back to run on the CPU. This may have performance implications. (function npu_cpu_fallback)
[W116 10:38:22.393866958 compiler_depend.ts:250] Warning: CAUTION: The operator 'aten::_assert_async' is not currently supported on the NPU backend and will fall back to run on the CPU. This may have performance implications. (function npu_cpu_fallback)
ckpt: /data/software/comfyui/models/vae/qwen_image_vae.safetensors
Using pytorch attention in VAE
Using pytorch attention in VAE
VAE load device: npu:0, offload device: cpu, dtype: torch.bfloat16
[EasyUse] Image Inset Crop: Cropping image 140x226 width inset by 0,140, and height inset by 184, 226
[EasyUse] Image Inset Crop: Cropping image 140x42 width inset by 64,140, and height inset by 0, 42
[EasyUse] Image Inset Crop: Cropping image 140x42 width inset by 0,76, and height inset by 0, 42
ckpt: /data/software/comfyui/models/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors
Found quantization metadata version 1
Using MixedPrecisionOps for text encoder
CLIP/text encoder model load device: npu:0, offload device: cpu, current: cpu, dtype: torch.float16
ckpt: /data/software/comfyui/models/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors
model weight dtype torch.bfloat16, manual cast: None
model_type FLUX
ckpt: /data/software/comfyui/models/loras/Qwen-Image-Lightning-8steps-V2.0-bf16.safetensors
SELECTED: input1
ckpt: /data/software/comfyui/models/loras/Fusion_lora.safetensors
# 😺dzNodes: LayerStyle -> LayerMaskTransform Processed 1 mask(s).
# 😺dzNodes: LayerStyle -> LayerMaskTransform Processed 1 mask(s).
SELECTED: input1
[Impact-Pack] The switch node does not guarantee proper functioning in API mode.
# 😺dzNodes: LayerStyle -> Draw BBOX Mask Processed 1 mask(s).
Requested to load WanVAE
loaded completely; 54833.98 MB usable, 242.03 MB loaded, full load: True
.Requested to load QwenImageTEModel_
loaded completely; 56526.11 MB usable, 7910.29 MB loaded, full load: True
!!! Exception during processing !!! copy_d2d_baseformat_opapi:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:89 NPU function error: call aclnnInplaceCopy failed, error code is 561103
[ERROR] 2026-01-16-10:39:19 (PID:53, Device:0, RankID:-1) ERR00100 PTA call acl api failed.

Traceback (most recent call last):
  File "/data/software/comfyui/execution.py", line 516, in execute
    output_data, output_ui, has_subgraph, has_pending_tasks = await get_output_data(prompt_id, unique_id, obj, input_data_all, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                                                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/execution.py", line 330, in get_output_data
    return_values = await _async_map_node_over_list(prompt_id, unique_id, obj, input_data_all, obj.FUNCTION, allow_interrupt=True, execution_block_cb=execution_block_cb, pre_execute_cb=pre_execute_cb, v3_data=v3_data)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/execution.py", line 304, in _async_map_node_over_list
    await process_inputs(input_dict, i)
  File "/data/software/comfyui/execution.py", line 292, in process_inputs
    result = f(**inputs)
             ^^^^^^^^^^^
  File "/data/software/comfyui/comfy_api/internal/__init__.py", line 149, in wrapped_func
    return method(locked_class, **inputs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy_api/latest/_io.py", line 1519, in EXECUTE_NORMALIZED
    to_return = cls.execute(*args, **kwargs)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy_extras/nodes_qwen.py", line 103, in execute
    conditioning = clip.encode_from_tokens_scheduled(tokens)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd.py", line 207, in encode_from_tokens_scheduled
    pooled_dict = self.encode_from_tokens(tokens, return_pooled=return_pooled, return_dict=True)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd.py", line 271, in encode_from_tokens
    o = self.cond_stage_model.encode_token_weights(tokens)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/text_encoders/qwen_image.py", line 62, in encode_token_weights
    out, pooled, extra = super().encode_token_weights(token_weight_pairs)
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd1_clip.py", line 704, in encode_token_weights
    out = getattr(self, self.clip).encode_token_weights(token_weight_pairs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd1_clip.py", line 45, in encode_token_weights
    o = self.encode(to_encode)
        ^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd1_clip.py", line 297, in encode
    return self(tokens)
           ^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd1_clip.py", line 257, in forward
    embeds, attention_mask, num_tokens, embeds_info = self.process_tokens(tokens, device)
                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/sd1_clip.py", line 219, in process_tokens
    emb, extra = self.transformer.preprocess_embed(emb, device=device)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/text_encoders/llama.py", line 593, in preprocess_embed
    return self.visual(image.to(device, dtype=torch.float32), grid), grid
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/text_encoders/qwen_vl.py", line 425, in forward
    hidden_states = block(hidden_states, position_embeddings, cu_seqlens_now, optimized_attention=optimized_attention)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/text_encoders/qwen_vl.py", line 252, in forward
    hidden_states = self.attn(hidden_states, position_embeddings, cu_seqlens, optimized_attention)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/text_encoders/qwen_vl.py", line 195, in forward
    qkv = self.qkv(hidden_states)
          ^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1739, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/nn/modules/module.py", line 1750, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/ops.py", line 611, in forward
    return self.forward_comfy_cast_weights(input, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/ops.py", line 602, in forward_comfy_cast_weights
    weight, bias, offload_stream = cast_bias_weight(self, input, offloadable=True)
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/ops.py", line 119, in cast_bias_weight
    weight = weight.dequantize()
             ^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/quant_ops.py", line 197, in dequantize
    return LAYOUTS[self._layout_type].dequantize(self._qdata, **self._layout_params)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/data/software/comfyui/comfy/quant_ops.py", line 434, in dequantize
    plain_tensor = torch.ops.aten._to_copy.default(qdata, dtype=orig_dtype)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/miniconda3/envs/comfyui/lib/python3.11/site-packages/torch/_ops.py", line 723, in __call__
    return self._op(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: copy_d2d_baseformat_opapi:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:89 NPU function error: call aclnnInplaceCopy failed, error code is 561103
[ERROR] 2026-01-16-10:39:19 (PID:53, Device:0, RankID:-1) ERR00100 PTA call acl api failed.


Prompt executed in 192.66 seconds

```

## 评论 (1)

### yunyiyun · 2026-02-13

fp8需要对应的芯片支持，
当前报错显示算子报错，故障定位流程可参考
https://www.hiascend.com/document/detail/zh/canncommercial/850/maintenref/troubleshooting/troubleshooting_0001.html

