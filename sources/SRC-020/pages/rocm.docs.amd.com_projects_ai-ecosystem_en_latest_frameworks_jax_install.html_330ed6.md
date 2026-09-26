source: https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/jax/install.html

# Install JAX for ROCm[#](https://rocm.docs.amd.com#install-jax-for-rocm)

This page guides you through installing JAX with ROCm support on AMD hardware.
It applies to [supported AMD GPUs and platforms](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support).

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

Ensure your system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/index.html).

Ensure your system has the AMD GPU Driver (amdgpu) installed. See the

[ROCm compatibility matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)for driver support information. For installation instructions, see the[AMD GPU Driver documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.40.1/index.html).

Ensure the host system has

[Docker Engine](https://docs.docker.com/engine/install/)installed.

Ensure your system has a

[supported Python version](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support)installed and accessible:**3.11, 3.12, 3.13, or 3.14**.

Ensure your system has a

[supported Python version](https://rocm.docs.amd.com/en/latest/about/release-notes.html#ai-ecosystem-support)installed and accessible:**3.12, 3.13, or 3.14**.

Complete the ROCm Core SDK installation prerequisites for installing via pip. See

[Prerequisites (Install ROCm 10.0.0)](https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html#prerequisites)for instructions.

Complete the ROCm Core SDK installation prerequisites for installing via pip. See

[Prerequisites (Install ROCm 7.14.1)](https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html#prerequisites)for instructions.

Complete the ROCm Core SDK installation prerequisites for installing via pip. See

[Prerequisites (Install ROCm 7.14.0)](https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html#prerequisites)for instructions.

Important

Unlike [PyTorch](https://rocm.docs.amd.com/pytorch/install.html), the JAX packages
don’t automatically install ROCm library and device packages as
dependencies. The following section includes recommended instructions to
install ROCm in a Python virtual environment alongside JAX. See [Install
ROCm](https://rocm.docs.amd.com/en/latest/install/rocm.html) for other
installation methods.

## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-10-0-0-i-docker)

Pull the ROCm JAX 0.11.0 Docker image.

docker pull rocm/jax:rocm10.0-jax0.11.0-py3.14

docker pull rocm/jax:rocm10.0-jax0.11.0-py3.13

docker pull rocm/jax:rocm10.0-jax0.11.0-py3.12

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.11.0-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.11.0-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.11.0-py3.12 \ bash


Pull the ROCm JAX 0.10.2 Docker image.

docker pull rocm/jax:rocm10.0-jax0.10.2-py3.14

docker pull rocm/jax:rocm10.0-jax0.10.2-py3.13

docker pull rocm/jax:rocm10.0-jax0.10.2-py3.12

docker pull rocm/jax:rocm10.0-jax0.10.2-py3.11

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.2-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.2-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.2-py3.12 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.2-py3.11 \ bash


Pull the ROCm JAX 0.10.0 Docker image.

docker pull rocm/jax:rocm10.0-jax0.10.0-py3.14

docker pull rocm/jax:rocm10.0-jax0.10.0-py3.13

docker pull rocm/jax:rocm10.0-jax0.10.0-py3.12

docker pull rocm/jax:rocm10.0-jax0.10.0-py3.11

Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.0-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.0-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.0-py3.12 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm10.0-jax0.10.0-py3.11 \ bash


## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-1-i-docker)

Pull the ROCm JAX 0.10.0 Docker image.

docker pull rocm/jax:rocm7.14.1-jax0.10.0-py3.14

docker pull rocm/jax:rocm7.14.1-jax0.10.0-py3.13

docker pull rocm/jax:rocm7.14.1-jax0.10.0-py3.12

docker pull rocm/jax:rocm7.14.1-jax0.10.0-py3.11


Pull the ROCm JAX 0.9.1 Docker image.

docker pull rocm/jax:rocm7.14.1-jax0.9.1-py3.14

docker pull rocm/jax:rocm7.14.1-jax0.9.1-py3.13

docker pull rocm/jax:rocm7.14.1-jax0.9.1-py3.12

docker pull rocm/jax:rocm7.14.1-jax0.9.1-py3.11


Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.10.0-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.10.0-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.10.0-py3.12 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.10.0-py3.11 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.9.1-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.9.1-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.9.1-py3.12 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14.1-jax0.9.1-py3.11 \ bash


## Get started[#](https://rocm.docs.amd.com#get-started-rocm-ver-7-14-0-i-docker)

Pull the ROCm JAX 0.10.0 Docker image.

docker pull rocm/jax:rocm7.14-jax0.10.0-py3.14

docker pull rocm/jax:rocm7.14-jax0.10.0-py3.13

docker pull rocm/jax:rocm7.14-jax0.10.0-py3.12

docker pull rocm/jax:rocm7.14-jax0.10.0-py3.11


Pull the ROCm JAX 0.9.1 Docker image.

docker pull rocm/jax:rocm7.14-jax0.9.1-py3.14

docker pull rocm/jax:rocm7.14-jax0.9.1-py3.13

docker pull rocm/jax:rocm7.14-jax0.9.1-py3.12

docker pull rocm/jax:rocm7.14-jax0.9.1-py3.11


Start the Docker container.

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.10.0-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.10.0-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.10.0-py3.12 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.10.0-py3.11 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.9.1-py3.14 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.9.1-py3.13 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.9.1-py3.12 \ bash

docker run -it --rm \ --device /dev/kfd \ --device /dev/dri \ --network=host \ --ipc=host \ --group-add=video \ --cap-add=SYS_PTRACE \ --security-opt seccomp=unconfined \ rocm/jax:rocm7.14-jax0.9.1-py3.11 \ bash


## Install JAX using pip[#](https://rocm.docs.amd.com#install-jax-using-pip-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-0-i-docker-i-pip-jax-ver-0-10-2-jax-ver-0-10-0-jax-ver-0-9-1-jax-ver-0-11-0-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-jax-ver-0-11-0-jax-ver-0-10-2-jax-ver-0-10-0-rocm-ver-7-14-1-i-docker-jax-ver-0-10-0-jax-ver-0-9-1-jax-ver-0-10-0-jax-ver-0-9-1-rocm-ver-7-14-0-i-docker-jax-ver-0-10-0-jax-ver-0-9-1-jax-ver-0-10-0-jax-ver-0-9-1-i-pip)

For prerequisite steps and post-installation recommendations, see the [ROCm
installation instructions](https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html).

For prerequisite steps and post-installation recommendations, see the [ROCm
installation instructions](https://rocm.docs.amd.com/en/docs-7.14.1/install/rocm.html).

For prerequisite steps and post-installation recommendations, see the [ROCm
installation instructions](https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html).

Set up your Python virtual environment.

python3.13 -m venv .venv

python3.12 -m venv .venv

python3.11 -m venv .venv

python3.14 -m venv .venv

python3.13 -m venv .venv

python3.12 -m venv .venv

python3.11 -m venv .venv

Activate your Python virtual environment.

source .venv/bin/activate


If you don’t have an existing ROCm installation, install ROCm using the following command; see the

[ROCm 10.0.0 installation instructions](https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html)for complete guidance. Otherwise, proceed to installing JAX libraries.python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-all]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx950]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx942]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx90a]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx1200]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx1201]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx1100]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx1101]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx1102]==10.0.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "rocm[libraries,device-gfx1103]==10.0.0"

Install the ROCm-enabled JAX libraries.

Note

The

`jax`

and`jaxlib`

packages are not published to the AMD package repository. After installing GFX architecture-based`jax_rocm10_plugin`

and`jax_rocm10_pjrt`

packages from the AMD repository, install`jax`

and`jaxlib`

from[PyPI](https://pypi.org/project/jax).python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "jax_rocm10_plugin==0.11.0+rocm10.0.0" \ "jax_rocm10_pjrt==0.11.0+rocm10.0.0" # Install jax from PyPI python -m pip install \ "jax==0.11.0" \ "jaxlib==0.11.0"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "jax_rocm10_plugin==0.10.2+rocm10.0.0" \ "jax_rocm10_pjrt==0.10.2+rocm10.0.0" # Install jax from PyPI python -m pip install \ "jax==0.10.2" \ "jaxlib==0.10.2"

python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ \ "jax_rocm10_plugin==0.10.0+rocm10.0.0" \ "jax_rocm10_pjrt==0.10.0+rocm10.0.0" # Install jax from PyPI python -m pip install \ "jax==0.10.0" \ "jaxlib==0.10.0"


If you don’t have an existing ROCm installation, install ROCm using the following command; otherwise, proceed to installing JAX libraries.

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-all]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx950]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx942]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx90a]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1200]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1201]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1100]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1101]==7.14.1"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1102]==7.14.1"

Install the ROCm-enabled JAX libraries.

Note

The

`jax`

and`jaxlib`

packages are not published to the AMD package repository. After installing GFX architecture-based`jax_rocm7_plugin`

and`jax_rocm7_pjrt`

packages from the AMD repository, install`jax`

and`jaxlib`

from[PyPI](https://pypi.org/project/jax).python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "jax_rocm7_plugin==0.10.0+rocm7.14.1" \ "jax_rocm7_pjrt==0.10.0+rocm7.14.1" # Install jax from PyPI python -m pip install \ "jax==0.10.0" \ "jaxlib==0.10.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "jax_rocm7_plugin==0.9.1+rocm7.14.1" \ "jax_rocm7_pjrt==0.9.1+rocm7.14.1" # Install jax from PyPI python -m pip install \ "jax==0.9.1" \ "jaxlib==0.9.1"


If you don’t have an existing ROCm installation, install ROCm using the following command; otherwise, proceed to installing JAX libraries.

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-all]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx950]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx942]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx90a]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1200]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1201]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1100]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1101]==7.14.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "rocm[libraries,device-gfx1102]==7.14.0"

Install the ROCm-enabled JAX libraries.

Note

The

`jax`

and`jaxlib`

packages are not published to the AMD package repository. After installing GFX architecture-based`jax_rocm7_plugin`

and`jax_rocm7_pjrt`

packages from the AMD repository, install`jax`

and`jaxlib`

from[PyPI](https://pypi.org/project/jax).python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "jax_rocm7_plugin==0.10.0+rocm7.14.0" \ "jax_rocm7_pjrt==0.10.0+rocm7.14.0" # Install jax from PyPI python -m pip install \ "jax==0.10.0" \ "jaxlib==0.10.0"

python -m pip install --index-url https://repo.amd.com/rocm/whl-multi-arch/ \ "jax_rocm7_plugin==0.9.1+rocm7.14.0" \ "jax_rocm7_pjrt==0.9.1+rocm7.14.0" # Install jax from PyPI python -m pip install \ "jax==0.9.1" \ "jaxlib==0.9.1"


Verify your JAX installation.

python -c "import jax; print(jax.devices())"

This prints something like

`[RocmDevice(id=0)]`

if JAX and ROCm are installed properly and your AMD GPUs are detected.

## Known issues[#](https://rocm.docs.amd.com#known-issues-fam-instinct-fam-radeon-rocm-ver-10-0-0-rocm-ver-7-14-0-i-docker-i-pip-jax-ver-0-10-2-jax-ver-0-10-0-jax-ver-0-9-1-jax-ver-0-11-0-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-rocm-ver-10-0-0-i-docker-jax-ver-0-11-0-jax-ver-0-10-2-jax-ver-0-10-0-rocm-ver-7-14-1-i-docker-jax-ver-0-10-0-jax-ver-0-9-1-jax-ver-0-10-0-jax-ver-0-9-1-rocm-ver-7-14-0-i-docker-jax-ver-0-10-0-jax-ver-0-9-1-jax-ver-0-10-0-jax-ver-0-9-1-i-pip-rocm-ver-10-0-0-rocm-ver-7-14-1-rocm-ver-7-14-0-jax-ver-0-11-0-jax-ver-0-10-2-jax-ver-0-10-0-rocm-ver-10-0-0-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx1200-gfx-gfx1201-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-jax-ver-0-11-0-jax-ver-0-10-2-jax-ver-0-10-0-rocm-ver-7-14-1-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx1200-gfx-gfx1201-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-jax-ver-0-10-0-jax-ver-0-9-1-rocm-ver-7-14-0-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx1200-gfx-gfx1201-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-jax-ver-0-10-0-jax-ver-0-9-1-fam-radeon)

JAX BERT FP16 training workloads might encounter a segmentation fault on some AMD Radeon graphics products, such as the Radeon PRO W7900, causing training to terminate unexpectedly. As a workaround, disable XLA GPU command buffers by setting the following environment variable before launching the workload:

export XLA_FLAGS="--xla_gpu_enable_command_buffer="