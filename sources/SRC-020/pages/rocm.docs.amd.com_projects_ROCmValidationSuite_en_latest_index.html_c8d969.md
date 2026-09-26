source: https://rocm.docs.amd.com/projects/ROCmValidationSuite/en/latest/index.html

# ROCm Validation Suite documentation[#](https://rocm.docs.amd.com#rocm-validation-suite-documentation)

The ROCm Validation Suite (RVS) is a system validation and diagnostics tool for monitoring, stress testing, detecting, and troubleshooting issues that affect the functionality and performance of AMD GPUs operating in a high-performance/AI/ML computing environment. RVS is enabled using the ROCm software stack on a compatible software and hardware platform.

RVS is a collection of tests, benchmarks, and qualification tools, each targeting a specific subsystem of the ROCm platform. All of the tools are implemented in software and share a common command-line interface. Each test set is implemented in a “module”, which is a library encapsulating the functionality specific to the tool. The CLI can specify the directory containing modules when searching for libraries to load. Each module may have a set of options that it defines and a configuration file that supports its execution.

For more information, refer to [GitHub.](https://github.com/ROCm/ROCmValidationSuite)

Note

TransferBench is now a part of the ROCm Validation Suite and is installed with it.
See the [TransferBench documentation](https://rocm.docs.amd.com/projects/TransferBench/en/latest/) for more information.

To contribute to the documentation, refer to
[Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the
[Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.