# [Issue #485] ERROR Please ensure that the 'en_US.UTF-8' locale is available on your system.

source: https://github.com/ROCm/rocprofiler-compute/issues/485
state: closed | updated: 2024-12-19T13:34:22Z
labels: question, Under Investigation

## 正文

### Describe your question

Hit this error when using omniperf on official [rocm/vllm](https://hub.docker.com/r/rocm/vllm) docker.
```
  ERROR Please ensure that the 'en_US.UTF-8' locale is available on your system.
  ERROR unsupported locale setting
```

Not sure how to resolve this issue properly. But was able to hack around it by modifying `/opt/rocm/libexec/omniperf/utils/utils.py` to skip the setlocale call entirely. Everything works afterwards.

```
--- utils.py
+++ utils.py
@@ -647,6 +647,7 @@


 def set_locale_encoding():
+    return
     try:
         locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
     except locale.Error as error:
```
I'm not sure if this function call should be strictly required for using omniperf..

### Additional context

_No response_

## 评论 (4)

### tcgu-amd · 2024-11-26

Hi @BowenBao, thanks for reaching out! I think you might be missing the locale in your docker. Can you run the following command insider your rocm/vllm docker container

```
sudo apt update && sudo install locales && sudo locale-gen en_US.UTF-8
```

then try the problematic python script again?

Please let me know if this works. Thanks!

### BowenBao · 2024-11-27

Hi @tcgu-amd thanks for advice. Yes running `sudo apt update && sudo apt install locales && sudo locale-gen en_US.UTF-8` resolves the issue. Is it possible to relax this constraint though? It would be better UX imo if omniperf just works out of the box.

### tcgu-amd · 2024-11-27

Hey @BowenBao, I think this is a rather an unusual case, since the locale would usually be available on the system (it is commonly a part of the system installation process). Relying on a specific `locale` is pretty common to allow applications to determine the date, time, display, and keyboard to use. Given that configuring the locales is a fairly common practice and most systems should have it configured, I think it is fair the way Omniperf currently works. If the locale happens to not be available, it is probably a good idea to install the correct one anyways :)

### fxmarty-amd · 2024-12-19

I had the same issue on `rocm/dev-ubuntu-22.04:6.3` docker image.
