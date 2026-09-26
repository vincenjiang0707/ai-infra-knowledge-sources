source: https://docs.nvidia.com/dynamo/reference/model-early-access-builds
lastmod: 2026-09-24T19:58:16.636Z

# Model Early Access Builds

Per-model early access container builds shipped ahead of stable releases

**Model early access builds do not go through QA validation.** They are experimental builds intended for early testing of a specific model. They may contain bugs, require pinned runtime flags, and receive no patch support. Use a stable release container for production workloads unless the build’s GA path says the recipe is promoted.

A **model early access build** packages a single model’s recipe on one runtime container, tagged `X.Y.Z-<model>-dev.N`

and cut from a side branch ahead of that model’s launch — independently of the stable release cadence. When the model’s backend patches land upstream in the versions a stable release ships, the recipe is **promoted** to the plain `:X.Y.Z`

release container and the early access image is no longer needed.

Full-platform early access builds (`vX.Y.Z-dev.N`

, covering all runtimes, wheels, crates, and Helm charts) are platform previews and are documented under [Early Access Artifacts](https://docs.nvidia.com/dynamo/reference/release-artifacts#early-access-artifacts) instead.

**GA path legend:**

**Promoted**— the recipe runs on the stock`:X.Y.Z`

stable release container; the early access image is superseded.**Dev-only**— the model still requires this early access image (its patches are not yet in a stable release).**Recipe in GA**— the model ships as a recipe on the standard release container.

Every card’s tag is click-to-copy as a full `docker pull`

command. The coverage dots show what each build actually shipped — model builds publish container images only (no wheels, Helm charts, or crates).

v1.4.0 release

First build on the v1.4.0 line; targets the next stable release.

ImagesWheelsHelmCrates[Inkling recipe (main)](https://github.com/ai-dynamo/dynamo/blob/main/docs/recipes/inkling.mdx)

v1.3.0 release

Container carries SGLang cherry-picks (stability, config parsing, model support) opened upstream but not yet in a released SGLang.

ImagesWheelsHelmCrates[GLM-5 NVFP4 recipe](https://docs.nvidia.com/dynamo/dev/recipes/glm-5-nvfp4)

Dynamo changes and the M2 tool-calling fix are in release/1.3.0; the recipes run on the stock :1.3.0 containers.

ImagesWheelsHelmCrates[Recipe on release branch](https://github.com/ai-dynamo/dynamo/tree/release/1.3.0-minimax-m3-dev.1/recipes/minimax-m3)

DeepSeek-V4 Flash and Pro recipes ship in v1.3.0 on the standard TensorRT-LLM release container.

ImagesWheelsHelmCrates[recipes/deepseek-v4 (main)](https://github.com/ai-dynamo/dynamo/tree/main/recipes/deepseek-v4)

Four un-upstreamed vLLM patches; requires pinned flags VLLM_DISABLED_KERNELS=FlashInferFP8ScaledMMLinearKernel and --no-enable-flashinfer-autotune.

ImagesWheelsHelmCrates[Nemotron-3-Ultra recipe](https://docs.nvidia.com/dynamo/dev/recipes/nemotron-3-ultra)

Requires the dedicated `vllm-runtime:1.3.0-nemotron-super-dev.1` image; the model-specific vLLM patches are not in the v1.3.0 release container.

ImagesWheelsHelmCrates[Nemotron-3-Super recipe](https://docs.nvidia.com/dynamo/dev/recipes/nemotron-3-super)

The build's only container patch is in vLLM v0.23.0; the recipes run on the stock vllm-runtime:1.3.0.

ImagesWheelsHelmCrates[Kimi-K2.6 recipe](https://docs.nvidia.com/dynamo/dev/recipes/kimi-k2-6)

Dynamo #10132 (Cosmos3 support in the vLLM-Omni backend) is open, not merged — v1.3.0 containers cannot run Cosmos3.

ImagesWheelsHelmCrates[Launch scripts (branch)](https://github.com/ai-dynamo/dynamo/tree/release/1.3.0-cosmos3-dev.1/examples/backends/vllm/launch)

v1.2.0 release

Blackwell (B200 + GB200) preview; per-arch/CUDA tags (e.g. vllm-runtime:1.2.0-deepseek-v4-cuda13-dev.3). Superseded by the v1.3.0 recipe.

ImagesWheelsHelmCratesBlackwell preview on vLLM v0.20.0 (native DSv4 support); superseded by dev.3.

ImagesWheelsHelmCratesEarliest DSv4 preview (SGLang, B200 only); superseded by dev.2/dev.3.

ImagesWheelsHelmCratesSee [Compatibility](https://docs.nvidia.com/dynamo/reference/compatibility) for hardware, platform, and backend feature support, and [Release Artifacts](https://docs.nvidia.com/dynamo/reference/release-artifacts) for the stable release inventory.