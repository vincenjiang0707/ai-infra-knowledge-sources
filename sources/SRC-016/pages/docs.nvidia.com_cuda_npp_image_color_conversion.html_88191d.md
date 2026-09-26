source: https://docs.nvidia.com/cuda/npp/image_color_conversion.html

# Image Color Conversion Functions[](https://docs.nvidia.com#image-color-conversion-functions)

Routines manipulating an image’s color model and sampling format.

These functions can be found in the nppicc library. Linking to only the sub-libraries that you use can significantly save link time, application load time, and CUDA runtime startup time when using dynamic libraries.

## Color Processing Functions[](https://docs.nvidia.com#color-processing-functions)

Routines for performing image color manipulation.

RGBToYUVColorTwist

Normally, color twist is a 3-channel operation that takes place on RGB data.

The following functions also perform the color twist operation, but while converting between image formats: RGBToYUV420, RGBToYUV422, and RGBToNV12.

To recap color twist pixel processing: Color twist consists of applying the following formula to each image pixel using coefficients from the user supplied color twist host matrix array as follows where dst[x] and src[x] represent destination pixel and source pixel channel or plane x. The full sized coefficient matrix should be sent for all pixel channel sizes, the function will process the appropriate coefficients and channels for the corresponding pixel size.

This is how the matrix works for a RGB->YUV420/YUV422/NV12 forward transform:

```
dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3]
dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3]
dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3]
```

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV420_8u_ColorTwist32f_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV420_8u_ColorTwist32f_P3R_Ctx)

-
Three channel 8-bit unsigned planar RGB convertion to three channel 8-bit unsigned planar YUV 4:2:0, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV420_16u_ColorTwist32f_P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV420_16u_ColorTwist32f_P3R_Ctx)

-
Three channel 16-bit unsigned planar RGB convertion to three channel 16-bit unsigned planar YUV 4:2:0, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV420_8u_ColorTwist32f_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV420_8u_ColorTwist32f_C3P3R_Ctx)

-
Three channel 8-bit unsigned packed RGB convertion to three channel 8-bit unsigned planar YUV 4:2:0, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV420_16u_ColorTwist32f_C3P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV420_16u_ColorTwist32f_C3P3R_Ctx)

-
Three channel 16-bit unsigned packed RGB convertion to three channel 16-bit unsigned planar YUV 4:2:0, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_8u_ColorTwist32f_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_8u_ColorTwist32f_P3R_Ctx)

-
Three channel 8-bit unsigned planar RGB convertion to three channel 8-bit unsigned planar YUV 4:2:2, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_16u_ColorTwist32f_P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_16u_ColorTwist32f_P3R_Ctx)

-
Three channel 16-bit unsigned planar RGB convertion to three channel 16-bit unsigned planar YUV 4:2:2, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_8u_ColorTwist32f_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_8u_ColorTwist32f_C3C2R_Ctx)

-
Three channel 8-bit unsigned packed RGB convertion to two channel 8-bit unsigned packed YUV 4:2:2, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_16u_ColorTwist32f_C3C2R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_16u_ColorTwist32f_C3C2R_Ctx)

-
Three channel 16-bit unsigned packed RGB convertion to two channel 16-bit unsigned packed YUV 4:2:2, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_8u_ColorTwist32f_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_8u_ColorTwist32f_C3P3R_Ctx)

-
Three channel 8-bit unsigned packed RGB convertion to three channel 8-bit unsigned planar YUV 4:2:2, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_16u_ColorTwist32f_C3P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_16u_ColorTwist32f_C3P3R_Ctx)

-
Three channel 16-bit unsigned packed RGB convertion to three channel 16-bit unsigned planar YUV 4:2:2, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToNV12_8u_ColorTwist32f_C3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[2], int aDstStep[2],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToNV12_8u_ColorTwist32f_C3P2R_Ctx)

-
Three channel 8-bit unsigned packed RGB convertion to two channel 8-bit unsigned planar NV12, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToNV12_16u_ColorTwist32f_C3P2R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[2], int aDstStep[2],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToNV12_16u_ColorTwist32f_C3P2R_Ctx)

-
Three channel 16-bit unsigned packed RGB convertion to two channel 16-bit unsigned planar NV12, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToNV12_8u_ColorTwist32f_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[2], int aDstStep[2],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToNV12_8u_ColorTwist32f_P3P2R_Ctx)

-
Three channel 8-bit unsigned planar RGB convertion to two channel 8-bit unsigned planar NV12, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToNV12_16u_ColorTwist32f_P3P2R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[2], int aDstStep[2],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToNV12_16u_ColorTwist32f_P3P2R_Ctx)

-
Three channel 16-bit unsigned planar RGB convertion to two channel 16-bit unsigned planar NV12, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


YUVToRGBColorTwist

This is the inverse color twist, a 3-channel operation that takes place on YUV/NV12 data to produce RGB data, supporting the following conversions: YUV420ToRGB, YUV422ToRGB, and NV12ToRGB.

The INVERSE Color twist consists of applying the following formula to each image pixel using coefficients from the user supplied color twist host matrix array as follows where dst[x] and src[x] represent destination pixel and source pixel channel or plane x. The full sized coefficient matrix should be sent for all pixel channel sizes, the function will process the appropriate coefficients and channels for the corresponding pixel size.

This is how the matrix works for the YUV420/YUV/422/NV12->RGB INVERSE transform:

(note- do the offsets first):

```
src[0]' = src[0] + aTwist[0][3]
src[1]' = src[1] + aTwist[1][3]
src[2]' = src[2] + aTwist[2][3]
```

And then the remaining 3x3 twist matrix is applied using those modified values:

```
dst[0] = aTwist[0][0] * src[0]' + aTwist[0][1] * src[1]' + aTwist[0][2] * src[2]'
dst[1] = aTwist[1][0] * src[0]' + aTwist[1][1] * src[1]' + aTwist[1][2] * src[2]'
dst[2] = aTwist[2][0] * src[0]' + aTwist[2][1] * src[1]' + aTwist[2][2] * src[2]'
```

Since the 4th column of the matrix is the offsets (either 0 or half-max to shift the values to be positive), as they’re applied last in the forward transform (to YUV), they need to be applied FIRST in the inverse transform (back to RGB). This does mean that +-16384 has to be used for 16u images where there was a +-128 for 8u images in both forward and inverse cases.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_ColorTwist32f_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_ColorTwist32f_P3R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:0 convertion to three channel 8-bit unsigned planar RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_16u_ColorTwist32f_P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_16u_ColorTwist32f_P3R_Ctx)

-
Three channel 16-bit unsigned planar YUV4:2:0 convertion to three channel 16-bit unsigned planar RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_ColorTwist32f_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_ColorTwist32f_P3C3R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:0 convertion to three channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_16u_ColorTwist32f_P3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_16u_ColorTwist32f_P3C3R_Ctx)

-
Three channel 16-bit unsigned planar YUV4:2:0 convertion to three channel 16-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_ColorTwist32f_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_ColorTwist32f_P3C4R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:0 convertion to four channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic, with constant alpha (0xFF).

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_16u_ColorTwist32f_P3C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_16u_ColorTwist32f_P3C4R_Ctx)

-
Three channel 16-bit unsigned planar YUV4:2:0 convertion to four channel 16-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic, with constant alpha (0xFFFF).

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_ColorTwist32f_P3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_ColorTwist32f_P3AC4R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:0 convertion to four channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic, with user set alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nAlpha**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_16u_ColorTwist32f_P3AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_16u_ColorTwist32f_P3AC4R_Ctx)

-
Three channel 16-bit unsigned planar YUV4:2:0 convertion to four channel 16-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic, with user set alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nAlpha**– 16-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_ColorTwist32f_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_ColorTwist32f_C2C3R_Ctx)

-
Two channel 8-bit unsigned packed YUV4:2:2 convertion to three channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_16u_ColorTwist32f_C2C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_16u_ColorTwist32f_C2C3R_Ctx)

-
Two channel 16-bit unsigned packed YUV4:2:2 convertion to three channel 16-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_ColorTwist32f_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_ColorTwist32f_P3R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:2 convertion to three channel 8-bit unsigned planar RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_16u_ColorTwist32f_P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_16u_ColorTwist32f_P3R_Ctx)

-
Three channel 16-bit unsigned planar YUV4:2:2 convertion to three channel 16-bit unsigned planar RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_ColorTwist32f_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_ColorTwist32f_P3C3R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:2 convertion to three channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_16u_ColorTwist32f_P3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_16u_ColorTwist32f_P3C3R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:2 convertion to three channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_ColorTwist32f_P3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_ColorTwist32f_P3AC4R_Ctx)

-
Three channel 8-bit unsigned planar YUV4:2:2 convertion to three channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic, with user set alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nAlpha**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_16u_ColorTwist32f_P3AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int aSrcStep[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_16u_ColorTwist32f_P3AC4R_Ctx)

-
Three channel 16-bit unsigned planar YUV4:2:2 convertion to three channel 16-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic, with user set alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nAlpha**– 16-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_8u_ColorTwist32f_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int aSrcStep[2],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_8u_ColorTwist32f_P2C3R_Ctx)

-
Two channel 8-bit unsigned planar NV12 convertion to three channel 8-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_16u_ColorTwist32f_P2C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[2], int aSrcStep[2],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_16u_ColorTwist32f_P2C3R_Ctx)

-
Two channel 16-bit unsigned planar NV12 convertion to three channel 16-bit unsigned packed RGB, using a Color Twist to compute the exact color space arithmetic.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


RGBToUYVP Conversion

Three unsigned 8-bit packed RGB channels color space conversion to three channel unsigned packed 10-bit UYVP pixel.

- param pSrc
- param aSrcStep
- param oSrcOffset
-
pSrc pixel offset relative to image origin, currently must be 0,0.

- param pDst
- param aDstStep
- param oSizeROI
- param eColorSpace
-
The input color space.

- param nppStreamCtx

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_8u_ToUYVP_10u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_8u_ToUYVP_10u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_8u_ToUYVP_10u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_8u_ToUYVP_10u_P3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_8u_ToUYVP_10u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc, const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_8u_ToUYVP_10u_C3P3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBA_8u_ToUYVP_10u_AC4C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc, const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBA_8u_ToUYVP_10u_AC4C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_16u_ToUYVP_10u_C3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_16u_ToUYVP_10u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_16u_ToUYVP_10u_P3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_16u_ToUYVP_10u_P3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBA_16u_ToUYVP_10u_AC4C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc, const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBA_16u_ToUYVP_10u_AC4C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_16f_ToUYVP_10u_C3C3R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_16f_ToUYVP_10u_C3C3R_Ctx)


UYVPToRGB Conversion

Three channel unsigned packed 10-bit UYVP pixel color space conversion to three unsigned packed 8-bit channels RGB.

- param pSrc
- param aSrcStep
- param oSrcOffset
-
pSrc pixel offset relative to image origin, currently must be 0,0.

- param pDst
- param aDstStep
- param oSizeROI
- param eColorSpace
-
The output color space.

- param nppStreamCtx

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_8u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int srcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int dstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_8u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_8u_C3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)alpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_8u_C3AC4R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], const int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_8u_C3P3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_16u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int srcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int dstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_16u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_16u_C3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)alpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_16u_C3AC4R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_16u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst[3], const int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_16u_C3P3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToRGB_16f_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToRGB_16f_C3C3R_Ctx)


UYVPTranscoding

UYVP 10-bit packed YCbCr 4:2:2 transcoding to/from NV12, P010, P208, NV16, V210, P210, I444, YUV444, Y410.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12_8u_ToUYVP_10u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], const int nSrcStep[2],[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12_8u_ToUYVP_10u_P2C3R_Ctx)

-
4:2:0 conversions


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiP010_16u_ToUYVP_10u_P3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiP010_16u_ToUYVP_10u_P3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToP208_8u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int srcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int dstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToP208_8u_C3C3R_Ctx)

-
4:2:2 conversions


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToNV16_8u_C3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc, const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[2], const int nDstStep[2],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToNV16_8u_C3P2R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToV210_10u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToV210_10u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiP208_8u_ToUYVP_10u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiP208_8u_ToUYVP_10u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV16_8u_ToUYVP_10u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], const int nSrcStep[2],[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV16_8u_ToUYVP_10u_P2C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiV210_10u_ToUYVP_10u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiV210_10u_ToUYVP_10u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiP210_16u_ToUYVP_10u_P2C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[2], const int nSrcStep[2],[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiP210_16u_ToUYVP_10u_P2C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToI444_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pDst[3], const int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToI444_8u_C3P3R_Ctx)

-
4:4:4 conversions


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToYUV444_8u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToYUV444_8u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVP_10u_ToY410_10u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVP_10u_ToY410_10u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiI444_8u_ToUYVP_10u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiI444_8u_ToUYVP_10u_P3C3R_Ctx)


RGBToUYVY Conversion

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_8u_ToUYVY_8u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_8u_ToUYVY_8u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_8u_ToUYVY_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_8u_ToUYVY_8u_P3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBA_8u_ToUYVY_8u_AC4C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc, const int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBA_8u_ToUYVY_8u_AC4C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGB_16u_ToUYVY16_16u_C3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGB_16u_ToUYVY16_16u_C3C3R_Ctx)


UYVYToRGB Conversion

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVY_8u_ToRGB_8u_C3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVY_8u_ToRGB_8u_C3C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVY_8u_ToRGB_8u_C3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVY_8u_ToRGB_8u_C3AC4R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVY_8u_ToRGB_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], const int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVY_8u_ToRGB_8u_C3P3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiUYVY16_16u_ToRGB_16u_C3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiUYVY16_16u_ToRGB_16u_C3C3R_Ctx)


NV12ToRGBAExt NV12 to RGB/BGR Extended Conversions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_8u_P2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_8u_P2C4R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToBGR_8u_P2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToBGR_8u_P2C4R_Ctx)


P010ToRGB P010 to RGB/RGBA Conversions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiP010ToRGB_8u_P2C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[2], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiP010ToRGB_8u_P2C3R_Ctx)


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiP010ToRGB_8u_P2C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[2], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, NppiColorSpace eColorSpace,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiP010ToRGB_8u_P2C4R_Ctx)


P016ToRGB P016 to RGB/RGBA Conversions

RGBToNV12 RGB to NV12 Conversions

YUV420ToNV12 YUV420 to NV12 Format Repack

### Color To Gray Conversion[](https://docs.nvidia.com#color-to-gray-conversion)

Routines for converting color images to grayscale.

RGBToGray

RGB to CCIR601 Gray conversion.

Here is how NPP converts gamma corrected RGB to CCIR601 Gray.

```
nGray = 0.299F * R + 0.587F * G + 0.114F * B;
```

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_8u_C3C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_8u_C3C1R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 1 channel 8-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_8u_AC4C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_8u_AC4C1R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 1 channel 8-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_16u_C3C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_16u_C3C1R_Ctx)

-
3 channel 16-bit unsigned packed RGB to 1 channel 16-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_16u_AC4C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_16u_AC4C1R_Ctx)

-
4 channel 16-bit unsigned packed RGB with alpha to 1 channel 16-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_16s_C3C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_16s_C3C1R_Ctx)

-
3 channel 16-bit signed packed RGB to 1 channel 16-bit signed packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_16s_AC4C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_16s_AC4C1R_Ctx)

-
4 channel 16-bit signed packed RGB with alpha to 1 channel 16-bit signed packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_32f_C3C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_32f_C3C1R_Ctx)

-
3 channel 32-bit floating point packed RGB to 1 channel 32-bit floating point packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToGray_32f_AC4C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToGray_32f_AC4C1R_Ctx)

-
4 channel 32-bit floating point packed RGB with alpha to 1 channel 32-bit floating point packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


ColorToGray

RGB Color to Gray conversion using user supplied conversion coefficients.

Here is how NPP converts gamma corrected RGB Color to Gray using user supplied conversion coefficients.

```
nGray = aCoeffs[0] * R + aCoeffs[1] * G + aCoeffs[2] * B;
```

For the C4C1R versions of the functions the calculations are as follows.

For BGRA or other formats with alpha just rearrange the coefficients accordingly.

```
nGray = aCoeffs[0] * R + aCoeffs[1] * G + aCoeffs[2] * B + aCoeffs[3] * A;
```

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_8u_C3C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_8u_C3C1R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 1 channel 8-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_8u_AC4C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_8u_AC4C1R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 1 channel 8-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_8u_C4C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_8u_C4C1R_Ctx)

-
4 channel 8-bit unsigned packed RGBA to 1 channel 8-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_16u_C3C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_16u_C3C1R_Ctx)

-
3 channel 16-bit unsigned packed RGB to 1 channel 16-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_16u_AC4C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_16u_AC4C1R_Ctx)

-
4 channel 16-bit unsigned packed RGB with alpha to 1 channel 16-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_16u_C4C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_16u_C4C1R_Ctx)

-
4 channel 16-bit unsigned packed RGBA to 1 channel 16-bit unsigned packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_16s_C3C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_16s_C3C1R_Ctx)

-
3 channel 16-bit signed packed RGB to 1 channel 16-bit signed packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_16s_AC4C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_16s_AC4C1R_Ctx)

-
4 channel 16-bit signed packed RGB with alpha to 1 channel 16-bit signed packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_16s_C4C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_16s_C4C1R_Ctx)

-
4 channel 16-bit signed packed RGBA to 1 channel 16-bit signed packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_32f_C3C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_32f_C3C1R_Ctx)

-
3 channel 32-bit floating point packed RGB to 1 channel 32-bit floating point packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_32f_AC4C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_32f_AC4C1R_Ctx)

-
4 channel 32-bit floating point packed RGB with alpha to 1 channel 32-bit floating point packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorToGray_32f_C4C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aCoeffs[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorToGray_32f_C4C1R_Ctx)

-
4 channel 32-bit floating point packed RGBA to 1 channel 32-bit floating point packed Gray conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aCoeffs**– Host memory fixed size array of constant floating point conversion coefficient values, one per color channel.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


GradientColorToGray

RGB Color to Gray Gradient conversion using user selected gradient distance method.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGradientColorToGray_8u_C3C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiNorm](https://docs.nvidia.com/nppdefs.html#c.NppiNorm)eNorm,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGradientColorToGray_8u_C3C1R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 1 channel 8-bit unsigned packed Gray Gradient conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**eNorm**– Gradient distance method to use.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGradientColorToGray_16u_C3C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiNorm](https://docs.nvidia.com/nppdefs.html#c.NppiNorm)eNorm,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGradientColorToGray_16u_C3C1R_Ctx)

-
3 channel 16-bit unsigned packed RGB to 1 channel 16-bit unsigned packed Gray Gradient conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**eNorm**– Gradient distance method to use.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGradientColorToGray_16s_C3C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiNorm](https://docs.nvidia.com/nppdefs.html#c.NppiNorm)eNorm,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGradientColorToGray_16s_C3C1R_Ctx)

-
3 channel 16-bit signed packed RGB to 1 channel 16-bit signed packed Gray Gradient conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**eNorm**– Gradient distance method to use.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGradientColorToGray_32f_C3C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiNorm](https://docs.nvidia.com/nppdefs.html#c.NppiNorm)eNorm,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGradientColorToGray_32f_C3C1R_Ctx)

-
3 channel 32-bit floating point packed RGB to 1 channel 32-bit floating point packed Gray Gradient conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**eNorm**– Gradient distance method to use.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### Color Debayer[](https://docs.nvidia.com#color-debayer)

Grayscale Color Filter Array to RGB Color Debayer conversion.

Generates one RGB color pixel for every grayscale source pixel. Source and destination images must have even width and height. Missing pixel colors are generated using bilinear interpolation with chroma correlation of generated green values (eInterpolation MUST be set to 0). eGrid allows the user to specify the Bayer grid registration position at source image location oSrcROI.x, oSrcROI.y relative to pSrc. Possible registration positions are:

```
NPPI_BAYER_BGGR NPPI_BAYER_RGGB NPPI_BAYER_GBRG NPPI_BAYER_GRBG
B G R G G B G R
G R G B R G B G
```

If it becomes necessary to access source pixels outside source image then the source image borders are mirrored.

Here is how the algorithm works. R, G, and B base pixels from the source image are used unmodified. To generate R values for those G pixels, the average of R(x - 1, y) and R(x + 1, y) or R(x, y - 1) and R(x, y + 1) is used depending on whether the left and right or top and bottom pixels are R base pixels. To generate B values for those G pixels, the same algorithm is used using nearest B values. For an R base pixel, if there are no B values in the upper, lower, left, or right adjacent pixels then B is the average of B values in the 4 diagonal (G base) pixels. The same algorithm is used using R values to generate the R value of a B base pixel. Chroma correlation is applied to generated G values only, for a B base pixel G(x - 1, y) and G(x + 1, y) are averaged or G(x, y - 1) and G(x, y + 1) are averaged depending on whether the absolute difference between B(x, y) and the average of B(x - 2, y) and B(x + 2, y) is smaller than the absolute difference between B(x, y) and the average of B(x, y - 2) and B(x, y + 2). For an R base pixel the same algorithm is used testing against the surrounding R values at those offsets. If the horizontal and vertical differences are the same at one of those pixels then the average of the four left, right, upper and lower G values is used instead.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCFAToRGB_8u_C1C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiRect](https://docs.nvidia.com/nppdefs.html#c.NppiRect)oSrcROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiBayerGridPosition](https://docs.nvidia.com/nppdefs.html#c.NppiBayerGridPosition)eGrid,[NppiInterpolationMode](https://docs.nvidia.com/nppdefs.html#c.NppiInterpolationMode)eInterpolation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCFAToRGB_8u_C1C3R_Ctx)

-
1 channel 8-bit unsigned packed CFA grayscale Bayer pattern to 3 channel 8-bit unsigned packed RGB conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**oSrcSize**– full source image width and height relative to pSrc.**oSrcROI**– rectangle specifying starting source image pixel x and y location relative to pSrc and ROI width and height.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**eGrid**– enumeration value specifying bayer grid registration position at location oSrcROI.x, oSrcROI.y relative to pSrc.**eInterpolation**– MUST be NPPI_INTER_UNDEFINED**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCFAToRGBA_8u_C1AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiRect](https://docs.nvidia.com/nppdefs.html#c.NppiRect)oSrcROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiBayerGridPosition](https://docs.nvidia.com/nppdefs.html#c.NppiBayerGridPosition)eGrid,[NppiInterpolationMode](https://docs.nvidia.com/nppdefs.html#c.NppiInterpolationMode)eInterpolation,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCFAToRGBA_8u_C1AC4R_Ctx)

-
1 channel 8-bit unsigned packed CFA grayscale Bayer pattern to 4 channel 8-bit unsigned packed RGB conversion with alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**oSrcSize**– full source image width and height relative to pSrc.**oSrcROI**– rectangle specifying starting source image pixel x and y location relative to pSrc and ROI width and height.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**eGrid**– enumeration value specifying bayer grid registration position at location oSrcROI.x, oSrcROI.y relative to pSrc.**eInterpolation**– MUST be NPPI_INTER_UNDEFINED**nAlpha**– constant alpha value to be written to each destination pixel**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCFAToRGB_16u_C1C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiRect](https://docs.nvidia.com/nppdefs.html#c.NppiRect)oSrcROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiBayerGridPosition](https://docs.nvidia.com/nppdefs.html#c.NppiBayerGridPosition)eGrid,[NppiInterpolationMode](https://docs.nvidia.com/nppdefs.html#c.NppiInterpolationMode)eInterpolation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCFAToRGB_16u_C1C3R_Ctx)

-
1 channel 16-bit unsigned packed CFA grayscale Bayer pattern to 3 channel 16-bit unsigned packed RGB conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**oSrcSize**– full source image width and height relative to pSrc.**oSrcROI**– rectangle specifying starting source image pixel x and y location relative to pSrc and ROI width and height.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**eGrid**– enumeration value specifying bayer grid registration position at location oSrcROI.x, oSrcROI.y relative to pSrc.**eInterpolation**– MUST be NPPI_INTER_UNDEFINED**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCFAToRGBA_16u_C1AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiRect](https://docs.nvidia.com/nppdefs.html#c.NppiRect)oSrcROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiBayerGridPosition](https://docs.nvidia.com/nppdefs.html#c.NppiBayerGridPosition)eGrid,[NppiInterpolationMode](https://docs.nvidia.com/nppdefs.html#c.NppiInterpolationMode)eInterpolation,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCFAToRGBA_16u_C1AC4R_Ctx)

-
1 channel 16-bit unsigned packed CFA grayscale Bayer pattern to 4 channel 16-bit unsigned packed RGB conversion with alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**oSrcSize**– full source image width and height relative to pSrc.**oSrcROI**– rectangle specifying starting source image pixel x and y location relative to pSrc and ROI width and height.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**eGrid**– enumeration value specifying bayer grid registration position at location oSrcROI.x, oSrcROI.y relative to pSrc.**eInterpolation**– MUST be NPPI_INTER_UNDEFINED**nAlpha**– constant alpha value to be written to each destination pixel**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCFAToRGB_32u_C1C3R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiRect](https://docs.nvidia.com/nppdefs.html#c.NppiRect)oSrcROI,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiBayerGridPosition](https://docs.nvidia.com/nppdefs.html#c.NppiBayerGridPosition)eGrid,[NppiInterpolationMode](https://docs.nvidia.com/nppdefs.html#c.NppiInterpolationMode)eInterpolation,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCFAToRGB_32u_C1C3R_Ctx)

-
1 channel 32-bit unsigned packed CFA grayscale Bayer pattern to 3 channel 32-bit unsigned packed RGB conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**oSrcSize**– full source image width and height relative to pSrc.**oSrcROI**– rectangle specifying starting source image pixel x and y location relative to pSrc and ROI width and height.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**eGrid**– enumeration value specifying bayer grid registration position at location oSrcROI.x, oSrcROI.y relative to pSrc.**eInterpolation**– MUST be NPPI_INTER_UNDEFINED**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCFAToRGBA_32u_C1AC4R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiRect](https://docs.nvidia.com/nppdefs.html#c.NppiRect)oSrcROI,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiBayerGridPosition](https://docs.nvidia.com/nppdefs.html#c.NppiBayerGridPosition)eGrid,[NppiInterpolationMode](https://docs.nvidia.com/nppdefs.html#c.NppiInterpolationMode)eInterpolation,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nAlpha,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCFAToRGBA_32u_C1AC4R_Ctx)

-
1 channel 32-bit unsigned packed CFA grayscale Bayer pattern to 4 channel 32-bit unsigned packed RGB conversion with alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**oSrcSize**– full source image width and height relative to pSrc.**oSrcROI**– rectangle specifying starting source image pixel x and y location relative to pSrc and ROI width and height.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**eGrid**– enumeration value specifying bayer grid registration position at location oSrcROI.x, oSrcROI.y relative to pSrc.**eInterpolation**– MUST be NPPI_INTER_UNDEFINED**nAlpha**– constant alpha value to be written to each destination pixel**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### Color Gamma Correction[](https://docs.nvidia.com#color-gamma-correction)

Routines for correcting image color gamma.

GammaFwd

Forward gamma correction.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaFwd_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaFwd_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed color not in place forward gamma correction.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaFwd_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaFwd_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned packed color in place forward gamma correction.

- Parameters
-
**pSrcDst**– in place packed pixel image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaFwd_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaFwd_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed color with alpha not in place forward gamma correction.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaFwd_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaFwd_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned packed color with alpha in place forward gamma correction.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaFwd_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaFwd_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar color not in place forward gamma correction.

- Parameters
-
**pSrc**– source planar pixel format image pointer array.**nSrcStep**– source planar pixel format image line step.**pDst**– destination planar pixel format image pointer array.**nDstStep**– destination planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaFwd_8u_IP3R_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaFwd_8u_IP3R_Ctx)

-
3 channel 8-bit unsigned planar color in place forward gamma correction.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


GammaInv

Inverse gamma correction.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaInv_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaInv_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed color not in place inverse gamma correction.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaInv_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaInv_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned packed color in place inverse gamma correction.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaInv_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaInv_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed color with alpha not in place inverse gamma correction.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaInv_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaInv_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned packed color with alpha in place inverse gamma correction.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaInv_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaInv_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar color not in place inverse gamma correction.

- Parameters
-
**pSrc**– source planar pixel format image pointer array.**nSrcStep**– source planar pixel format image line step.**pDst**– destination planar pixel format image pointer array.**nDstStep**– destination planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGammaInv_8u_IP3R_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGammaInv_8u_IP3R_Ctx)

-
3 channel 8-bit unsigned planar color in place inverse gamma correction.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### Complement Color Key[](https://docs.nvidia.com#complement-color-key)

Routines for performing complement color key replacement.

CompColorKey

Complement color key replacement.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompColorKey_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nColorKeyConst,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompColorKey_8u_C1R_Ctx)

-
1 channel 8-bit unsigned packed color complement color key replacement of source image 1 by source image 2.

- Parameters
-
**pSrc1**– source1 packed pixel format image pointer.**nSrc1Step**– source1 packed pixel format image line step.**pSrc2**– source2 packed pixel format image pointer.**nSrc2Step**– source2 packed pixel format image line step.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nColorKeyConst**– color key constant**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompColorKey_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nColorKeyConst[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompColorKey_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed color complement color key replacement of source image 1 by source image 2.

- Parameters
-
**pSrc1**– source1 packed pixel format image pointer.**nSrc1Step**– source1 packed pixel format image line step.**pSrc2**– source2 packed pixel format image pointer.**nSrc2Step**– source2 packed pixel format image line step.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nColorKeyConst**– color key constant array**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCompColorKey_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nColorKeyConst[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCompColorKey_8u_C4R_Ctx)

-
4 channel 8-bit unsigned packed color complement color key replacement of source image 1 by source image 2.

- Parameters
-
**pSrc1**– source1 packed pixel format image pointer.**nSrc1Step**– source1 packed pixel format image line step.**pSrc2**– source2 packed pixel format image pointer.**nSrc2Step**– source2 packed pixel format image line step.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nColorKeyConst**– color key constant array**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiAlphaCompColorKey_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc1, int nSrc1Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha1, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc2, int nSrc2Step,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAlpha2,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nColorKeyConst[4],[NppiAlphaOp](https://docs.nvidia.com/nppdefs.html#c.NppiAlphaOp)nppAlphaOp,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiAlphaCompColorKey_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed color complement color key replacement of source image 1 by source image 2 with alpha blending.

- Parameters
-
**pSrc1**– source1 packed pixel format image pointer.**nSrc1Step**– source1 packed pixel format image line step.**nAlpha1**– source1 image alpha opacity (0 - max channel pixel value).**pSrc2**– source2 packed pixel format image pointer.**nSrc2Step**– source2 packed pixel format image line step.**nAlpha2**– source2 image alpha opacity (0 - max channel pixel value).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nColorKeyConst**– color key constant array**nppAlphaOp**– NppiAlphaOp alpha compositing operation selector (excluding premul ops).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### ColorTwist[](https://docs.nvidia.com#colortwist)

Routines for converting between various image color models using user supplied matrix coefficients.

ColorTwist

Perform color twist pixel processing.

Color twist consists of applying the following formula to each image pixel using coefficients from the user supplied color twist host matrix array as follows where dst[x] and src[x] represent destination pixel and source pixel channel or plane x. The full sized coefficient matrix should be sent for all pixel channel sizes, the function will process the appropriate coefficients and channels for the corresponding pixel size.

```
dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3]
dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3]
dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3]
```

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C1R_Ctx)

-
1 channel 8-bit unsigned color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C2R_Ctx)

-
2 channel 8-bit unsigned color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C2IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C2IR_Ctx)

-
2 channel 8-bit unsigned in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C3R_Ctx)

-
3 channel 8-bit unsigned color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C4R_Ctx)

-
4 channel 8-bit unsigned color twist, with alpha copy.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is copied unmodified from the source pixel to the destination pixel.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_C4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is unmodified.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32fC_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[4][4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aConstants[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32fC_8u_C4R_Ctx)

-
4 channel 8-bit unsigned color twist with 4x4 matrix and constant vector addition.

An input 4x4 color twist matrix with floating-point coefficient values with an additional constant vector addition is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aConstants[0] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aConstants[1] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aConstants[2] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aConstants[3]

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**aConstants**– fixed size array of constant values, one per channel..**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32fC_8u_C4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[4][4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aConstants[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32fC_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned in place color twist with 4x4 matrix and an additional constant vector addition.

An input 4x4 color twist matrix with floating-point coefficient values with an additional constant vector addition is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aConstants[0] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aConstants[1] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aConstants[2] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aConstants[3]

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**aConstants**– fixed size array of constant values, one per channel..**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8u_IP3R_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8u_IP3R_Ctx)

-
3 channel 8-bit unsigned planar in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array, one pointer per plane.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C1R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C1R_Ctx)

-
1 channel 8-bit signed color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C1IR_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C1IR_Ctx)

-
1 channel 8-bit signed in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C2R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C2R_Ctx)

-
2 channel 8-bit signed color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C2IR_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C2IR_Ctx)

-
2 channel 8-bit signed in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C3R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C3R_Ctx)

-
3 channel 8-bit signed color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C3IR_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C3IR_Ctx)

-
3 channel 8-bit signed in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C4R_Ctx)

-
4 channel 8-bit signed color twist, with alpha copy.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is copied unmodified from the source pixel to the destination pixel.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_C4IR_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_C4IR_Ctx)

-
4 channel 8-bit signed in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is unmodified.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_AC4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_AC4R_Ctx)

-
4 channel 8-bit signed color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_AC4IR_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_AC4IR_Ctx)

-
4 channel 8-bit signed in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_P3R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*const pSrc[3], int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*const pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_P3R_Ctx)

-
3 channel 8-bit signed planar color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_8s_IP3R_Ctx([Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_8s_IP3R_Ctx)

-
3 channel 8-bit signed planar in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array, one pointer per plane.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_C1R_Ctx)

-
1 channel 16-bit unsigned color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_C1IR_Ctx)

-
1 channel 16-bit unsigned in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_C2R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_C2R_Ctx)

-
2 channel 16-bit unsigned color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_C2IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_C2IR_Ctx)

-
2 channel 16-bit unsigned in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_C3R_Ctx)

-
3 channel 16-bit unsigned color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrc[3], int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_P3R_Ctx)

-
3 channel 16-bit unsigned planar color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16u_IP3R_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16u_IP3R_Ctx)

-
3 channel 16-bit unsigned planar in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array, one pointer per plane.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_C1R_Ctx)

-
1 channel 16-bit signed color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_C1IR_Ctx)

-
1 channel 16-bit signed in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_C2R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_C2R_Ctx)

-
2 channel 16-bit signed color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_C2IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_C2IR_Ctx)

-
2 channel 16-bit signed in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_C3R_Ctx)

-
3 channel 16-bit signed color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_C3IR_Ctx)

-
3 channel 16-bit signed in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_AC4R_Ctx)

-
4 channel 16-bit signed color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_AC4IR_Ctx)

-
4 channel 16-bit signed in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_P3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const pSrc[3], int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_P3R_Ctx)

-
3 channel 16-bit signed planar color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16s_IP3R_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16s_IP3R_Ctx)

-
3 channel 16-bit signed planar in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array, one pointer per plane.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C1R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C1R_Ctx)

-
1 channel 16-bit floating point color twist.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C1IR_Ctx([Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C1IR_Ctx)

-
1 channel 16-bit floating point in place color twist.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C2R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C2R_Ctx)

-
2 channel 16-bit floating point color twist.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C2IR_Ctx([Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C2IR_Ctx)

-
2 channel 16-bit floating point in place color twist.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C3R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C3R_Ctx)

-
3 channel 16-bit floating point color twist.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C3IR_Ctx([Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C3IR_Ctx)

-
3 channel 16-bit floating point in place color twist.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C4R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C4R_Ctx)

-
4 channel 16-bit floating point color twist, with alpha copy.

An input color twist matrix with 32-bit floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is copied unmodified from the source pixel to the destination pixel.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32f_16f_C4IR_Ctx([Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32f_16f_C4IR_Ctx)

-
4 channel 16-bit floating point in place color twist, not affecting Alpha.

An input color twist matrix with 32-bit floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not modified.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32fC_16f_C4R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[4][4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aConstants[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32fC_16f_C4R_Ctx)

-
4 channel 16-bit floating point color twist with 4x4 matrix and constant vector addition.

An input 4x4 color twist matrix with 32-bit floating-point coefficient values with an additional 32-bit floating point constant vector addition is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aConstants[0] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aConstants[1] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aConstants[2] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aConstants[3]

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**aConstants**– fixed size array of constant values, one per channel..**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist32fC_16f_C4IR_Ctx([Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[4][4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aConstants[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist32fC_16f_C4IR_Ctx)

-
4 channel 16-bit floating point in place color twist with 4x4 matrix and an additional constant vector addition.

An input 4x4 color twist matrix with 32-bit floating-point coefficient values with an additional 32-bit floating point constant vector addition is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aConstants[0] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aConstants[1] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aConstants[2] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aConstants[3]

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**aConstants**– fixed size array of constant values, one per channel..**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C1R_Ctx)

-
1 channel 32-bit floating point color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C2R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C2R_Ctx)

-
2 channel 32-bit floating point color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C2IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C2IR_Ctx)

-
2 channel 32-bit floating point in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C3R_Ctx)

-
3 channel 32-bit floating point color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C4R_Ctx)

-
4 channel 32-bit floating point color twist, with alpha copy.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is copied unmodified from the source pixel to the destination pixel.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_C4IR_Ctx)

-
4 channel 32-bit floating point in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not modified.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_AC4R_Ctx)

-
4 channel 32-bit floating point color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place color twist, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied with in ROI. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32fC_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[4][4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aConstants[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32fC_C4R_Ctx)

-
4 channel 32-bit floating point color twist with 4x4 matrix and constant vector addition.

An input 4x4 color twist matrix with floating-point coefficient values with an additional constant vector addition is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aConstants[0] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aConstants[1] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aConstants[2] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aConstants[3]

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**aConstants**– fixed size array of constant values, one per channel..**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32fC_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[4][4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aConstants[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32fC_C4IR_Ctx)

-
4 channel 32-bit floating point in place color twist with 4x4 matrix and an additional constant vector addition.

An input 4x4 color twist matrix with floating-point coefficient values with an additional constant vector addition is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aConstants[0] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aConstants[1] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aConstants[2] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aConstants[3]

- Parameters
-
**pSrcDst**– in place packed pixel format image pointer.**nSrcDstStep**– in place packed pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**aConstants**– fixed size array of constant values, one per channel..**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_P3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const pSrc[3], int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_P3R_Ctx)

-
3 channel 32-bit floating point planar color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwist_32f_IP3R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const pSrcDst[3], int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aTwist[3][4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwist_32f_IP3R_Ctx)

-
3 channel 32-bit floating point planar in place color twist.

An input color twist matrix with floating-point coefficient values is applied within ROI.

- Parameters
-
**pSrcDst**– in place planar pixel format image pointer array, one pointer per plane.**nSrcDstStep**– in place planar pixel format image line step.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aTwist**– Host memory array containing the color twist matrix with floating-point coefficient values.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### ColorTwistBatch[](https://docs.nvidia.com#colortwistbatch)

Routines for converting between various image color models using user supplied matrix coefficients on batches of images.

ColorTwistBatch

Perform color twist pixel batch processing.

Color twist consists of applying the following formula to each image pixel using coefficients from one or more user supplied color twist device memory matrix arrays as follows where dst[x] and src[x] represent destination pixel and source pixel channel or plane x. The full sized coefficient matrix should be sent for all pixel channel sizes, the function will process the appropriate coefficients and channels for the corresponding pixel size. ColorTwistBatch generally takes the same parameter list as ColorTwist except that there is a list of N instances of those parameters (N > 1) and that list is passed in device memory; The matrix pointers referenced for each image in the batch also need to point to device memory matrix values. A convenient data structure is provided that allows for easy initialization of the parameter lists. The only restriction on these functions is that there is one single ROI which is applied respectively to each image in the batch. The primary purpose of this function is to provide improved performance for batches of smaller images as long as GPU resources are available. Therefore it is recommended that the function not be used for very large images as there may not be resources available for processing several large images simultaneously.

```
dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3]
dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3]
dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3]
```

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_C1R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer color twist batch.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_C1IR_Ctx)

-
1 channel 8-bit unsigned integer in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_C3R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer color twist batch.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned integer in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_C4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer color twist batch.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned integer in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_AC4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned integer color twist batch, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_8u_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned integer in place color twist batch, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32fC_8u_C4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32fC_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer color twist with 4x5 matrix including a constant vector (20 coefficients total).

An input 4x5 color twist matrix with floating-point coefficient values including a constant (in the fourth column) vector is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aTwist[0][4] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aTwist[1][4] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aTwist[2][4] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aTwist[3][4]

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32fC_8u_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32fC_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned integer in place color twist with 4x5 matrix including a constant vector (20 coefficients total).

An input 4x5 color twist matrix with floating-point coefficient values including a constant (in the fourth column) vector is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aTwist[0][4] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aTwist[1][4] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aTwist[2][4] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aTwist[3][4]

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_C1R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_C1R_Ctx)

-
1 channel 32-bit floating point color twist batch.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_C1IR_Ctx)

-
1 channel 32-bit floating point in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_C3R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_C3R_Ctx)

-
3 channel 32-bit floating point color twist batch.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_C4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_C4R_Ctx)

-
4 channel 32-bit floating point color twist batch.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_C4IR_Ctx)

-
4 channel 32-bit floating point in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_AC4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_AC4R_Ctx)

-
4 channel 32-bit floating point color twist batch, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point in place color twist batch, not affecting Alpha.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32fC_C4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32fC_C4R_Ctx)

-
4 channel 32-bit floating point color twist with 4x5 matrix including a constant vector (20 coefficients total).

An input 4x5 color twist matrix with floating-point coefficient values including a constant (in the fourth column) vector is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aTwist[0][4] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aTwist[1][4] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aTwist[2][4] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aTwist[3][4]

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch_32fC_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch_32fC_C4IR_Ctx)

-
4 channel in place 32-bit floating point color twist with 4x5 matrix including a constant vector (20 coefficients total).

An input 4x5 color twist matrix with floating-point coefficient values including a constant (in the fourth column) vector is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aTwist[0][4] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aTwist[1][4] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aTwist[2][4] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aTwist[3][4]

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_16f_C1R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_16f_C1R_Ctx)

-
1 channel 16-bit floating point color twist batch.

An input color twist matrix with 32-bit floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_16f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_16f_C1IR_Ctx)

-
1 channel 16-bit floating point in place color twist batch.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_16f_C3R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_16f_C3R_Ctx)

-
3 channel 16-bit floating point color twist batch.

An input color twist matrix with 32-bit floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_16f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_16f_C3IR_Ctx)

-
3 channel 16-bit floating point in place color twist batch.

An input color twist matrix with floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_16f_C4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_16f_C4R_Ctx)

-
4 channel 16-bit floating point color twist batch.

An input color twist matrix with 32-bit floating-point coefficient values is applied within the ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32f_16f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32f_16f_C4IR_Ctx)

-
4 channel 16-bit floating point in place color twist batch.

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32fC_16f_C4R_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32fC_16f_C4R_Ctx)

-
4 channel 16-bit floating point color twist with 4x5 matrix including a constant vector (20 coefficients total).

An input 4x5 color twist matrix with 32-bit floating-point coefficient values including a constant (in the fourth column) vector is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aTwist[0][4] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aTwist[1][4] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aTwist[2][4] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aTwist[3][4]

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiColorTwistBatch32fC_16f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#c.NppiColorTwistBatchCXR)*pBatchList, int nBatchSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiColorTwistBatch32fC_16f_C4IR_Ctx)

-
4 channel in place 16-bit floating point color twist with 4x5 matrix including a constant vector (20 coefficients total).

An input 4x5 color twist matrix with 32-bitfloating-point coefficient values including a constant (in the fourth column) vector is applied within ROI. For this particular version of the function the result is generated as shown below.

dst[0] = aTwist[0][0] * src[0] + aTwist[0][1] * src[1] + aTwist[0][2] * src[2] + aTwist[0][3] * src[3] + aTwist[0][4] dst[1] = aTwist[1][0] * src[0] + aTwist[1][1] * src[1] + aTwist[1][2] * src[2] + aTwist[1][3] * src[3] + aTwist[1][4] dst[2] = aTwist[2][0] * src[0] + aTwist[2][1] * src[1] + aTwist[2][2] * src[2] + aTwist[2][3] * src[3] + aTwist[2][4] dst[3] = aTwist[3][0] * src[0] + aTwist[3][1] * src[1] + aTwist[3][2] * src[2] + aTwist[3][3] * src[3] + aTwist[3][4]

An input color twist matrix with 32-bit floating-point coefficient values is applied within ROI for each image in batch. Color twist matrix can vary per image. The same ROI is applied to each image.

- Parameters
-
**nMin**– Minimum clamp value.**nMax**– Maximum saturation and clamp value.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pBatchList**– Device memory pointer to nBatchSize list of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures.**nBatchSize**– Number of[NppiColorTwistBatchCXR](https://docs.nvidia.com/nppdefs.html#structnppicolortwistbatchcxr)structures in this call (must be > 1).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### ColorLUT[](https://docs.nvidia.com#colorlut)

Perform image color processing using members of various types of color look up tables.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_C1R_Ctx)

-
8-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_C1IR_Ctx)

-
8-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_C3R_Ctx)

-
3 channel 8-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_C4R_Ctx)

-
4 channel 8-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_C4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_C1R_Ctx)

-
16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_C1IR_Ctx)

-
16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_C3R_Ctx)

-
3 channel 16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_C4R_Ctx)

-
4 channel 16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_C4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_C4IR_Ctx)

-
4 channel 16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_C1R_Ctx)

-
16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_C1IR_Ctx)

-
16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_C3R_Ctx)

-
3 channel 16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_C3IR_Ctx)

-
3 channel 16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_C4R_Ctx)

-
4 channel 16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_C4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_C4IR_Ctx)

-
4 channel 16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_AC4R_Ctx)

-
4 channel 16-bit signed look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_16s_AC4IR_Ctx)

-
4 channel 16-bit signed look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_C1R_Ctx)

-
32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_C1IR_Ctx)

-
32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_C3R_Ctx)

-
3 channel 32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_C3IR_Ctx)

-
3 channel 32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_C4R_Ctx)

-
4 channel 32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points with no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_C4IR_Ctx)

-
4 channel 32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_AC4R_Ctx)

-
4 channel 32-bit floating point look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




### ColorLUTLinear[](https://docs.nvidia.com#colorlutlinear)

Perform image color processing using linear interpolation between members of various types of color look up tables.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_C1R_Ctx)

-
8-bit unsigned linear interpolated look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through linear interpolation.

* >>>>>>> ATTENTION ATTENTION <<<<<<< *

NOTE: As of the 5.0 release of NPP, the pValues and pLevels pointers need to be device memory pointers.

* >>>>>>> <<<<<<< *

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is now a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is now a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_C1IR_Ctx)

-
8-bit unsigned linear interpolated look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_C3R_Ctx)

-
3 channel 8-bit unsigned linear interpolated look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through linear interpolation.

* >>>>>>> ATTENTION ATTENTION <<<<<<< *

NOTE: As of the 5.0 release of NPP, the pValues and pLevels pointers need to be host memory pointers to arrays of device memory pointers.

* >>>>>>> <<<<<<< *

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned linear interpolated look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_C4R_Ctx)

-
4 channel 8-bit unsigned linear interpolated look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through linear interpolation.

* >>>>>>> ATTENTION ATTENTION <<<<<<< *

NOTE: As of the 5.0 release of NPP, the pValues and pLevels pointers need to be host memory pointers to arrays of device memory pointers.

* >>>>>>> <<<<<<< *

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_C4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned linear interpolated look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned linear interpolated look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points through linear interpolation. Alpha channel is the last channel and is not processed.

* >>>>>>> ATTENTION ATTENTION <<<<<<< *

NOTE: As of the 5.0 release of NPP, the pValues and pLevels pointers need to be host memory pointers to arrays of device memory pointers.

* >>>>>>> <<<<<<< *

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned linear interpolated look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points through linear interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_C1R_Ctx)

-
16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_C1IR_Ctx)

-
16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_C3R_Ctx)

-
3 channel 16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_C4R_Ctx)

-
4 channel 16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_C4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_C4IR_Ctx)

-
4 channel 16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_C1R_Ctx)

-
16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_C1IR_Ctx)

-
16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_C3R_Ctx)

-
3 channel 16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_C3IR_Ctx)

-
3 channel 16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_C4R_Ctx)

-
4 channel 16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_C4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_C4IR_Ctx)

-
4 channel 16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_AC4R_Ctx)

-
4 channel 16-bit signed look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_16s_AC4IR_Ctx)

-
4 channel 16-bit signed look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_C1R_Ctx)

-
32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_C1IR_Ctx)

-
32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_C3R_Ctx)

-
3 channel 32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_C3IR_Ctx)

-
3 channel 32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_C4R_Ctx)

-
4 channel 32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using linear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_C4IR_Ctx)

-
4 channel 32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_AC4R_Ctx)

-
4 channel 32-bit floating point look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Linear_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Linear_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




### ColorLUTCubic[](https://docs.nvidia.com#colorlutcubic)

Perform image color processing using linear interpolation between members of various types of color look up tables.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_C1R_Ctx)

-
8-bit unsigned cubic interpolated look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_C1IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_C1IR_Ctx)

-
8-bit unsigned cubic interpolated look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_C3R_Ctx)

-
3 channel 8-bit unsigned cubic interpolated look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned cubic interpolated look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_C4R_Ctx)

-
4 channel 8-bit unsigned cubic interpolated look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_C4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned cubic interpolated look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned cubic interpolated look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points through cubic interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_8u_AC4IR_Ctx)

-
4 channel 8-bit unsigned cubic interpolated look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points through cubic interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_C1R_Ctx)

-
16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_C1IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_C1IR_Ctx)

-
16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_C3R_Ctx)

-
3 channel 16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_C4R_Ctx)

-
4 channel 16-bit unsigned look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_C4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_C4IR_Ctx)

-
4 channel 16-bit unsigned look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16u_AC4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16u_AC4IR_Ctx)

-
4 channel 16-bit unsigned look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_C1R_Ctx)

-
16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_C1IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_C1IR_Ctx)

-
16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_C3R_Ctx)

-
3 channel 16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_C3IR_Ctx)

-
3 channel 16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_C4R_Ctx)

-
4 channel 16-bit signed look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_C4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_C4IR_Ctx)

-
4 channel 16-bit signed look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_AC4R_Ctx)

-
4 channel 16-bit signed look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_16s_AC4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pValues[3], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_16s_AC4IR_Ctx)

-
4 channel 16-bit signed look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_C1R_Ctx)

-
32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_C1IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels, int nLevels,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_C1IR_Ctx)

-
32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Pointer to an array of user defined OUTPUT values (this is a device memory pointer)**pLevels**– Pointer to an array of user defined INPUT values (this is a device memory pointer)**nLevels**– Number of user defined number of input/output mapping points (levels)**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_C3R_Ctx)

-
3 channel 32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_C3IR_Ctx)

-
3 channel 32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_C4R_Ctx)

-
4 channel 32-bit floating point look-up-table color conversion.

The LUT is derived from a set of user defined mapping points through cubic interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[4], int nLevels[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_C4IR_Ctx)

-
4 channel 32-bit floating point look-up-table in place color conversion.

The LUT is derived from a set of user defined mapping points using no interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 4 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_AC4R_Ctx)

-
4 channel 32-bit floating point look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Cubic_32f_AC4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pValues[3], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pLevels[3], int nLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Cubic_32f_AC4IR_Ctx)

-
4 channel 32-bit floating point look-up-table in place color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points using no interpolation. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT values.**pLevels**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined INPUT values.**nLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per color CHANNEL.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 1024 (the current size limit).




### ColorLUTTrilinear[](https://docs.nvidia.com#colorluttrilinear)

Perform image color processing using 3D trilinear interpolation between members of various types of color look up tables.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Trilinear_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pValues,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pLevels[3], int aLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Trilinear_8u_C4R_Ctx)

-
Four channel 8-bit unsigned 3D trilinear interpolated look-up-table color conversion, with alpha copy.

Alpha channel is the last channel and is copied to the destination unmodified.

The LUT is derived from a set of user defined mapping points through trilinear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Device pointer to aLevels[2] number of contiguous 2D x,y planes of 4-byte packed RGBX values containing the user defined base OUTPUT values at that x,y, and z (R,G,B) level location. Each level must contain x * y 4-byte packed pixel values (4th byte is used for alignement only and is ignored) in row (x) order.**pLevels**– Host pointer to an array of 3 host pointers, one per cube edge, pointing to user defined INPUT level values.**aLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per 3D cube edge. aLevels[0] represents the number of x axis levels (Red), aLevels[1] represents the number of y axis levels (Green), and aLevels[2] represets the number of z axis levels (Blue).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Trilinear_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pValues,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pLevels[3], int aLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Trilinear_8u_AC4R_Ctx)

-
Four channel 8-bit unsigned 3D trilinear interpolated look-up-table color conversion, not affecting alpha.

Alpha channel is the last channel and is not processed.

The LUT is derived from a set of user defined mapping points through trilinear interpolation.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Device pointer to aLevels[2] number of contiguous 2D x,y planes of 4-byte packed RGBX values containing the user defined base OUTPUT values at that x,y, and z (R,G,B) level location. Each level must contain x * y 4-byte packed pixel values (4th byte is used for alignement only and is ignored) in row (x) order.**pLevels**– Host pointer to an array of 3 host pointers, one per cube edge, pointing to user defined INPUT level values.**aLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per 3D cube edge. aLevels[0] represents the number of x axis levels (Red), aLevels[1] represents the number of y axis levels (Green), and aLevels[2] represets the number of z axis levels (Blue).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUT_Trilinear_8u_AC4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pValues,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pLevels[3], int aLevels[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUT_Trilinear_8u_AC4IR_Ctx)

-
Four channel 8-bit unsigned 3D trilinear interpolated look-up-table in place color conversion, not affecting alpha.

Alpha channel is the last channel and is not processed.

The LUT is derived from a set of user defined mapping points through trilinear interpolation.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pValues**– Device pointer aLevels[2] number of contiguous 2D x,y planes of 4-byte packed RGBX values containing the user defined base OUTPUT values at that x,y, and z (R,G,B) level location. Each level must contain x * y 4-byte packed pixel values (4th byte is used for alignement only and is ignored) in row (x) order.**pLevels**– Host pointer to an array of 3 host pointers, one per cube edge, pointing to user defined INPUT level values.**aLevels**– Host pointer to an array of 3 user defined number of input/output mapping points, one per 3D cube edge. aLevels[0] represents the number of x axis levels (Red), aLevels[1] represents the number of y axis levels (Green), and aLevels[2] represets the number of z axis levels (Blue).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_NUMBER_OF_LEVELS_ERROR if the number of levels is less than 2 or greater than 256.




### ColorLUTPalette[](https://docs.nvidia.com#colorlutpalette)

Perform image color processing using various types of bit range restricted palette color look up tables.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_8u_C1R_Ctx)

-
One channel 8-bit unsigned bit range restricted palette look-up-table color conversion.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_8u24u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_8u24u_C1R_Ctx)

-
One channel 8-bit unsigned bit range restricted 24-bit palette look-up-table color conversion with 24-bit destination output per pixel.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(3 bytes per pixel).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_8u32u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_8u32u_C1R_Ctx)

-
One channel 8-bit unsigned bit range restricted 32-bit palette look-up-table color conversion with 32-bit destination output per pixel.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(4 bytes per pixel).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTables[3], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_8u_C3R_Ctx)

-
Three channel 8-bit unsigned bit range restricted palette look-up-table color conversion.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values.**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTables[4], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_8u_C4R_Ctx)

-
Four channel 8-bit unsigned bit range restricted palette look-up-table color conversion.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values.**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTables[3], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_8u_AC4R_Ctx)

-
Four channel 8-bit unsigned bit range restricted palette look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values.**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u_C1R_Ctx)

-
One channel 16-bit unsigned bit range restricted palette look-up-table color conversion.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u8u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u8u_C1R_Ctx)

-
One channel 16-bit unsigned bit range restricted 8-bit unsigned palette look-up-table color conversion with 8-bit unsigned destination output per pixel.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(1 unsigned byte per pixel).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u24u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u24u_C1R_Ctx)

-
One channel 16-bit unsigned bit range restricted 24-bit unsigned palette look-up-table color conversion with 24-bit unsigned destination output per pixel.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(3 unsigned bytes per pixel).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u32u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pTable, int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u32u_C1R_Ctx)

-
One channel 16-bit unsigned bit range restricted 32-bit palette look-up-table color conversion with 32-bit unsigned destination output per pixel.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(4 bytes per pixel).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTable**– Pointer to an array of user defined OUTPUT palette values (this is a device memory pointer)**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pTables[3], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u_C3R_Ctx)

-
Three channel 16-bit unsigned bit range restricted palette look-up-table color conversion.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values.**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pTables[4], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u_C4R_Ctx)

-
Four channel 16-bit unsigned bit range restricted palette look-up-table color conversion.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 4 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values.**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPalette_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pTables[3], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPalette_16u_AC4R_Ctx)

-
Four channel 16-bit unsigned bit range restricted palette look-up-table color conversion, not affecting Alpha.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values. Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values.**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPaletteSwap_8u_C3A0C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep, int nAlphaValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pTables[3], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPaletteSwap_8u_C3A0C4R_Ctx)

-
Three channel 8-bit unsigned source bit range restricted palette look-up-table color conversion to four channel 8-bit unsigned destination output with alpha.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values. This function also reverses the source pixel channel order in the destination so the Alpha channel is the first channel.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)(3 bytes per pixel).**nAlphaValue**– Signed alpha value that will be used to initialize the pixel alpha channel position in all modified destination pixels.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(4 bytes per pixel with alpha).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values. Alpha values < 0 or > 255 will cause destination pixel alpha channel values to be unmodified.**nBitSize**– Number of least significant bits (must be > 0 and <= 8) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 8.




-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUTPaletteSwap_16u_C3A0C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep, int nAlphaValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pTables[3], int nBitSize,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUTPaletteSwap_16u_C3A0C4R_Ctx)

-
Three channel 16-bit unsigned source bit range restricted palette look-up-table color conversion to four channel 16-bit unsigned destination output with alpha.

The LUT is derived from a set of user defined mapping points in a palette and source pixels are then processed using a restricted bit range when looking up palette values. This function also reverses the source pixel channel order in the destination so the Alpha channel is the first channel.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step)(3 unsigned short integers per pixel).**nAlphaValue**– Signed alpha value that will be used to initialize the pixel alpha channel position in all modified destination pixels.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step)(4 unsigned short integers per pixel with alpha).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**pTables**– Host pointer to an array of 3 device memory pointers, one per color CHANNEL, pointing to user defined OUTPUT palette values. Alpha values < 0 or > 65535 will cause destination pixel alpha channel values to be unmodified.**nBitSize**– Number of least significant bits (must be > 0 and <= 16) of each source pixel value to use as index into palette table during conversion.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes)NPP_LUT_PALETTE_BITSIZE_ERROR if nBitSize is < 1 or > 16.




## Color Sampling Format Conversion Functions[](https://docs.nvidia.com#color-sampling-format-conversion-functions)

Routines for converting between various image color sampling formats.

### YCbCr420ToYCbCr411[](https://docs.nvidia.com#ycbcr420toycbcr411)

YCbCr420 to YCbCr411 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToYCbCr411_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToYCbCr411_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 2 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToYCbCr411_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToYCbCr411_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToYCbCr422[](https://docs.nvidia.com#ycbcr422toycbcr422)

YCbCr422 to YCbCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 2 channel 8-bit unsigned packed YCbCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToYCrCb422[](https://docs.nvidia.com#ycbcr422toycrcb422)

YCbCr422 to YCrCb422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCrCb422_8u_C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCrCb422_8u_C2R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 2 channel 8-bit unsigned packed YCrCb422 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCrCb422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCrCb422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 2 channel 8-bit unsigned packed YCrCb422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToCbYCr422[](https://docs.nvidia.com#ycbcr422tocbycr422)

YCbCr422 to CbYCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToCbYCr422_8u_C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToCbYCr422_8u_C2R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 2 channel 8-bit unsigned packed CbYCr422 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToYCbCr411[](https://docs.nvidia.com#cbycr422toycbcr411)

CbYCr422 to YCbCr411 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToYCbCr411_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToYCbCr411_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 3 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToYCbCr420[](https://docs.nvidia.com#ycbcr422toycbcr420)

YCbCr422 to YCbCr420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr420_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr420_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr420_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr420_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 2 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr420_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr420_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr420_8u_C2P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr420_8u_C2P2R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 2 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb420ToYCbCr422[](https://docs.nvidia.com#ycrcb420toycbcr422)

YCrCb420 to YCbCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb420ToYCbCr422_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb420ToYCbCr422_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCrCb420 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb420ToYCbCr422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb420ToYCbCr422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar YCrCb420 to 2 channel 8-bit unsigned packed YCbCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToYCrCb420[](https://docs.nvidia.com#ycbcr422toycrcb420)

YCbCr422 to YCrCb420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCrCb420_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCrCb420_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned planar YCrCb420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToYCbCr411[](https://docs.nvidia.com#ycbcr422toycbcr411)

YCbCr422 to YCbCr411 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr411_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr411_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr411_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr411_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 2 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr411_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr411_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToYCbCr411_8u_C2P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToYCbCr411_8u_C2P2R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 2 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb422ToYCbCr422[](https://docs.nvidia.com#ycrcb422toycbcr422)

YCrCb422 to YCbCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb422ToYCbCr422_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb422ToYCbCr422_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb422ToYCbCr420[](https://docs.nvidia.com#ycrcb422toycbcr420)

YCrCb422 to YCbCr420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb422ToYCbCr420_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb422ToYCbCr420_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb422ToYCbCr411[](https://docs.nvidia.com#ycrcb422toycbcr411)

YCrCb422 to YCbCr411 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb422ToYCbCr411_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb422ToYCbCr411_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 3 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToYCbCr422[](https://docs.nvidia.com#cbycr422toycbcr422)

CbYCr422 to YCbCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToYCbCr422_8u_C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToYCbCr422_8u_C2R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 2 channel 8-bit unsigned packed YCbCr422 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToYCbCr422_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToYCbCr422_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToYCbCr420[](https://docs.nvidia.com#cbycr422toycbcr420)

CbYCr422 to YCbCr420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToYCbCr420_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToYCbCr420_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToYCbCr420_8u_C2P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToYCbCr420_8u_C2P2R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 2 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToYCrCb420[](https://docs.nvidia.com#cbycr422toycrcb420)

CbYCr422 to YCrCb420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToYCrCb420_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToYCrCb420_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 3 channel 8-bit unsigned planar YCrCb420 sampling format conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToYCbCr420[](https://docs.nvidia.com#ycbcr420toycbcr420)

YCbCr420 to YCbCr420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 2 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToYCbCr422[](https://docs.nvidia.com#ycbcr420toycbcr422)

YCbCr420 to YCbCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToYCbCr422_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToYCbCr422_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToYCbCr422_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToYCbCr422_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToYCbCr422_8u_P2C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToYCbCr422_8u_P2C2R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr420 to 2 channel 8-bit unsigned packed YCbCr422 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToCbYCr422[](https://docs.nvidia.com#ycbcr420tocbycr422)

YCbCr420 to CbYCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToCbYCr422_8u_P2C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToCbYCr422_8u_P2C2R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr420 to 2 channel 8-bit unsigned packed CbYCr422 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToYCrCb420[](https://docs.nvidia.com#ycbcr420toycrcb420)

YCbCr420 to YCrCb420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToYCrCb420_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToYCrCb420_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar YCrCb420 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb420ToCbYCr422[](https://docs.nvidia.com#ycrcb420tocbycr422)

YCrCb420 to CbYCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb420ToCbYCr422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb420ToCbYCr422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar YCrCb420 to 2 channel 8-bit unsigned packed CbYCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb420ToYCbYCr420[](https://docs.nvidia.com#ycrcb420toycbycr420)

YCrCb420 to YCbCr420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb420ToYCbCr420_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb420ToYCbCr420_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCrCb420 to 2 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb420ToYCbYCr411[](https://docs.nvidia.com#ycrcb420toycbycr411)

YCrCb420 to YCbCr411 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb420ToYCbCr411_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb420ToYCbCr411_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCrCb420 to 2 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToYCbCr411[](https://docs.nvidia.com#ycbcr411toycbcr411)

YCbCr411 to YCbCr411 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 2 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCbCr411 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToYCbCr422[](https://docs.nvidia.com#ycbcr411toycbcr422)

YCbCr411 to YCbCr422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr422_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr422_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 2 channel 8-bit unsigned packed YCbCr422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr422_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr422_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCbCr422 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr422_8u_P2C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr422_8u_P2C2R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr411 to 2 channel 8-bit unsigned packed YCbCr422 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToYCrCb422[](https://docs.nvidia.com#ycbcr411toycrcb422)

YCbCr411 to YCrCb422 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCrCb422_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCrCb422_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCrCb422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCrCb422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCrCb422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 2 channel 8-bit unsigned packed YCrCb422 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToYCbCr420[](https://docs.nvidia.com#ycbcr411toycbcr420)

YCbCr411 to YCbCr420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr420_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr420_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr420_8u_P3P2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstY, int nDstYStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDstCbCr, int nDstCbCrStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr420_8u_P3P2R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 2 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDstY**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstYStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**pDstCbCr**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstCbCrStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCbCr420_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCbCr420_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCbCr420 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToYCrCb420[](https://docs.nvidia.com#ycbcr411toycrcb420)

YCbCr411 to YCrCb420 sampling format conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToYCrCb420_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcY, int nSrcYStep, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcCbCr, int nSrcCbCrStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToYCrCb420_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar YCrCb420 sampling format conversion.

- Parameters
-
**pSrcY**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcYStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**pSrcCbCr**–[Source-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer).**nSrcCbCrStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### NV12ToYUV420[](https://docs.nvidia.com#nv12toyuv420)

NV12 to YUV420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToYUV420_8u_P2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToYUV420_8u_P2P3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned planar YUV420 color conversion.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**nSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


## Color Model Conversion Functions[](https://docs.nvidia.com#color-model-conversion-functions)

Routines for converting between various image color models.

### RGBToYUV[](https://docs.nvidia.com#rgbtoyuv)

RGB to YUV color conversion.

Here is how NPP converts gamma corrected RGB or BGR to YUV. For digital RGB values in the range [0..255], Y has the range [0..255], U varies in the range [-112..+112], and V in the range [-157..+157]. To fit in the range of [0..255], a constant value of 128 is added to computed U and V values, and V is then saturated.

```
Npp32f nY = 0.299F * R + 0.587F * G + 0.114F * B;
Npp32f nU = (0.492F * ((Npp32f)nB - nY)) + 128.0F;
Npp32f nV = (0.877F * ((Npp32f)nR - nY)) + 128.0F;
if (nV > 255.0F)
nV = 255.0F;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned packed YUV color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned packed YUV color conversion with alpha, not affecting alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YUV color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YUV color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV_8u_AC4P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV_8u_AC4P4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned planar YUV color conversion with alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYUV[](https://docs.nvidia.com#bgrtoyuv)

BGR to YUV color conversion.

Here is how NPP converts gamma corrected RGB or BGR to YUV. For digital RGB values in the range [0..255], Y has the range [0..255], U varies in the range [-112..+112], and V in the range [-157..+157]. To fit in the range of [0..255], a constant value of 128 is added to computed U and V values, and V is then saturated.

```
Npp32f nY = 0.299F * R + 0.587F * G + 0.114F * B;
Npp32f nU = (0.492F * ((Npp32f)nB - nY)) + 128.0F;
Npp32f nV = (0.877F * ((Npp32f)nR - nY)) + 128.0F;
if (nV > 255.0F)
nV = 255.0F;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYUV_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYUV_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned packed YUV color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYUV_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYUV_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 4 channel 8-bit unsigned packed YUV color conversion with alpha, not affecting alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYUV_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYUV_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned planar YUV color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYUV_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYUV_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YUV color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYUV_8u_AC4P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYUV_8u_AC4P4R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 4 channel 8-bit unsigned planar YUV color conversion with alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUVToRGB[](https://docs.nvidia.com#yuvtorgb)

YUV to RGB color conversion.

Here is how NPP converts YUV to gamma corrected RGB or BGR.

```
Npp32f nY = (Npp32f)Y;
Npp32f nU = (Npp32f)U - 128.0F;
Npp32f nV = (Npp32f)V - 128.0F;
Npp32f nR = nY + 1.140F * nV;
if (nR < 0.0F)
nR = 0.0F;
if (nR > 255.0F)
nR = 255.0F;
Npp32f nG = nY - 0.394F * nU - 0.581F * nV;
if (nG < 0.0F)
nG = 0.0F;
if (nG > 255.0F)
nG = 255.0F;
Npp32f nB = nY + 2.032F * nU;
if (nB < 0.0F)
nB = 0.0F;
if (nB > 255.0F)
nB = 255.0F;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YUV to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit packed YUV with alpha to 4 channel 8-bit unsigned packed RGB color conversion with alpha, not affecting alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGB_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGB_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUVToRGBBatch[](https://docs.nvidia.com#yuvtorgbbatch)

YUV to RGB batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

NPP converts YUV to gamma corrected RGB the same way as in [YUVToRGB](https://docs.nvidia.com#group__yuvtorgb).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGBBatch_8u_C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGBBatch_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YUV to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input and output images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGBBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGBBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUVToRGBBatchAdvanced[](https://docs.nvidia.com#yuvtorgbbatchadvanced)

YUV to RGB batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

NPP converts YUV to gamma corrected RGB the same way as in [YUVToRGB](https://docs.nvidia.com#group__yuvtorgb).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGBBatch_8u_C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGBBatch_8u_C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned packed YUV to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToRGBBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToRGBBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUVToBGR[](https://docs.nvidia.com#yuvtobgr)

YUV to BGR color conversion.

Here is how NPP converts YUV to gamma corrected RGB or BGR.

```
Npp32f nY = (Npp32f)Y;
Npp32f nU = (Npp32f)U - 128.0F;
Npp32f nV = (Npp32f)V - 128.0F;
Npp32f nR = nY + 1.140F * nV;
if (nR < 0.0F)
nR = 0.0F;
if (nR > 255.0F)
nR = 255.0F;
Npp32f nG = nY - 0.394F * nU - 0.581F * nV;
if (nG < 0.0F)
nG = 0.0F;
if (nG > 255.0F)
nG = 255.0F;
Npp32f nB = nY + 2.032F * nU;
if (nB < 0.0F)
nB = 0.0F;
if (nB > 255.0F)
nB = 255.0F;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGR_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGR_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YUV to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGR_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGR_8u_AC4R_Ctx)

-
4 channel 8-bit packed YUV with alpha to 4 channel 8-bit unsigned packed BGR color conversion with alpha, not affecting alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGR_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGR_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUVToBGRBatch[](https://docs.nvidia.com#yuvtobgrbatch)

YUV to BGR batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

NPP converts YUV to gamma corrected BGR the same way as in [YUVToBGR](https://docs.nvidia.com#group__yuvtobgr).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGRBatch_8u_C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGRBatch_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YUV to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input and output images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGRBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGRBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUVToBGRBatchAdvanced[](https://docs.nvidia.com#yuvtobgrbatchadvanced)

YUV to BGR batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

NPP converts YUV to gamma corrected BGR the same way as in [YUVToBGR](https://docs.nvidia.com#group__yuvtobgr).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGRBatch_8u_C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGRBatch_8u_C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned packed YUV to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUVToBGRBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUVToBGRBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YUV to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYUV422[](https://docs.nvidia.com#rgbtoyuv422)

RGB to YUV422 color conversion.

NPP converts YUV to gamma corrected BGR the same way as in [YUVToBGR](https://docs.nvidia.com#group__yuvtobgr).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_8u_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_8u_C3C2R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 2 channel 8-bit unsigned packed YUV422 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YUV422 color conversion.

images.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV422_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV422_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YUV422 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV422ToRGB[](https://docs.nvidia.com#yuv422torgb)

YUV422 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_C2C3R_Ctx)

-
2 channel 8-bit unsigned packed YUV422 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGB_8u_P3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGB_8u_P3AC4R_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 4 channel 8-bit unsigned packed RGB color conversion with alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV422ToRGBBatch[](https://docs.nvidia.com#yuv422torgbbatch)

Planar YUV422 to packed RGB batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGBBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGBBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV422ToRGBBatchAdvanced[](https://docs.nvidia.com#yuv422torgbbatchadvanced)

Planar YUV422 to packed RGB batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToRGBBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToRGBBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV422ToBGRBatch[](https://docs.nvidia.com#yuv422tobgrbatch)

Planar YUV422 to packed BGR batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToBGRBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToBGRBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV422ToBGRBatchAdvanced[](https://docs.nvidia.com#yuv422tobgrbatchadvanced)

Planar YUV422 to packed BGR batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV422ToBGRBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV422ToBGRBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YUV422 to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYUV420[](https://docs.nvidia.com#rgbtoyuv420)

RGB to YUV420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV420_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV420_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YUV420 color conversion.

images.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYUV420_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYUV420_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YUV420 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV420ToRGB[](https://docs.nvidia.com#yuv420torgb)

YUV420 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**nDstStep**–[Destination-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 4 channel 8-bit unsigned packed RGB color conversion with constant alpha (0xFF).

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGB_8u_P3AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGB_8u_P3AC4R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 4 channel 8-bit unsigned packed RGB color conversion with alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV420ToRGBBatch[](https://docs.nvidia.com#yuv420torgbbatch)

Planar YUV420 to packed RGB batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGBBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGBBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents Y planes. The second element of array (pSrcBatchList[1]) represents U planes. The third element of array (pSrcBatchList[2]) represents V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV420ToRGBBatchAdvanced[](https://docs.nvidia.com#yuv420torgbbatchadvanced)

Planar YUV420 to packed RGB batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToRGBBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToRGBBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### NV12ToRGB[](https://docs.nvidia.com#nv12torgb)

NV12 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each source plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_709HDTV_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_709HDTV_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed RGB 709 HDTV full color conversion.

Note that HDTV conversion assumes full color range of 0 - 255, use CSC version for limited range color.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_709CSC_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_709CSC_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed RGB 709 CSC color conversion.

Note that HDTV conversion assumes full color range of 0 - 255, use CSC version for limited range color.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToRGB_601_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToRGB_601_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed RGB BT.601 full-range color conversion (ITU-T T.871 / JFIF).

Coefficients derived from BT.601 luma weights (Kr=0.299, Kb=0.114) with full digital range Y=[0..255], Cb/Cr=[0..255] (offset 128). Use this variant for cameras that signal full-range BT.601 NV12 (e.g. OAK-D VPU encoder output), as distinct from the unspecified-range default nppiNV12ToRGB_8u_P2C3R and the BT.709 variants.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### NV21ToRGB[](https://docs.nvidia.com#nv21torgb)

NV21 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV21ToRGB_8u_P2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV21ToRGB_8u_P2C4R_Ctx)

-
2 channel 8-bit unsigned planar NV21 to 4 channel 8-bit unsigned packed RGBA color conversion with constant alpha (0xFF).

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for VU plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYUV420[](https://docs.nvidia.com#bgrtoyuv420)

BGR to YUV420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYUV420_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYUV420_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned pacmed BGR with alpha to 3 channel 8-bit unsigned planar YUV420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV420ToBGR[](https://docs.nvidia.com#yuv420tobgr)

YUV420 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToBGR_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToBGR_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 4 channel 8-bit unsigned packed BGR color conversion with constant alpha (0xFF).

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV420ToBGRBatch[](https://docs.nvidia.com#yuv420tobgrbatch)

Planar YUV420 to packed BGR batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToBGRBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToBGRBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents Y planes. The second element of array (pSrcBatchList[1]) represents U planes. The third element of array (pSrcBatchList[2]) represents V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YUV420ToBGRBatchAdvanced[](https://docs.nvidia.com#yuv420tobgrbatchadvanced)

Planar YUV420 to packed BGR batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYUV420ToBGRBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYUV420ToBGRBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YUV420 to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of U planes. The third element of array (pSrcBatchList[2]) represents a batch of V planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### NV12ToBGR[](https://docs.nvidia.com#nv12tobgr)

NV12 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToBGR_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToBGR_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToBGR_709HDTV_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToBGR_709HDTV_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed RGB 709 HDTV full color conversion.

Note that HDTV conversion assumes full color range of 0 - 255, use CSC version for limited range color.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToBGR_709CSC_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToBGR_709CSC_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed RGB 709 CSC color conversion.

Note that HDTV conversion assumes full color range of 0 - 255, use CSC version for limited range color.

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV12ToBGR_601_8u_P2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV12ToBGR_601_8u_P2C3R_Ctx)

-
2 channel 8-bit unsigned planar NV12 to 3 channel 8-bit unsigned packed BGR BT.601 full-range color conversion (ITU-T T.871 / JFIF).

Coefficients derived from BT.601 luma weights (Kr=0.299, Kb=0.114) with full digital range Y=[0..255], Cb/Cr=[0..255] (offset 128).

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for UV plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### NV21ToBGR[](https://docs.nvidia.com#nv21tobgr)

NV21 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiNV21ToBGR_8u_P2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[2], int rSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiNV21ToBGR_8u_P2C4R_Ctx)

-
2 channel 8-bit unsigned planar NV21 to 4 channel 8-bit unsigned packed BGRA color conversion with constant alpha (0xFF).

- Parameters
-
**pSrc**–[Source-Planar-Image Pointer Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_pointer_array)(one for Y plane, one for VU plane).**rSrcStep**–[Source-Planar-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step). Same value is used for each plane.**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYCbCr[](https://docs.nvidia.com#rgbtoycbcr)

RGB to YCbCr color conversion.

Here is how NPP converts gamma corrected RGB or BGR to YCbCr. In the YCbCr model, Y is defined to have a nominal range [16..235], while Cb and Cr are defined to have a range [16..240], with the value of 128 as corresponding to zero.

```
Npp32f nY = 0.257F * R + 0.504F * G + 0.098F * B + 16.0F;
Npp32f nCb = -0.148F * R - 0.291F * G + 0.439F * B + 128.0F;
Npp32f nCr = 0.439F * R - 0.368F * G - 0.071F * B + 128.0F;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel unsigned 8-bit packed YCbCr color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel unsigned 8-bit packed YCbCr with alpha color conversion, not affecting alpha.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr_8u_P3R_Ctx)

-
3 channel planar 8-bit unsigned RGB to 3 channel planar 8-bit YCbCr color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel unsigned 8-bit planar YCbCr color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 3 channel 8-bit unsigned planar YCbCr color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToRGB[](https://docs.nvidia.com#ycbcrtorgb)

YCbCr to RGB color conversion.

Here is how NPP converts YCbCr to gamma corrected RGB or BGR. The output RGB values are saturated to the range [0..255].

```
Npp32f nY = 1.164F * ((Npp32f)Y - 16.0F);
Npp32f nR = ((Npp32f)Cr - 128.0F); Npp32f nB = ((Npp32f)Cb
- 128.0F); Npp32f nG = nY - 0.813F * nR - 0.392F * nB; if (nG > 255.0F)
nG = 255.0F;
nR = nY + 1.596F * nR;
if (nR > 255.0F)
nR = 255.0F;
nB = nY + 2.017F * nB;
if (nB > 255.0F)
nB = 255.0F;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YCbCr to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed YCbCr with alpha to 4 channel 8-bit unsigned packed RGB with alpha color conversion, not affecting alpha.

Alpha channel is the last channel and is not processed.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGB_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGB_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGB_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGB_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 4 channel 8-bit unsigned packed RGB color conversion with constant alpha.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToRGBBatch[](https://docs.nvidia.com#ycbcrtorgbbatch)

YCbCr to RGB batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

NPP converts YCbCr to gamma corrected RGB the same way as in [YCbCr To RGB](https://docs.nvidia.com#group__ycbcrtorgb).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGBBatch_8u_C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGBBatch_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YCbCr to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input and output images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGBBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGBBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToRGBBatchAdvanced[](https://docs.nvidia.com#ycbcrtorgbbatchadvanced)

YCbCr to RGB batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

NPP converts YCbCr to gamma corrected RGB the same way as in [YCbCr To RGB](https://docs.nvidia.com#group__ycbcrtorgb).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGBBatch_8u_C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGBBatch_8u_C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned packed YCbCr to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToRGBBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToRGBBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToBGR[](https://docs.nvidia.com#ycbcrtobgr)

YCbCr to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGR_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGR_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 4 channel 8-bit unsigned packed BGR color conversion with constant alpha.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToBGRBatch[](https://docs.nvidia.com#ycbcrtobgrbatch)

YCbCr to BGR batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

NPP converts YCbCr to gamma corrected BGR the same way as in [YCbCrToBGR](https://docs.nvidia.com#group__ycbcrtobgr).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGRBatch_8u_C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGRBatch_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YCbCr to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input and output images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGRBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGRBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToBGRBatchAdvanced[](https://docs.nvidia.com#ycbcrtobgrbatchadvanced)

YCbCr to BGR batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

NPP converts YCbCr to gamma corrected BGR the same way as in [YCbCrToBGR](https://docs.nvidia.com#group__ycbcrtobgr).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGRBatch_8u_C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pSrcBatchList,[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGRBatch_8u_C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned packed YCbCr to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**–[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer).**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGRBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGRBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCrToBGR709CSC[](https://docs.nvidia.com#ycbcrtobgr709csc)

YCbCr to BGR_709CSC color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGR_709CSC_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGR_709CSC_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 3 channel 8-bit unsigned packed BGR_709CSC color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCrToBGR_709CSC_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCrToBGR_709CSC_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr to 4 channel 8-bit unsigned packed BGR_709CSC color conversion with constant alpha.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYCbCr422[](https://docs.nvidia.com#rgbtoycbcr422)

RGB to YCbCr422 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr422_8u_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr422_8u_C3C2R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 2 channel 8-bit unsigned packed YCbCr422 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr422_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr422_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YCbCr422 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 2 channel 8-bit unsigned packed YCbCr422 color conversion.

images.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToRGB[](https://docs.nvidia.com#ycbcr422torgb)

YCbCr422 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGB_8u_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGB_8u_C2C3R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned packed RGB color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGB_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGB_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned planar RGB color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed RGB color conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToRGBBatch[](https://docs.nvidia.com#ycbcr422torgbbatch)

Planar YCbCr422 to packed RGB batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGBBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGBBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToRGBBatchAdvanced[](https://docs.nvidia.com#ycbcr422torgbbatchadvanced)

Planar YCbCr422 to packed RGB batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGBBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGBBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYCrCb422[](https://docs.nvidia.com#rgbtoycrcb422)

RGB to YCrCb422 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCrCb422_8u_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCrCb422_8u_C3C2R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 2 channel 8-bit unsigned packed YCrCb422 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCrCb422_8u_P3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCrCb422_8u_P3C2R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 2 channel 8-bit unsigned packed YCrCb422 color conversion.

images.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb422ToRGB[](https://docs.nvidia.com#ycrcb422torgb)

YCrCb422 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb422ToRGB_8u_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb422ToRGB_8u_C2C3R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 3 channel 8-bit unsigned packed RGB color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb422ToRGB_8u_C2P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb422ToRGB_8u_C2P3R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 3 channel 8-bit unsigned planar RGB color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Planar-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_planar_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToBGR[](https://docs.nvidia.com#ycbcr422tobgr)

YCbCr422 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGR_8u_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGR_8u_C2C3R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 3 channel 8-bit unsigned packed BGR color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGR_8u_C2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGR_8u_C2C4R_Ctx)

-
2 channel 8-bit unsigned packed YCrCb422 to 4 channel 8-bit unsigned packed BGR color conversion with constant alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed BGR color conversion.

images.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToBGRBatch[](https://docs.nvidia.com#ycbcr422tobgrbatch)

Planar YCbCr422 to packed BGR batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGRBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGRBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr422ToBGRBatchAdvanced[](https://docs.nvidia.com#ycbcr422tobgrbatchadvanced)

Planar YCbCr422 to packed BGR batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGRBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGRBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToCbYCr422[](https://docs.nvidia.com#rgbtocbycr422)

RGB to CbYCr422 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToCbYCr422_8u_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToCbYCr422_8u_C3C2R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 2 channel 8-bit unsigned packed CbYCr422 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToCbYCr422Gamma_8u_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToCbYCr422Gamma_8u_C3C2R_Ctx)

-
3 channel 8-bit unsigned packed RGB first gets forward gamma corrected then converted to 2 channel 8-bit unsigned packed CbYCr422 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToRGB[](https://docs.nvidia.com#cbycr422torgb)

CbYCr422 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToRGB_8u_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToRGB_8u_C2C3R_Ctx)

-
2 channel 8-bit unsigned packed CbYCrC22 to 3 channel 8-bit unsigned packed RGB color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToCbYCr422[](https://docs.nvidia.com#bgrtocbycr422)

BGR to CbYCr422 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToCbYCr422_8u_AC4C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToCbYCr422_8u_AC4C2R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 2 channel 8-bit unsigned packed CbYCr422 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToCbYCr422 709HDTV[](https://docs.nvidia.com#bgrtocbycr422-709hdtv)

BGR to CbYCr422_709HDTV color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToCbYCr422_709HDTV_8u_C3C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToCbYCr422_709HDTV_8u_C3C2R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 2 channel 8-bit unsigned packed CbYCr422_709HDTV color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToCbYCr422_709HDTV_8u_AC4C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToCbYCr422_709HDTV_8u_AC4C2R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 2 channel 8-bit unsigned packed CbYCr422_709HDTV color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToBGR[](https://docs.nvidia.com#cbycr422tobgr)

CbYCr422 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToBGR_8u_C2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToBGR_8u_C2C4R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 4 channel 8-bit unsigned packed BGR color conversion with alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CbYCr422ToBGR 709HDTV[](https://docs.nvidia.com#cbycr422tobgr-709hdtv)

CbYCr422 to BGR_709HDTV color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToBGR_709HDTV_8u_C2C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToBGR_709HDTV_8u_C2C3R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 3 channel 8-bit unsigned packed BGR_709HDTV color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCbYCr422ToBGR_709HDTV_8u_C2C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCbYCr422ToBGR_709HDTV_8u_C2C4R_Ctx)

-
2 channel 8-bit unsigned packed CbYCr422 to 4 channel 8-bit unsigned packed BGR_709HDTV color conversion with constant alpha.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYCbCr420[](https://docs.nvidia.com#rgbtoycbcr420)

RGB to YCbCr420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr420_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr420_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToRGB[](https://docs.nvidia.com#ycbcr420torgb)

YCbCr420 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToRGBBatch[](https://docs.nvidia.com#ycbcr420torgbbatch)

Planar YCbCr420 to packed RGB batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToRGBBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToRGBBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed RGB batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToRGBBatchAdvanced[](https://docs.nvidia.com#ycbcr420torgbbatchadvanced)

Planar YCbCr420 to packed RGB batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToRGBBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToRGBBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed RGB batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYCrCb420[](https://docs.nvidia.com#rgbtoycrcb420)

RGB to YCrCb420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCrCb420_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCrCb420_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 3 channel 8-bit unsigned planar YCrCb420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCrCb420ToRGB[](https://docs.nvidia.com#ycrcb420torgb)

YCrCb420 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCrCb420ToRGB_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCrCb420ToRGB_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCrCb420 to 4 channel 8-bit unsigned packed RGB color conversion with constant alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCbCr420[](https://docs.nvidia.com#bgrtoycbcr420)

BGR to YCbCr420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCbCr420 709CSC[](https://docs.nvidia.com#bgrtoycbcr420-709csc)

BGR to YCbCr420_709CSC color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_709CSC_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_709CSC_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr420_709CSC color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_709CSC_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_709CSC_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCbCr420_709CSC color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCbCr420 709HDTV[](https://docs.nvidia.com#bgrtoycbcr420-709hdtv)

BGR to YCbCr420_709HDTV color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_709HDTV_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_709HDTV_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCbCr420_709HDTV color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCrCb420 709CSC[](https://docs.nvidia.com#bgrtoycrcb420-709csc)

BGR to YCrCb420_709CSC color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCrCb420_709CSC_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCrCb420_709CSC_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCrCb420_709CSC color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCrCb420_709CSC_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCrCb420_709CSC_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCrCb420_709CSC color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToBGR[](https://docs.nvidia.com#ycbcr420tobgr)

YCbCr420 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGR_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGR_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 4 channel 8-bit unsigned packed BGR color conversion with constant alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToBGRBatch[](https://docs.nvidia.com#ycbcr420tobgrbatch)

Planar YCbCr420 to packed BGR batch color conversion with a single [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification) for all pairs of input/output images provided in batches.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGRBatch_8u_P3C3R_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGRBatch_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed BGR batch color conversion for a single ROI.

Provided oSizeROI will be used for all pairs of input planes making input images and output packed images passed in pSrcBatchList and pSrcBatchList arguments. API user must ensure that provided ROI (oSizeROI) does not go beyond the borders of any of provided images.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– A number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToBGRBatchAdvanced[](https://docs.nvidia.com#ycbcr420tobgrbatchadvanced)

Planar YCbCr420 to packed BGR batch color conversion where each pair of input/output images from provided batches has own [Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGRBatch_8u_P3C3R_Advanced_Ctx(const[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*const pSrcBatchList[3],[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#c.NppiImageDescriptor)*pDstBatchList, int nBatchSize,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaxSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGRBatch_8u_P3C3R_Advanced_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed BGR batch color conversion where each pair of input/output images has own ROI.

Provided oMaxSizeROI must contain the maximum width and the maximum height of all ROIs defined in pDstBatchList. API user must ensure that ROI from pDstBatchList for each pair of input and output images does not go beyond the borders of images in each pair.

- Parameters
-
**pSrcBatchList**– An array where each element is a batch of images representing one of planes in planar images,[Source-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_batch_images_pointer). The first element of array (pSrcBatchList[0]) represents a batch of Y planes. The second element of array (pSrcBatchList[1]) represents a batch of Cb planes. The third element of array (pSrcBatchList[2]) represents a batch of Cr planes.**pDstBatchList**–[Destination-Batch-Images Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_batch_images_pointer).**nBatchSize**– Number of[NppiImageDescriptor](https://docs.nvidia.com/nppdefs.html#structnppiimagedescriptor)structures processed in this call (must be > 1).**oMaxSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification), must contain the maximum width and the maximum height from all destination ROIs used for processing data.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToBGR 709CSC[](https://docs.nvidia.com#ycbcr420tobgr-709csc)

YCbCr420_709CSC to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGR_709CSC_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGR_709CSC_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed BGR_709CSC color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr420ToBGR 709HDTV[](https://docs.nvidia.com#ycbcr420tobgr-709hdtv)

YCbCr420_709HDTV to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGR_709HDTV_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGR_709HDTV_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 4 channel 8-bit unsigned packed BGR_709HDTV color conversion with constant alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCrCb420[](https://docs.nvidia.com#bgrtoycrcb420)

BGR to YCrCb420 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCrCb420_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCrCb420_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCrCb420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCrCb420_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCrCb420_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCrCb420 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCbCr411[](https://docs.nvidia.com#bgrtoycbcr411)

BGR to YCbCr411 color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr411_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr411_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr411 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr411_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int rDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr411_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCbCr411 color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**rDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToYCbCr[](https://docs.nvidia.com#bgrtoycbcr)

BGR to YCbCr color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr_8u_AC4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr_8u_AC4P3R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 3 channel 8-bit unsigned planar YCbCr color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr_8u_AC4P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr_8u_AC4P4R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 4 channel 8-bit unsigned planar YCbCr color conversion.

images.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**– Destination-Planar-Image Line Step Array.**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToBGR[](https://docs.nvidia.com#ycbcr411tobgr)

YCbCr411 to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToBGR_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToBGR_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 4 channel 8-bit unsigned packed BGR color conversion with constant alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCbCr411ToRGB[](https://docs.nvidia.com#ycbcr411torgb)

YCbCr411 to RGB color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToRGB_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToRGB_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToRGB_8u_P3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int rSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nAval,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToRGB_8u_P3C4R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 4 channel 8-bit unsigned packed RGB color conversion with constant alpha.

- Parameters
-
**rSrcStep**–[Source-Planar-Image Line Step Array](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_planar_image_line_step_array).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nAval**– 8-bit unsigned alpha constant.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToXYZ[](https://docs.nvidia.com#rgbtoxyz)

RGB to XYZ color conversion.

Here is how NPP converts gamma corrected RGB or BGR to XYZ.

```
Npp32f nNormalizedR = (Npp32f)R * 0.003921569F; // / 255.0F
Npp32f nNormalizedG = (Npp32f)G * 0.003921569F;
Npp32f nNormalizedB = (Npp32f)B * 0.003921569F;
Npp32f nX = 0.412453F * nNormalizedR + 0.35758F * nNormalizedG + 0.180423F * nNormalizedB;
if (nX > 1.0F)
nX = 1.0F;
Npp32f nY = 0.212671F * nNormalizedR + 0.71516F * nNormalizedG + 0.072169F * nNormalizedB;
if (nY > 1.0F)
nY = 1.0F;
Npp32f nZ = 0.019334F * nNormalizedR + 0.119193F * nNormalizedG + 0.950227F * nNormalizedB;
if (nZ > 1.0F)
nZ = 1.0F;
X = (Npp8u)(nX * 255.0F);
Y = (Npp8u)(nY * 255.0F);
Z = (Npp8u)(nZ * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToXYZ_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToXYZ_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned packed XYZ color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToXYZ_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToXYZ_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned packed XYZ with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### XYZToRGB[](https://docs.nvidia.com#xyztorgb)

XYZ to RGB color conversion.

Here is how NPP converts XYZ to gamma corrected RGB or BGR. The code assumes that X,Y, and Z values are in the range [0..1].

```
Npp32f nNormalizedX = (Npp32f)X * 0.003921569F; // / 255.0F
Npp32f nNormalizedY = (Npp32f)Y * 0.003921569F;
Npp32f nNormalizedZ = (Npp32f)Z * 0.003921569F;
Npp32f nR = 3.240479F * nNormalizedX - 1.53715F * nNormalizedY - 0.498535F * nNormalizedZ;
if (nR > 1.0F)
nR = 1.0F;
Npp32f nG = -0.969256F * nNormalizedX + 1.875991F * nNormalizedY + 0.041556F * nNormalizedZ;
if (nG > 1.0F)
nG = 1.0F;
Npp32f nB = 0.055648F * nNormalizedX - 0.204043F * nNormalizedY + 1.057311F * nNormalizedZ;
if (nB > 1.0F)
nB = 1.0F;
R = (Npp8u)(nR * 255.0F);
G = (Npp8u)(nG * 255.0F);
B = (Npp8u)(nB * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiXYZToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiXYZToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed XYZ to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiXYZToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiXYZToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed XYZ with alpha to 4 channel 8-bit unsigned packed RGB with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToLUV[](https://docs.nvidia.com#rgbtoluv)

RGB to LUV color conversion.

Here is how NPP converts gamma corrected RGB or BGR to CIE LUV using the CIE XYZ D65 white point with a Y luminance of 1.0. The computed values of the L component are in the range [0..100], U component in the range [-134..220], and V component in the range [-140..122]. The code uses cbrtf() the 32 bit floating point cube root math function.

```
// use CIE D65 chromaticity coordinates
#define nCIE_XYZ_D65_xn 0.312713F
#define nCIE_XYZ_D65_yn 0.329016F
#define nn_DIVISOR (-2.0F * nCIE_XYZ_D65_xn + 12.0F * nCIE_XYZ_D65_yn + 3.0F)
#define nun (4.0F * nCIE_XYZ_D65_xn / nn_DIVISOR)
#define nvn (9.0F * nCIE_XYZ_D65_yn / nn_DIVISOR)
// First convert to XYZ
Npp32f nNormalizedR = (Npp32f)R * 0.003921569F; // / 255.0F
Npp32f nNormalizedG = (Npp32f)G * 0.003921569F;
Npp32f nNormalizedB = (Npp32f)B * 0.003921569F;
Npp32f nX = 0.412453F * nNormalizedR + 0.35758F * nNormalizedG + 0.180423F * nNormalizedB;
Npp32f nY = 0.212671F * nNormalizedR + 0.71516F * nNormalizedG + 0.072169F * nNormalizedB;
Npp32f nZ = 0.019334F * nNormalizedR + 0.119193F * nNormalizedG + 0.950227F * nNormalizedB;
// Now calculate LUV from the XYZ value
Npp32f nTemp = nX + 15.0F * nY + 3.0F * nZ;
Npp32f nu = 4.0F * nX / nTemp;
Npp32f nv = 9.0F * nY / nTemp;
Npp32f nL = 116.0F * cbrtf(nY) - 16.0F;
if (nL < 0.0F)
nL = 0.0F;
if (nL > 100.0F)
nL = 100.0F;
nTemp = 13.0F * nL;
Npp32f nU = nTemp * (nu - nun);
if (nU < -134.0F)
nU = -134.0F;
if (nU > 220.0F)
nU = 220.0F;
Npp32f nV = nTemp * (nv - nvn);
if (nV < -140.0F)
nV = -140.0F;
if (nV > 122.0F)
nV = 122.0F;
L = (Npp8u)(nL * 255.0F * 0.01F); // / 100.0F
U = (Npp8u)((nU + 134.0F) * 255.0F * 0.0028249F); // / 354.0F
V = (Npp8u)((nV + 140.0F) * 255.0F * 0.0038168F); // / 262.0F
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToLUV_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToLUV_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned packed LUV color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToLUV_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToLUV_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned packed LUV with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### LUVToRGB[](https://docs.nvidia.com#luvtorgb)

LUV to RGB color conversion.

Here is how NPP converts CIE LUV to gamma corrected RGB or BGR using the CIE XYZ D65 white point with a Y luminance of 1.0. The code uses powf() the 32 bit floating point power math function.

```
// use CIE D65 chromaticity coordinates
#define nCIE_XYZ_D65_xn 0.312713F
#define nCIE_XYZ_D65_yn 0.329016F
#define nn_DIVISOR (-2.0F * nCIE_XYZ_D65_xn + 12.0F * nCIE_XYZ_D65_yn + 3.0F)
#define nun (4.0F * nCIE_XYZ_D65_xn / nn_DIVISOR)
#define nvn (9.0F * nCIE_XYZ_D65_yn / nn_DIVISOR)
// First convert normalized LUV back to original CIE LUV range
Npp32f nL = (Npp32f)L * 100.0F * 0.003921569F; // / 255.0F
Npp32f nU = ((Npp32f)U * 354.0F * 0.003921569F) - 134.0F;
Npp32f nV = ((Npp32f)V * 262.0F * 0.003921569F) - 140.0F;
// Now convert LUV to CIE XYZ
Npp32f nTemp = 13.0F * nL;
Npp32f nu = nU / nTemp + nun;
Npp32f nv = nV / nTemp + nvn;
Npp32f nNormalizedY;
if (nL > 7.9996248F)
{
nNormalizedY = (nL + 16.0F) * 0.008621F; // / 116.0F
nNormalizedY = powf(nNormalizedY, 3.0F);
}
else
{
nNormalizedY = nL * 0.001107F; // / 903.3F
}
Npp32f nNormalizedX = (-9.0F * nNormalizedY * nu) / ((nu - 4.0F) * nv - nu * nv);
Npp32f nNormalizedZ = (9.0F * nNormalizedY - 15.0F * nv * nNormalizedY - nv * nNormalizedX) / (3.0F * nv);
Npp32f nR = 3.240479F * nNormalizedX - 1.53715F * nNormalizedY - 0.498535F * nNormalizedZ;
if (nR > 1.0F)
nR = 1.0F;
if (nR < 0.0F)
nR = 0.0F;
Npp32f nG = -0.969256F * nNormalizedX + 1.875991F * nNormalizedY + 0.041556F * nNormalizedZ;
if (nG > 1.0F)
nG = 1.0F;
if (nG < 0.0F)
nG = 0.0F;
Npp32f nB = 0.055648F * nNormalizedX - 0.204043F * nNormalizedY + 1.057311F * nNormalizedZ;
if (nB > 1.0F)
nB = 1.0F;
if (nB < 0.0F)
nB = 0.0F;
R = (Npp8u)(nR * 255.0F);
G = (Npp8u)(nG * 255.0F);
B = (Npp8u)(nB * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUVToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUVToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed LUV to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLUVToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLUVToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed LUV with alpha to 4 channel 8-bit unsigned packed RGB with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToLab[](https://docs.nvidia.com#bgrtolab)

BGR to Lab color conversion.

This is how NPP converts gamma corrected BGR or RGB to Lab using the CIE Lab D65 white point with a Y luminance of 1.0. The computed values of the L component are in the range [0..100], a and b component values are in the range [-128..127]. The code uses cbrtf() the 32 bit floating point cube root math function.

```
// use CIE Lab chromaticity coordinates
#define nCIE_LAB_D65_xn 0.950455F
#define nCIE_LAB_D65_yn 1.0F
#define nCIE_LAB_D65_zn 1.088753F
// First convert to XYZ
Npp32f nNormalizedR = (Npp32f)R * 0.003921569F; // / 255.0F
Npp32f nNormalizedG = (Npp32f)G * 0.003921569F;
Npp32f nNormalizedB = (Npp32f)B * 0.003921569F;
Npp32f nX = 0.412453F * nNormalizedR + 0.35758F * nNormalizedG + 0.180423F * nNormalizedB;
Npp32f nY = 0.212671F * nNormalizedR + 0.71516F * nNormalizedG + 0.072169F * nNormalizedB;
Npp32f nZ = 0.019334F * nNormalizedR + 0.119193F * nNormalizedG + 0.950227F * nNormalizedB;
Npp32f nL = cbrtf(nY);
Npp32f nA; Npp32f nB; Npp32f nfX = nX * 1.052128F; // / nCIE_LAB_D65_xn; Npp32f nfY = nY; Npp32f nfZ = nZ * 0.918482F; // /
nCIE_LAB_D65_zn; nfY = nL - 16.0F; nL = 116.0F * nL - 16.0F; nA = cbrtf(nfX) - 16.0F; nA = 500.0F
* (nA - nfY); nB = cbrtf(nfZ) - 16.0F; nB = 200.0F * (nfY - nB); // Now scale Lab range nL = nL * 255.0F
* 0.01F; // / 100.0F nA = nA + 128.0F; nB = nB + 128.0F; L = (Npp8u)nL; a = (Npp8u)nA; b = (Npp8u)nB;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToLab_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToLab_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned packed Lab color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### LabToBGR[](https://docs.nvidia.com#labtobgr)

Lab to BGR color conversion.

This is how NPP converts Lab to gamma corrected BGR or RGB using the CIE Lab D65 white point with a Y luminance of 1.0. The code uses powf() the 32 bit floating point power math function.

```
// use CIE Lab chromaticity coordinates
#define nCIE_LAB_D65_xn 0.950455F
#define nCIE_LAB_D65_yn 1.0F
#define nCIE_LAB_D65_zn 1.088753F
// First convert Lab back to original range then to CIE XYZ
Npp32f nL = (Npp32f)L * 100.0F * 0.003921569F; // / 255.0F
Npp32f nA = (Npp32f)a - 128.0F;
Npp32f nB = (Npp32f)b - 128.0F;
Npp32f nP = (nL + 16.0F) * 0.008621F; // / 116.0F
Npp32f nNormalizedY = nP * nP * nP; // powf(nP, 3.0F);
Npp32f nNormalizedX = nCIE_LAB_D65_xn * powf((nP + nA * 0.002F), 3.0F); // / 500.0F
Npp32f nNormalizedZ = nCIE_LAB_D65_zn * powf((nP - nB * 0.005F), 3.0F); // / 200.0F
Npp32f nR = 3.240479F * nNormalizedX - 1.53715F * nNormalizedY - 0.498535F * nNormalizedZ;
if (nR > 1.0F)
nR = 1.0F;
Npp32f nG = -0.969256F * nNormalizedX + 1.875991F * nNormalizedY + 0.041556F * nNormalizedZ;
if (nG > 1.0F)
nG = 1.0F;
nB = 0.055648F * nNormalizedX - 0.204043F * nNormalizedY + 1.057311F * nNormalizedZ;
if (nB > 1.0F)
nB = 1.0F;
R = (Npp8u)(nR * 255.0F);
G = (Npp8u)(nG * 255.0F);
B = (Npp8u)(nB * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiLabToBGR_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiLabToBGR_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed Lab to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToYCC[](https://docs.nvidia.com#rgbtoycc)

RGB to PhotoYCC color conversion.

This is how NPP converts gamma corrected BGR or RGB to PhotoYCC. The computed Y, C1, C2 values are then quantized and converted to fit in the range [0..1] before expanding to 8 bits.

```
Npp32f nNormalizedR = (Npp32f)R * 0.003921569F; // / 255.0F
Npp32f nNormalizedG = (Npp32f)G * 0.003921569F;
Npp32f nNormalizedB = (Npp32f)B * 0.003921569F;
Npp32f nY = 0.299F * nNormalizedR + 0.587F * nNormalizedG + 0.114F * nNormalizedB;
Npp32f nC1 = nNormalizedB - nY;
nC1 = 111.4F * 0.003921569F * nC1 + 156.0F * 0.003921569F;
Npp32f nC2 = nNormalizedR - nY;
nC2 = 135.64F * 0.003921569F * nC2 + 137.0F * 0.003921569F;
nY = 1.0F * 0.713267F * nY; // / 1.402F
Y = (Npp8u)(nY * 255.0F);
C1 = (Npp8u)(nC1 * 255.0F);
C2 = (Npp8u)(nC2 * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCC_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCC_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned packed YCC color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCC_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCC_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned packed YCC with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCCToRGB[](https://docs.nvidia.com#ycctorgb)

PhotoYCC to RGB color conversion.

This is how NPP converts PhotoYCC to gamma corrected RGB or BGR.

```
Npp32f nNormalizedY = ((Npp32f)Y * 0.003921569F) * 1.3584F; // / 255.0F
Npp32f nNormalizedC1 = (((Npp32f)C1 * 0.003921569F) - 156.0F * 0.003921569F) * 2.2179F;
Npp32f nNormalizedC2 = (((Npp32f)C2 * 0.003921569F) - 137.0F * 0.003921569F) * 1.8215F;
Npp32f nR = nNormalizedY + nNormalizedC2;
if (nR > 1.0F)
nR = 1.0F;
Npp32f nG = nNormalizedY - 0.194F * nNormalizedC1 - 0.509F * nNormalizedC2;
if (nG > 1.0F)
nG = 1.0F;
Npp32f nB = nNormalizedY + nNormalizedC1;
if (nB > 1.0F)
nB = 1.0F;
R = (Npp8u)(nR * 255.0F);
G = (Npp8u)(nG * 255.0F);
B = (Npp8u)(nB * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCCToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCCToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed YCC to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCCToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCCToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed YCC with alpha to 4 channel 8-bit unsigned packed RGB with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCCKToCMYK_JPEG[](https://docs.nvidia.com#yccktocmyk-jpeg)

This function partially converts JPEG YCCK to CMYK.

This is how NPP converts JPEG YCCK to CMYK. NPP only performs and initial YCC to RGB conversion using the 601 conversion coefficients and the RGB to CMY inversion leaving K unmodified. To complete this conversion to useful RGB values an additional RGB conversion needs to follow this function using the color profile contained in the YCCK JPEG file metadata section. NPP does not directly support this conversion but potentially nppiColorTwist can be used to perform it once the conversion coefficients are known.

```
Npp32f nY = static_cast<Npp32f>(Y);
Npp32f nC1 = static_cast<Npp32f>(Cb);
Npp32f nC2 = static_cast<Npp32f>(Cr);
Npp32f nR = nY + 1.402F * nC2 - 179.456F;
Npp32f nG = nY - 0.34414F * nC1 - 0.71414F * nC2 + 135.45984F;
Npp32f nB = nY + 1.772F * nC1 - 226.816F;
Npp8u nC = static_cast<Npp8u>(255.0F - nR);
Npp8u nM = static_cast<Npp8u>(255.0F - nG);
Npp8u nM = static_cast<Npp8u>(255.0F - nB);
Npp8u nK = K;
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCCKToCMYK_JPEG_601_8u_P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCCKToCMYK_JPEG_601_8u_P4R_Ctx)

-
4 channel 8-bit unsigned planar JPEG YCCK color format to 4 channel 8-bit unsigned planar CMYK color conversion using 601 RGB color coefficients and CMY inversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### CMYKOrYCCKJPEGToRGB[](https://docs.nvidia.com#cmykorycckjpegtorgb)

These functions convert JPEG CMYK or YCCK color format images to either planar or packed RGB images for images which need no color profile conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCMYKOrYCCKToRGB_JPEG_8u_P4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCMYKOrYCCKToRGB_JPEG_8u_P4P3R_Ctx)

-
4 channel 8-bit unsigned planar JPEG CMYK or YCCK color model image to 3 channel 8-bit unsigned planar RGB color model image without color profile conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCMYKOrYCCKToRGB_JPEG_8u_P4C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCMYKOrYCCKToRGB_JPEG_8u_P4C3R_Ctx)

-
4 channel 8-bit unsigned planar JPEG CMYK or YCCK color model image to 3 channel 8-bit unsigned packed RGB color model image without color profile conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### YCCKJPEGOrCMYKToBGR[](https://docs.nvidia.com#ycckjpegorcmyktobgr)

These functions convert JPEG CMYK or YCCK color format images to either planar or packed BGR images for images which need no color profile conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCMYKOrYCCKToBGR_JPEG_8u_P4P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCMYKOrYCCKToBGR_JPEG_8u_P4P3R_Ctx)

-
4 channel 8-bit unsigned planar JPEG CMYK or YCCK color model image to 3 channel 8-bit unsigned planar BGR color model image without color profile conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCMYKOrYCCKToBGR_JPEG_8u_P4C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCMYKOrYCCKToBGR_JPEG_8u_P4C3R_Ctx)

-
4 channel 8-bit unsigned planar JPEG CMYK or YCCK color model image to 3 channel 8-bit unsigned packed BGR color model image without color profile conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RGBToHLS[](https://docs.nvidia.com#rgbtohls)

RGB to HLS color conversion.

This is how NPP converts gamma corrected RGB or BGR to HLS. This code uses the fmaxf() and fminf() 32 bit floating point math functions.

```
Npp32f nNormalizedR = (Npp32f)R * 0.003921569F; // / 255.0F
Npp32f nNormalizedG = (Npp32f)G * 0.003921569F;
Npp32f nNormalizedB = (Npp32f)B * 0.003921569F;
Npp32f nS;
Npp32f nH;
// Lightness
Npp32f nMax = fmaxf(nNormalizedR, nNormalizedG);
nMax = fmaxf(nMax, nNormalizedB);
Npp32f nMin = fminf(nNormalizedR, nNormalizedG);
nMin = fminf(nMin, nNormalizedB);
Npp32f nL = (nMax + nMin) * 0.5F;
Npp32f nDivisor = nMax - nMin;
// Saturation
if (nDivisor == 0.0F) // achromatics case
{
nS = 0.0F;
nH = 0.0F;
}
else // chromatics case
{
if (nL > 0.5F)
nS = nDivisor / (1.0F - (nMax + nMin - 1.0F));
else
nS = nDivisor / (nMax + nMin);
}
// Hue
Npp32f nCr = (nMax - nNormalizedR) / nDivisor;
Npp32f nCg = (nMax - nNormalizedG) / nDivisor;
Npp32f nCb = (nMax - nNormalizedB) / nDivisor;
if (nNormalizedR == nMax)
nH = nCb - nCg;
else if (nNormalizedG == nMax)
nH = 2.0F + nCr - nCb;
else if (nNormalizedB == nMax)
nH = 4.0F + nCg - nCr;
nH = nH * 0.166667F; // / 6.0F
if (nH < 0.0F)
nH = nH + 1.0F;
H = (Npp8u)(nH * 255.0F);
L = (Npp8u)(nL * 255.0F);
S = (Npp8u)(nS * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToHLS_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToHLS_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned packed HLS color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToHLS_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToHLS_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned packed HLS with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### HLSToRGB[](https://docs.nvidia.com#hlstorgb)

HLS to RGB color conversion.

This is how NPP converts HLS to gamma corrected RGB or BGR.

```
Npp32f nNormalizedH = (Npp32f)H * 0.003921569F; // / 255.0F
Npp32f nNormalizedL = (Npp32f)L * 0.003921569F;
Npp32f nNormalizedS = (Npp32f)S * 0.003921569F;
Npp32f nM1;
Npp32f nM2;
Npp32f nR;
Npp32f nG;
Npp32f nB;
Npp32f nh = 0.0F;
if (nNormalizedL <= 0.5F)
nM2 = nNormalizedL * (1.0F + nNormalizedS);
else
nM2 = nNormalizedL + nNormalizedS - nNormalizedL * nNormalizedS;
nM1 = 2.0F * nNormalizedL - nM2;
if (nNormalizedS == 0.0F)
nR = nG = nB = nNormalizedL;
else
{
nh = nNormalizedH + 0.3333F;
if (nh > 1.0F)
nh -= 1.0F;
}
Npp32f nMDiff = nM2 - nM1;
if (0.6667F < nh)
nR = nM1;
else
{
if (nh < 0.1667F)
nR = (nM1 + nMDiff * nh * 6.0F); // / 0.1667F
else if (nh < 0.5F)
nR = nM2;
else
nR = nM1 + nMDiff * ( 0.6667F - nh ) * 6.0F; // / 0.1667F
}
if (nR > 1.0F)
nR = 1.0F;
nh = nNormalizedH;
if (0.6667F < nh)
nG = nM1;
else
{
if (nh < 0.1667F)
nG = (nM1 + nMDiff * nh * 6.0F); // / 0.1667F
else if (nh < 0.5F)
nG = nM2;
else
nG = nM1 + nMDiff * (0.6667F - nh ) * 6.0F; // / 0.1667F
}
if (nG > 1.0F)
nG = 1.0F;
nh = nNormalizedH - 0.3333F;
if (nh < 0.0F)
nh += 1.0F;
if (0.6667F < nh)
nB = nM1;
else
{
if (nh < 0.1667F)
nB = (nM1 + nMDiff * nh * 6.0F); // / 0.1667F
else if (nh < 0.5F)
nB = nM2;
else
nB = nM1 + nMDiff * (0.6667F - nh ) * 6.0F; // / 0.1667F
}
if (nB > 1.0F)
nB = 1.0F;
R = (Npp8u)(nR * 255.0F);
G = (Npp8u)(nG * 255.0F);
B = (Npp8u)(nB * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed HLS to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed HLS with alpha to 4 channel 8-bit unsigned packed RGB with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### BGRToHLS[](https://docs.nvidia.com#bgrtohls)

BGR to HLS color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 4 channel 8-bit unsigned packed HLS with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar HLS color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_AC4P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_AC4P4R_Ctx)

-
4 channel 8-bit unsigned packed BGR with alpha to 4 channel 8-bit unsigned planar HLS with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned packed HLS color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_AP4C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_AP4C4R_Ctx)

-
4 channel 8-bit unsigned planar BGR with alpha to 4 channel 8-bit unsigned packed HLS with alpha color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned planar HLS color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToHLS_8u_AP4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToHLS_8u_AP4R_Ctx)

-
4 channel 8-bit unsigned planar BGR with alpha to 4 channel 8-bit unsigned planar HLS with alpha color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### HLSToBGR[](https://docs.nvidia.com#hlstobgr)

HLS to BGR color conversion.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToBGR_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToBGR_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed HLS to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToBGR_8u_AC4P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToBGR_8u_AC4P4R_Ctx)

-
4 channel 8-bit unsigned packed HLS with alpha to 4 channel 8-bit unsigned planar BGR with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToBGR_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToBGR_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar HLS to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToBGR_8u_AP4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToBGR_8u_AP4R_Ctx)

-
4 channel 8-bit unsigned planar HLS with alpha to 4 channel 8-bit unsigned planar BGR with alpha color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToBGR_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToBGR_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar HLS to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHLSToBGR_8u_AP4C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHLSToBGR_8u_AP4C4R_Ctx)

-
4 channel 8-bit unsigned planar HLS with alpha to 4 channel 8-bit unsigned packed BGR with alpha color conversion.

- Parameters
-
**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### RBGToHSV[](https://docs.nvidia.com#rbgtohsv)

RGB to HSV color conversion.

This is how NPP converts gamma corrected RGB or BGR to HSV. This code uses the fmaxf() and fminf() 32 bit floating point math functions.

```
Npp32f nNormalizedR = (Npp32f)R * 0.003921569F; // / 255.0F
Npp32f nNormalizedG = (Npp32f)G * 0.003921569F;
Npp32f nNormalizedB = (Npp32f)B * 0.003921569F;
Npp32f nS;
Npp32f nH;
// Value
Npp32f nV = fmaxf(nNormalizedR, nNormalizedG);
nV = fmaxf(nV, nNormalizedB);
// Saturation
Npp32f nTemp = fminf(nNormalizedR, nNormalizedG);
nTemp = fminf(nTemp, nNormalizedB);
Npp32f nDivisor = nV - nTemp;
if (nV == 0.0F) // achromatics case
{
nS = 0.0F;
nH = 0.0F;
}
else // chromatics case
nS = nDivisor / nV;
// Hue:
Npp32f nCr = (nV - nNormalizedR) / nDivisor;
Npp32f nCg = (nV - nNormalizedG) / nDivisor;
Npp32f nCb = (nV - nNormalizedB) / nDivisor;
if (nNormalizedR == nV)
nH = nCb - nCg;
else if (nNormalizedG == nV)
nH = 2.0F + nCr - nCb;
else if (nNormalizedB == nV)
nH = 4.0F + nCg - nCr;
nH = nH * 0.166667F; // / 6.0F
if (nH < 0.0F)
nH = nH + 1.0F;
H = (Npp8u)(nH * 255.0F);
S = (Npp8u)(nS * 255.0F);
V = (Npp8u)(nV * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToHSV_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToHSV_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned packed HSV color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToHSV_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToHSV_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed RGB with alpha to 4 channel 8-bit unsigned packed HSV with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### HSVToRGB[](https://docs.nvidia.com#hsvtorgb)

HSV to RGB color conversion.

This is how NPP converts HSV to gamma corrected RGB or BGR. This code uses the floorf() 32 bit floating point math function.

```
Npp32f nNormalizedH = (Npp32f)H * 0.003921569F; // / 255.0F
Npp32f nNormalizedS = (Npp32f)S * 0.003921569F;
Npp32f nNormalizedV = (Npp32f)V * 0.003921569F;
Npp32f nR;
Npp32f nG;
Npp32f nB;
if (nNormalizedS == 0.0F)
{
nR = nG = nB = nNormalizedV;
}
else
{
if (nNormalizedH == 1.0F)
nNormalizedH = 0.0F;
else
nNormalizedH = nNormalizedH * 6.0F; // / 0.1667F
}
Npp32f nI = floorf(nNormalizedH);
Npp32f nF = nNormalizedH - nI;
Npp32f nM = nNormalizedV * (1.0F - nNormalizedS);
Npp32f nN = nNormalizedV * (1.0F - nNormalizedS * nF);
Npp32f nK = nNormalizedV * (1.0F - nNormalizedS * (1.0F - nF));
if (nI == 0.0F)
{ nR = nNormalizedV; nG = nK; nB = nM; }
else if (nI == 1.0F)
{ nR = nN; nG = nNormalizedV; nB = nM; }
else if (nI == 2.0F)
{ nR = nM; nG = nNormalizedV; nB = nK; }
else if (nI == 3.0F)
{ nR = nM; nG = nN; nB = nNormalizedV; }
else if (nI == 4.0F)
{ nR = nK; nG = nM; nB = nNormalizedV; }
else if (nI == 5.0F)
{ nR = nNormalizedV; nG = nM; nB = nN; }
R = (Npp8u)(nR * 255.0F);
G = (Npp8u)(nG * 255.0F);
B = (Npp8u)(nB * 255.0F);
```

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHSVToRGB_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHSVToRGB_8u_C3R_Ctx)

-
3 channel 8-bit unsigned packed HSV to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiHSVToRGB_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiHSVToRGB_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned packed HSV with alpha to 4 channel 8-bit unsigned packed RGB with alpha color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


### JPEG Color Conversion[](https://docs.nvidia.com#jpeg-color-conversion)

The set of JPEG color conversion functions available in the library.

RGBToYCbCr_JPEG Planar to planar.

JPEG RGB to YCbCr color conversion.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr420_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr420_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr422_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr422_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YCbCr422 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr411_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr411_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YCbCr411 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr444_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr444_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar RGB to 3 channel 8-bit unsigned planar YCbCr444 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr422_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr422_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned planar YCbCr422 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr411_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr411_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned planar YCbCr411 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr444_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr444_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar BGR to 3 channel 8-bit unsigned planar YCbCr444 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToRGB_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToRGB_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGB_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGB_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToRGB_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToRGB_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr444ToRGB_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr444ToRGB_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr444 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGR_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGR_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGR_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGR_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToBGR_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToBGR_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr444ToBGR_JPEG_8u_P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr444ToBGR_JPEG_8u_P3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr444 to 3 channel 8-bit unsigned planar BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


RGBToYCbCr_JPEG Planar to packed.

JPEG RGB to YCbCr color conversion.

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr420_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr420_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr422_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr422_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YCbCr422 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr411_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr411_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YCbCr411 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiRGBToYCbCr444_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiRGBToYCbCr444_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed RGB to 3 channel 8-bit unsigned planar YCbCr444 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr420_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr420_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr420 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr422_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr422_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr422 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr411_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int aDstStep[3],[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr411_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr411 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**aDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiBGRToYCbCr444_JPEG_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiBGRToYCbCr444_JPEG_8u_C3P3R_Ctx)

-
3 channel 8-bit unsigned packed BGR to 3 channel 8-bit unsigned planar YCbCr444 color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToRGB_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToRGB_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned packed YCbCr420 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToRGB_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToRGB_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned packed YCbCr422 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToRGB_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToRGB_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned packed YCbCr411 to 3 channel 8-bit unsigned planar RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr444ToRGB_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr444ToRGB_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr444 to 3 channel 8-bit unsigned packed RGB color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr420ToBGR_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr420ToBGR_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr420 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr422ToBGR_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr422ToBGR_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr422 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr411ToBGR_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int aSrcStep[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr411ToBGR_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr411 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**aSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiYCbCr444ToBGR_JPEG_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const pSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiYCbCr444ToBGR_JPEG_8u_P3C3R_Ctx)

-
3 channel 8-bit unsigned planar YCbCr444 to 3 channel 8-bit unsigned packed BGR color conversion.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns