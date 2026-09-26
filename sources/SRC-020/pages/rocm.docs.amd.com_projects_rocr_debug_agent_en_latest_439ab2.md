source: https://rocm.docs.amd.com/projects/rocr_debug_agent/en/latest

# ROCr Debug Agent[#](https://rocm.docs.amd.com#rocr-debug-agent)

The ROCr Debug Agent is a library that can be loaded by the [ROCr Runtime](https://rocm.docs.amd.com/projects/ROCR-Runtime/en/latest/index.html) to provide the following functionality:

Print the state of all AMD GPU wavefronts that cause a queue error (such as a memory violation, executing a

`s_trap 2`

, or executing an illegal instruction).Print the state of all AMD GPU wavefronts by sending a SIGQUIT signal to the process using

`kill -s SIGQUIT <pid>`

command or by pressing`Ctrl-\`

, while the program is executing.

This functionality is provided for all AMD GPUs supported by the [ROCm Debugger API (ROCdbgapi)](https://rocm.docs.amd.com/projects/ROCdbgapi/en/latest/index.html).

The code is open source and hosted at [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems/tree/develop/projects/rocr-debug-agent).

To contribute to the documentation, refer to
[Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.