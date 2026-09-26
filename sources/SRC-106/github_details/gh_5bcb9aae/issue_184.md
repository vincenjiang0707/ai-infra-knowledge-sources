# [Issue #184] /dev/dri/card1: Permission denied; owner=root(0):video(39);

source: https://github.com/ROCm/amdsmi/issues/184
state: closed | updated: 2026-04-09T15:18:42Z
labels: status: triage

## 正文

Since ROCm 7, amd-smi has a default command mimicking rocm-smi.
On an HPC machine with4 MI250X cards, rocm-smi works properly but amd-smi in ROCm 7 produces this error:
```
$ amd-smi
RuntimeError: WARNING: User is missing the following required groups: render, video. Please add user to these groups.
```
This seems weird as we never had to add this kind of group for the system to work properly, AFAIK, all other user level component of ROCm 7 work properly without these groups.

In ROCm 7.1.1 the error is still present but not as fatal:
```
$ amd-smi
Permission needed to access required GPU device node(s):
  - /dev/dri/card0: Permission denied; owner=root(0):video(39);
  - /dev/dri/card1: Permission denied; owner=root(0):video(39);
  - /dev/dri/card2: Permission denied; owner=root(0):video(39);
  - /dev/dri/card3: Permission denied; owner=root(0):video(39);
  - /dev/dri/card4: Permission denied; owner=root(0):video(39);
  - /dev/dri/card5: Permission denied; owner=root(0):video(39);
  - /dev/dri/card6: Permission denied; owner=root(0):video(39);
  - /dev/dri/card7: Permission denied; owner=root(0):video(39);

You can try:
  • Add your user to the group that owns these devices:
      sudo usermod -aG <group> "$USER"

+------------------------------------------------------------------------------+
| AMD-SMI 26.2.0+021c61fc      amdgpu version: 6.12.12  ROCm version: 7.1.1    |
| VBIOS version: 020.040.000.040.000000                                        |
| Platform: Linux Baremetal                                                    |
|-------------------------------------+----------------------------------------|
| BDF                        GPU-Name | Mem-Uti   Temp   UEC       Power-Usage |
| GPU  HIP-ID  OAM-ID  Partition-Mode | GFX-Uti    Fan               Mem-Usage |
|=====================================+========================================|
| 0000:c1:00.0    AMD Instinct MI250X | 0 %      44 °C   0            94/560 W |
|   0       0       0             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:c6:00.0    AMD Instinct MI250X | 0 %      45 °C   0               0/0 W |
|   1       1       1             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:c9:00.0    AMD Instinct MI250X | 0 %      48 °C   0            93/560 W |
|   2       2       2             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:ce:00.0    AMD Instinct MI250X | 0 %      50 °C   0               0/0 W |
|   3       3       3             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:d1:00.0    AMD Instinct MI250X | 0 %      43 °C   0            90/560 W |
|   4       4       4             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:d6:00.0    AMD Instinct MI250X | 0 %      46 °C   0               0/0 W |
|   5       5       5             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:d9:00.0    AMD Instinct MI250X | 0 %      47 °C   0            91/560 W |
|   6       6       6             N/A | 0 %        N/A             10/65520 MB |
|-------------------------------------+----------------------------------------|
| 0000:de:00.0    AMD Instinct MI250X | 0 %      52 °C   0               0/0 W |
|   7       7       7             N/A | 0 %        N/A             10/65520 MB |
+-------------------------------------+----------------------------------------+
+------------------------------------------------------------------------------+
| Processes:                                                                   |
|  GPU        PID  Process Name          GTT_MEM  VRAM_MEM  MEM_USAGE     CU % |
|==============================================================================|
|  No running processes found                                                  |
+------------------------------------------------------------------------------+
```

Would you mind explaining what requires this group, why rocm-smi didnt complain and if adding the group is really necessary.

Regards.

## 评论 (4)

### darren-amd · 2026-03-26

Hi @etiennemlb,

Thanks for reporting the issue! Some information does not require being added to these groups, but a subset of queries, such as queries related to VRAM require access to the `/dev/dri/renderD*` or `/dev/dr/card*` nodes, which require being added to the video/render groups. 

We have an official recommendation in our documentation when installing ROCm: [Configuring permissions for GPU access](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html#configuring-permissions-for-gpu-access), so I would recommend adding yourself to the group.

### etiennemlb · 2026-03-26

OK thanks, is there a doc where I could read the kind of info provided by these files?
These files do not seem necessary for most apps to work properly, and until amd smi it was not even noticed to be significant.

On 26 March 2026 19:17:10 UTC, darren-amd ***@***.***> wrote:
>darren-amd left a comment (ROCm/amdsmi#184)
>
>Hi @etiennemlb,
>
>Thanks for reporting the issue! Some information does not require being added to these groups, but a subset of queries, such as queries related to VRAM require access to the `/dev/dri/renderD*` or `/dev/dr/card*` nodes, which require being added to the video/render groups. 
>
>We have an official recommendation in our documentation when installing ROCm: [Configuring permissions for GPU access](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html#configuring-permissions-for-gpu-access), so I would recommend adding yourself to the group.
>


### darren-amd · 2026-03-31

Hi @etiennemlb,

We don't have explicit documentation on this but I found some documentation online which may be helpful: [render nodes](https://www.kernel.org/doc/html/latest/gpu/drm-uapi.html#render-nodes) and [drm](https://man.archlinux.org/man/drm.7.en). A lot of components probably wouldn't need access to `/dev/dri/renderD*` or `/dev/dri/card*` nodes so technically if you use case doesn't need it directly you would not need to add yourself to the group. 

### darren-amd · 2026-04-09

Going to close this off but please feel to let me know if you have more questions, thanks!
