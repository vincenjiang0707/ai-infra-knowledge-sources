# Changelog (aggregated from releases.body)

> releases: 32

## v0.2 (2018-01-31)

NOTE: This is a release pre apache incubation

This release comes with a complete set of TOPI support for NNVM compiler, which allows compilation of end to end workloads. We also make major improvements in supporting new backends: ROCm for AMDGPUs and ARM GPU. Check out [previous blogs](http://tvmlang.org/) that describes these major improvements in detail!

- Backend support
   - Support LLVM mainline(4.0, 5.0, 6.0)
   - Support ROCM stack for AMD GPUs
   - More robust OpenCL support for ARM GPUs
- Android RPC runtime
- Multi-threading optimization for ARM
   - multi-threaded depthwise
   - multi-threaded conv2d
- New schedule primitives
   - storage_align for shared memory alignment
   - double_buffer
- UnrollLoop : more robust version of unroll loop, count maximum steps that can be unrolled.
- Full set of TOPI operators
   - Introduce tvm.target to specify target options for compilation better.
   - broadcast/ reduction operators
   - pooling and global pooling
   - Generic target support for topi
   - schedule with external libraries
- End to end deep learning pipelines for CPU, GPU, ARM GPU
- Tutorials
  - How to load compiled module in any language runtime
  -  How to use java runtime
- Contrib library: MIOpen, CuDNN
- Ongoing items that contains functioning pieces
  - WebGL backend
  - C++ compiler support
  - MPS DNN
  - low bit support, introduced popcount


## v0.3 (2018-09-03)

NOTE: This is a release pre apache incubation

This release features numerous improvements in TOPI and backends. We make the first step toward object detection support in TOPI, featuring operators necessary for YOLO and SSDs. The topi now supports numpy-style API and operator overloading. RPC is significantly improved to support resource allocation and using a pool of devices. We are adding two new backends: WebGL for running GPUs on the browser, and Vulkan for running on next-generation graphics API. Please also check out [tvm blogs](http://tvmlang.org/)  for latest blogposts


## Change List 
- TOPI Vision operators
   - SSD support
   - YOLO support
   - NMS operator support in vision
- TOPI general numpy-style operators
   - numpy style operator overload in topi
   - more operators: flip, take
   - dilation support on conv2d and depthwise
- 8bit support
    - ARM 8bit gemm
    - ARM 8bit conv
- Low bit operator support
    - popcount intrinsics
    - 1-bit fully connected
- Contrib: MPSDNN fully-connected and conv2d support
- Better RPC support
   - RPC Tracker support to allow centralized resource management
   - RPC protocol upgrade (this is a non-backward compatible change) to support timeout in the proxy
     - This is a breaking change, need to use the latest version of TVM runtime with the RPC
   - Fault-tolerant to early server termination with correct exception propagated
   - RPC support enabled for ROCm AMDGPUs
- Tutorials and docs
  - How to deploy to android devices.
- Optimizations for hardware backends
  - intel CPU (AVX and AVX512)
- Schedule Primitives
   - rfactor now support factor_axis to specify the factored dimension in the result
   - cache_write now support multiple output operators
   - enable warp memory which generates shuffle instructions
- Framework bridge
  - MXNet bridge supported
- C++ compiler API support
   - build migration
   - topi migration to c++
   - Target system in c++
- WebGL backend
   - runtime and codegen
   - topi integration
   - end to end pipeline on the browser
- Vulkan backend
   - vulkan runtime
   - spirv code generator
- Security
    - intel SGX runtime support
    - multi-threaded SGX runtime
- LLVM 7.0 support
- Robustness
   - VerifyMemory to verify incorrect GPU schedules that writes into GPU memory from cpu
   - Verify compute formulas
- Better CPU parallel runtime


##  Main Contributors 

See [complete list here](https://github.com/dmlc/tvm/graphs/contributors?from=2018-02-01&to=2018-05-20&type=c). Thanks to all the contributors to contribute to this release.

 Code Reviewers
- @zhreshold for reviewing many vision ops
- @Huyuwei topi operators
- @sxjscience for reviewing topi operators

TOPI:
- @merrymercy Mali GPU support
- @PariksheetPinjari909 topi vision ops, support for darknet operators 
- @yzhliu intel CPU optimization
- @kevinthesun Vision operators, initial ssd, nms operator support
- @dingobye Various great TOPI improvements for operator overloading
- @Huyuwei dilation support to conv
- @masahi Intel CPU topi
- @nishi-t  improvements in pooling 

Compiler:
- @nhynes SGX support
- @phisiart WebGL backend
- @alex-weaver C++ compiler support
- @kun-zh bug fix bound checking in code.
- @xqdan improvement low-level schedule rewrite.
- @yidawang parallel runtime improvement
- @eqy AMD GPU backend improvements
- @Laurawly Initial improvements for Intel GPU
- @cnuernber Improved runtime device stream API



## v0.4 (2018-09-03)

NOTE: This is a release pre apache incubation

This release features several major improvements. The high-level graph optimizer is now part of TVM repo. Some of the highlights are: Initial support of AutoTVM for automated optimization; customized accelerator backend VTA. Please also check out [tvm.ai](https://tvm.ai) for latest blogposts.


The community welcomes new reviewers @kazum @alex-weaver @masahi @zhreshold @PariksheetPinjari909 @srkreddy1238 @eqy, new code owner @merrymercy,  and new committer @yzhliu 
 
## Change List
### Tensor Expression and Optimization
- Tensor operator primitives
  - Introduce attrs field to operator primitives(e.g. compute) to store additional metadata, the attrs can be used as hint for scheduling
- Enable embedding of asm micro-kernels 
- Hybrid python programming model
   - python AST based IR builder interface
   - support GPU programs
- AutoTVM, Automated tuning, and scheduling
   - basic autotvm infra
    - GPU IR verifier
   - basic autotuning tutorial
   - topi integration 
- ARM support
    - winograd support
   - initial support of ARM autotuning records
- TOPI Vision
   - Generic GPU sort support(useful for vision)
   - SSD operator support
- TOPI numpy consistency
   - Rename all binary operators for numpy consistecy: broadcast_add-> add, broadcast_sub -> substract, broadcast_mul -> multiply, broadcast_div->divide
   - New operators: slice, LRN, equal, not_equal, less, greater
   - tutorials on topi
- Initial low-bit operator support support 
    - Optimized popcount generation on ARM
    - general bit-serial convolution and GEMM
    - optimized low bit kernels
    - parallel optimization
- New topi backend optimization for intel graphics
- Adapt AVX schedules for SSE target

### Backend 
- VTA: customized accelerator backend
  - custom hardware backend example
  - tutorials on how to use customized accelerator
- Initial experimental support for  HLS backend
- Bugfix in SPIRV code generator for vulkan
- libdevice support, enable NVPTX backend

### Runtime
- Introduce NDArrayContainer for managed NDarray
- RPC and Device API
   - Support communication between big/small endian machines.
   - RPC and device API protocol upgrade (this is a non-backward compatible change) to support big-small endian communication. This is a non-backward compatible change, need to use the latest version of TVM runtime with the RPC
   - graduate rpc from contrib, tvm.contrib.rpc->tvm.rpc
   -Support tracker in Android RPC, add fault tolerance for AutoTVM
- BIG.LITTLE aware threadpool
- tvm4j graph runtime that runs end to end workload in java
- DLPack support
   - Support from_dlpack and to_dlpack
   - Enables bridges to pytorch
- Enable link of stackvm in runtime 

### NNVM
- Tensorflow graphdef frontend
- Keras frontend
   - improved to support reuse layers, add activations
- ONNX
   - gather,  LRN
- CoreML frontend
   - Support C-RNN and activation functions
- Fix grads for sum and expand_like
- Enhanced operator fusion for multiple elemwise branches
- Separate nnvm fusion and compilation pass

### Misc
- Unified build system to cmake, customizable cmake path for vulkan, rocm, cuda

##  Contributors 
See the [complete list here](https://github.com/dmlc/tvm/graphs/contributors?from=2018-05-20&to=2018-08-13&type=c). Thanks to all the contributors to contribute to this release.

Code reviewers
- @yzhliu topi, tvm4j, nnvm
- @kevinthesun nnvm
- @Huyuwei topi operators
- @tmoreau89  hardware backends
- @comaniac  fpga backends
- @kazum nnvm, opencl backend, fpga
- @nishi-t nnvm, opencl backend
- @merrymercy topi, arm, 
- @vinx13 gpu backend
- @masahi nnvm, topi
- @eqy autotvm
- @jroesch  runtime
- @PariksheetPinjari909 frontends, topi
- @srkreddy1238 frontends, topi 
- @FrozenGene autotvm

Compiler
- @alex-weaver vulkan 
- @were hybrid script mode
- @nishi-t CUDA, fp16, int8 support
- @ktabata intel FPGA support
- @kazum xilinx fpga support
- @cowanmeg arm optimized popcount
- @tmoreau89 VTA customized accelerator

TOPI, graph optimization
- @merrymercy AutoTVM
- @yzhliu tvm4j graph runtime, x86
- @Laurawly intel graphics
- @abergeron conda build fix
- @nhynes sgx random
- @masahi topi, more robust op fusion
- @kevinthesun vision ops
- @grwlf argmax/min ops
- @cowanmeg bit-serial operator
- @ehsanmok topi tutorial
- @zhiics refactor fusion and compilation into separate pass
- @liangfu binary logical operators

Frontends
- @srkreddy1238 tutorials for deployment, tensorflow frontend
- @siju-samuel coreml, tf frontend
- @PariksheetPinjari909 nnvm, slice
- @kazum keras
- @nishi-t  mxnet, nnvm

Deploy
- @eqy rpc, thread runtime
- @dayanandasiet android tutorials



## v0.5 (2019-02-18)

NOTE: This is a release pre apache incubation

This release features several major improvements. Some of the highlights are: Arbitrary bits quantization algorithm; High-level auto-differentiable programming IR--Relay(NNVMv2). 

The community welcomes new reviewers @nishi-t @were @siju-samuel @jroesch @xqdan @zhiics  @grwlf @ajtulloch @vinx13 @junrushao1994 @FrozenGene @liangfu , new committers @srkreddy1238 @eqy @masahi @nhynes @phisiart @merrymercy @Laurawly @adityaatluri  @Huyuwei 

# Change List
- Fully featured 8-bit network support
  - 8bit quantizer
  - Arbitrary bits quantization algorithm
  - Intel cpu support
- NVidia GPU 8-bit kernel
  - int8 gemm recipe
  - int8 conv2d
  - Autotvm integration
- Automated tuning and scheduling
  - AutoTVM optimizations for mobile GPUs
  - AutoTVM optimizations for CUDA
  - AutoTVM optimizations for x86
- Initial release of the differentiable programming IR, Relay
  - Generic & informative Relay error reporting #2408 
  - Relay IR text format support #1781 
  - Support control flows
  - A Normal Form Canonicalization #2251 
  - Type system support
  - End to end compilation
     * Frontend support: Caffe2 #2507 , CoreML #2476 , Keras #2376 , MXNet #2163 , ONNX, TFLite #2365 
     * Operator coverage #1799 #2051 
  - FoldScaleAxis #2020 
  - SimplifyInference #2033 
  - CombineParallelConv2D #2089
  - InstrumentBoundCheckers pass #2079 
  - Bind & FoldConstant #2100
  - Alter Op Layout #2150
  - General OpFusion #2090
- CodeGen
  - Gcc / g++ compatible C code generator for TVM #2161 
  - Device type annotation for heterogeneous compilation #2361 
  - Cache packed func ptr, lift alloca #2070 
  - Generalize compute to tensor region #1476 
- Runtime
  - Relay interpreter and compiler #1954 
  - Heterogeneous runtime #1695 
  - Language bindings: Golang runtime #1470 , Rust runtime #1597 
  - Add min_repeat_ms to time_evaluator #2200 
  - Bundled interpreter demonstration #2297 
  - Enable PlanMemory in the graph runtime #2120
- Language Binding
  - Rust frontend #2292 
- VTA
  - Improved RPC for VTA #2043
- Hybrid python programming model
  - Support for scheduling #2416 
  - Support for Inter-function call  #2287 
  - Backend support  https://github.com/dmlc/tvm/pull/2477 
- TOP
  - Initial support for sparse tensor computation
  - Improve ARM CPU depthwise convolution performance #2345 
  - Port winograd ops to relay #2356 
- Tutorials and docs
  - Relay language docs #2232 
  - Tutorials on how to use SGX backend
  - How to write a pass in python
  - General lowering flow of TVM
  - How to do tensorize
  - TFLite frontend tutorial #2508 
  - Keras seq2seq model for translation tutorial #1815 
  - Committer guide and tips #2468
  - Code review guideline on API designs #2459 

## Contributors

Code reviewers
- @tqchen 
- @liangfu quantization, relay, topi, frontend
- @zhiics relay, runtime, frontend
- @nhynes quantization, rust
- @Huyuwei frontend
- @yzhliu relay, frontend, perf
- @xqdan hybrid script, tvm/lang
- @ZihengJiang relay
- @vinx13 relay/pass, topi
- @masahi relay/pass, frontend, doc, topi
- @grwlf frontend, topi, relay, quantization
- @tmoreau89 vta, relay, backend, runtime
- @kazum frontend
- @nishi-t frontend, topi
- @PariksheetPinjari909 frontend
- @jroesch  relay, frontend, doc
- @srkreddy1238 relay/op, frontend
- @siju-samuel relay/op, frontend
- @junrushao1994 relay
- @icemelon9 relay, perf, tvm/lang, codegen
- @ajtulloch relay, frontend
- @alex-weaver relay
- @kevinthesun hybrid script, topi, relay
- @Laurawly topi
- @were hybrid script, topi
- @FrozenGene frontend, topi, relay/pass
- @eqy relay, topi, runtime, rust
- @zhreshold frontend, relay/op
- @merrymercy relay/op, topi, runtime, frontend
- @derisavi-huawei symbolic integers

Code contributions
- @tqchen tvm
- @vinx13 relay/pass, topi
- @siju-samuel topi, relay/op
- @merrymercy autotvm, topi, relay/pass
- @srkreddy1238 relay/op, frontend/tf
- @MarisaKirisame relay
- @slyubomirsky relay, docs
- @jroesch relay
- @nhynes rust
- @wweic docs, relay/pass
- @yzhliu perf, frontend
- @zhiics relay/pass, relay/op, runtime
- @were hybrid script
- @icemelon9 perf, relay/pass, relay/op
- @joshpoll relay, docs
- @sgrechanik-h codegen
- @kazum frontend/keras, topi
- @masahi relay/op, docs
- @FrozenGene perf, frontend/tf
- @liangdzou docs
- @junrushao1994 relay/op
- @eqy autotvm, runtime
- @apivovarov docs
- @ajtulloch runtime, nnpack
- @kevinthesun relay/op, perf
- @ZihengJiang relay/pass, quantization
- @hlu1 nnpack, frontend/caffe2
- @lixiaoquan nnvm
- @imorinaga frontend/mxnet
- @liangfu topi, docs
- @xqdan codegen
- @PariksheetPinjari909 frontend/darknet
- @alexeyr frontend/tensorflow
- @Rasterer topi
- @yangchen-MS codegen
- @anijain2305 relay/op
- @grwlf topi
- @Huyuwei topi, frontend/keras
- @denis0x0D runtime/trace, relay/pass
- @Mutinifni codegen
- @derisavi relay/pass
- @tmoreau89 vta
- @Laurawly topi, perf
- @zhreshold frontend, topi
- @kun-zh codegen
- @reminisce relay/op
- @ehsanmok  rust
- @cnuernber   perf
- @cowanmeg  topi, codegen
- @yuruofeifei  topi

## v0.6.0 (2019-12-05)

Apache TVM (incubating) is an effort undergoing incubation at The Apache Software Foundation (ASF), sponsored by the Apache Incubator PMC.

Incubation is required of all newly accepted projects until a further review indicates that the infrastructure, communications, and decision making process have stabilized in a manner consistent with other successful ASF projects.

While incubation status is not necessarily a reflection of the completeness or stability of the code, it does indicate that the project has yet to be fully endorsed by the ASF.

# New Features

### Relay in Production
Relay is a functional, differentiable programming language designed to be an expressive intermediate representation for machine learning systems. Relay supports algebraic data types, closures, control flow, and recursion, allowing it to directly represent more complex models than computation graph-based IRs (e.g., NNVM) can. In TVM v0.6, Relay is in stable phase and is ready for production.

* Algebraic Data Types (ADT) support ([#2442](https://github.com/apache/incubator-tvm/pull/2442), [#2575](https://github.com/apache/incubator-tvm/pull/2575)). ADT provides an expressive, efficient, and safe way to realize recursive computation (e.g., RNN). Refer to https://docs.tvm.ai/langref/relay_adt.html for more information.
* Pass manager for Relay ([#2546](https://github.com/apache/incubator-tvm/pull/2546), [#3226](https://github.com/apache/incubator-tvm/pull/3226), [#3234](https://github.com/apache/incubator-tvm/pull/3234), [#3191](https://github.com/apache/incubator-tvm/pull/3191))
* Most frameworks have been supported in Relay, including ONNX, Keras, Tensorflow, Caffe2, CoreML, NNVMv1, MXNet ([#2246](https://github.com/apache/incubator-tvm/issues/2246)).
* Explicitly manifest memory and tensor allocations in Relay. ([#3560](https://github.com/apache/incubator-tvm/pull/3560))

### Relay Virtual Machine
The Relay Virtual Machine (Relay VM) is the new generation of runtime to strike a balance between performance and flexibility when deploying and executing Relay programs. Previously, the graph runtime is able to utilize the fully static nature of the input graphs to perform aggressive optimization such as fully static allocation, and optimal memory reuse. When we introduce models which make use of control-flow, recursion, dynamic shapes, dynamic allocation we must change how execution works.

Relay VM is now usable and is able to achieve decent performance for a various of models and targets.

* Design ([#2810](https://github.com/apache/incubator-tvm/pull/2810) [#2915](https://github.com/apache/incubator-tvm/pull/2915)) and a first version of implementation ([#2889](https://github.com/apache/incubator-tvm/pull/2889)),
* Add VM runtime for Relay and compiler support ([#3120](https://github.com/apache/incubator-tvm/pull/3120), [#3121](https://github.com/apache/incubator-tvm/pull/3121), [#2889](https://github.com/apache/incubator-tvm/pull/2889), [#3139](https://github.com/apache/incubator-tvm/pull/3139))
* Relay VM (pattern matching [#3470](https://github.com/apache/incubator-tvm/pull/3470), port to python [#3391](https://github.com/apache/incubator-tvm/pull/3391), serialization [#3647](https://github.com/apache/incubator-tvm/pull/3647))
* Relay VM Profiler ([#3727](https://github.com/apache/incubator-tvm/pull/3727))
* Support execution on devices for Relay VM ([#3678](https://github.com/apache/incubator-tvm/pull/3678))
* [Relay][VM] Add more passes to VMCompiler ([#4058](https://github.com/apache/incubator-tvm/pull/4058))
* [relay][vm] Separate VM runtime with executable ([#4100](https://github.com/apache/incubator-tvm/pull/4100))
* Port VM, VM compiler, and Object into Python ([#3391](https://github.com/apache/incubator-tvm/pull/3391))
* VM: Add AllocTensor instruction and better instruction printer ([#3306](https://github.com/apache/incubator-tvm/pull/3306))
* [Relay][VM][Interpreter] Enable first-class constructors in VM and interpreter via eta expansion. ([#4218](https://github.com/apache/incubator-tvm/pull/4218))
* [Relay][VM] Clean up the VM and VM profiler code ([#4391](https://github.com/apache/incubator-tvm/pull/4391))

### Training
Relay is designed to natively support first-order and higher-order differentiation. The automatic differentiation infrastructure is now usable and a count of operators with gradient support are available in v0.6 release.

* Higher order reverse mode automatic differentiation that work with control flow ([#2496](https://github.com/apache/incubator-tvm/pull/2496))
* Higher order continuation passing style ([#3456](https://github.com/apache/incubator-tvm/pull/3456), [#3485](https://github.com/apache/incubator-tvm/pull/3485) )
* Relay gradient registration (clip [#3509](https://github.com/apache/incubator-tvm/pull/3509), max_pool2d and avg_pool2d [#3601](https://github.com/apache/incubator-tvm/pull/3601))
* Relay AD algorithm ([#3585](https://github.com/apache/incubator-tvm/pull/3585))
* Relay Training - allow gradient to return a tuple ([#3600](https://github.com/apache/incubator-tvm/pull/3600)), numerical gradient check ([#3630](https://github.com/apache/incubator-tvm/pull/3630))
* Improve AD for concatenate ([#3729](https://github.com/apache/incubator-tvm/pull/3729))
* [Relay][Training] Add missing gradient check to gradient pass ([#4169](https://github.com/apache/incubator-tvm/pull/4169))
* As a part of Relay's automatic differentiation system, we are adding primal gradients for Relay operators. Please refer to [#2562](https://github.com/apache/incubator-tvm/issues/2562) for tracking the progress.
* Gradient for Conv2d ([#3636](https://github.com/apache/incubator-tvm/pull/3636))
* Add gradient operators ([#3857](https://github.com/apache/incubator-tvm/pull/3857), [#3894](https://github.com/apache/incubator-tvm/pull/3894), [#3901](https://github.com/apache/incubator-tvm/pull/3901), [#3915](https://github.com/apache/incubator-tvm/pull/3915))
* Add gradient for log-softmax ([#4069](https://github.com/apache/incubator-tvm/pull/4069))
* [Relay][Training] Add gradient for Crossentropy ([#3925](https://github.com/apache/incubator-tvm/pull/3925))
* [Relay][Training] Add and fix gradients ([#4126](https://github.com/apache/incubator-tvm/pull/4126))

### Quantization


Low-bit inference is getting more and more popular as it benefits both the performance and storage usage. TVM now supports two types of quantization. 1. Automatic quantizaion takes floating-point precision model, does per-layer calibration and generates low-bit model. 2. TVM also imports pre-quantized model from Tensorflow and MXNet, a new dialect QNN is introduced to handle further lowering to normal operators.

* Automatic Quantization
  - Low-bit automatic quantization supported. ([#2116](https://github.com/apache/incubator-tvm/pull/2116)). The workflow includes annotation, calibration and transformation. 
  - Refactor quantization codebase and fix model accuracy. ([#3543](https://github.com/apache/incubator-tvm/pull/3543))
  - KL-divergence-based per-layer calibration. ([#3538](https://github.com/apache/incubator-tvm/pull/3538))
  - Add option to select which convolution layers are quantized. ([#3173](https://github.com/apache/incubator-tvm/pull/3173))
  - [Relay][Quantize] Integrate data-aware calibration into quantization. ([#4295](https://github.com/apache/incubator-tvm/pull/4295))
* Pre-quantized model support (QNN operators and legalize pass).
  - Add a legalize pass to Relay ([#3672](https://github.com/apache/incubator-tvm/pull/3672))
  - Qnn Concatenate, quantize, dequantize and requantize operators ([#3819](https://github.com/apache/incubator-tvm/pull/3819),  [#3730](https://github.com/apache/incubator-tvm/pull/3730), [#3745](https://github.com/apache/incubator-tvm/pull/3745), [#3531](https://github.com/apache/incubator-tvm/pull/3531))
  - QNNtoRelay & QNNLegalize Pass utility ([#3838](https://github.com/apache/incubator-tvm/pull/3838), [#3782](https://github.com/apache/incubator-tvm/pull/3782))
  - Requantize: Optimize lowering for some corner cases. ([#3864](https://github.com/apache/incubator-tvm/pull/3864))
  - New quantized operator support: conv2d, add, dense ([#3580](https://github.com/apache/incubator-tvm/pull/3580), [#3736](https://github.com/apache/incubator-tvm/pull/3736), [#3896](https://github.com/apache/incubator-tvm/pull/3896), [#3910](https://github.com/apache/incubator-tvm/pull/3910))
  - Do type checking for the input and kernel in the qnn conv2d ([#3904](https://github.com/apache/incubator-tvm/pull/3904))
  - Legalize and AlterOpLayout for Intel int8. ([#3961](https://github.com/apache/incubator-tvm/pull/3961))
  - Renaming tests to follow the Relay nomenclature. ([#3975](https://github.com/apache/incubator-tvm/pull/3975))
  - Fix padding changes due to #3739 ([#3989](https://github.com/apache/incubator-tvm/pull/3989))
  - Memorizing quantize node mapping to avoid duplicated simulated quantization ([#3233](https://github.com/apache/incubator-tvm/pull/3233))
  - Infrastructure to support pre-quantized models (QNN) ([#3971](https://github.com/apache/incubator-tvm/pull/3971)).
  - [Relay][AlterOp] NHWC to NCHWc support for Pool, concatenate, sum. ([#4059](https://github.com/apache/incubator-tvm/pull/4059))
  - [TOPI][x86] Cascade lake support. ([#4123](https://github.com/apache/incubator-tvm/pull/4123))
  - [TOPI][x86] Legalize - Support int8xint8 convolution to use VNNI inst ([#4196](https://github.com/apache/incubator-tvm/pull/4196))
  - Qnn dequantize with min max using Mxnet flavor to support Mxnet prequantized models. ([#3945](https://github.com/apache/incubator-tvm/pull/3945))
  - Improve the lowering of Qnn Dense ([#4213](https://github.com/apache/incubator-tvm/pull/4213))
  - Adding support for dequantizing from int32 to float32. ([#4130](https://github.com/apache/incubator-tvm/pull/4130))
  - [QNN] Refactor fixed point multiplication in requantize ([#4073](https://github.com/apache/incubator-tvm/pull/4073))
  - [Relay][Quantize] Use fixed point mulplications ([#4160](https://github.com/apache/incubator-tvm/pull/4160))
  - Add support for quantized multiply to Relay ([#4141](https://github.com/apache/incubator-tvm/pull/4141))
  - Use legalize to handle NHWC layout for arm_cpu ([#3754](https://github.com/apache/incubator-tvm/pull/3754))
  - [QNN][Legalize] Specialize for Platforms w/o fast Int8 support ([#4307](https://github.com/apache/incubator-tvm/pull/4307))
  - [QNN] Use Int16 upcast in Fallback Conv2D. ([#4329](https://github.com/apache/incubator-tvm/pull/4329))
  - Retain input kernel scales in QNN dialect ([#4292](https://github.com/apache/incubator-tvm/pull/4292))
  - [QNN] Lowering for Depthwise Convolution. ([#4351](https://github.com/apache/incubator-tvm/pull/4351))
  - [QNN][TFLite] Parsing QNN Add op. Adding MobilenetV2. ([#4142](https://github.com/apache/incubator-tvm/pull/4142))
  - [QNN][TFLite] Parsing TFLite quantized models. ([#3900](https://github.com/apache/incubator-tvm/pull/3900))
  - Added tflite frontend support for quantized mean. ([#4339](https://github.com/apache/incubator-tvm/pull/4339))
  - [Relay][Legalize] Legalize conv2d_transpose for NHWC ([#4399](https://github.com/apache/incubator-tvm/pull/4399))

### Accelerator and Microcontroller Support

TSIM is introduced to improve software and hardware integration and simulation accuracy. It integrates the hardware development process into the software stack. TSIM enables VTA to provide a more accurate performance feedback, i.e. clock cycles, compared to the traditional functional model of a hardware accelerator. Moreover, Chisel implementation for VTA is availale and it runs on top of TSIM.

There has been a proliferation of resource-constrained and embedded devices that do not have operating systems or a mature software stack. MicroTVM is intended to support TVM on such bare-metal devices.

* [TSIM] Enabling Cycle-Accurate Hardware Simulation for VTA ([#3010](https://github.com/apache/incubator-tvm/pull/3010), [#3206](https://github.com/apache/incubator-tvm/pull/3206), [#3242](https://github.com/apache/incubator-tvm/pull/3242))
* Chisel implementation for VTA and runs on top of TSIM ([#3258](https://github.com/apache/incubator-tvm/pull/3258), [#3347](https://github.com/apache/incubator-tvm/pull/3347))
* MicroTVM ([#3227](https://github.com/apache/incubator-tvm/pull/3227))
* Relay Compilation + AutoTVM compatible operator libraries for VTA ([#3135](https://github.com/apache/incubator-tvm/pull/3135))
* ChangeBatch pass for batched VTA compilation ([#3656](https://github.com/apache/incubator-tvm/pull/3656), [#3660](https://github.com/apache/incubator-tvm/pull/3660))
* VTA fast simulator statistics ([#3481](https://github.com/apache/incubator-tvm/pull/3481))
* TSIM improvements and fixes ([#3505](https://github.com/apache/incubator-tvm/pull/3505))
* Chisel VTA enhancements and fixes (32bit support [#3558](https://github.com/apache/incubator-tvm/pull/3558), alu instruction generation [#3592](https://github.com/apache/incubator-tvm/pull/3592), coherence support [#3593](https://github.com/apache/incubator-tvm/pull/3593), separate types [#3605](https://github.com/apache/incubator-tvm/pull/3605), tensor issue/commit [#3637](https://github.com/apache/incubator-tvm/pull/3637), uop load request [#3643](https://github.com/apache/incubator-tvm/pull/3643), uop dma requests [#3654](https://github.com/apache/incubator-tvm/pull/3654))
* VTA Runtime refactor for non-shared memory FPGAs ([#3590](https://github.com/apache/incubator-tvm/pull/3590))
* VTA HLS codebase refactor for Ultra96 ([#3496](https://github.com/apache/incubator-tvm/pull/3496))
* VTA support for batched inference ([#3661](https://github.com/apache/incubator-tvm/pull/3661))
* VTA bitstream compilation for Intel FPGA ([#3494](https://github.com/apache/incubator-tvm/pull/3494))
* TSIM: Introduce Virtual Memory for TSIM Driver ([#3686](https://github.com/apache/incubator-tvm/pull/3686))
* Parallel TSIM hardware compilation with macOS and debug support ([#3797](https://github.com/apache/incubator-tvm/pull/3797))
* Chisel: scale dram base address in hardware instead of runtime ([#3772](https://github.com/apache/incubator-tvm/pull/3772))
* Chisel: run all unittests by default ([#3766](https://github.com/apache/incubator-tvm/pull/3766))
* Chisel: improved Data Gen, Added ALU Test ([#3743](https://github.com/apache/incubator-tvm/pull/3743))
* Chisel dependencies for TSIM CI ([#3721](https://github.com/apache/incubator-tvm/pull/3721))
* Chisel: Added Module Unit Test Infrastructure ([#3698](https://github.com/apache/incubator-tvm/pull/3698))
* Add ISA BitPat generation ([#3891](https://github.com/apache/incubator-tvm/pull/3891))
* de10-nano driver ([#3394](https://github.com/apache/incubator-tvm/pull/3394))
* Extending Vision model coverage compilation for VTA ([#3740](https://github.com/apache/incubator-tvm/pull/3740))
* Conv2d transpose (deconvolution) operator support ([#3777](https://github.com/apache/incubator-tvm/pull/3777))
* Support TLPP in function simulator. ([#3555](https://github.com/apache/incubator-tvm/pull/3555))
* [VTA][Chisel] TSIM VTA Source Refactor ([#4163](https://github.com/apache/incubator-tvm/pull/4163))
* [VTA][TSIM] Serial GEMM Application Added ([#4082](https://github.com/apache/incubator-tvm/pull/4082))

### Rust Support
Rust language support in TVM includes two parts. 1. The frontend wraps the current C API and exposes a Rust programming model. 2. The backend serves as an alternative to C++ runtime. It privdes a standalone WASM module and security support, e.g., SGX.

* Rust frontend ([#2292](https://github.com/apache/incubator-tvm/pull/2292)).
* Unify types between bindings and pure Rust impl ([#2616](https://github.com/apache/incubator-tvm/pull/2616))
* Rust: load syslib modules at compile time ([#3274](https://github.com/apache/incubator-tvm/pull/3274))
* Rustify PackedFunc & Friends ([#2969](https://github.com/apache/incubator-tvm/pull/2969))
* Rust DSO module ([#2976](https://github.com/apache/incubator-tvm/pull/2976))

### Operator Support
* A special operator `annotation.stop_fusion` to prevent it being fused with previous expressions (#2624).
* `batch_matmul`  supported ([#2561](https://github.com/apache/incubator-tvm/pull/2561)).
* `reverse_reshape` supported ([#2503](https://github.com/apache/incubator-tvm/pull/2503)).
* Faster-RCNN proposal operator for CUDA ([#2420](https://github.com/apache/incubator-tvm/pull/2420)).
* Vision operator for YOLO `yolo_reorg` ([#1941](https://github.com/apache/incubator-tvm/pull/1941)).
* `slice` operator for MXNet ([#2662](https://github.com/apache/incubator-tvm/pull/2662)).
* `arange` supported ([#2621](https://github.com/apache/incubator-tvm/pull/2621)).
* Vision operator `roi_align` ([#2618](https://github.com/apache/incubator-tvm/pull/2618)).
* `where` operator for MXNet ([#2647](https://github.com/apache/incubator-tvm/pull/2647)).
* Deformable conv2d ([#2908](https://github.com/apache/incubator-tvm/pull/2908))
* Faster-RCNN Proposal OP ([#2725](https://github.com/apache/incubator-tvm/pull/2725)) 
* ROI Pool operator ([#2811](https://github.com/apache/incubator-tvm/pull/2811)) 
* Gluoncv SSD support on CPU ([#2353](https://github.com/apache/incubator-tvm/pull/2353)) 
* shape, reverse, and sign op ([#2749](https://github.com/apache/incubator-tvm/pull/2749), [#2800](https://github.com/apache/incubator-tvm/pull/2800), [#2775](https://github.com/apache/incubator-tvm/pull/2775)) 
* tile and repeat op ([#2720](https://github.com/apache/incubator-tvm/pull/2720))
* logical operators ([#2743](https://github.com/apache/incubator-tvm/pull/2743), [#2453](https://github.com/apache/incubator-tvm/pull/2453))
* stack op ([#2729](https://github.com/apache/incubator-tvm/pull/2729))
* NCHWc upsampling ([#2806](https://github.com/apache/incubator-tvm/pull/2806)) 
* clip and wrap mode support in take ([#2858](https://github.com/apache/incubator-tvm/pull/2858))
* AlterLayout support for `intel_graphics` conv2d , depthwise conv2d ([#2729](https://github.com/apache/incubator-tvm/pull/2729), [#2806](https://github.com/apache/incubator-tvm/pull/2806))
* Add foldr1 operator ([#2928](https://github.com/apache/incubator-tvm/pull/2928))
* Add rsqrt operator ([#2949](https://github.com/apache/incubator-tvm/pull/2949))
* Add clip and wrap mode support in take ([#2858](https://github.com/apache/incubator-tvm/pull/2858))
* Gather_nd exposed to relay ([#2945](https://github.com/apache/incubator-tvm/pull/2945))
* bitserial_conv2d move to autotvm template and updates ([#2819](https://github.com/apache/incubator-tvm/pull/2819))
* Port x86 NCHWc to AutoTVM for Task Extraction ([#2664](https://github.com/apache/incubator-tvm/pull/2664))
* Implement relay nn.bias_add compute in C++ ([#3027](https://github.com/apache/incubator-tvm/pull/3027))
* Rename output tensors for better readability ([#3006](https://github.com/apache/incubator-tvm/pull/3006))
* int8 dense on CUDA & Dense op quantization ([#2877](https://github.com/apache/incubator-tvm/pull/2877))
* Bitserial dense operators for CPU ([#3051](https://github.com/apache/incubator-tvm/pull/3051))
* Enhance upsample operator to adapt onnx opset v9 ([#2968](https://github.com/apache/incubator-tvm/pull/2968))
* Add adaptive pooling operator ([#3085](https://github.com/apache/incubator-tvm/pull/3085))
* Add all operator ([#3124](https://github.com/apache/incubator-tvm/pull/3124))
* Add cblas batch_matmul ([#3210](https://github.com/apache/incubator-tvm/pull/3210))
* Add packing for int8 1x1 convolution and support the int8 group convolution on X86 ([#2991](https://github.com/apache/incubator-tvm/pull/2991))
* Add op size ([#3094](https://github.com/apache/incubator-tvm/pull/3094))
* x86 TOPI (roi_align [#3475](https://github.com/apache/incubator-tvm/pull/3475), conv2d_transpose [#3491](https://github.com/apache/incubator-tvm/pull/3491) )
* Intel INT8 (dilation in conv2d [#3510](https://github.com/apache/incubator-tvm/pull/3510), type checking [#3516](https://github.com/apache/incubator-tvm/pull/3516))
* Reinterpretation of tensor elements ([#3599](https://github.com/apache/incubator-tvm/pull/3599))
* Spase-Dense for block-sparse multiplication ([#3566](https://github.com/apache/incubator-tvm/pull/3566))
* Winograd matrix computation ([#3553](https://github.com/apache/incubator-tvm/pull/3553))
* CUDA schedule for pool_grad ([#3622](https://github.com/apache/incubator-tvm/pull/3622)), group_conv2d ([#3663](https://github.com/apache/incubator-tvm/pull/3663))
* Bitserial operations conv2d, dense and bitpack ([#3844](https://github.com/apache/incubator-tvm/pull/3844))
* Improve numeric gradient check ([#3856](https://github.com/apache/incubator-tvm/pull/3856))
* Resize rework ([3788](https://github.com/apache/incubator-tvm/pull/3788))
* Improve `conv2d_transpose` CUDA schedule template ([#3796](https://github.com/apache/incubator-tvm/pull/3796))
* SpaceToDepth and MirrorPad Operators ([#3718](https://github.com/apache/incubator-tvm/pull/3718))
* Add variance and layer norm op ([#3700](https://github.com/apache/incubator-tvm/pull/3700))
* Add `sparse_transpose` for Square CSR matrices ([#3707](https://github.com/apache/incubator-tvm/pull/3707))
* TOPI: Memoize winograd matrix ([#3687](https://github.com/apache/incubator-tvm/pull/3687))
* New TOPI operators: `erf`, `logical_and`, `logical_or`, `logical_not`, `isnan` ([#3702](https://github.com/apache/incubator-tvm/pull/3702), [#3929](https://github.com/apache/incubator-tvm/pull/3929), [#3979](https://github.com/apache/incubator-tvm/pull/3979))
* Improve `ceil_divide` in tile/split ([#3842](https://github.com/apache/incubator-tvm/pull/3842))
* [Relay][Frontend][TF] Add tensor array ops ([#3798](https://github.com/apache/incubator-tvm/pull/3798), [#4309](https://github.com/apache/incubator-tvm/pull/4309))
* [TF][Op] Op where ([#4045](https://github.com/apache/incubator-tvm/pull/4045))
* [TOPI]Add op argwhere ([#3994](https://github.com/apache/incubator-tvm/pull/3994))
* [Relay] `crossentropy_with_logits` and its gradient ([#4075](https://github.com/apache/incubator-tvm/pull/4075))
* [Relay][Op] Enhance Upsample Operator to support float scales ([#4206](https://github.com/apache/incubator-tvm/pull/4206))
* [Relay][Op] Add instance norm op ([#4004](https://github.com/apache/incubator-tvm/pull/4004))

### Frontend and User Interface
* Frontend darknet ([#2773](https://github.com/apache/incubator-tvm/pull/2773))
* Support tf.gather ([#2935](https://github.com/apache/incubator-tvm/pull/2935)) 
* Support tf.where ([#2936](https://github.com/apache/incubator-tvm/pull/2936))
* Adding ADD operator to tflite frontend for compiling the MobileNetV2 ([#2919](https://github.com/apache/incubator-tvm/pull/2919))
* Support SpaceToBatchND/BatchToSpaceND in Tensorflow frontend ([#2943](https://github.com/apache/incubator-tvm/pull/2943))
* Simplify TF get_output_names ([#3025](https://github.com/apache/incubator-tvm/pull/3025))
* TF Tile Round Sign Pow Exp Reverse ([#2960](https://github.com/apache/incubator-tvm/pull/2960))
* Gluncv SSD support on the GPU ([#2784](https://github.com/apache/incubator-tvm/pull/2784))
* Allow an op as loop var in Tensorflow ([#3056](https://github.com/apache/incubator-tvm/pull/3056))
* Add FULLY_CONNECTED op into tflite frontend ([#3019](https://github.com/apache/incubator-tvm/pull/3019))
* Add MXNet converter for RNN layer ops ([#3125](https://github.com/apache/incubator-tvm/pull/3125))
* Add log op in tf frontend ([#3111](https://github.com/apache/incubator-tvm/pull/3111))
* Add SoftPlus Sqrt in Tensorflow frontend ([#3187](https://github.com/apache/incubator-tvm/pull/3187))
* Add onnx elemwise greater/less ([#3186](https://github.com/apache/incubator-tvm/pull/3186))
* Add PlaceholderWithDefault (limited) implementation in TensorFlow ([#3184](https://github.com/apache/incubator-tvm/pull/3184))
* Support tf.math.reduce_prod ([#3166](https://github.com/apache/incubator-tvm/pull/3166))
* Better shape inference in TensorFlow Frontend ([#3176](https://github.com/apache/incubator-tvm/pull/3176))
* Get list of unsupported ONNX operators ([#2995](https://github.com/apache/incubator-tvm/pull/2995))
* Implement ONNX MaxPool-v8 and MaxPool-v10 ([#3114](https://github.com/apache/incubator-tvm/pull/3114))
* Convert TFLite NCHW to NHWC ([#3141](https://github.com/apache/incubator-tvm/pull/3141))
* Add Crop op converter ([#3241](https://github.com/apache/incubator-tvm/pull/3241))
* TFLite frontend operator support: PAD, RESIZE, MUL, Reduce (min, max, mean, prod), LOGISTIC, elemwise operators (Sub, Divide, Power, Max, Min) ([#3310](https://github.com/apache/incubator-tvm/pull/3310), [#3370](https://github.com/apache/incubator-tvm/pull/3370), [#3304](https://github.com/apache/incubator-tvm/pull/3304), [#3421](https://github.com/apache/incubator-tvm/pull/3421), [#3313](https://github.com/apache/incubator-tvm/pull/3313), 3357)
* Tensorflow frontend operator support: Abs, FloorDiv, GatherND, LeftShift, LogSoftmax, Max, Min, Mod, RightShift, ZerosLike, TruncateMod, Neg, ClipByValue, ResizeNearestNeighbor ([#3270](https://github.com/apache/incubator-tvm/pull/3270), [#3211](https://github.com/apache/incubator-tvm/pull/3211), [#3393](https://github.com/apache/incubator-tvm/pull/3393))
* TFLite: Add fused_activation_function for ADD, SUB, MUL, DIV ([#3372](https://github.com/apache/incubator-tvm/pull/3372))
* Support bidirectional RNN layer for MXNet ([#3397](https://github.com/apache/incubator-tvm/pull/3397))
* TFLite operator support (pack [#3521](https://github.com/apache/incubator-tvm/pull/3521), split [#3520](https://github.com/apache/incubator-tvm/pull/3520) )
* Keras operator support (permute, softmax [#3618](https://github.com/apache/incubator-tvm/pull/3618))
* TF operator support (BatchMatMul [#3634](https://github.com/apache/incubator-tvm/pull/3634))
* TFLite frontend operator support: tile, transpose ([#3814](https://github.com/apache/incubator-tvm/pull/3814), [#3705](https://github.com/apache/incubator-tvm/pull/3705))
* ONNX frontend operator support: PReLU for NNVM, Not, Sign, Equal ([#3813](https://github.com/apache/incubator-tvm/pull/3813), [#3836](https://github.com/apache/incubator-tvm/pull/3836), [#3760](https://github.com/apache/incubator-tvm/pull/3760))
* Keras frontend operator support: Dot ([#3668](https://github.com/apache/incubator-tvm/pull/3668))
* Add more cases to Keras `_convert_reshape` ([#3846](https://github.com/apache/incubator-tvm/pull/3846))
* TensorFlow frontend operator support: OneHot, log1p, cos, sin ([#3781](https://github.com/apache/incubator-tvm/pull/3781), [#3614](https://github.com/apache/incubator-tvm/pull/3614))
* Support BatchMatMul with input dimensions larger than 3 for TensorFlow ([#3732](https://github.com/apache/incubator-tvm/pull/3732))
* ONNX new operator support: And, Tile, Erf ([#3878](https://github.com/apache/incubator-tvm/pull/3878), [#3941](https://github.com/apache/incubator-tvm/pull/3941), [#3988](https://github.com/apache/incubator-tvm/pull/3988))
* MXNet new operator support: pad, conv1d, deconv1d ([#3739](https://github.com/apache/incubator-tvm/pull/3739))
* TFLite new operator support: `batch_to_space_nd`, `space_to_batch_nd`, tanh, greater, relu ([#3850](https://github.com/apache/incubator-tvm/pull/3850), [#3996](https://github.com/apache/incubator-tvm/pull/3996), [#3963](https://github.com/apache/incubator-tvm/pull/3963), [#4022](https://github.com/apache/incubator-tvm/pull/4022))
* TFLite: Support depthwise convolution multiplier greater than 1 ([#3922](https://github.com/apache/incubator-tvm/pull/3922))
* Keras: Fix ReLU in Keras Converter missed the case ([#3917](https://github.com/apache/incubator-tvm/pull/3917))
* Keras: frontend upsample and 1 channel conv2d fixes ([#3937](https://github.com/apache/incubator-tvm/pull/3937))
* Tensorflow: Convert scalar Const into tvm.relay.const ([#3885](https://github.com/apache/incubator-tvm/pull/3885))
* TensorFlow: Add support for SquaredDifference ([#3930](https://github.com/apache/incubator-tvm/pull/3930))
* [relay][frontend] clean up tf frontend ([#3710](https://github.com/apache/incubator-tvm/pull/3710))
* [Relay][Topi][TensorFlow][ONNX][Lang] Add support for Any op ([#4205](https://github.com/apache/incubator-tvm/pull/4205))
* [Relay][Frontend][ONNX] Add support for op Where ([#4184](https://github.com/apache/incubator-tvm/pull/4184))
* [Relay][TopHub] Add switch to disable TopHub download ([#4015](https://github.com/apache/incubator-tvm/pull/4015))
* Add parser support for CAST tflite operator ([#4096](https://github.com/apache/incubator-tvm/pull/4096))
* Add parses support for `zeros_like` tflite operator ([#4042](https://github.com/apache/incubator-tvm/pull/4042))
* Add parser support for SUM tflite operator ([#4182](https://github.com/apache/incubator-tvm/pull/4182))
* Add support for tf.assert (as no-op) and `tf.no_op` to TF Relay frontend. ([#4172](https://github.com/apache/incubator-tvm/pull/4172))
* [Relay][Frontend][ONNX] New Operators and Opsets to Support BERT ([#4197](https://github.com/apache/incubator-tvm/pull/4197))
* [Relay][Params] Add APIs for storing and retrieving parameters from individual functions. ([#4194](https://github.com/apache/incubator-tvm/pull/4194))
* Add `build_create_shared_func` to tvm/contrib/cc.py ([#3840](https://github.com/apache/incubator-tvm/pull/3840))
* Tensorflow saved model for NNVM ([#2493](https://github.com/apache/incubator-tvm/pull/2493/) and Relay ([#2586](https://github.com/apache/incubator-tvm/pull/2586/)).
* Introduced `HybridModule` ([#2477](https://github.com/apache/incubator-tvm/pull/2477)) so that normal TVM schedule can be compiled to hybrid target, run and dumped to Hybrid Script.
* Relay ][Frontend][Tensorflow] add operator `add_n` ([#4181](https://github.com/apache/incubator-tvm/pull/4181))
* [Relay][Frontend][Tensorflow] StopGradient ([#4238](https://github.com/apache/incubator-tvm/pull/4238))
* [Relay][Frontend][ONNX] Add support for broadcasting to Where and MatMul ([#4267](https://github.com/apache/incubator-tvm/pull/4267))
* [TFLite] Support PRelu ([#4298](https://github.com/apache/incubator-tvm/pull/4298))
* [Frontend][MxNet] support mxnet cond op ([#4311](https://github.com/apache/incubator-tvm/pull/4311))
* Add support for `quant.mul` operator in tflite frontend ([#4283](https://github.com/apache/incubator-tvm/pull/4283))
* [Relay][Frontend][ONNX] operator support: DepthToSpace, SpaceToDepth ([#4271](https://github.com/apache/incubator-tvm/pull/4271))
* [Relay][Frontend][Tensorflow]Add `conv2d_transpose`. ([#4300](https://github.com/apache/incubator-tvm/pull/4300))
* [Frontend]Add TensorFlow FloorMod ([#4308](https://github.com/apache/incubator-tvm/pull/4308))

### Runtime and Backend Support
* Make external library extend TVM's NDArray more easily ([#2613](https://github.com/apache/incubator-tvm/pull/2613)).
* Improvements for NNPACK integratation, includes ci test, winograd ([#2846](https://github.com/apache/incubator-tvm/pull/2846), [#2868](https://github.com/apache/incubator-tvm/pull/2868), [#2856](https://github.com/apache/incubator-tvm/pull/2856), [#2721](https://github.com/apache/incubator-tvm/pull/2721)) 
* Improvements for OpenCL runtime ([#2741](https://github.com/apache/incubator-tvm/pull/2741), [#2737](https://github.com/apache/incubator-tvm/pull/2737))
* GraphRuntime: Enable sharing parameters of a model among multiple threads ([#3384](https://github.com/apache/incubator-tvm/pull/3384))
* Android runtime argsort support ([#3472](https://github.com/apache/incubator-tvm/pull/3472))
* GraphRuntime enhancements (set_input_zero_copy [#3416](https://github.com/apache/incubator-tvm/pull/3416))
* A new minimal runtime implementation (~12kb .text on ARMv7/x86) for TVM.
* Add AVX512VNNI support for TVM ([#3388](https://github.com/apache/incubator-tvm/pull/3388))
* Enable miopen Group Convolution ([#3987](https://github.com/apache/incubator-tvm/pull/3987))
* Minimal runtime (~12kb .text on ARMv7/x86) for subset of TVM models ([#3567](https://github.com/apache/incubator-tvm/pull/3567))
* [RUNTIME] Separate runtime related contrib into runtime/contrib ([#4207](https://github.com/apache/incubator-tvm/pull/4207))
* [topi] add ARM v8.2 udot (uint8) support ([#3978](https://github.com/apache/incubator-tvm/pull/3978))
* [codegen] Add multiple operands and function support when using fp16 compilation ([#4056](https://github.com/apache/incubator-tvm/pull/4056))
* [TOPI] Added support for Mali Bifrost target ([#4047](https://github.com/apache/incubator-tvm/pull/4047))
* [topi] enable fp16 sort for arm ([#4084](https://github.com/apache/incubator-tvm/pull/4084))
* Add OpenOCD Low-Level Device (RISC-V Support) ([#3756](https://github.com/apache/incubator-tvm/pull/3756))
* Add wave 32 bc for AMD ROCm backend ([#3984](https://github.com/apache/incubator-tvm/pull/3984))
* [RUTNIME] Support C++ RPC ([#4281](https://github.com/apache/incubator-tvm/pull/4281))
* [TOPI][OP] Support Faster-RCNN Proposal OP on CPU ([#4297](https://github.com/apache/incubator-tvm/pull/4297))
* [TVM][RUNTIME] A minimum example to generate external library wrappers for DSOModule ([#4280]https://github.com/apache/incubator-tvm/pull/4280))

### Language and Architecture
* Support custom datatypes ([#2900](https://github.com/apache/incubator-tvm/pull/2900))
* Add the acc16 intrinsic support ([#3081](https://github.com/apache/incubator-tvm/pull/3081))
* Handle float16 constants & fix BatchNorm ([#3260](https://github.com/apache/incubator-tvm/pull/3260))
* Structural hash - incorporate the var type into its hash ([#3267](https://github.com/apache/incubator-tvm/pull/3267))
* Relay C++ Build Module ([#3082](https://github.com/apache/incubator-tvm/pull/3082), [#3144](https://github.com/apache/incubator-tvm/pull/3144), [#3174](https://github.com/apache/incubator-tvm/pull/3174))
* Enable decorating python class to be a Relay Pass ([#3364](https://github.com/apache/incubator-tvm/pull/3364))
* Make Partial Eval support interprocedural optimization and termination check. ([#3033](https://github.com/apache/incubator-tvm/pull/3033))
* Introduce feature manager to Relay. ([#3236](https://github.com/apache/incubator-tvm/pull/3236))
* Use Relay parser to define the Relay prelude ([#3043](https://github.com/apache/incubator-tvm/pull/3043))
* Mechanism to detect incomplete expression match in Relay ([#3203](https://github.com/apache/incubator-tvm/pull/3203))
* EQ/NE operators support for StringImm expressions ([#3283](https://github.com/apache/incubator-tvm/pull/3283))
* Mechanism to detect incomplete expression match in Relay ([#3203](https://github.com/apache/incubator-tvm/pull/3203))
* Introduce CanonicalizeCast pass to formally reduce memory overhead introduced by fused cast operations ([#3280](https://github.com/apache/incubator-tvm/pull/3280))
* Support overloading comparison operations in Relay ([#3168](https://github.com/apache/incubator-tvm/pull/3168))
* Mac count: provide a pass to calculate the number of multiply-accumulate operations in a network ([#2609](https://github.com/apache/incubator-tvm/pull/2609)).
  - support for `conv_2d_transpose` ([#3469](https://github.com/apache/incubator-tvm/pull/3469))
  - [Relay][Pass] Count MAC for BatchMatMul ([#4157](https://github.com/apache/incubator-tvm/pull/4157))
  - Detect depthwise conv2d in `mac_count` pass ([#3083](https://github.com/apache/incubator-tvm/pull/3083))
* Add Tuple pattern ([#3596](https://github.com/apache/incubator-tvm/pull/3596))
* Text format support for ADTs and prelude ([#3863](https://github.com/apache/incubator-tvm/pull/3863), [#3939](https://github.com/apache/incubator-tvm/pull/3939))
* Add new IR pass CombineParallelDense ([#3862](https://github.com/apache/incubator-tvm/pull/3862))
* Add support for `EQ` op in the deduce bound and the loop partition ([#3775](https://github.com/apache/incubator-tvm/pull/3775))
* Introduce base-class IRMutatorWithAnalyzer ([#3969](https://github.com/apache/incubator-tvm/pull/3969))
* Define more standard global functions in the prelude of relay program, includes foldr1, hd, tl, nth, list update ([#2928](https://github.com/apache/incubator-tvm/pull/2928), [#2917](https://github.com/apache/incubator-tvm/pull/2917), [#2771](https://github.com/apache/incubator-tvm/pull/2771), [#2866](https://github.com/apache/incubator-tvm/pull/2866))
* Add SkipVectorize pass ([#3222](https://github.com/apache/incubator-tvm/pull/3222), [#3228](https://github.com/apache/incubator-tvm/pull/3228))
* [Relay][Pass] Add pass to remove unused functions in relay module ([#4334](https://github.com/apache/incubator-tvm/pull/4334))

## Feature Improvement
### Symbolic shape enhancement
* Add shape function for symbolic shape. It enables certain cases for broadcast with symbolic shapes. ([#3606](https://github.com/apache/incubator-tvm/pull/3606))
* [tvm][any] broadcast with values other than one ([#3967](https://github.com/apache/incubator-tvm/pull/3967))
* Symbolic shape support (broadcast op [#3389](https://github.com/apache/incubator-tvm/pull/3389))
* Support reshape for dynamic shape in tf converter ([#4185](https://github.com/apache/incubator-tvm/pull/4185))
* Runtime Shape Functions ([#4179](https://github.com/apache/incubator-tvm/pull/4179))

### Language and Architecture
* An optimization pass to eliminate expressions which have the same functionality and same inputs ([#2639](https://github.com/apache/incubator-tvm/pull/2639)).
* Refactor text printer to add stream-like API and FunctionType support ([#2605](https://github.com/apache/incubator-tvm/pull/2605), [#2882](https://github.com/apache/incubator-tvm/pull/2882))
* Build a scaffold for structured error handling ([#2838](https://github.com/apache/incubator-tvm/pull/2838)). The new mechanism detects and rewrites error messages so that c++ and python stack trace are unified and not redundant. Guideslines and conventions for error handling is also discussed.
* Higher order reverse mode automatic differentiation that work with control flow ([#2496](https://github.com/apache/incubator-tvm/pull/2496))
* Integer arithmetic analyzers, includes modular set analysis, const integer bound analysis and rewrite simplifier ([#2904](https://github.com/apache/incubator-tvm/pull/2904), [#2851](https://github.com/apache/incubator-tvm/pull/2851), [#2768](https://github.com/apache/incubator-tvm/pull/2768), [#2722](https://github.com/apache/incubator-tvm/pull/2722), [#2668](https://github.com/apache/incubator-tvm/pull/2668), [#2860](https://github.com/apache/incubator-tvm/pull/2860))
* Improve operator fusion for TupleGetItem in relay ([#2914](https://github.com/apache/incubator-tvm/pull/2914), [#2929](https://github.com/apache/incubator-tvm/pull/2929), 
* Compute FLOP of autotvm template for int8 models ([#2776](https://github.com/apache/incubator-tvm/pull/2776)) 
* Common subexpression elimination pass in Relay ([#2639](https://github.com/apache/incubator-tvm/pull/2639))
* Improve quantization in Relay ([#2723](https://github.com/apache/incubator-tvm/pull/2723))
* Refactor `build_func` in measure module of autotvm to better support cross compiler ([#2927](https://github.com/apache/incubator-tvm/pull/2927))
* Quantize all fields of concatenate ([#2913](https://github.com/apache/incubator-tvm/pull/2913))
* Remove stale verilog generator ([#2964](https://github.com/apache/incubator-tvm/pull/2964))
* Improve Relay printing ([#2984](https://github.com/apache/incubator-tvm/pull/2984), [#2881](https://github.com/apache/incubator-tvm/pull/2881), [#3030](https://github.com/apache/incubator-tvm/pull/3030), [#3041](https://github.com/apache/incubator-tvm/pull/3041))
* Add min_num_branches option in CombineParallelConv2D ([#2961](https://github.com/apache/incubator-tvm/pull/2961))
* Add expr_visitor, fix expr_functor exponential blowup problem ([#2988](https://github.com/apache/incubator-tvm/pull/2988))
* Support Deriving channels when it is not provided in AlterLayout. ([#2972](https://github.com/apache/incubator-tvm/pull/2972))
* Enhance BoundDeduce algorithm ([#2795](https://github.com/apache/incubator-tvm/pull/2795))
* Enhance loop partition algorithm ([#2956](https://github.com/apache/incubator-tvm/pull/2956))
* Better tuple fusion implementation ([#3092](https://github.com/apache/incubator-tvm/pull/3092))
* Enhance fusion rule that starts from elemwise and broadcast ([#2932](https://github.com/apache/incubator-tvm/pull/2932))
* Remove on_device op after annotation in heterogeneous pass ([#3204](https://github.com/apache/incubator-tvm/pull/3204))
* Improve canonical and rewrite simplifier ([#3132](https://github.com/apache/incubator-tvm/pull/3132), [#3149](https://github.com/apache/incubator-tvm/pull/3149))
* Capture constant external python variables in hybrid script ([#3157](https://github.com/apache/incubator-tvm/pull/3157))
* Remove Peano nats from the prelude ([#3045](https://github.com/apache/incubator-tvm/pull/3045))
* Macro to define NodeRef methods, constructor style example ([#3224](https://github.com/apache/incubator-tvm/pull/3224))
* Consistent RAII scoping API ([#3231](https://github.com/apache/incubator-tvm/pull/3231))
* Register all operators' attributes in Python ([#3175](https://github.com/apache/incubator-tvm/pull/3175))
* Add module supoort in relay.build ([#3424](https://github.com/apache/incubator-tvm/pull/3424))
* Relay pass infrastructure improvement ([#3319](https://github.com/apache/incubator-tvm/pull/3319), [#3336](https://github.com/apache/incubator-tvm/pull/3336), [#3430](https://github.com/apache/incubator-tvm/pull/3430), [#3353](https://github.com/apache/incubator-tvm/pull/3353))
* Migrate Relay passes to pass manager ([#3323](https://github.com/apache/incubator-tvm/pull/3323), [#3289](https://github.com/apache/incubator-tvm/pull/3289), [#3251](https://github.com/apache/incubator-tvm/pull/3251), [#3406](https://github.com/apache/incubator-tvm/pull/3406))
* Improve heterogeneous annotation by using visitor ([#3261](https://github.com/apache/incubator-tvm/pull/3261))
* Support export ADT value in Python ([#3299](https://github.com/apache/incubator-tvm/pull/3299))
* Extend TensorComputeOp to allow scalar inputs ([#3300](https://github.com/apache/incubator-tvm/pull/3300))
* Transitioning low-level IR away from HalideIR ([#3533](https://github.com/apache/incubator-tvm/pull/3533), [#3535](https://github.com/apache/incubator-tvm/pull/3535))
* Tags for ADT constructors ([#3369](https://github.com/apache/incubator-tvm/pull/3369))
* IR dumping for debugging ([#3493](https://github.com/apache/incubator-tvm/pull/3493))
* Pretty printer and parser roundtrip ([#3460](https://github.com/apache/incubator-tvm/pull/3460), [#3536](https://github.com/apache/incubator-tvm/pull/3536))
* Relay type checking (conv2d weight dimension [#3511](https://github.com/apache/incubator-tvm/pull/3511), any shape [#3221](https://github.com/apache/incubator-tvm/pull/3221))
* Relay Module enhancements (remove free variables [#3476](https://github.com/apache/incubator-tvm/pull/3476))
* LLVM DWARF debug information ([#3420](https://github.com/apache/incubator-tvm/pull/3420))
* Printer for Layout/BijectiveLayout ([#3582](https://github.com/apache/incubator-tvm/pull/3582))
* Type inference escape hatch ([#3571](https://github.com/apache/incubator-tvm/pull/3571))
* Making iterators compatible with constructors of STL containers ([#3624](https://github.com/apache/incubator-tvm/pull/3624))
* Moving Conv, Dense, Concatenate InferTypes to header ([#3783](https://github.com/apache/incubator-tvm/pull/3783))
* Simplify casts of constants 0 and 1 ([#3758](https://github.com/apache/incubator-tvm/pull/3758))
* Conditionally replace reduction init axis. ([#3408](https://github.com/apache/incubator-tvm/pull/3408))
* Improve Partial Evaluator ([#3749](https://github.com/apache/incubator-tvm/pull/3749), [#3703](https://github.com/apache/incubator-tvm/pull/3703))
* Strict mode in Relay pattern matching ([#3620](https://github.com/apache/incubator-tvm/pull/3620))
* Quit and clean when TVM is interrupted ([#3640](https://github.com/apache/incubator-tvm/pull/3640))
* Make Type Relation catch more errors ([#3899](https://github.com/apache/incubator-tvm/pull/3899), [#3699](https://github.com/apache/incubator-tvm/pull/3699))
* Refactor the way we interface between different modules of Relay ([#3906](https://github.com/apache/incubator-tvm/pull/3906))
* Introduce `schedule_injective_from_existing` and unify external schedules for all targets ([#3983](https://github.com/apache/incubator-tvm/pull/3983))
* [NODE][REFACTOR] Refactor reflection system in node. ([#4189](https://github.com/apache/incubator-tvm/pull/4189))
* Unify node system and object ([#4161](https://github.com/apache/incubator-tvm/pull/4161), [#4115](https://github.com/apache/incubator-tvm/pull/4115), [#4128](https://github.com/apache/incubator-tvm/pull/4128))
* [Relay][Refactor] Rename Datatype to ADT ([#4156](https://github.com/apache/incubator-tvm/pull/4156))
* [Relay] fix exponential blowup in interpreter ([#3559](https://github.com/apache/incubator-tvm/pull/3559))
* [Relay] Fix memory leak in the interpreter ([#4155](https://github.com/apache/incubator-tvm/pull/4155))
* [rpc] use callback func to do send & recv ([#4147](https://github.com/apache/incubator-tvm/pull/4147))
* Add `lift_if_then_else` pass to improve loop partitioning ([#3865](https://github.com/apache/incubator-tvm/pull/3865))
* Decrease the complexity of CalcDep from exponential to linear ([#4053](https://github.com/apache/incubator-tvm/pull/4053))
* [IR] Make iterators compatible with constructors of STL containers ([#3624](https://github.com/apache/incubator-tvm/pull/3624))
* [Relay][Pass] Avoid FoldConstant folding some ops ([#4245](https://github.com/apache/incubator-tvm/pull/4245))
* [Relay][Prelude] More dtypes support in `tensor_t` ([#4233](https://github.com/apache/incubator-tvm/pull/4233))
* [NODE][REFACTOR] Rename IRFunctor->NodeFunctor, use func pointer ([#4247](https://github.com/apache/incubator-tvm/pull/4247))
* [RUNTIME][REFACTOR] Use object protocol to support runtime::Module ([#4289](https://github.com/apache/incubator-tvm/pull/4289))
* [CodeGen] Add build config option `disable_assert` to control whether to generate assert. ([#4340](https://github.com/apache/incubator-tvm/pull/4340))

### Arithmetic Analysis
* Formalize Integer Arithmetic Analysis (RFC: [#2588](https://github.com/apache/incubator-tvm/issues/2588)). It is aiming to perform better context-dependent analysis, bound analysis, centralized arithmetic logic and arithmetic simplification. ([#3272](https://github.com/apache/incubator-tvm/pull/3272), [#3463](https://github.com/apache/incubator-tvm/pull/3463), [#3464](https://github.com/apache/incubator-tvm/pull/3464), [#3368](https://github.com/apache/incubator-tvm/pull/3368), [#3503](https://github.com/apache/incubator-tvm/pull/3503), [#3504](https://github.com/apache/incubator-tvm/pull/3504) , [#3502](https://github.com/apache/incubator-tvm/pull/3502), [#3479](https://github.com/apache/incubator-tvm/pull/3479) , [#3568](https://github.com/apache/incubator-tvm/pull/3568))
* Introduce FloorDiv/Mod, TruncDiv/Mod, and IndexDiv/Mod for better arithmetic simplification ([#3976](https://github.com/apache/incubator-tvm/pull/3976), [#3986](https://github.com/apache/incubator-tvm/pull/3986), [#4000](https://github.com/apache/incubator-tvm/pull/4000), [#4014](https://github.com/apache/incubator-tvm/pull/4014), [#4008](https://github.com/apache/incubator-tvm/pull/4008), [#4028](https://github.com/apache/incubator-tvm/pull/4028))
* [ARITH] Use floordiv for the deduce bound ([#4025](https://github.com/apache/incubator-tvm/pull/4025))
* [Simplifier] Rewrite simplification rule to eliminate unnecessary conditionals. ([#4076](https://github.com/apache/incubator-tvm/pull/4076))

### Runtime and Backend Support
* Provide error msg for failure function call in tvm4j ([#2967](https://github.com/apache/incubator-tvm/pull/2967))
* Expose backtrace symbols in Debug mode ([#3001](https://github.com/apache/incubator-tvm/pull/3001))
* C++ GraphRuntimeCodegen, Deprecate Python2 ([#2986](https://github.com/apache/incubator-tvm/pull/2986))
* Ensure interpreted functions can take values that are not TensorValues ([#3015](https://github.com/apache/incubator-tvm/pull/3015))
* Make OpenCL runtime Compatible with OpenCL2.0 ([#2897](https://github.com/apache/incubator-tvm/pull/2897))
* Handle INF and NAN in CUDA and OpenCL ([#3194](https://github.com/apache/incubator-tvm/pull/3194))
* Update debug graph runtime for more precise layerwise timing ([#3232](https://github.com/apache/incubator-tvm/pull/3232))
* ROCM support (llvm printing [#3662](https://github.com/apache/incubator-tvm/pull/3662), ld.lld finding [#3664](https://github.com/apache/incubator-tvm/pull/3664), save to file [#3665](https://github.com/apache/incubator-tvm/pull/3665))
* Threadpool: make spin_count configurable ([#3577](https://github.com/apache/incubator-tvm/pull/3577))
* RPC worker children termination ([#3669](https://github.com/apache/incubator-tvm/pull/3669))
* Vulkan runtime reimplementation (stream approach) ([#3849](https://github.com/apache/incubator-tvm/pull/3849))
* Vulkan backend supports Call::reinterpret and vectorized comparison ([#3795](https://github.com/apache/incubator-tvm/pull/3795))
* Support MKL on Windows ([#3837](https://github.com/apache/incubator-tvm/pull/3837))
* Vulkan IR builder (bool to float [#3513](https://github.com/apache/incubator-tvm/pull/3513))
* Force `code_object_v2` for amd gpu backend ([#4099](https://github.com/apache/incubator-tvm/pull/4099))
* [Codegen][cuda-fp16] fallback to fp32 simulation when cuda arch < sm53 ([#4268](https://github.com/apache/incubator-tvm/pull/4268))
* Fix and refactoring for AMD gpu backend ([#4305](https://github.com/apache/incubator-tvm/pull/4305), [#4321](https://github.com/apache/incubator-tvm/pull/4321), [#4341](https://github.com/apache/incubator-tvm/pull/4341), [#4342](https://github.com/apache/incubator-tvm/pull/4342))
* [Debugger] Sorting op-time breakdown for quicker analysis. ([#4352](https://github.com/apache/incubator-tvm/pull/4352))
* [nvcc] enable multiple arch in one fatbin ([#4377](https://github.com/apache/incubator-tvm/pull/4377))
* [RUNTIME] Move module export to the function level. ([#4405](https://github.com/apache/incubator-tvm/pull/4405))


### Frontend and User Interface
* Relay now supports saving and loading parameter dictionaries. ([#2620](https://github.com/apache/incubator-tvm/pull/2620))
* Add `max_num_threads` to Hybrid Script, which allows users to get max number of threads for GPU targets ([#2672](https://github.com/apache/incubator-tvm/pull/2672/)).
* Improvements for tensorflow frontend ([#2830](https://github.com/apache/incubator-tvm/pull/2830), [#2757](https://github.com/apache/incubator-tvm/pull/2757), [#2586](https://github.com/apache/incubator-tvm/pull/2586)), includes decompiling tf control flow ([#2830](https://github.com/apache/incubator-tvm/pull/2830))
* Improvements for mxnet frontend ([#2844](https://github.com/apache/incubator-tvm/pull/2844), [#2777](https://github.com/apache/incubator-tvm/pull/2777), [#2772](https://github.com/apache/incubator-tvm/pull/2772), [#2706](https://github.com/apache/incubator-tvm/pull/2706), [#2704](https://github.com/apache/incubator-tvm/pull/2704), [#2709](https://github.com/apache/incubator-tvm/pull/2709),, [#2739](https://github.com/apache/incubator-tvm/pull/2739)) 
* Improvements for keras frontend ([#2842](https://github.com/apache/incubator-tvm/pull/2842), [#2854](https://github.com/apache/incubator-tvm/pull/2854))
* Improvements for DarkNet frontend ([#2673](https://github.com/apache/incubator-tvm/pull/2673))
* Improvements for ONNX frontend ([#2843](https://github.com/apache/incubator-tvm/pull/2843), [#2840](https://github.com/apache/incubator-tvm/pull/2840))
* Better profile result dump in Chrome Tracing format ([#2922](https://github.com/apache/incubator-tvm/pull/2922), [#2863](https://github.com/apache/incubator-tvm/pull/2863))
* Unified error handling in NNVM and Relay frontends ([#2828](https://github.com/apache/incubator-tvm/pull/2828)) 
* Improve NNVM to Relay conversion ([#2734](https://github.com/apache/incubator-tvm/pull/2734))
* Remove `input_0d_mismatch` special handling for TF Frontend(#3087)
* Bumped ONNX version from 1.1.0 to 1.4.1 ([#3286](https://github.com/apache/incubator-tvm/pull/3286))
* Simplify parameter handling in Tensorflow frontend ([#2993](https://github.com/apache/incubator-tvm/pull/2993))
* CoreML improvement for image scaler and padding ([#3800](https://github.com/apache/incubator-tvm/pull/3800))
* Clean up TensorFlow frontend ([#3710](https://github.com/apache/incubator-tvm/pull/3710))
* Darknet: Solve tvm parsing darknet resnext failure bug ([#3778](https://github.com/apache/incubator-tvm/pull/3778))
* Frontend changes `get_workload` - ([#3483](https://github.com/apache/incubator-tvm/pull/3483))
* [TF][Relay][Op] Pass module when infer shape ([#4287](https://github.com/apache/incubator-tvm/pull/4287))

### AutoTVM
* Support override in `register_topi_compute` and `register_topi_schedule`. ([#3292](https://github.com/apache/incubator-tvm/pull/3292))
* Improve graph tuner dealing with Tuple. ([#3649](https://github.com/apache/incubator-tvm/pull/3649))
* Add AutoTVM template for conv2d Intel int8. ([#3955](https://github.com/apache/incubator-tvm/pull/3955))
* Add AutoTVM template for dense on CUDA. ([#3923](https://github.com/apache/incubator-tvm/pull/3923))
* Add AutoTVM template for conv2d on Intel graphics. ([#3839](https://github.com/apache/incubator-tvm/pull/3839))
* Optimizing autotvm task extraction speed. ([#4138](https://github.com/apache/incubator-tvm/pull/4138))
* [AutoTVM] Add batch_matmul to tunable operations. ([#4242](https://github.com/apache/incubator-tvm/pull/4242))
* Selecting tuning templates when extracting task. ([#4338](https://github.com/apache/incubator-tvm/pull/4338))

# Performance Improvements
* Enable AlterOpLayout pass for x86 on Relay ([#2585](https://github.com/apache/incubator-tvm/issues/2585)). It is essential to get decent performance for CNN-based model on Intel CPUs.
* Better intrinsic matching for x86 CPU and ARM CPU, includes variants of vcvtph2ps and vmlal.s16 ([#2925](https://github.com/apache/incubator-tvm/pull/2925), [#2748](https://github.com/apache/incubator-tvm/pull/2748)).
* Improve injective schedule for ARM CPU([#2801](https://github.com/apache/incubator-tvm/pull/2801))
* Core functionality for Graph tuner ([#2184](https://github.com/apache/incubator-tvm/pull/2184))
* Fast tanh implementation ([#3255](https://github.com/apache/incubator-tvm/pull/3255))
* Improve multi-batch conv2d on x86 ([#3308](https://github.com/apache/incubator-tvm/pull/3308))
* Improve `non_max_suppression` and `get_valid_counts` for CPU ([#3305](https://github.com/apache/incubator-tvm/pull/3305))
* Improve `roi_align` performance for CPU ([#3296](https://github.com/apache/incubator-tvm/pull/3296))
* Improve `nms` and `get_valid_count` performance ([#3282](https://github.com/apache/incubator-tvm/pull/3282))
* Graph tuner for multiple subgraph ([#3490](https://github.com/apache/incubator-tvm/pull/3490))
* For sparsity, fast transpose for square CSR matrices has been now merged, which is a good start point for more general sparse type support.
* Reduce `set_input` and `set_input_zero_copy` overhead ([#3805](https://github.com/apache/incubator-tvm/pull/3805))
* Parallelize batch axis for ARM ([#3931](https://github.com/apache/incubator-tvm/pull/3931))
* Support cuBLAS BatchMatMul ([#3936](https://github.com/apache/incubator-tvm/pull/3936))
* Add AVX512VNNI support for TVM ([#3388](https://github.com/apache/incubator-tvm/pull/3388))
* Enhance tuning space of split ([#3949](https://github.com/apache/incubator-tvm/pull/3949))
* Enable miopen transpose convolution and fp16 support ([#3952](https://github.com/apache/incubator-tvm/pull/3952))
* Improve `conv2d_transpose` schedule on X86 and CUDA ([#3948](https://github.com/apache/incubator-tvm/pull/3948))
* Expose llvm.nearbyint intrinsic ([#4001](https://github.com/apache/incubator-tvm/pull/4001))
* [TOPI][X86] Pool operator parallel support. ([#4090](https://github.com/apache/incubator-tvm/pull/4090))
* Improve layout for several operators ([#4103](https://github.com/apache/incubator-tvm/pull/4103), [#4040](https://github.com/apache/incubator-tvm/pull/4040), [#4080](https://github.com/apache/incubator-tvm/pull/4080))
* [Relay][VM] Fix constant folding issue in VM compiler ([#4077](https://github.com/apache/incubator-tvm/pull/4077))
* [relay][vm] Reuse allocated device memory ([#4170](https://github.com/apache/incubator-tvm/pull/4170))
* [Runtime] Enable option to use OpenMP thread pool ([#4089](https://github.com/apache/incubator-tvm/pull/4089))
* [PERF] Parallelize reduction for CPU ([#4158](https://github.com/apache/incubator-tvm/pull/4158))
* [TOPI] Tunable Template for Conv2D HWCN on CUDA ([#4168](https://github.com/apache/incubator-tvm/pull/4168))
* [TOPI] Add valid auto tvm for Intel Graphics ([#4078](https://github.com/apache/incubator-tvm/pull/4078))
* [TOPI] FIFO buffer op, to accelerate sequence modeling with dilated convolutions ([#4039](https://github.com/apache/incubator-tvm/pull/4039))
* TensorCore Support using Intrinsic ([#4136](https://github.com/apache/incubator-tvm/pull/4136))
* Auto TensorCore CodeGen ([#4234](https://github.com/apache/incubator-tvm/pull/4234))
* Use cblas for dense and batch_matmul ([#3787](https://github.com/apache/incubator-tvm/pull/3787))
* Update TOPI softmax compute and CPU schedule ([#3680](https://github.com/apache/incubator-tvm/pull/3680))
* [VTA] Performance optimize, remove unnecessary contigious memory use. ([#4246](https://github.com/apache/incubator-tvm/pull/4246))
* [TOPI][AlterOpLayout][ARM] Enabling NHWC to NCHW layout transformation. ([#4249](https://github.com/apache/incubator-tvm/pull/4249))
* [PERF] Parallelize reduction for CPU ([#4158](https://github.com/apache/incubator-tvm/pull/4158))
* [ThreadPool] Solve thread transitions issue ([#4344](https://github.com/apache/incubator-tvm/pull/4344))

# Documentation
* Tutorials for deep learning frameworks support in Relay.
* Tutorial for running AutoTVM with Relay ([#2594](https://github.com/apache/incubator-tvm/pull/2594)).
* Document for Algebraic Data Types ([#2575](https://github.com/apache/incubator-tvm/pull/2575)).
* Move NNVM tutorials to Relay ([#2783](https://github.com/apache/incubator-tvm/pull/2783), [#2785](https://github.com/apache/incubator-tvm/pull/2785), [#2766](https://github.com/apache/incubator-tvm/pull/2766), [#2693](https://github.com/apache/incubator-tvm/pull/2693))
* Documentation on operators ([#2761](https://github.com/apache/incubator-tvm/pull/2761))
* Add gradient operator tutorial docs ([#2751](https://github.com/apache/incubator-tvm/pull/))
* Add compiler pass tutorial docs ([#2746](https://github.com/apache/incubator-tvm/pull/))
* Add Android Tutorial ([#2977](https://github.com/apache/incubator-tvm/pull/2977)) 
* Developer documentation for InferBound pass ([#3126](https://github.com/apache/incubator-tvm/pull/3126))
* Add missing targets to target_name documentation ([#3128](https://github.com/apache/incubator-tvm/pull/3128))
* Various documentation improvements ([#3133](https://github.com/apache/incubator-tvm/pull/3133))
* Add VM doc ([#3188](https://github.com/apache/incubator-tvm/pull/3188))
* Update documents for TSim ([#3409](https://github.com/apache/incubator-tvm/pull/3409), [#3318](https://github.com/apache/incubator-tvm/pull/3318), [#3302](https://github.com/apache/incubator-tvm/pull/3302), [#3343](https://github.com/apache/incubator-tvm/pull/3343), [#3206](https://github.com/apache/incubator-tvm/pull/3206))
* Improve tvm4j document describing LLVM support ([#3404](https://github.com/apache/incubator-tvm/pull/3404))
* Tutorial migration to Python3 ([#3498](https://github.com/apache/incubator-tvm/pull/3498/files))
* Android RPC README ([#3500](https://github.com/apache/incubator-tvm/pull/3500))
* Documentation for Relay opcode ([#3522](https://github.com/apache/incubator-tvm/pull/3522))
* Tutorial for pass manager ([#3515](https://github.com/apache/incubator-tvm/pull/3515))
* Minimum version of Python in docs ([#3588](https://github.com/apache/incubator-tvm/pull/3588))
* Relay pass infra ([#3583](https://github.com/apache/incubator-tvm/pull/3583))
* X86 Autotune tutorial improvements ([#3609](https://github.com/apache/incubator-tvm/pull/3609))
* YOLOv3 tiny Darknet tutorial ([#3674](https://github.com/apache/incubator-tvm/pull/3674))
* SSD doc to avoid confusion ([#3677](https://github.com/apache/incubator-tvm/pull/3677))
* Tutorial: Build a Graph Convolutional Network on TVM ([#3681](https://github.com/apache/incubator-tvm/pull/3681))
* Add docs for analysis namespace ([#3985](https://github.com/apache/incubator-tvm/pull/3985))
* [tutorial] Relay pass infra tutorial ([#4083](https://github.com/apache/incubator-tvm/pull/4083))
* [DOCS] Add TensorFlow frontend docs ([#4154](https://github.com/apache/incubator-tvm/pull/4154))
* Tutorial: update Building a Graph Convolutional Network tutorial ([#4060](https://github.com/apache/incubator-tvm/pull/4060))
* [Docs] Add dependency of compilation with LLVM ([#4117](https://github.com/apache/incubator-tvm/pull/4117))
* [Documentation]Fix example code in comment of tvm.build_module.build() ([#4195](https://github.com/apache/incubator-tvm/pull/4195))
* TSIM: add virtual memory support to examples ([#3868](https://github.com/apache/incubator-tvm/pull/3868))
* Relay pass infra tutorial ([#4083](https://github.com/apache/incubator-tvm/pull/4083))
* Fix the TF tutorial to run against TF2.0 and TF1.x ([#4104](https://github.com/apache/incubator-tvm/pull/4104))
* Add `topi.nn.fifo_buffer` to TVM doc ([#4343](https://github.com/apache/incubator-tvm/pull/4343))
* License statement ([#4345](https://github.com/apache/incubator-tvm/pull/4345), [#4359](https://github.com/apache/incubator-tvm/pull/4359), [#4401](https://github.com/apache/incubator-tvm/pull/4401), [#4402](https://github.com/apache/incubator-tvm/pull/4402), [#4408](https://github.com/apache/incubator-tvm/pull/4408), [#4409](https://github.com/apache/incubator-tvm/pull/4409), [#4410](https://github.com/apache/incubator-tvm/pull/4410), [#4414](https://github.com/apache/incubator-tvm/pull/4414), [#4431](https://github.com/apache/incubator-tvm/pull/4431))

# Build and Test
* Increate the robuteness of CI test ([#2841](https://github.com/apache/incubator-tvm/pull/2841), [#2798](https://github.com/apache/incubator-tvm/pull/2798), [#2793](https://github.com/apache/incubator-tvm/pull/2793), [#2788](https://github.com/apache/incubator-tvm/pull/2788), [#2781](https://github.com/apache/incubator-tvm/pull/2781), [#2727](https://github.com/apache/incubator-tvm/pull/2727), [#2710](https://github.com/apache/incubator-tvm/pull/2710), [#2711](https://github.com/apache/incubator-tvm/pull/2711), [#2923](https://github.com/apache/incubator-tvm/pull/2923))
* Improve conda build ([#2742](https://github.com/apache/incubator-tvm/pull/2742)) 
* Add caffe2 nnvm frontend to CI ([#3018](https://github.com/apache/incubator-tvm/pull/3018))
* Use bridge network and expose port on macOS when launch docker image ([#3086](https://github.com/apache/incubator-tvm/pull/3086)）
* Run DarkNet tests ([#2673](https://github.com/apache/incubator-tvm/pull/2673)) 
* Add file type check ([#3116](https://github.com/apache/incubator-tvm/pull/3116))
* Always run cpptest during build to ensure library correctness ([#3147](https://github.com/apache/incubator-tvm/pull/3147))
* Handle more file types in ASF header ([#3235](https://github.com/apache/incubator-tvm/pull/3235))
* Add `test_forward_ssd_mobilenet_v1` to tflite/test_forward ([#3350](https://github.com/apache/incubator-tvm/pull/3350))
* Add Azure build pipeline ([#3458](https://github.com/apache/incubator-tvm/pull/3458), [#3459](https://github.com/apache/incubator-tvm/pull/3459))
* Update ci-gpu to v0.52 ([#3374](https://github.com/apache/incubator-tvm/pull/3374))
* Enable more visible symbols by default ([#3365](https://github.com/apache/incubator-tvm/pull/3365))
* Separate out legacy as a stage in CI ([#3337](https://github.com/apache/incubator-tvm/pull/3337))
* Simplify build script, remove python 2 support  ([#3419](https://github.com/apache/incubator-tvm/pull/3419))
* Ignore rust cargo lock files in rat ([#3314](https://github.com/apache/incubator-tvm/pull/3314))
* Improve CUDA Conda package build ([#3281](https://github.com/apache/incubator-tvm/pull/3281))
* Update CMakeLists.txt to be more flexible to find the third parties libraries ([#3354](https://github.com/apache/incubator-tvm/pull/3354))
* Docker update conda package ([#3344](https://github.com/apache/incubator-tvm/pull/3344)), requests and pillow ([#3495](https://github.com/apache/incubator-tvm/pull/3495)), Android demo ([#3499](https://github.com/apache/incubator-tvm/pull/3499)), rat install ([#3527](https://github.com/apache/incubator-tvm/pull/3527)), ARM support ([#3546](https://github.com/apache/incubator-tvm/pull/3546)), LLVM ([#3590](https://github.com/apache/incubator-tvm/pull/3590))
* Relay-to-Python testing ([#3156](https://github.com/apache/incubator-tvm/pull/3156))
* Code refactoring/remove ([#3523](https://github.com/apache/incubator-tvm/pull/3523), [#3667](https://github.com/apache/incubator-tvm/pull/3667))
* Zero-rank testing ([#3612](https://github.com/apache/incubator-tvm/pull/3612))
* CMake compilation ([#3611](https://github.com/apache/incubator-tvm/pull/3611), [#3650](https://github.com/apache/incubator-tvm/pull/3650), google test [#3628](https://github.com/apache/incubator-tvm/pull/3628))
* Standalone wheel build for TOPI ([#3657](https://github.com/apache/incubator-tvm/pull/3657))
* Fixing performance issues in PassUpDomain when fusing and splitting axes ([#3073](https://github.com/apache/incubator-tvm/pull/3073))
* conda recipe ([#3791](https://github.com/apache/incubator-tvm/pull/3791))
* Allow users to specify download directory ([#3803](https://github.com/apache/incubator-tvm/pull/3803))
* Update docs for installation for CUDA ([#3832](https://github.com/apache/incubator-tvm/pull/3832))
* Update hybrid_script.rst ([#3799](https://github.com/apache/incubator-tvm/pull/3799))
* Acknowledge Halide attributions ([#3824](https://github.com/apache/incubator-tvm/pull/3824))
* Add psutil dependency ([#3780](https://github.com/apache/incubator-tvm/pull/3780))
* Temporary disable rust test ([#3809](https://github.com/apache/incubator-tvm/pull/3809))
* Solve occasional CI issue when pad value is all 0 ([#3801](https://github.com/apache/incubator-tvm/pull/3801))
* Towards TSIM CI testing ([#3704](https://github.com/apache/incubator-tvm/pull/3704))
* Use pip3 for python3 ([#3742](https://github.com/apache/incubator-tvm/pull/3742))
* Update docker image `ci_cpu,i386` to include verilator ([#3738](https://github.com/apache/incubator-tvm/pull/3738))
* Remove sccache from Rust install ([#3728](https://github.com/apache/incubator-tvm/pull/3728))
* Update dmlc-core to the latest commit ([#3716](https://github.com/apache/incubator-tvm/pull/3716))
* Update GPU docker ([#3709](https://github.com/apache/incubator-tvm/pull/3709))
* Add an option to build with -pthread ([#3671](https://github.com/apache/incubator-tvm/pull/3671))
* Add DGL to `{ci_gpu, demo_cpu, demo_gpu}` docker images ([#3692](https://github.com/apache/incubator-tvm/pull/3692))
* Use pytest instead of nosetest ([#3524](https://github.com/apache/incubator-tvm/pull/3524))
* Enable NHWC of `relay.testing.mobilenet` ([#3886](https://github.com/apache/incubator-tvm/pull/3886))
* Add .hsaco save/load for tesnor_expr Tutorial ([#3852](https://github.com/apache/incubator-tvm/pull/3852))
* Support LLVM trunk ([#3907](https://github.com/apache/incubator-tvm/pull/3907))
* Remove GTest cmake flag from install docs ([#3953](https://github.com/apache/incubator-tvm/pull/3953))
* Allow `USE_LLVM` to take extra arguments ([#3954](https://github.com/apache/incubator-tvm/pull/3954))
* [CI] Pin NNPack pthreadtools version ([#4152](https://github.com/apache/incubator-tvm/pull/4152))
* [TOPI] Fix flaky testcase for check round ([#4211](https://github.com/apache/incubator-tvm/pull/4211))
* [CI] Move gpu docker binary to cuda10 ([#4229](https://github.com/apache/incubator-tvm/pull/4229))
* [CI] use llvm9 for the gpu tests ([#4224](https://github.com/apache/incubator-tvm/pull/4224))
* [CI] Update GPU docker to cuda10 ([#4228](https://github.com/apache/incubator-tvm/pull/4228))
* [Relay] Install Relay Prelude program in package install ([#4227](https://github.com/apache/incubator-tvm/pull/4227))
* [relay] use time_evaluator for measurement ([#4191](https://github.com/apache/incubator-tvm/pull/4191))
* [Relay] Improve build error when no lowered funcs are produced ([#4132](https://github.com/apache/incubator-tvm/pull/4132))
* [llvm] switch to use Align for llvm trunk ([#4051](https://github.com/apache/incubator-tvm/pull/4051))
* [CUDA] Update have_int8 condition to run on compute capability 7.x devices ([#4214](https://github.com/apache/incubator-tvm/pull/4214))
* [DOCKER] Pin torchvision==0.4.1 ([#4140](https://github.com/apache/incubator-tvm/pull/4140))
* [DOCKER] torch install depends on future package ([#4098](https://github.com/apache/incubator-tvm/pull/4098))
* [CodeGen] Disable -mfloat-abi hard option for LLVM < 6.0 ([#4071](https://github.com/apache/incubator-tvm/pull/4071))
* Add a python how to example of deploying tvm module with tvm runtime only ([#4094](https://github.com/apache/incubator-tvm/pull/4094))
* Hide symbols from dependent libraries if HIDE_PRIVATE_SYMBOLS is ON. ([#4041](https://github.com/apache/incubator-tvm/pull/4041))
* [BUILD] Disable utvm standalone runtime by default ([#4240](https://github.com/apache/incubator-tvm/pull/4240))
* Fix TSIM compile error in Linux (add missing -fPIC flag) ([#3876](https://github.com/apache/incubator-tvm/pull/3876))
* Add scalafmt and format existing scala codebase ([#3880](https://github.com/apache/incubator-tvm/pull/3880))
* Update TFLite wheel version to 1.13.1 ([#3435](https://github.com/apache/incubator-tvm/pull/3435))
* Remove PEP498 f-string new feature for support python3.5 ([#4250](https://github.com/apache/incubator-tvm/pull/4250))
* Require LLVM >= 9 for AMDGPU backend ([#4253](https://github.com/apache/incubator-tvm/pull/4253))
* Rename ml.dmlc.tvm to org.apache.tvm ([#4290](https://github.com/apache/incubator-tvm/pull/4290))
* [Test][TF][Relay] Fix argument preparation for vm test mode ([#4296](https://github.com/apache/incubator-tvm/pull/4296))
* Add test for the qnn_add operator ([#4282](https://github.com/apache/incubator-tvm/pull/4282))
* [CI][DOCKER] Add ONNX runtime dep ([#4314](https://github.com/apache/incubator-tvm/pull/4314))
* [CI][DOCKER] Upgrade image to include onnx runtime ([#4313](https://github.com/apache/incubator-tvm/pull/4313))
* [CI] Set workspace to be per executor ([#4336](https://github.com/apache/incubator-tvm/pull/4336))
* [Build][Windows] Fix Windows build by including cctype ([#4319](https://github.com/apache/incubator-tvm/pull/4336))
* [Contrib] Add MKL DNN option ([#4323](https://github.com/apache/incubator-tvm/pull/4323))
* [Test][Relay][Pass] Add test case for lambda lift ([#4317](https://github.com/apache/incubator-tvm/pull/4317))
* Remove Python imp module as it is deprecated ([#4275](https://github.com/apache/incubator-tvm/pull/4275))
* Bump up CUDA log version in tophub.py ([#4347](https://github.com/apache/incubator-tvm/pull/4347))
* Add rule for clean in APPs ([#4364](https://github.com/apache/incubator-tvm/pull/4364))
* [Relay tests] Temporary Attr Update for Order-Independent Testing ([#4357](https://github.com/apache/incubator-tvm/pull/4357))
* [CI] Avoid content-length request in test data download ([#4375](https://github.com/apache/incubator-tvm/pull/4375))
* Compare all outputs in TFLite `test_forward_ssd_mobilenet_v1` ([#4373](https://github.com/apache/incubator-tvm/pull/4373))

# Bug Fixes
* [RELAY] Fix `get_int_tuple`. ([#2691](https://github.com/apache/incubator-tvm/pull/2691))
* [ARITH] Select support for integer set analysis. ([#2687](https://github.com/apache/incubator-tvm/pull/2687))
* [Relay] Fix error in ANF (too agressively inline atomic expression and create free variable). ([#2665](https://github.com/apache/incubator-tvm/pull/2665))
* [Hybrid Script] Fix name conflict and attached scope problem. ([#2649](https://github.com/apache/incubator-tvm/pull/2649))
* [Relay] Fix ANF for reference and pattern matching. ([#2637](https://github.com/apache/incubator-tvm/pull/2637))
* [Relay] Fix fusion bug when call symbol that is not an operator. ([#2630](https://github.com/apache/incubator-tvm/pull/2630))
* Fix missing <sstream> header file. ([#2629](https://github.com/apache/incubator-tvm/pull/2629))
* [Relay]Fix the bug in heterogeneous annotation which mistakenly steps into the fused op. ([#2622](https://github.com/apache/incubator-tvm/pull/2622))
* [AutoTVM] Fix incorrect localhost usage in RPC mode. ([#2619](https://github.com/apache/incubator-tvm/pull/2619))
* [NNVM] Fix incorrectly getting layout attribute as a tuple. ([#2610](https://github.com/apache/incubator-tvm/pull/2610))
* [Relay] Fix mutating IF expression. ([#2601](https://github.com/apache/incubator-tvm/pull/2601))
* [Tutorial] Fix downloaded file path. ([#2590](https://github.com/apache/incubator-tvm/pull/2590))
* [Storage] Fix int32 overflow bug when input is big. ([#2580](https://github.com/apache/incubator-tvm/pull/2580))
* [NNVM] Fix non-identity problem for FInplaceIdentity. ([#2572](https://github.com/apache/incubator-tvm/pull/2572))
* [Golang] Fix compilation error. ([#2558](https://github.com/apache/incubator-tvm/pull/2558))
* [Tensor Expression] Fix missing reduction init predicates. ([#2495](https://github.com/apache/incubator-tvm/pull/2495))
* [Relay] Fix missing argument for NCHWc in Relay. ([#2627](https://github.com/apache/incubator-tvm/pull/2627))
* [TOPI] Fix Nms_ir data race. ([#2600](https://github.com/apache/incubator-tvm/pull/2600))
* Fix compute_inline with multiple outputs ([#2934](https://github.com/apache/incubator-tvm/pull/2934)) 
* [TEXPR][PASS] Fix thread all reduce to avoid write after read hazzard ([#2937](https://github.com/apache/incubator-tvm/pull/2937))
* [FRONTEND][TENSORFLOW] bug fix for tensorflow official slim models. ([#2864](https://github.com/apache/incubator-tvm/pull/2864))
* [FRONTEND][ONNX] Some bug fixes and Shape operator fixed for relay. ([#2850](https://github.com/apache/incubator-tvm/pull/2850))
* Turn on USE_SORT by default ([#2916](https://github.com/apache/incubator-tvm/pull/2916)) 
* [DOCKER] Upgrade ci-cpu to latest v0.50 ([#2901](https://github.com/apache/incubator-tvm/pull/2901)) 
* [TESTS] Import script robustness (set -u) ([#2896](https://github.com/apache/incubator-tvm/pull/2896)) 
* [Relay] Fix name of bias in testing.mlp ([#2892](https://github.com/apache/incubator-tvm/pull/2892)) 
* [TESTS] Improve script robustness ([#2893](https://github.com/apache/incubator-tvm/pull/2893))
* Add dense schedules to `__init__` for cpu ([#2855](https://github.com/apache/incubator-tvm/pull/2855))
* [Apps] [howto_deploy] fix cxx-flags order and build directory ([#2888](https://github.com/apache/incubator-tvm/pull/2888)) 
* [Relay] Add TVM_DLL for ANF/GNF conversion [#2883](https://github.com/apache/incubator-tvm/pull/2883) 
* [Relay] Fix Relay ARM CPU depthwise spatial pack schedule alter op layout issue. ([#2861](https://github.com/apache/incubator-tvm/pull/2861))
* Fix setting up hints for getaddrinfo ([#2872](https://github.com/apache/incubator-tvm/pull/2872)) 
* Add missing sgx includes ([#2878](https://github.com/apache/incubator-tvm/pull/2878)) 
* Fix error reporting for missing axis ([#2835](https://github.com/apache/incubator-tvm/pull/2835)) 
* Fix an OrderDict initilization bug. ([#2862](https://github.com/apache/incubator-tvm/pull/2862))
* Fix Xcode 10 metal compile error ([#2836](https://github.com/apache/incubator-tvm/pull/2836))
* tvmrpc: Fix includes ([#2825](https://github.com/apache/incubator-tvm/pull/2825)) 
* Fix `init_proj.py`: Team ID expected ([#2824](https://github.com/apache/incubator-tvm/pull/2824)) 
* [DOCKER] Fix git clone failure. ([#2816](https://github.com/apache/incubator-tvm/pull/2816)) 
* upgrade java style-check due to CVE-2019-9658 ([#2817](https://github.com/apache/incubator-tvm/pull/2817)) 
* [Relay][Quantization] Fix duplicated simulated quantization ([#2803](https://github.com/apache/incubator-tvm/pull/2803)) 
* [Bugfix] Repeat and tile bug fixed, relay tests added ([#2804](https://github.com/apache/incubator-tvm/pull/2804)) 
* Fix caffe2 relay frontend ([#2733](https://github.com/apache/incubator-tvm/pull/2733)) 
* Fix a bug in nnvm to relay converter. ([#2756](https://github.com/apache/incubator-tvm/pull/2756)) 
* Ensure loop count is a constant before trying to unroll. ([#2797](https://github.com/apache/incubator-tvm/pull/2797)) 
* xcode.py: Decode bytes before output [#2833](https://github.com/apache/incubator-tvm/pull/2833) 
* [WIN] Fix a bug in `find_llvm` when specify llvm-config ([#2758](https://github.com/apache/incubator-tvm/pull/2758)) 
* [DLPACK] fix flaky ctypes support ([#2759](https://github.com/apache/incubator-tvm/pull/2759)) 
* [Bugfix][Relay][Frontend] Fix bug in mxnet converter for slick_like ([#2744](https://github.com/apache/incubator-tvm/pull/2744))
* [DOCS] Fix tutorial ([#2724](https://github.com/apache/incubator-tvm/pull/2724)) 
* [TOPI][Relay] Fix default `out_dtype` for `conv2d_NCHWc` and Relay ([#2702](https://github.com/apache/incubator-tvm/pull/2702))
* [Relay] fix checkwellform ([#2705](https://github.com/apache/incubator-tvm/pull/2705)) 
 fix prelu, now can use on 2d input and add one test ([#2875](https://github.com/apache/incubator-tvm/pull/2875)) 
* [CODEGEN][OPENCL] Fix compile error about ternary expression. ([#2821](https://github.com/apache/incubator-tvm/pull/2821))
* Fix Placeholder issue ([#2834](https://github.com/apache/incubator-tvm/pull/2834))
* Fix makedirs() condition in contrib ([#2942](https://github.com/apache/incubator-tvm/pull/2942))
* Add missing #!/bin/bash directive ([#2951](https://github.com/apache/incubator-tvm/pull/2951))
* Bilinear resize bug fix from PR #2777 ([#2857](https://github.com/apache/incubator-tvm/pull/2857))
* Fix bias_add default axis ([#2829](https://github.com/apache/incubator-tvm/pull/2829))
* Remove empty ty.rs ([#2958](https://github.com/apache/incubator-tvm/pull/2958))
* fix undefined reference to dlopen, etc ([#2957](https://github.com/apache/incubator-tvm/pull/2957))
* Removed deprecated `std::unary_function` ([#2962](https://github.com/apache/incubator-tvm/pull/2962))
* Add output format to ndk build func ([#2999](https://github.com/apache/incubator-tvm/pull/2999))
* Fix java checkstyle version ([#2998](https://github.com/apache/incubator-tvm/pull/2998))
* Fix relay invariant error message ([#3011](https://github.com/apache/incubator-tvm/pull/3011))
* Fix for caffe2 nnvm frontend ([#2996](https://github.com/apache/incubator-tvm/pull/2996))
* Fix rust resnet example ([#3000](https://github.com/apache/incubator-tvm/pull/3000))
* Fix x||!x for comparisons in rewrite simplifier ([#3029](https://github.com/apache/incubator-tvm/pull/3029))
* Fix BatchMatMulRel typerelation ([#3032](https://github.com/apache/incubator-tvm/pull/3032))
* Update dmlc-core, fix default ctors of NodeEntry ([#3017](https://github.com/apache/incubator-tvm/pull/3017))
* Fix Fuse ([#3035](https://github.com/apache/incubator-tvm/pull/3035))
* Fix PostOrderVisit signature ([#3048](https://github.com/apache/incubator-tvm/pull/3048))
* Fix winograd nnpack fp16 ([#3046](https://github.com/apache/incubator-tvm/pull/3046))
* Fix some typos ([#3063](https://github.com/apache/incubator-tvm/pull/3063), [#3112](https://github.com/apache/incubator-tvm/pull/3112))
* Fix group_conv2d unit test ([#3113](https://github.com/apache/incubator-tvm/pull/3113))
* Fix bug in ONNX importer ([#3084](https://github.com/apache/incubator-tvm/pull/3084))
* Fixing a doc nit ([#3123](https://github.com/apache/incubator-tvm/pull/3123))
* Fix type code error for StringImm ([#3050](https://github.com/apache/incubator-tvm/pull/3050))
* Fix bug of wrongly generated device_map ([#2990](https://github.com/apache/incubator-tvm/pull/2990))
* use unordered_map instead of map in ANF ([#3024](https://github.com/apache/incubator-tvm/pull/3024))
* Fix PRelu layout in Relay ([#3013](https://github.com/apache/incubator-tvm/pull/3013))
* Minor addition to graph runtime debug ([#3129](https://github.com/apache/incubator-tvm/pull/3129))
* Fix mali conv2d performance regression ([#3131](https://github.com/apache/incubator-tvm/pull/3131))
* Fix dense autotvm template registration in ROCm ([#3136](https://github.com/apache/incubator-tvm/pull/3136))
* Fix `conv2d_transpose` ([#3138](https://github.com/apache/incubator-tvm/pull/3138))
* Fix python lint warnings ([#3145](https://github.com/apache/incubator-tvm/pull/3145))
* Some fixes for golang latest version compiler #3119 ([#3182](https://github.com/apache/incubator-tvm/pull/3182))
* Add more syncs to fix flaky test caused by `get_valid_counts` ([#3151](https://github.com/apache/incubator-tvm/pull/3151))
* Fix AlterLayout Pass ([#3155](https://github.com/apache/incubator-tvm/pull/3155))
* Fix a multithreaded bug in llvm LazyInitJIT ([#3158](https://github.com/apache/incubator-tvm/pull/3158))
* Fix a tensorflow test bug. ([#3165](https://github.com/apache/incubator-tvm/pull/3165))
* Fix concat for ARM ([#3061](https://github.com/apache/incubator-tvm/pull/3061))
* Handle vectorize for LE statement ([#3137](https://github.com/apache/incubator-tvm/pull/3137))
* Raise exception `group_conv2d_nchw` not supported ([#3195](https://github.com/apache/incubator-tvm/pull/3195))
* Quick fix of VTA FPGA Toolchain Installation documentation ([#3196](https://github.com/apache/incubator-tvm/pull/3196))
* Check file exists before removing it ([#3178](https://github.com/apache/incubator-tvm/pull/3178))
* Fix a bug of flatten in ONNX to Relay converter ([#3180](https://github.com/apache/incubator-tvm/pull/3180))
* Fix converter where initializers were not registered as nodes ([#3143](https://github.com/apache/incubator-tvm/pull/3143))
* Fix bug in cast to bool ([#3207](https://github.com/apache/incubator-tvm/pull/3207))
* Hotfix `build_module` creation ([#3198](https://github.com/apache/incubator-tvm/pull/3198))
* Fix sort changing original input data issue ([#3212](https://github.com/apache/incubator-tvm/pull/3212))
* Fix bug in vta runtime DepPop function ([#3208](https://github.com/apache/incubator-tvm/pull/3208))
* Fix resize nearest with fractional scaling ([#3244](https://github.com/apache/incubator-tvm/pull/3244))
* Fix `vta_conv2d` crash issue after change `vta_config.json` ([#3213](https://github.com/apache/incubator-tvm/pull/3213))
* Fix a memory leak in OpManager ([#3263](https://github.com/apache/incubator-tvm/pull/3263))
* PkgConfig cause crash in PYNQ board due to link library ([#3257](https://github.com/apache/incubator-tvm/pull/3257))
* Fix Error messages in tflite.py ([#3320](https://github.com/apache/incubator-tvm/pull/3320))
* Fix typos in docs and comments ([#3309](https://github.com/apache/incubator-tvm/pull/3309), [#3376](https://github.com/apache/incubator-tvm/pull/3376))
* Bugfix min/max const canonicalize rule ([#3386](https://github.com/apache/incubator-tvm/pull/3386))
* Return module from frontend for autotvm ([#3401](https://github.com/apache/incubator-tvm/pull/3401))
* Fix constant and reshape in ONNX ([#3387](https://github.com/apache/incubator-tvm/pull/3387))
* Default verilator location fix ([#3324](https://github.com/apache/incubator-tvm/pull/3324))
* Fix autodiff for conditional expression ([#3453](https://github.com/apache/incubator-tvm/pull/3453))
* Gramatical improvements to `tensor_expr_get_started` ([#3330](https://github.com/apache/incubator-tvm/pull/3330))
* Fix AutoTVM data structure bug ([#3462](https://github.com/apache/incubator-tvm/pull/3462))
* Fix MXNet RNN without providing state initialization as input ([#3326](https://github.com/apache/incubator-tvm/pull/3326))
* Fix flaky test on topk and quantize pass ([#3362](https://github.com/apache/incubator-tvm/pull/3362))
* Add VTA PYNQ metal_test bitstream program logic and fix compilation issue. ([#3400](https://github.com/apache/incubator-tvm/pull/3400))
* Fix VTA function Vivado Compile Error. ([#3375](https://github.com/apache/incubator-tvm/pull/3375))
* Fix VTA DRAM functionality issue. ([#3278](https://github.com/apache/incubator-tvm/pull/3278))
* Fix reshape precompute and type error in ONNX frontend ([#3230](https://github.com/apache/incubator-tvm/pull/3230))
* Fix interpreter argument conversion for tuples. ([#3349](https://github.com/apache/incubator-tvm/pull/3349))
* Fix code generation for packed functions + tuples in VM ([#3287](https://github.com/apache/incubator-tvm/pull/3287))
* Fix memory leak in Relay interpreter ([#3448](https://github.com/apache/incubator-tvm/pull/3448))
* Fix x86 depthwise conv2d `alter_op_layout` ([#3264](https://github.com/apache/incubator-tvm/pull/3264))
* Create closure object for GlobalVar ([#3411](https://github.com/apache/incubator-tvm/pull/3411))
* Fix getting global var in prelude ([#3405](https://github.com/apache/incubator-tvm/pull/3405))
* Fix rfactor bugs which related to predicate and loop partition ([#3382](https://github.com/apache/incubator-tvm/pull/3382), [#3444](https://github.com/apache/incubator-tvm/pull/3444))
* Fix the bug in AutoTVM where SimulatedAnnealingOptimizer sometimes finds useless candidate ([#3413](https://github.com/apache/incubator-tvm/pull/3413))
* Fix name conflict in PartialEval ([#3402](https://github.com/apache/incubator-tvm/pull/3402))
* Fix int bound analysis bug for modular ([#3288](https://github.com/apache/incubator-tvm/pull/3288))
* Check arg positiveness for modular rules ([#3279](https://github.com/apache/incubator-tvm/pull/3279))
* Fixes failure of `sum` and `all` on `axis=0` ([#3422](https://github.com/apache/incubator-tvm/pull/3422))
* Fix package path in tflite test ([#3427](https://github.com/apache/incubator-tvm/pull/3427))
* Fix Windows build ([#3429](https://github.com/apache/incubator-tvm/pull/3429))
* Fix `LSTMBlockCell` in Tensorflow frontend ([#3410](https://github.com/apache/incubator-tvm/pull/3410))
* TF fix where output index is ignored ([#3622](https://github.com/apache/incubator-tvm/pull/3622))
* Runtime fix for custom datatypes ([#3471](https://github.com/apache/incubator-tvm/pull/3471))
* Relay build module warnings ([#3452](https://github.com/apache/incubator-tvm/pull/3452))
* Relay partial evaluator ([#3482](https://github.com/apache/incubator-tvm/pull/3482))
* Pynq AutoTVM tracker ([#3497](https://github.com/apache/incubator-tvm/pull/3497), [#3578](https://github.com/apache/incubator-tvm/pull/3578))
* A normal form test ([#3525](https://github.com/apache/incubator-tvm/pull/3525))
* Lint issue ([#3519](https://github.com/apache/incubator-tvm/pull/3519), [#3615](https://github.com/apache/incubator-tvm/pull/3615) )
* Any shape testing ([#3528](https://github.com/apache/incubator-tvm/pull/3528))
* Android posix_memalign ([#3532](https://github.com/apache/incubator-tvm/pull/3532))
* Quantization add_rewrite and UnifyDTypeScale ([#3534](https://github.com/apache/incubator-tvm/pull/3534))
* Bound inference fix ([#3526](https://github.com/apache/incubator-tvm/pull/3526))
* Tensorflow NCHW data format ([#3514](https://github.com/apache/incubator-tvm/pull/3514))
* First order gradient ([#3550](https://github.com/apache/incubator-tvm/pull/3550))
* JS load module example ([#3556](https://github.com/apache/incubator-tvm/pull/3556))
* Build error ([#3552](https://github.com/apache/incubator-tvm/pull/3552))
* Relay VM debug statements ([#3565](https://github.com/apache/incubator-tvm/pull/3565))
* C++ lambda expr ([#3570](https://github.com/apache/incubator-tvm/pull/3570))
* Handling of tempdir if subprocess is killed ([#3574](https://github.com/apache/incubator-tvm/pull/3574))
* Remove tabs in Chisel source ([#3603](https://github.com/apache/incubator-tvm/pull/3603))
* Relay VM DataTypeObject ([#3604](https://github.com/apache/incubator-tvm/pull/3604))
* Removing prints ([#3616](https://github.com/apache/incubator-tvm/pull/3616))
* Average Pool2D Bug ([#3607](https://github.com/apache/incubator-tvm/pull/3607))
* Missing header in cuda_device_api.cc ([#3621](https://github.com/apache/incubator-tvm/pull/3621))
* Tensorflow frontend fix where output_shape is None ([#3632](https://github.com/apache/incubator-tvm/pull/3632))
* Winograd accuracy fix ([#3644](https://github.com/apache/incubator-tvm/pull/3644))
* Fix comment ([#3646](https://github.com/apache/incubator-tvm/pull/3646))
* Zero-input op fix for recursive traversals ([#3623](https://github.com/apache/incubator-tvm/pull/3623))
* Python 3.5 compatibility ([#3675](https://github.com/apache/incubator-tvm/pull/3675))
* Fix infinite recursive `device_api.ext_dev` call in VTA. ([#3843](https://github.com/apache/incubator-tvm/pull/3843))
* Fix depth_mult for TensorFlow frontend ([#3676](https://github.com/apache/incubator-tvm/pull/3676))
* Fix database APIs for AutoTVM ([#3821](https://github.com/apache/incubator-tvm/pull/3821))
* Fix axis of softmax in Keras ([#3834](https://github.com/apache/incubator-tvm/pull/3834))
* Fix VTA TensorLoad module ([#3841](https://github.com/apache/incubator-tvm/pull/3841))
* Fix inconsistent python/cpp API behavior for `if_then_else`, power ([#3829](https://github.com/apache/incubator-tvm/pull/3829))
* Fix code comment of operators in ONNX frontend ([#3830](https://github.com/apache/incubator-tvm/pull/3830))
* Added repo for llvm-9 to fix missing dependency issue ([#3826](https://github.com/apache/incubator-tvm/pull/3826))
* Fix typo in Relay text parser ([#3785](https://github.com/apache/incubator-tvm/pull/3785))
* Fix tvm const warnings ([#3817](https://github.com/apache/incubator-tvm/pull/3817))
* Add gfx906 bc ([#3808](https://github.com/apache/incubator-tvm/pull/3808))
* Fixed onnx test failures when run on a cpu backend ([#3764](https://github.com/apache/incubator-tvm/pull/3764))
* Fix ArgBinder assert order ([#3794](https://github.com/apache/incubator-tvm/pull/3794))
* Fix for NoneType Target for quantization ([#3792](https://github.com/apache/incubator-tvm/pull/3792))
* Fix out-of-date quantization realize ([#3790](https://github.com/apache/incubator-tvm/pull/3790))
* Fix Qnn concatenate InferType ([#3779](https://github.com/apache/incubator-tvm/pull/3779))
* Fix dense tuning ([#3768](https://github.com/apache/incubator-tvm/pull/3768))
* Fix `visit_pattern` in ExprMutator ([#3769](https://github.com/apache/incubator-tvm/pull/3769))
* Fix Chisel Scala style ([#3765](https://github.com/apache/incubator-tvm/pull/3765))
* Fix some pass docs ([#3767](https://github.com/apache/incubator-tvm/pull/3767))
* Fix mistype in rpc tutorial ([#3763](https://github.com/apache/incubator-tvm/pull/3763))
* Fix tvm.scan follow by tvm.compute segfault ([#3723](https://github.com/apache/incubator-tvm/pull/3723))
* Fix the potential index overflow in where operator ([#3751](https://github.com/apache/incubator-tvm/pull/3751))
* Revert `compile_cmd` kwarg name change ([#3746](https://github.com/apache/incubator-tvm/pull/3746))
* Update tophub ([#3752](https://github.com/apache/incubator-tvm/pull/3752))
* Fix typo in `ir_pass.h` ([#3741](https://github.com/apache/incubator-tvm/pull/3741))
* Bug fix for VME Shell ([#3737](https://github.com/apache/incubator-tvm/pull/3737))
* Fix missing apt https transport support ([#3735](https://github.com/apache/incubator-tvm/pull/3735))
* Take zero extent loops as NoOp and remove it ([#3724](https://github.com/apache/incubator-tvm/pull/3724))
* Fix mxnet converter for hybridblock and add `div_sqrt_dim` ([#3701](https://github.com/apache/incubator-tvm/pull/3701))
* Fix partial eval unit test name ([#3719](https://github.com/apache/incubator-tvm/pull/3719))
* Fix conv2d schedule code ([#3648](https://github.com/apache/incubator-tvm/issues/3648), [#3717](https://github.com/apache/incubator-tvm/pull/3717))
* Remove thread related headers ([#3713](https://github.com/apache/incubator-tvm/pull/3713))
* Fix FunctionPass ([#3712](https://github.com/apache/incubator-tvm/pull/3712))
* Export tvm::relay::OpRegistry::OpRegistry ([#3711](https://github.com/apache/incubator-tvm/pull/3711))
* Fix Metal reinterpret ([#3706](https://github.com/apache/incubator-tvm/pull/3706))
* Fix `gather_nd` in Relay ([#3442](https://github.com/apache/incubator-tvm/pull/3442))
* Fix error in partial evaluator ([#3693](https://github.com/apache/incubator-tvm/pull/3693))
* Align the naming rule for OpAttributeUnImplemented ([#3695](https://github.com/apache/incubator-tvm/pull/3695))
* Enable the sparse schedule ([#3651](https://github.com/apache/incubator-tvm/pull/3651))
* Fix typo names in Caffe2 frontend ([#3685](https://github.com/apache/incubator-tvm/pull/3685))
* Make tests multi-process friendly. ([#3683](https://github.com/apache/incubator-tvm/pull/3683))
* Fix typo in README.md ([#3684](https://github.com/apache/incubator-tvm/pull/3684))
* Fix doc rendering  ([#3897](https://github.com/apache/incubator-tvm/pull/3897))
* Add test script starter command to document ([#3993](https://github.com/apache/incubator-tvm/pull/3993))
* Add type solver unit tests for unifying quantified funcs ([#3947](https://github.com/apache/incubator-tvm/pull/3947))
* Change Vivado install instructions to version 2018.3 ([#4003](https://github.com/apache/incubator-tvm/pull/4003))
* Add a link to the defining network description of auto-tuning tutorial ([#4023](https://github.com/apache/incubator-tvm/pull/4023))
* Additional MXNet Convolution and Deconvolution tests ([#4026](https://github.com/apache/incubator-tvm/pull/4026))
* Adding support to check if an attribute is present or not without having to get the value ([#3957](https://github.com/apache/incubator-tvm/pull/3957))
* Fix parser for cast. ([#3873](https://github.com/apache/incubator-tvm/pull/3873))
* Fix operator fusion for multiple output ([#3871](https://github.com/apache/incubator-tvm/pull/3871))
* Remove extern C warpper for cuBLAS ([#3877](https://github.com/apache/incubator-tvm/pull/3877))
* Fix int32 range overflow by using int64 ([#3870](https://github.com/apache/incubator-tvm/pull/3870))
* Remove duplicate resize ([#3902](https://github.com/apache/incubator-tvm/pull/3902))
* Fix blas cmake for mac os ([#3898](https://github.com/apache/incubator-tvm/pull/3898))
* Add another MKL name alias for MKL installed through pypi ([#3853](https://github.com/apache/incubator-tvm/pull/3853))
* Numpy compatible dtype inference for `tvm.convert` and `tvm.const` ([#3861](https://github.com/apache/incubator-tvm/pull/3861))
* Remove incorrect check for LLVM in C codegen test ([#3921](https://github.com/apache/incubator-tvm/pull/3921))
* Fix exponential blowup in interpreter ([#3559](https://github.com/apache/incubator-tvm/pull/3559))
* Fix CUDA int8x4 vectorize ([#3928](https://github.com/apache/incubator-tvm/pull/3928))
* Make buffer auto broadcast independent to the order of input args ([#3956](https://github.com/apache/incubator-tvm/pull/3956))
* Fix benchmark layout in graph tuner ([#3926](https://github.com/apache/incubator-tvm/pull/3926))
* Fix Android Demo LLVM version ([#3962](https://github.com/apache/incubator-tvm/pull/3962))
* Cast filepath arguments to string ([#3968](https://github.com/apache/incubator-tvm/pull/3968))
* Fixes "common" sub crate using nightly and master ([#3965](https://github.com/apache/incubator-tvm/pull/3965))
* Changes to make tensorize work. These changes also fix the previously broken test. ([#3981](https://github.com/apache/incubator-tvm/pull/3981))
* Remove FLOP computation when calling 3rd party library ([#4005](https://github.com/apache/incubator-tvm/pull/4005))
* Use a more intuitive way to limit the #ops in a group ([#4018](https://github.com/apache/incubator-tvm/pull/4018))
* Add more `pad_mode` support for onnx converter ([#4029](https://github.com/apache/incubator-tvm/pull/4029))
* Impose a max op limit to the op fusion pass ([#4002](https://github.com/apache/incubator-tvm/pull/4002))
* Fixes issue with CPP enums ([#4019](https://github.com/apache/incubator-tvm/pull/4019))
* Int64 shape handling for outputs. ([#4031](https://github.com/apache/incubator-tvm/pull/4031))
* [PYTHON] Fix installation for generated grammar ([#4223](https://github.com/apache/incubator-tvm/pull/4223))
* [Bugfix] Fix target host for vm compiler ([#4057](https://github.com/apache/incubator-tvm/pull/4057))
* [Fix][VM] Fix VM invoke with set_params ([#4079](https://github.com/apache/incubator-tvm/pull/4079))
* [Fix] Fix a few bugs when dtype is fp16 ([#4088](https://github.com/apache/incubator-tvm/pull/4088))
* [Relay][Frontend][TF] Fix Size operator ([#4175](https://github.com/apache/incubator-tvm/pull/4175))
* [cmake][ANTLR] Support setting path to ANTLR jar ([#4176](https://github.com/apache/incubator-tvm/pull/4176))
* Fix infer type of kernel in dense. ([#4125](https://github.com/apache/incubator-tvm/pull/4125))
* [Relay] Fix match case in Python-side expr functor ([#4037](https://github.com/apache/incubator-tvm/pull/4037))
* Split adaptive_pool2d_avg into sum and div ([#4186](https://github.com/apache/incubator-tvm/pull/4186))
* [AutoTVM] Fix Split Factors when no_tail is off ([#4044](https://github.com/apache/incubator-tvm/pull/4044))
* Fix extent one for the `post_stmt` in loop partition ([#3734](https://github.com/apache/incubator-tvm/pull/3734))
* [TOPI] Fix bug in intel graphics auto tune ([#4093](https://github.com/apache/incubator-tvm/pull/4093))
* [ARITH] Fix lowering of `floormod(x, y) != 0` ([#4127](https://github.com/apache/incubator-tvm/pull/4127))
* [ARITH] Fix the rule `y < x && x <= y` ([#4220](https://github.com/apache/incubator-tvm/pull/4220))
* [Bugfix][TF] reset graph after getting tag of savedmodel ([#4055](https://github.com/apache/incubator-tvm/pull/4055))
* [Fix] Fix the logic of the number of nodes checking in op fusion ([#4074](https://github.com/apache/incubator-tvm/pull/4074))
* [VTA] hotfix for de10-nano driver ([#4081](https://github.com/apache/incubator-tvm/pull/4081))
* Fixing tensor not found issue in bitserial operator ([#4095](https://github.com/apache/incubator-tvm/pull/4095))
* Fix wrong `n_trial` number in autotvm tutorials' progress bar if `n_trial` is larger then config space. ([#4070](https://github.com/apache/incubator-tvm/pull/4070))
* [PATCH] Fix undefined `__floatdihf` in libtvmruntime.so on aarch64. ([#4119](https://github.com/apache/incubator-tvm/pull/4119))
* [ARITH] Fix lowering of FloorMod ([#4236](https://github.com/apache/incubator-tvm/pull/4236))
* [Relay][Frontend][Tensorflow] Fix GatherV2 ([#4238](https://github.com/apache/incubator-tvm/pull/4238))
* Fix typing.Deque import error for Python 3.5 ([#4254](https://github.com/apache/incubator-tvm/pull/4254))
* [VTA] Hotfix for padded load test in Chisel VTA ([#4264](https://github.com/apache/incubator-tvm/pull/4264))
* [Contrib] Fix error message at `callback_get_section_size()` ([#4221](https://github.com/apache/incubator-tvm/pull/4221))
* [TOPI] Fix bug in Winograd on CUDA ([#4260](https://github.com/apache/incubator-tvm/pull/4260))
* AutoTVM: Fix hang/crash issues on feature extraction ([#3689](https://github.com/apache/incubator-tvm/pull/3689))
* [TOPI][CUDA] Fix Winograd Kernel Size Support ([#4276](https://github.com/apache/incubator-tvm/pull/4276))
* [Relay][Frontend][Tensorflow] Fix type assignment for 'tf.range' operator ([#4294](https://github.com/apache/incubator-tvm/pull/4294))
* Fix incorrect call to Unicode Win32 InetPton ([#4306](https://github.com/apache/incubator-tvm/pull/4306))
* [Relay][Frontend][Keras] handle `batch_norm` op params well ([#4310](https://github.com/apache/incubator-tvm/pull/4310))
* [VTA] fix error when `memory_id` is `VTA_MEM_ID_OUT` ([#4330](https://github.com/apache/incubator-tvm/pull/4330))
* [Doc][fix] fix sphinx parsing for pass infra tutorial ([#4337](https://github.com/apache/incubator-tvm/pull/4337))
* [Codegen] remove fp16 function override for cuda ([#4331](https://github.com/apache/incubator-tvm/pull/4331))
* [TFLite] Fix Prelu unified shape error ([#4326](https://github.com/apache/incubator-tvm/pull/4326))
* [Relay][Frontend][TF] Fix transpose when axes is not a param ([#4327](https://github.com/apache/incubator-tvm/pull/4327))
* [VTA] Bug fix for padded load with large inputs ([#4293](https://github.com/apache/incubator-tvm/pull/4293))
* Fix inconsistent operator tag name ([#4134](https://github.com/apache/incubator-tvm/pull/4134))
* Fix for a specific case when loop partitioning with indivisble. ([#4243](https://github.com/apache/incubator-tvm/pull/4243))
* Send list as argument to `schedule_conv2d` ([#4358](https://github.com/apache/incubator-tvm/pull/4358))
* [Docker] Fix TVM folder name for installing on Android and OpenCL. ([#4363](https://github.com/apache/incubator-tvm/pull/4363))
* Fix TFLite Reshape assert ([#4320](https://github.com/apache/incubator-tvm/pull/4320))
* [Relay][Frontend][TF] Fix slice when begin or size is not Const ([#4372](https://github.com/apache/incubator-tvm/pull/4372))
* Fix compilaton of bfloat16 on Windows ([#4415](https://github.com/apache/incubator-tvm/pull/4415))

# Known Issues

* The performance of Relay VM is not good enough on GPU, due to memeory allocation overhead which will be resolved later.
* TFlite rounding vs tvm rounding causing differences in accuracy and potentially off by 1 errors. For reference [#3900](https://github.com/apache/incubator-tvm/pull/3900#discussion_r334324818)
* TFlite pre-quantized network support is still a work in progress and the project would welcome further contributions.
* TSIM build requires `python` command exist on the host. See [forum discussion](https://discuss.tvm.ai/t/vta-build-failure/4790) for details.
* Tensorflow control flow has not been fully supported in the frontend converter.
* `topi.floor_div` is inconsistent with floor division semantic when result number is close to an integer.


# Deprecation
* Deprecating python2 support in the master branch and following release (v0.6). ([#2994](https://github.com/apache/incubator-tvm/issues/2994), [#2986](https://github.com/apache/incubator-tvm/issues/2986))
* NNVM is deprecated and will be removed in a future version. ([#4333](https://github.com/apache/incubator-tvm/issues/4333), [#4368](https://github.com/apache/incubator-tvm/issues/4368))

## v0.6.1 (2020-07-10)

Apache TVM (incubating) is an effort undergoing incubation at The Apache Software Foundation (ASF), sponsored by the Apache Incubator PMC.

Incubation is required of all newly accepted projects until a further review indicates that the infrastructure, communications, and decision making process have stabilized in a manner consistent with other successful ASF projects.

While incubation status is not necessarily a reflection of the completeness or stability of the code, it does indicate that the project has yet to be fully endorsed by the ASF.

Apache TVM (incubating) 0.6.1 is a maintenance release incorporating important bug fixes and important performance improvements. All users of Apache TVM (incubating) 0.6.0 are advised to upgrade. Please review following release notes to learn the bug fixes.

# Bug Fixes

* Fixed process termination routine in windows #4844
* [Runtime] Fix NDArray SaveDLTensor declaration and implementation signature different #4586
* [NODE][Serialization]fix serialization precision loss in float #4503
* [Relay][Frontend][TF] fix _parse_param bug #4711
* Fix bias_add gradient #4516
* Make sure to visit the arguments of inlined functions #4783
* Fix Python syntax error in start_rpc_server_to_tracker.py #4682
* [Bugfix] Fixed crash caused by reversing bitwise operations #4852
* [Fix][VM] Fix copy constructor #5237
* fix small bug about dense_grad #5695
* [Fix] Fix conv2d alter op for arm cpu #5532
* [Fix] Fix dense x86 schedule #4728
* [Relay][Fix] Fix alter op layout when calling a global var #4454
* [Relay][Pass] Fix lambda lift pass for recursive call #4432
* [BUGFIX] Fix search path for libtvm_topi.so #4467
* [Bugfix] Fix Python debugger segfaults with TVM built with LLVM #5685
* [RUNTIME] Fix compile errors of OpenCL FPGA backend #4492
* [BUGFIX][BACKPORT-0.6][ARITH] Fix FloorMod Simplifier #5509
* Some Windows and MSVC fixes #4569
* [Chisel][VTA] Fix multiple transfer issue in LoadUop module #4442
* [VTA] Fix an issue in updating uop_idx in the TensorGemm module #4694
* [VTA] Fixed a crash issue in TSIM driver #4527
* [VTA] Enable streamlined GEMM execution #4392
* [VTA][Chisel] End-to-end Inference with Chisel VTA #4574
* Added declare of aluBits for TensorAlu #4624
* [Quantization] Fix annotation for multiply op #4458
* LRN only supports 4D tensors, remove it from alter_op_layout #5520
* fix topi.nn.global_pool layout="NHWC" #4656
* [FFI][Windows] Fix hasattr by extracting Python error type from Windows error message #4780
* [Runtime] Export GraphRuntime in tvm_runtime.dll #5002
* Fix Base64OutStream portability issue #4668
* [AUTOTVM] Fix a bug in generating the search space #4779
* [Relay][VM] Fix compilation of If-Elses #5040
* [RELAY][FRONTEND][TENSORFLOW] Fix FuseBatchNorm output cast error if need_cast is True #4894
* [Bugfix] fskip of EliminateCommonSubexpr cannot always return false #4620
* [Fix] Add ConstantNode to IsAtomic #5457
* [Fix] Fix RemoveUnusedFunctions pass #4700
* [Realy][fix] Fix alpha_equal bug for attribute check #4897
* [Arith] keep div_mode during floordiv simplify #5922
* [ARITH][BACKPORT-0.6] fix a min/max simplify bug #5761
* [0.6-BACKPORT] Improve robustness of the docs build #5583

## v0.7.0 (2020-10-02)

Apache TVM (incubating) is an effort undergoing incubation at The Apache Software Foundation (ASF), sponsored by the Apache Incubator PMC.

Incubation is required of all newly accepted projects until a further review indicates that the infrastructure, communications, and decision making process have stabilized in a manner consistent with other successful ASF projects.

While incubation status is not necessarily a reflection of the completeness or stability of the code, it does indicate that the project has yet to be fully endorsed by the ASF.

# Introduction
v0.7 brings many major features. The community works together to refactor the internal code base to bring an unified IR code structure with unified IRModule, type system and pass infrastructure. We have also bought many exciting new features, some highlights include:

* Initial automatic scheduling support
* Initial command line driver interface
* WebGPU and webassembly support
* Better first class rust support in the codebase
* Intial Hexagon support
* Bring your own codegen (BYOC) support

The community also continues to bring high quality improvements to the existing modules including, but not limited to: better frontend coverage, performance, quantization, uTVM and dynamic shape support.

# New Features
## Automatic Scheduling (Experimental)
* Phase 0: Ansor minimum system for auto schedule generating #5962
* Phase 1: Access Analyzer #6103
* Phase 1: Add `follow_split` and `follow_fused_split` steps #6142
* Phase 1: Add `pragma`/`storage_align`/`rfactor` steps #6141
* Phase 1: Add RPC Runner #6077
* Phase 1: Add `annotation`/`compute_at`/`compute_root`/`compute_inline` steps #6073
* Phase 1: Add `cache_read`/`cache_write` steps #6107
* Phase 1: Rename namspace form `auto_schedule` to `auto_scheduler` #6059
* Phase 1: The base class for cost models #6187
* Phase 1: feature extraction for cost models #6190
* Phase 1: XGBoost Cost Model #6270
* Phase 2: Basic GPU Sketch Search Policy #6269
* Phase 2: Evolutionary Search #6310
* Phase 2: Update heavy operations with `parallel_for` #6348
* Parallel the InitPopulation (#6512)
* Tutorial: Using the template-free auto-scheduler on CPU (#6488)

## BYOC
* External codegen support in Relay (#4482)，(#4544)
* Bring Your Own Codegen Guide -- Part 1 #4602
* Bring Your Own Codegen Guide -- Part 2 #4718
* Relay annotation and partitioning for external compilers #4570
* JSON Runtime with DNNL End-to-End Flow #5919
* Handle one symbol for each runtime #5989
* Run accelerator specific optimizations #6068
* Arm Compute Library integration #5915
* Retire the example json runtime #6177
* `json_node.h` should include `data_type.h` #6224
* Improve installation tutorial #6170
* Add support for dense (fully connected) layer #6254
* Introduce the Ethos-N BYOC integration #6222
* Enable remote device via environment variables #6279
* Improved pooling support #6248
* Add support for quantized convolution #6335
* CoreML codegen #5634

## Operator Coverage
* Add `strided_set` operation (#4303)
* Add support for conv3d (#4400), pool3d (#4478), 3d upsampling ops (#4584)
* Add group convolution for VTA (#4421)
* Add 1d deconvolution op (#4476)
* Allow batch matmul to be fused into injective ops (#4537)
* Add native depthtospace and spacetodepth operators (#4566)
* Add CUDNN conv3d support (#4418)
* Dilation2D operator support #5033
* Isfinite operator #4981
* Unravel Index operator #5082
* Add thrust support for nms #5116
* Resize3d, Upsample3d op support #5633
* Add operator Correlation #5628
* `affine_grid` and `grid_sample` #5657
* Sparse to dense operator #5447
* `Conv3d_transpose` op support added #5737
* add op `crop_and_resize` #4417
* Add bitwise ops #4815
* Sparse to dense operator #5447
* support dynamic NMS(Non Maximum Suppression), symbolic begin, end, and strides for strided_slice #4312
* `Conv3d_transpose` op support added #5737
* ReverseSequence operator #5495
* Conv1D #4639
* 1D Pooling #4663

## Quantization
* Channel wise quantization - Quantize & Requantize #4629
* Support QNN ops. #5066
* Adding support for QNN subtract op #5153
* TFLite QNN Tutorial #5595
* Tutorial: Deploy Quantized Model on CUDA #4667
* Support asymmetric per-layer quantized operators #6109

## Relay
* Add convertlayout pass in Relay (#4335, #4600)
* Added Merge Composite pass #4771
* Call graph for relay #4922
* Add inline pass #4927
* Target annotation for external codegen #4933
* GradientCell Relay Pass #5039
* Add MergeCompilerRegions pass #5134
* Non-recursive Graph Vistor and Rewriter (#4886)
* [Blocksparse] Pipeline for lowering dense model to sparse-dense (#5377)
* Relay op strategy #4644
* Static Tensor Array (#5103)
* Memory planner (part 1) #5144
* ONNX codegen #5052
* Add Parser 2.0 #5932, part 2 #6162
* Basic block normal form #6152
* Convert Layout pass. #4664
* Pattern Language, Matcher, Rewriter, and Function Paritioner #5231

## Runtime and Backend
* Add ADTObject POD container type (#4346)
* TFLite RPC runtime (#4439)
* Standardized graph runtime export (#4532)
* MISRA-C compliant TVM runtime #3934
* Add String container #4628
* Introduce Virtual Memory Allocator to CRT (#5124)
* Initial implementation of Hexagon runtime support (#5252)
* FastRPC interface for Hexagon runtime (#5353)
* CoreML Runtime (#5283)
* AutoTVM + uTVM for Cortex-M7 (#5417)
* Windows Support for cpp_rpc (#4857)
* Implement TVMDSOOp(TensorFlow custom op) for TVM runtime (#4459)
* WebGPU support #5545
* TVM WebAssembly JS Runtime #5506
* Hexagon driver for offloading kernels to simulator #5492
* Introduce runtime::Array #5585
* Allow non-nullable ObjectRef, introduce Optional. (#5314)
* Introduce static slots for common objects. (#5423)
* ntroduce RValue reference(move) support to TypedPackedFunc (#5271)
* Introduce MetadataModule to separate code compilation/interpretation and weight initialization #5770
* Support module based interface runtime #5753
* Add TVM application extension with WASM runtime #5892
* Provide guide to user who has difficulty register SEqualReduce (#5300)

## Rust Support
* Revive the Rust + SGX refactor #4976
* Improve Rust bindings: Map, Array, String, various IR nodes #6339
* Rust Refactor Stage 4: Rewrite Rust graph runtime to use new APIs #5830
* Second stage of Rust Refactor #5527
* tvm crate stage 3 of Rust refactor #5769
* Add first stage of updating and rewriting Rust bindings. #5526

## TIR
* Introduce StructuralHash for the Unified IR. #5160
* Introduce StructuralEqual Infra for the unified IR. #5154
* Introduce ExprDeepEqual, Remove IRDeepCompare #5206
* [TIR] Introduce BufferLoad/Store (#5205)
* Improved massive build times caused by tir.floormod and tir.floordiv. Fixed Topi testcase. #5666
* Buffer logger assert removed #6147
* Enhance VerifyGPUCode #6194
* HoistIfThenElse added #6066
* Hybrid Script Support for TIR #6227
* Migrate Low-level Passes to Pass Manager #5198
* HoistIfThenElse added #6066
* Hybrid Script Support for TIR #6227
* Block scope hoisting added #6238

## TE
* reverse-mode autodiff without any optimization #5121
* Tensor Expression Debug Display (TEDD) #4651
* Optimize and eliminate the Jacobian tensor for te.autodiff #6078

## TVMC(Experimental)
* TVMC - A command line driver for TVM (Part 1) #6112
* TVMC - Linting error on onnx command line driver frontend #6536
* TVMC - Command line driver 'compile' (part 2/4) #6302
* TVMC - Introduce 'tune' subcommand (part 3/4) #6537
* TVMC - Introduce 'run' subcommand (part 4/4) #6578
* TVMC - Getting started tutorial for TVMC #6597


# Feature Improvement
## Accelerator and Microcontroller Support
- Cleanup legacy verilog code (#4576)
- uTVM support for ARM STM32F746XX boards (#4274)
- Add --runtime=c, remove `micro_dev` target, enable LLVM backend #6145

## Arithmetic Analysis
* Linear system and equation solver (#5171)
* Inequalities solver #5618
* Improve IntervalSet's floormod (#5367)
* Remove legacy const pattern functions (#5387)
* Handle likely in IRMutatorWithAnalyzer #5665
* ExtendedEuclidean merge impl to int_operator #5625
* Rewrite simplify fix for Vectorized Cooperative Fetching #5924

## AutoTVM and Graph Tuner
* Adding ROCM schedules for TOPI (#4507)
* NHWC conv2d schedule templates for ARM (#3859)
* Use VM compile to extract autotvm tasks #4328
* Download fallback schedule file if it does not exist #4671
* Ignore error when removing tmpdir #4781
* Fix a bug in generating the search space #4779
* Minor bug fixes in AutoTVM for QNN graphs #4797
* Fix autotvm customized template #5034
* Add opt out operator for `has_multiple_inputs` for graph tuner #5000
* Customize SI prefix in logging (#5411)
* Update XGBoost verbosity option #5649
* Support range in index based tuners #4870
* Enable random fill and CPU cache flush for AutoTVM and Ansor (#6391)
* Auto-scheduler tutorial for GPU and necessary refactor/fix (#6512)

## BYOC
* [BYOC] Bind constant tuples in graph partitioner (#5476)
* [BYOC] Add support for composite functions in BYOC (#5261)
* [BYOC] Register pattern tables from external codegens (#5262)
* [BYOC] Enhance partitioning and external codegen (#5310)
* [BYOC] Refine AnnotateTarget and MergeCompilerRegion Passes (#5277)
* [BYOC] Use Non-Recursive Visitor/Mutator (#5410)
* [BYOC] Refine DNNL Codegen (#5288)
* [BYOC] Add example of Composite + Annotate for DNNL fused op (#5272)
* [BYOC] Prevent duplicate outputs in subgraph Tuple (#5320)
* [BYOC] Introduce further operator support (#6355)
* [BYOC] Support input nodes with multiple entries (#6368)
* [BYOC] Add maximum support for float32 (#6506)

## Codegen
* Intrinsic dispatching with OCML instead of LLVM for ROCm (#4499)
* Make target codegen take IRModule and PrimFunc. #5107
* Enhance CUDA codegen for SelectNode #4983
* Vectorization for intrinsics #5101
* [LLVM] Do not use `x86_vcvtph2ps_256` intrinsic with LLVM 11+ (#5267)
* [LLVM] Use llvm::ElementCount with LLVM 11+ when creating vectors (#5265)
* [LLVM] Use llvm::FunctionCallee in IRBuilder::CreateCall with LLVM 11+ (#5338)
* [LLVM] Include Support/Host.h for declaration of getDefaultTargetTriple (#5268)
* [LLVM] Replace calls to Type::getVectorNumElements (#5398)
* [LLVM] Use ArrayRef in calls to CreateShuffleVector (#5399)
* [LLVM] Use llvm::Align with LLVM 11+ to avoid warnings (#5264)
* [CodeGen] Cleanup generated code (#5424)
* Rename `target_id` => `target_kind` #6199
* 64-bit RPi4b target #6211
* Creating Target from JSON-like Configuration #6218
* Add python binding to new JSON target construction #6315
* Use target class in all codegens #6347
* Initial support for Hexagon codegen #6261
* Add --runtime=c, remove `micro_dev` target, enable LLVM backend #6145
* Add tvm::support::hexdump() debug utility #6154
* Adding AMD codegen unit tests (#4509)
* Support cuda tensorcore subbyte int data type in auto tensorcore #4546
* Handle empty LLVMModule in GetFunction #5146
* Support int4/int8 conv2d tensor core with HWNC layout #6121

## Dynamism Support
* Add shape function for `zero`, `zeros_like`, `ones`, `ones_like` (#4448), `tile` (#4441)
* Support symbolic newshape for Reshape #5429
* Support symbolic TopK, Ones, Zeros and Full #5459
* Add `shape_of` instruction #5855
* symbolic `max_output_size` #5844
* Dynamic TopK Op #6008
* Dynamic `broadcast_to`, `zeros`, `ones` #6007
* Add dynamic reshape grad #6080
* Keep fixed dim when unifying dynamic shape #5795
* OneHot operation #6209
* Add Dynamic Resize Op #6198
* Dynamic full operator #6260
* Dynamic upsampling relay op #6273
* Dynamic Tile Op #5983

## Frontend and User Interface
* TFLite parser support for `transpose_conv` (#4440), `unpack` (#4447)
* LLDB pretty printers for relay (#4453)
* ONNX to Relay converter op support: expand op (#4483)
* ONNX `auto_pad` in conv and convtranspose (#4563)
* TF to Relay converter op support (#4504) (#4551) (#4484)
* Remove unnecessary cast of constants in ONNX converter (#4573)
* Add support for tf.Keras networks in Relay Keras frontend #4630
* Add conv3d #4604
* Fix incorrect calculations in tf SLICE #4518
* Dynamically calculate `input_stats` of any `fake_quant` range #4789
* LSTM Support #4825
* Add `MIRROR_PAD` operator #4822
* use qnn helper function in softmax #4840
* Add Resize op converter #4838
* Add support for `TFLite_Detection_PostProcess` #4543
* Fix tests for tflite unary elemwise operations #4913
* GaussianDropout/Noise parsing support #4928
* Add parser support for 'square' operator #4915
* `make_loss` operator support #4930
* Add parser support for `l2_normalization` #4966
* ReadVariableOp operator support #4952
* Check graph inputs match expected #4992
* support multiply outputs #4980
* TFLite: Using real image for QNN testing. #4816
* TFLite: `FLOOR_MOD` & `FLOOR_DIV` support #4971
* PyTorch: Upsampling op support and enable registering a user defined op conversion map #4961
* PyTorch: fix unordered dictionary problem for python version under 3.6 #4982
* Operator support NonZero #5073
* Upsampling op support and enable registering a user defined op conversion map #4961
* Check graph inputs match expected #4992
* Add support for quantized models via QNN #4977
* Add initial control flow support #4964
* Remove FP32 piggy back and use QNN add/mul/concatenate #5061
* Add missing upcast to uint8 `avg_pool` conversion #5089
* Add initial 3D op support and test on Resnet 3D #5075
* Fix conv2d conversion for group conv (group > 1 but != in channels) #5132
* Add support for `max_pool1d` #5142
* Add support for split #5174
* `FLOOR_MOD` & `FLOOR_DIV` support #4971
* Activation functions support #4978
* Round op parsing support added #5022
* DepthToSpace and SpaceToDepth support #5041
* `TOP_K` op parser support #5051
* ReadVariableOp operator support #4952
* Support multiply outputs #4980
* `reduce_any` op parsing support #4926
* TensorFlow Parser Control Flow Enhancement #5020
* TensorFlow Frontend support with shared params #5042
* Support for AddV2 in Relay Tensorflow frontend converter. #5046
* conv3d frontend operator support #5080
* `max_pool3d` and Averagepool3d operator support #5085
* Support for Atan/Atan2 in Relay Tensorflow frontend converter. #5104
* Use leaky by default for LeakyReLU #5192
* Conv3D ONNX support and `conv3D_ncdhw` x86 schedules #4949
* Add support for FusedBatchNormV3 #5065
* Activations for pytorch #5194
* Dropouts And InstanceNorm support added #5203
* [Frontend] Asymmetric padding of convolution support (#4803)
* [ONNX]Pool3d & upsample3d op support (#5135)
* Add TopK to ONNX Frontend (#5441)
* Add RoiAlign to Onnx frontend (#5454)
* [PYTORCH]AvgPool3d, MaxPool3d and Squeeze op support (#5220)
* [PYTORCH]celu, gelu, selu activations (#5263)
* [Pytorch]layernorm bug fix and testcase updated (#5257)
* [PYTORCH]LayerNorm support added (#5249)
* [PYTORCH]GroupNorm op support added (#5358)
* [PYTORCH]Logical & Bitwise operator support (#5341)
* [PYTORCH]Tensor creation ops support (#5347)
* [PYTORCH]cosh,sinh,log2,log10,log1p op support (#5395)
* [PYTORCH]Rsub, Embedded, OneHot ops support (#5434)
* [PYTORCH]Abs, Arange, Softplus ops (#5295)
* [PYTORCH]isNan, isinf, isfinite, ceil, clamp, round ops (#5316)
* [PYTORCH]Activations for pytorch (#5194)
* [PYTORCH]Repeat, Reciprocal & Reshape Op support (#5280)
* [PYTORCH]`Reduce_ops` support added (#5308)
* [PYTORCH]Take, Topk op support (#5332)
* [PYTORCH]Dropouts And InstanceNorm support added (#5203)
* [PYTORCH]Unary Ops frontend support. (#5378)
* [Torch] Support Python list, more realistic recurrent networks (#5306)
* [PYTORCH]where, addcdiv, addcmul op support (#5383)
* [Torch] Add support for split (#5174)
* [Torch] Fix up graph input handling (#5204)
* [TFLITE]Logical not op support (#5475)
* [TFLITE]Hard Swish & MobilnetV3 model testing (#5239)
* [TFLITE]Gather, StridedSlice op support added (#4788)
* [TFLITE] Match TFLite shape for SSD custom op (#5473)
* Factor out import of common tflite.Operator in tflite frontend. (#5355)
* [TFLite] support for FILL and `SPLIT_V` operators (#5330)
* [TFLite] `L2_POOL_2D` operator (#5452)
* [TFLite] Add config option to specify FlatBuffers location (#5425)
* [TFLITE]Logical not op support (#5475)
* [TENSORFLOW]reduce ops updated (#5180)
* [TENSORFLOW] Fix `gather_nd` indices (#5279)
* [TensorFlow]Improve TensorFlow Static Shape Tensor Array (#5243)
* [KERAS]Minimum & AlphaDropout op support (#5380)
* [KERAS]Embedding layer (#5444)
* [KERAS]`Max_pool3d` and Averagepool3d operator support (#5085)
* [CAFFE2]add Mul and ConvTranspose operator (#5302)
* [MXNET]DepthToSpace & SpaceToDepth Operator (#5408)
* [MXNET]broadcast and logical op support (#5461)
* [MXNET] Use leaky by default for LeakyReLU (#5192)
* [MXNET] support elemwise logic ops (#5361)
* [Frontend|MXNet] SwapAxis operator support (#5246)
* [RELAY] Move frontend utils (#5345)
* [Pytorch] Fix translation of transpose when axis argument is as a list (#5451)
* LpPool Support added #5696
* Skip ADD inside Gemm op when vector is zero #5697
* ReduceL1, ReduceL2, ReduceSumSquare, ReduceLogSum ops added #5721
* MaxRoiPool, Mod & Xor op support added #5729
* Skip multiply with 1.0f constant for GEMM import #5800
* StatefulPartitionedCall/PartitionedCall Ops support added #5617
* Don't add cast for batch norm when type isn't changing #5731
* Conv3d Transpose OP added #5775
* expand bug fix #5576
* Support `max_pool2d_with_indices` #5549
* Add prim::device op #5584
* ImplicitTensorToNum support added #5603
* Matmul fix for `batch_matmul` #5604
* ReflectionPad2d op #5624
* Padding op support #5638
* Minor bug fixes #5683
* `floor_divide` support for squeezenet #5702
* ReplicationPad support added #5708
* aten::norm support added #5776
* broadcast and logical op support #5461
* MaxPool3d and AvgPool3d Ops support added #5614
* Softmin, trunc op support added #5715
* conv3d and `conv3d_transpose` addedx #5814
* Model importer to be compatible with tflite 2.1.0 #5497
* Nit: Function names made consistent #5515
* Select op support for tflite frontend #5486
* `GATHER_ND` #5508
* Quantize & Dequantize op #5394
* Fully connected op conversion made in sync with TFLite #5510
* `ADD_N` operator #5474
* onnx, mxnet, pytorch mathops added #5561
* abs, round, reciprocal, sign, softsign, `hard_sigmoid` ops support #5587
* Gather nd bug fix for one dim support in tensorflow #5588
* Add parser support for shape and range #5329
* Darknet support batch size for yolo #5688
* Improve Control Flow and TensorArray #5699
* MXNet: Softmin, trunc op support added #5715
* MXNet: conv3d and `conv3d_transpose` addedx #5814
* MXNet: Add parser for `contrib.box_decode` #5967
* Onnx: ReduceL1, ReduceL2, ReduceSumSquare, ReduceLogSum ops added #5721
* Onnx: MaxRoiPool, Mod & Xor op support added #5729
* Onnx: Skip multiply with 1.0f constant for GEMM import #5800
* Onnx: Fix an issue with #5755 and add Batch norm unit tests. #5845
* TensorFlow: StatefulPartitionedCall/PartitionedCall Ops support added #5617
* TensorFlow: Don’t add cast for batch norm when type isn’t changing #5731
* TensorFlow: Conv3d Transpose OP added #5775
* Add parser support for shape and range #5329
* Darknet support batch size for yolo #5688
* Improve Control Flow and TensorArray #5699
* Improve TF Parser to keep output nodes for `saved_model` #5794
* Add parser support for `relu6`, `leaky_relu`, `relu_n1_to_1`, `log_softmax` #4805
* Fix TF Dynamic input shape #5825
* Support a few contrib ops in mxnet #5819
* Improve TF Parser to keep output nodes for `saved_model` #5794
* Add parser support for `relu6`, `leaky_relu`, `relu_n1_to_1`, `log_softmax` #4805
* Check all unsupported ops before raising an exception #5929
* Add Pytorch advanced indexing #6318
* Support `index_select` #6295
* Fix cast to long #6301
* Fix dtype handling for modules with integer parameters #6311
* pytorch frontend support conv1d #6203
* Add cast to double, fix flatten conversion #6357
* Fix aten::max and aten::min conversion #6372
* Match pytorch 1.6 googlenet pretrained model (#6201) #6212Add unbiased variance op and corresponding support in pytorch frontend #6232
* Implemented PADV2 Operator for TFLite and added support for constant values in PAD. #6167
* Implemented `ONE_HOT` Operator for TFLite. #6223
* Implemented `EXPAND_DIMS` Operator for TFLite. #6243
* Implemented `REVERSE_V2` Operator for TFLite. #6304
* Implemented `MATRIX_SET_DIAG` Operator for Relay/TOPI and TFLite Frontend. #6303
* RESHAPE with dynamic shape arg in TFLite frontend #6208
* Constant input attr added to fully connected operation in TFLite frontend #6228
* Gather operation with indices as tensor expr in TFLite frontend #6168
* Added support for tflite quantized maximum and minimum #6018
* Unary ops support added in frontend #6196
* Introduce caffe frontend for tvm #6206
* Keras softmax and prelu fix under NHWC #6278
* add support for MXNET numpy operators #6054
* Refine tensorflow frontend 1.x & 2.x compatibility #6240
* Reduceops support added to frontend #6252
* Update precision in the ONNX `strided_slice`, update precision of ToScalar #6272
* NHWC import support. #4899
* Refine tensorflow frontend 1.x & 2.x compatibility #6240
* Fix node indices attribute error for tensorflow 2.3 #6288
* Support NMSv4 #6085
* Support for PyTorch Non-Maximum Suppression #6314
* ReplicationPad support added #5708
* MXNet pre-quantized BERT #6039
* Keep parameter names from PyTorch #5887
* Refine LSTMBlockCell to support dynamic rnn #5963

## Relay
* Add function attributes to IR hash (#4479)
* Relay passes lookup overhead optimization (#4594)
* Add `half_pixel` option to Resize op #4610
* Skip example json runtime test when config is not set #4614
* Test `tensor_array` in vm #4608
* Improve `memory_allocation` pass to support multiple i/o dynamic kernels #4595
* Add unit test for `tensor_array_split` #4619
* Add parses support for unary elemwise ops #4634
* Add parses support for SLICE #4502
* Added pool autopadding and simplified converters. #4672
* Fix meaning of `conv2d_transpose` `output_padding` parameter #4318
* Use packed func macro for external codegen #4710
* Fix `_parse_param` bug #4711
* Add constant input support for elemwise ops #4666
* Add parser support for squared difference #4652
* Add type check to dense #4724
* Invoke tvm::build from relay `compile_engine` and interpreter #4723
* Broadcast condition, x, and y for Where op #4774
* Add parser support for relational ops #4695
* Remove duplicated BindParamByName function in VM compiler #4793
* Use SimplifyInference for L2 Normalization. #4795
* Expose vm OptimizeModule to Python #4800
* Add parser support for logical operators #4642
* Conv2D padding representation #4787
* Add support for quantized LOGISTIC #4696
* Fix VM compiler for while loop with free vars #4889
* Fix bug in re-processing call node in MergeComposite pass #4879
* Expose FunctionGetAttr to Python #4905
* Add a PyTorch to Relay Parser #4497
* Support data types for CSourceModuleCodegen args and output #4934
* Clean up and refactor PyTorch frontend #4944
* Relay pass to use fast exp/tanh #4873
* BatchNorm support with run-time mean and variance calculation #4990
* Reduce plevel of conv2d winograd implementation on cuda #4987
* Add operation tan to TVM #4938
* Outline and inline lifted functions for external codegen #4996
* Remove primitive attribute from composite function #5014
* Refactor Relay Python to use new FFI #5077
* Fix relay node registration after refactor #5083
* `Codegen_c.h` should include relay.function #5093
* Move expr.Function to function.py #5087
* Propagate constant to subgraphs #5094
* Adjust strategy plevel to achieve expected performance by default #5118
* Added a AnnotatedRegion utility class #5030
* Support TupleGetItem in body of pattern #5106
* Partition graph codestyle fixes #5202
* Re-wrote the Graph Partitioner to support multiple outputs #5143
* Fixes to MergeCompilerRegions #5195
* Refactor build module to take IRModule #4988
* Separate analysis and transform passes #5035
* Relay Node::make to constructor #5128
* relay::StructuralHash to tvm::StructuralHash #5166
* Conditions updated to cover better user scenarios #5043
* Replace UseDefaultCompiler with GetAttr #5088
* Return empty CSourceModule when no `lowered_funcs` exists in Relay mod #4847
* Clean up for memory pass to enable heterogenous execution support. (#5324)
* Remove re-exports of tvm.transform (#5337)
* [Refactor] Add memoized expr translator for use by backend codegen (#5325)
* Legalize - Use Non-recursive Rewriter. (#5296)
* Add additional check before re-using the cached match #5552
* Remove kCompiler attr from external functions #5615
* Pattern Language MergeComposite #5656
* Support Tuple Output in C/DNNL Codegen #5701
* Infer types in MergeComposite #5766
* Convert PatternGrouper to do pre-order, non-recursive analysis #5653
* Remove constants from partitioned functions #5663
* Add a check for null function attributes #5674
* Add ConstantPattern #5689
* Conditionally Embedding Constants in Partitioned Functions #5693
* Simplify Pattern API Implementations #5703
* Add ShapePattern and DataTypePattern #5760
* Remove unnecessary print #5642
* Improve Shape Func handling for Tuple inputs #5467
* Relay updated with String #5578
* Fix the creation of tuple of tuples in PartitionGraph #5616
* Preserve type information in Merge Composite #5640
* Move `compiler_begin`/`end_op` to local static objects #5622
* Fix `dataflow_pattern`.rewrite() hang if Match in IR #5680
* Fix segfault in pretty print when ObjectRef is null #5681
* Move `fallback_device` to config #5690
* Replace `build_config` with PassContext #5698
* Clear compile engine after task extraction #5724
* Add `storage_order` ignore in pooling layer. #5781
* Tweak cublas/cudnn priority level #5820
* Skip Unknown Function Symbols #5888
* Allow every runtime module to handle constants #5885
* handle Tuple/TupleGetItem in first order gradient #5946
* Add resnet-3d & Update network definitions for NHWC layout #5945
* Use TargetNode::attrs for Target serialization #5993
* each option of target str should only contain one ‘=’ #5988
* Rename `target_id` => `target_kind` #6199
* 64-bit RPi4b target #6211
* Add resnet-3d & Update network definitions for NHWC layout #5945
* Small bug fix for Conv1D imports. #5995
* Move `invoke_tvm_op` and `shape_func` to vm dialect #5958
* GRU Layer Support #6020
* Add pass for getting calibration data from a relay module #5997
* Merge two consecutive reshape ops #6052
* Add operation `scatter_add` to relay, based on scatter implementation. #6030
* i64 indices #5235
* Port `eliminate_common_subexpr` to non-recursive form #6134
* Fix interpreter for dyanmic shape input of `ndarray_size` #6086
* Allow to config allocator type and refactor vm code structure #6105
* Handle `ndarray_size` in FoldConstant #6156
* when converting constant nodes with types of int64 or float64 #6159
* Add ReshapeTensor instruction in the VM to replace the reshape op #6089
* Support combine multiple dense op just into dense #6062
* Add unbiased variance op and corresponding support in pytorch frontend #6232
* Specify additional layouts in convert layout pass #5422
* Safe check added for Merge Composite Call Node #5562
* Non recursive partitioning #5493
* Support combine multiple dense op just into dense #6062
* Make the max number of fused ops configurable #6327
* Implementation of the dynamic pad operator #6284
* change device annotation from post DFS to recursive #6124
* Make check stricter: disallow inserting function with free vars into module #6313
* Make check stricter by using Feature. Fixed multiple bugs #6326
* Resize support for NCHW-convertible layouts #6293
* Make AutoDiff thread through global function #6336
* Create Interpreter for each constant subgraph #6195
* Add Dynamic reshape to a dynamic namespace and add DynamicToStatic Pass #5826
* Expose relay BindParamsByName to Python #4751
* Implement pass manager tracing API #4782
* Move Ops in relay.op.contrib #4942
* Conditions updated to cover better user scenarios #4951
* [External codegen] Add test cases for fused ops with manual annotation (#4741)
* Multiple output support, reshape, split ops added #6296

## Operator Coverage
* Allow empty tensor for `reshape`, `tile` and `strided_slice` #4618
* Fix meaning of `conv2d_transpose` `output_padding` parameter"; #4708
* Remove cpp upsampling and resize op #4769
* upsample operator 'NCHWinic' format support. #4791
* Injective schedule improvement #4786
* Enable vectorization on fp16 type #4867
* Support for Int8 schedules - CUDA/x86 #5031
* New PR to re-add tan to TVM #5025
* Register topi schedule for Relay `fast_exp` and `fast_tanh` #5131
* Move Dilation2d from nn to image namespace #5110
* Use Thrust sort for argsort and topk #5097
* Conv2d and Dense ops support on Tensor Core #5099
* Setting workload correctly for Depthwise Spatial conv ARM. #5182
* Adding a few missing math intrin #5011
* Missing vectorize for depthwise conv2d. #5196
* [TOPI] Using x86 schedules for ARM conv2d (#5334)
* [TOPI-ARM] Do not alter layout if layout is NHWC (#5350)
* [TOPI] Setting workload correctly for Depthwise Spatial conv ARM. (#5182)
* [OP] Add `fast_erf` implementation (#5241)
* [Topi] Tensorcore support for Conv3D (#5284)
* [intrin] a few more math functions (#5468)
* [Intrinsic] Add log1p, ldexp, atan2, hypot, nextafter, copysign (#5312)
* [topi] Add operation relay.nn.dilate() which calls topi.nn.dilate() (#5331)
* [Topi x86] Missing vectorize for depthwise conv2d. (#5196)
* [TOPI x86] Adding `unroll_kw` config option for depthwise conv2d. (#5197)
* [Topi] Breakdown topi.cc into smaller files (#5253)
* ReduceLogSumExp Operator support #5453
* Math ops added #5502
* Enable blocking format in x86 conv2d and fold scale axis #5357
* Add operation gather to relay. #5716
* Add `storage_order` ignore in pooling layer. #5781
* Fix bifrost spatial packing conv2d auto tune #5684
* Fix reshape usage in ARM schedule #5732
* Block sparse dense on cuda #5746
* Improve CUDA softmax scheduling #5600
* block sparse dense on cuda #5746
* pass-by-value -> pass-by-const-reference #5783
* Using MKL blas for quantized dense #6115
* topi -> tvm/topi #6186
* Use auto-tuner to improve `conv2d_gemm` performance #6117
* Improve CUDA `conv2d_transpose_nchw` #4762
* Add CUDA conv2d for NHWC layout #4737
* `conv3d_ndhwc` schedule #4775
* Fast exponent #4790
* Add Scatter to Topi/Relay/ONNX via hybrid script #5619
* Split MKL from BLAS. #6182
* Change the meaning of `conv3d_transpose` `output_padding` to match `conv{1,2}d_transpose` #6065
* Gather op support added #6013

## Runtime and Backend
* Cythonize NDArray.copyto (#4549)
* Unified Object System runtime refactor (#4578, #4581, #4603)
* VM profiler: sort VM stats by time (#4601)
* Update RPC runtime to allow remote module as arg (#4462)
* Refactorying system lib and dso lib into library module (#4481)
* Improve TSIM virtual memory mapping (#4545)
* make adt tag signed #4605
* Improve TVMBackendPackedCFunc to allow return val #4637
* EdgeTPU runtime for Coral Boards #4698
* Fix memory leak when using openMP #4811
* Fix memory leakage of TVMByteArray #4856
* Fix `TVM_DLL_EXPORT_TYPED_FUNC` to work on Windows #4955
* Fix memory leak when using openMP #4811
* Export GraphRuntime in `tvm_runtime.dll` #5002
* MISRA-C compliant TVM runtime #3934
* Update the `type_keys` to reflect the code-org #5074
* Fix AttrEqual for Array and StrMap, double #5054
* Export GraphRuntime in `tvm_runtime.dll` #5002
* Fix unused-value warning #5140
* crt error handling #5147
* Bundle deployment with static linking #5158
* Implemented kDLCPUPinned (cudaMallocHost) #4985
* Explicitly cast min/max operands #5090
* `ref_counter` -> `ref_counter_` #5184
* Expose runtime::String to Python (#5212)
* [FFI] Refactor runtime.String to subclass str (#5426)
* [RUNTIME] Auto conversion from str to runtime::String in PackedFUnc (#5251)
* [RUNTIME] Improved Packed FFI for optional. (#5478)
* [Hexagon] Add `hexagon_posix.cc` to TVM/RT sources in the right place (#5346)
* [FFI] Refactor runtime.String to subclass str (#5426)
* Fix workspace #5503
* Store nullptr PackedFunc as nullptr for better error propagation #5540
* Improve PackedFunc robustness #5517
* Seg fault in WorkspacePool's destructor (#5632) #5636
* Resolve constexpr issue in debug mode. #5651
* Add `compile_shared` option to linux compile utility fn #5751
* Call sync in CopyFromRemote and CopyToRemote #5512
* Fix the multihop cpu case #5522
* Improve RPCServer AsyncIO support. #5544
* Modularize the RPC infra #5484
* Add `compile_shared` option to linux compile utility fn #5751
* Overload string operators #5806
* Only initialize required module #5926
* if a param not in input, we should still consume it’s data #5990
* init TVMPackedFunc’s name #6044
* Enable auto conversion `String->DLDataType` #6214
* Support random fill #5913
* Use new to avoid exit-time de-allocation order #6292
* Add `parallel_for` support to run a loop in parallel #6275
* Solve ARM BIG.LITTLE heterogeneous multicores #4747
* [RUNTIME] Quick fix PackedFunc String passing (#5266)
* Introduce runtime::String::CanConvertFrom #5718
* Restore the StrMap behavior in JSON/SHash/SEqual #5719
* Support overriding RPCWatchdog termination behavior on Android and other platforms #6216
* Set `NDArray::Container.shape_` in NDArray::FromDLPack (#5301)
* Enable x86 cpu cache flush #5914

## Quantization
* Conv2D type checking for kernel per-channel scales. #4732
* Add missing nullptr check #4773
* Doc fix on convolution and dequantize #4799
* Conv2D with dilation support. #4796
* Making `scale`/`zero_points` as expr instead of attrs. #4611
* Make calibration faster and more memory usage friendly #4589
* Doc fix on convolution and dequantize #4799
* Conv2D with dilation support. #4796
* Optimize lowering for requantize and FixedPointMultiply. #4798
* More doc fix on quantize and convolution #4874
* Add support for per channel weight scale in dense op #4880
* Add support for quantized models via QNN #4977 #5013
* Support 4D padding. #5036
* [Requantize] Cleanup and Optimize Lowering (#5286)
* [Topi, ARM] Disbale Winograd for quantized tensors. (#5363)
* Adding support for TFLite QnnSubtract operator. (#5230)
* Remove developer facing api from frontend exports. (#5375)
* Add Quantize/Dequantize Partitioning #5940
* Add support for quantized models via QNN #5016
* Quanitze operation expanded to take const argument #6127
* FP32 and Quantized Object Detection Model #5479
* Support CallNode inputs in qnn.concatenate #5360
* QNN support for TFLite 2.1.0 quantized models #5848

## TE
* Tighten split's extent #4931
* Set split node's range to minimum of ext and split factor or split np… #5044
* Support mixing normal and cross-thread reduction (#5193)
* Inline -> `te/schedule/operation_inline.h` (#5386)
* Create loops according to storage scope and thread hierarchies (#5190)
* Fix import in dump pass ir (#5327)
* Scalar support for te.extern #6079

## TIR
* IR readability enhancement (#4501)
* Introduce tir::PrimFunc #5070
* Introduce PrimFuncPass. #5139
* [TIR] Enhance Substitute, python bindings for Substitute/PostOrderVisit (#5400)
* [TIR] Remove ProducerConsumer and `AllocateNode::new_expr` (#5333)
* [TRANSFORM] Enable CopyOnWrite for TIR passes. (#5309)
* [REFACTOR] Migrate LowerTVMBuiltin, InferFragment, LowerThreadAllreduce, ThreadSync to Pass Manager (#5213)
* [REFACTOR] Remove te::Tensor dependencies from TIR passes. (#5372)
* [TIR] Refactor MakePackedAPI to target dependent stage. (#5326)
* [REFACTOR] tvm.hybrid -> te.hybrid (#5223)
* [REFACTOR] Migrate most of low-level build to use the Pass Manager. (#5225)
* [REFACTOR] Migrate low-level passes in tvm.lower to the Pass Manager (#5364)
* [TIR] Migrate VTA TIR passes to the new pass manager. (#5397)
* [REFACTOR] Migrate all low-level passes to the Pass Manager. (#5233)
* [REFACTOR] Introduce ExprDeepEqual, Remove IRDeepCompare (#5206)
* [REFACTOR] RewriteForTensorCore -> te/schedule (#5379)
* [REFACTOR] Remove `ir_pass` in favor of analysis/transform. (#5415)
* text format printer considering future parsing use #5483
* Remove buffer params from pass config. #5652
* std::string -> String Migration in TIR nodes #5596
* Remove `CallNode.call_type` in favor of attribute. #5937
* Remove legacy HoistIfThenElse #5944
* Improve Let/LetStmt support. #5949
* Refine side effect analysis. #5954
* `Provide->ProducerStore`, `Realize->ProducerRealize`. #5750
* Migrate the tvm/tir/expr.h to constructor #5773
* Migrate tir/stmt.h to use constructor. #5778
* Cleanup unused classes #5789
* Add tir prefix to type keys #5802
* Enhance VerifyGPUCode #6194
* Enforce buffer pointer var type to be consistent with dtype. #6317
* Create a StringImm reference type #4806
* Add init member to ReduceNode #6138
* Add dump and print for debugging (NFC) #5207
* Streamline Function Attr interface. #5045
* `alpha_equal` to `structural_equal` #5161
* Remove AttrsEqual and AttrsHash related code #5169
* [NODE] General serialzation of leaf objects into bytes. (#5299)
* [POC] Initial stab at `std::string->String` upgrade (#5438)
* [TIR] Make `lower_warp_memory` support `extent(threadIdx.x) < warp_size` (#5307)
* [PASS] dtype rewrite for indexing variables (#5092)
* [PYTHON] Enhance `with_attr` API, cleanup MakeAPILegacy in testcases (#5335)
* [PYTHON] Make IntImm more like an integer (#5232)
* [IR] Move to runtime::String (#5276)
* [IR] kExternalSymbol -> kGlobalSymbol (#5211)
* [IR] Remove PrimExpr from String (#5311)
* IRModule is updated with String #5523
* IR is updated with String #5547
* Streamline ir/op Registry #5609
* Migrate IRModule ObjectRef to not-null #5654
* Migrate BuildConfig to PassContext. #5668
* relay.op.Op -> tvm.ir.Op #5705
* Separate ArgTypeCode from DLDataTypeCode #5730
* Remove legacy `compute_expr.h` #5738
* Call::Halide => ProducerLoad, DSL/TIR decouple. #5743
* `Provide->ProducerStore`, `Realize->ProducerRealize`. #5750
* Migrate the tvm/tir/expr.h to constructor #5773
* Migrate tir/stmt.h to use constructor. #5778
* Migrate all Object construction to constructor. #5784
* Cleanup unused classes #5789
* Finish `std::string->String` updates #5793
* Add tir prefix to type keys #5802
* Change Call.name to Call.op(RelayExpr) #5863
* Range/IntSet API style consistency. #5953
* Separate ArgTypeCode from DLDataTypeCode #5730
* Migrate all Object construction to constructor. #5784
* Finish `std::string->String` updates #5793
* Unify StrMapNode and MapNode #5687

# Performance Improvements
* Int8 GEMM performance enhancement using Cublas (#4550)
* Speedup TSIM with multi-threading (#4491)
* Support cudnn softmax (#5214)
* Add cuDNN grouped convolution support (#5319)
* Winograd support for Conv3D (#5186)
* Improve `get_valid_count` and nms performance for CUDA (#5339)
* Optimizations of `global_ave_pool` for NHWC layout (#5450)
* Optimization of Conv2d Winograd algorithm on Tensor #5485
* Some performance improvement to VM #5901
* Optimize x86 `conv3d_ndhwc` using data packing approach. #4866
* Improve NHWC depthwise convolution for AArch64 #6095
* Improve quantized convolution performance for armv8 architectures #5754

# Documentation
* Adding benchmark log format doc (#4366)
* Add Ninja build system to installation docs (#4554)
* Doc/comment fixes (#4452, #4463, #4469, #4493, #4397, #4580, #4585, #4591)
* Fix doc after moving to unified IR #4835
* Introduction to module serialization #4564
* ConvertLayout - Call RemoveUnunsedFunctions. #4834
* Fix bugs that override `n_trials` #4842
* Update the vm doc #4868
* Refine the example description of `max/min/sum/tag_scope` #4974
* Fix vta tutorial #4809
* Introduce how to add hardware backend to FAQ #4898
* Update API docs to reflect the status after the refactor. #4907
* Fix sphinx warnings #4917
* Fix Sphinx Warnings (RST indent, cross-ref, and image scale) #4920
* Fix Sphinx Warning: the target found for cross-reference #4925
* Sphinx -- Introduce alias detection. #4954
* Fix Warnings from #4942 #4959
* Fix sphinx precheck #4967
* Move `git_howto` to rst, add Stage documents to te #5055
* Add doc for Relay op strategy #5078
* Update relay docs #5112
* Include a tarball of docs, add a security faq #5119
* Cleanup docs before rebuild #5127
* Minimize necessary doc change #5129
* Various sphinx related fix. #5168
* Point docs to the ASF site. #5178
* Use https link #5183
* Reduce artifcats generated by sphinx gallery #5208
* Refine the example description of `max/min/sum/tag_scope` #4974
* Description updated for pooling attributes #5091
* [DOCS] Migrate some markdowns to rst, fix sphinx3 warnings (#5416)
* [DOCS] Misc docs improvements (#5222)
* [DOCS] Bring relay docs to the top-level flat view (#5343)
* [DOCS] Reduce artifcats generated by sphinx gallery (#5208)
* [DOCS] Use https link (#5183)
* [DOCSTRING]missing function parameters updated (#5228)
* [DOCS] Migrate HLS documents from md to rst (#5419)
* [Tutorial, QNN] Add tutorial for loading quantized PyTorch model (#5321)
* [Docs] VTA install doc migration from md to rst (#5442)
* [Docs] compiler version in docs (#5281)
* Remove legacy `compute_expr.h` #5738
* `TVM_REGISTER_API` -> `TVM_REGISTER_GLOBAL` #4768

# Bug Fixes
* Add bfloat16 typeflag support (#4525)
* MSVC / Windows fixes (#4455, #4569)
* Fix Makefile for `howto_deploy` (#4457)
* Fix GCC 4.8 compact (#4461)
* Fix search path to build `libtvm_topi.so` (#4467)
* Fix for `conv2d_transpose` CUDA compilation (#4472)
* Fix for LLVM 10.0 codegen (#4480, #4515)
* Fix alter op layout when calling global var (#4454)
* Fix `float2half_rn` support for cuda compute capabilities < 53 (#4489)
* Fix compile errors for OpenCL backends (#4492)
* Fix serialization precision loss (#4503)
* Fix hybrid script to support array of tensors (#4494)
* Fix annotation for multiply op (#4458)
* Fix Dockerfile for linter CI (#4506)
* Fix TF resize for dynamic size models (#4510)
* Fix `bias_add` gradient (#4516)
* Fix tanH unit test function call (#4517)
* Fix extra reshape parameter for ONNX (#4524)
* Fix crash caused by empty TOPI config (#4520)
* Fix ONNX shape op type to use int64 (#4528)
* Fix crash in TSIM virtual memory driver (#4527)
* Replace deprecated python library in setup script (#4533)
* Fix NMS `max_output_size` loop (#4541)
* Fix style in IR mutator and IR visitor (#4561)
* Fix compiler warning (#4559)
* Fix to get end to end inference on Chisel VTA (#4574)
* Fix LLVM build by adding missing intrinsics headers (#4575)
* Fix context creation in quantization (#4582)
* Fix NDArray SaveDLTensor signature (#4586)
* Fix dense pack schedule for x86 (#4539)
* Fix for broadcast tensor of scalar type (#4577)
* Datatype refactor (#4513, #4560)
* Add const qualifiers for NDArray container (#4590)
* Fix TF <= 1.12 compatibility (#4593)
* Fix for graph debug runtime (#4598)
* Disable copy constructor for external codegen (#4597)
* Make ADT tag signed (#4605)
* Added declare of aluBits for TensorAlu #4624
* Get around limitation of g++-4.8 #4626
* Bugfix StmtMutator IfThenElse #4609
* Remove unecessary rdynamic #4613
* Resolve constexpr related link error in debug mode #4641
* Asymmetric padding #4511
* Reduce data size of asymmetric padding testcase #4658
* Fix Base64OutStream portability issue #4668
* Fix `topi.nn.global_pool` layout="NHWC" #4656
* Also package core.rly #4679
* fskip of EliminateCommonSubexpr cannot always return false #4620
* Fix Python syntax error in `start_rpc_server_to_tracker.py` #4682
* os.path --> osp to match the import #4681
* GitHub actions/checkout@v1 --> v2 #4680
* Fix Python syntax error AGAIN in `start_rpc_server_to_tracker.py` #4685
* Use ==/!= to compare str, bytes, and int literals #4686
* Rename `start_rpc_server_to_tracker.py` to `start_rpc_server_to_tracker.sh` #4689
* GitHub Action lint Python code for syntax errors #4688
* Generate blob use LLVM directly #4657
* Reduce input size to fix oom #4653
* Fix RemoveUnusedFunctions pass #4700
* Link the math library by default #4713
* Update mainline version to 0.7.dev0 #4720
* Add SizeVar representing non-neg valued variable in a tensor shape #4684
* Fix the compile problem of `cpp_rpc` #4725
* JSON upgrader to upgrade serialized json. #4730
* Fallback schedule for Int8 depthwise. #4733
* Fix dense x86 schedule #4728
* Fix demo dockerfile build failed #4744
* Improve CUDA vectorizer #4736
* Add .asf.yaml for github info #4761
* Fix padding in pooling op #4738
* Remove `run_infer_type` duplicates #4766
* pooling.cc improvements #4767
* Export `builtin_fp16` on Windows #4731
* Fix Tensorflow conv3d pad bug, add non-cubic data and kernel tests #4772
* Bump prebuilt-image version in demo dockerfile #4770
* Update `tune_simple_template.py` #4778
* Explicitly link to cublasLt if it exists #4776
* Fix hasattr by extracting Python error type from Windows error message #4780
* Replace os.path.exists with try...except...else #4784
* Make sure to visit the arguments of inlined functions #4783
* Parse additional exception strings #4785
* Fix #4670: add bias for fc layer #4801
* Change color channel from BGR to RGB for darknet preprocessing #4794
* Fix -Wextra #4804
* Fix vta tutorial #4809
* Minor bug fixes in AutoTVM for QNN graphs #4797
* Fixed subprocess creation under windows #4820
* Improve tol to resolve flaky case #4836
* Fixed process termination routine in windows #4844
* `test_cuddn` flaky #4846
* Mxnet parser for Qnn dialect #4714
* Enhance `cc.cross_compiler` #4817
* Fixed crash caused by reversing bitwise operations #4852
* Reverse some changes made for `intel_graphics/conv2d.py` in PR #4849 #4853
* const auto p -> const auto& p #4861
* Fix onnx import bugs #4750
* Explicit llvm::StringRef to std::string conversion #4859
* Update the runtime PackedFunc for module #4871
* Improve antlr import error message #4888
* Fix `alpha_equal` bug for attribute check #4897
* Fix issues in cuda codegen #4876
* Fixed: Bitwise ops on floats causing wrong code generation and crashes. #4892
* Fix `tvm.target.generic_func` runtime detection #4910
* `topi/tests/python/test_topi_sort.py::test_argsort` #4891
* Use opencv reisze method for preprocessing of image in darknet #4883
* Fix build breaks with StringRef changes #4923
* Remove unnecessary spliting in the cached chunk #4935
* Fixing an Infinite Loop case in UnmatchedChecker. #4881
* Remove SGX toolchain installation from CI Dockerfile #4948
* Fix tedd tutorial after strategy change #4947
* Allow customize MKLDNN library location #4814
* Added CopyFromBytes and CopyToBytes convenience methods to NDArray. Fixed typos. #4970
* Fix gcn tutorial failure #4994
* Fix stride default value None in torch.nn.functional.avg_pool #4984
* Fix ROCm strategy for winograd conv selection #5001
* Fix `get_valid_count` flaky test for cuda #4901
* Change Scala Linter scalafmt => scalastyle #4998
* Kill from tvm import te #5007
* Chisel fixes and de10nano support #4986
* Fix gpu not found when running TVM docker #4975
* Fixes for pylint==2.4.4 #4849
* Fix unordered dictionary problem for python version under 3.6 #4982
* Fix gcn tutorial failure #4994
* Fix stride default value None in `torch.nn.functional.avg_pool` #4984
* Fix ROCm strategy for winograd conv selection #5001
* Early checking added and new test cases added for schedule fuse #5010
* Fixed div by zero core dump. Fixed rounding intrinsics on int crash #5026
* Test case modified for int type #5012
* Bug Fix for ARM CPUs. Lower strict assumption. #5063
* Triage the testcases to fit the the new namespaces #5071
* Add colors to `compute_at` edges and thread/block indices. #5111
* Temporary fix to the stack overflow issue in autotvm task extraction #5019
* Fix compilation of If-Elses #5040
* Fix CompilerAttrs #5109
* Fix the existing test cases before refactoring. #5122
* Fixed bug where shifting by out-of-bounds value results in no compute code being emitted. #5115
* Fix for issue #4831. The `data_min_idx` and `data_max_idx` were flipped. #5136
* Duplicate likely nodes added when loop axis split unevenly #5084
* Fix incorrect name of calibration mode #5150
* Remove contrib spatial pack schedule of depthwise convolution #5148
* Fix annotate pass static variable #5023
* Fixed ConvTranspose2D parsing #5157
* Nullptr check #5176
* rocm: fix miopen convolutions #5179
* rocm: fix `dense_rocblas` in strategy, topi #5191
* Fix CRT static test bug (#5293)
* Fix perf regression of tir refactor (#5258)
* Bugfix in tensorflow `space_to_batch_nd` (#5175)
* Compilation warnings fixed for 32bit and 64bit compilation (#5349)
* Fix hang in MergeCompilerRegions (#5227)
* Fixes to MergeCompilerRegions (#5195)
* Fix generation of LLVM intrinsics (#5282)
* Fix setting up hints for getaddrinfo (#2872)
* Add ConstantNode to IsAtomic (#5457)
* Fix String SEqual (#5275)
* Fix fuse over functions that are handled by external codegen (#5365)
* Fix memory leak when accessing NDArray (#5413)
* Remove the duplicate PrintIR pass in Relay (#5403)
* Fix `lower_warp_memory` (#5247)
* Fix `lower_warp_memory` when there are >1 warp buffers (#5368)
* Fix intel conv2d auto tune (#5200)
* Fix FuseBatchNorm output cast error if `need_cast` is True #4894
* Fix an assertion exposed by loop vectorizer #4916
* Fix error message #4945
* Fix for recursive let #5757
* Fix Calibration Pass to Support Modules with Multiple Functions #5768
* Fix what looks like bizzare copy-paste issue #6010
* Fix bug in `transpose_shape_func` #6180
* Fix bugs in CUDA codegen (#5209)
* Don’t remove() TemporaryFile in del. (#5414)
* Fix `test_ir_type`. (#5390)
* Fix multiple identical inputs bug (#5389)
* Add cuda target check to dense tensorcore schedule. (#5376)
* T2 test fixups (#5391)
* Fix miopen padding (#5433)
* Misc fixes for ROCm (#5431)
* Fix copy constructor (#5237)
* Corrected TVM autotuning on GPU (#5432)
* Fix vector load (#5226)
* Minor bugfix in `message_passing.cc` (#5254)
* Fix a bug when vectorized load&store was involved for… (#5428)
* Fix to skip node not in graph. (#5238)
* Fix #5388 [VULKAN] vkBuffer released before memory copy command se… (#5418)
* Fix a minor error in `device_annotation` (#5291)
* Fix scalar’s ndim is 0 (#5344)
* Fix the runtime raise error #5586
* Fixed bug in attribute parsing for pool layers. #5582
* AutoTVM incorrect measurement #5511
* fix a min/max simplify bug #5761
* Rename `tvm_dso_op` to `libtvm_dso_op` #5714
* Fix generating types like float44 and float88 #5722
* Avoid downloading when `TOPHUB_LOCATION` is NONE #5720
* codegen llvm: move nvptx-specific intrinsic handling into `codegen_nvptx` #5726
* ROCm warp shuffles and reductions #5727
* fix small bug about `dense_grad` #5695
* Clarify downstream consistency of TVMArgTypeCode #5742
* Fix gelu in PyTorch frontend, tighten numerical checks #5763
* Make batch matrix multiplication on GPU tunable #5752
* update vulkan build rule #5777
* aten::norm support added #5776
* Edit onnx parser to infer values in post order #5755
* Support symbolic inputs of Fill #5762
* support `aten::type_as` in the pytorch frontend #5787
* Temporary disable fp16 `type_as` test for PyTorch Frontend #5799
* Add config switch for nn.dense layer type. #5801
* Move cpu-only frontend tests to a CPU stage #5807
* Pin hand landmark network to version 0.7.4. #5813
* Limit number of threads in all jobs #5815
* Error msg update #5818
* fix relay.build to not change the module argument in place #5822
* Fix InferType when module contains Prelude #5797
* Add a combine `batch_matmul` pass #5791
* RepeatVector, Conv3DTranspose op support added #5833
* Fix converting serialized quantized models #5839
* ffi (Object): make class dict visible in instances #5843
* Additional canonicalization added for AddNode #5846
* Suppress the warning messages when compile engine selects impls #5821
* fix #5849 #5851
* Introduce POD-C Compliant tvm::Map #5740
* Add bfloat16 #5601
* Add Python Classes for all Attrs #5853
* Fix map assign issue in CI test #5854
* Introduce Target Id Registry #5838
* Update `has_dtype/has_shape` to pattern lang doc #5847
* Add `nn.batch_flatten` as quantizable. #5805
* Fail early before running invalid dynamic graphs #5856
* Improve type handling in PyTorch frontend #5834
* HotFix the python intrin rule #5895
* add a few gradients #5899
* Add Binary Intrinsic ops to TIR Ops in C++ #5900
* Allow implicit conversion in TVM FFI to tvm::Bool #5907
* PyTorch frontend: fix handling of duplicate use of a model weight #5897
* Don’t multiply by constant 1 uselessly in dense #5911
* Support any index matching for TupleGetItem #5909
* Add MicroTVM tutorial using the STM32F746 discovery board #5655
* Fix serialization of inf float value #5912
* Fix CPU Thread Binding for Multiple Sockets #5918
* CUDA device API & VerifyGPUCode pass update #5898
* Update install.rst #5858
* Two small fixes to AMDCPU codegen for LLVM 10+ and ROCm 3.5+ #5920
* Add LegalizeInvalidAttach to legalize the `compute_at` location after split or fuse #591
* Don’t rewrite expressions used outside of the pattern #5930
* Add TupleGetItem to CSE #5931
* Various update for CoreML codegen #5934
* Update date in the NOTICE #5943
* Raise right error in tensorflow split op #5951
* Add rm xla attributes in tf docs #5950
* Fix OpenCL `get_valid_counts` errors due to intrinsic `atomic_add` #5857
* Amendments for gradients #5941
* Fix the meaning of `conv{1,2}d_transpose` `output_padding` parameter. #5758
* Make first order gradient graphs more efficient #5959
* Raise an exception when extern function does not return Stmt #5964
* Improve docker/bash.sh to handle git worktrees #5970
* Install DNNL (OneDNN) to CI Environment #5936
* Add Dynamic reshape to a dynamic namespace and add DynamicToStatic Pass #5826
* Add meshgrid op in Relay, TOPI, Pytorch frontend #5961
* Print right number of parentheses for LoadNode #5965
* Migrate data structure of TargetNode #5960
* Remove redundant function CreateBufferVecPtr #5982
* Fix string argument mismatch in GraphRuntimeCodegen #5933
* VectorType::get with two parameters is deprecated in LLVM 11+ #5984
* Fix Compilation Error in CRT #5713
* Fix runtime::String backward compatibility in JSON #5725
* Allow RPCWrappedFunc to rewrite runtime::String as std::string #5796
* Fix reshape #5739
* Fix building with LLVM-10 on macOS #5859
* Add cuda 11 to `contrib.nvcc.find_libdevice_path()` #5902
* Fix sequential cpp test #5745
* Infer types in MergeComposite #5766
* Fix recursive let for well formed check #5780
* Recover global state after `test_util.py` #5824
* Fix bug in rpc ring buffer shrink #5516
* Fix remote device sync #5538
* Fix bug in rpc ring buffer shrink (#5516) #5537
* RPC Server error fix on Pynq FPGA #5607
* Fix FloorMod Simplifier #5509
* Fix Python debugger segfaults with TVM built with LLVM #5685
* Fix Compilation Error in CRT #5713
* Fix runtime::String backward compatibility in JSON #5725
* Allow RPCWrappedFunc to rewrite runtime::String as std::string #5796
* Fix reshape #5739
* Make "none" DataType explicit #5491
* Change "scalar" and "stack" in IDL from "inrout" to "in" #5487
* Link necessary libraries when building runtime for Android #5496
* Fixes for wasm32 target #5489
* Reset target and wait for runtime initialization on connect. #5499
* Bump tophub rocm version #5504
* Improve commentary for RingBuffer #5518
* Add unit tests for ONNX PRelu and fix importer to pass them. #5521
* LRN only supports 4D tensors, remove it from `alter_op_layout` #5520
* Fix an issue with ONNX Upsample #5530
* Cache PrimExpr instead of raw pointers in bound analyzer #5533
* fix a few bugs with shape inference and types in the ONNX importer #5534
* Add Onnx Pad v11 #5539
* Changes to `cpp_rpc` to make it work on Android (+ Hexagon offloading) #5535
* Fix to reduce RAM size during loading model #5507
* Fix MakeLoopNest for warp memory #5382
* Load platform specific lib for tvmdsoop instead of the hard-coded tvm_dso_op.so #5542
* Add tests for running micro on native arm hardware #5546
* Apparently, ONNX Conv with no 'pads' defaults to zero padding #5548
* clang-format the h,cc,m files. #5557
* Fix conv2d alter op for arm cpu #5532
* Fix topi test for non tensorcore CI. #5563
* Add clang-format and nodejs to ci-lint #5567
* Enable clang-format. #5572
* Allow `ubuntu_install_darknet.sh` to work in both 18.04 and 16.04 #5574
* Add a quantized conv2 unit test for the tflite front-end #5558
* Fix JSON graph dumping. #5591
* Warp level reduction support for CUDA #5498
* One more fix for concurrency count #5589
* Improve robustness of the docs build #5583
* Phase out WebGL #5570
* Fix vulkansdk in the ci-gpu and upgrade to 1.2.135 #5566
* Update ci-cpu to bionic #5554
* Overestimate binary size for microTVM compiled binaries. #5590
* Fix bug and re-enable RPC execution test #5436
* Add ostream formatters for TargetPtr/TargetVal. #5592
* Fix cross thread reduction #5551
* Fix TVMArray layout on device #5599
* Add debug mode to tempdir() #5581
* Represent alignment information in LLVM IR #5598
* Fix codegen for warp shuffle intrinsics #5606
* Fix Topological Order calculation for DFPattern Language #5612
* Global MaxPool3d and AvgPool3d support #5098
* Fix build error of iOS RPC #5621
* isn't a CallNode sometimes #5623
* Introduce config to PassContext. #5631
* CMAKE fix #5630
* Label Pattern Partitions #5627
* Extend AttrPattern to support CallNode and FunctionNode attributes #5637
* Increase bss section size. #5660
* Add buffer name when creating tensor bindings #5670
* µtvm debug improvements #5648
* enable `amd_apu` device on vulkan target #5659
* Support TupleWrapper as direct ancestor of control flow ops #5639
* add tvm.micro pydoc to sphinx #5661
* Add a regression testcase for #5674 #5677
* Fix C++ RPC build problem on Linux #5671
* Add a check Callback to the Pattern Paritioner #5646
* Call previous excepthook in `tvm_excepthook`. #5675
* Fix the shift column for `scale_shift_nchw` and `scale_shift_nhwc` in C topi #5679
* Support more dtypes for TVMDSOOp #5694
* In `memory_plan`, check if value is not None, instead of just checking value as boolean. #5700
* Fix flaky `test_topi_pooling.py:test_adaptive_pool` #5736
* Fix the values for `test_fmod` since it fails way too often otherwise #5723
* fix small bug about `dense_grad` #5695
* Fix sequential cpp test #5745
* Add Scatter to Topi/Relay/ONNX via hybrid script #5619
* Clean WASM environment before build #5759
* Fix gelu in PyTorch frontend, tighten numerical checks #5763
* fix #5686: remove a overstrict assert in MakeAllreduce (#5686) #5785
* Improve Pattern Language Docs #5676
* Add missing expr visitor for any #6082
* Remove the tvm web from version update #6122
* Clear relay cache after every build & Clear warning message cache after autotvm task extraction #6131
* avoid unexpected throw in AttrInitEntry #6128
* Verify that tensor reshape is valid. #6215
* Use LocalRunner by default in the tutorial tune_relay_cuda.py #6001
* Undefined names: import os for line 324 & import re for line 308 #6003
* GitHub Actions upgrade to actions/setup-python@v2 #6002
* Only pass pythonpath for ci images #6005
* Auto-convert shuffle with single index to “extract element” #6006
* Cache object refs in loop partitioner instead of object pointers #6004
* Fix `test_arith_solve_linear_inequality.py::test_multi_equal` #6014
* MXNet frontend support for AMP cast op #5976
* Demo showing how to run a pruned model. #5975
* Move compiler related registry items to `vta/build_module.py` #6012
* Pin keras version #6032
* Fix in `arm_cpu/conv2d_alter_op` for NHWC quantized #6027
* Add creation of Hexagon device in RPC client #6035
* Terminate basic block after “ret” instruction #6036
* µTVM CRT modifications for on-device RPC server #5921
* Create TBAA information based on the unrelying buffer type #6046
* Add support for tflite `arg_min` and `arg_max` #5992
* Fix `fully_connected` converter when batch size is not 1 #6038
* Fix a primitive check error #5991
* Refactor to expose MakeOp functions to C++ #6047
* Fix `conv2_gemm` after target structure update #6037
* Remove use of designated initializers from `hexagon_module.cc` #6055
* Build crttest and cpptest separately. #6057
* Fix pytorch frontend prim::Constant issue #6051
* update frontend tutorials to new model based runtime interface #6063
* Remove unnecessary std::cout #6072
* Fix error message in Buffer::vstore, NFC #6056
* Fix FSIM Compile Error. #6070
* Improve vector simplification for float operands #6043
* Fix LocalBuilder on macOS with python 3.8. #6083
* Add missing test for fast erf #6058
* Fixed point multiplication improvements for AArch64 #5980
* Fix code generation bugs for C/CUDA & Improve VerifyGPUCode pass #6041
* Delete declaration of unused `op_node` #6102
* Load configs even it has no entity #6100
* Update SGX example Cargo.toml #6067
* Add default value for option `USE_DNNL_CODEGEN` in the cmake #6099
* Update installation doc with minor improvements #6104
* lint: add opencl .cl file type #6092
* Clean up conversions between TVM and Rust functions #6114
* Improve reduction schedule on arm CPUs #6110
* Register Shape Func for Some Operators to Handle Dynamic Shapes #5955
* Fix variable name conflict with OpenCL keyword #6048
* Some rust cleanups #6116
* Option to specify alternate directory to output build to #6016
* Add `get_num_inputs` to GraphRuntime #6118
* TFLite quantized conv test #6084
* Fix autotvm on the `conv2d_nchw_winograd.mali` operator #6130
* add attr option mfloat-abi for arm32 #6123
* Fix CUDA Library Tuning #6132
* Add missing RPC sources after refactor #6113
* Correct `runtime.load_module` #6161
* Improve error messages in graph tuner, graph runtime, and module loader. #6148
* Fix some shape mismatches between TF and Relay #6166
* Improve doc string #6176
* Fix incorrect function signature in header #6172
* Fix alignment of note #6181
* Implemented PADV2 Operator for TFLite and added support for constant values in PAD. #6167
* Unary ops support added in frontend #6196
* Change the meaning of `conv3d_transpose` `output_padding` to match `conv{1,2}d_transpose` #6065
* Fix compile warnings. #6204
* Fix -mfloat-abi=soft compilation for ARM with OpenCL target #6150
* Match pytorch 1.6 googlenet pretrained model (#6201) #6212
* Mod operator, bug fix #6160
* RESHAPE with dynamic shape arg in TFLite frontend #6208
* Fix compilation error with cuda 11 #6213
* Fix `port_end` wrong default value 9199 to 9099 for keeping same with source code #6220
* Std op without specified dimensions support #6226
* fix crt building and running error #6231
* Implemented `ONE_HOT` Operator for TFLite. #6223)
* Avoid unexpected throw in AttrInitEntry #6128
* Added casting to hybrid script doc and fixed pass infra doc #6174
* Fix compile warnings. #6204
* Fix -mfloat-abi=soft compilation for ARM with OpenCL target #6150
* Mod operator, bug fix #6160
* Fix compilation error with cuda 11 #6213
* Fix `port_end` wrong default value 9199 to 9099 for keeping same with source code #6220
* Std op without specified dimensions support #6226
* Verify that tensor reshape is valid. #6215
* Fix crt building and running error #6231
* Fix `conv2d_transpose` output padding #6236
* Fix cuda half math function is undefined: hpow, htanh #6225
* Fix division range estimation error in simplifier #6244
* Fix newer GCC compiler warnings. #6257
* Support `_contrib_SyncBatchNorm` #6245
* Fix reduction #6250
* Add apt repository for clang-11 and llvm-11 #6256
* Update tutorial to new TARGET as `micro_dev` is no more #6262
* Fix clang-format #6264
* Trivial fix, up the rodata section for the discovery board to 512 bytes. #6259
* Fix cuda half math function is undefined: hpow, htanh #6253
* Add dilation in x86 NCHWc depthwise conv support #6267
* Decrease test times by introducing testing model #6235
* Add support for parsing the any dimension. #6277
* Improve error messages for memory verifier and gpu memory verifier #6281
* Reflect Compile-Time CMake Options into libtvm.so #6280
* Add cmake options into libinfo #6286
* Update slice to infer attributes when not graph inputs #6276
* Use rpc.LocalSession for simple tests #6294
* Fix random fail #6312
* Fix resize test #6298
* Fix cython FFI compact with np.int64 #6321
* Fix relay vm optimize #6322
* Changed TVMCTVMContext to TVMContext #6306
* Make able to compile with MSVC #6341
* ROCm changed name of library and removed the old one in ROCm 3.7 release. #6345
* Compatible for ROCm before 3.7 #6359
* Use clear name that is separate from ASF brand for cache #6360
* Fix `Dockerfile.demo_android` #6361
* Fx sparse dense schedule on cuda #5803
* Fix strategy for sparse dense cuda #5782
* Fix x86 conv2d template when tuning with unpacked layout #5938
* Fix the filter width parameter in `depthwise_conv2d` #6081
* Fix reshape usage in ARM schedule #5732
* Missing header #4865
* Fix `conv2d_transpose` output padding #6236
* Simplify reduce expression in te.gradient #6611

# API Changes
* `tvm.module` -> `tvm.runtime.module`
* `tvm.module.load` -> `tvm.runtime.load_module`
* `tvm.module.enabled` -> `tvm.runtime.enabled`
* `tvm.module.system_lib` -> `tvm.runtime.system_lib`
* `tvm.relay.Module` -> `tvm.IRModule`
* `tvm.create_schedule` -> `tvm.te.create_schedule`
* `tvm.placeholder` -> `tvm.te.placeholder`
* `tvm.compute` -> `tvm.te.compute`

# Deprecation
* Deprecate NNVM (#4535, #4562, #4565, #4571)
* Deprecate FreeStmt #5890
* Remove legacy `compute_expr.h` #5738
* Deprecate OpenGL #5711, #5712


## v0.8.0 (2021-11-24)

  - [Overview](#overview)
  - [Accepted RFCs](#accepted-rfcs)
  - [Features and Improvements](#features-and-improvements)
    - [TE, TIR, TVMScript](#te-tir-tvmscript)
    - [AutoTVM, AutoScheduler, Meta Schedule](#autotvm-autoscheduler-meta-schedule)
    - [Operator Coverage](#operator-coverage)
    - [Training](#training)
    - [Relay](#relay)
    - [MicroTVM, AOT, Graph Executor and VM](#microtvm-aot-graph-executor-and-vm)
    - [Arithmetic Analysis](#arithmetic-analysis)
    - [Frontends](#frontends)
    - [Codegen Backends and Runtime](#codegen-backends-and-runtime)
    - [BYOC Integration with Vendor Libraries: TensorRT, ACL, VitisAI](#byoc-integration-with-vendor-libraries-tensorrt-acl-vitisai)
    - [TVMC](#tvmc)
    - [Rust Binding](#rust-binding)
    - [Misc](#misc)

## Overview

Apache TVM v0.8 brings several major exciting experimental features, including:
- PaddlePaddle frontend
- TVMScript: round-trippable python-based syntax for TIR
- TorchScript integration
- TensorIR scheduling language
- TensorRT and CUTLASS integration via BYOC
- Int4 TensorCore support in AutoTVM
- MicroTVM Project API and Zephyr, Arduino support
- AOT executor
- Robust Windows support
- Affine analysis infra: iter-affine-map
- Improved Vulkan backend
- CUDA graph support in TVM runtime

Besides, The community has been working together to refactor and evolve the existing infrastructure, including but not limited to:
- Relay compilation engine
- Relay pattern language
- CI and build process
- Refactoring documentation and tutorials
- Stablizing AutoScheduler
- Stablizing TVMC command line driver interface
- Stablizing target system
- Frontend coverage, quantization, dynamic shape, training

Full changelog: https://gist.github.com/junrushao1994/c669905dbc41edc2e691316df49d8562.

## Accepted RFCs

The community has adopted a [formal RFC process](https://github.com/apache/tvm-rfcs). Below is a list of the formal RFCs accepted by the community since then:
- [RFC-0005] Meta schedule (AutoTIR)
- [RFC-0006] Automatic mixed-precision pass and support
- [RFC-0007] Parametrized unit tests
- [RFC-0008] MicroTVM Project API
- [RFC-0009] Unified static memory planner
- [RFC-0010] Target-registered compiler flow customisation
- [RFC-0011] Arm® Ethos-U integration
- [RFC-0014] Pipeline executor
- [RFC-0015] Use CMSIS-NN with TVM
- [RFC-0019] Add PaddlePaddle frontend
- [RFC-0020] Extend metadata in project option
- [RFC-0022] TIR non-scalar constants
- [RFC-0023] Adding annotation field to `tir.allocate` nodes
- [RFC-0025] PyTorchTVM
- [RFC-0027] Formalize TVM documentation organization
- [RFC-0028] Command line composition from internal registry
- [RFC-0029] Migrating target attributes to IRModule
- [RFC-0030] Command line configuration files
- [RFC-0031] C Device API
- [RFC-0036] TVMScript namespace
- [RFC-0041] Update TVMScript block syntax

## Features and Improvements
### TE, TIR, TVMScript

- TVMScript parser and printer [#7630](https://github.com/apache/tvm/pull/7630) [#9115](https://github.com/apache/tvm/pull/9115) [#9286](https://github.com/apache/tvm/pull/9286)
- Scheduleable TIR (S-TIR) infrastructure, analysis and lowering passes [#7553](https://github.com/apache/tvm/pull/7553) [#7765](https://github.com/apache/tvm/pull/7765) [#7847](https://github.com/apache/tvm/pull/7847) [#8114](https://github.com/apache/tvm/pull/8114) [#8121](https://github.com/apache/tvm/pull/8121) [#7873](https://github.com/apache/tvm/pull/7873) [#7923](https://github.com/apache/tvm/pull/7923) [#7962](https://github.com/apache/tvm/pull/7962) [#7848](https://github.com/apache/tvm/pull/7848) [#8044](https://github.com/apache/tvm/pull/8044) [#7806](https://github.com/apache/tvm/pull/7806)
- S-TIR schedule primitives: `compute-inline`, `reverse-compute-inline`, `fuse`, `split`, `rfactor`, `storage-align`, `vectorize`, `unroll`, `bind`, `reorder`, `cache-read`, `cache-write`, `compute-at`, `reverse-compute-at`, `decompose-reduction` [#8170](https://github.com/apache/tvm/pull/8170) [#8467](https://github.com/apache/tvm/pull/8467) [#8544](https://github.com/apache/tvm/pull/8544) [#8693](https://github.com/apache/tvm/pull/8693) [#8716](https://github.com/apache/tvm/pull/8716) [#8767](https://github.com/apache/tvm/pull/8767) [#8863](https://github.com/apache/tvm/pull/8863) [#8943](https://github.com/apache/tvm/pull/8943) [#9041](https://github.com/apache/tvm/pull/9041)
- While loop in TIR [#7425](https://github.com/apache/tvm/pull/7425) [#9004](https://github.com/apache/tvm/pull/9004)
- Metaprogramming in S-TIR via `specialize` [#8354](https://github.com/apache/tvm/pull/8354)
- Support Return value in TIR [#7084](https://github.com/apache/tvm/pull/7084) [#7932](https://github.com/apache/tvm/pull/7932)
- Storage scope support in `PointerType` [#8017](https://github.com/apache/tvm/pull/8017) [#8366](https://github.com/apache/tvm/pull/8366) [#8463](https://github.com/apache/tvm/pull/8463)
- Creation of S-TIR via TE compute [#7987](https://github.com/apache/tvm/pull/7987)

### AutoTVM, AutoScheduler, Meta Schedule

- PopenPoolExecutor is used to replace python native library to provide better multiprocessing support as well as enable auto-tuning in Jupyter notebooks for AutoTVM and AutoScheduler [#6959](https://github.com/apache/tvm/pull/6959) [#8492](https://github.com/apache/tvm/pull/8492) [#8913](https://github.com/apache/tvm/pull/8913) [#8820](https://github.com/apache/tvm/pull/8820) [#8851](https://github.com/apache/tvm/pull/8851)
- AutoScheduler improvement and stabilization: task scheduler, layout rewrite, early stopping, dispatching [#6945](https://github.com/apache/tvm/pull/6945) [#6750](https://github.com/apache/tvm/pull/6750) [#6987](https://github.com/apache/tvm/pull/6987) [#7156](https://github.com/apache/tvm/pull/7156) [#8862](https://github.com/apache/tvm/pull/8862) [#8995](https://github.com/apache/tvm/pull/8995) [#7571](https://github.com/apache/tvm/pull/7571) [#7376](https://github.com/apache/tvm/pull/7376) [#7377](https://github.com/apache/tvm/pull/7377) [#7344](https://github.com/apache/tvm/pull/7344) [#7185](https://github.com/apache/tvm/pull/7185)
- AutoScheduler support for sparse workloads [#7313](https://github.com/apache/tvm/pull/7313) [#7635](https://github.com/apache/tvm/pull/7635) [#8065](https://github.com/apache/tvm/pull/8065)
- AutoScheduler support for Vulkan, ROCm, Mali [#7626](https://github.com/apache/tvm/pull/7626) [#7038](https://github.com/apache/tvm/pull/7038) [#7132](https://github.com/apache/tvm/pull/7132)
- AutoTVM support for int4 TensorCore [#7831](https://github.com/apache/tvm/pull/7831) [#8402](https://github.com/apache/tvm/pull/8402)
- Meta Schedule core infrastructure, builder runner and database [#8615](https://github.com/apache/tvm/pull/8615) [#8623](https://github.com/apache/tvm/pull/8623) [#8642](https://github.com/apache/tvm/pull/8642) [#8817](https://github.com/apache/tvm/pull/8817) [#9079](https://github.com/apache/tvm/pull/9079) [#9132](https://github.com/apache/tvm/pull/9132) [#9154](https://github.com/apache/tvm/pull/9154) [#9053](https://github.com/apache/tvm/pull/9053) [#9059](https://github.com/apache/tvm/pull/9059) [#9044](https://github.com/apache/tvm/pull/9044) [#9111](https://github.com/apache/tvm/pull/9111) [#9061](https://github.com/apache/tvm/pull/9061) [#9153](https://github.com/apache/tvm/pull/9153)

### Operator Coverage
- Operators for Int-8 vision transformer on GPU [#7814](https://github.com/apache/tvm/pull/7814)
- Optimizing NMS and ROI-related kernel on GPU [#7257](https://github.com/apache/tvm/pull/7257) [#7172](https://github.com/apache/tvm/pull/7172) [#7136](https://github.com/apache/tvm/pull/7136) [#7796](https://github.com/apache/tvm/pull/7796) [#7463](https://github.com/apache/tvm/pull/7463) [#6516](https://github.com/apache/tvm/pull/6516) [#7440](https://github.com/apache/tvm/pull/7440) [#7666](https://github.com/apache/tvm/pull/7666) [#8174](https://github.com/apache/tvm/pull/8174)
- Support and optimize sparse operators [#8605](https://github.com/apache/tvm/pull/8605) [#7477](https://github.com/apache/tvm/pull/7477) [#7435](https://github.com/apache/tvm/pull/7435) [#6889](https://github.com/apache/tvm/pull/6889) [#6580](https://github.com/apache/tvm/pull/6580) [#8437](https://github.com/apache/tvm/pull/8437)
- Sort-related operators and optimization [#9184](https://github.com/apache/tvm/pull/9184) [#7669](https://github.com/apache/tvm/pull/7669) [#8672](https://github.com/apache/tvm/pull/8672) [#7611](https://github.com/apache/tvm/pull/7611) [#7195](https://github.com/apache/tvm/pull/7195) [#7056](https://github.com/apache/tvm/pull/7056) [#6978](https://github.com/apache/tvm/pull/6978)
- Support for einsum operator [#6370](https://github.com/apache/tvm/pull/6370)
- Matmul, dense operators and their optimization [#8921](https://github.com/apache/tvm/pull/8921) [#8527](https://github.com/apache/tvm/pull/8527) [#8234](https://github.com/apache/tvm/pull/8234) [#8250](https://github.com/apache/tvm/pull/8250) [#6616](https://github.com/apache/tvm/pull/6616) [#8229](https://github.com/apache/tvm/pull/8229) [#8401](https://github.com/apache/tvm/pull/8401) [#7404](https://github.com/apache/tvm/pull/7404) [#8669](https://github.com/apache/tvm/pull/8669)
- Convolution and pooling operators and their optimization [#8620](https://github.com/apache/tvm/pull/8620) [#8936](https://github.com/apache/tvm/pull/8936) [#8584](https://github.com/apache/tvm/pull/8584) [#7075](https://github.com/apache/tvm/pull/7075) [#7142](https://github.com/apache/tvm/pull/7142) [#7515](https://github.com/apache/tvm/pull/7515) [#6999](https://github.com/apache/tvm/pull/6999) [#6899](https://github.com/apache/tvm/pull/6899) [#6840](https://github.com/apache/tvm/pull/6840) [#6137](https://github.com/apache/tvm/pull/6137) [#6802](https://github.com/apache/tvm/pull/6802) [#6445](https://github.com/apache/tvm/pull/6445) [#6711](https://github.com/apache/tvm/pull/6711) [#6714](https://github.com/apache/tvm/pull/6714) [#8167](https://github.com/apache/tvm/pull/8167) [#8222](https://github.com/apache/tvm/pull/8222) [#8275](https://github.com/apache/tvm/pull/8275) [#8276](https://github.com/apache/tvm/pull/8276) [#8422](https://github.com/apache/tvm/pull/8422) [#8430](https://github.com/apache/tvm/pull/8430) [#6687](https://github.com/apache/tvm/pull/6687) [#7928](https://github.com/apache/tvm/pull/7928) [#8897](https://github.com/apache/tvm/pull/8897)
- Scatter and gather operators and their optimization [#8479](https://github.com/apache/tvm/pull/8479) [#7600](https://github.com/apache/tvm/pull/7600) [#7044](https://github.com/apache/tvm/pull/7044) [#7464](https://github.com/apache/tvm/pull/7464) [#7233](https://github.com/apache/tvm/pull/7233) [#6533](https://github.com/apache/tvm/pull/6533) [#6856](https://github.com/apache/tvm/pull/6856) [#6854](https://github.com/apache/tvm/pull/6854) [#7927](https://github.com/apache/tvm/pull/7927) [#8105](https://github.com/apache/tvm/pull/8105)
- Prefix scan, cumsum and cumprod [#7722](https://github.com/apache/tvm/pull/7722) [#7303](https://github.com/apache/tvm/pull/7303) [#7314](https://github.com/apache/tvm/pull/7314) [#7334](https://github.com/apache/tvm/pull/7334) [#7123](https://github.com/apache/tvm/pull/7123) [#6868](https://github.com/apache/tvm/pull/6868)
- Dynamic shape and shape functions [#7414](https://github.com/apache/tvm/pull/7414) [#6979](https://github.com/apache/tvm/pull/6979) [#6912](https://github.com/apache/tvm/pull/6912) [#6898](https://github.com/apache/tvm/pull/6898) [#6373](https://github.com/apache/tvm/pull/6373) [#8068](https://github.com/apache/tvm/pull/8068) [#7490](https://github.com/apache/tvm/pull/7490) [#7487](https://github.com/apache/tvm/pull/7487)
- Miscellaneous improvement. Operators including: reshape, resize, pad, PRNG, transpose, where, softmax, concat, nll_loss, space_to_batch_nd, batch_to_space_nd, slice_like; Libraries including thrust, cuDNN, cuBLAS, MIOpen; Improving schedules for generic reduction and softmax. [#8592](https://github.com/apache/tvm/pull/8592) [#7375](https://github.com/apache/tvm/pull/7375) [#7287](https://github.com/apache/tvm/pull/7287) [#7184](https://github.com/apache/tvm/pull/7184) [#7131](https://github.com/apache/tvm/pull/7131) [#7086](https://github.com/apache/tvm/pull/7086) [#7083](https://github.com/apache/tvm/pull/7083) [#8030](https://github.com/apache/tvm/pull/8030) [#6851](https://github.com/apache/tvm/pull/6851) [#6477](https://github.com/apache/tvm/pull/6477) [#8346](https://github.com/apache/tvm/pull/8346) [#6759](https://github.com/apache/tvm/pull/6759) [#8028](https://github.com/apache/tvm/pull/8028) [#8056](https://github.com/apache/tvm/pull/8056) [#8369](https://github.com/apache/tvm/pull/8369) [#7468](https://github.com/apache/tvm/pull/7468) [#7458](https://github.com/apache/tvm/pull/7458) [#7194](https://github.com/apache/tvm/pull/7194) [#8138](https://github.com/apache/tvm/pull/8138) [#8543](https://github.com/apache/tvm/pull/8543)

### Training

- Relay AutoDiff [#7677](https://github.com/apache/tvm/pull/7677) [#8318](https://github.com/apache/tvm/pull/8318)
- TE AutoDiff [#7321](https://github.com/apache/tvm/pull/7321)
- Gradient operators [#7685](https://github.com/apache/tvm/pull/7685) [#7340](https://github.com/apache/tvm/pull/7340) [#6767](https://github.com/apache/tvm/pull/6767) [#8307](https://github.com/apache/tvm/pull/8307) [#7357](https://github.com/apache/tvm/pull/7357) [#6827](https://github.com/apache/tvm/pull/6827)

### Relay

- Pattern language and mixed-mode visitor: matching more IR constructs, fuzzy matching; converting more passes to non-recursive.  [#8843](https://github.com/apache/tvm/pull/8843) [#7754](https://github.com/apache/tvm/pull/7754) [#7355](https://github.com/apache/tvm/pull/7355) [#7332](https://github.com/apache/tvm/pull/7332) [#7282](https://github.com/apache/tvm/pull/7282) [#7151](https://github.com/apache/tvm/pull/7151) [#7120](https://github.com/apache/tvm/pull/7120) [#6958](https://github.com/apache/tvm/pull/6958) [#7507](https://github.com/apache/tvm/pull/7507) [#8325](https://github.com/apache/tvm/pull/8325) [#8774](https://github.com/apache/tvm/pull/8774) [#7817](https://github.com/apache/tvm/pull/7817) [#7374](https://github.com/apache/tvm/pull/7374) [#6695](https://github.com/apache/tvm/pull/6695) [#6704](https://github.com/apache/tvm/pull/6704)
- Improving or adding passes including ExtractOperators, SimplifyExpr, DynamicToStatic, DefuseOps, ConvertLayout, FoldConstant. Added a set of utilities that allows a model to be run efficiently on TensorCores [#9253](https://github.com/apache/tvm/pull/9253) [#9245](https://github.com/apache/tvm/pull/9245) [#8996](https://github.com/apache/tvm/pull/8996) [#7827](https://github.com/apache/tvm/pull/7827) [#9034](https://github.com/apache/tvm/pull/9034) [#7807](https://github.com/apache/tvm/pull/7807) [#8755](https://github.com/apache/tvm/pull/8755) [#7731](https://github.com/apache/tvm/pull/7731) [#7368](https://github.com/apache/tvm/pull/7368) [#7603](https://github.com/apache/tvm/pull/7603) [#7656](https://github.com/apache/tvm/pull/7656) [#7423](https://github.com/apache/tvm/pull/7423) [#7354](https://github.com/apache/tvm/pull/7354) [#6946](https://github.com/apache/tvm/pull/6946) [#6748](https://github.com/apache/tvm/pull/6748) [#6720](https://github.com/apache/tvm/pull/6720) [#6776](https://github.com/apache/tvm/pull/6776) [#7835](https://github.com/apache/tvm/pull/7835) [#7895](https://github.com/apache/tvm/pull/7895) [#8205](https://github.com/apache/tvm/pull/8205)
- TECompiler and refactoring of compilation workflow [#9103](https://github.com/apache/tvm/pull/9103) [#8974](https://github.com/apache/tvm/pull/8974) [#8886](https://github.com/apache/tvm/pull/8886) [#8802](https://github.com/apache/tvm/pull/8802) [#8501](https://github.com/apache/tvm/pull/8501) [#8526](https://github.com/apache/tvm/pull/8526) [#8486](https://github.com/apache/tvm/pull/8486) [#8597](https://github.com/apache/tvm/pull/8597) [#7518](https://github.com/apache/tvm/pull/7518) [#7552](https://github.com/apache/tvm/pull/7552) [#8914](https://github.com/apache/tvm/pull/8914) [#9130](https://github.com/apache/tvm/pull/9130)
- Quantization and automatic-mixed precision [#8883](https://github.com/apache/tvm/pull/8883) [#8810](https://github.com/apache/tvm/pull/8810) [#8644](https://github.com/apache/tvm/pull/8644) [#7613](https://github.com/apache/tvm/pull/7613) [#8069](https://github.com/apache/tvm/pull/8069) [#8341](https://github.com/apache/tvm/pull/8341) [#8126](https://github.com/apache/tvm/pull/8126) [#8460](https://github.com/apache/tvm/pull/8460)
- Parser, printer and diagnostic [#7347](https://github.com/apache/tvm/pull/7347) [#6274](https://github.com/apache/tvm/pull/6274) [#6692](https://github.com/apache/tvm/pull/6692) [#8352](https://github.com/apache/tvm/pull/8352) [#8000](https://github.com/apache/tvm/pull/8000)

### MicroTVM, AOT, Graph Executor and VM

- Pipeline Executor [#8702](https://github.com/apache/tvm/pull/8702) [#9108](https://github.com/apache/tvm/pull/9108)
- CUDA graph integration in graph executor [#7616](https://github.com/apache/tvm/pull/7616)
- Enable add `set_output_zero_copy` in graph executor [#8497](https://github.com/apache/tvm/pull/8497)
- VM: memory allocation improvement, shape function improvement and misc [#7746](https://github.com/apache/tvm/pull/7746) [#7451](https://github.com/apache/tvm/pull/7451) [#7413](https://github.com/apache/tvm/pull/7413) [#7210](https://github.com/apache/tvm/pull/7210) [#8040](https://github.com/apache/tvm/pull/8040) [#6938](https://github.com/apache/tvm/pull/6938) [#8661](https://github.com/apache/tvm/pull/8661) [#7676](https://github.com/apache/tvm/pull/7676) [#8285](https://github.com/apache/tvm/pull/8285)
- AOT compilation and execution [#8697](https://github.com/apache/tvm/pull/8697) [#7785](https://github.com/apache/tvm/pull/7785) [#8014](https://github.com/apache/tvm/pull/8014) [#8023](https://github.com/apache/tvm/pull/8023) [#8096](https://github.com/apache/tvm/pull/8096) [#8075](https://github.com/apache/tvm/pull/8075)
- Project API infrastructure: [#8380](https://github.com/apache/tvm/pull/8380) [#8963](https://github.com/apache/tvm/pull/8963) [#8708](https://github.com/apache/tvm/pull/8708) [#8019](https://github.com/apache/tvm/pull/8019)
- MicroTVM, Zephyr, Arduino RVM, AutoTVM support [#9320](https://github.com/apache/tvm/pull/9320) [#8941](https://github.com/apache/tvm/pull/8941) [#7804](https://github.com/apache/tvm/pull/7804) [#7786](https://github.com/apache/tvm/pull/7786) [#7449](https://github.com/apache/tvm/pull/7449) [#7891](https://github.com/apache/tvm/pull/7891) [#7915](https://github.com/apache/tvm/pull/7915) [#8055](https://github.com/apache/tvm/pull/8055) [#8037](https://github.com/apache/tvm/pull/8037) [#8386](https://github.com/apache/tvm/pull/8386) [#8519](https://github.com/apache/tvm/pull/8519) [#8748](https://github.com/apache/tvm/pull/8748) [8154](https://github.com/apache/tvm/pull/8154) [#8945](https://github.com/apache/tvm/pull/8945) [#8624](https://github.com/apache/tvm/pull/8624) [#8701](https://github.com/apache/tvm/pull/8701) [#7723](https://github.com/apache/tvm/pull/7723) [#8715](https://github.com/apache/tvm/pull/8715) [#7225](https://github.com/apache/tvm/pull/7225) [#6964](https://github.com/apache/tvm/pull/6964) [#7813](https://github.com/apache/tvm/pull/7813) [#7528](https://github.com/apache/tvm/pull/7528)
- The pure C runtime (CRT) [#7398](https://github.com/apache/tvm/pull/7398) [#7333](https://github.com/apache/tvm/pull/7333) [#7095](https://github.com/apache/tvm/pull/7095) [#7225](https://github.com/apache/tvm/pull/7225)
- Model library format [#8270](https://github.com/apache/tvm/pull/8270) [#8072](https://github.com/apache/tvm/pull/8072) [#7938](https://github.com/apache/tvm/pull/7938)

### Arithmetic Analysis

- Tighter bounds and more simplification on cast [#6771](https://github.com/apache/tvm/pull/6771) [#7045](https://github.com/apache/tvm/pull/7045)
- Introducing iterator (quasi-) affine map detection [#6667](https://github.com/apache/tvm/pull/6667) [#7752](https://github.com/apache/tvm/pull/7752) [#7759](https://github.com/apache/tvm/pull/7759)
- Inverse of iterator affine map [#8384](https://github.com/apache/tvm/pull/8384) [#8427](https://github.com/apache/tvm/pull/8427)
- Subspace division in iterator affine map [#7760](https://github.com/apache/tvm/pull/7760)

### Frontends

- PaddlePaddle initial support [#8645](https://github.com/apache/tvm/pull/8645)  [#9124](https://github.com/apache/tvm/pull/9124) [#9126](https://github.com/apache/tvm/pull/9126) [#9295](https://github.com/apache/tvm/pull/9295) [#9370](https://github.com/apache/tvm/pull/9370) [#9236](https://github.com/apache/tvm/pull/9236) [#9283](https://github.com/apache/tvm/pull/9283)
- ONNX support, including better handling of control flow, coverage of more operators, better dynamic shape support, more tests. [#9265](https://github.com/apache/tvm/pull/9265) [#9178](https://github.com/apache/tvm/pull/9178) [#9146](https://github.com/apache/tvm/pull/9146) [#8894](https://github.com/apache/tvm/pull/8894) [#8966](https://github.com/apache/tvm/pull/8966) [#8967](https://github.com/apache/tvm/pull/8967) [#7818](https://github.com/apache/tvm/pull/7818) [#9000](https://github.com/apache/tvm/pull/9000) [#9001](https://github.com/apache/tvm/pull/9001) [#9066](https://github.com/apache/tvm/pull/9066) [#9028](https://github.com/apache/tvm/pull/9028) [#9002](https://github.com/apache/tvm/pull/9002) [#8985](https://github.com/apache/tvm/pull/8985) [#9019](https://github.com/apache/tvm/pull/9019) [#9017](https://github.com/apache/tvm/pull/9017) [#8972](https://github.com/apache/tvm/pull/8972) [#7802](https://github.com/apache/tvm/pull/7802) [#7800](https://github.com/apache/tvm/pull/7800) [#7781](https://github.com/apache/tvm/pull/7781) [#8919](https://github.com/apache/tvm/pull/8919) [#9054](https://github.com/apache/tvm/pull/9054) [#8906](https://github.com/apache/tvm/pull/8906) [#8933](https://github.com/apache/tvm/pull/8933) [#8959](https://github.com/apache/tvm/pull/8959) [#8907](https://github.com/apache/tvm/pull/8907) [#7771](https://github.com/apache/tvm/pull/7771) [#8923](https://github.com/apache/tvm/pull/8923) [#8924](https://github.com/apache/tvm/pull/8924) [#7755](https://github.com/apache/tvm/pull/7755) [#7720](https://github.com/apache/tvm/pull/7720) [#8773](https://github.com/apache/tvm/pull/8773) [#8872](https://github.com/apache/tvm/pull/8872) [#7655](https://github.com/apache/tvm/pull/7655) [#8741](https://github.com/apache/tvm/pull/8741) [#7633](https://github.com/apache/tvm/pull/7633) [#8781](https://github.com/apache/tvm/pull/8781) [#8866](https://github.com/apache/tvm/pull/8866) [#8867](https://github.com/apache/tvm/pull/8867) [#7522](https://github.com/apache/tvm/pull/7522) [#7519](https://github.com/apache/tvm/pull/7519) [#7489](https://github.com/apache/tvm/pull/7489) [#7438](https://github.com/apache/tvm/pull/7438) [#7429](https://github.com/apache/tvm/pull/7429) [#7364](https://github.com/apache/tvm/pull/7364) [#7300](https://github.com/apache/tvm/pull/7300) [#7259](https://github.com/apache/tvm/pull/7259) [#7243](https://github.com/apache/tvm/pull/7243) [#7237](https://github.com/apache/tvm/pull/7237) [#7208](https://github.com/apache/tvm/pull/7208) [#7189](https://github.com/apache/tvm/pull/7189) [#7115](https://github.com/apache/tvm/pull/7115) [#7109](https://github.com/apache/tvm/pull/7109) [#7089](https://github.com/apache/tvm/pull/7089) [#7036](https://github.com/apache/tvm/pull/7036) [#7031](https://github.com/apache/tvm/pull/7031) [#6839](https://github.com/apache/tvm/pull/6839) [#6351](https://github.com/apache/tvm/pull/6351) [#7842](https://github.com/apache/tvm/pull/7842) [#7844](https://github.com/apache/tvm/pull/7844) [#6646](https://github.com/apache/tvm/pull/6646) [#6647](https://github.com/apache/tvm/pull/6647) [#6681](https://github.com/apache/tvm/pull/6681) [#6700](https://github.com/apache/tvm/pull/6700) [#7883](https://github.com/apache/tvm/pull/7883) [#6726](https://github.com/apache/tvm/pull/6726) [#6730](https://github.com/apache/tvm/pull/6730) [#7899](https://github.com/apache/tvm/pull/7899) [#7900](https://github.com/apache/tvm/pull/7900) [#7906](https://github.com/apache/tvm/pull/7906) [#7934](https://github.com/apache/tvm/pull/7934) [#7956](https://github.com/apache/tvm/pull/7956) [#8007](https://github.com/apache/tvm/pull/8007) [#8011](https://github.com/apache/tvm/pull/8011) [#8084](https://github.com/apache/tvm/pull/8084) [#8099](https://github.com/apache/tvm/pull/8099) [#8189](https://github.com/apache/tvm/pull/8189) [#8191](https://github.com/apache/tvm/pull/8191) [#8304](https://github.com/apache/tvm/pull/8304) [#8321](https://github.com/apache/tvm/pull/8321) [#8337](https://github.com/apache/tvm/pull/8337) [#8356](https://github.com/apache/tvm/pull/8356) [#8385](https://github.com/apache/tvm/pull/8385) [#8502](https://github.com/apache/tvm/pull/8502) [#8426](https://github.com/apache/tvm/pull/8426) [#8440](https://github.com/apache/tvm/pull/8440) [#8456](https://github.com/apache/tvm/pull/8456) [#8475](https://github.com/apache/tvm/pull/8475) [#7391](https://github.com/apache/tvm/pull/7391) [#7394](https://github.com/apache/tvm/pull/7394) [#8621](https://github.com/apache/tvm/pull/8621) [#8322](https://github.com/apache/tvm/pull/8322) [#8323](https://github.com/apache/tvm/pull/8323) [#8435](https://github.com/apache/tvm/pull/8435) [#8436](https://github.com/apache/tvm/pull/8436) [#8455](https://github.com/apache/tvm/pull/8455) [#7353](https://github.com/apache/tvm/pull/7353) [#7215](https://github.com/apache/tvm/pull/7215)
- TensorFlow and TFLite, including more operators, better TensorArray support and quantization [#9404](https://github.com/apache/tvm/pull/9404) [#9256](https://github.com/apache/tvm/pull/9256) [#8689](https://github.com/apache/tvm/pull/8689) [#7789](https://github.com/apache/tvm/pull/7789) [#7736](https://github.com/apache/tvm/pull/7736) [#8763](https://github.com/apache/tvm/pull/8763) [#8647](https://github.com/apache/tvm/pull/8647) [#8648](https://github.com/apache/tvm/pull/8648) [#8558](https://github.com/apache/tvm/pull/8558) [#8780](https://github.com/apache/tvm/pull/8780) [#8538](https://github.com/apache/tvm/pull/8538) [#7659](https://github.com/apache/tvm/pull/7659) [#7639](https://github.com/apache/tvm/pull/7639) [#7531](https://github.com/apache/tvm/pull/7531) [#7520](https://github.com/apache/tvm/pull/7520) [#7502](https://github.com/apache/tvm/pull/7502) [#7496](https://github.com/apache/tvm/pull/7496) [#7473](https://github.com/apache/tvm/pull/7473) [#7452](https://github.com/apache/tvm/pull/7452) [#7442](https://github.com/apache/tvm/pull/7442) [#7441](https://github.com/apache/tvm/pull/7441) [#7400](https://github.com/apache/tvm/pull/7400) [#7320](https://github.com/apache/tvm/pull/7320) [#7293](https://github.com/apache/tvm/pull/7293) [#7267](https://github.com/apache/tvm/pull/7267) [#7159](https://github.com/apache/tvm/pull/7159) [#7148](https://github.com/apache/tvm/pull/7148) [#7114](https://github.com/apache/tvm/pull/7114) [#7113](https://github.com/apache/tvm/pull/7113) [#7093](https://github.com/apache/tvm/pull/7093) [#7074](https://github.com/apache/tvm/pull/7074) [#7048](https://github.com/apache/tvm/pull/7048) [#7030](https://github.com/apache/tvm/pull/7030) [#6998](https://github.com/apache/tvm/pull/6998) [#6984](https://github.com/apache/tvm/pull/6984) [#6970](https://github.com/apache/tvm/pull/6970) [#6949](https://github.com/apache/tvm/pull/6949) [#6933](https://github.com/apache/tvm/pull/6933) [#6918](https://github.com/apache/tvm/pull/6918) [#6901](https://github.com/apache/tvm/pull/6901) [#6885](https://github.com/apache/tvm/pull/6885) [#6849](https://github.com/apache/tvm/pull/6849) [#5767](https://github.com/apache/tvm/pull/5767) [#6589](https://github.com/apache/tvm/pull/6589) [#6670](https://github.com/apache/tvm/pull/6670) [#6674](https://github.com/apache/tvm/pull/6674) [#6675](https://github.com/apache/tvm/pull/6675) [#7866](https://github.com/apache/tvm/pull/7866) [#6685](https://github.com/apache/tvm/pull/6685) [#7885](https://github.com/apache/tvm/pull/7885) [#6729](https://github.com/apache/tvm/pull/6729) [#7901](https://github.com/apache/tvm/pull/7901) [#6774](https://github.com/apache/tvm/pull/6774) [#6783](https://github.com/apache/tvm/pull/6783) [#6799](https://github.com/apache/tvm/pull/6799) [#7951](https://github.com/apache/tvm/pull/7951) [#8024](https://github.com/apache/tvm/pull/8024) [#8051](https://github.com/apache/tvm/pull/8051) [#8060](https://github.com/apache/tvm/pull/8060) [#8074](https://github.com/apache/tvm/pull/8074) [#8142](https://github.com/apache/tvm/pull/8142) [#8179](https://github.com/apache/tvm/pull/8179) [#8251](https://github.com/apache/tvm/pull/8251) [#8277](https://github.com/apache/tvm/pull/8277) [#8335](https://github.com/apache/tvm/pull/8335) [#8364](https://github.com/apache/tvm/pull/8364) [#8375](https://github.com/apache/tvm/pull/8375) [#8431](https://github.com/apache/tvm/pull/8431) [#8454](https://github.com/apache/tvm/pull/8454) [#6818](https://github.com/apache/tvm/pull/6818) [#8483](https://github.com/apache/tvm/pull/8483) [#9099](https://github.com/apache/tvm/pull/9099) [#9165](https://github.com/apache/tvm/pull/9165)
- PyTorch: more operators including activations, inplace operators, RNNs, NMS [#9371](https://github.com/apache/tvm/pull/9371) [#9204](https://github.com/apache/tvm/pull/9204) [#9185](https://github.com/apache/tvm/pull/9185) [#9135](https://github.com/apache/tvm/pull/9135) [#9133](https://github.com/apache/tvm/pull/9133) [#9015](https://github.com/apache/tvm/pull/9015) [#8839](https://github.com/apache/tvm/pull/8839) [#8718](https://github.com/apache/tvm/pull/8718) [#8699](https://github.com/apache/tvm/pull/8699) [#8692](https://github.com/apache/tvm/pull/8692) [#7712](https://github.com/apache/tvm/pull/7712) [#8753](https://github.com/apache/tvm/pull/8753) [#7694](https://github.com/apache/tvm/pull/7694) [#8583](https://github.com/apache/tvm/pull/8583) [#7675](https://github.com/apache/tvm/pull/7675) [#7646](https://github.com/apache/tvm/pull/7646) [#7606](https://github.com/apache/tvm/pull/7606) [#7592](https://github.com/apache/tvm/pull/7592) [#7569](https://github.com/apache/tvm/pull/7569) [#7544](https://github.com/apache/tvm/pull/7544) [#7549](https://github.com/apache/tvm/pull/7549) [#7535](https://github.com/apache/tvm/pull/7535) [#7517](https://github.com/apache/tvm/pull/7517) [#7465](https://github.com/apache/tvm/pull/7465) [#7397](https://github.com/apache/tvm/pull/7397) [#7371](https://github.com/apache/tvm/pull/7371) [#7348](https://github.com/apache/tvm/pull/7348) [#7346](https://github.com/apache/tvm/pull/7346) [#7325](https://github.com/apache/tvm/pull/7325) [#7231](https://github.com/apache/tvm/pull/7231) [#7174](https://github.com/apache/tvm/pull/7174) [#7154](https://github.com/apache/tvm/pull/7154) [#7137](https://github.com/apache/tvm/pull/7137) [#7134](https://github.com/apache/tvm/pull/7134) [#7133](https://github.com/apache/tvm/pull/7133) [#7128](https://github.com/apache/tvm/pull/7128) [#7088](https://github.com/apache/tvm/pull/7088) [#7023](https://github.com/apache/tvm/pull/7023) [#6900](https://github.com/apache/tvm/pull/6900) [#6602](https://github.com/apache/tvm/pull/6602) [#7845](https://github.com/apache/tvm/pull/7845) [#6659](https://github.com/apache/tvm/pull/6659) [#6740](https://github.com/apache/tvm/pull/6740) [#6782](https://github.com/apache/tvm/pull/6782) [#6784](https://github.com/apache/tvm/pull/6784) [#7958](https://github.com/apache/tvm/pull/7958) [#8192](https://github.com/apache/tvm/pull/8192) [#8397](https://github.com/apache/tvm/pull/8397) [#8398](https://github.com/apache/tvm/pull/8398) [#8403](https://github.com/apache/tvm/pull/8403) [#8447](https://github.com/apache/tvm/pull/8447) [#6829](https://github.com/apache/tvm/pull/6829)
- MXNet support. More operators and NLP model coverage in GluonNLP [#7568](https://github.com/apache/tvm/pull/7568) [#7409](https://github.com/apache/tvm/pull/7409) [#7209](https://github.com/apache/tvm/pull/7209) [#7191](https://github.com/apache/tvm/pull/7191) [#7062](https://github.com/apache/tvm/pull/7062) [#6561](https://github.com/apache/tvm/pull/6561) [#6699](https://github.com/apache/tvm/pull/6699)
- Misc: CoreML, Keras, DarkNet, etc. [#7667](https://github.com/apache/tvm/pull/7667) [#6676](https://github.com/apache/tvm/pull/6676) [#6651](https://github.com/apache/tvm/pull/6651) [#6963](https://github.com/apache/tvm/pull/6963) [#7949](https://github.com/apache/tvm/pull/7949) [#7035](https://github.com/apache/tvm/pull/7035) [#7446](https://github.com/apache/tvm/pull/7446) [#8562](https://github.com/apache/tvm/pull/8562) [#8599](https://github.com/apache/tvm/pull/8599)

### Codegen Backends and Runtime

- LLVM backend: recover LLVM support on windows; support target feature strings in function attributes; atomic support in NVPTX, ROCm; LLVM compatibility to LLVM 12+ [#9305](https://github.com/apache/tvm/pull/9305) [#9223](https://github.com/apache/tvm/pull/9223) [#9138](https://github.com/apache/tvm/pull/9138) [#8860](https://github.com/apache/tvm/pull/8860) [#8958](https://github.com/apache/tvm/pull/8958) [#6763](https://github.com/apache/tvm/pull/6763) [#6698](https://github.com/apache/tvm/pull/6698) [#6717](https://github.com/apache/tvm/pull/6717) [#6738](https://github.com/apache/tvm/pull/6738) [#8293](https://github.com/apache/tvm/pull/8293) [#6907](https://github.com/apache/tvm/pull/6907) [#7051](https://github.com/apache/tvm/pull/7051)
- ROCm 3.9 bitcode files search [#6865](https://github.com/apache/tvm/pull/6865)
- Vulkan and SPIR-V refactoring and major improvement in codegen and runtime. [A critical bug fix in SPIRV codegen](https://github.com/apache/tvm/pull/8102) allows the Vulkan backend to produce correct outputs on more hardwares and drivers. Added support for querying device specific hardware parameters and capabilities, dynamic shapes, irregular ops such as sorting and NMS, UBO, fp16, and vectorization. We can now run complicated models like MaskRCNN on Vulkan end to end. [#8904](https://github.com/apache/tvm/pull/8904) [#7833](https://github.com/apache/tvm/pull/7833) [#7717](https://github.com/apache/tvm/pull/7717) [#7681](https://github.com/apache/tvm/pull/7681) [#8746](https://github.com/apache/tvm/pull/8746) [#8813](https://github.com/apache/tvm/pull/8813) [#7609](https://github.com/apache/tvm/pull/7609) [#8882](https://github.com/apache/tvm/pull/8882) [#7607](https://github.com/apache/tvm/pull/7607) [#7591](https://github.com/apache/tvm/pull/7591) [#7574](https://github.com/apache/tvm/pull/7574) [#7572](https://github.com/apache/tvm/pull/7572) [#7833](https://github.com/apache/tvm/pull/7833) [#6662](https://github.com/apache/tvm/pull/6662) [#7969](https://github.com/apache/tvm/pull/7969) [#8013](https://github.com/apache/tvm/pull/8013) [#8048](https://github.com/apache/tvm/pull/8048) [#8098](https://github.com/apache/tvm/pull/8098) [#8102](https://github.com/apache/tvm/pull/8102) [#8107](https://github.com/apache/tvm/pull/8107) [#8127](https://github.com/apache/tvm/pull/8127) [#8151](https://github.com/apache/tvm/pull/8151) [#8196](https://github.com/apache/tvm/pull/8196) [#8320](https://github.com/apache/tvm/pull/8320) [#8588](https://github.com/apache/tvm/pull/8588) [#8332](https://github.com/apache/tvm/pull/8332) [#8333](https://github.com/apache/tvm/pull/8333) [#8348](https://github.com/apache/tvm/pull/8348) [#8528](https://github.com/apache/tvm/pull/8528)
- Metal language version upgrade (`MTLLanguageVersion2_3`), better codegen support, int64 support, various bug fixes [#7830](https://github.com/apache/tvm/pull/7830) [#7819](https://github.com/apache/tvm/pull/7819) [#7714](https://github.com/apache/tvm/pull/7714) [#7118](https://github.com/apache/tvm/pull/7118) [#7116](https://github.com/apache/tvm/pull/7116) [#7105](https://github.com/apache/tvm/pull/7105) [#7980](https://github.com/apache/tvm/pull/7980) [#8054](https://github.com/apache/tvm/pull/8054) [#8175](https://github.com/apache/tvm/pull/8175) [#8202](https://github.com/apache/tvm/pull/8202) [#8206](https://github.com/apache/tvm/pull/8206) [#8313](https://github.com/apache/tvm/pull/8313)
- OpenCL, VTA, Verilator: refactored code generator, better error messages, various bug fixes [#7834](https://github.com/apache/tvm/pull/7834) [#7777](https://github.com/apache/tvm/pull/7777) [#7761](https://github.com/apache/tvm/pull/7761) [#7100](https://github.com/apache/tvm/pull/7100) [#6125](https://github.com/apache/tvm/pull/6125) [#6126](https://github.com/apache/tvm/pull/6126) [#6191](https://github.com/apache/tvm/pull/6191) [#7834](https://github.com/apache/tvm/pull/7834) [#8256](https://github.com/apache/tvm/pull/8256) [#8257](https://github.com/apache/tvm/pull/8257) [#8731](https://github.com/apache/tvm/pull/8731) [#8756](https://github.com/apache/tvm/pull/8756) [#8973](https://github.com/apache/tvm/pull/8973)
- CUDA: enable `__launch_bounds__`, dynamic shared memory, TensorCore, BF16, half2, NVCC version upgrade [#9341](https://github.com/apache/tvm/pull/9341) [#8678](https://github.com/apache/tvm/pull/8678) [#7561](https://github.com/apache/tvm/pull/7561) [#7273](https://github.com/apache/tvm/pull/7273) [#7146](https://github.com/apache/tvm/pull/7146) [#7147](https://github.com/apache/tvm/pull/7147) [#7099](https://github.com/apache/tvm/pull/7099) [#7065](https://github.com/apache/tvm/pull/7065) [#7033](https://github.com/apache/tvm/pull/7033) [#7014](https://github.com/apache/tvm/pull/7014) [#7907](https://github.com/apache/tvm/pull/7907) [#7964](https://github.com/apache/tvm/pull/7964) [#9087](https://github.com/apache/tvm/pull/9087) [#8135](https://github.com/apache/tvm/pull/8135) [#8137](https://github.com/apache/tvm/pull/8137) [#8457](https://github.com/apache/tvm/pull/8457) [#8466](https://github.com/apache/tvm/pull/8466) [#8571](https://github.com/apache/tvm/pull/8571)
- ARM: CMSIS-NN, Ethos-N [#8653](https://github.com/apache/tvm/pull/8653) [#7628](https://github.com/apache/tvm/pull/7628) [#8951](https://github.com/apache/tvm/pull/8951) [#7506](https://github.com/apache/tvm/pull/7506) [#7443](https://github.com/apache/tvm/pull/7443) [#7858](https://github.com/apache/tvm/pull/7858) [#6982](https://github.com/apache/tvm/pull/6982) [#8795](https://github.com/apache/tvm/pull/8795) [#8806](https://github.com/apache/tvm/pull/8806) [#8833](https://github.com/apache/tvm/pull/8833) [#9147](https://github.com/apache/tvm/pull/9147) [#9159](https://github.com/apache/tvm/pull/9159) [#9160](https://github.com/apache/tvm/pull/9160) [#9162](https://github.com/apache/tvm/pull/9162) [#9163](https://github.com/apache/tvm/pull/9163) [#9167](https://github.com/apache/tvm/pull/9167) [#9209](https://github.com/apache/tvm/pull/9209) [#9386](https://github.com/apache/tvm/pull/9386) [#9387](https://github.com/apache/tvm/pull/9387)
- Hexagon: build, compilation, model launcher, more target options and better runtime [#7784](https://github.com/apache/tvm/pull/7784) [#6718](https://github.com/apache/tvm/pull/6718) [#8821](https://github.com/apache/tvm/pull/8821) [#8822](https://github.com/apache/tvm/pull/8822) [#9033](https://github.com/apache/tvm/pull/9033) [#8823](https://github.com/apache/tvm/pull/8823) [#8859](https://github.com/apache/tvm/pull/8859) [#8865](https://github.com/apache/tvm/pull/8865) [#8915](https://github.com/apache/tvm/pull/8915) [#8954](https://github.com/apache/tvm/pull/8954) [#9024](https://github.com/apache/tvm/pull/9024) [#9025](https://github.com/apache/tvm/pull/9025) [#8960](https://github.com/apache/tvm/pull/8960) [#8986](https://github.com/apache/tvm/pull/8986) [#9010](https://github.com/apache/tvm/pull/9010) [#9011](https://github.com/apache/tvm/pull/9011) [#9189](https://github.com/apache/tvm/pull/9189) [#9220](https://github.com/apache/tvm/pull/9220) [#9355](https://github.com/apache/tvm/pull/9355) [#9356](https://github.com/apache/tvm/pull/9356)


- WASM: Update support for latest emcc, add ffi test. [#6751](https://github.com/apache/tvm/pull/6751)

### BYOC Integration with Vendor Libraries: TensorRT, ACL, VitisAI

- TensorRT initial integration, stabilization, int8 calibration, dynamism support  [#6395](https://github.com/apache/tvm/pull/6395) [#7702](https://github.com/apache/tvm/pull/7702) [#7595](https://github.com/apache/tvm/pull/7595) [#7581](https://github.com/apache/tvm/pull/7581) [#7412](https://github.com/apache/tvm/pull/7412) [#7372](https://github.com/apache/tvm/pull/7372) [#9047](https://github.com/apache/tvm/pull/9047) [#8073](https://github.com/apache/tvm/pull/8073) [#8808](https://github.com/apache/tvm/pull/8808) [#6905](https://github.com/apache/tvm/pull/6905) [#7967](https://github.com/apache/tvm/pull/7967) [#8005](https://github.com/apache/tvm/pull/8005) [#8172](https://github.com/apache/tvm/pull/8172) [#8461](https://github.com/apache/tvm/pull/8461) [#8506](https://github.com/apache/tvm/pull/8506) [#8607](https://github.com/apache/tvm/pull/8607) [#7205](https://github.com/apache/tvm/pull/7205) [#7026](https://github.com/apache/tvm/pull/7026) [#7016](https://github.com/apache/tvm/pull/7016) [#7011](https://github.com/apache/tvm/pull/7011) [#6955](https://github.com/apache/tvm/pull/6955) [#6872](https://github.com/apache/tvm/pull/6872) [#7253](https://github.com/apache/tvm/pull/7253) [#6805](https://github.com/apache/tvm/pull/6805) [#9324](https://github.com/apache/tvm/pull/9324)
- Arm Compute Library (ACL) integration [#7649](https://github.com/apache/tvm/pull/7649) [#7206](https://github.com/apache/tvm/pull/7206) [#6532](https://github.com/apache/tvm/pull/6532) [#7121](https://github.com/apache/tvm/pull/7121) [#6724](https://github.com/apache/tvm/pull/6724) [#8149](https://github.com/apache/tvm/pull/8149) [#7251](https://github.com/apache/tvm/pull/7251) [#9396](https://github.com/apache/tvm/pull/9396)
- Verilator integration [#7406](https://github.com/apache/tvm/pull/7406) [#7351](https://github.com/apache/tvm/pull/7351) [#7286](https://github.com/apache/tvm/pull/7286) [#8094](https://github.com/apache/tvm/pull/8094)
- VitisAI integration [#6343](https://github.com/apache/tvm/pull/6343) [#7350](https://github.com/apache/tvm/pull/7350)
- BYOC infrastructure enhancement: improving control flow, AnnotateTarget, custom codegen [#6641](https://github.com/apache/tvm/pull/6641) [#6655](https://github.com/apache/tvm/pull/6655) [#6697](https://github.com/apache/tvm/pull/6697) [#6786](https://github.com/apache/tvm/pull/6786) [#7977](https://github.com/apache/tvm/pull/7977) [#8464](https://github.com/apache/tvm/pull/8464)


### TVMC

- MacOS support [#8396](https://github.com/apache/tvm/pull/8396)
- AutoScheduler support [#7070](https://github.com/apache/tvm/pull/7070)
- Support cross compiler options [#7922](https://github.com/apache/tvm/pull/7922)
- Python scripting [#7823](https://github.com/apache/tvm/pull/7823) [#7698](https://github.com/apache/tvm/pull/7698)
- More flexible input specification [#7366](https://github.com/apache/tvm/pull/7366) [#7788](https://github.com/apache/tvm/pull/7788)
- More options, `--disable-pass` and `--config` [#7816](https://github.com/apache/tvm/pull/7816) [#8253](https://github.com/apache/tvm/pull/8253)
- Allow passing optional arguments to importers [#7674](https://github.com/apache/tvm/pull/7674)
- Model library format (MLF) support [#8086](https://github.com/apache/tvm/pull/8086) [#8331](https://github.com/apache/tvm/pull/8331)
- More backend and library support: metal, ACL, Vulkan, OpenCL, ROCm, Vitis AI [#8282](https://github.com/apache/tvm/pull/8282) [#7508](https://github.com/apache/tvm/pull/7508) [#8359](https://github.com/apache/tvm/pull/8359) [#6831](https://github.com/apache/tvm/pull/6831) [#8896](https://github.com/apache/tvm/pull/8896) [#7577](https://github.com/apache/tvm/pull/7577)
- Support for the new target system [#7651](https://github.com/apache/tvm/pull/7651) [#7654](https://github.com/apache/tvm/pull/7654) [#6788](https://github.com/apache/tvm/pull/6788) [#7304](https://github.com/apache/tvm/pull/7304) [#6855](https://github.com/apache/tvm/pull/6855)

### Rust Binding

- Rust bindings installable via Cargo [#7503](https://github.com/apache/tvm/pull/7503) [#6678](https://github.com/apache/tvm/pull/6678) [#8631](https://github.com/apache/tvm/pull/8631) [#8665](https://github.com/apache/tvm/pull/8665)
- Initial support for diagnostic interface [#6656](https://github.com/apache/tvm/pull/6656)
- Fixes for using Python APIs from Rust [#7085](https://github.com/apache/tvm/pull/7085)
- Improve NDArray, GraphRt, Relay, IRModule, Array, Attrs bindings [#6563](https://github.com/apache/tvm/pull/6563) [#6741](https://github.com/apache/tvm/pull/6741) [#7138](https://github.com/apache/tvm/pull/7138) [#8353](https://github.com/apache/tvm/pull/8353) [#7082](https://github.com/apache/tvm/pull/7082)
- Improve error handling, error messages and fix memory leaks [#8289](https://github.com/apache/tvm/pull/8289) [#6815](https://github.com/apache/tvm/pull/6815) [#8714](https://github.com/apache/tvm/pull/8714) [#8725](https://github.com/apache/tvm/pull/8725)

### Misc

- Enhanced CPP-RPC implementation: allow user supplied work dir, support of CPP-RPC server for Apple, support adb-shell style CPP-RPC [#7670](https://github.com/apache/tvm/pull/7670) [#8224](https://github.com/apache/tvm/pull/8224) [#8223](https://github.com/apache/tvm/pull/8223) [#7766](https://github.com/apache/tvm/pull/7766) [#7013](https://github.com/apache/tvm/pull/7013)
- Use PopenWorker to handle RPC system: [#7889](https://github.com/apache/tvm/pull/7889) [#7757](https://github.com/apache/tvm/pull/7757) [#7961](https://github.com/apache/tvm/pull/7961)
- Fold target host into target [#7462](https://github.com/apache/tvm/pull/7462) [#7791](https://github.com/apache/tvm/pull/7791) [#7534](https://github.com/apache/tvm/pull/7534) [#8835](https://github.com/apache/tvm/pull/8835)
- Target-based intrinsic lowering and legalization [#7936](https://github.com/apache/tvm/pull/7936) [#7809](https://github.com/apache/tvm/pull/7809)
- Add target tags for all existing CUDA GPU models [#7410](https://github.com/apache/tvm/pull/7410)
- Linear Congruential Random Engine [#8642](https://github.com/apache/tvm/pull/8642)

## v0.9.0 (2022-07-14)

# Introduction

The TVM community has worked since the v0.8 release to deliver many exciting features and improvements. v0.9.0 is the first release on the new [quarterly release](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0067-quarterly-releases.md) schedule and includes many highlights, such as:

* [MetaSchedule's full implementation](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0005-meta-schedule-autotensorir.md)
* [ARM cascading scheduler](https://github.com/apache/tvm-rfcs/pull/37) for Arm Ethos(TM)-U NPUs
* [Collage](https://github.com/apache/tvm-rfcs/pull/62) which brings tuning to BYOC
* Several microTVM improvements
* New `tvm.relay.build` parameters - `runtime=`, `executor=`,
* AOT - Support for the C++ runtime (with `llvm` and `c` targets only) and support for host-driven AOT in the C runtime
* Hexagon RPC support
    * Testing via Hexagon SDK simulator and on device via Snapdragon-based HDK boards and phones
    * AOT and USMP support
    * Threading
    * Initial op support
* MLF - Support for multiple modules in a single MLF artifact
* Several TIR schedule primitives and transforms including (abridged):
    * `schedule.transform_layout` - Applies a layout transformation to a buffer as specified by an IndexMap.
    * `schedule.transform_block_layout` - Applies a schedule transformation to a block as specified by an IndexMap.
    * `schedule.set_axis_separators` - Sets axis separators in a buffer to lower to multi-dimensional memory (e.g. texture memory).
    * `transform.InjectSoftwarePipeline` - Transforms annotated loop nest into a pipeline prologue, body and epilogue where producers and consumers are overlapped.
    * `transform.CommonSubexprElimTIR` - Implements common-subexpression elimination for TIR.
    * `transform.InjectPTXAsyncCopy` - Rewrites global to shared memory copies in CUDA with async copy when annotated tir::attr::async_scope.
    * `transform.LowerCrossThreadReduction` - Enables support for reductions across threads on GPUs.
* And many more! See the list of RFCs and PRs included in v0.9.0 for a complete list, as well as [the full change list](https://github.com/apache/tvm/compare/v0.8.0...v0.9.0.rc0).

## RFCs

These RFCs have been merged in [apache/tvm-rfcs](https://github.com/apache/tvm-rfcs) since the last release.

 * [[RFC] TUNIP: TVMScript Unified Printer (#74)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0074-tvmscript-unified-printer.md) ([`48d47c5`](https://github.com/apache/tvm-rfcs/commit/48d47c526fbb509115adf5bbaf8699129f4fe2be))
 * [[RFC][Backend] RFC-CSI-NN2-Integration (#75)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0075_RISC-V_CSI-NN2_Intergration.md) ([`cfcf114`](https://github.com/apache/tvm-rfcs/commit/cfcf11464003af4c3201345a24ab380952fed944))
 * [[RFC] Introducing DeclBuffer (#70)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0070-introducing-decl-buffer.md) ([`87ff1fa`](https://github.com/apache/tvm-rfcs/commit/87ff1facd55c0a7cef45efdf2b7548ee299e8e06))
 * [[RFC][MLF] Model Library Format with Multiple Modules (#76)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0076_mlf_with_multiple_modules.md) ([`f47c6ad`](https://github.com/apache/tvm-rfcs/commit/f47c6ad660edf2c97e54279910e8b60b2bdf9ada))
 * [[RFC] UMA Universal Modular Accelerator Interface (#60)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0060_UMA_Unified_Modular_Accelerator_Interface.md) ([`6990e13`](https://github.com/apache/tvm-rfcs/commit/6990e1363c96945b6c9d19dc2d331306d2be2a17))
 * [[RFC] DietCode: An Auto-Scheduler for Dynamic Tensor Programs (#72)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0072-dynamic-autoscheduler.md) ([`a518000`](https://github.com/apache/tvm-rfcs/commit/a518000cbc82e53321f526d2090c7c8067607391))
 * [[RFC] Quarterly Releases (#67)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0067-quarterly-releases.md) ([`70293c7`](https://github.com/apache/tvm-rfcs/commit/70293c7f910ad70f4744d26295d6c4f6fe0366c5))
 * [RFC-BYOC-DNNL-Integration (#73)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0069-byoc-onednn-integration.md) ([`7aed0ca`](https://github.com/apache/tvm-rfcs/commit/7aed0ca0e1e636aebcfe7fd10585f4c7e1893674))
 * [[RFC] Relay Next Roadmap (#69)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0069-relax-roadmap.md) ([`ac15f2a`](https://github.com/apache/tvm-rfcs/commit/ac15f2a7bd77b106636ae5e4d8357a05d7267ef5))
 * [RFC: clarifying buffer declaration and access (#63)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0063-clarifying-buffer-declaration-and-access.md) ([`de4fe97`](https://github.com/apache/tvm-rfcs/commit/de4fe97ac0ab9d8fe9d4309a380a5ea278aa1493))
 * [Inclusive Language RFC (#68) (#68)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0068-inclusive-language.md) ([`4203bd2`](https://github.com/apache/tvm-rfcs/commit/4203bd2da4ffc98eb70731a05fcadc478679a461))
 * [[USMP] Adding U4 usecase (#65)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0009_Unified_Static_Memory_Planning.md) ([`b9e246f`](https://github.com/apache/tvm-rfcs/commit/b9e246f6d1715176f5de10fe1e7e382b88bacabe))
 * [Collage RFC (#62)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0062-collage.md) ([`23250f5`](https://github.com/apache/tvm-rfcs/commit/23250f59cfc89673b7efe1d8f13192ed8381824d))
 * [Replace codeowners with more relevant automation (#58)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0058-replace-codeowners.md) ([`540c1f8`](https://github.com/apache/tvm-rfcs/commit/540c1f80631b5d9ee2ae9ff827edc73240fe1b09))
 * [[RFC][TIR] Layout transformations on buffer access (#39)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0039-buffer-physical-layout.md) ([`b675ef8`](https://github.com/apache/tvm-rfcs/commit/b675ef8e74351f298b8f3bc4ae944eaf3cbbe430))
 * [Module Based Model Runtime for AOT (#46)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0046-module-based-model-runtime-for-aot.md) ([`d9dd6eb`](https://github.com/apache/tvm-rfcs/commit/d9dd6eb5e522ff169fe3bf4f5b9c5c3e84d95145))
 * [@slow test RFC (#55)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0055-slow-tests.md) ([`9b6203a`](https://github.com/apache/tvm-rfcs/commit/9b6203a743693ea65eef66137d48abfc75d79d77))
 * [[RFC][Roadmap] TVM Continuous Integration & Testing Roadmap (#54)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0054-ci-testing-roadmap.md) ([`41e5ba0`](https://github.com/apache/tvm-rfcs/commit/41e5ba078b830299692c844e5ab3e5193d3d6129))
 * [Bring `PackedFunc` into TVM Object System (#51)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0051-PackedFunc-as-Object.md) ([`2e0de6c`](https://github.com/apache/tvm-rfcs/commit/2e0de6cbdae162c17f0842c32a4eb797cbd2c1ea))
 * [[RFC][OpenCLML] OpenCLML integration as BYOC (#52)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0052-OpenCLML-integratio-as-BYOC.md) ([`f5ef65f`](https://github.com/apache/tvm-rfcs/commit/f5ef65fd0f04178af266ed109206ba3f011d8eaa))
 * [Introduce the Arm(R) Ethos(TM)-U Cascading Scheduler (#37)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0037-arm-ethosu-cascading-scheduler.md) ([`f9fa824`](https://github.com/apache/tvm-rfcs/commit/f9fa8246ab9c95afa7025c2bd045b4e715c75103))
 * [[RFC][Roadmap] microTVM roadmap (#53)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0053-microtvm-roadmap.md) ([`1b14456`](https://github.com/apache/tvm-rfcs/commit/1b1445647039f0241f9ff0268de538329b48b3d6))
 * [Add Managed Jenkins Infrastructure for TVM RFC (#49)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0049-managed-jenkins-infrastructure-for-tvm.md) ([`a3a7d2c`](https://github.com/apache/tvm-rfcs/commit/a3a7d2c083e2384cfad158300ba2a22551ed4433))
 * [TVM Roadmap RFC (#50)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0050-roadmaps.md) ([`263335f`](https://github.com/apache/tvm-rfcs/commit/263335f905afae55e161a23e77b1c19da274e795))
 * [[RFC] Integrate LIBXSMM with TVM. (#47)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0046-Intel-LIBXSMM-integration.md) ([`1a3d4f1`](https://github.com/apache/tvm-rfcs/commit/1a3d4f13bf9c2ffb2baf420daeae460901fe79c7))
 * [[RELAY][AST] Add virtual device as a first class field to Relay expressions (#45)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0045-first-class-virtual-device.md) ([`67c39d2`](https://github.com/apache/tvm-rfcs/commit/67c39d2a0766165e0c090286130109173a86dbe2))


## What's Changed

Note that this list is not comprehensive of all PRs and discussions since v0.8. Please visit the full listing of commits for a complete view: https://github.com/apache/tvm/compare/v0.8.0...v0.9.0.rc0.


### AOT
 * #11208 - Calculate used memory at the callsite of primitive functions
 * #11365 - Fix function number datatype from char to uint16_t
 * #11091 - Enable A-Normal Form in the AOT executor
 * #10753 - Support LLVM backend with C++ runtime
 * #10518 - Use python temporary directory for AOT tests
 * #10337 - BugFix of workspace calculation
 * #10282 - [runtime] Add Metadata classes for AOTExecutor
 * #9501 - [3/3][DeviceAPI] Wire up cpacked Device API context
 * #9500 - [2/3][DeviceAPI] Add Hooks for Activate/Deactivate/Open/Close
 * #9395 - [1/3][DeviceAPI] Connecting devices structure to relevant operators

### BYOC
 * #11474 - Two helper passes for external codegen using RelayToTIR custom pass machinery
 * #11144 - Remove support for run-time linked-params from codegen
 * #10590 - Add order to functions in C Codegen
 * #11638 - [DNNL][CBLAS]Unifles all MKLDNN/DNNL  to DNNL
 * #11619 - RelayToTIR custom codegen passes can still depend on dynamic shape functions
 * DNNL - #11902, #11642, #11513, #11571, #11560, #11345, #11111, #10837, #10421, #9995, #9797
 * TensorRT - #11923, #11203, #10759, #10772, #10388
 * CMSIS-NN - #11732, #11625, #10939, #11013, #10817, #10563, #10224, #10148, #10100, #9338, #9531, #9409, #9331
 * OpenCLML - #10243
 * CUTLASS - #11631, #10185, #10177, #10110, #10036, #9899, #9820, #9800, #9795, #9746, #9737, #9698, #9595, #9571
 * CUDNN - #10997, #9986, #9948
 * ACL - #10801
 * PTX - #10855, #10339, #9909
 * CUBLAS - #10826, #10820

### CI
 * #11313 - Refactor of tvm.testing.requires_* annotations
 * #11666 - Enable pylint for tests/python/ci
 * #11657 - Apply linting rules to AOT tests
 * #11380 - Restructure Jenkinsfile
 * Automation - #11813, #11775, #11480, #11437, #10833, #10056, #9973, #9934
 * User experience improvements - #11470, #11329, #11553, #11497, #11051, #10933, #10960, #10525, #10425, #10322, #10121, #9971, #9554, #9752, #9556
 * Reduce CI runtime - #11402, #11349, #11258, #11132, #10946, #10743, #10359
 * Code cleanups - #10968, #10740

### Frontends
 * PaddlePaddle - #11537, #9724, #9564
 * TFLite - #10915, #10566
 * Oneflow - #11321, #11036, #8790
 * PyTorch - #11190, #10504, #10184, #10091
 * ONNX - #10949, #9438, #9186, #9493, #9475
 * Keras - #7006

### Hexagon
 * #11549 - Initial clip operator for Hexagon
 * #11834 - Add op resize2d for hexagon
 * #11559 - Softmax slice op initial version
 * #11529 - Slice ops added - add, subtract, multiply
 * #11720 - [testing] add max_pool2d benchmark
 * #11417 - Implement avg_pool2d slice op
 * #11653 - Add HexagonThreadManager
 * #11547 - Run single RPC server on Android in each testing session
 * #11490 - [testing] add TVMScript elemwise-add
 * #11400 - [testing] refactor benchmark-table code
 * #11277 - moves conftest.py to tvm.contrib.hexagon so outside repos can access the testing fixtures
 * #11319 - Add unit tests for Hexagon Device API
 * #11279 - Add USMP tests
 * #11283 - Update Readme
 * #11239 - capture gtest output and return over FFI
 * #11175 - Add schedule and test for conv2d_transpose_nchw
 * #11018 - [Runtime] Add QuRT thread pool backend
 * #11145 - Add support for on-device unit testing using gtest
 * #11138 - Add test for depthwise conv2d schedule
 * #11016 - Add test for registered schedules
 * #11104 - Add mobilenet test
 * #11090 - Delete offload runtime, move files to right places
 * #11065 - AoT with LLVM Codegen on Hexagon
 * #11025 - Deprecate USE_HEXAGON_DEVICE, introduce USE_HEXAGON
 * #10604 - HVX scheduling and bench-marking of TE element-wise add
 * #10905 - [LLVM] Enable/test tensorized Hexagon DMA on 2d transformed layout
 * #10907 - Move aot/graph_executor interactions into launcher
 * #10919 - Register basic strategies and schedules for common operators
 * #10904 - Add unit tests executing 2-d VTCM usage
 * #10910 - Refactor to keep HexagonBuffer private to the device api
 * #10908 - [LLVM][CodeGen] Make CodeGenHexagon a subclass of CodeGenCPU
 * #10878 - Generalized HexagonBuffer::CopyTo/CopyFrom
 * #10846 - Support both 1-d and 2-d VTCM allocations
 * #10581 - Improved ergonomics of HexagonLauncher in unit tests.
 * #10616 - Refactor tvm.contrib.hexagon, NFC
 * #10612 - Deprecate SDK 3.x, rewrite HexagonSDK.cmake
 * #10586 - Codegen for 2d Load/Store
 * #10558 - Generalize builtin for Nd memory alloc with storage scope and add lowering for VTCM / Hexagon
 * #10543 - [Runtime][PipelineExecutor] Add the pipeline internal forwarding logic.
 * #10507 - Add doc on TVM - Hexagon RPC flow
 * #10520 - Resolve breakage in test_hexagon/test_cache_read_write
 * #10311 - [runtime]AOTExecutor implementation for C Codegen
 * #10454 - Allow execution on target or simulator from HexagonLauncher
 * #10365 - Lower cache_read and cache_write to Hexagon DMA via tensorize
 * #10361 - RPC server/client for simulator
 * #10302 - [CI]Add Hexagon Tests to pipeline
 * #10263 - [Docker]Add docker file and scripts
 * #10227 - Refactor Hexagon.cmake
 * #10217 - Adding support for Hexagon User DMA Engine
 * #10068 - Update hexagon API build instruction and cleanup hexagon_proxy_rpc
 * #9970 - Do not auto-build apps when building TVM
 * #9736 - Add unit tests for HexagonBuffer
 * #9525 - Add Hexagon VTCM and discontiguous allocation support
 * #9631 - Add RPC Mechanism for Hexagon
 * #9473 - cleanup Hexagon conv2d tests

### MetaSchedule
 * #11884 - Postproc: Rewrite-Layout
 * #11848 - [OpStrategy] Support MetaSchedule Layout
 * #11845 - [Relay][Pass] Meta-Schedule-Layout-Rewrite
 * #11758 - [Runtime] Enhance Runner RandomFill
 * #11683 - Distributed Measurement
 * #11751 - [Minor] Organize Testing Scripts
 * #11735 - Modify Profiler Timers
 * #11727 - Developer Ergonomics Enhancement II
 * #11692 - Apply-History-Best Task Filtering
 * #11486 - Add Profiler Support For Tuning Efficiency Optimization
 * #11680 - JSONDatabase Utilities
 * #11641 - Generate MetaSchedule Dataset
 * #11622 - Developer Ergonomics Enhancement
 * #11604 - Resolve dependencies between header files
 * #11587 - Add Testing Script with ONNX Support
 * #11590 - Evo Independence from TaskScheduler
 * #11534 - No explicit unrolling for spatial PrimFunc
 * #11512 - Enable Task Filtering
 * #11177 - AutoBind rule and MutateThreadBinding
 * #11157 - Logging Interface Unification
 * #11088 - Auto tensorization for CPU / GPU dot product
 * #10986 - [Refactor] Introduce TuneConfig
 * #11020 - [Metaschedule, Refactor] Move MultiLevelTilingNode decl to a header
 * #10927 - [Refactor] Clarify Integration Logic
 * #10876 - Add utility API to ease using manual schedules
 * #10885 - [BugFix] Fix skipped tests
 * #10366 - Add Gradient Based Task Scheduler
 * #10823 - Fine-Grained Rewrite Unbound Block
 * #10793 - Add demonstration of selectively tuning relay ops with TIR schedules
 * #10811 - Support grouping in the cost model
 * #10810 - Extract task weights during task extraction
 * #10782 - [TIR]Estimate TIR FLOPs
 * #10776 - Misc updates for tuning end-to-end workloads
 * #10689 - Upstream the leftover changes
 * #10648 - [Meta Schedule] Refactor meta schedule testing utils
 * #10578 - New relay backend for meta schedule task extraction
 * #10534 - Bug Fix for Relay Integration
 * #10501 - Update scripts for subgraph tuning
 * #10497 - Refactor testing workloads
 * #10461 - Enable AutoTVM-style template-based search space
 * #10368 - Fix Cyclic Dependency in PyClass Family
 * #10403 - Arithmetic analysis
 * #10367 - Update Tuning Interfaces.
 * #10079 - [M4a] User-API: Tune-TE/TIR/Relay
 * #10081 - [M4a] Rewrite-Cooperative-Fetch
 * #10055 - [M4b] Testcases for TensorRT builder/runner
 * #10092 - [M4a] Mutator: Mutate-Tile-Size
 * #10096 - [M4a] Mutator: Mutate Parallel
 * #10071 - [M4a] PostProcessor: Rewrite-Parallel-Vectorize-Unroll
 * #10043 - [M4a] Schedule Rule: Multi-Level-Tiling
 * #10045 - Mutator: Mutate-Unroll
 * #10033 - [M4a] Schedule Rule: Parallelize-Vectorize-Unroll
 * #10027 - [M4a] PostProcessor: Rewrite-Unbound-Block
 * #10028 - Mutator: Mutate-Compute-Location
 * #9997 - [M4a] PostProcessor: Disallow-Dynamic-Loop
 * #9994 - [M4a] Schedule Rule: Cross-Thread-Reduction
 * #10013 - [M4a] PostProcessor: Rewrite Reduction Block
 * #9975 - [M4a] Schedule Rule: Add-RFactor
 * #9945 - [M4a] PostProcessor: Verify-GPU-Code
 * #9940 - [M4a] Schedule Rule: Random-Compute-Location
 * #9943 - [M4a] Schedule Rule: Auto-Inline
 * #9860 - [M3c] Add Per-Store-Feature
 * #9859 - [M3c] XGB-based Cost Model
 * #9836 - [M4a] Add EvolutionarySearch Search Strategy
 * #9799 - [M4a] Add ReplayFunc Search Strategy
 * #9789 - [M3c] Update TuneContext, TaskScheduler & Search Strategy Design
 * #9780 - [M3c] Add More Measure Callbacks
 * #9761 - [M4a] Add ScheduleRule class & PostOrderApply space generator
 * #9760 - [M3c] Random Feature Extractor

### MicroTVM
 * #11741 - Refactor RVM scripts and fix DNS network issue
 * #11472 - [ARM]Add tests for arm schedules
 * #11634 - Update pyproject to python3.7
 * Zephyr support - #11650
 * RPC - #11227, #10967

### Relay
 * #11825 - [realy][pass]add split infer shape with convert op layout pass
 * #11674 - Finish implementations of WithFields
 * #11481 - IndexedGraph improvements in preparation for Collage
 * #11432 - Plumb external codegen target via Target.current()
 * #11494 - [Pass] Add MaxPool, AvgPool to FoldExplicitPadding
 * #11183 - Add unidirectional sequence lstm
 * #11442 - Add 'static_library' runtime::Module
 * #11413 - [Topi]Support for FP16 ERF on CPU.
 * #11382 - Finish support for list-of-targets
 * #11386 - [Tests] Replace the Relay interpreter with the VM in the op tests
 * #11224 - Support i16, f16 scalars in Relay text
 * #11337 - Fix eltwise alter op layout for broadcast axis
 * #11199 - Flexible shape dispatch transformation
 * #11173 - Support 'external codegen targets'.
 * #10996 - Add FlattenAtrousConv transformation
 * #10871 - [CUDNN] Add cuDNN as a Relay partitioning target (BYOC)
 * #10787 - [Pass][Bugfix] Disable re-use of non-flat buffers in StorageRewrite.
 * #10378 - [FQ2I] Add leaky relu to FQ21
 * #10400 - RelayViz graphviz renderer
 * #10352 - [VIRTUALDEVICE] Change syntax for device planning and store parameter virtual devices in virtual_device_ field
 * #10310 - [ARM_CPU] Conv2d int8 intrinsic for cortex-A72
 * #10085 - RelayViz interface and terminal ast-dump
 * #10239 - Add a conversion of individual operations in FQ2I pass.
 * #10236 - [Refactor] Clean up type relations that are declared as template for no reason
 * #10156 - Fix broadcast InferCorrectLayout
 * #10026 - [VM] Relay VM memory liveness/lifetime analysis
 * #10089 - [Pass] Add a relay pass to extract fake quantized ops
 * #9690 - Change function constructors to WithFields
 * #10069 - [DefuseOps pass] bug fix: To support function body types other…
 * #9954 - Add `conv2d_backward_weight` op (without topi)
 * #9838 - [FoldScaleAxis] Support dense and bias_add op in fold scale axis
 * #9816 - Add sliding_window operator
 * #9874 - Add a JSON converter for 0.7 -> 0.8 and 0.8 -> 0.9
 * #9735 - [AMP][Pass][Typing] Add faster type inference
 * #9723 - [Frontend] Add Span filling for frontends to Relay
 * #9749 - Fix invalid shape function for "copy" operator
 * #9759 - s/SEScope/VirtualDevice/g
 * #9734 - Support large constants saved/loaded outside of VM executable
 * #9613 - Re-run PlanDevices after LowerTE to flow new memory scope constraints.
 * #9693 - PlanDevices supports 'free' on_device annotations
 * #9641 - [AST] Add virtual_device as a first class field in Relay
 * #9483 - Switch the VM to use the LowerTE pass instead of TECompiler::{Lower,LowerShapeFunc}.
 * #9569 - WithFields method for Call, Function, Var, TupleGetItem, If, Let, RefCreate, RefRead, RefWrite, Match, and Clause
 * #9533 - WithFields for Tuples
 * #9550 - Prepare for switching VM to LowerTEPass.
 * #9542 - Prepare DeadCodeElimination for running post LowerTEPass/ManifestAlloc.
 * #9352 - [TVMC]Introduce executor and runtime parameters
 * #9457 - Add the Arm(R) Ethos(TM)-U NPU identity operator
 * #9326 - Switch PlanDevices pass to be w.r.t. SEScopes instead of DLDeviceTypes.
 * QNN - #11228, #10718, #10086, #10053, #9637, #9982

### Runtime
 * #11334 - [PipelineExecutor] Add graph manually splitting logic into the unit test.
 * #11133 - [PipelineExecutor] Refactor PipelineExecutor.py and Add cross compile support for pipeline executor.
 * #11172 - Move WrapTimeEvaluator from RPC to profiling, NFC
 * #10990 - [PipelineExecutor]Add forwarding queue logic for set input.
 * #10953 - [Vulkan] Add RGP support to TVM for vulkan device
 * #10723 - [PipelineExecutor] Getting the asynchronous output
 * #10283 - AOTExecutor implementation and c target code-generator
 * #9802 - [ThreadPool]Refactor affinity function and support CPU affinity list setting.
 * #10234 - [Pipeline Executor] multiple threads management and the data forwarding notification mechanism.
 * #10326 - Improved log information with function signature
 * #10032 - [PackedFunc] Bring `PackedFunc` into TVM Object System
 * #10082 - [PipelineExecutor] Pipeline Executor Sequential execution
 * #10010 - [PipelineExecutor] Add Pipeline Executor Interface
 * #9846 - [Pipeline executor] Global parameters group name and runtime modules parameters map.
 * #9889 - [GraphExecutor] Add API `get_input_info` to graph_executor
 * #9751 - [Pipeline Executor] Add the map logic of global input and subgraph input.

### TE
 * #11589 - Support schedulable TIR compute definitions in TOPI
 * #11341 - Optimized version of concatenation layer
 * #10561 - [TECompiler] Decouple TE compute and schedule lowering in ScheduleBuilder

### TIR
 * #11592 - HoistExpression, generalization of HoistIfThenElse
 * #11870 - [Pass] Remove-Weight-Layout-Rewrite-Block
 * #11740 - [TIR, analysis] Add GetAutoTensorizeMappingInfo to generate transforms for auto tensorization
 * #11585 - Add preserve-unit-iters
 * #11677 - Register CUDA WMMA tensor intrinsics
 * #11658 - [TIR, CUDA] Add pass to replace global to shared memory copy with cp.async
 * #11624 - [Schedule] Allow named block and buffer arguments in Schedule
 * #11628 - [PASS] Refactor a couple of TIR passes - BindTarget, AnnotateEntryFunc, Filter, LowerInitBlock
 * #11574 - CSE pass : Restrict the equivalence to be decided by a normal form - avoids comparison of terms
 * #11575 - Schedule Primitive: Add-Unit-Loop
 * #11515 - Add schedule primitive ReIndex
 * #11524 - [Arith] Additional Simplifications Inside Conditionals
 * #11485 - Add schedule primitive TransformBlockLayout
 * #11495 - [Software pipeline] Fix hardcoded index in `access_ptr` rewriting, add a GPU test with depth 4
 * #11269 - [Schedule] Transform layout quality of life
 * #11355 - Support tensorization using ldmatrix + MMA
 * #11289 - [Schedule] Allowed typing.Tuple in tir.schedule._type_checker
 * #11317 - Support affine expressions as indices in reverse compute inline
 * #11235 - [Arith] Implemented padded inverses in IndexMap
 * #11238 - [ROOFLINE] Calculate roofline from existing TIR PrimFunc
 * #11225 - Add schedule primitive SetAxisSeparator
 * #11110 - Get read/write access precisely for opaque access.
 * #11106 - Enhance software pipeline validation and fix predicate of epilogue
 * #10843 - StmtFunctor RenewDefs
 * #11075 - Add function to tile a block according to a given tensor intrinsic
 * #11050 - Utility function to decide loop mapping for auto tensorization
 * #11009 - [ROCM] DP4A intrinsic support for TE/TIR
 * #10925 - VNNI and ARM dot product intrinsic for tensorization
 * #10887 - [Schedule] Relax reorder primitive's affine binding check
 * #10732 - [Analysis] Add SuggestIndexMap for layout rewriting
 * #10538 - [Schedule] Transform layout
 * #10638 - Change the behavior of read/write region analysis for reduction blocks.
 * #10705 - Use local complete block and local reduction block to identify compact dataflow
 * #10671 - Tuple Reduction Support in CreatePrimFunc
 * #9727 - [TE]Implement layout transformations, non-flat memory buffers
 * #10405 - [TensorIR] Update VerifyGPU
 * #10401 - [TensorIR] Renormalize split pattern
 * #10112 - [TIR, Relay] improve bfloat16 support
 * #8509 - Tir constants integration into compilation pipeline
 * #9996 - add support for multi-blocking layout and their transformation
 * #10066 - Add software pipelining
 * #10207 - Support sub warp reduction for CUDA target.
 * #9482 - Implementation of Common Subexpression Elimination for TIR
 * #9527 - Allow compute_at create block predicate for non-trivial bounds and support floordiv pattern
 * #10158 - [Schedule] Update compact_dataflow constraint
 * #9871 - [Schedule] Blockize and Tensorize
 * #10016 - [BugFix]Fix cross-thread reduction when single reduction loop with predicate
 * #9880 - Encode conditional accesses info into block read/write regions
 * #9699 - Affine utility support iter lowerbound and diagnostics
 * #9742 - [Schedule] Add Annotate/Unannotate primitive
 * #9738 - [TensorIR] Primitive "SetScope"
 * #9743 - [Schedule] Analysis functions to check if compute_inline and com…
 * #9689 - Allow memory (aka storage) scopes to be retrieved/applied to PrimFuncs
 * #9559 - [TensorIR][UX] Type annotation-based runtime type checking
 * #9444 - Add a 'rolling_buffer' scheduling primitive
 * #9360 - [TensorIR] Cross-Thread Reduction

### TOPI
 * #11531 - TE implementation of LSTM using scan
 * #11161 - Add Adreno GPU target and topi supporting textures with dynamically allocated textures
 * #10332 - VNNI support for batch matmul
 * #9873 - Add support for groupped conv3d
 * #10230 - VNNI support for int8 dense
 * #10098 - [Op]5 ops can accept unsigned integers as indices
 * #9832 - Support grouped conv1d
 * #9694 - Add generic batch norm
 * #9233 - Cortex-M DSP support

### TVMScript
 * #11308 - Represent ramp as index slice
 * #10099 - Support T.buffer_decl using data pointer from Let/Allocate
 * #9680 - Improve printer for TIR syntax sugar
 * #9492 - Add syntax sugar for T.handle and T.match_buffer
 * #9620 - Add for loop syntax sugar
 * #9543 - Misc error message improvements
 * #9505 - [Fix] Add type hints for more uncovered cases

### USMP
 * #11015 - U3 use case
 * #10189 - Adding support for U1 usecase for constant pools
 * #10785 - Adding support for U4 usecase
 * #10193 - adding support for U2 and U3 usecases
 * #10005 - Add performance characteristics to PoolInfo
 * #9565 - [TIR]Integrating USMP to AoT Executor
 * #9704 - Hill Climb allocator
 * #9418 - [TIR]adding the pass to convert to pool offsets
 * #9649 - [TIR]Augmenting the algo interface with memory pressure
 * #9214 - [TIR]Greedy memory planning algorithm
 * #8468 - [TIR]Added buffer info extraction pass

### microNPU
 * #11468 - Optimize separate padding operation for conv2d
 * #11453 - Add transform matrices and part matcher to identity op
 * #11410 - add E2E tests with cascader wo striping
 * #11288 - Expose compute cycle annotations to TIR lowering
 * #10959 - Add a pass to reorder copy and compute nodes
 * #10509 - Add various options to the cascader
 * #11263 - Adding a option to enable striping
 * #10251 - Add support for conv2d running on two cores on U65
 * #10862 - Integrate the cascader
 * #10344 - Integrate rolling buffers in Arm(R) Ethos(TM)-U
 * #10824 - Some housekeeping in the test_ethosu folder
 * #10763 - Tweak a layout transform matrix
 * #10725 - Add a pass to move allocate nodes to the outer scope
 * #10695 - Determine block configs using the cascader
 * #10599 - Refactor Relay to TIR hook
 * #10508 - Improve cascader memory transfer estimates
 * #10345 - Add support for TFLite FULLY_CONNECTED
 * #10254 - Introduce a pass to remove redundant identity operations
 * #10062 - [5] Convert Proposals to te.Schedules
 * #9959 - [4] Add the cascader Proposal generator
 * #10022 - enable USMP
 * #10127 - Add support for LeakyReLU
 * #10004 - Add FreeRTOS variant of NPU demo
 * #10060 - Refactor type inference data type checks
 * #9960 - Add support for pack and unpack
 * #10143 - Fix layout assignment in layout optimizer pass
 * #9890 - [3] Plan generation for the cascader
 * #9855 - Add support for transpose convolution
 * #9841 - Add support for nearest neighbor and bilinear upsampling
 * #9951 - Removing constant args from PrimFunc
 * #9929 - Refactor base address determination to codegen
 * #9910 - Add support for requantize
 * #9831 - Move optimization passes to be a module pass and ensure they are running
 * #9785 - [2d] Add more Part matchers to cascader
 * #9778 - [2c] Add performance modelling to cascader
 * #9471 - [2b] Create CascaderGraphs from TE graphs
 * #9469 - [2a] Add CascaderGraph for cascading analysis
 * #9621 - Add support for SPLIT and SPLIT_V
 * #9508 - Update Conv2D Tests to Use TF API to Gen Test Cases
 * #9627 - Add support for SIGMOID
 * #9589 - Add support for TFLite concatenate
 * #9623 - Refactor codegen tests
 * #9561 - Add NHWC -> NHCWB16 layout transformation pass
 * #9576 - Mean legalization support
 * #9597 - Move the compilation to use Target Hooks.
 * #9458 - [1] Add affine analysis structures for the cascader
 * #9547 - Add the infrastructure for lookup table and TANH
 * #9521 - Support binary elementwise with non-4D inputs
 * #9560 - Fix incorrectly calculated stride when converting NHWC to NHCWB16
 * #9530 - Add unary elementwise operator infrastructure with ABS
 * #9514 - Adding rounding mode attribute to operators
 * #9515 - Allow constants to be given as input to an operator

### microTVM
 * #11250 - [ARM] Add Relay tests for conv2d registered schedules
 * #11232 - [rpc] Implemented rpc logging
 * #11044 - Add support for host-driven AoT Executor
 * #11043 - Better version handling for Arduino
 * #10555 - Enable micro tvmc tutorial testing in CI
 * #10194 - [RVM] Add scripts for automated build and testing
 * #10144 - TVMCon 2021 Zephyr Demo with CMSIS-NN
 * #10024 - [tvmc] Add TVMC Micro tutorial for Zephyr
 * #9684 - Fix zephye/test_zephyr_armv7m test
 * #9584 - [TVMC] Add TVMC test for Arduino and Zephyr
 * #9526 - Add minimal forwarding RPC server for host driven python execution on Hexagon
 * Zephyr support - #11362, #10138

### Misc
 * #11465 - Add cooldown interval logic for the profiling functional
 * #11888 - [LLVM] Include LLVM headers in files that use them, not in llvm_common.h
 * #11646 - [Arith] Simplification of ceil, log2, and left_shift
 * #11464 - [MLF] Add support for multiple modules in Model Library Format
 * #11632 - [AutoTVM][Autoscheduler] Default build funcs inherit PassContext
 * #11543 - [OpenCL] Implement conv2d_winograd algorithm for Adreno
 * #11287 - [Arith] Merge surjective/non-surjective iter mapping detections
 * #11393 - Add utility to replace direct call to pytest.main
 * #11252 - [ROOFLINE] Roofline analysis over RPC
 * #11000 - [Graph Debugger] Expose way to benchmark individual nodes.
 * #10794 - bump PyTorch version to 1.11
 * #10821 - [REFACTOR] Remove legacy nnvm folder
 * #10798 - [Arith] Remove diagnostic ctx argument from DetectIterMap
 * #10567 - [Refactor] Reduced repetition in CodeGenLLVM's buffer access
 * #10455 - [AUTO_SCHEDULER] Add feature extraction directly from PrimFunc
 * #7401 - RFC: initial stab at TorchScript fallback
 * #10391 - [vulkan] Add integer dot product (4xint8, 4xuint8) tensorization for the vulkan SPIR-V target.
 * #10293 - [VirtualMachine] new method allowing to set one input tensor by its index or name
 * #10191 - Generate correct output tensor names in C Interface API
 * #9276 - Parameterize test_link_params
 * #9808 - [Rust] Update Rust bindings
 * #9553 - [PROFILING] Add ability to profile a single function_profiling
 * #9611 - [CMAKE] Automatically detect newly added source files
 * #9544 - [Target] enable -arch=sm_xx for assigning cuda target arch and deprecate autotvm.measure.set_cuda_target_arch api
 * Profiler - #11530, #11066
 * Docs - #10921, #11403, #10774, #10912, #9633, #9906, #9534, #9307, #9654, #9580
 * Android - #11241
 * ETHOSN - #11261, #10486, #10018, #9596
 * TVMC - #11012, #10962, #10722, #9817, #9529, #9229




## v0.10.0 (2022-10-17)

# Introduction

The TVM community has worked since the v0.9 release to deliver the following new exciting improvments!
* Metaschedule
    * Software pipelining and padding for irregular shapes for auto tensorization
    * Stabilized and polished user-interfaces (e.g. `database` changes, `tune_relay`)
    * A new MLP-based cost model
* TIR
    * New schedule primitive for `PadEinsum`  
    * A new TIR node: `DeclBuffer`
    * INT8 Intrinsics for TensorCores for CUDA!
* microTVM
    * Improved schedule primitives for ARM v8-m ISA  

And many other general improvements to code quality, TVMScript, and more! Please visit the full listing of commits for a complete view: https://github.com/apache/tvm/compare/v0.9.0...v0.10.0rc0.

## RFCs

These RFCs have been merged in [apache/tvm-rfcs](https://github.com/apache/tvm-rfcs) since the last release.
 
 * [Issue Triage Workflow RFC (#93)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0093_Issue_Triage.md) ([`3345cc1`](https://github.com/apache/tvm-rfcs/commit/3345cc1fe7db7c017051ee7e4b309c6182e81aef))
 * [[RFC] Add Commit Message Guideline (#88)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0088-commit-message-guideline.md) ([`e8a2d8b`](https://github.com/apache/tvm-rfcs/commit/e8a2d8bad2680e359a3a7bbd061fde205872004b))
 * [Add Target Features RFC (#78)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0078-target-features.md) ([`1ab898d`](https://github.com/apache/tvm-rfcs/commit/1ab898dfd46ee9ab4af228532b4c791dd06d135d))
 * [[RFC] TVMScript Metaprogramming (#79)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0079-tvmscript-metaprogramming.md) ([`ffbf686`](https://github.com/apache/tvm-rfcs/commit/ffbf68643a20a9b3daeb2adc87933d976e5a5513))
 * [Add Target Pre-processing RFC (#71)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0071-target-json-parser.md) ([`78423c5`](https://github.com/apache/tvm-rfcs/commit/78423c550413a242a457d054eb828403546afb65))

 * [[RFC] Name mangling in IRModules (#84)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0077_name_mangling_ir_modules.md) ([`831d702`](https://github.com/apache/tvm-rfcs/commit/831d7025b3b25773019cb8edf1bb633dab4df54b))
 * [Asynchronous stage in software pipeline (#80)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0077-async-pipeline.md) ([`aecb219`](https://github.com/apache/tvm-rfcs/commit/aecb21964f1797d25963657ddbfc0df1e269ddae))
 * [[RFC] Buffer Layout Padding (#77)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0077-layout-transform-padding.md) ([`ca695fe`](https://github.com/apache/tvm-rfcs/commit/ca695fe9b672c75f72dc5f05c3817eb547cf890e))
 * [[RFC] Create LLVM scope class for use with LLVM libraries (#83)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0080-llvm-target.md) ([`22d1d11`](https://github.com/apache/tvm-rfcs/commit/22d1d11ec0352131fccab58ee2ee5a912ec88dfc))

## What's Changed

Please visit the full listing of commits for a complete view: https://github.com/apache/tvm/compare/v0.9.0...v0.10.0rc0. 

Note that this list is not comprehensive of all PRs and discussions since v0.9. A non-truncated summary can be found here: https://github.com/apache/tvm/issues/12979

### TIR
 * #12720 - [TIR] Implement API for padded layout transformations
 * #12797 - [TIR] Construct the inverse in SuggestIndexMap 
 * #12827 - [TIR] Support pattern matching argmax/argmin generated by TOPI
 * #12750 - [TIR, Schedule] Add schedule primitive PadEinsum 
 * #11639 - [TIR][Meta-Schedule] Tuple-reduction scheduling support 
 * #12515 - [TIR][Arith] Add more strict checking in imm construction and folding. 
 * #12717 - [TIR, Schedule] Check consumer in-bound and covered in reverse_compute_inline 
 * #12652 - [TIR] Handle axis_separators during FlattenBuffer 
 * #12623 - [TIR] Expose MMA-related PTX builtins 
 * #12607 - [TIR][Schedule] enhance compute_at and reverse_compute_at primitive to choose possible position
...

## v0.11.0 (2023-02-25)

# Introduction

The TVM community has worked since the v0.10.0 release to deliver the following new exciting improvements!

* Metaschedule
    * Tuning API improvements and anchor-block tuning

* TVMSCript metaprogramming
    * Lots of progress wiht TVMScript, with the introduction of a core parser, AST, Evaluator, Source and diagnostics

And many other general improvements to microTVM, code quality, CI, frontends, and more! Please visit the full listing of commits for a complete view: https://github.com/apache/tvm/compare/v0.10.0...v0.11.0.

## RFCs

These RFCs have been merged in [apache/tvm-rfcs](https://github.com/apache/tvm-rfcs) since the last release.

  * [CodeGenAArch64 backend with Scalable Vector Extension (SVE) #94](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0094-aarch64-backend-with-sve.md) https://github.com/apache/tvm-rfcs/commit/04b9909d6f8b63524091f12ff5eb964ad490c7b8


## What's Changed

Note that this list is not comprehensive of all PRs and discussions since v0.10. Please visit the full listing of commits for a complete view: https://github.com/apache/tvm/compare/v0.10.0...v0.11.0.

### Adreno
  * [Adreno] Add global pooling schedule (#13573)
  * [Adreno] Add documentation for Adreno deployment (#13393)
  * [Adreno] Fix mem_scope annotations for prim funcs having several heads (#13153)
  * [Adreno] Adapt reduction schedule for adreno (#13100)
  * [Adreno] Fix winograd accuracy (#13117)
  * [Adreno][Textures] Fix static memory planner  (#13253)
  * [DOCKER][Adreno]Docker infra for Adreno target with CLML support (#12833)

### AoT
  * [AOT] Add CreateExecutorMetadata analysis pass (#13250)
  * [AOT] Add CreateFunctionMetadata analysis pass (#13095)
  * [AOT] Sanitize input/output name in runtime (#13046)

### Arith
  * [Arith] Add internal NarrowPredicateExpression utility (#13041)
  * [Arith] Optional rewriting and simplification into AND of ORs (#12972)

### arm
  * [bfloat16] Fixed dtype conversion in the arm_cpu injective schedule (#13417)

### AutoTVM
  * [AutoTVM] Introducing multi_filter into ConfigSpace autotvm (#12545)

### Build
  * [BUILD] Re-enable ccache by default (#12839)

### CI
  * [ci] Fix docs deploy (#13570)
  * [ci] Split Jenkinsfile into platform-specific jobs (#13300)
  * [ci] Dis-allow any non-S3 URLs in CI (#13283)
  * [ci] Split out C++ unittests (#13335)
  * [CI] Separate the ci scripts into Github and Jenkins scripts (#13368)
  * [ci] Assert some tests are not skipped in the CI (#12915)
  * [ci] Ignore JUnit upload failures (#13142)
  * [ci] Lint for trailing newlines and spaces  (#13058)
  * [ci] Template build steps (#12983)
  * [ci][docker] Allow usage of ECR images in PRs (#13590)
  * [ci][docker] Read docker image tags during CI runs (#13572)
  * [ci][wasm] Add package-lock.json to git (#13505)

### CL
  * [ACL] Enable int8 data type in pooling operators (#13488)

### CMSIS-NN
  * [CMSIS-NN] Support for int16 conv2d (#12950)
  * [CMSIS-NN] Support for int16 in fully connected layer (#13484)

### DNNL
  * [AMP] refine AMP and the corresponding tests for bfloat16 (#12787)

### Docker
  * [Docker]Refactor timezone script and NRF installation (#13342)

### Docs
  * [docs] Fix empty code blocks in tutorials (#13188)

### Ethos-N
  * [ETHOSN] Consolidate target string usage (#13159)
  * [ETHOSN] Throw error message when inference fails (#13022)
  * [ETHOSN] Inline non-compute-intensive partitions (#13092)
  * [ETHOSN] Transpose fully connected weights (#12970)
  * [ETHOSN] Support conversion of add/mul to requantize where possible (#12887)

### Frontend
  * [TFLite] Enable int64 biases for int16 quantized operators (#12042)

### Hexagon
  * [Hexagon] Add HVX quant conv2d implementation (#13256)
  * [Hexagon] Add test to show scheduling of resnet50 with async dma pipe… (#13352)
  * [Hexagon] Enable Hexagon User DMA bypass mode (#13381)
  * [Hexagon] Lint tests part 2 (#13271)
  * [Hexagon] Add pylint on tests (#13233)
  * [Hexagon] Add E2E test demonstrating how to apply blocked layout schedule to conv2d via metaschedule (#13180)
  * [Hexagon] Add a test to show how to use multi input async dma pipelin… (#13110)
  * [Hexagon]: Add upload function to hexagon session (#13161)
  * [Hexagon] Add support for instrumentation based profiling for Hexagon (#12971)
  * [Hexagon] Add power manager (#13162)
  * [Hexagon] Add scripts for e2e MetaSchedule tuning demonstration (#13135)
  * [Hexagon] Add feature to copy logcat to --hexagon-debug and add new --sysmon-profile option to run sysmon profiler during the test (#13107)
  * [Hexagon] Async DMA pipelining test suite (#13005)
  * [Hexagon] Enable multi input Async DMA; same queue / stage (#13037)
  * [Hexagon] Do not use `target` test fixture in Hexagon tests (#12981)
  * [Hexagon] 3-stage pipeline; multi queue async DMA for cache read / write (#12954)
  * [Hexagon] vrmpy tensorization for e2e compilation of int8 models (#12911)
  * [Hexagon] Support template-free meta schedule tuning (#12854)
  * [Hexagon] depth_to_space slice op (#12669)
  * [Hexagon] Make allocate_hexagon_array a hexagon contrib API (#13336)
  * [Hexagon] Add fix for vtcm allocation searches (#13197)
  * [MetaSchedule][Hexagon] Add postproc for verifying VTCM usage (#13538)
  * [Hexagon][QNN] Add TOPI strategies for qnn ops mul/tanh/subtract (#13416)
  * [Logging][Hexagon] Improve logging on Hexagon (#13072)
  * [Hexagon] [runtime] Per-thread hardware resource management (#13181)
  * [Hexagon] [runtime] Create objects to manage thread hardware resources (#13111)
  * [QNN][Hexagon] Disable QNN canonicalization pass (#12398)
  * [Hexagon] [runtime] Manage RPC and runtime buffers separately (#13028)
  * [Hexagon] [runtime] VTCM Allocator (#12947)
  * [TOPI][Hexagon] Add schedule and test for maxpool uint8 layout (#12826)
  * [TOPI][Hexagon] Implement quantize op for hexagon (#12820)
  * [Meta Schedule][XGBoost] Update the custom callback function of xgboost in meta schedule (#12141)
  * [TIR] [Hexagon] Add vdmpy intrinsic and transform_layout for tests (#13557)
  * [Hexagon] [runtime] Support VTCM alignments of 128 or 2k (#12999)
  * [HEXAGON][QHL] Clippling the inputs of HVX version of QHL Sigmoid operation (#12919)
  * [Hexagon] [runtime] Add user DMA to device API resource management (#12918)

### LLVM
  * [LLVM] Emit fp16/fp32 builtins directly into target module (#12877)
  * [LLVM] Switch to using New Pass Manager (NPM) with LLVM 16+ (#13515)

### MetaSchedule
  * [MetaSchedule] Make `MultiLevelTiling` apply condition customizable (#13535)
  * [MetaSchedule] Enhance Database Validation Script (#13459)
  * [MetaSchedule] Fix Dynamic Loop from AutoBinding (#13421)
  * [MetaSchedule] Support schedules with cache read in RewriteLayout (#13384)
  * [MetaSchedule] Improve inlining and `VerifyGPUCode` for quantized model workload (#13334)
  * [MetaSchedule] Add JSON Database Validation Scripts (#12948)
  * [MetaSchedule] Fix the order of applying `AutoInline` in `ScheduleUsingAnchorTrace` (#13329)
  * [MetaSchedule] Refactor ScheduleRule Attributes (#13195)
  * [MetaSchedule] Improve the script for TorchBench model tuning & benchmarking (#13255)
  * [MetaSchedule] Enable anchor-block tuning (#13206)
  * [MetaSchedule] Introduce a variant of ModuleEquality to enable ignoring NDArray raw data (#13091)
  * [MetaSchedule] Consolidate module hashing and equality testing (#13050)
  * [MetaSchedule] Support RewriteLayout postproc on AllocateConst  (#12991)
  * [MetaSchedule] Tuning API cleanup & ergonomics (#12895)
  * [MetaSchedule] Fix XGBoost Import Issue (#12936)
  * [MetaSchedule] Add Script for TorchBench Model Tuning & Benchmarking (#12914)
  * [MetaSchedule] Restore `num_threads` parameter in tuning API  (#13561)
  * [MetaSchedule] TorchBench tuning script: add option to disallow operators in sub graph (#13453)
  * [MetaSchedule] Fix segfault in gradient based scheduler (#13399)
  * [MetaSchedule] Add `from-target` Defaults for x86 VNNI Targets (#13383)
  * [MetaSchedule] Fix Task Hanging in EvolutionarySearch (#13246)
  * [MetaSchedule] Allow skipping exact NDArray rewrite in RemoveWeightLayoutRewriteBlock (#13052)
  * [MetaSchedule][UX] Support Interactive Performance Table Printing in Notebook (#13006)
  * [MetaSchedule][UX] User Interface for Jupyter Notebook (#12866)

### microNPU
  * [microNPU] Upgrade Vela to v3.5.0 (#13394)
  * [microNPU] Fixed MergeConstants pass on striped networks (#13281)

### microTVM
  * [microNPU] Upgrade Vela to v3.5.0 (#13394)
  * [microNPU] Fixed MergeConstants pass on striped networks (#13281)
  * [microTVM] Modernize Arm Cortex-M convolution schedules (#13242)
  * [microTVM] Improve code reuse in Corstone300 conv2d tests (#13051)
  * [microTVM] Add Cortex-M DSP schedules for optimal conv2d layouts (#12969)
  * [microTVM] Use default Project Options in template projects and add Makefile for Arduino template project (#12818)
  * [microTVM] Generalize depthwise_conv2d schedule (#12856)
  * [microTVM] add the option to open a saved micro project for debugging (#12495)
  * Added macro generation in MLF export (#12789)
  * [microTVM][Arduino]Add `serial_number` to project options and tests (#13518)
  * [microTVM][Zephyr] Add 'serial_number' option (#13377)
  * [microTVM][PyTorch][Tutorial]Adding a PyTorch tutorial for microTVM with CRT (#13324)

### Misc
  * [CodegenC] Explicit forward function declarations (#13522)
  * [FQ2I] Support converting `dense` -> `add` to `qnn.dense` -> `add` -> `requantize` (#13578)
  * [Minor][Testing] Consolidate IRs into corresponding functions (#13339)
  * Add recursive on loop with marked kUnrolled (#13536)
  * Skip stride check if shape is 1 in IsContiguous (#13121)
  * [TEST] CPU feature detection for x86 and ARM dot product instructions (#12980)
  * [Node] Expose StructuralEqual/Hash handler implemenation to header (#13001)
  * [Tensorize] Add logs to comparator to make debugging tensorize failures easier (#13285)
  * [usmp] Also remap VarNode to USMP-allocated buffer (#12880)
  * [Virtual Machine] Implementation of 'set_output_zero_copy' (#11358)

### ONNX
  * [ONNX] Add converter for FastGelu from Microsoft onnxruntime contrib opset (#13119)
  * [QNN, ONNX] Extension of QLinearMatMul in ONNX front-end for all ranks of input tensors (#13322)

### OpenCL
  * [OpenCL] Introduce OpenCL wrapper to TVM (#13362)
  * [OpenCL]  Introduction of weights on buffers (#13563)
  * [OPENCL][TEXTURE] Test case enhancements and fixes for RPC (#13408)

### Relay
  * [Relay] Fix `CombineParallelDense` slicing axis  (#13597)
  * [Relay] Refactor constant folding over expr into a utility function (#13343)
  * [Relay] Enhancement for fold_scale_axis and simplify_expr (#13275)
  * [Relay] Add ClipAndConsecutiveCast and CastClip to SimplifyExpr (#13236)
  * [Relay] Rewrite division by constant to multiply (#13182)
  * [Relay] Extend split for blocked ConvertLayout pass (#12886)
  * [Relay][transform][SimplifyExpr] simplify adjacent muls and adds with constants (#13213)
  * [Relay][Hexagon] Add per-channel FixedPointMultiply operation (#13080)
  * [IRBuilder][Minor] Add intrinsics like `T.int32x4` (#13361)

### roofline
  * [ROOFLINE] Add support for different dtypes (#13003)
  * [Roofline] Add fma (non-tensorcore) peak flops for CUDA (#13419)

### RPC
  * [RPC] Fix tracker connection termination (#13420)

### Runtime
  * [RUNTIME][CLML] Add fixes to clml runtime api (#13426)
  * [DLPack][runtime] Update DLPack to v0.7 (#13177)

### Target
  * [Target] Replace utility functions with target.features (#12455)
  * [Target] Add Target Parser for Arm(R) Cortex(R) A-Profile CPUs (#12454)
  * [Target] Add target_device_type attribute to override default device_type (#12509)

### TIR
  * [TIR] Add preserve_unit_iters option to blockize/tensorize (#13579)
  * [TIR] Introduce ReduceBranchingThroughOvercompute (#13299)
  * [TIR] Unify index data type when creating prim func (#13327)
  * [TIR] Remove PrimFuncNode::preflattened_buffer_map (#10940)
  * [TIR] Make syntax of AST nodes different than ops (#13358)
  * [TIR] Update ReductionIterNotIndexOutputBuffer to check BlockRealizeN… (#13301)
  * [TIR] Check producer predicate in `ReverseComputeInline` (#13338)
  * [TIR] Add utility for anchor block extraction (#13194)
  * [TIR] Allow IndexMap applied to arguments with different dtypes (#13085)
  * [TIR] Fix handling of int64 extent in blockize and tensorize (#13069)
  * [TIR] Refactor NarrowDataType into DataTypeLegalizer (#13049)
  * [TIR] add unit-tests for upcoming primfunc-slicing (#12794)
  * [TIR] Fix plan buffer allocation location for loop carried dependencies (#12757)
  * [TIR] Fix predefined inverse map in layout transform dtype legalization (#13565)
  * [TIR] Preserve loop annotation after loop partitioning (#13292)
  * [TIR] Use IndexMap to transform NDArray (#12949)
  * [TIR] Preserve loop annotations in inject_software_pipeline pass (#12937)
  * [TIR][Schedule] Support for specific consumer block targeting in cache_write (#13510)
  * [TIR][Hexagon] Add vtcm memory capacity verification for Hexagon target (#13349)
  * [TIR][Transform] Optional data-flow analysis in RemoveNoOp (#13217)
  * [TIR][Analysis][Arith] Implement basic data-flow analysis (#13130)
  * [TIR][Bugfix] Fix AXIS_SEPARATORS in tir.Schedule.transform_layout (#13326)
  * [TIR][Arith] Use TryCompare to narrow inequalities if possible (#13024)
  * [TIR][Primitive] Support rolling_buffer schedule primitive in TensorIR (#13033)
  * [Arith][TIR] Check for constant offsets of known literal constraints (#13023)
  * [TIR][Arith] Implement kApplyConstraintsToBooleanBranches extension (#13129)
  * [TIR][Schedule] Add cache_index to precompute index of buffer load (#13192)
  * [TIR][Schedule] Add cache_inplace primitive to cache opaque buffer (#12939)
  * [UnitTest][TIR] Support IRModule comparisons in CompareBeforeAfter (#12920)
  * [TIR][Arith] Prove conditionals by transitively applying knowns (#12863)
  * [TIR, MetaSchedule] Preserve unit block iters for auto-tensorization (#12974)
  * [TIR][MetaSchedule] Add regression test for layout_rewrite extent=1 (#12916)
  * [TIR][Transform] Keep the allocate buffers order after update buffer allocation location (#13560)
  * [TIR][Schedule] Fix cache_read loc detecting and region_cover checking (#13345)
  * [TIR][Transform] Clear buffer_map during MakeUnpackedAPI (#12891)
  * [TIR][Schedule] Relax cache read/write's restriction and fix unexpected behavior (#12766)

### TOPI
  * [TOPI] Implement Einsum with reduction axes (#12913)
  * [TOPI] Add layer norm operator (#12864)
  * [TOPI] Add handwritten matvec for dynamic cases (#13423)
  * [TOPI] Fix dtype legalize logic for CPU dot product instruction (#12865)
  * [TOPI][Hexagon] Implement quantized adaptive_avg_pool1d for hexagon (#13282)
  * [TOPI][Hexagon] Implement quantized depthwise conv2d (#12499)

### Torch
  * [TVM PyTorch Integration] optimized_torch & as_torch how-to guide (#12318)
  * [frontend][pytorch]Support aten::Tensor_split operator (#12871)

### TVMC
  * [TVMC] Global pass context for compile and tune (#13309)

### TVMScript
  * [TVMScript] Improvements tvm.script.highlight (#13438)
  * [TVMScript] Reorganize the folder structure (#12496)
  * [TVMScript] TIR parser (#13190)
  * [TVMScript] IRModule parser (#13176)
  * [TVMScript] Evaluator, core parser, var table (#13088)
  * [TVMScript] AST, Source and diagnostics for Parser (#12978)
  * [TVMScript] Import TIR methods into the IRBuilder (#12900)
  * [TVMScript] Infer T.match_buffer parameters for region (#12890)

## v0.11.1 (2023-03-09)

# Introduction

This is a `v0.11.1` bug fix release on top of `v0.11.0` (see https://github.com/apache/tvm/issues/13899), incorporating a fix to the Python dependencies description.

## What's Changed

### Python dependencies

* Add typing_extensions requirement (https://github.com/apache/tvm/pull/14244)
* Adjust version to 0.11.1 (https://github.com/apache/tvm/pull/14300)


## v0.12.0 (2023-05-17)

# Introduction

The TVM community has worked since the v0.11.1 release to deliver the following new exciting improvements! The main tags are below (**bold text is with lots of progress**):

- Community, RFC;
- Runtime: ACL(ArmComputeLibrary), Adreno, OpenCL & CLML, ROCm, CUDA & CUTLASS & TensorRT, Ethosn, CRT, Hexagon, Metal, Web & WASM, others about runtime;
- Frontend: TensorFlow/tflite, Pytorch/Torch, Paddle, OneFlow, keras;
- TE, Relay, BYOC, TOPI, Arith, **TIR, TVMScript, MetaSchedule**, Schedule;
- CI, Tests, BugFix, Docs, Docker, Build;
- Android, **microTVM**, Target, AutoTVM, AOT, LLVM.

Please visit the full listing of commits for a complete view: [v0.11.1...v0.12.0](https://github.com/apache/tvm/compare/v0.11.1...v0.12.0).

Thanks @ysh329 for the great effort to the release process as the release manager.

# Community

- Reviewer
  - [Cheng Wen](https://github.com/apache/tvm/pull/14153)  
  - [blackkker](https://github.com/apache/tvm/pull/13686)  
  - [Min Chen](https://github.com/apache/tvm/pull/13628)  
  - [janCommunityetsc](https://github.com/apache/tvm/pull/14359)  
  - [mkatanbaf](https://github.com/apache/tvm/pull/14085)  
  - [alanmacd](https://github.com/apache/tvm/pull/13814)  
- Committer
  - [Yaxing Cai](https://github.com/apache/tvm/pull/13787)  
  - [Hongyi Jin](https://github.com/apache/tvm/pull/13784)  
- PMC
  - [Wrongtest](https://github.com/apache/tvm/pull/13893)  

# RFC

 * [[RFC] Introduce PresburgerSet (#99)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0099-introduce-PresburgerSet.md) ([`e17994b`](https://github.com/apache/tvm-rfcs/commit/e17994b90d9278a280d019f3c8ad9065c9a3f584))
 * [[RFC] Further Unify Packed and Object in TVM Runtime (#97)](https://github.com/apache/tvm-rfcs/blob/main/rfcs/0097-unify-packed-and-object.md) ([`d646a22`](https://github.com/apache/tvm-rfcs/commit/d646a22eb00b8138573cb856edb16a7b05906e1e))

----

# Runtime

## ArmComputeLibrary

- [[ACL][TESTING] Use pytest.mark.parametrize in ACL conv2d tests](https://github.com/apache/tvm/pull/14011)  
- [[ACL] Prevent offloading of per-channel quantized operators](https://github.com/apache/tvm/pull/14484)  
- [[CL] Update Compute Library from v22.11 to v23.02.1](https://github.com/apache/tvm/pull/14426)  

## Adreno

- [[Adreno] Extend pack_filter for HWIO layout](https://github.com/apache/tvm/pull/13939)  
- [[Adreno] Update interface of AnnotateMemoryScope pass](https://github.com/apache/tvm/pull/13779)  
- [[Adreno] Optimize reduction schedule](https://github.com/apache/tvm/pull/13781)  
- [[BENCHMARK][ADRENO] Adreno Benchmarks with texture](https://github.com/apache/tvm/pull/13675)  
- [[BENCHMARKS][CLML] Adreno benchmarks with CLML BYOC path added](https://github.com/apache/tvm/pull/13696)  
- [[BENCHMARKS][ADRENO] Documentation for Adreno (Texture) benchmarks](https://github.com/apache/tvm/pull/13679)  
- [[DOCS][ADRENO] Improved Adreno documentation](https://github.com/apache/tvm/pull/13867)  

## OpenCL & CLML

- OpenCL
  - [[OpenCL][Textures] Always use SSA for texture loading](https://github.com/apache/tvm/pull/14397)  
  - [[OpenCL] Refactor OpenCL init function](https://github.com/apache/tvm/pull/13919)  
  - [[OpenCL] Implement save/load pre-compiled programs](https://github.com/apache/tvm/pull/13868)  
  - [[CMake][OpenCL] Remove warning for OpenCL wrapper](https://github.com/apache/tvm/pull/13683)  
  - [[RUNTIME][OPENCL] OpenCL host pointer support to acheive zero copy](https://github.com/apache/tvm/pull/13413)  
- CLML
  - [[CLML][RUNTIME] Enable more ops in CLML runtime](https://github.com/apache/tvm/pull/13834)  
  - [[CLML][RELAY] Enable Pad and Conv2d layer fusion](https://github.com/apache/tvm/pull/13649)  
  - [[CLML][CODEGEN] CLML native codegen utility](https://github.com/apache/tvm/pull/13837)  
  - [[CLML] Version compatibility and various test cases](https://github.com/apache/tvm/pull/13670)  
  - [[CLML] Changes corresponding to OpenCL workspace refactorization](https://github.com/apache/tvm/pull/13972)  
  - [[RUNTIME][CLML] OpenCLML tuning and profiling enhanced](https://github.com/apache/tvm/pull/13843) 

## ROCm

- [[ROCM] Fixes compiling on ROCM 5 and accuracy on dense op](https://github.com/apache/tvm/pull/13847)  

## CMSIS-NN

- [[CMSIS-NN] Global function that provides range based on dtype](https://github.com/apache/tvm/pull/13652)  
- [[CMSIS-NN] Add int16 add and mul operator support](https://github.com/apache/tvm/pull/13920)  
- [[CMSIS-NN] Add a runtime error message](https://github.com/apache/tvm/pull/13643)  
- [[CMSIS-NN] Reduction in code size of AOT test runner binary](https://github.com/apache/tvm/pull/13815)  
- [[CMSIS-NN] Remove support for the old CMSIS NN project](https://github.com/apache/tvm/pull/13760)  
- [[CMSIS-NN] Support CMSIS NN from new GitHub location](https://github.com/apache/tvm/pull/13656)  
- [[CMSIS-NN] Add Cortex-M85 support](https://github.com/apache/tvm/pull/13644)  

## CUDA & CUTLASS & TensorRT

- [[CUDA][Schedule] Better Layout Transform Schedules](https://github.com/apache/tvm/pull/14167)  
- [[Profiler] Allow user to flush L2 cache in `time_evalutor` function for profiling CUDA kernels](https://github.com/apache/tvm/pull/13726)  
- [[Codegen][CUDA] Add error message for missing fragment info](https://github.com/apache/tvm/pull/14073)  
- [[CUTLASS][Ansor] Combine CUTLASS and Ansor](https://github.com/apache/tvm/pull/13879)  
- [[TensorRT] Fix BiasAdd with correct axis attribute](https://github.com/apache/tvm/pull/13953)  
- [[TRT][BYOC] allow strided_slice ops on selected dimensions (#14142)](https://github.com/apache/tvm/pull/14144)  

## Ethosn

- [[ETHOSN] Update driver stack version to 22.11](https://github.com/apache/tvm/pull/13637)  
- [[ETHOSN] Support for addition with constant input](https://github.com/apache/tvm/pull/13931)  
- [[ETHOSN] Apply FoldConstant before NPU partitioning](https://github.com/apache/tvm/pull/13848)  
- [[ETHOSN] Remove support for NPU driver 22.08](https://github.com/apache/tvm/pull/13763)  
- [[ETHOSN] Fix for the mock inference after NPU driver update](https://github.com/apache/tvm/pull/13650)  
- [[ETHOSN] Remove requantize dependency on resize](https://github.com/apache/tvm/pull/14422)  
- [[ETHOSN] Add support for experimental compiler option](https://github.com/apache/tvm/pull/13410)  

## CRT

- [[CRT] USE CMake for CRT standalone libraries](https://github.com/apache/tvm/pull/14025)  
- [[CRT][microTVM] Enable USMP by default for AoTExecutor + CRT runtime](https://github.com/apache/tvm/pull/14107)  
- [[CRT]Cleanup unused macros in crt_config.h.template](https://github.com/apache/tvm/pull/14125)  

## Hexagon

- [[Hexagon][TOPI] Use IndexMap axis separator instead of TE](https://github.com/apache/tvm/pull/14459)  
- [[Hexagon] Add concept of DMA groups](https://github.com/apache/tvm/pull/14254)  
- [[Hexagon] Improve cache management strategy for HexagonBuffer](https://github.com/apache/tvm/pull/13883)  
- [[Hexagon] Denote DMA cache bypass as experimental feature](https://github.com/apache/tvm/pull/13699)  
- [[Hexagon] Adapt some intrinsics for high vector lanes](https://github.com/apache/tvm/pull/14345)  
- [Hexagon compilation on MacOS system](https://github.com/apache/tvm/pull/14308)  
- [[Hexagon] Enable depthwise conv2d NHWC with an HWIO kernel layout](https://github.com/apache/tvm/pull/13414)  
- [[Hexagon][QNN] Improve performance wo QNN canonicalization](https://github.com/apache/tvm/pull/13734)  
- [[Hexagon][Metaschedule] Add timeout_sec arg to get_hexagon_local_builder](https://github.com/apache/tvm/pull/13828)  
- [[Hexagon] Fix deprecated call for data layout size in bits](https://github.com/apache/tvm/pull/14438)  
- [[Hexagon] Allow scalar tensors to have null shape during allocation](https://github.com/apache/tvm/pull/14376)  
- [[Hexagon][runtime] Make HexagonThreadManager::CheckSemaphore thread safe](https://github.com/apache/tvm/pull/13609)  
- [[Hexagon] Float and quantized dense operators with schedules](https://github.com/apache/tvm/pull/12873)  
- [[Hexagon][CI] Updated sha for builder LLVM](https://github.com/apache/tvm/pull/13418)  
- [[Hexagon][CI] Update the docker image ID to reflect newer LLVM](https://github.com/apache/tvm/pull/13870)  
- [[Hexagon] Switch from default_rng to random in Hexagon tests](https://github.com/apache/tvm/pull/13616)  
- [[Hexagon] Add hexagon user DMA intrins for tensorization](https://github.com/apache/tvm/pull/13719)  
- [[hexagon] Hexagon inference fix](https://github.com/apache/tvm/pull/14533)  

## Metal

- [[METAL][CODEGEN] testcase for ramp codegen](https://github.com/apache/tvm/pull/14331)  
- [[CODEGEN][METAL] Fix unaligned vector load](https://github.com/apache/tvm/pull/14332)  
- [[CODEGEN][METAL] Fix ramp codegen](https://github.com/apache/tvm/pull/14330)  

## MicroNPU

- [[microNPU] Sum legalization support](https://github.com/apache/tvm/pull/13997)  
- [[microNPU] Add rescale parameters for binary elementwise](https://github.com/apache/tvm/pull/13890)  
- [[microNPU] Add hardware constraints for binary elementwise](https://github.com/apache/tvm/pull/13772)  
- [[microNPU] Add support for TFLite PAD](https://github.com/apache/tvm/pull/13732)  
- [[microNPU] Upgrade Vela to v3.7.0](https://github.com/apache/tvm/pull/14374)  
- [[microNPU] Merge LUT activation with binary elementwise operation](https://github.com/apache/tvm/pull/13935)  
- [[microNPU] Upgrade to 22.08 version of Arm(R) Ethos(TM)-U NPU drivers](https://github.com/apache/tvm/pull/13529)  
- [[microNPU] Add relu6 relu_n1_to_1 test cases for Ethos-U](https://github.com/apache/tvm/pull/13645)  
- [[microNPU] Add a legalization test for TFLite PAD](https://github.com/apache/tvm/pull/13750)  
- [[microNPU] Disable copying weights to SRAM for FullyConnected ops in CopyConstants scheduler](https://github.com/apache/tvm/pull/13588)  
- [[microNPU] Add support for ResizeNearestNeighbor with half_pixel_centers=True](https://github.com/apache/tvm/pull/14401)  


## Web & WASM

- [[Web] Try to upgrade WebGPU API usage to the latest](https://github.com/apache/tvm/pull/13731)  
- [[WEB] Reduce memleak in web runtime](https://github.com/apache/tvm/pull/14086)  
- [[WEB] WebGPU Codegen](https://github.com/apache/tvm/pull/14048)  
- [[WEB] Update web runtime to support latest emcc](https://github.com/apache/tvm/pull/14046)  
- [[WASM][FIX] test tests/node/websock_rpc_test.py](https://github.com/apache/tvm/pull/13862)  

## Others about Runtime

- [[FIX][RUNTIME] Convert container with function value type](https://github.com/apache/tvm/pull/14024)  
- [[RUNTIME] Fix the manual determination of cores in FillDataForMeasure](https://github.com/apache/tvm/pull/13849)  
- [[RUNTIME] Fix determination of big/little cores domains](https://github.com/apache/tvm/pull/13832)  
- [[Runtime] Fix Potential DeviceAPIManager Memory Bug](https://github.com/apache/tvm/pull/14114)  
- [[Runtime] Fix high RAM usage when saving / loading paramters of big models](https://github.com/apache/tvm/pull/14147)  
- [[Runtime] Runtime module property mask for Metal and Vulkan](https://github.com/apache/tvm/pull/14524)  
- [[Runtime] Introduce runtime module property](https://github.com/apache/tvm/pull/14406)  
- [[Runtime] Add missing Type2Str for TVMByteArray](https://github.com/apache/tvm/pull/14051)  


# Android

- [[Android] Fix using system libraries in Android apps](https://github.com/apache/tvm/pull/14145)  
- [[TOOL][NATIVE] Android native application for deploy and run](https://github.com/apache/tvm/pull/13791)  
# AOT
- [[AOT] Added a test for detecting output size post MLF export](https://github.com/apache/tvm/pull/13655)  
- [[AOT]Aot module post-test error workaround](https://github.com/apache/tvm/pull/13685)  
- [[AOT]Raise error when input name is not valid](https://github.com/apache/tvm/pull/14322)  
- [[AoT]Add get_input_name function to AoT Module](https://github.com/apache/tvm/pull/14071)  
# Arith
- ["[Arith] Simplifications for floormod(x](https://github.com/apache/tvm/pull/13936)  
- [[Arith] Implemented PMatchesOneOf and matches_one_of](https://github.com/apache/tvm/pull/13933)  
- [[Arith][UnitTest] Parametrize tests of RewriteSimplifier](https://github.com/apache/tvm/pull/13923)  
- [[Arith] Use ConstIntBound to remove negative numerator when lowering](https://github.com/apache/tvm/pull/13724)  
- ["[Arith][Bugfix] Simplify ""x - 1 < y"" into ""x <= y"""](https://github.com/apache/tvm/pull/14528)  
- ["[Arith] Add simplification rule for `x - max(x+y](https://github.com/apache/tvm/pull/14271)  
- [[Arith] Updated incorrect simplification rule](https://github.com/apache/tvm/pull/13922)  
- [[Arith] Allow const folding on fp16 involving one and zero](https://github.com/apache/tvm/pull/13631)  
- [](https://github.com/apache/tvm/pull/13918)  
- [[ARITH] Enhance CanProve to handle symbolic bound](https://github.com/apache/tvm/pull/14523)  
- [[ARITH] support floordiv in deduce bound](https://github.com/apache/tvm/pull/13880)  
- [[Arith] Support eq in detect_clip_bound](https://github.com/apache/tvm/pull/13746)  
- [[Fix][Arith] Analyzer simplification starts with canonical](https://github.com/apache/tvm/pull/13875)  
# AutoTVM
- [[AutoScheduler][AutoTVM] Enable xgboost >= 1.7.x new changes](https://github.com/apache/tvm/pull/14036)  
# BugFix
- [[BugFix][UMA] Protect target registration](https://github.com/apache/tvm/pull/13624)  
- [[BugFix][Runtime] Add missing check for `PackedFunc`](https://github.com/apache/tvm/pull/13687)  
- [[Bugfix][TIR] Fix version conflict with typing for Python 3.8.0](https://github.com/apache/tvm/pull/13744)  
- [Fix build platform environment variable](https://github.com/apache/tvm/pull/13914)  
- [[BugFix][TVMScript] Fix the roundtripability of  intrinsic pow](https://github.com/apache/tvm/pull/13692)  
- [[BugFix] Pylance emits the warnning 'Code is unreachable'](https://github.com/apache/tvm/pull/13673)  
- [[BugFix][TVMScript]fix var capturing order error](https://github.com/apache/tvm/pull/13640)  
- [[BugFix][TVMScript] Parser crash](https://github.com/apache/tvm/pull/13630)  
- [[Bugfix][TVMScript] Handle LetStmt for `var1 = var2` expressions](https://github.com/apache/tvm/pull/14320)  
- [[Bug][CodeGen,Cuda]fix cast fp16 to int8/uint8 in cuda](https://github.com/apache/tvm/pull/13641)  
- [[fix] MXNet dot for all tensor dimensions](https://github.com/apache/tvm/pull/11760)  
- [[Bugfix] Conv1Dtranspose default kernel layout should be IOW](https://github.com/apache/tvm/pull/14482)  
- [[Bugfix] Conv3Dtranspose default kernel layout should be IODHW](https://github.com/apache/tvm/pull/14340)  
- [[BugFix] Support rewrite_once when the number of callbacks > 1](https://github.com/apache/tvm/pull/14344)  
- [[Bugfix][TIR] Fix version conflict with typing for different Python versions (3.8.0-3.10.0)](https://github.com/apache/tvm/pull/13820)  
- [Fix out of bound enum conversion](https://github.com/apache/tvm/pull/13967)  
- [[bugfix] Fix the write buffer scope of `mma_store_impl`](https://github.com/apache/tvm/pull/14174)  
- [[BugFix][Runtime] Fix Incorrect node information](https://github.com/apache/tvm/pull/13693)  
# Build
- [[Build] Expose missing USE_VERILATOR in cmake](https://github.com/apache/tvm/pull/13676)  
- [[Build] Fix find_include_path when using TVM python package](https://github.com/apache/tvm/pull/14007)  
- [[Build] Fix misleading error messages](https://github.com/apache/tvm/pull/13887)  
- [[Build][Bugfix] Use CMAKE_ prefix for <LANG>_COMPILER_LAUNCHER](https://github.com/apache/tvm/pull/13697)  
# BYOC
- [[BYOC] DNNL C_SRC Fix](https://github.com/apache/tvm/pull/14267)  
- [[BYOC] Update CUTLASS backend (SIMT support and codegen clean up)](https://github.com/apache/tvm/pull/14056)  
# CI
- [[CI][microTVM] Enable USE_MICRO for mac and windows CI builds](https://github.com/apache/tvm/pull/14393)  
- [[CI] Pass the 'path' parameter passed to cmake_build to the task_build.py script](https://github.com/apache/tvm/pull/13905)  
- [[CI][EZ] Upgrade CI Lint Image](https://github.com/apache/tvm/pull/14373)  
- [[CI][Lint] Update black](https://github.com/apache/tvm/pull/14346)  
- [[CI][Flaky] Skip zephyr_qemu-x86 tests that are part of task_python_microTVM](https://github.com/apache/tvm/pull/14005)  
- [[CI] Fix for NNPack error due to misalignment with pthreadpool library](https://github.com/apache/tvm/pull/13940)  
- [[ci] Disable Windows-Static-Runtime](https://github.com/apache/tvm/pull/13951)  
- [[ci][docker] Make branch names valid before using them as tags](https://github.com/apache/tvm/pull/13738)  
- [[CI] Cross-compile libtvm_runtime to Aarch64 and run tests](https://github.com/apache/tvm/pull/13714)  
- [[CI] Include static builds of the runtime as part of CI](https://github.com/apache/tvm/pull/13612)  
- [[CI] Update rerun list for tvm-bot](https://github.com/apache/tvm/pull/13817)  
- [[CI] Update ci_minimal docker image to cross-compile TVM to aarch64](https://github.com/apache/tvm/pull/13776)  
- [[CI] Update ci_arm docker image to have LLVM 15](https://github.com/apache/tvm/pull/14296)  
- [[CI] Update Compute Library to v22.11](https://github.com/apache/tvm/pull/14084)  
- [[CI] Fix broken model link](https://github.com/apache/tvm/pull/14458)  
- [[CI][ETHOSN] Add ssh to the driver stack installation](https://github.com/apache/tvm/pull/14246)  
- [[CI] Fix android build by constraining numpy version](https://github.com/apache/tvm/pull/13648)  
- [[CI] NNPACK build issue workaround](https://github.com/apache/tvm/pull/13873)  
- [[CI] Update GPU image for CUDA 11.7](https://github.com/apache/tvm/pull/14363)  
- [[CI] Update CUDA to 11.7](https://github.com/apache/tvm/pull/14293)  
- [[CI] Update cpu and gpu image](https://github.com/apache/tvm/pull/14245)  
- [[CI] Enable USE_MICRO in minimal cross ISA build](https://github.com/apache/tvm/pull/13942)  
- [[CI][microTVM]Update ci_cortexm image](https://github.com/apache/tvm/pull/13764)  
- [[CI][Docker][Cortex-M]Update scripts to update ci_cortexm to Ubuntu 20.04](https://github.com/apache/tvm/pull/13736)  
- [[CI] Fix MLF input and output name map](https://github.com/apache/tvm/pull/13740)  
- [[CI] Pin sccache version to 0.3.3](https://github.com/apache/tvm/pull/14530)  
- [[CI] Add llvm-15 and mlir-15 to Docker setup](https://github.com/apache/tvm/pull/14303)  
- [[CI] Add onnx dependency to test_auto_tensorize.py::test_vnni_bert_int8](https://github.com/apache/tvm/pull/14102)  
- [[CI] Fix test skipping pytest attribute](https://github.com/apache/tvm/pull/14064)  
- [[skip ci][ci][docker] Add cross compilation libs](https://github.com/apache/tvm/pull/13800)  

# Tests

- [[Tests] Replace pytest.main with tvm.testing.main](https://github.com/apache/tvm/pull/13717)  
- [[TESTING] Enable execution of test_packed_8x8x32_resnet50](https://github.com/apache/tvm/pull/13799)  
- [[testing] Use tuples for numpy indexing](https://github.com/apache/tvm/pull/14476)  
- [[testing][py_converter] Enhance py_converter to better support entire modules](https://github.com/apache/tvm/pull/13769)  
- [[Unittest] merge test_cp_async_in_if_then_else into test_tir_transform_inject_ptx_async_copy](https://github.com/apache/tvm/pull/14138)  
- [[UnitTest] Parametrized test_arith_iter_affine_map::test_padding](https://github.com/apache/tvm/pull/13774)  

# Docker
- [[Docker] Update ci-cpu and ci-arm to tag 20230223-070143-a3b51f11b](https://github.com/apache/tvm/pull/14116)  
- [[docker][microTVM]Fix Zephyr 0.15.2 SDK installation and separate Zephyr python environment](https://github.com/apache/tvm/pull/13829)  
- [[docker][microTVM]Update zephyr version to 3.2 and Zephyr SDK to 0.15.2](https://github.com/apache/tvm/pull/13806)  
- [[Docker]Add dialout group by default on login](https://github.com/apache/tvm/pull/13810)  
- [[Docker] Add script to build llvm from source](https://github.com/apache/tvm/pull/13823)  
- [[DOCKER] Configurable NDK version support](https://github.com/apache/tvm/pull/14000)  
- [[Docker update] Update ci_cpu tag to the latest from tlcpackstaging](https://github.com/apache/tvm/pull/13748)  

# Docs
- [[Doc] fix doc for tvm.te.const()](https://github.com/apache/tvm/pull/13904)  
- [Add v0.11.0 docs link to site](https://github.com/apache/tvm/pull/14181)  
- [[docs] Remove empty code blocks](https://github.com/apache/tvm/pull/13689)  
- [[docs] Add details about patch releases](https://github.com/apache/tvm/pull/14301)  
- [[Docs] Update listed tvmc python dependencies](https://github.com/apache/tvm/pull/14341)  
- ["[docs] Add ""Open with Colab"" button to documentation"](https://github.com/apache/tvm/pull/13627)  
- [[Docs] Add `typing-extensions` dependency guide](https://github.com/apache/tvm/pull/13730)  
- [[Docs] Fix MetaSchedule Docs](https://github.com/apache/tvm/pull/14480)  
- [[FIX] Fix Typos in Docs and Comments](https://github.com/apache/tvm/pull/13793)  
- [[HotFix][docs] Use correct Colab button URL](https://github.com/apache/tvm/pull/13725)  
# Frontend
- TensorFlow & TFLite
  - [[Frontend][Tensorflow] Update Select to SelectV2](https://github.com/apache/tvm/pull/13884)  
  - [[Frontend][TFLite] Fix conv2d import bug](https://github.com/apache/tvm/pull/14124)  
  - [[TFLite] Support for BATCH_MATMUL tflite operator](https://github.com/apache/tvm/pull/14423)  
- Pytorch
  - [[Pytorch] frontend full_impl fix](https://github.com/apache/tvm/pull/14122)  
  - [[PyTorch] Fix in matmul function that enables working with all sizes](https://github.com/apache/tvm/pull/13927)  
  - [[Pytorch][Relay] aten::_weight_norm implementation](https://github.com/apache/tvm/pull/13661)  
  -  [[Torch] Added tests in test_forward_linear](https://github.com/apache/tvm/pull/13937)  
  -  [[Torch] Fix advanced indexing with NoneType index arguments](https://github.com/apache/tvm/pull/13826)  
  -  [[TORCH] scatter_reduce implementation](https://github.com/apache/tvm/pull/14018)  
- ONNX
  - [[Frontend] Add ONNX importer for QLinearSoftmax](https://github.com/apache/tvm/pull/14425)  
  - [[ONNX] QGemm support](https://github.com/apache/tvm/pull/13747)  
  - [[ONNX][TOPI] Add `DFT` operator](https://github.com/apache/tvm/pull/13999)  
  - [[Frontend] [ONNX] Support sequence_lens of GRU](https://github.com/apache/tvm/pull/13587)  
  - [[ONNX] Extend converter for Attention from Microsoft onnxruntime contrib opset](https://github.com/apache/tvm/pull/13797)  
  - [[ONNX] Add converter for QAttention from Microsoft onnxruntime contrib opset](https://github.com/apache/tvm/pull/13654)  
  - [[ONNX][TORCH] Replace scatter op by scatter_elements](https://github.com/apache/tvm/pull/14019)  
  - [[ONNX] Support ScatterElements with reduction](https://github.com/apache/tvm/pull/13894)  
  - [[ONNX] Support Bitwise operations](https://github.com/apache/tvm/pull/13888)  
  - [[ONNX] Support Bernoulli op on ONNX front-end](https://github.com/apache/tvm/pull/13802)  
  - [[ONNX] Extend reduction types supported by ScatterND](https://github.com/apache/tvm/pull/13946)  
  - [[ONNX] Support SequenceEmpty op](https://github.com/apache/tvm/pull/13866)  
  - [[ONNX] Support SequenceErase op](https://github.com/apache/tvm/pull/13865)  
  - [[ONNX] Support SequenceLength op](https://github.com/apache/tvm/pull/13863)  
- Keras
  - [[Keras] Fix importing conv2d_transpose for NHWC layout](https://github.com/apache/tvm/pull/13998)  
- OneFlow
  - [[Frontend][Oneflow] Use FLOW_2_STR_DTYPE for dtype](https://github.com/apache/tvm/pull/14454)  
- Paddle
  - [[PaddlePaddle Hackathon 4][Frontend][Paddle]add conv3d for paddle frontend](https://github.com/apache/tvm/pull/14290)  
  - [[Frontend][PaddlePaddle] Fix bug in tests for upgrading paddlepaddle to 2.4.2](https://github.com/apache/tvm/pull/14206)  
  - [[Frontend][Paddle]add take_alone_axis and topk converter for paddle frontend](https://github.com/apache/tvm/pull/14170)  
  - [[Frontend][Paddle] Add where_index op and add vm for paddle frontend's unitest](https://github.com/apache/tvm/pull/14099)  
  - [[Frontend][Paddle] Add norm and one_hot_v2 op](https://github.com/apache/tvm/pull/14049)  
  - ["[Frontend][PaddlePaddle] Add topk op and Fix bug](https://github.com/apache/tvm/pull/13701)  
  - [[PaddlePaddle Hackathon 4][Frontend][Paddle]Add tile/mish/stack/unstack/silu/softshrink/where op for paddle frontend](https://github.com/apache/tvm/pull/14160)  
  - [[Frontend][Paddle]fix eye and dist](https://github.com/apache/tvm/pull/14292)  
  - [[PaddlePaddle Hackathon 4][Frontend][Paddle]add grid-sample/gaussian_random/flip/fill_zeros_like/unique for paddle frontend](https://github.com/apache/tvm/pull/14277)  
  - [[PaddlePaddle Hackathon 4][Frontend][Paddle]add thresholded_relu/index_select/eye/linspace/take_alone_axis/dist for paddle frontend](https://github.com/apache/tvm/pull/14172)  

# microTVM

- [[microTVM] Clean-up test_crt.py and add to pylint](https://github.com/apache/tvm/pull/13886)  
- [[microTVM] Build standalone_crt with cmake instead of makefile](https://github.com/apache/tvm/pull/13600)  
- [[microTVM] additional refactoring for enabling USE_MICRO in more builds](https://github.com/apache/tvm/pull/13909)  
- [[microTVM] Fix host-driven AOT memory workspaces](https://github.com/apache/tvm/pull/13807)  
- [[microTVM] Fix MacOS build with USE_MICRO=ON](https://github.com/apache/tvm/pull/13711)  
- [[microTVM] Use QNN schedules to give SOTA performance](https://github.com/apache/tvm/pull/13752)  
- [[microTVM]Fix more security issues with pyproject](https://github.com/apache/tvm/pull/14434)  
- [[microTVM] Update poetry to fix security issues](https://github.com/apache/tvm/pull/14429)  
- [[microTVM]Enable TVMC micro with AoT Executor](https://github.com/apache/tvm/pull/14077)  
- [[microTVM]Add test for MLPerfTiny models](https://github.com/apache/tvm/pull/13978)  
- [[microTVM][CRT]Move Makefile to CMake to be cross-platform compatible](https://github.com/apache/tvm/pull/14013)  
- [[microTVM]Refactor crt_config.h header file generation](https://github.com/apache/tvm/pull/13955)  
- [[microTVM] Refactor required external functions in CRT to platform-template.c](https://github.com/apache/tvm/pull/13885)  
- [[microTVM] Update Zephyr version and Zephyr SDK version](https://github.com/apache/tvm/pull/13818)  
- [[microTVM]Refactor test and add skip to current failing tests/boards](https://github.com/apache/tvm/pull/13858)  
- [[microTVM] Update tutorials](https://github.com/apache/tvm/pull/13845)  
- [[microTVM] Add tutorial on how to generate MLPerfTiny submissions](https://github.com/apache/tvm/pull/13783)  
- [[microTVM][Zephyr]Add project files for mlperftiny submission](https://github.com/apache/tvm/pull/13690)  
- [[microTVM]Add default value to unspecified project options in project API](https://github.com/apache/tvm/pull/13610)  
- [[microTVM]Add MLPerfTiny test harness](https://github.com/apache/tvm/pull/14309)  
- [[microTVM] Fix tvmc tutorial](https://github.com/apache/tvm/pull/14076)  
- [[microTVM][Zephyr] Remove unnecessary use of generate_c_interface_header](https://github.com/apache/tvm/pull/14091)  
- [[microTVM][CRT]Separate CRT template project from standalone CRT build](https://github.com/apache/tvm/pull/13812)  
- [[microTVM][Zephyr] Fix flash command for nrfjprog](https://github.com/apache/tvm/pull/13723)  
- [[microTVM][Zephyr] Fix TVMC test on hardware](https://github.com/apache/tvm/pull/13598)  
- [[microTVM] Custom IDE Tutorial](https://github.com/apache/tvm/pull/13857)  
- [[microTVM] tuning on micro targets with meta-schedule](https://github.com/apache/tvm/pull/13514)  
- [[microTVM] Allow multiple runners in tuning micro models with meta-schedule](https://github.com/apache/tvm/pull/13811)  
- [[microTVM] Replace arm_nnsupportfunctions.h with arm_acle.h](https://github.com/apache/tvm/pull/13363)  

# LLVM

- [[LLVM] Use DataLayout::getABITypeAlign instead of getABITypeAlignment](https://github.com/apache/tvm/pull/14534)  
- [[LLVM] Add missing `override` to GetFormat and GetPropertyMask](https://github.com/apache/tvm/pull/14470)  
- [[LLVM] Add guard for #include <llvm/Transforms/IPO/PassManagerBuilder.h>](https://github.com/apache/tvm/pull/14469)  
- [[LLVM] Remove call to EmitDebugLocation from AddAliasInfo](https://github.com/apache/tvm/pull/13872)  
- [[LLVM] Use std::nullopt instead of llvm::None](https://github.com/apache/tvm/pull/13617)  
- [[LLVM] Fix registerCallbacks API after recent change](https://github.com/apache/tvm/pull/14323)  
- [[LLVM] Add support to generate llvm.assume](https://github.com/apache/tvm/pull/14294)  
- [[LLVM] Add support for DeclBufferNode](https://github.com/apache/tvm/pull/14103)  
- [[LLVM][BugFix] Fix include Triplet.h bug when LLVM version>= 17](https://github.com/apache/tvm/pull/14235)  
- [[TEST] Fix division by 0 in llvm codegen test](https://github.com/apache/tvm/pull/14232)  
- [[SVE] Adding codegen tests for SVE](https://github.com/apache/tvm/pull/14239)  


# MetaSchedule
- [[MetaSchedule] Introducing MemHammer](https://github.com/apache/tvm/pull/14164)  
- [[MetaSchedule] Introduce Async Pipeline in MultiLevelTiling](https://github.com/apache/tvm/pull/14009)  
- [[MetaSchedule][ARM] Enable ARM CPU intrinsic for MetaSchedule](https://github.com/apache/tvm/pull/14209)  
- [[MetaSchedule] Use `shared.dyn` for Tensor Core Schedule Rules](https://github.com/apache/tvm/pull/13891)  
- [[MetaSchedule] add fp16-16-32 TensorCores rule to default settings](https://github.com/apache/tvm/pull/13822)  
- [[MetaSchedule][Hexagon] Improve vectorization for standalone elementwise op](https://github.com/apache/tvm/pull/14408)  
- ["[MetaSchedule] Add ""disabled_pass"" option in tuning API"](https://github.com/apache/tvm/pull/13659)  
- [[MetaSchedule] Fix anchor-block flow with empty design space generator](https://github.com/apache/tvm/pull/14047)  
- [[Metaschedule] get_top_k should not return not built records](https://github.com/apache/tvm/pull/13824)  
- [[Metaschedule] Aligning get_top_k logic in MemoryDatabase and JSONDatabase](https://github.com/apache/tvm/pull/13611)  
- [[MetaSchedule] preseve global_symbol attached to function after applying MS](https://github.com/apache/tvm/pull/14219)  
- [[MetaSchedule] Fix a typo in MemoryDatabase](https://github.com/apache/tvm/pull/13928)  
- [[MetaSchedule] Fix for RewriteLayout + AllocateConst when the rank of the rewritten weight doesn't change](https://github.com/apache/tvm/pull/13851)  
- [[MetaSchedule] Fix tensorcore winograd task extraction](https://github.com/apache/tvm/pull/13625)  
- [[HotFix][MetaSchedule] Turn off database shash check](https://github.com/apache/tvm/pull/14188)  
- [[MetaSchedule] MutateTileSize skip single-candidate SampleCategorical](https://github.com/apache/tvm/pull/14072)  
- [[Metaschedule] EvolutionarySearchNode::State constructor typo fix](https://github.com/apache/tvm/pull/14002)  
- [[Fix][MetaSchedule] Fix redundant stages in async pipeline for mlt](https://github.com/apache/tvm/pull/14143)  
- [[Fix][MetaSchedule] RPCRunner timeout when queueing up](https://github.com/apache/tvm/pull/13963)  
- [[MetaSchedule] Add pass instrument to MetaSchedule api](https://github.com/apache/tvm/pull/13688)  
- [[MetaSchedule] Tile and pack intermediate output for CUDA TensorCore](https://github.com/apache/tvm/pull/14108)  
- [[MeteSchedule] Bugfix: Add checks for nullable `run_secs`](https://github.com/apache/tvm/pull/13790)  

# Misc

- [[UX] Make T.prim_func typecheck as staticmethod](https://github.com/apache/tvm/pull/13980)  
- [[VM][DMLC] Lower memory usage when loading and dumping weights](https://github.com/apache/tvm/pull/13877)  
- [[APP] Update android_rpc build tools version](https://github.com/apache/tvm/pull/14052)  
- [[apps][bundle_deploy]Fix bundle build issue](https://github.com/apache/tvm/pull/14315)  
- [[Diagnostic] Support constructing Diagnostic Error through ObjectRef](https://github.com/apache/tvm/pull/13977)  
- [[skip ci] Replace magic_wand model with micro_speech](https://github.com/apache/tvm/pull/14414)  
- [[IR] Enhance IRModule SEqual/SHash to support cross function calls](https://github.com/apache/tvm/pull/14289)  
- [[Fix]Fix function ObjectPath in IRModule SEqual](https://github.com/apache/tvm/pull/14230)  
- [Update to v0.12.dev0](https://github.com/apache/tvm/pull/14241)  
- [Enable C++17 for cmake modules](https://github.com/apache/tvm/pull/13869)  
- [Remove temporary VTCM workspace APIs](https://github.com/apache/tvm/pull/13681)  
- [[IR] Platform-independent SHash](https://github.com/apache/tvm/pull/14204)  
- [Fix numpy version constraint](https://github.com/apache/tvm/pull/13912)  
- [[Utils] Allow classmethod and staticmethod in TVMDerivedObject](https://github.com/apache/tvm/pull/14249)  
- [[Git] Ignore python/requirements directory](https://github.com/apache/tvm/pull/13684)  
- [Enhance the --help message of composite target](https://github.com/apache/tvm/pull/13842)  
- [Add support for named outputs in MLF archive](https://github.com/apache/tvm/pull/13704)  
- [Add Name Transforms for Rust style](https://github.com/apache/tvm/pull/13706)  
- [Refactor test to make it easier for user to understand how tensor_intrin works](https://github.com/apache/tvm/pull/14017)  
- [Remove tutorials CMSIS dependency when not needed](https://github.com/apache/tvm/pull/13762)  
- [Add DisallowAsyncStridedMemCopy post processor to rem](https://github.com/apache/tvm/pull/13720)  
- [Add check for non-contiguous memory access when lowering to async dma](https://github.com/apache/tvm/pull/13613)  
- [Relay transform for rolling a known pattern into batch_matmul](https://github.com/apache/tvm/pull/14210)  
- [[Typo] Fix name of iter var type 4](https://github.com/apache/tvm/pull/14436)  
- [Extend the USE_LIBBACKTRACE option](https://github.com/apache/tvm/pull/13816)  
- [[Refactor] Move `VarUseDefAnalysis` to header file](https://github.com/apache/tvm/pull/14185)  
- [Add header files for GraphExecutorDebug](https://github.com/apache/tvm/pull/13694)  
- [[pytest] Don't return values from test_* functions](https://github.com/apache/tvm/pull/14475)  
- [[Analysis] Improve error message in VerifyWellFormed](https://github.com/apache/tvm/pull/14389)  
- [Revert the changes for NNPACK build issue](https://github.com/apache/tvm/pull/13913)  
- [[Node] Utility methods for ObjectPathPair handling](https://github.com/apache/tvm/pull/14498)  
- [[Minor] Change file mode 755 -> 644; EOL CRLF -> LF](https://github.com/apache/tvm/pull/13959)  
- [[FIX] Minor Compilation Warning Fixes](https://github.com/apache/tvm/pull/13794)  
- [[Contrib][Sort] Faster Top-K Implementation](https://github.com/apache/tvm/pull/13599)  
- [[COLLAGE] Add more customization to support more targets](https://github.com/apache/tvm/pull/13450)  
- [[CONTAINER] Struct Hash/Equal and JSON support for ShapeTuple](https://github.com/apache/tvm/pull/13671)  
- [[VTA] Provide zero-initialization for VTAGenericInsn](https://github.com/apache/tvm/pull/13698)  
- [[Fix,Roofline] Fix roofline handling of multiple peak flops](https://github.com/apache/tvm/pull/13716)  
- [[RPC] Add fail-guard for termination time exception](https://github.com/apache/tvm/pull/13651)  
- [[TOPHUB] use keys as a keyword for searching of existing statistics](https://github.com/apache/tvm/pull/13874)  
- [[Transform] Use callable() instead of isinstance() for type checking](https://github.com/apache/tvm/pull/14248)  
- [[TRANSFORM] Fix virtual device annotation issue with BYOC subgraphs](https://github.com/apache/tvm/pull/13325)  

# Relay

- [[Fix][Relay] Fix axis transformation in squeeze shape function](https://github.com/apache/tvm/pull/14135)  
- [[QNN][Relay][Topi] Add qnn.dense with weight layout](https://github.com/apache/tvm/pull/13854)  
- [[fix][relay][qnn] Bug fix for 8-bit quantized mul](https://github.com/apache/tvm/pull/14286)  
- [[Relay][Op] Connect existing arm_cpu schedule to relay strategy for concat](https://github.com/apache/tvm/pull/14270)  
- [[Relay] Convert negative axes to positive when importing ONNX Unsqueeze](https://github.com/apache/tvm/pull/13846)  
- [[Relay][Frontend] Span Filling PyTorch](https://github.com/apache/tvm/pull/14050)  
- [[Relay][Frontend] Span Filling ONNX](https://github.com/apache/tvm/pull/13767)  
- [[Relay][Frontend] Span Filling TensorFlow 1](https://github.com/apache/tvm/pull/13728)  
- [[Relay][Frontend] Span Filling TFLite](https://github.com/apache/tvm/pull/13727)  
- [[Relay][Frontend] Span filling common API](https://github.com/apache/tvm/pull/13402)  
- [[Relay][Pass] Separate out the graph partitioning code from fuse_ops.cc](https://github.com/apache/tvm/pull/13964)  
- [[Relay] Remove overwriting of matmul shapes when they are static](https://github.com/apache/tvm/pull/13615)  
- [[Relay][Frontend][Onnx] SequenceAt and SplitToSequence Operators](https://github.com/apache/tvm/pull/13602)  
- [[Relay] Move pad value extraction past null pointer check](https://github.com/apache/tvm/pull/14445)  
- [[relay][frontend][pytorch]Fix a bug in the _get_pytorch_value_type function](https://github.com/apache/tvm/pull/14421)  
- [[Relay] Enhance EliminateCommonSubexpr to support Tuple argument](https://github.com/apache/tvm/pull/14169)  
- [[Relay][TIR] Add utility to lower Relay func to TIR prim func](https://github.com/apache/tvm/pull/13606)  
- ["[Relay] Check if the attribute ""name"" exists before accessing it"](https://github.com/apache/tvm/pull/14485)  
- [[Relay][Docs] Fixed examples in relay/transform.py documentation](https://github.com/apache/tvm/pull/13682)  
- [[Relay][Runtime] Add `set_input/output_zero_copy` in python](https://github.com/apache/tvm/pull/13623)  
- [[Relay][Testing][Bugfix] `py_converter` should use correct AST for versions above 3.8 too](https://github.com/apache/tvm/pull/13635)  
- [[relay] preserve the order of input_info of pytorch](https://github.com/apache/tvm/pull/14462)  
- [[QNN] Change in Pass Context for lookup table calculation](https://github.com/apache/tvm/pull/13660)  
- [[QNN] Convert fake quantized take to quantized op](https://github.com/apache/tvm/pull/14506)  

# Schedule
- [[Schedule][Bugfix] Fix decompose padding wrt the single child subtree](https://github.com/apache/tvm/pull/13646)  
- [[Schedule] Add an optional argument `disable_checks` for `Schedule`](https://github.com/apache/tvm/pull/14281)  

# Target
- ["[Target] Make `key=arm_cpu` --> `key=arm_cpu](https://github.com/apache/tvm/pull/13775)  
- [[Target] Add target tags for Apple Silicon GPU](https://github.com/apache/tvm/pull/14068)  
- [[Target] Fix Jetson AGX Xavier CPU core count](https://github.com/apache/tvm/pull/14508)  
- [[Target] Add A10G gpu cuda tag](https://github.com/apache/tvm/pull/14467)  

# TE
- [[TE] Record primitives of Schedule for visualization](https://github.com/apache/tvm/pull/14168)  
- [[TE][PrimFunc] Fix create primfunc from te extern with explicit buffer load](https://github.com/apache/tvm/pull/13729)  

# Tensorize
- [[Tensorize][runtime] Add support for AMX(Advanced Matrix Extensions) through Tensor intrinsics](https://github.com/apache/tvm/pull/13642)  
- [[Tensorize][TOPI] Add AMX Tensorizing for int8 batch matmul](https://github.com/apache/tvm/pull/13745)  

# TIR
- [[TensorIR] Support for L2 prefetch async copy and pred_guard enabled async in vectorized if_then_else](https://github.com/apache/tvm/pull/14329)  
- [[TensorIR][Schedule] New primitive `reorder_block_itervar`](https://github.com/apache/tvm/pull/14448)  
- [[TensorIR] New schedule primitive `set_dtype`](https://github.com/apache/tvm/pull/14316) 
- [[Fix][TIR] LowerCrossThreadReduction with write-back predicate](https://github.com/apache/tvm/pull/14199)  
- [[TIR] Introduce Pass InjectPTXLDG32](https://github.com/apache/tvm/pull/13973)  
- [[Fix][TIR] Fix tvm::arith::UnionLowerBound](https://github.com/apache/tvm/pull/14304)  
- [[TIR][Schedule] Add unittest for read_write_at](https://github.com/apache/tvm/pull/14395)  
- [[TIR] Add cp.async support for tir.if_then_else](https://github.com/apache/tvm/pull/13966)  
- [[tir] fix buffer_decl buffer allocation](https://github.com/apache/tvm/pull/13906)  
- [[tir] Add line level debug info](https://github.com/apache/tvm/pull/13012)  
- [[TIR][FIX] check args size when creating prim_func by runtime::Registry](https://github.com/apache/tvm/pull/13809)  
- [[TIR] not estimating the flops when there is a default estimated flops as attr](https://github.com/apache/tvm/pull/14379)  
- [[TIR][Hexagon] Enhancement of NarrowDataType pass for binary ops](https://github.com/apache/tvm/pull/14298)  
- [[TIR] Handle nullptr returned by FindEntryFunc](https://github.com/apache/tvm/pull/13852)  
- [[TIR]Fix the crash of the pass RemoveNoOp](https://github.com/apache/tvm/pull/13808)  
- [[TIR] Update SplitHostDevice to post-process with ConvertSSA](https://github.com/apache/tvm/pull/14496)  
- [[TIR][Utility] More flexible tir::Substitute arguments](https://github.com/apache/tvm/pull/14251)  
- [[TIR][Analysis] Implement IdentifyMemCpy analysis function](https://github.com/apache/tvm/pull/13947)  
- [[TIR] Merged kDeviceThreadAxis and kUseDynamicSharedMemoryTag](https://github.com/apache/tvm/pull/14495)  
- [[TIR] Improved SeqStmt::Flatten utility](https://github.com/apache/tvm/pull/14497)  
- [[TIR] Use IRModuleNode::Remove to remove None in PrimFuncPass](https://github.com/apache/tvm/pull/14494)  
- [[TIR] Use same DataType of builtin::tvm_struct_set in C++ and Python](https://github.com/apache/tvm/pull/14489)  
- [[TIR] Update LowerTVMBuiltin to use Optional<T>](https://github.com/apache/tvm/pull/14400)  
- [[TIR] Improved MakePackedAPI error message](https://github.com/apache/tvm/pull/14387)  
- [[TIR] Legalize dtype of constants in IndexMap](https://github.com/apache/tvm/pull/14385)  
- [[TIR] Improved error message in InjectSoftwarePipeline](https://github.com/apache/tvm/pull/14391)  
- [[TIR][Schedule] Allow buffer name argument to Schedule.set_scope](https://github.com/apache/tvm/pull/14327)  
- [[TIR] Fix dtype mismatch error due to LetStmt](https://github.com/apache/tvm/pull/13710)  
- [[Fix][TIR] SampleCategorical apply-to-schedule](https://github.com/apache/tvm/pull/14133)  
- [[TIR][Fix] IndexDataTypeNormalizer not unwrapping float casting](https://github.com/apache/tvm/pull/13789)  
- [[TIR][Fix] Buffer slicing using index dtype as extent](https://github.com/apache/tvm/pull/13788)  
- [[TIR] Create Layout with specified axis dtype](https://github.com/apache/tvm/pull/13663)  
- [[TIR][Schedule] Improve cache_index to cache common subexpressions](https://github.com/apache/tvm/pull/13700)  
- [[TIR][Arith] Add common sub expr analyzer](https://github.com/apache/tvm/pull/13702)  
- [[TIR] [Schedule] Add get_output_blocks primitive](https://github.com/apache/tvm/pull/14490)  
- [[TIR] [Analysis] Expose IsOutputBlock to python](https://github.com/apache/tvm/pull/14352)  
- [[TIR] [Bugfix] Pass the correct block_sref_reuse to Replace](https://github.com/apache/tvm/pull/14023)  
- [[TIR] Fix cache_write bug with allocate const node](https://github.com/apache/tvm/pull/13792)  
- [[TIR][Schedule] Fix reverse_compute_inline](https://github.com/apache/tvm/pull/14263)  
- [[TIR] Remove special-casing of T.address_of in the storage rewrite pass](https://github.com/apache/tvm/pull/14430)  
- [[TIR] Refactor BF16Legalize](https://github.com/apache/tvm/pull/14405)  
- [[TIR] Enhance loop unroll with unroll local access](https://github.com/apache/tvm/pull/14224)  
- [[TIR] Remove LoadNode and StoreNode](https://github.com/apache/tvm/pull/14381)  
- [[TIR] Allow TransformLayout index_map to contain RVs](https://github.com/apache/tvm/pull/13930)  
- [[TIR] Allow TransformLayout with non-inversible index map](https://github.com/apache/tvm/pull/14095)  
- [[TIR] Fix typo in doc](https://github.com/apache/tvm/pull/14178)  
- [[TIR] Update block flags and simplify predicate in Reverse-Compute-Inline](https://github.com/apache/tvm/pull/14030)  
- [[TIR][TOPI][x86][CI] Support skylake avx512](https://github.com/apache/tvm/pull/13621)  
- [[TIR][TOPI][CI] Fix number of arguments in calls of llvm_pure_intrin](https://github.com/apache/tvm/pull/13881)  
- [[TIR][Compute-at] Utilize InverseAffineIterMap for dom estimation](https://github.com/apache/tvm/pull/14184)  
- [[TIR] Expose bitwise ops to python](https://github.com/apache/tvm/pull/13945)  
- [[TIR] Add merge primitive for TIR schedule](https://github.com/apache/tvm/pull/14398)  
- [[TensorIR][Primitive] New schedule primitive `reindex_cache_read/write`](https://github.com/apache/tvm/pull/14161)  
- [[TIR] Fix Datatype in Lower TVM Builtin](https://github.com/apache/tvm/pull/14347)  
- [[TIR] Enable Host Func Attribute for PrimFunc](https://github.com/apache/tvm/pull/14020)  

# TOPI
- [[FIX][TOPI] Clip with IntImm/FloatImm](https://github.com/apache/tvm/pull/14027)  
- [[Fix,TOPI] Consolidate generic and x86 scatter nd](https://github.com/apache/tvm/pull/13755)  
- [[Test][Topi] Avoid depending on f32 rounding behavior for crop_and_divide tests](https://github.com/apache/tvm/pull/13773)  
- [[TOPI] Expose mem_scope from generic conv2d variants to be more reusable](https://github.com/apache/tvm/pull/13680)  
- [[TOPI][bugfix] Fix a bug in arm_cpu int8 dotprod schedule and modernize tests](https://github.com/apache/tvm/pull/13669)  
- [[TOPI] Bugfix arm_cpu schedule_conv2d_spatial_pack_nhwc schedule](https://github.com/apache/tvm/pull/14003)  
- [[TOPI][OP] Support grouped conv2d_NCHWc](https://github.com/apache/tvm/pull/13733)  
- [[TOPI] Fix batch_matmul tensorcore legalize for transpose_b = False case](https://github.com/apache/tvm/pull/13618)  
- [[TOPI] Group normalization](https://github.com/apache/tvm/pull/14193)  
- [[TOPI] dynamic externsion](https://github.com/apache/tvm/pull/14450)  
- [[TOPI] Fix tuple unpack in conv2d NCHWc int8](https://github.com/apache/tvm/pull/13761)  
- [[TOPI] Making test_strided_set require a GPU for testing](https://github.com/apache/tvm/pull/13804)  
- [[Fix][Relay][TOPI] Bug fix in relay.sum and topi.sum functions](https://github.com/apache/tvm/pull/14285)  
- ["[TOPI][Fix] Pool must return error if layout is tiled on H](https://github.com/apache/tvm/pull/13975)  
- [[TOPI] Batch Norm Training Mode](https://github.com/apache/tvm/pull/14190)  
- [[topi] remove comment redundancy in resize.py](https://github.com/apache/tvm/pull/13860)  
- [[TOPI][Hexagon] Implement global_avg_pool2d for hexagon](https://github.com/apache/tvm/pull/13614)  
- [[TOPI] Support non-batch cases for topi.nll_loss](https://github.com/apache/tvm/pull/14060)  
- [[TOPI] Add instance_norm operator](https://github.com/apache/tvm/pull/14410)  
- [[TOPI] Support symbolic shape in einsum](https://github.com/apache/tvm/pull/14521)  
- ["[TOPI][Relay][ONNX] Replace scatter_add by scatter_elements(reduction=""add"")"](https://github.com/apache/tvm/pull/14008)  
- [[TOPI] Fix data race of batch multibox detection](https://github.com/apache/tvm/pull/14343)  
- [[TOPI] Fix index dtype in topi strided_slice](https://github.com/apache/tvm/pull/14022)  
- [[TORCH][TOPI] Support mean reduction for scatter_reduce](https://github.com/apache/tvm/pull/14110)  

# TVMC
- [[TVMC] Fix logging in TVMC](https://github.com/apache/tvm/pull/14175)  
- [[TVMC] Stop printing a wall of warnings with tvmc tune](https://github.com/apache/tvm/pull/13882)  
- [[TVMC] Add option to dump TIR code to file](https://github.com/apache/tvm/pull/14186)  
- [[TVMC] Allow selecting a subset of tasks to be used in `tvmc tune`](https://github.com/apache/tvm/pull/12525)  
- [[TVMC] Improve --desired-layouts functionality](https://github.com/apache/tvm/pull/14272)  
- [[TVMC][microNPU] tvmc option for printing which operators are offloaded to Ethos-U](https://github.com/apache/tvm/pull/13212)  
- [[TVMC][TRANSFORMS] ToMixedPrecision transform support with custom options enabled](https://github.com/apache/tvm/pull/14010)  
# TVMScript
- [[Fix][TVMScript]TVMScript BinOP printing refactor](https://github.com/apache/tvm/pull/14200)  
- [[TVMScript] Schedule error reporting with new TVMScript printer](https://github.com/apache/tvm/pull/13921)  
- [[TVMScript] Connect `assert_structural_equal` with new TVMScript printer](https://github.com/apache/tvm/pull/13859)  
- [[TVMScript] Comments and docstrings printing](https://github.com/apache/tvm/pull/13839)  
- [[TVMScript] `T.allocate` with `T.decl_buffer` syntax sugar for TVMScript printer](https://github.com/apache/tvm/pull/13813)  
- [[TVMScript] `T.match_buffer` syntax sugar in arguments for TVMScript printer](https://github.com/apache/tvm/pull/13801)  
- [[TVMScript] Linter-friendly function definitions](https://github.com/apache/tvm/pull/13713)  
- [[TVMScript][Fix] Fix `bool` printing for roundtrip](https://github.com/apache/tvm/pull/14390)  
- [[Fix][TVMScript] Fix `LetStmt` printing logic](https://github.com/apache/tvm/pull/13900)  
- [[TVMScript] More concise `T.allocate` syntax printing](https://github.com/apache/tvm/pull/13830)  
- [[TVMScript] Implicit root block syntax sugar for TVMScript printer](https://github.com/apache/tvm/pull/13819)  
- [[TVMScript] `T.axis.remap` syntax sugar for TVMScript printer](https://github.com/apache/tvm/pull/13743)  
- [[TVMScript] Robustify the Highlight Printer](https://github.com/apache/tvm/pull/13861)  
- [[TVMScript] Sugar Var Definition in TIR Buffer](https://github.com/apache/tvm/pull/14223)  
- [[TVMScript] Distinguish LetStmt and Let expression](https://github.com/apache/tvm/pull/14207)  
- [[TVMScript] Simplify TIR Var Definition](https://github.com/apache/tvm/pull/13970)  
- [[TVMScript][UX] Introduce decorator for deprecation](https://github.com/apache/tvm/pull/13941)  
- [[TVMScript] Support `show_meta`](https://github.com/apache/tvm/pull/13934)  
- [[TVMScript] Consolidate folder structure](https://github.com/apache/tvm/pull/13841)  
- [[TVMScript] Default to T.Buffer than T.buffer_decl](https://github.com/apache/tvm/pull/13838)  
- [[TVMScript] Introduce `PrinterConfig`](https://github.com/apache/tvm/pull/13831)  
- [[TVMScript] Add ObjectPath to LiteralDoc](https://github.com/apache/tvm/pull/13821)  
- [[TVMScript] Use TVMScript for all TIR Printing](https://github.com/apache/tvm/pull/13795)  
- [[TVMScript] Migrate More to TVMScripr Printer](https://github.com/apache/tvm/pull/13785)  
- [[TVMScript] IR Fragment Printing](https://github.com/apache/tvm/pull/13742)  
- [[TVMScript] Refactor IRDocsifier](https://github.com/apache/tvm/pull/13593)  
- [[TVMScript] Remove obsolete modules](https://github.com/apache/tvm/pull/13638)  
- [[TVMScript] Support SizeVar Roundtripping](https://github.com/apache/tvm/pull/14227)  
- [[TVMScript] Sugar T.env_thread + T.launch_thread](https://github.com/apache/tvm/pull/14217)  
- [[TVMScript] Encourage using T.Buffer directly](https://github.com/apache/tvm/pull/13971)  
- [[TVMScript] Unify `T.handle` and `T.Ptr`](https://github.com/apache/tvm/pull/13969)  
- [[TVMScript] Enable Safe Autocasting in BufferStore](https://github.com/apache/tvm/pull/13960)  
- [[TVMScript] Deterministic function ordering](https://github.com/apache/tvm/pull/13962)  
- [[TVMScript][Fix] Print Multi-line String as Metadata](https://github.com/apache/tvm/pull/13965)  
- [[TVMScript] Use op attribute to control whether to print dtype in TVMScript](https://github.com/apache/tvm/pull/14111)  
- [[TVMScript] Upstream IRModule parser from unity](https://github.com/apache/tvm/pull/14487)  
- [[TVMScript] Upstream IRModule parser from unity](https://github.com/apache/tvm/pull/14487)  
- [[TVMScript] Upstream IRModule parser from unity](https://github.com/apache/tvm/pull/14487)  
- [[TVMScript] Improved error message for unexpected top frame](https://github.com/apache/tvm/pull/14399)  
- [[TVMScript] Use new variable frame in If/Then/Else](https://github.com/apache/tvm/pull/14250)  
- [[Bugfix][TVMScript] Preserve variable names in LetStmt](https://github.com/apache/tvm/pull/14319)  
- [[TVMScript] More accurate hints for ImportError](https://github.com/apache/tvm/pull/13662)  
- [[TVMScript,Fix] Fix findsource when classes are indented](https://github.com/apache/tvm/pull/13924)  
- [[TVMScript][Printer] Remove relax prefix for now](https://github.com/apache/tvm/pull/14140)  
- [[Fix][TVMScript] Fix index of metadata in printed script](https://github.com/apache/tvm/pull/14130)  
- [[TVMScript] Fix print round-tripable multi thread env binding](https://github.com/apache/tvm/pull/13622)  
- [[TVMScript][Parser] Add more warp-level builtins and `Range`](https://github.com/apache/tvm/pull/14279)  


## v0.13.0 (2023-07-14)

# Introduction

The TVM community has worked since the v0.12.0 release to deliver the following new exciting improvements! The main tags are below (**bold text is with lots of progress**):

- Community, RFC;
- Frontend: TensorFlow/TFLite, Pytorch/Torch, Paddle, keras;
- Runtime: Adreno, OpenCL & CLML, ROCm, CUDA & CUTLASS & TensorRT, Ethosn, Vulkan, Hexagon, Metal, others about runtime;
- Relay, BYOC, TOPI, Arith, **TIR, TVMScript, MetaSchedule**;
- microTVM, AOT, TVMC, LLVM;
- CI, BugFix, Docs, Docker, Miscs;

Please visit the full listing of commits for a complete view: [v0.12.0...v0.13.0](https://github.com/apache/tvm/compare/v0.12.0...v0.13.0).

### Community
 * [#15086](https://github.com/apache/tvm/pull/15086) - Aleksei-grovety -> Reviewer
 * [#14676](https://github.com/apache/tvm/pull/14676) - Jiajun Jiang -> Reviewer
 * [#14677](https://github.com/apache/tvm/pull/14677) - Qiang Zhang -> Reviewer
 * [#14622](https://github.com/apache/tvm/pull/14622) - Sunghyun Park -> Reviewer
 * [#14578](https://github.com/apache/tvm/pull/14578) - Zihao Ye -> Committer
 * [#14853](https://github.com/apache/tvm/pull/14853) - Anirudh Sundar Subramaniam -> Committer
 * [#14772](https://github.com/apache/tvm/pull/14772) - Add new key for release signing

### RFC

 * https://github.com/apache/tvm-rfcs/pull/100

----

### Frontend
 * [#14830](https://github.com/apache/tvm/pull/14830) - Use f-strings for string formatting, NFC
 * Keras
    * [#15122](https://github.com/apache/tvm/pull/15122) - [Relay][Keras] Fix SeparableConv2D conversion in dilation_rate attribute
    * [#15107](https://github.com/apache/tvm/pull/15107) - [Relay][Keras] Fix a wrong variable name in keras frontend
    * [#15053](https://github.com/apache/tvm/pull/15053) - [Relay][Keras] Fix the wrong implementation logic about cropping2D
    * [#15082](https://github.com/apache/tvm/pull/15082) - [Relay][Keras] Fix UpSampling2D about the wrong assertion about size
    * [#15060](https://github.com/apache/tvm/pull/15060) - [Relay][keras] Fix the bug about the attribute 'output_padding' in Deconv
    * [#14707](https://github.com/apache/tvm/pull/14707) - [Keras]fix a bug about alpha attribute in LeakyReLU which lead to passes conflict
    * [#15175](https://github.com/apache/tvm/pull/15175) - [Relay][Keras] Fix concatenate convert function in axis parsing
 * Paddle
    * [#14801](https://github.com/apache/tvm/pull/14801) - [Paddle] [PaddlePaddle Hackathon 4]add attribute support for gaussian_random/softplus/Conv3d/Conv2d
    * [#14973](https://github.com/apache/tvm/pull/14973) - [Paddle] [PaddlePaddle Hackathon 4] add convert support for tanhshrink/pool3d/set_value ops for paddle frontend
    * [#14826](https://github.com/apache/tvm/pull/14826) - [Paddle] [PaddlePaddle Hackathon 4] add convert support for p_norm/roi_align/softmax_with_cross_entropy
    * [#14575](https://github.com/apache/tvm/pull/14575) - [Paddle] [PaddlePaddle Hackathon 4]add attribute support for dropout/hard_sigmoid/pixel_shuffle
 * TFLite
    * [#14667](https://github.com/apache/tvm/pull/14667) - [TFLite]Support for quantized squared difference
    * [#14819](https://github.com/apache/tvm/pull/14819) - [TFLite]Generate name when tensor name is missing
    * [#15173](https://github.com/apache/tvm/pull/15173) - [FRONTEND][TFLITE]Fix int16 transpose conv loading
 * TensorFlow
    * [#14546](https://github.com/apache/tvm/pull/14546) - [Tensorflow] Fix conv2d_transpose for NHWC layout
 * PyTorch
    * [#14747](https://github.com/apache/tvm/pull/14747) - [PyTorch]  Add aten::new_zeros
    * [#14699](https://github.com/apache/tvm/pull/14699) - [Torch] fix typo in new_full
    * [#14963](https://github.com/apache/tvm/pull/14963) - [PyTorch] Support use_input_stats in instance_norm
    * [#14930](https://github.com/apache/tvm/pull/14930) - Fix pytorch axis
 * ONNX
    * [#15017](https://github.com/apache/tvm/pull/15017) - [ONNX] Fix bug in scatter_elements

### Runtime
 * [#15182](https://github.com/apache/tvm/pull/15182) - Add weak symbol to builtin fp16
 * [#15161](https://github.com/apache/tvm/pull/15161) - Clean TVM stacktrace in error messages
 * [#15162](https://github.com/apache/tvm/pull/15162) - Support void as dtype in FFI
 * [#14902](https://github.com/apache/tvm/pull/14902) - Update Module and Registry to use String Container
 * [#14967](https://github.com/apache/tvm/pull/14967) - [Runtime,RPC] Use f-strings for string formatting, NFC
 * [#14887](https://github.com/apache/tvm/pull/14887) - Make systemlib unique per prefix
 * [#14775](https://github.com/apache/tvm/pull/14775) - Added __str__ for tvm._ffi.runtime_ctypes.TVMArray
 * [#14656](https://github.com/apache/tvm/pull/14656) - Fix Can't "query_imports" Bug of VM Executable

### Adreno
 * [#15061](https://github.com/apache/tvm/pull/15061) - [TOPI]Fix problem with ceil_log2
 * [#14996](https://github.com/apache/tvm/pull/14996) - [OpenCL]Fix conv2d when output channels < 4

### CMSIS-NN
 * [#15059](https://github.com/apache/tvm/pull/15059) - Update CMSIS-NN release to v4.1.0

### OpenCL & CLML
 * [#14972](https://github.com/apache/tvm/pull/14972) - [OPENCL] Always use convert_T for type conversion
 * [#14995](https://github.com/apache/tvm/pull/14995) - [OpenCL] Improve diagnostic message
 * [#14833](https://github.com/apache/tvm/pull/14833) - [Codegen][OpenCL] fix amibiguous selection operator call
 * [#14792](https://github.com/apache/tvm/pull/14792) - [OpenCL] Refactor OpenCL runtime to support SPIRV binary ingestion
 * [#14922](https://github.com/apache/tvm/pull/14922) - [OpenCLML] Reactor and introduce on chip memory and memory planner
 * [#14949](https://github.com/apache/tvm/pull/14949) - [CodegenC] Updated unit test for sorted CodegenC output
 * [#14767](https://github.com/apache/tvm/pull/14767) - [OpenCLML] Transposed convolution support and other fixes

### cuda & cutlass & tensorrt
 * [#14751](https://github.com/apache/tvm/pull/14751) - [CUDA] Fixed the call of the min function in the schedule for cuda
 * [#14798](https://github.com/apache/tvm/pull/14798) - [CUTLASS] Add NDEBUG option to CUTLASS compile to speed up attention kernel
 * [#14782](https://github.com/apache/tvm/pull/14782) - [Bugfix][Codegen][CUDA] Wrong casting in ASM

### metal
 * [#14962](https://github.com/apache/tvm/pull/14962) - Fix int8 vectorized cast
 * [#14846](https://github.com/apache/tvm/pull/14846) - Fix vectorized select
 * [#14727](https://github.com/apache/tvm/pull/14727) - Update metal runtime to directly store kernel map
 * [#14671](https://github.com/apache/tvm/pull/14671) - Fix flaky memory issue due to racing

### Vulkan
 * [#15035](https://github.com/apache/tvm/pull/15035) - [Vulkan] Allow DeclBuffer in CodeGenSPIRV
 * [#14817](https://github.com/apache/tvm/pull/14817) - [Vulkan] Add cooperative matrix support

### Hexagon
 * [#14997](https://github.com/apache/tvm/pull/14997) - Remove "c" as aot_host_target tvm/contrib/hexagon/pytest_pl…
 * [#14948](https://github.com/apache/tvm/pull/14948) - Update instructions to compile hexagon runtime
 * [#14965](https://github.com/apache/tvm/pull/14965) - Add support for v73, make v68 default
 * [#14720](https://github.com/apache/tvm/pull/14720) - [TIR] Add get_vtcm_allocation_sizes with lowering
 * [#14567](https://github.com/apache/tvm/pull/14567) - [TIR] Use the "target" value in T.func_attr for VTCM limit

### ROCm
 * [#15106](https://github.com/apache/tvm/pull/15106) - [TensorIR]AMD Matrix Core Support
 * [#15088](https://github.com/apache/tvm/pull/15088) - [Target]Replace rocm arch parsing from int to string

### microTVM
 * [#14872](https://github.com/apache/tvm/pull/14872) - Use self.close_transport() on error

### AOT
 * [#15033](https://github.com/apache/tvm/pull/15033) - Avoid Var-to-Var Let binding in AOTExecutorCodegen
 * [#15032](https://github.com/apache/tvm/pull/15032) - Remove duplication in tvm.testing.aot.compile_models
 * [#14529](https://github.com/apache/tvm/pull/14529) - Fix warning on dropping const in TVMAotExecutor_GetInputName

### micoNPU
 * [#15159](https://github.com/apache/tvm/pull/15159) - [microNPU][ETHOSU] Fix compiler attributes types
 * [#15147](https://github.com/apache/tvm/pull/15147) - [microNPU][ETHOSU] Add option to disable copying constants for case without cascader
 * [#15069](https://github.com/apache/tvm/pull/15069) - [microNPU][ETHOSU] Fix SoftMax legalization parameters
 * [#15115](https://github.com/apache/tvm/pull/15115) - [microNPU][ETHOSU] Upgrade to 23.05 version of Arm(R) Ethos(TM)-U NPU drivers
 * [#15114](https://github.com/apache/tvm/pull/15114) - [microNPU] Upgrade Vela to v3.8.0
 * [#15104](https://github.com/apache/tvm/pull/15104) - [microNPU][ETHOSU] Fix minimum buffer size
 * [#15063](https://github.com/apache/tvm/pull/15063) - [microNPU][ETHOSU] Fix CopyComputeReordering pass arguments
 * [#14861](https://github.com/apache/tvm/pull/14861) - [microNPU][ETHOSU] Add offloading to the NPU the nn.avg_pool2d operator with a stride > 3
 * [#14765](https://github.com/apache/tvm/pull/14765) - [microNPU][ETHOSU] Channel pad offloaded to NPU
 * [#14774](https://github.com/apache/tvm/pull/14774) - [microNPU][ETHOSU] Fix Softmax quantization parameters
 * [#14629](https://github.com/apache/tvm/pull/14629) - [microNPU][ETHOSU] Softmax int8 legalization support
 * [#14353](https://github.com/apache/tvm/pull/14353) - [microNPU] Add support for MEAN with uint8 ifm
 * [#14587](https://github.com/apache/tvm/pull/14587) - [microNPU] Fix skip tests when Vela is not present
 * [#14464](https://github.com/apache/tvm/pull/14464) - [microNPU][ETHOSU] Add restrictions to convert to NHCWB16 layout in LayoutOptimization pass

### BYOC
 * [#15046](https://github.com/apache/tvm/pull/15046) - Add GEMM kernel from FasterTransformer as submodule
 * [#15029](https://github.com/apache/tvm/pull/15029) - Hide internal cutlass symbols

### Relay
 * [#15068](https://github.com/apache/tvm/pull/15068) - Improve the "clip" op optimization in simplify expr pass
 * [#14925](https://github.com/apache/tvm/pull/14925) - add a dimension check to reject invalid input
 * [#14858](https://github.com/apache/tvm/pull/14858) - [simplify_expr]: Add pass to remove trivial transpose ops
 * [#14838](https://github.com/apache/tvm/pull/14838) - Use f-strings for string formatting, NFC
 * [#14831](https://github.com/apache/tvm/pull/14831) - [Relay/Op] Use f-strings for string formatting, NFC
 * [#14580](https://github.com/apache/tvm/pull/14580) - Simplify the square of a binomial
 * [#14735](https://github.com/apache/tvm/pull/14735) - Handle pad value coming from Tensor instead of scalar
 * [#14601](https://github.com/apache/tvm/pull/14601) - Enhance type infer for dynamic shape
 * [#14885](https://github.com/apache/tvm/pull/14885) - [Relay] fix broadcast in PyTorch frontend
 * [#15090](https://github.com/apache/tvm/pull/15090) - [Relay] Insertion of "device_copy" CallNode to Resolve Device Conflict on Unconstrained Nodes
 * [#14845](https://github.com/apache/tvm/pull/14845) - [Relay] Fix softplus in paddlepaddle frontend
 * [#14837](https://github.com/apache/tvm/pull/14837) - [Relay] Fix AdaptiveAvgPool2d about wrong dtype prasing
 * [#14821](https://github.com/apache/tvm/pull/14821) - [Relay] Fix softplus about the wrong calculation formula in Relay PyTorch frontend
 * [#14820](https://github.com/apache/tvm/pull/14820) - [Relay] Fix threshold calculation logic in PyTorch frontend
 * [#14824](https://github.com/apache/tvm/pull/14824) - [Relay] fix a bug about ReLu in the threshold attribute which causes a different results with keras
 * [#14796](https://github.com/apache/tvm/pull/14796) - [relay] fix wrong calculate logic about celu
 * [#14773](https://github.com/apache/tvm/pull/14773) - [Relay] fix `scatter_nd` type relation
 * [#14742](https://github.com/apache/tvm/pull/14742) - [relay] Fix alpha attribute with None in ELU
 * [#14740](https://github.com/apache/tvm/pull/14740) - [Relay] Fix stride in LpPool for default
 * [#14556](https://github.com/apache/tvm/pull/14556) - [Relay] fix a bug caused by IncompleteTypeNode in EinsumRel while doing MergeComposite
 * [#15057](https://github.com/apache/tvm/pull/15057) - [QNN] Implement quantized avg_pool2d
 * [#14536](https://github.com/apache/tvm/pull/14536) - [QNN] Implement 'qnn.softmax'
 * [#14875](https://github.com/apache/tvm/pull/14875) - [Quantization]: Update simulated_quantize to infer correct layout

### TOPI
 * [#15018](https://github.com/apache/tvm/pull/15018) - Fix dynamic dimensions support for Dense on TOPI side
 * [#14856](https://github.com/apache/tvm/pull/14856) - Fix in interpretation of empty axis parameter in reduction fun…
 * [#14483](https://github.com/apache/tvm/pull/14483) - [Target] Add SVE specific convolution
 * [#14839](https://github.com/apache/tvm/pull/14839) - Use f-strings for string formatting, NFC
 * [#14822](https://github.com/apache/tvm/pull/14822) - Use f-strings for string formatting, NFC
 * [#14519](https://github.com/apache/tvm/pull/14519) - Vectorize depthwise conv2d output operator
 * [#14549](https://github.com/apache/tvm/pull/14549) - remove the i32 cast for output shape of pool
 * [#14566](https://github.com/apache/tvm/pull/14566) - [Topi] Output strides in pack_buffer() utility

### Arith
 * [#15131](https://github.com/apache/tvm/pull/15131) - Hotfix flaky test in padded matmul
 * [#15120](https://github.com/apache/tvm/pull/15120) - NormalizeToIterSum
 * [#15081](https://github.com/apache/tvm/pull/15081) - Improve arith simplify to handle symbolic reshape pattern
 * [#14532](https://github.com/apache/tvm/pull/14532) - Implement statistics counters for RewriteSimplifier
 * [#14704](https://github.com/apache/tvm/pull/14704) - [cherry-pick][BUGFIX] Fix a bug of iter map floormod(x,2) simplify
 * [#14849](https://github.com/apache/tvm/pull/14849) - [TVMScript] Capture fails if var appears only in annotation
 * [#14596](https://github.com/apache/tvm/pull/14596) - [TensorIR] Improve CompactBufferRegion for symbolic shape
 * [#15129](https://github.com/apache/tvm/pull/15129) - [TIR] Recognize empty extents
 * [#14982](https://github.com/apache/tvm/pull/14982) - [TIR][VTA] Update host-side target, even without device func
 * [#14547](https://github.com/apache/tvm/pull/14547) - Enhance IterMapSimplify for symbolic
 * [#14571](https://github.com/apache/tvm/pull/14571) - [BUGFIX] Fix a bug of iter map floormod(x,2) simplify
 * [#14582](https://github.com/apache/tvm/pull/14582) - Fix solve inequality of unbound var ranges
 * [#14538](https://github.com/apache/tvm/pull/14538) - Enhance CanonicalSimplify to Simplify ProdDiv

### MetaSchedule
 * [#14781](https://github.com/apache/tvm/pull/14781) - [MetaSchedule] RPC port needs to be an integer
 * [#14673](https://github.com/apache/tvm/pull/14673) - Introduce MMA Tensor Core Multilevel Tiling
 * [#14784](https://github.com/apache/tvm/pull/14784) - Enhance `tune_tir` to tune IRModule of TIR Collections
 * [#14783](https://github.com/apache/tvm/pull/14783) - Add an API to dump a pruned database
 * [#14785](https://github.com/apache/tvm/pull/14785) - Clear screen only when specified
 * [#14654](https://github.com/apache/tvm/pull/14654) - Handle output cases for InlineConstantScalars
 * [#14642](https://github.com/apache/tvm/pull/14642) - PostProc not rewriting unroll for purely spatial block
 * [#14591](https://github.com/apache/tvm/pull/14591) - Handle cases when no features found by FeatureExtractor
 * [#14584](https://github.com/apache/tvm/pull/14584) - [ARM] Beautification of the function names

### TIR
 * [#15153](https://github.com/apache/tvm/pull/15153) - [TensorIR][Visitor] Visit buffer members in `match_buffer`'s in block visitor functions
 * [#15168](https://github.com/apache/tvm/pull/15168) - [Schedule] Support padding-by-factor in PadEinsum
 * [#15165](https://github.com/apache/tvm/pull/15165) - Expose UndefinedVars to Python
 * [#15163](https://github.com/apache/tvm/pull/15163) - Fix RenewDef for symbolic input shapes
 * [#15142](https://github.com/apache/tvm/pull/15142) - [Schedule] Enhance `compute-inline` for fusion
 * [#15150](https://github.com/apache/tvm/pull/15150) - Fix typo in code example
 * [#15144](https://github.com/apache/tvm/pull/15144) - [TensorIR][Schedule] New schedule primitive `unsafe_hide_buffer_access`
 * [#15146](https://github.com/apache/tvm/pull/15146) - Block dependence analysis without schedules
 * [#15119](https://github.com/apache/tvm/pull/15119) - Avoid duplicate GlobalVar names in SplitHostDevice
 * [#15037](https://github.com/apache/tvm/pull/15037) - Handle DeclBuffer in CacheReadWrite schedule primitive
 * [#15098](https://github.com/apache/tvm/pull/15098) - [Ethos-U]Handle DeclBuffer in Ethos-U inputs
 * [#15044](https://github.com/apache/tvm/pull/15044) - [USMP] Preserve DeclBuffer in PoolAllocationToOffsetConverter
 * [#15078](https://github.com/apache/tvm/pull/15078) - Handle DeclBuffer in LowerThreadAllreduce
 * [#15094](https://github.com/apache/tvm/pull/15094) - Handle DeclBuffer in MergeDynamicSharedMemoryAllocations
 * [#15093](https://github.com/apache/tvm/pull/15093) - Handle DeclBuffer in StorageAccessInfoLower
 * [#15045](https://github.com/apache/tvm/pull/15045) - Handle DeclBuffer in InjectDoubleBuffer
 * [#15096](https://github.com/apache/tvm/pull/15096) - Handle DeclBuffer in RemoveNoOp
 * [#15076](https://github.com/apache/tvm/pull/15076) - [CodeGen] Define PackedFunc error code in MakePackedAPI
 * [#15102](https://github.com/apache/tvm/pull/15102) - Update primfunc host attachment to include host
 * [#14854](https://github.com/apache/tvm/pull/14854) - [Compute-at] Enable complex floordiv/floormod expressions in compute_at
 * [#15041](https://github.com/apache/tvm/pull/15041) - Handle DeclBuffer in LowerCustomDatatypes
 * [#15038](https://github.com/apache/tvm/pull/15038) - Handle DeclBuffer in Inline/ComputeAt/ReverseComputeAt
 * [#15052](https://github.com/apache/tvm/pull/15052) - [Analysis] Handle DeclBuffer in FlopEstimator
 * [#15051](https://github.com/apache/tvm/pull/15051) - Handle DeclBuffer in StorageRewrite
 * [#15050](https://github.com/apache/tvm/pull/15050) - [Schedule] Fix decompose_padding bug with dtypes
 * [#15034](https://github.com/apache/tvm/pull/15034) - Refactor BlockScope outside schedule
 * [#15054](https://github.com/apache/tvm/pull/15054) - Handle DeclBuffer in IRSubstitute
 * [#14986](https://github.com/apache/tvm/pull/14986) - Move SplitHostDevice to before MakePackedAPI
 * [#15042](https://github.com/apache/tvm/pull/15042) - Handle DeclBuffer in StorageFlatten's input
 * [#15040](https://github.com/apache/tvm/pull/15040) - Preserve object equality in Buffer::GetFlattenedBuffer
 * [#14693](https://github.com/apache/tvm/pull/14693) - Enhance TVMScript Buffer Slice Access
 * [#14988](https://github.com/apache/tvm/pull/14988) - Handle callees on same target, different codegen
 * [#14951](https://github.com/apache/tvm/pull/14951) - Keep trivial LetStmt in tir.Simplify when used in buffer decl
 * [#14944](https://github.com/apache/tvm/pull/14944) - Restrict tir.transform.LowerTVMBuiltin to host functions
 * [#14990](https://github.com/apache/tvm/pull/14990) - [IR,TE,TIR] Use f-strings for string formatting, NFC
 * [#14993](https://github.com/apache/tvm/pull/14993) - Fix incorrect construction of block frames
 * [#14952](https://github.com/apache/tvm/pull/14952) - Avoid re-defining `var = arg_var` in ArgBinder
 * [#14918](https://github.com/apache/tvm/pull/14918) - SplitHostDevice, handle subroutines
 * [#14943](https://github.com/apache/tvm/pull/14943) - Restrict tir.transform.InstallDebugSpans to host functions
 * [#14942](https://github.com/apache/tvm/pull/14942) - Preserve existing kTarget function attribute in BindTarget
 * [#14945](https://github.com/apache/tvm/pull/14945) - Restrict tir.transform.CombineContextCall to host functions
 * [#14914](https://github.com/apache/tvm/pull/14914) - Handle subroutine calls in MakeUnpackedAPI
 * [#14913](https://github.com/apache/tvm/pull/14913) - Handle subroutine calls in MakePackedAPI
 * [#14892](https://github.com/apache/tvm/pull/14892) - Expand unit tests for ConvertSSA
 * [#14866](https://github.com/apache/tvm/pull/14866) - Avoid too complex predicate in compaction
 * [#14766](https://github.com/apache/tvm/pull/14766) - [Schedule] Improve blockize to support blockizing multiple blocks
 * [#14776](https://github.com/apache/tvm/pull/14776) - Improved parameter name in DLTensor unpacking error messages
 * [#14562](https://github.com/apache/tvm/pull/14562) - [Driver] Move ShouldAnnotateEntryFunc logic into transform
 * [#14741](https://github.com/apache/tvm/pull/14741) - Keep block annotations from tensorization
 * [#14021](https://github.com/apache/tvm/pull/14021) - More flexible buffer compaction
 * [#14711](https://github.com/apache/tvm/pull/14711) - [Analysis] Calculate allocated memory at module level
 * [#14492](https://github.com/apache/tvm/pull/14492) - Flatten SeqStmt on construction
 * [#14598](https://github.com/apache/tvm/pull/14598) - Add CUDA int4 tensor core intrinsics
 * [#14593](https://github.com/apache/tvm/pull/14593) - [Schedule] Method returning the function being worked on
 * [#14592](https://github.com/apache/tvm/pull/14592) - [TensorIR] Fix ComputeAt with perfect symbolic bound
 * [#14491](https://github.com/apache/tvm/pull/14491) - Use String instead of StringImm for AttrStmtNode::node
 * [#14626](https://github.com/apache/tvm/pull/14626) - [TensorIR]`reindex_cache_write` do not mutate init statement
 * [#14588](https://github.com/apache/tvm/pull/14588) - [Fix][TIR] UnifyThreadBinding creating unit loop with annotation
 * [#14589](https://github.com/apache/tvm/pull/14589) - [Fix][TIR][Analysis] Reduction block checking alloc_buffers

### TVMScript
 * [#15083](https://github.com/apache/tvm/pull/15083) - Avoid visiting repetition tensor in SetCommonPrefix Visitor
 * [#15091](https://github.com/apache/tvm/pull/15091) - [TIR]Convert tir.op operands to PrimExpr
 * [#14919](https://github.com/apache/tvm/pull/14919) - [TIR] Parse subroutine calls with no arguments
 * [#14941](https://github.com/apache/tvm/pull/14941) - Prevent bool to int conversion in T.Assert condition
 * [#14915](https://github.com/apache/tvm/pull/14915) - Allow T.target("device", host="host") to specify host
 * [#14900](https://github.com/apache/tvm/pull/14900) - Round-trip DeclBuffer with undefined data pointer
 * [#14889](https://github.com/apache/tvm/pull/14889) - [TIR]Added format/parsing of subroutine calls
 * [#14874](https://github.com/apache/tvm/pull/14874) - Use default fallback for un-registered type
 * [#14840](https://github.com/apache/tvm/pull/14840) - Print Executor, Runtime, and FunctionInfo as metadata
 * [#14812](https://github.com/apache/tvm/pull/14812) - Handle AllocatedPoolInfo, ConstantPoolInfo, ConstantInfo
 * [#14786](https://github.com/apache/tvm/pull/14786) - Add `__name__` attr for parsed PrimFunc and IRModule
 * [#14531](https://github.com/apache/tvm/pull/14531) - Preserve LetStmt of constants
 * [#14488](https://github.com/apache/tvm/pull/14488) - Distinguish between void* and handle

### TVMC
 * [#14994](https://github.com/apache/tvm/pull/14994) - [Bugfix]Fix tvmc option for printing which operators are offloaded to the Ethos-U

### LLVM
 * [#15127](https://github.com/apache/tvm/pull/15127) - Remove the "ret_void" argument of AddFunction
 * [#15139](https://github.com/apache/tvm/pull/15139) - Minor refactor to LLVMModuleNode::SaveToFile
 * [#14958](https://github.com/apache/tvm/pull/14958) - [Codegen]Allow void return type from PackedFunc
 * [#14946](https://github.com/apache/tvm/pull/14946) - Expose Host CPU Feature Detection
 * [#14901](https://github.com/apache/tvm/pull/14901) - Codegen subroutine call when CallNode::op is GlobalVar
 * [#14570](https://github.com/apache/tvm/pull/14570) - Use Var annotation in LetStmt for pointer type
 * [#14843](https://github.com/apache/tvm/pull/14843) - [RUNTIME] Enable multi systemlib with device code
 * [#14564](https://github.com/apache/tvm/pull/14564) - Validate generated LLVM module before optimization
 * [#14568](https://github.com/apache/tvm/pull/14568) - Expand tvm::Type to DWARF conversion
 * [#14563](https://github.com/apache/tvm/pull/14563) - [Codegen]Remove cast to i8* in builtin::address_of

### BugFix
 * [#14960](https://github.com/apache/tvm/pull/14960) - [Bug] Add typing_extensions requirement again
 * [#15015](https://github.com/apache/tvm/pull/15015) - [Hotfix] Remove `LOG(INFO)` from unsupported dtype legalization pass
 * [#14991](https://github.com/apache/tvm/pull/14991) - Make ThreadAllReduce pass compatible with int64
 * [#14950](https://github.com/apache/tvm/pull/14950) - Avoid symbol conflicts in MakePackedAPI/MakeUnpackedAPI
 * [#14903](https://github.com/apache/tvm/pull/14903) - [Test Cases]Add some version check to make test cases run in all PyTorch versions
 * [#14890](https://github.com/apache/tvm/pull/14890) - [Fix] Fix typo in error message
 * [#14879](https://github.com/apache/tvm/pull/14879) - fix the undeclared identifier 'f'
 * [#14857](https://github.com/apache/tvm/pull/14857) - Fix batch_norm
 * [#14787](https://github.com/apache/tvm/pull/14787) - [FIX] fix typo in comment

## CI
 * [#15179](https://github.com/apache/tvm/pull/15179) - [Testing] Utility method to run TVM on remote device
 * [#15138](https://github.com/apache/tvm/pull/15138) - [Test] Improve check for TVMError exception in test_cast
 * [#15062](https://github.com/apache/tvm/pull/15062) - Clone submodule recursively
 * [#15065](https://github.com/apache/tvm/pull/15065) - Revert "Make Graviton3 default AArch64 job runner node (#14983)"
 * [#14983](https://github.com/apache/tvm/pull/14983) - Make Graviton3 default AArch64 job runner node
 * [#15056](https://github.com/apache/tvm/pull/15056) - [Bugfix]Fix CacheControl version constraint violation
 * [#14908](https://github.com/apache/tvm/pull/14908) - Update the expected CI jobs list in the update_branch script
 * [#14847](https://github.com/apache/tvm/pull/14847) - Update CPU image to install PyTorch
 * [#14808](https://github.com/apache/tvm/pull/14808) - [Testing] Use TVMScript's "name" argument for error messages
 * [#14780](https://github.com/apache/tvm/pull/14780) - fix doc deploy issue
 * [#14651](https://github.com/apache/tvm/pull/14651) - Modify test cases to accommodate the CI upgrades
 * [#14666](https://github.com/apache/tvm/pull/14666) - sccache support while using ci.py under multi user environments
 * [#14635](https://github.com/apache/tvm/pull/14635) - Upgrade CI
 * [#14713](https://github.com/apache/tvm/pull/14713) - Add PLATFORM env var to builds
 * [#14680](https://github.com/apache/tvm/pull/14680) - Downgrade ci_cpu llvm version back to 11
 * [#14653](https://github.com/apache/tvm/pull/14653) - [tests][scripts][release] Optimize release note script about categories etc
 * [#14646](https://github.com/apache/tvm/pull/14646) - [test][script] Fix release gather_pr.py of script about ghost users or blank PR nodes
 * [#14550](https://github.com/apache/tvm/pull/14550) - Add JAX deps in Dockerfiles
 * [#14466](https://github.com/apache/tvm/pull/14466) - Update ci_cpu image and build with llvm-15


### Docker
 * [#15149](https://github.com/apache/tvm/pull/15149) - Fix build.sh environment variables
 * [#15105](https://github.com/apache/tvm/pull/15105) - Update docker images for llvm-16
 * [#15092](https://github.com/apache/tvm/pull/15092) - Update ci-cortexm docker image to contain CMSIS-NN release v…
 * [#15095](https://github.com/apache/tvm/pull/15095) - Add build.sh environment variables
 * [#15067](https://github.com/apache/tvm/pull/15067) - Migrate arm docker image to use llvm packages
 * [#15031](https://github.com/apache/tvm/pull/15031) - Update ci_cpu docker image to one containing polly package f…
 * [#15003](https://github.com/apache/tvm/pull/15003) - [ADRENO] Docker setup changes for multi user environments
 * [#14912](https://github.com/apache/tvm/pull/14912) - Add polly package
 * [#14842](https://github.com/apache/tvm/pull/14842) - Install PyTorch on cpu image
 * [#14590](https://github.com/apache/tvm/pull/14590) - Support rootless docker when using docker/bash.sh

### Docs
 * [#15126](https://github.com/apache/tvm/pull/15126) - [DOC] Add RPC System Setup Document
 * [#15071](https://github.com/apache/tvm/pull/15071) - Updated the copyright year from 2020 to 2023
 * [#15055](https://github.com/apache/tvm/pull/15055) - [DOC][TUTORIAL] Fix typo for the 'Making your Hardware Accelerator TVM-ready with UMA'
 * [#14504](https://github.com/apache/tvm/pull/14504) - [TensorIR][Doc] Docstring of `reorder_block_iter_var`
 * [#14611](https://github.com/apache/tvm/pull/14611) - [TIR] Fix unsafe_set_dtype docstring
 * [#14585](https://github.com/apache/tvm/pull/14585) - Fix typo in the Vitis AI Integration docs

### Misc
 * [#15267](https://github.com/apache/tvm/pull/15267) - [release] Disable git merge to avoid conflict
 * [#15187](https://github.com/apache/tvm/pull/15187) - [RPC] Report RPC Session Timeout to Client Instead of "kShutdown"
 * [#15185](https://github.com/apache/tvm/pull/15185) - Update tvm_runtime.h
 * [#15164](https://github.com/apache/tvm/pull/15164) - [CMake] Support LLVM-16 static linking
 * [#15167](https://github.com/apache/tvm/pull/15167) - [Python] Enhance Wheel Packaging
 * [#15166](https://github.com/apache/tvm/pull/15166) - [Target] Add MetaSchedule-compatible attributes to OpenCL
 * [#15154](https://github.com/apache/tvm/pull/15154) - [Minor] Fix Compilation Warnings
 * [#15132](https://github.com/apache/tvm/pull/15132) - [NDArray] Allow creating a view from a strided array
 * [#15116](https://github.com/apache/tvm/pull/15116) - [RPC] Add Missing Option "port_end" to RPC Proxy
 * [#15073](https://github.com/apache/tvm/pull/15073) - [CodeGenC] Use PrimFuncNode::ret_type in function signature
 * [#15036](https://github.com/apache/tvm/pull/15036) - [StackVM] Updated CodeGenStackVM to handle DeclBuffer
 * [#15022](https://github.com/apache/tvm/pull/15022) - [Build] Fix missing virtual destructor in SIBuilder
 * [#15016](https://github.com/apache/tvm/pull/15016) - Fix type parse error about AdaptiveMaxPool
 * [#15007](https://github.com/apache/tvm/pull/15007) - [Minor] Fix compilation warnings
 * [#15000](https://github.com/apache/tvm/pull/15000) - [CMAKE] Introduce dummy build as an option
 * [#14863](https://github.com/apache/tvm/pull/14863) - [DataType] Initial support of fp8 (e4m3/e5m2)
 * [#14975](https://github.com/apache/tvm/pull/14975) - [CMAKE] Add a dummy target to defer libtvm dep
 * [#14574](https://github.com/apache/tvm/pull/14574) - [IR][SIBuilder]
 * [#14939](https://github.com/apache/tvm/pull/14939) - [Target] Add target to all TVM callbacks
 * [#14937](https://github.com/apache/tvm/pull/14937) - [BUILD] Enable log before throw message in windows
 * [#14934](https://github.com/apache/tvm/pull/14934) - [TestCases] fix unreachable test cases due to outside the for-loop
 * [#14916](https://github.com/apache/tvm/pull/14916) - [TypoFix] fix some typo problem in keras frontend
 * [#14893](https://github.com/apache/tvm/pull/14893) - [Contrib] Use f-strings for string formatting, NFC
 * [#14884](https://github.com/apache/tvm/pull/14884) - [AutoTVM] Use f-strings for string formatting, NFC
 * [#14876](https://github.com/apache/tvm/pull/14876) - [CONTRIB] Enable create_staticlib to take in tar files
 * [#14867](https://github.com/apache/tvm/pull/14867) - Fix f-string typo
 * [#14851](https://github.com/apache/tvm/pull/14851) - Add v0.12.0 docs
 * [#14813](https://github.com/apache/tvm/pull/14813) - [BUILD] Removed the duplicated MACROs in config.cmake
 * [#14743](https://github.com/apache/tvm/pull/14743) - [SUPPORT] Fix RingBuffer ReadWithCallback
 * [#14799](https://github.com/apache/tvm/pull/14799) - [LINT] Fix clang-format script for newest clang-format
 * [#14797](https://github.com/apache/tvm/pull/14797) - [NDArray] Allow arbitrary stride when the corresponding shape is 1
 * [#14790](https://github.com/apache/tvm/pull/14790) - More clear ref of thirdparty license
 * [#14779](https://github.com/apache/tvm/pull/14779) - fix: use arm on demand instead of spot
 * [#14762](https://github.com/apache/tvm/pull/14762) - [Target][Minor] Add A6000 Target Tag
 * [#14683](https://github.com/apache/tvm/pull/14683) - [AutoTVM] Added Droplet algorithm in TVM
 * [#14694](https://github.com/apache/tvm/pull/14694) - unify search path approach to various libs
 * [#14686](https://github.com/apache/tvm/pull/14686) - [CMAKE] Update search pattern of config
 * [#14636](https://github.com/apache/tvm/pull/14636) - Fix bug about wrong attribute name
 * [#14628](https://github.com/apache/tvm/pull/14628) - [CODEGEN] Fix metal codegen when with only single working dim
 * [#14607](https://github.com/apache/tvm/pull/14607) - fix: deploy ci
 * [#14569](https://github.com/apache/tvm/pull/14569) - [Node] Allow alternative root names in ObjectPath::Root()
 * [#14522](https://github.com/apache/tvm/pull/14522) - [Object] Implemented .as<T> for ObjectRef param, returns Optional<T>
 * [#14477](https://github.com/apache/tvm/pull/14477) - feat: use spot instances for ci with on demand as a backup
 * [#14468](https://github.com/apache/tvm/pull/14468) - [AutoTVM] New rank-binary loss_type for the new xgboost >= 2.0.0 behaviour
 * [#14544](https://github.com/apache/tvm/pull/14544) - Update to v0.13.dev0
 * [#14539](https://github.com/apache/tvm/pull/14539) - [Target] Add Apple M1 GPU tag with 256-thread restriction

## v0.14.0 (2023-10-23)

# Introduction

The TVM community has worked since the v0.13.0 release to deliver the following new exciting improvements! The main tags are below (**bold text is with lots of progress**):

- Community, RFC
- **Arith**, MetaSchedule
- Adreno, ArmComputeLibrary, Hexagon, Metal, OpenCL & CLML, ROCm, Vulkan, cuda & cutlass & tensorrt, **micoNPU**, web
- Runtime, TVMC, AOT, LLVM, microTVM, CMSIS-NN
- **Frontend**, **Relay**, BYOC
- TOPI, **TIR**, TVMScript
- Docs, **CI**, **Docker**
- **Misc**, , BugFix

Please visit the full listing of commits for a complete view: [v0.13.0...v0.14.0](https://github.com/apache/tvm/compare/v0.13.0...v0.14.0).

### Community

- [#15307](https://github.com/apache/tvm/pull/15307) - Qingchao Shen -> Reviewer
- [#15619](https://github.com/apache/tvm/pull/15619) - community strategy decision process

### RFC

- [#102](https://github.com/apache/tvm-rfcs/pull/102) - [[Process RFC] Clarify Community Strategy Decision Process](https://github.com/tqchen/tvm-rfcs/blob/strategy/rfcs/0102-clarify-strategy-decision-process.md)

----

### AOT
 * [#15301](https://github.com/apache/tvm/pull/15301) - Avoid call_extern() with incorrect argument count
 * [#15181](https://github.com/apache/tvm/pull/15181) - Remove workaround to help resolve test flakiness

### Adreno
 * [#15830](https://github.com/apache/tvm/pull/15830) - Minor changes for Adreno docs and help scripts
 * [#15671](https://github.com/apache/tvm/pull/15671) - [VM]Fix using buffers for weights in VM
 * [#15391](https://github.com/apache/tvm/pull/15391) - Small fixes in Adreno schedules

### Arith
 * [#15881](https://github.com/apache/tvm/pull/15881) - Simplify the result of non-divisible floordiv
 * [#15665](https://github.com/apache/tvm/pull/15665) - Fix detect non-divisible iteration form like (x % 255) // 16
 * [#15638](https://github.com/apache/tvm/pull/15638) - MLIR PresburgerSet compile fix mlir >= 160
 * [#15628](https://github.com/apache/tvm/pull/15628) - Added simplification rule for multiple equality compares
 * [#15558](https://github.com/apache/tvm/pull/15558) - Fix detect linear equation with uint var
 * [#14690](https://github.com/apache/tvm/pull/14690) - Add tvm::arith::PresburgerSetNode to work with Presburger Set in MLIR
 * [#15555](https://github.com/apache/tvm/pull/15555) - Fix handling of overlapping predicates
 * [#15471](https://github.com/apache/tvm/pull/15471) - Enhance Canonical Simplify for LE
 * [#15228](https://github.com/apache/tvm/pull/15228) - Enhance buffer shape bound deduction to include offset

### ArmComputeLibrary
 * [#15600](https://github.com/apache/tvm/pull/15600) - [ACL] Update Compute Library to v23.05.1
 * [#15344](https://github.com/apache/tvm/pull/15344) - [ACL] Update Compute Library to v23.05

### BugFix
 * [#15891](https://github.com/apache/tvm/pull/15891) - [Relay]fix axis parsing of repeat converter in the MXNet frontend
 * [#15873](https://github.com/apache/tvm/pull/15873) - [Fix] Remove duplicated words from comments, NFC
 * [#15868](https://github.com/apache/tvm/pull/15868) - [Relay]Fix conv transpose with default strides in ONNX frontend
 * [#15773](https://github.com/apache/tvm/pull/15773) - [CPP] Fix cpp deploy bug
 * [#15778](https://github.com/apache/tvm/pull/15778) - [Hotfix] Fix Windows Pipe
 * [#15748](https://github.com/apache/tvm/pull/15748) - Move symbols that are relevant to the runtime from libtvm to…
 * [#15752](https://github.com/apache/tvm/pull/15752) - [Relay]fix the wrong calculate logic of operator flip in PyTorch frontend
 * [#15715](https://github.com/apache/tvm/pull/15715) - [Relay]Fix the wrong implementation about operator Threshold in oneflow
 * [#15711](https://github.com/apache/tvm/pull/15711) - [Strategy] Fix `arm_cpu` int8 conv2d strategy for dotprod and i8mm targets
 * [#15717](https://github.com/apache/tvm/pull/15717) - [Relay]fix the wrong implementation of Softplus in OneFlow
 * [#15677](https://github.com/apache/tvm/pull/15677) - [Arith] IterMapRewriter abort rewriting once failure
 * [#15629](https://github.com/apache/tvm/pull/15629) - [VTA] tvm.tir.Call has no name attribute
 * [#15584](https://github.com/apache/tvm/pull/15584) - [Relay][Strategy] Enable compile time transformation of weights matrix for arm_cpu NHWC quantized conv2d
 * [#15542](https://github.com/apache/tvm/pull/15542) - [Fix] Fix the typo in compile flag
 * [#15484](https://github.com/apache/tvm/pull/15484) - [TOPI] Fix a bug in arm_cpu int8 conv2d i8mm schedule
 * [#15473](https://github.com/apache/tvm/pull/15473) - [Relay] Fix some bugs of dominator pattern
 * [#15478](https://github.com/apache/tvm/pull/15478) - [TIR] ThreadSync with shared.dyn awareness
 * [#15406](https://github.com/apache/tvm/pull/15406) - [TIR]Ensure the Var's scope is correct
 * [#15399](https://github.com/apache/tvm/pull/15399) - [TIR] Fix multi-grouped multi-warp allreduce
 * [#15350](https://github.com/apache/tvm/pull/15350) - [Relay] fix a bug of  printing dataflow pattern
 * [#15385](https://github.com/apache/tvm/pull/15385) - Work around "Internal Compiler Error" in MSVC
 * [#15294](https://github.com/apache/tvm/pull/15294) - [Bug][Relay] fix relay frontend pytorch op addmm bug
 * [#15323](https://github.com/apache/tvm/pull/15323) - [Fix][TIR] LowerThreadAllreduce with correct thread mask
 * [#15291](https://github.com/apache/tvm/pull/15291) - [Relay][GraphExecutor] Fix set_input_zero_copy() precision bug
 * [#15225](https://github.com/apache/tvm/pull/15225) - Fix function to read all file

### CI
 * [#15903](https://github.com/apache/tvm/pull/15903) - [Target]Add LLVM functions for current system info
 * [#15897](https://github.com/apache/tvm/pull/15897) - [ADRENO] Few updates to Adreno docker setup
 * [#15836](https://github.com/apache/tvm/pull/15836) - Update ci-gpu image
 * [#15668](https://github.com/apache/tvm/pull/15668) - Allow Limit CPUs in Docker
 * [#15568](https://github.com/apache/tvm/pull/15568) - [Testing] Allow Capitalized name in CompareBeforeAfter
 * [#15519](https://github.com/apache/tvm/pull/15519) - [TEST] Run tests/python/relay/aot tests in ci-cortexm
 * [#15485](https://github.com/apache/tvm/pull/15485) - Remove cython version pin
 * [#15421](https://github.com/apache/tvm/pull/15421) - Bump Flax and Jaxlib versions to fix Jaxlib install error
 * [#15226](https://github.com/apache/tvm/pull/15226) - Add ml_dypes dependency for all docker images
 * [#15353](https://github.com/apache/tvm/pull/15353) - Pin cython version to fix cython compilation
 * [#15352](https://github.com/apache/tvm/pull/15352) - Make Graviton3 default AArch64 job runner node
 * [#15339](https://github.com/apache/tvm/pull/15339) - Update test to include unique attribute
 * [#15277](https://github.com/apache/tvm/pull/15277) - [Testing] Return BenchmarkResult in local_run and rpc_run
 * [#15268](https://github.com/apache/tvm/pull/15268) - [Testing] Add tvm.testing.local_run
 * [#15136](https://github.com/apache/tvm/pull/15136) - [UnitTest][NVPTX] Avoid cascading failures from CUDA postproc

### CMSIS-NN
 * [#15747](https://github.com/apache/tvm/pull/15747) - Move CMSIS_5 from SHA to release based upgrade
 * [#15407](https://github.com/apache/tvm/pull/15407) - Support for Softmax Int16 operator

### Docker
 * [#15799](https://github.com/apache/tvm/pull/15799) - Add LLVM 17 to the LLVM install script
 * [#15862](https://github.com/apache/tvm/pull/15862) - Upgrade oneflow to v0.8.0
 * [#15819](https://github.com/apache/tvm/pull/15819) - Install oneflow from PyPi
 * [#15310](https://github.com/apache/tvm/pull/15310) - Update ci-cortexm docker image
 * [#15293](https://github.com/apache/tvm/pull/15293) - tensorflow_aarch64 package upgrade

### Docs
 * [#15619](https://github.com/apache/tvm/pull/15619) - community strategy decision process
 * [#15508](https://github.com/apache/tvm/pull/15508) - Add v0.13.0 docs to site
 * [#15213](https://github.com/apache/tvm/pull/15213) - [#15157][Rust][Doc] Re-enable the Rust documentation build

### Frontend
 * [#15821](https://github.com/apache/tvm/pull/15821) - [TFLite]Support quantized ELU
 * [#15844](https://github.com/apache/tvm/pull/15844) - [TFLite]Fix test failures caused by div-by-zero
 * [#15798](https://github.com/apache/tvm/pull/15798) - [TFLite]Support quantized Pow
 * [#15829](https://github.com/apache/tvm/pull/15829) - [Relay][Keras][Bugfix] fix the converters of GRU and SimpleRNN about the go_backwards attribute
 * [#15838](https://github.com/apache/tvm/pull/15838) - Fix unnecessary pylint errors
 * [#15802](https://github.com/apache/tvm/pull/15802) - [SkipCI][Hotfix][TFLite] Disable test of quantized floor mod
 * [#15790](https://github.com/apache/tvm/pull/15790) - [TFLite]Support quantized LESS_EQUAL
 * [#15775](https://github.com/apache/tvm/pull/15775) - [TFLite]Support quantized GREATER_EQUAL
 * [#15769](https://github.com/apache/tvm/pull/15769) - [TFLite]Support quantized NOT_EQUAL
 * [#15768](https://github.com/apache/tvm/pull/15768) - [TFLite]Support quantized div
 * [#15746](https://github.com/apache/tvm/pull/15746) - [TFLite]Support quantized LESS
 * [#15733](https://github.com/apache/tvm/pull/15733) - [TFLite]Support quantized floor_mod
 * [#15724](https://github.com/apache/tvm/pull/15724) - [TFLite]Support quantized floor_div
 * [#15602](https://github.com/apache/tvm/pull/15602) - [ONNX][BugFix] Support If body with free variable from graph input
 * [#15472](https://github.com/apache/tvm/pull/15472) - [Relay][TFLite] Fix in qnn.conv2d when parameter groups not equal to 1
 * [#15117](https://github.com/apache/tvm/pull/15117) - [TFLITE] Add support for TFLite's regular NMS operator
 * [#15415](https://github.com/apache/tvm/pull/15415) - [ONNX] add onnx Mish operator
 * [#15422](https://github.com/apache/tvm/pull/15422) - [Keras] Add support for swish actiivation
 * [#15370](https://github.com/apache/tvm/pull/15370) - [Relay][Pytorch] Add aten::view_as
 * [#15335](https://github.com/apache/tvm/pull/15335) - [Bugfix][Keras] Add a check to reject the invalid input shape
 * [#15334](https://github.com/apache/tvm/pull/15334) - [Bugfix][Relay][Keras] Add a assertion to reject a invalid value for attribute units in RNN layers
 * [#15337](https://github.com/apache/tvm/pull/15337) - [Bugfix][Keras]Fix a corner case bug in softmax converter of keras frontend
 * [#15259](https://github.com/apache/tvm/pull/15259) - [TFLITE][BugFix] Fix variable typo in batchmatmul converting func
 * [#15261](https://github.com/apache/tvm/pull/15261) - [bugfix][keras] Fix go_backwards attribute of LSTM in keras frontend

### Hexagon
 * [#15788](https://github.com/apache/tvm/pull/15788) - Properly handle RPC server shutdown
 * [#15599](https://github.com/apache/tvm/pull/15599) - F2qi avgpool bug fix
 * [#15414](https://github.com/apache/tvm/pull/15414) - Add default vtcm capacity for targets
 * [#15367](https://github.com/apache/tvm/pull/15367) - Simplify Mul->Sub->Conv to Conv->Add when possible
 * [#15258](https://github.com/apache/tvm/pull/15258) - Propagate QNN Concat Quantization Params to Inputs

### LLVM
 * [#15921](https://github.com/apache/tvm/pull/15921) - Fix for llvm CodeGenOpt API change

### MetaSchedule
 * [#15792](https://github.com/apache/tvm/pull/15792) - Allow generating uint random data
 * [#15574](https://github.com/apache/tvm/pull/15574) - Fix metaschedule flop estimation for non-integer loop dimensions
 * [#15532](https://github.com/apache/tvm/pull/15532) - Enable subprocess to stdout for DEBUG level
 * [#15437](https://github.com/apache/tvm/pull/15437) - Fix mma default rule and disable tuning abort
 * [#15133](https://github.com/apache/tvm/pull/15133) - [XGBoost,MetaSchedule] Support xgb set tree method

### Metal
 * [#15756](https://github.com/apache/tvm/pull/15756) - [Unittest]Add minimal metal functionality test to CI
 * [#15749](https://github.com/apache/tvm/pull/15749) - [UnitTest]Parametrize allreduce GPU tests
 * [#15401](https://github.com/apache/tvm/pull/15401) - [Codegen]Support metal warp-level primitive

### OpenCL & CLML
 * [#15745](https://github.com/apache/tvm/pull/15745) - [OpenCL] Don't initialize OpenCL runtime on host
 * [#15400](https://github.com/apache/tvm/pull/15400) - [VM][OpenCL] Introduce textures allocation to VM memory manager

### ROCm
 * [#15777](https://github.com/apache/tvm/pull/15777) - [Codegen]Mismatched Dtype of Workgroup/Workitem
 * [#15464](https://github.com/apache/tvm/pull/15464) - fma intrin
 * [#15454](https://github.com/apache/tvm/pull/15454) - Fix some ROCm codegen bugs

### Relay
 * [#15889](https://github.com/apache/tvm/pull/15889) - fix the conflicted documentation description
 * [#15648](https://github.com/apache/tvm/pull/15648) - [TOPI] Remove input padding for arm_cpu conv2d int8 native schedule in Legalize pass
 * [#15386](https://github.com/apache/tvm/pull/15386) - Fix an adaptive_max_pool1d operator conversion bug
 * [#15533](https://github.com/apache/tvm/pull/15533) - Disable exception for ADT in mixed precision pass
 * [#15506](https://github.com/apache/tvm/pull/15506) - [Strategy] Use x86 pool schedules for arm_cpu
 * [#15470](https://github.com/apache/tvm/pull/15470) - [Strategy] Use x86 dense schedules for arm_cpu
 * [#15392](https://github.com/apache/tvm/pull/15392) - add redirecting operation to dataflow pattern graph
 * [#15468](https://github.com/apache/tvm/pull/15468) - [Strategy] Fix `arm_cpu` int8 conv2d schedule selection for 32-bit targets
 * [#15461](https://github.com/apache/tvm/pull/15461) - Stop ToMixedPrecision when constant is out of dtype range
 * [#15362](https://github.com/apache/tvm/pull/15362) - improve SimplifyClipAndConsecutiveCast pass
 * [#15137](https://github.com/apache/tvm/pull/15137) - Introduce arguments limit to FuseOps pass
 * [#15211](https://github.com/apache/tvm/pull/15211) - Fix bug in MergeCompilerRegions pass
 * [#15237](https://github.com/apache/tvm/pull/15237) - ExprMutator Return Origin Expr When All Fields Isn't Changed
 * [#15235](https://github.com/apache/tvm/pull/15235) - [QNN] Support Dequantize to "float16" and Quantize to "uint16"

### Runtime
 * [#15693](https://github.com/apache/tvm/pull/15693) - Make `CSourceModule` and `StaticLibraryModule` Binary Serializable
 * [#15658](https://github.com/apache/tvm/pull/15658) - Make `export_library` parameters after `file_name` keyword-only
 * [#15637](https://github.com/apache/tvm/pull/15637) - [Backport]Fix ICE from Clang
 * [#15244](https://github.com/apache/tvm/pull/15244) - Serialization/Deserialization of runtime module
 * [#15630](https://github.com/apache/tvm/pull/15630) - Utils to Stringify Device
 * [#15623](https://github.com/apache/tvm/pull/15623) - Expose ModuleGetFunction as PackedFunc
 * [#15595](https://github.com/apache/tvm/pull/15595) - Enhance PackedFunc Metaprogramming with `PackArgs`
 * [#15543](https://github.com/apache/tvm/pull/15543) - [Minor] Suppress verbose logging in Metal device API
 * [#15305](https://github.com/apache/tvm/pull/15305) - Flush L2 cache in time eval
 * [#15332](https://github.com/apache/tvm/pull/15332) - Device API to query L2 cache size

### TIR
 * [#15913](https://github.com/apache/tvm/pull/15913) - Fix offset_factor in cuda tensor core intrins
 * [#15906](https://github.com/apache/tvm/pull/15906) - Fix the error example in the documentation for pad_einsum
 * [#15816](https://github.com/apache/tvm/pull/15816) - Revert "[TensorIR][Visitor] Visit buffer members in `match_buffer`'s in block visitor functions (#15153)
 * [#15763](https://github.com/apache/tvm/pull/15763) - Do not drop 4th argument to tir.max
 * [#15646](https://github.com/apache/tvm/pull/15646) - Output DeclBuffer in LowerThreadAllreduce
 * [#15493](https://github.com/apache/tvm/pull/15493) - Output DeclBuffer in SplitHostDevice
 * [#15517](https://github.com/apache/tvm/pull/15517) - Shuffle in PointerValueTypeRewrite for scalar reads
 * [#15263](https://github.com/apache/tvm/pull/15263) - Output DeclBuffer in MakePackedAPI
 * [#15465](https://github.com/apache/tvm/pull/15465) - [TIR, Schedule] Fix decompose reduction with thread binding loops
 * [#15432](https://github.com/apache/tvm/pull/15432) - Generalize implementation of T.macro to work with other dialects
 * [#15413](https://github.com/apache/tvm/pull/15413) - Fix Primitive Rfactor DType
 * [#15404](https://github.com/apache/tvm/pull/15404) - Allow starred expressions in TIR script
 * [#15374](https://github.com/apache/tvm/pull/15374) - Finer predicate handling in cross-thread reduction
 * [#15373](https://github.com/apache/tvm/pull/15373) - Allreduce broadcast result to each thread in multi-warp case
 * [#15214](https://github.com/apache/tvm/pull/15214) - [UX] Implement privacy annotations in TIR
 * [#15241](https://github.com/apache/tvm/pull/15241) - Return error code from kernels in SplitHostDevice
 * [#15327](https://github.com/apache/tvm/pull/15327) - ThreadAllreduce warp-level primitive support with multi-warp
 * [#15260](https://github.com/apache/tvm/pull/15260) - Implement TIR macros
 * [#15253](https://github.com/apache/tvm/pull/15253) - Call TVMBackendFreeWorkspace inside LetStmt
 * [#15264](https://github.com/apache/tvm/pull/15264) - Allow symbolic bounds in IndexMap analysis
 * [#15243](https://github.com/apache/tvm/pull/15243) - Output DeclBuffer in LowerTVMBuiltin
 * [#15236](https://github.com/apache/tvm/pull/15236) - [Schedule] Scoped CacheRead/Write producing compact region
 * [#15242](https://github.com/apache/tvm/pull/15242) - Preserve AllocateNode::annotations
 * [#15247](https://github.com/apache/tvm/pull/15247) - Allow VerifyWellFormed to accept IRModule
 * [#15192](https://github.com/apache/tvm/pull/15192) - Support cross-threaad reduction lowering with thread-broadcasting rewrite
 * [#15210](https://github.com/apache/tvm/pull/15210) - [Schedule] Derive Nonnegative Bounds from Shape Var
 * [#15207](https://github.com/apache/tvm/pull/15207) - [Transform] Add LiftThreadBinding Pass

### TOPI
 * [#15685](https://github.com/apache/tvm/pull/15685) - [Target]Use LLVM for x86 CPU feature lookup
 * [#15710](https://github.com/apache/tvm/pull/15710) - Ensure vectorization of input padding in `arm_cpu` int8 conv2d interleaved schedule
 * [#15513](https://github.com/apache/tvm/pull/15513) - check empty array of x86 injective's iters
 * [#15371](https://github.com/apache/tvm/pull/15371) - Revert "Add `arm_cpu` specific pooling schedules"
 * [#15311](https://github.com/apache/tvm/pull/15311) - Add `arm_cpu` specific pooling schedules
 * [#15286](https://github.com/apache/tvm/pull/15286) - Revert "Add `arm_cpu` specific pooling schedules"
 * [#14855](https://github.com/apache/tvm/pull/14855) - Add `arm_cpu` specific pooling schedules

### TVMC
 * [#15779](https://github.com/apache/tvm/pull/15779) - enable dumping imported modules too
 * [#15349](https://github.com/apache/tvm/pull/15349) - Add tvmc flag to print compilation time per pass

### TVMScript
 * [#15824](https://github.com/apache/tvm/pull/15824) - Preserve traceback across TVMScript parsing
 * [#15762](https://github.com/apache/tvm/pull/15762) - Use environment variable TVM_BLACK_FORMAT for .show()
 * [#15706](https://github.com/apache/tvm/pull/15706) - Disable `black_format` by default
 * [#15705](https://github.com/apache/tvm/pull/15705) - [FIX] Disable `show_object_address` in printing by default
 * [#15579](https://github.com/apache/tvm/pull/15579) - Optionally output the address as part of variable names
 * [#15564](https://github.com/apache/tvm/pull/15564) - Use triple-quoted python strings for metadata
 * [#15547](https://github.com/apache/tvm/pull/15547) - Create loop var with min_val dtype in for frame
 * [#15492](https://github.com/apache/tvm/pull/15492) - Allow use of Python builtins in script
 * [#15442](https://github.com/apache/tvm/pull/15442) - Support starred indices in for-loop
 * [#15249](https://github.com/apache/tvm/pull/15249) - Ensure completed root block has no read/write
 * [#15239](https://github.com/apache/tvm/pull/15239) - Handle parsing of PrimFunc calls with non-void return

### cuda & cutlass & tensorrt
 * [#15573](https://github.com/apache/tvm/pull/15573) - [CUTLASS][Cherry-pick] Introduce several features of cutlass profiler
 * [#15480](https://github.com/apache/tvm/pull/15480) - [Bugfix][CUTLASS] CUTLASS path finding

### micoNPU
 * [#15780](https://github.com/apache/tvm/pull/15780) - [microNPU][ETHOSU] MatMul legalization support
 * [#15428](https://github.com/apache/tvm/pull/15428) - [microNPU][ETHOSU] Fix concatenation with reused buffers
 * [#14909](https://github.com/apache/tvm/pull/14909) - [ETHOSU][MicroNPU][Pass] Add a pass to replicate pads
 * [#15186](https://github.com/apache/tvm/pull/15186) - [microNPU][ETHOSU] Add Vela's logic to select configuration block

### microTVM
 * [#15667](https://github.com/apache/tvm/pull/15667) - Check the output of microNPU demos in CI

### web
 * [#15218](https://github.com/apache/tvm/pull/15218) - Increase default EMCC compilation total memory size

### Misc
 * [#15934](https://github.com/apache/tvm/pull/15934) - [Release] [Dont Squash] Modify version number to 0.14.0 and 0.15.0.dev on main branch
 * [#15934](https://github.com/apache/tvm/pull/15934) - [Release] [Dont Squash] Modify version number to 0.14.0 and 0.15.0.dev on main branch
 * [#15847](https://github.com/apache/tvm/pull/15847) - [release] Update version to 0.14.0 and 0.15.0.dev on main branch
 * [#15867](https://github.com/apache/tvm/pull/15867) - Bump pillow from 9.3.0 to 10.0.1 in /apps/microtvm/ethosu
 * [#15866](https://github.com/apache/tvm/pull/15866) - Bump pillow from 9.3.0 to 10.0.1 in /apps/microtvm/cmsisnn
 * [#15865](https://github.com/apache/tvm/pull/15865) - Bump pillow from 9.2.0 to 10.0.1 in /apps/microtvm
 * [#15833](https://github.com/apache/tvm/pull/15833) - [VM] Memory Manager moved up to runtime
 * [#15859](https://github.com/apache/tvm/pull/15859) - [Script] Fix miscs of make_notes.py
 * [#15818](https://github.com/apache/tvm/pull/15818) - [CLI TOOLS][RTVM] Improve rtvm tool with new options to measure native performance
 * [#15761](https://github.com/apache/tvm/pull/15761) - [Target] LLVM helper functions for any target info
 * [#15672](https://github.com/apache/tvm/pull/15672) - [IR] Implemented Variant<...> container
 * [#15714](https://github.com/apache/tvm/pull/15714) - [Target][Device] Auto detect target and create device from str in torch style
 * [#15723](https://github.com/apache/tvm/pull/15723) - fix _convert_simple_rnn
 * [#15725](https://github.com/apache/tvm/pull/15725) - Revert "[CodeGenC] Handle GlobalVar callee as internal function call"
 * [#15684](https://github.com/apache/tvm/pull/15684) - [Hopper TMA] Add intrinsic to create barriers for synchronization
 * [#15683](https://github.com/apache/tvm/pull/15683) - Fix a bug caused by PyTorch instance_norm when the input shape is [1,1,1,2]
 * [#15596](https://github.com/apache/tvm/pull/15596) - [FFI] Propagate Python errors across FFI boundaries
 * [#15666](https://github.com/apache/tvm/pull/15666) - [Module] Implement custom imported modules serialization
 * [#15656](https://github.com/apache/tvm/pull/15656) - [Hopper TMA] Add CUDA codegen support for bulk asynchronous copy
 * [#15664](https://github.com/apache/tvm/pull/15664) - [IR] Use structural equal for Range equality
 * [#15649](https://github.com/apache/tvm/pull/15649) - Add output_data_sec section in corstone300.ld
 * [#15639](https://github.com/apache/tvm/pull/15639) - Do not link LLVM libraries into cpptest binary
 * [#15631](https://github.com/apache/tvm/pull/15631) - [RPC] Enhance RPC Protocol to support TVM Object
 * [#15624](https://github.com/apache/tvm/pull/15624) - [CMake] Add RCCL to TVM and TVM Runtime
 * [#15616](https://github.com/apache/tvm/pull/15616) - [Hopper TMA] CUDA codegen for async copy with barrier synchronization
 * [#15537](https://github.com/apache/tvm/pull/15537) - [CPP_RPC] export listdir for RPC
 * [#15605](https://github.com/apache/tvm/pull/15605) - [CMake] Add NCCL to TVM and TVM Runtime
 * [#15580](https://github.com/apache/tvm/pull/15580) - Fix "to" duplicate word in python and C header file
 * [#15581](https://github.com/apache/tvm/pull/15581) - Remove duplicate load word inside .cc file
 * [#15582](https://github.com/apache/tvm/pull/15582) - Remove duplicate 'from' word inside python script
 * [#15554](https://github.com/apache/tvm/pull/15554) - Bump tornado from 6.1 to 6.3.3 in /apps/microtvm
 * [#15552](https://github.com/apache/tvm/pull/15552) - Bump tornado from 6.1 to 6.3.3 in /apps/microtvm/ethosu
 * [#15553](https://github.com/apache/tvm/pull/15553) - Bump tornado from 6.1 to 6.3.3 in /apps/microtvm/cmsisnn
 * [#15536](https://github.com/apache/tvm/pull/15536) - fixed typo [TypoFix]
 * [#15529](https://github.com/apache/tvm/pull/15529) - [quantize] fix bug of annotate for output of add op
 * [#15535](https://github.com/apache/tvm/pull/15535) - Fixed search task comment
 * [#15530](https://github.com/apache/tvm/pull/15530) - Remove duplicate msg word and condition inside the function doc
 * [#15511](https://github.com/apache/tvm/pull/15511) - Remove IRModule Dependency from Target
 * [#15525](https://github.com/apache/tvm/pull/15525) - Fix typo mistake and change whethe to whether
 * [#15524](https://github.com/apache/tvm/pull/15524) - Remove duplicate the word
 * [#15103](https://github.com/apache/tvm/pull/15103) - [CodeGenC] Handle GlobalVar callee as internal function call
 * [#15419](https://github.com/apache/tvm/pull/15419) - [VM][Textures] Enable OpenCL textures for VM
 * [#15483](https://github.com/apache/tvm/pull/15483) - [Script] Be more careful when generating ast.ExtSlice for Subscript
 * [#15469](https://github.com/apache/tvm/pull/15469) - [CYTHON] Make cython compatible with 3.0
 * [#15423](https://github.com/apache/tvm/pull/15423) - [Submodule] Add Flash attention v2
 * [#15380](https://github.com/apache/tvm/pull/15380) - [Target] Add Jetson Orin Nano tag
 * [#15359](https://github.com/apache/tvm/pull/15359) - [CMAKE] Conditionally link "clog" in NNPack install
 * [#15326](https://github.com/apache/tvm/pull/15326) - [OP] Add `rms_norm` into TOPI
 * [#15312](https://github.com/apache/tvm/pull/15312) - [skipci] Fix typo in docs/arch/index.rst
 * [#15298](https://github.com/apache/tvm/pull/15298) - [Release] Extend PR tags and Format PR hyper-links in release report
 * [#15328](https://github.com/apache/tvm/pull/15328) - [Package] Remove cutlass media/docs inside cutlass_fpA_intB_gemm
 * [#15321](https://github.com/apache/tvm/pull/15321) - [JVM] Fix the Maven pom.xml for OS X arm64 tvm4j build
 * [#15265](https://github.com/apache/tvm/pull/15265) - Fix keras version problem
 * [#15292](https://github.com/apache/tvm/pull/15292) - [RPC] Fix socket bind errno on corner case
 * [#15287](https://github.com/apache/tvm/pull/15287) - [Exec] Add a script to test GPU memory bandwidth
 * [#15234](https://github.com/apache/tvm/pull/15234) - [Miscs] Enhance script about make release notes
 * [#15229](https://github.com/apache/tvm/pull/15229) - [CMAKE] Add Vulkan header for Android
 * [#15215](https://github.com/apache/tvm/pull/15215) - [Android] ndk static build
 * [#15208](https://github.com/apache/tvm/pull/15208) - Update version to 0.14.dev0 on main branch

## v0.15.0 (2024-01-19)

# Introduction

NOTE: This is last release version before unity branch switch as main branch. **No unity features**.

The TVM community has worked since the v0.14.0 release to deliver the following new exciting improvements! The main tags are below (**bold text is with lots of progress**):

- Community, RFCs
- Adreno, ArmComputeLibrary, Metal, cuda & cutlass & tensorrt, micoNPU, Runtime
- **Frontend & Relay**
- Arith, **TOPI**, **TIR**, TVMScript
- Docs, CI, **Misc**, **BugFix**

Please visit the full listing of commits for a complete view: [v0.14.0...v0.15.0](https://github.com/apache/tvm/compare/v0.14.0...v0.15.0).

### Community
 * [#16172](https://github.com/apache/tvm/pull/16172) - Yixin Dong -> Reviewer
 * [#16162](https://github.com/apache/tvm/pull/16162) - Shuai Yuan -> Committer
 * [#16164](https://github.com/apache/tvm/pull/16164) - Qiang Zhang -> Committer
 * [#16166](https://github.com/apache/tvm/pull/16166) - Bohan Hou -> PMC
 * [#16165](https://github.com/apache/tvm/pull/16165) - Ruihang Lai -> PMC

### RFCs

 * [#105](https://github.com/apache/tvm-rfcs/pull/105) - Add a new backend language——SYCL

----

### Adreno
 * [#15991](https://github.com/apache/tvm/pull/15991) - [CI] Enhancements to Adreno specific CI utils
 * [#15786](https://github.com/apache/tvm/pull/15786) - [TOPI] Add conv2d transpose nchw texture schedule

### Arith
 * [#16227](https://github.com/apache/tvm/pull/16227) - Simplify nested if_then_else when constant is appearing in then_expr

### ArmComputeLibrary
 * [#15990](https://github.com/apache/tvm/pull/15990) - [ACL] Update Compute Library to v23.08

### Metal
 * [#16192](https://github.com/apache/tvm/pull/16192) - [Device] Fix metal warp size
 * [#16033](https://github.com/apache/tvm/pull/16033) - [Codegen] Disable cross-function call in Metal codegen

### cuda & cutlass & tensorrt
 * [#16061](https://github.com/apache/tvm/pull/16061) - [CUDA] Add an option for profiling cuda kernels

### micoNPU
 * [#16003](https://github.com/apache/tvm/pull/16003) - [microNPU][ETHOSU] Fix ConcatRewriter args processing
 * [#15929](https://github.com/apache/tvm/pull/15929) - [microNPU][ETHOSU] Fix rounding mode in requantize operation

### Runtime
 * [#15896](https://github.com/apache/tvm/pull/15896) - [CLML] Fix for CLML ops and enable more test case
 * [#16133](https://github.com/apache/tvm/pull/16133) - Parallel-for with threading backend
 * [#16066](https://github.com/apache/tvm/pull/16066) - Support clear global memory allocators
 * [#16030](https://github.com/apache/tvm/pull/16030) - Introduce `TVM_MODULE_VTABLE` Macros

### BugFix
 * [#16269](https://github.com/apache/tvm/pull/16269) - Update pillow usage
 * [#16272](https://github.com/apache/tvm/pull/16272) - Fixed Inappropriate Logical Expression
 * [#16216](https://github.com/apache/tvm/pull/16216) - [TIR] Fix dynamic smem merge leaf alloc
 * [#16190](https://github.com/apache/tvm/pull/16190) - Fix the error of reloading the model library on the ROCm platform: "MIOpen Error: No invoker was registered for convolution forward.”
 * [#16167](https://github.com/apache/tvm/pull/16167) - [Relay][Pytorch] Fix missing `.dtype`
 * [#16091](https://github.com/apache/tvm/pull/16091) - [Fix] Fix `topi.rms_norm` with float32 upscale
 * [#16081](https://github.com/apache/tvm/pull/16081) - [Fix] Broken Windows Build with LLVM
 * [#16051](https://github.com/apache/tvm/pull/16051) - [Fix][TIR] Fix dtype issues for match_buffer and ramp node
 * [#14655](https://github.com/apache/tvm/pull/14655) - [VTA] Fix FSIM compile error on macOS
 * [#16021](https://github.com/apache/tvm/pull/16021) - [FFI] Typo fix of IncRef to DecRef
 * [#16010](https://github.com/apache/tvm/pull/16010) - [Fix][TIR] fix mul dtype mismatch
 * [#16000](https://github.com/apache/tvm/pull/16000) - [Fix][TIR] fix symbolic strides lower
 * [#15970](https://github.com/apache/tvm/pull/15970) - [Hotfix] Mark python-FFI handling with TVM_DLL
 * [#15965](https://github.com/apache/tvm/pull/15965) - [CI] Better to pass the build folder

### CI
 * [#16110](https://github.com/apache/tvm/pull/16110) - Refactor unittest folder
 * [#16055](https://github.com/apache/tvm/pull/16055) - Fix broken links about Jenkins
 * [#16062](https://github.com/apache/tvm/pull/16062) - Use LLVM 17 for tests on `ci_arm`
 * [#16018](https://github.com/apache/tvm/pull/16018) - [Tests] Fix work_dir location used by test_micro_tuning_with_meta_schedule
 * [#16019](https://github.com/apache/tvm/pull/16019) - [Tests] Check int8+int32 testcases in test_estimate_peak_flops_cpu
 * [#16017](https://github.com/apache/tvm/pull/16017) - [Tests] Fix str vs. int comparison in test_num_threads

### Docs
 * [#16282](https://github.com/apache/tvm/pull/16282) - [Doc] Fix minor error in doc (Add an operator to Relay)
 * [#16152](https://github.com/apache/tvm/pull/16152) - [DOC] Add v0.14.0 docs to site
 * [#16127](https://github.com/apache/tvm/pull/16127) - Revert "[#15157][Rust][Doc] Re-enable the Rust documentation build (#15213)"
 * [#16097](https://github.com/apache/tvm/pull/16097) - Add missing backtick to contribute/code_guide.rst
 * [#16089](https://github.com/apache/tvm/pull/16089) - Fix error on linting by adding `--rev` argument
 * [#16024](https://github.com/apache/tvm/pull/16024) - Update release_process.rst about version number modification

### Frontend & Relay
 * [#16243](https://github.com/apache/tvm/pull/16243) - [TFLite] Add support for quantized mirror pad
 * [#15914](https://github.com/apache/tvm/pull/15914) - [TFLite]Support quantized SQUARE
 * [#16159](https://github.com/apache/tvm/pull/16159) - [KERAS] Fix bug concat convert for NCHW
 * [#16319](https://github.com/apache/tvm/pull/16319) - [Torch] add aten:broadcast_to
 * [#16131](https://github.com/apache/tvm/pull/16131) - [Pytorch] Add support for `aten::unflatten`
 * [#16105](https://github.com/apache/tvm/pull/16105) - [Pytorch] Add support for `aten::bitwise_and`
 * [#16079](https://github.com/apache/tvm/pull/16079) - [Pytorch] Add support for aten::swapaxes operator
 * [#15502](https://github.com/apache/tvm/pull/15502) - [Pytorch] aten::copy_ support for pytorch
 * [#16180](https://github.com/apache/tvm/pull/16180) - [Pytorch] Fix bug when converting models with torch.nn.ParameterList
 * [#16143](https://github.com/apache/tvm/pull/16143) - [Pytorch] Add support for `aten::scaled_dot_product_attention`
 * [#16123](https://github.com/apache/tvm/pull/16123) - [Pytorch] Add support for `aten::linalg_vector_norm`
 * [#16171](https://github.com/apache/tvm/pull/16171) - [Frontend] Preserve Pytorch Span Names
 * [#16217](https://github.com/apache/tvm/pull/16217) - [Frontend][QNN] fix access `param_debug_name_map` to node output name in fx-quantized graph node replacement
 * [#16199](https://github.com/apache/tvm/pull/16199) - [Frontend] Add support for aten::concat
 * [#16151](https://github.com/apache/tvm/pull/16151) - conv3d depthwise bug fix
 * [#15928](https://github.com/apache/tvm/pull/15928) - Expose qnn ops directly from relay.qnn module

### TOPI
 * [#16259](https://github.com/apache/tvm/pull/16259) - Add support for group_conv3d_transpose_ncdhw for generic
 * [#16052](https://github.com/apache/tvm/pull/16052) - Enhance `topi.nn.matmul`
 * [#16080](https://github.com/apache/tvm/pull/16080) - Reduce code redundancy in conv2d weights transformation
 * [#16248](https://github.com/apache/tvm/pull/16248) - [TOPI] Add support for group_conv1d_transpose_ncw for generic
 * [#16106](https://github.com/apache/tvm/pull/16106) - [TOPI] Add conv2d NHWC hybrid schedule for `arm_cpu`

### TIR 
 * [#16239](https://github.com/apache/tvm/pull/16239) - [Schedule] TileWithTensorIntrin skip incorrect ComputeInline for input-padding
 * [#16236](https://github.com/apache/tvm/pull/16236) - ConvertSSA process entry func first
 * [#16070](https://github.com/apache/tvm/pull/16070) - [Transform] Introduce new `InjectPermutedLayout` pass
 * [#16083](https://github.com/apache/tvm/pull/16083) - Enhance Python Type Annotations for TIR Expr
 * [#16073](https://github.com/apache/tvm/pull/16073) - Support more mma intrinsics and `get_mma_intrin_group` utility
 * [#16076](https://github.com/apache/tvm/pull/16076) - Enhance Python Type Annotations for TIR stmt
 * [#16074](https://github.com/apache/tvm/pull/16074) - Fix the thread binding iter_var dtype in `Bind` primitive
 * [#16063](https://github.com/apache/tvm/pull/16063) - Fix pass RenewDefs error in gather/take case
 * [#16027](https://github.com/apache/tvm/pull/16027) - Fix software pipeline with dynamic loop extent

### TVMScript
 * [#16271](https://github.com/apache/tvm/pull/16271) - Disable concise scoping when the scope stmt is explicitly annotated
 * [#16041](https://github.com/apache/tvm/pull/16041) - Fix mismatched dtype of IterVar in `T.thread_binding`
 * [#15953](https://github.com/apache/tvm/pull/15953) - [TIR] Pretty print TIR LLVM function name
 * [#15972](https://github.com/apache/tvm/pull/15972) - delete print extra info at parsing

### Misc
 * [#16279](https://github.com/apache/tvm/pull/16279) - replace deprecated np.int with int to avoid crash
 * [#16262](https://github.com/apache/tvm/pull/16262) - Update conv2d.py
 * [#16255](https://github.com/apache/tvm/pull/16255) - [Support] Add Interrupt Handling in Pipe
 * [#16104](https://github.com/apache/tvm/pull/16104) - [LoopPartition] Fix a bug of LoopPartition in single point scenarioes
 * [#16231](https://github.com/apache/tvm/pull/16231) - [Target] Add Jetson AGX Orin tags
 * [#16221](https://github.com/apache/tvm/pull/16221) - remove deprecated np.int in slice converter (pytorch)
 * [#16214](https://github.com/apache/tvm/pull/16214) - [Python] Fix setup.py for inplace build
 * [#16174](https://github.com/apache/tvm/pull/16174) - Bump cryptography from 37.0.2 to 41.0.6 in /docker/python
 * [#16202](https://github.com/apache/tvm/pull/16202) - Fix IRModule initialization with attrs
 * [#16176](https://github.com/apache/tvm/pull/16176) - Enable ccache to accelerate contrib compilation
 * [#15968](https://github.com/apache/tvm/pull/15968) - Add missing backtick
 * [#16034](https://github.com/apache/tvm/pull/16034) - [Packaging] Include BYOC dynamic libraries into wheel
 * [#16087](https://github.com/apache/tvm/pull/16087) - Add _ffi_api.py under script folder
 * [#16039](https://github.com/apache/tvm/pull/16039) - [Target] Support obtain l2 cache size from target
 * [#16065](https://github.com/apache/tvm/pull/16065) - [Pylint] fix pylint issues from test_random to test_tedd
 * [#16031](https://github.com/apache/tvm/pull/16031) - [TRT] fix outdated module building method in tensorrt
 * [#16032](https://github.com/apache/tvm/pull/16032) - [CMake] Use llvm-config to locate Findzstd.cmake
 * [#16023](https://github.com/apache/tvm/pull/16023) - [Pylint] fix pylint issues for thrust&tflite_runtime&util
 * [#15998](https://github.com/apache/tvm/pull/15998) - [Codegen] Add shuffle for cuda and metal
 * [#16015](https://github.com/apache/tvm/pull/16015) - [Pylint] fix pylint issues for cblas
 * [#15955](https://github.com/apache/tvm/pull/15955) - [FFI][Python] Handle error propagation when line number is missing
 * [#15982](https://github.com/apache/tvm/pull/15982) - Bump werkzeug from 2.2.3 to 3.0.1 in /apps/microtvm
 * [#15966](https://github.com/apache/tvm/pull/15966) - [CMake] Fix order of GNUInstallDirs module
 * [#15952](https://github.com/apache/tvm/pull/15952) - Update ci_arm Docker tag
 * [#15940](https://github.com/apache/tvm/pull/15940) - [Minor] Fix compilation warnings for clang
 * [#15947](https://github.com/apache/tvm/pull/15947) - Bump urllib3 from 1.26.9 to 1.26.18 in /docker/python
 * [#15835](https://github.com/apache/tvm/pull/15835) - [CodeGenC][Redo] Handle GlobalVar callee as internal function call
 * [#15945](https://github.com/apache/tvm/pull/15945) - Bump urllib3 from 1.26.15 to 1.26.18 in /apps/microtvm

## v0.16.0 (2024-04-28)

# Introduction

The TVM community has worked since the v0.15.0 release to deliver the following new exciting improvements! This release version is:

- **First support of Relax**, with dynamic shape and pipeline
- **Dlight module** for optimizing LLM TIR workloads on GPU
- **Disco module** for initial SPMD multi-GPU support

The main tags are below (**bold text is with lots of progress**):

- Community, RFCs
- Adreno, ArmComputeLibrary, Metal, cuda & cutlass & tensorrt, micoNPU, Runtime
- **Relax**, **Dlight**, **Disco**
- Arith, **TIR**, TVMScript
- Docs, CI, **Misc**, **BugFix**

Please visit the full listing of commits for a complete view: [v0.16.dev0...v0.16.0.rc0](https://github.com/apache/tvm/compare/v0.16.dev0...v0.16.0.rc0).

### Community

 * [#16695](https://github.com/apache/tvm/pull/16695) - Add new key for release signing
 * [#16419](https://github.com/apache/tvm/pull/16419) - Add new key for release signing

 ### RFCs

This new RFC explores how TVM can be utilized to generate code for the SME ISA to achieve improved inference performance on supported Arm®-based hardware implementing the SME extension.

 * [#107](https://github.com/apache/tvm-rfcs/pull/107) - [RFC] Scalable Matrix Extension enablement
----

### Arith
 * [#16735](https://github.com/apache/tvm/pull/16735) - [Fixup] Require feature flag for tighter inequality bounds
 * [#16588](https://github.com/apache/tvm/pull/16588) - Provide tighter ConstIntBounds for special cases
 * [#16704](https://github.com/apache/tvm/pull/16704) - [Fix]Fix canonical simplification of LE

### BYOC
 * [#16567](https://github.com/apache/tvm/pull/16567) - Skip processed functions in FuseOpsByPattern and RunCodegen

### BugFix
 * [#16766](https://github.com/apache/tvm/pull/16766) - [Target] Added null check to fix segfault at ->defined() in cpu.cc DetectSystemTriple()
 * [#16739](https://github.com/apache/tvm/pull/16739) - [Ansor] Fixing Ansor Gradient Bug
 * [#16820](https://github.com/apache/tvm/pull/16820) - [Fix] PAPI docs
 * [#16793](https://github.com/apache/tvm/pull/16793) - [Fix] fix for numpy 2.0 compatibility
 * [#16790](https://github.com/apache/tvm/pull/16790) - [Fix] Fix build errors with VS2022
 * [#16780](https://github.com/apache/tvm/pull/16780) - [Fix] Fix numpy dtype map
 * [#16773](https://github.com/apache/tvm/pull/16773) - [Fix] Fix the purity flag of "vm.call_tir_dyn" and "kill" ops
 * [#16770](https://github.com/apache/tvm/pull/16770) - [Hotfix] Revert driver API pass ordering that breaks MLC, mark failing test
 * [#16771](https://github.com/apache/tvm/pull/16771) - [Fix] Remove redundant "remove_all_unused" in IPC memory lowering
 * [#16746](https://github.com/apache/tvm/pull/16746) - [Fix][Builtin] Fix "GetQueryPosition" of PagedKVCache
 * [#16728](https://github.com/apache/tvm/pull/16728) - [Fix] Introduce TVM_DEBUG_WITH_ABI_CHANGE to warn ABI changes in debug mode
 * [#16714](https://github.com/apache/tvm/pull/16714) - [Fix] PagedKVCache fetching compute stream when copy stream is needed
 * [#16684](https://github.com/apache/tvm/pull/16684) - [SLM] Produce well-formed Relax for nn.modules.KVCache
 * [#16659](https://github.com/apache/tvm/pull/16659) - add the default value for DFT in ONNX frontend
 * [#16637](https://github.com/apache/tvm/pull/16637) - [Transform] Preserve symbolic variables in FuseOps
 * [#16649](https://github.com/apache/tvm/pull/16649) - [FFI] Add a missing default for datatype lanes
 * [#16492](https://github.com/apache/tvm/pull/16492) - [Executor] fix debug_executor function debug_get_output
 * [#16598](https://github.com/apache/tvm/pull/16598) - [Transform]Handle non-composite lambda functions in FuseOps
 * [#16565](https://github.com/apache/tvm/pull/16565) - [Transform] Keep private non-primitive functions in FuseTIR
 * [#16518](https://github.com/apache/tvm/pull/16518) - Use x*x*x instead of pow(x,3)
 * [#16436](https://github.com/apache/tvm/pull/16436) - Ensure that bf16 arrays are created as expected
 * [#16361](https://github.com/apache/tvm/pull/16361) - Disable SingleEnvThreadVerifier
 * [#16289](https://github.com/apache/tvm/pull/16289) - [AUTOTVM][FIX] Typo fixes and add a warning in the Droplet Search

### CI
 * [#16837](https://github.com/apache/tvm/pull/16837) - Disable flaky unit test
 * [#16765](https://github.com/apache/tvm/pull/16765) - [AOT][Testing] Improve output mismatch information on test failure
 * [#16661](https://github.com/apache/tvm/pull/16661) - add merge_with_main in unity
 * [#16611](https://github.com/apache/tvm/pull/16611) - [AOT][Testing] Print output values on test failure
 * [#16546](https://github.com/apache/tvm/pull/16546) - Disable testing that downloads from mxnet
 * [#16521](https://github.com/apache/tvm/pull/16521) - Fix CI Script and Broken Tests
 * [#16502](https://github.com/apache/tvm/pull/16502) - Support tvm-bot rerun for tvm-unity task
 * [#16435](https://github.com/apache/tvm/pull/16435) - Update image tag to 20240126-070121-8ade9c30e
 * [#16420](https://github.com/apache/tvm/pull/16420) - [WASM] Update emsdk and nodejs version
 * [#16384](https://github.com/apache/tvm/pull/16384) - Remove NVIDIA_DISABLE_REQUIRE
 * [#16382](https://github.com/apache/tvm/pull/16382) - In jenkins.cmd_utils.Sh.tee, check for failing subprocess
 * [#16366](https://github.com/apache/tvm/pull/16366) - Upgrade sccache version to 0.7.*
 * [#16369](https://github.com/apache/tvm/pull/16369) - Upgrade Unity ci images
 * [#16344](https://github.com/apache/tvm/pull/16344) - Update docker images tag to 20240105-165030-51bdaec6
 * [#16340](https://github.com/apache/tvm/pull/16340) - [Unity][UnitTest] Increase atol to resolve flaky CI failure
 * [#16337](https://github.com/apache/tvm/pull/16337) - [Hexagon][UnitTest] Disable flaky quantization test
 * [#16336](https://github.com/apache/tvm/pull/16336) - Upgrade cmake version to 3.24.0

### Docker
 * [#16755](https://github.com/apache/tvm/pull/16755) - [SME]Add Fixed Virtual Platform (FVP) and toolchain install
 * [#16348](https://github.com/apache/tvm/pull/16348) - Upgrade pip in i386 container

### Disco
 * [#16618](https://github.com/apache/tvm/pull/16618) - [Disco] Propagate structlog configuration to disco workers
 * [#16639](https://github.com/apache/tvm/pull/16639) - [Disco] Expose functions to query the per-worker device/rank
 * [#16617](https://github.com/apache/tvm/pull/16617) - [Disco] Implement `Session.import_python_module` method
 * [#16715](https://github.com/apache/tvm/pull/16715) - [Disco] Propagate structlog/logging config to workers
 * [#16845](https://github.com/apache/tvm/pull/16845) - [Debug][Disco] Check if a PackedFunc exists before calling it
 * [#16817](https://github.com/apache/tvm/pull/16817) - [Disco] Reduce Process/ThreadSession message queue reads and writes
 * [#16807](https://github.com/apache/tvm/pull/16807) - [Disco] Support setting workers' CPU affinity
 * [#16375](https://github.com/apache/tvm/pull/16375) - [Unity] Fix creation of disco ProcessSession
 * [#16821](https://github.com/apache/tvm/pull/16821) - [Fix] Add TVM_DLL to Disco session
 * [#16752](https://github.com/apache/tvm/pull/16752) - [Fix] Lazy import of "psutil" in disco process pool

### Dlight
 * [#16775](https://github.com/apache/tvm/pull/16775) - [Fix][Dlight] (Low-batched-)GeMV on small spatial loops
 * [#16429](https://github.com/apache/tvm/pull/16429) - [Unity][Dlight][Fix] Reduction rule support dyn-shape epilogue
 * [#16351](https://github.com/apache/tvm/pull/16351) - [Unity] Add dlight.gpu.Fallback in DispatchSortScan, add argsort, topk, and cumprod
 * [#16338](https://github.com/apache/tvm/pull/16338) - [Unity][DLight] Introduce Specific Rule for RMSNorm
 * [#16251](https://github.com/apache/tvm/pull/16251) - [Unity][Dlight] Support dlight gemv rule on nested inner block
 * [#16878](https://github.com/apache/tvm/pull/16878) - [Dlight] Enhance vectorization loading weight for gemv
 * [#16848](https://github.com/apache/tvm/pull/16848) - [DLight] Fix a corner case for reduction rule
 * [#16701](https://github.com/apache/tvm/pull/16701) - [Dlight] Add fallback for low batch gemv with outer reduction
 * [#16678](https://github.com/apache/tvm/pull/16678) - [Dlight] LowBatchGemv rule only apply to function with spatial symbolic var
 * [#16665](https://github.com/apache/tvm/pull/16665) - [Dlight] Skip GeMV when normalization fails
 * [#16579](https://github.com/apache/tvm/pull/16579) - [Dlight] Scheduling Low batch GEMM using GEMV-like rule
 * [#16579](https://github.com/apache/tvm/pull/16579) - [Dlight] Scheduling Low batch GEMM using GEMV-like rule
 * [#16321](https://github.com/apache/tvm/pull/16321) - [DLight] Skip rule if target is not suitable
 * [#16731](https://github.com/apache/tvm/pull/16731) - [Dlight] Fix GeMV shared memory estimation

### Docs
 * [#16792](https://github.com/apache/tvm/pull/16792) - [Doc] Fix set_axis_separator example
 * [#16610](https://github.com/apache/tvm/pull/16610) - [Doc] Fixed Docstring usage example in `tvm.ir.make_node`
 * [#16572](https://github.com/apache/tvm/pull/16572) - [Doc] Remove MxNet related tutorials
 * [#16514](https://github.com/apache/tvm/pull/16514) - [Unity][Doc] Document passes that depend on `DataflowBlock`s and encourage using `ConvertToDataflow`
 * [#16482](https://github.com/apache/tvm/pull/16482) - [Doc] Fix Docstring in `extern.py` for Sphinx
 * [#16346](https://github.com/apache/tvm/pull/16346) - [Doc] Fix minor error in "Expressions in Relay"

### Frontend
 * [#16001](https://github.com/apache/tvm/pull/16001) - [ONNX] Fix interpreting auto_pad parameters in ConvTranspose operator
 * [#16651](https://github.com/apache/tvm/pull/16651) - [PaddlePaddle] PaddlePaddle model with NCHW data format that supports quantization
 * [#16616](https://github.com/apache/tvm/pull/16616) - [PaddlePaddle] Support conv2d when data_format is NHWC
 * [#16526](https://github.com/apache/tvm/pull/16526) - [Keras] Enable Dense operator for any input dims
 * [#16478](https://github.com/apache/tvm/pull/16478) - [PaddlePaddle] Fixed the bug that prevented the model from being successfully converted to microTVM on MacOS

### Hexagon
 * [#16762](https://github.com/apache/tvm/pull/16762) - [VM]Cache operations when bypass mode is enabled
 * [#16706](https://github.com/apache/tvm/pull/16706) - [VM] Add buffers to `dma_wait` builtin
 * [#16448](https://github.com/apache/tvm/pull/16448) - [VM]Implement dma_copy and dma_wait builtin for hexagon

### LLVM
 * [#16782](https://github.com/apache/tvm/pull/16782) - [SVE] Support scalable vectors in LoopVectorizer
 * [#16812](https://github.com/apache/tvm/pull/16812) - Fix compilation failure due to minor change
 * [#16808](https://github.com/apache/tvm/pull/16808) - [Runtime]Fix errors during loading of target tags
 * [#16748](https://github.com/apache/tvm/pull/16748) - Lack of DWARF type is not an error
 * [#16696](https://github.com/apache/tvm/pull/16696) - [SVE] Add codegen support for scalable buffer accesses
 * [#15964](https://github.com/apache/tvm/pull/15964) - [RUNTIME] Add optional LLVM ORCJIT runtime executor
 * [#16612](https://github.com/apache/tvm/pull/16612) - [SVE] Add support for scalable data type strings
 * [#16523](https://github.com/apache/tvm/pull/16523) - [SVE] Change the dtype of Ramp and Broadcast lanes to PrimExpr
 * [#16484](https://github.com/apache/tvm/pull/16484) - [SVE] Add vscale builtin
 * [#16373](https://github.com/apache/tvm/pull/16373) - Update Host.h path

### MetaSchedule
 * [#16725](https://github.com/apache/tvm/pull/16725) - Make the `opt_level` of `tune_relay()` adjustable

### Metal
 * [#16713](https://github.com/apache/tvm/pull/16713) - [RUNTIME]Provide richer runtime when error happens
 * [#16605](https://github.com/apache/tvm/pull/16605) - [RUNTIME]Fix multithreading access of metal runtime
 * [#16438](https://github.com/apache/tvm/pull/16438) - Dispatch numerically stable tanh for metal

### OpenCL & CLML
 * [#16854](https://github.com/apache/tvm/pull/16854) - [OpenCL] Add OpenCL device for automatic target detection
 * [#16846](https://github.com/apache/tvm/pull/16846) - [Meta-Schedule][OpenCL] Enable MS tuning for Android OpenCL
 * [#16768](https://github.com/apache/tvm/pull/16768) - [RUNTIME][OPENCL] Bugfix for ciImage create with host ptr
 * [#16672](https://github.com/apache/tvm/pull/16672) - [CLML] Fix build TVM with CLML on MacOS
 * [#16328](https://github.com/apache/tvm/pull/16328) - [RUNTIME][CLML] Fix for Softmax op for 4D tensors
 * [#16394](https://github.com/apache/tvm/pull/16394) - [OpenCL][CMake] Fix OpenCL tests compilation

### ROCm
 * [#16441](https://github.com/apache/tvm/pull/16441) - [WebGPU] Intrin Dispatch: `tanh`, `erf`, `log`
 * [#16404](https://github.com/apache/tvm/pull/16404) - Some fixes of ROCm codegen

### Relax
 * [#16872](https://github.com/apache/tvm/pull/16872) - Enhance symbolic expr estimation in memory planning
 * [#16867](https://github.com/apache/tvm/pull/16867) - Dispatch sort/scan for non-cuda gpu backends
 * [#16852](https://github.com/apache/tvm/pull/16852) - Fix EliminiateCommonSubexpr removing alloc tensor
 * [#16851](https://github.com/apache/tvm/pull/16851) - [Relax,Topi] Allow passing workspace to thrust to avoid allocations
 * [#16841](https://github.com/apache/tvm/pull/16841) - Provide well-formed output in `transform.LazyGetInput`
 * [#16798](https://github.com/apache/tvm/pull/16798) - [Transform] Provide callback versions of LazyTransformParams
 * [#16801](https://github.com/apache/tvm/pull/16801) - Allow DeadCodeElimination within ApplyPassToFunction
 * [#16834](https://github.com/apache/tvm/pull/16834) - Capture symbolic vars in struct info of weights
 * [#16830](https://github.com/apache/tvm/pull/16830) - Share storage allocs among functions after cuda graph rewriting
 * [#16823](https://github.com/apache/tvm/pull/16823) - [VM] Refactor CUDA graph builtins as VM extension
 * [#16828](https://github.com/apache/tvm/pull/16828) - [Bugfix] Provide the full Expr to pattern-match rewriter
 * [#16805](https://github.com/apache/tvm/pull/16805) - [Bugfix]BlockBuilder may not assume unique input functions
 * [#16815](https://github.com/apache/tvm/pull/16815) - Enable capturing symbolic shapes in cuda graph
 * [#16642](https://github.com/apache/tvm/pull/16642) - Allow R.Prim('bool') in relax::If and assert_op
 * [#16796](https://github.com/apache/tvm/pull/16796) - Unit-test for structural equal of recursive function
 * [#16732](https://github.com/apache/tvm/pull/16732) - Allow composition of DFPattern replacements
 * [#16783](https://github.com/apache/tvm/pull/16783) - Improve CanonicalizeBindings in DataflowVar edge case
 * [#16721](https://github.com/apache/tvm/pull/16721) - Implement operators to inspec DLTensor::strides and offset
 * [#16730](https://github.com/apache/tvm/pull/16730) - Refactor PatternRewriter into separate Block/Expr mutators
 * [#16756](https://github.com/apache/tvm/pull/16756) - [IR]Improve highlighting in assert_structural_equal
 * [#16779](https://github.com/apache/tvm/pull/16779) - Improve malform error msg
 * [#16569](https://github.com/apache/tvm/pull/16569) - [Unity][Parser] Check well-formedness in the parser
 * [#16759](https://github.com/apache/tvm/pull/16759) - [Pass] Lowering passes for GPU IPC memory and allreduce
 * [#16697](https://github.com/apache/tvm/pull/16697) - Implement relax.transform.TopologicalSort
 * [#16658](https://github.com/apache/tvm/pull/16658) - Normalize use of void-type variable to inline R.tuple()
 * [#16711](https://github.com/apache/tvm/pull/16711) - [Frontend] Add op `tanh`, `exp`, `negative`, and `permute`
 * [#16703](https://github.com/apache/tvm/pull/16703) - [Fix]Fix top-p/top-k sampling kernel
 * [#16669](https://github.com/apache/tvm/pull/16669) - [Frontend][Onnx] add sum and globalavgpool 1d/3d op
 * [#16691](https://github.com/apache/tvm/pull/16691) - CUDA graph rewrite treating StringImm as static
 * [#16685](https://github.com/apache/tvm/pull/16685) - Implement StructInfoPattern for dataflow pattern matching
 * [#16681](https://github.com/apache/tvm/pull/16681) - [Frontend][Onnx] support MaxPool1/2/3D and AveragePool1/2/3D
 * [#16584](https://github.com/apache/tvm/pull/16584) - [Unity][TIR] Clear struct info when specializing PrimFunc
 * [#16676](https://github.com/apache/tvm/pull/16676) - Remove the legalization of cumsum/cumprob
 * [#16654](https://github.com/apache/tvm/pull/16654) - [Frontend][NN] Add support for Conv3D
 * [#16674](https://github.com/apache/tvm/pull/16674) - Eager free original weights in transform_params
 * [#16675](https://github.com/apache/tvm/pull/16675) - add sample_indices in sampling
 * [#16648](https://github.com/apache/tvm/pull/16648) - [Runtime] Support Unpack API for NDArrayCache
 * [#16591](https://github.com/apache/tvm/pull/16591) - [Unity][Transform] Handle dynamic shapes in CombineParallelMatmul
 * [#16594](https://github.com/apache/tvm/pull/16594) - [Transform] Preserve param names in LiftTransformParams
 * [#16575](https://github.com/apache/tvm/pull/16575) - [Unity] GPU sampling
 * [#16574](https://github.com/apache/tvm/pull/16574) - Additional unit tests for RemoveUnusedParameters
 * [#16585](https://github.com/apache/tvm/pull/16585) - [Unity][Analysis] Include impure call in VerifyWellFormed errors
 * [#16421](https://github.com/apache/tvm/pull/16421) - [Unity][Transform] Raise error in FuseOpsByPattern for SSA violation
 * [#16629](https://github.com/apache/tvm/pull/16629) - Fix error message in BlockBuilder
 * [#16592](https://github.com/apache/tvm/pull/16592) - Handle dynamic arguments in legalization of nn.attention
 * [#16590](https://github.com/apache/tvm/pull/16590) - [Unity][Transform] Check for permute_dims in ExpandMatmulOfSum
 * [#16604](https://github.com/apache/tvm/pull/16604) - [Frontend][Onnx] fix clip unsqueeze opset implement
 * [#16568](https://github.com/apache/tvm/pull/16568) - [Runtime] RNNState for Space State Models
 * [#16563](https://github.com/apache/tvm/pull/16563) - Implement operators to read runtime DLTensor* information
 * [#16581](https://github.com/apache/tvm/pull/16581) - [Unity][MSC][M4.2][Step2] Enable plugin with manager, test plugins in compile pipeline
 * [#16600](https://github.com/apache/tvm/pull/16600) - Expose name_hint field for BlockBuilder.match_cast
 * [#16601](https://github.com/apache/tvm/pull/16601) - [Transform] Canonicalize `let var = R.const` bindings
 * [#16583](https://github.com/apache/tvm/pull/16583) - [Unity][VM] Recursively visit match bindings in VMShapeLowerMutator
 * [#16586](https://github.com/apache/tvm/pull/16586) - Ignore non-relax functions in relax.transform.RunCodegen
 * [#16573](https://github.com/apache/tvm/pull/16573) - [VM] Re-implementation of callback functions
 * [#16561](https://github.com/apache/tvm/pull/16561) - [Bugfix]Remove call to tvm.build for empty TIR module
 * [#16564](https://github.com/apache/tvm/pull/16564) - [Unity] Check for symbolic vars in PrimValue in when lowering to TIR
 * [#16558](https://github.com/apache/tvm/pull/16558) - Minor updates for NN frontend
 * [#16542](https://github.com/apache/tvm/pull/16542) - Support callback as argument
 * [#16487](https://github.com/apache/tvm/pull/16487) - [Unity][Transform] Handle `call_tir_inplace` in `FuseTIR` and `FuseOps`
 * [#16355](https://github.com/apache/tvm/pull/16355) - [Unity] Infer struct info for relax.op.split on dynamic-sized index
 * [#16465](https://github.com/apache/tvm/pull/16465) - [Redo][Unity] Split DecomposeOpsForTraining into two steps
 * [#16495](https://github.com/apache/tvm/pull/16495) - [Unity][MSC][M4.2][Step1] Enable plugin with manager, test plugins in compile pipeline
 * [#16498](https://github.com/apache/tvm/pull/16498) - [Frontent] "tensor_ir_inplace" op
 * [#16500](https://github.com/apache/tvm/pull/16500) - [Unity] Support storage reuse for dynamic shapes
 * [#16493](https://github.com/apache/tvm/pull/16493) - [Pass] Skip data type node for CSE pass
 * [#16467](https://github.com/apache/tvm/pull/16467) - [Unity][MSC][Refactor] Reconstruct BYOC and runner
 * [#16422](https://github.com/apache/tvm/pull/16422) - [Unity][CodeGen] RunCodegen based on externally-exposed functions
 * [#16483](https://github.com/apache/tvm/pull/16483) - [Unity][Frontend] Add Sigmoid and Square Op
 * [#16472](https://github.com/apache/tvm/pull/16472) - [Unity] Improved error message in tvm::relax::UpdateStructInfo
 * [#16473](https://github.com/apache/tvm/pull/16473) - [Unity] Improve error message in tensor_to_shape struct inference
 * [#16466](https://github.com/apache/tvm/pull/16466) - Memory planning for "partially dynamic" shapes
 * [#16464](https://github.com/apache/tvm/pull/16464) - NDArray Cache Update with DLTensor Support
 * [#16315](https://github.com/apache/tvm/pull/16315) - [Unity][Transform] Implement relax.transform.ReorderTakeAfterMatmul
 * [#16313](https://github.com/apache/tvm/pull/16313) - [Unity][Transform] Implement relax.transform.ExpandMatmulOfSum
 * [#16411](https://github.com/apache/tvm/pull/16411) - [Unity][Transform] Handle symbolic variables in LambdaLift
 * [#16443](https://github.com/apache/tvm/pull/16443) - [Unity][FIX] fix thread dtype mismatch
 * [#16442](https://github.com/apache/tvm/pull/16442) - Revert "[Unity] Split DecomposeOpsForTraining into two steps"
 * [#16437](https://github.com/apache/tvm/pull/16437) - [Unity] Improve buffer allocation for handling duplicated buffer names.
 * [#16439](https://github.com/apache/tvm/pull/16439) - [Unity]  Support cumsum with pure int32
 * [#16432](https://github.com/apache/tvm/pull/16432) - [Unity] downgrade cmake version requirement
 * [#16427](https://github.com/apache/tvm/pull/16427) - [Unity][Frontend][NN] Better support for dynamic convolutions
 * [#16418](https://github.com/apache/tvm/pull/16418) - [Unity][Fix] Fix mismatched intrinsic name
 * [#16129](https://github.com/apache/tvm/pull/16129) - [Unity][Transform] Replace eligible operators with in-place versions in dataflow blocks
 * [#16414](https://github.com/apache/tvm/pull/16414) - [Bugfix][Unity] Recover MSVC/NVCC/ROCm/Vulkan
 * [#15954](https://github.com/apache/tvm/pull/15954) - [Unity] Split DecomposeOpsForTraining into two steps
 * [#16111](https://github.com/apache/tvm/pull/16111) - [Unity][Transform] Memory planning for dynamic-shape func return
 * [#16396](https://github.com/apache/tvm/pull/16396) - [Unity] PagedKVCache supporting on-the-fly RoPE calculation
 * [#16395](https://github.com/apache/tvm/pull/16395) - [Frontend][ONNX]fix onnx frontend parse
 * [#16385](https://github.com/apache/tvm/pull/16385) - [Unity][Op] Add Conv3D Operator
 * [#16284](https://github.com/apache/tvm/pull/16284) - [Unity][nnModule] Dynamic shape support in nn Module
 * [#16378](https://github.com/apache/tvm/pull/16378) - [Unity][BlockBuilder] Restore bb.get()
 * [#16374](https://github.com/apache/tvm/pull/16374) - [Unity] Support TIR kernel for PagedKVCache
 * [#16314](https://github.com/apache/tvm/pull/16314) - [Unity][Transform] Implement relax.transform.AdjustMatmulOrder
 * [#16349](https://github.com/apache/tvm/pull/16349) - [Unity][MSC] Avoid depending on trivial bindings in Relax intermediate
 * [#16376](https://github.com/apache/tvm/pull/16376) - [Unity][Contrib] Fix a bug due to typo in vllm `reconstruct_from_cache` kernel and add test
 * [#16388](https://github.com/apache/tvm/pull/16388) - [Unity] Update dispatch test cases following the merge from main
 * [#16335](https://github.com/apache/tvm/pull/16335) - [Unity] Set CMAKE_CUDA_ARCHITECTURES default to native
 * [#16306](https://github.com/apache/tvm/pull/16306) - [Unity][Transform] Update LambdaLift to use name of lifted lambda
 * [#16310](https://github.com/apache/tvm/pull/16310) - [Unity][Analysis] Show objects instead of names in WellFormedChecker
 * [#16362](https://github.com/apache/tvm/pull/16362) - [Unity][Fix] Memory planning check value type of 'tir_var_upper_bound'
 * [#16367](https://github.com/apache/tvm/pull/16367) - [Unity][Transform] Handle replacement at both var binding and usage
 * [#16309](https://github.com/apache/tvm/pull/16309) - [Unity][Transform] Use parameter name in BundleModelParams
 * [#16307](https://github.com/apache/tvm/pull/16307) - [Unity] Improved error message in ExprMutator::ReEmitBinding
 * [#16308](https://github.com/apache/tvm/pull/16308) - [Unity] Improved error message for matmul shape mismatch
 * [#16360](https://github.com/apache/tvm/pull/16360) - [Unity] Enhance Torch-consistency in rehsape
 * [#16350](https://github.com/apache/tvm/pull/16350) - [Unity][Contrib] Add vLLM paged attention kernel
 * [#16303](https://github.com/apache/tvm/pull/16303) - [Unity][NN] Use Linear name for nn.op.permute_dims
 * [#16325](https://github.com/apache/tvm/pull/16325) - [Unity][MSC][Legalize] legalize codes and mute logging
 * [#16312](https://github.com/apache/tvm/pull/16312) - [Unity][Analysis] Add utility for collecting compile-time bindings
 * [#16330](https://github.com/apache/tvm/pull/16330) - [Unity][WEBGPU] Enable wasm exception propagation
 * [#16304](https://github.com/apache/tvm/pull/16304) - [Unity][Analysis] Handle PrimStructInfo in EraseToWellDefined
 * [#16305](https://github.com/apache/tvm/pull/16305) - [Unity][Transform] Implement UpdateParamStructInfo
 * [#16331](https://github.com/apache/tvm/pull/16331) - [Unity] Alter op impl handling empty transform for output
 * [#16254](https://github.com/apache/tvm/pull/16254) - [Unity] Dispatch cumsum and sort
 * [#16120](https://github.com/apache/tvm/pull/16120) - [Unity][Transform] Extract partial-tuple-usage from FuseTIR
 * [#16311](https://github.com/apache/tvm/pull/16311) - [Unity] Validate struct info in relax::Call constructor
 * [#16333](https://github.com/apache/tvm/pull/16333) - [Unity] Fix nn.op.tensor_ir_op signature
 * [#16302](https://github.com/apache/tvm/pull/16302) - [Unity] Cutlass kernel compatibility with cmake 3.18+

### Relay
 * [#16622](https://github.com/apache/tvm/pull/16622) - [ONNX] Fix the attribute mode parse of operator Upsample
 * [#16626](https://github.com/apache/tvm/pull/16626) - [ONNX] Fix the Resize operator in ONNX frontend
 * [#16624](https://github.com/apache/tvm/pull/16624) - [ONNX] fix the wrong default value about dtype in Multinomial converter
 * [#16417](https://github.com/apache/tvm/pull/16417) - [Frontend][Torch] fix pytorch frontend linspace op
 * [#16400](https://github.com/apache/tvm/pull/16400) - [Frontend][Torch] fix pytorch frontend not support logical or
 * [#16390](https://github.com/apache/tvm/pull/16390) - [Frontend][Torch] fix a typo mistake in nonzero_numpy
 * [#16324](https://github.com/apache/tvm/pull/16324) - make "ToScalar" support directly obtaining "int64_t"

### Runtime
 * [#16804](https://github.com/apache/tvm/pull/16804) - Introduce MSCCLPP with NCCL equivalent interface
 * [#16809](https://github.com/apache/tvm/pull/16809) - Add "TVM_DLL" to NVTX header
 * [#16750](https://github.com/apache/tvm/pull/16750) - CUDA IPC Memory support and custom allreduce kernels
 * [#16738](https://github.com/apache/tvm/pull/16738) - [Refactor]Always specify device in allocator interface
 * [#16716](https://github.com/apache/tvm/pull/16716) - Ensure NDArray.CopyTo(Device) always sync
 * [#16705](https://github.com/apache/tvm/pull/16705) - Add TVM_DLL to memory manager functions
 * [#16692](https://github.com/apache/tvm/pull/16692) - PagedKVCache execute data copy on a separate stream
 * [#16647](https://github.com/apache/tvm/pull/16647) - [RPC] Fix FreeObject in minrpc server
 * [#16667](https://github.com/apache/tvm/pull/16667) - [Builtin] Using float32 accumulation in attention kernel
 * [#16635](https://github.com/apache/tvm/pull/16635) - [RPC] Enable RPCObjectRef over multi-hop RPC
 * [#16630](https://github.com/apache/tvm/pull/16630) - Add TVM_DLL to threading backend funcs
 * [#16541](https://github.com/apache/tvm/pull/16541) - Add "TVM_DLL" to NDArray cache load func
 * [#16550](https://github.com/apache/tvm/pull/16550) - [ROCM] Properly align rocm parameter buffer
 * [#16545](https://github.com/apache/tvm/pull/16545) - Fix dtype conversion for bf16 and fp8
 * [#16508](https://github.com/apache/tvm/pull/16508) - ParallelFor skipping thread backend for unit extent
 * [#16486](https://github.com/apache/tvm/pull/16486) - KV cache providing workspace for attn kernel
 * [#16456](https://github.com/apache/tvm/pull/16456) - [KVCache] AttentionWithFusedQKV and RoPE mode
 * [#16415](https://github.com/apache/tvm/pull/16415) - [Memory] Implement support for non-zero offset within a storage object in AllocNDArr…
 * [#16387](https://github.com/apache/tvm/pull/16387) - [RPC] Enable RPCObjectRef return in RPC
 * [#16377](https://github.com/apache/tvm/pull/16377) - Use cudaGetDeviceCount to check if device exists

### TIR
 * [#16832](https://github.com/apache/tvm/pull/16832) - Use constructor for new PrimFunc in TransformLayout
 * [#16543](https://github.com/apache/tvm/pull/16543) - Fix segfaults from ordering of Let/Assert in MakePackedAPI
 * [#16795](https://github.com/apache/tvm/pull/16795) - Ramp and Broadcast lanes fixed to int32 dtype
 * [#16767](https://github.com/apache/tvm/pull/16767) - [Driver] Use `BindTarget` to specify target for FP8 legalization
 * [#16742](https://github.com/apache/tvm/pull/16742) - [Bugfix]Fix cache_read update buffer region
 * [#16726](https://github.com/apache/tvm/pull/16726) - [Bugfix]Avoid overwrite of unmanaged buffer allocations
 * [#16548](https://github.com/apache/tvm/pull/16548) - [CUDA] Add native FP8 support to codegen
 * [#16723](https://github.com/apache/tvm/pull/16723) - Implement max/min_value for fp8 data types
 * [#16655](https://github.com/apache/tvm/pull/16655) - Improve well-formed check's handling of match buffer
 * [#16673](https://github.com/apache/tvm/pull/16673) - Support Vector Reinterpret Calls
 * [#16682](https://github.com/apache/tvm/pull/16682) - [Bugfix]Handle AttrStmt of upcoming tir.Var in ConvertSSA
 * [#16560](https://github.com/apache/tvm/pull/16560) - Enhance and fix tensorize schedule for some case
 * [#16660](https://github.com/apache/tvm/pull/16660) - [Bugfix]Fix duplicate AllocateConst in CacheReadWrite schedule primitive
 * [#16544](https://github.com/apache/tvm/pull/16544) - Expand debug symbol output for CodeGenLLVM
 * [#16553](https://github.com/apache/tvm/pull/16553) - Fix get_block_access_region for let bindings
 * [#16515](https://github.com/apache/tvm/pull/16515) - Require exactly same-dtype matching for Vulkan smem reuse
 * [#16406](https://github.com/apache/tvm/pull/16406) - Fix of inter thread reduction with shared memory prefetch
 * [#16293](https://github.com/apache/tvm/pull/16293) - Extend DP4A tensor intrin
 * [#16345](https://github.com/apache/tvm/pull/16345) - Allow sync threads inside condition
 * [#16250](https://github.com/apache/tvm/pull/16250) - In SplitHostDevice, check for variables in thread extents
 * [#16184](https://github.com/apache/tvm/pull/16184) - [Transform] Implement InlinePrivateFunctions

### TOPI
 * [#16652](https://github.com/apache/tvm/pull/16652) - improve inclusive_scan for thrust
 * [#16383](https://github.com/apache/tvm/pull/16383) - [Target] Add fp16 SIMD support for conv2d on `arm_cpu` targets

### TVMC
 * [#16261](https://github.com/apache/tvm/pull/16261) - Add tvmc flag to print ir before and print ir after named pass

### TVMScript
 * [#16864](https://github.com/apache/tvm/pull/16864) - Add parser and printer support for e4m3/e5m2 fp8
 * [#16844](https://github.com/apache/tvm/pull/16844) - Produce empty DictAttrs when R.func_attrs is absent
 * [#16811](https://github.com/apache/tvm/pull/16811) - Do not throw error for duplicate definitions
 * [#16641](https://github.com/apache/tvm/pull/16641) - Allow use of relax.Expr with void type as a statement
 * [#16663](https://github.com/apache/tvm/pull/16663) - Infer T.reads() for DeclBuffer nodes
 * [#16640](https://github.com/apache/tvm/pull/16640) - Represent tir::builtin::ret() using python "return"
 * [#16562](https://github.com/apache/tvm/pull/16562) - [Bugfix]Handle R.match_cast as last binding in if/else
 * [#16593](https://github.com/apache/tvm/pull/16593) - [Unity]Parse R.Object return type from call_pure_packed
 * [#16356](https://github.com/apache/tvm/pull/16356) - [Unity]Optionally hide StructInfo that can be inferred
 * [#16379](https://github.com/apache/tvm/pull/16379) - [Unity]Update `call_packed` semantics to support empty sinfo_args

### Vulkan
 * [#16858](https://github.com/apache/tvm/pull/16858) - Fix CLZ support for Vulkan

### cuda & cutlass & tensorrt
 * [#16865](https://github.com/apache/tvm/pull/16865) - [Codegen, CUDA] Add handling of fp8 broadcast / const
 * [#16818](https://github.com/apache/tvm/pull/16818) - [Cutlass] Fix usage of cuda stream for group gemm
 * [#16788](https://github.com/apache/tvm/pull/16788) - [Cutlass] Add check for group gemm param shapes
 * [#16789](https://github.com/apache/tvm/pull/16789) - [Bugfix][Cutlass] Remove a typo in cutlass build
 * [#16787](https://github.com/apache/tvm/pull/16787) - [Codegen, Cuda] Add overload for fp8x4 e5m2 <-> half4 conversion
 * [#16751](https://github.com/apache/tvm/pull/16751) - [Cutlass] Add group gemm kernels
 * [#16736](https://github.com/apache/tvm/pull/16736) - [Target][CUDA] Allow non-numeric arch as needed for latest gpu
 * [#16619](https://github.com/apache/tvm/pull/16619) - [Bugfix][Cutlass] Check if function attributes is None
 * [#16342](https://github.com/apache/tvm/pull/16342) - [CUDA] Simple extend to optimize reuse for static shared memory.
 * [#16342](https://github.com/apache/tvm/pull/16342) - [CUDA] Simple extend to optimize reuse for static shared memory.
 * [#16342](https://github.com/apache/tvm/pull/16342) - [CUDA] Simple extend to optimize reuse for static shared memory.
 * [#16342](https://github.com/apache/tvm/pull/16342) - [CUDA] Simple extend to optimize reuse for static shared memory.
 * [#16342](https://github.com/apache/tvm/pull/16342) - [CUDA] Simple extend to optimize reuse for static shared memory.

### micoNPU
 * [#16266](https://github.com/apache/tvm/pull/16266) - [microNPU][ETHOSU] Add fixed point for tanh
 * [#16680](https://github.com/apache/tvm/pull/16680) - [microNPU][ETHOSU] Fix LUT size for int16 activations
 * [#16401](https://github.com/apache/tvm/pull/16401) - [microNPU][ETHOSU] Add fixed point for matmul

### web
 * [#16733](https://github.com/apache/tvm/pull/16733) - Support web indexDB cache for larger model storage
 * [#16810](https://github.com/apache/tvm/pull/16810) - Support building tvm/web on Windows
 * [#16825](https://github.com/apache/tvm/pull/16825) - Allow custom bc files in emcc making
 * [#16791](https://github.com/apache/tvm/pull/16791) - Add `kv_state` and `rnn_state` to wasm_runtime
 * [#16722](https://github.com/apache/tvm/pull/16722) - Implement linear congruential generator, make runtime seedable
 * [#16650](https://github.com/apache/tvm/pull/16650) - Seperate parallel shard download and iterative shard loading
 * [#16694](https://github.com/apache/tvm/pull/16694) - Initial support for asyncify
 * [#16631](https://github.com/apache/tvm/pull/16631) - Fix NDArrayCache loading report callback
 * [#16525](https://github.com/apache/tvm/pull/16525) - Move ArtifactCache to Interface, Support Cache delete and Batch Delete, Remove typo
 * [#16554](https://github.com/apache/tvm/pull/16554) - Compatibility with PagedKVCache in WebGPU
 * [#16527](https://github.com/apache/tvm/pull/16527) - Revert "[Unity]Temp disable wasm exception (#16444)"
 * [#16504](https://github.com/apache/tvm/pull/16504) - [Relax]Add ApplyPresenceAndRequencyPenalty
 * [#16485](https://github.com/apache/tvm/pull/16485) - [wasm] Enlarge initial memory for emcc
 * [#16444](https://github.com/apache/tvm/pull/16444) - [Unity]Temp disable wasm exception

### Misc
 * [#16873](https://github.com/apache/tvm/pull/16873) - [Thrust] Fix thrust workspace allocation
 * [#16868](https://github.com/apache/tvm/pull/16868) - [3rdparty] Bump flashinfer
 * [#16871](https://github.com/apache/tvm/pull/16871) - [PageKV] allow PopN to pop all the tokens in last block
 * [#16866](https://github.com/apache/tvm/pull/16866) - [3rdparty] Bump FlashInfer
 * [#16863](https://github.com/apache/tvm/pull/16863) - [Picojson] Let the key of objects in json be ordered by default
 * [#16856](https://github.com/apache/tvm/pull/16856) - [Thrust] Use pointer to tls pool to prevent creating new pool
 * [#16850](https://github.com/apache/tvm/pull/16850) - Fixing probability comment
 * [#16849](https://github.com/apache/tvm/pull/16849) - [KVCache] Initialize one extra page than specified
 * [#16843](https://github.com/apache/tvm/pull/16843) - [IR] Provide well-formed intermediate in ApplyPassToFunction
 * [#16772](https://github.com/apache/tvm/pull/16772) - [MSC][M5.3] Support torch.dynamo for dynamic models
 * [#16839](https://github.com/apache/tvm/pull/16839) - Bump pillow from 10.2.0 to 10.3.0 in /apps/microtvm/cmsisnn
 * [#16838](https://github.com/apache/tvm/pull/16838) - Bump pillow from 10.2.0 to 10.3.0 in /apps/microtvm/ethosu
 * [#16831](https://github.com/apache/tvm/pull/16831) - [KVCache] Reducing CacheAuxDataManager copy size
 * [#16794](https://github.com/apache/tvm/pull/16794) - [SME] Target parser support for SME
 * [#16824](https://github.com/apache/tvm/pull/16824) - [KVCache] Introducing auxiliary data manager
 * [#16800](https://github.com/apache/tvm/pull/16800) - [BugTIR]fix error merging shared memory for ptx_cp_async
 * [#16822](https://github.com/apache/tvm/pull/16822) - [VM] Recycle VMFrame
 * [#16813](https://github.com/apache/tvm/pull/16813) - [KVCache] Support forking sequence at specific posotion
 * [#16786](https://github.com/apache/tvm/pull/16786) - [Codegen] Add check to disable invalid reinterpret
 * [#16816](https://github.com/apache/tvm/pull/16816) - [Cmake] Allow using custom CCCL path for thrust
 * [#16784](https://github.com/apache/tvm/pull/16784) - [SLM] Add unit tests for SLM to Relax exporter
 * [#16814](https://github.com/apache/tvm/pull/16814) - Fix includes of custom allreduce kernel
 * [#16806](https://github.com/apache/tvm/pull/16806) - [Debug] Improve error message in VMShapeLower
 * [#16802](https://github.com/apache/tvm/pull/16802) - [Debug] Improve error messages in LiftTransformParams
 * [#16425](https://github.com/apache/tvm/pull/16425) - [Target] Use LLVM target parser for determining Arm(R) A-Profile Architecture features
 * [#16797](https://github.com/apache/tvm/pull/16797) - [3rdparty] AUTO mode for custom all-reduce strategy
 * [#16761](https://github.com/apache/tvm/pull/16761) - [SME] Add support for inserting processor state annotations
 * [#16778](https://github.com/apache/tvm/pull/16778) - [Analysis] Allow calls to GlobalVar in @R.function
 * [#16745](https://github.com/apache/tvm/pull/16745) - [IR] Default to empty attributes, instead of NULL
 * [#16777](https://github.com/apache/tvm/pull/16777) - Revert "[SLM] Allow modules to define pre-processing of weights"
 * [#16776](https://github.com/apache/tvm/pull/16776) - [Contrib] Remove thrust "built but not used" warning
 * [#16757](https://github.com/apache/tvm/pull/16757) - [SLM] Allow modules to define pre-processing of weights
 * [#16763](https://github.com/apache/tvm/pull/16763) - [CONTRIB] Add nm symbol dump
 * [#16717](https://github.com/apache/tvm/pull/16717) - Enable Shared Function in LiftTransformParam Pass
 * [#16729](https://github.com/apache/tvm/pull/16729) - [Builtin] Sliding window and sink support for PagedKVCache
 * [#16724](https://github.com/apache/tvm/pull/16724) - Fix cpp_rtvm cmake build on Windows
 * [#16513](https://github.com/apache/tvm/pull/16513) - [Target] Automatically detect system triple when not specified by the user
 * [#16710](https://github.com/apache/tvm/pull/16710) - [CMake] Add "USE_FLASHINFER" to libinfo
 * [#16702](https://github.com/apache/tvm/pull/16702) - [MSC][M5.2] Enable quantize && prune with gym by wrapper
 * [#16699](https://github.com/apache/tvm/pull/16699) - [Transform] Remove R.Object parameters after LazyTransformParams
 * [#16668](https://github.com/apache/tvm/pull/16668) - [MSC][M5.1] Build wrapper to support compression
 * [#16693](https://github.com/apache/tvm/pull/16693) - [Contrib] Support NDArray cache taking generator
 * [#16412](https://github.com/apache/tvm/pull/16412) - [Lint] Add check to prevent usage of #include <regex>
 * [#16689](https://github.com/apache/tvm/pull/16689) - [DeviceAPI] Support "GetCurrentStream"
 * [#16690](https://github.com/apache/tvm/pull/16690) - Use target name instead of node name as function name
 * [#16683](https://github.com/apache/tvm/pull/16683) - [skip ci] Fix wasm exception flag
 * [#16609](https://github.com/apache/tvm/pull/16609) - Minor update docs instructions
 * [#16656](https://github.com/apache/tvm/pull/16656) - Simplify Windows CMake Command
 * [#16666](https://github.com/apache/tvm/pull/16666) - [KVCache] Fix the reference counter in sequence fork
 * [#16662](https://github.com/apache/tvm/pull/16662) - Fixing workload comment
 * [#16595](https://github.com/apache/tvm/pull/16595) - [Transform] Check for zero-param operators in LiftTransformParams
 * [#16599](https://github.com/apache/tvm/pull/16599) - [Transform] De-duplicate MatchCast nodes in EliminateCommonSubexpr
 * [#16596](https://github.com/apache/tvm/pull/16596) - [Transform] Implement relax.transform.ReorderPermuteDimsAfterConcat
 * [#16597](https://github.com/apache/tvm/pull/16597) - [Transform] Allow explicit name of bundled model parameters
 * [#16602](https://github.com/apache/tvm/pull/16602) - [Transform] Improvements to LazyTransformParams
 * [#16606](https://github.com/apache/tvm/pull/16606) - [KVCache] Support passing in attn_score_scaling_factor into KV cache
 * [#16608](https://github.com/apache/tvm/pull/16608) - Extend gpu memory bandwidth test to work through RPC
 * [#16587](https://github.com/apache/tvm/pull/16587) - [Debug] Improve error message for codegen pattern mismatches
 * [#16570](https://github.com/apache/tvm/pull/16570) - [Marvell BYOC]: Marvell AI Accelerator Integration - Phase 1
 * [#16576](https://github.com/apache/tvm/pull/16576) - Update the 3rdparty/libflash_attn submodule
 * [#16580](https://github.com/apache/tvm/pull/16580) - [KVCache] Support mode "None" for Rotary Embebdding
 * [#16578](https://github.com/apache/tvm/pull/16578) - [KVCache] Support returning query positions
 * [#16571](https://github.com/apache/tvm/pull/16571) - Fix compile warnings
 * [#16540](https://github.com/apache/tvm/pull/16540) - [Upd] Enable lld search to include /opt/rocm/llvm/bin for rocm
 * [#16539](https://github.com/apache/tvm/pull/16539) - Improve error message in NDArray::CopyFromTo
 * [#16524](https://github.com/apache/tvm/pull/16524) - [Build] Improving debug and build-dir options
 * [#16551](https://github.com/apache/tvm/pull/16551) - [KVCache] Fix attention kernel for ROCm
 * [#16512](https://github.com/apache/tvm/pull/16512) - Cut pytest-lazy-fixture
 * [#16506](https://github.com/apache/tvm/pull/16506) - Bump 3rdparty/cutlass_fpA_intB_gemm version
 * [#16511](https://github.com/apache/tvm/pull/16511) - [Minor] Fix Clang compilation warning in fuse_tir.cc and codegen_c_host.cc
 * [#16516](https://github.com/apache/tvm/pull/16516) - Add Relax, Unity Tags in make_notes.py
 * [#16497](https://github.com/apache/tvm/pull/16497) - [Instrument] Add default instrument to print all passes
 * [#16494](https://github.com/apache/tvm/pull/16494) - [DPL] Support tir_vars field in is_call_tir pattern
 * [#16453](https://github.com/apache/tvm/pull/16453) - Bump pillow from 10.0.1 to 10.2.0 in /apps/microtvm
 * [#16454](https://github.com/apache/tvm/pull/16454) - [BugTIR] fix thread_sync occurs in letstmt
 * [#16468](https://github.com/apache/tvm/pull/16468) - [LINT] Fix pylint issues in test_dma_builtin.py
 * [#16413](https://github.com/apache/tvm/pull/16413) - [Contrib] Workspace for cuBLAS backend
 * [#16460](https://github.com/apache/tvm/pull/16460) - [Cherry-pick][MSC][M4.1] Add plugin && plugin_builder, enable build and test in different frameworks (#16397)
 * [#16461](https://github.com/apache/tvm/pull/16461) - [Minor] Fix Docstring for sphinx-build
 * [#16431](https://github.com/apache/tvm/pull/16431) - [Schedule] Loop-Partition Scheduling Primitive
 * [#16451](https://github.com/apache/tvm/pull/16451) - Bump pillow from 10.0.1 to 10.2.0 in /apps/microtvm/ethosu
 * [#16452](https://github.com/apache/tvm/pull/16452) - Bump pillow from 10.0.1 to 10.2.0 in /apps/microtvm/cmsisnn
 * [#16445](https://github.com/apache/tvm/pull/16445) - [skip ci] update branch rule to prepare for unity transition
 * [#16426](https://github.com/apache/tvm/pull/16426) - [CMake] Enable cuda lang if USE_CUDA is on
 * [#16407](https://github.com/apache/tvm/pull/16407) - Add NVIDIA Hopper H100 target tag
 * [#16398](https://github.com/apache/tvm/pull/16398) - [DeviceAPI] Support querying total global memory
 * [#16357](https://github.com/apache/tvm/pull/16357) - [RPC] Fix tuning on macOS and Windows (#15771)
 * [#16386](https://github.com/apache/tvm/pull/16386) - [Thrust] Use no sync exec policy and caching allocator
 * [#16343](https://github.com/apache/tvm/pull/16343) - [CMake][MSVC] Disable permissive mode for MSVC builds
 * [#16242](https://github.com/apache/tvm/pull/16242) - [Codegen] Fix if_then_else codegen
 * [#16341](https://github.com/apache/tvm/pull/16341) - [CMake] Use ccache as CMAKE_CUDA_COMPILER_LAUNCHER
 * [#16332](https://github.com/apache/tvm/pull/16332) - Change metal dtype of ceil_log2 to fp32

## v0.17.0 (2024-07-20)

# Introduction

The TVM community has worked since the v0.17.0 release to deliver the following new exciting improvements! This release version is:

The main tags are below (**bold text is with lots of progress**):

- Community, RFCs
- AOT, Hexagon， OpenCL & CLML, Web, Metal
- **Relax**, **Dlight**, **Disco**
- TIR, TVMScript
- Docs, CI, **Misc**, **BugFix**

Please visit the full listing of commits for a complete view: [v0.17.dev0...v0.17.0.rc0](https://github.com/apache/tvm/compare/v0.17.dev0...v0.17.0.rc0).

### Community

 * [#17018](https://github.com/apache/tvm/pull/17018) - New committer: Balint Cristian

 ### RFCs

This new RFC added an open, standardized format for neural network exchange developed by the Khronos Group since 2018 (https://www.khronos.org/nnef). It is aimed at deploying trained neural networks from deep learning frameworks to proprietary inference engines of neural network hardware vendors.

 * [#108](https://github.com/apache/tvm-rfcs/pull/108) - [RFC] Add NNEF frontend

----

### AOT
 * [#17077](https://github.com/apache/tvm/pull/17077) - Correctly calculate workspace for vector types

### Adreno
 * [#16927](https://github.com/apache/tvm/pull/16927) - [SCRIPT]Fix in build config for adreno

### BYOC
 * [#16895](https://github.com/apache/tvm/pull/16895) - Add layout check and update shape check for cublas FP8 BYOC

### BugFix
 * [#17138](https://github.com/apache/tvm/pull/17138) - [Fix][TIR] Fix outdated call to create extern buffer in make_extern
 * [#17132](https://github.com/apache/tvm/pull/17132) - Restrict CopyOnWrite to _type_final
 * [#17096](https://github.com/apache/tvm/pull/17096) - Update FAttrsGetter to return Map<String, ObjectRef>
 * [#17078](https://github.com/apache/tvm/pull/17078) - [NCCL] Release NCCL thread_local resources in destructor
 * [#17044](https://github.com/apache/tvm/pull/17044) - [Support] Fix copy constructor for support::OrderedSet
 * [#17000](https://github.com/apache/tvm/pull/17000) - [MSC] split name_string with index by colon from the right
 * [#16923](https://github.com/apache/tvm/pull/16923) - [Fix][Dlight] Fix GeneralReduction for log-sum-exp
 * [#16924](https://github.com/apache/tvm/pull/16924) - [Fix] Fix SSA conversion for SizeVar retention
 * [#16903](https://github.com/apache/tvm/pull/16903) - CudaDeviceAPI::GetAttr may check kExist when GPUs absent
 * [#16901](https://github.com/apache/tvm/pull/16901) - rocm shared memory issue on MI250

### CI
 * [#17055](https://github.com/apache/tvm/pull/17055) - [SME][Test] Add additional conv2d tests for asymmetric parameters
 * [#17007](https://github.com/apache/tvm/pull/17007) - [TOPI][Testing] Enable conv2d NHWC fp16 topi testing for `arm_cpu`
 * [#16930](https://github.com/apache/tvm/pull/16930) - [UnitTest] Use pytest's scope='session' for tvm.testing.parameter
 * [#16948](https://github.com/apache/tvm/pull/16948) - Update image tag to 20240428-060115-0b09ed018
 * [#16931](https://github.com/apache/tvm/pull/16931) - Use LLVM17 for tests on `ci_cpu`
 * [#16942](https://github.com/apache/tvm/pull/16942) - Enable Conda setup v3
 * [#16939](https://github.com/apache/tvm/pull/16939) - Upgrade CUDA to 12.4

### CRT
 * [#17097](https://github.com/apache/tvm/pull/17097) - [Bugfix]Return error code on error from ModuleGetFunction

### Disco
 * [#17035](https://github.com/apache/tvm/pull/17035) - [QoL] Implement broadcast/scatter methods for Session
 * [#16992](https://github.com/apache/tvm/pull/16992) - [Bugfix]Handle NDArray larger than OS buffer for pipe
 * [#16978](https://github.com/apache/tvm/pull/16978) - Implement `num_workers` property for `disco.Session`
 * [#16989](https://github.com/apache/tvm/pull/16989) - Treat hangup of disco worker process as kShutdown
 * [#16993](https://github.com/apache/tvm/pull/16993) - Allow allocation that only exists on worker0
 * [#16979](https://github.com/apache/tvm/pull/16979) - Expose disco.Session.shutdown through the python API
 * [#16919](https://github.com/apache/tvm/pull/16919) - Improve error message for CallPacked

### Dlight
 * [#17082](https://github.com/apache/tvm/pull/17082) - Use 16x32 spatial x reduction thread extents in GEMV scheduling
 * [#17052](https://github.com/apache/tvm/pull/17052) - Skip GEMV rules when more than one vector
 * [#17026](https://github.com/apache/tvm/pull/17026) - Perf improvement for low_batch_gemv on Metal
 * [#17016](https://github.com/apache/tvm/pull/17016) - Update Adreno GEMV Rules
 * [#16972](https://github.com/apache/tvm/pull/16972) - [GPU] Enhance opencl thread limit for schedules
 * [#16973](https://github.com/apache/tvm/pull/16973) - [GPU] Improved gemv outer fallback schedule
 * [#16958](https://github.com/apache/tvm/pull/16958) - Check for target in function attributes
 * [#16894](https://github.com/apache/tvm/pull/16894) - Enhance vectorization for gpu matmul
 * [#16884](https://github.com/apache/tvm/pull/16884) - Add check for matmul dtype and fix reduction rule

### Docs
 * [#17146](https://github.com/apache/tvm/pull/17146) - [DOC] Fix typo for the "We utilize the intermediate representation of nn.Graph to convert the OneFlow model to Reley."
 * [#17015](https://github.com/apache/tvm/pull/17015) - [DOC] Update Model Links to Include Commit

### Frontend
 * [#17014](https://github.com/apache/tvm/pull/17014) - [ArgParse] Pass default values to target compiler(#13264)
 * [#16961](https://github.com/apache/tvm/pull/16961) - [Bugfix][ONNX] Improve broadcast and batch_matmul conversion
 * [#16936](https://github.com/apache/tvm/pull/16936) - [TFLite] Add support for GELU conversion

### Hexagon
 * [#17123](https://github.com/apache/tvm/pull/17123) - Add support for v75

### LLVM
 * [#17046](https://github.com/apache/tvm/pull/17046) - [Arith][SVE] Add rewrite rules for indices split by scalable expressions
 * [#16966](https://github.com/apache/tvm/pull/16966) - [SVE] Add support for representing and creating buffer-level predicates
 * [#17001](https://github.com/apache/tvm/pull/17001) - [SVE] Use only powers of two as possible vscale values
 * [#16962](https://github.com/apache/tvm/pull/16962) - [SVE] Add codegen support for `vscale_range()` function attribute
 * [#16968](https://github.com/apache/tvm/pull/16968) - Stringref API deprecation fixes
 * [#16965](https://github.com/apache/tvm/pull/16965) - [SVE] Add get_active_lane_mask builtin
 * [#16899](https://github.com/apache/tvm/pull/16899) - [SVE][TOPI] Add conv2d NHWC hybrid SVE schedule for `arm_cpu`
 * [#16893](https://github.com/apache/tvm/pull/16893) - [SVE] Check for SVE target in VectorizeLoop
 * [#16862](https://github.com/apache/tvm/pull/16862) - [SVE] Support splitting by vscale in `tir::split` and `te::split`

### MetaSchedule
 * [#17012](https://github.com/apache/tvm/pull/17012) - [BugFix]MultiLevelTilingTensorCore generates inconsistent thread-binding sketch for batched matmul
 * [#17066](https://github.com/apache/tvm/pull/17066) - [BugFix]Fix TensorIntrin ‘dot_4x4_i8i8s32_sdot’ is not registered

### Metal
 * [#17059](https://github.com/apache/tvm/pull/17059) - Enable Debug Label
 * [#17025](https://github.com/apache/tvm/pull/17025) - Support metal device profiling

### OpenCL & CLML
 * [#16933](https://github.com/apache/tvm/pull/16933) - [CLML] Fix in clml pattern check condition
 * [#16929](https://github.com/apache/tvm/pull/16929) - [VM][OPENCL] Take advantage of OpenCL host ptr for improved copy

### ROCm
 * [#17141](https://github.com/apache/tvm/pull/17141) - [Backend]Fix error when building TVM with LLVM 19

### Relax
 * [#17139](https://github.com/apache/tvm/pull/17139) - Fix cublas dispatch for corner cases
 * [#17127](https://github.com/apache/tvm/pull/17127) - [KVCache] Support fork in sliding window sink part
 * [#17115](https://github.com/apache/tvm/pull/17115) - Support `input_axis_separator` to allow 2D to 1D conversion
 * [#17119](https://github.com/apache/tvm/pull/17119) - [Bugfix]Set purity=false for LazySetOutput
 * [#17118](https://github.com/apache/tvm/pull/17118) - [VM] Improved error messages for mismatched parameter count
 * [#17110](https://github.com/apache/tvm/pull/17110) - Alloc BYOC workspace with R.builtin.alloc_tensor
 * [#17089](https://github.com/apache/tvm/pull/17089) - [ONNX] Add support for HardSigmoid
 * [#17100](https://github.com/apache/tvm/pull/17100) -  [KVCache] Unlimited depth blocks
 * [#17075](https://github.com/apache/tvm/pull/17075) - [Transform] Modify FuseTIR pass to propagate buffer attributes
 * [#17088](https://github.com/apache/tvm/pull/17088) - [ONNX] Add support for HardSwish
 * [#17085](https://github.com/apache/tvm/pull/17085) - [PyTorch] Add support for torch.nn.Hardsigmoid
 * [#17083](https://github.com/apache/tvm/pull/17083) - [TVMScript]Preserve tir.SizeVar through TVMScript round-trip
 * [#17086](https://github.com/apache/tvm/pull/17086) - Ignore dynamic parameters in RewriteDataflowReshape
 * [#17084](https://github.com/apache/tvm/pull/17084) - [PyTorch] Add support for torch.nn.Hardswish
 * [#17074](https://github.com/apache/tvm/pull/17074) - [KVCache][Test] Fix TIR attn kernels for uncommon group size
 * [#17067](https://github.com/apache/tvm/pull/17067) - Add missing white spaces in error messages
 * [#17061](https://github.com/apache/tvm/pull/17061) - [Frontend][Onnx] Cast Op special handling for ShapeExpr input
 * [#17033](https://github.com/apache/tvm/pull/17033) - [Bugfix] Apply FuseOps to nested DataflowBlock
 * [#17032](https://github.com/apache/tvm/pull/17032) - [Bugfix] Annotate ComputePrimValue output as host function
 * [#17034](https://github.com/apache/tvm/pull/17034) - [Bugfix] Bind symbolic variables in R.match_cast
 * [#16960](https://github.com/apache/tvm/pull/16960) -  [UnitTest] Validate IRModule with multiple targets
 * [#16995](https://github.com/apache/tvm/pull/16995) - [KVCache] Support KVCache decode from forked sequence and pop more tokens
 * [#16959](https://github.com/apache/tvm/pull/16959) - [Transform] Handle identical PrimFunc with distinct VDevice
 * [#16589](https://github.com/apache/tvm/pull/16589) - [Unity] Check for transpose and dynamic shape in AdjustMatmulOrder
 * [#16988](https://github.com/apache/tvm/pull/16988) - [KVCache] Fix the aux data syncing order of paged KV cache
 * [#16922](https://github.com/apache/tvm/pull/16922) - [BugFix]change FuseOpsByPattern strategy to pattern-match maximal subgraph
 * [#16982](https://github.com/apache/tvm/pull/16982) - [Unity][BYOC] Use arith.Analyzer to check batch equality of matmul in cublas
 * [#16955](https://github.com/apache/tvm/pull/16955) - Implement relax.op.view
 * [#16971](https://github.com/apache/tvm/pull/16971) - Support nested ModuleList in nn.Module
 * [#16826](https://github.com/apache/tvm/pull/16826) - Express dynamic arguments of strided_slice as arguments
 * [#16476](https://github.com/apache/tvm/pull/16476) - [Unity][Cutlass] Fix C source generation of dense operation
 * [#16940](https://github.com/apache/tvm/pull/16940) - Allow PrimValue as index in relax.op.take
 * [#16934](https://github.com/apache/tvm/pull/16934) - [TIR] Introduce new `cumsum` op for gpu
 * [#16859](https://github.com/apache/tvm/pull/16859) - [QoL]Use SeqExpr in IR types when SeqExpr is required
 * [#16904](https://github.com/apache/tvm/pull/16904) - Prevent to generate duplicate func in dispatch_sort_scan
 * [#16905](https://github.com/apache/tvm/pull/16905) - [Bugfix]Raise exception for OOM allocation
 * [#16827](https://github.com/apache/tvm/pull/16827) - Handle binary operations between Tensor and PrimValue
 * [#16902](https://github.com/apache/tvm/pull/16902) - Allow specifying entry_funcs for BYOC
 * [#16860](https://github.com/apache/tvm/pull/16860) - [QoL]Infer StructInfo for relax::Tuple on construction
 * [#16861](https://github.com/apache/tvm/pull/16861) - [QoL]Return well-formed IR from relax::Function::CreateEmpty
 * [#16886](https://github.com/apache/tvm/pull/16886) - [Frontend] Fix sort, argsort and topk in nn module
 * [#16883](https://github.com/apache/tvm/pull/16883) - Stabilize relax pass mutation order

### Relay
 * [#16983](https://github.com/apache/tvm/pull/16983) - [BugFix]skip leaf args when matching 'path' part for dominator pattern
 * [#16996](https://github.com/apache/tvm/pull/16996) - fixed to make TupleGetItem inherits the previous span

### Runtime
 * [#17057](https://github.com/apache/tvm/pull/17057) - Stateless interface of PagedKVCache leaf node commit
 * [#17049](https://github.com/apache/tvm/pull/17049) - Support PagedKVCache with tree attention
 * [#17045](https://github.com/apache/tvm/pull/17045) - Fix PagedKVCache for PopN and enhance tests
 * [#16998](https://github.com/apache/tvm/pull/16998) - Compatibility with dmlc::Stream API changes
 * [#17037](https://github.com/apache/tvm/pull/17037) - [ROCm] Enable ROCm host memory support
 * [#17036](https://github.com/apache/tvm/pull/17036) - Use preferred host memory (pinned memory) in KV cache
 * [#16994](https://github.com/apache/tvm/pull/16994) - Allow query of available device memory through DeviceAPI
 * [#16997](https://github.com/apache/tvm/pull/16997) - [Disco] Restore checks for hangup of disco pipe
 * [#16938](https://github.com/apache/tvm/pull/16938) - Allow offset to be specified in NDArray::CreateView
 * [#16890](https://github.com/apache/tvm/pull/16890) - [VULKAN] Support total_global_memory
 * [#16880](https://github.com/apache/tvm/pull/16880) - Implemented Datatype.itemsize()

### TIR
 * [#17134](https://github.com/apache/tvm/pull/17134) - [Schedule] Remove `@type_check` for `set_axis_separator`
 * [#17112](https://github.com/apache/tvm/pull/17112) - [DLight] Enable SimdGroup op for Metal
 * [#17098](https://github.com/apache/tvm/pull/17098) - [RPC] Allow RPC calls to compiled PrimFuncs with no arguments
 * [#17039](https://github.com/apache/tvm/pull/17039) - Fix Bug in VectorizeLoop
 * [#17030](https://github.com/apache/tvm/pull/17030) - Fix Shuffle rewrite
 * [#16947](https://github.com/apache/tvm/pull/16947) - Support narrow dtype for let binding
 * [#16952](https://github.com/apache/tvm/pull/16952) - Enhance CLZ intrinsic support
 * [#16945](https://github.com/apache/tvm/pull/16945) - [Compute-at] Make compute-ated block simple when the predicate could be merged
 * [#16879](https://github.com/apache/tvm/pull/16879) - Make T.reinterpret nop when dtype is the same

### TOPI
 * [#17091](https://github.com/apache/tvm/pull/17091) - Add dense schedule for fp16 and fp32 using gemm
 * [#17048](https://github.com/apache/tvm/pull/17048) - [SME]Add conv2d NHWC SME fp16->fp32 schedule
 * [#17040](https://github.com/apache/tvm/pull/17040) - Fix SME conv2d schedule import and intrin argument
 * [#17003](https://github.com/apache/tvm/pull/17003) - [SME]Add conv2d NHWC SME fp32 schedule
 * [#16977](https://github.com/apache/tvm/pull/16977) - Remove `blockIdx.z` in topi sort
 * [#16951](https://github.com/apache/tvm/pull/16951) - Revert unification of conv2d NHWC hybrid scheduling for `arm_cpu` targets

### TVMScript
 * [#17107](https://github.com/apache/tvm/pull/17107) - Better Type Annotation for TIR OP
 * [#16967](https://github.com/apache/tvm/pull/16967) - Fix error reporting inside Macro func
 * [#16916](https://github.com/apache/tvm/pull/16916) - Support `T.launch_thread` with i64 dtype
 * [#16876](https://github.com/apache/tvm/pull/16876) - Optionally use `ruff format` instead of `black`
 * [#16877](https://github.com/apache/tvm/pull/16877) - [Bug] Add test case for missing symbolic bounds

### cuda & cutlass & tensorrt
 * [#16980](https://github.com/apache/tvm/pull/16980) - [Cuda] Skip FreeDataSpace when CUDA driver is in inconsistent state

### web
 * [#17031](https://github.com/apache/tvm/pull/17031) - Fix string to uint8 array for special characters
 * [#17028](https://github.com/apache/tvm/pull/17028) - Add dtype and offset for CreateView in runtime
 * [#16910](https://github.com/apache/tvm/pull/16910) - Support string[] in setPackedFunc() and exceptionally long arrays

### Misc
 * [#17135](https://github.com/apache/tvm/pull/17135) - [QoL][IR] Provide default constructor for NameSupply/GlobalVarSupply
 * [#17125](https://github.com/apache/tvm/pull/17125) - [Utils] Define line-length for "ruff format"
 * [#17152](https://github.com/apache/tvm/pull/17152) - GraphExecutor: Fix wild pointer assign when input and output are reshape
 * [#17150](https://github.com/apache/tvm/pull/17150) - [WebGPU] Fall back to 256MB for maxBufferSize if needed
 * [#17128](https://github.com/apache/tvm/pull/17128) - [Compute-inline] Prefer T.where for reverse compute-inlined block with predicate
 * [#16976](https://github.com/apache/tvm/pull/16976) - [WebGPU] Implement `tir.dp4a` with WGSL built-in function `dot4I8Packed`
 * [#17124](https://github.com/apache/tvm/pull/17124) - [WebGPU] Add `tir.dp4a`
 * [#17113](https://github.com/apache/tvm/pull/17113) - [CudaGraph] Handle exceptions thrown while capturing cuda graph
 * [#17094](https://github.com/apache/tvm/pull/17094) - [Utility][Container] Support non-nullable types in Array::Map
 * [#17101](https://github.com/apache/tvm/pull/17101) - [RPC] Raise error if server process terminated
 * [#17092](https://github.com/apache/tvm/pull/17092) - [UnitTests] Use tvm.ir.assert_structural_equal whenever possible
 * [#17054](https://github.com/apache/tvm/pull/17054) - [SME] Utilize predication in fp32 matmul and conv2d schedules
 * [#17079](https://github.com/apache/tvm/pull/17079) - [CMake] Show NVCC include directories in compile_commands.json
 * [#17076](https://github.com/apache/tvm/pull/17076) - [SME] Extract gemm block correctly when fused with bias
 * [#17071](https://github.com/apache/tvm/pull/17071) - [WebGPU] Translate `int8x4` into `u32`
 * [#17065](https://github.com/apache/tvm/pull/17065) - [FP8][Codegen] Add make_fp8 vector constructors
 * [#17064](https://github.com/apache/tvm/pull/17064) - Add docs of v0.15.0 and v0.16.0
 * [#16985](https://github.com/apache/tvm/pull/16985) - [CODEGEN] Vector-Codegen support for llvm-pure-intrin
 * [#17058](https://github.com/apache/tvm/pull/17058) - Introduce outer reduction for metal
 * [#17051](https://github.com/apache/tvm/pull/17051) - Use adapter.info when available instead of requestAdapterInfo
 * [#16981](https://github.com/apache/tvm/pull/16981) - [SME] Add scalable fp16->fp32 dense schedule
 * [#17029](https://github.com/apache/tvm/pull/17029) - [Contrib] Implement NDArray cache update
 * [#17027](https://github.com/apache/tvm/pull/17027) - [picojson] Let objects be ordered when serializing
 * [#17021](https://github.com/apache/tvm/pull/17021) - [WebGPU] Update error messages to be more user-friendly
 * [#17010](https://github.com/apache/tvm/pull/17010) - Support multinomial_from_uniform dispatch
 * [#16999](https://github.com/apache/tvm/pull/16999) - [USMP] add missing const specifier for global_const_workspace
 * [#17005](https://github.com/apache/tvm/pull/17005) - [WebGPU] Handle device OOM in createBuffer
 * [#16921](https://github.com/apache/tvm/pull/16921) - [SME] Introduce scalable fp32 dense schedule
 * [#16957](https://github.com/apache/tvm/pull/16957) - chore: remove repetitive words
 * [#16909](https://github.com/apache/tvm/pull/16909) - [QoL][IR] Provide std::hash and std::equal_to for IR Variable types
 * [#16987](https://github.com/apache/tvm/pull/16987) - [JVM] Automatic Compatibility of JVM AttachCurrentThread
 * [#16974](https://github.com/apache/tvm/pull/16974) - [CUBLAS][FP8] Enable R.matmul + R.multiply offloading
 * [#16896](https://github.com/apache/tvm/pull/16896) - [CUBLAS] Enable offloading of R.matmul + R.dequantize
 * [#16956](https://github.com/apache/tvm/pull/16956) - Add script for testing release package
 * [#16908](https://github.com/apache/tvm/pull/16908) - Overriding the StructuralEqual() for easy usage
 * [#16932](https://github.com/apache/tvm/pull/16932) - Enable gemv schedule for adreno
 * [#16935](https://github.com/apache/tvm/pull/16935) - [3rdparty] Bump FlashInfer for sampling functions
 * [#16937](https://github.com/apache/tvm/pull/16937) - [Thrust] Increase static workspace size
 * [#16915](https://github.com/apache/tvm/pull/16915) - [Marvell BYOC]: Marvell AI Accelerator Integration - Phase 2
 * [#16741](https://github.com/apache/tvm/pull/16741) - Restore "pytest.mark.gpu" for RELAX tests
 * [#16914](https://github.com/apache/tvm/pull/16914) - [CMAKE] Make LOG_BEFORE_THROW explicit
 * [#16913](https://github.com/apache/tvm/pull/16913) - Enhance Release Note Script and Remove Useless File
 * [#16907](https://github.com/apache/tvm/pull/16907) - [Upd] Fixed lld search in rocm
 * [#16900](https://github.com/apache/tvm/pull/16900) - [CMAKE] Misc improvment of Util
 * [#16897](https://github.com/apache/tvm/pull/16897) - [Target] Don't register AArch64 target tags without LLVM compiler support
 * [#16892](https://github.com/apache/tvm/pull/16892) - [CUBLAS] Set fp32 compute and scale dtypes in fp16 matmul
 * [#16888](https://github.com/apache/tvm/pull/16888) - [CUBLAS][FP8] Support e4m3 gemm in cuBLAS BYOC
 * [#16887](https://github.com/apache/tvm/pull/16887) - [Contrib] Enable fp16 for thrust sort
 * [#16881](https://github.com/apache/tvm/pull/16881) - [release][Dont Squash] Update version to 0.16.0 and 0.17.0.dev on main branch

## v0.18.0.rc0 (2024-10-17)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**):

- **Frontend**: PyTorch's ExportedProgram is supported in the relax frontend ( https://github.com/apache/tvm/issues/17346)
- Community, RFCs
- AOT, Hexagon， OpenCL & CLML, Web, Metal
- **Relax**, Dlight, Disco
- TIR, TVMScript
- Docs, Docker, CI, Misc, BugFix

Please visit the full listing of commits for a complete view: [v0.18.dev0...v0.18.0.rc0](https://github.com/apache/tvm/compare/v0.18.dev0...v0.18.0.rc0).

### Community

 * [#17450](https://github.com/apache/tvm/pull/17450) - update contributors

### RFCs

The new RFC introduces a new backend Android Neural Network API (NNAPI) for BYOC. It is a graph-level neural network inference API provided by the Android runtime. Prior to this RFC, TVM on Android mobile devices mainly relies on OpenCL for GPU acceleration. This RFC aims to add a new codegen and a runtime via the BYOC framework, which enables execution on custom accelerators from SoC vendors on mobile devices.

 * [#109](https://github.com/apache/tvm-rfcs/pull/109) - [RFC] NNAPI Integration via BYOC

----


### BYOC
 * [#17385](https://github.com/apache/tvm/pull/17385) - [NNAPI] Add NNAPI backend for BYOC

### BugFix
 * [#17440](https://github.com/apache/tvm/pull/17440) - [TIR][Schedule] TileWithTensorIntrin skip ComputeInline if bu…
 * [#17419](https://github.com/apache/tvm/pull/17419) - [FFI]Grab GIL when check env signals
 * [#17403](https://github.com/apache/tvm/pull/17403) - [Fix][LLVM] Fix getHostCPUFeatures LLVM version cutoff
 * [#17383](https://github.com/apache/tvm/pull/17383) - [ONNX] Skip constant If node generated by PyTorch
 * [#17360](https://github.com/apache/tvm/pull/17360) - [FIX] fix bug when normalize iter with different lower bounds
 * [#17148](https://github.com/apache/tvm/pull/17148) - [Relax] Preserve existing DataflowBlock in ConvertToDataflow
 * [#17345](https://github.com/apache/tvm/pull/17345) - [Fix][Relax] Add the missing tree-attn func arg for KV cache creation
 * [#17073](https://github.com/apache/tvm/pull/17073) - [Relax]FCallPacked not checked in CodegenVMTIR
 * [#17315](https://github.com/apache/tvm/pull/17315) - [MSC]Bugfix for strided_slice op
 * [#17335](https://github.com/apache/tvm/pull/17335) - [Relax][PyTorch][Fix] use`_convert_torch_tensor_to_relax()` where possible
 * [#17330](https://github.com/apache/tvm/pull/17330) - [Relax][PyTorch]Update `layer_norm` converter to support `immutable_list` for `normalized_shape`
 * [#17324](https://github.com/apache/tvm/pull/17324) - [Fix] Remove `tvm.` prefix from image name when `./docker/build.sh`
 * [#17308](https://github.com/apache/tvm/pull/17308) - [TVM4J]Fix unhandled return type in JNI
 * [#17307](https://github.com/apache/tvm/pull/17307) - [Fix][TIR] LowerThreadAllreduce warp reduction mask
 * [#17312](https://github.com/apache/tvm/pull/17312) - [Relax]Infer TIR values from shapes inside a tuple
 * [#17292](https://github.com/apache/tvm/pull/17292) - [Relax]Support torch.unbind op and fix bugs for expand && split
 * [#17263](https://github.com/apache/tvm/pull/17263) - [Relax]Preserve dtype in ToMixedPrecision for kNever ops
 * [#17229](https://github.com/apache/tvm/pull/17229) - [Cutlass] fix cutlass instantiate attention template bugs
 * [#17121](https://github.com/apache/tvm/pull/17121) - [Relax]Fix a bug about the IR construction in test file
 * [#17142](https://github.com/apache/tvm/pull/17142) - Allow import of TVM when current directory is read-only

### CI
 * [#17444](https://github.com/apache/tvm/pull/17444) - [Docs] Upgrade Sphinx
 * [#17425](https://github.com/apache/tvm/pull/17425) - Upgrade CI to Python 3.9
 * [#17410](https://github.com/apache/tvm/pull/17410) - Upgrade unity image tag to `20240917-153130-9f281758`
 * [#17409](https://github.com/apache/tvm/pull/17409) - [Windows] Workaround for error in FindLLVM
 * [#17397](https://github.com/apache/tvm/pull/17397) - Update image tag to 20240917-153130-9f281758
 * [#17338](https://github.com/apache/tvm/pull/17338) - Upgrade PyTorch to 2.4.1
 * [#17337](https://github.com/apache/tvm/pull/17337) - Disable NNPACK build and fix error on Android SDK installaion
 * [#17355](https://github.com/apache/tvm/pull/17355) - Upgrade github upload-artifact action
 * [#17334](https://github.com/apache/tvm/pull/17334) - [Hexagon] Forward gtest tests into pytest as separate tests
 * [#17271](https://github.com/apache/tvm/pull/17271) - Resolve CI compilation failures on MacOSX
 * [#17221](https://github.com/apache/tvm/pull/17221) - Reduce logging level when checking if docker image exists
 * [#17206](https://github.com/apache/tvm/pull/17206) - Update dummy-variable regex for pylint
 * [#17117](https://github.com/apache/tvm/pull/17117) - [CLML]Fix for few clml regression issues
 * [#17155](https://github.com/apache/tvm/pull/17155) - Remove lint step from `unity/pr-head` step

### Disco
 * [#17398](https://github.com/apache/tvm/pull/17398) - Enable float8 data type in disco
 * [#17275](https://github.com/apache/tvm/pull/17275) - Fix double free of nccl communicator
 * [#17264](https://github.com/apache/tvm/pull/17264) - Disable splitting nccl communicator in single-group
 * [#17182](https://github.com/apache/tvm/pull/17182) - Implement SocketSession
 * [#17191](https://github.com/apache/tvm/pull/17191) - Cross-group and p2p send/receive primitives
 * [#17180](https://github.com/apache/tvm/pull/17180) - Group-wise operation

### Dlight
 * [#17430](https://github.com/apache/tvm/pull/17430) - [GPU] Improve matmul schedule for adreno
 * [#17363](https://github.com/apache/tvm/pull/17363) - Fix Matmul rule for Conv3D
 * [#17259](https://github.com/apache/tvm/pull/17259) - [ADRENO] Fix for opencl adreno matmul schedule
 * [#17187](https://github.com/apache/tvm/pull/17187) - [GPU] Add OpenCL dequant matmul schedule

### Docker
 * [#17433](https://github.com/apache/tvm/pull/17433) - [CI] Add NNEF dependency to CI images

### Docs
 * [#17436](https://github.com/apache/tvm/pull/17436) - [Relax][PyTorch]Use `torch.export` insteamd of `fx.symbolic_trace` for tutorial
 * [#17402](https://github.com/apache/tvm/pull/17402) - [Doc] Update Architecture Overview
 * [#17382](https://github.com/apache/tvm/pull/17382) - More clarity on security model of RPC server
 * [#17380](https://github.com/apache/tvm/pull/17380) - [Doc] Relax Deep Dive
 * [#17377](https://github.com/apache/tvm/pull/17377) - Update document to include security model of RPC server
 * [#17378](https://github.com/apache/tvm/pull/17378) - Link to project-specific security page
 * [#17352](https://github.com/apache/tvm/pull/17352) - TVM pip Installation fix
 * [#17343](https://github.com/apache/tvm/pull/17343) - Minor fix typo in developer howto guide
 * [#17328](https://github.com/apache/tvm/pull/17328) - [Doc] Deep Dive TensorIR
 * [#17327](https://github.com/apache/tvm/pull/17327) - [Doc] How to Optimize a Language Model
 * [#17320](https://github.com/apache/tvm/pull/17320) - [Doc] Customize Optimization
 * [#17319](https://github.com/apache/tvm/pull/17319) - [Doc] Fix doc build error in e2e_opt_model.py
 * [#17306](https://github.com/apache/tvm/pull/17306) - [Doc] Refactor How-To
 * [#17296](https://github.com/apache/tvm/pull/17296) - [Doc] Overview
 * [#17298](https://github.com/apache/tvm/pull/17298) - [Doc] IRModule
 * [#17286](https://github.com/apache/tvm/pull/17286) - Introduce Relax API and move legacy part to standalone page
 * [#17289](https://github.com/apache/tvm/pull/17289) - [Doc] Quick Start
 * [#17287](https://github.com/apache/tvm/pull/17287) - [Doc] Refactor install docs

### Frontend
 * [#17431](https://github.com/apache/tvm/pull/17431) - [Relax][Onnx] Add support for pad-2
 * [#17447](https://github.com/apache/tvm/pull/17447) - [ONNX] Move relax related tests to the correct file
 * [#17427](https://github.com/apache/tvm/pull/17427) - [Relax][ONNX] Expand op support for ONNX frontend
 * [#17429](https://github.com/apache/tvm/pull/17429) - [Relax][PyTorch] Support tensor manipulation and creation ops for ExportedProgram importer
 * [#17426](https://github.com/apache/tvm/pull/17426) - [Relax][PyTorch] Support neural network ops for ExportedProgram importer
 * [#17424](https://github.com/apache/tvm/pull/17424) - [Relax][PyTorch] Support binary, statistical and search ops for ExportedProgram importer
 * [#17421](https://github.com/apache/tvm/pull/17421) - [Relax][PyTorch] Support more unary ops for ExportedProgram importer
 * [#17396](https://github.com/apache/tvm/pull/17396) - [Relax][PyTorch] Add support for `torch.export.ExportedProgram` in Relax PyTorch Frontend
 * [#17379](https://github.com/apache/tvm/pull/17379) - [Relax][PyTorch] Fix output shape of `torch.nn.functional.scaled_dot_product_attention`
 * [#17376](https://github.com/apache/tvm/pull/17376) - [Relax][PyTorch] Cleanup Tensor Manipulation and Creation op converters
 * [#17372](https://github.com/apache/tvm/pull/17372) - [Relax][PyTorch] Cleanup Statistical, Search and DataType op converters
 * [#17369](https://github.com/apache/tvm/pull/17369) - [Relax][PyTorch] Cleanup Neural Network op converters
 * [#17366](https://github.com/apache/tvm/pull/17366) - [Relax][PyTorch] Cleanup binary op converters
 * [#17356](https://github.com/apache/tvm/pull/17356) - [Relax][PyTorch] Cleanup unary op converters
 * [#17350](https://github.com/apache/tvm/pull/17350) - [Relax][Onnx] fix params name bug in onnx frontend
 * [#17342](https://github.com/apache/tvm/pull/17342) - [Relax][PyTorch] Add support for `torch.ops.aten.sym_size.int`
 * [#17300](https://github.com/apache/tvm/pull/17300) - [Relax][PyTorch] Add support for torchvision.ops.stochastic_depth
 * [#17325](https://github.com/apache/tvm/pull/17325) - [Relax][PyTorch] Add support for `torch.nn.functional.conv*`
 * [#17309](https://github.com/apache/tvm/pull/17309) - [Relax][Onnx] fix expand bug in onnx frontend
 * [#17304](https://github.com/apache/tvm/pull/17304) - [Relax][PyTorch] Add support for torch.repeat
 * [#17291](https://github.com/apache/tvm/pull/17291) - [Relax][PyTorch] Add support for torch.tile
 * [#17277](https://github.com/apache/tvm/pull/17277) - [Relay][Pytorch] Add support for `aten::tile`
 * [#17228](https://github.com/apache/tvm/pull/17228) -  [Unity]Add Sqrt Op
 * [#17189](https://github.com/apache/tvm/pull/17189) - [Relax][PyTorch] Add support for `torch.nn.functional.max_pool2d`
 * [#17186](https://github.com/apache/tvm/pull/17186) - [Relax][PyTorch] Add support for torch.einsum
 * [#17184](https://github.com/apache/tvm/pull/17184) - [Relax][PyTorch] Add support for torch.permute
 * [#17167](https://github.com/apache/tvm/pull/17167) - [Relax] [ONNX] Add support for Sign and Not

### Hexagon
 * [#17204](https://github.com/apache/tvm/pull/17204) - Fix LWP assembly handler (predicate register)
 * [#17169](https://github.com/apache/tvm/pull/17169) - [CMake] Fix v66 build issue
 * [#17162](https://github.com/apache/tvm/pull/17162) - Support RPC execution of existing shared lib

### LLVM
 * [#17347](https://github.com/apache/tvm/pull/17347) - [RUNTIME] Fix RISC-V CodeModel propagation to ORCJIT runtime executor
 * [#17199](https://github.com/apache/tvm/pull/17199) - Fix for getHostCPUFeatures API change

### MetaSchedule
 * [#17166](https://github.com/apache/tvm/pull/17166) - Replace `xgboost.rabit` with `xgboost.collective` because it's deprecated
 * [#17171](https://github.com/apache/tvm/pull/17171) - Add a testcase for padded conv2d in meta_schedule

### OpenCL & CLML
 * [#17273](https://github.com/apache/tvm/pull/17273) - [CODEGEN][OPENCL] Fix opencl codegen for few ops

### ROCm
 * [#17295](https://github.com/apache/tvm/pull/17295) - Fix non-standard rocm path
 * [#17290](https://github.com/apache/tvm/pull/17290) - hipBLAS integration
 * [#17256](https://github.com/apache/tvm/pull/17256) - Support ROCm 6

### Relax
 * [#17449](https://github.com/apache/tvm/pull/17449) - Add scatter_nd op support
 * [#17453](https://github.com/apache/tvm/pull/17453) - Add NonZero op
 * [#17448](https://github.com/apache/tvm/pull/17448) - Support left_shift and right_shift op
 * [#17432](https://github.com/apache/tvm/pull/17432) - [KVCACHE] Improved schedule for prefill attention
 * [#17428](https://github.com/apache/tvm/pull/17428) - Introduce static shape tuning pipeline
 * [#17401](https://github.com/apache/tvm/pull/17401) - [KVCache] Attention func accepting over-padded qkv and output NDArray
 * [#17331](https://github.com/apache/tvm/pull/17331) - Validate StructInfo annotations in well-formed check
 * [#17368](https://github.com/apache/tvm/pull/17368) - [Transform] Add SelectNode handling in SymbolicMatcher
 * [#17353](https://github.com/apache/tvm/pull/17353) - Fix BYOC removing existing ext mods
 * [#17359](https://github.com/apache/tvm/pull/17359) - Add new NN allgather operator
 * [#17362](https://github.com/apache/tvm/pull/17362) - [KV Cache] Refactor `_attention_sequence_prefill` function to …
 * [#17332](https://github.com/apache/tvm/pull/17332) - Validate StructInfo of variable bindings
 * [#17354](https://github.com/apache/tvm/pull/17354) - Fix inline source module cause path too long error
 * [#17213](https://github.com/apache/tvm/pull/17213) - Refactor RealizeVDevice to remove in-place mutation
 * [#17253](https://github.com/apache/tvm/pull/17253) - [Transform] Handle tuple return in RemoveUnusedOutputs
 * [#17285](https://github.com/apache/tvm/pull/17285) - Require correct input/output shapes `R.call_tir`
 * [#17202](https://github.com/apache/tvm/pull/17202) - Update GlobalVar name in AttachGlobalSymbol
 * [#17218](https://github.com/apache/tvm/pull/17218) - Allow dynamic shape argument to R.reshape
 * [#17326](https://github.com/apache/tvm/pull/17326) - [KVCache] Add tree attention with paged cache support
 * [#17314](https://github.com/apache/tvm/pull/17314) - [Transform] Compose preproc functions in LiftTransformParams
 * [#17313](https://github.com/apache/tvm/pull/17313) - Identify tuple unpack/repack in CanonicalizeBindings
 * [#17305](https://github.com/apache/tvm/pull/17305) - [Python]Rotary positional embedding scaling
 * [#17243](https://github.com/apache/tvm/pull/17243) - Avoid wrapping TupleStructInfo into a Tuple for R.call_tir
 * [#17224](https://github.com/apache/tvm/pull/17224) - [Analysis] Handle recursive functions in CollectVarUsage
 * [#17280](https://github.com/apache/tvm/pull/17280) - [KVCache] Increase coalesce threshold
 * [#17261](https://github.com/apache/tvm/pull/17261) - Add KVCache Interface for Relax NNModule
 * [#17145](https://github.com/apache/tvm/pull/17145) - Implement R.ensure_zero_offset and update memory planning for R.view
 * [#17242](https://github.com/apache/tvm/pull/17242) - Remove segfault in R.call_tir_inplace validation
 * [#17234](https://github.com/apache/tvm/pull/17234) - FuseTransposeMatmul Pass
 * [#17226](https://github.com/apache/tvm/pull/17226) - Fix segfault in rewrite_bindings for MatchCast node
 * [#17220](https://github.com/apache/tvm/pull/17220) - Handle presence of R.call_tir in MergeCompositeFunctions
 * [#17201](https://github.com/apache/tvm/pull/17201) - [Transform]Handle `is_group` argument in IPC AllReduce
 * [#17198](https://github.com/apache/tvm/pull/17198) - Disable fusion for fetching from the packed params in FuseOps
 * [#17149](https://github.com/apache/tvm/pull/17149) -  Implement Rewriter class for pattern-rewrite
 * [#17192](https://github.com/apache/tvm/pull/17192) - [KVCache] Partial layers support
 * [#17157](https://github.com/apache/tvm/pull/17157) - Integrate cuDNN attention
 * [#17160](https://github.com/apache/tvm/pull/17160) - Fix fuseOps via pattern

### Relay
 * [#17339](https://github.com/apache/tvm/pull/17339) - [qnn]: Fix qnn.avg_pool2d layout inference
 * [#17177](https://github.com/apache/tvm/pull/17177) - [FQ2I]: Use appropriate dtype while quantizing relay.op.nn.pad…

### Runtime
 * [#17407](https://github.com/apache/tvm/pull/17407) - Add property Module.is_device_module
 * [#17294](https://github.com/apache/tvm/pull/17294) - Support KV cache with RoPE extension factor array
 * [#17240](https://github.com/apache/tvm/pull/17240) - [FFI]Use TVMValue::v_int64 to represent boolean values
 * [#17252](https://github.com/apache/tvm/pull/17252) - Revert "[FFI]Introduce runtime boxed types for int/float/bool"
 * [#16183](https://github.com/apache/tvm/pull/16183) - [FFI]Introduce runtime boxed types for int/float/bool
 * [#17237](https://github.com/apache/tvm/pull/17237) - Reorganize PagedKVCache attn kernel invocation
 * [#17227](https://github.com/apache/tvm/pull/17227) - Allow aborting fetchWithCache through AbortSignal
 * [#17208](https://github.com/apache/tvm/pull/17208) - Allow aborting fetchNDArray through AbortSignal

### TIR
 * [#17443](https://github.com/apache/tvm/pull/17443) - Add `is_vector` Method to DataType class and update usages across Codebase
 * [#17411](https://github.com/apache/tvm/pull/17411) - [NarrowDataType] Bufferload's index should not inherit bits constraint of value
 * [#17219](https://github.com/apache/tvm/pull/17219) - Validate tir::Buffer axis_separators on construction
 * [#17158](https://github.com/apache/tvm/pull/17158) - [Analyzer] Simplify `x==x` expressions for all dtypes

### TOPI
 * [#17274](https://github.com/apache/tvm/pull/17274) - [ADRENO] Add Group Conv2d texture schedule

### TVMScript
 * [#17435](https://github.com/apache/tvm/pull/17435) - Enable T.macro decorateing class method
 * [#17434](https://github.com/apache/tvm/pull/17434) - [TIR] Add source kernel intetration via call_kernel
 * [#17395](https://github.com/apache/tvm/pull/17395) - [TIR, TVMScript] Add TIR - Triton integration
 * [#17131](https://github.com/apache/tvm/pull/17131) - [Relax] Allow return statement in DataflowBlock
 * [#17373](https://github.com/apache/tvm/pull/17373) - Avoid segfault from invalid TVMScript

### cuda & cutlass & tensorrt
 * [#17408](https://github.com/apache/tvm/pull/17408) - [CUTLASS] Add FP8 gemm kernels

### web
 * [#17420](https://github.com/apache/tvm/pull/17420) - Allow deprecated API requestAdapterInfo with any cast
 * [#17404](https://github.com/apache/tvm/pull/17404) - [WASM] Implement concat embeddings
 * [#17251](https://github.com/apache/tvm/pull/17251) - Add TVMArgBool to ArgTypeCode

### Misc
 * [#17457](https://github.com/apache/tvm/pull/17457) - Try to fix windows CI conda build issue
 * [#17415](https://github.com/apache/tvm/pull/17415) - [NVSHMEM] Enable nvshmem memory allocation
 * [#17422](https://github.com/apache/tvm/pull/17422) - [CMake] Add NCCL/RCCL header directory to include path
 * [#17405](https://github.com/apache/tvm/pull/17405) - [TVMjs] Modify web package description
 * [#17400](https://github.com/apache/tvm/pull/17400) - [3rdparty] Bump FlashInfer for tmp workspace reduction
 * [#17394](https://github.com/apache/tvm/pull/17394) - [MSC] Support concat with constant inputs
 * [#17351](https://github.com/apache/tvm/pull/17351) - [MSC][Refactor] Support dynamic shape
 * [#17371](https://github.com/apache/tvm/pull/17371) - [WEBGPU] Update runtime to remove deprecated API
 * [#17361](https://github.com/apache/tvm/pull/17361) - [IR] Expose ReplaceGlobalVars utility in the Python API
 * [#17358](https://github.com/apache/tvm/pull/17358) - Update tvmc_command_line_driver.py, modify the sentence, remove the duplicate "as"
 * [#17344](https://github.com/apache/tvm/pull/17344) - [MSC] Reconstruct tensorrt module
 * [#17297](https://github.com/apache/tvm/pull/17297) - [Apps] Remove mxnet dependency from /apps/android_camera/models
 * [#17299](https://github.com/apache/tvm/pull/17299) - [Apps] Remove mxnet dependency from /apps/ios_rpc
 * [#17293](https://github.com/apache/tvm/pull/17293) - [Rust] Remove mxnet dependency and re-enable rust example
 * [#17321](https://github.com/apache/tvm/pull/17321) - [Target] Refine equality check on TargetKind instances
 * [#17317](https://github.com/apache/tvm/pull/17317) - Add NVSHMEM support
 * [#17301](https://github.com/apache/tvm/pull/17301) - [TE][CreatePrimFunc] Fix create reduce block with spatial iter dependent init value
 * [#17284](https://github.com/apache/tvm/pull/17284) - [Support] Fix the Read/Write of socket stream
 * [#17302](https://github.com/apache/tvm/pull/17302) - [Codegen][WebGPU] LetNode common subexpr override
 * [#17246](https://github.com/apache/tvm/pull/17246) - [Cleanup] Remove `using namespace tvm::runtime` from headers
 * [#17278](https://github.com/apache/tvm/pull/17278) - [Codegen] Emit `tir::Let` as var assignment explicitly
 * [#17260](https://github.com/apache/tvm/pull/17260) - [WINDOWS] Compiler options for non x86 targets
 * [#17249](https://github.com/apache/tvm/pull/17249) - [IR] Handle NaN in StructuralEqual and StructuralHash
 * [#17257](https://github.com/apache/tvm/pull/17257) -  [FFI] Re-introduce the boxed primitive values
 * [#17265](https://github.com/apache/tvm/pull/17265) - [CompileBugfix][contrib] meet 'base64.h: No such file or directory' and '‘tvm::runtime::vm::AllocatorType’ has not been declared' while compiling
 * [#17214](https://github.com/apache/tvm/pull/17214) - Replacing unary ops with LookUpTable and Take op to improve performance
 * [#17250](https://github.com/apache/tvm/pull/17250) - [WebGPU] Fix unexpected device lost error when intentional dispose
 * [#17236](https://github.com/apache/tvm/pull/17236) - [3rdparty] Bump FlashInfer
 * [#17233](https://github.com/apache/tvm/pull/17233) - [Runtime Patch] Add AbortSignal to fetchWithCache in ArtifactCacheTemplate interface
 * [#17190](https://github.com/apache/tvm/pull/17190) - [Cython][FFI] Fix crash when call del operator for handle
 * [#17170](https://github.com/apache/tvm/pull/17170) - Pass to eliminate redundant branch and overcompute
 * [#17185](https://github.com/apache/tvm/pull/17185) - Remove and replace deprecated `distutils.util.strtobool()`
 * [#17188](https://github.com/apache/tvm/pull/17188) - Add `packaging` to `python/gen_requirements.py`
 * [#17181](https://github.com/apache/tvm/pull/17181) - [FFI] Add python signal handler for ctypes FFI
 * [#17173](https://github.com/apache/tvm/pull/17173) - Use `packaging.version.parse` instead of `distutils.version.LooseVersion`
 * [#17174](https://github.com/apache/tvm/pull/17174) - [TVMJS] Check DataType.NUMPY2STR when saving array
 * [#17168](https://github.com/apache/tvm/pull/17168) - [Meta Schedule][XGBoost] enable custom callback func test with xgboost>=1.6.0




## v0.19.0 (2025-01-24)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax, OpenCL, MetaSchedule.

Please visit the full listing of commits for a complete view: [v0.19.dev0...v0.19.0.rc0](https://github.com/apache/tvm/compare/v0.19.dev0...v0.19.0.rc0).

### Community

None.

### RFCs

None.


### Arith
 * [#17469](https://github.com/apache/tvm/pull/17469) - [LLVM]Presburger compile fix for MLIR/LLVM 19.x

### BugFix
 * [#17595](https://github.com/apache/tvm/pull/17595) - [Fix][KVCache] Fix incorrect tile size calculation
 * [#17549](https://github.com/apache/tvm/pull/17549) - [FIX][LLVM] Workaround -mcpu=apple-latest for llvm above 18.0 (#17492)
 * [#17537](https://github.com/apache/tvm/pull/17537) - [FIX][topi.scatter_nd] fixed shape equality assert by using analyzer to prove equality
 * [#17502](https://github.com/apache/tvm/pull/17502) - [FIX][TOPI][strided_slice] Fix topi.strided_slice output shape
 * [#17505](https://github.com/apache/tvm/pull/17505) - [RELAX][ONNX][FIX] add a parser to handle expression in the shape dim names 
 * [#17490](https://github.com/apache/tvm/pull/17490) - [FIX][ONNX][RELAX] Add support for dynamic ShapeExpr in Slice, Squeeze and Flatten
 * [#17467](https://github.com/apache/tvm/pull/17467) - [FIX][RELAX][ONNX] Fix typo in onnx frontend 

### CI
 * [#17596](https://github.com/apache/tvm/pull/17596) - [Test] Skip flaky test to unblock CI
 * [#17451](https://github.com/apache/tvm/pull/17451) - Upgrade CI image to `20241105-030952-3e386fd3`
 * [#17534](https://github.com/apache/tvm/pull/17534) - Upgrade zephyr-sdk to 0.16.9
 * [#17503](https://github.com/apache/tvm/pull/17503) - Upgrade `oneflow==0.9.0`
 * [#17485](https://github.com/apache/tvm/pull/17485) - Revert jax, keras, tensorflow, and tflite upgrades introduced #17425
 * [#17470](https://github.com/apache/tvm/pull/17470) - Pin cpplint==1.6.1

### Docs
 * [#17518](https://github.com/apache/tvm/pull/17518) - Few fixes for broken Adreno docs
 * [#17527](https://github.com/apache/tvm/pull/17527) - Fix typo in TensorIR
 * [#17528](https://github.com/apache/tvm/pull/17528) - Fix Typo in Debugging TVM

### LLVM
 * [#17547](https://github.com/apache/tvm/pull/17547) - Make compilable with LLVM-20
 * [#17538](https://github.com/apache/tvm/pull/17538) - [RUNTIME] Make ORCJIT LLVM executor the default one

### MetaSchedule
 * [#17465](https://github.com/apache/tvm/pull/17465) - Fix a multilevel tiling error on dynamic relax workload

### OpenCL & CLML
 * [#17516](https://github.com/apache/tvm/pull/17516) - [RUNTIME][CLML] Dynamic backward compatibility
 * [#17519](https://github.com/apache/tvm/pull/17519) - [OPENCL][ADRENO] Introduce Qualcomm extension support
 * [#17517](https://github.com/apache/tvm/pull/17517) - [TEST][CLML] Clip test case updated
 * [#17472](https://github.com/apache/tvm/pull/17472) - [Device][OpenCL] add CL_EXEC_STATUS_ERROR_FOR_EVENTS_IN_WAIT_LIST to …

### Relax
 * [#17541](https://github.com/apache/tvm/pull/17541) - Fix bug in convert_layout pass
 * [#17539](https://github.com/apache/tvm/pull/17539) - [KVCache] Fix attention prefill kernel for Metal and Android
 * [#17540](https://github.com/apache/tvm/pull/17540) - Add support for ONNX LPPool
 * [#17536](https://github.com/apache/tvm/pull/17536) - [Frontend][Onnx] Add auto_pad support for conv
 * [#17525](https://github.com/apache/tvm/pull/17525) - support masked_scatter
 * [#17506](https://github.com/apache/tvm/pull/17506) - [Python]Update Rotary positional embedding scaling
 * [#17523](https://github.com/apache/tvm/pull/17523) - Add gather_elements and gather_nd operators
 * [#17511](https://github.com/apache/tvm/pull/17511) - Update ONNX frontend for unique, nonzero and compress
 * [#17509](https://github.com/apache/tvm/pull/17509) - support scatter ops
 * [#17504](https://github.com/apache/tvm/pull/17504) - [ONNX] Add support for dynamic shape expression in Expand
 * [#17482](https://github.com/apache/tvm/pull/17482) - [KVCACHE] Improved schedule for prefill attention
 * [#17445](https://github.com/apache/tvm/pull/17445) - [MetaSchedule] Support CPU weight prepack
 * [#17462](https://github.com/apache/tvm/pull/17462) - Enhance Relax op and ONNX frontend
 * [#17466](https://github.com/apache/tvm/pull/17466) - Revert "[KVCACHE] Improved schedule for prefill attention"

### Runtime
 * [#17557](https://github.com/apache/tvm/pull/17557) - [Dist] Implementation of KV cache transfer
 * [#17498](https://github.com/apache/tvm/pull/17498) - [mrvl]: Support Marvell Hardware Runtime

### TIR
 * [#17423](https://github.com/apache/tvm/pull/17423) - [Schedule] Add annotate_buffer_access primitive

### web
 * [#17545](https://github.com/apache/tvm/pull/17545) - Allows setting powerPreference on webgpu

### Misc
 * [#17593](https://github.com/apache/tvm/pull/17593) - Fix GPU detection in PerStoreFeatureNode
 * [#17554](https://github.com/apache/tvm/pull/17554) - [Refactor] Phase out microTVM
 * [#17542](https://github.com/apache/tvm/pull/17542) - [REFACTOR] Phase out VTA
 * [#17533](https://github.com/apache/tvm/pull/17533) - [Contrib] Remove CLML version print
 * [#17532](https://github.com/apache/tvm/pull/17532) - [3rdparty] Update Picojson with const `operator[]` function (#327)
 * [#17474](https://github.com/apache/tvm/pull/17474) - [TE][CreatePrimFunc] Fix loop carried dependency case with nested block levels
 * [#17501](https://github.com/apache/tvm/pull/17501) - Fix InternalError in StaticPlanBlockMemory when visiting DataflowBlockNode
 * [#17455](https://github.com/apache/tvm/pull/17455) - Compiled with Default Target(LLVM) and Built with USE_MRVL=ON
 * [#17481](https://github.com/apache/tvm/pull/17481) - [Marvell BYOC]: global_max_pool2d and squeeze op support
 * [#17484](https://github.com/apache/tvm/pull/17484) - Replace `np.int` with `np.int32`
 * [#17476](https://github.com/apache/tvm/pull/17476) - Pin pytest-profiling==1.7.0
 * [#17464](https://github.com/apache/tvm/pull/17464) - [JVM] Align Java GraphModule Initialization with Python API
 * [#17458](https://github.com/apache/tvm/pull/17458) - Show the record if the escape sequence is unsupported

## v0.20.0 (2025-04-19)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax (especial PyTorch frontend), CUDA etc.

Please visit the full listing of commits for a complete view: [v0.20.dev0...v0.20.0.rc0](https://github.com/apache/tvm/compare/v0.20.dev0...v0.20.0.rc0).

### Community

None.

### RFCs

None.

### Adreno
 * [#17608](https://github.com/apache/tvm/pull/17608) - [WINDOWS] Windows build dependencies for Adreno target

### BugFix
 * [#17761](https://github.com/apache/tvm/pull/17761) - [FIX][RELAX] fix fusion of transpose + matmul when constant  weight 
 * [#17762](https://github.com/apache/tvm/pull/17762) - [Fix] Fix OpenCL header in attention utils
 * [#17711](https://github.com/apache/tvm/pull/17711) - [Fix][dlight] add an explicit reduction loop check in Reduce
 * [#17697](https://github.com/apache/tvm/pull/17697) - [Fix] Include `<chrono>` for `std::chrono`
 * [#17677](https://github.com/apache/tvm/pull/17677) - Declare build backend for python package
 * [#17598](https://github.com/apache/tvm/pull/17598) - [TIR][FIX] update FlopEstimator to include missing nodes
 * [#17601](https://github.com/apache/tvm/pull/17601) - [Flashinfer][Fix] fix missing args in flashinfer test
 * [#17607](https://github.com/apache/tvm/pull/17607) - [FIX][TVMC] Fix the mixed precision conversion pipeline

### CI
 * [#17687](https://github.com/apache/tvm/pull/17687) - Update images to 20250226-223225-63bc315f
 * [#17680](https://github.com/apache/tvm/pull/17680) - update images to 20250225-035137-aeadc31c
 * [#17675](https://github.com/apache/tvm/pull/17675) - [skip ci]Update github tvmbot
 * [#17635](https://github.com/apache/tvm/pull/17635) - Cleanup legacy files
 * [#17634](https://github.com/apache/tvm/pull/17634) - [skip ci]Improve build time
 * [#17629](https://github.com/apache/tvm/pull/17629) - [skip ci]Robustify CI for SPOT failure
 * [#17620](https://github.com/apache/tvm/pull/17620) - Unpin pytest-profiling
 * [#17621](https://github.com/apache/tvm/pull/17621) - [skip ci] Remove legacy CI runners protection
 * [#17619](https://github.com/apache/tvm/pull/17619) - [Refactor]Remove legacy frontend tests

### Dlight
 * [#17754](https://github.com/apache/tvm/pull/17754) - Fix general reduction rule to support non-last reduction axis
 * [#17663](https://github.com/apache/tvm/pull/17663) - [CPU] Add CPU Backend Support for GEMV Optimization

### Docker
 * [#17691](https://github.com/apache/tvm/pull/17691) - Fix ml_dtypes downgrade issue introduced by TensorFlow
 * [#17686](https://github.com/apache/tvm/pull/17686) - Update ml_dtypes to 0.5.1+
 * [#17676](https://github.com/apache/tvm/pull/17676) - Use Torch GPU on gpu device
 * [#17648](https://github.com/apache/tvm/pull/17648) - Tensorflow (aka TFLite) upgrade to 2.18.0
 * [#17643](https://github.com/apache/tvm/pull/17643) - Update ml_dtypes version
 * [#17638](https://github.com/apache/tvm/pull/17638) - [skip ci]Update ml_dtypes version
 * [#17638](https://github.com/apache/tvm/pull/17638) - [skip ci]Update ml_dtypes version
 * [#17617](https://github.com/apache/tvm/pull/17617) - Tensorflow upgrade to 2.18.0

### Docs
 * [#17650](https://github.com/apache/tvm/pull/17650) - Update README
 * [#17611](https://github.com/apache/tvm/pull/17611) - Download 3rd party embeds to local files
 * [#17604](https://github.com/apache/tvm/pull/17604) - Update README

### MetaSchedule
 * [#17104](https://github.com/apache/tvm/pull/17104) - Adding post optimization in MetaSchedule to Improve Scheduling

### OpenCL & CLML
 * [#17571](https://github.com/apache/tvm/pull/17571) - [OPENCL][TEXTURE] Improved texture memory planning

### Relax
 * [#17814](https://github.com/apache/tvm/pull/17814) - [PyTorch] Add stack.default and sum.default to exported programs translator
 * [#17820](https://github.com/apache/tvm/pull/17820) - [PyTorch] Add support for broadcast_to, narrow ops
 * [#17822](https://github.com/apache/tvm/pull/17822) - [PyTorch] Cleanup tests for ExportedProgram frontend
 * [#17806](https://github.com/apache/tvm/pull/17806) - [PyTorch] Add Softplus Op Support for Exported Program and FX graph
 * [#17817](https://github.com/apache/tvm/pull/17817) - [PyTorch] Support dynamic shapes in ExportedProgram frontend
 * [#17813](https://github.com/apache/tvm/pull/17813) - [PyTorch] Improve ExportedProgram frontend by supporting `unflatten.int`, `hardtanh_.default`, `dropout_.default`, `silu_.default`, `add_.Tensor` and `relu_.default`
 * [#17812](https://github.com/apache/tvm/pull/17812) - [PyTorch] Support argsort, topk ops for ExportedProgram importer
 * [#17810](https://github.com/apache/tvm/pull/17810) - [PyTorch] Add support for argsort, sort, topk ops
 * [#17809](https://github.com/apache/tvm/pull/17809) - [PyTorch] Delete duplicate converter function `_to`
 * [#17807](https://github.com/apache/tvm/pull/17807) - [PyTorch] Fix torch 2.6 compatibility issues
 * [#17797](https://github.com/apache/tvm/pull/17797) - [Pytorch] Update SELU Implementation Using Decomposed Core-Level Ops
 * [#17802](https://github.com/apache/tvm/pull/17802) - [Pytorch] support for arange in exported programs translator
 * [#17801](https://github.com/apache/tvm/pull/17801) - [PyTorch] Support where, cumprod and reciprocal ops for ExportedProgram importer
 * [#17790](https://github.com/apache/tvm/pull/17790) - [PyTorch] Add support for index_select
 * [#17786](https://github.com/apache/tvm/pull/17786) - [PyTorch] Support softshrink op for ExportedProgram
 * [#17788](https://github.com/apache/tvm/pull/17788) - [PyTorch] Add support for where, cumprod and reciprocal ops
 * [#17785](https://github.com/apache/tvm/pull/17785) - [PyTorch] Support prod, std and var ops for ExportedProgram importer
 * [#17778](https://github.com/apache/tvm/pull/17778) - [PyTorch] Support log2, log10 and log1p ops for ExportedProgram importer
 * [#17772](https://github.com/apache/tvm/pull/17772) - [PyTorch] Add support for prod, std and var ops
 * [#17766](https://github.com/apache/tvm/pull/17766) - [PyTorch] Add support for log2, log10 and log1p ops
 * [#17760](https://github.com/apache/tvm/pull/17760) - [PyTorch] Add support for lerp, select and clone ops
 * [#17751](https://github.com/apache/tvm/pull/17751) - [PyTorch] Support one_hot, empty_like ops for ExportedProgram importer
 * [#17747](https://github.com/apache/tvm/pull/17747) - [PyTorch] Support flip, gather, take ops for ExportedProgram importer
 * [#17738](https://github.com/apache/tvm/pull/17738) - [PyTorch] Support elu, celu, selu ops for ExportedProgram importer
 * [#17726](https://github.com/apache/tvm/pull/17726) - [PyTorch] Add support for numel, empty_like and one_hot ops
 * [#17707](https://github.com/apache/tvm/pull/17707) - [PyTorch] Add support for gather, flip and take ops
 * [#17702](https://github.com/apache/tvm/pull/17702) - [PyTorch] Add support for celu, selu, is_floating_point ops
 * [#17694](https://github.com/apache/tvm/pull/17694) - [PyTorch] Add support for elu, hardtanh ops
 * [#17689](https://github.com/apache/tvm/pull/17689) - [PyTorch] Support several binary ops for ExportedProgram importer
 * [#17672](https://github.com/apache/tvm/pull/17672) - [PyTorch] Refactor binary ops tests
 * [#17679](https://github.com/apache/tvm/pull/17679) - [PyTorch] Support several unary ops for ExportedProgram importer
 * [#17668](https://github.com/apache/tvm/pull/17668) - [PyTorch] Add support for and_, lshift, min, or_, rshift, xor ops
 * [#17664](https://github.com/apache/tvm/pull/17664) - [PyTorch] Add support for ge, gt, le, mod, ne ops
 * [#17659](https://github.com/apache/tvm/pull/17659) - [PyTorch] Add support for bitwise_not, isfinite, isinf, isnan, logical_not, sign and square ops
 * [#17622](https://github.com/apache/tvm/pull/17622) - [PyTorch] Add support for abs, ceil, erf, floor, log ops and refactor unary tests
 * [#17566](https://github.com/apache/tvm/pull/17566) - [ONNX] Add prim experssion support to Neg converter and update Arange converter to use relax.op.arange
 * [#17642](https://github.com/apache/tvm/pull/17642) - [ONNX]replace topi.split with relax.op.split in the onnx frontend
 * [#17674](https://github.com/apache/tvm/pull/17674) - [KVCache] PagedKVCache refactor, FlashInfer JIT and MLA integration
 * [#17618](https://github.com/apache/tvm/pull/17618) - [KVCache] TIR attention kernel support for MLA
 * [#17615](https://github.com/apache/tvm/pull/17615) - [KVCache] Add KV Cache for CPU Runtime
 * [#17616](https://github.com/apache/tvm/pull/17616) - [Runtime][KVCache] Initial interface setup for MLA
 * [#17782](https://github.com/apache/tvm/pull/17782) - [Frontend] Support max/min in frontend op interface
 * [#17758](https://github.com/apache/tvm/pull/17758) - Allow ingesting tensor.chunk() from exported torch program
 * [#17781](https://github.com/apache/tvm/pull/17781) - Enable bfloat16 for softmax struct-info inference
 * [#17752](https://github.com/apache/tvm/pull/17752) - Batch norm correctness on eval mode
 * [#17774](https://github.com/apache/tvm/pull/17774) - check for tensor_meta in exported_program_translator
 * [#17757](https://github.com/apache/tvm/pull/17757) - Tensor.split with uneven tensors
 * [#17749](https://github.com/apache/tvm/pull/17749) - Move TIR backend to gpu_generic
 * [#17725](https://github.com/apache/tvm/pull/17725) - Ingest Tensor.clamp from torch export
 * [#17724](https://github.com/apache/tvm/pull/17724) - Add support to ingest Tensor.expand_as()
 * [#17723](https://github.com/apache/tvm/pull/17723) - Add torch exported program ingestion capability for Tensor.detach(), Tensor.copy_, and aten.lift_fresh_copy
 * [#17721](https://github.com/apache/tvm/pull/17721) - Allow ingesting Upsample module from torch.export either using Size or Scale Factor argument
 * [#17722](https://github.com/apache/tvm/pull/17722) - Allow ingesting vector_norm from torch.export
 * [#17728](https://github.com/apache/tvm/pull/17728) - ingest Tensor.contiguous from torch export
 * [#17700](https://github.com/apache/tvm/pull/17700) - Fix tree attention for Qwen2-1.5 models
 * [#17682](https://github.com/apache/tvm/pull/17682) - Add support for func attr inheritance in SplitLayoutRewritePreproc
 * [#17654](https://github.com/apache/tvm/pull/17654) - [BYOC] OpenCLML offload support for Relax
 * [#17633](https://github.com/apache/tvm/pull/17633) - Pipeline file reorganization
 * [#17626](https://github.com/apache/tvm/pull/17626) - Initial setup of relax backend pipeline
 * [#17568](https://github.com/apache/tvm/pull/17568) - [PASS] Convert layout pass and ops enhanced to support sub indexing

### Runtime
 * [#17614](https://github.com/apache/tvm/pull/17614) - [CLML] Profiling options enabled for CLML
 * [#17614](https://github.com/apache/tvm/pull/17614) - [CLML] Profiling options enabled for CLML
 * [#17570](https://github.com/apache/tvm/pull/17570) - [OPENCL] Bugfix

### TIR
 * [#17799](https://github.com/apache/tvm/pull/17799) - Fix reduce buffer allocation position
 * [#17783](https://github.com/apache/tvm/pull/17783) - [REFACTOR]remove legacy tir::any
 * [#17706](https://github.com/apache/tvm/pull/17706) - Minor fix for default GPU schedule
 * [#17579](https://github.com/apache/tvm/pull/17579) - [SoftwarePipeline] Ensure pipeline epilogue and prologue do not overlap
 * [#17584](https://github.com/apache/tvm/pull/17584) - [LoopPartition] enforcement on loop partition control

### TVMC
 * [#17606](https://github.com/apache/tvm/pull/17606) - Bug fix

### cuda & cutlass & tensorrt
 * [#17789](https://github.com/apache/tvm/pull/17789) - [CUTLASS] Add blockwise scale gemm/bmm kernels
 * [#17741](https://github.com/apache/tvm/pull/17741) - [Codegen][CUDA] Fix codegen of cast among vector bfloat16, fp8 and fp4
 * [#17708](https://github.com/apache/tvm/pull/17708) - [CUDA] FP4 cast and reinterpret support
 * [#17639](https://github.com/apache/tvm/pull/17639) - [CUDA] Remove htanh from unsupported math ops for CUDA 12.8
 * [#16950](https://github.com/apache/tvm/pull/16950) - [Codegen, CUDA] Add FP8 Tensor Core Codegen

### web
 * [#17695](https://github.com/apache/tvm/pull/17695) - [WASM] Update wasm include in accordance to kv cache revamp

### Misc
 * [#17796](https://github.com/apache/tvm/pull/17796) - [Cublas] Added support for bfloat16 while dispatching to cublas kernels
 * [#17763](https://github.com/apache/tvm/pull/17763) - [Flashinfer] Added jit flow for sampling kernel
 * [#17811](https://github.com/apache/tvm/pull/17811) - [NFC] Fix `explict` typo
 * [#17780](https://github.com/apache/tvm/pull/17780) - [3rdparty] Enable bfloat16 for custom allreduce kernel
 * [#17784](https://github.com/apache/tvm/pull/17784) - [REFACTOR] Phase out StackVM
 * [#17750](https://github.com/apache/tvm/pull/17750) - BugFix: Relax comment
 * [#17748](https://github.com/apache/tvm/pull/17748) - [Codegen] Support codegen for vectorized tir.ShuffleNode
 * [#17743](https://github.com/apache/tvm/pull/17743) - Fix: Change variable i to x in split operation in cross_compilation_and_rpc.py
 * [#17730](https://github.com/apache/tvm/pull/17730) - [Attention] Added caching for flashinfer binaries during JIT
 * [#17733](https://github.com/apache/tvm/pull/17733) - [Refactor] Clean up Relay references in the codebase
 * [#17739](https://github.com/apache/tvm/pull/17739) - [BF16] Support ndarray.asnumpy() to bfloat16 tensor natively using ml_dtypes
 * [#17734](https://github.com/apache/tvm/pull/17734) - Remove Google Analytics
 * [#17731](https://github.com/apache/tvm/pull/17731) - [IR] Compact Functor vtable
 * [#17736](https://github.com/apache/tvm/pull/17736) - Fix typos in comments and strings
 * [#17670](https://github.com/apache/tvm/pull/17670) - [DataType] BF16 Support
 * [#17727](https://github.com/apache/tvm/pull/17727) - [FFI] Fix dynamic FFI index to ensure compatibility
 * [#17718](https://github.com/apache/tvm/pull/17718) - [Refactor] Migrate build API to `tvm.compile`
 * [#17714](https://github.com/apache/tvm/pull/17714) - [FFI] Phase out ctypes fallback in favor of cython
 * [#17716](https://github.com/apache/tvm/pull/17716) - Fix the get_target_compute_version for sm >= 100
 * [#17710](https://github.com/apache/tvm/pull/17710) - [Refactor] Introduce base Executable class and `tvm.compile` interface
 * [#17713](https://github.com/apache/tvm/pull/17713) - [REFACTOR] Cleanup legacy relay runtime data structures
 * [#17712](https://github.com/apache/tvm/pull/17712) - [DataType] Rename FP8 dtypes to standard names
 * [#17703](https://github.com/apache/tvm/pull/17703) - Fix typos in multiple files
 * [#17693](https://github.com/apache/tvm/pull/17693) - updated the assert in BindParams to allow tvm.relax.Constant
 * [#17701](https://github.com/apache/tvm/pull/17701) - [Refactor] Remove legacy TE schedule tag
 * [#17683](https://github.com/apache/tvm/pull/17683) - [MSC] Remove relay
 * [#17688](https://github.com/apache/tvm/pull/17688) - Fix relax.ccl.scatter_from_worker0 assert
 * [#17630](https://github.com/apache/tvm/pull/17630) - [Codegen] FP4 support
 * [#17685](https://github.com/apache/tvm/pull/17685) - [REFACTOR] Cleanup legacy TE-based passes
 * [#17681](https://github.com/apache/tvm/pull/17681) - [REFACTOR] Followup cleanup of relay phase out
 * [#17678](https://github.com/apache/tvm/pull/17678) - Bump 3rdparty/cutlass_fpA_intB_gemm
 * [#17669](https://github.com/apache/tvm/pull/17669) - [REFACTOR] Allow target dependent default tir pipeline dispatch in tir.build()
 * [#17665](https://github.com/apache/tvm/pull/17665) - [REFACTOR] move build flow from C++ to Python
 * [#17624](https://github.com/apache/tvm/pull/17624) - Added support for normal MLA kernel
 * [#17641](https://github.com/apache/tvm/pull/17641) - Pick up vector length from 'zvlXXXb' (RVV) mattr for riscv
 * [#17666](https://github.com/apache/tvm/pull/17666) - [Refactor] Improve TargetHasSVE function with optional target handling
 * [#17661](https://github.com/apache/tvm/pull/17661) - [Refactor] Phrase out python dependency `decorator`
 * [#17662](https://github.com/apache/tvm/pull/17662) - [REFACTOR] Phase out te.Schedule c++ components
 * [#17660](https://github.com/apache/tvm/pull/17660) - [REFACTOR] Phase out relay c++ components 
 * [#17655](https://github.com/apache/tvm/pull/17655) - Upgrading onnx and onnxrt verions
 * [#17657](https://github.com/apache/tvm/pull/17657) - Update argument order for relax.op.pad to make it round-trippable
 * [#17658](https://github.com/apache/tvm/pull/17658) - [REFACTOR] Phase out te.schedule python components 
 * [#17653](https://github.com/apache/tvm/pull/17653) - Update images to 20250214-034537-bd1411f8
 * [#17656](https://github.com/apache/tvm/pull/17656) - [REFACTOR] Phase out relay python components
 * [#17649](https://github.com/apache/tvm/pull/17649) - [Refactor] Phase out python dependency attrs
 * [#17644](https://github.com/apache/tvm/pull/17644) - Bump rollup from 2.79.1 to 2.79.2 in /web
 * [#17637](https://github.com/apache/tvm/pull/17637) - [PYTHON] Build cython by default
 * [#17631](https://github.com/apache/tvm/pull/17631) - Handle vector width (VLEN) for RISCV arches
 * [#17613](https://github.com/apache/tvm/pull/17613) - Bug Fix: Removed unused code
 * [#17585](https://github.com/apache/tvm/pull/17585) - [Relay]Disable InferType if it was done and no changes after previous pass
 * [#17605](https://github.com/apache/tvm/pull/17605) - [Refactor] Phase out legacy example apps
 * [#17603](https://github.com/apache/tvm/pull/17603) - [Refactor] Phase out legacy docs
 * [#17513](https://github.com/apache/tvm/pull/17513) - [GRAPH RT] Additional API support




## v0.21.0 (2025-07-17)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax (especial PyTorch frontend), FFI etc.

Please visit the full listing of commits for a complete view: [v0.21.dev0...v0.21.0.rc0](https://github.com/apache/tvm/compare/v0.21.dev0...v0.21.0.rc0).

### Community

None.

### RFCs

None.

### Arith
 * [#18067](https://github.com/apache/tvm/pull/18067) - Add IsBound method to ConstIntBoundAnalyzer
 * [#18031](https://github.com/apache/tvm/pull/18031) - Canonicalize mul-coefficient to rhs
 * [#18025](https://github.com/apache/tvm/pull/18025) - Fix canonical simplify for LE with incorrect range assumptions

### BugFix
 * [#18115](https://github.com/apache/tvm/pull/18115) - [Fix][Serialization] Add support for NaN value serialization
 * [#18103](https://github.com/apache/tvm/pull/18103) - [Fix] Replace dmlc::Error with std::exception in VerifyGPUCode
 * [#18092](https://github.com/apache/tvm/pull/18092) - [Fix] Fix ExecBuilderDeclareFunction method name in exec_builder.py
 * [#18087](https://github.com/apache/tvm/pull/18087) - fix exception when tvm not built with llvm support
 * [#18035](https://github.com/apache/tvm/pull/18035) - [CUDA] Fix: Update settings for rerun on Increase FloatImm precision when printing 64 bit values in CUDA codegen
 * [#17968](https://github.com/apache/tvm/pull/17968) - [Relax][Pytorch] Bugfix of conv_transpose1d and conv_transpose2d
 * [#17950](https://github.com/apache/tvm/pull/17950) - [Fix][Relax] Fix dangling reference in GetTargetFunctions()
 * [#17902](https://github.com/apache/tvm/pull/17902) - Fix off-by-one error in the type index range check within Object::IsInstance()
 * [#17882](https://github.com/apache/tvm/pull/17882) - [Relax][Pytorch] Fix incorrect behaviour of % (mod) operator in TVM frontend
 * [#17875](https://github.com/apache/tvm/pull/17875) - [Relax][Pytorch] Incorrect Handling of In-Place Ops in FX-Based TVM Frontend
 * [#17838](https://github.com/apache/tvm/pull/17838) - [TIR] Schedule support reverse-inline with reduction blocks

### CI
 * [#18071](https://github.com/apache/tvm/pull/18071) - Update windows to 2025
 * [#18058](https://github.com/apache/tvm/pull/18058) - [TEST] Move temp files into tempdir
 * [#18037](https://github.com/apache/tvm/pull/18037) - Further robustify is_last_build check
 * [#17981](https://github.com/apache/tvm/pull/17981) - Update images to `20250513-063354-70aa3797`
 * [#17891](https://github.com/apache/tvm/pull/17891) - Update images to 20250428-080833-03eadc65
 * [#17905](https://github.com/apache/tvm/pull/17905) - Install PyTorch 2.7 compatible with CUDA 11.8
 * [#17887](https://github.com/apache/tvm/pull/17887) - Upgrade pytorch to 2.7.0, torchvision to 0.22.0, and vulkan sdk to 1.4.309
 * [#17846](https://github.com/apache/tvm/pull/17846) - Upgrade ubuntu runner image for GitHub CI

### Docker
 * [#17955](https://github.com/apache/tvm/pull/17955) - [CI] Reintroduce NNEF to CI images

### Docs
 * [#18056](https://github.com/apache/tvm/pull/18056) - Update installation instruction based ffi refactor

### Frontend
 * [#18090](https://github.com/apache/tvm/pull/18090) - [Relax][ONNX] Update Reduce ops to support axes as input
 * [#18072](https://github.com/apache/tvm/pull/18072) - [Relax][ONNX] Update ReduceL1 to opset 18
 * [#18016](https://github.com/apache/tvm/pull/18016) - [Relax][ONNX] Replace deprecated `mapping.TENSOR_TYPE_TO_NP_TYPE` usage
 * [#18001](https://github.com/apache/tvm/pull/18001) - [Relax][ONNX] Fix: bitwise_not misclassified as binary (is …
 * [#17990](https://github.com/apache/tvm/pull/17990) - [Relax]Fix: Output tensor with zero dimension after torch.u…
 * [#17925](https://github.com/apache/tvm/pull/17925) - [Relax][PyTorch] Re-enable test_subgraph_capture in dynamo test
 * [#17980](https://github.com/apache/tvm/pull/17980) - [ONNX] Make bias input optional in LayerNormalization
 * [#17918](https://github.com/apache/tvm/pull/17918) - [Relax][PyTorch] Add ReLU6 Op Support for Exported Program and FX graph
 * [#17930](https://github.com/apache/tvm/pull/17930) - [Relax][PyTorch] Add torch.outer Op Support for Exported Program and FX graph 
 * [#17932](https://github.com/apache/tvm/pull/17932) - [Relax][PyTorch] Add UpSample Bicubic Op Support for Exported Program and FX graph
 * [#17921](https://github.com/apache/tvm/pull/17921) - [Relax][PyTorch] Add AvgPool 1D and 3D Op Support for Exported Program and FX graph
 * [#17922](https://github.com/apache/tvm/pull/17922) - [Relax][PyTorch] Add Adaptive AvgPool 1D and 3D Op Support for Exported Program and FX graph
 * [#17863](https://github.com/apache/tvm/pull/17863) - [Relax][PyTorch] CrossEntropyLoss
 * [#17919](https://github.com/apache/tvm/pull/17919) - [Relax][PyTorch] Add MaxPool 1D and 3D Op Support for Exported Program and FX graph
 * [#17926](https://github.com/apache/tvm/pull/17926) - [Relax][PyTorch] Add tests for all the dtypes supported in the PyTorch frontend
 * [#17924](https://github.com/apache/tvm/pull/17924) - [Relax][PyTorch] Add div.Tensor_mode and trunc Op Support for Exported Program and FX graph
 * [#17904](https://github.com/apache/tvm/pull/17904) - [Relax][PyTorch] Add Meshgrid Op Support for Exported Program and FX graph
 * [#17915](https://github.com/apache/tvm/pull/17915) - [Relax][PyTorch] Add support for linspace op in fx graph
 * [#17886](https://github.com/apache/tvm/pull/17886) - [Relax][PyTorch] Add Pixel Shuffle Op Support for Exported Program and FX graph
 * [#17908](https://github.com/apache/tvm/pull/17908) - [Relax][PyTorch] Add support for eye op in fx graph
 * [#17893](https://github.com/apache/tvm/pull/17893) - [Relax][Pytorch] Add fmod support
 * [#17894](https://github.com/apache/tvm/pull/17894) - [Relax][PyTorch] Support torch.bfloat16 dtype in pytorch frontend
 * [#17878](https://github.com/apache/tvm/pull/17878) - [Relax][PyTorch] Add torch.isin Op Support for Exported Program and FX graph
 * [#17889](https://github.com/apache/tvm/pull/17889) - [Relax][PyTorch] Support linspace op for ExportedProgram importer
 * [#17868](https://github.com/apache/tvm/pull/17868) - [Relax][Pytorch] Add support for ones_like, zero_, zeros, type_as, item ops
 * [#17857](https://github.com/apache/tvm/pull/17857) - [Relax][PyTorch] Refactor norm op for ExportedProgram importer
 * [#17852](https://github.com/apache/tvm/pull/17852) - [Relax][PyTorch] Sort.default
 * [#17871](https://github.com/apache/tvm/pull/17871) - [Relax][Pytorch] Add support for bitwise_or op support
 * [#17836](https://github.com/apache/tvm/pull/17836) - [Relax][PyTorch] support for index.Tensor
 * [#17864](https://github.com/apache/tvm/pull/17864) - [Relax][PyTorch] Support eye op for ExportedProgram importer
 * [#17858](https://github.com/apache/tvm/pull/17858) - [Relax][PyTorch] Add copy_ op support in fxGraph
 * [#17851](https://github.com/apache/tvm/pull/17851) - [Relax][PyTorch] Support `leaky_relu_.default` and `reshape_as.default` in ExportedProgram frontend
 * [#17843](https://github.com/apache/tvm/pull/17843) - [Relax][PyTorch] Add mul_.Tensor, max.default, min.default and pow.Scalar Op Support into Exported Program Frontend
 * [#17821](https://github.com/apache/tvm/pull/17821) - [Relax][PyTorch] Add Pad Op Support for Exported Program and FX graph
 * [#17819](https://github.com/apache/tvm/pull/17819) - [Relax][PyTorch] Add Stack Op Support for Exported Program 
 * [#17849](https://github.com/apache/tvm/pull/17849) - [Relax][PyTorch] Add RSub Op Support for Exported Program and FX graph
 * [#17850](https://github.com/apache/tvm/pull/17850) - [Relax][Pytorch] Add masked_fill op support in ExportedProgram
 * [#17816](https://github.com/apache/tvm/pull/17816) - [Relax][PyTorch] Add PReLU Op Support for Exported Program and FX graph
 * [#17803](https://github.com/apache/tvm/pull/17803) - [Relax][PyTorch] Add Logaddexp op support for exported program 
 * [#17841](https://github.com/apache/tvm/pull/17841) - [Relax][PyTorch] Add support for norm op
 * [#17832](https://github.com/apache/tvm/pull/17832) - [Relax][PyTorch] full.default, full_like.default, ones.default 
 * [#17830](https://github.com/apache/tvm/pull/17830) - [Relax][PyTorch] Support narrow and broadcast_to ops for ExportedProgram importer

### LLVM
 * [#17859](https://github.com/apache/tvm/pull/17859) - [Codegen] Enable SVE/VLA for RISCV targets
 * [#17958](https://github.com/apache/tvm/pull/17958) - Fix JIT unknown reloc issue for case of RISCV
 * [#17954](https://github.com/apache/tvm/pull/17954) - [FFI]Fix compilation errors with clang20

### Metal
 * [#18034](https://github.com/apache/tvm/pull/18034) - Fix `GetFunction` of metal runtime

### ROCm
 * [#18029](https://github.com/apache/tvm/pull/18029) - Fix ROCm build after FFI refactor

### Relax
 * [#18102](https://github.com/apache/tvm/pull/18102) - Fix rotary embedding buffer size calculation
 * [#17928](https://github.com/apache/tvm/pull/17928) - [KVCache] Per Layer Sliding Window
 * [#17840](https://github.com/apache/tvm/pull/17840) - Refactor missing op check into shared utility for Torch frontends
 * [#17826](https://github.com/apache/tvm/pull/17826) - Fix Torch frontends to report all the missing ops

### Runtime
 * [#18097](https://github.com/apache/tvm/pull/18097) - CutensorMap support

### TIR
 * [#18068](https://github.com/apache/tvm/pull/18068) - Extend address_of to support Buffer objects
 * [#18069](https://github.com/apache/tvm/pull/18069) - Fix block access region detection for nested let bindings
 * [#18057](https://github.com/apache/tvm/pull/18057) - Phase out ProducerStore, ProducerRealize and Prefetch

### TOPI
 * [#18039](https://github.com/apache/tvm/pull/18039) - [Relax] Support InstanceNorm & Bugfix of InstanceNorm
 * [#18063](https://github.com/apache/tvm/pull/18063) - [NN][Layer_Norm] Fix layer_norm error with reduce-only axes
 * [#18006](https://github.com/apache/tvm/pull/18006) - Fix index handling in expand_like operator for axis expansion
 * [#18015](https://github.com/apache/tvm/pull/18015) - Support integer type input for log10
 * [#17942](https://github.com/apache/tvm/pull/17942) - Add shape validation to prevent negative dimensions in conv operations

### Vulkan
 * [#18005](https://github.com/apache/tvm/pull/18005) - Add TIR unary trigonometric/hyperbolic intrinsic definitions

### cuda & cutlass & tensorrt
 * [#18064](https://github.com/apache/tvm/pull/18064) - [CUTLASS] Fix CUTLASS kernel build on Hopper
 * [#18033](https://github.com/apache/tvm/pull/18033) - [CUTLASS] Add GeMM kernels for Blackwell GPUs
 * [#18024](https://github.com/apache/tvm/pull/18024) - [CUDA] Fix thrust with latest FFI refactor
 * [#18118](https://github.com/apache/tvm/pull/18118) - bump cutlass_fpA_intB_gemm
 * [#18113](https://github.com/apache/tvm/pull/18113) - [CMake] Refine C++/CUDA standard settings in CMakeLists.txt

### FFI
 * [#18076](https://github.com/apache/tvm/pull/18076) - [FFI][REFACTOR] Stablize container ABI and implementation
 * [#18091](https://github.com/apache/tvm/pull/18091) - [FFI] Provide Field Visit bridge so we can do gradual transition
 * [#18095](https://github.com/apache/tvm/pull/18095) - [FFI][REFACTOR] Migrate attrs to use new reflection
 * [#18083](https://github.com/apache/tvm/pull/18083) - [FFI] Update typeinfo to speedup parent reflection
 * [#18077](https://github.com/apache/tvm/pull/18077) - [FFI] Optimize atomic decref in Object
 * [#18065](https://github.com/apache/tvm/pull/18065) - [FFI] Introduce FFI reflection support in python
 * [#18062](https://github.com/apache/tvm/pull/18062) - [FFI][REFACTOR] Update registry to have complete meta-data
 * [#18059](https://github.com/apache/tvm/pull/18059) - [FFI][REFACTOR] Enhance reflection
 * [#18050](https://github.com/apache/tvm/pull/18050) - [FFI] Enhance FFI Object exception safety during init
 * [#18121](https://github.com/apache/tvm/pull/18121) - Revert "[FFI] Replace `Arg2Str` with a more powerful `for_each`"
 * [#18117](https://github.com/apache/tvm/pull/18117) - [FFI] Replace `Arg2Str` with a more powerful `for_each`
 * [#18116](https://github.com/apache/tvm/pull/18116) - [FFI] Use fold expression to simplify for_each
 * [#18114](https://github.com/apache/tvm/pull/18114) - [FFI] Replace `__attribute__` with C++ standard attributes
 * [#18112](https://github.com/apache/tvm/pull/18112) - [FFI] Cleanup visit_attrs attribute after refactor
 * [#18111](https://github.com/apache/tvm/pull/18111) - [FFI] Introduce GlobalDef for function registration
 * [#18106](https://github.com/apache/tvm/pull/18106) - [REFACTOR][FFI] Phase out old VisitAttrs mechanism
 * [#18042](https://github.com/apache/tvm/pull/18042) - [REFACTOR][FFI] Update symbol name for library module
 * [#18023](https://github.com/apache/tvm/pull/18023) - [FFI] More strict tuple constructor checking
 * [#18022](https://github.com/apache/tvm/pull/18022) - [REFACTOR][FFI] Cleanup PackedFunc redirections
 * [#18020](https://github.com/apache/tvm/pull/18020) - [REFACTOR][PYTHON] Phase out tvm.\_ffi and Limited API support
 * [#17979](https://github.com/apache/tvm/pull/17979) - [FFI][REFACTOR] Update to distinguish as and cast
 * [#17983](https://github.com/apache/tvm/pull/17983) - [FFI][JVM] Upgrade tvm4j to latest FFI
 * [#18010](https://github.com/apache/tvm/pull/18010) - [REFACTOR][FFI] Phase out legacy C API
 * [#17943](https://github.com/apache/tvm/pull/17943) - [FFI] Variant specialize for all ObjectRef
 * [#17939](https://github.com/apache/tvm/pull/17939) - [REFACTOR] Phase out legacy rust ffi
 * [#17940](https://github.com/apache/tvm/pull/17940) - [REFACTOR] Phase out legacy go ffi
 * [#17931](https://github.com/apache/tvm/pull/17931) - [REFACTOR][FFI][RPC] Migrate RPC to use the latest FFI ABI
 * [#17929](https://github.com/apache/tvm/pull/17929) - [REFACTOR][FFI] Cleanup container redirections
 * [#17927](https://github.com/apache/tvm/pull/17927) - [FFI][FEAT] AutoDLPack for taking external tensor objects
 * [#17923](https://github.com/apache/tvm/pull/17923) - [REFACTOR][FFI] Cleanup PackedFunc related redirection
 * [#17920](https://github.com/apache/tvm/pull/17920) - [REFACTOR] Introduce and modernize ffi system

### web
 * [#17946](https://github.com/apache/tvm/pull/17946) - [REFACTOR][FFI]Upgrade Web Runtime to new FFI
 * [#17917](https://github.com/apache/tvm/pull/17917) - [WebGPU][CodeGen] Override PrintVecElemLoad and Store for WebGPU

### Misc
 * [#18104](https://github.com/apache/tvm/pull/18104) - Add LLVM Legalization for tir.erf
 * [#18107](https://github.com/apache/tvm/pull/18107) - fix: guard tensormap with cuda version check
 * [#18101](https://github.com/apache/tvm/pull/18101) - [REFACTOR] Formalize namespace for all objects
 * [#18040](https://github.com/apache/tvm/pull/18040) - Add support for bucketize
 * [#18098](https://github.com/apache/tvm/pull/18098) - [REFACTOR] Transition VisitAttrs to new reflection mechanism
 * [#18096](https://github.com/apache/tvm/pull/18096) - [REFACTOR] Transition VisitAttrs to new reflection mechanism in tir/ir_builder/meta_schedule
 * [#18093](https://github.com/apache/tvm/pull/18093) - [NVSHMEM] Extend CUDA backend to compile and link TIR modules with NVSHMEM
 * [#18088](https://github.com/apache/tvm/pull/18088) - [Script] Enhance alloc buffer handling in nested frames
 * [#18086](https://github.com/apache/tvm/pull/18086) - [SCRIPT] Bump Python minimum version to 3.9 and update AST compatibility
 * [#18075](https://github.com/apache/tvm/pull/18075) - add support for softsign op
 * [#18079](https://github.com/apache/tvm/pull/18079) - [Script] Add support for merging block annotations
 * [#18080](https://github.com/apache/tvm/pull/18080) - [REFACTOR] Phase out LegacyReprPrinter and improve CommonSubExprElim
 * [#18078](https://github.com/apache/tvm/pull/18078) - [REFACTOR] Phase out the RelaxExpr.checked_type in favor of struct_info
 * [#18073](https://github.com/apache/tvm/pull/18073) - [NVSHMEM] Update NDArray allocation
 * [#18066](https://github.com/apache/tvm/pull/18066) - [Script] Remove deprecated attributes from Constant AST node
 * [#18060](https://github.com/apache/tvm/pull/18060) - Add Python functor support for TIR expressions and statements
 * [#18054](https://github.com/apache/tvm/pull/18054) - [Pytest] Remove obsolete test suite entries
 * [#18036](https://github.com/apache/tvm/pull/18036) - Add support for hamming_window op
 * [#18049](https://github.com/apache/tvm/pull/18049) - [Refactor] Rename `relax_vm` to `vm`
 * [#18046](https://github.com/apache/tvm/pull/18046) - [3rdparty] Phasing out FlashInfer AOT from 3rdparty
 * [#18047](https://github.com/apache/tvm/pull/18047) - [Backend] JIT compile FlashInfer kernel with FFI header
 * [#18041](https://github.com/apache/tvm/pull/18041) - [DTYPE] Fix dtype functions after dtype refactor
 * [#18043](https://github.com/apache/tvm/pull/18043) - [REFACTOR] Phase out the relax tuning_api
 * [#18038](https://github.com/apache/tvm/pull/18038) - Resolving inconsistency between attention/attention_bias
 * [#18027](https://github.com/apache/tvm/pull/18027) - [Dtype] Low-precision Blackwell Datatype Support
 * [#17985](https://github.com/apache/tvm/pull/17985) - [Codegen] Resolve issue #17965 where the same model produces different outputs on the LLVM (CPU) and CUDA (GPU) backends
 * [#17978](https://github.com/apache/tvm/pull/17978) - Fix IR generation conflict in topi.nn.simplify by separating Tensor and PrimExpr handling
 * [#18026](https://github.com/apache/tvm/pull/18026) - [Python] Fix library lookup path for pip installed packages
 * [#18019](https://github.com/apache/tvm/pull/18019) - Add op support for slice_scatter
 * [#17974](https://github.com/apache/tvm/pull/17974) - Fix FLOP estimation for EvaluateNode by implementing VisitStmt_ handler
 * [#18013](https://github.com/apache/tvm/pull/18013) - Fix RuntimeError: parallel_for_dynamic
 * [#18014](https://github.com/apache/tvm/pull/18014) - Fix division truncation in window size calculation for small dtypes in average_pool
 * [#17995](https://github.com/apache/tvm/pull/17995) - Fix zero-extent loops in PerStoreFeature to prevent crashes
 * [#17969](https://github.com/apache/tvm/pull/17969) - Add registion for the operator asinh, acosh, atanh in llvm
 * [#17972](https://github.com/apache/tvm/pull/17972) - Fix g.costs
 * [#17953](https://github.com/apache/tvm/pull/17953) - Fix sqrt/rsqrt Compatibility with Integer Data Types
 * [#17961](https://github.com/apache/tvm/pull/17961) - Fix basic FLOP estimation for WhileNode
 * [#17945](https://github.com/apache/tvm/pull/17945) - Add registion for the operator asin and acos in llvm
 * [#17951](https://github.com/apache/tvm/pull/17951) - [NODE] Fix structural equality for Array<Any> specialization
 * [#17913](https://github.com/apache/tvm/pull/17913) - [Triton] Support latest `triton.compile` interface
 * [#17911](https://github.com/apache/tvm/pull/17911) - Add op support for new_zeros op in Exported Program and fx graph frontend
 * [#17909](https://github.com/apache/tvm/pull/17909) - Add masked_fill_.scalar, logical_not.default in Exported Program frontend
 * [#17910](https://github.com/apache/tvm/pull/17910) - [RPC] Fix Bug That Change Dict When Iterate The Keys
 * [#17896](https://github.com/apache/tvm/pull/17896) - Add op support for zeros_like and fill_
 * [#17900](https://github.com/apache/tvm/pull/17900) - Fix onnx expand op
 * [#17865](https://github.com/apache/tvm/pull/17865) - Add support for index_put_ op
 * [#17839](https://github.com/apache/tvm/pull/17839) - Add op support for roll op
 * [#17844](https://github.com/apache/tvm/pull/17844) - Fix incorrect docstring in topi softmax 
 * [#17831](https://github.com/apache/tvm/pull/17831) - [3rdparty] Bump DLPack to v1.1 for float8/6/4 dtype supports
 * [#17848](https://github.com/apache/tvm/pull/17848) - Fix docstring in batch_to_space_nd and bitpack
 * [#17845](https://github.com/apache/tvm/pull/17845) - fixing incorrect docstring in upsampling.py
 * [#17808](https://github.com/apache/tvm/pull/17808) - [Install] Fix error during python/tvm installation

## v0.22.0 (2025-10-24)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax (especial PyTorch frontend), FFI etc.

Please visit the full listing of commits for a complete view: [v0.22.dev0...v0.22.0.rc0](https://github.com/apache/tvm/compare/v0.22.dev0...v0.22.0.rc0).

### Community

None.

### RFCs

None.

### BugFix
 * [#18352](https://github.com/apache/tvm/pull/18352) - [Fix] Update ShapeView use in nccl.cc
 * [#18324](https://github.com/apache/tvm/pull/18324) - Fixing binding for bert
 * [#18296](https://github.com/apache/tvm/pull/18296) - [Fix] Add libxml2 dependency to fix Windows CI build failure
 * [#18294](https://github.com/apache/tvm/pull/18294) - [Fix] Set DRefObj and CUDAIPCMemoryObj as mutable
 * [#18285](https://github.com/apache/tvm/pull/18285) - [FFI]Enable `load_inline` on macos
 * [#18287](https://github.com/apache/tvm/pull/18287) - [Hotfix] Fix the conflicts about ffi-related updated names
 * [#18281](https://github.com/apache/tvm/pull/18281) - [FFI]Fix bug of `ffi.cpp.load_inline` on Windows
 * [#18262](https://github.com/apache/tvm/pull/18262) - [NNAPI] Use kind() instead of type_key() after FFI refactor
 * [#18244](https://github.com/apache/tvm/pull/18244) - [Fix] Update FlashInfer JIT header lookup
 * [#18237](https://github.com/apache/tvm/pull/18237) - [FFI]Fix type_traits on DataType after SmallStr update
 * [#18232](https://github.com/apache/tvm/pull/18232) - [LLVM][Fix] Do not emit debuginfo on vscale or other unknown types
 * [#18219](https://github.com/apache/tvm/pull/18219) - [Fix] Resolve deadlock in PopenPoolExecutor and LocalBuilder
 * [#18207](https://github.com/apache/tvm/pull/18207) - [Fix][ONNX] No precision widening for numpy binary operations
 * [#18209](https://github.com/apache/tvm/pull/18209) - [ONNX][FRONTEND][Fix] Update Resize to accept ShapeExpr
 * [#18210](https://github.com/apache/tvm/pull/18210) - [Bug] Fix core dump in InferLayoutRMSNorm and fix typo
 * [#18208](https://github.com/apache/tvm/pull/18208) - [FFI][Fix] Update datatype registry calls to the new paths
 * [#18190](https://github.com/apache/tvm/pull/18190) - [Fix] Codegen fix for relax cutlass
 * [#18170](https://github.com/apache/tvm/pull/18170) - [Fix] Fix the wrong check for tuple node in #18163
 * [#18174](https://github.com/apache/tvm/pull/18174) - [Misc]Fix missing PadAttrs register in op_attrs.py
 * [#18158](https://github.com/apache/tvm/pull/18158) - Fix NCCL build with GlobalDef registration
 * [#18140](https://github.com/apache/tvm/pull/18140) - [NNAPI] Fix type mismatch and test_mean annotation
 * [#18138](https://github.com/apache/tvm/pull/18138) - [Fix][ONNX] Fixed constant ROI handling in resize2d when loading onnx models
 * [#18137](https://github.com/apache/tvm/pull/18137) - [Fix][ONNX] Fix CumSum conversion when loading ONNX model

### CI
 * [#18245](https://github.com/apache/tvm/pull/18245) - [LLVM][MSWIN]Fix LLVM module build with latest CI update
 * [#18227](https://github.com/apache/tvm/pull/18227) - Exit the build for AbortException
 * [#18145](https://github.com/apache/tvm/pull/18145) - [Test] Use roi_list variable instead of hardcoded values in ROI tensor creation

### Docs
 * [#18279](https://github.com/apache/tvm/pull/18279) - [FFI]Initial bringup of cpp docs
 * [#18264](https://github.com/apache/tvm/pull/18264) - Misc docs fix
 * [#18263](https://github.com/apache/tvm/pull/18263) - [FFI]Initial docs scaffolding
 * [#18261](https://github.com/apache/tvm/pull/18261) - [FFI]Add missing files in packaging example
 * [#18256](https://github.com/apache/tvm/pull/18256) - [FFI]Wheel Packaging
 * [#18128](https://github.com/apache/tvm/pull/18128) - [Doc] Visualize the architecture using a UML sequence diagram

### Frontend
 * [#18143](https://github.com/apache/tvm/pull/18143) - [ONNX] Extend axes for layer_norm when gamma/beta are multi-dimensional

### LLVM
 * [#18204](https://github.com/apache/tvm/pull/18204) - Fixes up to the latest LLVM21
 * [#18202](https://github.com/apache/tvm/pull/18202) - [CPPTEST] Small fixes for LLVM >= 20

### MetaSchedule
 * [#18243](https://github.com/apache/tvm/pull/18243) - [LLVM]Add RISCV V-extension v1.0 kernels to metaschedule

### Metal
 * [#18290](https://github.com/apache/tvm/pull/18290) - Fix MetalModuleCreate
 * [#18283](https://github.com/apache/tvm/pull/18283) - [Fix]Fix type for device array in Metal API

### ROCm
 * [#18225](https://github.com/apache/tvm/pull/18225) - Minor fixes for latest refactor

### FFI
 * [#18375](https://github.com/apache/tvm/pull/18375) - [TE] [FFI] Fix broken axis/reduce_axis properties in BaseComputeOp and ScanOp after FFI refactoring
 * [#18376](https://github.com/apache/tvm/pull/18376) - [FFI] Bump tvm-ffi to 0.1.0rc2
 * [#18370](https://github.com/apache/tvm/pull/18370) - [FFI] Bump tvm-ffi dependency
 * [#18354](https://github.com/apache/tvm/pull/18354) - [FFI][ABI] Bump tvm-ffi to latest
 * [#18349](https://github.com/apache/tvm/pull/18349) - [FFI][ABI] Bump tvm-ffi to latest
 * [#18345](https://github.com/apache/tvm/pull/18345) - [FFI][ABI] Bump tvm-ffi version to reflect RC ABI Update
 * [#18332](https://github.com/apache/tvm/pull/18332) - [FFI][ABI] Bump version ffi to latest
 * [#18314](https://github.com/apache/tvm/pull/18314) - [REFACTOR][FFI] Split tvm-ffi into a separate repo
 * [#18312](https://github.com/apache/tvm/pull/18312) - [FFI][REFACTOR] Update TVM_FFI_STATIC_INIT_BLOCK to fn style
 * [#18311](https://github.com/apache/tvm/pull/18311) - [FFI][ABI] Better String and Nested Container handling
 * [#18308](https://github.com/apache/tvm/pull/18308) - [FFI][ABI] Refactor the naming of DLPack speed converter
 * [#18307](https://github.com/apache/tvm/pull/18307) - [FFI] Update `load_inline` interface
 * [#18306](https://github.com/apache/tvm/pull/18306) - [FFI][ABI][REFACTOR] Enhance DLPack Exchange Speed and Behavior
 * [#18302](https://github.com/apache/tvm/pull/18302) - [FFI][REFACTOR] Refactor python ffi call mechanism for perf
 * [#18298](https://github.com/apache/tvm/pull/18298) - [FFI] Fix system library symbol lookup
 * [#18297](https://github.com/apache/tvm/pull/18297) - [FFI] Temp skip windows tests
 * [#18295](https://github.com/apache/tvm/pull/18295) - [FFI][ABI] Introduce generic stream exchange protocol
 * [#18289](https://github.com/apache/tvm/pull/18289) - [FFI][REFACTOR] Streamline Object Declare Macros
 * [#18284](https://github.com/apache/tvm/pull/18284) - [FFI][REFACTOR] Introduce UnsafeInit and enhance ObjectRef null safety
 * [#18282](https://github.com/apache/tvm/pull/18282) - [FFI] Relax default alignment and continguous requirement
 * [#18280](https://github.com/apache/tvm/pull/18280) - [FFI][REFACTOR] Cleanup namespace
 * [#18278](https://github.com/apache/tvm/pull/18278) - [FFI] Temp skip load_inline tests nonlinux
 * [#18277](https://github.com/apache/tvm/pull/18277) - [FFI][REFACTOR] Cleanup tvm_ffi python API and types
 * [#18276](https://github.com/apache/tvm/pull/18276) - [FFI] Add ffi::Tensor.strides()
 * [#18275](https://github.com/apache/tvm/pull/18275) - [FFI][REFACTOR][ABI] Rename NDArray to Tensor
 * [#18274](https://github.com/apache/tvm/pull/18274) - [FFI] Update the interface of `ffi.load_inline` to match torch
 * [#18273](https://github.com/apache/tvm/pull/18273) - [FFI][ABI] Append symbol prefix for ffi exported functions
 * [#18272](https://github.com/apache/tvm/pull/18272) - [FFI] Construct NDArray.strides by default
 * [#18271](https://github.com/apache/tvm/pull/18271) - [FFI] Support inline module
 * [#18270](https://github.com/apache/tvm/pull/18270) - [FFI] Support Opaque PyObject
 * [#18266](https://github.com/apache/tvm/pull/18266) - [FFI] Update torch stream getter to use native torch c api
 * [#18259](https://github.com/apache/tvm/pull/18259) - [FFI][ABI] Introduce weak rc support
 * [#18258](https://github.com/apache/tvm/pull/18258) - [FFI] fix two seemingly migration issue
 * [#18254](https://github.com/apache/tvm/pull/18254) - [FFI][ABI] ABI Updates to for future metadata and complex ordering
 * [#18249](https://github.com/apache/tvm/pull/18249) - [FFI][CMAKE] Revert cmake libbacktrace URL and update submodule
 * [#18246](https://github.com/apache/tvm/pull/18246) - [FFI][CMAKE] Add missing download path for libbacktrace
 * [#18234](https://github.com/apache/tvm/pull/18234) - [FFI] Misc fixup for windows
 * [#18233](https://github.com/apache/tvm/pull/18233) - [FFI] Robustify the pyproject setup
 * [#18226](https://github.com/apache/tvm/pull/18226) - [FFI][REFACTOR] Establish tvm_ffi python module
 * [#18221](https://github.com/apache/tvm/pull/18221) - [FFI] Fix JSON parser/writer for the fast-math flag
 * [#18218](https://github.com/apache/tvm/pull/18218) - [FFI][REFACTOR] Cleanup API locations
 * [#18217](https://github.com/apache/tvm/pull/18217) - [FFI] AudoDLPack compatible with torch stream context
 * [#18216](https://github.com/apache/tvm/pull/18216) - [FFI][REFACTOR] Establish Stream Context in ffi
 * [#18214](https://github.com/apache/tvm/pull/18214) - [FFI][REFACTOR] Establish ffi.Module in python
 * [#18213](https://github.com/apache/tvm/pull/18213) - [FFI] Formalize ffi.Module
 * [#18212](https://github.com/apache/tvm/pull/18212) - [FFI] Make JSON Parser/Write fastmath safe
 * [#18205](https://github.com/apache/tvm/pull/18205) - [FFI][REFATOR] Cleanup entry function to redirect
 * [#18200](https://github.com/apache/tvm/pull/18200) - [FFI][REFACTOR] Update Map ABI to enable flexible smallMap switch
 * [#18198](https://github.com/apache/tvm/pull/18198) - [FFI][REFACTOR] Move Downcast out of ffi for now
 * [#18192](https://github.com/apache/tvm/pull/18192) - [FFI] Phase out ObjectPath in favor of AccessPath
 * [#18191](https://github.com/apache/tvm/pull/18191) - [FFI][REFACTOR] Refactor AccessPath to enable full tree repr
 * [#18189](https://github.com/apache/tvm/pull/18189) - [FFI][REFACTOR] Phase out getattr based attribute handling
 * [#18188](https://github.com/apache/tvm/pull/18188) - [FFI][REFACTOR] Migrate the Save/Load JSON to the new reflection
 * [#18187](https://github.com/apache/tvm/pull/18187) - [FFI][EXTRA] Serialization To/From JSONGraph
 * [#18186](https://github.com/apache/tvm/pull/18186) - [FFI] Lightweight json parser/writer
 * [#18185](https://github.com/apache/tvm/pull/18185) - [FFI] Introduce small string/bytes
 * [#18184](https://github.com/apache/tvm/pull/18184) - [FFI][REFACTOR] Hide StringObj/BytesObj into details
 * [#18183](https://github.com/apache/tvm/pull/18183) - [FFI][REFACTOR] Cleanup to align to latest ffi
 * [#18172](https://github.com/apache/tvm/pull/18172) - [REFACTOR][FFI] Phase out SEqualReduce/SHashReduce
 * [#18172](https://github.com/apache/tvm/pull/18172) - [REFACTOR][FFI] Phase out SEqualReduce/SHashReduce
 * [#18178](https://github.com/apache/tvm/pull/18178) - [FFI] Fix SmallMapInit with duplicated keys
 * [#18177](https://github.com/apache/tvm/pull/18177) - [FFI][REFACTOR] Isolate out extra API
 * [#18176](https://github.com/apache/tvm/pull/18176) - [FFI] Improve string equal/hash handling
 * [#18166](https://github.com/apache/tvm/pull/18166) - [FFI][REFACTOR] Migrate StructuralEqual/Hash to new reflection
 * [#18165](https://github.com/apache/tvm/pull/18165) - [FFI][REFACTOR] Enable custom s_hash/equal
 * [#18160](https://github.com/apache/tvm/pull/18160) - [FFI][REFACTOR] Introduce TypeAttr in reflection
 * [#18156](https://github.com/apache/tvm/pull/18156) - [FFI] Structural equal and hash based on reflectionx
 * [#18149](https://github.com/apache/tvm/pull/18149) - [FFI] Log and throw in function dup registration
 * [#18148](https://github.com/apache/tvm/pull/18148) - [FFI][REFACTOR] Phase out TVM_FFI_REGISTER_GLOBAL in favor of GlobalDef
 * [#18147](https://github.com/apache/tvm/pull/18147) - [FFI][REFACTOR] Modularize refelection
 * [#18141](https://github.com/apache/tvm/pull/18141) - [FFI][PYTHON] Improve the traceback generation in python

### Relax
 * [#18374](https://github.com/apache/tvm/pull/18374) - [PyTorch] improve the check for no bias situation
 * [#18358](https://github.com/apache/tvm/pull/18358) - [Frontend][ONNX] Fix `FastGelu` when bias does not set
 * [#18360](https://github.com/apache/tvm/pull/18360) - [PyTorch] Support gru op for ExportedProgram importer
 * [#18359](https://github.com/apache/tvm/pull/18359) - [PyTorch] Fix the segfault in from_exported_program when model returns (Tensor, None) tuple
 * [#18321](https://github.com/apache/tvm/pull/18321) - [ONNX] Support AllClassNMS Operator for ONNX Frontend
 * [#18346](https://github.com/apache/tvm/pull/18346) - [PyTorch] Support lstm op for ExportedProgram importer
 * [#18351](https://github.com/apache/tvm/pull/18351) - [Frontend][Torch] Fix parsing error when input dimension of unbind is 1
 * [#18331](https://github.com/apache/tvm/pull/18331) - Update BasePyModule with faster DLPack converter for tensor conversion
 * [#18343](https://github.com/apache/tvm/pull/18343) - [PyTorch] Support MatrixMultiply op for ExportedProgram importer
 * [#18336](https://github.com/apache/tvm/pull/18336) - Operator and RoPE support for Llama4
 * [#18329](https://github.com/apache/tvm/pull/18329) - [Frontend][ONNX] Error converting operator Expand: TVMError: broadcast_to expects the input tensor shape is broadcastable to the target shape
 * [#18326](https://github.com/apache/tvm/pull/18326) - [Backend] Implement R.call_py_func operator for calling Python functions from compiled TVM
 * [#18313](https://github.com/apache/tvm/pull/18313) - Introduce R.call_py_func operator for calling Python functions from Relax IR
 * [#18301](https://github.com/apache/tvm/pull/18301) - Fix RelaxToPyFuncConverter compatibility and improve fallback handling
 * [#18288](https://github.com/apache/tvm/pull/18288) - Add symbolic shape support to BasePyModule for dynamic tensor operations
 * [#18269](https://github.com/apache/tvm/pull/18269) - Add Relax to Python Function Converter
 * [#18253](https://github.com/apache/tvm/pull/18253) - Building TVMScript printer for IRModules with Python functions
 * [#18229](https://github.com/apache/tvm/pull/18229) - Add Python function support and BasePyModule for PyTorch integration
 * [#18242](https://github.com/apache/tvm/pull/18242) - ONNX frontend using relax softplus operator
 * [#18180](https://github.com/apache/tvm/pull/18180) - [ONNX] Parse ONNX Upsample to Relax resize2d
 * [#18179](https://github.com/apache/tvm/pull/18179) - Support Relax Operator PReLU
 * [#18163](https://github.com/apache/tvm/pull/18163) - Fix issue in fuse concat ops by pattern
 * [#18120](https://github.com/apache/tvm/pull/18120) - [Fix]Fix potential out-of-bounds access in `TupleRewriterNode`
 * [#18061](https://github.com/apache/tvm/pull/18061) - [ONNX][Transform] Add mode choice, new mode, and warning for take()
 * [#18122](https://github.com/apache/tvm/pull/18122) - [KVCache] Fix kernel dispatch based on attention kinds

### TIR
 * [#18319](https://github.com/apache/tvm/pull/18319) - Refactor division simplification in RewriteSimplifier
 * [#18341](https://github.com/apache/tvm/pull/18341) - Support sequence comparisons in TVMScript
 * [#18323](https://github.com/apache/tvm/pull/18323) - Add support for conditional expressions in TVMScript
 * [#18199](https://github.com/apache/tvm/pull/18199) - Fix host/device function check for build
 * [#18154](https://github.com/apache/tvm/pull/18154) - Fix trivial index map [] -> [0]
 * [#18151](https://github.com/apache/tvm/pull/18151) - Decouple DeepEqual from StructuralEqual
 * [#18134](https://github.com/apache/tvm/pull/18134) - Add `T.thread_return()` for early thread exit in CUDA kernels

### TVMScript
 * [#17804](https://github.com/apache/tvm/pull/17804) - Support continue and break in tvmscript

### cuda & cutlass & tensorrt
 * [#18353](https://github.com/apache/tvm/pull/18353) - [CUDA] Update FlashInfer JIT integration
 * [#18320](https://github.com/apache/tvm/pull/18320) - [TIR][CUDA] Preserve float precision in codegen with hexfloat output
 * [#18300](https://github.com/apache/tvm/pull/18300) - [CUDA] Support NVTX in CUDA 13
 * [#18238](https://github.com/apache/tvm/pull/18238) - [CUTLASS] Fix CUTLASS kernel compilation
 * [#18144](https://github.com/apache/tvm/pull/18144) - [CodeGen][CUDA] Add sinhf CUDA Math API for CodeGen

### web
 * [#18327](https://github.com/apache/tvm/pull/18327) - [CMake]Install `web/` directory in cmake for Python package
 * [#18168](https://github.com/apache/tvm/pull/18168) - Fix incompatible part after FFI updates

### Misc
 * [#18330](https://github.com/apache/tvm/pull/18330) - [Analyzer] Enhance ConstIntBoundAnalyzer and IntervalSet with modular set analysis
 * [#18372](https://github.com/apache/tvm/pull/18372) - Upgrade to CUTLASS 4.2.1
 * [#18348](https://github.com/apache/tvm/pull/18348) - [Python] Add library lookup path for tvm installed as a pakcage
 * [#18334](https://github.com/apache/tvm/pull/18334) - Fix conflict parameter name promote_dtye in FP8ComputeLegalize
 * [#18325](https://github.com/apache/tvm/pull/18325) - [flashinfer] Support directing JIT to FlashInfer GroupedGemm kernels
 * [#18328](https://github.com/apache/tvm/pull/18328) - Fixing datatype error for gpt-2
 * [#18318](https://github.com/apache/tvm/pull/18318) - [3rdparty] Remove dlpack/libbacktrace from 3rdparty
 * [#18317](https://github.com/apache/tvm/pull/18317) - [FlashInfer] Update include path and interface
 * [#18304](https://github.com/apache/tvm/pull/18304) - Clear ext_lib_dll_names for macOS platform
 * [#18299](https://github.com/apache/tvm/pull/18299) - [Python] Fix runtime tensor import
 * [#18252](https://github.com/apache/tvm/pull/18252) - [Build] Complete TVM wheel building migration
 * [#18236](https://github.com/apache/tvm/pull/18236) - upgrade cutlass v4.2.0 supporting cuda 13
 * [#18251](https://github.com/apache/tvm/pull/18251) - [Python] Complete Python packaging with scikit-build-core
 * [#18248](https://github.com/apache/tvm/pull/18248) - [Python] Update version.py to bump pyproject.toml automatically
 * [#18291](https://github.com/apache/tvm/pull/18291) - [3rdparty] Bump cutlass_fpA_intB_gemm to fix SM90 build
 * [#18239](https://github.com/apache/tvm/pull/18239) - [Build] Migrate Python packaging to pyproject.toml with scikit-build-core
 * [#18222](https://github.com/apache/tvm/pull/18222) - [NVSHMEM] Fix compatibility with CUDA code without nvshmem use
 * [#18220](https://github.com/apache/tvm/pull/18220) - [Thrust] Fix getting CUDA stream
 * [#18211](https://github.com/apache/tvm/pull/18211) - [TARGET]add target for nvidia rtx 5060ti
 * [#18206](https://github.com/apache/tvm/pull/18206) - [CODEGEN][REFACTOR] tir.call_llvm_intrin to remove nargs
 * [#18193](https://github.com/apache/tvm/pull/18193) - Bump cutlass_fpA_intB_gemm to latest commit
 * [#18197](https://github.com/apache/tvm/pull/18197) - [REFACTOR] Update data type rewriter to enable recursive rewrite in Any
 * [#18181](https://github.com/apache/tvm/pull/18181) - [REFACTOR] Upgrade NestedMsg<T> to use new ffi::Any mechanism
 * [#18142](https://github.com/apache/tvm/pull/18142) - [REFACTOR] Migrate TVM_FFI_REGISTER_GLOBAL to new reflection style
 * [#18130](https://github.com/apache/tvm/pull/18130) - Fix compilation warnings of unnecessary `std::move()` calls
 * [#18129](https://github.com/apache/tvm/pull/18129) - Delete redundant imports
 * [#18055](https://github.com/apache/tvm/pull/18055) - [Target] Support CUDA device function calls
 * [#18127](https://github.com/apache/tvm/pull/18127) - Revert "[Refactor] Build cython with isolate environment"
 * [#18125](https://github.com/apache/tvm/pull/18125) - Phase out StackVM runtime support
 * [#18124](https://github.com/apache/tvm/pull/18124) - [Refactor] Build cython with isolate environment
 * [#18123](https://github.com/apache/tvm/pull/18123) - [Codegen] Update LLVM version requirement for `insertDeclare`
 

## v0.23.0 (2026-02-01)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax (especial PyTorch frontend), TIR etc.

Please visit the full listing of commits for a complete view: [v0.23.dev0...v0.23.0.rc0](https://github.com/apache/tvm/compare/v0.23.dev0...v0.23.0.rc0).

### Community

None.

### RFCs

None.

### Adreno
 * [#18523](https://github.com/apache/tvm/pull/18523) - [TEXTURE] Texture based lowering

### Arith
 * [#18542](https://github.com/apache/tvm/pull/18542) - Revert "Fix InternalError: Check failed: (eval_vec_) is false"
 * [#18536](https://github.com/apache/tvm/pull/18536) - Fix InternalError: Check failed: (eval_vec_) is false

### BugFix
 * [#18628](https://github.com/apache/tvm/pull/18628) - [Fix] Fix typo in file header comment
 * [#18589](https://github.com/apache/tvm/pull/18589) - [OpenCL] Guard QCOM perf hint behind USE_OPENCL_EXTN_QCOM to avoid undefined symbol on non-QCOM runtimes
 * [#18534](https://github.com/apache/tvm/pull/18534) - Prevent segfault when instantiating abstract SearchStrategy

### CI
 * [#18549](https://github.com/apache/tvm/pull/18549) - Remove hardcoded user and repo values
 * [#18484](https://github.com/apache/tvm/pull/18484) - Update file patterns for specific linting hooks
 * [#18470](https://github.com/apache/tvm/pull/18470) - Enhance python linting scripts to support revision-based checks
 * [#18498](https://github.com/apache/tvm/pull/18498) - Use glob for `conda/build-environment.yaml` in cache key
 * [#18495](https://github.com/apache/tvm/pull/18495) - Update `actions/cache` to v4 in setup action
 * [#18457](https://github.com/apache/tvm/pull/18457) - Fix crash when grep finds no matches
 * [#18448](https://github.com/apache/tvm/pull/18448) - Update pre-commit configuration
 * [#18432](https://github.com/apache/tvm/pull/18432) - Enable username checks in PR title and body
 * [#18430](https://github.com/apache/tvm/pull/18430) - [TEST][CODEGEN] Fix the test scripts tries to tell numpy a dtype name that it cannot recognise
 * [#18419](https://github.com/apache/tvm/pull/18419) - [TEST] Refactor: remove the deprecated warning message check from test cases

### Docs
 * [#18545](https://github.com/apache/tvm/pull/18545) - Improve static shape tuning parameter configuration (follow-up to commit c71aefc)
 * [#18539](https://github.com/apache/tvm/pull/18539) - Fix e2e_opt_model tutorial for GPU deployment
 * [#18451](https://github.com/apache/tvm/pull/18451) - Update the merge setting
 * [#18436](https://github.com/apache/tvm/pull/18436) - Remove prebuilt package references and disable Colab button at tutorials
 * [#18413](https://github.com/apache/tvm/pull/18413) - Update cross-compilation and RPC tutorial with modern PyTorch deployment workflow
 * [#18412](https://github.com/apache/tvm/pull/18412) - Update tutorial for exporting and loading back Relax executables
 * [#18404](https://github.com/apache/tvm/pull/18404) - Add tutorial for exporting and loading back Relax executables

### Frontend
 * [#18435](https://github.com/apache/tvm/pull/18435) - [ONNX] Fix operator Transpose: TVMError: PermuteDims expects the number of input axes to equal the ndim of the input tensor

### LLVM
 * [#18586](https://github.com/apache/tvm/pull/18586) - [Codegen] Avoid segfault when `arith::GetVScaleValues` returns empty vector

### MetaSchedule
 * [#18547](https://github.com/apache/tvm/pull/18547) - Fix tune_tir crash with ScheduleError in RewriteParallelVectorizeUnroll

### Relax
 * [#18676](https://github.com/apache/tvm/pull/18676) - Implement dynamic output trimming for NMS
 * [#18664](https://github.com/apache/tvm/pull/18664) - Add FDataDependent operator attribute for LegalizeOps
 * [#18668](https://github.com/apache/tvm/pull/18668) - [Onnx] Support Local Response Normalization (LRN)
 * [#18667](https://github.com/apache/tvm/pull/18667) - Add native size operator
 * [#18675](https://github.com/apache/tvm/pull/18675) - [LAYOUT] Support for dynamic layout specification
 * [#18652](https://github.com/apache/tvm/pull/18652) - [ONNX] add support for unique optional outputs
 * [#18665](https://github.com/apache/tvm/pull/18665) - Replace topi.take with relax.op.take
 * [#18663](https://github.com/apache/tvm/pull/18663) - Fix wrong memory planning when only lower bound was provided
 * [#18666](https://github.com/apache/tvm/pull/18666) - [Onnx][Resize] Handle non-4D input tensors
 * [#18658](https://github.com/apache/tvm/pull/18658) - [Onnx][PReLU] Handle slope and axis argument with different slope shapes
 * [#18649](https://github.com/apache/tvm/pull/18649) - Remove obsolete TODO comments
 * [#18642](https://github.com/apache/tvm/pull/18642) - Add FRelaxInferLayout for gather_elements operator
 * [#18643](https://github.com/apache/tvm/pull/18643) - Add FRelaxInferLayout for scatter_nd operator
 * [#18641](https://github.com/apache/tvm/pull/18641) - [Op] Fixed incorrect output shape of Pool op when ceil_mode = true
 * [#18638](https://github.com/apache/tvm/pull/18638) - Add FRelaxInferLayout for scatter_elements operator
 * [#18637](https://github.com/apache/tvm/pull/18637) - Add FRelaxInferLayout for flip operator
 * [#18633](https://github.com/apache/tvm/pull/18633) - Add FRelaxInferLayout and TMixedPrecisionPolicy for dynamic_strided_slice
 * [#18635](https://github.com/apache/tvm/pull/18635) - [Onnx] Pass output_padding param in ConvTranspose
 * [#18632](https://github.com/apache/tvm/pull/18632) - Move GetUsedVars to analysis module
 * [#18629](https://github.com/apache/tvm/pull/18629) - Add FInferMixedPrecision and FRelaxInferLayout for conv transpose ops
 * [#18626](https://github.com/apache/tvm/pull/18626) - [Op][PyTorch] Supported Median operator
 * [#18576](https://github.com/apache/tvm/pull/18576) - Correct YaRN RoPE frequency scaling formula to align with the original paper
 * [#18615](https://github.com/apache/tvm/pull/18615) - Add gpu-generic fallback for unrecognized GPU targets
 * [#18621](https://github.com/apache/tvm/pull/18621) - Use weight shape instead of dim in Embedding.forward
 * [#18613](https://github.com/apache/tvm/pull/18613) - Remove duplicated test case: test_if_branch_var_scope
 * [#18616](https://github.com/apache/tvm/pull/18616) - Replaced call_pure_packed with tensor_to_shape operator
 * [#18593](https://github.com/apache/tvm/pull/18593) - feat: Implement FRelaxInferLayout for tile operator
 * [#18618](https://github.com/apache/tvm/pull/18618) - Add test case for op attributes in AST printer
 * [#18619](https://github.com/apache/tvm/pull/18619) - [PyTorch] Fix PyTorch Dynamo frontend for Darwin compatibility
 * [#18575](https://github.com/apache/tvm/pull/18575) - [ONNX] Add edge padding mode
 * [#18620](https://github.com/apache/tvm/pull/18620) - Fix flaky test_conv2d gradient numeric test
 * [#18609](https://github.com/apache/tvm/pull/18609) - Fix batch normalization computation logic
 * [#18574](https://github.com/apache/tvm/pull/18574) - [Torch] AssertionError: Unsupported function types ['mean.default']
 * [#18591](https://github.com/apache/tvm/pull/18591) - Chore: Fix the DeprecationWarning: invalid escape sequence \
 * [#18577](https://github.com/apache/tvm/pull/18577) - Clean up scatter_elements unknown dtype handling
 * [#18579](https://github.com/apache/tvm/pull/18579) - Add layout inference support for repeat operator
 * [#18583](https://github.com/apache/tvm/pull/18583) - [Torch] Fixed issues related to sum op when without dim and keep dim
 * [#18554](https://github.com/apache/tvm/pull/18554) - Enhance unique block name generation with numeric suffixes
 * [#18558](https://github.com/apache/tvm/pull/18558) - Add edge padding mode
 * [#18559](https://github.com/apache/tvm/pull/18559) - Add mod operator support
 * [#18544](https://github.com/apache/tvm/pull/18544) - [PyTorch] Add support for Custom Ops for ExportedProgram frontend
 * [#18535](https://github.com/apache/tvm/pull/18535) - [PyTorch] Add support for masked_select
 * [#18551](https://github.com/apache/tvm/pull/18551) - [Frontend] Introduce ModuleDict
 * [#18550](https://github.com/apache/tvm/pull/18550) - [PyTorch] Enhance scale_factor handling in interpolation
 * [#18553](https://github.com/apache/tvm/pull/18553) - [PyTorch] Unify dtype used in conv2d tests
 * [#18548](https://github.com/apache/tvm/pull/18548) - [PyTroch] Add NHWC layout support
 * [#18533](https://github.com/apache/tvm/pull/18533) - [PyTorch] Fix index_put with broadcast indices
 * [#18521](https://github.com/apache/tvm/pull/18521) - [PyTorch] Handle unknown output shapes for _sym_size_int
 * [#18532](https://github.com/apache/tvm/pull/18532) - [PyTorch] Add support for bidirectional GRU
 * [#18530](https://github.com/apache/tvm/pull/18530) - [PyTorch] Add boolean tensor support for max operation and corresponding test case
 * [#18524](https://github.com/apache/tvm/pull/18524) - [PyTorch] Fix InternalError when converting scaled_dot_product_attention with 2D inputs
 * [#18527](https://github.com/apache/tvm/pull/18527) - [PyTorch] Add support for non-persistent buffers in ExportedProgram frontend
 * [#18529](https://github.com/apache/tvm/pull/18529) - [PyTorch] Add support for binary scalar operations in ExportedProgram frontend and corresponding tests
 * [#18522](https://github.com/apache/tvm/pull/18522) - [PyTorch] Unify tests using shared tvm.testing.assert_allclose
 * [#18516](https://github.com/apache/tvm/pull/18516) - [PyTorch] Add support for bidirectional LSTM
 * [#18499](https://github.com/apache/tvm/pull/18499) - [PyTorch] Add support for sparse matrix multiplication
 * [#18518](https://github.com/apache/tvm/pull/18518) - [PyTorch] Fix batch normalization training mode correctness
 * [#18517](https://github.com/apache/tvm/pull/18517) - [PyTorch] Unify tests using shared verify_model
 * [#18506](https://github.com/apache/tvm/pull/18506) - [PyTorch] Enhance data type handling in FX graph translator
 * [#18507](https://github.com/apache/tvm/pull/18507) - [PyTorch] Support specifying decimals for _round
 * [#18500](https://github.com/apache/tvm/pull/18500) - [PyTorch] Add support for antialiased bilinear upsampling
 * [#18489](https://github.com/apache/tvm/pull/18489) - [PyTorch] Enhance handling of unbounded upper bound constraints
 * [#17599](https://github.com/apache/tvm/pull/17599) - [PASS] Annotate Custom Scope layout pass for Adreno GPU
 * [#18497](https://github.com/apache/tvm/pull/18497) - [PyTorch] Add binary operation dtype promotion following PyTorch rules in ExportedProgram frontend
 * [#18478](https://github.com/apache/tvm/pull/18478) - Fix the squeeze operator to behave consistently with torch
 * [#18496](https://github.com/apache/tvm/pull/18496) - [PyTorch] Add `mul` operator in ExportedProgram frontend
 * [#18494](https://github.com/apache/tvm/pull/18494) - [PyTorch] Add negative slicing support in `slice_scatter` operation
 * [#18493](https://github.com/apache/tvm/pull/18493) - [PyTorch] Add broadcast support for `copy` operation
 * [#18490](https://github.com/apache/tvm/pull/18490) - [PyTorch] Add `as_strided` operator in ExportedProgram frontend
 * [#18487](https://github.com/apache/tvm/pull/18487) - [PyTorch] Add `count_include_pad` support to `avg_pool2d` in PyTorch frontend
 * [#18488](https://github.com/apache/tvm/pull/18488) - [PyTorch] Enhance index_put support for multi-dimensional indices
 * [#18486](https://github.com/apache/tvm/pull/18486) - [PyTorch] Fix `batch_norm.default` args handling in ExportedProgram frontend
 * [#18483](https://github.com/apache/tvm/pull/18483) - [PyTorch] Add support for grid_sample operator
 * [#18482](https://github.com/apache/tvm/pull/18482) - [PyTorch] Add support for gumbel_softmax
 * [#18485](https://github.com/apache/tvm/pull/18485) - [PyTorch] Add dynamic shape support to `torch.ops.aten.sym_size.int` in ExportedProgram frontend
 * [#18473](https://github.com/apache/tvm/pull/18473) - [PyTorch] Add support for `torch.ops.aten.sym_size.int` in ExportedProgram frontend
 * [#18471](https://github.com/apache/tvm/pull/18471) - [PyTorch] Enable run_ep_decomposition by default
 * [#18462](https://github.com/apache/tvm/pull/18462) - [PyTorch] Add decomposed operator support for interpolate
 * [#18455](https://github.com/apache/tvm/pull/18455) - Fix flaky test_conv2d_offload by increasing float32 tolerance
 * [#18463](https://github.com/apache/tvm/pull/18463) - [PyTorch] Support advanced range constraints (multiplication)
 * [#18464](https://github.com/apache/tvm/pull/18464) - [PyTorch] Enable decomposition in all tests
 * [#18461](https://github.com/apache/tvm/pull/18461) - [PyTorch] Fix KeyError: dtype when converting PyTorch model with gradient checkpointing using torch.export
 * [#18452](https://github.com/apache/tvm/pull/18452) - [PyTorch] Support advanced range constraints (addition)
 * [#18454](https://github.com/apache/tvm/pull/18454) - [PyTorch]: Fix the sqrt operation requires float dtype but receives int64 in attention scaling
 * [#18459](https://github.com/apache/tvm/pull/18459) - [PyTorch] Fix MultiheadAttention complie
 * [#18460](https://github.com/apache/tvm/pull/18460) - [PyTorch] Add decomposed operator support for normalization
 * [#18458](https://github.com/apache/tvm/pull/18458) - [PyTorch] Add decomposed operator support for Binary
 * [#18449](https://github.com/apache/tvm/pull/18449) - [PyTorch] Add decomposed operator support for Pad
 * [#18447](https://github.com/apache/tvm/pull/18447) - [PyTorch] Add lower bound support for range constraints
 * [#18446](https://github.com/apache/tvm/pull/18446) - [PyTorch] Add decomposed operator support for MaxPool
 * [#18437](https://github.com/apache/tvm/pull/18437) - [PyTorch] Add decomposed operator support for AdaptiveAvgPool
 * [#18433](https://github.com/apache/tvm/pull/18433) - [PyTorch] Add decomposed operator support for Conv
 * [#18429](https://github.com/apache/tvm/pull/18429) - [PyTorch] Support basic range constraints
 * [#18428](https://github.com/apache/tvm/pull/18428) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(8)
 * [#18427](https://github.com/apache/tvm/pull/18427) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(7)
 * [#18420](https://github.com/apache/tvm/pull/18420) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(6)
 * [#18417](https://github.com/apache/tvm/pull/18417) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(5)
 * [#18416](https://github.com/apache/tvm/pull/18416) - [ONNX] Fix bug: Unsupported numpy or ml_dtypes dtype('O') when importing ONNX model using Relax frontend
 * [#18414](https://github.com/apache/tvm/pull/18414) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(4)
 * [#18410](https://github.com/apache/tvm/pull/18410) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(3)
 * [#18403](https://github.com/apache/tvm/pull/18403) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(2)
 * [#18402](https://github.com/apache/tvm/pull/18402) - [PyTorch] Add support for decomposed operators and fix IR of ops tests(1)
 * [#18401](https://github.com/apache/tvm/pull/18401) - [PyTorch] Enable decomposition for unary ops and refactor tests
 * [#18400](https://github.com/apache/tvm/pull/18400) - [PyTorch] Add support for decomposed operators in extended unary ops tests
 * [#18399](https://github.com/apache/tvm/pull/18399) - [PyTorch] Add run_ep_decomposition flag to control PyTorch decomposition

### Runtime
 * [#18546](https://github.com/apache/tvm/pull/18546) - [MatchShape] Type error: Cannot convert from type ' DLTensor* ' to ' ffi.Shape '

### TIR
 * [#18639](https://github.com/apache/tvm/pull/18639) - [Schedule] Fix type checker to support subscripted generics in Python 3.14+
 * [#18515](https://github.com/apache/tvm/pull/18515) - [Schedule] FuseReductionEpilogue: Add Clipping pattern support
 * [#18556](https://github.com/apache/tvm/pull/18556) - [Schedule] Fix bug on bfloat16 conversion
 * [#18528](https://github.com/apache/tvm/pull/18528) - [Schedule] Fix mma tensorize error
 * [#18514](https://github.com/apache/tvm/pull/18514) - Fix tir.LowerIntrin check failed additional_info.size() == new_size
 * [#18505](https://github.com/apache/tvm/pull/18505) - Update function signatures for decompose_reduction
 * [#18479](https://github.com/apache/tvm/pull/18479) - : Fix VerifyStream::Verify causes dereferencing an invalid pointer
 * [#18421](https://github.com/apache/tvm/pull/18421) - Add step attribute to ForNode (Initial codes)
 * [#18418](https://github.com/apache/tvm/pull/18418) - [Schedule] Add FuseReductionEpilogue primitive to fuse epilogue …
 * [#18466](https://github.com/apache/tvm/pull/18466) - Fix Data Type Mismatch (int64 vs int32) in T.match_buffer when Working with Scalar Buffers in TIR

### TVMScript
 * [#18504](https://github.com/apache/tvm/pull/18504) - Add test for TIR macro block name suffix handling
 * [#18465](https://github.com/apache/tvm/pull/18465) - Add block name suffix management for TIR macros

### cuda & cutlass & tensorrt
 * [#18624](https://github.com/apache/tvm/pull/18624) - [CUDA] Fix cuModuleUnload crash during interpreter shutdown
 * [#18604](https://github.com/apache/tvm/pull/18604) - [CUDA][FFI] Extend kernel launch config to support Programmatic Dependent Launch and cuLaunchCooperativeKernel

### web
 * [#18683](https://github.com/apache/tvm/pull/18683) - Fix RPC argument parsing for new FFI string/bytes types
 * [#18686](https://github.com/apache/tvm/pull/18686) - Fix incorrect FFI export name in runtime.ts
 * [#18480](https://github.com/apache/tvm/pull/18480) - Bump web runtime version 0.23.0-dev1
 * [#18467](https://github.com/apache/tvm/pull/18467) - Replace string with TVMFFIByteArray* to avoid memory issues
 * [#18450](https://github.com/apache/tvm/pull/18450) - Fix progress reporting when loading from cache
 * [#18415](https://github.com/apache/tvm/pull/18415) - Fix arrayDecodeStorage scope issue for q0f32 models
 * [#18385](https://github.com/apache/tvm/pull/18385) - Upgrade web runtime to new FFI

### Misc
 * [#18681](https://github.com/apache/tvm/pull/18681) - [NVRTC] Add NVSHMEM support to NVRTC compilation path
 * [#18674](https://github.com/apache/tvm/pull/18674) - fix: MSVC pragma
 * [#18654](https://github.com/apache/tvm/pull/18654) - [FFI] bump to latest version
 * [#18656](https://github.com/apache/tvm/pull/18656) - Put options before objects when compiling
 * [#18519](https://github.com/apache/tvm/pull/18519) - [Compile] accelerate compilation speed using NVRTC
 * [#18582](https://github.com/apache/tvm/pull/18582) - Fix ACOS precision issue for boundary values (x=±1.0)
 * [#18557](https://github.com/apache/tvm/pull/18557) - [Attn] Fix calling FlashInfer attention plan function
 * [#18555](https://github.com/apache/tvm/pull/18555) - Fix duplicate `PresburgerSetNode` registration when `USE_MLIR=ON` and MLIR >= 15.0
 * [#18525](https://github.com/apache/tvm/pull/18525) - [Schedule] Fix LocalBuilder Check failed: (index_map_func.has_value()) is false
 * [#18511](https://github.com/apache/tvm/pull/18511) - [Pass] Add DumpIR pass instrument to save IR snapshots
 * [#18512](https://github.com/apache/tvm/pull/18512) - Remove unused TVMC configs
 * [#18509](https://github.com/apache/tvm/pull/18509) - Fix compilation warnings
 * [#18492](https://github.com/apache/tvm/pull/18492) - Fix BufferError when converting PyTorch models with sparse tensors
 * [#18469](https://github.com/apache/tvm/pull/18469) - [Contrib] Update RandomFill to use StreamSync for CUDA synchronization
 * [#18453](https://github.com/apache/tvm/pull/18453) - [DataType] Update to use explicit Bool Type Aligning with DLPack
 * [#18422](https://github.com/apache/tvm/pull/18422) - Adjusted Longrope embedding function to match Huggingface Implementation
 * [#18426](https://github.com/apache/tvm/pull/18426) - Support integer type input for log and log2
 * [#18411](https://github.com/apache/tvm/pull/18411) - [FFI] Bump tvm-ffi to latest
 * [#18409](https://github.com/apache/tvm/pull/18409) - Fixing database bug
 * [#18390](https://github.com/apache/tvm/pull/18390) - Support integer types in TIR expression operators
 * [#18398](https://github.com/apache/tvm/pull/18398) - fix the  8-bit vector loads/stores problem, which will solve the problem raised in the codegen test for cuda
 * [#18389](https://github.com/apache/tvm/pull/18389) - Add VisitStmt_ method for AssertStmtNode and StringImmNode
 * [#18361](https://github.com/apache/tvm/pull/18361) - [WebLLM] Replace int64s with int32s in WebGPU kernels
 * [#18384](https://github.com/apache/tvm/pull/18384) - Fix crash when multiple PrimFunc objects are present in IRModule
 * [#18378](https://github.com/apache/tvm/pull/18378) - [release][Dont Squash] Update version to 0.22.0 and 0.23.0.dev on main branch

## v0.24.0 (2026-05-09)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax etc.

Please visit the full listing of commits for a complete view: [v0.24.dev0...v0.24.0.rc0](https://github.com/apache/tvm/compare/v0.24.dev0...v0.24.0.rc0).

### Community

None.

### RFCs

None.

### Adreno
 * [#18867](https://github.com/apache/tvm/pull/18867) - Revive and consolicate Adreno features

### Arith
 * [#19417](https://github.com/apache/tvm/pull/19417) - Expose allow_override parameter in Python Analyzer.bind()

### BugFix
 * [#19432](https://github.com/apache/tvm/pull/19432) - [Fix][CUDA] Version compatibility of CUDA symbols
 * [#19427](https://github.com/apache/tvm/pull/19427) - [FIX] Skip metal target tag registration for unsupported LLVM CPUs
 * [#19390](https://github.com/apache/tvm/pull/19390) - [LLVM] Fix `insertDeclare` API mismatch for ROCm-bundled LLVM 20
 * [#19410](https://github.com/apache/tvm/pull/19410) - [Fix][Runtime][RPC] Fix remote tensor handle cleanup for RPC return values
 * [#19385](https://github.com/apache/tvm/pull/19385) - [MetaSchedule] Fix `compile_relax` to apply `MetaScheduleApplyDatabase` after `FuseOps`
 * [#19383](https://github.com/apache/tvm/pull/19383) - [TIRx] Fix bad-optional-access in BF16/FP8 legalize passes for target-less PrimFuncs
 * [#19382](https://github.com/apache/tvm/pull/19382) - [TIRx] Fix VerifyMemory crash for PrimFuncs without target attribute
 * [#19380](https://github.com/apache/tvm/pull/19380) - [TOPI] Fix get_const_tuple hanging indefinitely when passed a te.Tensor
 * [#19368](https://github.com/apache/tvm/pull/19368) - Align `tir.round` to ties-to-even across all backends
 * [#19367](https://github.com/apache/tvm/pull/19367) - [ONNX] Fix Round op to use ties-to-even
 * [#19362](https://github.com/apache/tvm/pull/19362) - [TVMScript] Fix invalid f-string format spec causing TypeError on Python 3.14
 * [#19352](https://github.com/apache/tvm/pull/19352) - [TVMScript] Add `doc.keyword` handling for `ExprEvaluator._visit`
 * [#18957](https://github.com/apache/tvm/pull/18957) - [FIX] Inline ceil_log2 in gpu_2d_continuous_cumsum to fix MakePackedAPI error
 * [#18940](https://github.com/apache/tvm/pull/18940) - [Fix] Fix tvm.tir references in Tflite frontend
 * [#18887](https://github.com/apache/tvm/pull/18887) - [FIX] Fix cumsum kernel sblock_alloc_buffer for non-sblock buffer
 * [#18881](https://github.com/apache/tvm/pull/18881) - [FIX][Adreno] Replace AllocBuffer with Bind in texture alloc injection
 * [#18838](https://github.com/apache/tvm/pull/18838) - [TOPI] Fix resize accuracy issue with non-floor rounding
 * [#18782](https://github.com/apache/tvm/pull/18782) - [S-TIR][FIX] Remove redundant std::move() to itself
 * [#18742](https://github.com/apache/tvm/pull/18742) - [Fix] Handle empty variable name in NameSupply::FreshName
 * [#18694](https://github.com/apache/tvm/pull/18694) - [TIR] Fix incorrect optimization when lowering floordiv and f…
 * [#18695](https://github.com/apache/tvm/pull/18695) - [FIX] Fix T.sblock due to concurrent merge

### CI
 * [#19445](https://github.com/apache/tvm/pull/19445) - [REFACTOR] Decouple data.py from Jenkins script and docker images
 * [#18827](https://github.com/apache/tvm/pull/18827) - Update images to `20260301-134651-63f099ad`
 * [#18863](https://github.com/apache/tvm/pull/18863) - [S-TIR][Test] Mark meta_schedule tuning tests as skip
 * [#18851](https://github.com/apache/tvm/pull/18851) - Remove stale test scripts (i386, hexagon, mypy)
 * [#18850](https://github.com/apache/tvm/pull/18850) - [TEST] Remove stale URL mappings from request_hook
 * [#18848](https://github.com/apache/tvm/pull/18848) - Remove legacy lint scripts and Apache RAT
 * [#18817](https://github.com/apache/tvm/pull/18817) - [REFACTOR]Further cleanup docker images
 * [#18812](https://github.com/apache/tvm/pull/18812) - [REFACTOR]Modernize Python dependency management with uv
 * [#18809](https://github.com/apache/tvm/pull/18809) - Add GitHub Actions lint workflow
 * [#18805](https://github.com/apache/tvm/pull/18805) - [REFACTOR][TEST] Migrate tir-transform tests from TE to TVMScript
 * [#18804](https://github.com/apache/tvm/pull/18804) - [REFACTOR][TEST] Remove unused te imports from test files
 * [#18800](https://github.com/apache/tvm/pull/18800) - Update images to `20260219-160550-72f51851`
 * [#18796](https://github.com/apache/tvm/pull/18796) - Refactor Dockerfiles and installation scripts
 * [#18775](https://github.com/apache/tvm/pull/18775) - Update images to `20260214-152058-2a448ce4`
 * [#18783](https://github.com/apache/tvm/pull/18783) - Update system cuda version 12.4->12.8
 * [#18780](https://github.com/apache/tvm/pull/18780) - Remove unity from tvm-bot
 * [#18777](https://github.com/apache/tvm/pull/18777) - Update Pillow, pytest-rerunfailures, junitparser, xgboost, onnx and pytorch
 * [#18647](https://github.com/apache/tvm/pull/18647) - Upgrade Python to 3.10 in CI
 * [#18749](https://github.com/apache/tvm/pull/18749) - Remove i386 and Hexagon from CI pipeline (2)
 * [#18757](https://github.com/apache/tvm/pull/18757) - Further cleanup CI after merging unity to main test
 * [#18456](https://github.com/apache/tvm/pull/18456) - Move conda config files to tests/conda and remove unused conda build infrastructure
 * [#18755](https://github.com/apache/tvm/pull/18755) - [TEST] Cleanup legacy tests and migrate unity tests to main one
 * [#18737](https://github.com/apache/tvm/pull/18737) - Remove i386 and Hexagon from CI pipeline (1)
 * [#18748](https://github.com/apache/tvm/pull/18748) - Remove i386 and hexagon from `.asf.yaml`
 * [#18719](https://github.com/apache/tvm/pull/18719) - [REFACTOR][TEST] Migrate all codegen test to tvmscript
 * [#18717](https://github.com/apache/tvm/pull/18717) - Fix double newlines in nightly docker update
 * [#18711](https://github.com/apache/tvm/pull/18711) - [REFACTOR][TEST] Replace CompareBeforeAfter for pytest compact
 * [#18692](https://github.com/apache/tvm/pull/18692) - Fix NameError in nightly docker update workflow

### Docker
 * [#18854](https://github.com/apache/tvm/pull/18854) - Refactor bash.sh: auto-detect rootless, add --shell, TVM_DEV_MOUNTS
 * [#18710](https://github.com/apache/tvm/pull/18710) - [ci]Nightly Docker image update

### Docs
 * [#19439](https://github.com/apache/tvm/pull/19439) - Refactor BYOC example NPU tutorial
 * [#19414](https://github.com/apache/tvm/pull/19414) - Fix stale tvm.tirx exclude list and add missing legalize_ops.unary entry
 * [#19409](https://github.com/apache/tvm/pull/19409) - Fix outdated source install and API reference docs
 * [#19407](https://github.com/apache/tvm/pull/19407) - Fix #18714: python -c "import tvm; print(tvm.file)" fail
 * [#19396](https://github.com/apache/tvm/pull/19396) - Add code generation architecture documentation
 * [#19398](https://github.com/apache/tvm/pull/19398) - Add TVMScript architecture documentation
 * [#19397](https://github.com/apache/tvm/pull/19397) - Add PyModule tutorial to How-To toctree
 * [#19399](https://github.com/apache/tvm/pull/19399) - Clean up architecture docs: remove duplicates, fix stale content
 * [#19389](https://github.com/apache/tvm/pull/19389) - Add Relax VM architecture documentation
 * [#19394](https://github.com/apache/tvm/pull/19394) - Add operator fusion architecture documentation
 * [#19395](https://github.com/apache/tvm/pull/19395) - Add BYOC external library dispatch architecture documentation
 * [#19387](https://github.com/apache/tvm/pull/19387) - Add docstrings for nn.Module classes and core APIs in relax.frontend.nn
 * [#19386](https://github.com/apache/tvm/pull/19386) - Add tvm.s_tir.tensor_intrin API reference and remove empty legacy tvm/tir directory
 * [#19379](https://github.com/apache/tvm/pull/19379) - Add API reference for tvm.arith, tvm.testing, tvm.exec, tvm.tirx.backend and extend topi/contrib/ir/target docs
 * [#19369](https://github.com/apache/tvm/pull/19369) - Add API reference for tvm.s_tir submodules: dlight, meta_schedule, backend
 * [#19366](https://github.com/apache/tvm/pull/19366) - Add API reference documentation for tvm.script module
 * [#19356](https://github.com/apache/tvm/pull/19356) - Add DLight and MetaSchedule deep-dive instructions
 * [#19364](https://github.com/apache/tvm/pull/19364) - TFLite tests requiring Python 3.10 and specific package versions to avoid core dumps
 * [#19354](https://github.com/apache/tvm/pull/19354) - Add tutorial for importing models from PyTorch, ONNX, and TFLite
 * [#19358](https://github.com/apache/tvm/pull/19358) - Add Dataflow Pattern Language (DPL) documentation for Relax
 * [#19357](https://github.com/apache/tvm/pull/19357) - Add Disco distributed runtime architecture overview
 * [#19351](https://github.com/apache/tvm/pull/19351) - Fix outdated paths, links, and add missing API references across documentation(3)
 * [#19353](https://github.com/apache/tvm/pull/19353) - Add tvm.s_tir.analysis API reference page
 * [#19350](https://github.com/apache/tvm/pull/19350) - Add Relax VM architecture overview in documentation
 * [#19344](https://github.com/apache/tvm/pull/19344) - Fix outdated code examples, typos, and missing API reference in documentation(2)
 * [#18965](https://github.com/apache/tvm/pull/18965) - Fix outdated code examples, types, and missing references across documentation
 * [#18966](https://github.com/apache/tvm/pull/18966) - [DOC] Fix various issues
 * [#18953](https://github.com/apache/tvm/pull/18953) - Align documentation with tirx/s_tir namespace split
 * [#18947](https://github.com/apache/tvm/pull/18947) - Add tutorial for mixing Python/PyTorch with TVM using BasePyModule
 * [#18939](https://github.com/apache/tvm/pull/18939) - [DOC] Fix inconsistent code comments
 * [#18941](https://github.com/apache/tvm/pull/18941) - Fix duplicate license headers and incorrect module paths after tirx rename
 * [#18908](https://github.com/apache/tvm/pull/18908) - Clean up stale references from recent refactors
 * [#18906](https://github.com/apache/tvm/pull/18906) - Update outdated references from recent refactors
 * [#18860](https://github.com/apache/tvm/pull/18860) - [CI]Update Sphinx dependencies
 * [#18855](https://github.com/apache/tvm/pull/18855) - Fix RPC tutorial to use set_input + invoke_stateful API
 * [#18808](https://github.com/apache/tvm/pull/18808) - [DOC] Update installation docs with missing dependencies (#18194)
 * [#18799](https://github.com/apache/tvm/pull/18799) - [DOC] Fix docstring, unify CMake, nvidia-docker deprecation
 * [#18797](https://github.com/apache/tvm/pull/18797) - [DOC] Unify CUDA naming
 * [#18794](https://github.com/apache/tvm/pull/18794) - [DOC] Unify GitHub naming
 * [#18770](https://github.com/apache/tvm/pull/18770) - [DOC] Fix PYTHONPATH in "Install from Source"
 * [#18732](https://github.com/apache/tvm/pull/18732) - [DOC] Fix RST syntax
 * [#18753](https://github.com/apache/tvm/pull/18753) - [DOC] Fix the loop length in a loop tiling example
 * [#18731](https://github.com/apache/tvm/pull/18731) - [DOC] Fix grammar
 * [#18718](https://github.com/apache/tvm/pull/18718) - Clarify trusted usage

### Frontend
 * [#19401](https://github.com/apache/tvm/pull/19401) - [TFLite] Add test coverage for SHAPE and RANGE operators
 * [#19402](https://github.com/apache/tvm/pull/19402) - [Test][TFLite] Add unit tests for `PRELU`
 * [#19400](https://github.com/apache/tvm/pull/19400) - [TFLite] Add TILE operator tests and edge cases
 * [#19388](https://github.com/apache/tvm/pull/19388) - [Test][TFLite] Add unit tests for `LEAKY_RELU`, `HARD_SWISH` `ReLU_N1_to_1` and `LOG_SOFTMAX`
 * [#19365](https://github.com/apache/tvm/pull/19365) - [Test][TFLite] Add unit tests for RESIZE_BILINEAR and RESIZE_NEAREST_NEIGHBOR ops
 * [#18970](https://github.com/apache/tvm/pull/18970) - [TFLite]Add expected IRModule checks for conv2d, pool2d, and batch_matmul tests
 * [#19341](https://github.com/apache/tvm/pull/19341) - [ONNX] Fix SplitToSequence keepdims=0 and uneven last chunk
 * [#18969](https://github.com/apache/tvm/pull/18969) - [ONNX] Support select_last_index for ArgMax and ArgMin
 * [#18951](https://github.com/apache/tvm/pull/18951) - [ONNX] Add MatMulInteger support to Relax ONNX frontend
 * [#18946](https://github.com/apache/tvm/pull/18946) - [ONNX] Add If operator support to Relax ONNX frontend
 * [#18929](https://github.com/apache/tvm/pull/18929) - [TFLite] Fix undefined symbols and Relay API remnants in TFLite frontend
 * [#18773](https://github.com/apache/tvm/pull/18773) - [ONNX] Handle Gelu approximate attribute from Opset 20

### LLVM
 * [#18909](https://github.com/apache/tvm/pull/18909) - [Target]Fix -mcpu validation compatibility across LLVM versions
 * [#18853](https://github.com/apache/tvm/pull/18853) - Bump minimum LLVM version to 15
 * [#18818](https://github.com/apache/tvm/pull/18818) - Fix build failures when building with llvm>=22
 * [#18772](https://github.com/apache/tvm/pull/18772) - [Codegen] Cast NaN to bool gives true
 * [#18706](https://github.com/apache/tvm/pull/18706) - Fix insertDbgValueIntrinsic for Metal backend

### MetaSchedule
 * [#19438](https://github.com/apache/tvm/pull/19438) - [S-TIR]Make evolutionary search resilient to trace replay failures

### Metal
 * [#19493](https://github.com/apache/tvm/pull/19493) - Include logging headers for metal
 * [#18877](https://github.com/apache/tvm/pull/18877) - Batched command dispatch and staging buffer pool
 * [#18819](https://github.com/apache/tvm/pull/18819) - [REFACTOR]Update CHECK_LE to TVM_FFI_ICHECK_LE in Metal runtime
 * [#18811](https://github.com/apache/tvm/pull/18811) - [Refactor]Update ICHECK to TVM_FFI_ICHECK in Metal runtime

### ROCm
 * [#15518](https://github.com/apache/tvm/pull/15518) - Fix some ROCm codegen bugs

### Relax
 * [#19492](https://github.com/apache/tvm/pull/19492) - [BugFix]Add legalize for isnan, isinf, isfinite
 * [#19489](https://github.com/apache/tvm/pull/19489) - [Frontend][TFLite] Add BROADCAST_TO, EMBEDDING_LOOKUP, and SELECT_V2
 * [#19490](https://github.com/apache/tvm/pull/19490) - [Frontend][TFLite] Add SCATTER_ND operator for Relax TFLite
 * [#19467](https://github.com/apache/tvm/pull/19467) - [ONNX] Fix CumSum axis handling: support runtime axis tensor, error on multi-element axis
 * [#19473](https://github.com/apache/tvm/pull/19473) - [Frontend][TFLite] Add `RANDOM_UNIFORM`, `RANDOM_STANDARD_NORMAL`, and `MULTINOMIAL`
 * [#19487](https://github.com/apache/tvm/pull/19487) - [Frontend][TFLite] Add BROADCAST_ARGS operator mapping
 * [#19481](https://github.com/apache/tvm/pull/19481) - [Frontend][TFLite] Add DILATE operator mapping
 * [#19485](https://github.com/apache/tvm/pull/19485) - [Frontend][TFLite] Add ATAN2 op and TFLite mapping
 * [#19480](https://github.com/apache/tvm/pull/19480) - [BugFix][ONNX] Fix ConstantOfShape converter when value attr is absent
 * [#19468](https://github.com/apache/tvm/pull/19468) - [Frontend][TFLite] Fix `STRIDED_SLICE` negative stride and add `STRIDED_SLICE/SPLIT_V` tests
 * [#19421](https://github.com/apache/tvm/pull/19421) - [Frontend][TFLite] Add DENSIFY operator test and fix prefetched handling
 * [#19464](https://github.com/apache/tvm/pull/19464) - [Frontend][TFLite] Add NON_MAX_SUPPRESSION_V4 converter
 * [#19466](https://github.com/apache/tvm/pull/19466) - [Frontend][TFLite] Add BITCAST operator mapping
 * [#19433](https://github.com/apache/tvm/pull/19433) - [Frontend][TFLite] Fix dynamic FILL/SPLIT_V partial implementations
 * [#19426](https://github.com/apache/tvm/pull/19426) - [Frontend][TFLite] Add soft-NMS support for TFLite NON_MAX_SUPPRESSION_V5
 * [#19450](https://github.com/apache/tvm/pull/19450) - [BugFix][ONNX] Honor auto_pad in ConvTranspose converter
 * [#19431](https://github.com/apache/tvm/pull/19431) - [Frontend][KVCache] Extend masked sequence prefill to causal left-padding
 * [#19434](https://github.com/apache/tvm/pull/19434) - [Frontend][TFLite] Add CUMSUM operator mapping
 * [#19430](https://github.com/apache/tvm/pull/19430) - [NN] Use int64 for RoPE apply flag
 * [#19428](https://github.com/apache/tvm/pull/19428) - [FRONTEND][ONNX] Support Softmax, LogSoftmax and Hardmax when opset version ≤12
 * [#19425](https://github.com/apache/tvm/pull/19425) - [Backend]Add NPU BYOC backend example
 * [#19424](https://github.com/apache/tvm/pull/19424) - Fix deprecation warning
 * [#19416](https://github.com/apache/tvm/pull/19416) - [TVMScript] Print ExternFunc struct_info when non-default
 * [#19415](https://github.com/apache/tvm/pull/19415) - [Frontend][TFLite] Fix bool `REDUCE_ANY`/`REDUCE_ALL` compile failure
 * [#19413](https://github.com/apache/tvm/pull/19413) - [Frontend][TFLite] Add `REDUCE_ANY` and `REDUCE_ALL`
 * [#19411](https://github.com/apache/tvm/pull/19411) - fix 'occured' -> 'occurred' in transform.h doc comment
 * [#19408](https://github.com/apache/tvm/pull/19408) - [Frontend][TFLite] Fix and test `MATRIX_DIAG`, `MATRIX_SET_DIAG`, `SPARSE_TO_DENSE`
 * [#19405](https://github.com/apache/tvm/pull/19405) - [Frontend][KVCache] Restructure kv_cache kernels
 * [#19404](https://github.com/apache/tvm/pull/19404) - [tflite] Add PRELU/LRN/SQUARED_DIFFERENCE tests (partial #18971)
 * [#19392](https://github.com/apache/tvm/pull/19392) - [Frontend][KVCache] Add masked sequence prefill helper for encoder valid lengths
 * [#19372](https://github.com/apache/tvm/pull/19372) - [frontend][tflite] Add tests for fully_connected/depthwise_conv2d/transpose_conv/l2_pool2d
 * [#19391](https://github.com/apache/tvm/pull/19391) - [ONNX] Add frontend support for QuantizeLinear, DequantizeLinear, and DynamicQuantizeLinear
 * [#19384](https://github.com/apache/tvm/pull/19384) - [BugFix]Select target-specific pipeline in tvm.compile when GPU target is provided
 * [#19371](https://github.com/apache/tvm/pull/19371) - [frontend][tflite] Add tests for l2_normalization/slice/reverse_v2
 * [#19345](https://github.com/apache/tvm/pull/19345) - [Frontend][TFLite] Implement DETECTION_POSTPROCESS tflite operator
 * [#19381](https://github.com/apache/tvm/pull/19381) - [TFLite] Fix and test DEPTH_TO_SPACE/SPACE_TO_DEPTH, SELECT ops
 * [#19373](https://github.com/apache/tvm/pull/19373) - [TFLite] Fix `MIRROR_PAD`/`ONE_HOT` converters and add tests for `PAD`, `PADV2`, `MIRROR_PAD`, `TOPK_V2`, `ONE_HOT`
 * [#19370](https://github.com/apache/tvm/pull/19370) - [TFLite] Add test coverage for Reduction operations (#18971)
 * [#19361](https://github.com/apache/tvm/pull/19361) - [ONNX] Support ConcatFromSequenc/SequenceInsert with new_axis=1
 * [#19349](https://github.com/apache/tvm/pull/19349) - [TFLite] Add NON_MAX_SUPPRESSION_V5 support
 * [#18963](https://github.com/apache/tvm/pull/18963) - [ONNX] Support Resize dynamic ROI via TOPI
 * [#18955](https://github.com/apache/tvm/pull/18955) - [ONNX] Fix shape/dynamic restrictions for `Squeeze`/`Unsqueeze` and `Slice`
 * [#18956](https://github.com/apache/tvm/pull/18956) - [ONNX] Complete ShapeExpr reshape handling in ONNX frontend
 * [#18950](https://github.com/apache/tvm/pull/18950) - [ONNX] Add Optional and MatMulInteger16 frontend support
 * [#18952](https://github.com/apache/tvm/pull/18952) - [ONNX] Add roi_pool op and MaxRoiPool frontend support
 * [#18948](https://github.com/apache/tvm/pull/18948) - Add conv3d_transpose and ONNX ConvTranspose 3D support
 * [#18943](https://github.com/apache/tvm/pull/18943) - [Vision] Add get_valid_counts and classic NMS
 * [#18942](https://github.com/apache/tvm/pull/18942) - [TOPI] Add relax.vision.multibox_transform_loc for SSD/TFLite box decode
 * [#18933](https://github.com/apache/tvm/pull/18933) - Add affine_grid operator with PyTorch and ONNX frontend support
 * [#18937](https://github.com/apache/tvm/pull/18937) - [PyTorch] Add 3D interpolate support using resize3d
 * [#18936](https://github.com/apache/tvm/pull/18936) - [ONNX][Torch] Add roi_align support and frontend integration
 * [#18931](https://github.com/apache/tvm/pull/18931) - [ONNX] Add image.resize3d op and wire 5D Resize
 * [#18932](https://github.com/apache/tvm/pull/18932) - [ONNX] Add GridSample ONNX frontend integration
 * [#18868](https://github.com/apache/tvm/pull/18868) - [TFLite] Introduce TensorFlow Lite frontend
 * [#18869](https://github.com/apache/tvm/pull/18869) - [LAYOUT] Support multiple axis paching
 * [#18904](https://github.com/apache/tvm/pull/18904) - [PyTorch] Add torch.cond support to ExportedProgram frontend
 * [#18870](https://github.com/apache/tvm/pull/18870) - Add input type validation for make_shape and corresponding tests
 * [#18903](https://github.com/apache/tvm/pull/18903) - [PyTorch] Fix crash on dynamic shapes with identity slice in ExportedProgram importer
 * [#18878](https://github.com/apache/tvm/pull/18878) - [ONNX] Support dynamic repeats for Tile
 * [#18864](https://github.com/apache/tvm/pull/18864) - [Refactor] Phase out FewShotTuning
 * [#18814](https://github.com/apache/tvm/pull/18814) - Make ShapeType ndim parameter mandatory
 * [#18815](https://github.com/apache/tvm/pull/18815) - [PyTroch] Add randn.default and randn_like.default support
 * [#18520](https://github.com/apache/tvm/pull/18520) - Fix llama4_rope_with_position_map to support partial rotary factor
 * [#18764](https://github.com/apache/tvm/pull/18764) - Add size heuristic to skip folding large creation ops
 * [#18762](https://github.com/apache/tvm/pull/18762) - Remove TODO comment for moving code in fuse_tir.cc
 * [#18733](https://github.com/apache/tvm/pull/18733) - Migrate NN conv/pooling/grad attrs from Array<IntImm> to Array<int64_t>
 * [#18736](https://github.com/apache/tvm/pull/18736) - Support constant folding for call_tir with tuple outputs
 * [#18726](https://github.com/apache/tvm/pull/18726) - [PyTorch] Simplify tensor args conversion in Dynamo
 * [#18725](https://github.com/apache/tvm/pull/18725) - [PyTorch] Fix scalar parameter inputs in Dynamo
 * [#18670](https://github.com/apache/tvm/pull/18670) - [Torch] Avoid decomposition crash with sparse CSR buffers
 * [#18704](https://github.com/apache/tvm/pull/18704) - [Onnx][BatchNorm] Pass momentum and training_mode into BatchNorm Operator
 * [#18661](https://github.com/apache/tvm/pull/18661) - [Python]Fix YaRN correction dim calculation
 * [#18691](https://github.com/apache/tvm/pull/18691) - [Onnx][Resize] Fix ROI values when tensor ROI is Empty pass node Constant
 * [#18673](https://github.com/apache/tvm/pull/18673) - [Onnx] Support Multi Input Ops with Multidirectional Broadcasting
 * [#18677](https://github.com/apache/tvm/pull/18677) - [NN] Add batch_flatten operator
 * [#18690](https://github.com/apache/tvm/pull/18690) - Add NN operator attributes include to TensorRT codegen

### Runtime
 * [#19476](https://github.com/apache/tvm/pull/19476) - [REFACTOR]Phase out include/tvm/runtime/object.h
 * [#19465](https://github.com/apache/tvm/pull/19465) - [REFACTOR][CODEGEN] Backend specific target and runtime to enable cross-compile fallback
 * [#19471](https://github.com/apache/tvm/pull/19471) - [REFACTOR]Phase out IntTuple alias; use ffi::Shape directly
 * [#19472](https://github.com/apache/tvm/pull/19472) - [REFACTOR]Phase out include/tvm/runtime/builtin_fp16.h
 * [#19469](https://github.com/apache/tvm/pull/19469) - [REFACTOR]Phase out include/tvm/runtime/threading_backend.h
 * [#19455](https://github.com/apache/tvm/pull/19455) - [REFACTOR]Phase out profiling.h heavy types, rename to timer.h
 * [#19457](https://github.com/apache/tvm/pull/19457) - [REFACTOR]Macro cleanup — TVM_DLL alignment, [[maybe_unused]], logging.h legacy macros
 * [#18837](https://github.com/apache/tvm/pull/18837) - [Builtin] Handle mismatched type on argument #0 when calling Builtin Runtime Operators
 * [#18813](https://github.com/apache/tvm/pull/18813) - [REFACTOR]Phase out legacy contrib runtime backends
 * [#18784](https://github.com/apache/tvm/pull/18784) - [REFACTOR]Transition metadata into ffi
 * [#18756](https://github.com/apache/tvm/pull/18756) - [COMPACT] Fix 32bit compact in vm

### TOPI
 * [#18880](https://github.com/apache/tvm/pull/18880) - Reject non-float inputs for inverse unary math ops

### TVMScript
 * [#18891](https://github.com/apache/tvm/pull/18891) - Remove T.Bind backward-compat alias
 * [#18889](https://github.com/apache/tvm/pull/18889) - Normalize T.Bind to T.bind for statement builder convention
 * [#18856](https://github.com/apache/tvm/pull/18856) - Fix PEP 563 closure variable resolution

### Vulkan
 * [#18914](https://github.com/apache/tvm/pull/18914) - Avoid explicit layout decoration on non-interface allocations

### web
 * [#18944](https://github.com/apache/tvm/pull/18944) - Update includes after FFI JSON refactor
 * [#18893](https://github.com/apache/tvm/pull/18893) - [Experimental] Add support for cross-origin storage caching
 * [#18680](https://github.com/apache/tvm/pull/18680) - [Version] Fix WebLLM vision model issues
 * [#18687](https://github.com/apache/tvm/pull/18687) - Handle LocalSession init in WASM RPC server

### Misc
 * [#19483](https://github.com/apache/tvm/pull/19483) - [REFACTOR][FFI] Cleanup ffi indirections in tvm headers + switch logging.h to ffi/error.h where only ICHECK/THROW are used
 * [#19484](https://github.com/apache/tvm/pull/19484) - [FFI][ABI] Bump tvm-ffi to 0.1.11rc2
 * [#19477](https://github.com/apache/tvm/pull/19477) - [REFACTOR] Delete src/support/libinfo.cc; replace with runtime FFI-registry env query
 * [#19479](https://github.com/apache/tvm/pull/19479) - [REFACTOR][SCRIPT] TVMScript dialect-friendly refactor: per-dialect restructure + dialect registry
 * [#19475](https://github.com/apache/tvm/pull/19475) - [REFACTOR][S-TIR] Move tvm/support/random_engine.h → tvm/s_tir/random_engine.h
 * [#19474](https://github.com/apache/tvm/pull/19474) - [REFACTOR][IR] Move tvm/support/with.h → tvm/ir/with_context.h
 * [#19453](https://github.com/apache/tvm/pull/19453) - [S-TIR][Dlight] Add layered fall back strategy to handle missing attr `max_shared_memory_per_block`
 * [#19463](https://github.com/apache/tvm/pull/19463) - [REFACTOR][IR] Migrate include/tvm/node into include/tvm/ir
 * [#19462](https://github.com/apache/tvm/pull/19462) - [REFACTOR][NODE] Use fn_repr inside kRepr lambdas, not ffi::ReprPrint
 * [#19460](https://github.com/apache/tvm/pull/19460) - [REFACTOR][S-TIR] Minimize src/support/ by relocating s_tir-private headers
 * [#19459](https://github.com/apache/tvm/pull/19459) - [REFACTOR] Phase out src/support/ffi_testing.cc
 * [#19461](https://github.com/apache/tvm/pull/19461) - [REFACTOR][NODE] Migrate ReprPrinter to tvm-ffi __ffi_repr__ mechanism
 * [#19456](https://github.com/apache/tvm/pull/19456) - [REFACTOR] Move source_utils.h into runtime/opencl
 * [#19458](https://github.com/apache/tvm/pull/19458) - [REFACTOR] Phase out unreachable contrib/rust_extension.cc
 * [#19454](https://github.com/apache/tvm/pull/19454) - [REFACTOR][CODEGEN] Phase out tvm_global_barrier_state and tvm_prepare_global_barrier
 * [#19449](https://github.com/apache/tvm/pull/19449) - [REFACTOR] Use FFI types in runtime inline module-create wrapper signatures
 * [#18406](https://github.com/apache/tvm/pull/18406) - [TIR] Update symbolic index term order in loop fusion
 * [#19447](https://github.com/apache/tvm/pull/19447) - [REFACTOR] Isolate backend module creation via ffi.Module.create.<kind> registry
 * [#19444](https://github.com/apache/tvm/pull/19444) - [CMAKE][REFACTOR] Split libtvm.so into libtvm_runtime.so and libtvm_compiler.so
 * [#19440](https://github.com/apache/tvm/pull/19440) - [REFACTOR] Remove runtime/object.py shim and route Object via tvm_ffi
 * [#19442](https://github.com/apache/tvm/pull/19442) - [REFACTOR] Remove tvm.runtime.packed_func and container shims; route via tvm_ffi
 * [#19441](https://github.com/apache/tvm/pull/19441) - [REFACTOR] Phase out include/tvm/runtime/module.h
 * [#19393](https://github.com/apache/tvm/pull/19393) - fix: use `is None` instead of `== None` in test files (PEP 8 E711)
 * [#19406](https://github.com/apache/tvm/pull/19406) -  [S-TIR] Fix cache_read/cache_write region when inner block has T.whe…
 * [#19403](https://github.com/apache/tvm/pull/19403) - [S-TIR] Fix Segfault when applying Parallel during TIR schedule rewriting
 * [#18927](https://github.com/apache/tvm/pull/18927) - feat(meta_schedule): expand CUDA unroll steps for SM70 optimization
 * [#19347](https://github.com/apache/tvm/pull/19347) - fix: TFLite model retrieval with error handling
 * [#19343](https://github.com/apache/tvm/pull/19343) - test(relax): cover TFLite LOG and GREATER_EQUAL in test_frontend_tflite
 * [#18938](https://github.com/apache/tvm/pull/18938) - [FFI] Bump tvm-ffi to 63224e3 and fix regressions
 * [#18912](https://github.com/apache/tvm/pull/18912) - [TIR] Handle Bind in LowerDeviceKernelLaunch
 * [#18926](https://github.com/apache/tvm/pull/18926) - Revert "fix: add safety warning to pickle_memoize cache loading"
 * [#18925](https://github.com/apache/tvm/pull/18925) - fix: add safety warning to pickle_memoize cache loading
 * [#18913](https://github.com/apache/tvm/pull/18913) - [Refactor] Bring up tirx namespace
 * [#18240](https://github.com/apache/tvm/pull/18240) - [Optimization][Operator] Implement and enable Conv2d-Reshape-Add-ReLU fusion
 * [#18892](https://github.com/apache/tvm/pull/18892) - [Build] Fix version regex to anchor at line start in pyproject.toml
 * [#18879](https://github.com/apache/tvm/pull/18879) - [TIR] Reject non-floating inputs for trig unary ops
 * [#18886](https://github.com/apache/tvm/pull/18886) - [TIR][REFACTOR] Revamp Common Subexpression Elimination
 * [#18883](https://github.com/apache/tvm/pull/18883) - [TARGET] Fix round-trip reconstruction of targets with canonicalizer-generated `feature.*` attrs
 * [#18876](https://github.com/apache/tvm/pull/18876) - [REFACTOR][TIR] Remove body from AllocBuffer and DeclBuffer
 * [#18871](https://github.com/apache/tvm/pull/18871) - Batched GPU dispatch and object caching for WebGPU runtime
 * [#18875](https://github.com/apache/tvm/pull/18875) - [chore] Update docker/README.md documentation and fix links
 * [#18873](https://github.com/apache/tvm/pull/18873) - [TIR] Add VisitBufferDef/VisitBufferUse to base StmtVisitor/StmtMutator
 * [#18865](https://github.com/apache/tvm/pull/18865) - [REFACTOR][TIR] Introduce AllocBuffer and phase out Allocate+DeclBuffer
 * [#18862](https://github.com/apache/tvm/pull/18862) - [REFACTOR][TIR] Cleanup AttrStmt attributes
 * [#18857](https://github.com/apache/tvm/pull/18857) - [TIR][Refactor] Enhance error reporting with structured AssertStmt and TVMFFIABIBuilder
 * [#18861](https://github.com/apache/tvm/pull/18861) - fix: Complete CHECK update across contrib runtime
 * [#18859](https://github.com/apache/tvm/pull/18859) - fix: Use T.decl_buffer instead of T.Buffer for aliased buffers in LongRoPE
 * [#18858](https://github.com/apache/tvm/pull/18858) - fix: Complete ICHECK update across codebase
 * [#18845](https://github.com/apache/tvm/pull/18845) - [REFACTOR][CONTRIB] Remove MSC contrib module
 * [#18847](https://github.com/apache/tvm/pull/18847) - [PYTHON] Fix PEP 563 compat and remove args_converter
 * [#18843](https://github.com/apache/tvm/pull/18843) - [TIR][FEAT] Require DeclBuffer before use in verify_well_formed
 * [#18852](https://github.com/apache/tvm/pull/18852) - [REFACTOR] Remove unused mscclpp contrib module
 * [#18849](https://github.com/apache/tvm/pull/18849) - [CMAKE] Remove unused Libbacktrace.cmake
 * [#18844](https://github.com/apache/tvm/pull/18844) - [REFACTOR] Further cleanup node redirections
 * [#18830](https://github.com/apache/tvm/pull/18830) - [LINT][PYTHON] Modernize annotations with ruff UP rules
 * [#18832](https://github.com/apache/tvm/pull/18832) - [IR][TIR] Remove body from AssertStmt
 * [#18829](https://github.com/apache/tvm/pull/18829) - [REFACTOR][NODE] Remove node redirect headers
 * [#18825](https://github.com/apache/tvm/pull/18825) - [REFACTOR] Update CHECK and ICHECK_GE to TVM_FFI_ICHECK and TVM_FFI_ICHECK_GE in thrust.cu
 * [#18828](https://github.com/apache/tvm/pull/18828) - [REFACTOR] Phase out root Makefile
 * [#18821](https://github.com/apache/tvm/pull/18821) - fix: replace 6 bare except clauses with except Exception
 * [#18822](https://github.com/apache/tvm/pull/18822) - [TARGET] Specify correct `mcpu` for Metal target tags
 * [#18816](https://github.com/apache/tvm/pull/18816) - [REFACTOR][S-TIR] Lift STIR-only attributes out of tir::attr namespace
 * [#18810](https://github.com/apache/tvm/pull/18810) - [REFACTOR][LINT] Modernize ruff config
 * [#18801](https://github.com/apache/tvm/pull/18801) - Bump tvm-ffi to v0.1.9rc
 * [#18807](https://github.com/apache/tvm/pull/18807) - [LINT] Modernize lint to use pre-commit hooks
 * [#18803](https://github.com/apache/tvm/pull/18803) - [REFACTOR] Migrate CHECK macros to tvm-ffi ones
 * [#18768](https://github.com/apache/tvm/pull/18768) - support integer types in fast_tanh and fast_exp
 * [#18802](https://github.com/apache/tvm/pull/18802) - [FFI] Bring up latest tvm-ffi
 * [#18793](https://github.com/apache/tvm/pull/18793) - [REFACTOR][TARGET] Further cleanup target python api
 * [#18785](https://github.com/apache/tvm/pull/18785) - [REFACTOR][TARGET] Phase out legacy target string in favor of json
 * [#18786](https://github.com/apache/tvm/pull/18786) - [CONTRIB] Cache the shape and dtype array in json access
 * [#18781](https://github.com/apache/tvm/pull/18781) - [chore] cleanup unsed legacy backtrac code in logging
 * [#18779](https://github.com/apache/tvm/pull/18779) - [REFACTOR] Phase out dmlc dep
 * [#18776](https://github.com/apache/tvm/pull/18776) - [REFACTOR][S-TIR] More migrations to s-tir
 * [#18771](https://github.com/apache/tvm/pull/18771) - [REFACTOR][S-TIR] Migrate more transform to s_tir
 * [#18763](https://github.com/apache/tvm/pull/18763) - [REFACTOR][TIR] Phaseout BufferRealize
 * [#18759](https://github.com/apache/tvm/pull/18759) - [REFACTOR] Remove picojson dependency, replace with tvm::ffi::json API
 * [#18760](https://github.com/apache/tvm/pull/18760) - [chore] Cleanup stale dependencies
 * [#18761](https://github.com/apache/tvm/pull/18761) - [REFATOR][TIR] Phase out AllocConst
 * [#18758](https://github.com/apache/tvm/pull/18758) - [Cleanup] Remove redundant python/pyproject.toml and gen_requirements
 * [#18697](https://github.com/apache/tvm/pull/18697) - Fix Customize Optimization tutorial import error #18584
 * [#18754](https://github.com/apache/tvm/pull/18754) - [REFACTOR][S-TIR] Cleanup items on block scope
 * [#18743](https://github.com/apache/tvm/pull/18743) - [REFACTOR][S-TIR] Move remaining data structures to s_tir
 * [#18739](https://github.com/apache/tvm/pull/18739) - fix: correct typos 'recieve' and 'occurence'
 * [#18744](https://github.com/apache/tvm/pull/18744) - fix: skip dsymutil for static tvm_runtime on Apple platforms
 * [#18740](https://github.com/apache/tvm/pull/18740) - fix: correct typo 'occuring' to 'occurring'
 * [#18738](https://github.com/apache/tvm/pull/18738) - [chore][TIR] reorganize src/tir/transforms to src/tir/transform
 * [#18734](https://github.com/apache/tvm/pull/18734) - [REFACTOR][S-TIR] Lift dlight into s_tir namespace
 * [#18735](https://github.com/apache/tvm/pull/18735) - [REFACTOR][S-TIR] Migrate meta_schedule into s_tir namespace
 * [#18705](https://github.com/apache/tvm/pull/18705) - Add Windows-specific build notes to installation guide
 * [#18727](https://github.com/apache/tvm/pull/18727) - fix: correct typos in Python docstrings
 * [#18728](https://github.com/apache/tvm/pull/18728) - [REFACTOR][S-TIR] Migrate tir/schedule to s_tir
 * [#18722](https://github.com/apache/tvm/pull/18722) - [REFACTOR][S-TIR] Lift transform passes to s_tir namespace
 * [#18724](https://github.com/apache/tvm/pull/18724) - Remove cron schedule from nightly Docker update workflow
 * [#18716](https://github.com/apache/tvm/pull/18716) - [REFACTOR] Migrate old tir.ir_builder to tvmscript or builder
 * [#18715](https://github.com/apache/tvm/pull/18715) - [SPIRV] Fix forloop codegen in vulkan
 * [#18712](https://github.com/apache/tvm/pull/18712) - [REFACTOR][S-TIR] Initialize the s_tir module
 * [#18636](https://github.com/apache/tvm/pull/18636) - [TIR][Schedule]Generalize fuseReductionEpilogue to support arbitrary epilogue expressions
 * [#18699](https://github.com/apache/tvm/pull/18699) - [TIR] Further robustify floordiv/mod intrin lowering to prevent overflow
 * [#18689](https://github.com/apache/tvm/pull/18689) - [REFACTOR][TIR] Rename tir.Block to SBlock
 * [#18671](https://github.com/apache/tvm/pull/18671) - [TIR] Fix InjectPTXLDG32 segfaults and skip non-CUDA targets




## v0.25.0.rc0 (2026-06-08)

## What's Changed
* [release][Dont Squash] Update version to 0.24.0 and 0.25.0.dev on main branch by @ysh329 in https://github.com/apache/tvm/pull/19446
* [Relax][Frontend] Add ParameterList and ParameterDict containers by @mshr-h in https://github.com/apache/tvm/pull/19495
* [Relax][Frontend][TFLite] Add segment operator mappings by @Aharrypotter in https://github.com/apache/tvm/pull/19491
* [BUGFIX][TIR] Skip bool-typed expressions in CSE by @tqchen in https://github.com/apache/tvm/pull/19502
* [Relax][Frontend][TFLite] Add tests coverage for SPACE_TO_BATCH_ND and BATCH_TO_SPACE_ND by @rknastenka in https://github.com/apache/tvm/pull/19499
* [BugFix][Relax] Fix scatter_elements and scatter_nd CUDA compilation by @as4230 in https://github.com/apache/tvm/pull/19497
* [BugFix][Relax][ONNX] Resolve param Vars in Concat to handle mixed Shape/Tensor inputs by @swjng in https://github.com/apache/tvm/pull/19498
* [Web] Add support for OPFS by @akaashrp in https://github.com/apache/tvm/pull/19494
* [BugFix][Relax][Torch] Honor multi-axis dims in torch.flip converter by @swjng in https://github.com/apache/tvm/pull/19511
* [BugFix][Relax][Torch] Honor `correction` in std/var converter by @swjng in https://github.com/apache/tvm/pull/19512
* [BugFix][S-TIR] Wrap bare scalar bodies in DefaultGPUSchedule to avoid root-block crash by @swjng in https://github.com/apache/tvm/pull/19514
* [Relax][TFLite] Add gather frontend expected IRModule tests by @weicheng-hsu in https://github.com/apache/tvm/pull/19516
* [Relax][PyTorch] Fix segfault in from_exported_program when model uses index_put_ with tuple output by @cchung100m in https://github.com/apache/tvm/pull/19488
* [Relax][Frontend][TFLite] Add Conv3D support by @weicheng-hsu in https://github.com/apache/tvm/pull/19523
* [REFACTOR][IR] Remove dead AttrFunctor template by @tqchen in https://github.com/apache/tvm/pull/19528
* [Relax][ONNX] Normalize negative indices before the take call for `Gather` operator by @cchung100m in https://github.com/apache/tvm/pull/19525
* [Relax][Frontend] Add TFLite Frontend Support for CONV_3D_TRANSPOSE by @weicheng-hsu in https://github.com/apache/tvm/pull/19530
* [TIR] Add cooperative_tensor builtins and metal.cooperative_tensor storage scope by @oraluben in https://github.com/apache/tvm/pull/19423
* [Relax][Frontend][TFLite] Add initial StableHLO builtin operator support by @Aharrypotter in https://github.com/apache/tvm/pull/19536
* [Contrib] Fix CUDA contrib build after FFI/header cleanups by @MasterJH5574 in https://github.com/apache/tvm/pull/19539
* [BugFix][Relax]: handle ONNX ScatterElements reduction by @THINKER-ONLY in https://github.com/apache/tvm/pull/19527
* [Fix][Relax]: ONNX Clip NaN bounds and preserve input NaN (ORT parity) by @ConvolutedDog in https://github.com/apache/tvm/pull/19535
* [Fix][CI]: remove astral-sh/setup-uv from lint workflow by @ConvolutedDog in https://github.com/apache/tvm/pull/19554
* [Relax][ONNX] Set `max_output_boxes_per_class` default value to 0 for NonMaxSuppression by @cchung100m in https://github.com/apache/tvm/pull/19547
* [Relax][ONNX] Add ONNX Backend Tests for systematic frontend coverage by @Aharrypotter in https://github.com/apache/tvm/pull/19515
* [Fix][Relax] Lower bool prod as logical all by @ConvolutedDog in https://github.com/apache/tvm/pull/19557
* [Relax][ONNX] Prevent `Div` divide-by-zero crashes by @cchung100m in https://github.com/apache/tvm/pull/19566
* [TIRx] Bringup TIRx Infrastructure by @spectrometerHBH in https://github.com/apache/tvm/pull/19581
* [BugFix][Target][LLVM] Use libm for asin/acos instead of buggy inline Taylor by @swjng in https://github.com/apache/tvm/pull/19567
* [RFC][CodeGen][CUDA]: Gate fast math intrinsic lowering behind target option by @ConvolutedDog in https://github.com/apache/tvm/pull/19565
* [TVMScript] Handle undefined functions when dumping IRModule by @ConvolutedDog in https://github.com/apache/tvm/pull/19583
* [BugFix][Target][LLVM] Route sinh/cosh/atan/asinh/erf through libm extern by @swjng in https://github.com/apache/tvm/pull/19568
* [Relax][ONNX] Fix TopK scalar K extraction in from_onnx by @javierdejesusda in https://github.com/apache/tvm/pull/19573
* [Relax][Frontend][TFLite] Support StableHLO region-based ops and multi-subgraph models by @Aharrypotter in https://github.com/apache/tvm/pull/19587
* [ONNX] Add RMSNormalization converter for ONNX opset 23 by @q55180514 in https://github.com/apache/tvm/pull/19590
* [BUILD] Modularize device runtime into per-backend DSOs by @tqchen in https://github.com/apache/tvm/pull/19594
* [Relax] Normalize negative concat axis in ReorderPermuteDimsAfterConcat by @cchung100m in https://github.com/apache/tvm/pull/19588
* [RPC][Tracker] Bound msg_size to MAX_TRACKER_MSG_BYTES to prevent unbounded buffer growth by @bl4cksku11 in https://github.com/apache/tvm/pull/19586
* [CodeGen][CUDA] Move fast math intrinsic lowering option to PassContext by @tlopex in https://github.com/apache/tvm/pull/19596
* [IR] Add annotations to Call nodes by @tlopex in https://github.com/apache/tvm/pull/19597
* [REFACTOR][RELAX] Fold CalleeCollector into relax DeadCodeElimination by @tqchen in https://github.com/apache/tvm/pull/19603
* [Relax][Frontend][TFLite] Support quantized TFLite import via QDQ decomposition by @Aharrypotter in https://github.com/apache/tvm/pull/19538
* Fix PytestUnknownMarkWarning: Unknown pytest.mark.adreno_clml by @cchung100m in https://github.com/apache/tvm/pull/19602
* [REFACTOR][IR] Cleanup attrs.h: drop NullValue, AttrsNodeReflAdapter, legacy BaseAttrsNode methods by @tqchen in https://github.com/apache/tvm/pull/19607
* [Docs] Reorganize development guide content by @tlopex in https://github.com/apache/tvm/pull/19606
* [REFACTOR] Move src/ir/script_printer.cc to src/script/printer/ by @tqchen in https://github.com/apache/tvm/pull/19611
* [REFACTOR][IR] Phase out src/ir/structural_{hash,equal}.cc to tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/19613
* [REFACTOR][IR] Inline ApplyPassToFunction into relax decompose_ops, delete the util by @tqchen in https://github.com/apache/tvm/pull/19612
* [REFACTOR][TIR][ARITH] Phase out ControlFlowGraph, NarrowPredicateExpression, and rename Simplify to StmtSimplify by @tqchen in https://github.com/apache/tvm/pull/19604
* [REFACTOR][IR] Phase out class Integer and class Bool in Attrs and PassConfig by @tqchen in https://github.com/apache/tvm/pull/19614
* [CMAKE][RUNTIME] Link tvm_rpc with all backend runtime libraries by @cbalint13 in https://github.com/apache/tvm/pull/19617
* [REFACTOR][IR] attrs.h follow-up cleanup: drop legacy vtable / rename / phase out AttrFieldInfo by @tqchen in https://github.com/apache/tvm/pull/19615
* [REFACTOR][TIR] Tie AnnotateDeviceRegions/SplitHostDevice/LowerDeviceKernelLaunch together by @tqchen in https://github.com/apache/tvm/pull/19605
* [Relax][Frontend][TFLite] Support control-flow multi-subgraph operators by @Aharrypotter in https://github.com/apache/tvm/pull/19616
* [Relax][Frontend][TFLite] Add UNIDIRECTIONAL_SEQUENCE_RNN converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19601
* [IR] Rename Call annotations to attrs by @tlopex in https://github.com/apache/tvm/pull/19618
* [REFACTOR][RUNTIME] Phase out tvm::runtime::regex_match by @tqchen in https://github.com/apache/tvm/pull/19620
* [REFACTOR][RUNTIME] Remove leftover microTVM/CRT crumbs by @tqchen in https://github.com/apache/tvm/pull/19622
* [REFACTOR][RUNTIME] Relocate nvtx.h to tvm/support/cuda and make it header-only by @tqchen in https://github.com/apache/tvm/pull/19621
* [REFACTOR][PYTHON] Lift compiler/CLI/process modules from tvm.contrib to tvm.support by @tqchen in https://github.com/apache/tvm/pull/19624
* [REFACTOR][IR][FFI] Bump tvm-ffi (+ SEqHashDef migration) and phase out tvm/ir/repr.h by @tqchen in https://github.com/apache/tvm/pull/19627
* [REFACTOR][IR] Inline ReplaceGlobalVars into AttachGlobalSymbol by @tqchen in https://github.com/apache/tvm/pull/19625
* [BugFix][Vulkan][CodeGen] Change OpControlBarrier to AcquireRelease by @kistenklaus in https://github.com/apache/tvm/pull/19619
* [REFACTOR][RUNTIME] Structural reorganization: locality moves for thread_map, texture, minrpc, disco, contrib by @tqchen in https://github.com/apache/tvm/pull/19628
* [REFACTOR][PYTHON] Consolidate derived_object into tvm.ir.utils by @tqchen in https://github.com/apache/tvm/pull/19630
* [CI] Remove tvm-lint from tvm-bot by @yongwww in https://github.com/apache/tvm/pull/19629
* [REFACTOR][SCRIPT] tvmscript streamline: lift printer.h, restore one-way dep, migrate dialect config to extra_config by @tqchen in https://github.com/apache/tvm/pull/19631
* [REFACTOR][ARITH] Phase out arith/scalable_expression; arith no longer proves over scalable vectors by @tqchen in https://github.com/apache/tvm/pull/19638
* [Relax][Frontend][TFLite] Add REDUCE_WINDOW support by @THINKER-ONLY in https://github.com/apache/tvm/pull/19637
* [Relax][Frontend][TFLite] Add RNN converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19632
* [REFACTOR][IR] Delete class Bool and class Integer boxed-type wrappers by @tqchen in https://github.com/apache/tvm/pull/19636
* [Relax][Frontend][TFLite] Add LSTM and SVDF converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19633
* [Relax][Frontend][TFLite] Add TFLite Resource Variable and Static Hashtable Import Support by @Aharrypotter in https://github.com/apache/tvm/pull/19639
* [TIRx] Fix stale Simplify import in lowering test by @tlopex in https://github.com/apache/tvm/pull/19642
* [Relax][Frontend][TFLite] Support sequence LSTM and RNN operators by @LudovicoYIN in https://github.com/apache/tvm/pull/19634
* [Relax][Frontend][TFLite] Support STABLEHLO_WHILE by @Aharrypotter in https://github.com/apache/tvm/pull/19646
* [Fix] Stabilize layer_norm variance computation with two-pass reduction by @ConvolutedDog in https://github.com/apache/tvm/pull/19643
* [Relax][IR] Skip in-place multiply when two operands are views of the same tensor by @ConvolutedDog in https://github.com/apache/tvm/pull/19644
* [Relax][Frontend][TFLite] Support STABLEHLO_CUSTOM_CALL by @Aharrypotter in https://github.com/apache/tvm/pull/19649
* [REFACTOR][PYTHON] Revisit lifted support modules from tvm.contrib by @cbalint13 in https://github.com/apache/tvm/pull/19653
* [Relax][Frontend][TFLite] Add HASHTABLE_LOOKUP converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19654
* [Relax][Frontend][TFLite] Support STABLEHLO_RNG_BIT_GENERATOR by @Aharrypotter in https://github.com/apache/tvm/pull/19651
* fix: Security Patch: Fix missing exported flag in AndroidManifest by @CodeMechanic-Bot in https://github.com/apache/tvm/pull/19648
* [Relax][PyTorch] Cast non-bool inputs to bool in logical_not converter by @javierdejesusda in https://github.com/apache/tvm/pull/19645
* [Web][COS] Persist URL→hash mapping across page loads by @tomayac in https://github.com/apache/tvm/pull/19569
* [Fix][Relax] Support ND batched matmul chains in AdjustMatmulOrder pass by @ConvolutedDog in https://github.com/apache/tvm/pull/19650
* [Relax][Frontend][TFLite] Add EMBEDDING_LOOKUP_SPARSE converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19652
* [CI] Add cibw-based wheel publishing to PyPI by @tlopex in https://github.com/apache/tvm/pull/19656
* [TIRx] Post-bringup op-dispatch / codegen / TVMScript follow-ups by @spectrometerHBH in https://github.com/apache/tvm/pull/19657
* [RPC] Import tvm.testing lazily in rpc.testing by @tlopex in https://github.com/apache/tvm/pull/19658
* [CI] Wheel publishing follow-ups by @tlopex in https://github.com/apache/tvm/pull/19659
* [REFACTOR][TIRX] Consolidate split host device stages by @tqchen in https://github.com/apache/tvm/pull/19663
* [FFI][IR] Route JSON serialization through tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/19662
* [Relax][PyTorch] Decompose integer pow into repeated multiplication by @javierdejesusda in https://github.com/apache/tvm/pull/19660
* [CI] Derive the version from Git tags via setuptools_scm by @tlopex in https://github.com/apache/tvm/pull/19665
* [CI] Reformat the macOS repair-wheel-command as a multiline script by @tlopex in https://github.com/apache/tvm/pull/19664
* [FFI][REFACTOR] Direct structural APIs to tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/19661
* [Arith] Memoize IntervalSet variable relaxation to avoid exponential blowup by @jinhongyii in https://github.com/apache/tvm/pull/19670
* [Arith] Gate canonical-simplify LT Case 2 on extra scale == +1 by @jinhongyii in https://github.com/apache/tvm/pull/19669
* [Relax][ONNX] Fix Cast operator float->int NaN/Inf handling by @cchung100m in https://github.com/apache/tvm/pull/19626
* [TIRx] Update scoped ops and CUDA launch bounds by @spectrometerHBH in https://github.com/apache/tvm/pull/19677
* [Relax][ONNX] Preserve NaN in Sign to align with ONNX Runtime by @cchung100m in https://github.com/apache/tvm/pull/19674
* [Bump] tvm-ffi to 59da4c0 by @tqchen in https://github.com/apache/tvm/pull/19681
* [Web] Add support for OPFS synchronous access handles and committed records by @akaashrp in https://github.com/apache/tvm/pull/19673
* [Arith] Make Analyzer a tvm-ffi Object by @tlopex in https://github.com/apache/tvm/pull/19675
* [RELEASE] Bump web npm version to 0.25.0 by @MasterJH5574 in https://github.com/apache/tvm/pull/19684
* [CI] Target apache-tvm for PyPI wheel publishing by @MasterJH5574 in https://github.com/apache/tvm/pull/19697
* [Python] Bump apache-tvm-ffi floor to >=0.1.12 on v0.25.0 by @MasterJH5574 in https://github.com/apache/tvm/pull/19701

## New Contributors
* @weicheng-hsu made their first contribution in https://github.com/apache/tvm/pull/19516
* @THINKER-ONLY made their first contribution in https://github.com/apache/tvm/pull/19527
* @q55180514 made their first contribution in https://github.com/apache/tvm/pull/19590
* @bl4cksku11 made their first contribution in https://github.com/apache/tvm/pull/19586
* @kistenklaus made their first contribution in https://github.com/apache/tvm/pull/19619
* @CodeMechanic-Bot made their first contribution in https://github.com/apache/tvm/pull/19648
* @tomayac made their first contribution in https://github.com/apache/tvm/pull/19569

**Full Changelog**: https://github.com/apache/tvm/compare/v0.24.0...v0.25.0.rc0

## v0.25.0.rc1 (2026-06-16)

## What's Changed
* [CI] Merge PR against its target branch instead of main (#19712) by @MasterJH5574 in https://github.com/apache/tvm/pull/19775
* [RELEASE] Backport main to prepare v0.25.0.rc1 by @MasterJH5574 in https://github.com/apache/tvm/pull/19774
* [v0.25.0] Backport recent main to prepare v0.25.0.rc1 by @MasterJH5574 in https://github.com/apache/tvm/pull/19792
* [CMAKE] Revert build baseline to C++17 by @MasterJH5574 in https://github.com/apache/tvm/pull/19805
* [Fix] Revert C++20-only lambda captures for C++17 build by @MasterJH5574 in https://github.com/apache/tvm/pull/19808


**Full Changelog**: https://github.com/apache/tvm/compare/v0.25.0.rc0...v0.25.0.rc1

## v0.25.0 (2026-06-19)

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): **Relax**, **Frontend**, **TIR**, Runtime, etc.

Please visit the full listing of commits for a complete view: [v0.24.0...v0.25.0](https://github.com/apache/tvm/compare/v0.24.0...v0.25.0).

### Community

None.

### RFCs

None.

### Arith
 * [#19604](https://github.com/apache/tvm/pull/19604) - [REFACTOR][TIR]Phase out ControlFlowGraph, NarrowPredicateExpression, and rename Simplify to StmtSimplify
 * [#19638](https://github.com/apache/tvm/pull/19638) - [REFACTOR]Phase out arith/scalable_expression; arith no longer proves over scalable vectors
 * [#19670](https://github.com/apache/tvm/pull/19670) - Memoize IntervalSet variable relaxation to avoid exponential blowup
 * [#19669](https://github.com/apache/tvm/pull/19669) - Gate canonical-simplify LT Case 2 on extra scale == +1
 * [#19675](https://github.com/apache/tvm/pull/19675) - Make Analyzer a tvm-ffi Object

### BugFix
 * [#19502](https://github.com/apache/tvm/pull/19502) - [TIR] Skip bool-typed expressions in CSE
 * [#19497](https://github.com/apache/tvm/pull/19497) - [Relax] Fix scatter_elements and scatter_nd CUDA compilation
 * [#19498](https://github.com/apache/tvm/pull/19498) - [Relax][ONNX] Resolve param Vars in Concat to handle mixed Shape/Tensor inputs
 * [#19511](https://github.com/apache/tvm/pull/19511) - [Relax][Torch] Honor multi-axis dims in torch.flip converter
 * [#19512](https://github.com/apache/tvm/pull/19512) - [Relax][Torch] Honor `correction` in std/var converter
 * [#19514](https://github.com/apache/tvm/pull/19514) - [S-TIR] Wrap bare scalar bodies in DefaultGPUSchedule to avoid root-block crash
 * [#19527](https://github.com/apache/tvm/pull/19527) - [Relax]: handle ONNX ScatterElements reduction
 * [#19535](https://github.com/apache/tvm/pull/19535) - [Fix][Relax]: ONNX Clip NaN bounds and preserve input NaN (ORT parity)
 * [#19554](https://github.com/apache/tvm/pull/19554) - [Fix][CI]: remove astral-sh/setup-uv from lint workflow
 * [#19557](https://github.com/apache/tvm/pull/19557) - [Fix][Relax] Lower bool prod as logical all
 * [#19567](https://github.com/apache/tvm/pull/19567) - [Target][LLVM] Use libm for asin/acos instead of buggy inline Taylor
 * [#19568](https://github.com/apache/tvm/pull/19568) - [Target][LLVM] Route sinh/cosh/atan/asinh/erf through libm extern
 * [#19619](https://github.com/apache/tvm/pull/19619) - [Vulkan][CodeGen] Change OpControlBarrier to AcquireRelease
 * [#19643](https://github.com/apache/tvm/pull/19643) - [Fix] Stabilize layer_norm variance computation with two-pass reduction
 * [#19650](https://github.com/apache/tvm/pull/19650) - [Fix][Relax] Support ND batched matmul chains in AdjustMatmulOrder pass
 * [#19683](https://github.com/apache/tvm/pull/19683) - [Fix] CommReduce could handle 0-dim data
 * [#19779](https://github.com/apache/tvm/pull/19779) - [Fix] nn.attention support dynamic batch_size
 * [#19808](https://github.com/apache/tvm/pull/19808) - [Fix] Revert C++20-only lambda captures for C++17 build

### CI
 * [#19629](https://github.com/apache/tvm/pull/19629) - Remove tvm-lint from tvm-bot
 * [#19656](https://github.com/apache/tvm/pull/19656) - Add cibw-based wheel publishing to PyPI
 * [#19659](https://github.com/apache/tvm/pull/19659) - Wheel publishing follow-ups
 * [#19665](https://github.com/apache/tvm/pull/19665) - Derive the version from Git tags via setuptools_scm
 * [#19664](https://github.com/apache/tvm/pull/19664) - Reformat the macOS repair-wheel-command as a multiline script
 * [#19697](https://github.com/apache/tvm/pull/19697) - Target apache-tvm for PyPI wheel publishing
 * [#19775](https://github.com/apache/tvm/pull/19775) - Merge PR against its target branch instead of main (#19712)
 * [#19685](https://github.com/apache/tvm/pull/19685) - Remove PyPI-only tag ref guard from wheel publishing
 * [#19703](https://github.com/apache/tvm/pull/19703) - Pin actions by version tag, trim wheel perms
 * [#19706](https://github.com/apache/tvm/pull/19706) - [Tests] Fix s_tir tests using removed T.block API in TIRx script
 * [#19700](https://github.com/apache/tvm/pull/19700) - Fix release verification script
 * [#19704](https://github.com/apache/tvm/pull/19704) - [Tests] Skip test modules cleanly when optional deps are missing
 * [#19713](https://github.com/apache/tvm/pull/19713) - Fix CI script test subprocess environment
 * [#19724](https://github.com/apache/tvm/pull/19724) - [Tests][Disco] Skip CCL tests when runtime support is absent
 * [#19725](https://github.com/apache/tvm/pull/19725) - [Tests][Relax] Gate multi-GPU VM test on three devices
 * [#19726](https://github.com/apache/tvm/pull/19726) - [Tests][Hexagon] Lazily import pytest plugin dependencies
 * [#19730](https://github.com/apache/tvm/pull/19730) - [Tests][NNAPI] Skip tests cleanly when remote environment is unavailable
 * [#19729](https://github.com/apache/tvm/pull/19729) - [Tests][S-TIR] Fix stale MetaSchedule sketch expectations and migrate let binds to T.let
 * [#19715](https://github.com/apache/tvm/pull/19715) - [Tests] Remove test_runtime_ndarray (covered by tvm-ffi)
 * [#19731](https://github.com/apache/tvm/pull/19731) - [Script][Tests] Fix dialect redirect module re-execution and stray category-less tirx.intrin_test op
 * [#19735](https://github.com/apache/tvm/pull/19735) - [S-TIR][Tests] Fix transform test failures after TIRx bringup
 * [#19740](https://github.com/apache/tvm/pull/19740) - [Tests] Check WebGPU volatile allreduce annotation structurally
 * [#19746](https://github.com/apache/tvm/pull/19746) - [Tests] Fix flaky popen pool executor test
 * [#19738](https://github.com/apache/tvm/pull/19738) - Align cuda-python with PyTorch cuda-bindings
 * [#19745](https://github.com/apache/tvm/pull/19745) - [Tests][LLVM] Gate stepvector intrinsic rename on LLVM 20
 * [#19751](https://github.com/apache/tvm/pull/19751) - [S-TIR][Tests] Mark test_cp_async_in_if_then_else as xfail
 * [#19737](https://github.com/apache/tvm/pull/19737) - Run s_tir/transform tests in the python-unittest stage
 * [#19754](https://github.com/apache/tvm/pull/19754) - Updated cibw to 4.1.0
 * [#19752](https://github.com/apache/tvm/pull/19752) - [Tests][AArch64] Make SVE codegen assertions robust across LLVM versions
 * [#19761](https://github.com/apache/tvm/pull/19761) - Drop redundant cmake/ninja install from the Linux wheel CUDA sidecar
 * [#19777](https://github.com/apache/tvm/pull/19777) - [Tests] Modernize test gating
 * [#19786](https://github.com/apache/tvm/pull/19786) - [Tests] Make TargetCreation.DeduplicateKeys host-agnostic on AArch64
 * [#19787](https://github.com/apache/tvm/pull/19787) - [Tests] Replace remaining requires_* helpers with standard pytest
 * [#19793](https://github.com/apache/tvm/pull/19793) - Pin GitHub Actions to SHA for ASF INFRA compliance
 * [#19798](https://github.com/apache/tvm/pull/19798) - Remove Jenkins PR linter step
 * [#19800](https://github.com/apache/tvm/pull/19800) - [Tests][Refactor] Remove unused testing helpers

### Docs
 * [#19606](https://github.com/apache/tvm/pull/19606) - Reorganize development guide content
 * [#19720](https://github.com/apache/tvm/pull/19720) - Clarify loading serialized artifacts requires a trusted source
 * [#19782](https://github.com/apache/tvm/pull/19782) - [CI] Bump tlcpack-sphinx-addon to restore search result summaries
 * [#19788](https://github.com/apache/tvm/pull/19788) - Modernize test-gating documentation

### Frontend
 * [#19590](https://github.com/apache/tvm/pull/19590) - [ONNX] Add RMSNormalization converter for ONNX opset 23

### Hexagon
 * [#19747](https://github.com/apache/tvm/pull/19747) - [Tests] Clean up stale hexagon tests
 * [#19796](https://github.com/apache/tvm/pull/19796) - [REFACTOR]Phase out Hexagon app and test wrappers

### LLVM
 * [#19716](https://github.com/apache/tvm/pull/19716) - [Codegen]Accept splat form in VLA broadcast test
 * [#19744](https://github.com/apache/tvm/pull/19744) - [Codegen][Tests] Gate +v9a vscale_range expectation on LLVM version

### Relax
 * [#19495](https://github.com/apache/tvm/pull/19495) - [Frontend] Add ParameterList and ParameterDict containers
 * [#19491](https://github.com/apache/tvm/pull/19491) - [Frontend][TFLite] Add segment operator mappings
 * [#19499](https://github.com/apache/tvm/pull/19499) - [Frontend][TFLite] Add tests coverage for SPACE_TO_BATCH_ND and BATCH_TO_SPACE_ND
 * [#19516](https://github.com/apache/tvm/pull/19516) - [TFLite] Add gather frontend expected IRModule tests
 * [#19488](https://github.com/apache/tvm/pull/19488) - [PyTorch] Fix segfault in from_exported_program when model uses index_put_ with tuple output
 * [#19523](https://github.com/apache/tvm/pull/19523) - [Frontend][TFLite] Add Conv3D support
 * [#19525](https://github.com/apache/tvm/pull/19525) - [ONNX] Normalize negative indices before the take call for `Gather` operator
 * [#19530](https://github.com/apache/tvm/pull/19530) - [Frontend] Add TFLite Frontend Support for CONV_3D_TRANSPOSE
 * [#19536](https://github.com/apache/tvm/pull/19536) - [Frontend][TFLite] Add initial StableHLO builtin operator support
 * [#19547](https://github.com/apache/tvm/pull/19547) - [ONNX] Set `max_output_boxes_per_class` default value to 0 for NonMaxSuppression
 * [#19515](https://github.com/apache/tvm/pull/19515) - [ONNX] Add ONNX Backend Tests for systematic frontend coverage
 * [#19566](https://github.com/apache/tvm/pull/19566) - [ONNX] Prevent `Div` divide-by-zero crashes
 * [#19573](https://github.com/apache/tvm/pull/19573) - [ONNX] Fix TopK scalar K extraction in from_onnx
 * [#19587](https://github.com/apache/tvm/pull/19587) - [Frontend][TFLite] Support StableHLO region-based ops and multi-subgraph models
 * [#19588](https://github.com/apache/tvm/pull/19588) - Normalize negative concat axis in ReorderPermuteDimsAfterConcat
 * [#19603](https://github.com/apache/tvm/pull/19603) - [REFACTOR]Fold CalleeCollector into relax DeadCodeElimination
 * [#19538](https://github.com/apache/tvm/pull/19538) - [Frontend][TFLite] Support quantized TFLite import via QDQ decomposition
 * [#19616](https://github.com/apache/tvm/pull/19616) - [Frontend][TFLite] Support control-flow multi-subgraph operators
 * [#19601](https://github.com/apache/tvm/pull/19601) - [Frontend][TFLite] Add UNIDIRECTIONAL_SEQUENCE_RNN converter
 * [#19637](https://github.com/apache/tvm/pull/19637) - [Frontend][TFLite] Add REDUCE_WINDOW support
 * [#19632](https://github.com/apache/tvm/pull/19632) - [Frontend][TFLite] Add RNN converter
 * [#19633](https://github.com/apache/tvm/pull/19633) - [Frontend][TFLite] Add LSTM and SVDF converter
 * [#19639](https://github.com/apache/tvm/pull/19639) - [Frontend][TFLite] Add TFLite Resource Variable and Static Hashtable Import Support
 * [#19634](https://github.com/apache/tvm/pull/19634) - [Frontend][TFLite] Support sequence LSTM and RNN operators
 * [#19646](https://github.com/apache/tvm/pull/19646) - [Frontend][TFLite] Support STABLEHLO_WHILE
 * [#19644](https://github.com/apache/tvm/pull/19644) - [IR] Skip in-place multiply when two operands are views of the same tensor
 * [#19649](https://github.com/apache/tvm/pull/19649) - [Frontend][TFLite] Support STABLEHLO_CUSTOM_CALL
 * [#19654](https://github.com/apache/tvm/pull/19654) - [Frontend][TFLite] Add HASHTABLE_LOOKUP converter
 * [#19651](https://github.com/apache/tvm/pull/19651) - [Frontend][TFLite] Support STABLEHLO_RNG_BIT_GENERATOR
 * [#19645](https://github.com/apache/tvm/pull/19645) - [PyTorch] Cast non-bool inputs to bool in logical_not converter
 * [#19652](https://github.com/apache/tvm/pull/19652) - [Frontend][TFLite] Add EMBEDDING_LOOKUP_SPARSE converter
 * [#19660](https://github.com/apache/tvm/pull/19660) - [PyTorch] Decompose integer pow into repeated multiplication
 * [#19626](https://github.com/apache/tvm/pull/19626) - [ONNX] Fix Cast operator float->int NaN/Inf handling
 * [#19674](https://github.com/apache/tvm/pull/19674) - [ONNX] Preserve NaN in Sign to align with ONNX Runtime
 * [#19679](https://github.com/apache/tvm/pull/19679) - [PyTorch] Cast non-bool inputs to bool in logical_and converter
 * [#19711](https://github.com/apache/tvm/pull/19711) - [CoreML] Fix CoreML partition pass
 * [#19732](https://github.com/apache/tvm/pull/19732) - [PyTorch][DLight] Fix exported-program CUDA test failures
 * [#19756](https://github.com/apache/tvm/pull/19756) - [PyTorch] Add logical_or and logical_xor converters
 * [#19772](https://github.com/apache/tvm/pull/19772) - [ONNX] Fix LayerNormalization no-bias zero tensor shape and dtype
 * [#19773](https://github.com/apache/tvm/pull/19773) - [ONNX] Support exclusive option in CumSum
 * [#19755](https://github.com/apache/tvm/pull/19755) - [ONNX] Make ReduceMax/ReduceMin NaN propagation order-independent(numpy semantics)
 * [#19789](https://github.com/apache/tvm/pull/19789) - [TensorRT] Update TensorRT runtime to 10
 * [#19763](https://github.com/apache/tvm/pull/19763) - [Frontend][TFLite] Add support for FFT/complex operators: REAL, IMAG, COMPLEX_ABS

### Runtime
 * [#19617](https://github.com/apache/tvm/pull/19617) - [CMAKE]Link tvm_rpc with all backend runtime libraries
 * [#19620](https://github.com/apache/tvm/pull/19620) - [REFACTOR]Phase out tvm::runtime::regex_match
 * [#19622](https://github.com/apache/tvm/pull/19622) - [REFACTOR]Remove leftover microTVM/CRT crumbs
 * [#19621](https://github.com/apache/tvm/pull/19621) - [REFACTOR]Relocate nvtx.h to tvm/support/cuda and make it header-only
 * [#19628](https://github.com/apache/tvm/pull/19628) - [REFACTOR]Structural reorganization: locality moves for thread_map, texture, minrpc, disco, contrib
 * [#19714](https://github.com/apache/tvm/pull/19714) - [Tests] Fix contrib wheel tests
 * [#19736](https://github.com/apache/tvm/pull/19736) - [Disco] Fix session attribute storage, NVSHMEM build, and test gating
 * [#19748](https://github.com/apache/tvm/pull/19748) - [Tests] Drop int4 from random_fill test, fix dtype error message
 * [#19762](https://github.com/apache/tvm/pull/19762) - [CoreML] Fix FFI casts in CoreML runtime

### TIR
 * [#19581](https://github.com/apache/tvm/pull/19581) - [TIRx] Bringup TIRx Infrastructure
 * [#19642](https://github.com/apache/tvm/pull/19642) - [TIRx] Fix stale Simplify import in lowering test
 * [#19657](https://github.com/apache/tvm/pull/19657) - [TIRx] Post-bringup op-dispatch / codegen / TVMScript follow-ups
 * [#19663](https://github.com/apache/tvm/pull/19663) - [REFACTOR][TIRX] Consolidate split host device stages
 * [#19677](https://github.com/apache/tvm/pull/19677) - [TIRx] Update scoped ops and CUDA launch bounds
 * [#19728](https://github.com/apache/tvm/pull/19728) - [TIRx] Preserve Triton call_kernel compile options
 * [#19739](https://github.com/apache/tvm/pull/19739) - [TIRx] Use canonical PTX async script API in s_tir test
 * [#19753](https://github.com/apache/tvm/pull/19753) - [TIRX][Tests] Fix LLVM version gate for vectorized lround
 * [#19757](https://github.com/apache/tvm/pull/19757) - [TIRx] Post-bringup follow-ups: op-dispatch, namespaces, launch bounds, gemm-async, backend reorg
 * [#19785](https://github.com/apache/tvm/pull/19785) - [TIRX][CUDA] Framework support for FA4, CLC intrinsics, and nvfp4 tcgen05 GEMM
 * [#19776](https://github.com/apache/tvm/pull/19776) - [TIRx][RISC-V] Use scalable RVV loops for fixed vectorize
 * [#19797](https://github.com/apache/tvm/pull/19797) - [REFACTOR][TIRX] Add IntImm common scalar ctor and streamline MakeConst

### TVMScript
 * [#19583](https://github.com/apache/tvm/pull/19583) - Handle undefined functions when dumping IRModule

### cuda & cutlass & tensorrt
 * [#19565](https://github.com/apache/tvm/pull/19565) - [RFC][CodeGen][CUDA]: Gate fast math intrinsic lowering behind target option
 * [#19596](https://github.com/apache/tvm/pull/19596) - [CodeGen][CUDA] Move fast math intrinsic lowering option to PassContext
 * [#19741](https://github.com/apache/tvm/pull/19741) - [S-TIR][CUDA] Fix legacy predicated cp.async zero fill
 * [#19768](https://github.com/apache/tvm/pull/19768) - [REFACTOR][CUDA] Phase out l2 cache flush preproc test
 * [#19770](https://github.com/apache/tvm/pull/19770) - [REFACTOR][CUDA] Phase out cuda_common.h
 * [#19784](https://github.com/apache/tvm/pull/19784) - [CUDA] Narrow the cuda extra from cuda-python to cuda-bindings

### web
 * [#19494](https://github.com/apache/tvm/pull/19494) - Add support for OPFS
 * [#19569](https://github.com/apache/tvm/pull/19569) - [COS] Persist URL→hash mapping across page loads
 * [#19673](https://github.com/apache/tvm/pull/19673) - Add support for OPFS synchronous access handles and committed records
 * [#19687](https://github.com/apache/tvm/pull/19687) - Bump tvmjs version to 0.25.0-dev1
 * [#19790](https://github.com/apache/tvm/pull/19790) - Destroy GPUDevice once on buffer creation error
 * [#19780](https://github.com/apache/tvm/pull/19780) - use singular requestFileHandle() instead of requestFileHandles()

### Misc
 * [#19446](https://github.com/apache/tvm/pull/19446) - [release][Dont Squash] Update version to 0.24.0 and 0.25.0.dev on main branch
 * [#19528](https://github.com/apache/tvm/pull/19528) - [REFACTOR][IR] Remove dead AttrFunctor template
 * [#19423](https://github.com/apache/tvm/pull/19423) - [TIR] Add cooperative_tensor builtins and metal.cooperative_tensor storage scope
 * [#19539](https://github.com/apache/tvm/pull/19539) - [Contrib] Fix CUDA contrib build after FFI/header cleanups
 * [#19594](https://github.com/apache/tvm/pull/19594) - [BUILD] Modularize device runtime into per-backend DSOs
 * [#19586](https://github.com/apache/tvm/pull/19586) - [RPC][Tracker] Bound msg_size to MAX_TRACKER_MSG_BYTES to prevent unbounded buffer growth
 * [#19597](https://github.com/apache/tvm/pull/19597) - [IR] Add annotations to Call nodes
 * [#19602](https://github.com/apache/tvm/pull/19602) - Fix PytestUnknownMarkWarning: Unknown pytest.mark.adreno_clml
 * [#19607](https://github.com/apache/tvm/pull/19607) - [REFACTOR][IR] Cleanup attrs.h: drop NullValue, AttrsNodeReflAdapter, legacy BaseAttrsNode methods
 * [#19611](https://github.com/apache/tvm/pull/19611) - [REFACTOR] Move src/ir/script_printer.cc to src/script/printer/
 * [#19613](https://github.com/apache/tvm/pull/19613) - [REFACTOR][IR] Phase out src/ir/structural_{hash,equal}.cc to tvm-ffi
 * [#19612](https://github.com/apache/tvm/pull/19612) - [REFACTOR][IR] Inline ApplyPassToFunction into relax decompose_ops, delete the util
 * [#19614](https://github.com/apache/tvm/pull/19614) - [REFACTOR][IR] Phase out class Integer and class Bool in Attrs and PassConfig
 * [#19615](https://github.com/apache/tvm/pull/19615) - [REFACTOR][IR] attrs.h follow-up cleanup: drop legacy vtable / rename / phase out AttrFieldInfo
 * [#19605](https://github.com/apache/tvm/pull/19605) - [REFACTOR][TIR] Tie AnnotateDeviceRegions/SplitHostDevice/LowerDeviceKernelLaunch together
 * [#19618](https://github.com/apache/tvm/pull/19618) - [IR] Rename Call annotations to attrs
 * [#19624](https://github.com/apache/tvm/pull/19624) - [REFACTOR][PYTHON] Lift compiler/CLI/process modules from tvm.contrib to tvm.support
 * [#19627](https://github.com/apache/tvm/pull/19627) - [REFACTOR][IR][FFI] Bump tvm-ffi (+ SEqHashDef migration) and phase out tvm/ir/repr.h
 * [#19625](https://github.com/apache/tvm/pull/19625) - [REFACTOR][IR] Inline ReplaceGlobalVars into AttachGlobalSymbol
 * [#19630](https://github.com/apache/tvm/pull/19630) - [REFACTOR][PYTHON] Consolidate derived_object into tvm.ir.utils
 * [#19631](https://github.com/apache/tvm/pull/19631) - [REFACTOR][SCRIPT] tvmscript streamline: lift printer.h, restore one-way dep, migrate dialect config to extra_config
 * [#19636](https://github.com/apache/tvm/pull/19636) - [REFACTOR][IR] Delete class Bool and class Integer boxed-type wrappers
 * [#19653](https://github.com/apache/tvm/pull/19653) - [REFACTOR][PYTHON] Revisit lifted support modules from tvm.contrib
 * [#19648](https://github.com/apache/tvm/pull/19648) - fix: Security Patch: Fix missing exported flag in AndroidManifest
 * [#19658](https://github.com/apache/tvm/pull/19658) - [RPC] Import tvm.testing lazily in rpc.testing
 * [#19662](https://github.com/apache/tvm/pull/19662) - [FFI][IR] Route JSON serialization through tvm-ffi
 * [#19661](https://github.com/apache/tvm/pull/19661) - [FFI][REFACTOR] Direct structural APIs to tvm-ffi
 * [#19681](https://github.com/apache/tvm/pull/19681) - [Bump] tvm-ffi to 59da4c0
 * [#19684](https://github.com/apache/tvm/pull/19684) - [RELEASE] Bump web npm version to 0.25.0
 * [#19701](https://github.com/apache/tvm/pull/19701) - [Python] Bump apache-tvm-ffi floor to >=0.1.12 on v0.25.0
 * [#19709](https://github.com/apache/tvm/pull/19709) - [Refactor][Meta-schedule] Remove meta-schedule as_string mechanism in favor of default representation
 * [#19719](https://github.com/apache/tvm/pull/19719) - [REFACTOR][PYTHON] Slim tvm.libinfo to info-only helpers
 * [#19717](https://github.com/apache/tvm/pull/19717) - [Codegen][NVPTX] Skip runtime execution in Vulkan codegen tests
 * [#19721](https://github.com/apache/tvm/pull/19721) - [REFACTOR][PYTHON] Remove tvm.ffi shim; import tvm_ffi directly
 * [#19722](https://github.com/apache/tvm/pull/19722) - [REFACTOR][IR] Phase out diagnostic.h for visit-context-aware pass errors
 * [#19723](https://github.com/apache/tvm/pull/19723) - [Python] Refactor pyproject.toml dependencies
 * [#19727](https://github.com/apache/tvm/pull/19727) - [PYTHON] Autoload backends; simplify library loading; remove TVMError for native errors
 * [#19742](https://github.com/apache/tvm/pull/19742) - [S-TIR] Fix software pipeline offsets for legacy MMA intrinsics
 * [#19758](https://github.com/apache/tvm/pull/19758) - [REFACTOR][VM] Move CUDA graph VM builtin back under VM runtime
 * [#19760](https://github.com/apache/tvm/pull/19760) - [REFACTOR][DataType] Phase out target custom datatype support
 * [#19759](https://github.com/apache/tvm/pull/19759) - [REFACTOR][TARGET] Cleanup backend target registration
 * [#19767](https://github.com/apache/tvm/pull/19767) - [MetaScheduler] Improve print info about builder/runner state
 * [#19778](https://github.com/apache/tvm/pull/19778) - [CPP_RPC] Bugfix race conditions and enhance print infos
 * [#19734](https://github.com/apache/tvm/pull/19734) - [CMAKE] Upgrade TVM build baseline to C++20
 * [#19769](https://github.com/apache/tvm/pull/19769) - [REFACTOR][PYTHON] Consolidate backend autoload infra
 * [#19781](https://github.com/apache/tvm/pull/19781) - [REFACTOR][IR] Cleanup IR naming utilities
 * [#19783](https://github.com/apache/tvm/pull/19783) - [AGENT] Migrate agent instructions to vendor-neutral layout
 * [#19794](https://github.com/apache/tvm/pull/19794) - [REFACTOR] Phase out unused queue and rang license entries
 * [#19799](https://github.com/apache/tvm/pull/19799) - [REFACTOR][IR] Simplify CallingConv attribute access
 * [#19805](https://github.com/apache/tvm/pull/19805) - [CMAKE] Revert build baseline to C++17


## v0.26.0.rc0 (2026-08-05)

## What's Changed
* [release][Dont Squash] Update version to 0.24.0 and 0.25.0.dev on main branch by @ysh329 in https://github.com/apache/tvm/pull/19446
* [Relax][Frontend] Add ParameterList and ParameterDict containers by @mshr-h in https://github.com/apache/tvm/pull/19495
* [Relax][Frontend][TFLite] Add segment operator mappings by @Aharrypotter in https://github.com/apache/tvm/pull/19491
* [BUGFIX][TIR] Skip bool-typed expressions in CSE by @tqchen in https://github.com/apache/tvm/pull/19502
* [Relax][Frontend][TFLite] Add tests coverage for SPACE_TO_BATCH_ND and BATCH_TO_SPACE_ND by @rknastenka in https://github.com/apache/tvm/pull/19499
* [BugFix][Relax] Fix scatter_elements and scatter_nd CUDA compilation by @as4230 in https://github.com/apache/tvm/pull/19497
* [BugFix][Relax][ONNX] Resolve param Vars in Concat to handle mixed Shape/Tensor inputs by @swjng in https://github.com/apache/tvm/pull/19498
* [Web] Add support for OPFS by @akaashrp in https://github.com/apache/tvm/pull/19494
* [BugFix][Relax][Torch] Honor multi-axis dims in torch.flip converter by @swjng in https://github.com/apache/tvm/pull/19511
* [BugFix][Relax][Torch] Honor `correction` in std/var converter by @swjng in https://github.com/apache/tvm/pull/19512
* [BugFix][S-TIR] Wrap bare scalar bodies in DefaultGPUSchedule to avoid root-block crash by @swjng in https://github.com/apache/tvm/pull/19514
* [Relax][TFLite] Add gather frontend expected IRModule tests by @weicheng-hsu in https://github.com/apache/tvm/pull/19516
* [Relax][PyTorch] Fix segfault in from_exported_program when model uses index_put_ with tuple output by @cchung100m in https://github.com/apache/tvm/pull/19488
* [Relax][Frontend][TFLite] Add Conv3D support by @weicheng-hsu in https://github.com/apache/tvm/pull/19523
* [REFACTOR][IR] Remove dead AttrFunctor template by @tqchen in https://github.com/apache/tvm/pull/19528
* [Relax][ONNX] Normalize negative indices before the take call for `Gather` operator by @cchung100m in https://github.com/apache/tvm/pull/19525
* [Relax][Frontend] Add TFLite Frontend Support for CONV_3D_TRANSPOSE by @weicheng-hsu in https://github.com/apache/tvm/pull/19530
* [TIR] Add cooperative_tensor builtins and metal.cooperative_tensor storage scope by @oraluben in https://github.com/apache/tvm/pull/19423
* [Relax][Frontend][TFLite] Add initial StableHLO builtin operator support by @Aharrypotter in https://github.com/apache/tvm/pull/19536
* [Contrib] Fix CUDA contrib build after FFI/header cleanups by @MasterJH5574 in https://github.com/apache/tvm/pull/19539
* [BugFix][Relax]: handle ONNX ScatterElements reduction by @THINKER-ONLY in https://github.com/apache/tvm/pull/19527
* [Fix][Relax]: ONNX Clip NaN bounds and preserve input NaN (ORT parity) by @ConvolutedDog in https://github.com/apache/tvm/pull/19535
* [Fix][CI]: remove astral-sh/setup-uv from lint workflow by @ConvolutedDog in https://github.com/apache/tvm/pull/19554
* [Relax][ONNX] Set `max_output_boxes_per_class` default value to 0 for NonMaxSuppression by @cchung100m in https://github.com/apache/tvm/pull/19547
* [Relax][ONNX] Add ONNX Backend Tests for systematic frontend coverage by @Aharrypotter in https://github.com/apache/tvm/pull/19515
* [Fix][Relax] Lower bool prod as logical all by @ConvolutedDog in https://github.com/apache/tvm/pull/19557
* [Relax][ONNX] Prevent `Div` divide-by-zero crashes by @cchung100m in https://github.com/apache/tvm/pull/19566
* [TIRx] Bringup TIRx Infrastructure by @spectrometerHBH in https://github.com/apache/tvm/pull/19581
* [BugFix][Target][LLVM] Use libm for asin/acos instead of buggy inline Taylor by @swjng in https://github.com/apache/tvm/pull/19567
* [RFC][CodeGen][CUDA]: Gate fast math intrinsic lowering behind target option by @ConvolutedDog in https://github.com/apache/tvm/pull/19565
* [TVMScript] Handle undefined functions when dumping IRModule by @ConvolutedDog in https://github.com/apache/tvm/pull/19583
* [BugFix][Target][LLVM] Route sinh/cosh/atan/asinh/erf through libm extern by @swjng in https://github.com/apache/tvm/pull/19568
* [Relax][ONNX] Fix TopK scalar K extraction in from_onnx by @javierdejesusda in https://github.com/apache/tvm/pull/19573
* [Relax][Frontend][TFLite] Support StableHLO region-based ops and multi-subgraph models by @Aharrypotter in https://github.com/apache/tvm/pull/19587
* [ONNX] Add RMSNormalization converter for ONNX opset 23 by @q55180514 in https://github.com/apache/tvm/pull/19590
* [BUILD] Modularize device runtime into per-backend DSOs by @tqchen in https://github.com/apache/tvm/pull/19594
* [Relax] Normalize negative concat axis in ReorderPermuteDimsAfterConcat by @cchung100m in https://github.com/apache/tvm/pull/19588
* [RPC][Tracker] Bound msg_size to MAX_TRACKER_MSG_BYTES to prevent unbounded buffer growth by @bl4cksku11 in https://github.com/apache/tvm/pull/19586
* [CodeGen][CUDA] Move fast math intrinsic lowering option to PassContext by @tlopex in https://github.com/apache/tvm/pull/19596
* [IR] Add annotations to Call nodes by @tlopex in https://github.com/apache/tvm/pull/19597
* [REFACTOR][RELAX] Fold CalleeCollector into relax DeadCodeElimination by @tqchen in https://github.com/apache/tvm/pull/19603
* [Relax][Frontend][TFLite] Support quantized TFLite import via QDQ decomposition by @Aharrypotter in https://github.com/apache/tvm/pull/19538
* Fix PytestUnknownMarkWarning: Unknown pytest.mark.adreno_clml by @cchung100m in https://github.com/apache/tvm/pull/19602
* [REFACTOR][IR] Cleanup attrs.h: drop NullValue, AttrsNodeReflAdapter, legacy BaseAttrsNode methods by @tqchen in https://github.com/apache/tvm/pull/19607
* [Docs] Reorganize development guide content by @tlopex in https://github.com/apache/tvm/pull/19606
* [REFACTOR] Move src/ir/script_printer.cc to src/script/printer/ by @tqchen in https://github.com/apache/tvm/pull/19611
* [REFACTOR][IR] Phase out src/ir/structural_{hash,equal}.cc to tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/19613
* [REFACTOR][IR] Inline ApplyPassToFunction into relax decompose_ops, delete the util by @tqchen in https://github.com/apache/tvm/pull/19612
* [REFACTOR][TIR][ARITH] Phase out ControlFlowGraph, NarrowPredicateExpression, and rename Simplify to StmtSimplify by @tqchen in https://github.com/apache/tvm/pull/19604
* [REFACTOR][IR] Phase out class Integer and class Bool in Attrs and PassConfig by @tqchen in https://github.com/apache/tvm/pull/19614
* [CMAKE][RUNTIME] Link tvm_rpc with all backend runtime libraries by @cbalint13 in https://github.com/apache/tvm/pull/19617
* [REFACTOR][IR] attrs.h follow-up cleanup: drop legacy vtable / rename / phase out AttrFieldInfo by @tqchen in https://github.com/apache/tvm/pull/19615
* [REFACTOR][TIR] Tie AnnotateDeviceRegions/SplitHostDevice/LowerDeviceKernelLaunch together by @tqchen in https://github.com/apache/tvm/pull/19605
* [Relax][Frontend][TFLite] Support control-flow multi-subgraph operators by @Aharrypotter in https://github.com/apache/tvm/pull/19616
* [Relax][Frontend][TFLite] Add UNIDIRECTIONAL_SEQUENCE_RNN converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19601
* [IR] Rename Call annotations to attrs by @tlopex in https://github.com/apache/tvm/pull/19618
* [REFACTOR][RUNTIME] Phase out tvm::runtime::regex_match by @tqchen in https://github.com/apache/tvm/pull/19620
* [REFACTOR][RUNTIME] Remove leftover microTVM/CRT crumbs by @tqchen in https://github.com/apache/tvm/pull/19622
* [REFACTOR][RUNTIME] Relocate nvtx.h to tvm/support/cuda and make it header-only by @tqchen in https://github.com/apache/tvm/pull/19621
* [REFACTOR][PYTHON] Lift compiler/CLI/process modules from tvm.contrib to tvm.support by @tqchen in https://github.com/apache/tvm/pull/19624
* [REFACTOR][IR][FFI] Bump tvm-ffi (+ SEqHashDef migration) and phase out tvm/ir/repr.h by @tqchen in https://github.com/apache/tvm/pull/19627
* [REFACTOR][IR] Inline ReplaceGlobalVars into AttachGlobalSymbol by @tqchen in https://github.com/apache/tvm/pull/19625
* [BugFix][Vulkan][CodeGen] Change OpControlBarrier to AcquireRelease by @kistenklaus in https://github.com/apache/tvm/pull/19619
* [REFACTOR][RUNTIME] Structural reorganization: locality moves for thread_map, texture, minrpc, disco, contrib by @tqchen in https://github.com/apache/tvm/pull/19628
* [REFACTOR][PYTHON] Consolidate derived_object into tvm.ir.utils by @tqchen in https://github.com/apache/tvm/pull/19630
* [CI] Remove tvm-lint from tvm-bot by @yongwww in https://github.com/apache/tvm/pull/19629
* [REFACTOR][SCRIPT] tvmscript streamline: lift printer.h, restore one-way dep, migrate dialect config to extra_config by @tqchen in https://github.com/apache/tvm/pull/19631
* [REFACTOR][ARITH] Phase out arith/scalable_expression; arith no longer proves over scalable vectors by @tqchen in https://github.com/apache/tvm/pull/19638
* [Relax][Frontend][TFLite] Add REDUCE_WINDOW support by @THINKER-ONLY in https://github.com/apache/tvm/pull/19637
* [Relax][Frontend][TFLite] Add RNN converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19632
* [REFACTOR][IR] Delete class Bool and class Integer boxed-type wrappers by @tqchen in https://github.com/apache/tvm/pull/19636
* [Relax][Frontend][TFLite] Add LSTM and SVDF converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19633
* [Relax][Frontend][TFLite] Add TFLite Resource Variable and Static Hashtable Import Support by @Aharrypotter in https://github.com/apache/tvm/pull/19639
* [TIRx] Fix stale Simplify import in lowering test by @tlopex in https://github.com/apache/tvm/pull/19642
* [Relax][Frontend][TFLite] Support sequence LSTM and RNN operators by @LudovicoYIN in https://github.com/apache/tvm/pull/19634
* [Relax][Frontend][TFLite] Support STABLEHLO_WHILE by @Aharrypotter in https://github.com/apache/tvm/pull/19646
* [Fix] Stabilize layer_norm variance computation with two-pass reduction by @ConvolutedDog in https://github.com/apache/tvm/pull/19643
* [Relax][IR] Skip in-place multiply when two operands are views of the same tensor by @ConvolutedDog in https://github.com/apache/tvm/pull/19644
* [Relax][Frontend][TFLite] Support STABLEHLO_CUSTOM_CALL by @Aharrypotter in https://github.com/apache/tvm/pull/19649
* [REFACTOR][PYTHON] Revisit lifted support modules from tvm.contrib by @cbalint13 in https://github.com/apache/tvm/pull/19653
* [Relax][Frontend][TFLite] Add HASHTABLE_LOOKUP converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19654
* [Relax][Frontend][TFLite] Support STABLEHLO_RNG_BIT_GENERATOR by @Aharrypotter in https://github.com/apache/tvm/pull/19651
* fix: Security Patch: Fix missing exported flag in AndroidManifest by @CodeMechanic-Bot in https://github.com/apache/tvm/pull/19648
* [Relax][PyTorch] Cast non-bool inputs to bool in logical_not converter by @javierdejesusda in https://github.com/apache/tvm/pull/19645
* [Web][COS] Persist URL→hash mapping across page loads by @tomayac in https://github.com/apache/tvm/pull/19569
* [Fix][Relax] Support ND batched matmul chains in AdjustMatmulOrder pass by @ConvolutedDog in https://github.com/apache/tvm/pull/19650
* [Relax][Frontend][TFLite] Add EMBEDDING_LOOKUP_SPARSE converter by @LudovicoYIN in https://github.com/apache/tvm/pull/19652
* [CI] Add cibw-based wheel publishing to PyPI by @tlopex in https://github.com/apache/tvm/pull/19656
* [TIRx] Post-bringup op-dispatch / codegen / TVMScript follow-ups by @spectrometerHBH in https://github.com/apache/tvm/pull/19657
* [RPC] Import tvm.testing lazily in rpc.testing by @tlopex in https://github.com/apache/tvm/pull/19658
* [CI] Wheel publishing follow-ups by @tlopex in https://github.com/apache/tvm/pull/19659
* [REFACTOR][TIRX] Consolidate split host device stages by @tqchen in https://github.com/apache/tvm/pull/19663
* [FFI][IR] Route JSON serialization through tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/19662
* [Relax][PyTorch] Decompose integer pow into repeated multiplication by @javierdejesusda in https://github.com/apache/tvm/pull/19660
* [CI] Derive the version from Git tags via setuptools_scm by @tlopex in https://github.com/apache/tvm/pull/19665
* [CI] Reformat the macOS repair-wheel-command as a multiline script by @tlopex in https://github.com/apache/tvm/pull/19664
* [FFI][REFACTOR] Direct structural APIs to tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/19661
* [Arith] Memoize IntervalSet variable relaxation to avoid exponential blowup by @jinhongyii in https://github.com/apache/tvm/pull/19670
* [Arith] Gate canonical-simplify LT Case 2 on extra scale == +1 by @jinhongyii in https://github.com/apache/tvm/pull/19669
* [Relax][ONNX] Fix Cast operator float->int NaN/Inf handling by @cchung100m in https://github.com/apache/tvm/pull/19626
* [TIRx] Update scoped ops and CUDA launch bounds by @spectrometerHBH in https://github.com/apache/tvm/pull/19677
* [Relax][ONNX] Preserve NaN in Sign to align with ONNX Runtime by @cchung100m in https://github.com/apache/tvm/pull/19674
* [Bump] tvm-ffi to 59da4c0 by @tqchen in https://github.com/apache/tvm/pull/19681
* [Web] Add support for OPFS synchronous access handles and committed records by @akaashrp in https://github.com/apache/tvm/pull/19673
* [Arith] Make Analyzer a tvm-ffi Object by @tlopex in https://github.com/apache/tvm/pull/19675
* [Relax][PyTorch] Cast non-bool inputs to bool in logical_and converter by @javierdejesusda in https://github.com/apache/tvm/pull/19679
* [CI] Remove PyPI-only tag ref guard from wheel publishing by @tlopex in https://github.com/apache/tvm/pull/19685
* [CI] Target apache-tvm for PyPI wheel publishing by @tlopex in https://github.com/apache/tvm/pull/19686
* [Web] Bump tvmjs version to 0.25.0-dev1 by @akaashrp in https://github.com/apache/tvm/pull/19687
* [Fix] CommReduce could handle 0-dim data by @flashmouse in https://github.com/apache/tvm/pull/19683
* [CI] Pin actions by version tag, trim wheel perms by @MasterJH5574 in https://github.com/apache/tvm/pull/19703
* [Tests] Fix s_tir tests using removed T.block API in TIRx script by @tlopex in https://github.com/apache/tvm/pull/19706
* [CI] Fix release verification script by @MasterJH5574 in https://github.com/apache/tvm/pull/19700
* [Refactor][Meta-schedule] Remove meta-schedule as_string mechanism in favor of default representation by @tlopex in https://github.com/apache/tvm/pull/19709
* [Python] Bump apache-tvm-ffi floor to >=0.1.12 by @MasterJH5574 in https://github.com/apache/tvm/pull/19710
* [Relax][CoreML] Fix CoreML partition pass by @tlopex in https://github.com/apache/tvm/pull/19711
* [Tests] Skip test modules cleanly when optional deps are missing by @tlopex in https://github.com/apache/tvm/pull/19704
* [CI] Merge PR against its target branch instead of main by @MasterJH5574 in https://github.com/apache/tvm/pull/19712
* [CI] Fix CI script test subprocess environment by @tlopex in https://github.com/apache/tvm/pull/19713
* [Codegen][LLVM] Accept splat form in VLA broadcast test by @tlopex in https://github.com/apache/tvm/pull/19716
* [DOCS] Clarify loading serialized artifacts requires a trusted source by @tqchen in https://github.com/apache/tvm/pull/19720
* [REFACTOR][PYTHON] Slim tvm.libinfo to info-only helpers by @tqchen in https://github.com/apache/tvm/pull/19719
* [Codegen][NVPTX] Skip runtime execution in Vulkan codegen tests by @tlopex in https://github.com/apache/tvm/pull/19717
* [REFACTOR][PYTHON] Remove tvm.ffi shim; import tvm_ffi directly by @tqchen in https://github.com/apache/tvm/pull/19721
* [Runtime][Tests] Fix contrib wheel tests by @tlopex in https://github.com/apache/tvm/pull/19714
* [Tests][Disco] Skip CCL tests when runtime support is absent by @tlopex in https://github.com/apache/tvm/pull/19724
* [Tests][Relax] Gate multi-GPU VM test on three devices by @tlopex in https://github.com/apache/tvm/pull/19725
* [REFACTOR][IR] Phase out diagnostic.h for visit-context-aware pass errors by @tqchen in https://github.com/apache/tvm/pull/19722
* [Tests][Hexagon] Lazily import pytest plugin dependencies by @tlopex in https://github.com/apache/tvm/pull/19726
* [Python] Refactor pyproject.toml dependencies by @tlopex in https://github.com/apache/tvm/pull/19723
* [Tests][NNAPI] Skip tests cleanly when remote environment is unavailable by @tlopex in https://github.com/apache/tvm/pull/19730
* [Tests][S-TIR] Fix stale MetaSchedule sketch expectations and migrate let binds to T.let by @tlopex in https://github.com/apache/tvm/pull/19729
* [Tests] Remove test_runtime_ndarray (covered by tvm-ffi) by @tlopex in https://github.com/apache/tvm/pull/19715
* [TIRx] Preserve Triton call_kernel compile options by @tlopex in https://github.com/apache/tvm/pull/19728
* [Relax][PyTorch][DLight] Fix exported-program CUDA test failures by @tlopex in https://github.com/apache/tvm/pull/19732
* [PYTHON] Autoload backends; simplify library loading; remove TVMError for native errors by @tqchen in https://github.com/apache/tvm/pull/19727
* [Script][Tests] Fix dialect redirect module re-execution and stray category-less tirx.intrin_test op by @tlopex in https://github.com/apache/tvm/pull/19731
* [S-TIR][Tests] Fix transform test failures after TIRx bringup by @tlopex in https://github.com/apache/tvm/pull/19735
* [TIRx] Use canonical PTX async script API in s_tir test by @tlopex in https://github.com/apache/tvm/pull/19739
* [Tests] Check WebGPU volatile allreduce annotation structurally by @tlopex in https://github.com/apache/tvm/pull/19740
* [S-TIR] Fix software pipeline offsets for legacy MMA intrinsics by @tlopex in https://github.com/apache/tvm/pull/19742
* [Tests] Fix flaky popen pool executor test by @tlopex in https://github.com/apache/tvm/pull/19746
* [Hexagon][Tests] Clean up stale hexagon tests by @tlopex in https://github.com/apache/tvm/pull/19747
* [Runtime][Disco] Fix session attribute storage, NVSHMEM build, and test gating by @tlopex in https://github.com/apache/tvm/pull/19736
* [CI] Align cuda-python with PyTorch cuda-bindings by @tlopex in https://github.com/apache/tvm/pull/19738
* [Codegen][LLVM][Tests] Gate +v9a vscale_range expectation on LLVM version by @tlopex in https://github.com/apache/tvm/pull/19744
* [Runtime][Tests] Drop int4 from random_fill test, fix dtype error message by @tlopex in https://github.com/apache/tvm/pull/19748
* [Tests][LLVM] Gate stepvector intrinsic rename on LLVM 20 by @tlopex in https://github.com/apache/tvm/pull/19745
* [S-TIR][Tests] Mark test_cp_async_in_if_then_else as xfail by @tlopex in https://github.com/apache/tvm/pull/19751
* [CI] Run s_tir/transform tests in the python-unittest stage by @tlopex in https://github.com/apache/tvm/pull/19737
* [CI] Updated cibw to 4.1.0 by @tlopex in https://github.com/apache/tvm/pull/19754
* [TIRX][Tests] Fix LLVM version gate for vectorized lround by @tlopex in https://github.com/apache/tvm/pull/19753
* [S-TIR][CUDA] Fix legacy predicated cp.async zero fill by @tlopex in https://github.com/apache/tvm/pull/19741
* [Tests][AArch64] Make SVE codegen assertions robust across LLVM versions by @tlopex in https://github.com/apache/tvm/pull/19752
* [Relax][PyTorch] Add logical_or and logical_xor converters by @javierdejesusda in https://github.com/apache/tvm/pull/19756
* [TIRx] Post-bringup follow-ups: op-dispatch, namespaces, launch bounds, gemm-async, backend reorg by @spectrometerHBH in https://github.com/apache/tvm/pull/19757
* [REFACTOR][VM] Move CUDA graph VM builtin back under VM runtime by @tqchen in https://github.com/apache/tvm/pull/19758
* [Runtime][CoreML] Fix FFI casts in CoreML runtime by @tlopex in https://github.com/apache/tvm/pull/19762
* [CI] Drop redundant cmake/ninja install from the Linux wheel CUDA sidecar by @tlopex in https://github.com/apache/tvm/pull/19761
* [REFACTOR][DataType] Phase out target custom datatype support by @tqchen in https://github.com/apache/tvm/pull/19760
* [REFACTOR][TARGET] Cleanup backend target registration by @tqchen in https://github.com/apache/tvm/pull/19759
* [MetaScheduler] Improve print info about builder/runner state by @cbalint13 in https://github.com/apache/tvm/pull/19767
* [REFACTOR][CUDA] Phase out l2 cache flush preproc test by @tqchen in https://github.com/apache/tvm/pull/19768
* [Relax][ONNX] Fix LayerNormalization no-bias zero tensor shape and dtype by @javierdejesusda in https://github.com/apache/tvm/pull/19772
* [Relax][ONNX] Support exclusive option in CumSum by @javierdejesusda in https://github.com/apache/tvm/pull/19773
* [CPP_RPC] Bugfix race conditions and enhance print infos by @cbalint13 in https://github.com/apache/tvm/pull/19778
* [CMAKE] Upgrade TVM build baseline to C++20 by @Ubospica in https://github.com/apache/tvm/pull/19734
* [REFACTOR][CUDA] Phase out cuda_common.h by @tqchen in https://github.com/apache/tvm/pull/19770
* [REFACTOR][PYTHON] Consolidate backend autoload infra by @tqchen in https://github.com/apache/tvm/pull/19769
* [Fix] nn.attention support dynamic batch_size by @flashmouse in https://github.com/apache/tvm/pull/19779
* [Relax][ONNX] Make ReduceMax/ReduceMin NaN propagation order-independent(numpy semantics) by @cchung100m in https://github.com/apache/tvm/pull/19755
* [Docs][CI] Bump tlcpack-sphinx-addon to restore search result summaries by @tlopex in https://github.com/apache/tvm/pull/19782
* [REFACTOR][IR] Cleanup IR naming utilities by @tqchen in https://github.com/apache/tvm/pull/19781
* [CUDA] Narrow the cuda extra from cuda-python to cuda-bindings by @tlopex in https://github.com/apache/tvm/pull/19784
* [AGENT] Migrate agent instructions to vendor-neutral layout by @tqchen in https://github.com/apache/tvm/pull/19783
* [Tests] Modernize test gating by @tlopex in https://github.com/apache/tvm/pull/19777
* [TIRX][CUDA] Framework support for FA4, CLC intrinsics, and nvfp4 tcgen05 GEMM by @spectrometerHBH in https://github.com/apache/tvm/pull/19785
* [Relax][TensorRT] Update TensorRT runtime to 10 by @tlopex in https://github.com/apache/tvm/pull/19789
* [Tests] Make TargetCreation.DeduplicateKeys host-agnostic on AArch64 by @tlopex in https://github.com/apache/tvm/pull/19786
* [Tests] Replace remaining requires_* helpers with standard pytest by @tlopex in https://github.com/apache/tvm/pull/19787
* [TIRx][RISC-V] Use scalable RVV loops for fixed vectorize by @ZephyrLi-pro in https://github.com/apache/tvm/pull/19776
* [Docs] Modernize test-gating documentation by @tlopex in https://github.com/apache/tvm/pull/19788
* [Web] Destroy GPUDevice once on buffer creation error by @guan404ming in https://github.com/apache/tvm/pull/19790
* [REFACTOR] Phase out unused queue and rang license entries by @tqchen in https://github.com/apache/tvm/pull/19794
* [REFACTOR][HEXAGON] Phase out Hexagon app and test wrappers by @tqchen in https://github.com/apache/tvm/pull/19796
* [CI] Pin GitHub Actions to SHA for ASF INFRA compliance by @guan404ming in https://github.com/apache/tvm/pull/19793
* refactor(web): use singular requestFileHandle() instead of requestFileHandles() by @tomayac in https://github.com/apache/tvm/pull/19780
* [REFACTOR][IR] Simplify CallingConv attribute access by @tqchen in https://github.com/apache/tvm/pull/19799
* [CI] Remove Jenkins PR linter step by @tqchen in https://github.com/apache/tvm/pull/19798
* [Relax][Frontend][TFLite] Add support for FFT/complex operators: REAL, IMAG, COMPLEX_ABS by @fnhirwa in https://github.com/apache/tvm/pull/19763
* [Tests][Refactor] Remove unused testing helpers by @tlopex in https://github.com/apache/tvm/pull/19800
* [REFACTOR][TIRX] Add IntImm common scalar ctor and streamline MakeConst by @tqchen in https://github.com/apache/tvm/pull/19797
* [Relax] Fix FuseOpsByPattern dropping bound constants on duplicate-structure functions by @tlopex in https://github.com/apache/tvm/pull/19801
* [Tests] Migrate tvm.testing.parameters() to pytest.mark.parametrize by @tlopex in https://github.com/apache/tvm/pull/19803
* [Tests] Remove the now-unused tvm.testing.parameters() helper by @tlopex in https://github.com/apache/tvm/pull/19807
* [Tests] Drop tautological env-probe implication tests by @tlopex in https://github.com/apache/tvm/pull/19811
* [Relax][TensorRT] Update BYOC operator converters from Relay to Relax by @tlopex in https://github.com/apache/tvm/pull/19810
* [FIX][TIRX] Fix dangling Op static reference warning by @tqchen in https://github.com/apache/tvm/pull/19806
* [Relax][Frontend][TFLite] Add RFFT2D op and supporting TIR kernels by @Aharrypotter in https://github.com/apache/tvm/pull/19812
* [BUILD] Hide static linked library symbols in shared libs by @tqchen in https://github.com/apache/tvm/pull/19817
* Preserve ONNX BatchNormalization inference mode by @yinli-systems in https://github.com/apache/tvm/pull/19818
* [CI] Drop redundant conda LLVM install in GH Actions build by @tlopex in https://github.com/apache/tvm/pull/19823
* [Tests] Inline thin gating helpers in the pytest plugin and tvm.testing.env by @tlopex in https://github.com/apache/tvm/pull/19819
* [Relax][Frontend][NN] Fix SourceModule include resolution for installed wheels by @tlopex in https://github.com/apache/tvm/pull/19822
* [ARITH] Add optional Z3-backed proving to Analyzer by @Ubospica in https://github.com/apache/tvm/pull/19667
* [Relax][Frontend][TFLite] Add missing TFLite operator mappings by @Aharrypotter in https://github.com/apache/tvm/pull/19813
* [Tests] Migrate off tvm.testing.parametrize_targets to native pytest by @tlopex in https://github.com/apache/tvm/pull/19826
* [FFI][ABI] Bump tvm-ffi to latest by @tqchen in https://github.com/apache/tvm/pull/19831
* [Relax][TensorRT] Add partition_for_tensorrt and a pattern table by @tlopex in https://github.com/apache/tvm/pull/19820
* [Arith] Let IRMutatorWithAnalyzer take a const Analyzer& by @tlopex in https://github.com/apache/tvm/pull/19829
* fix: Support 5D volumetric inputs in ONNX GridSample frontend converter by @mvanhorn in https://github.com/apache/tvm/pull/19816
* [Tests] Remove dead helpers and unused probes from tvm.testing by @tlopex in https://github.com/apache/tvm/pull/19821
* [Arith] Restrict floormod coefficient reduction to keep DetectIterMapstable by @tlopex in https://github.com/apache/tvm/pull/19832
* [Web] Avoid redundant OPFS lookup on cache hit by @guan404ming in https://github.com/apache/tvm/pull/19791
* [Docs] Rework Bring Your Own Codegen tutorial and add TensorRT example by @tlopex in https://github.com/apache/tvm/pull/19839
* [Arith] Add Analyzer::Clone for deep-copying analyzer state by @tlopex in https://github.com/apache/tvm/pull/19836
* [BUILD] Bump tvm-ffi after RuntimeTypeIndex optimization by @tqchen in https://github.com/apache/tvm/pull/19834
* [CPP_RPC] Replace legacy OS-specific API with std:: libraries by @cbalint13 in https://github.com/apache/tvm/pull/19840
* [Relax][ONNX] Preserve NaN in Relu to align with ONNX Runtime by @cchung100m in https://github.com/apache/tvm/pull/19750
* [Relax] Fix matmul and reductions with zero-size dimension return uninitialized memory by @cchung100m in https://github.com/apache/tvm/pull/19680
* [TIRx] Phase out flat device-intrinsic op aliases by @tlopex in https://github.com/apache/tvm/pull/19838
* [BUILD] Sync fallback version strings to 0.26 dev cycle by @MasterJH5574 in https://github.com/apache/tvm/pull/19845
* [Docker] Bump CI image deps: sphinx-book-theme + z3-static by @tlopex in https://github.com/apache/tvm/pull/19835
* [Tests] Clean unused tvm.testing helpers by @tlopex in https://github.com/apache/tvm/pull/19846
* [Relax][ONNX] Drop NaN-preservation isnan-where wrappers by @tlopex in https://github.com/apache/tvm/pull/19847
* [Relax][ONNX] Accept 1-D scalar inputs in NonMaxSuppression by @guan404ming in https://github.com/apache/tvm/pull/19843
* [Relax][PyTorch] Add atan2 converter by @javierdejesusda in https://github.com/apache/tvm/pull/19850
* [REFACTOR][IR] Unify StructInfo and Type by @tqchen in https://github.com/apache/tvm/pull/19853
* [Docs] Add TIRx documentation section by @spectrometerHBH in https://github.com/apache/tvm/pull/19855
* [Metal] Enable Metal 4 shader compilation by @oraluben in https://github.com/apache/tvm/pull/19595
* [Relax][Frontend][TFLite] Add explicit operator marker handling by @Aharrypotter in https://github.com/apache/tvm/pull/19824
* [Relax][ONNX] Support align_corners in AffineGrid op by @guan404ming in https://github.com/apache/tvm/pull/19864
* [REFACTOR][RELAX] Phase out Relax PrimType by @tqchen in https://github.com/apache/tvm/pull/19858
* [REFACTOR][IR] Phase out Downcast usages by @tqchen in https://github.com/apache/tvm/pull/19857
* [Relax] Legalize nn.dropout as inference no-op by @guan404ming in https://github.com/apache/tvm/pull/19841
* [Docs][CI] Switch docs theme and bump images to 20260619-214849-4174cdf5 by @tlopex in https://github.com/apache/tvm/pull/19828
* [Relax] Legalize dilated conv_transpose by @guan404ming in https://github.com/apache/tvm/pull/19842
* [Relax] Update dropout call_tir out_ty spelling by @tqchen in https://github.com/apache/tvm/pull/19874
* [Docs] Right-align documentation footer by @tlopex in https://github.com/apache/tvm/pull/19868
* [Relax][TFLite] Add remaining operator tests and reverse_sequence op by @Aharrypotter in https://github.com/apache/tvm/pull/19814
* [CI] Stop building ci_lint Docker image by @tlopex in https://github.com/apache/tvm/pull/19872
* [DOCS] Align footer dropdown menu by @tlopex in https://github.com/apache/tvm/pull/19876
* [Relax][Frontend][TFLite] Support dynamic RANGE scalar bounds by @Aharrypotter in https://github.com/apache/tvm/pull/19867
* [Relax][Frontend][TFLite] Support static hashtable find by @Aharrypotter in https://github.com/apache/tvm/pull/19879
* [REFACTOR][IR] Unify PrimExpr type mechanism to PrimType instead of DataType by @tqchen in https://github.com/apache/tvm/pull/19875
* [DOCS] Add PyPI install guidance and update install command by @tlopex in https://github.com/apache/tvm/pull/19883
* [REFACTOR][IR] Clean up PrimType follow-ups by @tqchen in https://github.com/apache/tvm/pull/19884
* [TFLite] Use structural checks in frontend tests by @tlopex in https://github.com/apache/tvm/pull/19888
* [CI][CMAKE] Install CUDA driver stub for libtvm_runtime_cuda by @MasterJH5574 in https://github.com/apache/tvm/pull/19886
* [ARITH] Use IntImm in canonical scalar hot paths by @tqchen in https://github.com/apache/tvm/pull/19885
* [REFACTOR][RELAX] Rename Relax base type to AnyType by @tqchen in https://github.com/apache/tvm/pull/19889
* [Relax][Frontend][TFLite] Support dynamic DYNAMIC_UPDATE_SLICE starts by @Aharrypotter in https://github.com/apache/tvm/pull/19881
* [CI] Remove retired ci_lint Docker files by @tlopex in https://github.com/apache/tvm/pull/19878
* [TIRx] Replace vars in buffer strides and elem_offset by @guan404ming in https://github.com/apache/tvm/pull/19871
* [TIRx][LLVM] Support scalable Ramp lowering by @ZephyrLi-pro in https://github.com/apache/tvm/pull/19866
* [REFACTOR][Relax] Phase out PrimValue and Relax expression wrappers by @tqchen in https://github.com/apache/tvm/pull/19891
* [Relax] Use optional dtype for absent Relax dtype fields by @tqchen in https://github.com/apache/tvm/pull/19890
* [ONNX] Use structural checks for composite frontend tests by @tlopex in https://github.com/apache/tvm/pull/19880
* [Frontend][ONNX] Fix structural tests for TVMScript checks by @tlopex in https://github.com/apache/tvm/pull/19894
* [DOCS][TIRX] Add in-kernel profiling (CudaProfiler) tutorial by @spectrometerHBH in https://github.com/apache/tvm/pull/19895
* [Relax][PyTorch] Add rnn_tanh.input converter by @cchung100m in https://github.com/apache/tvm/pull/19837
* [DOCS] Refine tvm pypi wheel optional install guidance by @tlopex in https://github.com/apache/tvm/pull/19892
* [TIRx] Bundle CUDA tile primitive and op dispatch updates by @spectrometerHBH in https://github.com/apache/tvm/pull/19896
* [FFI] Bump tvm-ffi to latest June 28 by @tqchen in https://github.com/apache/tvm/pull/19903
* [CI][Docker] Move CI images to Ubuntu 24.04 (noble) by @tlopex in https://github.com/apache/tvm/pull/19893
* [Relax] Fix RemoveUnusedParameters symbolic var promotion by @MasterJH5574 in https://github.com/apache/tvm/pull/19901
* [Relax] Fix int64 row index cast in GPU multinomial sampling by @MasterJH5574 in https://github.com/apache/tvm/pull/19902
* [CI][Docker] Install libpolly-15-dev for noble llvm-15 static linking by @tlopex in https://github.com/apache/tvm/pull/19913
* [DOCS] Refine footer navigation links by @tlopex in https://github.com/apache/tvm/pull/19914
* [Relax] Clean up deprecated void-dtype sentinel usage by @guan404ming in https://github.com/apache/tvm/pull/19908
* [Target][RISC-V] Use riscv_cpu device key for RISC-V target tags by @Ga1axy0 in https://github.com/apache/tvm/pull/19915
* [TVMScript] Render invisible paths in structural diagnostics by @tqchen in https://github.com/apache/tvm/pull/19916
* [Runtime][KVCache] Adapt FlashInfer attention backend to 0.6.3 by @MasterJH5574 in https://github.com/apache/tvm/pull/19904
* [Relax][ONNX] Support 3D AffineGrid by @guan404ming in https://github.com/apache/tvm/pull/19863
* [TIRx] Add a dedicated boolean buffer lowering pass by @guan404ming in https://github.com/apache/tvm/pull/19873
* [ONNX] Fix missing helper in AffineGrid test by @tlopex in https://github.com/apache/tvm/pull/19920
* [REFACTOR][IR] Unify PrimExpr with Expr typed view by @tqchen in https://github.com/apache/tvm/pull/19910
* [TIRX] Remove SizeVar in favor of contextual constraints by @tqchen in https://github.com/apache/tvm/pull/19930
* [TIRx] Generalize expression functor signatures by @tqchen in https://github.com/apache/tvm/pull/19931
* [TIR] Construct proven scalar integer constants directly by @tqchen in https://github.com/apache/tvm/pull/19934
* [IR][Relax] Include expression types in structural identity by @tqchen in https://github.com/apache/tvm/pull/19933
* [FFI] Use thread-safe packed function initialization by @tqchen in https://github.com/apache/tvm/pull/19939
* [CI] Batch Python unittest pytest targets into a single invocation by @tqchen in https://github.com/apache/tvm/pull/19941
* [TEST] Serialize local GPU execution under pytest-xdist by @tqchen in https://github.com/apache/tvm/pull/19942
* [REFACTOR][SCRIPT] Keep dependent shape recursion in docsifier by @tqchen in https://github.com/apache/tvm/pull/19940
* Refactor Tensor arithmetic dispatch away from tirx.generic by @tqchen in https://github.com/apache/tvm/pull/19943
* [TIRx] Phase out duplicate Var type_annotation by @tqchen in https://github.com/apache/tvm/pull/19944
* [CI] Remove stale GitHub automation by @tqchen in https://github.com/apache/tvm/pull/19946
* [CI] Simplify Jenkins pytest execution by @tqchen in https://github.com/apache/tvm/pull/19947
* [CI] Restore dependabot configuration by @tqchen in https://github.com/apache/tvm/pull/19951
* [Cleanup] Remove macOS Clang warnings by @tqchen in https://github.com/apache/tvm/pull/19954
* [ARITH][TIR] Track positive loop extents in analyzer visitors by @tlopex in https://github.com/apache/tvm/pull/19927
* [CI] Repair Python test cleanup regressions by @tqchen in https://github.com/apache/tvm/pull/19955
* [FFI] Bump tvm-ffi for stable Optional layout by @tqchen in https://github.com/apache/tvm/pull/19956
* [ARITH] Scope interval constraints to mapped variables by @tqchen in https://github.com/apache/tvm/pull/19963
* Phase out Relax-specific Id aliases by @tqchen in https://github.com/apache/tvm/pull/19959
* [Relax][PyTorch] Bind symbolic scalar inputs in from_fx by @guan404ming in https://github.com/apache/tvm/pull/19964
* [Relax] Fix divide-by-zero in reshape pattern detection by @guan404ming in https://github.com/apache/tvm/pull/19958
* [Relax][Frontend][ONNX] Add support for Pad mode="wrap" for opset 19 by @napronald in https://github.com/apache/tvm/pull/19827
* [Relax][PyTorch] Fix masked_select VM build by @V-aerus in https://github.com/apache/tvm/pull/19937
* [TIRx] Reuse pass-through input names for inverse index map vars by @guan404ming in https://github.com/apache/tvm/pull/19906
* [Relax] Fix bucketize output dtype during legalization by @V-aerus in https://github.com/apache/tvm/pull/19936
* [Metal] Let compile callback declare payload format via (payload, fmt) by @echuraev in https://github.com/apache/tvm/pull/19924
* [Runtime] Fix CUDA build breaks in fp8 cutlass and thrust by @MasterJH5574 in https://github.com/apache/tvm/pull/19980
* [Fix][Relax][ONNX] Import TopK indices as int64 by @viiccwen in https://github.com/apache/tvm/pull/19973
* [Fix][Relax][ONNX] Cast BatchNorm params to input dtype by @viiccwen in https://github.com/apache/tvm/pull/19979
* [Relax] Legalize shape_to_tensor to device kernel by @guan404ming in https://github.com/apache/tvm/pull/19957
* [CI] Enable parallel GitHub Actions wheel builds by @tlopex in https://github.com/apache/tvm/pull/19983
* [Relax][Frontend][ONNX] Add GroupNormalization support by @napronald in https://github.com/apache/tvm/pull/19907
* [Fix] Add `origins` option to `requestFileHandle` by @tomayac in https://github.com/apache/tvm/pull/19960
* [Relax][PyTorch] Use make_tensor in exported program tests by @mshr-h in https://github.com/apache/tvm/pull/19989
* [Fix][Relax][TFLite] Use astype for frontend casts by @Aharrypotter in https://github.com/apache/tvm/pull/19932
* [Fix][Python] Use standard scikit-build directory by @tlopex in https://github.com/apache/tvm/pull/19990
* [Arith] Fix const-int-bound modular-set tightening for Mod/FloorMod by @sbinabdullah in https://github.com/apache/tvm/pull/19978
* [Fix][Relax][PyTorch] Compare Dynamo output against PyTorch reference by @mshr-h in https://github.com/apache/tvm/pull/19994
* [Fix][Relax][ONNX] Preserve rank-expanding Expand by @viiccwen in https://github.com/apache/tvm/pull/19992
* [DLight][CUDA] Fix undefined TX in GEMV broadcast epilogue by @Nanmur in https://github.com/apache/tvm/pull/19970
* [Relax][Frontend][ONNX] Support Modern QDQ opset attributes by @napronald in https://github.com/apache/tvm/pull/19993
* [Fix][Relax][ONNX] Recover ConstantOfShape initializer shape by @viiccwen in https://github.com/apache/tvm/pull/20002
* [CI] Bump CI at the Ubuntu 24.04 images and re-enable USE_Z3 by @tlopex in https://github.com/apache/tvm/pull/19911
* [Tests][TIRx] Localize hardware test gates by @tlopex in https://github.com/apache/tvm/pull/19985
* [RUNTIME][PYTHON] Add explicit Target device conversion by @tqchen in https://github.com/apache/tvm/pull/20005
* [Fix][Relax][ONNX] Preserve integer Div truncation during import by @viiccwen in https://github.com/apache/tvm/pull/19975
* [IR][Relax][TIRx] Unify Var identity by @tqchen in https://github.com/apache/tvm/pull/20004
* [RELAX] Unify call_tir primitive arguments by @tqchen in https://github.com/apache/tvm/pull/20009
* [Tests] Reduce runtime of slow Python tests by @tlopex in https://github.com/apache/tvm/pull/20006
* [Fix][Relax][ONNX] Relax op normalization for onnx subgraphs by @cbalint13 in https://github.com/apache/tvm/pull/20010
* [REFACTOR][IR] Use CamelCase Var copy helpers by @tqchen in https://github.com/apache/tvm/pull/20008
* [REFACTOR] Remove redundant defensive code guaranteed by IR invariants by @tqchen in https://github.com/apache/tvm/pull/20011
* [Tests][Frontend] Remove redundant ONNX and TFLite tests by @tlopex in https://github.com/apache/tvm/pull/20012
* [Relax][TensorRT] Fix YOLO BYOC offload and partitioning gaps by @tlopex in https://github.com/apache/tvm/pull/19998
* [Web] Link TVMFFIHandleInitOnce into WASM runtime by @akaashrp in https://github.com/apache/tvm/pull/20020
* [REFACTOR][TIR] Phase out redundant TIRx attr names by @tqchen in https://github.com/apache/tvm/pull/20017
* [IR] Rename Var name_hint field to name by @tqchen in https://github.com/apache/tvm/pull/20016
* [TIRx] Introduce first-class Return statement by @tqchen in https://github.com/apache/tvm/pull/20018
* [Tests][Frontend] Remove redundant PyTorch frontend tests by @tlopex in https://github.com/apache/tvm/pull/20021
* [REFACTOR][TIR] Remove buffer type and axis separators by @tqchen in https://github.com/apache/tvm/pull/20019
* [Tests] Update test_adaptive_pooling_window expected IR for const-int-bound fix by @sbinabdullah in https://github.com/apache/tvm/pull/20023
* [S-TIR] Remove unused meta-schedule annotation constants by @tqchen in https://github.com/apache/tvm/pull/20022
* [Fix][Relax][ONNX] Preserve ONNX Squeeze axes attribute for opset < 13 by @OmarAzizi in https://github.com/apache/tvm/pull/19966
* [Relax][Frontend][ONNX] Support dynamic index for Gather on shape by @hamzaqureshi5 in https://github.com/apache/tvm/pull/19968
* [Tests] Reduce redundant ONNX and PyTorch integration tests by @tlopex in https://github.com/apache/tvm/pull/20026
* [REFACTOR][TIRx] Keep AttrStmt node values unboxed by @tqchen in https://github.com/apache/tvm/pull/20030
* [CI] Bump tvm-ffi with compatible Python wrappers by @tqchen in https://github.com/apache/tvm/pull/20032
* [Vulkan] Fix SPIR-V 1.4+ entry-point interfaces by @wilx in https://github.com/apache/tvm/pull/20028
* [Web] Expose RNG state for deterministic restore by @akaashrp in https://github.com/apache/tvm/pull/20034
* [TIRx] Improve BufferStore cast warning context by @tlopex in https://github.com/apache/tvm/pull/20038
* [CI] Verify packed uint1 tvm-ffi revision by @tqchen in https://github.com/apache/tvm/pull/20041
* [Relax] Legalize grouped conv with symbolic channels by @guan404ming in https://github.com/apache/tvm/pull/20039
* [Fix][TIRx] Ignore statement spans in structural identity by @tlopex in https://github.com/apache/tvm/pull/20043
* [Web] Link custom allocator into WASM runtime by @akaashrp in https://github.com/apache/tvm/pull/20046
* [Relax][Frontend][ONNX] Support Shape start and end attributes by @napronald in https://github.com/apache/tvm/pull/20050
* [Fix][LLVM] Keep packed init callbacks local on Mach-O by @akaashrp in https://github.com/apache/tvm/pull/20052
* [Relax][Frontend][ONNX] Fix LpPool conversion by @napronald in https://github.com/apache/tvm/pull/20053
* [Fix][Relax] Return frontend tensor dtype value by @akaashrp in https://github.com/apache/tvm/pull/20051
* [Fix][TIRx] Handle vector access pointer addresses in C codegen by @tlopex in https://github.com/apache/tvm/pull/20058
* [FIX][TIRx] Use cluster arrivals for remote mbarrier views by @jinhongyii in https://github.com/apache/tvm/pull/20074
* [TVMSCRIPT][TIRx] Preserve parser source spans in IR by @jinhongyii in https://github.com/apache/tvm/pull/20073
* [FIX][TIRx] Make TilePrimitiveCall serializable by @jinhongyii in https://github.com/apache/tvm/pull/20071
* [FIX][TIRx] Preserve pointer expression types by @jinhongyii in https://github.com/apache/tvm/pull/20070
* [FIX][TIRx] Remap buffers consistently in ConvertSSA by @jinhongyii in https://github.com/apache/tvm/pull/20069
* [FIX][TIRx][CUDA] Fix tcgen05 register fragment layouts by @jinhongyii in https://github.com/apache/tvm/pull/20068
* [FIX][TIRx] Constant-fold copy slice extents by @jinhongyii in https://github.com/apache/tvm/pull/20067
* [FEATURE][TIRx][CUDA] Support TMEM datapath B by @jinhongyii in https://github.com/apache/tvm/pull/20075
* [TIRX] Represent buffers as typed variables by @tqchen in https://github.com/apache/tvm/pull/20079
* [Web] Batch GPU-to-GPU copies, fix WebGPU synchronization, and add tests for command batching by @akaashrp in https://github.com/apache/tvm/pull/20059
* [TIRx] tcgen05 dispatch paths, buffer dim-surgery views, FlashMLA lowering, and typed-buffer migration fixes by @spectrometerHBH in https://github.com/apache/tvm/pull/20080
* [TIRx] Flatten cuda/trn backend operator folder by @spectrometerHBH in https://github.com/apache/tvm/pull/20081
* [FFI] Bump tvm-ffi to latest Aug 3 by @tqchen in https://github.com/apache/tvm/pull/20083
* [BUILD] Migrate the Z3 dependency to mlc-z3-static by @Ubospica in https://github.com/apache/tvm/pull/20084
* [Relax][Test] Cover default GPU pipeline scheduling for R.power/elementwise kernels by @cchung100m in https://github.com/apache/tvm/pull/19923
* [FIX][TIRx] Use physical order for Buffer.local views by @jinhongyii in https://github.com/apache/tvm/pull/20076
* feat(lower-tirx): align NVIDIA IKET profiling with the official ABI by @spectrometerHBH in https://github.com/apache/tvm/pull/20085
* [FFI] Bump tvm-ffi to 0.1.13.post2 by @tqchen in https://github.com/apache/tvm/pull/20088
* tirx: represent buffer parameters with BufferType by @tqchen in https://github.com/apache/tvm/pull/20086
* [Web] Bump tvmjs version to 0.26.0  and apache-tvm-ffi floor to >=0.1.13.post2 by @MasterJH5574 in https://github.com/apache/tvm/pull/20093
* [Fix][TIRx] Fix MSVC build of IndexDataTypeNormalizer by @MasterJH5574 in https://github.com/apache/tvm/pull/20096

## New Contributors
* @weicheng-hsu made their first contribution in https://github.com/apache/tvm/pull/19516
* @THINKER-ONLY made their first contribution in https://github.com/apache/tvm/pull/19527
* @javierdejesusda made their first contribution in https://github.com/apache/tvm/pull/19573
* @q55180514 made their first contribution in https://github.com/apache/tvm/pull/19590
* @bl4cksku11 made their first contribution in https://github.com/apache/tvm/pull/19586
* @kistenklaus made their first contribution in https://github.com/apache/tvm/pull/19619
* @CodeMechanic-Bot made their first contribution in https://github.com/apache/tvm/pull/19648
* @tomayac made their first contribution in https://github.com/apache/tvm/pull/19569
* @flashmouse made their first contribution in https://github.com/apache/tvm/pull/19683
* @ZephyrLi-pro made their first contribution in https://github.com/apache/tvm/pull/19776
* @yinli-systems made their first contribution in https://github.com/apache/tvm/pull/19818
* @mvanhorn made their first contribution in https://github.com/apache/tvm/pull/19816
* @Ga1axy0 made their first contribution in https://github.com/apache/tvm/pull/19915
* @napronald made their first contribution in https://github.com/apache/tvm/pull/19827
* @V-aerus made their first contribution in https://github.com/apache/tvm/pull/19937
* @viiccwen made their first contribution in https://github.com/apache/tvm/pull/19973
* @sbinabdullah made their first contribution in https://github.com/apache/tvm/pull/19978
* @Nanmur made their first contribution in https://github.com/apache/tvm/pull/19970
* @hamzaqureshi5 made their first contribution in https://github.com/apache/tvm/pull/19968
* @wilx made their first contribution in https://github.com/apache/tvm/pull/20028

**Full Changelog**: https://github.com/apache/tvm/compare/v0.24.0...v0.26.0.rc0

## v0.26.0 (2026-08-11)

## What's Changed
* [Relax][PyTorch] Cast non-bool inputs to bool in logical_and converter by @javierdejesusda in https://github.com/apache/tvm/pull/19679
* [CI] Remove PyPI-only tag ref guard from wheel publishing by @tlopex in https://github.com/apache/tvm/pull/19685
* [CI] Target apache-tvm for PyPI wheel publishing by @tlopex in https://github.com/apache/tvm/pull/19686
* [Web] Bump tvmjs version to 0.25.0-dev1 by @akaashrp in https://github.com/apache/tvm/pull/19687
* [Fix] CommReduce could handle 0-dim data by @flashmouse in https://github.com/apache/tvm/pull/19683
* [CI] Pin actions by version tag, trim wheel perms by @MasterJH5574 in https://github.com/apache/tvm/pull/19703
* [Tests] Fix s_tir tests using removed T.block API in TIRx script by @tlopex in https://github.com/apache/tvm/pull/19706
* [CI] Fix release verification script by @MasterJH5574 in https://github.com/apache/tvm/pull/19700
* [Refactor][Meta-schedule] Remove meta-schedule as_string mechanism in favor of default representation by @tlopex in https://github.com/apache/tvm/pull/19709
* [Python] Bump apache-tvm-ffi floor to >=0.1.12 by @MasterJH5574 in https://github.com/apache/tvm/pull/19710
* [Relax][CoreML] Fix CoreML partition pass by @tlopex in https://github.com/apache/tvm/pull/19711
* [Tests] Skip test modules cleanly when optional deps are missing by @tlopex in https://github.com/apache/tvm/pull/19704
* [CI] Merge PR against its target branch instead of main by @MasterJH5574 in https://github.com/apache/tvm/pull/19712
* [CI] Fix CI script test subprocess environment by @tlopex in https://github.com/apache/tvm/pull/19713
* [Codegen][LLVM] Accept splat form in VLA broadcast test by @tlopex in https://github.com/apache/tvm/pull/19716
* [DOCS] Clarify loading serialized artifacts requires a trusted source by @tqchen in https://github.com/apache/tvm/pull/19720
* [REFACTOR][PYTHON] Slim tvm.libinfo to info-only helpers by @tqchen in https://github.com/apache/tvm/pull/19719
* [Codegen][NVPTX] Skip runtime execution in Vulkan codegen tests by @tlopex in https://github.com/apache/tvm/pull/19717
* [REFACTOR][PYTHON] Remove tvm.ffi shim; import tvm_ffi directly by @tqchen in https://github.com/apache/tvm/pull/19721
* [Runtime][Tests] Fix contrib wheel tests by @tlopex in https://github.com/apache/tvm/pull/19714
* [Tests][Disco] Skip CCL tests when runtime support is absent by @tlopex in https://github.com/apache/tvm/pull/19724
* [Tests][Relax] Gate multi-GPU VM test on three devices by @tlopex in https://github.com/apache/tvm/pull/19725
* [REFACTOR][IR] Phase out diagnostic.h for visit-context-aware pass errors by @tqchen in https://github.com/apache/tvm/pull/19722
* [Tests][Hexagon] Lazily import pytest plugin dependencies by @tlopex in https://github.com/apache/tvm/pull/19726
* [Python] Refactor pyproject.toml dependencies by @tlopex in https://github.com/apache/tvm/pull/19723
* [Tests][NNAPI] Skip tests cleanly when remote environment is unavailable by @tlopex in https://github.com/apache/tvm/pull/19730
* [Tests][S-TIR] Fix stale MetaSchedule sketch expectations and migrate let binds to T.let by @tlopex in https://github.com/apache/tvm/pull/19729
* [Tests] Remove test_runtime_ndarray (covered by tvm-ffi) by @tlopex in https://github.com/apache/tvm/pull/19715
* [TIRx] Preserve Triton call_kernel compile options by @tlopex in https://github.com/apache/tvm/pull/19728
* [Relax][PyTorch][DLight] Fix exported-program CUDA test failures by @tlopex in https://github.com/apache/tvm/pull/19732
* [PYTHON] Autoload backends; simplify library loading; remove TVMError for native errors by @tqchen in https://github.com/apache/tvm/pull/19727
* [Script][Tests] Fix dialect redirect module re-execution and stray category-less tirx.intrin_test op by @tlopex in https://github.com/apache/tvm/pull/19731
* [S-TIR][Tests] Fix transform test failures after TIRx bringup by @tlopex in https://github.com/apache/tvm/pull/19735
* [TIRx] Use canonical PTX async script API in s_tir test by @tlopex in https://github.com/apache/tvm/pull/19739
* [Tests] Check WebGPU volatile allreduce annotation structurally by @tlopex in https://github.com/apache/tvm/pull/19740
* [S-TIR] Fix software pipeline offsets for legacy MMA intrinsics by @tlopex in https://github.com/apache/tvm/pull/19742
* [Tests] Fix flaky popen pool executor test by @tlopex in https://github.com/apache/tvm/pull/19746
* [Hexagon][Tests] Clean up stale hexagon tests by @tlopex in https://github.com/apache/tvm/pull/19747
* [Runtime][Disco] Fix session attribute storage, NVSHMEM build, and test gating by @tlopex in https://github.com/apache/tvm/pull/19736
* [CI] Align cuda-python with PyTorch cuda-bindings by @tlopex in https://github.com/apache/tvm/pull/19738
* [Codegen][LLVM][Tests] Gate +v9a vscale_range expectation on LLVM version by @tlopex in https://github.com/apache/tvm/pull/19744
* [Runtime][Tests] Drop int4 from random_fill test, fix dtype error message by @tlopex in https://github.com/apache/tvm/pull/19748
* [Tests][LLVM] Gate stepvector intrinsic rename on LLVM 20 by @tlopex in https://github.com/apache/tvm/pull/19745
* [S-TIR][Tests] Mark test_cp_async_in_if_then_else as xfail by @tlopex in https://github.com/apache/tvm/pull/19751
* [CI] Run s_tir/transform tests in the python-unittest stage by @tlopex in https://github.com/apache/tvm/pull/19737
* [CI] Updated cibw to 4.1.0 by @tlopex in https://github.com/apache/tvm/pull/19754
* [TIRX][Tests] Fix LLVM version gate for vectorized lround by @tlopex in https://github.com/apache/tvm/pull/19753
* [S-TIR][CUDA] Fix legacy predicated cp.async zero fill by @tlopex in https://github.com/apache/tvm/pull/19741
* [Tests][AArch64] Make SVE codegen assertions robust across LLVM versions by @tlopex in https://github.com/apache/tvm/pull/19752
* [Relax][PyTorch] Add logical_or and logical_xor converters by @javierdejesusda in https://github.com/apache/tvm/pull/19756
* [TIRx] Post-bringup follow-ups: op-dispatch, namespaces, launch bounds, gemm-async, backend reorg by @spectrometerHBH in https://github.com/apache/tvm/pull/19757
* [REFACTOR][VM] Move CUDA graph VM builtin back under VM runtime by @tqchen in https://github.com/apache/tvm/pull/19758
* [Runtime][CoreML] Fix FFI casts in CoreML runtime by @tlopex in https://github.com/apache/tvm/pull/19762
* [CI] Drop redundant cmake/ninja install from the Linux wheel CUDA sidecar by @tlopex in https://github.com/apache/tvm/pull/19761
* [REFACTOR][DataType] Phase out target custom datatype support by @tqchen in https://github.com/apache/tvm/pull/19760
* [REFACTOR][TARGET] Cleanup backend target registration by @tqchen in https://github.com/apache/tvm/pull/19759
* [MetaScheduler] Improve print info about builder/runner state by @cbalint13 in https://github.com/apache/tvm/pull/19767
* [REFACTOR][CUDA] Phase out l2 cache flush preproc test by @tqchen in https://github.com/apache/tvm/pull/19768
* [Relax][ONNX] Fix LayerNormalization no-bias zero tensor shape and dtype by @javierdejesusda in https://github.com/apache/tvm/pull/19772
* [Relax][ONNX] Support exclusive option in CumSum by @javierdejesusda in https://github.com/apache/tvm/pull/19773
* [CPP_RPC] Bugfix race conditions and enhance print infos by @cbalint13 in https://github.com/apache/tvm/pull/19778
* [CMAKE] Upgrade TVM build baseline to C++20 by @Ubospica in https://github.com/apache/tvm/pull/19734
* [REFACTOR][CUDA] Phase out cuda_common.h by @tqchen in https://github.com/apache/tvm/pull/19770
* [REFACTOR][PYTHON] Consolidate backend autoload infra by @tqchen in https://github.com/apache/tvm/pull/19769
* [Fix] nn.attention support dynamic batch_size by @flashmouse in https://github.com/apache/tvm/pull/19779
* [Relax][ONNX] Make ReduceMax/ReduceMin NaN propagation order-independent(numpy semantics) by @cchung100m in https://github.com/apache/tvm/pull/19755
* [Docs][CI] Bump tlcpack-sphinx-addon to restore search result summaries by @tlopex in https://github.com/apache/tvm/pull/19782
* [REFACTOR][IR] Cleanup IR naming utilities by @tqchen in https://github.com/apache/tvm/pull/19781
* [CUDA] Narrow the cuda extra from cuda-python to cuda-bindings by @tlopex in https://github.com/apache/tvm/pull/19784
* [AGENT] Migrate agent instructions to vendor-neutral layout by @tqchen in https://github.com/apache/tvm/pull/19783
* [Tests] Modernize test gating by @tlopex in https://github.com/apache/tvm/pull/19777
* [TIRX][CUDA] Framework support for FA4, CLC intrinsics, and nvfp4 tcgen05 GEMM by @spectrometerHBH in https://github.com/apache/tvm/pull/19785
* [Relax][TensorRT] Update TensorRT runtime to 10 by @tlopex in https://github.com/apache/tvm/pull/19789
* [Tests] Make TargetCreation.DeduplicateKeys host-agnostic on AArch64 by @tlopex in https://github.com/apache/tvm/pull/19786
* [Tests] Replace remaining requires_* helpers with standard pytest by @tlopex in https://github.com/apache/tvm/pull/19787
* [TIRx][RISC-V] Use scalable RVV loops for fixed vectorize by @ZephyrLi-pro in https://github.com/apache/tvm/pull/19776
* [Docs] Modernize test-gating documentation by @tlopex in https://github.com/apache/tvm/pull/19788
* [Web] Destroy GPUDevice once on buffer creation error by @guan404ming in https://github.com/apache/tvm/pull/19790
* [REFACTOR] Phase out unused queue and rang license entries by @tqchen in https://github.com/apache/tvm/pull/19794
* [REFACTOR][HEXAGON] Phase out Hexagon app and test wrappers by @tqchen in https://github.com/apache/tvm/pull/19796
* [CI] Pin GitHub Actions to SHA for ASF INFRA compliance by @guan404ming in https://github.com/apache/tvm/pull/19793
* refactor(web): use singular requestFileHandle() instead of requestFileHandles() by @tomayac in https://github.com/apache/tvm/pull/19780
* [REFACTOR][IR] Simplify CallingConv attribute access by @tqchen in https://github.com/apache/tvm/pull/19799
* [CI] Remove Jenkins PR linter step by @tqchen in https://github.com/apache/tvm/pull/19798
* [Relax][Frontend][TFLite] Add support for FFT/complex operators: REAL, IMAG, COMPLEX_ABS by @fnhirwa in https://github.com/apache/tvm/pull/19763
* [Tests][Refactor] Remove unused testing helpers by @tlopex in https://github.com/apache/tvm/pull/19800
* [REFACTOR][TIRX] Add IntImm common scalar ctor and streamline MakeConst by @tqchen in https://github.com/apache/tvm/pull/19797
* [Relax] Fix FuseOpsByPattern dropping bound constants on duplicate-structure functions by @tlopex in https://github.com/apache/tvm/pull/19801
* [Tests] Migrate tvm.testing.parameters() to pytest.mark.parametrize by @tlopex in https://github.com/apache/tvm/pull/19803
* [Tests] Remove the now-unused tvm.testing.parameters() helper by @tlopex in https://github.com/apache/tvm/pull/19807
* [Tests] Drop tautological env-probe implication tests by @tlopex in https://github.com/apache/tvm/pull/19811
* [Relax][TensorRT] Update BYOC operator converters from Relay to Relax by @tlopex in https://github.com/apache/tvm/pull/19810
* [FIX][TIRX] Fix dangling Op static reference warning by @tqchen in https://github.com/apache/tvm/pull/19806
* [Relax][Frontend][TFLite] Add RFFT2D op and supporting TIR kernels by @Aharrypotter in https://github.com/apache/tvm/pull/19812
* [BUILD] Hide static linked library symbols in shared libs by @tqchen in https://github.com/apache/tvm/pull/19817
* Preserve ONNX BatchNormalization inference mode by @yinli-systems in https://github.com/apache/tvm/pull/19818
* [CI] Drop redundant conda LLVM install in GH Actions build by @tlopex in https://github.com/apache/tvm/pull/19823
* [Tests] Inline thin gating helpers in the pytest plugin and tvm.testing.env by @tlopex in https://github.com/apache/tvm/pull/19819
* [Relax][Frontend][NN] Fix SourceModule include resolution for installed wheels by @tlopex in https://github.com/apache/tvm/pull/19822
* [ARITH] Add optional Z3-backed proving to Analyzer by @Ubospica in https://github.com/apache/tvm/pull/19667
* [Relax][Frontend][TFLite] Add missing TFLite operator mappings by @Aharrypotter in https://github.com/apache/tvm/pull/19813
* [Tests] Migrate off tvm.testing.parametrize_targets to native pytest by @tlopex in https://github.com/apache/tvm/pull/19826
* [FFI][ABI] Bump tvm-ffi to latest by @tqchen in https://github.com/apache/tvm/pull/19831
* [Relax][TensorRT] Add partition_for_tensorrt and a pattern table by @tlopex in https://github.com/apache/tvm/pull/19820
* [Arith] Let IRMutatorWithAnalyzer take a const Analyzer& by @tlopex in https://github.com/apache/tvm/pull/19829
* fix: Support 5D volumetric inputs in ONNX GridSample frontend converter by @mvanhorn in https://github.com/apache/tvm/pull/19816
* [Tests] Remove dead helpers and unused probes from tvm.testing by @tlopex in https://github.com/apache/tvm/pull/19821
* [Arith] Restrict floormod coefficient reduction to keep DetectIterMapstable by @tlopex in https://github.com/apache/tvm/pull/19832
* [Web] Avoid redundant OPFS lookup on cache hit by @guan404ming in https://github.com/apache/tvm/pull/19791
* [Docs] Rework Bring Your Own Codegen tutorial and add TensorRT example by @tlopex in https://github.com/apache/tvm/pull/19839
* [Arith] Add Analyzer::Clone for deep-copying analyzer state by @tlopex in https://github.com/apache/tvm/pull/19836
* [BUILD] Bump tvm-ffi after RuntimeTypeIndex optimization by @tqchen in https://github.com/apache/tvm/pull/19834
* [CPP_RPC] Replace legacy OS-specific API with std:: libraries by @cbalint13 in https://github.com/apache/tvm/pull/19840
* [Relax][ONNX] Preserve NaN in Relu to align with ONNX Runtime by @cchung100m in https://github.com/apache/tvm/pull/19750
* [Relax] Fix matmul and reductions with zero-size dimension return uninitialized memory by @cchung100m in https://github.com/apache/tvm/pull/19680
* [TIRx] Phase out flat device-intrinsic op aliases by @tlopex in https://github.com/apache/tvm/pull/19838
* [BUILD] Sync fallback version strings to 0.26 dev cycle by @MasterJH5574 in https://github.com/apache/tvm/pull/19845
* [Docker] Bump CI image deps: sphinx-book-theme + z3-static by @tlopex in https://github.com/apache/tvm/pull/19835
* [Tests] Clean unused tvm.testing helpers by @tlopex in https://github.com/apache/tvm/pull/19846
* [Relax][ONNX] Drop NaN-preservation isnan-where wrappers by @tlopex in https://github.com/apache/tvm/pull/19847
* [Relax][ONNX] Accept 1-D scalar inputs in NonMaxSuppression by @guan404ming in https://github.com/apache/tvm/pull/19843
* [Relax][PyTorch] Add atan2 converter by @javierdejesusda in https://github.com/apache/tvm/pull/19850
* [REFACTOR][IR] Unify StructInfo and Type by @tqchen in https://github.com/apache/tvm/pull/19853
* [Docs] Add TIRx documentation section by @spectrometerHBH in https://github.com/apache/tvm/pull/19855
* [Metal] Enable Metal 4 shader compilation by @oraluben in https://github.com/apache/tvm/pull/19595
* [Relax][Frontend][TFLite] Add explicit operator marker handling by @Aharrypotter in https://github.com/apache/tvm/pull/19824
* [Relax][ONNX] Support align_corners in AffineGrid op by @guan404ming in https://github.com/apache/tvm/pull/19864
* [REFACTOR][RELAX] Phase out Relax PrimType by @tqchen in https://github.com/apache/tvm/pull/19858
* [REFACTOR][IR] Phase out Downcast usages by @tqchen in https://github.com/apache/tvm/pull/19857
* [Relax] Legalize nn.dropout as inference no-op by @guan404ming in https://github.com/apache/tvm/pull/19841
* [Docs][CI] Switch docs theme and bump images to 20260619-214849-4174cdf5 by @tlopex in https://github.com/apache/tvm/pull/19828
* [Relax] Legalize dilated conv_transpose by @guan404ming in https://github.com/apache/tvm/pull/19842
* [Relax] Update dropout call_tir out_ty spelling by @tqchen in https://github.com/apache/tvm/pull/19874
* [Docs] Right-align documentation footer by @tlopex in https://github.com/apache/tvm/pull/19868
* [Relax][TFLite] Add remaining operator tests and reverse_sequence op by @Aharrypotter in https://github.com/apache/tvm/pull/19814
* [CI] Stop building ci_lint Docker image by @tlopex in https://github.com/apache/tvm/pull/19872
* [DOCS] Align footer dropdown menu by @tlopex in https://github.com/apache/tvm/pull/19876
* [Relax][Frontend][TFLite] Support dynamic RANGE scalar bounds by @Aharrypotter in https://github.com/apache/tvm/pull/19867
* [Relax][Frontend][TFLite] Support static hashtable find by @Aharrypotter in https://github.com/apache/tvm/pull/19879
* [REFACTOR][IR] Unify PrimExpr type mechanism to PrimType instead of DataType by @tqchen in https://github.com/apache/tvm/pull/19875
* [DOCS] Add PyPI install guidance and update install command by @tlopex in https://github.com/apache/tvm/pull/19883
* [REFACTOR][IR] Clean up PrimType follow-ups by @tqchen in https://github.com/apache/tvm/pull/19884
* [TFLite] Use structural checks in frontend tests by @tlopex in https://github.com/apache/tvm/pull/19888
* [CI][CMAKE] Install CUDA driver stub for libtvm_runtime_cuda by @MasterJH5574 in https://github.com/apache/tvm/pull/19886
* [ARITH] Use IntImm in canonical scalar hot paths by @tqchen in https://github.com/apache/tvm/pull/19885
* [REFACTOR][RELAX] Rename Relax base type to AnyType by @tqchen in https://github.com/apache/tvm/pull/19889
* [Relax][Frontend][TFLite] Support dynamic DYNAMIC_UPDATE_SLICE starts by @Aharrypotter in https://github.com/apache/tvm/pull/19881
* [CI] Remove retired ci_lint Docker files by @tlopex in https://github.com/apache/tvm/pull/19878
* [TIRx] Replace vars in buffer strides and elem_offset by @guan404ming in https://github.com/apache/tvm/pull/19871
* [TIRx][LLVM] Support scalable Ramp lowering by @ZephyrLi-pro in https://github.com/apache/tvm/pull/19866
* [REFACTOR][Relax] Phase out PrimValue and Relax expression wrappers by @tqchen in https://github.com/apache/tvm/pull/19891
* [Relax] Use optional dtype for absent Relax dtype fields by @tqchen in https://github.com/apache/tvm/pull/19890
* [ONNX] Use structural checks for composite frontend tests by @tlopex in https://github.com/apache/tvm/pull/19880
* [Frontend][ONNX] Fix structural tests for TVMScript checks by @tlopex in https://github.com/apache/tvm/pull/19894
* [DOCS][TIRX] Add in-kernel profiling (CudaProfiler) tutorial by @spectrometerHBH in https://github.com/apache/tvm/pull/19895
* [Relax][PyTorch] Add rnn_tanh.input converter by @cchung100m in https://github.com/apache/tvm/pull/19837
* [DOCS] Refine tvm pypi wheel optional install guidance by @tlopex in https://github.com/apache/tvm/pull/19892
* [TIRx] Bundle CUDA tile primitive and op dispatch updates by @spectrometerHBH in https://github.com/apache/tvm/pull/19896
* [FFI] Bump tvm-ffi to latest June 28 by @tqchen in https://github.com/apache/tvm/pull/19903
* [CI][Docker] Move CI images to Ubuntu 24.04 (noble) by @tlopex in https://github.com/apache/tvm/pull/19893
* [Relax] Fix RemoveUnusedParameters symbolic var promotion by @MasterJH5574 in https://github.com/apache/tvm/pull/19901
* [Relax] Fix int64 row index cast in GPU multinomial sampling by @MasterJH5574 in https://github.com/apache/tvm/pull/19902
* [CI][Docker] Install libpolly-15-dev for noble llvm-15 static linking by @tlopex in https://github.com/apache/tvm/pull/19913
* [DOCS] Refine footer navigation links by @tlopex in https://github.com/apache/tvm/pull/19914
* [Relax] Clean up deprecated void-dtype sentinel usage by @guan404ming in https://github.com/apache/tvm/pull/19908
* [Target][RISC-V] Use riscv_cpu device key for RISC-V target tags by @Ga1axy0 in https://github.com/apache/tvm/pull/19915
* [TVMScript] Render invisible paths in structural diagnostics by @tqchen in https://github.com/apache/tvm/pull/19916
* [Runtime][KVCache] Adapt FlashInfer attention backend to 0.6.3 by @MasterJH5574 in https://github.com/apache/tvm/pull/19904
* [Relax][ONNX] Support 3D AffineGrid by @guan404ming in https://github.com/apache/tvm/pull/19863
* [TIRx] Add a dedicated boolean buffer lowering pass by @guan404ming in https://github.com/apache/tvm/pull/19873
* [ONNX] Fix missing helper in AffineGrid test by @tlopex in https://github.com/apache/tvm/pull/19920
* [REFACTOR][IR] Unify PrimExpr with Expr typed view by @tqchen in https://github.com/apache/tvm/pull/19910
* [TIRX] Remove SizeVar in favor of contextual constraints by @tqchen in https://github.com/apache/tvm/pull/19930
* [TIRx] Generalize expression functor signatures by @tqchen in https://github.com/apache/tvm/pull/19931
* [TIR] Construct proven scalar integer constants directly by @tqchen in https://github.com/apache/tvm/pull/19934
* [IR][Relax] Include expression types in structural identity by @tqchen in https://github.com/apache/tvm/pull/19933
* [FFI] Use thread-safe packed function initialization by @tqchen in https://github.com/apache/tvm/pull/19939
* [CI] Batch Python unittest pytest targets into a single invocation by @tqchen in https://github.com/apache/tvm/pull/19941
* [TEST] Serialize local GPU execution under pytest-xdist by @tqchen in https://github.com/apache/tvm/pull/19942
* [REFACTOR][SCRIPT] Keep dependent shape recursion in docsifier by @tqchen in https://github.com/apache/tvm/pull/19940
* Refactor Tensor arithmetic dispatch away from tirx.generic by @tqchen in https://github.com/apache/tvm/pull/19943
* [TIRx] Phase out duplicate Var type_annotation by @tqchen in https://github.com/apache/tvm/pull/19944
* [CI] Remove stale GitHub automation by @tqchen in https://github.com/apache/tvm/pull/19946
* [CI] Simplify Jenkins pytest execution by @tqchen in https://github.com/apache/tvm/pull/19947
* [CI] Restore dependabot configuration by @tqchen in https://github.com/apache/tvm/pull/19951
* [Cleanup] Remove macOS Clang warnings by @tqchen in https://github.com/apache/tvm/pull/19954
* [ARITH][TIR] Track positive loop extents in analyzer visitors by @tlopex in https://github.com/apache/tvm/pull/19927
* [CI] Repair Python test cleanup regressions by @tqchen in https://github.com/apache/tvm/pull/19955
* [FFI] Bump tvm-ffi for stable Optional layout by @tqchen in https://github.com/apache/tvm/pull/19956
* [ARITH] Scope interval constraints to mapped variables by @tqchen in https://github.com/apache/tvm/pull/19963
* Phase out Relax-specific Id aliases by @tqchen in https://github.com/apache/tvm/pull/19959
* [Relax][PyTorch] Bind symbolic scalar inputs in from_fx by @guan404ming in https://github.com/apache/tvm/pull/19964
* [Relax] Fix divide-by-zero in reshape pattern detection by @guan404ming in https://github.com/apache/tvm/pull/19958
* [Relax][Frontend][ONNX] Add support for Pad mode="wrap" for opset 19 by @napronald in https://github.com/apache/tvm/pull/19827
* [Relax][PyTorch] Fix masked_select VM build by @V-aerus in https://github.com/apache/tvm/pull/19937
* [TIRx] Reuse pass-through input names for inverse index map vars by @guan404ming in https://github.com/apache/tvm/pull/19906
* [Relax] Fix bucketize output dtype during legalization by @V-aerus in https://github.com/apache/tvm/pull/19936
* [Metal] Let compile callback declare payload format via (payload, fmt) by @echuraev in https://github.com/apache/tvm/pull/19924
* [Runtime] Fix CUDA build breaks in fp8 cutlass and thrust by @MasterJH5574 in https://github.com/apache/tvm/pull/19980
* [Fix][Relax][ONNX] Import TopK indices as int64 by @viiccwen in https://github.com/apache/tvm/pull/19973
* [Fix][Relax][ONNX] Cast BatchNorm params to input dtype by @viiccwen in https://github.com/apache/tvm/pull/19979
* [Relax] Legalize shape_to_tensor to device kernel by @guan404ming in https://github.com/apache/tvm/pull/19957
* [CI] Enable parallel GitHub Actions wheel builds by @tlopex in https://github.com/apache/tvm/pull/19983
* [Relax][Frontend][ONNX] Add GroupNormalization support by @napronald in https://github.com/apache/tvm/pull/19907
* [Fix] Add `origins` option to `requestFileHandle` by @tomayac in https://github.com/apache/tvm/pull/19960
* [Relax][PyTorch] Use make_tensor in exported program tests by @mshr-h in https://github.com/apache/tvm/pull/19989
* [Fix][Relax][TFLite] Use astype for frontend casts by @Aharrypotter in https://github.com/apache/tvm/pull/19932
* [Fix][Python] Use standard scikit-build directory by @tlopex in https://github.com/apache/tvm/pull/19990
* [Arith] Fix const-int-bound modular-set tightening for Mod/FloorMod by @sbinabdullah in https://github.com/apache/tvm/pull/19978
* [Fix][Relax][PyTorch] Compare Dynamo output against PyTorch reference by @mshr-h in https://github.com/apache/tvm/pull/19994
* [Fix][Relax][ONNX] Preserve rank-expanding Expand by @viiccwen in https://github.com/apache/tvm/pull/19992
* [DLight][CUDA] Fix undefined TX in GEMV broadcast epilogue by @Nanmur in https://github.com/apache/tvm/pull/19970
* [Relax][Frontend][ONNX] Support Modern QDQ opset attributes by @napronald in https://github.com/apache/tvm/pull/19993
* [Fix][Relax][ONNX] Recover ConstantOfShape initializer shape by @viiccwen in https://github.com/apache/tvm/pull/20002
* [CI] Bump CI at the Ubuntu 24.04 images and re-enable USE_Z3 by @tlopex in https://github.com/apache/tvm/pull/19911
* [Tests][TIRx] Localize hardware test gates by @tlopex in https://github.com/apache/tvm/pull/19985
* [RUNTIME][PYTHON] Add explicit Target device conversion by @tqchen in https://github.com/apache/tvm/pull/20005
* [Fix][Relax][ONNX] Preserve integer Div truncation during import by @viiccwen in https://github.com/apache/tvm/pull/19975
* [IR][Relax][TIRx] Unify Var identity by @tqchen in https://github.com/apache/tvm/pull/20004
* [RELAX] Unify call_tir primitive arguments by @tqchen in https://github.com/apache/tvm/pull/20009
* [Tests] Reduce runtime of slow Python tests by @tlopex in https://github.com/apache/tvm/pull/20006
* [Fix][Relax][ONNX] Relax op normalization for onnx subgraphs by @cbalint13 in https://github.com/apache/tvm/pull/20010
* [REFACTOR][IR] Use CamelCase Var copy helpers by @tqchen in https://github.com/apache/tvm/pull/20008
* [REFACTOR] Remove redundant defensive code guaranteed by IR invariants by @tqchen in https://github.com/apache/tvm/pull/20011
* [Tests][Frontend] Remove redundant ONNX and TFLite tests by @tlopex in https://github.com/apache/tvm/pull/20012
* [Relax][TensorRT] Fix YOLO BYOC offload and partitioning gaps by @tlopex in https://github.com/apache/tvm/pull/19998
* [Web] Link TVMFFIHandleInitOnce into WASM runtime by @akaashrp in https://github.com/apache/tvm/pull/20020
* [REFACTOR][TIR] Phase out redundant TIRx attr names by @tqchen in https://github.com/apache/tvm/pull/20017
* [IR] Rename Var name_hint field to name by @tqchen in https://github.com/apache/tvm/pull/20016
* [TIRx] Introduce first-class Return statement by @tqchen in https://github.com/apache/tvm/pull/20018
* [Tests][Frontend] Remove redundant PyTorch frontend tests by @tlopex in https://github.com/apache/tvm/pull/20021
* [REFACTOR][TIR] Remove buffer type and axis separators by @tqchen in https://github.com/apache/tvm/pull/20019
* [Tests] Update test_adaptive_pooling_window expected IR for const-int-bound fix by @sbinabdullah in https://github.com/apache/tvm/pull/20023
* [S-TIR] Remove unused meta-schedule annotation constants by @tqchen in https://github.com/apache/tvm/pull/20022
* [Fix][Relax][ONNX] Preserve ONNX Squeeze axes attribute for opset < 13 by @OmarAzizi in https://github.com/apache/tvm/pull/19966
* [Relax][Frontend][ONNX] Support dynamic index for Gather on shape by @hamzaqureshi5 in https://github.com/apache/tvm/pull/19968
* [Tests] Reduce redundant ONNX and PyTorch integration tests by @tlopex in https://github.com/apache/tvm/pull/20026
* [REFACTOR][TIRx] Keep AttrStmt node values unboxed by @tqchen in https://github.com/apache/tvm/pull/20030
* [CI] Bump tvm-ffi with compatible Python wrappers by @tqchen in https://github.com/apache/tvm/pull/20032
* [Vulkan] Fix SPIR-V 1.4+ entry-point interfaces by @wilx in https://github.com/apache/tvm/pull/20028
* [Web] Expose RNG state for deterministic restore by @akaashrp in https://github.com/apache/tvm/pull/20034
* [TIRx] Improve BufferStore cast warning context by @tlopex in https://github.com/apache/tvm/pull/20038
* [CI] Verify packed uint1 tvm-ffi revision by @tqchen in https://github.com/apache/tvm/pull/20041
* [Relax] Legalize grouped conv with symbolic channels by @guan404ming in https://github.com/apache/tvm/pull/20039
* [Fix][TIRx] Ignore statement spans in structural identity by @tlopex in https://github.com/apache/tvm/pull/20043
* [Web] Link custom allocator into WASM runtime by @akaashrp in https://github.com/apache/tvm/pull/20046
* [Relax][Frontend][ONNX] Support Shape start and end attributes by @napronald in https://github.com/apache/tvm/pull/20050
* [Fix][LLVM] Keep packed init callbacks local on Mach-O by @akaashrp in https://github.com/apache/tvm/pull/20052
* [Relax][Frontend][ONNX] Fix LpPool conversion by @napronald in https://github.com/apache/tvm/pull/20053
* [Fix][Relax] Return frontend tensor dtype value by @akaashrp in https://github.com/apache/tvm/pull/20051
* [Fix][TIRx] Handle vector access pointer addresses in C codegen by @tlopex in https://github.com/apache/tvm/pull/20058
* [FIX][TIRx] Use cluster arrivals for remote mbarrier views by @jinhongyii in https://github.com/apache/tvm/pull/20074
* [TVMSCRIPT][TIRx] Preserve parser source spans in IR by @jinhongyii in https://github.com/apache/tvm/pull/20073
* [FIX][TIRx] Make TilePrimitiveCall serializable by @jinhongyii in https://github.com/apache/tvm/pull/20071
* [FIX][TIRx] Preserve pointer expression types by @jinhongyii in https://github.com/apache/tvm/pull/20070
* [FIX][TIRx] Remap buffers consistently in ConvertSSA by @jinhongyii in https://github.com/apache/tvm/pull/20069
* [FIX][TIRx][CUDA] Fix tcgen05 register fragment layouts by @jinhongyii in https://github.com/apache/tvm/pull/20068
* [FIX][TIRx] Constant-fold copy slice extents by @jinhongyii in https://github.com/apache/tvm/pull/20067
* [FEATURE][TIRx][CUDA] Support TMEM datapath B by @jinhongyii in https://github.com/apache/tvm/pull/20075
* [TIRX] Represent buffers as typed variables by @tqchen in https://github.com/apache/tvm/pull/20079
* [Web] Batch GPU-to-GPU copies, fix WebGPU synchronization, and add tests for command batching by @akaashrp in https://github.com/apache/tvm/pull/20059
* [TIRx] tcgen05 dispatch paths, buffer dim-surgery views, FlashMLA lowering, and typed-buffer migration fixes by @spectrometerHBH in https://github.com/apache/tvm/pull/20080
* [TIRx] Flatten cuda/trn backend operator folder by @spectrometerHBH in https://github.com/apache/tvm/pull/20081
* [FFI] Bump tvm-ffi to latest Aug 3 by @tqchen in https://github.com/apache/tvm/pull/20083
* [BUILD] Migrate the Z3 dependency to mlc-z3-static by @Ubospica in https://github.com/apache/tvm/pull/20084
* [Relax][Test] Cover default GPU pipeline scheduling for R.power/elementwise kernels by @cchung100m in https://github.com/apache/tvm/pull/19923
* [FIX][TIRx] Use physical order for Buffer.local views by @jinhongyii in https://github.com/apache/tvm/pull/20076
* feat(lower-tirx): align NVIDIA IKET profiling with the official ABI by @spectrometerHBH in https://github.com/apache/tvm/pull/20085
* [FFI] Bump tvm-ffi to 0.1.13.post2 by @tqchen in https://github.com/apache/tvm/pull/20088
* tirx: represent buffer parameters with BufferType by @tqchen in https://github.com/apache/tvm/pull/20086
* [Web] Bump tvmjs version to 0.26.0  and apache-tvm-ffi floor to >=0.1.13.post2 by @MasterJH5574 in https://github.com/apache/tvm/pull/20093
* [Fix][TIRx] Fix MSVC build of IndexDataTypeNormalizer by @MasterJH5574 in https://github.com/apache/tvm/pull/20096

## New Contributors
* @flashmouse made their first contribution in https://github.com/apache/tvm/pull/19683
* @ZephyrLi-pro made their first contribution in https://github.com/apache/tvm/pull/19776
* @yinli-systems made their first contribution in https://github.com/apache/tvm/pull/19818
* @mvanhorn made their first contribution in https://github.com/apache/tvm/pull/19816
* @Ga1axy0 made their first contribution in https://github.com/apache/tvm/pull/19915
* @napronald made their first contribution in https://github.com/apache/tvm/pull/19827
* @V-aerus made their first contribution in https://github.com/apache/tvm/pull/19937
* @viiccwen made their first contribution in https://github.com/apache/tvm/pull/19973
* @sbinabdullah made their first contribution in https://github.com/apache/tvm/pull/19978
* @Nanmur made their first contribution in https://github.com/apache/tvm/pull/19970
* @hamzaqureshi5 made their first contribution in https://github.com/apache/tvm/pull/19968
* @wilx made their first contribution in https://github.com/apache/tvm/pull/20028

**Full Changelog**: https://github.com/apache/tvm/compare/v0.25.0...v0.26.0

## v0.27.0.rc0 (2026-09-19)

## What's Changed
* [Web] Bump tvmjs version to 0.27.0-dev0 on main by @MasterJH5574 in https://github.com/apache/tvm/pull/20095
* [Fix][Relax][ONNX] Handle Split initializer with keep_params_in_input by @hahalfx in https://github.com/apache/tvm/pull/20091
* [Fix][Arith] Isolate Z3 contexts and make memoization deterministic by @tlopex in https://github.com/apache/tvm/pull/20097
* [Fix][TIRx] Fix MSVC build of IndexDataTypeNormalizer by @MasterJH5574 in https://github.com/apache/tvm/pull/20098
* [Python] Bump apache-tvm-ffi floor to >=0.1.13.post2 by @MasterJH5574 in https://github.com/apache/tvm/pull/20094
* [FIX][TIRx] Traverse pointer expressions in tile calls by @jinhongyii in https://github.com/apache/tvm/pull/20089
* [FIX][TIRx] Remap typed buffer expressions during specialization by @jinhongyii in https://github.com/apache/tvm/pull/20090
* [FIX][Relax][ONNX] Keep the static shape of a rank-0 Shape input by @adityasingh2400 in https://github.com/apache/tvm/pull/20092
* [FIX][TIRx] Use typed buffer parameter in pointer config test by @tqchen in https://github.com/apache/tvm/pull/20102
* [FIX][CUDA] Select NVRTC architecture for output format by @jinhongyii in https://github.com/apache/tvm/pull/20100
* [TIRx][CUDA] Add a table-driven PTX dialect and retire tirx.ptx.* by @spectrometerHBH in https://github.com/apache/tvm/pull/20103
* [BugFix][Metal] Preserve pointer address spaces for byte offsets by @GY-Bai in https://github.com/apache/tvm/pull/20101
* [TIRx][CUDA] uint32 index dtypes, directive fixes, and PTX ISA coverage by @spectrometerHBH in https://github.com/apache/tvm/pull/20110
* [SCRIPT] Support PEP 695 symbolic variables in Relax and TIR by @tqchen in https://github.com/apache/tvm/pull/20107
* [Fix][WebGPU] Preserve read-only buffer access modes by @akaashrp in https://github.com/apache/tvm/pull/20113
* [Relax][ONNX] Support lower-rank PRelu slopes by @Aharrypotter in https://github.com/apache/tvm/pull/20115
* [TIRX] Split backend.cuda.intrinsics, fold tcgen05 descriptors, and fix two PTX dialect gaps by @spectrometerHBH in https://github.com/apache/tvm/pull/20120
* [Feature][Relax] Support shared-KV attention with configurable sliding windows by @akaashrp in https://github.com/apache/tvm/pull/20121
* [Web] Avoid redundant memory byte copies by @akaashrp in https://github.com/apache/tvm/pull/20127
* [TIRx][CUDA] Replace source helpers with typed PTX forms by @jinhongyii in https://github.com/apache/tvm/pull/20140
* [Fix][DLight] Reject GEMV accesses unsupported by scheduling by @akaashrp in https://github.com/apache/tvm/pull/20122
* [Fix][Relax][ONNX] Fold Min/Max/Sum/Mean constants elementwise by @aryanputta in https://github.com/apache/tvm/pull/20119
* [Relax][Frontend][TFLite] Support StableHLO shape ops by @Aharrypotter in https://github.com/apache/tvm/pull/20114
* [TIRx][CUDA] Version-gate CUDA 12.8 tensor-map enums and fix registry-test lock leak by @spectrometerHBH in https://github.com/apache/tvm/pull/20154
* [TIRx][CUDA] Add PTX address expressions with immediate byte offsets by @spectrometerHBH in https://github.com/apache/tvm/pull/20153
* [Fix][DLight] Handle rank-one GEMV cache loads by @SamJSui in https://github.com/apache/tvm/pull/20158
* [Relax][ONNX] Support scalar QDQ inputs by @Aharrypotter in https://github.com/apache/tvm/pull/20126
* [BugFix][TE] Initialize nested reductions at the outermost reduction scope by @Gunse11er in https://github.com/apache/tvm/pull/20116
* [Fix][Relax] Track lowered reshape storage aliases by @akaashrp in https://github.com/apache/tvm/pull/20134
* [Fix][WebGPU] Validate and bound symbolic stack allocations by @akaashrp in https://github.com/apache/tvm/pull/20132
* [Web] Avoid tensor-cache record copies by @akaashrp in https://github.com/apache/tvm/pull/20156
* [Fix][TOPI] Fuse GPU scan blocks to avoid CUDA gridDim.y overflow by @chenmiaoming in https://github.com/apache/tvm/pull/20108
* [TIRx][CUDA] Add register and cluster launch controls by @spectrometerHBH in https://github.com/apache/tvm/pull/20159
* [Fix][Relax][Torch] Preserve derived exported input dimensions by @akaashrp in https://github.com/apache/tvm/pull/20128
* [Web] Avoid copies when uploading WASM memory to WebGPU by @akaashrp in https://github.com/apache/tvm/pull/20165
* [Web] Upload pass-through tensor-cache records directly to WebGPU by @akaashrp in https://github.com/apache/tvm/pull/20166
* [IR][TIRX] Add first-class tuple expressions by @tqchen in https://github.com/apache/tvm/pull/20168
* [TIRx][CUDA] Allow newer CUTLASS packages for IKET by @jinhongyii in https://github.com/apache/tvm/pull/20164
* [Fix][Relax] Honor ONNX Reshape zero semantics by @tandede in https://github.com/apache/tvm/pull/20161
* [TIRx][CUDA] Fix single-CTA clusterCtaIdx resolution and accept packed sub-byte tensor-map dtypes by @spectrometerHBH in https://github.com/apache/tvm/pull/20172
* feat(lower-tirx): support PTX movmatrix by @spectrometerHBH in https://github.com/apache/tvm/pull/20171
* [Fix][Relax] Run destructors for non-trivially-destructible types in Arena by @OmarAzizi in https://github.com/apache/tvm/pull/20163
* [Fix][Relax] Lower non-contiguous WebGPU cumsum by @akaashrp in https://github.com/apache/tvm/pull/20133
* [TIRx][CUDA] Preserve explicit single-CTA cluster launches by @spectrometerHBH in https://github.com/apache/tvm/pull/20180
* [Fix][Relax][Frontend][ONNX] Fix Mean/Sum/Min/Max with all-constant inputs by @siyiweigeHEW in https://github.com/apache/tvm/pull/20147
* [Runtime] Add PagedAttentionKVCache checkpoint primitives by @akaashrp in https://github.com/apache/tvm/pull/20035
* [Fix][Relax][Frontend][ONNX] Support broadcastable multi-axis PRelu slopes by @siyiweigeHEW in https://github.com/apache/tvm/pull/20149
* [Fix][Relax][Torch] Align retained expand dimensions by trailing rank by @akaashrp in https://github.com/apache/tvm/pull/20137
* [Fix][Arith] Preserve nested floormod semantics by @tlopex in https://github.com/apache/tvm/pull/20181
* [Feat][Web] Support per-parameter tensor cache encoding by @akaashrp in https://github.com/apache/tvm/pull/20136
* [Codegen][LLVM] Add LLVM 23 compatibility by @tlopex in https://github.com/apache/tvm/pull/20189
* [Web] Decode packed BF16 tensor records in place by @akaashrp in https://github.com/apache/tvm/pull/20167
* [Fix][Relax][Frontend][ONNX] Fix Scatter with indices smaller than data by @siyiweigeHEW in https://github.com/apache/tvm/pull/20187
* [Fix][Relax] Raise error on non-unit dim ONNX Squeeze axis by @OmarAzizi in https://github.com/apache/tvm/pull/20188
* fix(tirx): stabilize multi-GPU correctness tests by @spectrometerHBH in https://github.com/apache/tvm/pull/20213
* [Fix][Relax] Preserve tensor-derived symbols during fusion by @akaashrp in https://github.com/apache/tvm/pull/20139
* [Fix][S-TIR][DLight] Guard non-affine reduction write-back by @Junius-Wynn in https://github.com/apache/tvm/pull/20057
* [Fix][Relax][ONNX] Correct fmod mapping in Mod constant folding by @shoemoney in https://github.com/apache/tvm/pull/20170
* [BugFix][Relax] Preserve take mode in ReorderTakeAfterMatmul by @katrinagui in https://github.com/apache/tvm/pull/20206
* [Fix][Relax][Frontend][ONNX] Support Shape outputs as Gather indices by @Gunse11er in https://github.com/apache/tvm/pull/20179
* [BugFix][Relax] Skip parallel matmul fusion for mixed output dtypes by @katrinagui in https://github.com/apache/tvm/pull/20208
* [Fix][DLight] Localize private scalar reduction buffers by @SamJSui in https://github.com/apache/tvm/pull/20160
* [Fix][Relax][Frontend][ONNX] Fix Softplus accuracy loss from hardcoded threshold by @siyiweigeHEW in https://github.com/apache/tvm/pull/20212
* [Perf][Arith] Materialize Z3 solvers lazily on first query by @tlopex in https://github.com/apache/tvm/pull/20215
* [Fix][Support] Use sbsa-linux CUDA include dir on ARM64 Linux by @spectrometerHBH in https://github.com/apache/tvm/pull/20222
* [TIRx][CUDA] Support exact required block dimensions by @spectrometerHBH in https://github.com/apache/tvm/pull/20223
* [Fix][Relax][ONNX] Where: broadcast size-1 shape expressions, materialize ShapeExpr inputs by @siyiweigeHEW in https://github.com/apache/tvm/pull/20210
* [Fix][Relax] Skip ReorderPermuteDimsAfterConcat for unknown-rank inputs by @yanght27 in https://github.com/apache/tvm/pull/20216
* [Fix][TIRx] Restore IterVar span reflection by @tlopex in https://github.com/apache/tvm/pull/20214
* [Fix][Relax] Normalize negative indices in Gather/Scatter/OneHot Ops by @OmarAzizi in https://github.com/apache/tvm/pull/20219
* [TIRx][CUDA] Align the PTX dialect with PTX ISA 9.2 by @spectrometerHBH in https://github.com/apache/tvm/pull/20224
* [TIRx][CUDA] Allow launch bounds with required block size by @spectrometerHBH in https://github.com/apache/tvm/pull/20226
* [Fix][Arith] Give each materialized Z3 solver a private context by @tlopex in https://github.com/apache/tvm/pull/20221
* [REFACTOR][TE] Represent tensor loads with opaque callees by @tqchen in https://github.com/apache/tvm/pull/20225
* [CUDA][TIRx] Preserve device state during cleanup and skip invalid Top-K references by @spectrometerHBH in https://github.com/apache/tvm/pull/20233
* [Relax][Frontend][ONNX] Support symbolic shapes in Min/Max broadcast by @cchung100m in https://github.com/apache/tvm/pull/20218
* [Fix][Relax] Preserve match-cast storage liveness by @zupengwang in https://github.com/apache/tvm/pull/20220
* [Fix][Relax][Frontend][ONNX] Support Pad-18 axes input, keep wrap for Pad-19 by @siyiweigeHEW in https://github.com/apache/tvm/pull/20152
* [Fix][TIRx] Preserve index semantics when narrowing to int32 by @akaashrp in https://github.com/apache/tvm/pull/20129
* [Fix][Relax][Torch] Materialize runtime scalar shape values by @akaashrp in https://github.com/apache/tvm/pull/20138
* [Fix][Relax][Frontend][ONNX] Validate Flatten axis range in `from_onnx` by @siyiweigeHEW in https://github.com/apache/tvm/pull/20145
* [REFACTOR][TIR] Split masked buffer access into special calls by @tqchen in https://github.com/apache/tvm/pull/20244
* [Docs][TIRx] Reorganize and align documentation with current APIs by @tlopex in https://github.com/apache/tvm/pull/20209
* [REFACTOR][IR] Introduce TensorLoad in core IR by @tqchen in https://github.com/apache/tvm/pull/20247
* [REFACTOR][IR] Unify expression subscription realization by @tqchen in https://github.com/apache/tvm/pull/20246
* [BugFix] Align default (C) tirx.round lowering to ties-to-even by @LngelKyo in https://github.com/apache/tvm/pull/20131
* [REFACTOR][IR] Consolidate expression operator overloading into the base layer by @tqchen in https://github.com/apache/tvm/pull/20248
* [FIX][IR] Complete lazy subscript realization by @jinhongyii in https://github.com/apache/tvm/pull/20251
* [TIRx][CUDA] Preserve local mbarrier predicate and count by @jinhongyii in https://github.com/apache/tvm/pull/20250
* [REFACTOR][IR] Lift primitive expressions into core IR by @tqchen in https://github.com/apache/tvm/pull/20249
* [Test] Run round ties-to-even test on every backend that implements it by @LngelKyo in https://github.com/apache/tvm/pull/20252
* [REFACTOR][IR] Make expression subscription eager and remove SubscriptProxy by @tqchen in https://github.com/apache/tvm/pull/20257
* [Fix][Relax][Frontend][PyTorch] Fix `x.split(int)` with a non-divisible `split_size` by @siyiweigeHEW in https://github.com/apache/tvm/pull/20240
* [REFACTOR][TIRx] Make BufferRegion a typed expression by @tqchen in https://github.com/apache/tvm/pull/20256
* [BugFix][Arith] Reject padded IterMapSimplify fallback by @zupengwang in https://github.com/apache/tvm/pull/20169
* [Fix][Relax][Frontend][Torch] Honor the `dtype` argument of `aten.mean` (`torch.Tensor.mean` / `torch.mean`) by @siyiweigeHEW in https://github.com/apache/tvm/pull/20241
* [Fix][S-TIR] Preserve general reduction predicates by @akaashrp in https://github.com/apache/tvm/pull/20242
* [Fix][Relax][Metal] Constrain wide-head prefill tiling by @akaashrp in https://github.com/apache/tvm/pull/20235
* [CUDA][TIRx] PTX ISA 9.4 / CUDA 13.4 support for SM103a and SM107a (Rubin) by @spectrometerHBH in https://github.com/apache/tvm/pull/20261
* [CUDA] Add NVIDIA Jetson AGX Thor target tag by @tlopex in https://github.com/apache/tvm/pull/20259
* [Fix][Metal] Bound symbolic stack allocations by @akaashrp in https://github.com/apache/tvm/pull/20236
* [Relax][Frontend][ONNX] Support dynamic Range bounds by @napronald in https://github.com/apache/tvm/pull/20109
* [CUDA][TIRx] Add collector-qualified tcgen05.mma block_scale forms and bind tcgen05.ld.red redval as output by @spectrometerHBH in https://github.com/apache/tvm/pull/20266
* [TIRx][Test] Gate tcgen05.mma collector certification on nvcc >= 13.4 by @spectrometerHBH in https://github.com/apache/tvm/pull/20270
* [CUDA][TIRx] Allow collector-A-only SM107 block-scale MMA and open cp.async wait_group immediates by @spectrometerHBH in https://github.com/apache/tvm/pull/20271
* [TIRx][Test] Gate collector-A-only block-scale MMA test on CUDA 13.4 by @spectrometerHBH in https://github.com/apache/tvm/pull/20276
* [REFACTOR][IR] Add structural hooks for Expr and Stmt by @tqchen in https://github.com/apache/tvm/pull/20275
* [Fix][Relax][Frontend][Torch] Validate flatten dims in `from_fx` by @hiyufan in https://github.com/apache/tvm/pull/20245
* [Test] Pin CUDA round ties-to-even on exact midpoints by @LngelKyo in https://github.com/apache/tvm/pull/20274
* [S-TIR][Test] Use tvm.testing.main() so schedule tests can run standalone by @Anai-Guo in https://github.com/apache/tvm/pull/20283
* [Relax][ONNX] Preserve bool dtype when folding constant comparisons by @StrongbodyStrongmind in https://github.com/apache/tvm/pull/20286
* [Relax][ONNX] Import Min/Max/Sum/Mean when an input has no static shape by @arpitjain099 in https://github.com/apache/tvm/pull/20288
* [Fix][LLVM] Preserve 64-bit AllocBuffer extents by @fallenmi in https://github.com/apache/tvm/pull/20141
* [Fix][Relax] Preserve identity permute_dims in AdjustMatmulOrder by @emecii in https://github.com/apache/tvm/pull/20287
* [TIR] Ignore None-valued pragma annotations by @StrongbodyStrongmind in https://github.com/apache/tvm/pull/20265
* [FFI] Upgrade to latest tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/20294
* [FFI] Bump tvm-ffi for StructuralMap policy by @tqchen in https://github.com/apache/tvm/pull/20299
* [Fix][TIRx] Fix buffer lifetime in LowerWarpMemory by @tlopex in https://github.com/apache/tvm/pull/20295
* [REFACTOR][ARITH] Use StructuralWalk and Map in arith by @tqchen in https://github.com/apache/tvm/pull/20300
* [REFACTOR][TIR] Remove IRTransform in favour of tvm_ffi.structural_map by @tqchen in https://github.com/apache/tvm/pull/20304
* [REFACTOR][Arith] Delete IntGroupBounds::Substitute by @tqchen in https://github.com/apache/tvm/pull/20305
* [REFACTOR][IR] Add structural hooks to remaining Type and Relax Expr nodes by @tqchen in https://github.com/apache/tvm/pull/20302
* [REFACTOR][TIR] Use StructuralWalk in place of PostOrderVisit by @tqchen in https://github.com/apache/tvm/pull/20308
* [REFACTOR][TIR] Inline StructuralWalk at variable-use checks by @tqchen in https://github.com/apache/tvm/pull/20306
* [Fix][Relax] Canonicalize strided slice begin indices by @napronald in https://github.com/apache/tvm/pull/20284
* [Relax] Preserve out_dtype in AdjustMatmulOrder by @StrongbodyStrongmind in https://github.com/apache/tvm/pull/20296
* [Fix][Codegen] Avoid extraneous parentheses in if_then_else generated code by @fengz72 in https://github.com/apache/tvm/pull/20285
* [Relax] Exclude R.null_value()-bound vars from KillAfterLastUse by @cchung100m in https://github.com/apache/tvm/pull/20267
* [Fix][Relax][Frontend][Torch] Support `aten.diagonal` from decomposed repeated-subscript einsum by @siyiweigeHEW in https://github.com/apache/tvm/pull/20237
* [Fix][Relax][Frontend][Torch] Fix `torch.round(x, decimals)` via `from_exported_program` and negative-decimals rounding by @siyiweigeHEW in https://github.com/apache/tvm/pull/20239
* [TOPI] Use branchless boundary index for reflect/replicate pad by @junghyunpark2001 in https://github.com/apache/tvm/pull/19928
* [TIRx][Schedule] Support rfactor for arg reducers selecting last index by @ZephyrLi-pro in https://github.com/apache/tvm/pull/19909
* [REFACTOR][Python] Delete the TIR Py* functor trampoline by @tqchen in https://github.com/apache/tvm/pull/20309
* [Relax][VM] Improve diagnostics for unlowered Relax operators by @yinli-systems in https://github.com/apache/tvm/pull/19899
* [Relax][TensorRT] Build and embed engines during code generation by @zupengwang in https://github.com/apache/tvm/pull/20301
* [Fix][Relax][Frontend][TFLite] Correct quantized SSD inference by @Aharrypotter in https://github.com/apache/tvm/pull/20291
* [Relax][ONNX] Add CastLike support and dynamic-k Trilu to expand backend coverage by @Aharrypotter in https://github.com/apache/tvm/pull/19898
* [REFACTOR][IR] Rename the uniform dispatch table to ObjectFunctor by @tqchen in https://github.com/apache/tvm/pull/20318
* [REFACTOR][TIR] Use StructuralMap in place of Substitute by @tqchen in https://github.com/apache/tvm/pull/20317
* [Relax][PyTorch] Support aten.scatter.src in ExportedProgram importer by @V-aerus in https://github.com/apache/tvm/pull/19935
* [REFACTOR][IR] Colocate type hooks and registrations by @tqchen in https://github.com/apache/tvm/pull/20325
* [REFACTOR][IR] New Functor/Visitor/Mutator Infra at Base Layer by @tqchen in https://github.com/apache/tvm/pull/20327
* [FIX][TIRx][CUDA] Support SM100 weight-stationary B collectors by @jinhongyii in https://github.com/apache/tvm/pull/20329
* [Fix][Relax][Frontend][Torch] Emit int64 indices for sort and argsort by @hiyufan in https://github.com/apache/tvm/pull/20254
* [Relax][cuDNN] Do not offload causal / non-fp16 attention, and fix the default softmax scale by @YangXu1990uiuc in https://github.com/apache/tvm/pull/20078
* [TOPI][CUDA] Fix topk/sort gridDim overflow by remapping grid axes in sort_ir by @cchung100m in https://github.com/apache/tvm/pull/19900
* [ONNX] Preserve integer Div constant-fold precision by @Nanmur in https://github.com/apache/tvm/pull/20324
* [ONNX] Fix initializer prefix stripping by @Nanmur in https://github.com/apache/tvm/pull/20323
* [REFACTOR][IR] Unify structural mutation modes and native traversal entrypoints by @tqchen in https://github.com/apache/tvm/pull/20338
* [REFACTOR] Default mutators to exceptions and migrate arithmetic passes by @tqchen in https://github.com/apache/tvm/pull/20339
* [CLEANUP][IR] Simplify exception-first traversal by @tqchen in https://github.com/apache/tvm/pull/20347
* [Fix][Relax][Frontend][Torch] Keep zero-sized dims when reshaping by @hiyufan in https://github.com/apache/tvm/pull/20255
* [REFACTOR][IR] Share checked PrimVar view across dialects by @tqchen in https://github.com/apache/tvm/pull/20348
* [REFACTOR][Arith] Inline bound-check Ramp expression by @tqchen in https://github.com/apache/tvm/pull/20349
* [REFACTOR][S-TIR] Preserve schedule error payloads across FFI bridges by @tqchen in https://github.com/apache/tvm/pull/20351
* [Fix][Relax][Frontend][Torch] Validate `num_classes` in the `one_hot` converters by @siyiweigeHEW in https://github.com/apache/tvm/pull/20320
* [TIRx][CUDA] Add the declared synchronization-word wait by @Irfnfnkemed in https://github.com/apache/tvm/pull/20353
* [REFACTOR][TIRx] Migrate visitors to shared expression traversal by @tqchen in https://github.com/apache/tvm/pull/20350
* [REFACTOR][Arith] Evaluate iterator domains through Var maps by @tqchen in https://github.com/apache/tvm/pull/20354
* [Refactor][Arith] Move conditional bounds into S-TIR by @tqchen in https://github.com/apache/tvm/pull/20355
* [Arith] Remove vscale-specific simplification and analysis by @tqchen in https://github.com/apache/tvm/pull/20357
* [Frontend][PyTorch] Simplify tests and support exported assertions by @tlopex in https://github.com/apache/tvm/pull/20360
* [IR][TE] Share expression effects and register tensor loads by @tqchen in https://github.com/apache/tvm/pull/20359
* [REFACTOR][RELAX] Own global device metadata in Relax by @tqchen in https://github.com/apache/tvm/pull/20363
* [REFACTOR][TIRX] Share generic expression functor dispatch by @tqchen in https://github.com/apache/tvm/pull/20358
* [Refactor][IR] Move ExprDeepEqual into shared primitive expressions by @tqchen in https://github.com/apache/tvm/pull/20356
* [IR] Make function attribute updates generic via reflected shallow copy by @tqchen in https://github.com/apache/tvm/pull/20366
* [REFACTOR][TIRX] Use single-inheritance typed StmtExprMutator by @tqchen in https://github.com/apache/tvm/pull/20365
* [REFACTOR][IR] Share primitive helpers and Python expressions by @tqchen in https://github.com/apache/tvm/pull/20364
* [CLEANUP][IR][Arith] Move CLZ to shared prim and remove dialect dependencies by @tqchen in https://github.com/apache/tvm/pull/20367
* [REFACTOR][IR] Move dialect and codegen registrations to their owners by @tqchen in https://github.com/apache/tvm/pull/20368
* [REFACTOR][IR] Share tensor region expressions across dialects by @tqchen in https://github.com/apache/tvm/pull/20369
* [REFACTOR][TIRX] Migrate StmtFunctor dispatch and organize analyzer helpers by @tqchen in https://github.com/apache/tvm/pull/20370
* [Fix][cuDNN] Avoid thread-local workspace pool for ConvEntry by @PengYoun9 in https://github.com/apache/tvm/pull/20362
* [IR][Arith] Use BigInt-backed integer immediates and wide coefficients by @tqchen in https://github.com/apache/tvm/pull/20371
* [CLEANUP][IR] Remove redundant functor helpers and CLZ float handling by @tqchen in https://github.com/apache/tvm/pull/20379
* [Arith] Use native GCD for fitting BigInt operands by @tqchen in https://github.com/apache/tvm/pull/20380
* Move S-TIR specific node and TensorIntrin out of TIRX by @tqchen in https://github.com/apache/tvm/pull/20378
* [REFACTOR][IR] Move declared call results into TIRX builders by @tqchen in https://github.com/apache/tvm/pull/20382
* [REFACTOR] Rename shared symbolic analysis namespace to sym by @tqchen in https://github.com/apache/tvm/pull/20381
* [REFACTOR][IR] Unify constants with GenericConst and shared StringImm by @tqchen in https://github.com/apache/tvm/pull/20386
* [FIX] Update v0.27.0 versions and FFI floor by @MasterJH5574 in https://github.com/apache/tvm/pull/20390

## New Contributors
* @hahalfx made their first contribution in https://github.com/apache/tvm/pull/20091
* @adityasingh2400 made their first contribution in https://github.com/apache/tvm/pull/20092
* @GY-Bai made their first contribution in https://github.com/apache/tvm/pull/20101
* @aryanputta made their first contribution in https://github.com/apache/tvm/pull/20119
* @SamJSui made their first contribution in https://github.com/apache/tvm/pull/20158
* @Gunse11er made their first contribution in https://github.com/apache/tvm/pull/20116
* @chenmiaoming made their first contribution in https://github.com/apache/tvm/pull/20108
* @tandede made their first contribution in https://github.com/apache/tvm/pull/20161
* @siyiweigeHEW made their first contribution in https://github.com/apache/tvm/pull/20147
* @Junius-Wynn made their first contribution in https://github.com/apache/tvm/pull/20057
* @shoemoney made their first contribution in https://github.com/apache/tvm/pull/20170
* @katrinagui made their first contribution in https://github.com/apache/tvm/pull/20206
* @yanght27 made their first contribution in https://github.com/apache/tvm/pull/20216
* @zupengwang made their first contribution in https://github.com/apache/tvm/pull/20220
* @LngelKyo made their first contribution in https://github.com/apache/tvm/pull/20131
* @hiyufan made their first contribution in https://github.com/apache/tvm/pull/20245
* @Anai-Guo made their first contribution in https://github.com/apache/tvm/pull/20283
* @StrongbodyStrongmind made their first contribution in https://github.com/apache/tvm/pull/20286
* @arpitjain099 made their first contribution in https://github.com/apache/tvm/pull/20288
* @fallenmi made their first contribution in https://github.com/apache/tvm/pull/20141
* @emecii made their first contribution in https://github.com/apache/tvm/pull/20287
* @fengz72 made their first contribution in https://github.com/apache/tvm/pull/20285
* @junghyunpark2001 made their first contribution in https://github.com/apache/tvm/pull/19928
* @YangXu1990uiuc made their first contribution in https://github.com/apache/tvm/pull/20078
* @Irfnfnkemed made their first contribution in https://github.com/apache/tvm/pull/20353
* @PengYoun9 made their first contribution in https://github.com/apache/tvm/pull/20362

**Full Changelog**: https://github.com/apache/tvm/compare/v0.26.0...v0.27.0.rc0

## v0.27.0.rc1 (2026-09-22)

## What's Changed
* [Web] Bump tvmjs version to 0.27.0-dev0 on main by @MasterJH5574 in https://github.com/apache/tvm/pull/20095
* [Fix][Relax][ONNX] Handle Split initializer with keep_params_in_input by @hahalfx in https://github.com/apache/tvm/pull/20091
* [Fix][Arith] Isolate Z3 contexts and make memoization deterministic by @tlopex in https://github.com/apache/tvm/pull/20097
* [Fix][TIRx] Fix MSVC build of IndexDataTypeNormalizer by @MasterJH5574 in https://github.com/apache/tvm/pull/20098
* [Python] Bump apache-tvm-ffi floor to >=0.1.13.post2 by @MasterJH5574 in https://github.com/apache/tvm/pull/20094
* [FIX][TIRx] Traverse pointer expressions in tile calls by @jinhongyii in https://github.com/apache/tvm/pull/20089
* [FIX][TIRx] Remap typed buffer expressions during specialization by @jinhongyii in https://github.com/apache/tvm/pull/20090
* [FIX][Relax][ONNX] Keep the static shape of a rank-0 Shape input by @adityasingh2400 in https://github.com/apache/tvm/pull/20092
* [FIX][TIRx] Use typed buffer parameter in pointer config test by @tqchen in https://github.com/apache/tvm/pull/20102
* [FIX][CUDA] Select NVRTC architecture for output format by @jinhongyii in https://github.com/apache/tvm/pull/20100
* [TIRx][CUDA] Add a table-driven PTX dialect and retire tirx.ptx.* by @spectrometerHBH in https://github.com/apache/tvm/pull/20103
* [BugFix][Metal] Preserve pointer address spaces for byte offsets by @GY-Bai in https://github.com/apache/tvm/pull/20101
* [TIRx][CUDA] uint32 index dtypes, directive fixes, and PTX ISA coverage by @spectrometerHBH in https://github.com/apache/tvm/pull/20110
* [SCRIPT] Support PEP 695 symbolic variables in Relax and TIR by @tqchen in https://github.com/apache/tvm/pull/20107
* [Fix][WebGPU] Preserve read-only buffer access modes by @akaashrp in https://github.com/apache/tvm/pull/20113
* [Relax][ONNX] Support lower-rank PRelu slopes by @Aharrypotter in https://github.com/apache/tvm/pull/20115
* [TIRX] Split backend.cuda.intrinsics, fold tcgen05 descriptors, and fix two PTX dialect gaps by @spectrometerHBH in https://github.com/apache/tvm/pull/20120
* [Feature][Relax] Support shared-KV attention with configurable sliding windows by @akaashrp in https://github.com/apache/tvm/pull/20121
* [Web] Avoid redundant memory byte copies by @akaashrp in https://github.com/apache/tvm/pull/20127
* [TIRx][CUDA] Replace source helpers with typed PTX forms by @jinhongyii in https://github.com/apache/tvm/pull/20140
* [Fix][DLight] Reject GEMV accesses unsupported by scheduling by @akaashrp in https://github.com/apache/tvm/pull/20122
* [Fix][Relax][ONNX] Fold Min/Max/Sum/Mean constants elementwise by @aryanputta in https://github.com/apache/tvm/pull/20119
* [Relax][Frontend][TFLite] Support StableHLO shape ops by @Aharrypotter in https://github.com/apache/tvm/pull/20114
* [TIRx][CUDA] Version-gate CUDA 12.8 tensor-map enums and fix registry-test lock leak by @spectrometerHBH in https://github.com/apache/tvm/pull/20154
* [TIRx][CUDA] Add PTX address expressions with immediate byte offsets by @spectrometerHBH in https://github.com/apache/tvm/pull/20153
* [Fix][DLight] Handle rank-one GEMV cache loads by @SamJSui in https://github.com/apache/tvm/pull/20158
* [Relax][ONNX] Support scalar QDQ inputs by @Aharrypotter in https://github.com/apache/tvm/pull/20126
* [BugFix][TE] Initialize nested reductions at the outermost reduction scope by @Gunse11er in https://github.com/apache/tvm/pull/20116
* [Fix][Relax] Track lowered reshape storage aliases by @akaashrp in https://github.com/apache/tvm/pull/20134
* [Fix][WebGPU] Validate and bound symbolic stack allocations by @akaashrp in https://github.com/apache/tvm/pull/20132
* [Web] Avoid tensor-cache record copies by @akaashrp in https://github.com/apache/tvm/pull/20156
* [Fix][TOPI] Fuse GPU scan blocks to avoid CUDA gridDim.y overflow by @chenmiaoming in https://github.com/apache/tvm/pull/20108
* [TIRx][CUDA] Add register and cluster launch controls by @spectrometerHBH in https://github.com/apache/tvm/pull/20159
* [Fix][Relax][Torch] Preserve derived exported input dimensions by @akaashrp in https://github.com/apache/tvm/pull/20128
* [Web] Avoid copies when uploading WASM memory to WebGPU by @akaashrp in https://github.com/apache/tvm/pull/20165
* [Web] Upload pass-through tensor-cache records directly to WebGPU by @akaashrp in https://github.com/apache/tvm/pull/20166
* [IR][TIRX] Add first-class tuple expressions by @tqchen in https://github.com/apache/tvm/pull/20168
* [TIRx][CUDA] Allow newer CUTLASS packages for IKET by @jinhongyii in https://github.com/apache/tvm/pull/20164
* [Fix][Relax] Honor ONNX Reshape zero semantics by @tandede in https://github.com/apache/tvm/pull/20161
* [TIRx][CUDA] Fix single-CTA clusterCtaIdx resolution and accept packed sub-byte tensor-map dtypes by @spectrometerHBH in https://github.com/apache/tvm/pull/20172
* feat(lower-tirx): support PTX movmatrix by @spectrometerHBH in https://github.com/apache/tvm/pull/20171
* [Fix][Relax] Run destructors for non-trivially-destructible types in Arena by @OmarAzizi in https://github.com/apache/tvm/pull/20163
* [Fix][Relax] Lower non-contiguous WebGPU cumsum by @akaashrp in https://github.com/apache/tvm/pull/20133
* [TIRx][CUDA] Preserve explicit single-CTA cluster launches by @spectrometerHBH in https://github.com/apache/tvm/pull/20180
* [Fix][Relax][Frontend][ONNX] Fix Mean/Sum/Min/Max with all-constant inputs by @siyiweigeHEW in https://github.com/apache/tvm/pull/20147
* [Runtime] Add PagedAttentionKVCache checkpoint primitives by @akaashrp in https://github.com/apache/tvm/pull/20035
* [Fix][Relax][Frontend][ONNX] Support broadcastable multi-axis PRelu slopes by @siyiweigeHEW in https://github.com/apache/tvm/pull/20149
* [Fix][Relax][Torch] Align retained expand dimensions by trailing rank by @akaashrp in https://github.com/apache/tvm/pull/20137
* [Fix][Arith] Preserve nested floormod semantics by @tlopex in https://github.com/apache/tvm/pull/20181
* [Feat][Web] Support per-parameter tensor cache encoding by @akaashrp in https://github.com/apache/tvm/pull/20136
* [Codegen][LLVM] Add LLVM 23 compatibility by @tlopex in https://github.com/apache/tvm/pull/20189
* [Web] Decode packed BF16 tensor records in place by @akaashrp in https://github.com/apache/tvm/pull/20167
* [Fix][Relax][Frontend][ONNX] Fix Scatter with indices smaller than data by @siyiweigeHEW in https://github.com/apache/tvm/pull/20187
* [Fix][Relax] Raise error on non-unit dim ONNX Squeeze axis by @OmarAzizi in https://github.com/apache/tvm/pull/20188
* fix(tirx): stabilize multi-GPU correctness tests by @spectrometerHBH in https://github.com/apache/tvm/pull/20213
* [Fix][Relax] Preserve tensor-derived symbols during fusion by @akaashrp in https://github.com/apache/tvm/pull/20139
* [Fix][S-TIR][DLight] Guard non-affine reduction write-back by @Junius-Wynn in https://github.com/apache/tvm/pull/20057
* [Fix][Relax][ONNX] Correct fmod mapping in Mod constant folding by @shoemoney in https://github.com/apache/tvm/pull/20170
* [BugFix][Relax] Preserve take mode in ReorderTakeAfterMatmul by @katrinagui in https://github.com/apache/tvm/pull/20206
* [Fix][Relax][Frontend][ONNX] Support Shape outputs as Gather indices by @Gunse11er in https://github.com/apache/tvm/pull/20179
* [BugFix][Relax] Skip parallel matmul fusion for mixed output dtypes by @katrinagui in https://github.com/apache/tvm/pull/20208
* [Fix][DLight] Localize private scalar reduction buffers by @SamJSui in https://github.com/apache/tvm/pull/20160
* [Fix][Relax][Frontend][ONNX] Fix Softplus accuracy loss from hardcoded threshold by @siyiweigeHEW in https://github.com/apache/tvm/pull/20212
* [Perf][Arith] Materialize Z3 solvers lazily on first query by @tlopex in https://github.com/apache/tvm/pull/20215
* [Fix][Support] Use sbsa-linux CUDA include dir on ARM64 Linux by @spectrometerHBH in https://github.com/apache/tvm/pull/20222
* [TIRx][CUDA] Support exact required block dimensions by @spectrometerHBH in https://github.com/apache/tvm/pull/20223
* [Fix][Relax][ONNX] Where: broadcast size-1 shape expressions, materialize ShapeExpr inputs by @siyiweigeHEW in https://github.com/apache/tvm/pull/20210
* [Fix][Relax] Skip ReorderPermuteDimsAfterConcat for unknown-rank inputs by @yanght27 in https://github.com/apache/tvm/pull/20216
* [Fix][TIRx] Restore IterVar span reflection by @tlopex in https://github.com/apache/tvm/pull/20214
* [Fix][Relax] Normalize negative indices in Gather/Scatter/OneHot Ops by @OmarAzizi in https://github.com/apache/tvm/pull/20219
* [TIRx][CUDA] Align the PTX dialect with PTX ISA 9.2 by @spectrometerHBH in https://github.com/apache/tvm/pull/20224
* [TIRx][CUDA] Allow launch bounds with required block size by @spectrometerHBH in https://github.com/apache/tvm/pull/20226
* [Fix][Arith] Give each materialized Z3 solver a private context by @tlopex in https://github.com/apache/tvm/pull/20221
* [REFACTOR][TE] Represent tensor loads with opaque callees by @tqchen in https://github.com/apache/tvm/pull/20225
* [CUDA][TIRx] Preserve device state during cleanup and skip invalid Top-K references by @spectrometerHBH in https://github.com/apache/tvm/pull/20233
* [Relax][Frontend][ONNX] Support symbolic shapes in Min/Max broadcast by @cchung100m in https://github.com/apache/tvm/pull/20218
* [Fix][Relax] Preserve match-cast storage liveness by @zupengwang in https://github.com/apache/tvm/pull/20220
* [Fix][Relax][Frontend][ONNX] Support Pad-18 axes input, keep wrap for Pad-19 by @siyiweigeHEW in https://github.com/apache/tvm/pull/20152
* [Fix][TIRx] Preserve index semantics when narrowing to int32 by @akaashrp in https://github.com/apache/tvm/pull/20129
* [Fix][Relax][Torch] Materialize runtime scalar shape values by @akaashrp in https://github.com/apache/tvm/pull/20138
* [Fix][Relax][Frontend][ONNX] Validate Flatten axis range in `from_onnx` by @siyiweigeHEW in https://github.com/apache/tvm/pull/20145
* [REFACTOR][TIR] Split masked buffer access into special calls by @tqchen in https://github.com/apache/tvm/pull/20244
* [Docs][TIRx] Reorganize and align documentation with current APIs by @tlopex in https://github.com/apache/tvm/pull/20209
* [REFACTOR][IR] Introduce TensorLoad in core IR by @tqchen in https://github.com/apache/tvm/pull/20247
* [REFACTOR][IR] Unify expression subscription realization by @tqchen in https://github.com/apache/tvm/pull/20246
* [BugFix] Align default (C) tirx.round lowering to ties-to-even by @LngelKyo in https://github.com/apache/tvm/pull/20131
* [REFACTOR][IR] Consolidate expression operator overloading into the base layer by @tqchen in https://github.com/apache/tvm/pull/20248
* [FIX][IR] Complete lazy subscript realization by @jinhongyii in https://github.com/apache/tvm/pull/20251
* [TIRx][CUDA] Preserve local mbarrier predicate and count by @jinhongyii in https://github.com/apache/tvm/pull/20250
* [REFACTOR][IR] Lift primitive expressions into core IR by @tqchen in https://github.com/apache/tvm/pull/20249
* [Test] Run round ties-to-even test on every backend that implements it by @LngelKyo in https://github.com/apache/tvm/pull/20252
* [REFACTOR][IR] Make expression subscription eager and remove SubscriptProxy by @tqchen in https://github.com/apache/tvm/pull/20257
* [Fix][Relax][Frontend][PyTorch] Fix `x.split(int)` with a non-divisible `split_size` by @siyiweigeHEW in https://github.com/apache/tvm/pull/20240
* [REFACTOR][TIRx] Make BufferRegion a typed expression by @tqchen in https://github.com/apache/tvm/pull/20256
* [BugFix][Arith] Reject padded IterMapSimplify fallback by @zupengwang in https://github.com/apache/tvm/pull/20169
* [Fix][Relax][Frontend][Torch] Honor the `dtype` argument of `aten.mean` (`torch.Tensor.mean` / `torch.mean`) by @siyiweigeHEW in https://github.com/apache/tvm/pull/20241
* [Fix][S-TIR] Preserve general reduction predicates by @akaashrp in https://github.com/apache/tvm/pull/20242
* [Fix][Relax][Metal] Constrain wide-head prefill tiling by @akaashrp in https://github.com/apache/tvm/pull/20235
* [CUDA][TIRx] PTX ISA 9.4 / CUDA 13.4 support for SM103a and SM107a (Rubin) by @spectrometerHBH in https://github.com/apache/tvm/pull/20261
* [CUDA] Add NVIDIA Jetson AGX Thor target tag by @tlopex in https://github.com/apache/tvm/pull/20259
* [Fix][Metal] Bound symbolic stack allocations by @akaashrp in https://github.com/apache/tvm/pull/20236
* [Relax][Frontend][ONNX] Support dynamic Range bounds by @napronald in https://github.com/apache/tvm/pull/20109
* [CUDA][TIRx] Add collector-qualified tcgen05.mma block_scale forms and bind tcgen05.ld.red redval as output by @spectrometerHBH in https://github.com/apache/tvm/pull/20266
* [TIRx][Test] Gate tcgen05.mma collector certification on nvcc >= 13.4 by @spectrometerHBH in https://github.com/apache/tvm/pull/20270
* [CUDA][TIRx] Allow collector-A-only SM107 block-scale MMA and open cp.async wait_group immediates by @spectrometerHBH in https://github.com/apache/tvm/pull/20271
* [TIRx][Test] Gate collector-A-only block-scale MMA test on CUDA 13.4 by @spectrometerHBH in https://github.com/apache/tvm/pull/20276
* [REFACTOR][IR] Add structural hooks for Expr and Stmt by @tqchen in https://github.com/apache/tvm/pull/20275
* [Fix][Relax][Frontend][Torch] Validate flatten dims in `from_fx` by @hiyufan in https://github.com/apache/tvm/pull/20245
* [Test] Pin CUDA round ties-to-even on exact midpoints by @LngelKyo in https://github.com/apache/tvm/pull/20274
* [S-TIR][Test] Use tvm.testing.main() so schedule tests can run standalone by @Anai-Guo in https://github.com/apache/tvm/pull/20283
* [Relax][ONNX] Preserve bool dtype when folding constant comparisons by @StrongbodyStrongmind in https://github.com/apache/tvm/pull/20286
* [Relax][ONNX] Import Min/Max/Sum/Mean when an input has no static shape by @arpitjain099 in https://github.com/apache/tvm/pull/20288
* [Fix][LLVM] Preserve 64-bit AllocBuffer extents by @fallenmi in https://github.com/apache/tvm/pull/20141
* [Fix][Relax] Preserve identity permute_dims in AdjustMatmulOrder by @emecii in https://github.com/apache/tvm/pull/20287
* [TIR] Ignore None-valued pragma annotations by @StrongbodyStrongmind in https://github.com/apache/tvm/pull/20265
* [FFI] Upgrade to latest tvm-ffi by @tqchen in https://github.com/apache/tvm/pull/20294
* [FFI] Bump tvm-ffi for StructuralMap policy by @tqchen in https://github.com/apache/tvm/pull/20299
* [Fix][TIRx] Fix buffer lifetime in LowerWarpMemory by @tlopex in https://github.com/apache/tvm/pull/20295
* [REFACTOR][ARITH] Use StructuralWalk and Map in arith by @tqchen in https://github.com/apache/tvm/pull/20300
* [REFACTOR][TIR] Remove IRTransform in favour of tvm_ffi.structural_map by @tqchen in https://github.com/apache/tvm/pull/20304
* [REFACTOR][Arith] Delete IntGroupBounds::Substitute by @tqchen in https://github.com/apache/tvm/pull/20305
* [REFACTOR][IR] Add structural hooks to remaining Type and Relax Expr nodes by @tqchen in https://github.com/apache/tvm/pull/20302
* [REFACTOR][TIR] Use StructuralWalk in place of PostOrderVisit by @tqchen in https://github.com/apache/tvm/pull/20308
* [REFACTOR][TIR] Inline StructuralWalk at variable-use checks by @tqchen in https://github.com/apache/tvm/pull/20306
* [Fix][Relax] Canonicalize strided slice begin indices by @napronald in https://github.com/apache/tvm/pull/20284
* [Relax] Preserve out_dtype in AdjustMatmulOrder by @StrongbodyStrongmind in https://github.com/apache/tvm/pull/20296
* [Fix][Codegen] Avoid extraneous parentheses in if_then_else generated code by @fengz72 in https://github.com/apache/tvm/pull/20285
* [Relax] Exclude R.null_value()-bound vars from KillAfterLastUse by @cchung100m in https://github.com/apache/tvm/pull/20267
* [Fix][Relax][Frontend][Torch] Support `aten.diagonal` from decomposed repeated-subscript einsum by @siyiweigeHEW in https://github.com/apache/tvm/pull/20237
* [Fix][Relax][Frontend][Torch] Fix `torch.round(x, decimals)` via `from_exported_program` and negative-decimals rounding by @siyiweigeHEW in https://github.com/apache/tvm/pull/20239
* [TOPI] Use branchless boundary index for reflect/replicate pad by @junghyunpark2001 in https://github.com/apache/tvm/pull/19928
* [TIRx][Schedule] Support rfactor for arg reducers selecting last index by @ZephyrLi-pro in https://github.com/apache/tvm/pull/19909
* [REFACTOR][Python] Delete the TIR Py* functor trampoline by @tqchen in https://github.com/apache/tvm/pull/20309
* [Relax][VM] Improve diagnostics for unlowered Relax operators by @yinli-systems in https://github.com/apache/tvm/pull/19899
* [Relax][TensorRT] Build and embed engines during code generation by @zupengwang in https://github.com/apache/tvm/pull/20301
* [Fix][Relax][Frontend][TFLite] Correct quantized SSD inference by @Aharrypotter in https://github.com/apache/tvm/pull/20291
* [Relax][ONNX] Add CastLike support and dynamic-k Trilu to expand backend coverage by @Aharrypotter in https://github.com/apache/tvm/pull/19898
* [REFACTOR][IR] Rename the uniform dispatch table to ObjectFunctor by @tqchen in https://github.com/apache/tvm/pull/20318
* [REFACTOR][TIR] Use StructuralMap in place of Substitute by @tqchen in https://github.com/apache/tvm/pull/20317
* [Relax][PyTorch] Support aten.scatter.src in ExportedProgram importer by @V-aerus in https://github.com/apache/tvm/pull/19935
* [REFACTOR][IR] Colocate type hooks and registrations by @tqchen in https://github.com/apache/tvm/pull/20325
* [REFACTOR][IR] New Functor/Visitor/Mutator Infra at Base Layer by @tqchen in https://github.com/apache/tvm/pull/20327
* [FIX][TIRx][CUDA] Support SM100 weight-stationary B collectors by @jinhongyii in https://github.com/apache/tvm/pull/20329
* [Fix][Relax][Frontend][Torch] Emit int64 indices for sort and argsort by @hiyufan in https://github.com/apache/tvm/pull/20254
* [Relax][cuDNN] Do not offload causal / non-fp16 attention, and fix the default softmax scale by @YangXu1990uiuc in https://github.com/apache/tvm/pull/20078
* [TOPI][CUDA] Fix topk/sort gridDim overflow by remapping grid axes in sort_ir by @cchung100m in https://github.com/apache/tvm/pull/19900
* [ONNX] Preserve integer Div constant-fold precision by @Nanmur in https://github.com/apache/tvm/pull/20324
* [ONNX] Fix initializer prefix stripping by @Nanmur in https://github.com/apache/tvm/pull/20323
* [REFACTOR][IR] Unify structural mutation modes and native traversal entrypoints by @tqchen in https://github.com/apache/tvm/pull/20338
* [REFACTOR] Default mutators to exceptions and migrate arithmetic passes by @tqchen in https://github.com/apache/tvm/pull/20339
* [CLEANUP][IR] Simplify exception-first traversal by @tqchen in https://github.com/apache/tvm/pull/20347
* [Fix][Relax][Frontend][Torch] Keep zero-sized dims when reshaping by @hiyufan in https://github.com/apache/tvm/pull/20255
* [REFACTOR][IR] Share checked PrimVar view across dialects by @tqchen in https://github.com/apache/tvm/pull/20348
* [REFACTOR][Arith] Inline bound-check Ramp expression by @tqchen in https://github.com/apache/tvm/pull/20349
* [REFACTOR][S-TIR] Preserve schedule error payloads across FFI bridges by @tqchen in https://github.com/apache/tvm/pull/20351
* [Fix][Relax][Frontend][Torch] Validate `num_classes` in the `one_hot` converters by @siyiweigeHEW in https://github.com/apache/tvm/pull/20320
* [TIRx][CUDA] Add the declared synchronization-word wait by @Irfnfnkemed in https://github.com/apache/tvm/pull/20353
* [REFACTOR][TIRx] Migrate visitors to shared expression traversal by @tqchen in https://github.com/apache/tvm/pull/20350
* [REFACTOR][Arith] Evaluate iterator domains through Var maps by @tqchen in https://github.com/apache/tvm/pull/20354
* [Refactor][Arith] Move conditional bounds into S-TIR by @tqchen in https://github.com/apache/tvm/pull/20355
* [Arith] Remove vscale-specific simplification and analysis by @tqchen in https://github.com/apache/tvm/pull/20357
* [Frontend][PyTorch] Simplify tests and support exported assertions by @tlopex in https://github.com/apache/tvm/pull/20360
* [IR][TE] Share expression effects and register tensor loads by @tqchen in https://github.com/apache/tvm/pull/20359
* [REFACTOR][RELAX] Own global device metadata in Relax by @tqchen in https://github.com/apache/tvm/pull/20363
* [REFACTOR][TIRX] Share generic expression functor dispatch by @tqchen in https://github.com/apache/tvm/pull/20358
* [Refactor][IR] Move ExprDeepEqual into shared primitive expressions by @tqchen in https://github.com/apache/tvm/pull/20356
* [IR] Make function attribute updates generic via reflected shallow copy by @tqchen in https://github.com/apache/tvm/pull/20366
* [REFACTOR][TIRX] Use single-inheritance typed StmtExprMutator by @tqchen in https://github.com/apache/tvm/pull/20365
* [REFACTOR][IR] Share primitive helpers and Python expressions by @tqchen in https://github.com/apache/tvm/pull/20364
* [CLEANUP][IR][Arith] Move CLZ to shared prim and remove dialect dependencies by @tqchen in https://github.com/apache/tvm/pull/20367
* [REFACTOR][IR] Move dialect and codegen registrations to their owners by @tqchen in https://github.com/apache/tvm/pull/20368
* [REFACTOR][IR] Share tensor region expressions across dialects by @tqchen in https://github.com/apache/tvm/pull/20369
* [REFACTOR][TIRX] Migrate StmtFunctor dispatch and organize analyzer helpers by @tqchen in https://github.com/apache/tvm/pull/20370
* [Fix][cuDNN] Avoid thread-local workspace pool for ConvEntry by @PengYoun9 in https://github.com/apache/tvm/pull/20362
* [IR][Arith] Use BigInt-backed integer immediates and wide coefficients by @tqchen in https://github.com/apache/tvm/pull/20371
* [CLEANUP][IR] Remove redundant functor helpers and CLZ float handling by @tqchen in https://github.com/apache/tvm/pull/20379
* [Arith] Use native GCD for fitting BigInt operands by @tqchen in https://github.com/apache/tvm/pull/20380
* Move S-TIR specific node and TensorIntrin out of TIRX by @tqchen in https://github.com/apache/tvm/pull/20378
* [REFACTOR][IR] Move declared call results into TIRX builders by @tqchen in https://github.com/apache/tvm/pull/20382
* [REFACTOR] Rename shared symbolic analysis namespace to sym by @tqchen in https://github.com/apache/tvm/pull/20381
* [REFACTOR][IR] Unify constants with GenericConst and shared StringImm by @tqchen in https://github.com/apache/tvm/pull/20386
* [FIX] Update v0.27.0 versions and FFI floor by @MasterJH5574 in https://github.com/apache/tvm/pull/20390
* [REFACTOR][IR] Promote primitive bitwise and shift operations to nodes by @tqchen in https://github.com/apache/tvm/pull/20392
* [FIX][TIRx] Avoid stale constraints from mutable memory predicates by @tlopex in https://github.com/apache/tvm/pull/20393
* [TIRx][CUDA] Preserve kernel launch calls and add CUDA host source bundling by @tqchen in https://github.com/apache/tvm/pull/20395
* [Fix][Metal][WebGPU] Preserve variable bindings when resolving allocation bounds by @akaashrp in https://github.com/apache/tvm/pull/20337
* [Fix][Relax] Allow callers to specify scan index-width budget by @akaashrp in https://github.com/apache/tvm/pull/20336
* [REFACTOR][TIRx] Group buffer APIs and remove generic composition by @tqchen in https://github.com/apache/tvm/pull/20402

## New Contributors
* @hahalfx made their first contribution in https://github.com/apache/tvm/pull/20091
* @adityasingh2400 made their first contribution in https://github.com/apache/tvm/pull/20092
* @GY-Bai made their first contribution in https://github.com/apache/tvm/pull/20101
* @aryanputta made their first contribution in https://github.com/apache/tvm/pull/20119
* @SamJSui made their first contribution in https://github.com/apache/tvm/pull/20158
* @Gunse11er made their first contribution in https://github.com/apache/tvm/pull/20116
* @chenmiaoming made their first contribution in https://github.com/apache/tvm/pull/20108
* @tandede made their first contribution in https://github.com/apache/tvm/pull/20161
* @siyiweigeHEW made their first contribution in https://github.com/apache/tvm/pull/20147
* @Junius-Wynn made their first contribution in https://github.com/apache/tvm/pull/20057
* @shoemoney made their first contribution in https://github.com/apache/tvm/pull/20170
* @katrinagui made their first contribution in https://github.com/apache/tvm/pull/20206
* @yanght27 made their first contribution in https://github.com/apache/tvm/pull/20216
* @zupengwang made their first contribution in https://github.com/apache/tvm/pull/20220
* @LngelKyo made their first contribution in https://github.com/apache/tvm/pull/20131
* @hiyufan made their first contribution in https://github.com/apache/tvm/pull/20245
* @Anai-Guo made their first contribution in https://github.com/apache/tvm/pull/20283
* @StrongbodyStrongmind made their first contribution in https://github.com/apache/tvm/pull/20286
* @arpitjain099 made their first contribution in https://github.com/apache/tvm/pull/20288
* @fallenmi made their first contribution in https://github.com/apache/tvm/pull/20141
* @emecii made their first contribution in https://github.com/apache/tvm/pull/20287
* @fengz72 made their first contribution in https://github.com/apache/tvm/pull/20285
* @junghyunpark2001 made their first contribution in https://github.com/apache/tvm/pull/19928
* @YangXu1990uiuc made their first contribution in https://github.com/apache/tvm/pull/20078
* @Irfnfnkemed made their first contribution in https://github.com/apache/tvm/pull/20353
* @PengYoun9 made their first contribution in https://github.com/apache/tvm/pull/20362

**Full Changelog**: https://github.com/apache/tvm/compare/v0.26.0...v0.27.0.rc1
