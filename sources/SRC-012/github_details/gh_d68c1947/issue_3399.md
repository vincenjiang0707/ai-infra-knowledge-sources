# [Issue #3399] [Bug] 'tvm/ffi/any.h' file not found

source: https://github.com/mlc-ai/mlc-llm/issues/3399
state: closed | updated: 2026-02-27T22:05:03Z
labels: bug

## 正文

## 🐛 Bug

While trying to install WASM build environment using the guide from: [https://llm.mlc.ai/docs/install/emcc.html#install-web-build ](), in Google Colab, on the following step:
`./web/prep_emcc_deps.sh`
returns the error:
`emcc/wasm_runtime.cc:33:10: fatal error: 'tvm/ffi/any.h' file not found` 
(full error below)

## To Reproduce

Steps to reproduce the behavior (In colab):

1. `!pip install --upgrade torch torchvision torchaudio`
2. `!python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cu128 mlc-ai-nightly-cu128`
3. `!git clone https://github.com/emscripten-core/emsdk.git`
4. `!cd emsdk && ./emsdk install latest`
5. `!cd emsdk && ./emsdk activate latest`
6. `!cd emsdk && source ./emsdk_env.sh` (for reference)
7. Update the environment variables to include the Emscripten directories:

    ```python
    import os 
    # Define the variables based on your output 
    os.environ['EMSDK'] = '/content/emsdk' 
    os.environ['EMSDK_NODE'] = '/content/emsdk/node/22.16.0_64bit/bin/node'

    # Update the PATH
    emscripten_paths = [
        '/content/emsdk',
        '/content/emsdk/upstream/emscripten'
    ]
    os.environ['PATH'] = ":".join(emscripten_paths) + ":" + os.environ['PATH']
    ```
8. `!emcc --version` (verification)
9. Find the location of `tvm` and `mlc_llm` for reference:

    ```python
    import mlc_llm
    print(mlc_llm)
    import tvm
    print(tvm.__file__)
    ```
10. Set env vars:

    ```python
    import os
    os.environ['TVM_SOURCE_DIR'] = '/usr/local/lib/python3.12/dist-packages/tvm'
    os.environ['MLC_LLM_SOURCE_DIR'] = '/usr/local/lib/python3.12/dist-packages/mlc_llm'
    ```
11. `!git clone https://github.com/mlc-ai/mlc-llm.git --recursive`
12. `!cd  mlc-llm && ./web/prep_emcc_deps.sh`


<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->
## Full Error:

```bash
+ emcc --version
emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 4.0.22 (0f3d2e62bccf8e14497ff19e05a1202c51eb0c65)
Copyright (C) 2025 the Emscripten authors (see AUTHORS.txt)
This is free and open source software under the MIT license.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

+ npm --version
10.8.2
+ TVM_SOURCE_DIR_SET=/usr/local/lib/python3.12/dist-packages/tvm
+ git submodule update --init --recursive
++ pwd
+ CURR_DIR=/content/mlc-llm
+ [[ -z /usr/local/lib/python3.12/dist-packages/tvm ]]
+ cd web
+ make
emcc -I/usr/local/lib/python3.12/dist-packages/tvm -I/usr/local/lib/python3.12/dist-packages/tvm/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dlpack/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dmlc-core/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/compiler-rt -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/picojson -I/content/mlc-llm/3rdparty/tokenizers-cpp -I/content/mlc-llm/3rdparty/tokenizers-cpp/include -I/content/mlc-llm/cpp -O3 -std=c++17 -Wno-ignored-attributes -c -MM -MT dist/wasm/mlc_wasm_runtime.bc emcc/mlc_wasm_runtime.cc >dist/wasm/mlc_wasm_runtime.d
clang: warning: argument unused during compilation: '-c' [-Wunused-command-line-argument]
emcc -I/usr/local/lib/python3.12/dist-packages/tvm -I/usr/local/lib/python3.12/dist-packages/tvm/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dlpack/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dmlc-core/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/compiler-rt -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/picojson -I/content/mlc-llm/3rdparty/tokenizers-cpp -I/content/mlc-llm/3rdparty/tokenizers-cpp/include -I/content/mlc-llm/cpp -O3 -std=c++17 -Wno-ignored-attributes -emit-llvm -c -o dist/wasm/mlc_wasm_runtime.bc emcc/mlc_wasm_runtime.cc
emcc -I/usr/local/lib/python3.12/dist-packages/tvm -I/usr/local/lib/python3.12/dist-packages/tvm/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dlpack/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dmlc-core/include -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/compiler-rt -I/usr/local/lib/python3.12/dist-packages/tvm/3rdparty/picojson -I/content/mlc-llm/3rdparty/tokenizers-cpp -I/content/mlc-llm/3rdparty/tokenizers-cpp/include -I/content/mlc-llm/cpp -O3 -std=c++17 -Wno-ignored-attributes -o dist/wasm/mlc_wasm_runtime.wasm dist/wasm/mlc_wasm_runtime.bc --no-entry -s WASM_BIGINT=1 -s ALLOW_MEMORY_GROWTH=1 -s STANDALONE_WASM=1 -s ERROR_ON_UNDEFINED_SYMBOLS=0
clang: warning: argument unused during compilation: '-I /usr/local/lib/python3.12/dist-packages/tvm' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /usr/local/lib/python3.12/dist-packages/tvm/include' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dlpack/include' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /usr/local/lib/python3.12/dist-packages/tvm/3rdparty/dmlc-core/include' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /usr/local/lib/python3.12/dist-packages/tvm/3rdparty/compiler-rt' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /usr/local/lib/python3.12/dist-packages/tvm/3rdparty/picojson' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /content/mlc-llm/3rdparty/tokenizers-cpp' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /content/mlc-llm/3rdparty/tokenizers-cpp/include' [-Wunused-command-line-argument]
clang: warning: argument unused during compilation: '-I /content/mlc-llm/cpp' [-Wunused-command-line-argument]
+ cd -
/content/mlc-llm
+ cd /usr/local/lib/python3.12/dist-packages/tvm/web
+ TVM_HOME=/usr/local/lib/python3.12/dist-packages/tvm
+ make
emcc -I/usr/local/lib/python3.12/dist-packages/tvm/web/../ -I/usr/local/lib/python3.12/dist-packages/tvm/web/..//include -I/usr/local/lib/python3.12/dist-packages/tvm/web/..//3rdparty/tvm-ffi/include -I/usr/local/lib/python3.12/dist-packages/tvm/web/..//3rdparty/tvm-ffi/3rdparty/dlpack/include -I/usr/local/lib/python3.12/dist-packages/tvm/web/..//3rdparty/dmlc-core/include -I/usr/local/lib/python3.12/dist-packages/tvm/web/..//3rdparty/compiler-rt -I/usr/local/lib/python3.12/dist-packages/tvm/web/..//3rdparty/picojson -O3 -std=c++17 -Wno-ignored-attributes -c -MM -MT dist/wasm/wasm_runtime.bc emcc/wasm_runtime.cc >dist/wasm/wasm_runtime.d
clang: warning: argument unused during compilation: '-c' [-Wunused-command-line-argument]
emcc/wasm_runtime.cc:33:10: fatal error: 'tvm/ffi/any.h' file not found
   33 | #include <tvm/ffi/any.h>
      |          ^~~~~~~~~~~~~~~
1 error generated.
make: *** [Makefile:39: dist/wasm/wasm_runtime.bc] Error 1
```


## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->
Successful installation of WASM build env.

## Environment

 - Platform: CUDA (T4 runtime in Colab)
 - Operating system (e.g. Ubuntu/Windows/MacOS/...):
 - Device: Nvidia T4
 - How you installed MLC-LLM and TVM: `!python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cu128 mlc-ai-nightly-cu128`
 - Python version: 3.12
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (4)

### MasterJH5574 · 2026-01-25

Hi @vmanvs sorry for the late reply.  I think it was because the `TVM_SOURCE_DIR` is pointing to a wrong place. The one you have
```
os.environ['TVM_SOURCE_DIR'] = '/usr/local/lib/python3.12/dist-packages/tvm'
os.environ['MLC_LLM_SOURCE_DIR'] = '/usr/local/lib/python3.12/dist-packages/mlc_llm'
```
means that `TVM_SOURCE_DIR` and `MLC_LLM_SOURCE_DIR` are pointing to the pip-installed packages, which does not come with TVM FFI and other header files.

You should point them to the path you cloned from GitHub by `!git clone https://github.com/mlc-ai/mlc-llm.git --recursive`. For example,
```
os.environ['TVM_SOURCE_DIR'] = '/path/to/cloned/mlc-llm/3rdparty/tvm'
os.environ['MLC_LLM_SOURCE_DIR'] = '/path/to/cloned/mlc-llm'
```

### MasterJH5574 · 2026-01-25

@vmanvs As developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC, WebLLM, and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!

### vmanvs · 2026-01-28

Here's the link to Google Colab notebook:

https://colab.research.google.com/drive/1R6w6QxfzXs6uvXbpkrXtpVl50nZu2ZtI?usp=sharing

It might be a bit messy, since I went back and forth trying to fix stuff, if there's anything I could clarify on, let me know.

### yatish04 · 2026-02-06

@vmanvs I think this is happening because TVM_SOURCE_DIR is incorrect. I was able to compile with below TVM_SOURCE_DIR. Also you are setting environ variable in python but compiling mlc which is not right.

<img width="630" height="861" alt="Image" src="https://github.com/user-attachments/assets/cf2c71b9-77ce-4d7e-848b-97ca659ceb41" />
