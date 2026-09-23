# Bringing Robotics AI to Embedded Platforms: Dataset Recording, VLA Fine‑Tuning, and On‑Device Optimizations

source: https://huggingface.co/blog/nxp/bringing-robotics-ai-to-embedded-platforms
published: Thu, 05 Mar 2026 14:16:49 GMT

Image-Text-to-Text • 2B • Updated • 599 • 91

#
[
](https://huggingface.co#bringing-robotics-ai-to-embedded-platforms-dataset-recording-vla-finetuning-and-ondevice-optimizations)
Bringing Robotics AI to Embedded Platforms: Dataset Recording, VLA Fine‑Tuning, and On‑Device Optimizations

[Enterprise Article](https://huggingface.co/blog)


*Authors*: ** Enzo Ruedas**,


[Tess Boivin](https://huggingface.co/tboivin)Recent advances in Large Language Models have enabled the transition from text-only reasoning to **multimodal systems**. First, with the integration of visual perception in **Vision–Language Models (VLMs)**, and more recently with the generation of robot actions in **Vision–Language–Action (VLA) models**. Deploying these models on **embedded robotic platforms** remains a challenge due to tight constraints in terms of compute, memory, and power, as well as real-time control requirements.

In synchronous control pipelines, while the VLA is running inference, the arm is idle awaiting commands leading to oscillatory behavior and delayed corrections. To tackle that, [asynchronous Inference](https://huggingface.co/docs/lerobot/async) can enable smooth and continuous motion by dissociating generation from execution. However, to be effective, the **end-to-end inference latency must remain shorter than the action execution duration**. This temporal constraint therefore sets an upper limit on the model's throughput.

Bringing VLA models to embedded platforms is not a matter of model compression, but a complex systems engineering problem requiring **architectural decomposition**, **latency-aware scheduling**, and **hardware-aligned execution**. Addressing these challenges is essential to translate recent advances in multimodal foundation models into practical and deployable embedded robotic systems.

This guide presents NXP’s hands‑on best practices for recording reliable robotic datasets, fine‑tuning VLA policies ([ ACT] and

[), and hightlights the real-time performance that]

**SmolVLA****SoC achieves after optimization.**

[NXP i.MX 95](https://www.nxp.com/products/i.MX95)##
[
](https://huggingface.co#🎥-dataset-recording-what-actually-matters)
🎥 Dataset Recording: What Actually Matters

High‑quality, **consistent** data beats “more but messy” data. This section turns hard‑earned lessons into concrete checklists and schemas.

In our case, we recorded a dataset for the task: *"Put the tea bag in the mug."*

###
[
](https://huggingface.co#1-consistency-first)
1) Consistency First

**Fixed cameras**: Use rigid mounts to avoid pose drift. If during recording or evaluation one or more cameras shift because of the robot's vibrations or the operator resetting the environment, you can observe a severe accuracy loss.**Controlled lighting**: Set up your environment where you can have as much control as possible on lighting (Fixed light source(s) and far from sunlight that vary during the day).**Strong contrast**: Avoid training with “white on white” unless that’s your deployment domain. Maximize contrast between the arm, the object and the environment.**Fixed calibration**: Make sure to have backups of your robot and teleoperator calibrations so you don't have to re-record your previous episodes if the code crashes.**Do not cheat**: Do not use information the model will not have access to at inference time. During data recording, it is tempting for the operator to rely on direct visual observation of the scene. However, this introduces information that is absent from the dataset. Dataset collection must be restricted to the same camera inputs that will be available to the policy at runtime.

###
[
](https://huggingface.co#2-use-a-gripper-camera-highly-recommended)
2) Use a Gripper Camera (Highly Recommended)

Moving from scene‑only views to mixed viewpoints increases the global accuracy, but the more cameras you have the more the latency is impacted. Therefore, you must choose right compromise. In our case that balance was reached with 3 cameras:

| Top | Gripper | Left |
|---|---|---|
| The global view of the whole scene. | The closest view for precise grasps and alignment. | Complement the top view for height and depth. |


We strongly recommend using a gripper-mounted camera. It consistently improves success rates on fine manipulation tasks by providing a close, task-relevant viewpoint. Importantly, it is also the camera that most effectively enforces correct data collection practices, allowing the operator to rely exclusively on the robot’s perception rather than observing the scene directly.When installing a gripper camera, we recommend securing the cable with

Velcro or a strain-relief guideto prevent it from obstructing the field of view or becoming disconnected during motion.

###
[
](https://huggingface.co#3-improve-prehension)
3) Improve Prehension

Simple hardware tweaks like **heat‑shrink tubing** over gripper claws increase friction, reduce roughness, reduce slippage during episodes, and increase task success rate (fewer “almost success” episodes), improving policy learning stability.

###
[
](https://huggingface.co#4-diversity--splits)
4) Diversity & Splits

When recording a dataset, you should:

**Vary episodes distribution**: Divide your workspace into starting-position clusters, and record at least 10 episodes per cluster. Add diversity by changing the object position and rotation.*e.g. we partitioned the robot arm’s reachable workspace into 11 clusters, each measuring 10 × 10 cm.***Differentiate training & validation sets**: Policies can easily overfit on the training set, so make sure that the validation set is unseen by the model.*e.g. we removed cluster 6 from the training set.***Record the most movements you can**: Small VLA models exhibit limited generalization on unseen motion. Therefore, record episodes that cover the wider ranges of degrees of freedom.*e.g. we grasped the tea bag either in horizontal or vertical position.***Anticipate failure**: Sometimes the policy will not reach the object the first time and will have to "go back to it". We noticed that having 20% of all episodes that corresponds to the case of going back to the object help the model improve overall success rate.*e.g. around 20% of our training set corresponds to***recovery episodes**.

This mirrors best practices across VLA papers and community guides. Here are 3 examples of data diversity within the same cluster:

Starting positions 1 and 2 correspond to different positions within the same cluster. In contrast, during the recovery episode, the robot does not begin in "starting mode"; but is instead already near the mug and should proceed directly to retrieve the tea bag from that location.

##
[
](https://huggingface.co#🎛️-finetuning-vlas)
🎛️ Fine‑Tuning VLAs

What we did in practice:

**Tasks:**"Grab the tea bag and place it in the mug."**Dataset:**- 120 episodes: 10 clusters x (10 different tea bag starting positions + 2 recovery episodes)
- 3 cameras (640x480px, 30fps): Top, Gripper, Left
- Cluster n°6 was removed for validation

**Batch size:**8**Training:**Model checkpoint with the lowest validation loss after 200k steps was chosen

The range providing the best trade-off between accuracy, generalization, and motion smoothness across both the training and validation sets was found for ACT (100 actions per chunk) within a 100k-160k training steps. For SMolVLA training (50 actions per chunk), the trade‑off appears after many more training steps. We found that continuing training slightly past the point where the model begins to overfit tends to improve overall accuracy.

Rule of thumb: choose final checkpoint by evaluating success on both training and validation set, not by training loss.


##
[
](https://huggingface.co#⚡-optimizing-for-the-nxp-imx-95-applications-processor)
⚡ Optimizing for the NXP i.MX 95 Applications processor

The ** i.MX 95** SoC integrates 6× Arm Cortex‑A55, a Cortex‑M7 and a Cortex M33 MCU, a Mali GPU, a new NXP ISP, and the

**eIQ® Neutron NPU**, targeting

**efficient, secure edge inference**with multi‑camera support and strong I/O.

[[nxp.com]](https://www.nxp.com/products/i.MX95)

###
[
](https://huggingface.co#1-divide-and-conquer)
1) Divide And Conquer

Instead of running the models as one monolithic graph, we decompose the VLA graph into logical stages: encoders, decoders, and action experts. Therefore, allowing each component to be optimized, scheduled, and deployed independently.

In practice, SmolVLA is partitioned into the following sub-blocks:

**Vision**: processes RGB camera frames and produces visual embeddings.**LLM backbone**: generates actions tokens from visual and textual embeddings.**Action expert**: applies flow matching to iteratively denoise action samples and outputs final control commands.

This separation allows per-block optimizations. The impact of each block quantization can be measured to choose the best tradeoff between latency and accuracy. Also, isolating the action expert from the VLM was ideal to run it at lower frequency.

###
[
](https://huggingface.co#2-quantization)
2) Quantization

In order to optimize the inference for i.MX 95 SoC, we explored several quantization techniques on different blocks. We found that quantizing the vision encoder and LLM prefill had limited impact on accuracy, whereas quantization of the denoising flow in the action expert significantly degrades performance.

This behaviour is expected, as quantization errors are accumulating across iterative denoising steps.

That is why we decided to keep this block at higher precision to preserve stability, while on the other blocks, we explored various quantization configurations, from 8-bit mixed precision to 4-bit quantization, depending on the layers.

In addition, we applied in-house optimization on the different blocks. Results are shown in the below table, referred as *optimized models*.

###
[
](https://huggingface.co#3-asynchronous-inference-control-aware-scheduling)
3) Asynchronous Inference: Control-Aware Scheduling

In a synchronous control loop, the pipeline operates as:

- Capture observation
- Run full model inference
- Execute generated action

During step (2), the robot remains idle. If inference latency is non-negligible, this produces:

**Idle gaps**in motion**Oscillatory corrections**due to stale observations- Reduced effective control frequency
- Poor recovery behavior

With [ Asynchronous Inference](https://huggingface.co/docs/lerobot/async), action generation runs in parallel with execution:

- The robot executes the current action chunk
- The next chunk is computed simultaneously

This increases effective control frequency, reduces observation staleness, and improves recovery behavior.

On embedded platforms such as the i.MX 95 SoC, asynchronous inference is essential — but only effective if inference latency is kept under the action horizon budget: inference time < execution time

| Synchronous inference | Asynchronous inference | |
|---|---|---|
Actions per chunk |
100 | 100 |
FPS |
60 | 60 |
Chunk size threshold |
N/A | 0.2 |
Aggregate function |
N/A | weighted_average |
Action queue evolution |
||
Results |

##
[
](https://huggingface.co#📊-what-we-achieve-on-imx-95-applications-processor)
📊 What We Achieve on i.MX 95 Applications Processor

**Setup**

**Tasks:**"Grab the tea bag and place it in the mug."**Test set (20 episodes):**2 random positions for each cluster.**Validation set (10 episodes):**all 10 positions in cluster n°6

| Platform (CPU) | Policy | Format | Inference Latency | Accuracy Test Set (20) | Accuracy Validation Set (10) | Global Accuracy (30) |
|---|---|---|---|---|---|---|
| i.MX 95 | ACT | ONNX FP32 | 2.86 s | 1.00 | 0.90 | 0.96 |
| i.MX 95 | ACT | Optimized | 0.32 s | 1.00 | 0.60 | 0.89 |
| i.MX 95 | SmolVLA | ONNX FP32 | 29.1 s | 0.50 | 0.40 | 0.47 |

##
[
](https://huggingface.co#⏩-next-steps)
⏩ Next Steps

Our immediate objective is to improve task accuracy with SmolVLA (ONNX FP32). We have already established a baseline and measured an optimized on-board inference latency of **6.15 s**.

The next phase will focus on deeper optimizations on our NPUs. In parallel, we aim to move from single-task setup toward longer-horizon and more complex scenarios. To do that, we will introduce:

**Simulation environments**for scalable data generation and benchmarking**Reinforcement Learning (RL)**for policy refinement**Sim-to-Real transfer**to bridge domain gaps and improve real-world performance

The goal is to move from a single validated manipulation task toward a reproducible methodology for deploying VLA policies on embedded robotic systems.

##
[
](https://huggingface.co#✅-checklists-you-can-reuse)
✅ Checklists You Can Reuse

**Recording**

- Fixed mounts verified
- Good cameras focus and illumination
- Good gripper claws prehension
- Calibration files backups saved
- Contrast validated

**Training**

- Save/eval checkpoints every 20k steps
- Save also your training parameters to be able to resume training if needed
- Prepare in advance your validation set and your tracking method for accuracy and latency

**Deployment on i.MX 95 SoC**

- You are satisfied with your accuracy
-
[Contact us](mailto:voice@nxp.com)to have your model optimized

##
[
](https://huggingface.co#📚-resources--inspiration)
📚 Resources & Inspiration

**ACT documentation & paper**(core idea, action chunking, low‑demo success).[[huggingface.co]](https://huggingface.co/docs/lerobot/act),[[arxiv.org]](https://arxiv.org/abs/2304.13705)**SmolVLM/SmolVLA family & repos**(compact multimodal + VLA design).[[huggingface.co]](https://huggingface.co/HuggingFaceTB/SmolVLM-Base),[[github.com]](https://github.com/huggingface/smollm),[[smolvla.net]](https://smolvla.net/index_en)**Sherry Chen’s HF blog**on training ACT on SO‑101 (practical lessons, pitfalls, fixes).[[huggingface.co]](https://huggingface.co/blog/sherryxychen/train-act-on-so-101)