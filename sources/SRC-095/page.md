source: https://github.com/ray-project/kuberay/releases

# Releases: ray-project/kuberay

## Release list

## v1.7.1

## Bug fixes

- Fixed a bug where the kubectl plugin did not re-check RayJob status after losing the port-forward connection, which could leave
`kubectl ray job submit`

hanging.[#5147](https://github.com/ray-project/kuberay/pull/5147) - Fixed a bug where the History Server could lose rotated Ray logs by collecting them only after they were overwritten.
[#5101](https://github.com/ray-project/kuberay/pull/5101) - Reduced History Server memory usage by caching the decoded snapshot struct in the session LRU instead of raw JSON bytes.
[#5208](https://github.com/ray-project/kuberay/pull/5208) - Fixed broken sample manifests.
[#5154](https://github.com/ray-project/kuberay/pull/5154) - Repinned the ML samples to a base Ray image with runtime-installed deps, since the
`rayproject/ray-ml:2.46.0.0e19ea-*`

tags were removed from Docker Hub and the samples failed with ImagePullBackOff.[#5194](https://github.com/ray-project/kuberay/pull/5194)

## Breaking Changes

- Disabled History Server live-cluster support by default to avoid unintended proxying to running clusters.
[#5199](https://github.com/ray-project/kuberay/pull/5199)

## Changelog

**Full Changelog**: `v1.7.0...v1.7.1`

## v1.7.0

## Highlights

### Ray History Server (beta)

The Ray History Server is graduating to **beta**. Introduced as alpha in KubeRay v1.6, the History Server lets you view the Ray Dashboard and debug ephemeral clusters (such as those managed by RayJob) even after they have been terminated.

Since v1.6, the History Server has received major improvements:

**Performance and scalability**: lazy loading, an LRU byte-based session cache, a disk-first event storage pipeline, and event compression significantly reduce memory usage for both the collector and the server.**Ray token authentication support**for both the collector and live-cluster proxying.**Better UI and API coverage**: a cluster selection page, task logs, and Serve / placement group / Ray Data endpoints polled by default.- History Server images are now published to
[quay.io/kuberay](https://quay.io/organization/kuberay)(`historyserver:v1.7.0`

and`collector:v1.7.0`

)

Try it here: [History Server Quick Start Guide](https://docs.ray.io/en/master/cluster/kubernetes/user-guides/kuberay-history-server.html).

### Automatic History Server Sidecar Configuration (alpha)

The operator can now automatically inject the History Server event collector sidecar into your RayCluster’s pods, no manual sidecar configuration needed. Enable the `RayClusterHistoryServer`

feature gate on the operator and set `spec.historyServerOptions`

on your RayCluster:

```
apiVersion: ray.io/v1
kind: RayCluster
metadata:
name: raycluster-historyserver
spec:
historyServerOptions:
collectorOptions:
image: quay.io/kuberay/collector:v1.7.0
```


See [ray-cluster.historyserver.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cluster.historyserver.yaml) for a full example.


⚠️ Warning:RayClusterHistoryServer is anAlphafeature and isdisabled by default. To enable it, set the feature gate on the kuberay-operator:`--feature-gates=RayClusterHistoryServer=true`


### RayService Incremental Upgrade graduates to Beta

The `RayServiceIncrementalUpgrade`

feature gate is now **beta and enabled by default**. This feature allows RayService to perform zero-downtime upgrades by gradually shifting traffic to the new cluster using the Kubernetes Gateway API, instead of requiring 2x resources for a blue/green switch.

Since its Alpha release, the feature has received several improvements for more reliable and robust upgrades, including:

**Rollback support:**Users can now revert the RayService spec mid-upgrade, with safe traffic shifting between the pending and active clusters.**Improved reliability:**Improved capacity management, traffic migration, failure handling, and cluster cleanup during incremental upgrades.**E2E test coverage:**Expanded test scenarios to improve coverage.

### mTLS support via cert-manager (alpha)

KubeRay v1.7 can automatically provision and rotate certificates for **mutual TLS between RayCluster’s pods** using cert-manager.


⚠️ Warning:RayClusterMTLS is anAlphafeature and isdisabled by default. To enable it, set the feature gate on the kuberay-operator:`--feature-gates=RayClusterMTLS=true`


Enable mTLS feature with following to try this feature:

```
apiVersion: ray.io/v1
kind: RayCluster
metadata:
name: raycluster-mtls
spec:
rayVersion: '2.55.1'
tlsOptions:
enabled: true
```


See [ray-cluster.mtls.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cluster.mtls.yaml) for a full example.

### NetworkPolicy support for RayCluster (alpha)

KubeRay v1.7 adds a new `spec.networkPolicy`

field to RayCluster for network isolation. When set, the operator creates separate NetworkPolicies for head and worker pods, with configurable modes (`DenyAll`

, `DenyAllIngress`

, `DenyAllEgress`

) and per-worker-group ingress/egress rules. Intra-cluster pod-to-pod traffic is always permitted.

Try it here: [Network Policy Quick Start Guide](https://docs.ray.io/en/master/cluster/kubernetes/user-guides/network-policy.html).


⚠️ Warning:RayClusterNetworkPolicy is anAlphafeature and isdisabled by default. To enable it, set the feature gate on the kuberay-operator:`--feature-gates=RayClusterNetworkPolicy=true`


Below is an example of enabling network policy feature:

```
apiVersion: ray.io/v1
kind: RayCluster
spec:
networkPolicy:
mode: DenyAll
head:
ingressRules:
- from:
- namespaceSelector:
matchLabels:
kubernetes.io/metadata.name: <prometheus-namespace>
ports:
- port: 8080
protocol: TCP
```


See [ray-cluster.network-policy-deny-all.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cluster.network-policy-deny-all.yaml) for an example.

### GCS fault tolerance with embedded storage (alpha)

GCS fault tolerance no longer requires an external Redis. With the `GCSFaultToleranceEmbeddedStorage`

feature gate enabled, you can persist GCS metadata in an embedded RocksDB store backed by a persistent volume on the head Pod:

```
spec:
gcsFaultToleranceOptions:
backend: rocksdb
storage:
size: 1Gi
```



⚠️ Warning:GCSFaultToleranceEmbeddedStorage is anAlphafeature and isdisabled by default. To enable it, set the feature gate on the kuberay-operator:`--feature-gates=GCSFaultToleranceEmbeddedStorage=true`


See [ray-cluster.embedded-gcs-ft.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cluster.embedded-gcs-ft.yaml) for a full example.

### Other Notable Features

- RayCluster now supports built-in Ingress configuration via
`headGroupSpec.ingressOptions`

with`host`

,`path`

,`pathType`

, and`tls`

fields. - RayCronJob now supports the
`spec.timeZone`

field, and child RayJobs use deterministic names to prevent duplicate firings. - The WorkerGroup API includes a new
`priority`

field for scheduler integrations. - A new alpha feature gate
`SidecarSubmitterRestart`

prevents premature job termination during transient head Pod resource spikes in RayJob sidecar mode. - The operator configuration supports
`defaultPodAnnotations`

and`defaultPodLabels`

applied to all Ray Pods. - Memory usage improvements in the operator: Pod informer cache selectors and more efficient pod resource calculation.
`kubectl ray logs`

support`--gke-link`

to print a Cloud Logging link on GKE.- Upgraded to Go 1.26; Grafana dashboards updated for Ray 2.56.

### Breaking Changes

**Helm**: in the kuberay-operator chart,`metrics.serviceMonitor.selector`

has been renamed to`metrics.serviceMonitor.additionalLabels`

, and empty labels are no longer emitted ([#4979](https://github.com/ray-project/kuberay/pull/4979)). Update your values file if you set this field.**History Server (alpha to beta)**: configuration has changed since the v1.6 alpha. S3 credentials now use the standard AWS environment variables (`AWS_ACCESS_KEY_ID`

,`AWS_SECRET_ACCESS_KEY`

, ...) instead of`AWS_S3ID`

/`AWS_S3SECRET`

/`AWS_S3TOKEN`

([#4665](https://github.com/ray-project/kuberay/pull/4665)), the runtime-class flag has been replaced by`--storage-backend`

([#5085](https://github.com/ray-project/kuberay/pull/5085)), and the on-storage event layout has changed ([#4670](https://github.com/ray-project/kuberay/pull/4670)). Redeploy the collector and history server together on v1.7 and see the updated[setup guide](https://docs.ray.io/en/master/cluster/kubernetes/user-guides/kuberay-history-server.html).

### Deprecations

- The
`ray.io/v1alpha1`

API version is now marked deprecated ([#5122](https://github.com/ray-project/kuberay/pull/5122)). Please migrate to`ray.io/v1`

.

## Changelog

- Disable RayMultiHostIndexing feature for TestReconcile_Multihost_Replicas by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4583](https://github.com/ray-project/kuberay/pull/4583) - Disable the field alignment lint check by
[@jinbum-kim](https://github.com/jinbum-kim)in[#4560](https://github.com/ray-project/kuberay/pull/4560) - Mark RC releases as pre-release in GoReleaser by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4590](https://github.com/ray-project/kuberay/pull/4590) - [RayCluster] Add example YAML for manually enabling Ray k8s auth by
[@andrewsykim](https://github.com/andrewsykim)in[#4582](https://github.com/ray-project/kuberay/pull/4582) - [RayService] Rollback Support for Incremental Upgrades by
[@ryanaoleary](https://github.com/ryanaoleary)in[#4109](https://github.com/ray-project/kuberay/pull/4109) - [RayService] Promote Incremental Upgrade Feature to Beta by
[@ryanaoleary](https://github.com/ryanaoleary)in[#4599](https://github.com/ray-project/kuberay/pull/4599) - Revert "[RayService] Promote Incremental Upgrade Feature to Beta" by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4602](https://github.com/ray-project/kuberay/pull/4602) - [Github Action] Skip krew-index update for pre-release tags by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4587](https://github.com/ray-project/kuberay/pull/4587) - [Helm] update ray-cluster chart to apiVersion: v2 by
[@mboersma](https://github.com/mboersma)in[#4593](https://github.com/ray-project/kuberay/pull/4593) - Update kind configs and docs to v1.29.0 by
[@mboersma](https://github.com/mboersma)in[#4595](https://github.com/ray-project/kuberay/pull/4595) - [Helm] remove ingress template support for k8s < 1.19 by
[@mboersma](https://github.com/mboersma)in[#4591](https://github.com/ray-project/kuberay/pull/4591) - [Helm] Update ray-cluster default resource values by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4588](https://github.com/ray-project/kuberay/pull/4588) - [Chore] Use RayCluster name as ServiceAccount name for RBAC authentication by
[@JiangJiaWei1103](https://github.com/JiangJiaWei1103)in[#4611](https://github.com/ray-project/kuberay/pull/4611) - [History Server] Add guide to push image to Google Artifact Registry for History Server images by
[@chiayi](https://github.com/chiayi)in[#4618](https://github.com/ray-project/kuberay/pull/4618) - [History Server] Fix API response format to match Ray Dashboard frontend schema by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4615](https://github.com/ray-project/kuberay/pull/4615) - [Test][Release] Change upgrade test version to test upgrade from 1.5.1 to 1.6.0 by
[@Future-Outlier](https://github.com/Future-Outlier)in[#4623](https://github.com/ray-project/kuberay/pull/4623) - [History Server] Typo and minor fix for image guide readme by
[@chiayi](https://github.com/chiayi)in[https://github.com/ray-proj](https://github.com/ray-proj)...

[Read more](https://github.com/ray-project/kuberay/releases/tag/v1.7.0)

## v1.7.0-rc.0

## Changelog

Fix rayClusterScaleExpectation deletion to use request object when instance is nil (`d59cbd8`[#4039](https://github.com/ray-project/kuberay/pull/4039))Inject the --block option to ray start command automatically (`480e128`[#932](https://github.com/ray-project/kuberay/pull/932))Make replicas configurable for kuberay-operator`0a9a3e3`[#4180](https://github.com/ray-project/kuberay/issues/4180)([#4195](https://github.com/ray-project/kuberay/pull/4195))Remove ray-cluster.without-block.yaml (`7850773`[#675](https://github.com/ray-project/kuberay/pull/675))[PodPool-VK] add podpool vk README (`162cafc`[#4250](https://github.com/ray-project/kuberay/issues/4250)) ([#4251](https://github.com/ray-project/kuberay/pull/4251))[Telemetry] Inject env identifying KubeRay.`38ac168`[#562](https://github.com/ray-project/kuberay/pull/562)AGC gateway api example (`97425fa`[#4076](https://github.com/ray-project/kuberay/pull/4076))Add DeepSeek example RayService (`dc203e2`[#3838](https://github.com/ray-project/kuberay/pull/3838))Add FAQ page (`7c0aa63`[#1150](https://github.com/ray-project/kuberay/pull/1150))Add Fake TPU e2e Autoscaling Test Cases (`8ae788b`[#2279](https://github.com/ray-project/kuberay/pull/2279))Add Google Artifact Registry image build/push guide (`fea763a`[#4618](https://github.com/ray-project/kuberay/pull/4618))Add Google Cloud storage history server deployment example (`506bea3`[#4641](https://github.com/ray-project/kuberay/pull/4641))Add Grafana Dashboard for KubeRay Operator (`dcb97ce`[#3676](https://github.com/ray-project/kuberay/pull/3676))Add Helm chart unit tests to ray-cluster (`bf7e497`[#3374](https://github.com/ray-project/kuberay/pull/3374))Add Helm chart unittests to CI (`113909f`[#3280](https://github.com/ray-project/kuberay/pull/3280))Add Helm values for ResourceClaims to RayCluster (`cb505dd`[#4290](https://github.com/ray-project/kuberay/pull/4290))Add KubeRay e2e Test for custom idleTimeoutSeconds with v2 Autoscaler (`d0e8b57`[#2725](https://github.com/ray-project/kuberay/pull/2725))Add KubeRay related blogs (`6818a08`[#1147](https://github.com/ray-project/kuberay/pull/1147))Add NumOfHosts to RayCluster helm-chart template (`042e6b4`[#1969](https://github.com/ray-project/kuberay/pull/1969))Add NumOfHosts to WorkerGroupSpec (CRD change only) (`5adc91a`[#1834](https://github.com/ray-project/kuberay/pull/1834))Add Pod informer cache selector to reduce memory usage (`6f4e680`[#4761](https://github.com/ray-project/kuberay/pull/4761))Add Ray cluster spec for TPU pods (`80a6d58`[#1292](https://github.com/ray-project/kuberay/pull/1292))Add RayCluster YAML for verl example (`abb5291`[#3833](https://github.com/ray-project/kuberay/pull/3833))Add RayCluster manifest example for history server (`3a3e634`[#4642](https://github.com/ray-project/kuberay/pull/4642))Add RayClusterProvisioned Condition Type (`f232b5b`[#2301](https://github.com/ray-project/kuberay/pull/2301))Add RayClusterReady Condition Type (`cbaf5d7`[#2271](https://github.com/ray-project/kuberay/pull/2271))Add RayJob sample for JAX TPU profiling (`745e176`[#5059](https://github.com/ray-project/kuberay/pull/5059))Add RayJob training example using pytorch resnet image classifier (`732453e`[#2107](https://github.com/ray-project/kuberay/pull/2107))Add RayService IncrementalUpgrade E2E tests to Buildkite (`e6ff35b`[#4497](https://github.com/ray-project/kuberay/pull/4497))Add RayService Manifests for Stable Diffusion TPU Examples (`a0afea2`[#2198](https://github.com/ray-project/kuberay/pull/2198))Add RayService finalizer (`f384932`[#4807](https://github.com/ray-project/kuberay/pull/4807))Add RayService incremental upgrade sample for guide (`044105c`[#4164](https://github.com/ray-project/kuberay/pull/4164))Add RayService sample test (`753dc05`[#1377](https://github.com/ray-project/kuberay/pull/1377))Add TPU to Known Custom Accelerators for generated rayStartCommand (`c835117`[#2495](https://github.com/ray-project/kuberay/pull/2495))Add`fe1ad90``NewClusterWithIncrementalUpgrade`

RayService rollback load tests ([#4915](https://github.com/ray-project/kuberay/pull/4915))Add`f05fa2e``ray.io/originated-from`

labels ([#1830](https://github.com/ray-project/kuberay/pull/1830))Add a document for profiling (`87407ac`[#1299](https://github.com/ray-project/kuberay/pull/1299))Add a document to outline the default settings for`08792ca``rayStartParams`

in Kuberay ([#1057](https://github.com/ray-project/kuberay/pull/1057))Add a flag to enable/disable worker init container injection (`b92d95a`[#1069](https://github.com/ray-project/kuberay/pull/1069))Add a grouping for 'google.golang.org/*' to avoid inconsistency between sub-projects (`8851088`[#3470](https://github.com/ray-project/kuberay/pull/3470))Add a sample RayJob to fine-tune a PyTorch lightning text classifier (`ceb9f01`[#1891](https://github.com/ray-project/kuberay/pull/1891))Add a test util function for killing the head Pod and wait (`a851490`[#3890](https://github.com/ray-project/kuberay/pull/3890))Add a util function to convert string and bytes array (`073de1f`[#2621](https://github.com/ray-project/kuberay/pull/2621))Add a variant of the ray data processing job with GCSFuse CSI driver (`3e20a9d`[#2401](https://github.com/ray-project/kuberay/pull/2401))Add a warning to discourage users from launching a KubeRay-incompatible autoscaler. (`7fe4050`[#1102](https://github.com/ray-project/kuberay/pull/1102))Add additional KubeRay autoscaler e2e tests (`efa2c1c`[#2761](https://github.com/ray-project/kuberay/pull/2761))Add all and worker node type to kubectl ray log (`8b61b73`[#2442](https://github.com/ray-project/kuberay/pull/2442))Add apply configurations to generated client (`966d9b3`[#1818](https://github.com/ray-project/kuberay/pull/1818))Add basic Helm chart unittests for kuberay-operator (`ef0129e`[#3253](https://github.com/ray-project/kuberay/pull/3253))Add basic e2e test for kubectl plugin (`cd239ab`[#2287](https://github.com/ray-project/kuberay/pull/2287))Add batch-scheduler option, deprecate enable-batch-scheduler option (`e1edb4c`[#2300](https://github.com/ray-project/kuberay/pull/2300))Add common containerEnv section to Helm Chart (`e330c03`[#1932](https://github.com/ray-project/kuberay/pull/1932))Add compression functions (`70194b7`[#4828](https://github.com/ray-project/kuberay/pull/4828))Add consistency check for deepcopy generated files (`70ef243`[#1127](https://github.com/ray-project/kuberay/pull/1127))Add dashboard component to master (`36267ed`[#3566](https://github.com/ray-project/kuberay/pull/3566))Add deletecollection for multi-namespace role (`cb2914d`[#2](https://github.com/ray-project/kuberay/pull/2)) ([#2231](https://github.com/ray-project/kuberay/pull/2231))Add dependabot.yml for enabling "Dependabot version updates" (`8bb3222`[#3357](https://github.com/ray-project/kuberay/pull/3357))Add dnsConfig to head, worker and additional workers (`9a0b9d0`[#2377](https://github.com/ray-project/kuberay/pull/2377))Add documentation for API Server monitoring (`80ce664`[#1479](https://github.com/ray-project/kuberay/pull/1479))Add documentations for the release process of Helm charts (`0bd28e7`[#723](https://github.com/ray-project/kuberay/pull/723))Add e2e KubeRay operator upgrade test (`7f3fe8b`[#3060](https://github.com/ray-project/kuberay/pull/3060))Add e2e test for kubectl ray job submit (`e9f3155`[#2614](https://github.com/ray-project/kuberay/pull/2614))Add e2e test make sure resource quota error is surfaced (`4fc48ce`[#3087](https://github.com/ray-project/kuberay/pull/3087))Add end to end tests to apiserver (`ff45923`[#1460](https://github.com/ray-project/kuberay/pull/1460))Add env and patch permission. (`4b0f7cb`[#740](https://github.com/ray-project/kuberay/pull/740))Add env variable comment to kuberay-operator`1bcfa9e`Add example YAML for manually enabling Ray k8s auth (`54a9488`[#4582](https://github.com/ray-project/kuberay/pull/4582))Add example and tutorial to explain how to create custom metrics for Prometheus (`d93c3c9`[#914](https://github.com/ray-project/kuberay/pull/914))Add example in GKE to enable Ray resource isolation using cgroupsv2 and writable cgroup containers (`9198189`[#4236](https://github.com/ray-project/kuberay/pull/4236))Add flag leader-election-namespace (`a34a42a`[#1624](https://github.com/ray-project/kuberay/pull/1624))Add gofumpt instructions from internal doc (`a2ebc61`[#1180](https://github.com/ray-project/kuberay/pull/1180))Add history server api for injecting collector sidecar (`1a544ab`[#4982](https://github.com/ray-project/kuberay/pull/4982))Add instruction to skip unit tests in DEVELOPMENT.md (`044008d`[#1171](https://github.com/ray-project/kuberay/pull/1171))Add kubectl plugin with basic command and deprecate cli (`abafd17`[#2243](https://github.com/ray-project/kuberay/pull/2243))Add kubectl ray cluster log command (`3e68606`[#2296](https://github.com/ray-project/kuberay/pull/2296))Add kubectl ray create cluster (`12babc8`[#2607](https://github.com/ray-project/kuberay/pull/2607))Add kubectl ray delete rayservice/job/cluster (`61a282f`[#2635](https://github.com/ray-project/kuberay/pull/2635))Add kubectl-plugin pre-commit (`8c64e60`[#2255](https://github.com/ray-project/kuberay/pull/2255))Add kuberay operator servicemonitor (`11c75ea`[#3717](https://github.com/ray-project/kuberay/pull/3717))Add kubernetes dependency in python client library (`25d5568`[#998](https://github.com/ray-project/kuberay/pull/998))Add kubernetes event to inform user of upgrade strategy (`c8f826b`[#2592](https://github.com/ray-project/kuberay/pull/2592))Add managedBy field to RayService (`ea46c77`[#4491](https://github.com/ray-project/kuberay/pull/4491))Add missing labels on RayCluster TPU manifests (`106f8fd`[#1987](https://github.com/ray-project/kuberay/pull/1987))Add more grouping to resolve inconsistencies when bumping versions (`4a12d78`[#3554](https://github.com/ray-project/kuberay/pull/3554))Add no-session defaulting route and test for enter_cluster (`20ed3b3`[#4907](https://github.com/ray-project/kuberay/pull/4907))Add quay release for history server (`81e45da`[#4980](https://github.com/ray-project/kuberay/pull/4980))Add rayVersion in the RayCluster chart (`7856027`[#975](https://github.com/ray-project/kuberay/pull/975))Add rayjob yaml generation to ray job submit command (`4021766`[#2644](https://github.com/ray-project/kuberay/pull/2644))Add release command and guidance for KubeRay cli (`d22d752`[#834](https://github.com/ray-project/kuberay/pull/834))Add reminders to avoid RBAC synchronization bug (`e9544fc`[#576](https://github.com/ray-project/kuberay/pull/576))Add seccompProfile to KubeRay operator deployment for PSS compliance (`08da595`[#3931](https://github.com/ray-project/kuberay/pull/3931))Add seccompProfile.type=RuntimeDefault to kuberay-operator. (`522807d`[#1955](https://github.com/ray-project/kuberay/pull/1955))Add structured config and default sidecar container configuration (`b5b4232`[#1822](https://github.com/ray-project/kuberay/pull/1822))Add support for Ray token auth (`58c2aad`[#4179](https://github.com/ray-project/kuberay/pull/4179))Add support for openshift routes (`224a444`[#1183](https://github.com/ray-project/kuberay/pull/1183))Add support for parsing neuron core resource limit and pass it as ray… (`43ed246`[#2409](https://github.com/ray-project/kuberay/pull/2409))Add support for pvcs to apiserver (`2de3fe5`[#1118](https://github.com/ray-project/kuberay/pull/1118))Add support for tolerations, env, annotations and labels (`3cc6116`[#1070](https://github.com/ray-project/kuberay/pull/1070))Add test for autoscaler and its desired state (`aeba37e`[#2601](https://github.com/ray-project/kuberay/pull/2601))Add test for configurable k8s job backoff...`76633c5`

[Read more](https://github.com/ray-project/kuberay/releases/tag/v1.7.0-rc.0)

## v1.6.2

## v1.6.1

## Bug fixes

- Fixed a bug where using
`spec.rayClusterSpec.suspend`

in RayService did not trigger suspend on the underlying RayCluster. This can break suspend behavior in some cases with Kueue when queueing or pre-empting RayService objects[#4739](https://github.com/ray-project/kuberay/pull/4739) - Fixed a bug where Volcano PodGroups can be deleted unconditionally.
[#4669](https://github.com/ray-project/kuberay/pull/4669)

## Changelog

## v1.5.2

## Bug fixes

- Fixed a bug where using
`spec.rayClusterSpec.suspend`

in RayService did not trigger suspend on the underlying RayCluster. This can break suspend behavior in some cases with Kueue when queueing or pre-empting RayService objects[#4739](https://github.com/ray-project/kuberay/pull/4739)

## Changelog

## v1.6.0

## Highlights

### Ray History Server (alpha)

KubeRay v1.6 introduces **alpha support** for the Ray History Server. This project enables users to collect and aggregate events from a Ray cluster, replaying them to restore historical snapshots of the cluster's state. By providing an alternative backend for the Ray Dashboard, the History Server allows users to view the Ray dashboard and debug ephemeral clusters (such as those managed via RayJob) even after they have been terminated.

**Try the history server here: History Server Quick Start Guide.**


⚠️ Warning:This feature is in alpha status, meaning future KubeRay releases may include breaking updates. We’d love to hear your experience with it! Please drop your feedback in[this tracking issue]to help us shape its development.

### Ray Token Authentication using Kubernetes RBAC

Starting in KubeRay v1.6 and Ray v2.55, you can use Kubernetes RBAC to manage user access control to Ray clusters that have [token authentication enabled](https://docs.ray.io/en/latest/ray-security/token-auth.html). With this feature enabled, Ray will be configured to delegate token authentication to Kubernetes. This means you can use the same credentials used with Kubernetes to access Ray clusters and platform operators can use standard Kubernetes RBAC to control access to Ray clusters. See [Configure Ray clusters to use Kubernetes RBAC authentication](https://docs.ray.io/en/master/cluster/kubernetes/user-guides/kuberay-auth-rbac.html) for a step-by-step guide.

You can now also reference Secrets containing static auth tokens for Ray cluster token authentication.

```
apiVersion: v1
kind: Secret
metadata:
name: ray-cluster-token
type: Opaque
stringData:
auth_token: "super-secret-example-token"
---
apiVersion: ray.io/v1
kind: RayCluster
metadata:
name: ray-cluster-with-auth
spec:
authOptions:
mode: token
secretName: ray-cluster-token
rayVersion: '2.53.0'
headGroupSpec:
rayStartParams: {}
```

### RayCronJob

KubeRay v1.6 introduces the `RayCronJob`

Custom Resource Definition (CRD), enabling users to schedule RayJobs on a recurring schedule using standard cron expressions. This is useful for periodic batch processing, scheduled training runs, or recurring data pipelines.

**Try the Ray CronJob API here: Ray CronJob Quick Start Guide.**


⚠️ Warning:RayCronJob is anAlphafeature and isdisabled by default. To enable it, set the feature gate on the kuberay-operator:`--feature-gates=RayCronJob=true`


Below is an example of the new custom resource:

```
apiVersion: ray.io/v1
kind: RayCronJob
metadata:
name: raycronjob-sample
spec:
schedule: "* * * * *"
jobTemplate:
entrypoint: python /home/ray/samples/sample_code.py
shutdownAfterJobFinishes: true
ttlSecondsAfterFinished: 600
runtimeEnvYAML: |
pip:
- requests==2.26.0
- pendulum==2.1.2
env_vars:
counter_name: "test_counter"
rayClusterSpec:
rayVersion: '2.52.0'
headGroupSpec:
...
...
```

See [ray-cronjob.sample.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cronjob.sample.yaml) for a full example.

### RayJob Deletion Policy API

The `RayJobDeletionPolicy`

feature gate is graduating to Beta and enabled by default. This feature enables a more advanced and flexible API for expressing deletion policies within the RayJob specification. This new design moves beyond the singular boolean field, `spec.shutdownAfterJobFinishes`

, and allows users to define different cleanup strategies using configurable TTL values based on the Ray job's status.

Below is an example of how to use this new, flexible API structure:

```
apiVersion: ray.io/v1
kind: RayJob
metadata:
name: rayjob-deletion-rules
spec:
deletionStrategy:
deletionRules:
- policy: DeleteWorkers
condition:
jobStatus: FAILED
ttlSeconds: 100
- policy: DeleteCluster
condition:
jobStatus: FAILED
ttlSeconds: 600
```

See [ray-job.deletion-rules.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-job.deletion-rules.yaml) for a comprehensive example.

### Other Notable Features

- RayJob now supports spec.preRunningDeadlineSeconds to automatically mark failed jobs if they do not reach Running state within a specified timeout.
- RayService now supports spec.managedBy for improved support with Multi-Kueue
- The
`RayMultihostIndexing`

feature gate is graduating to Beta and enabled by default. This feature provides ordered replica and host index labels that are useful for managing Ray clusters for multi-host TPU/GPU workloads that require atomic scheduling and scaling. These labels are only applied if numOfHosts > 1 in worker group configuration. - KubeRay v1.6 adds a new
`spec.upgradeStrategy`

field to RayCluster. Supported values are`Recreate`

and`None`

. The`Recreate`

strategy is useful for automatically recreating all Ray cluster Pods when the Ray cluster spec changes. This upgrade strategy is not recommended if Ray cluster state needs to be persisted. - RayService incremental upgrade feature (alpha status) now supports rollback.

## Breaking Changes

When using Sidecar submission mode with RayJob, the Head Pod will no longer be automatically recreated after initial provisioning. This is because the submission container runs along the Head container and recreating the Pod would result in restarting the job entirely. See [#4141](https://github.com/ray-project/kuberay/pull/4141) for more details.

## CHANGELOG

- Add support for Ray token auth (
[#4179](https://github.com/ray-project/kuberay/pull/4179),[@andrewsykim](https://github.com/andrewsykim)) - feat: upgrade to Ray 2.52.0 to support token auth mode (
[#4152](https://github.com/ray-project/kuberay/pull/4152),[@Future-Outlier](https://github.com/Future-Outlier)) - update minimum Ray version required for token authentication to 2.52.0 (
[#4201](https://github.com/ray-project/kuberay/pull/4201),[@andrewsykim](https://github.com/andrewsykim)) - add samples for RayCluster token auth (
[#4200](https://github.com/ray-project/kuberay/pull/4200),[@andrewsykim](https://github.com/andrewsykim)) - [RayCluster] Enable Secret informer watch/list and remove unused RBAC verbs (
[#4202](https://github.com/ray-project/kuberay/pull/4202),[@Future-Outlier](https://github.com/Future-Outlier)) - [RayJob] Add token authentication support for All mode (
[#4210](https://github.com/ray-project/kuberay/pull/4210),[@Future-Outlier](https://github.com/Future-Outlier)) - Support X-Ray-Authorization fallback header for accepting auth token via proxy (
[#4213](https://github.com/ray-project/kuberay/pull/4213),[@Future-Outlier](https://github.com/Future-Outlier)) - [RayJob] Add token authentication support for light weight job submitter (
[#4215](https://github.com/ray-project/kuberay/pull/4215),[@Future-Outlier](https://github.com/Future-Outlier)) - [RayCluster] make auth token secret name consistency (
[#4216](https://github.com/ray-project/kuberay/pull/4216),[@fscnick](https://github.com/fscnick)) - feat: kubectl ray get token command (
[#4218](https://github.com/ray-project/kuberay/pull/4218),[@rueian](https://github.com/rueian)) - [RayService] auth token mode e2e test (
[#4225](https://github.com/ray-project/kuberay/pull/4225),[@ryankert01](https://github.com/ryankert01)) - [e2e] RayJob Auth Mode E2E (
[#4229](https://github.com/ray-project/kuberay/pull/4229),[@seanlaii](https://github.com/seanlaii)) - [e2e] Enhance RayCluster Auth E2E (
[#4231](https://github.com/ray-project/kuberay/pull/4231),[@seanlaii](https://github.com/seanlaii)) - [RayJob] light weight job submitter upgrade to 1.5.1 to support auth token mode (
[#4235](https://github.com/ray-project/kuberay/pull/4235),[@Future-Outlier](https://github.com/Future-Outlier)) - Support enabling RAY_ENABLE_K8S_TOKEN_AUTH (
[#4509](https://github.com/ray-project/kuberay/pull/4509),[@andrewsykim](https://github.com/andrewsykim)) - [Enhance] Refactor IsK8sAuthEnabled to accept AuthOptions and add token audience TODO (
[#4543](https://github.com/ray-project/kuberay/pull/4543),[@Future-Outlier](https://github.com/Future-Outlier)) - [Enhancement] Add sample YAML for K8s token auth RayCluster (
[#4544](https://github.com/ray-project/kuberay/pull/4544),[@Future-Outlier](https://github.com/Future-Outlier)) - improve API docs for EnableK8sTokenAuth (
[#4553](https://github.com/ray-project/kuberay/pull/4553),[@andrewsykim](https://github.com/andrewsykim)) - [ray-operator] add support for referencing Secret names for auth tokens (
[#4554](https://github.com/ray-project/kuberay/pull/4554),[@andrewsykim](https://github.com/andrewsykim)) - [Fix] Skip auth Secret reconciliation when K8s token auth is enabled (
[#4556](https://github.com/ray-project/kuberay/pull/4556),[@Future-Outlier](https://github.com/Future-Outlier)) - [ray-operator][validation] K8s token auth mode does not support RayJob and RayService (
[#4562](https://github.com/ray-project/kuberay/pull/4562),[@Future-Outlier](https://github.com/Future-Outlier)) - fix: upgrade Ray image in ray-cluster.auth.yaml to 2.53.0 to resolve dashboard 'Failed to load' error (
[#4310](https://github.com/ray-project/kuberay/pull/4310),[@win5923](https://github.com/win5923)) - introduce historyserver directory and project structure (
[#4232](https://github.com/ray-project/kuberay/pull/4232),[@andrewsykim](https://github.com/andrewsykim)) - add the implementation of historyserver collector (
[#4241](https://github.com/ray-project/kuberay/pull/4241),[@KunWuLuan](https://github.com/KunWuLuan)) - [history server] Remove go.work and go.work.sum to follow Go's best practices (
[#4301](https://github.com/ray-project/kuberay/pull/4301),[@Future-Outlier](https://github.com/Future-Outlier)) - [history server] move storage interface (
[#4302](https://github.com/ray-project/kuberay/pull/4302),[@my-vegetable-has-exploded](https://github.com/my-vegetable-has-exploded)) - [historyserver][collector] Remove unused function processAllLogs (
[#4316](https://github.com/ray-project/kuberay/pull/4316),[@ryankert01](https://github.com/ryankert01)) - [historyserver][collector] Add file-level idempotency check for prev-logs processing on container restart (
[#4321](https://github.com/ray-project/kuberay/pull/4321),[@my-vegetable-has-exploded](https://github.com/my-vegetable-has-exploded)) - [history server] Web Server + Event Processor (
[#4329](https://github.com/ray-project/kuberay/pull/4329),[@Future-Outlier](https://github.com/Future-Outlier)) - [historyserver] Ensure at least one worker in sample RayCluster (
[#4330](https://github.com/ray-project/kuberay/pull/4330),[@Future-Outlier](https://github.com/Future-Outlier)) - historyserver: remove unused function in RayLogHandler (
[#4336](https://github.com/ray-project/kuberay/pull/4336),[@AndySung320](https://github.com/AndySung320)) - [history server][collector] Fix getJobID for job event collection (
[#4342](https://github.com/ray-project/kuberay/pull/4342),[@Future-Outlier](https://github.com/Future-Outlier)) - [KubeRay Dashboard][Feature] Integrate History Server into KubeRay Dashboard (
[#4395](https://github.com/ray-project/kuberay/pull/4395),[@CheyuWu](https://github.com/CheyuWu)) - [Feat] [history server] Enable running the history server outside the K8s cluster (
[#4404](https://github.com/ray-project/kuberay/pull/4404),[@JiangJiaWei1103](https://github.com/JiangJiaWei1103)) - [history server][collector] Add WaitGroup for graceful shutdown (
[#4409](https://github.com/ray-project/kuberay/pull/4409),[@fweilun](https://github.com/fweilun)) - [1/N][Feature][history server] support endpoint /api/v0/logs/file (
[#4411](https://github.com/ray-project/kuberay/pull/4411),[@machichima](https://github.com/machichima)) - [history server][storage] Add Azure Blob Storage support (
[#4413](https://github.com/ray-project/kuberay/pull/4413),[@ikchifo](https://github.com/ikchifo)) - [historyserver][collector] use filepath functions to handle file path (
[#4417](https://github.com/ray-project/kuberay/pull/4417),[@400Ping](https://github.com/400Ping)) - [Feature][history server] support endpoint /api/cluster_status (
[#4421](https://github.com/ray-project/kuberay/pull/4421),[@justinyeh1995](https://github.com/justinyeh1995)) - [1/N] [history server] Support job event processing and endpoint (
[#4422](https://github.com/ray-project/kuberay/pull/4422),[@chiayi](https://github.com/chiayi)) - [historyserver] implement grafana health for live session (
[#4425](https://github.com/ray-project/kuberay/pull/4425),[@fscnick](https://github.com/fscnick)) - [history server][collector] Enable run with race condition checker (
[#4430](https://github.com/ray-project/kuberay/pull/4430),[@machichima](https://github.com/machichima)) - [Feat] [history server] Add node endpoint (
[#4436](https://github.com/ray-project/kuberay/pull/4436),[@JiangJiaWei1103](https://github.com/JiangJiaWei1103)) - [Feature][history server] support endpoint /api/v0/tasks/timeline (
[#4437](https://github.com/ray-project/kuberay/pull/4437),[@AndySung320](https://github.com/AndySung320)) - [history server] Add logs/file resolution and logs/stream endpoint (
[#4456](https://github.com/ray-project/kuberay/pull/4456), ...

[Read more](https://github.com/ray-project/kuberay/releases/tag/v1.6.0)

## v1.6.0-rc.0

[Release] Update KubeRay version references for 1.6.0 (#4586) * [Release] Update KubeRay version references for 1.6.0 Signed-off-by: Future-Outlier <eric901201@gmail.com> * update Signed-off-by: Future-Outlier <eric901201@gmail.com> * update Signed-off-by: Future-Outlier <eric901201@gmail.com> * update Signed-off-by: Future-Outlier <eric901201@gmail.com> --------- Signed-off-by: Future-Outlier <eric901201@gmail.com>

## v1.5.1

# v1.5.1

## Highlights

This release adds support for Ray token authentication using RayCluster, RayJob and RayService.

You can enable Ray token authentication using the following API:

```
apiVersion: ray.io/v1
kind: RayCluster
metadata:
name: ray-cluster-with-auth
spec:
rayVersion: '2.52.0'
authOptions:
mode: token
```


You must specify `spec.rayVersion`

to `2.52.0`

or newer. See full example at [ray-cluster.auth.yaml](https://github.com/ray-project/kuberay/blob/master/ray-operator/config/samples/ray-cluster.auth.yaml).

## Bug fixes

- Fix a bug in the NewClusterWithIncrementalUpgrade strategy where the Active (old) cluster's Serve configuration cache was incorrectly updated to the new ServeConfigV2 during an upgrade.
[#4212](https://github.com/ray-project/kuberay/pull/4212)[@ryanaoleary](https://github.com/ryanaoleary) - Surface pod-level container failures to RayCluster status
[#4196](https://github.com/ray-project/kuberay/pull/4196)[@spencer-p](https://github.com/spencer-p) - Fix a bug where RayJob status is not updated if failure happens in Initializing phase
[#4191](https://github.com/ray-project/kuberay/pull/4191)[@spencer-p](https://github.com/spencer-p) - Fix a bug where RayCluster status was not always propagated to RayJob status
[#4192](https://github.com/ray-project/kuberay/pull/4192)[@machichima](https://github.com/machichima)

## v1.5.0

# Highlights

## Ray Label Selector API

Ray v2.49 introduced a [label selector API](https://docs.ray.io/en/latest/ray-core/scheduling/labels.html). Correspondingly, KubeRay v1.5 now features a top-level API for defining Ray labels and resources. This new top-level API is the preferred method going forward, replacing the previous practice of setting labels and custom resources within rayStartParams.

The new API will be consumed by the Ray autoscaler, improving autoscaling decisions based on task and actor label selectors. Furthermore, labels configured through this API are mirrored directly into the Pods. This mirroring allows users to more seamlessly combine Ray label selectors with standard Kubernetes label selectors when managing and interacting with their Ray clusters.

You can use the new API in the following way:

```
apiVersion: ray.io/v1
kind: RayCluster
spec:
...
headGroupSpec:
rayStartParams: {}
resources:
Custom1: "1"
labels:
ray.io/zone: us-west-2a
ray.io/region: us-west-2
workerGroupSpec:
- replicas: 1
rayStartParams: {}
resources:
Custom1: "1"
labels:
ray.io/zone: us-west-2a
ray.io/region: us-west-2
```

## RayJob Sidecar submission mode

The RayJob resource now supports a new value for `spec.submissionMode`

called `SidecarMode`

.

Sidecar mode directly addresses a key limitation in both `K8sJobMode`

and `HttpMode`

: the network connectivity requirement from an external Pod or the KubeRay operator for job submission. With Sidecar mode, job submission is orchestrated by injecting a sidecar container into the Head Pod. This solution eliminates the need for an external client to handle the submission process and reduces job submission failure due to network failures.

To use this feature, set spec.submissionMode to SidecarMode in your RayJob:

```
apiVersion: ray.io/v1
kind: RayJob
metadata:
name: my-rayjob
spec:
submissionMode: "SidecarMode"
...
```

## Advanced deletion policies for RayJob

KubeRay now supports a more advanced and flexible API for expressing deletion policies within the RayJob specification. This new design moves beyond the singular boolean field, spec.shutdownAfterJobFinishes, and allows users to define different cleanup strategies using configurable TTL values based on the Ray job's status.

This API unlocks new use cases that require specific resource retention after a job completes or fails. For example, users can now implement policies that:

- Preserve only the Head Pod for a set duration after job failure to facilitate debugging.
- Retain the entire Ray Cluster for a longer TTL after a successful run for post-analysis or data retrieval.

By linking specific TTLs to Ray job statuses (e.g., success, failure) and strategies (e.g. DeleteWorkers, DeleteCluster, DeleteSelf), users gain fine-grained control over resource cleanup and cost management.

Below is an example of how to use this new, flexible API structure:

```
apiVersion: ray.io/v1
kind: RayJob
metadata:
name: rayjob-deletion-rules
spec:
deletionStrategy:
deletionRules:
- policy: DeleteWorkers
condition:
jobStatus: FAILED
ttlSeconds: 100
- policy: DeleteCluster
condition:
jobStatus: FAILED
ttlSeconds: 600
- policy: DeleteCluster
condition:
jobStatus: SUCCEEDED
ttlSeconds: 0
```

This feature is disabled by default and requires enabling the `RayJobDeletionPolicy`

feature gate.

## Incremental upgrade support for RayService

KubeRay v1.5 introduces the capability to enable zero-downtime incremental upgrades for RayServices. This new feature improves the upgrade process by leveraging the Gateway API and Ray autoscaling to incrementally migrate user traffic from the existing Ray cluster to the newly upgraded one.

This approach is more efficient and reliable compared to the former mechanism. The previous method required creating the upgraded Ray cluster at its full capacity and then shifting all traffic at once, which could lead to disruptions and unnecessary resource usage. By contrast, the incremental approach gradually scales up the new cluster and migrates traffic in smaller, controlled steps, resulting in improved stability and resource utilization during upgrade.

To enable this feature, set the following fields in RayService:

```
apiVersion: ray.io/v1
kind: RayService
metadata:
name: example-rayservice
spec:
upgradeStrategy:
type: "NewClusterWithIncrementalUpgrade"
clusterUpgradeOptions:
maxSurgePercent: 40
stepSizePercent: 5
intervalSeconds: 10
gatewayClassName: "cluster-gateway"
```

This feature is disabled by default and requires enabling the `RayServiceIncrementalUpgrade`

feature gate.

## Improved multi-host support for RayCluster

Previous KubeRay versions supported multi-host worker groups via the numOfHosts API, but this capability lacked fundamental capabilities required for managing multi-host accelerators. Firstly, it lacked logical grouping of worker Pods belonging to the same multi-host unit (or slice). As a result, it was not possible to run operations like “replace all workers in this group”. In addition, there was no ordered indexing, which is often required for coordinating multi-host workers when using TPUs.

When using multi-host in KubeRay v1.5, KubeRay will automatically set the following labels for multi-host Ray workers:

```
labels:
ray.io/worker-group-replica-name: tpu-group-af03de
ray.io/worker-group-replica-index: 0
ray.io/replica-host-index: 1
```

Below is a description of each label and its purpose:

`ray.io/worker-group-replica-name`

: this label provides a unique identifier for each replica (i.e. host group or slice) in a worker group. The label enables KubeRay to rediscover all other pods in the same group and apply group operators.`ray.io/worker-group-replica-index`

: this label is an ordered replica index in the worker group. This label is particularly important for cases like multi-slice TPUs, where each slice must be aware of its slice index.`ray.io/replica-host-index`

: this label is an ordered host index per replica (host group or slice).

These changes collectively enable reliable, production-level scaling and management of multi-host GPU workers or TPU slices.

This feature is disabled by default and requires enabling the `RayMultiHostIndexing`

feature gate.

# Breaking Changes

For RayCluster objects created by a RayJob, KubeRay will no longer attempt to recreate the Head Pod if it fails or is deleted after its initial successful provisioning. To retry failed jobs, use spec.backoffLimit which will result in KubeRay provisioning a new RayCluster.

# CHANGELOG

- [release-1.5] update version to v1.5.0 (
[#4177](https://github.com/ray-project/kuberay/pull/4177),[@andrewsykim](https://github.com/andrewsykim)) - [CherryPick][Feature Enhancement] Set ordered replica index label to support mult… (
[#4171](https://github.com/ray-project/kuberay/pull/4171),[@ryanaoleary](https://github.com/ryanaoleary)) - [releasey-1.5] update version to v1.5.0-rc.1 (
[#4170](https://github.com/ray-project/kuberay/pull/4170),[@andrewsykim](https://github.com/andrewsykim)) - [release-1.5] fix: dashboard build for kuberay 1.5.0 (
[#4169](https://github.com/ray-project/kuberay/pull/4169),[@andrewsykim](https://github.com/andrewsykim)) - [release-1.5] update versions to v1.5.0-rc.0 (
[#4155](https://github.com/ray-project/kuberay/pull/4155),[@andrewsykim](https://github.com/andrewsykim)) - [Bug] Sidecar mode shouldn't restart head pod when head pod is delete… (
[#4156](https://github.com/ray-project/kuberay/pull/4156),[@rueian](https://github.com/rueian)) - Bump Kubernetes dependencies to v0.34.x (
[#4147](https://github.com/ray-project/kuberay/pull/4147),[@mbobrovskyi](https://github.com/mbobrovskyi)) - [Chore] Remove duplicate
`test-e2e-rayservice`

in Makefile ([#4145](https://github.com/ray-project/kuberay/pull/4145),[@seanlaii](https://github.com/seanlaii)) - [Scheduler] Replace AddMetadataToPod with AddMetadataToChildResource across all schedulers (
[#4123](https://github.com/ray-project/kuberay/pull/4123),[@win5923](https://github.com/win5923)) - [Feature] Add initializing timeout for RayService (
[#4143](https://github.com/ray-project/kuberay/pull/4143),[@seanlaii](https://github.com/seanlaii)) - [RayService] Support Incremental Zero-Downtime Upgrades (
[#3166](https://github.com/ray-project/kuberay/pull/3166),[@ryanaoleary](https://github.com/ryanaoleary)) - Example RayCluster spec with
`Labels`

and`label_selector`

API ([#4136](https://github.com/ray-project/kuberay/pull/4136),[@ryanaoleary](https://github.com/ryanaoleary)) - [RayCluster] Fix for multi-host indexing worker creation (
[#4139](https://github.com/ray-project/kuberay/pull/4139),[@chiayi](https://github.com/chiayi)) - Support uppercase default resource names for top-level Resources (
[#4137](https://github.com/ray-project/kuberay/pull/4137),[@ryanaoleary](https://github.com/ryanaoleary)) - [Bug] [KubeRay Dashboard] Misclassifies RayCluster type (
[#4135](https://github.com/ray-project/kuberay/pull/4135),[@CheyuWu](https://github.com/CheyuWu)) - [RayCluster] Add multi-host indexing labels (
[#3998](https://github.com/ray-project/kuberay/pull/3998),[@chiayi](https://github.com/chiayi)) - [Grafana] Use Range option instead of instant for RayCluster Provisioned Duration panel (
[#4062](https://github.com/ray-project/kuberay/pull/4062),[@win5923](https://github.com/win5923)) - [Feature] Separate controller namespace and CRD namespaces for KubeRay-Operator Dashboard (
[#4088](https://github.com/ray-project/kuberay/pull/4088),[@400Ping](https://github.com/400Ping)) - Update grafana dashboards to ray 2.49.2 + add README instructions on how to update (
[#4111](https://github.com/ray-project/kuberay/pull/4111),[@alanwguo](https://github.com/alanwguo)) - fix: update broken and outdated links (
[#4129](https://github.com/ray-project/kuberay/pull/4129),[@ErikJiang](https://github.com/ErikJiang)) - [Feature] Provide multi-arch images for apiserver and security proxy (
[#4131](https://github.com/ray-project/kuberay/pull/4131),[@seanlaii](https://github.com/seanlaii)) - test: add LastTransition to fix test (
[#4132](https://github.com/ray-project/kuberay/pull/4132),[@machichima](https://github.com/machichima)) - Add top-level Labels and Resources Structed fields to
`HeadGroupSpec`

and`WorkerGroupSpec`

([[#4106](https://github.com/ray-project/kuberay/pull/4106)]([#4](https://github.com/ray-project/kuberay/pull/4)...

[Read more](https://github.com/ray-project/kuberay/releases/tag/v1.5.0)