# [Issue #47] Counter values (potentially only those dependent on DIMENSION_INSTANCE[1:31]?) are consistently zero in rocprofv3 runs.

source: https://github.com/ROCm/rocprofiler-sdk/issues/47
state: closed | updated: 2025-07-10T20:09:04Z
labels: Under Investigation

## 正文

Hi-- I've been attempting to use `rocprofv3` for counter collection for a basic PyTorch workload, but I'm running into odd issues where various counters (both basic and derived) always output zero (so far I've tried `GPU_UTIL`, `FETCH_SIZE`, and `OccupancyPercent`.) Some counters still work though, like `SQ_WAVES`. I tried running my test programs both in the native Ubuntu 24.10 OS and the [provided](https://hub.docker.com/r/rocm/pytorch) Ubuntu 24.04.1 Docker container for PyTorch development (`rocm/pytorch:rocm6.3.2_ubuntu24.04_py3.12_pytorch_release_2.4.0`, image ID: `c99bb965c26e`) and the counter values were consistently zero in both environments. I've run `amd-smi process` while my Python scripts are running and can see that my script is running on the GPU-- so at the very least `GPU_UTIL` should be non-zero at some point in the output?

To start diagnosing the problem, I ran the set of sample programs in `samples/` and they all passed, but the verbose output for test 7 (`counter-collection-print-functional-counters`) showed a number of errors regarding missing values for any counter that reads from `DIMENSION_INSTANCE[1:31]`. Counters that read exclusively from `DIMENSION_INSTANCE[0]` like `GRBM_COUNT` show no missing values. Here's the [full output](https://pastebin.com/dFjk5Gw2) from my latest run of the test suite in the provided Docker container. Test 7 begins on line 149. The first error due to a "missing" value is on line 417.

This leads me to my primary questions: 
- What can I do to fix the zero counter values in my `rocprofv3` profiler runs?
- Are the errors regarding missing values for any counter reading from `DIMENSION_INSTANCE[1:31]` in test 7 intended behavior, or is this potentially why the zero counter values are occurring?

---

Additional things I've tried, including various recommended setup steps:

- Double-checking that I am sending all tensors to the device, etc. in my basic PyTorch scripts.
- Installing `libdw-dev` in the Docker container via `apt install` to be able to build and run the `samples/` program suite.
- Adding my user account to the `video` and `render` groups.
    - Notably the Docker container does not recognize the `render` group, so I have not been able to add it to that. I'm not sure if this matters, since my base user account is in both groups and is experiencing the same issue with counter values anyways. Regardless, this is only relevant on Ubuntu 20.04 (as stated [here](https://github.com/ROCm/ROCm-docker/blob/master/quick-start.md) in step 1), right?
- Configuring a stable power state for the GPU I am running the workload on via `sudo amd-smi set -g <N> -l stable_std` as suggested in this repo's README.md.
- Giving the Docker container `PERFMON` capabilities via an additional `--cap-add=PERFMON` flag in the Docker container's startup command.
    - One of the `sample/` tests (I believe 8 or 9?) flagged that the Docker container didn't have this capability, so I added it in the hopes that it would fix this issue. The only noticeable outcome is that the test no longer flags the missing capability.
- Restricting the Docker container's GPU access to only one of the two GPUs in the machine via `--device=/dev/dri/renderD128` *or* `--device=/dev/dri/renderD129`.
    - I have tried both GPUs and neither worked, which makes me think that this is not an odd hardware fault on just one card?
- Exporting variables: 
    - `LD_LIBRARY_PATH` = `/opt/rocm-6.3.2/lib`
    - `ROCM_PATH` = `/opt/rocm`
- Configuring the system linker as specified in the post-installation instructions [here](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/post-install.html) by creating file `/etc/ld.so.conf.d/rocm.conf` with the contents `/opt/rocm/lib` and `/opt/rocm/lib64` and running `sudo ldconfig`.

---

Machine specs:

- Bare metal OS:
  - NAME="Ubuntu"
  - VERSION="24.10 (Oracular Oriole)"
  - Kernel version via `uname -srmv`: `Linux 6.11.0-14-generic #15-Ubuntu SMP PREEMPT_DYNAMIC Fri Jan 10 23:48:25 UTC 2025 x86_64`
- Docker OS (provided by AMD):
  - NAME="Ubuntu"
  - VERSION="24.04.1 LTS (Noble Numbat)"
- CPU:
  - model name      : AMD Ryzen Threadripper 2990WX 32-Core Processor
- GPU:
  - Name:                    AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Marketing Name:          AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Name:                    AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Marketing Name:          AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Name:                    AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Marketing Name:          AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Name:                    AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Marketing Name:          AMD Ryzen Threadripper 2990WX 32-Core Processor
  - Name:                    gfx1100
  - Marketing Name:          Radeon RX 7900 XTX
      - Name:                    amdgcn-amd-amdhsa--gfx1100
  - Name:                    gfx1100
  - Marketing Name:          Radeon RX 7900 XTX
      - Name:                    amdgcn-amd-amdhsa--gfx1100
- `rocminfo --support` output run on bare metal [here](https://pastebin.com/Z5iYsqnb).




## 评论 (7)

### ppanchad-amd · 2025-02-18

Hi @Sunlost. Internal ticket has been created to assist with your issue. Thanks!

### ApoKalipse-V · 2025-02-20

Hi @Sunlost 
Have you used the stable pstate as described in the readme? Most counters require it for Radeon 7000 GPUs, with a few exceptions such as SQ_WAVES

### schung-amd · 2025-02-26

@Sunlost I can see you state you've tried this:

> Configuring a stable power state for the GPU I am running the workload on via sudo amd-smi set -g <N> -l stable_std as suggested in this repo's README.md.

but I suggest double-checking that you've set this for the correct device N (as shown by `rocm-smi` or `amd-smi monitor`). I can reproduce the zero values you're seeing on Ubuntu 24.04 + ROCm 6.3.3 + a single 7900XTX without setting the power state, and after `sudo amd-smi set -g 0 -l stable_std` the counters are populated correctly.

### Sunlost · 2025-02-27

Hi @schung-amd -- thanks for working on reproducing the issue. I appreciate it.

I've been setting the power state to `stable_std` for both devices since I wasn't sure which of the two 7900 XTX cards the provided sample programs would use when run outside of the Docker container. I have verified this by running `rocm-smi` and checking that the `Perf` column lists `stable_std` for both cards. I've tried running my experiment again just now to see if I had somehow missed this step when running my experiment and found no change in the result. 

For reference, the experimental workload I'm running is launching an instance of GPT2 on the device and running some basic inference. I'm running `rocprofv3` via the following command: `rocprofv3 -i rocprof-counters.txt --hip-trace --stats --output-format csv pftrace -- python experiment.py`. The input counter file contains the single line `pmc: GPU_UTIL FETCH_SIZE OccupancyPercent`. I'd expect at least `GPU_UTIL` to be non-zero at any point in the profiler run, but I get zero matches when I `grep` through `counter_collection.csv` for any non-zero `GPU_UTIL` counters (and the same for the other two tracked counters.)

I've also tried running the same experiment as root with no change in results. The output from the sample program counter collection test still shows the same weird errors regarding `DIMENSION_INSTANCE[1:31]` as was the case in my original post. `rocm-smi` still shows `stable_std` after concluding all of these tests, so I'm reluctant to think that it's a power state issue.

Let me know if I can provide any additional information. Thanks!

### schung-amd · 2025-02-27

Thanks for double-checking! I'll see if I can repro with two GPUs. Regarding the `DIMENSION_INSTANCE` errors in the tests, I can see those regardless of whether I've set the power state or not (i.e. whether I'm seeing zero values or not), so I don't think they're related to this issue. I also see these errors on MI systems, and given that the test reports as passing, I wouldn't be too worried about them.

### schung-amd · 2025-04-23

Hi @Sunlost, sorry for the delay on this, are you still experiencing this issue? Unfortunately, I haven't been able to repro this so far with dual GPU setups.

### schung-amd · 2025-07-10

Closing for now as I haven't been able to reproduce this. If you're still experiencing this issue on current ROCm and rocprof versions feel free to comment and we can reopen if necessary.
