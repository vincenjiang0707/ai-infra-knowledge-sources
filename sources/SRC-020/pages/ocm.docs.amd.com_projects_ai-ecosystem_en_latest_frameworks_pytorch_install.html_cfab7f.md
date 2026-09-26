source: https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/pytorch/install.html

# Install PyTorch for ROCm[#](https://rocm.docs.amd.com#install-pytorch-for-rocm)

This pages guides you through installing PyTorch with ROCm support on AMD
hardware. It applies to [supported AMD GPUs and platforms](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support).

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

Ensure your system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html).

Ensure your system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

Ensure the host system has

[Docker Engine](https://docs.docker.com/engine/install/)installed.

Ensure your system has a

[supported Python version](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support)installed and accessible:**3.11, 3.12, 3.13, or 3.14**.

Complete the ROCm Core SDK installation prerequisites. See

[Prerequisites (Install ROCm 10.0.0)](https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html#prerequisites)for instructions.

Complete the ROCm Core SDK installation prerequisites. See

[Prerequisites (Install ROCm 7.14.1)](https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html#prerequisites)for instructions.

Complete the ROCm Core SDK installation prerequisites. See

[Prerequisites (Install ROCm 7.14.0)](https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html#prerequisites)for instructions.

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-10-0-0-i-docker)

Pull the ROCm PyTorch 2.13.0 Docker image.

docker pull rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.13.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.13_pytorch_release_2.13.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.12_pytorch_release_2.13.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.11_pytorch_release_2.13.0


Pull the ROCm PyTorch 2.12.0 Docker image.

docker pull rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.13_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.12_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.11_pytorch_release_2.12.0


Pull the ROCm PyTorch 2.11.0 Docker image.

docker pull rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.13_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.12_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm10.0_ubuntu24.04_py3.11_pytorch_release_2.11.0


Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.13.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.13_pytorch_release_2.13.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.12_pytorch_release_2.13.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.11_pytorch_release_2.13.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.13_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.12_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.11_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.13_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.12_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm10.0_ubuntu24.04_py3.11_pytorch_release_2.11.0 \ bash


## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-1-i-docker)

Pull the ROCm PyTorch 2.12.0 Docker image.

docker pull rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.12.0


Pull the ROCm PyTorch 2.11.0 Docker image.

docker pull rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.11.0


Pull the ROCm PyTorch 2.10.0 Docker image.

docker pull rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.10.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.10.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.10.0

docker pull rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.10.0


Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu26.04_py3.14_pytorch_release_2.10.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.13_pytorch_release_2.10.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.12_pytorch_release_2.10.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14.1_ubuntu24.04_py3.11_pytorch_release_2.10.0 \ bash


## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-0-i-docker)

Pull the ROCm PyTorch 2.12.0 Docker image.

docker pull rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.12.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.12.0


Pull the ROCm PyTorch 2.11.0 Docker image.

docker pull rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.11.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.11.0


Pull the ROCm PyTorch 2.10.0 Docker image.

docker pull rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.10.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.10.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.10.0

docker pull rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.10.0


Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.12.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.11.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu26.04_py3.14_pytorch_release_2.10.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.13_pytorch_release_2.10.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.12_pytorch_release_2.10.0 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/pytorch:rocm7.14_ubuntu24.04_py3.11_pytorch_release_2.10.0 \ bash


## Install PyTorch using pip[#](https://rocm.docs.amd.com#install-pytorch-using-pip-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-i-docker-i-pip-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-pytorch-ver-2-13-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-13-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-rocm-ver-7-14-1-i-docker-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-rocm-ver-7-14-0-i-docker-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-i-pip)

Set up your Python virtual environment.

python3.14 -m venv .venv

py -3.14 -m venv .venv

python3.13 -m venv .venv

py -3.13 -m venv .venv

python3.12 -m venv .venv

py -3.12 -m venv .venv

python3.11 -m venv .venv

py -3.11 -m venv .venv

Activate your Python virtual environment. For example:

source .venv/bin/activate

.venv\Scripts\activate


Install the appropriate ROCm-enabled PyTorch libraries for your operating system and AMD hardware architecture.

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-all]==2.13.0+rocm10.0.0" \ "torchvision[device-all]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-all]==2.12.0+rocm10.0.0" \ "torchvision[device-all]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-all]==2.13.0+rocm10.0.0" "torchvision[device-all]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-all]==2.11.0+rocm10.0.0" \ "torchvision[device-all]==0.26.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx950]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx950]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx950]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx950]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx950]==2.11.0+rocm10.0.0" \ "torchvision[device-gfx950]==0.26.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx942]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx942]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx942]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx942]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx942]==2.11.0+rocm10.0.0" \ "torchvision[device-gfx942]==0.26.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx90a]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx90a]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx90a]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx90a]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx90a]==2.11.0+rocm10.0.0" \ "torchvision[device-gfx90a]==0.26.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx908]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx908]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx908]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx908]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx908]==2.11.0+rocm10.0.0" \ "torchvision[device-gfx908]==0.26.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1200]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1200]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1200]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1200]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1200]==2.13.0+rocm10.0.0" "torchvision[device-gfx1200]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1201]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1201]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1201]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1201]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1201]==2.13.0+rocm10.0.0" "torchvision[device-gfx1201]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1100]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1100]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1100]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1100]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1100]==2.13.0+rocm10.0.0" "torchvision[device-gfx1100]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1101]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1101]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1101]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1101]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1101]==2.13.0+rocm10.0.0" "torchvision[device-gfx1101]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1102]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1102]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1102]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1102]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1102]==2.13.0+rocm10.0.0" "torchvision[device-gfx1102]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1103]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1103]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1103]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1103]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1103]==2.13.0+rocm10.0.0" "torchvision[device-gfx1103]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1030]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1030]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1030]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1030]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1030]==2.13.0+rocm10.0.0" "torchvision[device-gfx1030]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1151]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1151]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1151]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1151]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1151]==2.13.0+rocm10.0.0" "torchvision[device-gfx1151]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1150]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1150]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1150]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1150]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1150]==2.13.0+rocm10.0.0" "torchvision[device-gfx1150]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1152]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1152]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1152]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1152]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1152]==2.13.0+rocm10.0.0" "torchvision[device-gfx1152]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1153]==2.13.0+rocm10.0.0" \ "torchvision[device-gfx1153]==0.28.0+rocm10.0.0" \ "torchaudio==2.11.0.2+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "torch[device-gfx1153]==2.12.0+rocm10.0.0" \ "torchvision[device-gfx1153]==0.27.0+rocm10.0.0" \ "torchaudio==2.11.0+rocm10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "torch[device-gfx1153]==2.13.0+rocm10.0.0" "torchvision[device-gfx1153]==0.28.0+rocm10.0.0" "torchaudio==2.11.0.2+rocm10.0.0"


Install the appropriate ROCm-enabled PyTorch libraries for your operating system and AMD hardware architecture.

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-all]==2.12.0+rocm7.14.1" \ "torchvision[device-all]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-all]==2.12.0+rocm7.14.1" "torchvision[device-all]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-all]==2.11.0+rocm7.14.1" \ "torchvision[device-all]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-all]==2.10.0+rocm7.14.1" \ "torchvision[device-all]==0.25.0+rocm7.14.1" \ "torchaudio==2.10.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx950]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx950]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.10.0+rocm7.14.1" \ "torchvision[device-gfx950]==0.25.0+rocm7.14.1" \ "torchaudio==2.10.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx942]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx942]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.10.0+rocm7.14.1" \ "torchvision[device-gfx942]==0.25.0+rocm7.14.1" \ "torchaudio==2.10.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx90a]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx90a]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx90a]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx90a]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx90a]==2.10.0+rocm7.14.1" \ "torchvision[device-gfx90a]==0.25.0+rocm7.14.1" \ "torchaudio==2.10.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx908]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx908]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx908]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx908]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx908]==2.10.0+rocm7.14.1" \ "torchvision[device-gfx908]==0.25.0+rocm7.14.1" \ "torchaudio==2.10.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1200]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1200]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1200]==2.12.0+rocm7.14.1" "torchvision[device-gfx1200]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1200]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1200]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1201]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1201]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1201]==2.12.0+rocm7.14.1" "torchvision[device-gfx1201]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1201]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1201]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1100]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1100]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1100]==2.12.0+rocm7.14.1" "torchvision[device-gfx1100]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1100]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1100]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1101]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1101]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1101]==2.12.0+rocm7.14.1" "torchvision[device-gfx1101]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1101]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1101]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1102]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1102]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1102]==2.12.0+rocm7.14.1" "torchvision[device-gfx1102]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1102]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1102]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1103]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1103]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1103]==2.12.0+rocm7.14.1" "torchvision[device-gfx1103]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1103]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1103]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1030]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1030]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1030]==2.12.0+rocm7.14.1" "torchvision[device-gfx1030]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1030]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1030]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1151]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1151]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1151]==2.12.0+rocm7.14.1" "torchvision[device-gfx1151]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1151]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1151]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1150]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1150]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1150]==2.12.0+rocm7.14.1" "torchvision[device-gfx1150]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1150]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1150]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1152]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1152]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1152]==2.12.0+rocm7.14.1" "torchvision[device-gfx1152]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1152]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1152]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1153]==2.12.0+rocm7.14.1" \ "torchvision[device-gfx1153]==0.27.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1153]==2.12.0+rocm7.14.1" "torchvision[device-gfx1153]==0.27.0+rocm7.14.1" "torchaudio==2.11.0+rocm7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1153]==2.11.0+rocm7.14.1" \ "torchvision[device-gfx1153]==0.26.0+rocm7.14.1" \ "torchaudio==2.11.0+rocm7.14.1"


Install the appropriate ROCm-enabled PyTorch libraries for your operating system and AMD hardware architecture.

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-all]==2.12.0+rocm7.14.0" \ "torchvision[device-all]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-all]==2.12.0+rocm7.14.0" "torchvision[device-all]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-all]==2.11.0+rocm7.14.0" \ "torchvision[device-all]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-all]==2.10.0+rocm7.14.0" \ "torchvision[device-all]==0.25.0+rocm7.14.0" \ "torchaudio==2.10.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx950]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx950]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx950]==2.10.0+rocm7.14.0" \ "torchvision[device-gfx950]==0.25.0+rocm7.14.0" \ "torchaudio==2.10.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx942]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx942]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx942]==2.10.0+rocm7.14.0" \ "torchvision[device-gfx942]==0.25.0+rocm7.14.0" \ "torchaudio==2.10.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx90a]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx90a]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx90a]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx90a]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx90a]==2.10.0+rocm7.14.0" \ "torchvision[device-gfx90a]==0.25.0+rocm7.14.0" \ "torchaudio==2.10.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx908]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx908]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx908]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx908]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx908]==2.10.0+rocm7.14.0" \ "torchvision[device-gfx908]==0.25.0+rocm7.14.0" \ "torchaudio==2.10.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1200]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1200]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1200]==2.12.0+rocm7.14.0" "torchvision[device-gfx1200]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1200]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1200]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1201]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1201]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1201]==2.12.0+rocm7.14.0" "torchvision[device-gfx1201]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1201]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1201]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1100]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1100]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1100]==2.12.0+rocm7.14.0" "torchvision[device-gfx1100]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1100]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1100]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1101]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1101]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1101]==2.12.0+rocm7.14.0" "torchvision[device-gfx1101]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1101]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1101]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1102]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1102]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1102]==2.12.0+rocm7.14.0" "torchvision[device-gfx1102]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1102]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1102]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1103]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1103]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1103]==2.12.0+rocm7.14.0" "torchvision[device-gfx1103]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1103]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1103]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1030]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1030]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1030]==2.12.0+rocm7.14.0" "torchvision[device-gfx1030]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1030]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1030]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1151]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1151]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1151]==2.12.0+rocm7.14.0" "torchvision[device-gfx1151]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1151]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1151]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1150]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1150]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1150]==2.12.0+rocm7.14.0" "torchvision[device-gfx1150]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1150]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1150]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1152]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1152]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1152]==2.12.0+rocm7.14.0" "torchvision[device-gfx1152]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1152]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1152]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1153]==2.12.0+rocm7.14.0" \ "torchvision[device-gfx1153]==0.27.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ "torch[device-gfx1153]==2.12.0+rocm7.14.0" "torchvision[device-gfx1153]==0.27.0+rocm7.14.0" "torchaudio==2.11.0+rocm7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "torch[device-gfx1153]==2.11.0+rocm7.14.0" \ "torchvision[device-gfx1153]==0.26.0+rocm7.14.0" \ "torchaudio==2.11.0+rocm7.14.0"


Verify your PyTorch installation.

python -c "import torch; print(torch.cuda.is_available())"

This prints

`True`

if PyTorch and ROCm are installed properly and your AMD GPUs are detected.

## Known issues[#](https://rocm.docs.amd.com#known-issues-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-i-docker-i-pip-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-pytorch-ver-2-13-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-13-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-rocm-ver-7-14-1-i-docker-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-rocm-ver-7-14-0-i-docker-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-i-pip-os-linux-os-windows-os-linux-os-windows-os-linux-os-windows-os-linux-os-windows-os-linux-os-windows-rocm-ver-10-0-0-fam-all-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx950-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx942-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx90a-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx908-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx1200-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1201-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1100-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1101-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1102-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1103-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1030-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1151-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1150-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1152-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1153-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-rocm-ver-7-14-1-fam-all-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx950-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx942-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx90a-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx908-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx1200-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1201-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1100-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1101-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1102-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1103-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1030-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1151-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1150-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1152-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1153-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-rocm-ver-7-14-0-fam-all-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx950-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx942-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx90a-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx908-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx1200-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1201-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1100-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1101-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1102-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1103-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1030-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1151-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1150-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1152-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1153-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-fam-instinct-rocm-ver-10-0-0)

Hugging Face model training workloads might see 9–25% lower training throughput on AMD Instinct MI350X (gfx950) GPUs, including BART, GPT-2, DiT (Diffusion Transformers), BERT, Llama 2 70B Chat, and RoBERTa-large. This occurs because AOTriton 0.13b selects a suboptimal flash-attention backward kernel instead of the faster 3-kernel split used in AOTriton 0.11.2b. As a workaround, rebuild PyTorch and pin AOTriton to version 0.11.2b.


## Known issues[#](https://rocm.docs.amd.com#known-issues-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-i-docker-i-pip-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-pytorch-ver-2-13-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-13-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-rocm-ver-7-14-1-i-docker-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-rocm-ver-7-14-0-i-docker-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-pytorch-ver-2-12-0-pytorch-ver-2-11-0-pytorch-ver-2-10-0-i-pip-os-linux-os-windows-os-linux-os-windows-os-linux-os-windows-os-linux-os-windows-os-linux-os-windows-rocm-ver-10-0-0-fam-all-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx950-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx942-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx90a-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx908-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-gfx-gfx1200-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1201-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1100-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1101-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1102-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1103-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1030-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1151-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1150-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1152-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-gfx-gfx1153-pytorch-ver-2-13-0-os-linux-pytorch-ver-2-12-0-os-linux-os-windows-rocm-ver-7-14-1-fam-all-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx950-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx942-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx90a-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx908-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx1200-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1201-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1100-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1101-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1102-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1103-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1030-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1151-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1150-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1152-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1153-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-rocm-ver-7-14-0-fam-all-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx950-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx942-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx90a-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx908-pytorch-ver-2-12-0-os-linux-pytorch-ver-2-11-0-os-linux-pytorch-ver-2-10-0-os-linux-gfx-gfx1200-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1201-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1100-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1101-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1102-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1103-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1030-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1151-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1150-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1152-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-gfx-gfx1153-pytorch-ver-2-12-0-os-linux-os-windows-pytorch-ver-2-11-0-os-linux-fam-instinct-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0)

On Linux, importing PyTorch might display a rocSHMEM error message about a missing

`libnuma`

library.`E-001h rocSHMEM Could not open libnuma. Returning NUMAWrapper@src/gda/numa_wrapper.cpp:48`

While

`libnuma`

is not required for the normal functioning of rocSHMEM, you can resolve this message by installing the corresponding development package using your Linux distribution’s package manager:sudo apt update && sudo apt install libnuma-dev

sudo dnf install numactl-devel

sudo zypper install libnuma-devel


Lower-than-expected performance might be observed in some large language model inference workloads, including vLLM FP16 decode workloads with batch sizes of 8 or greater, on AMD Radeon RX 7900 Series Graphics, AMD Radeon RX 7800 XT Graphics, and AMD Ryzen AI MAX / MAX+ Series Processors when using PyTorch versions earlier than 2.14. As a workaround, set the TORCH_BLAS_PREFER_HIPBLASLT=1 environment variable to use the hipBLASLt backend. This setting becomes the default for these architectures in PyTorch 2.14.

PyTorch training and fine-tuning workloads using Llama-Factory or Unsloth might experience GPU resets or application crashes on some AMD Radeon graphics products, such as the Radeon RX 9070 Series and Radeon AI PRO R9700. As a workaround, set the

`TORCH_BLAS_PREFER_HIPBLASLT=0`

environment variable to disable hipBLASLt for training and fine-tuning workloads. This workaround might result in performance degradation.