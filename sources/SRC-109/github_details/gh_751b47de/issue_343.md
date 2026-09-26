# [Issue #343] Lower GLIBC Requirement?

source: https://github.com/triton-inference-server/perf_analyzer/issues/343
state: open | updated: 2026-03-09T17:28:02Z
labels: 

## 正文

Currently when using the latest Amazon Ubuntu DLAMI (`Deep Learning OSS Nvidia Driver AMI GPU PyTorch 2.6.0 (Ubuntu 22.04) 20250309`), I run into this error when I `pip install tritonclient` and try to use `perf_analyzer`:

```
$ .venv/bin/perf_analyzer --help
.venv/bin/perf_analyzer: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by .venv/bin/perf_analyzer)
.venv/bin/perf_analyzer: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.31' not found (required by .venv/bin/perf_analyzer)
.venv/bin/perf_analyzer: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by .venv/bin/perf_analyzer)
```

Full output of `ldd`:

```
$ ldd .venv/bin/perf_analyzer
.venv/bin/perf_analyzer: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by .venv/bin/perf_analyzer)
.venv/bin/perf_analyzer: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.31' not found (required by .venv/bin/perf_analyzer)
.venv/bin/perf_analyzer: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by .venv/bin/perf_analyzer)
        linux-vdso.so.1 (0x00007ffd949e9000)
        libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x000073577ae84000)
        libssl.so.3 => /lib/x86_64-linux-gnu/libssl.so.3 (0x0000735779f5c000)
        libcrypto.so.3 => /lib/x86_64-linux-gnu/libcrypto.so.3 (0x0000735779a00000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x0000735779600000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x0000735779e75000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x0000735779e55000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x0000735779200000)
        /lib64/ld-linux-x86-64.so.2 (0x000073577aeb8000)
```

It would be great to lower the GLIBC requirement to enable perf_analyzer to work out of the box on the latest Amazon Ubuntu DLAMI without re-compiling `perf_analyzer` from source (which takes quite a while).

## 评论 (2)

### the-david-oy · 2025-04-07

CC: @nicolasnoble @matthewkotila 

### beni-thiago · 2026-03-09

Any updates?
