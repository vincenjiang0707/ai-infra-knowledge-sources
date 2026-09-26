# [Issue #99] amd-smi static --partition Shows Only 63 GPUs After NPS4 Partitioning

source: https://github.com/ROCm/amdsmi/issues/99
state: closed | updated: 2025-07-21T15:43:07Z
labels: Under Investigation

## 正文

**Summary**
After applying NPS4 partitioning on an MI300X system with 64 GPUs,` amd-smi static --partition` only lists 63 GPUs. One GPU appears to be missing from the partitioning report.

**How to Reproduce**
1. Run `sudo amd-smi set --memory-partition NPS4` on a baremetal.
2. Then check `amd-smi static --partition`

**Actual Behavior**
```
GPU: 0
    PARTITION:
        COMPUTE_PARTITION: CPX
        MEMORY_PARTITION: NPS4
        PARTITION_ID: 0
...
...
GPU: 62
```

**Expected Behavior**
All 64 GPUs should appear in the output of` amd-smi static --partition`.

**System Info**
Dell PowerEdge XE9680 (MI300X)
CPU: 2 x Intel Xeon Platinum 8462Y+: 32c @ 2.8 GHz                                                                             
RAM: 2.0 TiB  NVMe: 124 TB                                                                                                     
GPUs: 8 x AMD MI300X

Kernel: Linux 5.15.0-142-generic
ROCm version: 6.4.1
AMDSMI Tool: 25.4.2+aca1101
AMDSMI Library: 25.4.0
amdgpu version: 6.12.12
VBIOS: AMD MI300X_HW_SRIOV_CVS_1VF (Version: 022.040.003.043.000001, Date: 2025/02/18)
OS: Ubuntu 22.04.5 LTS


**Additional Info**
We have also tried as per AMD's troubleshooting [guide](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/troubleshooting.html#all-64-gpus-not-visible-in-amd-smi-output-in-cpx-mode), but it did not work.


## 评论 (4)

### kentrussell · 2025-06-24

DRM has a limitation of 64 devices max. This was addressed in the patch set from https://lkml.org/lkml/2024/8/12/1076 , but will take time to make its way into the drm tree, and then be distributed by the various distros. 
The easiest workaround is to remove the onboard GPU, which is likely listed as GPU0. This could be Aspeed, Matrox, AMD, nvidia, Intel, etc. I usually just do a "sudo rmmod ast" or similar command to remove the module for whichever GPU that is, before modprobing amdgpu. If you're unsure which vendor the onboard GPU is, you can "cat /sys/class/drm/card0/device/vendor" and match that PCI ID up with the various vendors, to find the module to rmmod/blacklist. 
Unfortunately there's no other way to get around it without manually building your own monolithic kernel and libdrm with the required fixes included in both projects, and installing them. Either you have to remove the non-MI300 GPU (removing the module , physically remove the non-MI300 GPU, or remove it via PCI commands), or you have to get by with 63 AMD devices. 

EDIT: According to https://www.delltechnologies.com/asset/en-us/products/servers/technical-support/poweredge-xe9680-technical-guide.pdf, it should be a Matrox G200 GPU. I believe that you can remove that with "sudo rmmod mgag200" before "sudo modprobe amdgpu". Or modprobe.blacklist=mgag200 . 

### Bihan · 2025-06-25

@kentrussell Thanks. After removing Matrox G200 GPU it worked. Here is the sequence that worked for me
```
sudo rmmod mgag200
sudo modprobe amdgpu
sudo amd-smi set --memory-partition NPS4
```

### schung-amd · 2025-07-09

Hi @Bihan, as this seems to be resolved on your end, are we good to close this issue? 

### schung-amd · 2025-07-21

Closing for now, feel free to comment if further guidance is needed and we can reopen if necessary.
