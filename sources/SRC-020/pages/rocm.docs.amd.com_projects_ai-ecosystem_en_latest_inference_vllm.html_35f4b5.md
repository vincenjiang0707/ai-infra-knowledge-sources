source: https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/inference/vllm.html

# vLLM inference and serving on ROCm[#](https://rocm.docs.amd.com#vllm-inference-and-serving-on-rocm)

vLLM is an open-source library for fast, memory-efficient LLM inference
and serving. This page describes how to set up and run vLLM on AMD GPUs and
APUs using either a prebuilt Docker image (recommended) or pip. It applies to
[supported AMD GPUs and platforms](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support).

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 10.0.0)](https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html).

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 7.14.1)](https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 7.14.0)](https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

Ensure the host system has

[Docker Engine](https://docs.docker.com/engine/install/)installed.

Ensure the host system has [Docker Engine](https://docs.docker.com/engine/install/) installed.

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix](https://rocm.docs.amd.com/en/docs-10.0.0/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 7.14.1)](https://rocm.docs.amd.com/en/docs-7.14.1/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

For Instinct and Radeon devices, ensure your host system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix (ROCm 7.14.0)](https://rocm.docs.amd.com/en/docs-7.14.0/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

Ensure your system has

[Python 3.14](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support)installed and accessible.Install

[uv](https://docs.astral.sh/uv/getting-started/installation/).Note

It’s recommended to use

[uv](https://docs.astral.sh/uv/pip/)to install the vLLM wheel. vLLM has many transitive dependencies, and pip may silently pull incompatible versions from PyPI when installing from a direct wheel URL.`uv pip`

resolves dependencies more predictably, respecting the exact versions bundled with or required by the wheel.

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-10-0-0-i-docker)

Pull the ROCm vLLM 0.27 Docker image.

docker pull rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/vllm:rocm10.0.0_ubuntu24.04_py3.14_pytorch_2.12.0_vllm_0.27.0 \ bash


See also

After setting up your environment, follow the vLLM 0.27 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.27.0/usage/).

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-1-i-docker)

Pull the ROCm vLLM 0.23 Docker image.

docker pull rocm/vllm:rocm7.14.1_cdna_ubuntu24.04_py3.14_pytorch_2.11_vllm_0.23.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/vllm:rocm7.14.1_cdna_ubuntu24.04_py3.14_pytorch_2.11_vllm_0.23.0 \ bash


Pull the ROCm vLLM 0.23 Docker image.

docker pull rocm/vllm:rocm7.14.1_rdna_ubuntu24.04_py3.14_pytorch_2.11_vllm_0.23.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/vllm:rocm7.14.1_rdna_ubuntu24.04_py3.14_pytorch_2.11_vllm_0.23.0 \ bash


See also

After setting up your environment, follow the vLLM 0.23 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.23.0/usage/).

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-0-i-docker)

Pull the ROCm vLLM 0.23 Docker image.

docker pull rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0 \ bash


Pull the ROCm vLLM 0.23 Docker image.

docker pull rocm/vllm:rocm7.14.0_rdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ -v <path/to/your/models>:/app/models \ -e HF_HOME="/app/models" \ rocm/vllm:rocm7.14.0_rdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0 \ bash


See also

After setting up your environment, follow the vLLM 0.23 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.23.0/usage/).

## Install vLLM using pip[#](https://rocm.docs.amd.com#install-vllm-using-pip-i-docker-fam-all-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-fam-ryzen-i-pip-fam-all-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-rocm-ver-7-14-1-i-docker-fam-instinct-fam-radeon-fam-ryzen-rocm-ver-7-14-0-i-docker-fam-instinct-fam-radeon-fam-ryzen-i-pip)

Set up your Python virtual environment.

python3.14 -m venv .venv

Activate your Python virtual environment.

source .venv/bin/activate


Install PyTorch 2.12 in your virtual environment. This should also install the ROCm core libraries as a dependency. See

[Install PyTorch for ROCm](https://rocm.docs.amd.com/frameworks/pytorch/install.html)for full instructions.python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx950]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx950]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx942]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx942]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1200]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1200]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1201]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1201]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1100]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1100]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1101]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1101]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1102]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1102]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1103]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1103]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1151]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1151]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1150]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1150]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1152]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1152]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1153]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1153]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

Install Flash Attention and

[AITER](https://github.com/rocm/aiter).python -m pip install --extra-index-url https://rocm.frameworks.amd.com/whl-multi-arch/vllm/ \ "flash-attn==2.8.3" \ "amd-aiter==0.1.20.post1"

Install the vLLM 0.27 wheel using

`uv pip`

.uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm/vllm/vllm-0.27.1.dev5%2Brocm10.0.0.gf46a9dfe2.d20260826-cp314-cp314-linux_x86_64.whl

Upgrade vLLM’s

`tensorizer`

dependency as a workaround for a[compatibility issue](https://rocm.docs.amd.com#vllm-tensorizer-issue).python -m pip install --upgrade "tensorizer==2.12.1"

Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

To make any of these settings permanent, add it to your shell startup file;

`~/.bashrc`

, for instance.Check your installation.

python -c "import vllm; print('vLLM version:', vllm.__version__)" python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')" python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

After setting up your environment, follow the vLLM 0.27 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.27.0/usage/).

See also

Install PyTorch 2.11 in your virtual environment. This should also install the ROCm core libraries as a dependency.

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx950]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx942]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1200]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1200]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1201]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1201]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1100]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1100]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1101]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1101]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1102]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1102]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1103]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1103]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1151]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1151]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1150]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1150]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1152]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1152]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

Install Flash Attention.

python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/flash-attn/flash_attn-2.8.3-cp314-cp314-linux_x86_64.whl

python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/flash-attn/flash_attn-2.8.3-py3-none-any.whl


Install

[AITER](https://github.com/rocm/aiter).python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/amd-aiter/amd_aiter-0.1.13.post2.dev1%2Bgb32deb267.d20260901-cp314-cp314-linux_x86_64.whl

Install the vLLM 0.23.1 wheel using

`uv pip`

.uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.1.g9ddef7117.d20260901-cp314-cp314-linux_x86_64.whl

Upgrade vLLM’s

`tensorizer`

dependency as a workaround for a[compatibility issue](https://rocm.docs.amd.com#vllm-tensorizer-issue).python -m pip install --upgrade "tensorizer==2.12.1"


Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

Check your installation.

python -c "import vllm; print('vLLM version:', vllm.__version__)" python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')" python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

After setting up your environment, follow the vLLM 0.23.1 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.23.0/usage/).

Install the vLLM 0.23.1 wheel using

`uv pip`

.uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.1.g9ddef7117.d20260831-cp314-cp314-linux_x86_64.whl

Upgrade vLLM’s tensorizer dependency as a workaround for a

[compatibility issue](https://rocm.docs.amd.com#vllm-tensorizer-issue).python -m pip install --upgrade "tensorizer==2.12.1"

Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

Check your installation.

python -c "import vllm; print('vLLM version:', vllm.__version__)" python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')" python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

After setting up your environment, follow the vLLM 0.23 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.23.0/usage/).

See also

Install PyTorch 2.11 in your virtual environment. This should also install the ROCm core libraries as a dependency.

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx950]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx942]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1200]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1200]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1201]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1201]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1100]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1100]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1101]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1101]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1102]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1102]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1103]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1103]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1151]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1151]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1150]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1150]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1152]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1152]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

Install Flash Attention.

python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/flash-attn/flash_attn-2.8.3-cp314-cp314-linux_x86_64.whl

python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/flash-attn/flash_attn-2.8.3-py3-none-any.whl


Install

[AITER](https://github.com/rocm/aiter).python -m pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/amd-aiter/amd_aiter-0.1.13.post2.dev1%2Bgb32deb267-cp314-cp314-linux_x86_64.whl

Install the vLLM 0.23.1 wheel using

`uv pip`

.uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-cdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.0.g9ddef7117.d20260715-cp314-cp314-linux_x86_64.whl

Upgrade vLLM’s

`tensorizer`

dependency as a workaround for a[compatibility issue](https://rocm.docs.amd.com#vllm-tensorizer-issue).python -m pip install --upgrade "tensorizer==2.12.1"


Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

Check your installation.

python -c "import vllm; print('vLLM version:', vllm.__version__)" python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')" python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

After setting up your environment, follow the vLLM 0.23.1 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.23.0/usage/).

Install the vLLM 0.23.1 wheel using

`uv pip`

.uv pip install https://rocm.frameworks.amd.com/whl-multi-arch/vllm-rdna/vllm/vllm-0.23.1.dev1%2Brocm7.14.0.g9ddef7117.d20260715-cp314-cp314-linux_x86_64.whl

Upgrade vLLM’s tensorizer dependency as a workaround for a

[compatibility issue](https://rocm.docs.amd.com#vllm-tensorizer-issue).python -m pip install --upgrade "tensorizer==2.12.1"

Set the following environment variables to prevent errors related to ROCm platform and Flash Attention availability when running vLLM.

export PYTHONPATH=$VIRTUAL_ENV/lib/python3.14/site-packages/_rocm_sdk_core/share/amd_smi export FLASH_ATTENTION_TRITON_AMD_ENABLE=TRUE

Check your installation.

python -c "import vllm; print('vLLM version:', vllm.__version__)" python -c "import torch; print('PyTorch:', torch.__version__); print('HIP available:', torch.cuda.is_available()); print('HIP built:', torch.backends.hip.is_built() if hasattr(torch.backends, 'hip') else 'N/A')" python -c "import flash_attn; print('flash-attn:', flash_attn.__version__)"

After setting up your environment, follow the vLLM 0.23 usage documentation to get started:

[Using vLLM](https://docs.vllm.ai/en/v0.23.0/usage/).

See also

## Known issues[#](https://rocm.docs.amd.com#known-issues-fam-instinct-i-pip)

An incompatibility with vLLM’s tensorizer dependency results in errors when running vLLM. As a workaround, manually bump the tensorizer version in your virtual environment.

python -m pip install --upgrade "tensorizer==2.12.1"


## Known issues[#](https://rocm.docs.amd.com#known-issues-i-docker-fam-all-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-fam-ryzen-i-pip-fam-all-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-rocm-ver-7-14-1-i-docker-fam-instinct-fam-radeon-fam-ryzen-rocm-ver-7-14-0-i-docker-fam-instinct-fam-radeon-fam-ryzen-i-pip-rocm-ver-10-0-0-gfx-gfx950-gfx-gfx942-gfx-gfx1200-gfx-gfx1201-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1152-rocm-ver-7-14-1-gfx-gfx950-gfx-gfx942-gfx-gfx1200-gfx-gfx1201-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-fam-instinct-fam-radeon-fam-ryzen-fam-instinct-fam-instinct-fam-radeon-fam-ryzen-rocm-ver-7-14-0-gfx-gfx950-gfx-gfx942-gfx-gfx1200-gfx-gfx1201-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-fam-instinct-fam-radeon-fam-ryzen-fam-instinct-fam-instinct-fam-radeon-fam-ryzen-fam-instinct-i-pip-fam-radeon-fam-ryzen)

An incompatibility with vLLM’s tensorizer dependency results in errors when running vLLM. As a workaround, manually bump the tensorizer version in your virtual environment.

python -m pip install --upgrade "tensorizer==2.12.1"


Significantly longer warmup times might be observed in some large language model inference workloads on AMD Radeon GPUs using vLLM versions v0.21.0 through v0.25.0. As a workaround, use a vLLM release earlier than v0.21.0 or upgrade to vLLM v0.26.0 or later, which includes a fix for this issue.


Intermittent segmentation faults or GPU hangs might be observed when running some vLLM or ComfyUI workloads on Ryzen AI systems using gfx1103 (RDNA3) GPUs.