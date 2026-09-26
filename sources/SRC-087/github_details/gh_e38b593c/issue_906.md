# [Issue #906] [RFC]: Speculators CLI — unified command-line interface for the full pipeline

source: https://github.com/vllm-project/speculators/issues/906
state: closed | updated: 2026-09-01T12:33:23Z
labels: RFC

## 正文

### Motivation.

The `speculators` package currently ships a single CLI command (`speculators convert`) while every other pipeline step — data preparation, response regeneration, hidden-states generation, training, stitching, evaluation, and plotting — lives as standalone scripts under `scripts/`. Users must clone the repo, navigate to the right script, and construct invocations by reading source code. This creates several problems:

- **Discoverability.** There is no single `--help` that shows the full speculative decoding workflow. Users learn the pipeline by reading tutorials or copying shell recipes — the tool itself teaches nothing.
- **Installability.** `pip install speculators` gives only `convert`. Running the training pipeline requires a repo clone, manual `PYTHONPATH` setup, and knowledge of which script lives where.
- **Scriptability.** Scripts write progress and results to the same stream, making it hard to compose pipeline steps or integrate with automation.
- **Fragmentation.** Eight scripts, three subdirectories, inconsistent flag styles. The cognitive overhead of switching between them adds up.

The recent config-file-first training CLI (#833) solved the configuration story for `train.py` specifically — `TrainConfig.resolve()` layers YAML + CLI flags with typed validation. This RFC extends that pattern to the rest of the pipeline, giving every workflow step a proper CLI command under a single `speculators` entry point.

### Proposed Change.

Expand the `speculators` CLI from just `convert` into a complete command-line interface covering the full speculative decoding workflow. All pipeline script logic moves into the `speculators` package; `scripts/` files become backward-compatible shims.

#### Design principles

1. **Verb-first flat subcommands** matching pipeline phases — discoverable in `--help`, reads in workflow order
2. **YAML config + CLI flag overrides** for training — leverages the existing `TrainConfig` pydantic schema (#833)
3. **torchrun stays external** — `speculators train` for single-GPU convenience, `torchrun -m speculators.train` for distributed
4. **Structured output to stdout, progress to stderr** — scripting and automation friendly
5. **Example configs ship with the package** in `configs/examples/`
6. **`pip install speculators` gives the full CLI** — no repo clone required for any workflow step

#### Command tree

```
speculators
├── regenerate-responses          # regenerate assistant responses on-policy via vLLM
├── prepare-data                  # tokenize + mask + token frequency stats
├── generate-data                 # offline hidden states generation (via vLLM server)
├── train                         # train speculator model (single-GPU via typer)
├── stitch                        # stitch MTP weights → verifier checkpoint
├── eval                          # evaluation group
│   ├── throughput                #   max throughput acceptance-rate run
│   ├── sweep                     #   full gen-len + sweep pipeline
│   └── prepare-speedbench        #   split SPEED-Bench flat files
├── plot                          # visualization group
│   ├── compare                   #   multi-version comparison overlay
│   └── speedup                   #   pairwise speedup gradient chart
├── convert                       # convert external models → speculators format (existing)
└── --version / --help
```

**8 top-level commands, max depth = 2.** Pipeline phases are listed first in `--help`; `convert` is grouped separately as a tool.

**Help layout:**

```
╭─ Pipeline ───────────────────────────────────────────────────────────────╮
│ regenerate-responses  Regenerate assistant responses on-policy via vLLM  │
│ prepare-data          Preprocess a dataset for speculator training       │
│ generate-data         Generate hidden states offline from a vLLM server │
│ train                 Train a speculator model                          │
│ stitch                Stitch MTP weights back into a verifier           │
│ eval                  Evaluate speculative decoding performance         │
│ plot                  Visualize evaluation results                      │
╰─────────────────────────────────────────────────────────────────────────╯
╭─ Tools ─────────────────────────────────────────────────────────────────╮
│ convert               Convert models to speculators format              │
╰─────────────────────────────────────────────────────────────────────────╯
```

#### Workflow paths

Three supported workflows use the same command tree:

| Workflow | Steps |
|---|---|
| **Online** (live vLLM) | `prepare-data` → *(launch vLLM externally)* → `train` → `stitch` → `eval` → `plot` |
| **Offline** (pre-generated hidden states) | `prepare-data` → *(launch vLLM externally)* → `generate-data` → `train` → `stitch` → `eval` → `plot` |
| **On-policy** (regenerated responses) | *(launch vLLM externally)* → `regenerate-responses` → `prepare-data` → `train` → `stitch` → `eval` → `plot` |

The on-policy workflow can combine with either online or offline training — `regenerate-responses` produces pretokenized JSONL that `prepare-data` passes through without re-tokenizing.

`launch_vllm.py` stays outside the command tree as a standalone script invoked in the vLLM environment (see [vLLM integration](#vllm-integration-approach) below).

---

#### Command reference

<details>
<summary><b>speculators regenerate-responses</b> — Regenerate assistant responses on-policy via a vLLM server</summary>

Takes a conversational dataset, strips original assistant responses, and regenerates them through a running vLLM server. Outputs pretokenized JSONL with `input_ids` and `loss_mask` that `prepare-data` passes through without re-tokenizing — this is the on-policy training path.

```bash
# Basic usage (vLLM server already running)
speculators regenerate-responses \
    --dataset ultrachat \
    --outfile ./regen-ultrachat.jsonl

# With sampling parameters and concurrency tuning
speculators regenerate-responses \
    --dataset ultrachat \
    --endpoint http://gpu-node:8000/v1/chat/completions \
    --concurrency 128 \
    --max-tokens 4096 \
    --sampling-params '{"temperature": 0.6, "top_p": 0.95}' \
    --outfile ./regen-ultrachat.jsonl

# Resume after interruption
speculators regenerate-responses \
    --dataset ultrachat \
    --outfile ./regen-ultrachat.jsonl \
    --resume

# Filter to a specific language subset
speculators regenerate-responses \
    --dataset ultrachat \
    --language-filter EN \
    --limit 10000 \
    --outfile ./regen-ultrachat-en.jsonl
```

**Current**: `python scripts/response_regeneration/script.py --dataset ... --outfile ...`

| Flag | Type | Default | Description |
|---|---|---|---|
| `--endpoint` | str | `http://127.0.0.1:8000/v1/chat/completions` | vLLM OpenAI-compatible Chat Completions endpoint |
| `--model` | str | auto-detected | Model name exposed by the vLLM server |
| `--dataset` | str | `ultrachat` | Dataset to process (see supported datasets below) |
| `--split` | str | dataset default | Dataset split |
| `--subset` | str | dataset default | Dataset subset/config name |
| `--limit` | int | None | Stop after N rows |
| `--concurrency` | int | 64 | Max concurrent requests to the server |
| `--max-tokens` | int | 8192 | `max_tokens` for generation |
| `--sampling-params` | JSON str | `{}` | JSON object merged into each chat-completion request |
| `--outfile` | str | `{dataset}_{model}.jsonl` | Output JSONL path |
| `--resume` | flag | false | Skip rows already in outfile (matched by stable primary id) |
| `--language-filter` | str | None | Only process rows where language matches (e.g. `EN`) |
| `--max-retries` | int | 3 | Max retry attempts per request on transient failure |

**Supported datasets:** `sharegpt`, `ultrachat`, `gsm8k`, `magpie`, `nemotron`, `open-perfectblend`, `hermes-fc`. Dataset configurations (HF path, subset, split, normalization) are defined in the shared `DATASET_CONFIGS` registry. Multimodal datasets (e.g. `sharegpt4v_coco`) are rejected with a descriptive error.

**Output format:** JSONL with fields `id`, `primary_id`, `input_ids`, `loss_mask`, `text`, `metadata`. Errors are written to a sibling `.errors.jsonl` file. The `input_ids`/`loss_mask` format is directly consumed by `prepare-data`'s passthrough path — no re-tokenization needed.

**Tool-call support:** If the source dataset contains `tools`, they are forwarded in the chat-completion request. Tool calls in the response are paired positionally with cached tool results from the source data.

</details>

<details>
<summary><b>speculators prepare-data</b> — Tokenize, mask, and compute token frequency statistics</summary>

```bash
# Basic usage
speculators prepare-data \
    --model meta-llama/Llama-3.1-8B-Instruct \
    --data /path/to/train.jsonl \
    --output ./prepared-data

# Multiple data files, custom sequence length
speculators prepare-data \
    --model meta-llama/Llama-3.1-8B-Instruct \
    --data file1.jsonl --data file2.jsonl \
    --seq-length 4096 \
    --max-samples 10000 \
    --output ./prepared-data
```

**Current**: `python scripts/prepare_data.py --model ... --data ... --output ...`

| Flag | Type | Default | Description |
|---|---|---|---|
| `--model` | str | *required* | HuggingFace model ID or local path |
| `--data` | str (repeatable) | *required* | Path(s) to training data |
| `--output` | str | `./output` | Output directory |
| `--seq-length` | int | 8192 | Maximum sequence length |
| `--max-samples` | int | None | Max samples to process |
| `--token-freq-path` | str | None | Custom path for token frequency file |
| `--assistant-pattern` | str | None | Custom regex for assistant responses |
| `--seed` | int | 0 | Random seed |
| `--num-preprocessing-workers` | int | 8 | CPU processes for preprocessing |
| `--minimum-valid-tokens` | int | None | Drop samples below this trainable token count |
| `--overwrite` | flag | false | Delete existing output before running |
| `--allow-empty-output` | flag | false | Allow empty dataset output |
| `--trust-remote-code` | flag | false | Allow executing code from HF Hub |

</details>

<details>
<summary><b>speculators generate-data</b> — Generate hidden states offline from a running vLLM server</summary>

```bash
# Basic usage (vLLM server already running)
speculators generate-data \
    --preprocessed-data ./prepared-data \
    --output ./hidden-states

# Multi-node generation
speculators generate-data \
    --preprocessed-data ./prepared-data \
    --endpoint http://gpu-node:8000/v1 \
    --concurrency 64 \
    --world-size 2 --rank 0
```

**Current**: `python scripts/data_generation_offline.py --preprocessed-data ... --output ...`

| Flag | Type | Default | Description |
|---|---|---|---|
| `--model` | str | None | Model ID for verification (auto-detected) |
| `--endpoint` | str | `http://localhost:8000/v1` | vLLM server endpoint |
| `--preprocessed-data` | str | `./output` | Path to prepared dataset |
| `--output` | str | None | Output directory (default: `<preprocessed>/hidden_states`) |
| `--max-samples` | int | None | Max samples to process |
| `--concurrency` | int | 32 | Active vLLM requests at a time |
| `--validate-outputs` | flag | false | Validate generated files |
| `--request-timeout` | float | (default) | Per-request timeout in seconds |
| `--max-retries` | int | (default) | Retry attempts per request |
| `--fail-on-error` | flag | false | Abort on any failure after retries |
| `--max-consecutive-errors` | int | None | Abort after N consecutive failures |
| `--world-size` | int | 1 | Number of nodes for multi-node generation |
| `--rank` | int | 0 | Node index in multi-node setup |

</details>

<details>
<summary><b>speculators train</b> — Train a speculator model</summary>

Uses the existing `TrainConfig` pydantic schema (#833) with YAML config + CLI flag overrides (flags win over YAML, YAML wins over defaults).

```bash
# Single-GPU with config file
speculators train config.yaml

# Single-GPU with CLI overrides
speculators train config.yaml --num_epochs 3 --lr 1e-4

# Distributed training (DDP/FSDP) — torchrun stays external
torchrun --standalone --nproc_per_node=4 -m speculators.train config.yaml

# Multi-node distributed
torchrun --nnodes 2 --nproc_per_node 4 \
    --node_rank 0 --master_addr head-node --master_port 29500 \
    -m speculators.train config.yaml --num_epochs 5
```

**Current**: `torchrun --standalone --nproc_per_node=<N> scripts/train.py [config.yaml] [--flags]`

| Invocation | Entry path | Use case |
|---|---|---|
| `speculators train config.yaml [overrides]` | typer → `speculators.train.cli:main` | Single-GPU convenience |
| `torchrun -m speculators.train config.yaml [overrides]` | `speculators/train/__main__.py` → same `main` | Distributed (DDP/FSDP) |

Training flags are defined by `TrainConfig` (pydantic schema) and are intentionally **not duplicated here** — the config schema is the source of truth. Run `speculators train --help` for the full flag list, or see `configs/examples/` for annotated example configs.

</details>

<details>
<summary><b>speculators stitch</b> — Stitch finetuned MTP weights back into a verifier checkpoint</summary>

```bash
speculators stitch ./finetuned-checkpoint Qwen/Qwen3-Next-80B-A3B-Instruct

# Custom output path
speculators stitch ./finetuned-checkpoint Qwen/Qwen3-Next-80B-A3B-Instruct \
    --output-path ./my-stitched-model
```

**Current**: `python scripts/stitch_mtp.py <finetuned_checkpoint> <verifier_path> [--output-path ...]`

Already uses typer. Arguments and behavior are unchanged.

| Argument / Flag | Type | Default | Description |
|---|---|---|---|
| `FINETUNED_CHECKPOINT` | Path (positional) | *required* | Path to the finetuned MTP checkpoint |
| `VERIFIER_PATH` | Path (positional) | *required* | Path or HF model ID of the verifier |
| `--output-path` | Path | `{verifier-name}-stitched` | Output directory |

</details>

<details>
<summary><b>speculators eval throughput / sweep / prepare-speedbench</b> — Evaluation commands</summary>

**`eval throughput`** — Max-rate acceptance-rate evaluation run:

```bash
speculators eval throughput \
    --target http://localhost:8000/v1 \
    --dataset nvidia/speculators-SPEED-bench \
    --max-concurrency 64
```

**`eval sweep`** — Full gen-len estimation + rate sweep pipeline:

```bash
speculators eval sweep \
    --target http://localhost:8000/v1 \
    --subsets "HumanEval,qa" \
    --output-dir ./results
```

**`eval prepare-speedbench`** — Split SPEED-Bench flat files into per-category JSONL:

```bash
speculators eval prepare-speedbench \
    --data-dir ./speedbench-data \
    --download
```

**Current**: `python scripts/evaluate/evaluate.py --target ... throughput|sweep` and `python scripts/evaluate/prepare_speedbench.py`

**Shared eval flags** (apply to both `throughput` and `sweep`):

| Flag | Type | Default | Description |
|---|---|---|---|
| `--target` | str | *required* | vLLM server endpoint |
| `--dataset` | str | `RedHatAI/speculator_benchmarks` | HF dataset ID or local directory |
| `--subsets` | str | all 9 standard subsets | Comma-separated subset names |
| `--output-dir` | str | `<model>_TIMESTAMP` | Output directory |
| `--max-concurrency` | int | 128 | Max concurrent requests |
| `--max-requests` | int | 200 | Max requests per sweep point |
| `--gen-len-rate` | int | 128 | Request rate for gen-len estimation |
| `--sweep-rate` | int | 10 | Number of sweep rate points |
| `--gen-kwargs` | str | `""` | JSON generation kwargs |

**prepare-speedbench flags:**

| Flag | Type | Default | Description |
|---|---|---|---|
| `--data-dir` | Path | *required* | Directory with flat JSONL files |
| `--configs` | str | all configs | Comma-separated configs to split |
| `--download` | flag | false | Download and run NVIDIA's prepare.py first |

</details>

<details>
<summary><b>speculators plot compare / speedup</b> — Visualization commands</summary>

**`plot compare`** — Overlay smoothed performance curves for multiple model versions:

```bash
speculators plot compare \
    --source "No Spec=nospec/results.csv" \
    --source "Eagle3=eagle3/results.csv" \
    --metric latency
```

**`plot speedup`** — Pairwise speedup visualization with gradient shading:

```bash
speculators plot speedup \
    --baseline "No Spec=nospec/results.csv" \
    --target "Eagle3=eagle3/results.csv" \
    --metric latency \
    --title "Llama-3.1-8B"
```

| Flag | Type | Default | Description |
|---|---|---|---|
| `--source` / `--baseline` / `--target` | str (repeatable) | *required* | Version data as `Label=path` |
| `--metric` | str (repeatable) | latency | Metric(s) to plot |
| `--output-dir` | Path | `.` | Directory for output PNGs |
| `--subsets` | str | all found | Comma-separated subset filter |
| `--title` | str | None | Optional title prefix for plots |

</details>

<details>
<summary><b>speculators convert</b> — Convert external models (existing, unchanged)</summary>

```bash
speculators convert "yuhuili/EAGLE-LLaMA3.1-Instruct-8B" \
    --algorithm eagle \
    --verifier "meta-llama/Llama-3.1-8B-Instruct"
```

Already implemented. No changes needed.

</details>

---

#### Distributed training (torchrun integration)

The `train` command is the only one that needs distributed support. The design keeps torchrun external rather than wrapping it:

```bash
# Single GPU — typer entry point
speculators train config.yaml

# Multi-GPU on one node
torchrun --standalone --nproc_per_node=4 -m speculators.train config.yaml

# Multi-node
torchrun --nnodes 2 --nproc_per_node 4 \
    --node_rank 0 --master_addr head-node --master_port 29500 \
    -m speculators.train config.yaml
```

**Implementation**: `speculators/train/__main__.py` calls the same `main()` as the typer wrapper. The existing `TrainConfig.resolve()` argparse machinery works identically under `-m` invocation.

#### vLLM integration approach

`launch_vllm.py` stays **outside the CLI** as a standalone script invoked in the vLLM environment:

- The vLLM and speculators environments are typically separate (torch/transformers version mismatches)
- The script imports nothing from the `speculators` package
- Adding it to the CLI would require installing speculators in the vLLM env, risking dependency conflicts

The CLI documents `launch_vllm.py` as a companion script. The online workflow shows it as an explicit external step between `prepare-data` and `train`.

#### CLI framework

**Typer** — already in use for `convert` and `stitch`. All new commands use typer. The existing dependencies (`typer>=0.12.0`, `click`, `rich`) are already declared in `pyproject.toml`.

**Why `train` is the exception:** The config-file-first RFC (#833) explicitly evaluated and rejected typer for the training CLI. The blocker is `nargs='+'` — space-separated multi-value flags like `--target-layer-ids 2 18 33` and `--full-attention-indices 2 18 33`. Typer/click cannot reproduce this syntax without click-level surgery, and changing it would break existing `examples/train/*.sh` recipes.

The `speculators train` command is therefore a **thin typer dispatch wrapper** — typer registers `train` as a subcommand (so it appears in `speculators --help`), but all argument parsing is delegated to `TrainConfig.resolve()` (argparse internally). Typer never sees train's flags.

```python
# Sketch — typer dispatches, argparse parses
@app.command(context_settings={"allow_extra_args": True, "allow_interspersed_args": False})
def train(ctx: typer.Context):
    from speculators.train.cli import main
    main(TrainConfig.resolve(ctx.args))
```

This does not affect the other commands. None of them use `nargs='+'`:
- `prepare-data` and `plot` use `action="append"` (repeated `--flag val1 --flag val2`), which maps cleanly to typer's `List[str]`
- All other flags are single-value scalars or boolean flags

#### Packaging: scripts move into the package

Every pipeline script's core logic moves into the `speculators` package so `pip install speculators` provides the full CLI without cloning the repo.

| Command | Current location | Package location | Script becomes |
|---|---|---|---|
| `regenerate-responses` | `scripts/response_regeneration/script.py` | `speculators.data_generation.regeneration` | backward-compat shim |
| `prepare-data` | `scripts/prepare_data.py` | `speculators.data.cli` | backward-compat shim |
| `generate-data` | `scripts/data_generation_offline.py` | `speculators.data.generate` | backward-compat shim |
| `train` | `scripts/train.py` | `speculators.train.cli` | backward-compat shim |
| `stitch` | `scripts/stitch_mtp.py` | `speculators.stitch` | backward-compat shim |
| `eval throughput/sweep` | `scripts/evaluate/evaluate.py` | `speculators.eval.cli` | backward-compat shim |
| `eval prepare-speedbench` | `scripts/evaluate/prepare_speedbench.py` | `speculators.eval.speedbench` | backward-compat shim |
| `plot compare/speedup` | `scripts/evaluate/plot.py` | `speculators.eval.plot` | backward-compat shim |

#### Scripts excluded from the package

The following scripts remain standalone in `scripts/` and are **not** migrated. The inclusion principle is **workflow-step membership**: a script earns a CLI command only when it is a step users walk through in the end-to-end speculative decoding workflow.

| Script | Why it stays out |
|---|---|
| `scripts/launch_vllm.py` | Runs in a **separate vLLM environment**. Imports nothing from `speculators`. Packaging it would force users to install speculators in the vLLM env, risking dependency conflicts. |
| `scripts/benchmark.py` | **Contributor/developer tool** for measuring training throughput — different audience than end users. |
| `scripts/build_vocab_mapping.py` | **Vestigial** — the core function is already called internally by `train.py`. The script exists as a standalone escape hatch for rare manual runs. |
| `scripts/response_regeneration/run_all.sh` | **Server lifecycle wrapper** — manages starting/stopping a vLLM server around `regenerate-responses`. Same rationale as `launch_vllm.py`: server management belongs outside the CLI. |

#### Migration guide

| Before | After |
|---|---|
| `python scripts/response_regeneration/script.py --dataset D` | `speculators regenerate-responses --dataset D` |
| `python scripts/prepare_data.py --model M --data D` | `speculators prepare-data --model M --data D` |
| `python scripts/data_generation_offline.py --preprocessed-data P` | `speculators generate-data --preprocessed-data P` |
| `torchrun ... scripts/train.py config.yaml` | `torchrun ... -m speculators.train config.yaml` |
| `python scripts/train.py config.yaml` | `speculators train config.yaml` |
| `python scripts/stitch_mtp.py CKPT VERIFIER` | `speculators stitch CKPT VERIFIER` |
| `python scripts/evaluate/evaluate.py --target T throughput` | `speculators eval throughput --target T` |
| `python scripts/evaluate/evaluate.py --target T sweep` | `speculators eval sweep --target T` |
| `python scripts/evaluate/prepare_speedbench.py --data-dir D` | `speculators eval prepare-speedbench --data-dir D` |
| `python scripts/evaluate/plot.py compare --source S` | `speculators plot compare --source S` |
| `python scripts/evaluate/plot.py speedup --baseline B --target T` | `speculators plot speedup --baseline B --target T` |
| `python scripts/launch_vllm.py ...` | *(unchanged — standalone script)* |

All `scripts/*.py` files are retained as backward-compatible shims that import and call the package entry point. Existing tutorials and CI scripts continue to work without changes.

#### End-to-end example session

```bash
# 0. (Optional) Regenerate responses on-policy
# Requires a running vLLM server
speculators regenerate-responses \
    --dataset ultrachat \
    --endpoint http://localhost:8000/v1/chat/completions \
    --outfile ./regen-ultrachat.jsonl

# 1. Prepare data
speculators prepare-data \
    --model meta-llama/Llama-3.1-8B-Instruct \
    --data ./regen-ultrachat.jsonl \
    --output ./prepared

# Or prepare from raw data (skipping regeneration)
speculators prepare-data \
    --model meta-llama/Llama-3.1-8B-Instruct \
    --data /data/train.jsonl \
    --output ./prepared

# 2. Launch vLLM server (in vLLM environment — separate step)
python scripts/launch_vllm.py meta-llama/Llama-3.1-8B-Instruct --port 8000

# 3a. Train online (single GPU)
speculators train configs/examples/eagle_online.yaml \
    --data-path ./prepared

# 3b. Or: generate offline data, then train
speculators generate-data --preprocessed-data ./prepared
speculators train configs/examples/eagle_offline.yaml \
    --data-path ./prepared

# 3c. Distributed training
torchrun --standalone --nproc_per_node=4 \
    -m speculators.train configs/examples/eagle_online.yaml

# 4. Stitch MTP weights (if applicable)
speculators stitch ./checkpoints/best Qwen/Qwen3-Next-80B-A3B-Instruct

# 5. Evaluate
speculators eval sweep --target http://localhost:8000/v1

# 6. Visualize
speculators plot compare \
    --source "Baseline=baseline/results.csv" \
    --source "Eagle3=eagle3/results.csv"
speculators plot speedup \
    --baseline "Baseline=baseline/results.csv" \
    --target "Eagle3=eagle3/results.csv"
```

### Any Other Things.

#### Relationship to prior work

This RFC builds on the config-file-first training CLI (#833), which established the `TrainConfig.resolve()` pattern for layering YAML + CLI flags. That work is implemented and closed. This RFC extends the same approach to the remaining pipeline scripts and unifies everything under a single `speculators` entry point.

#### Open questions for reviewers

1. **`eval` vs `evaluate`**: The command tree uses `eval` for brevity. Should it be `evaluate` for clarity, or is `eval` clear enough in context?
2. **`generate-data` naming**: This command wraps `data_generation_offline.py`. Should it be `generate-data`, `generate-hidden-states`, or something else? The current name is workflow-oriented (what the user is doing); an alternative could be more precise about the output.
3. **Example configs location**: Should example configs live in `configs/examples/` (package-relative, shipped with `pip install`) or `examples/configs/` (repo-relative, not shipped)?

## 评论 (6)

### orestis-z · 2026-08-04

Great proposal!

Some naming feedback:
- tend to prefer `evaluate` more than `eval`. Because if we can make it clearer with +4 chars why not? + keeps it consistent with previous script name (`evaluate.py`)
- would rename `stitch` -> `stitch-mtp` since it's mtp specific
- personally prefer starting by the higher level subject group first, e.g. `data-...` (`data-regen`, `data-prepare`, ...). Makes it easier to skim through a group of interest and keeps same subjects together when alphabetically ordered

### rahul-tuli · 2026-08-04

Planning to implement this via a `feat/cli` feature branch with 7 small, independently-reviewable sub-PRs:

1. **CLI infrastructure** — typer app, `__main__.py`, help groups, entry point
2. **`stitch-mtp`** — move + wire + deprecation shim + tests
3. **`prepare-data`** — move + wire + shim + tests
4. **`generate-data`** — move + wire + shim + tests
5. **`regenerate-responses`** — move + wire + shim + tests + aiohttp dep
6. **`train`** — thin typer dispatch + `speculators.train.__main__` for torchrun + tests
7. **`evaluate` + `plot`** — both subgroups + optional deps + tests

Each sub-PR is a mechanical migration — script logic moves verbatim, no core changes. Naming follows @orestis-z's feedback: `evaluate` (not `eval`), `stitch-mtp` (not `stitch`).

Any concerns with this approach before I start opening sub-PRs?

### rahul-tuli · 2026-08-04

> Planning to implement this via a `feat/cli` feature branch with 7 small, independently-reviewable sub-PRs:
> 
> 1. **CLI infrastructure** — typer app, `__main__.py`, help groups, entry point
> 2. **`stitch-mtp`** — move + wire + deprecation shim + tests
> 3. **`prepare-data`** — move + wire + shim + tests
> 4. **`generate-data`** — move + wire + shim + tests
> 5. **`regenerate-responses`** — move + wire + shim + tests + aiohttp dep
> 6. **`train`** — thin typer dispatch + `speculators.train.__main__` for torchrun + tests
> 7. **`evaluate` + `plot`** — both subgroups + optional deps + tests
> 
> Each sub-PR is a mechanical migration — script logic moves verbatim, no core changes. Naming follows [@orestis-z](https://github.com/orestis-z)'s feedback: `evaluate` (not `eval`), `stitch-mtp` (not `stitch`).
> 
> Any concerns with this approach before I start opening sub-PRs?

@fynnsu @shanjiaz @orestis-z 

### fynnsu · 2026-08-04

I'm not sold on the `evaluate/plot` scripts being included in this change. These scripts have additional dependencies like guidellm which speculators doesn't depend on.

### rahul-tuli · 2026-08-05

> I'm not sold on the `evaluate/plot` scripts being included in this change. These scripts have additional dependencies like guidellm which speculators doesn't depend on.

I was thinking of including an additional 'speculators[eval]' installable, but we can exclude it from this initial work

### rahul-tuli · 2026-09-01

Merged as of #1024 
