source: https://docs.nvidia.com/openshell/index.html

# Overview of NVIDIA OpenShell

NVIDIA OpenShell is an open-source runtime for executing autonomous AI agents in sandboxed environments with kernel-level isolation. It combines sandbox runtime controls and a declarative YAML policy so teams can run agents without giving them unrestricted access to local files, credentials, and external networks.

## Why OpenShell Exists

AI agents are most useful when they can read files, install packages, call APIs, and use credentials. That same access can create material risk. OpenShell is designed for this tradeoff: preserve agent capability while enforcing explicit controls over what the agent can access.

## Common Risks and Controls

The table below summarizes common failure modes and how OpenShell mitigates them.

## Protection Layers at a Glance

OpenShell applies defense in depth across the following policy domains.

For details, refer to [Customize Sandbox Policies](https://docs.nvidia.com/openshell/sandboxes/policies) and [Default Policy](https://docs.nvidia.com/openshell/reference/default-policy).

## Common Use Cases

OpenShell supports a range of agent deployment patterns.

## Next Steps

Explore these topics to go deeper:

- To understand the runtime architecture, refer to
[How OpenShell Works](https://docs.nvidia.com/openshell/about/how-it-works). - To install the CLI and create your first sandbox, refer to the
[Quickstart](https://docs.nvidia.com/openshell/get-started/quickstart). - To learn how OpenShell enforces policy controls across protection layers, refer to
[Customize Sandbox Policies](https://docs.nvidia.com/openshell/sandboxes/policies).