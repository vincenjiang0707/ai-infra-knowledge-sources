source: https://docs.nvidia.com/switch-infrastructure/config-manager

NVIDIA Switch Infrastructure - Config Manager


NVIDIA Switch Infrastructure - Config Manager

NVIDIA Config Manager is a platform for bootstrapping and managing NVIDIA AI-factory network infrastructure. It brings data from a selected DCIM provider, template rendering, DHCP, ZTP, configuration storage, and workflow automation into one deployment. Nautobot is bundled as the default provider, while other providers integrate through the standalone DCIM SDK.

Read the [Start Here guide](https://docs.nvidia.com/switch-infrastructure/config-manager/getting-started/start-here) or learn fundamental concepts through the [Config Manager overview](https://docs.nvidia.com/switch-infrastructure/config-manager/config-manager/overview). Then use the [deployment guide](https://docs.nvidia.com/switch-infrastructure/config-manager/getting-started/getting-started-with-config-manager) and [user guides](https://docs.nvidia.com/switch-infrastructure/config-manager/user-guides/new-site-bringup) to install Config Manager, model network intent, render device configuration, run approved workflows, and troubleshoot day-0 and day-2 operations.

The project’s GitHub repository is [https://github.com/dsx-ai-factory/nv-config-manager](https://github.com/dsx-ai-factory/nv-config-manager).

## Start here

[Start Here](https://docs.nvidia.com/switch-infrastructure/config-manager/getting-started/start-here)explains the product, personas, and recommended first path.[Getting Started with Config Manager](https://docs.nvidia.com/switch-infrastructure/config-manager/getting-started/getting-started-with-config-manager)covers the standard connected install path.[Which Interface Should I Use?](https://docs.nvidia.com/switch-infrastructure/config-manager/getting-started/which-interface-should-i-use)explains the Config Manager UI, Nautobot UI, Temporal Web, and APIs.[Spectrum-X Switch Management](https://docs.nvidia.com/switch-infrastructure/config-manager/user-guides/spectrum-x-switch-management)summarizes day-0 and day-2 Spectrum-X support and links to the relevant workflows.[Airgapped Deployment](https://docs.nvidia.com/switch-infrastructure/config-manager/deployment/airgapped)covers disconnected environments.[DSX Air Simulation User Guide](https://docs.nvidia.com/switch-infrastructure/config-manager/getting-started/dsx-air-simulation-user-guide)covers workflow validation in NVIDIA DSX Air.[I want to…](https://docs.nvidia.com/switch-infrastructure/config-manager/i-want-to)routes common tasks to the right guide.[Contribute a DCIM Provider](https://docs.nvidia.com/switch-infrastructure/config-manager/config-manager/contribute-a-dcim-provider)describes the provider SDK and package contract.

The local development quick start is only for render and UI exploration. Use the DSX Air simulation guide when you need simulated Cumulus switches for device-facing workflow validation.