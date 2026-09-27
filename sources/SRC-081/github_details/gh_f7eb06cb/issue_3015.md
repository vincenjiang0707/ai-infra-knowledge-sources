# [Issue #3015] Concurrent quantize() processes on the same machine can hang indefinitely (shared pack_block_cpu JIT extension build directory is not process-isolated)

source: https://github.com/ModelCloud/GPTQModel/issues/3015
state: closed | updated: 2026-09-06T09:23:00Z
labels: bug

## 正文

## Summary

Running two independent `GPTQModel.quantize()` processes at the same time on the same host (different models, different GPUs, each pinned via `CUDA_VISIBLE_DEVICES` to its own physical GPU) causes each process to eventually hang indefinitely — no exception, no crash, no further log output, GPU utilization drops to 0%, and the process's own CPU usage drops to ~0%. This happened independently to *both* concurrent processes (at different points in their respective runs, ~30-90 minutes in), not just one.

## Environment

```
GPT-QModel   : 7.3.4
Transformers : 5.14.1
Torch        : 2.13.0+cu130
Triton       : 3.7.1
Python       : 3.14.7 free-threading build (PYTHON_GIL=0)
OS           : Linux 7.0.0-28-generic (Ubuntu 20.04), glibc 2.39
GPU          : 4x NVIDIA RTX 3090 (24GB each)
```

Models: `Qwen/Qwen3.6-27B` and `Qwen/Qwen3.8-27B` (both `model_type: "qwen3_5"`, dense, hybrid full/linear attention). GPTQ, bits=4, group_size=128, `calibration_data_device="cpu"`, `dense_vram_strategy="exclusive"`, `offload_to_disk=True`.

## Setup

Two separate OS processes, launched a few minutes apart, each with its own `CUDA_VISIBLE_DEVICES` so they are fully isolated at the GPU level:

```bash
# process A
CUDA_VISIBLE_DEVICES=0 PYTHON_GIL=0 python quantize_qwen36.py   # dense_vram_strategy_devices=["cuda:0"]

# process B
CUDA_VISIBLE_DEVICES=1 PYTHON_GIL=0 python quantize_qwen38.py   # dense_vram_strategy_devices=["cuda:0"]  (i.e. physical GPU1)
```

Same Python venv / same GPTQModel install for both processes.

## Observed hang

- Process A stalled ~30 min into its run, mid-layer (`Forward: Layer=...layers.38, subset=5/5, batches=256 Forward` was the last line ever written).
- Process B (started later) independently stalled ~60 min into its own run, also mid-layer forward pass.
- In both cases: no Python exception, no traceback, `nvidia-smi` showed 0% utilization on the process's GPU, and sampling `/proc/<pid>/stat` over a 5s window showed ~0 jiffies of CPU time consumed (i.e. genuinely idle/blocked, not just slow).
- Both processes had already run for dozens of layers without issue before hanging.
- GPTQModel's own resume feature (`GPTQMODEL_RESUME=1` + `offload_to_disk_path`) let us confirm exactly how far each process got and restart cleanly from the last completed layer both times.

## Suspected root cause

Both processes' logs reference the **exact same** JIT build directory for the CPU packing extension:

```
/home/user0/.cache/gptqmodel/torch_extensions/pack_block_cpu/0701273d21c35c6c
```

(identical hash — expected, since both processes share the same venv/torch/source, and `default_torch_ops_build_root()` in `gptqmodel/utils/cpp.py` keys this path only by extension name + `GPTQMODEL_TORCH_EXTENSIONS_DIR`/home dir, with no process- or run-unique component.)

At the time we investigated (after both hangs), this directory existed but was **empty** (no `.so`, no `build.ninja`, nothing) — consistent with an interrupted/raced JIT build. We're aware this general area has had several fixes already (#2234/#2248, #2749, #2969, #3005, #3008, #3009 — all present in our installed commit), but none of them appear to address two independent *processes* sharing the same on-disk build cache directory concurrently; the locking added in those fixes (`threading.Lock`, e.g. `_TORCH_OPS_JIT_LOCK` in `gptqmodel/utils/cpp.py`) is process-local and cannot serialize two separate OS processes racing on the same directory.

We were not able to get a Python-level stack trace to confirm this with certainty (no `ptrace`/root access on the shared machine), so this is our best-supported hypothesis rather than a confirmed root cause — happy to help gather more diagnostics if useful.

## Workaround that resolved it for us

Setting `GPTQMODEL_TORCH_EXTENSIONS_DIR` to a distinct path per process before relaunching (with `GPTQMODEL_RESUME=1` to continue from the last completed layer) fixed it — both processes have since run for hours without a repeat hang:

```bash
# process A
GPTQMODEL_TORCH_EXTENSIONS_DIR=/home/user0/.cache/gptqmodel_ext_a ...

# process B
GPTQMODEL_TORCH_EXTENSIONS_DIR=/home/user0/.cache/gptqmodel_ext_b ...
```

## Suggested fix directions

1. Document that concurrent multi-process `quantize()` runs on one host require distinct `GPTQMODEL_TORCH_EXTENSIONS_DIR` values per process (simplest, could just be a docs/README note).
2. And/or make the default build directory include a process-unique component (e.g. PID, or a short random suffix cached for the process's lifetime) so concurrent processes never share a build path by default.
3. And/or add real cross-process locking (e.g. `flock` on a lockfile inside the build directory) around the JIT compile step in `gptqmodel/utils/cpp.py`, rather than relying only on the in-process `threading.Lock`.

Happy to provide the full logs / more repro detail if useful.

## 评论 (10)

### Ndgandhi23 · 2026-08-16

Hey, I'd like to take this one if possible. Planning to add a doc note plus a cross-process file lock fix, and will open a PR soon. This'll be my first PR here.


### Qubitium · 2026-08-18

@Ndgandhi23 Go ahead. @okdshin JIT compile does not have any visibility outside of it's own process so multi-process invocation can lead to bad JIT caching/compile. Not sure what is the best fix here. multi-process aware file-locking or somethig simlar but causes dead-lock resolution/check. If the proces is killed, and the file lock is never released, what happens?

### Ndgandhi23 · 2026-08-18

@Qubitium to answer your question about a killed process, from what I can tell an fcntl.flock lock belongs to the process's open file handle rather than the file, so the kernel drops it when the process dies. I tried it locally by SIGKILLing the holder and the second process acquired right away, so I don't think stale lock cleanup would be needed.

I also noticed that the never released case already exists in torch's own JIT compile step, which uses a lock file with no timeout or pid check. When I killed the process holding it, the next process calling load hung at 0% cpu. This seems a lot like what okdshin described, but I want to double check before claiming that.

So what I was leaning towards, if it makes sense to you, is flock around the JIT load step, remove any leftover torch lock file once we hold it, and a bounded wait that gives up with an error instead of hanging forever. No PR yet, wanted to check this seemed reasonable first.

@okdshin if you still have the logs, did "pack_block_cpu: torch.ops JIT extension ready" ever print after the "compiling" line? And if it happens again, is there a file named lock inside the build dir at hang time? The dir being empty afterwards is the part I can't explain.

### Qubitium · 2026-08-18

@Ndgandhi23 Good stuff. I see no holes in your plan. Lets implement it.

### okdshin · 2026-08-19

Thanks both for jumping on this so quickly and thinking through the fix design, @Ndgandhi23 and @Qubitium — really appreciate it. Follow-up after digging further into this on my end — two things worth flagging before you sink more time into the flock design:

1. **My original report was confounded by local code, not upstream.** On top of upstream GPTQModel (was on `fe8aecb8`), I had a custom, unshipped patch adding mid-run resume/checkpoint support (crash recovery for multi-hour quantization jobs) — this is not part of GPTQModel at all, it's local-only. It touches the per-layer forward/finalize path pretty extensively, and also rewrote the CPU disk-offload path: instead of serializing a module's state directly into its offload directory (which had a wide crash window where the only durable copy of an already-finalized module could be destroyed mid-write), it now writes to a sibling temp dir and swaps it in with two renames, so a crash can never leave a finalized module's on-disk state half-written. So the "shared JIT extension cache" story I originally told you isn't a clean signal — it's entangled with that custom code.

2. **I couldn't reproduce the hang on a clean checkout.** I set up a fresh, completely unmodified `origin/main` clone (no local patches at all) and ran real concurrent quantization jobs (2-3 processes, same models/configs as the original incident, shared default JIT cache dir, real GPU work) for about an hour. Processes made it well past where the original hang first appeared and never stalled. So on vanilla upstream, in a short run, I couldn't reproduce this.

@Ndgandhi23 to answer your two questions directly from the original logs:

- **"ready" message**: never printed, in either of the two hung logs. The only JIT-related lines were the one-time "compiling... failed in 0.0s... using fallback path" at each process's layer 0 (and once more after a resume-restart for one of them). Zero hits for "ready" anywhere. Note the "failed in 0.0s" itself turned out to be a red herring on my end too — in my clean-checkout testing this exact message reproduces instantly whenever `ninja`'s executable isn't on `PATH` (e.g. invoking the venv's python directly by absolute path instead of an activated shell), regardless of concurrency. I can't confirm with certainty that's what happened in the original run's launcher, but it's the same error signature and a very plausible explanation independent of any real JIT cache race.
- **lock file**: I checked the build directory days after the hang (never touched since) and it's completely empty — no `lock`, no `build.ninja`, no `.o`/`.so`, nothing. So no lock file was left behind either at the time or since.

That doesn't rule out a real upstream race (an hour may just not be long enough, and I haven't tried to match every detail of the original setup), but I wanted to correct the record — the evidence I gave you for the shared-cache race theory was weaker than I made it sound, and likely contaminated by my own local resume patch rather than anything in GPTQModel itself. Sorry for the noise. I'm planning to re-run the clean-checkout reproduction for much longer (multiple hours, matching the original run's actual duration) to get a more conclusive answer, and will report back once that's done. Happy to keep digging on my end if useful, but wanted you to have this before committing to the flock implementation.


### Ndgandhi23 · 2026-08-19

@okdshin thanks for rechecking and running the clean test. The failed in 0.0s plus the empty build dir fits ninja never being on PATH, which would mean your processes were on the fallback path the whole time and never waiting on a lock. So I agree your hang was probably not the JIT cache.

I do believe the fix I wrote still has some validity here. Torch's build lock has no timeout and no owner check, so if a process dies mid build the lock file stays and every later load waits on it forever. I hit that on a clean checkout while testing, no custom patches involved. So the PR still fixes a failure mode, it just may not be the one you hit. I'll update the PR wording so it no longer claims to explain your incident.

@Qubitium given the above, happy to keep the PR open as hardening or close it, whichever you prefer.

### Qubitium · 2026-08-19

@okdshin The dead lock in your situation is harder to catch. I would say the best way to track it down is for you to add granular telemtry to emit event logs for all the looper/process and offload enter/exit entry points. This would help us narrow down the region for analysis. Btw, your checkpointing feature to handle resumes is nice feature to have. Please upstream it if you have the chance.



### Qubitium · 2026-08-19

@Ndgandhi23 I agree the crash is likely not directly related to the jit compile deadlock but the bug and your fix is real. Thanks and merged! 

### Qubitium · 2026-09-05

Closing this for now. @okdshin I will likely move forward with our own quant midway checkponting/resume feature soon. Do you have plans to upstream your work?

### okdshin · 2026-09-06

Opened #3057 with the resume feature, split into 3 commits (atomic offload-write prerequisite, core resume mechanism, fingerprint hardening). Sorry for the delay in answering here — appreciate the nudge.

That said, if you'd rather design and build this yourselves rather than build on an external contribution, please don't feel obligated by the PR — I'm glad to defer to whatever you think is the better path for the project, and equally happy to keep iterating on it together if you'd like to build on this instead.

