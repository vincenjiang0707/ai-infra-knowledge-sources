source: https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/reference/system-requirements.html

# System requirements (Linux)[#](https://rocm.docs.amd.com#system-requirements-linux)

2026-04-17

9 min read time

## Supported GPUs[#](https://rocm.docs.amd.com#supported-gpus)

The following table shows the supported AMD Instinct™ GPUs, and Radeon™ PRO and Radeon GPUs. If a GPU is not listed on this table, it’s not officially supported by AMD.

GPUs listed in the following table support compute workloads (no display information or graphics). If you’re using ROCm with AMD Radeon™ GPUs or Ryzen™ APUs for graphics workloads, see the [Use ROCm on Radeon and Ryzen](https://rocm.docs.amd.com/projects/radeon-ryzen/en/latest/index.html) documentation to verify compatibility and system requirements.

Note

If your GPU is not listed, it might be community-enabled through [TheRock](https://github.com/ROCm/TheRock?tab=readme-ov-file#therock) nightly
builds. For more information, see [TheRock supported GPUs](https://github.com/ROCm/TheRock/blob/main/SUPPORTED_GPUS.md). For
installation guidance, see [TheRock releases](https://github.com/ROCm/TheRock/blob/main/RELEASES.md).

GPU |
Series |
Architecture |
LLVM target |
Support |
|---|---|---|---|---|
AMD Instinct MI355X |
MI350 |
CDNA4 |
gfx950 |
✅ |
AMD Instinct MI350X |
MI350 |
CDNA4 |
gfx950 |
✅ |
AMD Instinct MI325X |
MI300 |
CDNA3 |
gfx942 |
✅ |
AMD Instinct MI300X |
MI300 |
CDNA3 |
gfx942 |
✅ |
AMD Instinct MI300A |
MI300 |
CDNA3 |
gfx942 |
✅ |
AMD Instinct MI250X |
MI200 |
CDNA2 |
gfx90a |
✅ |
AMD Instinct MI250 |
MI200 |
CDNA2 |
gfx90a |
✅ |
AMD Instinct MI210 |
MI200 |
CDNA2 |
gfx90a |
✅ |
AMD Instinct MI100 |
MI100 |
CDNA |
gfx908 |
✅ |
AMD Instinct MI50 |
N/A |
GCN5.1 |
gfx906 |
❌ |
AMD Instinct MI25 |
N/A |
GCN5.0 |
gfx900 |
❌ |

GPU |
Architecture |
LLVM target |
Support |
|---|---|---|---|
AMD Radeon AI PRO R9700 |
RDNA4 |
gfx1201 |
✅ |
AMD Radeon AI PRO R9600D |
RDNA4 |
gfx1201 |
✅ |
AMD Radeon PRO V710 |
RDNA3 |
gfx1101 |
✅ |
AMD Radeon PRO W7900 Dual Slot |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon PRO W7900 |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon PRO W7800 48GB |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon PRO W7800 |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon PRO W7700 |
RDNA3 |
gfx1101 |
✅ |
AMD Radeon PRO W6800 |
RDNA2 |
gfx1030 |
✅ |
AMD Radeon PRO V620 |
RDNA2 |
gfx1030 |
✅ |
AMD Radeon PRO VII |
GCN5.1 |
gfx906 |
❌ |

GPU |
Architecture |
LLVM target |
Support |
|---|---|---|---|
AMD Radeon RX 9070 XT |
RDNA4 |
gfx1201 |
✅ |
AMD Radeon RX 9070 GRE |
RDNA4 |
gfx1201 |
✅ |
AMD Radeon RX 9070 |
RDNA4 |
gfx1201 |
✅ |
AMD Radeon RX 9060 XT LP |
RDNA4 |
gfx1200 |
✅ |
AMD Radeon RX 9060 XT |
RDNA4 |
gfx1200 |
✅ |
AMD Radeon RX 9060 |
RDNA4 |
gfx1200 |
✅ |
AMD Radeon RX 7900 XTX |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon RX 7900 XT |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon RX 7900 GRE |
RDNA3 |
gfx1100 |
✅ |
AMD Radeon RX 7800 XT |
RDNA3 |
gfx1101 |
✅ |
AMD Radeon RX 7700 XT |
RDNA3 |
gfx1101 |
✅ |
AMD Radeon RX 7700 |
RDNA3 |
gfx1101 |
✅ |
AMD Radeon VII |
GCN5.1 |
gfx906 |
❌ |

✅: **Supported** - Official software distributions of the current ROCm release fully support this hardware.

⚠️: **Deprecated** - The current ROCm release has limited support for this hardware. Existing features and capabilities are maintained, but no new features or optimizations will be added. A future ROCm release will remove support.

❌: **Unsupported** - The current ROCm release does not support this hardware. The HIP runtime might continue to run applications for an unsupported GPU, but prebuilt ROCm libraries are not officially supported and will cause runtime errors.

Important

Systems with multiple GPUs may require `iommu=pt`

to be set at boot time to prevent application hangs, as described in
[Issue #5: Application hangs on Multi-GPU systems](https://rocm.docs.amd.com/install-faq.html#multi-gpu).

Note

See the [Compatibility matrix](https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/compatibility-matrix.html#architecture-support-compatibility-matrix) for an overview
of supported GPU architectures across ROCm releases.

Footnotes

## Supported operating systems[#](https://rocm.docs.amd.com#supported-operating-systems)

AMD ROCm software supports the following Linux distributions.

Operating system |
Kernel |
Glibc |
Support |
|---|---|---|---|
Ubuntu 24.04.4 |
6.8 [GA], 6.17 [HWE] |
2.39 |
✅ |
Ubuntu 22.04.5 |
5.15 [GA], 6.8 [HWE] |
2.35 |
✅ |
RHEL 10.1 |
6.12.0-124 |
2.39 |
✅ |
RHEL 10.0 |
6.12.0-55 |
2.39 |
✅ |
RHEL 9.7 |
5.14.0-611 |
2.34 |
✅ |
RHEL 9.6 |
5.14.0-570 |
2.34 |
✅ |
RHEL 9.4 |
5.14.0-427 |
2.34 |
✅ |
RHEL 8.10 |
4.18.0-553 |
2.28 |
✅ |
SLES 15 SP7 |
6.4.0-150700.51 |
2.38 |
✅ |
Debian 13 |
6.12 |
2.35 |
✅ |
Debian 12 |
6.1.0 |
2.36 |
✅ |
Rocky Linux 9 |
5.14.0-570 |
2.34 |
✅ |
Oracle Linux 10 |
6.12.0 (UEK) |
2.39 |
✅ |
Oracle Linux 9 |
5.15.0 (UEK) |
2.34 |
✅ |
Oracle Linux 8 |
5.15.0 (UEK) |
2.28 |
✅ |

Note

See

[Red Hat Enterprise Linux Release Dates](https://access.redhat.com/articles/3078)to learn about the specific kernel versions supported on Red Hat Enterprise Linux (RHEL).See

[List of SUSE Linux Enterprise Server kernel](https://www.suse.com/support/kb/doc/?id=000019587)to learn about the specific kernel version supported on SUSE Linux Enterprise Server (SLES).See the

[Compatibility matrix](https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/compatibility-matrix.html)for an overview of OS support across ROCm releases.

Footnotes

[1](https://rocm.docs.amd.com#id33),

[2](https://rocm.docs.amd.com#id34),

[3](https://rocm.docs.amd.com#id35),

[4](https://rocm.docs.amd.com#id36))

RHEL 10.1 and RHEL 9.7 are supported on all listed [Supported GPUs](https://rocm.docs.amd.com#supported-gpus) except AMD Radeon PRO V620 GPU.

[10](https://rocm.docs.amd.com#id37)]

RHEL 10.0, RHEL 9.6, and RHEL 9.4 are supported on all AMD Instinct GPUs listed under [Supported GPUs](https://rocm.docs.amd.com#supported-gpus).

[11](https://rocm.docs.amd.com#id38)]

RHEL 8.10 is supported only on AMD Instinct MI300X, MI300A, MI250X, MI250, MI210, and MI100 GPUs.

[12](https://rocm.docs.amd.com#id39)]

SLES 15 SP7 is supported on all AMD Instinct GPUs listed under [Supported GPUs](https://rocm.docs.amd.com#supported-gpus).

[13](https://rocm.docs.amd.com#id40)]

Debian 13 is supported only on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs.

[14](https://rocm.docs.amd.com#id41)]

Debian 12 are supported only on AMD Instinct MI325X, MI300X, MI300A, MI250X, MI250, and MI210 GPUs.

[15](https://rocm.docs.amd.com#id42)]

Rocky Linux 9 is supported only on AMD Instinct MI300X and MI300A GPUs.

[1](https://rocm.docs.amd.com#id43),

[2](https://rocm.docs.amd.com#id44))

Oracle Linux 10 and 9 are supported only on AMD Instinct MI355X, MI350X, MI325X, and MI300X GPUs.

[17](https://rocm.docs.amd.com#id45)]

Oracle Linux 8 is supported only on AMD Instinct MI300X GPUs.

## Virtualization support[#](https://rocm.docs.amd.com#virtualization-support)

ROCm supports virtualization for the Instinct GPUs and Radeon PRO GPUs listed in the following table.

Important

GPU virtualization with KVM-based SR-IOV requires AMD GPU Virtualization Driver (GIM) driver. Refer to [GIM Release note](https://github.com/amd/MxGPU-Virtualization/releases).

|
GPU |
Hypervisor |
Virtualization technology |
Host OS |
Guest OS |
|---|---|---|---|---|
|
Instinct MI355X |
KVM |
Passthrough |
Ubuntu 24.04, |
Ubuntu 24.04, |
|
KVM |
SR-IOV |
Ubuntu 24.04 |
Ubuntu 24.04, |
|
|
Instinct MI350X |
KVM |
Passthrough |
Ubuntu 24.04, |
Ubuntu 24.04, |
|
KVM |
SR-IOV |
Ubuntu 24.04 |
Ubuntu 24.04, |
|
|
Instinct MI325X |
KVM |
Passthrough |
Ubuntu 24.04, |
Ubuntu 24.04, |
|
KVM |
SR-IOV |
Ubuntu 22.04 |
Ubuntu 22.04 |
|
|
Instinct MI300X |
ESXi |
Passthrough |
ESXi 8.0 Update 3 |
Ubuntu 24.04, |
|
KVM |
Passthrough |
Ubuntu 24.04, |
Ubuntu 24.04, |
|
|
KVM |
SR-IOV |
Ubuntu 22.04 |
Ubuntu 22.04 |
|
|
KVM |
SR-IOV |
RHEL 9.4 |
Ubuntu 24.04, |
|
|
Instinct MI210 |
KVM |
SR-IOV |
RHEL 9.4 |
Ubuntu 22.04, |
|
KVM |
Passthrough |
RHEL 9.4 |
Ubuntu 22.04, |
|
|
Radeon PRO V710 |
KVM |
SR-IOV |
Ubuntu 24.04 |
Ubuntu 24.04 |

Note

AMD Virtualization supports the following:

Passthrough: All 8 GPUs are assigned directly to a single virtual machine (VM).

SR-IOV: Provides 1 Virtual Function (VF) per GPU (8 VFs in total), which can be flexibly assigned among multiple VMs (for example, 8 VMs with 1 VF each, 4 VMs with 2 VFs each, or 2 VMs with 4 VFs each)


## CPU support[#](https://rocm.docs.amd.com#cpu-support)

ROCm requires CPUs that support PCIe™ atomics. Modern CPUs after the release of 1st generation AMD Zen CPU and Intel™ Haswell support PCIe atomics.