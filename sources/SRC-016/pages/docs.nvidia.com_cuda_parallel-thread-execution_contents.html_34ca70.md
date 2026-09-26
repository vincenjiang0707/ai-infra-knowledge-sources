source: https://docs.nvidia.com/cuda/parallel-thread-execution/contents.html

# Contents[](https://docs.nvidia.com#contents)

-
[1. Introduction](https://docs.nvidia.com/index.html) -
[2. Programming Model](https://docs.nvidia.com/index.html#programming-model) -
[3. PTX Machine Model](https://docs.nvidia.com/index.html#ptx-machine-model) -
[4. Syntax](https://docs.nvidia.com/index.html#syntax) -
[5. State Spaces, Types, and Variables](https://docs.nvidia.com/index.html#state-spaces-types-and-variables)-
[5.1. State Spaces](https://docs.nvidia.com/index.html#state-spaces) -
[5.2. Types](https://docs.nvidia.com/index.html#types) -
[5.3. Texture Sampler and Surface Types](https://docs.nvidia.com/index.html#texture-sampler-and-surface-types) -
[5.4. Variables](https://docs.nvidia.com/index.html#variables) -
[5.5. Tensors](https://docs.nvidia.com/index.html#tensors)

-
-
[6. Instruction Operands](https://docs.nvidia.com/index.html#instruction-operands) -
[7. Abstracting the ABI](https://docs.nvidia.com/index.html#abstracting-abi) -
[8. Memory Consistency Model](https://docs.nvidia.com/index.html#memory-consistency-model) -
[9. Instruction Set](https://docs.nvidia.com/index.html#instruction-set)[9.1. Format and Semantics of Instruction Descriptions](https://docs.nvidia.com/index.html#format-and-semantics-of-instruction-descriptions)[9.2. PTX Instructions](https://docs.nvidia.com/index.html#ptx-instructions)-
[9.3. Predicated Execution](https://docs.nvidia.com/index.html#predicated-execution) -
[9.4. Type Information for Instructions and Operands](https://docs.nvidia.com/index.html#type-information-for-instructions-and-operands) [9.5. Divergence of Threads in Control Constructs](https://docs.nvidia.com/index.html#divergence-of-threads-in-control-constructs)-
[9.6. Semantics](https://docs.nvidia.com/index.html#semantics) -
[9.7. Instructions](https://docs.nvidia.com/index.html#instructions)-
[9.7.1. Integer Arithmetic Instructions](https://docs.nvidia.com/index.html#integer-arithmetic-instructions)[9.7.1.1. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-add)`add`

[9.7.1.2. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-sub)`sub`

[9.7.1.3. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-mul)`mul`

[9.7.1.4. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-mad)`mad`

[9.7.1.5. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-clmad)`clmad`

[9.7.1.6. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-mul24)`mul24`

[9.7.1.7. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-mad24)`mad24`

[9.7.1.8. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-sad)`sad`

[9.7.1.9. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-div)`div`

[9.7.1.10. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-rem)`rem`

[9.7.1.11. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-abs)`abs`

[9.7.1.12. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-neg)`neg`

[9.7.1.13. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-min)`min`

[9.7.1.14. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-max)`max`

[9.7.1.15. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-popc)`popc`

[9.7.1.16. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-clz)`clz`

[9.7.1.17. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-bfind)`bfind`

[9.7.1.18. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-fns)`fns`

[9.7.1.19. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-brev)`brev`

[9.7.1.20. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-bfe)`bfe`

[9.7.1.21. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-bfi)`bfi`

[9.7.1.22. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-szext)`szext`

[9.7.1.23. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-bmsk)`bmsk`

[9.7.1.24. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-dp4a)`dp4a`

[9.7.1.25. Integer Arithmetic Instructions:](https://docs.nvidia.com/index.html#integer-arithmetic-instructions-dp2a)`dp2a`


-
[9.7.2. Extended-Precision Integer Arithmetic Instructions](https://docs.nvidia.com/index.html#extended-precision-integer-arithmetic-instructions)[9.7.2.1. Extended-Precision Arithmetic Instructions:](https://docs.nvidia.com/index.html#extended-precision-arithmetic-instructions-add-cc)`add.cc`

[9.7.2.2. Extended-Precision Arithmetic Instructions:](https://docs.nvidia.com/index.html#extended-precision-arithmetic-instructions-addc)`addc`

[9.7.2.3. Extended-Precision Arithmetic Instructions:](https://docs.nvidia.com/index.html#extended-precision-arithmetic-instructions-sub-cc)`sub.cc`

[9.7.2.4. Extended-Precision Arithmetic Instructions:](https://docs.nvidia.com/index.html#extended-precision-arithmetic-instructions-subc)`subc`

[9.7.2.5. Extended-Precision Arithmetic Instructions:](https://docs.nvidia.com/index.html#extended-precision-arithmetic-instructions-mad-cc)`mad.cc`

[9.7.2.6. Extended-Precision Arithmetic Instructions:](https://docs.nvidia.com/index.html#extended-precision-arithmetic-instructions-madc)`madc`


-
[9.7.3. Floating-Point Instructions](https://docs.nvidia.com/index.html#floating-point-instructions)[9.7.3.1. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-testp)`testp`

[9.7.3.2. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-copysign)`copysign`

[9.7.3.3. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-add)`add`

[9.7.3.4. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-sub)`sub`

[9.7.3.5. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-mul)`mul`

[9.7.3.6. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-fma)`fma`

[9.7.3.7. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-mad)`mad`

[9.7.3.8. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-div)`div`

[9.7.3.9. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-abs)`abs`

[9.7.3.10. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-neg)`neg`

[9.7.3.11. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-min)`min`

[9.7.3.12. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-max)`max`

[9.7.3.13. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-rcp)`rcp`

[9.7.3.14. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-rcp-approx-ftz-f64)`rcp.approx.ftz.f64`

[9.7.3.15. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-sqrt)`sqrt`

[9.7.3.16. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-rsqrt)`rsqrt`

[9.7.3.17. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-rsqrt-approx-ftz-f64)`rsqrt.approx.ftz.f64`

[9.7.3.18. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-sin)`sin`

[9.7.3.19. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-cos)`cos`

[9.7.3.20. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-lg2)`lg2`

[9.7.3.21. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-ex2)`ex2`

[9.7.3.22. Floating Point Instructions:](https://docs.nvidia.com/index.html#floating-point-instructions-tanh)`tanh`


-
[9.7.4. Half Precision Floating-Point Instructions](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions)[9.7.4.1. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-add)`add`

[9.7.4.2. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-sub)`sub`

[9.7.4.3. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-mul)`mul`

[9.7.4.4. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-fma)`fma`

[9.7.4.5. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-neg)`neg`

[9.7.4.6. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-abs)`abs`

[9.7.4.7. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-min)`min`

[9.7.4.8. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-max)`max`

[9.7.4.9. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-tanh)`tanh`

[9.7.4.10. Half Precision Floating Point Instructions:](https://docs.nvidia.com/index.html#half-precision-floating-point-instructions-ex2)`ex2`


-
[9.7.5. Mixed Precision Floating-Point Instructions](https://docs.nvidia.com/index.html#mixed-precision-floating-point-instructions) -
[9.7.6. Alternate Floating-Point Instructions](https://docs.nvidia.com/index.html#alternate-floating-point-instructions) -
[9.7.7. Comparison and Selection Instructions](https://docs.nvidia.com/index.html#comparison-and-selection-instructions) -
[9.7.8. Half Precision Comparison Instructions](https://docs.nvidia.com/index.html#half-precision-comparison-instructions) -
[9.7.9. Logic and Shift Instructions](https://docs.nvidia.com/index.html#logic-and-shift-instructions)[9.7.9.1. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-and)`and`

[9.7.9.2. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-or)`or`

[9.7.9.3. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-xor)`xor`

[9.7.9.4. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-not)`not`

[9.7.9.5. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-cnot)`cnot`

[9.7.9.6. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-lop3)`lop3`

[9.7.9.7. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-shf)`shf`

[9.7.9.8. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-shl)`shl`

[9.7.9.9. Logic and Shift Instructions:](https://docs.nvidia.com/index.html#logic-and-shift-instructions-shr)`shr`


-
[9.7.10. Data Movement and Conversion Instructions](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions)[9.7.10.1. Cache Operators](https://docs.nvidia.com/index.html#cache-operators)[9.7.10.2. Cache Eviction Priority Hints](https://docs.nvidia.com/index.html#cache-eviction-priority-hints)[9.7.10.3. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-mov)`mov`

[9.7.10.4. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-mov-2)`mov`

[9.7.10.5. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-shfl)`shfl`

(deprecated)[9.7.10.6. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-shfl-sync)`shfl.sync`

[9.7.10.7. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-prmt)`prmt`

[9.7.10.8. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-ld)`ld`

[9.7.10.9. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-ld-global-nc)`ld.global.nc`

[9.7.10.10. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-ldu)`ldu`

[9.7.10.11. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-st)`st`

[9.7.10.12. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-st-async)`st.async`

[9.7.10.13. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-multimem-st-async)`multimem.st.async`

[9.7.10.14. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-st-bulk)`st.bulk`

[9.7.10.15. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-multimem)`multimem.ld_reduce`

,`multimem.st`

,`multimem.red`

[9.7.10.16. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-prefetch-prefetchu)`prefetch`

,`prefetchu`

[9.7.10.17. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-applypriority)`applypriority`

[9.7.10.18. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-applypriority-async-bulk)`applypriority.async.bulk`

[9.7.10.19. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-applypriority-async-bulk-tensor)`applypriority.async.bulk.tensor`

[9.7.10.20. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-discard)`discard`

[9.7.10.21. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-createpolicy)`createpolicy`

[9.7.10.22. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-isspacep)`isspacep`

[9.7.10.23. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cvta)`cvta`

[9.7.10.24. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cvt)`cvt`

[9.7.10.25. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cvt-pack)`cvt.pack`

[9.7.10.26. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-mapa)`mapa`

[9.7.10.27. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-getctarank)`getctarank`

-
[9.7.10.28. Data Movement and Conversion Instructions: Asynchronous copy](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-asynchronous-copy)-
[9.7.10.28.1. Completion Mechanisms for Asynchronous Copy Operations](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-asynchronous-copy-completion-mechanisms) [9.7.10.28.2. Async Proxy](https://docs.nvidia.com/index.html#async-proxy)-
[9.7.10.28.3. Data Movement and Conversion Instructions: Non-bulk copy](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-non-bulk-copy) -
[9.7.10.28.4. Data Movement and Conversion Instructions: Bulk copy](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-bulk-copy)[9.7.10.28.4.1. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cp-async-bulk)`cp.async.bulk`

[9.7.10.28.4.2. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cp-reduce-async-bulk)`cp.reduce.async.bulk`

[9.7.10.28.4.3. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cp-async-bulk-prefetch)`cp.async.bulk.prefetch`

[9.7.10.28.4.4. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-multimem-cp-async-bulk)`multimem.cp.async.bulk`

[9.7.10.28.4.5. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-multimem-cp-reduce-async-bulk)`multimem.cp.reduce.async.bulk`


-
[9.7.10.28.5. Data Movement and Conversion Instructions: Tensor copy](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-tensor-copy)[9.7.10.28.5.1. Restriction on Tensor Copy instructions](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-tensor-copy-restrictions)-
[9.7.10.28.5.2. Overriding tensor property value](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-overriding-tensor-property-value) [9.7.10.28.5.3. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cp-async-bulk-tensor)`cp.async.bulk.tensor`

[9.7.10.28.5.4. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cp-reduce-async-bulk-tensor)`cp.reduce.async.bulk.tensor`

[9.7.10.28.5.5. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-cp-async-bulk-prefetch-tensor)`cp.async.bulk.prefetch.tensor`


-
[9.7.10.28.6. Data Movement and Conversion Instructions: Bulk and Tensor copy completion instructions](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-bulk-tensor-copy-completion)

-
[9.7.10.29. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-tensormap-replace)`tensormap.replace`

[9.7.10.30. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-spcompress)`spcompress`

[9.7.10.31. Data Movement and Conversion Instructions:](https://docs.nvidia.com/index.html#data-movement-and-conversion-instructions-spdecompress)`spdecompress`


-
[9.7.11. Fabric Instructions](https://docs.nvidia.com/index.html#fabric-instructions)[9.7.11.1. CFT Handles](https://docs.nvidia.com/index.html#cft-handles)-
[9.7.11.2. CFT Handles Overview](https://docs.nvidia.com/index.html#cft-handles-overview) -
[9.7.11.3. Life of a Fabric Operation](https://docs.nvidia.com/index.html#fabric-operations-lifecycle) -
[9.7.11.4. Completion mechanisms of fabric operations](https://docs.nvidia.com/index.html#fabric-completion-mechanisms) -
[9.7.11.5. Fabric operations](https://docs.nvidia.com/index.html#fabric-operations)[9.7.11.5.1. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-get)`fabric.try_get`

[9.7.11.5.2. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-put)`fabric.try_put`

[9.7.11.5.3. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-red)`fabric.try_red`

[9.7.11.5.4. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-pullred)`fabric.try_pullred`

[9.7.11.5.5. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-submit)`fabric.submit`

[9.7.11.5.6. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-wait)`fabric.wait`

[9.7.11.5.7. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-get-async-tensor)`fabric.try_get.async.tensor`

[9.7.11.5.8. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-put-async-tensor)`fabric.try_put.async.tensor`

[9.7.11.5.9. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-red-async-tensor)`fabric.try_red.async.tensor`

[9.7.11.5.10. Fabric Instructions:](https://docs.nvidia.com/index.html#fabric-instructions-try-atom)`fabric.try_atom`



-
[9.7.12. Texture Instructions](https://docs.nvidia.com/index.html#texture-instructions) -
[9.7.13. Surface Instructions](https://docs.nvidia.com/index.html#surface-instructions) -
[9.7.14. Control Flow Instructions](https://docs.nvidia.com/index.html#control-flow-instructions) -
[9.7.15. Parallel Synchronization and Communication Instructions](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions)[9.7.15.1. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-bar)`bar`

,`barrier`

[9.7.15.2. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-bar-warp-sync)`bar.warp.sync`

[9.7.15.3. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-barrier-cluster)`barrier.cluster`

[9.7.15.4. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-membar)`membar`

/`fence`

[9.7.15.5. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-atom)`atom`

[9.7.15.6. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-red)`red`

[9.7.15.7. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-red-async)`red.async`

[9.7.15.8. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-multimem-red-async)`multimem.red.async`

[9.7.15.9. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-vote)`vote`

(deprecated)[9.7.15.10. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-vote-sync)`vote.sync`

[9.7.15.11. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-match-sync)`match.sync`

[9.7.15.12. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-activemask)`activemask`

[9.7.15.13. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-redux-sync)`redux.sync`

[9.7.15.14. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-griddepcontrol)`griddepcontrol`

[9.7.15.15. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-elect-sync)`elect.sync`

-
[9.7.15.16. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier)`mbarrier`

[9.7.15.16.1. Size and alignment of mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-size-alignment)[9.7.15.16.2. Layouts of the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-object-layout)[9.7.15.16.3. Contents of the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-contents)[9.7.15.16.4. Lifecycle of the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-lifecycle)-
[9.7.15.16.5. Phases of the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-phase) -
[9.7.15.16.6. Tracking asynchronous operations by the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-tracking-async-operations) [9.7.15.16.7. Tracking successful completion of an operation using the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-tracking)[9.7.15.16.8. Phase Completion of the mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-phase-completion)[9.7.15.16.9. Arrive-on operation on mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-arrive-on)[9.7.15.16.10. Report-on operation on mbarrier object](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-report-on)[9.7.15.16.11. mbarrier support with shared memory](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-smem)[9.7.15.16.12. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-init)`mbarrier.init`

[9.7.15.16.13. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-inval)`mbarrier.inval`

[9.7.15.16.14. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-expect-tx)`mbarrier.expect_tx`

[9.7.15.16.15. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-complete-tx)`mbarrier.complete_tx`

[9.7.15.16.16. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-arrive)`mbarrier.arrive`

[9.7.15.16.17. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-arrive-drop)`mbarrier.arrive_drop`

[9.7.15.16.18. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-cp-async-mbarrier-arrive)`cp.async.mbarrier.arrive`

[9.7.15.16.19. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-test-wait-try-wait)`mbarrier.test_wait`

/`mbarrier.try_wait`

[9.7.15.16.20. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-pending-count)`mbarrier.pending_count`

[9.7.15.16.21. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-mbarrier-check-layout)`mbarrier.check_layout`


[9.7.15.17. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-tensormap-cp-fenceproxy)`tensormap.cp_fenceproxy`

[9.7.15.18. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-clusterlaunchcontrol-try-cancel)`clusterlaunchcontrol.try_cancel`

[9.7.15.19. Parallel Synchronization and Communication Instructions:](https://docs.nvidia.com/index.html#parallel-synchronization-and-communication-instructions-clusterlaunchcontrol-query-cancel)`clusterlaunchcontrol.query_cancel`


-
[9.7.16. Warp Level Matrix Multiply-Accumulate Instructions](https://docs.nvidia.com/index.html#warp-level-matrix-instructions)[9.7.16.1. Matrix Shape](https://docs.nvidia.com/index.html#warp-level-matrix-shape)[9.7.16.2. Matrix Data-types](https://docs.nvidia.com/index.html#warp-level-matrix-data-types)[9.7.16.3. Block Scaling for](https://docs.nvidia.com/index.html#warp-level-block-scaling)`mma.sync`

-
[9.7.16.4. Matrix multiply-accumulate operation using](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-wmma)`wmma`

instructions -
[9.7.16.5. Matrix multiply-accumulate operation using](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-for-mma)`mma`

instruction[9.7.16.5.1. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-884-f16)`mma.m8n8k4`

with`.f16`

floating point type[9.7.16.5.2. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-884-f64)`mma.m8n8k4`

with`.f64`

floating point type[9.7.16.5.3. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-8816)`mma.m8n8k16`

[9.7.16.5.4. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-8832)`mma.m8n8k32`

[9.7.16.5.5. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-88128)`mma.m8n8k128`

[9.7.16.5.6. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-1684)`mma.m16n8k4`

[9.7.16.5.7. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-1688)`mma.m16n8k8`

[9.7.16.5.8. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-16816-float)`mma.m16n8k16`

with floating point type[9.7.16.5.9. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-16816-i8-f8)`mma.m16n8k16`

with integer type[9.7.16.5.10. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-16832)`mma.m16n8k32`

[9.7.16.5.11. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-16864)`mma.m16n8k64`

[9.7.16.5.12. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-168128)`mma.m16n8k128`

[9.7.16.5.13. Matrix Fragments for](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-mma-168256)`mma.m16n8k256`

[9.7.16.5.14. Multiply-and-Accumulate Instruction:](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-mma)`mma`

[9.7.16.5.15. Warp-level matrix load instruction:](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-ldmatrix)`ldmatrix`

[9.7.16.5.16. Warp-level matrix store instruction:](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-stmatrix)`stmatrix`

[9.7.16.5.17. Warp-level matrix transpose instruction:](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-movmatrix)`movmatrix`


-
[9.7.16.6. Matrix multiply-accumulate operation using](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-for-sparse-mma)`mma.sp`

instruction with sparse matrix A[9.7.16.6.1. Sparse matrix storage](https://docs.nvidia.com/index.html#warp-level-sparse-matrix-storage)-
[9.7.16.6.2. Matrix fragments for multiply-accumulate operation with sparse matrix A](https://docs.nvidia.com/index.html#warp-level-matrix-fragments-for-sparse-mma)[9.7.16.6.2.1. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-16816-f16bf16)`mma.m16n8k16`

with`.f16`

and`.bf16`

types[9.7.16.6.2.2. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-16832-f16bf16)`mma.m16n8k32`

with`.f16`

and`.bf16`

types[9.7.16.6.2.3. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-16816-tf32)`mma.m16n8k16`

with`.tf32`

floating point type[9.7.16.6.2.4. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-1688-tf32)`mma.m16n8k8`

with`.tf32`

floating point type[9.7.16.6.2.5. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-16832-u8s8)`mma.m16n8k32`

with`.u8`

/`.s8`

integer type[9.7.16.6.2.6. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-16864-u8s8-fp8)`mma.m16n8k64`

with`.u8`

/`.s8`

/`.e4m3`

/`.e5m2`

type[9.7.16.6.2.7. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-16864-u4s4)`mma.m16n8k64`

with`.u4`

/`.s4`

integer type[9.7.16.6.2.8. Matrix Fragments for sparse](https://docs.nvidia.com/index.html#warp-level-matrix-fragment-sparse-mma-168128-u4s4)`mma.m16n8k128`

with`.u4`

/`.s4`

integer type

[9.7.16.6.3. Multiply-and-Accumulate Instruction:](https://docs.nvidia.com/index.html#warp-level-matrix-instructions-sparse-mma)`mma.sp`

/`mma.sp::ordered_metadata`



-
[9.7.17. Asynchronous Warpgroup Level Matrix Multiply-Accumulate Instructions](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-instructions)[9.7.17.1. Warpgroup](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-instructions-warpgroup)[9.7.17.2. Matrix Shape](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-shape)[9.7.17.3. Matrix Data-types](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-data-types)[9.7.17.4. Async Proxy](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-async-proxy)-
[9.7.17.5. Asynchronous Warpgroup Level Matrix Multiply-Accumulate Operation using](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-operation-wgmma-mma-async)`wgmma.mma_async`

instruction -
[9.7.17.6. Asynchronous Warpgroup Level Multiply-and-Accumulate Operation using](https://docs.nvidia.com/index.html#asynchronous-warpgroup-level-matrix-instructions-for-sparse-wgmma)`wgmma.mma_async.sp`

instruction -
[9.7.17.7. Asynchronous](https://docs.nvidia.com/index.html#asynchronous-wgmma-proxy-operations)`wgmma`

Proxy Operations

-
[9.7.18. TensorCore 5th Generation Family Instructions](https://docs.nvidia.com/index.html#tensorcore-5th-generation-instructions)-
[9.7.18.1. Tensor Memory](https://docs.nvidia.com/index.html#tensor-memory) -
[9.7.18.2. Matrix and Data Movement Shape](https://docs.nvidia.com/index.html#tcgen05-matrix-data-movement-shape) -
[9.7.18.3. Major-ness supported by Strides](https://docs.nvidia.com/index.html#tcgen05-majorness-supported-by-strides) -
[9.7.18.4. Matrix Descriptors](https://docs.nvidia.com/index.html#tcgen05-matrix-descriptors) -
[9.7.18.5. Issue Granularity](https://docs.nvidia.com/index.html#tcgen05-issue-granularity) -
[9.7.18.6. Memory Consistency Model for 5th generation of TensorCore operations](https://docs.nvidia.com/index.html#tcgen05-memory-consistency-model) -
[9.7.18.7. Tensor Memory Allocation and Management Instructions](https://docs.nvidia.com/index.html#tcgen05-memory-alloc-manage-instructions) -
[9.7.18.8. Tensor Memory and Register Load/Store Instructions](https://docs.nvidia.com/index.html#tcgen05-tensor-memory-ld-st) -
[9.7.18.9. Tensor Memory Data Movement Instructions](https://docs.nvidia.com/index.html#tcgen05-data-movement-instructions) -
[9.7.18.10. TensorCore 5th Generation Matrix Multiply and accumulate Operations](https://docs.nvidia.com/index.html#tcgen05-mma)[9.7.18.10.1. Transpose and Negate operations](https://docs.nvidia.com/index.html#tcgen05-transpose-and-negate-operations)[9.7.18.10.2. Matrix Layout Organization](https://docs.nvidia.com/index.html#tcgen05-matrix-layout-organization)[9.7.18.10.3. Valid Combinations of Type-Size, Major-ness and Swizzling](https://docs.nvidia.com/index.html#tcgen05-matrix-layout-organization-valid-comb-type-size-majorness-swizzle)-
[9.7.18.10.4. Packing formats of elements in Tensor and Shared memory](https://docs.nvidia.com/index.html#tcgen05-packing-formats)[9.7.18.10.4.1. Packing format for matrix D in Tensor Memory](https://docs.nvidia.com/index.html#tcgen05-packing-formats-mat-d)[9.7.18.10.4.2. Packing format for matrix A and B](https://docs.nvidia.com/index.html#tcgen05-packing-formats-mat-a-b)[9.7.18.10.4.3. Packing format used for matrix A by](https://docs.nvidia.com/index.html#tcgen05-packing-formats-mxf8f6f4-tmem)`.kind::mxf8f6f4`

in Tensor Memory[9.7.18.10.4.4. Packing format used for matrix A and B by](https://docs.nvidia.com/index.html#tcgen05-packing-formats-mxf8f6f4-smem)`.kind::mxf8f6f4`

in Shared Memory[9.7.18.10.4.5. Packing format used for matrix A by](https://docs.nvidia.com/index.html#tcgen05-packing-formats-mxf4-tmem)`.kind::mxf4`

and`.kind::mxf4nvf4`

in Tensor Memory[9.7.18.10.4.6. Packing format used for matrix A and B by](https://docs.nvidia.com/index.html#tcgen05-packing-formats-mxf4-smem)`.kind::mxf4`

and`.kind::mxf4nvf4`

in Shared Memory

-
[9.7.18.10.5. Data Path Layout Organization](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-organization)[9.7.18.10.5.1. Layout A (M = 256)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-a)[9.7.18.10.5.2. Layout B (M = 128 + cta_group::2 + Dense A matrix)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-b)[9.7.18.10.5.3. Layout C (M = 128 + cta_group::2 + Sparse A matrix)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-c)[9.7.18.10.5.4. Layout D (M = 128 + cta_group::1)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-d)[9.7.18.10.5.5. Layout E (M = 64 + .ws mode)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-e)[9.7.18.10.5.6. Layout F (M = 64 + non .ws mode)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-f)[9.7.18.10.5.7. Layout G (M = 32)](https://docs.nvidia.com/index.html#tcgen05-data-path-layout-g)

[9.7.18.10.6. Shared Memory Layout and Swizzling](https://docs.nvidia.com/index.html#tcgen05-shared-memory-layout-swizzling)-
[9.7.18.10.7. Block Scaling for](https://docs.nvidia.com/index.html#tcgen05-block-scaling)`tcgen05.mma`

[9.7.18.10.7.1. Valid combinations of scale_vectorsize with types and MMA-Kind](https://docs.nvidia.com/index.html#tcgen05-mma-scale-valid-vec-size)-
[9.7.18.10.7.2. Scale Factor A ID](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a)[9.7.18.10.7.2.1. Layout of the Scale Factor A Matrix for scale_vec::1X/block32 with K=32/K=64](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a-layout-1x)[9.7.18.10.7.2.2. Layout of the Scale Factor A Matrix for scale_vec::2X/block32 with K=64/K=128](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a-layout-2x)[9.7.18.10.7.2.3. Layout of the Scale Factor A Matrix for scale_vec::4X/block16 with K=64/K=128](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a-layout-4x)[9.7.18.10.7.2.4. Layout of the Scale Factor A Matrix for block32 with K=96 (Semantically equivalent to scale_vec::3X)](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a-layout-block32-k96)[9.7.18.10.7.2.5. Layout of the Scale Factor A Matrix for block16 with K=96 (Semantically equivalent to scale_vec::6X)](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a-layout-block16-k96)[9.7.18.10.7.2.6. Layout of the Scale Factor A Matrix for block16 with K=128/256 (Semantically equivalent to scale_vec::8X)](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-a-layout-block16-k128-256)

-
[9.7.18.10.7.3. Scale Factor B ID](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b)[9.7.18.10.7.3.1. Layout of the Scale Factor B Matrix for scale_vec::1X/block32 with K=32/K=64](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b-layout-1x)[9.7.18.10.7.3.2. Layout of the Scale Factor B Matrix for scale_vec::2X/block32 with K=64/K=128](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b-layout-2x)[9.7.18.10.7.3.3. Layout of the Scale Factor B Matrix for scale_vec::4X/block16 with K=64/K=128](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b-layout-4x)[9.7.18.10.7.3.4. Layout of the Scale Factor B Matrix for block32 with K=96 (Semantically equivalent to scale_vec::3X)](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b-layout-block32-k96)[9.7.18.10.7.3.5. Layout of the Scale Factor B Matrix for block16 with K=96 (Semantically equivalent to scale_vec::6X)](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b-layout-block16-k96)[9.7.18.10.7.3.6. Layout of the Scale Factor B Matrix for block16 with K=128/256 (Semantically equivalent to scale_vec::8X)](https://docs.nvidia.com/index.html#tcgen05-mma-scale-factor-b-layout-block16-k128-256)


[9.7.18.10.8. Decompression of input matrices](https://docs.nvidia.com/index.html#tcgen05-decompress-inp-mat)-
[9.7.18.10.9. Sparse Matrices](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices)[9.7.18.10.9.1. Sparse](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-kind-tf32)`tcgen05.mma.sp`

with`.kind::tf32`

[9.7.18.10.9.2. Sparse](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-kind-f16-f8f8f4-mxf8f6f4)`tcgen05.mma.sp`

with`.kind::f16`

,`.kind::f8f6f4`

,`.kind::mxf8f6f4`

,`.kind::i8`

,`.kind::ti16`

[9.7.18.10.9.3. Sparse](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-kind-mxf4)`tcgen05.mma.sp`

with`.kind::mxf4`

and`.kind::mxf4nvf4`

-
[9.7.18.10.9.4. Sparsity selector](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector)[9.7.18.10.9.4.1. Layout of the Sparsity Metadata Matrix for M = 64 for](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector-kind-f16-m64)`.kind::f16`

,`.kind::ti16`

[9.7.18.10.9.4.2. Layout of the Sparsity Metadata Matrix for M = 128 / M = 256 for](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector-kind-f16-m128-256)`.kind::f16`

,`.kind::ti16`

[9.7.18.10.9.4.3. Layout of the Sparsity Metadata Matrix for M = 64 for](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector-kind-tf32-m64)`.kind::tf32`

[9.7.18.10.9.4.4. Layout of the Sparsity Metadata Matrix for M = 128 / M = 256 for](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector-kind-tf32-m128-256)`.kind::tf32`

[9.7.18.10.9.4.5. Layout of the Sparsity Metadata Matrix for M = 64 for](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector-kind-f8f6f4-mxf8f6f4-m64)`.kind::f8f6f4`

,`.kind::mxf8f6f4`

,`.kind::i8`

,`.kind::mxf4`

,`.kind::mxf4nvf4`

[9.7.18.10.9.4.6. Layout of the Sparsity Metadata Matrix for M = 128 / M = 256 for](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-sparsity-selector-kind-f8f6f4-mxf8f6f4-m128-256)`.kind::f8f6f4`

,`.kind::mxf8f6f4`

,`.kind::i8`

,`.kind::mxf4`

,`.kind::mxf4nvf4`


[9.7.18.10.9.5. Alignment restriction](https://docs.nvidia.com/index.html#tcgen05-sparse-matrices-alignment-restriction)

-
[9.7.18.10.10. TensorCore 5th Generation of MMA Instructions](https://docs.nvidia.com/index.html#tcgen05-mma-instructions)

-
[9.7.18.11. TensorCore 5th Generation Specialized Synchronization Operations](https://docs.nvidia.com/index.html#tcgen05-special-sync-operations) -
[9.7.18.12. TensorCore 5th Generation Async Synchronization Operations](https://docs.nvidia.com/index.html#tcgen-async-sync-operations)

-
-
[9.7.19. Stack Manipulation Instructions](https://docs.nvidia.com/index.html#stack-manipulation-instructions) -
[9.7.20. Video Instructions](https://docs.nvidia.com/index.html#video-instructions) -
[9.7.21. Miscellaneous Instructions](https://docs.nvidia.com/index.html#miscellaneous-instructions)

-

-
[10. Special Registers](https://docs.nvidia.com/index.html#special-registers)[10.1. Special Registers:](https://docs.nvidia.com/index.html#special-registers-tid)`%tid`

[10.2. Special Registers:](https://docs.nvidia.com/index.html#special-registers-ntid)`%ntid`

[10.3. Special Registers:](https://docs.nvidia.com/index.html#special-registers-laneid)`%laneid`

[10.4. Special Registers:](https://docs.nvidia.com/index.html#special-registers-warpid)`%warpid`

[10.5. Special Registers:](https://docs.nvidia.com/index.html#special-registers-nwarpid)`%nwarpid`

[10.6. Special Registers:](https://docs.nvidia.com/index.html#special-registers-ctaid)`%ctaid`

[10.7. Special Registers:](https://docs.nvidia.com/index.html#special-registers-nctaid)`%nctaid`

[10.8. Special Registers:](https://docs.nvidia.com/index.html#special-registers-smid)`%smid`

[10.9. Special Registers:](https://docs.nvidia.com/index.html#special-registers-nsmid)`%nsmid`

[10.10. Special Registers:](https://docs.nvidia.com/index.html#special-registers-gridid)`%gridid`

[10.11. Special Registers:](https://docs.nvidia.com/index.html#special-registers-is-explicit-cluster)`%is_explicit_cluster`

[10.12. Special Registers:](https://docs.nvidia.com/index.html#special-registers-clusterid)`%clusterid`

[10.13. Special Registers:](https://docs.nvidia.com/index.html#special-registers-nclusterid)`%nclusterid`

[10.14. Special Registers:](https://docs.nvidia.com/index.html#special-registers-cluster-ctaid)`%cluster_ctaid`

[10.15. Special Registers:](https://docs.nvidia.com/index.html#special-registers-cluster-nctaid)`%cluster_nctaid`

[10.16. Special Registers:](https://docs.nvidia.com/index.html#special-registers-cluster-ctarank)`%cluster_ctarank`

[10.17. Special Registers:](https://docs.nvidia.com/index.html#special-registers-cluster-nctarank)`%cluster_nctarank`

[10.18. Special Registers:](https://docs.nvidia.com/index.html#special-registers-lanemask-eq)`%lanemask_eq`

[10.19. Special Registers:](https://docs.nvidia.com/index.html#special-registers-lanemask-le)`%lanemask_le`

[10.20. Special Registers:](https://docs.nvidia.com/index.html#special-registers-lanemask-lt)`%lanemask_lt`

[10.21. Special Registers:](https://docs.nvidia.com/index.html#special-registers-lanemask-ge)`%lanemask_ge`

[10.22. Special Registers:](https://docs.nvidia.com/index.html#special-registers-lanemask-gt)`%lanemask_gt`

[10.23. Special Registers:](https://docs.nvidia.com/index.html#special-registers-clock)`%clock`

,`%clock_hi`

[10.24. Special Registers:](https://docs.nvidia.com/index.html#special-registers-clock64)`%clock64`

[10.25. Special Registers:](https://docs.nvidia.com/index.html#special-registers-pm0-pm7)`%pm0`

…`%pm7`

[10.26. Special Registers:](https://docs.nvidia.com/index.html#special-registers-pm0-64-pm7-64)`%pm0_64`

…`%pm7_64`

[10.27. Special Registers:](https://docs.nvidia.com/index.html#special-registers-envreg-32)`%envreg<32>`

[10.28. Special Registers:](https://docs.nvidia.com/index.html#special-registers-globaltimer)`%globaltimer`

,`%globaltimer_lo`

,`%globaltimer_hi`

[10.29. Special Registers:](https://docs.nvidia.com/index.html#special-registers-reserved-smem)`%reserved_smem_offset_begin`

,`%reserved_smem_offset_end`

,`%reserved_smem_offset_cap`

,`%reserved_smem_offset_<2>`

[10.30. Special Registers:](https://docs.nvidia.com/index.html#special-registers-total-smem-size)`%total_smem_size`

[10.31. Special Registers:](https://docs.nvidia.com/index.html#special-registers-aggr-smem-size)`%aggr_smem_size`

[10.32. Special Registers:](https://docs.nvidia.com/index.html#special-registers-dynamic-smem-size)`%dynamic_smem_size`

[10.33. Special Registers:](https://docs.nvidia.com/index.html#special-registers-current-graph-exec)`%current_graph_exec`

[10.34. Special Registers:](https://docs.nvidia.com/index.html#special-registers-perctamemoryoffset)`%perctamemoryoffset`

[10.35. Special Registers:](https://docs.nvidia.com/index.html#special-registers-perctamemorysize)`%perctamemorysize`


-
[11. Directives](https://docs.nvidia.com/index.html#directives)-
[11.1. PTX Module Directives](https://docs.nvidia.com/index.html#ptx-module-directives) -
[11.2. Specifying Kernel Entry Points and Functions](https://docs.nvidia.com/index.html#specifying-kernel-entry-points-and-functions) -
[11.3. Control Flow Directives](https://docs.nvidia.com/index.html#control-flow-directives) -
[11.4. Performance-Tuning Directives](https://docs.nvidia.com/index.html#performance-tuning-directives)[11.4.1. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-maxnreg)`.maxnreg`

[11.4.2. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-maxntid)`.maxntid`

[11.4.3. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-reqntid)`.reqntid`

[11.4.4. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-minnctapersm)`.minnctapersm`

[11.4.5. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-maxnctapersm)`.maxnctapersm`

(deprecated)[11.4.6. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-noreturn)`.noreturn`

[11.4.7. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-pragma)`.pragma`

[11.4.8. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-abi-preserve)`.abi_preserve`

[11.4.9. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-abi-preserve-control)`.abi_preserve_control`

[11.4.10. Performance-Tuning Directives:](https://docs.nvidia.com/index.html#performance-tuning-directives-minperctamemory)`.minperctamemory`


-
[11.5. Debugging Directives](https://docs.nvidia.com/index.html#debugging-directives) -
[11.6. Linking Directives](https://docs.nvidia.com/index.html#linking-directives) -
[11.7. Cluster Dimension Directives](https://docs.nvidia.com/index.html#cluster-dimension-directives) -
[11.8. Miscellaneous Directives](https://docs.nvidia.com/index.html#miscellaneous-directives)

-
-
[12. Descriptions of](https://docs.nvidia.com/index.html#descriptions-pragma-strings)`.pragma`

Strings -
[13. Release Notes](https://docs.nvidia.com/index.html#release-notes)[13.1. Changes in PTX ISA Version 9.4](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-9-4)[13.2. Changes in PTX ISA Version 9.3](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-9-3)[13.3. Changes in PTX ISA Version 9.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-9-2)[13.4. Changes in PTX ISA Version 9.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-9-1)[13.5. Changes in PTX ISA Version 9.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-9-0)[13.6. Changes in PTX ISA Version 8.8](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-8)[13.7. Changes in PTX ISA Version 8.7](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-7)[13.8. Changes in PTX ISA Version 8.6](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-6)[13.9. Changes in PTX ISA Version 8.5](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-5)[13.10. Changes in PTX ISA Version 8.4](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-4)[13.11. Changes in PTX ISA Version 8.3](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-3)[13.12. Changes in PTX ISA Version 8.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-2)[13.13. Changes in PTX ISA Version 8.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-1)[13.14. Changes in PTX ISA Version 8.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-8-0)[13.15. Changes in PTX ISA Version 7.8](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-8)[13.16. Changes in PTX ISA Version 7.7](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-7)[13.17. Changes in PTX ISA Version 7.6](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-6)[13.18. Changes in PTX ISA Version 7.5](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-5)[13.19. Changes in PTX ISA Version 7.4](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-4)[13.20. Changes in PTX ISA Version 7.3](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-3)[13.21. Changes in PTX ISA Version 7.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-2)[13.22. Changes in PTX ISA Version 7.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-1)[13.23. Changes in PTX ISA Version 7.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-7-0)[13.24. Changes in PTX ISA Version 6.5](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-6-5)[13.25. Changes in PTX ISA Version 6.4](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-6-4)[13.26. Changes in PTX ISA Version 6.3](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-6-3)[13.27. Changes in PTX ISA Version 6.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-6-2)[13.28. Changes in PTX ISA Version 6.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-6-1)[13.29. Changes in PTX ISA Version 6.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-6-0)[13.30. Changes in PTX ISA Version 5.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-5-0)[13.31. Changes in PTX ISA Version 4.3](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-4-3)[13.32. Changes in PTX ISA Version 4.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-4-2)[13.33. Changes in PTX ISA Version 4.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-4-1)[13.34. Changes in PTX ISA Version 4.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-4-0)[13.35. Changes in PTX ISA Version 3.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-3-2)[13.36. Changes in PTX ISA Version 3.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-3-1)[13.37. Changes in PTX ISA Version 3.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-3-0)[13.38. Changes in PTX ISA Version 2.3](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-2-3)[13.39. Changes in PTX ISA Version 2.2](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-2-2)[13.40. Changes in PTX ISA Version 2.1](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-2-1)[13.41. Changes in PTX ISA Version 2.0](https://docs.nvidia.com/index.html#changes-in-ptx-isa-version-2-0)

-
[14. Notices](https://docs.nvidia.com/index.html#notices)