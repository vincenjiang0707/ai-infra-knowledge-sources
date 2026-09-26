source: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/mig-device-names.html

# MIG Device Names[#](https://docs.nvidia.com#mig-device-names)

By default, a MIG device consists of a single “GPU Instance” and a single “Compute Instance”. The following table highlights a naming convention to refer to a MIG device by its GPU Instance’s compute slice count and its total memory in GB (rather than just its memory slice count).

When only a single CI is created (that consumes the entire compute capacity of the GI), then the CI sizing is implied in the device name.

Note

The description below shows the profile names on the A100-SXM4-40GB product. For A100-SXM4-80GB, the profile names will change
according to the memory proportion - for example, `1g.10gb`

, `2g.20gb`

, `3g.40gb`

, `4g.40gb`

, `7g.80gb`

, respectively.

Memory |
20gb |
10gb |
5gb |
|---|---|---|---|
GPU Instance |
3g |
2g |
1g |
Compute Instance |
3c |
2c |
1c |
MIG Device |
3g.20gb |
2g.10gb |
1g.5gb |
GPC GPC GPC |
GPC GPC |
GPC |

Each GI can be further sub-divided into multiple CIs as required by users depending on their workloads. The following table highlights what the name of a MIG device would look like in this case. The example shown is for subdividing a 3g.20gb device into a set of sub-devices with different Compute Instance slice counts.

Memory |
20gb |
20gb |
|||
|---|---|---|---|---|---|
GPU Instance |
3g |
3g |
|||
Compute Instance |
1c |
1c |
1c |
2c |
1c |
MIG Device |
1c.3g.20gb |
1c.3g.20gb |
1c.3g.20gb |
2c.3g.20gb |
1c.3g.20gb |
GPC |
GPC |
GPC |
GPC GPC |
GPC |

## Device Enumeration[#](https://docs.nvidia.com#device-enumeration)

GPU Instances (GIs) and Compute Instances (CIs) are enumerated in the `/proc`

filesystem layout for MIG.

```
$ ls -l /proc/driver/nvidia-caps/
-r--r--r-- 1 root root 0 Nov 21 21:22 mig-minors
-r--r--r-- 1 root root 0 Nov 21 21:22 nvlink-minors
-r--r--r-- 1 root root 0 Nov 21 21:22 sys-minors
```

The corresponding device nodes (in `mig-minors`

) are created under `/dev/nvidia-caps`

. Refer to [CUDA Device Enumeration](https://docs.nvidia.com#cuda-device-enumeration) for more information.

## CUDA Device Enumeration[#](https://docs.nvidia.com#cuda-device-enumeration)

MIG supports running CUDA applications by specifying the CUDA device on which the application should be run. The CUDA device enumeration behavior has evolved across driver versions to provide better support and flexibility.

Starting with CUDA 12/R570, enumeration of a single compute instance (CI) per GPU instance (GI) is supported. In other words, a single CUDA process can enumerate across multiple GPU instances, but only one CI per GI. CUDA applications treat a CI and its parent GI as a single CUDA device. If several are visible, CUDA selects the first available.

**Caveats**

CUDA can only enumerate a single compute instance.

CUDA will enumerate a non-MIG GPU even if any compute instance is enumerated on any other GPU.

CUDA will only enumerate a single compute instance per GPU instance.

CUDA supports at most 64 MIG instances across all GPUs.


Note

Increase the open files limit above the common default of `1024`

using `ulimit -n <limit>`

.

These constraints may be relaxed in future NVIDIA driver releases for MIG.

**CUDA_VISIBLE_DEVICES and MIG**

`CUDA_VISIBLE_DEVICES`

has been extended to support MIG.You can specify compute instance UUIDs (at most one per GPU instance).

If multiple compute instances exist within a GPU instance and more than one are listed in

`CUDA_VISIBLE_DEVICES`

, CUDA will pick one from the list.If

`CUDA_VISIBLE_DEVICES`

is not set, CUDA will pick one from each GPU instance.

**Example: CI UUID assignment on H100 (R570 drivers)**

With the R570 NVIDIA datacenter drivers (470.42.01+), the example below shows how each CI is assigned GPU UUIDs in an H100 GPU:

```
$ nvidia-smi -L
GPU 0: NVIDIA H100 80GB HBM3 (UUID: GPU-c08d91cb-e324-655c-71ba-7570956445bc)
MIG 1c.3g.40gb Device 0: (UUID: MIG-c788539f-c1ea-5a36-8b4d-9b07d024b1bb)
MIG 1c.3g.40gb Device 1: (UUID: MIG-405bbda1-6b05-535f-9702-f95e8cd170ce)
MIG 1c.3g.40gb Device 2: (UUID: MIG-df7e5a27-eeea-51a0-9055-b36d5a552879)
MIG 1g.10gb Device 3: (UUID: MIG-b4b2228d-6933-5839-bc0e-41ab9edb61c6)
MIG 1g.10gb Device 4: (UUID: MIG-c71dc464-b9f9-5611-9d29-d601a47cffd6)
```

With CUDA 11/R450 and CUDA 12/R525, only enumeration of a single MIG instance is supported. In other words, regardless of how many MIG devices are created (or made available to a container), a single CUDA process can only enumerate a single MIG device.

CUDA applications treat a CI and its parent GI as a single CUDA device. CUDA is limited to use a single CI and will pick the first one available if several of them are visible. To summarize, there are two constraints:

CUDA can only enumerate a single compute instance

CUDA will not enumerate non-MIG GPU if any compute instance is enumerated on any other GPU


Note that these constraints may be relaxed in future NVIDIA driver releases for MIG. `CUDA_VISIBLE_DEVICES`

has been
extended to add support for MIG. Depending on the driver versions being used, two formats are supported:

With drivers >= R470 (470.42.01+), each MIG device is assigned a GPU UUID starting with

`MIG-<UUID>`

.With drivers < R470 (for example, R450 and R460), each MIG device is enumerated by specifying the CI and the corresponding parent GI. The format follows this convention:

`MIG-<GPU-UUID>/<GPU instance ID>/<compute instance ID>`

.

Note

With the R470 NVIDIA datacenter drivers (470.42.01+), the example below shows how MIG devices are assigned GPU UUIDs in an 8-GPU system with each GPU configured differently.

```
$ nvidia-smi -L
GPU 0: A100-SXM4-40GB (UUID: GPU-5d5ba0d6-d33d-2b2c-524d-9e3d8d2b8a77)
MIG 1g.5gb Device 0: (UUID: MIG-c6d4f1ef-42e4-5de3-91c7-45d71c87eb3f)
MIG 1g.5gb Device 1: (UUID: MIG-cba663e8-9bed-5b25-b243-5985ef7c9beb)
MIG 1g.5gb Device 2: (UUID: MIG-1e099852-3624-56c0-8064-c5db1211e44f)
MIG 1g.5gb Device 3: (UUID: MIG-8243111b-d4c4-587a-a96d-da04583b36e2)
MIG 1g.5gb Device 4: (UUID: MIG-169f1837-b996-59aa-9ed5-b0a3f99e88a6)
MIG 1g.5gb Device 5: (UUID: MIG-d5d0152c-e3f0-552c-abee-ebc0195e9f1d)
MIG 1g.5gb Device 6: (UUID: MIG-7df6b45c-a92d-5e09-8540-a6b389968c31)
GPU 1: A100-SXM4-40GB (UUID: GPU-0aa11ebd-627f-af3f-1a0d-4e1fd92fd7b0)
MIG 2g.10gb Device 0: (UUID: MIG-0c757cd7-e942-5726-a0b8-0e8fb7067135)
MIG 2g.10gb Device 1: (UUID: MIG-703fb6ed-3fa0-5e48-8e65-1c5bdcfe2202)
MIG 2g.10gb Device 2: (UUID: MIG-532453fc-0faa-5c3c-9709-a3fc2e76083d)
GPU 2: A100-SXM4-40GB (UUID: GPU-08279800-1cbe-a71d-f3e6-8f67e15ae54a)
MIG 3g.20gb Device 0: (UUID: MIG-aa232436-d5a6-5e39-b527-16f9b223cc46)
MIG 3g.20gb Device 1: (UUID: MIG-3b12da37-7fa2-596c-8655-62dab88f0b64)
GPU 3: A100-SXM4-40GB (UUID: GPU-71086aca-c858-d1e0-aae1-275bed1008b9)
MIG 7g.40gb Device 0: (UUID: MIG-3e209540-03e2-5edb-8798-51d4967218c9)
GPU 4: A100-SXM4-40GB (UUID: GPU-74fa9fb7-ccf6-8234-e597-7af8ace9a8f5)
MIG 1c.3g.20gb Device 0: (UUID: MIG-79c62632-04cc-574b-af7b-cb2e307120d8)
MIG 1c.3g.20gb Device 1: (UUID: MIG-4b3cc0fd-6876-50d7-a8ba-184a86e2b958)
MIG 1c.3g.20gb Device 2: (UUID: MIG-194837c7-0476-5b56-9c45-16bddc82e1cf)
MIG 1c.3g.20gb Device 3: (UUID: MIG-291820db-96a4-5463-8e7b-444c2d2e3dfa)
MIG 1c.3g.20gb Device 4: (UUID: MIG-5a97e28a-7809-5e93-abae-c3818c5ea801)
MIG 1c.3g.20gb Device 5: (UUID: MIG-3dfd5705-b18a-5a7c-bcee-d03a0ccb7a96)
GPU 5: A100-SXM4-40GB (UUID: GPU-3301e6dd-d38f-0eb5-4665-6c9659f320ff)
MIG 4g.20gb Device 0: (UUID: MIG-6d96b9f9-960e-5057-b5da-b8a35dc63aa8)
GPU 6: A100-SXM4-40GB (UUID: GPU-bb40ed7d-cbbb-d92c-50ac-24803cda52c5)
MIG 1c.7g.40gb Device 0: (UUID: MIG-66dd01d7-8cdb-5a13-a45d-c6eb0ee11810)
MIG 2c.7g.40gb Device 1: (UUID: MIG-03c649cb-e6ae-5284-8e94-4b1cf767e06c)
MIG 3c.7g.40gb Device 2: (UUID: MIG-8abf68e0-2808-525e-9133-ba81701ed6d3)
GPU 7: A100-SXM4-40GB (UUID: GPU-95fac899-e21a-0e44-b0fc-e4e3bf106feb)
MIG 4g.20gb Device 0: (UUID: MIG-219c765c-e07f-5b85-9c04-4afe174d83dd)
MIG 2g.10gb Device 1: (UUID: MIG-25884364-137e-52cc-a7e4-ecf3061c3ae1)
MIG 1g.5gb Device 2: (UUID: MIG-83e71a6c-f0c3-5dfc-8577-6e8b17885e1f)
```