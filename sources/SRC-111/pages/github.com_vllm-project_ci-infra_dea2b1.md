source: https://github.com/vllm-project/ci-infra

Infrastructure-as-Code and bootstrap scripts for vLLM's continuous integration pipeline, built on [Buildkite](https://buildkite.com/) with autoscaling compute across AWS and GCP.

```
ci-infra/
├── .buildkite/ # Scheduled Buildkite pipelines (e.g. daily AMI rebuild)
├── buildkite/ # Bootstrap scripts, pipeline generation, and build helpers
│ ├── bootstrap-amd.sh # AMD/ROCm CI entry point
│ ├── bootstrap-intel.sh # Intel CI entry point
│ ├── pipeline_generator/ # Python-based pipeline generator
│ ├── test-template-amd.j2 # AMD/ROCm Jinja2 pipeline template
│ └── scripts/ # Helper scripts (Docker bake, Codecov upload)
├── docker/ # Docker buildx bake configuration (ci.hcl)
├── terraform/
│ ├── aws/ # AWS infrastructure (primary, active)
│ ├── gcp/ # GCP GKE cluster and compute instances
│ └── gcp_old/ # GCP TPU infrastructure (v5, v6e, v7x)
├── packer/
│ ├── cpu/ # CPU build AMI with warm Docker cache
│ └── gpu/ # GPU AMI with NVIDIA drivers
├── infra-k8s/ # Kubernetes-based Buildkite agent deployment
├── github/ # GitHub Actions runner groups (Neural Magic, IBM)
├── claude-skills/ # Portable CI automations and investigation skills
└── usage-stats/ # Usage telemetry collection (Vector)
```


See [claude-skills/AUTOMATIONS.md](https://github.com/vllm-project/ci-infra/blob/main/claude-skills/AUTOMATIONS.md) for the
source-of-truth inventory of:

- portable scheduled automations and their destinations;
- systemd services, timers, schedules, credentials, and persistent state;
- installation, failover, validation, and operational commands;
- host-local automations that are not portable yet;
- investigation skills that do not run on a schedule.

When a commit is pushed to the [vLLM repository](https://github.com/vllm-project/vllm), a Buildkite webhook triggers a new build. The pipeline is dynamically generated based on the changes in the commit.

```
GitHub push/PR
│
▼
Buildkite webhook triggers build
│
▼
Bootstrap step
├── Installs pipeline-generator from ci-infra
├── Generates pipeline YAML from .buildkite/ci_config.yaml
└── Uploads pipeline YAML to Buildkite
│
▼
Steps dispatched to agent queues
├── CPU queues ─── Docker image build, compilation, CPU tests
├── GPU queues ─── Single/multi-GPU tests (L4, A100, H100, H200, B200)
├── TPU queues ─── TPU-specific tests (v5, v6e, v7x)
└── AMD queues ─── ROCm tests (MI250, MI325, MI355)
│
▼
Results reported back (test results, coverage via Codecov)
```


A Python tool (`buildkite/pipeline_generator/`

) that reads step definitions from YAML files in the vLLM repo (e.g. `.buildkite/test_areas/`

, `.buildkite/image_build/`

), groups them, and converts them into Buildkite YAML with proper agent queues, Docker/Kubernetes plugins, and environment configuration.

**How it runs:** The bootstrap step installs `pipeline-generator`

from ci-infra (`pip install git+...ci-infra.git@main#subdirectory=buildkite/pipeline_generator`

) and invokes it with the vLLM repo's `.buildkite/ci_config.yaml`

. The `VLLM_CI_BRANCH`

environment variable controls which ci-infra branch to install from (defaults to `main`

).

**Config:** Driven by a YAML config file (`ci_config.yaml`

) that specifies job directories, registries, repositories, and `run_all_patterns`

. See the [pipeline generator README](https://github.com/vllm-project/ci-infra/blob/main/buildkite/pipeline_generator/README.md) for details.

**Features:**

**Device types**: CPU, GPU (L4), A100, H100, H200, H200 18GB (MIG), B200, GH200, Intel CPU/HPU/GPU, ARM CPU, Ascend NPU, AMD MI250/MI325/MI355 (1-8 devices)**Plugin generation**: Docker plugin for EC2-based queues, Kubernetes pod specs for H100/H200/A100**AMD mirroring**: Steps can define`mirror.amd`

to automatically create parallel AMD test runs**Source file dependencies**: Steps can specify which source files they depend on for intelligent test filtering**Block steps**: Optional tests are gated behind manual approval blocks**Variable injection**: Automatically injects registry URLs, cache tags, and image references into step commands

`buildkite/test-template-amd.j2`

renders vLLM's [ test-pipeline.yaml](https://github.com/vllm-project/vllm/blob/main/.buildkite/test-pipeline.yaml) into Buildkite YAML using

[minijinja-cli](https://github.com/mitsuhiko/minijinja).

| Script | Pipeline | Generation Method |
|---|---|---|
`bootstrap-intel.sh` |
Intel CI | Pipeline generator (via ci-infra) |
`bootstrap-amd.sh` |
AMD/ROCm CI | Jinja2 template (`test-template-amd.j2` ) |

The AMD and Intel bootstrap scripts additionally handle:

**Diff detection**: Computes changed files vs.`origin/main`

(PRs) or`HEAD~1`

(main branch).**Docs-only skip**: If all changes are in`docs/`

,`*.md`

, or`mkdocs.yaml`

, CI is skipped entirely.**Run-all detection**: Changes to critical files (`Dockerfile`

,`CMakeLists.txt`

,`csrc/`

,`setup.py`

,`requirements/*.txt`

) trigger all tests and build wheels from source.**Precompiled wheels**: When no critical files changed, precompiled wheels from the merge-base commit are used if available at`wheels.vllm.ai`

.**PR labels**:`ready-run-all-tests`

forces all tests including optional/nightly.`ci-no-fail-fast`

disables fail-fast mode.**ECR cache resolution**: Resolves multi-layer cache sources with a fallback chain (PR-specific -> base branch -> main).

Managed via Terraform in `terraform/aws/`

. Uses the [Buildkite Elastic CI Stack for AWS](https://github.com/buildkite/elastic-ci-stack-for-aws) (v6.21.0) to deploy autoscaling agent clusters as CloudFormation stacks.

**Regions**: us-west-2 (GPU + CPU queues), us-east-1 (CPU build queues with warm-cache AMI, release queues)

| Queue | Instance Type | Max | Purpose |
|---|---|---|---|
`small_cpu_queue_premerge` |
r6in.large | 40 | Bootstrap, docs, lightweight tasks |
`medium_cpu_queue_premerge` |
r6in.4xlarge | 40 | Medium CPU workloads |
`cpu_queue_premerge` |
r6in.16xlarge (512GB) | 10 | CUDA kernel compilation |
`cpu_queue_premerge_us_east_1` |
r6in.16xlarge (512GB) | 20 | CPU builds (warm-cache AMI) |
`arm64_cpu_queue_premerge` |
r7g.16xlarge | 10 | ARM64 builds |
`gpu_1_queue` |
g6.4xlarge (1x L4) | 208 | Single-GPU tests |
`gpu_4_queue` |
g6.12xlarge (4x L4) | 64 | Multi-GPU tests |

Equivalent postmerge and release queues exist with ECR write access for pushing images. Specialized hardware (H100, H200, B200, A100) is managed via Kubernetes or dedicated pools.

**Each queue consists of:**

- An EC2 Auto Scaling Group that scales instances based on workload
- A Lambda function that polls Buildkite to assess capacity needs
- Buildkite agents running on each instance, executing jobs in Docker containers
- All on-demand (100%), terminated after each job for isolation

**VPC**: Isolated networks in us-west-2 and us-east-1 (10.0.0.0/16, 4 public subnets each)**ECR**:`vllm-ci-test-cache`

(PR builds) and`vllm-ci-postmerge-cache`

(main branch) with 14-day lifecycle**S3**:`vllm-build-sccache`

for C++ compiler cache,`vllm-wheels`

/`vllm-wheels-dev`

for wheel binaries**Secrets Manager**: HuggingFace token, Buildkite analytics token**SSM Parameter Store**: Agent tokens, AMI IDs

**GKE**(`terraform/gcp/`

): Kubernetes clusters in us-central1 and us-west1 with L4 GPU node pools (g2-standard machines, up to 64 nodes). Autopilot cluster available. Artifact registry with 7-day cleanup. Compute instance groups for CPU builders.**TPU**(`terraform/gcp_old/`

): TPU infrastructure across multiple GCP projects:**TPU v5**: v5litepod-1 nodes for CI testing**TPU v6e**: v6e-1 and v6e-8 nodes with hyperdisk-balanced storage**TPU v7x**: v7x-2 and v7x-8 nodes with up to 4TB disk**CPU**: e2-standard-2 and n2-standard-64 instances for CPU-only workloads**Monitoring**: e2-micro instances running buildkite-agent-metrics exporter with GCP Ops Agent


The `infra-k8s/`

directory provides Helm-based deployment of the [Buildkite Agent Stack for Kubernetes](https://github.com/buildkite/agent-stack-k8s). Used for specialized hardware (A100, H100, H200, B200) where the pipeline generator creates Kubernetes pod specs with GPU resource requests, node selectors, and shared storage mounts (EFS/FSx for model weights).

Build performance relies on a multi-layer caching approach:

The bootstrap script resolves cache sources with a fallback chain:

**PR-specific cache**:`vllm-ci-test-cache:pr-{number}`

**Base branch cache**: Cache from the PR's target branch**Main branch cache**:`vllm-ci-postmerge-cache:latest`


Cache is stored as registry refs in private ECR repositories with 14-day expiration.

A daily Buildkite pipeline (`.buildkite/pipelines/rebuild-cpu-ami.yml`

, scheduled at 3 AM PST) builds custom EC2 AMIs with pre-warmed Docker layer caches:

**Build AMI**: Packer creates an AMI from the Buildkite Elastic Stack base, installs BuildKit as a standalone systemd service (not docker-container driver), and pre-pulls the latest postmerge Docker image layers using the bake config artifact from the most recent CI build.**Update SSM**: Stores the new AMI ID in AWS SSM Parameter Store.**Update Launch Templates**: Creates new EC2 Launch Template versions for premerge, postmerge, and release CPU queues, then updates Auto Scaling Groups. Existing instances cycle out naturally (`TerminateInstanceAfterJob=true`

).**Cleanup**: Retains the 3 most recent old AMIs for rollback, deletes older ones and their snapshots.

The warm-cache AMI is used by the `cpu_queue_*_us_east_1`

queues and release queues.

C++ compilation outputs are cached in S3 (`vllm-build-sccache`

in us-west-2), configured via `docker/ci.hcl`

.

When no critical source files have changed, CI uses precompiled wheels from the merge-base commit (hosted at `wheels.vllm.ai`

) instead of building from source.

The `github/`

directory contains Terraform configurations for GitHub Actions runner groups used by partner organizations:

**Neural Magic**(`group-neural-magic/`

): Dedicated runner group for Neural Magic workloads.**IBM**(`group-ibm/`

): Dedicated runner group for IBM workloads.

These are deployed with `terraform apply`

and require a GitHub PAT with organizational admin permissions.

- Create a feature branch on this repo (contact @khluu for access if needed).
- Push your changes to the branch.
- Create a new build on Buildkite with the environment variable:
This tells the bootstrap script to fetch templates/code from your branch instead of
`VLLM_CI_BRANCH=my-feature-branch`

`main`

.

**Notes:**

- Run builds on your own vLLM feature branch/fork, preferably up-to-date with
`main`

. - For fork branches, use the full commit hash (not
`HEAD`

) and format the branch name as`<fork/username>:<branch>`

.

| Variable | Description |
|---|---|
`VLLM_CI_BRANCH` |
ci-infra branch to use for templates (default: `main` ) |
`RUN_ALL` |
Force all tests to run |
`SKIP_TIMEOUT` |
Omit configured step timeouts from Python-generated pipelines when set to `1` |
`NIGHTLY` |
Include optional nightly tests |
`VLLM_USE_PRECOMPILED` |
Use precompiled wheels (`1` ) or build from source (`0` ) |
`COV_ENABLED` |
Enable pytest coverage collection and Codecov upload |
`DOCS_ONLY_DISABLE` |
Skip docs-only detection (always run CI) |
`AMD_MIRROR_HW` |
AMD hardware mirror target (default: `amdproduction` ) |
`NOAUTO` |
Set to `1` to gate all steps behind manual approval blocks |
`PRIORITY` |
Set to `HIGH` for high-priority pipeline scheduling |

```
pip install pre-commit
pre-commit install
```

Enforces YAML validation, Python formatting (ruff), spell checking (typos), and GitHub Actions linting (actionlint).

Machines communicate with Buildkite via an agent. Three deployment options:

: Autoscaling EC2 instances (used by AWS queues).[Elastic CI Stack](https://buildkite.com/docs/agent/v3/elastic-ci-aws/elastic-ci-stack-overview): Kubernetes-orchestrated agents (used for specialized GPU hardware).[K8s Agent Stack](https://github.com/buildkite/agent-stack-k8s): Direct installation on existing machines.[Standalone Agent](https://buildkite.com/docs/agent/v3)

All options require a Buildkite agent token and queue name. Contact @khluu on `#sig-ci`

([vllm-dev.slack.com](https://vllm-dev.slack.com)) to obtain credentials.

For standalone agents, add the token and queue to the agent config (typically `/etc/buildkite-agent/buildkite-agent.cfg`

) and restart the service.

Apache License 2.0