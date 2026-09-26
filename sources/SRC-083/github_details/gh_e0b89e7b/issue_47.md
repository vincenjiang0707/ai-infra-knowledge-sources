# [Issue #47] ROCM Support

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/47
state: closed | updated: 2026-02-23T21:15:41Z
labels: Contributions Welcome, ROCm, Cross Platform

## 正文

bitsandbytes seems to be hardcoded to search for specific cuda libraries which don't seem to be provided the same way by rocm

> /root/anaconda3/lib/python3.9/site-packages/bitsandbytes/cuda_setup/paths.py:86: UserWarning: /root/anaconda3 did not contain libcudart.so as expected! Searching further paths...
  warn(
/root/anaconda3/lib/python3.9/site-packages/bitsandbytes/cuda_setup/paths.py:98: UserWarning: /opt/ompi/lib:/opt/rocm/lib:/usr/local/lib: did not contain libcudart.so as expected! Searching further paths...
  warn(
/root/anaconda3/lib/python3.9/site-packages/bitsandbytes/cuda_setup/paths.py:20: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('CompVis/stable-diffusion-v1-4')}
  warn(
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching /usr/local/cuda/lib64...
/root/anaconda3/lib/python3.9/site-packages/bitsandbytes/cuda_setup/paths.py:20: UserWarning: WARNING: The following directories listed in your path were found to be non-existent: {PosixPath('/usr/local/cuda/lib64')}
  warn(
WARNING: No libcudart.so found! Install CUDA or the cudatoolkit package (anaconda)!
CUDA SETUP: Loading binary /root/anaconda3/lib/python3.9/site-packages/bitsandbytes/libbitsandbytes_cpu.so...
/root/anaconda3/lib/python3.9/site-packages/bitsandbytes/cextension.py:48: UserWarning: The installed version of bitsandbytes was compiled without GPU support. 8-bit optimizers and GPU quantization are unavailable.
  warn(


## 评论 (23)

### errnoh · 2022-10-04

+1

Would be great to get this working on AMD hardware if there's no hard technical limitation blocking compatibility. Newer Radeon cards often have quite high VRAM and work really well for ML, main issue remaining is providing library compatibility.

### TimDettmers · 2022-10-10

I personally do not have time to implement ROCm support. If you have experience with ROCm I could guide you through the steps to get a working solution.

### gururise · 2022-12-11

An unofficial working port exists here: https://github.com/broncotc/bitsandbytes-rocm

Would be possible to merge the changes into the official port?

### Jarfeh · 2022-12-12

> An unofficial working port exists here: https://github.com/broncotc/bitsandbytes-rocm
> 
> Would be possible to merge the changes into the official port?

~~Doesn't seem to quite work yet, results in a CUDA_SETUP failed error when I attempt to use it~~

Edit: It seems I just attempted to install using the wrong flags while building. It works great.

### gururise · 2023-06-20

**EDIT**: A slightly newer version based on v0.37 available here:
https://github.com/Titaniumtown/bitsandbytes-rocm/tree/patch-2

### nktice · 2023-07-09

After much searching, I did find something that works - so I'll share it here. 
I've been making notes akin to an install script... Here is what I found 
```
# bitsandbytes rocm
# video guide : https://www.youtube.com/watch?v=2cPsvwONnL8
# https://git.ecker.tech/mrq/bitsandbytes-rocm
## https://github.com/0cc4m/bitsandbytes-rocm
git clone https://git.ecker.tech/mrq/bitsandbytes-rocm.git
cd bitsandbytes-rocm/
pip install -r requirements.txt
make hip
CUDA_VERSION=gfx1030 python setup.py install
```
I have found this makes bitsandbytes work with some things on my GPU...
[ AMD Radeon 6900 XT 16GB ] 
I would like to see these features merged back into the main bitsandbytes - 
so that new versions automatically have them, rather than needing
folks who wrote these mods, to go back and update them to follow updates. 


### yamfun · 2023-07-13

> After much searching, I did find something that works - so I'll share it here. I've been making notes akin to an install script... Here is what I found
> 
> ```
> # bitsandbytes rocm
> # video guide : https://www.youtube.com/watch?v=2cPsvwONnL8
> # https://git.ecker.tech/mrq/bitsandbytes-rocm
> ## https://github.com/0cc4m/bitsandbytes-rocm
> git clone https://git.ecker.tech/mrq/bitsandbytes-rocm.git
> cd bitsandbytes-rocm/
> pip install -r requirements.txt
> make hip
> CUDA_VERSION=gfx1030 python setup.py install
> ```
> 
> I have found this makes bitsandbytes work with some things on my GPU... [ AMD Radeon 6900 XT 16GB ] I would like to see these features merged back into the main bitsandbytes - so that new versions automatically have them, rather than needing folks who wrote these mods, to go back and update them to follow updates.

My AMD kohya setup worked with Lion but I want to try use AdamW8bit like the others. 
So after following this post, I finally got my Kohya to apparently use Adam8bit on Linux + AMD ROCm 5.6 with no more  python errors (thought it doesn't really work when used, see the last paragraph). 

For building at the "make hip" step, I performed some steps like, 
1. Install the meta-package mentioned at https://rocm.docs.amd.com/en/latest/deploy/linux/os-native/package_manager_integration.html (I installed all of them but i guess you guys know exactly which one is needed for the hipcub clang stuff)
2. Makefile line 117 "HIP_LIB := -L$(ROCM_DIR)/lib -L$(ROCM_DIR)/llvm/bin/../lib/clang/15.0.0/lib/linux "changed the 15 to 16 

There are also other steps that I did as some errors appeared during the "make hip" setup battle, but I am not sure whether they mattered or correct:
1. Makefile line 3 "ROCM_DIR := /opt/rocm/" take out the last path slash
2. ops.cuh line 16 "#include <hipblas.h>"  to hipblas/hipblas.h
3. ops.cuh line 17 "#include <hipsparse.h>"  to hipsparse/hipsparse.h


(All these steps only made the bnb-rocm "make hip" errors and Kohya bnb import/usage errors go away,
but when actually using AdamW8bit, the 1st epoch are some weird color artifacts, and the epochs afterwards are all black, and the console saying loss=nan; whereas AdamW and Lion work normally with the same params)


### arlo-phoenix · 2023-08-05

The Adam8bit optimizer issue probably wasn't from ROCm itself, but the general issue that's been fixed in the latest version 0.41.1. I made my own [fork](https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6) that just uses defines to make the CUDA code work with HIP, so it's easier to keep up to date and supports the latest version. Since the patch was just in python though, you could just apply it to the fork you are currently using as well.

### bennmann · 2023-08-05

Hi @arlo-phoenix , nice fork, what would i comment out of the Makefile to test 6900 XT (gfx1030)?

I have already "export HSA_OVERRIDE_GFX_VERSION=10.3.0"

### arlo-phoenix · 2023-08-06

> Hi @arlo-phoenix , nice fork, what would i comment out of the Makefile to test 6900 XT (gfx1030)?
> 
> I have already "export HSA_OVERRIDE_GFX_VERSION=10.3.0"

You shouldn't have to change anything special afaik just doing 

```bash
git clone https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6.git bitsandbytes
cd bitsandbytes

#see makefile comments under hip for more info
#using pip install . since python setup.py install is deprecated
make hip
pip install . 
```

works on a newly created docker using rocm 5.6 ([the one I'm using](https://hub.docker.com/r/rocm/pytorch-nightly)). This has all the environment variables including path setup and since ROCm doesn't have that much documentation I really recommend it. If you don't wanna use docker, you'll need to make sure, that hipcc is at /usr/bin or change the makefile accordingly (I'll probably update it myself at some point to work better out of the box, I just copied it from a previous port). You can also set the env var ROCM_HOME to the path to your rocm install (normally /opt/rocm) if the automatic find function doesn't work and add ```--offload-arch=gfx1030``` to the two hipcc commands if it doesn't use the correct one anyways / just compiles for all. And yes the ```export HSA_OVERRIDE_GFX_VERSION=10.3.0``` is also necessary.

For testing you can then go in the tests folder and use pytest test_optim.py to see what works and what doesn't. I'd be careful with the other tests, some froze my PC. I'd say this is probably because I just excluded some parts of the code as they didn't compile because of the different warp size (it's double at AMD and some static_asserts failed because of that) or the missing hipBLASlt stuff or which I hope it's not actually ROCm library issues. I'll see if I can fix that, I want to try out QLora at some point and I'm pretty sure I need some atleast, but haven't tried that out yet. 

**TLDR:**  
- Requires ROCm 5.6
- export HSA_OVERRIDE_GFX_VERSION=10.3.0
- set ROCM_HOME env and check if hipcc is in /usr/bin or otherwise change the Makefile under hip: to use it
- Add  ```--offload-arch=gfx1030``` to the two hipcc commands
- make hip should work now and afterwards just pip install .
- Only optimizers were tested, rest might freeze your system

### bennmann · 2023-08-06

thank you very much @arlo-phoenix - one more step forward, now the "make hip" is struggling with the below paths for my ROCM 5.6:

```
$ ls /opt/rocm/hip/include/hip/*runtime*
/opt/rocm/hip/include/hip/hip_runtime_api.h  /opt/rocm/hip/include/hip/hip_runtime.h

$make hip
...
...
/home/user/bitsandbytes/csrc/ops.cuh:17:10: fatal error: hip/hip_runtime_api.h: No such file or directory
   17 | #include <hip/hip_runtime_api.h>
      |          ^~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
make: *** [Makefile:124: hip] Error 1

```
can you check to make sure the $ROCM_HOME include makefile references match your installation paths in your fork? is this just my installation of Ubuntu and amdgpu-install rocm PATHs being non-standard in some way? 

### edt-xx · 2023-08-06

I am able to build arlo-phoenix's fork of bitandbytes using the docker image rocm/pytorch.  The nightly version of the image gives errors in make hip though.


### arlo-phoenix · 2023-08-06

All header should be found under $ROCM_HOME/include. To control where it searches for the libraries and headers you could try changing these two
```bash
HIP_INCLUDE := -I $(ROCM_HOME)/include -I $(ROOT_DIR)/csrc -I $(ROOT_DIR)/include 
HIP_LIB := -L $(ROCM_HOME)/lib -lhipblas -lhiprand -lhipsparse
```
like adding -I /opt/rocm/hip/include to the include thing and do that for literally every library, might need to change some headers as well so this is more like a last measure. Does doing `export ROCM_HOME=/opt/rocm-5.6.0` before doing make hip maybe work / do you even have the folder /opt/rocm-5.6.0/include or /opt/rocm/include?

### arlo-phoenix · 2023-08-06

> I am able to build arlo-phoenix's fork of bitandbytes using the docker image rocm/pytorch. The nightly version of the image gives errors in make hip though.

Ok that's weird... I haven't pulled it in a while, but I just tried it out again and it worked for me.  But it's great that rocm/pytorch still works, hope it's useful! I didn't really look too deep into the images and thought just the pytorch version would be different, but apparently it's not, good to know.

### edt-xx · 2023-08-07

I've been using bitandbytes as a requirement for petals.  The latest port to rocm ( git clone https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6.git ) allows a simple petals install in a docker container.   Petals, defaults to a quant-type of nf4. using this gets a bus error.  Things work if --quant-type int8 is passed to petals.  It would be really nice if nf4 could be made to  work in the arlo-phoenix (btw thanks for the port! ) version.  In the interest of repeatabilty: 
```
docker pull rocm/pytorch
sudo docker run -it --network=host --device=/dev/kfd --device=/dev/dri --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined rocm/pytorch
```
(in the running image)
```
cd /home
export HSA_OVERRIDE_GFX_VERSION=10.3.0
git clone https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6.git bitsandbytes
cd bitsandbytes
make hip
pip install pip --upgrade
pip install .
cd ..
pip install --upgrade git+https://github.com/bigscience-workshop/petals
python -m petals.cli.run_server stabilityai/StableBeluga2 --torch_dtype float16 --quant_type int8 --port <an open port>
```

### arlo-phoenix · 2023-08-08

Should work now. Atleast the tests from bitsandbytes for nf4 succeeded. See the [README](https://github.com/arlo-phoenix/bitsandbytes-rocm-5.6/blob/main/README.md) in the fork for updated install instructions (I improved the Makefile to take the ROCM_TARGET as an argument). 

The reason I didn't add this from the beginning and just did an ifndef around it, so it wasn't used with ROCm is, because I didn't know enough about Warp sizes from different devices. So that you can use this, your GPU needs to support wave32. It's supported since RDNA (https://en.wikipedia.org/wiki/RDNA_(microarchitecture)), so I think it should work for most people. 

It will even compile if your GPU doesn't support it, since I forcefully redefine __AMDGCN_WAVEFRONT_SIZE (will throw a lot of warnings and should not be done, but hey it works and couldn't find any alternative) . For whatever reason this takes the wrong value for gfx10.. GPU's and the priority for the issue https://github.com/ROCmSoftwarePlatform/MIOpen/issues/1431 isn't high anymore, so expect the workaround to stay for a while.

To check if your gpu supports it, call ```rocminfo | grep "Wavefront Size"```. If you see 32, great your GPU supports it. If you see 64 it's not the end of the world, but most libraries (including petals) likely use the smallest BLOCK_SIZE 64. This doesn't work with the function[ ```kQuantizeBlockwise```](https://github.com/TimDettmers/bitsandbytes/blob/18e827d666fa2b70a12d539ccedc17aa51b2c97c/csrc/kernels.cu#L724). With the warpSize 64 it will throw these errors at compile time. That function is required by quantize_4bit which is needed for nf4. The next smallest BLOCK_SIZE option is 128.

```bash
/opt/rocm-5.6.0/include/rocprim/block/block_load.hpp:776:5: error: static assertion failed due to requirement 'BlockSize % ::rocprim::device_warp_size() == 0': BlockSize must be a multiple of hardware warpsize

/opt/rocm-5.6.0/include/rocprim/block/block_store.hpp:505:5: error: static assertion failed due to requirement 'BlockSize % ::rocprim::device_warp_size() == 0': BlockSize must be a multiple of hardware warpsize
    static_assert(BlockSize % ::rocprim::device_warp_size() == 0,
```

I have no bloody idea if it's possible to make a workaround. If all modern AMD GPU's support wave32, shouldn't matter, but I couldn't find shit about the CDNA lineup, so if it doesn't support wave32 (which I highly doubt) that's a them problem .-.. You can also get warpSize from torch so it would be possible to catch BLOCK_SIZE 64 when the waveSize is 64, didn't test yet if that also returns the wrong size, probably does.

### edt-xx · 2023-08-09

arlo-phoenix.  Your update of 8 Aug works great with petals.  There was a  bug in petals measuring performance :-/ so ignore the following numbers:  Inferences when from 22.3 to 333.3 tokens/sec (15 x faster) and forward pass thruput when from 4783 to about 1433376 tokens/sec ( 300 x faster)!
 THANKS.

### swumagic · 2023-11-10

Bitsandbytes was not supported windows before, but my method can support windows.（yuhuang）
1  open folder J:\StableDiffusion\sdwebui，Click the address bar of the folder and enter CMD
or WIN+R, CMD  。enter，cd /d J:\StableDiffusion\sdwebui
2  J:\StableDiffusion\sdwebui\py310\python.exe -m pip uninstall bitsandbytes

3 J:\StableDiffusion\sdwebui\py310\python.exe -m pip uninstall bitsandbytes-windows

4 J:\StableDiffusion\sdwebui\py310\python.exe -m pip install https://github.com/jllllll/bitsandbytes-windows-webui/releases/download/wheels/bitsandbytes-0.41.1-py3-none-win_amd64.whl

Replace your SD venv directory file（python.exe Folder） here（J:\StableDiffusion\sdwebui\py310）

### j-dominguez9 · 2024-01-05

Is there anything we can do to get rocm support in main branch? AMD is only going to get bigger market share moving forward and rocm is already supported by most major frameworks/libraries. We can go around bnb for inference, but need it for fine-tuning.

### gigascake · 2024-10-26

i need support gfx908, amd instinct mi100

### Titus-von-Koeller · 2024-10-28

This should be on main in the next 2 months. We re actively working on this, among other high impact things.

Thanks for your patience. You can already pip install the alpha release: Please reference the installation instructions in our official docs and give us feedback about your experience to help us deliver the best once merging to main. Thanks!

### mrs83 · 2025-11-05

FYI https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1608#issuecomment-3492751299

### matthewdouglas · 2026-02-23

I'm going to close this as we've started shipping ROCm wheels to PyPI since [v0.49.0](https://github.com/bitsandbytes-foundation/bitsandbytes/releases/tag/0.49.0). We can track more specific issues separately, but we'll consider this feature request complete.
