# [Issue #618] [Question] Can we build a Mac or Universal version of the iOS app?

source: https://github.com/mlc-ai/mlc-llm/issues/618
state: closed | updated: 2026-03-01T20:43:48Z
labels: question

## 正文

## ❓ General Questions

Thank you so much for this amazing project -- it's a complete game-changer when it comes to running LLM locally. I'd like to make this available to my non-technical colleagues as a standalone Mac app. I can already install the iPad version,  but it would be great to have a "proper" Mac app. 

I've tried to edit the Xcode project to add Mac Catalyst as a target, but I get errors to do with the wrong architecture
```
Build failed because libmlc_llm.a, libmodel_iphone.a, libsentencepiece.a, libtokenizers_c.a, libtokenizers_cpp.a and libtvm_runtime.a are missing a required architecture. Would you like to build for Rosetta instead?
```
I think the correct archs are `aarch64-apple-ios-macabi` and `x86_64-apple-ios-macabi`, and I can use them by updating the `prepare_libs` script
```
cargo +nightly build -Z build-std --release --target aarch64-apple-ios-macabi
cargo +nightly build -Z build-std --release --target x86_64-apple-ios-macabi
```

However, that doesn't seem to fix the Xcode issue, so I'm a bit stuck. I'd be very grateful for an tips :) 

## 评论 (20)

### tqchen · 2023-07-29

To build an macapp, likely an update on https://github.com/mlc-ai/mlc-llm/blob/main/ios/prepare_libs.sh is needed. The swift UI also need some update, if you manage to do it, we love a PR

### elepedus · 2023-08-01

So I've been trying to re-purpose the iOS app for Mac, and while I feel like I'm tantalisingly close, I still can't quite get it to work.

The main approach I've taken is converting to a Mac Catalyst app. This required modifications to `prepare_libs.sh`, and I had to use [iOS CMake](https://github.com/leetal/ios-cmake) to get multi-arch builds
```bash
function help {
    echo -e "OPTION:"
    echo -e "  -s, --simulator                      Build for Simulator"
    echo -e "  -a, --arch        x86_64 | arm64     Simulator arch "
    echo -e "  -h,  --help                          Prints this help\n"
}

is_simulator="false"
arch="arm64"

# Args while-loop
while [ "$1" != "" ];
do
   case $1 in
   -s  | --simulator  )   is_simulator="true"
                          ;;
   -a  | --arch  )        shift
                          arch=$1
                          ;;
   -h   | --help )        help
                          exit
                          ;;
   *)
                          echo "$script: illegal option $1"
                          usage
						                  exit 1 # error
                          ;;
    esac
    shift
done

set -euxo pipefail

sysroot="MacOSX"
type="Release"

if [ "$is_simulator" = "true" ]; then
  if [ "$arch" = "arm64" ]; then
    # iOS simulator on Apple processors
    rustup target add aarch64-apple-ios-sim
  else
    # iOS simulator on x86 processors
    rustup target add x86_64-apple-ios
  fi
  sysroot="iphonesimulator"
  type="Debug"
else
  # MacOS devices
  cargo +nightly build -Z build-std --release --target aarch64-apple-ios-macabi
  cargo +nightly build -Z build-std --release --target x86_64-apple-ios-macabi
fi

mkdir -p build/ && cd build/

cmake ../.. -DCMAKE_TOOLCHAIN_FILE=../../../ios-cmake/ios.toolchain.cmake -DPLATFORM=MAC_CATALYST_ARM64 \
  -DCMAKE_BUILD_TYPE=$type\
  -DCMAKE_OSX_ARCHITECTURES="x86_64;arm64;"\
  -DDEPLOYMENT_TARGET=14.0\
  -DCMAKE_BUILD_WITH_INSTALL_NAME_DIR=ON\
  -DCMAKE_SKIP_INSTALL_ALL_DEPENDENCY=ON\
  -DCMAKE_INSTALL_PREFIX=.\
  -DCMAKE_CXX_FLAGS="-O3"\
  -DMLC_LLM_INSTALL_STATIC_LIB=ON\
  -DUSE_METAL=ON
make mlc_llm_static
cmake --build . --target install --config release -j
cd ..

rm -rf MLCSwift/tvm_home
ln -s ../../3rdparty/tvm MLCSwift/tvm_home

python prepare_model_lib.py
```

However, I still get the following error:
```
In [...]/mlc-ai/ios/build/lib/libmodel_iphone.a(Llama_2_7b_chat_hf_q3f16_1_devc.o), building for Mac Catalyst, but linking in object file built for , file '[...]/mlc-ai/ios/build/lib/libmodel_iphone.a' for architecture arm64
```
I've also tried converting the entire app to a standalone Mac app, but unfortunately the `MLCSwift` library uses UIKit, which is not available for Mac.

I'm not a Swift developer, so I'm kinda stumbling around in the dark trying to get this to work, but I would appreciate any suggestions :) 

### tqchen · 2023-08-02

I would avoid multiarch build, mainly because the the .o file that we build have a specific target string https://github.com/mlc-ai/mlc-llm/blob/main/mlc_llm/utils.py#L435 which should work for M1(arch64) but not for x86.

For now, going with the iPad app for Macbook might be the easiest option

### jparismorgan · 2023-08-02

I have also been working on this because I am interested in building a react-native project that works on OSX. I currently have been able to 
1) Build mac x86 static libs based off of these steps: https://mlc.ai/mlc-llm/docs/deploy/cli.html
```
~/repo/mlc-llm-paris/osx ls build/lib
libmlc_llm.a        libsentencepiece.a  libtokenizers_c.a   libtokenizers_cpp.a libtvm_runtime.a
```
2) Add a new osx target to the existing iOS project.

<img width="991" alt="Screenshot 2023-08-01 at 11 21 01 PM" src="https://github.com/mlc-ai/mlc-llm/assets/1396242/9bb28048-35a7-49ef-8200-93baa0b03eb4">

3) Build this new OSX target and see the app open on OSX.

<img width="1057" alt="Screenshot 2023-08-01 at 11 20 00 PM" src="https://github.com/mlc-ai/mlc-llm/assets/1396242/404489a5-639c-46e1-9793-07e898243882">

4) Click on a model to chat, but then I get a crash.

You can see my code here: https://github.com/jparismorgan/mlc-llm/pull/1 - check the `osx/README.md` for how to build it. The crash I am getting is `TVM runtime cannot find vm_load_executable`:
```
libc++abi: terminating with uncaught exception of type tvm::runtime::InternalError: [23:14:37] /Users/parismorgan/repo/mlc-llm/cpp/llm_chat.cc:244: InternalError: Check failed: (fload_exec.defined()) is false: TVM runtime cannot find vm_load_executable
Stack trace:
  [bt] (0) 1   MLCChat-macos                       0x0000000100fea528 tvm::runtime::Backtrace() + 24
  [bt] (1) 2   MLCChat-macos                       0x0000000100f9560d tvm::runtime::detail::LogFatal::Entry::Finalize() + 77
  [bt] (2) 3   MLCChat-macos                       0x0000000100f955b9 tvm::runtime::detail::LogFatal::~LogFatal() + 25
  [bt] (3) 4   MLCChat-macos                       0x0000000100f94559 tvm::runtime::detail::LogFatal::~LogFatal() + 9
  [bt] (4) 5   MLCChat-macos                       0x0000000100fa7dd5 mlc::llm::LLMChat::Reload(tvm::runtime::Module, tvm::runtime::String, tvm::runtime::String) + 6005
  [bt] (5) 6   MLCChat-macos                       0x0000000100fa6378 mlc::llm::LLMChatModule::GetFunction(tvm::runtime::String const&, tvm::runtime::ObjectPtr<tvm::runtime::Object> const&)::'lambda'(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*)::operator()(tvm::runtime::TVMArgs, tvm::runtime::TVMRetValue*) const + 536
  [bt] (6) 7   MLCChat-macos                       0x0000000100f85adf tvm::runtime::TVMRetValue tvm::runtime::PackedFunc::operator()<tvm::runtime::Module&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&>(tvm::runtime::Module&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >&) const + 351
  [bt] (7) 8   MLCChat-macos                       0x0000000100f854fa -[ChatModule reload:modelPath:appConfigJson:] + 570
  [bt] (8) 9   MLCChat-macos                       0x0000000100f4c818 $s13MLCChat_macos9ChatStateC010mainReloadC033_2124E0952CFB3CB7802CDB9B1453057DLL7localId8modelLib0N4Path16estimatedVRAMReq11displayNameySS_S2Ss5Int64VSStFyycfU_ + 6120
```

I'm not quite stuck, but if anyone would like to take a look, I don't think we are too far from getting this working! If we are able to get the inference part working then I am planning to rewrite the app as a new xcode project so we don't need to have all the commented out things.


### elepedus · 2023-08-02

@tqchen I have considered that, but it appears the iPad version can only be installed from the App Store? We would really like to be able to create a standalone executable for internal distribution, without having to go through the App Store.

@jparismorgan I had this very same problem. IIRC, I had missed the bit in the documentation which told us to install TVM Unity. I think I fixed it by following the steps at https://mlc.ai/mlc-llm/docs/install/tvm.html
<img width="870" alt="Screenshot 2023-08-02 at 08 59 54" src="https://github.com/mlc-ai/mlc-llm/assets/4815651/8eb84a6d-4015-4fca-bd6c-cb04b0671f67">


### elepedus · 2023-08-02

@tqchen If I were to update the linked script (https://github.com/mlc-ai/mlc-llm/blob/main/mlc_llm/utils.py#L435) to support Mac architecture, what else would I need to do to actually create a mac-compatible model?

### tqchen · 2023-08-02

I think the main issue would be multi arch. If we build the app for either apple silicon or x86 I think updating the flag should work. 

So atm we will need to build the app for each platform here 

### tqchen · 2023-08-02

Aka if we set the right target and say build an app only for apple silicon MacOS. 

I think the main thing would be to update the mlc related build part to producer the compatible lib for that specific target

### dylanbeadle · 2023-08-04

@jparismorgan I don't see `libmodel_iphone.a` in your list of mac x86 static libs. I believe this library is build by `prepare_model_lib.py`. Could this be the cause of `TVM runtime cannot find vm_load_executable` ?

### elepedus · 2023-08-04

@tqchen Sorry for the slow reply, I've had to move this into my pet projects time. I'm looking at the utils script and wondering if I can just pass `target=metal` or `target=metal_x86_64` to hit e.g https://github.com/mlc-ai/mlc-llm/blob/main/mlc_llm/utils.py#L378 

Would that not produce the correct arch? Do I just follow the instructions at https://mlc.ai/mlc-llm/docs/compilation/compile_models.html to try it out?

### elepedus · 2023-08-04

Ok, so I've been trying to set up my environment for compilation, but there's something wrong with TVM. 

These are the steps I've followed:
```
# Clone repo
git clone git@github.com:mlc-ai/mlc-llm.git --recursive
```
``` 
# Set up environment 
conda create -n mlc-chat-venv -c mlc-ai -c conda-forge mlc-chat-nightly
conda activate mlc-chat-venv
python3 -m mlc_llm.build --help
>> ModuleNotFoundError: No module named 'torch'
```

```
# Install pytorch
conda install pytorch -c pytorch
python3 -m mlc_llm.build --help
>> ModuleNotFoundError: No module named 'tvm'
```

```
# install tvm
conda install -c conda-forge tvm-py
>> package tvm-py-0.8.0-py310h4e15889_4_cpu requires python >=3.10,<3.11.0a0 *_cpython, but none of the providers can be installed
```

```
# downgrade to python 3.10
conda install python 3.10
conda install -c conda-forge tvm-py
python3 -m mlc_llm.build --help
>> AttributeError: module 'tvm.script.tir' has no attribute 'Buffer'
```
Any ideas where I'm going wrong?

### tqchen · 2023-08-04

We depend on tvm unity (the latest developments), please checkout instructions here https://mlc.ai/mlc-llm/docs/install/tvm.html

### elepedus · 2023-08-04

Yeah, I followed these instructions, but they don't seem to work. 
<img width="836" alt="Screenshot 2023-08-04 at 16 42 04" src="https://github.com/mlc-ai/mlc-llm/assets/4815651/55d25fd7-f363-4d82-a1b9-a0cd1d85f8a3">
<img width="1225" alt="Screenshot 2023-08-04 at 16 42 12" src="https://github.com/mlc-ai/mlc-llm/assets/4815651/b326761f-8942-4205-90a7-2c96b97cfd05">
I'm currently following the "Build from source" instructions and will report back :) 

### tqchen · 2023-08-04

Can you provide more details about the apple silicon prebuild and what does not work? Would love to help digging into it

### elepedus · 2023-08-04

So the prebuilt models are working great. I can use them with the CLI running on my Mac, and I can use the iPhone version with the sample iOS app, using "Designed for iPad". 

However, what I really need is to build a single, standalone  internal Mac app so less determined people in my organisation can easily experience LLMs without having to install python, conda, TVM etc. As far as I can tell, "Designed for iPad" can only be installed through the App Store, so I'm trying to convert the demo iOS app into a Mac Catalyst app. I've managed to rebuild everything else for the correct architecture, except for `libmodel_iphone.a`, so I get the error
```
building for Mac Catalyst, but linking in object file built for , file '[...]/mlc-ai/ios/build/lib/libmodel_iphone.a' for architecture arm64
```

Based on your earlier advice, I understand that I should rebuild my ML model with a different architecture, so I'm setting up my machine to compile models.

I've now managed to build TVM from source and used `export PYTHONPATH=/Users/elepedus/Developer/work/tvm-unity/python/:$PYTHONPATH`, but when I try to run `python3 -m mlc_llm.build --help`, I always get a missing dependency eg `numpy`,`scipy`, `psutil`, `typing_extensions`,`attr`, `pytorch` etc

I never thought I'd miss NPM's `package.json` 😓 


### elepedus · 2023-08-04

After installing all the missing modules, I get a new error:
```
python3 -m mlc_llm.build --hf-path togethercomputer/RedPajama-INCITE-Chat-3B-v1 --target metal --quantization q4f16_1
Weights exist at dist/models/RedPajama-INCITE-Chat-3B-v1, skipping download.
Using path "dist/models/RedPajama-INCITE-Chat-3B-v1" for model "RedPajama-INCITE-Chat-3B-v1"
Database paths: ['log_db/rwkv-raven-3b', 'log_db/redpajama-3b-q4f16', 'log_db/redpajama-3b-q4f32', 'log_db/rwkv-raven-1b5', 'log_db/dolly-v2-3b', 'log_db/rwkv-raven-7b', 'log_db/vicuna-v1-7b']
[17:03:55] /Users/elepedus/Developer/work/tvm-unity/src/runtime/metal/metal_device_api.mm:167: Intializing Metal device 0, name=Apple M2 Max
Host CPU dection:
  Target triple: arm64-apple-darwin22.5.0
  Process triple: arm64-apple-darwin22.5.0
  Host CPU: apple-m1
Target configured: metal -keys=metal,gpu -max_function_args=31 -max_num_threads=256 -max_shared_memory_per_block=32768 -max_threads_per_block=1024 -thread_warp_size=32
Traceback (most recent call last):
  File "/Users/elepedus/miniconda3/envs/mlc-chat-venv-src/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Users/elepedus/miniconda3/envs/mlc-chat-venv-src/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/Users/elepedus/Developer/work/mlc-llm-src/mlc_llm/build.py", line 13, in <module>
    main()
  File "/Users/elepedus/Developer/work/mlc-llm-src/mlc_llm/build.py", line 10, in main
    core.build_model_from_args(parsed_args)
  File "/Users/elepedus/Developer/work/mlc-llm-src/mlc_llm/core.py", line 471, in build_model_from_args
    mod, param_manager, params = gpt_neox.get_model(args, config)
  File "/Users/elepedus/Developer/work/mlc-llm-src/mlc_llm/relax_model/gpt_neox.py", line 787, in get_model
    param_manager.set_param_loading_func(
  File "/Users/elepedus/Developer/work/mlc-llm-src/mlc_llm/relax_model/param_manager.py", line 331, in set_param_loading_func
    self.torch_pname2binname = load_torch_pname2binname_map(
  File "/Users/elepedus/Developer/work/mlc-llm-src/mlc_llm/relax_model/param_manager.py", line 834, in load_torch_pname2binname_map
    assert os.path.isfile(single_shard_path)
AssertionError
```

### elepedus · 2023-08-05

Looks like the error above is caused by the script not downloading the model correctly when passing the `--hf-path togethercomputer/RedPajama-INCITE-Chat-3B-v1` param. The cloned repository only contains a few json files (perhaps it's not doing `git lfs clone`?)  Either way, if I manually clone the repo with all the correct files in it, then I'm able to build the model and use it from the CLI. 

Next, I will try to compile the model for different archs and see if I can get XCode to build the Mac Catalyst app with it.

### bryan1anderson · 2024-09-26

@elepedus did you get any further than this?

### elepedus · 2024-10-14

Nope, sorry -- ended up using & recommending LM Studio, which is based on `llama.cpp`. Although it recently added support for alternative backends (e.g MLX), so it might be possible to get an MLC backend as well...

### marcoleder · 2025-01-07

I would deeply support adding MLC backend to LM-Studio, are there any plans regarding this?
