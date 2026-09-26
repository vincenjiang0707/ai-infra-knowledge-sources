# [Issue #2725] FlashAttention-2 on AMD Radeon RX 9060 XT / gfx1200 with ROCm 7.14

source: https://github.com/Dao-AILab/flash-attention/issues/2725
state: open | updated: 2026-08-02T14:24:10Z
labels: 

## 正文

FlashAttention-2 on AMD Radeon RX 9060 XT / gfx1200 with ROCm 7.14
Summary

I successfully built and ran FlashAttention-2 using the Composable Kernel backend on an AMD Radeon RX 9060 XT (gfx1200) with ROCm 7.14 and PyTorch 2.12.

This is noteworthy because current FlashAttention ROCm documentation primarily identifies MI200/MI300-class GPUs as supported by the CK backend. In practice, the generated FlashAttention kernels compiled for gfx1200, and the resulting extension successfully loaded and executed.

Most of the difficulty encountered was not failure of the generated FlashAttention kernels themselves, but interaction between ROCm's Python SDK, development headers, system ROCm packages, and the FlashAttention build system.

After resolving these issues, FlashAttention-2 was operational on the RX 9060 XT.

System
GPU:          AMD Radeon RX 9060 XT 16 GB
Architecture: gfx1200

OS:           Linux / Docker
Python:       3.13.14

PyTorch:      2.12.0+rocm7.14.0
ROCm/HIP:     7.14.60850
ROCm SDK:     7.14.0
Triton:       3.7.1+git0263a6a6.rocm7.14.0

Relevant installed packages included:

rocm                         7.14.0
rocm-sdk-core                7.14.0
rocm-sdk-libraries           7.14.0
rocm-sdk-device-gfx1200      7.14.0

torch                        2.12.0+rocm7.14.0
torchvision                  0.27.0+rocm7.14.0
torchaudio                   2.11.0+rocm7.14.0

The GPU was correctly detected by PyTorch:

GPU available: True
GPU: AMD Radeon RX 9060 XT
Initial build

FlashAttention was cloned from source and the CK backend built with:

git clone https://github.com/Dao-AILab/flash-attention.git
cd flash-attention

pip install ninja
python setup.py install

The build correctly targeted:

--offload-arch=gfx1200

Approximately 1,837 compilation targets were generated.

A large number of generated CK FlashAttention kernels compiled successfully for gfx1200.

Typical output was:

1 warning generated when compiling for gfx1200.

The common warning concerned occupancy:

warning: failed to meet occupancy target given by
'amdgpu-waves-per-eu'

These warnings did not prevent compilation.

Issue 1 — build parallelism

The FlashAttention build automatically selected:

ninja -v -j 1

and reported:

Auto set MAX_JOBS to `1`

With approximately 1,837 generated compilation targets, this resulted in an extremely long build.

This is not necessarily a ROCm defect, but it makes source builds for consumer hardware particularly expensive.

It may be useful for the build system to provide more visible guidance about the selected job count and expected number of compilation units before beginning the build.

Issue 2 — missing ROCm development headers

Near completion, compilation of the FlashAttention extension failed with:

fatal error: 'thrust/complex.h' file not found

After supplying rocThrust, further dependencies were encountered, including rocPRIM and eventually:

fatal error: 'hipsparse/hipsparse.h' file not found

The environment contained:

rocm-sdk-core
rocm-sdk-libraries

but not the complete development SDK.

Installing:

python -m pip install \
    --index-url https://repo.amd.com/rocm/whl-multi-arch/ \
    "rocm[devel]==7.14.0"

provided the required development components.

The distinction between the runtime SDK and development SDK was not obvious when building a PyTorch C++/HIP extension.

A clearer diagnostic from the ROCm/PyTorch extension toolchain indicating that the development SDK is required would be useful.

Issue 3 — mixing system HIP and Python ROCm SDK headers

After installing the ROCm 7.14 development SDK, compilation progressed further but exposed a header-selection problem.

The compiler itself came from the Python ROCm 7.14 SDK:

/opt/venv/lib/python3.13/site-packages/_rocm_sdk_devel/lib/llvm/bin/clang++

while HIP headers were being selected from:

/usr/include/hip/

For example:

/usr/include/hip/hip_runtime_api.h

The system HIP installation was an older ROCm version.

This resulted in a mixed ROCm toolchain: ROCm 7.14 compiler/libraries combined with older system headers.

Explicitly placing the ROCm Python SDK include directories ahead of /usr/include resolved this class of problem.

This may warrant investigation into the default include-path behaviour of the wheel-distributed hipcc.

Issue 4 — hipDeviceAttributeNumberOfXccs

Once the CK API objects were reached, compilation failed at:

status = hipDeviceGetAttribute(
    &num_xccs,
    hipDeviceAttributeNumberOfXccs,
    device
);

with:

error: use of undeclared identifier
'hipDeviceAttributeNumberOfXccs'

The error originated from:

ck_tile/host/device_prop.hpp

This occurred because the build was resolving an incompatible hip_runtime_api.h.

Using the matching ROCm 7.14 SDK headers resolved the API mismatch.

Issue 5 — __AMDGCN_WAVEFRONT_SIZE

Compilation for gfx1200 also encountered:

error: use of undeclared identifier
'__AMDGCN_WAVEFRONT_SIZE'

originating from:

amd_warp_functions.h

For the RX 9060 XT / gfx1200 target, explicitly supplying:

-D__AMDGCN_WAVEFRONT_SIZE=32

allowed compilation to proceed.

It may be worth determining why this definition was not supplied automatically by this particular hipcc/header configuration when targeting:

--offload-arch=gfx1200
Preserving the existing CK build

At the point of failure, approximately:

1830 / 1837

objects had already successfully compiled.

Changing global Ninja compiler flags caused Ninja to correctly regard the existing objects as dirty and attempt a complete rebuild.

Restoring the original build.ninja showed that only approximately 10 final targets actually remained:

[1/10]
...

The final API/glue objects were therefore built using the corrected ROCm 7.14 include environment and gfx1200 wavefront definition without invalidating the approximately 1,830 previously generated CK objects.

This allowed the existing compilation to be recovered rather than repeated.

Result

The remaining objects successfully compiled and linked.

The resulting FlashAttention Python package imported correctly, and FlashAttention-2 was usable on the GPU.

The resulting stack was therefore:

FlashAttention-2
       ↓
Composable Kernel
       ↓
ROCm 7.14
       ↓
gfx1200
       ↓
AMD Radeon RX 9060 XT

This configuration works.

This suggests that at least some current FlashAttention-2 CK functionality is already viable on RDNA4 / gfx1200, despite this configuration being outside or beyond the currently documented CK support matrix.

Conclusions

The most interesting outcome is that FlashAttention-2's Composable Kernel implementation was successfully built and executed on consumer RDNA4 (gfx1200) hardware.

The principal obstacles encountered were integration issues rather than an inability to compile FlashAttention kernels for the architecture:

The ROCm runtime installation did not initially contain all development headers required for PyTorch HIP extension compilation.
The Python-distributed ROCm 7.14 compiler could resolve older system ROCm headers from /usr/include, producing a mixed toolchain.
__AMDGCN_WAVEFRONT_SIZE was not defined in the encountered gfx1200 compilation path and required an explicit value of 32.
Once the toolchain and header issues were addressed, the large body of generated CK kernels and the final extension successfully compiled.

The experience suggests that gfx1200 FlashAttention support may be substantially closer to working out-of-the-box than the current documented support matrix implies.

The main opportunity appears to be improving ROCm SDK/header consistency and making the required development environment clearer for third-party PyTorch HIP extensions.

Exact compiler invocations, build logs, the working container environment, and the resulting FlashAttention installation can be provided if useful for reproducing the issues.

## 评论 (1)

### AlfredSartan572 · 2026-08-02

@dreamdayapps 
Thank you!
Your findings allowed me to finally be able to install flash attention with CK backend.
I was using flash-attention in ComfyUI, but with the Triton backend.
After installing flash-attention with CK backed, my comfyui timings improved (slightly)
According to this amd blog : https://rocm.blogs.amd.com/software-tools-optimization/comfyui-fa-backends/README.html#more-on-attention, I should get 3%-5% more speed on my Navi31 card [RX 7900 XTX, gfx1100, RDNA3] compared to the Triton backend.
I got about 2% improvement:
with FLASH_ATTENTION_TRITON_AMD_ENABLE="TRUE" : 55.15 seconds
with FLASH_ATTENTION_TRITON_AMD_ENABLE="FALSE": 53.90 seconds

If anyone else wants to install flash-attention with CK backend on a 7900 XTX with ROCm 7.14 (on Linux) : this is what worked for me (adapt wheels and paths as needed):
```
    install prerequisites  (https://github.com/Dao-AILab/flash-attention)
        pip install packaging
        pip install psutil
        pip install ninja
    install libraries (if needed)
        #sudo apt install amdrocm-core-dev7.14
        sudo apt install amdrocm-core-sdk7.14
        pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "rocm[libraries,devel]==7.14.0"
    download
        git clone https://github.com/Dao-AILab/flash-attention.git
        cd flash-attention
    update env
        export CPLUS_INCLUDE_PATH="$HOME/comfyui-venv_7-14/lib/python3.12/site-packages/_rocm_sdk_core/include:$ROCM_PATH/include:$CPLUS_INCLUDE_PATH"
        export C_INCLUDE_PATH="$CPLUS_INCLUDE_PATH"
        export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$HOME/comfyui-venv_7-14/lib/python3.12/site-packages/_rocm_sdk_core/lib;$HOME/comfyui-venv_7-14/lib/python3.12/site-packages/_rocm_sdk_core/lib/llvm/bin"
        export HIP_CLANG_INCLUDE="/opt/rocm/llvm/lib/clang/23/include"
    fix clang ambiguity  (/usr/bin => clang-17 ,  /opt/rocm/llvm/bin => clang-23)   => put the /opt/rocm version first
        export PATH="/opt/rocm/llvm/bin:$PATH"
        export HIP_CLANG_PATH="/opt/rocm/llvm/bin"
    request CK backend only (don't combine CK with TRITON or the installer will not compile the kernels)
        export FLASH_ATTENTION_TRITON_AMD_ENABLE=FALSE
        export FLASH_ATTENTION_SKIP_CK_BUILD=FALSE
    install
        export MAX_JOBS=4
        export BUILD_TARGET="rocm"
        #export CXXFLAGS="-D__AMDGCN_WAVEFRONT_SIZE=32"    # I used this, but I don't think it is needed for gfx1100
        python setup.py install
            => starts with a warning => Please update to setuptools v70.1  => why? version 81.0.0 is installed...
            => 1869 kernel compiles. the first 900 or so give a warning => desired occupancy was 4294967295, final occupancy is 2
            => and a few more warnings after the 1869 kernel compiles => ignored 'inline' attribute on kernel function 'ParsePhiloxCudaState' [-Wcuda-compat]
            => takes about 4 hours
    if you installed for TRITON instead than for CK, then the installer will have replaced rocm-triton with cuda-triton !!!
        => reinstall triton (not needed for CK-only backend)
        pip install https://repo.amd.com/rocm/whl-multi-arch/triton-3.7.1%2Bgit0263a6a6.rocm7.14.0-cp312-cp312-linux_x86_64.whl
    enable TRITON backend
        if you installed for TRITON instead than for CK, then the installer will have installed amd-aiter 0.0.0
                => this throws an error in ComfyUI => aiter.ops.opus (a16w16) is gfx950-only
                => remove aiter 
            pip uninstall amd-aiter
        install aiter (this will enable the TRITON backend)
            pip install https://github.com/ROCm/aiter/releases/download/v0.1.19/amd_aiter-0.1.19+rocm7.2.manylinux.2.28-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl
    validate
        # should say TRITON
        export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE
        python -c 'import flash_attn, flash_attn.flash_attn_interface as f; print("flash-attn: %s [%s]" % (flash_attn.__version__, "TRITON" if "triton" in f.flash_attn_gpu.__file__.lower() else "CK"))'
        # should say CK
        export FLASH_ATTENTION_TRITON_AMD_ENABLE=FALSE
        python -c 'import flash_attn, flash_attn.flash_attn_interface as f; print("flash-attn: %s [%s]" % (flash_attn.__version__, "TRITON" if "triton" in f.flash_attn_gpu.__file__.lower() else "CK"))'

```
