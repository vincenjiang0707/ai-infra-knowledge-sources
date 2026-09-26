source: https://docs.nvidia.com/dynamo/reference/releases
lastmod: 2026-09-24T19:58:16.636Z

# Releases

Release history and per-release notes for every Dynamo release, mirrored from GitHub

Release notes for Dynamo v1.0.0 and newer are mirrored here from the [GitHub releases](https://github.com/ai-dynamo/dynamo/releases), with breaking changes tracked on the [Deprecations](https://docs.nvidia.com/dynamo/reference/releases/deprecations) ledger and known issues on the [Known Issues](https://docs.nvidia.com/dynamo/reference/releases/known-issues) page. Patch releases are folded into their base release’s page. Earlier releases link to GitHub.

For the artifact inventory each release shipped — container images, wheels, Helm charts, crates — see [Release Artifacts](https://docs.nvidia.com/dynamo/reference/release-artifacts).

Agents and automation: [Releases (machine-readable)](https://docs.nvidia.com/dynamo/reference/releases-data) renders this release data as generated markdown tables. Fetch the published [JSON](https://raw.githubusercontent.com/ai-dynamo/dynamo/docs-website/fern/assets/releases.json) or [Atom feed](https://raw.githubusercontent.com/ai-dynamo/dynamo/docs-website/fern/assets/releases-atom.xml).

## Releases

Pluggable worker selection policies and tiered KV indexing in the Router, guided tool-call streaming and request validation in the Frontend, image decoding at the Frontend for encode-prefill-decode deployments, v1beta1 CRD storage with the Rust EPP as the default Endpoint Picker, GPU Memory Service V1, and a standalone Snapshot operator.

Patch release and the first Dynamo Enterprise Support release: a curated set of release artifacts publishes under the -enterprise suffix on NGC, eligible for enterprise support, with no functional or binary differences from the open-source artifacts. Fixes NIXL loader-path resolution in the Frontend and SGLang Runtime images, removes the unused Nsight EFA metrics plugin, and tightens dependency pins (pillow v12.3.0 floor, plotext below v6, EFA Installer v1.50). Backend pins are unchanged from v1.4.0.

Patch release. Adds the classify and pooling endpoints, forwards logprob_token_ids through the OpenAI frontend, reconciles request-path overload marks in the Router, and fixes NIXL writable buffers for vLLM. All three Go modules move to Go 1.26.6 with aligned x/net and grpc. Backend pins are unchanged from v1.4.0.

Full-platform preview of v1.3.0: complete runtime matrix, wheels on pypi.nvidia.com, crates, and Helm charts. Superseded by v1.3.0 GA.

DeepSeek-V4 Blackwell preview; vLLM + SGLang containers only.

DeepSeek-V4 Blackwell preview; vLLM + SGLang containers only.

Partial platform preview: TRT-LLM runtime image + wheels only.

Partial platform preview: SGLang + TRT-LLM runtime images + wheels.

Platform preview: runtime matrix, wheels on pypi.nvidia.com, Helm charts.

No artifact additions or removals versus v0.9.0.

First publish of dynamo-tokens crate. Deprecated dynamo-graph Helm chart dropped from the publish stream.

Post-train of v0.8.1: republished the TensorRT-LLM runtime image and PyPI wheels only, with TRT-LLM pinned to 1.2.0rc6.post3. Same CUDA support as v0.8.1.

Post-train of v0.8.1: republished the TensorRT-LLM runtime image and PyPI wheels only, with TRT-LLM pinned to 1.2.0rc6.post2. Same CUDA support as v0.8.1.

Post-train of v0.8.1: republished the TensorRT-LLM runtime image and PyPI wheels only, with TRT-LLM pinned to 1.2.0rc6.post1. Same CUDA support as v0.8.1.

Post trains .post1/.post2/.post3 republished the TRT-LLM runtime image and PyPI wheels only; each carried a distinct TRT-LLM pin (see the v0.8.1.post1/.post2/.post3 rows).

dynamo-frontend image and CUDA 13 variants for vLLM and SGLang. First publish of dynamo-memory and dynamo-config crates.

Post-train of v0.7.0: TensorRT-LLM pin advanced to 1.2.0rc3 (v0.7.0 shipped 1.2.0rc2). Same CUDA support as v0.7.0.

Post-train of v0.6.1: same backend pins as v0.6.1. Same CUDA support as v0.6.1.

Oldest release tracked on this page.

## Release statistics

Counts taken from each release’s GitHub body. A dash means the count was not recorded for that release, not that it was zero.

The pre-v1.0.0 bodies predate the current release-note template and state no PR or contributor totals, so those cells stay empty: the figures were never published, and the counts recoverable from the archive and from git disagree with each other and with the totals the later bodies state. First-time contributors are counted release-wide; a release whose body lists only its external first-timers is left empty rather than undercounted.