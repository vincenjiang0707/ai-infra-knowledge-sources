# [Issue #2442] qdq_to_dq fails on MaxViT due to unsupported Transpose after DequantizeLinear

source: https://github.com/NVIDIA/Model-Optimizer/issues/2442
state: open | updated: 2026-09-16T00:53:41Z
labels: bug

## 正文

## Describe the bug
qdq_to_dq has issues working with my chosen model. Seems like the opcode following the one of the dequantizelinear nodes is a transpose node, which is unexpected by the `_convert_weight` function.

```
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\blake\Documents\advitech\acoustics-ml-quantisation\src\quantisation\issue.py", line 86, in <module>
    main()
  File "C:\Users\blake\Documents\advitech\acoustics-ml-quantisation\src\quantisation\issue.py", line 76, in main
    export_to_onnx(
  File "C:\Users\blake\Documents\advitech\acoustics-ml-quantisation\src\quantisation\issue.py", line 28, in export_to_onnx
    onnx_bytes, _ = get_onnx_bytes_and_metadata(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\blake\Documents\advitech\acoustics-ml-quantisation\.venv\Lib\site-packages\modelopt\torch\_deploy\utils\torch_onnx.py", line 635, in get_onnx_bytes_and_metadata
    onnx_opt_graph = qdq_to_dq(onnx_opt_graph)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\blake\Documents\advitech\acoustics-ml-quantisation\.venv\Lib\site-packages\modelopt\onnx\quantization\qdq_utils.py", line 785, in qdq_to_dq
    raise RuntimeError(f"Failed to convert node {node.name}: {e!s}")
RuntimeError: Failed to convert node /stages/stages.0/blocks/blocks.0/attn_block/attn/qkv/weight_quantizer/QuantizeLinear: Unsupported op_type for real weight quantization: Transpose
```

### Code to reproduce bug
```
import torch
import timm
import modelopt.torch.quantization as mtq
from torch import nn
from pathlib import Path
from modelopt.torch._deploy.utils import OnnxBytes, get_onnx_bytes_and_metadata


INPUT_SHAPE = (16, 3, 256, 256)
OUTPUT_PATH = "maxvit_tiny_rw_256_int8.onnx"


# from https://github.com/NVIDIA/Model-Optimizer/blob/21b95adabba3ab4f497937980497dee6bb69b207/examples/onnx_ptq/download_example_onnx.py
def export_to_onnx(
    model: nn.Module,
    input_shape: tuple[int, ...],
    output_path: Path,
    weights_dtype: str = "fp32",
) -> None:
    """Export the torch model to ONNX format."""
    device = "cpu"
    model = model.to(device).eval()
    # Create input tensor with same precision as model's first parameter
    input_dtype = next(model.parameters()).dtype
    input_tensor = torch.randn(input_shape, dtype=input_dtype).to(device)
    model_name = Path(output_path).stem

    onnx_bytes, _ = get_onnx_bytes_and_metadata(
        model=model,
        dummy_input=(input_tensor,),
        weights_dtype=weights_dtype,
        model_name=model_name,
    )

    onnx_bytes_obj = OnnxBytes.from_bytes(onnx_bytes)

    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    onnx_bytes_obj.write_to_disk(
        str(output_dir),
        clean_dir=False,
    )


def forward_loop(model):
    x = torch.randn(INPUT_SHAPE, device=next(model.parameters()).device)

    with torch.no_grad():
        model(x)


def main():
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Load model
    model = timm.create_model(
        "maxvit_tiny_rw_256",
        pretrained=False,
        num_classes=1000,
    ).to(device)
    model.eval()

    # Quantize
    mtq.quantize(
        model,
        mtq.INT8_DEFAULT_CFG,
        forward_loop,
    )

    # Export
    export_to_onnx(
        model=model,
        input_shape=INPUT_SHAPE,
        output_path=OUTPUT_PATH,
    )

    print(f"Exported: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
```

### Expected behavior

Looking at the model via netron when dq_only = False, it seems like the transpose follows a matmul layer, so i guess the simple fix is to just manually transpose the nodes stored in qdq and remove the transpose node. MatMul is accepted so that as an opcode so that should work, although there's probably a cleaner fix that I'm not aware of.

<img width="497" height="665" alt="Image" src="https://github.com/user-attachments/assets/443552ec-a501-4857-81ef-c279b7b40bbc" />

## System information

- Container used (if applicable): ?
- OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): Windows 11
- CPU architecture (x86_64, aarch64): AMD64
- GPU name (e.g. H100, A100, L40S): NVIDIA GeForce RTX 3050 Laptop GPU
- GPU memory size: 4.0 GB
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.12.10
  - ModelOpt version or commit hash: 0.46.0
  - CUDA: ?
  - PyTorch: 2.11.0+cu128
  - Transformers: ?
  - TensorRT-LLM: ?
  - ONNXRuntime: 1.22.0
  - TensorRT: ?
- Any other details that may help:
  - timm: 1.0.29


## 评论 (1)

### hychiang-git · 2026-09-16

ModelOpt’s ONNX export fails for quantized MaxViT because [qdq_to_dq()](https://github.com/NVIDIA/Model-Optimizer/blob/main/modelopt/onnx/quantization/qdq_utils.py#L703-L796) assumes DequantizeLinear directly feeds Conv, Gemm, or MatMul, while the exported graph contains DequantizeLinear → Transpose → MatMul ([issue #2442](https://github.com/NVIDIA/Model-Optimizer/issues/2442)). The fix should update [_get_successive_consumers() and _convert_weight()](https://github.com/NVIDIA/Model-Optimizer/blob/main/modelopt/onnx/quantization/qdq_utils.py#L580-L682) to safely trace through or fold Transpose while preserving the correct weight quantization axis, scale, and zero point.
