source: https://docs.nvidia.com/cuda/npp/image_linear_transforms.html

# Image Linear Transforms Functions[](https://docs.nvidia.com#image-linear-transforms-functions)

Linear image transformations.

These functions can be found in the nppist library. Linking to only the sub-libraries that you use can significantly save link time, application load time, and CUDA runtime startup time when using dynamic libraries.

## Fourier Transforms[](https://docs.nvidia.com#group__image__fourier__transforms_1image_fourier_transforms)

The set of Fourier transform functions available in the library.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMagnitude_32fc32f_C1R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMagnitude_32fc32f_C1R_Ctx)

-
32-bit floating point complex to 32-bit floating point magnitude.

Converts complex-number pixel image to single channel image computing the result pixels as the magnitude of the complex values.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context)

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMagnitudeSqr_32fc32f_C1R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMagnitudeSqr_32fc32f_C1R_Ctx)

-
32-bit floating point complex to 32-bit floating point squared magnitude.

Converts complex-number pixel image to single channel image computing the result pixels as the squared magnitude of the complex values.

The squared magnitude is an itermediate result of magnitude computation and can thus be computed faster than actual magnitude. If magnitudes are required for sorting/comparing only, using this function instead of nppiMagnitude_32fc32f_C1R can be a worthwhile performance optimization.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context)

- Returns