# [Issue #1038] Build flash-attn takes a lot of time 

source: https://github.com/Dao-AILab/flash-attention/issues/1038
state: open | updated: 2026-07-12T15:56:38Z
labels: 

## 正文

I'm trying to install the flash-attn package but it takes too much time. 
I've made sure that ninja is installed. 
![image](https://github.com/Dao-AILab/flash-attention/assets/59210021/3128acee-8605-4e34-bad5-3ce112351c92)
![image](https://github.com/Dao-AILab/flash-attention/assets/59210021/25157065-2a2f-4526-826a-6fa7655e57e3)


## 评论 (76)

### Ph0rk0z · 2024-07-10

If I ever get out of GH jail: https://github.com/Dao-AILab/flash-attention/pull/1025#issuecomment-2207077088

### tridao · 2024-07-10

yep it takes a long time because of all the templating

### puneeshkhanna · 2024-07-30

Same here

MAX_JOBS=4 pip -v install flash-attn==2.6.3 --no-build-isolation

I used verbose option ; it gets stuck in C++ compilation indefinitely. I tried other versions but same problem.

copying flash_attn/ops/triton/init.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
copying flash_attn/ops/triton/cross_entropy.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
copying flash_attn/ops/triton/k_activations.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
copying flash_attn/ops/triton/layer_norm.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
copying flash_attn/ops/triton/linear.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
copying flash_attn/ops/triton/mlp.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
copying flash_attn/ops/triton/rotary.py -> build/lib.linux-x86_64-cpython-310/flash_attn/ops/triton
running build_ext
/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/falcon-moe/lib/python3.10/site-packages/torch/utils/cpp_extension.py:418: UserWarning: The detected CUDA version (12.2) has a minor version mismatch with the version that was used to compile PyTorch (12.1). Most likely this shouldn't be a problem.
warnings.warn(CUDA_MISMATCH_WARN.format(cuda_str_version, torch.version.cuda))
/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/falcon-moe/lib/python3.10/site-packages/torch/utils/cpp_extension.py:428: UserWarning: There are no g++ version bounds defined for CUDA version 12.2
warnings.warn(f'There are no {compiler_name} version bounds defined for CUDA version {cuda_str_version}')
building 'flash_attn_2_cuda' extension
creating /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310
creating /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310/csrc
creating /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310/csrc/flash_attn
creating /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310/csrc/flash_attn/src
Emitting ninja build file /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310/build.ninja...
Compiling objects...
Using envvar MAX_JOBS (4) as the number of workers...
[1/85] c++ -MMD -MF /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310/csrc/flash_attn/flash_api.o.d -pthread -B /lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/compiler_compat -Wno-unused-result -Wsign-compare -DNDEBUG -fwrapv -O2 -Wall -fPIC -O2 -isystem /lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/include -fPIC -O2 -isystem /lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/include -fPIC -I/tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/csrc/flash_attn -I/tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/csrc/flash_attn/src -I/tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/csrc/cutlass/include -I/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/lib/python3.10/site-packages/torch/include -I/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/lib/python3.10/site-packages/torch/include/TH -I/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/lib/python3.10/site-packages/torch/include/THC -I/usr/local/cuda/include -I/lustre1/tier2/users/puneesh.khanna/miniconda3/envs/venv/include/python3.10 -c -c /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/csrc/flash_attn/flash_api.cpp -o /tmp/pip-install-14eos5qz/flash-attn_021be3b5eaac41e793324f2128cf5d4c/build/temp.linux-x86_64-cpython-310/csrc/flash_attn/flash_api.o -O3 -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=flash_attn_2_cuda -D_GLIBCXX_USE_CXX11_ABI=0

### Rahman2001 · 2024-09-27

How long it takes to finish building the wheel? 
Mine is still building since yesterday. I use GeForce 930MX GPU.

### faaany · 2024-10-23

I am using the docker image "nvidia/cuda:12.1.0-devel-ubuntu22.04", and `pip install flash-attn --no-build-isolation` takes forever...

### JohannesAck · 2024-10-26

Upgrading `pip`, `wheel` and `setuptools` helped me improve the compile time a lot.

```
python -m pip install --upgrade pip wheel setuptools
```

Also consider manually setting the number of jobs (64 requires ~500GB ram so adjust accordingly).

```
MAX_JOBS=64 python -m pip -v install flash-attn --no-build-isolation
```

Without both changes it defaulted to just using a single compilation job for me, taking forever (I gave up after an hour).

Maybe this could be added to the `ninja` disclaimer in the readme, @tridao , although I guess the recommended nvidia container has matching versions installed already.

### Antony-M1 · 2024-11-04

I tried in the **Google Colab L4** machine its taking too much time and I tried in the **Kaggle GPU P100** its installed with in `5 sec`. I don't know what's wrong with the google colab.

### iNLyze · 2024-11-06

I checked memory consumption with `bashtop` and made sure I set `MAX_JOBS` to stay <= 50% memory on average. Total memory is 128 GB.
I also set some limits to higher values
`ulimit -n 4096` and `ulimit -s 16384`. This way you can open enough files and sufficiently large stack size for the deep and complex build process.  
Before making these adjustments the build tasks each got killed due to running out of resources. Now it is building.

### ssb22 · 2024-11-10

For reference I just compiled it on a 2018 Dell laptop (Quadro P1000 GPU) and the build time was about 15 hours.

### MGParisi · 2024-12-20

```
Building wheels for collected packages: flash-attn
  Building wheel for flash-attn (setup.py) ... |
```
Its not stuck, but wow, yea.  Long time here too.  The little swirl thing on the left slowly changes. |/-\|/-\| 

60% of my memory is used, and I got 64gb in this machine. 50% of the CPU is used, so quite a few cores are running.  Nice that its winter, keeping my feet warm. I'm a generation behind on AMD, but its a faster processor, and an 1080ti.

### ixn3rd3mxn · 2024-12-27

I'm still installing it for 7 hours , need answer When will it be finished? XD

### MoonRide303 · 2025-01-03

It took almost 2 hours on my setup (using MAX_JOBS=4). It would be really nice to see some optimizations here.

### ixn3rd3mxn · 2025-01-06

dowload complete is use 9 hr , install in Notebook Asus TUF Gaming Dash F15 FX516PM-HN025T

### paniabhisek · 2025-01-28

Why is it installing very fast from `2.7.x` onwards. I am sure it is not installing fast just to my machine.

### JohnConnor123 · 2025-01-28

`pip install --no-build-isolation flash-attn==2.7.3` takes about 30 seconds while 2.6.x takes >1hour 

### MoonRide303 · 2025-01-28

> pip install --no-build-isolation flash-attn==2.7.3 takes about 30 seconds while 2.6.x takes >1hour

2.7.3 was over 1.5h for me, again - no pre-built binaries for Windows, sadly.

### Ph0rk0z · 2025-02-11

I notice that SM_86 also compiles SM_90 code and much of the compilation is for training and other kernels most do not need for pure inference.

### SPOOKEXE · 2025-02-12

It loves to eat my computer. Currently at 30 minutes compiling.

(7 minutes in)
![Image](https://github.com/user-attachments/assets/7801f5a0-34d8-438a-b524-38027eefbbd4)

(30 minutes in)

![Image](https://github.com/user-attachments/assets/c2c46c46-4de7-4ed3-bd58-17583413bd2a)

Every core:
![Image](https://github.com/user-attachments/assets/04620d43-4a79-426c-afd4-568c565f5ed1)


### SPOOKEXE · 2025-02-12

Compilation time was about 41 minutes - `flash_attn-2.7.4.post1.tar.gz`

### EthanChen1234 · 2025-02-16

nvidia/cuda:12.1.0-devel-ubuntu22.04
pip install flash-attn --no-build-isolation flash-attn==2.7.2.post1

It's too slow building wheel, even if ninja(1.11.1.3) installed.


### EthanChen1234 · 2025-02-17

> nvidia/cuda:12.1.0-devel-ubuntu22.04 pip install flash-attn --no-build-isolation flash-attn==2.7.2.post1
> 
> It's too slow building wheel, even if ninja(1.11.1.3) installed.

about 40 minutes.

### TCNOco · 2025-02-27

Naaah this is insane how does this one package take so long? Surely some optimizations can be made...
I was installing on Windows, but I'm wasting my time. WSL it is, hopefully a prebuilt version will save me.

EDIT: flash-attn installs SUPER quickly on WSL. If you're doing ANYTHING that needs it you can install WSL, build and use your project with many hours to spare vsv building just once on Windows. Consider it.

### LorisTecnology · 2025-03-01

same issues with latest pytorch cu128

### avakado0 · 2025-03-01

> `pip install --no-build-isolation flash-attn==2.7.3` takes about 30 seconds while 2.6.x takes >1hour

Having had the same error with a prebuild model's requirements.txt's reference to flash-attn. Used the 2.7.3 and magic. For me too, on a Tesla V100 instance it took ~30 seconds unlike other versions taking forever

### gterziysky · 2025-03-06

Took `1503.2s` or a little over 25 mins to build `flash-attn 2.7.4.post1` on a 32 core Threadripper PRO (32/64 threads were utilised) using [nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04](https://hub.docker.com/layers/nvidia/cuda/11.8.0-cudnn8-devel-ubuntu22.04/images/sha256-5079d0d0f36cc63050a0f5c010d769c68b8e959c2d2a45f8ec44dd7e5c1bf7f9) (there was some incompatibility with torch 2.6.0 and the latest cuda image which at the time was 12.8.0).

```bash
# after installing ninja
RUN pip3 install flash-attn --no-build-isolation
```

### kunibald413 · 2025-03-08

check prebuild wheels
https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/tag/v0.0.6

### SPOOKEXE · 2025-03-10

> check prebuild wheels https://github.com/mjun0812/flash-attention-prebuild-wheels/releases/tag/v0.0.6

They're all Linux prebuilds - I've been trying to build on Windows and even then the others still have long compile times (which is the issue here).

### LorisTecnology · 2025-03-18

> Compilation time was about 41 minutes - `flash_attn-2.7.4.post1.tar.gz`

on latest pytorch with cuda128? cause i've tested a while ago and with 5090 wasn't working

### KickAssDave · 2025-03-19

> > Compilation time was about 41 minutes - `flash_attn-2.7.4.post1.tar.gz`
> 
> on latest pytorch with cuda128? cause i've tested a while ago and with 5090 wasn't working

I have a 5090 and these three packages work fine together (haven't tested older/newer iterations at this point, but these are pretty new anyway):
torch-2.7.0.dev20250306+cu128-cp312-cp312-win_amd64.whl
torchaudio-2.6.0.dev20250306+cu128-cp312-cp312-win_amd64.whl
torchvision-0.22.0.dev20250307+cu128-cp312-cp312-win_amd64.whl

Of course.. now I am building wheels for flash attention like others and sitting her twiddling thumbs lol...
Building wheels for collected packages: flash-attn
  Building wheel for flash-attn (setup.py) ... \

I did it last night but with versions of the above which don't work with the 50xx series, (hence I am running it again), and it took between 3 and 4 hours on a 9800X3D with 32GB DDR5.  The system wasn't left idle so it could have went faster.

### mirekphd · 2025-03-21

Confirmed. In my `htop` I see unexpected NVIDIA compiler flags for Hopper architecture (`ptxas -arch sm_90`) when I specify Ampere arch. alone using `export TORCH_CUDA_ARCH_LIST="8.0"` (I'd expect only `ptxas -arch sm_80` with that setting). Which is probably a separate bug in itself... "unconditional inclusion of Hopper arch. during compilation" anyone? 

> I notice that SM_86 also compiles SM_90 code and much of the compilation is for training and other kernels most do not need for pure inference.



### HDANILO · 2025-03-27

made an issue my own then I found this, I' ve managed to get the installation running on 5090 windows, its running for 9hrs already. It means it'll work, right? right?

Ninja on...

### omegasrsw · 2025-03-28

> made an issue my own then I found this, I' ve managed to get the installation running on 5090 windows, its running for 9hrs already. It means it'll work, right? right?
> 
> Ninja on...

So is it working bro. I'm on 5080 and stuck at that 

Building wheel for flash-attn (setup.py)

for a really long while


### HDANILO · 2025-03-28

> > made an issue my own then I found this, I' ve managed to get the installation running on 5090 windows, its running for 9hrs already. It means it'll work, right? right?
> > Ninja on...
> 
> So is it working bro. I'm on 5080 and stuck at that
> 
> Building wheel for flash-attn (setup.py)
> 
> for a really long while

It's working yes. Took me 11h on a beefy machine to compile

### omegasrsw · 2025-03-28

> > > made an issue my own then I found this, I' ve managed to get the installation running on 5090 windows, its running for 9hrs already. It means it'll work, right? right?
> > > Ninja on...
> > 
> > 
> > So is it working bro. I'm on 5080 and stuck at that
> > Building wheel for flash-attn (setup.py)
> > for a really long while
> 
> It's working yes. Took me 11h on a beefy machine to compile

ok thanks bro appreciated I'll leave it overnight.

### mthompson0220 · 2025-04-06

Doubling as a CPU/Mem test.

### Sharrnah · 2025-04-14

I made a build for blackwell GPU's here.
I don't have a 50x GPU to test it, but soneone else said it works.

https://github.com/Sharrnah/flash-attention-win/releases

To fully support Blackwell, it also needs a nightly pyTorch version >=2.6.0 as mentioned in the release notes.

### sahilramani · 2025-04-18

For those still struggling with the error, it's important to note that the number of parallel jobs depends directly on how much memory you have. For me, the magic number is 4 and I have 48GB on my WSL2 Ubuntu. Took longer, but it didn't fail. 

`MAX_JOBS=4 pip -v install flash-attn --no-build-isolation`

### Jatts-Art · 2025-04-20

"MAX_JOBS=#" doesnt even work for me at all, and no idea if it was activated once running the command and cannot find any information online about how to go about solving that...

### sahilramani · 2025-04-20

> "MAX_JOBS=#" doesnt even work for me at all, and no idea if it was activated once running the command and cannot find any information online about how to go about solving that...

MAX_JOBS is a ninja option. Make sure you have ninja installed before you run the command.

`pip install ninja` 

Also, the `-v` option in the flash-attn installation is important to give you details on installation progress

### Jatts-Art · 2025-04-21

> > "MAX_JOBS=#" doesnt even work for me at all, and no idea if it was activated once running the command and cannot find any information online about how to go about solving that...
> 
> MAX_JOBS is a ninja option. Make sure you have ninja installed before you run the command.
> 
> `pip install ninja`
> 
> Also, the `-v` option in the flash-attn installation is important to give you details on installation progress

I did install Ninja as well, but still wasn't sure if what I was typing was working. I was typing the jobs command on its own, by itself, btw... so maybe that was part of it? Eventually I decided to use the jobs command within the same line as the install command, rather than separated, as well as including '-v' and yeah it all worked out and I was able to finish what I had wanted to do. Thanks!

### sahilramani · 2025-04-21

> > > "MAX_JOBS=#" doesnt even work for me at all, and no idea if it was activated once running the command and cannot find any information online about how to go about solving that...
> > 
> > 
> > MAX_JOBS is a ninja option. Make sure you have ninja installed before you run the command.
> > `pip install ninja`
> > Also, the `-v` option in the flash-attn installation is important to give you details on installation progress
> 
> I did install Ninja as well, but still wasn't sure if what I was typing was working. I was typing the jobs command on its own, by itself, btw... so maybe that was part of it? Eventually I decided to use the jobs command within the same line as the install command, rather than separated, as well as including '-v' and yeah it all worked out and I was able to finish what I had wanted to do. Thanks!

Yeah, it has to be on the same line. That sets the environment variable for that execution. If you have it on a different line the environment variable won't be set for ninja to use. Glad it worked.

### muhayyo-tash · 2025-05-05

On 2x H200 took around 14 minutes with MAX_JOBS=16

### tamoghnokandar · 2025-05-06

Has anyone tried installing using uv package?

### ighoshsubho · 2025-05-06

I faced the same issue, you could try like this -
1. Check the wheel supported on your system -
```py
import platform
import sys

import torch


def get_cuda_version():
    if torch.cuda.is_available():
        cuda_version = torch.version.cuda
        return f"cu{cuda_version.replace('.', '')[:2]}"  # 例如：cu121
    return "cpu"


def get_torch_version():
    return f"torch{torch.__version__.split('+')[0]}"[:-2]  # 例如：torch2.2


def get_python_version():
    version = sys.version_info
    return f"cp{version.major}{version.minor}"  # 例如：cp310


def get_abi_flag():
    return "abiTRUE" if torch._C._GLIBCXX_USE_CXX11_ABI else "abiFALSE"


def get_platform():
    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == "linux" and machine == "x86_64":
        return "linux_x86_64"
    elif system == "windows" and machine == "amd64":
        return "win_amd64"
    elif system == "darwin" and machine == "x86_64":
        return "macosx_x86_64"
    else:
        raise ValueError(f"Unsupported platform: {system}_{machine}")


def generate_flash_attn_filename(flash_attn_version="2.7.2.post1"):
    cuda_version = get_cuda_version()
    torch_version = get_torch_version()
    python_version = get_python_version()
    abi_flag = get_abi_flag()
    platform_tag = get_platform()

    filename = (
        f"flash_attn-{flash_attn_version}+{cuda_version}{torch_version}cxx11{abi_flag}-"
        f"{python_version}-{python_version}-{platform_tag}.whl"
    )
    return filename
```
2. wget the wheel from the flash_attn releases like so - `wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.4.post1/flash_attn-2.7.4.post1+cu12torch2.2cxx11abiFALSE-cp310-cp310-linux_x86_64.whl`
3. pip install the wheel and you are done!!

### Deskew · 2025-05-08

`MAX_JOBS=128 pip install flash-attn --no-build-isolation`
It took around 30 minutes;



### HorHang · 2025-05-15

It took me only few second by starting with the torch version matching with cuda version that is available in my machine. Then, `pip install flash-attn --no-build-isolation`
`pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124`

$nvidia-smi
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.144.03             Driver Version: 550.144.03     CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA H200                    On  |   00000000:0F:00.0 Off |                    0 |
| N/A   48C    P0            190W /  700W |   25802MiB / 143771MiB |     22%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A     15500      C   ...rkerDict.actor_rollout_update_actor      25784MiB |
+-----------------------------------------------------------------------------------------+
```

$nvcc --version
```
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Thu_Mar_28_02:18:24_PDT_2024
Cuda compilation tools, release 12.4, V12.4.131
Build cuda_12.4.r12.4/compiler.34097967_0
```

### vsahil · 2025-05-17

with MAX_JOBS 40 and 800 GB RAM allocated, it took 40 minutes on a H200 machine

### fxmarty-amd · 2025-05-21

Maybe having a flag to build only fwd kernels would help in some cases.

### qiaodan-cuhk · 2025-05-22

Download .whl files from flash-attn released pages and install them will help. It skips the building wheels stage.

### asahniSC · 2025-05-25

hi guys does this install FA3 or will it require building from source

### JohnSmithToYou · 2025-05-25

You know, I could deal with this **ridiculous** build duration if I got some feedback and I knew the combination of torch etc.. will result in a working configuration when it's finished building. It' just not worth it...

### AshishRam7 · 2025-05-27

> It took me only few second by starting with the torch version matching with cuda version that is available in my machine. Then, `pip install flash-attn --no-build-isolation` `pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124`
> 
> $nvidia-smi
> 
> ```
> +-----------------------------------------------------------------------------------------+
> | NVIDIA-SMI 550.144.03             Driver Version: 550.144.03     CUDA Version: 12.4     |
> |-----------------------------------------+------------------------+----------------------+
> | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
> | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
> |                                         |                        |               MIG M. |
> |=========================================+========================+======================|
> |   0  NVIDIA H200                    On  |   00000000:0F:00.0 Off |                    0 |
> | N/A   48C    P0            190W /  700W |   25802MiB / 143771MiB |     22%      Default |
> |                                         |                        |             Disabled |
> +-----------------------------------------+------------------------+----------------------+
> 
> +-----------------------------------------------------------------------------------------+
> | Processes:                                                                              |
> |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
> |        ID   ID                                                               Usage      |
> |=========================================================================================|
> |    0   N/A  N/A     15500      C   ...rkerDict.actor_rollout_update_actor      25784MiB |
> +-----------------------------------------------------------------------------------------+
> ```
> 
> $nvcc --version
> 
> ```
> nvcc: NVIDIA (R) Cuda compiler driver
> Copyright (c) 2005-2024 NVIDIA Corporation
> Built on Thu_Mar_28_02:18:24_PDT_2024
> Cuda compilation tools, release 12.4, V12.4.131
> Build cuda_12.4.r12.4/compiler.34097967_0
> ```

Thanks this worked for me , just took a minute on a H100 instance(I was struggling for hours using the standard procedure)

### kvbc · 2025-06-01

Low key fell asleep at my desk, I wake up and ts still building

### jakalope · 2025-06-01

It took me a few tries to get all the versions to match for Blackwell support. I ended up with
```
sudo apt-get install nvidia-cuda-toolkit-12-8
echo 'export PATH=/usr/local/cuda-12.8/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.8/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
pip install ninja
pip -v install flash-attn
```

The compilation output finally shows `-gencode arch=compute_120,code=sm_120`. I get build failures when using `MAX_JOBS`, so I'm stuck at 3 workers. Each of the 85 compilation steps is taking between 1 and 5 minutes. I'm on step 14 so far 🤞 

EDIT: After compilation finished, I attempted to run my trainer and got a failure to find a proper cuda kernel. I've updated my above commands to use `pip install --pre torch...`

### cyberyu · 2025-06-02

This could help.  Avoid using Torch 2.7 as now (June 2nd 2025) cause flash-attn has not released version to support that yet, otherwise it will start to build from source.  They key is to guide the installation process to pick the correct prebuilt wheel file. Python 3.9, 3.10, 3.11 should all work.  Upgrading pip wheel setuptools is important, otherwise the packages will not install correctly for some reasons. 

``` python
conda create -n grpo python==3.9
conda activate grpo
python -m pip install --upgrade pip wheel setuptools
pip install torch==2.6.0
pip install transformers --upgrade-strategy only-if-needed
pip install flash-attn --no-build-isolation
pip install peft --upgrade-strategy only-if-needed
```

### lty2226262 · 2025-06-05

https://github.com/Dao-AILab/flash-attention/issues/945#issuecomment-2943250395

### reponum8 · 2025-06-05


Windows wheels (community-maintained)
There are unofficial Windows wheels maintained by the community—one popular source is the “flash-attention-windows-wheel” repository on Hugging Face. For example, in that repo you might see a file named something like:

-----------------------------------------------------------------------------------------
flash_attn-2.7.0.post2+cu124torch2.4.1cxx11abiFALSE-cp310-cp310-win_amd64.whl
-----------------------------------------------------------------------------------------
2.7.0.post2 = flash-attn version

+cu124torch2.4.1 = built against CUDA 12.4 + PyTorch 2.4.1

cxx11abiFALSE = the C++ ABI flag

cp310-cp310 = Python 3.10

win_amd64 = Windows 64-bit
[huggingface.co](https://huggingface.co/lldacing/flash-attention-windows-wheel?utm_source=chatgpt.com)

If you need a Windows wheel that matches your setup (e.g. PyTorch 2.5.1+cu124, Python 3.10), look under that repo’s release assets for something like:

-----------------------------------------------------------------------------------------
flash_attn-2.7.4.post1+cu124torch2.5cxx11abiFALSE-cp310-cp310-win_amd64.whl
-----------------------------------------------------------------------------------------

### haok1402 · 2025-06-13

Please REALLLY make sure `ninja` is in the `$PATH`.

I thought I installed `ninja` and verified with `pip show ninja`, but it turns out, it wasn't in `$PATH`, so setting `MAX_JOBS = 128` means nothing... Wasted for like eight hours or more...

After ensuring proper setup, and confirmed more than one building process are running in `htop`, the build took like under 10 minutes.

![Image](https://github.com/user-attachments/assets/b68de45d-62dd-47fb-afda-05b950ff31f1)

### ps1dr3x · 2025-06-16

Official Linux wheels for Torch 2.7 are out, this should now get the precompiled wheels and avoid compilation:

`pip install --upgrade flash_attn==2.8.0.post2 torch==2.7.1`

### Ednaordinary · 2025-07-12

@mirekphd @Ph0rk0z 

> Confirmed. In my `htop` I see unexpected NVIDIA compiler flags for Hopper architecture (`ptxas -arch sm_90`) when I specify Ampere arch. alone using `export TORCH_CUDA_ARCH_LIST="8.0"` (I'd expect only `ptxas -arch sm_80` with that setting). Which is probably a separate bug in itself... "unconditional inclusion of Hopper arch. during compilation" anyone?
> 
> > I notice that SM_86 also compiles SM_90 code and much of the compilation is for training and other kernels most do not need for pure inference.

Does setting FLASH_ATTN_CUDA_ARCHS="80" help at all? (for non-ampere, see [the first table here](https://arnon.dk/matching-sm-architectures-arch-and-gencode-for-various-nvidia-cards/), options as of posting are 80, 90, 100, and 120, and you can select multiple with like "80;90"). This should compile just for ampere, as the default build in setup.py is for all four architectures :) I don't see anything but sm_80 now and I think I'm getting a speedup (haven't timed it though). Now building with MAX_JOBS=5 on 64gb ram + 5700X @ ~50% cpu within 40 min

### vidixha · 2025-07-16

install flash attn through conda. I found this to be extremely fast

conda install -c conda-forge flash-attn

### Marroh · 2025-07-29

> Upgrading `pip`, `wheel` and `setuptools` helped me improve the compile time a lot.
> 
> ```
> python -m pip install --upgrade pip wheel setuptools
> ```
> 
> Also consider manually setting the number of jobs (64 requires ~500GB ram so adjust accordingly).
> 
> ```
> MAX_JOBS=64 python -m pip -v install flash-attn --no-build-isolation
> ```
> 
> Without both changes it defaulted to just using a single compilation job for me, taking forever (I gave up after an hour).
> 
> Maybe this could be added to the `ninja` disclaimer in the readme, [@tridao](https://github.com/tridao) , although I guess the recommended nvidia container has matching versions installed already.
#
Provide a reference here: `MAX_JOBS=64 python -m pip -v install flash-attn==2.8.2 --no-build-isolation` finished installing within 30 mins on an 8 * A800 server.

### m15kh · 2025-08-11

Installing Flash Attention is a really tedious task; it is suitable for those who haven’t done the previous task very well


### MarsThunder · 2025-09-06

Similar to what @vidixha mentioned.  I was getting all kinds of errors including 'certificates not found' and 'egg_info' fails. This whole process took less than 2 minutes:
`conda install -c conda-forge -c nvidia cuda-python`
`python -m pip install flash-attn`

### fxmarty-amd · 2025-10-21

> Maybe having a flag to build only fwd kernels would help in some cases.

is there still no such flag?

### PaTiToMaSteR · 2025-11-11

My contribution: ...\ComfyUI_windows_portable\python_embeded> ./python.exe -m uv pip install "flash-attn==2.7.4.post1" --no-build-isolation

I'm not extremely sure if it's needed but I install pipx and with pipx I installed "uv" before being able to run that command. Long story short building the wheel was not using all cores no matter what I did. nVidia and others did "uv" and atlas etc... so they did it coz some reason xD

PS: cannot tell u how much is gonna take but I see all cores working on it

### ElenaHUI · 2025-11-21

I successfully resolved this issue by directly downloading the compatible wheel package. Here's how:  

1. Navigate to the official FlashAttention release page: <https://github.com/Dao-AILab/flash-attention/releases/tag/v2.6.3>  
2. Locate and download the wheel file that matches your environment (e.g., CUDA version, PyTorch version, Python version).  
3. Upload the downloaded file to the corresponding file directory and enter the directory.
4. Install the downloaded wheel locally using pip:  
   ```bash
   pip install flash_attn-2.6.3+cu123torch2.3cxx11abiFALSE-cp310-cp310-linux_x86_64.whl
   ```  

### vlatkan · 2025-12-03

rtx 4090 ,still waiting 1 hour 

:building 'flash_attn_2_cuda' extension
creating /workspace/lynx/flash-attention/build/temp.linux-x86_64-cpython-310/csrc/flash_attn
creating /workspace/lynx/flash-attention/build/temp.linux-x86_64-cpython-310/csrc/flash_attn/src
Emitting ninja build file /workspace/lynx/flash-attention/build/temp.linux-x86_64-cpython-310/build.ninja...
Compiling objects...
Using envvar MAX_JOBS (13) as the number of workers.

### LukeLIN-web · 2025-12-06

Same problem 

### mbetrifork · 2025-12-10

I hope someone will bring some attention to this issue. It represents a huge barrier to using flash_attn. Expecting people to sit for 9 hours to install something is not realistic.

### LukeLIN-web · 2025-12-10

At least print sth to tell people can go to  Navigate to the official FlashAttention release page: https://github.com/Dao-AILab/flash-attention/releases/tag/v2.6.3

### AHMEDSANA · 2026-01-29

> I'm trying to install the flash-attn package but it takes too much time. I've made sure that ninja is installed. ![image](https://github.com/Dao-AILab/flash-attention/assets/59210021/3128acee-8605-4e34-bad5-3ce112351c92) ![image](https://github.com/Dao-AILab/flash-attention/assets/59210021/25157065-2a2f-4526-826a-6fa7655e57e3)

i saw someone commented to utilized ninja + supertools as well and MAX_JOBS=4 which sped up the process.

### LukeLIN-web · 2026-01-29

pip install  flash==2.6.1 can use  pre compile package ,  but pip install  flash attn  **without version** cannot. 

### deividsoncs · 2026-02-15

You can use pre-built compiled versions.

Please note that pre-compiled packages may be insecure in some use cases, and they must match the versions of PyTorch and other dependencies. You can avoid spending time compiling by first aligning your environment versions with a pre-compiled flash-attn build using this search tool (you can set the PyTorch, flash-attn, CUDA, OS, and Python versions):

https://mjunya.com/flash-attention-prebuild-wheels/

You can also find a repository with pre-built flash-attn wheels here:

https://github.com/mjun0812/flash-attention-prebuild-wheels

Hope this helps.



### MarksonChen · 2026-03-13

In my case, `pip install flash-attn==2.8.3` took too long because [there does not exist a precompiled wheel of flash-attn==2.8.3 for python 3.10 + pytorch 2.9](https://github.com/Dao-AILab/flash-attention/releases/tag/v2.8.3). 

Running `pip -v install flash-attn` shows:

> DEBUG Guessing wheel URL:  https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/flash_attn-2.8.3+cu12torch2.9cxx11abiTRUE-cp310-cp310-linux_x86_64.whl
> DEBUG Precompiled wheel not found. Building from source...
> DEBUG running build
> DEBUG running build_py
> DEBUG running build_ext
> DEBUG W0313 07:19:09.234000 57115 torch/utils/cpp_extension.py:531] There are no x86_64-linux-gnu-g++ version bounds defined for CUDA version 12.8
> DEBUG building 'flash_attn_2_cuda' extension

Then I switched to Python 3.12, and the precompiled flash-attn wheel was found and installed in seconds.

### chilidog · 2026-07-12

CachyOS: If you have an RTX 40-series card, use 89 (Ada Lovelace). If you are running an RTX 30-series card, change this to 86 (Ampere). RTX 5050 (Blackwell) use 100:   env MAX_JOBS=4 FLASH_ATTN_CUDA_ARCHS=100 uv pip install --no-build-isolation flash-attn
