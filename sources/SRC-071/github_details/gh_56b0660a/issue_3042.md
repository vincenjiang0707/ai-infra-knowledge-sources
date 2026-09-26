# [Issue #3042] [BUG] 屏障误删导致的共享内存的读写冲突

source: https://github.com/tile-ai/tilelang/issues/3042
state: closed | updated: 2026-08-31T17:41:10Z
labels: bug

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

0.1.12

### System information

root@s-113-2-32:/mnt/nas/home/jianpeng.zhu/project/vllm_torch_op/150s/git/tilelang# python3 -m torch.utils.collect_env
<frozen runpy>:128: RuntimeWarning: 'torch.utils.collect_env' found in sys.modules after import of package 'torch.utils', but prior to execution of 'torch.utils.collect_env'; this may result in unpredictable behaviour
Collecting environment information...
PyTorch version: 2.10.0
Is debug build: False
CUDA used to build PyTorch: 10.2
ROCM used to build PyTorch: N/A

OS: Ubuntu 24.04.2 LTS (x86_64)
GCC version: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0
Clang version: 22.1.0git (4.5.0.20260721 7b070f4f757e4199bcefb8b8e743b4000b81e366)
CMake version: version 4.4.0
Libc version: glibc-2.39

Python version: 3.12.11 (main, Jul 31 2025, 06:45:11) [GCC 13.3.0] (64-bit runtime)
Python platform: Linux-5.4.0-42-generic-x86_64-with-glibc2.39
Is CUDA available: True
CUDA runtime version: 10.2.89
CUDA_MODULE_LOADING set to: 
GPU models and configuration: Could not collect
Nvidia driver version: Could not collect
cuDNN version: Could not collect
Is XPU available: False
HIP runtime version: N/A
MIOpen runtime version: N/A
Is XNNPACK available: True
Caching allocator config: N/A

CPU:
Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Address sizes:                   46 bits physical, 57 bits virtual
Byte Order:                      Little Endian
CPU(s):                          160
On-line CPU(s) list:             0-159
Vendor ID:                       GenuineIntel
BIOS Vendor ID:                  Intel(R) Corporation
Model name:                      Intel(R) Xeon(R) Platinum 8380 CPU @ 2.30GHz
BIOS Model name:                 Intel(R) Xeon(R) Platinum 8380 CPU @ 2.30GHz  CPU @ 2.3GHz
BIOS CPU family:                 179
CPU family:                      6
Model:                           106
Thread(s) per core:              2
Core(s) per socket:              40
Socket(s):                       2
Stepping:                        6
CPU(s) scaling MHz:              24%
CPU max MHz:                     3400.0000
CPU min MHz:                     800.0000
BogoMIPS:                        4600.00
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm3dnowprefetch cpuid_fault epb cat_l3 invpcid_single ssbd mba ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid cqm rdt_a avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb intel_pt avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local wbnoinvd dtherm ida arat pln pts hwp hwp_act_window hwp_epp hwp_pkg_req avx512vbmi umip pku ospke avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid md_clear pconfig flush_l1d arch_capabilities
Virtualization:                  VT-x
L1d cache:                       3.8 MiB (80 instances)
L1i cache:                       2.5 MiB (80 instances)
L2 cache:                        100 MiB (80 instances)
L3 cache:                        120 MiB (2 instances)
NUMA node(s):                    2
NUMA node0 CPU(s):               0-39,80-119
NUMA node1 CPU(s):               40-79,120-159
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; Enhanced IBRS, IBPB conditional, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected

Versions of relevant libraries:
[pip3] numpy==1.26.4
[pip3] onnx==1.22.0
[pip3] onnxruntime-gpu==1.17.1+corex.4.5.0.20260721
[pip3] torch==2.10.0+corex.4.5.0.20260721
[pip3] torch_c_dlpack_ext==0.1.5
[pip3] torch_cluster==1.6.0+corex.4.5.0.20260721
[pip3] torch_quiver==0.1.0+corex.4.5.0.20260721
[pip3] torch_scatter==2.1.0+corex.4.5.0.20260721
[pip3] torch_sparse==0.6.16+corex.4.5.0.20260721
[pip3] torchaudio==2.10.0+corex.4.5.0.20260721
[pip3] torchdebug==4.4.0+corex.4.5.0.20260721
[pip3] torchvision==0.25.0+corex.4.5.0.20260721
[pip3] triton==3.2.0+corex.4.5.0.20260721

### Problem description

因为线程发散走到这个分支，这边的代码仅对then分支进行了是否删除屏障的判断，就将then和else的屏障都删除了，但else中如果存在共享内存的读写操作，会因此导致读写冲突


### Reproducible example code

The Python snippets:

```python

```


### Traceback

```pytb

```

### Expected behavior

_No response_

### Additional context

_No response_

## 评论 (3)

### kdywt · 2026-08-17

因为线程发散走到这个分支，这边的代码仅对then分支进行了是否删除屏障的判断，就将then和else的屏障都删除了，但else中如果存在共享内存的读写操作，会因此导致读写冲突
<img width="1993" height="997" alt="Image" src="https://github.com/user-attachments/assets/abd36166-a4a0-48db-9e3a-941b09f94202" />

### kdywt · 2026-08-17

我的修改方式

<img width="667" height="578" alt="Image" src="https://github.com/user-attachments/assets/bb64ea1f-ad53-42a2-86a6-3ee3562f44a9" />

### KellyFrog · 2026-08-25

Hi!

Thank you for your contribution.

It is appreciated to provide reproduce code / link to your PR instead of presenting screenshots.

If you are introducing a fix, link to a PR so we can review your changes. Do let us know if you have any ongoing progress.

Best regaurds.

