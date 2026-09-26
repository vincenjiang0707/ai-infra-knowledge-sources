source: https://rocm.docs.amd.com/projects/install-on-windows/en/docs-6.4.2/reference/system-requirements.html

# System requirements (Windows)[#](https://rocm.docs.amd.com#system-requirements-windows)

2025-09-08

3 min read time

## Supported SKUs[#](https://rocm.docs.amd.com#supported-skus)

AMD HIP SDK supports the following Windows variants.

Distribution |
Processor architectures |
Validated update |
|---|---|---|
Windows 10 |
x86-64 |
22H2 (GA) |
Windows 11 |
x86-64 |
22H2 (GA) |
Windows Server 2022 |
x86-64 |
22H2 (GA) |

## Windows-supported GPUs and APUs[#](https://rocm.docs.amd.com#windows-supported-gpus-and-apus)

The tables below show supported GPUs/APUs for AMD Radeon™ PRO, AMD Radeon™, and AMD Ryzen™. If a GPU is not listed on this table, it is not officially supported by AMD.

Name |
Architecture |
LLVM target |
Runtime |
HIP SDK |
|---|---|---|---|---|
AMD Radeon AI PRO R9700 |
RDNA4 |
gfx1201 |
✅ |
✅ |
AMD Radeon PRO W7900 Dual Slot |
RDNA3 |
gfx1100 |
✅ |
✅ |
AMD Radeon PRO W7900 |
RDNA3 |
gfx1100 |
✅ |
✅ |
AMD Radeon PRO W7800 |
RDNA3 |
gfx1100 |
✅ |
✅ |
AMD Radeon PRO W7700 |
RDNA3 |
gfx1101 |
✅ |
✅ |
AMD Radeon PRO W6800 |
RDNA2 |
gfx1030 |
✅ |
✅ |
AMD Radeon PRO W6600 |
RDNA2 |
gfx1032 |
✅ |
❌ |
AMD Radeon PRO W5500 |
RDNA1 |
gfx1012 |
❌ |
❌ |
AMD Radeon PRO VII |
GCN5.1 |
gfx906 |
❌ |
❌ |

Name |
Architecture |
LLVM target |
Runtime |
HIP SDK |
|---|---|---|---|---|
AMD Radeon RX 9070 XT |
RDNA4 |
gfx1201 |
✅ |
✅ |
AMD Radeon RX 9070 |
RDNA4 |
gfx1201 |
✅ |
✅ |
AMD RX 9070 GRE |
RDNA4 |
gfx1201 |
✅ |
✅ |
AMD Radeon RX 9060 XT |
RDNA4 |
gfx1200 |
✅ |
✅ |
AMD Radeon RX 9060 |
RDNA4 |
gfx1200 |
✅ |
✅ |
AMD Radeon RX 7900 XTX |
RDNA3 |
gfx1100 |
✅ |
✅ |
AMD Radeon RX 7900 XT |
RDNA3 |
gfx1100 |
✅ |
✅ |
AMD Radeon RX 7800 XT |
RDNA3 |
gfx1101 |
✅ |
✅ |
AMD Radeon RX 7700 XT |
RDNA3 |
gfx1101 |
✅ |
✅ |
AMD Radeon RX 7650 GRE |
RDNA3 |
gfx1102 |
✅ |
✅ |
AMD Radeon RX 7600 XT |
RDNA3 |
gfx1102 |
✅ |
✅ |
AMD Radeon RX 7600 |
RDNA3 |
gfx1102 |
✅ |
✅ |
AMD Radeon RX 6950 XT |
RDNA2 |
gfx1030 |
✅ |
✅ |
AMD Radeon RX 6900 XT |
RDNA2 |
gfx1030 |
✅ |
✅ |
AMD Radeon RX 6800 XT |
RDNA2 |
gfx1030 |
✅ |
✅ |
AMD Radeon RX 6800 |
RDNA2 |
gfx1030 |
✅ |
✅ |
AMD Radeon RX 6750 XT |
RDNA2 |
gfx1031 |
✅ |
❌ |
AMD Radeon RX 6700 XT |
RDNA2 |
gfx1031 |
✅ |
❌ |
AMD Radeon RX 6700 |
RDNA2 |
gfx1031 |
✅ |
❌ |
AMD Radeon RX 6650 XT |
RDNA2 |
gfx1032 |
✅ |
❌ |
AMD Radeon RX 6600 XT |
RDNA2 |
gfx1032 |
✅ |
❌ |
AMD Radeon RX 6600 |
RDNA2 |
gfx1032 |
✅ |
❌ |

Name |
Architecture |
LLVM target |
Runtime |
HIP SDK |
|---|---|---|---|---|
AMD Ryzen AI Max+ Pro 395 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |
AMD Ryzen AI Max+ 395 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |
AMD Ryzen AI Max Pro 390 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |
AMD Ryzen AI Max 390 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |
AMD Ryzen AI Max Pro 385 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |
AMD Ryzen AI Max 385 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |
AMD Ryzen AI Max Pro 380 |
RDNA3.5 |
gfx1151 |
✅ |
✅ |

✅: **Supported** - Official software distributions of the current HIP SDK release fully support this hardware.

⚠️: **Deprecated** - The current HIP SDK release has limited support for this hardware. Existing features and capabilities are maintained, but no new features or optimizations will be added. A future release will remove support.

❌: **Unsupported** - The current HIP SDK release does not support this hardware. Prebuilt HIP SDK libraries are not officially supported and might cause runtime errors.

## Component support[#](https://rocm.docs.amd.com#component-support)

ROCm components are described in [What is ROCm?](https://rocm.docs.amd.com/en/docs-6.4.2/what-is-rocm.html) Support on Windows
is provided with two levels on enablement.

**Runtime**: Runtime enables the use of the HIP and OpenCL runtimes only.**HIP SDK**: Runtime plus additional HIP components (as listed in[API libraries](https://rocm.docs.amd.com/en/docs-6.4.2/reference/api-libraries.html)).

Note

Some math libraries are Linux exclusive.

## CPU support[#](https://rocm.docs.amd.com#cpu-support)

ROCm requires CPUs that support PCIe™ atomics. Modern CPUs after the release of 1st generation AMD Zen CPU and Intel™ Haswell support PCIe atomics.