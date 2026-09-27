# [Issue #3186] [Bug] Binary was created using {relax.Executable} but a loader of that name is not registered. Available loaders are relax.VMExecutable, const_loader, static_library, metal. Perhaps you need to recompile with this runtime enabled.

source: https://github.com/mlc-ai/mlc-llm/issues/3186
state: closed | updated: 2026-03-02T14:53:38Z
labels: bug

## 正文

## 🐛 Bug

After following the steps for installation, running MLCChat, clicking on a model (in this case, i chose the model that came with it "Llama-3.2-3B-Instruct-q4f16_1-MLC") I get this runtime error:

## To Reproduce
Steps to reproduce the behavior:

1. `git clone https://github.com/mlc-ai/mlc-llm.git`
2. `cd mlc-llm`
3. `git submodule update --init --recursive`
4. `cd ./ios`
5. created conda environment with python=3.11, activated the environment, and ran:
`python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu`
7. Continued following the documentation
```
cd /path/to/MLCChat  # e.g., "ios/MLCChat"
export MLC_LLM_SOURCE_DIR=/path/to/mlc-llm  # e.g., "../.."
mlc_llm package
```
8. I confirmed that the dist folder appeared on finder with the correct sub-directories according to the documentation (bundle, lib, etc.)
9. Opened the project, changed apple developer team account
10. Cleaned and build
11. Ran the project through My Mac (Designed for iPad) and also tested using my iPhone 16 pro
12. The project ran and after clicking on one of the models I would then get the runtime error:
```
libc++abi: terminating due to uncaught exception of type tvm::runtime::InternalError: [21:31:13] /Users/jappgalang/Documents/GitHub/mlc-llm/3rdparty/tvm/src/runtime/library_module.cc:122: Binary was created using {relax.Executable} but a loader of that name is not registered. Available loaders are relax.VMExecutable, const_loader, static_library, metal. Perhaps you need to recompile with this runtime enabled.
Stack trace:
  [bt] (0) 1   MLCChat                             0x0000000100f6ab14 tvm::runtime::detail::LogFatal::Entry::Finalize() + 100
  [bt] (1) 2   MLCChat                             0x0000000100f6aab0 tvm::runtime::detail::LogFatal::Entry::Finalize() + 0
  [bt] (2) 3   MLCChat                             0x0000000100f6a524 std::__1::basic_ostream<char, std::__1::char_traits<char>>& std::__1::__put_character_sequence[abi:ne180100]<char, std::__1::char_traits<char>>(std::__1::basic_ostream<char, std::__1::char_traits<char>>&, char const*, unsigned long) + 0
  [bt] (3) 4   MLCChat                             0x00000001011491b0 tvm::runtime::LoadModuleFromBinary(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&, dmlc::Stream*) + 1308
  [bt] (4) 5   MLCChat                             0x00000001011498fc tvm::runtime::ProcessModuleBlob(char const*, tvm::runtime::ObjectPtr<tvm::runtime::Library>, std::__1::function<tvm::runtime::PackedFunc (int (*)(TVMValue*, int*, int, TVMValue*, int*, void*), tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)>, tvm::runtime::Module*, tvm::runtime::ModuleNode**) + 864
  [bt] (5) 6   MLCChat                             0x000000010114a628 tvm::runtime::CreateModuleFromLibrary(tvm::runtime::ObjectPtr<tvm::runtime::Library>, std::__1::function<tvm::runtime::PackedFunc (int (*)(TVMValue*, int*, int, TVMValue*, int*, void*), tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)>) + 624
  [bt] (6) 7   MLCChat                             0x00000001012174d0 tvm::runtime::SystemLibModuleRegistry::GetOrCreateModule(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>) + 236
  [bt] (7) 8   MLCChat                             0x00000001012171a8 tvm::runtime::PackedFuncObj::Extractor<tvm::runtime::PackedFuncSubObj<tvm::runtime::$_0>>::Call(tvm::runtime::PackedFuncObj const*, tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) + 228
  [bt] (8) 9   MLCChat                             0x00000001010505a0 mlc::llm::serve::FunctionTable::Init(tvm::runtime::String, DLDevice, picojson::object_with_ordered_keys, tvm::runtime::Optional<tvm::runtime::Session>, int, int) + 3096 
```
## Environment

 - Platform: IOS
 - Operating system: MacOS
 - Device: iPhone 16 Pro and My Mac (Designed for iPad) Using a Macbook Pro with M4 pro chip
 - How you installed MLC-LLM (: Conda environment and 
 - 'python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu'

 - How you installed TVM-Unity: pip using:
 `python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu`

 - Python version: 3.11
 - Any other relevant information:
I was able to run the project before (and get responses from the model) using MLCChat and a custom iOS app but I'm not sure why I'm getting it now all of a sudden. 


## 评论 (9)

### dfilimon · 2025-03-25

I'm encountering it too, and the best I can find is that it's likely a recently introduced bug as part of a refactor - I see references to a refactor by @Hzfengsy 

https://github.com/mlc-ai/relax/commit/e7c04f554b81d9f7059269b78b6c645cf43b5540

I believe this is likely involved because the refactor missed a file or two. @Hzfengsy can you help us out here? It seems like the model compilation code needs an update too.

I'd be happy to try and send a pull request if you point me to what to change.

### dfilimon · 2025-03-25

I can confirm that checking out the [parent of that commit](https://github.com/mlc-ai/relax/commit/ec548eb6145171b9cdeb654d96b9e39db1bf771e) works for TVM -

```shell
(mlc-src) ➜  tvm git:(ec548eb61) ✗ git checkout ec548eb
```

But you then also need to adjust your MLC files slightly as I had to also revert changes to [auto_target.py](https://github.com/mlc-ai/mlc-llm/pull/3160/commits/c44c68c0a897554a359674c11d54eebd2158d518) - this is where the `relax.build` argument is renamed from `pipeline` to `relax_pipeline`.

I had to rebuild both TVM and MLC to get it working.

It would probably be better to check out an altogether earlier commit of the MLC root repo, I would [try this one](https://github.com/mlc-ai/mlc-llm/commit/01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c), but I haven't tried it because I need to get a release out.

Hope this helps until the bug is fixed!

### Japp-Galang · 2025-03-28

Thank you for your reply! @dfilimon 

I seem to still be having trouble with your workaround.
I have went into mlc-llm/3rdparty/tvm and used:
`git checkout ec548eb`

And i went into my python packages in my conda environment to update the python file auto_target.py to revert the changes where `relax_pipeline` is used to `pipeline`

I went into /MLCChat and ran `mlc_llm package` and I got the same error. 

I believe the crucial step that i am missing is when you mentioned that you had to rebuild both TVM and MLC. Does this mean that you had to completely uninstall everything and installed everything again and did the changes mentioned above? Or that you built the runtime libraries from source rather than pip installing? Thanks in advance! 

### dfilimon · 2025-03-28

Yes, you need to uninstall and rebuild both from source, but that will happen in the pip step automatically at the end.

For MLC:
- https://llm.mlc.ai/docs/install/mlc_llm.html#option-2-build-from-source

For TVM:
- https://llm.mlc.ai/docs/install/mlc_llm.html#option-2-build-from-source
- I built TVM from under the MLC source tree, building from the 3rdparty/tvm/ folder

If you're starting from scratch again make sure to checkout the mlc repo:
`git clone https://github.com/mlc-ai/mlc-llm/`
And then update all submodules:
`git submodule update --init --recursive`

Finally, when installing the project, use the "Install via pip local project option" in the docs, so:
`pip install -e . --config-settings editable_mode=compat`

The `--config-settings editable_mode=compat` is because there's an update with how pip install work wrt. file setup, so the install script likely needs an update (got a deprecation warning), so to keep the older behavior of `pip install -e .`, I added the extra flag.

Hope it helps!

### qixiaojian310 · 2025-04-03

Have the same error


### littleben803 · 2025-04-12

try to check out this commit：01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c
`git checkout 01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c`
then 
`
git submodule update --init --recursive
mlc_llm package
...

`
I tried it, and it works!

Wish it help~~~~

### jordanqi · 2025-04-18

> try to check out this commit：01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c
> `git checkout 01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c`
> then 
> `
> git submodule update --init --recursive
> mlc_llm package
> ...
> 
> `
> I tried it, and it works!
> 
> Wish it help~~~~


Can you provide the complete step-by-step process? After running git checkout in the mlc-llm directory and redoing convert_weight and generate-config, I encountered an error during the mlc_llm package step.

### FreddyAyala · 2025-05-06

I've tried a fresh configuration, packaging and rebuilt of mlc-llm and used it in IOS, I get: `c++abi: terminating due to uncaught exception of type tvm::runtime::InternalError: [23:06:03] /Users//Documents/GitHub/mlc-llm/3rdparty/tvm/src/runtime/library_module.cc:122: Binary was created using {relax.Executable} but a loader of that name is not registered. Available loaders are relax.VMExecutable, const_loader, static_library, metal. Perhaps you need to recompile with this runtime enabled.
Stack trace:
  [bt] (0) 1   MLCEngineExample.debug.dylib        0x0000000102add15c tvm::runtime::detail::LogFatal::Entry::Finalize() + 100
  [bt] (1) 2   MLCEngineExample.debug.dylib        0x0000000102add0f8 tvm::runtime::detail::LogFatal::Entry::Finalize() + 0
  [bt] (2) 3   MLCEngineExample.debug.dylib        0x0000000102adcb48 std::__1::basic_ostream<char, std::__1::char_traits<char>>& std::__1::__put_character_sequence[abi:ne180100]<char, std::__1::char_traits<char>>(std::__1::basic_ostream<char, std::__1::char_traits<char>>&, char const*, unsigned long) + 0
  [bt] (3) 4   MLCEngineExample.debug.dylib        0x0000000102cf05c8 tvm::runtime::LoadModuleFromBinary(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> const&, dmlc::Stream*) + 1308
  [bt] (4) 5   MLCEngineExample.debug.dylib        0x0000000102cf0d14 tvm::runtime::ProcessModuleBlob(char const*, tvm::runtime::ObjectPtr<tvm::runtime::Library>, std::__1::function<tvm::runtime::PackedFunc (int (*)(TVMValue*, int*, int, TVMValue*, int*, void*), tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)>, tvm::runtime::Module*, tvm::runtime::ModuleNode**) + 864
  [bt] (5) 6   MLCEngineExample.debug.dylib        0x0000000102cf1a9c tvm::runtime::CreateModuleFromLibrary(tvm::runtime::ObjectPtr<tvm::runtime::Library>, std::__1::function<tvm::runtime::PackedFunc (int (*)(TVMValue*, int*, int, TVMValue*, int*, void*), tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)>) + 624
  [bt] (6) 7   MLCEngineExample.debug.dylib        0x0000000102dd90cc tvm::runtime::SystemLibModuleRegistry::GetOrCreateModule(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>) + 236
  [bt] (7) 8   MLCEngineExample.debug.dylib        0x0000000102dd8da4 tvm::runtime::PackedFuncObj::Extractor<tvm::runtime::PackedFuncSubObj<tvm::runtime::$_0>>::Call(tvm::runtime::PackedFuncObj const*, tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) + 228
  [bt] (8) 9   MLCEngineExample.debug.dylib        0x0000000102bd3d14 mlc::llm::serve::FunctionTable::Init(tvm::runtime::String, DLDevice, picojson::object_with_ordered_keys, tvm::runtime::Optional<tvm::runtime::Session>, int, int) + 3096


warning: could not execute support code to read Objective-C class data in the process. This may reduce the quality of type information available.` do you have any step by step guidance to overcome this?

### benliong · 2025-05-17

> try to check out this commit：01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c `git checkout 01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c` then ` git submodule update --init --recursive mlc_llm package ...
> 
> ` I tried it, and it works!
> 
> Wish it help~~~~

With @littleben803 's instructions, I was able to get to a point where the model (Llama-3.2-3B-Instruct-q4f16_1-MLC in my case) loads with "[System] initialize..." on screen.  However, I still get a crash with the following log in Xcode:

```
App is being debugged, do not track this hang
Hang detected: 0.57s (debugger attached, not reporting)
App is being debugged, do not track this hang
Hang detected: 0.80s (debugger attached, not reporting)
libc++abi: terminating due to uncaught exception of type tvm::runtime::InternalError: [15:14:43] /Users/benliong/Projects/mlc-llm/3rdparty/tvm/src/runtime/relax_vm/vm.cc:719: InternalError: Check failed: (func.defined()) is false: Error: Cannot find PackedFunc vm.builtin.paged_attention_kv_cache_create_reduced in either Relax VM kernel library, or in TVM runtime PackedFunc registry, or in global Relax functions of the VM executable
Stack trace:
  [bt] (0) 1   MLCChat                             0x00000001002ab954 tvm::runtime::detail::LogFatal::Entry::Finalize() + 100
  [bt] (1) 2   MLCChat                             0x00000001002ab8f0 tvm::runtime::detail::LogFatal::Entry::Finalize() + 0
  [bt] (2) 3   MLCChat                             0x00000001002ab38c std::__1::basic_ostream<char, std::__1::char_traits<char>>& std::__1::__put_character_sequence[abi:ne190102]<char, std::__1::char_traits<char>>(std::__1::basic_ostream<char, std::__1::char_traits<char>>&, char const*, unsigned long) + 0
  [bt] (3) 4   MLCChat                             0x000000010052f7dc tvm::runtime::relax_vm::VirtualMachineImpl::InitFuncPool() + 1600
  [bt] (4) 5   MLCChat                             0x000000010052efcc tvm::runtime::relax_vm::VirtualMachineImpl::Init(std::__1::vector<DLDevice, std::__1::allocator<DLDevice>> const&, std::__1::vector<tvm::runtime::memory::AllocatorType, std::__1::allocator<tvm::runtime::memory::AllocatorType>> const&) + 1020
  [bt] (5) 6   MLCChat                             0x0000000100533b14 tvm::runtime::relax_vm::VirtualMachineImpl::_Init(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) + 656
  [bt] (6) 7   MLCChat                             0x00000001005364d4 tvm::runtime::PackedFuncObj::Extractor<tvm::runtime::PackedFuncSubObj<tvm::runtime::relax_vm::VirtualMachineImpl::GetFunction(tvm::runtime::String const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::'lambda'(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)>>::Call(tvm::runtime::PackedFuncObj const*, tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) + 52
  [bt] (7) 8   MLCChat                             0x0000000100389be4 mlc::llm::serve::FunctionTable::Init(tvm::runtime::String, DLDevice, picojson::object_with_ordered_keys, tvm::runtime::Optional<tvm::runtime::Session>, int, int) + 6244
  [bt] (8) 9   MLCChat                             0x00000001003a6f94 mlc::llm::serve::ModelImpl::ModelImpl(tvm::runtime::String, tvm::runtime::String, picojson::object_with_ordered_keys, DLDevice, tvm::runtime::Optional<tvm::runtime::Session> const&, int, int, bool) + 560


terminating due to uncaught exception of type tvm::runtime::InternalError: [15:14:43] /Users/benliong/Projects/mlc-llm/3rdparty/tvm/src/runtime/relax_vm/vm.cc:719: InternalError: Check failed: (func.defined()) is false: Error: Cannot find PackedFunc vm.builtin.paged_attention_kv_cache_create_reduced in either Relax VM kernel library, or in TVM runtime PackedFunc registry, or in global Relax functions of the VM executable
Stack trace:
  [bt] (0) 1   MLCChat                             0x00000001002ab954 tvm::runtime::detail::LogFatal::Entry::Finalize() + 100
  [bt] (1) 2   MLCChat                             0x00000001002ab8f0 tvm::runtime::detail::LogFatal::Entry::Finalize() + 0
  [bt] (2) 3   MLCChat                             0x00000001002ab38c std::__1::basic_ostream<char, std::__1::char_traits<char>>& std::__1::__put_character_sequence[abi:ne190102]<char, std::__1::char_traits<char>>(std::__1::basic_ostream<char, std::__1::char_traits<char>>&, char const*, unsigned long) + 0
  [bt] (3) 4   MLCChat                             0x000000010052f7dc tvm::runtime::relax_vm::VirtualMachineImpl::InitFuncPool() + 1600
  [bt] (4) 5   MLCChat                             0x000000010052efcc tvm::runtime::relax_vm::VirtualMachineImpl::Init(std::__1::vector<DLDevice, std::__1::allocator<DLDevice>> const&, std::__1::vector<tvm::runtime::memory::AllocatorType, std::__1::allocator<tvm::runtime::memory::AllocatorType>> const&) + 1020
  [bt] (5) 6   MLCChat                             0x0000000100533b14 tvm::runtime::relax_vm::VirtualMachineImpl::_Init(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) + 656
  [bt] (6) 7   MLCChat                             0x00000001005364d4 tvm::runtime::PackedFuncObj::Extractor<tvm::runtime::PackedFuncSubObj<tvm::runtime::relax_vm::VirtualMachineImpl::GetFunction(tvm::runtime::String const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::'lambda'(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)>>::Call(tvm::runtime::PackedFuncObj const*, tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) + 52
  [bt] (7) 8   MLCChat                             0x0000000100389be4 mlc::llm::serve::FunctionTable::Init(tvm::runtime::String, DLDevice, picojson::object_with_ordered_keys, tvm::runtime::Optional<tvm::runtime::Session>, int, int) + 6244
  [bt] (8) 9   MLCChat                             0x00000001003a6f94 mlc::llm::serve::ModelImpl::ModelImpl(tvm::runtime::String, tvm::runtime::String, picojson::object_with_ordered_keys, DLDevice, tvm::runtime::Optional<tvm::runtime::Session> const&, int, int, bool) + 560
```

The main point was that using `01c43c73b1146b433c7ff80df77b6b2e0fcb1a6c` is successful in getting relax.Executable to work, but  PackedFunc vm.builtin.paged_attention_kv_cache_create_reduced is still unavailable via TVM that was pinned with that commit. 
