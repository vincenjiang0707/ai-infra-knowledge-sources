# [Issue #3347] [Bug] Not Able to build the MLCChat #3346

source: https://github.com/mlc-ai/mlc-llm/issues/3347
state: closed | updated: 2026-03-02T14:48:52Z
labels: bug

## 正文

Additional context

-- TVM_SOURCE_DIR: D:/XX/mlc-llm/android/mlc4j/../../3rdparty/tvm
-- JNI_INCLUDE_DIRS=D:/androidSdk/sdk/sdk/ndk/27.0.11718014/toolchains/llvm/prebuilt/windows-x86_64/sysroot/usr/include
-- Configuring done (1.1s)
-- Generating done (0.4s)
-- Build files have been written to: D:/XX/mlc-llm/android/MLCChat/build
[2025-09-18 14:23:53] INFO prepare_libs.py:58: Running cmake build
[0/2] Re-checking globbed directories...
[2/2] Linking CXX shared library libtvm4j_runtime_packed.so
FAILED: libtvm4j_runtime_packed.so
C:\WINDOWS\system32\cmd.exe /C "cd . && D:\androidSdk\sdk\sdk\ndk\27.0.11718014\toolchains\llvm\prebuilt\windows-x86_64\bin\clang++.exe --target=aarch64-none-linux-android24 --sysroot=D:/androidSdk/sdk/sdk/ndk/27.0.11718014/toolchains/llvm/prebuilt/windows-x86_64/sysroot -fPIC -g -DANDROID -fdata-sections -ffunction-sections -funwind-tables -fstack-protector-strong -no-canonical-prefixes -D_FORTIFY_SOURCE=2 -Wformat -Werror=format-security  "-O3" -O3 -DNDEBUG  -shared -static-libstdc++ -Wl,--build-id=sha1 -Wl,--no-rosegment -Wl,--no-undefined-version -Wl,--fatal-warnings -Wl,--no-undefined -Qunused-arguments  -Wl,--gc-sections  -Xlinker --dependency-file=CMakeFiles\tvm4j_runtime_packed.dir\link.d -Wl,-soname,libtvm4j_runtime_packed.so -o libtvm4j_runtime_packed.so CMakeFiles/tvm4j_runtime_packed.dir/D_/XX/mlc-llm/3rdparty/tvm/jvm/native/src/main/native/org_apache_tvm_native_c_api.cc.o  mlc_llm/tokenizers/libtokenizers_cpp.a  -llog  -Wl,--whole-archive  mlc_llm/libmlc_llm.a  lib/libmodel_android.a  -Wl,--no-whole-archive  D:/XX/mlc-llm/3rdparty/tvm/build-android/libtvm_runtime.a  mlc_llm/tokenizers/aarch64-linux-android/release/libtokenizers_c.a  mlc_llm/tokenizers/sentencepiece/src/libsentencepiece.a  -pthread  -latomic -lm && cd ."
ld.lld: error: undefined symbol: TVMBackendRegisterSystemLibSymbol
>>> referenced by GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_devc
>>>               GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_devc.o:(__cxx_global_var_init) in archive lib/libmodel_android.a
>>> referenced by TVMMod
>>>               lib0.o:(__tvm_module_startup) in archive lib/libmodel_android.a
>>> referenced by TVMMod
>>>               lib0.o:(__tvm_module_startup) in archive lib/libmodel_android.a
>>> referenced 80 more times

ld.lld: error: undefined symbol: TVMFuncCall
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_NT_matmul) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_NT_matmul) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_NT_matmul1) in archive lib/libmodel_android.a
>>> referenced 145 more times

ld.lld: error: undefined symbol: TVMAPISetLastError
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_NT_matmul) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_NT_matmul1) in archive lib/libmodel_android.a
>>> referenced by IRModule.CodeGenLLVM:0
>>>               lib0.o:(GuPi_q0f16_d7f22b59f2bf57680dcb05d70e9a87df_NT_matmul10) in archive lib/libmodel_android.a
>>> referenced 155 more times
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
ninja: build stopped: subcommand failed.
Traceback (most recent call last):
  File "D:\XX\mlc-llm\android\mlc4j\prepare_libs.py", line 123, in <module>
    main(parsed.mlc_llm_source_dir)
  File "D:\XX\mlc-llm\android\mlc4j\prepare_libs.py", line 106, in main
    run_cmake_build()
  File "D:\XX\mlc-llm\android\mlc4j\prepare_libs.py", line 69, in run_cmake_build
    subprocess.run(cmd, check=True, env=os.environ)
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Lib\subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['cmake', '--build', '.', '--target', 'tvm4j_runtime_packed', '--config', 'release', '-j16']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Scripts\mlc_llm.exe\__main__.py", line 6, in <module>
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Lib\site-packages\mlc_llm\__main__.py", line 53, in main
    cli.main(sys.argv[2:])
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Lib\site-packages\mlc_llm\cli\package.py", line 64, in main
    package(
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Lib\site-packages\mlc_llm\interface\package.py", line 361, in package
    build_android_binding(mlc_llm_source_dir, output)
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Lib\site-packages\mlc_llm\interface\package.py", line 275, in build_android_binding
    subprocess.run([sys.executable, mlc4j_path / "prepare_libs.py"], check=True, env=os.environ)
  File "C:\Users\vvv\.conda\envs\mlc-llm-venv\Lib\subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['C:\\Users\\vvv\\.conda\\envs\\mlc-llm-venv\\python.exe', WindowsPath('D:/XX/mlc-llm/android/mlc4j/prepare_libs.py')]' returned non-zero exit status 1.

## 评论 (2)

### qiulinjian · 2025-09-18

"What should I do if I encounter this kind of problem?"

### Juryorca · 2025-10-21

Same
