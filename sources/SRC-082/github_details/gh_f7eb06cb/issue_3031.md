# [Issue #3031] [BUG] QQQ quantization causes cumulative CPU swap growth on large MoE models

source: https://github.com/ModelCloud/GPTQModel/issues/3031
state: closed | updated: 2026-08-28T00:43:30Z
labels: bug

## 正文


## Problem

QQQ quantization causes cumulative anonymous memory and swap growth when quantizing large MoE models.

I reproduced this while quantizing Qwen3.5-35B-A3B with disk offloading, synchronous submodule finalization, and one expert processed at a time. `VmSwap` continued to increase after every transformer layer instead of returning to a stable level.

By layer 13, the process had accumulated approximately:

- 138 GiB of `VmSwap`
- 18,000 anonymous VMAs

The process eventually failed while mapping a checkpoint shard:

```text
RuntimeError: unable to mmap 2224764664 bytes ...
Cannot allocate memory (12)
```

Reducing the calibration sample count and expert batch size did not stop the per-layer swap growth.

## Environment

- Model: Qwen3.5-35B-A3B
- Quantization: QQQ W4A8
- `bits=4`
- `group_size=-1`
- `sym=True`
- `device="cuda"`
- `offload_to_disk=True`
- `wait_for_submodule_finalizers=True`
- `ExpertsRoutingBypass(batch_size=1)`
- `GPTQMODEL_CPU_WORKERS=2`
- Transformers: 5.15.0
- Linux with limited physical RAM and swap enabled

## Reproduction

my `quantize_qwen3_5_moe_qqq_w4a8.py` file like

```python
import argparse
from pathlib import Path

from datasets import load_dataset

from gptqmodel import BACKEND, GPTQModel
from gptqmodel.quantization.config import (
    ExpertsRoutingBypass,
    MoEConfig,
    QQQConfig,
)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Quantize Qwen3.5 MoE to QQQ W4A8"
    )
    parser.add_argument(
        "--model",
        type=lambda path: str(Path(path).expanduser()),
        default="~/models/Qwen3.5-35B-A3B",
        help="Source Qwen3.5 MoE model directory",
    )
    parser.add_argument(
        "--output",
        type=lambda path: str(Path(path).expanduser()),
        default="~/models/Qwen3.5-35B-A3B-QQQ-W4A8-per-channel",
        help="Output directory",
    )
    parser.add_argument(
        "--offload-path",
        type=lambda path: str(Path(path).expanduser()),
        help="Optional local NVMe directory for disk offload",
    )
    parser.add_argument("--samples", type=int, default=256)
    parser.add_argument("--batch-size", type=int, default=1)
    parser.add_argument("--sequence-length", type=int, default=2048)
    parser.add_argument(
        "--expert-batch-size",
        type=int,
        default=1,
        help="Number of expert modules calibrated concurrently",
    )
    parser.add_argument(
        "--desc-act",
        action="store_true",
        help="Enable activation-order quantization after the baseline run succeeds",
    )
    parser.add_argument(
        "--calibration-file",
        type=Path,
        help="Optional UTF-8 text file with one calibration sample per line",
    )
    return parser.parse_args()


def load_calibration(args):
    if args.calibration_file:
        samples = [
            line.strip()
            for line in args.calibration_file.expanduser()
            .read_text(encoding="utf-8")
            .splitlines()
            if line.strip()
        ]
        if not samples:
            raise ValueError("Calibration file contains no non-empty samples")
        return samples[: args.samples]

    dataset = load_dataset(
        "wikitext",
        "wikitext-2-raw-v1",
        split="train",
    )
    samples = [text for text in dataset["text"] if len(text.split()) >= 20]
    return samples[: args.samples]


def main():
    args = parse_args()
    quantize_config = QQQConfig(
        bits=4,
        group_size=-1,
        sym=True,
        desc_act=args.desc_act,
        device="cuda",
        offload_to_disk=True,
        offload_to_disk_path=args.offload_path,
        wait_for_submodule_finalizers=True,
        rotation=None,
        auto_forward_data_parallel=False,
        moe=MoEConfig(
            routing=ExpertsRoutingBypass(batch_size=args.expert_batch_size)
        ),
    )

    model = GPTQModel.load(
        args.model,
        quantize_config=quantize_config,
    )
    model.quantize(
        load_calibration(args),
        batch_size=args.batch_size,
        calibration_concat_size=args.sequence_length,
        backend=BACKEND.QQQ,
    )
    model.save(args.output)
    print(f"Saved Qwen3.5 MoE QQQ W4A8 model to {args.output}")


if __name__ == "__main__":
    main()

```

and run : 

```bash
python quantize_qwen3_5_moe_qqq_w4a8.py \
    --model   ~/models/Qwen3.5-35B-A3B \
    --output ~/models/Qwen3.5-35B-A3B-QQQ-W4A8-per-channel \
    --offload-path ./qqq-offload-qwen3.5-35B-A3B \
```

As the program runs, you can see that by layer 13, the process had accumulated approximately:

- about 138 GiB of VmSwap

- 18,000 anonymous VMAs

This is unreasonable.

## Analysis

I found two sources of excessive memory retention.

### 1. QQQ quantization state is not released after each module

`QQQProcessor.process()` calls `QQQ.quantize()` but does not call `QQQ.free()` afterward.

The QQQ task can therefore continue to hold temporary state such as:

- the Hessian matrix;
- device Hessian partials;
- the quantizer;
- module copies;
- loss and trace buffers.

The GPTQ processor already releases its task state after processing each module.

### 2. QQQ packing creates multiple full-size temporary allocations

`QQQLinear.pack()` materializes the complete quantized weight and then creates additional full-size allocations through:

- reshape, permute, and indexing operations;
- conversion to a NumPy `uint32` array;
- a separate NumPy packed output;
- conversion from `uint32` to `int32`;
- conversion back to a Torch tensor.

For models containing thousands of expert projections, the allocator can retain these anonymous mappings after each pack operation. This appears as steadily increasing swap usage even after the temporary Python objects are no longer reachable.

## Proposed fix

I opened [PR #3029](https://github.com/ModelCloud/GPTQModel/pull/3029), which:

- releases QQQ temporary state in a `finally` block after each module is quantized;
- packs weights in bounded input and output chunks;
- writes chunks directly into the final CPU `int32` buffer;
- replaces full-size NumPy packing arrays with Torch bitwise operations;
- preserves the existing Marlin packed layout and quantization semantics.

The generated packed weights were compared against the previous implementation for:

- `group_size=-1`;
- `group_size=128`;
- dimensions crossing input and output chunk boundaries;
- FP16 and BF16 source weights.

The resulting packed weights and scales were bit-exact in these focused checks. The existing `tests/test_qqq_jit.py` suite also passed.

A complete Qwen3.5-35B-A3B run with the proposed changes has not yet been used to demonstrate that the layer-by-layer swap growth is fully eliminated. The PR addresses the identified allocation sources, but full-model memory validation is still required.

## Expected behavior

Temporary memory used for one QQQ module should be released or reused after that module is completed. Memory and swap usage should reach a bounded plateau rather than increasing approximately linearly with the number of completed transformer layers.

## Additional context

This is separate from asynchronous finalizer accumulation. `wait_for_submodule_finalizers=True` was enabled, so each layer's finalizers completed before processing the next layer.

Could the maintainers confirm whether the task lifecycle and chunked packing approach in [PR #3029](https://github.com/ModelCloud/GPTQModel/pull/3029) are acceptable? I can adjust the implementation or add targeted regression tests based on feedback.





## 评论 (1)

### Qubitium · 2026-08-28

@yujiongzhang Thanks for the clean PR fix. Closing this issue as completed.
