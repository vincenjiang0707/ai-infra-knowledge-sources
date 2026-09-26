source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/install.html

# Installing ROCm and deep learning frameworks[#](https://rocm.docs.amd.com#installing-rocm-and-deep-learning-frameworks)

2026-02-19

1 min read time

Before getting started, install ROCm and supported deep learning frameworks.

Each release of ROCm supports specific hardware and software configurations. Before installing, consult the
[System requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/reference/system-requirements.html) and
[Installation prerequisites](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/prerequisites.html) guides.

If you’re new to ROCm, refer to the [ROCm quick start install guide for Linux](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/quick-start.html).

If you’re using a Radeon GPU for graphics-accelerated applications, refer to the
[Radeon installation instructions](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/howto_native_linux.html).

You can install ROCm on [compatible systems](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/reference/system-requirements.html) via your Linux
distribution’s package manager. See the following documentation resources to get started:

Follow the [post-installation instructions](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/install/post-install.html) to
configure your system linker, PATH, and verify the installation.

If you encounter any issues during installation, refer to the
[Installation troubleshooting](https://rocm.docs.amd.com/projects/install-on-linux/en/docs-7.2.4/reference/install-faq.html) guide.

## Deep learning frameworks[#](https://rocm.docs.amd.com#deep-learning-frameworks)

ROCm supports deep learning frameworks and libraries including [PyTorch](https://pytorch.org), [TensorFlow](https://tensorflow.org), [JAX](https://jax.readthedocs.io/en/latest), and more.

Review the [framework installation documentation](https://rocm.docs.amd.com/deep-learning-rocm.html). For ease-of-use, it’s recommended to use official ROCm prebuilt Docker
images with the framework pre-installed.

## Next steps[#](https://rocm.docs.amd.com#next-steps)

After installing ROCm and your desired ML libraries – and before running AI workloads – conduct system health benchmarks
to test the optimal performance of your AMD hardware. See [System setup for AI workloads on ROCm](https://rocm.docs.amd.com/system-setup/index.html) to get started.