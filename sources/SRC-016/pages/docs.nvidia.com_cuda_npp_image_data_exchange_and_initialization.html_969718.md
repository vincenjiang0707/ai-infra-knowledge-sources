source: https://docs.nvidia.com/cuda/npp/image_data_exchange_and_initialization.html

# Image Data Exchange And Initialization Functions[](https://docs.nvidia.com#image-data-exchange-and-initialization-functions)

Functions for initializing, copying and converting image data.

These functions can be found in the nppidei library. Linking to only the sub-libraries that you use can significantly save link time, application load time, and CUDA runtime startup time when using dynamic libraries.

## Set[](https://docs.nvidia.com#group__image__set_1image_set)

Functions for setting all pixels within the ROI to a specific value.

### Common parameters for nppiSet functions:[](https://docs.nvidia.com#group__image__set_1CommonImageSetParameters)

- param nValue
-
The pixel value to be set.

- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8s_C1R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)nValue,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8s_C1R_Ctx)

-
8-bit image set.

For common parameter descriptions see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8s_C2R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)aValue[2],[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8s_C2R_Ctx)

-
8-bit two-channel image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8s_C3R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)aValue[3],[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8s_C3R_Ctx)

-
8-bit three-channel image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8s_C4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)aValue[4],[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8s_C4R_Ctx)

-
8-bit four-channel image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8s_AC4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)aValue[3],[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8s_AC4R_Ctx)

-
8-bit four-channel image set ignoring alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C1R_Ctx)

-
8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C2R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[2],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C2R_Ctx)

-
2 channel 8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C3R_Ctx)

-
3 channel 8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[4],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C4R_Ctx)

-
4 channel 8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C1R_Ctx)

-
16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C2R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[2],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C2R_Ctx)

-
2 channel 16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C3R_Ctx)

-
3 channel 16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[4],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C4R_Ctx)

-
4 channel 16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C1R_Ctx)

-
16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C2R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[2],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C2R_Ctx)

-
2 channel 16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[3],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C3R_Ctx)

-
3 channel 16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[4],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C4R_Ctx)

-
4 channel 16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[3],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_AC4R_Ctx)

-
4 channel 16-bit image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16sc_C1R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)oValue,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16sc_C1R_Ctx)

-
16-bit complex integer image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16sc_C2R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)aValue[2],[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16sc_C2R_Ctx)

-
16-bit complex integer two-channel image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16sc_C3R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)aValue[3],[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16sc_C3R_Ctx)

-
16-bit complex integer three-channel image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16sc_C4R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)aValue[4],[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16sc_C4R_Ctx)

-
16-bit complex integer four-channel image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16sc_AC4R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)aValue[3],[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16sc_AC4R_Ctx)

-
16-bit complex integer four-channel image set ignoring alpha.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C1R_Ctx)

-
32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C2R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[2],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C2R_Ctx)

-
2 channel 32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[3],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C3R_Ctx)

-
3 channel 32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[4],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C4R_Ctx)

-
4 channel 32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[3],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_AC4R_Ctx)

-
4 channel 32-bit image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32u_C1R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)nValue,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32u_C1R_Ctx)

-
32-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32u_C2R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)aValue[2],[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32u_C2R_Ctx)

-
2 channel 32-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32u_C3R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)aValue[3],[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32u_C3R_Ctx)

-
3 channel 32-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32u_C4R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)aValue[4],[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32u_C4R_Ctx)

-
4 channel 32-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32u_AC4R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)aValue[3],[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32u_AC4R_Ctx)

-
4 channel 32-bit unsigned image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32sc_C1R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)oValue,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32sc_C1R_Ctx)

-
Single channel 32-bit complex integer image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32sc_C2R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)aValue[2],[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32sc_C2R_Ctx)

-
Two channel 32-bit complex integer image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32sc_C3R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)aValue[3],[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32sc_C3R_Ctx)

-
Three channel 32-bit complex integer image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32sc_C4R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)aValue[4],[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32sc_C4R_Ctx)

-
Four channel 32-bit complex integer image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32sc_AC4R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)aValue[3],[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32sc_AC4R_Ctx)

-
32-bit complex integer four-channel image set ignoring alpha.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16f_C1R_Ctx)

-
16-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16f_C2R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValues[2],[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16f_C2R_Ctx)

-
2 channel 16-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValues[3],[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16f_C3R_Ctx)

-
3 channel 16-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValues[4],[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16f_C4R_Ctx)

-
4 channel 16-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C1R_Ctx)

-
32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C2R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[2],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C2R_Ctx)

-
2 channel 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C2R(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[2],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI)[](https://docs.nvidia.com#c.nppiSet_32f_C2R)

-
2 channel 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[3],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C3R_Ctx)

-
3 channel 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[4],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C4R_Ctx)

-
4 channel 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[3],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32fc_C1R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)oValue,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32fc_C1R_Ctx)

-
Single channel 32-bit complex image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32fc_C2R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)aValue[2],[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32fc_C2R_Ctx)

-
Two channel 32-bit complex image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32fc_C3R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)aValue[3],[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32fc_C3R_Ctx)

-
Three channel 32-bit complex image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32fc_C4R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)aValue[4],[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32fc_C4R_Ctx)

-
Four channel 32-bit complex image set.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32fc_AC4R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)aValue[3],[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32fc_AC4R_Ctx)

-
32-bit complex four-channel image set ignoring alpha.

For common parameter descriptions, see

[Common parameters for nppiSet functions:](https://docs.nvidia.com#group__image__set_1commonimagesetparameters).

## Masked Set[](https://docs.nvidia.com#group__image__masked__set_1image_masked_set)

The masked set primitives have an additional “mask image” input. The mask

controls which pixels within the ROI are set. For details see

[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation).

### Common parameters for nppiSet_CXM functions:[](https://docs.nvidia.com#group__image__masked__set_1CommonImageMaskedSetParameters)

- param nValue
-
The pixel value to be set for single channel functions.

- param aValue
-
The pixel-value to be set for multi-channel functions.

- param pDst
-
Pointer

[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer). - param nDstStep
- param oSizeROI
- param pMask
- param nMaskStep
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C1MR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C1MR_Ctx)

-
Masked 8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C3MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C3MR_Ctx)

-
Masked 3 channel 8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C4MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[4],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C4MR_Ctx)

-
Masked 4 channel 8-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_AC4MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[3],[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_AC4MR_Ctx)

-
Masked 4 channel 8-bit unsigned image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C1MR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C1MR_Ctx)

-
Masked 16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C3MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C3MR_Ctx)

-
Masked 3 channel 16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C4MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[4],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C4MR_Ctx)

-
Masked 4 channel 16-bit unsigned image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_AC4MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[3],[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_AC4MR_Ctx)

-
Masked 4 channel 16-bit unsigned image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C1MR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C1MR_Ctx)

-
Masked 16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C3MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[3],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C3MR_Ctx)

-
Masked 3 channel 16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C4MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[4],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C4MR_Ctx)

-
Masked 4 channel 16-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_AC4MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[3],[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_AC4MR_Ctx)

-
Masked 4 channel 16-bit image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C1MR_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C1MR_Ctx)

-
Masked 32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C3MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[3],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C3MR_Ctx)

-
Masked 3 channel 32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C4MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[4],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C4MR_Ctx)

-
Masked 4 channel 32-bit image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_AC4MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[3],[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_AC4MR_Ctx)

-
Masked 4 channel 16-bit image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C1MR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C1MR_Ctx)

-
Masked 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C3MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[3],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C3MR_Ctx)

-
Masked 3 channel 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C4MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[4],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C4MR_Ctx)

-
Masked 4 channel 32-bit floating point image set.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_AC4MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[3],[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_AC4MR_Ctx)

-
Masked 4 channel 32-bit floating point image set method, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXM functions:](https://docs.nvidia.com#group__image__masked__set_1commonimagemaskedsetparameters).

## Channel Set[](https://docs.nvidia.com#group__image__channel__set_1image_channel_set)

The selected-channel set primitives set a single color channel in multi-channel images to a given value. The channel is selected by adjusting the pDst pointer to point to the desired color channel (see [Channel-of-Interest API](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest)).

### Common parameters for nppiSet_CXC functions:[](https://docs.nvidia.com#group__image__channel__set_1CommonImageChannelSetParameters)

- param nValue
-
The pixel-value to be set.

- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C3CR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C3CR_Ctx)

-
3 channel 8-bit unsigned image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_8u_C4CR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_8u_C4CR_Ctx)

-
4 channel 8-bit unsigned image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C3CR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C3CR_Ctx)

-
3 channel 16-bit unsigned image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16u_C4CR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16u_C4CR_Ctx)

-
4 channel 16-bit unsigned image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C3CR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C3CR_Ctx)

-
3 channel 16-bit signed image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_16s_C4CR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_16s_C4CR_Ctx)

-
4 channel 16-bit signed image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C3CR_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C3CR_Ctx)

-
3 channel 32-bit unsigned image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32s_C4CR_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32s_C4CR_Ctx)

-
4 channel 32-bit unsigned image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C3CR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C3CR_Ctx)

-
3 channel 32-bit floating point image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSet_32f_C4CR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSet_32f_C4CR_Ctx)

-
4 channel 32-bit floating point image set affecting only single channel.

For common parameter descriptions, see

[Common parameters for nppiSet_CXC functions:](https://docs.nvidia.com#group__image__channel__set_1commonimagechannelsetparameters).

Functions for copying image pixels.

## Copy[](https://docs.nvidia.com#group__image__copy_1image_copy)

Copy pixels from one image to another.

### Common parameters for nppiCopy functions:[](https://docs.nvidia.com#group__image__copy_1CommonImageCopyParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8s_C1R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8s_C1R_Ctx)

-
8-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8s_C2R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8s_C2R_Ctx)

-
Two-channel 8-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8s_C3R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8s_C3R_Ctx)

-
Three-channel 8-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8s_C4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8s_C4R_Ctx)

-
Four-channel 8-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8s_AC4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8s_AC4R_Ctx)

-
Four-channel 8-bit image copy, ignoring alpha channel.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C1R_Ctx)

-
8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C3R_Ctx)

-
Three channel 8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C4R_Ctx)

-
4 channel 8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned image copy, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C1R_Ctx)

-
16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C3R_Ctx)

-
Three channel 16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C4R_Ctx)

-
4 channel 16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned image copy, not affecting Alpha channel.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C1R_Ctx)

-
16-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C3R_Ctx)

-
Three channel 16-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C4R_Ctx)

-
4 channel 16-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_AC4R_Ctx)

-
4 channel 16-bit image copy, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16sc_C1R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, int nSrcStep,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16sc_C1R_Ctx)

-
16-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16sc_C2R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, int nSrcStep,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16sc_C2R_Ctx)

-
Two-channel 16-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16sc_C3R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, int nSrcStep,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16sc_C3R_Ctx)

-
Three-channel 16-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16sc_C4R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, int nSrcStep,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16sc_C4R_Ctx)

-
Four-channel 16-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16sc_AC4R_Ctx(const[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pSrc, int nSrcStep,[Npp16sc](https://docs.nvidia.com/nppdefs.html#c.Npp16sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16sc_AC4R_Ctx)

-
Four-channel 16-bit complex image copy, ignoring alpha.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C1R_Ctx)

-
32-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C3R_Ctx)

-
Three channel 32-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C4R_Ctx)

-
4 channel 32-bit image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_AC4R_Ctx)

-
4 channel 32-bit image copy, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32sc_C1R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc, int nSrcStep,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32sc_C1R_Ctx)

-
32-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32sc_C2R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc, int nSrcStep,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32sc_C2R_Ctx)

-
Two-channel 32-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32sc_C3R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc, int nSrcStep,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32sc_C3R_Ctx)

-
Three-channel 32-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32sc_C4R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc, int nSrcStep,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32sc_C4R_Ctx)

-
Four-channel 32-bit complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32sc_AC4R_Ctx(const[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pSrc, int nSrcStep,[Npp32sc](https://docs.nvidia.com/nppdefs.html#c.Npp32sc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32sc_AC4R_Ctx)

-
Four-channel 32-bit complex image copy, ignoring alpha.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16f_C1R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16f_C1R_Ctx)

-
16-bit floating point image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16f_C3R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16f_C3R_Ctx)

-
Three channel 16-bit floating point image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16f_C4R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16f_C4R_Ctx)

-
4 channel 16-bit floating point image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C1R_Ctx)

-
32-bit floating point image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C3R_Ctx)

-
Three channel 32-bit floating point image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C4R_Ctx)

-
4 channel 32-bit floating point image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image copy, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32fc_C1R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32fc_C1R_Ctx)

-
32-bit floating-point complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32fc_C2R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32fc_C2R_Ctx)

-
Two-channel 32-bit floating-point complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32fc_C3R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32fc_C3R_Ctx)

-
Three-channel 32-bit floating-point complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32fc_C4R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32fc_C4R_Ctx)

-
Four-channel 32-bit floating-point complex image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32fc_AC4R_Ctx(const[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pSrc, int nSrcStep,[Npp32fc](https://docs.nvidia.com/nppdefs.html#c.Npp32fc)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32fc_AC4R_Ctx)

-
Four-channel 32-bit floating-point complex image copy, ignoring alpha.

For common parameter descriptions, see

[Common parameters for nppiCopy functions:](https://docs.nvidia.com#group__image__copy_1commonimagecopyparameters).

## Masked Copy[](https://docs.nvidia.com#group__image__masked__copy_1image_masked_copy)

The masked copy primitives have an additional “mask image” input. The mask

controls which pixels within the ROI are copied. For details see

[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation).

### Common parameters for nppiCopy_CXM functions:[](https://docs.nvidia.com#group__image__masked__copy_1CommonImageMaskedCopyParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param pMask
- param nMaskStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C1MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C1MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)8-bit unsigned image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C3MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C3MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)three channel 8-bit unsigned image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C4MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 8-bit unsigned image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_AC4MR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_AC4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 8-bit unsigned image copy, ignoring alpha.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C1MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C1MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)16-bit unsigned image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C3MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C3MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)three channel 16-bit unsigned image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C4MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 16-bit unsigned image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_AC4MR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_AC4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 16-bit unsigned image copy, ignoring alpha.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C1MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C1MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)16-bit signed image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C3MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C3MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)three channel 16-bit signed image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C4MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 16-bit signed image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_AC4MR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_AC4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 16-bit signed image copy, ignoring alpha.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C1MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C1MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)32-bit signed image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C3MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C3MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)three channel 32-bit signed image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C4MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 32-bit signed image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_AC4MR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_AC4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 32-bit signed image copy, ignoring alpha.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C1MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C1MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)32-bit float image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C3MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C3MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)three channel 32-bit float image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C4MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 32-bit float image copy.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_AC4MR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pMask, int nMaskStep,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_AC4MR_Ctx)

-
[Masked Operation](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1masked_operation)four channel 32-bit float image copy, ignoring alpha.For common parameter descriptions, see

[Common parameters for nppiCopy_CXM functions:](https://docs.nvidia.com#group__image__masked__copy_1commonimagemaskedcopyparameters).

## Channel Copy[](https://docs.nvidia.com#group__image__channel__copy_1image_channel_copy)

The channel copy primitives copy a single color channel from a multi-channel source image to any other color channel in a multi-channel destination image. The channel is selected by adjusting the respective image pointers to point to the desired color channel (see [Channel-of-Interest API](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest)).

### Common parameters for nppiCopy_CXC functions:[](https://docs.nvidia.com#group__image__channel__copy_1CommonImageChannelCopyParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C3CR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C3CR_Ctx)

-
Selected channel 8-bit unsigned image copy for three-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C4CR_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C4CR_Ctx)

-
Selected channel 8-bit unsigned image copy for four-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C3CR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C3CR_Ctx)

-
Selected channel 16-bit signed image copy for three-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C4CR_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C4CR_Ctx)

-
Selected channel 16-bit signed image copy for four-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C3CR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C3CR_Ctx)

-
Selected channel 16-bit unsigned image copy for three-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C4CR_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C4CR_Ctx)

-
Selected channel 16-bit unsigned image copy for four-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C3CR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C3CR_Ctx)

-
Selected channel 32-bit signed image copy for three-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C4CR_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C4CR_Ctx)

-
Selected channel 32-bit signed image copy for four-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C3CR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C3CR_Ctx)

-
Selected channel 32-bit float image copy for three-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C4CR_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C4CR_Ctx)

-
Selected channel 32-bit float image copy for four-channel images.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC functions:](https://docs.nvidia.com#group__image__channel__copy_1commonimagechannelcopyparameters).

## Extract Channel Copy[](https://docs.nvidia.com#group__image__extract__channel__copy_1image_extract_channel_copy)

The channel extract primitives copy a single color channel from a multi-channel source image to singl-channel destination image. The channel is selected by adjusting the source image pointer to point to the desired color channel (see [Channel-of-Interest API](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest)).

### Common parameters for nppiCopy_CXC1 functions:[](https://docs.nvidia.com#group__image__extract__channel__copy_1CommonImageExtractChannelCopyParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C3C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C3C1R_Ctx)

-
Three-channel to single-channel 8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C4C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C4C1R_Ctx)

-
Four-channel to single-channel 8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C3C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C3C1R_Ctx)

-
Three-channel to single-channel 16-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C4C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C4C1R_Ctx)

-
Four-channel to single-channel 16-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C3C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C3C1R_Ctx)

-
Three-channel to single-channel 16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C4C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C4C1R_Ctx)

-
Four-channel to single-channel 16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C3C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C3C1R_Ctx)

-
Three-channel to single-channel 32-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C4C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C4C1R_Ctx)

-
Four-channel to single-channel 32-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C2C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C2C1R_Ctx)

-
Two-channel to single-channel 32-bit float image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C3C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C3C1R_Ctx)

-
Three-channel to single-channel 32-bit float image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C4C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C4C1R_Ctx)

-
Four-channel to single-channel 32-bit float image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXC1 functions:](https://docs.nvidia.com#group__image__extract__channel__copy_1commonimageextractchannelcopyparameters).

## Insert Channel Copy[](https://docs.nvidia.com#group__image__insert__channel__copy_1image_insert_channel_copy)

The channel insert primitives copy a single-channel source image into one of the color channels in a multi-channel destination image. The channel is selected by adjusting the destination image pointer to point to the desired color channel (see [Channel-of-Interest API](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1channel_of_interest)).

### Common parameters for nppiCopy_C1CX functions:[](https://docs.nvidia.com#group__image__insert__channel__copy_1CommonImageInsertChannelCopyParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C1C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C1C3R_Ctx)

-
Single-channel to three-channel 8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C1C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C1C4R_Ctx)

-
Single-channel to four-channel 8-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C1C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C1C3R_Ctx)

-
Single-channel to three-channel 16-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C1C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C1C4R_Ctx)

-
Single-channel to four-channel 16-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C1C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C1C3R_Ctx)

-
Single-channel to three-channel 16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C1C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C1C4R_Ctx)

-
Single-channel to four-channel 16-bit unsigned image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C1C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C1C3R_Ctx)

-
Single-channel to three-channel 32-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C1C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C1C4R_Ctx)

-
Single-channel to four-channel 32-bit signed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C1C2R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C1C2R_Ctx)

-
Single-channel to two-channel 32-bit float image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C1C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C1C3R_Ctx)

-
Single-channel to three-channel 32-bit float image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C1C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C1C4R_Ctx)

-
Single-channel to four-channel 32-bit float image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_C1CX functions:](https://docs.nvidia.com#group__image__insert__channel__copy_1commonimageinsertchannelcopyparameters).

## Packed To Planar Channel Copy[](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1image_packed_to_planar_channel_copy)

Split a packed multi-channel image into multiple single channel planes.

E.g. copy the three channels of an RGB image into three separate single-channel images.

### Common parameters for nppiCopy_CXPX functions:[](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1CommonImagePackedToPlanarChannelCopyParameters)

- param pSrc
- param nSrcStep
- param aDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C3P3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const aDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C3P3R_Ctx)

-
Three-channel 8-bit unsigned packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_C4P4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const aDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_C4P4R_Ctx)

-
Four-channel 8-bit unsigned packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C3P3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const aDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C3P3R_Ctx)

-
Three-channel 16-bit signed packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_C4P4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const aDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_C4P4R_Ctx)

-
Four-channel 16-bit signed packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C3P3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const aDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C3P3R_Ctx)

-
Three-channel 16-bit unsigned packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_C4P4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const aDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_C4P4R_Ctx)

-
Four-channel 16-bit unsigned packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C3P3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*const aDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C3P3R_Ctx)

-
Three-channel 32-bit signed packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_C4P4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*const aDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_C4P4R_Ctx)

-
Four-channel 32-bit signed packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C3P3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const aDst[3], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C3P3R_Ctx)

-
Three-channel 32-bit float packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_C4P4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const aDst[4], int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_C4P4R_Ctx)

-
Four-channel 32-bit float packed to planar image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_CXPX functions:](https://docs.nvidia.com#group__image__packed__to__planar__channel__copy_1commonimagepackedtoplanarchannelcopyparameters).

## Planar To Packed Channel Copy[](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1image_planar_to_packed_channel_copy)

Combine multiple image planes into a packed multi-channel image.

E.g. copy three single-channel images into a single 3-channel image.

### Common parameters for nppiCopy_PXCX functions:[](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1CommonImagePlanarToPackedChannelCopyParameters)

- param aSrc
-
Planar

[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer). - param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_P3C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const aSrc[3], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_P3C3R_Ctx)

-
Three-channel 8-bit unsigned planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_8u_P4C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*const aSrc[4], int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_8u_P4C4R_Ctx)

-
Four-channel 8-bit unsigned planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_P3C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const aSrc[3], int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_P3C3R_Ctx)

-
Three-channel 16-bit unsigned planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16u_P4C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*const aSrc[4], int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16u_P4C4R_Ctx)

-
Four-channel 16-bit unsigned planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_P3C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const aSrc[3], int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_P3C3R_Ctx)

-
Three-channel 16-bit signed planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_16s_P4C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*const aSrc[4], int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_16s_P4C4R_Ctx)

-
Four-channel 16-bit signed planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_P3C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*const aSrc[3], int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_P3C3R_Ctx)

-
Three-channel 32-bit signed planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32s_P4C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*const aSrc[4], int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32s_P4C4R_Ctx)

-
Four-channel 32-bit signed planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_P3C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const aSrc[3], int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_P3C3R_Ctx)

-
Three-channel 32-bit float planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopy_32f_P4C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*const aSrc[4], int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopy_32f_P4C4R_Ctx)

-
Four-channel 32-bit float planar to packed image copy.

For common parameter descriptions, see

[Common parameters for nppiCopy_PXCX functions:](https://docs.nvidia.com#group__image__planar__to__packed__channel__copy_1commonimageplanartopackedchannelcopyparameters).

## Copy Constant Border[](https://docs.nvidia.com#group__image__copy__constant__border_1image_copy_constant_border)

Methods for copying images and padding borders with a constant, user-specifiable color.

### Common parameters for nppiCopyConstBorder functions:[](https://docs.nvidia.com#group__image__copy__constant__border_1CommonImageCopyConstantBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSizeROI
-
Size of the source region of pixels.

- param pDst
- param nDstStep
- param oDstSizeROI
-
Size (width, height) of the destination region, i.e. the region that gets filled with data from the source image (inner part) and constant border color (outer part).

- param nTopBorderHeight
-
Height (in pixels) of the top border. The number of pixel rows at the top of the destination ROI that will be filled with the constant border color. nBottomBorderHeight = oDstSizeROI.height - nTopBorderHeight - oSrcSizeROI.height.

- param nLeftBorderWidth
-
Width (in pixels) of the left border. The width of the border at the right side of the destination ROI is implicitly defined by the size of the source ROI: nRightBorderWidth = oDstSizeROI.width - nLeftBorderWidth - oSrcSizeROI.width.

- param nValue
-
The pixel value to be set for border pixels for single channel functions.

- param aValue
-
Vector of the RGBA values of the border pixels to be set for multi-channel functions.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned integer image copy with constant border color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16u_C3R_Ctx)

-
3 channel 16-bit unsigned integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16u_C4R_Ctx)

-
4 channel 16-bit unsigned integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned integer image copy with constant border color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16s_C3R_Ctx)

-
3 channel 16-bit signed integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16s_C4R_Ctx)

-
4 channel 16-bit signed integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_16s_AC4R_Ctx)

-
4 channel 16-bit signed integer image copy with constant border color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32s_C1R_Ctx)

-
1 channel 32-bit signed integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32s_C3R_Ctx)

-
3 channel 32-bit signed integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32s_C4R_Ctx)

-
4 channel 32-bit signed integer image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32s_AC4R_Ctx)

-
4 channel 32-bit signed integer image copy with constant border color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point image copy with constant border color.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyConstBorder_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth, const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)aValue[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyConstBorder_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image copy with constant border color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyConstBorder functions:](https://docs.nvidia.com#group__image__copy__constant__border_1commonimagecopyconstantborderparameters).

## Copy Replicate Border[](https://docs.nvidia.com#group__image__copy__replicate__border_1image_copy_replicate_border)

Methods for copying images and padding borders with a replicates of the nearest source image pixel color.

### Common parameters for nppiCopyReplicateBorder functions:[](https://docs.nvidia.com#group__image__copy__replicate__border_1CommonImageCopyReplicateBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSizeROI
-
Size of the source region of pixels.

- param pDst
- param nDstStep
- param oDstSizeROI
-
Size (width, height) of the destination region, i.e. the region that gets filled with data from the source image (inner part) and nearest source image pixel color (outer part).

- param nTopBorderHeight
-
Height (in pixels) of the top border. The number of pixel rows at the top of the destination ROI that will be filled with the nearest source image pixel color. nBottomBorderHeight = oDstSizeROI.height - nTopBorderHeight - oSrcSizeROI.height.

- param nLeftBorderWidth
-
Width (in pixels) of the left border. The width of the border at the right side of the destination ROI is implicitly defined by the size of the source ROI: nRightBorderWidth = oDstSizeROI.width - nLeftBorderWidth - oSrcSizeROI.width.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned integer image copy with nearest source image pixel color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16u_C3R_Ctx)

-
3 channel 16-bit unsigned integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16u_C4R_Ctx)

-
4 channel 16-bit unsigned integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned image copy with nearest source image pixel color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16s_C3R_Ctx)

-
3 channel 16-bit signed integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16s_C4R_Ctx)

-
4 channel 16-bit signed integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_16s_AC4R_Ctx)

-
4 channel 16-bit signed integer image copy with nearest source image pixel color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32s_C1R_Ctx)

-
1 channel 32-bit signed integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32s_C3R_Ctx)

-
3 channel 32-bit signed image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32s_C4R_Ctx)

-
4 channel 32-bit signed integer image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32s_AC4R_Ctx)

-
4 channel 32-bit signed integer image copy with nearest source image pixel color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point image copy with nearest source image pixel color.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyReplicateBorder_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyReplicateBorder_32f_AC4R_Ctx)

-
4 channel 32-bit floating point image copy with nearest source image pixel color with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyReplicateBorder functions:](https://docs.nvidia.com#group__image__copy__replicate__border_1commonimagecopyreplicateborderparameters).

## Copy Wrap Border[](https://docs.nvidia.com#group__image__copy__wrap__border_1image_copy_wrap_border)

Methods for copying images and padding borders with wrapped replications of the source image pixel colors.

### Common parameters for nppiCopyWrapBorder functions:[](https://docs.nvidia.com#group__image__copy__wrap__border_1CommonImageCopyWrapBorderParameters)

- param pSrc
- param nSrcStep
- param oSrcSizeROI
-
Size of the source region of pixels.

- param pDst
- param nDstStep
- param oDstSizeROI
-
Size (width, height) of the destination region, i.e. the region that gets filled with data from the source image (inner part) and a border consisting of wrapped replication of the source image pixel colors (outer part).

- param nTopBorderHeight
-
Height (in pixels) of the top border. The number of pixel rows at the top of the destination ROI that will be filled with the wrapped replication of the corresponding column of source image pixels colors. nBottomBorderHeight = oDstSizeROI.height - nTopBorderHeight - oSrcSizeROI.height.

- param nLeftBorderWidth
-
Width (in pixels) of the left border. The width of the border at the right side of the destination ROI is implicitly defined by the size of the source ROI: nRightBorderWidth = oDstSizeROI.width - nLeftBorderWidth - oSrcSizeROI.width.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16u_C3R_Ctx)

-
3 channel 16-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16u_C4R_Ctx)

-
4 channel 16-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned integer image copy with the borders wrapped by replication of source image pixel colors with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16s_C1R_Ctx)

-
1 channel 16-bit signed integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16s_C3R_Ctx)

-
3 channel 16-bit signed integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16s_C4R_Ctx)

-
4 channel 16-bit signed integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_16s_AC4R_Ctx)

-
4 channel 16-bit signed integer image copy with the borders wrapped by replication of source image pixel colors with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32s_C1R_Ctx)

-
1 channel 32-bit signed integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32s_C3R_Ctx)

-
3 channel 32-bit signed integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32s_C4R_Ctx)

-
4 channel 32-bit signed integer image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32s_AC4R_Ctx)

-
4 channel 32-bit signed integer image copy with the borders wrapped by replication of source image pixel colors with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32f_C1R_Ctx)

-
1 channel 32-bit floating point image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32f_C3R_Ctx)

-
3 channel 32-bit floating point image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32f_C4R_Ctx)

-
4 channel 32-bit floating point image copy with the borders wrapped by replication of source image pixel colors.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopyWrapBorder_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI, int nTopBorderHeight, int nLeftBorderWidth,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopyWrapBorder_32f_AC4R_Ctx)

-
1 channel 32-bit floating point image copy with the borders wrapped by replication of source image pixel colors with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopyWrapBorder functions:](https://docs.nvidia.com#group__image__copy__wrap__border_1commonimagecopywrapborderparameters).

## Copy Sub-Pixel[](https://docs.nvidia.com#group__image__copy__sub__pixel_1image_copy_sub_pixel)

Functions for copying linearly interpolated images using source image subpixel coordinates.

### Common parameters for nppiCopySubPix functions:[](https://docs.nvidia.com#group__image__copy__sub__pixel_1CommonImageCopySubPixelParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oDstSizeROI
-
Size (width, height) of the destination region, i.e. the region that gets filled with data from the source image, source image ROI is assumed to be same as destination image ROI.

- param nDx
-
Fractional part of source image X coordinate.

- param nDy
-
Fractional part of source image Y coordinate.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_8u_C1R_Ctx)

-
1 channel 8-bit unsigned integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned integer linearly interpolated source image subpixel coordinate color copy with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16u_C1R_Ctx)

-
1 channel 16-bit unsigned integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16u_C3R_Ctx)

-
3 channel 16-bit unsigned integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16u_C4R_Ctx)

-
4 channel 16-bit unsigned integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned linearly interpolated source image subpixel coordinate color copy with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16s_C1R_Ctx)

-
1 channel 16-bit signed integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16s_C3R_Ctx)

-
3 channel 16-bit signed integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16s_C4R_Ctx)

-
4 channel 16-bit signed integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_16s_AC4R_Ctx)

-
4 channel 16-bit signed integer linearly interpolated source image subpixel coordinate color copy with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32s_C1R_Ctx)

-
1 channel 32-bit signed integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32s_C3R_Ctx)

-
3 channel 32-bit signed linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32s_C4R_Ctx)

-
4 channel 32-bit signed integer linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32s_AC4R_Ctx)

-
4 channel 32-bit signed integer linearly interpolated source image subpixel coordinate color copy with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32f_C1R_Ctx)

-
1 channel 32-bit floating point linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32f_C3R_Ctx)

-
3 channel 32-bit floating point linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32f_C4R_Ctx)

-
4 channel 32-bit floating point linearly interpolated source image subpixel coordinate color copy.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiCopySubpix_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDx,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nDy,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiCopySubpix_32f_AC4R_Ctx)

-
4 channel 32-bit floating point linearly interpolated source image subpixel coordinate color copy with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiCopySubPix functions:](https://docs.nvidia.com#group__image__copy__sub__pixel_1commonimagecopysubpixelparameters).

## Convert Bit Depth[](https://docs.nvidia.com#group__image__convert_1image_convert)

Functions for converting bit depth without scaling.

## Convert To Increased Bit Depth[](https://docs.nvidia.com#group__image__convert__increase_1image_convert_increase)

The integer conversion methods do not involve any scaling. Also, even when increasing the bit-depth loss of information may occur:

When converting integers (e.g. Npp32u) to float (e.g. Npp32f) integer value not accurately representable by the float are rounded to the closest floating-point value.

When converting signed integers to unsigned integers all negative values are lost (saturated to 0).


Note that all pointers and step sizes for images with 16f ([Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.

### Common parameters for nppiConvert to increased bit depth functions:[](https://docs.nvidia.com#group__image__convert__increase_1CommonImageConvertToIncreasedBitDepthParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16u_C1R_Ctx)

-
Single channel 8-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16u_C3R_Ctx)

-
Three channel 8-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16u_C4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16u_AC4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16s_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16s_C1R_Ctx)

-
Single channel 8-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16s_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16s_C3R_Ctx)

-
Three channel 8-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16s_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16s_C4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u16s_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u16s_AC4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32s_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32s_C1R_Ctx)

-
Single channel 8-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32s_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32s_C3R_Ctx)

-
Three channel 8-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32s_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32s_C4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32s_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32s_AC4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32f_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32f_C1R_Ctx)

-
Single channel 8-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32f_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32f_C3R_Ctx)

-
Three channel 8-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32f_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32f_C4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u32f_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u32f_AC4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit floating-point conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32s_C1R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32s_C1R_Ctx)

-
Single channel 8-bit signed to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32s_C3R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32s_C3R_Ctx)

-
Three channel 8-bit signed to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32s_C4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32s_C4R_Ctx)

-
Four channel 8-bit signed to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32s_AC4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32s_AC4R_Ctx)

-
Four channel 8-bit signed to 32-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32f_C1R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32f_C1R_Ctx)

-
Single channel 8-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32f_C3R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32f_C3R_Ctx)

-
Three channel 8-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32f_C4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32f_C4R_Ctx)

-
Four channel 8-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32f_AC4R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32f_AC4R_Ctx)

-
Four channel 8-bit signed to 32-bit floating-point conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32s_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32s_C1R_Ctx)

-
Single channel 16-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32s_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32s_C3R_Ctx)

-
Three channel 16-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32s_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32s_C4R_Ctx)

-
Four channel 16-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32s_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32s_AC4R_Ctx)

-
Four channel 16-bit unsigned to 32-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32f_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32f_C1R_Ctx)

-
Single channel 16-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32f_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32f_C3R_Ctx)

-
Three channel 16-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32f_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32f_C4R_Ctx)

-
Four channel 16-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32f_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32f_AC4R_Ctx)

-
Four channel 16-bit unsigned to 32-bit floating-point conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32s_C1R_Ctx)

-
Single channel 16-bit signed to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32s_C3R_Ctx)

-
Three channel 16-bit signed to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32s_C4R_Ctx)

-
Four channel 16-bit signed to 32-bit signed conversion.


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32s_AC4R_Ctx)

-
Four channel 16-bit signed to 32-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32f_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32f_C1R_Ctx)

-
Single channel 16-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32f_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32f_C3R_Ctx)

-
Three channel 16-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32f_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32f_C4R_Ctx)

-
Four channel 16-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32f_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32f_AC4R_Ctx)

-
Four channel 16-bit signed to 32-bit floating-point conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16f32f_C1R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16f32f_C1R_Ctx)

-
Single channel 16-bit floating-point to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16f32f_C3R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16f32f_C3R_Ctx)

-
Three channel 16-bit floating-point to 32-bit floating-point conversion.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte alignedFor common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16f32f_C4R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16f32f_C4R_Ctx)

-
Four channel 16-bit floating-point to 32-bit floating-point conversion.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16f32f_AC4R_Ctx(const[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16f32f_AC4R_Ctx)

-
Four channel 16-bit floating-point to 32-bit floating-point conversion, not affecting Alpha.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s8u_C1Rs_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s8u_C1Rs_Ctx)

-
Single channel 8-bit signed to 8-bit unsigned conversion with saturation.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s16u_C1Rs_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s16u_C1Rs_Ctx)

-
Single channel 8-bit signed to 16-bit unsigned conversion with saturation.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s16s_C1R_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s16s_C1R_Ctx)

-
Single channel 8-bit signed to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8s32u_C1Rs_Ctx(const[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8s32u_C1Rs_Ctx)

-
Single channel 8-bit signed to 32-bit unsigned conversion with saturation.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s16u_C1Rs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s16u_C1Rs_Ctx)

-
Single channel 16-bit signed to 16-bit unsigned conversion with saturation.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s32u_C1Rs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s32u_C1Rs_Ctx)

-
Single channel 16-bit signed to 32-bit unsigned conversion with saturation.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u32u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u32u_C1R_Ctx)

-
Single channel 16-bit unsigned to 32-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s32u_C1Rs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s32u_C1Rs_Ctx)

-
Single channel 32-bit signed to 32-bit unsigned conversion with saturation.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s32f_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s32f_C1R_Ctx)

-
Single channel 32-bit signed to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32u32f_C1R_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32u32f_C1R_Ctx)

-
Single channel 32-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to increased bit depth functions:](https://docs.nvidia.com#group__image__convert__increase_1commonimageconverttoincreasedbitdepthparameters).

## Convert To Decreased Bit Depth[](https://docs.nvidia.com#group__image__convert__decrease_1image_convert_decrease)

The integer conversion methods do not involve any scaling. When converting floating-point values to integers the user may choose the most appropriate rounding-mode. Typically information is lost when converting to lower bit depth:

All converted values are saturated to the destination type’s range. E.g. any values larger than the largest value of the destination type are clamped to the destination’s maximum.

Converting floating-point values to integer also involves rounding, effectively loosing all fractional value information in the process.


Note that all pointers and step sizes for images with 16f ([Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.

### Common parameters for nppiConvert to decreased bit depth functions:[](https://docs.nvidia.com#group__image__convert__decrease_1CommonImageConvertToDecreasedBitDepthParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param eRoundMode
- param nScaleFactor
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u8u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u8u_C1R_Ctx)

-
Single channel 16-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u8u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u8u_C3R_Ctx)

-
Three channel 16-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u8u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u8u_C4R_Ctx)

-
Four channel 16-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u8u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u8u_AC4R_Ctx)

-
Four channel 16-bit unsigned to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s8u_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s8u_C1R_Ctx)

-
Single channel 16-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s8u_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s8u_C3R_Ctx)

-
Three channel 16-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s8u_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s8u_C4R_Ctx)

-
Four channel 16-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s8u_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s8u_AC4R_Ctx)

-
Four channel 16-bit signed to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8u_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8u_C1R_Ctx)

-
Single channel 32-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8u_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8u_C3R_Ctx)

-
Three channel 32-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8u_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8u_C4R_Ctx)

-
Four channel 32-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8u_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8u_AC4R_Ctx)

-
Four channel 32-bit signed to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8s_C1R_Ctx)

-
Single channel 32-bit signed to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8s_C3R_Ctx)

-
Three channel 32-bit signed to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8s_C4R_Ctx)

-
Four channel 32-bit signed to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s8s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s8s_AC4R_Ctx)

-
Four channel 32-bit signed to 8-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_8u8s_C1RSfs_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_8u8s_C1RSfs_Ctx)

-
Single channel 8-bit unsigned to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u8s_C1RSfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u8s_C1RSfs_Ctx)

-
Single channel 16-bit unsigned to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16s8s_C1RSfs_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16s8s_C1RSfs_Ctx)

-
Single channel 16-bit signed to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_16u16s_C1RSfs_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_16u16s_C1RSfs_Ctx)

-
Single channel 16-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32u8u_C1RSfs_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32u8u_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32u8s_C1RSfs_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32u8s_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32u16u_C1RSfs_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32u16u_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32u16s_C1RSfs_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32u16s_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32u32s_C1RSfs_Ctx(const[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32u32s_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s16u_C1RSfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s16u_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32s16s_C1RSfs_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32s16s_C1RSfs_Ctx)

-
Single channel 32-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8u_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8u_C1R_Ctx)

-
Single channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8u_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8u_C3R_Ctx)

-
Three channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8u_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8u_C4R_Ctx)

-
Four channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8u_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8u_AC4R_Ctx)

-
Four channel 32-bit floating point to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8s_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8s_C1R_Ctx)

-
Single channel 32-bit floating point to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8s_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8s_C3R_Ctx)

-
Three channel 32-bit floating point to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8s_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8s_C4R_Ctx)

-
Four channel 32-bit floating point to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8s_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8s_AC4R_Ctx)

-
Four channel 32-bit floating point to 8-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16u_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16u_C1R_Ctx)

-
Single channel 32-bit floating point to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16u_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16u_C3R_Ctx)

-
Three channel 32-bit floating point to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16u_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16u_C4R_Ctx)

-
Four channel 32-bit floating point to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16u_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16u_AC4R_Ctx)

-
Four channel 32-bit floating point to 16-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16s_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16s_C1R_Ctx)

-
Single channel 32-bit floating point to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16s_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16s_C3R_Ctx)

-
Three channel 32-bit floating point to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16s_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16s_C4R_Ctx)

-
Four channel 32-bit floating point to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16s_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16s_AC4R_Ctx)

-
Four channel 32-bit floating point to 16-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16f_C1R_Ctx)

-
Single channel 32-bit floating point to 16-bit floating-point conversion.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16f_C3R_Ctx)

-
Three channel 32-bit floating point to 16-bit floating-point conversion.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16f_C4R_Ctx)

-
Four channel 32-bit floating point to 16-bit floating-point conversion.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16f](https://docs.nvidia.com/nppdefs.html#c.Npp16f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16f_AC4R_Ctx)

-
Four channel 32-bit floating point to 16-bit floating-point conversion.

Note that all pointers and step sizes for images with 16f (

[Npp16f](https://docs.nvidia.com/nppdefs.html#structnpp16f)) data types perform best when they are at least 16 byte aligned.For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8u_C1RSfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8u_C1RSfs_Ctx)

-
Single channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f8s_C1RSfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8s](https://docs.nvidia.com/nppdefs.html#c.Npp8s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f8s_C1RSfs_Ctx)

-
Single channel 32-bit floating point to 8-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16u_C1RSfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16u_C1RSfs_Ctx)

-
Single channel 32-bit floating point to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f16s_C1RSfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f16s_C1RSfs_Ctx)

-
Single channel 32-bit floating point to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f32u_C1RSfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32u](https://docs.nvidia.com/nppdefs.html#c.Npp32u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f32u_C1RSfs_Ctx)

-
Single channel 32-bit floating point to 32-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiConvert_32f32s_C1RSfs_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppRoundMode](https://docs.nvidia.com/nppdefs.html#c.NppRoundMode)eRoundMode, int nScaleFactor,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiConvert_32f32s_C1RSfs_Ctx)

-
Single channel 32-bit floating point to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiConvert to decreased bit depth functions:](https://docs.nvidia.com#group__image__convert__decrease_1commonimageconverttodecreasedbitdepthparameters).

## Scale Bit Depth[](https://docs.nvidia.com#group__image__scale_1image_scale)

Functions for scaling bit depth up or down.

## Scale To Higher Bit Depth[](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1image_scale_to_higher_bit_depth)

Functions for scaling images to higher bit depth.

To map source pixel srcPixelValue to destination pixel dstPixelValue the following equation is used:

```
dstPixelValue = dstMinRangeValue + scaleFactor * (srcPixelValue - srcMinRangeValue)
```

For conversions between integer data types, the entire integer numeric range of the input data type is mapped onto the entire integer numeric range of the output data type.

For conversions to floating point data types the floating point data range is defined by the user supplied floating point values of nMax and nMin which are used as the dstMaxRangeValue and dstMinRangeValue respectively in the scaleFactor and dstPixelValue calculations and also as the saturation values to which output data is clamped.

When converting from floating-point values to integer values, nMax and nMin are used as the srcMaxRangeValue and srcMinRangeValue respectively in the scaleFactor and dstPixelValue calculations. Output values are saturated and clamped to the full output integer pixel value range.

### Common parameters for nppiScale to higher bit depth functions:[](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1CommonImageScaleToHigherBitDepthParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param nMin
-
specifies the minimum saturation value to which every output value will be clamped.

- param nMax
-
specifies the maximum saturation value to which every output value will be clamped.

- param nppStreamCtx
- return
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes), NPP_SCALE_RANGE_ERROR indicates an error condition if nMax <= nMin.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16u_C1R_Ctx)

-
Single channel 8-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16u_C3R_Ctx)

-
Three channel 8-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16u_C4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16u_AC4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16s_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16s_C1R_Ctx)

-
Single channel 8-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16s_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16s_C3R_Ctx)

-
Three channel 8-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16s_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16s_C4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u16s_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u16s_AC4R_Ctx)

-
Four channel 8-bit unsigned to 16-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32s_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32s_C1R_Ctx)

-
Single channel 8-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32s_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32s_C3R_Ctx)

-
Three channel 8-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32s_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32s_C4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit signed conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32s_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32s_AC4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit signed conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32f_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32f_C1R_Ctx)

-
Single channel 8-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32f_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32f_C3R_Ctx)

-
Three channel 8-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32f_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32f_C4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit floating-point conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_8u32f_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_8u32f_AC4R_Ctx)

-
Four channel 8-bit unsigned to 32-bit floating-point conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to higher bit depth functions:](https://docs.nvidia.com#group__image__scale__to__higher__bit__depth_1commonimagescaletohigherbitdepthparameters).

## Scale To Lower Bit Depth[](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1image_scale_to_lower_bit_depth)

Functions for scaling images to lower bit depth.

To map source pixel srcPixelValue to destination pixel dstPixelValue the following equation is used:

```
dstPixelValue = dstMinRangeValue + scaleFactor * (srcPixelValue - srcMinRangeValue)
```

For conversions between integer data types, the entire integer numeric range of the input data type is mapped onto the entire integer numeric range of the output data type.

For conversions to floating point data types the floating point data range is defined by the user supplied floating point values of nMax and nMin which are used as the dstMaxRangeValue and dstMinRangeValue respectively in the scaleFactor and dstPixelValue calculations and also as the saturation values to which output data is clamped.

When converting from floating-point values to integer values, nMax and nMin are used as the srcMaxRangeValue and srcMinRangeValue respectively in the scaleFactor and dstPixelValue calculations. Output values are saturated and clamped to the full output integer pixel value range.

### Common parameters for nppiScale to lower bit depth functions:[](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1CommonImageScaleToLowerBitDepthParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oSizeROI
- param hint
-
algorithm performance or accuracy selector, currently ignored

- param nMin
-
specifies the minimum saturation value to which every output value will be clamped.

- param nMax
-
specifies the maximum saturation value to which every output value will be clamped.

- param nppStreamCtx
- return
-
[Image Data Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1image_data_error_codes),[ROI Related Error Codes](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_error_codes), NPP_SCALE_RANGE_ERROR indicates an error condition if nMax <= nMin.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16u8u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16u8u_C1R_Ctx)

-
Single channel 16-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16u8u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16u8u_C3R_Ctx)

-
Three channel 16-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16u8u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16u8u_C4R_Ctx)

-
Four channel 16-bit unsigned to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16u8u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16u8u_AC4R_Ctx)

-
Four channel 16-bit unsigned to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16s8u_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16s8u_C1R_Ctx)

-
Single channel 16-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16s8u_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16s8u_C3R_Ctx)

-
Three channel 16-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16s8u_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16s8u_C4R_Ctx)

-
Four channel 16-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_16s8u_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_16s8u_AC4R_Ctx)

-
Four channel 16-bit signed to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32s8u_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32s8u_C1R_Ctx)

-
Single channel 32-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32s8u_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32s8u_C3R_Ctx)

-
Three channel 32-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32s8u_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32s8u_C4R_Ctx)

-
Four channel 32-bit signed to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32s8u_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[NppHintAlgorithm](https://docs.nvidia.com/nppdefs.html#c.NppHintAlgorithm)hint,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32s8u_AC4R_Ctx)

-
Four channel 32-bit signed to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32f8u_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32f8u_C1R_Ctx)

-
Single channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32f8u_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32f8u_C3R_Ctx)

-
Three channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32f8u_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32f8u_C4R_Ctx)

-
Four channel 32-bit floating point to 8-bit unsigned conversion.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiScale_32f8u_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMin,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nMax,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiScale_32f8u_AC4R_Ctx)

-
Four channel 32-bit floating point to 8-bit unsigned conversion, not affecting Alpha.

For common parameter descriptions, see

[Common parameters for nppiScale to lower bit depth functions:](https://docs.nvidia.com#group__image__scale__to__lower__bit__depth_1commonimagescaletolowerbitdepthparameters).

## Duplicate Channel[](https://docs.nvidia.com#group__image__duplicate__channel_1image_duplicate_channel)

Functions for duplicating a single channel image in a multiple channel image.

### Common parameters for nppiDup functions:[](https://docs.nvidia.com#group__image__duplicate__channel_1CommonImageDuplicateChannelParameters)

- param pSrc
- param nSrcStep
- param pDst
- param nDstStep
- param oDstSizeROI
-
Size (width, height) of the destination region, i.e. the region that gets filled with data from the source image, source image ROI is assumed to be same as destination image ROI.

- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_8u_C1C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_8u_C1C3R_Ctx)

-
1 channel 8-bit unsigned integer source image duplicated in all 3 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_8u_C1C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_8u_C1C4R_Ctx)

-
1 channel 8-bit unsigned integer source image duplicated in all 4 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_8u_C1AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_8u_C1AC4R_Ctx)

-
1 channel 8-bit unsigned integer source image duplicated in 3 channels of 4 channel destination image with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_16u_C1C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_16u_C1C3R_Ctx)

-
1 channel 16-bit unsigned integer source image duplicated in all 3 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_16u_C1C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_16u_C1C4R_Ctx)

-
1 channel 16-bit unsigned integer source image duplicated in all 4 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_16u_C1AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_16u_C1AC4R_Ctx)

-
1 channel 16-bit unsigned integer source image duplicated in 3 channels of 4 channel destination image with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_16s_C1C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_16s_C1C3R_Ctx)

-
1 channel 16-bit signed integer source image duplicated in all 3 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_16s_C1C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_16s_C1C4R_Ctx)

-
1 channel 16-bit signed integer source image duplicated in all 4 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_16s_C1AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_16s_C1AC4R_Ctx)

-
1 channel 16-bit signed integer source image duplicated in 3 channels of 4 channel destination image with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_32s_C1C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_32s_C1C3R_Ctx)

-
1 channel 32-bit signed integer source image duplicated in all 3 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_32s_C1C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_32s_C1C4R_Ctx)

-
1 channel 32-bit signed integer source image duplicated in all 4 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_32s_C1AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_32s_C1AC4R_Ctx)

-
1 channel 32-bit signed integer source image duplicated in 3 channels of 4 channel destination image with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_32f_C1C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_32f_C1C3R_Ctx)

-
1 channel 32-bit floating point source image duplicated in all 3 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_32f_C1C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_32f_C1C4R_Ctx)

-
1 channel 32-bit floating point source image duplicated in all 4 channels of destination image.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiDup_32f_C1AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oDstSizeROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiDup_32f_C1AC4R_Ctx)

-
1 channel 32-bit floating point source image duplicated in 3 channels of 4 channel destination image with alpha channel unaffected.

For common parameter descriptions, see

[Common parameters for nppiDup functions:](https://docs.nvidia.com#group__image__duplicate__channel_1commonimageduplicatechannelparameters).

## Transpose[](https://docs.nvidia.com#group__image__transpose_1image_transpose)

Functions for transposing images of various types. Like matrix transpose, image transpose is a mirror along the image’s diagonal (upper-left to lower-right corner).

### Common parameters for nppiTranspose functions:[](https://docs.nvidia.com#group__image__transpose_1CommonImageTransposeParameters)

- param pSrc
- param nSrcStep
- param pDst
-
Pointer to the destination ROI.

- param nDstStep
- param oSrcROI
- param nppStreamCtx
- return

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_8u_C1R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_8u_C1R_Ctx)

-
1 channel 8-bit unsigned int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_8u_C3R_Ctx)

-
3 channel 8-bit unsigned int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_8u_C4R_Ctx)

-
4 channel 8-bit unsigned int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_16u_C1R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_16u_C1R_Ctx)

-
1 channel 16-bit unsigned int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_16u_C3R_Ctx)

-
3 channel 16-bit unsigned int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_16u_C4R_Ctx)

-
4 channel 16-bit unsigned int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_16s_C1R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_16s_C1R_Ctx)

-
1 channel 16-bit signed int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_16s_C3R_Ctx)

-
3 channel 16-bit signed int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_16s_C4R_Ctx)

-
4 channel 16-bit signed int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_32s_C1R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_32s_C1R_Ctx)

-
1 channel 32-bit signed int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_32s_C3R_Ctx)

-
3 channel 32-bit signed int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_32s_C4R_Ctx)

-
4 channel 32-bit signed int image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_32f_C1R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_32f_C1R_Ctx)

-
1 channel 32-bit floating point image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_32f_C3R_Ctx)

-
3 channel 32-bit floating point image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiTranspose_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSrcROI,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiTranspose_32f_C4R_Ctx)

-
4 channel 32-bit floating point image transpose.

For common parameter descriptions, see

[Common parameters for nppiTranspose functions:](https://docs.nvidia.com#group__image__transpose_1commonimagetransposeparameters).

## Swap Channels[](https://docs.nvidia.com#group__image__swap__channels_1image_swap_channels)

Functions for swapping and duplicating channels in multiple channel images. The methods support arbitrary permutations of the original channels, including replication and setting one or more channels to a constant value.

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_C3R_Ctx)

-
3 channel 8-bit unsigned integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_C3IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_C3IR_Ctx)

-
3 channel 8-bit unsigned integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_C4C3R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_C4C3R_Ctx)

-
4 channel 8-bit unsigned integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to a 3 channel BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_C4R_Ctx)

-
4 channel 8-bit unsigned integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_C4IR_Ctx([Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_C4IR_Ctx)

-
4 channel 8-bit unsigned integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_C3C4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4], const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_C3C4R_Ctx)

-
3 channel 8-bit unsigned integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [3,2,1,0] converts this to VBGR channel order.**nValue**– (V) Single channel constant value that can be replicated in one or more of the 4 destination channels. nValue is either written or not written to a particular channel depending on the aDstOrder entry for that destination channel. An aDstOrder value of 3 will output nValue to that channel, an aDstOrder value greater than 3 will leave that particular destination channel value unmodified.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_8u_AC4R_Ctx(const[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pSrc, int nSrcStep,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_8u_AC4R_Ctx)

-
4 channel 8-bit unsigned integer source image to 4 channel destination image with destination alpha channel unaffected.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [3,2,1,0] converts this to VBGR channel order. of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to BGRA channel order. In the AC4R case, the alpha channel is always assumed to be channel 3.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_C3R_Ctx)

-
3 channel 16-bit unsigned integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_C3IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_C3IR_Ctx)

-
3 channel 16-bit unsigned integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_C4C3R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_C4C3R_Ctx)

-
4 channel 16-bit unsigned integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to a 3 channel BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_C4R_Ctx)

-
4 channel 16-bit unsigned integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_C4IR_Ctx([Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_C4IR_Ctx)

-
4 channel 16-bit unsigned integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_C3C4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4], const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_C3C4R_Ctx)

-
3 channel 16-bit unsigned integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [3,2,1,0] converts this to VBGR channel order.**nValue**– (V) Single channel constant value that can be replicated in one or more of the 4 destination channels. nValue is either written or not written to a particular channel depending on the aDstOrder entry for that destination channel. An aDstOrder value of 3 will output nValue to that channel, an aDstOrder value greater than 3 will leave that particular destination channel value unmodified.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16u_AC4R_Ctx(const[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pSrc, int nSrcStep,[Npp16u](https://docs.nvidia.com/nppdefs.html#c.Npp16u)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16u_AC4R_Ctx)

-
4 channel 16-bit unsigned integer source image to 4 channel destination image with destination alpha channel unaffected.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to BGRA channel order. In the AC4R case, the alpha channel is always assumed to be channel 3.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_C3R_Ctx)

-
3 channel 16-bit signed integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_C3IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_C3IR_Ctx)

-
3 channel 16-bit signed integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_C4C3R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_C4C3R_Ctx)

-
4 channel 16-bit signed integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to a 3 channel BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_C4R_Ctx)

-
4 channel 16-bit signed integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_C4IR_Ctx([Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_C4IR_Ctx)

-
4 channel 16-bit signed integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_C3C4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4], const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_C3C4R_Ctx)

-
3 channel 16-bit signed integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [3,2,1,0] converts this to VBGR channel order.**nValue**– (V) Single channel constant value that can be replicated in one or more of the 4 destination channels. nValue is either written or not written to a particular channel depending on the aDstOrder entry for that destination channel. An aDstOrder value of 3 will output nValue to that channel, an aDstOrder value greater than 3 will leave that particular destination channel value unmodified.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_16s_AC4R_Ctx(const[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pSrc, int nSrcStep,[Npp16s](https://docs.nvidia.com/nppdefs.html#c.Npp16s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_16s_AC4R_Ctx)

-
4 channel 16-bit signed integer source image to 4 channel destination image with destination alpha channel unaffected.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to BGRA channel order. In the AC4R case, the alpha channel is always assumed to be channel 3.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_C3R_Ctx)

-
3 channel 32-bit signed integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_C3IR_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_C3IR_Ctx)

-
3 channel 32-bit signed integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_C4C3R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_C4C3R_Ctx)

-
4 channel 32-bit signed integer source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to a 3 channel BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_C4R_Ctx)

-
4 channel 32-bit signed integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_C4IR_Ctx([Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_C4IR_Ctx)

-
4 channel 32-bit signed integer in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_C3C4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4], const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_C3C4R_Ctx)

-
3 channel 32-bit signed integer source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [3,2,1,0] converts this to VBGR channel order.**nValue**– (V) Single channel constant value that can be replicated in one or more of the 4 destination channels. nValue is either written or not written to a particular channel depending on the aDstOrder entry for that destination channel. An aDstOrder value of 3 will output nValue to that channel, an aDstOrder value greater than 3 will leave that particular destination channel value unmodified.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32s_AC4R_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc, int nSrcStep,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32s_AC4R_Ctx)

-
4 channel 32-bit signed integer source image to 4 channel destination image with destination alpha channel unaffected.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to BGRA channel order. In the AC4R case, the alpha channel is always assumed to be channel 3.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_C3R_Ctx)

-
3 channel 32-bit floating point source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_C3IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_C3IR_Ctx)

-
3 channel 32-bit floating point in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**– oSizeROI[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [2,1,0] converts this to BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_C4C3R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_C4C3R_Ctx)

-
4 channel 32-bit floating point source image to 3 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to a 3 channel BGR channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_C4R_Ctx)

-
4 channel 32-bit floating point source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_C4IR_Ctx([Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrcDst, int nSrcDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_C4IR_Ctx)

-
4 channel 32-bit floating point in place image.

- Parameters
-
**pSrcDst**–[In-Place Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_pointer).**nSrcDstStep**–[In-Place-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1in_place_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an ARGB image, aDstOrder = [3,2,1,0] converts this to BGRA channel order.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_C3C4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[4], const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)nValue,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_C3C4R_Ctx)

-
3 channel 32-bit floating point source image to 4 channel destination image.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGB image, aDstOrder = [3,2,1,0] converts this to VBGR channel order.**nValue**– (V) Single channel constant value that can be replicated in one or more of the 4 destination channels. nValue is either written or not written to a particular channel depending on the aDstOrder entry for that destination channel. An aDstOrder value of 3 will output nValue to that channel, an aDstOrder value greater than 3 will leave that particular destination channel value unmodified.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns


-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppiSwapChannels_32f_AC4R_Ctx(const[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pSrc, int nSrcStep,[Npp32f](https://docs.nvidia.com/nppdefs.html#c.Npp32f)*pDst, int nDstStep,[NppiSize](https://docs.nvidia.com/nppdefs.html#c.NppiSize)oSizeROI, const int aDstOrder[3],[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppiSwapChannels_32f_AC4R_Ctx)

-
4 channel 32-bit floating point source image to 4 channel destination image with destination alpha channel unaffected.

- Parameters
-
**pSrc**–[Source-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_pointer).**nSrcStep**–[Source-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1source_image_line_step).**pDst**–[Destination-Image Pointer](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_pointer).**nDstStep**–[Destination-Image Line Step](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1destination_image_line_step).**oSizeROI**–[Region-Of-Interest (ROI)](https://docs.nvidia.com/introduction.html#nppi_conventions_lb_1roi_specification).**aDstOrder**– Host memory integer array describing how channel values are permutated. The n-th entry of the array contains the number of the channel that is stored in the n-th channel of the output image. E.g. Given an RGBA image, aDstOrder = [2,1,0] converts this to BGRA channel order. In the AC4R case, the alpha channel is always assumed to be channel 3.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns