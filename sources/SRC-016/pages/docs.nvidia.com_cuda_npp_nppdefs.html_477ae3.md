source: https://docs.nvidia.com/cuda/npp/nppdefs.html

# Data Types, Structs, Enums, and Constants[](https://docs.nvidia.com#data-types-structs-enums-and-constants)

-
struct Npp16f
[](https://docs.nvidia.com#c.Npp16f)

-
Workarounds for cuda_fp16.h C incompatibility

[Npp16f](https://docs.nvidia.com#structnpp16f).Public Members

-
short fp16
[](https://docs.nvidia.com#c.Npp16f.fp16)

-
Original Cuda fp16 data size and format.


-
short fp16

-
enum NppiInterpolationMode
[](https://docs.nvidia.com#c.NppiInterpolationMode)

-
Filtering methods.

*Values:*-
enumerator NPPI_INTER_UNDEFINED
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_UNDEFINED)

-
Undefined filtering interpolation mode.


-
enumerator NPPI_INTER_NN
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_NN)

-
Nearest neighbor filtering.


-
enumerator NPPI_INTER_LINEAR
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_LINEAR)

-
Linear interpolation.


-
enumerator NPPI_INTER_CUBIC
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_CUBIC)

-
Cubic interpolation.


-
enumerator NPPI_INTER_CUBIC2P_BSPLINE
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_CUBIC2P_BSPLINE)

-
Two-parameter cubic filter (B=1, C=0)


-
enumerator NPPI_INTER_CUBIC2P_CATMULLROM
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_CUBIC2P_CATMULLROM)

-
Two-parameter cubic filter (B=0, C=1/2)


-
enumerator NPPI_INTER_CUBIC2P_B05C03
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_CUBIC2P_B05C03)

-
Two-parameter cubic filter (B=1/2, C=3/10)


-
enumerator NPPI_INTER_SUPER
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_SUPER)

-
Super sampling.


-
enumerator NPPI_INTER_LANCZOS
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_LANCZOS)

-
Lanczos filtering.


-
enumerator NPPI_INTER_LANCZOS3_ADVANCED
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_INTER_LANCZOS3_ADVANCED)

-
Generic Lanczos filtering with order 3.


-
enumerator NPPI_SMOOTH_EDGE
[](https://docs.nvidia.com#c.NppiInterpolationMode.NPPI_SMOOTH_EDGE)

-
Smooth edge filtering.


-
enumerator NPPI_INTER_UNDEFINED

-
enum NppiBayerGridPosition
[](https://docs.nvidia.com#c.NppiBayerGridPosition)

-
Bayer Grid Position Registration.

*Values:*-
enumerator NPPI_BAYER_BGGR
[](https://docs.nvidia.com#c.NppiBayerGridPosition.NPPI_BAYER_BGGR)

-
Default registration position BGGR.


-
enumerator NPPI_BAYER_RGGB
[](https://docs.nvidia.com#c.NppiBayerGridPosition.NPPI_BAYER_RGGB)

-
Registration position RGGB.


-
enumerator NPPI_BAYER_GBRG
[](https://docs.nvidia.com#c.NppiBayerGridPosition.NPPI_BAYER_GBRG)

-
Registration position GBRG.


-
enumerator NPPI_BAYER_GRBG
[](https://docs.nvidia.com#c.NppiBayerGridPosition.NPPI_BAYER_GRBG)

-
Registration position GRBG.


-
enumerator NPPI_BAYER_BGGR

-
enum NppiMaskSize
[](https://docs.nvidia.com#c.NppiMaskSize)

-
Fixed filter-kernel sizes.

*Values:*-
enumerator NPP_MASK_SIZE_1_X_3
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_1_X_3)

-
1 X 3 filter mask size.


-
enumerator NPP_MASK_SIZE_1_X_5
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_1_X_5)

-
1 X 5 filter mask size.


-
enumerator NPP_MASK_SIZE_3_X_1
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_3_X_1)

-
3 X 1 filter mask size, leaving space for more 1 X N type enum values.


-
enumerator NPP_MASK_SIZE_5_X_1
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_5_X_1)

-
5 X 1 filter mask size.


-
enumerator NPP_MASK_SIZE_3_X_3
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_3_X_3)

-
3 X 3 filter mask size, leaving space for more N X 1 type enum values.


-
enumerator NPP_MASK_SIZE_5_X_5
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_5_X_5)

-
5 X 5 filter mask size.


-
enumerator NPP_MASK_SIZE_7_X_7
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_7_X_7)

-
7 X 7 filter mask size.


-
enumerator NPP_MASK_SIZE_9_X_9
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_9_X_9)

-
9 X 9 filter mask size.


-
enumerator NPP_MASK_SIZE_11_X_11
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_11_X_11)

-
11 X 11 filter mask size.


-
enumerator NPP_MASK_SIZE_13_X_13
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_13_X_13)

-
13 X 13 filter mask size.


-
enumerator NPP_MASK_SIZE_15_X_15
[](https://docs.nvidia.com#c.NppiMaskSize.NPP_MASK_SIZE_15_X_15)

-
15 X 15 filter mask size.


-
enumerator NPP_MASK_SIZE_1_X_3

-
enum NppiDifferentialKernel
[](https://docs.nvidia.com#c.NppiDifferentialKernel)

-
Differential Filter types.

*Values:*-
enumerator NPP_FILTER_SOBEL
[](https://docs.nvidia.com#c.NppiDifferentialKernel.NPP_FILTER_SOBEL)

-
Differential kernel filter type sobel.


-
enumerator NPP_FILTER_SCHARR
[](https://docs.nvidia.com#c.NppiDifferentialKernel.NPP_FILTER_SCHARR)

-
Differential kernel filter type scharr.


-
enumerator NPP_FILTER_SOBEL

-
enum NppStatus
[](https://docs.nvidia.com#c.NppStatus)

-
Error Status Codes.

Almost all NPP function return error-status information using these return codes. Negative return codes indicate errors, positive return codes indicate warnings, a return code of 0 indicates success.

*Values:*-
enumerator NPP_LIBRARY_VERSION_MISMATCH_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_LIBRARY_VERSION_MISMATCH_ERROR)

-
Application and NPP library version mismatch.


-
enumerator NPP_INVALID_HOST_POINTER_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_INVALID_HOST_POINTER_ERROR)

-
Invalid host memory pointer error.


-
enumerator NPP_INVALID_DEVICE_POINTER_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_INVALID_DEVICE_POINTER_ERROR)

-
Invalid device memory pointer error.


-
enumerator NPP_LUT_PALETTE_BITSIZE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_LUT_PALETTE_BITSIZE_ERROR)

-
Color look up table bitsize error.


-
enumerator NPP_ZC_MODE_NOT_SUPPORTED_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_ZC_MODE_NOT_SUPPORTED_ERROR)

-
ZeroCrossing mode not supported error.


-
enumerator NPP_NOT_SUFFICIENT_COMPUTE_CAPABILITY
[](https://docs.nvidia.com#c.NppStatus.NPP_NOT_SUFFICIENT_COMPUTE_CAPABILITY)

-
Not sufficient Cuda compute capability error.


-
enumerator NPP_TEXTURE_BIND_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_TEXTURE_BIND_ERROR)

-
Texture bind error.


-
enumerator NPP_WRONG_INTERSECTION_ROI_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_WRONG_INTERSECTION_ROI_ERROR)

-
Wrong intersection region of interest error.


-
enumerator NPP_HAAR_CLASSIFIER_PIXEL_MATCH_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_HAAR_CLASSIFIER_PIXEL_MATCH_ERROR)

-
Haar classifier pixel match error.


-
enumerator NPP_MEMFREE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_MEMFREE_ERROR)

-
Memory free request error.


-
enumerator NPP_MEMSET_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_MEMSET_ERROR)

-
Memory set request error.


-
enumerator NPP_MEMCPY_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_MEMCPY_ERROR)

-
Memory copy request error.


-
enumerator NPP_ALIGNMENT_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_ALIGNMENT_ERROR)

-
Memory alignment error.


-
enumerator NPP_CUDA_KERNEL_EXECUTION_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_CUDA_KERNEL_EXECUTION_ERROR)

-
Cuda kernel execution error, most commonly Cuda kernel launch error.


-
enumerator NPP_STREAM_CTX_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_STREAM_CTX_ERROR)

-
Non CTX function support has been deprecated.


-
enumerator NPP_ROUND_MODE_NOT_SUPPORTED_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_ROUND_MODE_NOT_SUPPORTED_ERROR)

-
Unsupported round mode.


-
enumerator NPP_QUALITY_INDEX_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_QUALITY_INDEX_ERROR)

-
Image pixels are constant for quality index.


-
enumerator NPP_RESIZE_NO_OPERATION_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_RESIZE_NO_OPERATION_ERROR)

-
One of the output image dimensions is less than 1 pixel.


-
enumerator NPP_OVERFLOW_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_OVERFLOW_ERROR)

-
Number overflows the upper or lower limit of the data type.


-
enumerator NPP_NOT_EVEN_STEP_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NOT_EVEN_STEP_ERROR)

-
Step value is not pixel multiple.


-
enumerator NPP_HISTOGRAM_NUMBER_OF_LEVELS_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_HISTOGRAM_NUMBER_OF_LEVELS_ERROR)

-
Number of levels for histogram is less than 2.


-
enumerator NPP_LUT_NUMBER_OF_LEVELS_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_LUT_NUMBER_OF_LEVELS_ERROR)

-
Number of levels for LUT is less than 2.


-
enumerator NPP_ZERO_MASK_VALUE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_ZERO_MASK_VALUE_ERROR)

-
All values of the mask are zero.


-
enumerator NPP_CORRUPTED_DATA_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_CORRUPTED_DATA_ERROR)

-
Processed data is corrupted.


-
enumerator NPP_CHANNEL_ORDER_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_CHANNEL_ORDER_ERROR)

-
Wrong order of the destination channels.


-
enumerator NPP_DATA_TYPE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_DATA_TYPE_ERROR)

-
Data type is incorrect or not supported.


-
enumerator NPP_QUADRANGLE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_QUADRANGLE_ERROR)

-
The quadrangle is nonconvex or degenerates into triangle, line or point.


-
enumerator NPP_RECTANGLE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_RECTANGLE_ERROR)

-
Size of the rectangle region is less than or equal to 1.


-
enumerator NPP_COEFFICIENT_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_COEFFICIENT_ERROR)

-
Unallowable values of the transformation coefficients.


-
enumerator NPP_NUMBER_OF_CHANNELS_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NUMBER_OF_CHANNELS_ERROR)

-
Bad or unsupported number of channels.


-
enumerator NPP_COI_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_COI_ERROR)

-
Channel of interest is not 1, 2, or 3.


-
enumerator NPP_DIVISOR_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_DIVISOR_ERROR)

-
Divisor is equal to zero.


-
enumerator NPP_CHANNEL_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_CHANNEL_ERROR)

-
Illegal channel index.


-
enumerator NPP_STRIDE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_STRIDE_ERROR)

-
Stride is less than the row length.


-
enumerator NPP_ANCHOR_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_ANCHOR_ERROR)

-
Anchor point is outside mask.


-
enumerator NPP_MASK_SIZE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_MASK_SIZE_ERROR)

-
Lower bound is larger than upper bound.


-
enumerator NPP_RESIZE_FACTOR_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_RESIZE_FACTOR_ERROR)


-
enumerator NPP_INTERPOLATION_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_INTERPOLATION_ERROR)


-
enumerator NPP_MIRROR_FLIP_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_MIRROR_FLIP_ERROR)


-
enumerator NPP_MOMENT_00_ZERO_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_MOMENT_00_ZERO_ERROR)


-
enumerator NPP_THRESHOLD_NEGATIVE_LEVEL_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_THRESHOLD_NEGATIVE_LEVEL_ERROR)


-
enumerator NPP_THRESHOLD_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_THRESHOLD_ERROR)


-
enumerator NPP_FFT_FLAG_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_FFT_FLAG_ERROR)


-
enumerator NPP_FFT_ORDER_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_FFT_ORDER_ERROR)


-
enumerator NPP_STEP_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_STEP_ERROR)

-
Step is less or equal zero.


-
enumerator NPP_NOT_SUPPORTED_MODE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NOT_SUPPORTED_MODE_ERROR)

-
Not supported mode error.


-
enumerator NPP_CONTEXT_MATCH_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_CONTEXT_MATCH_ERROR)


-
enumerator NPP_SCALE_RANGE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_SCALE_RANGE_ERROR)


-
enumerator NPP_OUT_OFF_RANGE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_OUT_OFF_RANGE_ERROR)


-
enumerator NPP_DIVIDE_BY_ZERO_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_DIVIDE_BY_ZERO_ERROR)


-
enumerator NPP_MEMORY_ALLOCATION_ERR
[](https://docs.nvidia.com#c.NppStatus.NPP_MEMORY_ALLOCATION_ERR)


-
enumerator NPP_NULL_POINTER_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NULL_POINTER_ERROR)


-
enumerator NPP_RANGE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_RANGE_ERROR)


-
enumerator NPP_SIZE_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_SIZE_ERROR)


-
enumerator NPP_BAD_ARGUMENT_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_BAD_ARGUMENT_ERROR)


-
enumerator NPP_NO_MEMORY_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NO_MEMORY_ERROR)


-
enumerator NPP_NOT_IMPLEMENTED_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NOT_IMPLEMENTED_ERROR)


-
enumerator NPP_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_ERROR)


-
enumerator NPP_ERROR_RESERVED
[](https://docs.nvidia.com#c.NppStatus.NPP_ERROR_RESERVED)


-
enumerator NPP_NO_ERROR
[](https://docs.nvidia.com#c.NppStatus.NPP_NO_ERROR)

-
Error free operation.


-
enumerator NPP_SUCCESS
[](https://docs.nvidia.com#c.NppStatus.NPP_SUCCESS)

-
Successful operation (same as NPP_NO_ERROR)


-
enumerator NPP_NO_OPERATION_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_NO_OPERATION_WARNING)

-
Indicates that no operation was performed.


-
enumerator NPP_DIVIDE_BY_ZERO_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_DIVIDE_BY_ZERO_WARNING)

-
Divisor is zero however does not terminate the execution.


-
enumerator NPP_AFFINE_QUAD_INCORRECT_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_AFFINE_QUAD_INCORRECT_WARNING)

-
Indicates that the quadrangle passed to one of affine warping functions doesn’t have necessary properties.

First 3 vertices are used, the fourth vertex discarded.


-
enumerator NPP_WRONG_INTERSECTION_ROI_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_WRONG_INTERSECTION_ROI_WARNING)

-
The given ROI has no intersection with either the source or destination ROI.

Thus no operation was performed.


-
enumerator NPP_WRONG_INTERSECTION_QUAD_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_WRONG_INTERSECTION_QUAD_WARNING)

-
The given quadrangle has no intersection with either the source or destination ROI.

Thus no operation was performed.


-
enumerator NPP_DOUBLE_SIZE_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_DOUBLE_SIZE_WARNING)

-
Image size isn’t multiple of two.

Indicates that in case of 422/411/420 sampling the ROI width/height was modified for proper processing.


-
enumerator NPP_MISALIGNED_DST_ROI_WARNING
[](https://docs.nvidia.com#c.NppStatus.NPP_MISALIGNED_DST_ROI_WARNING)

-
Speed reduction due to uncoalesced memory accesses warning.


-
enumerator NPP_LIBRARY_VERSION_MISMATCH_ERROR

-
struct NppLibraryVersion
[](https://docs.nvidia.com#c.NppLibraryVersion)

-
NPPLibraryVersion This struct contains the NPP Library Version information.


-
typedef unsigned char Npp8u
[](https://docs.nvidia.com#c.Npp8u)

-
8-bit unsigned chars


-
typedef signed char Npp8s
[](https://docs.nvidia.com#c.Npp8s)

-
8-bit signed chars


-
typedef unsigned short Npp16u
[](https://docs.nvidia.com#c.Npp16u)

-
16-bit unsigned integers


-
typedef short Npp16s
[](https://docs.nvidia.com#c.Npp16s)

-
16-bit signed integers


-
typedef unsigned int Npp32u
[](https://docs.nvidia.com#c.Npp32u)

-
32-bit unsigned integers


-
typedef int Npp32s
[](https://docs.nvidia.com#c.Npp32s)

-
32-bit signed integers


-
typedef unsigned long long Npp64u
[](https://docs.nvidia.com#c.Npp64u)

-
64-bit unsigned integers


-
typedef long long Npp64s
[](https://docs.nvidia.com#c.Npp64s)

-
64-bit signed integers


-
typedef float Npp32f
[](https://docs.nvidia.com#c.Npp32f)

-
32-bit (IEEE) floating-point numbers


-
typedef double Npp64f
[](https://docs.nvidia.com#c.Npp64f)

-
64-bit floating-point numbers


-
struct Npp8uc
[](https://docs.nvidia.com#c.Npp8uc)

-
Complex Number This struct represents an unsigned char complex number.


-
struct Npp16uc
[](https://docs.nvidia.com#c.Npp16uc)

-
Complex Number This struct represents an unsigned short complex number.


-
struct Npp16sc
[](https://docs.nvidia.com#c.Npp16sc)

-
Complex Number This struct represents a short complex number.


-
struct Npp32uc
[](https://docs.nvidia.com#c.Npp32uc)

-
Complex Number This struct represents an unsigned int complex number.


-
struct Npp32sc
[](https://docs.nvidia.com#c.Npp32sc)

-
Complex Number This struct represents a signed int complex number.


-
struct Npp32fc
[](https://docs.nvidia.com#c.Npp32fc)

-
Complex Number This struct represents a single floating-point complex number.


-
struct Npp64sc
[](https://docs.nvidia.com#c.Npp64sc)

-
Complex Number This struct represents a long long complex number.


-
struct Npp64fc
[](https://docs.nvidia.com#c.Npp64fc)

-
Complex Number This struct represents a double floating-point complex number.


-
enum NppDataType
[](https://docs.nvidia.com#c.NppDataType)

-
Data types for nppiPlus functions.

*Values:*-
enumerator NPP_8U
[](https://docs.nvidia.com#c.NppDataType.NPP_8U)

-
8-bit unsigned integer data type


-
enumerator NPP_8S
[](https://docs.nvidia.com#c.NppDataType.NPP_8S)

-
8-bit signed integer data type


-
enumerator NPP_16U
[](https://docs.nvidia.com#c.NppDataType.NPP_16U)

-
16-bit unsigned integer data type


-
enumerator NPP_16S
[](https://docs.nvidia.com#c.NppDataType.NPP_16S)

-
16-bit signed integer data type


-
enumerator NPP_32U
[](https://docs.nvidia.com#c.NppDataType.NPP_32U)

-
32-bit unsigned integer data type


-
enumerator NPP_32S
[](https://docs.nvidia.com#c.NppDataType.NPP_32S)

-
32-bit signed integer data type


-
enumerator NPP_64U
[](https://docs.nvidia.com#c.NppDataType.NPP_64U)

-
64-bit unsigned integer data type


-
enumerator NPP_64S
[](https://docs.nvidia.com#c.NppDataType.NPP_64S)

-
64-bit signed integer data type


-
enumerator NPP_16F
[](https://docs.nvidia.com#c.NppDataType.NPP_16F)

-
16-bit original Cuda floating point data type


-
enumerator NPP_32F
[](https://docs.nvidia.com#c.NppDataType.NPP_32F)

-
32-bit floating point data type


-
enumerator NPP_64F
[](https://docs.nvidia.com#c.NppDataType.NPP_64F)

-
64-bit double precision floating point data type


-
enumerator NPP_8U

-
enum NppiChannels
[](https://docs.nvidia.com#c.NppiChannels)

-
Image channel counts for nppiPlus functions.

*Values:*-
enumerator NPP_CH_1
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_1)

-
Single channel per pixel data.


-
enumerator NPP_CH_2
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_2)

-
Two channel per pixel data.


-
enumerator NPP_CH_3
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_3)

-
Three channel per pixel data.


-
enumerator NPP_CH_4
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_4)

-
Four channel per pixel data.


-
enumerator NPP_CH_A4
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_A4)

-
Four channel per pixel data with alpha.


-
enumerator NPP_CH_P2
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_P2)

-
Two channel single channel per plane pixel data.


-
enumerator NPP_CH_P3
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_P3)

-
Three channel single channel per plane pixel data.


-
enumerator NPP_CH_P4
[](https://docs.nvidia.com#c.NppiChannels.NPP_CH_P4)

-
Four channel single channel per plane pixel data.


-
enumerator NPP_CH_1

-
NPP_MIN_8U
[](https://docs.nvidia.com#c.NPP_MIN_8U)

-
Minimum 8-bit unsigned integer.


-
NPP_MAX_8U
[](https://docs.nvidia.com#c.NPP_MAX_8U)

-
Maximum 8-bit unsigned integer.


-
NPP_MIN_16U
[](https://docs.nvidia.com#c.NPP_MIN_16U)

-
Minimum 16-bit unsigned integer.


-
NPP_MAX_16U
[](https://docs.nvidia.com#c.NPP_MAX_16U)

-
Maximum 16-bit unsigned integer.


-
NPP_MIN_32U
[](https://docs.nvidia.com#c.NPP_MIN_32U)

-
Minimum 32-bit unsigned integer.


-
NPP_MAX_32U
[](https://docs.nvidia.com#c.NPP_MAX_32U)

-
Maximum 32-bit unsigned integer.


-
NPP_MIN_64U
[](https://docs.nvidia.com#c.NPP_MIN_64U)

-
Minimum 64-bit unsigned integer.


-
NPP_MAX_64U
[](https://docs.nvidia.com#c.NPP_MAX_64U)

-
Maximum 64-bit unsigned integer.


-
NPP_MIN_8S
[](https://docs.nvidia.com#c.NPP_MIN_8S)

-
Minimum 8-bit signed integer.


-
NPP_MAX_8S
[](https://docs.nvidia.com#c.NPP_MAX_8S)

-
Maximum 8-bit signed integer.


-
NPP_MIN_16S
[](https://docs.nvidia.com#c.NPP_MIN_16S)

-
Minimum 16-bit signed integer.


-
NPP_MAX_16S
[](https://docs.nvidia.com#c.NPP_MAX_16S)

-
Maximum 16-bit signed integer.


-
NPP_MIN_32S
[](https://docs.nvidia.com#c.NPP_MIN_32S)

-
Minimum 32-bit signed integer.


-
NPP_MAX_32S
[](https://docs.nvidia.com#c.NPP_MAX_32S)

-
Maximum 32-bit signed integer.


-
NPP_MIN_64S
[](https://docs.nvidia.com#c.NPP_MIN_64S)

-
Minimum 64-bit signed integer.


-
NPP_MAX_64S
[](https://docs.nvidia.com#c.NPP_MAX_64S)

-
Minimum 64-bit signed integer.


-
NPP_MINABS_32F
[](https://docs.nvidia.com#c.NPP_MINABS_32F)

-
Smallest positive 32-bit floating point value.


-
NPP_MAXABS_32F
[](https://docs.nvidia.com#c.NPP_MAXABS_32F)

-
Largest positive 32-bit floating point value.


-
NPP_MINABS_64F
[](https://docs.nvidia.com#c.NPP_MINABS_64F)

-
Smallest positive 64-bit floating point value.


-
NPP_MAXABS_64F
[](https://docs.nvidia.com#c.NPP_MAXABS_64F)

-
Largest positive 64-bit floating point value.


-
struct NppiPoint
[](https://docs.nvidia.com#c.NppiPoint)

-
2D Point


-
struct NppiPoint32f
[](https://docs.nvidia.com#c.NppiPoint32f)

-
2D Npp32f Point


-
struct NppiPoint64f
[](https://docs.nvidia.com#c.NppiPoint64f)

-
2D Npp64f Point


-
struct NppPointPolar
[](https://docs.nvidia.com#c.NppPointPolar)

-
2D Polar Point


-
struct NppiSize
[](https://docs.nvidia.com#c.NppiSize)

-
2D Size This struct typically represents the size of a a rectangular region in two space.


-
struct NppiRect
[](https://docs.nvidia.com#c.NppiRect)

-
2D Rectangle This struct contains position and size information of a rectangle in two space.

The rectangle’s position is usually signified by the coordinate of its upper-left corner.


-
enum NppiAxis
[](https://docs.nvidia.com#c.NppiAxis)

-
nppiMirror direction controls

*Values:*-
enumerator NPP_HORIZONTAL_AXIS
[](https://docs.nvidia.com#c.NppiAxis.NPP_HORIZONTAL_AXIS)

-
Flip around horizontal axis in mirror function.


-
enumerator NPP_VERTICAL_AXIS
[](https://docs.nvidia.com#c.NppiAxis.NPP_VERTICAL_AXIS)

-
Flip around vertical axis in mirror function.


-
enumerator NPP_BOTH_AXIS
[](https://docs.nvidia.com#c.NppiAxis.NPP_BOTH_AXIS)

-
Flip around both axes in mirror function.


-
enumerator NPP_HORIZONTAL_AXIS

-
enum NppCmpOp
[](https://docs.nvidia.com#c.NppCmpOp)

-
Pixel comparison control values.

*Values:*-
enumerator NPP_CMP_LESS
[](https://docs.nvidia.com#c.NppCmpOp.NPP_CMP_LESS)

-
Threshold test for less than.


-
enumerator NPP_CMP_LESS_EQ
[](https://docs.nvidia.com#c.NppCmpOp.NPP_CMP_LESS_EQ)

-
Threshold test for less than or equal.


-
enumerator NPP_CMP_EQ
[](https://docs.nvidia.com#c.NppCmpOp.NPP_CMP_EQ)

-
Threshold test for equal.


-
enumerator NPP_CMP_GREATER_EQ
[](https://docs.nvidia.com#c.NppCmpOp.NPP_CMP_GREATER_EQ)

-
Threshold test for greater than or equal.


-
enumerator NPP_CMP_GREATER
[](https://docs.nvidia.com#c.NppCmpOp.NPP_CMP_GREATER)

-
Threshold test for greater than.


-
enumerator NPP_CMP_LESS

-
enum NppRoundMode
[](https://docs.nvidia.com#c.NppRoundMode)

-
Rounding Modes.

The enumerated rounding modes are used by a large number of NPP primitives to allow the user to specify the method by which fractional values are converted to integer values. Also see

[Rounding Modes](https://docs.nvidia.com/introduction.html#general_conventions_lb_1rounding_modes).For NPP release 5.5 new names for the three rounding modes are introduced that are based on the naming conventions for rounding modes set forth in the IEEE-754 floating-point standard. Developers are encouraged to use the new, longer names to be future proof as the legacy names will be deprecated in subsequent NPP releases.

*Values:*-
enumerator NPP_RND_NEAR
[](https://docs.nvidia.com#c.NppRoundMode.NPP_RND_NEAR)

-
Round to the nearest even integer.

All fractional numbers are rounded to their nearest integer. The ambiguous cases (i.e. <integer>.5) are rounded to the closest even integer. E.g.

roundNear(0.5) = 0

roundNear(0.6) = 1

roundNear(1.5) = 2

roundNear(-1.5) = -2



-
enumerator NPP_ROUND_NEAREST_TIES_TO_EVEN
[](https://docs.nvidia.com#c.NppRoundMode.NPP_ROUND_NEAREST_TIES_TO_EVEN)

-
Alias name for NPP_RND_NEAR.


-
enumerator NPP_RND_FINANCIAL
[](https://docs.nvidia.com#c.NppRoundMode.NPP_RND_FINANCIAL)

-
Round according to financial rule.

All fractional numbers are rounded to their nearest integer. The ambiguous cases (i.e. <integer>.5) are rounded away from zero. E.g.

roundFinancial(0.4) = 0

roundFinancial(0.5) = 1

roundFinancial(-1.5) = -2



-
enumerator NPP_ROUND_NEAREST_TIES_AWAY_FROM_ZERO
[](https://docs.nvidia.com#c.NppRoundMode.NPP_ROUND_NEAREST_TIES_AWAY_FROM_ZERO)

-
Alias name for NPP_RND_FINANCIAL.


-
enumerator NPP_RND_ZERO
[](https://docs.nvidia.com#c.NppRoundMode.NPP_RND_ZERO)

-
Round towards zero (truncation).

All fractional numbers of the form <integer>.<decimals> are truncated to <integer>.

roundZero(1.5) = 1

roundZero(1.9) = 1

roundZero(-2.5) = -2



-
enumerator NPP_ROUND_TOWARD_ZERO
[](https://docs.nvidia.com#c.NppRoundMode.NPP_ROUND_TOWARD_ZERO)

-
Alias name for NPP_RND_ZERO.


-
enumerator NPP_RND_NEAR

-
enum NppiBorderType
[](https://docs.nvidia.com#c.NppiBorderType)

-
Supported image border modes.

*Values:*-
enumerator NPP_BORDER_UNDEFINED
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_UNDEFINED)

-
Image border type undefined.


-
enumerator NPP_BORDER_NONE
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_NONE)

-
Image border type none.


-
enumerator NPP_BORDER_CONSTANT
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_CONSTANT)

-
Image border type constant value.


-
enumerator NPP_BORDER_REPLICATE
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_REPLICATE)

-
Image border type replicate border pixels.


-
enumerator NPP_BORDER_WRAP
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_WRAP)

-
Image border type wrap border pixels.


-
enumerator NPP_BORDER_MIRROR
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_MIRROR)

-
Image border type mirror border pixels (IPP mirrored border / OpenCV BORDER_REFLECT_101): gfedcb|abcdefgh|gfedcba — edge pixel is NOT repeated.


-
enumerator NPP_BORDER_MIRROR_REFL
[](https://docs.nvidia.com#c.NppiBorderType.NPP_BORDER_MIRROR_REFL)

-
Image border type mirror with replication (IPP mirrored border with replication / OpenCV BORDER_REFLECT): fedcba|abcdefgh|hgfedcba — edge pixel IS repeated.


-
enumerator NPP_BORDER_UNDEFINED

-
enum NppHintAlgorithm
[](https://docs.nvidia.com#c.NppHintAlgorithm)

-
Hints.

*Values:*-
enumerator NPP_ALG_HINT_NONE
[](https://docs.nvidia.com#c.NppHintAlgorithm.NPP_ALG_HINT_NONE)

-
Hint none, currently these are all ignored.


-
enumerator NPP_ALG_HINT_FAST
[](https://docs.nvidia.com#c.NppHintAlgorithm.NPP_ALG_HINT_FAST)

-
Hint fast, currently these are all ignored.


-
enumerator NPP_ALG_HINT_ACCURATE
[](https://docs.nvidia.com#c.NppHintAlgorithm.NPP_ALG_HINT_ACCURATE)

-
Hint accurate, currently these are all ignored.


-
enumerator NPP_ALG_HINT_NONE

-
enum NppiAlphaOp
[](https://docs.nvidia.com#c.NppiAlphaOp)

-
Alpha composition mode controls.

*Values:*-
enumerator NPPI_OP_ALPHA_OVER
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_OVER)

-
Alpha composition over operation.


-
enumerator NPPI_OP_ALPHA_IN
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_IN)

-
Alpha composition in operation.


-
enumerator NPPI_OP_ALPHA_OUT
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_OUT)

-
Alpha composition out operation.


-
enumerator NPPI_OP_ALPHA_ATOP
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_ATOP)

-
Alpha composition atop operation.


-
enumerator NPPI_OP_ALPHA_XOR
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_XOR)

-
Alpha composition xor operation.


-
enumerator NPPI_OP_ALPHA_PLUS
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_PLUS)

-
Alpha composition plus operation.


-
enumerator NPPI_OP_ALPHA_OVER_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_OVER_PREMUL)

-
Alpha composition over premultiply operation.


-
enumerator NPPI_OP_ALPHA_IN_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_IN_PREMUL)

-
Alpha composition in premultiply operation.


-
enumerator NPPI_OP_ALPHA_OUT_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_OUT_PREMUL)

-
Alpha composition out premultiply operation.


-
enumerator NPPI_OP_ALPHA_ATOP_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_ATOP_PREMUL)

-
Alpha composition atop premultiply operation.


-
enumerator NPPI_OP_ALPHA_XOR_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_XOR_PREMUL)

-
Alpha composition xor premultiply operation.


-
enumerator NPPI_OP_ALPHA_PLUS_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_PLUS_PREMUL)

-
Alpha composition plus premultiply operation.


-
enumerator NPPI_OP_ALPHA_PREMUL
[](https://docs.nvidia.com#c.NppiAlphaOp.NPPI_OP_ALPHA_PREMUL)

-
Alpha composition premultiply operation.


-
enumerator NPPI_OP_ALPHA_OVER

-
struct NppiHOGConfig
[](https://docs.nvidia.com#c.NppiHOGConfig)

-
The

[NppiHOGConfig](https://docs.nvidia.com#structnppihogconfig)structure defines the configuration parameters for the HOG descriptor:

-
NPP_HOG_MAX_CELL_SIZE
[](https://docs.nvidia.com#c.NPP_HOG_MAX_CELL_SIZE)

-
HOG Cell controls.

max horizontal/vertical pixel size of cell.


-
NPP_HOG_MAX_BLOCK_SIZE
[](https://docs.nvidia.com#c.NPP_HOG_MAX_BLOCK_SIZE)

-
max horizontal/vertical pixel size of block.


-
NPP_HOG_MAX_BINS_PER_CELL
[](https://docs.nvidia.com#c.NPP_HOG_MAX_BINS_PER_CELL)

-
max number of histogram bins.


-
NPP_HOG_MAX_CELLS_PER_DESCRIPTOR
[](https://docs.nvidia.com#c.NPP_HOG_MAX_CELLS_PER_DESCRIPTOR)

-
max number of cells in a descriptor window.


-
NPP_HOG_MAX_OVERLAPPING_BLOCKS_PER_DESCRIPTOR
[](https://docs.nvidia.com#c.NPP_HOG_MAX_OVERLAPPING_BLOCKS_PER_DESCRIPTOR)

-
max number of overlapping blocks in a descriptor window.


-
NPP_HOG_MAX_DESCRIPTOR_LOCATIONS_PER_CALL
[](https://docs.nvidia.com#c.NPP_HOG_MAX_DESCRIPTOR_LOCATIONS_PER_CALL)

-
max number of descriptor window locations per function call.


-
struct NppiHaarClassifier_32f
[](https://docs.nvidia.com#c.NppiHaarClassifier_32f)

-
Data structure for HaarClassifier_32f.


-
struct NppiHaarBuffer
[](https://docs.nvidia.com#c.NppiHaarBuffer)

-
Data structure for Haar buffer.


-
enum NppsZCType
[](https://docs.nvidia.com#c.NppsZCType)

-
Signal sign operations.

*Values:*-
enumerator nppZCR
[](https://docs.nvidia.com#c.NppsZCType.nppZCR)

-
sign change


-
enumerator nppZCXor
[](https://docs.nvidia.com#c.NppsZCType.nppZCXor)

-
sign change XOR


-
enumerator nppZCC
[](https://docs.nvidia.com#c.NppsZCType.nppZCC)

-
sign change count_0


-
enumerator nppZCR

-
enum NppiHuffmanTableType
[](https://docs.nvidia.com#c.NppiHuffmanTableType)

-
HuffMan Table controls.

*Values:*-
enumerator nppiDCTable
[](https://docs.nvidia.com#c.NppiHuffmanTableType.nppiDCTable)

-
DC Table.


-
enumerator nppiACTable
[](https://docs.nvidia.com#c.NppiHuffmanTableType.nppiACTable)

-
AC Table.


-
enumerator nppiDCTable

-
enum NppiNorm
[](https://docs.nvidia.com#c.NppiNorm)

-
Norm controls.

*Values:*-
enumerator nppiNormInf
[](https://docs.nvidia.com#c.NppiNorm.nppiNormInf)

-
maximum


-
enumerator nppiNormL1
[](https://docs.nvidia.com#c.NppiNorm.nppiNormL1)

-
sum


-
enumerator nppiNormL2
[](https://docs.nvidia.com#c.NppiNorm.nppiNormL2)

-
square root of sum of squares


-
enumerator nppiNormInf

-
struct NppiConnectedRegion
[](https://docs.nvidia.com#c.NppiConnectedRegion)

-
Data structure of connected pixel region information.


-
struct NppiImageDescriptor
[](https://docs.nvidia.com#c.NppiImageDescriptor)

-
General image descriptor.

Defines the basic parameters of an image, including data pointer, step, and image size. This can be used by both source and destination images.


-
struct NppiBufferDescriptor
[](https://docs.nvidia.com#c.NppiBufferDescriptor)

-
struct

[NppiBufferDescriptor](https://docs.nvidia.com#structnppibufferdescriptor)

-
struct NppiCompressedMarkerLabelsInfo
[](https://docs.nvidia.com#c.NppiCompressedMarkerLabelsInfo)

-
Provides details of uniquely labeled pixel regions of interest returned by CompressedLabelMarkersUF function.


-
struct NppiContourBlockSegment
[](https://docs.nvidia.com#c.NppiContourBlockSegment)

-
Provides details of contour pixel grid map location and association.

Public Members


-
struct NppiContourPixelGeometryInfo
[](https://docs.nvidia.com#c.NppiContourPixelGeometryInfo)

-
Provides contour (boundary) geometry info of uniquely labeled pixel regions returned by nppiCompressedMarkerLabelsUFInfo function in host memory in counterclockwise order relative to contour interiors.

Public Members

-
[NppiPoint](https://docs.nvidia.com#c.NppiPoint)oContourOrderedGeometryLocation[](https://docs.nvidia.com#c.NppiContourPixelGeometryInfo.oContourOrderedGeometryLocation)

-
image geometry X and Y location in requested output order


-
[Npp32u](https://docs.nvidia.com#c.Npp32u)nNextContourPixelIndex[](https://docs.nvidia.com#c.NppiContourPixelGeometryInfo.nNextContourPixelIndex)

-
index of next ordered contour pixel in

[NppiContourPixelGeometryInfo](https://docs.nvidia.com#structnppicontourpixelgeometryinfo)list

-
[Npp32u](https://docs.nvidia.com#c.Npp32u)nPrevContourPixelIndex[](https://docs.nvidia.com#c.NppiContourPixelGeometryInfo.nPrevContourPixelIndex)

-
index of previous ordered contour pixel in

[NppiContourPixelGeometryInfo](https://docs.nvidia.com#structnppicontourpixelgeometryinfo)list

-

-
NPP_CONTOUR_DIRECTION_SOUTH_EAST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_SOUTH_EAST)

-
Provides contour (boundary) direction info of uniquely labeled pixel regions returned by CompressedLabelMarkersUF function.

Contour direction south east


-
NPP_CONTOUR_DIRECTION_SOUTH
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_SOUTH)

-
Contour direction south.


-
NPP_CONTOUR_DIRECTION_SOUTH_WEST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_SOUTH_WEST)

-
Contour direction south west.


-
NPP_CONTOUR_DIRECTION_WEST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_WEST)

-
Contour direction west.


-
NPP_CONTOUR_DIRECTION_EAST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_EAST)

-
Contour direction east.


-
NPP_CONTOUR_DIRECTION_NORTH_EAST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_NORTH_EAST)

-
Contour direction north east.


-
NPP_CONTOUR_DIRECTION_NORTH
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_NORTH)

-
Contour direction north.


-
NPP_CONTOUR_DIRECTION_NORTH_WEST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_NORTH_WEST)

-
Contour direction north west.


-
NPP_CONTOUR_DIRECTION_ANY_NORTH
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_ANY_NORTH)

-
Provides contour (boundary) diagonal direction info of uniquely labeled pixel regions returned by CompressedLabelMarkersUF function.

Contour direction any north


-
NPP_CONTOUR_DIRECTION_ANY_WEST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_ANY_WEST)

-
Contour direction any west.


-
NPP_CONTOUR_DIRECTION_ANY_SOUTH
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_ANY_SOUTH)

-
Contour direction any south.


-
NPP_CONTOUR_DIRECTION_ANY_EAST
[](https://docs.nvidia.com#c.NPP_CONTOUR_DIRECTION_ANY_EAST)

-
Contour direction any east.


-
struct NppiContourPixelDirectionInfo
[](https://docs.nvidia.com#c.NppiContourPixelDirectionInfo)

-
Data structure for contour pixel direction information.

Public Members

-
[Npp8u](https://docs.nvidia.com#c.Npp8u)nContourDirectionCenterPixel[](https://docs.nvidia.com#c.NppiContourPixelDirectionInfo.nContourDirectionCenterPixel)

-
provides current center contour pixel input and output direction info


-
[Npp8u](https://docs.nvidia.com#c.Npp8u)nContourInteriorDirectionCenterPixel[](https://docs.nvidia.com#c.NppiContourPixelDirectionInfo.nContourInteriorDirectionCenterPixel)

-
provides current center contour pixel region interior direction info


-
[NppiContourPixelGeometryInfo](https://docs.nvidia.com#c.NppiContourPixelGeometryInfo)oContourPixelGeometryInfo[](https://docs.nvidia.com#c.NppiContourPixelDirectionInfo.oContourPixelGeometryInfo)

-
Pixel geometry info structure.


-

-
struct NppiContourTotalsInfo
[](https://docs.nvidia.com#c.NppiContourTotalsInfo)

-
Data structure for contour total counts.


-
enum NppiWatershedSegmentBoundaryType
[](https://docs.nvidia.com#c.NppiWatershedSegmentBoundaryType)

-
Provides control of the type of segment boundaries, if any, added to the image generated by the watershed segmentation function.

*Values:*-
enumerator NPP_WATERSHED_SEGMENT_BOUNDARIES_NONE
[](https://docs.nvidia.com#c.NppiWatershedSegmentBoundaryType.NPP_WATERSHED_SEGMENT_BOUNDARIES_NONE)

-
Image watershed segment boundary type none.


-
enumerator NPP_WATERSHED_SEGMENT_BOUNDARIES_BLACK
[](https://docs.nvidia.com#c.NppiWatershedSegmentBoundaryType.NPP_WATERSHED_SEGMENT_BOUNDARIES_BLACK)

-
Image watershed segment boundary type black.


-
enumerator NPP_WATERSHED_SEGMENT_BOUNDARIES_WHITE
[](https://docs.nvidia.com#c.NppiWatershedSegmentBoundaryType.NPP_WATERSHED_SEGMENT_BOUNDARIES_WHITE)

-
Image watershed segment boundary type white.


-
enumerator NPP_WATERSHED_SEGMENT_BOUNDARIES_CONTRAST
[](https://docs.nvidia.com#c.NppiWatershedSegmentBoundaryType.NPP_WATERSHED_SEGMENT_BOUNDARIES_CONTRAST)

-
Image watershed segment boundary type contrasting intensity.


-
enumerator NPP_WATERSHED_SEGMENT_BOUNDARIES_ONLY
[](https://docs.nvidia.com#c.NppiWatershedSegmentBoundaryType.NPP_WATERSHED_SEGMENT_BOUNDARIES_ONLY)

-
Image watershed segment boundary type render boundaries only.


-
enumerator NPP_WATERSHED_SEGMENT_BOUNDARIES_NONE

-
struct NppStreamContext
[](https://docs.nvidia.com#c.NppStreamContext)

-
## Application Managed Stream Context

[](https://docs.nvidia.com#structNppStreamContext_1application_managed_stream_context)NPP stream context structure must be filled in by application.

Populate all fields as shown below. Set hWorkspace = 0 to opt out of the optional workspace cache (pass a handle from nppiWorkspaceCreate() to enable it):

NppStreamContext ctx; ctx.hStream = myStream; cudaGetDevice(&ctx.nCudaDeviceId); cudaDeviceProp props; cudaGetDeviceProperties(&props, ctx.nCudaDeviceId); ctx.nMultiProcessorCount = props.multiProcessorCount; ctx.nMaxThreadsPerMultiProcessor = props.maxThreadsPerMultiProcessor; ctx.nMaxThreadsPerBlock = props.maxThreadsPerBlock; ctx.nSharedMemPerBlock = props.sharedMemPerBlock; ctx.nCudaDevAttrComputeCapabilityMajor = props.major; ctx.nCudaDevAttrComputeCapabilityMinor = props.minor; cudaStreamGetFlags(myStream, &ctx.nStreamFlags); ctx.hWorkspace = 0; // must be zero unless using nppiWorkspaceCreate()

Public Members

-
cudaStream_t hStream
[](https://docs.nvidia.com#c.NppStreamContext.hStream)

-
From current Cuda stream ID.


-
int nCudaDeviceId
[](https://docs.nvidia.com#c.NppStreamContext.nCudaDeviceId)

-
From cudaGetDevice().


-
int nMultiProcessorCount
[](https://docs.nvidia.com#c.NppStreamContext.nMultiProcessorCount)

-
From cudaGetDeviceProperties().


-
int nMaxThreadsPerMultiProcessor
[](https://docs.nvidia.com#c.NppStreamContext.nMaxThreadsPerMultiProcessor)

-
From cudaGetDeviceProperties().


-
int nMaxThreadsPerBlock
[](https://docs.nvidia.com#c.NppStreamContext.nMaxThreadsPerBlock)

-
From cudaGetDeviceProperties().


-
From cudaGetDeviceProperties().


-
int nCudaDevAttrComputeCapabilityMajor
[](https://docs.nvidia.com#c.NppStreamContext.nCudaDevAttrComputeCapabilityMajor)

-
From cudaGetDeviceAttribute().


-
int nCudaDevAttrComputeCapabilityMinor
[](https://docs.nvidia.com#c.NppStreamContext.nCudaDevAttrComputeCapabilityMinor)

-
From cudaGetDeviceAttribute().


-
unsigned int nStreamFlags
[](https://docs.nvidia.com#c.NppStreamContext.nStreamFlags)

-
From cudaStreamGetFlags().


-
NppWorkspace hWorkspace
[](https://docs.nvidia.com#c.NppStreamContext.hWorkspace)

-
Optional workspace handle; 0 = no workspace.

Set via nppiWorkspaceCreate().


-
[Npp32u](https://docs.nvidia.com#c.Npp32u)nReserved0[](https://docs.nvidia.com#c.NppStreamContext.nReserved0)

-
-
*Deprecated:* -
Use hWorkspace. Same type and storage, kept for source compatibility with existing code that sets nReserved0 = 0.


-

-
union
[NppStreamContext](https://docs.nvidia.com#c.NppStreamContext).[anonymous] [anonymous][](https://docs.nvidia.com#c.NppStreamContext.@1)


-
cudaStream_t hStream

-
struct NppiResizeBatchCXR
[](https://docs.nvidia.com#c.NppiResizeBatchCXR)

-
NPP Batch Geometry Structure Definitions.


-
struct NppiResizeBatchROI_Advanced
[](https://docs.nvidia.com#c.NppiResizeBatchROI_Advanced)

-
Data structure for variable ROI image batch resizing.


-
struct NppiMirrorBatchCXR
[](https://docs.nvidia.com#c.NppiMirrorBatchCXR)

-
Data structure for batched nppiMirrorBatch.


-
struct NppiWarpAffineBatchCXR
[](https://docs.nvidia.com#c.NppiWarpAffineBatchCXR)

-
Data structure for batched nppiWarpAffineBatch.

Public Members

-
const void *pSrc
[](https://docs.nvidia.com#c.NppiWarpAffineBatchCXR.pSrc)

-
source image device memory pointer.


-
int nSrcStep
[](https://docs.nvidia.com#c.NppiWarpAffineBatchCXR.nSrcStep)

-
source image byte count per row.


-
void *pDst
[](https://docs.nvidia.com#c.NppiWarpAffineBatchCXR.pDst)

-
destination image device memory pointer.


-
int nDstStep
[](https://docs.nvidia.com#c.NppiWarpAffineBatchCXR.nDstStep)

-
device image byte count per row.


-
const void *pSrc

-
struct NppiWarpPerspectiveBatchCXR
[](https://docs.nvidia.com#c.NppiWarpPerspectiveBatchCXR)

-
Data structure for batched nppiWarpPerspectiveBatch.

Public Members

-
const void *pSrc
[](https://docs.nvidia.com#c.NppiWarpPerspectiveBatchCXR.pSrc)

-
source image device memory pointer.


-
int nSrcStep
[](https://docs.nvidia.com#c.NppiWarpPerspectiveBatchCXR.nSrcStep)

-
source image byte count per row.


-
void *pDst
[](https://docs.nvidia.com#c.NppiWarpPerspectiveBatchCXR.pDst)

-
destination image device memory pointer.


-
int nDstStep
[](https://docs.nvidia.com#c.NppiWarpPerspectiveBatchCXR.nDstStep)

-
device image byte count per row.


-
const void *pSrc

-
struct NppiColorTwistBatchCXR
[](https://docs.nvidia.com#c.NppiColorTwistBatchCXR)

-
Data structure for batched nppiColorTwistBatch.