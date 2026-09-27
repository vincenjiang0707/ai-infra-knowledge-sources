# [Issue #3307] [Bug] mlc_llm package error

source: https://github.com/mlc-ai/mlc-llm/issues/3307
state: closed | updated: 2026-01-25T17:22:37Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->

## To Reproduce

Steps to reproduce the behavior:

1.mlc_llm convert_weight ...  successed
2.mlc_llm gen_config ... successed
3.mlc_llm compile ... success 
4.mlc_llm package error
error main info: CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles". 

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->

(llm3) llm@llm-virtual-machine:~/mlc-llm/android/MLCChat$ mlc_llm package
[2025-08-16 13:01:59] INFO package.py:327: MLC LLM HOME: "/home/llm/mlc-llm"
[2025-08-16 13:01:59] INFO package.py:28: Clean up all directories under "dist/bundle"
[2025-08-16 13:01:59] INFO jit.py:43: MLC_JIT_POLICY = ON. Can be one of: ON, OFF, REDO, READONLY
[2025-08-16 13:01:59] INFO package.py:86: Model lib path for "llama2_q4f16_1" is not specified in "model_lib_path_for_prepare_libs".Now jit compile the model library.
[2025-08-16 13:01:59] INFO jit.py:158: Using cached model lib: /home/llm/.cache/mlc_llm/model_lib/d7c5d287342a91cdfe409b2df4ba9d78.tar
[2025-08-16 13:01:59] INFO package.py:129: Bundle weight for llama2-q4f16_1, copy into dist/bundle/llama2-q4f16_1
[2025-08-16 13:02:02] INFO package.py:154: Dump the app config below to "dist/bundle/mlc-app-config.json":
{
  "model_list": [
    {
      "model_id": "llama2-q4f16_1",
      "model_lib": "llama2_q4f16_1",
      "model_url": "/home/llm/dist/Llama-2-7b-chat-hf-q4f16_1-MLC",
      "estimated_vram_bytes": 2960000000
    }
  ]
}
[2025-08-16 13:02:03] INFO package.py:211: Creating lib from ['/home/llm/dist/libs/Llama-2-7b-chat-hf-q4f16_1-android.tar', '/home/llm/.cache/mlc_llm/model_lib/d7c5d287342a91cdfe409b2df4ba9d78.tar']
[2025-08-16 13:02:03] INFO package.py:212: Validating the library dist/lib/libmodel_android.a
[2025-08-16 13:02:03] INFO package.py:213: List of available model libs packaged: ['llama_q4f16_1', 'llama2_q4f16_1'], if we have '-' in the model_lib string, it will be turned into '_'
[2025-08-16 13:02:03] INFO package.py:256: Validation pass
[2025-08-16 13:02:03] INFO package.py:270: Moving "dist/lib/libmodel_android.a" to "build/lib/libmodel_android.a"
[2025-08-16 13:02:03] INFO package.py:274: Building mlc4j
info: component 'rust-std' for target 'aarch64-linux-android' is up to date
[2025-08-16 13:02:05] INFO prepare_libs.py:93: Entering "/home/llm/mlc-llm/android/MLCChat/build" for MLC LLM and tvm4j build.
[2025-08-16 13:02:05] INFO prepare_libs.py:23: Running cmake
CMake Error: CMake was unable to find a build program corresponding to "Unix Makefiles".  CMAKE_MAKE_PROGRAM is not set.  You probably need to select a different build tool.
-- Configuring incomplete, errors occurred!
See also "/home/llm/mlc-llm/android/MLCChat/build/CMakeFiles/CMakeOutput.log".
Traceback (most recent call last):
  File "/home/llm/mlc-llm/android/mlc4j/prepare_libs.py", line 122, in <module>
    main(parsed.mlc_llm_source_dir)
  File "/home/llm/mlc-llm/android/mlc4j/prepare_libs.py", line 104, in main
    run_cmake(mlc_llm_source_dir / "android" / "mlc4j")
  File "/home/llm/mlc-llm/android/mlc4j/prepare_libs.py", line 53, in run_cmake
    subprocess.run(cmd, check=True, env=os.environ)
  File "/home/llm/anaconda3/envs/llm3/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['cmake', '/home/llm/mlc-llm/android/mlc4j', '-DCMAKE_BUILD_TYPE=Release', '-DCMAKE_TOOLCHAIN_FILE=/home/llm/Android/Sdk/ndk/27.0.11718014/build/cmake/android.toolchain.cmake', '-DCMAKE_INSTALL_PREFIX=.', '-DCMAKE_CXX_FLAGS="-O3"', '-DANDROID_ABI=arm64-v8a', '-DANDROID_NATIVE_API_LEVEL=android-24', '-DANDROID_PLATFORM=android-24', '-DCMAKE_FIND_ROOT_PATH_MODE_PACKAGE=ON', '-DANDROID_STL=c++_static', '-DUSE_HEXAGON_SDK=OFF', '-DMLC_LLM_INSTALL_STATIC_LIB=ON', '-DCMAKE_SKIP_INSTALL_ALL_DEPENDENCY=ON', '-DUSE_OPENCL=ON', '-DUSE_OPENCL_ENABLE_HOST_PTR=ON', '-DUSE_CUSTOM_LOGGING=ON', '-DTVM_FFI_USE_LIBBACKTRACE=OFF', '-DTVM_FFI_BACKTRACE_ON_SEGFAULT=OFF']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "/home/llm/anaconda3/envs/llm3/bin/mlc_llm", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/llm/anaconda3/envs/llm3/lib/python3.11/site-packages/mlc_llm/__main__.py", line 54, in main
    cli.main(sys.argv[2:])
  File "/home/llm/anaconda3/envs/llm3/lib/python3.11/site-packages/mlc_llm/cli/package.py", line 64, in main
    package(
  File "/home/llm/anaconda3/envs/llm3/lib/python3.11/site-packages/mlc_llm/interface/package.py", line 361, in package
    build_android_binding(mlc_llm_source_dir, output)
  File "/home/llm/anaconda3/envs/llm3/lib/python3.11/site-packages/mlc_llm/interface/package.py", line 275, in build_android_binding
    subprocess.run([sys.executable, mlc4j_path / "prepare_libs.py"], check=True, env=os.environ)
  File "/home/llm/anaconda3/envs/llm3/lib/python3.11/subprocess.py", line 569, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/home/llm/anaconda3/envs/llm3/bin/python', PosixPath('/home/llm/mlc-llm/android/mlc4j/prepare_libs.py')]' returned non-zero exit status 1.


## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA):Android
 - Operating system (e.g. Ubuntu/Windows/MacOS/...):Ubuntu22
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...):Android 15
 - How you installed MLC-LLM (`conda`, source):conda
 - How you installed TVM-Unity (`pip`, source):pip
 - Python version (e.g. 3.10):3.11
 - GPU driver version (if applicable):no
 - CUDA/cuDNN version (if applicable):no
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):/home/llm/anaconda3/envs/llm3/lib/python3.11/site-packages/tvm/__init__.py

 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->
this is my ~/.bashrc
...
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin/java
export ANDROID_NDK=/home/llm/Android/Sdk/ndk/27.0.11718014
export ANDROID_HOME=/home/llm/Android/Sdk
export PATH=$PATH:/home/llm/Android/Sdk/cmake/3.22.1/bin
export PATH=$PATH:/home/llm/Android/Sdk/platform-tools
export TVM_NDK_CC=$ANDROID_NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/aarch64-linux-android24-clang
export TVM_HOME=/home/llm/mlc-llm/3rdparty/tvm
export TVM_HOME=$TVM_HOME/include/tvm/runtime
source $HOME/.cargo/env # Rust



## 评论 (2)

### netslei · 2025-08-16

I have resolved this issue. The reason is that the Ubuntu I installed was a minimal installation, which lacked the make command. After running` sudo apt install build-essential`, I re-executed the process for the mlc_llm package, and it succeeded.

### MasterJH5574 · 2026-01-25

Hi @netslei, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
