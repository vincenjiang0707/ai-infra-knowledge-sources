# [Issue #2016] [ONNX PTQ] Support for third-party custom ORT/TRT plugins in static calibration

source: https://github.com/NVIDIA/Model-Optimizer/issues/2016
state: open | updated: 2026-08-02T22:08:53Z
labels: feature request

## 正文

## Describe the bug
When performing Post-Training Quantization (PTQ) via `modelopt.onnx.quantization.quantize()`, static calibration fails when the input ONNX graph contains non-standard custom domains or third-party operators (e.g., `custom_domain::CustomOp`), even when those custom operators are explicitly excluded from quantization via `op_types_to_exclude` / `nodes_to_exclude`.

**Impact:** Blocker for networks containing custom C++/CUDA operations when executing single-stage PTQ workflows under ONNX Runtime execution providers (such as `CUDAExecutionProvider`).

#### Technical Root Causes Identified:
1. **Validation Gate Failure (`trt_utils.py`):**
   `load_onnx_model` invokes `get_custom_layers()`, which initializes a native `trt.OnnxParser`. If a node belongs to a custom namespace/domain outside the empty default `""` or `trt.plugins`, the native parser throws an unhandled API error (`INVALID_NODE: creator && "Plugin not found..."`). Furthermore, `set_trt_plugin_domain` unconditionally overrides user-defined domains to `"trt.plugins"`.

2. **Session Isolation in Calibrator (`ort_patching.py`):**
   When bypassing initial parser validation, calibration fails during static graph execution. In `_create_inference_session_with_ep_config`, ModelOpt instantiates an `ort.InferenceSession` for the temporary `augmented_model.onnx` graph without providing a mechanism to register external custom operator binaries (e.g., calling `sess_options.register_custom_ops_library(plugin_path)`). This causes ONNX Runtime to halt execution with:
   `[ONNXRuntimeError] : 1 : FAIL : Load model failed: Fatal error: custom_domain:CustomOp(-1) is not a registered function/op`

### Steps/Code to reproduce bug

```python
import modelopt.onnx.quantization as moq

# Model containing a custom operator (e.g., domain: "custom_domain", op_type: "CustomOp")
onnx_model_path = "model_with_custom_op.onnx"

# Configure PTQ engine settings
# Assume user has a custom ORT operator shared library (.so) for execution
quant_cfg = {
    "quantize_mode": "int8",
    "calibration_method": "max",
    "calibration_eps": ["cuda:0", "cpu"],
    "op_types_to_exclude": ["CustomOp"],
    "nodes_to_exclude": ["/path/to/custom_node"],
}

# Execution halts during initial TRT parsing or internal augmented session instantiation
moq.quantize(
    onnx_path=onnx_model_path,
    quantize_mode="int8",
    calibration_data_reader=data_reader,
    engine_settings=quant_cfg,
)
```

### Expected behavior

ModelOpt should provide an official mechanism (e.g., via `engine_settings` or `extra_options`) to pass external custom operator shared libraries (`.so` / `.dll`) into both the initial graph inspection pass and all internal `ort.InferenceSession` instances (such as the augmented model calibrator in `ort_patching.py`), allowing custom operators to execute seamlessly on CUDA without requiring manual source patching.

### Who can help

N/A

## System information

- **Container used (if applicable):** Custom Docker Development Container
- **OS:** Linux 6.14.0-37-generic (Ubuntu x86_64)
- **CPU architecture:** x86_64
- **GPU name:** NVIDIA RTX 2000 Ada Generation
- **GPU memory size:** 15.58 GB
- **Number of GPUs:** 1
- **Library versions:**
  - **Python:** 3.12.12
  - **ModelOpt version or commit hash:** 0.42.0
  - **CUDA:** 12.4
  - **PyTorch:** 2.5.0+cu124
  - **Transformers:** N/A
  - **TensorRT-LLM:** N/A
  - **ONNXRuntime:** 1.23.0
  - **TensorRT:** 10.3.0
- **Any other details that may help:** Hard-patching `ort_patching.py` to invoke `sess_options.register_custom_ops_library("/path/to/plugin.so")` directly inside `_create_inference_session_with_ep_config` resolved the issue completely and allowed 100% of quantizable nodes (191 nodes) to calibrate and export successfully.

## 评论 (7)

### gcunhase · 2026-07-30

@e-said can you please share a full repro including ONNX file and plugin with instructions on how to compile it on our end?

For additional clarification, ORT requires 'trt.plugins' domain in order to detect those as TRT plugins, so my understanding is that a custom domain outside of that would not work with ORT. Are you able to run that model with ORT outside of ModelOpt?

### e-said · 2026-07-31

Thanks for taking a look @gcunhase 

To address your question regarding ORT vs. TRT execution for custom operators:

**Are we able to run this model in ORT outside of ModelOpt?**  
**Yes, 100%.** Standard ONNX Runtime executes the model smoothly on `CPUExecutionProvider` or `CUDAExecutionProvider` when registering the compiled `.so` C++ custom op library (`sess_options.register_custom_ops_library(...)`). 

The requirement for the `trt.plugins` domain only applies specifically when using ORT’s `TensorrtExecutionProvider` to map nodes directly to native TensorRT plugins. However, standard ORT custom op extensions support **any third-party domain** (e.g., `custom_domain`).

---

### API Gap Analysis

Comparing standard ONNX Runtime with ModelOpt's quantization API reveals a core design assumption:

| Capability | Standard ONNX Runtime (`onnxruntime`) | ModelOpt PTQ (`modelopt.onnx.quantization.quantize`) |
| :--- | :--- | :--- |
| **Plugin Registration** | `sess_options.register_custom_ops_library(path)` | `trt_plugins: list[str] | None = None` |
| **Plugin Type** | Native C++ ORT Custom Ops (`OrtCustomOp`) | TensorRT Plugins (`IPluginCreator`) |
| **Execution Behavior** | Executes natively via CPU/CUDA EPs | Automatically forces `calibration_eps=["trt"]` when custom ops are detected |

Because `moq.quantize()` currently only accepts `trt_plugins`, ModelOpt routes any detected custom op through TensorRT's parser. When TRT evaluates a non-TRT node like `custom_domain::DummyOp`, it checks the TRT plugin creator registry and fails during initialization with an `INVALID_NODE` error.

---

### Reproduction Instructions

I have attached a `.zip` file containing a `Dockerfile`, the custom domain C++ source (`dummy_plugin.cpp`), and the Python reproduction script (`repro.py`). You can reproduce the crash in an isolated environment matching the issue specifications (CUDA 12.4, TRT 10.3, ModelOpt 0.42.0).

**1. Unzip the archive:**
```bash
unzip modelopt_issue_2016.zip
```

**2. Build the Docker container:**
```bash
docker build -t modelopt-issue-2016 .
```

**3. Run the container with GPU passthrough:**
```bash
docker run --rm --gpus all modelopt-issue-2016
```

---

### Verification Logs

```text
[+] Dummy ONNX model created at: dummy_model.onnx

--- Testing Standalone ONNX Runtime Execution ---
[SUCCESS] Standalone ORT executed smoothly! Output shape: (1, 3, 8, 8)

--- Testing ModelOpt PTQ Quantization ---
[modelopt][onnx] - INFO - Starting quantization process for model: dummy_model.onnx
[modelopt][onnx] - INFO - Quantization mode: int8
[modelopt][onnx] - INFO - Preprocessing the model dummy_model.onnx
[07/31/2026-16:57:53] [TRT] [E] IPluginRegistry::getCreator: Error Code 4: API Usage Error (Cannot find plugin: DummyOp, version: 1, namespace:.)
[07/31/2026-16:57:53] [TRT] [E] ModelImporter.cpp:954: ERROR: onnxOpCheckers.cpp:781 In function checkFallbackPluginImporter:
[6] creator && "Plugin not found, are the plugin name, version, and namespace correct?"
[FAILURE] ModelOpt failed with error:
Failed to parse ONNX file: In node 0 with name:  and operator: DummyOp (checkFallbackPluginImporter): INVALID_NODE: creator && "Plugin not found, are the plugin name, version, and namespace correct?"
```

---

### Feature Request / Proposed Solution

Allow passing standard ORT custom op shared libraries into `moq.quantize()` (e.g., `ort_custom_plugins: list[str] = None`). When present, ModelOpt can register them with the calibration session so static calibration proceeds using `CPUExecutionProvider` or `CUDAExecutionProvider` without requiring a TensorRT `IPluginCreator`.

*(Attached: `modelopt_issue_2016.zip`)*
[modelopt_issue_2016.zip](https://github.com/user-attachments/files/30597611/modelopt_issue_2016.zip)

### gcunhase · 2026-07-31

Thank you for the detailed response and for providing a repro, @e-said!

When talking about custom ops, we imply TRT custom ops since the goal of this toolkit is to eventually deploy the quantized model as  TRT engine, so other ORT custom ops are out-of-scope and not currently in the roadmap.

@ajrasane this is not a bug but an RFE, changing the tag. Also note that this doesn't seem to be a trivial change, so we need to plan our engineering resources accordingly.

Thanks.

### ajrasane · 2026-07-31

@e-said, If this is urgent, could you file a PR for this? @gcunhase and I can assist you with the review process.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: c8ccfd6343789c8d03857b9b8e1ef6488b08e61b9ad422bc2ab1fd15d9da7fa7

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: fdc432994b3b90f4621777bc4e7a9e99bab5daddb12c061181b465045effc680

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 6b510241574d592b93c64a0a43862789eff352a2a58feb321511ba5fceb2a8da

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
