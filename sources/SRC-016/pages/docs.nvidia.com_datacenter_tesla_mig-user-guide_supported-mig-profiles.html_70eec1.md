source: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html

# Supported MIG Profiles[#](https://docs.nvidia.com#supported-mig-profiles)

This section provides an overview of the supported profiles and possible placements of the MIG profiles on supported GPUs.

## B200 MIG Profiles[#](https://docs.nvidia.com#b200-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA B200:

The following table shows the supported profiles on the B200 180 GB product.

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances |
||
|---|---|---|---|---|---|---|---|---|
NVDEC |
JPEG |
OFA |
||||||
MIG 1g.23gb |
1/8 |
1/7 |
1 |
1 |
0 |
1/8 |
2 |
7 |
MIG 1g.23gb+me |
1/8 |
1/7 |
1 |
1 |
1 |
1/8 |
2 |
1 (A single 1g profile can include media extensions) |
MIG 1g.45gb |
2/8 |
1/7 |
1 |
1 |
0 |
2/8 |
2 |
4 |
MIG 2g.45gb |
2/8 |
2/7 |
1 |
1 |
0 |
2/8 |
3 |
3 |
MIG 3g.90gb |
4/8 |
3/7 |
1 |
1 |
0 |
4/8 |
6 |
2 |
MIG 4g.90gb |
4/8 |
4/7 |
1 |
1 |
0 |
4/8 |
8 |
1 |
MIG 7g.180gb |
Full |
Full |
1 |
1 |
1 |
Full |
16 |
1 |

## RTX PRO 6000 Blackwell MIG Profiles[#](https://docs.nvidia.com#rtx-pro-6000-blackwell-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA RTX PRO 6000 Blackwell Workstation Edition, Max-Q Workstation Edition, and RTX PRO 6000 Blackwell Server Edition:

The following table shows the supported profiles on the RTX PRO 6000 Blackwell Workstation Edition, Max-Q Workstation Edition, and RTX PRO 6000 Blackwell Server Edition 96GB products:

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances |
|||
|---|---|---|---|---|---|---|---|---|---|
NVDEC |
NVENC |
JPEG |
OFA |
||||||
MIG 1g.24gb |
1/4 |
1/4 |
1 |
1 |
1 |
0 |
1/4 |
1 |
4 |
MIG 1g.24gb+me |
1/4 |
1/4 |
1 |
1 |
1 |
1 |
1/4 |
1 |
1 |
MIG 1g.24gb+gfx |
1/4 |
1/4 |
1 |
1 |
1 |
0 |
1/4 |
1 |
4 |
MIG 1g.24gb+me.all |
1/4 |
1/4 |
4 |
4 |
4 |
1 |
1/4 |
1 |
1 |
MIG 1g.24gb-me |
1/4 |
1/4 |
0 |
0 |
0 |
0 |
1/4 |
1 |
4 |
MIG 2g.48gb |
1/2 |
1/2 |
2 |
2 |
2 |
0 |
1/2 |
2 |
2 |
MIG 2g.48gb+gfx |
1/2 |
1/2 |
2 |
2 |
2 |
0 |
1/2 |
2 |
2 |
MIG 2g.48gb+me.all |
1/2 |
1/2 |
4 |
4 |
4 |
1 |
1/2 |
2 |
1 |
MIG 2g.48gb-me |
1/2 |
1/2 |
0 |
0 |
0 |
0 |
1/2 |
2 |
2 |
MIG 4g.96gb |
Full |
Full |
4 |
4 |
4 |
1 |
Full |
4 |
1 |
MIG 4g.96gb+gfx |
Full |
Full |
4 |
4 |
4 |
1 |
Full |
4 |
1 |

## RTX PRO 5000 Blackwell MIG Profiles[#](https://docs.nvidia.com#rtx-pro-5000-blackwell-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA RTX PRO 5000 Blackwell:

The following table shows the supported profiles on the RTX PRO 5000 Blackwell 48GB products:

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances |
|||
|---|---|---|---|---|---|---|---|---|---|
NVDEC |
NVENC |
JPEG |
OFA |
||||||
MIG 1g.24gb |
1/2 |
1/2 |
1 |
1 |
0 |
0 |
1/2 |
1 |
2 |
MIG 1g.24gb+me |
1/2 |
1/2 |
1 |
1 |
1 |
1 |
1/2 |
1 |
1 |
MIG 1g.24gb+gfx |
1/2 |
1/2 |
1 |
1 |
0 |
0 |
1/2 |
1 |
2 |
MIG 1g.24gb+me.all |
1/2 |
1/2 |
3 |
3 |
1 |
1 |
1/2 |
1 |
1 |
MIG 1g.24gb-me |
1/2 |
1/2 |
0 |
0 |
0 |
0 |
1/2 |
1 |
2 |
MIG 2g.48gb |
Full |
Full |
3 |
3 |
1 |
1 |
Full |
4 |
1 |
MIG 2g.48gb+gfx |
Full |
Full |
3 |
3 |
1 |
1 |
Full |
4 |
1 |

## RTX PRO 4500 Blackwell MIG Profiles[#](https://docs.nvidia.com#rtx-pro-4500-blackwell-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA RTX PRO 4500 Blackwell:

The following table shows the supported profiles on the RTX PRO 4500 Blackwell 32GB products:

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances |
|||
|---|---|---|---|---|---|---|---|---|---|
NVDEC |
NVENC |
JPEG |
OFA |
||||||
MIG 1g.16gb |
1/2 |
1/2 |
1 |
1 |
1 |
0 |
1/2 |
1 |
2 |
MIG 1g.16gb+gfx |
1/2 |
1/2 |
1 |
1 |
1 |
0 |
1/2 |
1 |
2 |
MIG 1g.16gb+me.all |
1/2 |
1/2 |
3 |
3 |
2 |
1 |
1/2 |
1 |
1 |
MIG 1g.16gb-me |
1/2 |
1/2 |
0 |
0 |
0 |
0 |
1/2 |
1 |
2 |
MIG 2g.32gb |
Full |
Full |
3 |
3 |
2 |
1 |
Full |
2 |
1 |
MIG 2g.32gb+gfx |
Full |
Full |
3 |
3 |
2 |
1 |
Full |
2 |
1 |

## Thor iGPU MIG Profiles[#](https://docs.nvidia.com#thor-igpu-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA Thor iGPU:

The following table shows the supported profiles on the NVIDIA Thor iGPU (GB10B).

Note

The Thor iGPU uses unified system memory shared with the CPU. There is no dedicated video memory, so all profiles report 0 GB. Memory bandwidth is proportional to the instance size.

At most two MIG instances can coexist simultaneously: one compute instance and one
graphics (`+gfx`

) instance. The full `3g.0gb`

profile cannot coexist with any
other instance.

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances |
|||
|---|---|---|---|---|---|---|---|---|---|
NVDEC |
NVENC |
JPEG |
OFA |
||||||
MIG 1g.0gb+me |
N/A |
~1/3 |
1 |
1 |
1 |
1 |
~1/3 |
1 |
1 |
MIG 1g.0gb |
N/A |
~1/3 |
1 |
1 |
1 |
0 |
~1/3 |
1 |
1 |
MIG 1g.0gb+gfx |
N/A |
~1/3 |
1 |
1 |
1 |
0 |
~1/3 |
1 |
1 |
MIG 2g.0gb |
N/A |
~2/3 |
1 |
1 |
1 |
0 |
~2/3 |
1 |
1 |
MIG 2g.0gb+gfx |
N/A |
~2/3 |
1 |
1 |
1 |
0 |
~2/3 |
1 |
1 |
MIG 3g.0gb |
N/A |
Full |
2 |
2 |
2 |
1 |
Full |
1 |
1 |
MIG 3g.0gb+gfx |
N/A |
Full |
2 |
2 |
2 |
1 |
Full |
1 |
1 |

## H100 MIG Profiles[#](https://docs.nvidia.com#h100-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA H100:

The following table shows the supported profiles on the H100 80GB product (PCIe and SXM5).

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances Available |
|---|---|---|---|---|---|---|
MIG 1g.10gb |
1/8 |
1/7 |
1 NVDEC /1 JPEG /0 OFA |
1/8 |
1 |
7 |
MIG 1g.10gb+me |
1/8 |
1/7 |
1 NVDEC /1 JPEG /1 OFA |
1/8 |
1 |
1 (A single 1g profile can include media extensions) |
MIG 1g.20gb |
1/4 |
1/7 |
1 NVDEC /1 JPEG /0 OFA |
1/8 |
1 |
4 |
MIG 2g.20gb |
2/8 |
2/7 |
2 NVDECs /2 JPEG /0 OFA |
2/8 |
2 |
3 |
MIG 3g.40gb |
4/8 |
3/7 |
3 NVDECs /3 JPEG /0 OFA |
4/8 |
3 |
2 |
MIG 4g.40gb |
4/8 |
4/7 |
4 NVDECs /4 JPEG /0 OFA |
4/8 |
4 |
1 |
MIG 7g.80gb |
Full |
7/7 |
7 NVDECs /7 JPEG /1 OFA |
Full |
8 |
1 |

The following table shows the supported profiles on the H100 94GB product (PCIe and SXM5).

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances Available |
|---|---|---|---|---|---|---|
MIG 1g.12gb |
1/8 |
1/7 |
1 NVDEC /1 JPEG /0 OFA |
1/8 |
1 |
7 |
MIG 1g.12gb+me |
1/8 |
1/7 |
1 NVDEC /1 JPEG /1 OFA |
1/8 |
1 |
1 (A single 1g profile can include media extensions) |
MIG 1g.24gb |
1/4 |
1/7 |
1 NVDEC /1 JPEG /0 OFA |
1/8 |
1 |
4 |
MIG 2g.24gb |
2/8 |
2/7 |
2 NVDECs /2 JPEG /0 OFA |
2/8 |
2 |
3 |
MIG 3g.47gb |
4/8 |
3/7 |
3 NVDECs /3 JPEG /0 OFA |
4/8 |
3 |
2 |
MIG 4g.47gb |
4/8 |
4/7 |
4 NVDECs /4 JPEG /0 OFA |
4/8 |
4 |
1 |
MIG 7g.94gb |
Full |
7/7 |
7 NVDECs /7 JPEG /1 OFA |
Full |
8 |
1 |

The following table shows the supported profiles on the H100 96GB product (H100 on GH200).

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances Available |
|---|---|---|---|---|---|---|
MIG 1g.12gb |
1/8 |
1/7 |
1 NVDEC /1 JPEG /0 OFA |
1/8 |
1 |
7 |
MIG 1g.12gb+me |
1/8 |
1/7 |
1 NVDEC /1 JPEG /1 OFA |
1/8 |
1 |
1 (A single 1g profile can include media extensions) |
MIG 1g.24gb |
1/4 |
1/7 |
1 NVDEC /1 JPEG /0 OFA |
1/8 |
1 |
4 |
MIG 2g.24gb |
2/8 |
2/7 |
2 NVDECs /2 JPEG /0 OFA |
2/8 |
2 |
3 |
MIG 3g.48gb |
4/8 |
3/7 |
3 NVDECs /3 JPEG /0 OFA |
4/8 |
3 |
2 |
MIG 4g.48gb |
4/8 |
4/7 |
4 NVDECs /4 JPEG /0 OFA |
4/8 |
4 |
1 |
MIG 7g.96gb |
Full |
7/7 |
7 NVDECs /7 JPEG /1 OFA |
Full |
8 |
1 |

## H200 MIG Profiles[#](https://docs.nvidia.com#h200-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA H200:

The following table shows the supported profiles on the H200 141GB product.

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances Available |
|---|---|---|---|---|---|---|
MIG 1g.18gb |
1/8 |
1/7 |
1 NVDECs /1 JPEG /0 OFA |
1/8 |
1 |
7 |
MIG 1g.18gb+me |
1/8 |
1/7 |
1 NVDEC /1 JPEG /1 OFA |
1/8 |
1 |
1 (A single 1g profile can include media extensions) |
MIG 1g.35gb |
1/4 |
1/7 |
1 NVDECs /1 JPEG /0 OFA |
1/8 |
1 |
4 |
MIG 2g.35gb |
2/8 |
2/7 |
2 NVDECs /2 JPEG /0 OFA |
2/8 |
2 |
3 |
MIG 3g.71gb |
4/8 |
3/7 |
3 NVDECs /3 JPEG /0 OFA |
4/8 |
3 |
2 |
MIG 4g.71gb |
4/8 |
4/7 |
4 NVDECs /4 JPEG /0 OFA |
4/8 |
4 |
1 |
MIG 7g.141gb |
Full |
7/7 |
7 NVDECs /7 JPEG /1 OFA |
Full |
8 |
1 |

## A100 MIG Profiles[#](https://docs.nvidia.com#a100-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA A100:

The following table shows the supported profiles on the A100-SXM4-40GB product. For A100-SXM4-80GB, the profile
names will change according to the memory proportion – for example, `1g.10gb`

, `1g.10gb+me`

, `1g.20gb`

,
`2g.20gb`

, `3g.40gb`

, `4g.40gb`

, `7g.80gb`

respectively.

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances Available |
|---|---|---|---|---|---|---|
MIG 1g.5gb |
1/8 |
1/7 |
0 NVDECs /0 JPEG /0 OFA |
1/8 |
1 |
7 |
MIG 1g.5gb+me |
1/8 |
1/7 |
1 NVDEC /1 JPEG /1 OFA |
1/8 |
1 |
1 (A single 1g profile can include media extensions) |
MIG 1g.10gb |
1/8 |
1/7 |
1 NVDEC /0 JPEG /0 OFA |
1/8 |
1 |
4 |
MIG 2g.10gb |
2/8 |
2/7 |
1 NVDEC /0 JPEG /0 OFA |
2/8 |
2 |
3 |
MIG 3g.20gb |
4/8 |
3/7 |
2 NVDECs /0 JPEG /0 OFA |
4/8 |
3 |
2 |
MIG 4g.20gb |
4/8 |
4/7 |
2 NVDECs /0 JPEG /0 OFA |
4/8 |
4 |
1 |
MIG 7g.40gb |
Full |
7/7 |
5 NVDECs /1 JPEG /1 OFA |
Full |
7 |
1 |

Note

The `1g.5gb+me`

profile is only available starting with R470 drivers.

The `1g.10gb`

profile is only available starting with R525 drivers.

## A30 MIG Profiles[#](https://docs.nvidia.com#a30-mig-profiles)

The following diagram shows the profiles supported on the NVIDIA A30:

The following table shows the supported profiles on the A30-24GB product.

Profile Name |
Fraction of Memory |
Fraction of SMs |
Hardware Units |
L2 Cache Size |
Copy Engines |
Number of Instances Available |
|---|---|---|---|---|---|---|
MIG 1g.6gb |
1/4 |
1/4 |
0 NVDECs /0 JPEG /0 OFA |
1/4 |
1 |
4 |
MIG 1g.6gb+me |
1/4 |
1/4 |
1 NVDEC /1 JPEG /1 OFA |
1/4 |
1 |
1 (A single 1g profile can include media extensions) |
MIG 2g.12gb |
2/4 |
2/4 |
2 NVDECs /0 JPEG /0 OFA |
2/4 |
2 |
2 |
MIG 2g.12gb+me |
2/4 |
2/4 |
2 NVDECs /1 JPEG /1 OFA |
2/4 |
2 |
1 (A single 2g profile can include media extensions) |
MIG 4g.24gb |
Full |
4/4 |
4 NVDECs /1 JPEG /1 OFA |
Full |
4 |
1 |

Note

The `1g.6gb+me`

profile is only available starting with R470 drivers.

The `2g.12gb+me`

profile is only available starting with R525 drivers.

**Universal MIG**

Universal MIG enables both compute and graphics workloads to run on the same GPU with hardware isolation. This feature is available on RTX PRO 6000 GPUs. `+gfx profiles`

which are new in GB20X architecture, enables graphics support in MIG instances.

**Profile References**

`+me profiles`

: Include at least one media engine (NVDEC, NVENC, NVJPG, or OFA).`+gfx`

: Adds support for graphics APIs (new in GB20X).`+me.all`

: Allocates all available media engines to this instance (does not include graphics support).`-me`

: Excludes all media engines for pure compute workloads.