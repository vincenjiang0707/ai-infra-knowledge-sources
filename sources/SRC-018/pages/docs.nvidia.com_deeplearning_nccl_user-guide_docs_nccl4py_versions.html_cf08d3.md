source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/versions.html

# Versions[](https://docs.nvidia.com#versions)

NCCL4Py exposes helpers to inspect the installed NCCL stack: `nccl4py`

itself, the version of the NCCL headers its bindings were generated from,
and the loaded `libnccl.so`

.

```
import nccl.core
nccl.core.show_versions() # human-readable block to stdout
v = nccl.core.get_version() # programmatic snapshot
```

## show_versions[](https://docs.nvidia.com#show-versions)

-
nccl.core.show_versions() None
[](https://docs.nvidia.com#nccl.core.show_versions) Print nccl4py, binding, and loaded-libnccl version information.


## get_version[](https://docs.nvidia.com#get-version)

-
nccl.core.get_version()
[VersionInfo](https://docs.nvidia.com#nccl.core.VersionInfo)[](https://docs.nvidia.com#nccl.core.get_version) Return structured nccl4py, binding, and loaded-libnccl versions.


## VersionInfo[](https://docs.nvidia.com#versioninfo)

-
*class*nccl.core.VersionInfo(*nccl4py:*,[Version](https://packaging.pypa.io/en/stable/version.html#packaging.version.Version)*nccl_bindings:*,[Version](https://packaging.pypa.io/en/stable/version.html#packaging.version.Version)*libnccl:*)[LibraryInfo](https://docs.nvidia.com#nccl.core.LibraryInfo)| None[](https://docs.nvidia.com#nccl.core.VersionInfo) Bases:

`object`

Version snapshot of nccl4py, its bindings, and loaded libnccl.

-
libnccl
*:*[LibraryInfo](https://docs.nvidia.com#nccl.core.LibraryInfo)| None[](https://docs.nvidia.com#nccl.core.VersionInfo.libnccl) Loaded libnccl information, or None when the library is unavailable.


-
libnccl