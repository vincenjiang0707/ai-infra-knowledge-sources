# [Issue #3240] [Bug] Not  Able to build the MLCChat

source: https://github.com/mlc-ai/mlc-llm/issues/3240
state: closed | updated: 2026-03-02T14:51:18Z
labels: bug

## 正文

## 🐛 Bug

<!--Not able to build the MLCChat android app -->

## To Reproduce

Steps to reproduce the behavior:

1. clone the rep 
1.set the envs 
1.mlc_llm package

<!-- 

FAILED: libtvm4j_runtime_packed.so
C:\WINDOWS\system32\cmd.exe /C "cd . && C:\Users\chakr\AppData\Local\Android\Sdk\ndk\27.0.12077973\toolchains\llvm\prebuilt\windows-x86_64\bin\clang++.exe --target=aarch64-none-linux-android24 --sysroot=C:/Users/chakr/AppData/Local/Android/Sdk/ndk/27.0.12077973/toolchains/llvm/prebuilt/windows-x86_64/sysroot -fPIC -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security  "-O3" -O3 -DNDEBUG  -static-libstdc++ -Wl,--build-id=sha1 -Wl,--no-rosegment -Wl,--no-undefined-version -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments  -Wl,--gc-sections   -Xlinker --dependency-file=CMakeFiles\tvm4j_runtime_packed.dir\link.d -shared -Wl,-soname,libtvm4j_runtime_packed.so -o libtvm4j_runtime_packed.so CMakeFiles/tvm4j_runtime_packed.dir/C_/Users/chakr/OneDrive/Documents/mlc-llm/3rdparty/tvm/jvm/native/src/main/native/org_apache_tvm_native_c_api.cc.o  mlc_llm/tokenizers/libtokenizers_cpp.a  -llog  -Wl,--whole-archive  mlc_llm/libmlc_llm.a  lib/libmodel_android.a  -Wl,--no-whole-archive  mlc_llm/tokenizers/aarch64-linux-android/release/libtokenizers_c.a  mlc_llm/tokenizers/sentencepiece/src/libsentencepiece.a  -pthread  -latomic -lm && cd ."
ld.lld: error: undefined symbol: TVMFuncCall
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(mistral_q4f16_1_c2cba77a6def4dd52f7e20b5d8576ab5_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(mistral_q4f16_1_c2cba77a6def4dd52f7e20b5d8576ab5_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(llama_q4f16_0_2d32572d8a4ab2af20a1f587ef6c8c63__gather_hidden_states) in archive lib/libmodel_android.a
>>> referenced 459 more times

ld.lld: error: undefined symbol: TVMAPISetLastError
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(mistral_q4f16_1_c2cba77a6def4dd52f7e20b5d8576ab5_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(llama_q4f16_0_2d32572d8a4ab2af20a1f587ef6c8c63__gather_hidden_states) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(gemma2_q4f16_1_5cc7dbd3ae3d1040984d9720b2d7b7d4_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced 528 more times
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
Traceback (most recent call last):
  File "C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\prepare_libs.py", line 122, in <module>
    main(parsed.mlc_llm_source_dir)
  File "C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\prepare_libs.py", line 105, in main
    run_cmake_build()
  File "C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\prepare_libs.py", line 68, in run_cmake_build
    subprocess.run(cmd, check=True, env=os.environ)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['cmake', '--build', '.', '--target', 'tvm4j_runtime_packed', '--config', 'release', '-j16']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\Scripts\mlc_llm.exe\__main__.py", line 7, in <module>
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\__main__.py", line 53, in main
    cli.main(sys.argv[2:])
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\cli\package.py", line 64, in main
    package(
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\interface\package.py", line 361, in package
    build_android_binding(mlc_llm_source_dir, output)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\interface\package.py", line 275, in build_android_binding
    subprocess.run([sys.executable, mlc4j_path / "prepare_libs.py"], check=True, env=os.environ)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['C:\\Users\\chakr\\miniconda3\\envs\\mlc-llm\\python.exe', WindowsPath('C:/Users/chakr/OneDrive/Documents/mlc-llm/android/mlc4j/prepare_libs.py')]' returned non-zero exit status 1.
 -->

## Expected behavior

<!-- I want to compile the MLCChat  app and use the build files . -->

## Environment

 - Platform (Android):
 - Operating system (Windows):
 - Device (Laptop+RTX 3060)
 - How you installed MLC-LLM (`conda`, source):
 - How you installed TVM-Unity (`pip`, source):
 - Python version (3.10):
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Unity Hash Tag (`GIT_COMMIT_HASH: 2685d6ace64c30a077c1b3f6893d2e38589be7bb`):
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->
```
C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\..\..\3rdparty\tvm\jvm\core\src\main\java\org\apache\tvm\TVMObject.java:39: warning: [removal] finalize() in Object has been deprecated and marked for removal
    super.finalize();
         ^
C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\..\..\3rdparty\tvm\jvm\core\src\main\java\org\apache\tvm\NDArrayBase.java:49: warning: [removal] finalize() in Object has been deprecated and marked for removal
  @Override protected void finalize() throws Throwable {
                           ^
C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\..\..\3rdparty\tvm\jvm\core\src\main\java\org\apache\tvm\NDArrayBase.java:51: warning: [removal] finalize() in Object has been deprecated and marked for removal
    super.finalize();
         ^
4 warnings
[141/162] Linking CXX static library mlc_llm\tvm\libtvm_runtime.a
You have build static version of the TVM runtime library. Make sure to use --whole-archive when linking it into your project.
[144/162] Generating aarch64-linux-android/release/libtokenizers_c.a
   Compiling proc-macro2 v1.0.95
   Compiling unicode-ident v1.0.18
   Compiling crossbeam-utils v0.8.21
   Compiling memchr v2.7.4
   Compiling fnv v1.0.7
   Compiling ident_case v1.0.1
   Compiling libc v0.2.172
   Compiling strsim v0.11.1
   Compiling serde v1.0.219
   Compiling shlex v1.3.0
   Compiling zerocopy v0.8.25
   Compiling pkg-config v0.3.32
   Compiling rayon-core v1.12.1
   Compiling either v1.15.0
   Compiling cfg-if v1.0.0
   Compiling paste v1.0.15
   Compiling cc v1.2.25
   Compiling serde_json v1.0.140
   Compiling thiserror v2.0.12
   Compiling regex-syntax v0.8.5
   Compiling esaxx-rs v0.1.10
   Compiling minimal-lexical v0.2.1
   Compiling itertools v0.11.0
   Compiling aho-corasick v1.1.3
   Compiling nom v7.1.3
   Compiling base64 v0.13.1
   Compiling ryu v1.0.20
   Compiling smallvec v1.15.0
   Compiling onig_sys v69.9.1
   Compiling once_cell v1.21.3
   Compiling regex-automata v0.4.9
   Compiling bitflags v2.9.1
   Compiling itoa v1.0.15
   Compiling macro_rules_attribute-proc_macro v0.2.2
   Compiling unicode-segmentation v1.12.0
   Compiling quote v1.0.40
   Compiling crossbeam-epoch v0.9.18
   Compiling getrandom v0.2.16
   Compiling unicode-normalization-alignments v0.1.12
   Compiling crossbeam-deque v0.8.6
   Compiling syn v2.0.101
   Compiling rand_core v0.6.4
   Compiling itertools v0.13.0
   Compiling unicode_categories v0.1.1
   Compiling lazy_static v1.5.0
   Compiling macro_rules_attribute v0.2.2
   Compiling ppv-lite86 v0.2.21
   Compiling log v0.4.27
   Compiling rand_chacha v0.3.1
   Compiling regex v1.11.1
   Compiling rand v0.8.5
   Compiling rayon v1.10.0
   Compiling darling_core v0.20.11
   Compiling rayon-cond v0.3.0
   Compiling serde_derive v1.0.219
   Compiling monostate-impl v0.1.14
   Compiling thiserror-impl v2.0.12
   Compiling darling_macro v0.20.11
   Compiling darling v0.20.11
   Compiling derive_builder_core v0.20.2
   Compiling derive_builder_macro v0.20.2
   Compiling derive_builder v0.20.2
   Compiling monostate v0.1.14
   Compiling spm_precompiled v0.1.4
   Compiling onig v6.5.1
   Compiling tokenizers v0.21.1
   Compiling tokenizers-c v0.1.0 (C:\Users\chakr\OneDrive\Documents\mlc-llm\3rdparty\tokenizers-cpp\rust)
    Finished `release` profile [optimized] target(s) in 1m 09s
[161/162] Linking CXX shared library libtvm4j_runtime_packed.so
FAILED: libtvm4j_runtime_packed.so
C:\WINDOWS\system32\cmd.exe /C "cd . && C:\Users\chakr\AppData\Local\Android\Sdk\ndk\27.0.12077973\toolchains\llvm\prebuilt\windows-x86_64\bin\clang++.exe --target=aarch64-none-linux-android24 --sysroot=C:/Users/chakr/AppData/Local/Android/Sdk/ndk/27.0.12077973/toolchains/llvm/prebuilt/windows-x86_64/sysroot -fPIC -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security  "-O3" -O3 -DNDEBUG  -static-libstdc++ -Wl,--build-id=sha1 -Wl,--no-rosegment -Wl,--no-undefined-version -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments  -Wl,--gc-sections   -Xlinker --dependency-file=CMakeFiles\tvm4j_runtime_packed.dir\link.d -shared -Wl,-soname,libtvm4j_runtime_packed.so -o libtvm4j_runtime_packed.so CMakeFiles/tvm4j_runtime_packed.dir/C_/Users/chakr/OneDrive/Documents/mlc-llm/3rdparty/tvm/jvm/native/src/main/native/org_apache_tvm_native_c_api.cc.o  mlc_llm/tokenizers/libtokenizers_cpp.a  -llog  -Wl,--whole-archive  mlc_llm/libmlc_llm.a  lib/libmodel_android.a  -Wl,--no-whole-archive  mlc_llm/tokenizers/aarch64-linux-android/release/libtokenizers_c.a  mlc_llm/tokenizers/sentencepiece/src/libsentencepiece.a  -pthread  -latomic -lm && cd ."
ld.lld: error: undefined symbol: TVMFuncCall
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(mistral_q4f16_1_c2cba77a6def4dd52f7e20b5d8576ab5_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(mistral_q4f16_1_c2cba77a6def4dd52f7e20b5d8576ab5_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(llama_q4f16_0_2d32572d8a4ab2af20a1f587ef6c8c63__gather_hidden_states) in archive lib/libmodel_android.a
>>> referenced 459 more times

ld.lld: error: undefined symbol: TVMAPISetLastError
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(mistral_q4f16_1_c2cba77a6def4dd52f7e20b5d8576ab5_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(llama_q4f16_0_2d32572d8a4ab2af20a1f587ef6c8c63__gather_hidden_states) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(gemma2_q4f16_1_5cc7dbd3ae3d1040984d9720b2d7b7d4_apply_bitmask_inplace) in archive lib/libmodel_android.a
>>> referenced 528 more times
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
Traceback (most recent call last):
  File "C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\prepare_libs.py", line 122, in <module>
    main(parsed.mlc_llm_source_dir)
  File "C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\prepare_libs.py", line 105, in main
    run_cmake_build()
  File "C:\Users\chakr\OneDrive\Documents\mlc-llm\android\mlc4j\prepare_libs.py", line 68, in run_cmake_build
    subprocess.run(cmd, check=True, env=os.environ)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['cmake', '--build', '.', '--target', 'tvm4j_runtime_packed', '--config', 'release', '-j16']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\Scripts\mlc_llm.exe\__main__.py", line 7, in <module>
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\__main__.py", line 53, in main
    cli.main(sys.argv[2:])
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\cli\package.py", line 64, in main
    package(
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\interface\package.py", line 361, in package
    build_android_binding(mlc_llm_source_dir, output)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\site-packages\mlc_llm\interface\package.py", line 275, in build_android_binding
    subprocess.run([sys.executable, mlc4j_path / "prepare_libs.py"], check=True, env=os.environ)
  File "C:\Users\chakr\miniconda3\envs\mlc-llm\lib\subprocess.py", line 526, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['C:\\Users\\chakr\\miniconda3\\envs\\mlc-llm\\python.exe', WindowsPath('C:/Users/chakr/OneDrive/Documents/mlc-llm/android/mlc4j/prepare_libs.py')]' returned non-zero exit status 1.

```

## 评论 (2)

### SeaTheDestiny · 2025-06-21

have you fix it? I meet the same bug when I try to build it.

### SeaTheDestiny · 2025-06-25

I fix it, the current version is unstable, when I go back to V0.19.0, everything is fine.

