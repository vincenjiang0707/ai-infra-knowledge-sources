# [Issue #695] Successfully built and installed the newest version of rccl but there is no /opt/rocm/rccl directory

source: https://github.com/ROCm/rccl/issues/695
state: closed | updated: 2023-04-05T23:12:00Z
labels: 

## 正文

Hi, I have successfully built and installed rccl on ROCm5.2 platform by following the instructions on [this page](https://github.com/ROCmSoftwarePlatform/rccl). The last of the output of this process is as the following:
```
root@XXXXX:~/rccl/build# sudo dpkg -i *.deb
(Reading database ... 78325 files and directories currently installed.)
Preparing to unpack rccl-dev_2.16.5-80ed608~dirty_amd64.deb ...
rm: cannot remove '/etc/ld.so.conf.d/rccl.conf': No such file or directory
Unpacking rccl-dev (2.16.5-80ed608~dirty) over (2.16.5-80ed608~dirty) ...
Preparing to unpack rccl_2.16.5-80ed608~dirty_amd64.deb ...
rm: cannot remove '/etc/ld.so.conf.d/rccl.conf': No such file or directory
Unpacking rccl (2.16.5-80ed608~dirty) over (2.16.5-80ed608~dirty) ...
Setting up rccl (2.16.5-80ed608~dirty) ...
Setting up rccl-dev (2.16.5-80ed608~dirty) ...
Processing triggers for libc-bin (2.31-0ubuntu9.9) ...
```
But there should be a directory "/opt/rocm/rccl", but there is not!
What could be the cause? Thanks in advance.

## 评论 (1)

### gilbertlee-amd · 2023-04-05

Sorry for the delayed response.
Could you try this with a newer version of ROCm and re-open ticket if you still have this issue?
