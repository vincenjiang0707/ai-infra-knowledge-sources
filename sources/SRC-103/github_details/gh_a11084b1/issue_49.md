# [Issue #49] Install from Release?

source: https://github.com/ROCm/rocprofiler-sdk/issues/49
state: closed | updated: 2025-03-25T14:22:37Z
labels: 

## 正文

[PAPI ](https://github.com/icl-utk-edu/papi) will soon support rocprofiler-sdk as a component, and we will need a way to install rocprofiler-sdk via [spack](https://github.com/spack/spack).  To do this, I have been looking at using the release tar files for the installation, however the CMake configuration process does not work due to the reliance on git submodules for the external dependencies.  I think we need a way to turn off the use of submodules and provide the external dependencies explicitly.   Thoughts?

@srekolam
@renjithravindrankannath
@afzpatel

## 评论 (7)

### srekolam · 2025-03-10

@G-Ragghianti , when i look at https://github.com/ROCm/rocprofiler-sdk/blob/amd-staging/external/CMakeLists.txt
i see dependencies on external packages such as https://github.com/gulrak/filesystem.git and other packages. These are downloaded using git submodules . We can create individual new packages for https://github.com/gulrak/filesystem.git (not present in spack currently as far as i see) 

Rather than build from sources, will download of the release rpms from https://repo.radeon.com/rocm/ , will that help ?




### G-Ragghianti · 2025-03-10

@srekolam It is actually probably OK if the spack install gets the external dependencies itself (though it is preferable for them to be separately installed), however the problem is that the release tar files in the rocprofiler-sdk repo do not allow the install via git submodules to work because the references to the original git repo are removed in the tar release. This would be a problem even if you are trying to install a release tar by hand, so it is not just a spack issue.

The PAPI component for rocmprofiler-sdk has been developed on a system that uses the RPM releases, so that is not an issue.  However, we are now working on the release in spack, and it has to be a source install in that case.

Ideally, I think the rocmprofiler-sdk CMake would allow specification of the locations of the external dependencies and then only try to use the git submodule method if the dep is not found.

### G-Ragghianti · 2025-03-10

@adanalis Just FYI, this package is necessary for the rocp_sdk component in PAPI.

### G-Ragghianti · 2025-03-12

I had started a new spack package for rocprofiler-sdk to see what it would take to get it to work.  I was able to avoid the attempted git checkout of some of the submodules by setting variables like `ROCPROFILER_BUILD_GHC_FS` that are used in `external/CMakeLists.txt`, but I was stuck on the following:

```CMake
if(NOT TARGET PTL::ptl-static)
    # checkout submodule if not already checked out or clone repo if no .gitmodules file
    rocprofiler_checkout_git_submodule(
        RELATIVE_PATH external/ptl
        WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
        REPO_URL https://github.com/jrmadsen/PTL.git
        REPO_BRANCH rocprofiler)
```

Here is what I have so far for the Spack package:

```python
import re

from spack.package import *


class RocprofilerSdk(CMakePackage):
    """ROCPROFILER-SDK AMD HSA runtime API extension support"""

    homepage = "https://github.com/ROCm/rocprofiler-sdk"
    git = "https://github.com/ROCm/rocprofiler-sdk.git"
    url = "https://github.com/ROCm/rocprofiler-sdk/archive/refs/tags/rocm-6.3.2.tar.gz"
    tags = ["rocm"]

    license("MIT")
    version("6.3.2", sha256="65338734e6eb8f6d928fe352848c814c668c522a05d1aeec121f0ef4b2bbf61e")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("cmake@3:", type="build")

    depends_on("hip@6.3.2")
    depends_on("hsa-rocr-dev@6.3.2")
    depends_on("rccl@6.3.2")

    def cmake_args(self):
        args = [
                self.define("ROCPROFILER_BUILD_GHC_FS", False),
                self.define("ROCPROFILER_BUILD_GLOG", False),
                self.define("ROCPROFILER_BUILD_FMT", False),
                ]
        return args
```

### afzpatel · 2025-03-12

@srekolam opened another pr for rocprofiler-sdk:
https://github.com/spack/spack/pull/49406

He used git instead of the release tar files, so the use of git_submodules wouldn't be an issue. I was able to build rocprofiler-sdk successfully using his pr. 

### G-Ragghianti · 2025-03-12

OK, I'll have a look at it. Thanks.

### afzpatel · 2025-03-25

https://github.com/spack/spack/pull/49406 is merged and rocprofiler-sdk has been added to Spack. Closing this issue.
