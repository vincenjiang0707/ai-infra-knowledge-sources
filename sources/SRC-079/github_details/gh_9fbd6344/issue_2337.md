# [Issue #2337] Only 1 sample from AutoCast calibration data set is truly used

source: https://github.com/NVIDIA/Model-Optimizer/issues/2337
state: open | updated: 2026-09-08T03:54:58Z
labels: bug

## 正文

**Before submitting an issue, please make sure it hasn't been already addressed by searching through the [existing and past issues](https://github.com/NVIDIA/Model-Optimizer/issues?q=is%3Aissue).**

## Describe the bug
<!-- Description of what the bug is, its impact (blocker, should have, nice to have) and any stack traces or error messages. -->

In nvidia-modelopt 0.42.0, modelopt.onnx.autocast.convert_to_mixed_precision(..., calibration_data="my_data.npz") OOM-kills the process (~35GB RSS observed) when the calibration NPZ contains hundreds of real samples (tested with 500). The process is SIGKILL'd by the OS with no Python traceback — logs stop right after "Setting up CalibrationDataProvider for calibration".
Root cause (traced through source at the pinned 0.42.0 tag): ReferenceRunner.run() in modelopt/onnx/autocast/referencerunner.py does:

results = Comparator.run(runners, data_loader=data_loader)  # runs ALL N samples
...
output_dict = OrderedDict(results[0][1][0])   # <- only iteration 0
...
input_data = next(iter(data_loader))          # <- only the first item

Since AutoCast first wraps the model with ModifyOutputs(..., outputs=MARK_ALL) (every intermediate tensor becomes a graph output), polygraphy's Comparator.run() executes all N samples and copy.deepcopy()s the full-graph activation dump for every iteration, holding all N of them in memory simultaneously — before this code ever runs. But only sample #0 is ever read out of that list. So:
Memory usage scales linearly with the number of calibration samples provided (N x full-graph-activation-size-per-sample), for a model with sizable intermediate tensors this reaches tens of GB well before N=500.
Samples 1..N-1 are computed, deep-copied, and then silently discarded — they never affect the precision-conversion decision.
Impact: blocker for using real (non-random) calibration data at any non-trivial sample count with this version — the intended use case (calibration_data accepting an NPZ, whose own CalibrationDataProvider docstring describes calibrating "with 512 samples") is unusable above roughly a few dozen samples before hitting OOM on a typical 64GB host.
Note: the main branch's ReferenceRunner.run() docstring now says "When multiple batches of input data are provided, inference is run for each batch and statistics are aggregated across all batches for more robust range estimation," which suggests this has since been addressed by aggregating across batches instead of discarding N-1 of them. This issue is to (a) confirm the 0.42.0 behavior described above is correctly understood, and (b) find out which release introduced the fix so we know what to upgrade to.


### Steps/Code to reproduce bug
<!-- Please list *minimal* steps or code snippet for us to be able to reproduce the bug. -->
<!-- A helpful guide on on how to craft a minimal bug report http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports. -->

Install nvidia-modelopt==0.42.0.
Build an NPZ calibration file with >= ~50-100 samples per ONNX graph input (following the shape/format described in CalibrationDataProvider's docstring in modelopt/onnx/quantization/calib_utils.py).
Run:


import modelopt.onnx.autocast as autocast
autocast.convert_to_mixed_precision(
    onnx_path="model.onnx",
    low_precision_type="fp16",
    calibration_data="calibration_data.npz",
)

Observe the process being killed by the OS OOM killer (check dmesg | grep -i "out of memory") shortly after logging "Setting up CalibrationDataProvider for calibration", with peak RSS scaling with the number of samples in the NPZ.
Separately, add a print(results[0][1]) (or breakpoint) right before the results[0][1][0] line in referencerunner.py to confirm only index [0] (iteration 0) is ever used, regardless of how many samples were in the NPZ.



### Expected behavior
Either: convert_to_mixed_precision should aggregate activation ranges across all provided calibration samples (as the main branch docstring now describes), instead of computing and discarding all-but-one of them, so that per-sample memory usage no longer scales with N for a result that only reflects 1 sample.
Or, at minimum: the documentation for calibration_data (in convert_to_mixed_precision's docstring and the --calibration_data CLI help text) should state that only a single sample is used in this version, so users don't unknowingly pay for the memory cost of N samples for zero additional benefit.

### Who can help?

<!-- To expedite the response to your issue, it would be helpful if you could identify the appropriate person(s) to tag using the @ symbol.
If you are unsure about whom to tag, you can leave it blank, and we will make sure to involve the appropriate person. -->

- ?

## System information

<!-- Run this script to automatically collect system information: https://github.com/NVIDIA/Model-Optimizer/blob/main/.github/ISSUE_TEMPLATE/get_system_info.py -->

Container used (if applicable): N/A (bare host, no container)
OS (e.g., Ubuntu 22.04, CentOS 7, Windows 10): Ubuntu 20.04.6 LTS (Focal Fossa)
CPU architecture (x86_64, aarch64): x86_64
GPU name (e.g. H100, A100, L40S): NVIDIA L4-12Q
GPU memory size: 12288 MiB
Number of GPUs: 1
Library versions (if applicable):
Python: 3.11
ModelOpt version or commit hash: 0.42.0
CUDA: driver 580.126.09 (nvcc not installed in this environment)
PyTorch: 2.6.0
Transformers: N/A (not used in this workflow)
TensorRT-LLM: N/A
ONNXRuntime: 1.24.4
TensorRT: 10.13.3 (trtexec [TensorRT v101303])
Any other details that may help: N/A



## 评论 (1)

### hychiang-git · 2026-09-08

Hi, thanks for reporting this. Based on your description, we identified two issues:
1. [PR #815](https://github.com/NVIDIA/Model-Optimizer/pull/815) retained activations from all calibration samples, but ModelOpt 0.42 used only the first sample for precision decisions.
2. The [current implementation](https://github.com/NVIDIA/Model-Optimizer/blob/6e4789fa43726f800b6d6f63d6611b6472b00ba0/modelopt/onnx/autocast/referencerunner.py#L297-L350) uses all samples but retains their activations until aggregation, causing memory usage to scale with the sample count and potentially trigger an OOM.
