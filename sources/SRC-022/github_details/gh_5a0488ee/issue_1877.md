# [Issue #1877] [Issue]: building from source tarball does not work due to missing MSCCLPP library that is never properly downloaded

source: https://github.com/ROCm/rccl/issues/1877
state: closed | updated: 2026-01-22T02:06:34Z
labels: Under Investigation

## 正文

### Problem Description

The following error occurs when trying to build RCCL for ROCm 6.4.3 from published source tarball (as opposed to doing a `git clone`), due to misconfigured MSCCLPP handling logic in cmake/MSCCLPP.cmake:
```
-- Building shared RCCL library
-- Could NOT find mscclpp_nccl (missing: MSCCLPP_INCLUDE_DIRS MSCCLPP_LIBRARIES)
-- Checking out external code
-- Building mscclpp only for gfx942.
-- Downloading/updating mscclpp_nccl
CMake Deprecation Warning at CMakeLists.txt:4 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


CMake Error at /usr/local/share/cmake-3.31/Modules/ExternalProject/shared_internal_commands.cmake:1323 (message):
  No download info given for 'mscclpp_nccl-download' and its source
  directory:

   /home/hpcuser/azhpc-images/distros/ubuntu24.04/rccl-rocm-6.4.3/ext-src/mscclpp

  is not an existing non-empty directory.  Please specify one of:

   * SOURCE_DIR with an existing non-empty directory
   * DOWNLOAD_COMMAND
   * URL
   * GIT_REPOSITORY
   * SVN_REPOSITORY
   * HG_REPOSITORY
   * CVS_REPOSITORY and CVS_MODULE
Call Stack (most recent call first):
  /usr/local/share/cmake-3.31/Modules/ExternalProject.cmake:3041 (_ep_add_download_command)
  CMakeLists.txt:9 (ExternalProject_Add)


-- Configuring incomplete, errors occurred!
CMake Error at cmake/DownloadProject.cmake:159 (message):
  CMake step for mscclpp_nccl failed: 1
Call Stack (most recent call first):
  cmake/MSCCLPP.cmake:103 (download_project)
  CMakeLists.txt:878 (include)


-- Configuring incomplete, errors occurred!
```

for downloaded tarball, the following code in MSCCLPP.cmake has multiple lines commented out that make it impossible to download MSCCLPP during build time, due to the fact that an extracted tarball is not a git repo and cannot checkout submodules.

```
if(ENABLE_MSCCLPP)
    # Try to find the mscclpp install
    set(MSCCLPP_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/ext/mscclpp CACHE PATH "")
    execute_process(
        COMMAND mkdir -p ${MSCCLPP_ROOT}
    )
    list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
    find_package(mscclpp_nccl)

    #if(NOT mscclpp_nccl_FOUND)
        # Ensure the source code is checked out
        set(MSCCLPP_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/mscclpp CACHE PATH "")
        set(JSON_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/json CACHE PATH "")
        if((NOT EXISTS ${MSCCLPP_SOURCE}/CMakeLists.txt) OR (NOT EXISTS ${JSON_SOURCE}/CMakeLists.txt))
            message(STATUS "Checking out external code")
            execute_process(
                COMMAND git submodule update --init --recursive
                WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
            )
        endif()

        execute_process(
           COMMAND git apply ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/cpx.patch
           WORKING_DIRECTORY ${MSCCLPP_SOURCE}
        )

        execute_process(
            COMMAND git apply ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/read-allred.patch
            WORKING_DIRECTORY ${MSCCLPP_SOURCE}
        )

        execute_process(
            COMMAND git apply ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/mscclpp_ibv_access_relaxed_ordering.patch
            WORKING_DIRECTORY ${MSCCLPP_SOURCE}
        )

        execute_process(
            COMMAND git apply ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/mem-reg.patch
            WORKING_DIRECTORY ${MSCCLPP_SOURCE}
        )

        execute_process(
            COMMAND git apply ${CMAKE_CURRENT_SOURCE_DIR}/ext-src/device-flag.patch
            WORKING_DIRECTORY ${MSCCLPP_SOURCE}
        )

        message(STATUS "Building mscclpp only for gfx942.")
        mscclpp_cmake_arg(CMAKE_PREFIX_PATH)
        mscclpp_cmake_arg(CMAKE_INSTALL_RPATH_USE_LINK_PATH)
        mscclpp_cmake_arg(HIP_COMPILER)

        set(GFX942_VARIANT "gfx942")
        if(BUILD_ADDRESS_SANITIZER)
            set(GFX942_VARIANT "gfx942:xnack+")
        endif()

        download_project(PROJ                mscclpp_nccl
                         #GIT_REPOSITORY      https://github.com/microsoft/mscclpp.git
                         #GIT_TAG             4ee15b7ad085daaf74349d4c49c9b8480d28f0dc
                         INSTALL_DIR         ${MSCCLPP_ROOT}
                         CMAKE_ARGS          -DAMDGPU_TARGETS=${GFX942_VARIANT} -DGPU_TARGETS=${GFX942_VARIANT} -DMSCCLPP_BYPASS_GPU_CHECK=ON -DMSCCLPP_USE_ROCM=ON -DCMAKE_BUILD_TYPE=${CMAKE_BUILD_TYPE} -DMSCCLPP_BUILD_APPS_NCCL=ON -DMSCCLPP_BUILD_PYTHON_BINDINGS=OFF -DMSCCLPP_BUILD_TESTS=OFF -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> "${CMAKE_PREFIX_PATH_ARG}" -DCMAKE_VERBOSE_MAKEFILE=1 "${CMAKE_INSTALL_RPATH_USE_LINK_PATH_ARG}" "${HIP_COMPILER_ARG}" -DFETCHCONTENT_SOURCE_DIR_JSON=${JSON_SOURCE}
                         LOG_DOWNLOAD        FALSE
                         LOG_CONFIGURE       FALSE
                         LOG_BUILD           FALSE
                         LOG_INSTALL         FALSE
                         UPDATE_DISCONNECTED TRUE
                         SOURCE_DIR          ${MSCCLPP_SOURCE}
        )
```

Either MSCCLPP source code should be included in the tarball, or the cmake file should handle building from tarball source properly by reading metadata from .gitmodules file and maintaining consistency of the hash in .gitmodules and the actual submodule commit hash used by using a git commit hook

### Operating System

irrelevant

### CPU

irrelevant

### GPU

irrelevant

### ROCm Version

irrelevant

### ROCm Component

_No response_

### Steps to Reproduce

```
tar -xzf ${TARBALL}
mkdir ./${rccl_folder}/build
pushd ./${rccl_folder}/build
CXX=/opt/rocm/bin/hipcc cmake -DCMAKE_PREFIX_PATH=/opt/rocm/ -DCMAKE_INSTALL_PREFIX=/opt/rccl ..
make -j$(nproc)
make install
popd
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (7)

### ppanchad-amd · 2025-08-22

Hi @arsdragonfly. Internal ticket has been created to assist with your issue. Thanks!

### huanrwan-amd · 2025-08-26

Hi @arsdragonfly, thanks for pointing out the issue here. We are curious about the context. Since direct building from source repo works, are you working on some automation or CI/CD pipeline? 

### arsdragonfly · 2025-08-27

> Hi [@arsdragonfly](https://github.com/arsdragonfly), thanks for pointing out the issue here. We are curious about the context. Since direct building from source repo works, are you working on some automation or CI/CD pipeline?

if you are doing `git clone` then it works; if you go to the releases page and download the tarball and work from the extracted tarball, it doesn't.

### huanrwan-amd · 2025-08-27

Hi @arsdragonfly , thanks for the response. As you noticed, this is a software release tarball. We are curious about the context, why you work on the extracted software release tarball not the git source code? Are you working on some automation or CI/CD pipeline?

### arsdragonfly · 2025-09-03

> Hi [@arsdragonfly](https://github.com/arsdragonfly) , thanks for the response. As you noticed, this is a software release tarball. We are curious about the context, why you work on the extracted software release tarball not the git source code? Are you working on some automation or CI/CD pipeline?

Yes, our CI/CD was working off of the tarball previously.
We've switched to doing a `git clone`, but we think it would be reasonable to make whatever tarball you release to be actually able to build your software.

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2786

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
