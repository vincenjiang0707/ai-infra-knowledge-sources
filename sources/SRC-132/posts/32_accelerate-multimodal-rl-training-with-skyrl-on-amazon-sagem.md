# accelerate-multimodal-rl-training-with-skyrl-on-amazon-sagemaker-hyperpod

source: https://aws.amazon.com/blogs/machine-learning/accelerate-multimodal-rl-training-with-skyrl-on-amazon-sagemaker-hyperpod/

[Artificial Intelligence](https://aws.amazon.com/blogs/machine-learning/)

# Accelerate multimodal RL training with SkyRL on Amazon SageMaker HyperPod

Reinforcement learning (RL) post-training is becoming a standard step in building capable language model agents. Models learn to reason and act across sequences of steps by generating trajectories, receiving rewards, and updating their policy based on outcomes. Running this at scale, across multiple nodes with hundreds of GPU-hours of rollouts per training run, requires persistent cluster infrastructure. That infrastructure needs to sustain long jobs, recover from hardware failures without losing progress, and provide visibility into training dynamics as they unfold.

[Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/hyperpod/) provides this infrastructure for large-scale machine learning (ML) workloads on [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/). Through its [cluster resiliency features](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-resiliency.html), it continuously monitors node health and automatically replaces faulty nodes, so a hardware failure does not take the cluster down with it. Paired with checkpointing, a training job can pick up from its last saved step instead of restarting from scratch. This matters for long multi-node RL runs, where a single hardware failure would otherwise cost hours of rollout progress. Combined with the [Ray capabilities on HyperPod](https://aws.amazon.com/blogs/machine-learning/introducing-new-ray-capabilities-on-sagemaker-hyperpod/), you can create Ray clusters from SageMaker Studio, submit jobs remotely using secure connections, and monitor training through pre-built [Amazon Managed Grafana dashboards](https://aws.amazon.com/grafana/) that the HyperPod Observability EKS add-on provisions for you.

In this post, we show how to use these capabilities to run [SkyRL](https://github.com/NovaSky-AI/SkyRL), an open-source RL framework, to train a `Qwen3-VL-8B`

vision-language model to navigate visual mazes using Group Relative Policy Optimization (GRPO) on SageMaker HyperPod. Starting from the [VisGym SFT checkpoint](https://huggingface.co/VisGym/visgym_model), a supervised fine-tuning (SFT) starting point, GRPO post-training on HyperPod improves the maze solve rate from 43.75% to more than 95% on a fixed 64-maze evaluation set.

## Prerequisites

To follow this walkthrough, you need:

- A SageMaker HyperPod cluster with Amazon EKS orchestration that has at least 3 ml.g7e.12xlarge instances and one ml.r5d.16xlarge instance.
- The following Kubernetes operators installed in your cluster:
**KubeRay operator**,**HyperPod Observability EKS add-on**, and**HyperPod Ray Endpoint Operator**(for remote job submission). See the[Ray on HyperPod getting started guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-getting-started.html). - The
[Amazon FSx for Lustre CSI driver](https://github.com/kubernetes-sigs/aws-fsx-csi-driver)installed on the cluster. You also need an Amazon FSx for Lustre filesystem, a PersistentVolume backed by that filesystem, and a PersistentVolumeClaim (ReadWriteMany) that the pods can mount. The training job uses this at`/shared`

for checkpoint storage, Low-Rank Adaptation (LoRA) adapter synchronization, and evaluation output. - A SageMaker Studio domain with permissions to connect to your HyperPod cluster. See
[setting up SageMaker Studio for Ray](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-studio-setup.html). - The
`toolkit-for-ray-on-sagemaker-ai`

Python package installed.

## Background

This section reviews the reinforcement learning concepts behind the training and the cluster topology the walkthrough uses.

### Multi-turn RL and GRPO

Standard single-turn RL assigns a reward to a single model output. [Multi-turn RL](https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-mtrl.html) instead trains an agent over a whole sequence of steps, where it observes a state, acts, gets feedback, and moves on to the next state. The policy learns from the reward accumulated over the entire episode rather than from any one step.

Consider the example problem of navigating a 2D maze. One episode is a single run at a maze, and each turn is one move: the model looks at the current picture of the maze, chooses a direction or decides to stop, and the environment sends back the updated view. Rewards are sparse, so the model earns 1.0 only when it actually reaches the goal within the move limit and nothing otherwise. There is no move-by-move answer key to train against, since whether a move was good depends on the moves around it.

This is where SkyRL’s Group Relative Policy Optimization (GRPO) comes in. For each starting position, the agent runs the maze several times under the current policy, and GRPO grades those runs against one another, reinforcing the ones that beat the group’s average and pushing down the ones that trail it. That within-group comparison is the whole training signal, which lets GRPO work without a separate critic or value model.

### Training topology

The solution discussed here runs SkyRL on a HyperPod Ray cluster with three GPU worker nodes and a CPU head node. SkyRL colocates inference and training on the same GPUs: vLLM engines generate rollouts (complete maze episodes) while a policy model sharded with Fully Sharded Data Parallel (FSDP) handles gradient updates. After each optimizer step, updated LoRA adapter weights sync from the training ranks to the inference engines through Amazon FSx for Lustre shared storage.

These are the instance types we used. Other GPU instances and cluster sizes work as well, provided the workers have enough GPU memory for the model.

**Workers**: 3x`ml.g7e.12xlarge`

(2x NVIDIA RTX PRO 6000 Blackwell GPUs each, 6 GPUs total).**Head**:`ml.r5d.16xlarge`

(512 GB RAM, manages Ray GCS, dashboard, and LoRA adapter consolidation).**Policy model**:`Qwen3-VL-8B`

with LoRA (rank 32), sharded across the 6 GPUs using PyTorch FSDP.**Rollout engines**: 6 colocated vLLM instances, one per GPU.**Shared storage**: Amazon FSx for Lustre at`/shared`

, used for LoRA sync and evaluation output.

HyperPod provides the cluster infrastructure: the Ray cluster is created from SageMaker Studio, job submission uses the `sagemaker_ray://`

protocol, and training metrics flow automatically into pre-built Amazon Managed Grafana dashboards through the HyperPod Observability add-on.

## Solution overview

The following steps walk through preparing the training environment, launching the cluster, running the job, monitoring progress, and hosting the trained model.

### Step 1: Prepare the container image

To get started quickly, use the following Dockerfile to build a container image with SkyRL, VisGym, and their dependencies pre-installed. This is the image you will specify when launching your Ray cluster on HyperPod in the next step. It builds on the official NovaSky-AI SkyRL base and pins both SkyRL and VisGym to specific commit SHAs so the build is reproducible:

Build the image and push it to an Amazon Elastic Container Registry (Amazon ECR) repository in your account. Note the full image URI, as you will use it when creating the Ray cluster in the next step:

### Step 2: Launch the Ray cluster from SageMaker Studio

Navigate to SageMaker Studio, choose **HyperPod**, select your cluster, then go to the **Tasks** tab. From the task type list, choose **RayCluster**, then choose **Create Ray Cluster**.

In the creation form, give the cluster the name `skyrl-visgym`

, set the head instance type to `ml.r5d.16xlarge`

, and add three workers using `ml.g7e.12xlarge`

. Set the container image to the `IMAGE_URI`

you pushed in Step 1.

The instance types listed here are what we used for this walkthrough. Other instance types will work, but keep one constraint in mind for the head node: it needs large memory. The head consolidates LoRA adapter shards from the GPU workers at each checkpoint save, which briefly loads the full adapter weight set into CPU memory. We used `ml.r5d.16xlarge`

for its large memory capacity (512 GB RAM) to accommodate this.

#### Mounting Amazon FSx for Lustre

To attach your Amazon FSx filesystem, choose the YAML button in the top-right corner of the creation form to switch to the raw manifest editor, then add the volume and mount to both the head and worker pod specs. The relevant section for each pod looks like this:

Replace `<your-fsx-pvc-name>`

with the name of the PersistentVolumeClaim backed by your Amazon FSx filesystem. With this in place, `/shared`

is available on every node in the cluster and the training job can read and write checkpoints, LoRA weights, and evaluation output from the pods.

Turn on Remote endpoints so you can submit jobs and open dashboards without a local `kubectl port-forward`

. The cluster generates IAM-authenticated URLs for both.

Once the cluster reaches Running status, the Actions menu in the Tasks tab offers Open Ray Dashboard, Open Grafana, and cluster management options.

### Step 3: Prepare the training script

Save the following as `train_job.sh`

in your working directory. The script downloads the SFT checkpoint and generates datasets on first run (both go to Amazon FSx, so they persist across runs), then launches the GRPO training job.

The SFT checkpoint gives GRPO a strong starting point: `Qwen3-VL-8B`

pre-trained on VisGym demonstrations already knows how to parse a maze image and emit structured move actions, so GRPO only needs to refine which sequences reach the goal.

With `trainer.placement.colocate_all=true`

, the vLLM rollout engines and FSDP policy workers share the same GPUs. During rollout, GPUs run inference in parallel. During the policy update step, they run FSDP training collectively. The `lora_sync_path`

points to Amazon FSx so updated adapter weights are immediately visible to the inference engines on the nodes after each optimizer step. Without colocation, you need separate GPU pools for training and inference, and they sit idle waiting for each other between phases, a ping-pong pattern that wastes compute. Colocation avoids that idle time by having training and inference take turns on the same hardware. That is why `gpu_memory_utilization=0.45`

is set conservatively: each GPU needs headroom for both the FSDP shard and the vLLM KV cache at the same time.

A few other parameters are worth noting. `n_samples_per_prompt=8`

controls how many rollout trajectories GRPO generates per maze prompt to compute the group advantage. `max_turns=15`

caps each episode at 15 moves. `hf_save_interval=20`

consolidates LoRA adapter shards onto the head node and saves a Hugging Face-compatible checkpoint every 20 steps. `eval_interval=10`

runs the held-out 64-maze evaluation every 10 steps so you can track solve rate as training progresses.

The job also writes full training checkpoints so it can recover from an interruption. Setting `ckpt_interval=20`

saves the complete training state to `ckpt_path`

every 20 steps. That state includes the model weights, optimizer state, learning rate schedule, and dataloader position. `resume_mode=latest`

tells SkyRL to pick up from the most recent checkpoint under that path when the job starts. Point `ckpt_path`

at durable shared storage that is not tied to a single node, such as an Amazon Simple Storage Service (Amazon S3) prefix or your Amazon FSx mount. Keep the path stable across runs so a restarted job can find its checkpoint. This is what pairs with HyperPod cluster resiliency. When a node fails, HyperPod detects and replaces it automatically, and when you resubmit the job it continues from the last saved step instead of starting over. The full checkpoints written here capture training state for resumption, while the `hf_save_interval`

exports capture inference-ready LoRA adapters, so the two run alongside each other for different purposes.

### Step 4: Submit the training job remotely

When `toolkit-for-ray-on-sagemaker-ai`

is installed, Ray’s standard Jobs CLI authenticates through the cluster’s secured endpoint using the `sagemaker_ray://`

address scheme the package registers. The library authenticates to the Ray endpoint using your AWS credentials, so you don’t need to do it yourself. This way, you can submit and track jobs from a laptop, a CI/CD pipeline, or an environment with AWS credentials, with no `kubectl port-forward`

and no direct network path to the cluster.

First, authenticate against the EKS cluster:

Then submit the job, passing the current directory as the working dir so `train_job.sh`

is uploaded to the cluster head:

Once submitted, track progress using the same address:

You can also track the job in SageMaker Studio under the Tasks tab, or open the Ray Dashboard directly from the cluster Actions menu for a full job view with per-actor resource utilization.

### Step 5: Monitor training progress

HyperPod provides two monitoring surfaces: the Ray Dashboard for job-level visibility, and Amazon Managed Grafana for infrastructure and training metrics. Both are accessible directly from the Tasks tab in SageMaker Studio.

#### Ray Dashboard

From the Tasks tab in SageMaker Studio, choose Open Ray Dashboard. This generates a short-lived authenticated URL for you automatically.

You can also generate the URL from the [HyperPod CLI](https://github.com/aws/sagemaker-hyperpod-cli):

The command returns a presigned URL. Open it in a browser to view the Ray dashboard. The session is valid for up to six hours. For more details, see [Generating a dashboard connection URL](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray-dashboard-connection-url.html) in the HyperPod documentation.

The following screenshot shows the Jobs view with the running job, its current step, and per-worker resource utilization.

#### HyperPod Observability dashboards

From the Tasks tab, choose **Open Grafana**. The HyperPod Observability EKS add-on provisions four pre-built Ray dashboards in Amazon Managed Grafana: **Ray Core**, **Ray Data**, **Ray Train**, and **Ray Serve**. All four appear under a **Ray** folder and support filtering by cluster name. Here is a section of the core dashboard showing CPU, GPU, and memory utilization while the training is in progress.

#### Tracking evaluation accuracy

SkyRL runs an evaluation pass every `eval_interval=10`

steps against the fixed 64-maze held-out set and logs `eval/all/pass_at_1`

to the console. You can grep for it in the job logs:

In our experiment, the model reached 75% solve rate around step 100 and peaked at 96.875% (62/64 mazes) at step 160, compared to a baseline of 43.75% (28/64 mazes) before GRPO post-training. Your results will vary based on hyperparameters and the maze configuration. Once the solve rate reaches your target, the LoRA adapter at that step is ready for inference. Checkpoints are saved to `/shared/runs/<run_id>/global_step_<N>/policy/adapter_model.safetensors`

every 20 steps.

### Step 6: Host the trained model for inference

With training complete, the artifact you deploy is a LoRA adapter rather than a full model, and Ray Serve loads that adapter on demand at request time. The one requirement is where the adapter lives. Ray Serve’s dynamic LoRA loader reads adapters from cloud storage such as Amazon S3, so begin by staging the adapter in an S3 prefix. Copy the adapter from the checkpoint step you selected during training into that prefix:

Each adapter occupies its own subdirectory beneath this prefix, and that subdirectory name (`maze-grpo`

in this example) is the name you will use to request the adapter once the endpoint is live.

#### Serve with Ray Serve on a Ray cluster

To host the adapter, run Ray Serve on a Ray cluster built from the [AWS Deep Learning Container for Ray Serve LLM](https://aws.github.io/deep-learning-containers/ray-llm/), which bundles Ray Serve, the `ray[llm]`

stack, and vLLM. With it, you can stand up an OpenAI-compatible endpoint using the built-in `ray.serve.llm:build_openai_app`

builder and no custom image. We recommend running inference on a `RayService`

, which KubeRay reconciles into its own Ray cluster (see the [KubeRay docs](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/rayservice-quick-start.html)).

A `RayService`

describes its Serve application through a `serveConfigV2`

spec, and within that spec the `ray.serve.llm:build_openai_app`

builder accepts one `llm_configs`

entry per base model, as shown in the following configuration:

In this configuration, `model_source`

points at the base SFT model on the Amazon FSx mount, while `dynamic_lora_loading_path`

points at the S3 prefix you populated in the previous step. Set `max_lora_rank`

to the same LoRA rank you used during training. Finally, make sure the Ray Serve replicas can obtain AWS credentials to read the adapters from your S3 bucket. On Amazon EKS, the recommended mechanism for this is [Amazon EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html).

#### Dynamic LoRA loading per request

With this configuration in place, a single deployment serves both the base model and every adapter stored under the S3 prefix, and you choose which one to run through the `model`

field on each request:

- Set
`model`

to`visgym-qwen3vl`

to run the base SFT model on its own. - Set
`model`

to`visgym-qwen3vl:maze-grpo`

to apply the GRPO adapter on top of that base model. The ID follows the`<base-model-id>:<adapter-name>`

convention, where the adapter name is the subdirectory you created under`dynamic_lora_loading_path`

.

The first time an adapter is requested, Ray Serve downloads it from Amazon S3 onto the replica and caches it, so every later request reuses the loaded weights without downloading again. Because the endpoint speaks the OpenAI API, you can call it from an OpenAI-compatible client. For the complete set of configuration options, see the [Ray Serve LLM documentation](https://docs.ray.io/en/latest/serve/llm/index.html) and the [multi-LoRA deployment guide](https://docs.ray.io/en/latest/serve/llm/user-guides/multi-lora.html).

With the adapter deployed, the model can run a full maze episode on its own, taking in the current view at each turn and returning its next move until it reaches the goal. The loop that drives this (building the prompt, encoding the maze image, parsing the action, stepping the environment) is the same one SkyRL and VisGym already use for rollouts. Point that environment at the served endpoint rather than rebuilding it around a raw client.

Here is a sample result, the trained model navigating two mazes end to end:

## Clean up

When you finish the walkthrough, clean up the resources you created to stop incurring charges. Open the **Tasks** tab in SageMaker Studio, select the `skyrl-visgym`

Ray cluster, and choose **Delete** from the **Actions** menu. If you created a separate `RayService`

to host the trained adapter, delete that as well with `kubectl delete rayservice <name>`

. To release the GPU capacity itself, scale down the HyperPod instance groups you added for this walkthrough, or delete the HyperPod cluster from the Amazon SageMaker AI console. If you no longer need the SageMaker Studio domain, you can delete it from the SageMaker AI console too.

## Conclusion

In this post, we walked through an end-to-end multimodal RL training workflow on Amazon SageMaker HyperPod: building a custom container image, launching a Ray cluster from SageMaker Studio, starting from the VisGym SFT checkpoint to give GRPO a strong initialization, submitting the job using the `sagemaker_ray://`

protocol, monitoring evaluation accuracy through the Ray Dashboard and Grafana dashboards provisioned by the HyperPod Observability add-on, and hosting the trained adapter for inference once it reached the target solve rate. The entire workflow runs on the resilient, self-healing compute infrastructure that Amazon SageMaker HyperPod provides.

The same pattern applies to SkyRL workloads or other Ray-based RL frameworks. The HyperPod infrastructure, the Studio console experience, and the Amazon FSx shared storage work with frameworks that use standard Ray APIs.

To get started, see the [Amazon SageMaker HyperPod documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) and the [Ray on HyperPod getting started guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-ray.html).
