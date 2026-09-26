source: https://docs.nvidia.com/datacenter/tesla/mig-user-guide/virtualization.html

# Virtualization[#](https://docs.nvidia.com#virtualization)

MIG can be used with two types of virtualization:

Under Linux guests on supported hypervisors, when MIG-supported GPUs are in GPU pass-through, the same workflows

[workflows](https://docs.nvidia.com/getting-started-with-mig.html#getting-started-with-mig), tools, and[Supported MIG Profiles](https://docs.nvidia.com/supported-mig-profiles.html#supported-profiles)available on bare-metal can be used.MIG allows multiple vGPUs (and thereby VMs) to run in parallel on a single MIG-supported GPU, while preserving the isolation guarantees that vGPU provides. To configure a GPU for use with vGPU VMs, refer to the

[Configuring a GPU for MIG-Backed vGPUs](https://docs.nvidia.com/ai-enterprise/latest/user-guide/index.html#configuring-a-gpu-for-mig-backed-vgpus). Refer also to the[technical brief](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/solutions/resources/documents1/TB-10226-001_v01.pdf)for more information on GPU partitioning with vGPU.