source: https://github.com/InternLM/lmdeploy/releases

# Releases: InternLM/lmdeploy

Releases · InternLM/lmdeploy

## Release list

## v0.17.0

## What's Changed

### 🚀 Features

- Integrate DeepEPv2 by
[@irexyc](https://github.com/irexyc)in[#4783](https://github.com/InternLM/lmdeploy/pull/4783) - feat(pytorch): support Kimi K2.6 by
[@qescccczmr](https://github.com/qescccczmr)in[#4846](https://github.com/InternLM/lmdeploy/pull/4846) - feat(kv_connector): support mooncake store by
[@caikun-pjlab](https://github.com/caikun-pjlab)in[#4903](https://github.com/InternLM/lmdeploy/pull/4903)

### 💥 Improvements

- feat(chat-completions): server-side fan-out for n>1 choices by
[@lvhan028](https://github.com/lvhan028)in[#4841](https://github.com/InternLM/lmdeploy/pull/4841) - perf: further optimize GLM-5.2 serving by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4853](https://github.com/InternLM/lmdeploy/pull/4853) - perf(cuda): use PDL for paged attention and V4 prefill by
[@grimoire](https://github.com/grimoire)in[#4861](https://github.com/InternLM/lmdeploy/pull/4861) - [ascend] update attn op_backend by
[@wanfengcxz](https://github.com/wanfengcxz)in[#4900](https://github.com/InternLM/lmdeploy/pull/4900) - perf(pytorch): optimize compact blocked FP8 MoE and route preparation by
[@grimoire](https://github.com/grimoire)in[#4857](https://github.com/InternLM/lmdeploy/pull/4857) - perf(pytorch): reduce speculative decoding pre/post-processing overhead by
[@grimoire](https://github.com/grimoire)in[#4877](https://github.com/InternLM/lmdeploy/pull/4877) - support page size that are not power of two by
[@irexyc](https://github.com/irexyc)in[#4854](https://github.com/InternLM/lmdeploy/pull/4854) - feat: support structural_tag response_format for turbomind and pytorch engines by
[@windreamer](https://github.com/windreamer)in[#4906](https://github.com/InternLM/lmdeploy/pull/4906)

### 🐞 Bug fixes

- fix(turbomind): restore FP8 weight-only fallback on pre-sm90 GPUs by
[@lvhan028](https://github.com/lvhan028)in[#4871](https://github.com/InternLM/lmdeploy/pull/4871) - fix(vl): raise a clear error on malformed data URLs by
[@SuperMarioYL](https://github.com/SuperMarioYL)in[#4837](https://github.com/InternLM/lmdeploy/pull/4837) - fix(api): fix reponses interface by
[@caikun-pjlab](https://github.com/caikun-pjlab)in[#4893](https://github.com/InternLM/lmdeploy/pull/4893) - Fix/dsv4 native transformers warmup by
[@grimoire](https://github.com/grimoire)in[#4878](https://github.com/InternLM/lmdeploy/pull/4878) - fix: support inline system messages in Anthropic API by
[@lvhan028](https://github.com/lvhan028)in[#4882](https://github.com/InternLM/lmdeploy/pull/4882) - fix: bound DSA prefill score memory by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4896](https://github.com/InternLM/lmdeploy/pull/4896) - fix(build): correct GEMM kernel archive link order by
[@lvhan028](https://github.com/lvhan028)in[#4910](https://github.com/InternLM/lmdeploy/pull/4910) - fix: reject unavailable GLM tool calls by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4901](https://github.com/InternLM/lmdeploy/pull/4901) - fix(pytorch): avoid Triton miscompile in paged attention reduction by
[@lvhan028](https://github.com/lvhan028)in[#4920](https://github.com/InternLM/lmdeploy/pull/4920) - fix Intern-S2-Preview-FP8 convert by
[@irexyc](https://github.com/irexyc)in[#4923](https://github.com/InternLM/lmdeploy/pull/4923)

### 🌐 Other

- [Fix] Validate cross-file Markdown link targets by
[@JimmyWang0417](https://github.com/JimmyWang0417)in[#4868](https://github.com/InternLM/lmdeploy/pull/4868) - Update README to Reflect EuroSys 2027 Paper Acceptance by
[@Youhe-Jiang](https://github.com/Youhe-Jiang)in[#4891](https://github.com/InternLM/lmdeploy/pull/4891) - docs: fix grammar in README by
[@MarkHe1222](https://github.com/MarkHe1222)in[#4866](https://github.com/InternLM/lmdeploy/pull/4866) - improve(autotest): trim unused model configs and gate routed_experts on yaml by
[@littlegy](https://github.com/littlegy)in[#4885](https://github.com/InternLM/lmdeploy/pull/4885) - build: remove flashinfer from CUDA runtime requirements by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4902](https://github.com/InternLM/lmdeploy/pull/4902) - [ci] add base api eval test workflow by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4874](https://github.com/InternLM/lmdeploy/pull/4874) - bump version to v0.17.0 by
[@lvhan028](https://github.com/lvhan028)in[#4914](https://github.com/InternLM/lmdeploy/pull/4914)

## New Contributors

[@JimmyWang0417](https://github.com/JimmyWang0417)made their first contribution in[#4868](https://github.com/InternLM/lmdeploy/pull/4868)[@Youhe-Jiang](https://github.com/Youhe-Jiang)made their first contribution in[#4891](https://github.com/InternLM/lmdeploy/pull/4891)[@MarkHe1222](https://github.com/MarkHe1222)made their first contribution in[#4866](https://github.com/InternLM/lmdeploy/pull/4866)[@qescccczmr](https://github.com/qescccczmr)made their first contribution in[#4846](https://github.com/InternLM/lmdeploy/pull/4846)

**Full Changelog**: `v0.16.0...v0.17.0`

## v0.16.0

## What's Changed

### 🚀 Features

- Support Interns2 mobius by
[@RunningLeon](https://github.com/RunningLeon)in[#4816](https://github.com/InternLM/lmdeploy/pull/4816) - feat: support GLM-5.2 by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4737](https://github.com/InternLM/lmdeploy/pull/4737) - Intern-S2-Mobius meta-MoE support, MoE gate v2, CP attention fixes by
[@lzhangzz](https://github.com/lzhangzz)in[#4835](https://github.com/InternLM/lmdeploy/pull/4835) - Add TurboMind ViT support for InternVL and Qwen VL models by
[@irexyc](https://github.com/irexyc)in[#4719](https://github.com/InternLM/lmdeploy/pull/4719) - feat: add Hy3 support, MTP, and FP8 optimizations by
[@yidingcheng0206](https://github.com/yidingcheng0206)in[#4815](https://github.com/InternLM/lmdeploy/pull/4815)

### 💥 Improvements

- refactor: report cache usage directly by
[@lvhan028](https://github.com/lvhan028)in[#4798](https://github.com/InternLM/lmdeploy/pull/4798) - SM90 native BF16/FP8 GEMM kernels, fused-SiLU quantization, and linear test harness by
[@lzhangzz](https://github.com/lzhangzz)in[#4795](https://github.com/InternLM/lmdeploy/pull/4795) - refactor: split api server endpoints by
[@lvhan028](https://github.com/lvhan028)in[#4797](https://github.com/InternLM/lmdeploy/pull/4797) - refactor(pytorch): derive CUDA step metadata from selected operators by
[@grimoire](https://github.com/grimoire)in[#4805](https://github.com/InternLM/lmdeploy/pull/4805) - optimize and modularize SSM prefix caching by
[@grimoire](https://github.com/grimoire)in[#4788](https://github.com/InternLM/lmdeploy/pull/4788) - perf(guided-decoding): optimize with async D2H copy and xgrammar v0.2.1 by
[@windreamer](https://github.com/windreamer)in[#4605](https://github.com/InternLM/lmdeploy/pull/4605) - refactor(serve): split chat_completions endpoint into a package by
[@lvhan028](https://github.com/lvhan028)in[#4840](https://github.com/InternLM/lmdeploy/pull/4840) - feat(chat-completions): add usage.completion_tokens_details by
[@lvhan028](https://github.com/lvhan028)in[#4842](https://github.com/InternLM/lmdeploy/pull/4842) - feat(pytorch): add optimized Gluon blocked FP8 GEMM for Hopper by
[@grimoire](https://github.com/grimoire)in[#4830](https://github.com/InternLM/lmdeploy/pull/4830) - perf(pytorch): add opt-in torch.compile for decode CUDA graphs by
[@grimoire](https://github.com/grimoire)in[#4808](https://github.com/InternLM/lmdeploy/pull/4808) - Ssm prefix cache non aligned by
[@grimoire](https://github.com/grimoire)in[#4799](https://github.com/InternLM/lmdeploy/pull/4799) - perf: optimize GLM-5.2 serving by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4827](https://github.com/InternLM/lmdeploy/pull/4827) - refactor: separate request preprocessing from generation by
[@lvhan028](https://github.com/lvhan028)in[#4856](https://github.com/InternLM/lmdeploy/pull/4856)

### 🐞 Bug fixes

- [Bugfix] Fix PyTorch H2D input lifetime across CUDA streams by
[@grimoire](https://github.com/grimoire)in[#4792](https://github.com/InternLM/lmdeploy/pull/4792) - fix(serve): reject empty/falsy prompt input in format_prompts and AsyncEngine.generate by
[@SuperMarioYL](https://github.com/SuperMarioYL)in[#4803](https://github.com/InternLM/lmdeploy/pull/4803) - Fix ray mp duplicate output by
[@RunningLeon](https://github.com/RunningLeon)in[#4833](https://github.com/InternLM/lmdeploy/pull/4833) - fix(turbomind): dispatch cuMemcpyBatchAsync by CUDA runtime version by
[@lvhan028](https://github.com/lvhan028)in[#4838](https://github.com/InternLM/lmdeploy/pull/4838) - fix(disagg): use JSON instead of pickle for P2P ZMQ requests (
[#4804](https://github.com/InternLM/lmdeploy/issues/4804)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#4812](https://github.com/InternLM/lmdeploy/pull/4812) - fix(serve): emit signatures for Anthropic thinking blocks by
[@matrix72c](https://github.com/matrix72c)in[#4851](https://github.com/InternLM/lmdeploy/pull/4851) - Fix int4 KV cache quantization range when the packed head width is not a power of two by
[@truong-v](https://github.com/truong-v)in[#4850](https://github.com/InternLM/lmdeploy/pull/4850) - fix: harden serving request validation by
[@lvhan028](https://github.com/lvhan028)in[#4872](https://github.com/InternLM/lmdeploy/pull/4872) - fix: fix allgather/allgather2d for cuda-ipc when byte_width is not multiple of uint by
[@irexyc](https://github.com/irexyc)in[#4873](https://github.com/InternLM/lmdeploy/pull/4873)

### 📚 Documentations

- docs: update recent model support by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4855](https://github.com/InternLM/lmdeploy/pull/4855) - docs,tests: cover Qwen3.8 preserve_thinking support by
[@lvhan028](https://github.com/lvhan028)in[#4869](https://github.com/InternLM/lmdeploy/pull/4869)

### 🌐 Other

- docs: remove non-existent
`--enable-metrics`

flag from metrics/spec_decoding guides by[@latent-9](https://github.com/latent-9)in[#4809](https://github.com/InternLM/lmdeploy/pull/4809) - Upgrade to cu130 by
[@RunningLeon](https://github.com/RunningLeon)in[#4753](https://github.com/InternLM/lmdeploy/pull/4753) - TEST: update turbomind qwen3.5 config by
[@littlegy](https://github.com/littlegy)in[#4778](https://github.com/InternLM/lmdeploy/pull/4778) - chore: use python3.12 for docformatter pre-commit hook by
[@lvhan028](https://github.com/lvhan028)in[#4839](https://github.com/InternLM/lmdeploy/pull/4839) - ci: support CUDA 13.0 Docker builds and publishing by
[@lvhan028](https://github.com/lvhan028)in[#4817](https://github.com/InternLM/lmdeploy/pull/4817) - TEST: update deepseekv4-flash config by
[@littlegy](https://github.com/littlegy)in[#4836](https://github.com/InternLM/lmdeploy/pull/4836) - [ci] Adjust evaluation gate benchmark datasets to reduce runtime and extend coverage by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4834](https://github.com/InternLM/lmdeploy/pull/4834) - [ci] remove old models and refactor interface testcase by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4806](https://github.com/InternLM/lmdeploy/pull/4806) - bump version to v0.16.0 by
[@lvhan028](https://github.com/lvhan028)in[#4847](https://github.com/InternLM/lmdeploy/pull/4847)

## New Contributors

[@latent-9](https://github.com/latent-9)made their first contribution in[#4809](https://github.com/InternLM/lmdeploy/pull/4809)[@SuperMarioYL](https://github.com/SuperMarioYL)made their first contribution in[#4803](https://github.com/InternLM/lmdeploy/pull/4803)[@yidingcheng0206](https://github.com/yidingcheng0206)made their first contribution in[#4815](https://github.com/InternLM/lmdeploy/pull/4815)[@matrix72c](https://github.com/matrix72c)made their first contribution in[#4851](https://github.com/InternLM/lmdeploy/pull/4851)[@truong-v](https://github.com/truong-v)made their first contribution in[#4850](https://github.com/InternLM/lmdeploy/pull/4850)

**Full Changelog**: `v0.15.0...v0.16.0`

## v0.15.0

## What's Changed

### 🚀 Features

- Support long-context and MTP prefix-cache hits by
[@grimoire](https://github.com/grimoire)in[#4688](https://github.com/InternLM/lmdeploy/pull/4688) - [Feature] Add guided decoding support for speculative decoding by
[@windreamer](https://github.com/windreamer)in[#4559](https://github.com/InternLM/lmdeploy/pull/4559) - feat(turbomind): memory allocator, object cache, and scheduler integration by
[@lzhangzz](https://github.com/lzhangzz)in[#4717](https://github.com/InternLM/lmdeploy/pull/4717) - feat: add AgRs all2all backend by
[@irexyc](https://github.com/irexyc)in[#4739](https://github.com/InternLM/lmdeploy/pull/4739) - DeepSeek V4 support by
[@grimoire](https://github.com/grimoire)in[#4554](https://github.com/InternLM/lmdeploy/pull/4554) - Support memdecode by
[@lvhan028](https://github.com/lvhan028)in[#4767](https://github.com/InternLM/lmdeploy/pull/4767)

### 💥 Improvements

- Force blksize=128 for linear attention on ascend by
[@jinminxi104](https://github.com/jinminxi104)in[#4705](https://github.com/InternLM/lmdeploy/pull/4705) - refactor: unify interleaved MRoPE rotary embedding by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4644](https://github.com/InternLM/lmdeploy/pull/4644) - Refine multi-node support on ascend-A3 by
[@jinminxi104](https://github.com/jinminxi104)in[#4711](https://github.com/InternLM/lmdeploy/pull/4711) - [Improve]: Remove dlblas from lmdeploy by
[@RunningLeon](https://github.com/RunningLeon)in[#4682](https://github.com/InternLM/lmdeploy/pull/4682) - replace sync with wait event in h2d by
[@grimoire](https://github.com/grimoire)in[#4709](https://github.com/InternLM/lmdeploy/pull/4709) - Respect --server-port in DP mode when proxy-url is set by
[@lvhan028](https://github.com/lvhan028)in[#4712](https://github.com/InternLM/lmdeploy/pull/4712) - add --language-model-only for text-only VLM inference and remove --disable-vision-encoder by
[@lvhan028](https://github.com/lvhan028)in[#4716](https://github.com/InternLM/lmdeploy/pull/4716) - Optimize TTFT by
[@grimoire](https://github.com/grimoire)in[#4695](https://github.com/InternLM/lmdeploy/pull/4695) - Optimize BaseResponseParser streaming and add parser benchmark by
[@lvhan028](https://github.com/lvhan028)in[#4697](https://github.com/InternLM/lmdeploy/pull/4697) - Support fp8 moe only for qwen3.5 by
[@RunningLeon](https://github.com/RunningLeon)in[#4740](https://github.com/InternLM/lmdeploy/pull/4740) - clear runtime state in sleep by
[@grimoire](https://github.com/grimoire)in[#4729](https://github.com/InternLM/lmdeploy/pull/4729) - feat(serve): add --generation-config CLI for server sampling defaults by
[@lvhan028](https://github.com/lvhan028)in[#4708](https://github.com/InternLM/lmdeploy/pull/4708) - fix: gzip torch profiler traces by default by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4747](https://github.com/InternLM/lmdeploy/pull/4747) - Optimize tp fp8 moe for small average router per expert by
[@grimoire](https://github.com/grimoire)in[#4751](https://github.com/InternLM/lmdeploy/pull/4751) - refactor(pytorch): clarify scheduler and input-maker control flow by
[@grimoire](https://github.com/grimoire)in[#4727](https://github.com/InternLM/lmdeploy/pull/4727) - Guard DP dummy inputs around pending work by
[@grimoire](https://github.com/grimoire)in[#4738](https://github.com/InternLM/lmdeploy/pull/4738) - Remove interactive chat and make inference stateless by
[@lvhan028](https://github.com/lvhan028)in[#4730](https://github.com/InternLM/lmdeploy/pull/4730) - feat(turbomind): Derive composable TurboMind parallel configurations by
[@lzhangzz](https://github.com/lzhangzz)in[#4769](https://github.com/InternLM/lmdeploy/pull/4769) - Add generic tensor copy and architecture-aware Gated Delta Rule support by
[@lzhangzz](https://github.com/lzhangzz)in[#4757](https://github.com/InternLM/lmdeploy/pull/4757) - Add GDR CP controls and legacy kernel override by
[@lzhangzz](https://github.com/lzhangzz)in[#4779](https://github.com/InternLM/lmdeploy/pull/4779) - fix(turbomind): fix zero-centered RMSNorm for Qwen3.5 by
[@lzhangzz](https://github.com/lzhangzz)in[#4790](https://github.com/InternLM/lmdeploy/pull/4790)

### 🐞 Bug fixes

- fix prefix caching by
[@grimoire](https://github.com/grimoire)in[#4700](https://github.com/InternLM/lmdeploy/pull/4700) - fix
`_reduce_split_kernel`

for triton 3.5.1 by[@irexyc](https://github.com/irexyc)in[#4696](https://github.com/InternLM/lmdeploy/pull/4696) - fix triton fp8 all_reduce group by
[@grimoire](https://github.com/grimoire)in[#4702](https://github.com/InternLM/lmdeploy/pull/4702) - fix(serve): use unique chatcmpl id for chat completions responses by
[@lvhan028](https://github.com/lvhan028)in[#4707](https://github.com/InternLM/lmdeploy/pull/4707) - [Bugfix] Fix ImportError in get_chat_template for builtin chat-template names by
[@waynehacking8](https://github.com/waynehacking8)in[#4690](https://github.com/InternLM/lmdeploy/pull/4690) - [Bugfix] Fix InternVL/InternVL3 LoRA loading TypeError in adapter fallback by
[@waynehacking8](https://github.com/waynehacking8)in[#4684](https://github.com/InternLM/lmdeploy/pull/4684) - Force blksize=128 when head_dim=256 on ascend by
[@wanfengcxz](https://github.com/wanfengcxz)in[#4723](https://github.com/InternLM/lmdeploy/pull/4723) - fix HCCL port conflict on multi-dp rank startup(single node) by
[@wanfengcxz](https://github.com/wanfengcxz)in[#4722](https://github.com/InternLM/lmdeploy/pull/4722) - fix: fail fast on invalid serve parsers by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4701](https://github.com/InternLM/lmdeploy/pull/4701) - fix: parse multimodal tool messages by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4680](https://github.com/InternLM/lmdeploy/pull/4680) - Reprobe once for health request by
[@RunningLeon](https://github.com/RunningLeon)in[#4703](https://github.com/InternLM/lmdeploy/pull/4703) - fix: enable graph capture during DP warmup decoding by
[@wanfengcxz](https://github.com/wanfengcxz)in[#4728](https://github.com/InternLM/lmdeploy/pull/4728) - fix: proper XGrammar integration for guided decoding by
[@windreamer](https://github.com/windreamer)in[#4726](https://github.com/InternLM/lmdeploy/pull/4726) - fix: release multimodal payload after mp handoff by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4725](https://github.com/InternLM/lmdeploy/pull/4725) - Fix MTP recurrent state round-trip for Qwen3.5 by
[@RunningLeon](https://github.com/RunningLeon)in[#4744](https://github.com/InternLM/lmdeploy/pull/4744) - Fix mtp dpmeta and guard the warmup by
[@RunningLeon](https://github.com/RunningLeon)in[#4741](https://github.com/InternLM/lmdeploy/pull/4741) - Fix GLM MTP by
[@RunningLeon](https://github.com/RunningLeon)in[#4749](https://github.com/InternLM/lmdeploy/pull/4749) - fix false negative healthy status check for turbomind by
[@irexyc](https://github.com/irexyc)in[#4745](https://github.com/InternLM/lmdeploy/pull/4745) - fix(vl): forward tools to multimodal chat templates by
[@lvhan028](https://github.com/lvhan028)in[#4759](https://github.com/InternLM/lmdeploy/pull/4759) - fix: restrict remote media domains by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4734](https://github.com/InternLM/lmdeploy/pull/4734) - fix(turbomind): restore INT8 KV quant-param offset in block layout by
[@lzhangzz](https://github.com/lzhangzz)in[#4764](https://github.com/InternLM/lmdeploy/pull/4764) - fix(turbomind): avoid async TP shutdown deadlock by
[@lzhangzz](https://github.com/lzhangzz)in[#4770](https://github.com/InternLM/lmdeploy/pull/4770) - fix: bound grouped GEMM scheduling by routed tokens by
[@lzhangzz](https://github.com/lzhangzz)in[#4771](https://github.com/InternLM/lmdeploy/pull/4771) - feat(turbomind): enable SM90 GDR PDL and fix CP matrix layout by
[@lzhangzz](https://github.com/lzhangzz)in[#4787](https://github.com/InternLM/lmdeploy/pull/4787) - fix(serve): auto-generate batch completion sessions to avoid id collision (
[#4773](https://github.com/InternLM/lmdeploy/issues/4773)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#4774](https://github.com/InternLM/lmdeploy/pull/4774) - feat(turbomind): restore metrics reporting by
[@lvhan028](https://github.com/lvhan028)in[#4768](https://github.com/InternLM/lmdeploy/pull/4768) - fix: skip interns2 preview time-series weights by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4801](https://github.com/InternLM/lmdeploy/pull/4801) - fix(serve): handle missing logprobs attrs on TurbomindEngineConfig in Anthropic messages by
[@lvhan028](https://github.com/lvhan028)in[#4800](https://github.com/InternLM/lmdeploy/pull/4800)

### 🌐 Other

- bump version to v0.14.0 by
[@lvhan028](https://github.com/lvhan028)in[#4689](https://github.com/InternLM/lmdeploy/pull/4689) - TEST: Improve tool test by
[@littlegy](https://github.com/littlegy)in[#4632](https://github.com/InternLM/lmdeploy/pull/4632) - chore: update deepgemm revision by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4713](https://github.com/InternLM/lmdeploy/pull/4713) - TEST：Add H Prefix Cache Test, HF Path Conversion, and Ascend Multi-node Startup Config by
[@littlegy](https://github.com/littlegy)in[#4706](https://github.com/InternLM/lmdeploy/pull/4706) - chore: remove deprecated model support by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4693](https://github.com/InternLM/lmdeploy/pull/4693) - [Ascend] support qwen35 mtp on Ascend-A3 by
[@wanfengcxz](https://github.com/wanfengcxz)in[#4721](https://github.com/InternLM/lmdeploy/pull/4721) - ci: pin jlumbroso/free-disk-space to a full commit SHA by
[@kobihikri](https://github.com/kobihikri)in[#4748](https://github.com/InternLM/lmdeploy/pull/4748) - fix: install xgrammar for jetson docker by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4758](https://github.com/InternLM/lmdeploy/pull/4758) - update turbomind builder image by
[@irexyc](https://github.com/irexyc)in[#4752](https://github.com/InternLM/lmdeploy/pull/4752) - fix(autotest): drop flaky text inequality in same session_id generate test by
[@littlegy](https://github.com/littlegy)in[#4766](https://github.com/InternLM/lmdeploy/pull/4766) - fix(benchmark): seed NumPy RNG so --seed controls random-mode lengths (
[#4784](https://github.com/InternLM/lmdeploy/issues/4784)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#4785](https://github.com/InternLM/lmdeploy/pull/4785) - update anthropic endpoint test by
[@littlegy](https://github.com/littlegy)in[#4594](https://github.com/InternLM/lmdeploy/pull/4594) - Update multimodal toolcall tests by
[@littlegy](https://github.com/littlegy)in[#4742](https://github.com/InternLM/lmdeploy/pull/4742) - Remove obsolete C++ tests by
[@lzhangzz](https://github.com/lzhangzz)in[#4796](https://github.com/InternLM/lmdeploy/pull/4796) - [Docs] Fix typos in contribution guide by
[@cupkk](https://github.com/cupkk)in[#4807](https://github.com/InternLM/lmdeploy/pull/4807) - bump version to v0.15.0 by
[@lvhan028](https://github.com/lvhan028)in[#4791](https://github.com/InternLM/lmdeploy/pull/4791)

## New Contributors

[@kobihikri](https://github.com/kobihikri)made their first contribution in[#4748](https://github.com/InternLM/lmdeploy/pull/4748)[@Anai-Guo](https://github.com/Anai-Guo)made their first contribution in[#4785](https://github.com/InternLM/lmdeploy/pull/4785)[@cupkk](https://github.com/cupkk)made their first contribution in[#4807](https://github.com/InternLM/lmdeploy/pull/4807)

**Full Changelog**: `v0.14.0...v0.15.0`

## v0.14.0

## What's Changed

### 🚀 Features

- FP8 kv cache quantization by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4563](https://github.com/InternLM/lmdeploy/pull/4563) - Support Qwen3 Omni by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4411](https://github.com/InternLM/lmdeploy/pull/4411) - support qwen3.5(vit) inference in turbomind backend by
[@irexyc](https://github.com/irexyc)in[#4602](https://github.com/InternLM/lmdeploy/pull/4602) - Add OpenAI Responses-compatible endpoint by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4582](https://github.com/InternLM/lmdeploy/pull/4582) - Add /get_ppl endpoint by
[@irexyc](https://github.com/irexyc)in[#4679](https://github.com/InternLM/lmdeploy/pull/4679)

### 💥 Improvements

- Update turbomind modeling infrastructure by
[@lzhangzz](https://github.com/lzhangzz)in[#4557](https://github.com/InternLM/lmdeploy/pull/4557) - refactor(turbomind): consolidate CUDA error handling and add manual stacktracing by
[@lzhangzz](https://github.com/lzhangzz)in[#4565](https://github.com/InternLM/lmdeploy/pull/4565) - Add Qwen3.5 Moe lite awq by
[@43758726](https://github.com/43758726)in[#4561](https://github.com/InternLM/lmdeploy/pull/4561) - [Improve]: Drain queues when sleep engine by
[@RunningLeon](https://github.com/RunningLeon)in[#4577](https://github.com/InternLM/lmdeploy/pull/4577) - Extend chat completions by introducing token-in/out and returning routed experts by
[@lvhan028](https://github.com/lvhan028)in[#4593](https://github.com/InternLM/lmdeploy/pull/4593) - Follow openai's spec to add "AllowedToolChoice" and report 400 when parsing request failed by
[@lvhan028](https://github.com/lvhan028)in[#4585](https://github.com/InternLM/lmdeploy/pull/4585) - Improve health endpoint by
[@lvhan028](https://github.com/lvhan028)in[#4615](https://github.com/InternLM/lmdeploy/pull/4615) - Remove state init by
[@grimoire](https://github.com/grimoire)in[#4604](https://github.com/InternLM/lmdeploy/pull/4604) - Include spec stats in metrics by
[@RunningLeon](https://github.com/RunningLeon)in[#4625](https://github.com/InternLM/lmdeploy/pull/4625) - Add raw chat completion logprob output by
[@lvhan028](https://github.com/lvhan028)in[#4637](https://github.com/InternLM/lmdeploy/pull/4637) - fix(pytorch): offload guided decoding CPU ops to thread pool to prevent event loop blocking by
[@windreamer](https://github.com/windreamer)in[#4590](https://github.com/InternLM/lmdeploy/pull/4590) - update gated delta rule state layout by
[@grimoire](https://github.com/grimoire)in[#4636](https://github.com/InternLM/lmdeploy/pull/4636) - Improve kernel dispatch for dp>1 by
[@RunningLeon](https://github.com/RunningLeon)in[#4653](https://github.com/InternLM/lmdeploy/pull/4653) - Extend v1/messages by introducing token-in/out and returning routed experts by
[@lvhan028](https://github.com/lvhan028)in[#4642](https://github.com/InternLM/lmdeploy/pull/4642) - Fuse gdr preprocess by
[@grimoire](https://github.com/grimoire)in[#4656](https://github.com/InternLM/lmdeploy/pull/4656) - refactor: simplify multimodal preprocessing expansion by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4663](https://github.com/InternLM/lmdeploy/pull/4663) - feat: configure cudagraph capture batch sizes by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4573](https://github.com/InternLM/lmdeploy/pull/4573) - Refactor prefix caching for pytorch engine by
[@grimoire](https://github.com/grimoire)in[#4618](https://github.com/InternLM/lmdeploy/pull/4618) - Pading one more block for fa3 prefill by
[@RunningLeon](https://github.com/RunningLeon)in[#4674](https://github.com/InternLM/lmdeploy/pull/4674) - Add usage.prompt_tokens_details.cached_tokens for prefix caching by
[@lvhan028](https://github.com/lvhan028)in[#4670](https://github.com/InternLM/lmdeploy/pull/4670) - Optimize XML tool parsers with incremental streaming and fast-path buffering by
[@lvhan028](https://github.com/lvhan028)in[#4664](https://github.com/InternLM/lmdeploy/pull/4664)

### 🐞 Bug fixes

- fix the anthropic adapter by
[@lvhan028](https://github.com/lvhan028)in[#4578](https://github.com/InternLM/lmdeploy/pull/4578) - Fix Structured Output for GPT-OSS Models by
[@windreamer](https://github.com/windreamer)in[#4386](https://github.com/InternLM/lmdeploy/pull/4386) - Allow W8A8Linear to accept dtype during initialization instead of hard code by
[@43758726](https://github.com/43758726)in[#4586](https://github.com/InternLM/lmdeploy/pull/4586) - fix: compact split multimodal tensors by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4583](https://github.com/InternLM/lmdeploy/pull/4583) - Fix legacy VLM preprocessors for normalized image data by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4584](https://github.com/InternLM/lmdeploy/pull/4584) - fix dockerfile which missing common.txt by
[@lvhan028](https://github.com/lvhan028)in[#4608](https://github.com/InternLM/lmdeploy/pull/4608) - fix: enable FA3 for SM80+ GPUs and fix CUDA version comparison by
[@windreamer](https://github.com/windreamer)in[#4591](https://github.com/InternLM/lmdeploy/pull/4591) - flatten_kv_cache zero padding by
[@grimoire](https://github.com/grimoire)in[#4613](https://github.com/InternLM/lmdeploy/pull/4613) - align streaming usage chunks with OpenAI spec by
[@lvhan028](https://github.com/lvhan028)in[#4616](https://github.com/InternLM/lmdeploy/pull/4616) - fix(vl): reduce multimodal feature memory use by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4603](https://github.com/InternLM/lmdeploy/pull/4603) - fix memleak when input contain large image data by
[@grimoire](https://github.com/grimoire)in[#4610](https://github.com/InternLM/lmdeploy/pull/4610) - fix(turbomind): map Intern-S1 HF checkpoint keys by
[@lvhan028](https://github.com/lvhan028)in[#4617](https://github.com/InternLM/lmdeploy/pull/4617) - fix(serve): emit all stream_chunk deltas to fix concurrent tool-call streaming by
[@lvhan028](https://github.com/lvhan028)in[#4622](https://github.com/InternLM/lmdeploy/pull/4622) - fix cp inference by
[@irexyc](https://github.com/irexyc)in[#4619](https://github.com/InternLM/lmdeploy/pull/4619) - refactor(serve): avoid per-request tokenizer work in parsers by
[@lvhan028](https://github.com/lvhan028)in[#4633](https://github.com/InternLM/lmdeploy/pull/4633) - Bring MixtralForCausalLM back to Turbomind by
[@43758726](https://github.com/43758726)in[#4623](https://github.com/InternLM/lmdeploy/pull/4623) - fix model loading on windows by
[@irexyc](https://github.com/irexyc)in[#4626](https://github.com/InternLM/lmdeploy/pull/4626) - Fix mtp cudagraph when no warmup in RL by
[@RunningLeon](https://github.com/RunningLeon)in[#4641](https://github.com/InternLM/lmdeploy/pull/4641) - fix: remove hard CUDA_PATH assert on Windows, search DLL paths from multiple sources by
[@windreamer](https://github.com/windreamer)in[#4628](https://github.com/InternLM/lmdeploy/pull/4628) - Fix unit test by removing latest-transformers-unsupported models by
[@lvhan028](https://github.com/lvhan028)in[#4649](https://github.com/InternLM/lmdeploy/pull/4649) - Fix qwen3.5 mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4652](https://github.com/InternLM/lmdeploy/pull/4652) - fix gdr kernel for tilelang>=0.1.9 by
[@grimoire](https://github.com/grimoire)in[#4660](https://github.com/InternLM/lmdeploy/pull/4660) - [Fix]: Revert the reuse of cudagraph buffer for mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4661](https://github.com/InternLM/lmdeploy/pull/4661) - Fix client-disconnect session leaks in PyTorch MP engine by
[@grimoire](https://github.com/grimoire)in[#4655](https://github.com/InternLM/lmdeploy/pull/4655) - fix cancel stopped seq by
[@RunningLeon](https://github.com/RunningLeon)in[#4654](https://github.com/InternLM/lmdeploy/pull/4654) - feat: support num_experts_per_tok=10 in turbomind backend by
[@irexyc](https://github.com/irexyc)in[#4665](https://github.com/InternLM/lmdeploy/pull/4665) - fix batched seqs with different stop words by
[@RunningLeon](https://github.com/RunningLeon)in[#4671](https://github.com/InternLM/lmdeploy/pull/4671) - Move warmup inside wakeup by
[@RunningLeon](https://github.com/RunningLeon)in[#4667](https://github.com/InternLM/lmdeploy/pull/4667) - Fix dequant_mixed by
[@irexyc](https://github.com/irexyc)in[#4657](https://github.com/InternLM/lmdeploy/pull/4657) - Improve engine health monitoring by
[@lvhan028](https://github.com/lvhan028)in[#4645](https://github.com/InternLM/lmdeploy/pull/4645) - fix qwen3.5 27b gdr preprocess by
[@grimoire](https://github.com/grimoire)in[#4676](https://github.com/InternLM/lmdeploy/pull/4676) - Fix dequant mixed for qwen3.5 quantized model made by vllm/llm-compressor by
[@irexyc](https://github.com/irexyc)in[#4675](https://github.com/InternLM/lmdeploy/pull/4675) - [Bugfix] Fix double-counted max_q_seqlen in decode delta kv_seqlens by
[@waynehacking8](https://github.com/waynehacking8)in[#4685](https://github.com/InternLM/lmdeploy/pull/4685) - Fix scheduler for ssm by
[@RunningLeon](https://github.com/RunningLeon)in[#4691](https://github.com/InternLM/lmdeploy/pull/4691) - fix(serve): avoid parallel tool-call argument leakage in XML parsers by
[@lvhan028](https://github.com/lvhan028)in[#4692](https://github.com/InternLM/lmdeploy/pull/4692) - fix prefix caching by
[@grimoire](https://github.com/grimoire)in[#4700](https://github.com/InternLM/lmdeploy/pull/4700)

### 📚 Documentations

- docs: update multimodal model support docs by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4643](https://github.com/InternLM/lmdeploy/pull/4643)

### 🌐 Other

- chore: gate request logs behind request level by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4581](https://github.com/InternLM/lmdeploy/pull/4581) - miss rdkit for intern-s models by
[@lvhan028](https://github.com/lvhan028)in[#4587](https://github.com/InternLM/lmdeploy/pull/4587) - extract common deps into requirements/common.txt by
[@lvhan028](https://github.com/lvhan028)in[#4595](https://github.com/InternLM/lmdeploy/pull/4595) - Remove staled cli arg in vlmevalkit docs by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4598](https://github.com/InternLM/lmdeploy/pull/4598) - log reponse for debugging by
[@lvhan028](https://github.com/lvhan028)in[#4592](https://github.com/InternLM/lmdeploy/pull/4592) - cancel in-progress runs when PR is updated or merged by
[@lvhan028](https://github.com/lvhan028)in[#4609](https://github.com/InternLM/lmdeploy/pull/4609) - TEST: update qwen3.5 397b test by
[@littlegy](https://github.com/littlegy)in[#4607](https://github.com/InternLM/lmdeploy/pull/4607) - TEST: update video test by
[@littlegy](https://github.com/littlegy)in[#4606](https://github.com/InternLM/lmdeploy/pull/4606) - Validate final chat response structure by
[@lvhan028](https://github.com/lvhan028)in[#4621](https://github.com/InternLM/lmdeploy/pull/4621) - Support dp for qwen35 mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4611](https://github.com/InternLM/lmdeploy/pull/4611) - [ci] refactor testcoverage config by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4630](https://github.com/InternLM/lmdeploy/pull/4630) - TEST: update ascend and mtp test config by
[@littlegy](https://github.com/littlegy)in[#4659](https://github.com/InternLM/lmdeploy/pull/4659) - TEST: update FP8 processing logic and remove duplicate MTP tests by
[@littlegy](https://github.com/littlegy)in[#4668](https://github.com/InternLM/lmdeploy/pull/4668) - freeze tilelang version by
[@grimoire](https://github.com/grimoire)in[#4669](https://github.com/InternLM/lmdeploy/pull/4669) - fix windows ci by
[@irexyc](https://github.com/irexyc)in[#4672](https://github.com/InternLM/lmdeploy/pull/4672) - [ci] add mtp test config in pr_test by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4651](https://github.com/InternLM/lmdeploy/pull/4651) - support disaggregated weight update by
[@irexyc](https://github.com/irexyc)in[#4638](https://github.com/InternLM/lmdeploy/pull/4638) - bump version to v0.14.0 by
[@lvhan028](https://github.com/lvhan028)in[#4689](https://github.com/InternLM/lmdeploy/pull/4689)

## New Contributors

[@waynehacking8](https://github.com/waynehacking8)made their first contribution in[#4685](https://github.com/InternLM/lmdeploy/pull/4685)

**Full Changelog**: `v0.13.0...v0.14.0`

## v0.14.0a2

## What's Changed

### 🚀 Features

- FP8 kv cache quantization by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4563](https://github.com/InternLM/lmdeploy/pull/4563) - Support Qwen3 Omni by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4411](https://github.com/InternLM/lmdeploy/pull/4411) - support qwen3.5(vit) inference in turbomind backend by
[@irexyc](https://github.com/irexyc)in[#4602](https://github.com/InternLM/lmdeploy/pull/4602) - Add OpenAI Responses-compatible endpoint by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4582](https://github.com/InternLM/lmdeploy/pull/4582)

### 💥 Improvements

- Update turbomind modeling infrastructure by
[@lzhangzz](https://github.com/lzhangzz)in[#4557](https://github.com/InternLM/lmdeploy/pull/4557) - refactor(turbomind): consolidate CUDA error handling and add manual stacktracing by
[@lzhangzz](https://github.com/lzhangzz)in[#4565](https://github.com/InternLM/lmdeploy/pull/4565) - Add Qwen3.5 Moe lite awq by
[@43758726](https://github.com/43758726)in[#4561](https://github.com/InternLM/lmdeploy/pull/4561) - [Improve]: Drain queues when sleep engine by
[@RunningLeon](https://github.com/RunningLeon)in[#4577](https://github.com/InternLM/lmdeploy/pull/4577) - Extend chat completions by introducing token-in/out and returning routed experts by
[@lvhan028](https://github.com/lvhan028)in[#4593](https://github.com/InternLM/lmdeploy/pull/4593) - Follow openai's spec to add "AllowedToolChoice" and report 400 when parsing request failed by
[@lvhan028](https://github.com/lvhan028)in[#4585](https://github.com/InternLM/lmdeploy/pull/4585) - Improve health endpoint by
[@lvhan028](https://github.com/lvhan028)in[#4615](https://github.com/InternLM/lmdeploy/pull/4615) - Remove state init by
[@grimoire](https://github.com/grimoire)in[#4604](https://github.com/InternLM/lmdeploy/pull/4604) - Include spec stats in metrics by
[@RunningLeon](https://github.com/RunningLeon)in[#4625](https://github.com/InternLM/lmdeploy/pull/4625) - Add raw chat completion logprob output by
[@lvhan028](https://github.com/lvhan028)in[#4637](https://github.com/InternLM/lmdeploy/pull/4637) - fix(pytorch): offload guided decoding CPU ops to thread pool to prevent event loop blocking by
[@windreamer](https://github.com/windreamer)in[#4590](https://github.com/InternLM/lmdeploy/pull/4590) - update gated delta rule state layout by
[@grimoire](https://github.com/grimoire)in[#4636](https://github.com/InternLM/lmdeploy/pull/4636) - Improve kernel dispatch for dp>1 by
[@RunningLeon](https://github.com/RunningLeon)in[#4653](https://github.com/InternLM/lmdeploy/pull/4653) - Extend v1/messages by introducing token-in/out and returning routed experts by
[@lvhan028](https://github.com/lvhan028)in[#4642](https://github.com/InternLM/lmdeploy/pull/4642) - Fuse gdr preprocess by
[@grimoire](https://github.com/grimoire)in[#4656](https://github.com/InternLM/lmdeploy/pull/4656) - refactor: simplify multimodal preprocessing expansion by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4663](https://github.com/InternLM/lmdeploy/pull/4663)

### 🐞 Bug fixes

- fix the anthropic adapter by
[@lvhan028](https://github.com/lvhan028)in[#4578](https://github.com/InternLM/lmdeploy/pull/4578) - Fix Structured Output for GPT-OSS Models by
[@windreamer](https://github.com/windreamer)in[#4386](https://github.com/InternLM/lmdeploy/pull/4386) - Allow W8A8Linear to accept dtype during initialization instead of hard code by
[@43758726](https://github.com/43758726)in[#4586](https://github.com/InternLM/lmdeploy/pull/4586) - fix: compact split multimodal tensors by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4583](https://github.com/InternLM/lmdeploy/pull/4583) - Fix legacy VLM preprocessors for normalized image data by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4584](https://github.com/InternLM/lmdeploy/pull/4584) - fix dockerfile which missing common.txt by
[@lvhan028](https://github.com/lvhan028)in[#4608](https://github.com/InternLM/lmdeploy/pull/4608) - fix: enable FA3 for SM80+ GPUs and fix CUDA version comparison by
[@windreamer](https://github.com/windreamer)in[#4591](https://github.com/InternLM/lmdeploy/pull/4591) - flatten_kv_cache zero padding by
[@grimoire](https://github.com/grimoire)in[#4613](https://github.com/InternLM/lmdeploy/pull/4613) - align streaming usage chunks with OpenAI spec by
[@lvhan028](https://github.com/lvhan028)in[#4616](https://github.com/InternLM/lmdeploy/pull/4616) - fix(vl): reduce multimodal feature memory use by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4603](https://github.com/InternLM/lmdeploy/pull/4603) - fix memleak when input contain large image data by
[@grimoire](https://github.com/grimoire)in[#4610](https://github.com/InternLM/lmdeploy/pull/4610) - fix(turbomind): map Intern-S1 HF checkpoint keys by
[@lvhan028](https://github.com/lvhan028)in[#4617](https://github.com/InternLM/lmdeploy/pull/4617) - fix(serve): emit all stream_chunk deltas to fix concurrent tool-call streaming by
[@lvhan028](https://github.com/lvhan028)in[#4622](https://github.com/InternLM/lmdeploy/pull/4622) - fix cp inference by
[@irexyc](https://github.com/irexyc)in[#4619](https://github.com/InternLM/lmdeploy/pull/4619) - refactor(serve): avoid per-request tokenizer work in parsers by
[@lvhan028](https://github.com/lvhan028)in[#4633](https://github.com/InternLM/lmdeploy/pull/4633) - Bring MixtralForCausalLM back to Turbomind by
[@43758726](https://github.com/43758726)in[#4623](https://github.com/InternLM/lmdeploy/pull/4623) - fix model loading on windows by
[@irexyc](https://github.com/irexyc)in[#4626](https://github.com/InternLM/lmdeploy/pull/4626) - Fix mtp cudagraph when no warmup in RL by
[@RunningLeon](https://github.com/RunningLeon)in[#4641](https://github.com/InternLM/lmdeploy/pull/4641) - fix: remove hard CUDA_PATH assert on Windows, search DLL paths from multiple sources by
[@windreamer](https://github.com/windreamer)in[#4628](https://github.com/InternLM/lmdeploy/pull/4628) - Fix unit test by removing latest-transformers-unsupported models by
[@lvhan028](https://github.com/lvhan028)in[#4649](https://github.com/InternLM/lmdeploy/pull/4649) - Fix qwen3.5 mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4652](https://github.com/InternLM/lmdeploy/pull/4652) - fix gdr kernel for tilelang>=0.1.9 by
[@grimoire](https://github.com/grimoire)in[#4660](https://github.com/InternLM/lmdeploy/pull/4660) - [Fix]: Revert the reuse of cudagraph buffer for mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4661](https://github.com/InternLM/lmdeploy/pull/4661) - Fix client-disconnect session leaks in PyTorch MP engine by
[@grimoire](https://github.com/grimoire)in[#4655](https://github.com/InternLM/lmdeploy/pull/4655) - fix cancel stopped seq by
[@RunningLeon](https://github.com/RunningLeon)in[#4654](https://github.com/InternLM/lmdeploy/pull/4654) - feat: support num_experts_per_tok=10 in turbomind backend by
[@irexyc](https://github.com/irexyc)in[#4665](https://github.com/InternLM/lmdeploy/pull/4665) - fix batched seqs with different stop words by
[@RunningLeon](https://github.com/RunningLeon)in[#4671](https://github.com/InternLM/lmdeploy/pull/4671) - Move warmup inside wakeup by
[@RunningLeon](https://github.com/RunningLeon)in[#4667](https://github.com/InternLM/lmdeploy/pull/4667) - Fix dequant_mixed by
[@irexyc](https://github.com/irexyc)in[#4657](https://github.com/InternLM/lmdeploy/pull/4657) - Improve engine health monitoring by
[@lvhan028](https://github.com/lvhan028)in[#4645](https://github.com/InternLM/lmdeploy/pull/4645) - fix qwen3.5 27b gdr preprocess by
[@grimoire](https://github.com/grimoire)in[#4676](https://github.com/InternLM/lmdeploy/pull/4676)

### 📚 Documentations

- docs: update multimodal model support docs by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4643](https://github.com/InternLM/lmdeploy/pull/4643)

### 🌐 Other

- chore: gate request logs behind request level by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4581](https://github.com/InternLM/lmdeploy/pull/4581) - miss rdkit for intern-s models by
[@lvhan028](https://github.com/lvhan028)in[#4587](https://github.com/InternLM/lmdeploy/pull/4587) - extract common deps into requirements/common.txt by
[@lvhan028](https://github.com/lvhan028)in[#4595](https://github.com/InternLM/lmdeploy/pull/4595) - Remove staled cli arg in vlmevalkit docs by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4598](https://github.com/InternLM/lmdeploy/pull/4598) - log reponse for debugging by
[@lvhan028](https://github.com/lvhan028)in[#4592](https://github.com/InternLM/lmdeploy/pull/4592) - cancel in-progress runs when PR is updated or merged by
[@lvhan028](https://github.com/lvhan028)in[#4609](https://github.com/InternLM/lmdeploy/pull/4609) - TEST: update qwen3.5 397b test by
[@littlegy](https://github.com/littlegy)in[#4607](https://github.com/InternLM/lmdeploy/pull/4607) - TEST: update video test by
[@littlegy](https://github.com/littlegy)in[#4606](https://github.com/InternLM/lmdeploy/pull/4606) - Validate final chat response structure by
[@lvhan028](https://github.com/lvhan028)in[#4621](https://github.com/InternLM/lmdeploy/pull/4621) - Support dp for qwen35 mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4611](https://github.com/InternLM/lmdeploy/pull/4611) - [ci] refactor testcoverage config by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4630](https://github.com/InternLM/lmdeploy/pull/4630) - TEST: update ascend and mtp test config by
[@littlegy](https://github.com/littlegy)in[#4659](https://github.com/InternLM/lmdeploy/pull/4659) - TEST: update FP8 processing logic and remove duplicate MTP tests by
[@littlegy](https://github.com/littlegy)in[#4668](https://github.com/InternLM/lmdeploy/pull/4668) - freeze tilelang version by
[@grimoire](https://github.com/grimoire)in[#4669](https://github.com/InternLM/lmdeploy/pull/4669) - fix windows ci by
[@irexyc](https://github.com/irexyc)in[#4672](https://github.com/InternLM/lmdeploy/pull/4672) - [ci] add mtp test config in pr_test by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4651](https://github.com/InternLM/lmdeploy/pull/4651)

**Full Changelog**: `v0.13.0...0.14.0a2`

## v0.14.0a1

## What's Changed

### 🚀 Features

- FP8 kv cache quantization by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4563](https://github.com/InternLM/lmdeploy/pull/4563)

### 💥 Improvements

- Update turbomind modeling infrastructure by
[@lzhangzz](https://github.com/lzhangzz)in[#4557](https://github.com/InternLM/lmdeploy/pull/4557) - refactor(turbomind): consolidate CUDA error handling and add manual stacktracing by
[@lzhangzz](https://github.com/lzhangzz)in[#4565](https://github.com/InternLM/lmdeploy/pull/4565) - Add Qwen3.5 Moe lite awq by
[@43758726](https://github.com/43758726)in[#4561](https://github.com/InternLM/lmdeploy/pull/4561) - [Improve]: Drain queues when sleep engine by
[@RunningLeon](https://github.com/RunningLeon)in[#4577](https://github.com/InternLM/lmdeploy/pull/4577) - Extend chat completions by introducing token-in/out and returning routed experts by
[@lvhan028](https://github.com/lvhan028)in[#4593](https://github.com/InternLM/lmdeploy/pull/4593) - Follow openai's spec to add "AllowedToolChoice" and report 400 when parsing request failed by
[@lvhan028](https://github.com/lvhan028)in[#4585](https://github.com/InternLM/lmdeploy/pull/4585) - Improve health endpoint by
[@lvhan028](https://github.com/lvhan028)in[#4615](https://github.com/InternLM/lmdeploy/pull/4615) - Remove state init by
[@grimoire](https://github.com/grimoire)in[#4604](https://github.com/InternLM/lmdeploy/pull/4604) - Include spec stats in metrics by
[@RunningLeon](https://github.com/RunningLeon)in[#4625](https://github.com/InternLM/lmdeploy/pull/4625)

### 🐞 Bug fixes

- fix the anthropic adapter by
[@lvhan028](https://github.com/lvhan028)in[#4578](https://github.com/InternLM/lmdeploy/pull/4578) - Fix Structured Output for GPT-OSS Models by
[@windreamer](https://github.com/windreamer)in[#4386](https://github.com/InternLM/lmdeploy/pull/4386) - Allow W8A8Linear to accept dtype during initialization instead of hard code by
[@43758726](https://github.com/43758726)in[#4586](https://github.com/InternLM/lmdeploy/pull/4586) - fix: compact split multimodal tensors by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4583](https://github.com/InternLM/lmdeploy/pull/4583) - Fix legacy VLM preprocessors for normalized image data by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4584](https://github.com/InternLM/lmdeploy/pull/4584) - fix dockerfile which missing common.txt by
[@lvhan028](https://github.com/lvhan028)in[#4608](https://github.com/InternLM/lmdeploy/pull/4608) - fix: enable FA3 for SM80+ GPUs and fix CUDA version comparison by
[@windreamer](https://github.com/windreamer)in[#4591](https://github.com/InternLM/lmdeploy/pull/4591) - flatten_kv_cache zero padding by
[@grimoire](https://github.com/grimoire)in[#4613](https://github.com/InternLM/lmdeploy/pull/4613) - align streaming usage chunks with OpenAI spec by
[@lvhan028](https://github.com/lvhan028)in[#4616](https://github.com/InternLM/lmdeploy/pull/4616) - fix(vl): reduce multimodal feature memory use by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4603](https://github.com/InternLM/lmdeploy/pull/4603) - fix memleak when input contain large image data by
[@grimoire](https://github.com/grimoire)in[#4610](https://github.com/InternLM/lmdeploy/pull/4610) - fix(turbomind): map Intern-S1 HF checkpoint keys by
[@lvhan028](https://github.com/lvhan028)in[#4617](https://github.com/InternLM/lmdeploy/pull/4617) - fix(serve): emit all stream_chunk deltas to fix concurrent tool-call streaming by
[@lvhan028](https://github.com/lvhan028)in[#4622](https://github.com/InternLM/lmdeploy/pull/4622) - fix cp inference by
[@irexyc](https://github.com/irexyc)in[#4619](https://github.com/InternLM/lmdeploy/pull/4619) - refactor(serve): avoid per-request tokenizer work in parsers by
[@lvhan028](https://github.com/lvhan028)in[#4633](https://github.com/InternLM/lmdeploy/pull/4633) - Bring MixtralForCausalLM back to Turbomind by
[@43758726](https://github.com/43758726)in[#4623](https://github.com/InternLM/lmdeploy/pull/4623) - fix model loading on windows by
[@irexyc](https://github.com/irexyc)in[#4626](https://github.com/InternLM/lmdeploy/pull/4626)

### 🌐 Other

- chore: gate request logs behind request level by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4581](https://github.com/InternLM/lmdeploy/pull/4581) - miss rdkit for intern-s models by
[@lvhan028](https://github.com/lvhan028)in[#4587](https://github.com/InternLM/lmdeploy/pull/4587) - extract common deps into requirements/common.txt by
[@lvhan028](https://github.com/lvhan028)in[#4595](https://github.com/InternLM/lmdeploy/pull/4595) - Remove staled cli arg in vlmevalkit docs by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4598](https://github.com/InternLM/lmdeploy/pull/4598) - log reponse for debugging by
[@lvhan028](https://github.com/lvhan028)in[#4592](https://github.com/InternLM/lmdeploy/pull/4592) - cancel in-progress runs when PR is updated or merged by
[@lvhan028](https://github.com/lvhan028)in[#4609](https://github.com/InternLM/lmdeploy/pull/4609) - TEST: update qwen3.5 397b test by
[@littlegy](https://github.com/littlegy)in[#4607](https://github.com/InternLM/lmdeploy/pull/4607) - TEST: update video test by
[@littlegy](https://github.com/littlegy)in[#4606](https://github.com/InternLM/lmdeploy/pull/4606)

**Full Changelog**: `v0.13.0...0.14.0a1`

## v0.13.0

## What's Changed

### 🚀 Features

- [Ascend] support qwen3.5 35BA3B by
[@wanfengcxz](https://github.com/wanfengcxz)in[#4485](https://github.com/InternLM/lmdeploy/pull/4485) - feat: Add TurboQuant (quant_policy=42) support for KV Cache Quantization by
[@windreamer](https://github.com/windreamer)in[#4510](https://github.com/InternLM/lmdeploy/pull/4510) - [refactor] [api_server] [2/N] improve tool parsers by abstracting xml parser by
[@lvhan028](https://github.com/lvhan028)in[#4548](https://github.com/InternLM/lmdeploy/pull/4548) - feat(turbomind): integrate cublasGemmGroupedBatchedEx for Qwen3.5 MoE inference on Blackwell GPUs with memory copy optimizations by
[@hd9568](https://github.com/hd9568)in[#4490](https://github.com/InternLM/lmdeploy/pull/4490) - feat: add Anthropic-compatible serving endpoints by
[@lvhan028](https://github.com/lvhan028)in[#4538](https://github.com/InternLM/lmdeploy/pull/4538) - Support InternS2 Preview by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4575](https://github.com/InternLM/lmdeploy/pull/4575)

### 💥 Improvements

- lmdeploy support kernel block size by
[@Tsundoku958](https://github.com/Tsundoku958)in[#4421](https://github.com/InternLM/lmdeploy/pull/4421) - Reject requests on stale session or sleeping engine by
[@lvhan028](https://github.com/lvhan028)in[#4496](https://github.com/InternLM/lmdeploy/pull/4496) - Add modern logging utils by
[@lzhangzz](https://github.com/lzhangzz)in[#4486](https://github.com/InternLM/lmdeploy/pull/4486) - refine dlinfer update_weights by
[@yao-fengchen](https://github.com/yao-fengchen)in[#4519](https://github.com/InternLM/lmdeploy/pull/4519) - feat(serve): expose repetition n-gram params on OpenAI routes by
[@lvhan028](https://github.com/lvhan028)in[#4522](https://github.com/InternLM/lmdeploy/pull/4522) - Refactor step inputs by
[@grimoire](https://github.com/grimoire)in[#4504](https://github.com/InternLM/lmdeploy/pull/4504) - fix lite module for transformers>=5.0 by
[@43758726](https://github.com/43758726)in[#4488](https://github.com/InternLM/lmdeploy/pull/4488) - [refactor] [api_server] [1/N] Improve reasoning and tool-call parsers by
[@lvhan028](https://github.com/lvhan028)in[#4468](https://github.com/InternLM/lmdeploy/pull/4468) - fix: prevent prefill starvation under high decode load by
[@grimoire](https://github.com/grimoire)in[#4532](https://github.com/InternLM/lmdeploy/pull/4532) - Mixed modality by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4531](https://github.com/InternLM/lmdeploy/pull/4531) - optimize get_sorted_idx in moe by
[@grimoire](https://github.com/grimoire)in[#4529](https://github.com/InternLM/lmdeploy/pull/4529) - Map user-input session_id to internal session_id to maintain session identity by
[@lvhan028](https://github.com/lvhan028)in[#4523](https://github.com/InternLM/lmdeploy/pull/4523) - support more message item types by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4501](https://github.com/InternLM/lmdeploy/pull/4501) - add explicit trust_remote_code controls to resolve the security issue by
[@lvhan028](https://github.com/lvhan028)in[#4511](https://github.com/InternLM/lmdeploy/pull/4511)

### 🐞 Bug fixes

- [ascend] fix prefix caching by
[@yao-fengchen](https://github.com/yao-fengchen)in[#4448](https://github.com/InternLM/lmdeploy/pull/4448) - fix update params by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4514](https://github.com/InternLM/lmdeploy/pull/4514) - fix ray mem leak by
[@grimoire](https://github.com/grimoire)in[#4487](https://github.com/InternLM/lmdeploy/pull/4487) - Fix mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4517](https://github.com/InternLM/lmdeploy/pull/4517) - fix kernel-block-size by
[@grimoire](https://github.com/grimoire)in[#4521](https://github.com/InternLM/lmdeploy/pull/4521) - fix: use
`is not None`

check for seed to prevent seed=0 being silently ignored by[@kuishou68](https://github.com/kuishou68)in[#4526](https://github.com/InternLM/lmdeploy/pull/4526) - Fix qwen35 dp by
[@grimoire](https://github.com/grimoire)in[#4535](https://github.com/InternLM/lmdeploy/pull/4535) - Fix mtp for rl by
[@RunningLeon](https://github.com/RunningLeon)in[#4520](https://github.com/InternLM/lmdeploy/pull/4520) - cancel request and block new inputs when sleeping by
[@grimoire](https://github.com/grimoire)in[#4541](https://github.com/InternLM/lmdeploy/pull/4541) - Fix mp engine by
[@RunningLeon](https://github.com/RunningLeon)in[#4540](https://github.com/InternLM/lmdeploy/pull/4540) - Fix cache sizing and cache block layout edge cases by
[@grimoire](https://github.com/grimoire)in[#4552](https://github.com/InternLM/lmdeploy/pull/4552) - Fix qwen3.5-moe mtp with tp>1 by
[@RunningLeon](https://github.com/RunningLeon)in[#4568](https://github.com/InternLM/lmdeploy/pull/4568) - block_offsets padding 0 by
[@grimoire](https://github.com/grimoire)in[#4569](https://github.com/InternLM/lmdeploy/pull/4569) - hotfix: resolve test issues for v0.13.0 by
[@lvhan028](https://github.com/lvhan028)in[#4571](https://github.com/InternLM/lmdeploy/pull/4571) - ResponseParser forget to strip tag in non-stream mode by
[@lvhan028](https://github.com/lvhan028)in[#4576](https://github.com/InternLM/lmdeploy/pull/4576) - yield error when prompt processing suffers exception by
[@lvhan028](https://github.com/lvhan028)in[#4574](https://github.com/InternLM/lmdeploy/pull/4574) - Fix the reprefill of evicted seqs with invalid draft tokens by
[@RunningLeon](https://github.com/RunningLeon)in[#4564](https://github.com/InternLM/lmdeploy/pull/4564) - Support mtp fp8 by
[@RunningLeon](https://github.com/RunningLeon)in[#4572](https://github.com/InternLM/lmdeploy/pull/4572)

### 🌐 Other

- Use env LMDEPLOY_FP32_MAMBA_SSM_DTYPE to control the dtype of recurrent state by
[@lvhan028](https://github.com/lvhan028)in[#4518](https://github.com/InternLM/lmdeploy/pull/4518) - add tool and reasoning test by
[@littlegy](https://github.com/littlegy)in[#4388](https://github.com/InternLM/lmdeploy/pull/4388) - update h config and add glm4.7 mtp test by
[@littlegy](https://github.com/littlegy)in[#4424](https://github.com/InternLM/lmdeploy/pull/4424) - [ci] change test whl into python 312 and use test images by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4513](https://github.com/InternLM/lmdeploy/pull/4513) - [Misc] fix typos in turbomind.py and model.py by
[@ZhijunLStudio](https://github.com/ZhijunLStudio)in[#4543](https://github.com/InternLM/lmdeploy/pull/4543) - [Misc] fix mutable default arguments by
[@ZhijunLStudio](https://github.com/ZhijunLStudio)in[#4544](https://github.com/InternLM/lmdeploy/pull/4544) - Add docker/Dockerfile_patch; minor tweaks in messages.py and setup.py. by
[@lvhan028](https://github.com/lvhan028)in[#4546](https://github.com/InternLM/lmdeploy/pull/4546) - remove barely used skills and checkin docker-build skill by
[@lvhan028](https://github.com/lvhan028)in[#4560](https://github.com/InternLM/lmdeploy/pull/4560) - bump version to v0.13.0 by
[@lvhan028](https://github.com/lvhan028)in[#4549](https://github.com/InternLM/lmdeploy/pull/4549)

## New Contributors

[@kuishou68](https://github.com/kuishou68)made their first contribution in[#4526](https://github.com/InternLM/lmdeploy/pull/4526)[@ZhijunLStudio](https://github.com/ZhijunLStudio)made their first contribution in[#4543](https://github.com/InternLM/lmdeploy/pull/4543)[@hd9568](https://github.com/hd9568)made their first contribution in[#4490](https://github.com/InternLM/lmdeploy/pull/4490)

**Full Changelog**: `v0.12.3...v0.13.0`

## v0.12.3

## What's Changed

### 🚀 Features

- Support video inputs by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4360](https://github.com/InternLM/lmdeploy/pull/4360) - feat: fully implement compressed-tensors gs32 support in TurboMind by
[@lapy](https://github.com/lapy)in[#4429](https://github.com/InternLM/lmdeploy/pull/4429) - Draft model update params by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4452](https://github.com/InternLM/lmdeploy/pull/4452)

### 💥 Improvements

- support qwen3.5 on volta by
[@grimoire](https://github.com/grimoire)in[#4405](https://github.com/InternLM/lmdeploy/pull/4405) - Optimize Qwen3.5 by
[@lzhangzz](https://github.com/lzhangzz)in[#4434](https://github.com/InternLM/lmdeploy/pull/4434) - Builtin mrope by
[@grimoire](https://github.com/grimoire)in[#4393](https://github.com/InternLM/lmdeploy/pull/4393) - delete ray remote function return value by
[@grimoire](https://github.com/grimoire)in[#4422](https://github.com/InternLM/lmdeploy/pull/4422) - support cache_seqlen on recurrent-gdr and causal-conv1d-update by
[@grimoire](https://github.com/grimoire)in[#4417](https://github.com/InternLM/lmdeploy/pull/4417) - safe ray api by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4455](https://github.com/InternLM/lmdeploy/pull/4455) - add R3 for qwen3-vl-moe models by
[@lvhan028](https://github.com/lvhan028)in[#4457](https://github.com/InternLM/lmdeploy/pull/4457) - Align rope init in lmdeploy by
[@RangiLyu](https://github.com/RangiLyu)in[#4466](https://github.com/InternLM/lmdeploy/pull/4466) - Make tilelang a Linux-only dependency (like triton) by @Copilot in
[#4469](https://github.com/InternLM/lmdeploy/pull/4469) - prepare chunk indices before cache initialize by
[@grimoire](https://github.com/grimoire)in[#4458](https://github.com/InternLM/lmdeploy/pull/4458) - unify rope device by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4467](https://github.com/InternLM/lmdeploy/pull/4467) - custom processor args by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4472](https://github.com/InternLM/lmdeploy/pull/4472) - Assign sequential api_server ports when proxy_url is unset by
[@lvhan028](https://github.com/lvhan028)in[#4416](https://github.com/InternLM/lmdeploy/pull/4416) - disable fla intracard_backend by
[@grimoire](https://github.com/grimoire)in[#4482](https://github.com/InternLM/lmdeploy/pull/4482) - [Fix][Feat] Fix worker sorting with external pg bundles & Support persistent buffer for update_params by
[@CyCle1024](https://github.com/CyCle1024)in[#4397](https://github.com/InternLM/lmdeploy/pull/4397) - simplify interns1 pro codes by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4480](https://github.com/InternLM/lmdeploy/pull/4480)

### 🐞 Bug fixes

- fix test_hf_overrides for transformers>5 by
[@grimoire](https://github.com/grimoire)in[#4418](https://github.com/InternLM/lmdeploy/pull/4418) - fix qwen3.5 pytorch multimodal inference by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4430](https://github.com/InternLM/lmdeploy/pull/4430) - fix
`generate`

endpoint by[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4432](https://github.com/InternLM/lmdeploy/pull/4432) - Make Intern-S1-Pro compatible with Transformers 5.0+ by
[@lvhan028](https://github.com/lvhan028)in[#4435](https://github.com/InternLM/lmdeploy/pull/4435) - fix multiround chat by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4438](https://github.com/InternLM/lmdeploy/pull/4438) - fix(async_engine): make safe_run cancellation cleanup reliable with shield and SafeRunException by
[@lvhan028](https://github.com/lvhan028)in[#4439](https://github.com/InternLM/lmdeploy/pull/4439) - release state cache by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4462](https://github.com/InternLM/lmdeploy/pull/4462) - Split/tool call args json for qwen3coder tool calls (Qwen3.5) by
[@lapy](https://github.com/lapy)in[#4433](https://github.com/InternLM/lmdeploy/pull/4433) - fix(turbomind): fix dimension mismatch in ApplyTokenBitmaskInplace by
[@windreamer](https://github.com/windreamer)in[#4456](https://github.com/InternLM/lmdeploy/pull/4456) - fix metrics by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4410](https://github.com/InternLM/lmdeploy/pull/4410) - fix security issues by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4447](https://github.com/InternLM/lmdeploy/pull/4447) - fix qwen3.5 fp8 support by
[@grimoire](https://github.com/grimoire)in[#4470](https://github.com/InternLM/lmdeploy/pull/4470) - fix image / video resize function by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4478](https://github.com/InternLM/lmdeploy/pull/4478) - fix dynamic ntk device by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4483](https://github.com/InternLM/lmdeploy/pull/4483) - fix pagedattention pointer range by
[@grimoire](https://github.com/grimoire)in[#4494](https://github.com/InternLM/lmdeploy/pull/4494) - fix glm4.7-flash by
[@grimoire](https://github.com/grimoire)in[#4500](https://github.com/InternLM/lmdeploy/pull/4500) - Fix torch awq by
[@grimoire](https://github.com/grimoire)in[#4503](https://github.com/InternLM/lmdeploy/pull/4503)

### 🌐 Other

- [ci] add legacy test workflow and test config by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4387](https://github.com/InternLM/lmdeploy/pull/4387) - chore: add CLAUDE.md and Claude Code skills by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4413](https://github.com/InternLM/lmdeploy/pull/4413) - Fix CI errors including linting error and unit test error by
[@lvhan028](https://github.com/lvhan028)in[#4431](https://github.com/InternLM/lmdeploy/pull/4431) - Use pyupgrade and ruff to modernize LMDeploy Python Code by
[@windreamer](https://github.com/windreamer)in[#4392](https://github.com/InternLM/lmdeploy/pull/4392) - reduce ci memory by
[@irexyc](https://github.com/irexyc)in[#4471](https://github.com/InternLM/lmdeploy/pull/4471) - fix: add safe.directory for git in docker workflows by
[@windreamer](https://github.com/windreamer)in[#4474](https://github.com/InternLM/lmdeploy/pull/4474) - [ci] add nightly docker build workflow by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4406](https://github.com/InternLM/lmdeploy/pull/4406) - split docker wheel preparation into staged build steps and use python 3.12 as the default version by
[@lvhan028](https://github.com/lvhan028)in[#4476](https://github.com/InternLM/lmdeploy/pull/4476) - [Feat]: Support qwen35 with mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4437](https://github.com/InternLM/lmdeploy/pull/4437) - bump version to v0.12.3 by
[@lvhan028](https://github.com/lvhan028)in[#4493](https://github.com/InternLM/lmdeploy/pull/4493)

## New Contributors

**Full Changelog**: `v0.12.2...v0.12.3`

## v0.12.2

## What's Changed

### 🚀 Features

- support glm5 by
[@grimoire](https://github.com/grimoire)in[#4355](https://github.com/InternLM/lmdeploy/pull/4355) - Qwen/Internlm/Llama Dense/Moe model fp8 quant online by
[@43758726](https://github.com/43758726)in[#4324](https://github.com/InternLM/lmdeploy/pull/4324) - Qwen3.5 by
[@grimoire](https://github.com/grimoire)in[#4351](https://github.com/InternLM/lmdeploy/pull/4351) - GLM-4.7-Flash Turbomind support by
[@lapy](https://github.com/lapy)in[#4362](https://github.com/InternLM/lmdeploy/pull/4362) - Support router replay and ignore quant layer for qwen3.5 by
[@RunningLeon](https://github.com/RunningLeon)in[#4394](https://github.com/InternLM/lmdeploy/pull/4394) - [Feature] Add TurboMind support for Qwen3.5 models (dense + MoE) by
[@lapy](https://github.com/lapy)in[#4389](https://github.com/InternLM/lmdeploy/pull/4389) - support repetition ngram logits processor by
[@grimoire](https://github.com/grimoire)in[#4288](https://github.com/InternLM/lmdeploy/pull/4288)

### 💥 Improvements

- Compatible with transformers 5.0 at TurboMind side by
[@lvhan028](https://github.com/lvhan028)in[#4304](https://github.com/InternLM/lmdeploy/pull/4304) - Support fp32 head for qwen and internlm models by
[@RunningLeon](https://github.com/RunningLeon)in[#4160](https://github.com/InternLM/lmdeploy/pull/4160) - Reduce MLA kv-cache memory by
[@lzhangzz](https://github.com/lzhangzz)in[#4373](https://github.com/InternLM/lmdeploy/pull/4373) - add recurrent_gated_delta_rule kernel by
[@grimoire](https://github.com/grimoire)in[#4376](https://github.com/InternLM/lmdeploy/pull/4376) - [ascend]adapt for s1-pro dp*tp+ep by
[@yao-fengchen](https://github.com/yao-fengchen)in[#4380](https://github.com/InternLM/lmdeploy/pull/4380) - Support glm4.7 with mtp by
[@RunningLeon](https://github.com/RunningLeon)in[#4346](https://github.com/InternLM/lmdeploy/pull/4346) - Faster MLA kernels by
[@lzhangzz](https://github.com/lzhangzz)in[#4391](https://github.com/InternLM/lmdeploy/pull/4391) - Attention kernel self-registration and decoupled dispatching by
[@lzhangzz](https://github.com/lzhangzz)in[#4396](https://github.com/InternLM/lmdeploy/pull/4396)

### 🐞 Bug fixes

- fix: change debug log from ERROR to DEBUG in RepetitionPenaltyKernel by
[@murray-macdonald](https://github.com/murray-macdonald)in[#4363](https://github.com/InternLM/lmdeploy/pull/4363) - Fix quant config parsing for internvl awq model by
[@RunningLeon](https://github.com/RunningLeon)in[#4369](https://github.com/InternLM/lmdeploy/pull/4369) - Fix XGrammar bitmask initialization and add null check for gen_config in generate method by
[@windreamer](https://github.com/windreamer)in[#4349](https://github.com/InternLM/lmdeploy/pull/4349) - fix the logic of closing session by
[@lvhan028](https://github.com/lvhan028)in[#4370](https://github.com/InternLM/lmdeploy/pull/4370) - Fix authorization by
[@lvhan028](https://github.com/lvhan028)in[#4338](https://github.com/InternLM/lmdeploy/pull/4338) - Fix some minor issues and provide tests for Pipeline by
[@windreamer](https://github.com/windreamer)in[#4365](https://github.com/InternLM/lmdeploy/pull/4365) - fix dllm mask on set_step by
[@grimoire](https://github.com/grimoire)in[#4278](https://github.com/InternLM/lmdeploy/pull/4278) - fix models for transformers>=5 by
[@grimoire](https://github.com/grimoire)in[#4381](https://github.com/InternLM/lmdeploy/pull/4381) - fix exception when aborting a request by
[@lvhan028](https://github.com/lvhan028)in[#4403](https://github.com/InternLM/lmdeploy/pull/4403) - fix inference crashed on v100 with qwen3.5-0.8b by
[@lvhan028](https://github.com/lvhan028)in[#4420](https://github.com/InternLM/lmdeploy/pull/4420)

### 🌐 Other

- ci(lint): skip flaky deadlink test for python wiki page by
[@windreamer](https://github.com/windreamer)in[#4357](https://github.com/InternLM/lmdeploy/pull/4357) - fix fa3 install by
[@irexyc](https://github.com/irexyc)in[#4361](https://github.com/InternLM/lmdeploy/pull/4361) - fix lint by
[@windreamer](https://github.com/windreamer)in[#4375](https://github.com/InternLM/lmdeploy/pull/4375) - upgrade triton and torch by
[@grimoire](https://github.com/grimoire)in[#4379](https://github.com/InternLM/lmdeploy/pull/4379) - Add speculative decoding test by
[@littlegy](https://github.com/littlegy)in[#4377](https://github.com/InternLM/lmdeploy/pull/4377) - ci: integrate clang-format lint into pre-commit hooks by
[@windreamer](https://github.com/windreamer)in[#4390](https://github.com/InternLM/lmdeploy/pull/4390) - Update dockerfile by removing cu11 and changing cu12.4 to cu12.6 by
[@lvhan028](https://github.com/lvhan028)in[#4398](https://github.com/InternLM/lmdeploy/pull/4398) - manually build dev image instead of publishing it every version by
[@lvhan028](https://github.com/lvhan028)in[#4409](https://github.com/InternLM/lmdeploy/pull/4409) - bump version to v0.12.2 by
[@lvhan028](https://github.com/lvhan028)in[#4378](https://github.com/InternLM/lmdeploy/pull/4378)

## New Contributors

[@murray-macdonald](https://github.com/murray-macdonald)made their first contribution in[#4363](https://github.com/InternLM/lmdeploy/pull/4363)[@lapy](https://github.com/lapy)made their first contribution in[#4362](https://github.com/InternLM/lmdeploy/pull/4362)

**Full Changelog**: `v0.12.1...v0.12.2`

## v0.12.1

## What's Changed

### 🚀 Features

- support glm-4.7-flash by
[@RunningLeon](https://github.com/RunningLeon)in[#4320](https://github.com/InternLM/lmdeploy/pull/4320) - [ascend]suppot ep by
[@yao-fengchen](https://github.com/yao-fengchen)in[#3696](https://github.com/InternLM/lmdeploy/pull/3696)

### 💥 Improvements

- fix rotary embedding for transformers v5 by
[@grimoire](https://github.com/grimoire)in[#4303](https://github.com/InternLM/lmdeploy/pull/4303) - Improve metrics log by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4297](https://github.com/InternLM/lmdeploy/pull/4297) - Support ignore layers in quant config for qwen3 models by
[@RunningLeon](https://github.com/RunningLeon)in[#4293](https://github.com/InternLM/lmdeploy/pull/4293) - add custom noaux kernel by
[@grimoire](https://github.com/grimoire)in[#4345](https://github.com/InternLM/lmdeploy/pull/4345) - fix qwen3vl with transformers5 by
[@grimoire](https://github.com/grimoire)in[#4348](https://github.com/InternLM/lmdeploy/pull/4348)

### 🐞 Bug fixes

- fix tool call parser's streaming cursor by
[@lvhan028](https://github.com/lvhan028)in[#4333](https://github.com/InternLM/lmdeploy/pull/4333) - Fix data race for guided decoding in TP mode by
[@lzhangzz](https://github.com/lzhangzz)in[#4341](https://github.com/InternLM/lmdeploy/pull/4341) - fa3 check by
[@grimoire](https://github.com/grimoire)in[#4340](https://github.com/InternLM/lmdeploy/pull/4340) - Fix time series preprocess by
[@CUHKSZzxy](https://github.com/CUHKSZzxy)in[#4339](https://github.com/InternLM/lmdeploy/pull/4339) - Negative KV sequence length error in Attention op by
[@jinminxi104](https://github.com/jinminxi104)in[#4316](https://github.com/InternLM/lmdeploy/pull/4316) - fix qwen3-vl-moe long context by
[@grimoire](https://github.com/grimoire)in[#4342](https://github.com/InternLM/lmdeploy/pull/4342) - fix: move quantized norm to CPU instead of stale q_linear reference in smooth_quant by
[@Mr-Neutr0n](https://github.com/Mr-Neutr0n)in[#4352](https://github.com/InternLM/lmdeploy/pull/4352) - update noaux-kernel check by
[@grimoire](https://github.com/grimoire)in[#4358](https://github.com/InternLM/lmdeploy/pull/4358)

### 🌐 Other

- change INPUT_CUDA_VERSION to 12.6.2 by
[@lvhan028](https://github.com/lvhan028)in[#4322](https://github.com/InternLM/lmdeploy/pull/4322) - add Qwen3-8B accuracy evaluation in llm_compressor.md by
[@43758726](https://github.com/43758726)in[#4319](https://github.com/InternLM/lmdeploy/pull/4319) - [ci] refactor ete testcase by
[@zhulinJulia24](https://github.com/zhulinJulia24)in[#4274](https://github.com/InternLM/lmdeploy/pull/4274) - Set alias interns1_1 for interns1_pro by
[@lvhan028](https://github.com/lvhan028)in[#4334](https://github.com/InternLM/lmdeploy/pull/4334) - build(docker): skip FA2 when use cu13 by
[@windreamer](https://github.com/windreamer)in[#4356](https://github.com/InternLM/lmdeploy/pull/4356) - bump version to v0.12.1 by
[@lvhan028](https://github.com/lvhan028)in[#4350](https://github.com/InternLM/lmdeploy/pull/4350)

## New Contributors

[@Mr-Neutr0n](https://github.com/Mr-Neutr0n)made their first contribution in[#4352](https://github.com/InternLM/lmdeploy/pull/4352)

**Full Changelog**: `v0.12.0...v0.12.1`