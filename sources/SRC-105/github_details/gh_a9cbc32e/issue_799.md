# [Issue #799] [Bug]: Freeze in kaleido

source: https://github.com/ROCm/rocprofiler-compute/issues/799
state: closed | updated: 2025-08-06T18:18:34Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

The profiler freeze when trying to generate the roofline using Plotly/Kaleido.

`rocprof-compute profile -n roof0 --roof-only --device 0 --kernel-names -- myprocess`

After computing the roofline, the software hangs. Cancelling it leads to the following stack trace:
```
CTraceback (most recent call last):
  File "bin/rocprof-compute", line 156, in <module>
    main()
  File "bin/rocprof-compute", line 144, in main
    rocprof_compute.run_profiler()
  File "libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "libexec/rocprofiler-compute/rocprof_compute_base.py", line 294, in run_profiler
    self.__soc[self.__mspec.gpu_arch].post_profiling()
  File "libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "libexec/rocprofiler-compute/rocprof_compute_soc/soc_gfx90a.py", line 109, in post_profiling
    self.roofline_obj.post_processing()
  File "libexec/rocprofiler-compute/roofline.py", line 445, in post_processing
    self.standalone_roofline()
  File "libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "libexec/rocprofiler-compute/roofline.py", line 382, in standalone_roofline
    self.empirical_roofline(ret_df=t_df)
  File "libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "libexec/rocprofiler-compute/roofline.py", line 158, in empirical_roofline
    ml_combo_fig_fp32_fp64.write_image(
  File "python-libs/plotly/basedatatypes.py", line 3895, in write_image
    return pio.write_image(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "python-libs/plotly/io/_kaleido.py", line 510, in write_image
    img_data = to_image(
               ^^^^^^^^^
  File "python-libs/plotly/io/_kaleido.py", line 398, in to_image
    img_bytes = scope.transform(
                ^^^^^^^^^^^^^^^^
  File "python-libs/kaleido/scopes/plotly.py", line 153, in transform
    response = self._perform_transform(
               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "python-libs/kaleido/scopes/base.py", line 293, in _perform_transform
    self._ensure_kaleido()
  File "python-libs/kaleido/scopes/base.py", line 192, in _ensure_kaleido
    startup_response_string = self._proc.stdout.readline().decode('utf-8')
```

### Linux Distribution

OS: NAME="Red Hat Enterprise Linux" VERSION="8.10 (Ootpa)"

### ROCm Compute Profiler Version

6.4.0

### GPU

MI250X

### ROCm Version

6.4.0

### Cluster name (if applicable)

Frontier

### Reproducer

-

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (12)

### etiennemlb · 2025-07-09

Kaleido process keep polling in a loop

### harkgill-amd · 2025-07-10

Hi @etiennemlb, thanks for the report. An internal ticket has been created to investigate this issue.

### benrichard-amd · 2025-07-17

Hi @etiennemlb,

Are you able to share a workload that can reproduce this?

Thanks.

### etiennemlb · 2025-07-21

Hey, turns out that we have rocprof compute asking ploty asking kaleido to produce a plot.
Somewhere in the chain, kaleido is given `--mathjax='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js'` which will not work on node without internet.  We end up having to wait for a timeout.
Clearly, the rocprof compute use case should assume nodes without internet as potential target machines.

### etiennemlb · 2025-07-21

Something must have changed in the dependencies somewhere, this workflow used to work, maybe being more stringent on the requierments.txt would help.

### benrichard-amd · 2025-07-23

Hi @etiennemlb,

I've been unable to reproduce this hang. Can you share what version of Python and Kaleido is installed on your machine?

### etiennemlb · 2025-07-24

I use kaleido 0.2.1. Are you sure your machine does not have access to internet ?

### feizheng10 · 2025-07-24

Not sure how big is your real workload? Any chance you could try a really simple single kernel to verify the env?

### etiennemlb · 2025-07-25

Its not workload specific, you just ahve to call kaleido on a machine without internet. See, it spawns a kaleido process referencing mathjax online:

```
(simplified ps aux output:)
/bin/bash .../rocprofiler-compute/python-libs/kaleido/executable/kaleido plotly --plotlyjs='.../rocprofiler-compute/python-libs/plotly/package_data/plotly.min.js' --mathjax='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js' --disable-gpu --allow-file-access-from-files --disable-breakpad --disable-dev-shm-usage --no-sandbox
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --plotlyjs='.../rocprofiler-compute/python-libs/plotly/package_data/plotly.min.js' --mathjax='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js' --disable-gpu --allow-file-access-from-files --disable-breakpad --disable-dev-shm-usage --no-sandbox plotly
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --type=zygote --no-zygote-sandbox --no-sandbox --headless --headless
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --type=zygote --no-sandbox --headless --headless
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --type=gpu-process --field-trial-handle=5308285597271888005,9133356378037671654,131072 --no-sandbox --disable-dev-shm-usage --disable-breakpad --headless --ozone-platform=headless --headless --gpu-preferences=QAAAAAAAAAAgAAAwAAAAAAAAAAAAAAAAAABgAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAA --use-gl=swiftshader-webgl --override-use-software-gl-for-tests --shared-files
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --type=utility --utility-sub-type=network.mojom.NetworkService --field-trial-handle=5308285597271888005,9133356378037671654,131072 --lang=en-US --service-sandbox-type=network --no-sandbox --disable-dev-shm-usage --use-gl=swiftshader-webgl --headless --shared-files
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --type=renderer --no-sandbox --disable-dev-shm-usage --disable-breakpad --allow-pre-commit-input --ozone-platform=headless --field-trial-handle=5308285597271888005,9133356378037671654,131072 --disable-databases --disable-gpu-compositing --lang=en-US --headless --num-raster-threads=4 --enable-main-frame-before-activation --renderer-client-id=4 --shared-files
```

and if I kill the process handling network:
```
.../rocprofiler-compute/python-libs/kaleido/executable/bin/kaleido --type=utility --utility-sub-type=network.mojom.NetworkService --field-trial-handle=5308285597271888005,9133356378037671654,131072 --lang=en-US --service-sandbox-type=network --no-sandbox --disable-dev-shm-usage --use-gl=swiftshader-webgl --headless --shared-files
```

It then continues generating the pdf without issue. This means that 1, mathjax des not seem to be needed for roofline pdfs, and 2; that internet is not required.

### benrichard-amd · 2025-07-25

> I use kaleido 0.2.1. Are you sure your machine does not have access to internet ?

Yes. I am attempting to reproduce it in a docker container with network disabled, but I am so far unable to. I wonder if there is some caching involved..

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/34

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
