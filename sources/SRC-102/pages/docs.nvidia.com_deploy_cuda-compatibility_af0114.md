source: https://docs.nvidia.com/deploy/cuda-compatibility

# CUDA Compatibility[#](https://docs.nvidia.com#cuda-compatibility)

[CUDA Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/) describes how CUDA applications and toolkit components can run across different NVIDIA driver versions. It enables greater flexibility when upgrading CUDA toolkits and applications by reducing the need to upgrade drivers at the same time in every deployment scenario.

This flexibility is important for data center, enterprise, and managed environments, where driver updates may follow different qualification or maintenance schedules than application and toolkit updates. CUDA Compatibility helps bridge that gap by defining supported ways to run newer CUDA software on existing driver installations, within documented limits.

CUDA Compatibility includes [Minor Version Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html), available starting with CUDA 11, which allows applications built within the same major CUDA release family to run on a sufficiently new driver, with some feature limitations.

It also includes [Forward Compatibility](https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html), which uses the `cuda-compat-<major>-<minor>`

package to allow applications built with a newer toolkit to run on older base drivers across major release families, subject to platform and GPU support.

This guide introduces these compatibility models, outlines the supported upgrade paths, and helps developers and administrators determine which approach is appropriate for their platform, driver, GPU, and CUDA toolkit combination.