# [Issue #2698] Remove iMatrixGatherer

source: https://github.com/vllm-project/llm-compressor/issues/2698
state: closed | updated: 2026-09-09T02:12:03Z
labels: enhancement, good first issue, stale

## 正文

In https://github.com/vllm-project/llm-compressor/pull/2473 we went back and forth about the implementation and finalized a temporary design. The plan was to implement it then with an iMatrixGatherer modifier and later remove it when required llmc functionality was added. That day has come.

The iMatrix technique is fundamentally about how you quantize values, making it an observer, but to support it we needed to add an iMatrixGatherer modifier because the normal quantization modifier did weight quantization at the start of the lifecycle, before calibration which would break the iMatrixObserver. This is no longer the case as of https://github.com/vllm-project/llm-compressor/pull/2585 which consolidated the lifecycle to always do quantization after calibration. This allows us to do the following:

1) remove iMatrixGatherer
2) store imatrix statistics always on the observer, never on the modifier
3) we need to make sure to do calibration if doing weight only quantization with the imatrix observer.

## 评论 (5)

### dshane1903 · 2026-05-12

I’d like to take this one.

My plan:
1. Remove `IMatrixGatherer` exports, registry entries, docs/examples, and tests that depend on the temporary modifier.
2. Keep `imatrix_mse` support in `IMatrixMSEObserver`, with importance statistics stored on the observer/module path rather than on a separate modifier.
3. Update the quantization/GPTQ flow so weight-only `imatrix_mse` still performs activation calibration now that quantization happens after calibration.
4. Add/update CPU tests proving recipes using `weights.observer: imatrix_mse` work without `IMatrixGatherer`, including an end-to-end comparison that iMatrix affects scales versus the fallback path.

Please let me know if you want backward compatibility for old recipes that still include `IMatrixGatherer`, or if removing it outright is preferred.


### HDCharles · 2026-05-13

Outright removal is preferred, go ahead I'll assign you

### vasuag09 · 2026-06-03

Hey @HDCharles, Is this issue still open to work upon?


### dshane1903 · 2026-06-03

Hey @vasuag09, I’m currently working on this in vllm-project/llm-compressor#2716. That PR implements the outright `IMatrixGatherer` removal requested above. It’s currently waiting on the companion compressed-tensors PR vllm-project/compressed-tensors#710, which moves the calibration-data check into `QuantizationConfig.requires_calibration_data()` so the llm-compressor PR can be simplified cleanly. Happy to coordinate if you were looking at a related piece.

### github-actions[bot] · 2026-09-01

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
