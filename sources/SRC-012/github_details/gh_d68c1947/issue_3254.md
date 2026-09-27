# [Issue #3254] [Bug] undefined symbol: nvshmemi_bootstrap_plugin_init

source: https://github.com/mlc-ai/mlc-llm/issues/3254
state: closed | updated: 2026-03-02T14:50:52Z
labels: bug

## 正文

## 🐛 Bug

<!-- mlc_llm serve  start model with P-D disaggregation and enable NVSHMEM-->

## To Reproduce
### install nv hpc cuda toolkit 
 which was installed in /opt/nvidia/hpc_sdk/Linux_x86_64/25.3/

### build tvm
    cd /path/mlc-llm/3rdparty/tvm/
    rm -f -R build
    mkdir build 
    cd build 

    cp ../cmake/config.cmake .

    export LLVM_PATH=/usr/bin/llvm-config
    sed -i "/.*set(USE_LLVM OFF)*/c\set(USE_LLVM ${LLVM_PATH})" config.cmake
    sed -i "/.*set(USE_CUDA OFF)*/c\set(USE_CUDA ON)" config.cmake
    sed -i "/.*set(USE_NVSHMEM OFF)*/c\set(USE_NVSHMEM ON)" config.cmake
    sed -i "/.*set(USE_CUDNN OFF)*/c\set(USE_CUDNN ON)" config.cmake
    sed -i "/.*set(USE_CUBLAS OFF)*/c\set(USE_CUBLAS ON)" config.cmake
    sed -i "/.*set(USE_CUTLASS OFF)*/c\set(USE_CUTLASS ON)" config.cmake
    sed -i "/.*set(USE_FLASHINFER OFF)*/c\set(USE_FLASHINFER ON)" config.cmake
    sed -i "/.*set(USE_NCCL OFF)*/c\set(USE_NCCL ON)" config.cmake

    cmake .. -DCMAKE_CUDA_ARCHITECTURES="86" \
            -DCUDA_CUBLAS_LIBRARY=/opt/nvidia/hpc_sdk/Linux_x86_64/25.3/math_libs/lib64/libcublas.so \
            -DCUDA_CUBLASLT_LIBRARY=/opt/nvidia/hpc_sdk/Linux_x86_64/25.3/math_libs/lib64/libcublasLt.so \
            -DCUDA_CURAND_LIBRARY=/opt/nvidia/hpc_sdk/Linux_x86_64/25.3/math_libs/lib64/


    make -j64
    echo "Finished."

## deploy model and start it
    export MODEL_ROOT=/data/llm_models
    export MODEL_NAME=Llama-2-7b-chat-hf
    export QUANT_NAME=q0f16

    cd ~
    mlc_llm convert_weight ${MODEL_ROOT}/${MODEL_NAME} \
                        --quantization ${QUANT_NAME} \
                        -o ${MODEL_ROOT}/${MODEL_NAME}-${QUANT_NAME}-MLC

    mlc_llm gen_config ${MODEL_ROOT}/${MODEL_NAME} \
        --quantization ${QUANT_NAME} --conv-template llama-2 \
        --tensor-parallel-shards 4 \
        -o ${MODEL_ROOT}/${MODEL_NAME}-${QUANT_NAME}-MLC

    mlc_llm compile ${MODEL_ROOT}/${MODEL_NAME}-${QUANT_NAME}-MLC/mlc-chat-config.json \
                    --device cuda \
                    --opt O3 \
                    --overrides "tensor_parallel_shards=4;disaggregation=1" \
                    -o ${MODEL_ROOT}/libs/${MODEL_NAME}-${QUANT_NAME}-cuda-tp4-disagg.so

    # ## Launch 1 engine with TP 4
    python3 -m mlc_llm serve ${MODEL_ROOT}/${MODEL_NAME}-${QUANT_NAME}-MLC \
                --model-lib ${MODEL_ROOT}/libs/${MODEL_NAME}-${QUANT_NAME}-cuda-tp4-disagg.so \
                --mode server --host 127.0.0.1 --port 9123 \
                --device cuda --prefix-cache-mode disable \
                # --enable-debug

## config MLC_NVSHMEM_INIT_CONFIG_JSON_STR
MLC_NVSHMEM_INIT_CONFIG_JSON_STR='{"uid": [65664, 2, 0, -65, 11, -84, 17, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, -108, 114, -10, 92, -70, -56, 9, 3, 0, 0, 0, 0, 0, 0, 0, 64, 2, 55, -118, -9, 85, 0, 0, 16, -65, 81, -84, -62, 127, 0, 0, 80, 66, 53, -118, -9, 85, 0, 0, 16, -65, 81, -84, -62, 127, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, -128, 35, -21, 78, -61, 127, 0, 0, 64, 2, 55, -118, -9, 85, 0, 0, -128, 41, -18, 78, -61, 127, 0, 0, 16, -65, 81, -84, -62, 127, 0, 0, 28, -73, 119, -119, -9, 85, 0, 0], "npes": 4, "pe_start": 0}'



# Error as follows:
root@d961cf47eec9:/home//repo# ./t1 
[2025-06-17 02:18:53] INFO auto_device.py:79: Found device: cuda:0
[2025-06-17 02:18:53] INFO auto_device.py:79: Found device: cuda:1
[2025-06-17 02:18:53] INFO auto_device.py:79: Found device: cuda:2
[2025-06-17 02:18:53] INFO auto_device.py:79: Found device: cuda:3
[2025-06-17 02:18:53] INFO auto_device.py:79: Found device: cuda:4
[2025-06-17 02:18:53] INFO engine_base.py:142: Using library model: /data/llm_models/libs/Llama-2-7b-chat-hf-q0f16-cuda-tp4-disagg.so
[2025-06-17 02:18:53] INFO engine_base.py:192: The selected engine mode is server. We use as much GPU memory as possible (within the limit of gpu_memory_utilization).
[2025-06-17 02:18:53] INFO engine_base.py:200: If you have low concurrent requests and want to use less GPU memory, please select mode "local".
[2025-06-17 02:18:53] INFO engine_base.py:205: If you don't have concurrent requests and only use the engine interactively, please select mode "interactive".
[02:19:06] /home//repo/mlc-llm/cpp/serve/engine.cc:408: Intiailizing NVSHMEM
[02:19:06] /home//repo/mlc-llm/cpp/serve/engine.cc:420: NVSHMEM initialized successfully.
[02:19:06] /home//repo/mlc-llm/cpp/serve/config.cc:798: Under mode "local", max batch size will be set to 4, max KV cache token capacity will be set to 4096, prefill chunk size will be set to 4096. 
[02:19:06] /home//repo/mlc-llm/cpp/serve/config.cc:798: Under mode "interactive", max batch size will be set to 1, max KV cache token capacity will be set to 4096, prefill chunk size will be set to 4096. 
[02:19:06] /home//repo/mlc-llm/cpp/serve/config.cc:798: Under mode "server", max batch size will be set to 128, max KV cache token capacity will be set to 120261, prefill chunk size will be set to 4096. 
[02:19:06] /home//repo/mlc-llm/cpp/serve/config.cc:879: The actual engine mode is "server". So max batch size is 128, max KV cache token capacity is 120261, prefill chunk size is 4096.
[02:19:06] /home//repo/mlc-llm/cpp/serve/config.cc:884: Estimated total single GPU memory usage: 19208.825 MB (Parameters: 3588.508 MB. KVCache: 15113.060 MB. Temporary buffer: 507.257 MB). The actual usage might be slightly larger than the estimated number.
/dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/modules/bootstrap/uid/ncclSocket/ncclsocket_socket.cpp:socketStartConnect:479: socketStartConnect: exceeded retries (20000)
/dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/modules/bootstrap/uid/bootstrap_uid.cpp:721: non-zero status: -6 /dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/host/bootstrap/bootstrap_loader.cpp:103: non-zero status: -6 Bootstrap plugin init failed for 'nvshmem_bootstrap_uid.so.3'

/dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/host/bootstrap/bootstrap_loader.cpp:100: NULL value Bootstrap failed to get symbol 'nvshmemi_bootstrap_plugin_init'
        �>
          ��U: undefined symbol: nvshmemi_bootstrap_plugin_init

/dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/host/bootstrap/bootstrap.cpp:240: non-zero status: 7 bootstrap_loader_init returned error for mode UID

/dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/host/init/init.cu:327: non-zero status: 7 bootstrap_init failed 

/dvs/p4/build/sw/rel/gpgpu/toolkit/r12.8/main_nvshmem/src/host/init/init.cu:1149: non-zero status: 7 nvshmem_bootstrap failed 

## 评论 (1)

### KrisLu999 · 2025-07-08

Have you managed to solve this issue? I’ve run into the same problem.
