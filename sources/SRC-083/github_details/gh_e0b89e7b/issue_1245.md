# [Issue #1245] ROCm and 8-bit quantization

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1245
state: closed | updated: 2026-02-21T20:27:30Z
labels: Documentation, ROCm, Cross Platform, Dependencies

## 正文

### System Info

An AMD Epyc system with 3 MI210.
Quite a complex setup. The system uses slurm to schedule batch jobs which are usually in the form of apptainer run containers. The image I'm using has rocm6.0.2 on ubuntu22.04.

### Reproduction

`python -m bitsandbytes`
```
CUDA specs: CUDASpecs(highest_compute_capability=(9, 0), cuda_version_string='61', cuda_version_tuple=(6, 1))
PyTorch settings found: CUDA_VERSION=61, Highest Compute Capability: (9, 0).
WARNING: CUDA versions lower than 11 are currently not supported for LLM.int8().
You will be only to use 8-bit optimizers and quantization routines!
To manually override the PyTorch CUDA version please see: https://github.com/TimDettmers/bitsandbytes/blob/main/docs/source/nonpytorchcuda.mdx
CUDA SETUP: WARNING! CUDA runtime files not found in any environmental path.
```
Two issues here: CUDA_VERSION here is not 61, that's the ROCm version (6.1), the cuda version is the hell knows what since torch.version.cuda is None on ROCm.
As a result the "lower than 11" makes little sense in this case.
Second issue: `https://github.com/TimDettmers/bitsandbytes/blob/main/docs/source/nonpytorchcuda.mdx` leads nowhere.
That leaves me wondering whether 8-bit on ROCm is really supported or not.

OK, let's try to run some code then:
```
model = AutoModelForCausalLM.from_pretrained(checkpoint, attn_implementation="eager", quantization_config=BitsAndBytesConfig(load_in_8bit=True))
outputs = model.generate(inputs)
```
Result:
```
[...]
Exception: cublasLt ran into an error!
```
See #538.
But now the question is: it's really the case that the existing 8-bit code is not supported on ROCm, or is it a case of architecture/libraries mismatch and 8-bit could actually work?

### Expected behavior

This might be a bug, or it might not. I've not been able to find specific documentation on this. It seems to me like it's possible that 8 bit quantization could actually work but the code to detect if the architecture is supported has issues. Or it may be the case that I can forget about 8 bit on ROCm. But at least I would know it for sure.

## 评论 (3)

### DavideRossi · 2024-06-20

Thanks @mohamedyassin1 what you describe is very similar to my own setup. Can I ask you to paste the output of `python -m bitsandbytes` from your system?

### DavideRossi · 2024-06-20

That's interesting. It says `highest_compute_capability=(11, 0)` whereas my output says `highest_compute_capability=(9, 0)`. An NVidia hardware this fully depends on the GPU model, on ROCm I have no idea if it only depends on the hardware or also on the HIP/ROCm version...

### TimDettmers · 2026-02-21

Closing this issue. The diagnostics output you saw was from the legacy `CUDASetup` code, which has since been removed. ROCm support status and 8-bit quantization on ROCm are tracked in #47 and #1271. The `cublasLt` error on MI210 was a known issue related to hipBLAS compatibility that has been worked on in subsequent releases.

If you're still experiencing issues on the latest bitsandbytes with ROCm, please check #1271 for current status or open a new issue with updated environment details.
