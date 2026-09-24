# how-to-train-a-cross-embodiment-robot-navigation-policy-with-ai-agents

source: https://developer.nvidia.com/blog/how-to-train-a-cross-embodiment-robot-navigation-policy-with-ai-agents/

Navigation enables a robot to turn perception and motion into purposeful autonomy. Unlike locomotion, which produces stable movement, navigation must be used to continuously localize the robot, interpret changing surroundings, select a route, and avoid obstacles to reach a goal safely.

Moving this capability to a new robot or scene can require new data, simulation assets, robot interfaces, training, diagnosis, and evaluation. Repeating that work for every robot-scene pair is expensive and difficult to reproduce.

An agent-driven workflow reduces this burden. The developer defines the robot, scene source, and navigation goal. A coding agent uses repository skills to validate dependencies, prepare assets, run smoke tests, launch training, diagnose failures, and compare checkpoints. Human approval gates control scene acceptance, the one-environment smoke test, and checkpoint promotion.

Using Spot as the reference robot, this post tutorial applies an agent-driven [COMPASS](https://github.com/NVlabs/COMPASS) workflow to a built-in scene and a SAGE-10K scene, while showing how [NVIDIA Omniverse NuRec](https://docs.nvidia.com/nurec/index.html#) supports captured environments. It follows the policy workflow through smoke testing, residual training, checkpoint evaluation, and runtime integration, including optional odometry.

## What is COMPASS?

[COMPASS](https://github.com/NVlabs/COMPASS) (Cross-Embodiment Mobility Policy via Residual RL and Skill Synthesis) is a unified framework that enables scalable cross-embodiment mobility using expert demonstrations from a single embodiment. It reuses navigation behavior from the pretrained [NVIDIA X-Mobility](https://huggingface.co/nvidia/X-Mobility) policy. It trains a residual specialist, a [reinforcement learning (RL)](https://www.nvidia.com/en-us/glossary/reinforcement-learning/) policy that corrects the base action for a selected robot and environment instead of relearning navigation from the beginning. Data from multiple specialists can later be distilled into a shared cross-embodiment policy.

The COMPASS policy architecture that this agent-driven workflow trains and evaluates is shown in Figure 1.

COMPASS packages this development workflow as repository skills. This tutorial uses Codex during development. The trained policy and robot controller execute navigation at runtime without the coding agent.

### Reference workflow overview

The reference workflow uses the Boston Dynamics Spot quadruped. The built-in warehouse is the primary reproducible path, SAGE-10K extends it to a generated scene, and NVIDIA Omniverse NuRec provides an optional path for a reconstructed target environment. [NVIDIA cuVSLAM](https://github.com/nvidia-isaac/cuVSLAM), a CUDA-accelerated visual odometry and simultaneous localization and mapping library, can provide deployment odometry when the robot does not already supply compatible odometry and transforms.

For another environment, use the repository-pinned COMPASS software stack and the following hardware guidance:

- An Ubuntu 22.04 or 24.04 system with at least 32 GB of RAM, an RTX-capable NVIDIA GPU with at least 16 GB of VRAM, and
[Linux driver 580.95.05](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/requirements.html), the version tested for[Isaac Sim 6.0](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/requirements.html). The Isaac Sim 6.0 minimum reference GPU is a GeForce RTX 4080. Run the[Isaac Sim Compatibility Checker](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/installation/requirements.html#isaac-sim-compatibility-checker)before installation. - Docker Engine 24 or later with the NVIDIA Container Toolkit.
- A Hugging Face account and read token with access to the gated
[nvidia/COMPASS](https://huggingface.co/nvidia/COMPASS)and[nvidia/X-Mobility](https://huggingface.co/nvidia/X-Mobility)Hugging Face repositories. - The tested tutorial stack: NVIDIA Isaac Lab 3.0 with NVIDIA Isaac Sim 6.0.

## Step 1: Set up the COMPASS agentic workflow

First, prepare the repository and give the coding agent a clear workflow contract before beginning the scene work. You will download the gated assets, make the COMPASS skill discoverable to Codex, run stack checks, and stop at the one-environment approval gate. All `$compass`

blocks are copyable prompts for the Codex chat at the COMPASS repository root, not shell commands. In Claude Code, use `/compass`

for the same workflow.

For Codex, first expose the repository skills under `.agents/skills`

, then select COMPASS with `/skills`

or mention `$compass`

in the prompt. Codex supports symlinked skill directories, so the current repository skill can remain in its maintained location. For Claude Code, invoke the same workflow with `/compass`

.

`mkdir -p .agents/skills` `ln -s ../../.claude/skills/compass .agents/skills/compass` `ln -s ../../.claude/skills/compass-doctor .agents/skills/compass-doctor` `ln -s ../../.claude/skills/compass-newembodiment .agents/skills/compass-newembodiment` |

The coding agent can clone, build, download non-secret assets, and validate the stack. The developer must accept the gated repository terms and enter the Hugging Face token outside the chat. The agent should never request, display, or store the token in logs.

### Install COMPASS and download the assets

Clone the [COMPASS repository](https://github.com/NVlabs/COMPASS) and follow the [COMPASS Handbook quick start](https://nvlabs.github.io/COMPASS/docs/quickstart.html) with the repository-pinned container. Before the first run, accept access to the gated [nvidia/COMPASS](https://huggingface.co/nvidia/COMPASS) and [nvidia/X-Mobility](https://huggingface.co/nvidia/X-Mobility) Hugging Face repositories, create a [Hugging Face read token](https://huggingface.co/settings/tokens), and confirm that it can read public gated repositories available to your account. Expose the token only in the current shell. Do not paste it into an agent prompt or commit it to source control.

`export HF_TOKEN=hf_xxx` `./docker/run.sh assets` `./docker/run.sh build` `source ./docker/activate` |

The assets step downloads the registered simulation assets to `./assets/usd/`

and the pretrained [X-Mobility checkpoint](https://huggingface.co/nvidia/X-Mobility) to `./assets/x_mobility.ckpt`

. A 401 or 403 response usually indicates incomplete repository access or token scope. Resolve authentication before debugging Isaac Lab.

Each phase produces reviewable evidence before the next phase begins:

**Validate:**Software and asset inventory, environment report, and smoke-test log**Prepare scene**: Registered scene configuration, occupancy map, and visual inspection evidence**Train:**Pinned command and configuration, logs, telemetry, and periodic checkpoints**Evaluate**: Matched protocol, standard COMPASS metrics, videos, and a promotion recommendation**Package:**Approved checkpoint, configuration, evaluation record, and artifact manifest

Approval criteria are project-specific, but every gate should answer the same question: are the required inputs present, did the expected outputs appear, are there unresolved errors, and is the evidence sufficient to continue?

### Invoke the COMPASS skill

After the container is active, open the coding agent at the repository root and describe the robot, scene, navigation outcome, and approval gates. For the baseline workflow, copy this prompt into the agent chat:

`$compass Validate the COMPASS environment for Spot. Confirm the pinned ` `repository revision, container, GPU, Isaac Lab and Isaac Sim versions, ` `simulation assets, and pretrained X-Mobility checkpoint. Run a one-environment ` `smoke test, save the validation report, and stop for approval.` |

The `$compass`

skill checks the requested workflow against the repository and runs the relevant validation steps. If a run fails, `$compass-doctor`

performs a read-only health check and reports likely causes without silently changing the environment.

## Step 2: Choose and prepare a navigation scene

This section explains how to choose and prepare one of three scene sources: the built-in COMPASS warehouse, a generated [SAGE-10K](https://huggingface.co/datasets/nvidia/SAGE-10k) scene, or a captured environment rendered with [Omniverse NuRec](https://isaac-sim.github.io/IsaacLab/develop/source/policy_deployment/03_compass_with_NuRec/compass_navigation_policy_with_NuRec.html). You will learn what each path is for and which registration, occupancy map, and approval checks must be completed before training.

### Path 1: Use the built-in warehouse

Start with the registered `combined_multi_rack`

warehouse for the fastest reproducible baseline. The robot, scene, and occupancy map are already registered, which makes this the best path for validating the installation before introducing a new scene.

Copy the following prompt into the coding agent to run the baseline and pause after the smoke test:

`$compass Train and evaluate Spot in the built-in combined_multi_rack warehouse. ` `Stop after the one-environment smoke test for approval.` |

### Path 2: Use a SAGE-10K scene

The [SAGE-10K](https://huggingface.co/datasets/nvidia/SAGE-10k) dataset contains 10,000 generated indoor scenes across 50 room types. It is a scene dataset, not a policy or simulator. Each scene provides geometry, materials, layout metadata, and a preview. Living room and warehouse scenes follow the same preparation path, so select one suitable candidate instead of downloading the entire dataset.

The SAGE-10K path includes two human approval gates. First, inspect the converted USD in [NVIDIA Isaac Sim](https://github.com/isaac-sim/IsaacSim) and confirm geometry, materials, scale, and collision meshes before registration. After registration and occupancy-map generation, approve the one-environment preview before full training. The occupancy map identifies free and blocked space for valid robot starts and navigation goals.

Copy the following prompt into the coding agent to shortlist a scene and pause at both gates:

`$compass Find suitable SAGE-10K living-room or warehouse scenes for Spot and show the best candidates. ` `After I approve a scene, convert and register it, generate and verify its occupancy map, and stop for inspection. ` `After I approve the scene and map, run a one-environment smoke test and stop again before full training.` |

### Path 3: Introduce a captured environment with NuRec

Use [Omniverse NuRec](https://isaac-sim.github.io/IsaacLab/develop/source/policy_deployment/03_compass_with_NuRec/compass_navigation_policy_with_NuRec.html) when the goal is to fine-tune and evaluate COMPASS in a reconstruction of the intended deployment environment. NuRec converts stereo RGB captures into an Isaac Sim-ready reconstruction with aligned visual geometry, collision meshes, and optional scene augmentation. The documented COMPASS path registers the rendered scene, verifies its supplied occupancy map and origin convention, inspects robot clearance, and runs a one-environment smoke test before training.

NuRec is an optional path for the purposes of this post. The hands-on training flow continues with SAGE-10K so that the tutorial follows one scene from preparation through evaluation. For a captured environment, use the [COMPASS NuRec workflow](https://github.com/NVlabs/COMPASS/blob/real2sim/isaaclab_3.0/docs/handbook/workflows/nurec_real2sim.md) and the [NVIDIA Isaac Sim NuRec guide](https://isaac-sim.github.io/IsaacLab/develop/source/policy_deployment/03_compass_with_NuRec/compass_navigation_policy_with_NuRec.html), including the [living room example](https://isaac-sim.github.io/IsaacLab/develop/source/policy_deployment/03_compass_with_NuRec/compass_navigation_policy_with_NuRec.html), for scene preparation, training, evaluation, export, and ROS 2 deployment.

Copy the following prompt into the coding agent to prepare a registered NuRec scene and pause before training:

`$compass Prepare the registered NuRec Real2Sim scene <scene_name> for <supported_robot>. ` `Verify the supplied occupancy map and origin convention, inspect collisions and robot clearance, ` `run a one-environment smoke test, and stop for approval before training.` |

## Step 3: Validate the robot-scene integration

Once the selected scene is available to COMPASS, run a one-environment preview before scaling training. For a SAGE-10K scene, complete the earlier visual inspection and scene-registration approval gate first. Confirm that Isaac Sim starts, the scene loads, Spot spawns in a valid location, camera observations are available, and the robot responds to policy commands without clipping, falling, or producing unresolved simulation errors.

Direct the coding agent to summarize the preview logs and visual evidence, identify any blockers, and stop for human approval. Proceed to residual training only after the scene, robot, observations, and action interface work together as expected.

## Step 4: Train the residual specialist

This section explains how COMPASS adapts the pretrained[ X-Mobility](https://github.com/NVlabs/X-MOBILITY) policy to the selected robot and scene. You will launch residual reinforcement learning, monitor the run, save candidate checkpoints, and preserve the evidence required for evaluation.

### Launch residual training

After the one-environment smoke test is approved, the coding agent can launch the[ ](https://nvlabs.github.io/COMPASS/docs/)[standard residual RL workflow](https://nvlabs.github.io/COMPASS/docs/). The following command uses Spot and the built-in warehouse. Replace the environment key with the registered SAGE-10K scene when following the generated-scene path.

After the smoke test is approved, the coding agent can launch the [standard residual RL workflow](https://nvlabs.github.io/COMPASS/docs/workflows/training.html). The following example runs the built-in warehouse baseline. Replace the environment key with the registered [SAGE-10K](https://huggingface.co/datasets/nvidia/SAGE-10k) scene when continuing the generated-scene path.

`python run.py \` ` ` `-c configs` `/train_config` `.gin \` ` ` `-o .` `/outputs/spot_combined_multi_rack` `\` ` ` `-b .` `/assets/x_mobility` `.ckpt \` ` ` `--enable_cameras \` ` ` `--embodiment spot \` ` ` `--environment combined_multi_rack` |

### Manage the training run

Residual training is a long-running process. The coding agent should run it in a persistent session or managed scheduler, write logs and checkpoints to the configured output directory, and report progress without keeping the interactive session open.

Before training, record the command, repository revision, scene key, configuration, checkpoint interval, and stopping criteria. If the run is interrupted, verify that the latest checkpoint is complete and confirm the supported resume options before continuing.

### Monitor training and save checkpoints

Set `--num_envs`

according to available GPU memory, using one environment only for the smoke test. During training, monitor reward components, goal progress, contacts and falls, episode terminations, throughput, and GPU memory.

Save periodic checkpoints and evaluate them under matched conditions instead of assuming that the final iteration is best. COMPASS also supports distributed multi-GPU training for larger runs. Training time varies with the hardware, scene complexity, environment count, and stopping criteria.

### Diagnose failures and preserve evidence

Use the COMPASS diagnostic workflow to investigate failures before changing the environment or training configuration. Route authentication errors to Hugging Face access checks, scene-loading or collision errors to scene preparation, camera or action-interface errors to the smoke-test stage, and memory errors to environment-count or multi-GPU configuration.

Preserve the training configuration, command, repository revision, scene registration, occupancy map, smoke-test evidence, logs, checkpoints, and artifact manifest. Require developer approval before changing dependencies, scene assets, rewards, or training settings.

## Step 5: Evaluate before promoting a checkpoint

This section shows how to determine whether a residual checkpoint is ready for promotion. You will learn how to compare the pretrained base policy and residual candidates under matched conditions, interpret the standard COMPASS metrics, label any derived evidence, and retain human approval before packaging.

Review task performance and safety together. Standard COMPASS evaluation reports goal-reached rate, fall-down rate, and travel time. Additional evidence, such as goal progress, contact behavior, timeouts, or command stability, should be labeled as derived analysis or custom instrumentation. Promote a checkpoint only after the matched evidence satisfies the project’s navigation and safety gates, and a human approves packaging.

The following prompt is an example. Adapt it to the robot, scene, checkpoints, and evidence required by your workflow:

`$compass Compare the pretrained X-Mobility base policy with the available Spot ` `residual checkpoints in the selected scene under matched seeds, goals, initial states, ` `rollout length, and active terminations. Report the standard COMPASS evaluation metrics, ` `save matched videos and the exact evaluation command, clearly label any derived evidence, ` `and stop for human approval before promoting or packaging a checkpoint.` |

## Step 6: Connect the policy to the robot runtime

This section explains how the trained policy connects to the robot runtime after development is complete. You will learn the reference policy inputs and outputs, when [cuVSLAM](https://github.com/nvidia-isaac/cuVSLAM) can provide deployment odometry, and when an unregistered robot requires the [new-embodiment workflow](https://nvlabs.github.io/COMPASS/docs/extending.html). The coding agent coordinates development and validation; it does not control the robot at runtime.

### Understand the policy inputs and outputs

The COMPASS asset step downloads the pretrained [X-Mobility checkpoint](https://huggingface.co/nvidia/X-Mobility) used for smoke testing and residual training. Training creates the residual checkpoint for the selected robot and scene. Export and deployment package the trained policy for inference; they do not expose the base and residual as two ROS 2 components that developers must connect manually.

In the [reference ROS 2 integration](https://nvlabs.github.io/COMPASS/docs/deployment/ros2.html), [ compass_inference](https://github.com/NVlabs/COMPASS/blob/main/ros2_deployment/compass_navigator/compass_navigator/compass_inference.py) converts front-camera images, the navigation target or route, and robot speed derived from odometry into the exported policy inputs. It publishes forward-linear and angular-velocity commands on

`/cmd_vel`

. Recurrent state and previous action are internal to the inference implementation, not external ROS integration inputs. Validate coordinate frames, update rates, normalization, command limits, stopping behavior, and the physical robot controller for the target deployment.### Add cuVSLAM odometry when needed

Use the cuVSLAM library when the deployed robot needs camera-based state estimation in a GPS-denied or GPS-intermittent environment and does not already provide compatible, validated odometry and transforms. Its odometry can support the COMPASS navigator, but its map is not an input to the navigation policy.

cuVSLAM is not part of COMPASS policy training and does not require an agent skill. Run it as a separate, version-matched ROS 2 component, connect or remap its odometry output to `/chassis/odom`

, provide the required `odom-to-base_link`

transform, and validate calibration, timestamps, topic names, and frame conventions. The optional `$cuvslam-onboard`

and `$cuvslam-troubleshoot`

skills can help configure and diagnose this state-estimation component during development.

Example prompt:

`$cuvslam-onboard Configure cuVSLAM as the odometry source for the COMPASS ` `navigator on <robot and camera rig>. Select a compatible release and tracking mode, ` `validate calibration and timestamps, connect odometry and TF to the expected COMPASS ` `interfaces, and stop for approval before enabling navigation.` |

### Extend the workflow to another robot

For a robot that is not registered, `$compass-newembodiment`

guides the developer through robot configuration, environment registration, action mapping, and a one-environment visual smoke test. Onboarding a new embodiment is a separate engineering task from training a specialist for an existing robot, but it uses the same validation and approval pattern.

This tutorial stops at checkpoint evaluation. Export to ONNX, JIT, or TensorRT, ROS 2 integration, and physical hardware deployment require separate validation for the target robot and runtime. Scene quality, training duration, and checkpoint performance vary with the embodiment, environment, reward design, and available compute, so the workflow does not define a universal success threshold.

## Get started with COMPASS

Start with the reference path, then extend one component at a time:

- Set up the reference environment. Clone the
[COMPASS repository](https://github.com/NVlabs/COMPASS), follow the[COMPASS Handbook quick start](https://nvlabs.github.io/COMPASS/docs/quickstart.html), accept the gated model terms, and download the[COMPASS simulation assets](https://huggingface.co/nvidia/COMPASS)and[X-Mobility checkpoint](https://huggingface.co/nvidia/X-Mobility). - Run the agentic workflow. Invoke
`$compass`

in Codex with a supported robot and built-in scene, retain approval after the smoke test, and train and evaluate the specialist under matched conditions. - Extend and package deliberately. Use
`$compass-newembodiment`

for an unregistered robot. Save the configuration, checkpoint, logs, matched evaluation results, and videos needed for the next engineering decision.

To reproduce and extend the workflow, check out these resources:

[SAGE-10K dataset](https://huggingface.co/datasets/nvidia/SAGE-10k)for generated indoor scenes[Omniverse NuRec developer page](https://developer.nvidia.com/omniverse/nurec),[COMPASS NuRec workflow](https://github.com/NVlabs/COMPASS/blob/real2sim/isaaclab_3.0/docs/handbook/workflows/nurec_real2sim.md), and[Isaac Lab NuRec guide](https://isaac-sim.github.io/IsaacLab/develop/source/policy_deployment/03_compass_with_NuRec/compass_navigation_policy_with_NuRec.html)for captured-scene reconstruction and navigation policy training[NVIDIA Isaac Sim](https://docs.isaacsim.omniverse.nvidia.com/latest/index.html)and[NVIDIA Isaac Lab](https://isaac-sim.github.io/IsaacLab/main/index.html)documentation for the simulation and robot-learning stack[Isaac ROS Visual SLAM documentation](https://nvidia-isaac-ros.github.io/repositories_and_packages/isaac_ros_visual_slam/index.html)for optional cuVSLAM-based deployment odometry

## Start the discussion at forums.developer.nvidia.com
