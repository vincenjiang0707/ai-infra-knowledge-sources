source: https://docs.nvidia.com/cuda/npp/introduction.html

# What is NPP ?[](https://docs.nvidia.com#what-is-npp)

NVIDIA NPP is a library of functions for performing CUDA accelerated 2D image and signal processing.

The primary set of functionality in the library focuses on image processing and is widely applicable for developers in these areas. NPP will evolve over time to encompass more of the compute heavy tasks in a variety of problem domains. The NPP library is written to maximize flexibility, while maintaining high performance.

NPP can be used in one of two ways:

A stand-alone library for adding GPU acceleration to an application with minimal effort. Using this route allows developers to add GPU acceleration to their applications in a matter of hours.

A cooperative library for interoperating with a developer’s GPU code efficiently.


Either route allows developers to harness the massive compute resources of NVIDIA GPUs, while simultaneously reducing development times. After reading this Main Page it is recommended that you read the General API Conventions page below and either the Image-Processing Specific API Conventions page or Signal-Processing Specific API Conventions page depending on the kind of processing you expect to do. Finally, if you select the Modules tab at the top of this page you can find the kinds of functions available for the NPP operations that support your needs.

[What is NPP?](https://docs.nvidia.com#introduction_lb) [general_conventions_lb](https://docs.nvidia.com#general_conventions_lb) [nppi_conventions_lb](https://docs.nvidia.com#nppi_conventions_lb) [npps_conventions_lb](https://docs.nvidia.com#npps_conventions_lb)

## Files[](https://docs.nvidia.com#introduction_lb_1Files)

NPP API is defined in the following files:

### Header Files[](https://docs.nvidia.com#introduction_lb_1header_files)

npp.h

nppdefs.h

nppcore.h

nppi.h

npps.h


All those header files are located in the following CUDA Toolkit’s directory:

```
/include/
```

### Library Files[](https://docs.nvidia.com#introduction_lb_1library_files)

NPP’s functionality is split up into 3 distinct library groups:

A core library (NPPC) containing basic functionality from the npp.h header file as well as common functionality used by the other two libraries.

The image processing library NPPI. Any functions from the nppi.h header file or the various header files named “nppi_xxx.h” are bundled into the NPPI library.

The signal processing library NPPS. Any function from the npps.h header file or the various header files named “npps_xxx.h” are bundled into the NPPS library.


On the Windows platform the NPP stub libraries are found in the CUDA Toolkit’s library directory:

```
/lib/nppc.lib
```

```
/lib/nppial.lib
```

```
/lib/nppicc.lib
```

```
/lib/nppidei.lib
```

```
/lib/nppif.lib
```

```
/lib/nppig.lib
```

```
/lib/nppim.lib
```

```
/lib/nppist.lib
```

```
/lib/nppisu.lib
```

```
/lib/nppitc.lib
```

```
/lib/npps.lib
```

The matching DLLs are located in the CUDA Toolkit’s binary directory. Example

```
* /bin/nppial64_111_<build_no>.dll // Dynamic image-processing library for 64-bit Windows.
```

On Linux platforms the dynamic libraries are located in the lib directory and the names include major and minor version numbers along with build numbers

```
* /lib/libnppc.so.11.1.<build_no> // NPP dynamic core library for Linux
```

## Library Organization[](https://docs.nvidia.com#introduction_lb_1NPP)

Note: To minimize library loading and CUDA runtime startup times it is recommended to use the static library(s) whenever possible. To improve loading and runtime performance when using dynamic libraries, NPP provides a full set of NPPI sub-libraries. Linking to only the sub-libraries that contain functions that your application uses can significantly improve load time and runtime startup performance. Some NPPI functions make calls to other NPPI and/or NPPS functions internally so you may need to link to a few extra libraries depending on what function calls your application makes. The NPPI sub-libraries are split into sections corresponding to the way that NPPI header files are split. This list of sub-libraries is as follows:

NPPC, NPP core library which MUST be included when linking any application, functions are listed in nppCore.h,

NPPIAL, arithmetic and logical operation functions in nppi_arithmetic_and_logical_operations.h,

NPPICC, color conversion and sampling functions in nppi_color_conversion.h,

NPPIDEI, data exchange and initialization functions in nppi_data_exchange_and_initialization.h,

NPPIF, filtering and computer vision functions in nppi_filtering_functions.h,

NPPIG, geometry transformation functions found in nppi_geometry_transforms.h,

NPPIM, morphological operation functions found in nppi_morphological_operations.h,

NPPIST, statistics and linear transform in nppi_statistics_functions.h and nppi_linear_transforms.h,

NPPISU, memory support functions in nppi_support_functions.h,

NPPITC, threshold and compare operation functions in nppi_threshold_and_compare_operations.h,


For example, on Linux, to compile a small color conversion application `foo`

using NPP against the dynamic library, the following command can be used:

```
nvcc foo.c -lnppc -lnppicc -o foo
```

Whereas to compile against the static NPP library, the following command has to be used:

```
nvcc foo.c -lnppc_static -lnppicc_static -o foo
```

It is also possible to use the native host C++ compiler. Depending on the host operating system, some additional libraries like pthread or dl might be needed on the linking line. The following command on Linux is suggested:

```
g++ foo.c -lnppc_static -lnppicc_static -lcudart_static -lpthread -ldl
-I <cuda-toolkit-path>/include -L <cuda-toolkit-path>/lib64 -o foo
```

NPP_Plus and NPP are stateless APIs. The default stream ID on any GPU device is 0. NPP_Plus and NPP applications using version 12.5 or greater MUST use the fully stateless application managed stream context interface described below. Also, the only function that remains in nppcore.h is nppGetVersion. The application can create one application managed stream context which can be modified on the fly or many appliction managed stream contexts each of which is unique to particular streams and/or GPU devices. The lifetime of application managed stream contexts are determined by the application. In general it is recommended to limit the number of unique application managed stream contexts to the number of GPUs in use as reinitializing an application managed stream context can have high overhead due to the need for CUDA device calls. However the stream ID of a single application managed stream context can be changed on the fly as needed with no extra overhead. It is the responsibility of the application to detect and respond to GPU resets if they happen and to reinitialize any existing application managed stream contexts. Calling older NPP non application managed stream context functions will now return the new NPP_STREAM_CONTEXt_ERROR value.

All NPP functions should be thread safe.

Note: In NPP 12.4 in order to support very large images NPP 12.4 and beyond has change the return value from GetBufferSize calls for statistics functions and a few others from int to size_t. Signal lengths have also changed from int to size_t. This should be the only change required for applications to be rebuilt using these versions of NPP.

Note: NPP 12.1 is the last release of NPP which will support NPP API calls that do not contain NPP stream context parameters. Also NPP will soon release an API variant that provides collapsed combined parameter versions of many API calls. For example a call like nppiAdd_8u_C3R_Ctx(pSrc1, nSrc1Step, pSrc2, nSrc2Step, pDst, nDstStep, oSizeROI, nppStreamCtx) will become nppiAdd_Ctx(NPP_8U, NPP_CH_3, pSrc1, nSrc1Step, pSrc2, nSrcStep2, pDst, nDstStep, oSizeROI, nppStreamCtx). This makes adding support for new data types and number of channels simpler as well as significantly reducing redundant documentation.

Note: New to NPP 11.6 are

```
nppiContoursImageMarchingSquaresInterpolation_32f_C1R_Ctx
```

```
nppiContoursImageMarchingSquaresInterpolation_64f_C1R_Ctx
```

Note: New to NPP 10.1 is support for the fp16 (__half) data type in GPU architectures of Volta and beyond in some NPP image processing functions. NPP image functions that support pixels of __half data types have function names of type 16f and pointers to pixels of that data type need to be passed to NPP as NPP data type [Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f). Here is an example of how to pass image pointers of type __half to an NPP 16f function that should work on all compilers including Armv7.

```
nppiAdd_16f_C3R_Ctx(reinterpret_cast<const Npp16f *>((const void *)(pSrc1Data)), nSrc1Pitch,
reinterpret_cast<const Npp16f *>((const void *)(pSrc2Data)), nSrc2Pitch,
reinterpret_cast<Npp16f *>((void *)(pDstData)), nDstPitch,
oDstROI, nppStreamCtx);
```

[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context) Application Managed Stream Context

Note: Also new to NPP 10.1 is support for application managed stream contexts. Application managed stream contexts make NPP truely stateless internally allowing for rapid, no overhead, stream context switching. While it is recommended that all new NPP application code use application managed stream contexts, existing application code can continue to use nppSetStream() and nppGetStream() to manage stream contexts (also with no overhead now) but over time NPP will likely deprecate the older non-application managed stream context API. Both the new and old stream management techniques can be intermixed in applications but any NPP calls using the old API will use the stream set by the most recent call to nppSetStream() and nppGetStream() calls will also return that stream ID. All NPP function names ending in _Ctx expect application managed stream contexts to be passed as a parameter to that function. The new [NppStreamContext](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext) application managed stream context structure is defined in nppdefs.h and should be initialized by the application to the Cuda device ID and values associated with a particular stream. Applications can use multiple fixed stream contexts or change the values in a particular stream context on the fly whenever a different stream is to be used.

Note: NPP 10.2 and beyond contain an additional element in the [NppStreamContext](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext) structure named nStreamFlags which MUST also be initialized by the application. Failure to do so could unnecessarily reduce NPP performance in some functions.

Note: NPP does not support non blocking streams on Windows for devices working in WDDM mode.

Note that some of the “GetBufferSize” style functions now have application managed stream contexts associated with them and should be used with the same stream context that the associated application managed stream context NPP function will use.

Note that NPP does minimal checking of the parameters in an application managed stream context structure so it is up to the application to assure that they are correct and valid when passed to NPP functions.

Note that NPP has deprecated the nppicom JPEG compression library as of NPP 11.0, use the NVJPEG library instead.

## Supported NVIDIA Hardware[](https://docs.nvidia.com#introduction_lb_1supported_hardware)

NPP runs on all CUDA capable NVIDIA hardware. For details please see [http://www.nvidia.com/object/cuda_learn_products.html](http://www.nvidia.com/object/cuda_learn_products.html)

# General Conventions[](https://docs.nvidia.com#general-conventions)

## Memory Management[](https://docs.nvidia.com#general_conventions_lb_1memory_management_lb)

The design of all the NPP functions follows the same guidelines as other NVIDIA CUDA libraries like cuFFT and cuBLAS. That is that all pointer arguments in those APIs are device pointers.

This convention enables the individual developer to make smart choices about memory management that minimize the number of memory transfers. It also allows the user the maximum flexibility regarding which of the various memory transfer mechanisms offered by the CUDA runtime is used, e.g. synchronous or asynchronous memory transfers, zero-copy and pinned memory, etc.

The most basic steps involved in using NPP for processing data is as follows:

-
Transfer input data from the host to device using

cudaMemCpy(...)

Process data using one or several NPP functions or custom CUDA kernels

-
Transfer the result data from the device to the host using

cudaMemCpy(...)


### Scratch Buffer and Host Pointer[](https://docs.nvidia.com#general_conventions_lb_1general_scratch_buffer)

Some primitives of NPP require additional device memory buffers (scratch buffers) for calculations, e.g. signal and image reductions (Sum, Max, Min, MinMax, etc.). In order to give the NPP user maximum control regarding memory allocations and performance, it is the user’s responsibility to allocate and delete those temporary buffers. For one this has the benefit that the library will not allocate memory unbeknownst to the user. It also allows developers who invoke the same primitive repeatedly to allocate the scratch only once, improving performance and potential device-memory fragmentation.

Scratch-buffer memory is unstructured and may be passed to the primitive in uninitialized form. This allows for reuse of the same scratch buffers with any primitive require scratch memory, as long as it is sufficiently sized.

The minimum scratch-buffer size for a given primitive (e.g. [nppsSum_32f_Ctx()](https://docs.nvidia.com/signal_statistical_functions.html#group__signal__sum_1gad162782d2f33321544e747aeae94e360)) can be obtained by a companion function (e.g. [nppsSumGetBufferSize_32f_Ctx()](https://docs.nvidia.com/signal_statistical_functions.html#group__signal__sum_1ga13cd6f4e6caed4a4994e37ff0964a7e9)). The buffer size is returned via a host pointer as allocation of the scratch-buffer is performed via CUDA runtime host code.

An example to invoke signal sum primitive and allocate and free the necessary scratch memory:

```
// pSrc, pSum, pDeviceBuffer are all device pointers.
NppStreamContext nppStreamCtx; // previously initiallzed
Npp32f * pSrc;
Npp32f * pSum;
Npp8u * pDeviceBuffer;
size_t nLength = 1024;
// Allocate the device memroy.
cudaMalloc((void **)(&pSrc), sizeof(Npp32f) * nLength);
nppsSet_32f_Ctx(1.0f, pSrc, nLength, nppStreamCtx);
cudaMalloc((void **)(&pSum), sizeof(Npp32f) * 1);
// Compute the appropriate size of the scratch-memory buffer, note that nBufferSize and nLength data types have changed from int to size_t.
size_t nBufferSize;
nppsSumGetBufferSize_32f_Ctx(nLength, &nBufferSize, nppStreamCtx);
// Allocate the scratch buffer
cudaMalloc((void **)(&pDeviceBuffer), nBufferSize);
// Call the primitive with the scratch buffer
nppsSum_32f_Ctx(pSrc, nLength, pSum, pDeviceBuffer, nppStreamCtx);
Npp32f nSumHost;
cudaMemcpy(&nSumHost, pSum, sizeof(Npp32f) * 1, cudaMemcpyDeviceToHost);
printf("sum = %f\n", nSumHost); // nSumHost = 1024.0f;
// Free the device memory
cudaFree(pSrc);
cudaFree(pDeviceBuffer);
cudaFree(pSum);
```

## Function Naming[](https://docs.nvidia.com#general_conventions_lb_1npp_naming)

Since NPP is a C API and therefore does not allow for function overloading for different data-types the NPP naming convention addresses the need to differentiate between different flavors of the same algorithm or primitive function but for various data types. This disambiguation of different flavors of a primitive is done via a suffix containing data type and other disambiguating information.

In addition to the flavor suffix, all NPP functions are prefixed with by the letters “npp”. Primitives belonging to NPP’s image-processing module add the letter “i” to the npp prefix, i.e. are prefixed by “nppi”. Similarly signal-processing primitives are prefixed with “npps”.

The general naming scheme is:

```
npp<module info><PrimitiveName>_<data-type info>[_<additional flavor info>](<parameter list>)
```

The data-type information uses the same names as the Basic NPP Data Types. For example the data-type information “8u” would imply that the primitive operates on [Npp8u](https://docs.nvidia.com/nppdefs.html#group__npp__basic__types_1ga29b502b6816fc0066fd59538483a5b62) data.

If a primitive consumes different type data from what it produces, both types will be listed in the order of consumed to produced data type.

Details about the “additional flavor information” is provided for each of the NPP modules, since each problem domain uses different flavor information suffixes.

## Integer Result Scaling[](https://docs.nvidia.com#general_conventions_lb_1integer_result_scaling)

NPP signal processing and imaging primitives often operate on integer data. This integer data is usually a fixed point fractional representation of some physical magnitue (e.g. luminance). Because of this fixed-point nature of the representation many numerical operations (e.g. addition or multiplication) tend to produce results exceeding the original fixed-point range if treated as regular integers.

In cases where the results exceed the original range, these functions clamp the result values back to the valid range. E.g. the maximum positive value for a 16-bit unsigned integer is 32767. A multiplication operation of 4 * 10000 = 40000 would exceed this range. The result would be clamped to be 32767.

To avoid the level of lost information due to clamping most integer primitives allow for result scaling. Primitives with result scaling have the “Sfs” suffix in their name and provide a parameter “nScaleFactor” that controls the amount of scaling. Before the results of an operation are clamped to the valid output-data range by multiplying them with \(2^{\mbox{-nScaleFactor}}\).

Example: The primitive [nppsSqr_8u_Sfs_Ctx()](https://docs.nvidia.com/signal_arithmetic_and_logical_operations.html#group__signal__square_1ga55fa03dffc3ff0018f6a04c0ba651c3f) computes the square of 8-bit unsigned sample values in a signal (1D array of values). The maximum value of a 8-bit value is 255. The square of \(255^2 = 65025\) which would be clamped to 255 if no result scaling is performed. In order to map the maximum value of 255 to 255 in the result, one would specify an integer result scaling factor of 8, i.e. multiply each result with \(2^{-8} = \frac{1}{2^8} = \frac{1}{256}\). The final result for a signal value of 255 being squared and scaled would be:

A medium gray value of 128 would result in

## Rounding Modes[](https://docs.nvidia.com#general_conventions_lb_1rounding_modes)

Many NPP functions require converting floating-point values to integers. The [Rounding Modes](https://docs.nvidia.com#general_conventions_lb_1rounding_modes) enum lists NPP’s supported rounding modes. Not all primitives in NPP that perform rounding as part of their functionality allow the user to specify the round-mode used. Instead they use NPP’s default rounding mode, which is NPP_RND_FINANCIAL.

### Rounding Mode Parameter[](https://docs.nvidia.com#general_conventions_lb_1rounding_mode_parameter)

A subset of NPP functions performing rounding as part of their functionality do allow the user to specify which rounding mode is used through a parameter of the [Rounding Modes](https://docs.nvidia.com#general_conventions_lb_1rounding_modes) type.

# Image Processing Conventions[](https://docs.nvidia.com#image-processing-conventions)

## Function Naming[](https://docs.nvidia.com#nppi_conventions_lb_1nppi_naming)

Image processing related functions use a number of suffixes to indicate various different flavors of a primitive beyond just different data types. The flavor suffix uses the following abbreviations:

”A” if the image is a 4 channel image this indicates the result alpha channel is not affected by the primitive.

”Cn” the image consists of n channel packed pixels, where n can be 1, 2, 3 or 4.

”Pn” the image consists of n separate image planes, where n can be 1, 2, 3 or 4.

”C” (following the channel information) indicates that the primitive only operates on one of the color channels, the “channel-of-interest”. All other output channels are not affected by the primitive.

”I” indicates that the primitive works “in-place”. In this case the image-data pointer is usually named

`pSrcDst`

to indicate that the image data serves as source and destination at the same time.”M” indicates “masked operation”. These types of primitives have an additional “mask image” as as input. Each pixel in the destination image corresponds to a pixel in the mask image. Only pixels with a corresponding non-zero mask pixel are being processed.

”R” indicates the primitive operates only on a rectangular region_of_interest or “ROI”. All ROI primitives take an additional input parameter of type

[NppiSize](https://docs.nvidia.com/nppdefs.html#structnppisize), which specifies the width and height of the rectangular region that the primitive should process. For details on how primitives operate on ROIs see: :ref: ‘roi_specification’.”Sfs” indicates the result values are processed by fixed scaling and saturation before they’re written out.


## Image Data[](https://docs.nvidia.com#nppi_conventions_lb_1passing_image_data)

Image data is passed to and from NPPI primitives via a pair of parameters:

A pointer to the image’s underlying data type.

A line step in bytes (also sometimes called line stride).


Passing a raw pointer to the underlying pixel data type, rather than structured (by color) channel pixel data allows usage of the function in a wide variety of situations avoiding risky type cast or expensive image data copies.

Passing the data pointer and line step individually rather than a higher-level image struct again allows for easy adoption by not requiring a specific image representation and thus avoiding awkward packing and unpacking of image data from the host application to an NPP specific image representation.


### Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1line_step)

The line step (also called “line stride” or “row step”) allows lines of oddly sized images to start on well-aligned addresses by adding a number of unused bytes at the ends of the lines. This type of line padding has been common practice in digital image processing for a long time and is not particular to GPU image processing.

The line step is the number of bytes in a line **including the padding.** An other way to interpret this number is to say that it is the number of bytes between the first pixels of successive rows in the image, or generally the number of bytes between two neighboring pixels in any column of pixels.

The general reason for the existence of the line step it is that uniformly aligned rows of pixel enable optimizations of memory-access patterns.

Even though all functions in NPP will work with arbitrarily aligned images, best performance can only be achieved with well aligned image data. Any image data allocated with the NPP image allocators or the 2D memory allocators in the CUDA runtime, is well aligned.

Particularly on older CUDA capable GPUs it is likely that the performance decrease for misaligned data is substantial (orders of magnitude).

All image data passed to NPPI primitives requires a line step to be provided. It is important to keep in mind that this line step is always specified in terms of bytes, not pixels.

### Parameter Names for Image Data[](https://docs.nvidia.com#nppi_conventions_lb_1image_data_parameter_names)

There are three general cases of image-data passing throughout NPP detailed in the following sections.

#### Passing Source-Image Data[](https://docs.nvidia.com#nppi_conventions_lb_1source_image)

Those are images consumed by the algorithm.

#### Source-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1source_image_pointer)

The source image data is generally passed via a pointer named

```
pSrc
```

```
nppiPrimitive_32s_C1R_Ctx(const Npp32s * pSrc, ...)
```

```
pSrc1, pScr2, ...
```

#### Source-Batch-Images Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1source_batch_images_pointer)

The batch of source images data is generally passed via a pointer of [NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor) type named

```
pSrcBatchList
```

```
nppiYUVToRGBBatch_8u_C3R_Ctx(NppiSize oSizeROI, const NppiImageDescriptor* pSrcBatchList, ...)
```

#### Source-Planar-Image Pointer Array[](https://docs.nvidia.com#nppi_conventions_lb_1source_planar_image_pointer_array)

The planar source image data is generally passed via an array of pointers named

```
pSrc[]
```

```
nppiPrimitive_8u_P3R_Ctx(const Npp8u * const pSrc[3], ...)
```

#### Source-Planar-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1source_planar_image_pointer)

The multiple plane source image data is passed via a set of pointers named

```
pSrc1, pSrc2, ...
```

#### Source-Image Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1source_image_line_step)

The source image line step is the number of bytes between successive rows in the image. The source image line step parameter is

```
nSrcStep
```

```
nSrcStep1, nSrcStep2, ...
```

#### Source-Planar-Image Line Step Array[](https://docs.nvidia.com#nppi_conventions_lb_1source_planar_image_line_step_array)

The source planar image line step array is an array where each element of the array contains the number of bytes between successive rows for a particular plane in the input image. The source planar image line step array parameter is

```
rSrcStep[]
```

#### Source-Planar-Image Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1source_planar_image_line_step)

The source planar image line step is the number of bytes between successive rows in a particular plane of the multiplane input image. The source planar image line step parameter is

```
nSrcStep1, nSrcStep2, ...
```

#### Passing Destination-Image Data[](https://docs.nvidia.com#nppi_conventions_lb_1destination_image)

Those are images produced by the algorithm.

#### Destination-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1destination_image_pointer)

The destination image data is generally passed via a pointer named

```
pDst
```

```
pDst1, pDst2, ...
```

#### Destination-Batch-Images Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1destination_batch_images_pointer)

The batch of destination images data is generally passed via a pointer of [NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor) type named

```
pDstBatchList
```

#### Destination-Planar-Image Pointer Array[](https://docs.nvidia.com#nppi_conventions_lb_1destination_planar_image_pointer_array)

The planar destination image data pointers are generally passed via an array of pointers named

```
pDst[]
```

#### Destination-Planar-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1destination_planar_image_pointer)

The destination planar image data is generally passed via a pointer to each plane of a multiplane output image named

```
pDst1, pDst2, ...
```

#### Destination-Image Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1destination_image_line_step)

The destination image line step parameter is

```
nDstStep
```

```
nDstStep1, nDstStep2, ...
```

#### Destination-Planar-Image Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1destination_planar_image_line_step)

The destination planar image line step is the number of bytes between successive rows for a particular plane in a multiplane output image. The destination planar image line step parameter is

```
nDstStep1, nDstStep2, ...
```

#### Passing In-Place Image Data[](https://docs.nvidia.com#nppi_conventions_lb_1in_place_image)

#### In-Place Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1in_place_image_pointer)

In the case of in-place processing, source and destination are served by the same pointer and thus pointers to in-place image data are called:

```
pSrcDst
```

#### In-Place-Image Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1in_place_image_line_step)

The in-place line step parameter is

```
nSrcDstStep
```

#### Passing Mask-Image Data[](https://docs.nvidia.com#nppi_conventions_lb_1mask_image)

Some image processing primitives have variants supporting masked_operation.

#### Mask-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1mask_image_pointer)

The mask-image data is generally passed via a pointer named

```
pMask
```

#### Mask-Image Line Step[](https://docs.nvidia.com#nppi_conventions_lb_1mask_image_line_step)

The mask-image line step parameter is

```
nMaskStep
```

#### Passing Channel-of-Interest Data[](https://docs.nvidia.com#nppi_conventions_lb_1channel_of_interest_section)

Some image processing primitives support channel_of_interest.

#### Channel_of_Interest Number[](https://docs.nvidia.com#nppi_conventions_lb_1channel_of_interest_number)

The channel-of-interest data is generally an integer (either 1, 2, or 3):

```
nCOI
```

### Image Data Alignment Requirements[](https://docs.nvidia.com#nppi_conventions_lb_1image_data_alignment)

NPP requires pixel data to adhere to certain alignment constraints.

For 2 and 4 channel images the following alignment requirement holds:

```
data_pointer % (\#channels * sizeof(channel type)) == 0
```

[Npp8u](https://docs.nvidia.com/nppdefs.html#group__npp__basic__types_1ga29b502b6816fc0066fd59538483a5b62)(8-bit unsigned) would require all pixels to fall on addresses that are multiples of 4 (4 channels * 1 byte size).

As a logical consequence of all pixels being aligned to their natural size the image line steps of 2 and 4 channel images also need to be multiples of the pixel size.

For 1 and 3 channel images only require that pixel pointers are aligned to the underlying data type, i.e. `pData % sizof(data type) == 0`

. And consequentially line steps are also held to this requirement.

### Image Data Related Error Codes[](https://docs.nvidia.com#nppi_conventions_lb_1image_data_error_codes)

All NPPI primitives operating on image data validate the image-data pointer for proper alignment and test that the point is not null. They also validate the line stride for proper alignment and guard against the step being less or equal to 0. Failed validation results in one of the following error codes being returned and the primitive not being executed: NPP_STEP_ERROR is returned if the data step is 0 or negative. NPP_NOT_EVEN_STEP_ERROR is returned if the line step is not a multiple of the pixel size for 2 and 4 channel images. NPP_NULL_POINTER_ERROR is returned if the image-data pointer is 0 (NULL). NPP_ALIGNMENT_ERROR if the image-data pointer address is not a multiple of the pixel size for 2 and 4 channel images.

## Region-Of-Interest (ROI)[](https://docs.nvidia.com#nppi_conventions_lb_1roi_specification)

In practice processing a rectangular sub-region of an image is often more common than processing complete images. The vast majority of NPP’s image-processing primitives allow for processing of such sub regions also referred to as regions-of-interest or ROIs.

All primitives supporting ROI processing are marked by a “R” in their name suffix. In most cases the ROI is passed as a single [NppiSize](https://docs.nvidia.com/nppdefs.html#structnppisize) struct, which provides the width and height of the ROI. This raises the question how the primitive knows where in the image this rectangle of (width, height) is located. The “start pixel” of the ROI is implicitly given by the image-data pointer. I.e. instead of explicitly passing a pixel coordinate for the upper-left corner (lowest memory address), the user simply offsets the image-data pointers to point to the first pixel of the ROI.

In practice this means that for an image (`pSrc`

, `nSrcStep`

) and the start-pixel of the ROI being at location (x, y), one would pass

```
pSrcOffset = pSrc + y * nSrcStep + x * PixelSize;
```

as the image-data source to the primitive. `PixelSize`

is typically computed as

```
PixelSize = NumberOfColorChannels * sizeof(PixelDataType).
```

E.g. for a pimitive like [nppiSet_16s_C4R_Ctx()](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__set_1ga0c73fce051a1cc0af9dff213ea97d39a) we would have

NumberOfColorChannels == 4;

sizeof(Npp16s) == 2;

and thus PixelSize = 4 * 2 = 8;


### ROI Related Error Codes[](https://docs.nvidia.com#nppi_conventions_lb_1roi_error_codes)

All NPPI primitives operating on ROIs of image data validate the ROI size and image’s step size. Failed validation results in one of the following error codes being returned and the primitive not being executed: NPP_SIZE_ERROR is returned if either the ROI width or ROI height are negative. NPP_STEP_ERROR is returned if the ROI width exceeds the image’s line step. In mathematical terms `(widthROI * PixelSize) > nLinStep`

indicates an error.

## Masked Operation[](https://docs.nvidia.com#nppi_conventions_lb_1masked_operation)

Some primitive support masked operation. An “M” in the suffix of those variants indicates masked operation. Primitives supporting masked operation consume an additional input image provided via a mask_image_pointer and mask_image_line_step. The mask image is interpreted by these primitives as a boolean image. The values of type Npp8u are interpreted as boolean values where a values of 0 indicates false, any non-zero values true.

Unless otherwise indicated the operation is only performed on pixels where its spatially corresponding mask pixel is true (non-zero). E.g. a masked copy operation would only copy those pixels in the ROI that have corresponding non-zero mask pixels.

## Channel-of-Interest API[](https://docs.nvidia.com#nppi_conventions_lb_1channel_of_interest)

Some primitives allow restricting operations to a single channel of interest within a multi-channel image. These primitives are suffixed with the letter “C” (after the channel information, e.g. [nppiCopy_8u_C3CR_Ctx()](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__channel__copy_1ga8a09fe4f5f6252fd089d6d1d577375e6)). The channel-of-interest is generally selected by offsetting the image-data pointer to point directly to the channel- of-interest rather than the base of the first pixel in the ROI. Some primitives also explicitly specify the selected channel number and pass it via an integer, e.g. [nppiMean_StdDev_8u_C3CR_Ctx()](https://docs.nvidia.com/image_statistics_functions.html#group__image__mean__stddev_1ga2d5ec1221a825781819179ca597c6f6e).

### Select-Channel Source-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1select_source_pointer)

This is a pointer to the channel-of-interest within the first pixel of the source image. E.g. if `pSrc`

is the pointer to the first pixel inside the ROI of a three channel image. Using the appropriate select-channel copy primitive one could copy the second channel of this source image into the first channel of a destination image given by `pDst`

by offsetting the pointer by one:

```
nppiCopy_8u_C3CR_Ctx(pSrc + 1, nSrcStep, pDst, nDstStep, oSizeROI);
```

### Select-Channel Source-Image[](https://docs.nvidia.com#nppi_conventions_lb_1select_source_channel)

Some primitives allow the user to select the channel-of-interest by specifying the channel number (`nCOI`

). This approach is typically used in the image statistical functions. For example,

```
nppiMean_StdDev_8u_C3CR_Ctx(pSrc, nSrcStep, oSizeROI, nCOI, pDeviceBuffer, pMean, pStdDev );
```

The channel-of-interest number can be either 1, 2, or 3.

### Select-Channel Destination-Image Pointer[](https://docs.nvidia.com#nppi_conventions_lb_1select_destination_pointer)

This is a pointer to the channel-of-interest within the first pixel of the destination image. E.g. if `pDst`

is the pointer to the first pixel inside the ROI of a three channel image. Using the appropriate select-channel copy primitive one could copy data into the second channel of this destination image from the first channel of a source image given by `pSrc`

by offsetting the destination pointer by one:

```
nppiCopy_8u_C3CR_Ctx(pSrc, nSrcStep, pDst + 1, nDstStep, oSizeROI);
```

## Source-Image Sampling[](https://docs.nvidia.com#nppi_conventions_lb_1source_image_sampling)

A large number of NPP image-processing functions consume at least one source image and produce an output image (e.g. [nppiAddC_8u_C1RSfs_Ctx()](https://docs.nvidia.com/image_arithmetic_and_logical_operations.html#group__image__addc_1ga0414687a64ae022a36219fad9d369167) or [nppiFilterBox_8u_C1R_Ctx()](https://docs.nvidia.com/image_filtering_functions.html#group__image__filter__box_1gae0d26e79669452e78fdd2b4fd0d7a008)). All NPP functions falling into this category also operate on ROIs (see :ref: _roi_specification) which for these functions should be considered to describe the destination ROI. In other words the ROI describes a rectangular region in the destination image and all pixels inside of this region are being written by the function in question.

In order to use such functions successfully it is important to understand how the user defined destination ROI affects which pixels in the input image(s) are being read by the algorithms. To simplify the discussion of ROI propagation (i.e. given a destination ROI, what are the ROIs in in the source(s)), it makes sense to distinguish two major cases:

Point-Wise Operations: These are primitives like

[nppiAddC_8u_C1RSfs_Ctx()](https://docs.nvidia.com/image_arithmetic_and_logical_operations.html#group__image__addc_1ga0414687a64ae022a36219fad9d369167). Each output pixel requires exactly one input pixel to be read.Neighborhood Operations: These are primitives like

[nppiFilterBox_8u_C1R_Ctx()](https://docs.nvidia.com/image_filtering_functions.html#group__image__filter__box_1gae0d26e79669452e78fdd2b4fd0d7a008), which require a group of pixels from the source image(s) to be read in order to produce a single output.

### Point-Wise Operations[](https://docs.nvidia.com#nppi_conventions_lb_1point_wise_operations)

As mentioned above, point-wise operations consume a single pixel from the input image (or a single pixel from each input image, if the operation in question has more than one input image) in order to produce a single output pixel.

### Neighborhood Operations[](https://docs.nvidia.com#nppi_conventions_lb_1neighborhood_operations)

In the case of neighborhood operations a number of input pixels (a “neighborhood” of pixels) is read in the input image (or images) in order to compute a single output pixel. All of the functions for image_filtering_functions and image_morphological_operations are neighborhood operations.

Most of these functions have parameters that affect the size and relative location of the neighborhood: a mask-size structure and an achor-point structure. Both parameters are described in more detail in the next subsections.

#### Mask-Size Parameter[](https://docs.nvidia.com#nppi_conventions_lb_1mask_size_parameter)

Many NPP neighborhood operations allow the user to specify the size of the neighborhood via a parameter usually named `oMaskSize`

of type [NppiSize](https://docs.nvidia.com/nppdefs.html#structnppisize). In those cases the neighborhood of pixels read from the source(s) is exactly the size of the mask. Assuming the mask is anchored at location (0, 0) (see anchor_point_parameter below) and has a size of (w, h), i.e.

```
assert(oMaskSize.w == w);
assert(oMaskSize.h == h);
assert(oAnchor.x == 0);
assert(oAnchor.y == 0);
```

a neighborhood operation would read the following source pixels in order to compute destination pixel \( D_{i,j} \):

#### Anchor-Point Parameter[](https://docs.nvidia.com#nppi_conventions_lb_1anchor_point_parameter)

Many NPP primitives performing neighborhood operations allow the user to specify the relative location of the neighborhood via a parameter usually named `oAnchor`

of type [NppiPoint](https://docs.nvidia.com/nppdefs.html#structnppipoint). Using the anchor a developer can chose the position of the mask (see mask_size_parameter) relative to current pixel index.

Using the same example as in mask_size_parameter, but this time with an anchor position of (a, b):

```
assert(oMaskSize.w == w);
assert(oMaskSize.h == h);
assert(oAnchor.x == a);
assert(oAnchor.y == b);
```

the following pixels from the source image would be read:

#### Sampling Beyond Image Boundaries[](https://docs.nvidia.com#nppi_conventions_lb_1sampling_beyond_image_boundaries)

NPP primitives in general and NPP neighborhood operations in particular require that all pixel locations read and written are valid and within the boundaries of the respective images. Sampling outside of the defined image data regions results in undefined behavior and may lead to system instability.

This poses a problem in practice: when processing full-size images one cannot choose the destination ROI to be the same size as the source image. Because neighborhood operations read pixels from an enlarged source ROI, the destination ROI must be shrunk so that the expanded source ROI does not exceed the source image’s size OR if the neighborhood operation function supports a Border version then this version can be used without ROI adjustment with the appropriate border protection mode selected.

For cases where this “shrinking” of the destination image size is unacceptable and a Border version of the function is not available, NPP provides a set of border-expanding Copy primitives. E.g. [nppiCopyConstBorder_8u_C1R_Ctx()](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__constant__border_1gae6fab93d49555b221542ada666e26cda), [nppiCopyReplicateBorder_8u_C1R_Ctx()](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__replicate__border_1ga411d46a19e541da6c87698b0dd02ff52) and [nppiCopyWrapBorder_8u_C1R_Ctx()](https://docs.nvidia.com/image_data_exchange_and_initialization.html#group__image__copy__wrap__border_1ga91be2c10f49a05edb686d10a3c8fa313). The user can use these primitives to “expand” the source image’s size using one of the three expansion modes. The expanded image can then be safely passed to a neighborhood operation producing a full-size result.

# Signal Processing Conventions[](https://docs.nvidia.com#signal-processing-conventions)

## Signal Data[](https://docs.nvidia.com#npps_conventions_lb_1passing_signal_data)

Signal data is passed to and from NPPS primitives via a pointer to the signal’s data type.

The general idea behind this fairly low-level way of passing signal data is ease-of-adoption into existing software projects:

Passing the data pointer rather than a higher-level signal struct allows for easy adoption by not requiring a specific signal representation (that could include total signal size offset, or other additional information). This avoids awkward packing and unpacking of signal data from the host application to an NPP specific signal representation.


### Parameter Names for Signal Data[](https://docs.nvidia.com#npps_conventions_lb_1signal_data_parameter_names)

There are three general cases of image-data passing throughout NPP detailed in the following sections.

Those are signals consumed by the algorithm.

#### Source Signal Pointer[](https://docs.nvidia.com#npps_conventions_lb_1source_signal_pointer)

The source signal data is generally passed via a pointer named

```
pSrc
```

```
nppsPrimitive_32s(const Npp32s * pSrc, ...)
```

```
pSrc1, pScr2, ...
```

#### Destination Signal Pointer[](https://docs.nvidia.com#npps_conventions_lb_1destination_signal_pointer)

The destination signal data is generally passed via a pointer named

```
pDst
```

```
pDst1, pDst2, ...
```

#### In-Place Signal Pointer[](https://docs.nvidia.com#npps_conventions_lb_1in_place_signal_pointer)

In the case of in-place processing, source and destination are served by the same pointer and thus pointers to in-place signal data are called:

```
pSrcDst
```

### Signal Data Alignment Requirements[](https://docs.nvidia.com#npps_conventions_lb_1signal_data_alignment)

NPP requires signal sample data to be naturally aligned, i.e. any pointer

```
NppType * p;
```

```
assert(p % sizeof(p) == 0);
```

### Signal Data Related Error Codes[](https://docs.nvidia.com#npps_conventions_lb_1signal_data_error_codes)

All NPPI primitives operating on signal data validate the signal-data pointer for proper alignment and test that the point is not null.

Failed validation results in one of the following error codes being returned and the primitive not being executed: NPP_NULL_POINTER_ERROR is returned if the image-data pointer is 0 (NULL). NPP_ALIGNMENT_ERROR if the signal-data pointer address is not a multiple of the signal’s data-type size.

## Signal Length[](https://docs.nvidia.com#npps_conventions_lb_1length_specification)

The vast majority of NPPS functions take a

```
nLength
```

### Length Related Error Codes[](https://docs.nvidia.com#npps_conventions_lb_1length_error_codes)

All NPPS primitives taking a length parameter validate this input.

Failed validation results in the following error code being returned and the primitive not being executed: NPP_SIZE_ERROR is returned if the length is negative.