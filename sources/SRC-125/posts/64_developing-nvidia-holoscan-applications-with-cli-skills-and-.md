# developing-nvidia-holoscan-applications-with-cli-skills-and-ai-coding-agents

source: https://developer.nvidia.com/blog/developing-nvidia-holoscan-applications-with-cli-skills-and-ai-coding-agents/

NVIDIA Holoscan is a platform for building real-time AI applications at the edge, from medical imaging to robotics. [HoloHub](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0) is its companion repository: a growing collection of reference applications and components that demonstrate what’s possible.

We wanted to explore how a general-purpose coding agent could use the same examples, documentation, and development tools available to an engineer in an actual development task.

In this post, we walk through building a real-time endoscopic tool segmentation application using an AI coding agent. HoloHub [examples](https://nvidia-holoscan.github.io/holohub/applications/) and documentation provide implementation patterns, and [the development skills](https://build.nvidia.com/skills?filters=library%3Alibrary_holoscan&q=holohub) guide the agent through the HoloHub development process.

The [Holoscan CLI](https://github.com/nvidia-holoscan/holoscan-cli/tree/v4.5.0), invoked via `./holohub`

wrapper, provides the shared execution interface. The agent can discover development operations through the CLI, while the engineer can inspect and repeat the same commands.

The development workflow proceeds in iterations:

- The engineer defines a goal and constraints
- The coding agent inspects relevant examples, implements the application-specific code, and uses CLI to run the required development operations
- The engineer reviews the code, outputs, and tests, then sets the goal for the next iteration

The workflow is agent-agnostic; in this example, we used Codex with GPT-5.6 sol max mode, and the agent processing times mentioned were approximate.

## Setup and development target

The overall objective is an end-to-end endoscopic tool segmentation application: real-time inference with a live visualization of the segmentation masks, along with statistical analysis rendering.

We reused the existing [MONAI endoscopic tool segmentation model](https://github.com/Project-MONAI/model-zoo/tree/dev/models/endoscopic_tool_segmentation) and a Holoscan sample video, and confirmed that the existing application

worked locally. We focused on a new application reusing the deep learning segmentation pipeline, and adding comprehensive visualization, runtime telemetry and repeatable benchmarking.[monai_endoscopic_tool_seg](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0/applications/monai_endoscopic_tool_seg)

The agents were additionally provided with:

- Holoscan CLI with Bash execution permission
- HoloHub repository with documentation in a progressive disclosure pattern via the
[agents.md](https://github.com/nvidia-holoscan/holohub/blob/holoscan-sdk-4.5.0/AGENTS.md) - HoloHub development skills, including holohub-app-lifecycle and holohub-debug-build-run

The next sections show how the pieces work together in an engineer-guided, agentic development workflow.

## Iteration 0: Divide the goal

Instead of trying to build the entire application with a single prompt, developers should decompose the ultimate objective into smaller, verifiable engineering iterations guided by uncertainty and evidence. This approach ensures that design choices are reviewed in a timely manner.

The comprehensive goal can thus be structured into a sequence of reviewable topics:

- Is the development environment configured correctly to run a similar existing application locally?
- Can the existing model and video run in a separate end-to-end application?
- Does the visualization present meaningful information?
- Can latency be measured repeatedly?
- Can rendering throughput be improved without feature regressions?

Each iteration produces reviewable code, outputs, and tests, which inform the prompts and design choices for the next iteration.

## Iteration 1: Create a minimal working application

The first prompt defined the outcome while constraining model and data reuse.

**Developer prompt 1:**

Use $holohub-app-lifecycle to create a separate new Python HoloHub application for displaying endoscopic tool tracking as model outputs https://github.com/Project-MONAI/model-zoo/tree/dev/models/endoscopic_tool_segmentation. Reuse the MONAI endoscopic tool segmentation model, sample data, preprocessing, and inference. Show the model-derived mask, coverage and timeline, and useful uncertainty measurements in a polished HoloViz overlay. Do not train or modify the model weights. Make the sample video work end to end.

That left implementation choices to the agent while keeping model reuse, visual evidence, and weight integrity explicit.

The agents collected information from the designated sources: read the app lifecycle skill, nearby HoloHub examples, project metadata, and CLI documentation.

Different types of actions were taken as expected:

- Inspected the relevant endoscopy, segmentation, HoloViz, recording, and testing patterns;
[monai_endoscopic_tool_seg](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0/applications/monai_endoscopic_tool_seg),[endoscopy_tool_tracking](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0/applications/endoscopy_tool_tracking),[surgical_scene_recon](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0/applications/surgical_scene_recon)were particularly useful references - Dry-ran and invoked ./holohub create to generate and register the standard scaffold
- Implemented the application graph, execution modes, tests and documentation using existing Holoscan operators and assets
- Built and ran the application via ./holohub run with the application metadata defined by the CLI

The resulting application connected video replay, preprocessing, TensorRT inference, the SDK segmentation postprocessor, telemetry, and HoloViz. Inference and mask postprocessing ran for every replayed frame. The overlay reported frame-derived measurements.

The agentic processing time was 40 minutes. The developer could review the live app through the same CLI used by the agent:

`.` `/holohub` `run endoscopy_tool_segmentation_dashboard visual --language python` |

After reviewing the implementation, the visual outputs, and the test cases, we confirmed that the reused model and sample video worked in the new application. Visual review also showed that the overlay needed clearer measurements, so we proceed to define the next iteration.

## Iteration 2: Make future reviews repeatable by implementing benchmarking

The second prompt turned the visual demonstration into a repeatable development artifact:

**Developer prompt 2:**

Revise the visual output, add more meaningful statistics, tool area, mask motion, temporal intersection-over-union as a stability indicator, edge entropy, FPS, bounding box position, and remove values that remain unchanged during replay. Add a benchmark mode that records actual latency and plots the results in Python. Export the figures to the build folder and also show them interactively when the environment supports it.

In response, the agent revised the dynamic measurements and screenshot readability, then made visual review and benchmarking explicit application modes. The app was implemented to have three named application modes:

Mode | Contract |
|---|---|
`visual` | Run the full sample at source pace in an interactive window |
`smoke` | Quick 60-frame headless recording with a finite verdict |
`benchmark` | Process 300 frames offscreen and export measurements and plots |

*Table 1. The three execution modes available via ./holohub run*

With the Holoscan CLI and application lifecycle management, the modes and tests are discoverable and runnable without remembering a detailed container and application script recipe:

`.` `/holohub` `modes endoscopy_tool_segmentation_dashboard --language python` `.` `/holohub` `run endoscopy_tool_segmentation_dashboard benchmark --language python` `.` `/holohub` `test` `endoscopy_tool_segmentation_dashboard --language python` |

Benchmark mode used Holoscan Data Flow Tracking for the configured path from the video replayer through preprocessing, inference, telemetry, offscreen HoloViz, and the rendered-frame sink. It effectively reused the ideas presented in the existing [holoscan flow benchmarking module](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0/benchmarks/holoscan_flow_benchmarking). The agentic processing time was 20 minutes.

The revised benchmark provided more repeatable measurements. With that baseline available, the next iteration could investigate performance without relying on visual checks alone.

## Iteration 3: Investigate and improve latency

Once the application was measurable, the developer issued a third prompt:

**Developer prompt 3:**

Check whether the deep-learning model runs on every frame. Investigate ways to reduce latency, including approaches that take advantage of similar neighboring segmentations, and show the new benchmark results.

In response, the agent confirmed that inference still ran on every frame. It considered reusing masks across neighboring frames, which could avoid some inference work but would require a policy for deciding when stale output is acceptable. For this engineering iteration, it kept inference on every frame and first removed lower-risk dashboard overhead:

- Reused HoloViz input specifications and static coordinate tensors while refreshing text and dynamic geometry for every frame.
- Queued the current 10-value GPU-to-host telemetry copy asynchronously in two pinned buffers and rendered with the previous completed values.

We compared the first iteration’s implementation with the final one on the same test system. The optimized version was faster in all five measured trials. The agentic processing time was 30 minutes.

Measurement | Before | After | Change |
|---|---|---|---|
| Rendered throughput | 204.0 FPS | 306.9 FPS | 50.5% higher |
| Mean application-path latency | 4.891 ms | 3.247 ms | 33.6% lower |
| P95 application-path latency | 6.273 ms | 4.554 ms | 27.4% lower |

*Table 2. Performance comparison between the baseline and optimized endoscopy dashboard implementations*

## Final handoff prompt and revalidation

After the three engineering iterations, the developer gave the agent a separate handoff prompt.

**Developer prompt 4:**

`Commit the implementation and keep the benchmark logs.` |

To finalize the progress, we reran the application and the tests, verified the output figures and headless test results. The implementation and benchmark evidence were retained along with the commit hash and dependency versions via `./holohub env-check`

and `./holohub env-info`

.

The development iterations show what the workflow produces. To better understand the impact of the CLI, skills and documentation, we next compare the same development task under different combinations of these resources.

## Ablation study

We compared resource usage using the same coding agent and sandbox environment across identical settings (note that the study was last conducted on Aug. 1, using Codex 0.146.0 with GPT-5.6 Sol at max reasoning effort). All evaluations were based on the single prompt used in the first iteration (with the skill name removed if unavailable) with the goal of creating a new application.

### CLI + skills + docs/examples (this blog)

The agentic processing time was 40 minutes, with a total cost of 11M tokens.

### CLI + docs/examples

The agents were given `agents.md`

including references to CLI usage guide and docs, as well as the HoloHub codebase. No HoloHub development skills were provided.

The agentic processing time was 65 minutes, with a total cost of 20M tokens. While the workflow resulted in a complete application that achieved the implementation goal, the process was less efficient. The agents correctly located similar apps within the HoloHub repository, but tended to use generic Bash tools that required more trial-and-error probing of the development environment. For instance, they often applied generic linting tools before CLI-based linting, or attempted to install Python dependencies and run inference scripts directly on the host (should have consistently worked in a container).

### docs/examples

The agents were given the HoloHub codebase but without the agents.md and explicit guidance on the CLI usage. No HoloHub development skills were provided.

The agentic processing time was 40min, with a total cost of 15M tokens.

No CLI guidance was provided, the coding agents still gained understanding of the CLI (from the overall codebase examples) and used it as the main dev tooling. However the coding quality is suboptimal compared to the other two settings:

- The 3rd party model config and code were embedded in the application code incorrectly
- A Dockerfile was created without leveraging the existing HoloHub base image already has all the required dependencies
- Existing optimized Holoscan operators such as TensorRT inference and format converter were ignored in the implementation, as a result this version is 2.6x slower then the other two settings

While follow-up prompts could potentially address these issues, the combination of CLI, skills, and documentation/examples provided the best developer experience with the lowest resource overhead.

| Cost to first end-to-end app | CLI + skills + docs/examples (this blog) | docs/examples | CLI + docs/examples |
| Agentic processing time | 40 min | 40 min | 65 min |
| Token usage | 11M | 15M | 20M |
| Outcome | Separate application using standard Holoscan operators | Application required rework, used custom PyTorch/MONAI inference instead of Holoscan InferenceOp/TensorRT | Reviewable application, with more agentic host-side validation and retries |

*Table 3. Agentic processing time and token usage across three scaffolding configurations*

## A co-development loop for engineers and agents

This post follows a small, verifiable development loop. The result is an engineering prototype built on an existing model, sample video, and Holoscan components. It runs end to end, provides several application modes and automated tests, preserves the model weights, and records reproducible benchmark evidence.

The main takeaway is the development loop shared by the developer and the agents: `./holohub`

supplies consistent operations, the skill encodes project-specific sequences and checks, and examples and documentation provide engineering context. The agent and the developer use the same CLI commands. The developer can focus on defining the objectives, setting the constraints, evaluating trade-offs, and deciding whether the evidence is sufficient.

## References

- HoloHub:
[https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0](https://github.com/nvidia-holoscan/holohub/tree/holoscan-sdk-4.5.0) - Holoscan CLI:
[https://github.com/nvidia-holoscan/holoscan-cli/tree/v4.5.0](https://github.com/nvidia-holoscan/holoscan-cli/tree/v4.5.0) - HoloHub skills source:
[https://github.com/nvidia-holoscan/holohub/tree/main/skills](https://github.com/nvidia-holoscan/holohub/tree/main/skills) - HoloHub skills at Nvidia catalog:
[https://build.nvidia.com/skills?filters=library%3Alibrary_holoscan&q=holohub](https://build.nvidia.com/skills?filters=library%3Alibrary_holoscan&q=holohub)

## Start the discussion at forums.developer.nvidia.com
