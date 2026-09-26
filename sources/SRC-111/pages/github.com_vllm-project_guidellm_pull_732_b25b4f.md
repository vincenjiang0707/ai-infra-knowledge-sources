source: https://github.com/vllm-project/guidellm/pull/732

# feat: synthetic image and video data generation for VLM benchmarking - #732

[mergify[bot]](https://github.com/mergify[bot])merged 18 commits into

## Conversation


**requested changes**

[dbutenhof](https://github.com/dbutenhof)May 18, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

First pass -- a few documentation comments. I think this is packing too much into `README.md`

, and should be broken out. There are also several places in the guide pages that mention synthetic (text) data that should probably be generalized.

[zakariaelh](https://github.com/zakariaelh)added a commit to zakariaelh/guidellm that referenced this pull request

May 18, 2026

Addresses dbutenhof's review on PR[vllm-project#732]. The Synthetic Multimodal Data section in README.md was too large and too specific for the front page, and the option list was a single dense bullet per type. - README.md: trim to a one-paragraph pointer at the new docs page - docs/guides/multimodal/synthetic_vision.md: new page; split into Synthetic image and Synthetic video subsections, each with example commands and a per-option Configuration Options list - docs/guides/datasets.md: frame the existing Synthetic Data section as text-specific, link out to the visual page - docs/guides/multimodal/index.md: add a Synthetic Vision card to the Available Guides grid Naming: "synthetic vision" rather than "synthetic multimodal" — covers images and video, but not audio.

|
This pull request has merge conflicts that must be resolved before it can be |

|
Thanks |

|
I'll start another review pass -- but, in the meantime, the CI failed because
|


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 19, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Second round of documentation comments.

[src/guidellm/data/deserializers/synthetic_image.py](https://github.com/vllm-project/guidellm/pull/732/files#diff-917b2d2347791b007183264d4ed26e631523577823388744e91736c9fa035955)Outdated

[src/guidellm/data/deserializers/synthetic_video.py](https://github.com/vllm-project/guidellm/pull/732/files#diff-ce107669b81f9e50e43e631abbf3497d05d46e0092629c233acc838a847c3921)Outdated

[docs/guides/multimodal/index.md](https://github.com/vllm-project/guidellm/pull/732/files#diff-821bf1c34ff37e7bd45a5b32af26bb2ac7fe4a48aa9339def92ca4cb54821e11)Outdated

[docs/guides/multimodal/synthetic_vision.md](https://github.com/vllm-project/guidellm/pull/732/files#diff-8d19e00deccbaab8a73c60054a562ecd1a3af26540de7ebecca32882b6e95484)Outdated

[docs/guides/multimodal/synthetic_vision.md](https://github.com/vllm-project/guidellm/pull/732/files#diff-8d19e00deccbaab8a73c60054a562ecd1a3af26540de7ebecca32882b6e95484)Outdated

[docs/guides/multimodal/synthetic_vision.md](https://github.com/vllm-project/guidellm/pull/732/files#diff-8d19e00deccbaab8a73c60054a562ecd1a3af26540de7ebecca32882b6e95484)Outdated


**requested changes**

[dbutenhof](https://github.com/dbutenhof)May 19, 2026


There was a problem hiding this comment.

A few more comments before I dive deep into the code of your deserializers (which may take a while).

PR [#733](https://github.com/vllm-project/guidellm/pull/733) refactors the mechanism used to discriminate deserializers, fixing some usability and extensibility problems. You need to rebase and resolve some conflicts anyway -- you might want to wait for that PR to drop first.

Sorry for the churn, and thanks for the contribution!

[pyproject.toml](https://github.com/vllm-project/guidellm/pull/732/files#diff-50c86b7ed8ac2cf95bd48334961bf0530cdc77b5a56f852c5c61b89d735fd711)

[src/guidellm/data/deserializers/synthetic_image.py](https://github.com/vllm-project/guidellm/pull/732/files#diff-917b2d2347791b007183264d4ed26e631523577823388744e91736c9fa035955)Outdated

[zakariaelh](https://github.com/zakariaelh)added a commit to zakariaelh/guidellm that referenced this pull request

May 20, 2026

Addresses dbutenhof's review on PR[vllm-project#732]. The Synthetic Multimodal Data section in README.md was too large and too specific for the front page, and the option list was a single dense bullet per type. - README.md: trim to a one-paragraph pointer at the new docs page - docs/guides/multimodal/synthetic_vision.md: new page; split into Synthetic image and Synthetic video subsections, each with example commands and a per-option Configuration Options list - docs/guides/datasets.md: frame the existing Synthetic Data section as text-specific, link out to the visual page - docs/guides/multimodal/index.md: add a Synthetic Vision card to the Available Guides grid Naming: "synthetic vision" rather than "synthetic multimodal" — covers images and video, but not audio. Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai>

[zakariaelh](https://github.com/zakariaelh)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e4df56a9e82671cebe11efb40c63edf5ed4e9a92..630e8041cfdd12de142e7875938b6eee26e56f35)the feat/synthetic-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/e4df56a9e82671cebe11efb40c63edf5ed4e9a92)

`e4df56a`


`630e804`

[Compare](https://github.com/vllm-project/guidellm/compare/e4df56a9e82671cebe11efb40c63edf5ed4e9a92..630e8041cfdd12de142e7875938b6eee26e56f35)

May 20, 2026 18:08

|
This pull request has merge conflicts that must be resolved before it can be |

|
Hey |

[alityb](https://github.com/alityb)

[force-pushed](https://github.com/vllm-project/guidellm/compare/630e8041cfdd12de142e7875938b6eee26e56f35..6314af498a8ed92b79707857aec3334b38bfbeff)the feat/synthetic-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/630e8041cfdd12de142e7875938b6eee26e56f35)

`630e804`


`6314af4`

[Compare](https://github.com/vllm-project/guidellm/compare/630e8041cfdd12de142e7875938b6eee26e56f35..6314af498a8ed92b79707857aec3334b38bfbeff)

June 25, 2026 20:06

[alityb](https://github.com/alityb)pushed a commit to zakariaelh/guidellm that referenced this pull request

Jun 25, 2026

Addresses dbutenhof's review on PR[vllm-project#732]. The Synthetic Multimodal Data section in README.md was too large and too specific for the front page, and the option list was a single dense bullet per type. - README.md: trim to a one-paragraph pointer at the new docs page - docs/guides/multimodal/synthetic_vision.md: new page; split into Synthetic image and Synthetic video subsections, each with example commands and a per-option Configuration Options list - docs/guides/datasets.md: frame the existing Synthetic Data section as text-specific, link out to the visual page - docs/guides/multimodal/index.md: add a Synthetic Vision card to the Available Guides grid Naming: "synthetic vision" rather than "synthetic multimodal" — covers images and video, but not audio. Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai>

|
Hi |

[alityb](https://github.com/alityb)pushed a commit to zakariaelh/guidellm that referenced this pull request

Jun 25, 2026

Addresses dbutenhof's review on PR[vllm-project#732]. The Synthetic Multimodal Data section in README.md was too large and too specific for the front page, and the option list was a single dense bullet per type. - README.md: trim to a one-paragraph pointer at the new docs page - docs/guides/multimodal/synthetic_vision.md: new page; split into Synthetic image and Synthetic video subsections, each with example commands and a per-option Configuration Options list - docs/guides/datasets.md: frame the existing Synthetic Data section as text-specific, link out to the visual page - docs/guides/multimodal/index.md: add a Synthetic Vision card to the Available Guides grid Naming: "synthetic vision" rather than "synthetic multimodal" — covers images and video, but not audio. Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

[alityb](https://github.com/alityb)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6314af498a8ed92b79707857aec3334b38bfbeff..ef6579e0fd05ea2f26df2aff907b43669c184cfd)the feat/synthetic-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/6314af498a8ed92b79707857aec3334b38bfbeff)

`6314af4`


`ef6579e`

[Compare](https://github.com/vllm-project/guidellm/compare/6314af498a8ed92b79707857aec3334b38bfbeff..ef6579e0fd05ea2f26df2aff907b43669c184cfd)

June 25, 2026 20:22

[alityb](https://github.com/alityb)pushed a commit to zakariaelh/guidellm that referenced this pull request

Jun 29, 2026

Addresses dbutenhof's review on PR[vllm-project#732]. The Synthetic Multimodal Data section in README.md was too large and too specific for the front page, and the option list was a single dense bullet per type. - README.md: trim to a one-paragraph pointer at the new docs page - docs/guides/multimodal/synthetic_vision.md: new page; split into Synthetic image and Synthetic video subsections, each with example commands and a per-option Configuration Options list - docs/guides/datasets.md: frame the existing Synthetic Data section as text-specific, link out to the visual page - docs/guides/multimodal/index.md: add a Synthetic Vision card to the Available Guides grid Naming: "synthetic vision" rather than "synthetic multimodal" — covers images and video, but not audio. Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

[alityb](https://github.com/alityb)

[force-pushed](https://github.com/vllm-project/guidellm/compare/ff1220c6cfffd60611c3c3f6f9ba58f1f9a75e3b..25aedb8f1f0894885b32fa49378a5e18de247fda)the feat/synthetic-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/ff1220c6cfffd60611c3c3f6f9ba58f1f9a75e3b)

`ff1220c`


`25aedb8`

[Compare](https://github.com/vllm-project/guidellm/compare/ff1220c6cfffd60611c3c3f6f9ba58f1f9a75e3b..25aedb8f1f0894885b32fa49378a5e18de247fda)

June 29, 2026 00:58

Pre-encoded data-URL output matching encode_image / encode_video shape. Per-row seeded gradient default with noise / solid / checkerboard opt-ins for images; gradient / noise for videos. Bit-exact mp4 encoding via imageio[ffmpeg] -fflags +bitexact so same seed produces byte-identical payloads. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

SyntheticImageDatasetConfig and SyntheticVideoDatasetConfig live next to the existing text config. text_tokens is canonical; prompt_tokens is accepted as an alias. resolution / aspect_ratio sugar resolves to width/height. Each deserializer peeks at the input type and refuses to claim configs explicitly marked for another deserializer, so the registry dispatch is deterministic when distinctive fields overlap. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

…video Unit tests cover synthesize_image / synthesize_video helpers (decoded dims, byte counts, reproducibility, per-row uniqueness, 1000-row cache-bust check) and the deserializers (pull 10 rows from a --data string, type-mismatch refusal, prompt_tokens alias, images_per_request). Integration test spins up the in-tree mock server and runs 'guidellm benchmark run' end-to-end with both synthetic_image and synthetic_video --data strings, asserting return code 0 and a non-empty benchmark report. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

Move synthetic multimodal generation out of Active Development for images and video. Audio remains WIP. Add two short --data examples (one image, one video) plus a parameter rundown for the new types. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

Two bugs caught by Section 4 of the evaluation plan against real vLLM: 1. SyntheticImageDataset and SyntheticVideoDataset features() omitted the image/video columns from the typed schema, so dataset.column_names returned only text columns. GenerativeColumnMapper reads column_names first and never sees `image`/`video`, so the request handler builds a text-only chat completion and the image is silently dropped. TTFT was identical across 480p/720p/1080p before the fix. 2. MediaEncoder still runs on synthetic rows. It called encode_image with the already-encoded canonical dict, which raised "Unsupported image type: <class 'dict'>" and dropped every row. Made encode_image and encode_video idempotent on the canonical dict shape so re-application is a no-op. After both fixes: resolution sweep TTFT 63.7 → 67.9 → 73.6ms (monotonic); frame sweep TTFT 94 → 211 → 376ms (monotonic, linear in frames); synth-vs-real fidelity 0.3% TTFT_p90 delta and 0.0% ITL_p50 delta. Co-authored-by: Claude Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

guidellm's AGENTS.md requires every AI-written test function to carry `## WRITTEN BY AI ##` at the end of its docstring. Adds the marker to all 45 new tests in the multimodal suite. Assisted-by: Claude (Anthropic) Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com>

Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Jack Wind <jckwind11@gmail.com>

Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Jack Wind <jckwind11@gmail.com>

Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com>

Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com>

[alityb](https://github.com/alityb)

[force-pushed](https://github.com/vllm-project/guidellm/compare/25aedb8f1f0894885b32fa49378a5e18de247fda..e5dccb92431f4fee49e87e53530db5c2482700dc)the feat/synthetic-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/25aedb8f1f0894885b32fa49378a5e18de247fda)

`25aedb8`


`e5dccb9`

[Compare](https://github.com/vllm-project/guidellm/compare/25aedb8f1f0894885b32fa49378a5e18de247fda..e5dccb92431f4fee49e87e53530db5c2482700dc)

June 30, 2026 20:21

|
I believe the earlier feedback is addressed now:
Would love any comments whenever you have time to take another look. Thanks! |


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 30, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Sorry I haven't gotten a chance for a full review yet, this is just a couple high-level things. We are working through a bit of a backlog right now plus some bugs that slipped into v0.7.0.

[src/guidellm/extras/vision.py](https://github.com/vllm-project/guidellm/pull/732/files#diff-dca0ea62c47fa14df5544d5fb37fcc43bc7ab4e15a6b5c2e71987316e475fbaa)

[src/guidellm/extras/vision.pyi](https://github.com/vllm-project/guidellm/pull/732/files#diff-36881053fafab4435f67a58b829b46721bd86c1c1c907eb06381b1c307b8f061)Outdated

[src/guidellm/utils/vision.py](https://github.com/vllm-project/guidellm/pull/732/files#diff-de60595dd945e059db8e43d6d0e30808769c92f7f6999ea56b7dd18c2c664dd6)Outdated


**reviewed**

[sjmonson](https://github.com/sjmonson)Jun 30, 2026

[tox.ini](https://github.com/vllm-project/guidellm/pull/732/files#diff-ef2cef9f88b4fe09ca3082140e67f5ad34fb65fb6e228f119d3812261ae51449)

Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com>

[alityb](https://github.com/alityb)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e5dccb92431f4fee49e87e53530db5c2482700dc..79bab9086dfdb1414e7704eba183cb28252a9286)the feat/synthetic-multimodal branch from

[to](https://github.com/vllm-project/guidellm/commit/e5dccb92431f4fee49e87e53530db5c2482700dc)

`e5dccb9`


`79bab90`

[Compare](https://github.com/vllm-project/guidellm/compare/e5dccb92431f4fee49e87e53530db5c2482700dc..79bab9086dfdb1414e7704eba183cb28252a9286)

June 30, 2026 22:43

|
Hey thanks for the comments, just addressed them. Hope to hear more updates when you guys are done with the backlog. Thanks once again! |


**requested changes**

[sjmonson](https://github.com/sjmonson)Jul 2, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Tried both dataset and they seem to work. Just a few nits.

[src/guidellm/extras/vision.py](https://github.com/vllm-project/guidellm/pull/732/files/79bab9086dfdb1414e7704eba183cb28252a9286#diff-dca0ea62c47fa14df5544d5fb37fcc43bc7ab4e15a6b5c2e71987316e475fbaa)Outdated

[src/guidellm/extras/vision.pyi](https://github.com/vllm-project/guidellm/pull/732/files/79bab9086dfdb1414e7704eba183cb28252a9286#diff-36881053fafab4435f67a58b829b46721bd86c1c1c907eb06381b1c307b8f061)

[src/guidellm/data/deserializers/synthetic_image.py](https://github.com/vllm-project/guidellm/pull/732/files/79bab9086dfdb1414e7704eba183cb28252a9286#diff-917b2d2347791b007183264d4ed26e631523577823388744e91736c9fa035955)Outdated

Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com>

|
Hey just followed your comments, should be all good now! Tested out Hope to hear back soon if there are any more updates needed! Thanks for all the help |

Ah my bad, I misremembered the behavior without alias. Regarding the type stub change I didn't realize that |

Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com>

|
No worries! I restored Happy to add |

All good, I have a branch with a bunch of small fixes that I have added those changes to. |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jul 2, 2026


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)Jul 2, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

[…llm-project#732]) ## Summary Adds two new `--data` types, `synthetic_image` and `synthetic_video`, that let users benchmark vLLM-served VLMs (Gemma 4, Qwen3-VL, InternVL3.5, etc.) without bringing their own image or video dataset. Composes with the existing synthetic-text knobs and produces TTFT/ITL within **0.3% of real media** at matched input shape on Gemma 4. This closes the "Generation of synthetic multimodal datasets" item under Active Development in the README. ## Details - [x] `SyntheticImageDatasetConfig` + `SyntheticImageDataset` + `SyntheticImageDatasetDeserializer` registered as `synthetic_image` - [x] `SyntheticVideoDatasetConfig` + `SyntheticVideoDataset` + `SyntheticVideoDatasetDeserializer` registered as `synthetic_video` - [x] `synthesize_image` / `synthesize_video` helpers in `guidellm.extras.vision`, sharing the canonical encoded-dict contract with `encode_image` / `encode_video` - [x] `encode_image` / `encode_video` now idempotent on the canonical dict (no-op if input already encoded) - [x] Per-row seeded gradients via PCG64 + `SeedSequence([seed, row_index])` (cross-platform deterministic, byte-different per row to defeat the mm-processor cache) - [x] `content` modes: `gradient` (default), `noise`, `solid`, `checkerboard` - [x] `images_per_request > 1` emits `image_0`, `image_1`, ... matching the existing column-mapper defaults - [x] `pyproject.toml`: `imageio[ffmpeg]` added to the `vision` extra - [x] README usage examples - [x] 45 unit + integration tests, all marked smoke/sanity/regression per AGENTS.md, all carrying `## WRITTEN BY AI ##` markers ### Levers exposed | Knob | Default | Purpose | |---|---|---| | `width`, `height` (or `resolution` + `aspect_ratio`) | required | Vision-tower FLOPs | | `frames`, `fps` (video) | required | Linear vision cost on most VLMs | | `format` | `jpeg` / `mp4` | Decode cost + wire size | | `jpeg_quality`, `video_bitrate` | 85 / libx264 default | Wire-size lever | | `content` | `gradient` | Cache-bust default; opt-in `noise` for worst-case wire size | | `text_tokens` (+ stdev/min/max) | required | Text-prefill cost (orthogonal to vision) | | `output_tokens` | required | Decode cost | | `images_per_request` | 1 | Multi-image-per-turn | | `seed` | 0 | Reproducibility | ### Example invocations ```bash guidellm benchmark run --target http://localhost:8000 --model google/gemma-4-E4B-it \ --profile constant --rate 2 --max-seconds 60 \ --data "type=synthetic_image,resolution=720p,text_tokens=200,output_tokens=64" guidellm benchmark run --target http://localhost:8000 --model google/gemma-4-E4B-it \ --profile constant --rate 2 --max-seconds 60 \ --data "type=synthetic_video,width=854,height=480,frames=6,fps=3,text_tokens=12,output_tokens=10" guidellm benchmark run --target http://localhost:8000 --model google/gemma-4-E4B-it \ --profile sweep --max-seconds 60 \ --data "type=synthetic_image,width=1024,height=1024,format=png,content=noise,images_per_request=2,text_tokens=128,output_tokens=32,seed=17" ``` ## Test Plan - `tox -e test-unit -- tests/unit/data/deserializers/test_synthetic_multimodal.py` - 43 unit tests covering decoded dimensions, byte counts, content modes, byte-uniqueness across 1000 gradient rows, reproducibility under matched seed, error handling on unsupported formats / content, deserializer dispatch, JSON config, multi-image emission - `tox -e test-integration -- tests/integration/data/test_synthetic_multimodal_benchmark.py` - 2 integration tests that drive a real `guidellm benchmark run` invocation against the in-tree mock server, end-to-end through the data pipeline + chat-completions request handler End-to-end validation against real vLLM serving `google/gemma-4-E4B-it`: | Check | Result | |---|---| | Real-vLLM smoke (image + video, rate=2, 30s) | Zero errors | | Resolution sweep TTFT_p50 (480p / 720p / 1080p) | 63.7 / 67.9 / 73.6 ms — monotonic | | Frame sweep TTFT_p50 (2 / 6 / 12 frames[@480p]) | 94.3 / 210.7 / 376.1 ms — monotonic, vision tokens scale linearly (~75/frame) | | **Synthetic vs real fidelity at matched shape (854×480, 6f@3fps, 100s @ rate=2)** | **TTFT_p90 delta 0.3% · ITL_p50 delta 0.0%** | | Reproducibility (same seed, two runs) | Byte-identical sha256 per row | Full evaluation methodology and per-section results are in the linked status doc. ## Related Issues - Resolves the "Generation of synthetic multimodal datasets" item listed under Active Development in `README.md` --- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [x] Includes tests generated or substantially modified by an AI agent Code and tests were drafted by Claude under my direction, then validated against real Gemma 4 inference on vLLM. The validation caught two real bugs in the initial draft, both fixed in `4ffa586` / current `1822225`: 1. `features()` in both deserializers declared text columns only, so `GenerativeColumnMapper` never saw `image` / `video` (dataset.column_names was text-only) and the request handler silently built text-only chat completions. TTFT was flat across all resolutions before the fix. 2. `MediaEncoder` still ran on synthetic rows and called `encode_image` with the already-encoded canonical dict, raising `Unsupported image type: <class 'dict'>` and dropping every row. Fixed by making `encode_image` / `encode_video` idempotent on the canonical dict shape. I have reviewed every line of the diff and am the submitter of record. --- # git log commit[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Wed May 13 00:48:17 2026 -0400 extras/vision: add synthesize_image and synthesize_video helpers Pre-encoded data-URL output matching encode_image / encode_video shape. Per-row seeded gradient default with noise / solid / checkerboard opt-ins for images; gradient / noise for videos. Bit-exact mp4 encoding via imageio[ffmpeg] -fflags +bitexact so same seed produces byte-identical payloads. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit]ce4767e[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Wed May 13 00:52:16 2026 -0400 data: add synthetic_image and synthetic_video deserializers SyntheticImageDatasetConfig and SyntheticVideoDatasetConfig live next to the existing text config. text_tokens is canonical; prompt_tokens is accepted as an alias. resolution / aspect_ratio sugar resolves to width/height. Each deserializer peeks at the input type and refuses to claim configs explicitly marked for another deserializer, so the registry dispatch is deterministic when distinctive fields overlap. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit]86d6d47[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Wed May 13 00:57:05 2026 -0400 tests: unit + integration coverage for synthetic_image and synthetic_video Unit tests cover synthesize_image / synthesize_video helpers (decoded dims, byte counts, reproducibility, per-row uniqueness, 1000-row cache-bust check) and the deserializers (pull 10 rows from a --data string, type-mismatch refusal, prompt_tokens alias, images_per_request). Integration test spins up the in-tree mock server and runs 'guidellm benchmark run' end-to-end with both synthetic_image and synthetic_video --data strings, asserting return code 0 and a non-empty benchmark report. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit]caf5a7f[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Wed May 13 00:57:41 2026 -0400 docs: README usage examples for synthetic_image and synthetic_video Move synthetic multimodal generation out of Active Development for images and video. Audio remains WIP. Add two short --data examples (one image, one video) plus a parameter rundown for the new types. Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit]df4c6eb[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Wed May 13 12:49:21 2026 -0400 fix: declare image/video features and make encoders idempotent Two bugs caught by Section 4 of the evaluation plan against real vLLM: 1. SyntheticImageDataset and SyntheticVideoDataset features() omitted the image/video columns from the typed schema, so dataset.column_names returned only text columns. GenerativeColumnMapper reads column_names first and never sees `image`/`video`, so the request handler builds a text-only chat completion and the image is silently dropped. TTFT was identical across 480p/720p/1080p before the fix. 2. MediaEncoder still runs on synthetic rows. It called encode_image with the already-encoded canonical dict, which raised "Unsupported image type: <class 'dict'>" and dropped every row. Made encode_image and encode_video idempotent on the canonical dict shape so re-application is a no-op. After both fixes: resolution sweep TTFT 63.7 → 67.9 → 73.6ms (monotonic); frame sweep TTFT 94 → 211 → 376ms (monotonic, linear in frames); synth-vs-real fidelity 0.3% TTFT_p90 delta and 0.0% ITL_p50 delta. Co-authored-by: Claude Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit]621fd9c[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Fri May 15 10:30:57 2026 -0400 tests: add WRITTEN BY AI marker per AGENTS.md guidellm's AGENTS.md requires every AI-written test function to carry `## WRITTEN BY AI ##` at the end of its docstring. Adds the marker to all 45 new tests in the multimodal suite. Assisted-by: Claude (Anthropic) Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit]8b62eaa[Author: Jack Wind <jckwind11@gmail.com> Date: Sat May 16 02:21:48 2026 +0000 Fix pre-existing lint and type-check failures Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Jack Wind <jckwind11@gmail.com> commit]a153b2c[Author: Jack Wind <jckwind11@gmail.com> Date: Sat May 16 02:21:48 2026 +0000 Add coordinate warp to synthetic gradient generator Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Jack Wind <jckwind11@gmail.com> commit]fd8fe19[Author: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Date: Mon May 18 18:43:35 2026 -0400 docs: move synthetic visual data out of README into dedicated guide Addresses dbutenhof's review on PR]aaef412[vllm-project#732]. The Synthetic Multimodal Data section in README.md was too large and too specific for the front page, and the option list was a single dense bullet per type. - README.md: trim to a one-paragraph pointer at the new docs page - docs/guides/multimodal/synthetic_vision.md: new page; split into Synthetic image and Synthetic video subsections, each with example commands and a per-option Configuration Options list - docs/guides/datasets.md: frame the existing Synthetic Data section as text-specific, link out to the visual page - docs/guides/multimodal/index.md: add a Synthetic Vision card to the Available Guides grid Naming: "synthetic vision" rather than "synthetic multimodal" — covers images and video, but not audio. Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> commit[Author: Zakaria el hjouji <zakaria@overshoot.ai> Date: Wed May 20 14:08:42 2026 -0400 review: address second-pass docs and code comments - Replace bare assert in both synthetic deserializers with an explicit isinstance check + RuntimeError, matching guidellm's style for unexpected-type guards. - docs/guides/multimodal/index.md: expand "VLM" to "Vision-Language Model (VLM)" on the Synthetic Vision card to avoid the VLM/vLLM/LLM visual collision. - docs/guides/multimodal/synthetic_vision.md: - drop the "wire-size pin" phrasing from the bitrate example - "pin"/"pinned" -> "specify"/"fixed" in the video_bitrate bullet - rewrite the ffmpeg/PIL note to just warn about byte-level variability across versions, instead of recommending users modify the uv.lock file - pyproject.toml unchanged; uv.lock regenerated via `uv sync --extra vision` so it tracks the vision-extra dependency closure. Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> commit]1b96f3a[Author: Ali Tayeb <ali.moh.islam.1@gmail.com> Date: Wed Jun 24 21:30:55 2026 -0700 data: align synthetic vision with kind routing Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com> commit]503e41c[Author: Ali Tayeb <ali.moh.islam.1@gmail.com> Date: Wed Jun 24 21:31:42 2026 -0700 tests: update synthetic vision kind coverage Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com> commit]4535918[Author: Ali Tayeb <ali.moh.islam.1@gmail.com> Date: Wed Jun 24 21:32:24 2026 -0700 docs: update synthetic vision CLI examples Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com> commit]39896b2[Author: Ali Tayeb <ali.moh.islam.1@gmail.com> Date: Tue Jun 30 15:43:37 2026 -0700 review: address media encoder comments Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com> commit]79bab90[Author: Ali Tayeb <ali.moh.islam.1@gmail.com> Date: Thu Jul 2 10:53:13 2026 -0700 review: compose synthetic vision with text data Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com> commit]97e8adf[Author: Ali Tayeb <ali.moh.islam.1@gmail.com> Date: Thu Jul 2 11:40:23 2026 -0700 review: restore __all__ in vision type stub Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com> --------- Assisted-by: Claude (Anthropic) Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com> Co-authored-by: Claude Signed-off-by: Zakaria el hjouji <zakaria@overshoot.ai> Signed-off-by: Zakaria el hjouji <elhjouji.zakaria@gmail.com> Signed-off-by: Jack Wind <jckwind11@gmail.com> Signed-off-by: Ali Tayeb <ali.moh.islam.1@gmail.com>]8d59ff0

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Adds two new

`--data`

types,`synthetic_image`

and`synthetic_video`

, that let users benchmark vLLM-served VLMs (Gemma 4, Qwen3-VL, InternVL3.5, etc.) without bringing their own image or video dataset. Composes with the existing synthetic-text knobs and produces TTFT/ITL within0.3% of real mediaat matched input shape on Gemma 4.This closes the "Generation of synthetic multimodal datasets" item under Active Development in the README.

## Details

`SyntheticImageDatasetConfig`

+`SyntheticImageDataset`

+`SyntheticImageDatasetDeserializer`

registered as`synthetic_image`

`SyntheticVideoDatasetConfig`

+`SyntheticVideoDataset`

+`SyntheticVideoDatasetDeserializer`

registered as`synthetic_video`

`synthesize_image`

/`synthesize_video`

helpers in`guidellm.extras.vision`

, sharing the canonical encoded-dict contract with`encode_image`

/`encode_video`

`encode_image`

/`encode_video`

now idempotent on the canonical dict (no-op if input already encoded)`SeedSequence([seed, row_index])`

(cross-platform deterministic, byte-different per row to defeat the mm-processor cache)`content`

modes:`gradient`

(default),`noise`

,`solid`

,`checkerboard`

`images_per_request > 1`

emits`image_0`

,`image_1`

, ... matching the existing column-mapper defaults`pyproject.toml`

:`imageio[ffmpeg]`

added to the`vision`

extra`## WRITTEN BY AI ##`

markers## Levers exposed

`width`

,`height`

(or`resolution`

+`aspect_ratio`

)`frames`

,`fps`

(video)`format`

`jpeg`

/`mp4`

`jpeg_quality`

,`video_bitrate`

`content`

`gradient`

`noise`

for worst-case wire size`text_tokens`

(+ stdev/min/max)`output_tokens`

`images_per_request`

`seed`

## Example invocations

## Test Plan

`tox -e test-unit -- tests/unit/data/deserializers/test_synthetic_multimodal.py`

`tox -e test-integration -- tests/integration/data/test_synthetic_multimodal_benchmark.py`

`guidellm benchmark run`

invocation against the in-tree mock server, end-to-end through the data pipeline + chat-completions request handlerEnd-to-end validation against real vLLM serving

`google/gemma-4-E4B-it`

:Synthetic vs real fidelity at matched shape (854×480, 6f@3fps, 100s @ rate=2)TTFT_p90 delta 0.3% · ITL_p50 delta 0.0%Full evaluation methodology and per-section results are in the linked status doc.

## Related Issues

`README.md`

## Use of AI

Code and tests were drafted by Claude under my direction, then validated against real Gemma 4 inference on vLLM. The validation caught two real bugs in the initial draft, both fixed in

`4ffa586`

/ current`1822225`

:`features()`

in both deserializers declared text columns only, so`GenerativeColumnMapper`

never saw`image`

/`video`

(dataset.column_names was text-only) and the request handler silently built text-only chat completions. TTFT was flat across all resolutions before the fix.`MediaEncoder`

still ran on synthetic rows and called`encode_image`

with the already-encoded canonical dict, raising`Unsupported image type: <class 'dict'>`

and dropping every row. Fixed by making`encode_image`

/`encode_video`

idempotent on the canonical dict shape.I have reviewed every line of the diff and am the submitter of record.

## git log

commit

ce4767eAuthor: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Wed May 13 00:48:17 2026 -0400

commit

86d6d47Author: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Wed May 13 00:52:16 2026 -0400

commit

caf5a7fAuthor: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Wed May 13 00:57:05 2026 -0400

commit

df4c6ebAuthor: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Wed May 13 00:57:41 2026 -0400

commit

621fd9cAuthor: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Wed May 13 12:49:21 2026 -0400

commit

8b62eaaAuthor: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Fri May 15 10:30:57 2026 -0400

commit

a153b2cAuthor: Jack Wind jckwind11@gmail.com

Date: Sat May 16 02:21:48 2026 +0000

commit

fd8fe19Author: Jack Wind jckwind11@gmail.com

Date: Sat May 16 02:21:48 2026 +0000

commit

aaef412Author: Zakaria el hjouji elhjouji.zakaria@gmail.com

Date: Mon May 18 18:43:35 2026 -0400

commit

1b96f3aAuthor: Zakaria el hjouji zakaria@overshoot.ai

Date: Wed May 20 14:08:42 2026 -0400

commit

503e41cAuthor: Ali Tayeb ali.moh.islam.1@gmail.com

Date: Wed Jun 24 21:30:55 2026 -0700

commit

4535918Author: Ali Tayeb ali.moh.islam.1@gmail.com

Date: Wed Jun 24 21:31:42 2026 -0700

commit

39896b2Author: Ali Tayeb ali.moh.islam.1@gmail.com

Date: Wed Jun 24 21:32:24 2026 -0700

commit

79bab90Author: Ali Tayeb ali.moh.islam.1@gmail.com

Date: Tue Jun 30 15:43:37 2026 -0700

commit

97e8adfAuthor: Ali Tayeb ali.moh.islam.1@gmail.com

Date: Thu Jul 2 10:53:13 2026 -0700

commit

8d59ff0Author: Ali Tayeb ali.moh.islam.1@gmail.com

Date: Thu Jul 2 11:40:23 2026 -0700

Assisted-by: Claude (Anthropic)

Co-Authored-By: Claude Opus 4.7 (1M context) noreply@anthropic.com

Co-authored-by: Claude

Signed-off-by: Zakaria el hjouji zakaria@overshoot.ai

Signed-off-by: Zakaria el hjouji elhjouji.zakaria@gmail.com

Signed-off-by: Jack Wind jckwind11@gmail.com

Signed-off-by: Ali Tayeb ali.moh.islam.1@gmail.com