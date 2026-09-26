# [Issue #453] Error: Invalid long option '--help'

source: https://github.com/triton-inference-server/perf_analyzer/issues/453
state: open | updated: 2025-11-28T14:26:45Z
labels: 

## 正文

This is a really stupid question, but how do I get documentation for `perf_analyzer` using the CLI? The [docs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/cli.html#help) clearly state that there is such an option, but I'm unable to use it:
```bash
root@[my_server]:/workspace# perf_analyzer --help
Error: Invalid long option '--help'
```
I'm running the analyzer inside the official docker-container:
```bash
docker run --gpus all --rm -it --net=host nvcr.io/nvidia/tritonserver:25.10-py3-sdk bash
```
and I haven't changed anything in it. Check:
```bash
root@[my_server]:/workspace# ls -l $(which perf_analyzer)
-rwxr-xr-x 1 root root 216 Oct 29 18:28 /usr/local/bin/perf_analyzer
```

## 评论 (2)

### TopCoder2K · 2025-11-26

The problem is also valid for some other options. For example, `--input_data` is stated in the [docs](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/perf_analyzer/docs/cli.html#input-data-zero-random-path) but I get
```bash
Error: Invalid long option '--input_data'
```

### TopCoder2K · 2025-11-28

The same is true for the recently released `25.11` version.
