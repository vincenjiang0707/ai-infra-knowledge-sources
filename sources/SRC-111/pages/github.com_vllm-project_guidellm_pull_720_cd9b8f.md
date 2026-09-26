source: https://github.com/vllm-project/guidellm/pull/720

# Add multi-arch (x86, arm) container image support - #720

[jaredoconnell](https://github.com/jaredoconnell)merged 3 commits into

## Conversation


[maryamtahhan](https://github.com/maryamtahhan)changed the title

May 7, 2026


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[build](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Abuild)

May 7, 2026

|
If you look at the original issue, we outlined that we do not want to publish official container images for a platform until we can fully support it will all features. I think |

|
The issue is if we want to benchmark inference on Arm platforms (which we do) We have to use an out of tree build and point folks to that, in our own quay repos. We would rather use an official guidellm build. Why not support the limited Arm image till the depedency is resolved and document the limitation? There's no clear timeline for the dependency being resolved in the meantime. |


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 12, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I think it's a positive that it moves the shared logic to one place.


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 12, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Looks good to me. I think it's a positive that it moves the shared logic to one place.


Agreed. I like the refactor.

The issue I see is whether we want to release/support a "watered down" arm64 container. I do think there's a potential cost in people grabbing it without understanding the limitations, but that may be justified as a (hopefully temporary) compromise.

Is there a good place to document this limitation? Having a container that supports all recommended dependencies isn't too bad. |

|
Some update on this, it looks like the only blocker on the |

|
I don't think this has to block on that. We can change it after we verify compatibility. |

My point is that this has been addressed (that PR merged) so I assume we can now build aarch64 with the |

|
TorchCodec 0.13 with stable aarch64 CPU-only wheels is now available. |

[maryamtahhan](https://github.com/maryamtahhan)dismissed stale reviews from

[dbutenhof](https://github.com/dbutenhof)and

[jaredoconnell](https://github.com/jaredoconnell)via

```
```[746fb9a](https://github.com/vllm-project/guidellm/commit/746fb9a3ad765ae7183e7ea124aa5107c81d2972)

May 25, 2026 09:10

|
This pull request has merge conflicts that must be resolved before it can be |

[maryamtahhan](https://github.com/maryamtahhan)

[force-pushed](https://github.com/vllm-project/guidellm/compare/746fb9a3ad765ae7183e7ea124aa5107c81d2972..c6b103dcf45a6d8eff074d816367fa7c4802c079)the feat/arm-container branch from

[to](https://github.com/vllm-project/guidellm/commit/746fb9a3ad765ae7183e7ea124aa5107c81d2972)

`746fb9a`


`c6b103d`

[Compare](https://github.com/vllm-project/guidellm/compare/746fb9a3ad765ae7183e7ea124aa5107c81d2972..c6b103dcf45a6d8eff074d816367fa7c4802c079)

May 25, 2026 10:19


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 26, 2026


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 26, 2026


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)May 26, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

I tested building an ARM64 container with this PR, and it worked fine for the simple use case of running a simple synthetic benchmark.

- Create reusable multi-arch build workflow - Build AMD64 with all extras, ARM64 with recommended extras - Generate manifest lists for automatic platform selection - Update development, nightly, and release workflows - Update container maintenance to handle arch-specific tags Fixes[vllm-project#498]Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Reusable workflows need explicit permissions passed from the caller. Added 'packages: write' permission to all three workflow callers. Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

- Upgrade torchcodec from 0.10 to 0.13 for stable aarch64 CPU wheels - Upgrade PyTorch from 2.10 to 2.11 (required for torchcodec 0.13) - Configure torchcodec to use CPU-only index to avoid CUDA dependencies - Enable 'all' extras for ARM64 builds (previously 'recommended' only) - Both AMD64 and ARM64 now include full audio support Validated builds successfully import torchcodec on both architectures. Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/c6b103dcf45a6d8eff074d816367fa7c4802c079..86ae651f3214f54fd7c5ba4c5e3862a96c7bcf83)the feat/arm-container branch from

[to](https://github.com/vllm-project/guidellm/commit/c6b103dcf45a6d8eff074d816367fa7c4802c079)

`c6b103d`


`86ae651`

[Compare](https://github.com/vllm-project/guidellm/compare/c6b103dcf45a6d8eff074d816367fa7c4802c079..86ae651f3214f54fd7c5ba4c5e3862a96c7bcf83)

May 26, 2026 18:17

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Add ARM64 container image support

Fixes #498

## Summary

This PR adds multi-architecture container image support for GuideLLM, enabling the container to run on both AMD64 (x86_64) and ARM64 (aarch64) platforms. This addresses issue #498 where users on ARM systems (e.g., Ampere processors) could not run the published container images.

The implementation creates a reusable workflow that builds architecture-specific images and combines them into manifest lists, allowing users to pull images without specifying architecture tags. The container runtime automatically selects the correct architecture.

Key architectural decision:ARM64 images are built with`recommended`

extras (excludes audio/vision) because PyTorch CPU wheels are not available for ARM64 Linux. AMD64 images continue to be built with`all`

extras for full feature support.## Details

New reusable workflow(`.github/workflows/build-multiarch-container.yml`

):`linux/amd64`

and`linux/arm64`

platforms in parallel using matrix strategy`workflow_call`

and`workflow_dispatch`

triggers for flexibilityUpdated workflowsto use the reusable workflow:`development.yml`

: Simplified to call reusable workflow with`pr-<number>`

tags`nightly.yml`

: Simplified to call reusable workflow with`nightly`

tag`release.yml`

: Added version extraction job, calls reusable workflow with release version tagContainer maintenance(`.github/workflows/container-maintenance.yml`

):`pr-N-amd64`

,`pr-N-arm64`

)`stable`

/`latest`

tag updates)Build configuration:`GUIDELLM_BUILD_EXTRAS=all`

(includes audio, vision, perf, tokenizers)`GUIDELLM_BUILD_EXTRAS=recommended`

(perf + tokenizers only)## Test Plan

## Local Testing (if you have podman/docker):

## Verify Manifest List:

Expected output: Two manifests (amd64 and arm64)

## CI Validation:

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)