source: https://docs.nvidia.com/cuda/npp/image_threshold_and_compare_operations.html

# Image Threshold And Compare Operations[](https://docs.nvidia.com#image-threshold-and-compare-operations)

Methods for pixel-wise threshold and compare operations.

These functions can be found in the nppitc library. Linking to only the sub-libraries that you use can significantly save link time, application load time, and CUDA runtime startup time when using dynamic libraries.

## Image Threshold Operations[](https://docs.nvidia.com#image-threshold-operations)

### Threshold Operations[](https://docs.nvidia.com#group__image__threshold__operations_1image_threshold_operations)

Threshold image pixels.

#### Common parameters for nppiThreshold non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__operations_1CommonThresholdParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThreshold
-
The threshold value.

- param eComparisonOperation
-
The type of comparison operation to be used. The only valid values are: NPP_CMP_LESS and NPP_CMP_GREATER.

- param nppStreamCtx
- return
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes), or NPP_NOT_SUPPORTED_MODE_ERROR if an invalid comparison operation type is specified.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__operations_1commonthresholdparameters).

### Image Threshold Greater Than Operations[](https://docs.nvidia.com#image-threshold-greater-than-operations)

#### Threshold Greater Than Operations[](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1image_threshold_greater_than_operations)

Threshold greater than image pixels.

##### Common parameters for nppiThreshold_GT non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1CommonThresholdGreaterThanParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThreshold
-
The threshold value.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GT_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GT_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__operations_1commonthresholdgreaterthanparameters).

### Image Threshold Less Than Operations[](https://docs.nvidia.com#image-threshold-less-than-operations)

#### Threshold Less Than Operations[](https://docs.nvidia.com#group__image__threshold__less__than__operations_1image_threshold_less_than_operations)

Threshold less than image pixels.

##### Common parameters for nppiThreshold_LT non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__less__than__operations_1CommonThresholdLessThanParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThreshold
-
The threshold value.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LT_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LT_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set value is set to nThreshold, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LT non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__operations_1commonthresholdlessthanparameters).

### Image Threshold Value Operations[](https://docs.nvidia.com#image-threshold-value-operations)

#### Threshold Value Operations[](https://docs.nvidia.com#group__image__threshold__value__operations_1image_threshold_value_operations)

Replace thresholded image pixels with a value.

##### Common parameters for nppiThreshold_Val non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__value__operations_1CommonThresholdValueParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThreshold
-
The threshold value.

- param nValue
-
The threshold replacement value.

- param eComparisonOperation
-
The type of comparison operation to be used. The only valid values are: NPP_CMP_LESS and NPP_CMP_GREATER.

- param nppStreamCtx
- return
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes), or NPP_NOT_SUPPORTED_MODE_ERROR if an invalid comparison operation type is specified.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations OP the predicate (sourcePixel OP nThreshold) is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_Val_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_Val_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations OP the predicate (sourcePixel.channel OP nThreshold) is true, the channel value is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_Val non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__value__operations_1commonthresholdvalueparameters).

### Image Threshold Greater Than Value Operations[](https://docs.nvidia.com#image-threshold-greater-than-value-operations)

#### Threshold Greater Than Value Operations[](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1image_threshold_greater_than_value_operations)

Replace image pixels greater than threshold with a value.

##### Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1CommonThresholdGreaterThanValueParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThreshold
-
The threshold value.

- param nValue
-
The threshold replacement value.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is greater than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_GTVal_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_GTVal_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is greater than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_GTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__greater__than__value__operations_1commonthresholdgreaterthanvalueparameters).

### Image Threshold Less Than Value Operations[](https://docs.nvidia.com#image-threshold-less-than-value-operations)

#### Threshold Less Than Value Operations[](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1image_threshold_less_than_value_operations)

Replace image pixels less than threshold with a value.

##### Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1CommonThresholdLessThanValueParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThreshold
-
The threshold value.

- param nValue
-
The threshold replacement value.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThreshold, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThreshold, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThreshold, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThreshold, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is less than nThreshold is true, the pixel is set to nValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholds[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholds[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholds[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTVal_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholds[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValues[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTVal_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThreshold is true, the pixel is set value is set to rValue, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__operations_1commonthresholdlessthanvalueparameters).

### Image Fused AbsDiff Threshold Greater Than Value Operations[](https://docs.nvidia.com#image-fused-absdiff-threshold-greater-than-value-operations)

#### Fused AbsDiff Threshold Greater Than Value Operations[](https://docs.nvidia.com#group__image__fused__absdiff__threshold__greater__than__value__operations_1image_fused_absdiff_threshold_greater_than_value_operations)

Replace image pixels greater than threshold with a value.

Supported data types include NPP_8U, NPP_16U, NPP_16S, NPP_32F. Supported channel counts include NPP_CH_1, NPP_CH_3, NPP_CH_A4.

- param eSrcDstType
-
image data type.

- param eSrcDstChannels
-
image channels.

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc1
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrc1Step
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pSrc2
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)to second source image for non-inplace functions. - param nSrc2Step
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)of second source image for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param pThreshold
-
The threshold value.

- param pValue
-
The threshold replacement value.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiFusedAbsDiff_Threshold_GTVal_Ctx([NppDataType](https://docs.nvidia.com/nppdefs.html#c.NppDataType)eSrcDstType,[NppiChannels](https://docs.nvidia.com/nppdefs.html#c.NppiChannels)eSrcDstChannels, const void *pSrc1, int nSrc1Step, const void *pSrc2, int nSrc2Step, void *pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const void *pThreshold, const void *pvalue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiFusedAbsDiff_Threshold_GTVal_Ctx)

-
Image fused absdiff and greater than threshold value.

If for a comparison operations absdiff of sourcePixels is greater than pThreshold is true, the output pixel is set to pValue, otherwise it is set to absdiff of sourcePixels.


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiFusedAbsDiff_Threshold_GTVal_I_Ctx([NppDataType](https://docs.nvidia.com/nppdefs.html#c.NppDataType)eSrcDstType,[NppiChannels](https://docs.nvidia.com/nppdefs.html#c.NppiChannels)eSrcDstChannels, void *pSrcDst, int nSrcDstStep, const void *pSrc2, int nSrc2Step,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const void *pThreshold, const void *pvalue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiFusedAbsDiff_Threshold_GTVal_I_Ctx)

-
In place fused absdiff image greater than threshold value.

If for a comparison operations absdiff of sourcePixels is greater than pThreshold is true, the output pixel is set to pValue, otherwise it is set to absdiff of sourcePixels.


### Image Threshold Less Than Value Greater Than Value Operations[](https://docs.nvidia.com#image-threshold-less-than-value-greater-than-value-operations)

#### Threshold Less Than Value Or Greater Than Value Operations[](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1image_threshold_less_than_value_greater_than_value_operations)

Replace image pixels less than thresholdLT or greater than thresholdGT with with valueLT or valueGT respectively.

##### Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:[](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1CommonThresholdLessThanValueGreaterThanValueParameters)

- param pSrcDst
-
[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer)for inplace functions. - param nSrcDstStep
-
[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step)for inplace functions. - param pSrc
-
[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer)for non-inplace functions. - param nSrcStep
-
[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)for non-inplace functions. - param pDst
-
[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer)for non-inplace functions. - param nDstStep
-
[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)for non-inplace functions. - param oSizeROI
- param nThresholdLT
-
The thresholdLT value.

- param nValueLT
-
The thresholdLT replacement value.

- param nThresholdGT
-
The thresholdGT value.

- param nValueGT
-
The thresholdGT replacement value.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThresholdLT, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValueLT, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThresholdGT, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThresholdLT, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValueLT, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nThresholdGT, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThresholdLT, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValueLT, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThresholdGT, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThresholdLT, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValueLT, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nThresholdGT, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThresholdLT, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValueLT, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThresholdGT, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16s_C1R_Ctx)

-
1 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThresholdLT, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValueLT, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nThresholdGT, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16s_C1IR_Ctx)

-
1 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThresholdLT, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValueLT, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThresholdGT, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_32f_C1R_Ctx)

-
1 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThresholdLT, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValueLT, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nThresholdGT, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValueGT,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is less than nThresholdLT is true, the pixel is set to nValueLT, else if sourcePixel is greater than nThresholdGT the pixel is set to nValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsGT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsGT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned char in place threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsGT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsGT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned short in place threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsGT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16s_C3R_Ctx)

-
3 channel 16-bit signed short threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsGT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16s_C3IR_Ctx)

-
3 channel 16-bit signed short in place threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsGT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_32f_C3R_Ctx)

-
3 channel 32-bit floating point threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsGT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place threshold.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsGT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesLT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rThresholdsGT[3], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned char in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsGT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesLT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rThresholdsGT[3], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsGT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesLT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rThresholdsGT[3], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_16s_AC4IR_Ctx)

-
4 channel 16-bit signed short in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsGT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiThreshold_LTValGTVal_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesLT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rThresholdsGT[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)rValuesGT[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiThreshold_LTValGTVal_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place image threshold, not affecting Alpha.

If for a comparison operations sourcePixel is less than rThresholdLT is true, the pixel is set value is set to rValueLT, else if sourcePixel is greater than rThresholdGT the pixel is set to rValueGT, otherwise it is set to sourcePixel.

For common parameter descriptions, see

[Common parameters for nppiThreshold_LTValGTVal non-inplace and inplace functions:](https://docs.nvidia.com#group__image__threshold__less__than__value__greater__than__value__operations_1commonthresholdlessthanvaluegreaterthanvalueparameters).

## Image Comparison Operations[](https://docs.nvidia.com#image-comparison-operations)

### Comparison Operations[](https://docs.nvidia.com#group__image__comparison__operations_1image_comparison_operations)

Compare the pixels of two images or one image and a constant value and create a binary result image. In case of multi-channel image types, the condition must be fulfilled for all channels, otherwise the comparison is considered false. The “binary” result image is of type 8u_C1. False is represented by 0, true by NPP_MAX_8U.

### Compare Images Operations[](https://docs.nvidia.com#compare-images-operations)

#### Compare Images Operations[](https://docs.nvidia.com#group__compare__images__operations_1compare_images_operations)

Compare the pixels of two images and create a binary result image. In case of multi-channel image types, the condition must be fulfilled for all channels, otherwise the comparison is considered false. The “binary” result image is of type 8u_C1. False is represented by 0, true by NPP_MAX_8U.

##### Common parameters for nppiCompare functions:[](https://docs.nvidia.com#group__compare__images__operations_1CommonCompareImagesParameters)

- param pSrc1
- param nSrc1Step
- param pSrc2
- param nSrc2Step
- param pDst
- param nDstStep
- param oSizeROI
- param eComparisonOperation
-
Specifies the comparison operation to be used in the pixel comparison.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_8u_C4R_Ctx)

-
4 channel 8-bit unsigned char image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image compare, not affecting Alpha.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, int nSrc1Step, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, int nSrc1Step, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, int nSrc1Step, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16u_C4R_Ctx)

-
4 channel 16-bit unsigned short image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc1, int nSrc1Step, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image compare, not affecting Alpha.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, int nSrc1Step, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16s_C1R_Ctx)

-
1 channel 16-bit signed short image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, int nSrc1Step, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16s_C3R_Ctx)

-
3 channel 16-bit signed short image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, int nSrc1Step, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16s_C4R_Ctx)

-
4 channel 16-bit signed short image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc1, int nSrc1Step, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image compare, not affecting Alpha.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_32f_C1R_Ctx)

-
1 channel 32-bit floating point image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_32f_C3R_Ctx)

-
3 channel 32-bit floating point image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_32f_C4R_Ctx)

-
4 channel 32-bit floating point image compare.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompare_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompare_32f_AC4R_Ctx)

-
4 channel 32-bit signed floating point compare, not affecting Alpha.

Compare pSrc1’s pixels with corresponding pixels in pSrc2.

For common parameter descriptions, see

[Common parameters for nppiCompare functions:](https://docs.nvidia.com#group__compare__images__operations_1commoncompareimagesparameters).

### Compare Image With Constant Operations[](https://docs.nvidia.com#compare-image-with-constant-operations)

#### Compare Image With Constant Operations[](https://docs.nvidia.com#group__compare__image__with__constant__operations_1compare_image_with_constant_operations)

Compare the pixels of an image with a constant value and create a binary result image. In case of multi-channel image types, the condition must be fulfilled for all channels, otherwise the comparison is considered false. The “binary” result image is of type 8u_C1. False is represented by 0, true by NPP_MAX_8U.

##### Common parameters for nppiCompareC functions:[](https://docs.nvidia.com#group__compare__image__with__constant__operations_1CommonCompareImageWithConstantParameters)

- param pSrc
- param nSrcStep
- param nConstant
-
constant value for single channel functions.

- param pConstants
-
pointer to a list of constant values, one per color channel for multi-channel functions.

- param pDst
- param nDstStep
- param oSizeROI
- param eComparisonOperation
-
Specifies the comparison operation to be used in the pixel comparison.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nConstant,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_8u_C1R_Ctx)

-
1 channel 8-bit unsigned char image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_8u_C3R_Ctx)

-
3 channel 8-bit unsigned char image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_8u_C4R_Ctx)

-
4 channel 8-bit unsigned char image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned char image compare, not affecting Alpha.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nConstant,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16u_C1R_Ctx)

-
1 channel 16-bit unsigned short image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16u_C3R_Ctx)

-
3 channel 16-bit unsigned short image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16u_C4R_Ctx)

-
4 channel 16-bit unsigned short image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned short image compare, not affecting Alpha.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nConstant,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16s_C1R_Ctx)

-
1 channel 16-bit signed short image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16s_C3R_Ctx)

-
3 channel 16-bit signed short image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16s_C4R_Ctx)

-
4 channel 16-bit signed short image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_16s_AC4R_Ctx)

-
4 channel 16-bit signed short image compare, not affecting Alpha.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nConstant,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_32f_C1R_Ctx)

-
1 channel 32-bit floating point image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_32f_C3R_Ctx)

-
3 channel 32-bit floating point image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_32f_C4R_Ctx)

-
4 channel 32-bit floating point image compare with constant value.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareC_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppCmpOp](https://docs.nvidia.com/nppdefs.html#c.NppCmpOp)eComparisonOperation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareC_32f_AC4R_Ctx)

-
4 channel 32-bit signed floating point compare, not affecting Alpha.

Compare pSrc’s pixels with constant value.

For common parameter descriptions, see

[Common parameters for nppiCompareC functions:](https://docs.nvidia.com#group__compare__image__with__constant__operations_1commoncompareimagewithconstantparameters).

### Compare Image Differences With Epsilon Operations[](https://docs.nvidia.com#compare-image-differences-with-epsilon-operations)

#### Compare Image Differences With Epsilon Operations[](https://docs.nvidia.com#group__compare__image__differences__with__epsilon__operations_1compare_image_differences_with_epsilon_operations)

Compare the pixels value differences of two images with an epsilon value and create a binary result image. In case of multi-channel image types, the condition must be fulfilled for all channels, otherwise the comparison is considered false. The “binary” result image is of type 8u_C1. False is represented by 0, true by NPP_MAX_8U.

##### Common parameters for nppiCompareEqualEps functions include:[](https://docs.nvidia.com#group__compare__image__differences__with__epsilon__operations_1CommonCompareImageDifferencesWithEpsilonParameters)

- param pSrc1
- param nSrc1Step
- param pSrc2
- param nSrc2Step
- param pDst
- param nDstStep
- param oSizeROI
- param nEpsilon
-
epsilon tolerance value to compare to pixel absolute differences

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEps_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEps_32f_C1R_Ctx)

-
1 channel 32-bit floating point image compare whether two images are equal within epsilon.

Compare pSrc1’s pixels with corresponding pixels in pSrc2 to determine whether they are equal with a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEps functions include:](https://docs.nvidia.com#group__compare__image__differences__with__epsilon__operations_1commoncompareimagedifferenceswithepsilonparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEps_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEps_32f_C3R_Ctx)

-
3 channel 32-bit floating point image compare whether two images are equal within epsilon.

Compare pSrc1’s pixels with corresponding pixels in pSrc2 to determine whether they are equal with a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEps functions include:](https://docs.nvidia.com#group__compare__image__differences__with__epsilon__operations_1commoncompareimagedifferenceswithepsilonparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEps_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEps_32f_C4R_Ctx)

-
4 channel 32-bit floating point image compare whether two images are equal within epsilon.

Compare pSrc1’s pixels with corresponding pixels in pSrc2 to determine whether they are equal with a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEps functions include:](https://docs.nvidia.com#group__compare__image__differences__with__epsilon__operations_1commoncompareimagedifferenceswithepsilonparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEps_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc1, int nSrc1Step, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEps_32f_AC4R_Ctx)

-
4 channel 32-bit signed floating point compare whether two images are equal within epsilon, not affecting Alpha.

Compare pSrc1’s pixels with corresponding pixels in pSrc2 to determine whether they are equal with a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEps functions include:](https://docs.nvidia.com#group__compare__image__differences__with__epsilon__operations_1commoncompareimagedifferenceswithepsilonparameters).

### Compare Image Difference To Constant With Epsilon Operations[](https://docs.nvidia.com#compare-image-difference-to-constant-with-epsilon-operations)

#### Compare Image Difference With Constant Within Epsilon Operations[](https://docs.nvidia.com#group__compare__image__difference__to__constant__with__epsilon__operations_1compare_image_difference_to_constant_with_epsilon_operations)

Compare differences between image pixels and constant within an epsilon value and create a binary result image. In case of multi-channel image types, the condition must be fulfilled for all channels, otherwise the comparison is considered false. The “binary” result image is of type 8u_C1. False is represented by 0, true by NPP_MAX_8U.

##### Common parameters for nppiCompareEqualEpsC functions:[](https://docs.nvidia.com#group__compare__image__difference__to__constant__with__epsilon__operations_1CommonCompareImageDifferenceWithConstantWithinEpsilonParameters)

- param pSrc
- param nSrcStep
- param nConstant
-
constant value for single channel functions.

- param pConstants
-
pointer to a list of constants, one per color channel for multi-channel image functions.

- param pDst
- param nDstStep
- param oSizeROI
- param nEpsilon
-
epsilon tolerance value to compare to per color channel pixel absolute differences

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEpsC_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nConstant,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEpsC_32f_C1R_Ctx)

-
1 channel 32-bit floating point image compare whether image and constant are equal within epsilon.

Compare pSrc’s pixels with constant value to determine whether they are equal within a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEpsC functions:](https://docs.nvidia.com#group__compare__image__difference__to__constant__with__epsilon__operations_1commoncompareimagedifferencewithconstantwithinepsilonparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEpsC_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEpsC_32f_C3R_Ctx)

-
3 channel 32-bit floating point image compare whether image and constant are equal within epsilon.

Compare pSrc’s pixels with constant value to determine whether they are equal within a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEpsC functions:](https://docs.nvidia.com#group__compare__image__difference__to__constant__with__epsilon__operations_1commoncompareimagedifferencewithconstantwithinepsilonparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEpsC_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEpsC_32f_C4R_Ctx)

-
4 channel 32-bit floating point image compare whether image and constant are equal within epsilon.

Compare pSrc’s pixels with constant value to determine whether they are equal within a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEpsC functions:](https://docs.nvidia.com#group__compare__image__difference__to__constant__with__epsilon__operations_1commoncompareimagedifferencewithconstantwithinepsilonparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompareEqualEpsC_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pConstants,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nEpsilon,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompareEqualEpsC_32f_AC4R_Ctx)

-
4 channel 32-bit signed floating point compare whether image and constant are equal within epsilon, not affecting Alpha.

Compare pSrc’s pixels with constant value to determine whether they are equal within a difference of epsilon.

For common parameter descriptions, see

[Common parameters for nppiCompareEqualEpsC functions:](https://docs.nvidia.com#group__compare__image__difference__to__constant__with__epsilon__operations_1commoncompareimagedifferencewithconstantwithinepsilonparameters).