# [Issue #640] [Bug]: `rocprof-compute analyze --gui` fails with `ObsoleteAttributeException`

source: https://github.com/ROCm/rocprofiler-compute/issues/640
state: closed | updated: 2025-07-04T22:58:34Z
labels: bug, Standalone GUI, packaging, analysis, triage, Under Investigation

## 正文

### Describe the bug

Following the official install instructions here: https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/install/core-install.html#install-via-package-manager

And launching the gui on a recently captured trace
```
rocprof-compute analyze -q -p <trace_directory> --gui
```

Fails with the following message
```
Traceback (most recent call last):
  File "/usr/bin/rocprof-compute", line 153, in <module>
    main()
  File "/usr/bin/rocprof-compute", line 145, in main
    rocprof_compute.run_analysis()
  File "/opt/rocm-6.4.0/libexec/rocprofiler-compute/utils/utils.py", line 45, in wrap_function
    result = function(*args, **kwargs)
  File "/opt/rocm-6.4.0/libexec/rocprofiler-compute/rocprof_compute_base.py", line 295, in run_analysis
    analyzer.run_analysis()
  File "/opt/rocm-6.4.0/libexec/rocprofiler-compute/utils/utils.py", line 45, in wrap_function
    result = function(*args, **kwargs)
  File "/opt/rocm-6.4.0/libexec/rocprofiler-compute/rocprof_compute_analyze/analysis_webui.py", line 319, in run_analysis
    self.app.run_server(debug=False, host="0.0.0.0", port=args.gui)
  File "/home/qdawkins/threadtrace/trace_venv/lib/python3.10/site-packages/dash/_obsolete.py", line 22, in __getattr__
    raise err.exc(err.message)
dash.exceptions.ObsoleteAttributeException: app.run_server has been replaced by app.run
```

Manually replacing `run_server` with `run` in `rocprofiler-compute/rocprof_compute_analyze/analysis_webui.py:319` fixes the issue.

### Linux Distribution

Ubuntu 22.04.2 LTS

### ROCm Compute Profiler Version

rocprofiler-compute version: 3.0.0 (release)

### GPU

MI300X

### ROCm Version

rocm-6.4.0

### Cluster name (if applicable)

_No response_

### Reproducer

1.
```
$ sudo apt install rocprofiler-compute
# Include rocprofiler-compute in your system PATH
$ sudo update-alternatives --install /usr/bin/rocprofiler-compute rocprof-compute /opt/rocm/bin/rocprofiler-compute 0
# Install Python dependencies
$ python3 -m pip install -r /opt/rocm/libexec/rocprofiler-compute/requirements.txt
```

2. Capture a trace

3. Run `rocprof-compute analyze -q -p <trace_directory> --gui`

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (5)

### Hamerlate · 2025-05-18

Suggestion: change line 346 in `src/rocprof_compute_analyze/analysis_webui.py` from  
    `self.app.run_server(...)`  
to  
    `self.app.run(...)`  
as `run_server` is deprecated in newer versions of Dash and raises `ObsoleteAttributeException`.


### ppanchad-amd · 2025-06-06

Hi @qedawkins. Has the suggestion above resolved your issue? Thanks!

### kuhar · 2025-06-16

I hit the same issue on rocm 6.4.1. The suggestion fixes the hard error but the GUI remains broken (the selection on the top-left) doesn't do anything. CLI analysis works OK though.

The underlying issue seems to be that the requirements file does not pin all the dependencies:
```
➜  padding cat /opt/rocm/libexec/rocprofiler-compute/requirements.txt
astunparse==1.6.2
colorlover
dash>=1.12.0
matplotlib
numpy>=1.17.5
pandas>=1.4.3
pymongo
pyyaml
tabulate
tqdm
dash-svg
dash-bootstrap-components
kaleido==0.2.1
setuptools
plotille
```

For example, newer versions of `dash` and related packages introduce breaking API changes that the requirements file doesn't account for.

### ppanchad-amd · 2025-06-18

@qedawkins This was fixed by https://github.com/ROCm/rocprofiler-compute/pull/719. Thanks!

### fxmarty-amd · 2025-07-04

+1, running `rocprofiler-compute analyze --gui` is broken with the above error on the latest available package on Ubuntu repos:

```
root@rocm-jupyter-gpu-mi300x1-192gb-devcloud-atl1:/repos# apt show rocprofiler-compute
Package: rocprofiler-compute
Version: 3.1.0.60401-83~22.04
Priority: optional
Section: devel
Maintainer: https://github.com/ROCm/rocprofiler-compute
Installed-Size: 14.7 MB
Provides: omniperf
Depends: rocprofiler
Breaks: omniperf
Replaces: omniperf
Homepage: https://github.com/ROCm/rocprofiler-compute
Download-Size: 2902 kB
APT-Manual-Installed: yes
APT-Sources: https://repo.radeon.com/rocm/apt/6.4.1 jammy/main amd64 Packages
Description: ROCm Compute Profiler: tool for GPU performance profiling
```

Will a new release be published?

For users new to MI300 & Instinct, they may expect the released version through the package manager to be stable and working, and it may not be feasible for them to install from source. I think this is critical.

For now I am suggesting this to users:
```
find /opt/rocm/libexec/rocprofiler-compute -type f -name '*.py' -exec sed -i 's/self.app.run_server/self.app.run/g' {} \;
find /opt/rocm/libexec/rocprofiler-compute -type f -name 'gui.py' -exec sed -i 's/\]\[0\]/\].iloc\[0\]/g' {} \;
```
