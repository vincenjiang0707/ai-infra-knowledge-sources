# [Issue #1] Use perf_analyzer without GPU/CUDA

source: https://github.com/triton-inference-server/perf_analyzer/issues/1
state: closed | updated: 2025-02-06T04:32:46Z
labels: 

## 正文

**Is your feature request related to a problem? Please describe.**
We are building a perf analyzer workflow on CI, and we plan to use perf_analyzer as client. The client worker won't have GPU/CUDA. But I tried both `pip install tritonclient` and the NGC image, both failed by complaining there is no cuda/gpu.

**Describe the solution you'd like**
I don't get why perf_analyzer requires GPU. It should be able to run perfectly on machines that has no GPU.


## 评论 (6)

### lkomali · 2024-03-13

Hi, can you clarify your setup? 
What version of Triton are you using?
Are you running Triton from NGC container?
Can you clarify if the machine you are using do not have any GPU/CUDA installed and running models only on CPU?

### ShuaiShao93 · 2024-03-13

> What version of Triton are you using? Are you running Triton from NGC container?

I tried perf_analyzer in both `nvcr.io/nvidia/tritonserver:24.02-py3-sdk` and pip3 `tritonclient 2.43.0`. Both need GPU/CUDA.

> Can you clarify if the machine you are using do not have any GPU/CUDA installed and running models only on CPU?

The triton server and perf_analyzer are run on separate machines. The perf_analyzer one doesn't have GPU/CUDA installed.

### debermudez · 2024-03-13

@matthewkotila i thought we removed this requirement?

### nv-hwoo · 2025-02-03

@ShuaiShao93 Are you still encountering the issue? Also, you could try more recent version of PA. I believe we recently made some updates around removing some GPU/CUDA related dependencies in perf analyzer (@matthewkotila correct me if I'm wrong).

### matthewkotila · 2025-02-03

> @nv-hwoo: [@ShuaiShao93](https://github.com/ShuaiShao93) Are you still encountering the issue? Also, you could try more recent version of PA. I believe we recently made some updates around removing some GPU/CUDA related dependencies in perf analyzer ([@matthewkotila](https://github.com/matthewkotila) correct me if I'm wrong).

To clarify, Perf Analyzer has never needed an actual _GPU_ on the device in order to run regularly without `--shared-memory=cuda`. What it had historically needed was the CUDA Runtime library installed (libcudart.so), regardless of whether `--shared-memory=cuda` was used, which was the valid UX frustration being mentioned here.

This changed as of [tritonclient 2.52.0](https://pypi.org/project/tritonclient/2.52.0/) (released Nov 25, 2024), where Perf Analyzer since then can run in an environment without the CUDA Runtime library (libcudart.so) installed:

```bash
docker run --pull=always --rm -it ubuntu:24.04

nvidia-smi

# bash: nvidia-smi: command not found

find / -name libcudart.so

# <nothing>

apt update && DEBIAN_FRONTEND=noninteractive apt install -y python3 python3-pip python3-venv

python3 -m venv /opt/venv && export PATH=/opt/venv/bin:$PATH

pip install tritonclient==2.52.0

perf_analyzer --help

# binary works
```

Edit: @nv-hwoo what you might have been thinking of that happened more recently than November 2024 is issue https://github.com/triton-inference-server/perf_analyzer/issues/248.

But that was related to someone struggling to _build_ Perf Analyzer without having CUDA installed on the system.

That issue was also fixed.

### the-david-oy · 2025-02-06

Thank you Hyunjae and Matt for providing an explanation. Closing this issue unless there are further questions/comments.
