source: https://docs.nvidia.com/cuda/npp/image_morphological_operations.html

# Image Morphological Operations[](https://docs.nvidia.com#image-morphological-operations)

Morphological image operations.

Morphological operations are classified as [Neighborhood Operations](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1neighborhood_operations).

These functions can be found in the nppim library. Linking to only the sub-libraries that you use can significantly save link time, application load time, and CUDA runtime startup time when using dynamic libraries.

## Dilation Functions[](https://docs.nvidia.com#dilation-functions)

### Image Dilate[](https://docs.nvidia.com#image-dilate)

#### Dilation[](https://docs.nvidia.com#group__image__dilate_1image_dilate)

Dilation computes the output pixel as the maximum pixel value of the pixels under the mask. Pixels who’s corresponding mask values are zero do not participate in the maximum search.

It is the user’s responsibility to avoid [Sampling Beyond Image Boundaries](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1sampling_beyond_image_boundaries).

##### Common parameters for nppiDilate functions:[](https://docs.nvidia.com#group__image__dilate_1CommonDilateParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer dilation, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer dilation, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point dilation, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate functions:](https://docs.nvidia.com#group__image__dilate_1commondilateparameters).

### Image Dilate Border[](https://docs.nvidia.com#image-dilate-border)

#### Dilation with border control[](https://docs.nvidia.com#group__image__dilate__border_1image_dilate_border)

Dilation computes the output pixel as the maximum pixel value of the pixels under the mask. Pixels who’s corresponding mask values are zero do not participate in the maximum search. For gray scale dilation the mask contains signed mask values which are added to the corresponding source image sample value before determining the maximum value after clamping.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiDilateBorder functions:[](https://docs.nvidia.com#group__image__dilate__border_1CommonDilateBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer dilation with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer dilation with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilateBorder_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilateBorder_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point dilation with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGrayDilateBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGrayDilateBorder_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer gray scale dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGrayDilateBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGrayDilateBorder_32f_C1R_Ctx)

-
Single-channel 32-bit floating point gray scale dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilateBorder functions:](https://docs.nvidia.com#group__image__dilate__border_1commondilateborderparameters).

### Image Dilate 3x3[](https://docs.nvidia.com#image-dilate-3x3)

#### Dilate3x3[](https://docs.nvidia.com#group__image__dilate__3x3_1image_dilate_3x3)

Dilation using a 3x3 mask with the anchor at its center pixel.

It is the user’s responsibility to avoid [Sampling Beyond Image Boundaries](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1sampling_beyond_image_boundaries).

##### Common parameters for nppiDilate3x3 functions:[](https://docs.nvidia.com#group__image__dilate__3x3_1CommonDilate3x3Parameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 dilation, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 dilation, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 dilation, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3_64f_C1R_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3_64f_C1R_Ctx)

-
Single-channel 64-bit floating-point 3x3 dilation.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3 functions:](https://docs.nvidia.com#group__image__dilate__3x3_1commondilate3x3parameters).

### Image Dilate 3x3 Border[](https://docs.nvidia.com#image-dilate-3x3-border)

#### Dilate3x3Border[](https://docs.nvidia.com#group__image__dilate__3x3__border_1image_dilate_3x3_border)

Dilation using a 3x3 mask with the anchor at its center pixel with border control.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiDilate3x3Border functions:[](https://docs.nvidia.com#group__image__dilate__3x3__border_1CommonDilate3x3BorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 dilation with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer 3x3 dilation with border control.


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 dilation with border control.


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 dilation with border control, ignoring alpha-channel.


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 dilation with border control.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDilate3x3Border_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDilate3x3Border_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 dilation with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiDilate3x3Border functions:](https://docs.nvidia.com#group__image__dilate__3x3__border_1commondilate3x3borderparameters).

## Erosion Functions[](https://docs.nvidia.com#erosion-functions)

### Image Erode[](https://docs.nvidia.com#image-erode)

#### Erode[](https://docs.nvidia.com#group__image__erode_1image_erode)

Erosion computes the output pixel as the minimum pixel value of the pixels under the mask. Pixels who’s corresponding mask values are zero do not participate in the maximum search.

It is the user’s responsibility to avoid [Sampling Beyond Image Boundaries](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1sampling_beyond_image_boundaries).

##### Common parameters for nppiErode functions:[](https://docs.nvidia.com#group__image__erode_1CommonErodeParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer erosion, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer erosion.


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer erosion, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point erosion.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point erosion, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode functions:](https://docs.nvidia.com#group__image__erode_1commonerodeparameters).

### Image Erode Border[](https://docs.nvidia.com#image-erode-border)

#### Erosion with border control[](https://docs.nvidia.com#group__image__erode__border_1image_erode_border)

Erosion computes the output pixel as the minimum pixel value of the pixels under the mask. Pixels who’s corresponding mask values are zero do not participate in the minimum search. For gray scale erosion the mask contains signed mask values which are added to the corresponding source image sample value before determining the minimum value after clamping.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiErodeBorder functions:[](https://docs.nvidia.com#group__image__erode__border_1CommonErodeBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer erosion with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer erosion with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErodeBorder_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErodeBorder_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point erosion with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGrayErodeBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGrayErodeBorder_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer gray scale erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiGrayErodeBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiGrayErodeBorder_32f_C1R_Ctx)

-
Single-channel 32-bit floating point gray scale erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErodeBorder functions:](https://docs.nvidia.com#group__image__erode__border_1commonerodeborderparameters).

### Image Erode 3x3[](https://docs.nvidia.com#image-erode-3x3)

#### Erode3x3[](https://docs.nvidia.com#group__image__erode__3x3_1image_erode_3x3)

Erosion using a 3x3 mask with the anchor at its center pixel.

It is the user’s responsibility to avoid [Sampling Beyond Image Boundaries](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1sampling_beyond_image_boundaries).

##### Common parameters for nppiErode3x3 functions:[](https://docs.nvidia.com#group__image__erode__3x3_1CommonErode3x3Parameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 erosion, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 erosion, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 erosion, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3_64f_C1R_Ctx(const[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[Npp64f](https://docs.nvidia.com/nppdefs.html#c.Npp64f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3_64f_C1R_Ctx)

-
Single-channel 64-bit floating-point 3x3 erosion.

For common parameter descriptions, see

[Common parameters for nppiErode3x3 functions:](https://docs.nvidia.com#group__image__erode__3x3_1commonerode3x3parameters).

### Image Erode 3x3 Border[](https://docs.nvidia.com#image-erode-3x3-border)

#### Erode3x3Border[](https://docs.nvidia.com#group__image__erode__3x3__border_1image_erode_3x3_border)

Erosion using a 3x3 mask with the anchor at its center pixel with border control.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiErode3x3Border functions:[](https://docs.nvidia.com#group__image__erode__3x3__border_1CommonErode3x3BorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_8u_C1R_Ctx)

-
Single-channel 8-bit unsigned integer 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_8u_C3R_Ctx)

-
Three-channel 8-bit unsigned integer 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_8u_C4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_8u_AC4R_Ctx)

-
Four-channel 8-bit unsigned integer 3x3 erosion with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_16u_C1R_Ctx)

-
Single-channel 16-bit unsigned integer 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_16u_C3R_Ctx)

-
Three-channel 16-bit unsigned integer 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_16u_C4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_16u_AC4R_Ctx)

-
Four-channel 16-bit unsigned integer 3x3 erosion with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_32f_C1R_Ctx)

-
Single-channel 32-bit floating-point 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_32f_C3R_Ctx)

-
Three-channel 32-bit floating-point 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_32f_C4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 erosion with border control.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiErode3x3Border_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiErode3x3Border_32f_AC4R_Ctx)

-
Four-channel 32-bit floating-point 3x3 erosion with border control, ignoring alpha-channel.

For common parameter descriptions, see

[Common parameters for nppiErode3x3Border functions:](https://docs.nvidia.com#group__image__erode__3x3__border_1commonerode3x3borderparameters).

## Image Complex Morphphological Operations[](https://docs.nvidia.com#image-complex-morphphological-operations)

### Image Morph[](https://docs.nvidia.com#image-morph)

#### ComplexImageMorphology[](https://docs.nvidia.com#group__image__morph_1image_morph)

Complex image morphological operations.

### Image Morph Get Buffer Size[](https://docs.nvidia.com#image-morph-get-buffer-size)

#### MorphGetBufferSize[](https://docs.nvidia.com#group__image__morph__get__buffer__size_1image_morph_get_buffer_size)

Before calling any of the MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder functions the application first needs to call the corresponding MorphGetBufferSize to determine the amount of device memory to allocate as a working buffer. The application allocated device memory is then passed as the pBuffer parameter to the corresponding MorphXXXBorder function.

##### Common parameters for nppiMorphGetBufferSize functions:[](https://docs.nvidia.com#group__image__morph__get__buffer__size_1CommonMorphGetBufferSizeParameters)

- param oSizeROI
- param hpBufferSize
-
Required buffer size in bytes.


Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_8u_C1R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_8u_C1R)

-
Calculate scratch buffer size needed for 1 channel 8-bit unsigned integer MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_8u_C3R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_8u_C3R)

-
Calculate scratch buffer size needed for 3 channel 8-bit unsigned integer MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_8u_C4R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_8u_C4R)

-
Calculate scratch buffer size needed for 4 channel 8-bit unsigned integer MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_16u_C1R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_16u_C1R)

-
Calculate scratch buffer size needed for 1 channel 16-bit unsigned integer MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_16s_C1R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_16s_C1R)

-
Calculate scratch buffer size needed for 1 channel 16-bit signed integer MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_32f_C1R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_32f_C1R)

-
Calculate scratch buffer size needed for 1 channel 32-bit floating point MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_32f_C3R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_32f_C3R)

-
Calculate scratch buffer size needed for 3 channel 32-bit floating point MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGetBufferSize_32f_C4R([NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, int *hpBufferSize)[](https://docs.nvidia.com#c.nppiMorphGetBufferSize_32f_C4R)

-
Calculate scratch buffer size needed for 4 channel 32-bit floating point MorphCloseBorder, MorphOpenBorder, MorphTopHatBorder, MorphBlackHatBorder, or MorphGradientBorder function based on destination image oSizeROI width and height.

For common parameter descriptions, see

[Common parameters for nppiMorphGetBufferSize functions:](https://docs.nvidia.com#group__image__morph__get__buffer__size_1commonmorphgetbuffersizeparameters).

### Image Morph Close Border[](https://docs.nvidia.com#image-morph-close-border)

#### MorphCloseBorder[](https://docs.nvidia.com#group__image__morph__close__border_1image_morph_close_border)

Dilation followed by Erosion with border control.

Morphological close computes the output pixel as the maximum pixel value of the pixels under the mask followed by a second pass using the result of the first pass as input which outputs the minimum pixel value of the pixels under the same mask. Pixels who’s corresponding mask values are zero do not participate in the maximum or minimum search.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image. The mask is centered over the source image pixel being tested.

Before calling any of the MorphCloseBorder functions the application first needs to call the corresponding MorphGetBufferSize to determine the amount of device memory to allocate as a working buffer. The allocated device memory is then passed as the pBuffer parameter to the corresponding MorphCloseBorder function.

Use the oSrcOffset and oSrcSize parameters to control where the border control operation is applied to the source image ROI borders.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiMorphCloseBorder functions:[](https://docs.nvidia.com#group__image__morph__close__border_1CommonMorphCloseBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param pBuffer
-
Pointer to device memory scratch buffer at least as large as value returned by the corresponding MorphGetBufferSize call.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphCloseBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphCloseBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point morphological close with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphCloseBorder functions:](https://docs.nvidia.com#group__image__morph__close__border_1commonmorphcloseborderparameters).

### Image Morph Open Border[](https://docs.nvidia.com#image-morph-open-border)

#### MorphOpenBorder[](https://docs.nvidia.com#group__image__morph__open__border_1image_morph_open_border)

Erosion followed by Dilation with border control.

Morphological open computes the output pixel as the minimum pixel value of the pixels under the mask followed by a second pass using the result of the first pass as input which outputs the maximum pixel value of the pixels under the same mask. Pixels who’s corresponding mask values are zero do not participate in the minimum or maximum search.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image. The mask is centered over the source image pixel being tested.

Before calling any of the MorphOpenBorder functions the application first needs to call the corresponding MorphGetBufferSize to determine the amount of device memory to allocate as a working buffer. The allocated device memory is then passed as the pBuffer parameter to the corresponding MorphOpenBorder function.

Use the oSrcOffset and oSrcSize parameters to control where the border control operation is applied to the source image ROI borders.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiMorphOpenBorder functions:[](https://docs.nvidia.com#group__image__morph__open__border_1CommonMorphOpenBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param pBuffer
-
Pointer to device memory scratch buffer at least as large as value returned by the corresponding MorphGetBufferSize call.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphOpenBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphOpenBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point morphological open with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphOpenBorder functions:](https://docs.nvidia.com#group__image__morph__open__border_1commonmorphopenborderparameters).

### Image Morph Top Hat Border[](https://docs.nvidia.com#image-morph-top-hat-border)

#### MorphToHatBorder[](https://docs.nvidia.com#group__image__morph__top__hat__border_1image_morph_top_hat_border)

Source pixel minus the morphological open pixel result with border control.

Morphological top hat computes the output pixel as the source pixel minus the morphological open result of the pixels under the mask. Pixels who’s corresponding mask values are zero do not participate in the maximum or minimum search.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image. The mask is centered over the source image pixel being tested.

Before calling any of the MorphTopHatBorder functions the application first needs to call the corresponding MorphGetBufferSize to determine the amount of device memory to allocate as a working buffer. The allocated device memory is then passed as the pBuffer parameter to the corresponding MorphTopHatBorder function.

Use the oSrcOffset and oSrcSize parameters to control where the border control operation is applied to the source image ROI borders.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiMorphTopHatBorder functions:[](https://docs.nvidia.com#group__image__morph__top__hat__border_1CommonMorphTopHatBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param pBuffer
-
Pointer to device memory scratch buffer at least as large as value returned by the corresponding MorphGetBufferSize call.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphTopHatBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphTopHatBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point morphological top hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphTopHatBorder functions:](https://docs.nvidia.com#group__image__morph__top__hat__border_1commonmorphtophatborderparameters).

### Image Morph Black Hat Border[](https://docs.nvidia.com#image-morph-black-hat-border)

#### MorphBlackHatBorder[](https://docs.nvidia.com#group__image__morph__black__hat__border_1image_morph_black_hat_border)

Morphological close pixel result minus source pixel with border control.

Morphological black hat computes the output pixel as the morphological close pixel value of the pixels under the mask minus the source pixel value. Pixels who’s corresponding mask values are zero do not participate in the maximum or minimum search.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image. The mask is centered over the source image pixel being tested.

Before calling any of the MorphBlackHatBorder functions the application first needs to call the corresponding MorphGetBufferSize to determine the amount of device memory to allocate as a working buffer. The allocated device memory is then passed as the pBuffer parameter to the corresponding MorphBlackHatBorder function.

Use the oSrcOffset and oSrcSize parameters to control where the border control operation is applied to the source image ROI borders.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiMorphBlackHatBorder functions:[](https://docs.nvidia.com#group__image__morph__black__hat__border_1CommonMorphBlackHatBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param pBuffer
-
Pointer to device memory scratch buffer at least as large as value returned by the corresponding MorphGetBufferSize call.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphBlackHatBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphBlackHatBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point morphological black hat with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphBlackHatBorder functions:](https://docs.nvidia.com#group__image__morph__black__hat__border_1commonmorphblackhatborderparameters).

### Image Morph Gradient Border[](https://docs.nvidia.com#image-morph-gradient-border)

#### MorphGradientBorder[](https://docs.nvidia.com#group__image__morph__gradient__border_1image_morph_gradient_border)

Morphological dilated pixel result minus morphological eroded pixel result with border control.

Morphological gradient computes the output pixel as the morphological dilated pixel value of the pixels under the mask minus the morphological eroded pixel value of the pixels under the mask. Pixels who’s corresponding mask values are zero do not participate in the maximum or minimum search.

If any portion of the mask overlaps the source image boundary the requested border type operation is applied to all mask pixels which fall outside of the source image. The mask is centered over the source image pixel being tested.

Before calling any of the MorphGradientBorder functions the application first needs to call the corresponding MorphGetBufferSize to determine the amount of device memory to allocate as a working buffer. The allocated device memory is then passed as the pBuffer parameter to the corresponding MorphGradientBorder function.

Use the oSrcOffset and oSrcSize parameters to control where the border control operation is applied to the source image ROI borders.

Currently only the NPP_BORDER_REPLICATE border type operation is supported.

##### Common parameters for nppiMorphGradientBorder functions:[](https://docs.nvidia.com#group__image__morph__gradient__border_1CommonMorphGradientBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSize
-
Source image width and height in pixels relative to pSrc.

- param oSrcOffset
-
Source image starting point relative to pSrc.

- param pDst
- param nDstStep
- param oSizeROI
- param pMask
-
Device memory pointer to the start address of the mask array (non-zero values select participating pixels).

- param oMaskSize
-
Width and Height mask array.

- param oAnchor
-
X and Y offsets of the mask origin frame of reference w.r.t the source pixel.

- param pBuffer
-
Pointer to device memory scratch buffer at least as large as value returned by the corresponding MorphGetBufferSize call.

- param eBorderType
-
The border type operation to be applied at source image border boundaries.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiMorphGradientBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oSrcOffset,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oMaskSize,[NppiPoint](https://docs.nvidia.com/nppdefs.html#c.NppiPoint)oAnchor,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pBuffer,[NppiBorderType](https://docs.nvidia.com/nppdefs.html#c.NppiBorderType)eBorderType,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiMorphGradientBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point morphological gradient with border control.

For common parameter descriptions, see

[Common parameters for nppiMorphGradientBorder functions:](https://docs.nvidia.com#group__image__morph__gradient__border_1commonmorphgradientborderparameters).