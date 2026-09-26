# [Issue #1464] [ROCm] [Stable diffusion LoRA training, sd-scripts] Error invalid device function at line 224 in file /src/csrc/ops.hip

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1464
state: closed | updated: 2026-02-21T20:10:05Z
labels: ROCm

## 正文

### System Info

### Resume
ROCm 6.2.4 + Linux Ubuntu 22.04.5 LTS, Using latest Pytorch Preview (Nightly) version.
AMD® Radeon graphics / AMD® Radeon rx 6700 xt

### Versions

OS: Ubuntu 22.04.5 LTS (x86_64)
GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
Clang version: Could not collect
CMake version: version 3.22.1
Libc version: glibc-2.35

Python version: 3.10.12 (main, Nov 6 2024, 20:22:13) [GCC 11.4.0] (64-bit runtime)
Python platform: Linux-6.8.0-49-generic-x86_64-with-glibc2.35
Is CUDA available: False
CUDA runtime version: No CUDA
CUDA_MODULE_LOADING set to: N/A
GPU models and configuration: No CUDA
Nvidia driver version: No CUDA
cuDNN version: No CUDA
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True

CPU:
Arquitectura: x86_64
modo(s) de operación de las CPUs: 32-bit, 64-bit
Address sizes: 48 bits physical, 48 bits virtual
Orden de los bytes: Little Endian
CPU(s): 16
Lista de la(s) CPU(s) en línea: 0-15
ID de fabricante: AuthenticAMD
Nombre del modelo: AMD Ryzen 7 5700G with Radeon Graphics
Familia de CPU: 25
Modelo: 80
Hilo(s) de procesamiento por núcleo: 2
Núcleo(s) por «socket»: 8
«Socket(s)» 1
Revisión: 0
CPU MHz máx.: 4673,0000
CPU MHz mín.: 400,0000
BogoMIPS: 7600.24
Indicadores: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl nonstop_tsc cpuid extd_apicid aperfmperf rapl pni pclmulqdq monitor ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand lahf_lm cmp_legacy svm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ibs skinit wdt tce topoext perfctr_core perfctr_nb bpext perfctr_llc mwaitx cpb cat_l3 cdp_l3 hw_pstate ssbd mba ibrs ibpb stibp vmmcall fsgsbase bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a rdseed adx smap clflushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local user_shstk clzero irperf xsaveerptr rdpru wbnoinvd cppc arat npt lbrv svm_lock nrip_save tsc_scale vmcb_clean flushbyasid decodeassists pausefilter pfthreshold avic v_vmsave_vmload vgif v_spec_ctrl umip pku ospke vaes vpclmulqdq rdpid overflow_recov succor smca fsrm debug_swap
Virtualización: AMD-V
Caché L1d: 256 KiB (8 instances)
Caché L1i: 256 KiB (8 instances)
Caché L2: 4 MiB (8 instances)
Caché L3: 16 MiB (1 instance)
Modo(s) NUMA: 1
CPU(s) del nodo NUMA 0: 0-15
Vulnerability Gather data sampling: Not affected
Vulnerability Itlb multihit: Not affected
Vulnerability L1tf: Not affected
Vulnerability Mds: Not affected
Vulnerability Meltdown: Not affected
Vulnerability Mmio stale data: Not affected
Vulnerability Reg file data sampling: Not affected
Vulnerability Retbleed: Not affected
Vulnerability Spec rstack overflow: Vulnerable: Safe RET, no microcode
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl
Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2: Mitigation; Retpolines; IBPB conditional; IBRS_FW; STIBP always-on; RSB filling; PBRSB-eIBRS Not affected; BHI Not affected
Vulnerability Srbds: Not affected
Vulnerability Tsx async abort: Not affected

Versions of relevant libraries:
[pip3] numpy==2.2.0
[pip3] nvidia-cublas-cu12==12.4.5.8
[pip3] nvidia-cuda-cupti-cu12==12.4.127
[pip3] nvidia-cuda-nvrtc-cu12==12.4.127
[pip3] nvidia-cuda-runtime-cu12==12.4.127
[pip3] nvidia-cudnn-cu12==9.1.0.70
[pip3] nvidia-cufft-cu12==11.2.1.3
[pip3] nvidia-curand-cu12==10.3.5.147
[pip3] nvidia-cusolver-cu12==11.6.1.9
[pip3] nvidia-cusparse-cu12==12.3.1.170
[pip3] nvidia-nccl-cu12==2.21.5
[pip3] nvidia-nvjitlink-cu12==12.4.127
[pip3] nvidia-nvtx-cu12==12.4.127
[pip3] torch==2.5.1
[pip3] triton==3.1.0

### Reproduction

### How to reproduce it
Just try to train using any optimizer that bitsandbytes adds, for example in this case the one that is trying to be used is AdamW-8bits.

### Error
```
UserWarning: Attempting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas (Triggered internally at /pytorch/aten/src/ATen/Context.cpp:310.)
  return F.linear(input, self.weight, self.bias)
steps:   0%|                          | 0/1358 [03:45<?, ?it/s, avr_loss=0.0248]

Error invalid device function at line 224 in file /src/csrc/ops.hip
Traceback (most recent call last):
  File "/home/santi-linux/.local/bin/accelerate", line 8, in <module>
    sys.exit(main())
  File "/home/santi-linux/.local/lib/python3.10/site-packages/accelerate/commands/accelerate_cli.py", line 46, in main
    args.func(args)
  File "/home/santi-linux/.local/lib/python3.10/site-packages/accelerate/commands/launch.py", line 1082, in launch_command
    simple_launcher(args)
  File "/home/santi-linux/.local/lib/python3.10/site-packages/accelerate/commands/launch.py", line 688, in simple_launcher
    raise subprocess.CalledProcessError(returncode=process.returncode, cmd=cmd)
subprocess.CalledProcessError: Command '['/usr/bin/python3', 'sdxl_train_network.py', '--config_file=/home/santi-linux/trainer_kohya_ss/train_network_SDXL_AdamW.toml']' returned non-zero exit status 1.
```
### More info
I was sent here to report this issue since I previously thought it was a PyTorch issue. Here's the issue I opened at PyTorch's repo:
https://github.com/pytorch/pytorch/issues/143718


### Expected behavior

What's expected to happen is to make the training steps to ocurr without a single error. When I was on ROCm 6.1, it used to work flawlessly. I was using this non-official bitsandbytes repo, though: https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6 but it worked flawlessly. 

Now it's a different story. I'm currently using ROCm 6.2.4 + latest PyTorch version, and I had to upgrade everything so I could be able to use newer versions of sd-scritps. 

I've made sure to install bitsandbytes correctly using 
```
cmake -DCOMPUTE_BACKEND=hip -S . -DBNB_ROCM_ARCH="gfx1030"
```
, just as the HF repo instructions indicated. Setting it gfx1030 worked for me (it used to work just fine, months ago when I was on ROCm 6.1.2 + PyTorch 2.3.1, and I was also using the unofficial repo of arlo-phoenix). 
I'm also already using 
```
export HSA_OVERRIDE_GFX_VERSION=10.3.0
```
for the launch script I have.

I do also tried to downgrade bitsandbytes to arlo-phoenix's repo while keeping my current ROCm 6.2.4 + Latest PyTorch Nightly, but I get the same Invalid device function Error. I ALSO tried with Pytorch 2.5.1 and 2.4.1 but they didn't worked for me, and I can't use 2.3.1 anymore since the minimum requirements for sd-scripts now is 2.4.0.

## 评论 (3)

### fluidnumericsJoe · 2025-03-26

Hey @devsantiagoweb - I'm attempting to reproduce the issue on my side at the moment (compiling bitsandbytes now). Can you share the output of `rocminfo` and `rocm-smi` ?

Additionally,  I think it might be helpful to set `AMD_LOG_LEVEL=3` to trace the ROCr Runtime log, then combine it with `HSAKMT_DEBUG_LEVEL=4` o check the HSA/Thunk interface log to pin point the error segment and see what we can do from there. Can you set those environment variables and post the logs here ?

Last, to make it easy to help, can you share a reproducer that we can run ?



### bghira · 2025-04-04

i went to provide the requested info but it turns out that kernel builtin amdgpu is incompatible with these tools, they fail once they can't find a module loaded 🙈 

### TimDettmers · 2026-02-21

Closing this issue. The `invalid device function` error on ROCm typically means the binary was not compiled for your GPU architecture (RX 6700 XT / gfx1031). Additionally, `torch.utils.collect_env` showed `Is CUDA available: False`, suggesting the ROCm/PyTorch integration was not fully functional in your environment.

Please ensure you have a ROCm-compatible PyTorch build that recognizes your GPU (`torch.cuda.is_available()` should return True). If you're still hitting issues on the latest bitsandbytes and ROCm versions, please open a new issue with updated environment details.
