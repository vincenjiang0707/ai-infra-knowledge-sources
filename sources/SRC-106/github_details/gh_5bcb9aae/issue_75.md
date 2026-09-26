# [Issue #75] [Issue]:  amd-smi --version | Unable to get devices, driver not initialized (amdgpu not found in modules)

source: https://github.com/ROCm/amdsmi/issues/75
state: closed | updated: 2026-01-19T15:31:20Z
labels: Under Investigation

## 正文

### Problem Description

In WSL2 , Dirver 25.1.1
use amd-smi --version commend
```
ERROR: Unable to get devices, driver not initialized (amdgpu not found in modules)
ERROR: Unable to detect any GPU devices, check amdgpu version and module status (sudo modprobe amdgpu)
ERROR: Unable to detect any CPU devices, check amd_hsmp version and module status (sudo modprobe amd_hsmp)
```
use rocminfo commend normally
```
WSL environment detected.
=====================
HSA System Attributes
=====================
Runtime Version:         1.1
Runtime Ext Version:     1.6
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    AMD Ryzen 9 7900X 12-Core Processor
  Uuid:                    CPU-XX
  Marketing Name:          AMD Ryzen 9 7900X 12-Core Processor
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      32768(0x8000) KB
  Chip ID:                 0(0x0)
  Cacheline Size:          64(0x40)
  Internal Node ID:        0
  Compute Unit:            24
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    32660996(0x1f25e04) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    32660996(0x1f25e04) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    32660996(0x1f25e04) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 4
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    32660996(0x1f25e04) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    gfx1100
  Marketing Name:          AMD Radeon RX 7900 XTX
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      6144(0x1800) KB
    L3:                      98304(0x18000) KB
  Chip ID:                 29772(0x744c)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2482
  Internal Node ID:        1
  Compute Unit:            96
  SIMDs per CU:            2
  Shader Engines:          6
  Shader Arrs. per Eng.:   2
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          32(0x20)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    1024(0x400)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 232
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    25079652(0x17eaf64) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    25079652(0x17eaf64) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx1100
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***
```

### Operating System

22.04

### CPU

AMD 7900X

### GPU

RX 7900 XTX

### ROCm Version

ROCm 6.3.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (7)

### ppanchad-amd · 2025-02-24

Hi @yihuishou. Internal ticket has been created to investigate this issue. Thanks!

### schung-amd · 2025-02-24

Hi @yihuishou, `amd-smi` is not supported in WSL so this is expected. Let me know if you need further guidance related to this.

### yihuishou · 2025-02-25

Well, ROCm not full support windows and not full support wsl... so, this is the prices of the use AMD？

### schung-amd · 2025-02-25

This is just due to how the driver is passed through to WSL, not really an indication of lack of support. This doesn't break core ROCm functionality, but there are a few applications which use `amd-smi` or `rocm-smi` internally to get GPU info which will not function correctly on WSL. We're currently working on adding some `amd-smi` features on WSL to address this issue.

### hairetikos · 2026-01-15

hi, same error here, but on Debian Linux 13

i have `amdgpu` built into the kernel, **_not as a module_**, i think that is where the problem is

```
ERROR:root:Unable to get devices, driver not initialized (amdgpu not found in modules)
ERROR:root:Unable to detect any GPU devices, check amdgpu version and module status (sudo modprobe amdgpu)
ERROR:root:Unable to detect any CPU devices, check amd_hsmp (or) hsmp_acpi version and module status (sudo modprobe amd_hsmp (or) sudo modprobe hsmp_acpi)
AMDSMI Tool: 26.1.0+b5522cc8 | AMDSMI Library version: 26.1.0 | ROCm version: N/A

```

it is assuming a module, but i have it directly built into the kernel...

### schung-amd · 2026-01-15

That's normal in WSL, the driver is passed through so `amdgpu` won't be loaded. Again, we don't have `amd-smi` support in WSL, so this is expected to fail. We have added some APIs related to `amd-smi` functions so that applications relying on `amd-smi` features may have workarounds available on WSL, but `amd-smi` itself will still not function.

> i have amdgpu built into the kernel, not as a module

This is also normal, the error messages refer to a kernel module. In a native environment even without ROCm installed (i.e. using the built-in kernel driver) you should see it loaded with `lsmod | grep amdgpu`. If for some reason you don't see it loaded you can manually load the driver with `modprobe amdgpu`, but as noted this will not work in WSL.

### hairetikos · 2026-01-17

@schung-amd just to clarify:  i am not using WSL.  i have opened a fresh issue for this, as its not related to WSL:  https://github.com/ROCm/amdsmi/issues/172

i use debian, i compile the Linux kernel with the `amdgpu` driver built _into_ the kernel (setting [y] not [m]):

`CONFIG_DRM_AMDGPU=y`

therefore `lsmod | grep amdgpu` will show nothing.

`lsmod` does not list anything that is built with option [y] in the compiled kernel.  it lists modules only,things  set to [m] when compiling the linux kernel

therefore, `amd-smi` will fail to find the module `initstate`, because it is not a module, it is built into the kernel here.
