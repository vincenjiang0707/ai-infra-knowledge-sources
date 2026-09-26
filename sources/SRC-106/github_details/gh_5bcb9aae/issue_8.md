# [Issue #8] PyPI wheel

source: https://github.com/ROCm/amdsmi/issues/8
state: open | updated: 2026-02-19T02:09:11Z
labels: Under Investigation, Feature Request

## 正文

Hi,

Having a PyPI wheels for this package would be very useful.

Thank you!

## 评论 (12)

### dmitrii-galantsev · 2023-12-11

Hm i think we do something with wheels already. I’ll investigate!
Do you want this tool available in pip? As in `pip install amdsmi`?

### fxmarty · 2023-12-12

Yes - not very important but it can be useful to host wheels on PyPI index.

### dmitrii-galantsev · 2023-12-12

I think right now we will run into an issue of libamd_smi.so being x86 specific.
We don't build a noarch version. And to be honest - I've never done that.
Any pointers? :)

### hliuca · 2024-03-08

Let us assume user has a ROCM installed already. the PyPI version can detect ROCm using ROCM_PATH and find the libraries it needs. So amdsmi or pyamdsmi can be independent of any ROCm.... This way, even multiple ROCm coexist on the system, it still works very well.

### jaywonchung · 2024-04-30

(Updated Oct. 17th, 2024)
We're distributing unofficial Python bindings for amdsmi: [Repo](https://github.com/ml-energy/amdsmi), [PyPI](https://pypi.org/project/amdsmi).
It's pretty much taking the `py-interface` directory for each `rocm-x.x.x` release and publishing it as a Python package so that `pip install amdsmi` works.

---

It'll be very nice to be able to do `pip install amdsmi` since my project [Zeus](https://github.com/ml-energy/zeus) is trying to support AMD GPUs as well.

NVML also assumes that the user has `libnvidia-ml.so` on the system. If not, it'll still import fine, but `pynvml.nvmlInit()` will fail.
NVML python bindings on PyPI: https://pypi.org/project/nvidia-ml-py/

### dmitrii-galantsev · 2024-10-29

@jaywonchung Thanks for doing that!

Some observations:

> AMDSMI package releases, based on year, month, and revision (e.g., 24.5.0).
ROCm-based releases, which is released whenever a new ROCm version is released (e.g., 6.2.2).

Correct, and picking ROCm-based releases also makes the most sense. That's part of the confusion with PyPI packaging here too. Do we make dev releases available?

> When AMD intends to officially maintain the amdsmi package on PyPI, we are happy to transfer ownership.

We're not quite ready to take ownership, sorry! We're awaiting migration to github after 6.3 release. We will have more control over our CI tests and packaging. _fyi: amdsmi dev happens on internal gerrit and gets mirrored to github overnight_

Part of the issue - I've never done manylinux compilation :disappointed: . And we want amdsmi in pypi to run on as many distributions as possible.

Also we really don't want it to interfere with a system-wide rocm-based amdsmi install. That would be very confusing..

### jaywonchung · 2024-10-29

> Correct, and picking ROCm-based releases also makes the most sense. That's part of the confusion with PyPI packaging here too. Do we make dev releases available?

For our particular use case, we're really just aiming to use stable releases of AMDSMI instead of getting nightly. If AMDSMI is planning to release nightly versions per commit or everyday, I think it's better to set up another PyPI project (e.g., `amdsmi-nightly`) that is only for nightly releases in order not to overflow the release history of the main project (e.g., [streamlit-nightly](https://pypi.org/project/streamlit-nightly/)). Another way is to set up AMDSMI's own index server (e.g., [PyTorch Nightly](https://download.pytorch.org/whl/nightly)), but this is probably too much.

> Part of the issue - I've never done manylinux compilation 😞 . And we want amdsmi in pypi to run on as many distributions as possible.

Right now, the bindings we unofficially distribute is just pure Python, so it's universal. It requires an installation of ROCm under the path designated by `ROCM_PATH` so that it can find `libamd_smi.so` inside it on import. This is following how Python bindings for NVML (`nvidia-ml-py`) is distributed -- they just ship Python bindings and will error out if it fails to find `libnvidia-ml.so` on the system. I thought this was reasonable, as it's likely that whoever hopes to use AMDSMI has an AMD device and ROCm installed, and a stable release of `libamd_smi.so` will come with that.

Regarding manylinux Python wheel builds, I've never done it myself either but I heard it's more or less just building the wheel inside the [manylinux Docker container](https://github.com/pypa/manylinux). It also comes with pre-built images for x64, aarch64, and a few more architectures.

PS. Copying @parthraut who did all the actual work.

### dmitrii-galantsev · 2024-10-30

ahh I see thanks for the explanation @jaywonchung .
in our "normal" install we actually copy libamd_smi.so _into_ the python install directory as well. So it doesn't try to find it.

Do you think it's better to try and find it in "$ROCM_PATH:-/opt/rocm"?
Think this can create issues where .so and python tools are not matching versions.

### jaywonchung · 2024-10-30

> Do you think it's better to try and find it in "$ROCM_PATH:-/opt/rocm"?

Aha, so currently in our bindings, `import amdsmi` will error if the environment variable `ROCM_PATH` is not set. We don't have a default for it when it's not set. If you say `/opt/rocm` is a good default, we can certainly do that!

Ref: https://github.com/ml-energy/amdsmi/blob/f5a9a6f68e7db32d6de507fc41ec08933e1ae1ba/py-interface/amdsmi/amdsmi_wrapper.py#L172

> Think this can create issues where .so and python tools are not matching versions.

Yeah, if the user's `amdsmi` Python binding version does not match with `libamd_smi.so` bundled with the current installation of ROCm, incompatibility issues will arise. But users can still set the `ROCM_PATH` environment variable to a directory that contains the right version of `libamd_smi.so`, things would work. 

### jaywonchung · 2025-09-24

For the record: Ownership of the PyPI proejct `amdsmi` was transferred to AMD today.

### jaywonchung · 2026-02-19

Nothing is being released, which is disappointing. My project also depends on the amdsmi Python package, and eventually it'll be a problem.

But please at least take down the past maintainers' names from https://pypi.org/project/amdsmi/ README as soon as possible, because we no longer have any control over the PyPI project and don't want to be portrayed as abandoning maintenance.

@dmitrii-galantsev 

### jaywonchung · 2026-02-19

Copying other potential maintainers regarding the above. @marifamd @marbre 
