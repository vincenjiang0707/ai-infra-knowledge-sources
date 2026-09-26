source: https://docs.nvidia.com/dynamo/dev/reference/enterprise/overview
lastmod: 2026-09-24T19:58:16.636Z

# Overview

Dynamo Enterprise Support identifies a curated set of Dynamo release artifacts that are eligible for enterprise support. It is a publishing and support designation, not a separate Dynamo fork, feature tier, or runtime implementation.

Only the exact artifacts and versions listed in [Supported Artifacts](https://docs.nvidia.com/dynamo/dev/reference/enterprise/supported-artifacts) are included in the Dynamo Enterprise Support scope. Every other Dynamo artifact, including the additional tags published in the corresponding open-source repositories, is out of scope for commercial support.

## Scope

Dynamo Enterprise Support covers a defined set of container images and the platform Helm chart that installs the Dynamo Operator for a Kubernetes deployment. It does not add features and it does not replace the open-source Dynamo distribution.

## Access and Support

Dynamo Enterprise Support artifacts are published on NGC as public images. Downloading and running them does not require an [NVIDIA AI Enterprise](https://docs.nvidia.com/ai-enterprise/) (NVAIE) subscription. An active NVAIE subscription is required to open commercial support cases against those artifacts.

## Relationship to Open-Source Artifacts

For the same release version, a Dynamo Enterprise Support artifact contains the same release binaries as its corresponding open-source artifact. The `-enterprise`

suffix identifies the curated publication channel and the commercial support boundary; it does not identify a separately compiled or forked build.

The open-source repositories can carry additional container tags for special-purpose builds, such as dated snapshots and nightly builds. Only the tags designated for commercial support are in the enterprise support scope.

Binary equivalence does not extend commercial support to an unlisted artifact, tag, component, or configuration. When commercial support is required, pull the exact `-enterprise`

artifact and version listed for the applicable release.

## Security Vulnerabilities in Open-Source Packages

Please review the Security Scanning tab on each supported container page for the latest security scan results: [vllm-runtime-enterprise](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/vllm-runtime-enterprise/security), [sglang-runtime-enterprise](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/sglang-runtime-enterprise/security), [tensorrtllm-runtime-enterprise](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/tensorrtllm-runtime-enterprise/security), [kubernetes-operator-enterprise](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/kubernetes-operator-enterprise/security), and [dynamo-frontend-enterprise](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/ai-dynamo/containers/dynamo-frontend-enterprise/security).

For certain open-source vulnerabilities listed in the scan results, NVIDIA provides a response in the form of a Vulnerability Exploitability eXchange (VEX) document. The VEX information can be reviewed and downloaded from the same Security Scanning tab.

## Get Help

**Commercial support cases.**Open cases through the[NVIDIA Enterprise Support portal](https://enterprise-support.nvidia.com/s/create-case)with an active NVAIE subscription. Route Dynamo Enterprise Support cases against the Dynamo product designation so they reach the Dynamo support pool.**Subscription and account questions.**For NVAIE subscription management, portal access, and account-level questions, see the[NVIDIA AI Enterprise documentation](https://docs.nvidia.com/ai-enterprise/).**Community and open-source discussion.**For questions and discussion that fall outside the commercial support scope, use the[ai-dynamo GitHub repository](https://github.com/ai-dynamo/dynamo)and the channels on the[Community](https://docs.nvidia.com/dynamo/dev/community)page.