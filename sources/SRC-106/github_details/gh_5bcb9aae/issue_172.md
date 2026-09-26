# [Issue #172] `amdgpu not found in modules` (i have it built into the kernel)

source: https://github.com/ROCm/amdsmi/issues/172
state: closed | updated: 2026-02-05T17:37:28Z
labels: status: triage

## 正文

debian 13

`amd-smi` cannot find `amdgpu` in modules

but i have `amdgpu` built directly into the kernel, **_not as a module_**

```
./amd-smi 
ERROR:root:Unable to get devices, driver not initialized (amdgpu not found in modules)
ERROR:root:Unable to detect any GPU devices, check amdgpu version and module status (sudo modprobe amdgpu)
ERROR:root:Unable to detect any CPU devices, check amd_hsmp (or) hsmp_acpi version and module status (sudo modprobe amd_hsmp (or) sudo modprobe hsmp_acpi)
AMDSMI Tool: 26.1.0+b5522cc8 | AMDSMI Library version: 26.1.0 | ROCm version: N/A
```

note also: the current version of `rocm-smi` from the debian 13 repository throws the same error, looking for amdgpu module

but my kernel has it builtin, not as a module

however, if i just set `driverInitialized()` to `True` in `/usr/bin/rocm-smi`, then `rocm-smi` shows GPU info and works (this issue seems fixed in upstream rocm-smi git)

## 评论 (5)

### hairetikos · 2026-01-17

to clarify, i set `CONFIG_DRM_AMDGPU=y` (default is [m]) when building the linux kernel

i notice `amd-smi` is trying to check `/sys/module/amdgpu/initstate` to determine if the amdgpu driver is initialized:  https://github.com/ROCm/amdsmi/blob/b5522cc8141a7241b22bebab639851074463f00f/amdsmi_cli/amdsmi_init.py#L57

however, on my system, this is what i have @ `/sys/module/amdgpu/` :

```
drwxr-xr-x   2 root root    0 Jan 17 16:49 drivers
drwxr-xr-x   2 root root    0 Jan 17 16:49 parameters
--w-------   1 root root 4.0K Jan 17 16:49 uevent
```

the driver is indeed loaded, dxvk works playing some windows games, etc.  but amd-smi fails.


i think `initstate` is only available for loaded modules, not builtin drivers.

to quote a stackexchange:
> I think that only loaded modules have an initstate file in their /sys/module directory
https://unix.stackexchange.com/questions/225706/are-modules-listed-under-sys-module-all-the-loaded-modules

### hairetikos · 2026-01-17

hi, i just made this change, it may not be the most elegant solution but it now works on my end:

https://github.com/ROCm/amdsmi/compare/amd-mainline...hairetikos:amdsmi:patch-1

essentially: if the `amdgpu` module `initstate` cannot be found, check `/sys/class/drm` to see if it has `amdgpu` builtin to the kernel and an AMD GPU is there)
```
./amd-smi 
+------------------------------------------------------------------------------+
| AMD-SMI 26.1.0+b5522cc8-d... amdgpu version: Linuxver ROCm version: N/A      |
| VBIOS version: 00076350                                                      |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:2f:00.0 AMD Radeon RX 7900 XTX | 1 %      43 °C   0            10/315 W |
|   0       0     N/A             N/A | 1 %      0.0 %           2192/24560 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
```

### kentrussell · 2026-01-19

@marifamd  How do you think you'd handle this? amdgpu isn't a module, but it's loaded. Is there anything SMI can do to work around that case, or does SMI have a dependency on amdgpu's module-ness?

### marifamd · 2026-01-20

Wasn't aware this was an issue, the patch looks good from a first glance. @hairetikos Can you please post as a PR in https://github.com/ROCm/rocm-systems/tree/develop/projects/amdsmi and I will make some edits and write some test cases for this as well.

### hairetikos · 2026-01-20

@marifamd thanks, i made the PR: https://github.com/ROCm/rocm-systems/pull/2689
