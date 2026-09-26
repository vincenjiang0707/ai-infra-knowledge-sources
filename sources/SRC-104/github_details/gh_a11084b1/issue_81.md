# [Issue #81] rocprofv3 att

source: https://github.com/ROCm/rocprofiler-sdk/issues/81
state: closed | updated: 2025-07-14T18:29:53Z
labels: Under Investigation

## 正文

Hi! Within the AMD-provided docker image:
https://hub.docker.com/r/rocm/7.0-preview

I am trying to use rocprofv3, but getting this error:

```
rocprofv3 --att=true \
          --att-library-path /opt/rocm/lib \
          -d transpose_matmul \
          -- python3 test_python.py
usage: rocprofv3 [options] -- <application> [application options]
rocprofv3: error: unrecognized arguments: --att=true --att-library-path /opt/rocm/lib
```

Is there some reason that att is not available? Do rocm-6.5.0 or 7.0 (the docker's rocm versions) have support as yet?

My installation procedure is leading to crashes:

```
mkdir -p rocprofiler-setup
cd rocprofiler-setup

git clone https://github.com/ROCm/rocprofiler-sdk.git rocprofiler-sdk-source
apt-get install libdw-dev
cmake -B rocprofiler-sdk-build -DCMAKE_INSTALL_PREFIX=/opt/rocm -DCMAKE_PREFIX_PATH=/opt/rocm rocprofiler-sdk-source
cmake --build rocprofiler-sdk-build --target all --parallel $(nproc)
cmake --build rocprofiler-sdk-build --target install

wget https://github.com/ROCm/rocprof-trace-decoder/releases/download/0.1.1/rocprof-trace-decoder-ubuntu-24.04-0.1.1-Linux.deb
sudo dpkg -i rocprof-trace-decoder-ubuntu-24.04-0.1.1-Linux.deb

git clone https://github.com/ROCm/aqlprofile.git
cd aqlprofile
./build.sh
cd build
sudo make install
cd ../../..
rm -rf rocprofiler-setup
```

This seems like part of the error in the AMD-provided docker:
```
^[[m     14027:	/lib/x86_64-linux-gnu/libc.so.6: error: version lookup error: version `GLIBC_2.38' not found (required by /opt/rocm/lib/librocprof-trace-decoder.so) (fatal)
^[[0;31mF20250713 20:18:44.351873 128144074837056 att_lib_wrapper.cpp:126] Error loading decoder: 37
^[[m    @     0x748beae7a930  google::LogMessage::Fail()
```

Thank you for your help!

## 评论 (2)

### ppanchad-amd · 2025-07-14

Hi @simran-arora. Internal ticket has been created to assist with your issue. Thanks!

### simran-arora · 2025-07-14

I've resolved the issue and forgot to update - the AMD-provided docker containers use an older Ubuntu version so I needed to adjust the decoder installation paths. Thanks for your help!
This is the container I was using: https://hub.docker.com/r/rocm/7.0-preview
