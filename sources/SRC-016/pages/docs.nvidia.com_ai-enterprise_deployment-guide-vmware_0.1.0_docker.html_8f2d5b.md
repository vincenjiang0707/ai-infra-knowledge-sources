source: https://docs.nvidia.com/ai-enterprise/deployment-guide-vmware/0.1.0/docker.html

# Installing Docker and The Docker Utility Engine for NVIDIA GPUs[#](https://docs.nvidia.com#installing-docker-and-the-docker-utility-engine-for-nvidia-gpus)

The NVIDIA Container Toolkit allows users to build and run GPU accelerated Docker containers. The toolkit includes a container runtime [library](https://github.com/NVIDIA/libnvidia-container) and utilities to configure containers to leverage NVIDIA GPUs automatically. Complete documentation and frequently asked questions are available on the [repository wiki](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/overview.html).

## Installing Docker[#](https://docs.nvidia.com#installing-docker)

Please refer to [Install Docker Engine on Ubuntu | Docker Documentation](https://docs.docker.com/engine/install/ubuntu/) for a current installation procedure for Ubuntu.

## Installing the NVIDIA Container Toolkit[#](https://docs.nvidia.com#installing-the-nvidia-container-toolkit)

Please refer to [Installing the NVIDIA Container Toolkit | NVIDIA Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-the-nvidia-container-toolkit) for a current installation procedure to enable the docker repository and install the NVIDIA Container Toolkit.

Once the NVIDIA Container Toolkit is installed, to configure the docker container runtime, please refer to [Configuration | NVIDIA Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#configuration).

## Testing Docker and NVIDIA Container Runtime[#](https://docs.nvidia.com#testing-docker-and-nvidia-container-runtime)

Please refer to [Running a Sample Workload | NVIDIA Documentation](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/sample-workload.html#running-a-sample-workload) to run a sample CUDA container test on your GPU.