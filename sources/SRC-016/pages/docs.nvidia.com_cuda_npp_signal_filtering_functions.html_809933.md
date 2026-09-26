source: https://docs.nvidia.com/cuda/npp/signal_filtering_functions.html

# Signal Filtering Functions[](https://docs.nvidia.com#signal-filtering-functions)

Functions that provide functionality of generating output signal based on the input signal like signal integral, etc.

## Integral[](https://docs.nvidia.com#group__signal__integral_1signal_integral)

Compute the indefinite integral of a given signal. The i-th element is computed to be

Functions

-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsIntegralGetBufferSize_32s(size_t nLength, size_t *hpBufferSize)[](https://docs.nvidia.com#c.nppsIntegralGetBufferSize_32s)

-
Device scratch buffer size (in bytes) for 32s nppsIntegral.

This primitive provides the correct buffer size for nppsIntegral_32s.

- Parameters
-
**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**hpBufferSize**– Required buffer size. Important: hpBufferSize is a*host pointer.*[Scratch Buffer and Host Pointer](https://docs.nvidia.com/introduction.html#general_conventions_lb_1general_scratch_buffer).



-
[NppStatus](https://docs.nvidia.com/nppdefs.html#c.NppStatus)nppsIntegral_32s_Ctx(const[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pSrc,[Npp32s](https://docs.nvidia.com/nppdefs.html#c.Npp32s)*pDst, size_t nLength,[Npp8u](https://docs.nvidia.com/nppdefs.html#c.Npp8u)*pDeviceBuffer,[NppStreamContext](https://docs.nvidia.com/nppdefs.html#c.NppStreamContext)nppStreamCtx)[](https://docs.nvidia.com#c.nppsIntegral_32s_Ctx)

-
Compute cumulative sum of 32-bit signed integer signal.

- Parameters
-
**pSrc**–[Source Signal Pointer](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1source_signal_pointer).**pDst**– Pointer to the output result.**nLength**–[Signal Length](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_specification).**pDeviceBuffer**– Pointer to the required device memory allocation.**nppStreamCtx**–[Application Managed Stream Context](https://docs.nvidia.com/nppdefs.html#structnppstreamcontext_1application_managed_stream_context).

- Returns
-
[Signal Data Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1signal_data_error_codes),[Length Related Error Codes](https://docs.nvidia.com/introduction.html#npps_conventions_lb_1length_error_codes).