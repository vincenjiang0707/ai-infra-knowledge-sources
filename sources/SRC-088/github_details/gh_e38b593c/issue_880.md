# [Issue #880] [RFC] Add reproducibility artifacts to eval runs and checkpoints

source: https://github.com/vllm-project/speculators/issues/880
state: open | updated: 2026-07-30T15:29:13Z
labels: enhancement, RFC

## 正文

## Motivation

Evaluation results are currently not reproducible from their output alone. The eval script (`scripts/evaluate/evaluate.py`) produces only benchmark data (`acceptance.csv`, `perf_results.csv`, raw guidellm JSONs) — no metadata about the environment, command, or code state that produced them.

This caused unnecessary re-work in #757 where we couldn't determine which vLLM patches had been applied to original eval runs. Training already records provenance via `save_train_command()` — evaluation has no equivalent.

## Artifact Summary

| Artifact | Script | Default Location | Format |
|---|---|---|---|
| `train_command.txt` | `train/utils.py` | `<checkpoint_dir>/` | `shlex.join(sys.argv)` |
| `eval_command.txt` | `evaluate.py` | `<output_dir>/` | Header (timestamp, git SHA, package versions) + `shlex.join(sys.argv)` |
| `vllm_command.txt` | `launch_vllm.py` | `vllm_<model>_<ts>/` | Header (timestamp, python, git SHA, vllm version) + `shlex.join(cmd)` |
| `vllm.patch` | `launch_vllm.py` | `vllm_<model>_<ts>/` | `# repo: <path> (<sha>)` + `git diff HEAD` |
| `checkpoint_sha256.txt` | `launch_vllm.py` | `vllm_<model>_<ts>/` | `<sha256>  <filename>` per `.safetensors` file |
| `speculators.patch` | `train/utils.py` | `<checkpoint_dir>/` | `git diff HEAD` |

`launch_vllm.py` provenance location is overridable with `--provenance-dir` to co-locate with eval results.

## Proposed Changes

### 1. `eval_command.txt` — eval metadata file

Mirror the existing `save_train_command()` pattern. Write to the eval output directory:
- Timestamp (UTC ISO 8601)
- Speculators git SHA
- Package versions (speculators, vllm, transformers, torch, compressed-tensors)
- Full `sys.argv` eval command

**Integration point:** `run_benchmark()` in `evaluate.py`, right after `artifacts_dir.mkdir()`.

### 2. `vllm_command.txt` + `vllm.patch` + `checkpoint_sha256.txt` — vLLM provenance

Written by `launch_vllm.py` (not the eval script) to keep concerns separated — the eval script doesn't know how vLLM was launched.

- `vllm_command.txt`: full constructed command + metadata header (timestamp, python path, git SHA, vllm version)
- `vllm.patch`: `git diff HEAD` from the vLLM source tree (auto-discovered by walking up from the installed package, falling back to `~/vllm` and `/workspace/vllm`). Header-only when the checkout is clean. Records version string when installed from a wheel.
- `checkpoint_sha256.txt`: SHA256 of all `.safetensors` files for local checkpoints, or a comment noting the model is a remote reference.

`launch_vllm.py` always saves provenance — defaults to `vllm_<model>_<YYYYMMDD_HHMMSS>/`, overridable with `--provenance-dir`.

### 3. `speculators.patch` — speculators diff artifact

Add `git diff HEAD` from the speculators repo root to `<checkpoint_dir>/` alongside the existing `train_command.txt`. This captures uncommitted changes at training time so the diff travels with the checkpoint (useful for HF uploads).

## Implementation Notes

- All artifacts are best-effort (wrapped in try/except) — failure to capture provenance never blocks training or evaluation.
- Atomic writes via tempfile + rename, matching the existing `save_train_command()` pattern.
- For wheel installs (no git checkout), the version string is recorded and no diff is available.

## 评论 (3)

### rahul-tuli · 2026-07-30

The RFC is well thought out and serves a real purpose, some thoughts:

1. SHA256 of all `.safetensors` on every launch is a critical-path cost.      
   `launch_vllm.py` hashes checkpoints before starting the server, and the RFC   
   says it "always saves provenance." For a 100GB+ local checkpoint that's     
  quite a bit of disk I/O added to every launch, on a script whose whole job is to
   start a server quickly. Suggestion: maybe make hashing opt-in (`--hash-checkpoints`),  
   or record size + mtime by default and full hashes only on request.

2. Git SHA is resolved from the caller's cwd. The existing                  
   `save_train_command()` runs `git rev-parse HEAD` with inherited `cwd` if eval is
   launched from outside the speculators checkout, the header records unknown  
   (or worse, the wrong repo's SHA). The new writers should anchor git commands
   to the repo root derived from `speculators.__file__` via `cwd=`

I know `launch_vllm.py` and the `train.py` would be invoked in different environments, but it would be nice to have a shared helper utility if possible

### orestis-z · 2026-07-30

@rahul-tuli thanks for your feedback! Good point about the hashing of large checkpoints. I'd lean toward a middle ground: keep hashing on by default but add `--no-hash-checkpoints` to skip it, rather than making it opt-in. That way provenance is complete out of the box (the whole point of the RFC), and people who hit the I/O cost on large models can opt out. Wdyt?

### rahul-tuli · 2026-07-30

> [@rahul-tuli](https://github.com/rahul-tuli) thanks for your feedback! Good point about the hashing of large checkpoints. I'd lean toward a middle ground: keep hashing on by default but add `--no-hash-checkpoints` to skip it, rather than making it opt-in. That way provenance is complete out of the box (the whole point of the RFC), and people who hit the I/O cost on large models can opt out. Wdyt?

Sounds good, that works too! We can skip hashing for large checkpoints
