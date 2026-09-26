# [Issue #1926] pip install flash-attn hangs on Google Colab A100 with latest environment

source: https://github.com/Dao-AILab/flash-attention/issues/1926
state: open | updated: 2026-08-28T11:03:08Z
labels: 

## 正文

Hello,

The command pip install flash-attn --no-build-isolation is currently hanging indefinitely on a standard Google Colab A100 instance. It seems a pre-compiled wheel is not available for the current Colab environment, and building from source fails.

This blocks the use of attn_implementation="flash_attention_2" in libraries like Hugging Face transformers.

Environment Details:

    GPU: NVIDIA A100 | NVIDIA-SMI 550.54.15   Driver Version: 550.54.15 

    Python Version: Python 3.12.11

    CUDA Version: 12.4

    PyTorch Version: 2.3.1+cu121

    PyTorch CUDA Version: 12.1

Steps to Reproduce:

    Start a new Google Colab notebook and select an A100 GPU runtime.

    Run the following cell to install PyTorch:
      !pip install torch==2.3.1 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

Run the installation for FlashAttention:
   !pip install flash-attn --no-build-isolation

Observed Behavior:
The pip install flash-attn command hangs and never completes.

Expected Behavior:
The command should quickly install a pre-compiled wheel compatible with the environment.

Thank you!

## 评论 (6)

### nataliameira · 2025-12-02

@vc77 , I encountered the same issue. Were you able to solve it?

### osinkolu · 2025-12-15

For your peace of mind, you can switch to the October 2025 pinned environment. 

<img width="623" height="537" alt="Image" src="https://github.com/user-attachments/assets/ec2277de-da35-4401-bcb2-7ac9551d58cd" />

then use` !pip install flash-attn --no-build-isolation`

Takes around 2 minutes or less.

> [@vc77](https://github.com/vc77) , I encountered the same issue. Were you able to solve it?



### Postlytllp · 2026-01-29

> For your peace of mind, you can switch to the October 2025 pinned environment.
> 
> <img alt="Image" width="623" height="537" src="https://private-user-images.githubusercontent.com/60588823/526759765-ec2277de-da35-4401-bcb2-7ac9551d58cd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njk2OTYwMzMsIm5iZiI6MTc2OTY5NTczMywicGF0aCI6Ii82MDU4ODgyMy81MjY3NTk3NjUtZWMyMjc3ZGUtZGEzNS00NDAxLWJjYjItN2FjOTU1MWQ1OGNkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTI5VDE0MDg1M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTdkNjdhNTNkOWQyZTRlZjRiMGU4NTJmN2FiMWZiM2U2Y2UyYmRjNTA3ZGYzMzEwN2ExM2FjOGNkOGYzMDE0OWYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.QfQbAAHNCl3tFYcbEAowI4JUDPerbpnhSQoUgQDL_iA">
> then use` !pip install flash-attn --no-build-isolation`
> 
> Takes around 2 minutes or less.
> 
> > [@vc77](https://github.com/vc77) , I encountered the same issue. Were you able to solve it?

it worked ofr me also


### rudro12356 · 2026-04-24

Changing runtime version to 2025.10 solved the problem. 

### hietzsche · 2026-06-28

thanks for github, maybe i argue with ai like 20 min

### isaacOluwafemiOg · 2026-08-28

> For your peace of mind, you can switch to the October 2025 pinned environment.
> 
> <img alt="Image" width="623" height="537" src="https://private-user-images.githubusercontent.com/60588823/526759765-ec2277de-da35-4401-bcb2-7ac9551d58cd.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODc5MTQ5NDMsIm5iZiI6MTc4NzkxNDY0MywicGF0aCI6Ii82MDU4ODgyMy81MjY3NTk3NjUtZWMyMjc3ZGUtZGEzNS00NDAxLWJjYjItN2FjOTU1MWQ1OGNkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA4MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwODI4VDEwNTcyM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRlMmJjNzgzODU1OGE1MWJlMGRmNTMyM2IwMjYwNTVkMWFlOGMyMWRhYmM0MDhlNWQzMGMyOGYyZTQwNDIxNTEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.mMNNKVfPyMIf_Lt8VLjlBz_joy0sQ7NT_4WdszSMEFM">
> then use` !pip install flash-attn --no-build-isolation`
> 
> Takes around 2 minutes or less.
> 
> > [@vc77](https://github.com/vc77) , I encountered the same issue. Were you able to solve it?

The professor comes in with a great save.
