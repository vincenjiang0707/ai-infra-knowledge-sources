# [Issue #3376] [Bug] Broken pip installation for mlc-llm-nightly-cpu, mlc-ai-nightly-cpu. 404s on wheel links

source: https://github.com/mlc-ai/mlc-llm/issues/3376
state: closed | updated: 2025-12-18T03:47:06Z
labels: bug

## 正文

## 🐛 Bug

The `mlc-ai-nightly-cpu` and `mlc-llm-nightly-cpu` wheel links provided by the official nightly index (`https://mlc.ai/wheels`) are returning 404 errors, making the package unusable on macOS ARM64.

When trying to install via `pip`, the wheel cannot be downloaded from GitHub:

ERROR: HTTP error 404 while getting https://github.com/mlc-ai/package/releases/download/v0.9.dev0/mlc_ai_nightly_cpu-0.20.dev537-py3-none-macosx_13_0_arm64.whl

---

## To Reproduce

Steps to reproduce the behavior:

1. Create a new virtual environment (Python 3.13, macOS ARM64).
2. Run the following command:

```bash
python -m pip install --pre -U -f https://mlc.ai/wheels mlc-ai-nightly-cpu
```
Observe the HTTP 404 error from GitHub and the failed installation.

Expected behavior
The nightly wheels should be available for download and installable via pip, so that mlc-llm can be used immediately on macOS ARM64.

Environment
Platform: CPU (macOS ARM64)

Operating system: macOS 13.x / Apple M1/M2

How you installed MLC-LLM: pip from https://mlc.ai/wheels

How you installed TVM: N/A (using prebuilt wheels)

Python version: 3.13.9

pip version: 25.2

Any other relevant information: Installation fails even in a clean virtual environment; the wheel URL points to a non-existent release on GitHub.

Additional context
This issue blocks all macOS ARM64 users from using mlc-llm via pip nightlies. Without the prebuilt wheel, users must build everything from source, which is error-prone and difficult, especially for TVM and ML C-extensions.

## 评论 (4)

### MasterJH5574 · 2025-11-10

@Guzzler Hey thanks for reporting this. The previous wheels were accidentally removed by some scripts and sorry for the inconvenience. Now the latest nightly build is back, and you can use the same command to try again.

### taytwkim · 2025-12-17

@MasterJH5574
Hello. Sorry to comment on a closed issue, but I am experiencing the same problem where https://mlc.ai/wheels returns a 404. I am also on ARM/macOS. Could you take a look? Thanks.

### qoli · 2025-12-18

pls reopen issue.


install via system python3
```
ronnie@Mac eisonAI % python3 -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu   
Looking in links: https://mlc.ai/wheels
Requirement already satisfied: mlc-llm-nightly-cpu in /Users/ronnie/.pyenv/versions/3.10.4/lib/python3.10/site-packages (0.1)
Requirement already satisfied: mlc-ai-nightly-cpu in /Users/ronnie/.pyenv/versions/3.10.4/lib/python3.10/site-packages (0.1)
```

install via uv python is not working 
```
(.venv) ronnie@Mac eisonAI % uv pip install --pre -U \
  -f https://mlc.ai/wheels \
  mlc-llm-nightly-cpu \
  mlc-ai-nightly-cpu
error: Failed to read `--find-links` URL: https://mlc.ai/wheels
  Caused by: Failed to fetch: `https://mlc.ai/wheels`
  Caused by: HTTP status client error (404 Not Found) for url (https://mlc.ai/wheels)
(.venv) ronnie@Mac eisonAI % uv pip install --pre -U \
  -f https://mlc.ai/wheels/ \
  mlc-llm-nightly-cpu \
  mlc-ai-nightly-cpu
error: Failed to read `--find-links` URL: https://mlc.ai/wheels/
  Caused by: Failed to fetch: `https://mlc.ai/wheels/`
  Caused by: HTTP status client error (404 Not Found) for url (https://mlc.ai/wheels/)
```

<img width="1243" height="919" alt="Image" src="https://github.com/user-attachments/assets/30366f36-e4b6-4f53-8982-7db43b6e9c85" />

### taytwkim · 2025-12-18

@qoli If you need to install it right now, I think you can manually download the packages from here:
https://github.com/mlc-ai/package/releases
