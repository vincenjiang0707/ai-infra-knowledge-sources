# Changelog (aggregated from releases.body)

> releases: 20

## v0.1.0-rc.1 (2024-09-10)

## What's Changed
* Add common project documents and skeleton folders by @Jeffwan in https://github.com/aibrix/aibrix/pull/4
* Scaffolding aibrix project using kubebuilder by @Jeffwan in https://github.com/aibrix/aibrix/pull/17
* Optimize project layouts by moving controllers to pkg folder by @Jeffwan in https://github.com/aibrix/aibrix/pull/21
* Create Lora api and controller by @Jeffwan in https://github.com/aibrix/aibrix/pull/23
* Rename LoraAdapter to ModelAdapter by @Jeffwan in https://github.com/aibrix/aibrix/pull/25
* Add ModelAdapter API by @Jeffwan in https://github.com/aibrix/aibrix/pull/26
* Use better way to set up controller with Manager by @Jeffwan in https://github.com/aibrix/aibrix/pull/27
* Initial model adapter controller implementation by @Jeffwan in https://github.com/aibrix/aibrix/pull/32
* Add mocked model container for lora adapter fast prototyping by @Jeffwan in https://github.com/aibrix/aibrix/pull/33
* [Misc] Add the PR and issues template by @jsw-zorro in https://github.com/aibrix/aibrix/pull/38
* [Docs] Add example to run vLLM distributed inference using Ray by @Jeffwan in https://github.com/aibrix/aibrix/pull/39
* [Doc] Improve the model adapter mock service by @Jeffwan in https://github.com/aibrix/aibrix/pull/45
* [Misc] Simplify the feature/bug/enhancement template. by @jsw-zorro in https://github.com/aibrix/aibrix/pull/48
* [Misc] Make model adapter controller e2e work by @Jeffwan in https://github.com/aibrix/aibrix/pull/50
* [Docs] A draft version of the contributing guideline document by @kr11 in https://github.com/aibrix/aibrix/pull/47
* [Core] Improve model adapter controller by handling existing resources by @Jeffwan in https://github.com/aibrix/aibrix/pull/54
* [Feat] Initial Implementation of PodAutoscaler Reconciler by @kr11 in https://github.com/aibrix/aibrix/pull/55
* [Docs] Move the sample mocked application to common folder by @Jeffwan in https://github.com/aibrix/aibrix/pull/64
* [Misc] Minor refactor the PodAutoscaler codes by @Jeffwan in https://github.com/aibrix/aibrix/pull/68
* [Core] Add model router controller by @varungup90 in https://github.com/aibrix/aibrix/pull/57
* Add rbac rules in model router by @varungup90 in https://github.com/aibrix/aibrix/pull/71
* [bugs] Add autoscaler RBAC to successfully list horizontalpodautoscalers by @kr11 in https://github.com/aibrix/aibrix/pull/72
* [Misc] Update license info; Add license check by @happyandslow in https://github.com/aibrix/aibrix/pull/73
* add github workflow to lint & test code by @M00nF1sh in https://github.com/aibrix/aibrix/pull/74
* [CI] Fix the golang lint issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/77
* [CI] fix the failures from make test by @Jeffwan in https://github.com/aibrix/aibrix/pull/80
* [Misc] Add code-generator and openapi-gen as dependencies by @Jeffwan in https://github.com/aibrix/aibrix/pull/59
* [Misc] Reconcile hpa, kpa and apa separately by @Jeffwan in https://github.com/aibrix/aibrix/pull/83
* [feat] Add rpm/tpm extension proc plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/79
* Add kpa scale algorithm implementation by @kr11 in https://github.com/aibrix/aibrix/pull/87
* Add host override to query specific pod by @varungup90 in https://github.com/aibrix/aibrix/pull/86
* [Core] init aibrix runtime framework by @brosoul in https://github.com/aibrix/aibrix/pull/88
* Support kpa/apa autoscaling workflow part I by @Jeffwan in https://github.com/aibrix/aibrix/pull/85
* Fix Dockerfile Packaging Issues Related to Go Version and Missing Utils by @kr11 in https://github.com/aibrix/aibrix/pull/92
* Autoscaling Workflow Enhancement - Part 2 by @kr11 in https://github.com/aibrix/aibrix/pull/94
* Add custom CRD clientset by @varungup90 in https://github.com/aibrix/aibrix/pull/97
* Autoscaling Workflow Enhancement - Part 3  by @kr11 in https://github.com/aibrix/aibrix/pull/101
* [Core] Add Downloader implementation for runtime by @brosoul in https://github.com/aibrix/aibrix/pull/96
* Add RayClusterReplicaSet and RayClusterFleet apis by @Jeffwan in https://github.com/aibrix/aibrix/pull/103
* Apply crd:maxDescLen=0 in manifest generation by @Jeffwan in https://github.com/aibrix/aibrix/pull/108
* Apply filter to objects owned by model adapters by @varungup90 in https://github.com/aibrix/aibrix/pull/111
* Add custom cache and interface for model adapter scheduling by @varungup90 in https://github.com/aibrix/aibrix/pull/100
* Refactor gateway package by @varungup90 in https://github.com/aibrix/aibrix/pull/112
* BatchAPI storage component together with test  by @xinchen384 in https://github.com/aibrix/aibrix/pull/104
* Update the installation guidance and README.md by @Jeffwan in https://github.com/aibrix/aibrix/pull/115
* [CI] Package AI Runtime by @brosoul in https://github.com/aibrix/aibrix/pull/118
* Add gateway installation by @varungup90 in https://github.com/aibrix/aibrix/pull/122
* [CI] Support container image build and push in CI by @Jeffwan in https://github.com/aibrix/aibrix/pull/120
* [CI] Fix nightly image push error by @Jeffwan in https://github.com/aibrix/aibrix/pull/127
* [Bug] Fix download bugs during download benchmark by @brosoul in https://github.com/aibrix/aibrix/pull/134
* Autoscaling Workflow Enhancement - Part 4: Integrating MetricClient into Autoscaling Workflow by @kr11 in https://github.com/aibrix/aibrix/pull/116
* Update make generate by @varungup90 in https://github.com/aibrix/aibrix/pull/132
* Model adapter controller improvement and refactor by @Jeffwan in https://github.com/aibrix/aibrix/pull/135
* Improve the aibrix installation scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/141
* [CI] Support python package publish by @brosoul in https://github.com/aibrix/aibrix/pull/138
* Fix some typo and naming issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/150
* Fix gateway bootstrap issues by @varungup90 in https://github.com/aibrix/aibrix/pull/154
* Add kubeconfig flag for cache initialization by @varungup90 in https://github.com/aibrix/aibrix/pull/155
* Using sphinx to generate html pages for our project static site by @xinchen384 in https://github.com/aibrix/aibrix/pull/153
* Add finalizer and handle the model unload requests by @Jeffwan in https://github.com/aibrix/aibrix/pull/152

## New Contributors
* @jsw-zorro made their first contribution in https://github.com/aibrix/aibrix/pull/38
* @happyandslow made their first contribution in https://github.com/aibrix/aibrix/pull/73
* @M00nF1sh made their first contribution in https://github.com/aibrix/aibrix/pull/74

**Full Changelog**: https://github.com/aibrix/aibrix/commits/v0.1.0-rc.1

## v0.1.0-rc.2 (2024-09-25)

Automatically generated release for tag v0.1.0-rc.2.

## What's Changed
* Fix kubeConfig redefined issue and update imagePullPolicy by @Jeffwan in https://github.com/aibrix/aibrix/pull/158
* Add expectation lib to allows us to set and wait on expectations by @Jeffwan in https://github.com/aibrix/aibrix/pull/164
* Add routing algorithms by @varungup90 in https://github.com/aibrix/aibrix/pull/143
* Add readthedocs configuration for CI builds and update theme by @Jeffwan in https://github.com/aibrix/aibrix/pull/169
* Add RayClusterReplicaSet initial implementation by @Jeffwan in https://github.com/aibrix/aibrix/pull/165
* Add template page for the docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/170
* Remove myst_parser from sphinx extensions by @Jeffwan in https://github.com/aibrix/aibrix/pull/172
* Update quickstart in the doc by @Jeffwan in https://github.com/aibrix/aibrix/pull/174
* Metric standardizing in ai runtime by @brosoul in https://github.com/aibrix/aibrix/pull/163
* [Misc] Rename env in runtime by @brosoul in https://github.com/aibrix/aibrix/pull/176
* Add readiness check for redis in gateway plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/173
* [batch] job manager handles job state transition by @xinchen384 in https://github.com/aibrix/aibrix/pull/180
* Add users CRUD API by @varungup90 in https://github.com/aibrix/aibrix/pull/181
* Add routing for model adapter by @varungup90 in https://github.com/aibrix/aibrix/pull/183
* Add installation tests and refactor some CI jobs by @Jeffwan in https://github.com/aibrix/aibrix/pull/188
* Add release pipeline for images and manifests by @Jeffwan in https://github.com/aibrix/aibrix/pull/189
* [Docs] Update Readme on project intro by @xieus in https://github.com/aibrix/aibrix/pull/191
* [CI] Add AI Runtime test case by @brosoul in https://github.com/aibrix/aibrix/pull/197
* Add AI Runtime exist model check by @brosoul in https://github.com/aibrix/aibrix/pull/198
* Implement rayclusterfleet controller by @Jeffwan in https://github.com/aibrix/aibrix/pull/194
* klog Level Standardization by @kr11 in https://github.com/aibrix/aibrix/pull/202
* Fix RayClusterReplicaSet e2e running issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/200
* Add lora adapter management API by @brosoul in https://github.com/aibrix/aibrix/pull/201
* Add kuberay manifest as installation dependencies by @Jeffwan in https://github.com/aibrix/aibrix/pull/203
* [doc] fix autoscaling readme by @kr11 in https://github.com/aibrix/aibrix/pull/215
* [doc] update runtime feature doc by @brosoul in https://github.com/aibrix/aibrix/pull/216
* Fix the annotation missing issue for ray workload by @Jeffwan in https://github.com/aibrix/aibrix/pull/218
* [CI]: Add python test on different python version by @brosoul in https://github.com/aibrix/aibrix/pull/219
* Add Autoscaling Tutorials in format of rst by @kr11 in https://github.com/aibrix/aibrix/pull/225
* [Misc] Check AI Runtime download env settings by @brosoul in https://github.com/aibrix/aibrix/pull/221
* Cut v0.1.0-rc.2 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/226

## New Contributors
* @xieus made their first contribution in https://github.com/aibrix/aibrix/pull/191

**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.0-rc.1...v0.1.0-rc.2

## v0.1.0-rc.3 (2024-10-09)

Automatically generated release for tag v0.1.0-rc.3.

## What's Changed
* Add model adapter and multi-node inference docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/222
* add gateway docs by @varungup90 in https://github.com/aibrix/aibrix/pull/232
* [Misc] add Runtime dependency for hf_transfer by @brosoul in https://github.com/aibrix/aibrix/pull/240
* Add validation for username and rpm/tpm negative value by @varungup90 in https://github.com/aibrix/aibrix/pull/241
* [CI] Merge python wheel publish process to release build pipeline by @brosoul in https://github.com/aibrix/aibrix/pull/247
* [CI] Push images to Github container registry by @Jeffwan in https://github.com/aibrix/aibrix/pull/246
* [CI] Fix post-submit container push failure by @Jeffwan in https://github.com/aibrix/aibrix/pull/249
* [Misc] Infer model name from model_uri and check AWS credential by @brosoul in https://github.com/aibrix/aibrix/pull/250
* [Misc ]Add runtime api metrics by @brosoul in https://github.com/aibrix/aibrix/pull/251
* [doc] Update release/contribution/quickstart docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/242
* [batch] job FIFO scheduler as baseline by @xinchen384 in https://github.com/aibrix/aibrix/pull/231
* [Misc] Improve the installation component sequence by @Jeffwan in https://github.com/aibrix/aibrix/pull/252
* Fix concurrency issue with gateway RPM plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/244
* Improve model adapter reliability and stability by @Jeffwan in https://github.com/aibrix/aibrix/pull/257
* Remove underscore from dir names and remove account word in rate limiter by @varungup90 in https://github.com/aibrix/aibrix/pull/271
* [Misc] Use klog as the logr implementation by @Jeffwan in https://github.com/aibrix/aibrix/pull/264
* [CI] Unify Dockerfile names and simplify the build scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/263
* Improve model adapter reconcile workflow stability by @Jeffwan in https://github.com/aibrix/aibrix/pull/260
* Add container override for images by @varungup90 in https://github.com/aibrix/aibrix/pull/273
* Add AIBrix Custom Autoscaling Algorithm APA by @kr11 in https://github.com/aibrix/aibrix/pull/223
* Use vllm metrics for routing by @varungup90 in https://github.com/aibrix/aibrix/pull/274
* Update random routing section and add support for anonymous user by @varungup90 in https://github.com/aibrix/aibrix/pull/276
* Add image build details and examples for multi-host inference by @Jeffwan in https://github.com/aibrix/aibrix/pull/278
* Cut v0.1.0-rc.3 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/280


**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.0-rc.2...v0.1.0-rc.3

## v0.1.0-rc.4 (2024-10-22)

## What's Changed

* [Misc] Add sync images step and scripts in release process by @Jeffwan in https://github.com/aibrix/aibrix/pull/283
* [batch] E2E works with driver and request proxy  by @xinchen384 in https://github.com/aibrix/aibrix/pull/272
* Fix address already in use when AIRuntime start in pod by @brosoul in https://github.com/aibrix/aibrix/pull/289
* Read model  name from request body by @varungup90 in https://github.com/aibrix/aibrix/pull/290
* Fix redis bootstrap flaky connection issue by @varungup90 in https://github.com/aibrix/aibrix/pull/293
* skip docs CI if no changes in /docs dir by @varungup90 in https://github.com/aibrix/aibrix/pull/294
* Improve Rayclusterreplicaset Status by @Yicheng-Lu-llll in https://github.com/aibrix/aibrix/pull/295
* Add request trace for profiling by @varungup90 in https://github.com/aibrix/aibrix/pull/291
* Update the crd definiton due to runtime upgrade by @Jeffwan in https://github.com/aibrix/aibrix/pull/298
* Push images to Github registry in release pipeline by @Jeffwan in https://github.com/aibrix/aibrix/pull/301
* Build autoscaler abstractions like fetcher, client and scaler by @Jeffwan in https://github.com/aibrix/aibrix/pull/300
* Support pod autoscaler periodically check by @Jeffwan in https://github.com/aibrix/aibrix/pull/306
* Add timeout in nc check for redis bootstrap by @varungup90 in https://github.com/aibrix/aibrix/pull/309
* Refactor AutoScaler: metricClient, context, reconcile by @kr11 in https://github.com/aibrix/aibrix/pull/308
* Cut v0.1.0-rc.4 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/314

## New Contributors
* @Yicheng-Lu-llll made their first contribution in https://github.com/aibrix/aibrix/pull/295

**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.0-rc.3...v0.1.0-rc.4




## v0.1.0-rc.5 (2024-11-12)

Automatically generated release for tag v0.1.0-rc.5.

## What's Changed
* [doc] update runtime readme by @brosoul in https://github.com/aibrix/aibrix/pull/318
* Add env for routing strategy override by @varungup90 in https://github.com/aibrix/aibrix/pull/323
* Fix pod autoscaler enqueue issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/329
* Autoscaling benchmark by @kr11 in https://github.com/aibrix/aibrix/pull/337
* Initial lora benchmark result by @Jeffwan in https://github.com/aibrix/aibrix/pull/321
* Adding plotting script by @happyandslow in https://github.com/aibrix/aibrix/pull/338
* Update the downloader performance plot by @Jeffwan in https://github.com/aibrix/aibrix/pull/341
* Reduce pod metrics refresh interval by @varungup90 in https://github.com/aibrix/aibrix/pull/343
* Enable ipv6 for envoy proxy by @varungup90 in https://github.com/aibrix/aibrix/pull/342
* Add benchmark scrips for gateway client side changes by @Jeffwan in https://github.com/aibrix/aibrix/pull/340
* Update the plots based on feedback by @Jeffwan in https://github.com/aibrix/aibrix/pull/346
* [batch] use volcano TOS as batch storage by @xinchen384 in https://github.com/aibrix/aibrix/pull/344
* Add check if no pods are present by @varungup90 in https://github.com/aibrix/aibrix/pull/345
* Add model exists check by @varungup90 in https://github.com/aibrix/aibrix/pull/353
* [Misc] Disable fastapi docs in runtime default action by @brosoul in https://github.com/aibrix/aibrix/pull/350
* Add check for acceptable routing strategies by @varungup90 in https://github.com/aibrix/aibrix/pull/352
* optimize PA messages: const 'HPA' -> actual pa type by @kr11 in https://github.com/aibrix/aibrix/pull/354
* [Misc] Runtime server startup with args by @brosoul in https://github.com/aibrix/aibrix/pull/355
* [Misc] Add python format script by @brosoul in https://github.com/aibrix/aibrix/pull/357
* optimize benchmark scripts for autoscaler, add more logs by @kr11 in https://github.com/aibrix/aibrix/pull/356
* Update the mocked app to cleaner state by @Jeffwan in https://github.com/aibrix/aibrix/pull/361
* Update manifests & docs about service httproute naming trick by @Jeffwan in https://github.com/aibrix/aibrix/pull/362
* Add reference grant to support httprouting for different namespace by @varungup90 in https://github.com/aibrix/aibrix/pull/347
* Validate routing strategy bug fix by @varungup90 in https://github.com/aibrix/aibrix/pull/364
* Bug fix for setting routing strategy via env var by @varungup90 in https://github.com/aibrix/aibrix/pull/369
* Improve the routing env value & flag retrieval by @Jeffwan in https://github.com/aibrix/aibrix/pull/373
* Sync main branch changes to release-0.1 branch by @Jeffwan in https://github.com/aibrix/aibrix/pull/375
* Cut v0.1.0-rc.5 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/376


**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.0-rc.4...v0.1.0-rc.5

## v0.1.0 (2024-11-12)

## Feature Highlights

### 1. Dynamic LoRa Adapter
The Dynamic LoRa Adapter introduces a flexible approach to model adaptation, allowing dynamic management of LoRa models within Kubernetes. This new functionality includes efficient handling of model registration, unloading, and routing, significantly enhancing operational control and scalability for production environments.

### 2. Gateway Extension Server with Multi-Algorithm Routing Support
We extend the Envoy Gateway through an extension server and the external processing service can inspect and mutate requests and responses. We use this way to extend some features not directly supported in kubernetes service like various routing algorithms, such as `least request`, `least throughput`, and `random` and rate limit feature. This flexibility allows users to fine-tune routing strategies based on their specific application needs, ultimately improving traffic distribution and system performance.

### 3. LLM-specific Autoscaler
This release integrates multiple autoscaling algorithms, including HPA (Horizontal Pod Autoscaler), KPA (Knative Pod Autoscaler), and APA (AIBrix Pod Autoscaler). The autoscaling framework now features a direct connection to fetch metrics from pods, enabling real-time adjustments based on load and optimized resource utilization.

### 4. Unified AI Runtime
The AI runtime has been created to support faster model downloading through GPU streaming way, streamlined metrics aggregation, and efficient LoRa request delegation to abstract underlying engine complexities. This runtime provides an optimized environment for deploying and managing machine learning models, making it easier to handle high-volume requests.


### Additional Enhancements:

- **Doc website**: Updated documents, including quick-start guides, installation instructions, and tutorials for autoscaling, make setup and onboarding smoother.
- **Benchmarking and Performance Analysis Tools**: Integrated tools for benchmarking autoscalers, gateways and lora to monitor and improve system efficiency and performance.
- **CI/CD Workflow**: The new CI/CD pipeline includes automated image builds, GitHub Actions for testing and linting, and release pipelines for simplified deployment.

## What's Changed
* Add common project documents and skeleton folders by @Jeffwan in https://github.com/aibrix/aibrix/pull/4
* Scaffolding aibrix project using kubebuilder by @Jeffwan in https://github.com/aibrix/aibrix/pull/17
* Optimize project layouts by moving controllers to pkg folder by @Jeffwan in https://github.com/aibrix/aibrix/pull/21
* Create Lora api and controller by @Jeffwan in https://github.com/aibrix/aibrix/pull/23
* Rename LoraAdapter to ModelAdapter by @Jeffwan in https://github.com/aibrix/aibrix/pull/25
* Add ModelAdapter API by @Jeffwan in https://github.com/aibrix/aibrix/pull/26
* Use better way to set up controller with Manager by @Jeffwan in https://github.com/aibrix/aibrix/pull/27
* Initial model adapter controller implementation by @Jeffwan in https://github.com/aibrix/aibrix/pull/32
* Add mocked model container for lora adapter fast prototyping by @Jeffwan in https://github.com/aibrix/aibrix/pull/33
* [Misc] Add the PR and issues template by @jsw-zorro in https://github.com/aibrix/aibrix/pull/38
* [Docs] Add example to run vLLM distributed inference using Ray by @Jeffwan in https://github.com/aibrix/aibrix/pull/39
* [Doc] Improve the model adapter mock service by @Jeffwan in https://github.com/aibrix/aibrix/pull/45
* [Misc] Simplify the feature/bug/enhancement template. by @jsw-zorro in https://github.com/aibrix/aibrix/pull/48
* [Misc] Make model adapter controller e2e work by @Jeffwan in https://github.com/aibrix/aibrix/pull/50
* [Docs] A draft version of the contributing guideline document by @kr11 in https://github.com/aibrix/aibrix/pull/47
* [Core] Improve model adapter controller by handling existing resources by @Jeffwan in https://github.com/aibrix/aibrix/pull/54
* [Feat] Initial Implementation of PodAutoscaler Reconciler by @kr11 in https://github.com/aibrix/aibrix/pull/55
* [Docs] Move the sample mocked application to common folder by @Jeffwan in https://github.com/aibrix/aibrix/pull/64
* [Misc] Minor refactor the PodAutoscaler codes by @Jeffwan in https://github.com/aibrix/aibrix/pull/68
* [Core] Add model router controller by @varungup90 in https://github.com/aibrix/aibrix/pull/57
* Add rbac rules in model router by @varungup90 in https://github.com/aibrix/aibrix/pull/71
* [bugs] Add autoscaler RBAC to successfully list horizontalpodautoscalers by @kr11 in https://github.com/aibrix/aibrix/pull/72
* [Misc] Update license info; Add license check by @happyandslow in https://github.com/aibrix/aibrix/pull/73
* add github workflow to lint & test code by @M00nF1sh in https://github.com/aibrix/aibrix/pull/74
* [CI] Fix the golang lint issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/77
* [CI] fix the failures from make test by @Jeffwan in https://github.com/aibrix/aibrix/pull/80
* [Misc] Add code-generator and openapi-gen as dependencies by @Jeffwan in https://github.com/aibrix/aibrix/pull/59
* [Misc] Reconcile hpa, kpa and apa separately by @Jeffwan in https://github.com/aibrix/aibrix/pull/83
* [feat] Add rpm/tpm extension proc plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/79
* Add kpa scale algorithm implementation by @kr11 in https://github.com/aibrix/aibrix/pull/87
* Add host override to query specific pod by @varungup90 in https://github.com/aibrix/aibrix/pull/86
* [Core] init aibrix runtime framework by @brosoul in https://github.com/aibrix/aibrix/pull/88
* Support kpa/apa autoscaling workflow part I by @Jeffwan in https://github.com/aibrix/aibrix/pull/85
* Fix Dockerfile Packaging Issues Related to Go Version and Missing Utils by @kr11 in https://github.com/aibrix/aibrix/pull/92
* Autoscaling Workflow Enhancement - Part 2 by @kr11 in https://github.com/aibrix/aibrix/pull/94
* Add custom CRD clientset by @varungup90 in https://github.com/aibrix/aibrix/pull/97
* Autoscaling Workflow Enhancement - Part 3  by @kr11 in https://github.com/aibrix/aibrix/pull/101
* [Core] Add Downloader implementation for runtime by @brosoul in https://github.com/aibrix/aibrix/pull/96
* Add RayClusterReplicaSet and RayClusterFleet apis by @Jeffwan in https://github.com/aibrix/aibrix/pull/103
* Apply crd:maxDescLen=0 in manifest generation by @Jeffwan in https://github.com/aibrix/aibrix/pull/108
* Apply filter to objects owned by model adapters by @varungup90 in https://github.com/aibrix/aibrix/pull/111
* Add custom cache and interface for model adapter scheduling by @varungup90 in https://github.com/aibrix/aibrix/pull/100
* Refactor gateway package by @varungup90 in https://github.com/aibrix/aibrix/pull/112
* BatchAPI storage component together with test  by @xinchen384 in https://github.com/aibrix/aibrix/pull/104
* Update the installation guidance and README.md by @Jeffwan in https://github.com/aibrix/aibrix/pull/115
* [CI] Package AI Runtime by @brosoul in https://github.com/aibrix/aibrix/pull/118
* Add gateway installation by @varungup90 in https://github.com/aibrix/aibrix/pull/122
* [CI] Support container image build and push in CI by @Jeffwan in https://github.com/aibrix/aibrix/pull/120
* [CI] Fix nightly image push error by @Jeffwan in https://github.com/aibrix/aibrix/pull/127
* [Bug] Fix download bugs during download benchmark by @brosoul in https://github.com/aibrix/aibrix/pull/134
* Autoscaling Workflow Enhancement - Part 4: Integrating MetricClient into Autoscaling Workflow by @kr11 in https://github.com/aibrix/aibrix/pull/116
* Update make generate by @varungup90 in https://github.com/aibrix/aibrix/pull/132
* Model adapter controller improvement and refactor by @Jeffwan in https://github.com/aibrix/aibrix/pull/135
* Improve the aibrix installation scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/141
* [CI] Support python package publish by @brosoul in https://github.com/aibrix/aibrix/pull/138
* Fix some typo and naming issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/150
* Fix gateway bootstrap issues by @varungup90 in https://github.com/aibrix/aibrix/pull/154
* Add kubeconfig flag for cache initialization by @varungup90 in https://github.com/aibrix/aibrix/pull/155
* Using sphinx to generate html pages for our project static site by @xinchen384 in https://github.com/aibrix/aibrix/pull/153
* Add finalizer and handle the model unload requests by @Jeffwan in https://github.com/aibrix/aibrix/pull/152
* Fix kubeConfig redefined issue and update imagePullPolicy by @Jeffwan in https://github.com/aibrix/aibrix/pull/158
* Add expectation lib to allows us to set and wait on expectations by @Jeffwan in https://github.com/aibrix/aibrix/pull/164
* Add routing algorithms by @varungup90 in https://github.com/aibrix/aibrix/pull/143
* Add readthedocs configuration for CI builds and update theme by @Jeffwan in https://github.com/aibrix/aibrix/pull/169
* Add RayClusterReplicaSet initial implementation by @Jeffwan in https://github.com/aibrix/aibrix/pull/165
* Add template page for the docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/170
* Remove myst_parser from sphinx extensions by @Jeffwan in https://github.com/aibrix/aibrix/pull/172
* Update quickstart in the doc by @Jeffwan in https://github.com/aibrix/aibrix/pull/174
* Metric standardizing in ai runtime by @brosoul in https://github.com/aibrix/aibrix/pull/163
* [Misc] Rename env in runtime by @brosoul in https://github.com/aibrix/aibrix/pull/176
* Add readiness check for redis in gateway plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/173
* [batch] job manager handles job state transition by @xinchen384 in https://github.com/aibrix/aibrix/pull/180
* Add users CRUD API by @varungup90 in https://github.com/aibrix/aibrix/pull/181
* Add routing for model adapter by @varungup90 in https://github.com/aibrix/aibrix/pull/183
* Add installation tests and refactor some CI jobs by @Jeffwan in https://github.com/aibrix/aibrix/pull/188
* Add release pipeline for images and manifests by @Jeffwan in https://github.com/aibrix/aibrix/pull/189
* [Docs] Update Readme on project intro by @xieus in https://github.com/aibrix/aibrix/pull/191
* [CI] Add AI Runtime test case by @brosoul in https://github.com/aibrix/aibrix/pull/197
* Add AI Runtime exist model check by @brosoul in https://github.com/aibrix/aibrix/pull/198
* Implement rayclusterfleet controller by @Jeffwan in https://github.com/aibrix/aibrix/pull/194
* klog Level Standardization by @kr11 in https://github.com/aibrix/aibrix/pull/202
* Fix RayClusterReplicaSet e2e running issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/200
* Add lora adapter management API by @brosoul in https://github.com/aibrix/aibrix/pull/201
* Add kuberay manifest as installation dependencies by @Jeffwan in https://github.com/aibrix/aibrix/pull/203
* [doc] fix autoscaling readme by @kr11 in https://github.com/aibrix/aibrix/pull/215
* [doc] update runtime feature doc by @brosoul in https://github.com/aibrix/aibrix/pull/216
* Fix the annotation missing issue for ray workload by @Jeffwan in https://github.com/aibrix/aibrix/pull/218
* [CI]: Add python test on different python version by @brosoul in https://github.com/aibrix/aibrix/pull/219
* Add Autoscaling Tutorials in format of rst by @kr11 in https://github.com/aibrix/aibrix/pull/225
* [Misc] Check AI Runtime download env settings by @brosoul in https://github.com/aibrix/aibrix/pull/221
* Cut v0.1.0-rc.2 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/226
* Add model adapter and multi-node inference docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/222
* add gateway docs by @varungup90 in https://github.com/aibrix/aibrix/pull/232
* [Misc] add Runtime dependency for hf_transfer by @brosoul in https://github.com/aibrix/aibrix/pull/240
* Add validation for username and rpm/tpm negative value by @varungup90 in https://github.com/aibrix/aibrix/pull/241
* [CI] Merge python wheel publish process to release build pipeline by @brosoul in https://github.com/aibrix/aibrix/pull/247
* [CI] Push images to Github container registry by @Jeffwan in https://github.com/aibrix/aibrix/pull/246
* [CI] Fix post-submit container push failure by @Jeffwan in https://github.com/aibrix/aibrix/pull/249
* [Misc] Infer model name from model_uri and check AWS credential by @brosoul in https://github.com/aibrix/aibrix/pull/250
* [Misc ]Add runtime api metrics by @brosoul in https://github.com/aibrix/aibrix/pull/251
* [doc] Update release/contribution/quickstart docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/242
* [batch] job FIFO scheduler as baseline by @xinchen384 in https://github.com/aibrix/aibrix/pull/231
* [Misc] Improve the installation component sequence by @Jeffwan in https://github.com/aibrix/aibrix/pull/252
* Fix concurrency issue with gateway RPM plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/244
* Improve model adapter reliability and stability by @Jeffwan in https://github.com/aibrix/aibrix/pull/257
* Remove underscore from dir names and remove account word in rate limiter by @varungup90 in https://github.com/aibrix/aibrix/pull/271
* [Misc] Use klog as the logr implementation by @Jeffwan in https://github.com/aibrix/aibrix/pull/264
* [CI] Unify Dockerfile names and simplify the build scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/263
* Improve model adapter reconcile workflow stability by @Jeffwan in https://github.com/aibrix/aibrix/pull/260
* Add container override for images by @varungup90 in https://github.com/aibrix/aibrix/pull/273
* Add AIBrix Custom Autoscaling Algorithm APA by @kr11 in https://github.com/aibrix/aibrix/pull/223
* Use vllm metrics for routing by @varungup90 in https://github.com/aibrix/aibrix/pull/274
* Update random routing section and add support for anonymous user by @varungup90 in https://github.com/aibrix/aibrix/pull/276
* Add image build details and examples for multi-host inference by @Jeffwan in https://github.com/aibrix/aibrix/pull/278
* Cut v0.1.0-rc.3 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/280
* Update manifests version to v0.1.0-rc.3 by @Jeffwan in https://github.com/aibrix/aibrix/pull/287
* [Misc] Add sync images step and scripts in release process by @Jeffwan in https://github.com/aibrix/aibrix/pull/283
* [batch] E2E works with driver and request proxy  by @xinchen384 in https://github.com/aibrix/aibrix/pull/272
* Fix address already in use when AIRuntime start in pod by @brosoul in https://github.com/aibrix/aibrix/pull/289
* Read model  name from request body by @varungup90 in https://github.com/aibrix/aibrix/pull/290
* Fix redis bootstrap flaky connection issue by @varungup90 in https://github.com/aibrix/aibrix/pull/293
* skip docs CI if no changes in /docs dir by @varungup90 in https://github.com/aibrix/aibrix/pull/294
* Improve Rayclusterreplicaset Status by @Yicheng-Lu-llll in https://github.com/aibrix/aibrix/pull/295
* Add request trace for profiling by @varungup90 in https://github.com/aibrix/aibrix/pull/291
* Update the crd definiton due to runtime upgrade by @Jeffwan in https://github.com/aibrix/aibrix/pull/298
* Push images to Github registry in release pipeline by @Jeffwan in https://github.com/aibrix/aibrix/pull/301
* Build autoscaler abstractions like fetcher, client and scaler by @Jeffwan in https://github.com/aibrix/aibrix/pull/300
* Support pod autoscaler periodically check by @Jeffwan in https://github.com/aibrix/aibrix/pull/306
* Add timeout in nc check for redis bootstrap by @varungup90 in https://github.com/aibrix/aibrix/pull/309
* Refactor AutoScaler: metricClient, context, reconcile by @kr11 in https://github.com/aibrix/aibrix/pull/308
* Cut v0.1.0-rc.4 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/314
* [doc] update runtime readme by @brosoul in https://github.com/aibrix/aibrix/pull/318
* Add env for routing strategy override by @varungup90 in https://github.com/aibrix/aibrix/pull/323
* Fix pod autoscaler enqueue issues by @Jeffwan in https://github.com/aibrix/aibrix/pull/329
* Autoscaling benchmark by @kr11 in https://github.com/aibrix/aibrix/pull/337
* Initial lora benchmark result by @Jeffwan in https://github.com/aibrix/aibrix/pull/321
* Adding plotting script by @happyandslow in https://github.com/aibrix/aibrix/pull/338
* Update the downloader performance plot by @Jeffwan in https://github.com/aibrix/aibrix/pull/341
* Reduce pod metrics refresh interval by @varungup90 in https://github.com/aibrix/aibrix/pull/343
* Enable ipv6 for envoy proxy by @varungup90 in https://github.com/aibrix/aibrix/pull/342
* Add benchmark scrips for gateway client side changes by @Jeffwan in https://github.com/aibrix/aibrix/pull/340
* Update the plots based on feedback by @Jeffwan in https://github.com/aibrix/aibrix/pull/346
* [batch] use volcano TOS as batch storage by @xinchen384 in https://github.com/aibrix/aibrix/pull/344
* Add check if no pods are present by @varungup90 in https://github.com/aibrix/aibrix/pull/345
* Add model exists check by @varungup90 in https://github.com/aibrix/aibrix/pull/353
* [Misc] Disable fastapi docs in runtime default action by @brosoul in https://github.com/aibrix/aibrix/pull/350
* Add check for acceptable routing strategies by @varungup90 in https://github.com/aibrix/aibrix/pull/352
* optimize PA messages: const 'HPA' -> actual pa type by @kr11 in https://github.com/aibrix/aibrix/pull/354
* [Misc] Runtime server startup with args by @brosoul in https://github.com/aibrix/aibrix/pull/355
* [Misc] Add python format script by @brosoul in https://github.com/aibrix/aibrix/pull/357
* optimize benchmark scripts for autoscaler, add more logs by @kr11 in https://github.com/aibrix/aibrix/pull/356
* Update the mocked app to cleaner state by @Jeffwan in https://github.com/aibrix/aibrix/pull/361
* Update manifests & docs about service httproute naming trick by @Jeffwan in https://github.com/aibrix/aibrix/pull/362
* Add reference grant to support httprouting for different namespace by @varungup90 in https://github.com/aibrix/aibrix/pull/347
* Validate routing strategy bug fix by @varungup90 in https://github.com/aibrix/aibrix/pull/364
* Bug fix for setting routing strategy via env var by @varungup90 in https://github.com/aibrix/aibrix/pull/369
* Improve the routing env value & flag retrieval by @Jeffwan in https://github.com/aibrix/aibrix/pull/373
* Sync main branch changes to release-0.1 branch by @Jeffwan in https://github.com/aibrix/aibrix/pull/375
* Cut v0.1.0-rc.5 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/376
* Cut v0.1.0-rc.5 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/378
* [runtime] Add download args for control download progress bar by @brosoul in https://github.com/aibrix/aibrix/pull/382
* [runtime] Update tos sdk version to 2.8.0 by @brosoul in https://github.com/aibrix/aibrix/pull/381
* replaced old names AIBricks with AIBrix by @nwangfw in https://github.com/aibrix/aibrix/pull/372
* [Misc] Update logos, docs and some configuration for v0.1.0 by @Jeffwan in https://github.com/aibrix/aibrix/pull/383
* Sync changes from main to release-0.1 by @Jeffwan in https://github.com/aibrix/aibrix/pull/384
* Cut v0.1.0 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/385

## New Contributors
* @Jeffwan made their first contribution in https://github.com/aibrix/aibrix/pull/4
* @jsw-zorro made their first contribution in https://github.com/aibrix/aibrix/pull/38
* @kr11 made their first contribution in https://github.com/aibrix/aibrix/pull/47
* @varungup90  made their first contribution in https://github.com/aibrix/aibrix/pull/57
* @happyandslow made their first contribution in https://github.com/aibrix/aibrix/pull/73
* @M00nF1sh made their first contribution in https://github.com/aibrix/aibrix/pull/74
* @brosoul made their first contribution in https://github.com/aibrix/aibrix/pull/88
* @xinchen384 made their first contribution in https://github.com/aibrix/aibrix/pull/104
* @xieus made their first contribution in https://github.com/aibrix/aibrix/pull/191
* @Yicheng-Lu-llll made their first contribution in https://github.com/aibrix/aibrix/pull/295
* @nwangfw made their first contribution in https://github.com/aibrix/aibrix/pull/372

**Full Changelog**: https://github.com/aibrix/aibrix/commits/v0.1.0

## v0.1.1 (2024-11-21)

Automatically generated release for tag v0.1.1.

## What's Changed
* Cherry-pick - Fix the ticker interval by removing unnecessary ms by @Jeffwan in https://github.com/aibrix/aibrix/pull/425
* Cut v0.1.1 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/427


**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.0...v0.1.1

## v0.2.0-rc.1 (2024-12-10)

## What's Changed

* Add envoy gateway streaming support by @varungup90 in https://github.com/aibrix/aibrix/pull/377
* Add client traffic policy to increase per connection buffer size from 32kb to 256kb by @varungup90 in https://github.com/aibrix/aibrix/pull/395
* Misc: add support to metricsSources property of podautoscaler by @zhangjyr in https://github.com/aibrix/aibrix/pull/371
* [Misc] Update runtime server startup command in v0.1.0 by @brosoul in https://github.com/aibrix/aibrix/pull/396
* [CI] improve the ci efficiency by parallelizing the build tasks by @nwangfw in https://github.com/aibrix/aibrix/pull/398
* Fix the ticker interval by removing unnecessary ms by @Jeffwan in https://github.com/aibrix/aibrix/pull/415
* [Misc] Disable specific endpoints logs by @Jeffwan in https://github.com/aibrix/aibrix/pull/418
* [CI] Github Action trigger condition optimized for cost saving by @nwangfw in https://github.com/aibrix/aibrix/pull/411
* [Misc] Fix the mocked app role permission issue by @Jeffwan in https://github.com/aibrix/aibrix/pull/416
* [CI] Nightly tag removed for release branch by @nwangfw in https://github.com/aibrix/aibrix/pull/422
* Enable setting PodAutoscaler configuration via YAML labels by @kr11 in https://github.com/aibrix/aibrix/pull/409
* Update manifest to adopt v0.1.1 images by @Jeffwan in https://github.com/aibrix/aibrix/pull/429
* [Bug]: duplicated http in rest metrics fetcher (#408) by @zhangjyr in https://github.com/aibrix/aibrix/pull/421
* [MISC]: Improve Request Trace Granularity with Version Control by @zhangjyr in https://github.com/aibrix/aibrix/pull/431
* Support histogram metrics from engine in cache by @Jeffwan in https://github.com/aibrix/aibrix/pull/424
* Support fetching metrics from remote Prometheus server by @Jeffwan in https://github.com/aibrix/aibrix/pull/433
* [CI] Add python wheel to release artifact by @Jeffwan in https://github.com/aibrix/aibrix/pull/434
* Fix update cache pod issue and refactor updatePod handler by @Jeffwan in https://github.com/aibrix/aibrix/pull/439
* Extract common metrics structure to types and utils by @Jeffwan in https://github.com/aibrix/aibrix/pull/438
* Fix gateway startup issue due to missing prometheus config by @Jeffwan in https://github.com/aibrix/aibrix/pull/441
* [feat]: GPU Optimizer and Simulator development app by @zhangjyr in https://github.com/aibrix/aibrix/pull/430
* Add selectrandom fallback in routing and only scraping healthy pods by @Jeffwan in https://github.com/aibrix/aibrix/pull/445
* AIBrix Workload Generator / Scenario Simulator by @happyandslow in https://github.com/aibrix/aibrix/pull/428
* CrashLoopBackOff status detection in CI by @nwangfw in https://github.com/aibrix/aibrix/pull/444
* Support installing individual controllers from giant controller-manager by @nwangfw in https://github.com/aibrix/aibrix/pull/442
* Refactor Scaler: Resolve Issues with Metric Parameter Updates in Multiple KPAs by @kr11 in https://github.com/aibrix/aibrix/pull/437
* Support metrics multi labels for different models by @brosoul in https://github.com/aibrix/aibrix/pull/450
* Add health check api interface for runtime by @Jeffwan in https://github.com/aibrix/aibrix/pull/451
* Fix the service name override issue in rolebindings by @Jeffwan in https://github.com/aibrix/aibrix/pull/453
* Reorganize docs/development and docs/tutorial structure by @Jeffwan in https://github.com/aibrix/aibrix/pull/455
* Move tools to separate folders and update mocked app README.md by @Jeffwan in https://github.com/aibrix/aibrix/pull/457
* Fix multi models metric result in PromQL by @brosoul in https://github.com/aibrix/aibrix/pull/458
* Support Azure LLM trace in workload generator by @happyandslow in https://github.com/aibrix/aibrix/pull/462
* Fix autoscaler scalingstrategy switching logic by @nwangfw in https://github.com/aibrix/aibrix/pull/475
* Fix missing handle of PromQL scope is PodMetricScope by @brosoul in https://github.com/aibrix/aibrix/pull/479
* [Misc] Consolidate app and simulator by @zhangjyr in https://github.com/aibrix/aibrix/pull/477
* [Bug] Avoid including sensitive info in Dockerfile ENV by @zhangjyr in https://github.com/aibrix/aibrix/pull/487
* Refactor generator to generate time-based traces by @happyandslow in https://github.com/aibrix/aibrix/pull/478
* [CI] Update deploy workload script in installation test by @nwangfw in https://github.com/aibrix/aibrix/pull/499
* [Bug] handle metricKey creation with MetricsSources  by @nwangfw in https://github.com/aibrix/aibrix/pull/498
* Adding Client for Workload Generator Workload File by @happyandslow in https://github.com/aibrix/aibrix/pull/501
* [Feat] Integrate deployment configurations and fix autoscaler/gpu optimizer connectivity by @zhangjyr in https://github.com/aibrix/aibrix/pull/500
* Fix some simulator format issue and add some TODOs by @Jeffwan in https://github.com/aibrix/aibrix/pull/505
* [Bug] Fix the way how podautoscaler handle 0 pods. by @zhangjyr in https://github.com/aibrix/aibrix/pull/508
* [Misc] Improve gpu optimizer debugging on podautoscaler. by @zhangjyr in https://github.com/aibrix/aibrix/pull/509
* Optimize kustomize overlay for volcano engine deployment by @Jeffwan in https://github.com/aibrix/aibrix/pull/512
* [perf] Refact tos downloader in Runtime by @brosoul in https://github.com/aibrix/aibrix/pull/510
* Refactor metric source for customized protocol, port and path by @kr11 in https://github.com/aibrix/aibrix/pull/511
* [Bug] Fixed the yaml of deployments in heterogenous GPU settings to make KPA scaling work as expected. by @zhangjyr in https://github.com/aibrix/aibrix/pull/513
* [Misc] Heterogeneous GPU Optimizer Logging Clean Up by @nwangfw in https://github.com/aibrix/aibrix/pull/514
* Fix KPA bug, and an elaborate KPA test case by @kr11 in https://github.com/aibrix/aibrix/pull/515
* Cut v0.2.0-rc.1 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/516


**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.1...v0.2.0-rc.1

## v0.1.2 (2025-01-09)

## What's Changed
* Support absolute path as lora adapter artifact path (#556) by @Jeffwan in https://github.com/aibrix/aibrix/pull/558
* Cherry pick streaming and client traffic policy by @varungup90 in https://github.com/aibrix/aibrix/pull/560
* Cut v0.1.2 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/561

**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.1...v0.1.2

## v0.2.0-rc.2 (2025-01-23)

Automatically generated release for tag v0.2.0-rc.2.

## What's Changed
* [Bug] Accumulated bug fix on controller manager, mock app configuration, and gpu optimizer. by @zhangjyr in https://github.com/aibrix/aibrix/pull/522
* [Misc] Reduced runtime's container image size by @nwangfw in https://github.com/aibrix/aibrix/pull/518
* clean memory scaler object when pa crd is deleted by @kr11 in https://github.com/aibrix/aibrix/pull/520
* Configure autoscaler http client to skip certificate check by @Jeffwan in https://github.com/aibrix/aibrix/pull/530
* [Doc] Update aibrix documentation by @Jeffwan in https://github.com/aibrix/aibrix/pull/533
* Refactor the gateway-plugin and metadata service manifests by @Jeffwan in https://github.com/aibrix/aibrix/pull/531
* Fix the GITHUB_WORKSPACE artifact sharing issue in release workflow by @Jeffwan in https://github.com/aibrix/aibrix/pull/532
* [Misc] Polish the benchmark scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/525
* Fix APA bugs in creation, add test and demo yaml by @kr11 in https://github.com/aibrix/aibrix/pull/536
* Add VKE IPv4 Testing Cluster Config by @nwangfw in https://github.com/aibrix/aibrix/pull/537
* Support for request length internal trace by @happyandslow in https://github.com/aibrix/aibrix/pull/538
* [Feat] Add download status into runtime downloader by @brosoul in https://github.com/aibrix/aibrix/pull/539
* [Feat] Add runtime model management api by @brosoul in https://github.com/aibrix/aibrix/pull/540
* [gateway] handle the wrong model name and cache inconsistency case by @Jeffwan in https://github.com/aibrix/aibrix/pull/542
* [Docs] fix: update the parameters instruction in readme by @scarlet25151 in https://github.com/aibrix/aibrix/pull/548
* add lora schedulers - bin pack, least latency, least throughput, random by @Aspirin96 in https://github.com/aibrix/aibrix/pull/544
* add request routers - least kv cache, least expected latency by @Aspirin96 in https://github.com/aibrix/aibrix/pull/543
* [Docs] heterogenous gpu docs added by @nwangfw in https://github.com/aibrix/aibrix/pull/545
* Fix race condition in cache by @varungup90 in https://github.com/aibrix/aibrix/pull/550
* Fix pod internal cache delete handling by @varungup90 in https://github.com/aibrix/aibrix/pull/552
* Handle terminating pod for request routing by @varungup90 in https://github.com/aibrix/aibrix/pull/549
* Support absolute path as lora adapter artifact path by @Jeffwan in https://github.com/aibrix/aibrix/pull/556
* Deadlock fix for cache by @varungup90 in https://github.com/aibrix/aibrix/pull/557
* Mock app log fix for missing metrics warning by @varungup90 in https://github.com/aibrix/aibrix/pull/564
* Add vllm graceful termination configuration by @nwangfw in https://github.com/aibrix/aibrix/pull/568
* Enhance dynamic lora adapter support for auth enabled scenario by @Jeffwan in https://github.com/aibrix/aibrix/pull/571
* Update pyproject.toml to support python 3.12 by @Jeffwan in https://github.com/aibrix/aibrix/pull/579
* [Docs ]Update ai runtime management api and downloader docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/577
* Check the HPA ownerReference in request enqueue by @Jeffwan in https://github.com/aibrix/aibrix/pull/582
* Add request length for traces by @happyandslow in https://github.com/aibrix/aibrix/pull/569
* Support model registration flow using aibrix runtime api by @Jeffwan in https://github.com/aibrix/aibrix/pull/580
* Gateway plugin report total incoming requests and pending requests by @zhangjyr in https://github.com/aibrix/aibrix/pull/554
* Support distributed kv cache orchestration by @Jeffwan in https://github.com/aibrix/aibrix/pull/583
* Grant workflow action permission to write packages by @Jeffwan in https://github.com/aibrix/aibrix/pull/586
* Update routers to use GetPodModelMetric api and misc cleanup in metri… by @varungup90 in https://github.com/aibrix/aibrix/pull/590
* Update upload/download artifact github actions version to v4 by @varungup90 in https://github.com/aibrix/aibrix/pull/591
* Update version in aibrix/python to 0.2.0-rc.2 by @varungup90 in https://github.com/aibrix/aibrix/pull/594

## New Contributors
* @scarlet25151 made their first contribution in https://github.com/aibrix/aibrix/pull/548
* @Aspirin96 made their first contribution in https://github.com/aibrix/aibrix/pull/544

**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.2.0-rc.1...v0.2.0-rc.2

## v0.2.0 (2025-02-19)

Automatically generated release for tag v0.2.0.

## 🚀 New Features Highlights
- **Distributed KV Cache**: Implemented support for managing KV cache across multiple nodes, enhancing performance. 
- **Cost-Driven Heterogenous Serving**: Improved scheduling and inference strategies for mixed GPU environments, optimizing cost and resource utilization. (#371 #430, #509, #598, #554, #598)
- **Optimizer Based Autoscaling**: Leverage offline profiles of inference server to calculate the number of replicas. (#430, #500, #692, #508)
- **Prefix Cache Aware Routing**: Added support for routing decisions based on prefix cache hits, improving inference efficiency. (#641, #657)

## 📊 Feature Enhancements
- **LoRA Scheduling Enhancements**: Introduced multiple scheduling strategies, including bin packing, least latency, least throughput, and random. (#544)
- **Prefix Cache Aware Routing**: Added support for routing decisions based on prefix cache hits, improving inference efficiency. (#641)
- **Gateway Enhancements**:  Improved request handling efficiency by enabling streaming in the Envoy gateway. (#377) Enhanced the handling of model registration and invalid cache scenarios. (#542), Introduced fallback strategies to ensure robust request allocation. (#445) Optimized cache store retrieval, reducing unnecessary overhead. (#639) Addressed missing Prometheus config preventing gateway startup. (#441)
- **PodAutoscaler Scaling improvements**: Improved scaling logic to handle edge cases more efficiently. (#508, #515)

## 🛠Infrastructure & CI/CD Upgrades
- Parallelized Build Tasks: CI efficiency improvements by running builds in parallel. (#398)
- CrashLoopBackOff Detection in CI: Added monitoring for pod failures in testing workflows. (#444)
- Improved GitHub Actions Cost Efficiency: Optimized triggers and removed unnecessary nightly builds. (#411, #422)
- Integration Tests for Core Components: Added integration tests for autoscalers, routing policies, and deployment configurations. (#616, #620)


## What's Changed
* Add envoy gateway streaming support by @varungup90 in https://github.com/aibrix/aibrix/pull/377
* Add client traffic policy to increase per connection buffer size from 32kb to 256kb by @varungup90 in https://github.com/aibrix/aibrix/pull/395
* Misc: add support to metricsSources property of podautoscaler by @zhangjyr in https://github.com/aibrix/aibrix/pull/371
* [Misc] Update runtime server startup command in v0.1.0 by @brosoul in https://github.com/aibrix/aibrix/pull/396
* [CI] improve the ci efficiency by parallelizing the build tasks by @nwangfw in https://github.com/aibrix/aibrix/pull/398
* Fix the ticker interval by removing unnecessary ms by @Jeffwan in https://github.com/aibrix/aibrix/pull/415
* [Misc] Disable specific endpoints logs by @Jeffwan in https://github.com/aibrix/aibrix/pull/418
* [CI] Github Action trigger condition optimized for cost saving by @nwangfw in https://github.com/aibrix/aibrix/pull/411
* [Misc] Fix the mocked app role permission issue by @Jeffwan in https://github.com/aibrix/aibrix/pull/416
* [CI] Nightly tag removed for release branch by @nwangfw in https://github.com/aibrix/aibrix/pull/422
* Enable setting PodAutoscaler configuration via YAML labels by @kr11 in https://github.com/aibrix/aibrix/pull/409
* Update manifest to adopt v0.1.1 images by @Jeffwan in https://github.com/aibrix/aibrix/pull/429
* [Bug]: duplicated http in rest metrics fetcher (#408) by @zhangjyr in https://github.com/aibrix/aibrix/pull/421
* [MISC]: Improve Request Trace Granularity with Version Control by @zhangjyr in https://github.com/aibrix/aibrix/pull/431
* Support histogram metrics from engine in cache by @Jeffwan in https://github.com/aibrix/aibrix/pull/424
* Support fetching metrics from remote Prometheus server by @Jeffwan in https://github.com/aibrix/aibrix/pull/433
* [CI] Add python wheel to release artifact by @Jeffwan in https://github.com/aibrix/aibrix/pull/434
* Fix update cache pod issue and refactor updatePod handler by @Jeffwan in https://github.com/aibrix/aibrix/pull/439
* Extract common metrics structure to types and utils by @Jeffwan in https://github.com/aibrix/aibrix/pull/438
* Fix gateway startup issue due to missing prometheus config by @Jeffwan in https://github.com/aibrix/aibrix/pull/441
* [feat]: GPU Optimizer and Simulator development app by @zhangjyr in https://github.com/aibrix/aibrix/pull/430
* Add selectrandom fallback in routing and only scraping healthy pods by @Jeffwan in https://github.com/aibrix/aibrix/pull/445
* AIBrix Workload Generator / Scenario Simulator by @happyandslow in https://github.com/aibrix/aibrix/pull/428
* CrashLoopBackOff status detection in CI by @nwangfw in https://github.com/aibrix/aibrix/pull/444
* Support installing individual controllers from giant controller-manager by @nwangfw in https://github.com/aibrix/aibrix/pull/442
* Refactor Scaler: Resolve Issues with Metric Parameter Updates in Multiple KPAs by @kr11 in https://github.com/aibrix/aibrix/pull/437
* Support metrics multi labels for different models by @brosoul in https://github.com/aibrix/aibrix/pull/450
* Add health check api interface for runtime by @Jeffwan in https://github.com/aibrix/aibrix/pull/451
* Fix the service name override issue in rolebindings by @Jeffwan in https://github.com/aibrix/aibrix/pull/453
* Reorganize docs/development and docs/tutorial structure by @Jeffwan in https://github.com/aibrix/aibrix/pull/455
* Move tools to separate folders and update mocked app README.md by @Jeffwan in https://github.com/aibrix/aibrix/pull/457
* Fix multi models metric result in PromQL by @brosoul in https://github.com/aibrix/aibrix/pull/458
* Support Azure LLM trace in workload generator by @happyandslow in https://github.com/aibrix/aibrix/pull/462
* Fix autoscaler scalingstrategy switching logic by @nwangfw in https://github.com/aibrix/aibrix/pull/475
* Fix missing handle of PromQL scope is PodMetricScope by @brosoul in https://github.com/aibrix/aibrix/pull/479
* [Misc] Consolidate app and simulator by @zhangjyr in https://github.com/aibrix/aibrix/pull/477
* [Bug] Avoid including sensitive info in Dockerfile ENV by @zhangjyr in https://github.com/aibrix/aibrix/pull/487
* Refactor generator to generate time-based traces by @happyandslow in https://github.com/aibrix/aibrix/pull/478
* [CI] Update deploy workload script in installation test by @nwangfw in https://github.com/aibrix/aibrix/pull/499
* [Bug] handle metricKey creation with MetricsSources  by @nwangfw in https://github.com/aibrix/aibrix/pull/498
* Adding Client for Workload Generator Workload File by @happyandslow in https://github.com/aibrix/aibrix/pull/501
* [Feat] Integrate deployment configurations and fix autoscaler/gpu optimizer connectivity by @zhangjyr in https://github.com/aibrix/aibrix/pull/500
* Fix some simulator format issue and add some TODOs by @Jeffwan in https://github.com/aibrix/aibrix/pull/505
* [Bug] Fix the way how podautoscaler handle 0 pods. by @zhangjyr in https://github.com/aibrix/aibrix/pull/508
* [Misc] Improve gpu optimizer debugging on podautoscaler. by @zhangjyr in https://github.com/aibrix/aibrix/pull/509
* Optimize kustomize overlay for volcano engine deployment by @Jeffwan in https://github.com/aibrix/aibrix/pull/512
* [perf] Refact tos downloader in Runtime by @brosoul in https://github.com/aibrix/aibrix/pull/510
* Refactor metric source for customized protocol, port and path by @kr11 in https://github.com/aibrix/aibrix/pull/511
* [Bug] Fixed the yaml of deployments in heterogenous GPU settings to make KPA scaling work as expected. by @zhangjyr in https://github.com/aibrix/aibrix/pull/513
* [Misc] Heterogeneous GPU Optimizer Logging Clean Up by @nwangfw in https://github.com/aibrix/aibrix/pull/514
* Fix KPA bug, and an elaborate KPA test case by @kr11 in https://github.com/aibrix/aibrix/pull/515
* Cut v0.2.0-rc.1 release by @Jeffwan in https://github.com/aibrix/aibrix/pull/516
* [Bug] Accumulated bug fix on controller manager, mock app configuration, and gpu optimizer. by @zhangjyr in https://github.com/aibrix/aibrix/pull/522
* [Misc] Reduced runtime's container image size by @nwangfw in https://github.com/aibrix/aibrix/pull/518
* clean memory scaler object when pa crd is deleted by @kr11 in https://github.com/aibrix/aibrix/pull/520
* Configure autoscaler http client to skip certificate check by @Jeffwan in https://github.com/aibrix/aibrix/pull/530
* [Doc] Update aibrix documentation by @Jeffwan in https://github.com/aibrix/aibrix/pull/533
* Refactor the gateway-plugin and metadata service manifests by @Jeffwan in https://github.com/aibrix/aibrix/pull/531
* Fix the GITHUB_WORKSPACE artifact sharing issue in release workflow by @Jeffwan in https://github.com/aibrix/aibrix/pull/532
* [Misc] Polish the benchmark scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/525
* Fix APA bugs in creation, add test and demo yaml by @kr11 in https://github.com/aibrix/aibrix/pull/536
* Add VKE IPv4 Testing Cluster Config by @nwangfw in https://github.com/aibrix/aibrix/pull/537
* Support for request length internal trace by @happyandslow in https://github.com/aibrix/aibrix/pull/538
* [Feat] Add download status into runtime downloader by @brosoul in https://github.com/aibrix/aibrix/pull/539
* [Feat] Add runtime model management api by @brosoul in https://github.com/aibrix/aibrix/pull/540
* [gateway] handle the wrong model name and cache inconsistency case by @Jeffwan in https://github.com/aibrix/aibrix/pull/542
* [Docs] fix: update the parameters instruction in readme by @scarlet25151 in https://github.com/aibrix/aibrix/pull/548
* add lora schedulers - bin pack, least latency, least throughput, random by @Aspirin96 in https://github.com/aibrix/aibrix/pull/544
* add request routers - least kv cache, least expected latency by @Aspirin96 in https://github.com/aibrix/aibrix/pull/543
* [Docs] heterogenous gpu docs added by @nwangfw in https://github.com/aibrix/aibrix/pull/545
* Fix race condition in cache by @varungup90 in https://github.com/aibrix/aibrix/pull/550
* Fix pod internal cache delete handling by @varungup90 in https://github.com/aibrix/aibrix/pull/552
* Handle terminating pod for request routing by @varungup90 in https://github.com/aibrix/aibrix/pull/549
* Support absolute path as lora adapter artifact path by @Jeffwan in https://github.com/aibrix/aibrix/pull/556
* Deadlock fix for cache by @varungup90 in https://github.com/aibrix/aibrix/pull/557
* Mock app log fix for missing metrics warning by @varungup90 in https://github.com/aibrix/aibrix/pull/564
* Add vllm graceful termination configuration by @nwangfw in https://github.com/aibrix/aibrix/pull/568
* Enhance dynamic lora adapter support for auth enabled scenario by @Jeffwan in https://github.com/aibrix/aibrix/pull/571
* Update pyproject.toml to support python 3.12 by @Jeffwan in https://github.com/aibrix/aibrix/pull/579
* [Docs ]Update ai runtime management api and downloader docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/577
* Check the HPA ownerReference in request enqueue by @Jeffwan in https://github.com/aibrix/aibrix/pull/582
* Add request length for traces by @happyandslow in https://github.com/aibrix/aibrix/pull/569
* Support model registration flow using aibrix runtime api by @Jeffwan in https://github.com/aibrix/aibrix/pull/580
* Gateway plugin report total incoming requests and pending requests by @zhangjyr in https://github.com/aibrix/aibrix/pull/554
* Support distributed kv cache orchestration by @Jeffwan in https://github.com/aibrix/aibrix/pull/583
* Grant workflow action permission to write packages by @Jeffwan in https://github.com/aibrix/aibrix/pull/586
* Update routers to use GetPodModelMetric api and misc cleanup in metri… by @varungup90 in https://github.com/aibrix/aibrix/pull/590
* Update upload/download artifact github actions version to v4 by @varungup90 in https://github.com/aibrix/aibrix/pull/591
* Update version in aibrix/python to 0.2.0-rc.2 by @varungup90 in https://github.com/aibrix/aibrix/pull/594
* Update image names in sync-image script by @varungup90 in https://github.com/aibrix/aibrix/pull/595
* Update dependency chart for release pipeline by @varungup90 in https://github.com/aibrix/aibrix/pull/597
* Patch release for older vllm engine lora support in gateway plugins by @varungup90 in https://github.com/aibrix/aibrix/pull/599
* Update component names in staging deployment and readme for new relea… by @varungup90 in https://github.com/aibrix/aibrix/pull/605
* Fix the PodAutoscaler kind typo by @Jeffwan in https://github.com/aibrix/aibrix/pull/610
* Improve condition update and fix multiple endpoint ips issue by @Jeffwan in https://github.com/aibrix/aibrix/pull/609
* Check if model name is present in response from inference engine by @varungup90 in https://github.com/aibrix/aibrix/pull/611
* Update log level for few messages in PodAutoscaler by @varungup90 in https://github.com/aibrix/aibrix/pull/612
* [enhancement] GPU optimizer accumulated fix by @zhangjyr in https://github.com/aibrix/aibrix/pull/598
* Update manifest to use v0.2.0-rc.2 tag by @Jeffwan in https://github.com/aibrix/aibrix/pull/614
* Add framework to setup integration test by @varungup90 in https://github.com/aibrix/aibrix/pull/616
* [docs] Update lora model adapter docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/618
* [docs] Update AI Engine Runtime and Fleet docs by @Jeffwan in https://github.com/aibrix/aibrix/pull/619
* [Doc] update quickstart tutorial and add example sending requests via gatew… by @nwangfw in https://github.com/aibrix/aibrix/pull/621
* [Doc] feature description for distributed kv cache by @DwyaneShi in https://github.com/aibrix/aibrix/pull/623
* WIP: Add docs gateway plugin by @varungup90 in https://github.com/aibrix/aibrix/pull/624
* [Docs] Update GPU Optimizer documentation by @zhangjyr in https://github.com/aibrix/aibrix/pull/622
* Add integration test to CI workflow by @varungup90 in https://github.com/aibrix/aibrix/pull/620
* [Docs] Updated autoscaling doc by @gangmuk in https://github.com/aibrix/aibrix/pull/625
* Filter active pods before metrics calculation by @Jeffwan in https://github.com/aibrix/aibrix/pull/629
* Fix some issues in the docs and polish contents by @Jeffwan in https://github.com/aibrix/aibrix/pull/630
* Ignore Jupyter notebooks for GitHub Linguist by @Jeffwan in https://github.com/aibrix/aibrix/pull/632
* [Docs] Improving the heterogenous-GPU feature doc by @nwangfw in https://github.com/aibrix/aibrix/pull/634
* [Doc] Fixed autoscaling doc by @gangmuk in https://github.com/aibrix/aibrix/pull/635
* Fix out of space error in running integration test github workflow by @varungup90 in https://github.com/aibrix/aibrix/pull/628
* Use AIBRIX_POD_METRIC_REFRESH_INTERVAL_MS=50 in base configs by @Jeffwan in https://github.com/aibrix/aibrix/pull/640
* Fix the least-kv-cache cache store retrieval by @Jeffwan in https://github.com/aibrix/aibrix/pull/639
* Add prefix cache aware routing by @varungup90 in https://github.com/aibrix/aibrix/pull/641
* [misc] Polish gateway code with better structure by @Jeffwan in https://github.com/aibrix/aibrix/pull/645
* Create AIBrix Single-Node Deployment on Lambda scripts by @Jeffwan in https://github.com/aibrix/aibrix/pull/659
* End-to-end benchmark pipeline for autoscalers and routing policies by @gangmuk in https://github.com/aibrix/aibrix/pull/650
* Clean up scripts under hack folder by @Jeffwan in https://github.com/aibrix/aibrix/pull/660
* Add a research section, update architecture and lambda guidance by @Jeffwan in https://github.com/aibrix/aibrix/pull/663
* Leverage literalinclude to keep only one code copy and move autoscaler configs to annotations by @Jeffwan in https://github.com/aibrix/aibrix/pull/665
* Updated scripts and fixed issues in benchmark/autoscaling by @gangmuk in https://github.com/aibrix/aibrix/pull/662
* Benchmark Generator Refactoring by @happyandslow in https://github.com/aibrix/aibrix/pull/655
* Add interface for prefix cache indexer by @varungup90 in https://github.com/aibrix/aibrix/pull/657
* Fix missing file to generator refactoring  by @happyandslow in https://github.com/aibrix/aibrix/pull/670
* [Bug] GPU optimizer bug fix and document fix by @zhangjyr in https://github.com/aibrix/aibrix/pull/656
* Change error response to json and improve e2e stability by @Jeffwan in https://github.com/aibrix/aibrix/pull/669
* Use response buffer to address stream request issue by @Jeffwan in https://github.com/aibrix/aibrix/pull/679
* [docs] Polish feature examples and user guidances by @Jeffwan in https://github.com/aibrix/aibrix/pull/686
* Update version and tags to v0.2.0 by @Jeffwan in https://github.com/aibrix/aibrix/pull/687
* fix api scheme by @kerthcet in https://github.com/aibrix/aibrix/pull/674
* [docs] Polish distributed inference and kv cache examples by @Jeffwan in https://github.com/aibrix/aibrix/pull/691
* Improve lora autoscaling and kvcache examples by @Jeffwan in https://github.com/aibrix/aibrix/pull/697
* [Docs] Add optimizer-based autoscaling doc and examples by @nwangfw in https://github.com/aibrix/aibrix/pull/692
* Add cpu/memory resources for control plane components by @varungup90 in https://github.com/aibrix/aibrix/pull/702
* Update log config for sample deployments by @varungup90 in https://github.com/aibrix/aibrix/pull/704
* [Docs] Add feature description of dist kv cache in README by @DwyaneShi in https://github.com/aibrix/aibrix/pull/705
* [Docs] Update README.md by @Jeffwan in https://github.com/aibrix/aibrix/pull/706
* Add feature description for heterogeneous gpu inference feature by @nwangfw in https://github.com/aibrix/aibrix/pull/707
* Bump py version to 0.2.0.post1 by @Jeffwan in https://github.com/aibrix/aibrix/pull/708
* Fix wrong path for generated html by @kerthcet in https://github.com/aibrix/aibrix/pull/709

## New Contributors
* @scarlet25151 made their first contribution in https://github.com/aibrix/aibrix/pull/548
* @Aspirin96 made their first contribution in https://github.com/aibrix/aibrix/pull/544
* @DwyaneShi made their first contribution in https://github.com/aibrix/aibrix/pull/623
* @gangmuk made their first contribution in https://github.com/aibrix/aibrix/pull/625
* @kerthcet made their first contribution in https://github.com/aibrix/aibrix/pull/674

**Full Changelog**: https://github.com/aibrix/aibrix/compare/v0.1.0...v0.2.0

## v0.2.1 (2025-03-09)

Automatically generated release for tag v0.2.1.

## What's Changed
* Cherry-pick Enable CI tests for release branch (#805) by @Jeffwan in https://github.com/vllm-project/aibrix/pull/808
* Cherry pick #776 #779 #788 #789 #794 to release branch by @Jeffwan @varungup90  in https://github.com/vllm-project/aibrix/pull/809
* Cherry-pick #825 #826 part of #717 in release branch by @varungup90 @Jeffwan  in https://github.com/vllm-project/aibrix/pull/828
* Update version and tags to v0.2.1 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/833


**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.2.0...v0.2.1

## v0.3.0-rc.1 (2025-05-13)


## What's Changed
* [Docs] fix format of the dist kv cache doc by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/714
* complete the 'make generate' command by @kerthcet in https://github.com/vllm-project/aibrix/pull/711
* Update organization reference in code base by @Jeffwan in https://github.com/vllm-project/aibrix/pull/717
* [Misc] Update the documentation link by @Jeffwan in https://github.com/vllm-project/aibrix/pull/720
* Initial implementation of radix tree-based cache by @gangmuk in https://github.com/vllm-project/aibrix/pull/678
* Add model adapter e2e tests by @varungup90 in https://github.com/vllm-project/aibrix/pull/701
* Add vllm cpu alternative for local development by @varungup90 in https://github.com/vllm-project/aibrix/pull/721
* Add white paper file by @Jeffwan in https://github.com/vllm-project/aibrix/pull/724
* Adding streaming client for AIbrix experiments by @happyandslow in https://github.com/vllm-project/aibrix/pull/676
* [Docs] Update Readme with new links and blog post, and update white paper by @xieus in https://github.com/vllm-project/aibrix/pull/725
* Recording failed requests in benchmark client by @gangmuk in https://github.com/vllm-project/aibrix/pull/727
* Process response headers in gateway by @varungup90 in https://github.com/vllm-project/aibrix/pull/703
* [misc] Fix white paper link by @Jeffwan in https://github.com/vllm-project/aibrix/pull/728
* Prefix and load aware routing with radix tree kv cache by @gangmuk in https://github.com/vllm-project/aibrix/pull/719
* Fix slack link in README.md by @Jeffwan in https://github.com/vllm-project/aibrix/pull/729
* [readme] Fix wrong link by @gaocegege in https://github.com/vllm-project/aibrix/pull/731
* [Misc] update scheduler.py by @eltociear in https://github.com/vllm-project/aibrix/pull/736
* Improve thread safety for TreeNode data structure and refactor related codes by @gangmuk in https://github.com/vllm-project/aibrix/pull/730
* Fix CacheSpec api scheme by @kerthcet in https://github.com/vllm-project/aibrix/pull/740
* docs: Fix link to license by @terrytangyuan in https://github.com/vllm-project/aibrix/pull/746
* Use native codegen cmd generating client-go by @kerthcet in https://github.com/vllm-project/aibrix/pull/741
* [Docs]: Fixed kubectl commands for install of components by @jolfr in https://github.com/vllm-project/aibrix/pull/744
* [fix] fixing bug in using AsyncOpenAI client (header setting, token counting, etc) by @gangmuk in https://github.com/vllm-project/aibrix/pull/738
* Add webhook framework by @kerthcet in https://github.com/vllm-project/aibrix/pull/748
* Use random seed for xxhash by @varungup90 in https://github.com/vllm-project/aibrix/pull/752
* Create SECURITY.md to enable security policy by @xieus in https://github.com/vllm-project/aibrix/pull/756
* [CI] Add integration test  by @kerthcet in https://github.com/vllm-project/aibrix/pull/759
* [Bug] fix: correct non-inherited context by @Abirdcfly in https://github.com/vllm-project/aibrix/pull/763
* [Misc] Parametrize Makefile for mocked vLLM apps by @pierDipi in https://github.com/vllm-project/aibrix/pull/764
* Support benchmarking script by using real application trace by @nwangfw in https://github.com/vllm-project/aibrix/pull/737
* Maintaining common benchmarks utils in a separate dir by @gangmuk in https://github.com/vllm-project/aibrix/pull/770
* Ignore worker pods for gateway routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/776
* Disable ENABLE_PROBES_INJECTION in correct way by @Jeffwan in https://github.com/vllm-project/aibrix/pull/779
* Make stream include usage as optional by @varungup90 in https://github.com/vllm-project/aibrix/pull/788
* Append ray head label selector in PodAutoscaler by @Jeffwan in https://github.com/vllm-project/aibrix/pull/789
* Remove redundant install crds in makefile by @varungup90 in https://github.com/vllm-project/aibrix/pull/792
* Update request message processing for /v1/completion input by @varungup90 in https://github.com/vllm-project/aibrix/pull/794
* Added target pod to client result and made clients consistent by @gangmuk in https://github.com/vllm-project/aibrix/pull/799
* Enable CI tests for release branch by @Jeffwan in https://github.com/vllm-project/aibrix/pull/805
* Move modelAdapter runtime validation to webhook by @kerthcet in https://github.com/vllm-project/aibrix/pull/786
* [Misc] Adding model field to each request by @happyandslow in https://github.com/vllm-project/aibrix/pull/812
* [Refactor]: gateway-plugins ext-proc server codebase by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/810
* [CI]: update release tags pattern by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/815
* [Docs]: fix vllm mock app Unauthorized response by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/817
* Reconfigure workload generator for predefined synthetic patterns by @happyandslow in https://github.com/vllm-project/aibrix/pull/771
* Workload generation scripts for prefix aware routing by @gangmuk in https://github.com/vllm-project/aibrix/pull/820
* Fix the paths in lambda cloud doc by @gangmuk in https://github.com/vllm-project/aibrix/pull/824
* [Bug] Added Startup Probe in Quickstart Model by @jolfr in https://github.com/vllm-project/aibrix/pull/773
* Add /v1/models endpoint to gateway by @varungup90 in https://github.com/vllm-project/aibrix/pull/802
* Increase envoy proxy memory config and client connection buffersize by @varungup90 in https://github.com/vllm-project/aibrix/pull/825
* Support to create default HttpRoute for RayClusterFleet by @Jeffwan in https://github.com/vllm-project/aibrix/pull/826
* [Misc] Fix CI issue on release branch and clean up logs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/837
* Fix repeated initialization of gateway routers and add unit test for prefix cache by @varungup90 in https://github.com/vllm-project/aibrix/pull/838
* Add deepseek-r1 671B deployment sample and docs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/835
* Bump AIBrix version to v0.2.1 in manifests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/839
* [Docs] Update Slack link by @gaocegege in https://github.com/vllm-project/aibrix/pull/841
* [Docs] Remove repeated lines by @zjd0112 in https://github.com/vllm-project/aibrix/pull/849
* Bump AIBrix version to v0.2.1 for standalone distributed inference by @SongGuyang in https://github.com/vllm-project/aibrix/pull/850
* Support OpenAI api style /v1/models response by @Jeffwan in https://github.com/vllm-project/aibrix/pull/829
* [Misc] Resolve symlink ambiguity when generating codes by @vaaandark in https://github.com/vllm-project/aibrix/pull/856
* Introduce RoutingContext in Route interface and clean up stale codes by @Jeffwan in https://github.com/vllm-project/aibrix/pull/855
* [Misc]: sync hpa status to podAutoScaler by @vie-serendipity in https://github.com/vllm-project/aibrix/pull/860
* Generate workload based on prefix sharing synthetic data by @happyandslow in https://github.com/vllm-project/aibrix/pull/840
* Fixing missing image link in #840 by @happyandslow in https://github.com/vllm-project/aibrix/pull/871
* Cite Melange paper in heterogeneous feature by @Jeffwan in https://github.com/vllm-project/aibrix/pull/872
* [Misc] support linux for vllm cpu local development by @nurali-techie in https://github.com/vllm-project/aibrix/pull/867
* Refactor make deploy to use apply instead of create by @varungup90 in https://github.com/vllm-project/aibrix/pull/793
* Use string based tokenizer in prefix cache by @varungup90 in https://github.com/vllm-project/aibrix/pull/774
* Add profiling support for gateway plugins and bug fix to close stream decoder by @varungup90 in https://github.com/vllm-project/aibrix/pull/857
* Add flag to enable/disable GPU Optimizer tracing by @varungup90 in https://github.com/vllm-project/aibrix/pull/875
* [Docs] fix typo in runtime feature page by @legendtkl in https://github.com/vllm-project/aibrix/pull/870
* chore: clean-up mock yaml by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/877
* Fixing image link error in workload generator README.md by @happyandslow in https://github.com/vllm-project/aibrix/pull/888
* Update Synthetic Load Prodefined Config for Geneerator by @happyandslow in https://github.com/vllm-project/aibrix/pull/889
* [Misc] Fix plot_workload to pass dirname to makedirs by @ronaldosaheki in https://github.com/vllm-project/aibrix/pull/886
* [Misc] Fix client.py in case workload has model null and client has default_model by @ronaldosaheki in https://github.com/vllm-project/aibrix/pull/887
* [WIP] Adding input/output distribution argument to constant load generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/882
* [Docs] Fix broken contributing guidelines link in README by @nadongjun in https://github.com/vllm-project/aibrix/pull/890
* [Bug] fix install script PATH environment variable by @cr7258 in https://github.com/vllm-project/aibrix/pull/893
* [Docs] Link to dynamic lora from docs by @thomasjpfan in https://github.com/vllm-project/aibrix/pull/883
* [API] Refactor: core cache design and impl by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/878
* Added antiaffinity in kvcache crd by @gangmuk in https://github.com/vllm-project/aibrix/pull/865
* [Docs] Fix tpm and rpm typo in gateway-plugins.rst by @runzhen in https://github.com/vllm-project/aibrix/pull/896
* [Misc] Remove unused function in pkg/utils by @my-git9 in https://github.com/vllm-project/aibrix/pull/895
* Remove model name from client and generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/894
* [Misc] Add PS benchmark manifests and scripts by @Jeffwan in https://github.com/vllm-project/aibrix/pull/899
* Add release overlays to update control plane config for production deployment by @varungup90 in https://github.com/vllm-project/aibrix/pull/900
* [Misc][Docs]: GCP and Kubernetes Terraform Deployment Modules by @jolfr in https://github.com/vllm-project/aibrix/pull/823
* [Misc] Cleanup deprecated function intstr.FromInt by @my-git9 in https://github.com/vllm-project/aibrix/pull/901
* [Bug] Routers that require cache failed on Register by @zhangjyr in https://github.com/vllm-project/aibrix/pull/913
* [Misc] chore: remove unnecessary check for pod is zero by @googs1025 in https://github.com/vllm-project/aibrix/pull/908
* [Bug] add Tolerations for kvcache pod to fix Pending and CrashLoopBackOff on GKE by @runzhen in https://github.com/vllm-project/aibrix/pull/909
* [Misc] chore(raycluster): add concurrency limit and error aggregation to scaleDown by @googs1025 in https://github.com/vllm-project/aibrix/pull/914
* [API] Cache and Router refactoring for concurrent performance, concurrent safety and stateful routing. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/884
* Enable parallel client using thread pool in benchmark client by @happyandslow in https://github.com/vllm-project/aibrix/pull/919
* [Misc] Add pods stats example: running requests. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/918
* [CLI] feature(modeladapter): make modeladapter controller scheduler policy be configured by @googs1025 in https://github.com/vllm-project/aibrix/pull/921
* [Bug] Syncmap.Store does not update. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/925
* [API] [Misc]: Support LRU cache with TTL for prefix cache indexer by @vie-serendipity in https://github.com/vllm-project/aibrix/pull/905
* Remove unused argument from workload generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/929
* [BUG] cache: handle DeletedFinalStateUnknown by the delete func by @Iceber in https://github.com/vllm-project/aibrix/pull/926
* [Misc] feature(rayclusterreplicaset): check rayclusters crd is installed before controller start by @googs1025 in https://github.com/vllm-project/aibrix/pull/922
* [BUG] return directly when error occurs while adding the controller by @Iceber in https://github.com/vllm-project/aibrix/pull/937
* [Misc] fix log typo by @Iceber in https://github.com/vllm-project/aibrix/pull/935
* Move delays to threads in benchmark by @happyandslow in https://github.com/vllm-project/aibrix/pull/939
* [BUG] controller: fix generating the corresponding HPA object for the PA by @Iceber in https://github.com/vllm-project/aibrix/pull/934
* Support multi-turn scenarios in benchmark client by @happyandslow in https://github.com/vllm-project/aibrix/pull/907
* Refactoring benchmark folder by @happyandslow in https://github.com/vllm-project/aibrix/pull/946
* Performance improvements for prefix cache routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/933
* [Misc]: move crd check in Initialize part by @googs1025 in https://github.com/vllm-project/aibrix/pull/949
* [CLI] Add —disableWebhook in controller  by @Jeffwan in https://github.com/vllm-project/aibrix/pull/931
* [BUG] controller: handle DeletedFinalStateUnknown by the delete func by @Iceber in https://github.com/vllm-project/aibrix/pull/938
* fix: complete RayClusterFleet example for multi-node vLLM inference by @ModiIntel in https://github.com/vllm-project/aibrix/pull/954
* [Misc] remove the duplicated env functions by @Iceber in https://github.com/vllm-project/aibrix/pull/953
* [Misc] increase the memory limit of the controller-manager by @Iceber in https://github.com/vllm-project/aibrix/pull/952
* chore: add help func for get Env value by @googs1025 in https://github.com/vllm-project/aibrix/pull/941
* [Bug] avoid frequent lookup of the routing strategy env by @Iceber in https://github.com/vllm-project/aibrix/pull/956
* Enable standalone installation of kv-cache-controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/930
* [fix] Fix wheel build errors in runtime image by @Jeffwan in https://github.com/vllm-project/aibrix/pull/961
* Control maximum concurrent session for workload generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/963
* Updating Plotting Script to Visualize Sharing Patterns by @happyandslow in https://github.com/vllm-project/aibrix/pull/965
* Change synthetic cache sharing dataset format by @happyandslow in https://github.com/vllm-project/aibrix/pull/966
* [Bug] prevent reference grant delete if shared by other deployments by @varungup90 in https://github.com/vllm-project/aibrix/pull/968
* Add graceful shutdown for gateway and add liveness/readiness probes by @varungup90 in https://github.com/vllm-project/aibrix/pull/962
* Add httproute status check for response header errors by @varungup90 in https://github.com/vllm-project/aibrix/pull/957
* Update envoy proxy and gateway-plugins config by @varungup90 in https://github.com/vllm-project/aibrix/pull/967
* Refactor kv cache controller to support different setup modes by @Jeffwan in https://github.com/vllm-project/aibrix/pull/971
* [Misc] chore: use t.Log instead of Println by @googs1025 in https://github.com/vllm-project/aibrix/pull/973
* [fix] Handle error output in analysis script by @happyandslow in https://github.com/vllm-project/aibrix/pull/975
* [Fix] Unify all workload generator output file names by @happyandslow in https://github.com/vllm-project/aibrix/pull/976
* [Fix] Fix shallowcopy error in prompt history retrieval by @happyandslow in https://github.com/vllm-project/aibrix/pull/978
* Assign tasks to client by keys by @happyandslow in https://github.com/vllm-project/aibrix/pull/979
* [Fix] Fix error case handling for client output analysis by @happyandslow in https://github.com/vllm-project/aibrix/pull/980
* cmd/controllers: add readyz check for the webhook by @Iceber in https://github.com/vllm-project/aibrix/pull/969
* Bug fix generating plain data format by @happyandslow in https://github.com/vllm-project/aibrix/pull/982
* [BUG] cache: start informer after adding the resource handler by @Iceber in https://github.com/vllm-project/aibrix/pull/981
* Support distributed hashing mode kv cache pool by @Jeffwan in https://github.com/vllm-project/aibrix/pull/984
* [Feature]: introducing a basic VTC router in gateway plugin to start supporting fairness based routing by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/964
* [Docs]: Fixed Broken link for tutorials by @SuperMohit in https://github.com/vllm-project/aibrix/pull/992
* End-to-end script for workload runnning process by @happyandslow in https://github.com/vllm-project/aibrix/pull/947
* Support hpkv in kv cache controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/985
* Update add redis pass for client by @weapons97 in https://github.com/vllm-project/aibrix/pull/990
* [Misc] chore: refactor selectTargetPod func by @googs1025 in https://github.com/vllm-project/aibrix/pull/1000
* [Misc] chore: remove unuse func by @googs1025 in https://github.com/vllm-project/aibrix/pull/1005
* [Misc] Move redis load_env to method level by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1002
* [Fix] 401 errors in gateway should be returned as immediate response  by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1006
* [BUG] ratelimit: fix the wrong TPM key name by @runzhen in https://github.com/vllm-project/aibrix/pull/987
* [Misc] Add app.kubernetes.io/name labels to components by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1003
* E2E CI fix to ensure all pods are ready by @varungup90 in https://github.com/vllm-project/aibrix/pull/972
* Allow manual trigger for build/push docker images by @varungup90 in https://github.com/vllm-project/aibrix/pull/1017
* [Fix] Prioritize AutoTokenizer in get_tokenizer with fallback to tiktoken by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1016
* [Bug] fix: update metaPods cache to use namespace/name as the key by @googs1025 in https://github.com/vllm-project/aibrix/pull/1015
* [Fix]: optimize vtc-basic router algo from modulo to more robust adaptive-clamped-linear by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1011
* Enabling adjustable client pool size and output token limit by @happyandslow in https://github.com/vllm-project/aibrix/pull/1025
* [Misc] fix: Optimizing Route method of the gateway algorithms by @googs1025 in https://github.com/vllm-project/aibrix/pull/1001
* [Docs] Support minikube on Lambda cloud and add AWS page by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1020
* [BUG] Use more accurate chi-squared test for randomness validation in e2e test. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1027
* Support multiple configs in synthetic shared dataset by @happyandslow in https://github.com/vllm-project/aibrix/pull/1033
* [Fix] Bug fix  for constant workload QPS by @happyandslow in https://github.com/vllm-project/aibrix/pull/1036
* Improve installlation test e2e time by @varungup90 in https://github.com/vllm-project/aibrix/pull/1034
* Add Pareto Sampler for Multiturn Dataset Generation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1038
* use atomic.Int32c instead of use Int32 type by @googs1025 in https://github.com/vllm-project/aibrix/pull/1035
* [CI] Enable GHCR image build and push by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1041
* Adding interval scaling factor for client by @happyandslow in https://github.com/vllm-project/aibrix/pull/1043
* [Bug] fix: use RLock() instead of Lock() when reading var by @googs1025 in https://github.com/vllm-project/aibrix/pull/1044
* Dataset generator output argument fix by @happyandslow in https://github.com/vllm-project/aibrix/pull/1042
* Docker push multi-platform images by @varungup90 in https://github.com/vllm-project/aibrix/pull/1026
* Refactor the kvcache backend to support infinistore by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1037
* [Docs] Document gpu optimizer as experimental and improve deployment config. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1051
* [Fix] Removing redundant locks in prefix cache and load router function by @gangmuk in https://github.com/vllm-project/aibrix/pull/1024
* [Feature] AIBrix KVCache common by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1057
* [Feature] AIBrix KVCache L1Cache by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1061
* [Feature] AIBrix KVCache L2Cache Part1 by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1062
* Add dashboard and monitoring setup steps for control plane by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1048
* [Feature] AIBrix KVCache L2Cache Part2 by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1063
* [Feature] AIBrix KVCache L2Cache Part3 and KVCache Managers by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1064
* [Bug] fix: add more info for pod metric fetch failures in GetMetricsFromPods by @googs1025 in https://github.com/vllm-project/aibrix/pull/1039
* [Fix] Fix multiple issues for benchmark implementation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1049
* [Fix] Fix L2Cache's register descriptor container by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1068
* Update kvcache v1alpha1 api spec by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1055
* [Integration] vLLM integration patch for AIBrix KVCache by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1069
* [Misc] fix: add miss Close() for redis client by @googs1025 in https://github.com/vllm-project/aibrix/pull/1056
* Support prometheus metrics in kv watcher pod by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1073
* Add rdma gid search scripts by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1072
* Support watcher pod rbac in kvcache controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1071
* [Misc] chore: change Scheduler interface describe in modeladapter controller by @googs1025 in https://github.com/vllm-project/aibrix/pull/1075
* [MISC]: add vtc_bucket_size_active metric gauge for vtc-basic  by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1065
* [Integration] Update vLLM integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1080
* [Misc] Clean up deployment scripts for volcengine by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1081
* Cut v0.3.0-rc.1 release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1083
* [fix] Correct the python build path in same step by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1084
* [Misc] Skip attaching python artifacts to github release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1085

## New Contributors
* @gaocegege made their first contribution in https://github.com/vllm-project/aibrix/pull/731
* @eltociear made their first contribution in https://github.com/vllm-project/aibrix/pull/736
* @terrytangyuan made their first contribution in https://github.com/vllm-project/aibrix/pull/746
* @jolfr made their first contribution in https://github.com/vllm-project/aibrix/pull/744
* @Abirdcfly made their first contribution in https://github.com/vllm-project/aibrix/pull/763
* @pierDipi made their first contribution in https://github.com/vllm-project/aibrix/pull/764
* @Xunzhuo made their first contribution in https://github.com/vllm-project/aibrix/pull/810
* @zjd0112 made their first contribution in https://github.com/vllm-project/aibrix/pull/849
* @SongGuyang made their first contribution in https://github.com/vllm-project/aibrix/pull/850
* @vaaandark made their first contribution in https://github.com/vllm-project/aibrix/pull/856
* @vie-serendipity made their first contribution in https://github.com/vllm-project/aibrix/pull/860
* @nurali-techie made their first contribution in https://github.com/vllm-project/aibrix/pull/867
* @legendtkl made their first contribution in https://github.com/vllm-project/aibrix/pull/870
* @ronaldosaheki made their first contribution in https://github.com/vllm-project/aibrix/pull/886
* @nadongjun made their first contribution in https://github.com/vllm-project/aibrix/pull/890
* @cr7258 made their first contribution in https://github.com/vllm-project/aibrix/pull/893
* @thomasjpfan made their first contribution in https://github.com/vllm-project/aibrix/pull/883
* @runzhen made their first contribution in https://github.com/vllm-project/aibrix/pull/896
* @my-git9 made their first contribution in https://github.com/vllm-project/aibrix/pull/895
* @googs1025 made their first contribution in https://github.com/vllm-project/aibrix/pull/908
* @Iceber made their first contribution in https://github.com/vllm-project/aibrix/pull/926
* @ModiIntel made their first contribution in https://github.com/vllm-project/aibrix/pull/954
* @Venkat2811 made their first contribution in https://github.com/vllm-project/aibrix/pull/964
* @SuperMohit made their first contribution in https://github.com/vllm-project/aibrix/pull/992
* @weapons97 made their first contribution in https://github.com/vllm-project/aibrix/pull/990

**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.2.0...v0.3.0-rc.1

## v0.3.0-rc.2 (2025-05-21)

Automatically generated release for tag v0.3.0-rc.2.

## What's Changed
* [Bug] fix: condition nil panic in FindStatusCondition func by @googs1025 in https://github.com/vllm-project/aibrix/pull/1078
* Refactor request body processing and add multi-turn conversation support by @varungup90 in https://github.com/vllm-project/aibrix/pull/1067
* Upload arm build images with git.ref_name by @varungup90 in https://github.com/vllm-project/aibrix/pull/1090
* Update documentation and add openai sdk samples by @varungup90 in https://github.com/vllm-project/aibrix/pull/1092
* Rename preble based prefix routing strategy by @varungup90 in https://github.com/vllm-project/aibrix/pull/1104
* Add v0.3.0 ps performance regression test scenario by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1099
* Migrating benchmark entrypoints to python client by @happyandslow in https://github.com/vllm-project/aibrix/pull/1066
* [Misc] Add demo manifests for volcano engine by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1105
* [Integration] KVCache: update vLLM integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1107
* [Bug]fix: add scale subresource to rayclusterfleet by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1082
* [Feature] KVCache: Suppport InfiniStore GID and enhance cluster mode by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1106
* [Chore] fix: regenerate crd by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1109
* [Chore] KVCache: enhance format and dependencies by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1108
* Polish benchmark manifests and VE samples by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1113
* [API] Support customized template for cache by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1114
* Bump version to v0.3.0-rc.2 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1115
* [Fix] Move pdb from patch to resources by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1117

## New Contributors
* @zhixian82 made their first contribution in https://github.com/vllm-project/aibrix/pull/1082

**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.3.0-rc.1...v0.3.0-rc.2

## v0.3.0 (2025-05-21)

Automatically generated release for tag v0.3.0.

## 🚀 New Features Highlights
- **AIBrix KVCache Offloading Framework**: Introduces a pluggable multi-tier KVCache architecture with support for DRAM and remote backends, enabling efficient offloading of KV states to reduce GPU memory pressure and increase deployment density. (#1057, #1061, #1062, #1063, #1064, #1068, #1069, #1080, #1107)
- **New KVCache orchestration API**: Refactors the orchestration layer to support distributed hashing based caching solutions. (#971, #984, #985, #1037, #1055, #1071, #1114)
- **Prefix Cache and Load aware Routing**: Uses hash token-based prefix matching and load awareness to reduce latency by increasing prefix cache hit rate and routing efficiency (#838, #774, #933, #1067)
- **Preble Routing (ICLR’25)**: An implementation of Preble, it balances KV cache reuse and GPU load by comparing prefix lengths and computing prompt-aware cost scores for optimal routing. (#678, #719, #730, #1024)
- **Fairness-oriented Routing (OSDI’24 VTC)**: Introduces the vtc-basic router with Windowed Adaptive Fairness Routing, which dynamically tracks token usage and ensures fair load distribution across pods. (#964, #1011, #1065)

## 📊 Feature Enhancements
### Gateway Enhancements
- Support for OpenAI-compatible APIs, including streaming responses, usage reporting, asynchronous handling, and standardized error responses for seamless end-to-end integration. (#703, #788, #799)
- Introduced the /v1/models endpoint for compatibility with OpenAI-style API clients. (#802)
- Refactored gateway-plugins with an extensible ext-proc server architecture, laying the foundation for pluggable policies. (#810)
- Improved concurrency safety and routing stability through major cache and router redesigns (#878, #884)

### Control Plane:
- Added Kubernetes webhook validation for CRDs, providing early error feedback during resource creation (#748, #786).
- Improve RayClusterFleet to fully support Deepseek-r1/v3 models (#789, #826, #835, #914, #954).
- Add scale subresource in RayClusterFleet CRD and enable HPA support (#1082, #1109)

### Installation Experiences:
- Introduced Terraform modules for GCP and Kubernetes deployment (#823).
- Added setup guides for Minikube on Lambda Cloud and AWS in the documentation (#1020).
- Enabled standalone controller installation for simplified system bootstrapping.(#930, #931)
- Streamlined upgrade workflows by introducing kubectl apply support. CRDs are now split and applied with --server-side, avoiding annotation size limits and enabling smooth incremental updates. (#793)
- Enabled container image publishing to Github Container Registry (GHCR) (#1041).
- Support ARM container Images (#1090)

### Observability & Stability:
- Shipped prebuilt Grafana dashboards covering control plane, gateway, and KV cache components for out-of-the-box observability. (#1048)
- Tuned Envoy proxy memory and buffer configurations for better performance under high concurrency. (#825)
- Tuned Envoy proxy configurations for memory and buffer management under high concurrency (#967).
- Added graceful shutdown, liveness, and readiness probes to improve service resilience (#962).
- Delivered production-ready monitoring setups for all major system components (#1048).

## New Contributors

* @gaocegege made their first contribution in https://github.com/vllm-project/aibrix/pull/731
* @eltociear made their first contribution in https://github.com/vllm-project/aibrix/pull/736
* @terrytangyuan made their first contribution in https://github.com/vllm-project/aibrix/pull/746
* @jolfr made their first contribution in https://github.com/vllm-project/aibrix/pull/744
* @Abirdcfly made their first contribution in https://github.com/vllm-project/aibrix/pull/763
* @pierDipi made their first contribution in https://github.com/vllm-project/aibrix/pull/764
* @Xunzhuo made their first contribution in https://github.com/vllm-project/aibrix/pull/810
* @zjd0112 made their first contribution in https://github.com/vllm-project/aibrix/pull/849
* @SongGuyang made their first contribution in https://github.com/vllm-project/aibrix/pull/850
* @vaaandark made their first contribution in https://github.com/vllm-project/aibrix/pull/856
* @vie-serendipity made their first contribution in https://github.com/vllm-project/aibrix/pull/860
* @nurali-techie made their first contribution in https://github.com/vllm-project/aibrix/pull/867
* @legendtkl made their first contribution in https://github.com/vllm-project/aibrix/pull/870
* @ronaldosaheki made their first contribution in https://github.com/vllm-project/aibrix/pull/886
* @nadongjun made their first contribution in https://github.com/vllm-project/aibrix/pull/890
* @cr7258 made their first contribution in https://github.com/vllm-project/aibrix/pull/893
* @thomasjpfan made their first contribution in https://github.com/vllm-project/aibrix/pull/883
* @runzhen made their first contribution in https://github.com/vllm-project/aibrix/pull/896
* @my-git9 made their first contribution in https://github.com/vllm-project/aibrix/pull/895
* @googs1025 made their first contribution in https://github.com/vllm-project/aibrix/pull/908
* @Iceber made their first contribution in https://github.com/vllm-project/aibrix/pull/926
* @ModiIntel made their first contribution in https://github.com/vllm-project/aibrix/pull/954
* @Venkat2811 made their first contribution in https://github.com/vllm-project/aibrix/pull/964
* @SuperMohit made their first contribution in https://github.com/vllm-project/aibrix/pull/992
* @weapons97 made their first contribution in https://github.com/vllm-project/aibrix/pull/990
* @zhixian82 made their first contribution in https://github.com/vllm-project/aibrix/pull/1082

## What's Changed

**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.2.0...v0.3.0

* [Docs] fix format of the dist kv cache doc by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/714
* complete the 'make generate' command by @kerthcet in https://github.com/vllm-project/aibrix/pull/711
* Update organization reference in code base by @Jeffwan in https://github.com/vllm-project/aibrix/pull/717
* [Misc] Update the documentation link by @Jeffwan in https://github.com/vllm-project/aibrix/pull/720
* Initial implementation of radix tree-based cache by @gangmuk in https://github.com/vllm-project/aibrix/pull/678
* Add model adapter e2e tests by @varungup90 in https://github.com/vllm-project/aibrix/pull/701
* Add vllm cpu alternative for local development by @varungup90 in https://github.com/vllm-project/aibrix/pull/721
* Add white paper file by @Jeffwan in https://github.com/vllm-project/aibrix/pull/724
* Adding streaming client for AIbrix experiments by @happyandslow in https://github.com/vllm-project/aibrix/pull/676
* [Docs] Update Readme with new links and blog post, and update white paper by @xieus in https://github.com/vllm-project/aibrix/pull/725
* Recording failed requests in benchmark client by @gangmuk in https://github.com/vllm-project/aibrix/pull/727
* Process response headers in gateway by @varungup90 in https://github.com/vllm-project/aibrix/pull/703
* [misc] Fix white paper link by @Jeffwan in https://github.com/vllm-project/aibrix/pull/728
* Prefix and load aware routing with radix tree kv cache by @gangmuk in https://github.com/vllm-project/aibrix/pull/719
* Fix slack link in README.md by @Jeffwan in https://github.com/vllm-project/aibrix/pull/729
* [readme] Fix wrong link by @gaocegege in https://github.com/vllm-project/aibrix/pull/731
* [Misc] update scheduler.py by @eltociear in https://github.com/vllm-project/aibrix/pull/736
* Improve thread safety for TreeNode data structure and refactor related codes by @gangmuk in https://github.com/vllm-project/aibrix/pull/730
* Fix CacheSpec api scheme by @kerthcet in https://github.com/vllm-project/aibrix/pull/740
* docs: Fix link to license by @terrytangyuan in https://github.com/vllm-project/aibrix/pull/746
* Use native codegen cmd generating client-go by @kerthcet in https://github.com/vllm-project/aibrix/pull/741
* [Docs]: Fixed kubectl commands for install of components by @jolfr in https://github.com/vllm-project/aibrix/pull/744
* [fix] fixing bug in using AsyncOpenAI client (header setting, token counting, etc) by @gangmuk in https://github.com/vllm-project/aibrix/pull/738
* Add webhook framework by @kerthcet in https://github.com/vllm-project/aibrix/pull/748
* Use random seed for xxhash by @varungup90 in https://github.com/vllm-project/aibrix/pull/752
* Create SECURITY.md to enable security policy by @xieus in https://github.com/vllm-project/aibrix/pull/756
* [CI] Add integration test  by @kerthcet in https://github.com/vllm-project/aibrix/pull/759
* [Bug] fix: correct non-inherited context by @Abirdcfly in https://github.com/vllm-project/aibrix/pull/763
* [Misc] Parametrize Makefile for mocked vLLM apps by @pierDipi in https://github.com/vllm-project/aibrix/pull/764
* Support benchmarking script by using real application trace by @nwangfw in https://github.com/vllm-project/aibrix/pull/737
* Maintaining common benchmarks utils in a separate dir by @gangmuk in https://github.com/vllm-project/aibrix/pull/770
* Ignore worker pods for gateway routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/776
* Disable ENABLE_PROBES_INJECTION in correct way by @Jeffwan in https://github.com/vllm-project/aibrix/pull/779
* Make stream include usage as optional by @varungup90 in https://github.com/vllm-project/aibrix/pull/788
* Append ray head label selector in PodAutoscaler by @Jeffwan in https://github.com/vllm-project/aibrix/pull/789
* Remove redundant install crds in makefile by @varungup90 in https://github.com/vllm-project/aibrix/pull/792
* Update request message processing for /v1/completion input by @varungup90 in https://github.com/vllm-project/aibrix/pull/794
* Added target pod to client result and made clients consistent by @gangmuk in https://github.com/vllm-project/aibrix/pull/799
* Enable CI tests for release branch by @Jeffwan in https://github.com/vllm-project/aibrix/pull/805
* Move modelAdapter runtime validation to webhook by @kerthcet in https://github.com/vllm-project/aibrix/pull/786
* [Misc] Adding model field to each request by @happyandslow in https://github.com/vllm-project/aibrix/pull/812
* [Refactor]: gateway-plugins ext-proc server codebase by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/810
* [CI]: update release tags pattern by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/815
* [Docs]: fix vllm mock app Unauthorized response by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/817
* Reconfigure workload generator for predefined synthetic patterns by @happyandslow in https://github.com/vllm-project/aibrix/pull/771
* Workload generation scripts for prefix aware routing by @gangmuk in https://github.com/vllm-project/aibrix/pull/820
* Fix the paths in lambda cloud doc by @gangmuk in https://github.com/vllm-project/aibrix/pull/824
* [Bug] Added Startup Probe in Quickstart Model by @jolfr in https://github.com/vllm-project/aibrix/pull/773
* Add /v1/models endpoint to gateway by @varungup90 in https://github.com/vllm-project/aibrix/pull/802
* Increase envoy proxy memory config and client connection buffersize by @varungup90 in https://github.com/vllm-project/aibrix/pull/825
* Support to create default HttpRoute for RayClusterFleet by @Jeffwan in https://github.com/vllm-project/aibrix/pull/826
* [Misc] Fix CI issue on release branch and clean up logs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/837
* Fix repeated initialization of gateway routers and add unit test for prefix cache by @varungup90 in https://github.com/vllm-project/aibrix/pull/838
* Add deepseek-r1 671B deployment sample and docs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/835
* Bump AIBrix version to v0.2.1 in manifests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/839
* [Docs] Update Slack link by @gaocegege in https://github.com/vllm-project/aibrix/pull/841
* [Docs] Remove repeated lines by @zjd0112 in https://github.com/vllm-project/aibrix/pull/849
* Bump AIBrix version to v0.2.1 for standalone distributed inference by @SongGuyang in https://github.com/vllm-project/aibrix/pull/850
* Support OpenAI api style /v1/models response by @Jeffwan in https://github.com/vllm-project/aibrix/pull/829
* [Misc] Resolve symlink ambiguity when generating codes by @vaaandark in https://github.com/vllm-project/aibrix/pull/856
* Introduce RoutingContext in Route interface and clean up stale codes by @Jeffwan in https://github.com/vllm-project/aibrix/pull/855
* [Misc]: sync hpa status to podAutoScaler by @vie-serendipity in https://github.com/vllm-project/aibrix/pull/860
* Generate workload based on prefix sharing synthetic data by @happyandslow in https://github.com/vllm-project/aibrix/pull/840
* Fixing missing image link in #840 by @happyandslow in https://github.com/vllm-project/aibrix/pull/871
* Cite Melange paper in heterogeneous feature by @Jeffwan in https://github.com/vllm-project/aibrix/pull/872
* [Misc] support linux for vllm cpu local development by @nurali-techie in https://github.com/vllm-project/aibrix/pull/867
* Refactor make deploy to use apply instead of create by @varungup90 in https://github.com/vllm-project/aibrix/pull/793
* Use string based tokenizer in prefix cache by @varungup90 in https://github.com/vllm-project/aibrix/pull/774
* Add profiling support for gateway plugins and bug fix to close stream decoder by @varungup90 in https://github.com/vllm-project/aibrix/pull/857
* Add flag to enable/disable GPU Optimizer tracing by @varungup90 in https://github.com/vllm-project/aibrix/pull/875
* [Docs] fix typo in runtime feature page by @legendtkl in https://github.com/vllm-project/aibrix/pull/870
* chore: clean-up mock yaml by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/877
* Fixing image link error in workload generator README.md by @happyandslow in https://github.com/vllm-project/aibrix/pull/888
* Update Synthetic Load Prodefined Config for Geneerator by @happyandslow in https://github.com/vllm-project/aibrix/pull/889
* [Misc] Fix plot_workload to pass dirname to makedirs by @ronaldosaheki in https://github.com/vllm-project/aibrix/pull/886
* [Misc] Fix client.py in case workload has model null and client has default_model by @ronaldosaheki in https://github.com/vllm-project/aibrix/pull/887
* [WIP] Adding input/output distribution argument to constant load generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/882
* [Docs] Fix broken contributing guidelines link in README by @nadongjun in https://github.com/vllm-project/aibrix/pull/890
* [Bug] fix install script PATH environment variable by @cr7258 in https://github.com/vllm-project/aibrix/pull/893
* [Docs] Link to dynamic lora from docs by @thomasjpfan in https://github.com/vllm-project/aibrix/pull/883
* [API] Refactor: core cache design and impl by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/878
* Added antiaffinity in kvcache crd by @gangmuk in https://github.com/vllm-project/aibrix/pull/865
* [Docs] Fix tpm and rpm typo in gateway-plugins.rst by @runzhen in https://github.com/vllm-project/aibrix/pull/896
* [Misc] Remove unused function in pkg/utils by @my-git9 in https://github.com/vllm-project/aibrix/pull/895
* Remove model name from client and generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/894
* [Misc] Add PS benchmark manifests and scripts by @Jeffwan in https://github.com/vllm-project/aibrix/pull/899
* Add release overlays to update control plane config for production deployment by @varungup90 in https://github.com/vllm-project/aibrix/pull/900
* [Misc][Docs]: GCP and Kubernetes Terraform Deployment Modules by @jolfr in https://github.com/vllm-project/aibrix/pull/823
* [Misc] Cleanup deprecated function intstr.FromInt by @my-git9 in https://github.com/vllm-project/aibrix/pull/901
* [Bug] Routers that require cache failed on Register by @zhangjyr in https://github.com/vllm-project/aibrix/pull/913
* [Misc] chore: remove unnecessary check for pod is zero by @googs1025 in https://github.com/vllm-project/aibrix/pull/908
* [Bug] add Tolerations for kvcache pod to fix Pending and CrashLoopBackOff on GKE by @runzhen in https://github.com/vllm-project/aibrix/pull/909
* [Misc] chore(raycluster): add concurrency limit and error aggregation to scaleDown by @googs1025 in https://github.com/vllm-project/aibrix/pull/914
* [API] Cache and Router refactoring for concurrent performance, concurrent safety and stateful routing. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/884
* Enable parallel client using thread pool in benchmark client by @happyandslow in https://github.com/vllm-project/aibrix/pull/919
* [Misc] Add pods stats example: running requests. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/918
* [CLI] feature(modeladapter): make modeladapter controller scheduler policy be configured by @googs1025 in https://github.com/vllm-project/aibrix/pull/921
* [Bug] Syncmap.Store does not update. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/925
* [API] [Misc]: Support LRU cache with TTL for prefix cache indexer by @vie-serendipity in https://github.com/vllm-project/aibrix/pull/905
* Remove unused argument from workload generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/929
* [BUG] cache: handle DeletedFinalStateUnknown by the delete func by @Iceber in https://github.com/vllm-project/aibrix/pull/926
* [Misc] feature(rayclusterreplicaset): check rayclusters crd is installed before controller start by @googs1025 in https://github.com/vllm-project/aibrix/pull/922
* [BUG] return directly when error occurs while adding the controller by @Iceber in https://github.com/vllm-project/aibrix/pull/937
* [Misc] fix log typo by @Iceber in https://github.com/vllm-project/aibrix/pull/935
* Move delays to threads in benchmark by @happyandslow in https://github.com/vllm-project/aibrix/pull/939
* [BUG] controller: fix generating the corresponding HPA object for the PA by @Iceber in https://github.com/vllm-project/aibrix/pull/934
* Support multi-turn scenarios in benchmark client by @happyandslow in https://github.com/vllm-project/aibrix/pull/907
* Refactoring benchmark folder by @happyandslow in https://github.com/vllm-project/aibrix/pull/946
* Performance improvements for prefix cache routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/933
* [Misc]: move crd check in Initialize part by @googs1025 in https://github.com/vllm-project/aibrix/pull/949
* [CLI] Add —disableWebhook in controller  by @Jeffwan in https://github.com/vllm-project/aibrix/pull/931
* [BUG] controller: handle DeletedFinalStateUnknown by the delete func by @Iceber in https://github.com/vllm-project/aibrix/pull/938
* fix: complete RayClusterFleet example for multi-node vLLM inference by @ModiIntel in https://github.com/vllm-project/aibrix/pull/954
* [Misc] remove the duplicated env functions by @Iceber in https://github.com/vllm-project/aibrix/pull/953
* [Misc] increase the memory limit of the controller-manager by @Iceber in https://github.com/vllm-project/aibrix/pull/952
* chore: add help func for get Env value by @googs1025 in https://github.com/vllm-project/aibrix/pull/941
* [Bug] avoid frequent lookup of the routing strategy env by @Iceber in https://github.com/vllm-project/aibrix/pull/956
* Enable standalone installation of kv-cache-controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/930
* [fix] Fix wheel build errors in runtime image by @Jeffwan in https://github.com/vllm-project/aibrix/pull/961
* Control maximum concurrent session for workload generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/963
* Updating Plotting Script to Visualize Sharing Patterns by @happyandslow in https://github.com/vllm-project/aibrix/pull/965
* Change synthetic cache sharing dataset format by @happyandslow in https://github.com/vllm-project/aibrix/pull/966
* [Bug] prevent reference grant delete if shared by other deployments by @varungup90 in https://github.com/vllm-project/aibrix/pull/968
* Add graceful shutdown for gateway and add liveness/readiness probes by @varungup90 in https://github.com/vllm-project/aibrix/pull/962
* Add httproute status check for response header errors by @varungup90 in https://github.com/vllm-project/aibrix/pull/957
* Update envoy proxy and gateway-plugins config by @varungup90 in https://github.com/vllm-project/aibrix/pull/967
* Refactor kv cache controller to support different setup modes by @Jeffwan in https://github.com/vllm-project/aibrix/pull/971
* [Misc] chore: use t.Log instead of Println by @googs1025 in https://github.com/vllm-project/aibrix/pull/973
* [fix] Handle error output in analysis script by @happyandslow in https://github.com/vllm-project/aibrix/pull/975
* [Fix] Unify all workload generator output file names by @happyandslow in https://github.com/vllm-project/aibrix/pull/976
* [Fix] Fix shallowcopy error in prompt history retrieval by @happyandslow in https://github.com/vllm-project/aibrix/pull/978
* Assign tasks to client by keys by @happyandslow in https://github.com/vllm-project/aibrix/pull/979
* [Fix] Fix error case handling for client output analysis by @happyandslow in https://github.com/vllm-project/aibrix/pull/980
* cmd/controllers: add readyz check for the webhook by @Iceber in https://github.com/vllm-project/aibrix/pull/969
* Bug fix generating plain data format by @happyandslow in https://github.com/vllm-project/aibrix/pull/982
* [BUG] cache: start informer after adding the resource handler by @Iceber in https://github.com/vllm-project/aibrix/pull/981
* Support distributed hashing mode kv cache pool by @Jeffwan in https://github.com/vllm-project/aibrix/pull/984
* [Feature]: introducing a basic VTC router in gateway plugin to start supporting fairness based routing by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/964
* [Docs]: Fixed Broken link for tutorials by @SuperMohit in https://github.com/vllm-project/aibrix/pull/992
* End-to-end script for workload runnning process by @happyandslow in https://github.com/vllm-project/aibrix/pull/947
* Support hpkv in kv cache controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/985
* Update add redis pass for client by @weapons97 in https://github.com/vllm-project/aibrix/pull/990
* [Misc] chore: refactor selectTargetPod func by @googs1025 in https://github.com/vllm-project/aibrix/pull/1000
* [Misc] chore: remove unuse func by @googs1025 in https://github.com/vllm-project/aibrix/pull/1005
* [Misc] Move redis load_env to method level by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1002
* [Fix] 401 errors in gateway should be returned as immediate response  by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1006
* [BUG] ratelimit: fix the wrong TPM key name by @runzhen in https://github.com/vllm-project/aibrix/pull/987
* [Misc] Add app.kubernetes.io/name labels to components by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1003
* E2E CI fix to ensure all pods are ready by @varungup90 in https://github.com/vllm-project/aibrix/pull/972
* Allow manual trigger for build/push docker images by @varungup90 in https://github.com/vllm-project/aibrix/pull/1017
* [Fix] Prioritize AutoTokenizer in get_tokenizer with fallback to tiktoken by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1016
* [Bug] fix: update metaPods cache to use namespace/name as the key by @googs1025 in https://github.com/vllm-project/aibrix/pull/1015
* [Fix]: optimize vtc-basic router algo from modulo to more robust adaptive-clamped-linear by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1011
* Enabling adjustable client pool size and output token limit by @happyandslow in https://github.com/vllm-project/aibrix/pull/1025
* [Misc] fix: Optimizing Route method of the gateway algorithms by @googs1025 in https://github.com/vllm-project/aibrix/pull/1001
* [Docs] Support minikube on Lambda cloud and add AWS page by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1020
* [BUG] Use more accurate chi-squared test for randomness validation in e2e test. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1027
* Support multiple configs in synthetic shared dataset by @happyandslow in https://github.com/vllm-project/aibrix/pull/1033
* [Fix] Bug fix  for constant workload QPS by @happyandslow in https://github.com/vllm-project/aibrix/pull/1036
* Improve installlation test e2e time by @varungup90 in https://github.com/vllm-project/aibrix/pull/1034
* Add Pareto Sampler for Multiturn Dataset Generation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1038
* use atomic.Int32c instead of use Int32 type by @googs1025 in https://github.com/vllm-project/aibrix/pull/1035
* [CI] Enable GHCR image build and push by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1041
* Adding interval scaling factor for client by @happyandslow in https://github.com/vllm-project/aibrix/pull/1043
* [Bug] fix: use RLock() instead of Lock() when reading var by @googs1025 in https://github.com/vllm-project/aibrix/pull/1044
* Dataset generator output argument fix by @happyandslow in https://github.com/vllm-project/aibrix/pull/1042
* Docker push multi-platform images by @varungup90 in https://github.com/vllm-project/aibrix/pull/1026
* Refactor the kvcache backend to support infinistore by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1037
* [Docs] Document gpu optimizer as experimental and improve deployment config. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1051
* [Fix] Removing redundant locks in prefix cache and load router function by @gangmuk in https://github.com/vllm-project/aibrix/pull/1024
* [Feature] AIBrix KVCache common by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1057
* [Feature] AIBrix KVCache L1Cache by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1061
* [Feature] AIBrix KVCache L2Cache Part1 by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1062
* Add dashboard and monitoring setup steps for control plane by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1048
* [Feature] AIBrix KVCache L2Cache Part2 by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1063
* [Feature] AIBrix KVCache L2Cache Part3 and KVCache Managers by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1064
* [Bug] fix: add more info for pod metric fetch failures in GetMetricsFromPods by @googs1025 in https://github.com/vllm-project/aibrix/pull/1039
* [Fix] Fix multiple issues for benchmark implementation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1049
* [Fix] Fix L2Cache's register descriptor container by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1068
* Update kvcache v1alpha1 api spec by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1055
* [Integration] vLLM integration patch for AIBrix KVCache by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1069
* [Misc] fix: add miss Close() for redis client by @googs1025 in https://github.com/vllm-project/aibrix/pull/1056
* Support prometheus metrics in kv watcher pod by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1073
* Add rdma gid search scripts by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1072
* Support watcher pod rbac in kvcache controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1071
* [Misc] chore: change Scheduler interface describe in modeladapter controller by @googs1025 in https://github.com/vllm-project/aibrix/pull/1075
* [MISC]: add vtc_bucket_size_active metric gauge for vtc-basic  by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1065
* [Integration] Update vLLM integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1080
* [Misc] Clean up deployment scripts for volcengine by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1081
* Cut v0.3.0-rc.1 release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1083
* [fix] Correct the python build path in same step by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1084
* [Misc] Skip attaching python artifacts to github release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1085
* [Bug] fix: condition nil panic in FindStatusCondition func by @googs1025 in https://github.com/vllm-project/aibrix/pull/1078
* Refactor request body processing and add multi-turn conversation support by @varungup90 in https://github.com/vllm-project/aibrix/pull/1067
* Upload arm build images with git.ref_name by @varungup90 in https://github.com/vllm-project/aibrix/pull/1090
* Update documentation and add openai sdk samples by @varungup90 in https://github.com/vllm-project/aibrix/pull/1092
* Rename preble based prefix routing strategy by @varungup90 in https://github.com/vllm-project/aibrix/pull/1104
* Add v0.3.0 ps performance regression test scenario by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1099
* Migrating benchmark entrypoints to python client by @happyandslow in https://github.com/vllm-project/aibrix/pull/1066
* [Misc] Add demo manifests for volcano engine by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1105
* [Integration] KVCache: update vLLM integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1107
* [Bug]fix: add scale subresource to rayclusterfleet by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1082
* [Feature] KVCache: Suppport InfiniStore GID and enhance cluster mode by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1106
* [Chore] fix: regenerate crd by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1109
* [Chore] KVCache: enhance format and dependencies by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1108
* Polish benchmark manifests and VE samples by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1113
* [API] Support customized template for cache by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1114
* Bump version to v0.3.0-rc.2 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1115
* [Fix] Move pdb from patch to resources by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1117
* [Docs] Add feature manuals for KVCache by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1119
* [Docs] Adding benchmark doc by @happyandslow in https://github.com/vllm-project/aibrix/pull/999
* [Docs] format KVCache docs to eliminate warnings by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1122
* Update multi-arch image push to include all platforms for release by @varungup90 in https://github.com/vllm-project/aibrix/pull/1124
* [Docs] Init folder for KVCache benchmark scenario by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1125
* [Docs] Addressing benchmark doc comments by @happyandslow in https://github.com/vllm-project/aibrix/pull/1123
* Cut v0.3.0 release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1126
* Bump python project version to v0.3.0 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1127


## v0.4.0 (2025-08-05)

## 🚀  New Features Highlights
- **Prefill/Decode (P/D) Disaggregation Support**: Introduces StormService and RoleSet CRDs to enable fine-grained orchestration of P/D roles, along with routing to unlock disaggregated inference at scale. (#1209, #1226, #1229, #1256, #1258, #1259, #1268, #1280, #1309, #1311, #1354, #1355, #1377, #1399, #1402)
- **KVCache V1 Connector Optimizations**: Delivers a major refactor with v1 Connector integration, CUDA kernel separation from vllm downstream, compact memory layout, connector integration for PrisDB and InfiniStore(/w TCP), tunable block sizes, RDMA auto-detection support and few performance optimizations to boost throughput and deployment density. ( #1174, #1194, #1247, #1274, #1276, #1278, #1286, #1287, #1288, #1295, #1303, #1312, #1318)
- **KV Event Synchronization**: Introduces remote tokenizer support to ensure tokenization consistency between client and server and implements a comprehensive KV cache event synchronization system that shares KV cache state between vLLM instances and aibrix gateway for improved prefix caching efficiency  (#1307, #1328, #1349, #1362) 
- **Multi-Engine Deployment Support**: Adds unified regression test suites and Helm values to support heterogeneous backends including vLLM, SGLang, and Dynamo, enabling flexible model deployment across engines. (#1293, #1319, #1322, #1341, #1346)

## 📊 Feature Enhancements

### 🌐 Gateway Enhancements
- SLO-aware router with profile support (#1192, #1305, #1368) 
- Adds custom inference port and metrics port support (#1140, #1313).
-  Make httproute timeout configurable and checks missing httproute before request start(#1212, #1344).
- Adds metrics server support and adds ready-to-use sample dashboard (#1211).

### ☁️ Control Plane Improvements
- Enhance the CRD existence check and improve webhook support (#1170, #1187).
- Ensure cache sync before starting controller reconcile and resync object on component restarts (#1146, #1219).
- Use worker pool management for periodic metrics update (#1096) 

### 📦 Installation & Tooling & CI
- Adds Helm Chart support with helm standard labels and probes (#1323, #1331, #1343).
- Supports multi-arch (AMD, ARM) Docker builds and refactors release pipelines (#1315, #1317, #1324, #1325).
- Improves kind development workflow and supports port-forward via Makefile, support override IMAGE_TAG and disable docker push workflow in forked repo(#1210, #1274, #1301).

## 🐞 Bug Fixes
- Fixes incorrect request count, out-of-index errors, and race conditions in AIBrix router(#1246, #1262, #1305).
- Fix Prefix cache chained hashing issue and optimize to O(N) via block-hash. (#1218, #1262)
- Fixes completion body parsing and complex content bugs (#1145, #1160).
- Fixes legacy autoscaling annotation misconfigurations (#1173).
- Fixes image replacement issues in Kustomize (#1165).
- Fixes e2e test flakiness with wait.PollUntilContextTimeout (#1214).
- Add read lock for h.histogram (#1147)

## 📚 Documentation Updates
- Adds v0.4.0 new features documentation including P/D disaggregation, multi-engine, KVCache Offloading and SLO routing documentation (#1279, #1285, #1341, #1356, #1368).
- Fixes broken links, typos, and dashboard URLs (#1190, #1193, #1237, #1270, #1271).
- Refactors component design docs into structured architecture folders (#1224, #1236, #1250).
- Refactors local development and quickstart guides (#1193, #1339, #1172).
- Improve installation commands and add more deployment examples  (#1128, #1136, #1230, #1379, #1395)

## New Contributors
* @dittops made their first contribution in https://github.com/vllm-project/aibrix/pull/1128
* @yyzxw made their first contribution in https://github.com/vllm-project/aibrix/pull/1139
* @firebook made their first contribution in https://github.com/vllm-project/aibrix/pull/1145
* @windsonsea made their first contribution in https://github.com/vllm-project/aibrix/pull/1150
* @emmanuel-ferdman made their first contribution in https://github.com/vllm-project/aibrix/pull/1161
* @MondayCha made their first contribution in https://github.com/vllm-project/aibrix/pull/1165
* @learner0810 made their first contribution in https://github.com/vllm-project/aibrix/pull/1170
* @jiahuipaung made their first contribution in https://github.com/vllm-project/aibrix/pull/1172
* @didier-durand made their first contribution in https://github.com/vllm-project/aibrix/pull/1190
* @gcalmettes made their first contribution in https://github.com/vllm-project/aibrix/pull/1193
* @justadogistaken made their first contribution in https://github.com/vllm-project/aibrix/pull/1218
* @ModiCodeCraftsman made their first contribution in https://github.com/vllm-project/aibrix/pull/1217
* @haitwang-cloud made their first contribution in https://github.com/vllm-project/aibrix/pull/1230
* @ae86zhizhi made their first contribution in https://github.com/vllm-project/aibrix/pull/1262
* @nicole-lihui made their first contribution in https://github.com/vllm-project/aibrix/pull/1270
* @omerap12 made their first contribution in https://github.com/vllm-project/aibrix/pull/1282
* @li-rongzhi made their first contribution in https://github.com/vllm-project/aibrix/pull/1285
* @rudeigerc made their first contribution in https://github.com/vllm-project/aibrix/pull/1301
* @Yaegaki1Erika made their first contribution in https://github.com/vllm-project/aibrix/pull/1313
* @elizabetht made their first contribution in https://github.com/vllm-project/aibrix/pull/1339
* @autopear made their first contribution in https://github.com/vllm-project/aibrix/pull/1362
* @Epsilon314 made their first contribution in https://github.com/vllm-project/aibrix/pull/1402

## What's Changed
**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.3.0...v0.4.0

* [Docs] Update typo for installation command by @dittops in https://github.com/vllm-project/aibrix/pull/1128
* [Docs] fix: update example yaml ai runtime tag to v0.3.0 by @yyzxw in https://github.com/vllm-project/aibrix/pull/1139
* [Bug]: fix: README.md docs install error by @googs1025 in https://github.com/vllm-project/aibrix/pull/1136
* [Bug] fix: error when parse stop param in completion body by @firebook in https://github.com/vllm-project/aibrix/pull/1145
* Resync model adapters on gateway restart by @dittops in https://github.com/vllm-project/aibrix/pull/1146
* [Docs]add management user link by @yyzxw in https://github.com/vllm-project/aibrix/pull/1141
* [Bug] Add read lock for h.histogram by @runzhen in https://github.com/vllm-project/aibrix/pull/1147
* [Doc] Improve samples/volcano-engine/README.md by @windsonsea in https://github.com/vllm-project/aibrix/pull/1150
* feature: use worker pool management for periodic metrics update by @googs1025 in https://github.com/vllm-project/aibrix/pull/1096
* [Misc] [gpu_optimizer] add namespace info for log by @googs1025 in https://github.com/vllm-project/aibrix/pull/1149
* Add support for custom inference engine port by @varungup90 in https://github.com/vllm-project/aibrix/pull/1140
* Modernize logger interface by @emmanuel-ferdman in https://github.com/vllm-project/aibrix/pull/1161
* Add unit test code coverage by @varungup90 in https://github.com/vllm-project/aibrix/pull/1156
* feat: simplfy router interface by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/1163
* [Bug] Fix image replacements in Kustomize files to support installation by @MondayCha in https://github.com/vllm-project/aibrix/pull/1165
* [Bug]: fix(aibrix kvcache): ObjectPool  by @googs1025 in https://github.com/vllm-project/aibrix/pull/1162
* [Bug]: Fix legacy misconfigurations of autoscaling annotations. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1173
* Enhance the CRD existence check by @learner0810 in https://github.com/vllm-project/aibrix/pull/1170
* [Misc]: add unit test for aibrix metrics collector by @googs1025 in https://github.com/vllm-project/aibrix/pull/1153
* [Docs] Add vllm-cpu local deployment guide to Quickstart by @jiahuipaung in https://github.com/vllm-project/aibrix/pull/1172
* fix: gateway benchmark info by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/1180
* [Bug] fix: error when parse complex content in completion body by @firebook in https://github.com/vllm-project/aibrix/pull/1160
* Add race condition check in unit-test CI and add test-coverage cmd in Makefile by @varungup90 in https://github.com/vllm-project/aibrix/pull/1169
* Supporting Mooncake Traces in Workload Generator by @happyandslow in https://github.com/vllm-project/aibrix/pull/1182
* Recover Client Implementation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1191
* Docs: fixing various text issues by @didier-durand in https://github.com/vllm-project/aibrix/pull/1190
* [Docs] update development instructions to new make commands by @gcalmettes in https://github.com/vllm-project/aibrix/pull/1193
* feat: make preble configurable and rename by @Xunzhuo in https://github.com/vllm-project/aibrix/pull/1189
* [Misc] Add deepseek-r1 tp8 pp2 example by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1195
* [Misc] Update the latest news in README.md by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1196
* [Feature] Add RDMA auto-detection for kvcache by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1194
* [Tooling]: port-forward support, Makefile changes for easier dev workflow in kind by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1210
* Multiple fixes and adding workload merging tool by @happyandslow in https://github.com/vllm-project/aibrix/pull/1213
* Add configurable httproute timeout by @varungup90 in https://github.com/vllm-project/aibrix/pull/1212
* [Bug] fix(e2e flaky): replace for-loop with wait.PollUntilContextTimeout in validateAllPodsAreReady by @googs1025 in https://github.com/vllm-project/aibrix/pull/1214
* [Misc] chore: use constant var for gpu_busy_time_ratio metrics by @googs1025 in https://github.com/vllm-project/aibrix/pull/1215
* fix prefix hash incorrect sometimes by @justadogistaken in https://github.com/vllm-project/aibrix/pull/1218
* [FIX]: vtc-basic router constructor config init, enable e2e tests & add benchmark results only by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1222
* [Doc] Add maintainer guidelines and contributor promotion criteria by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1224
* [PD] Add RoleSet and StormService API skeleton for disaggregation orchestration by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1209
* [Misc]: ensure cache sync before starting controller reconcile by @googs1025 in https://github.com/vllm-project/aibrix/pull/1219
* [FEATURE]: metrics server support for gateway plugins & dashboard by @Venkat2811 in https://github.com/vllm-project/aibrix/pull/1211
* Adding callback patterns for generator client by @happyandslow in https://github.com/vllm-project/aibrix/pull/993
* Add RoleSet and StormService detail spec by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1226
* Add RoleSet and StormService controller implementation by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1229
* Add new test cases for gateway server by @ModiCodeCraftsman in https://github.com/vllm-project/aibrix/pull/1217
* [Refactor] New memory layout for AIBrix KVCache  by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1174
* [Docs]: add advanced kubernetes deployment examples by @haitwang-cloud in https://github.com/vllm-project/aibrix/pull/1230
* [Misc] SLO-aware router with profile support by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1192
* [Misc] Fix storm service rbac issue by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1235
* Support standalone stormservice deployment by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1239
* [Docs]fix: example docs error by @yyzxw in https://github.com/vllm-project/aibrix/pull/1237
* [Docs]refactor: change architecture to stand-alone directories by @yyzxw in https://github.com/vllm-project/aibrix/pull/1236
* [Lint] KVCache uses pre-commit lint by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1243
* [Misc] feature: use kvcache webhook by @googs1025 in https://github.com/vllm-project/aibrix/pull/1187
* [Feature] kvcache cuda kernel by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1247
* Update stormservice controller DefaultRequeueAfter to 15s by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1253
* Set Storm Service default update strategy by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1256
* [docs] Move aibrix component design doc to separate architecture folder by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1250
* Ignore StormService NotFound error during deletion by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1257
* [Misc] Use domain-qualified finalizer name by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1258
* [Bug] Optimize prefix cache hashing to O(N) via block-hash same as vllm by @ae86zhizhi in https://github.com/vllm-project/aibrix/pull/1262
* [Misc]: add ROLE_TEMPLATE_HASH info to container env by @googs1025 in https://github.com/vllm-project/aibrix/pull/1268
* Support /scale sub resource for replica mode by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1259
* [Docs]fix: observability docs dashboard link 404 by @nicole-lihui in https://github.com/vllm-project/aibrix/pull/1270
* [Docs] fix after reorganize incorrect file path by @nicole-lihui in https://github.com/vllm-project/aibrix/pull/1271
* [Doc] KVCache: add section for env vars by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1279
* [Misc] Improve the unit test coverage of stormservice controller by @omerap12 in https://github.com/vllm-project/aibrix/pull/1282
* [Misc] Support role replica index in pod labels by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1280
* [Fix] KVCache: enhance rdma auto-detection by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1276
* [Feature] KVCache: enhance profiling by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1278
* [Fix] KVCache: change cuda kernel's namespace by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1286
* [Feature] KVCache: optimize token list iteration and key building by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1287
* [Feature] KVCache: optimize allocator for compact layout by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1288
* [CI] Support custom IMAGE_TAG to override build tags by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1274
* [Docs] Add documentation for StormService by @li-rongzhi in https://github.com/vllm-project/aibrix/pull/1285
* [Fix] KVCache: fix requirements by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1294
* Improve UT coverage for stormservice controller by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1283
* [Integration] vLLM V1 Connector integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1295
* [Misc] extract hashfunc as a field to allow injection by @vie-serendipity in https://github.com/vllm-project/aibrix/pull/1297
* [Misc] Add unit test code coverage of rolesyncer by @vie-serendipity in https://github.com/vllm-project/aibrix/pull/1296
* [Bug] fix incorrect request count by @firebook in https://github.com/vllm-project/aibrix/pull/1246
* [Fix] KVCache: enhance status by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1304
* [CI] Disable docker push images workflow in forked repositories by @rudeigerc in https://github.com/vllm-project/aibrix/pull/1301
* [Docs] Update stormservice docs and link to index page by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1299
* Adding help flag to benchmark script  by @happyandslow in https://github.com/vllm-project/aibrix/pull/1302
* [Feature] KVCache: add Pris connector by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1303
* [feat] Support dynamic metrics port via model.aibrix.ai/metric-port label by @Yaegaki1Erika in https://github.com/vllm-project/aibrix/pull/1313
* [CI] Support multi-arch build in main branch by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1315
* [Misc] enhance headless service sync with update logic by @omerap12 in https://github.com/vllm-project/aibrix/pull/1311
* [Bug] Fix simple queue out of index error in unit test. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1305
* Fix nil slice issue and add UT coverage for stormservice utils by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1314
* [Misc]: use ctx instead of context by @googs1025 in https://github.com/vllm-project/aibrix/pull/1316
* [Fix] KVCache: InfiniStore connector w/ TCP by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1312
* [CI] Enable multi-arch parallel build by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1317
* [Feature] KVCache: support configurable block size by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1318
* [Feature] Adding raw metrics name conversion in metrics by @happyandslow in https://github.com/vllm-project/aibrix/pull/1293
* [Misc] Add SGLang P/D disaggregation examples by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1319
* [feat] Support generic remote tokenizer by @ae86zhizhi in https://github.com/vllm-project/aibrix/pull/1307
* [feat] Add prefill-decode disaggregation support in aibrix router by @varungup90 in https://github.com/vllm-project/aibrix/pull/1309
* [Feature] Supporting new policies for xLLM  by @happyandslow in https://github.com/vllm-project/aibrix/pull/1322
* [CI] rebuilt kuberay operator with multi-arch support by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1324
* [Fix] KVCache: fix release workflow by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1327
* [CI] Refactor the multi-arch image build in release pipeline by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1325
* [feat] Support Helm Chart by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1323
* [Misc] Support helm chart values for VKE by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1331
* [Misc] Move release test to test/regression folder by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1332
* [Docs] Refactor local development from quick start by @elizabetht in https://github.com/vllm-project/aibrix/pull/1339
* Add initial v0.4.0 regression test yamls by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1337
* feat: Add Helm standard labels and health probes by @omerap12 in https://github.com/vllm-project/aibrix/pull/1343
* Add Qwen3-32b stormservice benchmark manifests by @nwangfw in https://github.com/vllm-project/aibrix/pull/1342
* [Docs] Adding multi engine support documentation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1341
* [Misc] Add vLLM disaggregation samples by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1346
* Switch disaggregation-transfer-backend to mooncake in regression manifests by @nwangfw in https://github.com/vllm-project/aibrix/pull/1348
* Bug fixes for PD disaggregation routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/1354
* Adding v0.4.0 vllm, sglang and dynamo test yamls by @nwangfw in https://github.com/vllm-project/aibrix/pull/1352
* [Docs] KVCache: v0.4.0 release by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1356
* feat: add vLLM remote tokenizer with engine integration by @ae86zhizhi in https://github.com/vllm-project/aibrix/pull/1328
* Add check for missing httproute before request start by @varungup90 in https://github.com/vllm-project/aibrix/pull/1344
* Bug fix streaming in PD disaggregation and add unit tests by @varungup90 in https://github.com/vllm-project/aibrix/pull/1355
* Cut v0.4.0-rc.1 release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1358
* [Fix] KVCache: fix no-space-left issue of release-build action by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1361
* [bench] Add vLLM disagg_proxy_server.py with xPyD Support by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1360
* [Fix] Correct default Helm values for health check port by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1365
* [Fix] Skip adding common labels in  EnvoyProxy by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1367
* [Docs] Added docs for slo routing under Heterogeneous GPU Inference section by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1368
* [Misc] Update v0.4.0 regression benchmark yamls by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1369
* feat: Add KV cache event synchronization system by @ae86zhizhi in https://github.com/vllm-project/aibrix/pull/1349
* Cut v0.4.0-rc.2 release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1373
* [Fix] Use dynamic versioning for AIBrix python package by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1380
* [fix] Use t.Setenv to resolve racing problem by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1382
* [Doc] Add documentation for pd routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/1381
* [Docs] Update the release and kv event docs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1379
* Make prefill request timeout configurable by @varungup90 in https://github.com/vllm-project/aibrix/pull/1377
* Cut release v0.4.0-rc.3 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1384
* [fix] Fix logic bug in prefix cache load balancing causing race test failures by @ae86zhizhi in https://github.com/vllm-project/aibrix/pull/1386
* Replace some hard-coded strings with pkg/constants/model.go  by @autopear in https://github.com/vllm-project/aibrix/pull/1362
* [CI] Install poetry-dynamic-versioning plugin in release workflow by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1389
* Cut release v0.4.0-rc.4 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1390
* [Bug] fix: kvcache_webhook in integration test and webhook config by @googs1025 in https://github.com/vllm-project/aibrix/pull/1392
* Use random as fallback if cache miss in P/D router by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1393
* Revert "Use random as fallback if cache miss in P/D router (#1393)" by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1394
* [Docs] add pd-model deployment example in quickstart doc by @nwangfw in https://github.com/vllm-project/aibrix/pull/1395
* Add @googs1025 as AIBrix maintainer by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1397
* [API] Add PodGroupSize to form a minimum role instance by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1400
* Use random strategy as fallback on cache miss for PD routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/1399
* [Bug] ensure retry not ready roleset by @Epsilon314 in https://github.com/vllm-project/aibrix/pull/1402
* Cut release v0.4.0 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1398

## v0.4.1 (2025-08-19)

Automatically generated release for tag v0.4.1.

## What's Changed
* [Misc] KVCache bugfixes cherry-picks for v0.4.1 by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1458
* [Cherry-Pick] fix: align envoy pod template labels with controller selector by @omerap12 in https://github.com/vllm-project/aibrix/pull/1462
* Cherry picks #1409 #1412 #1425 #1436 #1429 #1427 #1442 #1441 to release-0.4 branch by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1468
* KVCache integration cherry picks by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1474
* Cut release v0.4.1 against release-0.4 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1478


**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.4.0...v0.4.1

## v0.5.0 (2025-11-09)

## 🚀  New Features Highlights
**Batch API & Multimodal and other OpenAI compatible API Surface**
- **Batch API Support**: Add OpenAI-style Batch API with simple LLM workers, Envoy/Gateway integration, JSONL & File List support, job pool sizing, and robust validation to safely offload large asynchronous workloads. (#1298, #1617, #1671, #1698, #1700, #1701)
- **Embeddings API and Moltimodal API**: Introduce OpenAI-compatible embeddings endpoint so online inference, search, and RAG traffic can share the same AIBrix control plane and routing. (#1570) Support multimodality deployments and for image/video generation for other engines. (#1678, #1679, #1603, #1584)
- **Files API & Unified Storage**: Implement OpenAI Files API plus a pluggable storage layer (local, S3, TOS, Redis metadata) to standardize artifact and batch job management across backends. (#1583, #1571)

**AIBrix KVCache Offloading frameworks & Connectors:**
- **High-Performance KVCache**: Adds GDR support, optimized collective communications, configurable max sequence length and batched tokens, multi-threading for higher concurrency, and block-hash based APIs plus external cache handles for flexible distributed deployments. (#1411, #1446, #1453, #1451, #1627, #1628, #1545, #1531, #1542)
- **Deep Engine Integrations**: Provide official AIBrix KVCache Dockerfiles and integration paths for vLLM and SGLang plus correctness fixes (head size, metrics, types) to make KV offloading a first-class option. (#1641, #1696, #1705, #1473, #1450, #1689)

**Production-Grade Prefill/Decode (P/D) Orchestration Support:**
- **New StormService Primitives**: Add PodSet API, PodGroup support, FullRecreate strategy, role upgrade sequences, roleStatuses, and richer RoleSet/PodSet fields to model multi-pod workers, shard groups, and safer rollout/rollback for complex topologies. (#1475, #1506, #1511, #1432, #1599, #1560)
- **P/D-Aware & Topology-Aware Routing**: Prefer P/D workers in the same RoleSet in replication mode, score candidates by locality/load, and harden PD routing behavior for Nixl-based setups. (#1409, #1634, #1429, #1601, #1703, #1693)
- **Role-Level Autoscaling for StormService**: Introduced the "subTargetSelector" field in the PodAutoscaler API, allowing independent autoscaling of specific roles (e.g., prefill, decode) within a StormService resource, particularly in pooled mode. (#1625)

## 📊 Feature Enhancements
- **Unified Runtime & Metadata**: Migrate metadata server from golang to Python for a simpler, lighter control path. Add liveness/readiness probes and shrink runtime image sizes. Improve downloader reliability and recursive object-store fetch support. (#1391, #1639, #1548, #1702, #1571)
- **LoRA & Model Adapter Reliability**: Support adapter scaling to desired replicas, refactor replica management, add wrappers, and enable LoRA downloading via the runtime to stabilize multi-adapter hosting.
 (#1132, #1472, #1670, #1680, #1537, #1541)
- **Autoscaling**: Unify and harden metrics fetching by adding retryable RestMetricsFetcher, shared client/aggregator and fixing race-condition for configuration updates  (#1466, #1487, #1620, #1621, #1709), Tune KPA defaults, support metric label selectors, and ensure PodAutoscaler emits events only when replica counts actually change. (#1624, #1629, #1630) scaling history decision has been supported in the status spec (#1618)
- **AIBrixRuntime Injection**: Deployment & StormService webhooks and wrapper libraries to auto-inject the runtime sidecar, standardizing metrics, downloads, and admin controls across engines.
 (#1403, #1457, #1543, #1681, #1561)

## 📦 Installation & Tooling & CI
- **Helm & Installation**: Strengthen the AIBrix Helm chart as the recommended deployment path by adding dedicated chart CI and fixes (#1370, #1424), enriching Chart.yaml metadata (#1414), introducing values.schema.json for input validation (#1415), supporting imagePullSecrets configuration (#1522), and resolving duplicate label issues for Flux Helm Controller compatibility (#1615). Made KubeRay optional for AIBrix installations if you do not use RayclusterFleet API(#1724)

## 🐞 Critical Bug Fixes
- Fixes StormService headless Service ownership and DNS behavior by setting proper ownerReferences and PublishNotReadyAddresses. (#1441, #1442)
- Fixes incorrect naming for AIBRIX_MODEL_GPU_PROFILE_CACHING_FLAG to ensure configuration consistency. (#1427)
- Fixes KVCache stability issues by preventing panic when watcher or metadata are not set in kvcache.spec. (#1526)
- Fixes PodAutoscaler and metrics correctness by emitting events only on replica changes, aggregating resources across all containers, handling optional MetricSource fields, validating multiple PodAutoscalers targeting the same workload, and ensuring PodSet autoscaler collects metrics from rank0. (#1630, #1643, #1648, #1662, #1704)

## New Contributors
- @JonathonShea made their first contribution in https://github.com/vllm-project/aibrix/pull/1427
- @bigerous made their first contribution in https://github.com/vllm-project/aibrix/pull/1442
- @jiangxiaobin96 made their first contribution in https://github.com/vllm-project/aibrix/pull/1431
- @mayooot made their first contribution in https://github.com/vllm-project/aibrix/pull/1496
- @zyfy29 made their first contribution in https://github.com/vllm-project/aibrix/pull/1505
- @zhengkezhou1 made their first contribution in https://github.com/vllm-project/aibrix/pull/1502
- @tianzhiqiang3 made their first contribution in https://github.com/vllm-project/aibrix/pull/1566
- @atakli made their first contribution in https://github.com/vllm-project/aibrix/pull/1574
- @jwjwjw3 made their first contribution in https://github.com/vllm-project/aibrix/pull/1573
- @lx1036 made their first contribution in https://github.com/vllm-project/aibrix/pull/1586
- @chethanuk made their first contribution in https://github.com/vllm-project/aibrix/pull/1558
- @baozixiaoxixi made their first contribution in https://github.com/vllm-project/aibrix/pull/1608
- @TylerGillson made their first contribution in https://github.com/vllm-project/aibrix/pull/1615
- @omrishiv made their first contribution in https://github.com/vllm-project/aibrix/pull/1626
- @lex1ng made their first contribution in https://github.com/vllm-project/aibrix/pull/1658
- @ChenTaoyu-SJTU made their first contribution in https://github.com/vllm-project/aibrix/pull/1672
- @zhenyu-02 made their first contribution in https://github.com/vllm-project/aibrix/pull/1682
- @yapple made their first contribution in https://github.com/vllm-project/aibrix/pull/1705
- @xvoron made their first contribution in https://github.com/vllm-project/aibrix/pull/1708
- @freedown19 made their first contribution in https://github.com/vllm-project/aibrix/pull/1716
- @Leafykn made their first contribution in https://github.com/vllm-project/aibrix/pull/1718

## What's Changed
**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.4.0...v0.5.0

* Update installation guidance for v0.4.0 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1406
* [Bug] fix webhook config output when using make manifests by @googs1025 in https://github.com/vllm-project/aibrix/pull/1412
* Feat: Add AIBrix Helm chart CI by @omerap12 in https://github.com/vllm-project/aibrix/pull/1370
* [Feature] KVCache: support GDR by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1411
* Select PD workers in same roleset by @varungup90 in https://github.com/vllm-project/aibrix/pull/1409
* [Bug] fix chart-ci by @omerap12 in https://github.com/vllm-project/aibrix/pull/1424
* [Misc]: Enhance Chart.yaml metadata with comprehensive information by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1414
* [feat]: Add values.schema.json for Helm chart input validation by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1415
* [Fix] Fix vLLM NIXL-based P/D samples by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1425
* [Bug] Corrected naming convention for AIBRIX_MODEL_GPU_PROFILE_CACHING_FLAG by @JonathonShea in https://github.com/vllm-project/aibrix/pull/1427
* Feat: add liveness & readiness probes to metadata service by @omerap12 in https://github.com/vllm-project/aibrix/pull/1391
* [Fix] Disable GGA in NIXL samples by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1436
* doc: correct release date in README.md by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1435
* [Misc]: Remove v0.4.0 test files replaced by consolidated base templates by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1428
* feature: add stormservice webhook for inject aibrix runtime by @googs1025 in https://github.com/vllm-project/aibrix/pull/1403
* [Chore] KVCache: downgrade to cuda 12.1 by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1444
* [misc] Update vLLM PD disaggregation image by @happyandslow in https://github.com/vllm-project/aibrix/pull/1445
* [Misc] remove unuseless event by @googs1025 in https://github.com/vllm-project/aibrix/pull/1447
* [Feature] KVCache: support max seq len by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1446
* [Bug] stormservice's headless service not set ownerRef by @bigerous in https://github.com/vllm-project/aibrix/pull/1442
* [Bug] stormservice's headless service need set PublishNotReadyAddresses by @bigerous in https://github.com/vllm-project/aibrix/pull/1441
* [Bug] KVCache: fix metrics by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1450
* [Improvement] KVCache: optimize coll communication by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1451
* Fix P/D disaggregation router to follow Nixl kv_transfer_params by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1429
* [Misc] fix regression test manifests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1456
* [Bug] KVCache: fix max seq len support by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1453
* fix: align envoy pod template labels with controller selector by @omerap12 in https://github.com/vllm-project/aibrix/pull/1439
* [Docs] Update helm installation guidance by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1461
* Refactor to use single loop for least request pod selection by @jiangxiaobin96 in https://github.com/vllm-project/aibrix/pull/1431
* [Misc]: Updates docs to reflect the latest router interface by @googs1025 in https://github.com/vllm-project/aibrix/pull/1465
* [Misc] Add development workload samples by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1467
* Feat(autoscaler): Add retry delays to RestMetricsFetcher by @omerap12 in https://github.com/vllm-project/aibrix/pull/1466
* [Feat] Support adapter scaling to desired replicas by @dittops in https://github.com/vllm-project/aibrix/pull/1132
* [fix] Correct the headless service ownerReference UID in tests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1469
* Refactor: Extract KV event management to break circular dependency by @ae86zhizhi in https://github.com/vllm-project/aibrix/pull/1401
* [Integration] correct head size calculation for AIBrix connectors by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1473
* Cut release v0.4.1 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1477
* Update installation guidance for v0.4.1 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1479
* add least_request_test by @jiangxiaobin96 in https://github.com/vllm-project/aibrix/pull/1463
* [Test]: add controller integration test framework by @googs1025 in https://github.com/vllm-project/aibrix/pull/1448
* Fix missing traffic_pattern parameters in benchmark script by @happyandslow in https://github.com/vllm-project/aibrix/pull/1484
* [Misc] Enhance S3Downloader error handling and IRSA support by @ronaldosaheki in https://github.com/vllm-project/aibrix/pull/1483
* [Chore] KVCache: update torch version by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1490
* refactor(scheme): prevent duplicate registration in RegisterSchemas by @googs1025 in https://github.com/vllm-project/aibrix/pull/1464
* [DOCS] fix: add ReferenceGrant configuration by @omerap12 in https://github.com/vllm-project/aibrix/pull/1486
* Feat: Support role upgrade sequences in stormservice by @omerap12 in https://github.com/vllm-project/aibrix/pull/1432
* [Feat]: add deployment webhook to inject AIBrixRuntime sidecar container by @googs1025 in https://github.com/vllm-project/aibrix/pull/1457
* refactor: improve autoscaler metrics fetcher design by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1487
* [feat]: Add PodSet API for multi-pod worker support in StormService by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1475
* Fix missing FQDN and reuse hash func from syncer by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1500
* [fix] deep copy template to avoid hash mutation issue by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1501
* [Docs] Add `Using NodePort to Expose the Gateway API` section by @mayooot in https://github.com/vllm-project/aibrix/pull/1496
* [Misc] Add unit tests for least_busy_time by @omerap12 in https://github.com/vllm-project/aibrix/pull/1495
* add rolset integration test by @googs1025 in https://github.com/vllm-project/aibrix/pull/1491
* [Misc]: ignore AlreadyExists and NotFound in controller operations by @googs1025 in https://github.com/vllm-project/aibrix/pull/1507
* [Misc] Add unit test for least util routing algorithm by @jiangxiaobin96 in https://github.com/vllm-project/aibrix/pull/1497
* [Misc] test: add unit test for leastGpuCacheRouter by @zyfy29 in https://github.com/vllm-project/aibrix/pull/1505
* [Bug] fix count ready podset condition by @Epsilon314 in https://github.com/vllm-project/aibrix/pull/1518
* [Misc]: add sync-crds makefile cmd by @googs1025 in https://github.com/vllm-project/aibrix/pull/1513
* [Misc] Refactor KPA algorithm by @omerap12 in https://github.com/vllm-project/aibrix/pull/1503
* [CI]: add verify_crd makefile by @googs1025 in https://github.com/vllm-project/aibrix/pull/1514
* [Misc]chore: ignore auto-generated ` _version.py` file by @zhengkezhou1 in https://github.com/vllm-project/aibrix/pull/1502
* [Feat] Improve ModelAdapter reliability with retry and pod switching by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1472
* [Misc] Fix incorrect expressions for mean TTFT and TPOP in Grafana by @rudeigerc in https://github.com/vllm-project/aibrix/pull/1521
* [Docs] Add development test guidance by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1520
* [feat]Add imagePullSecrets values for helm by @my-git9 in https://github.com/vllm-project/aibrix/pull/1522
* [Misc] Add autoscaling validation of minReplicas and maxReplicas by @jiangxiaobin96 in https://github.com/vllm-project/aibrix/pull/1508
* [Misc] test: add unit test for throughputRouter by @zyfy29 in https://github.com/vllm-project/aibrix/pull/1516
* [Misc] test: add unit test for leastKvCacheRouter by @zyfy29 in https://github.com/vllm-project/aibrix/pull/1515
* [MISC]: add test for least_load by @omerap12 in https://github.com/vllm-project/aibrix/pull/1524
* [Bug]fix panic when watcher and metadata not set in kvcache.spec by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1526
* [Bug]: fix annotation in deployment webhook by @googs1025 in https://github.com/vllm-project/aibrix/pull/1527
* [Misc] Generate StormService golang client by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1532
* [Feature] KVCache: support external cache handle by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1531
* [Misc] add model adapter wrapper by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1537
* [Misc]: add podset integration test by @googs1025 in https://github.com/vllm-project/aibrix/pull/1533
* [Bug] use fallback value to prevent divide zero error by @zyfy29 in https://github.com/vllm-project/aibrix/pull/1517
* [Refactor] KVCache: simplify external cache handle create API by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1542
* [MISC] Add wrapper for stormservice by @omerap12 in https://github.com/vllm-project/aibrix/pull/1543
* [Misc] add kvcache wrapper by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1541
* [Misc]: add stormservice integration test by @googs1025 in https://github.com/vllm-project/aibrix/pull/1544
* Improve the runtime downloader quality by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1548
* [misc] Consolidate tests under top-level python tests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1549
* [runtime] Improve lora registration reliability by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1550
* [runtime] Enrich engine metrics and add support for sglang by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1551
* Improve upgradeOrder behavior more intuitive and safer  by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1547
* [CI] fix vllm-mock runtime sidecar startup issue by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1555
* [Mics]: exclude integration tests from make test by @googs1025 in https://github.com/vllm-project/aibrix/pull/1556
* [Misc] test: modify apa scale test by @jiangxiaobin96 in https://github.com/vllm-project/aibrix/pull/1523
* [Misc] add deployment wrapper by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1561
* [API] KVCache: support block hashes by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1545
* [API] Add "FullRecreate" strategy for atomic PodSet recovery by @mayooot in https://github.com/vllm-project/aibrix/pull/1511
* [Misc]: add more field for stormservice roleset podset by @googs1025 in https://github.com/vllm-project/aibrix/pull/1560
* [Misc] (test): add unit test for prefix_cache_preble by @zhengkezhou1 in https://github.com/vllm-project/aibrix/pull/1519
* [MISC] Refactor labels.go & add unit tests by @omerap12 in https://github.com/vllm-project/aibrix/pull/1563
* fix(deploy): add missing labels to pod template by @googs1025 in https://github.com/vllm-project/aibrix/pull/1568
* [Docs]: update installation guide for AIBrix with Helm prerequisites … by @haitwang-cloud in https://github.com/vllm-project/aibrix/pull/1539
* Add multi-metrics-source-support for hpa by @tianzhiqiang3 in https://github.com/vllm-project/aibrix/pull/1566
* Update the broken link related to vllm metrics by @atakli in https://github.com/vllm-project/aibrix/pull/1574
* [feat]Add tolerations values for chart by @my-git9 in https://github.com/vllm-project/aibrix/pull/1579
* [Feat] Batch API Service, working with temporary existing local batch driver by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1298
* [Bug] fix: unexpectedly high TTFT in benchmarks results of reasoning (Chain-of-Thought) LLMs by @jwjwjw3 in https://github.com/vllm-project/aibrix/pull/1573
* [Misc] Suppress info logs in integration tests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1585
* [Bug] add the return value check to pass linter by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1588
* [Feat] Enable redis password in helm chart by @lx1036 in https://github.com/vllm-project/aibrix/pull/1586
* [Misc] Add tests for FallbackRouter by @chethanuk in https://github.com/vllm-project/aibrix/pull/1558
* [CI] Exclude integration tests from race condition test by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1590
* [feat] Add embedding API by @varungup90 in https://github.com/vllm-project/aibrix/pull/1570
* [Mics]: optimize deleteReferenceGrant with label selector in ModelRouter controller by @googs1025 in https://github.com/vllm-project/aibrix/pull/1589
* refactor: implement clean layered autoscaler architecture by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1575
* [Misc] Remove type and impl duplication in autocaler by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1596
* [Feat] Support OpenAI Files API and refactor storage library to support local, s3, tos, and redis (for metadata) by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1583
* Add recursive download for tos v2/s3 client by @happyandslow in https://github.com/vllm-project/aibrix/pull/1571
* [API]: add roleStatuses field in stormservice api by @googs1025 in https://github.com/vllm-project/aibrix/pull/1599
* Add gateway-plugin support to generate image and video by @varungup90 in https://github.com/vllm-project/aibrix/pull/1603
* Improve pdRouter with load-aware routing by @googs1025 in https://github.com/vllm-project/aibrix/pull/1601
* [Misc]: add more field for podautoscaler resource by @omerap12 in https://github.com/vllm-project/aibrix/pull/1611
* [Docs]: Update set_metrics override keys and example curl by @googs1025 in https://github.com/vllm-project/aibrix/pull/1612
* Use EnqueueRequestsFromMapFunc for KVCache controller by @baozixiaoxixi in https://github.com/vllm-project/aibrix/pull/1608
* [Misc] Add tests for PrefixCacheRouting by @chethanuk in https://github.com/vllm-project/aibrix/pull/1587
* Simplify autoscaler by unifying client and aggregator by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1620
* Resolve the UpdateConfiguration race issue in autoscaler by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1621
* Bug: remove duplicate labels that prevent flux helm-controller from deploying the aibrix chart by @TylerGillson in https://github.com/vllm-project/aibrix/pull/1615
* Support scaling behaviors and remove configuration duplication by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1622
* [Docs] update aws documentation to include AI on EKS AIBrix deployment by @omrishiv in https://github.com/vllm-project/aibrix/pull/1626
* feat: add scaling history decision in the status spec by @omerap12 in https://github.com/vllm-project/aibrix/pull/1618
* [Chore] KVCache: add max_num_batched_tokens config by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1627
* feat: support metric label by @baozixiaoxixi in https://github.com/vllm-project/aibrix/pull/1624
* [Misc] Benchmark: add duration limit and max concurrent sessions settings to client by @ronaldosaheki in https://github.com/vllm-project/aibrix/pull/1632
* Support P/D Pooling autoscaling in StormService by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1625
* [Feat] OpenAI Batch API Support with Simple LLM Workers by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1617
* [Bug] podautoscaler: only emit when replica count changes by @omerap12 in https://github.com/vllm-project/aibrix/pull/1630
* update stable and panic value for KPA by @baozixiaoxixi in https://github.com/vllm-project/aibrix/pull/1629
* [Mics]: support qos and burst flag in controller by @googs1025 in https://github.com/vllm-project/aibrix/pull/1637
* feat(metrics): add autoscaler scale action prometheus metric by @omerap12 in https://github.com/vllm-project/aibrix/pull/1638
* [Misc]: sync crds file to helm by @googs1025 in https://github.com/vllm-project/aibrix/pull/1635
* [Feature] KVCache: support multi-threading mode by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1628
* [Integration] vllm aibrix scheduler and connectors by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1641
* [Feat] Migrate metadata server from Go to Python by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1639
* [Doc] Refining workload generator documentation by @happyandslow in https://github.com/vllm-project/aibrix/pull/1631
* [Misc] Multimodality Scenarios Sample Deployment by @happyandslow in https://github.com/vllm-project/aibrix/pull/1584
* [Bug] fix: aggregate resource metrics across all containers in pod by @googs1025 in https://github.com/vllm-project/aibrix/pull/1643
* [Bug]: Make optional fields in MetricSource by @googs1025 in https://github.com/vllm-project/aibrix/pull/1648
* Add requirements file and fix api-key bug by @omerap12 in https://github.com/vllm-project/aibrix/pull/1657
* [Doc] Support batch inference usage doc by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1646
* [Bug]: add validation for multiple PodAutoscalers targeting the same workload by @googs1025 in https://github.com/vllm-project/aibrix/pull/1662
* [Misc] refactor roleSet test validation to use validation Package by @lex1ng in https://github.com/vllm-project/aibrix/pull/1658
* [Misc] add num_waiting_reqs metrics by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1668
* [Mics]: fix retry reconciler in podautoscaler controller by @googs1025 in https://github.com/vllm-project/aibrix/pull/1669
* [Misc] Batch API envoy integration fix, E2E verification, and document update by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1671
* [Misc] Added unit test for WorkloadScale by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1666
* [Misc] Added unit test for APA post autoscaler by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1659
* [MISC] add unit test for podautoscaler monitor by @omerap12 in https://github.com/vllm-project/aibrix/pull/1676
* [CLI] Fix replicate args assignment in main.go by @ChenTaoyu-SJTU in https://github.com/vllm-project/aibrix/pull/1672
* Link to system-installed zmq without building by @autopear in https://github.com/vllm-project/aibrix/pull/1372
* Refactor the model adapter replicas feature by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1670
* Add e2e OpenAI API compatibility test by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1678
* Make Gateway API compatible with OpenAI API by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1679
* Support downloading lora models through runtime by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1680
* [Misc] Optimize runtime sidecar injection logic by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1681
* [Docs] Add VKE docs and update P/D examples on VKE by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1687
* [Misc] Add Integration Test Utilities for PodAutoscaler Controller by @zhenyu-02 in https://github.com/vllm-project/aibrix/pull/1682
* [Fix] KVCache: fix result type of group aware kv manager by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1689
* [Feat]: support mulit metrics for podautoscaler by @googs1025 in https://github.com/vllm-project/aibrix/pull/1688
* [Feat]: add podautoscaler webhook by @googs1025 in https://github.com/vllm-project/aibrix/pull/1683
* [Misc] Added unit tests for WorkloadScale.SetDesiredReplicas by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1692
* [Bug]: fix pd route Algorithms do not check http route by @googs1025 in https://github.com/vllm-project/aibrix/pull/1693
* [Integration] Update vLLM v0.10.2 patch by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1695
* [Integration] add AIBrix KVCache x vLLM dockerfile by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1696
* [batch] Bug fixes and code Improvements in batch API by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1698
* [batch] Support File List API, configurable job pool size and error file handling by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1700
* [batch] Add jsonl input and file validation by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1701
* [CI] Reduce runtime container image size by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1702
* [Misc] Improve P/D router reliability by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1703
* [Misc] Added unit tests related to PodAutoscaler by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1694
* [Integration] clone repo w/ tags in vLLM dockerfile by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1706
* [Integration] add AIBrix KVCache x SGLang dockerfile by @yapple in https://github.com/vllm-project/aibrix/pull/1705
* [BUG] fix: aibrix_benchmark streaming issue #1674 by @xvoron in https://github.com/vllm-project/aibrix/pull/1708
* [Misc]Add unit tests related to gateway server by @freedown19 in https://github.com/vllm-project/aibrix/pull/1716
* [Docs]: add multi metrics podautoscaler docs by @googs1025 in https://github.com/vllm-project/aibrix/pull/1712
* [feat]: Select and score P/D in same roleset by @varungup90 in https://github.com/vllm-project/aibrix/pull/1634
* fix: autoscaler for the podset only collect metrics from rank0 by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1704
* [Misc] Added unit test for metrics fetcher by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1709
* [Misc] Made KubeRay optional for AIBrix installations by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1724
* [fix] Moved deps from profiling group back to main by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1726
* [Docs] Add volcano engine startup docs and quick start by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1725
* feat: add EIC connector by @Leafykn in https://github.com/vllm-project/aibrix/pull/1718
* [API] stormservice support podgroup by @Epsilon314 in https://github.com/vllm-project/aibrix/pull/1506
* Cut v0.5.0 release by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1737
* [Docs] Improve the docs and examples by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1738

## New Contributors
* @JonathonShea made their first contribution in https://github.com/vllm-project/aibrix/pull/1427
* @bigerous made their first contribution in https://github.com/vllm-project/aibrix/pull/1442
* @jiangxiaobin96 made their first contribution in https://github.com/vllm-project/aibrix/pull/1431
* @mayooot made their first contribution in https://github.com/vllm-project/aibrix/pull/1496
* @zyfy29 made their first contribution in https://github.com/vllm-project/aibrix/pull/1505
* @zhengkezhou1 made their first contribution in https://github.com/vllm-project/aibrix/pull/1502
* @tianzhiqiang3 made their first contribution in https://github.com/vllm-project/aibrix/pull/1566
* @atakli made their first contribution in https://github.com/vllm-project/aibrix/pull/1574
* @jwjwjw3 made their first contribution in https://github.com/vllm-project/aibrix/pull/1573
* @lx1036 made their first contribution in https://github.com/vllm-project/aibrix/pull/1586
* @chethanuk made their first contribution in https://github.com/vllm-project/aibrix/pull/1558
* @baozixiaoxixi made their first contribution in https://github.com/vllm-project/aibrix/pull/1608
* @TylerGillson made their first contribution in https://github.com/vllm-project/aibrix/pull/1615
* @omrishiv made their first contribution in https://github.com/vllm-project/aibrix/pull/1626
* @lex1ng made their first contribution in https://github.com/vllm-project/aibrix/pull/1658
* @ChenTaoyu-SJTU made their first contribution in https://github.com/vllm-project/aibrix/pull/1672
* @zhenyu-02 made their first contribution in https://github.com/vllm-project/aibrix/pull/1682
* @yapple made their first contribution in https://github.com/vllm-project/aibrix/pull/1705
* @xvoron made their first contribution in https://github.com/vllm-project/aibrix/pull/1708
* @freedown19 made their first contribution in https://github.com/vllm-project/aibrix/pull/1716
* @Leafykn made their first contribution in https://github.com/vllm-project/aibrix/pull/1718

**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.4.0...v0.5.0

## v0.6.0 (2026-03-03)

# Release Notes

## 📌 Release Summary

- Improvements to **gateway routing and traffic management** for LLM inference services.
- Enhancements to **distributed serving and orchestration**, enabling more flexible multi-node deployments.
- Updates to **batch request processing and OpenAI-compatible APIs**.
- Better **metrics and observability** support.
- Various **bug fixes, stability improvements, and CI/CD updates**.

Overall: This release focuses on improving routing, scalability, and operational stability for running vLLM-based LLM services in Kubernetes.


## 🚀 New Feature Highlights

### **Expanded OpenAI-Compatible API Surface**

This release significantly expands the OpenAI-compatible API capabilities supported by AIBrix.

* **Audio & Classification APIs**: Added support for OpenAI-style audio endpoints (/v1/audio/transcriptions, /v1/audio/translations) along with the new /v1/classify inference API. (#1859, #1905)
* **Image Generation Endpoint**: Introduced OpenAI-compatible generation APIs for images and videos (/v1/images/generations, /v1/video/generations), allowing multimodal generation workloads to run through the same gateway. (#1867)
* **Rerank Model Support**: Added support for rerank models via the /v1/rerank endpoint, enabling improved ranking and retrieval pipelines. (#1837)

These additions further strengthen AIBrix as a unified gateway for diverse AI workloads.

---

### **Advanced Gateway & Routing Capabilities**

Major improvements were made to the gateway routing layer to enable smarter and more flexible inference traffic management.

* **Session Affinity Routing**: Add plugin-based session affinity routing strategies for sticky workloads. (#1751, #1823)
* **Advanced Routing Filters**: Support external header filters for advanced routing scenarios. (#1804)
* **Custom HTTPRoute Paths**: Allow custom path configuration through annotations. (#1841)
* **Multi-Deployment Router Support**: Enable router configuration across multiple deployment targets. (#1835)
* **Least-Request Routing Strategy**: Introduce distributed DP API server routing using least-request algorithms. (#1866)

Together these improvements provide better flexibility when deploying large-scale inference workloads.

---

### **Prefill/Decode (P/D) Disaggregation Improvements**

This release continues to expand support for Prefill/Decode disaggregated inference architectures.

* **PD + KVCache Routing Compatibility**: Enable routing that supports both KVCache and P/D disaggregation within a single runtime image. (#1781)
* **Prefix Cache Optimizations**: Introduce asynchronous prefix cache updates and shared indexers across routing strategies. (#1914, #1939)
* **Combined Routing Strategy with P/D**: Enables intelligent routing across both PD-optimized pods (prefill/decode disaggregated) and combined pods (non-PD) within the same deployment, allowing mixed serving strategies and improved resource utilization. (#1911)

These changes improve the scalability and flexibility of large LLM inference clusters.

---

### **StormService & Control Plane Enhancements**

The StormService controller received multiple upgrades to improve reliability and visibility.

* **Role Revision Tracking**: Add per-role revision tracking to StormService for improved upgrade visibility. (#1731)
* **Role Status Aggregation**: Implement role-level status aggregation and improvements to reconcile logic. (#1761, #1767)
* **Periodic Reconciliation**: Introduce periodic reconciliation for ModelAdapter resources. (#1824)
* **Dynamic Discovery Provider Updates**: Enable discovery providers to dynamically update runtime state. (#1908)
* **Improved Scheduling Integration**: Enhance PodGroup and scheduling strategy handling. (#1889, #1795)

These changes strengthen the orchestration layer used for distributed inference deployments.

---

### **LoRA & Model Adapter Lifecycle Management**

Model adapter and LoRA workflows are improved for reliability and runtime control.

* **Dynamic LoRA Load/Unload for SGLang**: Support runtime loading and unloading of LoRA adapters. (#1853)
* **Artifact Preparation Improvements**: Delegate artifact preparation to LoRA downloader components. (#1898)
* **Improved Adapter Failure Handling**: Transition LoRA resources to `Failed` state when pods are not recoverable. (#1884)

These updates improve multi-adapter inference reliability in production.

---

### **KVCache Framework Improvements**

The AIBrix KVCache framework continues to evolve with new optimizations.

* **Block-First KVCache Layout**: Introduce block-first KVCache layout support. (#1947)
* **CUDA Kernel Improvements**: Add padding token support in KVCache CUDA kernels. (#1958)
* **New KV Connector for PD Reuse**: Add `aibrix_pd_reuse_connector` to support combined PD reuse workflows. (#1852)

These improvements further optimize memory efficiency and performance of KVCache-based inference.

---

## 📊 Observability & Metrics

Major improvements were introduced to monitoring and observability across gateway and runtime layers.

* **Gateway Metrics Support**: Introduce metrics collection directly from the gateway layer. (#1907, #1922)
* **Inference Request Metrics**: Add granular metrics tracking inference request behavior. (#1926)
* **Prometheus Integration Enhancements**:
  * Prometheus authentication support via Kubernetes secrets (#1949)
  * Query queueing support for Prometheus requests (#1964)
* **Routing & Cache Metrics Updates**: Improve routing and cache metrics definitions and naming. (#1968)

A new **SGLang gateway metrics dashboard** was also added. (#1959)

---

## 📦 Installation, Deployment & Platform Support

Deployment workflows and platform support continue to improve.

* **Docker Compose Installation**: Simplify standalone installation with improved docker-compose configuration. (#1871, #1878)
* **Gateway Plugin Standalone Mode**: Allow gateway plugin to run without Kubernetes. (#1873)
* **Envoy Sidecar Support**: Add support for running Envoy as a sidecar alongside the gateway-plugin. (#1931)
* **Flexible Docker Builds**: Improve Docker builds to support multiple platforms and architectures. (#1942)
* **Custom Registry Support**: Support registry addresses containing port values. (#1919)

Additional samples were also added for **Ascend hardware deployments**. (#1935)

---

## 📚 Documentation Improvements

A large set of documentation updates and guides were added.

Highlights include:

* Envoy AI Gateway integration guide (#1733)
* Session affinity routing documentation (#1823)
* Prefill/Decode disaggregation examples (#1811)
* LoRA adapter documentation updates (#1813)
* AIBrix container images for vLLM/SGLang (#1792)
* AWS Trainium2 / Neuron support documentation (#1894)
* Prometheus gateway configuration documentation (#1954)

Numerous README and documentation improvements were also included.

---

## 🐞 Critical Bug Fixes

A number of stability and correctness fixes were implemented across routing, metrics, and runtime systems.

Key fixes include:

* Resolve RDMA issues affecting SGLang and vLLM in P/D disaggregation setups. (#1783)
* Fix Redis authentication handling in Helm charts. (#1806)
* Prevent divide-by-zero errors in APA autoscaling logic. (#1879)
* Fix envoy extension policy paths and gateway service configuration issues. (#1921, #1932)
* Resolve inconsistent label cardinality panic when emitting metrics. (#1977)
* Fix CGO build failures caused by mismatched builder/runtime environments. (#1925)

Additional fixes improve controller stability, metrics correctness, and routing behavior.

---

## 🧪 Testing & Developer Experience

Testing coverage and development workflows were expanded.

* Add E2E tests for Batch API using OpenAI client. (#1743)
* Improve client metrics testing. (#1727)
* Add fake-client based PodGroup unit tests. (#1790)
* Improve benchmark script dependencies and testing utilities. (#1909)

---


## What's Changed
* [Misc] Added test for client metrics by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1727
* [Docs] v0.5.0 KVCache docs and samples by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1745
* [Bug]: fix infinistore(rdma) exists/delete to avoid TCP interleaving by @sherlockkenan in https://github.com/vllm-project/aibrix/pull/1748
* [Chore] fix links in bug report template by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1750
* [Test] Add E2E test for batch API using open AI client. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/1743
* fix(api): correct API comment of RayClusterReplicaSetStatus.Replicas by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1754
* docs(router): clarify parameter and return descriptions by @googs1025 in https://github.com/vllm-project/aibrix/pull/1755
* [Docs]: feature: envoy ai gateway integration by @googs1025 in https://github.com/vllm-project/aibrix/pull/1733
* [feat] Support per-role revision tracking in Stormservice by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1731
* [Docs] added v0.5.0 entry in README by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1757
* [Docs] seperate section for talks in README by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1758
* [Misc] upgrade sidecar webhook image from v0.4.0 to v0.5.0 by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1762
* [Feat] Implement role status aggregation for StormService by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1761
* [fix] Consider revision in role status aggregation by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1767
* [feat] Add affinity values for chart by @my-git9 in https://github.com/vllm-project/aibrix/pull/1763
* [Misc] fix sequence for dev-install-in-kind make target by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1764
* refactor(metrics): use Subsystem for aibrix metrics instead of embedding in Name by @googs1025 in https://github.com/vllm-project/aibrix/pull/1756
* [Bug]: add miss webhook config in helm chart by @googs1025 in https://github.com/vllm-project/aibrix/pull/1776
* [Integration] auto detect torch version in dockerfiles by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1782
* Fix sglang/vllm NIXL RDMA issues with PD disaggregation by @dczhu in https://github.com/vllm-project/aibrix/pull/1783
* [Bug]: add validation in stormservice webhook by @googs1025 in https://github.com/vllm-project/aibrix/pull/1778
* Support both AIBrix KVCache and PD disaggregation routing in one image by @dczhu in https://github.com/vllm-project/aibrix/pull/1781
* Update Aibrix version in installation instructions by @googs1025 in https://github.com/vllm-project/aibrix/pull/1791
* fix(controller): shorten resource name by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1777
* [Docs] Add documentation for AIBrix vLLM/SGLang container images by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1792
* add Podgroup util ut cases using fake-client by @DengHom in https://github.com/vllm-project/aibrix/pull/1790
* fix(controller): correct volcano podgroup annotation key by @zhixian82 in https://github.com/vllm-project/aibrix/pull/1795
* [Feat] KVCache: change Pris to PrisKV by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1807
* [Bug] use redis auth in helm chart if redis pwd is enabled by @sceneryback in https://github.com/vllm-project/aibrix/pull/1806
* [Misc] Shorten hash length from 10 to 6 chars to mitigate 63-char name limit by @Deepam02 in https://github.com/vllm-project/aibrix/pull/1789
* Fix envoy, gateway, and quickstart pd-model images by @dczhu in https://github.com/vllm-project/aibrix/pull/1812
* [Docs]: docs(vllm, sglang): update P/D disaggregation examples Docs by @googs1025 in https://github.com/vllm-project/aibrix/pull/1811
* [Feature]: Add external-filter in Header for advanced routing by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1804
* [Docs] updated lora adapter doc for replica feature redesign by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1813
* feature: add simple session affinity plugins in gateway plugin by @googs1025 in https://github.com/vllm-project/aibrix/pull/1751
* [Docs] Fix typo at samples/disaggregation/vllm/README.md by @n0gu-furiosa in https://github.com/vllm-project/aibrix/pull/1821
* docs(routing): add documentation for session-affinity routing strategy by @googs1025 in https://github.com/vllm-project/aibrix/pull/1823
* Add vLLM Lora testing scripts by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1829
* [Misc] Improve Lora edge cases test coverage by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1830
* [Docs] Add a line break to resolve the issue of code not rendering. by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1833
* [helm]: Include default helpers, rename using fullname by @cabrinha in https://github.com/vllm-project/aibrix/pull/1828
* [Feat] Implement periodic reconcile for ModelAdapter by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1824
* [feat]: support rerank models by @sanmuny in https://github.com/vllm-project/aibrix/pull/1837
* [Feature] add custom path for httpRoute by annotation (#1840) by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1841
* [bugfix] ReqBody receive stream=true when calling /v1/completion by @DengHom in https://github.com/vllm-project/aibrix/pull/1850
* [Feat] Support LoRA loading/unloading for SGLang by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1853
* feat:router based on multi deployment configs by @erictanjn in https://github.com/vllm-project/aibrix/pull/1835
* Feat: Audio endpoint support by @dittops in https://github.com/vllm-project/aibrix/pull/1859
* feat(docker-compose): polish simplified installation setup by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1871
* Support OpenAI compatible image generation endpoint by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1867
* [Feature] support LWS in model-router controller (#1839) by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1851
* [Bugfix] change errMsg for GVK and use ctx.Background instead (#1839) by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1872
* [MISC]: move constants to types.go by @omerap12 in https://github.com/vllm-project/aibrix/pull/1875
* feat: Support gateway plugin running without Kubernetes by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1873
* feat: Add OpenAI-compatible and vLLM-specific endpoints in mocked app by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1877
* fix: standalone docker-compose configuration issues by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1878
* [bug] Fix the simulator import issue by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1883
* [Feature] kv_transfer/kv_connector: Add aibrix_pd_reuse_connector to support PD + reuse by @dczhu in https://github.com/vllm-project/aibrix/pull/1852
* Fix msgpack-based events decoder/encoder from map type to list type by @autopear in https://github.com/vllm-project/aibrix/pull/1848
* [fix] Transition Lora to Failed state when no pods are retriable by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1884
* [Misc] follow up changes for LoRA load/unload in SGLang by @nurali-techie in https://github.com/vllm-project/aibrix/pull/1863
* [Feat]: update PodGroup when RoleSet.SchedulingStrategy changed by @fungaren in https://github.com/vllm-project/aibrix/pull/1889
* Update metrics to align with latest version of vllm by @varungup90 in https://github.com/vllm-project/aibrix/pull/1892
* Replace json package with sonic for better performance by @varungup90 in https://github.com/vllm-project/aibrix/pull/1891
* Fix GetPercentile method by @varungup90 in https://github.com/vllm-project/aibrix/pull/1893
* [Bug] Add roleset-index to annotations by @sceneryback in https://github.com/vllm-project/aibrix/pull/1901
* [feat] add distribute-dp api server least_request route by @paranoidRick in https://github.com/vllm-project/aibrix/pull/1866
* feature: add v1/classify endpoint support by @dittops in https://github.com/vllm-project/aibrix/pull/1905
* [Feat] Add metrics support in the gateway by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1907
* [Misc] Add missing dependency for benchmark script by @pbillaut in https://github.com/vllm-project/aibrix/pull/1909
* [Misc] Set leader election namespace according to release namespace by @pbillaut in https://github.com/vllm-project/aibrix/pull/1910
* Enable combined strategy routing along with PD by @varungup90 in https://github.com/vllm-project/aibrix/pull/1911
* refactor metrics collector by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1912
* [refactor] only update readyPodsMap of prefixCacheRouter in the imbalanced situation by @DengHom in https://github.com/vllm-project/aibrix/pull/1906
* Add async prefix cache update in PD disaggregation by @varungup90 in https://github.com/vllm-project/aibrix/pull/1914
* Feat: Discovery Provider support dynamic update by @penfree in https://github.com/vllm-project/aibrix/pull/1908
* [Bug] Refactor downloader and artifact_service to be non-blocking by @xieus in https://github.com/vllm-project/aibrix/pull/1895
* [Bug] Prevent div by zero in APA by @alpe in https://github.com/vllm-project/aibrix/pull/1879
* [Fix] Add sidecar injection webhook to helm chart by @pbillaut in https://github.com/vllm-project/aibrix/pull/1916
* fix: envoy extension policy path by @pbillaut in https://github.com/vllm-project/aibrix/pull/1921
* Feat: delegate artifacts preparation to lora downloader by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1898
* fix: resolve CGO build failure by aligning builder and runtime env by @varungup90 in https://github.com/vllm-project/aibrix/pull/1925
* feat: add gateway metrics by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1922
* Add metrics to track inference request granular details by @varungup90 in https://github.com/vllm-project/aibrix/pull/1926
* Add gateway configuration for tuning concurrent streams by @varungup90 in https://github.com/vllm-project/aibrix/pull/1918
* feat: emit error metric on failure to read metrics from prometheus or LLM engine by @varungup90 in https://github.com/vllm-project/aibrix/pull/1927
* fix: add missed docker copy cmd from PR #1925 by @varungup90 in https://github.com/vllm-project/aibrix/pull/1928
* fix: allow envoy gateway service customization by @pbillaut in https://github.com/vllm-project/aibrix/pull/1932
* add support for custom registry addr contains ':' by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1919
* fix:validation logic for combined and PD separated deployment by @erictanjn in https://github.com/vllm-project/aibrix/pull/1933
* fix: set default http route and extension policy values explicitly by @pbillaut in https://github.com/vllm-project/aibrix/pull/1937
* Samples for deploying aibrix on ascend by @liangdong1201 in https://github.com/vllm-project/aibrix/pull/1935
* fix: bump up setup-envtest version by @varungup90 in https://github.com/vllm-project/aibrix/pull/1941
* fix: use a shared prefix cache indexer across routing-strategies by @varungup90 in https://github.com/vllm-project/aibrix/pull/1939
* Feat: make the gateway docker flexible to platform by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1942
* fix lock amd64 build by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1945
* [Bugfix] add APA support to stormService without podGroupSize (#1913) by @rayne-Li in https://github.com/vllm-project/aibrix/pull/1917
* revert back the original build way by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1946
* Feat: load prom auth from secret by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1949
* [Docs][API] Add AWS Neuron/Trainium2 support for disaggregated inference by @yahavb in https://github.com/vllm-project/aibrix/pull/1894
* feat: add feature to support envoy as a sidecar to gateway-plugin by @varungup90 in https://github.com/vllm-project/aibrix/pull/1931
* [fix] Add missing model name in unit test by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1950
* [Feature] KVCache support block-first layout by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1947
* [Doc] add gateway prometheus config by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1954
* [feat] Add apps/ structure with chat web portal by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1956
* [Feature] kvcache cuda kernel supports padding tokens by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/1958
* feat: add queue for prometheus query by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1964
* Feat: Support vllm new kvevent format by @penfree in https://github.com/vllm-project/aibrix/pull/1962
* feat: add sglang gateway metrics and gateway dashboard by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1959
* fix: update metric name for routing-algorithms by @varungup90 in https://github.com/vllm-project/aibrix/pull/1968
* fix: add shared path for the downloaded artifacts by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1972
* fix: panic inconsistent label cardinality in emit metrics by @varungup90 in https://github.com/vllm-project/aibrix/pull/1977

## New Contributors
* @sherlockkenan made their first contribution in https://github.com/vllm-project/aibrix/pull/1748
* @dczhu made their first contribution in https://github.com/vllm-project/aibrix/pull/1783
* @sceneryback made their first contribution in https://github.com/vllm-project/aibrix/pull/1806
* @Deepam02 made their first contribution in https://github.com/vllm-project/aibrix/pull/1789
* @rayne-Li made their first contribution in https://github.com/vllm-project/aibrix/pull/1804
* @n0gu-furiosa made their first contribution in https://github.com/vllm-project/aibrix/pull/1821
* @cabrinha made their first contribution in https://github.com/vllm-project/aibrix/pull/1828
* @sanmuny made their first contribution in https://github.com/vllm-project/aibrix/pull/1837
* @erictanjn made their first contribution in https://github.com/vllm-project/aibrix/pull/1835
* @fungaren made their first contribution in https://github.com/vllm-project/aibrix/pull/1889
* @paranoidRick made their first contribution in https://github.com/vllm-project/aibrix/pull/1866
* @pbillaut made their first contribution in https://github.com/vllm-project/aibrix/pull/1909
* @alpe made their first contribution in https://github.com/vllm-project/aibrix/pull/1879
* @liangdong1201 made their first contribution in https://github.com/vllm-project/aibrix/pull/1935
* @yahavb made their first contribution in https://github.com/vllm-project/aibrix/pull/1894

**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.5.0...v0.6.0

## v0.7.0 (2026-06-18)

AIBrix v0.7.0 is here! This release lands **242 merged PRs** over three months and pushes AIBrix toward a composable, self-service inference platform. The theme this cycle is **composability across the operational, workload, engine, and gateway layers**: a new web Console for self-service operations, a production OpenAI-compatible Batch API, first-class multi-engine support (vLLM, SGLang, **TensorRT-LLM**), a KV-cache-centric P/D disaggregation data plane, and a highly-available gateway with pluggable, blendable routing.

📖 Read the full release blog: https://aibrix.github.io/posts/2026-06-16-v0.7.0-release/

> ⚠️ **Maturity note**: The **Console**, **Batch API**, and **Resource Manager / Cloud GPU execution** are new or rebuilt in this cycle and are evolving quickly. Treat them as preview features for now — APIs and behavior may change in v0.8.0.

## 🚀 New Features Highlights

**AIBrix Management Console (Preview)**
- **Web-based control plane**: A new React frontend + Go backend that lets users register models, deploy from reusable versioned templates, submit and track batch jobs, and download results — no `kubectl`/YAML required. (#2094, #2095, #2176)
- **Model & template-centric UX**: `ModelDeploymentTemplate` with model-centric workflows, `CreateModel` API with HDFS path support, and provider-agnostic templates. (#2141, #2144, #2175, #2214)
- **Enterprise & auth**: OIDC login/callback with real user avatar rendering, MySQL backend, file proxy, and feature flags to gate Deployments/Playground. (#2100, #2177, #2178, #2187, #2188, #2314)
- **Batch experience in console**: job execution details, pagination, owner filtering, owner-only downloads, cursor-based listing, and an error-injection framework for resilience testing. (#2244, #2268, #2272, #2274, #2317, #2336)
- **Storage backends**: URI-based store factory with pure-Go SQLite driver and a hardened DB schema for self-hosted deployments. (#2174, #2182, #2208, #2209, #2212)

**OpenAI-Compatible Batch API (Rebuilt for Production)**
- **Wire-compatible Batch API**: Self-hosted async batch processing for `/v1/chat/completions`, `/v1/completions`, and `/v1/embeddings`, backed by a persistent metadata store and an async job state machine. (#2136, #2147, #2185, #2203)
- **Config-driven deployment**: `ModelDeploymentTemplate` + `BatchProfile`, inline template specs end-to-end, and the optional `aibrix.model_template` extension to specify deployment. (#2134, #2207, #2236, #2306)
- **Execution engine rebuild**: Reworked around a `Runtime` + `compute.provider` model (retiring kopf/JobCache), with SSH-launch runtimes for cloud providers and a smart client with transport retry. (#2257, #2261, #2267, #2339)
- **Robust job lifecycle**: scheduling concurrency fixes, double-release prevention, job informer + pagination, and improved resilience across scheduler, console, and engine adapter. (#2217, #2218, #2226, #2240, #2270, #2322)
- **New API surface**: OpenAI **Responses API** support. (#2312)

**Resource Manager & Cloud GPU Execution (Preview)**
- **Pluggable provider model**: Resource Manager interfaces with a GORM-backed store and k8s-backed provisioning. (#2171, #2172, #2183)
- **Cloud GPU providers**: **Lambda Cloud** and **RunPod** via a registry/provider pattern, enabling batch jobs to burst to cloud GPUs. (#2248)
- **Non-blocking planner**: policy-plugin planner with exponential backoff on provisioning failures and provider-agnostic core. (#2239, #2280, #2319)

**Multi-Engine Support (vLLM, SGLang, TensorRT-LLM)**
- **TensorRT-LLM as a first-class engine**: tensor-rt inference engine support, TRT-LLM v1.1.0 metrics integration, and PD support for TRT-LLM 1.3.x. (#2000, #2005, #2043)
- **Engine-aware routing & metrics**: model validation and routing context carry engine information; per-engine metrics fixes for load- and KV-aware routing. (#2022, #2118)
- **Cross-engine PD validation**: PD disaggregation e2e tests across vLLM, SGLang, and TRT-LLM. (#2080)
- **vLLM-Omni / multimodal**: vLLM-Omni endpoints in mock + Dockerfile, multi-model per-service config, and v0.14.0 integration. (#2036, #2037, #2056, #2129)

**KV-Cache-Centric P/D Disaggregation**
- **Unified KV data plane**: L2 KVCache zero-copy APIs and vLLM v0.14.0 integration over a single `aibrix_kvcache` substrate (L1 DRAM + pluggable L2, PrisKV production backend). (#2056, #2060)
- **Connectors**: `AIBrixPDReuseConnector` with prefix-cache support, per-pod KV connector type selection via pod labels, and Type2-inherits-Type1 connector refactor. (#2092, #2125, #2238)
- **Pluggable PD routing**: pluggable prefill score policies (least_request, prefix_cache), configurable decode scorers, decode pod load balancing, and a `KVTransferAgent` abstraction (Mooncake stub). (#2070, #2087, #2105, #2284)
- **PD refactors & hardening**: split router into focused files, extracted `EngineHandler`/`PodSelector` and `PrefillExecutor`, and fixed stale-handle/slot_mapping issues in connector type2. (#2121, #2232, #2308, #2320)

**Highly-Available Gateway with Composable Routing**
- **Cross-replica state sync**: Redis-backed state sync for the in-memory gateway cache, aggregating running requests and prefix-cache state across gateway instances for consistent routing. (#1989, #2159)
- **Composable, blendable routing**: multi-strategy routing with normalized soft-scoring and weighting (e.g. `"least-request:2,throughput:1"`), routing profiles, and a power-of-two router with request-tracker callbacks. (#1944, #2024, #2124)
- **Production hardening**: per-model RPS rate limiting, always-on prefix-cache metrics, HTTPRoute status caching to drop per-request API calls, GOMAXPROCS tuning, and graceful ext_proc shutdown. (#2137, #2200, #2283, #2313, #2334)

## 📊 Feature Enhancements

- **Local mode**: Run gateway, router, and KV cache without Kubernetes, with Redis now optional and a local `/v1/models` endpoint. (#2039, #2055, #2058)
- **Anthropic compatibility**: New `/v1/messages` endpoint. (#2115)
- **OpenTelemetry tracing**: Optional end-to-end tracing with upstream `x-request-id` preservation. (#2157, #2255, #2271)
- **Pluggable service discovery**: Unified `Provider` interface (static / Consul / etcd) with refreshed static discovery. (#2034, #2035)
- **Autoscaling**: KV cache usage percentage added to APA, plus documented PodAutoscaler annotations. (#2057, #2282)
- **Chat app**: backend service, Dockerfile/compose/k8s manifests, image attachments, edit/retry persistence and UI cleanup. (#1971, #1996, #2102, #2278)
- **brixbench**: benchmark provisioning harness for release validation and regression testing, with PD routing scenarios and docs. (#2165, #2273, #2298, #2352)

## 📦 Installation & Tooling & CI

- **Helm**: external Redis config with component-level password validation, controller-manager env support, router idleTimeout, and CRDs separated from operator manifests. (#2201, #2216, #2222, #2230, #2234)
- **CI**: build & preload AIBrix images into kind for chart-testing, multi-arch vllm-mock builds, reduced e2e workflow time, ruff bump/format, and CI action upgrades. (#2059, #2081, #2093, #2219, #2259, #2349)
- **Docs**: production gateway deployment guide, expanded routing/PD guides, vLLM semantic router integration, local-mode, console production setup, batch inference, and brixbench usage. (#2189, #2192, #2193, #2337, #2347, #2348)

## 🐞 Critical Bug Fixes

- Fix per-model metrics cross-talk on multi-model pods and drop duplicate metric-label sanitization. (#2228, #2331)
- Fix session-affinity routing by preserving the `x-session-id` header and prevent nil-pointer panic in request tracking on context cancellation. (#2122, #2338)
- Fix several data races: `TreeNode.lastAccess` in prefix cache, SLO router fallback init, and shared `SyncPrefixHashTable` instance. (#2096, #2106, #2327)
- Fix `/v1/models` returning 404 without a trailing slash and remove `min_tokens` from PD prefill requests to avoid vLLM validation failure. (#2194, #2237)
- Prevent goroutine leaks in periodical sync loops and make the gRPC max message size configurable via env var. (#2077, #2364)
- Clean up orphan resources when RoleSet `podGroupSize` changes. (#2131)

## New Contributors

- @jasonlee-1024 made their first contribution in https://github.com/vllm-project/aibrix/pull/1990
- @Lucas-Qian6 made their first contribution in https://github.com/vllm-project/aibrix/pull/1996
- @xvchris made their first contribution in https://github.com/vllm-project/aibrix/pull/2007
- @NJX-njx made their first contribution in https://github.com/vllm-project/aibrix/pull/1982
- @DhyeyTr made their first contribution in https://github.com/vllm-project/aibrix/pull/2057
- @gabrnavarro made their first contribution in https://github.com/vllm-project/aibrix/pull/2069
- @tmchow made their first contribution in https://github.com/vllm-project/aibrix/pull/2076
- @Peakpine made their first contribution in https://github.com/vllm-project/aibrix/pull/2108
- @naroam1 made their first contribution in https://github.com/vllm-project/aibrix/pull/2119
- @Yang1032 made their first contribution in https://github.com/vllm-project/aibrix/pull/2122
- @DaveLi8086 made their first contribution in https://github.com/vllm-project/aibrix/pull/2153
- @Genmin made their first contribution in https://github.com/vllm-project/aibrix/pull/2168
- @ianliuy made their first contribution in https://github.com/vllm-project/aibrix/pull/2118
- @HeyZackWang made their first contribution in https://github.com/vllm-project/aibrix/pull/2157
- @zhutong196 made their first contribution in https://github.com/vllm-project/aibrix/pull/2194
- @justinchen033 made their first contribution in https://github.com/vllm-project/aibrix/pull/2226
- @Jing-ze made their first contribution in https://github.com/vllm-project/aibrix/pull/2228
- @NelZyhh made their first contribution in https://github.com/vllm-project/aibrix/pull/2230
- @JustAnotherDevv made their first contribution in https://github.com/vllm-project/aibrix/pull/2259
- @xiaoyu-xyz made their first contribution in https://github.com/vllm-project/aibrix/pull/2279
- @arnavnagzirkar made their first contribution in https://github.com/vllm-project/aibrix/pull/2264
- @SarthakB11 made their first contribution in https://github.com/vllm-project/aibrix/pull/2296
- @whalepark made their first contribution in https://github.com/vllm-project/aibrix/pull/2165
- @JinKim48 made their first contribution in https://github.com/vllm-project/aibrix/pull/2232
- @jan-stanek made their first contribution in https://github.com/vllm-project/aibrix/pull/2312
- @V-3604 made their first contribution in https://github.com/vllm-project/aibrix/pull/2331
- @DebugSy made their first contribution in https://github.com/vllm-project/aibrix/pull/2131

## What's Changed

**Full Changelog**: https://github.com/vllm-project/aibrix/compare/v0.6.0...v0.7.0

* feat: add sglang gateway metrics and gateway dashboard by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1959
* feat: add support for routing-profiles by @varungup90 in https://github.com/vllm-project/aibrix/pull/1944
* Feat: Support vllm new kvevent format by @penfree in https://github.com/vllm-project/aibrix/pull/1962
* feat: add queue for prometheus query by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1964
* fix: update metric name for routing-algorithms by @varungup90 in https://github.com/vllm-project/aibrix/pull/1968
* fix: add shared path for the downloaded artifacts by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1972
* fix: panic inconsistent label cardinality in emit metrics by @varungup90 in https://github.com/vllm-project/aibrix/pull/1976
* chore: add s3 example by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/1988
* [feat] Add backend for chat app by @Jeffwan in https://github.com/vllm-project/aibrix/pull/1971
* Misc: replace deprecated vllm entrypoint with vllm serve by @omerap12 in https://github.com/vllm-project/aibrix/pull/1987
* Cut v0.6.0 release by @varungup90 in https://github.com/vllm-project/aibrix/pull/1986
* Misc: replace deprecated vllm entrypoint with vllm serve by @omerap12 in https://github.com/vllm-project/aibrix/pull/1991
* fix: add missing imports in chat app routers by @jasonlee-1024 in https://github.com/vllm-project/aibrix/pull/1990
* [Bug]: broken binary search in GetSignature func by @omerap12 in https://github.com/vllm-project/aibrix/pull/1993
* [API] Support image attachments in chat flow with backend images handling by @Lucas-Qian6 in https://github.com/vllm-project/aibrix/pull/1996
* fix: gateway metrics initialization and nit refactoring in gateway.go by @varungup90 in https://github.com/vllm-project/aibrix/pull/1997
* [Misc] use DescribeTable for GetSignature tests by @omerap12 in https://github.com/vllm-project/aibrix/pull/1998
* feat: add tensor-rt inference engine support by @varungup90 in https://github.com/vllm-project/aibrix/pull/2000
* [Bug]: fix flaky TestLRUStore_TTL by using injectable clock in Put by @xvchris in https://github.com/vllm-project/aibrix/pull/2007
* feat: integrate trtllm v1.1.0 metrics by @varungup90 in https://github.com/vllm-project/aibrix/pull/2005
* Samples and readme for audio endpoints by @dittops in https://github.com/vllm-project/aibrix/pull/1973
* Fix: Support Chat Template Tokenization with vLLM Parameters in Prefix Cache Router by @penfree in https://github.com/vllm-project/aibrix/pull/2002
* chore: enhance model validation and routing context with engine information by @varungup90 in https://github.com/vllm-project/aibrix/pull/2022
* refactor: add AlgorithmConfig to ModelConfigProfile by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2027
* feat(batch): add multi-endpoint body validation and testing by @NJX-njx in https://github.com/vllm-project/aibrix/pull/1982
* feat(metadata): introduce MetadataStore abstraction layer by @NJX-njx in https://github.com/vllm-project/aibrix/pull/1981
* refactor: Update static service discovery by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2034
* [Misc] Fix ruff issues and address review comments by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2030
* feat(mock): add vLLM-Omni endpoint support to mock app by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2036
* refactor: per-service URL/key config for vLLM-Omni multi-model setup by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2037
* Feat: Support running AIBrix in local mode by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2039
* fix: crashloop issue in metadata service by @varungup90 in https://github.com/vllm-project/aibrix/pull/2044
* feat: add pd support for trtllm 1.3.x by @varungup90 in https://github.com/vllm-project/aibrix/pull/2043
* fix: for trtllm update input prompt with prompt_token_ids in /v1/completions by @varungup90 in https://github.com/vllm-project/aibrix/pull/2047
* [App][API] Centralize default model names in config for easy switching by @Lucas-Qian6 in https://github.com/vllm-project/aibrix/pull/2048
* Feat: Support RequestTracker callback & add power of two router by @penfree in https://github.com/vllm-project/aibrix/pull/2024
* [bug] Converted tree from recursive to iterative by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2052
* [Feature] AIBrix L2 KVCache Zero-Copy APIs and vLLM v0.14.0 integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2056
* feat: add /v1/models endpoint to gateway plugin for local mode by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2055
* [Feat] Make Redis optional in local mode by @Lucas-Qian6 in https://github.com/vllm-project/aibrix/pull/2058
* [Bug] Add KV Cache Usage Percentage to APA by @DhyeyTr in https://github.com/vllm-project/aibrix/pull/2057
* [Feature] vLLM integration by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2060
* [bug] Fix flaky test TestRandomRouting by @googs1025 in https://github.com/vllm-project/aibrix/pull/2059
* Fix: Non-blocking metrics worker pool by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2063
* Fix: Replace fmt.Sprintf("%d", n) with strconv.Itoa(n) by @gabrnavarro in https://github.com/vllm-project/aibrix/pull/2069
* Fix lint and types error for apps/chat by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2072
* refactor: replace fmt.Sprintf("%d") with strconv by @tmchow in https://github.com/vllm-project/aibrix/pull/2076
* fix(controller): handle io.ReadAll errors in lora_client.go by @tmchow in https://github.com/vllm-project/aibrix/pull/2075
* fix(gateway): handle strconv.Atoi error in response header processing by @tmchow in https://github.com/vllm-project/aibrix/pull/2074
* feat: improve decode pod load balancing in PD disaggregation by @varungup90 in https://github.com/vllm-project/aibrix/pull/2070
* fix(controller): prevent goroutine leaks in periodical sync loops by @googs1025 in https://github.com/vllm-project/aibrix/pull/2077
* fix(test): fix flaky TestPrefixCacheRouting by using distinct message prefix by @googs1025 in https://github.com/vllm-project/aibrix/pull/2079
* [Misc]: PD disaggregation e2e tests (vLLM, SGLang, TRT-LLM) by @varungup90 in https://github.com/vllm-project/aibrix/pull/2080
* Add lint and type check for multi-modality chat app by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2073
* [CI] Reduce installation e2e workflow time by @varungup90 in https://github.com/vllm-project/aibrix/pull/2081
* perf(gateway): faster chat-completions request body validation by @varungup90 in https://github.com/vllm-project/aibrix/pull/2084
* fix(test): fix flaky TestVTCHighUtilizationFairness by @googs1025 in https://github.com/vllm-project/aibrix/pull/2083
* fix: Optimize MatchPrefix hot path with pre-sized result map and deferred percent calculation by @varungup90 in https://github.com/vllm-project/aibrix/pull/2085
* refactor(pd): pluggable prefill score policy with least_request and prefix_cache impls by @varungup90 in https://github.com/vllm-project/aibrix/pull/2087
* test(gateway): add PD disaggregation benchmark suite for routing hot paths by @varungup90 in https://github.com/vllm-project/aibrix/pull/2088
* [Fix] PD reuse connector supports prefix cache enabled by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2092
* fix preble prefix cache crashes from map race and other issues by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2091
* ci: build vllm-mock as multi-arch image (linux/amd64,linux/arm64) by @googs1025 in https://github.com/vllm-project/aibrix/pull/2093
* feat: Unify service discovery with Provider interface by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2035
* [feat] Add AIBrix management console frontend by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2094
* fix: fix the failed after add mdoeladapter by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/2097
* [feat] Add backend service for aibrix console by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2095
* feat: add enterprise features to console (MySQL, auth, file proxy) by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2100
* fix(console): address review findings (CORS, ListJobs bug, interval cleanup) by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2101
* fix: ensure single shared SyncPrefixHashTable instance across Store a… by @penfree in https://github.com/vllm-project/aibrix/pull/2096
* Add Dockerfile, docker-compose, and Kubernetes manifest for chat app by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2102
* Fix data race on TreeNode.lastAccess in prefix cache MatchPrefix path by @varungup90 in https://github.com/vllm-project/aibrix/pull/2106
* feat: add configurable decode scorer policies by @varungup90 in https://github.com/vllm-project/aibrix/pull/2105
* [Bug] Modify the way container environment variables are rendered by @Peakpine in https://github.com/vllm-project/aibrix/pull/2108
* [Bug]: The podset built-in envs is placed before container envs.(#2113) by @Peakpine in https://github.com/vllm-project/aibrix/pull/2114
* feat:ignore pods with label podGroupIndex > 0 (#2111) by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2112
* feat: add /v1/messages endpoint by @varungup90 in https://github.com/vllm-project/aibrix/pull/2115
* refactor: split PD disaggregation router into focused files by @varungup90 in https://github.com/vllm-project/aibrix/pull/2121
* fix: Dockerfile for new vLLM versions + implement get_num_new_matched_tokens by @naroam1 in https://github.com/vllm-project/aibrix/pull/2119
* [Bug]: Fix session-affinity routing by preserving x-session-id header by @Yang1032 in https://github.com/vllm-project/aibrix/pull/2122
* refactor(kv_connector): Type2 Connector inherits from Type1 Connector by @naroam1 in https://github.com/vllm-project/aibrix/pull/2125
* Revert "fix: Dockerfile for new vLLM versions + implement get_num_new… by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2132
* feat: add semantic routing e2e sample with Envoy ext_proc and vLLM backends by @varungup90 in https://github.com/vllm-project/aibrix/pull/2120
* feat(batch): Config driven ModelDeploymentTemplate and BatchProfile by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2134
* feat(batch): expose OpenAI Batch usage + model fields, flatten state enum by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2136
* feat(console): make /api/v1/jobs a BFF over metadata service /v1/batches by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2139
* feat(console): introduce ModelDeploymentTemplate with model-centric UX by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2141
* refactor(batch): migrate extra_body.aibrix to nested structure by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2142
* feat(console): batch flow picks a deployment template after the model by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2144
* feat: replace k8s annotation with data store as source of truth by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2147
* Update OpenAI compatible file and batch interface tests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2150
* feat(batch): --dry-run mode + fix request_counts.total by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2151
* refactor(batch): collapse BatchJobStore into batch metastore helpers by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2152
* feat(gateway): add per-model requests-per-second rate limiting by @varungup90 in https://github.com/vllm-project/aibrix/pull/2137
* test: run metadata-service in --dry-run mode under config/test by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2155
* fix: update metric name in throughput routing strategy by @DaveLi8086 in https://github.com/vllm-project/aibrix/pull/2153
* fix(storage): make S3 put_object work with non-tellable Readers by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2156
* fix(batch): unblock end-to-end K8s submission path by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2158
* chore(batch): drop dead K8s-API path from aibrix_batch_worker by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2160
* fix(batch): disable sevice links to avoid env-naming collision by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2161
* refactor(batch): always persist BatchJob to metastore by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2162
* fix(batch): compute usage from output file and add in_progress_at time by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2163
* feat(batch): Support worker level REDIS override by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2164
* feat(console/web): batch overrides and model/template UX by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2170
* chore: migrate OpenAI Go SDK to v3 by @Genmin in https://github.com/vllm-project/aibrix/pull/2168
* feat(console/web): JSONL validation hardening, playground API wiring, template fix, nav cleanup by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2173
* feat(console): URI-based store factory, serving_name for JSONL validation by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2174
* refactor(console,batch): keep ModelDeploymentTemplate provider-agnostic by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2175
* feat(console): introduce URL-based routing with React Router and SPA fallback by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2176
* feat(console/auth): implement OIDC login and callback handlers by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2177
* chore(console): batch e2e plumbing + OIDC auth hardening by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2178
* feat(rm): resource manager interfaces by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2171
* fix: resolve trtllm metrics showing undefined model_name and engine_type by @ianliuy in https://github.com/vllm-project/aibrix/pull/2118
* feat(rm): provision result DB CRUD & GORM-backed store impl by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2172
* console: Dockerfile + default sqlite store + BFF↔MDS HTTP logging by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2182
* feat(rm): k8s-backed resource manager by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2183
* feat(batch): basic planner passthrough for integration test by @nwangfw in https://github.com/vllm-project/aibrix/pull/2184
* console: show real user in sidebar/header, add login button when unauthenticated by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2187
* console: expose OIDC username + picture, render avatar by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2188
* feat(cache): aggregate running requests across gateway instances via Redis snapshots by @varungup90 in https://github.com/vllm-project/aibrix/pull/2159
* docs: add production gateway deployment guide and expand routing algorithm docs by @varungup90 in https://github.com/vllm-project/aibrix/pull/2189
* feat: support preserving upstream x-request-id for e2e tracing(#2157) by @HeyZackWang in https://github.com/vllm-project/aibrix/pull/2157
* docs: add vLLM semantic router integration guide by @varungup90 in https://github.com/vllm-project/aibrix/pull/2192
* chore: docs: restructure and expand gateway, PD disaggregation, and production deployment guides by @varungup90 in https://github.com/vllm-project/aibrix/pull/2193
* feat(gateway): implement multi-strategy routing by @DaveLi8086 in https://github.com/vllm-project/aibrix/pull/2124
* [Bugfix]: Remove min_tokens from PD prefill requests to avoid vLLM validation failure by @zhutong196 in https://github.com/vllm-project/aibrix/pull/2194
* feat(batch): planner-batch-intergation test by @nwangfw in https://github.com/vllm-project/aibrix/pull/2186
* fix(rm): fix provision store apis by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2195
* optimize: gateway-plugin cpu usage optimize when stream is true #2196 by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2196
* perf(gateway): optimize GOMAXPROCS for K8s limits to reduce futex contention by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2200
* chart: add router idleTimeout in chart by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2201
* feat(batch): implement async planner for batch orchestration by @nwangfw in https://github.com/vllm-project/aibrix/pull/2197
* Batch refactoring to support dynamic worker. Deployment can be used as job worker now. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2185
* batch(console): persisted job state machine with MDS lazy sync by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2203
* fix[batch]: several job status and db issues by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2206
* batch: inline ModelDeploymentTemplate spec end-to-end by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2207
* fix(store): enhance db schema by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2209
* fix(store): use pure go sqlite driver by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2208
* fix(console): update key to snake_case by @nwangfw in https://github.com/vllm-project/aibrix/pull/2211
* fix(store): fix schema by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2212
* feat(console): add CreateModel API and support hdfs path by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2214
* feat: add state sync for in-memory cache of aibrix-gateway instances by @varungup90 in https://github.com/vllm-project/aibrix/pull/1989
* ci(chart): build and preload Aibrix images into kind for chart-testing by @varungup90 in https://github.com/vllm-project/aibrix/pull/2219
* chore(console): update gpu list and add provisioner config by @nwangfw in https://github.com/vllm-project/aibrix/pull/2221
* [Bug] Fixed scheduling logic to avoid repeat job scheduling. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2218
* [Bug] Job entity manager supports full async methods by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2217
* [Bug] Prevent double-release on submitted job cancellation by @justinchen033 in https://github.com/vllm-project/aibrix/pull/2226
* bugfix: add completed check after process envoy request by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2225
* [Bug] Drop duplicate sanitizeMetricValueLabels call in worker by @Jing-ze in https://github.com/vllm-project/aibrix/pull/2228
* feat(helm): support external Redis config and component-level password validation by @NelZyhh in https://github.com/vllm-project/aibrix/pull/2230
* chart: optimize redis passwd logic in helper.tpl by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2234
* chart: add env for controller-manager by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2216
* [Bug] Fix /v1/models returning 404 without a trailing slash by @Jing-ze in https://github.com/vllm-project/aibrix/pull/2237
* [Misc] Batch: apply inline template specs support by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2236
* [bug] fix console and planner job fetching interaction logics for terminal jobs by @nwangfw in https://github.com/vllm-project/aibrix/pull/2235
* fix(batch): improve batch service resilience across scheduler, console, and engine adapter by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2240
* fix: fix unused fields of provision results by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2242
* fix(chart): fix helm chart-testing CI failures by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2241
* fix(install): separate CRDs from operator manifests by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2222
* batch: upstreamable storage, drivers, resource schema, and model discovery by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2243
* refactor[planner] split provider-agnostic core from planner by @nwangfw in https://github.com/vllm-project/aibrix/pull/2239
* feat(console): batch jobs list pagination, owner filter, and owner-only downloads by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2244
* feat(RM): add extension support by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2245
* feat(RM): add Lambda Cloud & RunPod providers via registry/provider pattern by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2248
* refactor(rm): refactor k8s provider by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2251
* fix(rm): make k8s clientset self-contained by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2252
* [CI]Add vLLM-Omni support to Dockerfile.vllm and sample deployment by @Lucas-Qian6 in https://github.com/vllm-project/aibrix/pull/2129
* [feat]: Support per-pod KV connector type selection via pod labels by @zhutong196 in https://github.com/vllm-project/aibrix/pull/2238
* chore: increase warm up period for gateway state sync in e2e tests to prevent flakiness by @varungup90 in https://github.com/vllm-project/aibrix/pull/2256
* refactor(batch): rebuild execution around Runtime + compute.provider; retire kopf/JobCache by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2257
* Refactor batch AIBrix runtime payload and Kubernetes execution flow by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2261
* feat(batch): support SSH-launch runtimes for cloud providers by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2267
* feat: add openTelemetry support by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2255
* docs: adjust doc level and add guide of enable openTelemetry by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2271
* feat(batch): Expose batch job execution details in console by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2268
* [CI] chore(python): bump ruff to 0.15.12 and apply format by @JustAnotherDevv in https://github.com/vllm-project/aibrix/pull/2259
* [Bug] Fix scheduler concurrency scheduling by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2270
* fix(console): improve batch creation, file selection, and job controls by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2272
* fix(console): improve batch job creation UX by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2274
* Fix: lazy import redis dependencies in mds by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2277
* fix(rm): use UTC time by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2276
* fix(chat): edit/retry persistence, model selector, remove projects, UI cleanup by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2278
* [Misc] Bump Python Ruff dependency by @xiaoyu-xyz in https://github.com/vllm-project/aibrix/pull/2279
* fix(gateway): interrupt idle ext_proc Recv on shutdown to fix slow pod termination by @varungup90 in https://github.com/vllm-project/aibrix/pull/2283
* [Docs] Document PodAutoscaler annotations by @xiaoyu-xyz in https://github.com/vllm-project/aibrix/pull/2282
* fix(batch): correct resource-failed job finalization and runtime display by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2291
* feat(batch): surface CREATED as 'scheduling' status by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2292
* docs: Examples should come with health and readiness checks by @arnavnagzirkar in https://github.com/vllm-project/aibrix/pull/2264
* fix(console): order timeline events by lifecycle on same-second tie, fix dot colors by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2294
* fix(console): mark required fields in deployment template form by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2295
* feat(pd): introduce pluggable KVTransferAgent abstraction with Mooncake stub by @varungup90 in https://github.com/vllm-project/aibrix/pull/2284
* feat(planner): non-blocking planner with policy plugin by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2280
* [Bug] Validate lora_name in ArtifactDelegationService by @SarthakB11 in https://github.com/vllm-project/aibrix/pull/2296
* fix(console): sort batch job list by creation time, page size 10 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2299
* fix(console/batch): anchor batch model field to serving_name across the stack by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2300
* [Misc] Add brixbench benchmark module by @whalepark in https://github.com/vllm-project/aibrix/pull/2165
* refactor(planner): refactor backend APIs by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2303
* Chore(planner): fix provision result and enhance logging by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2305
* fix(batch): accept aibrix.model on the request entry schema by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2306
* fix cn character error in auth header by @scarlet25151 in https://github.com/vllm-project/aibrix/pull/2311
* feat(console/web): gate Deployments and Playground behind feature flags by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2314
* [Misc] Improve brixbench runner cleanup and vLLM argument handling by @whalepark in https://github.com/vllm-project/aibrix/pull/2298
* [Misc] Add Qwen3-8B 4P4D PD routing benchmark scenarios by @whalepark in https://github.com/vllm-project/aibrix/pull/2273
* chore: add license header to brixbench files by @varungup90 in https://github.com/vllm-project/aibrix/pull/2315
* fix(console/web): page through all jobs via cursor instead of capping the list by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2317
* chore: fix race condition tests by @varungup90 in https://github.com/vllm-project/aibrix/pull/2316
* fix(console): frontend passes through request count by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2318
* [Misc] Add exponential backoff to provisioning failure. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2319
* perf(gateway): cache HTTPRoute status to eliminate per-request Kubernetes API calls by @varungup90 in https://github.com/vllm-project/aibrix/pull/2313
* feat(pd): extract EngineHandler and PodSelector abstractions for PD routing by @varungup90 in https://github.com/vllm-project/aibrix/pull/2308
* chore: refine kvcache related dockerfile and docs by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2297
* feat(rm): add time window to resource listing options by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2325
* [Bug] Fix stale-handle KeyError and slot_mapping buffer overflow in connector type2 by @JinKim48 in https://github.com/vllm-project/aibrix/pull/2232
* fix(console): add extraBody field to job struct by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2321
* refactor(pd): extract PrefillExecutor into pd/prefill/ package by @varungup90 in https://github.com/vllm-project/aibrix/pull/2320
* fix(gateway): fix SLO router fallback initialization race against global RouterManager by @varungup90 in https://github.com/vllm-project/aibrix/pull/2327
* chore: nit fix in slo_test race condition test by @varungup90 in https://github.com/vllm-project/aibrix/pull/2328
* [API] Add support for OpenAI Responses API by @jan-stanek in https://github.com/vllm-project/aibrix/pull/2312
* Restore stand alone driver mode by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2323
* Decoupling redis client and redis libs. by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2324
* feat(gateway): always-on prefix cache metrics with routing selection, error, and load imbalance counters by @varungup90 in https://github.com/vllm-project/aibrix/pull/2334
* [Docs] Update batch inference docs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2337
* [Docs] Add local-mode doc and update stable install to v0.6.0 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2347
* [Docs] Add console production setup docs by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2348
* chore: upgrade CI action versions by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2349
* Bump version to v0.7.0-rc.2 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2350
* fix(race-test): slo queue router by @varungup90 in https://github.com/vllm-project/aibrix/pull/2353
* fix(gateway): prevent nil pointer panic in request tracking on context cancellation by @Yang1032 in https://github.com/vllm-project/aibrix/pull/2338
* [Docs] Add Brixbench usage documentation by @xiaoyu-xyz in https://github.com/vllm-project/aibrix/pull/2352
* fix(docs): document AIBRIX_STATESYNC_ENABLED requirement and fix Helm chart env var name by @varungup90 in https://github.com/vllm-project/aibrix/pull/2355
* fix(chart): remove redundant openTelemetry provider and prioritize backendRefs by @rayne-Li in https://github.com/vllm-project/aibrix/pull/2356
* [docs] Add TRT-LLM support to multi-engine page by @varungup90 in https://github.com/vllm-project/aibrix/pull/2357
* feat(batch): Enabling job informer + job list pagination by @zhangjyr in https://github.com/vllm-project/aibrix/pull/2322
* feat(console): error injection framework by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2336
* feat(batch): Add batch smart client transport retry foundation by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2339
* Fix smart client regression by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2361
* fix: fix error injection's lint errors by @DwyaneShi in https://github.com/vllm-project/aibrix/pull/2363
* [Bug] Fix per-model metrics cross-talk on multi-model pods by @V-3604 in https://github.com/vllm-project/aibrix/pull/2331
* fix(gateway): make gRPC max message size configurable via env var by @varungup90 in https://github.com/vllm-project/aibrix/pull/2364
* fix(roleset): cleanup orphan resources when podGroupSize changes by @DebugSy in https://github.com/vllm-project/aibrix/pull/2131
* [Misc] Fix the gofmt issue by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2369
* Bump version to v0.7.0-rc.3 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2370
* Bump version to v0.7.0 by @Jeffwan in https://github.com/vllm-project/aibrix/pull/2371

