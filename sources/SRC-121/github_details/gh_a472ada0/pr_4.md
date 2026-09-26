# [PR #4] fix: update environment setup for session 4

source: https://github.com/gpu-mode/lectures/pull/4
state: closed | updated: 2024-02-03T21:54:59Z
labels: 

## 正文

Added a new cell for the environment setup as part of running this in google colab:
- `ninja`: Required for PyTorch's extension loader.
- `g++-11`: Set as the C++ compiler in environment variables for CUDA extension compilation.
- `ccache`: Configured for `g++` and `gcc` to improve compile times in interactive development environments like Colab.


## 评论 (0)

## Review (1)

### msaroufim · 2024-02-03 · APPROVED

(no text)
