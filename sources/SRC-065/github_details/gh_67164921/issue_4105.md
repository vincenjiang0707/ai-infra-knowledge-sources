# [Issue #4105] [AMD] Undefined behavior sanitizer invalid-bool-load in optimize_epilogue.mlir

source: https://github.com/triton-lang/triton/issues/4105
state: closed | updated: 2026-09-19T03:50:15Z
labels: bug, help wanted

## 正文

This is an AMD-only test, which we don't have the bandwidth to look at at the moment, but our sanitizers detected an issue with it. So filing this in case someone on the AMD side wants to fix it. Here is the stack trace:

```
RUN: triton-opt %s -split-input-file --tritonamdgpu-optimize-epilogue | FileCheck --check-prefixes=GCN %s
[FAIL]
triton-opt third_party/triton/test/TritonGPU/optimize_epilogue.mlir -split-input-file --tritonamdgpu-optimize-epilogue | FileCheck --check-prefixes=GCN 
third_party/triton/test/TritonGPU/optimize_epilogue.mlir
third_party/llvm/llvm-project/mlir/include/mlir/IR/OpImplementation.h:910:26: runtime error: load of value 120, which is not a valid value for type 'bool'

    #0 0x55d960663da5 in auto mlir::AsmParser::getChecked<mlir::triton::gpu::AMDMfmaEncodingAttr, mlir::MLIRContext*, unsigned int&, unsigned int&, llvm::SmallVector<unsigned int, 12u>&, unsigned int&, unsigned int&, bool&, mlir::triton::gpu::CTALayoutAttr&>(mlir::MLIRContext*&&, unsigned int&, unsigned int&, llvm::SmallVector<unsigned int, 12u>&, unsigned int&, unsigned int&, bool&, mlir::triton::gpu::CTALayoutAttr&) third_party/llvm/llvm-project/mlir/include/mlir/IR/OpImplementation.h:910:26

    #1 0x55d9606635fe in mlir::triton::gpu::AMDMfmaEncodingAttr::parse(mlir::AsmParser&, mlir::Type) third_party/triton/lib/Dialect/TritonGPU/IR/Dialect.cpp:1426:17

    #2 0x55d9606588c9 in operator() blaze-out/k8-opt-cuda12/bin/third_party/triton/include/triton/Dialect/TritonGPU/IR/TritonGPUAttrDefs.cpp.inc:39:15

    #3 0x55d9606588c9 in Case<(lambda at blaze-out/k8-opt-cuda12/bin/third_party/triton/include/triton/Dialect/TritonGPU/IR/TritonGPUAttrDefs.cpp.inc:38:68)> third_party/llvm/llvm-project/mlir/include/mlir/IR/OpImplementation.h:820:34

    #4 0x55d9606588c9 in generatedAttributeParser blaze-out/k8-opt-cuda12/bin/third_party/triton/include/triton/Dialect/TritonGPU/IR/TritonGPUAttrDefs.cpp.inc:38:6

    #5 0x55d9606588c9 in mlir::triton::gpu::TritonGPUDialect::parseAttribute(mlir::DialectAsmParser&, mlir::Type) const blaze-out/k8-opt-cuda12/bin/third_party/triton/include/triton/Dialect/TritonGPU/IR/TritonGPUAttrDefs.cpp.inc:1203:24

    #6 0x55d961812052 in operator() third_party/llvm/llvm-project/mlir/lib/AsmParser/DialectSymbolParser.cpp:272:37

    #7 0x55d961812052 in parseExtendedSymbol<mlir::Attribute, llvm::StringMap<mlir::Attribute, llvm::MallocAllocator>, (lambda at third_party/llvm/llvm-project/mlir/lib/AsmParser/DialectSymbolParser.cpp:257:7)> third_party/llvm/llvm-project/mlir/lib/AsmParser/DialectSymbolParser.cpp:242:10

    #8 0x55d961812052 in mlir::detail::Parser::parseExtendedAttr(mlir::Type) third_party/llvm/llvm-project/mlir/lib/AsmParser/DialectSymbolParser.cpp:255:20

    #9 0x55d9618230ff in mlir::detail::Parser::parseAttribute(mlir::Type) third_party/llvm/llvm-project/mlir/lib/AsmParser/AttributeParser.cpp

    #10 0x55d96183e9c1 in parseAttributeAliasDef third_party/llvm/llvm-project/mlir/lib/AsmParser/Parser.cpp:2572:20

    #11 0x55d96183e9c1 in parse third_party/llvm/llvm-project/mlir/lib/AsmParser/Parser.cpp:2752:11

    #12 0x55d96183e9c1 in mlir::parseAsmSourceFile(llvm::SourceMgr const&, mlir::Block*, mlir::ParserConfig const&, mlir::AsmParserState*, mlir::AsmParserCodeCompleteContext*) third_party/llvm/llvm-project/mlir/lib/AsmParser/Parser.cpp:2786:41

    #13 0x55d9617f21a2 in mlir::parseSourceFile(std::__u::shared_ptr<llvm::SourceMgr> const&, mlir::Block*, mlir::ParserConfig const&, mlir::LocationAttr*) third_party/llvm/llvm-project/mlir/lib/Parser/Parser.cpp:46:10

    #14 0x55d961292c02 in parseSourceFile<mlir::ModuleOp, const std::__u::shared_ptr<llvm::SourceMgr> &> third_party/llvm/llvm-project/mlir/include/mlir/Parser/Parser.h:159:14

    #15 0x55d961292c02 in parseSourceFile<mlir::ModuleOp> third_party/llvm/llvm-project/mlir/include/mlir/Parser/Parser.h:189:10

    #16 0x55d961292c02 in mlir::parseSourceFileForTool(std::__u::shared_ptr<llvm::SourceMgr> const&, mlir::ParserConfig const&, bool) third_party/llvm/llvm-project/mlir/include/mlir/Tools/ParseUtilities.h:31:12

    #17 0x55d961291e83 in performActions(llvm::raw_ostream&, std::__u::shared_ptr<llvm::SourceMgr> const&, mlir::MLIRContext*, mlir::MlirOptMainConfig const&) third_party/llvm/llvm-project/mlir/lib/Tools/mlir-opt/MlirOptMain.cpp:384:33

    #18 0x55d9612918f8 in processBuffer third_party/llvm/llvm-project/mlir/lib/Tools/mlir-opt/MlirOptMain.cpp:474:12

    #19 0x55d9612918f8 in operator() third_party/llvm/llvm-project/mlir/lib/Tools/mlir-opt/MlirOptMain.cpp:549:12

    #20 0x55d9612918f8 in mlir::LogicalResult llvm::function_ref<mlir::LogicalResult (std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, llvm::raw_ostream&)>::callback_fn<mlir::MlirOptMain(llvm::raw_ostream&, std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, mlir::DialectRegistry&, mlir::MlirOptMainConfig const&)::$_0>(long, std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, llvm::raw_ostream&) third_party/llvm/llvm-project/llvm/include/llvm/ADT/STLFunctionalExtras.h:45:12

    #21 0x55d9619e17ce in operator() third_party/llvm/llvm-project/llvm/include/llvm/ADT/STLFunctionalExtras.h:68:12

    #22 0x55d9619e17ce in mlir::splitAndProcessBuffer(std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, llvm::function_ref<mlir::LogicalResult (std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, llvm::raw_ostream&)>, llvm::raw_ostream&, llvm::StringRef, llvm::StringRef)::$_0::operator()(llvm::StringRef) const third_party/llvm/llvm-project/mlir/lib/Support/ToolUtilities.cpp:87:16

    #23 0x55d9619e1195 in interleave<const llvm::StringRef *, (lambda at third_party/llvm/llvm-project/mlir/lib/Support/ToolUtilities.cpp:80:23), (lambda at third_party/llvm/llvm-project/llvm/include/llvm/ADT/STLExtras.h:2147:49), void> third_party/llvm/llvm-project/llvm/include/llvm/ADT/STLExtras.h:2125:3

    #24 0x55d9619e1195 in interleave<llvm::SmallVector<llvm::StringRef, 8U>, (lambda at third_party/llvm/llvm-project/mlir/lib/Support/ToolUtilities.cpp:80:23), llvm::raw_ostream, llvm::StringRef> third_party/llvm/llvm-project/llvm/include/llvm/ADT/STLExtras.h:2147:3

    #25 0x55d9619e1195 in mlir::splitAndProcessBuffer(std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, llvm::function_ref<mlir::LogicalResult (std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, llvm::raw_ostream&)>, llvm::raw_ostream&, llvm::StringRef, llvm::StringRef) third_party/llvm/llvm-project/mlir/lib/Support/ToolUtilities.cpp:90:3

    #26 0x55d961289a70 in mlir::MlirOptMain(llvm::raw_ostream&, std::__u::unique_ptr<llvm::MemoryBuffer, std::__u::default_delete<llvm::MemoryBuffer>>, mlir::DialectRegistry&, mlir::MlirOptMainConfig const&) third_party/llvm/llvm-project/mlir/lib/Tools/mlir-opt/MlirOptMain.cpp:552:10

    #27 0x55d961289edc in mlir::MlirOptMain(int, char**, llvm::StringRef, llvm::StringRef, mlir::DialectRegistry&) third_party/llvm/llvm-project/mlir/lib/Tools/mlir-opt/MlirOptMain.cpp:590:14

    #28 0x55d96128a378 in mlir::MlirOptMain(int, char**, llvm::StringRef, mlir::DialectRegistry&) third_party/llvm/llvm-project/mlir/lib/Tools/mlir-opt/MlirOptMain.cpp:606:10

    #29 0x55d95c5967e4 in main third_party/triton/bin/triton-opt.cpp:9:33

SUMMARY: UndefinedBehaviorSanitizer: invalid-bool-load third_party/llvm/llvm-project/mlir/include/mlir/IR/OpImplementation.h:910:26
```

## 评论 (5)

### zhanglx13 · 2024-06-10

Could you share the input ir for this pass? I cannot find `third_party/triton/test/TritonGPU/optimize_epilogue.mlir`.

### ThomasRaoux · 2024-06-10

This is the test:
https://github.com/triton-lang/triton/blob/main/test/TritonGPU/optimize_epilogue.mlir

### zhanglx13 · 2024-06-10

> This is the test: https://github.com/triton-lang/triton/blob/main/test/TritonGPU/optimize_epilogue.mlir

This one is test in CI and it works fine. I also tested it on MI300 and it also works fine. 
@gflegar Are you using the latest main branch? And could you share the GPU and rocm version info?

### ThomasRaoux · 2024-06-10

My understanding from the message is that it only fails when running with UB sanitizer (we don't have those runs in CI)

### zhanglx13 · 2024-06-10

> it only fails when running with UB sanitizer (we don't have those runs in CI)

Ah, yes, I missed that part. Thanks for the clarification.
