# Train AI models with Unsloth and Hugging Face Jobs for FREE

source: https://huggingface.co/blog/unsloth-jobs
published: Fri, 20 Feb 2026 00:00:00 GMT

Text Generation • 1B • Updated • 172k • 672

#
[
](https://huggingface.co#train-ai-models-with-unsloth-and-hugging-face-jobs-for-free)
Train AI models with Unsloth and Hugging Face Jobs for FREE

[Update on GitHub](https://github.com/huggingface/blog/blob/main/unsloth-jobs.md)

[Unsloth](https://github.com/unslothai/unsloth)and Hugging Face Jobs for fast LLM fine-tuning (specifically

[) through coding agents like Claude Code and Codex. Unsloth provides ~2x faster training and ~60% less VRAM usage compared to standard methods, so training small models can cost just a few dollars.](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)

`LiquidAI/LFM2.5-1.2B-Instruct`

Why a small model? Small language models like LFM2.5-1.2B-Instruct are ideal candidates for fine-tuning. They are cheap to train, fast to iterate on, and increasingly competitive with much larger models on focused tasks. LFM2.5-1.2B-Instruct runs under 1GB of memory and is optimized for on-device deployment, so what you fine-tune can be served on CPUs, phones, and laptops.


##
[
](https://huggingface.co#you-will-need)
You will need

We are giving away free credits to fine-tune models on Hugging Face Jobs. Join the [Unsloth Jobs Explorers](https://huggingface.co/unsloth-jobs) organization to claim your free credits and one-month Pro subscription.

- A
[Hugging Face](https://huggingface.co)account (required for HF Jobs) - Billing setup (for verification, you can monitor your usage and manage your billing in your
[billing page](https://huggingface.co/settings/billing)). - A Hugging Face token with write permissions
- (optional) A coding agent (
`Open Code`

,`Claude Code`

, or`Codex`

)

##
[
](https://huggingface.co#run-the-job)
Run the Job

If you want to train a model using HF Jobs and Unsloth, you can simply use the `hf jobs`

CLI to submit a job.

First, you need to install the `hf`

CLI. You can do this by running the following command:

```
# mac or linux
curl -LsSf https://hf.co/cli/install.sh | bash
```


Next you can run the following command to submit a job:

```
hf jobs uv run https://huggingface.co/datasets/unsloth/jobs/resolve/main/sft-lfm2.5.py \
--flavor a10g-small \
--secrets HF_TOKEN \
--timeout 4h \
--dataset mlabonne/FineTome-100k \
--num-epochs 1 \
--eval-split 0.2 \
--output-repo your-username/lfm-finetuned
```


Check out the [training script](https://huggingface.co/datasets/unsloth/jobs/blob/main/sft-lfm2.5.py) and [Hugging Face Jobs documentation](https://huggingface.co/docs/hub/jobs) for more details.

##
[
](https://huggingface.co#installing-the-skill)
Installing the Skill

Hugging Face model training skill lowers barrier of entry to train a model by simply prompting. First, install the skill with your coding agent.

###
[
](https://huggingface.co#claude-code)
Claude Code

Claude Code discovers skills through its [plugin system](https://code.claude.com/docs/en/discover-plugins), so we need to install the Hugging Face skills first. To do so:

- Add the marketplace:

```
/plugin marketplace add huggingface/skills
```


- Browse available skills in the
`Discover`

tab:

```
/plugin
```


- Install the model trainer skill:

```
/plugin install hugging-face-model-trainer@huggingface-skills
```


For more details, see the [documentation](https://huggingface.co/docs/hub/en/agents-skills) on using the hub with skills or the Claude Code [Skills docs](https://code.claude.com/docs/en/skills).

###
[
](https://huggingface.co#codex)
Codex

Codex discovers skills through [ AGENTS.md](https://developers.openai.com/codex/guides/agents-md) files and

[directories.](https://developers.openai.com/codex/skills)

`.agents/skills/`

Install individual skills with `$skill-installer`

:

```
$skill-installer install https://github.com/huggingface/skills/tree/main/skills/hugging-face-model-trainer
```


For more details, see the [Codex Skills docs](https://developers.openai.com/codex/skills) and the [AGENTS.md guide](https://developers.openai.com/codex/guides/agents-md).

###
[
](https://huggingface.co#anything-else)
Anything else

A generic install method is simply to clone the [skills repository](https://github.com/huggingface/skills) and copy the [skill](https://github.com/huggingface/skills/tree/main/skills/hugging-face-model-trainer) to your agent's skills directory.

```
git clone https://github.com/huggingface/skills.git
mkdir -p ~/.agents/skills && cp -R skills/skills/hugging-face-model-trainer ~/.agents/skills/
```


##
[
](https://huggingface.co#quick-start)
Quick Start

Once the skill is installed, ask your coding agent to train a model:

```
Train LiquidAI/LFM2.5-1.2B-Instruct on mlabonne/FineTome-100k using Unsloth on HF Jobs
```


The agent will generate a training script based on an [example in the skill](https://github.com/huggingface/skills/blob/main/skills/hugging-face-model-trainer/scripts/unsloth_sft_example.py), submit the training to HF Jobs, and provide a monitoring link via Trackio.

##
[
](https://huggingface.co#how-it-works)
How It Works

Training jobs run on [Hugging Face Jobs](https://huggingface.co/docs/huggingface_hub/guides/jobs), fully managed cloud GPUs. The agent:

- Generates a UV script with inline dependencies
- Submits it to HF Jobs via the
`hf`

CLI - Reports the job ID and monitoring URL
- Pushes the trained model to your Hugging Face Hub repository

###
[
](https://huggingface.co#example-training-script)
Example Training Script

The skill generates scripts like this based on the example in the [skill](https://github.com/huggingface/skills/blob/main/skills/hugging-face-model-trainer/scripts/unsloth_sft_example.py).

```
# /// script
# dependencies = ["unsloth", "trl>=0.12.0", "datasets", "trackio"]
# ///
from unsloth import FastLanguageModel
from trl import SFTTrainer, SFTConfig
from datasets import load_dataset
model, tokenizer = FastLanguageModel.from_pretrained(
"LiquidAI/LFM2.5-1.2B-Instruct",
load_in_4bit=True,
max_seq_length=2048,
)
model = FastLanguageModel.get_peft_model(
model,
r=16,
lora_alpha=32,
lora_dropout=0,
target_modules=[
"q_proj",
"k_proj",
"v_proj",
"out_proj",
"in_proj",
"w1",
"w2",
"w3",
],
)
dataset = load_dataset("trl-lib/Capybara", split="train")
trainer = SFTTrainer(
model=model,
tokenizer=tokenizer,
train_dataset=dataset,
args=SFTConfig(
output_dir="./output",
push_to_hub=True,
hub_model_id="username/my-model",
per_device_train_batch_size=4,
gradient_accumulation_steps=4,
num_train_epochs=1,
learning_rate=2e-4,
report_to="trackio",
),
)
trainer.train()
trainer.push_to_hub()
```


| Model Size | Recommended GPU | Approx Cost/hr |
|---|---|---|
| <1B params | `t4-small` |
~$0.40 |
| 1-3B params | `t4-medium` |
~$0.60 |
| 3-7B params | `a10g-small` |
~$1.00 |
| 7-13B params | `a10g-large` |
~$3.00 |

For a full overview of Hugging Face Spaces pricing, check out the guide [here](https://huggingface.co/docs/hub/en/spaces-overview#hardware-resources).

##
[
](https://huggingface.co#tips-for-working-with-coding-agents)
Tips for Working with Coding Agents

- Be specific about the model and dataset to use, and include Hub IDs (for example,
`Qwen/Qwen2.5-0.5B`

and`trl-lib/Capybara`

). Agents will search for and validate those combinations. - Mention Unsloth explicitly if you want it used. Otherwise, the agent will choose a framework based on the model and budget.
- Ask for cost estimates before launching large jobs.
- Request Trackio monitoring for real-time loss curves.
- Check job status by asking the agent to inspect logs after submission.